---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.17.0
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
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-092 fecha a lacuna funcional específica entre o resultado aprovado corrente de `PER-105`, `GKR-TRN-108` e `GKR-SURF-PER-106 — Meus Coletivos`, sem materializar `PER-107`, `PER-108` ou estados P0B adicionais.

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
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | resultado aprovado + 1 SVG de PER-106, ambos reformulados | **fechada por UXA-092** | nenhuma lacuna nesta ligação específica |
| Meus Coletivos → Central de Atualizações | PER-106; TRN-110; PER-107 | origem validada; destino sem SVG | parcial | materializar PER-107 em frente separada e depois validar continuidade |

`PER-106` deixa a fila de gate funcional. `TRN-108` deixa a fila de dívida integrada e passa a integralmente validada.

## 4. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | Central de Atualizações | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | sem SVG | materialização controlada após UXA-092 |
| 2 | estados P0B adicionais de Meus Coletivos | GKR-SURF-PER-106 | referência P0A validada; estados alternativos sem SVG | materialização apenas quando decisão/hierarquia justificar SVG próprio |
| 3 | Início do Participante reformulado | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação, materialização e validação |
| 4 | participantes e operação interna | GKR-SURF-COL-004 a GKR-SURF-COL-007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | GKR-SURF-ORG-004 a 006; GKR-SURF-COL-008; GKR-TRN-206 a 209 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

Nenhuma dessas materializações é iniciada pela UXA-092.

## 5. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 | compreensão inicial → Tela Hoje | telas separadas; transição não examinada | validação integrada |
| V2 | publicação → descoberta e mapa/lista/detalhe | pacotes distintos | revalidação integrada |
| V3 | dez estados residuais do Opportunity Boost | 10 SVGs sem validação | pacote específico |
| V4 | efeito externo de oportunidades | fronteira sem tela por definição | contrato e validação específicos |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

`TRN-110` não é fechável nesta fila enquanto `PER-107` permanecer ausente.

## 6. Efeito da UXA-092

A UXA-092:

- não adiciona ou remove SVG;
- reforma 2 SVGs existentes: resultado aprovado de `PER-105` e referência P0A de `PER-106`;
- valida as versões correntes de `PER-105` aprovado e `PER-106`;
- promove `TRN-108` de `parcial` para `integralmente validada`;
- mantém `TRN-105`, `106`, `107`, `109` e `112` integralmente validadas;
- mantém `TRN-110` parcial porque `PER-107` continua ausente;
- não materializa `PER-107`, `PER-108` ou `COL-004` a `COL-008`;
- não promove qualquer jornada.

## 7. Cobertura vigente proposta

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 106 |
| associações individuais | 106 |
| perfis de rastreabilidade | 26 |
| com validação funcional vigente | 96 |
| pendentes de validação específica | 10 |
| handoffs integralmente validados no fluxo de solicitação | 6 |
| IDs granulares com referência visual | 28 de 40 |
| responsabilidades sem SVG dedicado | 11 |
| fronteira corretamente sem tela | 1 |

Os dez pendentes remanescentes correspondem exclusivamente aos estados residuais da UXA-055.

## 8. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver autoridade, materialização necessária, entradas e saídas, retornos e exceções, proteção de dados, tratamento de concorrência, validação correspondente e atualização governada deste registro.

A UXA-092 cumpre esse gate para a continuidade `PER-105 aprovado → TRN-108 → PER-106`.

## 9. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- materialização não equivale a validação;
- uma versão visual reformulada exige revalidação;
- dois endpoints materializados não validam automaticamente a ligação;
- validação integral documental não equivale a implementação técnica;
- `Meus Coletivos` não presume Central de Atualizações ou Início do Participante disponíveis.

## 10. Próximo ato possível

A próxima ação governada é **UXA-093 — Materialização Controlada da Central de Atualizações (`GKR-SURF-PER-107`)**, mediante autorização separada.

A UXA-093 não é iniciada por esta atualização.
