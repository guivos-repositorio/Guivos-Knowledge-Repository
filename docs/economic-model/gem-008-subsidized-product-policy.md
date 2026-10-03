---
id: GEM-008-SUBSIDIZED-PRODUCT-POLICY-001
title: Política de Produtos Subsidiados
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Política de Produtos Subsidiados

## 1. Objetivo

Definir condições para sustentar produtos ou capacidades que não gerem receita direta suficiente sem ocultar custos, dependências ou ausência de valor.

## 2. Princípio

Um produto poderá ser estrategicamente relevante sem receita direta, mas deverá demonstrar contribuição legítima, fonte de financiamento identificável, custos visíveis e condição de revisão.

## 3. Requisitos

- propósito e valor principal;
- beneficiários;
- fonte candidata;
- custos diretos e compartilhados;
- duração ou condição de revisão;
- evidência de valor;
- dependências críticas;
- hipótese de evolução;
- condição de continuidade;
- condição de redução ou encerramento;
- impacto sobre o gratuito e outros produtos.

## 4. Estados

```yaml
subsidized_product_status:
  not_assessed |
  subsidy_candidate |
  conceptually_supported |
  evidence_required |
  dependency_exposed |
  remediation_required |
  continuation_conditioned |
  exit_candidate
```

## 5. Regras

- subsídio permanente não poderá permanecer invisível;
- relevância institucional não dispensa evidência;
- engajamento não comprova sustentabilidade;
- custos compartilhados deverão permanecer visíveis;
- fonte temporária exigirá transição;
- dependência de fonte única exigirá mitigação;
- ausência de owner ou revisão bloqueia continuidade afirmada;
- produto subsidiado não poderá degradar valor essencial de outro escopo;
- manutenção poderá ser condicionada, reduzida ou encerrada.

## 6. Cenários legítimos

- infraestrutura comum;
- Journey gratuito;
- segurança e privacidade;
- conteúdo e conhecimento;
- acessibilidade;
- experimentação controlada;
- entrada responsável em novo mercado;
- impacto social;
- recuperação temporária de produto relevante.

## 7. Proibições

- manutenção por status ou preferência sem evidência;
- ocultação de inviabilidade;
- uso incompatível de recurso vinculado;
- transferência silenciosa de custo;
- subsídio para comprar relevância;
- promessa de autossustentação sem validação;
- expansão de escopo enquanto a capacidade estiver degradada.

## 8. Fora do escopo

- duração quantitativa;
- orçamento;
- valores;
- decisão sobre produtos específicos;
- encerramento real;
- operação.