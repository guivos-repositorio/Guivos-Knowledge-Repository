#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

BASE_SHA = "72a20d43f12d7efb9c646368ec009828c607924f"

CANDIDATES = {
    "UXA-005": "uxa-005-low-fidelity-wireframes.md",
    "UXA-006": "uxa-006-today-low-fidelity-wireframe.md",
    "UXA-007": "uxa-007-opportunity-detail-low-fidelity-wireframe.md",
    "UXA-008": "uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md",
    "UXA-022": "uxa-022-public-home-low-fidelity-wireframe.md",
    "UXA-024": "uxa-024-opportunity-map-low-fidelity-wireframe.md",
    "UXA-034": "uxa-034-protected-journey-entry-low-fidelity-wireframe.md",
    "UXA-036": "uxa-036-initial-understanding-low-fidelity-wireframe.md",
    "UXA-040": "uxa-040-opportunity-boost-advertiser-flow-low-fidelity-wireframes.md",
    "UXA-042": "uxa-042-opportunity-boost-sponsored-card-and-explanation-low-fidelity-wireframes.md",
    "UXA-044": "uxa-044-opportunity-boost-sponsored-list-and-map-low-fidelity-wireframes.md",
    "UXA-046": "uxa-046-opportunity-boost-active-campaign-management-low-fidelity-wireframes.md",
    "UXA-048": "uxa-048-opportunity-boost-aggregated-report-low-fidelity-wireframes.md",
    "UXA-051": "uxa-051-opportunity-boost-mobile-advertiser-configuration-low-fidelity-wireframes.md",
    "UXA-053": "uxa-053-opportunity-boost-mobile-active-campaign-management-low-fidelity-wireframes.md",
    "UXA-055": "uxa-055-opportunity-boost-residual-states-low-fidelity-wireframes.md",
    "UXA-060": "uxa-060-collective-explore-and-search-mobile-low-fidelity-wireframes.md",
    "UXA-062": "uxa-062-collective-public-profile-mobile-low-fidelity-wireframes.md",
    "UXA-064": "uxa-064-collective-participation-review-request-mobile-low-fidelity-wireframes.md",
    "UXA-066": "uxa-066-collective-pending-request-mobile-low-fidelity-wireframes.md",
    "UXA-068": "uxa-068-guided-current-moment-text-voice-low-fidelity-wireframes.md",
    "UXA-086": "uxa-086-collective-responsible-overview-low-fidelity-wireframe.md",
    "UXA-088": "uxa-088-collective-request-management-low-fidelity-wireframes.md",
    "UXA-091": "uxa-091-my-collectives-materialization-and-post-approval-continuity-refinement.md",
    "UXA-093": "uxa-093-collective-updates-center-materialization.md",
    "UXA-095": "uxa-095-participant-home-materialization-and-trn111-refinement.md",
}

ALREADY_REMOVED = {
    "UXA-081": "uxa-081-integrated-screen-gallery-and-coverage-audit.md",
    "UXA-082": "uxa-082-integrated-gallery-functional-visual-validation-and-gap-prioritization.md",
    "UXA-083": "uxa-083-controlled-integrated-gallery-and-inspection-sequence-reformulation.md",
    "UXA-084": "uxa-084-reformulated-integrated-gallery-functional-visual-revalidation.md",
    "UXA-085": "uxa-085-controlled-integrated-gallery-promotion-and-post-revalidation-synchronization.md",
}

KEEP_IDS = {
    "UXA-035", "UXA-037", "UXA-041", "UXA-050", "UXA-052", "UXA-054",
    "UXA-059", "UXA-061", "UXA-063", "UXA-065", "UXA-067", "UXA-069",
    "UXA-087", "UXA-089", "UXA-090", "UXA-092", "UXA-094", "UXA-096", "UXA-097",
}

KEEP_PATHS = {
    "docs/experience-architecture/d5-c2-direction-movement-evolution-low-fidelity-wireframes.md",
    "docs/experience-architecture/d5-c3-direction-movement-evolution-functional-validation.md",
    "docs/experience-architecture/public-home-pre-wireframe-readiness-audit.md",
    "docs/experience-architecture/organizations-collectives-ux-state.md",
}

SVG_PATH_RE = re.compile(r"(?i)(?:docs/)?assets/wireframes/([A-Za-z0-9._-]+\.svg)")
MD_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\n]+)\)")
FM_ITEM_RE = re.compile(r"^(\s*-\s*)[\"']?(UXA-\d{3})[\"']?(\s*(?:#.*)?)$")


