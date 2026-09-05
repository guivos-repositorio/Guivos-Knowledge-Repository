from pathlib import Path
import re

TODAY='2026-09-05'


def read(path): return Path(path).read_text(encoding='utf-8')
def write(path,text): Path(path).write_text(text,encoding='utf-8')

def replace_once(text,old,new,label):
    n=text.count(old)
    if n!=1: raise SystemExit(f'{label}: expected 1 occurrence, found {n}')
    return text.replace(old,new,1)

def replace_section(path,heading,body):
    s=read(path); marker='## '+heading
    i=s.find(marker)
    if i<0: raise SystemExit(f'{path}: missing {marker}')
    j=s.find('\n## ',i+len(marker))
    if j<0: j=len(s)
    write(path,s[:i]+marker+'\n\n'+body.rstrip()+'\n'+s[j:])

def fm_set(path,key,value):
    s=read(path)
    if not s.startswith('---\n'): raise SystemExit(f'{path}: missing frontmatter')
    end=s.find('\n---\n',4)
    if end<0: raise SystemExit(f'{path}: malformed frontmatter')
    fm=s[4:end]; body=s[end+5:]
    pat=re.compile(rf'(?m)^{re.escape(key)}:\s*.*$')
    if pat.search(fm): fm=pat.sub(f'{key}: {value}',fm,count=1)
    else: fm=fm.rstrip()+f'\n{key}: {value}'
    write(path,'---\n'+fm+'\n---\n'+body)

# README — current physical truth + final F-016-A state.
replace_section('README.md','Inventário visual auditado','''Após `F-016-A`, a camada física de wireframes foi removida do corpus vigente:

- **0 SVGs físicos** em `docs/assets/wireframes/`;
- **0 associações físicas correntes**;
- **34 perfis de rastreabilidade preservados como proveniência/semântica**, sem autoridade visual;
- **0 embeds ou links vivos** para os assets removidos na prova pós-delete.

```text
SVG FÍSICO
≠ AUTORIDADE VISUAL
≠ MATURIDADE DE DESIGN

AUTORIDADE VISUAL
→ DESIGN
```

`F-006` e `F-010` permanecem `RESOLVED`. O review Codex de F-010 permaneceu indisponível por limite de uso, sem claim `CLEAN`.

`F-016-A` está `RESOLVED` após elegibilidade estrutural/semântica, autorização humana separada, cleanup 119/119, reconciliação das referências, Semantic #832, Mechanical #1090 e prova read-only pós-delete v2.

`F-016` global permanece `OPEN`: as famílias Markdown de materialização ainda exigem classificação individual e eventual reescrita/absorção.''')
replace_section('README.md','Próximo gate da auditoria','''`F-016-A` está formalmente `RESOLVED`. A camada física SVG não é mais uma dependência do corpus vigente.

```text
F-016-A
→ PRE-CLEANUP STRUCTURAL ELIGIBILITY PROVEN
→ PRE-CLEANUP SEMANTIC RECEIVER COVERAGE PROVEN
→ HUMAN PHYSICAL CLEANUP AUTHORIZATION GRANTED
→ PHYSICAL CLEANUP APPLIED 119/119
→ PHYSICAL SVG COUNT = 0
→ LIVE EMBEDS / LINKS RECONCILED
→ HISTORICAL PROVENANCE PRESERVED
→ SEMANTIC #832 SUCCESS
→ MECHANICAL #1090 SUCCESS
→ INDEPENDENT POST-DELETE READ-ONLY PROOF V2 SUCCESS
→ RESOLVED
```

O eixo corrente continua sendo `F-016 — desmaterialização documental repo-wide`, agora restrito às famílias documentais remanescentes. Nenhum Markdown é removido por inferência: cada artefato deverá ser classificado como `KEEP_FUNCTIONAL`, `REWRITE_FUNCTIONAL`, `REMOVE_AFTER_ABSORPTION`, `REMOVE` ou `HISTORICAL_PROVENANCE_ONLY`.

```text
J / K / L / M / N
→ NOT RELEASED AUTOMATICALLY

O
→ PENDING / HOLD

Q
→ BLOCKED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

DESIGN / MATERIALIZATION
→ NOT AUTHORIZED

MERGE #363
→ NOT AUTHORIZED
```''')

