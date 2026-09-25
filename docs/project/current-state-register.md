---
id: GKR-STATE-001
title: Registro do Estado Atual do Guivos Knowledge Repository
status: active
version: 3.50.33
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-09-25
normative: true
maturity: current_truth_gia_cog_001_active_normative
related:
  - GKR-FULL-CORPUS-AUDIT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GEB-P01
  - GOG-001
  - GKR-BRAND-SIGNATURE-001
  - GKR-BRAND-PUBLIC-AUTHORITY-001
  - GKR-CHRISTIAN-FOUNDATION-001
  - GPA-004
  - GPA-006
  - GIA-000
  - GIA-COG-001
  - ADR-008
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
  - RP-002-PMF-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
  - GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001
  - GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001
  - GKR-GLOBAL-UPDATE-2026-09-18-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-OC-NARR-001
  - GKR-UX-HOME-OC-NAV-001
  - GKR-UX-HOME-OC-SYS-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - GKR-UX-PER002-PROTOTYPE-DELIVERY-001
  - GKR-UX-PER002-PROTOTYPE-REVALIDATION-001
  - GTM-009
  - GTM-010
  - GTM-011
  - UXA-101
  - M7.88
---

# Registro do Estado Atual do Guivos Knowledge Repository

## 1. Função desta autoridade

Este documento registra **o que pode ser afirmado hoje** sobre a Guivos e sobre o estado do Guivos Knowledge Repository.

Ele não é histórico de construção, changelog, checkpoint ou inventário de PRs.

A regra vigente do corpus é:

```text
GIT
→ preserva a história

GKR VIGENTE
→ preserva a verdade atual
→ com detalhe material suficiente
→ sem depender de versões substituídas para ser compreendido
```


A frente posterior da Cognitive Reference Architecture também foi concluída em seu limite documental: `ADR-008` aprovou placement e ownership sob a GIA; `GIA-COG-001 v0.1.1` passou por revisão, remediação, revalidação semântica e gate de promoção e é agora a **Cognitive Reference Architecture vigente, ativa e normativa**. Essa promoção não autoriza `GIA-COG-002..008`, arquitetura física, dados reais, implementação, operação ou produção.

A frente documental posterior de Organizações e Coletivos avançou por gates próprios até a Navigation Materialization canônica `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.2`. A autorização governada subsequente `GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001 v1.0.0` liberou exclusivamente os wireframes autenticados low-fidelity, a primeira entrega foi executada em `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` e a validação funcional posterior concluiu `PASS` em `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`, com 30/30 itens de cobertura, 15/15 invariantes, 12/12 desafios de estado, 0 findings materiais e nenhuma reformulação requerida. O pacote Delivery + Validation é a referência corrente low-fidelity O/C. A adjudicação pós-validação `GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001 v1.0.2` concluiu `PASS` e a decisão humana subsequente `GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001 v1.0.2` concedeu autorização para Design high-fidelity. O ato separado `GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001 v1.0.0` liberou a execução externa de Design high-fidelity; a entrega permanece `NOT_RECEIVED`. Protótipo interativo e Product Engineering continuam não liberados.

## 2. Estado executivo

O estado corrente do GKR deve ser lido por autoridade temática, não pela cronologia de construção.

```text
CURRENT MAIN
→ VERDADE DOCUMENTAL CORRENTE

GIT
→ HISTÓRICO / PROVENIÊNCIA

HISTORICAL AUDIT / SNAPSHOT / CHECKPOINT
→ NOT DESIGN INPUT
→ NOT AI INPUT
```

Estado executivo vigente:

- **Participantes estruturais:** Pessoa, Organização e Coletivo;
- **Contextos principais de experiência:** Pessoa, Coletivo, Organização e Guivos Business, preservando Business como produto especializado B2B e não como participante estrutural;
- **Homes públicas:** documentação reconciliada e pronta para Design externo, sem identidade visual canônica imposta pelo GKR;
- **Organização/Coletivo autenticados:** Jobs/autoridade, IA, Surface Map, State Map, Priority Flows, Navigation Materialization e low-fidelity principal definidos/validados; high-fidelity autorizado, com execução externa liberada e entrega ainda `NOT_RECEIVED`; protótipo interativo não autorizado;
- **Pessoa / PER-002:** fronteira funcional e referência interativa pós-review preservadas pelas autoridades específicas; autenticação continua gate interno e não autorização automática de processamento material;
- **Journey:** registries de superfícies, transições, cenários, handoffs e gaps ativos como fonte corrente;
- **Guivos Business:** produto separado de Organização e Ads, com Start · Growth · Scale · Enterprise e contratação online/Self-service quando elegível, suporte ou modelo gerenciado conforme complexidade;
- **Guivos Intelligence:** arquitetura conceitual/de referência corrente preservada; implementação física, dados reais e produção não autorizados por maturidade documental;
- **Research / mercado:** método documental não equivale a pesquisa aplicada, PMF, disposição a pagar, retenção, impacto ou causalidade comprovados;
- **Product Engineering:** permanece pausada/não liberada;
- **UXA-102 / V5:** `NOT_STARTED`;
- **execução automática seguinte:** nenhuma.

```text
DOCUMENTED
≠ IMPLEMENTED

VALIDATED DOCUMENTALLY
≠ PRODUCTION

DESIGN AUTHORIZED
≠ DESIGN EXECUTED

PROTOTYPE
≠ IMPLEMENTED PRODUCT

AUDIT COMPLETE
≠ PMF VALIDATED
```

## 3. Fundação e identidade da Guivos

A Fundação corrente permanece consolidada sem redução do conhecimento validado.

A leitura fundacional vigente é:

> **A Guivos amplia condições, percepção, acesso, conexão e possibilidades para que Pessoas, Organizações e Coletivos possam compreender melhor seu Momento, reconhecer Próximos Passos e viver experiências capazes de contribuir para sua evolução.**

A direção humana preservada é:

> **Como podemos ajudar os seres humanos a terem uma vida melhor?**

A arquitetura conceitual reconciliada distingue:

```text
MOMENTO
→ OBJETIVO / NECESSIDADE, quando houver
→ PRÓXIMO PASSO
→ POSSIBILIDADE, quando agregar valor
→ MECANISMO, quando necessário
→ OPORTUNIDADE REAL, quando existir
→ ESCOLHA
→ EXPERIÊNCIA
→ CONTRIBUIÇÃO / APRENDIZADO, quando houver evidência
→ NOVO MOMENTO
```

Definições preservadas:

> **Possibilidade é um caminho potencial de evolução compatível com um Momento.**

> **Oportunidade é uma materialização concreta de uma Possibilidade, oferecida ou viabilizada por agente legítimo, com condições reais de acesso.**

O fluxo não é obrigatório nem sempre linear. Um Próximo Passo pode não depender de uma Oportunidade externa.

Princípios estruturais:

```text
AMPLIAR POSSIBILIDADES
≠ DECIDIR PELA PESSOA

APOIAR EVOLUÇÃO
≠ DEFINIR O QUE É UMA VIDA BOA PARA CADA PESSOA

COMPREENDER CONTEXTO
≠ ASSUMIR AUTORIDADE SOBRE A PESSOA

OPORTUNIDADE
≠ ETAPA OBRIGATÓRIA

EXPERIÊNCIA
≠ IMPACTO COMPROVADO

TECNOLOGIA
≠ PRODUTO

ECOSSISTEMA
≠ SOMA DE SERVIÇOS
```

A Guivos deve continuar sendo percebida como maior do que a soma de seus Produtos Especializados: futuro, possibilidade, simplicidade, confiança, escala e centralidade humana, tecnológica sem ser fria e sofisticada sem ser desnecessariamente complexa.

