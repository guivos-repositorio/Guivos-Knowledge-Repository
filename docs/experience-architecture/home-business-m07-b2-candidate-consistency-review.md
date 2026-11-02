---
id: GKR-UX-HOME-BUSINESS-M07-B2-CONSISTENCY-001
title: Business B2 — revisão de consistência e dependências de publicação
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
normative: false
---

# Business B2 — revisão de consistência das versões candidatas

## Autoridade e alcance
Revisão estática das versões candidatas da branch `proposal/homes-temporal-ai-compatibility-diagnostic-20261101`, sem promoção normativa, merge, publicação, execução operacional ou alteração de Source Locks vigentes em `main`.

## Resultado da inspeção estática

| Fonte | Versão candidata | Verificação |
| --- | --- | --- |
| Home Business Documento Mestre | `1.1.11` | Adendo B2 presente junto ao M07, rotulado **não vigente**; direção principal, supporting copy e CTA permanecem preservados. |
| Business Source Lock | `1.1.29` | Adendo editorial B2 presente, rotulado **não vigente**; fonte candidata continua citando `Master 1.1.10`, `Authority 1.0.11` e sua própria `1.1.28` em referências internas congeladas. |
| Authority Contracts, Contrato 7 | `1.0.12` | Adendo B2 presente junto ao Contrato 7, rotulado **não vigente**; não amplia legitimidade de dados e resultados. |
| Leia Primeiro Business | `1.0.19` vigente | Ainda referencia Master `1.1.10`, Source Lock `1.1.28` e Authority `1.0.11`; **correto para o conjunto vigente**, mas deverá ser sincronizado somente se candidatas forem aprovadas. |
| Manifesto Canônico das Homes | `7.0.53` na branch | Ainda referencia Master `1.1.10`, Source Lock `1.1.28` e Authority `1.0.11`; não promover candidatas antes de decisão. |
| Design Handoff específico Business | Não encontrado em `docs/experience-architecture/public-home-business-design-handoff.md` | Não presumir inexistência do handoff; localizar a fonte ou contrato de handoff correto antes de criar/alterar documento. |

## Incompatibilidades a tratar antes de propor integração
1. **Referências internas no Source Lock candidato:** se o pacote candidato for aprovado, reconciliar cuidadosamente as referências às versões `1.1.11`, `1.0.12` e `1.1.29` com a hierarquia de autoridade e os blocos congelados, separando referências históricas das correntes.
2. **Leia Primeiro e Manifesto:** elaborar versões candidatas sincronizadas apenas após decisão normativa de conteúdo; manter as referências atuais como representação da `main` vigente até lá.
3. **Handoff:** identificar a fonte real de design e seu mecanismo de atualização, sem inventar caminho.
4. **Estados do conteúdo:** a marcação `não vigente` nos adendos deve sobreviver ao preparo de candidatos; qualquer promoção exige decisão expressa e revisão desses avisos.
5. **Regressões:** garantir `COMPREENDER ≠ DECIDIR`, `CORRELAÇÃO ≠ CAUSA`, ausência de leitura da Journey individual e ausência de anúncio de funcionalidades prospectivas não comprovadas.
6. **CI:** até a presente verificação, não foram retornadas execuções de workflows associadas ao commit `0b37e922dceedc0a9079691ba44be136fc19e484`. Ausência de runs retornados não é aprovação nem falha. Após eventual PR, verificar os checks do SHA relevante.

## Parecer
**Preparação B2 documental concluída; consistência transversal para integração ainda pendente.** Os textos candidatos respeitam, em leitura estática, o escopo de preparação autorizado; o pacote não deve ser integrado tal como está sem reconciliação formal das referências, validação e autorização específica.

## Próximo passo
Localizar o handoff aplicável, preparar plano de sincronização de dependências e submeter à direção a revisão normativa do texto candidato, sem aplicar mudanças de consumo externo antes dessa decisão.
