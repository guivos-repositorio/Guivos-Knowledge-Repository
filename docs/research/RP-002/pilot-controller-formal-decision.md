---
id: RP-002-PILOT-CTRL-DEC-001
title: Piloto — Decisão Formal de Controlador do RP-002
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_decision_approved
related:
  - RP-002-PILOT-PRIV-001
  - RP-002-PILOT-OP-001
  - RP-002-PMF-001
---

# Piloto — Decisão Formal de Controlador do RP-002

## 1. Finalidade

Este documento registra a decisão operacional autorizada para o `RP-002` sobre quem exercerá o papel de **controlador do tratamento de dados pessoais** no escopo do Dry Run Real e do piloto de validação humana associado.

Ele fecha especificamente o blocker:

```text
P1B — CONTROLADOR DO PILOTO FORMALMENTE DESIGNADO
```

Este documento não fecha, por si só:

- canal de privacidade;
- processo de atendimento de direitos;
- base legal;
- aviso de privacidade;
- aplicabilidade/designação de encarregado;
- operadores e ferramentas;
- permissões;
- Safety Gate;
- liberação de `Participant 001`.

## 2. Decisão

Fica formalmente designada, para o escopo operacional definido neste documento:

```text
CONTROLADOR DO PILOTO
→ GUIVOS LTDA

CNPJ
→ 43.530.598/0001-33

ESCOPO
→ Dry Run Real e piloto RP-002

VIGÊNCIA
→ 27/08/2026

RESPONSABILIDADE OPERACIONAL INTERNA
→ Guivos Research / Pilot Owner do RP-002

ESTADO
→ APPROVED
```

A designação é restrita ao tratamento de dados realizado no contexto do `RP-002` e não pretende, por si só, classificar todas as demais operações de tratamento existentes no ecossistema Guivos.

## 3. Base da decisão

A decisão combina dois elementos distintos:

### 3.1 Evidência institucional pública

O site oficial da Guivos apresenta publicamente:

```text
Guivos Ltda ®
CNPJ: 43.530.598/0001-33
```

Fonte verificada em 27/08/2026:

<https://www.guivos.com/>

Essa evidência identifica a entidade jurídica pública utilizada pela Guivos.

### 3.2 Decisão operacional autorizada

A identidade pública, isoladamente, não era suficiente para fechar o gate de controlador.

O blocker somente é promovido neste registro porque houve autorização expressa para que **Guivos Ltda assuma formalmente o papel de controlador do piloto RP-002**.

Portanto:

```text
IDENTIDADE PÚBLICA
+
DECISÃO OPERACIONAL AUTORIZADA
=
CONTROLADOR FORMAL DO RP-002
```

## 4. Papel decisório assumido

No escopo do piloto, Guivos Ltda assume responsabilidade pelas principais decisões sobre o tratamento, incluindo a definição e aprovação de:

- finalidades do tratamento;
- categorias de dados necessárias;
- critérios de minimização;
- arquitetura `Identity Vault × Research Base`;
- ferramentas e operadores autorizados;
- regras de acesso;
- retenção e exclusão;
- correção e limitação quando cabíveis;
- follow-ups;
- benchmark;
- uso de IA quando autorizado;
- tratamento de incidentes;
- atendimento de solicitações dos titulares;
- encerramento do ciclo de pesquisa.

A execução operacional pode ser delegada a operadores ou funções internas, mas a delegação não transfere automaticamente o papel de controlador.

## 5. Responsabilidade operacional interna

Para fins de governança do piloto, a função responsável pela implementação desta decisão é:

```text
GUIVOS RESEARCH
→ PILOT OWNER DO RP-002
```

Essa função deve garantir que as decisões documentadas correspondam à prática real antes da entrada de qualquer participante.

A atribuição de tarefas específicas a Interviewer, Data Steward, Supply Researcher, Supply Verifier, Benchmark Operator, Analyst ou outros papéis continua subordinada ao `RP-002-PILOT-OP-001`.

## 6. Relação com a definição da ANPD

A decisão segue a compreensão operacional registrada em `RP-002-PILOT-PRIV-001`: controlador é o agente que toma as principais decisões relativas ao tratamento de dados pessoais.

Referência oficial:

<https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1>

