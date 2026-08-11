---
id: GKR-UX-HOME-OC-SYS-001
title: Mapa de Conteúdo, Prova e Evidência por Movimento da Home Pública de Organizações e Coletivos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-11
parent: GKR-UX-HOME-OC-MASTER-001
depends_on:
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-OC-AUDIT-001
  - GKR-UX-HOME-OC-NARR-001
  - GKR-UX-HOME-OC-NAV-001
  - GKR-UX-HOME-SYS-001
  - GKR-UX-HOME-NARR-004
  - UXA-014
  - UXA-019
related:
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-AUDIT-001
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
normative: false
---

# Mapa de Conteúdo, Prova e Evidência por Movimento da Home Pública de Organizações e Coletivos

## 1. Finalidade

Este documento executa o **P3 da prontidão pré-materialização** da Home Pública de Organizações e Coletivos e resolve em princípio `OC-GAP-03 — Conteúdo, prova e evidência por movimento` identificado por `GKR-UX-HOME-OC-AUDIT-001`.

Seu objetivo é definir:

- qual função editorial predomina em cada um dos onze movimentos;
- quando a narrativa precisa de evidência real;
- qual tipo de evidência é adequado a cada função;
- como distinguir evidência, explicação, ilustração e futuro;
- como operar quando a Guivos ainda possuir poucas provas públicas;
- como impedir que a futura Home se torne mural de logos, coleção de cases corporativos, dashboard de alcance ou publicidade institucional;
- como preservar verdade operacional sem empobrecer a ambição narrativa.

Este documento não escolhe casos concretos, parceiros, números, fotografias, vídeos, componentes, layouts ou copy pública final.

Ele também não cria nem autoriza:

- wireframe;
- Figma;
- SVG;
- protótipo;
- UI final;
- implementação;
- UXA-102/V5;
- Engenharia de Produto;
- publicação da página em produção.

Decisão central:

> **Cada movimento precisa provar somente aquilo que afirma. Prova não é decoração de credibilidade; é uma relação verificável entre uma afirmação e aquilo que a sustenta.**

---

## 2. Princípios herdados da Home Pública principal

A segunda Home pertence à mesma Guivos e herda o sistema transversal `GKR-UX-HOME-SYS-001`.

Continuam válidos:

### 2.1 Cinco classes de conteúdo

1. institucional permanente;
2. evidência real;
3. conteúdo editorial;
4. conteúdo de ecossistema;
5. navegação e ação.

### 2.2 Hierarquia de conteúdo

```text
SIGNIFICADO
→ REALIDADE
→ CONEXÃO
→ COMPREENSÃO
→ AÇÃO
```

### 2.3 Hierarquia de prova

Da forma mais forte para a mais fraca, quando aplicável:

1. prova direta;
2. história documentada;
3. evidência institucional;
4. métrica com definição, fonte, período e método;
5. depoimento contextualizado;
6. afirmação institucional.

Regra herdada:

> **Quanto maior a afirmação, maior deve ser a proximidade da evidência.**

### 2.4 Verdade antes de volume

Permanecem proibidos:

- Pessoas fictícias apresentadas como reais;
- Organizações fictícias apresentadas como parceiras reais;
- Coletivos fictícios apresentados como participantes reais;
- relações inexistentes apresentadas como relações da Guivos;
- números sem definição, fonte ou período;
- resultados inventados;
- geografias não confirmadas apresentadas como presença operacional;
- capacidades futuras apresentadas como disponíveis;
- claims de segurança, privacidade, conformidade ou inteligência sem base governada.

### 2.5 Pouca prova real é melhor que muita simulação

No estágio inicial:

> **Poucas evidências fortes e verdadeiras são superiores a uma superfície cheia de sinais de escala artificiais.**

A falta temporária de determinada prova não autoriza a criação de uma prova fictícia.

---

## 3. Classificação obrigatória de verdade editorial

Antes de qualquer conteúdo dinâmico, exemplo, história, métrica ou relação chegar à futura Home, ele deve ser enquadrável internamente em uma das categorias abaixo.

### 3.1 FATO GOVERNADO

Afirmação sustentada pelo Canon, por decisão arquitetural vigente ou por estado operacional verificável.

Exemplos de natureza:

- definição de Pessoa, Organização e Coletivo;
- arquitetura de produtos vigente;
- princípio `participante ≠ produto`;
- regra `Organização ≠ Business`;
- política ou contrato efetivamente governado.

Um fato governado pode ser explicado publicamente sem depender de um case.

### 3.2 EVIDÊNCIA VERIFICÁVEL

Acontecimento, relação, participante, experiência, iniciativa, métrica ou documento cuja existência possa ser demonstrada.

Deve possuir, conforme a natureza:

- origem;
- responsável ou autor;
- contexto;
- período;
- vínculo legítimo;
- limites de interpretação.

### 3.3 INTERPRETAÇÃO EDITORIAL

Síntese ou leitura produzida a partir de fatos e evidências.

