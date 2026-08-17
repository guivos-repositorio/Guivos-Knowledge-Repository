---
id: GKR-BUSINESS-HOME-CONTINUITY-005
title: Checkpoint de Continuidade — Home Pública — Guivos Business — Emissão de Handoff de Design v3
status: active
version: 1.1.0
owner: Experience Architecture
last_updated: 2026-08-16
parent: GKR-BUSINESS-HOME-CONTINUITY-004
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOME-BUSINESS-SOURCELOCK-001
  - GKR-UX-HOME-BUSINESS-GENINPUT-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GPA-004
normative: false
---

# Checkpoint de Continuidade — Home Pública — Guivos Business — Emissão de Handoff de Design v3

## 1. Finalidade

Preservar o ponto exato de continuidade da Home Pública do Guivos Business após a integração do Source Lock e durante a preparação da **emissão v3 do pacote de Design**, seguindo a mesma lógica operacional aplicada às Homes anteriores.

Correção explícita desta continuidade:

> **Esta frente não entra em mapa, wireframe, direção visual, UI ou protótipo. O GKR prepara e congela o pacote; a frente externa de Design materializa depois.**

## 2. Base técnica

```text
MAIN DE PARTIDA
693193ca4cd924d751648a88635ac705286dac94

ÚLTIMO MARCO FUNCIONAL
M7.88

ÚLTIMA UXA NUMERADA
UXA-101

GKR-STATE-001
2.37.0

ROADMAP
12.79.0
```

Esta frente permanece em Experience Architecture e não retoma Product Engineering.

## 3. Estado de convergência

```text
CHECKPOINT 5 — ARQUITETURA NARRATIVA
→ CONVERGIDO

CHECKPOINT 6 — CONTRATOS DE AUTORIDADE
→ CONVERGIDO

CHECKPOINT 7 — CONVERSÃO GLOBAL
→ CONVERGIDO / REFINADO

CHECKPOINT 8 — DOCUMENTO MESTRE
→ CONVERGIDO

SOURCE LOCK BUSINESS
→ INTEGRADO EM GKR-UX-HOME-BUSINESS-SOURCELOCK-001

HANDOFF CANÔNICO
→ GKR-UX-HOMES-DESIGN-HANDOFF-001 EVOLUÍDO PARA v1.2.0 NA EMISSÃO PROPOSTA

MANIFESTO DE ENTREGA
→ GKR-UX-HOMES-DESIGN-DELIVERY-001 EVOLUÍDO PARA v3.0.0 NA EMISSÃO PROPOSTA

SOURCE LOCK OPERACIONAL + PROMPT BUSINESS
→ GKR-UX-HOME-BUSINESS-GENINPUT-001 PROPOSTO

MAPA / WIREFRAME / VISUAL / UI / PROTÓTIPO
→ NÃO INICIADOS NESTA FRENTE
```

## 4. Método vigente

Business passa a seguir o mesmo método das Homes anteriores:

```text
AUTORIDADES CANÔNICAS
↓
SOURCE LOCK
↓
HANDOFF CANÔNICO
↓
MANIFESTO DE ENTREGA
↓
SOURCE LOCK OPERACIONAL + PROMPT
↓
SNAPSHOT EXTERNO / ZIP
↓
DESIGNER / FIGMA MAKE
↓
OUTPUT = EXPLORAÇÃO
↓
VALIDAÇÃO HUMANA
```

O GKR encerra sua responsabilidade operacional da emissão no snapshot/ZIP auditado e no registro pós-merge correspondente.

## 5. Emissão v3

A emissão v3 adiciona Business às seis Homes já presentes na v2 e preserva v1/v2 historicamente.

Composição prevista:

```text
25 FONTES CANÔNICAS
+
7 GUIAS OPERACIONAIS LEIA-PRIMEIRO
=
32 ARQUIVOS NO SNAPSHOT EXTERNO V3
```

A branch externa prevista é:

`delivery/design-handoff-v3`

Ela somente deve ser materializada após integração das autoridades desta emissão na `main`.

## 6. Contexto específico de Business

A pasta Business da emissão v3 deverá utilizar:

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

O contexto maior é deliberado e deriva do próprio Source Lock Business.

## 7. Estado semântico preservado

A emissão deve preservar, entre outros:

- pergunta-mãe `O que sua empresa pode tornar possível para as pessoas?`;
- evolução humana antes do produto;
- `A empresa apoia. A pessoa escolhe.`;
- Journey antes de Incentivos;
- Journey custeado pela empresa sem controle empresarial sobre a Journey;
- Pontos fora da Home;
- Incentivos abrindo possibilidades, não apenas premiando passado;
- ecossistema narrado pela vida da pessoa;
- Intelligence visual;
- CTA `Conheça o Guivos Intelligence`;
- Start / Growth / Scale / Enterprise com comparação;
- configurador comercial;
- contratação online;
- implementação/operação `Self-service / Com apoio do suporte / Gerenciado`;
- suporte depois da contratação quando aplicável;
- escala global;
- Business distinto de Ads e das demais autoridades do ecossistema.

## 8. O que esta frente não fará

Não serão produzidos aqui:

- mapa da página;
- arquitetura visual;
- wireframe;
- direção visual;
- UI;
- protótipo;
- decisões estéticas;
- implementação frontend/backend.

Esses materiais pertencem à etapa externa de Design, exatamente como nas Homes anteriores.

## 9. Próximo ponto exato após integração da emissão v3

Após a PR da emissão v3 ser validada e integrada:

```text
1. reconfirmar a main canônica pós-merge;
2. criar delivery/design-handoff-v3 a partir do conteúdo integrado;
3. materializar a estrutura oficial das sete Homes;
4. criar os sete LEIA-PRIMEIRO operacionais;
5. auditar 25 fontes canônicas + 7 guias;
6. gerar snapshot/ZIP reproduzível;
7. registrar em ato canônico pós-merge o SHA de origem, snapshot commit, tree e contagem exata;
8. preservar delivery/design-handoff-v1 e v2 intactas.
```

Somente depois, fora desta frente, a designer poderá utilizar o pacote para explorar a Home Business.

## 10. Preservações

Este checkpoint não:

- altera M7.88;
- inicia UXA-102/V5;
- retoma Product Engineering;
- implementa a Home;
- define preços;
- define limites, SLA ou entitlements;
- cria Home Intelligence;
- cria clientes, cases ou métricas reais;
- altera GPA-004;
- redefine Points;
- incorpora Ads ao Business;
- produz qualquer artefato visual.

## 11. Instrução de retomada

Ao retomar esta frente:

1. usar `GKR-UX-HOMES-DESIGN-HANDOFF-001` como autoridade comum vigente;
2. usar `GKR-UX-HOMES-DESIGN-DELIVERY-001` como autoridade da emissão;
3. usar `GKR-UX-HOME-BUSINESS-SOURCELOCK-001` como lock semântico;
4. usar `GKR-UX-HOME-BUSINESS-GENINPUT-001` como Source Lock Operacional + Prompt;
5. não iniciar Design visual dentro do GKR;
6. concluir primeiro snapshot/ZIP v3 e registro factual pós-merge.
