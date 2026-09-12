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
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - UXA-014
  - UXA-019
related:
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-INTEL-DASH-KPI-ANALYTICS-MASTER-001
---

# Organizações e Coletivos — Mapa de Superfícies da Experiência Autenticada

## 1. Finalidade

Este documento define o **mapa lógico de superfícies autenticadas** de Organização e Coletivo a partir da Arquitetura da Informação vigente e o reconcilia com o inventário estável já registrado em `GKR-JOURNEY-SURFACE-REGISTRY-001`.

Ele responde à pergunta:

> **Quais áreas lógicas de trabalho precisam existir para que uma pessoa autenticada atue no contexto de uma Organização ou de um Coletivo sem misturar contexto, autoridade, operação, governança, evidência e capacidades comerciais especializadas?**

Esta etapa materializa o mapa lógico de superfícies. Ela **não** materializa estados, transições, fluxos, wireframes, UI, permissões técnicas ou implementação.

```text
JOBS AUTENTICADOS
+
ARQUITETURA DA INFORMAÇÃO
+
REGISTRO ESTÁVEL DE SUPERFÍCIES
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

## 2. Autoridade e regra de identidade

Este mapa deriva principalmente de:

1. `GKR-UX-ORGCOL-AUTH-IA-001` — camadas, domínios e limites da experiência autenticada;
2. `GKR-UX-ORGCOL-AUTH-JOBS-001` — atores, autoridade e jobs que justificam os domínios;
3. `GKR-JOURNEY-SURFACE-REGISTRY-001` — identificadores estáveis, maturidade registrada e fronteiras documentais já existentes;
4. `GKR-UX-ORGCOL-STATE-001` e `GKR-UX-ORGCOL-UX-STATE-001` — estado vigente e limites de maturidade;
5. `UXA-014` e `UXA-019` — distinção estrutural entre Organização e Coletivo e limites de suas relações.

Regra central:

> **Este documento não cria um segundo namespace de superfícies. Quando já existe um `GKR-SURF-*`, ele é preservado. Quando não existe um identificador dedicado, a lacuna permanece explícita e nenhum ID é inventado por esta frente.**

Consequentemente, códigos locais como `ORG-Sxx` e `COL-Sxx` **não são usados**.

A existência de um ID no registro também não significa que sua materialização ou validação esteja concluída. A maturidade de cada entrada continua sendo a registrada em `GKR-JOURNEY-SURFACE-REGISTRY-001` e em suas autoridades de origem.

## 3. O que é uma superfície lógica nesta autoridade

Neste documento, **superfície lógica** é uma área coerente de compreensão e trabalho pertencente ao contexto autenticado.

Uma superfície lógica:

- possui responsabilidade semântica própria;
- agrupa objetos e ações do mesmo domínio;
- preserva participante, contexto, papel e autoridade aplicáveis;
- pode corresponder a uma ou mais entradas estáveis já registradas;
- pode depender de capacidades especializadas que permanecem separadas;
- não promove a maturidade das entradas `GKR-SURF-*` relacionadas.

Uma superfície lógica não é, por definição:

- URL ou rota técnica;
- item obrigatório de menu;
- aba, drawer ou componente;
- tela única;
- permissão;
- papel de negócio;
- estado de interface;
- autorização de Design ou Engenharia.

## 4. Modelo de contexto autenticado

A Pessoa autenticada permanece o agente humano. Organização e Coletivo são contextos distintos nos quais essa Pessoa pode atuar somente quando existe relação e autoridade aplicáveis.

```text
PESSOA AUTENTICADA
↓
CONTEXTO ATIVO
├── ORGANIZAÇÃO
└── COLETIVO
```

A mudança de contexto não concede privilégio.

```text
ACESSAR UM CONTEXTO
≠ RECEBER AUTORIDADE