# docs/index
replace_section('docs/index.md','Materializações e contagens','''`F-006` e `F-016-A` concluíram seus cleanups físicos governados. O estado corrente da camada SVG é:

```text
SVGs FÍSICOS EM docs/assets/wireframes/
→ 0

ASSOCIAÇÕES FÍSICAS CORRENTES
→ 0

PERFIS DE RASTREABILIDADE
→ 34
→ PROVENIÊNCIA / SEMÂNTICA
→ NÃO AUTORIDADE VISUAL
```

`F-016-A = RESOLVED` após cleanup 119/119, reconciliação, Semantic #832, Mechanical #1090 e prova read-only pós-delete v2. Nomes `.svg` remanescentes em documentos preservados são proveniência histórica qualificada, não arquivos disponíveis.''')
replace_section('docs/index.md','Próximo movimento','''O próximo eixo prioritário permanece `F-016 — desmaterialização documental repo-wide`.

A subfrente física foi encerrada:

```text
F-016-A
→ RESOLVED
→ 119/119 SVGs REMOVED
→ PHYSICAL SVG COUNT = 0
→ LIVE REFERENCES = 0
```

A próxima subfrente é exclusivamente documental: classificar produtores de low-fidelity, documentos de validação/programação, ciclo `UXA-081..085`, galerias e demais materializações sem presumir remoção.

A documentação continua responsável por conteúdo, estados, regras, comportamento, permissões, fluxos, relações, requisitos, restrições, critérios de aceite e handoff. Wireframes, mockups, protótipos, layout, composição e materialização final pertencem exclusivamente a Design.

Isso **não** libera J/K/L/M/N, `UXA-102/V5`, Design em execução, Product Engineering ou merge da PR #363.''')

# Current state
fm_set('docs/project/current-state-register.md','version','3.11.0')
replace_section('docs/project/current-state-register.md','2. Estado executivo','''```text
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
→ PRE-CLEANUP STRUCTURAL + SEMANTIC ELIGIBILITY PROVEN
→ HUMAN PHYSICAL CLEANUP AUTHORIZATION GRANTED
→ PHYSICAL CLEANUP APPLIED 119/119
→ PHYSICAL SVG COUNT = 0
→ LIVE EMBEDS / LINKS = 0
→ HISTORICAL PROVENANCE PRESERVED
→ SEMANTIC #832 SUCCESS
→ MECHANICAL #1090 SUCCESS
→ INDEPENDENT POST-DELETE READ-ONLY PROOF V2 SUCCESS
→ RESOLVED

NEXT F-016 SUBFRONT
→ CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES INDIVIDUALLY
→ NO AUTOMATIC MARKDOWN DELETION

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

O encerramento de `F-016-A` remove a camada física SVG do GKR, mas não promove maturidade funcional, não cria Design e não libera implementação.''')
replace_section('docs/project/current-state-register.md','26. Auditoria integral do corpus — estado corrente','''`GKR-FULL-CORPUS-AUDIT-001 v1.11.0` está ativo como instrumento temporário de execução.

```text
A / B / C / D / E / F / G
→ COMPLETED

H / I
→ AUDITED / UPDATE_APPLIED
→ F-006 RESOLVED
→ F-007 RESOLVED

F-016
→ OPEN

F-016-A
→ RESOLVED
→ PHYSICAL SVG COUNT = 0

F-016 REMAINING MARKDOWN FAMILIES
→ CLASSIFICATION / REWRITE / ABSORPTION AUDIT PENDING

J–N
→ PENDING / NOT RELEASED AUTOMATICALLY

O
→ PENDING / HOLD

P
→ PENDING

Q
→ BLOCKED
```

O encerramento de `F-016-A` não libera automaticamente J–N. `F-016` permanece o eixo prioritário de auditoria.''')
replace_section('docs/project/current-state-register.md','29. Próximo ato governado','''O eixo corrente permanece `F-016`, com a camada física `F-016-A` já encerrada.

```text
F-016-A
→ RESOLVED
→ PHYSICAL SVG COUNT = 0

NEXT
→ CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES
→ PRESERVE FUNCTIONAL CONTENT
→ REWRITE OR ABSORB BEFORE ANY DOCUMENT DELETION
→ VALIDATE EACH RESULTING HEAD

J / K / L / M / N
→ NOT RELEASED AUTOMATICALLY

O
→ PENDING / HOLD

Q
→ BLOCKED

AINDA BLOQUEADOS
→ UXA-102
→ PRIMEIRA TELA PÓS-HOME DA PESSOA
→ WIREFRAME / FIGMA / UI / PROTÓTIPO
→ NOVOS SOURCE LOCKS OPERACIONAIS DE DESIGN
→ DESIGN AUTOMÁTICO
→ PRODUCT ENGINEERING
→ PMF
→ IMPLEMENTAÇÃO
```

Nenhuma autorização de cleanup Markdown é inferida do fechamento de F-016-A.''')

