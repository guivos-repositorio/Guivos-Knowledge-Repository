---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 1.0.30
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-04
related:
  - GKR-UX-G5-OPPORTUNITY-BOOST-VALIDATION-001
  - GKR-UX-G4-INTERNAL-OPPORTUNITY-PROCESS-VALIDATION-001
  - GKR-UX-G3-ORGANIZATION-COLLECTIVE-RELATIONSHIP-VALIDATION-001
  - GKR-UXA-106-G2-SCOPE-EXAM-001
  - GKR-UXA-106-G2-FUNCTIONAL-EXAM-001
  - GKR-UXA-106-G2-MATURITY-EXAM-001
  - GKR-UX-G2-COLLECTIVE-DISCOVERY-REQUEST-VALIDATION-001
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-UXA-103-TRN005-FUNCTIONAL-EXAM-001
  - GKR-UXA-103-TRN005-MATURITY-EXAM-001
  - GKR-UX-EVALUATION-REPUTATION-AUTHORITY-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-BUSINESS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
  - GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001
  - GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Finalidade

Este documento registra **somente lacunas correntes** de continuidade da experiência e os limites que ainda exigem autoridade, evidência ou materialização própria.

Uma lacuna registrada aqui:

- não autoriza execução automática;
- não reduz a maturidade das autoridades já concluídas;
- não transforma ausência visual em ausência funcional;
- não permite completar estados ou transições por inferência.

## 2. Pessoa

A Jornada da Pessoa possui topologia corrente, Screen Catalog, Surface Registry e Transition Registry ativos.

As continuidades ainda parciais devem ser lidas diretamente no `GKR-JOURNEY-TRANSITION-REGISTRY-001`. Entre as fronteiras ainda não fechadas ponta a ponta estão:

- integrações iniciais entre Home pública, entrada protegida, expressão, inventário e processamento quando marcadas como parciais no Registry;
- estados alternativos/sensíveis ainda não governados por autoridade específica;
- Conta/Configurações quando uma materialização própria for necessária;
- integrações comerciais patrocinadas que permaneçam parciais.

As ligações `Hoje ↔ Meus Objetivos`, `Hoje ↔ Meus Próximos Passos` e `Hoje ↔ Minha Evolução` não constituem lacuna corrente de continuidade básica.

## 2.1 Avaliação e Reputação — lacunas de materialização

A autoridade semântica de Avaliação e Reputação passa a ser `GKR-UX-EVALUATION-REPUTATION-AUTHORITY-001`, mas a materialização de superfícies e handoffs permanece deliberadamente aberta onde o Registry não comprova responsabilidade suficiente.

Lacunas correntes:

- **entrada contextual para avaliar**: `PER-108` e `PER-203` podem ser origens candidatas somente mediante extensão explícita de seus contratos; outros objetos exigem origem comprovada;
- **registro protegido da avaliação (R-A)**: responsabilidade adjudicada por `GKR-UX-EVALUATION-REPUTATION-SURFACE-RESPONSIBILITY-ADJUDICATION-001`; materialização física/`GKR-SURF-*` ainda não criada;
- **continuidade da autora / “Minhas Avaliações” (R-B)**: responsabilidade adjudicada; `PER-009` permanece apenas possível ponto administrativo de acesso mediante extensão expressa e não autoridade canônica;
- **exibição pública contextual**: continua dependente de extensão explícita por objeto; `PER-103` e `PER-203` não recebem publicação por analogia, e Organização, atividade, curso/programa e relação institucional continuam sem detalhe público presumido;
- **resposta e contestação do responsável (R-C)**: responsabilidade adjudicada; `COL-002` e `ORG-001` permanecem apenas possíveis entradas administrativas mediante extensão expressa e mandato comprovado;
- **denúncia, moderação e recurso (R-D)**: responsabilidade adjudicada como governança especializada; materialização física, política operacional e instâncias concretas permanecem abertas;
- **relação Organização↔Coletivo**: avaliação reputacional permanece separada de `ORG-005/COL-008` e de `UXA-019`; negociação bilateral não autoriza publicação reputacional;
- **handoffs UXA-057**: nenhum novo `GKR-TRN-*` é criado enquanto origem, destino, autoridade, retorno, falha e idempotência não estiverem comprovados.

