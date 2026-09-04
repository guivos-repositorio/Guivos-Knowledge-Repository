#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

TARGET_SHA = "20ac46358f07513830e72745f998cb46ca7d4509"
TODAY = "2026-09-04"

DELETIONS = [
    *(f"docs/project/canonical-consolidation-matrix-cod-{n:03d}-submission-addendum.md" for n in range(3, 18)),
    "docs/research/RP-002/pilot-operator-and-tool-registry.md",
    "docs/research/RP-002/pilot-participant-privacy-notice-and-consent-draft.md",
]

RP_VERSIONS = {
    "docs/research/RP-002/pilot-documentation-closure-decision.md": ("1.0.0", "1.0.1"),
    "docs/research/RP-002/pilot-final-legal-privacy-review-checklist.md": ("1.0.0", "1.0.1"),
    "docs/research/RP-002/pilot-identity-vault-implementation-decision.md": ("1.0.0", "1.0.1"),
    "docs/research/RP-002/pilot-minimum-stack-options-and-recommendation.md": ("0.1.0", "0.1.1"),
    "docs/research/RP-002/pilot-minimum-stack-target-decision.md": ("1.1.0", "1.1.1"),
    "docs/research/RP-002/pilot-notice-consent-flow-decision.md": ("1.0.0", "1.0.1"),
    "docs/research/RP-002/pilot-openai-api-implementation-decision.md": ("1.0.0", "1.0.1"),
    "docs/research/RP-002/pilot-operator-and-tool-registry-reconciliation.md": ("1.0.0", "1.0.1"),
    "docs/research/RP-002/pilot-participant-privacy-notice-and-consent-v0.2.md": ("0.2.0", "0.2.1"),
    "docs/research/RP-002/pilot-research-base-implementation-decision.md": ("1.0.0", "1.0.1"),
    "docs/research/RP-002/pilot-search-web-implementation-decision.md": ("1.0.0", "1.0.1"),
}

OPS_REPLACE = {
    "docs/research/RP-002/pilot-documentation-closure-decision.md",
    "docs/research/RP-002/pilot-final-legal-privacy-review-checklist.md",
    "docs/research/RP-002/pilot-identity-vault-implementation-decision.md",
    "docs/research/RP-002/pilot-minimum-stack-options-and-recommendation.md",
    "docs/research/RP-002/pilot-openai-api-implementation-decision.md",
    "docs/research/RP-002/pilot-participant-privacy-notice-and-consent-v0.2.md",
    "docs/research/RP-002/pilot-research-base-implementation-decision.md",
    "docs/research/RP-002/pilot-search-web-implementation-decision.md",
}
NOTICE_REPLACE = {
    "docs/research/RP-002/pilot-minimum-stack-options-and-recommendation.md",
    "docs/research/RP-002/pilot-minimum-stack-target-decision.md",
    "docs/research/RP-002/pilot-notice-consent-flow-decision.md",
}

GLOBAL_EDITS = {
    "docs/project/gkr-full-corpus-audit.md",
    "docs/project/current-state-register.md",
    "docs/roadmap.md",
    "README.md",
    "docs/index.md",
    "docs/experience-architecture/uxa-047-101-index.md",
}
EXPECTED_CHANGED = set(DELETIONS) | set(RP_VERSIONS) | GLOBAL_EDITS


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"EXPECTED_ONE {label} count={count}")
    return text.replace(old, new, 1)


