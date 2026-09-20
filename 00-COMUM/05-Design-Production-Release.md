---
id: GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
title: Homes Públicas — Autorização Governada de Design Production Release
status: active
version: 1.2.1
owner: Guivos
last_updated: 2026-09-19
normative: true
maturity: design_production_release_granted_current_package_delegated
depends_on:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
related:
  - GKR-STATE-001
  - GKR-HOME-MASTERS-REMEDIATION-001
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
---

# Homes Públicas — Autorização Governada de Design Production Release

## 1. Finalidade

Esta autoridade registra o ato humano que libera a **produção externa de Design das oito Homes pela designer**, usando o GKR como fonte de verdade semântica e funcional.

O release permanece válido como autorização humana. Sua execução operacional, porém, exige um pacote externo corrente e semanticamente válido. Um release concedido não cura contradições internas de um snapshot nem autoriza usar um pacote posteriormente invalidado. O método de execução permanece designer-first:

```text
DESIGN PRODUCTION RELEASE
→ GRANTED

DESIGNER
→ CREATIVE AUTHOR
→ MANUAL PRODUCTION IS FIRST-CLASS

AI
→ OPTIONAL TOOL AT DESIGNER DISCRETION

GKR / CHATGPT
→ DOES NOT CREATE FIGMA
→ DOES NOT PRECOMPOSE VISUAL DIRECTION
→ DOES NOT REPLACE DESIGNER

AUTHORIZATION
≠ DESIGN OUTPUT
≠ FINAL ACCEPTANCE
≠ IMPLEMENTATION
```

## 2. Alvos autorizados

```text
HOME PESSOA
HOME ORGANIZAÇÕES E COLETIVOS
HOME MALL
HOME TRAVEL
HOME MEDIA
HOME ADS
HOME BUSINESS
HOME INTELLIGENCE
```

A autorização vale para o trabalho externo de Design sobre fontes governadas.

Ela não obriga:

- qualquer ferramenta generativa específica;
- qualquer IA específica;
- qualquer ferramenta generativa;
- protótipo gerado previamente pelo GKR;
- direção visual pré-escolhida;
- identidade visual predefinida pelo GKR.

## 3. Evidência de entrada

O release foi concedido após emissão e validação do snapshot v5:

```text
ORIGIN MAIN FOR SNAPSHOT
→ aa1b524c20f6707d007208222ba8581af097c38d

SNAPSHOT BRANCH
→ delivery/design-handoff-v5

SNAPSHOT COMMIT
→ f2e8375258fda4f37aea27a5e5ec5e83f5c1a66d

SNAPSHOT TREE
→ 67bacb135166e7f3e85bfb4c52602ba89a515a1e

PACKAGE
→ 34 FILES
→ 26 CANONICAL SOURCES
→ 8 PER-HOME GUIDES

CANONICAL BLOB PRESERVATION
→ 26 / 26 EXACT MATCH
→ MISMATCHES = 0
```

O v5 permanece snapshot histórico congelado. O v6 também foi posteriormente emitido e congelado, mas uma revisão independente pós-emissão identificou contradição material no Operational Flow v3.0.1 preservado pelo snapshot. Portanto, o v6 não é válido para nova execução; a correção canônica ocorre em revisão posterior e exige nova emissão, nunca reescrita do snapshot.

## 4. Fonte de verdade para cada Home

A designer deve receber, para cada Home:

1. autoridades comuns vigentes;
2. Documento Mestre da Home;
3. autoridades específicas necessárias daquela Home;
4. guia de consumo / Source Lock da emissão vigente;
5. classificação explícita do que é verdade, liberdade criativa, candidato, placeholder, dado real necessário, questão aberta e inferência proibida.

As classes operacionais vigentes são:

- `CANONICAL`;
- `DESIGN_CREATIVE`;
- `CONTENT_CANDIDATE`;
- `DESIGN_HYPOTHESIS`;
- `PROTOTYPE_PLACEHOLDER`;
- `REAL_DATA_REQUIRED`;
- `OPEN_QUESTION`;
- `PROHIBITED_INFERENCE`.

## 5. Liberdade criativa protegida

O GKR não congela identidade visual prévia para as Homes.

Permanecem sob autoria da designer:

- tipografia;
- paleta;
- fotografia;
- ilustração;
- iconografia;
- composição;
- grid;
- ritmo;
- motion;
- aparência de componentes;
- linguagem gráfica;
- atmosfera;
- direção visual;
- soluções responsivas;
- copy/tom não congelados.

