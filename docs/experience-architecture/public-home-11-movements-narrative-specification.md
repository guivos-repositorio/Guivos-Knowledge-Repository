---
id: GKR-UX-HOME-NARR-001
title: Especificação Narrativa Detalhada dos 11 Movimentos da Home Pública
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
parent: GKR-UX-HOME-HANDOFF-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-001
  - GKR-UX-HOME-VAL-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-BENCH-001
  - GKR-UX-HOME-BENCH-002
  - GEB-P01-F01
  - GEB-P01-F02
  - GEB-P01-F03
  - GEB-P01-F04
  - GEB-P01-F06
  - GPA-005
normative: false
---

# Especificação Narrativa Detalhada dos 11 Movimentos da Home Pública

## 1. Finalidade

Este documento detalha a arquitetura narrativa validada da Home pública de `guivos.com` em onze movimentos funcionais.

Seu objetivo é transformar a estratégia consolidada da Home em uma especificação suficientemente precisa para servir, futuramente, como entrada direta de:

- arquitetura de informação da Home;
- mapa narrativo;
- wireframe desktop;
- wireframe mobile;
- UX;
- UI;
- prototipação;
- direção de conteúdo;
- direção editorial;
- direção de movimento;
- especificação de mídia;
- avaliação de propostas em Figma;
- instrução de ferramentas generativas.

Este artefato não cria uma tela e não determina a quantidade final de blocos visuais.

Os onze movimentos definidos aqui são **funções narrativas obrigatórias**, não onze seções visuais obrigatoriamente independentes.

Uma futura solução poderá:

- combinar dois ou mais movimentos em uma mesma composição;
- distribuir um movimento em mais de um momento da página;
- usar uma única história para cumprir múltiplas funções;
- comprimir a narrativa quando a compreensão for preservada;
- variar composição entre desktop e mobile.

Ela não poderá eliminar a função semântica necessária apenas para reduzir a extensão da Home.

A regra principal é:

> **liberdade de composição não significa liberdade para perder significado.**

---

## 2. Escopo estrito

Este documento governa exclusivamente a **Home pública de `guivos.com`**.

Não governa, não desenha e não inicia:

- onboarding;
- cadastro;
- autenticação;
- Home autenticada;
- Journey protegida;
- perfil;
- recomendações personalizadas;
- fluxos internos de produtos;
- compra;
- checkout;
- reserva;
- publicação;
- criação de campanhas;
- operação B2B;
- backoffice;
- telas de Guivos Media;
- telas de Guivos Travel;
- telas de Guivos Mall;
- telas de Guivos Business;
- telas de Guivos Intelligence;
- telas de Guivos Ads;
- qualquer outro fluxo posterior à superfície pública da Home.

Produtos podem ser **apresentados institucionalmente** na Home somente no movimento definido para isso, sem que esta especificação passe a governar seus fluxos internos.

---

## 3. Estado da decisão

Estado deste documento:

> **ESPECIFICAÇÃO NARRATIVA CONCEITUALMENTE VALIDADA PARA SERVIR DE ENTRADA À FUTURA MATERIALIZAÇÃO DA HOME, AINDA SEM AUTORIZAÇÃO DE WIREFRAME, FIGMA, UI OU IMPLEMENTAÇÃO.**

A arquitetura consolidada é:

1. Hero — abrir o horizonte;
2. Possibilidades Reais — provar realidade;
3. Amplitude — mostrar diversidade de caminhos;
4. Desconexão — revelar o problema estrutural;
5. Guivos / Conexão — explicar o papel do ecossistema;
6. Do Possível ao Vivido — demonstrar consequência real;
7. Pertencimento — mostrar quem faz o ecossistema acontecer;
8. Ecossistema / Produtos — revelar formas de materialização;
9. Autoridade — demonstrar substância;
10. Autonomia e Confiança — preservar escolha e controle;
11. Descoberta — convidar à continuidade.

Essa sequência representa a ordem lógica dominante.

A futura solução pode combinar visualmente movimentos adjacentes, desde que preserve a progressão de compreensão.

---

## 4. Regra de precedência

Quando uma futura decisão de design entrar em conflito com esta especificação, prevalece:

1. Fundação da Guivos;
2. `UXA-020` e `UXA-021`;
3. `GKR-UX-HOME-001`;
4. `GKR-UX-HOME-VAL-001`;
5. `GKR-UX-HOME-HANDOFF-001`;
6. este documento;
7. benchmark;
8. proposta de wireframe;
9. proposta visual;
10. preferência estética ou tendência de mercado.

Nenhuma referência visual externa possui autoridade para redefinir a Guivos.

---

## 5. Tese-mãe que todos os movimentos devem preservar

A Home inteira deve responder progressivamente à pergunta:

> **O que se torna possível quando você entra aqui?**

A resposta emocional de amplitude é:

> **Um mundo maior de possibilidades passa a fazer parte do seu.**

A concretização institucional de trabalho é:

> **A Guivos conecta pessoas, organizações, conhecimento, oportunidades e experiências para tornar novos caminhos mais visíveis e possíveis.**

A Home deve fazer a pessoa compreender essa ideia por experiência narrativa e evidência, não por um manifesto longo na abertura.

---

## 6. Transformação perceptiva da Home

A Home deve conduzir o visitante por uma transformação de entendimento aproximada:

```text
ENTRAR
↓
PERCEBER QUE EXISTE MAIS
↓
VER QUE É REAL
↓
COMPREENDER A AMPLITUDE
↓
PERCEBER A FRAGMENTAÇÃO
↓
ENTENDER POR QUE A GUIVOS EXISTE
↓
VER POSSIBILIDADES SE TORNANDO EXPERIÊNCIAS
↓
PERCEBER QUE PODE FAZER PARTE
↓
COMPREENDER O ECOSSISTEMA
↓
ENCONTRAR EVIDÊNCIA
↓
SENTIR CONFIANÇA E CONTROLE
↓
QUERER DESCOBRIR
```

O visitante não precisa verbalizar essas etapas conscientemente.

A experiência deve permitir que essa compreensão se forme progressivamente.

---

## 7. Regra de encadeamento

Cada movimento deve responder uma pergunta deixada pelo anterior e, idealmente, criar a pergunta que justifica o seguinte.

A cadeia de perguntas é:

```text
O que pode ser possível?
↓
Isso acontece de verdade?
↓
Possibilidades de quê?
↓
Se já existem, por que a Guivos precisa existir?
↓
O que a Guivos faz com isso?
↓
O que acontece quando uma possibilidade faz sentido?
↓
Quem faz esse ecossistema acontecer?
↓
Como a Guivos organiza e materializa tudo isso?
↓
Por que acreditar que existe substância?
↓
A Guivos vai decidir por mim?
↓
O que faço agora?
```

Uma futura proposta que não preserve esse encadeamento deve justificar como alcança compreensão equivalente.

---

## 8. Contrato de especificação por movimento

Cada movimento é documentado com os seguintes campos:

- função estratégica;
- pergunta que resolve;
- resposta semântica;
- estado perceptivo de entrada;
- estado perceptivo desejado de saída;
- mensagem obrigatória;
- conteúdos elegíveis;
- tipos de prova;
- direção de mídia;
- papel da interação;
- ação comportamental desejada;
- transição para o próximo movimento;
- critérios de aceitação;
- critérios de rejeição;
- liberdade de design permitida;
- fragmento de instrução para ferramentas generativas.

---

# 9. MOVIMENTO 01 — HERO / ABRIR O HORIZONTE

## 9.1 Função estratégica

Abrir um novo campo de possibilidades sem iniciar pela estrutura interna da Guivos.

A Hero deve:

- interromper a leitura automática de landing page;
- colocar o visitante dentro da ideia;
- criar curiosidade;
- sugerir amplitude;
- transmitir futuro;
- transmitir humanidade;
- sinalizar sofisticação;
- deixar claro, em poucas camadas, que existe um ecossistema por trás da proposta;
- produzir vontade de continuar.

