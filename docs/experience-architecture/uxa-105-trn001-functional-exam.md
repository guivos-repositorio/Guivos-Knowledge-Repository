---
id: GKR-UXA-105-TRN001-FUNCTIONAL-EXAM-001
title: UXA-105 — TRN-001 — Exame Funcional da Continuidade Home Pública → Entrada Protegida
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: adjudicated_functional_contract
depends_on:
  - GKR-UXA-105-TRN001-SCOPE-EXAM-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-PER002-MASTER-001
  - UXA-020
  - UXA-023
  - UXA-035
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - GKR-UX-PER002-PROTOTYPE-REVALIDATION-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
---

# UXA-105 — TRN-001 — Exame Funcional da Continuidade Home Pública → Entrada Protegida

## 1. Finalidade

Este documento executa o exame funcional autorizado da UXA-105 exclusivamente sobre:

```text
TRN-001
→ PER-001 — HOME PÚBLICA
→ PER-002 — ENTRADA PROTEGIDA
```

O exame funcional foi adjudicado como contrato normativo. A adjudicação não promove maturidade e não transforma validação documental em implementação.

## 2. Autoridades examinadas

O exame considera em conjunto:

- `GKR-UX-HOME-MASTER-001`;
- `GKR-UX-PER002-MASTER-001`;
- `UXA-020`;
- `UXA-023`;
- `UXA-035`;
- `GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001`;
- Transition Registry e Gaps correntes;
- escopo normativo da própria UXA-105.

## 3. Origem — PER-001 / Home pública

A origem funcional está suficientemente definida:

- a Home é pública e institucional;
- explorar a Home não exige personalização;
- `Iniciar Jornada` é porta própria e persistente;
- iniciar é decisão voluntária;
- a Home não diagnostica a Pessoa;
- a Home não pede relato pessoal como condição para explicar a Guivos;
- a Home não autoriza processamento material;
- Login de relação existente é rota distinta de retomada.

Resultado:

```text
ORIGIN / PER-001
→ FUNCTIONALLY SUFFICIENT CANDIDATE
```

## 4. Destino — PER-002 / Entrada Protegida

O destino funcional está suficientemente definido:

- `PER-002` é a primeira responsabilidade protegida após a Home;
- deve explicar onde a Pessoa está entrando e por quê;
- autenticação é gate/estado interno quando necessária;
- autenticação não equivale a autorização material;
- a Pessoa pode voltar, interromper ou não prosseguir;
- nenhum relato material deve ser presumido;
- `PER-002` não é captura do Momento Atual;
- `TRN-002` permanece separada e localmente validada.

Resultado:

```text
DESTINATION / PER-002
→ FUNCTIONALLY SUFFICIENT CANDIDATE
```

## 5. Gatilho consciente e mudança de contexto

O gatilho legítimo é a escolha consciente da Pessoa de iniciar a Journey a partir da Home.

```text
EXPLORAR HOME
≠ INICIAR JOURNEY

VER CTA / LINK
≠ ACIONAR TRANSIÇÃO

INICIAR JOURNEY
→ AÇÃO CONSCIENTE
→ MUDANÇA DE CONTEXTO
→ PÚBLICO → PROTEGIDO
```

A mudança de contexto não pode ser tratada como:

- consentimento genérico;
- autorização de processamento;
- autorização de personalização;
- fornecimento de relato;
- conclusão de autenticação;
- conclusão de `PER-002`.

Resultado: **FECHADO FUNCIONALMENTE / CANDIDATO**.

## 6. Informação mínima antes e depois do handoff

Antes da mudança, a Home deve permitir compreender que iniciar a Journey leva a um ambiente protegido distinto da navegação pública.

Ao entrar em `PER-002`, a Pessoa deve receber a explicação detalhada de proteção, finalidade, alternativas e controles antes de qualquer captura material downstream.

Não é necessário deslocar para a Home todo o contrato de `PER-002`.

```text
HOME
→ SINALIZA A MUDANÇA DE CONTEXTO

PER-002
→ EXPLICA O CONTEXTO PROTEGIDO EM DETALHE

SINALIZAÇÃO
≠ CONSENTIMENTO
≠ AUTORIZAÇÃO MATERIAL
```

Resultado: **FECHADO FUNCIONALMENTE / CANDIDATO**.

## 7. Primeira entrada × retomada

A arquitetura corrente permite distinguir:

```text
INICIAR JORNADA
→ PRIMEIRA ENTRADA / ENTRADA CONSCIENTE NA JOURNEY

LOGIN
→ RETOMADA DE RELAÇÃO EXISTENTE
```

Login não deve forçar onboarding de primeira entrada. Iniciar Journey não deve presumir sessão prévia nem transformar autenticação em autorização material.

Resultado: **FECHADO FUNCIONALMENTE / CANDIDATO**.

## 8. Retorno, interrupção e não prosseguimento