A Fundação também passa a explicitar a separação:

```text
VERDADE VIGENTE
≠ VISÃO FUTURA

TARGET
≠ IMPLEMENTAÇÃO
```

A visão de capacidade máxima pode ser documentada, mas deve permanecer classificada como visão/target até possuir evidência de realização.

## 4. Fundamento Cristão

`GKR-CHRISTIAN-FOUNDATION-001 v1.0.0` permanece autoridade fundacional normativa e semanticamente consistente com as autoridades correntes.

Princípio central:

> **Evolução com propósito.**

Estado:

```text
primary_use
→ internal_governance

classification
→ public

authority_profile
→ public_foundational

external_reuse_automatic
→ false
```

A essência cristã preserva Deus como direção superior do propósito e Cristo como referência central, sem retirar autonomia, liberdade de consciência ou dignidade das pessoas.

Passagens fundamentais preservadas:

- Lucas 2:52 — crescer;
- Efésios 4:15 — direcionar;
- Efésios 5:14–17 — despertar;
- Mateus 25:14–30 — desenvolver aquilo que foi confiado;
- Colossenses 4:5 — discernir;
- Lucas 19:41–44 — reconhecer.

Narrativa convergente:

```text
DESPERTAR
→ PERCEBER
→ DISCERNIR
→ DESENVOLVER
→ CRESCER
→ APROXIMAR-SE DE DEUS
```

A existência dessa autoridade não transforma fé em mecanismo comercial, campanha, produto ou classificação de Pessoas.

## 5. Participantes estruturais

O ecossistema preserva três participantes estruturais:

```text
PESSOA
ORGANIZAÇÃO
COLETIVO
```

Eles não são planos, produtos, personas comerciais nem tipos de conta intercambiáveis.

### 5.1 Pessoa

A Pessoa permanece centro de sua própria Journey.

A Guivos pode organizar contexto, apoiar compreensão, apresentar Possibilidades, Oportunidades e Próximos Passos, mas a decisão permanece com a Pessoa.

### 5.2 Organização

Organização é entidade institucional com identidade, autoridade, responsabilidades, recursos, processos, representantes e capacidade de oferecer ou habilitar produtos, serviços, programas, benefícios, suporte, infraestrutura e Oportunidades.

```text
ORGANIZAÇÃO
≠ GUIVOS BUSINESS
≠ ANUNCIANTE
≠ PARCEIRO COMERCIAL
≠ OPORTUNIDADE
```

### 5.3 Coletivo

Coletivo é formação voluntária de pessoas reunidas por propósito, identidade, causa, interesse, território, prática, experiência ou objetivo compartilhado.

```text
COLETIVO
≠ GRUPO DE MENSAGENS
≠ AUDIÊNCIA
≠ CANAL DE MARKETING
≠ PROPRIEDADE DE ORGANIZAÇÃO
```

Apoio, financiamento, patrocínio ou infraestrutura não transferem automaticamente propósito, governança, pertencimento ou autoridade.

### 5.4 Contextos correntes de experiência

A ontologia de participantes e a topologia de experiência não são a mesma coisa.

Os **participantes estruturais** permanecem três:

```text
PESSOA
ORGANIZAÇÃO
COLETIVO
```

Nesta frente de Experience Architecture, porém, os **contextos principais de experiência** são quatro:

```text
PESSOA
COLETIVO
ORGANIZAÇÃO
BUSINESS
```

A diferença é deliberada:

```text
PESSOA / COLETIVO / ORGANIZAÇÃO
→ participantes estruturais
→ também possuem contextos próprios de experiência

GUIVOS BUSINESS
→ produto especializado B2B
→ possui contexto próprio de experiência
→ NÃO é participante estrutural
```

Portanto:

```text
CONTEXTO DE EXPERIÊNCIA
≠ TIPO DE PARTICIPANTE

BUSINESS
≠ ORGANIZAÇÃO
≠ ADS / OPPORTUNITY BOOST
≠ "COMERCIAL"
```

Ads / Opportunity Boost e fronteiras documentais permanecem capacidades/recortes auxiliares e não substituem os quatro contextos acima.

## 6. Domínios de Evolução

Os nove Domínios de Evolução permanecem o vocabulário canônico da Journey:

| ID | Domínio |
|---|---|
| JED-001 | Saúde e Bem-estar |
| JED-002 | Trabalho, Carreira e Estudos |
| JED-003 | Vida Financeira |
| JED-004 | Empreendedorismo e Projetos |
| JED-005 | Relacionamentos e Vida Social |
| JED-006 | Espiritualidade, Propósito e Valores |
| JED-007 | Viagens, Lazer, Cultura e Novas Experiências |
| JED-008 | Causas, Voluntariado e Contribuição |
| JED-009 | Organização e Equilíbrio da Vida |

`Ainda estou descobrindo` permanece estado transversal legítimo quando não existe base suficiente para classificação segura.

```text
AINDA ESTOU DESCOBRINDO
≠ DÉCIMO DOMÍNIO
```

O mesmo domínio entre Pessoa, Organização e Coletivo não cria automaticamente match, relevância, autoridade ou compartilhamento de dados.

## 7. Journey e Experience Architecture da Pessoa

A arquitetura funcional da Pessoa preserva maturidades independentes por superfície e transição.

Estado global funcional:

```text
M7.88
→ vigente

UXA-101
→ última UXA funcional numerada

UXA-102 / V5
→ NOT_STARTED
```

Responsabilidades centrais autenticadas já reconhecidas incluem:

- entrada protegida (`PER-002`) no estado autenticado definido por Q;
- Tela Hoje (`PER-008`);
- Conta e configurações (`PER-009`) como responsabilidade contratada, ainda sem materialização própria completa;
- Meus Objetivos (`PER-010`);
- Meus Próximos Passos (`PER-011`);
- Minha Evolução (`PER-012`).

Q consolidou a fronteira da primeira entrada sem criar novo identificador:

```text
PER-001 — HOME PÚBLICA
→ PER-002 — ENTRADA PROTEGIDA
→ EXPLICAÇÃO / ALTERNATIVAS ANTES DA AUTENTICAÇÃO
→ AUTENTICAÇÃO COMO GATE / ESTADO INTERNO DE PER-002
→ CONTINUAÇÃO AUTENTICADA DE PER-002
→ FINALIDADES / PRIVACIDADE / CONTROLES
→ TRN-002
→ PER-003 — ESCOLHA DE MODALIDADE
```

A autenticação concluída não encerra `PER-002` automaticamente e não autoriza processamento material. `PER-003` é a primeira superfície registrada distinta downstream após o fechamento legítimo dessa responsabilidade. `PER-008 — Tela Hoje` permanece downstream e não é a primeira responsabilidade autenticada.


Duas notas anti-regressão acompanham qualquer próximo estágio: conteúdo exibido ou interação concluída não prova compreensão; e explicação genérica de finalidades futuras ou clique em protótipo não autoriza processamento material futuro. Cada finalidade material continua exigindo disclosure/controle/autorização aplicáveis antes do processamento correspondente.

`PER-010..012` preservam validação local em seus limites próprios.

`TRN-008..013` possuem estados documentais próprios e não devem ser promovidas por simples existência de retorno visual.

Preservações:

```text
HOJE
≠ LISTA GENÉRICA DE TAREFAS

MEUS OBJETIVOS
≠ SCORE DE PRODUTIVIDADE

MEUS PRÓXIMOS PASSOS
≠ COERÇÃO

MINHA EVOLUÇÃO
≠ RANKING HUMANO
≠ RODA DA VIDA OBRIGATÓRIA
```

