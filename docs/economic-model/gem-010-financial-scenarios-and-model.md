---
id: GEM-010
title: Cenários e Modelo Financeiro
status: active
version: 0.2.0
owner: Guivos Economic Model
last_updated: 2026-07-28
parent: GEM-000
depends_on:
  - GEM-009
  - GEM-009-DEPENDENCY-VALIDATION-CHECKPOINT-001
related:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-009
  - GEM-010-A1
  - GEM-COMMERCIAL-BASELINE-001
  - M6.9
  - M7.39
---

# GEM-010 — Cenários e Modelo Financeiro

## 1. Objetivo

Definir a arquitetura pela qual premissas rastreáveis poderão ser transformadas em cenários comparáveis de atividade, receita, custos, margem, caixa, capital, capacidade e sustentabilidade, sem inventar valores nem tratar projeções como fatos.

A versão 0.2.0 incorpora preços e limites candidatos dos planos como parâmetros de validação, sem tratá-los como premissas calibradas ou receita aprovada.

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
3. planos, preços, cotas e mix de contratação;
4. receitas, custos e margens;
5. caixa, capital de giro, runway e necessidade de capital;
6. unit economics por produto, segmento e coorte;
7. sensibilidades, break-even e eventos de estresse;
8. consolidação entre produtos, reservas, subsídios e reinvestimento;
9. governança, versionamento e gates.

## 4. Estados

`conceptual`, `candidate_parameterized`, `parameter_pending`, `evidence_pending`, `calibrated`, `reviewed`, `approved_for_planning`, `superseded` ou `retired`.

Os preços do GEM-004-A1 encontram-se em `candidate_parameterized`.

## 5. Separações canônicas

- cenário não é previsão garantida;
- projeção não é fato, meta ou compromisso;
- preço candidato não é disposição a pagar;
- preço publicado não é receita realizada;
- assinatura não é transação;
- GMV não é receita;
- receita não é caixa;
- aporte e dívida não são receita;
- margem não é lucro nem caixa livre;
- break-even contábil não é liquidez suficiente;
- runway não é autorização para consumir reservas protegidas;
- transferência interna não é receita consolidada;
- crescimento modelado não comprova capacidade;
- premissa otimista não é cenário base;
- valuation não é resultado automático do modelo.

## 6. Autoridade de parâmetros comerciais

O GEM-010-A1 governa:

- preços mensais e anuais candidatos;
- faixas de sensibilidade;
- premissas de moeda e cobrança;
- drivers de custo;
- perguntas e métricas de validação;
- unit economics mínimos;
- gates de teste;
- critérios de parada.

## 7. Limites

Esta versão não aprova:

- previsão de receita;
- orçamento;
- captação;
- dívida;
- investimento;
- política contábil;
- metas;
- margem;
- valuation;
- tributos;
- comissão;
- oferta pública;
- operação;
- implementação técnica.

## 8. Estado

`candidate_parameterized — commercial plan prices and limits documented; costs, evidence, specialist reviews and planning approvals pending`.
