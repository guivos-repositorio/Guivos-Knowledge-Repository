---
id: GKR-UX-PER002-PROTOTYPE-DELIVERY-001
title: PER-002 — Entrega do Protótipo Interativo de Design
status: active
version: 0.1.0
owner: Design Guivos
last_updated: 2026-09-09
normative: false
maturity: interactive_prototype_delivery_pending_validation
depends_on:
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

# PER-002 — Entrega do Protótipo Interativo de Design

## 1. Finalidade da entrega

Esta entrega executa a autorização `GKR-UX-PER002-PROTOTYPE-AUTH-001 v1.0.0` exclusivamente para um **protótipo interativo de Design de `PER-002 — Entrada protegida`**.

O protótipo torna clicavelmente inspecionáveis os estados, variantes, alternativas e o handoff já definidos e validados na referência high-fidelity, sem redescobrir arquitetura funcional e sem presumir implementação.

```text
INTERACTIVE PROTOTYPE AUTHORIZATION
→ GRANTED

INTERACTIVE PROTOTYPE EXECUTION
→ EXECUTED
→ PER-002 ONLY
→ SIMULATED INTERACTION ONLY

DELIVERY
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0

PROTOTYPE VALIDATION
→ PENDING
→ NOT_PERFORMED_BY_THIS_DELIVERY
```

Esta entrega é **não normativa**. Ela não substitui as autoridades funcionais correntes e não constitui produto implementado, UI de produção, teste com pessoas ou evidência de compreensão humana.

## 2. Artefato entregue

```text
ARTIFACT
→ docs/assets/prototypes/per-002-interactive-prototype.html

FORMAT
→ SELF-CONTAINED HTML / CSS / JAVASCRIPT

NATURE
→ DESIGN INSPECTION ARTIFACT
→ STATIC CLIENT-SIDE SIMULATION
→ NO EXTERNAL DEPENDENCIES REQUIRED

CONTENT
→ SYNTHETIC / FICTIONAL / DESIGN-SAFE

NETWORK REQUESTS
→ NONE BY DESIGN

BACKEND
→ NONE

PERSISTENCE
→ NONE

ANALYTICS / TELEMETRY
→ NONE
```

O uso de HTML/CSS/JavaScript nesta entrega é somente um meio de prototipação interativa de Design. Não representa escolha de stack de Product Engineering nem implementação de autenticação, sessão, autorização, dados ou produto.

## 3. Boundary funcional preservado

A composição permanece exatamente dentro do boundary autorizado:

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
4 PRIMARY FRAMES + 3 VARIANTS
→ 7 / 7 AUTHORIZED COVERAGE AREAS REPRESENTED

7 COVERAGE AREAS
≠ 7 NEW SCREENS
≠ 7 NEW SURFACES
```

Nenhuma nova superfície canônica e nenhum novo `PER-ID` são criados.

## 4. Referência visual consumida

O protótipo consome a referência funcionalmente validada:

```text
CURRENT FUNCTIONALLY VALIDATED HIGH-FIDELITY DESIGN REFERENCE
→ GKR-UX-PER002-HIFI-DELIVERY-001 v0.1.0
+
→ GKR-UX-PER002-HIFI-VALIDATION-001 v1.0.0
```

Foram mantidos no artefato:

- direção mobile-first;
- coluna central de até aproximadamente 560 px em viewports maiores;
- working copy high-fidelity de `PER-002`;
- tokens cromáticos locais da entrega high-fidelity;
- tipografia local `Inter` com fallbacks de sistema;
- alvos interativos mínimos projetados de 44 × 44 px;
- controles primários com 52 px de altura;
- foco visível;
- cards informativos de baixo contraste;
- erro contextual sem transformar toda a superfície em estado de ameaça;
- alternativas visíveis e não subordinadas por coerção visual.

```text
LOCAL DESIGN TOKENS
→ CONSUMED FOR PROTOTYPE INSPECTION
→ NOT PROMOTED TO GLOBAL DESIGN SYSTEM
```

## 5. Frame 01 — Orientação protegida / pré-auth

O Frame 01 materializa interativamente:

```text
EYEBROW
→ Antes de começar

H1
→ Saiba o que muda ao entrar.

