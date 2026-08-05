---
id: GKR-SEMANTIC-SYNC-001
title: Política de Sincronização Semântica do Estado Global
status: active
version: 1.0.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-04
depends_on:
  - GKR-STATE-001
  - ADR-001
  - ADR-005
related:
  - GKR-UPDATES-INVENTORY-001
  - GKR-UPDATE-PROGRAM-001
  - GKR-CHANGELOG-INDEX-001
  - GKR-CANON-ADDENDA-INDEX-001
normative: false
---

# Política de Sincronização Semântica do Estado Global

## 1. Finalidade

Esta política impede que superfícies de entrada, navegação, histórico e consolidação comuniquem um estado diferente daquele declarado pelo `GKR-STATE-001 — Registro do Estado Atual`.

Ela não cria estado arquitetural. Ela controla consumidores e resumos do estado já governado.

## 2. Autoridade

A ordem de precedência é:

```text
autoridade normativa de domínio
→ Registro do Estado Atual para o estado transversal
→ Roadmap, Painel e Marcos
→ matrizes, índices, páginas de entrada e navegação
→ históricos e documentos supersedidos
```

README, Home documental, MkDocs, changelog e índices não podem criar autorização, maturidade, preço, operação, produto, implementação ou próximo ato independente.

## 3. Superfícies controladas

| Superfície | Responsabilidade |
|---|---|
| `docs/project/current-state-register.md` | declarar o estado transversal vigente |
| `README.md` | oferecer entrada curta e derivada |
| `docs/index.md` | oferecer entrada navegável e derivada |
| `mkdocs.yml` | tornar ativos vigentes e índices encontráveis |
| `CHANGELOG.md` | preservar o ledger histórico legado até `0.58.0` |
| `docs/project/changelog-index.md` | orientar a continuidade do histórico posterior |
| `docs/project/canonical-consolidation-matrix.md` | preservar a matriz central consolidada em seu checkpoint |
| `docs/project/canonical-consolidation-addenda-index.md` | tornar os adendos posteriores rastreáveis |
| `scripts/validate_gkr_semantic_state.py` | detectar divergências objetivas entre essas superfícies |

## 4. Invariantes

1. O marco exibido em README e Home documental deve corresponder ao marco do Registro do Estado Atual.
2. README e Home devem apontar explicitamente para o Registro do Estado Atual.
3. Páginas de entrada não devem repetir catálogos extensos de estado mutável.
4. Produtos, preços e mecanismos comerciais candidatos devem permanecer identificados como candidatos.
5. Programa, wireframe, validação, protótipo, aplicação e operação devem permanecer estados distintos.
6. Documentos ativos recentes devem possuir navegação ou exceção documental explícita.
7. Histórico legado não deve ser apagado para corrigir drift.
8. Adendos não devem ser tratados como incorporados à matriz central sem consolidação formal.
9. A inclusão de um documento na navegação não altera sua maturidade.
10. O próximo ato descrito por uma superfície derivada não pode contradizer a autoridade vigente.

## 5. Política do changelog

O `CHANGELOG.md` raiz é preservado como ledger histórico original até `0.58.0`.

A partir dos incrementos posteriores:

- cada pacote mantém seu changelog temático em `docs/project/`;
- o `GKR-CHANGELOG-INDEX-001` organiza a continuidade e aponta o checkpoint mais recente;
- a ausência de uma entrada posterior no ledger raiz não significa ausência do incremento;
- nenhuma entrada histórica será reescrita retroativamente apenas para apresentar continuidade numérica.

## 6. Política da Matriz Canônica

A Matriz de Consolidação Canônica central preserva o checkpoint em que foi consolidada.

Adendos posteriores:

- permanecem autoridades complementares de seus pacotes;
- são listados no `GKR-CANON-ADDENDA-INDEX-001`;
- não são considerados absorvidos pela matriz central sem ato de consolidação próprio;
- não alteram silenciosamente decisões anteriores.

## 7. Validação automática

A validação semântica deverá falhar quando, no mínimo:

- README ou Home não exibirem o marco atual;
- um marco anterior explicitamente proibido permanecer nessas superfícies;
- README ou Home não apontarem o Registro do Estado Atual;
- documentos UXA-047 a UXA-070 estiverem ausentes da navegação;
- os índices de changelog ou adendos estiverem ausentes da navegação;
- esta política estiver ausente da navegação;
- UXA-071 for apresentada como iniciada sem alteração autorizada da autoridade vigente.

## 8. Limites da automação

A automação não determina:

- se uma decisão é correta;
- se uma tecnologia foi implementada;
- se um produto está disponível;
- se um preço foi aprovado;
- se uma entidade foi constituída;
- se uma evidência de mercado é suficiente;
- se uma alteração temática deve ser integrada.

Esses pontos continuam dependentes das autoridades e decisões humanas aplicáveis.

## 9. Aplicação a novos pacotes

Todo pacote que altere estado transversal deverá avaliar, antes da integração, impacto em:

- Registro do Estado Atual;
- README e Home;
- navegação;
- changelog e índice;
- Matriz e índice de adendos;
- Roadmap, Painel e Marcos;
- validador semântico.

Nem todas as superfícies precisam mudar em todo pacote. A decisão de não alterar deverá ser consciente e compatível com os invariantes.

## 10. Fronteiras deste incremento

A criação desta política:

- não altera `M7.72`;
- não altera versões globais;
- não inicia UXA-071;
- não materializa a seção integrada de telas;
- não atualiza produtos, tecnologia, mercado, marca, Fundação ou internacionalização;
- não inicia Product Engineering.
