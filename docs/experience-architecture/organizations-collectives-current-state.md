---
id: GKR-UX-ORGCOL-STATE-001
title: Organizações e Coletivos — Visão Geral e Estado Atual
status: active
version: 1.10.8
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-24
normative: false
related:
  - UXA-014
  - UXA-019
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
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-UX-ORGCOL-SUPPLY-VALUE-001
  - RP-002
  - RP-002-SUP-001
  - RP-002-OCE-001
  - RP-002-PMF-001
---

# Organizações e Coletivos — Visão Geral e Estado Atual

## 1. Finalidade

Este documento é a porta de entrada atual para o conhecimento sobre **Organizações e Coletivos** no Guivos Knowledge Repository.

Ele existe para impedir três confusões:

1. tratar Organizações e Coletivos apenas como telas ou contas de produto;
2. confundir conhecimento funcional já estabelecido com hipóteses de Research;
3. apresentar como vigente uma materialização de UX que ainda não foi oficialmente definida.

A regra de leitura é:

> **Organizações e Coletivos são participantes estruturais do ecossistema Guivos. Sua fundação, suas relações, suas jornadas, seu papel no supply e sua experiência de produto possuem níveis de maturidade diferentes e devem permanecer explicitamente separados.**

Para compreender em profundidade **quais oportunidades esses agentes podem materializar, como a Guivos pesquisa supply real, como relevância é testada para diferentes perfis e por que algumas oportunidades são descartadas**, a leitura principal complementar é [Organizações e Coletivos — Atlas de Oportunidades, Relevância, Supply e Validação](organizations-collectives-supply-and-value.md). Essa página reúne exemplos mundiais, perfis sintéticos, gates, counterexamples, evidência e limites de PMF.

## 2. Estado executivo

| Dimensão | Estado atual | Autoridade / referência |
|---|---|---|
| definição de Organização | definida funcionalmente | `UXA-014` |
| definição de Coletivo | definida funcionalmente | `UXA-014` |
| distinção Organização × Coletivo | definida funcionalmente | `UXA-014` |
| relações Organização ↔ Coletivo | contrato funcional existente, não normativo | `UXA-019` |
| atores, autoridades e jobs autenticados | **definidos documentalmente** | [Atores, Autoridades e Jobs](organizations-collectives-authenticated-actors-authorities-and-jobs.md) |
| Arquitetura da Informação autenticada | **definida** | [Arquitetura da Informação](organizations-collectives-authenticated-information-architecture.md) |
| mapa lógico de superfícies autenticadas | **definido documentalmente** | [Mapa de Superfícies](organizations-collectives-authenticated-surface-map.md) |
| mapa funcional de estados autenticados | **definido documentalmente** | [Mapa de Estados](organizations-collectives-authenticated-state-map.md) |
| Jornada da Organização | **active**; continuidade funcional corrente, não equivale a UI final | [Jornada da Organização](../journeys/organization.md) |
| Jornada do Coletivo | **active**; continuidade funcional corrente, não equivale a UI final | [Jornada do Coletivo](../journeys/collective.md) |
| corpus de oportunidades reais | Research consolidado pré-campo | `RP-002-SUP-001` |
| atlas de oportunidades, supply, relevância e testes | `active`, não normativo | `GKR-UX-ORGCOL-SUPPLY-VALUE-001` |
| papel no supply | pesquisa consolidada pré-campo | `RP-002-OCE-001` |
| proposta de valor econômica e de rede | hipótese de Research, não Canon | `RP-002-OCE-001` |
| validação com perfis sintéticos | executada metodologicamente; não é PMF | `RP-002-PMF-001` + atlas |
| validação humana real / PMF | **pendente** | piloto de campo |
| Home pública de Organizações e Coletivos | possui Documento Mestre próprio | `public-home-organizations-collectives-master-document.md` |
| wireframe low-fidelity da experiência autenticada da Organização | **Delivery v0.1.0 + Validation v1.0.0** | [Entrega Low-Fidelity](organizations-collectives-authenticated-low-fidelity-wireframe-delivery.md) + [Validação](organizations-collectives-authenticated-low-fidelity-functional-validation.md) |
| wireframe low-fidelity da experiência autenticada do Coletivo | **Delivery v0.1.0 + Validation v1.0.0** | [Entrega Low-Fidelity](organizations-collectives-authenticated-low-fidelity-wireframe-delivery.md) + [Validação](organizations-collectives-authenticated-low-fidelity-functional-validation.md) |
| validação de wireframe da Organização | **PASS / 0 findings materiais** | concluída |
| validação de wireframe do Coletivo | **PASS / 0 findings materiais** | concluída |
| elegibilidade high-fidelity O/C | **PASS** | [Elegibilidade High-Fidelity](organizations-collectives-authenticated-high-fidelity-eligibility.md) |
| autorização high-fidelity O/C | **GRANTED** | [Autorização High-Fidelity](organizations-collectives-authenticated-high-fidelity-authorization.md) |
| execução high-fidelity O/C | **RELEASED FOR EXTERNAL DESIGN / DELIVERY NOT_RECEIVED** | [Release e Handoff High-Fidelity](organizations-collectives-authenticated-high-fidelity-execution-handoff.md) |
| UI / protótipo autenticado | não definido | pendente |
| Engenharia da experiência autenticada | não autorizada a partir de wireframe | pendente |

