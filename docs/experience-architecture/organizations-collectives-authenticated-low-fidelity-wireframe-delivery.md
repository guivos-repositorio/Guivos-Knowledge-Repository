---
id: GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
title: Organizações e Coletivos — Entrega de Wireframes Autenticados Low-Fidelity
status: active
version: 0.1.0
owner: Design da Experiência da Guivos
last_updated: 2026-09-18
normative: false
maturity: authenticated_low_fidelity_wireframe_delivery_pending_functional_validation
depends_on:
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
related:
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-019
---

# Organizações e Coletivos — Entrega de Wireframes Autenticados Low-Fidelity

## 1. Finalidade

Esta entrega materializa visualmente, em baixa fidelidade, a experiência autenticada principal de Organização e Coletivo conforme:

- autorização `GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001`;
- Navigation Materialization `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0`;
- Surface Map, State Map e Priority Flows vigentes.

```text
DESIGN AUTHORIZATION
→ GRANTED

LOW-FIDELITY DELIVERY
→ EXECUTED
→ FUNCTIONAL / STRUCTURAL
→ O/C AUTHENTICATED EXPERIENCE

FUNCTIONAL VALIDATION
→ NOT YET PERFORMED

HIGH-FIDELITY UI
→ NOT AUTHORIZED
```

A entrega é não normativa. Ela torna o boundary funcional visualmente inspecionável sem promover maturidade funcional ou técnica.

## 2. Decisão de composição

A primeira entrega utiliza **dois frames principais, duas variantes específicas e três variantes compartilhadas**.

```text
ORGANIZAÇÃO
├─ FRAME O1 — VISÃO GERAL / OPERAÇÃO REGULAR
└─ VARIANTE O-A — ATENÇÃO / OBRIGAÇÃO / RISCO

COLETIVO
├─ FRAME C1 — INÍCIO / OPERAÇÃO REGULAR
└─ VARIANTE C-A — PARTICIPAÇÃO / GOVERNANÇA / PROTEÇÃO

COMPARTILHADO
├─ VARIANTE X1 — TROCA DE CONTEXTO / REVALIDAÇÃO
├─ VARIANTE X2 — AUTORIDADE INSUFICIENTE / PROTEÇÃO / CONTESTAÇÃO
└─ VARIANTE X3 — CONTEXTO EXPIRADO / INDISPONIBILIDADE / BAIXA CONECTIVIDADE
```

Estados operacionais não viram automaticamente novas superfícies ou telas canônicas.

## 3. Linguagem visual low-fidelity

A representação é monoespaçada, estrutural e mobile-first.

```text
DEFINED NOW
→ INFORMATION HIERARCHY
→ RELATIVE PRIORITY
→ NAVIGATION GROUPING
→ CONTEXT POSITION
→ ATTENTION POSITION
→ RETURN / INTERRUPTION AFFORDANCE
→ STATE VARIANTS

NOT DEFINED NOW
→ FINAL COMPONENTS
→ FINAL COPY
→ BRAND TYPOGRAPHY
→ COLORS
→ ICON SYSTEM
→ MOTION
→ FINAL SPACING TOKENS
→ TECHNICAL ROUTES
```

Os labels são working labels derivados das autoridades atuais.

## 4. Shell comum

A estrutura compartilhada é:

```text
+------------------------------------------------------+
| GUIVOS                                               |
| [ Contexto ativo ▾ ]      [ Buscar ] [ Atenção ]     |
|------------------------------------------------------|
| CONTEXTO / PAPEL / UNIDADE                           |
| autoridade aplicável · estado de contexto            |
|------------------------------------------------------|
| NAVEGAÇÃO PRINCIPAL                                  |
| domínio 1 · domínio 2 · domínio 3 · ...              |
|------------------------------------------------------|
| MOMENTO                                              |
| síntese da situação atual                            |
|------------------------------------------------------|
| ATENÇÃO MATERIAL                                     |
| apenas o que exige compreensão / ação legítima       |
|------------------------------------------------------|
| PRÓXIMOS PASSOS                                      |
| acessos contextuais a objetos/superfícies existentes |
|------------------------------------------------------|
| CAPACIDADES CONTEXTUAIS                              |
| Planos / capacidades especializadas quando aplicável |
|------------------------------------------------------|
| [ Voltar ] [ Interromper ]                           |
+------------------------------------------------------+
```

A forma final de header/sidebar/tabs não é congelada.

## 5. Frame O1 — Organização / Visão Geral regular

Anchor: `GKR-SURF-ORG-001`.

