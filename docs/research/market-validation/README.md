---
title: Guivos Market Validation System
status: active
version: 1.2.1
owner: Guivos
last_updated: 2026-07-12
---

# Guivos Market Validation System

Este domínio organiza a validação de mercado da Guivos antes do lançamento e durante a evolução dos produtos.

## Objetivo

Transformar hipóteses internas em perguntas testáveis, coletar evidências de mercado e orientar decisões de produto com critérios explícitos.

## Princípios centrais

> A pesquisa não existe para provar que a Guivos é uma boa ideia. Ela existe para descobrir onde a proposta é forte, onde é fraca e o que precisa ser ajustado.

> A Guivos será construída com base em evidências e na participação das pessoas.

> Uma pergunta somente integra uma rodada quando o participante possui informação suficiente para avaliá-la de forma consciente.

## Documentos

- [VAL-001 — Framework de Validação de Mercado](VAL-001-framework-de-validacao-de-mercado.md) — versão 1.2.1;
- [VAL-002 — Pesquisa Conceitual B2C](VAL-002-pesquisa-oficial-da-guivos.md) — versão 1.2.1, título público `Construindo a Guivos`;
- [VAL-003 — Guia do Entrevistador](VAL-003-guia-do-entrevistador.md) — versão 1.1.1;
- [VAL-004 — Modelo de Consolidação e Análise](VAL-004-modelo-de-consolidacao-e-analise.md) — versão 1.2.1;
- [VAL-005 — Plano de Amostragem](VAL-005-plano-de-amostragem.md) — versão 1.1.0;
- [VAL-006 — Dashboard de Indicadores](VAL-006-dashboard-de-indicadores.md) — versão 1.2.1;
- [VAL-007 — Critérios de Decisão](VAL-007-criterios-de-decisao.md) — versão 1.2.1;
- [VAL-008 — Sinais Comportamentais](VAL-008-sinais-comportamentais.md) — versão 1.0.2.

## Sequência oficial

```mermaid
flowchart LR
    A["Hipótese"] --> B["Pesquisa"] --> C["Entrevistas"] --> D["Resultados"] --> E["Dashboard"] --> F["Decisão"] --> G["Ajustes"] --> H["Nova validação"]
```

## Escopo inicial

A primeira aplicação valida a proposta B2C da Guivos, com foco em:

- descoberta tardia de oportunidades potencialmente úteis;
- busca sem encontro de oportunidade adequada ao momento;
- esforço atual para encontrar possibilidades relevantes;
- compreensão da proposta;
- relevância para a área prioritária da vida;
- situação prática de primeiro uso;
- expectativas sobre o que encontrar ou fazer na Guivos;
- resultado concreto considerado valioso;
- contribuição percebida;
- intenção de experimentar uma primeira versão;
- interesse em participar de uma primeira experiência;
- sinais iniciais de monetização;
- barreiras e diferenças entre segmentos.

Confiança operacional, recorrência, retenção e recomendação serão validadas posteriormente por protótipos, beta e comportamento real, e não por previsão abstrata nesta primeira pesquisa.

## Estado operacional

- instrumento oficial revisado para 5 a 7 minutos;
- 22 perguntas principais;
- apenas duas perguntas abertas centrais;
- apresentação da proposta com exemplos de saúde e espiritualidade;
- descoberta tardia e ausência de oportunidade adequada medidas separadamente;
- Índice de Fricção de Oportunidades — IFO composto por `Q8` e `Q9`;
- alternativas codificadas no padrão `n.x`;
- coleta geográfica principal por estado ou Distrito Federal;
- cidade ou município como campo complementar opcional;
- dashboard vinculado diretamente às perguntas;
- IGV composto por problema, compreensão, relevância, contribuição, intenção e primeira experiência;
- critérios formais de `Go`, `Go com ajustes`, `Pivot parcial` e `No-Go temporário`;
- mínimo de 200 respostas válidas para decisão inicial;
- meta preferencial de 500 respostas válidas.

## Entregáveis operacionais pendentes

- formulário definitivo para aplicação;
- planilha automática para recepção, tratamento e cálculo dos KPIs, IGV e gates.