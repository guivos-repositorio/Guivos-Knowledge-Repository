---
id: PRODUCT-ARCHITECTURE-OVERLAY-1.34.0
title: Product Architecture Effective State 1.34.0
status: active
version: 1.34.0
owner: Guivos
last_updated: 2026-07-19
normative: true
supersedes_partial:
  - PRODUCT-ARCHITECTURE-OVERLAY-1.33.0
related:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-LIFECYCLE-001
---

# Arquitetura de Produtos — Estado Efetivo 1.34.0

> Este overlay preserva o índice e o inventário histórico. Ele prevalece somente sobre versão efetiva, estado técnico da UIC-01, marco vigente e ponto de retomada.

## Estado arquitetural

| Ativo | Estado efetivo |
|---|---|
| PAS-001 | Active 1.0.0 |
| Mapa Final | Active 1.0.1 |
| Engineering Handoff | Draft 0.3.0 efetivo |
| UIC-01 — Captura de Contexto | Draft 0.3.0 |
| Modelo de domínio | Domain model proposed |
| Ciclo técnico | Lifecycle technically defined |
| Progresso UIC-01 | 60% |
| Capacidades 01–09 | Functionally complete |
| Frente operacional | Product Engineering |
| Marco vigente | M5.14 |

## Novo ativo normativo

[`PAS-001-CC-UIC-LIFECYCLE-001`](pas-001-captura-de-contexto-technical-lifecycle.md) define:

- máquinas de estado independentes;
- coordenação pelo agregado;
- matriz de transições da sessão;
- estados de entradas e derivados;
- guardas por comando;
- pausa, retomada e continuidade entre canais;
- timeouts e expirações;
- falhas parciais, retries e compensações;
- sincronização funcional-técnica;
- transcrição e persistência temporária;
- observabilidade e testes de ciclo.

## Decisões consolidadas

1. estado global único é proibido para representar a captura;
2. máquinas técnicas não substituem autoridade funcional;
3. operação técnica concluída não cria fato funcional automaticamente;
4. correção preserva histórico e reabre derivados afetados;
5. revogação bloqueia novos usos antes da propagação completa;
6. persistência temporária exige expiração e descarte verificável;
7. falhas parciais preservam ativos válidos e não fabricam sucesso.

## Gaps resolvidos acumulados

- UIC01-GAP-001;
- UIC01-GAP-002;
- UIC01-GAP-004;
- UIC01-GAP-005.

## Autoridades preservadas

Permanecem inalterados:

- PAS-001 1.0.0;
- Mapa Final 1.0.1;
- nove contratos finais;
- 54 extensões normativas;
- GLPA-001 1.1.1;
- GIA-000 1.3.0.

## Próximo ponto

> Elaborar contratos técnicos da Captura de Contexto para alcançar `Contracts technically proposed — 80%`.
