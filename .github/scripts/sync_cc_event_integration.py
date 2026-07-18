from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs/product-architecture/pas-001-captura-de-contexto-eventos-integracoes-funcionais.md"
WORKFLOW = ROOT / ".github/workflows/sync-cc-event-integration.yml"
SCRIPT = ROOT / ".github/scripts/sync_cc_event_integration.py"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {count}")
    return text.replace(old, new, 1)


def section(text: str, start: int, end: int) -> str:
    pattern = rf"(?ms)^# {start}\. .*?(?=^# {end}\.)"
    match = re.search(pattern, text)
    if not match:
        raise RuntimeError(f"section {start}-{end} not found")
    return match.group(0)


def validate_normative_document() -> None:
    text = DOC.read_text(encoding="utf-8")
    numbers = [int(value) for value in re.findall(r"(?m)^# (\d+)\.", text)]
    expected = list(range(4669, 4759))
    if numbers != expected:
        raise RuntimeError(f"section sequence mismatch: {numbers[:3]}...{numbers[-3:] if numbers else []}")

    prohibited = re.findall(r"(?m)^\d+\. ", section(text, 4753, 4754))
    criteria = re.findall(r"(?m)^\d+\. ", section(text, 4754, 4755))
    families = [number for number in numbers if 4696 <= number <= 4715]
    if len(prohibited) != 42:
        raise RuntimeError(f"expected 42 prohibited behaviors, found {len(prohibited)}")
    if len(criteria) != 80:
        raise RuntimeError(f"expected 80 acceptance criteria, found {len(criteria)}")
    if len(families) != 20:
        raise RuntimeError(f"expected 20 event families, found {len(families)}")
    required = [
        "PAS-001-CC-EVENT-INTEGRATION-001",
        "Substantially complete — final functional contract required",
        "etapa `2 de 3`",
        "PAS-001-CC-CONTRACT-001",
        "Not ready",
    ]
    for value in required:
        if value not in text:
            raise RuntimeError(f"missing required normative value: {value}")


def sync_product_architecture() -> None:
    path = "docs/product-architecture/index.md"
    text = read(path)
    text = replace_once(text, "version: 1.23.0", "version: 1.24.0", path)
    old = """`PAS-001-CC-LIFECYCLE-001 1.0.0` conclui a etapa `1 de 3` do fechamento formal da Capacidade 01, consolidando o `Registro de Captura de Contexto`, sessão, entradas, transcrição, interpretação, síntese, confirmação, autorização, persistência temporária, correção, limitação, contestação, revogação, acessibilidade, idempotência, ordenação, concorrência, reconstrução e falha segura.

A capacidade permanece `Substantially complete`; `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001` continuam obrigatórios antes da auditoria final de prontidão."""
    new = """`PAS-001-CC-LIFECYCLE-001 1.0.0` concluiu a etapa `1 de 3`, consolidando o `Registro de Captura de Contexto`, sessão, estados, transições, entradas, transcrição, interpretação, síntese, confirmação, autorização, persistência temporária, correção, contestação, reconstrução e falha segura.

`PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` conclui a etapa `2 de 3`, consolidando estrutura comum versionada, 20 famílias de eventos, contrato funcional comum de integração, produtores, consumidores, recortes, correção compensatória, revogação propagada, sincronização, prevenção de ciclos, idempotência, ordenação, concorrência, explicabilidade e auditoria.

A capacidade permanece `Substantially complete`; somente `PAS-001-CC-CONTRACT-001` continua obrigatório antes da auditoria final de prontidão."""
    text = replace_once(text, old, new, path)
    write(path, text)


