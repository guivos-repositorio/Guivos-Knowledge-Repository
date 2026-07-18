from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PA = DOCS / "product-architecture"
OUT = ROOT / "pas001-audit-output.json"

EXPECTED = {
    "CC": 3,
    "CV": 8,
    "OBJ": 7,
    "EV": 6,
    "PP": 6,
    "OA": 6,
    "IC": 6,
    "EXP": 6,
    "EC": 6,
}
FINAL_IDS = {
    "CC": "PAS-001-CC-CONTRACT-001",
    "CV": "PAS-001-CV-CONTRACT-001",
    "OBJ": "PAS-001-OBJ-CONTRACT-001",
    "EV": "PAS-001-EV-CONTRACT-001",
    "PP": "PAS-001-PP-CONTRACT-001",
    "OA": "PAS-001-OA-CONTRACT-001",
    "IC": "PAS-001-IC-CONTRACT-001",
    "EXP": "PAS-001-EXP-CONTRACT-001",
    "EC": "PAS-001-EC-CONTRACT-001",
}
REQUIRED_META = {"id", "title", "status", "version", "owner", "last_updated"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def front_matter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    block = text[4:end].splitlines()
    data: dict[str, object] = {}
    current_list: str | None = None
    for line in block:
        if re.match(r"^\s+-\s+", line) and current_list:
            assert isinstance(data[current_list], list)
            data[current_list].append(re.sub(r"^\s+-\s+", "", line).strip())
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        if value == "":
            data[key] = []
            current_list = key
        else:
            data[key] = value.strip("\"'")
            current_list = None
    return data


def slugify(title: str) -> str:
    import unicodedata
    value = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s-]+", "-", value)
    return value.strip("-")


def headings(text: str) -> set[str]:
    result = set()
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            result.add(slugify(re.sub(r"\s+#+$", "", match.group(1))))
    return result


def extract_question(text: str) -> str | None:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^#{1,6}\s+.*(?:pergunta|quest[aã]o)\s+(?:central|normativa)", line, re.I):
            for candidate in lines[index + 1:index + 15]:
                if candidate.startswith(">"):
                    return candidate.lstrip("> ").strip().strip("*")
    return None


def has_reopen(text: str) -> bool:
    return bool(re.search(r"^#{1,6}\s+.*reabertura", text, re.I | re.M))


def local_links(path: Path, text: str) -> list[tuple[str, str | None]]:
    links: list[tuple[str, str | None]] = []
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        if target.startswith("#"):
            links.append(("", target[1:]))
            continue
        file_part, anchor = (target.split("#", 1) + [None])[:2] if "#" in target else (target, None)
        links.append((file_part, anchor))
    return links


files: list[dict[str, object]] = []
by_id: dict[str, dict[str, object]] = {}
cap_counts: Counter[str] = Counter()
questions: dict[str, list[dict[str, str]]] = defaultdict(list)
missing_metadata: list[dict[str, object]] = []

for path in sorted(PA.glob("pas-001*.md")):
    text = read(path)
    meta = front_matter(text)
    doc_id = str(meta.get("id", ""))
    if not doc_id:
        continue
    record = {
        "id": doc_id,
        "path": str(path.relative_to(ROOT)),
        "title": meta.get("title"),
        "status": meta.get("status"),
        "version": meta.get("version"),
        "parent": meta.get("parent"),
        "normative": meta.get("normative"),
        "related": meta.get("related", []),
        "question": extract_question(text),
        "has_reopen": has_reopen(text),
    }
    files.append(record)
    by_id[doc_id] = record
    cap_match = re.match(r"PAS-001-(CC|CV|OBJ|EV|PP|OA|IC|EXP|EC)-", doc_id)
    if cap_match:
        cap = cap_match.group(1)
        cap_counts[cap] += 1
        if record["question"]:
            questions[cap].append({"id": doc_id, "question": str(record["question"])})
        absent = sorted(REQUIRED_META - set(meta))
        if absent:
            missing_metadata.append({"id": doc_id, "path": record["path"], "missing": absent})

# MkDocs navigation and file existence.
mkdocs_path = ROOT / "mkdocs.yml"
mkdocs = read(mkdocs_path)
nav_paths = re.findall(r":\s+([^\s#]+\.md)\s*$", mkdocs, re.M)
missing_nav_targets = [path for path in nav_paths if not (DOCS / path).exists()]
journey_nav_ids = re.findall(r"-\s+(PAS-001(?:-[A-Z0-9-]+)?)\s+—", mkdocs)