A Hero não deve tentar explicar a empresa inteira.

## 9.2 Pergunta que resolve

> **O que é este lugar e por que deveria continuar olhando?**

## 9.3 Resposta semântica

> **Aqui existe um universo maior de possibilidades e a Guivos conecta elementos desse universo para tornar novos caminhos mais visíveis e possíveis.**

## 9.4 Estado perceptivo de entrada

O visitante chega sem contexto ou com contexto limitado sobre a Guivos.

Pode interpretar inicialmente o domínio como:

- empresa;
- aplicativo;
- marca;
- comunidade;
- marketplace;
- tecnologia;
- portal.

A Hero precisa impedir uma redução prematura.

## 9.5 Estado perceptivo desejado de saída

A pessoa deve sentir algo próximo de:

1. “Que universo é esse?”
2. “Parece maior do que um serviço.”
3. “Talvez exista algo aqui que eu ainda não conheça.”
4. “Isso parece sério, humano e bem construído.”
5. “Quero continuar.”

## 9.6 Sistema semântico obrigatório

### Camada 1 — pergunta-mãe

> **O que se torna possível quando você entra aqui?**

### Camada 2 — amplitude / pertencimento

> **Um mundo maior de possibilidades passa a fazer parte do seu.**

### Camada 3 — concretização

> **A Guivos conecta pessoas, organizações, conhecimento, oportunidades e experiências para tornar novos caminhos mais visíveis e possíveis.**

A copy final poderá lapidar a terceira camada, mas não remover:

- conexão;
- pluralidade de participantes;
- conhecimento;
- oportunidades;
- experiências;
- novos caminhos;
- visibilidade/possibilidade;
- ausência de promessa de resultado.

## 9.7 Conteúdos elegíveis

A Hero pode utilizar, quando houver material real e direito de uso:

- vídeo documental curto;
- fotografia real;
- sequência de momentos humanos;
- recortes de experiências;
- pessoas em atividades reais;
- organizações em ação;
- coletivos em mobilização;
- lugares reais;
- criação;
- descoberta;
- aprendizagem;
- encontros;
- experiências em movimento.

## 9.8 Direção de mídia

A mídia deve comunicar:

> **há vida acontecendo além desta tela.**

Não deve ser decoração.

Deve evitar:

- pessoa sorrindo sem contexto;
- stock genérico;
- holograma;
- cérebro digital;
- interfaces de IA como protagonista;
- luxo como sinônimo de evolução;
- dashboard;
- mockup de produto dominante;
- “cidade futurista” genérica;
- estética cyberpunk;
- mapa-múndi usado apenas para parecer global.

## 9.9 Papel da tecnologia

A tecnologia deve ser percebida como capacidade implícita, não como assunto principal.

A primeira interpretação desejada é vida, possibilidade e descoberta.

## 9.10 Papel da interação

A interação deve ser mínima e orientada a continuidade.

A Hero não deve exigir:

- formulário;
- seleção de interesses;
- relato pessoal;
- upload;
- login;
- conta;
- questionário;
- câmera;
- voz;
- permissão de localização.

## 9.11 Ação comportamental desejada

> **Continuar explorando.**

Não é necessário converter ainda.

## 9.12 Transição para o movimento 02

A pergunta-mãe cria uma obrigação de prova.

A transição deve responder implicitamente:

> **“Veja.”**

O próximo movimento não deve abrir com portfólio de produtos.

## 9.13 Critérios de aceitação

A Hero é aderente se:

- a pergunta-mãe permanece dominante;
- existe amplitude sem vagueza absoluta;
- a Guivos não é reduzida a um produto;
- a terceira camada oferece compreensão suficiente;
- a pessoa não é pressionada a fornecer dados;
- a mídia comunica mundo real;
- existe curiosidade;
- existe sofisticação sem frieza;
- a página continua compreensível sem vídeo;
- não existe promessa de transformação.

## 9.14 Critérios de rejeição

Rejeitar se:

- abre com produtos;
- abre com IA;
- abre com dashboard;
- abre com categorias comerciais;
- parece coaching;
- parece manifesto sem explicar nada;
- exige cadastro para continuar;
- promete “transformar sua vida”;
- usa urgência artificial;
- usa stock como principal prova humana;
- copia visual reconhecível de um benchmark.

## 9.15 Liberdade de design

Pode variar:

- composição;
- proporção entre texto e mídia;
- direção de movimento;
- densidade;
- presença ou ausência de vídeo;
- forma de transição;
- CTA exploratório.

Não pode variar o significado central.

## 9.16 Fragmento de prompt para materialização

> Construa a abertura da Home como uma porta para um universo de possibilidades, não como apresentação de portfólio. Preserve a pergunta “O que se torna possível quando você entra aqui?”, comunique amplitude e pertencimento, explique brevemente que a Guivos conecta pessoas, organizações, conhecimento, oportunidades e experiências, use realidade humana em vez de estética tecnológica genérica e faça a principal ação psicológica ser continuar descobrindo.

---

# 10. MOVIMENTO 02 — POSSIBILIDADES REAIS / PROVAR REALIDADE

## 10.1 Função estratégica

Responder rapidamente à pergunta:

> **“O que vocês querem dizer com possibilidades?”**

por meio de realidade observável.

Este movimento reduz a distância entre promessa e prova.

## 10.2 Pergunta que resolve

> **Isso é apenas discurso de marca ou existem possibilidades acontecendo de verdade?**

## 10.3 Resposta semântica

> **Possibilidades começam de muitos lugares e podem ser vistas em pessoas, organizações, coletivos, conhecimento, experiências, lugares, relações e acontecimentos reais.**

## 10.4 Estado perceptivo de entrada

A pessoa está interessada, mas ainda pode interpretar a Hero como aspiração abstrata.

## 10.5 Estado perceptivo desejado de saída

> **“Isso acontece de verdade.”**

A credibilidade começa antes de qualquer grande claim institucional.

## 10.6 Mensagem obrigatória

A Home deve mostrar, não apenas afirmar.

Princípio:

```text
não apenas dizer que existem possibilidades
→ mostrar possibilidades reais
```

## 10.7 Exemplos de evidência elegível

### Pessoa

- descobriu algo que desconhecia;
- encontrou um caminho;
- participou de uma experiência;
- aprendeu;
- criou;
- contribuiu;
- conheceu alguém;
- mudou uma perspectiva.

### Organização

- criou uma oportunidade;
- ofereceu uma experiência;
- compartilhou conhecimento;
- abriu acesso;
- promoveu iniciativa;
- colaborou com participantes.

### Coletivo

- mobilizou pessoas;
- criou movimento;
- organizou causa;
- gerou experiência;
- compartilhou conhecimento;
- conectou participantes.

### Conhecimento

- conteúdo que ajudou alguém a perceber um caminho;
- história que ampliou perspectiva;
- informação que aproximou ação.

### Lugar / experiência

- experiência cultural;
- viagem;
- evento;
- encontro;
- atividade;
- contexto real verificável.

## 10.8 Pequenos e grandes movimentos

A Home não deve construir evolução apenas como evento extraordinário.

São elegíveis:

- pequenos próximos passos;
- mudanças graduais;
- experiências pontuais;
- grandes transições;
- movimentos institucionais;
- mobilizações coletivas.

Princípio:

> **evolução não possui uma única escala.**

## 10.9 Estrutura mínima de história

Quando aplicável:

```text
CONTEXTO
→ POSSIBILIDADE
→ ESCOLHA
→ EXPERIÊNCIA
→ CONTINUIDADE
```

Não é obrigatório apresentar todos os campos visualmente ao mesmo tempo, mas a origem e o papel dos participantes devem ser compreensíveis.

## 10.10 Protagonismo

Evitar:

> “A Guivos transformou a vida de X.”

