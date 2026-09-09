---
id: GKR-UX-PER002-MAT-ELIGIBILITY-001
title: PER-002 — Elegibilidade de Materialização e Boundary de Handoff para Design
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-09
normative: true
maturity: materialization_eligibility_pass_pre_design_authorization
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOME-MASTER-001
  - UXA-003-A1
  - UXA-020
  - UXA-023
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - PER-001
  - PER-002
  - PER-003
  - PER-008
  - TRN-001
  - TRN-002
---

# PER-002 — Elegibilidade de Materialização e Boundary de Handoff para Design

## 1. Finalidade

Esta autoridade consolida a adjudicação documental de elegibilidade de materialização da primeira responsabilidade autenticada da Pessoa após a Home e congela o **boundary funcional mínimo que poderá ser entregue a Design somente após autorização governada separada**.

Ela não cria nova superfície, novo `PER-ID`, UXA numerada, wireframe, Source Lock visual, UI, protótipo ou implementação.

```text
FUNCTIONAL DEFINITION
→ JÁ CONSOLIDADA

MATERIALIZATION ELIGIBILITY
→ ADJUDICADA NESTA AUTORIDADE

DESIGN AUTHORIZATION
→ SEPARATE GOVERNED GATE
→ NOT GRANTED BY THIS DOCUMENT
```

## 2. Decisão canônica

```text
Q MATERIALIZATION ELIGIBILITY
→ PASS

MATERIALIZATION WARRANTED
→ YES

TARGET
→ PER-002 — ENTRADA PROTEGIDA

MATERIALIZATION NATURE
→ LOW-FIDELITY
→ FUNCTIONAL
→ EXISTING RESPONSIBILITY ONLY

NEW SURFACE
→ NO

NEW PER-ID
→ NO

UXA-102 / V5
→ NOT_STARTED

F-022
→ NOT OPENED
```

O `PASS` significa que o corpus vigente possui definição funcional suficiente para tornar `PER-002` inspecionável visualmente em baixa fidelidade **sem usar Design para descobrir a responsabilidade**.

```text
MATERIALIZAR
→ TORNAR O CONTRATO FUNCIONAL INSPECIONÁVEL

MATERIALIZAR
≠ REDESCOBRIR A ARQUITETURA
≠ CRIAR NOVA RESPONSABILIDADE
≠ PROMOVER MATURIDADE DE TRANSIÇÃO
```

## 3. Boundary funcional congelado

A futura materialização, se Design for explicitamente autorizado, deverá tratar os elementos abaixo como estados/variantes da **mesma responsabilidade `PER-002`**, e não como novas superfícies por inferência.

```text
PER-001 — HOME PÚBLICA
        │
        │ decisão consciente de iniciar
        ▼

PER-002 — ENTRADA PROTEGIDA
        │
        ├─ A. ORIENTAÇÃO PROTEGIDA / PRÉ-AUTH
        │    → informar saída do ambiente público
        │    → explicar natureza do ambiente protegido
        │    → apresentar alternativas
        │    → nenhuma coleta automática
        │
        ├─ B. GATE DE AUTENTICAÇÃO
        │    → entrar
        │    → criar conta
        │    → recuperar acesso, quando aplicável
        │    → gate condicional
        │    → pode já estar satisfeito
        │
        ├─ C. CONTINUAÇÃO AUTENTICADA
        │    → confirmar contexto protegido
        │    → apresentar finalidades aplicáveis
        │    → apresentar privacidade e controles
        │    → esclarecer que login ≠ autorização de processamento
        │    → preservar reversibilidade
        │
        ├─ D. ALTERNATIVAS
        │    → voltar
        │    → interromper
        │    → não prosseguir
        │    → explorar sem personalização material, quando aplicável
        │
        └─ E. HANDOFF READY
             → orientação / controles suficientes
             → decisão consciente de continuar
                    │
                    │ TRN-002
                    ▼
PER-003 — ESCOLHA DE MODALIDADE
```

## 4. Regra de autenticação

```text
AUTHENTICATION
→ INTERNAL GATE / STATE WITHIN PER-002

AUTHENTICATION COMPLETED
≠ PER-002 COMPLETED

LOGIN / ACCOUNT CREATION
≠ MATERIAL PROCESSING AUTHORIZATION

PER-002 COMPLETION
→ LEGITIMATE HANDOFF TO PER-003
```

Uma sessão já autenticada pode satisfazer o gate de autenticação sem eliminar as responsabilidades restantes de `PER-002` que forem aplicáveis ao contexto real.

A futura materialização não deve criar fricção artificial apenas para representar o gate quando ele já estiver legitimamente satisfeito.

## 5. Entrada nova × relação existente

Dois caminhos permanecem distintos.

### 5.1 Primeira / nova entrada na Journey

```text
HOME
→ decisão voluntária de iniciar
→ PER-002
→ TRN-002
→ PER-003
→ ...
```

### 5.2 Login de relação existente

```text
HOME
→ LOGIN
→ AUTHENTICATION
→ RECOVER / RESUME LEGITIMATE EXISTING STATE
```

A rota de login existente é **resumptiva**. Ela não deve ser transformada, por conveniência visual, em onboarding universal `PER-002 → PER-003` quando o estado real da Pessoa legitimar outra retomada.

## 6. Conteúdo funcional mínimo que Design deverá conseguir representar

