---
id: ROADMAP-11.97.0
title: Roadmap Arquitetural — Wireframe Gráfico da Página Inicial Pública
status: active
version: 11.97.0
owner: Guivos
last_updated: 2026-07-26
supersedes_partial:
  - ROADMAP-11.96.0
related:
  - GKR-STATE-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - UXA-000
  - UXA-010
  - UXA-011-A1
  - UXA-020
  - UXA-021
  - UXA-022
  - M7.23
---

# Roadmap Arquitetural — Wireframe Gráfico da Página Inicial Pública

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do **Repositório de Conhecimento da Guivos**. O estado transversal vigente é declarado pelo Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | wireframe gráfico vetorial da Página Inicial pública criado | M7.23; UXA-022 |
| Remediação | concluída | R1–R6 |
| Resultados Empresariais | 18 de 18 decisões; nenhum Resultado canônico | BA-STR-002-CODR-001 |
| Candidatos | 9 em validação, 3 fundidos e 6 rejeitados | BA-STR-002-COR-001 |
| Arquitetura da Experiência | ativa até o wireframe gráfico da Home pública | UXA-000 a UXA-022 |
| Página Inicial pública | validada, reformulada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Referência móvel da Home | não iniciada | — |
| Início protegido da jornada | contrato estabelecido; validação detalhada pendente | UXA-020 |
| Tela Hoje | entrada recorrente após compreensão inicial | UXA-002; UXA-006; UXA-010 |
| Protótipo navegável | não iniciado | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência executada

1. Guivos Journey concluído funcionalmente e publicado;
2. Modelo Econômico documentado inicialmente;
3. validação externa dos 18 candidatos concluída;
4. Matriz de Avaliação inicial concluída;
5. decisões humanas 1 a 18 registradas;
6. remediação do repositório concluída;
7. Arquitetura da Experiência integrada;
8. Tela Hoje, Detalhe de Oportunidade e Cadastro pela Organização validados;
9. experiências de Organizações e Coletivos estruturadas e validadas;
10. relações entre Organizações e Coletivos detalhadas;
11. `BUS-CAND-010` fundido em `BUS-CAND-005`;
12. Página Inicial pública e início protegido da jornada separados;
13. Tela Hoje reposicionada como superfície recorrente;
14. Página Inicial pública validada e reformulada;
15. wireframe gráfico vetorial da Página Inicial pública criado para computador.

## 4. Resultado da Página Inicial pública

### 4.1 Pergunta respondida

A Home deverá permitir que uma pessoa compreenda:

- o que é a Guivos;
- como o ecossistema pode ser utilizado;
- que a pessoa mantém suas decisões;
- que poderá iniciar uma jornada ou explorar sem personalização;
- que a superfície pública não coleta seu relato.

### 4.2 Hierarquia validada

```text
identidade, propósito e descrição concreta da Guivos
→ ação principal adequada ao estado e exploração sem personalização
→ explicação simples de como a Guivos atua
→ caminhos pessoal, geral e institucional
→ ecossistema organizado por finalidade
→ possibilidades gerais opcionais e identificadas
→ confiança, privacidade, transparência e controle
→ acesso institucional, ajuda e rodapé
```

### 4.3 Ações por estado

- visitante: `Iniciar minha jornada` e `Explorar sem personalização`;
- pessoa com relato em andamento: `Continuar minha jornada`;
- pessoa com compreensão aguardando revisão: `Revisar minha compreensão`;
- pessoa com jornada ativa: `Ir para a Tela Hoje`.

A Home não exibirá dados do relato, alertas pessoais ou oportunidades personalizadas.

### 4.4 Ecossistema organizado

#### Jornada e possibilidades para pessoas

- Guivos Journey;
- Guivos Mall;
- Guivos Travel;
- Guivos Media.

#### Organizações, programas e Coletivos

- Guivos Business.

#### Compreensão e transparência

- Guivos Intelligence.

#### Publicidade e patrocínio institucional

- Guivos Ads.

Guivos Mall é o nome oficial do shopping do ecossistema. Guivos Ads é o nome oficial da solução de anúncios, publicidade e patrocínios.

## 5. Resultado do wireframe gráfico

O arquivo vetorial de baixa fidelidade foi criado com referência de **1.440 × 2.200 pixels**.

Ele materializa:

- cabeçalho público orientado por intenção;
- primeiro campo visual com propósito e descrição concreta;
- início voluntário e exploração sem personalização;
- garantia de ausência de coleta pública;
- explicação do funcionamento em seis etapas;
- três caminhos de entrada;
- ecossistema agrupado por finalidade;
- possibilidades gerais identificadas;
- confiança, privacidade e transparência;
- rodapé institucional.

O arquivo é monocromático e estrutural. Ele não define identidade visual, textos finais, responsividade, componentes, protótipo ou implementação.

## 6. Sequência pessoal preservada

```text
Página Inicial pública da Guivos
→ decisão voluntária de iniciar ou explorar
→ autenticação e explicação de privacidade, quando necessárias
→ ambiente protegido para relato do Momento Atual
→ compreensão inicial apresentada pela Guivos
→ revisão, correção, limitação e autorização
→ Tela Hoje
```

A criação do arquivo gráfico não valida automaticamente o ambiente protegido.

## 7. Estado da fase de Resultados Empresariais

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

A fusão de `BUS-CAND-010` em `BUS-CAND-005` não aprova o candidato-alvo e não torna reinvestimento obrigatório.

## 8. Próximas etapas candidatas

### 8.1 Arquitetura da Experiência

Após integração e nova autorização, poderá ocorrer um dos seguintes atos separados:

1. validar funcionalmente a entrada protegida da jornada;
2. criar a referência móvel da Página Inicial pública;
3. detalhar texto, voz e arquivos;
4. detalhar e validar a revisão da compreensão inicial;
5. validar a transição entre o início protegido e a Tela Hoje;
6. selecionar estados alternativos para novos wireframes.

### 8.2 Arquitetura de Negócios

Também permanece pendente, em ato independente:

```text
reaplicação dos quatro testes
→ ajuste prático do AQS-O01
→ decisão sobre catálogos canônicos
→ matriz de sustentação entre Resultados
→ preparação da Arquitetura de Capacidades Empresariais
```

Nenhuma das duas frentes avança automaticamente.

## 9. Regras transversais preservadas

- nenhum candidato é aprovado por fusão, reformulação ou contagem de testes;
- Resultados canônicos continuam em zero;
- reinvestimento não é obrigação automática;
- financiamento interno e externo permanecem alternativas legítimas;
- resultado financeiro isolado não comprova continuidade ou valor;
- a Home não coleta relato pessoal;
- personalização material exige compreensão revisável e autorizada;
- exploração geral permanece disponível sem início da jornada;
- publicidade e relação comercial permanecem identificadas;
- Guivos Ads não aumenta relevância pessoal;
- wireframe não equivale a design, protótipo ou implementação;
- a referência para computador não conclui responsividade;
- Arquitetura da Experiência não inicia Engenharia de Produto;
- protótipo, design, testes e desenvolvimento permanecem não iniciados;
- Validação de Mercado mantém execução própria e paralela.

## 10. Frentes posteriores preservadas

A evolução especializada de Guivos Mall, Guivos Business, Guivos Intelligence, Guivos Ads, Guivos Media e Guivos Travel, bem como Modelo Comercial e Entrada no Mercado, continua sem autorização de início neste incremento.