Preferir narrativas que mostrem:

- o que a pessoa fez;
- o que a organização criou;
- o que o coletivo mobilizou;
- qual foi a contribuição da Guivos;
- quais outras condições participaram.

## 10.11 Papel do Guivos Media

O Guivos Media pode, futuramente e mediante integração autorizada, fornecer evidência editorial elegível.

Sua função na Home não é criar um feed de notícias.

É documentar o ecossistema acontecendo.

## 10.12 Ação comportamental desejada

> **Acreditar que a tese merece ser explorada.**

## 10.13 Transição para o movimento 03

Depois de observar alguns exemplos, a pergunta esperada é:

> **“Possibilidades de quê?”**

## 10.14 Critérios de aceitação

- provas reais ou claramente marcadas como ilustração quando não reais;
- origem verificável;
- papéis compreensíveis;
- diversidade de tipos de possibilidade;
- curadoria maior que volume;
- ausência de exagero causal;
- conteúdo humano;
- possibilidade de continuidade editorial.

## 10.15 Critérios de rejeição

- testemunho genérico;
- história sem fonte;
- case fictício apresentado como real;
- depoimento inventado;
- transformação milagrosa;
- antes/depois humilhante;
- sofrimento explorado;
- excesso de cards;
- feed infinito;
- narrativa em que a Guivos é “salvadora”.

## 10.16 Fragmento de prompt

> Logo após a Hero, prove a tese com poucas evidências humanas e institucionais cuidadosamente escolhidas. Mostre possibilidades reais surgindo de Pessoas, Organizações, Coletivos, conhecimento, lugares e experiências. Priorize histórias com contexto, escolha, experiência e continuidade; evite depoimentos genéricos, stock e volume de cards.

---

# 11. MOVIMENTO 03 — AMPLITUDE / EXPANDIR O CAMPO

## 11.1 Função estratégica

Mostrar que “possibilidade” não é uma categoria de produto nem uma única dimensão da vida.

## 11.2 Pergunta que resolve

> **Possibilidades de quê?**

## 11.3 Resposta semântica

> **Existem muitas formas de seguir em frente, descobrir, aprender, criar, experimentar, viajar, trabalhar, participar, contribuir, conectar-se, pertencer ou viver algo novo.**

## 11.4 Estado perceptivo de entrada

O visitante já acredita que existem casos reais, mas ainda pode imaginar que pertencem a uma vertical específica.

## 11.5 Estado perceptivo desejado de saída

> **“A Guivos não está tentando me encaixar em uma categoria.”**

## 11.6 Regra central

Amplitude deve ser comunicada por **situações e consequências**, não por departamentos comerciais.

Evitar como estrutura dominante:

- Carreira;
- Educação;
- Viagens;
- Saúde;
- Compras;
- Comunidades;
- Benefícios.

Esses domínios podem existir no ecossistema, mas não devem definir o significado da amplitude.

## 11.7 Forma conceitual preferida

Em vez de “Educação”:

> aprender algo que torna um próximo passo possível.

Em vez de “Networking”:

> conhecer alguém que talvez nunca cruzasse seu caminho.

Em vez de “Viagens”:

> conhecer um lugar ou viver uma experiência que amplia perspectiva.

Em vez de “Carreira”:

> descobrir um caminho profissional antes fora do campo de visão.

## 11.8 Regra de autonomia

A Home não deve comunicar que a pessoa precisa evoluir em todas as dimensões.

Amplitude não é checklist de vida ideal.

## 11.9 Escala percebida

A amplitude também pode comunicar escala por:

- diferentes idades;
- diferentes contextos;
- diferentes regiões;
- diferentes culturas;
- diferentes tipos de participantes;
- movimentos pequenos e grandes;
- diversidade de consequências.

## 11.10 Ação comportamental desejada

> **Perceber que o ecossistema pode ser relevante para muitos contextos sem exigir que todos sejam relevantes para mim.**

## 11.11 Transição para o movimento 04

A amplitude cria a pergunta:

> **“Se o mundo já possui tantas possibilidades, por que a Guivos precisa existir?”**

## 11.12 Critérios de aceitação

- amplitude perceptível;
- ausência de taxonomia rígida como mensagem dominante;
- diversidade sem sobrecarga;
- nenhuma definição única de sucesso;
- possibilidade de tradução global;
- diferentes formas de movimento humano/institucional.

## 11.13 Critérios de rejeição

- transformar amplitude em superapp;
- grade de categorias como tese central;
- sugerir que mais atividades = mais evolução;
- status, consumo ou dinheiro como medida universal;
- excesso de opções sem narrativa.

## 11.14 Fragmento de prompt

> Expanda o campo de possibilidades por consequências humanas e institucionais, não por uma grade de categorias comerciais. Mostre que próximos passos podem envolver aprender, conhecer, criar, experimentar, viajar, participar, contribuir ou mudar perspectiva, sem sugerir que todos precisam fazer tudo ou que existe uma definição única de sucesso.

---

# 12. MOVIMENTO 04 — DESCONEXÃO / REVELAR O PROBLEMA

## 12.1 Função estratégica

Justificar por que um ecossistema como a Guivos precisa existir.

## 12.2 Pergunta que resolve

> **Se as possibilidades já existem, qual problema a Guivos resolve?**

## 12.3 Resposta semântica

> **O mundo já possui muitas possibilidades, mas grande parte delas permanece dispersa, invisível, distante, fora de contexto ou desconectada de quem poderia percebê-las.**

## 12.4 Tese de trabalho

> **Possibilidades existem em todos os lugares. Encontrá-las no momento em que podem fazer sentido é outra história.**

Outra formulação interna válida:

> **O mundo não tem poucas possibilidades. Ele tem muitas possibilidades que ainda não se encontraram.**

## 12.5 Estado perceptivo de entrada

O visitante percebe amplitude, mas ainda não compreende a necessidade estrutural da Guivos.

## 12.6 Estado perceptivo desejado de saída

> **“Faz sentido: muitas coisas existem, mas eu só encontro uma pequena parte delas.”**

## 12.7 Tipos de desconexão

### Pessoa ↔ oportunidade

A oportunidade existe, mas a pessoa não sabe.

### Pessoa ↔ conhecimento

O conhecimento existe, mas não cruza seu contexto.

### Pessoa ↔ pessoa

Partes potencialmente complementares nunca se encontram.

### Pessoa ↔ organização

Uma organização possui algo relevante, mas não alcança aquele participante.

### Organização ↔ participantes

Uma organização procura públicos ou parceiros, mas os canais existentes são limitados.

### Coletivo ↔ participantes

Uma iniciativa existe, mas permanece dentro de círculos restritos.

### Experiência ↔ contexto

Algo potencialmente relevante aparece sem timing ou contexto.

### Conteúdo ↔ ação

Conhecimento é consumido, mas permanece isolado de possibilidades concretas.

## 12.8 Tom obrigatório

Este movimento deve ser uma **observação inteligente**, não dramatização.

Evitar:

- “você está perdendo sua vida”;
- “milhares de oportunidades estão passando por você”;
- culpa;
- medo;
- urgência artificial;
- discurso de mundo quebrado.

## 12.9 Direção visual conceitual

Pode representar:

- elementos isolados;
- relações ainda não percebidas;
- contextos que passam a fazer sentido;
- histórias paralelas que se aproximam.

Evitar grafo técnico como atalho visual obrigatório.

## 12.10 Ação comportamental desejada

> **Reconhecer a fragmentação como problema real.**

## 12.11 Transição para o movimento 05

A pergunta passa a ser:

> **“Então, o que a Guivos faz com essa fragmentação?”**

## 12.12 Critérios de aceitação

- problema compreensível;
- sem alarmismo;
- não afirma escassez artificial;
- mostra fragmentação, não incapacidade do participante;
- prepara naturalmente a função de conexão.

## 12.13 Critérios de rejeição

