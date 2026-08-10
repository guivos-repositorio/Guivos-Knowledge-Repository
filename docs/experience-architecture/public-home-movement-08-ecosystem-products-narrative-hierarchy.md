---
id: GKR-UX-HOME-NARR-002
title: Refinamento do Movimento 08 — Hierarquia Narrativa do Ecossistema e Produtos na Home Pública
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-10
parent: GKR-UX-HOME-NARR-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-002
  - GKR-UX-HOME-NAV-003
  - GLPA-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GPA-001
  - GPA-002
  - GPA-003
  - GPA-004
  - GPA-005
  - GPA-006
  - GPA-007
  - GKR-UX-HOME-GTM-BOUNDARY-001
normative: false
---

# Refinamento do Movimento 08 — Hierarquia Narrativa do Ecossistema e Produtos na Home Pública

## 1. Finalidade

Este documento refina o `Movimento 08 — Ecossistema / Produtos` da Home pública de `guivos.com`.

Seu objetivo é impedir que Journey, Travel, Mall, Media, Business, Intelligence e Ads sejam apresentados como uma grade horizontal de sete produtos equivalentes e fazer com que o visitante compreenda por que essas manifestações pertencem a uma única Guivos.

A decisão central é:

> **O Movimento 08 não é uma vitrine de produtos. É uma explicação da coerência do ecossistema.**

Este documento não cria wireframe, layout, cards, fluxos internos, disponibilidade operacional, estratégia de lançamento ou Marketing/GTM.

Quando houver conflito de interpretação com a descrição resumida do Movimento 08 em `GKR-UX-HOME-NARR-001`, este refinamento prevalece no limite específico da hierarquia entre os produtos e de sua representação institucional na Home.

---

## 2. Problema que o Movimento 08 precisa resolver

Ao chegar ao Movimento 08, o visitante já deve ter compreendido:

- que existe um universo maior de possibilidades;
- que possibilidades podem assumir formas diferentes;
- que muitas delas existem de maneira desconectada;
- por que a Guivos existe;
- que Pessoas, Organizações e Coletivos participam do ecossistema;
- que possibilidades podem chegar ao mundo real sem que a Guivos prometa resultado.

Neste ponto, a pergunta deixa de ser:

> “Quais produtos a Guivos vende?”

E passa a ser:

> **“Como uma ideia tão ampla ganha formas concretas sem deixar de ser uma única Guivos?”**

O Movimento 08 deve responder essa pergunta.

---

## 3. Regra estrutural

A arquitetura oficial da Guivos não trata todos os componentes como equivalentes funcionais.

Para a Home, essa diferença deve ser preservada semanticamente sem transformar a página em diagrama técnico.

A hierarquia conceitual é:

```text
GUIVOS
= uma tese / um ecossistema

├── EXPERIÊNCIA E CONTINUIDADE
│   └── Guivos Journey
│
├── MANIFESTAÇÕES ESPECIALIZADAS
│   ├── Guivos Travel
│   ├── Guivos Mall
│   ├── Guivos Media
│   ├── Guivos Business
│   └── Guivos Ads
│
└── INTELIGÊNCIA TRANSVERSAL
    └── Guivos Intelligence
```

Essa representação é conceitual.

Os rótulos `Experiência e Continuidade`, `Manifestações Especializadas` e `Inteligência Transversal` não são copy pública obrigatória.

A futura solução visual deve traduzir essa hierarquia com linguagem humana, não expor necessariamente as camadas técnicas da arquitetura de produto.

---

## 4. Tese do movimento

Território de formulação de trabalho:

> **Um ecossistema. Diferentes formas de tornar possibilidades acessíveis.**

Essa frase não é copy final.

Seu significado obrigatório é:

- existe uma única Guivos;
- diferentes componentes possuem responsabilidades distintas;
- cada componente materializa ou apoia uma parte da mesma tese maior;
- nenhum componente é a Guivos inteira;
- diversidade de produtos não equivale a fragmentação de marca.

---

## 5. Guivos Journey — não é apenas mais um item da grade

Guivos Journey deve aparecer como a principal camada de experiência e continuidade do participante.

Na narrativa institucional da Home, seu papel pode ser compreendido como o ambiente em que a jornada ganha continuidade, contexto, descoberta e próximos passos dentro dos limites já governados.