```text
GKR
→ SIGNIFICADO / FUNÇÃO / LIMITES / VERDADE / EVIDÊNCIA

DESIGNER
→ EXPRESSÃO VISUAL / CRIATIVA

AI
→ OPTIONAL ASSISTANT

DESIGN FREEDOM
≠ PRODUCT REDEFINITION
≠ FACTUAL INVENTION
```

## 6. Uso opcional de IA

Sistemas de IA podem ser usados pela designer para:

- explorar alternativas;
- organizar referências;
- gerar hipóteses;
- apoiar composição;
- apoiar conteúdo candidato;
- comparar soluções;
- acelerar tarefas criativas.

Toda IA deve consumir o mesmo Source Lock da Home e obedecer às mesmas fronteiras.

```text
AI OUTPUT
→ PROPOSAL / HYPOTHESIS

AI OUTPUT
≠ CANONICAL TRUTH
≠ APPROVED DESIGN
≠ EVIDENCE
```

O uso ou não uso de IA é decisão da designer.

## 7. Artefatos de Design produzidos pelo GKR

A frente documental não produz Design.

Qualquer exploração Figma criada durante tentativa operacional anterior é explicitamente:

```text
ABANDONED
→ NON-AUTHORITATIVE
→ NOT A DESIGN REFERENCE
→ NOT A SOURCE FOR THE DESIGNER
→ NOT APPROVED FOR IMPLEMENTATION
```

Nenhuma decisão visual deve ser derivada desse artefato.

## 8. Validação humana

A designer pode criar livremente dentro das fronteiras.

A revisão humana posterior deve verificar:

- fidelidade semântica;
- inexistência de redefinição de produto;
- ausência de claims não sustentados;
- autonomia do participante;
- distinções entre participantes/produtos;
- evidência/prova;
- acessibilidade e responsividade;
- consistência entre as oito Homes quando aplicável.

O GKR não exige uma etapa de protótipo gerativo prévia para que a designer comece.

## 9. Limites explícitos

Este release não autoriza automaticamente:

- Product Engineering;
- frontend/backend;
- publicação/deploy;
- nova arquitetura de produto;
- funcionalidade não governada;
- alteração de modelo econômico;
- Marketing/GTM;
- Research com participantes reais;
- claims não sustentados;
- promoção de `GKR-SURF-*`/`GKR-TRN-*`;
- `UXA-102/V5`;
- high-fidelity da experiência autenticada O/C por inferência.

```text
PUBLIC HOME O/C DESIGN RELEASE
≠ O/C AUTHENTICATED HIGH-FIDELITY AUTHORIZATION
```

## 10. Estado

```text
V5 SNAPSHOT
→ FROZEN / HISTORICAL DELIVERY SNAPSHOT

DESIGN PRODUCTION RELEASE
→ GRANTED

EXTERNAL DESIGNER PRODUCTION AUTHORIZATION
→ RELEASED

OPERATIONAL EXECUTION
→ REQUIRES SNAPSHOT DESIGNATED CURRENT / VALID
→ CURRENT PACKAGE STATUS GOVERNED BY GKR-UX-HOMES-DESIGN-DELIVERY-001 + GKR-STATE-001

MANUAL CREATIVE PRODUCTION
→ AUTHORIZED

AI-ASSISTED CREATIVE PRODUCTION
→ OPTIONAL / DESIGNER-CONTROLLED

GKR-CREATED FIGMA
→ NONE

PRIOR GKR FIGMA EXPLORATION
→ ABANDONED / NON-AUTHORITATIVE / NOT A DESIGN REFERENCE

FINAL DESIGN ACCEPTANCE
→ HUMAN / SEPARATE

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED

UXA-102 / V5
→ NOT_STARTED
```

## 11. Próximo movimento legítimo

A completude pré-emissão foi concluída historicamente, mas o snapshot v6 foi invalidado para nova execução por um P1 pós-emissão no Operational Flow v3.0.1.

O próximo movimento legítimo é:

```text
CANONICAL SOURCES
→ RECONCILED

CURRENT EXTERNAL SOURCE PACKAGE
→ GOVERNED BY GKR-UX-HOMES-DESIGN-DELIVERY-001 + GKR-STATE-001
→ THIS RELEASE DOES NOT FREEZE A TRANSITORY PACKAGE VALUE

NEXT GOVERNED ACT
→ FOLLOW CURRENT MANIFEST / STATE
→ MATERIALIZATION OF ANY NEW SNAPSHOT REQUIRES SEPARATE HUMAN AUTHORIZATION
```

A designer somente deve iniciar ou retomar execução operacional contra um snapshot que o Manifesto + Estado Atual designem explicitamente como corrente e válido.