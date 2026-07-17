from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


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


# Product Architecture
PA = "docs/product-architecture/index.md"
replace_once(PA, "version: 1.13.0", "version: 1.14.0", "versão")
replace_once(
    PA,
    "- `PAS-001-EXP-EVENT-001 1.0.0` — agregado funcional, estrutura comum, 19 famílias de eventos, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução e auditoria.\n",
    "- `PAS-001-EXP-EVENT-001 1.0.0` — agregado funcional, estrutura comum, 19 famílias de eventos, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução e auditoria.\n- `PAS-001-EXP-INTEGRATION-001 1.0.0` — contrato comum, identidade, associação, autoridade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, capacidades, produtos, organizações, dispositivos, canais, observabilidade e falha segura.\n",
    "lista de extensões",
)
pa_integration_summary = """`PAS-001-EXP-INTEGRATION-001 1.0.0` consolida:

- integração funcional como intercâmbio governado sem reconhecimento automático da experiência;
- titularidade, produtores, consumidores, modos, finalidade, autoridade, escopo, sensibilidade, proveniência, temporalidades, permissões, retenção e relação comercial;
- identidade e associação confiáveis, com limitação de efeitos diante de incerteza e correção auditável de associações incorretas;
- qualidade técnica, confiança funcional, completude e autoridade como dimensões independentes;
- transformações permitidas e proibição de fabricar ocorrência, participação, percepção, satisfação, memória, significado, transformação ou evolução;
- minimização, recortes funcionais, consentimento granular, proteção de terceiros e neutralidade comercial;
- séries, episódios, experiências compartilhadas, operação offline e sincronização reconciliável;
- pausa, desconexão, revogação, propagação e retenção residual justificada;
- ordenação, concorrência, prevenção de ciclos, tempo real limitado, lote, retentativas e falha segura;
- integrações com todas as capacidades do Journey, Guivos Intelligence e Platform Layer;
- integrações com Mall, Travel, Business, Media, Ads, organizações, profissionais, setores sensíveis, esportes, dispositivos, calendários, localização, mídias, fontes públicas e sistemas externos;
- observabilidade, explicabilidade, auditoria, reconstrução, 30 comportamentos proibidos e 52 critérios de aceite.

"""
replace_once(
    PA,
    "- correção compensatória, revogação propagada, retenção proporcional, explicabilidade e auditoria;\n- 30 comportamentos proibidos e 60 critérios de aceite.\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de `80%`.\n\nO próximo bloco deverá consolidar as integrações funcionais das Experiências.",
    "- correção compensatória, revogação propagada, retenção proporcional, explicabilidade e auditoria;\n- 30 comportamentos proibidos e 60 critérios de aceite.\n\n" + pa_integration_summary + "A Capacidade 08 está **In progress**, com progresso editorial de referência de `90%`.\n\nO próximo bloco deverá consolidar KPIs, guardrails, baseline, cenários e o contrato final das Experiências.",
    "resumo e progresso",
)
text = read(PA)
if "| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 |" not in text:
    marker = "| PAS-001-EXP-EVENT-001 | Active 1.0.0 |"
    if marker in text:
        text = text.replace(marker, marker + "\n| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 |", 1)
        write(PA, text)


