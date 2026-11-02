---
id: GKR-UX-HOMES-PERSON-OC-REF-RECON-001
title: Plano candidato de reconciliação de referências — Pessoa e O/C
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Reconciliação de referências — proposta para deliberação

## Limite da decisão recebida
A direção concordou com o encaminhamento de reconciliação documental. Este aceite autoriza **preparar e conferir uma proposta**, não implica aprovação normativa dos seis adendos, alteração de contratos de autoridade, merge ou publicação.

## Diferenças confirmadas diretamente na main e destino candidato

| Fonte | Declaração vigente na main | Proposta condicionada |
| --- | --- | --- |
| Leia Primeiro Pessoa 1.0.5 | Pessoa 1.0.8 | Referenciar candidata Pessoa 1.0.9 |
| Leia Primeiro O/C 1.0.5 | O/C 1.0.7 | Referenciar candidata O/C 1.0.10 |
| Manifesto 7.0.56 | Pessoa 1.0.8 | Pessoa 1.0.9 |
| Manifesto 7.0.56 | O/C 1.0.9 | O/C 1.0.10 |
| Manifesto 7.0.56 | Generative Source Lock 2.3.17 | **Não promover automaticamente:** verificar por que o arquivo na main declara 2.3.18 |
| Generative Source Lock 2.3.18 | Pessoa 1.0.7; O/C 1.0.7 | Propor referências 1.0.9 / 1.0.10, **sujeito ao gate próprio do Source Lock** |

## Sequência proposta de atualização
1. Aprovar especificamente o texto dos adendos temporais de Pessoa M06/M09/M10 e O/C M03/M06/M10, hoje marcados *não vigente*.
2. Confirmar a autoridade e o status de promoção do Source Lock generativo `2.3.18` versus a versão `2.3.17` do Manifesto. **A versão física mais alta não prova vigência normativa.**
3. Produzir patch coordenado dos dois Leia Primeiro, Manifesto e — apenas se autorizado — Source Lock generativo. Não modificar o Handoff global sem necessidade semântica demonstrada.
4. Conferir invariantes: 11 movimentos Pessoa, 12 movimentos O/C; CTAs, Hero, conteúdo original, autonomia, privacidade, causalidade e separação entre hipótese e previsão preservados.
5. Submeter PR a validações por commit (semântica/mecânica) e solicitação distinta de merge. Publicação exige autorização própria.

## Bloqueios explícitos
- Não converter a simples autorização de elaboração em decisão normativa.
- Não promover Source Lock por inferência de numeração.
- Não afirmar publicação, atualização do GitHub Pages ou execução operacional.

**Estado:** `reconciliation_patch_plan_prepared / normative_approval_pending / source_lock_promotion_unresolved / no_merge`.
