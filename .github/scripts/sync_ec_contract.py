from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TODAY = "2026-07-18"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 ocorrência, encontrado {count}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 match, encontrado {count}")
    return updated


def insert_after_once(text: str, anchor: str, insertion: str, label: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 anchor, encontrado {count}")
    return text.replace(anchor, anchor + insertion, 1)


def insert_before_once(text: str, anchor: str, insertion: str, label: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 anchor, encontrado {count}")
    return text.replace(anchor, insertion + anchor, 1)


def section_block(text: str, number: int, next_number: int) -> str:
    start = text.index(f"# {number}.")
    end = text.index(f"# {next_number}.", start)
    return text[start:end]


DOC = "docs/product-architecture/pas-001-evolucao-continua-kpis-cenarios-contrato-final.md"
doc = read(DOC)
sections = [int(value) for value in re.findall(r"^# (\d+)\.", doc, flags=re.MULTILINE)]
expected = list(range(4401, 4492))
if sections != expected:
    raise RuntimeError(f"sequência normativa inválida: {sections[:4]} ... {sections[-4:] if sections else []}")

kpis = sorted(set(re.findall(r"`EC-KPI-(\d{3})`", doc)))
if kpis != [f"{value:03d}" for value in range(1, 91)]:
    raise RuntimeError(f"KPIs inválidos: {len(kpis)}")

for number, next_number, expected_count, label in (
    (4432, 4433, 36, "guardrails"),
    (4471, 4472, 52, "critérios de conclusão"),
    (4489, 4490, 52, "regras finais"),
):
    block = section_block(doc, number, next_number)
    found = len(re.findall(r"^\d+\. ", block, flags=re.MULTILINE))
    if found != expected_count:
        raise RuntimeError(f"{label}: esperado {expected_count}, encontrado {found}")

contract_summary_index = """

`PAS-001-EC-CONTRACT-001 1.0.0` consolida:

- 90 KPIs em 18 famílias, orientados à qualidade da capacidade e do sistema;
- baseline funcional segmentada, critérios de maturidade e metas posteriores à baseline real;
- painel de saúde com 19 visões e cinco níveis de desempenho;
- 36 guardrails de tolerância zero, prevalentes sobre médias agregadas;
- cenários funcionalmente ideais, alternativos e limite;
- 52 critérios de conclusão funcional, lacunas bloqueantes e não bloqueantes e critérios de reabertura;
- finalidade, singularidade, titularidade, responsabilidades, limites, entradas, admissão, saídas e 28 dimensões preservadas;
- neutralidade comercial, privacidade, confiabilidade, explicabilidade, auditoria, reconstrução e controle do participante;
- ausência de lacuna funcional bloqueante conhecida na baseline normativa.
"""

contract_summary_board = """

### Contrato final

- 90 KPIs em 18 famílias;
- baseline funcional segmentada e critérios de maturidade;
- painel de saúde com 19 visões;
- cinco níveis de desempenho;
- 36 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- 52 critérios de conclusão funcional;
- lacunas bloqueantes e não bloqueantes;
- finalidade, singularidade, titularidade, responsabilidades, limites, entradas, admissão, saídas e 28 dimensões preservadas;
- neutralidade comercial, privacidade, confiabilidade, explicabilidade, auditoria e critérios de reabertura;
- nenhuma lacuna funcional bloqueante conhecida.
"""

# Arquitetura de Produtos
path = "docs/product-architecture/index.md"
text = read(path)
text = replace_once(text, "version: 1.20.0", "version: 1.21.0", f"{path} versão")
text = replace_once(text, "last_updated: 2026-07-17", f"last_updated: {TODAY}", f"{path} data")
text = regex_once(
    text,
    r"A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `90%`, por meio de [^\n]+",
    "A Capacidade 09 — Evolução Contínua está `Functionally complete`, com progresso editorial de referência de `100%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0`, `PAS-001-EC-INTEGRATION-001 1.0.0` e `PAS-001-EC-CONTRACT-001 1.0.0`.",
    f"{path} estado inicial",
)
text = insert_before_once(
    text,
    "A Capacidade 09 está `In progress`, com progresso editorial de referência de `90%`.",
    contract_summary_index,
    f"{path} resumo contrato",
)
text = replace_once(
    text,
    "A Capacidade 09 está `In progress`, com progresso editorial de referência de `90%`.",
    "A Capacidade 09 está `Functionally complete`, com progresso editorial de referência de `100%`.",
    f"{path} progresso",
)
text = replace_once(
    text,
    "O próximo bloco normativo consolida KPIs, guardrails, baseline, painel de saúde, níveis de desempenho, cenários e contrato funcional final da Evolução Contínua.",
    "A próxima frente oficial é a Reconciliação e o Fechamento do `PAS-001 — Guivos Journey`, com revisão da Capacidade 01, consolidação do mapa de capacidades e avaliação de prontidão para `PAS-001 1.0.0`.",
    f"{path} próximo bloco",
)
write(path, text)

# Roadmap
path = "docs/roadmap.md"
text = read(path)
text = replace_once(text, "version: 11.1.0", "version: 11.2.0", f"{path} versão")
text = replace_once(text, "last_updated: 2026-07-17", f"last_updated: {TODAY}", f"{path} data")
text = replace_once(
    text,
    "- **Capacidades concluídas:** `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais` e `08 — Experiências`.",
    "- **Capacidades concluídas:** `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais`, `08 — Experiências` e `09 — Evolução Contínua`.",
    f"{path} capacidades concluídas",
)
text = replace_once(
    text,
    "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 90%.",
    "- **Capacidade concluída:** `09 — Evolução Contínua`, `Functionally complete`, 100%.",
    f"{path} capacidade 09",
)
text = replace_once(
    text,
    "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0`.",
    "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0`, `PAS-001-EC-INTEGRATION-001 1.0.0` e `PAS-001-EC-CONTRACT-001 1.0.0`.",
    f"{path} extensões",
)
text = replace_once(
    text,
    "O próximo trabalho deverá consolidar os KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários e contrato final da `Capacidade 09 — Evolução Contínua`.",
    "O próximo trabalho deverá realizar a Reconciliação e o Fechamento do `PAS-001 — Guivos Journey`, revisar a Capacidade 01, consolidar o mapa final de capacidades e avaliar a prontidão para `PAS-001 1.0.0`.",
    f"{path} direção",
)
text = insert_before_once(
    text,
    "A Capacidade 09 está `In progress`, com progresso editorial de referência de `90%`.",
    contract_summary_index.replace("consolida:", "consolidou:"),
    f"{path} resumo contrato",
)
text = replace_once(
    text,
    "A Capacidade 09 está `In progress`, com progresso editorial de referência de `90%`.",
    "A Capacidade 09 está `Functionally complete`, com progresso editorial de referência de `100%`.",
    f"{path} progresso",
)
text = regex_once(
    text,
    r"## Ponto exato de retomada\n\nRetomar em \*\*KPIs, Guardrails, Cenários e Contrato Final da Capacidade 09 — Evolução Contínua\*\*\.\n\nPróxima entrega:\n\n1\. KPIs e famílias de indicadores sistêmicos;\n2\. guardrails de tolerância zero e baseline funcional segmentada;\n3\. painel de saúde, níveis de desempenho e metas posteriores à baseline;\n4\. cenários funcionalmente ideal, alternativo e limite;\n5\. critérios de conclusão, lacunas, reabertura e contrato funcional final\.",
    "## Ponto exato de retomada\n\nRetomar na **Reconciliação e Fechamento do PAS-001 — Guivos Journey**.\n\nPróxima entrega:\n\n1. revisar o estado da Capacidade 01 — Captura de Contexto;\n2. atualizar o Mapa de Capacidades do Journey;\n3. consolidar as extensões normativas das Capacidades 02 a 09;\n4. resolver divergências residuais e disposições substituídas;\n5. avaliar a prontidão para `PAS-001 1.0.0` e definir o próximo ciclo de Product Engineering.",
    f"{path} retomada",
    flags=re.MULTILINE,
)
write(path, text)

# Knowledge Board
path = "docs/project/knowledge-board.md"
text = read(path)
text = replace_once(text, "version: 11.1.0", "version: 11.2.0", f"{path} versão")
text = replace_once(text, "last_updated: 2026-07-17", f"last_updated: {TODAY}", f"{path} data")
text = insert_after_once(
    text,
    "| PAS-001-EC-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais da Evolução Contínua |",
    "\n| PAS-001-EC-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final da Evolução Contínua |",
    f"{path} ativo contrato",
)
text = replace_once(
    text,
    "| Capacidades concluídas | `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais` e `08 — Experiências` |",
    "| Capacidades concluídas | `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais`, `08 — Experiências` e `09 — Evolução Contínua` |",
    f"{path} concluídas",
)
text = replace_once(text, "| Capacidade ativa | `09 — Evolução Contínua` |", "| Frente ativa | Reconciliação e Fechamento do `PAS-001 — Guivos Journey` |", f"{path} frente")
text = replace_once(text, "| Estado da capacidade ativa | `In progress — 90%` |", "| Estado da frente ativa | Próxima frente oficial |", f"{path} estado frente")
text = replace_once(
    text,
    "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0` |",
    "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0`, `PAS-001-EC-INTEGRATION-001 1.0.0` e `PAS-001-EC-CONTRACT-001 1.0.0` |",
    f"{path} extensões",
)
text = replace_once(text, "| Progresso editorial de Evolução Contínua | `90%` |", "| Progresso editorial de Evolução Contínua | `100%` |", f"{path} progresso")
text = replace_once(text, "| Foco imediato | Consolidar KPIs, guardrails, baseline, cenários e contrato final da Capacidade 09 — Evolução Contínua |", "| Foco imediato | Reconciliar e fechar o PAS-001 — Guivos Journey, revisar a Capacidade 01 e avaliar prontidão para 1.0.0 |", f"{path} foco")
text = replace_once(
    text,
    "| 09 — Evolução Contínua | In progress — 90% | Cinco extensões normativas consolidadas; contrato final como próximo bloco |",
    "| 09 — Evolução Contínua | Functionally complete — 100% | Seis extensões normativas, 90 KPIs, 36 guardrails, baseline, cenários e contrato final consolidados |",
    f"{path} capacidade 09",
)
text = insert_before_once(
    text,
    "A Capacidade 09 está `In progress`, com progresso editorial de referência de `90%`.",
    contract_summary_board,
    f"{path} resumo contrato",
)
text = replace_once(text, "A Capacidade 09 está `In progress`, com progresso editorial de referência de `90%`.", "A Capacidade 09 está `Functionally complete`, com progresso editorial de referência de `100%`.", f"{path} estado seção")
text = replace_once(text, "| Evolução Contínua | In progress — 90% |", "| Evolução Contínua | Functionally complete — 100% |", f"{path} conceito estado")
text = insert_after_once(
    text,
    "| Contrato de integração de evolução | Define produtor, consumidor, participante, trajetória, segmento, finalidade, modo, autoridade, dimensão, baseline, direção, escopo, sensibilidade, proveniência, confiança, incerteza, temporalidades, retenção, sincronização e revogação |",
    "\n| Contrato Final de Evolução Contínua | Normative 1.0.0 |\n| Baseline de Evolução Contínua | Referência empírica segmentada construída antes de metas permanentes e destinada a avaliar o sistema, não estabelecer padrão humano ideal |\n| Guardrail de Evolução Contínua | Regra crítica de tolerância zero cuja violação não pode ser compensada por média positiva |\n| Conclusão funcional de Evolução Contínua | Contratos essenciais concluídos com 90 KPIs, 36 guardrails, baseline, cenários e ausência de lacuna bloqueante conhecida |",
    f"{path} conceitos contrato",
)
write(path, text)

# Matriz de Consolidação Canônica
path = "docs/project/canonical-consolidation-matrix.md"
text = read(path)
text = replace_once(text, "version: 1.20.0", "version: 1.21.0", f"{path} versão")
text = replace_once(text, "last_updated: 2026-07-17", f"last_updated: {TODAY}", f"{path} data")
text = replace_once(
    text,
    "| Evolução Contínua | Refinar | Capacidade 09 ativa em 90%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |",
    "| Evolução Contínua | Manter | Capacidade 09 Functionally complete em 100%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |",
    f"{path} evolução",
)
text = insert_after_once(
    text,
    "| Integrações Funcionais da Evolução Contínua | Manter | PAS-001-EC-INTEGRATION-001 1.0.0 define contrato comum, identidade, associação, titularidade, autoridade, finalidade, minimização, proveniência, temporalidades, confiança, incerteza, sincronização, prevenção de ciclos, revogação, produtos, organizações, dispositivos, observabilidade e falha segura |",
    "\n| KPIs, Guardrails, Cenários e Contrato Final da Evolução Contínua | Manter | PAS-001-EC-CONTRACT-001 1.0.0 define 90 KPIs, 18 famílias, 36 guardrails, baseline, painel de saúde, cinco níveis, cenários, critérios de conclusão, lacunas, reabertura e contrato final |\n| Baseline de Evolução Contínua | Manter | Referência empírica segmentada construída antes de metas permanentes para avaliar a capacidade e o sistema |\n| Guardrail de Evolução Contínua | Manter | Regra crítica de tolerância zero prevalente sobre médias agregadas |\n| Conclusão funcional de Evolução Contínua | Manter | Contratos essenciais concluídos; não equivale a implementação ou validação em produção |",
    f"{path} contrato",
)
write(path, text)

# README
path = "README.md"
text = read(path)
text = replace_once(
    text,
    "- **Capacidades concluídas:** 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais e 08 — Experiências",
    "- **Capacidades concluídas:** 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais, 08 — Experiências e 09 — Evolução Contínua",
    f"{path} concluídas",
)
text = replace_once(text, "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 90%`", "- **Próxima frente:** Reconciliação e Fechamento do PAS-001 — Guivos Journey", f"{path} frente")
text = replace_once(
    text,
    "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0, PAS-001-EC-LIFECYCLE-001 1.0.0, PAS-001-EC-VIEW-001 1.0.0, PAS-001-EC-EVENT-001 1.0.0 e PAS-001-EC-INTEGRATION-001 1.0.0",
    "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0, PAS-001-EC-LIFECYCLE-001 1.0.0, PAS-001-EC-VIEW-001 1.0.0, PAS-001-EC-EVENT-001 1.0.0, PAS-001-EC-INTEGRATION-001 1.0.0 e PAS-001-EC-CONTRACT-001 1.0.0",
    f"{path} extensões",
)
text = insert_after_once(
    text,
    "`PAS-001-EC-INTEGRATION-001 1.0.0` consolida o contrato comum de integração, identidade, associação, titularidade, autoridade, finalidade, minimização, proveniência, temporalidades, sensibilidade, confiança, incerteza, transformações, sincronização, prevenção de ciclos, correção, pausa, desconexão, revogação, propagação, integrações internas e externas, observabilidade, explicabilidade, auditoria, reconstrução e falha segura.",
    "\n\n`PAS-001-EC-CONTRACT-001 1.0.0` consolida 90 KPIs em 18 famílias, baseline funcional segmentada, painel de saúde com 19 visões, cinco níveis de desempenho, 36 guardrails de tolerância zero, cenários ideais, alternativos e limite, 52 critérios de conclusão, lacunas, reabertura e contrato funcional final.",
    f"{path} resumo contrato",
)
text = replace_once(text, "A Capacidade 09 está **In progress**, com progresso editorial de referência de **90%**.", "A Capacidade 09 está **Functionally complete**, com progresso editorial de referência de **100%**.", f"{path} estado")
text = regex_once(
    text,
    r"## Ponto exato de retomada\n\nRetomar em \*\*KPIs, Guardrails, Cenários e Contrato Final da Capacidade 09 — Evolução Contínua\*\*\.\n\nPróxima entrega:\n\n- KPIs e famílias de indicadores sistêmicos;\n- guardrails de tolerância zero e baseline funcional segmentada;\n- painel de saúde, níveis de desempenho e metas posteriores à baseline;\n- cenários funcionalmente ideal, alternativo e limite;\n- critérios de conclusão, lacunas, reabertura e contrato funcional final\.",
    "## Ponto exato de retomada\n\nRetomar na **Reconciliação e Fechamento do PAS-001 — Guivos Journey**.\n\nPróxima entrega:\n\n- revisar a Capacidade 01 — Captura de Contexto;\n- atualizar o Mapa de Capacidades;\n- consolidar extensões e disposições substituídas;\n- resolver divergências residuais;\n- avaliar a prontidão para `PAS-001 1.0.0`.",
    f"{path} retomada",
    flags=re.MULTILINE,
)
text = replace_once(
    text,
    "As Capacidades 06 — Oportunidades Ativas, 07 — Intervenções Contextuais e 08 — Experiências estão `Functionally complete`; a Capacidade 09 — Evolução Contínua está `In progress — 90%`.",
    "As Capacidades 02 a 09 estão funcionalmente concluídas. A próxima frente é a Reconciliação e o Fechamento do `PAS-001 — Guivos Journey`.",
    f"{path} product engineering",
)
text = replace_once(text, "| 09 — Evolução Contínua | In progress — 90% |", "| 09 — Evolução Contínua | Functionally complete — 100% |", f"{path} tabela")
text = insert_after_once(
    text,
    "- [Integrações Funcionais da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-integracoes-funcionais.md)",
    "\n- [Contrato Final da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-kpis-cenarios-contrato-final.md)",
    f"{path} link contrato",
)
write(path, text)

# Página inicial
path = "docs/index.md"
text = read(path)
text = replace_once(
    text,
    "- Capacidades 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais e 08 — Experiências funcionalmente concluídas;",
    "- Capacidades 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais, 08 — Experiências e 09 — Evolução Contínua funcionalmente concluídas;",
    f"{path} concluídas",
)
text = replace_once(text, "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 90%;", "- Capacidade 09 — Evolução Contínua funcionalmente concluída, `Functionally complete`, 100%;", f"{path} capacidade")
text = replace_once(
    text,
    "- `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0` como extensões normativas vigentes da Capacidade 09;",
    "- `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0`, `PAS-001-EC-INTEGRATION-001 1.0.0` e `PAS-001-EC-CONTRACT-001 1.0.0` como extensões normativas vigentes da Capacidade 09;",
    f"{path} extensões",
)
text = replace_once(text, "Consolidar **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários e contrato funcional final da Capacidade 09 — Evolução Contínua**.", "Realizar a **Reconciliação e o Fechamento do PAS-001 — Guivos Journey**, revisar a Capacidade 01, consolidar o mapa de capacidades e avaliar a prontidão para `PAS-001 1.0.0`.", f"{path} missão")
text = regex_once(
    text,
    r"As seis extensões vigentes concluem a Capacidade 06[^\n]+As cinco extensões de Evolução Contínua mantêm a Capacidade 09 ativa[^\n]+",
    "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As seis extensões de Intervenções Contextuais concluem a Capacidade 07 com 80 KPIs em 16 famílias e 28 guardrails. As seis extensões de Experiências concluem a Capacidade 08 com 85 KPIs em 17 famílias e 32 guardrails. As seis extensões de Evolução Contínua concluem a Capacidade 09 com fundamentos, ciclo de vida, `Minha Evolução`, eventos, integrações, 90 KPIs em 18 famílias, 36 guardrails, baseline, painel de saúde, cenários e contrato final.",
    f"{path} resumo",
)
text = insert_after_once(
    text,
    "- [Integrações Funcionais da Evolução Contínua](product-architecture/pas-001-evolucao-continua-integracoes-funcionais.md)",
    "\n- [Contrato Final da Evolução Contínua](product-architecture/pas-001-evolucao-continua-kpis-cenarios-contrato-final.md)",
    f"{path} link contrato",
)
text = replace_once(text, "| 09 — Evolução Contínua | In progress — 90% |", "| 09 — Evolução Contínua | Functionally complete — 100% |", f"{path} tabela")
text = replace_once(text, "Retomar em **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 09 — Evolução Contínua**.", "Retomar na **Reconciliação e Fechamento do PAS-001 — Guivos Journey**.", f"{path} retomada")
write(path, text)

# MkDocs
path = "mkdocs.yml"
text = read(path)
text = insert_after_once(
    text,
    "      - PAS-001-EC-INTEGRATION-001 — Integrações Funcionais da Evolução Contínua: product-architecture/pas-001-evolucao-continua-integracoes-funcionais.md",
    "\n      - PAS-001-EC-CONTRACT-001 — Contrato Final da Evolução Contínua: product-architecture/pas-001-evolucao-continua-kpis-cenarios-contrato-final.md",
    f"{path} nav contrato",
)
write(path, text)

# Changelog
path = "CHANGELOG.md"
text = read(path)
entry = """

## 0.49.0 — Continuous Evolution Functional Completion

- Criação de `PAS-001-EC-CONTRACT-001 — KPIs, Guardrails, Cenários e Contrato Final da Capacidade de Evolução Contínua`, versão `1.0.0`.
- Registro do documento como sexta extensão normativa e contrato final da Capacidade 09 do `PAS-001 — Guivos Journey`.
- Substituição do estado `In progress` por `Functionally complete` e elevação do progresso editorial de 90% para 100%.
- Consolidação de 90 KPIs em 18 famílias, baseline funcional segmentada, critérios de maturidade e metas posteriores à baseline real.
- Definição de painel de saúde com 19 visões e cinco níveis de desempenho.
- Consolidação de 36 guardrails de tolerância zero, prevalentes sobre médias agregadas.
- Consolidação de cenários funcionalmente ideais, alternativos e limite.
- Definição de 52 critérios de conclusão, lacunas bloqueantes e não bloqueantes e critérios de reabertura.
- Consolidação da finalidade, singularidade, titularidade, responsabilidades, limites, entradas, admissão, saídas e 28 dimensões preservadas.
- Preservação de neutralidade comercial, privacidade, confiabilidade, explicabilidade, auditoria, reconstrução e controle do participante.
- Registro de ausência de lacuna funcional bloqueante conhecida na baseline normativa.
- Conclusão funcional das Capacidades 02 a 09 do Journey.
- Atualização da Arquitetura de Produtos para `1.21.0`.
- Atualização do Roadmap e do Knowledge Board para `11.2.0`.
- Atualização da Matriz de Consolidação Canônica para `1.21.0`.
- Atualização do README, da página inicial e da navegação do MkDocs.
- Definição da Reconciliação e Fechamento do `PAS-001 — Guivos Journey` como próximo ponto exato.
"""
text = insert_before_once(text, "## 0.48.0 — Continuous Evolution Functional Integrations", entry + "\n", f"{path} entrada")
write(path, text)

# Validações derivadas
checks = {
    "docs/product-architecture/index.md": ["version: 1.21.0", "Functionally complete", "PAS-001-EC-CONTRACT-001 1.0.0"],
    "docs/roadmap.md": ["version: 11.2.0", "Reconciliação e Fechamento", "Functionally complete", "100%"],
    "docs/project/knowledge-board.md": ["version: 11.2.0", "PAS-001-EC-CONTRACT-001", "Functionally complete — 100%"],
    "docs/project/canonical-consolidation-matrix.md": ["version: 1.21.0", "KPIs, Guardrails, Cenários e Contrato Final da Evolução Contínua"],
    "README.md": ["PAS-001-EC-CONTRACT-001", "Functionally complete — 100%", "Reconciliação e Fechamento"],
    "docs/index.md": ["PAS-001-EC-CONTRACT-001", "Functionally complete — 100%", "Reconciliação e Fechamento"],
    "mkdocs.yml": ["PAS-001-EC-CONTRACT-001"],
    "CHANGELOG.md": ["0.49.0 — Continuous Evolution Functional Completion"],
}
for file_path, tokens in checks.items():
    current = read(file_path)
    for token in tokens:
        if token not in current:
            raise RuntimeError(f"{file_path}: token ausente: {token}")

# Limpeza dos executores temporários
for temporary in (
    ROOT / ".github/scripts/sync_ec_contract.py",
    ROOT / ".github/workflows/sync-ec-contract.yml",
):
    if temporary.exists():
        temporary.unlink()
