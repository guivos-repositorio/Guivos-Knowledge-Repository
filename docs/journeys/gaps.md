---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-059
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é **observacional e não promocional**. Uma lacuna somente muda de estado por pacote governado com autoridade, materialização e validação correspondentes.

A [Galeria Visual Integrada de Telas](screen-gallery.md) facilita a inspeção, mas não fecha nenhuma ausência.

## 2. Fila priorizada com rastreabilidade granular

| Prioridade | Lacuna | Participante afetado | IDs relacionados | Estado visual | Gate de fechamento |
|---:|---|---|---|---|---|
| 1 | Meus Coletivos | Pessoa | GKR-SURF-PER-106; GKR-TRN-108; GKR-TRN-110 | sem SVG | materialização e validação funcional |
| 2 | Central de Atualizações | Pessoa | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | sem SVG | materialização e validação funcional |
| 3 | Início do Participante reformulado | Pessoa em Coletivo | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação, materialização e validação |
| 4 | Visão Geral do Responsável | Coletivo | GKR-SURF-COL-002; GKR-TRN-112 | sem SVG | materialização e validação funcional |
| 5 | gestão completa de solicitações | Coletivo | GKR-SURF-COL-003; GKR-TRN-105 a GKR-TRN-109 | apenas efeitos na visão da Pessoa | fluxo bilateral materializado e validado |
| 6 | participantes, comunicação e operação interna | Coletivo | GKR-SURF-COL-004 a GKR-SURF-COL-007 | sem SVGs dedicados | programa, materialização e validação |
| 7 | relação Organização–Coletivo | Organização e Coletivo | GKR-SURF-ORG-004 a GKR-SURF-ORG-006; GKR-SURF-COL-008; GKR-TRN-206 a GKR-TRN-209 | sem SVGs dedicados | materialização e validação bilateral |
| 8 | matriz institucional completa | Organização | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |
| 9 | dez estados residuais do Opportunity Boost | camada comercial | GKR-SURF-COM-005; GKR-TRN-305 | 10 SVGs sem validação | pacote de validação correspondente |
| 10 | efeito externo de oportunidades | Pessoa | GKR-SURF-PER-203; GKR-SURF-BND-001; GKR-TRN-205 | fronteira sem tela por definição | contrato e validação específicos |
| 11 | compreensão inicial → Tela Hoje | Pessoa | GKR-SURF-PER-007; GKR-SURF-PER-008; GKR-TRN-007 | telas existem separadamente | validação da continuidade integrada |
| 12 | publicação → descoberta | Organização e Pessoa | GKR-SURF-ORG-003; GKR-SURF-PER-201; GKR-TRN-203 | telas existem em pacotes distintos | revalidação funcional integrada |
| 13 | mapa, lista e detalhe | Pessoa | GKR-SURF-PER-201 a GKR-SURF-PER-203; GKR-TRN-204; GKR-TRN-210; GKR-TRN-211 | telas existentes | validação do conjunto |
| 14 | erros, retornos e interrupções | todos | registro de transições seletivo | cobertura dispersa | matriz integrada por jornada |

## 3. Resultado da auditoria visual da UXA-081

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 10 |
| IDs granulares com referência visual | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira corretamente sem tela | 1 |

A diferença entre 97 SVGs e 25 IDs cobertos decorre de estados alternativos, dispositivos e variações da mesma responsabilidade.

## 4. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver:

1. autoridade documental identificada;
2. maturidade primária registrada;
3. materialização específica quando necessária;
4. transições de entrada e saída;
5. estados alternativos, retornos e exceções;
6. proteção de dados e autoridade;
7. validação funcional correspondente;
8. atualização deste registro por pacote governado.

## 5. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- proximidade visual não comprova continuidade;
- inclusão na galeria não altera maturidade;
- validação de superfície não valida automaticamente a jornada;
- atribuição de ID não equivale a materialização;
- promoção do registro não promove os objetos;
- ausência de evidência permanece `indeterminado`, `parcial` ou `ausente`.

## 6. Estado vigente

A UXA-081 torna as ausências mais visíveis, sem fechá-las ou reclassificá-las. Os registros granulares permanecem `active`; a galeria permanece `draft` até revisão visual e funcional específica.