# Roadmap
ROADMAP = "docs/roadmap.md"
replace_once(ROADMAP, "version: 10.4.0", "version: 10.5.0", "versão")
replace_once(ROADMAP, "- **Capacidade ativa:** `08 — Experiências`, `In progress`, 80%.", "- **Capacidade ativa:** `08 — Experiências`, `In progress`, 90%.", "estado atual")
replace_once(
    ROADMAP,
    "- **Extensões normativas vigentes de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0` e `PAS-001-EXP-EVENT-001 1.0.0`.",
    "- **Extensões normativas vigentes de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0` e `PAS-001-EXP-INTEGRATION-001 1.0.0`.",
    "extensões vigentes",
)
replace_once(ROADMAP, "O próximo trabalho deverá consolidar as integrações funcionais da `Capacidade 08 — Experiências`.", "O próximo trabalho deverá consolidar KPIs, guardrails, baseline, cenários e o contrato final da `Capacidade 08 — Experiências`.", "direção vigente")
roadmap_summary = """`PAS-001-EXP-INTEGRATION-001 1.0.0` consolida:

- integração funcional sem transferência de titularidade ou reconhecimento automático do vivido;
- contrato comum com produtor, consumidor, participante, Registro de Experiência, série, episódio, finalidade, modo, autoridade, escopo, sensibilidade, proveniência, qualidade, confiança, incerteza, retenção, permissões, sincronização, revogação e falha;
- identidade, associação incerta, correção de associação incorreta e autoridade limitada por fonte;
- qualidade técnica, confiança funcional, completude, precisão temporal e autoridade como dimensões separadas;
- transformações permitidas e proibição de fabricar ocorrência, participação, percepção, satisfação, memória, significado, transformação ou evolução;
- finalidade específica, minimização, recortes funcionais, consentimento granular, proteção de terceiros e neutralidade comercial;
- séries, episódios, experiências compartilhadas, coletivas, institucionais e operação offline;
- sincronização, divergência, ordenação, concorrência, reconciliação e prevenção de ciclos;
- pausa, desconexão, revogação, propagação, retenção residual, retentativas e falha segura;
- integrações com todas as capacidades do Journey, Intelligence, Platform Layer, produtos especializados, organizações, profissionais, dispositivos, canais e sistemas externos;
- observabilidade, explicabilidade, auditoria, reconstrução, 30 comportamentos proibidos e 52 critérios de aceite.

"""
replace_once(
    ROADMAP,
    "- correção compensatória, revogação propagada, retenção proporcional, explicabilidade e auditoria;\n- 30 comportamentos proibidos e 60 critérios de aceite.\n\nA Capacidade 08 está `In progress`, com progresso editorial de referência de `80%`.",
    "- correção compensatória, revogação propagada, retenção proporcional, explicabilidade e auditoria;\n- 30 comportamentos proibidos e 60 critérios de aceite.\n\n" + roadmap_summary + "A Capacidade 08 está `In progress`, com progresso editorial de referência de `90%`.",
    "resumo de integração",
)
replace_once(ROADMAP, "| 08 — Experiências | In progress | 80% |", "| 08 — Experiências | In progress | 90% |", "tabela de progresso")
regex_once(
    ROADMAP,
    r"## Ponto exato de retomada\n\nRetomar nas \*\*integrações funcionais da Capacidade 08 — Experiências\*\*\.\n\nPróxima entrega:\n\n1\. contrato comum de integração e recortes minimizados;\n2\. titularidade, finalidade, autoridade, proveniência, sensibilidade, permissões e retenção;\n3\. integrações com as Capacidades 01 a 07 e candidatura limitada para Evolução Contínua;\n4\. integrações com Guivos Intelligence, Platform Layer e produtos especializados;\n5\. organizações, profissionais, canais, calendários, localização, dispositivos, mídias, fontes públicas e sistemas externos;\n6\. sincronização, prevenção de ciclos, contestação, correção, revogação, observabilidade e falha segura\.",
    "## Ponto exato de retomada\n\nRetomar nos **KPIs, guardrails, baseline, cenários e contrato final da Capacidade 08 — Experiências**.\n\nPróxima entrega:\n\n1. famílias de KPIs sistêmicos e baseline funcional segmentada;\n2. painel de saúde e níveis de desempenho;\n3. guardrails de tolerância zero;\n4. cenários funcionalmente ideal, alternativo e limite;\n5. critérios de conclusão, lacunas bloqueantes e não bloqueantes;\n6. critérios de reabertura e contrato final da Capacidade 08.",
    "ponto de retomada",
    flags=re.S,
)


