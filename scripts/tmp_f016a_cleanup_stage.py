from pathlib import Path
import re
import subprocess

ROOT = Path('.')
TODAY = '2026-09-05'


def read(path: str) -> str:
    return Path(path).read_text(encoding='utf-8')


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding='utf-8')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {n}')
    return text.replace(old, new, 1)


def replace_section(path: str, heading: str, body: str) -> None:
    text = read(path)
    marker = '## ' + heading
    start = text.find(marker)
    if start < 0:
        raise SystemExit(f'{path}: missing section {heading}')
    end = text.find('\n## ', start + len(marker))
    if end < 0:
        end = len(text)
    replacement = marker + '\n\n' + body.rstrip() + '\n'
    write(path, text[:start] + replacement + text[end:])


def frontmatter_set(path: str, key: str, value: str) -> None:
    text = read(path)
    if not text.startswith('---\n'):
        raise SystemExit(f'{path}: no YAML frontmatter')
    end = text.find('\n---\n', 4)
    if end < 0:
        raise SystemExit(f'{path}: malformed YAML frontmatter')
    fm = text[4:end]
    body = text[end+5:]
    pat = re.compile(rf'(?m)^{re.escape(key)}:\s*.*$')
    if pat.search(fm):
        fm = pat.sub(f'{key}: {value}', fm, count=1)
    else:
        fm = fm.rstrip() + f'\n{key}: {value}'
    write(path, '---\n' + fm + '\n---\n' + body)


def insert_notice(path: str) -> None:
    text = read(path)
    marker = '> **F-016-A — desmaterialização física.**'
    if marker in text:
        return
    m = re.search(r'(?m)^# .+$', text)
    if not m:
        raise SystemExit(f'{path}: missing H1 for F-016-A notice')
    end = text.find('\n', m.end())
    if end < 0:
        end = len(text)
    notice = (
        '\n\n> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. '
        'Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. '
        'O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.\n'
    )
    write(path, text[:end] + notice + text[end:])


tracked = [x.decode() for x in subprocess.check_output(['git','ls-files','-z']).split(b'\0') if x]
assets = sorted(x for x in tracked if x.startswith('docs/assets/wireframes/') and x.endswith('.svg'))
if len(assets) != 119:
    raise SystemExit(f'F016A_ASSET_COUNT={len(assets)} expected 119')
basenames = {Path(a).name for a in assets}

# Preserve explicit history/provenance documents unchanged.
def provenance_only(rel: str) -> bool:
    p = Path(rel)
    name = p.name
    if rel.startswith('docs/project/changelog'):
        return True
    if rel.startswith('docs/project/') and name.endswith('-pr-checkpoint.md'):
        return True
    if rel.startswith('docs/project/canonical-consolidation-matrix-uxa-'):
        return True
    return False

md_image = re.compile(r'!\[[^\]]*\]\([^\)]*\.svg(?:#[^\)]*)?\)(?:\{[^\n]*\})?', re.I)
md_link = re.compile(r'(?<!!)\[[^\]]*\]\([^\)]*\.svg(?:#[^\)]*)?\)', re.I)
standalone_raw = re.compile(r'^\s*`(?:docs/)?assets/wireframes/[^`]+\.svg`[;,.]?\s*$')

active_affected = []
removed_embeds = 0
removed_links = 0
removed_raw_lines = 0

for rel in tracked:
    if rel in assets or provenance_only(rel):
        continue
    p = Path(rel)
    try:
        text = p.read_text(encoding='utf-8')
    except (UnicodeDecodeError, IsADirectoryError):
        continue
    if not any(base in text for base in basenames):
        continue

    original = text
    new_lines = []
    for line in text.splitlines():
        if not any(base in line for base in basenames):
            new_lines.append(line)
            continue
        image_hits = len(md_image.findall(line))
        link_hits = len(md_link.findall(line))
        if image_hits:
            line = md_image.sub('', line)
            removed_embeds += image_hits
        if link_hits:
            line = md_link.sub('', line)
            removed_links += link_hits
        if standalone_raw.match(line.strip()):
            removed_raw_lines += 1
            continue
        # If an embed/link-only line became empty, drop it.
        if not line.strip():
            continue
        new_lines.append(line.rstrip())

    text = '\n'.join(new_lines) + ('\n' if original.endswith('\n') else '')
    if text != original:
        write(rel, text)
    if rel.startswith('docs/experience-architecture/') or rel.startswith('docs/journeys/'):
        insert_notice(rel)
    active_affected.append(rel)

