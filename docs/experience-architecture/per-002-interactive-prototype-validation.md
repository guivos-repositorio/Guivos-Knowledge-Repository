---
id: GKR-UX-PER002-PROTOTYPE-VALIDATION-001
title: PER-002 — Validação Governada do Protótipo Interativo de Design
status: superseded
version: 1.0.1
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-09
normative: false
maturity: historical_pre_review_interactive_prototype_validation
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
  - GKR-UX-PER002-PROTOTYPE-REVALIDATION-001
  - GKR-STATE-001
  - PER-002
  - PER-003
  - PER-008
  - TRN-001
  - TRN-002
---

# PER-002 — Validação Governada do Protótipo Interativo de Design

## 1. Finalidade

Esta autoridade preserva como evidência histórica o ato governado de validação da entrega `GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0` e do artefato `docs/assets/prototypes/per-002-interactive-prototype.html` no checkpoint anterior à revisão Codex que posteriormente encontrou dois findings `P2`.

O `PASS` registrado abaixo descreve exclusivamente o resultado daquele ato pré-review. Ele deixou de ser suficiente como fechamento final quando a revisão posterior encontrou regressões de interação e, por isso, esta autoridade foi reclassificada como `superseded`. A conclusão corrente do protótipo é governada por `GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v1.0.0`, após remediação dos findings.

A validação verificou somente se o protótipo executado permanecia dentro do boundary funcional congelado de `PER-002 — Entrada protegida`, preservava a referência high-fidelity validada e tornava inspecionáveis os caminhos autorizados sem converter Design em implementação.

```text
PROTOTYPE EXECUTION
→ EXECUTED

ORIGINAL PROTOTYPE VALIDATION
→ PERFORMED AS SEPARATE GOVERNED ACT
→ HISTORICAL PRE-CODEX-REVIEW EVIDENCE
→ SUPERSEDED AS FINAL CURRENT CLOSURE

CURRENT FINAL CONCLUSION
→ GOVERNED BY GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v1.0.0

VALIDATION NATURE
→ STATIC / INTERACTION-LOGIC / DESIGN-INSPECTION REVIEW
→ NO HUMAN-SUBJECT TEST
→ NO PRODUCTION CERTIFICATION
```

## 2. Resultado histórico do checkpoint pré-review

```text
PER-002 INTERACTIVE PROTOTYPE VALIDATION — PRE-REVIEW CHECKPOINT
→ PASS AT THAT CHECKPOINT

TARGET
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0
→ docs/assets/prototypes/per-002-interactive-prototype.html

VALIDATION CRITERIA
→ 16 / 16 PASS AT THAT CHECKPOINT

MATERIAL FINDINGS OBSERVED BY THIS ACT
→ 0

BLOCKING FINDINGS OBSERVED BY THIS ACT
→ 0

REFORMULATION REQUIRED BY THIS ACT
→ NO

LATER CODEX REVIEW
→ FOUND 2 P2
→ THIS PASS IS NOT THE CURRENT FINAL CLOSURE
```

O `PASS` vale exclusivamente como registro histórico do protótipo inspecionado naquele checkpoint. Não constitui a conclusão corrente pós-review nem validação de produto implementado, autenticação real, segurança operacional, acessibilidade de produção, usabilidade com pessoas, consentimento, processamento, PMF ou prontidão de Engineering.

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
HISTORICAL VALIDATION CRITERIA AT PRE-REVIEW CHECKPOINT
→ 16 / 16 PASS
```

A matriz acima permanece como evidência do ato histórico e não substitui a revalidação pós-review corrente.

## 4. Cobertura interativa

A cobertura observada naquele ato foi:

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
AUTHORIZED COVERAGE OBSERVED AT PRE-REVIEW CHECKPOINT
→ 7 / 7 PASS

COVERAGE
≠ 7 NEW SCREENS
≠ 7 NEW SURFACES
```

## 5. N1 — compreensão não inferida

O protótipo não usava clique, avanço, autenticação simulada ou conclusão como prova de compreensão.

O dialog informativo continha a ação de interface `Entendi o que foi apresentado`, acompanhada de nota explícita de que essa ação não constituía prova de compreensão humana.

O Frame 04 registrava somente fatos de interface:

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
→ PASS AT PRE-REVIEW CHECKPOINT
```

## 6. N2 — finalidade, autenticação e processamento

O protótipo preservava repetidamente que entrar/criar conta não autorizava análise nem personalização e que cada uso material futuro exigia finalidade e explicação aplicáveis antes do processamento correspondente.

Não existiam:

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
→ PASS AT PRE-REVIEW CHECKPOINT
```

## 7. Autonomia e reversibilidade

Os caminhos de não continuidade observados permaneciam alcançáveis nos estados aplicáveis:

- voltar;
- recuperar acesso;
- tentar novamente;
- usar outra forma de acesso, se disponível;
- explorar sem personalização;
- voltar para a Home;
- pausar por agora;
- sair por agora;
- retornar à entrada protegida.

Nenhum caminho de saída era bloqueado por estado `disabled`, countdown, urgência artificial ou penalização visual material.

```text
AUTONOMY / REVERSIBILITY
→ PASS AT PRE-REVIEW CHECKPOINT

DARK PATTERN MATERIAL FINDING OBSERVED BY THIS ACT
→ NONE
```

