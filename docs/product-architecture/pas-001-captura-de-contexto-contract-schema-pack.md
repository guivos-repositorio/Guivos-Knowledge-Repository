---
id: PAS-001-CC-UIC-SCHEMAS-001
title: Pacote de Schemas dos Contratos Técnicos da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
parent: PAS-001-CC-UIC-CONTRACTS-001
normative: true
related:
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-LIFECYCLE-001
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-EVENT-INTEGRATION-001
---

# PAS-001-CC-UIC-SCHEMAS-001 — Pacote de Schemas dos Contratos Técnicos da Captura de Contexto

> **Estado:** `Draft 0.1.0 — Contract schema pack proposed`.
>
> Este documento materializa o conjunto mínimo de schemas lógicos da UIC-01. A notação YAML é descritiva e não escolhe formato físico de serialização, biblioteca de validação ou protocolo de transporte.

# 7401. Objetivo

O pacote permite:

- validar comandos antes de efeitos materiais;
- validar eventos antes da publicação;
- preservar versões e compatibilidade;
- testar produtores e consumidores;
- impedir ampliação de autoridade por payload;
- padronizar correção, revogação e reconstrução;
- isolar contratos incompatíveis;
- gerar fixtures de teste independentes de tecnologia.

# 7402. Registro lógico de schemas

```yaml
schema_registry:
  registry_id: PAS-001-CC-SCHEMA-REGISTRY
  version: 0.1.0
  owner: Guivos
  contracts:
    - name: CaptureCommandEnvelope
      version: 1.0.0
      compatibility: backward
    - name: CaptureCommandResponse
      version: 1.0.0
      compatibility: backward
    - name: CaptureFunctionalEventEnvelope
      version: 1.0.0
      compatibility: backward
    - name: CaptureTechnicalEventEnvelope
      version: 1.0.0
      compatibility: backward
    - name: CaptureSlice
      version: 1.0.0
      compatibility: none
    - name: CaptureConsumerResponse
      version: 1.0.0
      compatibility: backward
    - name: CaptureCorrectionMessage
      version: 1.0.0
      compatibility: none
    - name: CaptureRevocationMessage
      version: 1.0.0
      compatibility: none
    - name: CaptureSnapshot
      version: 1.0.0
      compatibility: none
```

# 7403. Regras comuns de validação

1. campos `id` são strings opacas não vazias;
2. datas usam representação temporal inequívoca;
3. versão segue `major.minor.patch`;
4. arrays de escopo não admitem duplicidade material;
5. conteúdo sensível inline exige permissão explícita do schema;
6. campos desconhecidos são aceitos somente quando o perfil declarar extensibilidade;
7. campos desconhecidos nunca alteram autoridade ou finalidade;
8. campos obrigatórios ausentes rejeitam a mensagem;
9. enum desconhecido é incompatível, salvo extensão explicitamente prevista;
10. `null` não substitui ausência quando a distinção possuir significado;
11. hashes são auxiliares de integridade e não identidades;
12. IDs de transporte não substituem IDs funcionais;
13. valores monetários, geográficos ou biométricos exigem tipos especializados futuros;
14. conteúdo de terceiros deve possuir indicador explícito;
15. menores e dispositivos compartilhados exigem flags de proteção.

# 7404. Schema `ActorContext 1.0.0`

```yaml
name: ActorContext
version: 1.0.0
required:
  - actor_id
  - actor_role
  - identity_mode
  - authority_scope
properties:
  actor_id:
    type: opaque_id
  actor_role:
    enum:
      - participant
      - representative
      - journey_experience
      - journey_domain
      - intelligence
      - platform
      - external_source
      - professional
      - organization
      - auditor
      - policy
  participant_id:
    type: opaque_id
    nullable: true
  representation_id:
    type: opaque_id
    nullable: true
  identity_mode:
    enum: [authenticated, provisional, pseudonymous, temporary]
  authority_scope:
    type: array
    items: authority_code
    min_items: 1
  assurance_level:
    type: string
    nullable: true
constraints:
  - representative requires representation_id
  - participant role requires participant_id unless temporary mode
  - intelligence cannot include confirm or authorize authority codes
```

# 7405. Schema `PurposeContext 1.0.0`

```yaml
name: PurposeContext
version: 1.0.0
required:
  - purpose_id
  - purpose_code
  - allowed_operations
  - prohibited_operations
  - authorized_consumers
  - valid_from
properties:
  purpose_id: opaque_id
  purpose_code: string
  description_reference: protected_reference
  allowed_operations:
    type: array
    items: operation_code
  prohibited_operations:
    type: array
    items: operation_code
  authorized_consumers:
    type: array
    items: consumer_id
  valid_from: datetime
  valid_until:
    type: datetime
    nullable: true
  jurisdiction:
    type: string
    nullable: true
constraints:
  - prohibited operation prevails over allowed operation
  - valid_until must be after valid_from
  - generic purpose codes are rejected for material propagation
```

