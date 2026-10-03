---
id: GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001
title: Organizações e Coletivos — Elegibilidade para Materialização da Navegação Autenticada
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-18
normative: false
maturity: authenticated_navigation_materialization_eligibility_pass
depends_on:
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
related:
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
---

# Organizações e Coletivos — Elegibilidade para Materialização da Navegação Autenticada

## 1. Finalidade

Este documento adjudica se existe **base documental suficiente para autorizar, em ato humano separado, a materialização da navegação autenticada de Organizações e Coletivos**.

A adjudicação foi promovida canonicamente após `DRAFT SUFFICIENCY = PASS`, Semantic #1125 `SUCCESS`, Mechanical #1363 `SUCCESS`, revisão read-only sem finding material e autorização humana explícita. A promoção estabelece a elegibilidade como verdade corrente; ela não autoriza a execução da etapa seguinte.

Ele não materializa a navegação.

A pergunta governada é:

> **Jobs, Arquitetura da Informação, Surface Map, State Map e Priority Flows já fornecem autoridade suficiente para transformar a topologia funcional O/C em uma estrutura explícita de navegação, sem inventar superfícies, transições, permissões, telas ou comportamento de produto não sustentado?**

```text
ELIGIBILITY ADJUDICATION
≠ NAVIGATION MATERIALIZATION
≠ WIREFRAME
≠ DESIGN
≠ UI
≠ PROTOTYPE
≠ IMPLEMENTATION
```

## 2. Estado de entrada

A adjudicação parte do estado integrado em `main` após a atualização global do GKR:

```text
MAIN BASELINE
→ a3e8ee6c6979ad83bda102c1d0c7a9baee26c447

GKR-STATE-001
→ v3.39.0

ROADMAP
→ 13.38.0

GKR-UX-ORGCOL-AUTH-JOBS-001
→ v1.4.0
→ ACTIVE

GKR-UX-ORGCOL-AUTH-IA-001
→ v1.3.0
→ ACTIVE / DEFINED PRE-SURFACE-MAP

GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
→ v1.0.0
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY

GKR-UX-ORGCOL-AUTH-STATE-MAP-001
→ v1.0.0
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY

GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
→ v1.0.0
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY

O/C NAVIGATION MATERIALIZATION
→ NOT MATERIALIZED
→ REQUIRES SEPARATE GOVERNED AUTHORIZATION

O/C AUTHENTICATED WIREFRAMES
→ NOT STARTED / NOT RELEASED

DESIGN / UI / PROTOTYPE
→ NOT AUTHORIZED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01 / NOT RELEASED
```

A autorização humana para retomar o avanço funcional permite esta **adjudicação documental de elegibilidade**. Ela não concede autorização para executar a materialização.

## 3. Definição do objeto avaliado

Para esta adjudicação, **Navigation Materialization** significa transformar as autoridades documentais existentes em um modelo explícito de navegação que possa definir, quando autorizado:

- hierarquia de acesso principal e contextual;
- entrada autenticada por contexto ativo;
- troca explícita de Organização, Coletivo ou unidade aplicável;
- relação entre entrada/síntese e domínios de trabalho;
- caminhos para objetos e responsabilidades prioritárias;
- acesso contextual a capacidades especializadas;
- handoffs e retornos legítimos entre superfícies conhecidas;
- tratamento de bloqueio, ausência, proteção e autoridade insuficiente;
- regras de retorno, interrupção e retomada;
- diferenças legítimas entre Organização e Coletivo.

Esse objeto não inclui:

- layout;
- frame;
- wireframe;
- componente;
- posição visual;
- URL;
- rota técnica;
- nomenclatura final de interface;
- responsive behavior;
- gesto;
- copy final;
- RBAC técnico;
- implementação.

```text
NAVIGATION MATERIALIZATION
→ TOPOLOGY + HIERARCHY + ENTRY/RETURN SEMANTICS
→ CONTEXT-AWARE ACCESS STRUCTURE
→ DOCUMENTARY / FUNCTIONAL

NAVIGATION MATERIALIZATION
≠ SCREEN GEOMETRY
≠ FINAL UI
≠ TECHNICAL ROUTING
```

## 4. Autoridades consumidas

### 4.1 Atores, autoridades e jobs

`GKR-UX-ORGCOL-AUTH-JOBS-001 v1.4.0` estabelece:

- a unidade autenticada `Pessoa + participante representado + contexto/unidade + papel + autoridade + job`;
- separação entre pertencimento, representação, aprovação, moderação e administração;
- contexto antes de ação;
- necessidade de revalidar autoridade na troca de contexto;
- jobs estruturais, operacionais, de governança/proteção e prestação de contas;
- distinção entre job prioritário e item de menu/tela.

Essa autoridade fornece a base para decidir **o que a navegação deve tornar encontrável**, sem decidir sua forma visual.

### 4.2 Arquitetura da Informação

`GKR-UX-ORGCOL-AUTH-IA-001 v1.3.0` estabelece:

- contexto antes de ação;
- síntese antes de volume;
- objeto antes de canal;
- autoridade antes de confirmação;
- operação separada de evidência;
- domínio informacional e responsabilidade sem transformar IA em sitemap/menu final;
- estados de autoridade, proteção, bloqueio, ausência, contestação e revisão.

Essa autoridade fornece agrupamento semântico suficiente para impedir que a navegação seja inventada a partir de telas.

### 4.3 Surface Map

`GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.0.0` fornece:

- IDs estáveis de superfícies existentes;
- crosswalk entre domínios e superfícies;
- separação de perspectivas Organização, Coletivo e Pessoa;
- lacunas explícitas onde não existe superfície exclusiva;
- preservação do `GKR-JOURNEY-SURFACE-REGISTRY-001`.

A futura navegação deve reutilizar essas identidades e não criar superfícies apenas para completar simetria.

### 4.4 State Map

`GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.0.0` fornece:

- estados materiais que alteram o que pode ser compreendido ou realizado;
- autoridade válida, insuficiente, contestada, expirada ou dependente de aprovação;
- atenção, bloqueio, pausa, encerramento e responsabilidades remanescentes;
- estados de proteção, informação incompleta, indisponibilidade e contestação;
- lifecycle bilateral Organização ↔ Coletivo sem transformar estado em transição inventada.

A navegação futura precisa ser compatível com esses estados, inclusive quando uma ação não pode ser executada.

### 4.5 Priority Flows

`GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0` fornece:

- espinha `contexto → autoridade → Momento → objeto → Próximo Passo → ação/decisão legítima`;
- fluxos prioritários de Organização, Coletivo e relação bilateral;
- conexões contextuais com Planos e capacidades especializadas;
- retorno, interrupção, concorrência, idempotência e revalidação de contexto;
- relação explícita com `GKR-TRN-*`, inclusive lacunas;
- declaração expressa de que o próximo gate elegível após a promoção é Navigation Materialization.

Essa autoridade fornece continuidade funcional suficiente para avaliar a materialização sem converter Priority Flow em sequência fixa de telas.

## 5. Condições obrigatórias para uma futura materialização

Qualquer Navigation Materialization autorizada deverá preservar cumulativamente:

### NME-01 — contexto ativo explícito

A estrutura não pode permitir atuação material sem tornar compreensível:

- qual participante está ativo;
- qual unidade/contexto se aplica;
- qual papel está ativo;
- quais limites de autoridade existem.

Troca de contexto exige revalidação e não transporta silenciosamente permissões, dados protegidos, decisão pendente ou objeto de outro contexto.

### NME-02 — Organização e Coletivo não precisam de paridade artificial

As duas experiências compartilham princípios e espinhas, mas não precisam possuir menus simétricos, mesma quantidade de entradas ou mesmas hierarquias.

```text
CONSISTÊNCIA
≠ SIMETRIA ARTIFICIAL
```

### NME-03 — jobs orientam encontrabilidade, não viram itens de menu automaticamente

A navegação deve permitir que os jobs prioritários sejam alcançáveis e compreensíveis sem exigir correspondência 1:1 entre job e item de navegação.

### NME-04 — superfícies existentes são reutilizadas

A materialização não pode criar `GKR-SURF-*` para preencher estética, simetria ou conveniência.

Nova superfície exigiria autoridade própria.

### NME-05 — transições existentes mantêm identidade e maturidade

A materialização não pode:

- criar `GKR-TRN-*` por inferência;
- promover transição parcial, proposta ou contratada;
- tratar relação conceitual como transição estável;
- esconder uma lacuna de transição sob um link visual.

### NME-06 — Visão Geral/Início não se torna dashboard total