PRIMARY
→ Continuar
→ FRAME 02

SECONDARY
→ Como funciona
→ INFORMATION DIALOG WITHIN PER-002

ALTERNATIVES
→ Explorar sem personalização
→ Voltar para a Home
```

A ação `Como funciona` abre explicação contextual dentro do próprio artefato, sem criar nova superfície canônica.

`Explorar sem personalização` e `Voltar para a Home` preservam alternativas legítimas e desembocam apenas em placeholders de boundary, porque seus destinos não pertencem à materialização autorizada de `PER-002`.

## 6. Frame 02 — Gate de acesso simulado

O Frame 02 representa:

```text
ACCESS MODES
→ Entrar
→ Criar conta

FUNCTIONAL SLOTS
→ Identificação
→ Credencial

PRIMARY
→ Continuar
→ SIMULATED AUTHENTICATED CONTINUATION

RECOVERY
→ Recuperar acesso
→ VARIANTE B

ALTERNATIVES
→ Voltar
→ Explorar sem personalização
```

Os campos são explicitamente rotulados como funcionais/simulados. O artefato não define tecnologia real de identificação ou credencial.

```text
IDENTIFICAÇÃO SLOT
≠ EMAIL DECISION
≠ PHONE DECISION
≠ USERNAME DECISION

CREDENCIAL SLOT
≠ PASSWORD DECISION
≠ PASSKEY DECISION
≠ BIOMETRIC DECISION

CONTINUE CLICK
→ LOCAL UI STATE CHANGE ONLY
→ NO AUTHENTICATION REQUEST
→ NO SESSION CREATION
```

## 7. Variante A — Sessão já autenticada

A variante é inspecionável por um controle de Design explicitamente identificado como simulação.

Quando acionada:

- o Frame 02 é funcionalmente omitido;
- o Frame 03 recebe o status textual `Sessão ativa`;
- a support copy da referência high-fidelity é apresentada;
- nenhuma tela de celebração, confirmação de consentimento ou “login concluído” é criada.

```text
SIMULATED ACTIVE SESSION
≠ REAL SESSION
≠ SESSION IMPLEMENTATION
≠ PROOF OF AUTHENTICATION
```

## 8. Variante B — Recuperação / restrição / falha

A variante é acionável pelo caminho `Recuperar acesso` ou pelo controle de inspeção de falha.

Ela apresenta:

```text
H1
→ Não foi possível concluir o acesso.

ERROR CARD
→ Não conseguimos concluir esta etapa.
→ Revise os dados ou use uma opção de recuperação disponível.

PRIMARY
→ Tentar novamente

ALTERNATIVES
→ Recuperar acesso
→ Usar outra forma de acesso, se disponível
→ Voltar à entrada protegida
→ Explorar sem personalização
```

A simulação não verifica se uma identificação possui conta, não consulta qualquer serviço e não expõe motivo sensível de restrição.

## 9. Frame 03 — Continuação autenticada / controles

O Frame 03 torna inspecionáveis os três controles high-fidelity:

1. `O que você compartilha — Só quando você decidir.`;
2. `Como pode ser usado — Cada uso relevante deverá ser explicado antes de acontecer.`;
3. `Seus controles — Revisar, corrigir, limitar, retirar ou interromper quando aplicável.`.

Também preserva explicitamente:

```text
ENTRAR
≠ AUTHORIZATION TO PROCESS

GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION

PROTOTYPE CLICK
≠ REAL CONSENT
≠ REAL DATA AUTHORIZATION
```

A ação `Ver detalhes de privacidade` abre apenas uma explicação contextual dentro de `PER-002`; ela não cria consentimento omnibus, checkbox de autorização ou nova superfície.

## 10. Variante C — Sair / interromper / explorar sem personalização

A variante é representada como `dialog` responsivo:

- visualmente equivalente a bottom sheet em viewport mobile;
- dialog central em viewport maior;
- mesma árvore semântica e mesmas alternativas.

Ações representadas:

```text
Explorar sem personalização
Voltar para a Home
Pausar por agora
Continuar na entrada protegida
```

Os três primeiros caminhos conduzem apenas a uma parada de boundary explicativa, sem implementar seus destinos.

```text
PAUSAR POR AGORA
→ SIMULATED INTERRUPTION INTENT
→ NO PERSISTENCE SEMANTICS
→ NO SAVE / RESUME IMPLEMENTATION
```

## 11. Frame 04 — Handoff ready

O Frame 04 preserva a correção N1 e usa somente fatos observáveis de interface:

```text
H1
→ Sua entrada está preparada.

