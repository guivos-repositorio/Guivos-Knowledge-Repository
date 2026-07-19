---
title: Roadmap Arquitetural
status: active
version: 11.12.0
owner: Guivos
last_updated: 2026-07-19
---

# Roadmap Arquitetural

Este roadmap acompanha a evolução do GKR, da arquitetura empresarial e das frentes de especificação executável da Guivos.

## Estado atual

- **Era vigente:** `GE-2 — Knowledge`.
- **Marco vigente:** `M5.10 — Journey Functional Architecture Published and Engineering Handoff Ready`.
- **Sincronização vigente:** `GE2-SYNC-008 1.0.0`.
- **Frente operacional vigente:** `Product Engineering`.
- **Especificação arquitetural ativa:** `PAS-001 — Guivos Journey 1.0.0`.
- **Mapa final vigente:** `PAS-001-CAPABILITY-MAP-001 1.0.1`.
- **Estado canônico:** `Published — PAS-001 1.0.0 active`.
- **Lacuna bloqueante da arquitetura funcional:** nenhuma.
- **Capacidades concluídas:** `01 — Captura de Contexto`, `02 — Contexto Vivo`, `03 — Objetivos`, `04 — Eventos de Vida`, `05 — Próximos Passos`, `06 — Oportunidades Ativas`, `07 — Intervenções Contextuais`, `08 — Experiências` e `09 — Evolução Contínua`.
- **Contratos finais:** nove ativos em `1.0.0`.
- **Extensões normativas:** 54 vigentes.
- **Próxima especificação:** `PAS-001-ENGINEERING-HANDOFF-001`.

## Direção vigente

Transformar a arquitetura funcional publicada do Guivos Journey em planejamento técnico por capacidade, preservando `PAS-001 1.0.0`, o Mapa Final, os contratos especializados e as fronteiras decisórias.

> A unidade de trabalho é a capacidade funcional completa, não uma funcionalidade isolada, tela, microsserviço ou tecnologia.

## Ciclo concluído do PAS-001

| Etapa | Documento | Estado |
|---|---|---|
| Reconciliação | `PAS-001-RECON-001 1.0.0` | Concluída |
| Fechamento das capacidades | 54 extensões e nove contratos finais | Concluído |
| Auditoria final | `PAS-001-AUDIT-001 1.0.0` | 15 gates aprovados |
| Edição candidata | `PAS-001-CANDIDATE-001 1.0.0-rc.1` | Histórica — promoted |
| Validação de release | `PAS-001-RELEASE-VALIDATION-001 1.0.0` | 25 gates aprovados |
| Publicação controlada | `PAS-001-PUBLICATION-001 1.0.0` | Concluída |
| Mapa Final | `PAS-001-CAPABILITY-MAP-001 1.0.1` | Ativo e navegável |
| Reconciliação pós-publicação | `GE2-SYNC-008 1.0.0` | Concluída |

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

Conclusão funcional não equivale a implementação, operação ou validação quantitativa em produção.

## Frente ativa — PAS-001-ENGINEERING-HANDOFF-001

### Finalidade

Produzir uma tradução técnica governada da arquitetura funcional, sem reabrir automaticamente o `PAS-001`.

### Entregáveis obrigatórios

Por capacidade, o Handoff deverá identificar:

1. agregados e autoridades de domínio;
2. superfícies e jornadas de interação;
3. módulos, serviços e componentes;
4. comandos, eventos e schemas;
5. persistência, busca e grafo;
6. integrações produtoras e consumidoras;
7. identidade, autorização, privacidade e segurança;
8. observabilidade e métricas técnicas;
9. testes funcionais, contratuais, de integração e resiliência;
10. protótipos necessários;
11. dependências técnicas;
12. critérios de prontidão;
13. ordem recomendada de implementação;
14. formação do backlog técnico.

### Primeira entrega

Criar `PAS-001-ENGINEERING-HANDOFF-001` com:

- autoridade e vínculo;
- finalidade;
- escopo e não escopo;
- fontes normativas;
- unidade de trabalho;
- princípios de tradução técnica;
- entregáveis;
- critérios de aceite;
- comportamentos proibidos;
- método de decomposição por capacidade.

## Sequência recomendada

```text
PAS-001 1.0.0
→ PAS-001-CAPABILITY-MAP-001 1.0.1
→ PAS-001-ENGINEERING-HANDOFF-001
→ decomposição técnica por capacidade
→ arquitetura física candidata
→ backlog de implementação
→ protótipos e decisões técnicas
→ implementação incremental
```

A ordem de implementação deverá ser recomendada pelo Handoff. A ordem canônica das capacidades não constitui sequência obrigatória de construção.

## Frentes posteriores

1. arquitetura física e decisões técnicas do Journey;
2. backlog de implementação e protótipos;
3. Guivos Economic Model;
4. especificações especializadas de Mall, Business, Intelligence, Ads, Media e Travel;
5. Commercial Model;
6. Go-to-Market;
7. entregáveis operacionais do Guivos Market Validation System.

## Restrições

- não reabrir capacidades sem fundamento formal;
- não transformar relações funcionais em pipeline obrigatório;
- não reduzir capacidade a tela, serviço ou banco de dados;
- não permitir que Intelligence assuma decisão funcional;
- não permitir que Platform redefina significado;
- não transferir relevância para critérios comerciais;
- não transformar Experiência em Evolução automática;
- não criar score humano ou percentual global do Journey;
- não alterar contratos normativos durante o Handoff sem retorno ao documento competente.

## Ponto exato de retomada

> **Criar `PAS-001-ENGINEERING-HANDOFF-001 — Handoff Arquitetural do Guivos Journey para Product Engineering`.**

A próxima decisão deverá aprovar sua proposta normativa antes de qualquer alteração no GitHub.