A rota `Login` da Home para uma Pessoa com relação já existente permanece uma rota de retomada: Q não força usuários existentes ao onboarding de primeira entrada.

A definição funcional de Q e todos os gates específicos de Design de `PER-002` não alteram a maturidade das transições: `TRN-001` permanece `partial` e `TRN-002` permanece `locally validated`. Eles não iniciam `UXA-102/V5` nem retomam Product Engineering.

## 8. Organizações e Coletivos — experiência autenticada

A frente avançou além do estado registrado nas versões globais anteriores.

### 8.1 Fundação e relações

Permanecem autoridades funcionais:

- `UXA-014` — fundação funcional de Organização e Coletivo;
- `UXA-019` — contrato funcional das relações Organização ↔ Coletivo.

### 8.2 Atores, autoridades e jobs

`GKR-UX-ORGCOL-AUTH-JOBS-001 v1.4.2` está ativo e define, antes da arquitetura visual:

- classes funcionais de atores;
- participante representado;
- contexto/unidade;
- papel declarado;
- autoridade e limites;
- jobs prioritários;
- bilateralidade das relações;
- separação entre ator funcional e RBAC técnico.

```text
ATOR FUNCIONAL
≠ ROLE TÉCNICA

JOB
≠ ITEM DE MENU
≠ TELA

AUTORIDADE DECLARADA
≠ PERMISSÃO IMPLEMENTADA
```

### 8.3 Arquitetura da Informação

`GKR-UX-ORGCOL-AUTH-IA-001 v1.3.2` está ativo em maturidade `authenticated_information_architecture_defined`. A progressão documental posterior permanece registrada nas autoridades correntes de Surface Map, State Map, Priority Flows, Navigation Materialization e wireframes autenticados.

Organização:

```text
Visão Geral
Oportunidades e Programas
Relações
Responsabilidades e Evidências
Organização e Autoridade
Planos e Capacidade [especializado/contextual]
```

Coletivo:

```text
Início
Atividades e Oportunidades
Participação
Governança e Proteção
Relações
Aprendizados e Evidências
Coletivo e Autoridade
Planos e Capacidade [especializado/contextual]
```

Princípios:

```text
CONTEXTO ANTES DE AÇÃO
SÍNTESE ANTES DE VOLUME
OBJETO ANTES DE CANAL
AUTORIDADE ANTES DE CONFIRMAÇÃO
OPERAÇÃO ≠ EVIDÊNCIA
COMERCIAL ≠ RELEVÂNCIA
ORGANIZAÇÃO ≠ COLETIVO
```

### 8.4 Mapa lógico de superfícies — estado canônico documental

`GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.1.3` está ativo como **mapa lógico-documental canônico** da experiência autenticada de Organização e Coletivo.

O mapa:

- preserva os identificadores estáveis de `GKR-JOURNEY-SURFACE-REGISTRY-001` por crosswalk, sem criar namespace paralelo;
- define cinco domínios lógicos principais para Organização e sete para Coletivo;
- mantém `Planos e Capacidade` como capacidade **comercial especializada/contextual**, ligada aos fluxos `GKR-SURF-ORG-301..304`, `GKR-SURF-COL-301..304` e `GKR-SURF-BND-002`;
- mantém explícitas as lacunas em que ainda não existe ID dedicado, sem inventar identificadores;
- não promove por inferência a maturidade individual das superfícies registradas.

### 8.5 Mapa funcional de estados — estado canônico documental

`GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.1.4` está ativo como **mapa funcional canônico documental dos estados autenticados** de Organização e Coletivo.

Ele:

- organiza estados funcionais transversais de contexto/autoridade, operação/atenção, proveniência/evidência/compreensão, proteção/governança/contestação e capacidade/disponibilidade;
- preserva `ORG-004..006` e `COL-008` exclusivamente para Organização–Coletivo sob `UXA-019`;
- mantém Organização–Organização e Coletivo–Coletivo como lacunas explícitas sem ID dedicado;
- preserva a perspectiva da Pessoa separada das superfícies operacionais do Coletivo;
- não cria namespace estável de estados;
- não cria nem promove `GKR-TRN-*`;
- não redefine estados especializados de Planos nem suas autoridades.

Estado governado:

```text
O/C MAPA LÓGICO DE SUPERFÍCIES
→ DEFINED / CANONICAL DOCUMENTARY

O/C MAPA FUNCIONAL DE ESTADOS
→ DEFINED / CANONICAL DOCUMENTARY

PRIORITY FLOWS
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY
→ GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.2

NAVIGATION MATERIALIZATION ELIGIBILITY
→ PASS / ACTIVE / CANONICAL
→ GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001 v1.0.0

NAVIGATION MATERIALIZATION
→ GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.2
→ ACTIVE / DEFINED / CANONICAL DOCUMENTARY
→ PRODUCT MENU VISUAL = NOT DEFINED

LOW-FIDELITY WIREFRAMES
→ DELIVERY v0.1.0 + VALIDATION v1.0.0 / PASS

HIGH-FIDELITY ELIGIBILITY
→ PASS / GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001 v1.0.2

HIGH-FIDELITY DESIGN AUTHORIZATION
→ GRANTED / GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001 v1.0.2
→ EXECUTION = NOT_STARTED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
→ NOT RELEASED
```

A antiga proposta pré-auditoria `agent/gkr-orgcol-authenticated-surface-map-v1` permanece somente `HOLD_REVIEW` e não é autoridade vigente.

Os Priority Flows O/C foram promovidos documentalmente em ato governado específico. A elegibilidade para **Navigation Materialization** foi adjudicada como `PASS` e a materialização documental foi posteriormente autorizada, executada, validada e promovida em `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.2`. Os **Authenticated Wireframes low-fidelity** foram então autorizados, entregues e funcionalmente validados com `PASS` por `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`. A elegibilidade high-fidelity O/C foi adjudicada como `PASS` em `GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001 v1.0.2` e a autorização humana subsequente foi concedida em `GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001 v1.0.2`. O release de execução externa high-fidelity foi emitido em `GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001 v1.0.0`; a entrega permanece `NOT_RECEIVED`. Protótipo interativo, implementação e Product Engineering continuam não liberados.

```text
DOCUMENTAÇÃO
→ DEFINE RESPONSABILIDADES, ESTADOS E FRONTEIRAS SEMÂNTICAS

DESIGN
→ DEFINE COMO A EXPERIÊNCIA É VISUALMENTE MATERIALIZADA
```

Wireframe, mockup, protótipo, layout, composição e componentes visuais **não são entregáveis normativos deste ato**. Nenhuma etapa posterior é liberada automaticamente.

## 9. Artefatos visuais e registries

O corpus corrente não utiliza inventário físico de SVGs como proxy de maturidade.

```text
PHYSICAL SVGs
→ 0

CURRENT PHYSICAL ASSOCIATIONS
→ 0

HISTORICAL VISUAL PRODUCERS
→ REMOVED / ABSORBED WHERE GOVERNED
→ GIT PRESERVES PROVENANCE

SURFACE MATURITY
→ READ FROM GKR-JOURNEY-SURFACE-REGISTRY-001

TRANSITION MATURITY
→ READ FROM GKR-JOURNEY-TRANSITION-REGISTRY-001

AGGREGATE VISUAL WIREFRAME MATURITY
→ NOT_CERTIFIED
→ NOT INFERRED
```

Referências visuais/funcionais correntes somente existem quando uma autoridade vigente as declara explicitamente. Em especial:

