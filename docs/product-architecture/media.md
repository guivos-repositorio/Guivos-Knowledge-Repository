---
id: GPA-005
title: Guivos Media
status: consolidated
version: 1.1.0
owner: Guivos
last_updated: 2026-08-13
related:
  - GLPA-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GPA-001
  - GPA-003
  - GPA-004
  - GPA-006
  - GPA-007
---

# Guivos Media

## Papel

Guivos Media é o produto responsável pela produção, organização e distribuição de conteúdo editorial e institucional da Guivos.

Na arquitetura em camadas do ecossistema, Guivos Media pertence à **Service Layer**.

Sua responsabilidade editorial não substitui o Guivos Journey, a operação de viagens, a unidade comercial do Mall, a solução B2B, a camada de inteligência ou a plataforma de publicidade.

## Escopo principal

Guivos Media suporta progressivamente:

- podcast;
- vídeos;
- entrevistas;
- documentários;
- histórias reais;
- imprensa;
- livros;
- artigos;
- newsletters;
- transmissões;
- séries de conteúdo;
- conteúdo editorial e institucional;
- conteúdos educacionais, formativos e de conhecimento quando aderentes ao papel do produto.

A existência desses formatos não exige que todos possuam área própria na Home ou sejam tratados como produtos independentes.

## Modelo editorial

Guivos Media organiza seu conteúdo em níveis distintos.

### Produto / especialidade

**Guivos Media** é o produto especializado da Service Layer.

### Propriedades editoriais

Propriedades editoriais são identidades recorrentes que vivem dentro do Media, como Guivos Podcast, séries identificadas, programas, newsletters específicas e projetos editoriais recorrentes.

### Tipos editoriais

Podem incluir entrevista, documentário, artigo, história real, reportagem, conversa, ensaio, cobertura e livro.

### Formatos de expressão

Podem incluir vídeo, áudio, texto, imagem, multimídia e ao vivo.

Esses níveis não devem ser tratados como equivalentes na taxonomia, na navegação ou na arquitetura de dados.

## Conteúdo-base e relações semânticas

Uma produção editorial pode existir como núcleo único e gerar vídeo completo, áudio, artigo, cortes, citações, newsletter e publicações sociais. Essas manifestações devem permanecer relacionadas ao mesmo conteúdo-base quando representarem a mesma produção.

Conteúdos podem relacionar-se a pessoas, lugares, assuntos, perspectivas, propriedades editoriais, outros conteúdos, organizações, destinos de publicação e continuações contextuais.

> **Complexidade no sistema. Simplicidade na experiência.**

## Guivos Podcast

Guivos Media substitui **Guivos Podcast** como nome de produto.

A precisão arquitetural vigente é:

```text
GUIVOS MEDIA
→ produto / especialidade

GUIVOS PODCAST
→ propriedade editorial do Guivos Media

TEMPORADA
→ estrutura da propriedade

EPISÓDIO
→ unidade editorial

ÁUDIO / VÍDEO / TEXTO
→ expressões possíveis
```

`podcast`, quando utilizado genericamente, permanece um formato editorial suportado pelo Media.

`Guivos Podcast`, como nome próprio, é uma propriedade editorial e não um produto equivalente aos demais componentes especializados.

## Relação com o Guivos Blog

Guivos Media e Guivos Blog não são sinônimos.

Guivos Media é o produto / especialidade editorial multimídia e semântica da Service Layer. Guivos Blog é um canal ou destino editorial predominantemente textual.

O Blog pode receber publicações originadas no Media e também em outras especialidades da Guivos. O Media pode referenciar, selecionar ou distribuir conteúdos por meio do Blog.

Consequências:

- nem todo conteúdo do Blog precisa nascer no Media;
- nem toda produção do Media precisa ser publicada no Blog;
- o Blog não deve ser tratado como produto equivalente ao Media;
- conteúdo textual do Media não deve ser automaticamente reduzido ao Blog.

## Distribuição editorial e continuidade no ecossistema

Destinos de publicação e continuações contextuais são relações diferentes.

### Distribuição

Pode incluir superfície Guivos Media, Guivos Blog, newsletters, redes sociais, plataformas externas e outros canais editoriais autorizados.

Distribuição responde:

> **Onde este conteúdo é publicado ou manifestado?**

### Continuidade contextual

Um conteúdo do Media pode revelar, quando houver relação real, uma continuidade em outra capacidade Guivos.

Exemplos:

- lugar ou experiência → Guivos Travel;
- trajetória, contexto ou próximo passo → Guivos Journey;
- organização, empreendimento ou tema empresarial → Guivos Business;
- produto ou item comercial pertinente → Guivos Mall.

Regra:

```text
CONTEÚDO
↓
CONTEXTO
↓
POSSIBILIDADE
↓
CONTINUAÇÃO PERTINENTE
```

Essa relação não transforma a superfície editorial em vitrine de cross-selling.

## Conteúdo patrocinado e Guivos Ads

Guivos Media pode produzir formatos patrocinados operados e governados em conjunto com as autoridades aplicáveis do Guivos Ads.

Conteúdo patrocinado deve ser identificado e não deve ser apresentado como recomendação editorial orgânica quando sua exposição decorrer de relação comercial.

Separação de responsabilidade:

```text
GUIVOS MEDIA
→ autoridade editorial

GUIVOS ADS
→ publicidade, mídia patrocinada e relação comercial publicitária
```

## Home Pública do Guivos Media

A arquitetura estratégica, narrativa, editorial e funcional da Home Pública do produto é governada por `GKR-UX-HOME-MEDIA-MASTER-001` — **Home Pública — Guivos Media — Documento Mestre**.

A Home v1 é uma superfície pública especializada de descoberta editorial e não redefine nem esgota o escopo integral do Guivos Media descrito neste documento.

Pergunta-mãe:

> **O que você pode descobrir quando vê além do que já conhece?**

Expressão funcional de referência:

> **Veja. Ouça. Leia. Descubra.**

A Home deve privilegiar identidade editorial, curadoria, descoberta e continuidade. Ela não deve ser estruturada prioritariamente como portal de notícias, streaming, Blog, feed social ou catálogo de formatos.

O Documento Mestre serve como autoridade de handoff e não materializa wireframe gráfico, protótipo visual, UI final, frontend, backend ou implementação.

## Limites

Guivos Media não é:

- o ambiente principal da jornada do participante;
- a unidade comercial de produtos;
- a operação de viagens;
- a solução B2B;
- a camada de inteligência;
- a plataforma de publicidade.

## Relações principais

- abastece o Guivos Journey com conteúdo;
- produz materiais e conteúdos que podem apoiar Guivos Travel e Guivos Business;
- pode estabelecer continuidade contextual com Journey, Travel, Business, Mall ou outra capacidade pertinente;
- utiliza Guivos Intelligence para análise editorial, relações semânticas, personalização e distribuição dentro das autoridades aplicáveis;
- pode produzir formatos patrocinados operados pelo Guivos Ads, com identificação e separação de autoridade;
- pode distribuir conteúdo por Guivos Blog, newsletters, redes e plataformas externas;
- possui Home Pública especializada governada por `GKR-UX-HOME-MEDIA-MASTER-001`.

## Decisão de nomenclatura

`Guivos Media` permanece o nome oficial do produto.

`Guivos Podcast` não é produto independente. Como nome próprio, é uma propriedade editorial do Guivos Media.
