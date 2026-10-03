---
id: KNOWLEDGE-BOARD-OVERLAY-11.14.0
title: Knowledge Board — Estado Efetivo 11.14.0
status: active
version: 11.14.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - KNOWLEDGE-BOARD-OVERLAY-11.13.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-DOMAIN-001
  - M5.13
---

# Knowledge Board — Estado Efetivo 11.14.0

> O Knowledge Board-base permanece como inventário histórico. Este overlay prevalece somente sobre frente vigente, versões, decisões correntes, riscos prioritários e retomada.

## Quadro vigente

| Item | Estado |
|---|---|
| PAS-001 | Active 1.0.0 |
| Mapa Final | Active 1.0.1 |
| Engineering Handoff | Draft 0.2.0 efetivo |
| UIC-01 | Draft 0.2.0 efetivo |
| Estado técnico | Domain model proposed |
| Progresso | 40% |
| Marco | M5.13 |
| Frente | Product Engineering |
| Próxima transição | Lifecycle technically defined — 60% |

## Decisões vigentes

| ID | Decisão | Estado |
|---|---|---|
| D-067 | Adotar PAS-001-CC-UIC-001 como primeira UIC publicada | Aprovada |
| D-068 | Preservar o Handoff-base e elevar sua versão por overlay efetivo | Aprovada |
| D-069 | Manter tecnologia e topologia em aberto até maturidade do domínio | Aprovada |
| D-070 | Confirmar `CaptureRecord` como Aggregate Root | Aprovada |
| D-071 | Confirmar `CaptureSession` como entidade interna com identidade própria | Aprovada |
| D-072 | Separar entrada, transcrição, interpretação, síntese e confirmação | Aprovada |
| D-073 | Definir identidade permanente e opaca para `CaptureInput` | Aprovada |
| D-074 | Adotar consistência imediata para alterações funcionais do registro | Aprovada |
| D-075 | Permitir consistência eventual apenas para derivados e projeções controladas | Aprovada |
| D-076 | Adotar concorrência otimista e idempotência material | Aprovada |
| D-077 | Tratar autorização como agregado auxiliar e revogação como processo explícito | Aprovada |
| D-078 | Resolver `UIC01-GAP-001` e `UIC01-GAP-002` | Aprovada |
| D-079 | Definir M5.13 como marco vigente | Aprovada |

## Riscos prioritários

- confirmação sobre síntese desatualizada;
- conflito entre correções concorrentes;
- revogação durante processamento;
- reconstrução de conteúdo legitimamente eliminado;
- conteúdo sensível em eventos, logs ou índices;
- autorização ampliada por consumidor;
- transformação do agregado em microsserviço por conveniência;
- escolha tecnológica anterior ao ciclo técnico completo.

## Evidências publicadas

- mapa de agregados;
- classificação de entidades e objetos de valor;
- política de identidades;
- 31 invariantes estruturais confirmadas;
- matriz comando–agregado–invariantes–evento;
- limites de consistência;
- regras de concorrência e idempotência;
- modelo de reconstrução;
- diagramas de correção e revogação;
- 28 testes obrigatórios de domínio;
- resolução documentada de dois gaps prioritários.

## Backlog imediato

1. máquinas de estado independentes;
2. matriz completa de transições;
3. precondições e efeitos por transição;
4. compensações e timeouts;
5. falhas parciais;
6. testes completos de ciclo;
7. revisão técnica para `Lifecycle technically defined`.

## Ponto de retomada

> Definir tecnicamente o ciclo de vida da UIC-01 e elevá-la para 60%.