- Organização/Coletivo autenticados: low-fidelity corrente = `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` + `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0 / PASS`;
- `PER-002`: referência interativa corrente e validação pós-review são governadas pelas autoridades específicas de `PER-002`;
- Homes públicas: expressão visual final pertence ao Design; o GKR governa significado, função, limites e evidências, não uma identidade visual canônica.

A existência de uma referência visual local não promove automaticamente outras superfícies, protótipo, implementação ou Product Engineering.

## 10. Homes públicas — estado corrente para Design

As oito Homes públicas estão documentalmente preparadas para consumo por Design externo:

| Home | Estado corrente |
|---|---|
| Pessoa | `READY_FOR_EXTERNAL_DESIGN` |
| Organizações e Coletivos | `READY_FOR_EXTERNAL_DESIGN` |
| Mall | `READY_FOR_EXTERNAL_DESIGN` |
| Travel | `READY_FOR_EXTERNAL_DESIGN` |
| Media | `READY_FOR_EXTERNAL_DESIGN` |
| Ads | `READY_FOR_EXTERNAL_DESIGN` |
| Business | `READY_FOR_EXTERNAL_DESIGN` |
| Intelligence | `READY_FOR_EXTERNAL_DESIGN` |

A fonte de entrada é o Manifesto Canônico de Entrega para Design, seguido por quatro autoridades universais de Design, pelo Read-First e pelas fontes específicas da Home. `GKR-UX-HOMES-GENINPUT-001` entra somente quando a designer optar por usar IA.

```text
GKR
→ SIGNIFICADO
→ FUNÇÃO
→ NARRATIVA
→ ATORES / AUTORIDADE
→ LIMITES
→ EVIDÊNCIAS
→ FRONTEIRAS DE JORNADA

DESIGNER
→ TIPOGRAFIA
→ PALETA
→ IMAGENS
→ ILUSTRAÇÃO
→ GRID
→ COMPOSIÇÃO
→ COMPONENTES
→ MOTION
→ DIREÇÃO VISUAL

AI
→ OPTIONAL / DESIGNER-CONTROLLED
```

O GKR **não define identidade visual canônica** para essas Homes e não exige reconstrução de arquivos Figma, SVGs, snapshots ou explorações históricas como entrada de Design.

Preservações essenciais:

- Pessoa, Organização e Coletivo continuam participantes estruturais;
- Guivos Business continua produto especializado B2B e contexto próprio de experiência;
- Organização ≠ Business;
- Ads ≠ Business;
- Journey = Experience Layer;
- Intelligence = Produto Especializado transversal / Intelligence Layer;
- Possibilidade ≠ Oportunidade;
- publicidade paga ≠ relevância orgânica;
- Home pública ≠ experiência autenticada;
- Home documentada ≠ Home implementada.

A Journey deve ser carregada adicionalmente somente quando o protótipo atravessar da Home pública para experiência autenticada.

```text
PUBLIC HOMES
→ READY FOR DESIGN

SNAPSHOT REQUIREMENT
→ NONE

HISTORICAL FIGMA / SVG / CHECKPOINT RECONSTRUCTION
→ NOT REQUIRED

IMPLEMENTATION / PUBLICATION / PRODUCT ENGINEERING
→ SEPARATE GATES
→ NOT RELEASED BY HOME DESIGN READINESS
```

A experiência autenticada de Organização/Coletivo permanece governada por suas autoridades próprias: low-fidelity principal validado, high-fidelity autorizado, com execução externa liberada e entrega ainda `NOT_RECEIVED`, protótipo interativo não autorizado.

## 11. Guivos Business

`GPA-004 v1.7.4` permanece autoridade superior do Guivos Business. A síntese corrente da experiência está em `GKR-JOURNEY-BUSINESS-001 — Experiência Integrada do Guivos Business`.

Ofertas principais preservadas:

```text
PROGRAMAS DE INCENTIVO
+
GUIVOS JOURNEY CUSTEADO PELA EMPRESA
```

A segunda oferta é o **Guivos Journey existente**, custeado pela empresa. Não significa Journey controlado pela empresa nem nova Journey corporativa.

Direção humana:

> **Como podemos ajudar os seres humanos a terem uma vida melhor?**

Planos Business:

```text
START
→ operar

GROWTH
→ acompanhar e compreender

SCALE
→ interpretar e integrar

ENTERPRISE
→ governar em alta complexidade e escala
```

Separações obrigatórias:

```text
OFERTA
≠ PLANO
≠ ESCALA
≠ ORÇAMENTO PRÉ-PAGO
≠ MODELO DE IMPLEMENTAÇÃO
```

Contratação e operação:

```text
CONTRATAÇÃO
→ ONLINE

IMPLEMENTAÇÃO / OPERAÇÃO
→ SELF-SERVICE
→ COM APOIO DO SUPORTE
→ GERENCIADO
```

`Self-service / Com apoio / Gerenciado ≠ Start / Growth / Scale / Enterprise`.

A composição Self-service vigente deve ser lida como:

```text
OFERTA(S)
+
ESCALA / PARTICIPANTES / ACESSOS
+
CAPACIDADES REQUERIDAS
↓
PLANO COMPATÍVEL
↓
COMPOSIÇÃO DO VALOR
↓
CONTRATAÇÃO ONLINE
```

O plano é a camada de capacidade que suporta integralmente a configuração. O valor pode incluir componentes variáveis e serviços adicionais; o orçamento pré-pago de incentivo permanece recurso operacional separado da assinatura.

### 11.1 Pontos no Business

O Programa de Pontos permanece capacidade Business quando governado por suas autoridades próprias.

```text
PONTOS
≠ PAGAMENTO DE PLANO JOURNEY
≠ COMPRA DE PERTINÊNCIA
≠ RECOMENDAÇÃO
≠ PRIORIDADE
≠ EVOLUÇÃO
```

A empresa financia orçamento; concessão e uso pela Pessoa são eventos distintos.

As autoridades econômicas temáticas correntes **não definem nem aprovam equivalência Pontos ↔ BRL, valor monetário ou taxa de conversão**.

```text
PONTOS GUIVOS
→ BENEFÍCIO TRANSACIONAL DO ECOSSISTEMA

EQUIVALÊNCIA PONTOS ↔ BRL
→ NÃO APROVADA COMO REGRA ECONÔMICA VIGENTE
→ SEM TAXA / VALOR MONETÁRIO APROVADO POR AUTORIDADE ECONÔMICA VIGENTE
→ NÃO AUTORIZADA PARA IMPLEMENTAÇÃO, COBRANÇA OU LIQUIDAÇÃO
→ REQUER AUTORIDADE ECONÔMICA ESPECÍFICA PARA VOLTAR A SER REGRA CORRENTE
```

`VALOR DE IMPACTO LIBERADO ≠ impacto realizado ≠ impacto comprovado`.

Pontos permanecem fora da narrativa pública da Home Business conforme decisão vigente, sem eliminar a capacidade funcional.

### 11.2 Business × Organização × Ads × Intelligence

```text
ORGANIZAÇÃO
≠ BUSINESS
≠ ADS

COM-* NO JOURNEY REGISTRY
→ ADS / OPPORTUNITY BOOST
→ NÃO BUSINESS

BND-*
→ FRONTEIRAS DOCUMENTAIS
→ NÃO BUSINESS

INTELLIGENCE APOIANDO BUSINESS
≠ INTELLIGENCE COMO MÓDULO BUSINESS
≠ ACESSO IRRESTRITO A DADOS PESSOAIS
```

Uma Organização pode possuir relação comercial Business e Ads, mas isso não muda sua natureza estrutural nem compra relevância funcional.

## 12. Guivos Intelligence

