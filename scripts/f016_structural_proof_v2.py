#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

import f016_cleanup_executor as model


def scalar_values(value):
    if value is None:
        return []
    if isinstance(value, str):
        return [value.strip()]
    if isinstance(value, (list, tuple, set)):
        out = []
        for item in value:
            out.extend(scalar_values(item))
        return out
    return [str(value).strip()]


def frontmatter_dict(text: str) -> dict:
    parts = model.front_matter(text)
    if not parts:
        return {}
    data = yaml.safe_load(parts[1])
    return data if isinstance(data, dict) else {}


def proof(root: Path, require_resolved: bool = False) -> None:
    root = root.resolve()
    docs = root / "docs"
    errors: list[str] = []
    candidate_ids = set(model.CANDIDATES)
    filenames = set(model.CANDIDATES.values())

    deleted_count = 0
    for uid, filename in model.CANDIDATES.items():
        path = docs / "experience-architecture" / filename
        if path.exists():
            errors.append(f"producer still exists: {uid} {path.relative_to(root)}")
        else:
            deleted_count += 1

    svg_dir = docs / "assets" / "wireframes"
    physical = sorted(svg_dir.glob("*.svg")) if svg_dir.is_dir() else []
    if physical:
        errors.append(f"physical SVG count is {len(physical)}, expected 0")

    known_ids: set[str] = set()
    structural_hits: list[str] = []
    filename_hits: list[str] = []
    svg_path_hits: list[str] = []
    body_id_occurrences = 0

    for path in sorted(docs.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        did = model.doc_id(text)
        if did:
            known_ids.add(did)

        if model.SVG_PATH_RE.search(text):
            svg_path_hits.append(str(path.relative_to(root)))

        for filename in filenames:
            if filename in text:
                filename_hits.append(f"{path.relative_to(root)} -> {filename}")

        fm = frontmatter_dict(text)
        for key in ("related", "depends_on"):
            for value in scalar_values(fm.get(key)):
                if value in candidate_ids:
                    structural_hits.append(f"{path.relative_to(root)}:{key}:{value}")

        for uid in candidate_ids:
            body_id_occurrences += len(re.findall(rf"(?<![A-Za-z0-9-]){re.escape(uid)}(?![A-Za-z0-9-])", text))

    if svg_path_hits:
        errors.extend(f"direct SVG path remains: {x}" for x in svg_path_hits)
    if filename_hits:
        errors.extend(f"removed producer filename remains: {x}" for x in filename_hits)
    if structural_hits:
        errors.extend(f"exact structural reference remains: {x}" for x in structural_hits)

    missing_keep = sorted(model.KEEP_IDS - known_ids)
    if missing_keep:
        errors.append("KEEP IDs missing: " + ", ".join(missing_keep))
    for rel in sorted(model.KEEP_PATHS):
        if not (root / rel).is_file():
            errors.append(f"KEEP path missing: {rel}")

    if require_resolved:
        state = (root / "docs/project/current-state-register.md").read_text(encoding="utf-8")
        audit = (root / "docs/project/gkr-full-corpus-audit.md").read_text(encoding="utf-8")
        required = [
            ("state", "F-016\n→ RESOLVED", state),
            ("state", "LEGACY VISUAL PRODUCERS REMOVED\n→ 26/26", state),
            ("audit", "F-016 | Major", audit),
            ("audit", "**RESOLVED — cleanup documental", audit),
        ]
        for where, needle, text in required:
            if needle not in text:
                errors.append(f"closure marker missing in {where}: {needle}")

        # Historical checkpoints inside the non-normative audit are provenance,
        # not current-state drift. Stale markers are forbidden only in the
        # normative current-state authority; the audit must preserve history.
        stale_current_state = [
            "OPEN / REPO-WIDE DOCUMENTATION DEMATERIALIZATION",
            "NEXT F-016 SUBFRONT",
            "CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES INDIVIDUALLY",
            "demais famílias Markdown continuam em auditoria",
        ]
        for marker in stale_current_state:
            if marker in state:
                errors.append(f"stale F-016 marker remains in current state: {marker}")

    print(f"F016_PROOF_DELETED_COUNT={deleted_count}")
    print(f"F016_PROOF_PHYSICAL_SVG_COUNT={len(physical)}")
    print(f"F016_PROOF_EXACT_STRUCTURAL_HITS={len(structural_hits)}")
    print(f"F016_PROOF_FILENAME_HITS={len(filename_hits)}")
    print(f"F016_PROOF_SVG_PATH_HITS={len(svg_path_hits)}")
    print(f"F016_PROOF_BODY_ID_OCCURRENCES={body_id_occurrences}")
    print(f"F016_PROOF_KEEP_IDS={len(model.KEEP_IDS & known_ids)}/{len(model.KEEP_IDS)}")

    if errors:
        print("F016_EXACT_PROOF=FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    print("F016_EXACT_PROOF=SUCCESS")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: f016_structural_proof_v2.py <repo-root> [--require-resolved]", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    proof(root, require_resolved="--require-resolved" in sys.argv[2:])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
