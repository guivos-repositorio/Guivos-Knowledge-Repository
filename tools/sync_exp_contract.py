from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str, label: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: {label}: esperado 1 ocorrência, encontrado {count}")
    write(path, text.replace(old, new, 1))


def regex_once(path: str, pattern: str, replacement: str, label: str, flags: int = 0) -> None:
    text = read(path)
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{path}: {label}: esperado 1 match, encontrado {count}")
    write(path, updated)


PA = "docs/product-architecture/index.md"
replace_once(PA, "version: 1.14.0", "version: 1.15.0", "versão")
replace_once(
    PA,
    "- `PAS-001-EXP-INTEGRATION-001 1.0.0` — contrato comum, identidade, associação, autoridade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, capacidades, produtos, organizações, dispositivos, canais, observabilidade e falha segura.\n",
    "- `PAS-001-EXP-INTEGRATION-001 1.0.0` — contrato comum, identidade, associação, autoridade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, capacidades, produtos, organizações, dispositivos, canais, observabilidade e falha segura.\n- `PAS-001-EXP-CONTRACT-001 1.0.0` — 85 KPIs em 17 famílias, 32 guardrails, baseline, painel de saúde, níveis de desempenho, cenários, critérios de conclusão, lacunas, reabertura e contrato final.\n",
    "lista de extensões",
)
contract_summary = """`PAS-001-EXP-CONTRACT-001 1.0.0` consolida:

- 85 KPIs em 17 famílias sistêmicas;
- baseline funcional segmentada;
- painel de saúde com 18 visões e cinco níveis de desempenho;
- 32 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- critérios de conclusão, lacunas bloqueantes e não bloqueantes;
- finalidade, singularidade, titularidade, responsabilidades, limites, entradas, admissão, saídas e dimensões preservadas;
- neutralidade comercial, privacidade, confiabilidade, explicabilidade, auditoria, critérios de reabertura e contrato final;
- ausência de lacuna funcional bloqueante conhecida.

"""
replace_once(
    PA,
    "A Capacidade 08 está **In progress**, com progresso editorial de referência de `90%`.\n\nO próximo bloco deverá consolidar KPIs, guardrails, baseline, cenários e o contrato final das Experiências.",
    contract_summary + "A Capacidade 08 está **Functionally complete**, com progresso editorial de referência de `100%`.\n\nA próxima frente oficial é a Capacidade 09 — Evolução Contínua, que permanece `Planned` até a aprovação de sua primeira extensão normativa.",
    "conclusão da capacidade",
)
text = read(PA)
marker = "| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 |"
if marker in text and "| PAS-001-EXP-CONTRACT-001 | Active 1.0.0 |" not in text:
    text = text.replace(marker, marker + "\n| PAS-001-EXP-CONTRACT-001 | Active 1.0.0 |", 1)
write(PA, text)

