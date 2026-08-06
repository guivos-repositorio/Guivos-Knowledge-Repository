---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.9.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-06
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
  - UXA-083
  - UXA-084
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A revalidação da galeria melhora a inspeção, mas não fecha, inicia ou reclassifica nenhuma ausência.

## 2. Regra de priorização

A fila distingue:

1. **lacunas de materialização**, que exigem novas superfícies ou estados;
2. **dívidas de validação**, nas quais os artefatos existem, mas a continuidade não foi examinada como conjunto.

A origem de autoridade deve preceder o efeito percebido a jusante.

## 3. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | Visão Geral do Responsável | GKR-SURF-COL-002; GKR-TRN-112 | sem SVG | materialização e validação funcional |
| 2 | gestão completa de solicitações | GKR-SURF-COL-003; GKR-TRN-105 a GKR-TRN-109; GKR-TRN-112 | apenas efeitos na visão da Pessoa | fluxo bilateral materializado e validado |
| 3 | Meus Coletivos | GKR-SURF-PER-106; GKR-TRN-108; GKR-TRN-110 | sem SVG | depende da aprovação originada no Coletivo |
| 4 | Central de Atualizações | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | sem SVG | depende de vínculo ativo |
| 5 | Início do Participante reformulado | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação, materialização e validação |
| 6 | participantes, comunicação e operação interna | GKR-SURF-COL-004 a GKR-SURF-COL-007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 7 | relação Organização–Coletivo | GKR-SURF-ORG-004 a GKR-SURF-ORG-006; GKR-SURF-COL-008; GKR-TRN-206 a GKR-TRN-209 | sem SVGs | materialização e validação bilateral |
| 8 | matriz institucional completa | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

## 4. Fila separada de dívidas de validação

| Prioridade | Continuidade | IDs relacionados | Estado atual | Gate |
|---:|---|---|---|---|
| V1 | compreensão inicial → Tela Hoje | GKR-SURF-PER-007; GKR-SURF-PER-008; GKR-TRN-007 | telas separadas e revalidadas como inspeção; transição não examinada | validação integrada |
| V2 | publicação → descoberta | GKR-SURF-ORG-003; GKR-SURF-PER-201; GKR-TRN-203 | rota visual aprovada; pacotes distintos | revalidação integrada |
| V3 | mapa, lista e detalhe | GKR-SURF-PER-201 a GKR-SURF-PER-203; GKR-TRN-204; GKR-TRN-210; GKR-TRN-211 | ordem visual aprovada | validação do conjunto e retornos |
| V4 | dez estados residuais do Opportunity Boost | GKR-SURF-COM-005; GKR-TRN-305 | 10 SVGs rastreados e sem validação | pacote específico de validação |
| V5 | efeito externo de oportunidades | GKR-SURF-PER-203; GKR-SURF-BND-001; GKR-TRN-205 | fronteira sem tela por definição | contrato e validação específicos |
| V6 | erros, retornos e interrupções | todos | matriz aprovada com ressalvas; cobertura integrada ainda dispersa | validação por jornada |

## 5. Resultado da UXA-084

A UXA-084 aprovou com ressalvas a galeria e a matriz como instrumentos documentais de inspeção.

Foram confirmados:

- ordem funcional corrigida;
- Home e Tela Hoje separadas;
- rota integrada entre cinco páginas;
- 97 SVGs associados individualmente a 23 perfis;
- versões sincronizadas;
- ausência e indeterminação preservadas.

A aprovação não altera o estado das lacunas ou das transições.

## 6. Ressalvas vigentes

- 14 responsabilidades permanecem sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- dez estados da UXA-055 continuam sem validação específica;
- perfis agregados não substituem análise exclusiva de cada estado;
- continuidades entre pacotes permanecem parciais ou não examinadas.

## 7. Cobertura vigente

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| associações individuais | 97 |
| perfis de rastreabilidade | 23 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 10 |
| IDs granulares com referência visual | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira corretamente sem tela | 1 |

## 8. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver autoridade, maturidade, materialização necessária, entradas e saídas, retornos e exceções, proteção de dados, validação correspondente e atualização governada deste registro.

## 9. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- proximidade visual não comprova continuidade;
- associação a perfil não valida jornada;
- promoção do registro não promove os objetos;
- ausência de evidência permanece `indeterminado`, `parcial`, `ausente` ou `não examinado`.

## 10. Estado vigente

A galeria está em `draft` 0.4.0 e a matriz em `draft` 0.2.0, ambas aprovadas com ressalvas e aguardando eventual promoção controlada. Nenhuma lacuna foi fechada, iniciada ou reclassificada pela UXA-084.
