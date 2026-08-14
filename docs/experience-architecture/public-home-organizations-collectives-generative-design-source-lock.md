---
id: GKR-UX-HOME-OC-GENINPUT-001
title: Source Lock Operacional — Home Pública — Organizações e Coletivos — Primeira Exploração de Design
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-13
parent: GKR-UX-HOMES-GENINPUT-001
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-OC-MEDIA-SUPPLY-001
normative: true
---

# Source Lock Operacional — Home Pública — Organizações e Coletivos

## 1. Finalidade

Esta instância prepara a primeira exploração de Design da **Home Pública — Organizações e Coletivos**. Ela congela fontes e invariantes para arquitetura visual e wireframe low-fi responsivo sem criar nova arquitetura.

Estado inicial da saída:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

## 2. Source Lock

- Home: `Organizações e Coletivos`.
- Fase: `arquitetura visual + wireframe low-fi responsivo`.
- Checkpoint: `main @ 6a4e2b2ea73c90726c3292867fdb71a91e0689db`.
- Objetivo: validar hierarquia, narrativa, participação, confiança, prova, capacidades, caminhos de ação e comportamento desktop/mobile.

## 3. Fontes autorizadas

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.0.0 — `docs/experience-architecture/public-homes-design-handoff.md`;
2. `GKR-UX-HOME-OC-MASTER-001` v0.1.0 — `docs/experience-architecture/public-home-organizations-collectives-master-document.md`;
3. `GKR-UX-HOME-OC-MEDIA-SUPPLY-001` v1.0.0 — `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md`.

Não incluir automaticamente P1–P5, auditorias, wireframes históricos, benchmarks ou outras Homes. Fontes adicionais só entram após declaração explícita.

## 4. Invariantes

A materialização deve preservar:

1. a pergunta-mãe **“O que podemos tornar possível juntos?”**;
2. Organizações e Coletivos como outra perspectiva da mesma Guivos, não uma Guivos paralela;
3. capacidade e participação antes de produto;
4. confiança antes de conversão;
5. autonomia antes de dependência;
6. a Pessoa continuando no centro da própria jornada mesmo quando a perspectiva inicial é da Organização ou do Coletivo;
7. os onze movimentos como progressão narrativa, sem obrigação de onze blocos equivalentes;
8. a página como Home narrativa, não landing page B2B, portal de fornecedores, área de patrocinadores ou catálogo comercial;
9. prova baseada em realidade, responsabilidade e autoridade;
10. fato governado, evidência verificável, interpretação editorial, cenário ilustrativo e estado futuro mantendo naturezas distinguíveis;
11. Media podendo documentar e fornecer histórias, conhecimento e evidências, sem transformar a Home em mural de cases do Media;
12. conteúdo sobre uma Organização não provando automaticamente parceria, impacto ou participação ativa na Guivos;
13. conteúdo patrocinado não adquirindo autoridade institucional por ter aparência editorial.

## 5. Liberdades de Design

Podem ser explorados grid, composição, dobras, agrupamentos, escala, ritmo, tipografia provisória, fotografia, vídeo, tratamento de capacidades, prova, iniciativas, Header, navegação, CTAs, microinterações e soluções distintas para desktop e mobile.

A solução não precisa replicar a Home da Pessoa. `Mesma família` não significa `mesmo template`.

## 6. Proibições de inferência

Não inventar:

- parceiros;
- Organizações participantes;
- Coletivos ativos;
- números de impacto;
- resultados sociais;
- cases;
- depoimentos;
- programas vigentes;
- campanhas;
- patrocinadores;
- planos comerciais;
- benefícios;
- métricas;
- integrações;
- capacidades que não estejam governadas.

Não transformar cenário ilustrativo em case real, nem tratamento audiovisual em prova factual.

## 7. Placeholders

Quando necessário, usar rótulos explícitos, por exemplo:

- `[ORGANIZAÇÃO REAL — A DEFINIR]`;
- `[COLETIVO REAL — A DEFINIR]`;
- `[INICIATIVA VERIFICÁVEL — A DEFINIR]`;
- `[HISTÓRIA DOCUMENTADA — A DEFINIR]`;
- `[EVIDÊNCIA — A DEFINIR]`.

## 8. Pacote entregue à ferramenta

Fornecer:

1. este Source Lock;
2. Handoff Canônico;
3. Documento Mestre de Organizações e Coletivos;
4. Reconciliação pós-Media de Organizações e Coletivos.

## 9. Prompt controlado

```text
Você está trabalhando na primeira exploração de Design da Home Pública da Guivos para Organizações e Coletivos.

OBJETIVO
Crie uma arquitetura visual e wireframe low-fi responsivo para desktop e mobile. A saída deve permitir avaliar narrativa, hierarquia, participação, confiança, prova, capacidades e caminhos de ação. Não produza UI final nem trate a solução como implementação aprovada.

FONTES
Use exclusivamente os documentos anexados e este Source Lock para decisões sobre a Guivos e esta Home. Quando faltar informação, sinalize a lacuna ou crie hipótese explicitamente rotulada.

INVARIANTES
- preserve “O que podemos tornar possível juntos?”;
- esta é outra perspectiva da mesma Guivos, não uma marca B2B separada;
- capacidade e participação vêm antes de produto;
- confiança vem antes de conversão;
- autonomia dos participantes deve permanecer visível;
- preserve a função dos onze movimentos sem criar onze blocos equivalentes por obrigação;
- não transforme a página em portal de fornecedores, área de patrocínio, catálogo B2B ou landing SaaS;
- prova precisa ser verificável e não pode ser fabricada;
- conteúdo do Media pode documentar histórias e iniciativas, mas não prova automaticamente parceria, impacto ou participação;
- patrocinado deve permanecer distinguível de evidência institucional;
- mobile deve preservar hierarquia e intenção, não apenas empilhar desktop.

LIBERDADE
Explore grid, composição, ritmo, tipografia provisória, mídia, componentes, Header, navegação, CTAs, prova, capacidades, agrupamentos e comportamento responsivo.

NÃO INVENTE
Organizações, Coletivos, parceiros, cases, métricas, impacto, depoimentos, patrocinadores, planos, campanhas ou programas vigentes. Use placeholders rotulados.

ANTI-TEMPLATE
Evite solução SaaS/B2B automática com hero comercial + logos + benefícios + pricing + CTA. A página deve comunicar possibilidade conjunta, capacidade, participação e confiança antes de conversão.

ENTREGUE
1. mapa resumido da página;
2. wireframe low-fi desktop;
3. wireframe low-fi mobile;
4. explicação dos agrupamentos narrativos;
5. hipóteses introduzidas;
6. lacunas encontradas;
7. autoauditoria dos invariantes.

STATUS
EXPLORAÇÃO. Nenhum output se torna canônico sem validação humana contra o GKR.
```

## 10. Autoauditoria

Antes de promover uma direção a `CANDIDATO`, confirmar:

- a página parece Guivos, não uma empresa B2B paralela?;
- capacidade e participação antecedem produto e conversão?;
- a Pessoa não desapareceu conceitualmente?;
- os onze movimentos foram preservados em função?;
- prova real e cenário ilustrativo continuam distinguíveis?;
- conteúdo do Media não virou case automático?;
- patrocinado não parece autoridade institucional?;
- nenhuma Organização, impacto ou parceria foi inventada?;
- desktop e mobile possuem decisões adequadas?;
- acessibilidade e performance continuam plausíveis?;
- hipóteses estão identificadas?

## 11. Próxima etapa

Após seleção humana de um candidato, registrar decisões aceitas, rejeitadas e lacunas antes de iniciar direção visual/UI. Uma nova fase exige novo Source Lock ou reconciliação explícita do checkpoint.

## 12. Síntese

> **A ferramenta pode explorar como capacidades e participantes se tornam compreensíveis juntos; não pode fabricar prova, parceria, impacto ou transformar esta perspectiva pública em uma landing page B2B.**
