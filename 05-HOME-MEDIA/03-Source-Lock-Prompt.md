---
id: GKR-UX-HOME-MEDIA-GENINPUT-001
title: Source Lock Operacional — Home Pública — Guivos Media — Primeira Exploração de Design
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-13
parent: GKR-UX-HOMES-GENINPUT-001
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GPA-005
normative: true
---

# Source Lock Operacional — Home Pública — Guivos Media

## 1. Finalidade

Esta instância prepara a primeira exploração de Design da **Home Pública do Guivos Media**. Ela congela as fontes vigentes para arquitetura visual e wireframe low-fi responsivo, preservando a identidade editorial própria do Media e sua relação com o ecossistema.

Estado inicial:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

## 2. Source Lock

- Home: `Guivos Media`.
- Fase: `arquitetura visual + wireframe low-fi responsivo`.
- Checkpoint: `main @ 6a4e2b2ea73c90726c3292867fdb71a91e0689db`.
- Objetivo: validar descoberta editorial, curadoria, hierarquia de conteúdo, humanidade, profundidade, recorrência e continuidade contextual em desktop e mobile.

## 3. Fontes autorizadas

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.0.0 — `docs/experience-architecture/public-homes-design-handoff.md`;
2. `GKR-UX-HOME-MEDIA-MASTER-001` v1.0.0 — `docs/experience-architecture/public-home-media-master-document.md`;
3. `GPA-005` v1.2.0 — `docs/product-architecture/media.md`.

Não adicionar automaticamente referências de portais de notícia, plataformas de streaming, redes sociais, blogs, benchmarks ou outras Homes.

## 4. Invariantes

Preservar:

1. a tese: **“Guivos Media transforma histórias, ideias, experiências e conhecimento em conteúdos que ajudam a tornar novas perspectivas visíveis.”**;
2. a pergunta-mãe **“O que você pode descobrir quando vê além do que já conhece?”**;
3. a expressão de referência **“Veja. Ouça. Leia. Descubra.”** como formas de descoberta, não departamentos;
4. `identidade editorial + curadoria + descoberta + continuidade`;
5. significado antes de quantidade;
6. curadoria antes de cronologia;
7. conteúdo antes de formato;
8. descoberta antes de classificação;
9. pessoa antes de metadados;
10. contexto antes de promoção;
11. os onze movimentos como progressão narrativa, sem obrigação de onze seções independentes;
12. Home como curadoria, não inventário;
13. Guivos Podcast como propriedade editorial do Media, nunca produto independente;
14. propriedades editoriais, tipos editoriais, formatos de expressão e destinos de publicação como níveis distintos;
15. Media diferente de Blog;
16. conteúdo patrocinado identificado e não confundido com relevância orgânica;
17. continuidade para Travel, Mall, Business, Journey ou outra capacidade apenas quando semanticamente genuína;
18. complexidade no sistema e simplicidade na experiência.

## 5. Liberdades de Design

Podem ser explorados:

- hierarquia editorial assimétrica;
- escala dominante para conteúdo principal;
- ritmo entre impacto, respiro, descoberta e profundidade;
- grid;
- composição;
- tratamento especial de `Veja / Ouça / Leia / Descubra`;
- tratamento de `Vale descobrir agora`;
- pessoas em contexto;
- fotografia, vídeo e multimídia;
- tipografia provisória;
- territórios editoriais;
- propriedades recorrentes como Guivos Podcast;
- Header, navegação, busca e CTAs;
- desktop e mobile com hierarquia própria;
- motion quando sustentar a narrativa.

Evitar cardificação como arquitetura dominante.

## 6. Proibições de inferência

Não inventar:

- conteúdos publicados;
- episódios;
- pessoas entrevistadas;
- documentários;
- séries;
- newsletters vigentes;
- audiência;
- visualizações;
- rankings;
- popularidade;
- datas;
- parceiros;
- patrocínios;
- recomendações personalizadas reais;
- categorias rígidas que não estejam governadas;
- propriedades editoriais novas apresentadas como existentes.

Não transformar:

- Media em portal de notícias;
- Home em streaming;
- Home em feed social;
- Media em sinônimo de Blog;
- conteúdos em grade uniforme de cards;
- continuidade contextual em cross-sell obrigatório.

## 7. Placeholders

Usar rótulos explícitos:

- `[CONTEÚDO DE DESTAQUE — A DEFINIR]`;
- `[HISTÓRIA REAL — A DEFINIR]`;
- `[PESSOA — PLACEHOLDER]`;
- `[PROPRIEDADE EDITORIAL — EXEMPLO]`;
- `[CONTEÚDO PATROCINADO — EXEMPLO IDENTIFICADO]`;
- `[IMAGEM / VÍDEO — A DEFINIR]`.