# 7406. Schema `SensitivityContext 1.0.0`

```yaml
name: SensitivityContext
version: 1.0.0
required:
  - classification
  - categories
  - third_party_data
  - minor_data
  - shared_device_restrictions
  - log_policy
  - index_policy
properties:
  classification:
    enum: [public, internal, personal, sensitive, highly_sensitive]
  categories:
    type: array
    items: sensitivity_category
  third_party_data: boolean
  minor_data: boolean
  shared_device_restrictions: boolean
  log_policy:
    enum: [none, identifiers_only, redacted]
  index_policy:
    enum: [prohibited, metadata_only, protected]
constraints:
  - highly_sensitive cannot use unrestricted inline payload
  - minor_data requires reinforced purpose and authority
  - shared device requires protected presentation context
```

# 7407. Schema `CaptureCommandEnvelope 1.0.0`

```yaml
name: CaptureCommandEnvelope
version: 1.0.0
additional_properties: false
required:
  - command_id
  - command_type
  - command_version
  - contract_instance_id
  - actor
  - purpose
  - sensitivity
  - requested_at
  - idempotency_key
  - correlation_id
  - channel
  - payload
properties:
  command_id: opaque_id
  command_type: command_type
  command_version: semantic_version
  contract_instance_id: opaque_id
  capture_record_id:
    type: opaque_id
    nullable: true
  capture_session_id:
    type: opaque_id
    nullable: true
  expected_aggregate_version:
    type: integer
    minimum: 0
    nullable: true
  actor:
    schema: ActorContext@1.0.0
  purpose:
    schema: PurposeContext@1.0.0
  sensitivity:
    schema: SensitivityContext@1.0.0
  requested_at: datetime
  idempotency_key: string
  correlation_id: opaque_id
  causation_id:
    type: opaque_id
    nullable: true
  channel: string
  payload: object
  client_context:
    type: object
    nullable: true
constraints:
  - updates require capture_record_id and expected_aggregate_version
  - payload schema selected by command_type and command_version
  - same idempotency key cannot map to materially different normalized payload
```

# 7408. Schema `CaptureCommandResponse 1.0.0`

```yaml
name: CaptureCommandResponse
version: 1.0.0
required:
  - request_command_id
  - response_id
  - status
  - accepted_scope
  - rejected_scope
  - warnings
  - recorded_at
  - correlation_id
properties:
  request_command_id: opaque_id
  response_id: opaque_id
  status:
    enum: [accepted, rejected, conflict, pending, partially_accepted]
  capture_record_id:
    type: opaque_id
    nullable: true
  capture_session_id:
    type: opaque_id
    nullable: true
  aggregate_version:
    type: integer
    nullable: true
  result_reference:
    type: protected_reference
    nullable: true
  accepted_scope:
    type: array
  rejected_scope:
    type: array
  error:
    schema: CaptureError@1.0.0
    nullable: true
  warnings:
    type: array
    items: warning_code
  recorded_at: datetime
  correlation_id: opaque_id
constraints:
  - rejected and conflict require error
  - accepted cannot declare rejected_scope unless partially_accepted
  - pending cannot imply event publication
```

# 7409. Schema `CaptureError 1.0.0`

```yaml
name: CaptureError
version: 1.0.0
required:
  - code
  - category
  - retryable
properties:
  code: stable_error_code
  category:
    enum:
      - domain
      - authorization
      - validation
      - conflict
      - lifecycle
      - integration
      - technical
      - security
      - privacy
      - compatibility
  message_reference:
    type: string
    nullable: true
  retryable: boolean
  retry_after:
    type: duration
    nullable: true
  current_state_reference:
    type: protected_reference
    nullable: true
  details:
    type: object
    nullable: true
constraints:
  - details cannot contain raw sensitive content
  - retry_after allowed only when retryable
```

# 7410. Payload `StartCaptureSession 1.0.0`

```yaml
name: StartCaptureSessionPayload
version: 1.0.0
required:
  - identity_mode
  - purpose_id
  - requested_channel
  - temporary_mode_requested
properties:
  participant_reference:
    type: opaque_id
    nullable: true
  identity_mode:
    enum: [authenticated, provisional, pseudonymous, temporary]
  purpose_id: opaque_id
  requested_channel: string
  representation_id:
    type: opaque_id
    nullable: true
  temporary_mode_requested: boolean
constraints:
  - authenticated mode requires participant_reference
  - representative actor requires representation_id
```

# 7411. Payload `SubmitCaptureInput 1.0.0`