# Link validation for PAS-001 documents and canonical navigation artifacts.
link_scope = [PA / Path(str(item["path"])).name for item in files]
link_scope += [
    ROOT / "README.md",
    DOCS / "index.md",
    PA / "index.md",
    DOCS / "roadmap.md",
    DOCS / "project" / "knowledge-board.md",
    DOCS / "project" / "canonical-consolidation-matrix.md",
]
broken_links: list[dict[str, str]] = []
checked_links = 0
for path in link_scope:
    if not path.exists():
        continue
    text = read(path)
    own_headings = headings(text)
    for file_part, anchor in local_links(path, text):
        checked_links += 1
        if file_part == "":
            target_path = path
            target_headings = own_headings
        else:
            target_path = (path.parent / file_part).resolve()
            try:
                target_path.relative_to(ROOT.resolve())
            except ValueError:
                broken_links.append({"source": str(path.relative_to(ROOT)), "target": file_part, "reason": "outside-repository"})
                continue
            if not target_path.exists():
                broken_links.append({"source": str(path.relative_to(ROOT)), "target": file_part, "reason": "missing-file"})
                continue
            target_headings = headings(read(target_path)) if anchor else set()
        if anchor and slugify(anchor) not in target_headings:
            broken_links.append({"source": str(path.relative_to(ROOT)), "target": f"{file_part}#{anchor}", "reason": "missing-anchor"})

# Final contracts and reopening criteria.
final_contracts: dict[str, dict[str, object]] = {}
for cap, doc_id in FINAL_IDS.items():
    record = by_id.get(doc_id)
    final_contracts[cap] = {
        "id": doc_id,
        "present": record is not None,
        "status": record.get("status") if record else None,
        "version": record.get("version") if record else None,
        "has_reopen": record.get("has_reopen") if record else False,
    }

# Version synchronization anchors.
canonical_paths = {
    "product_architecture": PA / "index.md",
    "roadmap": DOCS / "roadmap.md",
    "board": DOCS / "project" / "knowledge-board.md",
    "matrix": DOCS / "project" / "canonical-consolidation-matrix.md",
    "changelog": ROOT / "CHANGELOG.md",
    "pas001": PA / "pas-001-guivos-journey.md",
}
versions = {name: front_matter(read(path)).get("version") if path.exists() else None for name, path in canonical_paths.items()}
versions["changelog_latest"] = (re.search(r"^##\s+([^\n]+)", read(ROOT / "CHANGELOG.md"), re.M).group(1) if (ROOT / "CHANGELOG.md").exists() else None)

# Readiness and map evidence.
roadmap = read(canonical_paths["roadmap"])
board = read(canonical_paths["board"])
product_index = read(canonical_paths["product_architecture"])
all_caps_named = all(name in roadmap and name in board for name in [
    "Captura de Contexto", "Contexto Vivo", "Objetivos", "Eventos de Vida", "Próximos Passos",
    "Oportunidades Ativas", "Intervenções Contextuais", "Experiências", "Evolução Contínua"
])

matrix_text = read(canonical_paths["matrix"])
full_supersession_fields = all(term in matrix_text.lower() for term in [
    "seção original", "documento substituto", "ação editorial", "necessidade de reabertura"
])
authority_register_fields = all(term in matrix_text.lower() for term in [
    "documento pai", "autoridade", "dependências", "critérios de reabertura"
])

results = {
    "expected_counts": EXPECTED,
    "actual_counts": dict(cap_counts),
    "count_match": {cap: cap_counts[cap] == expected for cap, expected in EXPECTED.items()},
    "total_capability_extensions": sum(cap_counts.values()),
    "files": files,
    "missing_metadata": missing_metadata,
    "final_contracts": final_contracts,
    "questions": questions,
    "question_coverage": {cap: bool(questions.get(cap)) for cap in EXPECTED},
    "nav": {
        "total_markdown_targets": len(nav_paths),
        "missing_targets": missing_nav_targets,
        "journey_ids": journey_nav_ids,
        "audit_present": "PAS-001-AUDIT-001" in mkdocs,
    },
    "links": {
        "checked": checked_links,
        "broken": broken_links,
    },
    "versions": versions,
    "all_capabilities_named_in_roadmap_and_board": all_caps_named,
    "full_supersession_matrix_present": full_supersession_fields,
    "authority_register_present": authority_register_fields,
    "readiness_mentions": {
        "roadmap_conditionally_ready": "Conditionally ready — final PAS-001 audit required" in roadmap,
        "board_conditionally_ready": "Conditionally ready — final PAS-001 audit required" in board,
        "product_index_conditionally_ready": "Conditionally ready — final PAS-001 audit required" in product_index,
    },
}
OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({
    "total_capability_extensions": results["total_capability_extensions"],
    "count_match": results["count_match"],
    "missing_metadata": len(missing_metadata),
    "broken_links": len(broken_links),
    "question_coverage": results["question_coverage"],
    "final_contracts": final_contracts,
    "full_supersession_matrix_present": full_supersession_fields,
    "authority_register_present": authority_register_fields,
}, ensure_ascii=False, indent=2))