- medo;
- FOMO;
- vitimização;
- diagnóstico pessoal sem contexto;
- visual tecnológico que substitui explicação humana;
- dizer que “tudo o que você precisa está na Guivos”.

## 12.14 Fragmento de prompt

> Revele o problema estrutural sem dramatização: o mundo já contém pessoas, conhecimento, organizações, coletivos, experiências e oportunidades, mas grande parte desse universo permanece dispersa ou fora de contexto. Faça o visitante reconhecer a fragmentação sem sentir culpa, medo ou dependência da Guivos.

---

# 13. MOVIMENTO 05 — GUIVOS / CONEXÃO

## 13.1 Função estratégica

Explicar pela primeira vez de forma direta o papel estrutural da Guivos.

## 13.2 Pergunta que resolve

> **O que a Guivos faz?**

## 13.3 Resposta semântica

> **A Guivos conecta aquilo que normalmente existe separado e amplia as condições para que novos caminhos possam se tornar mais visíveis e possíveis.**

## 13.4 Estado perceptivo de entrada

O visitante reconhece a fragmentação, mas ainda não sabe qual é a resposta da Guivos.

## 13.5 Estado perceptivo desejado de saída

> **“Agora entendi por que a Guivos existe.”**

## 13.6 Relações que a Guivos pode conectar

```text
Pessoas ↔ Pessoas
Pessoas ↔ Organizações
Pessoas ↔ Coletivos
Pessoas ↔ Conhecimento
Pessoas ↔ Oportunidades
Pessoas ↔ Experiências
Organizações ↔ Participantes
Coletivos ↔ Participantes
Conhecimento ↔ Possibilidade
Possibilidade ↔ Próximo passo
Experiência ↔ Continuidade
```

Essa lista é arquitetura semântica, não recomendação de diagrama literal.

## 13.7 Conceito interno

> **infraestrutura de possibilidades**

A expressão ajuda a equipe interna a compreender que a Guivos não precisa ser proprietária de todos os elementos que conecta.

Ela não deve ser usada de modo a tornar a comunicação fria ou excessivamente técnica.

## 13.8 Regra de simplicidade

A complexidade interna não deve aparecer como complexidade pública.

A lógica pública desejada é:

```text
existe um momento
→ existem possibilidades
→ a Guivos conecta contexto e relações
→ algo se torna mais visível
→ o participante decide se quer explorar
```

## 13.9 Autonomia

Evitar:

- “a Guivos encontra seu caminho”;
- “nós sabemos seu próximo passo”;
- “a Guivos decide o que é relevante para você”.

Preferir a lógica:

> **tornar caminhos mais visíveis.**

## 13.10 Representação dos participantes

A Guivos não deve aparecer em fluxo unilateral:

```text
Guivos → usuário
```

A leitura correta é relacional:

```text
participantes ↔ possibilidades ↔ experiências ↔ novos contextos
```

com a Guivos conectando, organizando e apoiando relações.

## 13.11 Ação comportamental desejada

> **Compreender a função central da Guivos.**

## 13.12 Transição para o movimento 06

> **“E o que acontece quando uma dessas possibilidades realmente faz sentido?”**

## 13.13 Critérios de aceitação

- papel da Guivos compreensível;
- conexão acima de catálogo;
- tecnologia não domina;
- autonomia preservada;
- Pessoas, Organizações e Coletivos reconhecidos;
- ecossistema percebido como relacional.

## 13.14 Critérios de rejeição

- diagrama técnico como explicação principal;
- blockchain/grafo como estética;
- “AI matching” como protagonista;
- lista de produtos neste momento;
- promessa de encontrar o caminho ideal;
- superapp que “tem tudo”.

## 13.15 Fragmento de prompt

> Explique a Guivos como o ecossistema que conecta elementos normalmente separados. Mostre relações entre Pessoas, Organizações, Coletivos, conhecimento, oportunidades e experiências sem transformar a seção em diagrama técnico. O visitante deve entender por que a Guivos existe, mas continuar percebendo que a escolha de caminho pertence ao participante.

---

# 14. MOVIMENTO 06 — DO POSSÍVEL AO VIVIDO

## 14.1 Função estratégica

Demonstrar que valor não termina em descoberta, clique ou recomendação.

## 14.2 Pergunta que resolve

> **O que pode acontecer quando uma possibilidade faz sentido e é escolhida?**

## 14.3 Resposta semântica

> **Algumas possibilidades podem ser descobertas, consideradas, escolhidas e se transformar em experiências reais que geram novos contextos.**

## 14.4 Assinatura narrativa

> **Do possível ao vivido.**

## 14.5 Cadeia de valor

```text
POSSIBILIDADE
→ DESCOBERTA
→ CONSIDERAÇÃO
→ ESCOLHA
→ EXPERIÊNCIA
→ NOVO CONTEXTO
```

Nenhuma etapa deve ser interpretada como inevitável.

## 14.6 Estado perceptivo de entrada

O visitante entende conexão, mas ainda pode imaginar a Guivos como camada digital de descoberta.

## 14.7 Estado perceptivo desejado de saída

> **“Isso pode sair da tela e entrar na vida real.”**

## 14.8 Tipos de experiência

Podem incluir, conforme existência real e governança:

- aprendizagem;
- trabalho;
- criação;
- viagem;
- cultura;
- encontro;
- colaboração;
- participação comunitária;
- causa;
- produto ou serviço relevante;
- evento;
- projeto;
- relação;
- experiência pessoal ou institucional.

Nenhum domínio define universalmente evolução.

## 14.9 Estrutura narrativa preferida

### Momento

Qual era o contexto?

### Possibilidade

O que apareceu?

### Escolha

O que o participante decidiu?

### Experiência

O que aconteceu?

### Depois

Que novo contexto surgiu?

## 14.10 Autoridade longitudinal

Quando possível, documentar:

> **“E depois?”**

A continuidade deve ser valorizada porque evita tratar transformação como instante publicitário.

## 14.11 Causalidade

Não atribuir à Guivos resultados que dependem de múltiplos participantes e condições.

Explicitar papéis quando necessário.

## 14.12 Papel do Guivos Media

Pode documentar:

- “Do possível ao vivido”;
- “E depois?”;
- “O momento que abriu um caminho”;
- experiências;
- pessoas;
- organizações;
- coletivos;
- continuidade.

## 14.13 Ação comportamental desejada

> **Perceber a Guivos como capaz de conectar possibilidades a experiências concretas sem prometer resultado.**

## 14.14 Transição para o movimento 07

> **“Quem faz tudo isso acontecer?”**

## 14.15 Critérios de aceitação

- mundo real;
- processo compreensível;
- protagonismo correto;
- continuidade quando possível;
- ausência de milagre;
- ausência de promessa individual;
- experiência acima de clique.

## 14.16 Critérios de rejeição

- transformação garantida;
- histórias sensacionalistas;
- sucesso financeiro como padrão;
- “a Guivos mudou minha vida” sem contexto;
- causalidade exagerada;
- exploração de sofrimento;
- confundir engajamento digital com evolução real.

## 14.17 Fragmento de prompt

> Mostre a passagem do possível ao vivido por histórias de contexto, possibilidade, escolha, experiência e continuidade. A Guivos não deve ser a heroína da história. O foco é a experiência real e, quando possível, o que aconteceu depois. Não prometa que o mesmo resultado acontecerá com o visitante.

---

# 15. MOVIMENTO 07 — PERTENCIMENTO

## 15.1 Função estratégica

Transformar a percepção de “usuário de plataforma” em “participante de ecossistema”.

## 15.2 Pergunta que resolve

> **Quem faz esse ecossistema acontecer?**

## 15.3 Resposta semântica

> **Pessoas, Organizações e Coletivos também descobrem, criam, conectam, compartilham, participam e tornam possibilidades possíveis; a Guivos conecta esse movimento.**

## 15.4 Estado perceptivo de entrada

