---
id: GKR-UX-PER002-HIFI-DELIVERY-001
title: PER-002 — Entrega High-Fidelity de Design
status: active
version: 0.1.0
owner: Design Guivos
last_updated: 2026-09-09
normative: false
maturity: high_fidelity_design_delivery_pending_validation
depends_on:
  - GKR-UX-PER002-HIFI-AUTH-001
  - GKR-UX-PER002-HIFI-ELIGIBILITY-001
  - GKR-UX-PER002-DESIGN-VALIDATION-001
  - GKR-UX-PER002-DESIGN-DELIVERY-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - GKR-UX-HOME-MASTER-001
  - UXA-020
  - UXA-023
related:
  - GKR-STATE-001
  - PER-001
  - PER-002
  - PER-003
  - PER-008
  - TRN-001
  - TRN-002
---

# PER-002 — Entrega High-Fidelity de Design

## 1. Finalidade da entrega

Esta entrega executa a autorização `GKR-UX-PER002-HIFI-AUTH-001 v1.0.0` e refina visualmente, em alta fidelidade de Design, a responsabilidade existente `PER-002 — Entrada protegida`.

Ela consome obrigatoriamente:

- a referência low-fidelity funcionalmente validada `GKR-UX-PER002-DESIGN-DELIVERY-001 v0.1.0` + `GKR-UX-PER002-DESIGN-VALIDATION-001 v1.0.0`;
- o boundary funcional congelado em `GKR-UX-PER002-MAT-ELIGIBILITY-001`;
- as notas anti-regressão `N1` e `N2`;
- a direção institucional vigente da Home principal/Pessoa;
- as autoridades funcionais correntes de Experience Architecture.

```text
HIGH-FIDELITY DESIGN AUTHORIZATION
→ GRANTED

HIGH-FIDELITY DESIGN DELIVERY
→ EXECUTED
→ PER-002 ONLY
→ EXISTING RESPONSIBILITY ONLY

DELIVERY VERSION
→ 0.1.0

HIGH-FIDELITY DESIGN VALIDATION
→ NOT_YET_PERFORMED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

SOURCE LOCK
→ NOT_CREATED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
```

Esta entrega é **não normativa**. Ela governa a proposta visual high-fidelity submetida à validação; não substitui as autoridades funcionais textuais e não constitui UI de produção.

## 2. Boundary preservado

A arquitetura validada permanece inalterada:

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
AUTHENTICATION
→ INTERNAL GATE / STATE WITHIN PER-002

AUTHENTICATION COMPLETED
≠ PER-002 COMPLETED

LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION

EXISTING-RELATIONSHIP LOGIN
→ RESUMPTIVE PATH
→ NOT FORCED INTO FIRST-ENTRY ONBOARDING

PER-003
→ DOWNSTREAM HANDOFF ONLY

PER-008
→ DOWNSTREAM

NEW SURFACE / NEW PER-ID
→ NOT CREATED
```

A alta fidelidade altera tratamento visual, hierarquia, componentes e working copy, mas não altera a arquitetura funcional.

## 3. Direção visual consumida

A direção institucional aplicável permanece:

> **Futuro sem ficção. Tecnologia sem frieza. Sofisticação sem elitismo. Escala sem ruído. Humanidade sem clichê.**

A tradução local para `PER-002` é:

```text
CALMA
→ espaço e baixa densidade visual

CONFIANÇA
→ hierarquia nítida + proteção explicável

FUTURO
→ geometria limpa + acento cromático contemporâneo

HUMANIDADE
→ linguagem direta + ausência de alarmismo

AUTONOMIA
→ alternativas visíveis sem punição visual