Não deve ser apresentada como dado bruto nem como conclusão universal.

Exemplo de natureza:

> uma história demonstra que diferentes capacidades podem se complementar em determinado contexto.

Ela não autoriza concluir:

> a Guivos sempre produz esse resultado.

### 3.4 CENÁRIO ILUSTRATIVO

Exemplo conceitual utilizado para facilitar compreensão.

Pode mostrar relações possíveis, mas precisa permanecer distinguível de um acontecimento real.

Regra:

> **Cenário ilustrativo explica possibilidade; não prova que aquela relação aconteceu.**

Uma futura materialização não deve usar nomes, logos, fotografias realistas ou números que façam um cenário ilustrativo parecer um case verdadeiro.

### 3.5 ESTADO FUTURO OU CAPACIDADE NÃO DISPONÍVEL

Algo governado como direção, arquitetura ou intenção, mas ainda não necessariamente disponível em produção.

Sua comunicação pública precisa respeitar verdade operacional.

Arquitetura futura não equivale a disponibilidade atual.

---

## 4. Regra contra mistura de níveis de verdade

Os cinco níveis acima podem coexistir na mesma Home, mas não podem ser materializados de forma indistinguível.

Evitar:

```text
história real
+ cenário ilustrativo
+ produto futuro
+ métrica projetada

apresentados visualmente como se todos fossem fatos operacionais equivalentes
```

Regra:

> **A sofisticação visual nunca deve apagar a diferença entre o que existe, o que sabemos, o que interpretamos, o que ilustramos e o que ainda pode existir.**

---

## 5. Função de prova nesta segunda Home

A Home de Organizações e Coletivos não precisa provar que a Guivos é grande.

Ela precisa sustentar cinco percepções diferentes:

1. **capacidades e iniciativas reais já existem no mundo;**
2. **essas capacidades podem ser complementares sem que a Guivos invente causalidade;**
3. **valor pode circular entre participantes sem reduzir evolução a volume ou recompensa;**
4. **há responsabilidade, governança e limites na forma como a Guivos pretende conectar esse ecossistema;**
5. **existe uma arquitetura coerente de capacidades Guivos por trás da narrativa, sem confundir produto com participante.**

A prova é distribuída pela narrativa.

Não deve existir uma única seção chamada `Provas`, `Clientes`, `Cases` ou `Nossos números` encarregada de legitimar toda a página.

---

## 6. Mapa executivo dos onze movimentos

| Movimento | Função predominante | Necessidade de prova | Conteúdo preferencial |
|---|---|---|---|
| 01 — Abrir o horizonte | tese | baixa | institucional permanente |
| 02 — Reconhecer o que já existe | reconhecimento + realidade | média/alta | evidência real e exemplos reconhecíveis |
| 03 — Continuidade | hipótese explicativa | média | relações reais quando disponíveis; cenário ilustrativo claramente distinguido quando necessário |
| 04 — Papel da Guivos | explicação institucional | média | fato governado + arquitetura de atuação |
| 05 — Quem participa | explicação estrutural | baixa/média | fato governado + diversidade de tipos reais quando útil |
| 06 — Complementaridade | demonstração relacional | alta | relação documentada ou cenário ilustrativo explicitamente não factual |
| 07 — Múltiplas dimensões | amplitude contextual | média | repertório real diverso, sem catálogo de categorias |
| 08 — Valor, diversidade e escala | demonstração de reciprocidade | alta | evidência de valor contextual; métricas apenas quando interpretáveis |
| 09 — Confiança | autoridade e limites | muito alta | governança, método, fontes, transparência, privacidade, relações e limites verificáveis |
| 10 — Capacidades da Guivos | explicação de ecossistema | alta para disponibilidade; média para arquitetura | fatos governados + estado operacional correto |
| 11 — Como participar | navegação e ação | baixa | ação clara, contexto e autonomia |

Esse mapa governa **função**, não layout.

---

# 7. Movimento 01 — Abrir o horizonte

## Pergunta implícita

> **“Existe algo maior que minha atuação isolada?”**

## Função editorial

Tese.

A Hero introduz:

> `O que podemos tornar possível juntos?`

Sua responsabilidade é abrir campo de possibilidades, não demonstrar escala institucional.

## Conteúdo adequado

- pergunta-mãe;
- síntese curta da capacidade de Organizações e Coletivos;
- ideia de possibilidade compartilhada;
- sinal de que a narrativa continuará.

## Prova

Não é obrigatório colocar evidência pesada no primeiro viewport.

A credibilidade deve vir inicialmente de:

- clareza;
- sobriedade da afirmação;
- ausência de promessa exagerada;
- coerência com o que será demonstrado depois.

## Evitar

- parede de logos na Hero;
- `+1 milhão de pessoas` sem contexto;
- `transforme o mundo`;
- `alcance milhões de usuários`;
- CTA comercial como `fale com vendas` como ação dominante;
- claims superlativos para compensar falta de prova.

