---
id: GEM-010
title: Cenários e Modelo Financeiro
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
related:
  - GEM-009
  - M6.9
---

# GEM-010 — Cenários e Modelo Financeiro

## 1. Objetivo

Definir a arquitetura pela qual premissas rastreáveis poderão ser transformadas em cenários comparáveis de atividade, receita, custos, margem, caixa, capital, capacidade e sustentabilidade, sem inventar valores nem tratar projeções como fatos.

## 2. Princípio central

```text
pergunta decisória
→ data-base e horizonte
→ premissas classificadas
→ drivers e dependências
→ cenário coerente
→ demonstrações reconciliadas
→ sensibilidade e riscos
→ gates e decisão humana
```

## 3. Camadas do modelo

1. premissas e evidências;
2. drivers de usuários, parceiros, transações e capacidade;
3. receitas, custos e margens;
4. caixa, capital de giro, runway e necessidade de capital;
5. unit economics por produto, segmento e coorte;
6. sensibilidades, break-even e eventos de estresse;
7. consolidação entre produtos, reservas, subsídios e reinvestimento;
8. governança, versionamento e gates.

## 4. Estados

`conceptual`, `parameter_pending`, `evidence_pending`, `calibrated`, `reviewed`, `approved_for_planning`, `superseded` ou `retired`.

## 5. Separações canônicas

- cenário não é previsão garantida;
- projeção não é fato, meta ou compromisso;
- receita não é caixa;
- GMV não é receita;
- aporte e dívida não são receita;
- margem não é lucro nem caixa livre;
- break-even contábil não é liquidez suficiente;
- runway não é autorização para consumir reservas protegidas;
- transferência interna não é receita consolidada;
- crescimento modelado não comprova capacidade;
- premissa otimista não é cenário base;
- valuation não é resultado automático do modelo.

## 6. Limites

Esta versão não aprova valores, preços, orçamento, captação, dívida, investimento, política contábil, metas, valuation, operação ou implementação técnica.

## 7. Estado

`conceptually_defined — financial scenario architecture defined, parameters and approvals pending`.