Quando houver autorização separada de Design, a materialização low-fidelity deverá permitir inspeção dos seguintes requisitos, na medida em que forem aplicáveis ao estado:

1. reconhecimento inequívoco de que a Pessoa deixou a Home pública e entrou em ambiente protegido;
2. explicação suficiente do que muda antes de solicitar autenticação ou dados pessoais adicionais;
3. alternativas legítimas de retorno, interrupção ou não prosseguimento;
4. autenticação, criação de conta e recuperação como gate funcional — não como finalidade da experiência;
5. continuação autenticada de `PER-002` após conclusão do gate quando ainda houver responsabilidades de orientação/controle pendentes;
6. finalidades aplicáveis, privacidade, controles e reversibilidade antes de processamento material correspondente;
7. distinção visível entre autenticar e autorizar processamento/materialidade adicional;
8. condição compreensível de `HANDOFF READY` antes de `TRN-002`;
9. destino `PER-003` tratado somente como handoff downstream, sem absorção de sua responsabilidade dentro de `PER-002`;
10. tratamento coerente de voltar, cancelar, interromper, erro e recuperação sem aprisionamento;
11. preservação do caminho de login resumptivo para relações existentes;
12. nenhuma dependência de uma aparência histórica removida para que o contrato seja compreendido.

## 7. O que está fora do handoff

A futura materialização de `PER-002` não está autorizada a absorver ou definir por inferência:

- a responsabilidade de `PER-003 — Escolha de modalidade` além do ponto de handoff;
- `PER-008 — Tela Hoje` como primeira responsabilidade autenticada;
- arquitetura completa de Conta / `PER-009`;
- dashboard, feed ou home autenticada genérica;
- consentimento omnibus que substitua finalidades e autorizações específicas;
- processamento material iniciado pelo simples fato de existir conta ou sessão autenticada;
- nova taxonomia, novo participante, novo Produto Especializado ou novo Domínio de Evolução;
- UXA-102/V5;
- Product Engineering;
- implementação, produção ou operação.

## 8. Tratamento de evidência histórica

O corpus vigente preserva referências funcionais e de proveniência a materializações antigas, mas `F-016/F-016-A` removeu a camada física de SVGs e produtores visuais elegíveis após absorção.

```text
UXA-034
→ PODE CONTRIBUIR PROVENIÊNCIA / CONTRATO FUNCIONAL ABSORVIDO
→ NÃO RESTAURA O LOW-FIDELITY REMOVIDO
→ NÃO É BASELINE VISUAL CORRENTE POR INFERÊNCIA

UXA-035
→ NENHUMA AUTORIDADE VISUAL CORRENTE É PROMOVIDA POR ESTA ADJUDICAÇÃO

REMOVED SVG / HISTORICAL MATERIALIZATION
→ NOT TO BE RESTORED
→ NOT A DESIGN SOURCE OF TRUTH

CURRENT DESIGN INPUT
→ CURRENT CANONICAL FUNCTIONAL AUTHORITIES
```

Design futuro poderá consultar proveniência para compreensão histórica, mas não deverá copiar, restaurar ou promover aparência removida como baseline sem uma nova decisão explícita e justificada.

## 9. Maturidade das transições

A adjudicação de materialização não altera maturidade funcional.

```text
TRN-001
→ PARTIAL
→ UNCHANGED

TRN-002
→ LOCALLY VALIDATED
→ UNCHANGED

LOW-FIDELITY MATERIALIZATION FUTURE
≠ AUTOMATIC TRANSITION MATURITY PROMOTION
```

Qualquer promoção futura exige evidência e adjudicação próprias.

## 10. Critérios de aceitação para eventual Design low-fidelity

Uma futura entrega somente poderá ser considerada aderente a este handoff se:

- representar `PER-002` como uma responsabilidade existente, ainda que use estados ou passos visualmente distinguíveis;
- não criar novo `PER-ID` para autenticação ou continuação autenticada sem evidência adicional e decisão própria;
- permitir que o gate de autenticação seja condicional ou já satisfeito;
- deixar claro que autenticação não equivale a autorização de processamento material;
- preservar retorno, interrupção, recusa e reversibilidade;
- não forçar login de relação existente ao onboarding de primeira entrada;
- não antecipar `PER-003`, `PER-008` ou outra responsabilidade downstream;
- não restaurar materialização visual removida como fonte de verdade;
- manter `TRN-001` e `TRN-002` em suas maturidades vigentes até validação própria;
- permanecer low-fidelity e funcional no primeiro ato de Design, salvo autorização explícita posterior de maior fidelidade.

## 11. Gate seguinte

```text
Q MATERIALIZATION ELIGIBILITY
→ PASS / CANONICALLY CONSOLIDATED

DESIGN HANDOFF BOUNDARY
→ FROZEN FOR A SEPARATE AUTHORIZATION DECISION

DESIGN
→ NOT AUTHORIZED BY THIS DOCUMENT

NEXT GOVERNED ACT
→ EXPLICIT DESIGN AUTHORIZATION DECISION
→ SCOPE, IF AUTHORIZED: LOW-FIDELITY FUNCTIONAL MATERIALIZATION OF PER-002 ONLY

UXA-102 / V5
→ NOT_STARTED
→ MUST NOT BE STARTED BY INFERENCE

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01

MERGE PR #363
→ NOT AUTHORIZED
```

Esta autoridade prepara o handoff; ela não executa o handoff para Design por si só.