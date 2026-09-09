---
id: GKR-UX-PER002-PROTOTYPE-VALIDATION-001
title: PER-002 — Validação Governada do Protótipo Interativo de Design
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-09
normative: false
maturity: interactive_prototype_validation_pass
depends_on:
  - GKR-UX-PER002-PROTOTYPE-DELIVERY-001
  - GKR-UX-PER002-PROTOTYPE-AUTH-001
  - GKR-UX-PER002-PROTOTYPE-ELIGIBILITY-001
  - GKR-UX-PER002-HIFI-VALIDATION-001
  - GKR-UX-PER002-HIFI-DELIVERY-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - UXA-020
  - UXA-023
related:
  - GKR-STATE-001
  - PER-002
  - PER-003
  - PER-008
  - TRN-001
  - TRN-002
---

# PER-002 — Validação Governada do Protótipo Interativo de Design

## 1. Finalidade

Esta autoridade registra a validação governada e separada da entrega `GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0` e do artefato `docs/assets/prototypes/per-002-interactive-prototype.html`.

A validação verifica somente se o protótipo executado permanece dentro do boundary funcional congelado de `PER-002 — Entrada protegida`, preserva a referência high-fidelity validada e torna inspecionáveis os caminhos autorizados sem converter Design em implementação.

```text
PROTOTYPE EXECUTION
→ EXECUTED

PROTOTYPE VALIDATION
→ PERFORMED AS SEPARATE GOVERNED ACT

VALIDATION NATURE
→ STATIC / INTERACTION-LOGIC / DESIGN-INSPECTION REVIEW
→ NO HUMAN-SUBJECT TEST
→ NO PRODUCTION CERTIFICATION
```

## 2. Resultado

```text
PER-002 INTERACTIVE PROTOTYPE VALIDATION
→ PASS

TARGET
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0
→ docs/assets/prototypes/per-002-interactive-prototype.html

VALIDATION CRITERIA
→ 16 / 16 PASS

MATERIAL FINDINGS
→ 0

BLOCKING FINDINGS
→ 0

REFORMULATION REQUIRED
→ NO
```

O `PASS` vale exclusivamente para o protótipo como artefato interativo de inspeção de Design. Não constitui validação de produto implementado, autenticação real, segurança operacional, acessibilidade de produção, usabilidade com pessoas, consentimento, processamento, PMF ou prontidão de Engineering.

## 3. Matriz de validação

| Critério | Resultado | Evidência principal |
|---|---|---|
| `PER-002` permanece a única responsabilidade materializada | PASS | quatro frames + três variantes dentro do mesmo shell |
| 7/7 áreas autorizadas possuem representação interativa | PASS | Frames 01–04 + Variantes A/B/C |
| progressão principal é clicavelmente inspecionável | PASS | Frame 01 → Frame 02 → Frame 03 → Frame 04 |
| sessão já autenticada permanece caminho resumptivo | PASS | `data-session` → Frame 03 com status `Sessão ativa` |
| recuperação/restrição/falha possui retorno e alternativas | PASS | Variante B + retry/recovery/back/explore |
| sair/interromper/explorar sem personalização permanece reversível | PASS | dialog de alternativas + retorno ao protótipo |
| N1 — interação exibida/concluída não prova compreensão | PASS | aviso explícito no dialog informativo e readiness factual |
| N2 — autenticação/click não autoriza processamento futuro | PASS | copy de Frames 01–03 + ausência de consentimento omnibus |
| `PER-003` permanece apenas handoff | PASS | boundary dedicado sem modalidades internas de `PER-003` |
| `PER-008`/novo `PER-ID` não são antecipados | PASS | ausência de materialização downstream adicional |
| foco visível e acesso por teclado são representados | PASS | `:focus-visible`, controles nativos e foco de mudança de estado |
| comportamento responsivo preserva ordem semântica | PASS | coluna única + breakpoint mobile sem reordenação funcional |
| alternativas não dependem de hover/cor e não há dark pattern material | PASS | ações textuais/botões explícitos + mensagens textuais |
| dados são sintéticos e não há rede/persistência/analytics | PASS | HTML autocontido; sem fetch/XHR/storage/cookies/telemetria |
| maturidade de `TRN-001`/`TRN-002` não é promovida | PASS | handoff simulado explicitamente não promocional |
| Source Lock, UXA-102/V5, Engineering e produção permanecem fora do escopo | PASS | entrega + artefato + boundary final |

```text
VALIDATION CRITERIA
→ 16 / 16 PASS
```

