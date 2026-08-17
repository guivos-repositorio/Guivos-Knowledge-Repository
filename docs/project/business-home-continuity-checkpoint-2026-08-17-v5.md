---
id: GKR-BUSINESS-HOME-CONTINUITY-005
title: Checkpoint de Continuidade — Home Pública — Guivos Business — Pós-Emissão de Design v3
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-17
parent: GKR-BUSINESS-HOME-CONTINUITY-004
depends_on:
  - GKR-UX-HOME-BUSINESS-SOURCELOCK-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GPA-004
  - GKR-UX-HOME-BUSINESS-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V3-SNAPSHOT-001
  - GKR-STATE-001
  - ROADMAP-12.80.0
normative: false
---

# Checkpoint de Continuidade — Home Pública — Guivos Business — Pós-Emissão de Design v3

## 1. Finalidade

Preservar o ponto exato de continuidade da Home Pública do Guivos Business depois de sua convergência documental, congelamento por Source Lock, inclusão no handoff canônico de Design e materialização da emissão externa v3.

Este checkpoint sucede `GKR-BUSINESS-HOME-CONTINUITY-004`. A v4 permanece como registro histórico do estado imediatamente posterior ao Source Lock, quando Business ainda não fazia parte do handoff de Design.

## 2. Base técnica

```text
MAIN CANÔNICA APÓS REGISTRO PÓS-EMISSÃO V3
2c40d221529ca128bb8d565bc8dfa70efd05f946

SNAPSHOT EXTERNO V3
branch: delivery/design-handoff-v3
commit: 7b2b20c035551e3b1206af987aaddda710757166
tree: 2744a86ca761146a7fcb90ee5ee2e09ef6baefa7

ÚLTIMO MARCO FUNCIONAL
M7.88

ÚLTIMA UXA NUMERADA
UXA-101
```

A evolução da Home Business e sua entrega para Design continuam sendo uma frente de Experience Architecture separada da fila UXA. Não criam novo marco funcional, não iniciam UXA-102/V5 e não retomam Product Engineering.

## 3. Estado de convergência

```text
CHECKPOINT 5 — ARQUITETURA NARRATIVA
→ CONVERGIDO

CHECKPOINT 6 — CONTRATOS DE AUTORIDADE
→ CONVERGIDO

CHECKPOINT 7 — CONVERSÃO GLOBAL
→ CONVERGIDO / REFINADO POR GKR-UX-HOME-BUSINESS-CONVERSION-002

CHECKPOINT 8 — DOCUMENTO MESTRE
→ CONVERGIDO EM GKR-UX-HOME-BUSINESS-MASTER-001

SOURCE LOCK SEMÂNTICO
→ CONVERGIDO EM GKR-UX-HOME-BUSINESS-SOURCELOCK-001

SOURCE LOCK OPERACIONAL + PROMPT
→ CONVERGIDO EM GKR-UX-HOME-BUSINESS-GENINPUT-001

HANDOFF CANÔNICO DE DESIGN
→ BUSINESS INCLUÍDO EM GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.2.0

DESIGN
→ AUTORIZADO PROCEDIMENTALMENTE

SNAPSHOT EXTERNO V3
→ MATERIALIZADO E AUDITADO

OUTPUT VISUAL DA HOME BUSINESS
→ AINDA NÃO PRODUZIDO NESTA FRENTE CANÔNICA
```

## 4. Fonte de verdade da Home Business

A materialização de Design deve preservar a seguinte ordem de autoridade:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.2.0 — regras comuns da fase de Design;
2. `GKR-UX-HOME-BUSINESS-SOURCELOCK-001` — lock semântico superior;
3. `GKR-UX-HOME-BUSINESS-MASTER-001` — Documento Mestre vigente;
4. `GKR-UX-HOME-BUSINESS-CONVERSION-002` — conversão e contratação online vigentes;
5. `GKR-UX-HOME-BUSINESS-AUTHORITY-001` — contratos de autoridade;
6. `GPA-004` v1.6.0 ou autoridade posterior vigente — arquitetura funcional/comercial do produto;
7. `GKR-UX-HOME-BUSINESS-GENINPUT-001` — Source Lock Operacional + Prompt controlado.

O guia `07-HOME-BUSINESS/00-LEIA-PRIMEIRO-BUSINESS.md` da emissão v3 é operacional de embalagem, não nova autoridade canônica.

## 5. Emissão externa v3

A emissão v3 foi materializada a partir do conteúdo canônico integrado à `main` e contém:

```text
25 FONTES CANÔNICAS CONGELADAS
+
7 GUIAS OPERACIONAIS LEIA-PRIMEIRO
=
32 ARQUIVOS EXTERNOS
```

As sete Homes permanecem em contextos isolados:

1. Pessoa;
2. Organizações e Coletivos;
3. Guivos Mall;
4. Guivos Travel;
5. Guivos Media;
6. Guivos Ads;
7. Guivos Business.

A branch `delivery/design-handoff-v3` é artefato externo reproduzível de distribuição. Não constitui fonte canônica paralela à `main`.

