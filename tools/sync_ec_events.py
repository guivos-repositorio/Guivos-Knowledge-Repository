from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    content = read(path)
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one anchor, found {count}: {old[:100]!r}")
    write(path, content.replace(old, new, 1))


def insert_after(path: str, anchor: str, addition: str) -> None:
    replace_once(path, anchor, anchor + addition)


# Arquitetura de Produtos
pa = "docs/product-architecture/index.md"
replace_once(pa, "version: 1.18.0", "version: 1.19.0")
replace_once(
    pa,
    "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `60%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0`.",
    "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `80%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0`.",
)
insert_after(
    pa,
    "- 34 comportamentos proibidos e 72 critérios de aceite.\n",
    "\n`PAS-001-EC-EVENT-001 1.0.0` consolida:\n\n"
    "- distinção entre sinal, comando, proposta, declaração, observação, interpretação, evento e efeito;\n"
    "- `Trajetória de Evolução` como agregado funcional permanente, com segmentos e janelas de observação;\n"
    "- estrutura comum versionada com participante, ator, autoridade, finalidade, baseline, direção, temporalidades, proveniência, sensibilidade, confiança, incerteza, permissões e retenção;\n"
    "- 19 famílias de eventos cobrindo identificação, baseline, direção, observações, evidências, interpretações, reconhecimento, padrões, causalidade, controles, privacidade, contestação, correção, revogação, sincronização e reconstrução;\n"
    "- persistência anterior à publicação e consumo limitado à semântica do evento;\n"
    "- correção compensatória, revogação propagada, idempotência, ordenação, concorrência, atomicidade, compatibilidade, explicabilidade, auditoria e falha segura;\n"
    "- 34 comportamentos proibidos e 64 critérios de aceite.\n",
)
replace_once(pa, "A Capacidade 09 está `In progress`, com progresso editorial de referência de `60%`.", "A Capacidade 09 está `In progress`, com progresso editorial de referência de `80%`.")
replace_once(pa, "O próximo bloco normativo são os eventos funcionais da Evolução Contínua.", "O próximo bloco normativo são as integrações funcionais da Evolução Contínua.")

# Roadmap
roadmap = "docs/roadmap.md"
replace_once(roadmap, "version: 10.9.0", "version: 11.0.0")
replace_once(roadmap, "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 60%.", "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 80%.")
replace_once(
    roadmap,
    "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0`.",
    "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0`.",
)
replace_once(roadmap, "O próximo trabalho deverá consolidar os eventos funcionais da `Capacidade 09 — Evolução Contínua`.", "O próximo trabalho deverá consolidar as integrações funcionais da `Capacidade 09 — Evolução Contínua`.")
insert_after(
    roadmap,
    "- 34 comportamentos proibidos e 72 critérios de aceite.\n",
    "\n`PAS-001-EC-EVENT-001 1.0.0` consolidou:\n\n"
    "- `Trajetória de Evolução` como agregado funcional e estrutura comum versionada;\n"
    "- identidade, titularidade, ator, autoridade, finalidade, dimensão, baseline, direção, temporalidades, proveniência, sensibilidade, confiança e incerteza;\n"
    "- 19 famílias de eventos de identificação, observação, evidência, interpretação, reconhecimento, padrões, causalidade, controles, privacidade, validações externas, contestação, correção, revogação e reconstrução;\n"
    "- persistência anterior à publicação, minimização e consumo limitado à semântica reconhecida;\n"
    "- correção compensatória, revogação propagada, idempotência, ordenação, concorrência, atomicidade, compatibilidade, explicabilidade, auditoria e falha segura;\n"
    "- 34 comportamentos proibidos e 64 critérios de aceite.\n",
)
replace_once(roadmap, "A Capacidade 09 está `In progress`, com progresso editorial de referência de `60%`.", "A Capacidade 09 está `In progress`, com progresso editorial de referência de `80%`.")
replace_once(roadmap, "| 09 — Evolução Contínua | In progress | 60% |", "| 09 — Evolução Contínua | In progress | 80% |")
replace_once(
    roadmap,
    "## Ponto exato de retomada\n\nRetomar nos **Eventos Funcionais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. distinção entre sinais, comandos, propostas, declarações e eventos reconhecidos;\n2. agregado `Trajetória de Evolução` e estrutura comum versionada;\n3. autoridade, finalidade, temporalidades, proveniência, sensibilidade e permissões;\n4. famílias de eventos, correção compensatória, revogação e propagação;\n5. idempotência, ordenação, concorrência, reconstrução, auditoria e falha segura.",
    "## Ponto exato de retomada\n\nRetomar nas **Integrações Funcionais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. contrato comum de integração, identidade, associação, finalidade e autoridade;\n2. minimização, proveniência, temporalidades, qualidade, confiança e incerteza;\n3. sincronização, prevenção de ciclos, ordenação, concorrência e reconciliação;\n4. correção, pausa, desconexão, revogação, propagação e retenção residual;\n5. integrações internas, externas, profissionais, organizacionais, dispositivos, canais, observabilidade e falha segura.",
)

