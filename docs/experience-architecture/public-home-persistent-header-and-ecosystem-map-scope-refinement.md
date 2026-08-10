---
id: GKR-UX-HOME-NAV-002
title: Refinamento do Header Persistente e Limite do Mapa do Ecossistema na Home Pública
status: draft
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-10
parent: GKR-UX-HOME-NAV-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-VAL-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-004
normative: false
---

# Refinamento do Header Persistente e Limite do Mapa do Ecossistema na Home Pública

## 1. Finalidade

Este documento registra a hipótese principal vigente para a arquitetura de navegação da Home pública de `guivos.com`.

Ele possui quatro funções:

1. consolidar o inventário conceitual do **Header Persistente**;
2. distinguir a porta principal `Iniciar Jornada` do launcher dos demais produtos/serviços;
3. preservar o limite de que o **Mapa do Ecossistema** será apenas um link no rodapé nesta frente;
4. delegar a `GKR-UX-HOME-NAV-004` o comportamento de persistência, compactação, scroll e mobile do Header.

A decisão mais recente deste documento prevalece sobre hipóteses anteriores desta frente quando houver conflito.

---

## 2. Escopo estrito

Este documento governa somente a presença conceitual dos elementos de navegação na **Home pública**.

Ele não cria:

- wireframe;
- layout final de Header;
- layout final de Footer;
- dropdown final;
- mega menu final;
- modal final;
- página `Mapa do Ecossistema`;
- arquitetura de informação da página `Mapa do Ecossistema`;
- conteúdo da página `Mapa do Ecossistema`;
- fluxos internos de Journey, Travel, Mall, Media, Business, Intelligence ou Ads;
- fluxo de login;
- fluxo de `Iniciar Jornada`;
- página de Organizações e Coletivos.

O comportamento conceitual do Header durante scroll e em mobile é tratado separadamente por `GKR-UX-HOME-NAV-004`.

---

## 3. Header Persistente — hipótese principal atual

A hipótese de arquitetura considera no Header Persistente os seguintes elementos:

### Núcleo institucional

- marca / acesso à Home da Guivos;
- `Sobre`;
- acesso dedicado para `Organizações e Coletivos`.

### Núcleo utilitário e de ecossistema

- ícone de compartilhar;
- controle de idioma/região representado conceitualmente pelo ícone de globo;
- launcher do ecossistema representado conceitualmente por uma grade de pontos;
- `Login`;
- CTA de maior hierarquia `Iniciar Jornada`.

A disposição, ordem exata, espaçamento, labels finais e materialização visual permanecem para a futura etapa de design.

A persistência semântica não implica que todos os controles permaneçam simultaneamente visíveis em todas as larguras. A prioridade de exposição e as regras de condensação são governadas por `GKR-UX-HOME-NAV-004`.

---

## 4. Launcher do ecossistema — inventário atual

A grade de pontos é tratada como hipótese forte de acesso rápido aos demais produtos e serviços do ecossistema.

Na decisão atual, ela disponibiliza conceitualmente:

- Guivos Travel;
- Guivos Ads;
- Guivos Media;
- Guivos Business;
- Guivos Intelligence;
- Guivos Mall.

A ordem visual dessa lista ainda não está fechada.

Regra preservada:

> **acessível desde o início ≠ explicado desde o início ≠ protagonista desde o início.**

O launcher permite que quem já conhece um desses destinos o acesse rapidamente, enquanto a Hero e a narrativa continuam apresentando primeiro a Guivos como ideia/ecossistema maior.

O launcher não deve transformar o Header em catálogo visual de produtos.

Em mobile, se houver condensação, o launcher deve preservar sua semântica própria de acesso ao ecossistema e não se tornar indistinguível de um menu geral de navegação.

---

## 5. Journey — porta própria no Header

Na hipótese principal aprovada, **Guivos Journey não integra o launcher de grade de pontos**.

A Journey já possui uma porta de maior hierarquia e semanticamente própria no Header:

> **Iniciar Jornada**

Essa separação possui função estratégica:

- a Pessoa é o participante naturalmente atendido pela Home pública;
- `Iniciar Jornada` representa sua principal continuidade;
- a Journey não precisa disputar espaço dentro do launcher com os demais produtos/serviços;
- evita duplicação de acesso com igual peso no mesmo Header;
- preserva a diferença entre `continuar pela Jornada` e `acessar outro ambiente do ecossistema`.

Journey continua podendo aparecer e ser explicada no Movimento 08 — Ecossistema / Produtos.

Journey também pode possuir outros acessos contextuais quando houver fundamento legítimo.

Formalização:

> **Journey permanece parte do ecossistema, mas sua porta principal no Header é `Iniciar Jornada`, e não o launcher.**

Esta decisão substitui, no limite do Header, hipóteses anteriores de `GKR-UX-HOME-NAV-001` e de versões anteriores deste documento que incluíam Journey no launcher.

---

## 6. Sobre

`Sobre` permanece como acesso institucional de primeiro nível no Header.

Esta frente não detalha a página `Sobre`.

Seu papel na Home é garantir que visitantes com intenção institucional encontrem esse caminho com facilidade.

No mobile, sua presença pode ser condensada na primeira superfície de navegação sem perder encontrabilidade.

---

## 7. Organizações e Coletivos

A hipótese atual é manter **um único acesso de primeiro nível** para `Organizações e Coletivos`.

A Pessoa continua sendo o participante naturalmente atendido pela própria Home pública e pelo CTA `Iniciar Jornada`.

O acesso `Organizações e Coletivos` deverá futuramente conduzir a uma única página capaz de explicar ambos, suas diferenças e suas formas de participação no ecossistema.

A página em si não é objeto desta frente.

No mobile, o acesso pode ser condensado na primeira superfície de navegação, mas não removido ou enterrado em navegação profunda.

---

## 8. Compartilhar

O Header pode conter um ícone utilitário de compartilhamento da Home/Guivos.

A presença conceitual do controle está aceita para exploração futura.

Seu comportamento técnico, canais de compartilhamento, analytics e estados não são definidos aqui.

Compartilhar possui prioridade de exposição inferior à identidade, continuidade, launcher, Login e idioma/região quando a largura exigir condensação.

---

## 9. Idioma e região

O Header pode conter um controle compacto de globo para acesso a uma superfície dedicada de idioma e região.

Princípios:

- idioma e região são preferências distintas;
- idioma governa apresentação linguística;
- região poderá futuramente influenciar disponibilidade pública, contexto operacional e obrigações locais quando houver fundamento real;
- seleção de região não equivale a conhecimento pessoal do visitante;
- o Header não deve listar dezenas de países/idiomas diretamente.

A superfície de seleção permanece para materialização futura.

Em mobile, o globo pode permanecer diretamente visível ou integrar a primeira camada de navegação, mas não deve depender do rodapé para ser encontrado.

---

## 10. Login

`Login` permanece acessível para participantes existentes.

Não deve substituir nem competir hierarquicamente com a mensagem principal da Hero ou com `Iniciar Jornada`.

A presença de `Login` no Header não inicia nesta frente qualquer fluxo autenticado.

Em mobile, pode permanecer diretamente visível ou integrar a primeira superfície de navegação, sempre com alta encontrabilidade.

---

## 11. Iniciar Jornada

`Iniciar Jornada` é a hipótese atual de CTA de maior hierarquia no Header.

Sua função é representar a principal porta de continuidade para a Pessoa e a principal porta de entrada para Guivos Journey a partir do Header público.

Esta decisão não define:

- URL/destino;
- requisitos de autenticação;
- onboarding;
- coleta de contexto;
- personalização;
- fluxo posterior.

Esses elementos permanecem fora do escopo atual.

`GKR-UX-HOME-NAV-004` estabelece que sua disponibilidade deve permanecer estável durante a rolagem sem aumentar progressivamente a pressão perceptiva.

---

## 12. Comportamento persistente — autoridade específica

O significado de `Header Persistente` é aprofundado por:

`GKR-UX-HOME-NAV-004 — Comportamento Persistente do Header — Scroll, Densidade e Mobile na Home Pública`.

