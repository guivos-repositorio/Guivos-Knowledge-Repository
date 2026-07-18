from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BRANCH = "agent/captura-contexto-ciclo-de-vida"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_once(content: str, old: str, new: str, label: str) -> str:
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return content.replace(old, new, 1)


def section(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        raise RuntimeError(f"section anchors missing: {start} / {end}")
    return text.split(start, 1)[1].split(end, 1)[0]


def validate_contract() -> None:
    path = "docs/product-architecture/pas-001-captura-de-contexto-ciclo-de-vida.md"
    text = read(path)
    if "id: PAS-001-CC-LIFECYCLE-001" not in text or "version: 1.0.0" not in text:
        raise RuntimeError("contract metadata is invalid")
    numbers = [int(value) for value in re.findall(r"^# (\d+)\.", text, re.MULTILINE)]
    expected = list(range(4566, 4669))
    if numbers != expected:
        raise RuntimeError(f"section sequence mismatch: {numbers[:3]} ... {numbers[-3:] if numbers else []}")
    forbidden = section(text, "# 4661. Comportamentos proibidos", "# 4662. Critérios de aceite")
    criteria = section(text, "# 4662. Critérios de aceite", "# 4663. Relação com o PAS-001 0.5.0")
    forbidden_count = len(re.findall(r"^\d+\. ", forbidden, re.MULTILINE))
    criteria_count = len(re.findall(r"^\d+\. ", criteria, re.MULTILINE))
    if forbidden_count != 34:
        raise RuntimeError(f"expected 34 prohibited behaviors, found {forbidden_count}")
    if criteria_count != 68:
        raise RuntimeError(f"expected 68 acceptance criteria, found {criteria_count}")


def update_product_architecture() -> None:
    path = "docs/product-architecture/index.md"
    text = read(path)
    text = replace_once(text, "version: 1.22.0", "version: 1.23.0", "product architecture version")
    anchor = "A Capacidade 01 permanece `Substantially complete` e deverá ser concluída por `PAS-001-CC-LIFECYCLE-001`, `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001`."
    replacement = anchor + "\n\n### Capacidade 01 — Captura de Contexto\n\n`PAS-001-CC-LIFECYCLE-001 1.0.0` conclui a etapa `1 de 3` do fechamento formal da Capacidade 01, consolidando o `Registro de Captura de Contexto`, sessão, entradas, transcrição, interpretação, síntese, confirmação, autorização, persistência temporária, correção, limitação, contestação, revogação, acessibilidade, idempotência, ordenação, concorrência, reconstrução e falha segura.\n\nA capacidade permanece `Substantially complete`; `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001` continuam obrigatórios antes da auditoria final de prontidão."
    text = replace_once(text, anchor, replacement, "product architecture Capability 01 anchor")
    write(path, text)


def update_roadmap() -> None:
    path = "docs/roadmap.md"
    text = read(path)
    text = replace_once(text, "version: 11.3.0", "version: 11.4.0", "roadmap version")
    text = replace_once(
        text,
        "- **Reconciliação vigente:** `PAS-001-RECON-001 1.0.0`.",
        "- **Reconciliação vigente:** `PAS-001-RECON-001 1.0.0`.\n- **Extensão vigente da Capacidade 01:** `PAS-001-CC-LIFECYCLE-001 1.0.0`, etapa `1 de 3`.",
        "roadmap lifecycle state",
    )
    text = replace_once(
        text,
        "- **Lacuna bloqueante:** ausência de fechamento funcional formal da Capacidade 01 — Captura de Contexto.",
        "- **Lacuna bloqueante:** permanecem `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001` para o fechamento funcional formal da Capacidade 01.",
        "roadmap blocking gap",
    )
    old_direction = "A reconciliação do `PAS-001 — Guivos Journey` foi concluída por `PAS-001-RECON-001 1.0.0`. O próximo trabalho deverá consolidar o **Ciclo de Vida e os Estados Funcionais da Capacidade 01 — Captura de Contexto**, sem avançar diretamente para `PAS-001 1.0.0`."
    new_direction = "O ciclo de vida e os estados funcionais da Capacidade 01 foram consolidados por `PAS-001-CC-LIFECYCLE-001 1.0.0`. O próximo trabalho deverá consolidar os **Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto**, mantendo o `PAS-001` em `Draft 0.5.0` e a prontidão como `Not ready`."
    text = replace_once(text, old_direction, new_direction, "roadmap direction")
    heading = "## Capacidades concluídas"
    block = "## Capacidade 01 — Fechamento formal em andamento\n\n`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou a primeira das três etapas obrigatórias, com 103 seções normativas, 34 comportamentos proibidos e 68 critérios de aceite.\n\nA Capacidade 01 permanece `Substantially complete`. Eventos, integrações, KPIs, guardrails, cenários e contrato final permanecem necessários para a conclusão funcional.\n\n"
    text = replace_once(text, heading, block + heading, "roadmap Capability 01 section")
    write(path, text)


def update_board() -> None:
    path = "docs/project/knowledge-board.md"
    text = read(path)
    text = replace_once(text, "version: 11.3.0", "version: 11.4.0", "board version")
    row = "| PAS-001-RECON-001 | Active 1.0.0 | Reconciliar autoridade, supersessão e prontidão do Journey |"
    text = replace_once(text, row, row + "\n| PAS-001-CC-LIFECYCLE-001 | Active 1.0.0 | Consolidar ciclo de vida e estados funcionais da Captura de Contexto |", "board asset row")
    text = replace_once(
        text,
        "| Lacuna bloqueante | Fechamento funcional formal da Capacidade 01 — Captura de Contexto |",
        "| Lacuna bloqueante | Eventos/integrações e contrato final da Capacidade 01 ainda pendentes |",
        "board blocking gap",
    )
    text = replace_once(
        text,
        "| Extensões projetadas da Capacidade 01 | `PAS-001-CC-LIFECYCLE-001`, `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001` |",
        "| Extensão vigente da Capacidade 01 | `PAS-001-CC-LIFECYCLE-001 1.0.0`, etapa `1 de 3` |\n| Extensões restantes da Capacidade 01 | `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001` |",
        "board extension rows",
    )
    text = replace_once(
        text,
        "| Frente ativa | Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto |",
        "| Frente ativa | Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto |",
        "board active front",
    )
    text = replace_once(
        text,
        "| Foco imediato | Criar `PAS-001-CC-LIFECYCLE-001` e iniciar o fechamento formal da Capacidade 01 |",
        "| Foco imediato | Criar `PAS-001-CC-EVENT-INTEGRATION-001` e concluir a etapa `2 de 3` |",
        "board immediate focus",
    )
    text = replace_once(
        text,
        "| 01 — Captura de Contexto | Substantially complete | Fechamento formal requerido; ciclo de vida, eventos/integrações e contrato final projetados |",
        "| 01 — Captura de Contexto | Substantially complete — etapa 1 de 3 | Ciclo de vida consolidado; eventos/integrações e contrato final permanecem pendentes |",
        "board Capability 01 state",
    )
    write(path, text)


def update_matrix() -> None:
    path = "docs/project/canonical-consolidation-matrix.md"
    text = read(path)
    text = replace_once(text, "version: 1.22.0", "version: 1.23.0", "matrix version")
    text = replace_once(
        text,
        "| Captura de Contexto | Refinar | `Substantially complete`; requer fechamento formal por três extensões |",
        "| Captura de Contexto | Refinar | `Substantially complete`; etapa `1 de 3` concluída por `PAS-001-CC-LIFECYCLE-001 1.0.0` |",
        "matrix Capture Context row",
    )
    anchor = "| Sessão de Captura de Contexto | Refinar | Ciclo próprio, estados independentes, encerramento e falha segura |"
    additions = "\n| Ciclo de Vida da Captura de Contexto | Manter | `PAS-001-CC-LIFECYCLE-001 1.0.0` governa agregado, sessão, estados, transições, canais, transcrição, interpretação, síntese, confirmação, autorização e persistência |\n| Estado funcional da sessão de captura | Manter | `Not initiated`, `Explaining purpose`, `Awaiting participant`, `Capturing`, `Paused`, `Processing`, `Reflecting understanding`, `Awaiting review`, `Partially confirmed`, `Confirmed`, `Correction requested`, `Limited`, `Temporary`, `Abandoned`, `Expired`, `Contested`, `Revoked`, `Closed` ou `Failed` |\n| Entrada original de contexto | Manter | Permanece distinta de transcrição, interpretação, síntese e confirmação |\n| Confirmação suficiente da captura | Refinar | Confirmação delimitada à finalidade; não representa verdade absoluta, perfil integral ou autorização universal |\n| Etapa de fechamento da Capacidade 01 | Manter | Ciclo de vida concluído; eventos/integrações e contrato final permanecem obrigatórios |"
    text = replace_once(text, anchor, anchor + additions, "matrix lifecycle concepts")
    write(path, text)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_once(
        text,
        "- **Reconciliação vigente:** PAS-001-RECON-001 1.0.0",
        "- **Reconciliação vigente:** PAS-001-RECON-001 1.0.0\n- **Extensão vigente da Capacidade 01:** PAS-001-CC-LIFECYCLE-001 1.0.0 — etapa 1 de 3",
        "README lifecycle status",
    )
    text = replace_once(
        text,
        "- **Próxima frente:** Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto",
        "- **Próxima frente:** Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto",
        "README next front",
    )
    heading = "## Capacidade 02 — Contexto Vivo"
    block = "## Capacidade 01 — Captura de Contexto\n\n`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou a etapa `1 de 3` do fechamento formal, com `Registro de Captura de Contexto`, sessão, estados independentes, transições, entradas, canais, transcrição, interpretação, síntese, confirmação, autorização, persistência temporária, correção, limitação, contestação, revogação, acessibilidade, idempotência, ordenação, concorrência, reconstrução e falha segura.\n\nA capacidade permanece **Substantially complete**. Eventos/integrações e o contrato final ainda são necessários.\n\n"
    text = replace_once(text, heading, block + heading, "README Capability 01 section")
    write(path, text)


def update_docs_index() -> None:
    path = "docs/index.md"
    text = read(path)
    text = replace_once(
        text,
        "- `PAS-001-RECON-001 1.0.0` como reconciliação normativa vigente;",
        "- `PAS-001-RECON-001 1.0.0` como reconciliação normativa vigente;\n- `PAS-001-CC-LIFECYCLE-001 1.0.0` como primeira extensão de fechamento da Capacidade 01, etapa `1 de 3`;",
        "docs index lifecycle status",
    )
    text = replace_once(
        text,
        "Consolidar o **Ciclo de Vida e os Estados Funcionais da Capacidade 01 — Captura de Contexto**, iniciando seu fechamento formal por `PAS-001-CC-LIFECYCLE-001`.",
        "Consolidar os **Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto** por `PAS-001-CC-EVENT-INTEGRATION-001`, preservando o estado `Substantially complete` até o contrato final.",
        "docs index mission",
    )
    link_anchor = "- [Reconciliação e Prontidão do Guivos Journey](product-architecture/pas-001-guivos-journey-reconciliacao-fechamento.md)"
    link = "- [Ciclo de Vida e Estados Funcionais da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-ciclo-de-vida.md)"
    text = replace_once(text, link_anchor, link_anchor + "\n" + link, "docs index quick link")
    text = replace_once(
        text,
        "| 01 — Captura de Contexto | Substantially complete |",
        "| 01 — Captura de Contexto | Substantially complete — etapa 1 de 3 |",
        "docs index Capability 01 state",
    )
    text = replace_once(
        text,
        "Retomar no **Ciclo de Vida e Estados Funcionais da Capacidade 01 — Captura de Contexto**.",
        "Retomar nos **Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto**.",
        "docs index resume point",
    )
    write(path, text)


def update_mkdocs() -> None:
    path = "mkdocs.yml"
    text = read(path)
    anchor = "      - PAS-001-RECON-001 — Reconciliação e Prontidão: product-architecture/pas-001-guivos-journey-reconciliacao-fechamento.md"
    line = "      - PAS-001-CC-LIFECYCLE-001 — Ciclo de Vida da Captura de Contexto: product-architecture/pas-001-captura-de-contexto-ciclo-de-vida.md"
    text = replace_once(text, anchor, anchor + "\n" + line, "mkdocs Capture Context nav")
    write(path, text)


def update_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    anchor = "## 0.50.0 — PAS-001 Reconciliation and Readiness"
    entry = """## 0.51.0 — Capture Context Lifecycle and Functional States

- Criação de `PAS-001-CC-LIFECYCLE-001 — Regras do Ciclo de Vida e Estados Funcionais da Captura de Contexto`, versão `1.0.0`.
- Registro do documento como primeira extensão complementar de fechamento da Capacidade 01.
- Consolidação do `Registro de Captura de Contexto` como agregado funcional permanente.
- Consolidação de sessão, entradas, canais, transcrição, interpretação, síntese, confirmação, autorização, persistência temporária, correção, limitação, remoção, contestação, revogação e encerramento.
- Definição de 14 dimensões de estado independentes e 19 estados funcionais da sessão.
- Definição de transições fundamentais e transições proibidas.
- Preservação da entrada original e distinção entre captura, transcrição, interpretação, síntese e confirmação.
- Proteção de voz, texto, fluxo guiado, arquivos, dispositivos compartilhados, informações sensíveis, crianças, adolescentes e terceiros.
- Consolidação de acessibilidade, idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, reconstrução, observabilidade, auditoria e falha segura.
- Registro de 34 comportamentos proibidos e 68 critérios de aceite.
- Manutenção da Capacidade 01 como `Substantially complete`, com etapa `1 de 3` concluída.
- Manutenção do `PAS-001` em `Draft 0.5.0` e da prontidão `Not ready — Capability 01 closure required`.
- Atualização da Arquitetura de Produtos para `1.23.0`.
- Atualização do Roadmap e do Knowledge Board para `11.4.0`.
- Atualização da Matriz de Consolidação Canônica para `1.23.0`.
- Atualização do README, da página inicial e da navegação do MkDocs.
- Definição de Eventos e Integrações Funcionais da Capacidade 01 como próximo ponto exato.


"""
    text = replace_once(text, anchor, entry + anchor, "changelog insertion")
    write(path, text)


def validate_outputs() -> None:
    expectations = {
        "docs/product-architecture/index.md": ["version: 1.23.0", "PAS-001-CC-LIFECYCLE-001 1.0.0", "etapa `1 de 3`"],
        "docs/roadmap.md": ["version: 11.4.0", "PAS-001-CC-LIFECYCLE-001 1.0.0", "Eventos e Integrações Funcionais"],
        "docs/project/knowledge-board.md": ["version: 11.4.0", "PAS-001-CC-LIFECYCLE-001 | Active 1.0.0", "etapa 1 de 3"],
        "docs/project/canonical-consolidation-matrix.md": ["version: 1.23.0", "Ciclo de Vida da Captura de Contexto", "Entrada original de contexto"],
        "README.md": ["PAS-001-CC-LIFECYCLE-001 1.0.0 — etapa 1 de 3", "Eventos e Integrações Funcionais"],
        "docs/index.md": ["PAS-001-CC-LIFECYCLE-001 1.0.0", "Substantially complete — etapa 1 de 3"],
        "mkdocs.yml": ["PAS-001-CC-LIFECYCLE-001 — Ciclo de Vida da Captura de Contexto"],
        "CHANGELOG.md": ["## 0.51.0 — Capture Context Lifecycle and Functional States", "34 comportamentos proibidos", "68 critérios de aceite"],
    }
    for path, values in expectations.items():
        text = read(path)
        for value in values:
            if value not in text:
                raise RuntimeError(f"{path}: missing validation value {value!r}")
    if "version: 0.5.0" not in read("docs/product-architecture/pas-001-guivos-journey.md"):
        raise RuntimeError("PAS-001 version changed unexpectedly")
    if "Not ready — Capability 01 closure required" not in read("docs/roadmap.md"):
        raise RuntimeError("readiness changed unexpectedly")


def git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, text=True, capture_output=True)


def commit_and_cleanup() -> None:
    workflow = ROOT / ".github/workflows/sync-cc-lifecycle.yml"
    script = ROOT / "scripts/sync_cc_lifecycle.py"
    if workflow.exists():
        workflow.unlink()
    if script.exists():
        script.unlink()
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    git("add", "-A")
    status = git("status", "--porcelain").stdout.strip()
    if not status:
        raise RuntimeError("synchronizer produced no changes")
    git("commit", "-m", "synchronize Capture Context lifecycle canon")
    git("push", "origin", f"HEAD:{BRANCH}")


def main() -> None:
    validate_contract()
    update_product_architecture()
    update_roadmap()
    update_board()
    update_matrix()
    update_readme()
    update_docs_index()
    update_mkdocs()
    update_changelog()
    validate_outputs()
    commit_and_cleanup()


if __name__ == "__main__":
    main()