O visitante pode ainda imaginar uma relação Guivos → consumidor.

## 15.5 Estado perceptivo desejado de saída

> **“Talvez eu também tenha algo para descobrir, viver, criar ou contribuir.”**

## 15.6 Pessoas

Podem:

- descobrir;
- aprender;
- participar;
- criar;
- compartilhar;
- contribuir;
- experimentar;
- conectar;
- gerar novas possibilidades.

## 15.7 Organizações

Podem:

- criar oportunidades;
- oferecer experiências;
- disponibilizar conhecimento;
- abrir acesso;
- colaborar;
- apoiar iniciativas;
- desenvolver produtos e serviços;
- participar institucionalmente do ecossistema.

Não devem aparecer somente como patrocinadores ou logos.

## 15.8 Coletivos

Podem:

- mobilizar;
- reunir;
- organizar;
- criar movimentos;
- gerar experiências;
- compartilhar conhecimento;
- ampliar alcance;
- permitir participação comunitária.

## 15.9 Reciprocidade

Princípio:

> **Na Guivos, possibilidades não apenas são encontradas. Elas também podem ser criadas por quem participa do ecossistema.**

## 15.10 Limite de interpretação

Pertencimento não torna a Guivos uma rede social.

Não requer:

- seguir perfis;
- criar audiência;
- publicar constantemente;
- buscar seguidores;
- pertencer a uma “tribo” obrigatória.

## 15.11 Ação comportamental desejada

> **Perceber múltiplas formas legítimas de participação.**

## 15.12 Transição para o movimento 08

> **“Como a Guivos organiza e materializa tudo isso?”**

## 15.13 Critérios de aceitação

- Pessoas, Organizações e Coletivos com papel real;
- participante não reduzido a consumidor;
- reciprocidade;
- pertencimento sem dependência;
- diversidade sem estereótipos.

## 15.14 Critérios de rejeição

- “junte-se à nossa comunidade” como definição da Guivos;
- organizações mostradas apenas como logos;
- coletivos como decoração;
- pessoa apenas consumidora;
- gamificação como prova de pertencimento;
- visual de rede social.

## 15.15 Fragmento de prompt

> Mostre que o ecossistema é feito por Pessoas, Organizações e Coletivos com papéis reais. O visitante deve perceber que pode descobrir, viver, criar ou contribuir, sem transformar a Guivos em rede social. Organizações não são apenas logos e Pessoas não são apenas consumidoras.

---

# 16. MOVIMENTO 08 — ECOSSISTEMA / PRODUTOS

## 16.1 Função estratégica

Revelar, somente depois da compreensão da ideia maior, como a Guivos se materializa em diferentes estruturas e produtos.

## 16.2 Pergunta que resolve

> **Como a Guivos organiza e materializa esse ecossistema?**

## 16.3 Resposta semântica

> **Por diferentes manifestações especializadas da mesma ideia central, cada uma contribuindo para formas distintas de descobrir, conectar ou viver possibilidades.**

## 16.4 Estado perceptivo de entrada

O visitante entende propósito, conexão, realidade e participantes.

Agora está preparado para conhecer produtos sem reduzi-los à totalidade da marca.

## 16.5 Estado perceptivo desejado de saída

> **“Agora entendi como essa ideia maior começa a se materializar.”**

## 16.6 Regra principal

> **Os produtos devem ser explicados pela tese da Guivos; a tese não deve ser explicada pela lista de produtos.**

## 16.7 Interpretação institucional das manifestações

### Guivos Journey

Continuidade, contexto, descoberta e próximos passos, quando funcionalmente autorizado.

### Guivos Media

Histórias, conhecimento, perspectivas, acontecimentos e memória editorial do ecossistema.

### Guivos Travel

Descoberta e materialização de possibilidades associadas a lugares e experiências de viagem.

### Guivos Mall

Aproximação de produtos e serviços capazes de integrar contextos e experiências, dentro de regras de relevância e governança.

### Guivos Business

Participação de Organizações e relações institucionais no ecossistema.

### Guivos Intelligence

Capacidades de compreensão, organização e conexão de contexto, subordinadas à autonomia.

### Guivos Ads

Presença comercial e institucional governada, transparente e sem confundir pagamento com relevância pessoal.

A descrição acima é institucional e não abre os fluxos internos dos produtos.

## 16.8 Forma de apresentação

Pode utilizar:

- caminhos;
- portas de entrada;
- manifestações;
- ambientes especializados;
- relações entre capacidades;
- narrativa conectada.

Evitar tratar uma grade homogênea de cards como única solução possível.

## 16.9 Regra de marca

> **Nenhum produto pode se tornar sinônimo da Guivos inteira.**

## 16.10 Escala

A grandeza do ecossistema deve vir da coerência entre manifestações, não da quantidade de nomes.

## 16.11 Ação comportamental desejada

> **Compreender que existe estrutura suficiente para sustentar a ideia maior.**

## 16.12 Transição para o movimento 09

> **“Tudo bem. Mas por que eu deveria acreditar que existe substância por trás disso?”**

## 16.13 Critérios de aceitação

- produtos aparecem depois da tese;
- relação entre eles é compreensível;
- nenhum domina a marca;
- linguagem de ecossistema;
- sem excesso funcional;
- sem documentação técnica.

## 16.14 Critérios de rejeição

- abrir Home com Journey/Travel/Mall/etc.;
- grade de produtos sem narrativa;
- explicar funcionalidades demais;
- transformar Home em catálogo;
- transformar Intelligence em “a Guivos é uma IA”;
- transformar Mall em “a Guivos é marketplace”.

## 16.15 Fragmento de prompt

> Apresente os produtos somente depois de o visitante já compreender por que a Guivos existe. Trate Journey, Media, Travel, Mall, Business, Intelligence e Ads como manifestações especializadas da mesma ideia de ecossistema. Evite portfólio corporativo, grid genérico e excesso de funcionalidades.

---

# 17. MOVIMENTO 09 — AUTORIDADE / DEMONSTRAR SUBSTÂNCIA

## 17.1 Função estratégica

Responder por que a Guivos merece confiança e por que a ideia possui substância.

## 17.2 Pergunta que resolve

> **Por que acreditar nisso?**

## 17.3 Resposta semântica

> **Porque a Guivos demonstra evidências reais, participantes reais, critérios, conhecimento, transparência, continuidade e, conforme a operação amadurece, dados verificáveis.**

## 17.4 Estado perceptivo de entrada

O visitante compreende a arquitetura, mas ainda pode considerar a ambição maior que a prova disponível.

## 17.5 Estado perceptivo desejado de saída

> **“Existe método, contexto, gente real e responsabilidade por trás.”**

## 17.6 Fontes de autoridade

### Histórias reais

Com origem e autorização.

### Continuidade

O que aconteceu depois.

### Organizações reais

Com contexto de participação, não apenas logo.

### Coletivos reais

Com atuação verificável.

### Conhecimento

Conteúdo, especialistas, análises, pesquisas e perspectivas com autoria.

### Experiências verificáveis

Eventos, programas, iniciativas e experiências existentes.

### Indicadores reais

Quando existirem:

- participantes;
- organizações;
- coletivos;
- experiências;
- oportunidades;
- cidades;
- países;
- conteúdos;
- relações;
- outros indicadores governados.

Sempre com contexto, fonte e período.

### Governança

Autoridade também deriva de limites:

- não simular personalização;
- identificar patrocínio;
- não prometer resultado;
- não inventar números;
- preservar autonomia;
- reconhecer limitações.

## 17.7 Regra central

> **A Guivos deve parecer grande pelo que consegue demonstrar, não pelo que consegue afirmar.**

## 17.8 Escala percebida no estágio inicial

Pode vir de:

- qualidade editorial;
- consistência;
- diversidade de contextos;
- profundidade da arquitetura;
- clareza institucional;
- qualidade visual;
- diferentes tipos de participantes;
- ambição global coerente.

