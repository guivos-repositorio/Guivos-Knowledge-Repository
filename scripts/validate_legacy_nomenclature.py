#!/usr/bin/env python3
"""Detect legacy Guivos nomenclature that must not survive in live authority.

The validator distinguishes three classes:
1. forbidden legacy names in live/current documentation -> error;
2. preserved historical/superseded or explicit migration evidence -> reported but not failed;
3. ambiguous Business tier tokens -> reported for semantic review, not auto-rewritten.

The purpose is deliberately conservative: never replace generic words such as
"gestão", "impacto", "rede", "marketplace" or "enterprise" without governed
plan/product context.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

TEXT_SUFFIXES = {".md", ".svg", ".yml", ".yaml", ".json", ".txt"}

# These files intentionally document migrations and therefore may mention
# superseded names without reasserting them as current authority. Keep this
# allowlist narrow and path-specific: a newly created live surface is blocking
# by default until it is explicitly reviewed as migration/reference authority.
EXPLICIT_REFERENCE_FILES = {
    "docs/economic-model/gem-004-plan-taxonomy-conceptual-authority.md",
    "docs/glossary.md",
    "docs/product-architecture/index.md",
    "docs/product-architecture/mall.md",
    "docs/project/legacy-nomenclature-reconciliation-2026-08-08.md",
    # P3 naming/asset governance must retain the superseded product name only
    # to explain the governed migration to Guivos Mall. These exact documents
    # are authorities of migration/evidence, not authorization for live reuse.
    "docs/governance-framework/brand-and-digital-assets-index.md",
    "docs/governance-framework/brand-naming-and-digital-assets-governance.md",
    "docs/governance-framework/digital-asset-control-model.md",
    "docs/governance-framework/official-naming-authority.md",
}

# Versioned project evidence and roadmap snapshots preserve history. They are
# still reported so a human can verify that the old term is genuinely historic.
HISTORICAL_PATH_PREFIXES = (
    "docs/project/",
)

HISTORICAL_FILE_PATTERNS = (
    re.compile(r"^docs/roadmap-\d+\.\d+\.\d+\.md$"),
)

HISTORICAL_STATUSES = {
    "historical",
    "superseded",
    "deprecated",
    "archived",
    "withdrawn",
}


@dataclass(frozen=True)
class Rule:
    key: str
    description: str
    replacement: str
    regex: re.Pattern[str]


FORBIDDEN_RULES = (
    Rule(
        "collective-gestao",
        "nome legado de plano de Coletivo",
        "Coletivo Mobiliza",
        re.compile(r"\bColetivo(?:\s+Guivos)?\s+Gest(?:ã|a)o\b", re.IGNORECASE),
    ),
    Rule(
        "collective-impacto",
        "nome legado de plano de Coletivo",
        "Coletivo Impacta",
        re.compile(r"\bColetivo(?:\s+Guivos)?\s+Impacto\b", re.IGNORECASE),
    ),
    Rule(
        "collective-enterprise",
        "nome legado de plano de Coletivo",
        "Coletivo Rede",
        re.compile(r"\bColetivo(?:\s+Guivos)?\s+Enterprise\b", re.IGNORECASE),
    ),
    Rule(
        "organization-start",
        "tier legado atribuído a Organização",
        "Organização Conecta",
        re.compile(
            r"(?:\bOrganiza(?:ç|c)(?:ã|a)o(?:\s+Guivos)?\s+Start\b|"
            r"\bplano\s+Start\s+(?:da|de)\s+Organiza(?:ç|c)(?:ã|a)o\b)",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "organization-growth",
        "tier legado atribuído a Organização",
        "Organização Eleva",
        re.compile(
            r"(?:\bOrganiza(?:ç|c)(?:ã|a)o(?:\s+Guivos)?\s+Growth\b|"
            r"\bplano\s+Growth\s+(?:da|de)\s+Organiza(?:ç|c)(?:ã|a)o\b)",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "organization-scale",
        "tier legado atribuído a Organização",
        "Organização Transforma",
        re.compile(
            r"(?:\bOrganiza(?:ç|c)(?:ã|a)o(?:\s+Guivos)?\s+Scale\b|"
            r"\bplano\s+Scale\s+(?:da|de)\s+Organiza(?:ç|c)(?:ã|a)o\b)",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "product-marketplace",
        "nome legado do Produto Especializado atualmente denominado Guivos Mall",
        "Guivos Mall",
        re.compile(r"\bGuivos\s+Marketplace\b", re.IGNORECASE),
    ),
)

# Start/Growth/Scale/Enterprise are current Guivos Business tiers, so these
# tokens cannot be globally forbidden. Occurrences outside Business/canonical
# plan authority are surfaced as review candidates only.
BUSINESS_TIER_RE = re.compile(r"\b(?:Start|Growth|Scale|Enterprise)\b")
BUSINESS_CONTEXT_PREFIXES = (
    "docs/product-architecture/business.md",
    "docs/go-to-market/",
    "docs/economic-model/",
)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def front_matter_status(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end]
    match = re.search(r"(?mi)^status:\s*['\"]?([^\n'\"]+)", block)
    return match.group(1).strip().lower() if match else None


def historical_path(rel: str, text: str) -> bool:
    if rel in EXPLICIT_REFERENCE_FILES:
        return True
    if rel.startswith(HISTORICAL_PATH_PREFIXES):
        return True
    if any(pattern.match(rel) for pattern in HISTORICAL_FILE_PATTERNS):
        return True
    status = front_matter_status(text)
    return status in HISTORICAL_STATUSES if status else False


def line_no(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def compact_line(text: str, offset: int) -> str:
    start = text.rfind("\n", 0, offset) + 1
    end = text.find("\n", offset)
    if end == -1:
        end = len(text)
    return " ".join(text[start:end].strip().split())[:240]


def iter_text_files() -> list[Path]:
    paths: list[Path] = []
    for path in DOCS.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            paths.append(path)
    for extra in (ROOT / "README.md", ROOT / "mkdocs.yml"):
        if extra.exists():
            paths.append(extra)
    return sorted(paths)


def main() -> int:
    errors: list[str] = []
    historical: list[str] = []
    candidates: list[str] = []

    for path in iter_text_files():
        text = read_text(path)
        if text is None:
            continue
        rel = relative(path)
        is_historical = historical_path(rel, text)

        for rule in FORBIDDEN_RULES:
            for match in rule.regex.finditer(text):
                item = (
                    f"{rel}:{line_no(text, match.start())}: {match.group(0)!r} -> "
                    f"{rule.replacement} [{rule.key}] | {compact_line(text, match.start())}"
                )
                if is_historical:
                    historical.append(item)
                else:
                    errors.append(item)

        if (
            rel not in EXPLICIT_REFERENCE_FILES
            and not is_historical
            and not any(rel == prefix or rel.startswith(prefix) for prefix in BUSINESS_CONTEXT_PREFIXES)
        ):
            for match in BUSINESS_TIER_RE.finditer(text):
                candidates.append(
                    f"{rel}:{line_no(text, match.start())}: {match.group(0)!r} | "
                    f"{compact_line(text, match.start())}"
                )

    print("GKR legacy nomenclature audit")
    print(f"live violations: {len(errors)}")
    print(f"historical/reference occurrences: {len(historical)}")
    print(f"Business-tier semantic review candidates: {len(candidates)}")

    if errors:
        print("\nERROR — legacy nomenclature asserted in live/current surfaces:")
        for item in errors:
            print(f"  - {item}")

    if historical:
        print("\nINFO — preserved historical/reference occurrences (non-blocking):")
        for item in historical:
            print(f"  - {item}")

    if candidates:
        print("\nREVIEW — Start/Growth/Scale/Enterprise outside explicit Business/economic/GTM context:")
        for item in candidates:
            print(f"  - {item}")

    if errors:
        print(
            "\nValidation failed. Replace only proven live legacy names. "
            "Do not mass-replace generic words or historical evidence."
        )
        return 1

    print("\nLegacy nomenclature gate passed for known forbidden live terms and aliases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