# Reclassify physical-gallery instruments as historical provenance only.
gallery_files = sorted(Path('docs/journeys').glob('screen-gallery*.md'))
for p in gallery_files:
    path = str(p)
    frontmatter_set(path, 'status', 'superseded')
    frontmatter_set(path, 'last_updated', TODAY)
    frontmatter_set(path, 'maturity', 'historical_provenance_only')
    insert_notice(path)

# Traceability matrix no longer has a current physical association layer.
trace = 'docs/journeys/screen-gallery-traceability-matrix.md'
frontmatter_set(trace, 'version', '0.26.0')
replace_section(trace, '1. Finalidade', '''Esta matriz preserva os **34 perfis de rastreabilidade** e a proveniência dos ciclos visuais anteriores, mas não representa mais uma camada física vigente.

O cleanup `F-016-A` removeu os **119/119 SVGs** que ainda existiam em `docs/assets/wireframes/`. A cobertura funcional foi provada antes da remoção: cada asset possuía perfil rastreável e referência textual em Experience Architecture, e cada perfil físico possuía receiver textual corrente fora da família de galeria.

```text
SVGs FÍSICOS VIGENTES
→ 0

ASSOCIAÇÕES FÍSICAS VIGENTES
→ 0

PERFIS DE RASTREABILIDADE PRESERVADOS
→ 34
→ PROVENIÊNCIA / RASTREABILIDADE SEMÂNTICA
→ NÃO AUTORIDADE VISUAL
```

R09 e R11 já eram perfis sem SVG após `F-006`; os demais perfis deixam de ter associação física após `F-016-A`.''')
replace_section(trace, '4. Associação individual dos 119 SVGs físicos remanescentes', '''A associação física foi encerrada por `F-016-A`.

```text
ANTES DO CLEANUP F-016-A
→ 119 SVGs físicos
→ 119 associações físicas

APÓS O CLEANUP F-016-A
→ 0 SVGs físicos
→ 0 associações físicas
```

Os nomes dos assets e suas associações anteriores permanecem recuperáveis no histórico Git. O corpus vigente preserva somente os perfis e contratos textuais necessários.''')

# Screen catalog: physical layer becomes zero; functional registry remains authoritative.
catalog = 'docs/journeys/screen-catalog.md'
text = read(catalog)
text = text.replace('inventário físico corrente após F-006: **119 SVGs**;', 'inventário físico corrente após F-016-A: **0 SVGs**;', 1)
text = text.replace('matriz física: **119 associações / 34 perfis estáveis**, com R09/R11 preservados apenas como proveniência sem SVG;', 'matriz física: **0 associações físicas / 34 perfis de proveniência**, sem autoridade visual;', 1)
write(catalog, text)
insert_notice(catalog)

# Experience Architecture index: replace current physical coverage section with post-cleanup truth.
exa = 'docs/experience-architecture/index.md'
frontmatter_set(exa, 'version', '1.6.0')
frontmatter_set(exa, 'last_updated', TODAY)
replace_section(exa, '3. Cobertura visual e granular', '''A camada física de wireframes foi removida do corpus vigente por `F-016-A` após prova estrutural e semântica de absorção.

```text
SVGs FÍSICOS EM docs/assets/wireframes/
→ 0

ASSOCIAÇÕES FÍSICAS CORRENTES
→ 0

PERFIS DE RASTREABILIDADE
→ 34
→ preservados apenas como proveniência/semântica

AUTORIDADE VISUAL
→ DESIGN

AUTORIDADE FUNCIONAL
→ DOCUMENTAÇÃO TEXTUAL / EXPERIENCE ARCHITECTURE
```

A remoção física não altera por si só maturidade funcional de superfícies, estados ou transições. Nomes `.svg` ainda citados em documentos preservados devem ser lidos exclusivamente como proveniência histórica.''')

