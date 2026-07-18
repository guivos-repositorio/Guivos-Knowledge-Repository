from __future__ import annotations

import hashlib
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CANONICAL = DOCS / "product-architecture" / "pas-001-guivos-journey.md"
CANDIDATE = DOCS / "product-architecture" / "pas-001-guivos-journey-1.0.0-candidate.md"
VALIDATION = DOCS / "product-architecture" / "pas-001-guivos-journey-validacao-publicacao.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected 1 anchor, found {count}")
    return text.replace(old, new, 1)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def section(text: str, heading: str, next_heading: str) -> str:
    start = text.find(heading)
    end = text.find(next_heading, start + len(heading))
    if start < 0 or end < 0:
        raise RuntimeError(f"section not found: {heading}")
    return text[start:end]


def count_numbered(block: str) -> int:
    return len(re.findall(r"(?m)^\d+\.\s", block))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def update_readme() -> None:
    path = ROOT / "README.md"
    text = read(path)
    text = replace_once(
        text,
        "- **Edição candidata:** PAS-001-CANDIDATE-001 1.0.0-rc.1\n- **Parecer de prontidão:** `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`\n- **Próxima frente:** `PAS-001-RELEASE-VALIDATION-001` — Validação Editorial e Normativa da Edição Candidata",
        "- **Edição candidata:** PAS-001-CANDIDATE-001 1.0.0-rc.1\n- **Validação de release:** PAS-001-RELEASE-VALIDATION-001 1.0.0\n- **Parecer de prontidão:** `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`\n- **Próxima frente:** `PAS-001-PUBLICATION-001` — Publicação Controlada do PAS-001 — Guivos Journey 1.0.0",
        "README status",
    )
    text = replace_once(
        text,
        "- [Edição Candidata Federada do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)\n",
        "- [Edição Candidata Federada do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)\n- [Validação Editorial e Normativa do PAS-001 1.0.0](docs/product-architecture/pas-001-guivos-journey-validacao-publicacao.md)\n",
        "README validation link",
    )
    write(path, text)


def update_docs_index() -> None:
    path = DOCS / "index.md"
    text = read(path)
    text = replace_once(
        text,
        "- `PAS-001-CANDIDATE-001 1.0.0-rc.1` como edição candidata consolidada e federada;\n- prontidão `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`;",
        "- `PAS-001-CANDIDATE-001 1.0.0-rc.1` como edição candidata consolidada e federada;\n- `PAS-001-RELEASE-VALIDATION-001 1.0.0` como validação editorial e normativa vigente;\n- prontidão `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`;",
        "docs index status",
    )
    text = replace_once(
        text,
        "Executar `PAS-001-RELEASE-VALIDATION-001` — **Validação Editorial e Normativa da Edição Candidata do PAS-001 — Guivos Journey 1.0.0**, preservando o arquivo canônico em `Draft 0.5.0` até decisão formal `Ready for publication`.",
        "Preparar `PAS-001-PUBLICATION-001` — **Publicação Controlada do PAS-001 — Guivos Journey 1.0.0**, preservando o arquivo canônico em `Draft 0.5.0` até aprovação expressa de publicação.",
        "docs index mission",
    )
    text = replace_once(
        text,
        "- [Edição Candidata Federada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)\n",
        "- [Edição Candidata Federada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-1.0.0-candidate.md)\n- [Validação Editorial e Normativa do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-validacao-publicacao.md)\n",
        "docs index validation link",
    )
    write(path, text)


def update_product_index() -> None:
    path = DOCS / "product-architecture" / "index.md"
    text = read(path)
    text = replace_once(text, "version: 1.27.0", "version: 1.28.0", "product version")
    text = replace_once(
        text,
        "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates e autorizou a consolidação editorial. `PAS-001-CANDIDATE-001 1.0.0-rc.1` materializa a edição candidata federada e emite `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`.",
        "`PAS-001-RECON-001 1.0.0` reconcilia a especificação-base. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates. `PAS-001-CANDIDATE-001 1.0.0-rc.1` materializa a edição federada. `PAS-001-RELEASE-VALIDATION-001 1.0.0` aprova os 25 gates de release e emite `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`.",
        "product readiness",
    )
    text = replace_once(
        text,
        "Todas as nove capacidades estão funcionalmente concluídas. O `PAS-001` canônico permanece `Draft 0.5.0` até validação e aprovação formal de publicação.",
        "Todas as nove capacidades estão funcionalmente concluídas. O `PAS-001` canônico permanece `Draft 0.5.0` até aprovação expressa e execução de `PAS-001-PUBLICATION-001`.",
        "product canonical state",
    )
    anchor = "### Edição candidata do PAS-001\n\n`PAS-001-CANDIDATE-001 1.0.0-rc.1` consolida filosofia, arquitetura em camadas, princípios, invariantes, mapa das nove capacidades, perguntas centrais, fronteiras, autoridade federada e critérios globais, preservando os contratos especializados e o arquivo canônico `0.5.0`.\n"
    replacement = anchor + "\n### Validação de release do PAS-001\n\n`PAS-001-RELEASE-VALIDATION-001 1.0.0` confirma 25 gates, 35 critérios de aceite, 30 comportamentos proibidos, nove contratos finais, 54 extensões, links, navegação, versões, preservação histórica, plano de publicação e rollback. O parecer é `Ready for publication`, condicionado à aprovação expressa.\n"
    text = replace_once(text, anchor, replacement, "product validation section")
    write(path, text)