# Roadmap
fm_set('docs/roadmap.md','id','ROADMAP-13.11.0'); fm_set('docs/roadmap.md','version','13.11.0')
s=read('docs/roadmap.md').replace('GKR-STATE-001 v3.10.0','GKR-STATE-001 v3.11.0')
s=replace_once(s,'`F-016-A` provou, no head `549fe10...`, que os 119 SVGs físicos possuem cobertura de rastreabilidade, referência textual e receiver funcional corrente, sem dependência runtime/código. A camada física está `CLEANUP_ELIGIBILITY_PROVEN`, mas **PHYSICAL_CLEANUP_NOT_AUTHORIZED**.','`F-016-A` concluiu o ciclo governado: elegibilidade estrutural/semântica, autorização humana separada, cleanup físico 119/119, reconciliação, Semantic #832, Mechanical #1090 e prova read-only pós-delete v2. A subfrente está `RESOLVED` e o inventário físico corrente de SVGs é zero.','road intro F016A')
write('docs/roadmap.md',s)
replace_section('docs/roadmap.md','2. Baseline governada','''| Elemento | Estado vigente |
|---|---|
| Era | **GE-2 — Knowledge** |
| Estado global | **GKR-STATE-001 v3.11.0** |
| Auditoria integral | **IN_PROGRESS** |
| Baseline final pós-auditoria | **NOT AUTHORIZED** |
| Marco funcional | **M7.88** |
| Última UXA funcional numerada | **UXA-101** |
| UXA-102/V5 | **NOT_STARTED** |
| Product Engineering | **PAUSED BEFORE W0-01** |
| PMF | **NOT VALIDATED** |
| Fundação | **RECONCILED / ENRICHED IN LOT C** |
| Public Canon | **GOG-001 v5.3.0** |
| Bloco G — Jornada da Pessoa | **COMPLETED / UPDATE_APPLIED; JOURNEY REMAINS DRAFT** |
| Bloco H — Organização / Coletivo | **AUDITED / UPDATE_APPLIED / F-006 RESOLVED** |
| Bloco I — Registries / Catálogos / SVGs | **AUDITED / UPDATE_APPLIED / F-006 RESOLVED / F-007 RESOLVED** |
| F-010 | **RESOLVED** |
| F-016 | **OPEN — REPO-WIDE DOCUMENTATION DEMATERIALIZATION** |
| F-016-A | **RESOLVED — PHYSICAL SVG COUNT 0** |
| O/C atores, autoridades e jobs | **DEFINED / ACTIVE** |
| O/C Arquitetura da Informação | **DEFINED PRE-SURFACE-MAP / ACTIVE** |
| O/C mapa de superfícies | **NOT CANONICAL** |
| Design das Homes | **OPERATIONAL AUTHORIZATION SUSPENDED DURING AUDIT** |
| Primeira tela autenticada pós-Home da Pessoa | **BLOCKED UNTIL AUDIT CLOSES** |

Inventário físico corrente após F-016-A:

- **0 SVGs físicos**;
- **0 associações físicas correntes**;
- **34 perfis de rastreabilidade preservados como proveniência/semântica**;
- **0 embeds/links vivos** para assets removidos.

Contagens agregadas de wireframes vigentes/validados permanecem `NOT_CERTIFIED`; ausência de SVG no GKR não constitui maturidade de Design.''')
replace_section('docs/roadmap.md','13. Lote I — Registries, catálogos e materializações','''Estado do Bloco 2:

```text
AUDITED / UPDATE_APPLIED
F-006 → RESOLVED
F-007 → RESOLVED NO LIMITE SEMÂNTICO/INVENTÁRIO
F-016 → OPEN
F-016-A → RESOLVED
```

Inventário físico corrente comprovado após F-016-A:

- **0 SVGs físicos**;
- **0 associações físicas correntes**;
- **34 perfis de rastreabilidade preservados como proveniência/semântica**;
- **0 dependências runtime/código**;
- **0 embeds/links vivos** para assets removidos.

A prova pré-delete confirmou receivers textuais para 32/32 perfis físicos e referência em Experience Architecture para 119/119 assets; a prova pós-delete v2 confirmou ausência física e segurança das referências no head `cde46281a99ac9746fcca11381c3b8e54d284f23`.

```text
CONTAGEM FÍSICA DE SVGs
≠ WIREFRAMES VIGENTES
≠ WIREFRAMES VALIDADOS
```

As famílias Markdown de materialização permanecem sob F-016 e devem ser classificadas individualmente antes de qualquer remoção ou reescrita.''')
replace_section('docs/roadmap.md','26. Regra do próximo movimento','''`F-016-A` está `RESOLVED`.

```text
F-016-A
→ PHYSICAL CLEANUP APPLIED 119/119
→ PHYSICAL SVG COUNT = 0
→ SEMANTIC #832 SUCCESS
→ MECHANICAL #1090 SUCCESS
→ INDEPENDENT READ-ONLY PROOF V2 SUCCESS
→ RESOLVED

NEXT F-016 SUBFRONT
→ CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES
→ KEEP_FUNCTIONAL | REWRITE_FUNCTIONAL | REMOVE_AFTER_ABSORPTION | REMOVE | HISTORICAL_PROVENANCE_ONLY
→ NO AUTOMATIC MARKDOWN DELETION
```

J/K/L/M/N, `UXA-102/V5`, Design, Product Engineering e merge da PR #363 permanecem bloqueados ou não autorizados.''')

