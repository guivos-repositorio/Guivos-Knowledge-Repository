---
id: GEM-008-CROSS-SUBSIDY-POLICY-001
title: Política de Subsídios Cruzados
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Política de Subsídios Cruzados

## 1. Objetivo

Definir condições conceituais para transferir capacidade ou recursos entre produtos, programas e finalidades sem ocultar custos, utilizar recursos vinculados indevidamente ou manter inviabilidade permanente sem revisão.

## 2. Contrato conceitual

```yaml
subsidy_id: string
source_scope: string
destination_scope: string
purpose: string
beneficiary: string
resource_type: string
restricted: boolean
start_condition: string
review_condition: string
end_condition: string
evidence_required:
  - string
amount_defined: false
allocation_defined: false
```

## 3. Subsídios admissíveis

- financiamento do gratuito;
- segurança e privacidade;
- acessibilidade;
- suporte e contestação;
- conteúdo e conhecimento;
- Intelligence;
- impacto social;
- infraestrutura compartilhada;
- pesquisa e validação;
- recuperação de falha material;
- entrada responsável em novo território.

## 4. Subsídios condicionados

Exigem revisão reforçada:

- produto ainda sem receita;
- expansão geográfica;
- benefício promocional;
- aquisição subsidiada;
- oferta experimental;
- parceiro estratégico;
- capacidade temporariamente ociosa.

## 5. Subsídios proibidos

- uso de recurso vinculado em finalidade incompatível;
- transferência silenciosa de custo ao participante;
- ocultação permanente de inviabilidade;
- financiamento de prática incompatível com propósito;
- manutenção indefinida sem evidência, owner ou revisão;
- redução do gratuito para sustentar produto secundário;
- dupla contagem entre fonte e destino;
- subsídio usado para comprar relevância ou influência.

## 6. Regras

- origem e destino deverão permanecer visíveis;
- benefício esperado não é resultado comprovado;
- subsídio não elimina custo ou risco;
- produto subsidiado deverá possuir hipótese de valor e condição de continuidade;
- recursos restritos deverão manter segregação lógica;
- encerramento deverá tratar obrigações e transição;
- nenhuma alocação financeira é autorizada por este documento.

## 7. Fora do escopo

- valores;
- percentuais;
- rateios;
- transfer pricing;
- contratos;
- orçamento;
- operação.