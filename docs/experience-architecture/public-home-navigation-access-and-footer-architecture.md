---
id: GKR-UX-HOME-NAV-001
title: Arquitetura de Navegação e Acessos da Home Pública
status: draft
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: GKR-UX-HOME-HANDOFF-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-001
  - GKR-UX-HOME-VAL-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GEB-P01-F01
  - GEB-P01-F02
  - GEB-P01-F03
  - GEB-P01-F04
  - GEB-P01-F06
related:
  - GKR-UX-HOME-NAV-002
normative: false
---

# Arquitetura de Navegação e Acessos da Home Pública

## 1. Finalidade

Este documento define a arquitetura conceitual de navegação e acesso da Home pública de `guivos.com`.

Ele esclarece como produtos, páginas institucionais, áreas utilitárias e caminhos de continuidade podem permanecer acessíveis sem transformar a Home em catálogo, portal corporativo ou inventário de links.

A decisão central é:

> **disponibilidade de navegação não implica protagonismo narrativo.**

Um produto pode estar acessível desde o primeiro viewport e ainda assim somente receber explicação e destaque institucional quando a narrativa tiver construído contexto suficiente.

Este documento não define layout, wireframe, Figma, comportamento visual final de menus, nem fluxos internos dos destinos.

---

## 2. Escopo estrito

Esta especificação governa somente os elementos de navegação e acesso relacionados à Home pública.

Pode definir acesso para:

- Guivos Journey, por sua porta própria `Iniciar Jornada`;
- Guivos Travel;
- Guivos Mall;
- Guivos Media;
- Guivos Business;
- Guivos Intelligence;
- Guivos Ads;
- futuras manifestações oficialmente integradas ao ecossistema;
- Sobre a Guivos;
- Organizações e Coletivos;
- idioma e região;
- compartilhamento;
- login;
- link `Mapa do Ecossistema` no rodapé.

Esta especificação não governa os fluxos internos desses destinos.

A existência de um link para Travel não inicia UX de Travel.

A existência de login não inicia a experiência autenticada.

A existência do link `Mapa do Ecossistema` não inicia nem governa essa futura página.

---

## 3. Dois sistemas coexistentes

A Home possui dois sistemas diferentes e complementares.

### 3.1 Sistema narrativo

Responde progressivamente à pergunta-mãe da Home por meio dos onze movimentos definidos em `GKR-UX-HOME-NARR-001`.

Sua função é fazer o visitante compreender a Guivos.

### 3.2 Sistema de navegação

Permite que visitantes com intenção já formada encontrem diretamente um destino sem precisar percorrer toda a narrativa.

Sua função é orientar e permitir acesso.

Regra:

> **a narrativa governa significado; a navegação garante liberdade.**

---

## 4. Camadas de acesso da Home

A arquitetura conceitual deve admitir quatro formas de acesso.

### 4.1 Header Persistente

Função:

- orientação imediata;
- acesso direto a destinos essenciais;
- entrada de participantes existentes;
- acesso ao launcher do ecossistema;
- continuidade pela Jornada.

Hipótese principal atual, refinada em `GKR-UX-HOME-NAV-002`:

- marca / acesso à Home;
- `Sobre`;
- `Organizações e Coletivos`;
- compartilhar;
- idioma/região por controle de globo;
- launcher do ecossistema por grade de pontos;
- `Login`;
- `Iniciar Jornada` como CTA de maior hierarquia e porta própria da Journey.

A ordem final, layout, comportamento responsivo e labels ainda podem ser refinados.

### 4.2 Acesso contextual ao longo da narrativa

Função:

- transformar conteúdo em continuidade;
- permitir que uma história, oportunidade ou experiência leve naturalmente ao produto ou ambiente correspondente;
- evitar CTAs genéricos.

Regra:

> **produto pode aparecer cedo como destino contextual sem precisar aparecer cedo como categoria dominante.**

### 4.3 Movimento 08 — Ecossistema / Produtos

Função:

- apresentar explicitamente a arquitetura de produtos;
- explicar por que existem diferentes manifestações;
- mostrar como pertencem à mesma tese;
- permitir acesso direto a cada uma.

É o principal momento de protagonismo institucional dos produtos dentro da narrativa.

### 4.4 Rodapé

Nesta frente, o rodapé não é detalhado como mapa completo.