def sync_roadmap() -> None:
    path = "docs/roadmap.md"
    text = read(path)
    text = replace_once(text, "version: 11.4.0", "version: 11.5.0", path)
    text = replace_once(
        text,
        "- **Extensão vigente da Capacidade 01:** `PAS-001-CC-LIFECYCLE-001 1.0.0`, etapa `1 de 3`.",
        "- **Extensões vigentes da Capacidade 01:** `PAS-001-CC-LIFECYCLE-001 1.0.0` e `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0`, etapa `2 de 3`.",
        path,
    )
    text = replace_once(
        text,
        "- **Lacuna bloqueante:** permanecem `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001` para o fechamento funcional formal da Capacidade 01.",
        "- **Lacuna bloqueante:** permanece `PAS-001-CC-CONTRACT-001` para o fechamento funcional formal da Capacidade 01.",
        path,
    )
    text = replace_once(
        text,
        "O ciclo de vida e os estados funcionais da Capacidade 01 foram consolidados por `PAS-001-CC-LIFECYCLE-001 1.0.0`. O próximo trabalho deverá consolidar os **Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto**, mantendo o `PAS-001` em `Draft 0.5.0` e a prontidão como `Not ready`.",
        "Os eventos e as integrações funcionais da Capacidade 01 foram consolidados por `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0`. O próximo trabalho deverá consolidar os **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto**, mantendo o `PAS-001` em `Draft 0.5.0` e a prontidão como `Not ready`.",
        path,
    )
    old = """`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou a primeira das três etapas obrigatórias, com 103 seções normativas, 34 comportamentos proibidos e 68 critérios de aceite.

A Capacidade 01 permanece `Substantially complete`. Eventos, integrações, KPIs, guardrails, cenários e contrato final permanecem necessários para a conclusão funcional."""
    new = """`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou a primeira etapa. `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` consolidou a segunda etapa, com 90 seções normativas, 20 famílias de eventos, 42 comportamentos proibidos e 80 critérios de aceite.

A Capacidade 01 permanece `Substantially complete`, etapa `2 de 3`. KPIs, guardrails, baseline, cenários e contrato final permanecem necessários para a conclusão funcional."""
    text = replace_once(text, old, new, path)
    write(path, text)


def sync_board() -> None:
    path = "docs/project/knowledge-board.md"
    text = read(path)
    text = replace_once(text, "version: 11.4.0", "version: 11.5.0", path)
    text = replace_once(
        text,
        "| PAS-001-CC-LIFECYCLE-001 | Active 1.0.0 | Consolidar ciclo de vida e estados funcionais da Captura de Contexto |",
        "| PAS-001-CC-LIFECYCLE-001 | Active 1.0.0 | Consolidar ciclo de vida e estados funcionais da Captura de Contexto |\n| PAS-001-CC-EVENT-INTEGRATION-001 | Active 1.0.0 | Consolidar eventos e integrações funcionais da Captura de Contexto |",
        path,
    )
    text = replace_once(text, "| Lacuna bloqueante | Eventos/integrações e contrato final da Capacidade 01 ainda pendentes |", "| Lacuna bloqueante | Contrato final da Capacidade 01 ainda pendente |", path)
    text = replace_once(text, "| Extensão vigente da Capacidade 01 | `PAS-001-CC-LIFECYCLE-001 1.0.0`, etapa `1 de 3` |", "| Extensões vigentes da Capacidade 01 | `PAS-001-CC-LIFECYCLE-001 1.0.0` e `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0`, etapa `2 de 3` |", path)
    text = replace_once(text, "| Extensões restantes da Capacidade 01 | `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001` |", "| Extensão restante da Capacidade 01 | `PAS-001-CC-CONTRACT-001` |", path)
    text = replace_once(text, "| Frente ativa | Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto |", "| Frente ativa | KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto |", path)
    text = replace_once(text, "| Foco imediato | Criar `PAS-001-CC-EVENT-INTEGRATION-001` e concluir a etapa `2 de 3` |", "| Foco imediato | Criar `PAS-001-CC-CONTRACT-001` e concluir a etapa `3 de 3` |", path)
    text = replace_once(
        text,
        "| 01 — Captura de Contexto | Substantially complete — etapa 1 de 3 | Ciclo de vida consolidado; eventos/integrações e contrato final permanecem pendentes |",
        "| 01 — Captura de Contexto | Substantially complete — etapa 2 de 3 | Ciclo de vida, eventos e integrações consolidados; contrato final permanece pendente |",
        path,
    )
    write(path, text)


