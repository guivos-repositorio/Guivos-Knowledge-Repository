---
id: ROADMAP-OVERLAY-11.16.0
title: Roadmap Arquitetural — Estado Efetivo 11.16.0
status: active
version: 11.16.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - ROADMAP-OVERLAY-11.15.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-SCHEMAS-001
  - M5.15
---

# Roadmap Arquitetural — Estado Efetivo 11.16.0

> O Roadmap-base permanece preservado. Este overlay prevalece sobre estado corrente, marco vigente, backlog prioritário e ponto de retomada.

## Estado atual

| Frente | Estado |
|---|---|
| Arquitetura funcional do Journey | Publicada e concluída |
| Engineering Handoff | Draft 0.4.0 efetivo |
| UIC-01 — Captura de Contexto | Draft 0.4.0 |
| Estado técnico da UIC-01 | Contracts technically proposed |
| Progresso | 80% |
| Marco vigente | M5.15 — Capture Context Technical Contracts Proposed |
| Frente operacional | Product Engineering |

## Entrega concluída

- 30 comandos versionados;
- 32 eventos funcionais versionados;
- eventos técnicos separados;
- schemas de comandos, eventos, recortes, consumidores, correções, revogações e reconstrução;
- contratos síncronos e assíncronos;
- contrato com Contexto Vivo;
- contrato com Guivos Intelligence;
- contrato com Journey Experience;
- correção e revogação distribuídas;
- reconstrução e replay;
- 16 dependências mínimas da Onda 0;
- catálogo de erros;
- idempotência;
- compatibilidade;
- 80 testes de contrato;
- resolução dos gaps 006, 007 e 009.

## Progressão técnica

| Etapa | Estado | Progresso |
|---|---|---:|
| Fundação normativa | Normative sources mapped | 20% |
| Modelo de domínio | Domain model proposed | 40% |
| Ciclo técnico | Lifecycle technically defined | 60% |
| Contratos técnicos | Contracts technically proposed | 80% |
| Prontidão técnica | Technically ready for implementation | 100% |

## Backlog prioritário

### P0 — Readiness técnico da UIC-01

1. matriz de armazenamento multimodal;
2. política de busca e indexação sensível;
3. matriz técnica verificável dos guardrails;
4. requisitos não funcionais;
5. SLOs iniciais;
6. threat model;
7. matriz de acesso e proteção;
8. estratégia final de testes;
9. evidências de conformidade;
10. critérios de readiness da Onda 0;
11. riscos residuais;
12. ADRs requeridos.

### P1 — Gaps finais

- `UIC01-GAP-003 — armazenamento multimodal`;
- `UIC01-GAP-008 — busca sensível`;
- `UIC01-GAP-010 — matriz técnica dos guardrails`.

### P2 — Decisões tecnológicas

Somente após o readiness:

- comparação de tecnologias;
- ADRs de persistência;
- ADRs de eventos e mensageria;
- ADRs de mídia;
- ADRs de busca;
- ADRs de implantação;
- planejamento da Onda 0.

## Próximo marco candidato

> `M5.16 — Capture Context Technically Ready for Implementation`

Condição: UIC-01 em 100%, três gaps finais resolvidos, requisitos não funcionais, segurança, testes, evidências, riscos e ADRs requeridos suficientemente definidos.

## Ponto exato de retomada

> Elaborar o pacote final de readiness técnico da Captura de Contexto.

## Limites

O estado de 80% não autoriza código de produção, contratação de tecnologia, lançamento ou topologia definitiva.
