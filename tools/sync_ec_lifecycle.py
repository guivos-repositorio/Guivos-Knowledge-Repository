from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK = "--check" in sys.argv


def replace_once(path: str, old: str, new: str) -> None:
    file_path = ROOT / path
    text = file_path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected exactly one anchor, found {count}: {old[:100]!r}")
    updated = text.replace(old, new, 1)
    if CHECK:
        raise RuntimeError(f"{path}: pending replacement in check mode")
    file_path.write_text(updated, encoding="utf-8")


def require(path: str, *needles: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise RuntimeError(f"{path}: missing validation marker: {needle!r}")


def absent(path: str, *needles: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        if needle in text:
            raise RuntimeError(f"{path}: stale marker remains: {needle!r}")


if not CHECK:
    # Product Architecture
    replace_once("docs/product-architecture/index.md", "version: 1.16.0", "version: 1.17.0")
    replace_once(
        "docs/product-architecture/index.md",
        "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `20%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0`.",
        "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `40%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0`.",
    )
    replace_once(
        "docs/product-architecture/index.md",
        "- 30 comportamentos proibidos e 52 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `20%`.\n\nO próximo bloco normativo é o ciclo de vida da Evolução Contínua.",
        "- 30 comportamentos proibidos e 52 critérios de aceite.\n\n`PAS-001-EC-LIFECYCLE-001 1.0.0` consolida:\n\n- significado de continuidade sem vigilância permanente ou exigência de progresso constante;\n- `Trajetória de Evolução`, segmentos, janelas de observação, mudanças candidatas, observações, interpretações, evidências e fatores contribuintes;\n- 17 dimensões independentes de estado funcional, informação, baseline, direção, observação, reconhecimento, interpretação, evidências, confiança, temporalidade, sustentação, padrão, causalidade, relação, autorização, contestação e propagação;\n- estados funcionais, transições fundamentais e transições proibidas;\n- identificação, fontes, deduplicação, candidatura, rejeição e avaliação;\n- identidade, titularidade, finalidade, sensibilidade, dimensão, baseline e janela temporal;\n- evidências, suficiência, observação, divergência, magnitude e interpretação;\n- direção, ausência de direção, confirmação do participante e validação profissional limitada;\n- reconhecimento delimitado, acompanhamento proporcional, manutenção, estabilidade, progressão, oscilação, regressão, interrupção, recuperação e reorientação;\n- múltiplas dimensões, trajetórias paralelas, ausência de mudança e separação entre trajetórias individuais, coletivas e institucionais;\n- casos sensíveis, contestação, correção, revogação, propagação, retroatividade, idempotência, ordenação, concorrência, reconstrução e falha segura;\n- 32 comportamentos proibidos e 64 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `40%`.\n\nO próximo bloco normativo é a visualização e o controle da Evolução Contínua.",
    )

    # Roadmap
    replace_once("docs/roadmap.md", "version: 10.7.0", "version: 10.8.0")
    replace_once("docs/roadmap.md", "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 20%.", "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 40%.")
    replace_once(
        "docs/roadmap.md",
        "- **Extensão normativa vigente de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`.",
        "- **Extensões normativas vigentes de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0`.",
    )
    replace_once(
        "docs/roadmap.md",
        "O próximo trabalho deverá consolidar as regras do ciclo de vida da `Capacidade 09 — Evolução Contínua`.",
        "O próximo trabalho deverá consolidar a visualização e o controle da `Capacidade 09 — Evolução Contínua`.",
    )
    replace_once(
        "docs/roadmap.md",
        "- 30 comportamentos proibidos e 52 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `20%`.",
        "- 30 comportamentos proibidos e 52 critérios de aceite.\n\n`PAS-001-EC-LIFECYCLE-001 1.0.0` consolidou:\n\n- significado de continuidade sem coleta ininterrupta, vigilância ou progresso obrigatório;\n- Trajetória de Evolução, segmentos e janelas de observação;\n- 17 dimensões independentes e estados próprios;\n- transições válidas e proibidas;\n- identificação, candidatura, deduplicação, avaliação e rejeição preliminar;\n- baseline, direção, dimensão, temporalidade, observação, evidências, confiança e incerteza;\n- reconhecimento delimitado, acompanhamento proporcional e ausência legítima de mudança;\n- manutenção, estabilidade, progressão, oscilação, regressão, interrupção, recuperação e reorientação;\n- múltiplas dimensões e trajetórias individuais, coletivas e institucionais separadas;\n- casos sensíveis, contestação, correção, revogação e propagação;\n- retroatividade, idempotência, ordenação, concorrência, reconstrução e falha segura;\n- 32 comportamentos proibidos e 64 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `40%`.",
    )
    replace_once("docs/roadmap.md", "| 09 — Evolução Contínua | In progress | 20% |", "| 09 — Evolução Contínua | In progress | 40% |")
    replace_once(
        "docs/roadmap.md",
        "Retomar nas **Regras do Ciclo de Vida da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. identificação de mudança, candidatura e baseline;\n2. observação, interpretação, direção e confirmação;\n3. estabilidade, progressão, oscilação, regressão, interrupção e reorientação;\n4. contestação, correção, revogação e propagação;\n5. idempotência, ordenação, reconstrução e falha segura.",
        "Retomar na **Visualização e Controle da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n1. superfície `Minha Evolução`;\n2. trajetórias por dimensão e período;\n3. baseline, direção, evidências, confiança e incerteza;\n4. interpretações alternativas e ausência legítima de mudança;\n5. controles, privacidade, acessibilidade, contestação, correção, revogação e falha segura.",
    )

    # Knowledge Board
    replace_once("docs/project/knowledge-board.md", "version: 10.7.0", "version: 10.8.0")
    replace_once(
        "docs/project/knowledge-board.md",
        "| PAS-001-EC-FOUNDATION-001 | Active 1.0.0 | Definir os fundamentos iniciais da Capacidade de Evolução Contínua |",
        "| PAS-001-EC-FOUNDATION-001 | Active 1.0.0 | Definir os fundamentos iniciais da Capacidade de Evolução Contínua |\n| PAS-001-EC-LIFECYCLE-001 | Active 1.0.0 | Definir o ciclo de vida da Evolução Contínua |",
    )
    replace_once("docs/project/knowledge-board.md", "| Estado da capacidade ativa | `In progress — 20%` |", "| Estado da capacidade ativa | `In progress — 40%` |")
    replace_once(
        "docs/project/knowledge-board.md",
        "| Extensão normativa de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0` |",
        "| Extensões normativas de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0` |",
    )
    replace_once("docs/project/knowledge-board.md", "| Progresso editorial de Evolução Contínua | `20%` |", "| Progresso editorial de Evolução Contínua | `40%` |")
    replace_once(
        "docs/project/knowledge-board.md",
        "| Foco imediato | Consolidar as regras do ciclo de vida da Capacidade 09 — Evolução Contínua |",
        "| Foco imediato | Consolidar a visualização e o controle da Capacidade 09 — Evolução Contínua |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| 09 — Evolução Contínua | In progress — 20% | Primeira extensão normativa consolidada; ciclo de vida como próximo bloco |",
        "| 09 — Evolução Contínua | In progress — 40% | Duas extensões normativas consolidadas; visualização e controle como próximo bloco |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "- 30 comportamentos proibidos e 52 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `20%`.",
        "- 30 comportamentos proibidos e 52 critérios de aceite.\n\n### Ciclo de vida\n\n- continuidade compreendida sem vigilância permanente ou progresso obrigatório;\n- Trajetória de Evolução, segmentos, janelas, mudanças candidatas, observações e interpretações;\n- 17 dimensões independentes com estados próprios;\n- transições fundamentais e transições proibidas;\n- identificação, fontes, deduplicação, candidatura, rejeição e avaliação;\n- baseline, direção, dimensão, temporalidade, evidências, confiança e incerteza;\n- reconhecimento delimitado e acompanhamento proporcional;\n- manutenção, estabilidade, progressão, oscilação, regressão, interrupção, recuperação e reorientação;\n- múltiplas dimensões, trajetórias paralelas e ausência legítima de mudança;\n- trajetórias individuais, coletivas e institucionais separadas;\n- casos sensíveis, contestação, correção, revogação, propagação, retroatividade, idempotência, ordenação, concorrência, reconstrução e falha segura;\n- 32 comportamentos proibidos e 64 critérios de aceite.\n\nA Capacidade 09 está `In progress`, com progresso editorial de referência de `40%`.",
    )
    replace_once("docs/project/knowledge-board.md", "| Evolução Contínua | In progress — 20% |", "| Evolução Contínua | In progress — 40% |")
    replace_once(
        "docs/project/knowledge-board.md",
        "| Fundamentos de Evolução Contínua | Normative 1.0.0 |",
        "| Fundamentos de Evolução Contínua | Normative 1.0.0 |\n| Ciclo de Vida de Evolução Contínua | Normative 1.0.0 |",
    )
    replace_once("docs/project/knowledge-board.md", "| Roadmap | 10.7.0 |", "| Roadmap | 10.8.0 |")
    replace_once("docs/project/knowledge-board.md", "| Knowledge Board | 10.7.0 |", "| Knowledge Board | 10.8.0 |")
    replace_once(
        "docs/project/knowledge-board.md",
        "| PAS-001-EC-FOUNDATION-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
        "| PAS-001-EC-FOUNDATION-001 | Active 1.0.0 |\n| PAS-001-EC-LIFECYCLE-001 | Active 1.0.0 |\n| GLPA-001 | Approved 1.1.1 |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "Consolidar as **Regras do Ciclo de Vida da Capacidade 09 — Evolução Contínua**, incluindo identificação, candidatura, baseline, observação, interpretação, direção, estabilidade, progressão, oscilação, regressão, interrupção, reorientação, contestação, correção, revogação, propagação, reconstrução e falha segura.",
        "Consolidar a **Visualização e Controle da Capacidade 09 — Evolução Contínua**, incluindo `Minha Evolução`, trajetórias por dimensão e período, baseline, direção, evidências, confiança, incerteza, interpretações alternativas, ausência legítima de mudança, controles, privacidade, acessibilidade, contestação, correção, revogação e falha segura.",
    )

    # Canonical Matrix
    replace_once("docs/project/canonical-consolidation-matrix.md", "version: 1.16.0", "version: 1.17.0")
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "| Evolução Contínua | Refinar | Capacidade 09 ativa em 20%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |",
        "| Evolução Contínua | Refinar | Capacidade 09 ativa em 40%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |",
    )
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "| Fundamentos Iniciais da Evolução Contínua | Manter | PAS-001-EC-FOUNDATION-001 1.0.0 define finalidade, singularidade, direção, baseline, trajetória, temporalidades, evidências, causalidade, não linearidade, privacidade, estados, eventos e limites iniciais |",
        "| Fundamentos Iniciais da Evolução Contínua | Manter | PAS-001-EC-FOUNDATION-001 1.0.0 define finalidade, singularidade, direção, baseline, trajetória, temporalidades, evidências, causalidade, não linearidade, privacidade, estados, eventos e limites iniciais |\n| Ciclo de Vida da Evolução Contínua | Manter | PAS-001-EC-LIFECYCLE-001 1.0.0 define 17 dimensões independentes, estados, transições, identificação, candidatura, baseline, direção, observação, interpretação, reconhecimento, acompanhamento, não linearidade, contestação, correção, revogação, propagação, reconstrução e falha segura |",
    )
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "As Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0` inicia a Capacidade 09 como `In progress — 20%` e consolida finalidade, definição canônica, Trajetória de Evolução, direção, baseline, temporalidades, evidências, correlação, causalidade, não linearidade, autoridade, privacidade, estados, eventos, responsabilidades e limites, sem promover candidatos arquiteturais à Canon.",
        "As Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0` mantêm a Capacidade 09 como `In progress — 40%` e consolidam finalidade, definição canônica, Trajetória de Evolução, direção, baseline, temporalidades, evidências, causalidade, não linearidade, estados, transições, acompanhamento, contestação, correção, revogação, reconstrução e falha segura, sem promover candidatos arquiteturais à Canon.",
    )
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "Consolidar as **regras do ciclo de vida da Capacidade 09 — Evolução Contínua**, incluindo identificação, candidatura, baseline, observação, interpretação, direção, estabilidade, progressão, oscilação, regressão, interrupção, reorientação, contestação, correção, revogação, propagação, reconstrução e falha segura.",
        "Consolidar a **visualização e o controle da Capacidade 09 — Evolução Contínua**, incluindo `Minha Evolução`, trajetórias por dimensão e período, baseline, direção, evidências, confiança, incerteza, interpretações alternativas, ausência legítima de mudança, controles, privacidade, acessibilidade, contestação, correção, revogação e falha segura.",
    )

    # README
    replace_once("README.md", "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 20%`", "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 40%`")
    replace_once(
        "README.md",
        "- **Extensão vigente de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0",
        "- **Extensões vigentes de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0 e PAS-001-EC-LIFECYCLE-001 1.0.0",
    )
    replace_once(
        "README.md",
        "`PAS-001-EC-FOUNDATION-001 1.0.0` consolida finalidade, pergunta central, definição canônica, singularidade, Trajetória de Evolução, direção, baseline, temporalidades, evidências, correlação, causalidade, não linearidade, autoridade, privacidade, estados, eventos, responsabilidades e limites iniciais.\n\nA Capacidade 09 está **In progress**, com progresso editorial de referência de **20%**.\n\n## Ponto exato de retomada\n\nRetomar nas **Regras do Ciclo de Vida da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- identificação de mudança, candidatura e baseline;\n- observação, interpretação, direção e confirmação;\n- estabilidade, progressão, oscilação, regressão, interrupção e reorientação;\n- contestação, correção, revogação e propagação;\n- idempotência, ordenação, reconstrução e falha segura.",
        "`PAS-001-EC-FOUNDATION-001 1.0.0` consolida finalidade, pergunta central, definição canônica, singularidade, Trajetória de Evolução, direção, baseline, temporalidades, evidências, correlação, causalidade, não linearidade, autoridade, privacidade, estados, eventos, responsabilidades e limites iniciais.\n\n`PAS-001-EC-LIFECYCLE-001 1.0.0` consolida 17 dimensões independentes, estados e transições, identificação, candidatura, baseline, direção, observação, interpretação, reconhecimento, acompanhamento proporcional, manutenção, estabilidade, progressão, oscilação, regressão, interrupção, recuperação, reorientação, contestação, correção, revogação, propagação, reconstrução e falha segura.\n\nA Capacidade 09 está **In progress**, com progresso editorial de referência de **40%**.\n\n## Ponto exato de retomada\n\nRetomar na **Visualização e Controle da Capacidade 09 — Evolução Contínua**.\n\nPróxima entrega:\n\n- superfície `Minha Evolução`;\n- trajetórias por dimensão e período;\n- baseline, direção, evidências, confiança e incerteza;\n- interpretações alternativas e ausência legítima de mudança;\n- controles, privacidade, acessibilidade, contestação, correção, revogação e falha segura.",
    )
    replace_once("README.md", "a Capacidade 09 — Evolução Contínua está `In progress — 20%`.", "a Capacidade 09 — Evolução Contínua está `In progress — 40%`.")
    replace_once("README.md", "| 09 — Evolução Contínua | In progress — 20% |", "| 09 — Evolução Contínua | In progress — 40% |")
    replace_once(
        "README.md",
        "- [Fundamentos Iniciais da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-fundamentos-iniciais.md)",
        "- [Fundamentos Iniciais da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-fundamentos-iniciais.md)\n- [Ciclo de Vida da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-ciclo-de-vida.md)",
    )

    # docs/index
    replace_once("docs/index.md", "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 20%;", "- Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 40%;")
    replace_once(
        "docs/index.md",
        "- `PAS-001-EC-FOUNDATION-001 1.0.0` como primeira extensão normativa vigente da Capacidade 09;",
        "- `PAS-001-EC-FOUNDATION-001 1.0.0` e `PAS-001-EC-LIFECYCLE-001 1.0.0` como extensões normativas vigentes da Capacidade 09;",
    )
    replace_once("docs/index.md", "Consolidar as **Regras do Ciclo de Vida da Capacidade 09 — Evolução Contínua**.", "Consolidar a **Visualização e Controle da Capacidade 09 — Evolução Contínua**.")
    replace_once(
        "docs/index.md",
        "A primeira extensão de Evolução Contínua inicia a Capacidade 09 com finalidade, pergunta central, singularidade, direção, baseline, Trajetória de Evolução, temporalidades, evidências, causalidade, não linearidade, autoridade, privacidade, estados, eventos e limites.",
        "As duas extensões de Evolução Contínua mantêm a Capacidade 09 ativa com fundamentos, Trajetória de Evolução, direção, baseline, temporalidades, evidências, causalidade, não linearidade, 17 dimensões independentes, estados, transições, acompanhamento, contestação, correção, revogação, reconstrução e falha segura.",
    )
    replace_once(
        "docs/index.md",
        "- [Fundamentos Iniciais de Evolução Contínua](product-architecture/pas-001-evolucao-continua-fundamentos-iniciais.md)",
        "- [Fundamentos Iniciais de Evolução Contínua](product-architecture/pas-001-evolucao-continua-fundamentos-iniciais.md)\n- [Ciclo de Vida da Evolução Contínua](product-architecture/pas-001-evolucao-continua-ciclo-de-vida.md)",
    )
    replace_once("docs/index.md", "| 09 — Evolução Contínua | In progress — 20% |", "| 09 — Evolução Contínua | In progress — 40% |")
    replace_once("docs/index.md", "Retomar nas **Regras do Ciclo de Vida da Capacidade 09 — Evolução Contínua**.", "Retomar na **Visualização e Controle da Capacidade 09 — Evolução Contínua**.")

    # MkDocs
    replace_once(
        "mkdocs.yml",
        "      - PAS-001-EC-FOUNDATION-001 — Fundamentos de Evolução Contínua: product-architecture/pas-001-evolucao-continua-fundamentos-iniciais.md",
        "      - PAS-001-EC-FOUNDATION-001 — Fundamentos de Evolução Contínua: product-architecture/pas-001-evolucao-continua-fundamentos-iniciais.md\n      - PAS-001-EC-LIFECYCLE-001 — Ciclo de Vida da Evolução Contínua: product-architecture/pas-001-evolucao-continua-ciclo-de-vida.md",
    )

    # Changelog
    changelog = ROOT / "CHANGELOG.md"
    text = changelog.read_text(encoding="utf-8")
    anchor = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    if text.count(anchor) != 1:
        raise RuntimeError("CHANGELOG.md: invalid insertion anchor")
    entry = """## 0.45.0 — Continuous Evolution Lifecycle\n\n- Criação de `PAS-001-EC-LIFECYCLE-001 — Regras do Ciclo de Vida da Evolução Contínua`, versão `1.0.0`.\n- Registro do documento como segunda extensão normativa da Capacidade 09 do `PAS-001 — Guivos Journey`.\n- Elevação do progresso editorial da Capacidade 09 de 20% para 40%, mantendo o estado `In progress`.\n- Definição do significado de continuidade sem vigilância permanente, rastreamento contínuo ou progresso obrigatório.\n- Consolidação de Trajetória de Evolução, segmentos, janelas de observação, mudanças candidatas, observações, interpretações, evidências e fatores contribuintes.\n- Definição de 17 dimensões independentes e seus estados.\n- Consolidação de transições fundamentais e transições proibidas.\n- Definição de identificação, fontes, deduplicação, candidatura, rejeição preliminar e avaliação.\n- Consolidação de baseline, direção, dimensão, temporalidade, evidências, confiança e incerteza.\n- Definição de reconhecimento delimitado e acompanhamento proporcional.\n- Consolidação de manutenção, estabilidade, progressão, oscilação, regressão, interrupção, recuperação e reorientação.\n- Proteção de múltiplas dimensões, trajetórias paralelas e ausência legítima de mudança.\n- Separação entre trajetórias individuais, coletivas e institucionais.\n- Consolidação de contestação, correção, revogação, propagação, retroatividade, idempotência, ordenação, concorrência, reconstrução e falha segura.\n- Registro de 32 comportamentos proibidos e 64 critérios de aceite.\n- Atualização da Arquitetura de Produtos para `1.17.0`.\n- Atualização do Roadmap e do Knowledge Board para `10.8.0`.\n- Atualização da Matriz de Consolidação Canônica para `1.17.0`.\n- Atualização do README, da página inicial e da navegação do MkDocs.\n- Definição de Visualização e Controle da Capacidade 09 como próximo ponto exato.\n\n"""
    changelog.write_text(text.replace(anchor, anchor + entry, 1), encoding="utf-8")

