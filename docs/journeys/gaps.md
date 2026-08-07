---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.14.0
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
  - UXA-087
  - UXA-088
  - UXA-089
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-089 fecha o gate funcional específico de `GKR-SURF-COL-003`, mas não encerra os handoffs bilaterais associados e não materializa `PER-106`.

## 2. Regra de priorização

A fila distingue:

1. **materialização** — novas referências necessárias;
2. **gate de fechamento** — materialização existente aguardando validação funcional;
3. **dívida de validação integrada** — endpoints existentes e validados como superfícies sem exame ponta a ponta.

## 3. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável | COL-002; TRN-112 | 1 SVG | validada por UXA-087 | TRN-112 ainda não validada como conjunto |
| gestão de solicitações | COL-003; TRN-105 a 109; TRN-112 | 7 SVGs desktop em UXA-088 | validada por UXA-089 | handoffs bilaterais e saída para PER-106 pendentes |

`COL-003` deixa a fila de gate funcional e passa a compor a **dívida de validação integrada** das transições.

## 4. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | Meus Coletivos | GKR-SURF-PER-106; GKR-TRN-108; GKR-TRN-110 | sem SVG | depende da continuidade de participação e de autorização separada |
| 2 | Central de Atualizações | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | sem SVG | depende de vínculo ativo |
| 3 | Início do Participante reformulado | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação, materialização e validação |
| 4 | participantes e operação interna | GKR-SURF-COL-004 a GKR-SURF-COL-007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | GKR-SURF-ORG-004 a 006; GKR-SURF-COL-008; GKR-TRN-206 a 209 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

Nenhuma dessas materializações é iniciada pela UXA-089.

## 5. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V0 | COL-002 → COL-003 e handoffs PER-105 ↔ COL-003 | endpoints validados como superfícies; transições parciais | UXA-090 — validação integrada específica |
| V1 | compreensão inicial → Tela Hoje | telas separadas; transição não examinada | validação integrada |
| V2 | publicação → descoberta e mapa/lista/detalhe | pacotes distintos | revalidação integrada |
| V3 | dez estados residuais do Opportunity Boost | 10 SVGs sem validação | pacote específico |
| V4 | efeito externo de oportunidades | fronteira sem tela por definição | contrato e validação específicos |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

`GKR-TRN-108` não entra na UXA-090 como transição fechável enquanto `GKR-SURF-PER-106` permanecer ausente; sua origem está validada, mas o destino ainda exige materialização própria.

## 6. Efeito da UXA-089

A UXA-089:

- preserva os sete SVGs de `GKR-SURF-COL-003`;
- reformula seis desses SVGs;
- valida funcionalmente os sete estados;
- distingue estimativa de prazo de resposta;
- exige critérios previamente apresentados à Pessoa;
- separa acessibilidade de elegibilidade;
- impede autodeclaração de autoridade por confirmação;
- não valida `TRN-105` a `109` ou `TRN-112` ponta a ponta;
- não materializa `PER-106`, `PER-107`, `PER-108` ou `COL-004` a `COL-008`.

## 7. Cobertura vigente proposta

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 105 |
| associações individuais | 105 |
| perfis de rastreabilidade | 25 |
| com validação funcional registrada | 95 |
| pendentes de validação específica | 10 |
| IDs granulares com referência visual | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |
| fronteira corretamente sem tela | 1 |

Os dez pendentes remanescentes são exclusivamente os estados residuais da UXA-055.

## 8. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver autoridade, materialização necessária, entradas e saídas, retornos e exceções, proteção de dados, validação correspondente e atualização governada deste registro.

Para `COL-003`, o gate específico da superfície está encerrado pela UXA-089. A continuidade bilateral permanece aberta e deverá ser examinada separadamente.

## 9. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- proximidade visual não comprova continuidade;
- materialização não equivale a validação;
- validação de uma superfície não valida o handoff inteiro;
- dois endpoints validados não validam automaticamente a ligação entre eles.

## 10. Próximo ato possível

A próxima ação governada é **UXA-090 — Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos**, mediante autorização separada.

A UXA-090 não é iniciada por esta atualização.
