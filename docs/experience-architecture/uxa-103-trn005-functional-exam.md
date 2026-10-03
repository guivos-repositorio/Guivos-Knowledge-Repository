---
id: GKR-UXA-103-TRN005-FUNCTIONAL-EXAM-001
title: UXA-103 — TRN-005 — Exame Funcional de Resultado Indeterminado, Reconciliação e Retry
status: candidate
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: functional_exam_candidate
depends_on:
  - UXA-103
  - GKR-UXA-103-TRN005-SCOPE-AUTHORITY-001
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
  - GKR-UX-PER005-MASTER-001
  - GKR-UX-PER006-MASTER-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
---

# UXA-103 — TRN-005 — Exame Funcional de Resultado Indeterminado, Reconciliação e Retry

## 1. Finalidade

Este documento registra o exame funcional governado de `TRN-005 — PER-005 → PER-006` dentro do escopo adjudicado da UXA-103.

O exame testa se as autoridades correntes fecham, ponta a ponta, resultado indeterminado, reconciliação antes de retry, não duplicação do efeito lógico e recuperação após interrupção.

Este documento é candidato e não promove maturidade por si só.

## 2. Baseline examinada

A baseline corrente já fecha:

- inventário revisado e autorização específica antes do processamento;
- exclusão de itens não autorizados;
- início visível de processamento;
- interrupção voluntária com efeito conhecido;
- descarte de resultado parcial quando a interrupção é confirmada;
- falha conhecida sem simulação de sucesso;
- ausência de continuidade silenciosa em background;
- distinção entre processamento, persistência e personalização.

A lacuna de G1 permanece especificamente quando houve tentativa de processamento, mas não existe confirmação suficiente de qual efeito ocorreu.

## 3. Resultado por dimensão

### 3.1 Resultado indeterminado

**Baseline atual: insuficiente.**

`PER-006` possui estados de processamento, interrupção e falha, mas não contém condição funcional explícita para:

> houve tentativa, porém não há evidência suficiente para afirmar sucesso, falha conhecida ou interrupção efetivada.

Conclusão candidata:

```text
NO SUFFICIENT CONFIRMATION
→ INDETERMINATE
→ ≠ SUCCESS
→ ≠ KNOWN FAILURE
→ ≠ CONFIRMED INTERRUPTION
```

### 3.2 Reconciliação antes de retry

**Baseline atual: insuficiente localmente.**

A regra transversal `V5-R3` exige reconciliação antes de retry após resultado indeterminado, mas `PER-005/PER-006` ainda não traduzem essa regra para o handoff específico de `TRN-005`.

Conclusão candidata:

```text
TRN-005 INDETERMINATE
→ RECONCILE CURRENT EFFECT
→ ONLY THEN
→ RETRY OR CONTINUE
```

Enquanto a reconciliação estiver pendente, nenhuma nova mutação equivalente deve ser disparada.

### 3.3 Identidade lógica da intenção

**Baseline atual: parcialmente suficiente.**

`PER-005` preserva identificadores dos itens, proveniência, finalidade, revisão e autorização. Isso fornece contexto suficiente para definir semanticamente uma mesma intenção lógica, mas não existe ainda contrato explícito ligando esse conjunto ao retry.

Conclusão candidata:

A intenção lógica de `TRN-005` é o mesmo conjunto material de:

- conteúdo revisado;
- recorte autorizado;
- finalidade autorizada;
- decisão de autorização aplicável.

A identidade é funcional, não um token técnico.

Mudança material em conteúdo, finalidade ou autorização deixa de ser retry da mesma intenção e exige novo gate de revisão/autorização em `PER-005`.

### 3.4 Não duplicação do efeito lógico

**Baseline atual: requisito transversal existente, fechamento específico ausente.**

`V5-R6` já determina que não duplicar efeito lógico é requisito funcional. Porém o contrato específico de `TRN-005` ainda não diz como interpretar repetição da mesma intenção após estado indeterminado.

Conclusão candidata:

```text
SAME LOGICAL INTENT
→ MUST NOT CREATE SILENT DUPLICATE PROCESSING EFFECT

TECHNICAL MECHANISM
→ ENGINEERING DECISION LATER
```

### 3.5 Interrupção conhecida versus interrupção indeterminada

**Baseline atual: precisa de distinção adicional.**

`PER-006` governa corretamente a interrupção quando o encerramento e o descarte do resultado parcial são conhecidos.

Se a Pessoa solicita interrupção, mas não há confirmação suficiente de que o processamento realmente cessou ou de que nenhum efeito concorrente foi concluído, o estado não pode ser apresentado como “processamento interrompido”.

Conclusão candidata:

- interrupção confirmada → estado conhecido de interrupção;
- interrupção sem confirmação suficiente → resultado indeterminado;
- resultado indeterminado → reconciliação antes de retry ou nova mutação.

### 3.6 Estado durante reconciliação

**Baseline atual: ausente localmente.**

A UXA-102/V5 admite semanticamente “em reconciliação”, mas `PER-006` não o incorpora à experiência específica.

Conclusão candidata:

Enquanto houver reconciliação:

- não fabricar conclusão;
- não fabricar falha específica;
- não disparar retry mutante equivalente;
- manter a Pessoa informada de que o estado ainda está sendo confirmado;
- permitir somente ações não conflitantes compatíveis com a autoridade corrente.

Isso não cria novo `PER-ID` nem obriga uma tela própria.

### 3.7 Evidência suficiente para sair do indeterminado

Conclusão candidata:

O estado indeterminado só pode ser encerrado quando a fonte competente permitir afirmar uma das condições:

1. **efeito não ocorreu** → retry pode voltar a ser elegível, sujeito à autoridade vigente;
2. **efeito está em andamento** → representar o processamento corrente sem reiniciar a mesma intenção;
3. **efeito concluiu** → seguir a continuidade legítima sem repetir processamento;
4. **falha conhecida confirmada** → apresentar falha comprovável e ações aplicáveis;
5. **interrupção confirmada** → aplicar o contrato de interrupção já existente.

Projeção local, animação, timeout ou ausência de resposta não bastam, isoladamente, como estado canônico.

## 4. Contrato funcional candidato

O exame converge para o seguinte contrato candidato:

```text
PER-005
→ REVIEWED + SPECIFICALLY AUTHORIZED LOGICAL INTENT
→ TRN-005

TRN-005
→ ATTEMPT

CONFIRMED PROCESSING
→ PER-006 CURRENT PROCESSING

KNOWN FAILURE
→ KNOWN FAILURE CONTRACT

CONFIRMED INTERRUPTION
→ INTERRUPTION CONTRACT

INSUFFICIENT CONFIRMATION
→ INDETERMINATE
→ RECONCILE BEFORE RETRY

RECONCILIATION
→ EFFECT NOT OCCURRED
   → SAFE RETRY MAY BECOME ELIGIBLE
→ EFFECT IN PROGRESS
   → DO NOT RESTART
→ EFFECT COMPLETED
   → CONTINUE WITHOUT REPROCESSING
→ KNOWN FAILURE
   → FAILURE CONTRACT
→ CONFIRMED INTERRUPTION
   → INTERRUPTION CONTRACT

SAME LOGICAL INTENT
→ NO SILENT DUPLICATE EFFECT
```

## 5. Compatibilidade com as autoridades existentes

O contrato candidato:

- especializa `V5-R2`, `V5-R3`, `V5-R6` e `V5-R9` para `TRN-005`;
- não cria protocolo técnico;
- não define idempotency key;
- não seleciona banco, fila, lock ou mecanismo de concorrência;
- não amplia finalidade ou autorização;
- não altera `PER-013/014`;
- não toca G2–G5;
- não cria superfície ou transição nova.

## 6. Avaliação dos critérios da autoridade de escopo

| Critério | Resultado do exame |
|---|---|
| estado indeterminado explícito | **CONTRATO CANDIDATO DEFINIDO** |
| reconciliação antes de retry | **CONTRATO CANDIDATO DEFINIDO** |
| não duplicação do efeito lógico | **CONTRATO CANDIDATO DEFINIDO** |
| recuperação após interrupção | **CONTRATO CANDIDATO DEFINIDO** |
| sucesso × falha conhecida × ausência de confirmação | **DISTINÇÃO CANDIDATA DEFINIDA** |
| continuidade ponta a ponta verificável | **CANDIDATA, AINDA NÃO ADJUDICADA** |

## 7. Resultado do exame

```text
UXA-103 FUNCTIONAL EXAM
→ COMPLETED AT CANDIDATE LEVEL

FUNCTIONAL CONVERGENCE
→ YES

ADJUDICATION
→ PENDING HUMAN GATE

TRN-005
→ PARTIAL / UNCHANGED

MATURITY PROMOTIONS
→ 0
```

A convergência analítica não equivale à adjudicação.

## 8. Próximo gate

O próximo gate é a adjudicação humana do contrato funcional candidato.

Somente após essa adjudicação será legítimo:

1. materializar a autoridade normativa específica da UXA-103;
2. reconciliar `PER-005`, `PER-006` e o Transition Registry;
3. submeter `TRN-005` a um gate separado de maturidade.

Nenhuma dessas três etapas é executada por este exame.
