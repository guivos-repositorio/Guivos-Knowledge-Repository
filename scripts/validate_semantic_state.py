#!/usr/bin/env python3
"""Valida a sincronização semântica das superfícies globais do GKR."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "docs/project/current-state-register.md"
README = ROOT / "README.md"
HOME = ROOT / "docs/index.md"
UXA_DIR = ROOT / "docs/experience-architecture"
UXA_INDEX = UXA_DIR / "uxa-047-101-index.md"
CONTROL_PATHS = [
    ROOT / "docs/project/global-semantic-state-synchronization-policy.md",
    ROOT / "docs/project/changelog-index.md",
    ROOT / "docs/project/canonical-consolidation-addenda-index.md",
    ROOT / "docs/project/p1-post-uxa084-rebaseline-2026-08-06.md",
    ROOT / "docs/project/changelog-p1-post-uxa084-2026-08-06.md",
]
STALE = ("M7.48", "M7.0 —", "GKR-STATE-001 1.99.0", "GKR-STATE-001 1.0.2", "UXA-071, não iniciada")


def read(path: Path) -> str:
    if not path.is_file():
        raise ValueError(f"arquivo obrigatório ausente: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def fm(text: str) -> str:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("front matter inválido")
    return text[4:text.find("\n---\n", 4)]


def scalar(front: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", front)
    if not match:
        raise ValueError(f"campo {key!r} ausente")
    return match.group(1).strip().strip("'\"")


def main() -> int:
    errors: list[str] = []
    try:
        state_text = read(STATE)
        front = fm(state_text)
        state_id = scalar(front, "id")
        version = scalar(front, "version")
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if state_id != "GKR-STATE-001":
        errors.append(f"ID inesperado: {state_id}")

    milestone_match = re.search(r"(?m)^\s*-\s*(M\d+\.\d+)\s*$", front)
    milestone = milestone_match.group(1) if milestone_match else ""
    if not milestone:
        errors.append("marco não localizado no front matter")

    related = [int(v) for v in re.findall(r"(?m)^\s*-\s*UXA-(\d{3})\s*$", front)]
    latest = f"UXA-{max(related):03d}" if related else ""
    next_uxa = f"UXA-{max(related)+1:03d}" if related else ""
    if not related:
        errors.append("nenhuma frente UXA no front matter")

    surfaces = {}
    for path in (README, HOME, UXA_INDEX):
        try:
            surfaces[str(path.relative_to(ROOT))] = read(path)
        except ValueError as exc:
            errors.append(str(exc))

    for name, text in surfaces.items():
        for expected, label in ((version, "versão"), (milestone, "marco"), (latest, "última UXA"), (next_uxa, "próxima UXA")):
            if expected and expected not in text:
                errors.append(f"{name} não declara {label} {expected}")
        if latest and f"{latest}, não iniciada" in text:
            errors.append(f"{name} apresenta {latest} como não iniciada")
        for marker in STALE:
            if marker in text:
                errors.append(f"{name} contém marcador superado: {marker}")

    try:
        index_text = read(UXA_INDEX)
    except ValueError as exc:
        errors.append(str(exc))
        index_text = ""

    artifacts: dict[int, Path] = {}
    for path in UXA_DIR.glob("uxa-*.md"):
        try:
            match = re.search(r"(?m)^id:\s*UXA-(\d{3})\s*$", fm(read(path)))
        except ValueError:
            continue
        if match:
            artifacts[int(match.group(1))] = path

    for number in range(47, 102):
        path = artifacts.get(number)
        if path is None:
            errors.append(f"artefato UXA-{number:03d} ausente")
        elif path.name not in index_text:
            errors.append(f"artefato UXA-{number:03d} não indexado: {path.name}")

    for path in CONTROL_PATHS:
        if not path.is_file():
            errors.append(f"controle P1 ausente: {path.relative_to(ROOT)}")

    if errors:
        print("GKR semantic state validation: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("GKR semantic state validation: PASS")
    print(f"state={version} milestone={milestone} latest={latest} next={next_uxa}")
    print(f"uxa_artifacts={len(artifacts)} surfaces={len(surfaces)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())