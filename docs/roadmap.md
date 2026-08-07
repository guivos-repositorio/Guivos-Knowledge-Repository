---
id: ROADMAP-12.72.0
title: Roadmap Arquitetural — Estados Residuais do Opportunity Boost Validados
status: active
version: 12.72.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.71.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-055
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-099
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.86
---

# Roadmap Arquitetural — Estados Residuais do Opportunity Boost Validados

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado proposto

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | dez estados residuais Opportunity Boost validados | UXA-099; M7.86 |
| Registros granulares | 40 superfícies e 37 transições | UXA-099 |
| Galeria visual | `active` 0.17.0; 109 SVGs | UXA-099 |
| matriz por SVG | 109 arquivos / 28 perfis; `active` 0.15.0 | UXA-099 |
| validações funcionais vigentes de SVG | **109** | UXA-099 |
| pendentes de validação específica | **0** | UXA-099 |
| COM-005 | **validado funcionalmente** | UXA-099 |
| TRN-305 | **parcial** | integração ponta a ponta não promovida |
| V3 | **encerrada** | UXA-099 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência governada recente

```text
UXA-090 — cinco handoffs de solicitação validados
→ UXA-091 — PER-106 materializada
→ UXA-092 — PER-106 e TRN-108 validadas
→ UXA-093 — PER-107 materializada
→ UXA-094 — PER-107 e TRN-110 validadas
→ UXA-095 — PER-108 materializada e TRN-111 parcial
→ UXA-096 — PER-107/PER-108 validadas e TRN-111 validada ponta a ponta
→ UXA-097 — primeira PER-008 materializada e validada; PER-007 revalidada; TRN-007 validada ponta a ponta
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe validados como continuidade integrada
→ UXA-099 — dez estados residuais Opportunity Boost validados após duas reformulações controladas
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-099

| Dimensão | Resultado |
|---|---|
| estados UXA-055 examinados | **10** |
| aprovados sem alteração visual | **8** |
| reformulados e validados | **2** |
| SVGs novos | **0** |
| SVGs reformulados | **2** |
| COM-005 | materializado → **validado no escopo dos dez estados** |
| TRN-305 | **permanece parcial** |
| SVGs totais | **109** |
| associações | **109** |
| perfis | **28** |
| validações vigentes | **109** |
| pendentes | **0** |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato V3 validado

A UXA-099 fecha os estados residuais com as seguintes regras:

- erro técnico patrocinado não é representado como zero inventário;
- zero inventário não amplia critérios automaticamente;
- baixa oferta orgânica reduz publicidade;
- tentativa de alteração material que não possa ser confirmada preserva a versão confirmada, não aplica a candidata e pausa entrega futura por proteção;
- retorno e nova tentativa são conscientes;
- repetição da mesma intenção é funcionalmente idempotente;
- ocultar campanha, mostrar menos e desativar patrocinados mantêm escopos próprios;
- histórico de preferências mostra data, superfície e escopo;
- denúncia e contestação permanecem fluxos independentes;
- identidade, motivo, preferência e contestação da pessoa não são revelados ao anunciante.

## 6. Fronteiras preservadas

- `TRN-205`: efeito externo posterior continua parcial;
- `TRN-304` e `TRN-306`: integração patrocinada com Mapa/Lista continua parcial;
- `TRN-305`: ligação para estados residuais continua parcial, pois validação de superfície não equivale a validação de transição;
- pagamento amplia distribuição publicitária identificada, não relevância funcional;
- nenhum resultado econômico, campanha real ou implementação é criado pela UXA-099.

## 7. Trilha governada de Coletivos preservada

```text
COL-002
→ TRN-112
→ COL-003
↔ TRN-105/106/107/109
→ TRN-108
→ PER-106
→ TRN-110
→ PER-107
→ TRN-111
→ PER-108
```

As oito transições indicadas permanecem integralmente validadas.

## 8. Fila de validação

```text
V1 — compreensão inicial → Tela Hoje — ENCERRADA pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — ENCERRADA pela UXA-098
→ V3 — dez estados residuais UXA-055 — ENCERRADA pela UXA-099
→ V4 — efeito externo de oportunidades — próxima prioridade
→ V5 — erros, retornos e interrupções
```

## 9. Dívidas preservadas

- estados P0B adicionais de Meus Coletivos, Central e Início do Participante;
- áreas P1 de comunicação especializada;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda parciais;
- `TRN-205` efeito externo de oportunidades;
- `TRN-304` e `TRN-306` integração patrocinada;
- `TRN-305` integração ponta a ponta dos estados residuais;
- erros, retornos e interrupções em outras jornadas;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada como conjunto.

## 10. Limites

A UXA-099 não cria novos SVGs ou IDs, não define algoritmo, política jurídica final, antifraude, cobrança ou perfil publicitário, não valida `TRN-305` ponta a ponta, não executa efeito externo, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia de Produto.

## 11. Próxima iniciativa possível

A próxima prioridade registrada é **V4 — efeito externo de oportunidades**, associada a `TRN-205`. Uma eventual UXA-100 dependerá de autorização separada e **não foi iniciada**.