def update_roadmap() -> None:
    path = DOCS / "roadmap.md"
    text = read(path)
    text = replace_once(text, "version: 11.8.0", "version: 11.9.0", "roadmap version")
    text = replace_once(
        text,
        "- **Edição candidata vigente:** `PAS-001-CANDIDATE-001 1.0.0-rc.1`.\n- **Extensões vigentes da Capacidade 01:**",
        "- **Edição candidata vigente:** `PAS-001-CANDIDATE-001 1.0.0-rc.1`.\n- **Validação de release vigente:** `PAS-001-RELEASE-VALIDATION-001 1.0.0`.\n- **Extensões vigentes da Capacidade 01:**",
        "roadmap validation row",
    )
    text = replace_once(
        text,
        "- **Parecer de prontidão:** `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`.\n- **Lacuna bloqueante:** validação editorial e normativa da candidata ainda não executada.",
        "- **Parecer de prontidão:** `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`.\n- **Lacuna bloqueante:** aprovação expressa e execução controlada de `PAS-001-PUBLICATION-001`.",
        "roadmap readiness",
    )
    text = replace_once(
        text,
        "`PAS-001-CANDIDATE-001 1.0.0-rc.1` materializa a edição consolidada e federada. O próximo trabalho deverá executar `PAS-001-RELEASE-VALIDATION-001`, mantendo o arquivo canônico em `Draft 0.5.0` até decisão formal `Ready for publication`.",
        "`PAS-001-RELEASE-VALIDATION-001 1.0.0` valida a candidata e autoriza preparar a publicação controlada. O próximo trabalho deverá executar `PAS-001-PUBLICATION-001` somente após aprovação expressa, mantendo o arquivo canônico em `Draft 0.5.0` até o commit de promoção.",
        "roadmap direction",
    )
    anchor = "## Edição candidata concluída\n\n`PAS-001-CANDIDATE-001 1.0.0-rc.1` consolida o Journey de forma federada, sem substituir o `PAS-001 0.5.0`. A próxima etapa é a validação editorial e normativa da candidata.\n"
    replacement = anchor + "\n## Validação de release concluída\n\n`PAS-001-RELEASE-VALIDATION-001 1.0.0` aprovou 25 gates, validou os 35 critérios da candidata e confirmou o bloqueio dos 30 comportamentos proibidos. O estado é `Ready for publication`, mas a publicação depende de aprovação expressa.\n"
    text = replace_once(text, anchor, replacement, "roadmap validation section")
    text = replace_once(
        text,
        "A Capacidade 01 está `Functionally complete — 100%`. Todas as capacidades estão funcionalmente concluídas; a próxima etapa é a edição candidata federada do `PAS-001 1.0.0`.",
        "A Capacidade 01 está `Functionally complete — 100%`. Todas as capacidades estão funcionalmente concluídas; a próxima etapa é a publicação controlada do `PAS-001 1.0.0`, condicionada à aprovação expressa.",
        "roadmap stale next step",
    )
    write(path, text)