## Estado de saída

> **“Quero entender o que essa ideia significa.”**

---

# 8. Movimento 02 — Reconhecer o que já existe

## Pergunta implícita

> **“Isso já acontece no mundo real?”**

## Função editorial

Reconhecimento + realidade.

Esse movimento mostra que Organizações e Coletivos já criam conhecimento, oportunidades, experiências, serviços, iniciativas, relações e mobilização.

A Guivos ainda não precisa ser protagonista.

## Objeto da prova

> **a existência real das capacidades e iniciativas.**

## Evidências preferenciais

Quando disponíveis:

- uma Organização realizando algo concreto;
- um Coletivo mobilizando algo concreto;
- conhecimento produzido;
- oportunidade criada;
- experiência realizada;
- serviço ou iniciativa observável;
- contexto local ou global real.

## O que um logo sozinho não prova

Um logo apenas prova, no máximo, que a entidade existe ou possui algum vínculo autorizado para exposição.

Não prova:

- impacto;
- parceria estratégica;
- participação ativa;
- resultado;
- aderência ao ecossistema;
- transformação humana.

## Fallback inicial

Se ainda não houver casos Guivos suficientes, o movimento pode reconhecer capacidades do mundo por meio de linguagem institucional e conteúdo editorial verdadeiro sem insinuar que tais entidades já participam da Guivos.

Regra:

> **Reconhecer uma realidade externa não é o mesmo que reivindicá-la como resultado da Guivos.**

## Estado de saída

> **“Sim, essas capacidades existem e reconheço esse universo.”**

---

# 9. Movimento 03 — Continuidade

## Pergunta implícita

> **“E se esses momentos não precisassem permanecer isolados?”**

## Função editorial

Hipótese explicativa.

O movimento apresenta continuidade sem afirmar causalidade garantida.

## Formas de sustentação

### Preferência A — relação real documentada

Uma sequência verdadeira pode demonstrar que:

- uma experiência revelou um interesse;
- um interesse levou a conhecimento;
- uma conexão tornou uma oportunidade visível;
- uma iniciativa encontrou capacidade complementar.

A narrativa deve documentar apenas aquilo que realmente pode ser sustentado.

### Preferência B — cenário ilustrativo

Quando não houver uma sequência real adequada, pode-se explicar:

```text
experiência
→ pode abrir contexto para aprendizado
→ que pode tornar uma conexão mais provável
→ que pode revelar uma oportunidade
```

Mas a natureza ilustrativa precisa ser preservada.

## Linguagem causal proibida sem prova

Evitar afirmações universais como:

- `a Guivos transforma uma experiência em emprego`;
- `uma conexão gera oportunidade`;
- `participar da Guivos muda sua trajetória`;
- `a plataforma leva você ao próximo passo`.

Preferir:

- `pode abrir contexto`;
- `pode tornar visível`;
- `pode se conectar`;
- `pode fazer parte`;
- `pode contribuir`.

## Estado de saída

> **“Há uma possibilidade de continuidade; não uma promessa automática de resultado.”**

---

# 10. Movimento 04 — Papel da Guivos

## Pergunta implícita

> **“Qual é, então, o papel da Guivos?”**

## Função editorial

Explicação institucional.

## Objeto da prova

O movimento não precisa provar grandeza.

Precisa demonstrar coerência entre a tese e a arquitetura governada.

Pode se apoiar em fatos canônicos sobre o papel da Guivos:

- conectar participantes;
- organizar contexto;
- tornar possibilidades mais encontráveis;
- apoiar continuidade;
- aproximar capacidades complementares;
- preservar autonomia.

## Proteção

Não transformar arquitetura ou intenção em alegação de disponibilidade operacional universal.

A frase:

> `A Guivos conecta...`

precisa ser materializada de forma compatível com o estágio real do ecossistema no momento da publicação.

## Estado de saída

> **“Entendo o papel que a Guivos pretende exercer e ele é diferente de simplesmente intermediar oferta e demanda.”**

---

# 11. Movimento 05 — Quem participa

## Pergunta implícita

> **“Quem existe dentro desse ecossistema e como esses tipos se diferenciam?”**

## Função editorial

Explicação estrutural.

## Fonte de verdade

A principal prova aqui é o próprio contrato governado de participantes:

- Pessoa;
- Organização;
- Coletivo.

## Evidência complementar

Exemplos reais podem mostrar diversidade de formas, desde que não substituam a definição.

Exemplos possíveis de natureza organizacional:

- empresa;
- universidade;
- órgão público;
- fundação;
- associação formal;
- organização social.

Exemplos possíveis de natureza coletiva:

- movimento;
- rede;
- grupo;
- comunidade compatível com o contrato de Coletivo;
- articulação territorial;
- coletivo profissional, esportivo, cultural ou de interesse.

## Regra

> **Exemplo ajuda a reconhecer o tipo; exemplo não redefine o tipo.**

## Proteções