A cadeia autenticada corrente pode ser percorrida diretamente a partir deste hub:

1. [Atores, Autoridades e Jobs](organizations-collectives-authenticated-actors-authorities-and-jobs.md);
2. [Arquitetura da Informação](organizations-collectives-authenticated-information-architecture.md);
3. [Mapa de Superfícies](organizations-collectives-authenticated-surface-map.md);
4. [Mapa de Estados](organizations-collectives-authenticated-state-map.md);
5. [Fluxos Prioritários](organizations-collectives-authenticated-priority-flows.md);
6. [Materialização de Navegação](organizations-collectives-authenticated-navigation-materialization.md);
7. [Entrega Low-Fidelity](organizations-collectives-authenticated-low-fidelity-wireframe-delivery.md);
8. [Validação Low-Fidelity](organizations-collectives-authenticated-low-fidelity-functional-validation.md);
9. [Elegibilidade High-Fidelity](organizations-collectives-authenticated-high-fidelity-eligibility.md);
10. [Autorização High-Fidelity](organizations-collectives-authenticated-high-fidelity-authorization.md);
11. [Release e Handoff para Execução High-Fidelity](organizations-collectives-authenticated-high-fidelity-execution-handoff.md).

Esses documentos permanecem autoridades correntes de detalhe. Eles saem do MENU principal para reduzir poluição de navegação, não por perda de validade.

A existência de Jobs, Arquitetura da Informação, mapa lógico de superfícies e mapa funcional de estados não promove automaticamente fluxos, sitemap técnico, menu visual, wireframe, UI, RBAC técnico ou implementação.

```text
JOBS DEFINIDOS
+
ARQUITETURA DA INFORMAÇÃO DEFINIDA
+
MAPA LÓGICO DE SUPERFÍCIES DEFINIDO
+
MAPA DE ESTADOS DEFINIDO
≠ FLUXOS
≠ WIREFRAME
≠ UI
≠ IMPLEMENTAÇÃO
```

## 3. Organização

Uma **Organização** é uma entidade institucional que possui identidade, autoridade, responsabilidades, recursos, processos, representantes e capacidade de oferecer produtos, serviços, programas, benefícios, suporte, infraestrutura ou oportunidades.

Pode possuir natureza:

- empresarial;
- pública;
- educacional;
- social;
- comunitária;
- religiosa;
- cultural;
- profissional;
- filantrópica;
- híbrida.

Organização não é sinônimo de:

- cliente do Guivos Business;
- anunciante;
- parceiro comercial;
- página institucional;
- fornecedor admitido;
- oportunidade;
- autoridade sobre a Journey de uma Pessoa.

Uma Organização pode exercer um ou vários desses papéis, mas sua natureza institucional permanece distinta deles.

## 4. Coletivo

Um **Coletivo** é uma formação voluntária de pessoas reunidas por propósito, identidade, causa, interesse, território, prática, experiência ou objetivo compartilhado.

Pode existir:

- independentemente;
- apoiado por uma Organização;
- em relação com múltiplas Organizações;
- em colaboração com outros Coletivos.

Coletivo não é sinônimo de:

- grupo de mensagens;
- audiência;
- comunidade de seguidores;
- canal de marketing;
- propriedade de uma Organização;
- força de trabalho gratuita;
- conta comercial.

Sua autonomia, governança, participação voluntária, pausa, saída e contestação devem permanecer protegidas.