```yaml
name: SubmitCaptureInputPayload
version: 1.0.0
required:
  - capture_input_id
  - input_type
  - content_hash
  - provenance
  - retention_request
properties:
  capture_input_id: opaque_id
  input_type:
    enum:
      - text
      - voice
      - audio
      - image
      - video
      - document
      - selection
      - structured_response
      - imported_data
  content_reference:
    type: protected_reference
    nullable: true
  inline_content:
    type: string
    nullable: true
  content_hash: integrity_hash
  content_length:
    type: integer
    nullable: true
  source_occurred_at:
    type: datetime
    nullable: true
  language:
    type: string
    nullable: true
  provenance:
    schema: ProvenanceContext@1.0.0
  retention_request:
    enum: [temporary, purpose_bound, authorized_persistent]
constraints:
  - exactly one of content_reference or inline_content is required
  - sensitive and highly_sensitive inputs prefer content_reference
  - authorized_persistent requires separate authorization reference in command context
```

# 7412. Payload `RecordCaptureTranscript 1.0.0`

```yaml
name: RecordCaptureTranscriptPayload
version: 1.0.0
required:
  - transcript_id
  - capture_input_id
  - transcript_version
  - text_reference
  - language
  - method_reference
  - uncertainty_codes
  - source_segments
properties:
  transcript_id: opaque_id
  capture_input_id: opaque_id
  transcript_version:
    type: integer
    minimum: 1
  text_reference: protected_reference
  language: string
  method_reference: string
  model_reference:
    type: string
    nullable: true
  confidence:
    type: number
    minimum: 0
    maximum: 1
    nullable: true
  uncertainty_codes:
    type: array
    items: uncertainty_code
  source_segments:
    type: array
    items:
      input_offset_start: integer
      input_offset_end: integer
      transcript_offset_start: integer
      transcript_offset_end: integer
      confidence: number | null
constraints:
  - source segments cannot reference another input
  - model_reference required for automated transcription
```

# 7413. Payload `RecordCaptureInterpretation 1.0.0`

```yaml
name: RecordCaptureInterpretationPayload
version: 1.0.0
required:
  - interpretation_id
  - interpretation_version
  - source_references
  - information_nature
  - statement_reference
  - method_reference
  - uncertainty_codes
  - alternative_interpretations
  - limitations
properties:
  interpretation_id: opaque_id
  interpretation_version:
    type: integer
    minimum: 1
  source_references:
    type: array
    min_items: 1
  information_nature:
    enum: [interpretation, hypothesis, inference, estimate, observation]
  statement_reference: protected_reference
  method_reference: string
  model_reference:
    type: string
    nullable: true
  confidence:
    type: number
    minimum: 0
    maximum: 1
    nullable: true
  uncertainty_codes:
    type: array
  alternative_interpretations:
    type: array
  limitations:
    type: array
constraints:
  - participant_statement is not an accepted information_nature
  - automated method requires model_reference
```

# 7414. Payload `RecordCaptureSynthesis 1.0.0`

```yaml
name: RecordCaptureSynthesisPayload
version: 1.0.0
required:
  - synthesis_id
  - synthesis_version
  - source_references
  - sections
  - uncertainty_codes
  - excluded_topics
  - review_required
properties:
  synthesis_id: opaque_id
  synthesis_version:
    type: integer
    minimum: 1
  source_references:
    type: array
    min_items: 1
  sections:
    type: array
    items:
      section_id: opaque_id
      title_reference: string
      content_reference: protected_reference
      information_natures: string[]
      source_references: string[]
      sensitive: boolean
  uncertainty_codes:
    type: array
  excluded_topics:
    type: array
  valid_until:
    type: datetime
    nullable: true
  review_required: boolean
constraints:
  - material synthesis requires review_required true
  - every section requires source references
```

# 7415. Payload `ConfirmCaptureSynthesis 1.0.0`

```yaml
name: ConfirmCaptureSynthesisPayload
version: 1.0.0
required:
  - confirmation_id
  - synthesis_id
  - synthesis_version
  - confirmed_scope
  - excluded_scope
  - purpose_id
  - consumer_scope
  - participant_statement_reference
properties:
  confirmation_id: opaque_id
  synthesis_id: opaque_id
  synthesis_version:
    type: integer
    minimum: 1
  confirmed_scope:
    type: array
    min_items: 1
  excluded_scope:
    type: array
  purpose_id: opaque_id
  consumer_scope:
    type: array
  valid_until:
    type: datetime
    nullable: true
  participant_statement_reference: protected_reference
constraints:
  - confirmed_scope and excluded_scope cannot overlap
  - consumer_scope must be subset of purpose authorized consumers
```

# 7416. Payload `AuthorizeCapturePersistence 1.0.0`

