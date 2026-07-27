---
id: ROADMAP-12.4.0
title: Roadmap Arquitetural — Visualização em Lista do Mapa Validada
status: active
version: 12.4.0
owner: Guivos
last_updated: 2026-07-27
supersedes_partial:
  - ROADMAP-12.3.0
related:
  - GKR-STATE-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - UXA-000
  - UXA-004
  - UXA-011-A1
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - M7.30
---

# Roadmap Arquitetural — Visualização em Lista do Mapa Validada

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do Repositório de Conhecimento da Guivos. O estado transversal vigente é declarado pelo Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | visualização em Lista do Mapa funcionalmente validada e reformulada | M7.30; UXA-028; UXA-029 |
| Remediação | concluída | R1–R6 |
| Resultados Empresariais | 18 de 18 decisões; nenhum Resultado canônico | BA-STR-002-CODR-001 |
| Candidatos | 9 em validação, 3 fundidos e 6 rejeitados | BA-STR-002-COR-001 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Início protegido | funcionalmente validado e reformulado; wireframe pendente | UXA-020; UXA-023 |
| Tela Hoje | entrada recorrente após o gate | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estado sem localização | funcionalmente validado e reformulado | UXA-026; UXA-027 |
| Visualização em Lista do Mapa | funcionalmente validada e reformulada | UXA-028; UXA-029 |
| Demais estados do Mapa | governados; wireframes não iniciados | UXA-025 |
| Protótipo, design e testes | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência executada

1. Guivos Journey concluído funcionalmente e publicado;
2. Modelo Econômico documentado inicialmente;
3. validação externa e Matriz de Avaliação concluídas;
4. decisões humanas 1 a 18 registradas;
5. remediação do repositório concluída;
6. Arquitetura da Experiência integrada;
7. Tela Hoje, Detalhe de Oportunidade e Cadastro pela Organização validados;
8. experiências de Organizações e Coletivos estruturadas e validadas;
9. relações entre Organizações e Coletivos detalhadas;
10. BUS-CAND-010 fundido em BUS-CAND-005;
11. Home pública, início protegido e Tela Hoje separados;
12. Home pública validada e reformulada;
13. wireframe gráfico da Home para computador criado;
14. início protegido da jornada validado e reformulado;
15. posição do Mapa na navegação recorrente consolidada;
16. wireframe gráfico móvel do Mapa criado;
17. Mapa funcionalmente validado e reformulado;
18. estado móvel de localização desativada criado;
19. estado sem localização funcionalmente validado e reformulado;
20. visualização móvel em Lista criada;
21. visualização em Lista funcionalmente validada e reformulada.

## 4. Sequência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não integra a sequência obrigatória de primeira entrada. Mapa e Lista são modos internos da mesma superfície recorrente.

## 5. Resultado da validação especializada

A UXA-029 confirmou, após reformulação:

- declaração `Lista territorial do Mapa · mesma consulta`;
- diferença compreensível para `Explorar`;
- contexto `Agindo como` preservado;
- localização opcional e região manual distintas;
- pesquisa vinculada à região ativa;
- total consolidado de filtros;
- quantidade e momento de atualização visíveis;
- ordenação explícita e acompanhada de explicação;
- cartões com estrutura mínima comparável;
- dados ausentes declarados sem inferência;
- item selecionado preservado;
- explicação funcional em todos os cartões;
- relação comercial separada da relevância;
- salvamento e Detalhe sem localização;
- retorno ao Mapa sem perda de contexto;
- Lista integral sem dependência do mapa carregado.

A referência possui 390 por 844 pixels. A validação é arquitetural e não equivale a teste de usabilidade, design ou implementação.

## 6. Proteções preservadas

- Lista não duplica `Explorar`;
- contexto de atuação não muda silenciosamente;
- localização permanece opcional;
- região manual não equivale a posição atual;
- busca, filtros e seleção permanecem ao trocar de modo;
- ordenação não é apresentada como personalização sem gate;
- patrocínio não aumenta relevância de forma oculta;
- dados ausentes não são completados por inferência;
- salvamento não autoriza localização ou rastreamento;
- origem manual não autoriza histórico territorial;
- troca de modo não altera permissões;
- residências e locais sensíveis permanecem protegidos.

## 7. Estado dos Resultados Empresariais

```text
External validation: completed
Initial four-test evaluation: completed
Human decisions: completed — 18 of 18
Under Validation: 9
Merged: 3
Rejected: 6
Approved Outcomes: 0
Canonical codes: 0
Reapplication of the four tests: not started
AQS-O01: not started
Canonical consolidation: not started
```

A fusão de BUS-CAND-010 em BUS-CAND-005 não aprova o candidato-alvo e não torna reinvestimento obrigatório.

## 8. Próximas etapas candidatas

### 8.1 Arquitetura da Experiência

Após integração e nova autorização, poderá ocorrer um ato separado:

1. criar o estado sem resultados;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido;
4. criar a referência móvel da Home;
5. validar a revisão da compreensão inicial;
6. validar a transição para a primeira Tela Hoje.

### 8.2 Arquitetura de Negócios

Também permanece pendente, em ato independente:

```text
reaplicação dos quatro testes
→ ajuste prático do AQS-O01
→ decisão sobre catálogos canônicos
→ matriz de sustentação entre Resultados
→ preparação da Arquitetura de Capacidades Empresariais
```

Nenhuma frente avança automaticamente.

## 9. Regras transversais preservadas

- nenhum candidato é aprovado por fusão ou reformulação;
- Resultados canônicos continuam em zero;
- reinvestimento não é obrigação automática;
- a Home não coleta relato pessoal;
- personalização exige compreensão revisável e autorizada;
- exploração geral continua disponível;
- localização não é condição universal de uso;
- publicidade não aumenta relevância pessoal;
- wireframe, validação funcional, protótipo, design, testes e desenvolvimento permanecem atos separados;
- Validação de Mercado mantém execução própria e paralela.
