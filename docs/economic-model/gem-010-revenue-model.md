---
id: GEM-010-REVENUE-MODEL-001
title: Modelo de Receitas e Captura
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-010
---

# Modelo de Receitas e Captura

## Estrutura

Cada família deverá modelar volume elegível, base de cobrança, taxa ou preço `TBD`, descontos, cancelamentos, reembolsos, repasses, tributos candidatos, momento de reconhecimento e prazo de recebimento.

## Pontes obrigatórias

```text
volume bruto
→ volume elegível
→ GMV ou base aplicável
→ receita bruta candidata
→ deduções e repasses
→ receita líquida gerencial
→ contas a receber
→ caixa recebido
```

## Guardrails

- aporte, dívida, patrocínio vinculado e recursos de terceiros serão classificados separadamente;
- receita entre produtos será eliminada na consolidação;
- recorrência contratual não será confundida com retenção realizada;
- nenhuma taxa, preço ou critério contábil é aprovado por este documento.