def front_matter(text: str) -> tuple[str, str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[:4], text[4:end], text[end:]


def clean_structural_frontmatter(text: str, candidate_ids: set[str]) -> tuple[str, int]:
    parts = front_matter(text)
    if not parts:
        return text, 0
    prefix, front, suffix = parts
    lines = front.splitlines()
    out: list[str] = []
    current_key = ""
    removed = 0

    for line in lines:
        top = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if top:
            current_key = top.group(1)
            value = (top.group(2) or "").strip()
            if current_key in {"related", "depends_on"} and value:
                inline = re.fullmatch(r"\[(.*)\]", value)
                if inline:
                    items = [x.strip().strip("'\"") for x in inline.group(1).split(",") if x.strip()]
                    kept = [x for x in items if x not in candidate_ids]
                    removed += len(items) - len(kept)
                    if kept:
                        out.append(f"{current_key}: [{', '.join(kept)}]")
                    else:
                        current_key = ""
                    continue
                scalar = value.strip("'\"")
                if scalar in candidate_ids:
                    removed += 1
                    current_key = ""
                    continue
            out.append(line)
            continue

        if current_key in {"related", "depends_on"}:
            item = FM_ITEM_RE.match(line)
            if item and item.group(2) in candidate_ids:
                removed += 1
                continue
        out.append(line)

    compact: list[str] = []
    for i, line in enumerate(out):
        if re.fullmatch(r"(?:related|depends_on):\s*", line):
            nxt = out[i + 1] if i + 1 < len(out) else ""
            if not re.match(r"^\s+-\s+", nxt):
                continue
        compact.append(line)

    return prefix + "\n".join(compact) + suffix, removed


def normalized_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1:target.index(">")]
    else:
        target = target.split()[0] if target else ""
    target = target.split("#", 1)[0].split("?", 1)[0]
    return target.replace("\\", "/")


def transform_markdown(text: str, by_filename: dict[str, str], candidate_ids: set[str]) -> tuple[str, dict[str, int]]:
    counts = {"structural": 0, "producer_links": 0, "svg_links": 0, "producer_filenames": 0, "svg_paths": 0}
    text, n = clean_structural_frontmatter(text, candidate_ids)
    counts["structural"] += n

    def repl_link(match: re.Match[str]) -> str:
        bang, label, raw = match.groups()
        target = normalized_target(raw)
        base = Path(target).name
        if base in by_filename:
            counts["producer_links"] += 1
            uid = by_filename[base]
            desc = label.strip() or uid
            return f"{desc} — `{uid}` [historical producer removed_after_absorption in F-016]"
        svg = SVG_PATH_RE.search(target)
        if svg:
            counts["svg_links"] += 1
            desc = label.strip() or svg.group(1)
            return f"{desc} — {svg.group(1)} [historical SVG; physical file removed in F-016-A]"
        return match.group(0)

    text = MD_LINK_RE.sub(repl_link, text)

    for filename, uid in by_filename.items():
        occurrences = text.count(filename)
        if occurrences:
            counts["producer_filenames"] += occurrences
            text = text.replace(filename, f"{uid} [historical producer removed_after_absorption in F-016]")

    def repl_svg(match: re.Match[str]) -> str:
        counts["svg_paths"] += 1
        return f"{match.group(1)} [historical SVG; physical file removed in F-016-A]"

    text = SVG_PATH_RE.sub(repl_svg, text)
    return text, counts


def update_semantic_validator(root: Path) -> None:
    path = root / "scripts/validate_semantic_state.py"
    text = path.read_text(encoding="utf-8")
    start = text.index("    removed_after_absorption = {")
    end = text.index("    for path in CONTROL_PATHS:", start)
    combined = {**CANDIDATES, **ALREADY_REMOVED}
    items = []
    for uid, filename in sorted(combined.items(), key=lambda kv: int(kv[0].split("-")[1])):
        number = int(uid.split("-")[1])
        items.append(f'        {number}: "{filename}",')
    replacement = "    removed_after_absorption = {\n" + "\n".join(items) + "\n    }\n\n"
    replacement += "    for number, expected_name in removed_after_absorption.items():\n"
    replacement += "        expected_path = UXA_DIR / expected_name\n"
    replacement += "        path = artifacts.get(number)\n"
    replacement += "        if expected_path.is_file() or path is not None:\n"
    replacement += "            errors.append(f\"artefato UXA-{number:03d} deveria estar ausente após cleanup governado\")\n"
    replacement += "        if expected_name in index_text:\n"
    replacement += "            errors.append(f\"artefato removido UXA-{number:03d} permanece indexado: {expected_name}\")\n\n"
    replacement += "    for number in range(47, 102):\n"
    replacement += "        if number in removed_after_absorption:\n"
    replacement += "            continue\n"
    replacement += "        path = artifacts.get(number)\n"
    replacement += "        if path is None:\n"
    replacement += "            errors.append(f\"artefato UXA-{number:03d} ausente\")\n"
    replacement += "        elif path.name not in index_text:\n"
    replacement += "            errors.append(f\"artefato UXA-{number:03d} não indexado: {path.name}\")\n\n"
    path.write_text(text[:start] + replacement + text[end:], encoding="utf-8")


