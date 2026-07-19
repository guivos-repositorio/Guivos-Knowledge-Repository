---
id: GKR-CHANGELOG-0.61.0
status: active
version: 0.61.0
owner: Guivos
last_updated: 2026-07-19
related:
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - M5.13
---

# Changelog 0.61.0 — UIC-01 Domain Model Proposed

## Added

- `PAS-001-CC-UIC-001 0.1.0` como fundação da primeira Unidade de Implementação de Capacidade;
- `PAS-001-CC-UIC-001` em estado efetivo `Draft 0.2.0`;
- `PAS-001-CC-UIC-DOMAIN-001 0.1.0`;
- autoridade, finalidade, escopo e decisões proibidas;
- `CaptureRecord` confirmado como Aggregate Root;
- `CaptureSession` confirmada como entidade interna;
- cardinalidade entre registro, sessões, entradas e derivados;
- política completa de identidades funcionais;
- identidade permanente e independente de `CaptureInput`;
- classificação de agregados, entidades, objetos de valor, projeções e registros técnicos;
- 31 invariantes estruturais confirmadas;
- limites de consistência imediata e eventual;
- regras de concorrência otimista;
- idempotência material;
- matriz comando–agregado–invariantes–evento;
- modelo inicial de reconstrução;
- mapa de agregados;
- diagrama de entidades e relações;
- fluxo comando–agregado–evento;
- ciclo técnico da sessão;
- propagação de correção;
- propagação de revogação;
- 28 testes obrigatórios de domínio;
- resolução de `UIC01-GAP-001`;
- resolução de `UIC01-GAP-002`.

## Changed

- Engineering Handoff mantido em estado efetivo `Draft 0.2.0`, agora registrando a UIC-01 em `Domain model proposed`;
- UIC-01 elevada de `Normative sources mapped — 20%` para `Domain model proposed — 40%`;
- Arquitetura de Produtos efetiva `1.33.0`;
- Roadmap efetivo `11.14.0`;
- Knowledge Board efetivo `11.14.0`;
- Architectural Milestones efetivo `4.12.0`;
- Matriz de Consolidação Canônica efetiva `1.33.0`;
- marco vigente atualizado para `M5.13`;
- ponto de retomada atualizado para o ciclo técnico da UIC-01.

## Resolved

- `UIC01-GAP-001 — limite entre CaptureRecord e CaptureSession`;
- `UIC01-GAP-002 — identidade técnica da entrada original`.

## Preserved

- PAS-001 1.0.0;
- Mapa Final 1.0.1;
- Handoff-base 0.1.0;
- UIC-base 0.1.0;
- nove contratos finais;
- 54 extensões normativas;
- GLPA-001 1.1.1;
- GIA-000 1.3.0;
- documentos-base históricos;
- ausência de decisões tecnológicas definitivas.

## Milestone

> `M5.13 — Capture Context Domain Model Proposed`

## Next

> Definir máquinas de estado, transições, compensações, timeouts, falhas parciais e testes de ciclo para preparar `M5.14 — Capture Context Technical Lifecycle Defined` e elevar a UIC-01 para 60%.