PERTENCER
≠ REPRESENTAR
≠ APROVAR
≠ ADMINISTRAR
```

O mapa define **onde uma responsabilidade pertence**. As autoridades funcionais definem **se, como e até onde** determinada pessoa pode atuar.

## 5. Organização — mapa lógico principal

A Arquitetura da Informação define cinco domínios principais para a Organização:

```text
ORGANIZAÇÃO
├── Visão Geral
├── Oportunidades e Programas
├── Relações
├── Responsabilidades e Evidências
└── Organização e Autoridade

CAPACIDADE ESPECIALIZADA / CONTEXTUAL
└── Planos e Capacidade comercial
```

`Planos e Capacidade` não é promovido a sexta superfície principal. Ele permanece capacidade comercial especializada/contextual com fluxos próprios já registrados.

### 5.1 Visão Geral

**Função:** orientar a pessoa sobre o contexto institucional ativo e sintetizar o que exige atenção agora, sem se transformar em painel administrativo total.

Crosswalk vigente:

- `GKR-SURF-ORG-001` — Visão Geral da Organização.

A maturidade de `GKR-SURF-ORG-001` permanece a do registro central; este mapa não declara wireframe principal validado.

### 5.2 Oportunidades e Programas

**Função:** concentrar o trabalho relacionado ao que a Organização oferece, publica, opera ou habilita legitimamente.

Crosswalk vigente:

- `GKR-SURF-ORG-002` — cadastro de oportunidade;
- `GKR-SURF-ORG-003` — oportunidade aprovada/ativa.

As duas entradas continuam separadas no registro. Este domínio lógico não as funde e não transforma publicação em relevância, distribuição ou impacto.

```text
OPORTUNIDADE PUBLICADA
≠ DISTRIBUIÇÃO GARANTIDA
≠ RELEVÂNCIA
≠ IMPACTO
```

### 5.3 Relações

**Função:** concentrar relações institucionais com finalidade, autoridade, compromissos, recursos, dados ou responsabilidades materialmente relevantes.

Crosswalk vigente:

- `GKR-SURF-ORG-004` — proposta de relação com Coletivo;
- `GKR-SURF-ORG-005` — avaliação e negociação bilateral;
- `GKR-SURF-ORG-006` — relação ativa e revisão.

Essas entradas permanecem objetos distintos. A relação não transfere automaticamente autoridade sobre a contraparte.

### 5.4 Responsabilidades e Evidências

**Função:** localizar responsabilidades, compromissos, resultados autorizados e evidências sem confundir atividade, resultado e impacto.

Crosswalk vigente:

- `GKR-SURF-ORG-007` — resultados e evidências institucionais.

A entrada permanece com a maturidade registrada no inventário central. Este mapa não completa por inferência campos ainda indeterminados.

```text
ATIVIDADE
≠ RESULTADO

RESULTADO
≠ IMPACTO

CORRELAÇÃO
≠ CAUSALIDADE
```

### 5.5 Organização e Autoridade

**Função:** preservar identidade institucional, unidade/contexto, papel, representação, autoridade, limites e necessidade de aprovação adicional.

O registro estável **não possui atualmente um `GKR-SURF-ORG-*` dedicado exclusivamente a este domínio**. Portanto:

- nenhum novo ID é criado nesta frente;
- autoridade continua requisito transversal das superfícies registradas;
- eventual criação futura de identificador exige governança própria do registro central;
- ausência de ID dedicado não autoriza fundir autoridade com configuração técnica ou RBAC.

```text
REPRESENTAÇÃO
≠ APROVAÇÃO IRRESTRITA

