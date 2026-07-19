---
id: GKR-ROADMAP-11.13.0
title: Roadmap Arquitetural — Engineering Handoff Initiated
status: active
version: 11.13.0
owner: Guivos
last_updated: 2026-07-19
supersedes_state:
  - GKR-ROADMAP-11.12.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - M5.11
---

# Roadmap Arquitetural — Estado 11.13.0

## 1. Estado vigente

| Dimensão | Estado |
|---|---|
| Frente | Product Engineering |
| PAS-001 | Active 1.0.0 |
| Mapa Final | Active 1.0.1 |
| Engineering Handoff | Draft 0.1.0 |
| Marco | M5.11 — Journey Engineering Handoff Initiated |
| Capacidades funcionais | 9 de 9 concluídas |
| Capacidades tecnicamente traduzidas | 0 de 9 concluídas |
| Próximo incremento | UIC-01 — Captura de Contexto |

## 2. Objetivo da frente

Transformar a arquitetura funcional publicada em especificações técnicas implementáveis, mantendo rastreabilidade, autoridade, segurança, privacidade, observabilidade e testabilidade.

## 3. Backlog prioritário

| Ordem | Item | Resultado esperado | Estado |
|---:|---|---|---|
| 1 | UIC-01 — Captura de Contexto | Tradução técnica completa da capacidade 01 | Next |
| 2 | Foundation técnica da Onda 0 | Identidade, autorização, eventos, auditoria e padrões mínimos | Planned |
| 3 | Catálogo técnico de eventos | Separação entre eventos funcionais, integração e infraestrutura | Planned |
| 4 | Modelo de autorização contextual | Finalidade, papel, escopo e revogação | Planned |
| 5 | Estratégia de persistência | Critérios para transacional, documentos, eventos, busca e grafo | Planned |
| 6 | Observabilidade de guardrails | Sinais, métricas, alertas e auditoria | Planned |
| 7 | UIC-02 — Contexto Vivo | Tradução técnica completa da capacidade 02 | Planned |
| 8 | Backlog das Ondas 1–6 | Dependências e unidades de entrega | Planned |

## 4. Ondas vigentes

| Onda | Escopo | Estado |
|---:|---|---|
| 0 | Foundation técnica e padrões transversais | Initiated |
| 1 | Captura de Contexto e Contexto Vivo | Initiated |
| 2 | Objetivos, Eventos de Vida e Próximos Passos | Planned |
| 3 | Oportunidades Ativas e Intervenções Contextuais | Planned |
| 4 | Experiências e Evolução Contínua | Planned |
| 5 | Intelligence e integrações transversais | Planned |
| 6 | Escala, resiliência e evolução arquitetural | Planned |

## 5. Critério de avanço

O Roadmap somente avançará uma capacidade para `Technically ready for implementation` quando a respectiva UIC possuir:

- fontes normativas mapeadas;
- autoridade e decisões proibidas;
- agregados e invariantes;
- comandos, eventos e estados;
- interfaces e integrações;
- persistência e projeções;
- segurança e privacidade;
- observabilidade;
- estratégia de testes;
- riscos e critérios de prontidão.

## 6. Ponto exato de retomada

> Desenvolver `UIC-01 — Captura de Contexto` no `PAS-001-ENGINEERING-HANDOFF-001`, preservando o contrato final e as extensões `PAS-001-CC-*` como autoridades especializadas.