Não precisa ser simulada por números inexistentes.

## 17.9 Ação comportamental desejada

> **Confiar que existe substância institucional.**

## 17.10 Transição para o movimento 10

Quanto maior a autoridade percebida, mais necessária é a pergunta:

> **“Essa estrutura vai tentar decidir por mim?”**

## 17.11 Critérios de aceitação

- evidência verificável;
- contexto;
- fonte;
- transparência;
- maturidade sem autoengrandecimento;
- diferenciação entre prova atual e ambição futura.

## 17.12 Critérios de rejeição

- números inventados;
- logos sem relação;
- estatísticas decorativas;
- “líder”, “maior”, “revolucionária” sem evidência;
- presença global simulada;
- depoimentos vagos;
- cases fictícios;
- selos artificiais.

## 17.13 Fragmento de prompt

> Construa autoridade por evidência, não por autodeclaração. Use histórias verificáveis, participantes reais, conhecimento com autoria, continuidade, transparência e métricas somente quando existirem com fonte e período. Faça a Guivos parecer global pela qualidade e coerência, nunca por escala inventada.

---

# 18. MOVIMENTO 10 — AUTONOMIA E CONFIANÇA

## 18.1 Função estratégica

Equilibrar capacidade institucional com liberdade do participante.

## 18.2 Pergunta que resolve

> **A Guivos vai decidir por mim ou usar sua inteligência para definir o que é melhor para minha vida?**

## 18.3 Resposta semântica

> **Não. A Guivos amplia horizonte, contexto e possibilidades; a escolha continua sendo do participante.**

## 18.4 Formulação central

> **A Guivos amplia o horizonte. O caminho continua sendo seu.**

## 18.5 Estado perceptivo de entrada

O visitante reconhece autoridade, mas precisa perceber limites claros dessa autoridade.

## 18.6 Estado perceptivo desejado de saída

> **“Eles parecem saber o que estão fazendo, mas não estão tentando decidir minha vida.”**

## 18.7 Autonomia na experiência pública

### Explorar sem cadastro

Compreender a Guivos não deve depender de conta.

### Sem falsa personalização

Não afirmar conhecer o visitante antes de contexto autorizado.

### Sem urgência artificial

Evitar pressão comercial sem justificativa real.

### Sem definição universal de sucesso

Não estabelecer dinheiro, status, produtividade, viagem, consumo ou carreira como medida única.

### Direito de não seguir

Nem toda possibilidade é relevante para toda pessoa ou momento.

## 18.8 Confiança como comportamento

A pessoa deve perceber:

- posso explorar;
- não estão fingindo me conhecer;
- sei quando algo é patrocinado;
- consigo identificar origem de histórias;
- números possuem contexto;
- consigo sair;
- não preciso entregar dados para entender a proposta.

## 18.9 Tecnologia e inteligência

Princípio:

> **inteligência amplia contexto; não substitui decisão.**

## 18.10 Ação comportamental desejada

> **Sentir segurança suficiente para escolher continuar.**

## 18.11 Transição para o movimento 11

> **“Então o que posso fazer agora?”**

## 18.12 Critérios de aceitação

- controle perceptível;
- ausência de coerção;
- privacidade comportamental;
- autonomia clara;
- sem promessa pessoal;
- possibilidade de exploração pública.

## 18.13 Critérios de rejeição

- “sabemos o que você precisa”;
- “seu próximo passo é...” sem contexto;
- falsa recomendação pessoal;
- dark patterns;
- cadastro obrigatório para entender;
- urgência artificial;
- manipulação emocional.

## 18.14 Fragmento de prompt

> Depois de construir autoridade, explicite confiança por comportamento: a pessoa pode explorar sem cadastro, a Guivos não simula conhecê-la, patrocínio é transparente e inteligência não substitui decisão. Preserve a ideia “A Guivos amplia o horizonte. O caminho continua sendo seu.”

---

# 19. MOVIMENTO 11 — DESCOBERTA / CONTINUAR

## 19.1 Função estratégica

Transformar compreensão, credibilidade e confiança em vontade de explorar o ecossistema.

## 19.2 Pergunta que resolve

> **Entendi a Guivos. E agora?**

## 19.3 Resposta semântica

> **Descubra.**

A palavra sintetiza a motivação desejada, não necessariamente a copy final do CTA.

## 19.4 Estado perceptivo de entrada

O visitante já:

- compreendeu a tese;
- viu realidade;
- percebeu amplitude;
- entendeu a desconexão;
- entendeu o papel da Guivos;
- viu experiências;
- percebeu participantes;
- compreendeu o ecossistema;
- encontrou autoridade;
- sentiu autonomia.

## 19.5 Estado perceptivo desejado de saída

> **“Quero ver o que existe.”**

ou:

> **“Quero descobrir o que pode fazer sentido.”**

## 19.6 Função do CTA

O CTA deve ser continuação narrativa, não interrupção comercial.

Fluxo psicológico:

```text
CURIOSIDADE
→ COMPREENSÃO
→ CREDIBILIDADE
→ CONFIANÇA
→ DESCOBERTA
```

Evitar:

```text
CURIOSIDADE
→ PRESSÃO
→ CADASTRO
```

## 19.7 Territórios de copy futura

Não finais:

- Descubra a Guivos;
- Explore possibilidades;
- Veja o que existe aqui;
- Explore o que pode vir depois;
- Comece a descobrir.

A futura validação deve escolher pela combinação de:

- clareza;
- autonomia;
- curiosidade;
- simplicidade;
- continuidade.

## 19.8 Possível bifurcação futura

A Home poderá, se validado em UX, distinguir:

- quem deseja descobrir possibilidades;
- quem deseja criar possibilidades.

Essa bifurcação não deve complicar a Hero nem antecipar complexidade.

## 19.9 Fechamento como porta

A Home não deve parecer terminar a jornada.

Ela deve parecer abrir uma porta para aprofundamento.

Simetria narrativa:

```text
INÍCIO
“O que se torna possível quando você entra aqui?”

HOME
responde progressivamente

FECHAMENTO
“Descubra.”
```

## 19.10 Ação comportamental desejada

> **Explorar voluntariamente.**

## 19.11 Critérios de aceitação

- continuidade natural;
- CTA claro;
- ausência de pressão;
- não promete resultado;
- não reduz a Guivos a cadastro;
- preserva sensação de mundo aberto;
- permite caminhos secundários sem competir com a ação principal.

## 19.12 Critérios de rejeição

- “mude sua vida agora”;
- “encontre seu verdadeiro potencial”;
- “encontre seu caminho” como promessa;
- CTA agressivamente comercial;
- múltiplos CTAs equivalentes competindo;
- fechamento que parece captura de lead após narrativa institucional.

## 19.13 Fragmento de prompt

> Feche a Home como uma porta para exploração. A principal motivação deve ser “descobrir”, não comprar ou se cadastrar por pressão. Faça a chamada final parecer continuação natural da pergunta inicial e preserve autonomia, clareza e sensação de mundo aberto.

---

# 20. Matriz consolidada dos 11 movimentos

| # | Movimento | Pergunta central | Resposta desejada | Mudança perceptiva |
|---|---|---|---|---|
| 01 | Hero | O que é este lugar? | Existe um mundo maior de possibilidades | curiosidade → abertura |
| 02 | Possibilidades Reais | Isso é real? | Veja possibilidades acontecendo | aspiração → credibilidade |
| 03 | Amplitude | Possibilidades de quê? | Existem muitas formas de próximos passos | caso isolado → amplitude |
| 04 | Desconexão | Por que a Guivos precisa existir? | Muitas possibilidades permanecem dispersas | abundância → problema compreendido |
| 05 | Guivos / Conexão | O que a Guivos faz? | Conecta o que normalmente está separado | problema → função compreendida |
| 06 | Do Possível ao Vivido | O que acontece depois? | Algumas possibilidades viram experiências | digital → mundo real |
| 07 | Pertencimento | Quem faz acontecer? | Pessoas, Organizações e Coletivos | usuário → participante |
| 08 | Ecossistema | Como se materializa? | Produtos são manifestações da mesma tese | ideia → estrutura |
| 09 | Autoridade | Por que acreditar? | Evidência, continuidade e transparência | estrutura → confiança institucional |
| 10 | Autonomia | Vão decidir por mim? | O caminho continua sendo seu | autoridade → confiança sem submissão |
| 11 | Descoberta | E agora? | Explore voluntariamente | compreensão → continuidade |

