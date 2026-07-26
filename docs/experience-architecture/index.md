---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.6.0
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
  - UXA-012
normative: false
---

# Arquitetura da Experiência da Guivos (identificador UXA-000)

## 1. Finalidade

A Arquitetura da Experiência da Guivos transforma capacidades, princípios e contratos funcionais consolidados no **Repositório de Conhecimento da Guivos** em uma experiência navegável, compreensível, coerente e reconhecível para Pessoas, Organizações e Coletivos.

Ela governa, antes do design visual definitivo:

- jornadas por tipo de participante;
- arquitetura de informação e navegação;
- responsabilidade e hierarquia de cada superfície;
- controles de relevância, frequência e privacidade;
- presença companheira e posicionamento institucional;
- gate de alinhamento à Fundação da Guivos;
- coerência entre Guivos Journey, Business, Mall, Travel, Media, Ads e Intelligence;
- critérios para wireframes, protótipos e testes posteriores.

## 2. O que esta frente não representa

Esta frente não inicia Engenharia de Produto, não define tecnologia ou código, não cria design visual final, não conclui preços e planos e não autoriza produção.

## 3. Documentos ativos

| Nome completo | Identificador | Finalidade |
|---|---|---|
| [Fundação da Arquitetura da Experiência](uxa-001-foundation.md) | UXA-001 | princípios, escopo, participantes, navegação e método |
| [Experiência Diária e Tela Hoje](uxa-002-daily-experience-and-home.md) | UXA-002 | recorrência legítima, prioridade diária e superfície inicial |
| [Mapa Inicial de Jornadas e Telas](uxa-003-journeys-and-screen-map.md) | UXA-003 | inventário de superfícies para Pessoa, Organização e Coletivo |
| [Oportunidades, Organizações, Coletivos e Mapa](uxa-004-opportunities-organizations-collectives-map.md) | UXA-004 | cadastro, descoberta, relevância, preço e localização |
| [Programa Inicial de Wireframes de Baixa Fidelidade](uxa-005-low-fidelity-wireframes.md) | UXA-005 | método, convenções e critérios de avanço |
| [Wireframe de Baixa Fidelidade da Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | entrada diária pessoal reformulada |
| [Wireframe de Baixa Fidelidade do Detalhe de Oportunidade](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | jornada, preço, elegibilidade, fonte e ação contextual |
| [Wireframe de Baixa Fidelidade do Cadastro pela Organização](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | fluxo institucional e etapa de preço e condições |
| [Padrão de Linguagem Clara e Identificadores Técnicos](uxa-009-plain-language-and-technical-identifiers.md) | UXA-009 | nomes completos, tradução de estados e uso secundário de códigos |
| [Validação Funcional e Reformulação da Tela Hoje](uxa-010-today-functional-validation-and-reformulation.md) | UXA-010 | decisão humana e consequências da primeira reformulação funcional |
| [Presença Companheira e Coerência de Posicionamento da Guivos](uxa-011-companion-presence-and-ecosystem-positioning.md) | UXA-011 | princípio transversal e gate de alinhamento à Fundação |
| [Validação Funcional e Reformulação do Detalhe de Oportunidade](uxa-012-opportunity-detail-functional-validation-and-reformulation.md) | UXA-012 | decisão humana, gate fundacional e reformulação da superfície |

## 4. Estado atual

| Elemento | Situação compreensível | Referência técnica |
|---|---|---|
| Arquitetura da Experiência | descoberta ativa e integrada | UXA-000 a UXA-012 |
| Resultados Empresariais | pausados antes da capacidade de reinvestimento responsável | BUS-CAND-010 |
| Engenharia de Produto | pausada antes da primeira unidade de trabalho | W0-01 |
| Tela Hoje | validada funcionalmente e reformulada | UXA-006, UXA-010 e UXA-011 |
| Detalhe de Oportunidade | validado funcionalmente e reformulado segundo a Fundação | UXA-007, UXA-011 e UXA-012 |
| Cadastro pela Organização | wireframe inicial aguardando validação funcional | UXA-008 |
| Protótipo navegável | não iniciado | — |
| Design visual | não iniciado | — |
| Validação de usabilidade | não iniciada | — |

## 5. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à:

- Essência da Guivos;
- Propósito;
- Missão Operacional;
- Visão de Longo Prazo;
- Constituição da Guivos;
- Princípios Permanentes.

Falha material impede avanço para protótipo, design, teste, especificação técnica ou desenvolvimento.

## 6. Resultado da Tela Hoje

A Tela Hoje preserva contexto de atuação, síntese condicional, uma atenção principal, continuidade da jornada, possibilidades para o Próximo Passo, atividades temporalmente relevantes e navegação global.

## 7. Resultado do Detalhe de Oportunidade

A ordem funcional reformulada é:

```text
identidade e origem
→ como pode apoiar sua jornada
→ investimento e condições
→ o que precisa saber antes de decidir
→ condições para participar
→ quem oferece
→ relação comercial com a Guivos
→ ações contextuais
```

Decisões principais:

- a relação com a jornada antecede preço e conversão;
- a oportunidade é apresentada como possibilidade, não recomendação definitiva;
- preço e custo total permanecem visíveis e transparentes;
- relevância explica também por que a oportunidade apareceu agora;
- elegibilidade é apresentada em `Condições para participar`;
- ação principal varia conforme tipo e estado real;
- salvar e comparar permanecem alternativas legítimas;
- publicidade e comissão não alteram relevância funcional.

## 8. Presença companheira e posicionamento

Toda superfície deverá demonstrar que a Guivos acompanha a jornada sem controlar decisões, preservando contexto, explicação, alternativas, correção, pausa e recusa.

Uma formulação que poderia pertencer indistintamente a qualquer marketplace, rede social, aplicativo de tarefas ou plataforma de conteúdo deverá ser reavaliada.

## 9. Wireframes atuais

| Superfície | Canal | Situação |
|---|---|---|
| Tela Hoje | aplicativo móvel | reformulada após validação funcional |
| Detalhe de Oportunidade | aplicativo móvel | reformulado após validação funcional e gate fundacional |
| Cadastro de Oportunidade pela Organização | web para computador | wireframe inicial criado |

Os artefatos continuam sendo hipóteses estruturais, sem design visual ou implementação.

## 10. Próximo ponto de decisão

Validar funcionalmente o Cadastro de Oportunidade pela Organização aplicando presença companheira, gate fundacional, clareza institucional, responsabilidade, preço, condições e separação entre envio, avaliação, ativação e apresentação.

Protótipo navegável, design visual, testes e desenvolvimento permanecem não iniciados.