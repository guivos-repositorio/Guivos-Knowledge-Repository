#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_exact(rel, old, new, expected=1):
    p = ROOT / rel
    text = p.read_text(encoding="utf-8")
    found = text.count(old)
    if found != expected:
        raise SystemExit(f"{rel}: expected {expected} occurrence(s), found {found}: {old[:120]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")
    print(f"UPDATED {rel}: {found} replacement(s)")


# 1) Normative current state: F-010 already adjudicated the transitional propagation.
replace_exact(
    "docs/project/current-state-register.md",
    "`GKR-BRAND-PUBLIC-AUTHORITY-001` também permanece preservado. O registro de propagação derivado continua transitório e não normativo; as correções relacionadas à Home Pessoa já foram absorvidas no Lote D, e sua permanência ou remoção passa a depender exclusivamente da avaliação dos resíduos especializados sob F-010, com remoção somente após absorção completa e sem perda de conhecimento vigente.",
    "`GKR-BRAND-PUBLIC-AUTHORITY-001` também permanece preservado. `GKR-BRAND-PUBLIC-AUTHORITY-PROPAGATION-001` foi adjudicado no fechamento de `F-010` como `KEEP TEMPORARILY`: continua transitório, não normativo e parcialmente absorvido, preservando rastreabilidade enquanto seus próprios gates de absorção permanecem aplicáveis. A decisão sob `F-010` está encerrada; eventual remoção futura depende exclusivamente dos critérios internos de `REMOVE_AFTER_ABSORPTION` da própria propagation, sem perda de conhecimento vigente.",
)

# 2) Roadmap: synchronize State v3.12 and F-016 closure without releasing downstream blocks.
replace_exact(
    "docs/roadmap.md",
    "Este roadmap traduz `GKR-STATE-001 v3.11.0` em **frentes governadas de avanço**.",
    "Este roadmap traduz `GKR-STATE-001 v3.12.0` em **frentes governadas de avanço**.",
)
replace_exact(
    "docs/roadmap.md",
    "Os Lotes A–F estão reconciliados. O Bloco G está concluído no limite documental; H/I estão auditados/remediados com `F-006 RESOLVED` e `F-007 RESOLVED`. `F-016` é o eixo prioritário corrente.",
    "Os Lotes A–F estão reconciliados. O Bloco G está concluído no limite documental; H/I estão auditados/remediados com `F-006 RESOLVED` e `F-007 RESOLVED`. `F-016` também está `RESOLVED` após auditoria, adjudicação, cleanup documental 26/26, reconciliação estrutural e prova pós-delete. Esse fechamento não libera automaticamente J/K/L/M/N.",
)
replace_exact(
    "docs/roadmap.md",
    "| Estado global | **GKR-STATE-001 v3.11.0** |",
    "| Estado global | **GKR-STATE-001 v3.12.0** |",
)
replace_exact(
    "docs/roadmap.md",
    "| F-016 | **OPEN — REPO-WIDE DOCUMENTATION DEMATERIALIZATION** |",
    "| F-016 | **RESOLVED — AUDIT + ADJUDICATION + CLEANUP 26/26 + POST-DELETE PROOF COMPLETE** |",
)
replace_exact(
    "docs/roadmap.md",
    "F-016 DESMATERIALIZAÇÃO DOCUMENTAL       [OPEN / NEXT PRIORITY]\n↓\nAUDITAR WIREFRAMES / MATERIALIZATIONS / GALLERIES / MENU / SVGs [PENDING]\n↓\nABSORVER CONTEÚDO FUNCIONAL ÚNICO + REMOVER/REESCREVER MATERIALIZAÇÕES INDEVIDAS [PENDING]",
    "F-016 DESMATERIALIZAÇÃO DOCUMENTAL       [RESOLVED / 26/26 LEGACY PRODUCERS REMOVED]\n↓\nDECISÃO GOVERNADA SOBRE J/K/L/M/N         [NOT RELEASED AUTOMATICALLY]",
)
replace_exact(
    "docs/roadmap.md",
    "- manter a propagação de autoridade pública apenas como registro transitório dos resíduos especializados ainda sujeitos a F-010; as correções relacionadas à Home Pessoa já foram absorvidas no Lote D, e eventual remoção exige absorção completa sem perda de conhecimento vigente.",
    "- manter `GKR-BRAND-PUBLIC-AUTHORITY-PROPAGATION-001` conforme a adjudicação já concluída em F-010: `KEEP TEMPORARILY`, transitória, não normativa e parcialmente absorvida; eventual remoção futura continua sujeita aos próprios critérios de `REMOVE_AFTER_ABSORPTION`, sem perda de conhecimento vigente.",
)
replace_exact(
    "docs/roadmap.md",
    "F-016 → OPEN\nF-016-A → RESOLVED",
    "F-016 → RESOLVED\nF-016-A → RESOLVED",
)
replace_exact(
    "docs/roadmap.md",
    "As famílias Markdown de materialização permanecem sob F-016 e devem ser classificadas individualmente antes de qualquer remoção ou reescrita.",
    "As famílias Markdown adjudicadas sob F-016 foram classificadas individualmente; o cleanup governado removeu os 26 produtores legados elegíveis após absorção, preservando autoridades, validadores e evidências correntes. Histórico e proveniência permanecem no Git.",
)
replace_exact(
    "docs/roadmap.md",
    "`F-016-A` está `RESOLVED`.\n\n```text\nF-016-A\n→ PHYSICAL CLEANUP APPLIED 119/119\n→ PHYSICAL SVG COUNT = 0\n→ SEMANTIC #832 SUCCESS\n→ MECHANICAL #1090 SUCCESS\n→ INDEPENDENT READ-ONLY PROOF V2 SUCCESS\n→ RESOLVED\n\nNEXT F-016 SUBFRONT\n→ CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES\n→ KEEP_FUNCTIONAL | REWRITE_FUNCTIONAL | REMOVE_AFTER_ABSORPTION | REMOVE | HISTORICAL_PROVENANCE_ONLY\n→ NO AUTOMATIC MARKDOWN DELETION\n```",
    "`F-016-A` e `F-016` estão `RESOLVED`.\n\n```text\nF-016-A\n→ PHYSICAL CLEANUP APPLIED 119/119\n→ PHYSICAL SVG COUNT = 0\n→ SEMANTIC #832 SUCCESS\n→ MECHANICAL #1090 SUCCESS\n→ INDEPENDENT READ-ONLY PROOF V2 SUCCESS\n→ RESOLVED\n\nF-016\n→ AUDIT + ADJUDICATION COMPLETE\n→ LEGACY VISUAL PRODUCERS REMOVED 26/26\n→ STRUCTURAL REFERENCES TO REMOVED PRODUCERS = 0\n→ DIRECT REMOVED-SVG PATH REFERENCES = 0\n→ POST-DELETE PROOF = SUCCESS\n→ RESOLVED\n\nNEXT DOWNSTREAM DECISION\n→ J / K / L / M / N REMAIN NOT RELEASED AUTOMATICALLY\n→ REQUIRE SEPARATE GOVERNED RELEASE DECISION\n```",
)

