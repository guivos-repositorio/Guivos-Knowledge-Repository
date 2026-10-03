---
id: GKR-CANON-MATRIX-UIC01-LIFECYCLE-ADDENDUM-001
title: Adendo da Matriz de Consolidação Canônica — Ciclo Técnico da UIC-01
status: active
version: 1.34.0
owner: Guivos
last_updated: 2026-07-19
normative: true
related:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-LIFECYCLE-001
---

# Adendo da Matriz de Consolidação Canônica — Ciclo Técnico da UIC-01

> Este adendo preserva a Matriz-base e o adendo de domínio. Ele acrescenta rastreabilidade para o ciclo técnico da Captura de Contexto.

## 1. Registro do ativo

| Campo | Valor |
|---|---|
| ID | PAS-001-CC-UIC-LIFECYCLE-001 |
| Título | Ciclo Técnico da UIC da Captura de Contexto |
| Versão | 0.1.0 |
| Estado | Draft |
| Parent | PAS-001-CC-UIC-001 |
| Estado funcional | Functionally complete |
| Estado técnico | Lifecycle technically defined |
| Progresso | 60% |
| Marco | M5.14 |

## 2. Cadeia de autoridade

| Ordem | Autoridade | Função |
|---:|---|---|
| 1 | Foundation e Princípios Permanentes | Limites fundamentais |
| 2 | GIA-000 | Arquitetura institucional |
| 3 | GLPA-001 | Arquitetura em camadas |
| 4 | PAS-001 1.0.0 | Autoridade funcional global |
| 5 | Contratos da Captura de Contexto | Autoridade especializada |
| 6 | Engineering Handoff 0.3.0 | Tradução para Product Engineering |
| 7 | UIC-01 0.3.0 | Unidade técnica da capacidade |
| 8 | Modelo de Domínio | Agregados, identidades e invariantes |
| 9 | Ciclo Técnico | Máquinas, transições e compensações |
| 10 | Contratos técnicos futuros | Interfaces e schemas |
| 11 | Código e infraestrutura | Implementação subordinada |

## 3. Rastreabilidade estado funcional–máquina técnica

| Dimensão funcional | Máquina técnica | Autoridade preservada |
|---|---|---|
| sessão | SessionLifecycle | Captura de Contexto |
| canal | ChannelLifecycle | Captura de Contexto e Platform |
| entrada original | InputLifecycle | Participante ou produtor autorizado |
| transcrição | TranscriptLifecycle | Resultado derivado |
| interpretação | InterpretationLifecycle | Resultado derivado e incerto |
| síntese | SynthesisLifecycle | Conteúdo revisável |
| confirmação | ConfirmationLifecycle | Participante ou representante |
| autorização | AuthorizationLifecycle | Autoridade contextual |
| persistência | PersistenceLifecycle | Política e autoridade aplicável |
| propagação | PropagationLifecycle | Integração minimizada |
| contestação | ContestLifecycle | Participante ou representante |
| revogação | RevocationLifecycle | Autoridade aplicável |
| operação técnica | TechnicalOperationLifecycle | Infraestrutura sem autoridade funcional |

## 4. Guardrails e mecanismos

| Guardrail | Mecanismo técnico | Estado |
|---|---|---|
| sessão não confirma conteúdo | máquinas independentes | Definido |
| operação técnica não cria fato | promoção pelo domínio | Definido |
| pausa não é abandono | transições distintas | Definido |
| timeout não é sucesso | estado TimedOut | Definido |
| correção preserva histórico | compensação e versionamento | Definido |
| revogação bloqueia novos usos | BlockingNewUses | Definido |
| confirmação parcial limita recorte | escopo granular | Definido |
| síntese desatualizada invalida confirmação | version guard | Definido |
| temporário não vira permanente | nova autoridade obrigatória | Definido |
| falha parcial preserva ativo válido | classificação por dimensão | Definido |
| retry não duplica fato | idempotency key e tentativa técnica | Definido |
| projeção não é sistema de registro | reconstrução e reconciliação | Definido |

## 5. Transições críticas rastreadas

- início somente após finalidade;
- captura somente com canal e autoridade válidos;
- processamento somente sobre entrada elegível;
- confirmação somente sobre síntese vigente apresentada;
- propagação somente sobre recorte autorizado;
- correção reabre derivados afetados;
- revogação prevalece sobre operações concorrentes;
- expiração temporária inicia descarte;
- falha de descarte mantém bloqueio;
- fechamento não apaga direitos posteriores.

## 6. Gaps

| Gap | Estado | Evidência |
|---|---|---|
| UIC01-GAP-001 | Resolved | Modelo de domínio |
| UIC01-GAP-002 | Resolved | Modelo de domínio |
| UIC01-GAP-004 | Resolved | Protocolo de transcrição e correção |
| UIC01-GAP-005 | Resolved | Política de persistência temporária |
| UIC01-GAP-006 | Open | Contratos de revogação no ciclo de 80% |
| UIC01-GAP-007 | Open | Contratos de replay e reconstrução no ciclo de 80% |
| UIC01-GAP-009 | Open | Contratos mínimos da Onda 0 no ciclo de 80% |

## 7. Testabilidade

A rastreabilidade inclui:

- 60 testes obrigatórios de transição;
- cenários de concorrência;
- cenários de falha parcial;
- cenários de retomada e troca de canal;
- correção antes e após propagação;
- revogação durante processamento e entrega;
- descarte temporário e falha de eliminação;
- reconstrução e reconciliação de projeções.

## 8. Próxima consolidação

A próxima atualização deverá registrar contratos técnicos, catálogos, schemas, compatibilidade, erros, idempotência por operação e testes de contrato da UIC-01.
