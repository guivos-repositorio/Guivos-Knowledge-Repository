---
id: GKR-UX-HOMES-GENINPUT-001
title: Homes Públicas — Contrato de Consumo para Designer e IA Opcional
status: active
version: 3.0.0
owner: Experience Architecture
last_updated: 2026-09-20
normative: true
maturity: current_main_ai_optional
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-STATE-001
---

# Homes Públicas — Contrato de Consumo para Designer e IA Opcional

## 1. Regra superior

O `main` corrente é o Source Lock operacional.

```text
CURRENT MAIN
→ FIRST-CLASS SOURCE

SNAPSHOT / EXPORT
→ OPTIONAL DERIVED ARTIFACT

HISTORICAL DOCS
→ NOT OPERATIONAL INPUT

DESIGNER
→ MAY WORK MANUALLY

AI
→ OPTIONAL
```

As fontes exatas por Home são definidas pelo Manifesto Canônico de Fontes para Design.

## 2. Isolamento de contexto

Trabalhar uma Home por vez.

Carregar somente:

```text
COMMON AUTHORITIES
+
HOME MASTER
+
HOME-SPECIFIC SOURCES LISTED IN THE MANIFEST
```

Não misturar documentos de outra Home para completar lacunas.

## 3. Contrato de leitura

Antes de gerar ou desenhar:

1. identificar tese e pergunta-mãe;
2. compreender os movimentos e sua ordem;
3. separar participantes de produtos;
4. separar possibilidade de oportunidade;
5. identificar claims que exigem evidência real;
6. identificar perguntas ainda abertas;
7. preservar autonomia e autoridade humana.

## 4. Classificação mínima

Use:

- `CANONICAL`;
- `REAL_DATA_REQUIRED`;
- `CONTENT_CANDIDATE`;
- `DESIGN_HYPOTHESIS`;
- `PROTOTYPE_PLACEHOLDER`.

Nada que esteja em `CONTENT_CANDIDATE`, `DESIGN_HYPOTHESIS` ou `PROTOTYPE_PLACEHOLDER` se torna canônico por repetição.

## 5. Prompt-base opcional

```text
OBJETIVO
Crie ou critique uma proposta de Design para a Home indicada.

FONTES
Use exclusivamente as autoridades correntes fornecidas pelo Manifesto.

PRESERVE
- tese;
- pergunta-mãe;
- ordem dos movimentos;
- fronteiras funcionais;
- autoridade;
- evidência;
- autonomia;
- distinções semânticas do GKR.

LIBERDADE
A solução visual é livre. Não reproduza estrutura documental mecanicamente.

NÃO INVENTE
Preço, disponibilidade, parceiro, métrica, case, depoimento, cobertura,
capacidade, regra ou claim não sustentado pelas fontes.

ROTULE
Conteúdo provisório e hipóteses de Design explicitamente.
```

## 6. Saída esperada

Uma proposta pode incluir estrutura, composição, wireframe, UI, microinterações, conteúdo candidato e protótipo, desde que mantenha rastreabilidade para as fontes e não crie nova autoridade.

```text
AI EXECUTION
→ OPTIONAL

DESIGN AUTHORITY
→ HUMAN

CURRENT SOURCE LOCK
→ CURRENT MAIN + MANIFEST
```
