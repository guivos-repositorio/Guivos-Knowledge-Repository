---
id: PAS-001-CC-UIC-CONTRACTS-001
title: Contratos Técnicos da Unidade de Implementação da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
parent: PAS-001-CC-UIC-001
normative: true
related:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-LIFECYCLE-001
  - PAS-001-CC-LIFECYCLE-001
  - PAS-001-CC-EVENT-INTEGRATION-001
  - PAS-001-CC-CONTRACT-001
  - GIA-000
  - GLPA-001
---

# PAS-001-CC-UIC-CONTRACTS-001 — Contratos Técnicos da Unidade de Implementação da Captura de Contexto

> **Estado:** `Draft 0.1.0 — Contracts technically proposed`.
>
> **Progresso de referência da UIC-01:** `80%`.
>
> Este documento transforma o modelo de domínio e o ciclo técnico da Captura de Contexto em contratos versionados, testáveis e independentes de linguagem, framework, banco, broker, nuvem ou topologia final de serviços.

# 7301. Pergunta central

> Como permitir que superfícies, domínio, Intelligence, Platform Layer e capacidades consumidoras troquem comandos, eventos, recortes, correções, revogações e confirmações técnicas sem confundir transporte com autoridade, entrega com efeito, processamento com confirmação ou recorte com Contexto Vivo?

# 7302. Autoridade e ordem de prevalência

A interpretação deverá respeitar:

1. Foundation e Princípios Permanentes;
2. `GIA-000`;
3. `GLPA-001`;
4. `PAS-001 1.0.0`;
5. `PAS-001-CAPABILITY-MAP-001 1.0.1`;
6. `PAS-001-CC-LIFECYCLE-001 1.0.0`;
7. `PAS-001-CC-EVENT-INTEGRATION-001 1.0.0`;
8. `PAS-001-CC-CONTRACT-001 1.0.0`;
9. `PAS-001-CC-UIC-DOMAIN-001 0.1.0`;
10. `PAS-001-CC-UIC-LIFECYCLE-001 0.1.0`;
11. este documento;
12. schemas e exemplos derivados;
13. código, configuração e infraestrutura.

Nenhuma implementação poderá ampliar autoridade, finalidade, escopo, retenção ou significado além dessa ordem.

# 7303. Resultado técnico alcançado

Este documento conclui, no nível de proposta contratual:

- modelo comum de comandos;
- modelo comum de respostas;
- catálogo versionado de comandos;
- modelo comum de eventos funcionais;
- modelo comum de eventos técnicos;
- catálogo versionado de eventos;
- contratos síncronos e assíncronos;
- contratos de recorte com consumidores;
- protocolo contratual de correção;
- protocolo contratual de revogação;
- estratégia contratual de reconstrução;
- dependências mínimas da Onda 0;
- códigos estáveis de erro;
- regras de idempotência por operação;
- regras de ordenação e causalidade;
- política de compatibilidade e evolução;
- requisitos de segurança e minimização;
- testes de contrato;
- resolução de `UIC01-GAP-006`, `UIC01-GAP-007` e `UIC01-GAP-009`.

# 7304. Limites preservados

Este documento não decide:

- protocolo físico de transporte;
- produto de mensageria;
- padrão de serialização definitivo;
- framework de API;
- banco de dados;
- linguagem;
- provedor de identidade;
- provedor de nuvem;
- quantidade de serviços;
- distribuição entre times;
- uso integral ou parcial de event sourcing;
- estratégia física de mídia;
- desenho visual das superfícies;
- autorização de produção.

Contrato lógico não equivale a endpoint, tópico, tabela, serviço ou fila obrigatória.

# 7305. Princípios contratuais

Todos os contratos deverão preservar:

1. comando é solicitação, não fato;
2. evento funcional é fato reconhecido e persistido;
3. evento técnico não comprova autoridade humana;
4. entrada original permanece distinta dos derivados;
5. transcrição permanece corrigível;
6. interpretação permanece incerta e contestável;
7. síntese permanece versionada e revisável;
8. confirmação é granular e vinculada à versão apresentada;
9. autorização é específica por finalidade, escopo, consumidor e período;
10. persistência temporária não se converte automaticamente em permanência;
11. recorte é minimizado e não representa contexto definitivo;
12. consumidor realiza decisão própria;
13. correção é compensatória;
14. revogação bloqueia novos usos antes da propagação completa;
15. entrega técnica não equivale a processamento funcional;
16. processamento funcional não equivale a efeito admitido;
17. replay não cria nova manifestação humana;
18. idempotência limita cada chave a um efeito material;
19. incompatibilidade de significado exige nova versão maior;
20. conteúdo sensível não deve ser replicado quando referência protegida for suficiente.

# 7306. Convenções de identidade

## 7306.1 Identificadores permanentes

São permanentes e não reutilizáveis:

- `capture_record_id`;
- `capture_session_id`;
- `capture_input_id`;
- `media_reference_id`;
- `transcript_id`;
- `interpretation_id`;
- `synthesis_id`;
- `confirmation_id`;
- `authorization_id`;
- `persistence_decision_id`;
- `capture_slice_id`;
- `correction_id`;
- `contest_id`;
- `revocation_id`;
- `event_id`;
- `command_id`;
- `delivery_id`;
- `processing_attempt_id`;
- `contract_instance_id`.

## 7306.2 Regras

- identificadores são opacos;
- identificadores não carregam classificação humana;
- identificadores não expõem sequência global;
- o mesmo elemento mantém identidade entre retries;
- novas versões de conteúdo mantêm identidade de entidade e avançam `entity_version`;
- substituição material preserva `supersedes_id` e `superseded_by_id`;
- eventos possuem identidade própria e não substituem a identidade do elemento;
- IDs de transporte não substituem IDs funcionais.

# 7307. Tipos comuns

## 7307.1 `ContractVersion`

```yaml
contract_name: string
major: integer
minor: integer
patch: integer
schema_revision: integer
published_at: datetime
compatibility: backward | forward | full | none
```

## 7307.2 `ActorContext`

```yaml
actor_id: string
actor_role: participant | representative | journey_experience | journey_domain | intelligence | platform | external_source | professional | organization | auditor | policy
participant_id: string | null
representation_id: string | null
authority_scope: string[]
identity_mode: authenticated | provisional | pseudonymous | temporary
assurance_level: string
```

## 7307.3 `PurposeContext`

```yaml
purpose_id: string
purpose_code: string
description_reference: string
allowed_operations: string[]
prohibited_operations: string[]
authorized_consumers: string[]
valid_from: datetime
valid_until: datetime | null
jurisdiction: string | null
```

## 7307.4 `SensitivityContext`

```yaml
classification: public | internal | personal | sensitive | highly_sensitive
categories: string[]
third_party_data: boolean
minor_data: boolean
shared_device_restrictions: boolean
log_policy: none | identifiers_only | redacted
index_policy: prohibited | metadata_only | protected
```

## 7307.5 `TemporalContext`

```yaml
occurred_at: datetime | null
captured_at: datetime | null
received_at: datetime
recorded_at: datetime | null
effective_at: datetime | null
valid_from: datetime | null
valid_until: datetime | null
expires_at: datetime | null
```

## 7307.6 `ProvenanceContext`

```yaml
source_type: participant | representative | device | document | external_system | intelligence | platform | derived
source_id: string
source_version: string | null
transformation_chain: string[]
model_reference: string | null
method_reference: string | null
confidence: number | null
uncertainty_codes: string[]
```

# 7308. Envelope comum de comando