PROTEÇÃO
→ sinalização contextual sem estética de ameaça
```

A entrega evita estética de dashboard corporativo, excesso de gradientes, “cyber security”, cadeados dominantes, dramatização de risco e gamificação de consentimento.

## 4. Design System local da entrega

Não existe inferência de Design System global da Guivos. Os tokens abaixo são **locais desta entrega `PER-002`** e permanecem sujeitos à validação posterior.

### 4.1 Cores locais

| Token local | Valor | Uso |
|---|---|---|
| `canvas` | `#F7F8FC` | fundo principal |
| `surface` | `#FFFFFF` | cartões, campos e superfícies elevadas |
| `text-primary` | `#15161A` | títulos e texto principal |
| `text-secondary` | `#626A78` | apoio e explicações |
| `border` | `#E2E6EC` | divisores e contornos |
| `accent` | `#5B5CE2` | CTA primário e foco de marca local |
| `accent-strong` | `#4849C2` | estado pressionado/ênfase |
| `accent-soft` | `#EEF0FF` | status e apoio contextual |
| `focus` | `#7C83FF` | anel de foco visível |
| `success` | `#177A56` | confirmação/status positivo |
| `success-soft` | `#ECF8F3` | fundo de status positivo |
| `danger` | `#B42318` | erro material |
| `danger-soft` | `#FFF1F0` | fundo de erro |

Esses valores não constituem autoridade cromática institucional para outras superfícies.

### 4.2 Tipografia local

```text
WORKING TYPEFACE
→ Inter
→ fallback: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif

DISPLAY / H1 MOBILE
→ 32 / 38
→ weight 600

H2
→ 24 / 30
→ weight 600

BODY
→ 16 / 24
→ weight 400

BODY STRONG
→ 16 / 24
→ weight 600

LABEL
→ 14 / 20
→ weight 600

CAPTION
→ 13 / 18
→ weight 500

BUTTON
→ 16 / 20
→ weight 600
```

A tipografia é decisão local de Design para esta entrega e não substitui eventual sistema tipográfico global futuro.

### 4.3 Escala espacial e geometria

```text
BASE SPACING UNIT
→ 4 px

MOBILE PAGE PADDING
→ 24 px

SECTION GAP
→ 24–32 px

CARD PADDING
→ 20 px

FIELD HEIGHT
→ 52 px

PRIMARY BUTTON HEIGHT
→ 52 px

MINIMUM INTERACTIVE TARGET
→ 44 × 44 px

CARD RADIUS
→ 20 px

CONTROL RADIUS
→ 14 px

PILL RADIUS
→ 999 px

MAX CONTENT WIDTH DESKTOP
→ 560 px
```

Sombras são discretas e usadas apenas quando necessárias para separar superfície de canvas:

```text
shadow-soft
→ 0 8px 30px rgba(21, 22, 26, 0.08)
```

## 5. Estrutura responsiva

A referência primária continua **mobile-first**.

```text
MOBILE REFERENCE
→ 390 × 844

TABLET REFERENCE
→ 768 px viewport

DESKTOP REFERENCE
→ 1440 px viewport
```

Comportamento:

- mobile: conteúdo em coluna única, largura total menos 24 px por lado;
- tablet: conteúdo centralizado, largura máxima aproximada de 560 px;
- desktop: conteúdo centralizado em coluna de 560 px, com canvas respirado e sem sidebar;
- elementos de decisão permanecem na mesma ordem semântica em todas as larguras;
- alternativas não são escondidas em menu secundário apenas para “limpar” a tela;
- nenhum breakpoint altera o boundary funcional.

## 6. Componentes locais

### 6.1 Header de contexto

Composição:

```text
GUIVOS
Entrada protegida
[ícone discreto de proteção contextual]
```

O ícone é apoio semântico, não selo de segurança comprovada.

### 6.2 Status pill

Usos:

- `Entrada protegida`;
- `Sessão ativa`;
- `Acesso não concluído` quando necessário.

Status não deve ser comunicado somente por cor.

### 6.3 Primary action

```text
BACKGROUND
→ accent

TEXT
→ white

HEIGHT
→ 52 px

RADIUS
→ 14 px

WIDTH MOBILE
→ 100%
```

Estados visuais projetados:

- default;
- hover quando aplicável;
- pressed;
- focus-visible;
- disabled apenas quando houver motivo funcional real;
- loading somente como estado visual futuro, sem comportamento implementado nesta entrega.