# Full audit
fm_set('docs/project/gkr-full-corpus-audit.md','version','1.11.0')
s=read('docs/project/gkr-full-corpus-audit.md')
s=s.replace('| I — Registries / Catálogos / SVGs | `AUDITED / UPDATE_APPLIED / F-006_RESOLVED / F-007_RESOLVED` | inventário pós-F-006 = 119 SVGs; F-016-A cleanup-eligible, remoção física ainda não autorizada |','| I — Registries / Catálogos / SVGs | `AUDITED / UPDATE_APPLIED / F-006_RESOLVED / F-007_RESOLVED / F-016-A_RESOLVED` | camada SVG removida; inventário físico corrente = 0; demais famílias F-016 continuam abertas |',1)
s=s.replace('F-016. desmaterialização documental              [aberta; F-016-A cleanup-eligible / physical cleanup not authorized]','F-016. desmaterialização documental              [aberta; F-016-A resolved; famílias Markdown pendentes]',1)
# Historical F-006 passage is explicitly marked as an old checkpoint rather than current truth.
s=s.replace('Registries, galleries e a matriz de rastreabilidade ainda preservam referências aos dois SVGs porque o inventário físico atual continua sendo 121. Essas referências descrevem **presença física/histórica**, não autoridade funcional. Elas deverão ser removidas ou recalculadas na mesma transação de cleanup físico para que o inventário continue verdadeiro.','No checkpoint pré-cleanup de F-006, registries, galleries e a matriz ainda preservavam referências aos dois SVGs e o inventário físico era 121. Esse trecho é **proveniência do estado anterior**; F-006 foi posteriormente executado e resolvido.',1)
s=s.replace('Consequência do teste positivo:\n\n```text\nF-006\n→ OPEN\n→ ABSORPTION_APPLIED\n→ ACTIVE_FUNCTION_DEPENDENCIES_RECONCILED\n→ CLEANUP_ELIGIBILITY_PROVEN\n→ PHYSICAL_REMOVAL_NOT_AUTHORIZED\n```\n\nA elegibilidade não equivale a cleanup concluído. Antes de qualquer remoção física ainda é obrigatório:','Consequência naquele checkpoint pré-cleanup:\n\n```text\nF-006\n→ OPEN / CLEANUP_ELIGIBLE / PHYSICAL_REMOVAL_NOT_AUTHORIZED\n→ HISTORICAL CHECKPOINT ONLY\n```\n\nA sequência então exigida — e posteriormente concluída — era:',1)
write('docs/project/gkr-full-corpus-audit.md',s)
replace_section('docs/project/gkr-full-corpus-audit.md','22. Estado atual','''```text
AUDIT
→ IN_PROGRESS

A / B / C / D / E / F / G
→ COMPLETED

H / I
→ AUDITED / UPDATE_APPLIED
→ F-006 RESOLVED
→ F-007 RESOLVED NO LIMITE SEMÂNTICO/INVENTÁRIO

F-016
→ OPEN / REPO-WIDE DOCUMENTATION DEMATERIALIZATION

F-016-A
→ PRE-CLEANUP ELIGIBILITY PROVEN
→ HUMAN AUTHORIZATION GRANTED
→ PHYSICAL CLEANUP APPLIED 119/119
→ PHYSICAL SVG COUNT = 0
→ LIVE EMBED/LINK HITS = 0
→ HISTORICAL PROVENANCE PRESERVED
→ SEMANTIC #832 SUCCESS
→ MECHANICAL #1090 SUCCESS
→ INDEPENDENT POST-DELETE READ-ONLY PROOF V2 SUCCESS
→ RESOLVED

F-016 REMAINING MARKDOWN FAMILIES
→ CLASSIFICATION / REWRITE / ABSORPTION PENDING

NEXT SPECIALIZED BLOCK J/K/L/M/N
→ NOT RELEASED YET

BASELINE FINAL
→ NOT AUTHORIZED

CORPUS CLEANUP
→ NOT YET COMPLETE

DESIGN / MATERIALIZATION
→ NOT AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

MENU FINAL
→ NOT YET DESIGNED
```''')
replace_section('docs/project/gkr-full-corpus-audit.md','F-016 — Desmaterialização documental repo-wide','''A auditoria mantém a fronteira estrutural obrigatória:

```text
GKR
→ intenção, conteúdo, informação, estados, regras, comportamento, permissões, fluxos, relações, requisitos, restrições, critérios e handoff

DESIGN
→ composição visual, layout, posicionamento, wireframes, mockups, protótipos, componentes visuais, aparência e materialização final
```

### F-016-A — camada física SVG — RESOLVED

```text
PRE-DELETE PHYSICAL SVGs
→ 119

POST-DELETE PHYSICAL SVGs
→ 0

LIVE EMBEDS / LINKS
→ 0

PRE-CLEANUP STRUCTURAL + SEMANTIC ELIGIBILITY
→ PASS

HUMAN AUTHORIZATION
→ GRANTED / CONSUMED

SEMANTIC #832
→ SUCCESS

MECHANICAL #1090
→ SUCCESS

POST-DELETE READ-ONLY PROOF V2
→ SUCCESS

F-016-A
→ RESOLVED
```

Nomes `.svg` preservados em documentos históricos permanecem somente como proveniência. Galerias e matriz por SVG são `superseded / historical_provenance_only`, sem autoridade visual corrente.

### Demais famílias F-016

Documentos `low-fidelity-wireframe`, `materialization`, validações/programas de wireframe, ciclo de galerias e linguagem de UI continuam sujeitos à classificação individual:

- `KEEP_FUNCTIONAL`;
- `REWRITE_FUNCTIONAL`;
- `REMOVE_AFTER_ABSORPTION`;
- `REMOVE`;
- `HISTORICAL_PROVENANCE_ONLY`.

Nenhum Markdown é removido automaticamente pelo fechamento de F-016-A. Critério global: **o GKR não pode competir com Design na definição de interface**.''')