```yaml
command_id: string
command_type: string
command_version: 1.0.0
contract_instance_id: string
capture_record_id: string | null
capture_session_id: string | null
expected_aggregate_version: integer | null
actor: ActorContext
purpose: PurposeContext
sensitivity: SensitivityContext
requested_at: datetime
idempotency_key: string
correlation_id: string
causation_id: string | null
channel: string
payload: object
client_context:
  client_id: string
  client_version: string
  locale: string | null
  accessibility_profile_reference: string | null
```

## 7308.1 Regras do comando

- `command_id` identifica a solicitação funcional;
- `idempotency_key` identifica o efeito material pretendido;
- retry preserva ambos quando o efeito pretendido for o mesmo;
- `expected_aggregate_version` é obrigatório em alterações materiais posteriores à criação;
- `actor`, `purpose` e `sensitivity` são avaliados antes do payload;
- payload incompatível é rejeitado antes de qualquer efeito material;
- comando aceito ainda pode resultar em processamento assíncrono;
- comando rejeitado não publica evento de sucesso;
- comando parcialmente aceito deverá declarar exatamente o escopo admitido.

# 7309. Envelope comum de resposta síncrona

```yaml
request_command_id: string
response_id: string
status: accepted | rejected | conflict | pending | partially_accepted
capture_record_id: string | null
capture_session_id: string | null
aggregate_version: integer | null
result_reference: string | null
accepted_scope: string[]
rejected_scope: string[]
error:
  code: string | null
  category: domain | authorization | validation | conflict | lifecycle | integration | technical | security | privacy | compatibility | null
  message_reference: string | null
  retryable: boolean
  retry_after: duration | null
  current_state_reference: string | null
warnings: string[]
recorded_at: datetime
correlation_id: string
```

Resposta síncrona não substitui o evento funcional quando o contrato exigir fato persistido e publicável.

# 7310. Catálogo versionado de comandos

| ID | Comando | Versão | Ator permitido | Consistência | Idempotência | Resultado funcional principal |
|---|---|---:|---|---|---|---|
| `CC-CMD-001` | `StartCaptureSession` | 1.0.0 | participante, representante, Journey Experience | imediata | por participante + finalidade + solicitação | `CaptureSessionStarted` |
| `CC-CMD-002` | `ExplainCapturePurpose` | 1.0.0 | Journey Experience | imediata | por sessão + versão da explicação | `CapturePurposeExplained` |
| `CC-CMD-003` | `SelectCaptureChannel` | 1.0.0 | participante, Journey Experience | imediata | por sessão + canal + versão | `CaptureChannelSelected` |
| `CC-CMD-004` | `SubmitCaptureInput` | 1.0.0 | participante, representante, integração autorizada | imediata para reconhecimento | por entrada original | `CaptureInputReceived` |
| `CC-CMD-005` | `AttachCaptureMedia` | 1.0.0 | participante, dispositivo autorizado | imediata para referência | por mídia original | `CaptureMediaAttached` |
| `CC-CMD-006` | `PauseCaptureSession` | 1.0.0 | participante, sistema autorizado | imediata | por sessão + versão alvo | `CaptureSessionPaused` |
| `CC-CMD-007` | `ResumeCaptureSession` | 1.0.0 | participante, sistema autorizado | imediata | por sessão + versão alvo | `CaptureSessionResumed` |
| `CC-CMD-008` | `RequestCaptureProcessing` | 1.0.0 | Journey Domain | imediata para agendamento | por conjunto de fontes + finalidade | `CaptureProcessingRequested` |
| `CC-CMD-009` | `RecordCaptureTranscript` | 1.0.0 | processador autorizado | imediata para registro | por entrada + versão + método | `CaptureTranscriptProduced` |
| `CC-CMD-010` | `CorrectCaptureTranscript` | 1.0.0 | participante, autoridade competente | imediata | por transcrição + correção | `CaptureTranscriptCorrected` |
| `CC-CMD-011` | `RecordCaptureInterpretation` | 1.0.0 | Intelligence, regra autorizada, profissional competente | imediata para registro | por fontes + método + versão | `CaptureInterpretationProduced` |
| `CC-CMD-012` | `RecordCaptureSynthesis` | 1.0.0 | Journey Domain, Intelligence assistiva | imediata para versão | por fontes + versão | `CaptureSynthesisProduced` |
| `CC-CMD-013` | `PresentCaptureSynthesis` | 1.0.0 | Journey Experience | imediata | por síntese + versão + participante | `CaptureSynthesisPresented` |
| `CC-CMD-014` | `ConfirmCaptureSynthesis` | 1.0.0 | participante, representante válido | imediata | por síntese + versão + escopo | `CaptureSynthesisConfirmed` |
| `CC-CMD-015` | `PartiallyConfirmCaptureSynthesis` | 1.0.0 | participante, representante válido | imediata | por síntese + versão + escopo | `CaptureSynthesisPartiallyConfirmed` |
| `CC-CMD-016` | `RequestCaptureCorrection` | 1.0.0 | participante, representante válido | imediata | por alvo + fundamento material | `CaptureCorrectionRequested` |
| `CC-CMD-017` | `RegisterCaptureCorrection` | 1.0.0 | autoridade competente | imediata | por alvo + versão corrigida | `CaptureCorrectionRegistered` |
| `CC-CMD-018` | `AuthorizeCapturePersistence` | 1.0.0 | participante, autoridade aplicável | imediata | por conteúdo + finalidade + consumidor + período | `CapturePersistenceAuthorized` |
| `CC-CMD-019` | `PersistCaptureTemporarily` | 1.0.0 | Journey Domain | imediata | por conteúdo + política temporal | `TemporaryCapturePersistenceRegistered` |
| `CC-CMD-020` | `IssueCaptureSlice` | 1.0.0 | Journey Domain | imediata para emissão | por consumidor + finalidade + fontes + versão | `CaptureSliceIssued` |
| `CC-CMD-021` | `AcknowledgeCaptureSlice` | 1.0.0 | consumidor autorizado | imediata | por recorte + consumidor | `CaptureSliceAcknowledged` |
| `CC-CMD-022` | `RejectCaptureSlice` | 1.0.0 | consumidor autorizado | imediata | por recorte + consumidor + motivo | `CaptureSliceRejected` |
| `CC-CMD-023` | `ContestCaptureRecord` | 1.0.0 | participante, representante válido | imediata | por alvo + escopo de contestação | `CaptureRecordContested` |
| `CC-CMD-024` | `RevokeCaptureAuthorization` | 1.0.0 | participante, autoridade aplicável | imediata para bloqueio | por autorização + escopo | `CaptureAuthorizationRevoked` |
| `CC-CMD-025` | `ConfirmCorrectionPropagation` | 1.0.0 | consumidor autorizado | imediata | por correção + consumidor + versão | `CaptureCorrectionPropagationConfirmed` |
| `CC-CMD-026` | `ConfirmRevocationPropagation` | 1.0.0 | consumidor autorizado | imediata | por revogação + consumidor + versão | `CaptureRevocationPropagationConfirmed` |
| `CC-CMD-027` | `CloseCaptureSession` | 1.0.0 | participante, sistema autorizado | imediata | por sessão + versão alvo | `CaptureSessionClosed` |
| `CC-CMD-028` | `ExpireCaptureSession` | 1.0.0 | política temporal | imediata | por sessão + política | `CaptureSessionExpired` |
| `CC-CMD-029` | `AbandonCaptureSession` | 1.0.0 | participante, política | imediata | por sessão + causa | `CaptureSessionAbandoned` |
| `CC-CMD-030` | `RebuildCaptureProjection` | 1.0.0 | operação autorizada | assíncrona | por projeção + checkpoint + versão | evento técnico de reconstrução |

