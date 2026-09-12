---
id: GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
title: Organizações e Coletivos — Mapa de Superfícies da Experiência Autenticada
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-12
normative: false
maturity: authenticated_surface_map_defined_pre_state_flow_wireframe
depends_on:
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - UXA-014
  - UXA-019
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-INTEL-DASH-KPI-ANALYTICS-MASTER-001
---

# Organizações e Coletivos — Mapa de Superfícies da Experiência Autenticada

## 1. Finalidade

Este documento define o **mapa lógico de superfícies autenticadas** de Organização e Coletivo a partir da Arquitetura da Informação vigente.

Ele responde à pergunta:

> **Quais superfícies lógicas precisam existir para que uma pessoa autenticada atue no contexto de uma Organização ou de um Coletivo sem misturar contexto, autoridade, trabalho, governança, evidência e capacidades especializadas?**

Esta etapa materializa superfícies. Ela **não** materializa estados, fluxos, wireframes, UI ou implementação.

```text
JOBS AUTENTICADOS
+
ARQUITETURA DA INFORMAÇÃO
↓
MAPA LÓGICO DE SUPERFÍCIES

MAPA DE SUPERFÍCIES
≠ MAPA DE ESTADOS
≠ FLUXO
≠ ROTA / URL
≠ MENU VISUAL
≠ WIREFRAME
≠ UI
≠ RBAC TÉCNICO
≠ IMPLEMENTAÇÃO
```

## 2. Autoridade e leitura

Este mapa é derivado principalmente de:

1. `GKR-UX-ORGCOL-AUTH-IA-001` — agrupamentos, camadas e domínios da experiência autenticada;
2. `GKR-UX-ORGCOL-AUTH-JOBS-001` — atores, limites de autoridade e jobs que justificam os domínios;
3. `GKR-UX-ORGCOL-STATE-001` — estado mestre e separação entre conhecimento vigente e materializações ainda pendentes;
4. `UXA-014` e `UXA-019` — distinção estrutural entre Organização e Coletivo e limites de suas relações.

Nenhuma superfície criada aqui pode ampliar autoridade, inventar papel, tornar dado visível por padrão ou transformar uma possibilidade de produto em direito de acesso.

## 3. O que é uma superfície lógica

Neste documento, **superfície lógica** significa uma área coerente de trabalho e compreensão pertencente a um contexto autenticado.

Uma superfície lógica:

- possui um propósito semântico próprio;
- agrupa objetos e ações do mesmo domínio;
- mantém referência explícita ao participante e ao contexto ativos;
- pode ter sua disponibilidade condicionada por autoridade, política, dados e capacidade existente;
- pode futuramente ser materializada em uma ou mais telas sem que isso esteja decidido aqui.

Uma superfície lógica **não é**, por definição:

- uma URL;
- uma rota técnica;
- um item obrigatório de menu;
- uma aba;
- uma tela única;
- um componente visual;
- uma permissão;
- um papel de negócio;
- um estado de interface.

Os códigos `ORG-Sxx` e `COL-Sxx` usados abaixo são **referências locais deste mapa**, criadas apenas para tornar o documento rastreável. Eles não constituem rotas, IDs técnicos nem novos objetos de domínio.

## 4. Modelo de contexto

A Pessoa autenticada permanece o agente humano que acessa a Guivos. Organização e Coletivo são contextos distintos nos quais essa Pessoa pode atuar quando existe relação e autoridade aplicáveis.

```text
PESSOA AUTENTICADA
↓
CONTEXTO PESSOAL
↓ quando legitimamente disponível
┌──────────────────────┬──────────────────────┐
│ CONTEXTO ORGANIZAÇÃO │ CONTEXTO COLETIVO    │
└──────────────────────┴──────────────────────┘
```

A mudança de contexto não concede privilégio.

```text
ACESSAR UM CONTEXTO
≠ RECEBER AUTORIDADE

VER UMA SUPERFÍCIE NO MAPA
≠ PODER ACESSÁ-LA EM QUALQUER SITUAÇÃO

PERTENCER
≠ REPRESENTAR
≠ APROVAR
≠ ADMINISTRAR
```