Objetivo: permitir compreensão do contexto institucional ativo, estado corrente e caminhos legítimos de trabalho sem transformar a Visão Geral em dashboard total.

```text
+------------------------------------------------------------------+
| GUIVOS                                                           |
| Organização: Horizonte Social ▾         Buscar     Atenção (2)   |
| Unidade: Brasil · Papel: Gestor autorizado                       |
|------------------------------------------------------------------|
| VISÃO GERAL                                                      |
|------------------------------------------------------------------|
| Navegação                                                        |
| [Visão Geral] [Oportunidades] [Relações] [Responsabilidades]     |
|                                                         [Mais ▾] |
|------------------------------------------------------------------|
| MOMENTO                                                          |
| Operação regular                                                 |
| 2 responsabilidades próximas · nenhuma urgência crítica           |
|                                                                  |
| [ Ver responsabilidades ]                                        |
|------------------------------------------------------------------|
| ATENÇÃO MATERIAL                                                 |
| • Programa "Rede Local" aguarda evidência complementar           |
| • Relação com Coletivo Aurora tem revisão em 5 dias              |
|                                                                  |
| [ Abrir objeto ]    [ Ver todas as atenções ]                    |
|------------------------------------------------------------------|
| PRÓXIMOS PASSOS                                                  |
| [ Criar oportunidade ]                                           |
| [ Revisar relação O↔C ]                                          |
| [ Consultar resultados/evidências ]                              |
|------------------------------------------------------------------|
| CONTEXTO E AUTORIDADE                                            |
| Você atua como Gestor autorizado nesta unidade.                   |
| [ Entender limites de autoridade ]                               |
|------------------------------------------------------------------|
| CAPACIDADE                                                       |
| Planos e capacidade                                              |
| [ Ver capacidade atual ]                                         |
|------------------------------------------------------------------|
| Voltar ao contexto anterior                        Interromper    |
+------------------------------------------------------------------+
```

### 5.1 Hierarquia O1

```text
PRIMARY
→ MOMENTO
→ ATTENTION
→ NEXT LEGITIMATE WORK

SECONDARY
→ PRIMARY DOMAINS

CONTEXTUAL
→ AUTHORITY
→ PLANOS / CAPACITY

NOT PRIMARY
→ ADS
→ BUSINESS
→ INTELLIGENCE
→ OTHER SPECIALIZED PRODUCTS
```

### 5.2 Resolução de domínios da Organização

O wireframe não cria hubs adicionais.

```text
OPORTUNIDADES
→ criar / preparar → ORG-002
→ aprovada / ativa → ORG-003

RELAÇÕES O↔C
→ proposta → ORG-004
→ negociação → ORG-005
→ ativa / revisão → ORG-006

RESPONSABILIDADES / EVIDÊNCIAS
→ ORG-007

ORGANIZAÇÃO E AUTORIDADE
→ CONTEXTUAL
→ NO EXCLUSIVE NEW SURFACE

PLANOS
→ ORG-301..304
→ SPECIALIZED / CONTEXTUAL
```

## 6. Variante O-A — atenção, obrigação ou risco

Objetivo: mostrar que atenção material altera prioridade, não identidade da superfície.

```text
+------------------------------------------------------------------+
| Organização: Horizonte Social ▾                 Atenção crítica  |
| Unidade: Brasil · Papel: Gestor autorizado                       |
|------------------------------------------------------------------|
| VISÃO GERAL                                                      |
|------------------------------------------------------------------|
| MOMENTO                                                          |
| Exige atenção                                                    |
| Relação institucional contestada + obrigação vencida             |
|------------------------------------------------------------------|
| ATENÇÃO MATERIAL                                                 |
| [!] Obrigação "Prestação de evidência" venceu há 2 dias          |
|     fonte: responsabilidade existente                             |
|     [ Abrir ORG-007 ]                                            |
|                                                                  |
| [!] Relação com Coletivo Aurora está contestada                  |
|     estado: revisão                                              |
|     [ Abrir relação existente ]                                  |
|------------------------------------------------------------------|
| O QUE NÃO MUDA                                                   |
| • contestação não encerra relação automaticamente                |
| • atraso não prova falha de impacto                              |
| • ausência técnica não vira conclusão funcional                  |
|------------------------------------------------------------------|
| [ Voltar sem alterar ]                           [ Interromper ]  |
+------------------------------------------------------------------+
```

Essa variante cobre risco, obrigação material, contestação e evidência insuficiente sem inventar estado de negócio.

## 7. Frame C1 — Coletivo / Início regular

Anchor: `GKR-SURF-COL-002`.