# Knowledge Board
BOARD = "docs/project/knowledge-board.md"
replace_once(BOARD, "version: 10.4.0", "version: 10.5.0", "versão")
replace_once(
    BOARD,
    "| PAS-001-EXP-EVENT-001 | Active 1.0.0 | Definir os contratos dos eventos funcionais das Experiências |",
    "| PAS-001-EXP-EVENT-001 | Active 1.0.0 | Definir os contratos dos eventos funcionais das Experiências |\n| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais das Experiências |",
    "ativo normativo",
)
replace_once(
    BOARD,
    "| Extensões normativas vigentes | `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0` e `PAS-001-EXP-EVENT-001 1.0.0` |",
    "| Extensões normativas vigentes | `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0` e `PAS-001-EXP-INTEGRATION-001 1.0.0` |",
    "extensões vigentes",
)
replace_once(BOARD, "| Progresso editorial de Experiências | `80%` |", "| Progresso editorial de Experiências | `90%` |", "progresso")
replace_once(BOARD, "| Foco imediato | Consolidar as integrações funcionais da Capacidade 08 — Experiências |", "| Foco imediato | Consolidar KPIs, guardrails, baseline, cenários e contrato final da Capacidade 08 — Experiências |", "foco")
replace_once(BOARD, "| 08 — Experiências | In progress — 80% | Fundamentos, ciclo de vida, visualização, controle e eventos funcionais consolidados; integrações funcionais são a próxima entrega |", "| 08 — Experiências | In progress — 90% | Fundamentos, ciclo de vida, visualização, controle, eventos e integrações funcionais consolidados; contrato final é a próxima entrega |", "tabela de capacidades")
board_event_summary = """### Eventos funcionais

- distinção entre sinal, comando, proposta, declaração, evento e efeito;
- Registro de Experiência como agregado funcional principal;
- estrutura comum versionada com titular, ator, autoridade, finalidade, temporalidades, proveniência, sensibilidade, permissões, incerteza e retenção;
- 19 famílias de eventos cobrindo identificação, ocorrência, planejamento, participação, encerramento, resultados, percepção, evidências, memórias, significado, privacidade, compartilhamento, correção, revogação, sincronização e reconstrução;
- persistência anterior à publicação, idempotência, ordenação, concorrência, atomicidade, compatibilidade e falha segura;
- correção compensatória, revogação propagada, explicabilidade, auditoria, 30 comportamentos proibidos e 60 critérios de aceite.

### Integrações funcionais

- integração funcional sem reconhecimento automático do vivido;
- contrato comum, produtores, consumidores, titularidade, finalidade, autoridade, escopo, sensibilidade, proveniência, temporalidades, permissões, retenção, sincronização, revogação e falha;
- identidade confiável, associação incerta limitada e correção auditável;
- qualidade, confiança, completude e autoridade separadas;
- transformações permitidas e proibição de fabricar ocorrência, participação, percepção, satisfação, memória, significado, transformação ou evolução;
- minimização, consentimento granular, séries, episódios, experiências compartilhadas, operação offline e proteção de terceiros;
- pausa, desconexão, revogação, propagação, prevenção de ciclos, tempo real limitado e falha segura;
- integrações com capacidades, produtos, organizações, profissionais, dispositivos, canais e sistemas externos;
- observabilidade, explicabilidade, auditoria, reconstrução, 30 comportamentos proibidos e 52 critérios de aceite.

A Capacidade 08 está `In progress`, com progresso editorial de referência de `90%`.
"""
regex_once(
    BOARD,
    r"A Capacidade 08 está `In progress`, com progresso editorial de referência de `60%`\.",
    board_event_summary,
    "consolidação da capacidade",
)
text = read(BOARD)
text = text.replace("| Experiências | In progress — 60% |", "| Experiências | In progress — 90% |")
if "| Eventos Funcionais de Experiências | Normative 1.0.0 |" not in text:
    text = text.replace("| Visualização e Controle de Experiências | Normative 1.0.0 |", "| Visualização e Controle de Experiências | Normative 1.0.0 |\n| Eventos Funcionais de Experiências | Normative 1.0.0 |\n| Integrações Funcionais de Experiências | Normative 1.0.0 |", 1)
if "| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 |" not in text:
    text = text.replace("| PAS-001-EXP-EVENT-001 | Active 1.0.0 |", "| PAS-001-EXP-EVENT-001 | Active 1.0.0 |\n| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 |", 1)
text = re.sub(r"\| Roadmap \| \d+\.\d+\.\d+ \|", "| Roadmap | 10.5.0 |", text)
text = re.sub(r"\| Knowledge Board \| \d+\.\d+\.\d+ \|", "| Knowledge Board | 10.5.0 |", text)
text = re.sub(
    r"## (?:Próxima atividade|Próximo ponto de retomada)\n\n.*\Z",
    "## Próxima atividade\n\nConsolidar os **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão, lacunas bloqueantes e não bloqueantes, critérios de reabertura e contrato final da Capacidade 08 — Experiências**.",
    text,
    flags=re.S,
)
write(BOARD, text)


