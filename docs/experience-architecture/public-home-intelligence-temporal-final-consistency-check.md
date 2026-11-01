---
id: GKR-UX-HOME-INTELLIGENCE-GAI-CONSISTENCY-001
title: Checagem estática de consistência — PR 720
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Checagem estática de consistência — PR #720

**Área de governança das Homes:** Experiência e Journey (`docs/experience-architecture/`).  
**Escopo:** leitura dos arquivos candidatos na branch `proposal/home-intelligence-temporal-perspectives-20261101`. **Nenhum teste automatizado, build, gate ou publicação Pages verificado nesta etapa.**

## 1. Resultado por documento
| Fonte | Versão lida | Resultado |
| --- | --- | --- |
| [Documento Mestre](public-home-intelligence-master-document.md) | 0.2.15 candidata | Tríade temporal no M06; preservados 11 movimentos |
| [Home Source Lock](public-home-intelligence-source-lock.md) | 1.1.17 candidata | Quatro ocorrências do Master 0.2.15, zero do 0.2.14; atualização depende de aprovação |
| [Design Handoff](public-home-intelligence-design-handoff.md) | 1.1.18 candidata | Referências ao Master 0.2.15; orientação sem novos motores ou promessa preditiva |
| [Arquitetura Conceitual](public-home-intelligence-conceptual-architecture.md) | 0.2.6 vigente | Não alterada; mantém 11 movimentos |
| [GPA-006](../product-architecture/intelligence.md) | frontmatter 2.0.3 | Corpo ainda identifica 2.0.2 como autoridade; não corrigir por inferência |
| `mkdocs.yml` | conferido estaticamente | Home Intelligence continua navegável sob Experiência e Journey |

## 2. Invariantes preservados
- Guivos Intelligence não é sinônimo de Guivos AI; inteligência de produto e infraestrutura/capacidades de IA são responsabilidades distintas.
- Retrospectiva, Contextual e Prospectiva são lentes complementares, não estágios obrigatórios ou predição determinística.
- M06 é a inserção semântica principal; M05, M08 e M11 recebem orientação contextual; permanece o conjunto de 11 movimentos.
- `COMPREENDER ≠ DECIDIR`; `RESULTADO ESPERADO ≠ RESULTADO COMPROVADO`; profundidade de compreensão não confere direito de exposição de dados individuais.
- Designer-first e Design Release previamente governado não representam implantação ou operação autorizada.

## 3. Pendências para merge
1. **GPA-006:** frontmatter 2.0.3 e referência textual de autoridade 2.0.2 precisam de adjudicação da fonte canônica; editar o produto sem comprovação seria indevido.
2. **Manifesto:** confirmar os IDs e versões nas autoridades/manifesto corrente, não inferir alinhamento só pela leitura de três arquivos.
3. **Validações:** executar pelo fluxo de PR, quando permitido, e verificar resultados reais de checks sem declarar sucesso antecipado; nenhuma validação automatizada foi executada nesta análise.
4. **Handoff e narração:** conferir que a copy congelada e as regras transversais continuam compatíveis com a revisão candidata.
5. **Integração:** manter PR #720 em draft até prova dos itens anteriores e decisão de merge conforme governança; conferir o deploy Pages separadamente.

## 4. Disposição
**Consistência documental local: parcialmente confirmada. Elegibilidade para merge: não demonstrada.** Este arquivo é relatório de inspeção estática de conteúdo, não parecer institucional ou validação oficial. A main permanece com versões anteriormente vigentes até integração efetiva.
