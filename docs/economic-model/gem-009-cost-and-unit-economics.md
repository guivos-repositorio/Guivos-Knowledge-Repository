---
id: GEM-009-COST-AND-UNIT-ECONOMICS-001
title: Métricas de Custos e Unit Economics Conceitual
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-009
---

# Métricas de Custos e Unit Economics Conceitual

## 1. Objetivo

Definir relações econômicas analisáveis por unidade sem escolher valores, método contábil, rateio definitivo ou conclusão de viabilidade.

## 2. Unidade econômica

Cada análise deverá declarar uma unidade coerente, como relação ativa, transação concluída, participante servido, parceiro ativo, programa ou coorte. Unidades incompatíveis não serão combinadas.

## 3. Indicadores candidatos

| Indicador | Fórmula conceitual | Limite |
|---|---|---|
| custo direto unitário | custos diretos elegíveis / unidades entregues | não inclui automaticamente estrutura |
| custo de servir | custos de entrega e suporte elegíveis / unidades servidas | população deve ser estável |
| margem de contribuição unitária | receita líquida elegível − custos variáveis e obrigações atribuíveis | não é lucro líquido |
| CAC conceitual | custos incrementais de aquisição elegíveis / novas relações qualificadas | excluir alcance sem qualificação |
| payback conceitual | CAC / contribuição periódica elegível | inválido sem contribuição estável |
| LTV conceitual | contribuição esperada durante relação legítima | exige retenção, incerteza e sensibilidade |
| relação LTV/CAC | LTV conceitual / CAC conceitual | não aprova escala |
| custo de qualidade | prevenção + avaliação + correção elegíveis | não incentiva reduzir proteção |
| custo de falha | reembolso + retrabalho + suporte + perdas elegíveis | externalidades permanecem visíveis |

## 4. Regras

- custos compartilhados serão exibidos antes e depois de qualquer alocação candidata;
- alocação deverá declarar driver, período e sensibilidade;
- CAC e LTV serão segmentados por coorte e origem quando possível;
- benefício indireto não será convertido em receita sem evento admissível;
- resultados negativos ou inconclusivos permanecerão visíveis;
- unit economics favorável não compensa falha de propósito, segurança ou qualidade.

## 5. Estado desta versão

`formulas_defined — values, allocation methods and viability conclusions pending`.