A continuidade deve preservar:

- retorno à Home;
- interrupção sem penalidade semântica;
- não prosseguimento como escolha legítima;
- ausência de personalização material por mera entrada;
- ausência de inferência de recusa global da Guivos.

```text
VOLTAR
≠ FALHA

INTERROMPER
≠ RECUSAR A GUIVOS

NÃO PROSSEGUIR
≠ AUTORIZAR QUALQUER EFEITO
```

Resultado: **FECHADO FUNCIONALMENTE / CANDIDATO**.

## 9. Falha, indisponibilidade e estado indeterminado

Quando a entrada protegida não puder ser aberta ou confirmada:

```text
ATTEMPT
≠ SUCCESS

UNKNOWN
≠ SUCCESS
≠ FAILURE CONFIRMED

RETRY
→ REVALIDATE CURRENT CONTEXT
→ DO NOT INFER MATERIAL AUTHORIZATION
```

Regras funcionais candidatas:

- falha conhecida deve ser comunicada como falha recuperável;
- indisponibilidade não deve ativar fallback que capture relato na Home;
- estado indeterminado não deve ser tratado como entrada protegida confirmada;
- retry deve revalidar o contexto corrente;
- repetir a tentativa não cria efeito material duplicado, porque `TRN-001` não produz autorização/processamento material por si.

Resultado: **FECHADO NO LIMITE FUNCIONAL / CANDIDATO**.

## 10. Dados e autoridade

`TRN-001` não exige transferência de relato material para existir como transição legítima.

Pode haver dados técnicos necessários à navegação/sessão, mas eles não devem ser confundidos com conteúdo da Journey nem usados como autorização de processamento do Momento Atual.

```text
NAVIGATION / ACCESS DATA
≠ JOURNEY CONTENT

AUTHENTICATION
≠ MATERIAL PROCESSING AUTHORIZATION

TRN-001
≠ PERSONALIZATION AUTHORIZATION
```

Resultado: **FECHADO FUNCIONALMENTE / CANDIDATO**.

## 11. Acessibilidade e coerência de linguagem

A transição deve permanecer compreensível sem depender exclusivamente de:

- cor;
- motion;
- hover;
- mídia rica;
- vocabulário técnico.

O significado de “público → protegido” deve sobreviver à composição visual escolhida pela designer.

Resultado: **FECHADO FUNCIONALMENTE / CANDIDATO**.

## 12. Preservação de fronteiras

O exame não reabre:

- narrativa da Home;
- autoria criativa de Design;
- autenticação como superfície própria;
- `TRN-002`;
- `PER-003` ou downstream;
- implementação técnica;
- Product Engineering.

```text
TRN-001
→ HANDOFF DE CONTEXTO

TRN-001
≠ AUTH FLOW COMPLETO
≠ ONBOARDING COMPLETO
≠ PROCESSAMENTO
≠ PERSONALIZAÇÃO
```

## 13. Conclusão funcional adjudicada

O motivo histórico de `TRN-001` permanecer `PARTIAL` era a continuidade entre os pacotes público e protegido não estar examinada como conjunto.

O exame específico da UXA-105 encontra cobertura funcional suficiente, nas autoridades correntes, para fechar localmente:

- origem;
- destino;
- trigger consciente;
- mudança de contexto;
- informação mínima;
- primeira entrada × retomada;
- retorno/interrupção;
- falha/indeterminação;
- retry;
- ausência de processamento/autorização implícitos;
- acessibilidade;
- fronteiras downstream.

Conclusão candidata:

```text
UXA-105 FUNCTIONAL EXAM
→ COMPLETE

TRN-001
→ FUNCTIONALLY SUFFICIENT / ADJUDICATED

NEW FUNCTIONAL RULE REQUIRED
→ NONE IDENTIFIED

FUNCTIONAL FINDINGS
→ ADJUDICATED / NORMATIVE

CURRENT MATURITY
→ PARTIAL / UNCHANGED

MATURITY PROMOTIONS
→ 0

G1 END-TO-END
→ NOT PROMOTED BY THIS EXAM
```

## 14. Limites

Esta conclusão:

- não comprova implementação;
- não comprova roteamento real;
- não comprova autenticação técnica;
- não comprova persistência;
- não promove `TRN-001`;
- não declara G1 integralmente validado;
- não libera Product Engineering.

## 15. Estado downstream corrente

O contrato funcional foi adjudicado sem promover maturidade por si só. A frente de maturidade posterior foi concluída por gate próprio:

```text
UXA-105 FUNCTIONAL CONTRACT
→ ADJUDICATED / NORMATIVE

MATURITY EXAM
→ COMPLETE

MATURITY ADJUDICATION
→ COMPLETE

TRN-001
→ LOCALLY VALIDATED
→ PARTIAL → LOCALLY VALIDATED
→ INTEGRALLY VALIDATED NOT SUPPORTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```