As emissões v1 e v2 permanecem historicamente preservadas e não são alteradas pela v3.

O ZIP é apenas embalagem transportável derivada da árvore congelada. O conteúdo autoritativo é determinado pelo snapshot/tree e pelas fontes canônicas da `main`, não por um binário ZIP versionado como autoridade.

## 6. Regras públicas congeladas relevantes para Design

A exploração da Home Business deve preservar, entre outras, estas decisões:

- pergunta-mãe: **O que sua empresa pode tornar possível para as pessoas?**;
- promessa: **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**;
- evolução humana antes do produto;
- assinatura de autonomia: **A empresa apoia. A pessoa escolhe.**;
- Journey antes de Incentivos;
- Journey custeado pela empresa sem controle empresarial sobre a Journey da pessoa;
- Pontos Guivos fora da narrativa pública da Home;
- Incentivos como reconhecimento, estímulo, viabilização e abertura de novas possibilidades;
- ecossistema apresentado pela vida e pelas possibilidades da pessoa antes do catálogo de produtos;
- Guivos Intelligence prioritariamente visual, limitado ao que acontece ou é legitimamente conhecido dentro do ecossistema Guivos;
- CTA `Conheça o Guivos Intelligence`;
- Start / Growth / Scale / Enterprise com comparação de capacidades, sem inventar preços, limites, SLA ou entitlements;
- configurador comercial como experiência de configuração, comparação, estimativa e contratação;
- contratação online como regra vigente;
- modelos de implementação/operação `Self-service`, `Com apoio do suporte` e `Gerenciado`;
- no modelo `Com apoio do suporte`, suporte após a contratação online;
- Business distinto de Ads e das demais autoridades do ecossistema;
- princípio de escala global sem presumir disponibilidade concreta de país, moeda ou entidade ainda não evidenciada.

## 7. O que a autorização de Design permite

A autorização procedimental permite, fora desta frente canônica:

- arquitetura visual;
- wireframe low-fi;
- estudos de hierarquia e composição;
- direção visual;
- UX/UI;
- protótipos;
- estudos responsivos;
- exploração generativa controlada por Figma Make ou ferramenta equivalente.

Todo primeiro output permanece:

```text
EXPLORAÇÃO
≠ AUTORIDADE CANÔNICA
≠ IMPLEMENTAÇÃO
≠ PUBLICAÇÃO
```

Nenhum output se promove automaticamente ao GKR.

## 8. Preservações

Este checkpoint não:

- altera `M7.88`;
- inicia `UXA-102/V5`;
- retoma Product Engineering;
- altera `GPA-004`;
- muda as duas ofertas principais do Business;
- cria Journey corporativa;
- transforma Intelligence em auditor de KPIs internos;
- incorpora Ads ao Business;
- redefine economia de Pontos;
- recoloca Pontos na Home pública;
- define preços finais;
- define limites quantitativos;
- define SLA;
- congela entitlements não formalizados;
- define países, moedas, meios de pagamento ou entidades concretamente disponíveis;
- define fórmula final do configurador;
- cria a Home Guivos Intelligence;
- materializa Design dentro do GKR;
- aprova automaticamente qualquer output visual;
- autoriza implementação ou publicação.

## 9. Próximo ponto exato

A etapa documental da Home Business necessária para iniciar Design está concluída.

O próximo ato é:

> **MATERIALIZAR A PRIMEIRA EXPLORAÇÃO DE DESIGN DA HOME GUIVOS BUSINESS A PARTIR DO CONTEXTO ISOLADO DA EMISSÃO V3 E SUBMETÊ-LA À VALIDAÇÃO HUMANA CONTRA O SOURCE LOCK.**

Fluxo:

```text
PACOTE BUSINESS V3
→ leitura na ordem governada
→ execução na frente externa de Design
→ OUTPUT = EXPLORAÇÃO
→ revisão humana contra Source Lock + Documento Mestre + contratos vigentes
→ ajustes, se necessários
→ decisão explícita sobre eventual promoção de uma direção
```

A existência do handoff e do snapshot não exige que Design seja produzido no GKR nem autoriza a ferramenta a redefinir narrativa, produto, autoridade ou conversão.

## 10. Instrução de retomada

Ao retomar a Home Guivos Business:

1. considerar Checkpoints 5, 6, 7 e 8 convergidos;
2. considerar Source Lock semântico concluído;
3. considerar Source Lock Operacional + Prompt concluído;
4. considerar Business incluído no handoff canônico de Design v1.2.0;
5. considerar a emissão externa v3 materializada e auditada;
6. usar somente o contexto isolado da pasta `07-HOME-BUSINESS` junto do Handoff Canônico comum;
7. não misturar fontes específicas das demais Homes na mesma execução generativa;
8. preservar Pontos fora da Home pública;
9. preservar contratação online e os três modelos de implementação/operação;
10. tratar qualquer primeiro output visual como `EXPLORAÇÃO`;
11. não retomar UXA-102/V5 ou Product Engineering por consequência desta frente;
12. próximo ato: exploração externa de Design + validação humana.