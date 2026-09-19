---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 3.0.0
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
normative: false
maturity: v6_manual_designer_ai_assisted_flow_candidate
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este fluxo governa como a **designer humana** consome o pacote documental das oito Homes e produz a solução visual com liberdade criativa.

Figma é ferramenta da designer. Sistemas de IA são apoio opcional. O GKR não cria nem governa diretamente o arquivo oficial de Design.

## 2. Gate de início

`DESIGN PRODUCTION RELEASE` permanece concedido, mas a execução externa fica em `HOLD` até a emissão e validação do snapshot v6.

## 3. Isolamento de contexto

Trabalhar uma Home por vez.

```text
00-COMUM
+
00-LEIA-PRIMEIRO DA HOME
+
FONTES ESPECÍFICAS DA HOME
```

## 4. Fase A — compreensão humana obrigatória

A designer deve ler o guia, as autoridades comuns e as fontes específicas; distinguir as oito classes operacionais; e registrar dúvidas materiais antes de transformar ausência documental em solução visual.

## 5. Fase B — apoio opcional de IA

IA pode apoiar síntese, comparação de fontes, ideação, alternativas, Content Design candidato, referências/assets candidatos e autoauditoria.

IA não é etapa obrigatória e não recebe autoridade para definir produto, preencher lacuna factual, promover hipótese, aprovar direção ou tornar seu output o arquivo oficial.

## 6. Fase C — exploração de Design pela designer

A designer cria e organiza manualmente ou cura conscientemente a solução em suas ferramentas de trabalho.

Ela pode usar IA, plugins e recursos criativos de sua escolha, desde que preserve contratos, identifique placeholders, não apresente ficção como realidade e mantenha acessibilidade e responsividade.

Output: `DESIGN EXPLORATION / HUMAN-CURATED / NON-CANONICAL`.

## 7. Fase D — revisão humana de direção

Revisar fidelidade semântica, clareza, criatividade, hierarquia, conteúdo candidato, desktop/mobile, acessibilidade, estados, dados/provas e hipóteses introduzidas.

Sem aprovação humana da direção, não iniciar finalização contratual.

## 8. Fase E — finalização pela designer

A direção aprovada é refinada pela designer no Figma ou ferramenta contratada.

Tipografia, cores, estilos, componentes, assets, estados, comportamento responsivo e motion necessários à consistência são documentados como consequência do Design, não como baseline estética pré-imposta pelo GKR.

## 9. Fase F — aceite final

O aceite humano verifica o checklist de `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001`.

```text
FINAL DESIGN ACCEPTED
≠ IMPLEMENTATION
≠ PRODUCT ENGINEERING RELEASE
```

## 10. Regra de mudança

Mudança semântica material após o snapshot interrompe a Home afetada até reconciliação documental. Refinamento puramente criativo permanece sob autonomia da designer.

## 11. Estado

```text
FLOW v3.0.0
→ CANDIDATE FOR V6

PRIMARY EXECUTOR
→ HUMAN DESIGNER

AI
→ OPTIONAL ASSISTANCE

OFFICIAL FIGMA
→ DESIGNER-CREATED / DESIGNER-CURATED

DIRECT GKR/AI FIGMA MATERIALIZATION
→ OUT_OF_SCOPE
```
