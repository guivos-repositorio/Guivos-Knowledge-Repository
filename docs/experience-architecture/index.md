---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.5.0
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
  - UXA-010
  - UXA-011
normative: false
---

# Arquitetura da Experiência da Guivos (identificador UXA-000)

## 1. Finalidade

A Arquitetura da Experiência da Guivos transforma capacidades, princípios e contratos funcionais já consolidados no **Repositório de Conhecimento da Guivos (Guivos Knowledge Repository — GKR)** em uma experiência navegável, compreensível, coerente e reconhecível para Pessoas, Organizações e Coletivos.

Ela governa, antes do design visual definitivo:

- jornadas por tipo de participante;
- arquitetura de informação;
- navegação global;
- responsabilidades de cada superfície;
- hierarquia e prioridade do conteúdo;
- relações entre telas;
- pontos de entrada e retorno;
- controles de relevância, frequência e privacidade;
- presença companheira e posicionamento institucional;
- coerência entre Guivos Journey, Guivos Business, Guivos Mall, Guivos Travel, Guivos Media, Guivos Ads e Guivos Intelligence;
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
| [Wireframe de Baixa Fidelidade da Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | estrutura móvel reformulada da entrada diária pessoal |
| [Wireframe de Baixa Fidelidade do Detalhe de Oportunidade](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | preço, relevância, elegibilidade, fonte e ação |
| [Wireframe de Baixa Fidelidade do Cadastro pela Organização](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | fluxo institucional e etapa de preço e condições |
| [Padrão de Linguagem Clara e Identificadores Técnicos](uxa-009-plain-language-and-technical-identifiers.md) | UXA-009 | nomes completos, tradução de estados e uso secundário de códigos |
| [Validação Funcional e Reformulação da Tela Hoje](uxa-010-today-functional-validation-and-reformulation.md) | UXA-010 | decisão humana, critérios e consequências da primeira reformulação funcional |
| [Presença Companheira e Coerência de Posicionamento da Guivos](uxa-011-companion-presence-and-ecosystem-positioning.md) | UXA-011 | princípio transversal de comunicação, comportamento e coerência entre produtos |

## 4. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | descoberta ativa e integrada | UXA-000 a UXA-004 |
| Resultados Empresariais (Business Outcomes) | pausados antes da decisão sobre capacidade de reinvestimento responsável | BUS-CAND-010 |
| Engenharia de Produto (Product Engineering) | pausada antes da primeira unidade de trabalho | W0-01 |
| Tela Hoje | primeira validação funcional concluída; wireframe reformulado e alinhado à presença companheira | UXA-006, UXA-010 e UXA-011 |
| Detalhe de oportunidade | wireframe inicial aguardando validação funcional segundo o novo princípio | UXA-007 e UXA-011 |
| Cadastro de oportunidade pela Organização | wireframe inicial aguardando validação funcional | UXA-008 |
| Presença companheira | princípio transversal estabelecido para todo o ecossistema | UXA-011 |
| Protótipo navegável | não iniciado | — |
| Design visual | não iniciado | — |
| Validação de usabilidade | não iniciada | — |
| Linguagem clara | padrão aplicado aos documentos ativos | UXA-009 |

## 5. Resultado da reformulação da Tela Hoje

A Tela Hoje preserva a ordem funcional:

```text
contexto de atuação
→ síntese condicional
→ atenção principal
→ movimento atual
→ possibilidades para o próximo passo
→ Coletivos e atividades, quando materialmente relevantes
→ navegação global
```

Foram aplicadas as seguintes decisões:

- seletor com `Agindo como`;
- síntese somente quando acrescentar compreensão;
- um único item principal de atenção;
- Próximo Passo antes das oportunidades;
- até dois cartões de oportunidade em largura integral;
- Coletivos e atividades somente com utilidade temporal;
- navegação Hoje, Jornada, Explorar, Mapa e Eu preservada.

## 6. Presença companheira e posicionamento

Toda superfície deverá demonstrar que a Guivos acompanha a jornada sem controlar decisões.

A experiência deverá:

- reconhecer o momento e a continuidade da jornada;
- explicar por que algo importa agora;
- relacionar informações a possibilidades ou Próximos Passos;
- preservar alternativas, correção, pausa e recusa;
- mostrar propósito por meio do comportamento da tela, não por slogans genéricos;
- manter intenção comercial explicitamente separada do apoio à jornada;
- preservar a mesma identidade institucional em todos os produtos.

A voz companheira não representa amizade simulada, intimidade artificial, pressão emocional, vigilância ou autoridade sobre a vida do participante.

## 7. Wireframes atuais

| Superfície | Canal | Situação |
|---|---|---|
| Tela Hoje | aplicativo móvel | reformulada e alinhada ao princípio de presença companheira |
| Detalhe de oportunidade | aplicativo móvel | wireframe inicial criado; validação funcional pendente |
| Cadastro de oportunidade pela Organização | web para computador | wireframe inicial criado |

Os artefatos são hipóteses estruturais. Eles não definem design visual, componentes técnicos ou comportamento implementado.

## 8. Regra de comunicação

O nome completo deverá aparecer antes do identificador técnico. Identificadores não deverão aparecer sozinhos em respostas, títulos executivos ou explicações dirigidas ao Fundador.

Textos e comportamentos deverão refletir a presença companheira e o propósito da Guivos. Uma formulação que poderia pertencer indistintamente a qualquer marketplace, rede social, aplicativo de tarefas ou plataforma de conteúdo deverá ser reavaliada.

## 9. Próximo ponto de decisão

Validar funcionalmente o Detalhe de Oportunidade aplicando, desde o início:

1. presença companheira;
2. relação explícita com a jornada;
3. explicação de relevância e temporalidade;
4. autonomia para considerar, salvar, comparar, recusar ou iniciar;
5. transparência de preço, elegibilidade, fonte e relação comercial.

Protótipo navegável, design visual, testes e desenvolvimento permanecem não iniciados.