CONTEXTO ORGANIZAÇÃO
≠ PAPEL ADMINISTRATIVO
```

## 6. Organização — capacidade comercial especializada

### Planos e Capacidade comercial

A IA classifica esta capacidade como **especializada/contextual**. O fluxo canônico já existe e preserva a taxonomia:

```text
Conecta · Eleva · Transforma
```

Crosswalk estável:

- `GKR-SURF-ORG-301` — Planos e comparação da Organização;
- `GKR-SURF-ORG-302` — revisão de contratação da Organização;
- `GKR-SURF-ORG-303` — gestão de downgrade e cancelamento da Organização;
- `GKR-SURF-ORG-304` — resultado e recuperação de plano/cobrança da Organização;
- `GKR-SURF-BND-002` — fronteira de contratação/dimensionamento assistido quando necessária.

Esta capacidade deve ser acessível quando a pessoa busca capacidade comercial ou atinge limite legítimo e deve permitir retorno ao contexto anterior quando não houver contratação confirmada.

Ela **não** é uma capacidade genérica de planejamento institucional e não pode ser usada para inventar uma nova função de planejamento.

```text
PLANO
≠ IDENTIDADE DA ORGANIZAÇÃO
≠ RELEVÂNCIA
≠ AUTORIDADE
≠ EVIDÊNCIA
```

## 7. Coletivo — mapa lógico principal

A Arquitetura da Informação define sete domínios principais para o Coletivo:

```text
COLETIVO
├── Início
├── Atividades e Oportunidades
├── Participação
├── Governança e Proteção
├── Relações
├── Aprendizados e Evidências
└── Coletivo e Autoridade

CAPACIDADE ESPECIALIZADA / CONTEXTUAL
└── Planos e Capacidade comercial
```

`Planos e Capacidade` não é promovido a oitava superfície principal. Ele permanece capacidade comercial especializada/contextual.

### 7.1 Início

**Função:** orientar a pessoa autorizada sobre o contexto coletivo ativo, o Momento e a atenção material.

Crosswalk vigente:

- `GKR-SURF-COL-002` — Visão Geral do Responsável.

`GKR-SURF-COL-001` permanece entrada/presença pública parcialmente consolidada e **não é absorvida** pela experiência autenticada principal. Sua perspectiva e maturidade continuam registradas separadamente.

### 7.2 Atividades e Oportunidades

**Função:** concentrar atividades, consultas, decisões e oportunidades legitimamente relacionadas ao trabalho do Coletivo.

Crosswalk vigente:

- `GKR-SURF-COL-006` — atividades, consultas e decisões.

O mapa não inventa um novo ID apenas para “oportunidades”. Quando uma oportunidade utilizar fluxos especializados existentes, esses fluxos mantêm sua própria autoridade e identidade.

### 7.3 Participação

**Função:** concentrar entrada, vínculos e continuidade da participação sob regras de voluntariedade, proteção e autoridade.

Crosswalk vigente:

- `GKR-SURF-COL-003` — gestão de solicitações;
- `GKR-SURF-COL-004` — participantes e vínculos;
- `GKR-SURF-COL-005` — comunicação oficial, quando vinculada à continuidade operacional da participação.

As superfícies da perspectiva da Pessoa `GKR-SURF-PER-103..108` permanecem **separadas** e não são absorvidas pelo contexto operacional do Coletivo.

```text
PARTICIPAÇÃO
≠ REPRESENTAÇÃO
≠ ADMINISTRAÇÃO
```

### 7.4 Governança e Proteção

**Função:** concentrar decisões coletivas, proteção, moderação, contestação e continuidade quando legitimamente aplicáveis.

Crosswalk vigente:

- `GKR-SURF-COL-006` — no recorte de decisões;
- `GKR-SURF-COL-007` — proteção e moderação.

Uma mesma entrada estável pode participar de mais de um domínio lógico sem ser duplicada.

### 7.5 Relações

**Função:** concentrar relações do Coletivo com Organizações, outros Coletivos ou contrapartes, preservando autonomia e autoridade bilateral.

Crosswalk vigente:

- `GKR-SURF-COL-008` — relações institucionais.

```text
APOIO
≠ POSSE
≠ CONTROLE
≠ TRANSFERÊNCIA DE GOVERNANÇA
```

### 7.6 Aprendizados e Evidências

**Função:** permitir compreensão sobre o que ocorreu, o que pode ser sustentado por evidência e quais incertezas permanecem.

O registro estável **não possui atualmente um `GKR-SURF-COL-*` dedicado exclusivamente a este domínio**. Portanto:

- nenhum ID é criado nesta frente;
- evidência continua requisito transversal nos objetos responsáveis;
- ausência de evidência deve permanecer declarável;
- eventual ID dedicado dependerá de governança futura do registro central.

### 7.7 Coletivo e Autoridade

**Função:** preservar identidade do Coletivo, propósito, governança, papéis, representação e limites de autoridade.

`GKR-SURF-COL-002` contém parte do contexto de autoridade na visão geral do responsável, mas **não é reclassificado aqui como superfície exclusiva de autoridade**.

Não existe hoje um ID estável dedicado exclusivamente a este domínio. Nenhum novo ID é criado.

```text
PERTENCIMENTO
≠ REPRESENTAÇÃO