### 6.4 Secondary action

Botão de superfície branca com borda `border`, texto `text-primary` e mesma altura do primário quando a decisão exigir peso próximo.

### 6.5 Text action

Ações como `Voltar`, `Sair por agora`, `Explorar sem personalização` e `Recuperar acesso` usam affordance textual visível, com área interativa mínima preservada.

### 6.6 Information card

Cartão informativo de fundo `accent-soft` ou neutro, ícone + título curto + explicação. Não utiliza checkbox para comunicar informação.

### 6.7 Error card

Fundo `danger-soft`, texto principal neutro e detalhe/ícone de erro em `danger`. O erro explica o próximo caminho possível sem expor existência de conta ou dado sensível.

## 7. Frame 01 — Orientação protegida / pré-auth

### 7.1 Objetivo

Deixar inequívoco que a Pessoa saiu do ambiente público, explicar o que muda e oferecer alternativas antes de solicitar autenticação.

### 7.2 Hierarquia high-fidelity

```text
HEADER
→ GUIVOS
→ Entrada protegida

EYEBROW
→ Antes de começar

H1
→ Saiba o que muda ao entrar.

BODY
→ Você está saindo do ambiente público e entrando em uma área protegida da Guivos. Aqui, você decide quando compartilhar informações sobre sua jornada.

INFORMATION CARD
→ Este passo não solicita seu relato pessoal.
→ Entrar ou criar conta não autoriza análise nem personalização.

SUPPORT LIST
→ Conheça o processo antes de entrar
→ Revise seus controles antes de compartilhar algo
→ Volte ou explore sem personalização quando quiser

PRIMARY CTA
→ Continuar

SECONDARY
→ Como funciona

ALTERNATIVES
→ Explorar sem personalização
→ Voltar para a Home
```

### 7.3 Decisão visual

- H1 ocupa no máximo três linhas em 390 px;
- informação de proteção fica em card de baixo contraste, não banner de alerta;
- CTA primário aparece após o contexto, nunca antes;
- alternativas permanecem visíveis abaixo do CTA sem redução extrema de contraste;
- nenhum campo, upload, gravação ou pedido de dado pessoal aparece neste frame.

## 8. Frame 02 — Gate de acesso

### 8.1 Objetivo

Permitir autenticação/criação/recuperação como gate interno de `PER-002`, sem converter credencial em autorização de processamento.

### 8.2 Hierarquia high-fidelity

```text
HEADER
→ GUIVOS
→ Entrada protegida

EYEBROW
→ Acesso

H1
→ Entre para continuar.

BODY
→ O acesso vincula esta etapa a você. Isso não autoriza o uso do que você vier a compartilhar.

ACCESS MODE CONTROL
→ Entrar
→ Criar conta

AUTH CONTROL SLOT 01
→ Identificação

AUTH CONTROL SLOT 02
→ Credencial

PRIMARY CTA
→ Continuar

TEXT ACTION
→ Recuperar acesso

PRIVACY NOTE
→ O acesso não inicia análise da sua jornada.

ALTERNATIVES
→ Voltar
→ Explorar sem personalização
```

`Identificação` e `Credencial` permanecem nomes funcionais de slot. Esta entrega não define e-mail, telefone, senha, biometria, passkey, provedor externo ou tecnologia concreta de autenticação.

### 8.3 Estados de campo

Visualmente previstos:

```text
DEFAULT
FOCUS
FILLED
ERROR
DISABLED — SOMENTE SE HOUVER MOTIVO FUNCIONAL
```

Erro deve aparecer abaixo do campo ou em card contextual; cor nunca é o único sinal.

## 9. Variante A — Sessão já autenticada

O Frame 02 é omitido quando a sessão válida já satisfaz legitimamente o gate.

No topo do Frame 03 aparece um status discreto:

```text
STATUS PILL
→ Sessão ativa

SUPPORT COPY
→ Seu acesso já está válido. Você continua nesta entrada para revisar contexto e controles antes de qualquer compartilhamento material.
```

