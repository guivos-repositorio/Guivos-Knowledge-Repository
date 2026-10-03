---
id: GKR-BUSINESS-HOME-CONTINUITY-003
title: Checkpoint de Continuidade — Home Pública — Guivos Business — Pós-Documento Mestre
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-16
parent: GKR-BUSINESS-HOME-CONTINUITY-002
depends_on:
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GKR-UX-HOME-BUSINESS-NARRATIVE-001
  - GPA-004
  - GKR-STATE-001
  - ROADMAP-12.79.0
normative: false
---

# Checkpoint de Continuidade — Home Pública — Guivos Business — Pós-Documento Mestre

## 1. Finalidade

Preservar o ponto exato de continuidade da Home Pública do Guivos Business após a validação do Documento Mestre v2 em conversa.

Este checkpoint sucede `GKR-BUSINESS-HOME-CONTINUITY-002` para fins de retomada da Home Business.

## 2. Base técnica

```text
MAIN DE PARTIDA
d149b1497b791f0b7396dd12b90c272a605d2c27

ÚLTIMO MARCO FUNCIONAL
M7.88

ÚLTIMA UXA NUMERADA
UXA-101

GKR-STATE-001
2.37.0

ROADMAP
12.79.0
```

Esta atualização de Experience Architecture não cria novo marco funcional, não inicia UXA-102/V5 e não retoma Product Engineering.

## 3. Estado de convergência

```text
CHECKPOINT 5 — ARQUITETURA NARRATIVA
→ CONVERGIDO

CHECKPOINT 6 — CONTRATOS DE AUTORIDADE
→ CONVERGIDO

CHECKPOINT 7 — CONVERSÃO GLOBAL
→ CONVERGIDO E REFINADO POR GKR-UX-HOME-BUSINESS-CONVERSION-002

CHECKPOINT 8 — DOCUMENTO MESTRE
→ CONVERGIDO EM GKR-UX-HOME-BUSINESS-MASTER-001

SOURCE LOCK
→ NÃO EXISTE

DESIGN
→ NÃO AUTORIZADO
```

## 4. Refinamentos posteriores ao Checkpoint 7

### 4.1 Pontos não aparecem na Home

Pontos Guivos permanecem mecanismo interno/funcional, mas a Home Business não precisa mencioná-los.

A narrativa pública não deve reintroduzir pontos como explicação de incentivo, benefício ou possibilidade.

### 4.2 Incentivos e benefícios não são movimentos separados

O antigo desenho público `Incentivos → Benefícios` foi substituído por um único movimento:

> **Reconheça. Incentive. Abra novas possibilidades.**

O incentivo pode reconhecer algo que aconteceu, estimular algo que está começando, viabilizar acesso ou abrir uma possibilidade.

### 4.3 Intelligence é demonstrado visualmente

A seção Intelligence deve utilizar direção visual de dashboards, KPIs, gráficos, tendências, participação, utilização, recorrência, interesses agregados e movimentos ao longo do tempo.

Copy de referência:

> **Entenda como as pessoas participam, utilizam e se movimentam entre as possibilidades que escolhem dentro do ecossistema Guivos.**

A seção preserva CTA:

> **Conheça o Guivos Intelligence**

O destino arquitetônico é a futura Home própria do Guivos Intelligence, ainda não construída.

### 4.4 Planos ganham comparativo

A Home deve apresentar Start, Growth, Scale e Enterprise e prever comparação entre capacidades, sem inventar preços, limites, SLA ou entitlements ainda não formalizados.

### 4.5 Configurador substitui simples calculadora

O Movimento 09 deve combinar:

```text
CONFIGURAÇÃO
+
COMPARAÇÃO
+
VALOR / ESTIMATIVA
+
MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
+
CONTRATAÇÃO ONLINE
```

Ele pode considerar fatores como número de pessoas, oferta, plano/capacidade, tipo de operação, Intelligence, integrações, governança, serviço e mercado.

### 4.6 Toda contratação é online

