---
id: GKR-UX-HOMES-PERSON-OC-RECONCILED-CANDIDATES-001
title: Conferência de reconciliação candidata de Pessoa e Organizações e Coletivos
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Reconciliação coordenada — candidata e não vigente

Preparada na branch `proposal/person-oc-temporal-perspectives-review-20261101` por concordância da direção com a elaboração documental. **Não representa aprovação editorial ou normativa, merge nem publicação.**

| Artefato | main | branch candidata | Natureza |
| --- | --- | --- | --- |
| Mestre Pessoa | 1.0.8 | 1.0.9 | Adendos não vigentes M06/M09/M10 |
| Mestre Organizações e Coletivos | 1.0.9 | 1.0.10 | Adendos não vigentes M03/M06/M10 |
| Leia Primeiro Pessoa | 1.0.5 | 1.0.6 | Referência Pessoa atualizada |
| Leia Primeiro O/C | 1.0.5 | 1.0.6 | Referência O/C atualizada; divergência anterior 1.0.7 removida na candidata |
| Manifesto | 7.0.56 | 7.0.57 | Referências Pessoa/O/C coordenadas |

## Source Lock generativo: decisão reservada

O Manifesto candidato **mantém** `GKR-UX-HOMES-GENINPUT-001 v2.3.17` como referência. O arquivo existente na `main` declara `v2.3.18`, `active` e `normative: true`, mas o Manifesto define a versão de consumo. Sem conferência da promoção normativa e decisão específica, **não alterar a referência nem o Source Lock**, cujas referências internas continuam defasadas. Esta é uma **ressalva aberta** que impede declarar integral conformidade do pacote.

## Gates restantes

1. Aprovação editorial expressa dos seis adendos e decisão de preservação/remoção dos rótulos *não vigente* se houver futura promoção.
2. Decisão expressa sobre reconciliação do Source Lock generativo (2.3.17 ou 2.3.18), incluindo eventual impacto de suas referências internas.
3. Verificação semântica e mecânica por SHA final de futura PR, depois da deliberação de escopo.
4. Autorização de merge e autorização de publicação independentes.

**Estado:** `draft_dependencies_aligned_except_source_lock / normative_gate_open / no_merge_no_publish`.
