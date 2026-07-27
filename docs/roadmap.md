---
id: ROADMAP-12.7.0
title: Roadmap Arquitetural — Referência Desktop do Mapa Criada
status: active
version: 12.7.0
owner: Guivos
last_updated: 2026-07-27
supersedes_partial:
  - ROADMAP-12.6.0
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
  - M7.33
---

# Roadmap Arquitetural — Referência Desktop do Mapa Criada

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do Repositório de Conhecimento da Guivos. O estado transversal vigente é declarado pelo Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | referência do Mapa de Oportunidades para computador criada | M7.33; UXA-032 |
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
| Referência do Mapa para computador | criada; validação funcional pendente | UXA-032 |
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
21. visualização em Lista funcionalmente validada e reformulada;
22. estado móvel sem resultados criado;
23. estado sem resultados funcionalmente validado e reformulado;
24. referência do Mapa para computador criada.

## 4. Sequência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não integra a sequência obrigatória de primeira entrada. Os estados sem localização, em Lista, sem resultados e para computador pertencem à mesma superfície recorrente.

## 5. Resultado da referência para computador

A UXA-032 demonstra, em dois arquivos de 1.440 por 1.024 pixels:

- navegação recorrente com `Mapa` selecionado;
- contexto `Agindo como: Pessoa`;
- exploração geral sem personalização;
- localização desativada e posição não acessada;
- região manual distinta da posição pessoal;
- pesquisa territorial preservada;
- painel lateral de filtros;
- Mapa como maior campo visual;
- Lista territorial da mesma consulta ao lado do Mapa;
- quantidade, atualização e ordenação sincronizadas;
- oportunidade selecionada reconhecível nos dois painéis;
- explicação funcional e relação comercial separadas;
- continuidade para o Detalhe;
- estado zero com cobertura verificável e recuperação explícita;
- operação integral da Lista sem mapa carregado.

A referência adapta disposição, não significado. Ela não cria um catálogo desktop independente.

## 6. Proteções preservadas

- Mapa e Lista utilizam a mesma consulta e versão de dados;
- localização permanece opcional;
- região manual não equivale a posição atual;
- mais espaço visual não autoriza mais coleta;
- filtros não são removidos automaticamente;
- região não é ampliada sem confirmação;
- busca não é substituída silenciosamente;
- seleção não altera relevância ou ordenação;
- endereço protegido não é revelado;
- relação comercial permanece separada da relevância funcional;
- zero representa somente a consulta atual;
- cobertura precisa ser verificável;
- falha de fonte não é apresentada como ausência de oportunidades;
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

Após integração e nova autorização, poderá ocorrer um ato separado:

1. validar funcionalmente a referência do Mapa para computador;
2. criar o wireframe gráfico do início protegido;
3. criar a referência móvel da Home;
4. validar a revisão da compreensão inicial;
5. validar a transição para a primeira Tela Hoje;
6. criar outros estados alternativos do Mapa.

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
