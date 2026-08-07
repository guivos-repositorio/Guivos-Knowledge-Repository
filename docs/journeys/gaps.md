---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.18.0
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
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-093 materializa `GKR-SURF-PER-107 — Central de Atualizações` sem validar a nova superfície, sem fechar `GKR-TRN-110` e sem materializar `PER-108` ou estados P0B adicionais.

## 2. Regra de priorização

A fila distingue:

1. **materialização** — novas referências necessárias;
2. **gate de fechamento** — materialização existente aguardando validação funcional;
3. **dívida de validação integrada** — endpoints existentes sem exame ponta a ponta da ligação corrente;
4. **continuidade pós-resultado** — resultado compreensível existe e a superfície seguinte foi ou será materializada, mas a passagem ainda exige validação.

## 3. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável → gestão de solicitações | COL-002; TRN-112; COL-003 | 8 SVGs somados | superfícies validadas; TRN-112 integralmente validada por UXA-090 | nenhuma lacuna nesta ligação específica |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | estados materializados nas duas perspectivas | quatro handoffs bilaterais integralmente validados por UXA-090 | aprovação fechada separadamente em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | resultado aprovado + 1 SVG de PER-106, ambos reformulados | fechada por UXA-092 | nenhuma lacuna nesta ligação específica |
| Meus Coletivos → Central de Atualizações | PER-106; TRN-110; PER-107 | **ambos os endpoints materializados**; PER-107 com 1 SVG móvel | parcial | validar PER-107 e a ligação TRN-110 como conjunto |
| Central de Atualizações → Início do Participante | PER-107; TRN-111; PER-108 | origem materializada; destino não vigente | ausente | reformular/materializar PER-108 antes de validar a continuidade |

`PER-107` deixa a fila de materialização e entra na fila de gate funcional. `TRN-110` continua como dívida integrada; dois endpoints materializados não fecham a ligação automaticamente.

## 4. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | Início do Participante reformulado | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação, materialização e validação após gate próprio de PER-107/TRN-110 |
| 2 | estados P0B adicionais de Meus Coletivos | GKR-SURF-PER-106 | referência P0A validada; estados alternativos sem SVG | materialização apenas quando decisão/hierarquia justificar SVG próprio |
| 3 | estados P0B da Central de Atualizações | GKR-SURF-PER-107 | referência P0A materializada; vazio, agrupamento e baixa conectividade sem SVG | materialização separada quando necessária |
| 4 | participantes e operação interna | GKR-SURF-COL-004 a GKR-SURF-COL-007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | GKR-SURF-ORG-004 a 006; GKR-SURF-COL-008; GKR-TRN-206 a 209 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

Nenhuma dessas materializações é iniciada pela UXA-093.

## 5. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 | `PER-107 — Central de Atualizações` + `TRN-110` | referência P0A materializada; ambos os endpoints de TRN-110 existem | validação funcional da superfície e revalidação ponta a ponta do handoff |
| V2 | compreensão inicial → Tela Hoje | telas separadas; transição não examinada | validação integrada |
| V3 | publicação → descoberta e mapa/lista/detalhe | pacotes distintos | revalidação integrada |
| V4 | dez estados residuais do Opportunity Boost | 10 SVGs sem validação | pacote específico |
| V5 | efeito externo de oportunidades | fronteira sem tela por definição | contrato e validação específicos |
| V6 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

`TRN-110` torna-se validável após UXA-093, mas não é promovida por inferência.

## 6. Efeito da UXA-093

A UXA-093:

- adiciona 1 SVG móvel para `PER-107`;
- não altera qualquer SVG previamente validado;
- materializa `PER-107` sem validação funcional;
- mantém `TRN-110` `parcial`, agora com os dois endpoints materializados;
- mantém `TRN-111` `ausente` porque `PER-108` continua não materializado;
- preserva `TRN-105`, `106`, `107`, `108`, `109` e `112` integralmente validadas;
- não materializa `PER-108`, estados P0B da Central ou áreas P1;
- não promove qualquer jornada.

## 7. Cobertura vigente proposta

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| com validação funcional vigente | 96 |
| pendentes de validação específica | 11 |
| handoffs integralmente validados no fluxo de solicitação | 6 |
| IDs granulares com referência visual | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |
| fronteira corretamente sem tela | 1 |

Os 11 pendentes correspondem aos dez estados residuais da UXA-055 e ao novo SVG da UXA-093.

## 8. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver autoridade, materialização necessária, entradas e saídas, retornos e exceções, proteção de dados, tratamento de concorrência, validação correspondente e atualização governada deste registro.

A UXA-093 cumpre somente o gate de materialização de `PER-107`; a validação funcional e `TRN-110` continuam abertas.

## 9. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- materialização não equivale a validação;
- uma versão visual reformulada exige revalidação;
- dois endpoints materializados não validam automaticamente a ligação;
- estado `lido` não equivale a ação concluída ou consentimento;
- validação integral documental não equivale a implementação técnica;
- a Central não presume `PER-108` ou canais especializados disponíveis.

## 10. Próximo ato possível

A próxima ação governada é **UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de `GKR-TRN-110`**, mediante autorização separada.

A UXA-094 não é iniciada por esta atualização.