# Knowledge Board
board = "docs/project/knowledge-board.md"
replace_once(board, "version: 10.9.0", "version: 11.0.0")
insert_after(board, "| PAS-001-EC-VIEW-001 | Active 1.0.0 | Definir a visualização e o controle da Evolução Contínua |\n", "| PAS-001-EC-EVENT-001 | Active 1.0.0 | Definir os contratos dos eventos funcionais da Evolução Contínua |\n")
replace_once(board, "| Estado da capacidade ativa | `In progress — 60%` |", "| Estado da capacidade ativa | `In progress — 80%` |")
replace_once(
    board,
    "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0` |",
    "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0` |",
)
replace_once(board, "| Progresso editorial de Evolução Contínua | `60%` |", "| Progresso editorial de Evolução Contínua | `80%` |")
replace_once(board, "| Foco imediato | Consolidar os eventos funcionais da Capacidade 09 — Evolução Contínua |", "| Foco imediato | Consolidar as integrações funcionais da Capacidade 09 — Evolução Contínua |")
replace_once(board, "| 09 — Evolução Contínua | In progress — 60% | Três extensões normativas consolidadas; eventos funcionais como próximo bloco |", "| 09 — Evolução Contínua | In progress — 80% | Quatro extensões normativas consolidadas; integrações funcionais como próximo bloco |")
insert_after(
    board,
    "- 34 comportamentos proibidos e 72 critérios de aceite.\n",
    "\n### Eventos funcionais\n\n"
    "- `Trajetória de Evolução` como agregado funcional permanente e estrutura comum versionada;\n"
    "- distinção entre sinal, comando, proposta, declaração, observação, interpretação, evento e efeito;\n"
    "- autoridade, finalidade, dimensão, baseline, direção, temporalidades, proveniência, sensibilidade, confiança, incerteza, permissões e retenção;\n"
    "- 19 famílias de eventos de identificação, observações, evidências, interpretações, reconhecimento, padrões, causalidade, controles, privacidade, validações externas, contestação, correção, revogação, sincronização e reconstrução;\n"
    "- persistência anterior à publicação, minimização, compatibilidade e consumo limitado à semântica;\n"
    "- correção compensatória, revogação propagada, idempotência, ordenação, concorrência, atomicidade, explicabilidade, auditoria e falha segura;\n"
    "- 34 comportamentos proibidos e 64 critérios de aceite.\n",
)
replace_once(board, "A Capacidade 09 está `In progress`, com progresso editorial de referência de `60%`.", "A Capacidade 09 está `In progress`, com progresso editorial de referência de `80%`.")
replace_once(board, "| Evolução Contínua | In progress — 60% |", "| Evolução Contínua | In progress — 80% |")
insert_after(board, "| Visualização e Controle de Evolução Contínua | Normative 1.0.0 |\n", "| Eventos Funcionais de Evolução Contínua | Normative 1.0.0 |\n| Evento funcional de evolução | Fato reconhecido, persistido, versionado e publicado dentro de autoridade, finalidade, dimensão e incerteza explícitas |\n| Contrato de evento de evolução | Estrutura comum com trajetória, segmento, participante, ator, autoridade, baseline, direção, temporalidades, proveniência, confiança, permissões e retenção |\n")
replace_once(board, "| Roadmap | 10.9.0 |", "| Roadmap | 11.0.0 |")
replace_once(board, "| Knowledge Board | 10.9.0 |", "| Knowledge Board | 11.0.0 |")
insert_after(board, "| PAS-001-EC-VIEW-001 | Active 1.0.0 |\n", "| PAS-001-EC-EVENT-001 | Active 1.0.0 |\n")
replace_once(
    board,
    "## Próxima atividade\n\nConsolidar os **Eventos Funcionais da Capacidade 09 — Evolução Contínua**, incluindo sinais, comandos, propostas, declarações, eventos reconhecidos, agregado `Trajetória de Evolução`, estrutura comum, autoridade, temporalidades, famílias de eventos, correção compensatória, revogação, propagação, idempotência, ordenação, concorrência, reconstrução e falha segura.",
    "## Próxima atividade\n\nConsolidar as **Integrações Funcionais da Capacidade 09 — Evolução Contínua**, incluindo contrato comum, identidade, associação, finalidade, autoridade, minimização, proveniência, temporalidades, qualidade, confiança, incerteza, sincronização, prevenção de ciclos, correção, pausa, desconexão, revogação, propagação, observabilidade, neutralidade comercial e falha segura.",
)

