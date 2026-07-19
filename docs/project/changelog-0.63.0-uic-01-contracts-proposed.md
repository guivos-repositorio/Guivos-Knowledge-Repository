---
id: CHANGELOG-OVERLAY-0.63.0
status: active
version: 0.63.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - CHANGELOG-OVERLAY-0.62.0
related:
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-SCHEMAS-001
  - M5.15
---

# Changelog 0.63.0 — UIC-01 Technical Contracts Proposed

## Added

- `PAS-001-CC-UIC-CONTRACTS-001 0.1.0`;
- `PAS-001-CC-UIC-SCHEMAS-001 0.1.0`;
- UIC-01 effective state `0.4.0`;
- Engineering Handoff effective state `0.4.0`;
- Product Architecture `1.35.0`;
- Roadmap `11.16.0`;
- Knowledge Board `11.16.0`;
- Architectural Milestones `4.14.0`;
- Canonical Matrix addendum `1.35.0`;
- milestone `M5.15`.

## Technical contracts

- 30 versioned commands;
- 32 versioned functional events;
- separate technical event envelope;
- command response contract;
- synchronous and asynchronous contracts;
- consumer admission contract;
- Living Context evaluation contract;
- Intelligence output contract;
- Journey Experience surface contract;
- correction propagation protocol;
- revocation propagation protocol;
- reconstruction and replay contract;
- 16 Wave 0 minimum dependencies;
- stable error catalogue;
- per-operation idempotency;
- compatibility policy;
- 80 contract tests.

## Schema pack

- logical schema registry;
- actor, purpose and sensitivity schemas;
- command and response envelopes;
- functional and technical event envelopes;
- input, transcript, interpretation, synthesis and confirmation payloads;
- Capture Slice schema;
- consumer response schema;
- correction and revocation schemas;
- snapshot and reconstruction schemas;
- command and event manifests;
- validation profiles;
- fixtures and compatibility matrix.

## Resolved

- `UIC01-GAP-006 — technical revocation propagation`;
- `UIC01-GAP-007 — reconstruction strategy`;
- `UIC01-GAP-009 — Wave 0 minimum dependencies`.

## Remaining

- `UIC01-GAP-003 — multimodal storage`;
- `UIC01-GAP-008 — sensitive search and indexing`;
- `UIC01-GAP-010 — technical guardrail matrix`.

## Preserved

No changes were made to:

- PAS-001 1.0.0;
- Capability Map 1.0.1;
- Engineering Handoff base 0.1.0;
- UIC-01 base 0.1.0;
- Domain Model 0.1.0;
- Technical Lifecycle 0.1.0;
- nine final functional contracts;
- 54 normative extensions;
- GLPA-001 1.1.1;
- GIA-000 1.3.0.

## Limits

This release does not authorize production, technology selection, final service topology or automatic incorporation into Living Context.