`GPA-006 v2.0.1` permanece autoridade superior do Produto Especializado Guivos Intelligence.

Unidade de valor:

> **compreensão útil e contextualizada**

Duas frentes superiores:

```text
PESSOA / JOURNEY
→ contexto individual autorizado
→ compreensão + possibilidades
→ decisão permanece com a Pessoa

BUSINESS / POPULAÇÃO
→ minimização + agregação + proteção
→ indicadores + tendências + movimentos + insights
→ decisão empresarial permanece com a Empresa
```

Guardrails:

```text
INTELLIGENCE ≠ JOURNEY
INTELLIGENCE ≠ BUSINESS
COMPREENDER ≠ DECIDIR
CONHECER ≠ UTILIZAR ≠ COMPARTILHAR
PERSONALIZAR ≠ EXPOR
DECLARADO ≠ OBSERVADO ≠ INFERIDO ≠ PREDITO
INFERÊNCIA ≠ FATO
SINAL ≠ CERTEZA
TENDÊNCIA ≠ DESTINO
CORRELAÇÃO ≠ CAUSALIDADE
ENTITLEMENT ≠ AUTORIDADE
MAIOR PLANO ≠ MENOR PRIVACIDADE
PERCEBER ANTES ≠ PREVER O FUTURO
TECNOLOGIA ≠ PRODUTO
```

`GIA-000 v1.7.0` preserva CIE, LPM, GPMA e Intelligence Engines como candidatos técnicos/arquiteturais, não como implementação comprovada, reconcilia o estado documental da Home Intelligence v1 e reconhece `GIA-COG-001 v0.1.1` como arquitetura cognitiva de referência vigente.

`GIA-COG-001 v0.1.1` está `active / normative` em nível conceitual/de referência. Ela governa o fluxo cognitivo lógico, incluindo finalidade/autoridade/sensibilidade, elegibilidade pré-processamento, contexto e evidência, processamento, fusão, assurance, disclosure, projeção ao consumidor e serving, preservando `COMPREENDER ≠ DECIDIR` e `PROCESSING AUTHORIZED ≠ DISCLOSURE AUTHORIZED`.

```text
GIA-COG-001
→ ACTIVE / NORMATIVE
→ CURRENT COGNITIVE REFERENCE ARCHITECTURE
→ CONCEPTUAL / REFERENCE LEVEL

GIA-COG-002..008
→ RESERVED / NOT MATERIALIZED

ACTIVE / NORMATIVE REFERENCE ARCHITECTURE
≠ IMPLEMENTATION AUTHORIZATION
≠ REAL DATA AUTHORIZATION
≠ PRODUCTION AUTHORIZATION
```

```text
PRODUCT SOURCE LOCK
→ INTEGRATED

HOME INTELLIGENCE v1
→ MASTER EXISTS
→ CONCEPTUAL ARCHITECTURE COMPLETE

HOME SOURCE LOCK
→ GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.1.15
→ ACTIVE / NORMATIVE
→ FREEZES SOURCES AND INVARIANTS
→ DESIGN RELEASE GOVERNED BY COMMON AUTHORITY

PUBLIC HOME DESIGN
→ GRANTED FOR EXTERNAL DESIGNER

IMPLEMENTATION / PUBLICATION / PRODUCT ENGINEERING
→ NOT RELEASED
```

## 13. Grafo, dados e tecnologia

Neo4j permanece tecnologia primária de referência para a camada de grafo.

```text
NEO4J
→ reference_selected
≠ POC
≠ provisioned
≠ integrated
≠ production
```

A promoção de `GIA-COG-001` não altera esse estado nem seleciona mecanismo, fornecedor ou topologia física.

Não há autoridade suficiente para afirmar como implementados:

- GraphRAG;
- GDS em produção;
- Power BI conectado ao grafo em produção;
- ontologia física final;
- MLOps;
- APIs/serving técnico;
- pipelines de produção;
- dados pessoais reais no grafo.

```text
GRAFO GLOBAL
≠ GUIVOS INTELLIGENCE
≠ NEO4J
≠ IA
≠ GUIVOS.AI
≠ POWER BI
```

Product Engineering continua pausada antes de `W0-01` e só pode ser reativada por ato explícito próprio.

## 14. Marca, assinatura e autoridade pública

`GKR-BRAND-SIGNATURE-001 v1.3.0` permanece autoridade verbal institucional vigente.

```text
GUIVOS — GLOBAL
→ Possibility, lived.

GUIVOS — PT
→ Possibilidade, vivida.

HASHTAG GLOBAL
→ #PossibilityLived
```

Autoridade pública humana:

```text
Guilherme Oliveira
→ Founder of Guivos / Fundador da Guivos
→ principal referência humana pública inicial
```

Assinatura pessoal/autoral:

```text
Do possível ao vivido.
→ FUNDADOR
→ NÃO é assinatura institucional da Guivos
```

Lucas 2:52 permanece referência deliberada da bio pública pessoal do fundador, sem se tornar copy institucional automática.

```text
GUIVOS
≠ FUNDADOR

FALA PESSOAL
≠ POSICIONAMENTO INSTITUCIONAL
```

`GKR-BRAND-PUBLIC-AUTHORITY-001` também permanece preservado. `GKR-BRAND-PUBLIC-AUTHORITY-PROPAGATION-001` foi adjudicado no fechamento de `F-010` como `KEEP TEMPORARILY`: continua transitório, não normativo e parcialmente absorvido, preservando rastreabilidade enquanto seus próprios gates de absorção permanecem aplicáveis. A decisão sob `F-010` está encerrada; eventual remoção futura depende exclusivamente dos critérios internos de `REMOVE_AFTER_ABSORPTION` da própria propagation, sem perda de conhecimento vigente.

## 15. Proteção marcária

Portfólio brasileiro GUIVOS reconciliado:

| Processo | Classe | Estado |
|---|---:|---|
| 932319793 | 09 | registro em vigor |
| 932319920 | 39 | registro em vigor |
| 932319971 | 42 | registro em vigor |
| 932412840 | 35 | registro em vigor |

A continuidade `CLUBE DE VIAGENS E TURISMO LTDA → GUIVOS LTDA` permanece reconciliada pelo mesmo CNPJ informado nas autoridades correspondentes.

Assinaturas:

```text
Possibility, lived.
→ CLEAR
→ classes 35 e 42 = FILE

Possibilidade, vivida.
→ CLEAR
→ classes 35 e 42 = FILE
```

Estado de execução:

```text
authorization_package_prepared = true
filing_authorized = false
GRU_issued = false
GRU_paid = false
signature_filed = false
signature_registered = false
```

Próximo gate: **Human Filing Authorization**.

```text
FILE
≠ FILING_AUTHORIZED

CLEAR
≠ REGISTRO
```

AIaaS continua condicional na classe 42: incluir somente com evidência de atividade efetiva/objeto compatível.

## 16. Go-to-Market e presença pública

As seguintes autoridades estão ativas e integradas:

- `GTM-009` — Instagram Guivos — Presença, Arquitetura Editorial e Governança v1;
- `GTM-010` — Instagram do Fundador — Especificação Mestre v1;
- `GTM-011` — Instagram do Fundador — Especificação Operacional v1.

Preservação:

```text
PRESENÇA INSTITUCIONAL GUIVOS
≠ PRESENÇA PESSOAL DO FUNDADOR
```

A documentação dessas frentes não significa que toda configuração ou publicação real já tenha sido executada.

## 17. Research, supply e RP-002

O RP-002 ampliou o entendimento de Possibilidade, Oportunidade, supply contextual, Organização, Coletivo e método de validação.

Formulações preservadas em Research e agora reconciliadas na Fundação:

> **Possibilidade é um caminho potencial de evolução compatível com um Momento.**

> **Oportunidade é uma materialização concreta desse caminho, oferecida ou viabilizada por um agente legítimo, com condições reais de acesso.**

```text
MOMENTO
→ OBJETIVO / NECESSIDADE
→ PRÓXIMO PASSO
→ POSSIBILIDADE, quando agrega valor
→ MECANISMO
→ OPORTUNIDADE REAL
→ EXPERIÊNCIA
→ CONTRIBUIÇÃO
→ NOVO MOMENTO
```

Princípio de relevância:

> **A relevância pertence à relação Pessoa ↔ Oportunidade.**

```text
POPULARIDADE
≠ RELEVÂNCIA

QUALIDADE DO PROVIDER
≠ FIT CONTEXTUAL

PAGAR
≠ SER MAIS RELEVANTE
```

### 17.1 Readiness atual do RP-002

```text
CONCEPTUAL READINESS
→ PASS

METHODOLOGICAL READINESS
→ PASS

FIELD KIT v0.1
→ FROZEN FOR FIRST DRY RUN

METHOD / ANALYSIS PLAN
→ FROZEN v1.0.0

DOCUMENTATION PHASE OF MINIMUM PILOT STACK
→ CLOSED
→ PASS DOCUMENTAL

OPERATIONAL IMPLEMENTATION
→ DEFERRED BY DECISION

OPERATIONAL READINESS
→ HOLD

P3-C
→ HOLD

P3-D
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED

PMF
→ NOT VALIDATED
```

`PASS DOCUMENTAL` não significa implementação, teste do stack real, revisão jurídica final, liberação operacional ou PMF.

Simulações sintéticas não são evidência de PMF.

## 18. Stack mínimo privacy-first do piloto

A documentação do stack mínimo está fechada no limite documental, mas a implementação operacional foi deliberadamente adiada.

Elementos documentados incluem:

- research mailbox;
- Identity Vault target;
- Research Base target;
- Linkage Key target;
- backup/recovery target;
- correction/deletion drill design;
- OpenAI API target e controles previstos;
- Search/Web target;
- retenção;
- Notice;
- revisão final prevista antes de campo.

A1 Research Mailbox possui PASS documental/operacional nos limites explicitamente evidenciados por seu próprio registro; isso não promove o restante do stack.

Identity Vault e demais componentes que exigem configuração física continuam sem prova operacional quando não executados.

O fechamento da auditoria integral do corpus não reabre a decisão de adiar a implantação.

## 19. Privacidade e direitos

Estados do piloto já registrados por autoridades próprias incluem:

```text
P1A — instituição da identidade/controlador
→ PASS

P1B — controlador formal
→ PASS

P2B — canal oficial de privacidade
→ PASS

P2C — processo sintético de direitos
→ PASS
```

Canais funcionais de privacidade documentados:

- `privacy@guivos.com`;
- `privacidade@guivos.com`.

O GKR público não armazena credenciais, tokens, senhas, recovery materials, PIMs, keyfiles, IDs internos sensíveis de mailbox ou dados reais de participantes.

Separações:

```text
ACEITE CONTRATUAL
≠ CONSENTIMENTO LGPD
≠ PREFERÊNCIA VOLUNTÁRIA

ARQUITETURA DE PRIVACIDADE
≠ CONFORMIDADE OPERACIONAL COMPROVADA

CONTROLE PROJETADO
≠ CONTROLE IMPLEMENTADO
≠ CONTROLE EVIDENCIADO
```

## 20. Public Canon

`GOG-001 — Guia Oficial da Guivos v5.3.0` é a principal superfície institucional classificada como `public-canon` no estado atual documentado.

O GOG corrente permanece alinhado à Fundação e ao RP-002 para:

- distinguir Possibilidade, Mecanismo e Oportunidade;
- remover a leitura de Oportunidade como caminho universal;
- atualizar o fluxo público da Journey;
- preservar a separação Guivos × fundador;
- explicitar Intelligence como Produto Especializado transversal sem reduzi-lo a tecnologia isolada;
- retirar a contagem física de SVGs como claim de maturidade visual validada;
- manter separação explícita entre visão, arquitetura, implementação, operação e evidência.

Nenhum texto público pode promover estado superior ao suportado internamente.

```text
VISÃO
≠ DISPONIBILIDADE

ARQUITETURA
≠ IMPLEMENTAÇÃO

CLEAR
≠ REGISTRO

FILE
≠ PROTOCOLO

DESIGN DELIVERY
≠ FUNCTIONAL VALIDATION

FUNCTIONALLY VALIDATED LOW-FIDELITY
≠ HIGH-FIDELITY UI
≠ PRODUCTION UI

VALIDATED HIGH-FIDELITY DESIGN REFERENCE
≠ INTERACTIVE PROTOTYPE
≠ IMPLEMENTED UI

PROTOTYPE AUTHORIZATION
≠ PROTOTYPE EXECUTION
≠ IMPLEMENTATION
```

## 21. Programa P0–P9

P0–P9 permanece documentalmente consolidado no limite de suas autoridades.

```text
P0–P9 DOCUMENTALMENTE CONSOLIDADO
≠ NEGÓCIO IMPLEMENTADO
≠ MERCADO VALIDADO
≠ TECNOLOGIA EM PRODUÇÃO
≠ OPERAÇÃO JURÍDICA/FISCAL CONCLUÍDA
```

O fechamento da auditoria preserva o conhecimento vigente e o histórico Git; eventual cleanup futuro permanece sujeito à mesma regra de absorção sem perda e não reabre automaticamente decisões de domínio.

## 22. Fundação Guivos e institucional

`Fundação Guivos` permanece:

```text
conceito institucional social validado
+ nome de trabalho
≠ forma jurídica escolhida
≠ entidade constituída
≠ CNPJ/registro próprio comprovado
≠ operação social própria comprovada
```

Nenhuma limpeza documental pode promover esse estado por inferência.

## 23. Internacionalização

Baseline territorial candidata preservada:

```text
Belo Horizonte
→ São Paulo
→ amplificação nacional seletiva
→ Portugal / Lisboa
→ Portugal / Porto somente após gate
→ novo país europeu somente mediante novo gate
```

Portugal permanece `T1_candidate` enquanto as evidências e gates correspondentes não forem satisfeitos.

Não estão comprovados apenas pela documentação:

- entidade/filial portuguesa;
- equipe local;
- contratos locais;
- IVA/OSS em operação;
- PSP europeu em produção;
- suporte internacional em produção;
- piloto Lisboa executado;
- Porto autorizado;
- segundo país europeu autorizado.

## 24. Mercado e evidência ainda ausentes

Continuam dependentes de evidência real:

- aplicação e resultados válidos da validação B2C;
- PMF;
- disposição a pagar;
- retenção/recorrência;
- uso real e resultado de ofertas;
- evidência longitudinal real;
- impacto real;
- causalidade demonstrada quando alegada;
- performance real das Homes;
- conversão real dos canais GTM.

```text
MÉTODO DEFINIDO
≠ INSTRUMENTO APLICADO
≠ BASE VÁLIDA
≠ KPI CALCULADO
≠ DECISÃO DE MERCADO
≠ PMF
```

## 25. Dívidas e gates reais ainda abertos

Permanecem abertos quando dependentes de realidade, materialização, Design, implementação, operação ou autoridade própria:

- validação B2C real;
- PMF e disposição a pagar;
- POC/provisionamento/produção Neo4j;
- GraphRAG/GDS/Power BI em produção;
- modelo físico/ontologia/serving/MLOps final do Intelligence;
- `GIA-COG-002..008` somente mediante necessidade material e autorização própria;
- constituição jurídica de eventual veículo social;
- superfícies legais e controles de privacidade em produção;
- piloto internacional real;
- entidade/equipe/fiscalidade/pagamentos internacionais;
- cobrança real e gateway;
- handoffs Journey → Mall e Journey → Travel;
- materialização de `PER-009` somente se necessária;
- arquitetura técnica final de analytics/Intelligence Business;
- regras econômicas restantes de Pontos;
- operação Ads real, pricing, inventário e mensuração;
- Human Filing Authorization das aplicações das assinaturas;
- evidência de atividade efetiva para AIaaS se incluído;
- implantação real do perfil pessoal do fundador;
- publicação real de conteúdo do fundador;
- execução de Design high-fidelity O/C, já autorizada e liberada para execução externa por `GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001 v1.0.0`, com entrega ainda `NOT_RECEIVED`;
- protótipo interativo O/C, ainda não autorizado/não liberado;
- UXA-102/V5;
- Product Engineering.

## 26. Auditoria integral do corpus — referência de proveniência

A auditoria integral anterior está concluída e sua proveniência permanece no Git e nas autoridades de auditoria correspondentes. Este Registro do Estado Atual **não reproduz lotes, checkpoints, SHAs, contagens históricas ou sequência de remediações**.

Para consumo corrente:

```text
ESTADO ATUAL
→ ESTE REGISTRO + AUTORIDADES TEMÁTICAS VIGENTES

AUDITORIAS / LOTES / CHECKPOINTS / BASELINES HISTÓRICAS
→ GIT / PROVENIÊNCIA
→ NOT DESIGN INPUT
→ NOT AI INPUT

AUDITORIA CONCLUÍDA
≠ IMPLEMENTAÇÃO
≠ PRODUÇÃO
≠ PMF VALIDADO
```

Os estados específicos de `PER-002`, arquitetura cognitiva, Organização/Coletivo, Homes, Business, Intelligence, tecnologia, Research e demais domínios devem ser lidos diretamente nas respectivas seções correntes deste registro e nas autoridades temáticas citadas.

## 27. Regra de navegação corrente

O `mkdocs.yml` funciona como superfície de descoberta do corpus e organiza hubs por domínio e rotas de consumo multiequipe sem transformar o MENU em inventário completo de arquivos.

```text
MENU
→ SUPERFÍCIE DE DESCOBERTA
→ HUBS / AUTORIDADES DE ENTRADA
→ ROTAS MULTIEQUIPE

NOT_IN_NAV
≠ PRIVATE
≠ DEPRECATED
≠ NON-AUTHORITATIVE

REPOSITORY NAVIGATION
≠ PRODUCT INFORMATION ARCHITECTURE
≠ EXPERIENCE NAVIGATION
≠ UI NAVIGATION
```

Documentos vigentes não precisam estar diretamente listados no MENU para manter autoridade, desde que permaneçam alcançáveis por hubs, links internos, busca e Git.

Uma mesma autoridade pode atender várias rotas; o GKR não cria cópias paralelas por equipe. Evidência de builds, SHAs e validações históricas pertence ao Git e aos workflows, não a esta regra de navegação corrente.

## 28. Preservações finais e regra de não inferência

```text
ORGANIZAÇÃO ≠ GUIVOS BUSINESS ≠ GUIVOS ADS
EMPRESA COMO INÍCIO DO CONTRATO BUSINESS ≠ NOVO PARTICIPANTE ESTRUTURAL
OFERTA ≠ PLANO ≠ ESCALA ≠ ORÇAMENTO PRÉ-PAGO ≠ MODELO DE IMPLEMENTAÇÃO
CONTRATAÇÃO ONLINE ≠ MODELO DE IMPLEMENTAÇÃO/OPERAÇÃO
CUSTEIO DA JOURNEY ≠ PROPRIEDADE DA JOURNEY ≠ ACESSO AO CONTEXTO PESSOAL
PONTOS ≠ EVOLUÇÃO ≠ RELEVÂNCIA ≠ PRIORIDADE
VALOR DE IMPACTO LIBERADO ≠ IMPACTO REALIZADO ≠ IMPACTO COMPROVADO
INTELLIGENCE BUSINESS ≠ INGESTÃO OBRIGATÓRIA DE KPIs INTERNOS
INTELLIGENCE APOIANDO BUSINESS ≠ MÓDULO BUSINESS
ENTITLEMENT ≠ AUTORIDADE
MAIOR PLANO ≠ MENOR PRIVACIDADE
GRAPH / KNOWLEDGE / ANALYTICS / AI ≠ IDENTIDADE DO PRODUTO
NEO4J = REFERENCE_SELECTED ≠ PRODUCTION
GRAPHRAG = CANDIDATO ≠ IMPLEMENTAÇÃO
POWER BI = CONSUMIDOR POSSÍVEL ≠ FONTE DE VERDADE
GUIVOS.AI = POSSÍVEL SUPERFÍCIE ≠ GUIVOS INTELLIGENCE
PERCEBER ANTES ≠ PREVER O FUTURO
ACTIVE / NORMATIVE REFERENCE ARCHITECTURE ≠ IMPLEMENTATION AUTHORIZATION
GIA-COG-001 ACTIVE / NORMATIVE ≠ GIA-COG-002..008 AUTHORIZED
GUIVOS ≠ FUNDADOR
DO POSSÍVEL AO VIVIDO. → FUNDADOR
POSSIBILITY, LIVED. → GUIVOS
POSSIBILIDADE, VIVIDA. → GUIVOS
LUCAS 2:52 NA BIO DO FUNDADOR ≠ COPY INSTITUCIONAL AUTOMÁTICA
HOME DOCUMENTADA ≠ HOME IMPLEMENTADA
SOURCE LOCK ≠ AUTORIZAÇÃO AUTOMÁTICA DE DESIGN
ARTEFATO FÍSICO ≠ AUTORIDADE VIGENTE
AUDITORIA DOCUMENTAL ≠ EVIDÊNCIA OPERACIONAL
CONSOLIDAÇÃO ≠ REDUÇÃO DE CONHECIMENTO
HISTÓRICO P1–P5 ≠ SEQUÊNCIA OPERACIONAL ATUAL
DESIGN HANDOFF HISTÓRICO ≠ AUTORIZAÇÃO ATUAL DE DESIGN
DESIGN HANDOFF BOUNDARY ≠ DESIGN AUTHORIZATION
DESIGN AUTHORIZATION ≠ DESIGN DELIVERY ≠ FUNCTIONAL VALIDATION
FUNCTIONAL VALIDATION PASS ≠ HIGH-FIDELITY AUTHORIZATION
HIGH-FIDELITY ELIGIBILITY ≠ HIGH-FIDELITY AUTHORIZATION ≠ EXECUTION
HIGH-FIDELITY AUTHORIZATION ≠ HIGH-FIDELITY EXECUTION ≠ PROTOTYPE
HIGH-FIDELITY DELIVERY ≠ HIGH-FIDELITY VALIDATION
HIGH-FIDELITY VALIDATION PASS ≠ PROTOTYPE AUTHORIZATION
PROTOTYPE ELIGIBILITY ≠ PROTOTYPE AUTHORIZATION ≠ PROTOTYPE EXECUTION
PROTOTYPE AUTHORIZATION ≠ PROTOTYPE EXECUTION ≠ PROTOTYPE VALIDATION
PROTOTYPE VALIDATION PRE-REVIEW ≠ CURRENT POST-REVIEW CONCLUSION
PROTOTYPE ≠ IMPLEMENTED PRODUCT ≠ REAL AUTHENTICATION ≠ REAL DATA PROCESSING
DISPLAYED ≠ UNDERSTOOD
CLICKED ≠ UNDERSTOOD
GENERIC PURPOSE EXPLANATION ≠ FUTURE PROCESSING AUTHORIZATION

AUDIT COMPLETE
≠ PRODUTO IMPLEMENTADO
≠ PMF VALIDADO
≠ TECNOLOGIA EM PRODUÇÃO

P PASS
≠ Q EXECUTADO AUTOMATICAMENTE

Q RELEASE ELIGIBILITY PASS
≠ Q FUNCTIONAL DEFINITION COMPLETED AUTOMATICAMENTE

Q FUNCTIONAL DEFINITION PASS
≠ MATERIALIZATION AUTHORIZED

MATERIALIZATION ELIGIBILITY PASS
≠ DESIGN AUTHORIZATION

DESIGN AUTHORIZATION GRANTED
≠ DESIGN DELIVERY

DESIGN DELIVERY EXECUTED
≠ FUNCTIONAL VALIDATION PASS

FUNCTIONAL VALIDATION PASS
≠ HIGH-FIDELITY AUTHORIZATION

HIGH-FIDELITY ELIGIBILITY PASS
≠ HIGH-FIDELITY AUTHORIZATION
≠ EXECUTION

HIGH-FIDELITY AUTHORIZATION GRANTED
≠ HIGH-FIDELITY EXECUTION

HIGH-FIDELITY DELIVERY EXECUTED
≠ HIGH-FIDELITY VALIDATION PASS

HIGH-FIDELITY VALIDATION PASS
≠ PROTOTYPE AUTHORIZATION

PROTOTYPE ELIGIBILITY PASS
≠ PROTOTYPE AUTHORIZATION
≠ PROTOTYPE EXECUTION

PROTOTYPE AUTHORIZATION GRANTED
≠ PROTOTYPE EXECUTION

PROTOTYPE EXECUTION
≠ PROTOTYPE VALIDATION
≠ IMPLEMENTATION

PROTOTYPE VALIDATION PRE-REVIEW
≠ CURRENT POST-REVIEW CONCLUSION

PROTOTYPE
≠ IMPLEMENTED PRODUCT
≠ REAL AUTHENTICATION
≠ REAL DATA PROCESSING

DISPLAYED
≠ UNDERSTOOD

CLICKED
≠ UNDERSTOOD

GENERIC PURPOSE EXPLANATION
≠ FUTURE PROCESSING AUTHORIZATION

GIA-COG-001 ACTIVE / NORMATIVE
≠ GIA-COG-002..008 AUTHORIZED
≠ IMPLEMENTATION AUTHORIZED

O/C SURFACE MAP + STATE MAP + PRIORITY FLOWS DOCUMENTARY DEFINED
≠ MATERIALIZED NAVIGATION
≠ WIREFRAME
≠ UI
≠ IMPLEMENTATION

STATE MAP DEFINED
≠ GKR-TRN-* PROMOTED
≠ GKR-SURF-* PROMOTED BY INFERENCE
≠ MATERIALIZED NAVIGATION
```
## 29. Gates correntes sem execução automática