Regra central:

> **O Header da Guivos deve permanecer disponível sem permanecer dominante. Ele orienta enquanto a narrativa conduz.**

Consequências principais:

- o Header pode compactar após a Hero;
- não deve desaparecer completamente durante longos trechos como comportamento padrão;
- não muda de arquitetura a cada macroexperiência;
- `Iniciar Jornada` não aumenta pressão durante o scroll;
- mobile preserva a mesma arquitetura de intenção com menor densidade;
- caminhos condensados ficam, em regra, a uma camada de navegação de distância;
- launcher e menu geral não devem perder sua distinção semântica;
- contraste e acessibilidade prevalecem sobre transparência estética.

---

## 13. Mapa do Ecossistema — correção de escopo

A interpretação anterior de que o Footer deveria, nesta frente, ser detalhado como um **mapa completo do ecossistema** com categorias e todos os acessos é substituída pela seguinte decisão:

> **Nesta fase, `Mapa do Ecossistema` será somente um link disponível no rodapé da Home.**

O link poderá futuramente conduzir a uma página própria chamada, provisoriamente ou definitivamente, `Mapa do Ecossistema`.

Nesta frente não serão definidos:

- estrutura da página;
- famílias de links;
- categorias;
- hierarquia de informação;
- todos os produtos e serviços nela listados;
- Trabalhe Conosco dentro dela;
- Central de Ajuda dentro dela;
- Imprensa dentro dela;
- páginas legais dentro dela;
- redes sociais dentro dela;
- países/regiões dentro dela;
- layout;
- navegação interna;
- copy;
- comportamento responsivo.

Essas decisões serão tratadas futuramente quando a página `Mapa do Ecossistema` se tornar uma frente própria.

---

## 14. Efeito sobre GKR-UX-HOME-NAV-001

Este documento refina e prevalece sobre `GKR-UX-HOME-NAV-001` em dois pontos específicos:

1. **launcher** — Journey deixa de integrar o inventário atual do launcher e passa a ter `Iniciar Jornada` como porta principal própria no Header;
2. **Mapa do Ecossistema** — o Footer não é detalhado nesta frente como mapa completo; existe somente o link para futura página.

Em particular, ficam superadas nesta frente as hipóteses de:

- Journey dentro do launcher do Header;
- Footer como inventário completo de Guivos, Ecossistema, Empresa, Suporte, Legal e Presença/Social;
- obrigatoriedade de replicar Trabalhe Conosco, Imprensa, Central de Ajuda ou outros destinos dentro do `Mapa do Ecossistema` já nesta fase;
- necessidade de definir agora a taxonomia interna dessa futura página.

Permanece válido o princípio geral de encontrabilidade dos destinos públicos, mas a solução específica para esses acessos será definida separadamente quando necessário.

---

## 15. Rodapé da Home — limite atual

Para esta frente, a única decisão específica relacionada ao `Mapa do Ecossistema` no rodapé é:

> **deve existir um link para `Mapa do Ecossistema`.**

A composição completa do rodapé além desse ponto não é fechada por este documento.

Isso evita antecipar a arquitetura de uma página que ainda não será trabalhada.

---

## 16. Síntese de controle

Header Persistente — hipótese principal atual:

```text
GUIVOS

Sobre
Organizações e Coletivos

Compartilhar
Idioma / Região (globo)
Ecossistema (grade de pontos)
  → Travel
  → Ads
  → Media
  → Business
  → Intelligence
  → Mall
Login
Iniciar Jornada
  → porta própria da Journey
```

Comportamento:

```text
Hero
→ Header presente e visualmente secundário
→ scroll
→ Header pode compactar
→ permanece previsível durante a narrativa
→ mobile condensa sem mudar a arquitetura de intenção
```

Rodapé — decisão atual sobre o mapa:

```text
Mapa do Ecossistema → link
```

Regra final:

> **A Home deve oferecer caminhos essenciais sem tentar resolver agora a arquitetura de todas as páginas que esses caminhos poderão abrir no futuro.**