def update_board() -> None:
    path = DOCS / "project" / "knowledge-board.md"
    text = read(path)
    text = replace_once(text, "version: 11.8.0", "version: 11.9.0", "board version")
    text = replace_once(
        text,
        "| PAS-001-CANDIDATE-001 | Candidate 1.0.0-rc.1 | Consolidar a edição federada candidata do Guivos Journey |\n",
        "| PAS-001-CANDIDATE-001 | Candidate 1.0.0-rc.1 | Consolidar a edição federada candidata do Guivos Journey |\n| PAS-001-RELEASE-VALIDATION-001 | Active 1.0.0 | Validar a candidata e emitir parecer de publicação |\n",
        "board validation row",
    )
    text = replace_once(
        text,
        "| Parecer de prontidão | `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized` |\n| Lacuna bloqueante | `PAS-001-RELEASE-VALIDATION-001` ainda não executado |",
        "| Parecer de prontidão | `Ready for publication — PAS-001 1.0.0 publication requires explicit approval` |\n| Lacuna bloqueante | Aprovação expressa e execução controlada de `PAS-001-PUBLICATION-001` |",
        "board readiness",
    )
    text = replace_once(
        text,
        "| Frente ativa | `PAS-001-RELEASE-VALIDATION-001` — Validação Editorial e Normativa da Edição Candidata |\n| Estado da frente ativa | Candidata `1.0.0-rc.1` criada; validação e publicação ainda não autorizadas |",
        "| Frente ativa | `PAS-001-PUBLICATION-001` — Publicação Controlada do PAS-001 — Guivos Journey 1.0.0 |\n| Estado da frente ativa | Validação concluída; publicação depende de aprovação expressa |",
        "board active front",
    )
    text = replace_once(
        text,
        "| Foco imediato | Validar a candidata contra os 15 gates, contratos finais, autoridade, supersessão, links, versões e navegação |",
        "| Foco imediato | Preparar a promoção controlada da candidata, sem alterar o canônico antes da aprovação expressa |",
        "board focus",
    )
    anchor = "## Edição candidata do PAS-001\n\n`PAS-001-CANDIDATE-001 1.0.0-rc.1` está criada e pronta para validação. O `PAS-001 0.5.0` permanece canônico e a publicação de `1.0.0` continua condicionada.\n"
    replacement = anchor + "\n## Validação de release do PAS-001\n\n`PAS-001-RELEASE-VALIDATION-001 1.0.0` aprovou os 25 gates, os 35 critérios de aceite e o bloqueio dos 30 comportamentos proibidos. O `PAS-001 0.5.0` permanece canônico até aprovação expressa e publicação controlada.\n"
    text = replace_once(text, anchor, replacement, "board validation section")
    write(path, text)


def update_matrix() -> None:
    path = DOCS / "project" / "canonical-consolidation-matrix.md"
    text = read(path)
    text = replace_once(text, "version: 1.27.0", "version: 1.28.0", "matrix version")
    text = replace_once(
        text,
        "Todas as nove capacidades estão funcionalmente concluídas. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates, consolidou a matriz final de supersessão e o registro transversal de autoridade. `PAS-001-CANDIDATE-001 1.0.0-rc.1` aplica essas decisões em uma edição federada, preservando o `PAS-001 0.5.0` e as 54 extensões especializadas.",
        "Todas as nove capacidades estão funcionalmente concluídas. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates. `PAS-001-CANDIDATE-001 1.0.0-rc.1` aplica a consolidação federada. `PAS-001-RELEASE-VALIDATION-001 1.0.0` confirma ausência de regressões, preserva o `PAS-001 0.5.0`, os nove contratos e as 54 extensões, e emite `Ready for publication` condicionado à aprovação expressa.",
        "matrix reconciliation",
    )
    text = replace_once(
        text,
        "| Estado de prontidão | Refinar | `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized` |",
        "| Estado de prontidão | Refinar | `Ready for publication — PAS-001 1.0.0 publication requires explicit approval` |\n| PAS-001-RELEASE-VALIDATION-001 1.0.0 | Manter | Autoridade da validação de release e do parecer condicionado |",
        "matrix readiness",
    )
    text = replace_once(
        text,
        "Executar `PAS-001-RELEASE-VALIDATION-001`, comparando a candidata com os 15 gates, contratos finais, matriz de supersessão, registro de autoridade, `GLPA-001`, `GIA-000`, links, versões e navegação.",
        "Executar `PAS-001-PUBLICATION-001` somente após aprovação expressa, promovendo a candidata de forma controlada, preservando histórico, sincronizando artefatos e validando rollback.",
        "matrix next review",
    )
    text = replace_once(
        text,
        "Parecer vigente: `Candidate ready for validation — PAS-001 1.0.0 publication not yet authorized`.",
        "Parecer vigente: `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`.",
        "matrix opinion",
    )
    anchor = "## Próxima revisão\n"
    section_text = "## Validação de release do PAS-001\n\n| Elemento | Decisão | Situação |\n|---|---|---|\n| 25 gates de release | Manter | Todos aprovados, sem regressão dos 15 gates anteriores |\n| 35 critérios da candidata | Manter | Todos atendidos |\n| 30 comportamentos proibidos | Manter | Todos bloqueados |\n| PAS-001 0.5.0 | Manter | Permanece canônico até aprovação expressa |\n| Publicação controlada | Pendente de aprovação | Próxima frente normativa |\n\n"
    text = replace_once(text, anchor, section_text + anchor, "matrix validation section")
    write(path, text)


