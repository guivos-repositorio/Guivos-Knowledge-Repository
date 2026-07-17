#!/usr/bin/env python3
"""Sincroniza os artefatos derivados de PAS-001-EC-FOUNDATION-001.

O script é determinístico e falha quando uma âncora esperada não existe ou
aparece em quantidade diferente de uma. Execute na raiz do repositório:

    python tools/sync_ec_foundation.py

Use --check para validar se a sincronização já foi aplicada.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-17"

FILES = {
    "architecture": ROOT / "docs/product-architecture/index.md",
    "roadmap": ROOT / "docs/roadmap.md",
    "board": ROOT / "docs/project/knowledge-board.md",
    "matrix": ROOT / "docs/project/canonical-consolidation-matrix.md",
    "readme": ROOT / "README.md",
    "changelog": ROOT / "CHANGELOG.md",
}


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 ocorrência, encontrado {count}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 casamento, encontrado {count}")
    return updated


def set_frontmatter_version(text: str, old: str, new: str, label: str) -> str:
    text = replace_once(text, f"version: {old}", f"version: {new}", f"{label}: versão")
    if "last_updated:" in text:
        text = regex_once(
            text,
            r"(?m)^last_updated: .+$",
            f"last_updated: {DATE}",
            f"{label}: data",
        )
    return text


def sync_architecture(text: str) -> str:
    text = set_frontmatter_version(text, "1.15.0", "1.16.0", "Arquitetura")
    text = replace_once(
        text,
        "A próxima frente oficial é a Capacidade 09 — Evolução Contínua, que permanece `Planned` até a aprovação de sua primeira extensão normativa.",
        "A Capacidade 09 — Evolução Contínua está `In progress`, com progresso editorial de referência de `20%`, por meio de `PAS-001-EC-FOUNDATION-001 1.0.0`.",
        "Arquitetura: estado da Capacidade 09",
    )
    section = """
## Capacidade 09 ativa

### Capacidade 09 — Evolução Contínua

`PAS-001-EC-FOUNDATION-001 1.0.0` consolida:

- finalidade, pergunta central, definição canônica, singularidade e valor entregue;
- Evolução Contínua como trajetória governada de mudanças humanas observadas, declaradas ou sustentadas por evidências ao longo do tempo;
- distinções entre mudança, evolução, progresso, resultado, satisfação, Experiência, Evento de Vida, Objetivo, identidade, produtividade, mérito e diagnóstico;
- `Trajetória de Evolução` como unidade funcional, com participante, dimensão, direção, baseline, período, estados, mudanças, evidências, interpretações, confiança, incertezas e histórico;
- direção declarada, ausência legítima de direção e baseline centrada na trajetória do próprio participante;
- temporalidades, duração, sustentação, estabilidade, oscilação, regressão, pausa, reorientação e não linearidade;
- observação e interpretação como dimensões distintas;
- evidências, autoridade das fontes, correlação, causalidade e fatores contribuintes com limites explícitos;
- evolução individual, coletiva e institucional como trajetórias distintas;
- proteção reforçada de espiritualidade, religião, saúde, bem-estar, sensibilidade e terceiros;
- estados e eventos funcionais iniciais, controles, explicabilidade, responsabilidades, limites e neutralidade comercial;
- 30 comportamentos proibidos e 52 critérios de aceite.

A Capacidade 09 está `In progress`, com progresso editorial de referência de `20%`.

O próximo bloco normativo é o ciclo de vida da Evolução Contínua.

"""
    return replace_once(text, "## Regras arquiteturais", section + "## Regras arquiteturais", "Arquitetura: seção EC")


def sync_roadmap(text: str) -> str:
    text = set_frontmatter_version(text, "10.6.0", "10.7.0", "Roadmap")
    text = replace_once(
        text,
        "- **Próxima capacidade:** `09 — Evolução Contínua`, `Planned`.",
        "- **Capacidade ativa:** `09 — Evolução Contínua`, `In progress`, 20%.",
        "Roadmap: estado atual",
    )
    anchor = "- **Extensões normativas vigentes de Experiências:** `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0`, `PAS-001-EXP-INTEGRATION-001 1.0.0` e `PAS-001-EXP-CONTRACT-001 1.0.0`."
    text = replace_once(
        text,
        anchor,
        anchor + "\n- **Extensão normativa vigente de Evolução Contínua:** `PAS-001-EC-FOUNDATION-001 1.0.0`.",
        "Roadmap: extensão EC",
    )
    text = replace_once(
        text,
        "O próximo trabalho deverá consolidar os fundamentos iniciais da `Capacidade 09 — Evolução Contínua`.",
        "O próximo trabalho deverá consolidar as regras do ciclo de vida da `Capacidade 09 — Evolução Contínua`.",
        "Roadmap: direção",
    )
    text = replace_once(text, "## Capacidade 08 ativa", "## Capacidade 08 concluída", "Roadmap: título C08")
    section = """
