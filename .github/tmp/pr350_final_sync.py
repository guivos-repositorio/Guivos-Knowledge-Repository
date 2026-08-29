from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    n = s.count(old)
    if n != 1:
        raise SystemExit(f"{path}: expected exactly 1 match, found {n}: {old[:100]!r}")
    p.write_text(s.replace(old, new), encoding="utf-8")


STATE = "docs/project/current-state-register.md"
README = "README.md"
INDEX = "docs/index.md"
ROADMAP = "docs/roadmap.md"

# GKR-STATE-001 detailed audit state (§26)
replace_once(
    STATE,
    "D — HOME PRINCIPAL / PESSOA\n→ REBUILD_REQUIRED\n\nE — HOME ORGANIZAÇÕES E COLETIVOS\n→ REBUILD_REQUIRED",
    "D — HOME PRINCIPAL / PESSOA\n→ DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION\n\nE — HOME ORGANIZAÇÕES E COLETIVOS\n→ REBUILD_REQUIRED / NEXT",
)

# GKR-STATE-001 next governed act (§29)
replace_once(
    STATE,
    """## 29. Próximo ato governado

O próximo lote da auditoria é a **reconstrução da Home principal/Pessoa**, confrontando o master antigo com a Fundação reconciliada, Marca, Public Canon, Journey, Research, Domínios de Evolução e demais autoridades aplicáveis.

Isso ainda não autoriza a primeira tela autenticada pós-Home.

```text
PRÓXIMO LOTE
→ D — HOME PRINCIPAL / PESSOA

AINDA BLOQUEADOS
→ UXA-102
→ PRIMEIRA TELA PÓS-HOME DA PESSOA
→ DESIGN AUTOMÁTICO
→ PRODUCT ENGINEERING
→ PMF
→ IMPLEMENTAÇÃO
```
""",
    """## 29. Próximo ato governado

O próximo lote da auditoria é **E — Home Organizações e Coletivos**, reconstruindo a autoridade pública O/C contra as autoridades posteriores aplicáveis sem antecipar a experiência autenticada.

O fechamento documental da Home principal/Pessoa não autoriza materialização visual nem a primeira tela autenticada pós-Home.

```text
PRÓXIMO LOTE
→ E — HOME ORGANIZAÇÕES E COLETIVOS
→ REBUILD_REQUIRED

AINDA BLOQUEADOS
→ UXA-102
→ PRIMEIRA TELA PÓS-HOME DA PESSOA
→ WIREFRAME / FIGMA / UI / PROTÓTIPO
→ DESIGN AUTOMÁTICO
→ PRODUCT ENGINEERING
→ PMF
→ IMPLEMENTAÇÃO
```
""",
)

# Landing pages: lower Homes tables
for path in [README, INDEX]:
    replace_once(
        path,
        "| Principal / Pessoa | `REBUILD_REQUIRED` |",
        "| Principal / Pessoa | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |",
    )

# Roadmap version/state
replace_once(ROADMAP, "id: ROADMAP-13.1.0", "id: ROADMAP-13.2.0")
replace_once(ROADMAP, "version: 13.1.0", "version: 13.2.0")
replace_once(ROADMAP, "last_updated: 2026-08-27", "last_updated: 2026-08-29")
replace_once(
    ROADMAP,
    "Este roadmap traduz `GKR-STATE-001 v3.1.0` em **frentes governadas de avanço**.",
    "Este roadmap traduz `GKR-STATE-001 v3.2.0` em **frentes governadas de avanço**.",
)
replace_once(
    ROADMAP,
    "Os Lotes A, B e C estão reconciliados nesta baseline proposta. O próximo lote governado é **D — Home principal / Pessoa**.",
    "Os Lotes A, B, C e D estão reconciliados no estado vigente. O próximo lote governado é **E — Home Organizações e Coletivos**.",
)
replace_once(ROADMAP, "| Estado global | **GKR-STATE-001 v3.1.0** |", "| Estado global | **GKR-STATE-001 v3.2.0** |")
replace_once(ROADMAP, "| Home principal/Pessoa | **REBUILD_REQUIRED / NEXT LOT** |", "| Home principal/Pessoa | **DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION** |")
replace_once(ROADMAP, "| Home Organizações e Coletivos | **REBUILD_REQUIRED** |", "| Home Organizações e Coletivos | **REBUILD_REQUIRED / NEXT LOT** |")
replace_once(
    ROADMAP,
    "D. HOME PRINCIPAL / PESSOA              [PRÓXIMO]\n↓\nE. HOME ORGANIZAÇÕES E COLETIVOS",
    "D. HOME PRINCIPAL / PESSOA              [CONCLUÍDO]\n↓\nE. HOME ORGANIZAÇÕES E COLETIVOS          [PRÓXIMO]",
)