Não há tela de “login concluído”, celebração ou sucesso artificial.

## 10. Variante B — Recuperação / restrição / falha

### 10.1 Hierarquia

```text
EYEBROW
→ Acesso protegido

H1
→ Não foi possível concluir o acesso.

BODY
→ Você pode tentar novamente ou escolher outro caminho. Esta tentativa não inicia sua jornada material.

ERROR CARD
→ Não conseguimos concluir esta etapa.
→ Revise os dados ou use uma opção de recuperação disponível.

PRIMARY CTA
→ Tentar novamente

SECONDARY / TEXT ACTIONS
→ Recuperar acesso
→ Usar outra forma de acesso, se disponível
→ Voltar à entrada protegida
→ Explorar sem personalização
```

### 10.2 Guardrails

- não revelar se determinada identificação possui conta;
- não expor motivo sensível de restrição sem necessidade;
- não transformar recuperação em onboarding novo;
- preservar saída e alternativa sem personalização;
- não usar vermelho como estado dominante de toda a superfície.

## 11. Frame 03 — Continuação autenticada / controles

### 11.1 Objetivo

Confirmar contexto protegido e tornar finalidades, privacidade, controles e reversibilidade compreensíveis antes do handoff.

### 11.2 Hierarquia high-fidelity

```text
HEADER
→ GUIVOS
→ Entrada protegida

EYEBROW
→ Seus controles

H1
→ Você continua no controle.

BODY
→ Antes de seguir, veja o que esta entrada significa — e o que ela ainda não autoriza.

CONTROL CARD 01
→ O que você compartilha
→ Só quando você decidir.

CONTROL CARD 02
→ Como pode ser usado
→ Cada uso relevante deverá ser explicado antes de acontecer.

CONTROL CARD 03
→ Seus controles
→ Revisar, corrigir, limitar, retirar ou interromper quando aplicável.

INFORMATION NOTE
→ Entrar não autoriza, por si só, análise ou personalização do que você vier a compartilhar.

PRIMARY CTA
→ Continuar

TEXT ACTION
→ Ver detalhes de privacidade

ALTERNATIVES
→ Sair por agora
→ Explorar sem personalização
```

### 11.3 N2 preservada

Não existe:

- `Aceito tudo`;
- consentimento omnibus;
- checkbox pré-selecionado;
- autorização material antecipada;
- copy que converta explicação genérica em permissão futura.

```text
GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION
```

## 12. Variante C — Sair / interromper / explorar sem personalização

A variante é tratada como **bottom sheet em mobile** e **dialog central em desktop**, sem criar nova superfície canônica.

### 12.1 Hierarquia

```text
TITLE
→ Como você quer continuar?

BODY
→ Você não precisa concluir agora.

PRIMARY ALTERNATIVE
→ Explorar sem personalização

SECONDARY ALTERNATIVE
→ Voltar para a Home

TERTIARY
→ Pausar por agora

RETURN ACTION
→ Continuar na entrada protegida
```

A ação `Pausar por agora` representa intenção de interrupção e não define persistência técnica.

## 13. Frame 04 — Handoff ready

### 13.1 Objetivo

Mostrar que as responsabilidades de entrada foram apresentadas e que a próxima ação leva a `PER-003`, sem inferir compreensão silenciosa e sem desenhar as modalidades de `PER-003`.

### 13.2 Correção explícita de N1

A working copy low-fidelity `ambiente protegido compreendido` não é promovida para high-fidelity como prova de compreensão.

Ela é substituída por fatos de interface verificáveis:

```text
DISPLAYED
≠ UNDERSTOOD
```

### 13.3 Hierarquia high-fidelity

```text
HEADER
→ GUIVOS
→ Entrada protegida

EYEBROW
→ Próximo passo

H1
→ Sua entrada está preparada.

BODY
→ Você já viu como esta entrada funciona e quais controles permanecem com você. O próximo passo abre a escolha de como começar.

READINESS LIST
→ Contexto da entrada apresentado
→ Acesso concluído ou já válido
→ Controles e alternativas apresentados
→ Nenhum relato é solicitado nesta etapa

PRIMARY CTA
→ Escolher como quero começar

TEXT ACTIONS
→ Revisar privacidade e controles
→ Sair por agora

HANDOFF LABEL
→ Próximo: escolha de modalidade
```