# Derived O/C audit
fm_set('docs/experience-architecture/organizations-collectives-derived-state-audit.md','version','1.2.0'); fm_set('docs/experience-architecture/organizations-collectives-derived-state-audit.md','last_updated',TODAY)
replace_section('docs/experience-architecture/organizations-collectives-derived-state-audit.md','2. Resultado executivo','''```text
UXA-015..018
→ REMOVIDOS DO CORPUS CORRENTE POR F-006
→ PROVENIÊNCIA PRESERVADA NO HISTÓRICO GIT

JOBS AUTENTICADOS O/C
→ DEFINIDOS

ARQUITETURA DA INFORMAÇÃO AUTENTICADA O/C
→ DEFINIDA PRÉ-SURFACE-MAP

MAPA FINAL DE SUPERFÍCIES
→ PENDENTE

WIREFRAMES PRINCIPAIS AUTENTICADOS
→ PENDENTES / AUTORIDADE DE DESIGN

F-016-A
→ RESOLVED
→ PHYSICAL SVG COUNT = 0
```

## 3. Matriz de divergências e estado atual

| Derivado | Snapshot anterior | Estado correto atual | Situação da normalização |
|---|---|---|---|
| `GKR-STATE-001` | `121 SVGs — 121 validados / 0 pendentes` | camada física removida; maturidade não inferida | normalizado |
| `GKR-JOURNEY-SCREEN-CATALOG-001` | inventário físico 121/119 em checkpoints anteriores | **0 SVGs físicos após F-016-A** | normalizado |
| `GKR-JOURNEY-SCREEN-GALLERY-001` | leitura agregada de validação | `superseded / historical_provenance_only` | normalizado |
| `GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001` | associação visual podia ser lida como vigência | **0 associações físicas / 34 perfis de proveniência** | normalizado |
| `GKR-JOURNEY-SURFACE-REGISTRY-001` — `ORG-001` | Visão Geral validada por `UXA-015/017` | responsabilidade conhecida; materialização histórica removida; Design governa futura materialização | normalizado |
| registro do Coletivo | `UXA-016/018` como evidência da UX principal | não utilizar esses IDs para afirmar wireframe principal vigente | normalizado |
| Jornada da Organização | Visão Geral = validada | Jobs + IA existem; mapa funcional ainda não canônico; materialização pertence a Design | normalizado |
| Jornada do Coletivo | `UXA-016/018` como evidência principal | Jobs + IA existem; mapa funcional ainda não canônico; materialização pertence a Design | normalizado |''')
# remove obsolete consequence paragraph and sync gate/final state
s=read('docs/experience-architecture/organizations-collectives-derived-state-audit.md')
s=s.replace('> **Os testes de absorção e função atual estão concluídos e a elegibilidade documental de cleanup foi comprovada. `F-006` permanece aberto, e qualquer remoção física continua condicionada a autorização humana separada e explícita.**','> **F-006 está resolvido. F-016-A também está resolvido; futuras remoções Markdown dependem de classificação e autorização próprias.**',1)
s=s.replace('Para `F-016-A`, os 119 SVGs físicos estão `CLEANUP_ELIGIBILITY_PROVEN`, mas `PHYSICAL_CLEANUP_NOT_AUTHORIZED`.','Para `F-016-A`, o cleanup 119/119 foi aplicado e validado; a contagem física corrente é zero e a subfrente está `RESOLVED`.',1)
s=s.replace('F-016-A\n→ 119 SVGs\n→ CLEANUP_ELIGIBILITY_PROVEN\n→ PHYSICAL_CLEANUP_NOT_AUTHORIZED','F-016-A\n→ PHYSICAL_CLEANUP_APPLIED_119_OF_119\n→ PHYSICAL_SVG_COUNT_0\n→ POST_DELETE_PROOF_V2_SUCCESS\n→ RESOLVED',1)
write('docs/experience-architecture/organizations-collectives-derived-state-audit.md',s)

