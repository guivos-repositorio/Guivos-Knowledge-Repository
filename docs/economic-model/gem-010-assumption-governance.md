---
id: GEM-010-ASSUMPTION-GOVERNANCE-001
title: Governança de Premissas
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-010
---

# Governança de Premissas

## Classes de evidência

| Classe | Definição | Uso permitido |
|---|---|---|
| E0 | sem evidência | placeholder `TBD`, nunca cálculo oficial |
| E1 | hipótese declarada | exploração e sensibilidade |
| E2 | referência externa contextualizada | cenário provisório |
| E3 | evidência interna observada | calibração com ressalvas |
| E4 | série interna validada | planejamento revisado |
| E5 | evidência reconciliada ou auditada | uso conforme autoridade competente |

## Registro mínimo

Toda premissa deverá conter `assumption_id`, descrição, valor ou `TBD`, unidade, moeda, data-base, período, segmento, fonte, classe de evidência, owner, racional, intervalo, dependências, data de revisão e versão.

## Regras

- nenhuma lacuna será preenchida por conveniência;
- moeda nominal, moeda real e taxa de câmbio deverão ser explícitas;
- premissas correlacionadas não serão variadas como independentes sem justificativa;
- mudança material exige nova versão e registro de impacto;
- hipótese E1 ou E2 não poderá ser apresentada como baseline validado;
- premissa expirada degrada o cenário dependente.