## 8. Teclado, foco e semântica de interação

O artefato representava:

- elementos `button` e `input` nativos;
- anel `focus-visible` de 3 px com offset;
- labels persistentes para os slots funcionais;
- dialogs nativos para informação e alternativas;
- anúncio de mudança de estado por região `aria-live`;
- foco programático no primeiro elemento relevante após mudança de estado;
- mensagens de erro textuais, não somente cromáticas.

```text
KEYBOARD / FOCUS REPRESENTATION
→ PASS RECORDED AT PRE-REVIEW PROTOTYPE INSPECTION LEVEL
→ LATER CODEX REVIEW IDENTIFIED A P2 IN ACCESS-MODE SEMANTICS
→ REMEDIATION / CURRENT CONCLUSION GOVERNED BY GKR-UX-PER002-PROTOTYPE-REVALIDATION-001

PASS
≠ WCAG PRODUCTION CERTIFICATION
≠ ASSISTIVE-TECH FIELD TEST
```

A alternância `Entrar / Criar conta` foi inicialmente considerada acessível neste ato. A revisão Codex posterior identificou que a semântica anunciada como tabs excedia o comportamento implementado; essa deficiência foi posteriormente remediada e revalidada sob a autoridade pós-review corrente.

## 9. Responsividade

O CSS preservava a coluna semântica e modificava apenas apresentação local em viewport estreito. A Variante C usava `dialog` central em telas maiores e representação inferior em mobile, sem criar nova superfície.

```text
RESPONSIVE BEHAVIOR
→ PASS AT PRE-REVIEW DESIGN-PROTOTYPE LEVEL

SEMANTIC ORDER
→ PRESERVED

RIGHTS / ALTERNATIVES
→ PRESERVED
```

## 10. Dados e tecnologia

A inspeção do artefato naquele checkpoint não encontrou dependências externas nem mecanismos de comunicação/persistência.

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

HTML/CSS/JavaScript continuavam classificados somente como mecanismo da entrega de prototipação e não como escolha de stack de Product Engineering.

## 11. Handoff e maturidade de transições

O CTA final levava somente a uma parada de boundary explicitamente identificada como `PER-003` fora do escopo.

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

## 12. Findings observados neste ato histórico

```text
MATERIAL FINDINGS OBSERVED BY THIS PRE-REVIEW ACT
→ 0

BLOCKING FINDINGS OBSERVED BY THIS PRE-REVIEW ACT
→ 0

NON-BLOCKING REFORMULATION REQUIRED BY THIS PRE-REVIEW ACT
→ NO

LATER CODEX REVIEW
→ 2 P2 IDENTIFIED
→ REMEDIATED AFTER THIS ACT
```

Esta seção não declara ausência corrente de findings após review; a conclusão corrente pertence à revalidação pós-review.

## 13. Limites do PASS histórico

Este `PASS` histórico não autoriza nem comprova:

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

## 14. Estado do ato histórico e deferência corrente

```text
PER-002 INTERACTIVE PROTOTYPE EXECUTION
→ EXECUTED
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0

ORIGINAL PER-002 INTERACTIVE PROTOTYPE VALIDATION ACT
→ GKR-UX-PER002-PROTOTYPE-VALIDATION-001 v1.0.0
→ HISTORICAL PRE-CODEX-REVIEW VALIDATION CHECKPOINT
→ SUPERSEDED AS FINAL CURRENT CLOSURE

CURRENT PUBLISHED HISTORICAL VALIDATION AUTHORITY
→ GKR-UX-PER002-PROTOTYPE-VALIDATION-001 v1.0.1
→ STATUS = SUPERSEDED
→ PRESERVES THE ORIGINAL v1.0.0 ACT AS PROVENANCE

CURRENT PER-002 INTERACTIVE DESIGN REFERENCE
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0
+
→ GKR-UX-PER002-PROTOTYPE-VALIDATION-001 v1.0.1 AS HISTORICAL PRE-REVIEW / SUPERSEDED EVIDENCE
+
→ GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v1.0.0 AS CURRENT POST-REVIEW CONCLUSION

FINAL CURRENT CONCLUSION
→ POST-REVIEW REVALIDATION PASS
→ GOVERNED BY GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v1.0.0

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

Este validator não é mais a autoridade de fechamento corrente da cadeia de protótipo. Ele preserva somente a evidência histórica do checkpoint pré-review e defere integralmente a conclusão atual para `GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v1.0.0`.

```text
THIS AUTHORITY
→ GKR-UX-PER002-PROTOTYPE-VALIDATION-001 v1.0.1
→ HISTORICAL PRE-REVIEW VALIDATION EVIDENCE
→ SUPERSEDED AS FINAL CURRENT CLOSURE

ORIGINAL VALIDATION ACT PRESERVED BY THIS AUTHORITY
→ v1.0.0

CURRENT POST-REVIEW CONCLUSION
→ GKR-UX-PER002-PROTOTYPE-REVALIDATION-001 v1.0.0

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

A preservação deste documento mantém a proveniência do ato inicial sem permitir que ele seja usado para contornar a revalidação pós-review corrente.