`GKR-SURF-ORG-001` e a entrada equivalente do Coletivo devem sintetizar Momento, atenção e Próximos Passos sem absorver objetos, evidências ou fontes de verdade de outros domínios.

### NME-07 — capacidades especializadas permanecem contextuais

Planos, Intelligence, Ads, Business, Journey, Mall, Travel e Media não podem virar eixo principal apenas por existirem ou possuírem maior maturidade.

Acesso especializado deve surgir quando contexto/job/autoridade justificar.

### NME-08 — estados alternativos permanecem navegáveis e compreensíveis

A estrutura futura deve acomodar sem colapsar em happy path:

- autoridade insuficiente;
- aprovação adicional necessária;
- responsável ausente;
- informação incompleta;
- bloqueio;
- proteção;
- contestação;
- indisponibilidade;
- pausa;
- expiração;
- encerramento com responsabilidades remanescentes.

### NME-09 — retorno e interrupção não produzem mutação silenciosa

```text
NAVEGAR
≠ CONFIRMAR

VOLTAR
≠ DESFAZER AUTOMATICAMENTE

RETRY
≠ DUPLICAR EFEITO
```

A materialização deve preservar retorno ao contexto de origem quando legítimo e explicitar quando reconsulta/revalidação é necessária.

### NME-10 — bilateralidade permanece bilateral

O fluxo Organização ↔ Coletivo deve preservar duas autoridades, duas perspectivas e o mesmo objeto/escopo governado sem absorver a contraparte como recurso interno.

### NME-11 — lacunas reais permanecem lacunas

Permanecem explicitamente fora de qualquer falsa completude:

- Organização ↔ Organização onde não há autoridade própria;
- Coletivo ↔ Coletivo onde não há autoridade própria;
- continuidades sem `GKR-TRN-*` estável;
- domínio de aprendizados/evidências do Coletivo sem ID exclusivo quando assim registrado.

Essas lacunas não bloqueiam a materialização do escopo já autorizado; bloqueiam somente a invenção do que ainda não possui autoridade.

### NME-12 — navegação não concede autoridade

A existência de um caminho, entrada ou objeto encontrável não autoriza ação material.

```text
VISIBLE
≠ AUTHORIZED

ACCESSIBLE
≠ APPROVED

NAVIGABLE
≠ EFFECTIVE
```

### NME-13 — materialização permanece pré-wireframe

O resultado autorizado, se houver, deverá continuar estritamente documental/funcional.

```text
NAVIGATION MATERIALIZATION
≠ AUTHENTICATED WIREFRAMES
≠ DESIGN
≠ UI
≠ PROTOTYPE
≠ PRODUCT ENGINEERING
```

## 6. Matriz de suficiência

| Requisito para materializar navegação | Autoridade disponível | Avaliação draft |
|---|---|---|
| atores e contextos | Jobs v1.4.0 | suficiente |
| limites de autoridade | Jobs + IA + State Map | suficiente |
| agrupamento semântico | IA v1.3.0 | suficiente |
| superfícies conhecidas | Surface Map v1.0.0 | suficiente |
| estados materiais | State Map v1.0.0 | suficiente |
| continuidades prioritárias | Priority Flows v1.0.0 | suficiente |
| retornos/interrupções | Priority Flows v1.0.0 | suficiente |
| transições conhecidas e lacunas | Priority Flows + Transition Registry | suficiente sem promoção |
| capacidades especializadas | Jobs + IA + Priority Flows | suficiente como acesso contextual |
| diferenças Organização/Coletivo | Jobs + IA + Surface Map | suficiente |
| gaps O↔O / C↔C | gaps explicitamente preservados | não bloqueiam escopo definido |
| wireframes/UI | deliberadamente ausentes | não requeridos para este gate |

## 7. Findings da adjudicação

### NMF-001 — ausência de menu final não é blocker

A IA deliberadamente não definiu sitemap/menu final. Isso não representa lacuna anterior ao gate atual; é precisamente o objeto que Navigation Materialization deverá resolver se for autorizada.

**Classificação:** não bloqueante.

### NMF-002 — gaps de relações homólogas não impedem o escopo atual

Organização↔Organização e Coletivo↔Coletivo permanecem sem autoridade própria equivalente a `UXA-019`.

A materialização pode avançar no escopo documental existente desde que:

- não invente essas relações;
- não reutilize `ORG-004..006` fora de Organização↔Coletivo;
- não apresente completude inexistente.