```yaml
name: AuthorizeCapturePersistencePayload
version: 1.0.0
required:
  - authorization_id
  - content_scope
  - purpose_id
  - authorized_consumers
  - allowed_operations
  - prohibited_operations
  - valid_from
  - retention_policy_id
  - revocation_policy_id
properties:
  authorization_id: opaque_id
  content_scope:
    type: array
    min_items: 1
  purpose_id: opaque_id
  authorized_consumers:
    type: array
  allowed_operations:
    type: array
  prohibited_operations:
    type: array
  valid_from: datetime
  valid_until:
    type: datetime
    nullable: true
  retention_policy_id: opaque_id
  revocation_policy_id: opaque_id
constraints:
  - prohibited operations prevail
  - valid_until must be after valid_from
```

# 7417. Schema `CaptureSlice 1.0.0`

```yaml
name: CaptureSlice
version: 1.0.0
additional_properties: false
required:
  - capture_slice_id
  - slice_version
  - capture_record_id
  - consumer_id
  - consumer_contract_version
  - purpose_id
  - source_references
  - confirmation_references
  - authorization_references
  - fields
  - correction_channel
  - revocation_channel
  - issued_at
properties:
  capture_slice_id: opaque_id
  slice_version:
    type: integer
    minimum: 1
  capture_record_id: opaque_id
  participant_id:
    type: opaque_id
    nullable: true
  consumer_id: opaque_id
  consumer_contract_version: semantic_version
  purpose_id: opaque_id
  source_references:
    type: array
  confirmation_references:
    type: array
  authorization_references:
    type: array
  fields:
    type: array
    items:
      field_id: opaque_id
      semantic_code: string
      value_reference: protected_reference
      information_nature: string
      provenance_reference: opaque_id
      confidence: number | null
      uncertainty_codes: string[]
      sensitivity: string
      valid_until: datetime | null
  valid_until:
    type: datetime
    nullable: true
  correction_channel: string
  revocation_channel: string
  issued_at: datetime
constraints:
  - fields must be purpose-minimized
  - every field must have provenance
  - derived fields require uncertainty representation
  - slice cannot contain fields outside confirmations and authorizations
```

# 7418. Schema `CaptureConsumerResponse 1.0.0`

```yaml
name: CaptureConsumerResponse
version: 1.0.0
required:
  - capture_slice_id
  - consumer_id
  - status
  - admitted_fields
  - rejected_fields
  - reason_codes
  - correction_subscription_confirmed
  - revocation_subscription_confirmed
  - processed_at
properties:
  capture_slice_id: opaque_id
  consumer_id: opaque_id
  status:
    enum: [admitted, partially_admitted, rejected, needs_review, deferred]
  admitted_fields:
    type: array
  rejected_fields:
    type: array
  reason_codes:
    type: array
  effect_references:
    type: array
  consumer_aggregate_version:
    type: integer
    nullable: true
  correction_subscription_confirmed: boolean
  revocation_subscription_confirmed: boolean
  processed_at: datetime
constraints:
  - rejected status requires no admitted fields
  - admitted status requires no rejected fields
  - material admission requires both subscriptions confirmed
```

# 7419. Schema `CaptureCorrectionMessage 1.0.0`

```yaml
name: CaptureCorrectionMessage
version: 1.0.0
required:
  - correction_id
  - correction_version
  - target_reference
  - previous_value_reference
  - corrected_value_reference
  - effective_at
  - affected_slice_ids
  - affected_consumer_effects
  - required_action
  - response_due_at
  - correlation_id
properties:
  correction_id: opaque_id
  correction_version:
    type: integer
    minimum: 1
  target_reference: protected_reference
  previous_value_reference: protected_reference
  corrected_value_reference: protected_reference
  effective_at: datetime
  affected_slice_ids:
    type: array
  affected_consumer_effects:
    type: array
  required_action:
    enum: [replace, invalidate, limit, review, delete_optional_copy]
  response_due_at: datetime
  correlation_id: opaque_id
constraints:
  - corrected and previous references cannot be identical
  - response_due_at must be after effective_at
```

# 7420. Schema `CaptureCorrectionResponse 1.0.0`

```yaml
name: CaptureCorrectionResponse
version: 1.0.0
required:
  - correction_id
  - consumer_id
  - status
  - applied_effect_references
  - pending_effect_references
  - residual_references
  - reason_codes
  - confirmed_at
  - consumer_contract_version
properties:
  correction_id: opaque_id
  consumer_id: opaque_id
  status:
    enum: [applied, partially_applied, rejected, not_applicable, pending]
  applied_effect_references:
    type: array
  pending_effect_references:
    type: array
  residual_references:
    type: array
  reason_codes:
    type: array
  confirmed_at: datetime
  consumer_contract_version: semantic_version
```