def sync_matrix() -> None:
    path = "docs/project/canonical-consolidation-matrix.md"
    text = read(path)
    text = replace_once(text, "version: 1.23.0", "version: 1.24.0", path)
    text = replace_once(
        text,
        "| Captura de Contexto | Refinar | `Substantially complete`; etapa `1 de 3` concluída por `PAS-001-CC-LIFECYCLE-001 1.0.0` |",
        "| Captura de Contexto | Refinar | `Substantially complete`; etapa `2 de 3` concluída por `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` |",
        path,
    )
    anchor = "| Ciclo de Vida da Captura de Contexto | Manter | `PAS-001-CC-LIFECYCLE-001 1.0.0` governa agregado, sessão, estados, transições, canais, transcrição, interpretação, síntese, confirmação, autorização e persistência |"
    addition = anchor + "\n" + "\n".join([
        "| Eventos e Integrações da Captura de Contexto | Manter | `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` governa eventos versionados, 20 famílias, integrações, recortes, propagação, sincronização e prevenção de ciclos |",
        "| Evento funcional de Captura de Contexto | Refinar | Fato reconhecido e persistido sobre o Registro de Captura, distinto de sinal, comando, proposta, entrada, transcrição, interpretação e síntese |",
        "| Contrato de integração da Captura de Contexto | Manter | Define produtor, consumidor, finalidade, autoridade, escopo, natureza da informação, sensibilidade, proveniência, temporalidades, retenção e revogação |",
        "| Recorte de Captura de Contexto | Refinar | Conjunto minimizado, autorizado e versionado para finalidade e consumidor específicos; não equivale à captura integral |",
        "| Correção compensatória da Captura de Contexto | Manter | Novo evento preserva o histórico, corrige elementos derivados e propaga a alteração aos consumidores afetados |",
        "| Revogação propagada da Captura de Contexto | Manter | Bloqueia novos usos e somente é concluída após propagação suficiente e registro de retenção residual aplicável |",
    ])
    text = replace_once(text, anchor, addition, path)
    text = replace_once(
        text,
        "| Etapa de fechamento da Capacidade 01 | Manter | Ciclo de vida concluído; eventos/integrações e contrato final permanecem obrigatórios |",
        "| Etapa de fechamento da Capacidade 01 | Manter | Ciclo de vida, eventos e integrações concluídos; contrato final permanece obrigatório |",
        path,
    )
    write(path, text)


def sync_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_once(text, "- **Extensão vigente da Capacidade 01:** PAS-001-CC-LIFECYCLE-001 1.0.0 — etapa 1 de 3", "- **Extensões vigentes da Capacidade 01:** PAS-001-CC-LIFECYCLE-001 1.0.0 e PAS-001-CC-EVENT-INTEGRATION-001 1.0.0 — etapa 2 de 3", path)
    text = replace_once(text, "- **Próxima frente:** Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto", "- **Próxima frente:** KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto", path)
    old = """`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou a etapa `1 de 3` do fechamento formal, com `Registro de Captura de Contexto`, sessão, estados independentes, transições, entradas, canais, transcrição, interpretação, síntese, confirmação, autorização, persistência temporária, correção, limitação, contestação, revogação, acessibilidade, idempotência, ordenação, concorrência, reconstrução e falha segura.

A capacidade permanece **Substantially complete**. Eventos/integrações e o contrato final ainda são necessários."""
    new = """`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou o ciclo de vida e os estados. `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` conclui a etapa `2 de 3`, com estrutura comum versionada, 20 famílias de eventos, integrações funcionais, recortes autorizados, correção compensatória, revogação propagada, sincronização e prevenção de ciclos.

A capacidade permanece **Substantially complete**. KPIs, guardrails, cenários e contrato final ainda são necessários."""
    text = replace_once(text, old, new, path)
    write(path, text)


def sync_docs_index() -> None:
    path = "docs/index.md"
    text = read(path)
    text = replace_once(
        text,
        "- `PAS-001-CC-LIFECYCLE-001 1.0.0` como primeira extensão de fechamento da Capacidade 01, etapa `1 de 3`;",
        "- `PAS-001-CC-LIFECYCLE-001 1.0.0` e `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` como extensões de fechamento da Capacidade 01, etapa `2 de 3`;",
        path,
    )
    text = replace_once(
        text,
        "Consolidar os **Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto** por `PAS-001-CC-EVENT-INTEGRATION-001`, preservando o estado `Substantially complete` até o contrato final.",
        "Consolidar os **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto** por `PAS-001-CC-CONTRACT-001`, concluindo a etapa `3 de 3` antes da auditoria final de prontidão.",
        path,
    )
    text = replace_once(
        text,
        "- [Ciclo de Vida e Estados Funcionais da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-ciclo-de-vida.md)",
        "- [Ciclo de Vida e Estados Funcionais da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-ciclo-de-vida.md)\n- [Eventos e Integrações Funcionais da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-eventos-integracoes-funcionais.md)",
        path,
    )
    text = replace_once(text, "| 01 — Captura de Contexto | Substantially complete — etapa 1 de 3 |", "| 01 — Captura de Contexto | Substantially complete — etapa 2 de 3 |", path)
    text = replace_once(text, "Retomar nos **Eventos e Integrações Funcionais da Capacidade 01 — Captura de Contexto**.", "Retomar nos **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto**.", path)
    write(path, text)