# Journeys index: update only current physical statements.
jidx = 'docs/journeys/index.md'
frontmatter_set(jidx, 'version', '0.42.0')
frontmatter_set(jidx, 'last_updated', TODAY)
text = read(jidx)
text = text.replace('| catálogo integrado | `active` 0.33.0 | 121 SVGs físicos; TRN-008..013 integrais; claim agregada antiga de validação superseded |', '| catálogo integrado | `active` 0.33.0 | 0 SVGs físicos após F-016-A; TRN-008..013 integrais; contratos textuais preservados |', 1)
text = text.replace('| galeria visual integrada | `active` | 121 SVGs físicos para inspeção; não equivalem a 121 wireframes vigentes |', '| galeria visual integrada | `superseded / historical_provenance_only` | camada física removida por F-016-A; sem autoridade visual corrente |', 1)
text = text.replace('| matriz por SVG | `active` | 121 associações físicas / 34 perfis; não é prova agregada de vigência |', '| matriz por SVG | `superseded / historical_provenance_only` | 0 associações físicas / 34 perfis de proveniência; sem autoridade visual |', 1)
write(jidx, text)
insert_notice(jidx)

# Current global authorities: transition state after physical cleanup, before post-cleanup validation.
state = 'docs/project/current-state-register.md'
frontmatter_set(state, 'version', '3.10.0')
replace_section(state, '2. Estado executivo', '''```text
ERA
→ GE-2 — KNOWLEDGE

ESTADO GLOBAL DO GKR
→ AUDITORIA INTEGRAL EM CURSO

BLOCO 2 — G / H / I
→ G COMPLETED / UPDATE_APPLIED
→ H AUDITED / UPDATE_APPLIED / F-006 RESOLVED
→ I AUDITED / UPDATE_APPLIED / F-006 RESOLVED / F-007 RESOLVED

F-010
→ RESOLVED
→ CODEX REVIEW UNAVAILABLE / NOT RUN (USAGE LIMIT)
→ CLEAN RESULT NOT CLAIMED

F-006
→ RESOLVED

F-016
→ OPEN / REPO-WIDE DOCUMENTATION DEMATERIALIZATION

F-016-A — PHYSICAL SVG LAYER
→ PRE-CLEANUP ELIGIBILITY PROVEN
→ HUMAN PHYSICAL CLEANUP AUTHORIZATION GRANTED
→ PHYSICAL CLEANUP APPLIED 119/119
→ PHYSICAL SVG COUNT = 0
→ EMBEDS / LIVE LINKS RECONCILED
→ HISTORICAL PROVENANCE PRESERVED
→ POST-CLEANUP VALIDATION PENDING
→ FORMAL RESOLUTION NOT YET CLAIMED

J / K / L / M / N
→ NOT RELEASED AUTOMATICALLY

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

PMF
→ NOT VALIDATED

BASELINE FINAL PÓS-AUDITORIA
→ NOT AUTHORIZED

PRIMEIRA TELA AUTENTICADA DA PESSOA APÓS A HOME
→ BLOCKED UNTIL AUDIT CLOSES

MATERIALIZAÇÃO VISUAL DAS HOMES
→ NOT AUTHORIZED DURING FULL-CORPUS AUDIT
```

A remoção física de `F-016-A` não promove maturidade funcional, não cria Design e não libera implementação. O próximo gate é validar e revisar o novo head exato antes de qualquer adjudicação formal de fechamento.''')

