#!/usr/bin/env python3
"""Validação semântica das superfícies globais do GKR.

Verifica invariantes objetivas entre o Registro do Estado Atual, páginas de
entrada, navegação, índices e arquivos referenciados. Não avalia o mérito de
decisões arquiteturais ou temáticas.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PROJECT = DOCS / "project"
STATE = PROJECT / "current-state-register.md"
README = ROOT / "README.md"
HOME = DOCS / "index.md"
MKDOCS = ROOT / "mkdocs.yml"
CHANGELOG_INDEX = PROJECT / "changelog-index.md"
ADDENDA_INDEX = PROJECT / "canonical-consolidation-addenda-index.md"
POLICY = PROJECT / "global-semantic-state-synchronization-policy.md"
WORKFLOW = ROOT / ".github" / "workflows" / "gkr-semantic-validation.yml"

MILESTONE_ROW = re.compile(
    r"^\|\s*Marco\s*\|.*?\|\s*(M\d+\.\d+)(?:\s*;.*?)?\|\s*$",
    re.MULTILINE,
)
MILESTONE_ANY = re.compile(r"\bM\d+\.\d+\b")
FRONT_MATTER_VALUE = r"^{}\s*:\s*[\"']?([^\"'\n]+?)[\"']?\s*$"

REQUIRED_NAV_PATHS = {
    "project/accumulated-updates-inventory-2026-08-04.md",
    "project/controlled-repository-update-program-2026-08-04.md",
    "project/changelog-index.md",
    "project/canonical-consolidation-addenda-index.md",
    "project/global-semantic-state-synchronization-policy.md",
    "project/changelog-1.95.0-p1-global-semantic-resynchronization.md",
}

REQUIRED_CHANGELOGS = {
    "changelog-1.92.0-uxa-068.md",
    "changelog-1.93.0-uxa-069.md",
    "changelog-1.94.0-uxa-070.md",
    "changelog-1.95.0-p1-global-semantic-resynchronization.md",
}

UXA_NOT_STARTED = re.compile(
    r"\bUXA-071\b(?:(?!\n## ).){0,240}\bnão\s+(?:(?:está|estão|foi|foram)\s+)?iniciad[ao]s?\b",
    re.IGNORECASE | re.DOTALL,
)


def read(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: leitura falhou: {exc}")
        return ""


def require(condition: bool, errors: list[str], message: str) -> None:
    if not condition:
        errors.append(message)


def front_matter_value(text: str, key: str) -> str:
    match = re.search(FRONT_MATTER_VALUE.format(re.escape(key)), text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def require_only_current_milestone(
    text: str,
    label: str,
    milestone: str,
    errors: list[str],
) -> None:
    tokens = set(MILESTONE_ANY.findall(text))
    require(
        tokens == {milestone},
        errors,
        f"{label}: marcos encontrados {sorted(tokens)}; esperado somente {milestone}",
    )


def require_indexed_file(
    path: Path,
    index_text: str,
    index_label: str,
    errors: list[str],
) -> None:
    require(path.exists(), errors, f"{path.relative_to(ROOT)}: arquivo referenciado não existe")
    require(
        path.name in index_text,
        errors,
        f"{index_label}: referência ausente para {path.name}",
    )


def main() -> int:
    errors: list[str] = []

    state = read(STATE, errors)
    readme = read(README, errors)
    home = read(HOME, errors)
    mkdocs = read(MKDOCS, errors)
    changelog_index = read(CHANGELOG_INDEX, errors)
    addenda_index = read(ADDENDA_INDEX, errors)
    policy = read(POLICY, errors)
    workflow = read(WORKFLOW, errors)

    milestone_match = MILESTONE_ROW.search(state)
    require(
        milestone_match is not None,
        errors,
        "Registro do Estado Atual: linha de Marco não encontrada",
    )
    milestone = milestone_match.group(1) if milestone_match else ""
    state_version = front_matter_value(state, "version")
    require(
        bool(state_version),
        errors,
        "Registro do Estado Atual: version ausente no front matter",
    )

    if milestone:
        require_only_current_milestone(readme, "README.md", milestone, errors)
        require_only_current_milestone(home, "docs/index.md", milestone, errors)
        require(
            milestone in changelog_index,
            errors,
            f"índice de changelog: marco vigente {milestone} ausente",
        )

    if state_version:
        for text, label in (
            (readme, "README.md"),
            (home, "docs/index.md"),
            (changelog_index, "índice de changelog"),
        ):
            require(
                state_version in text,
                errors,
                f"{label}: versão vigente do Registro do Estado Atual {state_version} ausente",
            )

    require(
        "docs/project/current-state-register.md" in readme,
        errors,
        "README.md: vínculo para o Registro do Estado Atual ausente",
    )
    require(
        "project/current-state-register.md" in home,
        errors,
        "docs/index.md: vínculo para o Registro do Estado Atual ausente",
    )

    for text, label in (
        (state, "Registro do Estado Atual"),
        (readme, "README.md"),
        (home, "docs/index.md"),
    ):
        require(
            UXA_NOT_STARTED.search(text) is not None,
            errors,
            f"{label}: UXA-071 não está contextualmente declarada como não iniciada",
        )

    require(
        not list(DOCS.glob("experience-architecture/uxa-071-*.md")),
        errors,
        "UXA-071: documento foi localizado apesar do estado não iniciado",
    )

    for number in range(47, 71):
        matches = sorted(DOCS.glob(f"experience-architecture/uxa-{number:03d}-*.md"))
        require(
            len(matches) == 1,
            errors,
            f"UXA-{number:03d}: esperado um documento integrado; encontrados {len(matches)}",
        )
        for path in matches:
            relative = path.relative_to(DOCS).as_posix()
            require(
                relative in mkdocs,
                errors,
                f"mkdocs.yml: {relative} ausente da navegação",
            )

    for relative in sorted(REQUIRED_NAV_PATHS):
        path = DOCS / relative
        require(path.exists(), errors, f"{path.relative_to(ROOT)}: entrada obrigatória não existe")
        require(
            relative in mkdocs,
            errors,
            f"mkdocs.yml: entrada obrigatória ausente: {relative}",
        )

    require(
        "CHANGELOG.md" in changelog_index,
        errors,
        "índice de changelog: ledger raiz não referenciado",
    )
    for name in sorted(REQUIRED_CHANGELOGS):
        require_indexed_file(
            PROJECT / name,
            changelog_index,
            "índice de changelog",
            errors,
        )

    general_addendum = PROJECT / "canonical-consolidation-matrix-opportunity-boost-addendum.md"
    require_indexed_file(
        general_addendum,
        addenda_index,
        "índice de adendos",
        errors,
    )

    for number in range(39, 71):
        require_indexed_file(
            PROJECT / f"canonical-consolidation-matrix-uxa-{number:03d}-addendum.md",
            addenda_index,
            "índice de adendos",
            errors,
        )

    require(
        "GKR-STATE-001" in policy,
        errors,
        "política semântica: autoridade GKR-STATE-001 ausente",
    )
    require(
        "python scripts/validate_gkr_semantic_state.py" in workflow,
        errors,
        "workflow semântico: execução do validador ausente",
    )
    require(
        re.search(r"(?m)^\s*push:\s*$", workflow) is not None
        and re.search(r"(?m)^\s*-\s*main\s*$", workflow) is not None,
        errors,
        "workflow semântico: execução após push na main ausente",
    )

    print(f"Current milestone: {milestone or 'not found'}")
    print(f"Current state version: {state_version or 'not found'}")
    print("UXA navigation entries checked: 24")
    print(f"Required global navigation entries checked: {len(REQUIRED_NAV_PATHS)}")
    print(f"Recent changelog files checked: {len(REQUIRED_CHANGELOGS)}")
    print("Canonical addenda files checked: 33")
    print(
        "Semantic surfaces checked: README, Home, MkDocs, changelog index, "
        "addenda index, policy, workflow"
    )

    if errors:
        print(f"\nSEMANTIC VALIDATION FAILED: {len(errors)} issue(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("\nSEMANTIC VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
