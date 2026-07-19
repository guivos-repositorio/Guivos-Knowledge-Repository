---
id: CANONICAL-CONSOLIDATION-MATRIX-ADDENDUM-UIC01-CONTRACTS
status: active
version: 1.35.0
owner: Guivos
last_updated: 2026-07-19
parent: CANONICAL-CONSOLIDATION-MATRIX
related:
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-SCHEMAS-001
  - PAS-001-CC-UIC-001-OVERLAY-0.4.0
---

# Matriz de Consolidação Canônica — Addendum UIC-01 Contratos Técnicos

## 1. Autoridades consolidadas

| Autoridade | Versão | Estado | Papel |
|---|---:|---|---|
| PAS-001 | 1.0.0 | Active | arquitetura funcional do Journey |
| Capability Map | 1.0.1 | Active | capacidades e fronteiras |
| CC Lifecycle funcional | 1.0.0 | Active | estados e regras funcionais |
| CC Events & Integrations | 1.0.0 | Active | fatos e integrações funcionais |
| CC Final Contract | 1.0.0 | Active | guardrails e conclusão funcional |
| UIC-01 base | 0.1.0 | Draft | fundação técnica |
| Domain Model | 0.1.0 | Draft | agregados, identidades e invariantes |
| Technical Lifecycle | 0.1.0 | Draft | máquinas e transições |
| Technical Contracts | 0.1.0 | Draft | comandos, eventos e integrações |
| Contract Schema Pack | 0.1.0 | Draft | schemas, manifestos e fixtures |
| UIC-01 effective state | 0.4.0 | Active overlay | maturidade de 80% |
| Engineering Handoff effective state | 0.4.0 | Active overlay | estado de Product Engineering |

## 2. Matriz de decisões

| Dimensão | Autoridade funcional | Autoridade técnica especializada | Estado |
|---|---|---|---|
| raiz do agregado | Events & Integrations | Domain Model | Confirmed |
| sessão | Lifecycle | Domain Model + Technical Lifecycle | Defined |
| entrada original | Lifecycle | Domain Model + Schemas | Defined |
| transcrição | Lifecycle | Technical Lifecycle + Contracts | Contracted |
| interpretação | GIA + Lifecycle | Contracts + Schemas | Contracted |
| síntese | Lifecycle | Contracts + Schemas | Contracted |
| confirmação | Final Contract | Contracts + Schemas | Contracted |
| autorização | Final Contract | Contracts + Schemas | Contracted |
| persistência temporária | Lifecycle | Technical Lifecycle | Defined |
| recorte | Events & Integrations | Contracts + Schemas | Contracted |
| Contexto Vivo | CV Contract | Technical Contracts | Contract proposed |
| correção | Events & Integrations | Technical Contracts | Contract proposed |
| revogação | Events & Integrations | Technical Contracts | Contract proposed |
| reconstrução | Events & Integrations | Technical Contracts | Contract proposed |
| Onda 0 | Handoff | Technical Contracts | Dependencies defined |
| compatibilidade | Events & Integrations | Technical Contracts + Schemas | Proposed |

## 3. Distinções protegidas

| Elemento A | Não equivale a | Proteção contratual |
|---|---|---|
| comando | evento | envelopes distintos |
| evento técnico | fato funcional | schemas distintos |
| entrega | admissão | resposta de consumidor |
| admissão | confirmação humana | autoridade do consumidor |
| entrada | transcrição | IDs e schemas distintos |
| transcrição | interpretação | naturezas distintas |
| interpretação | declaração | `information_nature` restrita |
| síntese | Contexto Vivo | contrato de avaliação |
| confirmação | autorização | comandos e entidades distintas |
| recorte | contexto definitivo | minimização e decisão própria |
| retenção residual | novo uso | escopo proibido por contrato |
| replay | novo fato humano | regra de reconstrução |

## 4. Gaps

| Gap | Estado anterior | Estado 1.35.0 | Evidência |
|---|---|---|---|
| UIC01-GAP-001 | Open | Resolved | Domain Model |
| UIC01-GAP-002 | Open | Resolved | Domain Model |
| UIC01-GAP-003 | Open | Open | ciclo final |
| UIC01-GAP-004 | Open | Resolved | Technical Lifecycle |
| UIC01-GAP-005 | Open | Resolved | Technical Lifecycle |
| UIC01-GAP-006 | Open | Resolved | Technical Contracts 7323 |
| UIC01-GAP-007 | Open | Resolved | Technical Contracts 7324 |
| UIC01-GAP-008 | Open | Open | ciclo final |
| UIC01-GAP-009 | Open | Resolved | Technical Contracts 7325 |
| UIC01-GAP-010 | Open | Open | ciclo final |

## 5. Compatibilidade canônica

Os contratos técnicos são subordinados às autoridades funcionais. Em caso de conflito:

1. o contrato técnico deve ser corrigido;
2. não se adapta silenciosamente o significado funcional;
3. não se amplia autoridade para preservar conveniência técnica;
4. não se promove evento técnico a evento funcional;
5. não se reutiliza versão incompatível;
6. não se declara readiness enquanto o conflito permanecer.

## 6. Estado de consolidação

| Item | Estado |
|---|---|
| Modelo de domínio | Consolidated for 40% |
| Ciclo técnico | Consolidated for 60% |
| Contratos técnicos | Consolidated for 80% |
| Readiness técnico | Pending |
| Produção | Not authorized |

## 7. Próxima consolidação

A próxima versão deverá incorporar:

- armazenamento multimodal;
- busca sensível;
- matriz de guardrails;
- requisitos não funcionais;
- segurança e acesso;
- testes e evidências finais;
- ADRs requeridos;
- decisão de readiness da Onda 0.