# 3) Master audit: remove current-state drift while preserving historical checkpoints.
replace_exact(
    "docs/project/gkr-full-corpus-audit.md",
    "`GKR-BRAND-PUBLIC-AUTHORITY-PROPAGATION-001` teve as correções relacionadas à Home Pessoa absorvidas durante o Lote D; sua função residual passa a ser avaliada sob F-010 antes de qualquer consolidação ou remoção.",
    "`GKR-BRAND-PUBLIC-AUTHORITY-PROPAGATION-001` teve as correções relacionadas à Home Pessoa absorvidas durante o Lote D e foi adjudicado no fechamento de `F-010` como `KEEP TEMPORARILY`: registro transitório, não normativo e parcialmente absorvido, candidato a `REMOVE_AFTER_ABSORPTION` somente quando seus próprios critérios internos forem satisfeitos.",
)
replace_exact(
    "docs/project/gkr-full-corpus-audit.md",
    "| I — Registries / Catálogos / SVGs | `AUDITED / UPDATE_APPLIED / F-006_RESOLVED / F-007_RESOLVED / F-016-A_RESOLVED` | camada SVG removida; inventário físico corrente = 0; demais famílias F-016 continuam abertas |",
    "| I — Registries / Catálogos / SVGs | `AUDITED / UPDATE_APPLIED / F-006_RESOLVED / F-007_RESOLVED / F-016-A_RESOLVED / F-016_RESOLVED` | camada SVG removida; inventário físico corrente = 0; cleanup documental F-016 concluído 26/26 com autoridades/validadores/evidências preservados |",
)
replace_exact(
    "docs/project/gkr-full-corpus-audit.md",
    "F-016. desmaterialização documental              [aberta; F-016-A resolved; famílias Markdown pendentes]",
    "F-016. desmaterialização documental              [RESOLVED; F-016-A resolved; cleanup documental 26/26 + prova pós-delete concluídos]",
)

