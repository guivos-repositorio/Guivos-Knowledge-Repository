---
id: GKR-JOURNEY-SECTION-CLARIFICATION-001
title: Clarificação de Escopo — Seção de Jornadas no GKR
status: draft
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-05
related:
  - UXA-070
  - UXA-071
  - GKR-STATE-001
  - ROADMAP-12.46.0
normative: false
---

# Clarificação de Escopo — Seção de Jornadas no GKR

## 1. Correção terminológica

Nas tratativas sobre o Ambiente de Simulação das Jornadas, o termo `domínio` foi utilizado no sentido de **área documental própria dentro do Guivos Knowledge Repository**.

Ele não significa:

- domínio de internet;
- subdomínio DNS;
- site externo ao Repositório;
- aplicação publicada em `jornadas.guivos.com`;
- novo repositório independente.

A formulação correta passa a ser:

> **seção própria de Jornadas Integradas no Guivos Knowledge Repository.**

## 2. Decisão de organização

A futura materialização deverá criar uma seção de primeiro nível no GKR, separada da sequência incremental dos documentos UXA, mas governada por eles.

Estrutura documental candidata:

```text
docs/journeys/
├── index.md
├── person.md
├── collective.md
├── organization.md
├── handoffs.md
├── scenarios.md
├── gaps.md
└── screen-catalog.md
```

Rótulo candidato na navegação do MkDocs:

```text
Jornadas Integradas
```

A nomenclatura e a árvore poderão ser refinadas durante a UXA-071, sem alterar a decisão de que a seção pertence ao próprio GKR.

## 3. Finalidade da seção

A seção deverá reunir, por referência, as jornadas completas de:

- Pessoa;
- Coletivo;
- Organização.

Ela deverá permitir:

- visualizar a sequência de telas por participante;
- alternar perspectivas em eventos compartilhados;
- identificar tela anterior, próxima tela e caminhos alternativos;
- localizar handoffs de autoridade;
- exibir maturidade, dependências e origem documental;
- mostrar estados de erro, exceção, interrupção e retorno seguro;
- revelar telas ausentes, transições incompletas e lacunas funcionais;
- abrir os SVGs e documentos canônicos sem duplicá-los.

## 4. Relação com a UXA-070

A UXA-070 permanece válida como programa funcional do ambiente documental.

Esta clarificação apenas fixa o local lógico da futura materialização:

```text
Guivos Knowledge Repository
→ seção Jornadas Integradas
→ perspectivas de Pessoa, Coletivo e Organização
→ mapas, cenários, handoffs, catálogo de telas e lacunas
```

O ambiente continua sendo uma camada de leitura por referência. Contratos, programas, wireframes, validações e registros de origem permanecem como autoridades.

## 5. Relação com a UXA-071

A UXA-071 continua não iniciada.

Quando autorizada, deverá materializar a primeira versão documental da seção dentro do GKR, incluindo:

1. página inicial da seção;
2. mapa integrado de jornadas e transições;
3. vistas por Pessoa, Coletivo e Organização;
4. catálogo unificado dos wireframes existentes;
5. matriz de maturidade e cobertura;
6. fila de lacunas e continuidades ausentes;
7. cenários mínimos previstos pela UXA-070;
8. navegação no `mkdocs.yml`.

A UXA-071 não deverá criar domínio externo, protótipo navegável ou aplicação técnica.

## 6. Preservações

Esta correção não:

- inicia a UXA-071;
- cria a pasta `docs/journeys/`;
- altera wireframes existentes;
- cria telas substitutas para lacunas;
- inicia protótipo, teste ou Engenharia de Produto;
- altera `GKR-STATE-001` 1.99.0;
- altera o marco M7.72;
- modifica P2–P9;
- autoriza publicação externa.

## 7. Estado resultante

| Elemento | Estado correto |
|---|---|
| programa funcional | concluído pela UXA-070 |
| seção própria no GKR | definida conceitualmente, ainda não materializada |
| mapa integrado | não iniciado |
| catálogo navegável de telas | não iniciado |
| UXA-071 | não iniciada |
| domínio ou subdomínio externo | fora do escopo |
| protótipo ou aplicação | não iniciados |

## 8. Próxima transição governada

A próxima transição permanece:

> **UXA-071 — Materialização Documental do Mapa Integrado de Jornadas e Transições como seção própria do Guivos Knowledge Repository.**

Sua criação e sua integração exigirão autorizações separadas.