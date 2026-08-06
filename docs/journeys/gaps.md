---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.7.0
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
  - UXA-082
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é **observacional e não promocional**. Uma lacuna somente muda de estado por pacote governado com autoridade, materialização e validação correspondentes.

A [Galeria Visual Integrada de Telas](screen-gallery.md) facilita a inspeção, mas não fecha nenhuma ausência.

## 2. Regra de priorização da UXA-082

A fila passa a distinguir:

1. **lacunas de materialização**, que exigem novas superfícies ou estados;
2. **dívidas de validação**, nas quais os artefatos existem, mas a continuidade não foi examinada como conjunto.

Dentro da fila de materialização, a origem de autoridade deve preceder o efeito percebido a jusante.

## 3. Fila de materialização por dependência

| Prioridade | Lacuna | Participante afetado | IDs relacionados | Estado visual | Dependência e gate |
|---:|---|---|---|---|---|
| 1 | Visão Geral do Responsável | Coletivo | GKR-SURF-COL-002; GKR-TRN-112 | sem SVG | origem protegida da operação; materialização e validação funcional |
| 2 | gestão completa de solicitações | Coletivo | GKR-SURF-COL-003; GKR-TRN-105 a GKR-TRN-109; GKR-TRN-112 | apenas efeitos na visão da Pessoa | depende da visão do responsável; fluxo bilateral materializado e validado |
| 3 | Meus Coletivos | Pessoa | GKR-SURF-PER-106; GKR-TRN-108; GKR-TRN-110 | sem SVG | depende da aprovação originada em GKR-SURF-COL-003 |
| 4 | Central de Atualizações | Pessoa | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | sem SVG | depende de vínculo ativo em Meus Coletivos |
| 5 | Início do Participante reformulado | Pessoa em Coletivo | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | depende da Central e requer reformulação, materialização e validação |
| 6 | participantes, comunicação e operação interna | Coletivo | GKR-SURF-COL-004 a GKR-SURF-COL-007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação após a base operacional |
| 7 | relação Organização–Coletivo | Organização e Coletivo | GKR-SURF-ORG-004 a GKR-SURF-ORG-006; GKR-SURF-COL-008; GKR-TRN-206 a GKR-TRN-209 | sem SVGs dedicados | materialização e validação bilateral |
| 8 | matriz institucional completa | Organização | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

A ordem anterior, que iniciava por Meus Coletivos, foi substituída porque `GKR-TRN-108` depende da decisão produzida em `GKR-SURF-COL-003` e `GKR-TRN-112` depende de `GKR-SURF-COL-002`.

## 4. Fila separada de dívidas de validação

| Prioridade | Continuidade | IDs relacionados | Estado atual | Gate |
|---:|---|---|---|---|
| V1 | compreensão inicial → Tela Hoje | GKR-SURF-PER-007; GKR-SURF-PER-008; GKR-TRN-007 | telas existem separadamente; transição não examinada | validação da continuidade integrada |
| V2 | publicação → descoberta | GKR-SURF-ORG-003; GKR-SURF-PER-201; GKR-TRN-203 | telas em pacotes distintos | revalidação funcional integrada |
| V3 | mapa, lista e detalhe | GKR-SURF-PER-201 a GKR-SURF-PER-203; GKR-TRN-204; GKR-TRN-210; GKR-TRN-211 | telas existentes | validação do conjunto e retornos |
| V4 | dez estados residuais do Opportunity Boost | GKR-SURF-COM-005; GKR-TRN-305 | 10 SVGs sem validação | pacote de validação correspondente |
| V5 | efeito externo de oportunidades | GKR-SURF-PER-203; GKR-SURF-BND-001; GKR-TRN-205 | fronteira sem tela por definição | contrato e validação específicos |
| V6 | erros, retornos e interrupções | todos | cobertura dispersa | matriz integrada por jornada |

Esses itens não devem ser priorizados como se exigissem necessariamente novas telas.

## 5. Resultado da auditoria visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 10 |
| IDs granulares com referência visual | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira corretamente sem tela | 1 |

A diferença entre 97 SVGs e 25 IDs cobertos decorre de estados alternativos, dispositivos e variações da mesma responsabilidade.

## 6. Resultado da validação da galeria

A UXA-082 não aprovou a galeria para promoção. Foram identificados:

- ordem funcional incorreta na página da Pessoa;
- Home pública e Tela Hoje agrupadas em um mesmo bloco;
- ausência de rota integrada de inspeção;
- rastreabilidade agrupada insuficiente para assertividade por SVG;
- divergência de versões em resumos documentais.

A correção da galeria precede a materialização das lacunas priorizadas.

## 7. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver:

1. autoridade documental identificada;
2. maturidade primária registrada;
3. materialização específica quando necessária;
4. transições de entrada e saída;
5. estados alternativos, retornos e exceções;
6. proteção de dados e autoridade;
7. validação funcional correspondente;
8. atualização deste registro por pacote governado.

## 8. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- proximidade visual não comprova continuidade;
- inclusão na galeria não altera maturidade;
- validação de superfície não valida automaticamente a jornada;
- atribuição de ID não equivale a materialização;
- promoção do registro não promove os objetos;
- ausência de evidência permanece `indeterminado`, `parcial` ou `ausente`.

## 9. Estado vigente

Os registros granulares permanecem `active`. A galeria permanece `draft` e não aprovada para promoção até reformulação controlada. Nenhuma lacuna foi fechada ou iniciada pela UXA-082.