O mapa define **onde um domínio pertence**. A autoridade vigente define **se, como e até onde** determinada pessoa pode atuar nele.

## 5. Mapa de superfícies — Organização

A Organização possui cinco superfícies-base e uma superfície especializada/contextual, preservando exatamente os domínios definidos pela Arquitetura da Informação.

```text
ORGANIZAÇÃO
├── ORG-S01 — Visão Geral
├── ORG-S02 — Oportunidades e Programas
├── ORG-S03 — Relações
├── ORG-S04 — Responsabilidades e Evidências
├── ORG-S05 — Organização e Autoridade
└── ORG-S06 — Planos e Capacidade [especializada / contextual]
```

### 5.1 ORG-S01 — Visão Geral

**Função:** orientar a pessoa sobre o contexto institucional ativo e sintetizar o que merece atenção agora.

Pode reunir, em síntese limitada:

- identidade e contexto da Organização;
- papel e limites da pessoa autenticada;
- itens materiais em andamento;
- atenção requerida;
- referências para os domínios responsáveis pelos objetos apresentados.

Preservação:

> **Visão Geral orienta; não substitui as superfícies de domínio e não se transforma em painel administrativo total.**

A composição exata de cards, métricas, blocos ou chamadas permanece fora deste documento.

### 5.2 ORG-S02 — Oportunidades e Programas

**Função:** concentrar o trabalho relacionado às oportunidades, programas e registros aplicáveis à Organização.

Pertencem semanticamente aqui, quando sustentados pelas autoridades e pelos dados vigentes:

- oportunidades ligadas à Organização;
- programas e iniciativas relevantes;
- referências operacionais necessárias para compreender sua participação;
- continuidade do trabalho associado a esses objetos.

A presença de uma oportunidade nesta superfície não implica relevância universal, prioridade comercial ou maior força de evidência.

### 5.3 ORG-S03 — Relações

**Função:** concentrar relações da Organização com Pessoas, Coletivos, outras Organizações ou contrapartes quando essas relações são legitimamente representáveis no contexto autenticado.

Esta superfície preserva a diferença entre:

```text
RELAÇÃO
≠ GOVERNANÇA
≠ PARTICIPAÇÃO
≠ AUTORIDADE ADMINISTRATIVA
```

Ela não cria automaticamente acesso a dados da contraparte nem converte vínculo em representação.

### 5.4 ORG-S04 — Responsabilidades e Evidências

**Função:** localizar compromissos, responsabilidades, entregas e evidências que pertencem à atuação institucional da Organização.

Pode reunir objetos relacionados a:

- responsabilidades assumidas;
- compromissos verificáveis;
- entregas;
- prestação de contas;
- evidências associadas ao trabalho realizado;
- continuidade ou revisão desses objetos.

Atividade realizada não deve ser apresentada automaticamente como impacto, avanço ou causalidade comprovada.

### 5.5 ORG-S05 — Organização e Autoridade

**Função:** concentrar os elementos institucionais de gestão, representação, pertencimento administrativo e autoridade que legitimamente pertencem à Organização.

A superfície pode abrigar controles de gestão somente quando o papel e a autoridade aplicáveis os permitem.

Preservações:

```text
CONTEXTO ORGANIZAÇÃO
≠ PAPEL ADMINISTRATIVO

REPRESENTAÇÃO
≠ APROVAÇÃO IRRESTRITA

GESTÃO DA ORGANIZAÇÃO
≠ AUTORIDADE SOBRE A JOURNEY DA PESSOA
```

Este mapa não define RBAC técnico, matriz de permissões ou comportamento de controles.

### 5.6 ORG-S06 — Planos e Capacidade

**Classificação:** especializada / contextual.

**Função:** hospedar capacidades de planejamento e capacidade institucional apenas quando houver suporte de produto, política e dados para isso.

Sua existência no mapa não significa que:

- toda Organização terá acesso à superfície;
- todo plano comercial a tornará visível;
- ela deverá aparecer no menu principal;
- capacidade comercial determine relevância funcional.