---

# 21. Regras de compressão narrativa

Os onze movimentos **não equivalem automaticamente a onze blocos visuais**.

Uma proposta pode combinar, por exemplo:

- Possibilidades Reais + Amplitude;
- Guivos / Conexão + Do Possível ao Vivido;
- Pertencimento + Ecossistema;
- Autoridade + Autonomia.

A combinação é aceita quando:

1. as duas funções continuam identificáveis;
2. a pergunta anterior é respondida;
3. a transição seguinte continua lógica;
4. a densidade não impede compreensão;
5. nenhuma função é reduzida a decoração.

A combinação é rejeitada quando serve apenas para encurtar a página e perde a progressão perceptiva.

---

# 22. Regra contra “seções porque sites têm”

Nenhuma seção futura deve existir apenas por convenção de mercado.

Elementos como:

- Sobre nós;
- Benefícios;
- Features;
- Clientes;
- Depoimentos;
- Blog;
- FAQ;
- Logos;
- números;
- newsletter;
- parceiros;

só devem entrar quando cumprirem uma função explícita dentro dos onze movimentos.

Exemplos:

- logos podem servir a Autoridade, desde que tenham contexto;
- conteúdo pode servir a Possibilidades Reais, Do Possível ao Vivido ou Autoridade;
- perguntas frequentes podem existir se resolverem fricções reais, não porque a landing page “precisa de FAQ”.

---

# 23. Hierarquia de evidência

Quando houver escolha entre estética e evidência, priorizar evidência legítima.

Ordem aproximada de força:

1. experiência real documentada;
2. história longitudinal com continuidade;
3. participante real com contexto;
4. organização/coletivo real com atuação identificável;
5. conteúdo editorial com autoria e fonte;
6. dado verificável com período;
7. demonstração institucional;
8. ilustração claramente identificada;
9. abstração visual.

Stock genérico não deve ocupar o papel de evidência.

---

# 24. Papel transversal do Guivos Media

O Guivos Media pode futuramente alimentar os movimentos 02, 06, 07 e 09, desde que exista integração autorizada e conteúdo elegível.

Papéis:

- documentar possibilidade;
- registrar experiência;
- acompanhar continuidade;
- mostrar quem criou a possibilidade;
- produzir contexto;
- gerar memória editorial;
- demonstrar autoridade.

A Home não deve ser transformada em feed.

Regra:

> **conteúdo editorial entra para provar ou aprofundar a tese, não para aumentar volume.**

---

# 25. Direção de ritmo

A Home deve alternar, em lógica narrativa:

- abertura;
- prova;
- expansão;
- compreensão;
- emoção;
- estrutura;
- evidência;
- confiança;
- convite.

Evitar repetição de:

- card após card;
- texto após texto;
- vídeo após vídeo;
- números após números.

O ritmo deve reforçar a mudança perceptiva.

---

# 26. Estado sem prova suficiente

A arquitetura deve funcionar mesmo no estágio em que a Guivos ainda não possua volume suficiente de:

- cases;
- países;
- organizações;
- histórias;
- métricas.

Nesses casos:

- usar poucas provas verdadeiras;
- reduzir claims;
- reforçar clareza institucional;
- usar conteúdo editorial real;
- explicitar disponibilidade atual quando necessário;
- não preencher lacunas com ficção.

Princípio:

> **pouca prova verdadeira é superior a grandeza simulada.**

---

# 27. Teste dos primeiros dez segundos

Após breve exposição à Home, uma pessoa deve tender a compreender:

1. Guivos é maior do que um produto isolado;
2. fala sobre possibilidades, experiências e evolução;
3. existe dimensão humana real;
4. não precisa entregar dados imediatamente;
5. a Guivos conecta, mas não decide por ela;
6. a marca possui ambição global.

Falha crítica se a leitura principal for:

- IA;
- marketplace;
- viagens;
- coaching;
- benefícios;
- rede social;
- portal de conteúdo;
- conglomerado sem ideia central.

---

# 28. Teste de compreensão ao final da Home

Pergunta de pesquisa:

> **“Como você explicaria a Guivos para outra pessoa?”**

Interpretações desejadas devem incluir ideias próximas de:

- ecossistema;
- possibilidades;
- conexão;
- pessoas/organizações/coletivos;
- experiências;
- próximos passos;
- descoberta;
- autonomia.

A resposta não precisa repetir copy oficial.

O teste avalia significado, não memorização.

---

# 29. Teste de sensação

Perguntar:

> **“O que você sentiu que passou a ser possível depois de conhecer a Home?”**

Não existe uma resposta pessoal obrigatória.

O desejado é que a Home amplie horizonte sem induzir promessa específica.

---

# 30. Teste de pertencimento

Perguntar:

> **“Você se percebeu apenas como consumidor da Guivos ou como alguém que poderia descobrir, participar ou contribuir?”**

A resposta desejada tende à segunda leitura, sem obrigação de participação ativa.

---

# 31. Teste de autonomia

Perguntar:

> **“A página pareceu tentar decidir o que é melhor para você?”**

Desejado: não.

---

# 32. Teste de autoridade

Perguntar:

> **“O que fez a Guivos parecer confiável ou não confiável?”**

Sinais desejados:

- histórias reais;
- clareza;
- transparência;
- contexto;
- qualidade;
- coerência;
- ausência de pressão;
- fontes.

---

# 33. Contrato mínimo para futuro wireframe

Quando autorizada a fase de wireframe, cada proposta deverá anexar uma tabela de rastreabilidade com:

| Campo | Obrigatório |
|---|---|
| movimento atendido | sim |
| pergunta que resolve | sim |
| mensagem usada | sim |
| conteúdo/prova | sim |
| ação esperada | sim |
| transição | sim |
| risco principal | sim |
| estado mobile | sim |
| estado sem mídia | sim |
| justificativa de combinação de movimentos | quando aplicável |

Um wireframe sem rastreabilidade não deve ser considerado suficiente para validação estratégica.

---

# 34. Requisitos para desktop e mobile

A mesma narrativa deve sobreviver aos dois contextos.

No mobile:

- reduzir densidade sem eliminar significado;
- não esconder explicação essencial atrás de interação opcional;
- priorizar legibilidade;
- evitar vídeos obrigatórios;
- manter CTA e autonomia claros;
- preservar sequência narrativa.

No desktop:

- espaço adicional pode aumentar imersão;
- não deve ser usado para inserir complexidade desnecessária;
- mídia maior não substitui clareza.

---

# 35. Requisitos para movimento e animação

Movimento visual só deve ser usado para comunicar:

- entrada;
- ampliação;
- relação;
- conexão;
- passagem;
- continuidade;
- transformação de contexto.

Animação ornamental que não comunica significado deve ser tratada como secundária.

A experiência deve permanecer compreensível com `prefers-reduced-motion` ou sem animação.

---

# 36. Requisitos de internacionalização

Os onze movimentos devem funcionar globalmente.

A futura copy deve ser validada nativamente por idioma.

O design deve tolerar:

- expansão textual;
- contração textual;
- scripts diferentes;
- diferentes comprimentos de nomes;
- diferentes convenções culturais;
- diversidade real de participantes.

Evitar que uma metáfora visual brasileira seja requisito para compreensão.

---

