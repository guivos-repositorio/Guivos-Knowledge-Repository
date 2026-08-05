#!/usr/bin/env python3
"""Validação semântica das superfícies globais do GKR.

Verifica invariantes objetivas entre o Registro do Estado Atual, páginas de
entrada, navegação e índices de histórico/consolidação. Não avalia o mérito de
decisões arquiteturais ou temáticas.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
STATE = DOCS / "project" / "current-state-register.md"
README = ROOT / "README.md"
HOME = DOCS / "index.md"
MKDOCS = ROOT / "mkdocs.yml"
CHANGELOG_INDEX = DOCS / "project" / "changelog-index.md"
ADDENDA_INDEX = DOCS / "project" / "canonical-consolidation-addenda-index.md"
POLICY = DOCS / "project" / "global-semantic-state-synchronization-policy.md"

MILESTONE_ROW = re.compile(r"^\|\s*Marco\s*\|.*?\|.*?\b(M\d+\.\d+)\b.*?\|\s*$", re.MULTILINE)
MILESTONE_ANY = re.compile(r"\bM\d+\.\d+\b")
STALE_ENTRY_MILESTONES = {"M7.48"}

UXA_FILES = {
    number: next(
        DOCS.glob(f"experience-architecture/uxa-{number:03d}-*.md"),
        None,
    )
    for number in range(47, 71)
}

REQUIRED_NAV_PATHS = {
    "project/accumulated-updates-inventory-2026-08-04.md",
    "project/controlled-repository-update-program-2026-08-04.md",
    "project/changelog-index.md",
    "project/canonical-consolidation-addenda-index.md",
    "project/global-semantic-state-synchronization-policy.md",
    "project/changelog-1.95.0-p1-global-semantic-resynchronization.md",
}


def read(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: leitura falhou: {exc}")
        return ""


def require(condition: bool, errors: list[str], message: str) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    state = read(STATE, errors)
    readme = read(README, errors)
    home = read(HOME, errors)
    mkdocs = read(MKDOCS, errors)
    changelog_index = read(CHANGELOG_INDEX, errors)
    addenda_index = read(ADDENDA_INDEX, errors)
    policy = read(POLICY, errors)

    match = MILESTONE_ROW.search(state)
    require(match is not None, errors, "Registro do Estado Atual: linha de Marco não encontrada")
    milestone = match.group(1) if match else ""

    if milestone:
        require(milestone in readme, errors, f"README.md: marco vigente {milestone} ausente")
        require(milestone in home, errors, f"docs/index.md: marco vigente {milestone} ausente")
        require(milestone in changelog_index, errors, f"índice de changelog: marco vigente {milestone} ausente")

    for stale in sorted(STALE_ENTRY_MILESTONES):
        require(stale not in readme, errors, f"README.md: marco superado {stale} permanece na entrada")
        require(stale not in home, errors, f"docs/index.md: marco superado {stale} permanece na entrada")

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

    for number, path in UXA_FILES.items():
        require(path is not None, errors, f"UXA-{number:03d}: documento integrado não localizado")
        if path is not None:
            relative = path.relative_to(DOCS).as_posix()
            require(relative in mkdocs, errors, f"mkdocs.yml: {relative} ausente da navegação")

    for relative in sorted(REQUIRED_NAV_PATHS):
        require(relative in mkdocs, errors, f"mkdocs.yml: entrada obrigatória ausente: {relative}")

    require("../../CHANGELOG.md" in changelog_index, errors, "índice de changelog: ledger raiz não referenciado")
    require("changelog-1.95.0-p1-global-semantic-resynchronization.md" in changelog_index, errors, "índice de changelog: P1 1.95.0 ausente")

    for number in range(39, 71):
        expected = f"canonical-consolidation-matrix-uxa-{number:03d}-addendum.md"
        require(expected in addenda_index, errors, f"índice de adendos: UXA-{number:03d} ausente")

    require("UXA-071" in state and "não iniciad" in state.lower(), errors, "Registro do Estado Atual: UXA-071 não está explicitamente preservada como não iniciada")
    require("UXA-071" in readme and "não iniciad" in readme.lower(), errors, "README.md: UXA-071 não está explicitamente preservada como não iniciada")
    require("UXA-071" in home and "não iniciad" in home.lower(), errors, "docs/index.md: UXA-071 não está explicitamente preservada como não iniciada")

    require("GKR-STATE-001" in policy, errors, "política semântica: autoridade GKR-STATE-001 ausente")
    require(not MILESTONE_ANY.search(readme.replace(milestone, "", 1)) if milestone else True, errors, "README.md: múltiplos marcos globais detectados")

    print(f"Current milestone: {milestone or 'not found'}")
    print(f"UXA navigation entries checked: {len(UXA_FILES)}")
    print(f"Required global navigation entries checked: {len(REQUIRED_NAV_PATHS)}")
    print("Semantic surfaces checked: README, Home, MkDocs, changelog index, addenda index, policy")

    if errors:
        print(f"\nSEMANTIC VALIDATION FAILED: {len(errors)} issue(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("\nSEMANTIC VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
