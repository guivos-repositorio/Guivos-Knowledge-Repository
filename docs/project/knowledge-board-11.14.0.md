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
  - M5.12
---

# Knowledge Board — Estado Efetivo 11.14.0

> O Knowledge Board-base permanece como inventário histórico. Este overlay prevalece somente sobre frente vigente, versões, decisões correntes, riscos prioritários e retomada.

## Quadro vigente

| Item | Estado |
|---|---|
| PAS-001 | Active 1.0.0 |
| Mapa Final | Active 1.0.1 |
| Engineering Handoff | Draft 0.2.0 efetivo |
| UIC-01 | Draft 0.1.0 |
| Marco | M5.12 |
| Frente | Product Engineering |
| Próxima transição | UIC-01 para Domain model proposed |

## Decisões vigentes

| ID | Decisão | Estado |
|---|---|---|
| D-067 | Adotar PAS-001-CC-UIC-001 como primeira UIC publicada | Aprovada |
| D-068 | Preservar o Handoff-base e elevar sua versão por overlay efetivo | Aprovada |
| D-069 | Manter tecnologia e topologia em aberto até maturidade do domínio | Aprovada |
| D-070 | Tratar CaptureRecord e CaptureSession como hipótese a validar | Aprovada |
| D-071 | Separar entrada, transcrição, interpretação, síntese e confirmação | Aprovada |
| D-072 | Exigir finalidade, autorização, correção e revogação como invariantes transversais | Aprovada |
| D-073 | Priorizar UIC01-GAP-001 e UIC01-GAP-002 | Aprovada |
| D-074 | Definir M5.12 como marco vigente | Aprovada |

## Riscos prioritários

- mistura entre entrada original e interpretação;
- persistência sem autorização;
- revogação incompleta;
- conteúdo sensível em logs ou índices;
- Intelligence promovida a autoridade;
- recorte excessivo para consumidores;
- definição prematura de microsserviços;
- escolha tecnológica anterior à consolidação do domínio.

## Evidências publicadas

- UIC-01 com autoridade, agregados candidatos e invariantes;
- catálogo inicial de comandos e eventos;
- estados e transições preservados;
- produtores e consumidores delimitados;
- classificação de persistência, busca e grafo;
- requisitos de segurança, privacidade, observabilidade e testes;
- dependências da Onda 0;
- 12 riscos e 10 lacunas iniciais.

## Backlog imediato

1. mapa detalhado de agregados;
2. identidade técnica de CaptureInput;
3. invariantes por comando;
4. consistência e concorrência;
5. estratégia de reconstrução;
6. revisão técnica do domínio proposto.

## Ponto de retomada

> Aprofundar agregados, identidades e invariantes da Captura de Contexto.