# Canonical Consolidation Matrix
MATRIX = "docs/project/canonical-consolidation-matrix.md"
replace_once(MATRIX, "version: 1.13.0", "version: 1.14.0", "versão")
replace_once(
    MATRIX,
    "| Experiências | Refinar | Capacidade 08 em desenvolvimento, com fundamentos, ciclo de vida, visualização, controle e eventos funcionais consolidados e progresso editorial de 80% |",
    "| Experiências | Refinar | Capacidade 08 em desenvolvimento, com fundamentos, ciclo de vida, visualização, controle, eventos e integrações funcionais consolidados e progresso editorial de 90% |",
    "estado de Experiências",
)
replace_once(
    MATRIX,
    "| Eventos Funcionais das Experiências | Manter | PAS-001-EXP-EVENT-001 1.0.0 define Registro de Experiência, estrutura comum, 19 famílias de eventos, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução e auditoria |",
    "| Eventos Funcionais das Experiências | Manter | PAS-001-EXP-EVENT-001 1.0.0 define Registro de Experiência, estrutura comum, 19 famílias de eventos, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, ordenação, concorrência, reconstrução e auditoria |\n| Integrações Funcionais das Experiências | Manter | PAS-001-EXP-INTEGRATION-001 1.0.0 define contrato comum, identidade, associação, autoridade, finalidade, minimização, proveniência, sincronização, prevenção de ciclos, revogação, produtos, organizações, dispositivos, observabilidade e falha segura |",
    "documento de integração",
)
replace_once(
    MATRIX,
    "| Contrato de evento de experiência | Manter | Estrutura comum com agregado, versões, titular, ator, autoridade, finalidade, temporalidades, proveniência, sensibilidade, idempotência, incerteza e retenção |",
    "| Contrato de evento de experiência | Manter | Estrutura comum com agregado, versões, titular, ator, autoridade, finalidade, temporalidades, proveniência, sensibilidade, idempotência, incerteza e retenção |\n| Integração funcional de experiência | Refinar | Intercâmbio governado de sinais, fatos, declarações, evidências, mídias, resultados e recortes sem reconhecimento automático do vivido |\n| Contrato de integração de experiência | Manter | Define produtor, consumidor, participante, experiência, série, episódio, finalidade, modo, autoridade, escopo, sensibilidade, proveniência, qualidade, confiança, incerteza, retenção, sincronização, revogação e falha |",
    "conceitos de integração",
)
text = read(MATRIX)
text = re.sub(r"\| Roadmap \| \d+\.\d+\.\d+ \|", "| Roadmap | 10.5.0 |", text)
text = re.sub(r"\| Knowledge Board \| \d+\.\d+\.\d+ \|", "| Knowledge Board | 10.5.0 |", text)
if "| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 |" not in text:
    text = text.replace("| PAS-001-EXP-EVENT-001 | Active 1.0.0 |", "| PAS-001-EXP-EVENT-001 | Active 1.0.0 |\n| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 |", 1)
write(MATRIX, text)