## 4. Cobertura interativa

A cobertura observada é:

```text
FRAME 01 — ORIENTAÇÃO PROTEGIDA / PRÉ-AUTH
→ PASS
→ CONTINUAR / COMO FUNCIONA / EXPLORAR / HOME

FRAME 02 — GATE DE ACESSO
→ PASS
→ ENTRAR / CRIAR CONTA COMO MODOS SIMULADOS
→ IDENTIFICAÇÃO / CREDENCIAL COMO SLOTS FUNCIONAIS
→ CONTINUAR / RECUPERAR / VOLTAR / EXPLORAR

VARIANTE A — SESSÃO JÁ AUTENTICADA
→ PASS
→ FRAME 02 PODE SER OMITIDO
→ FRAME 03 EXIBE `SESSÃO ATIVA`

VARIANTE B — RECUPERAÇÃO / RESTRIÇÃO / FALHA
→ PASS
→ TRY AGAIN / RECOVERY / ALTERNATIVE ACCESS / BACK / EXPLORE

FRAME 03 — CONTINUAÇÃO AUTENTICADA / CONTROLES
→ PASS
→ CONTROLES / PRIVACIDADE / SAÍDA / EXPLORAÇÃO

VARIANTE C — SAIR / INTERROMPER / EXPLORAR SEM PERSONALIZAÇÃO
→ PASS
→ DIALOG / BOTTOM-SHEET RESPONSIVE REPRESENTATION
→ EXPLORE / HOME / PAUSE / RETURN

FRAME 04 — HANDOFF READY
→ PASS
→ READINESS FACTUAL
→ REVIEW / EXIT / HANDOFF

PER-003 BOUNDARY
→ PASS
→ STOP POINT ONLY
→ NO INTERNAL PER-003 CONTENT
```

```text
AUTHORIZED COVERAGE
→ 7 / 7 PASS

COVERAGE
≠ 7 NEW SCREENS
≠ 7 NEW SURFACES
```

## 5. N1 — compreensão não inferida

O protótipo não usa clique, avanço, autenticação simulada ou conclusão como prova de compreensão.

O dialog informativo contém a ação de interface `Entendi o que foi apresentado`, acompanhada de nota explícita de que essa ação não constitui prova de compreensão humana.

O Frame 04 registra somente fatos de interface:

- contexto apresentado;
- acesso concluído ou já válido em nível simulado;
- controles e alternativas apresentados;
- nenhum relato solicitado nesta etapa.

```text
DISPLAYED
≠ UNDERSTOOD

CLICKED
≠ UNDERSTOOD

COMPLETED INTERACTION
≠ UNDERSTOOD

N1
→ PASS
```

## 6. N2 — finalidade, autenticação e processamento

O protótipo preserva repetidamente que entrar/criar conta não autoriza análise nem personalização e que cada uso material futuro exige finalidade e explicação aplicáveis antes do processamento correspondente.

Não existem:

- checkbox de consentimento omnibus;
- autorização pré-selecionada;
- `Aceito tudo`;
- processamento desencadeado por clique;
- persistência técnica de autorização;
- interpretação de credencial como consentimento.

```text
PROTOTYPE CLICK
≠ REAL CONSENT
≠ REAL DATA AUTHORIZATION

AUTHENTICATION SIMULATION
≠ MATERIAL PROCESSING AUTHORIZATION

N2
→ PASS
```

## 7. Autonomia e reversibilidade

Os caminhos de não continuidade permanecem alcançáveis nos estados aplicáveis:

- voltar;
- recuperar acesso;
- tentar novamente;
- usar outra forma de acesso, se disponível;
- explorar sem personalização;
- voltar para a Home;
- pausar por agora;
- sair por agora;
- retornar à entrada protegida.

Nenhum caminho de saída é bloqueado por estado `disabled`, countdown, urgência artificial ou penalização visual material.

```text
AUTONOMY / REVERSIBILITY
→ PASS

DARK PATTERN MATERIAL FINDING
→ NONE
```

## 8. Teclado, foco e semântica de interação

O artefato representa:

- elementos `button` e `input` nativos;
- anel `focus-visible` de 3 px com offset;
- labels persistentes para os slots funcionais;
- dialogs nativos para informação e alternativas;
- anúncio de mudança de estado por região `aria-live`;
- foco programático no primeiro elemento relevante após mudança de estado;
- mensagens de erro textuais, não somente cromáticas.

