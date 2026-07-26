---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
related:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - GLPA-001
  - GIA-000
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-004
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-008
  - UXA-009
normative: false
---

# Arquitetura da Experiência da Guivos (identificador UXA-000)

## 1. Finalidade

A Arquitetura da Experiência da Guivos transforma capacidades, princípios e contratos funcionais já consolidados no **Repositório de Conhecimento da Guivos (Guivos Knowledge Repository — GKR)** em uma experiência navegável, compreensível e coerente para Pessoas, Organizações e Coletivos.

Ela governa, antes do design visual definitivo:

- jornadas por tipo de participante;
- arquitetura de informação;
- navegação global;
- responsabilidades de cada superfície;
- hierarquia e prioridade do conteúdo;
- relações entre telas;
- pontos de entrada e retorno;
- controles de relevância, frequência e privacidade;
- fluxos entre Guivos Journey, Guivos Business, Guivos Mall, Guivos Travel, Guivos Media, Guivos Ads e Guivos Intelligence;
- critérios para wireframes, protótipos e testes posteriores.

## 2. O que esta frente não representa

Esta frente não:

- inicia Engenharia de Produto (Product Engineering);
- define tecnologia, componentes ou código;
- cria layout visual final;
- escolhe cores, tipografia ou identidade visual definitiva;
- transforma capacidades da Especificação Arquitetural do Guivos Journey (identificador PAS-001) em etapas obrigatórias;
- altera os contratos funcionais do Guivos Journey;
- conclui preços, planos ou regras comerciais;
- autoriza produção.

## 3. Documentos ativos

| Nome completo | Identificador | Finalidade |
|---|---|---|
| [Fundação da Arquitetura da Experiência](uxa-001-foundation.md) | UXA-001 | princípios, escopo, participantes, navegação e método |
| [Experiência Diária e Tela Hoje](uxa-002-daily-experience-and-home.md) | UXA-002 | recorrência legítima, prioridade diária e superfície inicial |
| [Mapa Inicial de Jornadas e Telas](uxa-003-journeys-and-screen-map.md) | UXA-003 | inventário de superfícies para Pessoa, Organização e Coletivo |
| [Oportunidades, Organizações, Coletivos e Mapa](uxa-004-opportunities-organizations-collectives-map.md) | UXA-004 | cadastro, descoberta, relevância, preço e localização |
| [Programa Inicial de Wireframes de Baixa Fidelidade](uxa-005-low-fidelity-wireframes.md) | UXA-005 | método, convenções, relação entre artefatos e critérios de avanço |
| [Wireframe de Baixa Fidelidade da Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | estrutura móvel da entrada diária pessoal |
| [Wireframe de Baixa Fidelidade do Detalhe de Oportunidade](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | preço, relevância, elegibilidade, fonte e ação |
| [Wireframe de Baixa Fidelidade do Cadastro pela Organização](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | fluxo institucional e etapa de preço e condições |
| [Padrão de Linguagem Clara e Identificadores Técnicos](uxa-009-plain-language-and-technical-identifiers.md) | UXA-009 | nomes completos, tradução de estados e uso secundário de códigos |

## 4. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | descoberta ativa e integrada | UXA-000 a UXA-004 |
| Resultados Empresariais (Business Outcomes) | pausados antes da decisão sobre capacidade de reinvestimento responsável | BUS-CAND-010 |
| Engenharia de Produto (Product Engineering) | pausada antes da primeira unidade de trabalho | W0-01 |
| Wireframes de baixa fidelidade | três superfícies iniciais criadas e em revisão | UXA-005 a UXA-008 |
| Protótipo navegável | não iniciado | — |
| Design visual | não iniciado | — |
| Validação de usabilidade | não iniciada | — |
| Linguagem clara | padrão criado para aplicação imediata | UXA-009 |

## 5. Wireframes iniciais

| Superfície | Canal | Situação |
|---|---|---|
| Tela Hoje | aplicativo móvel | wireframe inicial criado |
| Detalhe de oportunidade | aplicativo móvel | wireframe inicial criado |
| Cadastro de oportunidade pela Organização | web para computador | wireframe inicial criado |

Os artefatos são hipóteses estruturais. Eles não definem design visual, componentes técnicos ou comportamento implementado.

## 6. Regra de comunicação

O nome completo deverá aparecer antes do identificador técnico. Exemplo:

> Wireframe de Baixa Fidelidade da Tela Hoje (identificador UXA-006).

Identificadores não deverão aparecer sozinhos em respostas, títulos executivos ou explicações dirigidas ao Fundador.

## 7. Próximo ponto de decisão

Validar:

1. hierarquia da Tela Hoje;
2. posição de preço, relevância e elegibilidade no detalhe da oportunidade;
3. sequência e densidade do cadastro pela Organização;
4. significado e apresentação da validade do preço;
5. estados alternativos prioritários;
6. aplicação do padrão de linguagem clara;
7. autorização futura para reformulação ou protótipo navegável de baixa fidelidade.
