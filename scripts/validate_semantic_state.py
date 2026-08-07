#!/usr/bin/env python3
"""Valida a sincronização semântica das superfícies globais do GKR."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "docs/project/current-state-register.md"
README_PATH = ROOT / "README.md"
HOME_PATH = ROOT / "docs/index.md"
UXA_INDEX_PATH = ROOT / "docs/experience-architecture/uxa-047-086-index.md"

REQUIRED_CONTROL_PATHS = [
    ROOT / "docs/project/global-semantic-state-synchronization-policy.md",
    ROOT / "docs/project/changelog-index.md",
    ROOT / "docs/project/canonical-consolidation-addenda-index.md",
    ROOT / "docs/project/p1-post-uxa084-rebaseline-2026-08-06.md",
    ROOT / "docs/project/changelog-p1-post-uxa084-2026-08-06.md",
]

EXPECTED_UXA_FILES = [
    "uxa-047-opportunity-boost-active-campaign-management-functional-validation-and-reformulation.md",
    "uxa-048-opportunity-boost-aggregated-report-low-fidelity-wireframes.md",
    "uxa-049-opportunity-boost-aggregated-report-functional-validation-and-reformulation.md",
    "uxa-050-opportunity-boost-complete-wireframe-set-functional-validation.md",
    "uxa-051-opportunity-boost-mobile-advertiser-configuration-low-fidelity-wireframes.md",
    "uxa-052-opportunity-boost-mobile-advertiser-configuration-functional-validation-and-reformulation.md",
    "uxa-053-opportunity-boost-mobile-active-campaign-management-low-fidelity-wireframes.md",
    "uxa-054-opportunity-boost-mobile-active-campaign-management-functional-validation-and-reformulation.md",
    "uxa-055-opportunity-boost-residual-states-low-fidelity-wireframes.md",
    "uxa-056-collective-discovery-public-profile-and-participation-functional-contract.md",
    "uxa-057-evaluation-and-reputation-functional-contract.md",
    "uxa-058-interactions-recommendations-connections-functional-contract.md",
    "uxa-059-collective-wireframe-program-and-prioritization.md",
    "uxa-060-collective-explore-and-search-mobile-low-fidelity-wireframes.md",
    "uxa-061-collective-explore-and-search-mobile-functional-validation.md",
    "uxa-062-collective-public-profile-mobile-low-fidelity-wireframes.md",
    "uxa-063-collective-public-profile-mobile-functional-validation.md",
    "uxa-064-collective-participation-review-request-mobile-low-fidelity-wireframes.md",
    "uxa-065-collective-participation-review-request-mobile-functional-validation.md",
    "uxa-066-collective-pending-request-mobile-low-fidelity-wireframes.md",
    "uxa-067-collective-pending-request-mobile-functional-validation.md",
    "uxa-068-guided-current-moment-text-voice-low-fidelity-wireframes.md",
    "uxa-069-guided-current-moment-functional-validation-and-reformulation.md",
    "uxa-070-journey-simulation-environment-functional-program.md",
    "uxa-071-integrated-journeys-map-materialization.md",
    "uxa-072-integrated-journeys-functional-validation-and-reformulation.md",
    "uxa-073-integrated-journeys-reformulation-navigation-and-synchronization.md",
    "uxa-074-integrated-journeys-functional-revalidation.md",
    "uxa-075-integrated-journeys-controlled-promotion-and-post-validation-synchronization.md",
    "uxa-076-integrated-journeys-granular-transition-and-surface-registry.md",
    "uxa-077-granular-registry-functional-validation.md",
    "uxa-078-controlled-granular-registry-reformulation.md",
    "uxa-079-granular-registry-functional-revalidation.md",
    "uxa-080-controlled-granular-registry-promotion-and-post-revalidation-synchronization.md",
    "uxa-081-integrated-screen-gallery-and-coverage-audit.md",
    "uxa-082-integrated-gallery-functional-visual-validation-and-gap-prioritization.md",
    "uxa-083-controlled-integrated-gallery-and-inspection-sequence-reformulation.md",
    "uxa-084-reformulated-integrated-gallery-functional-visual-revalidation.md",
    "uxa-085-controlled-integrated-gallery-promotion-and-post-revalidation-synchronization.md",
    "uxa-086-collective-responsible-overview-low-fidelity-wireframe.md",
]

STALE_MARKERS = (
    "M7.48",
    "M7.0 —",
    "GKR-STATE-001 1.99.0",
    "GKR-STATE-001 1.0.2",
    "UXA-071, não iniciada",
)


def read_text(path: Path) -> str:
    if not path.is_file():
        raise ValueError(f"arquivo obrigatório ausente: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("GKR-STATE-001 não possui front matter válido")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("front matter de GKR-STATE-001 não foi encerrado")
    return text[4:end]


def scalar(front: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", front)
    if not match:
        raise ValueError(f"campo {key!r} ausente em GKR-STATE-001")
    return match.group(1).strip().strip("'\"")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    try:
        state_text = read_text(STATE_PATH)
        state_front = front_matter(state_text)
        state_id = scalar(state_front, "id")
        version = scalar(state_front, "version")
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if state_id != "GKR-STATE-001":
        fail(errors, f"ID inesperado para o registro do estado: {state_id}")

    milestone_match = re.search(r"(?m)^\s*-\s*(M\d+\.\d+)\s*$", state_front)
    if not milestone_match:
        fail(errors, "marco não localizado no front matter de GKR-STATE-001")
        milestone = ""
    else:
        milestone = milestone_match.group(1)

    related_uxa = [int(value) for value in re.findall(r"(?m)^\s*-\s*UXA-(\d{3})\s*$", state_front)]
    if not related_uxa:
        fail(errors, "nenhuma frente UXA localizada no front matter de GKR-STATE-001")
        latest_uxa = ""
        next_uxa = ""
    else:
        latest_number = max(related_uxa)
        latest_uxa = f"UXA-{latest_number:03d}"
        next_uxa = f"UXA-{latest_number + 1:03d}"

    surfaces: dict[str, str] = {}
    for path in (README_PATH, HOME_PATH, UXA_INDEX_PATH):
        try:
            surfaces[str(path.relative_to(ROOT))] = read_text(path)
        except ValueError as exc:
            fail(errors, str(exc))

    for name, text in surfaces.items():
        if version not in text:
            fail(errors, f"{name} não declara a versão vigente {version}")
        if milestone and milestone not in text:
            fail(errors, f"{name} não declara o marco vigente {milestone}")
        if latest_uxa and latest_uxa not in text:
            fail(errors, f"{name} não referencia a última frente integrada {latest_uxa}")
        if next_uxa and next_uxa not in text:
            fail(errors, f"{name} não referencia a próxima frente {next_uxa}")
        if latest_uxa and f"{latest_uxa}, não iniciada" in text:
            fail(errors, f"{name} apresenta a última frente integrada como não iniciada")
        for marker in STALE_MARKERS:
            if marker in text:
                fail(errors, f"{name} contém marcador de estado superado: {marker}")

    try:
        index_text = read_text(UXA_INDEX_PATH)
    except ValueError as exc:
        fail(errors, str(exc))
        index_text = ""

    experience_dir = ROOT / "docs/experience-architecture"
    for filename in EXPECTED_UXA_FILES:
        target = experience_dir / filename
        if not target.is_file():
            fail(errors, f"artefato UXA ausente: {target.relative_to(ROOT)}")
        if filename not in index_text:
            fail(errors, f"artefato UXA não indexado: {filename}")

    for path in REQUIRED_CONTROL_PATHS:
        if not path.is_file():
            fail(errors, f"controle P1 ausente: {path.relative_to(ROOT)}")

    if errors:
        print("GKR semantic state validation: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("GKR semantic state validation: PASS")
    print(f"state={version} milestone={milestone} latest={latest_uxa} next={next_uxa}")
    print(f"uxa_artifacts={len(EXPECTED_UXA_FILES)} surfaces={len(surfaces)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