Objetivo: sintetizar Momento coletivo, participação, atividade, governança e responsabilidades sem transformar Início em superdashboard.

```text
+------------------------------------------------------------------+
| GUIVOS                                                           |
| Coletivo: Rede Aurora ▾                Buscar       Atenção (3)  |
| Papel: Responsável · Governança vigente                           |
|------------------------------------------------------------------|
| INÍCIO                                                           |
|------------------------------------------------------------------|
| Navegação                                                        |
| [Início] [Atividades] [Participação] [Governança] [Relações]     |
|                                                         [Mais ▾] |
|------------------------------------------------------------------|
| MOMENTO DO COLETIVO                                              |
| Operação regular                                                 |
| Próxima atividade em 3 dias · 1 solicitação pendente             |
|                                                                  |
| [ Ver atividade ]                                                |
|------------------------------------------------------------------|
| ATENÇÃO MATERIAL                                                 |
| • 1 solicitação de participação aguarda análise                  |
| • comunicação oficial precisa confirmação de responsável         |
| • relação com Organização Horizonte entra em revisão             |
|                                                                  |
| [ Abrir objeto ]    [ Ver todas as atenções ]                    |
|------------------------------------------------------------------|
| PRÓXIMOS PASSOS                                                  |
| [ Revisar solicitação ]                                          |
| [ Consultar atividade ]                                          |
| [ Revisar relação O↔C ]                                          |
|------------------------------------------------------------------|
| GOVERNANÇA E AUTORIDADE                                          |
| Você atua como Responsável conforme regra vigente.                |
| [ Entender governança aplicável ]                                |
|------------------------------------------------------------------|
| CAPACIDADE                                                       |
| Planos e capacidade                                              |
| [ Ver capacidade atual ]                                         |
|------------------------------------------------------------------|
| Voltar ao contexto anterior                        Interromper    |
+------------------------------------------------------------------+
```

### 7.1 Resolução de domínios do Coletivo

```text
ATIVIDADES / OPORTUNIDADES
→ COL-006

PARTICIPAÇÃO
→ solicitações → COL-003
→ participantes / vínculos → COL-004
→ comunicação relacionada → COL-005

GOVERNANÇA / PROTEÇÃO
→ comunicação oficial → COL-005
→ decisão / consulta → COL-006
→ proteção / moderação → COL-007

RELAÇÕES O↔C
→ COL-008

APRENDIZADOS / EVIDÊNCIAS
→ CONTEXTUAL
→ NO EXCLUSIVE NEW SURFACE

COLETIVO E AUTORIDADE
→ CONTEXTUAL / COL-002 PARTIALLY

PLANOS
→ COL-301..304
→ SPECIALIZED / CONTEXTUAL
```

## 8. Variante C-A — participação, governança e proteção

```text
+------------------------------------------------------------------+
| Coletivo: Rede Aurora ▾                        Proteção requerida |
| Papel: Responsável                                               |
|------------------------------------------------------------------|
| INÍCIO                                                           |
|------------------------------------------------------------------|
| ATENÇÃO MATERIAL                                                 |
| [!] Solicitação de participação aguarda autoridade competente    |
|     [ Abrir COL-003 ]                                            |
|                                                                  |
| [!] Conteúdo protegido requer moderação                          |
|     conteúdo sensível oculto neste resumo                        |
|     [ Abrir COL-007 conforme autoridade ]                        |
|                                                                  |
| [!] Função de facilitação sem responsável disponível             |
|     [ Entender dependência ]                                     |
|------------------------------------------------------------------|
| GOVERNANÇA                                                       |
| A navegação não elege responsável automaticamente.               |
| Acesso técnico não substitui regra de governança.                |
|------------------------------------------------------------------|
| [ Voltar sem decidir ]                            [ Interromper ] |
+------------------------------------------------------------------+
```

A variante torna proteção, autoridade ausente e participação pendente visíveis sem expor informação sensível.

## 9. Variante X1 — troca de contexto e revalidação

Objetivo: materializar L0 sem converter troca de contexto em lifecycle transition.

```text
+------------------------------------------------------+
| TROCAR CONTEXTO                                      |
|------------------------------------------------------|
| Contexto atual                                       |
| Organização: Horizonte Social / Brasil               |
| Papel: Gestor autorizado                             |
|------------------------------------------------------|
| Selecionar outro contexto elegível                   |
| ( ) Organização: Horizonte Social / Portugal         |
| ( ) Coletivo: Rede Aurora                            |
| ( ) Coletivo: Mobiliza Centro                        |
|------------------------------------------------------|
| Ao trocar, serão revalidados:                        |
| • participante                                       |
| • unidade / escopo                                   |
| • papel                                              |
| • autoridade                                         |
| • acesso a dados protegidos                          |
|                                                      |
| Filtros e ações não portáveis não serão carregados.  |
|                                                      |
| [ Trocar contexto ]             [ Manter atual ]     |
+------------------------------------------------------+
```