```text
AUTORIDADE DE DOMÍNIO RESOLVIDA
≠ SUPERFÍCIE MATERIALIZADA
≠ TRANSIÇÃO MATERIALIZADA
≠ DESIGN LIBERADO
≠ ENGENHARIA LIBERADA
```

## 2.2 UXA-102 / V5 — lacunas pós-adjudicação transversal

A autoridade transversal corrente é `GKR-UXA-102-V5-AUTHORITY-001`.

O exame de V5 não promove maturidade e não cria transições. Permanecem abertas cinco famílias de lacuna:

1. **G1 — primeira entrada, expressão e inventário**: refinada por `GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001`, UXA-103, UXA-104 e UXA-105; `TRN-001`, `TRN-003/004/005` e `TRN-014..017` estão localmente validadas; a lacuna local de continuidade público → protegido foi fechada por UXA-105; a cadeia completa, porém, **continua não integralmente validada**;
2. **G2 — descoberta e solicitação de Coletivo**: refinada por `GKR-UX-G2-COLLECTIVE-DISCOVERY-REQUEST-VALIDATION-001`; UXA-106 concluiu o maturity exam e adjudicou a elegibilidade de `TRN-102/103/104` para `LOCALLY VALIDATED`; a materialização das promoções permanece pendente e a maturidade operativa corrente continua `partial` e `TRN-114` permanece `contracted` até maturidade/materialização de `COL-003/004`; `TRN-101` permanece localmente validada;
3. **G3 — Organização e relação O↔C**: refinada por `GKR-UX-G3-ORGANIZATION-COLLECTIVE-RELATIONSHIP-VALIDATION-001`; concorrência, retorno, estado indeterminado e idempotência deixam de ser lacuna genérica; `TRN-201` permanece `partial`, `TRN-202` permanece localmente validada e `TRN-206..209` permanecem `contracted` por ausência de validação ponta a ponta/materialização das autoridades bilaterais;
4. **G4 — processo interno de oportunidade**: refinada por `GKR-UX-G4-INTERNAL-OPPORTUNITY-PROCESS-VALIDATION-001`; `TRN-212` e `TRN-214` permanecem `contracted`, retornos `PER-204 → PER-203` e `ORG-008 → ORG-003` permanecem contextuais sem IDs dedicados, e as lacunas correntes são validação ponta a ponta + maturidade/materialização dos contratos de `PER-204/ORG-008`;
5. **G5 — Opportunity Boost**: refinada por `GKR-UX-G5-OPPORTUNITY-BOOST-VALIDATION-001`; falha, estado indeterminado, retry e idempotência deixam de ser lacuna genérica; `TRN-301/302/304/305/306` permanecem `partial`, `TRN-303` permanece localmente validada, e continuam abertas integração ponta a ponta + operacionalização econômica sem autorização para inventar cobrança, mensuração ou deduplicação técnica.

Regras transversais adjudicadas aplicam-se onde cabível:

```text
ATTEMPT ≠ SUCCESS
UNKNOWN ≠ FAILURE
RETURN ≠ ROLLBACK
RETRY → RECONCILE FIRST WHEN NEEDED
STALE CLIENT ≠ CANONICAL AUTHORITY
BOUNDARY ≠ EXTERNAL RESULT CONFIRMED
```

Essas regras não convertem gap em transição validada.

## 3. Oportunidades e fronteiras externas

A continuidade publicação → descoberta → Mapa/Lista → Detalhe está governada pelas autoridades correntes. A entrada institucional `ORG-001 → ORG-002` permanece separadamente parcial em `TRN-201`; o contrato funcional do cadastro existe, mas a ligação ponta a ponta com a visão institucional ainda não está fechada.

Permanece fora da autoridade da Guivos:

```text
DETALHE
→ REVISÃO CONSCIENTE
→ FRONTEIRA EXTERNA
→ PROCESSO DO TERCEIRO
```