# Validations
require("docs/product-architecture/index.md", "version: 1.17.0", "PAS-001-EC-LIFECYCLE-001 1.0.0", "progresso editorial de referência de `40%`", "visualização e o controle da Evolução Contínua")
require("docs/roadmap.md", "version: 10.8.0", "PAS-001-EC-LIFECYCLE-001 1.0.0", "| 09 — Evolução Contínua | In progress | 40% |", "Visualização e Controle da Capacidade 09")
require("docs/project/knowledge-board.md", "version: 10.8.0", "PAS-001-EC-LIFECYCLE-001", "In progress — 40%", "Visualização e Controle da Capacidade 09")
require("docs/project/canonical-consolidation-matrix.md", "version: 1.17.0", "Ciclo de Vida da Evolução Contínua", "In progress — 40%", "visualização e o controle da Capacidade 09")
require("README.md", "In progress — 40%", "PAS-001-EC-LIFECYCLE-001 1.0.0", "Ciclo de Vida da Evolução Contínua", "Visualização e Controle da Capacidade 09")
require("docs/index.md", "In progress — 40%", "PAS-001-EC-LIFECYCLE-001 1.0.0", "Ciclo de Vida da Evolução Contínua", "Visualização e Controle da Capacidade 09")
require("mkdocs.yml", "PAS-001-EC-LIFECYCLE-001 — Ciclo de Vida da Evolução Contínua")
require("CHANGELOG.md", "## 0.45.0 — Continuous Evolution Lifecycle")
require("docs/product-architecture/pas-001-evolucao-continua-ciclo-de-vida.md", "# 4009. Autoridade e vínculo", "# 4094. Consolidação e próximo ponto", "32 comportamentos proibidos", "64 critérios de aceite")
absent("docs/roadmap.md", "Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 20%", "| 09 — Evolução Contínua | In progress | 20% |")
absent("README.md", "Capacidade ativa:** 09 — Evolução Contínua, `In progress — 20%`", "| 09 — Evolução Contínua | In progress — 20% |")
absent("docs/index.md", "Capacidade 09 — Evolução Contínua como frente ativa, `In progress`, 20%", "| 09 — Evolução Contínua | In progress — 20% |")

print("EC lifecycle synchronization validated")
