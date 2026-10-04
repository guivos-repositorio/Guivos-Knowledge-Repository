---
id: GKR-UXA-106-G2-FUNCTIONAL-EXAM-001
title: UXA-106 — Exame Funcional — Continuidade G2 da Descoberta ao Estado Pendente
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-04
normative: false
maturity: functional_exam_complete_pending_adjudication
depends_on:
  - GKR-UXA-106-G2-SCOPE-EXAM-001
  - GKR-UX-G2-COLLECTIVE-DISCOVERY-REQUEST-VALIDATION-001
  - GKR-UX-PER102-MASTER-001
  - GKR-UX-PER103-MASTER-001
  - GKR-UX-PER104-MASTER-001
  - GKR-UX-PER105-MASTER-001
  - GKR-UXA-102-V5-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - UXA-056
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - GKR-TRN-102
  - GKR-TRN-103
  - GKR-TRN-104
---

# UXA-106 — Exame Funcional — Continuidade G2 da Descoberta ao Estado Pendente

## 1. Finalidade

Este documento executa o Functional Exam autorizado da UXA-106 dentro do escopo já adjudicado e normativo:

```text
TRN-102
→ PER-102 → PER-103

TRN-103
→ PER-103 → PER-104

TRN-104
→ PER-104 → PER-105
```

O exame verifica suficiência funcional documental. Ele não adjudica contrato funcional, não promove maturidade, não altera o Transition Registry e não libera Design, protótipo ou Product Engineering.

## 2. Baseline governada

A autoridade de escopo da UXA-106 preserva:

```text
TRN-102
TRN-103
TRN-104
→ PARTIAL / UNCHANGED

MATURITY PROMOTIONS
→ 0

G2 END-TO-END
→ NOT VALIDATED
```

A autoridade G2 já havia concluído que a lacuna remanescente não é ausência de semântica básica, mas ausência de validação integrada da continuidade ponta a ponta.

## 3. Pergunta funcional

> As autoridades correntes sustentam, sem criação de nova regra, um contrato funcional coerente e verificável para a continuidade `PER-102 → PER-103 → PER-104 → PER-105`, preservando identidade, contexto, intenção, consentimento, estado canônico, retorno, indeterminação e não duplicação lógica?

## 4. TRN-102 — PER-102 → PER-103

### 4.1 Evidência corrente

`PER-102` governa:

- consulta, filtros, origem e território legitimamente ativos;
- seleção consciente de um resultado;
- ausência de vínculo por mera exposição ou seleção;
- proteção de identidade e contexto pessoal;
- erro distinto de ausência legítima de resultados;
- recuperação sem ampliação silenciosa.

`PER-103` governa:

- recebimento do identificador lógico do mesmo Coletivo;
- contexto mínimo necessário à explicação da origem e ao retorno;
- compreensão pública antes de vínculo;
- ausência de participação ou solicitação por mera visualização.

### 4.2 Resultado

A continuidade é funcionalmente coerente quando:

1. o resultado selecionado resolve para o mesmo Coletivo em `PER-103`;
2. origem/contexto necessário ao retorno é preservado sem ampliar dados pessoais;
3. patrocínio ou natureza da descoberta continua distinguível quando material;
4. falha ao abrir o perfil não é representada como inexistência do Coletivo;
5. seleção ou abertura do perfil não cria acompanhamento, solicitação ou vínculo.

```text
TRN-102
→ FUNCTIONALLY SUFFICIENT CANDIDATE
→ HUMAN ADJUDICATION PENDING
→ MATURITY = PARTIAL / UNCHANGED
```

## 5. TRN-103 — PER-103 → PER-104

### 5.1 Evidência corrente

`PER-103` exige avanço consciente antes de revisão e afirma que abrir a revisão não equivale a enviar solicitação.

`PER-104` governa:

- identificação do mesmo Coletivo;
- modelo de entrada, regras e critérios materiais;
- dados e permissões necessários;
- significado e consequências do ato;
- edição, retorno e cancelamento antes do envio;
- confirmação afirmativa e não pré-selecionada.

### 5.2 Resultado

A continuidade é funcionalmente coerente quando:

1. a Pessoa escolhe conscientemente avançar do Perfil Público;
2. o mesmo Coletivo e o mesmo contexto material são preservados;
3. `PER-104` apresenta revisão suficiente antes de qualquer efeito;
4. cancelar ou retornar antes do envio não cria solicitação;
5. abrir `PER-104` não cria vínculo nem envia solicitação;
6. nenhuma regra, consentimento ou confirmação material começa presumida.

```text
TRN-103
→ FUNCTIONALLY SUFFICIENT CANDIDATE
→ HUMAN ADJUDICATION PENDING
→ MATURITY = PARTIAL / UNCHANGED
```

## 6. TRN-104 — PER-104 → PER-105

### 6.1 Evidência corrente

`PER-104` governa confirmação explícita, distinção entre revisão e envio, processamento sem sucesso fabricado e não duplicação lógica da intenção.

