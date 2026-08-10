---
id: GKR-UX-HOME-NARR-003
title: Refinamento da Transição Movimento 07 → 08 — Participantes e Produtos na Home Pública
status: draft
version: 0.1.1
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-10
parent: GKR-UX-HOME-NARR-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NARR-002
  - GKR-UX-HOME-NAV-002
  - GKR-UX-HOME-NAV-003
  - GLPA-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GKR-UX-HOME-GTM-BOUNDARY-001
normative: false
---

# Refinamento da Transição Movimento 07 → 08 — Participantes e Produtos na Home Pública

## 1. Finalidade

Este documento refina a passagem narrativa entre:

- `Movimento 07 — Pertencimento`; e
- `Movimento 08 — Ecossistema / Produtos`.

O objetivo é impedir que a Home pública crie uma associação equivocada de correspondência direta entre tipos de participante e produtos da Guivos.

A transição deve fazer o visitante compreender primeiro **quem participa do ecossistema** e somente depois **como a Guivos materializa capacidades diferentes dentro desse mesmo ecossistema**.

Este documento não cria wireframe, layout, página de participante, fluxo de produto, disponibilidade operacional, Marketing/GTM ou implementação.

---

## 2. Problema de interpretação a evitar

A proximidade entre o Movimento 07 e o Movimento 08 pode induzir uma leitura falsa como:

```text
Pessoa → Journey
Organização → Business
Coletivo → algum produto específico
```

Essa leitura é incorreta.

A arquitetura vigente distingue explicitamente:

```text
Pessoa / Organização / Coletivo
= tipos estruturais de participante

Journey / Travel / Mall / Media / Business / Intelligence / Ads
= produtos, manifestações ou capacidades do ecossistema
```

Consequentemente:

> **participante ≠ produto**

---

## 3. Decisão central

A passagem 07 → 08 deve preservar duas dimensões diferentes.

### Dimensão 1 — quem faz o ecossistema acontecer

- Pessoas;
- Organizações;
- Coletivos.

Essa é a resposta do Movimento 07.

### Dimensão 2 — como a Guivos dá forma, continuidade e capacidade a esse ecossistema

- Journey;
- Travel;
- Mall;
- Media;
- Business;
- Intelligence;
- Ads.

Essa é a resposta aprofundada pelo Movimento 08.

Regra sintética:

> **Participantes respondem “quem”. Produtos e capacidades respondem “como”.**

A formulação é regra interna de arquitetura narrativa e não copy pública obrigatória.

---

## 4. Relação entre as duas dimensões

As dimensões são relacionadas, mas não possuem correspondência 1:1.

Um mesmo participante pode, conforme contexto e autoridade aplicável, relacionar-se com diferentes manifestações do ecossistema.

Isso significa conceitualmente:

- uma Pessoa não é definida por Journey;
- uma Organização não é definida por Guivos Business;
- um Coletivo não precisa de um produto homônimo para possuir papel estrutural;
- Journey pode organizar experiências sem representar um “tipo Pessoa”;
- Travel, Mall, Media, Business, Intelligence e Ads não criam novos tipos de participante;
- produtos existem para materializar capacidades, não para classificar pessoas ou instituições.

---

## 5. Estado perceptivo no fim do Movimento 07

Ao sair do Movimento 07, o visitante deve compreender algo próximo de:

> **“A Guivos não é apenas uma plataforma me oferecendo coisas. Pessoas, Organizações e Coletivos também descobrem, criam, conectam, compartilham e tornam possibilidades possíveis.”**

A percepção principal é pertencimento e reciprocidade.

O visitante ainda não precisa conhecer a arquitetura de produtos.

---

## 6. Pergunta de transição correta

A pergunta que abre naturalmente o Movimento 08 permanece:

> **“Como a Guivos organiza e materializa tudo isso?”**

Mas sua interpretação deve ser explícita internamente:

> **“Se existem diferentes participantes criando e vivendo possibilidades, como uma única Guivos oferece experiências, serviços e inteligência capazes de dar forma a esse universo sem separar cada participante em um produto?”**

A segunda formulação é explicativa e não copy pública obrigatória.

---

## 7. Ponte narrativa recomendada

A transição deve seguir esta lógica:

```text
PESSOAS + ORGANIZAÇÕES + COLETIVOS
fazem o ecossistema acontecer

↓

possibilidades podem ser descobertas, criadas, compartilhadas e vividas de muitas formas

↓

nenhum participante é reduzido a um único produto

↓

para dar forma a essa diversidade, a Guivos se materializa em capacidades e ambientes diferentes

↓

MOVIMENTO 08 — uma Guivos, diferentes formas de materialização
```

A experiência futura não precisa exibir esse fluxo literalmente.

Ela precisa preservar o raciocínio.

---

## 8. Territórios de linguagem pública

A futura copy poderá explorar ideias equivalentes a:

- `Um ecossistema feito por diferentes participantes e vivido de diferentes formas.`;
- `Quem participa pode descobrir, criar, conectar e viver possibilidades por caminhos diferentes.`;
- `Uma mesma Guivos pode ganhar formas diferentes conforme o contexto.`;
- `Diferentes possibilidades pedem diferentes formas de acontecer.`;
- `Um ecossistema, diferentes formas de tornar possibilidades acessíveis.`

Essas formulações são territórios de copy, não redação final aprovada.

Evitar linguagem que pareça dizer:

- “escolha seu tipo de usuário”;
- “Pessoa usa Journey”;
- “Empresa usa Business”;
- “Coletivo usa X”;
- “cada participante tem seu produto”;
- “sete produtos para sete necessidades”;
- “selecione a solução ideal para você”.

A Home não deve transformar pertencimento em segmentação comercial.

---

## 9. Pessoa

A Pessoa é participante estrutural do ecossistema.