READINESS
→ Contexto da entrada apresentado
→ Acesso concluído ou já válido
→ Controles e alternativas apresentados
→ Nenhum relato é solicitado nesta etapa

PRIMARY CTA
→ Escolher como quero começar

HANDOFF LABEL
→ Próximo: escolha de modalidade
```

```text
DISPLAYED
≠ UNDERSTOOD

CLICKED
≠ UNDERSTOOD

COMPLETED INTERACTION
≠ UNDERSTOOD
```

A working copy não declara que a Pessoa compreendeu, consentiu ou autorizou uso futuro.

## 12. Handoff para `PER-003`

O CTA final leva somente a uma **parada explícita de boundary**:

```text
TRN-002
→ REPRESENTED AS HANDOFF

PER-003
→ NAMED AS NEXT DESTINATION
→ INTERNAL CONTENT NOT MATERIALIZED

TEXT / VOICE / FILE / OTHER MODALITIES
→ NOT DESIGNED HERE
→ NOT PROTOTYPED HERE
```

A parada informa que o protótipo terminou e oferece somente retorno ao `HANDOFF READY`.

```text
SHOW HANDOFF TO PER-003
≠ DESIGN PER-003
≠ PROTOTYPE PER-003
```

## 13. N1 — compreensão não inferida

O artefato inclui nota explícita também no dialog informativo:

```text
INTERFACE ACKNOWLEDGEMENT
→ ACTION IN PROTOTYPE ONLY
→ NOT HUMAN UNDERSTANDING EVIDENCE
```

Nenhum clique, navegação, foco, preenchimento simulado ou conclusão é gravado ou tratado como evidência de compreensão.

## 14. N2 — finalidade e processamento

O protótipo não inclui:

- `Aceito tudo`;
- consentimento omnibus;
- checkbox pré-selecionado;
- autorização de processamento;
- solicitação de relato pessoal;
- upload;
- gravação;
- coleta de dado material;
- persistência de preferências.

```text
LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION
```

## 15. Dados, rede e persistência

O artefato foi deliberadamente construído sem dependência de rede e sem armazenamento.

```text
REAL PERSONAL DATA
→ NOT REQUIRED
→ NOT AUTHORIZED

REAL CREDENTIALS
→ NOT REQUIRED
→ NOT AUTHORIZED

FETCH / XHR / WEBSOCKET
→ NOT USED

LOCALSTORAGE / SESSIONSTORAGE / COOKIE
→ NOT USED

BACKEND / API
→ NOT USED

ANALYTICS / TELEMETRY
→ NOT USED
```

Campos de entrada existem apenas para inspeção visual/teclado do gate simulado. Seu conteúdo permanece somente no DOM corrente da página enquanto aberta e não é transmitido ou persistido pelo artefato.

## 16. Acessibilidade representada

A entrega torna inspecionáveis, em nível de protótipo:

- headings semânticos;
- labels persistentes dos campos;
- foco `:focus-visible` de 3 px com offset de 2 px;
- alvos interativos mínimos projetados;
- status textual além da cor;
- erro com texto além da cor;
- dialogs nativos com labels;
- região `aria-live` para mudanças de estado simuladas;
- alternativas alcançáveis sem hover;
- ordem de leitura compatível com a ordem visual;
- layout responsivo sem esconder direitos ou alternativas.

```text
PROTOTYPE ACCESSIBILITY REPRESENTATION
≠ ACCESSIBILITY VALIDATION
≠ WCAG CERTIFICATION
≠ PRODUCTION ACCESSIBILITY TEST
```

A verificação desses requisitos pertence ao gate posterior de validação do protótipo.

## 17. Responsividade representada

A composição usa uma única ordem semântica responsiva:

```text
MOBILE
→ SINGLE COLUMN / COMPACT PADDING

TABLET / DESKTOP
→ CENTERED COLUMN / MAX WIDTH APPROX. 560 PX