Após troca válida:

```text
TARGET ORGANIZATION
→ LAND ON ORG-001

TARGET COLLECTIVE
→ LAND ON COL-002

CONTEXT SWITCH
≠ NEW GKR-TRN
```

## 10. Variante X2 — autoridade insuficiente, proteção ou contestação

```text
+------------------------------------------------------+
| ACESSO AO OBJETO                                     |
|------------------------------------------------------|
| Você pode compreender este contexto.                 |
| A ação solicitada exige autoridade adicional.        |
|                                                      |
| Estado do objeto: preservado                         |
| Conteúdo protegido: minimizado                       |
| Decisão: nenhuma alteração executada                 |
|                                                      |
| [ Entender autoridade necessária ]                   |
| [ Voltar ao objeto ]                                 |
| [ Interromper ]                                      |
+------------------------------------------------------+
```

Quando houver contestação:

```text
CONTESTED
→ SHOW CONTESTATION EXISTS
→ DO NOT RESOLVE BY INFERENCE
→ KEEP OBJECT IN RESPONSIBLE DOMAIN
```

## 11. Variante X3 — contexto expirado, indisponibilidade e baixa conectividade

```text
+------------------------------------------------------+
| CONTEXTO PRECISA SER REVALIDADO                      |
|------------------------------------------------------|
| Não foi possível confirmar o contexto atual.         |
| Nenhuma ação material foi executada.                 |
|                                                      |
| [ Revalidar contexto ]                               |
| [ Voltar ]                                           |
|                                                      |
| Conexão limitada?                                    |
| Mostramos apenas informação já segura para exibição. |
+------------------------------------------------------+
```

```text
TECHNICAL FAILURE
≠ BUSINESS STATE

RETRY
≠ DUPLICATE EFFECT

EXPIRED CONTEXT
→ REVALIDATE BEFORE MATERIAL ACTION
```

## 12. Busca, atenção e notificações

Busca e notificações não ganham domínio próprio.

```text
SEARCH / NOTIFICATION
→ RESOLVE EXISTING OBJECT
→ PRESERVE ACTIVE CONTEXT
→ REVALIDATE AUTHORITY
→ OPEN EXISTING RESPONSIBLE SURFACE
```

O resultado nunca cria superfície nem authority.

## 13. Planos e capacidades especializadas

Planos aparece somente como capacidade contextual secundária.

```text
ORGANIZATION
ORG-001
→ TRN-427
→ ORG-301
→ specialized flow
→ TRN-428
→ ORG-001

COLLECTIVE
COL-002
→ TRN-417
→ COL-301
→ specialized flow
→ TRN-418
→ COL-002
```

Regras visuais:

- nunca acima de Momento/Atenção;
- nunca substitui tarefa institucional;
- nunca parece condição para relevância;
- abrir não equivale a escolher plano;
- retornar não altera capacidade.

## 14. Bilateralidade O↔C

A relação bilateral mantém perspectivas separadas.

```text
ORGANIZATION PERSPECTIVE
→ ORG-004 / ORG-005 / ORG-006

COLLECTIVE PERSPECTIVE
→ COL-008

SAME BILATERAL SCOPE
→ DIFFERENT AUTHORITY / PERSPECTIVE
```

O wireframe não oferece "atuar como contraparte".

## 15. Gaps preservados

```text
O↔O
→ NO NEW NAVIGATION DESTINATION
→ GAP REMAINS

C↔C
→ NO NEW NAVIGATION DESTINATION
→ GAP REMAINS

COL-003 → COL-004
→ LOGICAL CONTINUITY
→ NO NEW GKR-TRN

ORGANIZATION AUTHORITY HUB
→ NOT INVENTED

COLLECTIVE LEARNINGS HUB
→ NOT INVENTED
```

## 16. Responsividade low-fidelity

### Mobile

```text
CONTEXT
→ STICKY / ALWAYS DISCOVERABLE IN STRUCTURE

PRIMARY NAV
→ COLLAPSED / DISCOVERABLE

MOMENT
→ FIRST CONTENT BLOCK

ATTENTION
→ SECOND CONTENT BLOCK WHEN PRESENT

NEXT STEPS
→ AFTER ATTENTION

CONTEXTUAL CAPABILITIES
→ AFTER PRIMARY WORK
```

