from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    count = s.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly 1 match, found {count}")
    p.write_text(s.replace(old, new), encoding="utf-8")

# P2: propagation retention must reflect the actual residual lifecycle after Lot D.
replace_once(
    "docs/project/current-state-register.md",
    "`GKR-BRAND-PUBLIC-AUTHORITY-001` também permanece preservado. O registro de propagação derivado não é removido ainda porque continua necessário para a reconstrução da Home Pessoa; sua eventual remoção depende da absorção completa no master futuro.",
    "`GKR-BRAND-PUBLIC-AUTHORITY-001` também permanece preservado. O registro de propagação derivado continua transitório e não normativo; as correções relacionadas à Home Pessoa já foram absorvidas no Lote D, e sua permanência ou remoção passa a depender exclusivamente da avaliação dos resíduos especializados sob F-010, com remoção somente após absorção completa e sem perda de conhecimento vigente."
)

replace_once(
    "docs/roadmap.md",
    "- não remover ainda a propagação de autoridade pública, pois ela continua necessária até a reconstrução da Home Pessoa.",
    "- manter a propagação de autoridade pública apenas como registro transitório dos resíduos especializados ainda sujeitos a F-010; as correções relacionadas à Home Pessoa já foram absorvidas no Lote D, e eventual remoção exige absorção completa sem perda de conhecimento vigente."
)

# P1: dedicated next-movement section must agree with Roadmap 13.2.0.
replace_once(
    "docs/roadmap.md",
    """## 26. Regra do próximo movimento

Após a integração do Lote C, o próximo movimento é **Lote D — Home principal / Pessoa**.

Até o fechamento da auditoria:

```text
NÃO HÁ UXA-102 AUTOMÁTICA
NÃO HÁ PRIMEIRA TELA PÓS-HOME AUTOMÁTICA
NÃO HÁ WIREFRAME AUTENTICADO AUTOMÁTICO
NÃO HÁ DESIGN AUTOMÁTICO
NÃO HÁ ENGINEERING AUTOMÁTICA
NÃO HÁ FILING AUTOMÁTICO
NÃO HÁ PMF AUTOMÁTICO
```

A Home Pessoa será reconstruída primeiro; a primeira tela autenticada somente será definida após os gates restantes da auditoria.""",
    """## 26. Regra do próximo movimento

Com os Lotes A, B, C e D concluídos no estado vigente, o próximo movimento é **Lote E — Home Organizações e Coletivos**.

Até o fechamento integral da auditoria:

```text
NÃO HÁ UXA-102 AUTOMÁTICA
NÃO HÁ PRIMEIRA TELA PÓS-HOME AUTOMÁTICA
NÃO HÁ WIREFRAME AUTENTICADO AUTOMÁTICO
NÃO HÁ DESIGN AUTOMÁTICO
NÃO HÁ ENGINEERING AUTOMÁTICA
NÃO HÁ FILING AUTOMÁTICO
NÃO HÁ PMF AUTOMÁTICO
```

A Home principal/Pessoa permanece `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION`. O Lote E reconstrói documentalmente a Home Organizações e Coletivos; a primeira tela autenticada somente será definida após os gates restantes e o fechamento integral da auditoria."""
)

# No stale dependency on future Person Home reconstruction may survive in these canonical surfaces.
for path in ["docs/project/current-state-register.md", "docs/roadmap.md"]:
    s = Path(path).read_text(encoding="utf-8")
    stale = [
        "continua necessário para a reconstrução da Home Pessoa",
        "continua necessária até a reconstrução da Home Pessoa",
        "A Home Pessoa será reconstruída primeiro",
        "o próximo movimento é **Lote D — Home principal / Pessoa**",
    ]
    for needle in stale:
        if needle in s:
            raise SystemExit(f"{path}: stale directive survived: {needle}")
