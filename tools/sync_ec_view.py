#!/usr/bin/env python3
"""Sincroniza PAS-001-EC-VIEW-001 com os artefatos canônicos do GKR."""

from __future__ import annotations

import argparse
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
        raise RuntimeError(f"{path}: âncora esperada uma vez, encontrada {count}: {old[:100]!r}")
    write(path, content.replace(old, new, 1))


def insert_after(path: str, anchor: str, insertion: str) -> None:
    replace_once(path, anchor, anchor + insertion)


PRODUCT_VIEW_SUMMARY = """`PAS-001-EC-VIEW-001 1.0.0` consolida:

- `Minha Evolução` como superfície principal de compreensão, acompanhamento, revisão e controle;
- trajetórias por dimensão, período e segmento, sem nota global ou ranking humano;
- visão geral, áreas funcionais, lista, cartões, linha do tempo, períodos comparados, matriz de dimensões e gráficos limitados;
- baseline, direção, estados, padrões, evidências, confiança, incerteza, observações, interpretações e causalidade representados separadamente;
- interpretações do participante, profissionais, institucionais e automatizadas com autoria, autoridade e alternativas preservadas;
- estabilidade, manutenção, progressão, oscilação, regressão, recuperação, reorientação e inconclusão com linguagem não julgadora;
- proteção de espiritualidade, saúde, trabalho, educação, finanças, voluntariado, trajetórias coletivas e terceiros;
- controles de associação, pausa, encerramento, contestação, correção, revogação, compartilhamento e exportação;
- acessibilidade técnica e cognitiva, privacidade visual, consistência entre canais e falha segura;
- 34 comportamentos proibidos e 72 critérios de aceite.

"""

ROADMAP_VIEW_SUMMARY = """`PAS-001-EC-VIEW-001 1.0.0` consolidou:

- `Minha Evolução` como superfície de compreensão, acompanhamento, revisão e controle;
- trajetórias por dimensão, período e segmento, preservando não linearidade e ausência legítima de mudança;
- visão geral, áreas funcionais, lista, cartões, linha do tempo, períodos comparados, matriz de dimensões e gráficos governados;
- baseline, direção, estados, padrões, evidências, confiança, incerteza, observações, interpretações e causalidade separados;
- estabilidade, progressão, oscilação, regressão, recuperação, reorientação e inconclusão sem julgamento moral;
- proteção de trajetórias sensíveis, espiritualidade, saúde, trabalho, educação, finanças, voluntariado e terceiros;
- controles de associação, pausa, encerramento, contestação, correção, revogação, compartilhamento e exportação;
- acessibilidade, privacidade visual, consistência entre canais e falha segura;
- 34 comportamentos proibidos e 72 critérios de aceite.

"""

BOARD_VIEW_SUMMARY = """### Visualização e controle

- `Minha Evolução` como superfície principal de compreensão, acompanhamento, revisão e controle;
- trajetórias organizadas por dimensão, período e segmento, sem nota global ou comparação humana;
- visão geral, áreas funcionais, lista, cartões, linha do tempo, períodos comparados, matriz de dimensões e gráficos limitados;
- baseline, direção, estados, padrões, evidências, confiança, incerteza, observações, interpretações e causalidade separados;
- interpretações alternativas e autoria do participante preservadas;
- estabilidade, progressão, oscilação, regressão, recuperação, reorientação e inconclusão com linguagem não julgadora;
- proteção de trajetórias sensíveis, espiritualidade, saúde, trabalho, educação, finanças, voluntariado e terceiros;
- controles de associação, pausa, encerramento, contestação, correção, revogação, compartilhamento e exportação;
- acessibilidade, privacidade visual, consistência entre canais e falha segura;
- 34 comportamentos proibidos e 72 critérios de aceite.

"""