# 7421. Schema `CaptureRevocationMessage 1.0.0`

```yaml
name: CaptureRevocationMessage
version: 1.0.0
required:
  - revocation_id
  - revocation_version
  - authorization_id
  - revoked_scope
  - effective_at
  - capture_slice_ids
  - consumer_effect_references
  - required_action
  - response_due_at
  - correlation_id
properties:
  revocation_id: opaque_id
  revocation_version:
    type: integer
    minimum: 1
  authorization_id: opaque_id
  revoked_scope:
    type: array
    min_items: 1
  effective_at: datetime
  capture_slice_ids:
    type: array
  consumer_effect_references:
    type: array
  required_action:
    enum:
      - stop_new_use
      - invalidate
      - delete_optional_copy
      - expire
      - restrict
      - preserve_legitimate_residual
  response_due_at: datetime
  correlation_id: opaque_id
constraints:
  - stop_new_use applies from effective_at regardless of delivery completion
```

# 7422. Schema `CaptureRevocationResponse 1.0.0`

```yaml
name: CaptureRevocationResponse
version: 1.0.0
required:
  - revocation_id
  - consumer_id
  - status
  - new_uses_blocked_at
  - invalidated_effect_references
  - deleted_copy_references
  - residual_references
  - reason_codes
  - confirmed_at
  - consumer_contract_version
properties:
  revocation_id: opaque_id
  consumer_id: opaque_id
  status:
    enum: [applied, partially_applied, rejected, not_applicable, pending, retained_legitimately]
  new_uses_blocked_at: datetime
  invalidated_effect_references:
    type: array
  deleted_copy_references:
    type: array
  residual_references:
    type: array
  residual_basis_reference:
    type: protected_reference
    nullable: true
  residual_valid_until:
    type: datetime
    nullable: true
  reason_codes:
    type: array
  confirmed_at: datetime
  consumer_contract_version: semantic_version
constraints:
  - retained_legitimately requires residual_basis_reference
  - residual_valid_until required when the legal basis is temporally limited
```

# 7423. Schema `CaptureFunctionalEventEnvelope 1.0.0`

```yaml
name: CaptureFunctionalEventEnvelope
version: 1.0.0
additional_properties: false
required:
  - event_id
  - event_type
  - event_version
  - schema_revision
  - capture_record_id
  - aggregate_version
  - expected_aggregate_version
  - entity_type
  - actor
  - purpose
  - sensitivity
  - temporal
  - provenance
  - information_nature
  - authorization_references
  - authorized_consumers
  - correlation_id
  - idempotency_key
  - payload
  - integrity
properties:
  event_id: opaque_id
  event_type: event_type
  event_version: semantic_version
  schema_revision:
    type: integer
    minimum: 1
  capture_record_id: opaque_id
  aggregate_version:
    type: integer
    minimum: 1
  expected_aggregate_version:
    type: integer
    minimum: 0
  capture_session_id:
    type: opaque_id
    nullable: true
  entity_type: string
  entity_id:
    type: opaque_id
    nullable: true
  entity_version:
    type: integer
    nullable: true
  participant_id:
    type: opaque_id
    nullable: true
  actor:
    schema: ActorContext@1.0.0
  purpose:
    schema: PurposeContext@1.0.0
  sensitivity:
    schema: SensitivityContext@1.0.0
  temporal:
    schema: TemporalContext@1.0.0
  provenance:
    schema: ProvenanceContext@1.0.0
  information_nature: string
  confirmation_scope:
    type: array
  authorization_references:
    type: array
  authorized_consumers:
    type: array
  retention_policy_id:
    type: opaque_id
    nullable: true
  correlation_id: opaque_id
  causation_id:
    type: opaque_id
    nullable: true
  idempotency_key: string
  payload: object
  integrity:
    type: object
    required: [payload_hash]
constraints:
  - aggregate_version equals expected_aggregate_version plus one for material changes
  - event payload schema selected by event_type and version
  - functional event requires recorded_at
```

# 7424. Schema `CaptureTechnicalEventEnvelope 1.0.0`

```yaml
name: CaptureTechnicalEventEnvelope
version: 1.0.0
required:
  - technical_event_id
  - technical_event_type
  - technical_event_version
  - operation
  - state
  - occurred_at
  - recorded_at
  - correlation_id
  - idempotency_key
  - technical_metadata
properties:
  technical_event_id: opaque_id
  technical_event_type: technical_event_type
  technical_event_version: semantic_version
  processing_attempt_id:
    type: opaque_id
    nullable: true
  delivery_id:
    type: opaque_id
    nullable: true
  capture_record_id:
    type: opaque_id
    nullable: true
  capture_session_id:
    type: opaque_id
    nullable: true
  related_functional_event_id:
    type: opaque_id
    nullable: true
  operation: string
  state:
    enum: [scheduled, running, succeeded, failed_recoverable, failed_unrecoverable, timed_out, compensating, compensated]
  occurred_at: datetime
  recorded_at: datetime
  correlation_id: opaque_id
  causation_id:
    type: opaque_id
    nullable: true
  idempotency_key: string
  technical_metadata: object
constraints:
  - technical event cannot carry confirmation or authorization payloads
  - technical success cannot declare functional effect
```