ROADMAP = "docs/roadmap.md"
replace_once(ROADMAP, "version: 10.5.0", "version: 10.6.0", "versão")
replace_once(
    ROADMAP,
    "- **Capacidades concluídas:** `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas` e `07 — Intervenções Contextuais`.",
    "- **Capacidades concluídas:** `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais` e `08 — Experiências`.",
    "capacidades concluídas",
)
replace_once(ROADMAP, "- **Capacidade ativa:** `08 — Experiências`, `In progress`, 90%.", "- **Capacidade concluída:** `08 — Experiências`, `Functionally complete`, 100%.\n- **Próxima capacidade:** `09 — Evolução Contínua`, `Planned`.", "estado atual")
replace_once(
    ROADMAP,
    "- **Extensões normativas vigentes de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0` e `PAS-001-EXP-INTEGRATION-001 1.0.0`.",
    "- **Extensões normativas vigentes de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0`, `PAS-001-EXP-INTEGRATION-001 1.0.0` e `PAS-001-EXP-CONTRACT-001 1.0.0`.",
    "extensões vigentes",
)
replace_once(ROADMAP, "O próximo trabalho deverá consolidar KPIs, guardrails, baseline, cenários e o contrato final da `Capacidade 08 — Experiências`.", "O próximo trabalho deverá consolidar os fundamentos iniciais da `Capacidade 09 — Evolução Contínua`.", "direção vigente")
roadmap_contract = """### Contrato final

- 85 KPIs em 17 famílias;
- baseline funcional segmentada e painel de saúde com 18 visões;
- cinco níveis de desempenho;
- 32 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- 48 critérios de conclusão funcional;
- lacunas bloqueantes e não bloqueantes;
- finalidade, singularidade, titularidade, responsabilidades, limites, entradas, admissão, saídas e dimensões preservadas;
- neutralidade comercial, privacidade, confiabilidade, explicabilidade, auditoria e critérios de reabertura;
- nenhuma lacuna funcional bloqueante conhecida.

A Capacidade 08 está `Functionally complete`, com progresso editorial de referência de `100%`.
"""
replace_once(ROADMAP, "A Capacidade 08 está `In progress`, com progresso editorial de referência de `90%`.", roadmap_contract, "resumo de conclusão")
replace_once(ROADMAP, "| 08 — Experiências | In progress | 90% |", "| 08 — Experiências | Functionally complete | 100% |", "tabela de progresso")
regex_once(
    ROADMAP,
    r"## Ponto exato de retomada\n\nRetomar nos \*\*KPIs, guardrails, baseline, cenários e contrato final da Capacidade 08 — Experiências\*\*\.\n\nPróxima entrega:\n\n1\. famílias de KPIs sistêmicos e baseline funcional segmentada;\n2\. painel de saúde e níveis de desempenho;\n3\. guardrails de tolerância zero;\n4\. cenários funcionalmente ideal, alternativo e limite;\n5\. critérios de conclusão, lacunas bloqueantes e não bloqueantes;\n6\. critérios de reabertura e contrato final da Capacidade 08\.",
    "## Ponto exato de retomada\n\nRetomar nos **Fundamentos Iniciais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. finalidade e pergunta central;\n2. singularidade da evolução contínua;\n3. mudança observada, direção, temporalidade e evidência;\n4. interpretação, causalidade e progresso humano não linear;\n5. autonomia, limites e proteção contra avaliação moral;\n6. relações com as demais capacidades do Journey.",
    "ponto de retomada",
    flags=re.S,
)

BOARD = "docs/project/knowledge-board.md"
replace_once(BOARD, "version: 10.5.0", "version: 10.6.0", "versão")
replace_once(BOARD, "| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais das Experiências |", "| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais das Experiências |\n| PAS-001-EXP-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final das Experiências |", "ativo normativo")
replace_once(BOARD, "| Capacidades concluídas | `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas` e `07 — Intervenções Contextuais` |", "| Capacidades concluídas | `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais` e `08 — Experiências` |", "capacidades concluídas")
replace_once(BOARD, "| Capacidade ativa | `08 — Experiências` |", "| Próxima capacidade | `09 — Evolução Contínua` |", "capacidade ativa")
replace_once(BOARD, "| Estado da capacidade ativa | `In progress` |", "| Estado da próxima capacidade | `Planned` |", "estado da capacidade")
replace_once(BOARD, "| Extensões normativas vigentes | `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0` e `PAS-001-EXP-INTEGRATION-001 1.0.0` |", "| Extensões normativas de Experiências | `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0`, `PAS-001-EXP-INTEGRATION-001 1.0.0` e `PAS-001-EXP-CONTRACT-001 1.0.0` |", "extensões")
replace_once(BOARD, "| Progresso editorial de Experiências | `90%` |", "| Progresso editorial de Experiências | `100%` |", "progresso")
replace_once(BOARD, "| Foco imediato | Consolidar KPIs, guardrails, baseline, cenários e contrato final da Capacidade 08 — Experiências |", "| Foco imediato | Consolidar os fundamentos iniciais da Capacidade 09 — Evolução Contínua |", "foco")
replace_once(BOARD, "| 08 — Experiências | In progress — 90% | Fundamentos, ciclo de vida, visualização, controle, eventos e integrações funcionais consolidados; contrato final é a próxima entrega |", "| 08 — Experiências | Functionally complete — 100% | Seis extensões normativas, 85 KPIs, 32 guardrails, baseline, cenários e contrato final consolidados |", "tabela")
board_contract = """### Contrato final

- 85 KPIs em 17 famílias;
- baseline funcional segmentada;
- painel de saúde com 18 visões;
- cinco níveis de desempenho;
- 32 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- 48 critérios de conclusão funcional;
- lacunas bloqueantes e não bloqueantes;
- finalidade, singularidade, titularidade, responsabilidades, limites, entradas, admissão, saídas e dimensões preservadas;
- neutralidade comercial, privacidade, confiabilidade, explicabilidade, auditoria e critérios de reabertura;
- nenhuma lacuna funcional bloqueante conhecida.

A Capacidade 08 está `Functionally complete`, com progresso editorial de referência de `100%`.

"""
replace_once(BOARD, "A Capacidade 08 está `In progress`, com progresso editorial de referência de `90%`.\n\n", board_contract, "resumo final")
text = read(BOARD)
text = text.replace("| Experiências | In progress — 90% |", "| Experiências | Functionally complete — 100% |")
if "| Contrato Final de Experiências | Normative 1.0.0 |" not in text:
    text = text.replace("| Integrações Funcionais de Experiências | Normative 1.0.0 |", "| Integrações Funcionais de Experiências | Normative 1.0.0 |\n| Contrato Final de Experiências | Normative 1.0.0 |\n| Baseline de Experiências | Construída antes de metas permanentes e segmentada por modalidade, tipo, sensibilidade, origem, estado, participação, resultado, integração e relação comercial |\n| Guardrail de Experiências | Regra crítica cuja violação não pode ser compensada por média positiva |\n| Conclusão funcional de Experiências | Contratos essenciais concluídos; não equivale a implementação ou validação em produção |", 1)