CHANGELOG_ENTRY = """## 0.46.0 — Continuous Evolution View and Control

- Criação de `PAS-001-EC-VIEW-001 — Visualização e Controle da Evolução Contínua`, versão `1.0.0`.
- Registro do documento como terceira extensão normativa da Capacidade 09 do `PAS-001 — Guivos Journey`.
- Elevação do progresso editorial da Capacidade 09 de 40% para 60%, mantendo o estado `In progress`.
- Consolidação de `Minha Evolução` como superfície principal de compreensão, acompanhamento, revisão e controle.
- Definição de visão geral, áreas funcionais, lista, cartões, linha do tempo, períodos comparados, matriz de dimensões, gráficos, escalas e cores governadas.
- Representação independente de baseline, direção, estado funcional, padrão, evidências, confiança, incerteza, observações, interpretações e causalidade.
- Preservação de interpretações alternativas e da autoria do participante.
- Representação não julgadora de estabilidade, manutenção, progressão, oscilação, regressão, recuperação, reorientação e inconclusão.
- Proteção de trajetórias sensíveis, espiritualidade, religião, saúde, trabalho, educação, finanças, voluntariado, coletivos e terceiros.
- Consolidação de controles de associação, pausa, encerramento, contestação, correção, revogação, compartilhamento e exportação.
- Definição de acessibilidade técnica e cognitiva, privacidade visual, consistência entre canais e falha segura.
- Registro de 34 comportamentos proibidos e 72 critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.18.0`.
- Atualização do Roadmap e do Knowledge Board para `10.9.0`.
- Atualização da Matriz de Consolidação Canônica para `1.18.0`.
- Atualização do README, da página inicial e da navegação do MkDocs.
- Definição de Eventos Funcionais da Capacidade 09 como próximo ponto exato.

"""


