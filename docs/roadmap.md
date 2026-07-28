---
id: ROADMAP-12.8.0
title: Roadmap Arquitetural — Referência Desktop do Mapa Validada
status: active
version: 12.8.0
owner: Guivos
last_updated: 2026-07-27
supersedes_partial:
  - ROADMAP-12.7.0
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
  - UXA-030
  - UXA-031
  - UXA-032
  - UXA-033
  - M7.34
---

# Roadmap Arquitetural — Referência Desktop do Mapa Validada

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do Repositório de Conhecimento da Guivos. O estado transversal vigente é declarado pelo Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | referência do Mapa para computador funcionalmente validada e reformulada | M7.34; UXA-032; UXA-033 |
| Remediação | concluída | R1–R6 |
| Resultados Empresariais | 18 de 18 decisões; nenhum Resultado canônico | BA-STR-002-CODR-001 |
| Candidatos | 9 em validação, 3 fundidos e 6 rejeitados | BA-STR-002-COR-001 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Início protegido | funcionalmente validado e reformulado; wireframe pendente | UXA-020; UXA-023 |
| Tela Hoje | entrada recorrente após o gate | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estado sem localização | funcionalmente validado e reformulado | UXA-026; UXA-027 |
| Visualização em Lista do Mapa | funcionalmente validada e reformulada | UXA-028; UXA-029 |
| Estado sem resultados | funcionalmente validado e reformulado | UXA-030; UXA-031 |
| Referência do Mapa para computador | funcionalmente validada e reformulada | UXA-032; UXA-033 |
| Referência para tablet | não iniciada | — |
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
7. Tela Hoje, Detalhe e Cadastro validados;
8. experiências de Organizações e Coletivos estruturadas e validadas;
9. relações institucionais e coletivas detalhadas;
10. BUS-CAND-010 fundido em BUS-CAND-005;
11. Home pública, início protegido e Tela Hoje separados;
12. Home pública validada e reformulada;
13. wireframe da Home para computador criado;
14. início protegido validado e reformulado;
15. posição recorrente do Mapa consolidada;
16. wireframe móvel do Mapa criado;
17. Mapa funcionalmente validado e reformulado;
18. estado sem localização criado, validado e reformulado;
19. visualização em Lista criada, validada e reformulada;
20. estado sem resultados criado, validado e reformulado;
21. referência do Mapa para computador criada;
22. referência do Mapa para computador funcionalmente validada e reformulada.

## 4. Sequência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não integra a sequência obrigatória de primeira entrada. Seus estados móveis e para computador pertencem à mesma superfície recorrente.

## 5. Resultado da validação para computador

A UXA-032 e a UXA-033 estabelecem:

- faixa compartilhada `Consulta territorial ativa`;
- valores de filtros consistentes entre resumo e controles;
- `Visão dividida ativa`;
- `Focar no Mapa` e `Focar na Lista` sem perda de contexto;
- retorno à visão dividida;
- movimento do Mapa sem atualização silenciosa;
- `Pesquisar nesta área` somente após movimento pendente;
- seleção `Marcador 1` sincronizada;
- cartões com tipo, origem, explicação e relação comercial;
- `Entender ordenação` explícito;
- painel contextual recolhível;
- recuperação do estado zero concentrada em `Consulta e filtros`;
- seleção anterior explicável;
- Lista integral sem mapa carregado.

A referência adapta disposição, não significado, e não cria catálogo independente.

## 6. Proteções preservadas

- Mapa, Lista e filtros utilizam a mesma consulta;
- localização permanece opcional;
- região manual não equivale a posição atual;
- foco não altera permissões;
- mais espaço não autoriza mais coleta;
- movimento não executa consulta automaticamente;
- filtros não são removidos sem revisão;
- seleção não altera relevância ou ordenação;
- endereço protegido não é revelado;
- relação comercial permanece separada da relevância funcional;
- zero representa somente a consulta atual;
- cobertura precisa ser verificável;
- personalização não é iniciada sem gate;
- publicidade não preenche artificialmente o estado.

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

Após integração e nova autorização, poderá ocorrer separadamente:

1. criar o wireframe gráfico do início protegido;
2. criar a referência móvel da Home;
3. validar a revisão da compreensão inicial;
4. validar a transição para a primeira Tela Hoje;
5. criar outros estados alternativos do Mapa;
6. criar referência específica para tablet, caso priorizada.

### 8.2 Arquitetura de Negócios

Permanece pendente, em ato independente:

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