## Capacidade 09 ativa

### Capacidade 09 — Evolução Contínua

`PAS-001-EC-FOUNDATION-001 1.0.0` consolidou:

- finalidade, pergunta central, definição canônica, singularidade e valor entregue;
- mudança humana como trajetória temporal, sem obrigação de melhoria ascendente;
- distinções entre mudança, evolução, progresso, resultado, satisfação, Experiência, Evento de Vida, Objetivo e identidade;
- direção declarada ou ausente, baseline funcional e comparação limitada;
- `Trajetória de Evolução` como unidade funcional;
- temporalidades, duração, sustentação, não linearidade, estabilidade, oscilação, regressão e reorientação;
- dimensões funcionais não hierárquicas e direção da mudança explicável;
- observação, interpretação, evidências, autoridade, correlação, causalidade e fatores contribuintes;
- confiança, incerteza, ausência de evidência e trajetórias individuais, coletivas e institucionais;
- proteção de espiritualidade, religião, saúde, bem-estar, sensibilidade, privacidade e terceiros;
- estados e eventos iniciais, controles, explicabilidade, responsabilidades, limites e neutralidade comercial;
- 30 comportamentos proibidos e 52 critérios de aceite.

A Capacidade 09 está `In progress`, com progresso editorial de referência de `20%`.

"""
    text = replace_once(text, "## Progresso das capacidades do Journey", section + "## Progresso das capacidades do Journey", "Roadmap: seção EC")
    text = replace_once(
        text,
        "| 09 — Evolução Contínua | Planned | 0% |",
        "| 09 — Evolução Contínua | In progress | 20% |",
        "Roadmap: tabela EC",
    )
    text = replace_once(
        text,
        "Esses entregáveis podem ser executados como frente operacional independente, sem substituir a prioridade arquitetural da Capacidade 08.",
        "Esses entregáveis podem ser executados como frente operacional independente, sem substituir a prioridade arquitetural da Capacidade 09.",
        "Roadmap: prioridade operacional",
    )
    replacement = """## Ponto exato de retomada

Retomar nas **Regras do Ciclo de Vida da Capacidade 09 — Evolução Contínua**.

Próxima entrega:

1. identificação de mudança, candidatura e baseline;
2. observação, interpretação, direção e confirmação;
3. estabilidade, progressão, oscilação, regressão, interrupção e reorientação;
4. contestação, correção, revogação e propagação;
5. idempotência, ordenação, reconstrução e falha segura.
"""
    return regex_once(text, r"## Ponto exato de retomada\n[\s\S]*\Z", replacement, "Roadmap: retomada")


def sync_board(text: str) -> str:
    text = set_frontmatter_version(text, "10.6.0", "10.7.0", "Knowledge Board")
    asset = "| PAS-001-EXP-CONTRACT-001 | Active 1.0.0 | Consolidar KPIs, guardrails, cenários e contrato final das Experiências |"
    text = replace_once(
        text,
        asset,
        asset + "\n| PAS-001-EC-FOUNDATION-001 | Active 1.0.0 | Definir os fundamentos iniciais da Capacidade de Evolução Contínua |",
        "Board: ativo EC",
    )
    text = replace_once(text, "| Próxima capacidade | `09 — Evolução Contínua` |", "| Capacidade ativa | `09 — Evolução Contínua` |", "Board: capacidade ativa")
    text = replace_once(text, "| Estado da próxima capacidade | `Planned` |", "| Estado da capacidade ativa | `In progress — 20%` |", "Board: estado EC")
    anchor = "| Extensões normativas de Experiências | `PAS-001-EXP-FOUNDATION-001 1.0.0`, `PAS-001-EXP-LIFECYCLE-001 1.0.0`, `PAS-001-EXP-VIEW-001 1.0.0`, `PAS-001-EXP-EVENT-001 1.0.0`, `PAS-001-EXP-INTEGRATION-001 1.0.0` e `PAS-001-EXP-CONTRACT-001 1.0.0` |"
    text = replace_once(
        text,
        anchor,
        anchor + "\n| Extensão normativa de Evolução Contínua | `PAS-001-EC-FOUNDATION-001 1.0.0` |\n| Progresso editorial de Evolução Contínua | `20%` |",
        "Board: extensão EC",
    )
    text = replace_once(
        text,
        "| Foco imediato | Consolidar os fundamentos iniciais da Capacidade 09 — Evolução Contínua |",
        "| Foco imediato | Consolidar as regras do ciclo de vida da Capacidade 09 — Evolução Contínua |",
        "Board: foco",
    )
    text = replace_once(
        text,
        "| 09 — Evolução Contínua | Planned | — |",
        "| 09 — Evolução Contínua | In progress — 20% | Primeira extensão normativa consolidada; ciclo de vida como próximo bloco |",
        "Board: tabela EC",
    )
    section = """