# 4) Specialized Homes authorities: remove decayed global-version claims and stale F-016 gate.
replace_exact(
    "docs/project/gkr-specialized-homes-audit.md",
    "Na integração do Lote F, o estado resultante era consumido por `GKR-STATE-001 v3.4.0` e `ROADMAP-13.4.0`. Essas versões são **proveniência do fechamento daquele lote**, não autoridades globais correntes. No estado posterior desta auditoria, prevalecem `GKR-STATE-001 v3.5.0`, `ROADMAP-13.5.0` e `GKR-FULL-CORPUS-AUDIT-001 v1.5.0`.",
    "Na integração do Lote F, o estado resultante era consumido por `GKR-STATE-001 v3.4.0` e `ROADMAP-13.4.0`. Essas versões são **proveniência do fechamento daquele lote**, não autoridades globais correntes. Para estado corrente, devem ser consultadas diretamente as revisões vigentes de `GKR-STATE-001`, `ROADMAP` e `GKR-FULL-CORPUS-AUDIT-001`; versões intermediárias posteriores ao Lote F também permanecem checkpoints históricos, não aliases permanentes da verdade atual.",
)
replace_exact(
    "docs/experience-architecture/public-specialized-homes-reconciliation.md",
    "As divergências encontradas foram resolvidas documentalmente sem perda de conhecimento e sem rebuild conceitual. O fechamento do Lote F foi originalmente consumido por `GKR-FULL-CORPUS-AUDIT-001 v1.4.0`, `GKR-STATE-001 v3.4.0` e `ROADMAP-13.4.0`; essas versões permanecem como **checkpoint histórico do Lote F**. No estado global posterior desta auditoria, prevalecem `GKR-FULL-CORPUS-AUDIT-001 v1.5.0`, `GKR-STATE-001 v3.5.0` e `ROADMAP-13.5.0`.",
    "As divergências encontradas foram resolvidas documentalmente sem perda de conhecimento e sem rebuild conceitual. O fechamento do Lote F foi originalmente consumido por `GKR-FULL-CORPUS-AUDIT-001 v1.4.0`, `GKR-STATE-001 v3.4.0` e `ROADMAP-13.4.0`; essas versões permanecem como **checkpoint histórico do Lote F**. Para o estado global corrente, devem ser consultadas diretamente as revisões vigentes de `GKR-FULL-CORPUS-AUDIT-001`, `GKR-STATE-001` e `ROADMAP`; revisões intermediárias posteriores ao Lote F não constituem aliases permanentes da verdade atual.",
)
replace_exact(
    "docs/experience-architecture/public-specialized-homes-reconciliation.md",
    "F-016\n→ OPEN\n\nF-016-A\n→ RESOLVED\n→ PHYSICAL_SVG_COUNT = 0\n\nNEXT F-016 GATE\n→ CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES\n→ J / K / L / M / N NOT RELEASED",
    "F-016\n→ RESOLVED\n→ LEGACY VISUAL PRODUCERS REMOVED 26/26\n→ POST-DELETE PROOF COMPLETE\n\nF-016-A\n→ RESOLVED\n→ PHYSICAL_SVG_COUNT = 0\n\nDOWNSTREAM RELEASE\n→ J / K / L / M / N NOT RELEASED AUTOMATICALLY\n→ REQUIRES SEPARATE GOVERNED DECISION",
)

# 5) Transitional propagation: current global refs + explicit F-010 adjudication.
replace_exact(
    "docs/governance-framework/brand-public-authority-propagation.md",
    "  - ROADMAP-13.5.0",
    "  - ROADMAP-13.11.0",
)
replace_exact(
    "docs/governance-framework/brand-public-authority-propagation.md",
    "| `GKR-STATE-001 v3.5.0` | `ABSORBED` | estado global já incorporado |",
    "| `GKR-STATE-001 v3.12.0` | `ABSORBED` | estado global já incorporado |",
)
replace_exact(
    "docs/governance-framework/brand-public-authority-propagation.md",
    "Até lá:\n\n```text\nPROPAGATION\n→ KEEP TEMPORARILY\n→ NON-NORMATIVE\n→ PARTIALLY ABSORBED\n→ CANDIDATE FOR REMOVE_AFTER_ABSORPTION\n```",
    "A adjudicação de `F-010` para este artefato está concluída e não permanece pendente: sua função corrente foi classificada como preservação transitória até que os critérios acima permitam uma decisão futura independente de remoção.\n\nAté lá:\n\n```text\nF-010 ADJUDICATION\n→ RESOLVED\n\nPROPAGATION\n→ KEEP TEMPORARILY\n→ NON-NORMATIVE\n→ PARTIALLY ABSORBED\n→ CANDIDATE FOR REMOVE_AFTER_ABSORPTION\n```",
)

# 6) RP-002 A11 closure: current notice revision is metadata-only reconciliation of reviewed target.
replace_exact(
    "docs/research/RP-002/pilot-documentation-closure-review.md",
    "- `RP-002-PILOT-NOTICE-CONSENT-002` v0.2.0.\n\nA versão está reconciliada documentalmente com:",
    "- `RP-002-PILOT-NOTICE-CONSENT-002` v0.2.1.\n\n`v0.2.0` permanece o checkpoint substantivo originalmente revisado em A11. A revisão `v0.2.1` reconciliou somente metadados de dependência (`RP-002-PILOT-OPS-REG-001` → `RP-002-PILOT-OPS-REG-002`), versão e data, sem alterar o conteúdo participante-facing do Notice; portanto o fechamento documental de A11 continua aplicável à revisão corrente, ainda condicionado a A12 e à reconciliação com a configuração operacional real.\n\nA versão está reconciliada documentalmente com:",
)

print("POST_F016_AUTHORITY_RECONCILIATION=SUCCESS")
