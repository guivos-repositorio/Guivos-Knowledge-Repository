---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 2.1.0
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
  - GKR-UX-HOMES-DESIGN-SOURCE-READINESS-AUDIT-001
normative: false
maturity: designer_first_ai_optional_source_hardening_in_progress
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este fluxo governa como o pacote documental das Homes deve ser preparado e consumido por uma designer humana, com sistemas de AI como apoio opcional.

O GKR não cria arquivos Figma, não produz direção visual e não exige uma etapa de Figma Make.

## 2. Estado de início

O Design Production Release foi concedido anteriormente, mas o início operacional da designer está deliberadamente postergado até o fechamento de `GKR-UX-HOMES-DESIGN-SOURCE-READINESS-AUDIT-001`.

```text
DESIGN PRODUCTION RELEASE
→ GRANTED

SOURCE READINESS AUDIT
→ IN_PROGRESS

EXTERNAL DESIGNER START
→ DEFERRED UNTIL PASS

GKR / CHATGPT FIGMA EXECUTION
→ NOT TO BE PERFORMED
```

## 3. Isolamento de contexto

Trabalhar uma Home por vez.

A unidade mínima de consumo é:

```text
PACOTE COMUM
+
LEIA-PRIMEIRO / SOURCE LOCK DA HOME
+
DOCUMENTO MESTRE
+
FONTES ESPECÍFICAS NECESSÁRIAS
```

Não carregar indiscriminadamente documentos específicos das oito Homes na mesma execução humana ou de AI.

## 4. Fase A — preparação documental

Antes de liberar uma Home para Design:

1. validar o Documento Mestre vigente;
2. validar as fontes complementares realmente necessárias;
3. confirmar IDs, versões, paths e checkpoint;
4. classificar `CANONICAL`, `DESIGN_CREATIVE`, `CONTENT_CANDIDATE`, `DESIGN_HYPOTHESIS`, `PROTOTYPE_PLACEHOLDER`, `REAL_DATA_REQUIRED`, `OPEN_QUESTION` e `PROHIBITED_INFERENCE`;
5. confirmar que nenhuma leitura histórica é necessária para reconstruir a verdade atual;
6. confirmar que questões abertas possuem destino explícito;
7. confirmar que a liberdade visual está explícita e não confundida com lacuna.

## 5. Fase B — leitura e compreensão da designer

A designer deve receber material suficiente para compreender, sem conversa obrigatória adicional:

- papel da Home;
- público/perspectiva predominante;
- tese/pergunta-mãe;
- narrativa e funções que precisam sobreviver;
- relações com participantes, produtos e outras Homes;
- fatos e estados que exigem fonte real;
- limites de claims, causalidade, privacidade e personalização;
- o que pode ser criado livremente;
- o que está aberto;
- o que não pode ser inferido.

A designer pode consultar `guivos.com 2.0` e outras referências visuais, mas nenhuma referência externa substitui o GKR.

## 6. Fase C — criação manual de Design

A criação visual é responsabilidade da designer.

```text
DESIGNER
→ FIGMA / FERRAMENTAS DE SUA ESCOLHA
→ EXPRESSÃO VISUAL E CRIATIVA

GKR
→ NÃO DEFINE LAYOUT
→ NÃO DEFINE IDENTIDADE VISUAL
→ NÃO PRODUZ ARTEFATO FIGMA
```

A designer pode criar ou evoluir:

- tipografia;
- paleta;
- imagem/fotografia/ilustração;
- composição;
- grid;
- iconografia;
- motion;
- componentes;
- atmosfera;
- ritmo;
- comportamento responsivo;
- microcopy não congelada.

## 7. Fase D — apoio opcional de sistemas de AI

Sistemas de AI podem ser usados a critério da designer ou da Guivos para:

- ideação;
- alternativas de copy;
- exploração de hierarquia;
- síntese do Source Lock;
- geração de imagem conceitual;
- comparação de hipóteses;
- autoauditoria textual.

Eles não são gate obrigatório e não recebem autoridade para preencher lacunas factuais ou arquiteturais.

```text
AI OUTPUT
→ CANDIDATE / HYPOTHESIS / PLACEHOLDER AS APPLICABLE
→ NEVER CANONICAL BY GENERATION ALONE
```

## 8. Fase E — revisão humana durante o serviço

A Guivos deve revisar quando necessário:

- fidelidade semântica;
- clareza;
- coerência da família Guivos;
- originalidade;
- responsividade;
- acessibilidade;
- conteúdo candidato;
- placeholders;
- claims e dados;
- hipóteses introduzidas.

A revisão não transforma o GKR em diretor artístico. Ela verifica aderência aos contratos e decide o aceite do serviço.

## 9. Fase F — entrega e aceite final

O aceite final deve registrar, no mínimo:

- Homes entregues;
- arquivo(s) e versão avaliada;
- responsável humano pelo aceite;
- checklist de produção concluído;
- assets/fontes/plugins/licenças entregues ou documentados;
- pendências inexistentes ou classificadas;
- controle/acesso da Guivos aos arquivos essenciais;
- confirmação de que nenhum finding material de significado permanece;
- status final de aceite.

A conclusão operacional do serviço de Design deve ocorrer depois desse aceite conforme o instrumento contratual aplicável.

## 10. Regra de mudança durante Design

Se uma decisão semântica mudar depois da emissão do Source Lock:

1. interromper apenas a Home afetada quando necessário;
2. reconciliar o GKR;
3. classificar o impacto;
4. reemitir o Source Lock/pacote quando material.

Melhorias puramente criativas não exigem atualização do GKR.

## 11. Relação com snapshots

```text
V5
→ FROZEN / HISTORICAL FOR NEW START

V6
→ NOT_EMITTED
→ TARGET AFTER FINAL SOURCE READINESS PASS
```

## 12. Estado

```text
FLOW
→ v2.1.0

MODEL
→ DESIGNER-FIRST
→ AI-OPTIONAL
→ GKR-SOURCE-BOUND

SOURCE READINESS
→ IN_PROGRESS

EXTERNAL DESIGNER START
→ DEFERRED UNTIL PASS

GKR FIGMA EXECUTION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED
```