def update_mechanical_guard(root: Path) -> None:
    path = root / "scripts/validate_gkr.py"
    text = path.read_text(encoding="utf-8")
    if "F016_SVG_PATH_REFERENCE" not in text:
        marker = "MARKDOWN_LINK = re.compile(r\"!?\\[[^\\]]*\\]\\(([^)]+)\\)\")\n"
        insert = marker + "F016_SVG_PATH_REFERENCE = re.compile(r\"(?i)(?:docs/)?assets/wireframes/[^\\s)`\\\"']+\\.svg\")\n"
        if marker not in text:
            raise RuntimeError("MARKDOWN_LINK marker not found in validate_gkr.py")
        text = text.replace(marker, insert, 1)

        marker2 = "    markdown_files = sorted(DOCS.rglob(\"*.md\"))\n"
        insert2 = marker2 + "    wireframe_dir = DOCS / \"assets\" / \"wireframes\"\n    physical_svgs = sorted(wireframe_dir.glob(\"*.svg\")) if wireframe_dir.is_dir() else []\n    for svg in physical_svgs:\n        fail(errors, f\"F-016: SVG físico reintroduzido: {svg.relative_to(ROOT)}\")\n    for path in markdown_files:\n        raw = read_utf8(path, errors)\n        if raw is not None and F016_SVG_PATH_REFERENCE.search(raw):\n            fail(errors, f\"F-016: referência direta a SVG físico removido: {path.relative_to(ROOT)}\")\n"
        if marker2 not in text:
            raise RuntimeError("markdown_files marker not found in validate_gkr.py")
        text = text.replace(marker2, insert2, 1)
    path.write_text(text, encoding="utf-8")


def prepare(root: Path) -> None:
    root = root.resolve()
    docs = root / "docs"
    by_filename = {filename: uid for uid, filename in CANDIDATES.items()}
    candidate_ids = set(CANDIDATES)
    totals = {"structural": 0, "producer_links": 0, "svg_links": 0, "producer_filenames": 0, "svg_paths": 0}
    modified_docs = 0

    for path in sorted(docs.rglob("*.md")):
        old = path.read_text(encoding="utf-8")
        new, counts = transform_markdown(old, by_filename, candidate_ids)
        if new != old:
            path.write_text(new, encoding="utf-8")
            modified_docs += 1
        for key, value in counts.items():
            totals[key] += value

    deleted = 0
    for uid, filename in CANDIDATES.items():
        path = docs / "experience-architecture" / filename
        if not path.is_file():
            raise RuntimeError(f"expected producer missing before cleanup: {uid} {path}")
        path.unlink()
        deleted += 1

    mkdocs = root / "mkdocs.yml"
    old = mkdocs.read_text(encoding="utf-8")
    lines = old.splitlines(keepends=True)
    removed_nav = sum(1 for line in lines if any(filename in line for filename in by_filename))
    new = "".join(line for line in lines if not any(filename in line for filename in by_filename))
    if new != old:
        mkdocs.write_text(new, encoding="utf-8")

    update_semantic_validator(root)
    update_mechanical_guard(root)

    print(f"F016_PREPARE_BASE={BASE_SHA}")
    print(f"F016_DELETED_PRODUCERS={deleted}")
    print(f"F016_MODIFIED_MARKDOWN={modified_docs}")
    for key, value in totals.items():
        print(f"F016_{key.upper()}={value}")
    print(f"F016_MKDOCS_LINES_REMOVED={removed_nav}")


def doc_id(text: str) -> str | None:
    parts = front_matter(text)
    if not parts:
        return None
    m = re.search(r"(?m)^id:\s*[\"']?([^\n\"']+)", parts[1])
    return m.group(1).strip() if m else None