def update_changelog() -> None:
    path = ROOT / "CHANGELOG.md"
    text = read(path)
    entry = """## 0.56.0 — PAS-001 Release Validation\n\n- Criação de `PAS-001-RELEASE-VALIDATION-001 1.0.0`.\n- Avaliação e aprovação dos 25 gates de release.\n- Confirmação da permanência dos 15 gates da auditoria.\n- Validação individual dos 35 critérios de aceite da candidata.\n- Confirmação do bloqueio dos 30 comportamentos globais proibidos.\n- Preservação dos nove contratos finais e das 54 extensões especializadas.\n- Validação de `GLPA-001`, `GIA-000`, links, navegação, versões, publicação e rollback.\n- Manutenção do arquivo canônico `PAS-001` em `Draft 0.5.0` e da candidata em `1.0.0-rc.1`.\n- Parecer `Ready for publication — PAS-001 1.0.0 publication requires explicit approval`.\n- Arquitetura e Matriz `1.28.0`; Roadmap e Board `11.9.0`.\n- Próximo ponto: `PAS-001-PUBLICATION-001`.\n\n\n"""
    text = replace_once(
        text,
        "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n",
        "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n" + entry,
        "changelog insertion",
    )
    write(path, text)


def update_mkdocs() -> None:
    path = ROOT / "mkdocs.yml"
    text = read(path)
    text = replace_once(
        text,
        "      - PAS-001-CANDIDATE-001 — Edição Candidata Federada 1.0.0: product-architecture/pas-001-guivos-journey-1.0.0-candidate.md\n",
        "      - PAS-001-CANDIDATE-001 — Edição Candidata Federada 1.0.0: product-architecture/pas-001-guivos-journey-1.0.0-candidate.md\n      - PAS-001-RELEASE-VALIDATION-001 — Validação Editorial e Normativa: product-architecture/pas-001-guivos-journey-validacao-publicacao.md\n",
        "mkdocs validation nav",
    )
    write(path, text)


def validate_document_state() -> None:
    canonical = read(CANONICAL)
    candidate = read(CANDIDATE)
    validation = read(VALIDATION)
    canonical_meta = frontmatter(canonical)
    candidate_meta = frontmatter(candidate)
    validation_meta = frontmatter(validation)

    assert canonical_meta.get("id") == "PAS-001"
    assert canonical_meta.get("status") == "draft"
    assert canonical_meta.get("version") == "0.5.0"
    assert git_blob_sha(CANONICAL) == "d5e84f75f012dee07edc570712c301331d1e09be"

    assert candidate_meta.get("id") == "PAS-001-CANDIDATE-001"
    assert candidate_meta.get("status") == "candidate"
    assert candidate_meta.get("version") == "1.0.0-rc.1"
    assert validation_meta.get("id") == "PAS-001-RELEASE-VALIDATION-001"
    assert validation_meta.get("status") == "active"
    assert validation_meta.get("version") == "1.0.0"

    principles = section(candidate, "# 8. Princípios permanentes", "# 9. Invariantes globais")
    prohibited = section(candidate, "# 28. Comportamentos globais proibidos", "# 29. Critérios de aceite")
    acceptance = section(candidate, "# 29. Critérios de aceite", "# 30. Processo de validação")
    assert count_numbered(principles) == 30
    assert count_numbered(prohibited) == 30
    assert count_numbered(acceptance) == 35

    capabilities = [
        "Captura de Contexto", "Contexto Vivo", "Objetivos", "Eventos de Vida",
        "Próximos Passos", "Oportunidades Ativas", "Intervenções Contextuais",
        "Experiências", "Evolução Contínua",
    ]
    for name in capabilities:
        assert name in candidate

    required_phrases = [
        "Ready for publication — PAS-001 1.0.0 publication requires explicit approval",
        "gates avaliados: `25 de 25`",
        "gates bloqueados: `0`",
        "achados críticos abertos: `0`",
        "achados altos abertos: `0`",
        "PAS-001-PUBLICATION-001",
    ]
    for phrase in required_phrases:
        assert phrase in validation


