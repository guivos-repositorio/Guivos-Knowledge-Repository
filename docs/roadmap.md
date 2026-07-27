---
id: ROADMAP-12.1.0
title: Roadmap Arquitetural — Estado do Mapa sem Localização Criado
status: active
version: 12.1.0
owner: Guivos
last_updated: 2026-07-26
supersedes_partial:
  - ROADMAP-12.0.0
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
  - M7.27
---

# Roadmap Arquitetural — Estado do Mapa sem Localização Criado

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do Repositório de Conhecimento da Guivos. O estado transversal vigente é declarado pelo Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | primeiro estado alternativo do Mapa criado para localização desativada | M7.27; UXA-026 |
| Remediação | concluída | R1–R6 |
| Resultados Empresariais | 18 de 18 decisões; nenhum Resultado canônico | BA-STR-002-CODR-001 |
| Candidatos | 9 em validação, 3 fundidos e 6 rejeitados | BA-STR-002-COR-001 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Início protegido | funcionalmente validado e reformulado | UXA-020; UXA-023 |
| Wireframe do início protegido | não iniciado | — |
| Tela Hoje | entrada recorrente após o gate | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estado de localização desativada | wireframe móvel criado; validação especializada pendente | UXA-026 |
| Demais estados alternativos do Mapa | governados; wireframes não iniciados | UXA-025 |
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
16. wireframe gráfico móvel do Mapa de Oportunidades criado;
17. Mapa de Oportunidades funcionalmente validado e reformulado;
18. estado móvel de localização desativada criado.

## 4. Sequência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não integra a sequência obrigatória de primeira entrada.

## 5. Resultado do estado sem localização

A UXA-026 demonstra:

- exploração geral sem personalização;
- aviso claro de localização desativada;
- escolha manual de cidade ou região;
- pesquisa territorial preservada;
- Mapa e Lista sincronizados;
- filtros e quantidade de resultados da região;
- área territorial sem marcador da pessoa;
- legenda e controles de camadas;
- oportunidade explicada por busca e região, não por Momento Atual;
- distância pessoal omitida sem origem válida;
- ativação opcional de localização aproximada;
- possibilidade de definir origem manual para rota.

A referência possui 390 por 844 pixels e não define geografia real, tecnologia cartográfica, coordenadas, design ou implementação.

## 6. Proteções preservadas

- localização permanece opcional;
- recusa de permissão não bloqueia exploração;
- marcador pessoal não aparece no estado;
- região manual permanece visível e editável;
- linguagem personalizada é removida sem gate;
- rastreamento contínuo não é exigido;
- residências e locais sensíveis permanecem protegidos;
- proximidade não equivale a relevância;
- patrocínio não aumenta relevância funcional;
- rota depende de origem válida e não contorna endereço protegido.

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

1. validar funcionalmente o estado de localização desativada;
2. criar o estado alternativo em Lista;
3. criar o estado sem resultados;
4. criar referência do Mapa para computador;
5. criar o wireframe gráfico do início protegido;
6. criar a referência móvel da Home;
7. validar a revisão da compreensão inicial;
8. validar a transição para a primeira Tela Hoje.

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

## 10. Frentes posteriores preservadas

A evolução especializada de Guivos Mall, Guivos Business, Guivos Intelligence, Guivos Ads, Guivos Media e Guivos Travel, bem como Modelo Comercial e Entrada no Mercado, continua sem autorização de início neste incremento.