# 7311. Contratos críticos de comando

## 7311.1 `StartCaptureSession`

Payload mínimo:

```yaml
participant_reference: string | null
identity_mode: authenticated | provisional | pseudonymous | temporary
purpose_id: string
requested_channel: string
representation_id: string | null
temporary_mode_requested: boolean
```

Precondições:

- finalidade existente e apresentável;
- ator identificado;
- representação válida quando aplicável;
- canal admissível para sensibilidade esperada;
- ausência de bloqueio material vigente.

Falhas estáveis:

- `CC-AUTH-001` autoridade insuficiente;
- `CC-PURPOSE-001` finalidade ausente;
- `CC-IDENTITY-001` identidade incompatível;
- `CC-LIFECYCLE-001` sessão não pode ser iniciada;
- `CC-SECURITY-001` canal inadequado.

## 7311.2 `SubmitCaptureInput`

Payload mínimo:

```yaml
capture_input_id: string
input_type: text | voice | audio | image | video | document | selection | structured_response | imported_data
content_reference: string | null
inline_content: string | null
content_hash: string
content_length: integer | null
source_occurred_at: datetime | null
language: string | null
provenance: ProvenanceContext
retention_request: temporary | purpose_bound | authorized_persistent
```

Regras:

- `capture_input_id` nasce antes do processamento;
- `content_hash` auxilia integridade, não substitui identidade;
- conteúdo sensível deverá preferir referência protegida;
- duplicidade com mesmo ID e mesmo hash retorna o resultado anterior;
- mesmo ID com hash diferente retorna `CC-IDEMPOTENCY-002`;
- reconhecimento da entrada não confirma interpretação.

## 7311.3 `RecordCaptureTranscript`

Payload mínimo:

```yaml
transcript_id: string
capture_input_id: string
transcript_version: integer
text_reference: string
language: string
method_reference: string
model_reference: string | null
confidence: number | null
uncertainty_codes: string[]
source_segments: object[]
```

Regras:

- transcrição referencia exatamente uma entrada original;
- versão anterior permanece preservada;
- baixa confiança permanece explícita;
- transcrição produzida não confirma conteúdo;
- retry técnico não cria nova versão sem alteração material.

## 7311.4 `RecordCaptureInterpretation`

Payload mínimo:

```yaml
interpretation_id: string
interpretation_version: integer
source_references: string[]
information_nature: interpretation | hypothesis | inference | estimate | observation
statement_reference: string
method_reference: string
model_reference: string | null
confidence: number | null
uncertainty_codes: string[]
alternative_interpretations: string[]
limitations: string[]
```

Regras:

- nenhuma interpretação pode declarar natureza `participant_statement`;
- fontes devem ser rastreáveis;
- método e autoria são obrigatórios;
- efeitos materiais permanecem bloqueados quando contestada ou inconclusiva.

## 7311.5 `RecordCaptureSynthesis`

Payload mínimo:

```yaml
synthesis_id: string
synthesis_version: integer
source_references: string[]
sections: object[]
uncertainty_codes: string[]
excluded_topics: string[]
valid_until: datetime | null
review_required: boolean
```

Regras:

- síntese é versão, não verdade integral;
- toda síntese material exige revisão;
- revisão aponta para versão exata;
- correção de fonte relevante invalida ou limita a versão afetada.

## 7311.6 `ConfirmCaptureSynthesis`

Payload mínimo:

```yaml
confirmation_id: string
synthesis_id: string
synthesis_version: integer
confirmed_scope: object[]
excluded_scope: object[]
purpose_id: string
consumer_scope: string[]
valid_until: datetime | null
participant_statement_reference: string
```

Precondições:

- síntese apresentada ao ator correto;
- versão apresentada igual à versão confirmada;
- finalidade compreensível;
- escopo granular;
- ausência de correção ou contestação bloqueante;
- autoridade válida.

Falhas:

- `CC-CONFLICT-002` síntese desatualizada;
- `CC-AUTH-002` ator não pode confirmar;
- `CC-CONFIRMATION-001` escopo inválido;
- `CC-LIFECYCLE-006` revisão não concluída.

## 7311.7 `AuthorizeCapturePersistence`

Payload mínimo:

```yaml
authorization_id: string
content_scope: object[]
purpose_id: string
authorized_consumers: string[]
allowed_operations: string[]
prohibited_operations: string[]
valid_from: datetime
valid_until: datetime | null
retention_policy_id: string
revocation_policy_id: string
```

Autorização não poderá ser inferida de confirmação, uso da interface ou aceitação de termos gerais.

## 7311.8 `IssueCaptureSlice`

Payload mínimo:

```yaml
capture_slice_id: string
consumer_id: string
consumer_contract_version: string
purpose_id: string
source_references: string[]
confirmation_references: string[]
authorization_references: string[]
fields: object[]
valid_until: datetime | null
correction_channel: string
revocation_channel: string
```

Precondições:

- consumidor registrado;
- contrato compatível;
- finalidade admitida;
- escopo minimizado;
- confirmação suficiente quando aplicável;
- autorização vigente;
- nenhuma contestação ou revogação bloqueante;
- capacidade de receber correção e revogação.

## 7311.9 `RegisterCaptureCorrection`

Payload mínimo:

```yaml
correction_id: string
target_type: input | transcript | interpretation | synthesis | confirmation | association | slice
target_id: string
target_version: integer
corrected_value_reference: string
reason_code: string
actor_statement_reference: string | null
affected_derivative_policy: reopen | limit | replace | review_required
```

A correção preserva valor anterior, registra novo valor e inicia identificação de derivados e consumidores afetados.

## 7311.10 `RevokeCaptureAuthorization`

Payload mínimo:

```yaml
revocation_id: string
authorization_id: string
revoked_scope: object[]
effective_at: datetime
reason_code: string | null
requested_retention_action: delete | restrict | expire | preserve_legitimate_residual
```

Efeito imediato:

- bloquear novos usos no escopo;
- bloquear novos recortes;
- interromper operações não irreversíveis;
- identificar consumidores e cópias conhecidas;
- iniciar propagação verificável.

# 7312. Envelope comum de evento funcional

```yaml
event_id: string
event_type: string
event_version: 1.0.0
schema_revision: integer
capture_record_id: string
aggregate_version: integer
expected_aggregate_version: integer
capture_session_id: string | null
entity_type: string
entity_id: string | null
entity_version: integer | null
participant_id: string | null
actor: ActorContext
purpose: PurposeContext
sensitivity: SensitivityContext
temporal: TemporalContext
provenance: ProvenanceContext
information_nature: string
confirmation_scope: object[]
authorization_references: string[]
authorized_consumers: string[]
retention_policy_id: string | null
correlation_id: string
causation_id: string | null
idempotency_key: string
payload: object
integrity:
  payload_hash: string
  previous_event_reference: string | null
```

## 7312.1 Regras de publicação

Um evento funcional material somente pode ser publicado quando:

1. o fato ocorreu;
2. identidade mínima foi validada;
3. finalidade foi registrada;
4. autoridade foi delimitada;
5. estado anterior foi preservado;
6. novo estado foi persistido;
7. versão do agregado avançou;
8. sensibilidade foi classificada;
9. payload foi minimizado;
10. idempotência está disponível;
11. consumidores autorizados foram delimitados;
12. correção e revogação são possíveis.

# 7313. Catálogo versionado de eventos funcionais