Este Registro não define uma fila automática de próximos atos.

```text
NEXT AUTOMATIC EXECUTION
→ NONE

O/C HIGH-FIDELITY DESIGN
→ AUTHORIZATION GRANTED
→ EXECUTION RELEASE ISSUED
→ EXTERNAL DELIVERY NOT_RECEIVED

O/C INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED

GIA-COG-002..008
→ RESERVED / NOT MATERIALIZED
→ NOT AUTHORIZED BY INFERENCE

REAL MARKET / PMF / REAL PARTICIPANT TESTING
→ DEPENDS ON REAL EVIDENCE AND OWN GOVERNED ACTS

IMPLEMENTATION / PRODUCTION
→ NOT AUTHORIZED BY DOCUMENTARY MATURITY ALONE
```

Qualquer avanço deve partir da autoridade temática vigente e do gate específico aplicável. Nenhum snapshot, Source Lock, protótipo, implementação, operação, teste com participantes reais ou Engenharia de Produto é criado por inferência a partir deste registro.

## 30. Home Masters — estado corrente

Os oito Documentos Mestres são a fonte direta de verdade das Homes públicas.

```text
PESSOA
→ GKR-UX-HOME-MASTER-001 v1.0.7

ORGANIZAÇÕES E COLETIVOS
→ GKR-UX-HOME-OC-MASTER-001 v1.0.6

MALL
→ GKR-UX-HOME-MALL-MASTER-001 v1.1.3

TRAVEL
→ GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.5

MEDIA
→ GKR-UX-HOME-MEDIA-MASTER-001 v1.0.3

ADS
→ GKR-UX-HOME-ADS-MASTER-001 v1.0.3

BUSINESS
→ GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.9

INTELLIGENCE
→ GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.13

QUICK-REFERENCE MOVEMENTS
→ 83 / 83

HISTORICAL REMEDIATION / CHECKPOINT INPUT
→ NOT REQUIRED
```

Auditorias, remediações, candidatos e snapshots usados para chegar a este estado não fazem parte da cadeia operacional corrente. O Git preserva sua proveniência.

## 31. Homes públicas — fonte corrente para Design e IA opcional

```text
PRIMARY SOURCE OF TRUTH
→ CURRENT MAIN

AUTHORIZED WHITELIST
→ GKR-UX-HOMES-DESIGN-DELIVERY-001 v7.0.44

UNIVERSAL DESIGN AUTHORITIES
→ HANDOFF v1.7.10
→ READINESS v1.3.26
→ FLOW v3.1.3
→ RELEASE v1.3.2

OPTIONAL AI AUTHORITY
→ GENINPUT v2.3.15
→ ONLY WHEN AI IS USED

READ-FIRST ROUTERS
→ 8 / 8 CURRENT / NON-NORMATIVE

DESIGN PRODUCTION READINESS
→ PASS / CURRENT

DESIGN PRODUCTION RELEASE
→ GRANTED

SNAPSHOT REQUIREMENT
→ NONE

CANDIDATE REQUIREMENT
→ NONE

HISTORICAL PACKAGE INPUT
→ EXCLUDED

DESIGNER
→ CREATIVE AUTHOR

AI
→ OPTIONAL / DESIGNER-CONTROLLED

GKR-CREATED FIGMA
→ NONE

VISUAL IDENTITY
→ DESIGN-OWNED

O/C AUTHENTICATED HIGH-FIDELITY
→ ELIGIBILITY PASS
→ AUTHORIZATION GRANTED / GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001 v1.0.2
→ EXECUTION RELEASE ISSUED / GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001 v1.0.0
→ HIGH-FIDELITY DELIVERY NOT_RECEIVED
→ HIGH-FIDELITY VALIDATION NOT_STARTED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

A designer pode consumir diretamente o Manifesto corrente, as quatro autoridades universais, o Read-First e as fontes específicas da Home. Quando usar IA, acrescenta `GKR-UX-HOMES-GENINPUT-001`. Journey é carregado apenas quando a solução atravessa para experiência autenticada.

## 32. Regra corrente de atualização

```text
VALIDATED CHANGE
→ UPDATE EXISTING CANONICAL AUTHORITY

MASTER CHANGE
→ UPDATE MASTER + MANIFEST + AFFECTED CURRENT AUTHORITIES

SNAPSHOT
→ ONLY FOR A REAL EXTERNAL FREEZE / TRANSPORT NEED

CANDIDATE
→ NOT CREATED BY DEFAULT

HISTORY
→ GIT
```