Journey não deve ser representada como um card equivalente a Travel, Mall, Media, Business, Intelligence e Ads.

Isso preserva três decisões já consolidadas:

1. Journey é a experiência principal do participante;
2. no Header Persistente, Journey possui porta própria em `Iniciar Jornada`;
3. Journey não integra o launcher de grade de pontos na hipótese vigente.

Regra:

> **Journey organiza a continuidade da experiência; não é apenas mais uma especialidade do portfólio.**

---

## 6. Produtos especializados — formas distintas de materialização

Travel, Mall, Media, Business e Ads devem ser tratados como manifestações especializadas do ecossistema.

Eles não precisam receber o mesmo tamanho, o mesmo formato ou a mesma intensidade visual.

A Home deve explicar primeiro a contribuição de cada um para o universo Guivos e somente depois, se fizer sentido, oferecer aprofundamento.

### 6.1 Guivos Travel

Território semântico:

- lugares;
- viagens;
- destinos;
- experiências relacionadas a deslocamento e turismo;
- possibilidades que podem sair da tela e ganhar espaço físico e vivência.

Leitura desejada:

> **“Parte do universo Guivos pode se materializar em lugares e experiências de viagem.”**

Não reduzir a Guivos a turismo.

### 6.2 Guivos Mall

Território semântico:

- produtos;
- serviços;
- ofertas curadas;
- ativos capazes de apoiar contextos, necessidades e experiências legítimas.

Leitura desejada:

> **“Produtos e serviços podem fazer parte da jornada quando possuem contexto e relevância — não como catálogo genérico.”**

Não reduzir a Guivos a marketplace, shopping promocional ou portal de descontos.

### 6.3 Guivos Media

Território semântico:

- histórias;
- conhecimento;
- perspectivas;
- entrevistas;
- vídeos;
- conteúdo editorial;
- memória do que acontece no ecossistema.

Leitura desejada:

> **“O ecossistema também torna histórias, conhecimento e experiências visíveis e compartilháveis.”**

Media não deve transformar a Home em portal de notícias ou feed.

### 6.4 Guivos Business

Guivos Business deve ser apresentado com precisão especial.

Ele é um produto especializado para contextos empresariais e institucionais de maior complexidade.

Ele **não é sinônimo de Organização** e não representa automaticamente a participação de Organizações no ecossistema.

Território semântico:

- soluções B2B;
- desenvolvimento de pessoas e públicos vinculados;
- programas corporativos;
- relacionamento e engajamento;
- benefícios e experiências;
- parcerias;
- inteligência empresarial no contexto autorizado.

Leitura desejada:

> **“Quando uma necessidade empresarial ou institucional exige capacidades próprias, existe uma manifestação especializada do ecossistema para esse contexto.”**

Regra obrigatória:

```text
Organização
≠
Guivos Business
```

A página `Organizações e Coletivos` pertence à arquitetura de participantes e não deve ser confundida com Guivos Business.

### 6.5 Guivos Ads

Território semântico:

- publicidade;
- mídia patrocinada;
- ativações de marca;
- patrocínios;
- presença comercial governada;
- transparência da natureza patrocinada.

Leitura desejada:

> **“Marcas e organizações podem ampliar presença por mecanismos patrocinados governados, sem transformar pagamento em relevância pessoal.”**

Ads não deve aparecer como atalho para comprar prioridade orgânica dentro da experiência do participante.

---

## 7. Guivos Intelligence — inteligência transversal, não protagonista isolada

Guivos Intelligence possui papel diferente dos serviços especializados.

Na Home, deve ser compreendida como inteligência do ecossistema que pode apoiar contexto, análise, organização, recomendações e relações entre conhecimento e possibilidades dentro dos limites governados.

Intelligence não deve ser representada como:

- “a IA da Guivos” ocupando o centro da marca;
- chatbot como definição da Guivos;
- produto tecnológico isolado dos demais;
- promessa de que a Guivos sabe o que é melhor para o participante;
- substituto da autonomia humana.

Leitura desejada:

> **“Existe inteligência apoiando o ecossistema, mas a experiência continua humana e a decisão permanece do participante.”**

Regra:

> **Intelligence sustenta compreensão; não substitui a tese da Guivos nem o protagonismo do participante.**

---

## 8. Relação entre os sete componentes