| ID | Evento | Versão | Entidade principal | Publicável externamente | Observação |
|---|---|---:|---|---|---|
| `CC-EVT-001` | `CaptureSessionStarted` | 1.0.0 | sessão | não por padrão | criação não autoriza coleta irrestrita |
| `CC-EVT-002` | `CapturePurposeExplained` | 1.0.0 | sessão | não | registra versão explicada |
| `CC-EVT-003` | `CaptureChannelSelected` | 1.0.0 | sessão | não | canal não amplia finalidade |
| `CC-EVT-004` | `CaptureInputReceived` | 1.0.0 | entrada | não | referência protegida preferencial |
| `CC-EVT-005` | `CaptureMediaAttached` | 1.0.0 | mídia | não | sem conteúdo bruto no evento |
| `CC-EVT-006` | `CaptureSessionPaused` | 1.0.0 | sessão | não | preserva demais máquinas |
| `CC-EVT-007` | `CaptureSessionResumed` | 1.0.0 | sessão | não | registra revalidações |
| `CC-EVT-008` | `CaptureProcessingRequested` | 1.0.0 | processamento | interno | não comprova resultado |
| `CC-EVT-009` | `CaptureTranscriptProduced` | 1.0.0 | transcrição | interno | inclui confiança e método |
| `CC-EVT-010` | `CaptureTranscriptCorrected` | 1.0.0 | transcrição | interno e afetados | inicia reavaliação de derivados |
| `CC-EVT-011` | `CaptureInterpretationProduced` | 1.0.0 | interpretação | interno | natureza derivada explícita |
| `CC-EVT-012` | `CaptureSynthesisProduced` | 1.0.0 | síntese | não | exige apresentação |
| `CC-EVT-013` | `CaptureSynthesisPresented` | 1.0.0 | síntese | não | registra versão apresentada |
| `CC-EVT-014` | `CaptureSynthesisPartiallyConfirmed` | 1.0.0 | confirmação | conforme finalidade | somente escopo confirmado |
| `CC-EVT-015` | `CaptureSynthesisConfirmed` | 1.0.0 | confirmação | conforme finalidade | não autoriza persistência automaticamente |
| `CC-EVT-016` | `CaptureCorrectionRequested` | 1.0.0 | correção | afetados | limita efeitos incompatíveis |
| `CC-EVT-017` | `CaptureCorrectionRegistered` | 1.0.0 | correção | afetados | compensatório |
| `CC-EVT-018` | `CapturePersistenceAuthorized` | 1.0.0 | autorização | consumidores delimitados | escopo e validade obrigatórios |
| `CC-EVT-019` | `TemporaryCapturePersistenceRegistered` | 1.0.0 | persistência | não | expiração obrigatória |
| `CC-EVT-020` | `CaptureSliceIssued` | 1.0.0 | recorte | consumidor específico | minimizado |
| `CC-EVT-021` | `CaptureSliceAcknowledged` | 1.0.0 | entrega | produtor | recebimento não equivale a admissão |
| `CC-EVT-022` | `CaptureSliceRejected` | 1.0.0 | entrega | produtor | ausência de efeito explícita |
| `CC-EVT-023` | `CaptureRecordContested` | 1.0.0 | contestação | afetados | bloqueia efeitos materiais aplicáveis |
| `CC-EVT-024` | `CaptureAuthorizationRevoked` | 1.0.0 | revogação | todos os afetados | bloqueio imediato de novos usos |
| `CC-EVT-025` | `CaptureCorrectionPropagationConfirmed` | 1.0.0 | correção | coordenador | confirmação por consumidor |
| `CC-EVT-026` | `CaptureRevocationPropagationConfirmed` | 1.0.0 | revogação | coordenador | confirmação por consumidor |
| `CC-EVT-027` | `CaptureCorrectionPropagated` | 1.0.0 | correção | auditoria | somente após suficiência |
| `CC-EVT-028` | `CaptureRevocationPropagated` | 1.0.0 | revogação | auditoria | não exige eliminação de retenção legítima |
| `CC-EVT-029` | `CaptureSessionClosed` | 1.0.0 | sessão | não | não impede direito posterior |
| `CC-EVT-030` | `CaptureSessionExpired` | 1.0.0 | sessão | não | não autoriza descarte fora da política |
| `CC-EVT-031` | `CaptureSessionAbandoned` | 1.0.0 | sessão | não | não representa fracasso humano |
| `CC-EVT-032` | `CaptureFailureRegistered` | 1.0.0 | registro | interno | falha explícita e localizada |

# 7314. Eventos técnicos

Eventos técnicos usam envelope separado e não avançam automaticamente o agregado funcional.

```yaml
technical_event_id: string
technical_event_type: string
technical_event_version: 1.0.0
processing_attempt_id: string | null
delivery_id: string | null
capture_record_id: string | null
capture_session_id: string | null
related_functional_event_id: string | null
operation: string
state: scheduled | running | succeeded | failed_recoverable | failed_unrecoverable | timed_out | compensating | compensated
occurred_at: datetime
recorded_at: datetime
correlation_id: string
causation_id: string | null
idempotency_key: string
technical_metadata: object
```

Eventos técnicos mínimos:

- `ProcessingAttemptStarted`;
- `ProcessingAttemptTimedOut`;
- `ProcessingRetryScheduled`;
- `TechnicalResultAvailable`;
- `ProjectionRebuildStarted`;
- `ProjectionRebuildCompleted`;
- `ProjectionRebuildFailed`;
- `ConsumerDeliveryAttempted`;
- `ConsumerDeliveryAcknowledged`;
- `ConsumerDeliveryFailed`;
- `TemporaryAssetDeletionScheduled`;
- `TemporaryAssetDeletionCompleted`;
- `TemporaryAssetDeletionFailed`;
- `IncompatibleContractIsolated`.

# 7315. Contratos síncronos

Contratos síncronos são permitidos para:

- validação de autoridade;
- validação de finalidade;
- leitura de estado vigente;
- reconhecimento de comando;
- criação e transição imediata do agregado;
- consulta de compatibilidade;
- admissão preliminar de recorte;
- obtenção de estado de propagação.

Não devem exigir conclusão síncrona de:

- transcrição;
- interpretação;
- síntese automatizada;
- reconstrução ampla;
- propagação para múltiplos consumidores;
- eliminação distribuída;
- reindexação completa.

# 7316. Contratos assíncronos

## 7316.1 Semântica mínima

- entrega poderá ocorrer mais de uma vez;
- processamento deverá ser idempotente;
- ordenação será garantida ou verificada por `capture_record_id` e `aggregate_version`;
- evento fora de ordem será isolado ou mantido pendente;
- incompatibilidade será rejeitada sem perda silenciosa;
- dead letter ou mecanismo equivalente deverá preservar correlação;
- retry não altera significado;
- confirmação de transporte não substitui confirmação funcional;
- timeout não presume falha humana;
- consumidor deverá responder quando correção ou revogação exigir confirmação.

## 7316.2 Estados de entrega

```text
Created
→ Scheduled
→ Attempted
→ TransportAcknowledged
→ ConsumerAccepted, ConsumerRejected ou ConsumerPending
→ EffectConfirmed quando aplicável
```

Estados terminais:

- `ConsumerAccepted`;
- `ConsumerRejected`;
- `Expired`;
- `RevokedBeforeEffect`;
- `FailedUnrecoverable`.

`TransportAcknowledged` não é terminal para recortes materiais, correções ou revogações.

# 7317. Contrato comum de consumidor

Todo consumidor deverá declarar:

```yaml
consumer_id: string
consumer_contract_name: string
consumer_contract_version: string
accepted_event_versions: object
accepted_slice_versions: object
allowed_purposes: string[]
allowed_information_natures: string[]
allowed_sensitivity: string[]
prohibited_fields: string[]
required_confirmation_levels: string[]
correction_endpoint_reference: string
revocation_endpoint_reference: string
acknowledgement_policy: string
retention_policy_id: string
failure_policy_id: string
```

O consumidor deverá:

- validar versão;
- validar finalidade;
- validar autoridade;
- validar escopo e sensibilidade;
- processar idempotentemente;
- decidir sob contrato próprio;
- preservar incerteza e proveniência;
- registrar admissão, rejeição ou pendência;
- receber correções;
- receber revogações;
- bloquear novos usos durante revogação;
- não ampliar significado.

# 7318. Contrato com Contexto Vivo

## 7318.1 Operação lógica

`EvaluateCaptureSliceForLivingContext`

Entrada:

```yaml
capture_slice_id: string
slice_version: integer
participant_id: string
purpose_id: string
fields: object[]
source_references: string[]
confirmation_references: string[]
authorization_references: string[]
provenance: ProvenanceContext
sensitivity: SensitivityContext
valid_until: datetime | null
```

Saída:

```yaml
evaluation_id: string
status: admitted | partially_admitted | rejected | needs_review | deferred
admitted_fields: string[]
rejected_fields: string[]
reason_codes: string[]
living_context_effect_references: string[]
consumer_aggregate_version: integer | null
correction_subscription_confirmed: boolean
revocation_subscription_confirmed: boolean
```

## 7318.2 Limites

- Captura de Contexto não atualiza diretamente o Contexto Vivo;
- Contexto Vivo avalia admissibilidade sob sua própria autoridade;
- rejeição não é falha do participante;
- admissão parcial não amplia confirmação;
- o resultado retorna à Captura de Contexto;
- correção posterior deve alcançar efeitos admitidos;
- revogação posterior deve bloquear novos usos e revisar efeitos aplicáveis.

# 7319. Contrato com Guivos Intelligence

Intelligence poderá receber somente:

- fontes autorizadas;
- referência de finalidade;
- classificação de sensibilidade;
- restrições de inferência;
- versão do método;
- requisitos de proveniência;
- política de retenção;
- escopo de saída esperado.

Saída obrigatória:

```yaml
processing_attempt_id: string
output_type: transcript | interpretation | synthesis_candidate | classification | conflict_signal
source_references: string[]
method_reference: string
model_reference: string
model_version: string
confidence: number | null
uncertainty_codes: string[]
limitations: string[]
output_reference: string
human_review_required: boolean
```

Intelligence não pode retornar `confirmation`, `authorization`, `living_context_fact`, `goal`, `life_event` ou `evolution` como fato reconhecido.

# 7320. Contrato com Journey Experience

Journey Experience poderá:

- iniciar comandos de superfície;
- apresentar finalidade;
- apresentar síntese;
- coletar manifestação explícita;
- exibir estado, falha, correção e revogação;
- oferecer pausa, retomada e encerramento.

Deverá preservar:

- versão do conteúdo apresentado;
- ator e participante;
- opções disponíveis;
- acessibilidade;
- ausência de dark patterns;
- separação entre revisão e autorização;
- ausência de confirmação presumida.

# 7321. Contratos de auditoria e observabilidade

Auditoria recebe referências suficientes para verificar:

- autoridade;
- finalidade;
- versão;
- transição;
- idempotência;
- correção;
- revogação;
- consumidores;
- retenção residual.

Observabilidade recebe, por padrão:

- identificadores opacos;
- tipos de operação;
- estados;
- durações;
- códigos de erro;
- versões contratuais;
- indicadores de sensibilidade sem conteúdo bruto.

# 7322. Protocolo contratual de correção

## 7322.1 Fluxo

```text
correção solicitada
→ autoridade e alvo validados
→ efeitos incompatíveis limitados
→ correção persistida
→ novo evento funcional publicado
→ derivados afetados identificados
→ novas versões produzidas quando necessárias
→ recortes afetados identificados
→ consumidores notificados
→ cada consumidor confirma aplicado, rejeitado, não aplicável ou pendente
→ suficiência avaliada
→ correção propagada
```

## 7322.2 Mensagem de propagação

```yaml
correction_id: string
correction_version: integer
target_reference: string
previous_value_reference: string
corrected_value_reference: string
effective_at: datetime
affected_slice_ids: string[]
affected_consumer_effects: object[]
required_action: replace | invalidate | limit | review | delete_optional_copy
response_due_at: datetime
correlation_id: string
```

## 7322.3 Resposta do consumidor

```yaml
correction_id: string
consumer_id: string
status: applied | partially_applied | rejected | not_applicable | pending
applied_effect_references: string[]
pending_effect_references: string[]
residual_references: string[]
reason_codes: string[]
confirmed_at: datetime
consumer_contract_version: string
```

Correção não é concluída somente porque a mensagem foi entregue.

# 7323. Protocolo contratual de revogação

## 7323.1 Decisão central

A revogação utiliza coordenação explícita e verificável. O estado global é derivado das confirmações conhecidas, das obrigações de cada consumidor e da retenção residual legítima.

## 7323.2 Fluxo

```text
revogação solicitada
→ autoridade validada
→ revogação persistida
→ novos usos bloqueados imediatamente
→ operações em andamento avaliadas
→ consumidores, recortes e efeitos conhecidos identificados
→ mensagens versionadas emitidas
→ confirmações recebidas
→ falhas e pendências reconciliadas
→ retenção residual legitimada e restrita
→ suficiência de propagação avaliada
→ revogação propagada
```

## 7323.3 Mensagem de revogação

```yaml
revocation_id: string
revocation_version: integer
authorization_id: string
revoked_scope: object[]
effective_at: datetime
capture_slice_ids: string[]
consumer_effect_references: object[]
required_action: stop_new_use | invalidate | delete_optional_copy | expire | restrict | preserve_legitimate_residual
response_due_at: datetime
correlation_id: string
```

## 7323.4 Resposta do consumidor

```yaml
revocation_id: string
consumer_id: string
status: applied | partially_applied | rejected | not_applicable | pending | retained_legitimately
new_uses_blocked_at: datetime
invalidated_effect_references: string[]
deleted_copy_references: string[]
residual_references: string[]
residual_basis_reference: string | null
residual_valid_until: datetime | null
reason_codes: string[]
confirmed_at: datetime
consumer_contract_version: string
```

## 7323.5 Suficiência

A revogação poderá alcançar `Propagated` quando:

- novos usos estiverem bloqueados em todos os consumidores conhecidos;
- consumidores obrigatórios tiverem respondido;
- pendências não bloqueantes estiverem registradas;
- retenções residuais tiverem fundamento, escopo e validade;
- falhas críticas estiverem escaladas;
- nenhum novo recorte puder ser emitido no escopo.

Não é requisito apagar fatos históricos mínimos legitimamente preservados, mas esses fatos não poderão sustentar novos usos incompatíveis.

# 7324. Reconstrução contratual

## 7324.1 Fonte de reconstrução

A reconstrução usa, conforme arquitetura física futura:

1. snapshot válido do `CaptureRecord`, quando existente;
2. eventos funcionais posteriores ao snapshot;
3. registros de entidades versionadas quando não representados integralmente no evento;
4. decisões de autorização e retenção;
5. correções, contestações e revogações;
6. confirmações de consumidores quando necessárias ao estado de propagação.