def sync_mkdocs() -> None:
    path = "mkdocs.yml"
    text = read(path)
    anchor = "      - PAS-001-CC-LIFECYCLE-001 — Ciclo de Vida da Captura de Contexto: product-architecture/pas-001-captura-de-contexto-ciclo-de-vida.md"
    addition = anchor + "\n      - PAS-001-CC-EVENT-INTEGRATION-001 — Eventos e Integrações da Captura de Contexto: product-architecture/pas-001-captura-de-contexto-eventos-integracoes-funcionais.md"
    text = replace_once(text, anchor, addition, path)
    write(path, text)


def sync_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    anchor = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n"
    block = """## 0.52.0 — Capture Context Events and Functional Integrations

- Criação de `PAS-001-CC-EVENT-INTEGRATION-001 — Eventos e Integrações Funcionais da Captura de Contexto`, versão `1.0.0`.
- Registro do documento como segunda extensão complementar de fechamento da Capacidade 01.
- Conclusão da etapa `2 de 3`, mantendo a capacidade como `Substantially complete`.
- Consolidação de estrutura comum versionada para eventos do `Registro de Captura de Contexto`.
- Consolidação de 20 famílias de eventos funcionais.
- Distinção entre sinal, comando, proposta, declaração, entrada, transcrição, interpretação, síntese, confirmação, evento, recorte e efeito.
- Consolidação de produtores, consumidores, autoridade, finalidade, temporalidades, proveniência, sensibilidade, minimização, confiança e incerteza.
- Consolidação do contrato funcional comum de integração e dos recortes para as capacidades do Journey.
- Definição de persistência anterior à publicação, correção compensatória e revogação propagada.
- Consolidação de idempotência, duplicidade semântica, ordenação, concorrência, atomicidade, sincronização, reconstrução e prevenção de ciclos.
- Registro de 42 comportamentos proibidos e 80 critérios de aceite.
- Manutenção do `PAS-001` em `Draft 0.5.0` e da prontidão `Not ready — Capability 01 closure required`.
- Atualização da Arquitetura de Produtos para `1.24.0`.
- Atualização do Roadmap e do Knowledge Board para `11.5.0`.
- Atualização da Matriz de Consolidação Canônica para `1.24.0`.
- Atualização do README, da página inicial e da navegação do MkDocs.
- Definição de `PAS-001-CC-CONTRACT-001` como próximo ponto exato.


"""
    text = replace_once(text, anchor, anchor + block, path)
    write(path, text)


def validate_derived_files() -> None:
    checks = {
        "docs/product-architecture/index.md": ["version: 1.24.0", "PAS-001-CC-EVENT-INTEGRATION-001 1.0.0", "somente `PAS-001-CC-CONTRACT-001`"],
        "docs/roadmap.md": ["version: 11.5.0", "etapa `2 de 3`", "KPIs, Guardrails, Cenários e Contrato Final"],
        "docs/project/knowledge-board.md": ["version: 11.5.0", "PAS-001-CC-EVENT-INTEGRATION-001", "Substantially complete — etapa 2 de 3"],
        "docs/project/canonical-consolidation-matrix.md": ["version: 1.24.0", "Eventos e Integrações da Captura de Contexto", "Revogação propagada da Captura de Contexto"],
        "CHANGELOG.md": ["## 0.52.0", "42 comportamentos proibidos", "80 critérios de aceite"],
        "README.md": ["etapa 2 de 3", "PAS-001-CC-EVENT-INTEGRATION-001", "KPIs, Guardrails, Cenários e Contrato Final"],
        "docs/index.md": ["etapa `2 de 3`", "Eventos e Integrações Funcionais da Captura de Contexto", "PAS-001-CC-CONTRACT-001"],
        "mkdocs.yml": ["PAS-001-CC-EVENT-INTEGRATION-001", "pas-001-captura-de-contexto-eventos-integracoes-funcionais.md"],
    }
    for path, values in checks.items():
        text = read(path)
        for value in values:
            if value not in text:
                raise RuntimeError(f"{path}: missing expected value {value}")

    if "version: 1.23.0" in read("docs/product-architecture/index.md"):
        raise RuntimeError("product architecture version not advanced")
    if "version: 11.4.0" in read("docs/roadmap.md") or "version: 11.4.0" in read("docs/project/knowledge-board.md"):
        raise RuntimeError("roadmap or board version not advanced")


def main() -> None:
    validate_normative_document()
    sync_product_architecture()
    sync_roadmap()
    sync_board()
    sync_matrix()
    sync_readme()
    sync_docs_index()
    sync_mkdocs()
    sync_changelog()
    validate_derived_files()
    SCRIPT.unlink(missing_ok=True)
    WORKFLOW.unlink(missing_ok=True)
    print("Capture Context event and integration synchronization completed successfully.")


if __name__ == "__main__":
    main()