# Specialized homes reconciliation
fm_set('docs/experience-architecture/public-specialized-homes-reconciliation.md','version','1.1.0'); fm_set('docs/experience-architecture/public-specialized-homes-reconciliation.md','last_updated',TODAY)
s=read('docs/experience-architecture/public-specialized-homes-reconciliation.md')
s=s.replace('F-016-A\n→ CLEANUP_ELIGIBILITY_PROVEN\n→ PHYSICAL_CLEANUP_NOT_AUTHORIZED','F-016-A\n→ RESOLVED\n→ PHYSICAL_SVG_COUNT = 0')
s=s.replace('NEXT PHYSICAL GATE\n→ SEPARATE EXPLICIT HUMAN AUTHORIZATION FOR F-016-A','NEXT F-016 GATE\n→ CLASSIFY REMAINING MARKDOWN MATERIALIZATION FAMILIES')
write('docs/experience-architecture/public-specialized-homes-reconciliation.md',s)

# UXA index
fm_set('docs/experience-architecture/uxa-047-101-index.md','version','3.11.0')
s=read('docs/experience-architecture/uxa-047-101-index.md')
s=s.replace('GKR-STATE-001\n→ 3.10.0','GKR-STATE-001\n→ 3.11.0')
s=s.replace('| F-016-A — camada física SVG | **PHYSICAL CLEANUP APPLIED 119/119 / PHYSICAL SVG COUNT 0 / POST-CLEANUP VALIDATION PENDING** |','| F-016-A — camada física SVG | **RESOLVED / PHYSICAL CLEANUP 119/119 / PHYSICAL SVG COUNT 0 / POST-DELETE PROOF V2 SUCCESS** |')
write('docs/experience-architecture/uxa-047-101-index.md',s)

