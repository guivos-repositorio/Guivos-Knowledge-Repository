---
id: GKR-UX-PER002-DESIGN-VALIDATION-001
title: PER-002 — Validação Funcional da Materialização Low-Fidelity
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-09
normative: false
maturity: low_fidelity_functional_validation_pass
parent: UXA-000
depends_on:
  - GKR-UX-PER002-DESIGN-DELIVERY-001
  - GKR-UX-PER002-DESIGN-AUTH-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - UXA-020
  - UXA-023
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-STATE-001
  - PER-001
  - PER-002
  - PER-003
  - PER-008
  - TRN-001
  - TRN-002
---

# PER-002 — Validação Funcional da Materialização Low-Fidelity

## 1. Finalidade

Este documento registra a validação documental/visual da primeira entrega low-fidelity de `PER-002 — Entrada protegida`, materializada em `GKR-UX-PER002-DESIGN-DELIVERY-001 v0.1.0`.

A validação não redesenha a entrega, não cria nova superfície, não promove automaticamente maturidade agregada e não autoriza estágio posterior.

```text
VALIDATION TARGET
→ GKR-UX-PER002-DESIGN-DELIVERY-001 v0.1.0

VALIDATION MODE
→ DOCUMENTARY / VISUAL
→ FUNCTIONAL ADHERENCE

RESULT
→ PASS

MATERIAL FINDINGS
→ 0

BLOCKING FINDINGS
→ 0

REFORMULATION REQUIRED
→ NO
```

## 2. Autoridades confrontadas

A validação foi executada contra:

1. `GKR-UX-PER002-MAT-ELIGIBILITY-001` — boundary funcional congelado;
2. `GKR-UX-PER002-DESIGN-AUTH-001` — escopo e limites da autorização;
3. `UXA-020` — relação Home × entrada protegida × continuidade;
4. `UXA-023` — contrato funcional validado da entrada protegida;
5. `GKR-JOURNEY-SURFACE-REGISTRY-001`;
6. `GKR-JOURNEY-SURFACE-DETAIL-PERSON-001`;
7. `GKR-JOURNEY-TRANSITION-REGISTRY-001`;
8. distinção primeira entrada × login resumptivo;
9. guardrails de privacidade, autonomia, reversibilidade e não coerção.

## 3. Objeto inspecionado

A entrega validada representa `PER-002` como uma única responsabilidade com quatro frames principais e três variantes:

```text
PER-002
├─ FRAME 01 — ORIENTAÇÃO PROTEGIDA / PRÉ-AUTH
├─ FRAME 02 — GATE DE ACESSO
│  ├─ VARIANTE A — SESSÃO JÁ AUTENTICADA
│  └─ VARIANTE B — RECUPERAÇÃO / RESTRIÇÃO / FALHA
├─ FRAME 03 — CONTINUAÇÃO AUTENTICADA / CONTROLES
├─ VARIANTE C — SAIR / INTERROMPER / EXPLORAR SEM PERSONALIZAÇÃO
└─ FRAME 04 — HANDOFF READY
                 ↓
               TRN-002
                 ↓
               PER-003
```

```text
7 AUTHORIZED COVERAGE AREAS
→ 7 / 7 REPRESENTED

7 AREAS
≠ 7 CANONICAL SURFACES
≠ 7 PER-IDs
```

## 4. Matriz de cobertura obrigatória

| Requisito | Evidência na entrega | Resultado |
|---|---|---|
| orientação protegida / pré-auth | Frame 01 | PASS |
| gate de autenticação quando necessário | Frame 02 | PASS |
| sessão já autenticada | Variante A | PASS |
| continuação autenticada de `PER-002` | Frame 03 | PASS |
| acesso / recuperação / restrição / falha | Variante B | PASS |
| retorno / interrupção / não prosseguimento / alternativa sem personalização | Variante C + ações persistentes | PASS |
| condição de handoff legítimo | Frame 04 | PASS |

Resultado:

```text
AUTHORIZED COVERAGE
→ 7 / 7 PASS
```

## 5. Critérios de aceitação do boundary

A entrega foi confrontada com os critérios explícitos de `GKR-UX-PER002-MAT-ELIGIBILITY-001`.

| Critério | Resultado |
|---|---|
| representar `PER-002` como responsabilidade existente | PASS |
| não criar novo `PER-ID` para autenticação/continuação | PASS |
| permitir gate de autenticação condicional/já satisfeito | PASS |
| autenticação ≠ autorização de processamento | PASS |
| preservar retorno, interrupção, recusa e reversibilidade | PASS |
| não forçar login existente ao onboarding de primeira entrada | PASS |
| não antecipar `PER-003`, `PER-008` ou outra responsabilidade downstream | PASS |
| não restaurar materialização histórica como fonte de verdade | PASS |
| manter `TRN-001/002` em suas maturidades vigentes | PASS |
| permanecer low-fidelity / funcional | PASS |

```text
BOUNDARY ACCEPTANCE
→ 10 / 10 PASS
```

## 6. Requisitos funcionais mínimos

A validação também verificou os doze requisitos mínimos congelados para Design:

1. saída inequívoca da Home pública — PASS;
2. explicação anterior a autenticação/dados adicionais — PASS;
3. alternativas legítimas antes do avanço — PASS;
4. autenticação/criação/recuperação como gate — PASS;
5. continuação autenticada após o gate — PASS;
6. finalidades, privacidade, controles e reversibilidade — PASS;
7. distinção autenticar × autorizar processamento — PASS;
8. condição compreensível de `HANDOFF READY` — PASS;
9. `PER-003` somente como destino downstream — PASS;
10. retorno/cancelamento/interrupção/erro/recuperação sem aprisionamento — PASS;
11. preservação de login resumptivo — PASS;
12. independência de aparência histórica removida — PASS.

