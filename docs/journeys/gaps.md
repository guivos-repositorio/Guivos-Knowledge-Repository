---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.11.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
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
  - UXA-085
  - UXA-086
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-086 materializa a primeira superfície priorizada, mas não a declara funcionalmente validada nem encerra automaticamente sua lacuna.

## 2. Regra de priorização

A fila distingue:

1. **materialização**, que exige novas superfícies ou estados;
2. **gate de fechamento**, quando a materialização existe mas ainda requer validação funcional;
3. **dívidas de validação integrada**, quando os artefatos existem mas a continuidade não foi examinada como conjunto.

A origem de autoridade deve preceder o efeito percebido a jusante.

## 3. Primeira lacuna em gate de fechamento

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Gate para fechamento |
|---|---|---|---|---|
| Visão Geral do Responsável | GKR-SURF-COL-002; GKR-TRN-112 | 1 SVG desktop em UXA-086 | materializada; não validada | validação funcional específica da superfície; GKR-TRN-112 permanece parcial |

A UXA-086 conclui a materialização visual desta responsabilidade, mas a lacuna continua aberta até o gate funcional correspondente.

## 4. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | gestão completa de solicitações | GKR-SURF-COL-003; GKR-TRN-105 a GKR-TRN-109; GKR-TRN-112 | apenas efeitos na visão da Pessoa | depende da validação de GKR-SURF-COL-002 e de nova autorização |
| 2 | Meus Coletivos | GKR-SURF-PER-106; GKR-TRN-108; GKR-TRN-110 | sem SVG | depende da aprovação originada no Coletivo |
| 3 | Central de Atualizações | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | sem SVG | depende de vínculo ativo |
| 4 | Início do Participante reformulado | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação, materialização e validação |
| 5 | participantes, comunicação e operação interna | GKR-SURF-COL-004 a GKR-SURF-COL-007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 6 | relação Organização–Coletivo | GKR-SURF-ORG-004 a GKR-SURF-ORG-006; GKR-SURF-COL-008; GKR-TRN-206 a GKR-TRN-209 | sem SVGs | materialização e validação bilateral |
| 7 | matriz institucional completa | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

Nenhuma dessas materializações é iniciada pela UXA-086.

## 5. Fila separada de dívidas de validação

| Prioridade | Continuidade | IDs relacionados | Estado atual | Gate |
|---:|---|---|---|---|
| V0 | Visão Geral do Responsável | GKR-SURF-COL-002; GKR-TRN-112 | SVG materializado; destino operacional ausente | validação funcional específica da UXA-086 |
| V1 | compreensão inicial → Tela Hoje | GKR-SURF-PER-007; GKR-SURF-PER-008; GKR-TRN-007 | telas separadas; transição não examinada | validação integrada |
| V2 | publicação → descoberta | GKR-SURF-ORG-003; GKR-SURF-PER-201; GKR-TRN-203 | rota visual aprovada; pacotes distintos | revalidação integrada |
| V3 | mapa, lista e detalhe | GKR-SURF-PER-201 a GKR-SURF-PER-203; GKR-TRN-204; GKR-TRN-210; GKR-TRN-211 | ordem visual aprovada | validação do conjunto e retornos |
| V4 | dez estados residuais do Opportunity Boost | GKR-SURF-COM-005; GKR-TRN-305 | 10 SVGs rastreados e sem validação | pacote específico de validação |
| V5 | efeito externo de oportunidades | GKR-SURF-PER-203; GKR-SURF-BND-001; GKR-TRN-205 | fronteira sem tela por definição | contrato e validação específicos |
| V6 | erros, retornos e interrupções | todos | cobertura integrada ainda dispersa | validação por jornada |

## 6. Efeito da UXA-086

A UXA-086 altera somente a primeira responsabilidade priorizada:

- `GKR-SURF-COL-002` deixa de estar visualmente ausente;
- `GKR-TRN-112` passa de `ausente` para `parcial` porque somente a origem está materializada;
- `GKR-SURF-COL-003` continua ausente como operação completa;
- nenhuma outra lacuna é fechada, iniciada ou reclassificada.

## 7. Cobertura vigente

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 98 |
| associações individuais | 98 |
| perfis de rastreabilidade | 24 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 11 |
| IDs granulares com referência visual | 26 de 40 |
| responsabilidades sem SVG dedicado | 13 |
| fronteira corretamente sem tela | 1 |

## 8. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver autoridade, maturidade, materialização necessária, entradas e saídas, retornos e exceções, proteção de dados, validação correspondente e atualização governada deste registro.

Para `GKR-SURF-COL-002`, o SVG da UXA-086 é condição necessária, mas não suficiente.

## 9. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- proximidade visual não comprova continuidade;
- associação a perfil não valida jornada;
- materialização não equivale a validação funcional;
- ausência de evidência permanece `indeterminado`, `parcial`, `ausente` ou `não examinado`.

## 10. Próximo ato possível

A próxima ação governada é a validação funcional da UXA-086. `GKR-SURF-COL-003` não deve ser iniciado antes dessa decisão e de autorização separada.