A única decisão específica relativa ao `Mapa do Ecossistema` é:

> **deve existir no rodapé um link chamado `Mapa do Ecossistema` ou equivalente validado posteriormente.**

A página que esse link poderá abrir não é definida nesta frente.

---

## 5. Header Persistente — princípio geral

O Header deve equilibrar simplicidade e acessibilidade.

Ele não deve tentar representar toda a estrutura da Guivos em uma única linha.

A hipótese principal atual é:

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

Essa representação é semântica, não layout final.

---

## 6. Launcher do Ecossistema

O launcher do ecossistema é uma porta compacta para os demais produtos e serviços que precisam de acesso rápido sem ocupar individualmente o Header.

A grade de pontos é a hipótese visual atualmente preferida para representá-lo.

Objetivos:

- permitir acesso rápido a quem já conhece um produto;
- preservar uma primeira camada simples;
- impedir que a Guivos pareça conglomerado de marcas independentes;
- permitir expansão futura sem aumentar indefinidamente a navegação primária.

Regra:

> **acessível desde o início ≠ explicado desde o início ≠ protagonista desde o início.**

---

## 7. Produtos no launcher

O inventário conceitualmente aprovado do launcher nesta fase é:

- Guivos Travel;
- Guivos Ads;
- Guivos Media;
- Guivos Business;
- Guivos Intelligence;
- Guivos Mall.

A ordem visual ainda não está fechada e a disponibilidade operacional de cada destino precisa ser confirmada antes do wireframe.

**Guivos Journey não integra o launcher na hipótese principal atual.**

Journey permanece parte do ecossistema, aparece no Movimento 08 e pode possuir acessos contextuais, mas sua porta principal no Header é `Iniciar Jornada`.

Regra:

> **Journey pertence ao ecossistema; `Iniciar Jornada` é sua porta própria no Header.**

O launcher não deve virar catálogo promocional.

---

## 8. Acessos contextuais aos produtos

A Home pode apontar para produtos antes do Movimento 08 quando o acesso nasce naturalmente do conteúdo.

Critérios:

1. existe contexto suficiente;
2. o destino é coerente com o que a pessoa acabou de ver;
3. o CTA não interrompe a narrativa principal;
4. o produto é destino, não explicação da marca;
5. o acesso não cria falsa disponibilidade;
6. o destino operacional existe ou possui estado público legítimo.

---

## 9. Movimento 08 como apresentação institucional do ecossistema

O Movimento 08 possui a função principal de apresentar os produtos de forma estruturada.

Mensagem conceitual:

> **um ecossistema, diferentes formas de tornar possibilidades acessíveis, conectadas e vivíveis.**

Cada produto deve ser apresentado como manifestação da mesma tese, não como negócio independente.

Journey pode aparecer aqui junto às demais manifestações mesmo não integrando o launcher do Header.

O requisito é:

> **a coerência entre os produtos deve ser mais perceptível que a quantidade de produtos.**

---

## 10. Sobre

`Sobre` permanece como acesso institucional de primeiro nível no Header.

A página `Sobre` não é detalhada nesta frente.

Seu papel aqui é apenas garantir encontrabilidade para quem quer compreender a organização, sua essência e sua visão.

---

## 11. Organizações e Coletivos

A hipótese atual é manter um único acesso de primeiro nível chamado `Organizações e Coletivos`.

A Pessoa continua sendo o participante naturalmente atendido pela própria Home e pelo CTA `Iniciar Jornada`.

A futura página `Organizações e Coletivos` deverá explicar a diferença entre ambos e suas formas de participação no ecossistema, mas essa página não é objeto desta frente.

---

## 12. Compartilhar

O Header pode conter um ícone utilitário de compartilhamento da Home/Guivos.

A presença conceitual está aceita para futura materialização.

Comportamento técnico e canais de compartilhamento permanecem abertos.

---

## 13. Idioma e região

O Header pode conter um controle compacto de globo para abrir uma superfície dedicada de idioma e região.

Princípios:

- idioma e região são preferências distintas;
- idioma governa apresentação linguística;
- região poderá influenciar disponibilidade pública e contexto operacional quando houver fundamento real;
- região selecionada não equivale a conhecimento pessoal do visitante;
- o Header não deve listar diretamente dezenas de países ou idiomas.

