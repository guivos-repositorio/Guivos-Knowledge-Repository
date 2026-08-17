---
id: GKR-UX-HOME-MEDIA-MASTER-001
title: Home Pública — Guivos Media — Documento Mestre
status: draft
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-13
parents:
  - GKR-UX-HOME-MASTER-001
  - GPA-005
  - GKR-STATE-001
related:
  - GPA-001
  - GPA-003
  - GPA-004
  - GPA-005
  - GPA-006
  - GPA-007
---

# Home Pública — Guivos Media — Documento Mestre

## 1. Finalidade e autoridade

Este documento governa exclusivamente a **Home Pública do Guivos Media — v1** e é a referência de handoff para Design, UX, UI, Content Design e implementação futura.

A Home possui expressão editorial própria e não deve ser tratada como adaptação de outra Home Guivos.

> **A Home v1 não redefine nem esgota o escopo integral do Guivos Media estabelecido em `GPA-005`.**

Este documento não contém protótipo visual nem UI final.

## 2. Tese, papel e percepção

Guivos Media pertence à **Service Layer**. Sua Home v1 é uma superfície pública de descoberta editorial.

> **Guivos Media transforma histórias, ideias, experiências e conhecimento em conteúdos que ajudam a tornar novas perspectivas visíveis.**

A Home combina `identidade editorial + curadoria + descoberta + continuidade` e deve fazer a pessoa perceber que existe algo além daquilo que já conhece, que outras perspectivas podem ser encontradas e que uma descoberta pode levar a outra.

Ela não deve funcionar primordialmente como portal de notícias, streaming, Blog, feed, catálogo ou vitrine dos demais produtos.

## 3. Pergunta-mãe e expressão funcional

Pergunta-mãe:

# O que você pode descobrir quando vê além do que já conhece?

Expressão de referência:

# Veja. Ouça. Leia. Descubra.

Os quatro verbos são formas de descoberta, não produtos ou departamentos.

Princípios permanentes:

- significado antes de quantidade;
- curadoria antes de cronologia;
- conteúdo antes de formato;
- descoberta antes de classificação;
- pessoa antes de metadados;
- pergunta antes de autoridade quando o objetivo for compreender;
- contexto antes de promoção;
- **complexidade no sistema; simplicidade na experiência**.

## 4. Arquitetura narrativa — 11 movimentos

Os movimentos governam a progressão narrativa, mas **não obrigam onze seções visuais independentes**.

### 01 — Abrir uma nova perspectiva

Hero governado pela pergunta-mãe. Ação de referência: **Descobrir**. Não iniciar por cards, catálogo, episódio, campanha ou lista de formatos.

### 02 — Dar significado

Direção: **Há sempre outra forma de ver.** Explica por que o Media existe sem manifesto institucional longo.

### 03 — Tornar a tese concreta

Uma história, experiência, entrevista, documentário ou produção especial comprova a promessa. Um conteúdo deve receber hierarquia dominante.

### 04 — Oferecer maneiras de descobrir

**Veja. Ouça. Leia. Descubra.** Entrega controle sem expor taxonomia interna.

### 05 — Demonstrar o pulso editorial

Direção: **Vale descobrir agora.** Um destaque dominante + seleção reduzida. Priorizar relevância, qualidade, perspectiva, diversidade e atualidade. Não é feed cronológico.

### 06 — Aproximar das pessoas

Direção: **Existem histórias que merecem atravessar fronteiras.** Unidade: `pessoa + experiência + significado`. Não reduzir a histórias motivacionais ou foto + cargo.

### 07 — Aprofundar a compreensão

Direção: **Descobrir também é entender.** Pode abordar ciência, tecnologia, cultura, sociedade, criatividade, negócios e futuro. A pergunta ou ideia vem antes do especialista.

### 08 — Ampliar o universo

Direção: **O mundo é maior quando diferentes perspectivas se encontram.** Territórios iniciais: Pessoas, Lugares, Ideias, Tecnologia, Criatividade, Sociedade, Negócios e Futuro. São caminhos de descoberta, não departamentos rígidos.

### 09 — Criar recorrência

Direção: **Algumas histórias não terminam em um único conteúdo.** Abriga propriedades editoriais como Guivos Podcast, séries, temporadas, newsletters e projetos recorrentes. Guivos Podcast permanece propriedade do Media, não produto independente.

### 10 — Permitir continuidade pelo ecossistema

Direção: **Uma descoberta pode levar a outra.**

```text
conteúdo → contexto → possibilidade → continuação pertinente
```

Pode levar a Journey, Travel, Business, Mall ou outra capacidade pertinente. Nunca inverter para produto → promoção → conteúdo. Se não houver relação genuína, o movimento pode ser omitido.

### 11 — Reabrir a descoberta

Direção: **Há sempre algo além do que você já conhece.** Ação de referência: **Continue descobrindo**.