## 7324.2 Contrato de snapshot

```yaml
snapshot_id: string
capture_record_id: string
aggregate_version: integer
created_at: datetime
contract_versions: object
state_vector:
  sessions: object
  inputs: object
  transcripts: object
  interpretations: object
  syntheses: object
  confirmations: object
  authorizations: object
  persistence: object
  propagation: object
  contests: object
  revocations: object
last_event_id: string
integrity_hash: string
excluded_content_references: string[]
```

## 7324.3 Operação `ReconstructCaptureRecord`

Entrada:

```yaml
capture_record_id: string
target_aggregate_version: integer | latest
projection_targets: string[]
verification_level: standard | strict | forensic
```

Saída:

```yaml
reconstruction_id: string
status: completed | completed_with_warnings | failed
aggregate_version: integer
replayed_event_count: integer
ignored_duplicate_count: integer
out_of_order_count: integer
incompatible_event_references: string[]
missing_reference_codes: string[]
reconciled_projections: string[]
integrity_status: valid | warning | invalid
```

## 7324.4 Regras

- replay preserva `event_id`;
- replay não publica novamente fatos humanos;
- projeções podem ser reconstruídas sem alterar o registro;
- conteúdo legitimamente descartado não é recriado;
- ausência de conteúdo descartado permanece explícita;
- eventos incompatíveis são isolados;
- correções posteriores prevalecem sem apagar anteriores;
- revogações preservam bloqueios;
- evento fora de ordem não sobrescreve estado posterior;
- divergência entre projeção e registro é reconciliada em favor do registro.

# 7325. Dependências mínimas da Onda 0

A Onda 0 exige contratos mínimos, não implementação completa de toda a plataforma.

| ID | Dependência contratual | Obrigatoriedade | Capacidade mínima |
|---|---|---|---|
| `CC-W0-001` | Identidade e representação | Required | identificar ator, participante, modo e representação |
| `CC-W0-002` | Autoridade contextual | Required | avaliar operação, escopo, finalidade e validade |
| `CC-W0-003` | Registro transacional do agregado | Required | persistir versão e invariantes |
| `CC-W0-004` | Publicação confiável de eventos | Required | publicar após persistência sem duplicidade material |
| `CC-W0-005` | Registro de idempotência | Required | recuperar resultado anterior e detectar conflito de payload |
| `CC-W0-006` | Registro de schemas | Required | resolver versão e compatibilidade |
| `CC-W0-007` | Registro de consumidores | Required | declarar finalidade, versões, retenção, correção e revogação |
| `CC-W0-008` | Persistência temporária e expiração | Required | agendar, bloquear conversão automática e comprovar descarte |
| `CC-W0-009` | Auditoria minimizada | Required | preservar decisões, autoridade e versões |
| `CC-W0-010` | Observabilidade segura | Required | detectar falhas sem conteúdo sensível bruto |
| `CC-W0-011` | Coordenação de correção | Required | identificar e acompanhar consumidores afetados |
| `CC-W0-012` | Coordenação de revogação | Required | bloquear novos usos e acompanhar confirmações |
| `CC-W0-013` | Reconstrução e replay | Required | reconstruir agregado e projeções sem novos fatos |
| `CC-W0-014` | Proteção de referências de mídia | Required when multimodal | armazenar referência, integridade, acesso e expiração |
| `CC-W0-015` | Classificação de sensibilidade | Required | governar canal, logs, índice, retenção e consumidores |
| `CC-W0-016` | Catálogo de erros | Required | códigos estáveis e tratamento seguro |

## 7325.1 Dependências não exigidas para iniciar a Onda 0

Não são pré-requisitos para iniciar implementação controlada:

- grafo global completo;
- busca semântica ampla;
- todos os canais possíveis;
- todos os produtos Guivos;
- todos os países;
- automação integral por Intelligence;
- marketplace de modelos;
- arquitetura física definitiva de longo prazo.

# 7326. Catálogo estável de erros

## 7326.1 Autorização e identidade

| Código | Significado | Retry |
|---|---|---|
| `CC-AUTH-001` | autoridade insuficiente | não sem nova autoridade |
| `CC-AUTH-002` | ator não pode confirmar | não |
| `CC-AUTH-003` | representação expirada | após revalidação |
| `CC-IDENTITY-001` | associação incompatível | após correção |
| `CC-IDENTITY-002` | identidade insuficiente para efeito material | após elevação proporcional |

## 7326.2 Finalidade, privacidade e segurança

| Código | Significado | Retry |
|---|---|---|
| `CC-PURPOSE-001` | finalidade ausente | após informar finalidade |
| `CC-PURPOSE-002` | finalidade incompatível | não com mesmo contrato |
| `CC-PRIVACY-001` | escopo excessivo | após minimização |
| `CC-PRIVACY-002` | retenção incompatível | após nova política |
| `CC-SECURITY-001` | canal inadequado | em canal adequado |
| `CC-SECURITY-002` | conteúdo sensível proibido no payload | com referência protegida |

## 7326.3 Validação e compatibilidade

| Código | Significado | Retry |
|---|---|---|
| `CC-VALIDATION-001` | schema inválido | após correção |
| `CC-VALIDATION-002` | referência obrigatória ausente | após correção |
| `CC-COMPAT-001` | versão maior não suportada | após atualização ou adaptador aprovado |
| `CC-COMPAT-002` | significado incompatível | não sem novo contrato |
| `CC-COMPAT-003` | consumidor sem canal de correção ou revogação | após adequação |

## 7326.4 Concorrência e idempotência

| Código | Significado | Retry |
|---|---|---|
| `CC-CONFLICT-001` | versão do agregado divergente | após releitura |
| `CC-CONFLICT-002` | síntese desatualizada | após nova apresentação |
| `CC-IDEMPOTENCY-001` | efeito já processado | retornar resultado anterior |
| `CC-IDEMPOTENCY-002` | mesma chave com payload material diferente | não |
| `CC-ORDER-001` | evento fora de ordem | após dependência ou reconciliação |

## 7326.5 Ciclo e domínio

| Código | Significado | Retry |
|---|---|---|
| `CC-LIFECYCLE-001` | transição de sessão inválida | após estado válido |
| `CC-LIFECYCLE-002` | sessão pausada | após retomada |
| `CC-LIFECYCLE-003` | sessão expirada | após nova validação ou sessão |
| `CC-LIFECYCLE-004` | operação bloqueada por contestação | após resolução |
| `CC-LIFECYCLE-005` | operação bloqueada por revogação | não no escopo revogado |
| `CC-LIFECYCLE-006` | revisão não concluída | após revisão |

## 7326.6 Integração e técnica

| Código | Significado | Retry |
|---|---|---|
| `CC-INTEGRATION-001` | consumidor rejeitou recorte | após ajuste contratual |
| `CC-INTEGRATION-002` | confirmação de propagação pendente | automático controlado |
| `CC-INTEGRATION-003` | consumidor desconhecido | após registro |
| `CC-TECH-001` | falha recuperável | conforme política |
| `CC-TECH-002` | timeout | conforme política e autoridade vigente |
| `CC-TECH-003` | falha irrecuperável | intervenção |
| `CC-TECH-004` | reconstrução inconsistente | investigação |

# 7327. Idempotência por operação