- `Comunidade` não vira produto;
- comunidade não é automaticamente sinônimo de Coletivo;
- Organização não equivale a empresa privada;
- Coletivo não equivale a ONG;
- papel momentâneo não substitui tipo estrutural.

## Estado de saída

> **“Entendo quem participa e onde minha realidade pode se encaixar.”**

---

# 12. Movimento 06 — Complementaridade

## Pergunta implícita

> **“Como capacidades diferentes podem fazer sentido umas para as outras?”**

## Função editorial

Demonstração relacional.

Este é um dos pontos de maior risco de simulação da Home.

## Preferência de prova

A evidência ideal é uma relação documentada em que diferentes participantes contribuíram de maneiras distintas para um mesmo contexto.

Exemplo estrutural legítimo quando real:

```text
Organização A
→ oferece determinada capacidade

Coletivo B
→ possui contexto, propósito ou mobilização

Pessoas
→ escolhem participar

resultado observável
→ limitado ao que a evidência sustenta
```

## O que precisa ser conhecido para usar uma relação real

Quando aplicável:

- quem participou;
- qual era a finalidade;
- qual capacidade cada participante ofereceu;
- quais responsabilidades existiam;
- qual período;
- qual relação efetivamente ocorreu;
- que consequência foi observada;
- quais conclusões não podem ser feitas.

## Fallback

Na ausência de relação real adequada, utilizar **cenário ilustrativo claramente não factual**.

Exemplo:

> Uma Organização pode possuir conhecimento; um Coletivo pode reunir pessoas interessadas; outra Organização pode possuir uma oportunidade relacionada.

Esse exemplo explica arquitetura de possibilidade, não prova que a Guivos já realizou essa composição.

## Regra

> **Nunca criar uma falsa parceria para demonstrar complementaridade.**

## Estado de saída

> **“Consigo visualizar como capacidades diferentes poderiam se complementar sem que uma delas precise dominar as demais.”**

---

# 13. Movimento 07 — Múltiplas dimensões

## Pergunta implícita

> **“Isso se limita a trabalho, negócios ou causas sociais?”**

## Função editorial

Amplitude contextual.

## Objeto da prova

Mostrar que evolução e participação podem fazer sentido em diferentes dimensões da vida sem prescrever um destino humano único.

## Conteúdo preferencial

Poucos exemplos diversos e suficientemente distintos podem provar amplitude melhor do que uma lista exaustiva.

Possíveis contextos:

- trabalho, carreira e estudos;
- saúde e bem-estar;
- relações e pertencimento;
- conhecimento;
- cultura;
- espiritualidade e propósito;
- viagens;
- empreendedorismo;
- cidadania;
- lazer;
- território.

## Regra editorial

> **Amplitude deve ser percebida pela diversidade de contextos, não por uma taxonomia infinita.**

## Cuidados adicionais

Em saúde, finanças, espiritualidade ou outros domínios sensíveis:

- não prometer resultado;
- não criar aconselhamento prescritivo na Home;
- não representar a Guivos como autoridade sobre qual caminho a pessoa deve seguir;
- distinguir claramente participante, fonte e contexto.

## Estado de saída

> **“Esse ecossistema não reduz a jornada humana a uma única dimensão.”**

---

# 14. Movimento 08 — Valor, diversidade e escala

## Pergunta implícita

> **“Participar gera valor para quem e como esse valor pode crescer?”**

## Função editorial

Demonstração de reciprocidade e escala responsável.

## Objeto da prova

O movimento precisa sustentar que diferentes participantes **podem gerar e receber valor**, sem afirmar que todo encontro produz resultado positivo.

## Evidências preferenciais

Quando existirem:

- benefício real recebido por Pessoas;
- capacidade ampliada de um Coletivo;
- resultado institucional, social ou econômico de uma Organização;
- colaboração entre participantes;
- continuidade de uma relação;
- diversidade real de contextos conectados.

## Métricas

Métricas podem ser utilizadas somente quando responderem uma pergunta relevante.

Exemplos de perguntas legítimas:

- o que está sendo contado?
- em qual período?
- em qual território?
- qual definição de participante?
- qual definição de oportunidade, experiência ou relação?
- qual relação existe entre o número e a afirmação feita?

## Métricas que não provam evolução sozinhas

```text
usuários cadastrados
impressões
cliques
membros
anúncios
visualizações
número de países listados
```

Esses números podem ser operacionalmente úteis, mas não demonstram por si sós:

- evolução humana;
- relevância;
- confiança;
- reciprocidade;
- impacto;
- qualidade da relação.

## Escala global

Não usar mapas preenchidos, bandeiras ou nomes de países como prova de presença se a presença operacional não existir.

A escala pode ser inicialmente comunicada como **arquitetura capaz de acomodar diversidade e expansão**, desde que não seja confundida com atuação já materializada.

## Regra

> **Escala é ampliação responsável do campo de possibilidades; volume é apenas uma das dimensões possíveis de medição.**