# Matriz Canônica
matrix = "docs/project/canonical-consolidation-matrix.md"
replace_once(matrix, "version: 1.18.0", "version: 1.19.0")
replace_once(matrix, "| Evolução Contínua | Refinar | Capacidade 09 ativa em 60%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |", "| Evolução Contínua | Refinar | Capacidade 09 ativa em 80%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |")
insert_after(matrix, "| Visualização e Controle da Evolução Contínua | Manter | PAS-001-EC-VIEW-001 1.0.0 define `Minha Evolução`, trajetórias por dimensão e período, baseline, direção, estados, padrões, evidências, confiança, incerteza, interpretações alternativas, controles, privacidade, acessibilidade e falha segura |\n", "| Eventos Funcionais da Evolução Contínua | Manter | PAS-001-EC-EVENT-001 1.0.0 define Trajetória de Evolução, estrutura comum, 19 famílias, autoridade, finalidade, baseline, direção, temporalidades, proveniência, confiança, incerteza, correção, revogação, idempotência, ordenação, concorrência, reconstrução e auditoria |\n")
insert_after(matrix, "| Trajetória de Evolução | Manter | Unidade funcional com participante, dimensão, direção, baseline, período, estados, mudanças, evidências, interpretações, confiança, incertezas, fatores contribuintes, correções, permissões e histórico |\n", "| Evento funcional de evolução | Manter | Fato reconhecido, persistido, versionado e publicado dentro de autoridade, finalidade, dimensão e incerteza explícitas |\n| Contrato de evento de evolução | Manter | Estrutura comum com trajetória, segmento, participante, ator, autoridade, baseline, direção, temporalidades, proveniência, confiança, permissões e retenção |\n")
replace_once(
    matrix,
    "As Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0` mantêm a Capacidade 09 como `In progress — 60%` e consolidam finalidade, Trajetória de Evolução, direção, baseline, estados, transições, visualização, evidências, confiança, incerteza, interpretações alternativas, controles, privacidade, acessibilidade, contestação, correção, revogação, reconstrução e falha segura, sem promover candidatos arquiteturais à Canon.",
    "As Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0` mantêm a Capacidade 09 como `In progress — 80%` e consolidam finalidade, Trajetória de Evolução, direção, baseline, estados, transições, visualização, estrutura comum, 19 famílias de eventos, evidências, interpretações, confiança, incerteza, causalidade, controles, privacidade, contestação, correção, revogação, idempotência, ordenação, concorrência, reconstrução e falha segura, sem promover candidatos arquiteturais à Canon.",
)
replace_once(
    matrix,
    "Consolidar os **eventos funcionais da Capacidade 09 — Evolução Contínua**, incluindo sinais, comandos, propostas, declarações, eventos reconhecidos, agregado, estrutura comum, autoridade, temporalidades, correção compensatória, revogação, propagação, idempotência, ordenação, concorrência, reconstrução e falha segura.",
    "Consolidar as **integrações funcionais da Capacidade 09 — Evolução Contínua**, incluindo contrato comum, identidade, associação, autoridade, finalidade, minimização, proveniência, temporalidades, sincronização, prevenção de ciclos, correção, revogação, propagação, observabilidade, neutralidade comercial e falha segura.",
)