| Operação | Chave material mínima | Resultado em retry idêntico | Conflito material |
|---|---|---|---|
| iniciar sessão | ator + participante/modo + finalidade + solicitação | sessão existente | finalidade ou participante diferente |
| receber entrada | `capture_input_id` + hash | entrada existente | mesmo ID e conteúdo diferente |
| registrar transcrição | entrada + versão + método | transcrição existente | mesma versão e texto diferente |
| registrar interpretação | fontes + método + versão | interpretação existente | mesma identidade e fontes diferentes |
| produzir síntese | fontes + versão | síntese existente | mesma versão e composição diferente |
| confirmar síntese | síntese + versão + escopo + ator | confirmação existente | escopo diferente |
| autorizar persistência | conteúdo + finalidade + consumidor + período | autorização existente | ampliação de escopo |
| emitir recorte | consumidor + finalidade + fontes + versões | recorte existente | campos diferentes |
| registrar correção | alvo + versão + correção | correção existente | valor corrigido diferente |
| revogar autorização | autorização + escopo + effective_at | revogação existente | escopo incompatível |
| confirmar propagação | operação + consumidor + versão | confirmação existente | resultado incompatível |
| reconstruir projeção | projeção + checkpoint + contrato | resultado anterior ou continuação | checkpoint incompatível |

# 7328. Ordenação, causalidade e concorrência

## 7328.1 Ordenação

- ordenação principal por `capture_record_id` e `aggregate_version`;
- entidades versionadas preservam `entity_version`;
- `occurred_at` não substitui ordem do agregado;
- fatos antigos recebidos tardiamente não sobrescrevem correções posteriores;
- evento sem predecessores necessários permanece pendente ou isolado;
- correção e revogação têm prioridade operacional sobre emissão de novos recortes.

## 7328.2 Causalidade

- `causation_id` exige relação funcional direta;
- entrada não causa automaticamente Objetivo, Evento de Vida ou evolução;
- resultado de Intelligence não causa confirmação;
- entrega não causa admissão;
- confirmação de consumidor pode causar avanço do estado de propagação.

## 7328.3 Concorrência

Conflitos deverão impedir:

- duas confirmações incompatíveis;
- correção perdida;
- revogação perdida;
- recorte emitido durante revogação;
- persistência concorrente com descarte;
- evento funcional criado a partir de versão antiga;
- fechamento com entrada material ainda não reconhecida.

# 7329. Versionamento e compatibilidade

## 7329.1 Regras semânticas

- `major`: alteração incompatível de significado, obrigatoriedade ou autoridade;
- `minor`: adição opcional compatível;
- `patch`: correção editorial ou restrição mais segura sem mudar payload válido;
- `schema_revision`: ajuste técnico compatível dentro da mesma versão contratual.

## 7329.2 Compatibilidade permitida

Pode ser compatível:

- novo campo opcional;
- novo código de aviso;
- nova natureza de metadado sem significado funcional;
- nova versão de exemplo;
- restrição de tamanho documentada para novos produtores.

## 7329.3 Alterações que exigem nova versão maior

- ampliar finalidade;
- tornar campo opcional obrigatório;
- alterar natureza da informação;
- mudar autoridade necessária;
- mudar semântica de confirmação;
- remover suporte a correção ou revogação;
- alterar regra de retenção;
- reutilizar tipo de evento para fato diferente;
- transformar referência protegida em conteúdo bruto obrigatório.

## 7329.4 Janela de suporte

Cada consumidor deverá declarar versões aceitas. A descontinuação exige:

- inventário de produtores e consumidores;
- aviso registrado;
- período de migração;
- testes de replay;
- preservação de correções e revogações;
- isolamento de mensagens incompatíveis;
- proibição de conversão silenciosa que amplie significado.

# 7330. Segurança e privacidade contratual

Todo contrato deverá declarar:

- classificação de sensibilidade;
- campos permitidos em logs;
- política de conteúdo inline;
- política de referência protegida;
- retenção;
- consumidores;
- correção;
- revogação;
- criptografia exigida como propriedade, sem escolher implementação;
- proteção contra enumeração;
- tratamento de terceiros;
- tratamento de menores;
- contexto de dispositivo compartilhado.

Payloads deverão preferir identificadores e referências. Conteúdo bruto somente poderá ser transportado quando indispensável, proporcional e autorizado.

# 7331. Observabilidade contratual

Métricas mínimas:

- comandos aceitos, rejeitados e conflitantes;
- distribuição de códigos de erro;
- versão contratual por produtor e consumidor;
- eventos incompatíveis isolados;
- duplicidades detectadas;
- eventos fora de ordem;
- latência até persistência;
- latência até publicação;
- entregas por estado;
- consumidores pendentes de correção;
- consumidores pendentes de revogação;
- retenções residuais;
- reconstruções concluídas e inconsistentes;
- violações de minimização;
- tentativas de uso após revogação.

Nenhuma métrica deve avaliar profundidade, vulnerabilidade, fé, valor ou evolução do participante.

# 7332. Testes obrigatórios de contrato

## 7332.1 Envelopes e validação

1. comando sem `command_id` é rejeitado;
2. comando sem finalidade é rejeitado;
3. comando sem autoridade é rejeitado;
4. payload incompatível não produz efeito;
5. evento funcional sem versão é rejeitado;
6. evento funcional sem persistência suficiente não é publicado;
7. conteúdo sensível inline proibido é rejeitado;
8. referência protegida preserva rastreabilidade;
9. campo opcional novo não quebra consumidor compatível;
10. mudança de significado exige nova versão maior.

## 7332.2 Comandos

11. iniciar sessão é idempotente;
12. finalidade diferente não reutiliza a mesma sessão por inferência;
13. entrada recebe identidade permanente;
14. mesma entrada e mesmo hash retornam resultado anterior;
15. mesma entrada e hash diferente geram conflito;
16. pausa impede nova entrada;
17. retomada revalida autoridade;
18. transcrição referencia a entrada correta;
19. interpretação preserva natureza derivada;
20. síntese preserva fontes e versão;
21. confirmação usa a versão apresentada;
22. confirmação parcial não amplia escopo;
23. autorização de persistência não é inferida;
24. recorte sem consumidor registrado é rejeitado;
25. contestação bloqueia efeito material aplicável;
26. revogação bloqueia novo recorte imediatamente.

## 7332.3 Eventos e entrega

27. evento funcional avança versão do agregado;
28. evento técnico não avança fato funcional;
29. retry preserva `event_id` quando representa a mesma publicação;
30. duplicidade não gera segundo efeito;
31. evento fora de ordem não sobrescreve estado posterior;
32. transporte reconhecido não marca recorte como admitido;
33. consumidor rejeitado registra ausência de efeito;
34. versão incompatível é isolada;
35. dead letter preserva correlação e causalidade;
36. replay não cria nova confirmação.

## 7332.4 Contexto Vivo e consumidores

37. Contexto Vivo decide admissibilidade própria;
38. admissão parcial preserva campos rejeitados;
39. rejeição não é tratada como falha humana;
40. consumidor não amplia natureza da informação;
41. consumidor sem correção é inadmissível;
42. consumidor sem revogação é inadmissível;
43. Intelligence não produz confirmação;
44. Experience registra versão apresentada;
45. auditoria opera com conteúdo minimizado;
46. observabilidade não recebe narrativa bruta por padrão.

## 7332.5 Correção

47. correção preserva valor anterior;
48. correção identifica derivados afetados;
49. correção recompõe recortes afetados;
50. entrega da correção não equivale a aplicação;
51. confirmação parcial mantém correção pendente;
52. consumidor rejeitado exige reconciliação;
53. correção idempotente não duplica evento;
54. correção posterior prevalece na projeção;
55. reconstrução preserva histórico de correção;
56. conteúdo corrigido não permanece em índice reconstruído.