## Consolidação inicial da Capacidade 09 — Evolução Contínua

### Fundamentos iniciais

- pergunta central sobre mudanças legitimamente reconhecíveis ao longo do tempo;
- singularidade centrada em trajetórias humanas sem redução a produtividade, consumo, satisfação ou mérito;
- `Trajetória de Evolução` como unidade funcional;
- direção, ausência de direção, baseline e comparação limitada;
- temporalidades, duração, sustentação e não linearidade;
- estabilidade, oscilação, regressão, pausa e reorientação como estados legítimos;
- observação e interpretação separadas;
- evidência, autoridade, correlação, causalidade e fatores contribuintes governados;
- confiança, incerteza e ausência de evidência preservadas;
- trajetórias individuais, coletivas e institucionais separadas;
- proteção de espiritualidade, religião, saúde, bem-estar, sensibilidade e terceiros;
- estados e eventos iniciais, controles, explicabilidade, responsabilidades, limites e neutralidade comercial;
- 30 comportamentos proibidos e 52 critérios de aceite.

A Capacidade 09 está `In progress`, com progresso editorial de referência de `20%`.

"""
    text = replace_once(text, "## Conceitos internos preservados", section + "## Conceitos internos preservados", "Board: consolidação EC")
    concept_anchor = "| Experiências | Functionally complete — 100% |"
    concept_rows = """| Evolução Contínua | In progress — 20% |
| Fundamentos de Evolução Contínua | Normative 1.0.0 |
| Trajetória de Evolução | Unidade funcional que preserva participante, dimensão, direção, baseline, período, estados, mudanças, evidências, interpretações, confiança, incertezas e histórico |
| Baseline de evolução | Referência legítima, preferencialmente centrada na trajetória do próprio participante |
| Não linearidade da evolução | Reconhecimento de avanços, pausas, regressões, oscilações, reorientações e períodos sem mudança |
| Direção de evolução | Referência declarada, legítima, revisável e distinta de valor moral |
"""
    text = replace_once(text, concept_anchor, concept_anchor + "\n" + concept_rows.rstrip(), "Board: conceitos EC")
    text = replace_once(text, "| Roadmap | 10.5.0 |", "| Roadmap | 10.7.0 |", "Board: governança roadmap")
    text = replace_once(text, "| Knowledge Board | 10.5.0 |", "| Knowledge Board | 10.7.0 |", "Board: governança board")
    for doc in ("PAS-001-EXP-EVENT-001", "PAS-001-EXP-INTEGRATION-001", "PAS-001-EXP-CONTRACT-001"):
        marker = f"| {doc} | Active 1.0.0 |"
        if marker not in text:
            insert_after = "| PAS-001-EXP-VIEW-001 | Active 1.0.0 |"
            text = replace_once(text, insert_after, insert_after + f"\n{marker}", f"Board: governança {doc}")
    marker = "| PAS-001-EC-FOUNDATION-001 | Active 1.0.0 |"
    if marker not in text:
        text = replace_once(text, "| PAS-001-EXP-CONTRACT-001 | Active 1.0.0 |", "| PAS-001-EXP-CONTRACT-001 | Active 1.0.0 |\n" + marker, "Board: governança EC")
    text = regex_once(
        text,
        r"## Próxima atividade\n[\s\S]*\Z",
        "## Próxima atividade\n\nConsolidar as **Regras do Ciclo de Vida da Capacidade 09 — Evolução Contínua**, incluindo identificação, candidatura, baseline, observação, interpretação, direção, estabilidade, progressão, oscilação, regressão, interrupção, reorientação, contestação, correção, revogação, propagação, reconstrução e falha segura.\n",
        "Board: próxima atividade",
    )
    return text


def sync_matrix(text: str) -> str:
    text = set_frontmatter_version(text, "1.15.0", "1.16.0", "Matriz")
    anchor = "| KPIs, Guardrails, Cenários e Contrato Final das Experiências | Manter | PAS-001-EXP-CONTRACT-001 1.0.0 define 85 KPIs, 17 famílias, 32 guardrails, baseline, painel de saúde, cenários, critérios de conclusão, lacunas, reabertura e contrato final |"
    rows = """| Evolução Contínua | Refinar | Capacidade 09 ativa em 20%, responsável por trajetórias de mudança humana reconhecidas ao longo do tempo |