def apply() -> None:
    # Arquitetura de Produtos
    replace_once("docs/product-architecture/index.md", "version: 1.17.0", "version: 1.18.0")
    replace_once(
        "docs/product-architecture/index.md",
        "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `40%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0`.",
        "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `60%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0`.",
    )
    replace_once(
        "docs/product-architecture/index.md",
        "- 32 comportamentos proibidos e 64 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `40%`.\n\nO próximo bloco normativo é a visualização e o controle da Evolução Contínua.",
        "- 32 comportamentos proibidos e 64 critérios de aceite.\n\n" + PRODUCT_VIEW_SUMMARY + "A Capacidade 09 está `In progress`, com progresso editorial de referência de `60%`.\n\nO próximo bloco normativo são os eventos funcionais da Evolução Contínua.",
    )

    # Roadmap
    replace_once("docs/roadmap.md", "version: 10.8.0", "version: 10.9.0")
    replace_once(
        "docs/roadmap.md",
        "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 40%.",
        "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 60%.",
    )
    replace_once(
        "docs/roadmap.md",
        "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0`.",
        "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0`.",
    )
    replace_once(
        "docs/roadmap.md",
        "O próximo trabalho deverá consolidar a visualização e o controle da `Capacidade 09 — Evolução Contínua`.",
        "O próximo trabalho deverá consolidar os eventos funcionais da `Capacidade 09 — Evolução Contínua`.",
    )
    replace_once(
        "docs/roadmap.md",
        "- 32 comportamentos proibidos e 64 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `40%`.",
        "- 32 comportamentos proibidos e 64 critérios de aceite.\n\n" + ROADMAP_VIEW_SUMMARY + "A Capacidade 09 está `In progress`, com progresso editorial de referência de `60%`.",
    )
    replace_once(
        "docs/roadmap.md",
        "| 09 — Evolução Contínua | In progress | 40% |",
        "| 09 — Evolução Contínua | In progress | 60% |",
    )
    replace_once(
        "docs/roadmap.md",
        "Retomar na **Visualização e Controle da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. superfície `Minha Evolução`;\n2. trajetórias por dimensão e período;\n3. baseline, direção, evidências, confiança e incerteza;\n4. interpretações alternativas e ausência legítima de mudança;\n5. controles, privacidade, acessibilidade, contestação, correção, revogação e falha segura.",
        "Retomar nos **Eventos Funcionais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. distinção entre sinais, comandos, propostas, declarações e eventos reconhecidos;\n2. agregado `Trajetória de Evolução` e estrutura comum versionada;\n3. autoridade, finalidade, temporalidades, proveniência, sensibilidade e permissões;\n4. famílias de eventos, correção compensatória, revogação e propagação;\n5. idempotência, ordenação, concorrência, reconstrução, auditoria e falha segura.",
    )

    # Knowledge Board
    replace_once("docs/project/knowledge-board.md", "version: 10.8.0", "version: 10.9.0")
    insert_after(
        "docs/project/knowledge-board.md",
        "| PAS-001-EC-LIFECYCLE-001 | Active 1.0.0 | Definir o ciclo de vida da Evolução Contínua |\n",
        "| PAS-001-EC-VIEW-001 | Active 1.0.0 | Definir a visualização e o controle da Evolução Contínua |\n",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| Estado da capacidade ativa | `In progress — 40%` |",
        "| Estado da capacidade ativa | `In progress — 60%` |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0` |",
        "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0` |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| Progresso editorial de Evolução Contínua | `40%` |",
        "| Progresso editorial de Evolução Contínua | `60%` |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| Foco imediato | Consolidar a visualização e o controle da Capacidade 09 — Evolução Contínua |",
        "| Foco imediato | Consolidar os eventos funcionais da Capacidade 09 — Evolução Contínua |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| 09 — Evolução Contínua | In progress — 40% | Duas extensões normativas consolidadas; visualização e controle como próximo bloco |",
        "| 09 — Evolução Contínua | In progress — 60% | Três extensões normativas consolidadas; eventos funcionais como próximo bloco |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "- 32 comportamentos proibidos e 64 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `40%`.",
        "- 32 comportamentos proibidos e 64 critérios de aceite.\n\n" + BOARD_VIEW_SUMMARY + "A Capacidade 09 está `In progress`, com progresso editorial de referência de `60%`.",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| Evolução Contínua | In progress — 40% |",
        "| Evolução Contínua | In progress — 60% |",
    )
    insert_after(
        "docs/project/knowledge-board.md",
        "| Ciclo de Vida de Evolução Contínua | Normative 1.0.0 |\n",
        "| Visualização e Controle de Evolução Contínua | Normative 1.0.0 |\n| Minha Evolução | Superfície principal de compreensão, acompanhamento, revisão e controle das Trajetórias de Evolução |\n| Privacidade visual de evolução | Títulos neutros, prévias protegidas, autenticação proporcional e minimização de trajetórias sensíveis |\n| Matriz de dimensões de evolução | Visão comparativa sem média global entre dimensões incompatíveis |\n| Interpretação alternativa de evolução | Leitura concorrente, atribuída, explicável e contestável, preservada sem substituição silenciosa |\n",
    )
    replace_once("docs/project/knowledge-board.md", "| Roadmap | 10.8.0 |", "| Roadmap | 10.9.0 |")
    replace_once("docs/project/knowledge-board.md", "| Knowledge Board | 10.8.0 |", "| Knowledge Board | 10.9.0 |")
    insert_after(
        "docs/project/knowledge-board.md",
        "| PAS-001-EC-LIFECYCLE-001 | Active 1.0.0 |\n",
        "| PAS-001-EC-VIEW-001 | Active 1.0.0 |\n",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "Consolidar a **Visualização e Controle da Capacidade 09 — Evolução Contínua**, incluindo `Minha Evolução`, trajetórias por dimensão e período, baseline, direção, evidências, confiança, incerteza, interpretações alternativas, ausência legítima de mudança, controles, privacidade, acessibilidade, contestação, correção, revogação e falha segura.",
        "Consolidar os **Eventos Funcionais da Capacidade 09 — Evolução Contínua**, incluindo sinais, comandos, propostas, declarações, eventos reconhecidos, agregado `Trajetória de Evolução`, estrutura comum, autoridade, temporalidades, famílias de eventos, correção compensatória, revogação, propagação, idempotência, ordenação, concorrência, reconstrução e falha segura.",
    )

    # Matriz Canônica
    replace_once("docs/project/canonical-consolidation-matrix.md", "version: 1.17.0", "version: 1.18.0")
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "| Evolução Contínua | Refinar | Capacidade 09 ativa em 40%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |",
        "| Evolução Contínua | Refinar | Capacidade 09 ativa em 60%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |",
    )
    insert_after(
        "docs/project/canonical-consolidation-matrix.md",
        "| Ciclo de Vida da Evolução Contínua | Manter | PAS-001-EC-LIFECYCLE-001 1.0.0 define 17 dimensões independentes, estados, transições, identificação, candidatura, baseline, direção, observação, interpretação, reconhecimento, acompanhamento, não linearidade, contestação, correção, revogação, propagação, reconstrução e falha segura |\n",
        "| Visualização e Controle da Evolução Contínua | Manter | PAS-001-EC-VIEW-001 1.0.0 define `Minha Evolução`, trajetórias por dimensão e período, baseline, direção, estados, padrões, evidências, confiança, incerteza, interpretações alternativas, controles, privacidade, acessibilidade e falha segura |\n| Minha Evolução | Manter | Superfície de compreensão, acompanhamento, revisão e controle, sem nota global, ranking, perfil determinístico ou expectativa de melhoria contínua |\n| Privacidade visual de evolução | Manter | Títulos neutros, prévias protegidas, autenticação proporcional e minimização de trajetórias sensíveis |\n| Matriz de dimensões de evolução | Manter | Representa dimensões independentes sem média global ou comparação de valor humano |\n| Interpretação alternativa de evolução | Manter | Preserva leituras concorrentes, autoria, autoridade, evidências, confiança e contestação |\n",
    )
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "As Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0` mantêm a Capacidade 09 como `In progress — 40%` e consolidam finalidade, definição canônica, Trajetória de Evolução, direção, baseline, temporalidades, evidências, causalidade, não linearidade, estados, transições, acompanhamento, contestação, correção, revogação, reconstrução e falha segura, sem promover candidatos arquiteturais à Canon.",
        "As Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0` mantêm a Capacidade 09 como `In progress — 60%` e consolidam finalidade, Trajetória de Evolução, direção, baseline, estados, transições, visualização, evidências, confiança, incerteza, interpretações alternativas, controles, privacidade, acessibilidade, contestação, correção, revogação, reconstrução e falha segura, sem promover candidatos arquiteturais à Canon.",
    )
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "Consolidar a **visualização e o controle da Capacidade 09 — Evolução Contínua**, incluindo `Minha Evolução`, trajetórias por dimensão e período, baseline, direção, evidências, confiança, incerteza, interpretações alternativas, ausência legítima de mudança, controles, privacidade, acessibilidade, contestação, correção, revogação e falha segura.",
        "Consolidar os **eventos funcionais da Capacidade 09 — Evolução Contínua**, incluindo sinais, comandos, propostas, declarações, eventos reconhecidos, agregado, estrutura comum, autoridade, temporalidades, correção compensatória, revogação, propagação, idempotência, ordenação, concorrência, reconstrução e falha segura.",
    )

    # README
    replace_once("README.md", "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 40%`", "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 60%`")
    replace_once(
        "README.md",
        "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0 e PAS-001-EC-LIFECYCLE-001 1.0.0",
        "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0, PAS-001-EC-LIFECYCLE-001 1.0.0 e PAS-001-EC-VIEW-001 1.0.0",
    )
    replace_once(
        "README.md",
        "`PAS-001-EC-LIFECYCLE-001 1.0.0` consolida 17 dimensões independentes, estados e transições, identificação, candidatura, baseline, direção, observação, interpretação, reconhecimento, acompanhamento proporcional, manutenção, estabilidade, progressão, oscilação, regressão, interrupção, recuperação, reorientação, contestação, correção, revogação, propagação, reconstrução e falha segura.\n\nA Capacidade 09 está **In progress**, com progresso editorial de referência de **40%**.",
        "`PAS-001-EC-LIFECYCLE-001 1.0.0` consolida 17 dimensões independentes, estados e transições, identificação, candidatura, baseline, direção, observação, interpretação, reconhecimento, acompanhamento proporcional, manutenção, estabilidade, progressão, oscilação, regressão, interrupção, recuperação, reorientação, contestação, correção, revogação, propagação, reconstrução e falha segura.\n\n`PAS-001-EC-VIEW-001 1.0.0` consolida `Minha Evolução`, trajetórias por dimensão, período e segmento, baseline, direção, estados, padrões, evidências, confiança, incerteza, interpretações alternativas, controles, privacidade, acessibilidade, contestação, correção, revogação, compartilhamento, exportação e falha segura.\n\nA Capacidade 09 está **In progress**, com progresso editorial de referência de **60%**.",
    )
    replace_once(
        "README.md",
        "Retomar na **Visualização e Controle da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- superfície `Minha Evolução`;\n- trajetórias por dimensão e período;\n- baseline, direção, evidências, confiança e incerteza;\n- interpretações alternativas e ausência legítima de mudança;\n- controles, privacidade, acessibilidade, contestação, correção, revogação e falha segura.",
        "Retomar nos **Eventos Funcionais da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- sinais, comandos, propostas, declarações e eventos reconhecidos;\n- agregado `Trajetória de Evolução` e estrutura comum versionada;\n- autoridade, finalidade, temporalidades, proveniência e sensibilidade;\n- famílias de eventos, correção compensatória, revogação e propagação;\n- idempotência, ordenação, concorrência, reconstrução, auditoria e falha segura.",
    )
    replace_once("README.md", "`In progress — 40%`.", "`In progress — 60%`.")
    replace_once("README.md", "| 09 — Evolução Contínua | In progress — 40% |", "| 09 — Evolução Contínua | In progress — 60% |")
    insert_after(
        "README.md",
        "- [Ciclo de Vida da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-ciclo-de-vida.md)\n",
        "- [Visualização e Controle da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-visualizacao-controle.md)\n",
    )

    # Página inicial documental
    replace_once("docs/index.md", "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 40%;", "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 60%;")
    replace_once(
        "docs/index.md",
        "- `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0` como extensões normativas vigentes da Capacidade 09;",
        "- `PAS-001-EC-FOUNDATION-001 1.0.0`, `PAS-001-EC-LIFECYCLE-001 1.0.0` e `PAS-001-EC-VIEW-001 1.0.0` como extensões normativas vigentes da Capacidade 09;",
    )
    replace_once(
        "docs/index.md",
        "Consolidar a **Visualização e Controle da Capacidade 09 — Evolução Contínua**.",
        "Consolidar os **Eventos Funcionais da Capacidade 09 — Evolução Contínua**.",
    )
    replace_once(
        "docs/index.md",
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As seis extensões de Intervenções Contextuais concluem a Capacidade 07 com fundamentos, ciclo de vida, visualização, controle, 19 famílias de eventos, integrações, 80 KPIs em 16 famílias, 28 guardrails, baseline, cenários e contrato final. As seis extensões de Experiências concluem a Capacidade 08 com fundamentos, ciclo de vida, Minhas Experiências, 19 famílias de eventos, integrações, 85 KPIs em 17 famílias, 32 guardrails, baseline, painel de saúde, cenários e contrato final. As duas extensões de Evolução Contínua mantêm a Capacidade 09 ativa com fundamentos, Trajetória de Evolução, direção, baseline, temporalidades, evidências, causalidade, não linearidade, 17 dimensões independentes, estados, transições, acompanhamento, contestação, correção, revogação, reconstrução e falha segura.",
        "As seis extensões vigentes concluem a Capacidade 06 com fundamentos, ciclo de vida, visualização, 19 famílias de eventos, integrações, 75 KPIs em 15 famílias, 24 guardrails, baseline, cenários e contrato final. As seis extensões de Intervenções Contextuais concluem a Capacidade 07 com fundamentos, ciclo de vida, visualização, controle, 19 famílias de eventos, integrações, 80 KPIs em 16 famílias, 28 guardrails, baseline, cenários e contrato final. As seis extensões de Experiências concluem a Capacidade 08 com fundamentos, ciclo de vida, Minhas Experiências, 19 famílias de eventos, integrações, 85 KPIs em 17 famílias, 32 guardrails, baseline, painel de saúde, cenários e contrato final. As três extensões de Evolução Contínua mantêm a Capacidade 09 ativa com fundamentos, ciclo de vida, `Minha Evolução`, direção, baseline, temporalidades, evidências, causalidade, não linearidade, 17 dimensões independentes, estados, transições, visualização, interpretações alternativas, controles, privacidade, acessibilidade, contestação, correção, revogação, reconstrução e falha segura.",
    )
    insert_after(
        "docs/index.md",
        "- [Ciclo de Vida da Evolução Contínua](product-architecture/pas-001-evolucao-continua-ciclo-de-vida.md)\n",
        "- [Visualização e Controle da Evolução Contínua](product-architecture/pas-001-evolucao-continua-visualizacao-controle.md)\n",
    )
    replace_once("docs/index.md", "| 09 — Evolução Contínua | In progress — 40% |", "| 09 — Evolução Contínua | In progress — 60% |")
    replace_once(
        "docs/index.md",
        "Retomar na **Visualização e Controle da Capacidade 09 — Evolução Contínua**.",
        "Retomar nos **Eventos Funcionais da Capacidade 09 — Evolução Contínua**.",
    )

    # Navegação
    insert_after(
        "mkdocs.yml",
        "      - PAS-001-EC-LIFECYCLE-001 — Ciclo de Vida da Evolução Contínua: product-architecture/pas-001-evolucao-continua-ciclo-de-vida.md\n",
        "      - PAS-001-EC-VIEW-001 — Visualização e Controle da Evolução Contínua: product-architecture/pas-001-evolucao-continua-visualizacao-controle.md\n",
    )

    # Changelog
    insert_after(
        "CHANGELOG.md",
        "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n",
        CHANGELOG_ENTRY,
    )