## Estado de saída

> **“Entendo por que participar pode fazer sentido para diferentes partes e por que diversidade importa mais que volume isolado.”**

---

# 15. Movimento 09 — Confiança

## Pergunta implícita

> **“Por que confiar na forma como a Guivos organiza essas relações?”**

## Função editorial

Autoridade + limites + responsabilidade.

Este é o território de prova institucional mais exigente da página.

## Distinção em relação ao Movimento 02

Movimento 02 responde:

> `isso existe?`

Movimento 09 responde:

> `há razões verificáveis para confiar em como a Guivos lida com isso?`

## Conteúdo preferencial

Conforme houver base governada e operacional:

- origem e autoria das informações;
- critérios de curadoria;
- governança;
- transparência de relações;
- metodologia;
- fontes;
- estado de verificação;
- privacidade e proteção de dados;
- critérios de uso de inteligência;
- identificação de patrocínio ou interesse comercial;
- mecanismo de contestação;
- limites da Guivos;
- distinção entre fato, declaração, inferência e desconhecido;
- evidências institucionais verificáveis.

## Métricas

Quando utilizadas aqui, exigem:

- nome da métrica;
- definição;
- período;
- fonte;
- método;
- escopo;
- limitações relevantes.

## Logos e relações

Uma marca conhecida não substitui governança.

Se um logo for usado como evidência de relação, a natureza da relação deve ser verdadeira e autorizada.

Não sugerir:

- parceria quando houve apenas fornecedor;
- cliente quando houve apenas contato;
- participação quando houve apenas prospecção;
- validação institucional quando houve apenas citação.

## Confiança e limites

A Home deve poder afirmar, quando governado:

> **Inteligência apoia. Não governa a decisão humana.**

E deve tornar possível compreender:

```text
o que sabemos
o que foi declarado
o que foi verificado
o que inferimos
o que ainda não sabemos
```

## Estado de saída

> **“Há critérios, responsabilidade e limites compreensíveis por trás da proposta.”**

---

# 16. Movimento 10 — Capacidades da Guivos

## Pergunta implícita

> **“Existe infraestrutura coerente por trás dessa visão?”**

## Função editorial

Explicação do ecossistema e de suas capacidades.

## Fonte de verdade

A arquitetura governada permanece:

```text
GUIVOS

├── EXPERIÊNCIA E CONTINUIDADE
│   └── Journey
│
├── MANIFESTAÇÕES ESPECIALIZADAS
│   ├── Travel
│   ├── Mall
│   ├── Media
│   ├── Business
│   └── Ads
│
└── INTELIGÊNCIA TRANSVERSAL
    └── Intelligence
```

## Função da prova

Aqui a prova não é mostrar sete logos de produtos.

É demonstrar **coerência arquitetural** e, quando a página estiver em produção, **verdade de estado**.

Para cada capacidade apresentada, deve ser possível diferenciar:

- existe como arquitetura governada;
- está em desenvolvimento;
- está disponível;
- está disponível apenas em determinado contexto;
- depende de futura ativação.

## Proteções

- Organização não equivale a Business;
- Pessoa não equivale a Journey;
- Coletivo não possui produto obrigatório homônimo;
- Intelligence não é um produto de vigilância;
- produto futuro não pode parecer funcionalidade disponível;
- quantidade de produtos não é prova de maturidade.

## Conteúdo preferencial

Cada nome de produto, quando necessário, deve responder:

> **“O que esta capacidade torna possível dentro da tese que já foi compreendida?”**

Não responder primeiro:

- lista de features;
- plano;
- preço;
- integração técnica;
- catálogo comercial.

## Estado de saída

> **“Entendo que existe uma arquitetura única por trás da visão e que os produtos são capacidades da Guivos, não a definição dos participantes.”**

---

# 17. Movimento 11 — Como participar

## Pergunta implícita

> **“Qual caminho faz sentido para mim agora?”**

## Função editorial

Navegação e ação.

## Necessidade de prova

Baixa.

A narrativa já deve ter construído contexto suficiente.

Esse movimento precisa provar principalmente **clareza e autonomia da ação**.

## Conteúdo

Dois caminhos equivalentes em legitimidade:

- `Descobrir como participar como Organização`;
- `Descobrir como participar como Coletivo`.

## Regra

O clique não precisa significar cadastro, compra ou contratação.

Ele abre uma jornada específica de compreensão e participação.

## Evitar

- `Cadastre sua empresa agora` como fechamento obrigatório;
- `Crie seu coletivo`;
- `Comece a vender`;
- `Alcance nossos usuários`;
- CTA de Organização visualmente superior ao de Coletivo sem razão governada;
- formulário comercial como única saída.

## Estado de saída

> **“Entendi onde me encaixo e posso continuar sem ser pressionado a converter.”**

---

## 18. Relação entre prova e as sete macroexperiências

O P1 consolidou sete macroexperiências.

A densidade de prova pode evoluir assim:

### Macro 01 — Abrir o campo de possibilidades

**Movimento 01**

- baixa densidade de prova;
- alta clareza de tese.

### Macro 02 — Reconhecer o que já existe e perceber a desconexão

**Movimentos 02 + 03**

- realidade concreta;
- exemplos verificáveis;
- hipótese de continuidade sem causalidade forçada.

### Macro 03 — Entender a Guivos e quem participa

**Movimentos 04 + 05**

- fatos governados;
- explicação institucional;
- exemplos de tipos sem transformar a macro em galeria de logos.

### Macro 04 — Perceber complementaridade e ampliar os contextos

**Movimentos 06 + 07**

- alta necessidade de honestidade relacional;
- relação real quando possível;
- cenário ilustrativo quando necessário;
- diversidade contextual.

### Macro 05 — Compreender valor, diversidade e escala

**Movimento 08**

- evidência de reciprocidade;
- métricas apenas com significado;
- escala sem simulação.

### Macro 06 — Encontrar confiança e compreender as capacidades da Guivos

**Movimentos 09 + 10**

- maior densidade institucional;
- governança;
- proveniência;
- limites;
- arquitetura do ecossistema;
- verdade operacional.

### Macro 07 — Escolher como continuar participando

**Movimento 11**

- baixa densidade de prova;
- alta clareza de ação e autonomia.

---

## 19. História real não é automaticamente `case de sucesso`

A linguagem editorial deve preservar agência e complexidade.

Quando uma história for usada, considerar:

1. contexto;
2. possibilidade;
3. decisão dos participantes;
4. experiência;
5. consequência observável;
6. continuidade;
7. limites da interpretação.

Preferir, quando adequado:

> **história de possibilidade**

em vez de:

> **case de sucesso**

quando `sucesso` implicar uma definição universal de evolução ou atribuição causal excessiva à Guivos.

---

## 20. Prova de relação entre Organização e Coletivo

A existência de duas entidades não prova uma relação.

Para representar uma relação como real, deve haver base para afirmar ao menos:

- que a relação existiu;
- qual era sua natureza;
- em qual período ou contexto;
- quais participantes estavam envolvidos;
- qual finalidade podia ser comunicada;
- quais dados e resultados podem ser publicados;
- se existe autorização de marca, nome, imagem ou depoimento quando necessária.

Regra:

> **Nunca construir visualmente uma parceria que o contrato real não sustenta.**

---

## 21. Patrocínio, publicidade e interesse comercial

Uma relação paga, patrocinada ou comercial não deve ser usada como prova neutra sem identificação adequada.

Quando materialmente relevante, distinguir:

- conteúdo editorial;
- participação institucional;
- parceria;
- patrocínio;
- publicidade;
- relação comercial;
- conteúdo promovido.

A existência de pagamento não invalida a relação, mas muda o contexto necessário para interpretá-la.

Regra:

> **Transparência comercial é parte da confiança, não um detalhe jurídico escondido.**

---

## 22. Dados, Intelligence e prova

A Home não pode sugerir que a Guivos conhece profundamente Pessoas porque possui grande volume de dados.

Intelligence deve ser explicada como capacidade de apoiar compreensão de contexto de forma responsável.

Quando dados forem utilizados como evidência, distinguir:

- dado pessoal;
- dado declarado;
- dado observado;
- dado agregado;
- inferência;
- evidência externa;
- informação desconhecida.

Não comunicar que Organizações recebem automaticamente dados de Pessoas ou membros de Coletivos.

Não transformar inferência em fato.

Não transformar precisão estatística em autoridade moral sobre a trajetória humana.

---

## 23. Métricas: contrato mínimo

Toda métrica pública material usada como prova deve possuir internamente:

| Campo | Obrigação |
|---|---|
| nome | o que está sendo medido |
| definição | o que entra e o que não entra |
| período | quando |
| escopo | onde / para quem |
| fonte | origem |
| método | como foi produzido |
| atualização | quando foi atualizada |
| limitações | o que não pode ser concluído |

Uma métrica que não possui esses atributos pode existir operacionalmente, mas não deve ser elevada a prova pública de grande afirmação.

---

## 24. Logos: contrato mínimo

Logos podem cumprir funções legítimas, mas precisam responder:

> **“O que este logo prova aqui?”**

Possibilidades legítimas incluem:

- identificação de autor;
- identificação de participante real;
- identificação de organização responsável por determinada evidência;
- identificação de relação explicitamente contextualizada.

Não utilizar logos apenas para produzir aparência de grandeza.

Parede de logos sem contexto é rejeitada como substituto de autoridade.

---

## 25. Depoimentos

Depoimento é evidência auxiliar.

Não deve sustentar sozinho grandes afirmações sobre:

- impacto;
- escala;
- eficácia;
- segurança;
- transformação;
- inteligência;
- representatividade.

Quando utilizado, preferir contexto:

- quem fala;
- em qual capacidade;
- sobre qual experiência;
- em qual período;
- qual relação possui com a Guivos.

---

## 26. Estado inicial com pouca evidência Guivos

A fase inicial não deve ser tratada como um problema a esconder.

A Home pode funcionar com um conjunto reduzido de provas se a hierarquia for correta.

### Estado inicial recomendado

- Hero forte e sóbria;
- reconhecimento de capacidades reais sem apropriação;
- poucos exemplos ou histórias profundas e verdadeiras;
- cenários ilustrativos claramente distinguíveis quando forem úteis à compreensão;
- arquitetura governada do ecossistema;
- transparência sobre estágio e disponibilidade;
- governança e limites verificáveis;
- ação de participação sem pressão.

### Estado inicial proibido

Compensar pouca maturidade por meio de:

- logos sem relação;
- números projetados apresentados como realizados;
- países não ativados;
- histórias sintéticas apresentadas como depoimentos;
- mockups de produto apresentados como disponibilidade;
- participantes genéricos chamados de `comunidade Guivos` sem base;
- afirmações de liderança de mercado.

Regra:

> **A verdade do estágio inicial é mais valiosa para confiança do que a aparência artificial de escala madura.**

---

## 27. Conteúdo vivo sem transformar a Home em feed

A segunda Home pode combinar três velocidades:

### Permanente

- tese;
- definições;
- papel da Guivos;
- princípios;
- arquitetura dos participantes;
- confiança e limites.

### Editorial

- histórias;
- entrevistas;
- experiências;
- conhecimento;
- relações documentadas;
- contextos de participação.

### Temporal

- iniciativas atuais;
- acontecimentos que justificam atualização;
- eventos ou oportunidades quando realmente relevantes à narrativa.

Regra herdada:

> **A Guivos é estável; o ecossistema está vivo.**

A Home não se torna um feed institucional de parceiros ou notícias.

---

## 28. Guivos Media como possível fonte editorial

Quando legitimamente autorizado e operacional, Media pode funcionar como memória editorial de evidências e histórias.

Isso não significa que todo conteúdo de Media seja prova adequada para a Home.

Para chegar à Home, o conteúdo precisa cumprir uma função narrativa específica:

- tornar realidade reconhecível;
- demonstrar complementaridade;
- mostrar amplitude;
- sustentar valor;
- demonstrar autoridade;
- explicar continuidade.

---

## 29. Responsividade do significado

Desktop e mobile podem exibir quantidades diferentes de evidência simultaneamente.

Mas ambos precisam preservar:

- origem da afirmação;
- distinção entre real e ilustrativo;
- contexto mínimo da métrica;
- identificação de relação quando relevante;
- transparência de patrocínio;
- acesso a fonte ou aprofundamento quando necessário.

Mobile não pode remover os qualificadores que tornam uma prova honesta apenas para reduzir espaço.

Regra:

> **Contexto essencial não é detalhe descartável de responsividade.**

---

## 30. Progressive disclosure da evidência

Nem todo método, fonte ou detalhe precisa ocupar o primeiro nível visual.

É legítimo trabalhar com:

```text
afirmação compreensível
→ sinal de evidência
→ contexto resumido
→ aprofundamento / fonte / metodologia
```

Desde que a informação essencial não seja escondida de modo enganoso.

A prova pode ser aprofundável; não pode ser opaca.

---

## 31. Prova e acessibilidade

Evidência não pode depender exclusivamente de:

- imagem;
- animação;
- hover;
- vídeo sem transcrição;
- cor;
- interação por arraste.

Uma pessoa utilizando leitor de tela, teclado, redução de movimento ou conexão limitada deve continuar entendendo:

- qual afirmação está sendo feita;
- qual evidência a sustenta;
- qual é seu contexto.

---

## 32. Anti-padrões gerais

Rejeitar uma futura materialização se ela utilizar prova para produzir qualquer uma destas leituras:

### `Empresas que confiam na Guivos`

sem que a relação e a natureza dessa confiança sejam demonstráveis.

### `Milhões de possibilidades`

como número abstrato sem definição.

### `Impacto comprovado`

sem método, período e objeto de impacto.

### `Transformamos vidas`

atribuindo causalidade institucional à Guivos.

### `Acesse nossa comunidade`

reduzindo Pessoas e Coletivos a audiência disponível para Organizações.

### `Dados que conhecem você`

apresentando Intelligence como vigilância ou autoridade sobre a Pessoa.

### `Ecossistema global`

representado como atuação mundial já existente quando for apenas ambição ou arquitetura de escala.

### `Case ilustrativo`

materializado de forma que pareça um case real.

---

## 33. Testes de integridade por movimento

### Movimento 01

Se removermos logos e números, a Hero continua forte?

Se não, a tese está dependente de prova de status.

### Movimento 02

O conteúdo mostra capacidades acontecendo ou apenas nomes conhecidos?

Se mostrar apenas nomes, não prova realidade suficiente.

### Movimento 03