| Fundamentos Iniciais da Evolução Contínua | Manter | PAS-001-EC-FOUNDATION-001 1.0.0 define finalidade, singularidade, direção, baseline, trajetória, temporalidades, evidências, causalidade, não linearidade, privacidade, estados, eventos e limites iniciais |
| Trajetória de Evolução | Manter | Unidade funcional com participante, dimensão, direção, baseline, período, estados, mudanças, evidências, interpretações, confiança, incertezas, fatores contribuintes, correções, permissões e histórico |
| Direção de evolução | Refinar | Referência legítima e revisável; não representa obrigação, sucesso universal ou valor moral |
| Baseline de evolução | Manter | Referência temporal legítima, preferencialmente centrada na própria trajetória e distinta de ranking populacional |
| Não linearidade da evolução | Manter | Avanços, pausas, regressões, oscilações, reorientações e períodos sem mudança permanecem representáveis |
| Observação de evolução | Refinar | Fato, resultado ou diferença identificada, distinto de interpretação, identidade e causalidade |
| Interpretação de evolução | Refinar | Leitura explicável, rastreável e contestável sobre observações e trajetória |
| Causalidade de evolução | Refinar | Somente reconhecida com fundamento suficiente; proximidade temporal e correlação não equivalem a causa |
"""
    text = replace_once(text, anchor, anchor + "\n" + rows.rstrip(), "Matriz: conceitos EC")
    text = regex_once(
        text,
        r"## Reconciliação mais recente\n[\s\S]*?\n## Próxima revisão\n[\s\S]*\Z",
        "## Reconciliação mais recente\n\nAs Capacidades 02 a 08 estão funcionalmente concluídas. `PAS-001-EC-FOUNDATION-001 1.0.0` inicia a Capacidade 09 como `In progress — 20%` e consolida finalidade, definição canônica, Trajetória de Evolução, direção, baseline, temporalidades, evidências, correlação, causalidade, não linearidade, autoridade, privacidade, estados, eventos, responsabilidades e limites, sem promover candidatos arquiteturais à Canon.\n\n## Próxima revisão\n\nConsolidar as **regras do ciclo de vida da Capacidade 09 — Evolução Contínua**, incluindo identificação, candidatura, baseline, observação, interpretação, direção, estabilidade, progressão, oscilação, regressão, interrupção, reorientação, contestação, correção, revogação, propagação, reconstrução e falha segura.\n",
        "Matriz: reconciliação",
    )
    return text


def sync_readme(text: str) -> str:
    text = replace_once(
        text,
        "- **Próxima capacidade:** 09 — Evolução Contínua, `Planned`",
        "- **Capacidade ativa:** 09 — Evolução Contínua, `In progress — 20%`",
        "README: estado EC",
    )
    anchor = "- **Extensões vigentes de Experiências:** PAS-001-EXP-FOUNDATION-001 1.0.0, PAS-001-EXP-LIFECYCLE-001 1.0.0, PAS-001-EXP-VIEW-001 1.0.0, PAS-001-EXP-EVENT-001 1.0.0, PAS-001-EXP-INTEGRATION-001 1.0.0 e PAS-001-EXP-CONTRACT-001 1.0.0"
    text = replace_once(text, anchor, anchor + "\n- **Extensão vigente de Evolução Contínua:** PAS-001-EC-FOUNDATION-001 1.0.0", "README: extensão EC")
    section = """
## Capacidade 09 — Evolução Contínua

`PAS-001-EC-FOUNDATION-001 1.0.0` consolida finalidade, pergunta central, definição canônica, singularidade, Trajetória de Evolução, direção, baseline, temporalidades, evidências, correlação, causalidade, não linearidade, autoridade, privacidade, estados, eventos, responsabilidades e limites iniciais.

A Capacidade 09 está **In progress**, com progresso editorial de referência de **20%**.