```text
PLANO MAIOR
≠ MAIS RELEVÂNCIA
≠ MAIS AUTORIDADE
≠ MAIS EVIDÊNCIA
```

## 6. Mapa de superfícies — Coletivo

O Coletivo possui sete superfícies-base e uma superfície especializada/contextual, preservando os domínios definidos pela Arquitetura da Informação.

```text
COLETIVO
├── COL-S01 — Início
├── COL-S02 — Atividades e Oportunidades
├── COL-S03 — Participação
├── COL-S04 — Governança e Proteção
├── COL-S05 — Relações
├── COL-S06 — Aprendizados e Evidências
├── COL-S07 — Coletivo e Autoridade
└── COL-S08 — Planos e Capacidade [especializada / contextual]
```

### 6.1 COL-S01 — Início

**Função:** orientar a pessoa dentro do Coletivo ativo, preservando identidade, propósito, contexto, participação aplicável e atenção material.

Pode sintetizar referências ao trabalho em andamento sem absorver os demais domínios.

> **Início é uma síntese contextual do Coletivo; não é um painel total de governança, participação, relações ou evidências.**

### 6.2 COL-S02 — Atividades e Oportunidades

**Função:** concentrar atividades e oportunidades que pertencem ao contexto do Coletivo e que podem ser apresentadas legitimamente à pessoa autenticada.

A superfície não torna toda atividade pública, não presume elegibilidade e não converte patrocínio ou promoção em prioridade funcional.

### 6.3 COL-S03 — Participação

**Função:** concentrar informações e trabalho relacionados a quem participa, em que condição e por quais formas legítimas de participação.

Preservações:

```text
PARTICIPAÇÃO
≠ REPRESENTAÇÃO
≠ GOVERNANÇA TOTAL
≠ PROPRIEDADE SOBRE O COLETIVO
```

Participação deve continuar submetida aos limites de privacidade, proteção, voluntariedade, pausa, saída e contestação vigentes.

### 6.4 COL-S04 — Governança e Proteção

**Função:** concentrar decisões, mecanismos de governança e elementos de proteção que pertencem ao Coletivo.

Esta superfície existe para preservar a autonomia coletiva e tornar localizável o trabalho de governança sem presumir um modelo único de autoridade.

Ela não autoriza a criação de novos papéis, quóruns, poderes de moderação ou regras de decisão.

### 6.5 COL-S05 — Relações

**Função:** localizar as relações do Coletivo com Pessoas, Organizações, outros Coletivos e contrapartes quando essas relações estão legitimamente representadas.

Relação não é sinônimo de participação e apoio externo não transfere automaticamente propósito ou governança.

> **Apoio, financiamento, patrocínio ou infraestrutura não transferem automaticamente propósito, governança, pertencimento ou autoridade.**

### 6.6 COL-S06 — Aprendizados e Evidências

**Função:** concentrar aprendizados, evidências, feedback e registros de corroboração que podem ser legitimamente compreendidos no contexto do Coletivo.

Esta superfície não é sinônimo de dashboard nem autorização para analytics irrestrita.

Ela deve preservar:

- distinção entre fato, evidência, interpretação e inferência;
- contexto de origem;
- limites de visibilidade;
- ausência de causalidade quando ela não puder ser sustentada.

### 6.7 COL-S07 — Coletivo e Autoridade

**Função:** concentrar gestão do Coletivo e elementos de autoridade que não pertencem às superfícies de participação ou governança operacional.

A presença desta superfície não transforma todo participante em administrador e não reduz o Coletivo a uma conta institucional tradicional.

Este mapa não define permissões técnicas nem ações específicas de administração.

### 6.8 COL-S08 — Planos e Capacidade

**Classificação:** especializada / contextual.

**Função:** hospedar capacidades de planejamento e capacidade coletiva quando sustentadas por produto, política e dados.

Sua disponibilidade deve permanecer contextual. A existência do domínio não autoriza paywall, plano comercial, feature gating ou exposição automática.

## 7. Invariantes entre contextos

O mapa inteiro deve preservar os seguintes invariantes:

1. **Organização ≠ Coletivo** — semelhanças funcionais não apagam a diferença estrutural entre os participantes;
2. **mudança de contexto ≠ concessão de autoridade**;
3. **superfície existente ≠ superfície visível para todos**;
4. **superfície visível ≠ autorização para toda ação contida nela**;
5. **síntese ≠ nova fonte de verdade** — Visão Geral e Início referenciam objetos dos domínios responsáveis;
6. **relação ≠ governança** e **relação ≠ participação**;
7. **evidência ≠ impacto** e **correlação ≠ causalidade**;
8. **capacidade comercial ≠ relevância, autoridade ou força de evidência**;
9. **dados de uma Pessoa, Organização ou Coletivo não atravessam contextos apenas porque os contextos estão conectados**;
10. **autonomia humana e institucional permanece superior à conveniência de navegação**.

## 8. Limite com Dashboards, KPIs e Analytics

`GKR-INTEL-DASH-KPI-ANALYTICS-MASTER-001` permanece a autoridade mestre de handoff para **Dashboards, KPIs e Analytics**, inclusive para futura implementação no Replit.

Este mapa **não redefine, duplica nem substitui**:

- composição de dashboards;
- KPIs;
- fórmulas ou cálculos;
- gráficos;
- badges;
- insights;
- recomendações;
- confiança;
- explicabilidade analítica;
- permissões analíticas;
- comportamento fail-closed;
- regras de implementação desse handoff.

A única função deste documento em relação a analytics é indicar **onde conceitos como síntese, aprendizados ou evidências pertencem semanticamente na experiência O/C**.

```text
MAPA DE SUPERFÍCIES O/C
→ organiza localização semântica da experiência

DASHBOARDS / KPIs / ANALYTICS MASTER
→ governa o handoff analítico

UM NÃO SUBSTITUI O OUTRO
```

O documento mestre de Dashboards, KPIs e Analytics permanece **inalterado** por esta autoridade.

## 9. O que permanece deliberadamente diferido

Esta versão não define:

- estados de loading, vazio, erro, bloqueio, indisponibilidade, restrição ou degradação;
- relações entre estados;
- transições;
- fluxos prioritários;
- sitemap técnico;
- rotas ou URLs;
- menu, drawer, tabs ou hierarquia visual de navegação;
- wireframes;
- layout;
- UI copy;
- design visual;
- protótipo;
- componentes;
- RBAC técnico;
- APIs;
- persistência;
- implementação frontend ou backend.

Esses itens não podem ser inferidos a partir dos diagramas e tabelas deste documento.

## 10. Relação com a branch pré-auditoria

A branch histórica:

```text
agent/gkr-orgcol-authenticated-surface-map-v1
```

permanece classificada como `HOLD_REVIEW` no estado mestre.

Este documento:

- não promove aquela branch a autoridade;
- não copia sua taxonomia de superfícies;
- não reativa estados, wireframes ou decisões nela materializadas;
- foi reautorado a partir das autoridades vigentes no `main` confirmado em `490dccae41b0a8cdb4df49f68f796f2b4ae0403f`.

A existência do artefato histórico preserva proveniência, mas não altera a autoridade atual.

## 11. Estado governado desta etapa

Com este documento, a frente pode declarar documentalmente:

```text
ATORES / AUTORIDADES / JOBS
→ DEFINIDOS

ARQUITETURA DA INFORMAÇÃO AUTENTICADA
→ DEFINIDA

MAPA LÓGICO DE SUPERFÍCIES AUTENTICADAS
→ DEFINIDO NESTE ARTEFATO

ESTADOS
→ NÃO MATERIALIZADOS NESTA ETAPA

FLUXOS
→ NÃO MATERIALIZADOS NESTA ETAPA

WIREFRAMES
→ NÃO INICIADOS POR ESTE ARTEFATO

UI / PROTÓTIPO / IMPLEMENTAÇÃO
→ NÃO AUTORIZADOS POR ESTE ARTEFATO
```

A autoridade deste documento passa a valer no `main` somente após revisão e merge governados. Enquanto permanecer em branch/PR draft, constitui **candidato de autoridade**, não promoção antecipada do estado canônico.