```text
MINIMUM FUNCTIONAL REQUIREMENTS
→ 12 / 12 PASS
```

## 7. Invariantes preservados

```text
AUTHENTICATION
→ INTERNAL GATE / STATE WITHIN PER-002

AUTHENTICATION COMPLETED
≠ PER-002 COMPLETED

LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION

PER-002 COMPLETION
→ LEGITIMATE HANDOFF TO PER-003

PER-003
→ DOWNSTREAM DESTINATION ONLY

PER-008
→ DOWNSTREAM
→ NOT FIRST AUTHENTICATED RESPONSIBILITY
```

O caminho de relação existente permanece separado:

```text
HOME
→ LOGIN
→ AUTHENTICATION
→ RECOVER / RESUME LEGITIMATE EXISTING STATE
```

## 8. Privacidade, autonomia e reversibilidade

A entrega preserva:

- nenhuma coleta material iniciada pelo simples ato de entrar;
- ausência de consentimento omnibus;
- ausência de checkbox pré-selecionado;
- alternativa de não prosseguir;
- possibilidade de voltar/interromper;
- alternativa sem personalização quando aplicável;
- autenticação separada de autorização de processamento;
- proteção contra exposição indevida de existência de conta em recuperação;
- ausência de urgência artificial ou coerção.

A validação é funcional. Ela não comprova acessibilidade real, segurança técnica, usabilidade com participantes, conformidade operacional ou implementação.

## 9. Nota anti-regressão N1 — compreensão

O Frame 04 representa a precondição de handoff com a linha `ambiente protegido compreendido`.

Essa representação é aceita em baixa fidelidade, desde que qualquer estágio posterior preserve:

```text
DISPLAYED
≠ UNDERSTOOD

SCROLLED
≠ UNDERSTOOD

TIME ON SCREEN
≠ UNDERSTOOD

AUTHENTICATED
≠ UNDERSTOOD
```

A UI futura não pode inferir compreensão exclusivamente por visualização, tempo, scroll, autenticação ou navegação passiva.

## 10. Nota anti-regressão N2 — finalidades específicas

No Frame 03, a working copy informa que finalidades concretas serão apresentadas no momento em que cada uso material for solicitado.

Essa formulação é funcionalmente aceitável neste boundary porque `PER-002` não inicia relato ou processamento material.

Permanece obrigatório:

```text
GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION

EACH MATERIAL USE
→ REQUIRES APPLICABLE PURPOSE DISCLOSURE
→ REQUIRES APPLICABLE CONTROL / AUTHORIZATION
→ BEFORE THE CORRESPONDING MATERIAL PROCESSING
```

## 11. Evidência histórica

A validação não restaura nem promove materializações removidas.

```text
UXA-034 HISTORICAL VISUAL PRODUCER
→ NOT RESTORED
→ NOT CURRENT VISUAL BASELINE

UXA-035
→ MAY INFORM FUNCTIONAL / ANTI-REGRESSION READING
→ DOES NOT DEFINE CURRENT APPEARANCE
```

## 12. Maturidade resultante

A entrega low-fidelity passa a poder ser tratada como **referência corrente de Design funcionalmente validada de `PER-002`**, exclusivamente no boundary validado.

```text
CURRENT FUNCTIONALLY VALIDATED LOW-FIDELITY DESIGN REFERENCE
→ GKR-UX-PER002-DESIGN-DELIVERY-001 v0.1.0
→ VALIDATED BY GKR-UX-PER002-DESIGN-VALIDATION-001 v1.0.0

DESIGN DELIVERY
→ REMAINS NON-NORMATIVE

FUNCTIONAL VALIDATION
→ PASS

AGGREGATE VISUAL WIREFRAME MATURITY
→ NOT_CERTIFIED
```

Essa classificação não transforma o artefato de Design em autoridade funcional normativa. As autoridades funcionais correntes continuam prevalecendo.

## 13. Transições

```text
TRN-001
→ PARTIAL
→ UNCHANGED

TRN-002
→ LOCALLY VALIDATED
→ UNCHANGED

THIS VALIDATION
≠ TRN-001 PROMOTION
≠ TRN-002 PROMOTION
```

## 14. Limites do PASS

O `PASS` não autoriza por si só:

- high-fidelity UI;
- protótipo interativo;
- Source Lock visual;
- `UXA-102/V5`;
- materialização detalhada de `PER-003`;
- materialização de `PER-008` sob Q;
- Design das Homes;
- Product Engineering;
- implementação;
- produção;
- operação;
- merge da PR #363.

## 15. Resultado final

```text
PER-002 LOW-FIDELITY FUNCTIONAL VALIDATION
→ PASS

AUTHORIZED COVERAGE
→ 7 / 7 PASS

BOUNDARY ACCEPTANCE
→ 10 / 10 PASS

MINIMUM FUNCTIONAL REQUIREMENTS
→ 12 / 12 PASS

MATERIAL FINDINGS
→ 0

BLOCKING FINDINGS
→ 0

ANTI-REGRESSION NOTES
→ N1 / N2
→ NON-BLOCKING

REFORMULATION REQUIRED
→ NO
```

O próximo movimento deve ser decidido por gate próprio; esta validação não executa nem autoriza automaticamente estágio posterior.