## 5. Arquitetura editorial e descoberta

A entidade central é **Conteúdo**, que pode relacionar-se a assuntos, perspectivas, pessoas, lugares, propriedades e outros conteúdos.

Níveis editoriais devem permanecer distintos conforme `GPA-005`: produto, propriedade editorial, tipo editorial e formato de expressão.

A experiência deve suportar:

```text
Descobrir → Explorar → Consumir → Continuar
```

Modos de descoberta: curadoria, interesse, contexto e continuidade.

A navegação visível deve ser muito mais simples que a taxonomia interna. Busca é complementar à curadoria. `Descobrir`, `Veja`, `Ouça` e `Leia` são hipóteses, não menu final obrigatório.

## 6. Media, Blog e ecossistema

`Guivos Media ≠ Guivos Blog`.

Media é produto editorial multimídia e semântico da Service Layer. Blog é canal/destino editorial predominantemente textual. Nem todo conteúdo do Blog precisa nascer no Media e nem toda produção do Media precisa ir ao Blog.

Distribuição e continuidade são relações diferentes:

```text
DISTRIBUIÇÃO
→ Media / Blog / newsletter / redes / plataformas externas

CONTINUIDADE
→ Journey / Travel / Business / Mall / outra capacidade pertinente
```

Conteúdo patrocinado pode existir conforme as autoridades de Media e Ads, deve ser identificado e não constitui seção obrigatória da Home.

## 7. Estados editoriais

A Home deve funcionar em três maturidades:

- **Inicial:** pouco conteúdo, ainda intencional e completa;
- **Crescimento:** formatos e propriedades ganham densidade;
- **Madura:** grande acervo sem perder curadoria e hierarquia.

> **Nunca produzir conteúdo artificial apenas para preencher interface.**

## 8. Guardrails para Design, UX e UI

Preservar hierarquia editorial, significado antes de volume, mídia com propósito, variação de escala e densidade, pessoas em contexto, tipografia como parte da narrativa, metadados secundários e identidade Guivos com expressão própria do Media.

**Card é componente, não arquitetura.** Evitar cardificação e grids uniformes como linguagem dominante.

Princípio responsivo: **preservar hierarquia e significado, não geometria**. Mobile não é desktop simplesmente empilhado.

Acessibilidade e performance são requisitos desde a concepção, incluindo contraste, teclado, foco, alternativas textuais, legendas/transcrições quando aplicáveis, redução de movimento, mídia responsiva e carregamento progressivo.

## 9. Não escopo e modelos rejeitados

Não são especificados aqui: cadastro, login, perfil, pagamentos, gamificação, comunidade, comentários, CMS, algoritmo final de recomendação, personalização avançada, páginas internas completas, wireframe gráfico, protótipo visual, frontend ou backend.

A solução deve ser revista se parecer predominantemente portal de notícias, streaming, Blog, feed social, dashboard, landing page SaaS, catálogo de formatos ou cópia de outra Home Guivos; se todos os conteúdos tiverem o mesmo peso; se Podcast virar produto independente; se Blog virar a “área de artigos do Media”; ou se produtos forem promovidos sem contexto.

## 10. Liberdade e critérios de aceite

Design, UX e UI podem definir composição, grid, dobras, agrupamento dos movimentos, tipografia, fotografia, vídeo, paleta, motion, componentes, menu, busca, microinterações e breakpoints.

O documento define **o que a experiência precisa significar, fazer e preservar**; a equipe define **como materializar**.

A solução deve:

1. ser inequivocamente Guivos Media;
2. preservar descoberta como conceito central;
3. comunicar significado antes de volume;
4. preservar os 11 movimentos sem exigir 11 blocos;
5. funcionar com pouco ou muito conteúdo;
6. manter Guivos Podcast como propriedade editorial;
7. não confundir Media e Blog;
8. integrar produtos apenas contextualmente;
9. separar distribuição de continuidade;
10. atender desktop, mobile, acessibilidade e performance;
11. possuir personalidade própria sem romper os fundamentos Guivos;
12. permitir evolução editorial sem reconstruir a tese.

## 11. Síntese canônica

A Home v1 do Guivos Media existe para **tornar algo digno de descoberta visível**.

```text
PROVOCAR → DAR SIGNIFICADO → MOSTRAR → PERMITIR ESCOLHER → CURAR
→ APROXIMAR → APROFUNDAR → EXPANDIR → CRIAR RECORRÊNCIA
→ CONECTAR → REABRIR A DESCOBERTA
```

> **O que você pode descobrir quando vê além do que já conhece?**

Estado:

> **ARQUITETURA CONCEITUAL E FUNCIONAL DA HOME V1 CONVERGIDA — DOCUMENTO PREPARADO PARA HANDOFF; PROTÓTIPO VISUAL NÃO INCLUÍDO NESTE ESCOPO.**