write(BOARD, text)

MATRIX = "docs/project/canonical-consolidation-matrix.md"
replace_once(MATRIX, "version: 1.14.0", "version: 1.15.0", "versão")
replace_once(MATRIX, "| Experiências | Refinar | Capacidade 08 em desenvolvimento, com fundamentos, ciclo de vida, visualização, controle, eventos e integrações funcionais consolidados e progresso editorial de 90% |", "| Experiências | Manter | Capacidade 08 funcionalmente concluída por seis extensões normativas, 85 KPIs, 32 guardrails, baseline, cenários e progresso editorial de 100% |", "estado")
replace_once(MATRIX, "| Integrações Funcionais das Experiências | Manter | PAS-001-EXP-INTEGRATION-001 1.0.0 define contrato comum, identidade, associação, autoridade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, produtos, organizações, dispositivos, observabilidade e falha segura |", "| Integrações Funcionais das Experiências | Manter | PAS-001-EXP-INTEGRATION-001 1.0.0 define contrato comum, identidade, associação, autoridade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, produtos, organizações, dispositivos, observabilidade e falha segura |\n| KPIs, Guardrails, Cenários e Contrato Final das Experiências | Manter | PAS-001-EXP-CONTRACT-001 1.0.0 define 85 KPIs, 17 famílias, 32 guardrails, baseline, painel de saúde, cenários, critérios de conclusão, lacunas, reabertura e contrato final |\n| Baseline de Experiências | Manter | Construída antes de metas permanentes e segmentada por modalidade, tipo, sensibilidade, origem, estado, participação, resultado, integração e relação comercial |\n| Guardrail de Experiências | Manter | Regra crítica cuja violação não pode ser compensada por média positiva |\n| Conclusão funcional de Experiências | Manter | Contratos essenciais concluídos; não equivale a implementação ou validação em produção |", "contrato final")