def frontmatter(text: str, path: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise SystemExit(f"NO_FRONTMATTER {path}")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise SystemExit(f"UNCLOSED_FRONTMATTER {path}")
    return text[: end + 1], text[end + 1 :]


def apply() -> None:
    if len(DELETIONS) != 17 or len(EXPECTED_CHANGED) != 34:
        raise SystemExit(f"CLOSED_SET_MISMATCH deletions={len(DELETIONS)} total={len(EXPECTED_CHANGED)}")

    for path, (old_v, new_v) in RP_VERSIONS.items():
        text = read(path)
        fm, body = frontmatter(text, path)
        fm = once(fm, f"version: {old_v}", f"version: {new_v}", f"{path}:version")
        fm = once(fm, "last_updated: 2026-08-27", f"last_updated: {TODAY}", f"{path}:date")
        if path in OPS_REPLACE:
            fm = once(fm, "RP-002-PILOT-OPS-REG-001", "RP-002-PILOT-OPS-REG-002", f"{path}:ops")
        if path in NOTICE_REPLACE:
            fm = once(fm, "RP-002-PILOT-NOTICE-CONSENT-001", "RP-002-PILOT-NOTICE-CONSENT-002", f"{path}:notice")
        if path.endswith("pilot-operator-and-tool-registry-reconciliation.md"):
            fm = once(fm, "  - RP-002-PILOT-OPS-REG-001\n", "", f"{path}:remove-old-related")
        write(path, fm + body)

    recon = "docs/research/RP-002/pilot-operator-and-tool-registry-reconciliation.md"
    text = read(recon)
    text = once(
        text,
        "Este documento reconcilia o `RP-002-PILOT-OPS-REG-001` com as decisões documentais posteriores do stack.",
        "Este documento reconcilia o registro histórico `RP-002-PILOT-OPS-REG-001`, removido do corpus corrente após absorção e preservado no histórico Git, com as decisões documentais posteriores do stack.",
        "recon:history",
    )
    text = once(
        text,
        "O registro anterior permanece como histórico do momento em que vários componentes estavam `TBD`. Para o estado documental atual, este documento prevalece quando houver divergência de status-alvo.",
        "O registro anterior permanece recuperável no histórico Git como evidência do momento em que vários componentes estavam `TBD`. No corpus corrente, este documento é a autoridade documental de reconciliação e prevalece quando houver divergência de status-alvo.",
        "recon:status",
    )
    write(recon, text)

    audit = "docs/project/gkr-full-corpus-audit.md"
    text = read(audit)
    text = once(text, "version: 1.5.0", "version: 1.6.0", "audit:version")
    text = once(text, "last_updated: 2026-08-30", f"last_updated: {TODAY}", "audit:date")
    text = once(
        text,
        "| F-010 | Major | checkpoints, snapshots, propagations e reconciliações precisam de teste de função atual | `HOLD_REVIEW` | aberto; overlays pós-313 testados/reconciliados no Bloco H, demais famílias pendentes |",
        "| F-010 | Major | checkpoints, snapshots, propagations e reconciliações precisam de teste de função atual | `UPDATE + REMOVE_AFTER_ABSORPTION` | **auditoria estrutural concluída; cleanup aplicado no conjunto fechado de 17 artefatos; validação pós-cleanup pendente; não resolvido** |",
        "audit:f010-row",
    )
    audit_insert = (
        "Esse resultado do Bloco H não encerrava F-010 para as demais famílias.\n\n"
        "A adjudicação estrutural posterior concluiu a varredura das famílias residuais. Os snapshots e addenda que preservam função documental, evidência ou proveniência permanecem no corpus; o conjunto físico de remoção foi fechado em **17 artefatos** — quinze addenda intermediários de submissão `COD-003..017` e dois intermediários do `RP-002` já absorvidos por autoridades posteriores.\n\n"
        "A prova pré-delete foi executada sobre o checkpoint congelado `20ac46358f07513830e72745f998cb46ca7d4509` / tree `58b30bef8c01126c47a4c5f691bfbcfc7c4b44c3`: 1.390 blobs rastreados, 1.388 UTF-8 pesquisáveis, 443 hits externos classificados e **0 `UNCLASSIFIED`**. Os dois blobs não textuais eram archives ZIP históricos. Referências correntes aos intermediários `RP-002` foram reconciliadas com `RP-002-PILOT-OPS-REG-002` e `RP-002-PILOT-NOTICE-CONSENT-002` na mesma transação.\n\n"
        "```text\nF-010\n→ STRUCTURAL AUDIT COMPLETE\n→ CLEANUP APPLIED\n→ POST-CLEANUP VALIDATION PENDING\n→ NOT RESOLVED\n\nF-006\n→ NOT TOUCHED BY THIS TRANSACTION\n```\n\n"
        "O fechamento de F-010 somente poderá ser adjudicado após recomputação da árvore, verificação de ausência dos 17 artefatos, Semantic, Mechanical e review repo-wide no novo head."
    )
    text = once(text, "Isso não encerra F-010 para as demais famílias.", audit_insert, "audit:f010-section")
    write(audit, text)

    state = "docs/project/current-state-register.md"
    text = read(state)
    text = once(text, "version: 3.5.0", "version: 3.6.0", "state:version")
    text = once(text, "last_updated: 2026-08-30", f"last_updated: {TODAY}", "state:date")
    state_new = (
        "→ F-007 RESOLVED NO LIMITE SEMÂNTICO/INVENTÁRIO\n\n"
        "F-010\n→ STRUCTURAL AUDIT COMPLETE\n→ CLEANUP APPLIED ON CLOSED 17-ARTIFACT SET\n→ POST-CLEANUP VALIDATION PENDING\n→ NOT RESOLVED\n→ DOES NOT AUTHORIZE F-006 OR DOWNSTREAM RELEASE\n\n"
        "PRÓXIMO GATE DA AUDITORIA"
    )
    text = once(
        text,
        "→ F-007 RESOLVED NO LIMITE SEMÂNTICO/INVENTÁRIO\n\nPRÓXIMO GATE DA AUDITORIA",
        state_new,
        "state:f010",
    )
    write(state, text)

    roadmap = "docs/roadmap.md"
    text = read(roadmap)
    text = once(text, "id: ROADMAP-13.5.0", "id: ROADMAP-13.6.0", "roadmap:id")
    text = once(text, "version: 13.5.0", "version: 13.6.0", "roadmap:version")
    text = once(text, "last_updated: 2026-08-30", f"last_updated: {TODAY}", "roadmap:date")
    text = once(text, "Este roadmap traduz `GKR-STATE-001 v3.5.0`", "Este roadmap traduz `GKR-STATE-001 v3.6.0`", "roadmap:state")
    anchor = "O próximo gate é a autorização humana separada e explícita para o cleanup físico de F-006; somente após eventual remoção/reconciliação, recomputação, validações e review no novo head poderá ocorrer a decisão de fechamento de F-006 e de G/H/I."
    text = once(
        text,
        anchor,
        anchor
        + "\n\nEm trilha independente, `F-010` concluiu a auditoria estrutural e teve cleanup aplicado sobre um conjunto fechado de 17 artefatos. Seu estado é `POST-CLEANUP VALIDATION PENDING / NOT RESOLVED`. Esse ato **não consome nem substitui a autorização separada exigida por F-006**, não libera J/K/L/M/N e não ativa UXA-102, Design/materialização ou Product Engineering.",
        "roadmap:f010-paragraph",
    )
    text = once(
        text,
        "| Bloco I — Registries / Catálogos / SVGs | **AUDITED / UPDATE_APPLIED / F-006 OPEN / F-007 RESOLVED** |",
        "| Bloco I — Registries / Catálogos / SVGs | **AUDITED / UPDATE_APPLIED / F-006 OPEN / F-007 RESOLVED** |\n| F-010 — cleanup transversal | **CLEANUP APPLIED / POST-CLEANUP VALIDATION PENDING / NOT RESOLVED** |",
        "roadmap:f010-row",
    )
    write(roadmap, text)

    readme = "README.md"
    text = read(readme)
    text = once(text, "| GKR-STATE-001 | **3.5.0** |", "| GKR-STATE-001 | **3.6.0** |", "readme:state")
    text = once(text, "| F-007 | **RESOLVED — semantic/inventory scope** |", "| F-007 | **RESOLVED — semantic/inventory scope** |\n| F-010 | **CLEANUP APPLIED · POST-CLEANUP VALIDATION PENDING · NOT RESOLVED** |", "readme:f010-row")
    text = once(text, "O [Roadmap 13.5.0](docs/roadmap.md)", "O [Roadmap 13.6.0](docs/roadmap.md)", "readme:roadmap")
    text = once(text, "`F-006` permanece `OPEN / CLEANUP_ELIGIBILITY_PROVEN / PHYSICAL_REMOVAL_NOT_AUTHORIZED`; nenhum `UXA-015..018` ou SVG associado possui remoção autorizada.", "`F-006` permanece `OPEN / CLEANUP_ELIGIBILITY_PROVEN / PHYSICAL_REMOVAL_NOT_AUTHORIZED`; nenhum `UXA-015..018` ou SVG associado possui remoção autorizada.\n\n`F-010` está em `CLEANUP APPLIED / POST-CLEANUP VALIDATION PENDING / NOT RESOLVED`; esse estado não altera a autorização separada exigida por F-006.", "readme:f010-body")
    text = once(text, "[Estado Atual 3.5.0](docs/project/current-state-register.md)", "[Estado Atual 3.6.0](docs/project/current-state-register.md)", "readme:state-link")
    text = once(text, "[Roadmap 13.5.0](docs/roadmap.md)", "[Roadmap 13.6.0](docs/roadmap.md)", "readme:roadmap-link")
    write(readme, text)

    home = "docs/index.md"
    text = read(home)
    text = once(text, "| Registro | `GKR-STATE-001` **3.5.0** |", "| Registro | `GKR-STATE-001` **3.6.0** |", "home:state")
    text = once(text, "| F-007 | **RESOLVED — semantic/inventory scope** |", "| F-007 | **RESOLVED — semantic/inventory scope** |\n| F-010 | **CLEANUP APPLIED · POST-CLEANUP VALIDATION PENDING · NOT RESOLVED** |", "home:f010-row")
    text = once(text, "O [Roadmap 13.5.0](roadmap.md)", "O [Roadmap 13.6.0](roadmap.md)", "home:roadmap")
    text = once(text, "[Registro do Estado Atual 3.5.0](project/current-state-register.md)", "[Registro do Estado Atual 3.6.0](project/current-state-register.md)", "home:state-link")
    text = once(text, "[Roadmap 13.5.0](roadmap.md)", "[Roadmap 13.6.0](roadmap.md)", "home:roadmap-link")
    text = once(text, "`F-006` permanece `OPEN / CLEANUP_ELIGIBILITY_PROVEN / PHYSICAL_REMOVAL_NOT_AUTHORIZED`; nenhum `UXA-015..018` ou SVG associado possui remoção autorizada neste estágio.", "`F-006` permanece `OPEN / CLEANUP_ELIGIBILITY_PROVEN / PHYSICAL_REMOVAL_NOT_AUTHORIZED`; nenhum `UXA-015..018` ou SVG associado possui remoção autorizada neste estágio.\n\n`F-010` está em `CLEANUP APPLIED / POST-CLEANUP VALIDATION PENDING / NOT RESOLVED`; esse estado não altera a autorização separada exigida por F-006.", "home:f010-body")
    write(home, text)

    uxa_index = "docs/experience-architecture/uxa-047-101-index.md"
    text = read(uxa_index)
    text = once(text, "version: 3.5.0", "version: 3.6.0", "uxa-index:version")
    text = once(text, "last_updated: 2026-08-30", f"last_updated: {TODAY}", "uxa-index:date")
    text = once(text, "GKR-STATE-001\n→ 3.5.0", "GKR-STATE-001\n→ 3.6.0", "uxa-index:state-block")
    text = once(text, "→ F-007 RESOLVED NO LIMITE SEMÂNTICO/INVENTÁRIO\n\nPRÓXIMO GATE DA AUDITORIA", "→ F-007 RESOLVED NO LIMITE SEMÂNTICO/INVENTÁRIO\n\nF-010\n→ CLEANUP APPLIED / POST-CLEANUP VALIDATION PENDING / NOT RESOLVED\n→ F-006 E DOWNSTREAM NÃO LIBERADOS\n\nPRÓXIMO GATE DA AUDITORIA", "uxa-index:f010-block")
    text = once(text, "| Registro do Estado Atual | **3.5.0** |", "| Registro do Estado Atual | **3.6.0** |", "uxa-index:state-row")
    text = once(text, "| Bloco I — Registries / Catálogos / SVGs | **AUDITED / UPDATE_APPLIED / F-006 OPEN / F-007 RESOLVED** |", "| Bloco I — Registries / Catálogos / SVGs | **AUDITED / UPDATE_APPLIED / F-006 OPEN / F-007 RESOLVED** |\n| F-010 — cleanup transversal | **CLEANUP APPLIED / POST-CLEANUP VALIDATION PENDING / NOT RESOLVED** |", "uxa-index:f010-row")
    write(uxa_index, text)

    for path in DELETIONS:
        p = Path(path)
        if not p.is_file():
            raise SystemExit(f"MISSING_DELETE_CANDIDATE {path}")
        p.unlink()

    changed = set(subprocess.check_output(["git", "diff", "--name-only"], text=True).splitlines())
    if changed != EXPECTED_CHANGED:
        raise SystemExit(f"CHANGED_SET_MISMATCH missing={sorted(EXPECTED_CHANGED - changed)} extra={sorted(changed - EXPECTED_CHANGED)}")

    if any(any(token in Path(p).name for token in ("uxa-015", "uxa-016", "uxa-017", "uxa-018")) for p in changed):
        raise SystemExit("F006_TOUCHED")

    print(f"CLOSED_TRANSACTION_OK deletions=17 edits=17 total={len(changed)}")


def grep_lines(token: str) -> list[str]:
    p = subprocess.run(["git", "grep", "-n", "-F", token, "HEAD", "--", "."], text=True, capture_output=True)
    if p.returncode not in (0, 1):
        raise SystemExit(f"GREP_ERROR {token}")
    return [line for line in p.stdout.splitlines() if line.strip()] if p.returncode == 0 else []


def verify() -> None:
    changed = set(subprocess.check_output(["git", "diff", "--name-only", TARGET_SHA, "HEAD"], text=True).splitlines())
    if changed != EXPECTED_CHANGED or len(changed) != 34:
        raise SystemExit(f"COMMITTED_SET_MISMATCH count={len(changed)} missing={sorted(EXPECTED_CHANGED - changed)} extra={sorted(changed - EXPECTED_CHANGED)}")

    tree_paths = set(subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "HEAD"], text=True).splitlines())
    present = sorted(set(DELETIONS) & tree_paths)
    if present:
        raise SystemExit(f"DELETION_CANDIDATES_STILL_PRESENT {present}")

    for n in range(3, 18):
        token = f"GKR-CANON-MATRIX-COD-{n:03d}-SUBMISSION"
        if grep_lines(token):
            raise SystemExit(f"DANGLING {token}")

    if grep_lines("RP-002-PILOT-NOTICE-CONSENT-001"):
        raise SystemExit("DANGLING_NOTICE_001")

    ops = grep_lines("RP-002-PILOT-OPS-REG-001")
    if len(ops) != 1 or "pilot-operator-and-tool-registry-reconciliation.md" not in ops[0] or "histórico Git" not in ops[0]:
        raise SystemExit(f"OPS_001_PROVENANCE_NOT_EXACT {ops}")

    surfaces = ["README.md", "docs/index.md", "docs/experience-architecture/uxa-047-101-index.md"]
    for path in surfaces:
        text = read(path)
        if "3.6.0" not in text or "F-010" not in text or "POST-CLEANUP VALIDATION PENDING" not in text:
            raise SystemExit(f"SEMANTIC_SURFACE_NOT_SYNCHRONIZED {path}")

    required = {
        "docs/research/RP-002/pilot-operator-and-tool-registry-reconciliation.md",
        "docs/research/RP-002/pilot-participant-privacy-notice-and-consent-v0.2.md",
        "docs/project/gkr-full-corpus-audit.md",
        "docs/project/current-state-register.md",
        "docs/roadmap.md",
    }
    missing = sorted(required - tree_paths)
    if missing:
        raise SystemExit(f"RECEIVER_MISSING {missing}")

    print("POST_COMMIT_STRUCTURE_OK")
    print("NEW_SHA=" + subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip())
    print("NEW_TREE=" + subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], text=True).strip())


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"apply", "verify"}:
        raise SystemExit("usage: f010_cleanup_apply_temp.py apply|verify")
    if sys.argv[1] == "apply":
        apply()
    else:
        verify()


if __name__ == "__main__":
    main()