`Sua entrada está preparada` significa somente que as condições de interface deste boundary foram apresentadas; não significa que a Pessoa compreendeu, consentiu com usos futuros ou concluiu `PER-003`.

### 13.4 Handoff

```text
PRIMARY CTA
→ TRN-002
→ PER-003

THIS DELIVERY
→ DOES NOT MATERIALIZE PER-003 OPTIONS
→ DOES NOT DEFINE TEXT / VOICE / FILE / OTHER MODALITIES
```

## 14. Sistema de ícones local

A entrega utiliza ícones lineares simples, espessura visual consistente e significado sempre acompanhado por texto quando material.

Famílias semânticas permitidas:

- proteção/contexto;
- informação;
- conta/acesso;
- recuperação;
- privacidade/controle;
- voltar/sair;
- confirmação factual;
- próximo passo.

Ícone não pode funcionar como selo de conformidade, garantia de segurança ou prova de autorização.

## 15. Estados de foco, feedback e erro

### 15.1 Focus visible

Todos os controles interativos recebem anel perceptível:

```text
outline
→ 3 px focus
→ offset 2 px
```

### 15.2 Feedback

Feedback de ação deve ser textual + visual. Não depender exclusivamente de animação, cor, vibração ou som.

### 15.3 Disabled

Estado disabled não é usado para coercivamente impedir saída ou alternativa. Quando possível, explicar por que uma ação primária ainda não pode prosseguir.

## 16. Acessibilidade projetada

A entrega high-fidelity adota como requisitos de validação:

- contraste de texto/controle orientado a WCAG AA;
- foco visível;
- alvos interativos de pelo menos 44 × 44 px;
- ordem semântica equivalente à ordem visual;
- nenhuma informação material apenas por cor;
- labels persistentes para campos;
- mensagens de erro associáveis ao controle correspondente;
- escala de texto sem perda de conteúdo essencial;
- alternativas e saída acessíveis por teclado quando aplicável;
- headings hierárquicos consistentes;
- linguagem simples e não coerciva.

Esses itens são **requisitos de Design submetidos à validação**; não constituem evidência de acessibilidade implementada ou testada em produção.

## 17. Motion e microinterações

Nenhuma motion spec executável é autorizada nesta entrega.

```text
MOTION DIRECTION
→ QUIET / OPTIONAL / NON-BLOCKING

MOTION IMPLEMENTATION
→ NOT_AUTHORIZED
```

Se motion for proposta posteriormente, não poderá:

- retardar saída;
- esconder alternativa;
- simular segurança;
- criar urgência;
- transformar autenticação em celebração de consentimento;
- inferir compreensão.

## 18. Working copy e autoridade verbal

A copy desta entrega é high-fidelity de Design/UX Writing em nível de proposta, mas continua não publicada.

Ela preserva:

```text
GUIVOS
≠ FUNDADOR

Possibility, lived.
→ assinatura institucional
→ não é necessária dentro de PER-002 por padrão

Do possível ao vivido.
→ NÃO utilizar em PER-002
```

A interface prioriza clareza funcional sobre repetição de assinatura de marca.

## 19. Matriz de cobertura high-fidelity

| Área autorizada | High-fidelity | Evidência |
|---|---|---|
| orientação protegida / pré-auth | materializada | Frame 01 |
| autenticação quando necessária | materializada | Frame 02 |
| sessão já autenticada | materializada | Variante A |
| continuação autenticada | materializada | Frame 03 |
| recuperação / restrição / falha | materializada | Variante B |
| sair / interromper / alternativa | materializada | Variante C + ações persistentes |
| handoff legítimo | materializada | Frame 04 |

```text
HIGH-FIDELITY AUTHORIZED COVERAGE
→ 7 / 7 MATERIALIZED
```