A Home não deve sugerir uma sequência técnica obrigatória entre os produtos.

Não afirmar, sem autoridade específica, que todo participante necessariamente passa por:

```text
Media → Journey → Intelligence → Travel → Mall → Ads → Business
```

ou qualquer cadeia equivalente.

A relação a comunicar é institucional:

> **cada manifestação possui uma responsabilidade distinta e todas pertencem ao mesmo universo de possibilidades da Guivos.**

A integração operacional real entre produtos permanece sob suas autoridades específicas.

---

## 9. Movimento 08 × launcher do Header

O launcher e o Movimento 08 não possuem a mesma função.

### Launcher do Header

Responde:

> **“Eu já sei onde quero ir. Como acesso?”**

É atalho de navegação.

Na hipótese vigente contém:

- Travel;
- Ads;
- Media;
- Business;
- Intelligence;
- Mall.

Journey possui `Iniciar Jornada` como porta própria.

### Movimento 08

Responde:

> **“Por que essas manifestações existem juntas e como fazem parte da mesma Guivos?”**

É explicação de significado e coerência.

Portanto:

> **o Movimento 08 não deve copiar visualmente o launcher ampliando seus seis itens para seis ou sete cards.**

O launcher orienta destino.

O Movimento 08 constrói compreensão.

---

## 10. Relação com Pessoas, Organizações e Coletivos

Pessoas, Organizações e Coletivos são participantes estruturais.

Journey, Travel, Mall, Media, Business, Intelligence e Ads são componentes/produtos do ecossistema.

A Home deve preservar:

```text
participante ≠ produto
```

Consequências:

- Pessoa não é sinônimo de Journey;
- Organização não é sinônimo de Business;
- Coletivo não precisa possuir um produto homônimo para ter papel estrutural;
- um participante pode relacionar-se com diferentes manifestações conforme contexto;
- nenhum produto cria um quarto tipo de participante.

---

## 11. Sequência narrativa interna recomendada

Sem determinar layout, o Movimento 08 deve seguir aproximadamente esta lógica:

### Passo 1 — reafirmar unidade

Começar pela ideia de que existe **uma Guivos**.

Não começar por sete logos.

### Passo 2 — mostrar a experiência principal

Explicar Journey como continuidade da experiência e da jornada.

### Passo 3 — abrir as manifestações especializadas

Mostrar que o mesmo ecossistema pode ganhar formas específicas por Travel, Mall, Media, Business e Ads.

A apresentação deve privilegiar consequência e contexto humano/institucional antes de feature.

### Passo 4 — revelar inteligência transversal

Explicar Intelligence como capacidade que apoia o ecossistema sem transformá-la na identidade inteira da Guivos.

### Passo 5 — recompor unidade

Fechar voltando à percepção:

> **“São formas diferentes de participar, descobrir, acessar, compreender ou viver possibilidades dentro de um mesmo ecossistema.”**

A redação é território conceitual, não copy final.

---

## 12. Direção de composição futura

O design poderá explorar, entre outras soluções:

- composição contínua em vez de grade;
- campos conectados;
- sequência editorial;
- camadas visuais com papéis diferentes;
- expansão progressiva de uma única ideia;
- relações espaciais que comuniquem unidade sem parecer arquitetura técnica;
- alternância entre experiência, manifestações especializadas e inteligência.

Evitar usar por convenção:

- sete cards idênticos;
- sete logos do mesmo tamanho com uma frase abaixo;
- mosaico SaaS;
- tabela comparativa;
- cards de preço;
- carousel de produtos como única explicação;
- diagrama técnico de camadas como peça pública dominante;
- grafo neural, linhas de dados ou estética de infraestrutura como metáfora principal;
- “hub central” que faça a Guivos parecer software de integração empresarial.

A solução futura precisa parecer simples para quem visita e coerente para quem analisa.

---

## 13. Hierarquia visual conceitual

Sem definir layout, a hierarquia de significado deve ser aproximadamente:

```text
1. GUIVOS / UMA IDEIA MAIOR
2. JOURNEY / EXPERIÊNCIA E CONTINUIDADE
3. MANIFESTAÇÕES ESPECIALIZADAS / TRAVEL, MALL, MEDIA, BUSINESS, ADS
4. INTELLIGENCE / APOIO TRANSVERSAL
5. ACESSOS DE APROFUNDAMENTO, SE NECESSÁRIOS
```

