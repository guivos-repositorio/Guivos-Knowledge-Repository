---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.2.0
owner: Guivos Experience Architecture
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
normative: false
---

# UXA-000 — Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência da Guivos transforma capacidades, princípios e contratos funcionais já consolidados no GKR em uma experiência navegável, compreensível e coerente para Pessoas, Organizações e Coletivos.

Ela governa, antes do design visual definitivo:

- jornadas por tipo de participante;
- arquitetura de informação;
- navegação global;
- responsabilidades de cada superfície;
- hierarquia e prioridade do conteúdo;
- relações entre telas;
- pontos de entrada e retorno;
- controles de relevância, frequência e privacidade;
- fluxos entre Journey, Business, Mall, Travel, Media, Ads e Intelligence;
- critérios para wireframes, protótipos e testes posteriores.

## 2. O que esta frente não representa

Esta frente não:

- inicia Product Engineering;
- define tecnologia, componentes ou código;
- cria layout visual final;
- escolhe cores, tipografia ou identidade visual definitiva;
- transforma capacidades do `PAS-001` em etapas obrigatórias;
- altera os contratos funcionais do Guivos Journey;
- conclui preços, planos ou regras comerciais;
- autoriza produção.

## 3. Autoridades iniciais

| Documento | Finalidade |
|---|---|
| [UXA-001 — Fundação](uxa-001-foundation.md) | princípios, escopo, participantes, navegação e método |
| [UXA-002 — Experiência diária e tela Hoje](uxa-002-daily-experience-and-home.md) | recorrência legítima, prioridade diária e superfície inicial |
| [UXA-003 — Mapa de jornadas e telas](uxa-003-journeys-and-screen-map.md) | inventário de superfícies para Pessoa, Organização e Coletivo |
| [UXA-004 — Oportunidades, organizações, coletivos e mapa](uxa-004-opportunities-organizations-collectives-map.md) | fluxos de cadastro, descoberta, relevância, preço e localização |
| [UXA-005 — Programa de wireframes](uxa-005-low-fidelity-wireframes.md) | método, convenções, relação entre artefatos e gates de baixa fidelidade |
| [UXA-006 — Wireframe da tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | estrutura móvel da entrada diária pessoal |
| [UXA-007 — Wireframe do detalhe de oportunidade](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | compreensão de preço, relevância, elegibilidade, fonte e ação |
| [UXA-008 — Wireframe do cadastro pela Organização](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | fluxo institucional e etapa de preço e condições |

## 4. Estado

```text
Experience Architecture: active discovery
Business Outcomes: paused before BUS-CAND-010
Product Engineering: paused before W0-01
Low-fidelity wireframes: 3 initial surfaces drafted
Clickable prototype: not started
Visual Design: not started
Usability Validation: not started
```

## 5. Wireframes iniciais

| Superfície | Canal | Situação |
|---|---|---|
| Hoje | móvel | wireframe inicial criado |
| Detalhe de oportunidade | móvel | wireframe inicial criado |
| Cadastro de oportunidade pela Organização | desktop | wireframe inicial criado |

Os artefatos são hipóteses estruturais. Eles não definem design visual, componentes técnicos ou comportamento implementado.

## 6. Próximo gate

Validar com o Fundador:

1. hierarquia da tela `Hoje`;
2. posição de preço, relevância e elegibilidade no detalhe;
3. sequência e densidade do cadastro organizacional;
4. estados alternativos prioritários;
5. autorização para protótipo navegável de baixa fidelidade ou novo ciclo de reformulação.
