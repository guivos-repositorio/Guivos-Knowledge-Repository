---
id: UXA-003-A1
title: Correção da Ordem Funcional da Primeira Entrada Pessoal
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-003
depends_on:
  - UXA-003
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
related:
  - UXA-002
  - UXA-004
  - UXA-005
  - UXA-006
  - UXA-010
normative: false
---

# Correção da Ordem Funcional da Primeira Entrada Pessoal

## 1. Finalidade

Este adendo corrige a leitura da ordem funcional apresentada no Mapa Inicial de Jornadas e Telas.

Ele substitui exclusivamente:

- a arquitetura global de entrada da jornada pessoal;
- a ordem das superfícies de descoberta e primeira entrada;
- a ordem funcional dos wireframes pessoais;
- a posição do Mapa de Oportunidades em relação à Home e à Tela Hoje.

As demais definições do documento principal permanecem válidas.

## 2. Regra de interpretação

Os identificadores da Arquitetura da Experiência registram a ordem histórica de criação dos documentos. Eles não representam a ordem em que as telas aparecem para a pessoa.

A existência do identificador **UXA-006 — Wireframe da Tela Hoje** antes do identificador **UXA-022 — Wireframe da Página Inicial Pública** não significa que a Tela Hoje antecede a Home.

## 3. Ordem funcional obrigatória

A jornada pessoal começa pela Página Inicial pública da Guivos.

```text
Página Inicial pública da Guivos
→ decisão voluntária de iniciar ou explorar
→ explicação do ambiente protegido e das alternativas
→ autenticação ou criação de conta
→ finalidades, privacidade e controles
→ escolha da modalidade de relato
→ compartilhamento mínimo e progressivo
→ revisão do que foi recebido
→ autorização específica para processamento aplicável
→ compreensão inicial revisável
→ correção, limitação e decisão da pessoa
→ Tela Hoje, jornada sem personalização ou exploração geral
→ navegação recorrente: Hoje | Jornada | Explorar | Mapa | Eu
```

A Tela Hoje é a superfície recorrente posterior ao início da jornada e à compreensão inicial suficiente, revisável e autorizada.

O Mapa não entra entre a Home e a Tela Hoje. Ele é uma superfície própria da navegação recorrente, com acessos complementares pela Home, por Explorar e pelo bloco contextual `Perto de mim` da Tela Hoje.

## 4. Superfícies da primeira entrada

| Ordem | Superfície | Referência principal | Situação |
|---:|---|---|---|
| 1 | Página Inicial pública da Guivos | UXA-020, UXA-021 e UXA-022 | validada e com wireframe gráfico para computador |
| 2 | Início protegido da jornada | UXA-020 e UXA-023 | funcionalmente validado; wireframe gráfico pendente |
| 3 | Compreensão inicial | UXA-011-A1, UXA-020 e UXA-023 | contrato estabelecido; validação especializada posterior |
| 4 | Tela Hoje | UXA-002, UXA-006 e UXA-010 | validada como superfície recorrente |
| 5 | Navegação recorrente | UXA-002, UXA-003 e UXA-004 | Hoje, Jornada, Explorar, Mapa e Eu |

## 5. Wireframe da Página Inicial

O wireframe da Home já foi elaborado e está registrado como:

> **UXA-022 — Wireframe de Baixa Fidelidade da Página Inicial Pública da Guivos**

Arquivo gráfico vetorial:

`docs/assets/wireframes/uxa-022-public-home-desktop.svg`

A referência atual representa uma página web para computador com dimensão estrutural de 1.440 por 2.200 pixels.

A versão móvel da Home permanece pendente e não deve ser confundida com a inexistência do wireframe principal.

## 6. Posição do Mapa de Oportunidades

O Mapa possui três níveis de presença.

### 6.1 Home pública

A Home poderá oferecer um acesso secundário como `Ver oportunidades no mapa` ou `Explorar por região`.

Nesse estado:

- a exploração será geral e não personalizada;
- a pessoa poderá escolher cidade ou região;
- a Guivos não afirmará relevância pessoal;
- localização exata não será obrigatória;
- oportunidades, Organizações, Coletivos e atividades poderão ser apresentados com origem e condições visíveis.

### 6.2 Tela Hoje

A Tela Hoje poderá exibir um bloco compacto denominado `Perto de mim` quando localização estiver autorizada e houver utilidade material.

O bloco poderá apresentar uma oportunidade, atividade, Organização, Coletivo, serviço ou experiência próxima e oferecer a ação `Abrir no mapa`.

A Tela Hoje não incorporará o mapa completo.

### 6.3 Superfície própria Mapa

O Mapa será uma das cinco áreas principais da navegação recorrente:

```text
Hoje | Jornada | Explorar | Mapa | Eu
```

A superfície completa poderá reunir:

- oportunidades;
- Organizações;
- Coletivos;
- eventos e atividades;
- experiências públicas;
- pontos de apoio;
- locais salvos;
- mapa e lista sincronizada;
- pesquisa nesta região;
- perto de mim;
- calendário geográfico;
- rota ou deslocamento;
- filtros de categoria, data, distância, preço, modalidade, disponibilidade, acessibilidade e origem.

## 7. Relação entre Explorar e Mapa

`Explorar` organiza descoberta ampla por lista, busca, filtros e categorias.

`Mapa` organiza a mesma descoberta pela dimensão territorial.

As duas superfícies deverão permanecer sincronizadas quando aplicável:

```text
Explorar em lista
↔ visualizar no Mapa
↔ abrir detalhe da oportunidade
```

Proximidade geográfica não equivale a relevância. Patrocínio não altera a posição funcional de uma oportunidade.

## 8. Ordem funcional dos wireframes

1. Página Inicial pública da Guivos — wireframe criado em UXA-022;
2. início protegido da jornada — wireframe gráfico pendente;
3. primeira Tela Hoje após a compreensão inicial — estado específico pendente;
4. Tela Hoje recorrente — wireframe criado em UXA-006;
5. Mapa de Oportunidades — contrato funcional existente em UXA-004 e wireframe gráfico ainda pendente;
6. detalhe da oportunidade — wireframe criado em UXA-007;
7. cadastro de oportunidade pela Organização — wireframe criado em UXA-008;
8. demais superfícies pessoais, institucionais e coletivas conforme dependências.

## 9. Privacidade territorial

O Mapa não deverá:

- mostrar localização de participantes;
- revelar residência ou local sensível de membros;
- exigir localização contínua;
- utilizar histórico sensível para publicidade;
- presumir interesse somente pela proximidade;
- revelar endereço protegido antes da autorização aplicável.

A pessoa poderá utilizar localização exata temporária, localização aproximada, cidade informada, região selecionada ou localização desativada.

## 10. Efeitos bloqueados

Esta correção não:

- renumera documentos existentes;
- elimina a Tela Hoje;
- transforma a Home em painel pessoal;
- permite coleta de relato na superfície pública;
- cria um novo wireframe duplicado da Home;
- cria a versão móvel da Home;
- cria o wireframe do início protegido;
- cria o wireframe gráfico do Mapa;
- define tecnologia de geolocalização, rotas ou mapas;
- inicia protótipo, design visual, teste ou desenvolvimento.

## 11. Decisão consolidada

A leitura oficial do repositório passa a ser:

> **A Página Inicial pública da Guivos antecede o início protegido da jornada e a Tela Hoje. O Mapa de Oportunidades é uma superfície própria da navegação recorrente, acessível também pela exploração geral da Home, por Explorar e pelo bloco Perto de mim.**