### Desktop

```text
CONTEXT
→ TOP / PERSISTENT

PRIMARY DOMAINS
→ MAY USE SIDE OR TOP STRUCTURE

CONTENT
→ MOMENT + ATTENTION + NEXT STEPS

SPECIALIZED CAPABILITIES
→ SECONDARY REGION
```

A escolha final entre sidebar e top navigation permanece aberta.

## 17. Acessibilidade funcional incorporada

A entrega exige:

- labels textuais, não apenas ícones;
- prioridade não dependente apenas de cor;
- estados críticos identificáveis por texto;
- foco lógico preservável;
- alternativas de retorno/interrupção;
- conteúdo protegido minimizado;
- linguagem de autoridade compreensível;
- navegação compatível com zoom e reflow;
- low connectivity sem ocultar estado crítico conhecido.

Isso é requisito de especificação, não teste de acessibilidade real.

## 18. Working copy

Toda copy apresentada nos frames é provisória.

```text
WORKING COPY
→ FUNCTIONAL
→ EDITABLE

FINAL UX WRITING
→ NOT AUTHORIZED / NOT APPROVED
```

## 19. Anti-regressão

A entrega não pode:

- transformar Visão Geral/Início em dashboard total;
- colocar Planos como eixo primário;
- promover produto especializado por monetização;
- criar hubs para domínios contextual-only;
- inventar O↔O ou C↔C;
- mostrar conteúdo protegido por simples navegabilidade;
- transformar clique em confirmação;
- persistir autoridade após troca de contexto;
- transformar falha técnica em conclusão funcional;
- usar históricos UXA-015..018 como baseline visual;
- promover maturidade de transition.

## 20. Matriz de cobertura

| Boundary | Organização | Coletivo | Cobertura |
|---|---|---|---|
| contexto ativo / autoridade | O1 + X1/X2 | C1 + X1/X2 | materializada |
| anchor | ORG-001 | COL-002 | materializada |
| Momento | O1/O-A | C1/C-A | materializada |
| atenção | O1/O-A | C1/C-A | materializada |
| Próximos Passos | O1 | C1 | materializada |
| domínios principais | O1 | C1 | materializada |
| state-resolved | O1 matrix | C1 matrix | materializada |
| contextual-only | autoridade | aprendizados/autoridade | materializada |
| Planos contextual | O1 | C1 | materializada |
| troca de contexto | X1 | X1 | materializada |
| autoridade insuficiente | X2 | X2 | materializada |
| proteção | X2 | C-A/X2 | materializada |
| contestação | O-A/X2 | X2 | materializada |
| contexto expirado | X3 | X3 | materializada |
| indisponibilidade | X3 | X3 | materializada |
| retorno/interrupção | todos | todos | materializada |

## 21. Maturidade após esta entrega

```text
O/C LOW-FIDELITY WIREFRAME AUTHORIZATION
→ GRANTED
→ GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001 v1.0.0

O/C LOW-FIDELITY WIREFRAME DELIVERY
→ EXECUTED
→ GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0

FUNCTIONAL VALIDATION
→ NOT_STARTED

WIREFRAME STATUS
→ DELIVERY EXISTS
→ NOT YET FUNCTIONALLY VALIDATED

PHYSICAL SVG COUNT
→ 0 / UNCHANGED

NEW GKR-SURF-*
→ NONE

NEW GKR-TRN-*
→ NONE

TRANSITION MATURITY CHANGES
→ NONE

HIGH-FIDELITY UI
→ NOT AUTHORIZED

PROTOTYPE
→ NOT AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01 / NOT RELEASED
```

## 22. Próximo gate

O próximo ato governado é somente a **validação funcional da entrega low-fidelity autenticada O/C**.

Ela deverá confrontar:

1. `GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001`;
2. `GKR-UX-ORGCOL-AUTH-NAV-MAT-001`;
3. State Map;
4. Priority Flows;
5. Surface Registry;
6. Transition Registry;
7. `UXA-019`;
8. cobertura absorvida de UXA-015..018;
9. autonomia, autoridade, proteção, retorno e gaps.

```text
NEXT
→ O/C LOW-FIDELITY FUNCTIONAL VALIDATION

DO NOT YET
→ PROMOTE AS VALIDATED VISUAL REFERENCE
→ START HIGH-FIDELITY UI
→ START PROTOTYPE
→ START UXA-102/V5
→ RESUME PRODUCT ENGINEERING
```