```text
KEYBOARD / FOCUS REPRESENTATION
→ PASS AT PROTOTYPE INSPECTION LEVEL

PASS
≠ WCAG PRODUCTION CERTIFICATION
≠ ASSISTIVE-TECH FIELD TEST
```

A alternância `Entrar / Criar conta` permanece acessível por controles de botão no fluxo de teclado do protótipo. Esta validação não transforma a representação em componente de produção certificado.

## 9. Responsividade

O CSS preserva a coluna semântica e modifica apenas apresentação local em viewport estreito. A Variante C usa `dialog` central em telas maiores e representação inferior em mobile, sem criar nova superfície.

```text
RESPONSIVE BEHAVIOR
→ PASS AT DESIGN-PROTOTYPE LEVEL

SEMANTIC ORDER
→ PRESERVED

RIGHTS / ALTERNATIVES
→ PRESERVED
```

## 10. Dados e tecnologia

A inspeção do artefato não encontrou dependências externas nem mecanismos de comunicação/persistência.

```text
CONTENT
→ SYNTHETIC / FICTIONAL / DESIGN-SAFE

NETWORK
→ NONE

BACKEND
→ NONE

FETCH / XHR
→ NONE

LOCALSTORAGE / SESSIONSTORAGE / COOKIE WRITE
→ NONE

ANALYTICS / TELEMETRY
→ NONE

REAL CREDENTIAL VALIDATION
→ NONE
```

HTML/CSS/JavaScript continuam classificados somente como mecanismo da entrega de prototipação e não como escolha de stack de Product Engineering.

## 11. Handoff e maturidade de transições

O CTA final leva somente a uma parada de boundary explicitamente identificada como `PER-003` fora do escopo.

```text
TRN-002 CLICKABLE REPRESENTATION
→ PRESENT

PER-003 INTERNAL MODALITIES / STATES
→ NOT MATERIALIZED

TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

PROTOTYPE VALIDATION
≠ TRANSITION MATURITY PROMOTION
```

## 12. Findings

```text
MATERIAL FINDINGS
→ 0

BLOCKING FINDINGS
→ 0

NON-BLOCKING REFORMULATION REQUIRED
→ NO
```

A validação não identifica regressão material que exija nova execução antes do fechamento deste gate.

## 13. Limites do PASS

Este `PASS` não autoriza nem comprova:

- Source Lock;
- `UXA-102/V5`;
- Product Engineering;
- implementação;
- backend;
- autenticação real;
- sessão real;
- persistência;
- dados reais;
- segurança operacional;
- acessibilidade de produção;
- teste com participantes reais;
- PMF;
- produção;
- operação;
- merge da PR #363.

## 14. Estado após validação

```text
PER-002 INTERACTIVE PROTOTYPE EXECUTION
→ EXECUTED
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0

PER-002 INTERACTIVE PROTOTYPE VALIDATION
→ PASS
→ GKR-UX-PER002-PROTOTYPE-VALIDATION-001 v1.0.0
→ 16 / 16 CRITERIA PASS
→ MATERIAL FINDINGS = 0
→ BLOCKING FINDINGS = 0
→ REFORMULATION REQUIRED = NO

CURRENT PER-002 INTERACTIVE DESIGN REFERENCE
→ DELIVERY v0.1.0 + VALIDATION v1.0.0

SOURCE LOCK
→ NOT_CREATED
→ NOT_REQUIRED BY CURRENT EVIDENCE
→ NOT_AUTHORIZED BY INFERENCE

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

IMPLEMENTATION / PRODUCTION
→ NOT_AUTHORIZED

PR #363 MERGE
→ NOT_AUTHORIZED
```

## 15. Próximo limite legítimo

A cadeia autorizada de Design de `PER-002` alcança neste ponto uma referência interativa validada. Nenhum próximo estágio é liberado automaticamente.

```text
PER-002 DESIGN / PROTOTYPE CHAIN
→ LOW-FIDELITY VALIDATED
→ HIGH-FIDELITY VALIDATED
→ INTERACTIVE PROTOTYPE VALIDATED

SOURCE LOCK
→ NOT WARRANTED BY CURRENT EVIDENCE
→ REQUIRES OWN PURPOSE / AUTHORITY IF EVER NEEDED

UXA-102 / V5
→ NOT_STARTED
→ REQUIRES SEPARATE GOVERNED RELEASE

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
→ REQUIRES SEPARATE GOVERNED RELEASE

NEXT AUTOMATIC EXECUTION
→ NONE
```

O fechamento deste validator encerra somente a validação governada do protótipo interativo de `PER-002`; fases posteriores exigem autoridade própria.