from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PAS_BLOB = "15871a071d00d409d68fd043c02d236307a2b4c7"
MAP_PATH = ROOT / "docs/product-architecture/pas-001-guivos-journey-mapa-final-capacidades.md"
PAS_PATH = ROOT / "docs/product-architecture/pas-001-guivos-journey.md"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def replace_once(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"{path}: expected one anchor, found {text.count(old)}: {old[:80]!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


def validate_map() -> None:
    text = MAP_PATH.read_text(encoding="utf-8")
    required = [
        "id: PAS-001-CAPABILITY-MAP-001",
        "status: active",
        "version: 1.0.0",
        "# 5023. Visão executiva",
        "# 5024. Mapa visual",
        "# 5025. Perguntas centrais",
        "# 5027. Fronteiras decisórias",
        "PAS-001-ENGINEERING-HANDOFF-001",
    ]
    for item in required:
        if item not in text:
            raise RuntimeError(f"capability map missing {item}")
    for number in range(1, 10):
        token = f"| {number:02d} |"
        if text.count(token) != 1:
            raise RuntimeError(f"capability map row count invalid for {token}")
    contracts = [
        "PAS-001-CC-CONTRACT-001",
        "PAS-001-CV-CONTRACT-001",
        "PAS-001-OBJ-CONTRACT-001",
        "PAS-001-EV-CONTRACT-001",
        "PAS-001-PP-CONTRACT-001",
        "PAS-001-OA-CONTRACT-001",
        "PAS-001-IC-CONTRACT-001",
        "PAS-001-EXP-CONTRACT-001",
        "PAS-001-EC-CONTRACT-001",
    ]
    for contract in contracts:
        if text.count(contract) < 2:
            raise RuntimeError(f"capability map missing contract references: {contract}")
    if text.count("Functionally complete") < 9:
        raise RuntimeError("capability map does not preserve nine completed states")


def update_changelog() -> None:
    anchor = "Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n"
    block = """Todas as alterações relevantes do Guivos Knowledge Repository são registradas neste arquivo.\n\n\n## 0.58.0 — PAS-001 Final Capability Map\n\n- Criação de `PAS-001-CAPABILITY-MAP-001 1.0.0`.\n- Consolidação executiva e navegável das nove capacidades do Guivos Journey.\n- Preservação das nove perguntas centrais, responsabilidades, fronteiras e contratos finais.\n- Referência às 54 extensões normativas como autoridades especializadas.\n- Inclusão de mapa Mermaid, matrizes de entradas, saídas e fronteiras decisórias.\n- Arquitetura e Matriz `1.30.0`; Roadmap e Board `11.11.0`.\n- Próximo ponto: `PAS-001-ENGINEERING-HANDOFF-001`.\n- `PAS-001 1.0.0`, contratos e extensões permaneceram inalterados.\n\n\n"""
    replace_once("CHANGELOG.md", anchor, block)


def update_roadmap() -> None:
    replace_once("docs/roadmap.md", "version: 11.10.0", "version: 11.11.0")
    replace_once(
        "docs/roadmap.md",
        "- **Validação de release vigente:** `PAS-001-RELEASE-VALIDATION-001 1.0.0`.\n",
        "- **Validação de release vigente:** `PAS-001-RELEASE-VALIDATION-001 1.0.0`.\n- **Mapa final vigente:** `PAS-001-CAPABILITY-MAP-001 1.0.0`.\n",
    )
    replace_once(
        "docs/roadmap.md",
        "`PAS-001-PUBLICATION-001 1.0.0` promoveu a candidata validada para `PAS-001 1.0.0 active`. O próximo trabalho é `PAS-001-CAPABILITY-MAP-001`, mantendo contratos e extensões como autoridades especializadas.",
        "`PAS-001-CAPABILITY-MAP-001 1.0.0` consolidou a visão executiva e navegável das nove capacidades. O próximo trabalho é `PAS-001-ENGINEERING-HANDOFF-001`, mantendo `PAS-001`, contratos e extensões como autoridades normativas.",
    )
    replace_once(
        "docs/roadmap.md",
        "## Capacidade 01 — Fechamento formal concluído\n",
        "## Mapa Final de Capacidades concluído\n\n`PAS-001-CAPABILITY-MAP-001 1.0.0` consolida perguntas, responsabilidades, entradas, saídas, fronteiras, relações não lineares, contratos e critérios de reabertura das nove capacidades. A lacuna de mapa executivo está encerrada.\n\n## Capacidade 01 — Fechamento formal concluído\n",
    )
    replace_once(
        "docs/roadmap.md",
        "Todas as capacidades estão funcionalmente concluídas; o `PAS-001 1.0.0` está publicado; a próxima etapa é o Mapa Final de Capacidades.",
        "Todas as capacidades estão funcionalmente concluídas; o `PAS-001 1.0.0` e o Mapa Final estão ativos; a próxima etapa é o Handoff Arquitetural para Product Engineering.",
    )


def update_board() -> None:
    replace_once("docs/project/knowledge-board.md", "version: 11.10.0", "version: 11.11.0")
    replace_once(
        "docs/project/knowledge-board.md",
        "| PAS-001-PUBLICATION-001 | Active 1.0.0 | Registrar a publicação controlada do PAS-001 1.0.0 |\n",
        "| PAS-001-PUBLICATION-001 | Active 1.0.0 | Registrar a publicação controlada do PAS-001 1.0.0 |\n| PAS-001-CAPABILITY-MAP-001 | Active 1.0.0 | Consolidar a visão executiva e navegável das nove capacidades |\n",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| Frente ativa | `PAS-001-CAPABILITY-MAP-001` — Mapa Final de Capacidades do Guivos Journey |\n| Estado da frente ativa | Publicação concluída; mapa executivo e navegável pendente |",
        "| Frente ativa | `PAS-001-ENGINEERING-HANDOFF-001` — Handoff Arquitetural do Guivos Journey para Product Engineering |\n| Estado da frente ativa | Mapa final concluído; planejamento técnico por capacidade pendente |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "| Foco imediato | Consolidar o Mapa Final de Capacidades a partir do PAS-001 1.0.0 publicado |",
        "| Foco imediato | Transformar a arquitetura funcional publicada em plano de engenharia por capacidade |",
    )
    replace_once(
        "docs/project/knowledge-board.md",
        "## Capacidades do Journey\n",
        "## Mapa Final de Capacidades\n\n`PAS-001-CAPABILITY-MAP-001 1.0.0` está ativo, consolida as nove capacidades em visão executiva e navegável e define `PAS-001-ENGINEERING-HANDOFF-001` como próxima frente.\n\n## Capacidades do Journey\n",
    )


def update_product_architecture() -> None:
    replace_once("docs/product-architecture/index.md", "version: 1.29.0", "version: 1.30.0")
    replace_once(
        "docs/product-architecture/index.md",
        "### Capacidade 01 — Captura de Contexto\n",
        "### Mapa Final de Capacidades\n\n`PAS-001-CAPABILITY-MAP-001 1.0.0` apresenta as nove capacidades, perguntas centrais, responsabilidades, entradas, saídas, fronteiras, relações não lineares, contratos e critérios de reabertura. O próximo ponto é `PAS-001-ENGINEERING-HANDOFF-001`.\n\n### Capacidade 01 — Captura de Contexto\n",
    )


def update_readme() -> None:
    replace_once(
        "README.md",
        "- **Estado canônico:** `Published — PAS-001 1.0.0 active`\n- **Próxima frente:** `PAS-001-CAPABILITY-MAP-001` — Mapa Final de Capacidades do Guivos Journey",
        "- **Estado canônico:** `Published — PAS-001 1.0.0 active`\n- **Mapa final:** `PAS-001-CAPABILITY-MAP-001 1.0.0` — ativo\n- **Próxima frente:** `PAS-001-ENGINEERING-HANDOFF-001` — Handoff Arquitetural para Product Engineering",
    )
    replace_once(
        "README.md",
        "- [Publicação Controlada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-publicacao-controlada.md)\n",
        "- [Publicação Controlada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-publicacao-controlada.md)\n- [Mapa Final de Capacidades do Guivos Journey](product-architecture/pas-001-guivos-journey-mapa-final-capacidades.md)\n",
    )


def update_home() -> None:
    replace_once(
        "docs/index.md",
        "- `PAS-001-PUBLICATION-001 1.0.0` como registro de publicação controlada;\n",
        "- `PAS-001-PUBLICATION-001 1.0.0` como registro de publicação controlada;\n- `PAS-001-CAPABILITY-MAP-001 1.0.0` como mapa executivo e navegável vigente;\n",
    )
    replace_once(
        "docs/index.md",
        "Executar `PAS-001-CAPABILITY-MAP-001` — **Mapa Final de Capacidades do Guivos Journey**, utilizando o `PAS-001 1.0.0` publicado e seus contratos especializados.",
        "Executar `PAS-001-ENGINEERING-HANDOFF-001` — **Handoff Arquitetural do Guivos Journey para Product Engineering**, utilizando o `PAS-001 1.0.0`, o Mapa Final e os contratos especializados.",
    )
    replace_once(
        "docs/index.md",
        "- [Publicação Controlada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-publicacao-controlada.md)\n",
        "- [Publicação Controlada do PAS-001 1.0.0](product-architecture/pas-001-guivos-journey-publicacao-controlada.md)\n- [Mapa Final de Capacidades do Guivos Journey](product-architecture/pas-001-guivos-journey-mapa-final-capacidades.md)\n",
    )


def update_matrix() -> None:
    replace_once("docs/project/canonical-consolidation-matrix.md", "version: 1.29.0", "version: 1.30.0")
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "Todas as nove capacidades estão funcionalmente concluídas. `PAS-001-AUDIT-001 1.0.0` aprovou os 15 gates. `PAS-001-CANDIDATE-001 1.0.0-rc.1` consolidou a edição federada e agora é histórica. `PAS-001-RELEASE-VALIDATION-001 1.0.0` confirmou ausência de regressões. `PAS-001-PUBLICATION-001 1.0.0` promoveu a edição validada para `PAS-001 1.0.0 active`, preservando os nove contratos e as 54 extensões.",
        "Todas as nove capacidades estão funcionalmente concluídas. `PAS-001 1.0.0` está ativo. `PAS-001-CAPABILITY-MAP-001 1.0.0` consolida a visão executiva e navegável, preservando os nove contratos, as 54 extensões e a autoridade federada.",
    )
    replace_once(
        "docs/project/canonical-consolidation-matrix.md",
        "Executar `PAS-001-CAPABILITY-MAP-001`, produzindo o Mapa Final de Capacidades do Guivos Journey a partir do `PAS-001 1.0.0` publicado e de seus contratos especializados.",
        "Executar `PAS-001-ENGINEERING-HANDOFF-001`, transformando a arquitetura funcional publicada e o Mapa Final em planejamento técnico por capacidade.",
    )
    append = """

## PAS-001 — Mapa Final de Capacidades 1.0.0

| Objeto | Decisão | Autoridade vigente | Situação |
|---|---|---|---|
| PAS-001-CAPABILITY-MAP-001 | Maintain | PAS-001 1.0.0 e nove contratos finais | Active 1.0.0 |
| Nove capacidades | Maintain | PAS-001 e contratos `*-CONTRACT-001` | Functionally complete |
| Perguntas e responsabilidades | Maintain | PAS-001 1.0.0 | Consolidadas no mapa |
| Entradas, saídas e fronteiras | Refine | Mapa e contratos especializados | Visão executiva não linear |
| Extensões normativas | Maintain | 54 documentos vigentes | Autoridades detalhadas |
| Intelligence, Service e Platform Layers | Maintain | GLPA-001, GIA-000 e PAS-001 | Fronteiras preservadas |
| Próximo ponto | Refine | Roadmap e Knowledge Board | PAS-001-ENGINEERING-HANDOFF-001 |
"""
    p = ROOT / "docs/project/canonical-consolidation-matrix.md"
    text = p.read_text(encoding="utf-8")
    if "## PAS-001 — Mapa Final de Capacidades 1.0.0" in text:
        raise RuntimeError("matrix capability map section already exists")
    p.write_text(text.rstrip() + append + "\n", encoding="utf-8")