Este registro é uma decisão interna de governança do piloto e não substitui avaliação jurídica sobre outras obrigações específicas aplicáveis.

## 7. Atualização do gate P1

Com esta decisão, o estado vigente passa a ser:

```text
P1A — IDENTIDADE INSTITUCIONAL PÚBLICA
→ PASS

P1B — CONTROLADOR DO PILOTO FORMALMENTE DESIGNADO
→ PASS
```

Para `P1B`, este documento **prevalece sobre o estado anterior `HOLD` registrado em `RP-002-PILOT-PRIV-001`**, que permanece preservado como checkpoint anterior à decisão.

Nenhum outro gate daquele documento é promovido automaticamente.

## 8. O que permanece em HOLD

Estado imediatamente após esta decisão:

```text
P1A — IDENTIDADE INSTITUCIONAL
→ PASS

P1B — CONTROLADOR FORMAL DO PILOTO
→ PASS

P2A — CONTEÚDO DA POLÍTICA / AVISO APLICÁVEL
→ A VALIDAR

P2B — CANAL OFICIAL DE PRIVACIDADE
→ HOLD

P2C — PROCESSO DE DIREITOS TESTADO NO CANAL REAL
→ HOLD

P3 — FINALIDADES / CATEGORIAS
→ PENDING FINALIZATION

P4 — BASE LEGAL
→ HOLD

ENCARREGADO / DPO
→ APPLICABILITY REVIEW REQUIRED

OPERADORES / FERRAMENTAS
→ HOLD

PERMISSÕES REAIS
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

## 9. Canal de privacidade não foi inferido

A auditoria pública não encontrou um canal explicitamente designado para privacidade/direitos do titular.

Por isso, esta decisão **não converte** automaticamente nenhum dos seguintes meios em canal de privacidade:

- e-mail institucional genérico;
- e-mail comercial;
- suporte;
- WhatsApp;
- formulário de contato;
- telefone;
- canal de vendas.

Regra preservada:

> **canal existente ≠ canal de privacidade designado.**

Também não será criado no GKR um endereço hipotético como `privacidade@...` sem que esse canal exista e possa realmente receber solicitações.

## 10. Consequência operacional

A promoção de `P1B` para `PASS` reduz um blocker, mas não libera o piloto.

A sequência legítima passa a ser:

```text
CONTROLADOR FORMAL
→ PASS
↓
CANAL OFICIAL DE PRIVACIDADE
→ DEFINIR / MATERIALIZAR
↓
PROCESSO DE DIREITOS
→ CONFIGURAR / TESTAR
↓
POLÍTICA / AVISO DO PILOTO
→ VALIDAR
↓
BASE LEGAL
→ DOCUMENTAR / REVISAR
↓
OPERADORES + PERMISSÕES + PAPÉIS
→ CONFIGURAR
↓
FINAL RELEASE GATE
↓
PARTICIPANT 001
```

## 11. Regra de autoridade

Para o estado de `P1B`, a autoridade temporal é:

```text
RP-002-PILOT-PRIV-001
→ checkpoint pré-decisão

RP-002-PILOT-CTRL-DEC-001
→ decisão vigente
```

Em caso de conflito exclusivamente sobre a designação do controlador do piloto, prevalece este documento.

Os demais blockers continuam governados pelo `RP-002-PILOT-PRIV-001` e pelo `RP-002-PILOT-OP-001`.

## 12. Limites

Esta decisão:

- não constitui parecer jurídico;
- não declara conformidade LGPD completa;
- não define base legal;
- não designa encarregado por inferência;
- não cria canal de privacidade fictício;
- não autoriza coleta de dados reais;
- não libera `Participant 001`;
- não transforma Research em Canon;
- não altera a arquitetura conceitual do RP-002.

## 13. Estado final deste passo

```text
CONTROLADOR DO RP-002
→ GUIVOS LTDA
→ CNPJ 43.530.598/0001-33
→ FORMALLY DESIGNATED

P1B
→ PASS

P2B — PRIVACY CHANNEL
→ HOLD

PARTICIPANT 001
→ HOLD

PMF
→ NOT VALIDATED
```

O próximo blocker material é a existência de um **canal oficial, real, monitorado e testável de privacidade/direitos do titular**.