Essa hierarquia não exige que Journey seja visualmente maior em todos os breakpoints.

Exige apenas que seu papel diferente seja compreensível.

Da mesma forma, Intelligence pode atravessar a composição sem receber o tratamento de um sétimo bloco equivalente.

---

## 14. Acessos e CTAs no Movimento 08

O Movimento 08 pode oferecer acesso aos ambientes quando a futura materialização considerar isso útil.

Porém:

- acesso não deve dominar a explicação;
- não são necessários sete botões de mesma hierarquia;
- nomes ou áreas podem funcionar como aprofundamento de baixa hierarquia;
- o launcher já atende acesso rápido a quem conhece o destino;
- `Iniciar Jornada` permanece disponível no Header;
- CTA não deve transformar o movimento em catálogo de conversão.

Regra:

> **primeiro compreender por que o produto existe dentro da Guivos; depois, se desejar, aprofundar.**

---

## 15. Transição para Autoridade

O Movimento 08 deve terminar deixando uma pergunta natural:

> **“Entendi como o ecossistema se organiza. Mas existe substância real por trás dessa arquitetura?”**

Isso abre o Movimento 09 — Autoridade.

Portanto, o Movimento 08 não precisa tentar provar toda a operação dos produtos.

Sua função principal é coerência.

A função do movimento seguinte é substância e evidência.

---

## 16. Critérios de aceitação

Uma futura solução é aderente quando:

- o visitante percebe uma única Guivos antes de perceber sete nomes;
- Journey possui papel diferente dos serviços especializados;
- Intelligence possui papel transversal compreensível;
- Travel, Mall, Media, Business e Ads aparecem como especializações da mesma tese;
- Organização não é confundida com Business;
- participantes não são confundidos com produtos;
- nenhum produto se torna sinônimo da marca inteira;
- não existe necessidade de conhecer a arquitetura técnica para compreender a seção;
- o launcher e o Movimento 08 cumprem funções claramente diferentes;
- a seção produz coerência em vez de sensação de portfólio;
- a transição para autoridade permanece natural.

---

## 17. Critérios de rejeição

Rejeitar ou revisar se:

1. Journey, Travel, Mall, Media, Business, Intelligence e Ads aparecem como sete cards equivalentes;
2. a seção parece página de portfólio corporativo;
3. a seção replica visualmente o launcher do Header;
4. Journey parece apenas mais um serviço;
5. Intelligence vira protagonista tecnológico da marca;
6. Business é apresentado como “o lugar das Organizações”;
7. Coletivos desaparecem porque não possuem produto homônimo;
8. Mall faz a Guivos parecer marketplace;
9. Travel faz a Guivos parecer empresa de turismo;
10. Media faz a Home parecer portal de conteúdo;
11. Ads faz parecer que pagamento compra relevância orgânica;
12. o visitante precisa entender Experience Layer, Service Layer ou Intelligence Layer para entender a mensagem;
13. há excesso de features, planos, preços ou detalhes operacionais;
14. a seção descreve integrações não governadas como fatos;
15. quantidade de produtos é usada como prova de grandeza.

---

## 18. Teste de compreensão

Após o Movimento 08, o visitante deveria ser capaz de formular algo próximo de:

> **“A Guivos é uma só. A Journey organiza a continuidade da experiência; existem ambientes especializados para viagens, produtos e serviços, conteúdo, necessidades empresariais e mídia patrocinada; e existe uma camada de inteligência apoiando o ecossistema. Agora entendo por que esses nomes fazem parte da mesma ideia.”**

A pessoa não precisa conhecer os termos de arquitetura interna.

---

## 19. Regra sintética para design

> **Uma Guivos antes de sete produtos. Papéis diferentes antes de cards iguais. Coerência antes de catálogo.**

---

## 20. Estado da decisão

Estado deste refinamento:

> **HIERARQUIA NARRATIVA DO MOVIMENTO 08 CONCEITUALMENTE DEFINIDA; MATERIALIZAÇÃO VISUAL, COPY FINAL E ACESSOS MATERIAIS PERMANECEM PARA ETAPA FUTURA.**

Este documento não altera Marketing/GTM, disponibilidade operacional, launch plan, arquitetura interna dos produtos ou a página `Mapa do Ecossistema`.