# README
README = "README.md"
replace_once(README, "- **Capacidade ativa:** 08 — Experiências, `In progress`, 80%", "- **Capacidade ativa:** 08 — Experiências, `In progress`, 90%", "status")
replace_once(
    README,
    "- **Extensões vigentes de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0, PAS-001-EXP-LIFECYCLE-001 1.0.0, PAS-001-EXP-VIEW-001 1.0.0 e PAS-001-EXP-EVENT-001 1.0.0",
    "- **Extensões vigentes de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0, PAS-001-EXP-LIFECYCLE-001 1.0.0, PAS-001-EXP-VIEW-001 1.0.0, PAS-001-EXP-EVENT-001 1.0.0 e PAS-001-EXP-INTEGRATION-001 1.0.0",
    "extensões",
)
readme_summary = """`PAS-001-EXP-INTEGRATION-001 1.0.0` consolida:

- integração funcional sem transferência de titularidade ou reconhecimento automático do vivido;
- contrato comum, produtores, consumidores, identidade, associação, autoridade, finalidade, escopo, sensibilidade, proveniência, temporalidades, permissões, retenção, sincronização, revogação e falha;
- transformações permitidas e proibição de fabricar ocorrência, participação, percepção, satisfação, memória, significado, transformação ou evolução;
- minimização, consentimento granular, séries, episódios, experiências compartilhadas, operação offline e proteção de terceiros;
- prevenção de ciclos, pausa, desconexão, revogação propagada, observabilidade, explicabilidade, auditoria e reconstrução;
- integrações com capacidades, produtos, organizações, profissionais, dispositivos, canais e sistemas externos;
- 30 comportamentos proibidos e 52 critérios de aceite.

"""
replace_once(
    README,
    "- correção compensatória, revogação propagada, retenção proporcional, explicabilidade e auditoria;\n- 30 comportamentos proibidos e 60 critérios de aceite.\n\nA Capacidade 08 está **In progress**, com progresso editorial de referência de **80%**.",
    "- correção compensatória, revogação propagada, retenção proporcional, explicabilidade e auditoria;\n- 30 comportamentos proibidos e 60 critérios de aceite.\n\n" + readme_summary + "A Capacidade 08 está **In progress**, com progresso editorial de referência de **90%**.",
    "resumo e progresso",
)
regex_once(
    README,
    r"## Ponto exato de retomada\n\nRetomar nas integrações funcionais da Capacidade 08 — Experiências\.\n\nPróxima entrega:\n\n(?:- .*\n)+",
    "## Ponto exato de retomada\n\nRetomar nos KPIs, guardrails, baseline, cenários e contrato final da Capacidade 08 — Experiências.\n\nPróxima entrega:\n\n- famílias de KPIs sistêmicos e baseline funcional segmentada;\n- painel de saúde e níveis de desempenho;\n- guardrails de tolerância zero;\n- cenários funcionalmente ideal, alternativo e limite;\n- critérios de conclusão, lacunas e reabertura;\n- contrato final da Capacidade 08.\n\n",
    "retomada",
)
text = read(README)
text = text.replace("a Capacidade 08 — Experiências está `In progress`, com progresso editorial de referência de `40%`", "a Capacidade 08 — Experiências está `In progress`, com progresso editorial de referência de `90%`")
text = text.replace("| 08 — Experiências | In progress — 40% |", "| 08 — Experiências | In progress — 90% |")
if "[Integrações Funcionais das Experiências]" not in text:
    text = text.replace("- [Eventos Funcionais das Experiências](docs/product-architecture/pas-001-experiencias-eventos-funcionais.md)", "- [Eventos Funcionais das Experiências](docs/product-architecture/pas-001-experiencias-eventos-funcionais.md)\n- [Integrações Funcionais das Experiências](docs/product-architecture/pas-001-experiencias-integracoes-funcionais.md)", 1)
write(README, text)


# Site home
HOME = "docs/index.md"
replace_once(HOME, "- Capacidade 08 — Experiências em desenvolvimento, `In progress`, 80%;", "- Capacidade 08 — Experiências em desenvolvimento, `In progress`, 90%;", "progresso")
replace_once(
    HOME,
    "- `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0` e `PAS-001-EXP-EVENT-001 1.0.0` como extensões normativas vigentes da Capacidade 08;",
    "- `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0` e `PAS-001-EXP-INTEGRATION-001 1.0.0` como extensões normativas vigentes da Capacidade 08;",
    "extensões",
)
replace_once(HOME, "Consolidar as **integrações funcionais da Capacidade 08 — Experiências**.", "Consolidar os **KPIs, guardrails, baseline, cenários e contrato final da Capacidade 08 — Experiências**.", "missão")
replace_once(
    HOME,
    "As quatro extensões de Experiências consolidam o vivido, suas distinções, titularidade, ciclo de vida, Minhas Experiências, áreas funcionais, eventos funcionais, 19 famílias, autoridade, finalidade, temporalidades, proveniência, sensibilidade, correção, revogação, idempotência, reconstrução e falha segura.",
    "As cinco extensões de Experiências consolidam o vivido, suas distinções, titularidade, ciclo de vida, Minhas Experiências, áreas funcionais, 19 famílias de eventos, contratos de integração, autoridade, finalidade, minimização, proveniência, sensibilidade, sincronização, prevenção de ciclos, correção, revogação, idempotência, reconstrução e falha segura.",
    "síntese",
)
text = read(HOME)
if "[Integrações Funcionais das Experiências]" not in text:
    text = text.replace("- [Eventos Funcionais das Experiências](product-architecture/pas-001-experiencias-eventos-funcionais.md)", "- [Eventos Funcionais das Experiências](product-architecture/pas-001-experiencias-eventos-funcionais.md)\n- [Integrações Funcionais das Experiências](product-architecture/pas-001-experiencias-integracoes-funcionais.md)", 1)
