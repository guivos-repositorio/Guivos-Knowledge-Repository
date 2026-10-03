---
id: ROADMAP-OVERLAY-11.18.0
title: Roadmap Arquitetural — Estado Efetivo 11.18.0
status: active
version: 11.18.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - ROADMAP-OVERLAY-11.17.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-W0-PLAN-001
  - M5.17
---

# Roadmap Arquitetural — Estado Efetivo 11.18.0

> O Roadmap-base permanece preservado. Este overlay prevalece sobre estado corrente, marco, backlog prioritário e ponto de retomada.

## 1. Estado atual

| Frente | Estado |
|---|---|
| Arquitetura funcional do Journey | publicada e concluída |
| Engineering Handoff | Draft 0.6.0 efetivo |
| UIC-01 | Draft 0.6.0 |
| Estado técnico | Wave 0 implementation planned |
| Readiness arquitetural | 100% |
| Implementação | não iniciada |
| Marco vigente | M5.17 — Capture Context Wave 0 Implementation Planned |
| Frente operacional | Product Engineering |

## 2. Entrega concluída

- oito incrementos planejados;
- 80 histórias verificáveis;
- 16 dependências classificadas;
- seis ambientes;
- seis POCs;
- 18 evidências distribuídas;
- cinco gates com responsabilidades lógicas;
- 20 riscos iniciais;
- critérios de interrupção;
- dez dossiers tecnológicos;
- estado 0.6.0 consolidado.

## 3. Progressão da UIC-01

| Etapa | Estado |
|---|---|
| Fundação normativa | concluída |
| Modelo de domínio | concluído para implementação |
| Ciclo técnico | concluído |
| Contratos técnicos | concluídos para planejamento |
| Readiness técnico | 100% |
| Planejamento da Onda 0 | concluído |
| Execução da Onda 0 | não iniciada |

## 4. Backlog prioritário

### P0 — Autorizar e preparar W0-01

1. definir local de implementação;
2. atribuir owners nominais;
3. decidir estratégia de repositório e módulos;
4. aprovar política de dados sintéticos;
5. aprovar template de evidências;
6. aprovar registro de riscos e exceções;
7. definir limites de custo;
8. autorizar pipeline mínimo;
9. selecionar ADRs bloqueantes para decisão;
10. manter produção fora do escopo.

### P1 — Decisões bloqueantes

- ADR-TCC-001 — linguagem e framework;
- ADR-TCC-002 — persistência funcional;
- ADR-TCC-004 — eventos e mensageria;
- ADR-TCC-006 — identidade e políticas;
- ADR-TCC-007 — chaves e segredos;
- ADR-TCC-010 — infraestrutura da Onda 0.

### P2 — Execução futura

- W0-02 a W0-08;
- POC-01 a POC-06;
- produção de EV-001 a EV-018;
- execução dos cinco gates;
- decisão de conclusão da Onda 0.

## 5. Próximo marco candidato

> `M5.18 — Capture Context Wave 0 Foundation Authorized`

Condição:

- W0-01 aprovado;
- owners nominais;
- local de implementação;
- estratégia de branches;
- pipeline mínimo;
- política de dados sintéticos;
- templates de evidência;
- riscos críticos com owner;
- ADRs bloqueantes priorizados;
- produção explicitamente fora do escopo.

## 6. Ponto exato de retomada

> Elaborar proposta de execução controlada do W0-01 — Fundação do Projeto.

## 7. Gaps

Não existem gaps arquiteturais reabertos. Descobertas futuras usarão `UIC01-IMP-GAP-###`.

## 8. Limites

Este Roadmap não autoriza:

- execução automática;
- código em produção;
- POC sem decisão;
- dados reais;
- Internal Trial;
- contratação automática;
- avanço das demais UICs;
- go-live.