---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 1.2.0
owner: Experience Architecture
last_updated: 2026-08-16
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
normative: false
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este guia registra como a pessoa responsável por Design, UX e UI deve iniciar o trabalho após receber o pacote externo vigente das **sete Homes públicas da Guivos**.

Ele é subordinado a `GKR-UX-HOMES-DESIGN-DELIVERY-001` e `GKR-UX-HOMES-DESIGN-HANDOFF-001`.

Este documento:

- não cria nova arquitetura;
- não substitui o Manifesto Canônico de Entrega;
- não substitui o Handoff Canônico;
- não altera Documentos Mestres ou Source Locks;
- não produz mapa, wireframe, direção visual, UI ou protótipo;
- não autoriza implementação ou publicação.

## 2. Fluxo obrigatório após recebimento do pacote

```text
BAIXAR O ZIP DA EMISSÃO VIGENTE
      ↓
abrir 00-LEIA-PRIMEIRO
      ↓
escolher UMA Home
      ↓
abrir o LEIA-PRIMEIRO daquela Home
      ↓
seguir somente os documentos indicados
      ↓
usar o Source Lock + Prompt da Home
      ↓
OUTPUT EXTERNO = EXPLORAÇÃO
```

A sequência significa:

1. baixar o ZIP oficial da emissão vigente;
2. ler o Handoff Canônico comum;
3. escolher somente uma Home: Pessoa, Organizações e Coletivos, Mall, Travel, Media, Ads ou Business;
4. abrir o `LEIA-PRIMEIRO` daquela Home;
5. carregar somente as fontes específicas indicadas naquele contexto;
6. utilizar o Source Lock + Prompt Controlado no Figma Make ou ferramenta equivalente;
7. tratar toda saída como `EXPLORAÇÃO` até validação humana.

## 3. Regra de isolamento de contexto

> **Uma Home = uma execução semanticamente isolada.**

Não carregar simultaneamente documentos específicos das sete Homes.

As seis Homes já presentes na emissão v2 preservam o fluxo de contexto mínimo já vigente.

Business utiliza contexto específico maior porque suas fronteiras vigentes são distribuídas por Source Lock, Documento Mestre, Conversão, Contratos de Autoridade e `GPA-004`.

## 4. Regra específica para Guivos Ads

Para Ads, permanece:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-ADS-MASTER-001
+
GPA-007
+
GKR-UX-HOME-ADS-GENINPUT-001
```

Não carregar automaticamente contratos detalhados do Opportunity Boost, pricing ou documentação operacional de outros produtos.

## 5. Regra específica para Guivos Business

Para Business, utilizar:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-BUSINESS-SOURCELOCK-001
+
GKR-UX-HOME-BUSINESS-MASTER-001
+
GKR-UX-HOME-BUSINESS-CONVERSION-002
+
GKR-UX-HOME-BUSINESS-AUTHORITY-001
+
GPA-004
+
GKR-UX-HOME-BUSINESS-GENINPUT-001
```

Ordem operacional:

```text
HANDOFF COMUM
↓
SOURCE LOCK SEMÂNTICO BUSINESS
↓
DOCUMENTO MESTRE
↓
CONVERSÃO GLOBAL
↓
CONTRATOS DE AUTORIDADE
↓
GPA-004
↓
SOURCE LOCK OPERACIONAL + PROMPT
↓
EXECUÇÃO EXTERNA
```

Não carregar automaticamente:

- outras Homes;
- conversão v1;
- documentos históricos;
- pricing ainda não formalizado;
- Ads;
- benchmarks como requisito;
- documentos adicionais de Journey sem dúvida concreta.

## 6. Estado do resultado gerado

Todo resultado inicial produzido pela frente de Design, Figma Make ou ferramenta equivalente começa obrigatoriamente como:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

Fluxo de promoção:

```text
EXPLORAÇÃO
↓
CANDIDATO
↓
VALIDADO EM UX
↓
VALIDADO EM UI
↓
APROVADO PARA HANDOFF DE ENGENHARIA
```

A ferramenta generativa não possui autoridade para promover seu próprio output.

## 7. Relação entre v1, v2 e v3

- v1 permanece snapshot histórico íntegro das cinco Homes originalmente entregues;
- v2 adicionou Guivos Ads e permanece preservada;
- v3 adiciona Guivos Business em nova branch/snapshot/ZIP próprios após integração canônica.

Não misturar arquivos entre emissões sem reconciliação explícita.

## 8. Regra final

> **Baixe a emissão correta, leia a orientação comum, escolha uma Home, mantenha o contexto isolado e só então use o Source Lock + Prompt como entrada da exploração externa.**

O GKR governa o significado. Design governa a materialização. Ferramentas generativas ampliam a exploração; não decidem a arquitetura da Guivos.
