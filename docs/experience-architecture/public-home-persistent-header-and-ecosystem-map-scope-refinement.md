---
id: GKR-UX-HOME-NAV-002
title: Refinamento do Header Persistente e Limite do Mapa do Ecossistema na Home Pública
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: GKR-UX-HOME-NAV-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-VAL-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NAV-001
normative: false
---

# Refinamento do Header Persistente e Limite do Mapa do Ecossistema na Home Pública

## 1. Finalidade

Este documento registra um refinamento posterior de escopo da arquitetura de navegação da Home pública de `guivos.com`.

Ele possui duas funções:

1. consolidar a hipótese principal atual para o **Header Persistente** da Home;
2. corrigir a interpretação anterior de que o **Mapa do Ecossistema** deveria ser detalhado nesta frente.

A decisão mais recente prevalece sobre hipóteses anteriores desta frente quando houver conflito.

---

## 2. Escopo estrito

Este documento governa somente a presença conceitual de elementos de navegação na **Home pública**.

Ele não cria:

- wireframe;
- layout de Header;
- layout de Footer;
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

---

## 3. Header Persistente — hipótese principal atual

A hipótese de arquitetura passa a considerar no Header Persistente os seguintes elementos:

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

A disposição, ordem exata, espaçamento, labels finais e comportamento responsivo permanecem abertos para a futura etapa de design.

---

## 4. Launcher do ecossistema

A grade de pontos é tratada como hipótese forte de acesso rápido ao ecossistema.

Ela pode disponibilizar diretamente:

- Guivos Journey;
- Guivos Travel;
- Guivos Mall;
- Guivos Media;
- Guivos Business;
- Guivos Intelligence;
- Guivos Ads.

Regra preservada:

> **acessível desde o início ≠ explicado desde o início ≠ protagonista desde o início.**

O launcher permite que quem já conhece um produto o acesse rapidamente, enquanto a Hero e a narrativa continuam apresentando primeiro a Guivos como ideia/ecossistema maior.

O launcher não deve transformar o Header em catálogo visual de produtos.

---

## 5. Sobre

`Sobre` permanece como acesso institucional de primeiro nível no Header.

Esta frente não detalha a página `Sobre`.

Seu papel na Home é apenas garantir que visitantes com intenção institucional encontrem esse caminho com facilidade.

---

## 6. Organizações e Coletivos

A hipótese atual é manter **um único acesso de primeiro nível** no Header para `Organizações e Coletivos`.

A Pessoa continua sendo o participante naturalmente atendido pela própria Home pública e pelo CTA `Iniciar Jornada`.

O acesso `Organizações e Coletivos` deve futuramente conduzir a uma única página capaz de:

- explicar o que é uma Organização no ecossistema Guivos;
- explicar o que é um Coletivo;
- mostrar suas diferenças;
- mostrar o que compartilham como participantes capazes de criar, articular ou ampliar possibilidades.

A página em si não é objeto desta frente.

---

## 7. Compartilhar

O Header pode conter um ícone utilitário de compartilhamento da Home/Guivos.

A presença conceitual do controle está aceita para exploração futura.

Seu comportamento técnico, canais de compartilhamento, analytics e estados não são definidos aqui.

---

## 8. Idioma e região

O Header pode conter um controle compacto de globo para acesso a uma superfície dedicada de idioma e região.

Princípios:

- idioma e região são preferências distintas;
- idioma governa apresentação linguística;
- região poderá futuramente influenciar disponibilidade pública, contexto operacional e obrigações locais quando houver fundamento real;
- seleção de região não equivale a conhecimento pessoal do visitante;
- o Header não deve listar dezenas de países/idiomas diretamente.

A superfície de seleção permanece para materialização futura.

---

## 9. Login

`Login` permanece acessível para participantes existentes.

Não deve substituir nem competir hierarquicamente com a mensagem principal da Hero.

A presença de `Login` no Header não inicia nesta frente qualquer fluxo autenticado.

---

## 10. Iniciar Jornada

`Iniciar Jornada` é a hipótese atual de CTA de maior hierarquia no Header.

Sua função é representar a principal porta de continuidade para a Pessoa.

Esta decisão não define ainda:

- copy final;
- URL/destino;
- requisitos de autenticação;
- onboarding;
- coleta de contexto;
- personalização;
- fluxo posterior.

Esses elementos permanecem fora do escopo atual.

---

## 11. Mapa do Ecossistema — correção de escopo

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

## 12. Efeito sobre GKR-UX-HOME-NAV-001

Este documento refina e prevalece sobre `GKR-UX-HOME-NAV-001` especificamente nos trechos que tratavam o Footer como mapa completo ou que propunham uma arquitetura detalhada do `Mapa do Ecossistema`.

Em particular, ficam superadas nesta frente as hipóteses de:

- Footer como inventário completo de Guivos, Ecossistema, Empresa, Suporte, Legal e Presença/Social;
- obrigatoriedade de replicar Trabalhe Conosco, Imprensa, Central de Ajuda ou outros destinos dentro do `Mapa do Ecossistema` já nesta fase;
- necessidade de definir agora a taxonomia interna dessa futura página.

Permanece válido o princípio geral de encontrabilidade dos destinos públicos, mas a solução específica para esses acessos será definida separadamente quando necessário.

---

## 13. Rodapé da Home — limite atual

Para esta frente, a única decisão específica relacionada ao `Mapa do Ecossistema` no rodapé é:

> **deve existir um link para `Mapa do Ecossistema`.**

A composição completa do rodapé além desse ponto não é fechada por este documento.

Isso evita antecipar a arquitetura de uma página que ainda não será trabalhada.

---

## 14. Síntese de controle

Header Persistente — hipótese principal atual:

```text
GUIVOS

Sobre
Organizações e Coletivos

Compartilhar
Idioma / Região (globo)
Ecossistema (grade de pontos)
Login
Iniciar Jornada
```

Rodapé — decisão atual sobre o mapa:

```text
Mapa do Ecossistema → link
```

Regra final:

> **A Home deve oferecer caminhos essenciais sem tentar resolver agora a arquitetura de todas as páginas que esses caminhos poderão abrir no futuro.**