def proof(root: Path, require_resolved: bool = False) -> None:
    root = root.resolve()
    docs = root / "docs"
    errors: list[str] = []
    candidate_ids = set(CANDIDATES)
    filenames = set(CANDIDATES.values())

    for uid, filename in CANDIDATES.items():
        path = docs / "experience-architecture" / filename
        if path.exists():
            errors.append(f"producer still exists: {uid} {path.relative_to(root)}")

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
        did = doc_id(text)
        if did:
            known_ids.add(did)
        if SVG_PATH_RE.search(text):
            svg_path_hits.append(str(path.relative_to(root)))
        for filename in filenames:
            if filename in text:
                filename_hits.append(f"{path.relative_to(root)} -> {filename}")
        parts = front_matter(text)
        if parts:
            front = parts[1]
            current = ""
            for line in front.splitlines():
                top = re.match(r"^([A-Za-z0-9_-]+):", line)
                if top:
                    current = top.group(1)
                    value = line.split(":", 1)[1]
                    if current in {"related", "depends_on"}:
                        for uid in candidate_ids:
                            if re.search(rf"\b{re.escape(uid)}\b", value):
                                structural_hits.append(f"{path.relative_to(root)}:{current}:{uid}")
                    continue
                if current in {"related", "depends_on"}:
                    for uid in candidate_ids:
                        if re.search(rf"\b{re.escape(uid)}\b", line):
                            structural_hits.append(f"{path.relative_to(root)}:{current}:{uid}")
        for uid in candidate_ids:
            body_id_occurrences += len(re.findall(rf"\b{re.escape(uid)}\b", text))

    if svg_path_hits:
        errors.extend(f"direct SVG path remains: {x}" for x in svg_path_hits)
    if filename_hits:
        errors.extend(f"removed producer filename remains: {x}" for x in filename_hits)
    if structural_hits:
        errors.extend(f"structural reference remains: {x}" for x in structural_hits)

    missing_keep = sorted(KEEP_IDS - known_ids)
    if missing_keep:
        errors.append("KEEP IDs missing: " + ", ".join(missing_keep))
    for rel in sorted(KEEP_PATHS):
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
        stale = [
            "OPEN / REPO-WIDE DOCUMENTATION DEMATERIALIZATION",
            "NEXT F-016 SUBFRONT",
            "CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES INDIVIDUALLY",
            "demais famílias Markdown continuam em auditoria",
        ]
        for marker in stale:
            if marker in state or marker in audit:
                errors.append(f"stale F-016 marker remains: {marker}")

    print(f"F016_PROOF_DELETED_COUNT={sum(not (docs / 'experience-architecture' / fn).exists() for fn in CANDIDATES.values())}")
    print(f"F016_PROOF_PHYSICAL_SVG_COUNT={len(physical)}")
    print(f"F016_PROOF_STRUCTURAL_HITS={len(structural_hits)}")
    print(f"F016_PROOF_FILENAME_HITS={len(filename_hits)}")
    print(f"F016_PROOF_SVG_PATH_HITS={len(svg_path_hits)}")
    print(f"F016_PROOF_BODY_ID_OCCURRENCES={body_id_occurrences}")
    print(f"F016_PROOF_KEEP_IDS={len(KEEP_IDS & known_ids)}/{len(KEEP_IDS)}")

    if errors:
        print("F016_PROOF=FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    print("F016_PROOF=SUCCESS")


def replace_required(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"required marker not found in {path}: {old[:120]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def finalize(root: Path) -> None:
    root = root.resolve()
    state = root / "docs/project/current-state-register.md"
    audit = root / "docs/project/gkr-full-corpus-audit.md"

    replace_required(state, "version: 3.11.0", "version: 3.12.0")
    replace_required(
        state,
        "F-016\n→ OPEN / REPO-WIDE DOCUMENTATION DEMATERIALIZATION",
        "F-016\n→ RESOLVED\n→ AUDIT + ADJUDICATION + IMPLEMENTATION + POST-DELETE PROOF COMPLETE\n→ LEGACY VISUAL PRODUCERS REMOVED\n→ 26/26\n→ DIRECT REMOVED-SVG PATH REFERENCES = 0\n→ PHYSICAL SVG COUNT = 0",
    )
    replace_required(
        state,
        "NEXT F-016 SUBFRONT\n→ CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES INDIVIDUALLY\n→ NO AUTOMATIC MARKDOWN DELETION",
        "F-016 CLOSURE\n→ 26 LEGACY VISUAL PRODUCERS REMOVED AFTER ABSORPTION\n→ STRUCTURAL REFERENCES RECONCILED\n→ 23 DIRECT PATH REFERENCES TO REMOVED SVGs NEUTRALIZED\n→ CURRENT AUTHORITIES / VALIDATORS / EVIDENCE PRESERVED\n→ REINTRODUCTION GUARDS ACTIVE",
    )
    replace_required(
        state,
        "O encerramento de `F-016-A` remove a camada física SVG do GKR, mas não promove maturidade funcional, não cria Design e não libera implementação.",
        "O encerramento de `F-016` conclui a desmaterialização documental auditada sem promover maturidade funcional, sem criar Design e sem liberar implementação. A história permanece no Git; o corpus vigente preserva autoridades, validadores e evidências necessárias.",
    )

    replace_required(audit, "version: 1.13.0", "version: 1.14.0")
    old_row = "| F-016 | Major | corpus ainda contém documentos de materialização e linguagem de UI que podem competir com Design; camada física SVG, família `screen-gallery*` e ciclo `UXA-081..085` já foram desmaterializados após prova de absorção | `REMOVE_AFTER_ABSORPTION + REWRITE` | **OPEN — F-016-A RESOLVED; `screen-gallery*` removida 8/8 e `UXA-081..085` removidos 5/5 após absorção; demais famílias Markdown continuam em auditoria** |"
    new_row = "| F-016 | Major | o corpus continha produtores visuais legados e referências estruturais capazes de competir com Design; a auditoria separou produtores removíveis de autoridades, validadores e evidências que devem permanecer | `REMOVE_AFTER_ABSORPTION + REWRITE` | **RESOLVED — cleanup documental 26/26 concluído após absorção; referências estruturais reconciliadas; 23 caminhos de SVG removidos neutralizados; autoridades/validadores/evidências preservados; guards e prova pós-delete concluídos** |"
    replace_required(audit, old_row, new_row)

    closure = """
### 6.1 Fechamento de F-016 — desmaterialização documental governada

A adjudicação de `F-016` foi implementada somente depois da prova de absorção das famílias legadas. O fechamento preserva a distinção entre histórico Git e verdade documental vigente.

```text
F-016
→ RESOLVED

LEGACY VISUAL PRODUCERS
→ REMOVE_AFTER_ABSORPTION EXECUTED
→ 26/26 REMOVED

PHYSICAL SVGs
→ 0

DIRECT PATH REFERENCES TO REMOVED SVGs
→ 23 IDENTIFIED BEFORE CLEANUP
→ 0 LIVE/DIRECT PATH REFERENCES AFTER CLEANUP

STRUCTURAL depends_on / related TO REMOVED PRODUCERS
→ 0 AFTER RECONCILIATION

CURRENT AUTHORITIES / VALIDATORS / EVIDENCE
→ PRESERVED

REINTRODUCTION GUARDS
→ ACTIVE IN SEMANTIC + MECHANICAL VALIDATION

POST-DELETE READ-ONLY PROOF
→ SUCCESS
```

Este fechamento não autoriza Design, nova materialização, `UXA-102 / V5`, Product Engineering, liberação automática de J/K/L/M/N nem merge da PR #363.

"""
    anchor = "## 7. F-003 — Home principal/Pessoa — resolvido no Lote D"
    text = audit.read_text(encoding="utf-8")
    if anchor not in text:
        raise RuntimeError("audit section anchor not found")
    audit.write_text(text.replace(anchor, closure + anchor, 1), encoding="utf-8")

    for rel in ["README.md", "docs/index.md", "docs/experience-architecture/uxa-047-101-index.md"]:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        if "3.11.0" not in text:
            raise RuntimeError(f"current-state version 3.11.0 not found in synchronization surface {rel}")
        path.write_text(text.replace("3.11.0", "3.12.0"), encoding="utf-8")

    print("F016_FINALIZE=SUCCESS")


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: f016_cleanup_executor.py prepare|proof|finalize|proof-final <repo-root>", file=sys.stderr)
        return 2
    mode = sys.argv[1]
    root = Path(sys.argv[2])
    if mode == "prepare":
        prepare(root)
    elif mode == "proof":
        proof(root, require_resolved=False)
    elif mode == "finalize":
        finalize(root)
    elif mode == "proof-final":
        proof(root, require_resolved=True)
    else:
        raise SystemExit(f"unknown mode: {mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