Guivos Podcast pode ser usado como propriedade real porque sua natureza já é governada; episódios, convidados e temporadas não devem ser inventados como vigentes.

## 8. Pacote entregue à ferramenta

Fornecer:

1. este Source Lock;
2. Handoff Canônico;
3. Documento Mestre do Media;
4. `GPA-005 — Guivos Media`.

## 9. Prompt controlado

```text
Você está trabalhando na primeira exploração de Design da Home Pública do Guivos Media.

OBJETIVO
Crie uma arquitetura visual e wireframe low-fi responsivo para desktop e mobile que permita validar descoberta editorial, curadoria, hierarquia, humanidade, profundidade, recorrência e continuidade contextual. Não produza UI final nem trate a saída como portal pronto.

FONTES
Use somente os documentos anexados e este Source Lock para decisões sobre o Guivos Media. Lacunas devem ser sinalizadas; hipóteses devem ser explicitamente rotuladas.

INVARIANTES
- preserve “O que você pode descobrir quando vê além do que já conhece?”;
- preserve a tese do Media e “Veja. Ouça. Leia. Descubra.” como formas de descoberta;
- significado antes de quantidade;
- curadoria antes de cronologia;
- conteúdo antes de formato;
- pessoa antes de metadados;
- preserve a função dos onze movimentos sem criar onze seções equivalentes;
- Home é curadoria, não inventário;
- Guivos Podcast é propriedade editorial do Media, não produto independente;
- Media não é Blog;
- conteúdo patrocinado deve ser distinguível;
- continuidade pelo ecossistema só aparece quando houver relação genuína;
- mobile preserva hierarquia editorial e não é desktop apenas empilhado.

LIBERDADE
Explore composição, escala, assimetria, grid, ritmo, mídia, tipografia provisória, territórios, propriedades editoriais, Header, busca, navegação, CTAs e motion conceitual.

NÃO INVENTE
Conteúdos, episódios, convidados, séries, newsletters, audiência, visualizações, rankings, parceiros, patrocínios ou propriedades editoriais vigentes. Use placeholders rotulados.

ANTI-TEMPLATE
Não copie Netflix, YouTube, Medium, portal de notícias, Pinterest, dashboard ou feed social. Evite fileiras infinitas e cards iguais. “Card é componente, não arquitetura.”

ENTREGUE
1. mapa resumido da página;
2. wireframe low-fi desktop;
3. wireframe low-fi mobile;
4. explicação de como os onze movimentos foram materializados sem virar onze blocos equivalentes;
5. explicação da hierarquia editorial e da curadoria;
6. indicação de onde Guivos Podcast e outras propriedades recorrentes podem viver sem dominar a Home;
7. hipóteses introduzidas;
8. lacunas encontradas;
9. autoauditoria dos invariantes.

STATUS
EXPLORAÇÃO. Nenhum conteúdo ou propriedade inventada pode ser interpretado como vigente, e nenhuma direção visual se torna canônica sem validação humana contra o GKR.
```

## 10. Autoauditoria

Antes de promover uma direção a `CANDIDATO`, confirmar:

- a primeira percepção é descoberta editorial, não portal ou streaming?;
- existe hierarquia real e não grade uniforme?;
- curadoria prevalece sobre cronologia?;
- pessoas e histórias têm contexto?;
- `Veja / Ouça / Leia / Descubra` não viraram quatro departamentos SaaS?;
- `Vale descobrir agora` possui hierarquia e não feed?;
- Guivos Podcast permanece propriedade do Media?;
- Media e Blog continuam distintos?;
- patrocinado permanece identificável?;
- continuidade pelo ecossistema não virou cross-sell forçado?;
- nenhum conteúdo, convidado, audiência ou propriedade foi inventado como real?;
- mobile preserva ritmo e hierarquia?;
- acessibilidade e performance permanecem plausíveis?;
- hipóteses estão rotuladas?

## 11. Próxima etapa

Após seleção humana de um candidato, registrar decisões, lacunas e necessidades de conteúdo antes da direção visual/UI. Conteúdo real futuro pode alimentar nova execução por Source Lock atualizado sem mudar a arquitetura da Home.

## 12. Síntese

> **A ferramenta pode explorar como histórias e perspectivas ganham forma editorial; não pode inventar o catálogo do Media nem reduzir descoberta a uma grade de conteúdo.**
