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
---

# Adendo da Matriz de Consolidação Canônica — UIC-01

> Este adendo preserva a Matriz de Consolidação Canônica-base e acrescenta a rastreabilidade da primeira Unidade de Implementação de Capacidade.

## 1. Registro do ativo

| Campo | Valor |
|---|---|
| ID | PAS-001-CC-UIC-001 |
| Título | Unidade de Implementação da Capacidade de Captura de Contexto |
| Versão | 0.1.0 |
| Estado | Draft |
| Parent | PAS-001-ENGINEERING-HANDOFF-001 |
| Capacidade | Captura de Contexto |
| Estado funcional | Functionally complete |
| Estado técnico | Normative sources mapped |
| Marco | M5.12 |

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
| 8 | UIC-01 0.1.0 | Unidade técnica da capacidade |
| 9 | Artefatos técnicos derivados | Implementação futura |

## 3. Rastreabilidade funcional-técnica

| Elemento funcional | Representação técnica candidata | Autoridade preservada |
|---|---|---|
| Registro de Captura | CaptureRecord | Captura de Contexto |
| Sessão | CaptureSession | Captura de Contexto |
| Entrada original | CaptureInput | Participante ou produtor autorizado |
| Transcrição | CaptureTranscript | Resultado derivado |
| Interpretação | CaptureInterpretation | Resultado derivado e incerto |
| Síntese | CaptureSynthesis | Conteúdo revisável |
| Confirmação | CaptureConfirmation | Participante ou representante autorizado |
| Autorização | CaptureAuthorization | Autoridade contextual |
| Recorte | CaptureSlice | Integração minimizada |
| Correção | CaptureCorrection | Registro compensatório |
| Contestação | CaptureContest | Participante ou representante autorizado |
| Revogação | CaptureRevocation | Autoridade aplicável |

## 4. Guardrails rastreados

| Guardrail | Mecanismo técnico inicial | Estado |
|---|---|---|
| Entrada não equivale a confirmação | Tipos e eventos distintos | Proposto |
| Transcrição não equivale a verdade | Proveniência e versionamento | Proposto |
| Interpretação não equivale a fato | Tipo derivado e confiança | Proposto |
| Síntese exige revisão | Estado Awaiting review | Proposto |
| Persistência exige autoridade | Policy enforcement | Proposto |
| Contexto Vivo avalia recortes | Contrato consumidor próprio | Proposto |
| Correção preserva histórico | Evento compensatório | Proposto |
| Revogação bloqueia novos usos | Protocolo a detalhar | Em aberto |
| Dados sensíveis não vão para logs | Redação e testes | Proposto |
| IA não confirma fatos | Limite de produtor | Proposto |

## 5. Dependências

- identidade do participante e do ator;
- representação e delegação;
- autorização e finalidade;
- envelope de eventos;
- idempotência;
- auditoria;
- criptografia;
- retenção e eliminação;
- observabilidade;
- versionamento de schemas;
- propagação de revogação;
- testes de contrato.

## 6. Lacunas prioritárias

1. `UIC01-GAP-001 — limite entre CaptureRecord e CaptureSession`;
2. `UIC01-GAP-002 — identidade técnica da entrada original`;
3. `UIC01-GAP-006 — propagação técnica de revogação`;
4. `UIC01-GAP-009 — contratos mínimos da Onda 0`.

## 7. Próxima consolidação

A próxima atualização deverá registrar o modelo de domínio proposto da UIC-01, incluindo agregados confirmados, identidades, objetos de valor, invariantes por comando e regras de consistência.