# README
readme = "README.md"
replace_once(readme, "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 60%`", "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 80%`")
replace_once(readme, "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0, PAS-001-EC-LIFECYCLE-001 1.0.0 e PAS-001-EC-VIEW-001 1.0.0", "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0, PAS-001-EC-LIFECYCLE-001 1.0.0, PAS-001-EC-VIEW-001 1.0.0 e PAS-001-EC-EVENT-001 1.0.0")
insert_after(readme, "`PAS-001-EC-VIEW-001 1.0.0` consolida `Minha Evolução`, trajetórias por dimensão, período e segmento, baseline, direção, estados, padrões, evidências, confiança, incerteza, interpretações alternativas, controles, privacidade, acessibilidade, contestação, correção, revogação, compartilhamento, exportação e falha segura.\n", "\n`PAS-001-EC-EVENT-001 1.0.0` consolida a `Trajetória de Evolução` como agregado funcional, estrutura comum versionada, 19 famílias de eventos, autoridade, finalidade, dimensão, baseline, direção, temporalidades, proveniência, sensibilidade, confiança, incerteza, correção compensatória, revogação, idempotência, ordenação, concorrência, reconstrução, explicabilidade, auditoria e falha segura.\n")
replace_once(readme, "A Capacidade 09 está **In progress**, com progresso editorial de referência de **60%**.", "A Capacidade 09 está **In progress**, com progresso editorial de referência de **80%**.")
replace_once(
    readme,
    "## Ponto exato de retomada\n\nRetomar nos **Eventos Funcionais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- sinais, comandos, propostas, declarações e eventos reconhecidos;\n- agregado `Trajetória de Evolução` e estrutura comum versionada;\n- autoridade, finalidade, temporalidades, proveniência e sensibilidade;\n- famílias de eventos, correção compensatória, revogação e propagação;\n- idempotência, ordenação, concorrência, reconstrução, auditoria e falha segura.",
    "## Ponto exato de retomada\n\nRetomar nas **Integrações Funcionais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- contrato comum, identidade, associação, finalidade e autoridade;\n- minimização, proveniência, temporalidades, qualidade, confiança e incerteza;\n- sincronização, prevenção de ciclos, ordenação, concorrência e reconciliação;\n- correção, pausa, desconexão, revogação, propagação e retenção residual;\n- integrações internas, externas, profissionais, organizacionais, dispositivos, canais, observabilidade e falha segura.",
)
replace_once(readme, "a Capacidade 09 — Evolução Contínua está `In progress — 60%`.", "a Capacidade 09 — Evolução Contínua está `In progress — 80%`.")
replace_once(readme, "| 09 — Evolução Contínua | In progress — 60% |", "| 09 — Evolução Contínua | In progress — 80% |")
insert_after(readme, "- [Visualização e Controle da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-visualizacao-controle.md)\n", "- [Eventos Funcionais da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-eventos-funcionais.md)\n")

# Página inicial documental
index = "docs/index.md"
replace_once(index, "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 60%;", "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 80%;")
replace_once(index, "- `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0` como extensões normativas vigentes da Capacidade 09;", "- `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0`, `PAS-001-EC-VIEW-001 1.0.0` e `PAS-001-EC-EVENT-001 1.0.0` como extensões normativas vigentes da Capacidade 09;")
replace_once(index, "Consolidar os **Eventos Funcionais da Capacidade 09 — Evolução Contínua**.", "Consolidar as **Integrações Funcionais da Capacidade 09 — Evolução Contínua**.")
replace_once(index, "As três extensões de Evolução Contínua mantêm a Capacidade 09 ativa com fundamentos, ciclo de vida, `Minha Evolução`, direção, baseline, temporalidades, evidências, causalidade, não linearidade, 17 dimensões independentes, estados, transições, visualização, interpretações alternativas, controles, privacidade, acessibilidade, contestação, correção, revogação, reconstrução e falha segura.", "As quatro extensões de Evolução Contínua mantêm a Capacidade 09 ativa com fundamentos, ciclo de vida, `Minha Evolução`, `Trajetória de Evolução` como agregado, estrutura comum, 19 famílias de eventos, direção, baseline, temporalidades, evidências, causalidade, não linearidade, estados, transições, interpretações alternativas, controles, privacidade, contestação, correção, revogação, idempotência, ordenação, concorrência, reconstrução e falha segura.")
insert_after(index, "- [Visualização e Controle da Evolução Contínua](product-architecture/pas-001-evolucao-continua-visualizacao-controle.md)\n", "- [Eventos Funcionais da Evolução Contínua](product-architecture/pas-001-evolucao-continua-eventos-funcionais.md)\n")
replace_once(index, "| 09 — Evolução Contínua | In progress — 60% |", "| 09 — Evolução Contínua | In progress — 80% |")
replace_once(index, "Retomar nos **Eventos Funcionais da Capacidade 09 — Evolução Contínua**.", "Retomar nas **Integrações Funcionais da Capacidade 09 — Evolução Contínua**.")

# Navegação
mkdocs = "mkdocs.yml"
insert_after(mkdocs, "      - PAS-001-EC-VIEW-001 — Visualização e Controle da Evolução Contínua: product-architecture/pas-001-evolucao-continua-visualizacao-controle.md\n", "      - PAS-001-EC-EVENT-001 — Eventos Funcionais da Evolução Contínua: product-architecture/pas-001-evolucao-continua-eventos-funcionais.md\n")