# Experience Architecture index
fm_set('docs/experience-architecture/index.md','version','1.7.0')
s=read('docs/experience-architecture/index.md')
anchor='A remoção física não altera por si só maturidade funcional de superfícies, estados ou transições. Nomes `.svg` ainda citados em documentos preservados devem ser lidos exclusivamente como proveniência histórica.'
replacement=anchor+'\n\n`F-016-A = RESOLVED` após Semantic #832, Mechanical #1090 e prova read-only pós-delete v2. `F-016` global permanece aberto para as famílias documentais remanescentes.'
s=replace_once(s,anchor,replacement,'EA closure sentence')
write('docs/experience-architecture/index.md',s)

# Journeys index
fm_set('docs/journeys/index.md','version','0.43.0')
s=read('docs/journeys/index.md')
s=s.replace('| visão geral das Jornadas Integradas | `active` 0.42.0 |','| visão geral das Jornadas Integradas | `active` 0.43.0 |',1)
s=s.replace('| F-016-A | `physical_cleanup_applied / validation_in_progress` | **119/119 SVGs removidos; 0 SVGs físicos; referências vivas reconciliadas; fechamento formal pendente de prova pós-delete** |','| F-016-A | `resolved` | **119/119 SVGs removidos; 0 SVGs físicos; referências vivas reconciliadas; Semantic #832 + Mechanical #1090 + prova pós-delete v2 SUCCESS** |',1)
write('docs/journeys/index.md',s)

