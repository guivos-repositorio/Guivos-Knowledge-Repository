---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 1.0.8
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-22
related:
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
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Finalidade

Este documento registra **somente lacunas correntes** de continuidade da experiência. Ele não preserva a cronologia de como cada lacuna foi descoberta ou fechada; essa proveniência pertence ao Git.

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

A cadeia corrente está documentalmente fechada até a autorização de Design high-fidelity:

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
```

Estado corrente:

```text
O/C HIGH-FIDELITY DESIGN
→ AUTHORIZED
→ NOT_STARTED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

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
- `ORG-007`: revisão institucional de evidências/resultados — responsabilidade conhecida, com evidência insuficiente para classificar;
- `COL-004`: gestão de vínculo — contrato corrente com cobertura low-fidelity parcial em Participação; materialização dedicada e continuidade ponta a ponta ainda não estão comprovadas;
- `COL-005`: comunicação oficial do Coletivo — contrato corrente com cobertura low-fidelity parcial em Participação/Governança; materialização dedicada e continuidade ponta a ponta ainda não estão comprovadas;
- `COL-006`: atividades, consultas e decisões — contrato corrente com cobertura low-fidelity parcial em Atividades/Governança; materialização dedicada e continuidade ponta a ponta ainda não estão comprovadas;
- `COL-007`: proteção e moderação — contrato corrente com cobertura low-fidelity parcial e `Governança e Proteção = PASS`; materialização dedicada e continuidade ponta a ponta ainda não estão comprovadas;
- `COL-008`: relação Organização ↔ Coletivo — contrato/lifecycle definidos sob `UXA-019`, com cobertura low-fidelity O↔C em `PASS`; materialização dedicada e continuidade ponta a ponta permanecem abertas;
- capacidades de avaliação/reputação e de interações/recomendações/conexões governadas por `UXA-057` e `UXA-058` permanecem dependentes de materialização/validação específica onde o Registry ainda não comprova fechamento.

Essas lacunas especializadas não reabrem a cadeia principal autenticada já fechada até `HIGH-FIDELITY AUTHORIZATION`; elas devem ser tratadas como frentes funcionais próprias, sem promoção por analogia.

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