A Guivos governa até a transferência consciente de autoridade. O comportamento e o resultado posteriores pertencem ao terceiro.

Opportunity Boost preserva maturidade parcial nas ligações `TRN-301`, `TRN-302`, `TRN-304`, `TRN-305` e `TRN-306`. Isso inclui ativação/gestão de campanha, projeção em unidade patrocinada, integração com descoberta orgânica e estados residuais; nenhuma dessas ligações é promovida além do estado registrado no Transition Registry.

## 4. Planos, cobrança e contratação assistida

A arquitetura documental de Planos existe para **Pessoa, Coletivo, Organização e Guivos Business**. Pessoa, Coletivo e Organização possuem superfícies granulares neste Registry; Business possui continuidade própria governada por suas autoridades e por `docs/journeys/business.md`, sem IDs granulares próprios neste momento.

Permanecem fora da maturidade corrente quando não houver autoridade específica:

- gateway e cobrança real;
- proration;
- liquidação e condições fiscais;
- proposta/contrato após `BND-002`;
- dimensionamento assistido posterior à fronteira;
- handoffs operacionais de contratação ainda não formalizados.

`BND-002` continua sendo fronteira genérica de contratação/dimensionamento assistido para os fluxos aplicáveis de **Coletivo e Organização**. Ele não corresponde a um plano específico e **não governa a contratação do Guivos Business**.

Guivos Business permanece produto especializado separado:

```text
GUIVOS BUSINESS
→ CONTRATAÇÃO ONLINE
→ SELF-SERVICE QUANDO ELEGÍVEL
→ SUPORTE QUANDO NECESSÁRIO
→ GERENCIADO QUANDO A COMPLEXIDADE EXIGIR

BND-002
→ NÃO É FLUXO BUSINESS
```

A composição Self-service e seus fatores de plano/valor são governados por `GPA-004` e `docs/plans/business.md`, sem criação de IDs Business neste registry.

### Lacunas correntes específicas de Business

Permanecem abertas somente quando não houver autoridade própria formalizada:

- thresholds quantitativos e entitlements finais entre Start, Growth, Scale e Enterprise;
- preços unitários/faixas de componentes variáveis ainda não governados;
- implementação técnica do configurador;
- checkout, cobrança, tributação e liquidação reais;
- critérios operacionais exatos de roteamento entre Self-service, suporte e gerenciado;
- implementação das integrações/API/exportações contratadas;
- implementação e publicação operacional da experiência Business.

Essas lacunas não convertem Business em Organização, não remetem automaticamente a `BND-002` e não criam uma camada "Comercial".

## 5. Organização e Coletivo autenticados

A cadeia corrente está documentalmente fechada até a autorização de Design high-fidelity e o release separado de execução externa:

```text
JOBS / AUTORIDADE
→ INFORMATION ARCHITECTURE
→ SURFACE MAP
→ STATE MAP
→ PRIORITY FLOWS
→ NAVIGATION MATERIALIZATION
→ LOW-FIDELITY DELIVERY
→ LOW-FIDELITY VALIDATION
→ HIGH-FIDELITY ELIGIBILITY
→ HIGH-FIDELITY AUTHORIZATION
→ HIGH-FIDELITY EXECUTION RELEASE
```

Estado corrente:

```text
O/C HIGH-FIDELITY DESIGN
→ AUTHORIZATION GRANTED
→ EXECUTION RELEASE ISSUED
→ EXTERNAL DELIVERY NOT_RECEIVED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

UXA-102 / V5
→ TRANSVERSE CONTRACT ADJUDICATED
→ 76/76 TRANSITIONS EXAMINED
→ G1–G5 REFINED
→ NO GENERIC V5 GAP REMAINS

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

Portanto, **Navigation Materialization, wireframe principal low-fidelity e sua validação não são lacunas correntes**.


### 5.1 Lacunas especializadas que permanecem abertas

O fechamento da cadeia principal autenticada **não** significa que todas as capacidades especializadas de Organização e Coletivo estejam materializadas ou validadas ponta a ponta.

Permanecem abertas, conforme os Surface Registries e contratos correntes:

- `TRN-102..104`: descoberta de Coletivo → perfil público → revisão/solicitação → estado pendente — superfícies e contrato funcional existem sob `UXA-056`, mas os handoffs continuam parciais e não foram validados ponta a ponta como conjunto;
- `COL-001`: presença pública e entrada coletiva — presença pública governada pelo Master/`UXA-056`, com continuidade autenticada coberta pela arquitetura O/C corrente; a separação final entre presença pública, entrada autenticada e operação interna ainda não está fechada ponta a ponta;
- `ORG-004..006`: proposta, negociação e relação ativa Organização ↔ Coletivo — contratos/lifecycle definidos sob `UXA-019` + Surface/State Map, com cobertura low-fidelity O↔C em `PASS`; materialização dedicada e continuidade ponta a ponta `TRN-206..209` ainda não estão fechadas;
- `Organização ↔ Organização`: necessidade conceitual reconhecida por `UXA-014`, mas sem evidência suficiente para adjudicar superfície, lifecycle ou transições próprias; `ORG-004..006` e `UXA-019` permanecem exclusivos de Organização↔Coletivo, e nenhum novo ID deve ser criado por analogia;
- `ORG-007`: responsabilidades e evidências institucionais — contrato funcional candidato definido em `GKR-UX-ORG-RESPONSIBILITIES-EVIDENCE-MASTER-001`, com responsabilidade e estados mínimos contratados; inventário completo de fontes, regras especializadas, transições, implementação e validação ponta a ponta permanecem abertos;
- `COL-004`: gestão de vínculo — contrato corrente com cobertura low-fidelity parcial em Participação; materialização dedicada e continuidade ponta a ponta ainda não estão comprovadas;
- `COL-005`: comunicação oficial do Coletivo — contrato corrente com cobertura low-fidelity parcial em Participação/Governança; materialização dedicada e continuidade ponta a ponta ainda não estão comprovadas;
- `COL-006`: atividades, consultas e decisões — contrato corrente com cobertura low-fidelity parcial em Atividades/Governança; materialização dedicada e continuidade ponta a ponta ainda não estão comprovadas;
- `COL-007`: proteção e moderação — contrato corrente com cobertura low-fidelity parcial e `Governança e Proteção = PASS`; materialização dedicada e continuidade ponta a ponta ainda não estão comprovadas;
- `COL-008`: relação Organização ↔ Coletivo — contrato/lifecycle definidos sob `UXA-019`, com cobertura low-fidelity O↔C em `PASS`; materialização dedicada e continuidade ponta a ponta permanecem abertas;
- `Coletivo ↔ Coletivo`: necessidade conceitual reconhecida por `UXA-014`, mas sem evidência suficiente para adjudicar superfície, lifecycle ou transições próprias; `COL-008` e `UXA-019` permanecem exclusivos de Organização↔Coletivo, e nenhum novo ID deve ser criado por analogia;
- capacidades de avaliação/reputação permanecem condicionadas às autoridades correntes aplicáveis e à materialização/validação específica onde o Registry ainda não comprova fechamento;
- referências históricas de `UXA-058` a interações, recomendações, conexões, convite, contato ou mensagem **não constituem lacuna de implementação**: `UXA-058` é proveniência histórica, e qualquer relação bilateral autônoma Pessoa↔Pessoa ou iniciativa genérica Coletivo→Pessoa exige nova evidência canônica e adjudicação própria antes de materialização.

Essas lacunas especializadas não reabrem a cadeia principal autenticada já fechada até `HIGH-FIDELITY EXECUTION RELEASE`; elas devem ser tratadas como frentes funcionais próprias, sem promoção por analogia.

## 6. Regra de continuidade

Nenhuma lacuna acima cria uma fila automática de execução.

```text
CURRENT AUTHORITY
→ PRESERVED

OPEN GAP
→ DOCUMENTED WITHOUT IMPLIED EXECUTION

DESIGN / PROTOTYPE / ENGINEERING
→ ONLY BY THEIR OWN GOVERNED GATE
```