text = text.replace("| 08 — Experiências | In progress — 80% |", "| 08 — Experiências | In progress — 90% |")
text = re.sub(
    r"## Ponto de retomada\n\n.*\Z",
    "## Ponto de retomada\n\nRetomar nos KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários, critérios de conclusão, lacunas, reabertura e contrato final da Capacidade 08 — Experiências.",
    text,
    flags=re.S,
)
write(HOME, text)


# MkDocs navigation
MKDOCS = "mkdocs.yml"
replace_once(
    MKDOCS,
    "      - PAS-001-EXP-EVENT-001 — Eventos Funcionais das Experiências: product-architecture/pas-001-experiencias-eventos-funcionais.md",
    "      - PAS-001-EXP-EVENT-001 — Eventos Funcionais das Experiências: product-architecture/pas-001-experiencias-eventos-funcionais.md\n      - PAS-001-EXP-INTEGRATION-001 — Integrações Funcionais das Experiências: product-architecture/pas-001-experiencias-integracoes-funcionais.md",
    "navegação",
)


# Changelog
CHANGELOG = "CHANGELOG.md"
entry = """## 0.42.0 — Experiences Functional Integrations

- Criação de `PAS-001-EXP-INTEGRATION-001 — Integrações Funcionais da Capacidade de Experiências`, versão `1.0.0`.
- Registro do documento como quinta extensão normativa da Capacidade 08 do `PAS-001 — Guivos Journey`.
- Manutenção da Capacidade 08 como `In progress` e elevação do progresso editorial de 80% para 90%.
- Definição da integração funcional como intercâmbio governado sem reconhecimento automático da experiência.
- Consolidação do contrato comum com produtor, consumidor, participante, Registro de Experiência, série, episódio, finalidade, modo, autoridade, escopo, sensibilidade, proveniência, qualidade, confiança, incerteza, retenção, sincronização, revogação e falha.
- Definição de identidade, associação incerta, associação incorreta e autoridade por participante, organização, profissional, dispositivo, sensor e sistema transacional.
- Separação entre qualidade técnica, confiança funcional, completude, precisão temporal e autoridade.
- Definição de transformações permitidas e proibição de fabricar ocorrência, participação, percepção, satisfação, memória, significado, transformação ou evolução.
- Consolidação de finalidade específica, minimização, recortes funcionais, consentimento granular, proteção de terceiros e neutralidade comercial.
- Definição de séries, episódios, experiências compartilhadas, coletivas, institucionais e operação offline.
- Consolidação de sincronização, divergência, ordenação, concorrência, reconciliação e prevenção de ciclos.
- Definição de pausa, desconexão, revogação, propagação, retenção residual, retentativas e falha segura.
- Consolidação das integrações com todas as capacidades do Journey, Guivos Intelligence e Platform Layer.
- Consolidação das integrações com Mall, Travel, Business, Media, Ads, organizações, profissionais, setores sensíveis, esportes, dispositivos, calendários, localização, mídias, fontes públicas e sistemas externos.
- Registro de 30 comportamentos proibidos e 52 critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.14.0` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap e do Knowledge Board para `10.5.0`.
- Atualização da Matriz de Consolidação Canônica para `1.14.0`.
- Atualização do README e da página inicial do GKR.
- Preservação das Capacidades 02, 03, 04, 05, 06 e 07 como `Functionally complete`.
- Preservação da Capacidade 09 — Evolução Contínua como `Planned`.
- Definição dos KPIs, guardrails, baseline, cenários e contrato final de Experiências como próximo ponto exato de retomada.

"""
replace_once(
    CHANGELOG,
    "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n",
    "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n" + entry,
    "entrada 0.42.0",
)

print("Sincronização normativa de Integrações Funcionais concluída.")