`PER-105` governa:

- a mesma solicitação lógica após o envio;
- estado pendente sem promessa de aprovação;
- consulta sem alterar fila, prioridade, decisão ou vínculo;
- resposta adicional sem duplicar solicitação;
- cancelamento como estado próprio quando aplicável;
- processamento, recuperação e não fabricação de resultado.

A autoridade transversal `GKR-UXA-102-V5-AUTHORITY-001` adiciona:

```text
ATTEMPT ≠ SUCCESS
UNKNOWN ≠ FAILURE
RETRY → RECONCILE FIRST WHEN NEEDED
STALE CLIENT ≠ CANONICAL AUTHORITY
```

### 6.2 Resultado

A continuidade é funcionalmente coerente quando:

1. o envio decorre de confirmação afirmativa e válida;
2. `PER-105` referencia o mesmo objeto lógico solicitado;
3. `pending` só é apresentado após confirmação suficiente de recebimento/efeito;
4. ausência de confirmação suficiente resulta em estado indeterminado, não em sucesso fabricado;
5. retry após indeterminação exige reconciliação suficiente antes de nova mutação;
6. repetição técnica não é apresentada como nova solicitação;
7. envio não equivale a aprovação nem a vínculo;
8. consultar `PER-105` não altera o estado material da solicitação.

```text
TRN-104
→ FUNCTIONALLY SUFFICIENT CANDIDATE
→ HUMAN ADJUDICATION PENDING
→ MATURITY = PARTIAL / UNCHANGED
```

## 7. Continuidade integrada do conjunto

O conjunto é funcionalmente coerente no limite documental quando preserva:

```text
SEARCH RESULT
→ SAME COLLECTIVE
→ PUBLIC COMPREHENSION
→ CONSCIOUS REVIEW
→ AFFIRMATIVE CONFIRMATION
→ SAME LOGICAL REQUEST
→ PENDING ONLY AFTER SUFFICIENT CONFIRMATION
```

Preservações obrigatórias:

- identidade do mesmo Coletivo;
- proveniência/contexto necessário à navegação e retorno;
- exploração pública sem vínculo;
- revisão separada de envio;
- envio separado de aprovação;
- minimização e finalidade dos dados;
- retorno/cancelamento antes do efeito sem fabricar falha;
- resultado indeterminado explícito;
- reconciliação antes de retry quando necessária;
- não duplicação lógica;
- estado canônico prevalecendo sobre interface stale;
- acessibilidade e linguagem suficientes para distinguir estados e efeitos.

## 8. Stress cases

### 8.1 Perfil indisponível após seleção

A falha não transforma seleção em inexistência do Coletivo nem cria vínculo. O contexto legitimamente necessário pode ser preservado para recuperação.

### 8.2 Pessoa entra em revisão e volta

Retornar a `PER-103` antes de confirmar não envia solicitação, não cria vínculo e não produz rollback de efeito inexistente.

### 8.3 Duplo acionamento de confirmação

Repetição de interface não autoriza múltiplas solicitações lógicas. O mecanismo técnico permanece decisão posterior de Engenharia.

### 8.4 Confirmação sem resultado conclusivo

A interface deve representar indeterminação e reconciliar o estado antes de nova mutação quando necessário.

### 8.5 Reabertura de PER-105

Reabrir ou recarregar não cria nova solicitação e deve refletir o estado canônico corrente do mesmo objeto lógico.

## 9. O que o exame não comprova

Este exame não comprova:

- implementação;
- persistência técnica;
- protocolo técnico de idempotência;
- observabilidade;
- comportamento real de backend;
- teste integrado executado;
- materialização visual;
- aprovação/recusa downstream;
- `TRN-105+`;
- `TRN-114`;
- G2 integralmente validada.

## 10. Resultado do exame

```text
UXA-106 FUNCTIONAL EXAM
→ COMPLETE

TRN-102
→ FUNCTIONALLY SUFFICIENT CANDIDATE

TRN-103
→ FUNCTIONALLY SUFFICIENT CANDIDATE

TRN-104
→ FUNCTIONALLY SUFFICIENT CANDIDATE

NEW FUNCTIONAL RULE REQUIRED
→ NO

FUNCTIONAL CONTRACT ADJUDICATION
→ PENDING HUMAN GATE

CURRENT MATURITY
→ TRN-102 = PARTIAL
→ TRN-103 = PARTIAL
→ TRN-104 = PARTIAL

MATURITY PROMOTIONS
→ 0

TRANSITION REGISTRY
→ UNCHANGED

G2 INTEGRALLY VALIDATED
→ NOT CLAIMED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 11. Próximo gate

O próximo gate, se autorizado, é exclusivamente a adjudicação humana do contrato funcional examinado.

Essa adjudicação, por si só:

- não promove maturidade;
- não altera o Transition Registry;
- não declara G2 integralmente validada;
- não autoriza maturity exam;
- não libera Design, protótipo ou Product Engineering.