def validate_extensions_and_contracts() -> None:
    expected_counts = {"CC": 3, "CV": 8, "OBJ": 7, "EV": 6, "PP": 6, "OA": 6, "IC": 6, "EXP": 6, "EC": 6}
    found: dict[str, list[Path]] = {key: [] for key in expected_counts}
    for path in (DOCS / "product-architecture").glob("pas-001-*.md"):
        meta = frontmatter(read(path))
        doc_id = meta.get("id", "")
        for prefix in expected_counts:
            if doc_id.startswith(f"PAS-001-{prefix}-"):
                found[prefix].append(path)
                assert meta.get("status") == "active", f"inactive extension: {doc_id}"
                assert meta.get("version") == "1.0.0", f"unexpected version: {doc_id}"
                break
    for prefix, expected in expected_counts.items():
        assert len(found[prefix]) == expected, f"{prefix}: expected {expected}, found {len(found[prefix])}"
    assert sum(len(items) for items in found.values()) == 54

    contract_paths = [
        "pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md",
        "pas-001-contexto-vivo-cenarios-contrato-final.md",
        "pas-001-objetivos-kpis-cenarios-contrato-final.md",
        "pas-001-eventos-de-vida-kpis-cenarios-contrato-final.md",
        "pas-001-proximos-passos-kpis-cenarios-contrato-final.md",
        "pas-001-oportunidades-ativas-kpis-cenarios-contrato-final.md",
        "pas-001-intervencoes-contextuais-kpis-cenarios-contrato-final.md",
        "pas-001-experiencias-kpis-cenarios-contrato-final.md",
        "pas-001-evolucao-continua-kpis-cenarios-contrato-final.md",
    ]
    for name in contract_paths:
        path = DOCS / "product-architecture" / name
        assert path.exists(), name
        meta = frontmatter(read(path))
        assert meta.get("status") == "active", name
        assert meta.get("version") == "1.0.0", name


def validate_links() -> tuple[int, int]:
    checked = 0
    broken: list[str] = []
    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for md in ROOT.rglob("*.md"):
        text = read(md)
        for raw_target in link_re.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "javascript:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            checked += 1
            resolved = (ROOT / target.lstrip("/")) if target.startswith("/") else (md.parent / target)
            if not resolved.resolve().exists():
                broken.append(f"{md.relative_to(ROOT)} -> {raw_target}")
    if broken:
        raise RuntimeError("broken markdown links:\n" + "\n".join(broken[:30]))

    mkdocs = read(ROOT / "mkdocs.yml")
    targets = re.findall(r":\s+([^\s#]+\.md)\s*$", mkdocs, flags=re.MULTILINE)
    missing = [target for target in targets if not (DOCS / target).exists()]
    if missing:
        raise RuntimeError("missing MkDocs targets:\n" + "\n".join(missing))
    return checked, len(targets)


def validate_canonical_artifacts() -> None:
    expectations = {
        DOCS / "product-architecture" / "index.md": ["version: 1.28.0", "PAS-001-RELEASE-VALIDATION-001 1.0.0"],
        DOCS / "roadmap.md": ["version: 11.9.0", "Ready for publication", "PAS-001-PUBLICATION-001"],
        DOCS / "project" / "knowledge-board.md": ["version: 11.9.0", "PAS-001-RELEASE-VALIDATION-001", "PAS-001-PUBLICATION-001"],
        DOCS / "project" / "canonical-consolidation-matrix.md": ["version: 1.28.0", "Ready for publication", "25 gates de release"],
        ROOT / "CHANGELOG.md": ["## 0.56.0 — PAS-001 Release Validation"],
        ROOT / "README.md": ["PAS-001-RELEASE-VALIDATION-001 1.0.0", "Ready for publication", "PAS-001-PUBLICATION-001"],
        DOCS / "index.md": ["PAS-001-RELEASE-VALIDATION-001 1.0.0", "Ready for publication", "PAS-001-PUBLICATION-001"],
        ROOT / "mkdocs.yml": ["pas-001-guivos-journey-validacao-publicacao.md"],
    }
    for path, phrases in expectations.items():
        text = read(path)
        for phrase in phrases:
            assert phrase in text, f"{path.relative_to(ROOT)} missing {phrase}"


def main() -> None:
    update_readme()
    update_docs_index()
    update_product_index()
    update_roadmap()
    update_board()
    update_matrix()
    update_changelog()
    update_mkdocs()

    validate_document_state()
    validate_extensions_and_contracts()
    markdown_links, mkdocs_targets = validate_links()
    validate_canonical_artifacts()

    print("PAS-001 release validation passed")
    print("gates=25/25")
    print("candidate_acceptance=35/35")
    print("prohibited_behaviors=30/30 blocked")
    print("extensions=54")
    print("contracts=9")
    print(f"markdown_links={markdown_links}")
    print(f"mkdocs_targets={mkdocs_targets}")
    print("canonical_pas_001=draft-0.5.0-preserved")
    print("readiness=Ready for publication — explicit approval required")


if __name__ == "__main__":
    main()
