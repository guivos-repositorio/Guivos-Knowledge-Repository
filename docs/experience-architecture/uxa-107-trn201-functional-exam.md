---
id: GKR-UXA-107-TRN201-FUNCTIONAL-EXAM-001
title: UXA-107 — TRN-201 — Exame Funcional da Continuidade ORG-001 → ORG-002
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-04
normative: false
maturity: functional_exam_complete_pending_adjudication
depends_on:
  - GKR-UXA-107-TRN201-SCOPE-EXAM-001
  - GKR-UX-G3-ORGANIZATION-COLLECTIVE-RELATIONSHIP-VALIDATION-001
  - GKR-UX-ORGCOL-OVERVIEW-MASTER-001
  - GKR-UX-ORG-OPPORTUNITY-REGISTRATION-MASTER-001
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - GKR-TRN-201
---

# UXA-107 — TRN-201 — Exame Funcional da Continuidade ORG-001 → ORG-002

## 1. Finalidade

Este documento executa o Functional Exam autorizado da UXA-107 exclusivamente dentro do escopo adjudicado:

~~~text
TRN-201 ONLY
→ ORG-001 — Visão Geral da Organização
→ ORG-002 — Cadastro de Oportunidade / Programa
~~~

O exame verifica suficiência funcional documental da continuidade. Ele não adjudica ainda o contrato funcional, não promove maturidade, não altera o Transition Registry e não libera Product Engineering.

## 2. Baseline governada

~~~text
TRN-201
→ CURRENT MATURITY = PARTIAL

SCOPE
→ ADJUDICATED / NORMATIVE

FUNCTIONAL EXAM
→ AUTHORIZED

MATURITY PROMOTIONS
→ 0
~~~

A lacuna corrente é a continuidade ponta a ponta entre a Visão Geral institucional e a entrada no Cadastro de Oportunidade/Programa.

## 3. Pergunta funcional

> As autoridades correntes sustentam, sem criação de nova regra, uma continuidade coerente e verificável de ORG-001 para ORG-002, preservando contexto, autoridade, intenção, ausência de efeito por mera navegação, retorno, indeterminação, retry e separação entre cadastro e ativação?

## 4. Continuidade ORG-001 → ORG-002

### 4.1 Contexto e identidade institucional

ORG-001 governa contexto ativo, Organização/unidade, papel e autoridade da Pessoa autenticada.

ORG-002 exige que a Pessoa atue no contexto da mesma Organização e com autoridade compatível com a ação pretendida.

Resultado:

- a mesma Organização/unidade/contexto deve ser preservada;
- troca de contexto exige revalidação de autoridade;
- acesso a ORG-002 não pode reinterpretar silenciosamente qual Organização está ativa.

### 4.2 Intenção consciente de iniciar cadastro

A Visão Geral pode oferecer continuidade para Oportunidades e Programas, mas não absorve a responsabilidade de cadastro.

O avanço funcional exige ação consciente que represente intenção de iniciar ou retomar trabalho de cadastro.

~~~text
OPEN ORG-002
≠ CREATE DRAFT
≠ SEND
≠ PUBLISH
≠ ACTIVATE
~~~

A mera navegação para ORG-002 não cria objeto material, rascunho, envio ou publicação.

### 4.3 Autoridade

A autoridade deve ser compatível com a ação material pretendida.

A continuidade é funcionalmente suficiente quando:

1. o contexto de autoridade de ORG-001 é preservado;
2. ORG-002 revalida autoridade quando necessário;
3. autoridade insuficiente não é representada como capacidade disponível;
4. acesso, edição, envio e aprovação permanecem semanticamente distintos.

### 4.4 Retorno e abandono

Retornar a ORG-001 antes de qualquer efeito material:

- não cria cadastro;
- não cria rascunho;
- não envia oportunidade;
- não constitui falha;
- preserva contexto legítimo quando seguro.

### 4.5 Falha e estado indeterminado

Se ORG-002 não puder ser aberto ou confirmado:

~~~text
ATTEMPT
≠ SUCCESS

UNKNOWN
≠ FAILURE CONFIRMED
~~~

A interface não pode fabricar cadastro aberto, rascunho criado ou outro efeito material sem confirmação suficiente.

### 4.6 Retry e não duplicação

Retry ou reabertura não pode duplicar efeito material.

Quando houver possibilidade de efeito anterior não confirmado, a autoridade transversal de UXA-102/V5 exige reconciliação suficiente antes de nova mutação.

### 4.7 Separação ORG-002 ≠ ORG-003

ORG-002 governa cadastro, revisão e envio.

ORG-003 governa oportunidade aprovada/ativa.

TRN-201 não publica, ativa ou aprova oportunidade.

TRN-202 permanece fora deste exame.

## 5. Stress cases

### 5.1 Mudança de Organização antes da entrada

A continuidade deve revalidar contexto e autoridade. Não é válido carregar silenciosamente um cadastro para outra Organização/unidade.

### 5.2 Clique repetido para abrir cadastro

Repetição de navegação não pode criar múltiplos rascunhos ou objetos materiais por inferência.

### 5.3 Sessão/contexto expirado

A experiência deve representar bloqueio, falha ou indeterminação conforme evidência, preservando o que for seguro e sem fabricar acesso.

### 5.4 Pessoa sem autoridade suficiente

ORG-002 pode preservar trabalho permitido quando a autoridade corrente sustentar isso, mas não pode simular capacidade de envio ou aprovação inexistente.

### 5.5 Retorno imediato à Visão Geral

Voltar sem efeito material não constitui cancelamento de cadastro enviado, rollback ou falha.

## 6. Critérios examinados

O exame fecha documentalmente os critérios adjudicados no Scope Exam:

1. mesma Organização/unidade/contexto preservada;
2. início de cadastro distinguível de publicação;
3. ação de entrada consciente;
4. autoridade revalidada quando material;
5. acesso a ORG-002 sem criação automática de cadastro/rascunho/envio;
6. retorno preservando contexto legítimo;
7. interrupção antes de efeito sem fabricar falha;
8. indisponibilidade/indeterminação sem fabricar sucesso;
9. retry sem duplicação lógica;
10. ORG-002 separado de ORG-003;
11. TRN-202 fora do exame;
12. nenhuma relação O↔C inferida por analogia.

## 7. O que o exame não comprova

Este exame não comprova:

- implementação;
- persistência técnica;
- telemetria;
- teste integrado em produto;
- existência de um mecanismo técnico específico de idempotência;
- publicação/ativação em ORG-003;
- TRN-202;
- TRN-203;
- TRN-206..209;
- relação bilateral Organização ↔ Coletivo;
- G3 integralmente validada.

## 8. Resultado do exame

~~~text
UXA-107 FUNCTIONAL EXAM
→ COMPLETE

TRN-201
→ FUNCTIONALLY SUFFICIENT CANDIDATE

NEW FUNCTIONAL RULE REQUIRED
→ NO

FUNCTIONAL CONTRACT ADJUDICATION
→ PENDING HUMAN GATE

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

O próximo gate, se autorizado, é exclusivamente a adjudicação humana do contrato funcional examinado.

Essa adjudicação, por si só:

- não promove maturidade;
- não altera o Transition Registry;
- não autoriza maturity exam;
- não declara G3 integralmente validada;
- não libera Design, protótipo ou Product Engineering.
