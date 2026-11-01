---
id: GKR-UX-HOME-INTELLIGENCE-GAI-COMPAT-REVIEW-001
title: Revisão de Compatibilidade Normativa — Perspectivas Temporais da Home Intelligence
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Revisão de Compatibilidade Normativa — PR #720

**Objeto:** proposta de inclusão das perspectivas retrospectiva, contextual e prospectiva no Movimento 06 do Documento Mestre da Home Guivos Intelligence, com conexões editoriais a M05/M08/M11. **Esta revisão não aprova a alteração e não altera a autoridade do Source Lock.**

## 1. Fontes efetivamente verificadas
- [Documento Mestre](public-home-intelligence-master-document.md), candidato `v0.2.15` somente nesta PR; versão vigente na main `v0.2.14`.
- [Home Source Lock](public-home-intelligence-source-lock.md), `v1.1.16` vigente; **congela explicitamente o Master `v0.2.14`**, a copy e a arquitetura de 11 movimentos.
- [GPA-006](../product-architecture/intelligence.md), frontmatter `v2.0.3`, mas seção de autoridade e referência do Source Lock declaram `v2.0.2`. **Divergência documental de versão ainda não adjudicada.**
- [Adendo não normativo](home-intelligence-guivos-ai-temporal-reconciliation-proposed.md) na main, definindo os limites da proposta.

## 2. Resultado de compatibilidade
| Dimensão | Constatação | Situação |
| --- | --- | --- |
| Identidade do produto | `Guivos Intelligence ≠ Guivos AI` preservado | Compatível em nível semântico |
| Autoridade de decisão | `COMPREENDER ≠ DECIDIR` mantido | Compatível em nível semântico |
| Temporalidade | Produto já contém contexto temporal, cenários e incerteza | Explicitação incremental compatível em tese |
| Narrativa | 11 movimentos preservados, sem novo movimento | Compatível em estrutura |
| Source Lock | Congela Master 0.2.14; proposta altera Master para 0.2.15 | **Conflito de versão / depende de revisão governada** |
| Copy e handoff | Copy nova ainda não incorporada ao pacote congelado | **Depende de revisão/ratificação e compatibilidade do handoff** |
| GPA-006 | Cabeçalho 2.0.3, corpo 2.0.2 | **Divergência de referência superior** |
| Implementação | Nenhuma evidência de operação da tríade | Não declarar capacidade operacional comprovada |

## 3. Encaminhamentos necessários antes de qualquer merge
1. Conferir o manifesto corrente, a autoridade exata de GPA-006 e o motivo da diferença de versões; não alterar silenciosamente o produto superior.
2. Revisar e, **se aprovado pela autoridade competente**, versionar o Home Source Lock para aceitar o Master candidato; manter referência a 11 movimentos e copy autorizada.
3. Verificar o Design Handoff específico e as autoridades comuns; somente alterar se a nova semântica requerer instrução explícita à designer. Não substituir o contrato de designer-first.
4. Verificar se as regras de validação semântica, MkDocs strict build e checks pertinentes da PR passaram; não afirmar sucesso sem evidência.
5. Registrar a decisão de integração e conferir publicação no Pages separadamente após eventual merge.

## 4. Decisão atual
**Recomendação de revisão:** preservar a PR #720 em **draft, sem merge** até resolver a diferença entre Master e Source Lock e verificar o handoff. Não promover este registro ao status normativo, nem considerar a proposta aceita em produção.

**Limites:** nenhuma execução de Guivos AI, Pedido B/C, pesquisa COMP-04-P, gate, credencial, dado individual ou aprovação operacional decorre desta revisão.
