---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.15.0
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
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-090 encerra a dívida de validação integrada de `GKR-TRN-105`, `106`, `107`, `109` e `112`, mas preserva `GKR-TRN-108` e `PER-106` como continuidade aberta.

## 2. Regra de priorização

A fila distingue:

1. **materialização** — novas referências necessárias;
2. **gate de fechamento** — materialização existente aguardando validação funcional;
3. **dívida de validação integrada** — endpoints existentes e validados como superfícies sem exame ponta a ponta;
4. **continuidade pós-resultado** — resultado compreensível existe, mas a superfície operacional seguinte ainda não foi materializada.

## 3. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável → gestão de solicitações | COL-002; TRN-112; COL-003 | 8 SVGs somados nas superfícies | superfícies validadas; TRN-112 integralmente validada por UXA-090 | nenhuma lacuna nesta ligação específica |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | estados materializados nas duas perspectivas | quatro handoffs bilaterais integralmente validados por UXA-090 | aprovação segue separada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | resultado aprovado existe em PER-105; PER-106 sem SVG | parcial | materializar PER-106 e refinar passagem resultado aprovado → ambiente participante |

`COL-003` e os cinco handoffs elegíveis deixam a fila de dívida integrada. `TRN-108` permanece explicitamente aberta.

## 4. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | Meus Coletivos e continuidade pós-aprovação | GKR-SURF-PER-106; GKR-TRN-108; GKR-TRN-110 | sem SVG para PER-106 | materialização própria + refinamento da passagem desde o resultado aprovado em PER-105 |
| 2 | Central de Atualizações | GKR-SURF-PER-107; GKR-TRN-110; GKR-TRN-111 | sem SVG | depende de vínculo ativo |
| 3 | Início do Participante reformulado | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação, materialização e validação |
| 4 | participantes e operação interna | GKR-SURF-COL-004 a GKR-SURF-COL-007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | GKR-SURF-ORG-004 a 006; GKR-SURF-COL-008; GKR-TRN-206 a 209 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

Nenhuma dessas materializações é iniciada pela UXA-090.

## 5. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V0 | continuidade pós-aprovação | TRN-108 parcial; PER-106 ausente | materialização de PER-106 e refinamento da continuidade |
| V1 | compreensão inicial → Tela Hoje | telas separadas; transição não examinada | validação integrada |
| V2 | publicação → descoberta e mapa/lista/detalhe | pacotes distintos | revalidação integrada |
| V3 | dez estados residuais do Opportunity Boost | 10 SVGs sem validação | pacote específico |
| V4 | efeito externo de oportunidades | fronteira sem tela por definição | contrato e validação específicos |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

Os handoffs `105`, `106`, `107`, `109` e `112` deixam esta fila após a UXA-090.

## 6. Efeito da UXA-090

A UXA-090:

- não adiciona SVG;
- não cria superfície ou transição;
- valida integralmente `TRN-105`, `106`, `107`, `109` e `112`;
- formaliza identidade estável da solicitação e estado canônico;
- exige autoridade vigente antes de efeito;
- trata cancelamento, expiração, resposta e decisão concorrentes;
- impede que estado obsoleto sobrescreva evento mais recente;
- exige efeito lógico único diante de repetição ou reenvio;
- mantém `TRN-108` parcial;
- mantém `PER-106`, `PER-107`, `PER-108` e `COL-004` a `COL-008` fora do escopo.

## 7. Cobertura vigente proposta

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 105 |
| associações individuais | 105 |
| perfis de rastreabilidade | 25 |
| com validação funcional registrada | 95 |
| pendentes de validação específica | 10 |
| transições integralmente validadas pela UXA-090 | 5 |
| IDs granulares com referência visual | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |
| fronteira corretamente sem tela | 1 |

Os dez pendentes de SVG remanescentes são exclusivamente os estados residuais da UXA-055.

## 8. Critérios de fechamento

Uma lacuna somente poderá ser encerrada quando houver autoridade, materialização necessária, entradas e saídas, retornos e exceções, proteção de dados, tratamento de concorrência, validação correspondente e atualização governada deste registro.

Os cinco handoffs elegíveis cumprem esses critérios no escopo documental da experiência. A continuidade pós-aprovação não cumpre porque `PER-106` ainda não existe.

## 9. Restrições

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- proximidade visual não comprova continuidade;
- materialização não equivale a validação;
- validação de uma superfície não valida o handoff inteiro;
- dois endpoints validados não validam automaticamente a ligação entre eles;
- validação integral documental não equivale a implementação técnica;
- resultado aprovado visível não presume que o ambiente participante esteja materializado.

## 10. Próximo ato possível

A próxima ação governada é **UXA-091 — Materialização Controlada de Meus Coletivos (`GKR-SURF-PER-106`) e Refinamento da Continuidade Pós-Aprovação**, mediante autorização separada.

A UXA-091 não é iniciada por esta atualização.