Na Home pública, a Pessoa é atendida naturalmente pela narrativa principal e possui `Iniciar Jornada` como porta de continuidade no Header vigente.

Isso não significa:

```text
Pessoa = Journey
```

Journey é produto/camada de experiência e continuidade.

A Pessoa poderá se relacionar com outras manifestações do ecossistema quando houver contexto legítimo.

---

## 10. Organização

Organização é participante estrutural e possui papel próprio no ecossistema.

Pode criar oportunidades, conhecimento, experiências, iniciativas, relações e outras possibilidades conforme autoridades vigentes.

A Home preserva um acesso dedicado `Organizações e Coletivos` para aprofundamento futuro.

Isso não significa:

```text
Organização = Guivos Business
```

Guivos Business é produto especializado B2B para contextos empresariais e institucionais de maior complexidade.

A existência de uma Organização não implica uso ou contratação de Business.

---

## 11. Coletivo

Coletivo é participante estrutural do ecossistema.

Seu valor não depende da existência de um `Guivos Coletivos` como produto homônimo.

Pode mobilizar, organizar, compartilhar conhecimento, criar experiências, gerar possibilidades e articular participação.

A ausência de produto homônimo deve reforçar, e não enfraquecer, a distinção:

> **os tipos de participante não são categorias de produto.**

---

## 12. Como entrar no Movimento 08

A primeira impressão do Movimento 08 não deve ser:

> “Agora veja nossos produtos.”

Deve ser próxima de:

> **“Para que um ecossistema tão diverso continue sendo uma única Guivos, diferentes capacidades cumprem papéis diferentes.”**

A redação não é copy final.

A partir daí, aplica-se `GKR-UX-HOME-NARR-002`:

1. reafirmar uma única Guivos;
2. apresentar Journey como experiência e continuidade;
3. apresentar Travel, Mall, Media, Business e Ads como manifestações especializadas;
4. apresentar Intelligence como inteligência transversal;
5. recompor tudo como um único ecossistema.

---

## 13. Relação visual futura

Sem definir layout, a transição deve evitar a imagem mental de três colunas que desembocam em produtos fixos.

Evitar especialmente:

```text
Pessoa       Organização       Coletivo
  ↓               ↓               ↓
Journey         Business          ???
```

Esse padrão seria conceitualmente incorreto.

A futura composição poderá explorar:

- múltiplos participantes compartilhando o mesmo universo;
- relações cruzadas;
- possibilidades circulando entre participantes;
- passagem de pessoas e instituições para diferentes contextos;
- uma expansão do campo de participação para o campo de capacidades;
- continuidade espacial que mostre unidade antes de especialização.

Não é necessário representar todas as relações possíveis.

A clareza da distinção é mais importante que a completude de um diagrama.

---

## 14. Papel da interação

Se houver movimento ou interação na transição, sua função deve ser demonstrar:

- muitos participantes;
- múltiplas formas de participação;
- uma única Guivos;
- diferentes capacidades que emergem sem fragmentar o ecossistema.

Não usar animação para criar falsa lógica causal entre um participante e um produto.

Exemplo de anti-padrão:

```text
Organização entra → ícone Business acende
```

Isso implicaria associação automática que a arquitetura não autoriza.

---

## 15. Critérios de aceitação

A transição é aderente quando:

- Pessoa, Organização e Coletivo continuam reconhecíveis como participantes;
- nenhum participante é reduzido a consumidor;
- nenhum participante é mapeado automaticamente a um produto;
- Organização não é confundida com Business;
- Journey não é apresentado como sinônimo de Pessoa;
- Coletivo mantém papel estrutural sem depender de produto homônimo;
- o visitante entende por que o Movimento 08 entra naquele momento;
- produtos aparecem como formas de materialização da mesma Guivos;
- a transição preserva simplicidade e não exige arquitetura técnica para ser entendida.

---

## 16. Critérios de rejeição

Rejeitar ou revisar se:

1. a Home cria correspondência `Pessoa → Journey`;
2. a Home cria correspondência `Organização → Business`;
3. Coletivo parece incompleto por não possuir produto homônimo;
4. participantes viram segmentos comerciais imediatamente antes da seção de produtos;
5. existe seletor obrigatório de tipo de participante para compreender a Home;
6. a transição parece catálogo por persona;
7. produtos parecem propriedades exclusivas de um tipo de participante;
8. a composição exige conhecimento da GLPA para ser compreendida;
9. o Movimento 07 termina em pertencimento e o 08 surge abruptamente como portfólio;
10. a ligação entre reciprocidade e materialização não é perceptível.

---

## 17. Teste de compreensão

Ao atravessar a passagem 07 → 08, o visitante deveria conseguir formular algo próximo de:

> **“Pessoas, Organizações e Coletivos fazem parte do mesmo ecossistema e podem criar ou viver possibilidades de maneiras diferentes. Os produtos não definem quem eles são; são formas pelas quais a Guivos organiza experiências, serviços e inteligência dentro desse universo.”**

---

## 18. Regra sintética para design

> **O tipo de participante não determina um produto correspondente. O contexto orienta quais capacidades do ecossistema podem fazer sentido.**

E, como regra de sequência:

> **Pertencimento primeiro. Materialização depois. Segmentação por produto, nunca.**

---

## 19. Estado da decisão

Estado deste refinamento:

> **TRANSIÇÃO MOVIMENTO 07 → 08 CONCEITUALMENTE DEFINIDA; COPY FINAL, COMPOSIÇÃO VISUAL E INTERAÇÃO MATERIAL PERMANECEM PARA ETAPA FUTURA.**

Este documento não altera fluxos internos dos produtos, Marketing/GTM, disponibilidade operacional, páginas de participantes ou a página `Mapa do Ecossistema`.
