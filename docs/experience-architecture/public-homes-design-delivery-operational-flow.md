---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 3.0.3
owner: Experience Architecture
last_updated: 2026-09-19
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
normative: false
maturity: designer_first_ai_optional_current_package_delegated
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este fluxo governa **como a designer consome as fontes do GKR** antes e durante a criação das oito Homes.

Ele não prescreve ferramenta criativa específica e não exige IA, geração automática, wireframe prévio ou direção visual pré-selecionada.

```text
SOURCE OF TRUTH
→ GKR

CREATIVE AUTHOR
→ DESIGNER

AI
→ OPTIONAL

DESIGN TOOL
→ DESIGNER CHOICE
```

## 2. Gate de início

A produção criativa só deve começar quando:

- o pacote vigente estiver materializado;
- o guia de consumo da Home estiver presente;
- as fontes específicas estiverem completas;
- não houver finding material aberto de completude;
- o Design Production Release estiver vigente.

A reauditoria C1–C15 foi concluída para a emissão v6. Uma revisão independente pós-emissão identificou posteriormente um P1 neste próprio fluxo v3.0.1: o snapshot v6 congelado preservou linguagem pré-emissão contraditória. A autoridade canônica foi corrigida nesta revisão v3.0.2; o snapshot v6 não é reescrito e não permanece válido para nova execução. Uma nova emissão/revalidação é necessária antes de iniciar trabalho criativo com um pacote externo corrente.

## 3. Isolamento de contexto

Trabalhar uma Home por vez.

Para cada Home, carregar apenas:

```text
COMMON AUTHORITIES
+
HOME READ-FIRST / SOURCE LOCK
+
HOME MASTER
+
HOME-SPECIFIC AUTHORITIES
```

Não misturar documentos específicos de Homes diferentes por conveniência.

## 4. Fase A — compreensão humana obrigatória

A designer deve compreender primeiro:

1. papel da Home;
2. tese;
3. pergunta-mãe;
4. narrativa;
5. regiões/movimentos;
6. Header, navegação, launcher e CTAs quando aplicáveis;
7. estados e comportamentos relevantes;
8. participantes e produtos;
9. prova/evidência;
10. dados reais necessários;
11. questões abertas;
12. inferências proibidas;
13. limites de produto;
14. liberdade criativa.

A designer não precisa reconstruir histórico de PRs, auditorias ou conversas para entender o estado vigente.

## 5. Fase B — criação da designer

A criação é externa ao GKR.

A designer possui liberdade para decidir:

- processo;
- sketches;
- referências;
- ferramenta;
- ordem de exploração;
- tipografia;
- cor;
- imagem;
- composição;
- grid;
- motion;
- iconografia;
- componentes;
- atmosfera;
- comportamento responsivo;
- alternativas de direção visual.

```text
DESIGNER
→ MAY CREATE MANUALLY

DESIGNER
→ MAY USE AI

AI USE
→ OPTIONAL
→ NOT A GATE
→ NOT A REQUIREMENT
```

O GKR não cria uma alternativa visual para ser seguida.

## 6. Fase C — uso opcional de IA

Quando a designer optar por IA:

1. usar o guia tool-neutral da Home;
2. carregar somente as fontes autorizadas;
3. preservar `CANONICAL`;
4. tratar liberdade visual como `DESIGN_CREATIVE`;
5. tratar copy ainda não congelada como `CONTENT_CANDIDATE`;
6. tratar propostas de layout/estética como `DESIGN_HYPOTHESIS`;
7. usar `PROTOTYPE_PLACEHOLDER` apenas quando explicitamente provisório;
8. não inventar `REAL_DATA_REQUIRED`;
9. preservar `OPEN_QUESTION`;
10. nunca ultrapassar `PROHIBITED_INFERENCE`.

A saída de IA não cria autoridade.

## 7. Fase D — autoauditoria da designer

Antes de apresentar uma Home para revisão:

- conferir aderência ao Master;
- conferir que nenhuma decisão visual redefiniu produto;
- conferir que não há dado inventado;
- conferir que claims têm suporte;
- conferir responsividade;
- conferir acessibilidade;
- conferir fallback/reduced motion quando aplicável;
- conferir Header/CTA/navegação;
- conferir distinção participante × produto;
- conferir estados/fallbacks quando aplicáveis;
- conferir questões abertas;
- registrar placeholders ainda existentes.

## 8. Fase E — revisão humana

A Guivos revisa o resultado contra as fontes vigentes.

A revisão humana avalia significado e aderência, não substitui autoria criativa da designer.

Resultados possíveis:

```text
APPROVED
→ direction accepted

ADJUST
→ targeted changes required

REJECT
→ semantic/functional/creative direction must be revisited
```

A aprovação pode ocorrer sobre Design produzido manualmente, com IA ou por combinação dos dois.

## 9. Fase F — entrega final de Design

A designer é responsável por produzir e organizar os artefatos finais de Design nas ferramentas definidas pela própria execução contratual. O GKR não determina, cria, edita nem governa arquivos de Design e não exige ferramenta específica, etapa intermediária gerativa ou materialização visual pelo repositório.

A entrega deve preservar:

- arquivos editáveis;
- assets;
- fontes/licenças;
- componentes necessários;
- estados relevantes;
- desktop/mobile quando aplicável;
- documentação suficiente para continuidade;
- controle/acesso da Guivos aos ativos contratados.

```text
FINAL DESIGN ACCEPTED
≠ IMPLEMENTATION RELEASE
```

## 10. Mudança semântica durante o Design

Se uma autoridade do GKR mudar materialmente:

```text
AFFECTED HOME
→ STOP SEMANTIC DEPENDENT WORK
→ RECONCILE SOURCE PACKAGE
→ REISSUE IF MATERIAL
```

Mudanças puramente criativas da designer, sem alteração de contrato, não exigem mudança no GKR.

## 11. Estado

```text
FLOW v3.0.2
→ DESIGNER-FIRST
→ AI-OPTIONAL
→ TOOL-NEUTRAL

GKR-CREATED FIGMA
→ NONE

PRIOR GKR FIGMA EXPLORATION
→ ABANDONED / NON-AUTHORITATIVE / NOT A DESIGN REFERENCE

SOURCE COMPLETENESS AUDIT
→ PRE-EMISSION C1–C15 PASS / CLOSED
→ POST-EMISSION PACKAGE CONSISTENCY P1 ADJUDICATED

HISTORICAL INVALID SNAPSHOTS
→ V6 / V7 REMAIN IMMUTABLE PROVENANCE WHEN SO CLASSIFIED BY MANIFEST / STATE

CURRENT EXTERNAL SOURCE PACKAGE
→ GOVERNED BY GKR-UX-HOMES-DESIGN-DELIVERY-001 + GKR-STATE-001
→ THIS FLOW DOES NOT FREEZE A TRANSITORY PACKAGE VALUE

DESIGN PRODUCTION RELEASE
→ GRANTED
→ EXECUTION REQUIRES A SNAPSHOT DESIGNATED CURRENT / VALID

PRODUCT ENGINEERING
→ NOT RELEASED
```