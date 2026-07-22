---
id: GKR-GOV-OUT-001
title: Outcome Governance Method
status: draft
version: 0.3.0
owner: Guivos Knowledge Repository
last_updated: 2026-07-22
applies_to:
  - BA-STR-002
related:
  - BA-STR-002-COR-001
  - BA-STR-002-EOVP-001
---

# Outcome Governance Method

## Objetivo

Definir o processo pelo qual Candidate Outcomes são descobertos, registrados, validados, avaliados e consolidados antes de integrarem a Canon da Guivos.

Este método pertence ao Governance Framework do GKR. Ele não integra a Business Architecture nem antecipa a Governance Architecture da GEA.

## Princípio de responsabilidade

A Guivos não controla a transformação de Pessoas, Organizações ou Coletivos.

Ela projeta, opera e evolui um ecossistema que amplia as condições para que seus participantes realizem sua própria transformação.

Consequentemente, um Ecosystem Outcome deve descrever uma condição permanente do ecossistema que aumente a probabilidade de transformação positiva, sem atribuir à Guivos controle sobre decisões ou resultados individuais.

## Definição operacional

Um Ecosystem Outcome candidato é uma condição desejada, permanente e observável do ecossistema, suficientemente relevante para orientar decisões estratégicas e independente de produtos, tecnologias ou jornadas específicas.

## Fluxo de governança

```mermaid
graph LR
    D[Discovery] --> COR[Candidate Outcome Register]
    COR --> EV[External Validation]
    EV --> COEM[Candidate Outcome Evaluation Matrix]
    COEM --> AO[Approved Outcomes]
    AO --> C[Canon]
```

## 1. Discovery

A fase de Discovery identifica estados desejados possíveis sem aprovação, priorização ou consolidação.

O objetivo é ampliar cobertura e reduzir o risco de omissão prematura.

### Regras

- registrar hipóteses sem tratá-las como Canon;
- evitar organização por produto, departamento ou tecnologia;
- descrever condições do ecossistema, não funcionalidades;
- não criar novas camadas arquiteturais durante o levantamento;
- interromper refinamentos conceituais que não sejam dependências reais do BA-STR-002.

## 2. Candidate Outcome Register — COR

O COR é o inventário oficial de Candidate Outcomes.

### Campos mínimos

| Campo | Descrição |
|---|---|
| Código | Identificador provisório |
| Nome provisório | Formulação curta |
| Definição provisória | Condição desejada do ecossistema |
| Origem | Foundation, GEB, necessidade estratégica ou validação externa |
| Participantes afetados | Pessoa, Organização e/ou Coletivo |
| Status | Estado no ciclo de avaliação |
| Observações | Dúvidas, sobreposições e dependências |

### Status permitidos

| Status | Significado |
|---|---|
| Candidate | Registrado e ainda não avaliado |
| Under Validation | Em validação interna ou externa |
| Approved | Aprovado para consolidação |
| Rejected | Não atende aos critérios |
| Merged | Incorporado a outro Outcome |
| Deferred | Adiado sem bloqueio da arquitetura |

## 3. External Validation

A validação externa compara grupos de candidatos com o melhor conhecimento disponível aplicável ao problema.

### Objetivo

- verificar omissões relevantes;
- confirmar ou ampliar candidatos;
- identificar conceitos já consolidados em referências externas;
- evitar criação desnecessária de conceitos proprietários.

### Regras

- consultar somente fontes com impacto direto na decisão arquitetural;
- não transformar pesquisa externa em investigação filosófica;
- não copiar estruturas sem avaliar aderência à Guivos;
- registrar confirmação, ampliação, contradição ou ausência de evidência.

### Protocolo de execução

O [External Outcome Validation Protocol](../business-architecture/strategy/external-outcome-validation-protocol.md) aplica estas regras ao primeiro COR. Ele define cobertura, perguntas, critérios de fonte, direção da evidência, tratamento de omissões, testes dos clusters e gate de saída.

A existência do protocolo não equivale à validação. Candidatos somente passam a `Under Validation` individualmente após autorização de execução e registro da primeira evidência qualificada.

## 4. Candidate Outcome Evaluation Matrix — COEM

A COEM avalia cada candidato por critérios repetíveis.

### Testes obrigatórios

| Teste | Pergunta |
|---|---|
| Essential Test | Sem essa condição, o propósito da Guivos continua alcançável de forma sustentável? |
| Decision Test | Se essa condição piorar continuamente, a estratégia deverá ser revista? |
| Replacement Test | O candidato continua válido se todos os produtos e tecnologias atuais forem substituídos? |
| Outcome Quality Test | O candidato atende ao padrão de qualidade de Outcome? |

### Resultado possível

- Approve;
- Reject;
- Merge;
- Defer;
- Reformulate.

## 5. Outcome Quality Standard — AQS-O01

O AQS-O01 permanece em validação prática até ser aplicado aos primeiros candidatos.

Todo Outcome aprovado deverá ser:

| Critério | Exigência |
|---|---|
| Permanente | Mantém validade de longo prazo |
| Orientado ao propósito | Deriva da Foundation Architecture |
| Ecossistêmico | Descreve condição do ecossistema, não da plataforma |
| Independente | Não depende de produto, tecnologia, processo ou organograma |
| Decisório | Orienta estratégia, investimento ou desenho de capacidades |
| Observável | Pode produzir evidências por diferentes indicadores |
| Rastreável | Conecta-se a Business Outcomes, Capabilities, Produtos e KPIs |
| Não redundante | Não duplica outro Outcome aprovado |

## 6. Padrão de redação

Cada Outcome consolidado deverá possuir:

| Campo | Regra |
|---|---|
| Código | Identificador único |
| Nome | Conceito curto, permanente e não operacional |
| Definição canônica | Condição desejada do ecossistema |
| Justificativa | Razão de existência |
| Rastreabilidade | Relação com Foundation e Business Outcomes |
| Evidências possíveis | Formas futuras de observação |
| Produtos contribuintes | Produtos que materializam capacidades relacionadas |

### Regras linguísticas

- usar o ecossistema como sujeito quando isso aumentar a precisão;
- descrever um estado, não uma atividade;
- evitar produtos, canais, tecnologias e metas;
- manter uma ideia principal por Outcome;
- preferir formulação afirmativa;
- não utilizar substantivo isolado como definição do Outcome.

## 7. Limites metodológicos

- O Catálogo de Outcomes não deve ser substituído por um ciclo de jornada do participante.
- Taxonomias de fenômenos do ecossistema podem evoluir futuramente, mas não bloqueiam o BA-STR-002.
- Dimensões, propriedades emergentes e novas camadas permanecem fora da Canon enquanto não forem dependências comprovadas.
- Nenhum refinamento conceitual deve bloquear a evolução da arquitetura quando os ativos atuais já forem suficientes para decisões corretas.

## Regra permanente do GKR

> Nenhum conceito canônico nasce diretamente na Canon. Todo conceito percorre um processo explícito de descoberta, registro, validação, avaliação, aprovação e consolidação.

## Próximo passo

Executar o `BA-STR-002-EOVP-001` somente após aprovação separada. A validação externa e a COEM ocorrerão em ciclos próprios antes da definição de qualquer código canônico `EO-###` ou `BO-###`.