VARIANTE C
→ BOTTOM-SHEET-LIKE ON MOBILE
→ CENTERED DIALOG ON LARGER VIEWPORTS
```

Nenhum breakpoint altera responsabilidade funcional, direitos, alternativas ou destino de handoff.

## 18. Mapa de interações

| Origem | Ação simulada | Destino/resultado | Boundary |
|---|---|---|---|
| Frame 01 | Continuar | Frame 02 | dentro de `PER-002` |
| Frame 01 | Como funciona | dialog informativo | dentro de `PER-002` |
| Frame 01 | Explorar sem personalização | Variante C / parada | destino não materializado |
| Frame 01 | Voltar para a Home | parada | Home não materializada |
| Frame 02 | Entrar / Criar conta | troca visual de modo | sem tecnologia real |
| Frame 02 | Continuar | Frame 03 | autenticação simulada |
| Frame 02 | Recuperar acesso | Variante B | recuperação simulada |
| Frame 02 | Simular sessão já ativa | Frame 03 + Variante A | sessão simulada |
| Variante B | Tentar novamente | Frame 02 | sem consulta real |
| Frame 03 | Continuar | Frame 04 | dentro de `PER-002` |
| Frame 03 | Ver detalhes de privacidade | dialog informativo | sem consentimento real |
| Frame 03 | Sair / explorar | Variante C | alternativa preservada |
| Variante C | Continuar na entrada protegida | fecha dialog | retorna ao estado corrente |
| Variante C | Sair / Home / pausar | parada de boundary | destino não materializado |
| Frame 04 | Revisar privacidade e controles | Frame 03 | reversível |
| Frame 04 | Escolher como quero começar | parada `PER-003` | handoff somente |
| Parada `PER-003` | Voltar | Frame 04 | conteúdo de `PER-003` ausente |

## 19. Cobertura da execução

| Área autorizada | Protótipo | Evidência |
|---|---|---|
| orientação protegida / pré-auth | representada | Frame 01 |
| autenticação quando necessária | representada | Frame 02 |
| sessão já autenticada | representada | Variante A |
| continuação autenticada / controles | representada | Frame 03 |
| recuperação / restrição / falha | representada | Variante B |
| sair / interromper / explorar sem personalização | representada | Variante C |
| handoff legítimo | representado | Frame 04 + parada `PER-003` |

```text
AUTHORIZED COVERAGE
→ 7 / 7 REPRESENTED IN EXECUTED ARTIFACT

COVERAGE CLAIM
→ DELIVERY INVENTORY ONLY
→ NOT VALIDATION PASS
```

## 20. Autonomia e ausência de coerção

A execução mantém disponíveis, conforme o estado:

- voltar;
- sair;
- interromper;
- recuperar acesso;
- explorar sem personalização;
- continuar na entrada protegida;
- revisar controles antes do handoff.

Não foram introduzidos:

- urgência artificial;
- countdown;
- pré-seleção de autorização;
- punição visual de recusa;
- disabled state para coagir continuidade;
- celebração de autenticação como consentimento;
- ocultação de alternativa legítima.

```text
PROTOTYPE EXECUTION
≠ DARK PATTERN AUTHORIZATION
```

## 21. Tecnologia não decidida

Esta entrega não decide:

- e-mail, telefone ou username;
- senha, passkey ou biometria;
- provedor social/externo;
- IdP;
- backend;
- modelo de sessão;
- storage;
- API;
- política técnica de recuperação;
- arquitetura de autorização;
- telemetria;
- analytics;
- infraestrutura;
- framework ou stack de Product Engineering.

```text
HTML / CSS / JS PROTOTYPE FORMAT
→ DESIGN DELIVERY MECHANISM ONLY
→ NOT PRODUCT STACK DECISION
```

## 22. Source Lock

```text
SOURCE LOCK
→ NOT_CREATED
→ NOT_REQUIRED BY CURRENT EVIDENCE
→ NOT_AUTHORIZED BY THIS EXECUTION
```

A existência do protótipo não cria Source Lock por inferência.

## 23. UXA-102/V5 e Product Engineering

```text
UXA-102 / V5
→ NOT_STARTED
→ UNCHANGED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
→ UNCHANGED

