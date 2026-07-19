---
id: GKR-KNOWLEDGE-BOARD-11.13.0
title: Knowledge Board — Engineering Handoff Initiated
status: active
version: 11.13.0
owner: Guivos
last_updated: 2026-07-19
supersedes_state:
  - GKR-KNOWLEDGE-BOARD-11.12.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - M5.11
---

# Knowledge Board — Estado 11.13.0

## 1. Resumo executivo

| Item | Estado |
|---|---|
| Fundação | Frozen |
| Modelo Fundamental | Active |
| GIA-000 | Active 1.3.0 |
| GLPA-001 | Active 1.1.1 |
| PAS-001 | Active 1.0.0 |
| Mapa Final | Active 1.0.1 |
| Engineering Handoff | Draft 0.1.0 |
| Marco vigente | M5.11 |
| Frente | Product Engineering |
| Próxima atividade | UIC-01 — Captura de Contexto |

## 2. Decisões vigentes

| ID | Decisão | Estado |
|---|---|---|
| KB-D-067 | Iniciar o Engineering Handoff sem reabrir o PAS-001 | Active |
| KB-D-068 | Utilizar UIC como unidade padronizada de tradução técnica | Active |
| KB-D-069 | Preservar capacidade como conceito funcional, não topologia técnica | Active |
| KB-D-070 | Adiar escolhas tecnológicas definitivas para ADRs | Active |
| KB-D-071 | Iniciar pela UIC-01 e pelas dependências da Onda 0 | Active |
| KB-D-072 | Tratar segurança, privacidade, observabilidade e testes como requisitos obrigatórios | Active |

## 3. Artefatos ativos da frente

| Artefato | Versão | Função |
|---|---:|---|
| PAS-001-ENGINEERING-HANDOFF-001 | 0.1.0 | Especificação normativa da tradução técnica |
| Product Architecture Overlay | 1.32.0 | Estado efetivo da arquitetura de produtos |
| Roadmap Overlay | 11.13.0 | Ordem de execução e backlog prioritário |
| Knowledge Board Overlay | 11.13.0 | Decisões e estado da frente |
| Architectural Milestones Overlay | 4.11.0 | Registro de M5.11 |
| Canonical Matrix Addendum | 1.32.0 | Reconciliação canônica do novo artefato |
| Changelog Record | 0.60.0 | Registro da alteração |

## 4. Riscos ativos

| ID | Risco | Resposta |
|---|---|---|
| KB-R-031 | Confundir capacidade com microsserviço | Exigir análise de contexto e ADR |
| KB-R-032 | Transferir autoridade por integração | Declarar ownership e decisão própria |
| KB-R-033 | Tratar evento técnico como fato humano | Aplicar taxonomia do Handoff |
| KB-R-034 | Selecionar tecnologia antes dos requisitos | Usar matriz comparativa e ADR |
| KB-R-035 | Produzir perfil paralelo em busca, grafo ou IA | Aplicar finalidade, minimização e revogação |
| KB-R-036 | Avançar sem testes de guardrails | Bloquear prontidão técnica |
| KB-R-037 | Criar sequência obrigatória da jornada | Tratar ondas como ordem técnica, não humana |

## 5. Critério de governança

Nenhuma implementação poderá iniciar como baseline oficial apenas com base no Handoff `0.1.0`.

O avanço requer:

- UIC aprovada;
- especificações técnicas derivadas suficientes;
- ADRs aplicáveis;
- estratégia de testes;
- revisão de segurança e privacidade;
- decisão formal de implementação.

## 6. Próxima atividade

> Elaborar a `UIC-01 — Captura de Contexto`, começando por fontes normativas, autoridade, agregados, invariantes e dependências da Onda 0.