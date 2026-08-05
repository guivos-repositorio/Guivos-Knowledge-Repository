---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
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
6. consulte o catálogo de superfícies e transições;
7. acompanhe as lacunas registradas.

## 3. Vistas disponíveis

- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Catálogo de telas](screen-catalog.md)
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
| reformulação, navegação e sincronização | executadas neste pacote | UXA-073 |
| nova validação funcional | não iniciada | futura UXA-074 |
| protótipo navegável | não iniciado | — |
| aplicação ou motor | não iniciado | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Regra de leitura

Uma sequência exibida nesta seção é uma hipótese documental rastreável. Ela só poderá ser declarada como jornada integrada validada quando nós, transições, autoridades, dados, retornos, interrupções e estados alternativos tiverem evidência funcional suficiente.

Quando a continuidade necessária ainda não estiver materializada ou validada, ela será apresentada como **parcial**, **ausente** ou **não examinada**, nunca preenchida por suposição.

## 7. Regra de promoção

- os mapas permanecem `draft` até nova validação funcional aprovada;
- o registro de lacunas pode permanecer `active` por ser observacional e não promocional;
- inclusão nesta seção não altera maturidade, prioridade ou canonicidade;
- nenhuma referência será promovida para `active` apenas por estar navegável no GKR.