README = "README.md"
replace_once(README, "- **Capacidades concluídas:** 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas e 07 — Intervenções Contextuais", "- **Capacidades concluídas:** 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais e 08 — Experiências", "capacidades concluídas")
replace_once(README, "- **Capacidade ativa:** 08 — Experiências, `In progress`, 90%", "- **Próxima capacidade:** 09 — Evolução Contínua, `Planned`", "capacidade")
replace_once(README, "- **Extensões vigentes de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0, PAS-001-EXP-LIFECYCLE-001 1.0.0, PAS-001-EXP-VIEW-001 1.0.0, PAS-001-EXP-EVENT-001 1.0.0 e PAS-001-EXP-INTEGRATION-001 1.0.0", "- **Extensões vigentes de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0, PAS-001-EXP-LIFECYCLE-001 1.0.0, PAS-001-EXP-VIEW-001 1.0.0, PAS-001-EXP-EVENT-001 1.0.0, PAS-001-EXP-INTEGRATION-001 1.0.0 e PAS-001-EXP-CONTRACT-001 1.0.0", "extensões")
readme_contract = """`PAS-001-EXP-CONTRACT-001 1.0.0` consolida:

- 85 KPIs em 17 famílias;
- baseline funcional segmentada;
- painel de saúde com 18 visões e cinco níveis de desempenho;
- 32 guardrails de tolerância zero;
- cenários funcionalmente ideais, alternativos e limite;
- critérios de conclusão, lacunas e reabertura;
- contrato funcional final.

A Capacidade 08 está **Functionally complete**, com progresso editorial de referência de **100%**.
"""
replace_once(README, "A Capacidade 08 está **In progress**, com progresso editorial de referência de **90%**.", readme_contract, "resumo")
regex_once(README, r"## Ponto exato de retomada\n\nRetomar nos KPIs, guardrails, baseline, cenários e contrato final da Capacidade 08 — Experiências\.\n\nPróxima entrega:\n\n- famílias de KPIs sistêmicos e baseline funcional segmentada;\n- painel de saúde e níveis de desempenho;\n- guardrails de tolerância zero;\n- cenários funcionalmente ideal, alternativo e limite;\n- critérios de conclusão, lacunas e reabertura;\n- contrato final da Capacidade 08\.", "## Ponto exato de retomada\n\nRetomar nos **Fundamentos Iniciais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- finalidade e pergunta central;\n- singularidade da evolução contínua;\n- mudança observada, direção, temporalidade e evidência;\n- interpretação, causalidade e progresso humano não linear;\n- autonomia, limites e proteção contra avaliação moral;\n- relações com as demais capacidades do Journey.", "retomada", flags=re.S)
replace_once(README, "As Capacidades 06 — Oportunidades Ativas e 07 — Intervenções Contextuais estão `Functionally complete`; a Capacidade 08 — Experiências está `In progress`, com progresso editorial de referência de `90%`.", "As Capacidades 06 — Oportunidades Ativas, 07 — Intervenções Contextuais e 08 — Experiências estão `Functionally complete`; a Capacidade 09 — Evolução Contínua permanece `Planned`.", "product engineering")
replace_once(README, "| 08 — Experiências | In progress — 90% |", "| 08 — Experiências | Functionally complete — 100% |", "tabela")
replace_once(README, "- [Integrações Funcionais das Experiências](docs/product-architecture/pas-001-experiencias-integracoes-funcionais.md)", "- [Integrações Funcionais das Experiências](docs/product-architecture/pas-001-experiencias-integracoes-funcionais.md)\n- [Contrato Final das Experiências](docs/product-architecture/pas-001-experiencias-kpis-cenarios-contrato-final.md)", "link")

DOCS = "docs/index.md"
replace_once(DOCS, "- Capacidades 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas e 07 — Intervenções Contextuais funcionalmente concluídas;", "- Capacidades 02 — Contexto Vivo, 03 — Objetivos, 04 — Eventos de Vida, 05 — Próximos Passos, 06 — Oportunidades Ativas, 07 — Intervenções Contextuais e 08 — Experiências funcionalmente concluídas;", "capacidades")
replace_once(DOCS, "- Capacidade 08 — Experiências em desenvolvimento, `In progress`, 90%;", "- Capacidade 08 — Experiências funcionalmente concluída, `Functionally complete`, 100%;\n- Capacidade 09 — Evolução Contínua como próxima frente, `Planned`;", "estado")
replace_once(DOCS, "- `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0` e `PAS-001-EXP-INTEGRATION-001 1.0.0` como extensões normativas vigentes da Capacidade 08;", "- `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0`, `PAS-001-EXP-INTEGRATION-001 1.0.0` e `PAS-001-EXP-CONTRACT-001 1.0.0` como extensões normativas vigentes da Capacidade 08;", "extensões")
replace_once(DOCS, "Consolidar os **KPIs, guardrails, baseline, cenários e contrato final da Capacidade 08 — Experiências**.", "Consolidar os **Fundamentos Iniciais da Capacidade 09 — Evolução Contínua**.", "missão")
replace_once(DOCS, "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As seis extensões de Intervenções Contextuais concluem a Capacidade 07 com fundamentos, ciclo de vida, visualização, controle, 19 famílias de eventos, integrações, 80 KPIs em 16 famílias, 28 guardrails, baseline, cenários e contrato final. As cinco extensões de Experiências consolidam o vivido, suas distinções, titularidade, ciclo de vida, Minhas Experiências, áreas funcionais, 19 famílias de eventos, contratos de integração, autoridade, finalidade, minimização, proveniência, sensibilidade, sincronização, prevenção de ciclos, correção, revogação, idempotência, reconstrução e falha segura.", "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As seis extensões de Intervenções Contextuais concluem a Capacidade 07 com fundamentos, ciclo de vida, visualização, controle, 19 famílias de eventos, integrações, 80 KPIs em 16 famílias, 28 guardrails, baseline, cenários e contrato final. As seis extensões de Experiências concluem a Capacidade 08 com fundamentos, ciclo de vida, Minhas Experiências, 19 famílias de eventos, integrações, 85 KPIs em 17 famílias, 32 guardrails, baseline, painel de saúde, cenários e contrato final.", "missão detalhada")
replace_once(DOCS, "| 08 — Experiências | In progress — 90% |", "| 08 — Experiências | Functionally complete — 100% |", "tabela")
replace_once(DOCS, "- [Integrações Funcionais das Experiências](product-architecture/pas-001-experiencias-integracoes-funcionais.md)", "- [Integrações Funcionais das Experiências](product-architecture/pas-001-experiencias-integracoes-funcionais.md)\n- [Contrato Final das Experiências](product-architecture/pas-001-experiencias-kpis-cenarios-contrato-final.md)", "link")
regex_once(DOCS, r"## Ponto de retomada\n\nRetomar nos KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários, critérios de conclusão, lacunas, reabertura e contrato final da Capacidade 08 — Experiências\.", "## Ponto de retomada\n\nRetomar nos **Fundamentos Iniciais da Capacidade 09 — Evolução Contínua**.", "retomada")

