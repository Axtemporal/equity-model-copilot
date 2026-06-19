"""Analyst panel for the assumption-session chat.

When the analyst suggests something, a panel of specialised agents responds — each from its own
angle, all by default (the analyst can address just one by naming it). Checker01 also computes the
proposed per-period values (and does the sanity/scale check the study flagged as critical); the
others argue, verify and source. Agents run as independent Claude calls in parallel threads.
"""
from __future__ import annotations

import json
import re
import threading

from .advisor import DEFAULT_MODEL, claude_available, premise_prompt, run_claude
from .sector_knowledge import card_excerpt

_COMMON = (
    "CONVENÇÃO DE UNIDADE: campos com unidade '%' guardam DECIMAL (52% = 0,52). Colunas anuais de "
    "linhas de FLUXO (receita, capex, D&A) são ~4x o trimestral; taxas (ARPU R$/mo, margem %, "
    "alíquota) NÃO multiplicam por 4. Se houver CONHECIMENTO SETORIAL (method card) no prompt, "
    "FUNDAMENTE-SE nele e cite-o; nunca invente fonte. Não é recomendação de investimento. "
    "Seja conciso (2 a 4 frases)."
)

AGENTS = {
    "checker": {
        "name": "Checker01",
        "avatar": "🔍",
        "system": (
            "Você é Checker01, o analista de SANITY-CHECK. O analista sugeriu um ajuste de premissa. "
            "(1) CALCULE os valores resultantes por período (declínio/crescimento/% de outra linha/valor fixo), "
            "respeitando a convenção de unidade. (2) Cheque a sanidade: escala (decimal vs %), sinal, magnitude "
            "plausível, continuidade (sem saltos absurdos entre períodos de mesma frequência) e faixas razoáveis "
            "(ARPU>0; margem em [0,1]; alíquota em [0,~0,45]). Aponte qualquer valor implausível ou seed "
            "não-representativo. " + _COMMON + " Responda SOMENTE em JSON: "
            '{"reply": "<seu parecer curto>", "proposal": {"values": {"<período>": <número>, ...}, '
            '"method": "<método>", "source": "", "source_date": "", "rationale": "<racional>"}}. '
            'Use "proposal": null se não houver mudança numérica.'
        ),
    },
    "verifier": {
        "name": "Verifier01",
        "avatar": "⚖️",
        "system": (
            "Você é Verifier01, o analista que VERIFICA A ARGUMENTAÇÃO. A lógica do analista é consistente? "
            "O método casa com a linha? Os números são internamente coerentes (ex.: o declínio implícito bate "
            "com a curva; a margem implica um opex coerente; a soma das partes fecha)? Aponte furos lógicos ou "
            "inconsistências, ou confirme que fecha. " + _COMMON + ' Responda SOMENTE em JSON: {"reply": "<parecer>"}.'
        ),
    },
    "counter": {
        "name": "Counter01",
        "avatar": "🥊",
        "system": (
            "Você é Counter01, o ADVOGADO DO DIABO. Contra-argumente a sugestão: por que ela pode estar otimista "
            "ou pessimista demais? Que evidência setorial/histórica aponta o contrário? Qual o cenário oposto "
            "(bull/bear)? Seja específico e construtivo, não só cético. " + _COMMON +
            ' Responda SOMENTE em JSON: {"reply": "<contra-argumento>"}.'
        ),
    },
    "supporter": {
        "name": "Supporter01",
        "avatar": "📚",
        "system": (
            "Você é Supporter01, que REFORÇA A TESE com fundamentação. Que fontes públicas, dados setoriais, "
            "histórico da empresa ou benchmarks de pares sustentam essa premissa? Cite fontes verificáveis "
            "(releases, ANP/CVM, curvas forward, consenso) — rotule estimativa como estimativa, nunca invente "
            "dado reportado. " + _COMMON + ' Responda SOMENTE em JSON: '
            '{"reply": "<fundamentação>", "source": "<fonte ou vazio>", "source_date": "<AAAA-MM ou vazio>"}.'
        ),
    },
}

ORDER = ["checker", "verifier", "counter", "supporter"]


def select_agents(message: str) -> list[str]:
    """Which agents the analyst is addressing — those named, else all of them."""
    low = message.lower()
    picked = [k for k in ORDER if AGENTS[k]["name"].lower() in low or f"@{k}" in low]
    return picked or ORDER


def _parse_agent(raw: str) -> dict:
    match = re.search(r"\{.*\}", raw or "", re.S)
    if not match:
        return {"reply": raw.strip() or None}
    try:
        data = json.loads(match.group(0))
    except Exception:
        return {"reply": raw.strip() or None}
    out = {"reply": data.get("reply") or raw.strip()}
    proposal = data.get("proposal")
    if proposal and isinstance(proposal.get("values"), dict):
        proposal["values"] = {str(k): float(v) for k, v in proposal["values"].items()
                              if isinstance(v, (int, float))}
        out["proposal"] = proposal if proposal["values"] else None
    if data.get("source"):
        out["source"] = data["source"]
    if data.get("source_date"):
        out["source_date"] = data["source_date"]
    return out


def run_panel(user_message: str, *, line: dict, all_lines: list[dict],
              chat_history: list[dict] | None = None, agents: list[str] | None = None,
              model: str | None = None, sector: str | None = None) -> dict:
    """Run the requested analysts (default all) in parallel. Returns {'available', 'responses'}.

    When `sector` is given, the relevant method-card excerpt is injected so the panel grounds its
    proposal in the sector knowledge base (Stage 3) rather than in model memory."""
    if not claude_available():
        return {"available": False, "responses": []}
    keys = agents or ORDER
    grounding = card_excerpt(sector, line["line_item"]) if sector else ""
    prompt = premise_prompt(user_message, line, all_lines, chat_history, grounding)
    results: dict[str, dict] = {}

    def _worker(key: str):
        text, error = run_claude(AGENTS[key]["system"], prompt, model or DEFAULT_MODEL)
        if not text and error:
            results[key] = {"reply": f"(falhou: {error})"}
        else:
            results[key] = _parse_agent(text)

    threads = [threading.Thread(target=_worker, args=(k,)) for k in keys]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    responses = [{"agent": k, **results[k]} for k in keys if k in results]
    return {"available": True, "responses": responses}
