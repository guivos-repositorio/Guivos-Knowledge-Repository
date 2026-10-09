---
id: GKR-UXA-108-G4-SCOPE-EXAM-001
title: UXA-108 — G4 — Exame de Escopo do Processo Interno de Oportunidade
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-09
normative: false
maturity: scope_candidate_pending_adjudication
depends_on:
  - GKR-UX-G4-INTERNAL-OPPORTUNITY-PROCESS-VALIDATION-001
  - GKR-UX-PERSON-INTERNAL-OPPORTUNITY-APPLICATION-CONTRACT-001
  - GKR-UX-ORG-OPPORTUNITY-APPLICATIONS-CONTRACT-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - GKR-TRN-212
  - GKR-TRN-214
---

# UXA-108 — G4 — Exame de Escopo do Processo Interno de Oportunidade

## 1. Finalidade

Este documento executa o Scope Exam autorizado da UXA-108 sobre a família G4 deixada pela UXA-102/V5.

O objetivo é verificar qual recorte possui evidência suficiente para eventual adjudicação humana de escopo e posterior Functional Exam próprio.

## 2. Baseline corrente

A autoridade G4 corrente declara:

```text
TRN-212
→ PER-203 → PER-204
→ CONTRACTED / UNCHANGED

TRN-214
→ ORG-003 → ORG-008
→ CONTRACTED / UNCHANGED

MATURITY PROMOTIONS
→ 0
```

As duas transições permanecem abertas por ausência de validação ponta a ponta e pela maturidade ainda candidata das responsabilidades especializadas `PER-204` e `ORG-008`.

A mesma autoridade preserva:

```text
TRN-213
TRN-215
TRN-216
→ OUTSIDE THIS G4 EXAM
→ OWN BILATERAL CONTINUITY
```

## 3. Unidades examinadas

### 3.1 TRN-212 — PER-203 → PER-204

Representa a entrada consciente da Pessoa a partir do Detalhe da Oportunidade em um processo interno legítimo de manifestação de interesse ou inscrição.

O recorte exige preservar:

- mesma oportunidade e publicador;
- finalidade e contexto autorizados;
- ação consciente da Pessoa;
- entrada sem criar elegibilidade, seleção, participação ou resultado;
- retorno contextual a PER-203;
- ausência de criação automática de objeto por mera navegação;
- falha/indeterminação sem fabricar sucesso;
- retry sem duplicação lógica.

### 3.2 TRN-214 — ORG-003 → ORG-008

Representa o acesso institucional contextual da oportunidade ativa à gestão de manifestações/inscrições legitimamente recebidas.

O recorte exige preservar:

- mesma Organização/unidade/contexto;
- mesma oportunidade ativa;
- autoridade institucional suficiente;
- acesso sem criar inscrição ou objeto bilateral;
- ausência de confirmação de recebimento por mera navegação;
- ausência de mutação do estado da oportunidade;
- retorno contextual a ORG-003;
- revalidação de autoridade e dados;
- falha/indeterminação sem fabricar estado;
- retry/reabertura sem duplicação de efeito lógico.

## 4. Pergunta de escopo

> É possível examinar autonomamente TRN-212 e TRN-214 como duas continuidades locais da família G4, sem absorver envio bilateral, comunicação pós-envio, seleção, resultado ou implementação?

## 5. Escopo candidato

A evidência corrente sustenta como candidato:

```text
UXA-108 CANDIDATE SCOPE

TRN-212
→ PER-203 → PER-204

TRN-214
→ ORG-003 → ORG-008
```

As duas transições podem ser examinadas no mesmo pacote porque:

1. pertencem explicitamente à família G4 corrente;
2. foram examinadas conjuntamente pela autoridade G4;
3. compartilham o mesmo problema de continuidade local para responsabilidades especializadas;
4. não exigem absorver as continuidades bilaterais pós-envio;
5. preservam limites de autoridade distintos entre Pessoa e Organização.

## 6. Fora do escopo

Explicitamente fora:

- TRN-213 — PER-204 → ORG-008;
- TRN-215 — ORG-008 → PER-204;
- TRN-216 — PER-204 → ORG-008;
- seleção, elegibilidade, aprovação, participação ou resultado;
- regras de ranking, score ou priorização;
- novos PER-ID, ORG-ID ou TRN-ID;
- retornos contextuais como novas transições dedicadas;
- persistência técnica, storage, locking, delivery ou telemetria;
- wireframe, high-fidelity ou protótipo;
- Product Engineering;
- promoção automática de maturidade;
- declaração de G4 integralmente validada.

## 7. Critérios para futuro Functional Exam

Se o escopo for adjudicado, o Functional Exam deverá verificar, no mínimo:

### TRN-212

1. mesma oportunidade/publicador preservados;
2. ação de entrada consciente e distinguível de mera navegação;
3. entrada não cria manifestação/inscrição automaticamente;
4. finalidade e recorte de dados permanecem proporcionais;
5. retorno a PER-203 preserva contexto legítimo;
6. interrupção antes de efeito não fabrica falha;
7. resultado indeterminado não fabrica sucesso;
8. retry não duplica objeto lógico;
9. entrada não cria elegibilidade, seleção, participação ou resultado.

### TRN-214

1. mesma Organização/unidade/oportunidade preservadas;
2. autoridade institucional revalidada quando material;
3. abertura de ORG-008 não cria objeto nem confirma recebimento;
4. abertura não altera o estado da oportunidade;
5. retorno a ORG-003 preserva contexto legítimo;
6. dados não são ampliados silenciosamente;
7. falha/indeterminação não fabrica estado;
8. retry/reabertura não duplica efeito lógico.

## 8. Resultado do Scope Exam

A evidência corrente é suficiente para delimitar as duas transições como unidade candidata de exame.

```text
UXA-108 SCOPE EXAM
→ COMPLETE

CANDIDATE SCOPE
→ TRN-212 + TRN-214
→ PER-203 → PER-204
→ ORG-003 → ORG-008

SCOPE SUFFICIENCY
→ SUFFICIENT AS CANDIDATE

SCOPE ADJUDICATION
→ PENDING
→ NOT NORMATIVE

FUNCTIONAL EXAM
→ NOT_STARTED
→ NOT_AUTHORIZED

CURRENT MATURITY
→ TRN-212 = CONTRACTED
→ TRN-214 = CONTRACTED

MATURITY PROMOTIONS
→ 0

TRANSITION REGISTRY
→ UNCHANGED

G4 INTEGRALLY VALIDATED
→ NOT CLAIMED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 9. Próximo gate

O próximo gate é exclusivamente a adjudicação humana do escopo candidato:

```text
TRN-212 + TRN-214
→ CANDIDATE SCOPE
```

Até essa adjudicação:

```text
SCOPE
→ NOT NORMATIVE

FUNCTIONAL EXAM
→ NOT AUTHORIZED

MATURITY
→ UNCHANGED
```
