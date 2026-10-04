---
id: GKR-UXA-107-TRN201-SCOPE-EXAM-001
title: UXA-107 — TRN-201 — Exame de Escopo da Continuidade Institucional
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-04
normative: false
maturity: scope_exam_complete_pending_adjudication
depends_on:
  - GKR-UX-G3-ORGANIZATION-COLLECTIVE-RELATIONSHIP-VALIDATION-001
  - GKR-UX-ORGCOL-OVERVIEW-MASTER-001
  - GKR-UX-ORG-OPPORTUNITY-REGISTRATION-MASTER-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - UXA-013
  - UXA-014
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - GKR-TRN-201
---

# UXA-107 — TRN-201 — Exame de Escopo da Continuidade Institucional

## 1. Finalidade

Este documento executa o Scope Exam autorizado da UXA-107 exclusivamente para a continuidade:

~~~text
TRN-201
→ ORG-001 — Visão Geral da Organização
→ ORG-002 — Cadastro de Oportunidade / Programa
~~~

O exame existe para verificar se esse recorte é suficientemente delimitado para posterior adjudicação humana de escopo e eventual exame funcional próprio.

## 2. Baseline corrente

O Transition Registry declara:

~~~text
TRN-201
→ ORG-001 → ORG-002
→ PARTIAL
→ lacuna principal = ligação com visão institucional
~~~

A autoridade G3 refinou a lacuna como falta de validação ponta a ponta entre Visão Geral institucional e Cadastro de Oportunidade/Programa.

TRN-202 já está LOCALLY VALIDATED.

TRN-206..209 permanecem CONTRACTED e pertencem à continuidade bilateral Organização ↔ Coletivo, fora deste recorte.

## 3. Autoridades de origem e destino

### 3.1 ORG-001 — Visão Geral da Organização

GKR-UX-ORGCOL-OVERVIEW-MASTER-001 governa:

- contexto institucional ativo;
- identidade da Organização/unidade;
- papel e autoridade da Pessoa autenticada;
- estado material do contexto;
- atenção e continuidades legítimas;
- retorno preservando contexto;
- revalidação de autoridade quando o contexto muda.

A Visão Geral pode contextualizar Oportunidades e Programas, mas não absorve ORG-002.

### 3.2 ORG-002 — Cadastro de Oportunidade / Programa

GKR-UX-ORG-OPPORTUNITY-REGISTRATION-MASTER-001 governa:

- entrada em contexto de Organização;
- autoridade suficiente para iniciar e executar ação material;
- criação, revisão e preservação como rascunho;
- cancelamento antes do envio;
- envio, processamento, falha, indeterminação e retry;
- separação entre cadastro e oportunidade ativa em ORG-003;
- entrada registrada por TRN-201.

O próprio Master preserva a maturidade de TRN-201, sem promovê-la.

## 4. Pergunta de escopo

> É possível examinar de forma autônoma e suficiente a continuidade ORG-001 → ORG-002, sem incluir publicação/ativação, relação bilateral Organização↔Coletivo ou outros fluxos institucionais?

## 5. Escopo candidato

O recorte candidato é:

~~~text
UXA-107 CANDIDATE SCOPE

TRN-201 ONLY
→ ORG-001 → ORG-002
~~~

O exame funcional posterior, se autorizado após adjudicação do escopo, deverá verificar somente a passagem entre:

1. contexto institucional compreendido em ORG-001;
2. ação consciente de iniciar cadastro;
3. preservação da mesma Organização/unidade/contexto;
4. revalidação de autoridade aplicável;
5. chegada a ORG-002 sem criar cadastro material por mera navegação;
6. retorno/abandono sem fabricar efeito;
7. falha/indeterminação de abertura sem fabricar sucesso;
8. não duplicação por retry/reabertura;
9. preservação da separação entre ORG-002 e ORG-003.

## 6. Fora do escopo

Explicitamente fora:

- TRN-202 — ORG-002 → ORG-003;
- TRN-203;
- TRN-206..209;
- relação bilateral Organização ↔ Coletivo;
- criação de novos ORG-ID, TRN-ID ou superfícies;
- reformulação dos Masters;
- wireframe ou high-fidelity;
- protótipo;
- implementação;
- Product Engineering;
- qualquer promoção automática de maturidade;
- declaração de G3 integralmente validada.

## 7. Critérios para futuro exame funcional

Se o escopo for adjudicado, o futuro exame funcional deverá responder, no mínimo:

1. a mesma Organização/unidade/contexto é preservada;
2. a Pessoa entende que está iniciando um cadastro, não publicando uma oportunidade;
3. a ação de entrada é consciente e distinguível de mera navegação;
4. autoridade é revalidada quando material;
5. acesso a ORG-002 não cria cadastro, rascunho ou envio automaticamente;
6. retorno preserva contexto legítimo;
7. interrupção antes de efeito não é tratada como falha;
8. indisponibilidade/resultado indeterminado não fabrica sucesso;
9. retry não duplica efeito lógico;
10. ORG-002 permanece separado de ORG-003;
11. TRN-202 permanece fora do exame;
12. nenhuma relação O↔C é inferida por analogia.

## 8. Resultado do Scope Exam

A evidência corrente é suficiente para delimitar TRN-201 como unidade autônoma de exame.

~~~text
UXA-107 SCOPE EXAM
→ COMPLETE

CANDIDATE SCOPE
→ TRN-201 ONLY
→ ORG-001 → ORG-002

SCOPE SUFFICIENCY
→ SUFFICIENT CANDIDATE

SCOPE ADJUDICATION
→ PENDING HUMAN GATE

FUNCTIONAL EXAM
→ NOT_STARTED
→ NOT_AUTHORIZED

CURRENT MATURITY
→ TRN-201 = PARTIAL

MATURITY PROMOTIONS
→ 0

TRANSITION REGISTRY
→ UNCHANGED

G3 INTEGRALLY VALIDATED
→ NOT CLAIMED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
~~~

## 9. Próximo gate

O próximo gate, se autorizado, é exclusivamente a adjudicação humana do escopo candidato:

~~~text
TRN-201 ONLY
→ ORG-001 → ORG-002
~~~

A adjudicação de escopo não autoriza automaticamente exame funcional, maturity exam, promoção de maturidade, Design, protótipo ou Product Engineering.