## 5. Diferença estrutural

```text
ORGANIZAÇÃO
→ identidade institucional
→ autoridade formal
→ recursos e processos
→ responsabilidades institucionais
→ capacidade de oferta e execução

COLETIVO
→ propósito compartilhado
→ formação voluntária
→ pertencimento
→ governança própria
→ ação e experiência coletiva
```

Uma Organização pode apoiar um Coletivo sem possuí-lo.

Um Coletivo pode colaborar com uma Organização sem representá-la institucionalmente fora do escopo acordado.

## 6. Relações entre Organizações e Coletivos

O contrato funcional atual está em [`UXA-019`](uxa-019-organization-collective-relationship-functional-contract.md).

Ele preserva, entre outros elementos:

- finalidade explícita;
- autoridade bilateral;
- compromissos verificáveis;
- recursos e condições econômicas transparentes;
- dados e privacidade;
- uso de marca;
- autonomia e influência;
- proteção e não retaliação;
- revisão, suspensão e encerramento.

Princípio central:

> **Apoio, financiamento, patrocínio ou infraestrutura não transferem automaticamente propósito, governança, pertencimento ou autoridade.**

## 7. Experiência autenticada — atores, autoridades e jobs

`GKR-UX-ORGCOL-AUTH-JOBS-001` está ativo e define a unidade funcional de atuação autenticada antes de qualquer decisão visual:

```text
PESSOA AUTENTICADA
+
PARTICIPANTE REPRESENTADO
+
CONTEXTO / UNIDADE APLICÁVEL
+
PAPEL DECLARADO
+
AUTORIDADE E LIMITES
+
JOB ATUAL
```

Para Organização, o documento distingue representante institucional, autoridade de aprovação, responsável operacional/prestação de contas e contraparte autorizada.

Para Coletivo, distingue responsável/representante autorizado, instância de governança, responsável por operação/moderação/proteção, participante e contraparte autorizada.

Preservações:

```text
MESMA PESSOA
≠ MESMA AUTORIDADE

PERTENCIMENTO
≠ REPRESENTAÇÃO

REPRESENTAÇÃO
≠ APROVAÇÃO IRRESTRITA

JOB PRIORITÁRIO
≠ ITEM DE MENU
≠ TELA
```

Os jobs cobrem contexto, Momento, capacidade, oportunidades/atividades, relações, compromissos, evidência, participação, governança, proteção, contestação, continuidade, Planos contextuais e Próximos Passos justificáveis.

## 8. Arquitetura da Informação autenticada

`GKR-UX-ORGCOL-AUTH-IA-001` está ativo e estabelece as cinco camadas lógicas da experiência autenticada.

A arquitetura comum preserva:

```text
CAMADA 0 — CONTEXTO E AUTORIDADE
↓
CAMADA 1 — SÍNTESE DO MOMENTO
↓
CAMADA 2 — DOMÍNIOS DE TRABALHO
↓
CAMADA 3 — GOVERNANÇA, EVIDÊNCIA E CONTINUIDADE
↓
CAMADA 4 — CAPACIDADES ESPECIALIZADAS / CONTEXTUAIS
```

Organização:

```text
ORGANIZAÇÃO
├── Visão Geral
├── Oportunidades e Programas
├── Relações
├── Responsabilidades e Evidências
├── Organização e Autoridade
└── Planos e Capacidade [especializado / contextual]
```

Coletivo:

```text
COLETIVO
├── Início
├── Atividades e Oportunidades
├── Participação
├── Governança e Proteção
├── Relações
├── Aprendizados e Evidências
├── Coletivo e Autoridade
└── Planos e Capacidade [especializado / contextual]
```

A IA agrupa informação e trabalho; `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001` materializa esses domínios como superfícies lógicas autenticadas; `GKR-UX-ORGCOL-AUTH-STATE-MAP-001` define as condições funcionais que essas responsabilidades precisam preservar; `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.1` define os fluxos prioritários canônicos documentais; e `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.2` define topologia, hierarquia, entrada, retorno e recontextualização. Nenhuma dessas autoridades define quantidade final de telas, menu visual, wireframe, UI, protótipo, RBAC técnico ou implementação.

## 9. Jornadas atuais

As Jornadas integradas permanecem documentadas em:

- [Jornada Integrada da Organização](../journeys/organization.md);
- [Jornada Integrada do Coletivo](../journeys/collective.md).