Fica substituída a antiga separação `Online / Assistida / Especializada` como forma de contratação.

A arquitetura vigente é:

```text
CONTRATAÇÃO
→ ONLINE

MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
→ SELF-SERVICE
→ COM APOIO DO SUPORTE
→ GERENCIADO
```

No modelo `Com apoio do suporte`, a contratação e o pagamento ocorrem normalmente online; o suporte entra depois para continuidade da implementação.

## 5. Arquitetura pública vigente — 10 movimentos

```text
01 — POSSIBILIDADE
O que sua empresa pode tornar possível para as pessoas?

02 — PROPÓSITO
Empresas também podem ajudar seres humanos a terem uma vida melhor

03 — AUTONOMIA
A empresa apoia. A pessoa escolhe.

04 — JOURNEY
Amplie o acesso à evolução

05 — INCENTIVOS
Reconheça. Incentive. Abra novas possibilidades.

06 — ECOSSISTEMA
Diferentes áreas da vida. Diferentes possibilidades.

07 — INTELLIGENCE
Compreenda os movimentos dentro da Guivos

08 — PLANOS
Encontre a capacidade adequada para sua empresa

09 — CONFIGURADOR / CONTRATAÇÃO
Configure. Compare. Contrate.

10 — SÍNTESE
O que sua empresa pode tornar possível?
```

## 6. Formulações centrais preservadas

Pergunta-mãe:

> **O que sua empresa pode tornar possível para as pessoas?**

Tese:

> **Quando uma empresa amplia possibilidades para as pessoas, novas possibilidades também se abrem para a própria empresa.**

Promessa:

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

Autonomia:

> **A empresa apoia. A pessoa escolhe.**

Journey:

> **Sua empresa pode oferecer acesso ao Guivos Journey e permitir que seus funcionários encontrem caminhos, experiências e possibilidades de evolução relevantes para suas próprias vidas.**

Guardrail humano:

> **Empresas não definem quem as pessoas devem se tornar. Podem, porém, ampliar as condições e possibilidades para que elas construam vidas melhores.**

## 7. Preservações

Esta atualização não:

- altera `M7.88`;
- inicia `UXA-102/V5`;
- retoma Product Engineering;
- altera `GPA-004`;
- muda as duas ofertas principais do Business;
- cria Journey corporativa;
- transforma Intelligence em auditor de KPIs internos;
- incorpora Ads ao Business;
- redefine economia de Pontos;
- define preços finais;
- define limites quantitativos;
- define SLA;
- congela entitlements;
- define disponibilidade concreta por país/moeda;
- cria Source Lock;
- autoriza Design.

## 8. Próximo ponto exato

A próxima etapa governada é:

> **SOURCE LOCK — HOME GUIVOS BUSINESS**

Objetivo:

- congelar a fonte pública aprovada para implementação;
- eliminar ambiguidades entre documentos anteriores e Documento Mestre;
- estabelecer o texto/fonte que Design deverá tratar como referência imutável salvo nova decisão explícita.

## 9. Instrução de retomada

Ao retomar a Home Guivos Business:

1. usar `GKR-UX-HOME-BUSINESS-MASTER-001` como Documento Mestre vigente;
2. usar `GKR-UX-HOME-BUSINESS-CONVERSION-002` como autoridade vigente de conversão;
3. preservar `GKR-UX-HOME-BUSINESS-AUTHORITY-001` para fronteiras de autoridade;
4. preservar `GKR-UX-HOME-BUSINESS-NARRATIVE-001` como origem da arquitetura narrativa, observando os refinamentos de precedência do Documento Mestre;
5. não recolocar Pontos na Home;
6. não separar Benefícios como movimento próprio;
7. preservar CTA `Conheça o Guivos Intelligence` para a futura Home Intelligence;
8. tratar toda contratação como online;
9. distinguir apenas os modelos de implementação/operação: Self-service, Com apoio do suporte e Gerenciado;
10. iniciar pelo Source Lock;
11. não avançar para Design antes da integração do Source Lock apropriado.
