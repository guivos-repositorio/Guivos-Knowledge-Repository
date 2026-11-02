---
id: GKR-UX-HOME-BUSINESS-B2-NONREGRESSION-001
title: Business B2 — auditoria de não regressão e parecer para deliberação normativa
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Business B2 — auditoria de não regressão

## Escopo
Confronto estático entre arquivos vigentes em `main` e versões candidatas na branch `proposal/homes-temporal-ai-compatibility-diagnostic-20261101`. O parecer não aprova texto normativo, merge, publicação ou operação.

## Resultado por documento

| Documento | Versão em main | Versão candidata | Resultado estático |
| --- | --- | --- | --- |
| Home Business Documento Mestre | 1.1.10 | 1.1.11 | Diferenças encontradas: versionamento/data e adendo candidato B2. **Dez títulos de movimentos preservados**, headline, supporting copy e CTA do M07 preservados literalmente. |
| Business Source Lock | 1.1.28 | 1.1.29 | Diferenças encontradas: versionamento/data e adendo candidato B2. Direção principal, supporting copy e CTA congelados preservados literalmente. |
| Business Authority Contracts | 1.0.11 | 1.0.12 | Diferenças encontradas: versionamento/data e adendo candidato B2 ao Contrato 7. O contrato não contém necessariamente a mesma copy do M07: comparação de headline/CTA não é aplicável. |

O contraste de linhas identificou somente textos adicionados dos adendos e modificações de metadados; não detectou substituição de linhas normativas anteriores. Isso é **evidência de não regressão textual**, não comprovação de disponibilidade funcional.

## Restrições e pendências

1. **Adendos ainda rotulados não vigentes:** versões candidatas não podem ser consumidas como autoridades correntes antes de deliberação de conteúdo e integração.
2. **Sincronização pendente:** Source Lock candidato contém referências internas às versões anteriores, enquanto Leia Primeiro e Manifesto ainda declaram versões vigentes. Correção condicionada a aprovação normativa específica, não automática.
3. **Handoff aplicável identificado:** `public-homes-design-handoff.md`, seção 4.7 Business; não criar Handoff individual.
4. **Limites preservados:** `COMPREENDER ≠ DECIDIR`, `CORRELAÇÃO ≠ CAUSA`, Journey individual protegida, sem KPIs empresariais internos automáticos, sem predição demonstrada ou promessa de resultado.
5. **Validação GitHub:** uma auditoria textual não substitui workflows em PR do SHA final, nem revisão de conflitos, regras de branch e publicação separada.

## Parecer

**Resultado: não regressão textual confirmada para o escopo comparado; integração normativa não aprovada.** Recomenda-se submeter à direção a deliberação específica sobre aceitação dos adendos B2 como conteúdo normativo candidato, mantendo a separação da decisão de merge.

A decisão B2 anterior autorizou preparar e versionar documentos candidatos, não aprovar o uso público de capacidade prospectiva.

## Próximo gate documental

Após deliberação expressa sobre o conteúdo: reconciliar referências de Master, Source Lock e Authority Contracts; elaborar versões candidatas de Leia Primeiro e Manifesto; revisar necessidade de alteração no Handoff comum; validar em PR e solicitar autorização independente para eventual merge.
