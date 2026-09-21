---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 1.0.3
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
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

A continuidade publicação → descoberta → Mapa/Lista → Detalhe está governada pelas autoridades correntes.

Permanece fora da autoridade da Guivos:

```text
DETALHE
→ REVISÃO CONSCIENTE
→ FRONTEIRA EXTERNA
→ PROCESSO DO TERCEIRO
```

A Guivos governa até a transferência consciente de autoridade. O comportamento e o resultado posteriores pertencem ao terceiro.

Integrações orgânico–patrocinado permanecem limitadas à maturidade registrada para `TRN-304..306`.

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
