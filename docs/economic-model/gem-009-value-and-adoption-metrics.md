---
id: GEM-009-VALUE-AND-ADOPTION-METRICS-001
title: Métricas de Valor e Adoção
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-009
---

# Métricas de Valor e Adoção

## 1. Cadeia de observação

```text
elegibilidade → alcance legítimo → ativação → uso significativo → valor percebido → resultado observável → continuidade
```

Cada estágio mantém denominador próprio e não autoriza inferir o estágio seguinte.

## 2. Indicadores candidatos

| Indicador | Fórmula conceitual | Cuidado |
|---|---|---|
| taxa de alcance elegível | alcançados elegíveis / elegíveis | alcance não é compreensão |
| taxa de ativação | ativados / elegíveis expostos | definir ativação por produto |
| tempo para primeiro valor | instante do primeiro valor − início elegível | primeiro valor exige evento legítimo |
| uso significativo | usuários com evento de valor / ativados | frequência isolada não basta |
| continuidade por coorte | ativos na janela posterior / coorte elegível | separar churn voluntário e técnico |
| valor percebido | respostas válidas favoráveis / respostas válidas | viés de resposta explícito |
| resultado observado | casos com resultado elegível / casos avaliáveis | não implica causalidade |
| acessibilidade efetiva | jornadas concluídas com suporte / jornadas que requereram suporte | não reduzir a pessoas com deficiência |

## 3. Segmentações mínimas

Produto, coorte, canal, origem, plano, acesso financiado, contexto geográfico e grupos sujeitos a barreiras, somente quando legítimos, seguros e com tamanho suficiente.

## 4. Guardrails

- tempo de tela, cliques ou recorrência não serão tratados isoladamente como evolução;
- retenção coercitiva, dificuldade de saída ou dependência induzida não contam como valor;
- monetização não poderá elevar artificialmente ativação removendo proteção;
- nenhuma métrica representará dignidade, mérito ou potencial humano.
