---
id: ROADMAP-12.74.0
title: Roadmap Arquitetural — Saída Consciente para Fronteira Externa Validada
status: active
version: 12.74.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.73.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-099
  - UXA-100
  - UXA-101
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.88
---

# Roadmap Arquitetural — Saída Consciente para Fronteira Externa Validada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual e só se torna vigente na `main` após integração governada.

## 2. Estado proposto

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | saída consciente para fronteira externa validada | UXA-101; M7.88 |
| Registros granulares | **53 superfícies/estados/fronteiras e 54 transições** | UXA-101 |
| Galeria visual | `active` 0.21.0; **118 SVGs** | UXA-101 |
| matriz por SVG | **118 arquivos / 31 perfis**; `active` 0.17.0 | UXA-101 |
| validações funcionais vigentes de SVG | **118** | UXA-101 |
| pendentes de validação específica | **0** | UXA-101 |
| V4 | **encerrada até BND-001** | UXA-101 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência governada recente

```text
UXA-097 — compreensão inicial → primeira Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — dez estados residuais Opportunity Boost
→ UXA-100/A1/A2/A3 — Planos materializados, validados e promovidos
→ UXA-101 — Detalhe → revisão consciente → BND-001
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-101

| Dimensão | Resultado |
|---|---|
| SVGs reformulados | **1 — uxa-007-opportunity-detail-mobile.svg** |
| novos SVGs | **0** |
| novas superfícies | **0** |
| novas fronteiras | **0** |
| novas transições | **0** |
| `TRN-205` | **validada até BND-001** |
| `BND-001` | **examinada como fronteira externa sem tela** |
| SVGs totais | **118** |
| associações | **118** |
| perfis | **31** |
| superfícies/estados/fronteiras | **53** |
| transições | **54** |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato V4

```text
PER-203 — Detalhe
→ “Ver como participar”
→ revisão de saída na própria PER-203
→ destino/responsável + dados/contexto + limites
→ confirmação afirmativa
→ revalidação do destino
→ TRN-205
→ BND-001
→ autoridade externa
```

- revisão pré-saída não cria nova superfície;
- ausência/invalidade do destino bloqueia redirecionamento silencioso;
- cancelamento preserva a Pessoa no Detalhe;
- saída não presume resultado externo;
- retorno não presume inscrição, reserva, compra ou contratação;
- dados pessoais e inferências não acompanham a saída sem finalidade e autorização adequadas.

## 6. Fronteiras preservadas

- `TRN-304`, `TRN-305` e `TRN-306`: integrações patrocinadas continuam parciais;
- `TRN-416/426`: processo comercial após `BND-002` continua parcial;
- gateway, cobrança real, proration, grace period e regras fiscais finais permanecem fora do escopo;
- comportamento posterior a `BND-001` permanece sob autoridade externa;
- nenhuma implementação é criada pela validação documental.

## 7. Fila global

```text
V1 — compreensão inicial → Tela Hoje — ENCERRADA pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — ENCERRADA pela UXA-098
→ V3 — dez estados residuais UXA-055 — ENCERRADA pela UXA-099
→ Planos — identidade/promoção canônica — ENCERRADA pela UXA-100-A3
→ V4 — efeito externo de oportunidades — ENCERRADA pela UXA-101 até BND-001
→ V5 — erros, retornos e interrupções — PENDENTE
```

## 8. Dívidas preservadas

- estados P0B adicionais de Meus Coletivos, Central e Início do Participante;
- áreas P1 de comunicação especializada;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` parciais;
- `TRN-304`, `TRN-305` e `TRN-306` parciais;
- cobrança real e gateway de Planos;
- processo Enterprise/Scale após `BND-002`;
- entradas contextuais de Planos sem origem canônica adequada;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada;
- processo/resultados externos posteriores a `BND-001`.

## 9. Próxima iniciativa possível

V5 continua dependente de autorização humana separada. A auditoria dos Produtos Especializados é um diagnóstico transversal permitido após UXA-101 e não inicia automaticamente nova UXA, implementação ou Engenharia de Produto.