Cobertura não equivale a validação.

## 20. Critérios que deverão ser validados

A validação posterior deverá verificar pelo menos:

1. integridade das 7 áreas;
2. manutenção de `PER-002` como única responsabilidade;
3. autenticação como gate interno;
4. ausência de inferência de consentimento/processamento;
5. preservação de N1;
6. preservação de N2;
7. autonomia/reversibilidade perceptíveis;
8. `PER-003` apenas como handoff;
9. ausência de expansão para `PER-008`;
10. coerência entre mobile/tablet/desktop;
11. contraste/foco/legibilidade no nível de especificação;
12. ausência de dark patterns;
13. ausência de restauração visual histórica;
14. ausência de Source Lock por inferência;
15. ausência de UXA-102/Engineering/implementação.

## 21. Evidência histórica

```text
UXA-034
→ HISTORICAL PRODUCER REMOVED
→ NOT RESTORED
→ NOT COPIED AS CURRENT APPEARANCE

UXA-035
→ MAY INFORM FUNCTIONAL / ANTI-REGRESSION VALIDATION
→ DOES NOT DEFINE CURRENT APPEARANCE
```

Nenhum SVG histórico foi restaurado.

## 22. O que esta entrega não é

```text
HIGH-FIDELITY DELIVERY
≠ FUNCTIONAL / VISUAL VALIDATION
≠ PRODUCTION UI
≠ INTERACTIVE PROTOTYPE
≠ SOURCE LOCK
≠ DESIGN SYSTEM GLOBAL
≠ IMPLEMENTATION
≠ OPERATION
```

Esta entrega não autoriza:

- nova superfície ou novo `PER-ID`;
- materialização detalhada de `PER-003`;
- materialização de `PER-008`;
- Design das Homes;
- protótipo interativo;
- Source Lock visual;
- `UXA-102/V5`;
- Product Engineering;
- implementação;
- produção;
- merge da PR #363.

## 23. Resultado da execução

```text
PER-002 HIGH-FIDELITY DESIGN EXECUTION
→ EXECUTED

DELIVERY
→ GKR-UX-PER002-HIFI-DELIVERY-001 v0.1.0

COMPOSITION
→ 4 PRIMARY FRAMES + 3 VARIANTS

HIGH-FIDELITY COVERAGE
→ 7 / 7 MATERIALIZED

LOCAL VISUAL TOKENS
→ DEFINED FOR THIS DELIVERY
→ NOT GLOBAL BRAND / DESIGN SYSTEM AUTHORITY

N1
→ PRESERVED / EXPLICITLY REFORMULATED IN FRAME 04

N2
→ PRESERVED

HIGH-FIDELITY DESIGN VALIDATION
→ NOT_STARTED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

SOURCE LOCK
→ NOT_CREATED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

IMPLEMENTATION / PRODUCTION
→ NOT_AUTHORIZED

PR #363 MERGE
→ NOT_AUTHORIZED
```

## 24. Próximo gate

O próximo ato legítimo é uma **validação governada da entrega high-fidelity de `PER-002`**.

```text
NEXT
→ PER-002 HIGH-FIDELITY DESIGN VALIDATION

VALIDATION TARGET
→ GKR-UX-PER002-HIFI-DELIVERY-001 v0.1.0

MUST CHECK
→ FUNCTIONAL BOUNDARY
→ 7 / 7 COVERAGE
→ N1 / N2
→ VISUAL HIERARCHY
→ ACCESSIBILITY SPECIFICATION
→ AUTONOMY / REVERSIBILITY
→ NO DARK PATTERN
→ NO DOWNSTREAM EXPANSION

DO NOT YET
→ CREATE PROTOTYPE
→ CREATE SOURCE LOCK BY INFERENCE
→ START UXA-102/V5
→ RESUME PRODUCT ENGINEERING
→ IMPLEMENT
→ MERGE PR #363
```

A validação high-fidelity deverá ser um ato separado. Esta entrega encerra somente a execução autorizada de Design.