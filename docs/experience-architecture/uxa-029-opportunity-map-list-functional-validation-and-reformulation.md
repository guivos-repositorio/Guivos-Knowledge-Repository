---
id: UXA-029
title: Contrato Funcional Corrente da Lista Territorial de Oportunidades
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-000
depends_on:
  - UXA-004
  - UXA-009
  - UXA-025
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-201
  - GKR-SURF-PER-202
  - GKR-SURF-PER-203
  - UXA-098
normative: true
---

# Contrato Funcional Corrente da Lista Territorial de Oportunidades

## 1. Finalidade

Governar `GKR-SURF-PER-202 — Lista de Oportunidades` como representação textual integral da mesma consulta territorial de `PER-201`.

A Lista não é uma experiência inferior, um erro do mapa nem uma duplicação de `Explorar`.

## 2. Identidade da consulta

```text
MAPA
↔ LISTA
→ MESMA REGIÃO
→ MESMA BUSCA
→ MESMOS FILTROS
→ MESMA IDENTIDADE DE OPORTUNIDADES
```

Alternar modo não reinicia a jornada nem cria uma nova consulta silenciosa.

## 3. Conteúdo mínimo

A Lista pode apresentar, quando aplicável:

- região ativa;
- busca;
- filtros;
- ordenação explícita;
- quantidade de resultados orgânicos;
- cartões comparáveis;
- oportunidade selecionada;
- relação comercial identificada;
- ação para Detalhe.

Campos ausentes devem ser tratados como ausência de informação, não completados por inferência.

## 4. Ordenação

Ordenação deve ser compreensível e não pode apresentar publicidade como relevância orgânica.

Quando houver unidade patrocinada:

- deve ser identificada;
- contagem orgânica permanece separada;
- primeiro resultado orgânico permanece orgânico conforme contrato de Ads;
- pagamento não altera relevância pessoal.

## 5. Continuidade

Abrir o Detalhe preserva a identidade da oportunidade e o contexto necessário para retorno.

`TRN-210` e `TRN-211` governam a integração atual com Mapa e Detalhe.

## 6. Localização

Lista territorial não exige localização do dispositivo.

Região manual, localização aproximada ou localização temporária autorizada podem produzir a mesma responsabilidade funcional, respeitados os controles de privacidade.

## 7. Sem resultados

A Lista compartilha o mesmo estado de zero resultados da consulta territorial.

Não deve:

- preencher o vazio com publicidade;
- ampliar automaticamente a região;
- remover filtros sem confirmação;
- tratar ausência momentânea de correspondência como ausência de possibilidades para a Pessoa.

## 8. Acessibilidade e resiliência

A Lista é uma forma válida de acesso à descoberta territorial em situações como:

- preferência textual;
- tecnologia cartográfica indisponível;
- baixa conectividade;
- necessidade de comparação;
- requisitos de acessibilidade.

Isso não obriga uma composição visual específica.

## 9. Estado

```text
PER-202
→ FUNCTIONALLY VALIDATED

PER-201 ↔ PER-202
→ SAME QUERY

CHANNEL
→ DESIGN-OWNED / MULTICHANNEL

VISUAL BASELINE
→ NONE REQUIRED
```
