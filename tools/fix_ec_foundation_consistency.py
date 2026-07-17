#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1, encontrado {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    architecture = ROOT / "docs/product-architecture/index.md"
    readme = ROOT / "README.md"
    board = ROOT / "docs/project/knowledge-board.md"

    replace_once(
        architecture,
        "## Capacidade 08 ativa",
        "## Capacidade 08 concluída",
        "Arquitetura: título da Capacidade 08",
    )

    old_delivery = """Próxima entrega:

- finalidade e pergunta central;
- singularidade da evolução contínua;
- mudança observada, direção, temporalidade e evidência;
- interpretação, causalidade e progresso humano não linear;
- autonomia, limites e proteção contra avaliação moral;
- relações com as demais capacidades do Journey.
"""
    new_delivery = """Próxima entrega:

- identificação de mudança, candidatura e baseline;
- observação, interpretação, direção e confirmação;
- estabilidade, progressão, oscilação, regressão, interrupção e reorientação;
- contestação, correção, revogação e propagação;
- idempotência, ordenação, reconstrução e falha segura.
"""
    replace_once(readme, old_delivery, new_delivery, "README: próxima entrega")

    replace_once(
        readme,
        "As Capacidades 06 — Oportunidades Ativas, 07 — Intervenções Contextuais e 08 — Experiências estão `Functionally complete`; a Capacidade 09 — Evolução Contínua permanece `Planned`.",
        "As Capacidades 06 — Oportunidades Ativas, 07 — Intervenções Contextuais e 08 — Experiências estão `Functionally complete`; a Capacidade 09 — Evolução Contínua está `In progress — 20%`.",
        "README: estado Product Engineering",
    )

    old_governance = """| PAS-001-EXP-VIEW-001 | Active 1.0.0 |
| GLPA-001 | Approved 1.1.1 |"""
    new_governance = """| PAS-001-EXP-VIEW-001 | Active 1.0.0 |
| PAS-001-EXP-EVENT-001 | Active 1.0.0 |
| PAS-001-EXP-INTEGRATION-001 | Active 1.0.0 |
| PAS-001-EXP-CONTRACT-001 | Active 1.0.0 |
| PAS-001-EC-FOUNDATION-001 | Active 1.0.0 |
| GLPA-001 | Approved 1.1.1 |"""
    replace_once(board, old_governance, new_governance, "Board: governança normativa")

    checks = {
        architecture: ["## Capacidade 08 concluída", "## Capacidade 09 ativa"],
        readme: ["Capacidade 09 — Evolução Contínua está `In progress — 20%`", "identificação de mudança, candidatura e baseline"],
        board: ["| PAS-001-EC-FOUNDATION-001 | Active 1.0.0 |", "| PAS-001-EXP-CONTRACT-001 | Active 1.0.0 |"],
    }
    for path, markers in checks.items():
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                raise RuntimeError(f"{path}: marcador ausente: {marker}")


if __name__ == "__main__":
    main()
