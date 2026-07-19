---
id: KNOWLEDGE-BOARD-OVERLAY-11.15.0
title: Knowledge Board — Estado Efetivo 11.15.0
status: active
version: 11.15.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - KNOWLEDGE-BOARD-OVERLAY-11.14.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-LIFECYCLE-001
  - M5.14
---

# Knowledge Board — Estado Efetivo 11.15.0

> O Knowledge Board-base permanece como inventário histórico. Este overlay prevalece somente sobre frente vigente, versões, decisões correntes, riscos prioritários e retomada.

## Quadro vigente

| Item | Estado |
|---|---|
| PAS-001 | Active 1.0.0 |
| Mapa Final | Active 1.0.1 |
| Engineering Handoff | Draft 0.3.0 efetivo |
| UIC-01 | Draft 0.3.0 |
| Estado técnico | Lifecycle technically defined |
| Progresso | 60% |
| Marco | M5.14 |
| Frente | Product Engineering |
| Próxima transição | Contracts technically proposed |

## Decisões vigentes

| ID | Decisão | Estado |
|---|---|---|
| D-075 | Representar a captura por máquinas de estado independentes | Aprovada |
| D-076 | Proibir status global único como autoridade da captura | Aprovada |
| D-077 | Separar estado técnico de fato funcional | Aprovada |
| D-078 | Adotar matriz explícita de transições da sessão | Aprovada |
| D-079 | Revalidar identidade, finalidade e autorização na retomada | Aprovada |
| D-080 | Tratar timeout como falha ou pendência explícita | Aprovada |
| D-081 | Preservar ativos válidos diante de falha parcial | Aprovada |
| D-082 | Exigir compensação para correção e revogação | Aprovada |
| D-083 | Exigir expiração para persistência temporária | Aprovada |
| D-084 | Bloquear conversão automática de temporário em permanente | Aprovada |
| D-085 | Resolver UIC01-GAP-004 e UIC01-GAP-005 | Aprovada |
| D-086 | Definir M5.14 como marco vigente | Aprovada |

## Evidências publicadas

- ciclo técnico com 13 máquinas;
- matriz material da sessão;
- estados e transições de entradas e derivados;
- regras de sincronização;
- guardas por comando;
- continuidade entre canais;
- timeouts e expirações;
- falhas parciais e compensações;
- política de transcrição e correção;
- política de persistência temporária;
- observabilidade de ciclo;
- 60 testes obrigatórios.

## Gaps

| Gap | Estado |
|---|---|
| UIC01-GAP-001 | Resolved |
| UIC01-GAP-002 | Resolved |
| UIC01-GAP-003 | Open |
| UIC01-GAP-004 | Resolved |
| UIC01-GAP-005 | Resolved |
| UIC01-GAP-006 | Open — próximo ciclo |
| UIC01-GAP-007 | Open — próximo ciclo |
| UIC01-GAP-008 | Open |
| UIC01-GAP-009 | Open — próximo ciclo |
| UIC01-GAP-010 | Open |

## Riscos prioritários

- divergência entre máquinas paralelas;
- confirmação sobre síntese desatualizada;
- retry duplicando fato funcional;
- timeout apresentado como sucesso;
- revogação concorrente com emissão de recorte;
- descarte temporário incompleto;
- falha parcial ocultando ativo válido;
- estado técnico promovido a autoridade;
- contrato de consumidor insuficiente;
- schema incompatível sem versionamento.

## Backlog imediato

1. catálogo de comandos;
2. catálogo de eventos;
3. schemas mínimos;
4. contratos síncronos e assíncronos;
5. contratos com consumidores;
6. protocolo completo de revogação;
7. política de reconstrução contratual;
8. dependências da Onda 0;
9. testes de contrato.

## Ponto de retomada

> Elaborar contratos técnicos da Captura de Contexto para alcançar 80%.
