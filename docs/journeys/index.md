---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SECTION-CLARIFICATION-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne, por referência, as jornadas da **Pessoa**, do **Coletivo** e da **Organização** para permitir leitura contínua, comparação de perspectivas, inspeção de handoffs e identificação de lacunas.

Ela não substitui contratos, programas, wireframes, validações ou registros canônicos. Em caso de divergência, prevalece o artefato de origem.

## 2. Como utilizar

1. escolha o participante ou cenário;
2. percorra os nós e transições apresentados;
3. confira separadamente maturidade, autoridade, materialização e validação;
4. verifique se a continuidade integrada foi examinada;
5. observe handoffs, retornos, contestações e pontos de interrupção;
6. consulte o catálogo agregado;
7. use os registros granulares para localizar superfícies e transições por ID;
8. acompanhe as lacunas registradas.

## 3. Vistas disponíveis

- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Catálogo de telas](screen-catalog.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e continuidades ausentes](gaps.md)

## 4. Modelo de evidência

Cada nó ou família deve separar, quando aplicável:

| Campo | Significado |
|---|---|
| maturidade primária | um único estado controlado da UXA-070 |
| autoridade contratual | documento que governa a responsabilidade |
| referência materializada | documento, wireframe ou SVG existente |
| evidência de validação | pacote que validou a referência materializada |
| continuidade integrada | validada, parcial, ausente ou não examinada |

```text
cobertura das superfícies
≠ cobertura das transições
≠ validação da jornada integrada
```

## 5. Estado desta seção

| Camada | Estado | Referência |
|---|---|---|
| programa funcional | concluído | UXA-070 |
| primeira materialização documental | integrada | UXA-071 |
| primeira validação funcional | não aprovada até reformulação | UXA-072 |
| reformulação, navegação e sincronização | executadas | UXA-073 |
| nova validação funcional | aprovada com ressalvas no escopo documental | UXA-074 |
| promoção e sincronização pós-validação | executadas seletivamente | UXA-075 |
| registro granular de superfícies e transições | materializado em `draft` | UXA-076 |
| validação dos registros granulares | não iniciada | UXA-077 |
| protótipo navegável | não iniciado | — |
| aplicação ou motor | não iniciado | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Registros granulares

A UXA-076 cria uma camada de rastreabilidade individual:

```text
família agregada
→ superfície ou responsabilidade identificada
→ transição identificada
→ autoridade e evidência
→ estado da continuidade
→ lacuna associada
```

Os IDs estabilizam a referência documental. Eles não implementam interfaces, não executam transições e não promovem maturidade.

## 7. Regra de leitura

Uma sequência exibida nesta seção é uma hipótese documental rastreável. Ela só poderá ser declarada como jornada integrada completa quando nós, transições, autoridades, dados, retornos, interrupções e estados alternativos tiverem evidência funcional suficiente.

Quando a continuidade necessária ainda não estiver materializada ou validada, ela será apresentada como **parcial**, **ausente** ou **não examinada**, nunca preenchida por suposição.

## 8. Regra de promoção

- esta visão geral está `active` porque a seção foi aprovada como instrumento documental de leitura e governança;
- as vistas de Pessoa, Coletivo e Organização permanecem `draft` por representarem jornadas incompletas;
- handoffs, cenários e catálogo estão `active` dentro dos limites explicitados pela UXA-074;
- os registros granulares permanecem `draft` até validação própria;
- o registro de lacunas permanece `active` por ser observacional e não promocional;
- inclusão nesta seção não altera maturidade, prioridade ou canonicidade;
- nenhuma referência é promovida apenas por estar navegável no GKR.

## 9. Escopo vigente

O status `active` desta seção confirma sua validade documental. Ele não declara:

- jornadas completas;
- validação ponta a ponta;
- validação funcional dos registros granulares;
- fechamento de lacunas;
- prontidão para protótipo;
- prontidão para implementação.
