---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.16.0
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
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-091 materializa `GKR-SURF-PER-106 — Meus Coletivos` e refina a continuidade pós-aprovação, mas não valida a superfície, o estado aprovado reformulado de `PER-105` ou `GKR-TRN-108`.

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
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | estados materializados nas duas perspectivas | quatro handoffs bilaterais integralmente validados por UXA-090 | aprovação segue separada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | resultado aprovado reformulado + 1 SVG de PER-106 | pendente de revalidação | validar estado aprovado corrente, PER-106 e ligação completa |
| Meus Coletivos → Central de Atualizações | PER-106; TRN-110; PER-107 | origem materializada; destino sem SVG | parcial | materializar PER-107 em frente separada e depois validar continuidade |

`PER-106` deixa a fila de materialização e entra na fila de **gate funcional**. `TRN-108` continua aberta.

## 4. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | Central de Atualizações | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | sem SVG | somente após validação governada de PER-106/continuidade pós-aprovação |
| 2 | Início do Participante reformulado | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação, materialização e validação |
| 3 | participantes e operação interna | GKR-SURF-COL-004 a GKR-SURF-COL-007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 4 | relação Organização–Coletivo | GKR-SURF-ORG-004 a 006; GKR-SURF-COL-008; GKR-TRN-206 a 209 | sem SVGs | materialização e validação bilateral |
| 5 | matriz institucional completa | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

Nenhuma dessas materializações é iniciada pela UXA-091.

## 5. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V0 | PER-105 aprovado → PER-106 / TRN-108 | ambos visualmente materializados; versões correntes ainda não validadas como conjunto | UXA-092 — validação funcional e revalidação integrada |
| V1 | compreensão inicial → Tela Hoje | telas separadas; transição não examinada | validação integrada |
| V2 | publicação → descoberta e mapa/lista/detalhe | pacotes distintos | revalidação integrada |
| V3 | dez estados residuais do Opportunity Boost | 10 SVGs sem validação | pacote específico |
| V4 | efeito externo de oportunidades | fronteira sem tela por definição | contrato e validação específicos |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

`TRN-110` não é fechável nesta fila enquanto `PER-107` permanecer ausente.

## 6. Efeito da UXA-091

A UXA-091:

- adiciona 1 SVG móvel de `PER-106`;
- reforma 1 SVG existente do estado aprovado de `PER-105`;
- não cria superfície ou transição nova;
- mantém `TRN-105`, `106`, `107`, `109` e `112` integralmente validadas;
- mantém `TRN-108` parcial, agora com destino materializado;
- altera `TRN-110` de ausente para parcial porque somente sua origem existe;
- não materializa `PER-107`, `PER-108` ou `COL-004` a `COL-008`;
- não promove qualquer jornada.

## 7. Cobertura vigente proposta

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 106 |
| associações individuais | 106 |
| perfis de rastreabilidade | 26 |
| com validação funcional vigente | 94 |
| pendentes de validação específica | 12 |
| transições integralmente validadas pela UXA-090 | 5 |
| IDs granulares com referência visual | 28 de 40 |
| responsabilidades sem SVG dedicado | 11 |
| fronteira corretamente sem tela | 1 |

Os 12 pendentes são 10 estados residuais da UXA-055, o estado aprovado de `PER-105` reformulado pela UXA-091 e o novo SVG de `PER-106`.

## 8. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver autoridade, materialização necessária, entradas e saídas, retornos e exceções, proteção de dados, tratamento de concorrência, validação correspondente e atualização governada deste registro.

`PER-106` cumpre somente o gate de materialização nesta UXA.

## 9. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- materialização não equivale a validação;
- uma versão visual reformulada exige revalidação;
- dois endpoints materializados não validam automaticamente a ligação;
- validação integral documental não equivale a implementação técnica;
- `Meus Coletivos` não presume Central de Atualizações ou Início do Participante disponíveis.

## 10. Próximo ato possível

A próxima ação governada é **UXA-092 — Validação Funcional de Meus Coletivos e Revalidação da Continuidade Pós-Aprovação**, mediante autorização separada.

A UXA-092 não é iniciada por esta atualização.
