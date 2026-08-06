---
id: GKR-P1-REBASELINE-001
title: Rebaseline do P1 após a UXA-084
status: draft
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-06
depends_on:
  - GKR-STATE-001
  - GKR-P0-REBASELINE-001
  - GKR-SEMANTIC-SYNC-001
related:
  - GKR-UXA-047-084-INDEX-001
  - GKR-CHANGELOG-INDEX-001
  - GKR-CANON-ADDENDA-INDEX-001
  - UXA-084
normative: false
---

# Rebaseline do P1 após a UXA-084

## 1. Finalidade

Este documento reconstrói o P1 — Ressincronização Semântica Global — sobre a `main` posterior à recuperação do P0 e à integração da UXA-084.

O pacote corrige superfícies derivadas e controles de descoberta. Ele não altera o estado arquitetural vigente.

## 2. Ruptura de linhagem identificada

O PR nº 163 foi criado contra uma baseline anterior, quando:

- `GKR-STATE-001` estava em 1.99.0;
- o marco era M7.72;
- UXA-071 ainda não havia sido iniciada;
- a galeria integrada ainda não existia;
- P0 ainda não estava integrado.

Enquanto o PR permaneceu aberto, UXA-071 a UXA-084 avançaram por outras branches. A integração direta do PR antigo reintroduziria premissas temporais falsas, especialmente o gate que exigia a inexistência da UXA-071.

## 3. Baseline reconstruída

| Elemento | Baseline |
|---|---|
| `main` de origem | `795008499867de1820cd28b1dcef8db2e89da2f1` |
| Registro do Estado Atual | `GKR-STATE-001` 2.10.0 |
| Marco | M7.72 |
| Última frente integrada | UXA-084 |
| P0 | recuperado e integrado pelo PR nº 181 |
| Galeria visual | `draft` 0.4.0; aprovada com ressalvas |
| Matriz por SVG | `draft` 0.2.0; aprovada com ressalvas |
| Engenharia de Produto | pausada antes de W0-01 |
| Resultado Empresarial canônico | nenhum |
| Próxima frente | UXA-085, não iniciada |

## 4. Decisão sobre o P1 antigo

O conteúdo do PR nº 163 não será integrado diretamente.

Serão preservadas apenas as intenções ainda válidas:

- sincronizar README e Home com o estado corrente;
- tornar a sequência UXA descobrível;
- manter índices de changelogs e adendos;
- instalar uma política e um gate semântico;
- executar o gate em pull requests e pushes para `main`.

Serão descartadas as premissas obsoletas:

- estado 1.99.0 como vigente;
- UXA-071 não iniciada;
- ausência de artefatos UXA-071 a UXA-084;
- navegação que substitua ou reverta a árvore atual;
- qualquer referência ao P0 como não integrado.

## 5. Escopo da reconstrução

O P1 reconstruído:

1. atualiza `README.md` e `docs/index.md`;
2. cria índice UXA-047 a UXA-084;
3. recria o índice de changelogs;
4. recria o índice dos adendos canônicos;
5. estabelece política dinâmica de sincronização;
6. cria validador semântico derivado de `GKR-STATE-001`;
7. cria workflow próprio;
8. registra este rebaseline e o changelog do pacote.

## 6. Preservação da navegação atual

`mkdocs.yml` não será substituído pelo snapshot antigo.

A descobribilidade adicional ocorrerá por links no README e na Home para os índices novos. Uma alteração futura da árvore de navegação, caso necessária, deverá preservar toda a estrutura corrente e possuir escopo próprio.

## 7. Gates

Antes de qualquer merge, o pacote deverá comprovar:

- coerência de versão e marco;
- presença de UXA-047 a UXA-084 e dos respectivos links;
- ausência de premissas antigas nas superfícies vigentes;
- front matter e IDs válidos;
- links e navegação válidos;
- whitespace aprovado;
- construção MkDocs em modo estrito;
- árvore rastreada limpa;
- workflow semântico aprovado.

## 8. Fora do escopo

Este pacote não:

- altera `GKR-STATE-001`;
- promove a galeria ou a matriz por SVG;
- resolve as ressalvas da UXA-084;
- inicia UXA-085;
- retoma Engenharia de Produto;
- executa P2–P9;
- altera modelos comerciais, resultados ou evidências de mercado;
- autoriza merge automático.

## 9. Resultado esperado

```text
P1 lineage: reconstructed after UXA-084
Old PR direct merge: blocked
Semantic surfaces: synchronized
Semantic gate: dynamic
Architectural state change: none
UXA-085: not started
Product Engineering: paused
```