# 7425. Schema `CaptureSnapshot 1.0.0`

```yaml
name: CaptureSnapshot
version: 1.0.0
required:
  - snapshot_id
  - capture_record_id
  - aggregate_version
  - created_at
  - contract_versions
  - state_vector
  - last_event_id
  - integrity_hash
  - excluded_content_references
properties:
  snapshot_id: opaque_id
  capture_record_id: opaque_id
  aggregate_version:
    type: integer
    minimum: 0
  created_at: datetime
  contract_versions: object
  state_vector:
    required:
      - sessions
      - inputs
      - transcripts
      - interpretations
      - syntheses
      - confirmations
      - authorizations
      - persistence
      - propagation
      - contests
      - revocations
  last_event_id: opaque_id
  integrity_hash: integrity_hash
  excluded_content_references:
    type: array
constraints:
  - snapshot cannot contain content already legitimately discarded
  - aggregate version must match last event or documented compacted state
```

# 7426. Schema `ReconstructCaptureRecord 1.0.0`

```yaml
name: ReconstructCaptureRecordRequest
version: 1.0.0
required:
  - capture_record_id
  - target_aggregate_version
  - projection_targets
  - verification_level
properties:
  capture_record_id: opaque_id
  target_aggregate_version: integer | latest
  projection_targets:
    type: array
  verification_level:
    enum: [standard, strict, forensic]
```

```yaml
name: ReconstructCaptureRecordResponse
version: 1.0.0
required:
  - reconstruction_id
  - status
  - aggregate_version
  - replayed_event_count
  - ignored_duplicate_count
  - out_of_order_count
  - incompatible_event_references
  - missing_reference_codes
  - reconciled_projections
  - integrity_status
properties:
  reconstruction_id: opaque_id
  status:
    enum: [completed, completed_with_warnings, failed]
  aggregate_version: integer
  replayed_event_count: integer
  ignored_duplicate_count: integer
  out_of_order_count: integer
  incompatible_event_references: string[]
  missing_reference_codes: string[]
  reconciled_projections: string[]
  integrity_status:
    enum: [valid, warning, invalid]
```

# 7427. Manifesto de comandos

```yaml
command_manifest:
  version: 1.0.0
  commands:
    StartCaptureSession: StartCaptureSessionPayload@1.0.0
    ExplainCapturePurpose: ExplainCapturePurposePayload@1.0.0
    SelectCaptureChannel: SelectCaptureChannelPayload@1.0.0
    SubmitCaptureInput: SubmitCaptureInputPayload@1.0.0
    AttachCaptureMedia: AttachCaptureMediaPayload@1.0.0
    PauseCaptureSession: SessionTransitionPayload@1.0.0
    ResumeCaptureSession: SessionTransitionPayload@1.0.0
    RequestCaptureProcessing: RequestCaptureProcessingPayload@1.0.0
    RecordCaptureTranscript: RecordCaptureTranscriptPayload@1.0.0
    CorrectCaptureTranscript: CorrectCaptureTranscriptPayload@1.0.0
    RecordCaptureInterpretation: RecordCaptureInterpretationPayload@1.0.0
    RecordCaptureSynthesis: RecordCaptureSynthesisPayload@1.0.0
    PresentCaptureSynthesis: PresentCaptureSynthesisPayload@1.0.0
    ConfirmCaptureSynthesis: ConfirmCaptureSynthesisPayload@1.0.0
    PartiallyConfirmCaptureSynthesis: ConfirmCaptureSynthesisPayload@1.0.0
    RequestCaptureCorrection: RequestCaptureCorrectionPayload@1.0.0
    RegisterCaptureCorrection: RegisterCaptureCorrectionPayload@1.0.0
    AuthorizeCapturePersistence: AuthorizeCapturePersistencePayload@1.0.0
    PersistCaptureTemporarily: PersistCaptureTemporarilyPayload@1.0.0
    IssueCaptureSlice: CaptureSlice@1.0.0
    AcknowledgeCaptureSlice: CaptureConsumerResponse@1.0.0
    RejectCaptureSlice: CaptureConsumerResponse@1.0.0
    ContestCaptureRecord: ContestCaptureRecordPayload@1.0.0
    RevokeCaptureAuthorization: RevokeCaptureAuthorizationPayload@1.0.0
    ConfirmCorrectionPropagation: CaptureCorrectionResponse@1.0.0
    ConfirmRevocationPropagation: CaptureRevocationResponse@1.0.0
    CloseCaptureSession: SessionTransitionPayload@1.0.0
    ExpireCaptureSession: SessionTransitionPayload@1.0.0
    AbandonCaptureSession: SessionTransitionPayload@1.0.0
    RebuildCaptureProjection: ReconstructCaptureRecordRequest@1.0.0
```

