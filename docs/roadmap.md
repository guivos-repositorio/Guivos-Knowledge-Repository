---
id: ROADMAP-11.83.0
title: Roadmap Arquitetural — Experience Architecture Discovery
status: active
version: 11.83.0
owner: Guivos
last_updated: 2026-07-25
supersedes_partial:
  - ROADMAP-11.82.0
related:
  - GKR-STATE-001
  - UXA-000
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-004
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-017
  - M7.19.1
---

# Roadmap Arquitetural — Experience Architecture Discovery

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do GKR. O estado transversal vigente é declarado pelo [Current State Register](project/current-state-register.md).

## 2. Estado atual

| Elemento | Estado |
|---|---|
| Era | `GE-2 — Knowledge` |
| Marco | `M7.19.1` |
| Remediação R1–R5 | concluída; `PASS` |
| R6 | concluído |
| A2-R03 | ativa, operacionalmente pausada antes de `BUS-CAND-010` |
| Business Outcomes | 17 de 18 decisões; 0 submissões abertas |
| COR | 10 `Under Validation`; 2 `Merged`; 6 `Rejected` |
| CODR | 17 de 18 decisões |
| Experience Architecture | ativa em Discovery |
| Wireframes | não iniciados |
| Product Engineering | pausado antes do `W0-01` |

## 3. Sequência já executada

### 3.1 Guivos Journey

Concluído funcionalmente e publicado em `PAS-001 1.0.0 active`, com nove capacidades funcionais concluídas e implementação pausada.

### 3.2 Guivos Economic Model

Arquitetura documental inicial concluída em `GEM-001` a `GEM-010`. Parâmetros reais e validações especializadas permanecem pendentes.

### 3.3 Business Outcomes

- COR, validação externa e COEM concluídos;
- 17 de 18 decisões humanas registradas;
- `COD-001` a `COD-017` preservados;
- `BUS-CAND-010` permanece `Under Validation`;
- nenhuma submissão `018` criada;
- nenhum Outcome canônico criado.

## 4. Pausa governada

O Fundador determinou que a sequência de Business Outcomes seja pausada antes de `BUS-CAND-010` para permitir o desenvolvimento da Arquitetura da Experiência e da Jornada do Usuário.

A pausa:

- não cancela `BA-STR-002`;
- não altera a recomendação de `BUS-CAND-010`;
- não cria `COD-018`;
- não antecipa fusão;
- não inicia Business Capabilities;
- não autoriza Product Engineering.

## 5. Experience Architecture — frente ativa

### Incremento inicial

- `UXA-000` — índice e autoridade;
- `UXA-001` — fundação, princípios, participantes e navegação;
- `UXA-002` — experiência diária e tela `Hoje`;
- `UXA-003` — mapa inicial de jornadas e telas;
- `UXA-004` — oportunidades, Organizações, Coletivos e Mapa.

### Perguntas que a frente deverá responder

1. O que faz um participante retornar à Guivos de forma legítima?
2. O que aparece na tela inicial e em qual ordem?
3. Como a pessoa controla o que considera relevante?
4. Onde aparecem oportunidades, preços, condições e relações comerciais?
5. Como Organizações cadastram e gerenciam oportunidades?
6. Como Coletivos são criados, descobertos e operados?
7. Como o Mapa conecta oportunidades, Organizações, Coletivos e atividades?
8. Como alternar entre jornada pessoal, Organização e Coletivo?
9. Quais telas são necessárias antes de qualquer implementação?

## 6. Sequência proposta da Experience Architecture

1. validar fundação e navegação;
2. validar a tela `Hoje` e a hipótese de retorno;
3. validar mapa de telas;
4. detalhar fluxos críticos;
5. criar wireframes de baixa fidelidade, somente após autorização;
6. prototipar jornadas selecionadas;
7. executar testes de compreensão e usabilidade;
8. ajustar contratos de experiência;
9. preparar handoff posterior para Product Engineering.

## 7. Fluxos prioritários para wireframes futuros

1. entrada e captura progressiva de contexto;
2. `Hoje`;
3. descoberta e detalhe de oportunidade;
4. controle de relevância;
5. Mapa;
6. criação de oportunidade por Organização;
7. perfil e operação de Coletivo;
8. integração com Objetivos e Próximos Passos.

## 8. Retorno a Business Outcomes

Quando explicitamente autorizado:

1. preparar submissão de `BUS-CAND-010`;
2. receber a décima oitava decisão humana;
3. reavaliar formulações reformuladas e combinadas;
4. aplicar e ajustar `AQS-O01`;
5. consolidar catálogos canônicos;
6. desenvolver Business Capabilities.

## 9. Frentes posteriores preservadas

A ordem histórica de referência permanece:

1. Guivos Mall;
2. Guivos Business;
3. Guivos Intelligence;
4. Guivos Ads;
5. Guivos Media;
6. Guivos Travel;
7. Commercial Model;
8. Go-to-Market.

Essa ordem não autoriza início.

## 10. Próximo ponto exato

Revisar as decisões propostas por `UXA-001` a `UXA-004` e definir se o próximo incremento deverá:

- refinar a arquitetura de informação; ou
- iniciar wireframes de baixa fidelidade da tela `Hoje` e do fluxo de oportunidades.
