---
id: GKR-UX-PLANS-ORCHESTRATION-001
title: Planos — Superfícies e Fluxos — Documento Mestre de Orquestração UX/UI
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
depends_on:
  - GKR-UX-PLANS-READ-FIRST-001
  - GKR-PLANS-INDEX-001
  - GEM-004-A1
---

# Planos — Superfícies e Fluxos — Documento Mestre de Orquestração UX/UI

## 1. Objetivo

Orquestrar a experiência de planos sem misturar quatro contextos econômicos distintos.

## 2. Arquitetura de alto nível

```text
ENTRADA EM PLANOS
↓
IDENTIFICAR CONTEXTO
├─ Pessoa
├─ Coletivo
├─ Organização
└─ Guivos Business
↓
COMPREENDER PLANOS E DIFERENÇAS
↓
ESCOLHER PERIODICIDADE
├─ Mensal
└─ Anual
↓
DECISÃO
├─ permanecer / voltar
├─ revisar mudança de plano
└─ no Business: configurar composição
```

## 3. Regra de comparação

A comparação deve mostrar diferenças relevantes em capacidades e limites. “Vantagem” significa **capacidade adicional, maior limite, maior profundidade ou menor custo relativo quando uma economia anual estiver documentalmente comprovada**.

A superfície não deve usar superioridade moral, pressão, medo de perda ou garantia de resultado.

## 4. Informação mínima por plano

Cada plano deve possuir nome, finalidade, preço mensal, preço anual, capacidades incluídas, limites principais, diferenças em relação ao tier anterior quando aplicável, condições sujeitas a dimensionamento, ação de continuidade e opção de não prosseguir.

## 5. Mensal e anual

A periodicidade deve ser uma escolha explícita para todo plano pago.

Quando ambas as cifras forem conhecidas, a superfície pode apresentar a comparação entre elas. Economia percentual ou absoluta só pode ser exibida se derivada diretamente dos valores vigentes.

Quando uma cifra não estiver congelada:

```text
ANUAL OU MENSAL
→ DISPONÍVEL
→ VALOR DIMENSIONADO / SOB CONSULTA
```

## 6. Estado atual

Quando houver contexto autenticado e fonte confiável, a superfície pode identificar o plano atual. A ausência de informação não autoriza inferência.

## 7. Continuidade sem efeito comercial

Comparar, alternar periodicidade, abrir detalhes ou selecionar temporariamente um plano para leitura não equivale a contratar.

## 8. Business

Guivos Business acrescenta uma etapa de composição:

```text
PLANO-BASE
+ POPULAÇÃO / ESCALA
+ OFERTA(S)
+ ACESSOS JOURNEY CUSTEADOS
+ CAPACIDADES ADICIONAIS
+ IMPLEMENTAÇÃO / OPERAÇÃO
= VALOR RECORRENTE CONTRATUAL, QUANDO PRECIFICÁVEL

ORÇAMENTO DE INCENTIVO
= RECURSO OPERACIONAL SEPARADO
```

## 9. Estados transversais

Design pode representar, sem criar nova autoridade: carregamento, comparação disponível, preço conhecido, preço dimensionado, periodicidade mensal, periodicidade anual, configuração incompleta, configuração calculável, configuração que exige proposta, erro recuperável e retorno sem alteração.

## 10. Acessibilidade

Diferenças, preços, periodicidade e ações não podem depender apenas de cor, posição ou ícone. Tabelas e cards precisam preservar leitura linear e tecnologias assistivas.

## 11. Critérios de aceite

A experiência é aceitável quando as quatro taxonomias permanecem separadas; mensal/anual é explicitamente selecionável; diferenças funcionais são legíveis; valores não são inventados; dimensionamento é distinguido de preço fixo; comparar não produz contratação; Business separa assinatura de orçamento de incentivo; Design mantém liberdade criativa; e Product Engineering não é liberado por este documento.
