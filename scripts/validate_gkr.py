#!/usr/bin/env python3
"""Validação mecânica do Guivos Knowledge Repository.

Verifica:
- sintaxe do mkdocs.yml;
- front matter YAML dos documentos Markdown;
- unicidade dos IDs declarados no front matter;
- existência dos caminhos configurados na navegação;
- rótulos de navegação orientados por assunto, sem IDs técnicos expostos;
- resolução de links e imagens Markdown locais.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"

FRONT_MATTER_DELIMITER = re.compile(r"^---\s*$")
FENCED_CODE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`]*`")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
NAV_TECHNICAL_IDENTIFIER = re.compile(
    r"(?:^|\s)(?:UXA|GEM|GAI|GEF|GEB|GLPA|PAS|UIC|VAL|RP|AV|ADR|GCCM|MS|A2-R\d+)"
    r"-[A-Z0-9][A-Z0-9.-]*(?=\s|$|\s*[—–-])",
    re.IGNORECASE,
)


class MkDocsLoader(yaml.SafeLoader):
    """Loader tolerante às referências Python usadas pelo MkDocs."""


def _unknown_tag(loader: MkDocsLoader, tag_suffix: str, node: yaml.Node) -> str:
    del loader, node
    return tag_suffix


MkDocsLoader.add_multi_constructor("tag:yaml.org,2002:python/name:", _unknown_tag)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_utf8(path: Path, errors: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        fail(errors, f"{path.relative_to(ROOT)}: leitura UTF-8 falhou: {exc}")
        return None


def parse_front_matter(path: Path, text: str, errors: list[str]) -> dict[str, Any] | None:
    lines = text.splitlines()
    if not lines or not FRONT_MATTER_DELIMITER.match(lines[0]):
        return None

    closing = next(
        (index for index, line in enumerate(lines[1:], start=1) if FRONT_MATTER_DELIMITER.match(line)),
        None,
    )
    if closing is None:
        fail(errors, f"{path.relative_to(ROOT)}: front matter sem delimitador de fechamento")
        return None

    raw = "\n".join(lines[1:closing])
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        fail(errors, f"{path.relative_to(ROOT)}: front matter YAML inválido: {exc}")
        return None

    if not isinstance(data, dict):
        fail(errors, f"{path.relative_to(ROOT)}: front matter deve ser um mapa YAML")
        return None

    if "id" in data and (not isinstance(data["id"], str) or not data["id"].strip()):
        fail(errors, f"{path.relative_to(ROOT)}: campo id deve ser texto não vazio")

    return data


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        return target[1:-1].strip()

    # Remove título opcional: (arquivo.md "Título").
    match = re.match(r"([^\s]+)(?:\s+[\"'].*)?$", target)
    return match.group(1) if match else target


def candidate_paths(source: Path, target: str) -> Iterable[Path]:
    decoded = unquote(target).replace("\\", "/")
    split = urlsplit(decoded)
    path_text = split.path
    if not path_text:
        return []

    if path_text.startswith("/"):
        base = DOCS
        relative = path_text.lstrip("/")
    else:
        base = source.parent
        relative = path_text

    candidate = (base / relative).resolve()
    candidates = [candidate]

    if candidate.suffix.lower() == ".html":
        candidates.append(candidate.with_suffix(".md"))

    if not candidate.suffix:
        candidates.extend(
            [
                candidate.with_suffix(".md"),
                candidate / "index.md",
                candidate / "README.md",
            ]
        )
    elif candidate.is_dir():
        candidates.extend([candidate / "index.md", candidate / "README.md"])

    return candidates


def is_external(target: str) -> bool:
    lowered = target.lower()
    return (
        not target
        or target.startswith("#")
        or lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:"))
        or target.startswith("{{")
    )


def validate_markdown_links(markdown_files: list[Path], errors: list[str]) -> int:
    checked = 0
    for path in markdown_files:
        text = read_utf8(path, errors)
        if text is None:
            continue
        scrubbed = INLINE_CODE.sub("", FENCED_CODE.sub("", text))
        for match in MARKDOWN_LINK.finditer(scrubbed):
            raw_target = match.group(1)
            target = normalize_target(raw_target)
            if is_external(target):
                continue

            checked += 1
            candidates = list(candidate_paths(path, target))
            if not candidates or not any(candidate.exists() for candidate in candidates):
                fail(
                    errors,
                    f"{path.relative_to(ROOT)}: link local não resolvido: {target}",
                )
    return checked


def load_mkdocs(errors: list[str]) -> dict[str, Any] | None:
    text = read_utf8(MKDOCS, errors)
    if text is None:
        return None
    try:
        data = yaml.load(text, Loader=MkDocsLoader)
    except yaml.YAMLError as exc:
        fail(errors, f"mkdocs.yml: YAML inválido: {exc}")
        return None
    if not isinstance(data, dict):
        fail(errors, "mkdocs.yml: raiz deve ser um mapa YAML")
        return None
    return data


def nav_paths(node: Any) -> Iterable[str]:
    if isinstance(node, str):
        yield node
    elif isinstance(node, list):
        for item in node:
            yield from nav_paths(item)
    elif isinstance(node, dict):
        for value in node.values():
            yield from nav_paths(value)


def nav_labels(node: Any) -> Iterable[str]:
    """Percorre somente os rótulos visíveis do menu configurado em nav."""
    if isinstance(node, list):
        for item in node:
            yield from nav_labels(item)
    elif isinstance(node, dict):
        for label, value in node.items():
            yield str(label)
            yield from nav_labels(value)


def validate_navigation(config: dict[str, Any], errors: list[str]) -> int:
    nav = config.get("nav")
    if nav is None:
        fail(errors, "mkdocs.yml: chave nav ausente")
        return 0

    checked = 0
    for entry in nav_paths(nav):
        checked += 1
        target = (DOCS / entry).resolve()
        try:
            target.relative_to(DOCS.resolve())
        except ValueError:
            fail(errors, f"mkdocs.yml: caminho fora de docs/: {entry}")
            continue
        if not target.is_file():
            fail(errors, f"mkdocs.yml: entrada de navegação inexistente: {entry}")
    return checked


def validate_navigation_labels(config: dict[str, Any], errors: list[str]) -> int:
    """Impede que IDs documentais virem o texto primário do menu público do GKR."""
    nav = config.get("nav")
    if nav is None:
        return 0

    checked = 0
    for label in nav_labels(nav):
        checked += 1
        if NAV_TECHNICAL_IDENTIFIER.search(label):
            fail(
                errors,
                "mkdocs.yml: rótulo de navegação expõe identificador técnico; "
                f"use título orientado por assunto e mantenha o ID dentro do conteúdo: {label}",
            )
    return checked


def main() -> int:
    errors: list[str] = []
    if not DOCS.is_dir():
        print("ERRO: diretório docs/ não encontrado", file=sys.stderr)
        return 1

    markdown_files = sorted(DOCS.rglob("*.md"))
    ids: dict[str, list[Path]] = defaultdict(list)
    front_matter_count = 0

    for path in markdown_files:
        text = read_utf8(path, errors)
        if text is None:
            continue
        metadata = parse_front_matter(path, text, errors)
        if metadata is not None:
            front_matter_count += 1
            document_id = metadata.get("id")
            if isinstance(document_id, str) and document_id.strip():
                ids[document_id.strip()].append(path)

    for document_id, paths in sorted(ids.items()):
        if len(paths) > 1:
            rendered = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            fail(errors, f"ID duplicado {document_id}: {rendered}")

    config = load_mkdocs(errors)
    nav_count = validate_navigation(config, errors) if config else 0
    nav_label_count = validate_navigation_labels(config, errors) if config else 0
    link_count = validate_markdown_links(markdown_files, errors)

    print(f"Markdown files: {len(markdown_files)}")
    print(f"Front matters parsed: {front_matter_count}")
    print(f"Unique IDs: {len(ids)}")
    print(f"Navigation entries checked: {nav_count}")
    print(f"Navigation labels checked: {nav_label_count}")
    print(f"Local links checked: {link_count}")

    if errors:
        print(f"\nVALIDATION FAILED: {len(errors)} issue(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("\nVALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
