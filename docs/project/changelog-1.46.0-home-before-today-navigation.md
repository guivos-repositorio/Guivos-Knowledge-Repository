---
id: GKR-CHANGELOG-1.46.0
title: Histórico de Alterações 1.46.0 — Home Antes da Tela Hoje
status: historical
version: 1.46.0
owner: Guivos
last_updated: 2026-07-26
related:
  - UXA-000
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-006
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
normative: false
---

# Histórico de Alterações 1.46.0 — Home Antes da Tela Hoje

## Correção realizada

A navegação oficial e os documentos de orientação da Arquitetura da Experiência foram reconciliados para refletir a ordem funcional correta da jornada pessoal.

```text
Página Inicial pública da Guivos
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ navegação recorrente: Hoje | Jornada | Explorar | Mapa | Eu
```

## Motivo

A numeração histórica dos documentos fazia o Wireframe da Tela Hoje, identificado como UXA-006, aparecer antes do Wireframe da Página Inicial Pública, identificado como UXA-022.

Essa ordem documental não representa a ordem das telas. O menu oficial também omitia os documentos UXA-020 a UXA-023, gerando uma leitura incorreta.

Também era necessário esclarecer que o Mapa de Oportunidades não é uma etapa obrigatória entre a Home e a Tela Hoje.

## Adicionado

- UXA-003-A1 — Correção da Ordem Funcional da Primeira Entrada Pessoal;
- explicação explícita de que identificadores registram criação documental, não precedência de tela;
- acesso direto ao wireframe da Página Inicial pública no menu oficial;
- posição explícita do Mapa como superfície própria da navegação recorrente;
- três acessos complementares ao Mapa: Home pública, Explorar e bloco `Perto de mim` da Tela Hoje.

## Alterado

- menu oficial da Arquitetura da Experiência reorganizado por responsabilidade funcional;
- Página Inicial pública posicionada antes da Tela Hoje;
- `Explorar e Mapa` separado da primeira entrada e apresentado como navegação recorrente;
- Programa Inicial de Wireframes reorganizado pela ordem real de uso;
- visão geral da Arquitetura da Experiência reorganizada por responsabilidades;
- documentos ativos UXA-020 a UXA-023 incluídos na navegação oficial;
- histórico detalhado retirado do menu principal, permanecendo construído e pesquisável.

## Wireframe da Home preservado

O wireframe da Página Inicial pública já existe como:

- documento: UXA-022 — Wireframe de Baixa Fidelidade da Página Inicial Pública da Guivos;
- arquivo vetorial: `docs/assets/wireframes/uxa-022-public-home-desktop.svg`;
- dimensão de referência: 1.440 por 2.200 pixels;
- canal: web para computador.

A versão móvel da Home permanece pendente.

## Posição do Mapa de Oportunidades

O Mapa passa a ser apresentado oficialmente em três níveis:

1. Home pública — acesso secundário para exploração geral por cidade ou região, sem personalização;
2. Tela Hoje — bloco compacto `Perto de mim`, com a ação `Abrir no mapa`;
3. Mapa — superfície completa e independente da navegação `Hoje | Jornada | Explorar | Mapa | Eu`.

O contrato funcional do Mapa permanece em UXA-004. O wireframe gráfico do Mapa ainda não foi criado.

## Preservado

- UXA-006 permanece o identificador histórico da Tela Hoje;
- Tela Hoje permanece a superfície recorrente posterior ao gate;
- a Home pública não coleta texto pessoal, voz, arquivos ou fontes externas;
- o início protegido permanece separado da Home;
- o wireframe do início protegido permanece pendente;
- o wireframe gráfico do Mapa permanece pendente;
- localização de participantes e locais sensíveis permanece protegida;
- protótipo, design visual, testes e Engenharia de Produto permanecem não iniciados;
- Resultados Empresariais permanecem sem alteração.