"""
    text = replace_once(text, "## Ponto exato de retomada", section + "## Ponto exato de retomada", "README: seção EC")
    text = replace_once(text, "Retomar nos **Fundamentos Iniciais da Capacidade 09 — Evolução Contínua**.", "Retomar nas **Regras do Ciclo de Vida da Capacidade 09 — Evolução Contínua**.", "README: retomada")
    text = replace_once(text, "| 09 — Evolução Contínua | Planned |", "| 09 — Evolução Contínua | In progress — 20% |", "README: tabela EC")
    link_anchor = "- [Contrato Final das Experiências](docs/product-architecture/pas-001-experiencias-kpis-cenarios-contrato-final.md)"
    text = replace_once(text, link_anchor, link_anchor + "\n- [Fundamentos Iniciais da Evolução Contínua](docs/product-architecture/pas-001-evolucao-continua-fundamentos-iniciais.md)", "README: link EC")
    return text


def sync_changelog(text: str) -> str:
    entry = """## 0.44.0 — Continuous Evolution Initial Foundations

- Criação de `PAS-001-EC-FOUNDATION-001 — Fundamentos Iniciais da Capacidade de Evolução Contínua`, versão `1.0.0`.
- Registro do documento como primeira extensão normativa da Capacidade 09 do `PAS-001 — Guivos Journey`.
- Substituição do estado da Capacidade 09 de `Planned` para `In progress` e estabelecimento do progresso editorial inicial de 20%.
- Definição da finalidade, pergunta central, definição canônica, singularidade e valor entregue.
- Consolidação de Evolução Contínua como trajetória governada de mudanças humanas observadas, declaradas ou sustentadas por evidências ao longo do tempo.
- Definição da `Trajetória de Evolução` como unidade funcional.
- Consolidação de direção, ausência de direção, baseline, comparação limitada, temporalidades, duração e sustentação.
- Reconhecimento de estabilidade, oscilação, regressão, pausa, reorientação e não linearidade.
- Separação entre observação, interpretação, correlação, contribuição e causalidade.
- Definição de evidências, autoridade das fontes, fatores contribuintes, confiança e incerteza.
- Proteção reforçada de espiritualidade, religião, saúde, bem-estar, sensibilidade e informações de terceiros.
- Definição de estados e eventos funcionais iniciais, controles, explicabilidade, responsabilidades, limites e neutralidade comercial.
- Registro de 30 comportamentos proibidos e 52 critérios de aceite.
- Atualização da Arquitetura de Produtos para `1.16.0` e inclusão da extensão na navegação do MkDocs.
- Atualização do Roadmap e do Knowledge Board para `10.7.0`.
- Atualização da Matriz de Consolidação Canônica para `1.16.0`.
- Atualização do README e da página inicial do GKR.
- Preservação das Capacidades 02 a 08 como `Functionally complete`.
- Definição das Regras do Ciclo de Vida da Capacidade 09 como próximo ponto exato de retomada.

"""
    marker = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n"
    return replace_once(text, marker, marker + entry, "Changelog: entrada 0.44.0")


SYNCERS = {
    "architecture": sync_architecture,
    "roadmap": sync_roadmap,
    "board": sync_board,
    "matrix": sync_matrix,
    "readme": sync_readme,
    "changelog": sync_changelog,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="não grava; exige que a sincronização já esteja aplicada")
    args = parser.parse_args()

    changed = []
    for key, path in FILES.items():
        original = path.read_text(encoding="utf-8")
        if args.check:
            expected_markers = {
                "architecture": ("version: 1.16.0", "PAS-001-EC-FOUNDATION-001 1.0.0"),
                "roadmap": ("version: 10.7.0", "In progress | 20%"),
                "board": ("version: 10.7.0", "PAS-001-EC-FOUNDATION-001"),
                "matrix": ("version: 1.16.0", "Trajetória de Evolução"),
                "readme": ("Capacidade ativa:** 09 — Evolução Contínua", "Fundamentos Iniciais da Evolução Contínua"),
                "changelog": ("## 0.44.0 — Continuous Evolution Initial Foundations", "PAS-001-EC-FOUNDATION-001"),
            }[key]
            missing = [marker for marker in expected_markers if marker not in original]
            if missing:
                raise RuntimeError(f"{path}: sincronização ausente: {missing}")
            continue

        updated = SYNCERS[key](original)
        if updated == original:
            raise RuntimeError(f"{path}: nenhuma alteração produzida")
        path.write_text(updated, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())

    if args.check:
        print("Sincronização de Evolução Contínua validada.")
    else:
        print("Arquivos sincronizados:")
        for path in changed:
            print(f"- {path}")
        print("Execute `python tools/sync_ec_foundation.py --check` após revisar o diff.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