REPRESENTAÇÃO
≠ AUTORIDADE IRRESTRITA
```

## 8. Coletivo — capacidade comercial especializada

### Planos e Capacidade comercial

A IA classifica esta capacidade como **especializada/contextual** e preserva a taxonomia:

```text
Livre · Mobiliza · Impacta · Rede
```

Crosswalk estável:

- `GKR-SURF-COL-301` — Planos e comparação do Coletivo;
- `GKR-SURF-COL-302` — revisão de contratação do Coletivo;
- `GKR-SURF-COL-303` — gestão de downgrade e cancelamento do Coletivo;
- `GKR-SURF-COL-304` — resultado e recuperação de plano/cobrança do Coletivo;
- `GKR-SURF-BND-002` — fronteira de contratação/dimensionamento assistido quando necessária.

O acesso é contextual quando houver necessidade legítima de capacidade comercial ou consulta explícita. Nenhuma contratação converte a experiência em funil de upsell nem altera pertencimento, legitimidade, relevância ou impacto.

Esta capacidade **não** é uma função genérica de planejamento do Coletivo.

## 9. Matriz consolidada de crosswalk

| Domínio lógico | IDs estáveis relacionados | Tratamento |
|---|---|---|
| Organização — Visão Geral | `GKR-SURF-ORG-001` | preservado |
| Organização — Oportunidades e Programas | `GKR-SURF-ORG-002`, `GKR-SURF-ORG-003` | preservados e separados |
| Organização — Relações | `GKR-SURF-ORG-004..006` | preservados e separados |
| Organização — Responsabilidades e Evidências | `GKR-SURF-ORG-007` | preservado; maturidade não promovida |
| Organização — Organização e Autoridade | sem ID dedicado | nenhum ID criado; requisito transversal |
| Organização — Planos e Capacidade comercial | `GKR-SURF-ORG-301..304`, `GKR-SURF-BND-002` | fluxo especializado separado |
| Coletivo — Início | `GKR-SURF-COL-002` | preservado; `COL-001` permanece fronteira/presença pública separada |
| Coletivo — Atividades e Oportunidades | `GKR-SURF-COL-006` | preservado; sem ID novo por inferência |
| Coletivo — Participação | `GKR-SURF-COL-003..005` | preservados; superfícies da Pessoa permanecem separadas |
| Coletivo — Governança e Proteção | `GKR-SURF-COL-006`, `GKR-SURF-COL-007` | responsabilidades distintas preservadas |
| Coletivo — Relações | `GKR-SURF-COL-008` | preservado |
| Coletivo — Aprendizados e Evidências | sem ID dedicado | nenhum ID criado; requisito transversal |
| Coletivo — Coletivo e Autoridade | `GKR-SURF-COL-002` parcialmente; sem ID exclusivo | nenhum ID novo; autoridade transversal |
| Coletivo — Planos e Capacidade comercial | `GKR-SURF-COL-301..304`, `GKR-SURF-BND-002` | fluxo especializado separado |

A tabela é um **crosswalk semântico**, não uma alteração do registro central. O `GKR-JOURNEY-SURFACE-REGISTRY-001` continua sendo a autoridade para IDs e maturidade individual.

## 10. Relações entre superfícies sem materializar fluxo

Este mapa reconhece dependências sem declarar transições como definidas.

Exemplos de relação conceitual:

- Visão Geral referencia objetos de outros domínios sem duplicá-los;
- Oportunidades e Programas podem gerar responsabilidades e evidências;
- Relações podem gerar compromissos e revisões;
- Participação pode exigir governança e proteção;
- capacidades comerciais especializadas devem retornar ao contexto anterior conforme suas autoridades próprias.

```text
RELAÇÃO ENTRE DOMÍNIOS
≠ TRANSIÇÃO DEFINIDA
≠ FLUXO DEFINIDO
```

As transições permanecem sob autoridade própria do `GKR-JOURNEY-TRANSITION-REGISTRY-001` e de futuros atos documentais autorizados.

## 11. Limite com Dashboards, KPIs e Analytics

`GKR-INTEL-DASH-KPI-ANALYTICS-MASTER-001` permanece a autoridade mestre do handoff analítico, inclusive para futura implementação no Replit.

Este Surface Map não define:

- dashboards;
- KPIs;
- fórmulas;
- gráficos;
- badges;
- thresholds;
- insights;
- recomendações;
- níveis de confiança;
- permissões analíticas;
- comportamento fail-closed.

```text
SUPERFÍCIE AUTENTICADA
≠ DASHBOARD

