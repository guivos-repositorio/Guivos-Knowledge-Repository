from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one exact anchor, found {count}")
    return text.replace(old, new, 1)


def replace_regex(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one regex anchor, found {count}")
    return updated


# README
path = "README.md"
text = read(path)
text = replace_exact(
    text,
    "- **Capacidades concluídas:** 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais, 08 — Experiências e 09 — Evolução Contínua",
    "- **Capacidades concluídas:** 01 — Captura de Contexto, 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais, 08 — Experiências e 09 — Evolução Contínua",
    "README capabilities",
)
text = replace_exact(
    text,
    "- **Extensões vigentes da Capacidade 01:** PAS-001-CC-LIFECYCLE-001 1.0.0 e PAS-001-CC-EVENT-INTEGRATION-001 1.0.0 — etapa 2 de 3",
    "- **Extensões vigentes da Capacidade 01:** PAS-001-CC-LIFECYCLE-001 1.0.0, PAS-001-CC-EVENT-INTEGRATION-001 1.0.0 e PAS-001-CC-CONTRACT-001 1.0.0 — etapa 3 de 3 concluída",
    "README extensions",
)
text = replace_exact(
    text,
    "- **Parecer de prontidão:** `Not ready — Capability 01 closure required`",
    "- **Parecer de prontidão:** `Conditionally ready — final PAS-001 audit required`",
    "README readiness",
)
text = replace_exact(
    text,
    "- **Próxima frente:** KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto",
    "- **Próxima frente:** Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey",
    "README next front",
)
text = replace_exact(
    text,
    "`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou o ciclo de vida e os estados. `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` conclui a etapa `2 de 3`, com estrutura comum versionada, 20 famílias de eventos, integrações funcionais, recortes autorizados, correção compensatória, revogação propagada, sincronização e prevenção de ciclos.\n\nA capacidade permanece **Substantially complete**. KPIs, guardrails, cenários e contrato final ainda são necessários.",
    "`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou o ciclo de vida e os estados. `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` consolidou eventos, integrações, recortes, correção compensatória e revogação propagada. `PAS-001-CC-CONTRACT-001 1.0.0` conclui a etapa `3 de 3`, com 80 KPIs em 16 famílias, baseline segmentada, painel de saúde com 17 visões, cinco níveis de desempenho, 42 guardrails, cenários e contrato final.\n\nA capacidade está **Functionally complete — 100%**. Todas as nove capacidades do Journey estão funcionalmente concluídas; o `PAS-001` permanece em `Draft 0.5.0` até a auditoria final.",
    "README capability 01 section",
)
write(path, text)

# Docs home
path = "docs/index.md"
text = read(path)
text = replace_exact(
    text,
    "- `PAS-001-CC-LIFECYCLE-001 1.0.0` e `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` como extensões de fechamento da Capacidade 01, etapa `2 de 3`;",
    "- `PAS-001-CC-LIFECYCLE-001 1.0.0`, `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` e `PAS-001-CC-CONTRACT-001 1.0.0` como extensões de fechamento da Capacidade 01, etapa `3 de 3` concluída;",
    "docs index extensions",
)
text = replace_exact(
    text,
    "- prontidão `Not ready — Capability 01 closure required`;",
    "- prontidão `Conditionally ready — final PAS-001 audit required`;",
    "docs index readiness",
)
text = replace_exact(
    text,
    "- Capacidades 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais, 08 — Experiências e 09 — Evolução Contínua funcionalmente concluídas;",
    "- Capacidades 01 — Captura de Contexto, 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais, 08 — Experiências e 09 — Evolução Contínua funcionalmente concluídas;",
    "docs index capabilities",
)
text = replace_exact(
    text,
    "Consolidar os **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto** por `PAS-001-CC-CONTRACT-001`, concluindo a etapa `3 de 3` antes da auditoria final de prontidão.",
    "Executar a **Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey** por `PAS-001-AUDIT-001`, preservando o `PAS-001` em `Draft 0.5.0` até a decisão formal de publicação.",
    "docs index mission",
)
text = replace_exact(
    text,
    "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final.",
    "As três extensões vigentes concluem a Capacidade 01 com ciclo de vida, 20 famílias de eventos, integrações, 80 KPIs em 16 famílias, 42 guardrails, baseline, painel de saúde, cenários e contrato final. As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final.",
    "docs index capability summary",
)
text = replace_exact(
    text,
    "- [Eventos e Integrações Funcionais da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-eventos-integracoes-funcionais.md)",
    "- [Eventos e Integrações Funcionais da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-eventos-integracoes-funcionais.md)\n- [Contrato Final da Captura de Contexto](product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md)",
    "docs index quick link",
)
text = replace_exact(
    text,
    "| 01 — Captura de Contexto | Substantially complete — etapa 2 de 3 |",
    "| 01 — Captura de Contexto | Functionally complete — 100% |",
    "docs index capability row",
)
text = replace_exact(
    text,
    "Retomar nos **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto**.",
    "Retomar na **Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey**.",
    "docs index resumption",
)
write(path, text)

# Product architecture index
path = "docs/product-architecture/index.md"
text = read(path)
text = replace_exact(text, "version: 1.24.0", "version: 1.25.0", "product architecture version")
text = replace_exact(
    text,
    "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base com as 51 extensões normativas das Capacidades 02 a 09, classifica estados e pontos de retomada históricos, define a hierarquia documental e registra o parecer `Not ready — Capability 01 closure required`.",
    "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base com as extensões normativas, classifica estados e pontos de retomada históricos e define a hierarquia documental. Após o contrato final da Capacidade 01, o parecer vigente passa a `Conditionally ready — final PAS-001 audit required`.",
    "product architecture reconciliation",
)
text = replace_exact(
    text,
    "A Capacidade 01 permanece `Substantially complete` e deverá ser concluída por `PAS-001-CC-LIFECYCLE-001`, `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001`.",
    "A Capacidade 01 está `Functionally complete — 100%` pelas extensões `PAS-001-CC-LIFECYCLE-001`, `PAS-001-CC-EVENT-INTEGRATION-001` e `PAS-001-CC-CONTRACT-001`. Todas as nove capacidades estão funcionalmente concluídas.",
    "product architecture capability status",
)
text = replace_exact(
    text,
    "`PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` conclui a etapa `2 de 3`, consolidando estrutura comum versionada, 20 famílias de eventos, contrato funcional comum de integração, produtores, consumidores, recortes, correção compensatória, revogação propagada, sincronização, prevenção de ciclos, idempotência, ordenação, concorrência, explicabilidade e auditoria.\n\nA capacidade permanece `Substantially complete`; somente `PAS-001-CC-CONTRACT-001` continua obrigatório antes da auditoria final de prontidão.",
    "`PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` concluiu a etapa `2 de 3`, consolidando estrutura comum versionada, 20 famílias de eventos, contrato funcional comum de integração, produtores, consumidores, recortes, correção compensatória, revogação propagada, sincronização, prevenção de ciclos, idempotência, ordenação, concorrência, explicabilidade e auditoria.\n\n`PAS-001-CC-CONTRACT-001 1.0.0` conclui a etapa `3 de 3`, consolidando 80 KPIs em 16 famílias, baseline segmentada, painel de saúde com 17 visões, cinco níveis de desempenho, 42 guardrails, cenários, 52 critérios de conclusão, 50 regras fundamentais e contrato funcional final.\n\nA capacidade está `Functionally complete — 100%`; o próximo ponto é `PAS-001-AUDIT-001`.",
    "product architecture contract section",
)
write(path, text)

# Roadmap
path = "docs/roadmap.md"
text = read(path)
text = replace_exact(text, "version: 11.5.0", "version: 11.6.0", "roadmap version")
text = replace_exact(
    text,
    "- **Extensões vigentes da Capacidade 01:** `PAS-001-CC-LIFECYCLE-001 1.0.0` e `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0`, etapa `2 de 3`.",
    "- **Extensões vigentes da Capacidade 01:** `PAS-001-CC-LIFECYCLE-001 1.0.0`, `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` e `PAS-001-CC-CONTRACT-001 1.0.0`, etapa `3 de 3` concluída.",
    "roadmap extensions",
)
text = replace_exact(
    text,
    "- **Parecer de prontidão:** `Not ready — Capability 01 closure required`.",
    "- **Parecer de prontidão:** `Conditionally ready — final PAS-001 audit required`.",
    "roadmap readiness",
)
text = replace_exact(
    text,
    "- **Lacuna bloqueante:** permanece `PAS-001-CC-CONTRACT-001` para o fechamento funcional formal da Capacidade 01.",
    "- **Lacuna funcional bloqueante:** nenhuma no nível de especificação das capacidades; permanece obrigatória a auditoria final do `PAS-001`.",
    "roadmap blocker",
)
text = replace_exact(
    text,
    "- **Capacidades concluídas:** `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais`, `08 — Experiências` e `09 — Evolução Contínua`.",
    "- **Capacidades concluídas:** `01 — Captura de Contexto`, `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais`, `08 — Experiências` e `09 — Evolução Contínua`.",
    "roadmap capabilities",
)
text = replace_exact(
    text,
    "Os eventos e as integrações funcionais da Capacidade 01 foram consolidados por `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0`. O próximo trabalho deverá consolidar os **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto**, mantendo o `PAS-001` em `Draft 0.5.0` e a prontidão como `Not ready`.",
    "A Capacidade 01 foi concluída por `PAS-001-CC-CONTRACT-001 1.0.0`. O próximo trabalho deverá executar a **Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey**, mantendo o `PAS-001` em `Draft 0.5.0` até a decisão formal de publicação.",
    "roadmap direction",
)
text = replace_exact(text, "## Capacidade 01 — Fechamento formal em andamento", "## Capacidade 01 — Fechamento formal concluído", "roadmap heading")
text = replace_exact(
    text,
    "`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou a primeira etapa. `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` consolidou a segunda etapa, com 90 seções normativas, 20 famílias de eventos, 42 comportamentos proibidos e 80 critérios de aceite.\n\nA Capacidade 01 permanece `Substantially complete`, etapa `2 de 3`. KPIs, guardrails, baseline, cenários e contrato final permanecem necessários para a conclusão funcional.",
    "`PAS-001-CC-LIFECYCLE-001 1.0.0` consolidou o ciclo de vida. `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` consolidou eventos e integrações. `PAS-001-CC-CONTRACT-001 1.0.0` conclui a etapa `3 de 3`, com 80 KPIs em 16 famílias, baseline, painel de saúde, cinco níveis de desempenho, 42 guardrails, cenários, 52 critérios de conclusão e 50 regras fundamentais.\n\nA Capacidade 01 está `Functionally complete — 100%`. Todas as capacidades do Journey estão funcionalmente concluídas; resta a auditoria final do `PAS-001`.",
    "roadmap capability section",
)
write(path, text)

# Knowledge Board
path = "docs/project/knowledge-board.md"
text = read(path)
text = replace_exact(text, "version: 11.5.0", "version: 11.6.0", "board version")
text = replace_exact(
    text,
    "| PAS-001-CC-EVENT-INTEGRATION-001 | Active 1.0.0 | Consolidar eventos e integrações funcionais da Captura de Contexto |",
    "| PAS-001-CC-EVENT-INTEGRATION-001 | Active 1.0.0 | Consolidar eventos e integrações funcionais da Captura de Contexto |\n| PAS-001-CC-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final da Captura de Contexto |",
    "board asset row",
)
text = replace_exact(
    text,
    "| Parecer de prontidão | `Not ready — Capability 01 closure required` |",
    "| Parecer de prontidão | `Conditionally ready — final PAS-001 audit required` |",
    "board readiness",
)
text = replace_exact(
    text,
    "| Lacuna bloqueante | Contrato final da Capacidade 01 ainda pendente |",
    "| Lacuna bloqueante | Nenhuma lacuna funcional de capacidade; auditoria final do PAS-001 permanece obrigatória |",
    "board blocker",
)
text = replace_exact(
    text,
    "| Extensões vigentes da Capacidade 01 | `PAS-001-CC-LIFECYCLE-001 1.0.0` e `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0`, etapa `2 de 3` |",
    "| Extensões vigentes da Capacidade 01 | `PAS-001-CC-LIFECYCLE-001 1.0.0`, `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` e `PAS-001-CC-CONTRACT-001 1.0.0`, etapa `3 de 3` concluída |",
    "board extensions",
)
text = replace_exact(
    text,
    "| Extensão restante da Capacidade 01 | `PAS-001-CC-CONTRACT-001` |",
    "| Extensão restante da Capacidade 01 | Nenhuma |",
    "board remaining extension",
)
text = replace_exact(
    text,
    "| Capacidades concluídas | `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais`, `08 — Experiências` e `09 — Evolução Contínua` |",
    "| Capacidades concluídas | `01 — Captura de Contexto`, `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais`, `08 — Experiências` e `09 — Evolução Contínua` |",
    "board capabilities",
)
text = replace_exact(
    text,
    "| Frente ativa | KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto |",
    "| Frente ativa | Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey |",
    "board active front",
)
text = replace_exact(
    text,
    "| Estado da frente ativa | Próximo ciclo normativo |",
    "| Estado da frente ativa | Auditoria normativa e editorial |",
    "board front state",
)
text = replace_exact(
    text,
    "| Foco imediato | Criar `PAS-001-CC-CONTRACT-001` e concluir a etapa `3 de 3` |",
    "| Foco imediato | Criar `PAS-001-AUDIT-001` e decidir a prontidão para publicação do `PAS-001 1.0.0` |",
    "board immediate focus",
)
text = replace_exact(
    text,
    "| 01 — Captura de Contexto | Substantially complete — etapa 2 de 3 | Ciclo de vida, eventos e integrações consolidados; contrato final permanece pendente |",
    "| 01 — Captura de Contexto | Functionally complete — 100% | Três extensões normativas, 80 KPIs, 42 guardrails, baseline, cenários e contrato final consolidados |",
    "board capability row",
)
text = replace_regex(
    text,
    r"Retomar nos \*\*KPIs, Guardrails, Cenários e Contrato Final da Capacidade 01 — Captura de Contexto\*\*\.",
    "Retomar na **Auditoria Final de Prontidão e Consolidação Editorial do PAS-001 — Guivos Journey**.",
    "board resumption",
)
write(path, text)

# Canonical matrix
path = "docs/project/canonical-consolidation-matrix.md"
text = read(path)
text = replace_exact(text, "version: 1.24.0", "version: 1.25.0", "matrix version")
text = replace_exact(
    text,
    "| Prontidão para PAS-001 1.0.0 | Refinar | Estado vigente `Not ready — Capability 01 closure required` |",
    "| Prontidão para PAS-001 1.0.0 | Refinar | Estado vigente `Conditionally ready — final PAS-001 audit required` |",
    "matrix readiness",
)
text = replace_exact(
    text,
    "| Captura de Contexto | Refinar | `Substantially complete`; etapa `2 de 3` concluída por `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` |",
    "| Captura de Contexto | Manter | `Functionally complete — 100%`; etapa `3 de 3` concluída por `PAS-001-CC-CONTRACT-001 1.0.0` |",
    "matrix capture status",
)
text = replace_exact(
    text,
    "| Eventos e Integrações da Captura de Contexto | Manter | `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` governa eventos versionados, 20 famílias, integrações, recortes, propagação, sincronização e prevenção de ciclos |",
    "| Eventos e Integrações da Captura de Contexto | Manter | `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0` governa eventos versionados, 20 famílias, integrações, recortes, propagação, sincronização e prevenção de ciclos |\n| Contrato Final da Captura de Contexto | Manter | `PAS-001-CC-CONTRACT-001 1.0.0` governa 80 KPIs, 16 famílias, baseline, painel de saúde, cinco níveis, 42 guardrails, cenários, conclusão e reabertura |\n| KPIs da Captura de Contexto | Manter | 80 indicadores avaliam o sistema, sem medir quantidade de dados ou valor humano |\n| Guardrails da Captura de Contexto | Manter | 42 proibições de tolerância zero prevalecem sobre médias e metas operacionais |",
    "matrix contract rows",
)
text = replace_exact(
    text,
    "| Etapa de fechamento da Capacidade 01 | Manter | Ciclo de vida, eventos e integrações concluídos; contrato final permanece obrigatório |",
    "| Etapa de fechamento da Capacidade 01 | Manter | Ciclo de vida, eventos, integrações e contrato final concluídos; etapa `3 de 3` encerrada |",
    "matrix closure stage",
)
text = replace_exact(
    text,
    "| Edição PAS-001 1.0.0 | Planejar | Especificação consolidada e federada após fechamento da Capacidade 01 e auditoria final |",
    "| Edição PAS-001 1.0.0 | Planejar | Todas as capacidades estão concluídas; publicação depende de `PAS-001-AUDIT-001` e decisão formal |",
    "matrix edition",
)
write(path, text)

# PAS-001 base notice
path = "docs/product-architecture/pas-001-guivos-journey.md"
text = read(path)
text = replace_exact(
    text,
    "  - PAS-001-RECON-001\n  - DR-001",
    "  - PAS-001-RECON-001\n  - PAS-001-CC-LIFECYCLE-001\n  - PAS-001-CC-EVENT-INTEGRATION-001\n  - PAS-001-CC-CONTRACT-001\n  - DR-001",
    "PAS related documents",
)
text = replace_exact(
    text,
    "> **Aviso normativo de reconciliação:** `PAS-001-RECON-001 1.0.0` estabelece que esta especificação-base permanece `Draft 0.5.0`, classifica o mapa e os pontos de retomada históricos conforme as extensões posteriores e registra a prontidão como `Not ready — Capability 01 closure required`.",
    "> **Aviso normativo de reconciliação:** `PAS-001-RECON-001 1.0.0` estabelece que esta especificação-base permanece `Draft 0.5.0` e classifica o mapa e os pontos de retomada históricos. `PAS-001-CC-CONTRACT-001 1.0.0` conclui funcionalmente a Capacidade 01 e atualiza a prontidão para `Conditionally ready — final PAS-001 audit required`.",
    "PAS readiness notice",
)
write(path, text)

# Changelog
path = "CHANGELOG.md"
text = read(path)
entry = """## 0.53.0 — Capture Context Final Contract

- Criação de `PAS-001-CC-CONTRACT-001 — KPIs, Guardrails, Cenários e Contrato Final da Captura de Contexto`, versão `1.0.0`.
- Registro do documento como terceira extensão complementar e contrato final da Capacidade 01.
- Conclusão da etapa `3 de 3` e elevação da Capacidade 01 para `Functionally complete — 100%`.
- Consolidação de 80 KPIs em 16 famílias.
- Consolidação de baseline funcional segmentada, painel de saúde com 17 visões e cinco níveis de desempenho.
- Registro de 42 guardrails de tolerância zero.
- Consolidação de cenários funcionalmente ideais, alternativos e limite.
- Registro de 52 critérios de conclusão e 50 regras fundamentais.
- Encerramento da lacuna funcional bloqueante da Capacidade 01.
- Manutenção do `PAS-001` em `Draft 0.5.0`.
- Atualização da prontidão para `Conditionally ready — final PAS-001 audit required`.
- Atualização da Arquitetura de Produtos e da Matriz Canônica para `1.25.0`.
- Atualização do Roadmap e do Knowledge Board para `11.6.0`.
- Atualização do README, página inicial, especificação-base e navegação do MkDocs.
- Definição de `PAS-001-AUDIT-001` como próximo ponto exato.


"""
text = replace_exact(
    text,
    "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n## 0.52.0",
    "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n" + entry + "## 0.52.0",
    "changelog entry",
)
write(path, text)

# MkDocs navigation
path = "mkdocs.yml"
text = read(path)
text = replace_exact(
    text,
    "      - PAS-001-CC-EVENT-INTEGRATION-001 — Eventos e Integrações da Captura de Contexto: product-architecture/pas-001-captura-de-contexto-eventos-integracoes-funcionais.md",
    "      - PAS-001-CC-EVENT-INTEGRATION-001 — Eventos e Integrações da Captura de Contexto: product-architecture/pas-001-captura-de-contexto-eventos-integracoes-funcionais.md\n      - PAS-001-CC-CONTRACT-001 — Contrato Final da Captura de Contexto: product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md",
    "mkdocs navigation",
)
write(path, text)

# Structural validations
contract_path = "docs/product-architecture/pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md"
contract = read(contract_path)
sections = [int(value) for value in re.findall(r"^# (\d+)\.", contract, flags=re.MULTILINE)]
expected_sections = list(range(4759, 4851))
if sections != expected_sections:
    raise RuntimeError(f"contract sections are not contiguous: {sections[:3]} ... {sections[-3:]}")

kpis = re.findall(r"`CC-KPI-(\d{3})`", contract)
expected_kpis = [f"{number:03d}" for number in range(1, 81)]
if kpis != expected_kpis:
    raise RuntimeError(f"KPI sequence mismatch: {len(kpis)} entries")


def numbered_items_between(start: int, end: int) -> list[int]:
    match = re.search(rf"^# {start}\..*?\n(.*?)^# {end}\.", contract, flags=re.MULTILINE | re.DOTALL)
    if not match:
        raise RuntimeError(f"missing section range {start}-{end}")
    return [int(value) for value in re.findall(r"^(\d+)\. ", match.group(1), flags=re.MULTILINE)]

if numbered_items_between(4792, 4793) != list(range(1, 43)):
    raise RuntimeError("guardrail count or sequence mismatch")
if numbered_items_between(4841, 4842) != list(range(1, 53)):
    raise RuntimeError("completion criteria count or sequence mismatch")
if numbered_items_between(4845, 4846) != list(range(1, 51)):
    raise RuntimeError("final rules count or sequence mismatch")

checks = {
    "README.md": ["Functionally complete — 100%", "Conditionally ready — final PAS-001 audit required", "PAS-001-AUDIT-001"],
    "docs/index.md": ["Functionally complete — 100%", "Conditionally ready — final PAS-001 audit required", "pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md"],
    "docs/product-architecture/index.md": ["version: 1.25.0", "80 KPIs em 16 famílias", "PAS-001-AUDIT-001"],
    "docs/roadmap.md": ["version: 11.6.0", "Conditionally ready — final PAS-001 audit required", "Capacidade 01 — Fechamento formal concluído"],
    "docs/project/knowledge-board.md": ["version: 11.6.0", "PAS-001-CC-CONTRACT-001", "Functionally complete — 100%"],
    "docs/project/canonical-consolidation-matrix.md": ["version: 1.25.0", "80 indicadores", "42 proibições"],
    "docs/product-architecture/pas-001-guivos-journey.md": ["version: 0.5.0", "Conditionally ready — final PAS-001 audit required", "PAS-001-CC-CONTRACT-001"],
    "CHANGELOG.md": ["## 0.53.0 — Capture Context Final Contract", "Roadmap e do Knowledge Board para `11.6.0`"],
    "mkdocs.yml": ["PAS-001-CC-CONTRACT-001 — Contrato Final da Captura de Contexto"],
}
for filename, needles in checks.items():
    data = read(filename)
    for needle in needles:
        if needle not in data:
            raise RuntimeError(f"{filename}: missing validation token {needle!r}")

current_files = [
    "README.md",
    "docs/index.md",
    "docs/product-architecture/index.md",
    "docs/roadmap.md",
    "docs/project/knowledge-board.md",
    "docs/project/canonical-consolidation-matrix.md",
    "docs/product-architecture/pas-001-guivos-journey.md",
]
for filename in current_files:
    data = read(filename)
    if "Not ready — Capability 01 closure required" in data:
        raise RuntimeError(f"{filename}: stale readiness remains")
    if "Substantially complete — etapa 2 de 3" in data:
        raise RuntimeError(f"{filename}: stale capability status remains")

# Remove temporary automation from the final diff.
(ROOT / ".github/workflows/sync-cc-contract.yml").unlink()
Path(__file__).unlink()