A sequência é real ou ilustrativa?

O visitante consegue distinguir?

### Movimento 04

Estamos explicando papel governado ou prometendo capacidade ainda não disponível?

### Movimento 05

Os exemplos ajudam a reconhecer os participantes ou os redefinem de forma estreita?

### Movimento 06

Existe base real para a relação representada?

Se não, ela está claramente apresentada como possibilidade ilustrativa?

### Movimento 07

A diversidade está no significado ou apenas na aparência das imagens?

### Movimento 08

Os números demonstram valor ou apenas tamanho?

### Movimento 09

Há razões verificáveis para confiar ou apenas autodeclaração institucional?

### Movimento 10

A arquitetura está clara sem transformar produtos em catálogo ou disponibilidade fictícia?

### Movimento 11

A ação preserva autonomia ou utiliza toda a prova anterior para pressionar conversão?

---

## 34. Matriz de risco de prova

| Risco | Movimentos mais sensíveis | Proteção |
|---|---|---|
| falsa causalidade | 03, 06, 08 | linguagem probabilística + consequência observável |
| falsa relação | 02, 06, 09 | proveniência e natureza da relação |
| falsa escala | 08, 10 | métricas contextualizadas + estado operacional |
| participante = audiência | 06, 08, 11 | agência, reciprocidade e autonomia |
| produto = participante | 05, 10 | contrato `quem ≠ como` |
| Intelligence = acesso a Pessoas | 08, 09, 10 | privacidade, finalidade e distinção de dados |
| prova = logo | 02, 09 | contexto da relação |
| ilustração = evidência | 03, 06 | classificação editorial explícita |
| arquitetura = disponibilidade | 04, 10 | estado operacional verificável |
| volume = evolução | 08 | métricas de significado e limites |

---

## 35. Critério de fechamento do P3

`OC-GAP-03` é considerado resolvido em princípio quando uma futura equipe de Design consegue responder, sem inventar estratégia:

1. qual movimento precisa de prova forte e qual pode funcionar por tese;
2. o que cada evidência está tentando provar;
3. quando uma história pode ser usada;
4. quando um cenário precisa ser marcado como ilustrativo;
5. quando uma métrica é admissível;
6. por que um logo isolado não é autoridade;
7. como provar complementaridade sem inventar relações;
8. como mostrar valor sem transformar volume em evolução;
9. como demonstrar confiança por governança, método e limites;
10. como apresentar produtos respeitando verdade operacional;
11. como operar com poucas provas reais no estágio inicial.

Estado após este documento:

```text
OC-GAP-01 — Macroexperiências
= RESOLVIDO EM PRINCÍPIO

OC-GAP-02 — Header / Hero / CTAs
= RESOLVIDO EM PRINCÍPIO

OC-GAP-03 — Conteúdo / Prova / Evidência
= RESOLVIDO EM PRINCÍPIO

OC-GAP-04 — Handoff específico para Design
= AINDA ABERTO
```

---

## 36. O que permanece aberto para P4

Este documento não determina:

- quais trechos do Documento Mestre são copy obrigatória;
- quais trechos são apenas matéria-prima estratégica;
- o que Design pode condensar;
- o que não pode desaparecer;
- qual copy ainda precisa de lapidação;
- critérios formais de aceite do primeiro wireframe;
- instruções consolidadas para ferramentas generativas;
- pacote final de fontes que Design deve receber.

Essas responsabilidades pertencem ao **P4 — Handoff específico para Design/UX/UI**.

---

## 37. Contrato final de conteúdo e prova

> **A Home Pública de Organizações e Coletivos deve construir credibilidade distribuindo evidência de acordo com a função de cada movimento. Realidade prova que capacidades existem; relações reais ou cenários explicitamente ilustrativos ajudam a compreender complementaridade; métricas só sustentam afirmações quando possuem contexto; governança, proveniência e limites sustentam confiança; arquitetura e estado operacional sustentam os produtos. Em nenhum ponto a Guivos deve substituir ausência de prova por logos, números, histórias, geografias ou relações simuladas.**

Teste final:

> **Se retirarmos o prestígio visual de marcas, números e efeitos, a afirmação ainda continua verdadeira e demonstrável? Se não continuar, a prova escolhida está mascarando uma lacuna em vez de resolvê-la.**

---

## 38. Limites desta decisão

Este documento:

- não altera os onze movimentos do Documento Mestre;
- não altera as sete macroexperiências do P1;
- não altera a arquitetura de Header, Hero e CTAs do P2;
- não escolhe parceiros, cases, histórias, métricas ou países;
- não autoriza uso público de nenhuma relação existente;
- não define política jurídica de consentimento ou licenciamento de conteúdo;
- não cria wireframe;
- não cria Figma;
- não cria SVG;
- não cria protótipo;
- não cria UI;
- não inicia UXA-102/V5;
- não inicia implementação.

A próxima etapa governada é o **P4 — Handoff específico para Design/UX/UI**.