---

## 14. Login

O acesso para participantes existentes deve permanecer facilmente encontrável.

Regra:

> **usuário existente precisa acessar; visitante novo precisa compreender.**

`Login` não deve se tornar o CTA narrativo dominante.

---

## 15. Iniciar Jornada

`Iniciar Jornada` é a hipótese atual de CTA de maior hierarquia no Header.

Sua função é representar a principal porta de continuidade para a Pessoa e a porta própria de entrada para Guivos Journey a partir do Header público.

Esta frente não define o fluxo posterior, autenticação, onboarding, personalização ou coleta de contexto.

---

## 16. Mapa do Ecossistema — limite atual

`Mapa do Ecossistema` não é uma seção detalhada do rodapé nem uma página a ser especificada agora.

A decisão vigente é:

> **nesta fase, será apenas um link no rodapé.**

A futura página permanece fora do escopo.

Não são definidos agora:

- arquitetura da página;
- grupos de links;
- conteúdo;
- categorias;
- produtos e serviços nela listados;
- Trabalhe Conosco;
- Central de Ajuda;
- Imprensa;
- páginas legais;
- redes sociais;
- países/regiões;
- layout;
- navegação interna.

Esses temas serão tratados futuramente em frente própria.

---

## 17. Relação com GKR-UX-HOME-NAV-002

`GKR-UX-HOME-NAV-002` registra a decisão de refinamento que originou esta versão 0.3.0.

Em caso de conflito com hipóteses históricas anteriores, prevalecem:

1. Journey fora do launcher e `Iniciar Jornada` como sua porta própria no Header;
2. launcher composto por Travel, Ads, Media, Business, Intelligence e Mall;
3. o limite de que `Mapa do Ecossistema` é somente um link no rodapé nesta fase;
4. a postergação integral da página `Mapa do Ecossistema`.

---

## 18. Desktop e mobile

A hierarquia semântica deve ser equivalente em desktop e mobile.

O mobile pode usar drawer, grupos progressivos ou outra solução apropriada.

Não deve:

- esconder produtos essenciais;
- eliminar `Sobre` ou `Organizações e Coletivos` sem solução equivalente;
- remover idioma/região;
- tornar `Login` ou `Iniciar Jornada` difíceis de encontrar;
- depender de hover.

---

## 19. Acessibilidade

A futura materialização deve assegurar:

- navegação por teclado;
- foco visível;
- labels compreensíveis;
- compatibilidade com leitor de tela;
- estado expandido/recolhido anunciado;
- ordem lógica;
- alvo de toque adequado;
- ausência de dependência exclusiva de hover;
- retorno de foco adequado.

---

## 20. Comportamento do Header

Este documento chama o componente de **Header Persistente** como função de navegação contínua, mas ainda não fixa mecanismo visual específico.

Qualquer solução futura deve preservar:

- acesso previsível;
- legibilidade;
- baixo ruído;
- autonomia;
- ausência de mudança inesperada;
- acesso ao ecossistema sem bloquear conteúdo.

---

## 21. CTA da Hero versus Header

A navegação e os CTAs da Hero possuem funções diferentes.

O Header atende intenção existente.

A Hero cria continuidade narrativa.

`Iniciar Jornada` no Header não elimina a necessidade de avaliar separadamente o CTA da própria Hero.

---

## 22. Relação com Pessoas, Organizações e Coletivos

A arquitetura preserva uma única Home e uma única tese.

A Pessoa é atendida prioritariamente pela Home e pela Jornada.

Organizações e Coletivos recebem uma porta de aprofundamento dedicada.

Regra:

> **uma Home, uma tese, múltiplas formas de participação.**

---

## 23. Internacionalização

A arquitetura deve tolerar:

- nomes maiores em outros idiomas;
- expansão de labels;
- diferentes convenções de navegação;
- diferenças regulatórias por país;
- páginas legais locais;
- região diferente do idioma escolhido.

---

## 24. Anti-padrões

Rejeitar ou revisar uma proposta quando:

1. todos os produtos ocupam individualmente o Header;
2. o Header parece menu de conglomerado;
3. o visitante precisa rolar para acessar um produto que já conhece;
4. o launcher vira catálogo promocional;
5. Journey é duplicada no launcher sem nova decisão explícita;
6. `Sobre` fica escondido;
7. `Organizações e Coletivos` perde encontrabilidade sem alternativa equivalente;
8. login vira CTA principal da experiência;
9. `Iniciar Jornada` é tratado como autorização para desenhar onboarding nesta frente;
10. idioma e região são confundidos como uma única preferência;
11. o `Mapa do Ecossistema` é detalhado ou desenhado antes da frente própria;
12. mobile perde caminhos disponíveis no desktop;
13. navegação depende de hover;
14. o Header se torna mais importante que a Hero.

---

## 25. Critérios de aceitação

Uma futura arquitetura será considerada aderente quando:

- os produtos do launcher forem acessíveis sem dominar a primeira percepção;
- Journey possuir `Iniciar Jornada` como porta própria no Header;
- o launcher representar os demais ambientes de forma compacta;
- a marca permanecer maior que a soma dos produtos;
- `Sobre` for facilmente encontrável;
- `Organizações e Coletivos` possuir porta clara;
- idioma/região estiver disponível sem poluir o Header;
- compartilhar permanecer utilitário;
- login estiver disponível sem disputar a narrativa;
- `Iniciar Jornada` possuir hierarquia adequada;
- o rodapé contiver o link `Mapa do Ecossistema` sem antecipar a página;
- desktop e mobile preservarem hierarquia;
- nenhuma área pública simular disponibilidade inexistente.

---

## 26. Perguntas obrigatórias de revisão

Antes de aprovar um futuro Header, responder:

1. Quem já conhece Travel consegue acessá-lo rapidamente?
2. Quem quer iniciar sua Journey encontra `Iniciar Jornada` imediatamente?
3. Quem nunca ouviu falar de Guivos entende a marca antes de ser bombardeado por produtos?
4. O launcher parece pertencer a um único ecossistema?
5. Journey está corretamente separada do launcher?
6. `Sobre` está encontrável?
7. `Organizações e Coletivos` está encontrável?
8. idioma/região está acessível?
9. compartilhar está presente sem competir com a narrativa?
10. login está claro sem dominar?
11. `Iniciar Jornada` é a ação de maior hierarquia no Header?
12. mobile preserva os mesmos caminhos essenciais?
13. algum elemento existe apenas porque concorrentes usam?
14. o `Mapa do Ecossistema` foi mantido somente como link, sem detalhamento prematuro?

---

## 27. Prompt para futura arquitetura de informação

```text
Projete a arquitetura de navegação da Home pública de Guivos.com sem desenhar ainda a interface final.

Princípio obrigatório: disponibilidade de navegação não implica protagonismo narrativo.

Considere como hipótese principal de Header Persistente:
- marca Guivos;
- Sobre;
- Organizações e Coletivos;
- compartilhar;
- idioma/região por ícone de globo;
- launcher do ecossistema por grade de pontos;
- Login;
- Iniciar Jornada como CTA de maior hierarquia e porta própria da Journey.

O launcher deve permitir acesso a Travel, Ads, Media, Business, Intelligence e Mall sem transformar o Header em catálogo. Journey pertence ao ecossistema, mas não integra o launcher nesta hipótese; sua porta principal no Header é Iniciar Jornada.

A Home precisa permitir acesso imediato a produtos conhecidos, mas os produtos não podem dominar a primeira percepção da marca.

No rodapé, considere apenas um link Mapa do Ecossistema. Não desenhe nem detalhe a página de destino; ela pertence a frente futura.

Preserve a mesma hierarquia semântica em desktop e mobile.

Entregue:
- taxonomia proposta;
- racional de cada item;
- comportamento conceitual do launcher;
- relação entre Header e Hero;
- diferenças desktop/mobile;
- riscos;
- itens ainda abertos para teste.
```

---

## 28. Síntese de controle

A arquitetura deve permitir simultaneamente:

> **quem não conhece a Guivos, compreender; quem já conhece Travel, Ads, Media, Business, Intelligence ou Mall, acessar; quem quer saber quem é a Guivos, encontrar Sobre; quem representa Organização ou Coletivo, encontrar sua porta; quem já participa, fazer login; e quem quer avançar como Pessoa, iniciar sua Jornada.**

Sem transformar a Home em inventário.

Regra final:

> **a Home conta uma história enquanto a navegação preserva liberdade.**