def check() -> None:
    expected = {
        "docs/product-architecture/index.md": ["version: 1.18.0", "PAS-001-EC-VIEW-001 1.0.0", "progresso editorial de referência de `60%`", "eventos funcionais da Evolução Contínua"],
        "docs/roadmap.md": ["version: 10.9.0", "`In progress`, 60%", "PAS-001-EC-VIEW-001 1.0.0", "Eventos Funcionais da Capacidade 09"],
        "docs/project/knowledge-board.md": ["version: 10.9.0", "PAS-001-EC-VIEW-001", "In progress — 60%", "Eventos Funcionais da Capacidade 09"],
        "docs/project/canonical-consolidation-matrix.md": ["version: 1.18.0", "Visualização e Controle da Evolução Contínua", "In progress — 60%", "eventos funcionais da Capacidade 09"],
        "README.md": ["In progress — 60%", "PAS-001-EC-VIEW-001 1.0.0", "Eventos Funcionais da Capacidade 09", "pas-001-evolucao-continua-visualizacao-controle.md"],
        "docs/index.md": ["`In progress`, 60%", "PAS-001-EC-VIEW-001 1.0.0", "Eventos Funcionais da Capacidade 09", "pas-001-evolucao-continua-visualizacao-controle.md"],
        "mkdocs.yml": ["PAS-001-EC-VIEW-001 — Visualização e Controle da Evolução Contínua"],
        "CHANGELOG.md": ["## 0.46.0 — Continuous Evolution View and Control"],
    }
    for path, markers in expected.items():
        content = read(path)
        for marker in markers:
            if marker not in content:
                raise RuntimeError(f"{path}: marcador final ausente: {marker}")

    doc = read("docs/product-architecture/pas-001-evolucao-continua-visualizacao-controle.md")
    headings = [int(value) for value in re.findall(r"^# (\d{4})\.", doc, flags=re.MULTILINE)]
    if headings != list(range(4095, 4185)):
        raise RuntimeError(f"Numeração normativa inválida: {headings[:3]} ... {headings[-3:]}")

    forbidden = re.search(r"# 4182\. Comportamentos proibidos\n\n(.*?)\n\n# 4183\.", doc, flags=re.DOTALL)
    acceptance = re.search(r"# 4183\. Critérios de aceite\n\n(.*?)\n\n# 4184\.", doc, flags=re.DOTALL)
    if not forbidden or not acceptance:
        raise RuntimeError("Blocos de validação não encontrados")
    if len(re.findall(r"^\d+\.", forbidden.group(1), flags=re.MULTILINE)) != 34:
        raise RuntimeError("Quantidade inválida de comportamentos proibidos")
    if len(re.findall(r"^\d+\.", acceptance.group(1), flags=re.MULTILINE)) != 72:
        raise RuntimeError("Quantidade inválida de critérios de aceite")

    forbidden_stale = {
        "docs/product-architecture/index.md": ["version: 1.17.0", "progresso editorial de referência de `40%`"],
        "docs/roadmap.md": ["version: 10.8.0", "| 09 — Evolução Contínua | In progress | 40% |"],
        "docs/project/knowledge-board.md": ["version: 10.8.0", "| Evolução Contínua | In progress — 40% |"],
        "docs/project/canonical-consolidation-matrix.md": ["version: 1.17.0", "Capacidade 09 ativa em 40%"],
    }
    for path, markers in forbidden_stale.items():
        content = read(path)
        for marker in markers:
            if marker in content:
                raise RuntimeError(f"{path}: marcador obsoleto presente: {marker}")

    print("Validação EC-VIEW concluída com sucesso.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check()
    else:
        apply()
        check()


if __name__ == "__main__":
    main()
