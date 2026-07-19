---
title: Roadmap Arquitetural — Estado Reconciliado
status: active
effective_version: 11.12.0
base_document: roadmap.md 11.11.0
owner: Guivos
last_updated: 2026-07-19
related:
  - GE2-SYNC-008
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
---

# Roadmap Arquitetural — Estado Reconciliado 11.12.0

## Autoridade

Este overlay preserva integralmente o [Roadmap 11.11.0](roadmap.md) e prevalece somente sobre estados, versões, prontidão, backlog prioritário e ponto de retomada que tenham sido superados pela publicação do `PAS-001 1.0.0`.

## Estado atual

- **Era vigente:** `GE-2 — Knowledge`.
- **Marco vigente:** `M5.10 — Journey Functional Architecture Published and Engineering Handoff Ready`.
- **Sincronização vigente:** `GE2-SYNC-008 1.0.0`.
- **Frente operacional vigente:** `Product Engineering`.
- **Especificação arquitetural ativa:** `PAS-001 — Guivos Journey 1.0.0`.
- **Mapa final vigente:** `PAS-001-CAPABILITY-MAP-001 1.0.1`.
- **Estado canônico:** `Published — PAS-001 1.0.0 active`.
- **Lacuna bloqueante da arquitetura funcional:** nenhuma.
- **Capacidades concluídas:** nove de nove.
- **Contratos finais:** nove ativos em `1.0.0`.
- **Extensões normativas:** 54 vigentes.
- **Próxima especificação:** `PAS-001-ENGINEERING-HANDOFF-001`.

## Estados superados

| Registro anterior | Estado vigente |
|---|---|
| Captura de Contexto em 95% | Functionally complete — 100% |
| Evolução Contínua em 80% | Functionally complete — 100% |
| Concluir funcionalmente o Journey | Concluído |
| Retomar Capacidade 01 | Histórico |
| Retomar Capacidade 02 | Histórico |
| Executar auditoria final | Concluído |
| Criar Mapa Final | Concluído; mapa ativo 1.0.1 |

## Estado das capacidades

| Nº | Capacidade | Estado | Autoridade final |
|---:|---|---|---|
| 01 | Captura de Contexto | Functionally complete | `PAS-001-CC-CONTRACT-001 1.0.0` |
| 02 | Contexto Vivo | Functionally complete | `PAS-001-CV-CONTRACT-001 1.0.0` |
| 03 | Objetivos | Functionally complete | `PAS-001-OBJ-CONTRACT-001 1.0.0` |
| 04 | Eventos de Vida | Functionally complete | `PAS-001-EV-CONTRACT-001 1.0.0` |
| 05 | Próximos Passos | Functionally complete | `PAS-001-PP-CONTRACT-001 1.0.0` |
| 06 | Oportunidades Ativas | Functionally complete | `PAS-001-OA-CONTRACT-001 1.0.0` |
| 07 | Intervenções Contextuais | Functionally complete | `PAS-001-IC-CONTRACT-001 1.0.0` |
| 08 | Experiências | Functionally complete | `PAS-001-EXP-CONTRACT-001 1.0.0` |
| 09 | Evolução Contínua | Functionally complete | `PAS-001-EC-CONTRACT-001 1.0.0` |

Conclusão funcional não equivale a implementação ou validação em produção.

## Frente ativa — PAS-001-ENGINEERING-HANDOFF-001

O Handoff deverá identificar, por capacidade:

1. agregados e autoridades de domínio;
2. superfícies e jornadas de interação;
3. módulos, serviços e componentes;
4. comandos, eventos e schemas;
5. persistência, busca e grafo;
6. integrações produtoras e consumidoras;
7. identidade, autorização, privacidade e segurança;
8. observabilidade e métricas técnicas;
9. estratégias de teste;
10. protótipos necessários;
11. dependências técnicas;
12. critérios de prontidão;
13. ordem recomendada de implementação;
14. backlog técnico.

## Restrições

- não reabrir capacidades sem fundamento formal;
- não transformar relações funcionais em pipeline obrigatório;
- não reduzir capacidade a tela, serviço ou banco de dados;
- não permitir que Intelligence assuma decisão funcional;
- não permitir que Platform redefina significado;
- não transferir relevância para critérios comerciais;
- não transformar Experiência em Evolução automática;
- não alterar contratos normativos durante o Handoff sem retorno ao documento competente.

## Ponto exato de retomada

> **Criar `PAS-001-ENGINEERING-HANDOFF-001 — Handoff Arquitetural do Guivos Journey para Product Engineering`.**

A próxima decisão deverá aprovar sua proposta normativa antes de qualquer alteração estrutural no GitHub.
