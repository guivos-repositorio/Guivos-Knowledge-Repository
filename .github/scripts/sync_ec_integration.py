from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 ocorrência, encontrado {count}")
    return text.replace(old, new, 1)


def insert_after_once(text: str, anchor: str, insertion: str, label: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 anchor, encontrado {count}")
    return text.replace(anchor, anchor + insertion, 1)


def insert_before_after(text: str, start_anchor: str, end_marker: str, insertion: str, label: str) -> str:
    start = text.find(start_anchor)
    if start < 0:
        raise RuntimeError(f"{label}: start anchor ausente")
    end = text.find(end_marker, start)
    if end < 0:
        raise RuntimeError(f"{label}: end marker ausente")
    if insertion.strip() in text[start:end]:
        raise RuntimeError(f"{label}: inserção já presente")
    return text[:end] + insertion + text[end:]


def replace_lines_containing(text: str, required: tuple[str, ...], old: str, new: str) -> str:
    lines = text.splitlines(keepends=True)
    changed = 0
    for idx, line in enumerate(lines):
        if all(token in line for token in required) and old in line:
            lines[idx] = line.replace(old, new)
            changed += 1
    if changed == 0:
        raise RuntimeError(f"nenhuma linha alterada para {required} / {old}")
    return "".join(lines)


DOC = "docs/product-architecture/pas-001-evolucao-continua-integracoes-funcionais.md"
doc = read(DOC)
sections = [int(value) for value in re.findall(r"^# (\d+)\.", doc, flags=re.MULTILINE)]
expected_sections = list(range(4284, 4401))
if sections != expected_sections:
    raise RuntimeError(f"sequência normativa inválida: {sections[:3]} ... {sections[-3:] if sections else []}")

for section, expected_count in ((4397, 36), (4398, 58), (4399, 52)):
    start = doc.index(f"# {section}.")
    next_heading = doc.find("\n# ", start + 3)
    block = doc[start:] if next_heading < 0 else doc[start:next_heading]
    numbered = re.findall(r"^\d+\. ", block, flags=re.MULTILINE)
    if len(numbered) != expected_count:
        raise RuntimeError(f"seção {section}: esperado {expected_count}, encontrado {len(numbered)}")

integration_summary_index = """

`PAS-001-EC-INTEGRATION-001 1.0.0` consolida:

- integração funcional como intercâmbio governado sem reconhecimento automático de evolução;
- contrato comum com produtores, consumidores, participante, trajetória, segmento, finalidade, modo, autoridade, dimensão, baseline, direção, escopo, sensibilidade, proveniência, qualidade, confiança, incerteza, temporalidades, permissões, retenção, sincronização e revogação;
- identidade, associação, titularidade, autoridade, finalidade, minimização, proveniência e temporalidades com limites explícitos;
- qualidade técnica, confiança funcional e autoridade como dimensões independentes;
- transformações permitidas e proibição de fabricar evolução, progresso, regressão, direção, baseline, intenção, significado, mérito, fé, diagnóstico ou causalidade;
- consentimento granular, pausa, desconexão, revogação propagada e retenção residual justificada;
- sincronização, divergência, ordenação, concorrência, reconciliação e prevenção de ciclos;
- integrações com todas as capacidades do Journey, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, dispositivos, canais e sistemas externos;
- proteção de saúde, espiritualidade, trabalho, educação, finanças, voluntariado, fontes públicas e terceiros;
- observabilidade, explicabilidade, auditoria, reconstrução, 36 comportamentos proibidos e 58 critérios de aceite.
"""

integration_summary_board = """

### Integrações funcionais

- integração funcional sem reconhecimento automático de evolução;
- contrato comum com produtores, consumidores, participante, trajetória, segmento, finalidade, autoridade, dimensão, baseline, direção, escopo, sensibilidade, proveniência, temporalidades, permissões, retenção, sincronização e revogação;
- identidade, associação, titularidade, autoridade, finalidade, minimização e proveniência governadas;
- qualidade técnica, confiança funcional, incerteza e autoridade separadas;
- transformações permitidas e proibição de fabricar evolução, progresso, regressão, baseline, direção, intenção, significado, mérito, fé, diagnóstico ou causalidade;
- pausa, desconexão, revogação propagada, retenção residual, sincronização, divergência, ordenação, concorrência, reconciliação e prevenção de ciclos;
- integrações com capacidades, produtos, organizações, profissionais, dispositivos, canais e sistemas externos;
- observabilidade, explicabilidade, auditoria, reconstrução, 36 comportamentos proibidos e 58 critérios de aceite.
"""

# Arquitetura de Produtos
path = "docs/product-architecture/index.md"
text = read(path)
text = replace_once(text, "version: 1.19.0", "version: 1.20.0", f"{path} versão")
text = replace_once(
    text,
    "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `80%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0`.",
    "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `90%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0`.",
    f"{path} estado inicial",
)
text = insert_before_after(
    text,
    "`PAS-001-EC-EVENT-001 1.0.0` consolida:",
    "\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `80%`.",
    integration_summary_index,
    f"{path} resumo integração",
)
text = replace_once(text, "A Capacidade 09 está `In progress`, com progresso editorial de referência de `80%`.", "A Capacidade 09 está `In progress`, com progresso editorial de referência de `90%`.", f"{path} progresso")
text = replace_once(text, "O próximo bloco normativo são as integrações funcionais da Evolução Contínua.", "O próximo bloco normativo consolida KPIs, guardrails, baseline, painel de saúde, níveis de desempenho, cenários e contrato funcional final da Evolução Contínua.", f"{path} próximo bloco")
write(path, text)

# Roadmap
path = "docs/roadmap.md"
text = read(path)
text = replace_once(text, "version: 11.0.0", "version: 11.1.0", f"{path} versão")
text = replace_once(text, "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 80%.", "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 90%.", f"{path} capacidade ativa")
text = replace_once(
    text,
    "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0`.",
    "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0`.",
    f"{path} extensões",
)
text = replace_once(text, "O próximo trabalho deverá consolidar as integrações funcionais da `Capacidade 09 — Evolução Contínua`.", "O próximo trabalho deverá consolidar os KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários e contrato final da `Capacidade 09 — Evolução Contínua`.", f"{path} direção")
text = insert_before_after(text, "`PAS-001-EC-EVENT-001 1.0.0`", "\nA Capacidade 09", integration_summary_index.replace("consolida:", "consolidou:"), f"{path} resumo integração")
text = replace_lines_containing(text, ("Capacidade 09",), "80%", "90%")
text = replace_once(
    text,
    "Retomar nas **Integrações Funcionais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. contrato comum de integração, identidade, associação, finalidade e autoridade;\n2. minimização, proveniência, temporalidades, qualidade, confiança e incerteza;\n3. sincronização, prevenção de ciclos, ordenação, concorrência e reconciliação;\n4. correção, pausa, desconexão, revogação, propagação e retenção residual;\n5. integrações internas, externas, profissionais, organizacionais, dispositivos, canais, observabilidade e falha segura.",
    "Retomar em **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. KPIs e famílias de indicadores sistêmicos;\n2. guardrails de tolerância zero e baseline funcional segmentada;\n3. painel de saúde, níveis de desempenho e metas posteriores à baseline;\n4. cenários funcionalmente ideal, alternativo e limite;\n5. critérios de conclusão, lacunas, reabertura e contrato funcional final.",
    f"{path} ponto de retomada",
)
write(path, text)

# Knowledge Board
path = "docs/project/knowledge-board.md"
text = read(path)
text = replace_once(text, "version: 11.0.0", "version: 11.1.0", f"{path} versão")
text = insert_after_once(text, "| PAS-001-EC-EVENT-001 | Active 1.0.0 | Definir os contratos dos eventos funcionais da Evolução Contínua |", "\n| PAS-001-EC-INTEGRATION-001 | Active 1.0.0 | Definir as integrações funcionais da Evolução Contínua |", f"{path} ativo integração")
text = replace_once(text, "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0` |", "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0` |", f"{path} extensões")
text = replace_once(text, "| Foco imediato | Consolidar as integrações funcionais da Capacidade 09 — Evolução Contínua |", "| Foco imediato | Consolidar KPIs, guardrails, baseline, cenários e contrato final da Capacidade 09 — Evolução Contínua |", f"{path} foco")
text = replace_once(text, "| 09 — Evolução Contínua | In progress — 80% | Quatro extensões normativas consolidadas; integrações funcionais como próximo bloco |", "| 09 — Evolução Contínua | In progress — 90% | Cinco extensões normativas consolidadas; contrato final como próximo bloco |", f"{path} capacidade")
text = replace_once(text, "## Consolidação inicial da Capacidade 09 — Evolução Contínua", "## Consolidação da Capacidade 09 — Evolução Contínua", f"{path} título consolidação")
text = insert_before_after(text, "## Consolidação da Capacidade 09 — Evolução Contínua", "\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `80%`.", integration_summary_board, f"{path} resumo integração")
text = replace_lines_containing(text, ("Evolução Contínua",), "80%", "90%")
text = replace_lines_containing(text, ("Capacidade 09",), "80%", "90%")
text = insert_after_once(text, "| Contrato de evento de evolução | Estrutura comum com trajetória, segmento, participante, ator, autoridade, baseline, direção, temporalidades, proveniência, confiança, permissões e retenção |", "\n| Integração funcional de evolução | Intercâmbio governado de sinais, fatos, observações, evidências, interpretações, comandos, propostas e recortes sem reconhecimento automático |\n| Contrato de integração de evolução | Define produtor, consumidor, participante, trajetória, segmento, finalidade, modo, autoridade, dimensão, baseline, direção, escopo, sensibilidade, proveniência, confiança, incerteza, temporalidades, retenção, sincronização e revogação |", f"{path} conceitos integração")
text = insert_after_once(text, "| PAS-001-EC-EVENT-001 | Active 1.0.0 |", "\n| PAS-001-EC-INTEGRATION-001 | Active 1.0.0 |", f"{path} governança integração")
text = text.replace("| Roadmap | 11.0.0 |", "| Roadmap | 11.1.0 |")
text = text.replace("| Knowledge Board | 11.0.0 |", "| Knowledge Board | 11.1.0 |")
text = replace_once(text, "Consolidar as **Integrações Funcionais da Capacidade 09 — Evolução Contínua**, incluindo contrato comum, identidade, associação, finalidade, autoridade, minimização, proveniência, temporalidades, qualidade, confiança, incerteza, sincronização, prevenção de ciclos, correção, pausa, desconexão, revogação, propagação, observabilidade, neutralidade comercial e falha segura.", "Consolidar **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários e contrato funcional final da Capacidade 09 — Evolução Contínua**, incluindo critérios de conclusão, lacunas bloqueantes e não bloqueantes e critérios de reabertura.", f"{path} próxima atividade")
write(path, text)

# Matriz Canônica
path = "docs/project/canonical-consolidation-matrix.md"
text = read(path)
text = replace_once(text, "version: 1.19.0", "version: 1.20.0", f"{path} versão")
text = replace_once(text, "| Evolução Contínua | Refinar | Capacidade 09 ativa em 80%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |", "| Evolução Contínua | Refinar | Capacidade 09 ativa em 90%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |", f"{path} estado")
text = insert_after_once(text, "| Eventos Funcionais da Evolução Contínua | Manter | PAS-001-EC-EVENT-001 1.0.0 define Trajetória de Evolução, estrutura comum, 19 famílias, autoridade, finalidade, baseline, direção, temporalidades, proveniência, confiança, incerteza, correção, revogação, idempotência, ordenação, concorrência, reconstrução e auditoria |", "\n| Integrações Funcionais da Evolução Contínua | Manter | PAS-001-EC-INTEGRATION-001 1.0.0 define contrato comum, identidade, associação, titularidade, autoridade, finalidade, minimização, proveniência, temporalidades, confiança, incerteza, sincronização, prevenção de ciclos, revogação, produtos, organizações, dispositivos, observabilidade e falha segura |", f"{path} linha integração")
text = insert_after_once(text, "| Contrato de evento de evolução | Manter | Estrutura comum com trajetória, segmento, participante, ator, autoridade, baseline, direção, temporalidades, proveniência, confiança, permissões e retenção |", "\n| Integração funcional de evolução | Refinar | Intercâmbio governado de sinais, fatos, observações, evidências, interpretações, propostas, comandos e recortes sem reconhecimento automático |\n| Contrato de integração de evolução | Manter | Define produtor, consumidor, participante, trajetória, segmento, finalidade, modo, autoridade, dimensão, baseline, direção, escopo, sensibilidade, proveniência, qualidade, confiança, incerteza, temporalidades, retenção, sincronização e revogação |", f"{path} conceitos integração")
text = replace_once(text, "As Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0` mantêm a Capacidade 09 como `In progress — 80%` e consolidam finalidade, Trajetória de Evolução, direção, baseline, estados, transições, visualização, estrutura comum, 19 famílias de eventos, evidências, interpretações, confiança, incerteza, causalidade, controles, privacidade, contestação, correção, revogação, idempotência, ordenação, concorrência, reconstrução e falha segura, sem promover candidatos arquiteturais à Canon.", "As Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0` mantêm a Capacidade 09 como `In progress — 90%` e consolidam finalidade, Trajetória de Evolução, direção, baseline, estados, transições, visualização, estrutura comum, 19 famílias de eventos, contrato comum de integração, identidade, associação, autoridade, minimização, proveniência, temporalidades, evidências, interpretações, confiança, incerteza, causalidade, sincronização, prevenção de ciclos, controles, privacidade, contestação, correção, revogação, idempotência, ordenação, concorrência, reconstrução e falha segura, sem promover candidatos arquiteturais à Canon.", f"{path} reconciliação")
text = replace_once(text, "Consolidar as **integrações funcionais da Capacidade 09 — Evolução Contínua**, incluindo contrato comum, identidade, associação, autoridade, finalidade, minimização, proveniência, temporalidades, sincronização, prevenção de ciclos, correção, revogação, propagação, observabilidade, neutralidade comercial e falha segura.", "Consolidar **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários e contrato funcional final da Capacidade 09 — Evolução Contínua**, incluindo critérios de conclusão, lacunas bloqueantes e não bloqueantes e critérios de reabertura.", f"{path} próxima revisão")
write(path, text)

# README
path = "README.md"
text = read(path)
text = replace_once(text, "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 80%`", "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 90%`", f"{path} status")
text = replace_once(text, "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0, PAS-001-EC-LIFECYCLE-001 1.0.0, PAS-001-EC-VIEW-001 1.0.0 e PAS-001-EC-EVENT-001 1.0.0", "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0, PAS-001-EC-LIFECYCLE-001 1.0.0, PAS-001-EC-VIEW-001 1.0.0, PAS-001-EC-EVENT-001 1.0.0 e PAS-001-EC-INTEGRATION-001 1.0.0", f"{path} extensões")
text = insert_after_once(text, "`PAS-001-EC-EVENT-001 1.0.0` consolida a `Trajetória de Evolução` como agregado funcional, estrutura comum versionada, 19 famílias de eventos, autoridade, finalidade, dimensão, baseline, direção, temporalidades, proveniência, sensibilidade, confiança, incerteza, correção compensatória, revogação, idempotência, ordenação, concorrência, reconstrução, explicabilidade, auditoria e falha segura.", "\n\n`PAS-001-EC-INTEGRATION-001 1.0.0` consolida o contrato comum de integração, identidade, associação, titularidade, autoridade, finalidade, minimização, proveniência, temporalidades, sensibilidade, confiança, incerteza, transformações, sincronização, prevenção de ciclos, correção, pausa, desconexão, revogação, propagação, integrações internas e externas, observabilidade, explicabilidade, auditoria, reconstrução e falha segura.", f"{path} resumo integração")
text = replace_once(text, "A Capacidade 09 está **In progress**, com progresso editorial de referência de **80%**.", "A Capacidade 09 está **In progress**, com progresso editorial de referência de **90%**.", f"{path} progresso")
text = replace_once(text, "Retomar nas **Integrações Funcionais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- contrato comum, identidade, associação, finalidade e autoridade;\n- minimização, proveniência, temporalidades, qualidade, confiança e incerteza;\n- sincronização, prevenção de ciclos, ordenação, concorrência e reconciliação;\n- correção, pausa, desconexão, revogação, propagação e retenção residual;\n- integrações internas, externas, profissionais, organizacionais, dispositivos, canais, observabilidade e falha segura.", "Retomar em **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- KPIs e famílias de indicadores sistêmicos;\n- guardrails de tolerância zero e baseline funcional segmentada;\n- painel de saúde, níveis de desempenho e metas posteriores à baseline;\n- cenários funcionalmente ideal, alternativo e limite;\n- critérios de conclusão, lacunas, reabertura e contrato funcional final.", f"{path} retomada")
text = text.replace("a Capacidade 09 — Evolução Contínua está `In progress — 80%`", "a Capacidade 09 — Evolução Contínua está `In progress — 90%`")
text = replace_once(text, "| 09 — Evolução Contínua | In progress — 80% |", "| 09 — Evolução Contínua | In progress — 90% |", f"{path} tabela")
text = insert_after_once(text, "- [Eventos Funcionais da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-eventos-funcionais.md)", "\n- [Integrações Funcionais da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-integracoes-funcionais.md)", f"{path} acesso rápido")
write(path, text)

# Página inicial
path = "docs/index.md"
text = read(path)
text = replace_once(text, "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 80%;", "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 90%;", f"{path} status")
text = replace_once(text, "- `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0` como extensões normativas vigentes da Capacidade 09;", "- `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0`, `PAS-001-EC-EVENT-001 1.0.0` e `PAS-001-EC-INTEGRATION-001 1.0.0` como extensões normativas vigentes da Capacidade 09;", f"{path} extensões")
text = replace_once(text, "Consolidar as **Integrações Funcionais da Capacidade 09 — Evolução Contínua**.", "Consolidar **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários e contrato funcional final da Capacidade 09 — Evolução Contínua**.", f"{path} missão")
text = replace_once(text, "As quatro extensões de Evolução Contínua mantêm a Capacidade 09 ativa com fundamentos, ciclo de vida, `Minha Evolução`, `Trajetória de Evolução` como agregado, estrutura comum, 19 famílias de eventos, direção, baseline, temporalidades, evidências, causalidade, não linearidade, estados, transições, interpretações alternativas, controles, privacidade, contestação, correção, revogação, idempotência, ordenação, concorrência, reconstrução e falha segura.", "As cinco extensões de Evolução Contínua mantêm a Capacidade 09 ativa com fundamentos, ciclo de vida, `Minha Evolução`, `Trajetória de Evolução` como agregado, estrutura comum, 19 famílias de eventos, contrato comum de integração, identidade, associação, titularidade, autoridade, finalidade, minimização, proveniência, temporalidades, evidências, causalidade, não linearidade, estados, transições, interpretações alternativas, sincronização, prevenção de ciclos, controles, privacidade, contestação, correção, revogação, idempotência, ordenação, concorrência, reconstrução e falha segura.", f"{path} síntese")
text = insert_after_once(text, "- [Eventos Funcionais da Evolução Contínua](product-architecture/pas-001-evolucao-continua-eventos-funcionais.md)", "\n- [Integrações Funcionais da Evolução Contínua](product-architecture/pas-001-evolucao-continua-integracoes-funcionais.md)", f"{path} acesso rápido")
text = replace_once(text, "| 09 — Evolução Contínua | In progress — 80% |", "| 09 — Evolução Contínua | In progress — 90% |", f"{path} tabela")
text = replace_once(text, "Retomar nas **Integrações Funcionais da Capacidade 09 — Evolução Contínua**.", "Retomar em **KPIs, Guardrails, Cenários e Contrato Final da Capacidade 09 — Evolução Contínua**.", f"{path} retomada")
write(path, text)

# MkDocs
path = "mkdocs.yml"
text = read(path)
text = insert_after_once(text, "      - PAS-001-EC-EVENT-001 — Eventos Funcionais da Evolução Contínua: product-architecture/pas-001-evolucao-continua-eventos-funcionais.md", "\n      - PAS-001-EC-INTEGRATION-001 — Integrações Funcionais da Evolução Contínua: product-architecture/pas-001-evolucao-continua-integracoes-funcionais.md", f"{path} nav")
write(path, text)

# Changelog
path = "CHANGELOG.md"
text = read(path)
entry = """
## 0.48.0 — Continuous Evolution Functional Integrations

- Criação de `PAS-001-EC-INTEGRATION-001 — Integrações Funcionais da Evolução Contínua`, versão `1.0.0`.
- Registro do documento como quinta extensão normativa da Capacidade 09 do `PAS-001 — Guivos Journey`.
- Elevação do progresso editorial da Capacidade 09 de 80% para 90%, mantendo o estado `In progress`.
- Consolidação do contrato comum de integração com produtores, consumidores, participante, trajetória, segmento, finalidade, modo, autoridade, dimensão, baseline, direção, escopo, sensibilidade, proveniência, confiança, incerteza, temporalidades, permissões, retenção, sincronização e revogação.
- Consolidação de identidade, associação, titularidade, autoridade, finalidade, minimização, proveniência, temporalidades, qualidade, confiança e incerteza.
- Definição de transformações permitidas e proibição de fabricar evolução, progresso, regressão, baseline, direção, intenção, significado, mérito, fé, diagnóstico ou causalidade.
- Consolidação de consentimento granular, pausa, desconexão, revogação propagada e retenção residual justificada.
- Consolidação de sincronização, divergência, ordenação, concorrência, reconciliação, prevenção de ciclos, correção, retroatividade e falha segura.
- Integração governada com todas as capacidades do Journey, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, dispositivos, canais e sistemas externos.
- Proteção reforçada de saúde, espiritualidade, trabalho, educação, finanças, voluntariado, fontes públicas, dispositivos compartilhados e terceiros.
- Definição de observabilidade, explicabilidade, auditoria, reconstrução, 36 comportamentos proibidos e 58 critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.20.0`.
- Atualização do Roadmap e do Knowledge Board para `11.1.0`.
- Atualização da Matriz de Consolidação Canônica para `1.20.0`.
- Atualização do README, da página inicial e da navegação do MkDocs.
- Definição de KPIs, guardrails, baseline, cenários e contrato final da Capacidade 09 como próximo ponto exato.

"""
text = replace_once(text, "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n", "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n" + entry, f"{path} entrada")
write(path, text)

# Validações finais
checks = {
    "docs/product-architecture/index.md": ["version: 1.20.0", "PAS-001-EC-INTEGRATION-001 1.0.0", "referência de `90%`", "KPIs, guardrails"],
    "docs/roadmap.md": ["version: 11.1.0", "`In progress`, 90%", "PAS-001-EC-INTEGRATION-001 1.0.0", "KPIs, Guardrails, Cenários e Contrato Final"],
    "docs/project/knowledge-board.md": ["version: 11.1.0", "PAS-001-EC-INTEGRATION-001", "In progress — 90%", "Contrato de integração de evolução"],
    "docs/project/canonical-consolidation-matrix.md": ["version: 1.20.0", "Capacidade 09 ativa em 90%", "Integrações Funcionais da Evolução Contínua", "Contrato de integração de evolução"],
    "README.md": ["In progress — 90%", "PAS-001-EC-INTEGRATION-001 1.0.0", "Integrações Funcionais da Evolução Contínua", "Contrato Final da Capacidade 09"],
    "docs/index.md": ["`In progress`, 90%", "PAS-001-EC-INTEGRATION-001 1.0.0", "Integrações Funcionais da Evolução Contínua", "Contrato Final da Capacidade 09"],
    "mkdocs.yml": ["PAS-001-EC-INTEGRATION-001 — Integrações Funcionais da Evolução Contínua"],
    "CHANGELOG.md": ["## 0.48.0 — Continuous Evolution Functional Integrations", "Arquitetura de Produtos para `1.20.0`", "Roadmap e do Knowledge Board para `11.1.0`"],
}
for file_path, tokens in checks.items():
    content = read(file_path)
    for token in tokens:
        if token not in content:
            raise RuntimeError(f"{file_path}: validação ausente: {token}")

for file_path in checks:
    content = read(file_path)
    if "Capacidade 09" in content and "In progress — 80%" in content:
        raise RuntimeError(f"{file_path}: estado antigo remanescente")

print("Sincronização da quinta extensão normativa concluída com sucesso.")