road = 'docs/roadmap.md'
frontmatter_set(road, 'id', 'ROADMAP-13.10.0')
frontmatter_set(road, 'version', '13.10.0')
text = read(road)
text = text.replace('GKR-STATE-001 v3.9.0', 'GKR-STATE-001 v3.10.0')
text = text.replace('ROADMAP-13.9.0', 'ROADMAP-13.10.0')
write(road, text)
replace_section(road, '26. Regra do próximo movimento', '''`F-016-A` consumiu a autorização humana separada e teve o cleanup físico aplicado sobre os **119/119 SVGs**.

```text
F-016-A
→ CLEANUP_ELIGIBILITY_PROVEN BEFORE DELETE
→ HUMAN AUTHORIZATION GRANTED
→ PHYSICAL CLEANUP APPLIED 119/119
→ PHYSICAL SVG COUNT = 0
→ REFERENCE RECONCILIATION APPLIED
→ POST-CLEANUP VALIDATION PENDING
→ FORMAL CLOSURE PENDING

NEXT
→ RECOMPUTE THE RESULTING TREE
→ SEMANTIC VALIDATION
→ MECHANICAL VALIDATION
→ INDEPENDENT READ-ONLY REVIEW
→ ONLY THEN ADJUDICATE F-016-A
```

J/K/L/M/N, `UXA-102/V5`, Design, Product Engineering e merge da PR #363 permanecem bloqueados ou não autorizados.''')

audit = 'docs/project/gkr-full-corpus-audit.md'
frontmatter_set(audit, 'version', '1.10.0')
text = read(audit)
text = text.replace('| F-016 | Major | corpus ainda contém wireframes, materializações, galerias e linguagem de UI que podem competir com Design como autoridade visual | `REMOVE_AFTER_ABSORPTION + REWRITE` | **OPEN — desmaterialização documental repo-wide; preservar apenas conteúdo funcional necessário e proveniência legítima** |', '| F-016 | Major | corpus ainda contém documentos de materialização/galeria e linguagem de UI que podem competir com Design; a camada física SVG já foi removida | `REMOVE_AFTER_ABSORPTION + REWRITE` | **OPEN — F-016-A cleanup físico 119/119 aplicado; validação pós-cleanup pendente; demais famílias documentais continuam em auditoria** |', 1)
write(audit, text)
# Replace the dedicated F-016 section with current transitional state while preserving the governing boundary.
replace_section(audit, 'F-016 — Desmaterialização documental repo-wide', '''A auditoria mantém a fronteira estrutural obrigatória:

```text
GKR
→ intenção, conteúdo, informação, estados, regras, comportamento, permissões, fluxos, relações, requisitos, restrições, critérios e handoff

DESIGN
→ composição visual, layout, posicionamento, wireframes, mockups, protótipos, componentes visuais, aparência e materialização final
```

### F-016-A — camada física SVG

A subfrente física teve elegibilidade provada no head pré-delete, recebeu autorização humana separada e teve cleanup aplicado sobre o conjunto fechado de **119 SVGs**.

```text
PRE-DELETE PHYSICAL SVGs
→ 119

POST-DELETE PHYSICAL SVGs
→ 0

EMBEDS / LIVE LINKS TO REMOVED ASSETS
→ RECONCILED IN SAME TRANSACTION

NOMINAL .svg REFERENCES THAT REMAIN
→ HISTORICAL PROVENANCE ONLY
→ QUALIFIED IN ACTIVE DOCUMENTS

POST-CLEANUP VALIDATION
→ PENDING

F-016-A FORMAL RESOLUTION
→ NOT YET CLAIMED
```

As galerias e a matriz por SVG permanecem fisicamente como documentos de proveniência `superseded / historical_provenance_only`, sem autoridade visual corrente. Nenhum Markdown foi removido automaticamente por este gate.

### Demais famílias F-016

Documentos `low-fidelity-wireframe`, `materialization`, validações/programas de wireframe, galerias e linguagem de UI continuam sujeitos à classificação individual:

- `KEEP_FUNCTIONAL`;
- `REWRITE_FUNCTIONAL`;
- `REMOVE_AFTER_ABSORPTION`;
- `REMOVE`;
- `HISTORICAL_PROVENANCE_ONLY`.

Critério de encerramento global: **o GKR não pode competir com Design na definição de interface**.''')