# Replace the whole Lot D section so its explanatory content is current, not just its label.
p = Path(ROADMAP)
s = p.read_text(encoding="utf-8")
start = s.index("## 8. Lote D — Home principal / Pessoa")
end = s.index("## 9. Lote E — Home Organizações e Coletivos")
new_d = """## 8. Lote D — Home principal / Pessoa

Estado:

```text
COMPLETED
DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION
```

O Lote D foi fechado documentalmente pela sequência canônica de PRs #342–#349, preservando e reconciliando a narrativa pública da Home principal/Pessoa contra Fundação, Marca, Public Canon, Journey, Research, Domínios de Evolução e Experience Architecture.

Conflitos originalmente comprovados e absorvidos:

- `Do possível ao vivido.` deixou de operar como assinatura institucional e permanece no âmbito pessoal/autoral do fundador;
- Movimento 06 = `Da Possibilidade à Experiência`;
- `Possibilidade ≠ Oportunidade`, com Mecanismo explicitado quando necessário;
- nove Domínios de Evolução preservados como vocabulário de amplitude, sem materialização visual automática;
- participante ≠ produto e Organização ≠ Business;
- Intelligence preservada como Produto Especializado transversal / Intelligence Layer;
- fronteira pública × Journey, Header, launcher e hierarquia de CTAs reconciliados;
- prova, histórias reais, patrocínio identificável, autonomia e acessibilidade protegidos;
- briefing/handoff subordinado ao Master e às autoridades especializadas.

Movimento 06 vigente:

```text
DA POSSIBILIDADE À EXPERIÊNCIA
```

O fechamento de D é exclusivamente documental. Não autoriza wireframe, Figma, UI, protótipo, implementação, publicação, disponibilidade operacional, PMF ou primeira tela autenticada da Pessoa.

Gate preservado:

```text
HOME PRINCIPAL / PESSOA
→ DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION

MATERIALIZAÇÃO VISUAL
→ NOT AUTHORIZED

PRIMEIRA TELA AUTENTICADA DA PESSOA
→ BLOCKED UNTIL FULL AUDIT CLOSES
```

"""
p.write_text(s[:start] + new_d + s[end:], encoding="utf-8")

# Lot E is next while still rebuild-required.
replace_once(
    ROADMAP,
    "## 9. Lote E — Home Organizações e Coletivos\n\nEstado:\n\n```text\nREBUILD_REQUIRED\n```",
    "## 9. Lote E — Home Organizações e Coletivos\n\nEstado:\n\n```text\nREBUILD_REQUIRED\nNEXT_LOT\n```",
)

# Synchronize current landing-page roadmap references.
for path in [README, INDEX]:
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    n = s.count("Roadmap 13.1.0")
    if n != 2:
        raise SystemExit(f"{path}: expected exactly 2 Roadmap 13.1.0 refs, found {n}")
    p.write_text(s.replace("Roadmap 13.1.0", "Roadmap 13.2.0"), encoding="utf-8")

# Stale-state assertions.
checks = {
    STATE: [
        "D — HOME PRINCIPAL / PESSOA\n→ REBUILD_REQUIRED",
        "→ D — HOME PRINCIPAL / PESSOA\n\nAINDA BLOQUEADOS",
        "O próximo lote da auditoria é a **reconstrução da Home principal/Pessoa**",
    ],
    README: ["| Principal / Pessoa | `REBUILD_REQUIRED` |", "Roadmap 13.1.0"],
    INDEX: ["| Principal / Pessoa | `REBUILD_REQUIRED` |", "Roadmap 13.1.0"],
    ROADMAP: [
        "ROADMAP-13.1.0",
        "version: 13.1.0",
        "GKR-STATE-001 v3.1.0",
        "D. HOME PRINCIPAL / PESSOA              [PRÓXIMO]",
    ],
}
for path, needles in checks.items():
    s = Path(path).read_text(encoding="utf-8")
    for needle in needles:
        if needle in s:
            raise SystemExit(f"{path}: stale state survived: {needle!r}")

for path in [README, INDEX]:
    if Path(path).read_text(encoding="utf-8").count("Roadmap 13.2.0") != 2:
        raise SystemExit(f"{path}: Roadmap 13.2.0 references not synchronized")