Ambos os documentos possuem estado `active`.

Eles ajudam a mapear continuidade, estados e relações do ecossistema, mas **não devem ser interpretados como prova de que wireframes ou UI já foram definidos**.

`UXA-015..018` permanecem somente como proveniência histórica. Nenhuma maturidade corrente pode ser derivada desses produtores removidos; a referência low-fidelity vigente é exclusivamente `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` + `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0 / PASS`.

A existência de Jobs, IA, mapa de superfícies e State Map atuais também não reativa `UXA-015..018`.

## 10. Organizações e Coletivos no supply

A investigação `RP-002` ampliou a compreensão sobre Organizações e Coletivos como agentes do supply.

A leitura rica e orientada a exemplos está em [Atlas de Oportunidades, Relevância, Supply e Validação](organizations-collectives-supply-and-value.md). O corpus probatório completo está em [Corpus Real e Supply Ecosystems](../research/RP-002/real-world-supply-corpus.md), e o aprofundamento econômico em [Organizações, Coletivos, Efeito de Rede e Modelo Econômico do Supply](../research/RP-002/organizations-collectives-and-economic-model.md).

### 10.1 Papéis possíveis de Organizações

Research observou papéis como:

- provider;
- enabler;
- employer;
- infrastructure provider;
- funder;
- partner;
- verifier;
- venue / host;
- executor;
- sponsor;
- aggregator;
- source.

Esses papéis pertencem à relação ou à oportunidade concreta; não substituem a identidade institucional da Organização.

### 10.2 Papéis possíveis de Coletivos

Research observou papéis como:

- provider;
- ambiente de experiência;
- enabler;
- source;
- destination;
- rede de reciprocidade;
- detector de necessidades;
- criador de supply;
- coordenador local;
- mobilizador de recursos.

Coletivos podem materializar ou habilitar possibilidades que mercados tradicionais não atendem adequadamente.

### 10.3 Como ler relevância

A investigação preserva:

> **A relevância pertence à relação Pessoa ↔ Oportunidade.**

O mesmo programa pode ter alto fit para uma Pessoa e falhar para outra por horário, território, elegibilidade, custo indireto, carga, risco, acessibilidade ou necessidade de renda. Por isso, o atlas registra tanto oportunidades apresentadas quanto oportunidades legitimamente descartadas.

## 11. Modelo de valor — estado de Research

A hipótese atual para Organizações é:

> **A Guivos pode ajudar uma Organização a compreender para quais Pessoas, Momentos e Possibilidades aquilo que ela oferece realmente apresenta valor — e aprender com o que acontece depois da experiência.**

A hipótese atual para Coletivos é:

> **A Guivos pode ajudar Coletivos a encontrar Pessoas, capacidades e recursos compatíveis com seu propósito compartilhado, organizar participação e compreender contribuição sem reduzir valor a popularidade.**

Essas formulações são **Research**, não promessa comercial nem contrato canônico de produto.

## 12. Neutralidade econômica

Permanecem preservadas as seguintes separações:

```text
PAGAR ≠ SER RELEVANTE
PARCEIRO ≠ SER MAIS RELEVANTE
PLANO MAIOR ≠ TER MAIS EVIDÊNCIA
PATROCÍNIO ≠ AUTORIDADE SOBRE O COLETIVO
PUBLICAR MAIS ≠ CONTRIBUIR MAIS
```

A Guivos pode monetizar infraestrutura, operação, integração, escala, serviços, transações e Intelligence agregada sem vender relevância funcional, dignidade, autoridade ou força de evidência.

## 13. Presença pública

A Home pública de Organizações e Coletivos possui construção própria em [Documento Mestre da Home Pública de Organizações e Coletivos](public-home-organizations-collectives-master-document.md).

Essa Home pública não deve ser confundida com:

- ambiente autenticado da Organização;
- ambiente autenticado do Coletivo;
- dashboard;
- área administrativa;
- wireframe das jornadas internas.

## 14. Estado de UX

O estado vigente está detalhado em [Organizações e Coletivos — Estado de UX e Wireframes](organizations-collectives-ux-state.md).

Resumo:

> **A cadeia documental canônica O/C está definida e a primeira entrega de Authenticated Wireframes low-fidelity foi funcionalmente validada com `PASS` em `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`. O pacote Delivery v0.1.0 + Validation v1.0.0 é a referência visual low-fidelity corrente.**

