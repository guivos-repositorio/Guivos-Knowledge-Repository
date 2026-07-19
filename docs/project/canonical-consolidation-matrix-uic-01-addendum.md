---
id: GKR-CANON-MATRIX-UIC01-ADDENDUM-001
title: Adendo da Matriz de Consolidação Canônica — UIC-01
status: active
version: 1.33.0
owner: Guivos
last_updated: 2026-07-19
normative: true
related:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-DOMAIN-001
---

# Adendo da Matriz de Consolidação Canônica — UIC-01

> Este adendo preserva a Matriz de Consolidação Canônica-base e registra a fundação e o modelo de domínio da primeira Unidade de Implementação de Capacidade.

## 1. Registro dos ativos

| Campo | Fundação da UIC | Modelo de domínio |
|---|---|---|
| ID | PAS-001-CC-UIC-001 | PAS-001-CC-UIC-DOMAIN-001 |
| Versão | 0.1.0 | 0.1.0 |
| Estado documental | Draft | Draft |
| Estado efetivo da UIC | Draft 0.2.0 | Domain model proposed |
| Parent | PAS-001-ENGINEERING-HANDOFF-001 | PAS-001-CC-UIC-001 |
| Capacidade | Captura de Contexto | Captura de Contexto |
| Estado funcional | Functionally complete | Functionally complete |
| Progresso técnico | 40% | 40% |
| Marco | M5.13 | M5.13 |

## 2. Cadeia de autoridade

| Ordem | Autoridade | Função |
|---:|---|---|
| 1 | Foundation e Princípios Permanentes | Limites fundamentais |
| 2 | GIA-000 | Arquitetura institucional |
| 3 | GLPA-001 | Arquitetura em camadas |
| 4 | PAS-001 1.0.0 | Autoridade funcional global |
| 5 | Mapa Final 1.0.1 | Visão navegável das capacidades |
| 6 | Contratos e extensões da Captura de Contexto | Autoridade especializada |
| 7 | Engineering Handoff 0.2.0 efetivo | Tradução para Product Engineering |
| 8 | UIC-01 0.2.0 efetivo | Unidade técnica da capacidade |
| 9 | Modelo de domínio | Decisões de agregados, identidades e invariantes |
| 10 | Artefatos técnicos derivados | Implementação futura |

## 3. Rastreabilidade funcional-técnica consolidada

| Elemento funcional | Representação técnica confirmada | Classificação | Autoridade preservada |
|---|---|---|---|
| Registro de Captura | `CaptureRecord` | Aggregate Root | Captura de Contexto |
| Sessão | `CaptureSession` | Entidade interna | Captura de Contexto |
| Finalidade | `PurposeDescriptor` | Objeto de valor versionado | Autoridade contextual |
| Entrada original | `CaptureInput` | Entidade interna | Participante ou produtor autorizado |
| Mídia original | `CaptureMediaReference` | Objeto de valor protegido | Fonte original |
| Transcrição | `CaptureTranscript` | Entidade derivada | Resultado derivado |
| Interpretação | `CaptureInterpretation` | Entidade derivada | Resultado derivado e incerto |
| Síntese | `CaptureSynthesis` | Entidade versionada | Conteúdo revisável |
| Confirmação | `CaptureConfirmation` | Entidade de evidência | Participante ou representante autorizado |
| Autorização | `CaptureAuthorizationGrant` | Aggregate Root auxiliar | Autoridade contextual |
| Recorte | `CaptureSlice` | Projeção autorizada | Integração minimizada |
| Correção | `CaptureCorrection` | Entidade compensatória | Captura de Contexto |
| Contestação | `CaptureContest` | Entidade de controle | Participante ou representante |
| Revogação | `CaptureRevocationProcess` | Process manager | Autoridade aplicável |

## 4. Decisões de consistência

| Decisão | Resultado |
|---|---|
| Limite principal | Alterações funcionais materiais passam pelo `CaptureRecord` |
| Sessão | Subordinada ao registro; não emite recorte independentemente |
| Autorização | Consistência imediata em agregado auxiliar |
| Derivados | Consistência eventual permitida com proveniência |
| Projeções | Reconstruíveis e não autoritativas |
| Concorrência | `expected_version` e rejeição de sobrescrita silenciosa |
| Idempotência | Mesma chave e conteúdo preservam o resultado original |
| Reconstrução | Estado efetivo, eventos, fontes, correções e revogações |

## 5. Guardrails rastreados

| Guardrail | Mecanismo técnico | Estado |
|---|---|---|
| Entrada não equivale a confirmação | Entidades e IDs distintos | Confirmado no domínio |
| Transcrição não equivale a verdade | Derivação versionada e proveniência | Confirmado no domínio |
| Interpretação não equivale a fato | Confiança, incerteza e autoridade limitada | Confirmado no domínio |
| Síntese exige revisão | Versão apresentada vinculada à confirmação | Confirmado no domínio |
| Persistência exige autoridade | `CaptureAuthorizationGrant` | Proposto e delimitado |
| Contexto Vivo avalia recortes | `CaptureSlice` minimizado | Confirmado no domínio |
| Correção preserva histórico | Entidade compensatória e reconstrução | Confirmado no domínio |
| Revogação bloqueia novos usos | Processo de revogação explícito | Proposto e diagramado |
| Dados sensíveis não vão para logs | Referências protegidas e testes | Confirmado como requisito |
| IA não confirma fatos | Limite de produtor e invariantes | Confirmado no domínio |

## 6. Gaps

| Gap | Estado | Evidência |
|---|---|---|
| `UIC01-GAP-001` | Resolved | Limite do agregado e cardinalidade confirmados |
| `UIC01-GAP-002` | Resolved | Política de identidade de `CaptureInput` confirmada |
| `UIC01-GAP-003` | Open | Tecnologia de conteúdo multimodal permanece aberta |
| `UIC01-GAP-004` | Open | Protocolo detalhado de transcrição e correção |
| `UIC01-GAP-005` | Open | Política completa de persistência temporária |
| `UIC01-GAP-006` | Open | Protocolo operacional completo de revogação |
| `UIC01-GAP-007` | Open | Estratégia final de reconstrução depende de ADR |
| `UIC01-GAP-008` | Open | Política de busca sensível |
| `UIC01-GAP-009` | Open | Contratos mínimos da Onda 0 |
| `UIC01-GAP-010` | Open | Matriz técnica final dos guardrails |

## 7. Próxima consolidação

A próxima atualização deverá registrar o ciclo técnico completo da UIC-01, incluindo máquinas de estado independentes, transições, compensações, timeouts, falhas parciais e testes de ciclo, elevando a unidade para `Lifecycle technically defined — 60%`.