PROTOTYPE EXECUTION
≠ UXA-102 RELEASE
≠ PRODUCT ENGINEERING RELEASE
≠ IMPLEMENTATION
```

## 24. Transições

```text
TRN-001
→ PARTIAL / UNCHANGED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

INTERACTIVE PROTOTYPE EXECUTION
≠ TRANSITION MATURITY PROMOTION
```

A presença de uma transição simulada clicável não promove sua maturidade.

## 25. Testes com pessoas

Nenhum participante real foi necessário ou autorizado para esta execução.

```text
HUMAN-SUBJECT TEST
→ NOT_PERFORMED
→ NOT_AUTHORIZED BY PROTOTYPE EXECUTION

FIELD RESEARCH
→ NOT_RELEASED BY THIS DELIVERY
```

A entrega não produz evidência de usabilidade humana, compreensão, preferência, PMF ou comportamento real.

## 26. O que esta entrega não é

```text
INTERACTIVE PROTOTYPE DELIVERY
≠ PROTOTYPE VALIDATION
≠ FUNCTIONAL AUTHORITY REPLACEMENT
≠ PRODUCTION UI
≠ IMPLEMENTED PRODUCT
≠ REAL AUTHENTICATION
≠ REAL SESSION
≠ REAL PERSISTENCE
≠ REAL DATA PROCESSING
≠ SOURCE LOCK
≠ HUMAN TEST
≠ PRODUCT ENGINEERING
```

Esta entrega não autoriza:

- `PER-003` além do handoff;
- `PER-008`;
- nova superfície ou novo `PER-ID`;
- Design das Homes;
- Source Lock;
- UXA-102/V5;
- Product Engineering;
- implementação;
- backend;
- autenticação real;
- sessão real;
- persistência real;
- dados reais;
- analytics real;
- telemetria real;
- testes com participantes reais;
- produção;
- operação;
- PMF;
- merge da PR #363.

## 27. Estado após a execução

```text
PER-002 INTERACTIVE PROTOTYPE AUTHORIZATION
→ GRANTED

PER-002 INTERACTIVE PROTOTYPE EXECUTION
→ EXECUTED
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0

INTERACTIVE ARTIFACT
→ docs/assets/prototypes/per-002-interactive-prototype.html

PROTOTYPE VALIDATION
→ PENDING
→ SEPARATE GOVERNED ACT REQUIRED

SOURCE LOCK
→ NOT_CREATED
→ NOT_AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

TRN-001
→ PARTIAL

TRN-002
→ LOCALLY VALIDATED

IMPLEMENTATION / PRODUCTION
→ NOT_AUTHORIZED

PR #363 MERGE
→ NOT_AUTHORIZED
```

## 28. Próximo gate legítimo

O próximo ato legítimo é uma **validação governada e separada do protótipo interativo executado**.

```text
NEXT
→ PER-002 INTERACTIVE PROTOTYPE VALIDATION

VALIDATION TARGET
→ GKR-UX-PER002-PROTOTYPE-DELIVERY-001 v0.1.0
→ docs/assets/prototypes/per-002-interactive-prototype.html

MUST CHECK
→ FUNCTIONAL BOUNDARY
→ 7 / 7 COVERAGE
→ INTERACTION PATHS
→ N1 / N2
→ AUTONOMY / REVERSIBILITY
→ KEYBOARD / FOCUS REPRESENTATION
→ RESPONSIVE BEHAVIOR
→ NO DARK PATTERN
→ NO REAL DATA / NETWORK / PERSISTENCE
→ PER-003 HANDOFF ONLY
→ NO TRANSITION MATURITY PROMOTION
→ NO SOURCE LOCK / UXA-102 / ENGINEERING EXPANSION

DO NOT YET
→ CLAIM PROTOTYPE PASS
→ CREATE SOURCE LOCK BY INFERENCE
→ START UXA-102/V5
→ EXPAND TO PER-003
→ RESUME PRODUCT ENGINEERING
→ IMPLEMENT
→ TEST WITH REAL PARTICIPANTS
→ MERGE PR #363
```

Esta entrega encerra somente a execução autorizada do protótipo interativo de Design de `PER-002`. A validação permanece pendente e deverá ocorrer em ato separado.