DOMÍNIO DE TRABALHO
≠ KPI

SÍNTESE DO MOMENTO
≠ PAINEL DE MÉTRICAS
```

## 12. Separação da Home pública

A Home pública de Organizações e Coletivos possui autoridade documental própria.

```text
HOME PÚBLICA
→ aquisição / posicionamento / entrada pública

SURFACE MAP AUTENTICADO
→ organização lógica do trabalho sob contexto e autoridade
```

Nenhum elemento da Home pública é promovido por inferência para a experiência autenticada.

## 13. Estado documental após este mapa

Com esta autoridade, a sequência fica:

```text
FUNDAMENTOS E PAPÉIS
→ DEFINED

ATORES / AUTORIDADE / JOBS
→ DEFINED

ARQUITETURA DA INFORMAÇÃO
→ DEFINED

MAPA LÓGICO DE SUPERFÍCIES
→ DEFINED

MAPA DE ESTADOS
→ NOT MATERIALIZED

FLUXOS PRIORITÁRIOS
→ NOT MATERIALIZED

WIREFRAMES
→ NOT STARTED

UI / PROTÓTIPO
→ NOT AUTHORIZED

PRODUCT ENGINEERING
→ NOT RELEASED
```

A palavra `DEFINED` neste documento significa **definição documental do mapa lógico**, não materialização visual, implementação nem promoção automática da maturidade de qualquer `GKR-SURF-*` individual.

## 14. Próximo gate

Este documento não autoriza automaticamente a etapa seguinte.

Quando houver autorização específica, o próximo ato elegível poderá trabalhar **estados críticos e fluxos prioritários** sobre este mapa, respeitando:

- IDs estáveis do registro central;
- maturidade individual já registrada;
- fluxos especializados existentes;
- autoridade e proteção;
- reversibilidade;
- estados de ausência, bloqueio, contestação e indisponibilidade;
- separação entre semântica funcional e Design.

Até nova autorização:

```text
STATES
→ NOT MATERIALIZED

FLOWS
→ NOT MATERIALIZED

WIREFRAMES
→ NOT STARTED

DESIGN / UI
→ NOT AUTHORIZED

IMPLEMENTATION
→ NOT AUTHORIZED
```