# Screen catalog current physical sections; preserve the D5 historical snapshot section.
fm_set('docs/journeys/screen-catalog.md','version','0.34.0'); fm_set('docs/journeys/screen-catalog.md','last_updated',TODAY)
s=read('docs/journeys/screen-catalog.md')
s=s.replace('| **Total físico do catálogo** |  | **119** | **maturidade agregada não pode ser inferida; recomputação governada pendente** |  |  |','| **Total físico do catálogo** |  | **0** | **camada SVG removida por F-016-A; maturidade funcional preservada por autoridade textual** |  |  |',1)
s=s.replace('| catálogo físico | **119 SVGs** | `active` 0.33.0; inclui artefatos históricos superseded |','| catálogo físico | **0 SVGs** | `active` 0.34.0; camada física removida por F-016-A |',1)
s=s.replace('| matriz de rastreabilidade | **119 associações físicas / 34 perfis estáveis** | associação ≠ autoridade vigente |','| matriz de rastreabilidade | **0 associações físicas / 34 perfis de proveniência** | sem autoridade visual |',1)
s=s.replace('| galeria visual | **119 SVGs físicos** | resumo global `121 validados / 0 pendentes` superseded como claim de maturidade |','| galeria visual | **0 SVGs físicos** | documentos de galeria preservados somente como proveniência histórica |',1)
s=s.replace('Essas contagens descrevem cobertura física/associativa do snapshot e não resolvem a vigência de cada artefato após supersessões posteriores.','Essas contagens de IDs descrevem o snapshot estrutural/histórico. A camada física SVG corrente é zero após F-016-A.',1)
write('docs/journeys/screen-catalog.md',s)

# Integrated gallery is provenance only: remove current-presence wording, preserve historic 119 fact.
fm_set('docs/journeys/screen-gallery.md','version','0.27.0')
replace_section('docs/journeys/screen-gallery.md','1. Finalidade','''Este documento preserva a **proveniência histórica da galeria que, antes de F-016-A, reunia 119 SVGs físicos** para inspeção humana de sequência, coerência e cobertura.

Após F-016-A, nenhum desses SVGs existe no corpus vigente. O documento permanece somente como `historical_provenance_only`; nomes e contagens abaixo descrevem snapshots anteriores e não arquivos disponíveis.''')
replace_section('docs/journeys/screen-gallery.md','2. Estado do instrumento','''A galeria está `superseded / historical_provenance_only`.

```text
SVGs FÍSICOS CORRENTES
→ 0

AUTORIDADE VISUAL CORRENTE
→ DESIGN

CONTEÚDO DESTE DOCUMENTO
→ PROVENIÊNCIA HISTÓRICA
```

As referências a `121`, `119`, estados low-fidelity e maturidades locais abaixo pertencem aos respectivos checkpoints históricos. Elas não reativam assets, não promovem wireframes e não restringem futura decisão de Design.''')

# Traceability matrix: heading and current state.
fm_set('docs/journeys/screen-gallery-traceability-matrix.md','version','0.27.0')
s=read('docs/journeys/screen-gallery-traceability-matrix.md')
s=s.replace('## 4. Associação individual dos 119 SVGs físicos remanescentes','## 4. Associação histórica dos 119 SVGs físicos removidos por F-016-A',1)
write('docs/journeys/screen-gallery-traceability-matrix.md',s)

print('F016A_CLOSURE_ADJUDICATION_TRANSFORMATION=PASS')