def update_nav() -> None:
    replace_once(
        "mkdocs.yml",
        "      - PAS-001-PUBLICATION-001 — Publicação Controlada 1.0.0: product-architecture/pas-001-guivos-journey-publicacao-controlada.md\n",
        "      - PAS-001-PUBLICATION-001 — Publicação Controlada 1.0.0: product-architecture/pas-001-guivos-journey-publicacao-controlada.md\n      - PAS-001-CAPABILITY-MAP-001 — Mapa Final de Capacidades: product-architecture/pas-001-guivos-journey-mapa-final-capacidades.md\n",
    )


def validate_final() -> None:
    if git_blob_sha(PAS_PATH) != EXPECTED_PAS_BLOB:
        raise RuntimeError("PAS-001 1.0.0 changed during capability map synchronization")
    checks = {
        "CHANGELOG.md": ["## 0.58.0 — PAS-001 Final Capability Map", "PAS-001-ENGINEERING-HANDOFF-001"],
        "docs/roadmap.md": ["version: 11.11.0", "Mapa final vigente", "PAS-001-ENGINEERING-HANDOFF-001"],
        "docs/project/knowledge-board.md": ["version: 11.11.0", "PAS-001-CAPABILITY-MAP-001 | Active 1.0.0", "PAS-001-ENGINEERING-HANDOFF-001"],
        "docs/product-architecture/index.md": ["version: 1.30.0", "### Mapa Final de Capacidades"],
        "docs/project/canonical-consolidation-matrix.md": ["version: 1.30.0", "## PAS-001 — Mapa Final de Capacidades 1.0.0"],
        "README.md": ["Mapa Final de Capacidades do Guivos Journey", "PAS-001-ENGINEERING-HANDOFF-001"],
        "docs/index.md": ["PAS-001-CAPABILITY-MAP-001 1.0.0", "PAS-001-ENGINEERING-HANDOFF-001"],
        "mkdocs.yml": ["PAS-001-CAPABILITY-MAP-001 — Mapa Final de Capacidades"],
    }
    for path, tokens in checks.items():
        text = (ROOT / path).read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                raise RuntimeError(f"{path} missing {token}")
    for path in [ROOT / "README.md", ROOT / "docs/index.md", ROOT / "docs/product-architecture/index.md", MAP_PATH]:
        text = path.read_text(encoding="utf-8")
        if "pas-001-guivos-journey-mapa-final-capacidades.md" not in text and path != MAP_PATH:
            if path.name in {"README.md", "index.md"}:
                raise RuntimeError(f"{path} missing capability map link")
    nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    if nav.count("pas-001-guivos-journey-mapa-final-capacidades.md") != 1:
        raise RuntimeError("mkdocs capability map target count invalid")


def main() -> None:
    if git_blob_sha(PAS_PATH) != EXPECTED_PAS_BLOB:
        raise RuntimeError("unexpected PAS-001 baseline blob")
    validate_map()
    update_changelog()
    update_roadmap()
    update_board()
    update_product_architecture()
    update_readme()
    update_home()
    update_matrix()
    update_nav()
    validate_final()
    print("PAS-001 capability map synchronization validated")
    print(f"PAS-001 blob preserved: {git_blob_sha(PAS_PATH)}")


if __name__ == "__main__":
    main()
