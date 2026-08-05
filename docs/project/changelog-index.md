---
id: GKR-CHANGELOG-INDEX-001
title: Índice Atual do Histórico de Evolução do GKR
status: active
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-04
depends_on:
  - GKR-STATE-001
related:
  - GKR-SEMANTIC-SYNC-001
  - GKR-CHANGELOG-1.95.0-P1
normative: false
---

# Índice Atual do Histórico de Evolução do GKR

## 1. Finalidade

Este índice conecta o ledger histórico raiz aos changelogs temáticos posteriores, sem reescrever ou apagar o histórico original.

## 2. Regra de leitura

| Faixa | Fonte de histórico |
|---|---|
| até `0.58.0` | `CHANGELOG.md` na raiz do repositório |
| após `0.58.0` | changelogs temáticos em `docs/project/` |
| estado transversal vigente | [Registro do Estado Atual](current-state-register.md) |

O arquivo `CHANGELOG.md` raiz não pertence ao diretório publicado pelo MkDocs. Sua referência permanece textual para preservar o histórico sem criar um vínculo inválido no site documental.

O número de um changelog registra a sequência editorial de seu pacote. Ele não substitui versões de arquiteturas, documentos especializados ou marcos.

## 3. Checkpoint vigente

| Elemento | Estado |
|---|---|
| marco | `M7.72` |
| autoridade | `GKR-STATE-001 1.99.0` |
| último pacote temático anterior ao P1 | `1.94.0 — UXA-070` |
| ressincronização semântica | `1.95.0 — P1` |

## 4. Histórico recente

- [1.92.0 — Expressão Guiada do Momento Atual](changelog-1.92.0-uxa-068.md)
- [1.93.0 — Validação Funcional da Expressão Guiada](changelog-1.93.0-uxa-069.md)
- [1.94.0 — Programa Funcional do Ambiente de Simulação](changelog-1.94.0-uxa-070.md)
- [1.95.0 — Ressincronização Semântica Global](changelog-1.95.0-p1-global-semantic-resynchronization.md)

Os históricos intermediários permanecem preservados no diretório `docs/project/` e em seus vínculos especializados.

## 5. Política de preservação

- o ledger raiz não será truncado;
- changelogs temáticos não serão fundidos retroativamente apenas por conveniência editorial;
- um índice pode organizar o histórico sem alterar o conteúdo dos registros;
- documentos históricos não governam o estado atual;
- divergências devem ser resolvidas pela autoridade vigente, não pela exclusão do passado.