# 37. Requisitos de acessibilidade

Cada movimento futuro deve prever:

- ordem de leitura;
- hierarquia semântica;
- contraste;
- navegação por teclado;
- foco;
- alternativa textual de mídia;
- legendas;
- transcrição;
- redução de movimento;
- comportamento sem autoplay quando necessário;
- entendimento sem depender apenas de cor.

---

# 38. Requisitos de integridade editorial

Toda prova real deve possuir, quando aplicável:

- origem;
- autorização de uso;
- autoria;
- data;
- contexto;
- indicação de patrocínio;
- critérios de privacidade;
- política de retirada/correção;
- ausência de promessa indevida.

---

# 39. Anti-padrões transversais

Rejeitar propostas que:

1. começam por produtos;
2. começam por tecnologia;
3. parecem marketplace;
4. parecem portal de benefícios;
5. parecem coaching;
6. prometem transformação;
7. fingem conhecer o visitante;
8. exigem cadastro para compreensão;
9. dependem de stock genérico;
10. usam luxo como evolução;
11. viram feed infinito;
12. usam patrocínio como relevância pessoal;
13. empilham cards sem progressão;
14. usam efeitos para compensar tese fraca;
15. copiam estética de benchmark;
16. tratam participantes como decoração;
17. escondem o papel da Guivos em abstração;
18. dependem de animação para compreensão;
19. simulam escala operacional;
20. transformam os onze movimentos em onze blocos burocráticos sem ritmo.

---

# 40. Prompt estruturado para geração do mapa narrativo da Home

O bloco abaixo pode ser usado futuramente como entrada complementar ao Prompt Mestre de `GKR-UX-HOME-HANDOFF-001`.

```text
Você está materializando somente a Home pública de guivos.com.

Não crie onboarding, área autenticada, Journey interna, checkout, cadastro detalhado ou fluxos de produto.

A Home deve responder progressivamente à pergunta:
“O que se torna possível quando você entra aqui?”

A tese emocional é:
“Um mundo maior de possibilidades passa a fazer parte do seu.”

A função institucional da Guivos é conectar Pessoas, Organizações, Coletivos, conhecimento, oportunidades e experiências para tornar novos caminhos mais visíveis e possíveis, preservando autonomia.

Construa a narrativa respeitando estas 11 funções:

1. HERO — abrir horizonte, curiosidade, futuro e pertencimento; não iniciar por produtos ou tecnologia.
2. POSSIBILIDADES REAIS — provar cedo com poucas histórias e experiências reais; mostrar antes de explicar.
3. AMPLITUDE — mostrar diferentes formas de próximos passos sem virar grade de categorias.
4. DESCONEXÃO — mostrar que muitas possibilidades já existem, mas permanecem dispersas ou fora de contexto; sem medo ou FOMO.
5. GUIVOS / CONEXÃO — explicar que a Guivos conecta o que normalmente está separado; sem grafo técnico ou IA como protagonista.
6. DO POSSÍVEL AO VIVIDO — mostrar possibilidade → escolha → experiência → continuidade, com mundo real e sem promessa de resultado.
7. PERTENCIMENTO — mostrar Pessoas, Organizações e Coletivos como participantes que também criam valor; não transformar em rede social.
8. ECOSSISTEMA / PRODUTOS — somente agora apresentar Journey, Media, Travel, Mall, Business, Intelligence e Ads como manifestações da mesma ideia, nunca como catálogo que define a marca.
9. AUTORIDADE — usar evidências, contexto, histórias, participantes e métricas apenas quando reais e verificáveis.
10. AUTONOMIA E CONFIANÇA — mostrar que a Guivos amplia horizonte sem decidir pela pessoa; permitir compreensão sem cadastro e sem falsa personalização.
11. DESCOBERTA — encerrar como porta para explorar; CTA orientado a descobrir, não a pressão comercial.

Os 11 movimentos são funções narrativas, não 11 blocos obrigatórios. Combine funções quando isso melhorar ritmo e compreensão, mas não elimine significado.

Cada movimento ou composição deve responder a pergunta criada pelo anterior.

Não adicione seções genéricas apenas porque landing pages costumam tê-las. “Sobre”, “Features”, “Clientes”, “Blog”, “FAQ”, logos ou números só podem entrar se cumprirem uma função narrativa explícita.

Use realidade humana, respiro, sofisticação, simplicidade, escala percebida e linguagem global. Tecnologia deve permanecer subordinada à vida.

Não use stock genérico como prova, hologramas, cyberpunk, dashboards como abertura, grade de produtos na Hero, promessas de transformação, urgência artificial, falsa personalização, números inventados, depoimentos fictícios ou presença global simulada.

A solução deve continuar compreensível sem vídeo e sem animação.

Antes de finalizar, gere uma tabela de rastreabilidade indicando para cada proposta:
- qual movimento atende;
- qual pergunta resolve;
- qual evidência usa;
- qual sensação pretende produzir;
- qual ação espera;
- como transiciona;
- quais riscos evita.
```

---

# 41. Prompt de auditoria de proposta futura

```text
Audite esta proposta de Home da Guivos contra GKR-UX-HOME-NARR-001.

Para cada um dos 11 movimentos, classifique:
- atendido;
- parcialmente atendido;
- ausente;
- contradito.

Explique a evidência observada na proposta.

Depois avalie de 0 a 5:
- clareza da tese;
- possibilidade;
- realidade;
- amplitude;
- compreensão da desconexão;
- clareza do papel da Guivos;
- mundo real / experiência;
- pertencimento;
- coerência do ecossistema;
- autoridade;
- autonomia;
- desejo de descoberta;
- simplicidade;
- sofisticação;
- escala percebida;
- acessibilidade conceitual;
- adequação global.

Aponte qualquer anti-padrão de rejeição imediata.

Não aprove a proposta apenas por qualidade estética.
```

---

# 42. Gate para materialização

Este documento não autoriza automaticamente a criação do wireframe.

Antes de materialização futura, deverá existir decisão explícita que confirme:

- escopo ainda restrito à Home;
- documentação desta frente integrada ou aceita como baseline de trabalho;
- copy que permanecerá fixa versus copy ainda experimental;
- disponibilidade real de histórias, imagens, vídeos e evidências;
- produtos/nomes que podem ser mostrados publicamente;
- estado operacional que pode ser comunicado;
- responsável por aprovação de design;
- ferramenta de materialização;
- critérios de versionamento e rastreabilidade.

---

# 43. Critério final de aderência

A futura Home será considerada narrativamente aderente quando uma pessoa puder percorrê-la e chegar, sem precisar conhecer a arquitetura interna da Guivos, a uma compreensão próxima de:

> **Existe um mundo maior de possibilidades. Algumas já acontecem de verdade. Elas assumem muitas formas, mas frequentemente estão desconectadas. A Guivos existe para conectar esse universo e tornar novos caminhos mais visíveis e possíveis. Pessoas, Organizações e Coletivos também fazem isso acontecer. Diferentes produtos materializam partes do mesmo ecossistema. Há evidências reais por trás da proposta. A Guivos amplia meu horizonte, mas a escolha continua comigo. Agora quero descobrir o que existe aqui.**

---

# 44. Síntese canônica desta especificação

```text
HOME GUIVOS
=
pergunta que abre horizonte
+
realidade que prova
+
amplitude que expande
+
desconexão que justifica
+
conexão que explica
+
experiência que concretiza
+
pertencimento que humaniza
+
ecossistema que estrutura
+
autoridade que sustenta
+
autonomia que protege
+
descoberta que continua
```

Regra-mãe:

> **A Home da Guivos não deve explicar um ecossistema para depois mostrar possibilidades. Deve mostrar possibilidades até que a pessoa naturalmente compreenda por que esse ecossistema precisa existir.**

Regra de design:

> **Os onze movimentos governam o significado; o design governa a melhor forma de materializá-los sem perder esse significado.**