# README / docs index / UXA index: synchronize global version and transitional F-016-A state.
for path in ['README.md', 'docs/index.md']:
    text = read(path)
    text = text.replace('3.9.0', '3.10.0')
    text = text.replace('13.9.0', '13.10.0')
    text = text.replace('F-016-A\n→ CLEANUP_ELIGIBILITY_PROVEN\n→ PHYSICAL_CLEANUP_NOT_AUTHORIZED', 'F-016-A\n→ PHYSICAL CLEANUP APPLIED 119/119\n→ PHYSICAL SVG COUNT = 0\n→ POST-CLEANUP VALIDATION PENDING')
    text = text.replace('F-016-A — 119 SVGs físicos', 'F-016-A — camada física SVG')
    write(path, text)

uxaidx = 'docs/experience-architecture/uxa-047-101-index.md'
frontmatter_set(uxaidx, 'version', '3.10.0')
text = read(uxaidx)
text = text.replace('GKR-STATE-001\n→ 3.9.0', 'GKR-STATE-001\n→ 3.10.0')
text = text.replace('F-016-A — 119 SVGs físicos | **CLEANUP_ELIGIBILITY_PROVEN / PHYSICAL_CLEANUP_NOT_AUTHORIZED**', 'F-016-A — camada física SVG | **PHYSICAL CLEANUP APPLIED 119/119 / PHYSICAL SVG COUNT 0 / POST-CLEANUP VALIDATION PENDING**')
write(uxaidx, text)

# Remove the physical assets last, after references/state have been reconciled in the working tree.
for asset in assets:
    Path(asset).unlink()

# Guardrails on the candidate working tree.
remaining = sorted(Path('docs/assets/wireframes').glob('*.svg')) if Path('docs/assets/wireframes').exists() else []
if remaining:
    raise SystemExit(f'POST_DELETE_SVG_COUNT={len(remaining)} expected 0')

tracked_after = [x.decode() for x in subprocess.check_output(['git','ls-files','-z']).split(b'\0') if x]
# git ls-files still lists deleted files until commit; inspect actual filesystem instead.

# No active document may retain a clickable/embed reference to a removed SVG.
broken_live = []
unqualified_active = []
for rel in tracked:
    if rel in assets or provenance_only(rel):
        continue
    p = Path(rel)
    if not p.exists():
        continue
    try:
        text = p.read_text(encoding='utf-8')
    except (UnicodeDecodeError, IsADirectoryError):
        continue
    if any(base in text for base in basenames):
        if md_image.search(text) or md_link.search(text):
            broken_live.append(rel)
        if (rel.startswith('docs/experience-architecture/') or rel.startswith('docs/journeys/')) and '> **F-016-A — desmaterialização física.**' not in text:
            unqualified_active.append(rel)

if broken_live:
    raise SystemExit('LIVE_SVG_LINKS_REMAIN=' + ','.join(sorted(set(broken_live))))
if unqualified_active:
    raise SystemExit('UNQUALIFIED_ACTIVE_SVG_PROVENANCE=' + ','.join(sorted(set(unqualified_active))))

print(f'F016A_DELETED_ASSETS={len(assets)}')
print(f'REMOVED_MARKDOWN_EMBEDS={removed_embeds}')
print(f'REMOVED_MARKDOWN_LINKS={removed_links}')
print(f'REMOVED_STANDALONE_RAW_PATH_LINES={removed_raw_lines}')
print(f'ACTIVE_DOCUMENTS_QUALIFIED={len(set(active_affected))}')
print('POST_DELETE_PHYSICAL_SVG_COUNT=0')
print('F016A_STAGE_TRANSFORMATION=PASS')