Materiais anteriores que afirmavam wireframes principais vigentes ou validação vigente foram reclassificados como registros históricos `superseded`.

## 15. Mapa de conhecimento

| Tema | Documento principal |
|---|---|
| definição e fundamento | `UXA-014` |
| estado mestre | este documento |
| relações Organização ↔ Coletivo | `UXA-019` |
| atores, autoridades e jobs autenticados | `GKR-UX-ORGCOL-AUTH-JOBS-001` |
| Arquitetura da Informação autenticada | `GKR-UX-ORGCOL-AUTH-IA-001` |
| mapa de superfícies autenticadas | `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001` |
| mapa de estados autenticados | `GKR-UX-ORGCOL-AUTH-STATE-MAP-001` |
| fluxos prioritários autenticados | `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001` |
| elegibilidade de Navigation Materialization | `GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001` |
| Navigation Materialization autenticada | `GKR-UX-ORGCOL-AUTH-NAV-MAT-001` |
| autorização de wireframes low-fidelity | `GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001` |
| entrega de wireframes low-fidelity | `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001` |
| validação funcional low-fidelity | `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001` |
| elegibilidade high-fidelity | `GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001` |
| autorização high-fidelity | `GKR-UX-ORGCOL-AUTH-HIFI-AUTH-001` |
| release de execução high-fidelity | `GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001` |
| Jornada da Organização | `journeys/organization.md` |
| Jornada do Coletivo | `journeys/collective.md` |
| Home pública | `public-home-organizations-collectives-master-document.md` |
| **atlas de oportunidades, exemplos mundiais, perfis e testes de relevância** | `GKR-UX-ORGCOL-SUPPLY-VALUE-001` |
| corpus real de supply | `RP-002-SUP-001` |
| método de PMF e simulações | `RP-002-PMF-001` |
| supply, rede e modelo econômico — aprofundamento | `RP-002-OCE-001` |
| estado de UX e wireframes | `GKR-UX-ORGCOL-UX-STATE-001` |

## 16. Sequência corrente de maturidade da UX autenticada

A maturidade corrente é:

```text
FUNDAMENTOS / PAPÉIS
→ DEFINED

ATORES / AUTORIDADES / JOBS
→ DEFINED

INFORMATION ARCHITECTURE
→ DEFINED

SURFACE MAP
→ DEFINED / CANONICAL DOCUMENTARY

STATE MAP
→ DEFINED / CANONICAL DOCUMENTARY

PRIORITY FLOWS
→ DEFINED / CANONICAL DOCUMENTARY

NAVIGATION MATERIALIZATION
→ DEFINED / CANONICAL DOCUMENTARY / v1.0.0

LOW-FIDELITY
→ DELIVERY v0.1.0
→ VALIDATION v1.0.0 / PASS

HIGH-FIDELITY ELIGIBILITY
→ PASS / v1.0.1

HIGH-FIDELITY AUTHORIZATION
→ GRANTED / v1.0.2

HIGH-FIDELITY EXECUTION RELEASE
→ ISSUED / GKR-UX-ORGCOL-AUTH-HIFI-EXEC-001 v1.0.0

HIGH-FIDELITY DELIVERY
→ NOT_RECEIVED

HIGH-FIDELITY VALIDATION
→ NOT_STARTED

INTERACTIVE PROTOTYPE
→ NOT_AUTHORIZED

PRODUCT ENGINEERING
→ NOT_RELEASED
```

Nenhuma etapa posterior deve ser presumida antes do gate específico aplicável.

## 17. Regra de autoridade corrente

Para o estado atual de Organizações e Coletivos:

> **as autoridades O/C correntes prevalecem sobre afirmações de maturidade presentes em registros históricos ou documentos que dependam de `UXA-015..018`.**

Isso não apaga o histórico; apenas impede que materializações prematuras sejam confundidas com decisão vigente.

O atlas de supply e relevância possui função diferente: ele preserva Research, exemplos e método para tornar compreensível o universo de oportunidades. Ele **não** promove wireframes, matching, PMF ou implementação a estado superior.

`GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.1.2`, `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.1.3`, `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.1` e `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.2` compõem a cadeia documental canônica corrente. A Navigation Materialization define topologia/hierarquia/entrada/retorno, mas não define wireframes, Design/UI ou implementação.