# 7428. Manifesto de eventos

```yaml
event_manifest:
  version: 1.0.0
  event_envelope: CaptureFunctionalEventEnvelope@1.0.0
  events:
    CaptureSessionStarted: 1.0.0
    CapturePurposeExplained: 1.0.0
    CaptureChannelSelected: 1.0.0
    CaptureInputReceived: 1.0.0
    CaptureMediaAttached: 1.0.0
    CaptureSessionPaused: 1.0.0
    CaptureSessionResumed: 1.0.0
    CaptureProcessingRequested: 1.0.0
    CaptureTranscriptProduced: 1.0.0
    CaptureTranscriptCorrected: 1.0.0
    CaptureInterpretationProduced: 1.0.0
    CaptureSynthesisProduced: 1.0.0
    CaptureSynthesisPresented: 1.0.0
    CaptureSynthesisPartiallyConfirmed: 1.0.0
    CaptureSynthesisConfirmed: 1.0.0
    CaptureCorrectionRequested: 1.0.0
    CaptureCorrectionRegistered: 1.0.0
    CapturePersistenceAuthorized: 1.0.0
    TemporaryCapturePersistenceRegistered: 1.0.0
    CaptureSliceIssued: 1.0.0
    CaptureSliceAcknowledged: 1.0.0
    CaptureSliceRejected: 1.0.0
    CaptureRecordContested: 1.0.0
    CaptureAuthorizationRevoked: 1.0.0
    CaptureCorrectionPropagationConfirmed: 1.0.0
    CaptureRevocationPropagationConfirmed: 1.0.0
    CaptureCorrectionPropagated: 1.0.0
    CaptureRevocationPropagated: 1.0.0
    CaptureSessionClosed: 1.0.0
    CaptureSessionExpired: 1.0.0
    CaptureSessionAbandoned: 1.0.0
    CaptureFailureRegistered: 1.0.0
```

# 7429. Exemplo válido — entrada temporária

```yaml
command_id: cmd_opaque_001
command_type: SubmitCaptureInput
command_version: 1.0.0
contract_instance_id: contract_instance_001
capture_record_id: capture_record_001
capture_session_id: capture_session_001
expected_aggregate_version: 4
actor:
  actor_id: participant_001
  actor_role: participant
  participant_id: participant_001
  representation_id: null
  identity_mode: authenticated
  authority_scope: [submit_own_input]
  assurance_level: proportional
purpose:
  purpose_id: purpose_001
  purpose_code: initial_context_capture
  description_reference: purpose_text_v1
  allowed_operations: [capture, temporary_store, synthesize]
  prohibited_operations: [advertising, permanent_share]
  authorized_consumers: []
  valid_from: 2026-07-19T00:00:00-03:00
  valid_until: null
  jurisdiction: BR
sensitivity:
  classification: personal
  categories: [general_context]
  third_party_data: false
  minor_data: false
  shared_device_restrictions: false
  log_policy: identifiers_only
  index_policy: metadata_only
requested_at: 2026-07-19T10:00:00-03:00
idempotency_key: input_001_submission_v1
correlation_id: correlation_001
causation_id: null
channel: web
payload:
  capture_input_id: capture_input_001
  input_type: text
  content_reference: protected_content_001
  inline_content: null
  content_hash: hash_001
  content_length: 380
  source_occurred_at: null
  language: pt-BR
  provenance:
    source_type: participant
    source_id: participant_001
    source_version: null
    transformation_chain: []
    model_reference: null
    method_reference: direct_text
    confidence: null
    uncertainty_codes: []
  retention_request: temporary
```

# 7430. Exemplo inválido — confirmação por Intelligence

```yaml
actor:
  actor_id: intelligence_001
  actor_role: intelligence
  authority_scope: [confirm_synthesis]
payload:
  synthesis_id: synthesis_001
  synthesis_version: 2
  confirmed_scope: [all]
```

Resultado obrigatório:

```yaml
status: rejected
error:
  code: CC-AUTH-002
  category: authorization
  retryable: false
```

# 7431. Exemplo inválido — mesma idempotência com conteúdo diferente

Primeira tentativa:

```yaml
idempotency_key: input_001_submission_v1
payload:
  capture_input_id: capture_input_001
  content_hash: hash_A
```

Segunda tentativa:

```yaml
idempotency_key: input_001_submission_v1
payload:
  capture_input_id: capture_input_001
  content_hash: hash_B
```

Resultado obrigatório:

```yaml
status: conflict
error:
  code: CC-IDEMPOTENCY-002
  category: conflict
  retryable: false
```

# 7432. Exemplo — revogação com retenção residual

```yaml
revocation_id: revocation_001
consumer_id: living_context
status: retained_legitimately
new_uses_blocked_at: 2026-07-19T11:00:00-03:00
invalidated_effect_references: [effect_001]
deleted_copy_references: []
residual_references: [audit_minimum_001]
residual_basis_reference: legal_basis_001
residual_valid_until: 2031-07-19T11:00:00-03:00
reason_codes: [mandatory_audit_retention]
confirmed_at: 2026-07-19T11:05:00-03:00
consumer_contract_version: 1.0.0
```

Esse exemplo não autoriza novo uso do registro residual.

# 7433. Perfis de validação

## 7433.1 `surface-ingress`

Valida:

- ator;
- finalidade;
- canal;
- formato;
- tamanho;
- sensibilidade;
- idempotência sintática.

Não decide:

- autoridade material final;
- transição do agregado;
- publicação de evento.

## 7433.2 `domain-command`

Valida:

- autoridade;
- versão do agregado;
- estado e invariantes;
- idempotência material;
- escopo;
- finalidade;
- retenção;
- correção e revogação vigentes.

## 7433.3 `event-publication`

Valida:

- fato persistido;
- nova versão do agregado;
- payload minimizado;
- schema compatível;
- consumidores autorizados;
- correção e revogação possíveis.

## 7433.4 `consumer-admission`

Valida:

- versão do consumidor;
- finalidade;
- natureza da informação;
- sensibilidade;
- confirmação;
- autorização;
- retenção;
- canais de correção e revogação.

## 7433.5 `replay`

Valida:

- integridade;
- ordem do agregado;
- duplicidade;
- compatibilidade histórica;
- conteúdo descartado;
- correções;
- revogações;
- projeções reconstruíveis.

# 7434. Matriz de compatibilidade inicial

| Produtor | Contrato produzido | Consumidores mínimos | Versão |
|---|---|---|---:|
| Journey Experience | comandos de sessão e revisão | Journey Domain | 1.0.0 |
| Journey Domain | eventos funcionais e recortes | Contexto Vivo, auditoria, integrações autorizadas | 1.0.0 |
| Guivos Intelligence | resultados derivados | Journey Domain | 1.0.0 |
| Platform Layer | eventos técnicos | operação e observabilidade | 1.0.0 |
| Contexto Vivo | resposta de admissão | Journey Domain | 1.0.0 |
| consumidores autorizados | respostas de correção e revogação | coordenadores da UIC-01 | 1.0.0 |

# 7435. Fixtures obrigatórias

O pacote de testes deverá conter fixtures para:

1. sessão autenticada válida;
2. sessão temporária válida;
3. representação legítima;
4. finalidade ausente;
5. canal inadequado;
6. entrada por referência protegida;
7. entrada inline permitida;
8. duplicidade idempotente;
9. conflito de idempotência;
10. transcrição de baixa confiança;
11. interpretação automatizada identificada;
12. síntese com fontes completas;
13. síntese sem fontes;
14. confirmação integral válida;
15. confirmação parcial;
16. confirmação por versão antiga;
17. autorização limitada;
18. persistência temporária;
19. recorte minimizado;
20. recorte excessivo;
21. consumidor incompatível;
22. Contexto Vivo admite parcialmente;
23. consumidor rejeita;
24. correção propagada;
25. correção parcialmente aplicada;
26. revogação aplicada;
27. revogação com retenção residual;
28. revogação pendente;
29. snapshot válido;
30. snapshot inválido;
31. evento fora de ordem;
32. replay com evento incompatível.

# 7436. Critérios para promover schemas

Um schema poderá sair de `draft` quando:

- possui owner;
- possui versão;
- possui compatibilidade declarada;
- possui produtor identificado;
- possui consumidor identificado;
- possui exemplos válidos e inválidos;
- possui testes positivos e negativos;
- não amplia autoridade;
- não permite confirmação presumida;
- suporta correção e revogação;
- preserva minimização;
- passou por revisão de segurança e privacidade;
- passou por replay de compatibilidade.

# 7437. Limites

Este pacote:

- não determina JSON, Avro, Protobuf ou outro formato;
- não determina HTTP, gRPC, eventos ou filas como transporte final;
- não cria endpoints;
- não escolhe schema registry físico;
- não autoriza produção;
- não substitui o contrato funcional;
- não torna exemplos dados reais;
- não permite geração automática de autoridade a partir do schema.