MKDOCS = "mkdocs.yml"
replace_once(MKDOCS, "      - PAS-001-EXP-INTEGRATION-001 — Integrações Funcionais das Experiências: product-architecture/pas-001-experiencias-integracoes-funcionais.md", "      - PAS-001-EXP-INTEGRATION-001 — Integrações Funcionais das Experiências: product-architecture/pas-001-experiencias-integracoes-funcionais.md\n      - PAS-001-EXP-CONTRACT-001 — Contrato Final das Experiências: product-architecture/pas-001-experiencias-kpis-cenarios-contrato-final.md", "navegação")

CHANGELOG = "CHANGELOG.md"
entry = """## 0.43.0 — Experiences Final Contract

- Criação de `PAS-001-EXP-CONTRACT-001 — KPIs, Guardrails, Cenários e Contrato Final da Capacidade de Experiências`, versão `1.0.0`.
- Registro do documento como sexta extensão normativa e contrato final da Capacidade 08 do `PAS-001 — Guivos Journey`.
- Substituição do estado da Capacidade 08 de `In progress` para `Functionally complete`.
- Elevação do progresso editorial de 90% para 100%.
- Consolidação de 85 KPIs em 17 famílias.
- Definição de baseline funcional segmentada, painel de saúde com 18 visões e cinco níveis de desempenho.
- Consolidação de 32 guardrails de tolerância zero.
- Definição de cenários funcionalmente ideais, alternativos e limite.
- Definição de 48 critérios de conclusão funcional.
- Consolidação de lacunas bloqueantes e não bloqueantes, sem lacuna funcional bloqueante conhecida.
- Consolidação da finalidade, singularidade, titularidade, responsabilidades, limites, entradas, admissão, saídas e dimensões preservadas.
- Consolidação de neutralidade comercial, privacidade, confiabilidade, explicabilidade, auditoria e critérios de reabertura.
- Atualização da Arquitetura de Produtos para `1.15.0` e inclusão do contrato final na navegação do MkDocs.
- Atualização do Roadmap e do Knowledge Board para `10.6.0`.
- Atualização da Matriz de Consolidação Canônica para `1.15.0`.
- Atualização do README e da página inicial do GKR.
- Preservação das Capacidades 02 a 07 como `Functionally complete`.
- Definição da Capacidade 09 — Evolução Contínua como próxima frente oficial, permanecendo `Planned` até sua primeira extensão normativa.
- Definição dos Fundamentos Iniciais da Capacidade 09 como próximo ponto exato de retomada.

"""
replace_once(CHANGELOG, "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n", "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n" + entry, "entrada")