**Classificação:** não bloqueante, com boundary explícito.

### NMF-003 — lacunas de transição não devem ser “resolvidas” pela navegação

Existem continuidades funcionais conhecidas sem transição estável declarada.

Links, entradas ou retornos futuros não podem ser usados como evidência de maturidade de `GKR-TRN-*`.

**Classificação:** não bloqueante, com preservação obrigatória de registry.

### NMF-004 — ausência de wireframes é condição esperada

Wireframes autenticados continuam `NOT STARTED`. Navigation Materialization deve precedê-los e não depende de frame visual para ser adjudicada.

**Classificação:** não bloqueante.

## 8. Conclusão canônica de elegibilidade

A cadeia documental vigente contém informação suficiente para que uma futura frente separada materialize a navegação **sem precisar inventar a arquitetura funcional primeiro**.

```text
NAVIGATION MATERIALIZATION ELIGIBILITY
→ PASS
→ ACTIVE / CANONICAL ELIGIBILITY ADJUDICATION

DOCUMENTARY PREREQUISITES
→ SUFFICIENT

MATERIAL BLOCKER PROVEN
→ NONE

NEW GKR-SURF-* REQUIRED FOR ELIGIBILITY
→ NO

NEW GKR-TRN-* REQUIRED FOR ELIGIBILITY
→ NO

TRANSITION MATURITY PROMOTION REQUIRED
→ NO

AUTHENTICATED WIREFRAMES REQUIRED BEFORE NAVIGATION MATERIALIZATION
→ NO
```

O resultado `PASS` significa que existe base documental suficiente para solicitar uma **autorização humana separada** de Navigation Materialization. A promoção desta adjudicação não concede essa autorização.

```text
ELIGIBILITY PASS
≠ MATERIALIZATION AUTHORIZED
```

## 9. Boundary de uma eventual autorização

Com esta elegibilidade promovida, uma autorização posterior de Navigation Materialization poderá permitir exclusivamente a definição documental de:

- topologia principal e contextual;
- hierarquia de acesso;
- entradas por contexto;
- troca explícita de contexto;
- caminhos entre superfícies já registradas;
- handoffs/retornos suportados pelas autoridades;
- acesso contextual a capacidades especializadas;
- comportamento documental diante de autoridade insuficiente, bloqueio, proteção, contestação e indisponibilidade.

Continuarão fora do escopo:

- wireframes;
- frames;
- layout;
- visual design;
- UI;
- protótipo;
- URLs e rotas técnicas;
- RBAC técnico;
- implementação;
- Product Engineering;
- dados reais;
- produção;
- testes com participantes reais.

## 10. Critérios consumidos na promoção desta adjudicação

A promoção canônica consumiu cumulativamente os seguintes critérios:

1. nenhuma autoridade corrente contradisser NME-01..13;
2. a matriz de suficiência permanecer suportada pelas versões correntes;
3. nenhum `GKR-SURF-*` ou `GKR-TRN-*` for criado por inferência;
4. nenhuma maturidade de transição for promovida;
5. gaps O↔O e C↔C permanecerem explícitos;
6. relação Organização↔Coletivo continuar limitada ao escopo de `UXA-019`;
7. Planos e Produtos Especializados permanecerem contextuais;
8. wireframes, Design/UI e Product Engineering permanecerem fechados;
9. Semantic State Validation concluir com sucesso;
10. Mechanical Validation concluir com sucesso;
11. revisão independente não identificar finding material;
12. qualquer finding do review ser adjudicado antes da promoção;
13. autorização de Navigation Materialization permanecer ato humano separado.

## 11. Estado governado desta frente

```text
GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001
→ ACTIVE v1.0.0
→ NORMATIVE = FALSE

FUNCTIONAL ADVANCEMENT
→ RESUMED BY HUMAN AUTHORIZATION
→ ELIGIBILITY FRONT COMPLETED

NAVIGATION MATERIALIZATION ELIGIBILITY
→ PASS
→ CANONICALLY PROMOTED / ACTIVE

NAVIGATION MATERIALIZATION
→ NOT AUTHORIZED
→ NOT MATERIALIZED

AUTHENTICATED WIREFRAMES
→ NOT STARTED / NOT RELEASED

DESIGN / UI / PROTOTYPE
→ NOT AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01 / NOT RELEASED

NEXT AUTOMATIC EXECUTION
→ NONE
```
