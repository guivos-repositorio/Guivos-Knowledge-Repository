from pathlib import Path

AUDIT_PATH = Path("docs/project/gkr-full-corpus-audit.md")
STATE_PATH = Path("docs/project/current-state-register.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


def replace_section(text: str, start: str, end: str, replacement: str, label: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise RuntimeError(
            f"{label}: start={text.count(start)} end={text.count(end)}"
        )
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + replacement + text[j:]


audit = AUDIT_PATH.read_text(encoding="utf-8")
state = STATE_PATH.read_text(encoding="utf-8")

# --- GKR-FULL-CORPUS-AUDIT-001 ---
audit = replace_once(audit, "version: 1.1.0", "version: 1.2.0", "audit version")
audit = replace_once(
    audit, "last_updated: 2026-08-27", "last_updated: 2026-08-29", "audit date"
)
audit = replace_once(
    audit,
    "| F-003 | Critical | Home principal/Pessoa conflita com assinatura e Movimento 06 vigentes | `REBUILD` | próximo lote |",
    "| F-003 | Critical | Home principal/Pessoa conflita com assinatura e Movimento 06 vigentes | `REBUILD` | resolvido no Lote D |",
    "F-003 row",
)
audit = replace_once(
    audit,
    "| F-004 | Major | Home O/C antecede mudanças estruturais posteriores | `REBUILD` | aberto |",
    "| F-004 | Major | Home O/C antecede mudanças estruturais posteriores | `REBUILD` | próximo lote |",
    "F-004 row",
)

f003 = """## 7. F-003 — Home principal/Pessoa — resolvido no Lote D

O conflito material originalmente comprovado foi tratado de forma incremental e governada no Lote D, sem abrir materialização visual.

A sequência canônica foi:

- PR #342 — reconstrução de `GKR-UX-HOME-MASTER-001` como autoridade de consumo autocontida;
- PR #343 — reclassificação de resíduos de autoridade/checkpoint;
- PR #344 — reconciliação dos artefatos narrativos detalhados;
- PR #345 — correção do ciclo de dependência documental;
- PR #346 — reconciliação das autoridades de auditoria da Home;
- PR #348 — fechamento de `RES-01` em navegação/fronteira GTM;
- PR #349 — fechamento do último resíduo conhecido `RES-03` em `GKR-UX-HOME-HANDOFF-001`.

O estado reconciliado preserva, entre outros pontos:

```text
GUIVOS
→ Possibility, lived.
→ Possibilidade, vivida.
→ #PossibilityLived

FUNDADOR
→ Do possível ao vivido.
→ assinatura pessoal/autoral
→ não é assinatura institucional da Guivos

MOVIMENTO 06
→ Da Possibilidade à Experiência

POSSIBILIDADE
≠ OPORTUNIDADE

MECANISMO
→ obrigatório quando necessário na passagem específica

OPORTUNIDADE REAL
→ condicional à existência de oferta/viabilização concreta e acesso real
```

O fechamento documental também preserva Header/launcher/CTAs, autonomia, acessibilidade, prova, histórias reais, patrocínio identificável, fronteira pública × Journey protegida, os nove Domínios como vocabulário sem taxonomia visual obrigatória e a separação entre participantes e Produtos.

Conclusão comprovada:

> **Home principal/Pessoa = DOCUMENTALMENTE_RECONCILIADA_PRE_MATERIALIZAÇÃO.**

Esse estado não autoriza wireframe, Figma, UI, protótipo, implementação, publicação, disponibilidade operacional nem a primeira tela autenticada da Pessoa.

"""
audit = replace_section(
    audit,
    "## 7. F-003 — conflito material da Home principal\n",
    "## 8. F-004 — Home de Organizações e Coletivos\n",
    f003,
    "F-003 section",
)

audit = replace_once(
    audit,
    "`GKR-BRAND-PUBLIC-AUTHORITY-PROPAGATION-001` permanece temporariamente necessário porque ainda contém correções que precisam ser absorvidas no master da Home Pessoa no Lote D.",
    "`GKR-BRAND-PUBLIC-AUTHORITY-PROPAGATION-001` teve as correções relacionadas à Home Pessoa absorvidas durante o Lote D; sua função residual passa a ser avaliada sob F-010 antes de qualquer consolidação ou remoção.",
    "propagation status",
)
audit = replace_once(
    audit,
    "| C — Fundação / Marca / Public Canon | `COMPLETED_IN_BRANCH_PENDING_FINAL_VALIDATION` | Fundação reconciliada/enriquecida + GOG 5.3.0 |",
    "| C — Fundação / Marca / Public Canon | `COMPLETED` | Fundação reconciliada/enriquecida + GOG 5.3.0 |",
    "matrix C",
)
audit = replace_once(
    audit,
    "| D — Home principal / Pessoa | `REBUILD_REQUIRED / NEXT` | master reconstruído e enriquecido |",
    "| D — Home principal / Pessoa | `COMPLETED` | master e resíduos documentais reconciliados; materialização não autorizada |",
    "matrix D",
)
audit = replace_once(
    audit,
    "| E — Home Organizações e Coletivos | `REBUILD_REQUIRED` | master reconstruído |",
    "| E — Home Organizações e Coletivos | `REBUILD_REQUIRED / NEXT` | master reconstruído |",
    "matrix E",
)
audit = replace_once(
    audit,
    "C. Fundação / Marca / Public Canon              [concluído no branch; validar/integrar]\n↓\nD. Home principal / Pessoa                      [próximo]\n↓\nE/F. demais Homes",
    "C. Fundação / Marca / Public Canon              [concluído]\n↓\nD. Home principal / Pessoa                      [concluído]\n↓\nE. Home Organizações e Coletivos                 [próximo]\n↓\nF. Homes de Produtos",
    "execution order",
)

state22 = """## 22. Estado atual

```text
AUDIT
→ IN_PROGRESS

A / B / C / D
→ COMPLETED

NEXT LOT
→ E — HOME ORGANIZAÇÕES E COLETIVOS

BASELINE FINAL
→ NOT AUTHORIZED

CORPUS CLEANUP
→ NOT YET COMPLETE

HOME PRINCIPAL
→ DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION

HOME ORGANIZAÇÕES E COLETIVOS
→ REBUILD_REQUIRED

DEMAIS HOMES
→ AUDIT_PENDING

MENU FINAL
→ NOT YET DESIGNED

FIRST PERSON SCREEN AFTER HOME
→ BLOCKED UNTIL AUDIT CLOSES
```

"""
audit = replace_section(
    audit,
    "## 22. Estado atual\n",
    "## 23. Destino deste registro\n",
    state22,
    "audit current state section",
)

# --- GKR-STATE-001 ---
state = replace_once(state, "version: 3.1.0", "version: 3.2.0", "state version")
state = replace_once(
    state, "last_updated: 2026-08-27", "last_updated: 2026-08-29", "state date"
)
state = replace_once(
    state,
    "ESTADO GLOBAL DO GKR\n→ AUDITORIA INTEGRAL EM CURSO\n\nMARCO FUNCIONAL",
    "ESTADO GLOBAL DO GKR\n→ AUDITORIA INTEGRAL EM CURSO\n\nPRÓXIMO LOTE DA AUDITORIA\n→ E — HOME ORGANIZAÇÕES E COLETIVOS\n\nMARCO FUNCIONAL",
    "state executive next lot",
)
state = replace_once(
    state,
    "| Principal / Pessoa | `REBUILD_REQUIRED` |",
    "| Principal / Pessoa | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |",
    "state homes table",
)

home_person = """### 10.1 Home principal / Pessoa

O Lote D foi concluído documentalmente pela sequência canônica de PRs #342–#349.

A reconstrução e as reconciliações posteriores absorveram os conflitos conhecidos com Fundação, Marca, Public Canon e Experience Architecture, incluindo:

- separação `Guivos × fundador` e remoção de `Do possível ao vivido.` como assinatura institucional da Home;
- Movimento 06 = `Da Possibilidade à Experiência`;
- distinção `Possibilidade ≠ Oportunidade` e presença de Mecanismo quando necessário;
- nove Domínios de Evolução como vocabulário de amplitude, sem materialização visual automática;
- separação `participante ≠ produto` e `Organização ≠ Business`;
- Intelligence como Produto Especializado transversal / Intelligence Layer;
- fronteira entre exploração pública e Journey protegida;
- navegação, Header, launcher e hierarquia de CTAs;
- prova, histórias reais, patrocínio identificável, autonomia e acessibilidade;
- briefing/handoff subordinado ao Master e às autoridades especializadas.

Estado:

```text
HOME PRINCIPAL / PESSOA
→ DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION

WIREFRAME / FIGMA / UI / PROTÓTIPO / IMPLEMENTAÇÃO
→ NOT AUTHORIZED BY THIS CLOSURE

PRIMEIRA TELA AUTENTICADA DA PESSOA
→ BLOCKED UNTIL FULL AUDIT CLOSES
```

O fechamento de D não promove disponibilidade operacional, PMF, lançamento ou qualquer lote posterior da auditoria.

"""
state = replace_section(
    state,
    "### 10.1 Home principal / Pessoa\n",
    "### 10.2 Home de Organizações e Coletivos\n",
    home_person,
    "state home person section",
)

AUDIT_PATH.write_text(audit, encoding="utf-8")
STATE_PATH.write_text(state, encoding="utf-8")

# Self-cleaning working artifacts. They must not survive in the final PR diff.
Path("docs/project/.audit-lote-d-close-e-next-work.md").unlink(missing_ok=True)
Path(".github/workflows/temp-gkr-lot-d-close.yml").unlink(missing_ok=True)
Path(".github/scripts/temp_gkr_lot_d_close.py").unlink(missing_ok=True)

print("governed patch applied")
