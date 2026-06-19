"""Live Claude bridge for the assumption-session chat (Claude Agent SDK, host auth, no API key).

Lets the analyst discuss a premise in natural language — "produção do Charlie declina 1,5% ao ano",
"que seja 60% da produção do Bravo", "qual a sua visão para o Brent?" — and have Claude reason about
it, compute the per-period values, and return a structured proposal with a rationale and sources.
`_run_claude` is the shared single-call primitive (used by discuss, reflect, and the analyst panel).
Falls back cleanly (reply=None) when the Agent SDK is unavailable.
"""
from __future__ import annotations

import json
import os
import re
import threading

DEFAULT_MODEL = os.environ.get("EMC_MODEL", "claude-sonnet-4-6")

_SYSTEM = """Você é um copiloto de modelagem de equities (research de ações) ajudando um analista a definir UMA premissa de um modelo financeiro, linha a linha, com aprovação humana.

O analista vai discutir ou propor um ajuste em linguagem natural. Pense de verdade sobre a mensagem dele:
- Se ele descrever uma regra (taxa de declínio/crescimento X% ao ano, valor fixo, % da produção/receita de outra linha, convergência a um nível), CALCULE o valor resultante para CADA período listado, na ordem dada.
- CONVENÇÃO DE UNIDADE (importante): campos com unidade "%" guardam DECIMAL (52% = 0,52; 34% = 0,34). Colunas anuais de linhas de FLUXO (receita, capex, D&A) são ~4x o trimestral; mas TAXAS (ARPU em R$/mo, margem %, alíquota) NÃO multiplicam por 4.
- Se ele pedir sua visão, proponha um número com raciocínio. Se for só conversa, responda sem mudar valores.

Dê sempre um racional rico: método, lógica econômica/setorial, e fontes públicas quando fizer sentido (rotule estimativa como estimativa; não é recomendação de investimento).

Responda SOMENTE com um objeto JSON válido, sem texto fora dele:
{"reply": "<resposta ao analista, em português>",
 "proposal": {"values": {"<período>": <número>, ...}, "method": "<método curto>", "source": "<fonte ou vazio>", "source_date": "<AAAA-MM ou vazio>", "rationale": "<racional detalhado>"}}
Use "proposal": null quando não houver mudança de valor. Os períodos em "values" devem ser exatamente os rótulos fornecidos."""

_REFLECT_SYSTEM = """Você é um copiloto de modelagem de equities. Resuma a sessão de premissas que o analista acabou de concluir em 3 a 5 frases, em português: destaque as decisões mais relevantes, aponte tensões ou riscos entre premissas (ex.: declínio otimista vs. capex, premissas inconsistentes entre linhas), e o que valeria revisar. Não faça recomendação de investimento. Responda em texto corrido, sem JSON."""


def claude_available() -> bool:
    try:
        import claude_agent_sdk  # noqa: F401
        return True
    except Exception:
        return False


def _context(line: dict, all_lines: list[dict]) -> tuple[str, str]:
    current = ", ".join(f"{p}={v}" for p, v in line["periods"])
    others = []
    for other in all_lines:
        if other["line_item"] == line["line_item"]:
            continue
        vals = ", ".join(f"{p}={v}" for p, v in other["periods"] if v is not None)
        if vals:
            others.append(f"- {other['line_item']} ({other.get('unit', '')}): {vals}")
    return current, "\n".join(others[:40])


def premise_prompt(user_message: str, line: dict, all_lines: list[dict],
                   chat_history: list[dict] | None = None, grounding: str = "") -> str:
    current, others = _context(line, all_lines)
    history = "\n".join(f"{m['role']}: {m['text']}" for m in (chat_history or [])[-8:])
    ground_block = (
        "CONHECIMENTO SETORIAL (method card — FUNDAMENTE sua proposta nisto, cite a card; "
        "se a card não cobrir, diga que é estimativa e não invente fonte):\n"
        f"{grounding}\n\n" if grounding else ""
    )
    return (
        f"Premissa atual: {line['line_item']} ({line.get('unit', '')}).\n"
        f"Valores atuais por período (em ordem): {current}\n"
        f"Outras linhas do modelo (para referência cruzada):\n{others or '(nenhuma)'}\n\n"
        f"{ground_block}"
        f"Conversa até agora:\n{history or '(início)'}\n\n"
        f"Mensagem do analista: {user_message}"
    )


def run_claude(system: str, prompt: str, model: str | None = None) -> tuple[str, str | None]:
    """One Claude call via the Agent SDK in an isolated thread. Returns (text, error_or_None)."""
    if not claude_available():
        return "", "claude_agent_sdk indisponível"

    chunks: list[str] = []
    failure: dict = {}

    def _worker():
        try:
            import anyio
            from claude_agent_sdk import ClaudeAgentOptions, query

            options = ClaudeAgentOptions(max_turns=1, system_prompt=system, model=model or DEFAULT_MODEL)

            async def _run():
                async for message in query(prompt=prompt, options=options):
                    content = getattr(message, "content", None)
                    if content:
                        for block in (content if isinstance(content, list) else [content]):
                            text = getattr(block, "text", None)
                            if text:
                                chunks.append(text)

            anyio.run(_run)
        except Exception as exc:  # noqa: BLE001
            failure["error"] = repr(exc)[:200]

    thread = threading.Thread(target=_worker)
    thread.start()
    thread.join()
    text = "".join(chunks).strip()
    if not text and failure:
        return "", failure["error"]
    return text, None


def _parse(text: str) -> dict:
    match = re.search(r"\{.*\}", text or "", re.S)
    if not match:
        return {"reply": (text or None), "proposal": None}
    try:
        data = json.loads(match.group(0))
    except Exception:
        return {"reply": text, "proposal": None}
    proposal = data.get("proposal")
    if proposal and isinstance(proposal.get("values"), dict):
        proposal["values"] = {str(k): float(v) for k, v in proposal["values"].items()
                              if isinstance(v, (int, float))}
        if not proposal["values"]:
            proposal = None
    else:
        proposal = None
    return {"reply": data.get("reply") or text, "proposal": proposal}


def discuss(user_message: str, *, line: dict, all_lines: list[dict],
            chat_history: list[dict] | None = None, model: str | None = None,
            grounding: str = "") -> dict:
    """Discuss a premise with Claude. Returns {'reply': str|None, 'proposal': dict|None, 'error'?}."""
    if not claude_available():
        return {"reply": None, "proposal": None}
    prompt = premise_prompt(user_message, line, all_lines, chat_history, grounding)
    text, error = run_claude(_SYSTEM, prompt, model)
    if not text and error:
        return {"reply": None, "proposal": None, "error": error}
    return _parse(text)


def reflect_on_session(decisions: list[dict], model: str | None = None) -> str | None:
    """A short reflection on the concluded session. Returns None if the bridge is unavailable."""
    if not claude_available() or not decisions:
        return None
    lines = "\n".join(
        f"- {d.get('line_item')}: {'; '.join(f'{p}={v}' for p, v in (d.get('values') or {}).items())}"
        f" [{d.get('method', '')}]"
        for d in decisions
    )
    text, _error = run_claude(_REFLECT_SYSTEM, f"Premissas aprovadas nesta sessão:\n{lines}\n\nEscreva a reflexão.", model)
    return text or None