# Changelog
changelog = "CHANGELOG.md"
insert_after(
    changelog,
    "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n",
    "\n## 0.47.0 — Continuous Evolution Functional Events\n\n"
    "- Criação de `PAS-001-EC-EVENT-001 — Contratos dos Eventos Funcionais da Evolução Contínua`, versão `1.0.0`.\n"
    "- Registro do documento como quarta extensão normativa da Capacidade 09 do `PAS-001 — Guivos Journey`.\n"
    "- Elevação do progresso editorial da Capacidade 09 de 60% para 80%, mantendo o estado `In progress`.\n"
    "- Consolidação da `Trajetória de Evolução` como agregado funcional permanente, com segmentos e janelas de observação.\n"
    "- Definição de estrutura comum versionada com autoridade, finalidade, dimensão, baseline, direção, temporalidades, proveniência, sensibilidade, confiança, incerteza, permissões e retenção.\n"
    "- Definição de 19 famílias de eventos funcionais.\n"
    "- Persistência funcional anterior à publicação e consumo limitado à semântica reconhecida.\n"
    "- Consolidação de observações, evidências, interpretações, reconhecimento, manutenção, progressão, oscilação, regressão, recuperação, reorientação e causalidade limitada.\n"
    "- Consolidação de controles do participante, privacidade, compartilhamento, validações externas e proteção de terceiros.\n"
    "- Definição de correção compensatória, revogação propagada, idempotência, ordenação, concorrência, atomicidade, compatibilidade, reconstrução, explicabilidade, auditoria e falha segura.\n"
    "- Registro de 34 comportamentos proibidos e 64 critérios de aceite.\n"
    "- Atualização da Arquitetura de Produtos para `1.19.0`.\n"
    "- Atualização do Roadmap e do Knowledge Board para `11.0.0`.\n"
    "- Atualização da Matriz de Consolidação Canônica para `1.19.0`.\n"
    "- Atualização do README, da página inicial e da navegação do MkDocs.\n"
    "- Definição de Integrações Funcionais da Capacidade 09 como próximo ponto exato.\n",
)

# Validações normativas e de sincronização
event_doc = read("docs/product-architecture/pas-001-evolucao-continua-eventos-funcionais.md")
headings = [int(x) for x in re.findall(r"^# (\d{4})\.", event_doc, flags=re.MULTILINE)]
expected = list(range(4185, 4284))
if headings != expected:
    raise RuntimeError(f"sequência de seções inválida: {headings[:3]} ... {headings[-3:]}")

prohibited = event_doc.split("# 4281. Comportamentos proibidos", 1)[1].split("# 4282. Critérios de aceite", 1)[0]
criteria = event_doc.split("# 4282. Critérios de aceite", 1)[1].split("# 4283. Consolidação e próximo ponto", 1)[0]
if len(re.findall(r"^\d+\. ", prohibited, flags=re.MULTILINE)) != 34:
    raise RuntimeError("quantidade inválida de comportamentos proibidos")
if len(re.findall(r"^\d+\. ", criteria, flags=re.MULTILINE)) != 64:
    raise RuntimeError("quantidade inválida de critérios de aceite")

checks = {
    pa: ["version: 1.19.0", "PAS-001-EC-EVENT-001 1.0.0", "progresso editorial de referência de `80%`", "integrações funcionais da Evolução Contínua"],
    roadmap: ["version: 11.0.0", "`In progress`, 80%", "PAS-001-EC-EVENT-001 1.0.0", "Integrações Funcionais da Capacidade 09"],
    board: ["version: 11.0.0", "PAS-001-EC-EVENT-001", "In progress — 80%", "Integrações Funcionais da Capacidade 09"],
    matrix: ["version: 1.19.0", "Eventos Funcionais da Evolução Contínua", "In progress — 80%", "integrações funcionais da Capacidade 09"],
    readme: ["In progress — 80%", "PAS-001-EC-EVENT-001 1.0.0", "Integrações Funcionais da Capacidade 09"],
    index: ["`In progress`, 80%", "PAS-001-EC-EVENT-001 1.0.0", "Integrações Funcionais da Capacidade 09"],
    mkdocs: ["PAS-001-EC-EVENT-001 — Eventos Funcionais da Evolução Contínua"],
    changelog: ["## 0.47.0 — Continuous Evolution Functional Events"],
}
for path, markers in checks.items():
    content = read(path)
    for marker in markers:
        if marker not in content:
            raise RuntimeError(f"{path}: marcador ausente: {marker}")

print("Sincronização dos eventos funcionais validada.")