## 7332.6 Revogação

57. revogação bloqueia novos usos antes da propagação;
58. revogação identifica consumidores conhecidos;
59. confirmação de transporte não conclui revogação;
60. consumidor confirma bloqueio de novos usos;
61. retenção residual exige fundamento;
62. retenção residual não permite novo uso;
63. consumidor pendente mantém estado parcial;
64. falha crítica gera escalonamento;
65. novo recorte no escopo revogado é rejeitado;
66. replay de revogação não duplica efeitos.

## 7332.7 Reconstrução e Onda 0

67. snapshot inválido é rejeitado;
68. eventos posteriores ao snapshot são reproduzidos em ordem;
69. projeção divergente é reconstruída a partir do registro;
70. conteúdo legitimamente descartado não é recriado;
71. evento incompatível é isolado;
72. bloqueio de revogação sobrevive à reconstrução;
73. dependência ausente da Onda 0 bloqueia somente o fluxo afetado;
74. catálogo de schema resolve versão correta;
75. registro de consumidor impede finalidade não declarada;
76. registro de idempotência recupera resultado anterior;
77. falha de auditoria crítica impede publicação material;
78. falha de observabilidade não expõe conteúdo;
79. correção e revogação funcionam sem busca global completa;
80. Onda 0 opera sem topologia física definitiva.

# 7333. Cenários mínimos de aceitação

O pacote contratual deverá demonstrar:

- captura temporária sem persistência permanente;
- entrada multimodal por referência protegida;
- transcrição com baixa confiança e correção;
- síntese apresentada e parcialmente confirmada;
- recorte avaliado e parcialmente admitido pelo Contexto Vivo;
- consumidor que rejeita recorte;
- correção após admissão;
- revogação com múltiplos consumidores e retenção residual;
- retry após timeout;
- evento fora de ordem;
- conflito de versão;
- reconstrução após indisponibilidade;
- descarte legítimo sem recriação;
- versão incompatível isolada;
- falha de Intelligence com encerramento seguro.

# 7334. Gaps resolvidos

## 7334.1 `UIC01-GAP-006` — Resolvido

**Questão:** definir propagação técnica de revogação.

**Decisão:**

- bloqueio de novos usos é imediato;
- consumidores e efeitos conhecidos são inventariados;
- mensagens possuem versão e escopo;
- consumidor confirma ação e retenção residual;
- transporte não conclui propagação;
- suficiência depende de consumidores obrigatórios, pendências e bases residuais;
- falhas críticas permanecem abertas e observáveis.

**Evidência:** seções 7323, 7326, 7327, 7328 e 7332.

**Estado:** `Resolved`.

## 7334.2 `UIC01-GAP-007` — Resolvido

**Questão:** definir estratégia de reconstrução.

**Decisão:**

- snapshot válido é opcional;
- eventos funcionais preservam ordem do agregado;
- entidades versionadas completam o estado quando necessário;
- replay não cria novos fatos humanos;
- correções e revogações são preservadas;
- projeções são reconstruíveis;
- conteúdo legitimamente descartado não é recriado;
- incompatibilidades são isoladas e auditadas.

**Evidência:** seções 7324, 7328, 7329 e 7332.

**Estado:** `Resolved`.

## 7334.3 `UIC01-GAP-009` — Resolvido

**Questão:** definir dependências mínimas da Onda 0.

**Decisão:**

- 16 dependências contratuais mínimas foram classificadas;
- cada dependência declara capacidade mínima;
- contratos são exigidos antes de implementação ampla;
- grafo global, busca ampla e todos os produtos não são pré-requisitos;
- correção, revogação, reconstrução, idempotência e schemas são obrigatórios desde a Onda 0.

**Evidência:** seções 7325, 7326, 7332 e 7333.

**Estado:** `Resolved`.

# 7335. Estado da UIC-01 após este incremento

| Dimensão | Estado efetivo |
|---|---|
| Fontes normativas | Mapeadas |
| Modelo de domínio | Proposto |
| Ciclo técnico | Definido |
| Catálogo de comandos | Proposto e versionado |
| Catálogo de eventos | Proposto e versionado |
| Schemas mínimos | Propostos |
| Contratos síncronos | Propostos |
| Contratos assíncronos | Propostos |
| Contratos com consumidores | Propostos |
| Contexto Vivo | Contrato proposto |
| Guivos Intelligence | Contrato proposto |
| Correção | Protocolo contratual proposto |
| Revogação | Protocolo contratual proposto |
| Reconstrução | Contrato proposto |
| Dependências da Onda 0 | Definidas |
| Erros | Catálogo proposto |
| Idempotência | Definida por operação |
| Compatibilidade | Política proposta |
| Testes de contrato | 80 definidos |
| `UIC01-GAP-001` | Resolvido |
| `UIC01-GAP-002` | Resolvido |
| `UIC01-GAP-004` | Resolvido |
| `UIC01-GAP-005` | Resolvido |
| `UIC01-GAP-006` | Resolvido |
| `UIC01-GAP-007` | Resolvido |
| `UIC01-GAP-009` | Resolvido |
| Estado técnico | `Contracts technically proposed` |
| Progresso de referência | `80%` |

# 7336. Critérios atendidos para 80%

O estado é alcançado porque:

1. comandos possuem envelope comum e catálogo versionado;
2. eventos funcionais e técnicos possuem envelopes distintos;
3. eventos materiais exigem persistência suficiente;
4. contratos síncronos e assíncronos foram delimitados;
5. consumidores declaram finalidade, versões, retenção, correção e revogação;
6. Contexto Vivo mantém decisão própria;
7. Intelligence permanece assistiva;
8. correção possui confirmação por consumidor;
9. revogação possui bloqueio imediato e suficiência verificável;
10. reconstrução não cria novos fatos nem recupera conteúdo descartado;
11. dependências mínimas da Onda 0 foram classificadas;
12. erros e idempotência são estáveis;
13. compatibilidade e evolução foram definidas;
14. 80 testes de contrato foram registrados;
15. três gaps prioritários foram resolvidos;
16. nenhum conflito funcional bloqueante foi identificado.

# 7337. Gaps ainda abertos

| Gap | Estado | Próxima decisão |
|---|---|---|
| `UIC01-GAP-003` | Open | matriz de armazenamento multimodal |
| `UIC01-GAP-008` | Open | política de busca e indexação sensível |
| `UIC01-GAP-010` | Open | matriz técnica verificável dos guardrails |

# 7338. Próximo incremento

O próximo ciclo deverá elevar a UIC-01 para:

> **`Technically ready for implementation — 100%`.**

Deverá concluir:

- matriz de armazenamento multimodal;
- política de busca e indexação sensível;
- matriz técnica dos guardrails;
- requisitos não funcionais e SLOs iniciais;
- threat model;
- matriz de acesso e proteção;
- estratégia final de testes e evidências;
- critérios de readiness da Onda 0;
- riscos residuais e ADRs requeridos;
- resolução de `UIC01-GAP-003`, `UIC01-GAP-008` e `UIC01-GAP-010`.

# 7339. Limites de aprovação

A aprovação deste documento:

- não autoriza produção;
- não escolhe tecnologia;
- não define microsserviços;
- não transforma contrato lógico em API obrigatória;
- não permite conteúdo sensível em payload por conveniência;
- não torna Intelligence autoridade;
- não incorpora recortes automaticamente ao Contexto Vivo;
- não encerra gaps além dos explicitamente resolvidos;
- não reduz direitos de correção, contestação, limitação ou revogação.
