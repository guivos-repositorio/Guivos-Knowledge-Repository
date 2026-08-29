---
id: GKR-UX-HOME-OC-SYS-001
title: Mapa de Conteúdo, Prova e Evidência por Movimento da Home Pública de Organizações e Coletivos
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-29
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
  - GKR-FULL-CORPUS-AUDIT-001
  - GKR-UX-HOME-HANDOFF-001
  - GKR-UX-HOME-AUDIT-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
normative: false
maturity: reconciled_content_proof_detail_pre_materialization
---

# Mapa de Conteúdo, Prova e Evidência por Movimento da Home Pública de Organizações e Coletivos

## 1. Finalidade e função atual

Este documento nasceu como o **P3 da prontidão pré-materialização** da Home Pública de Organizações e Coletivos e, naquele checkpoint, resolveu em princípio `OC-GAP-03 — Conteúdo, prova e evidência por movimento` identificado por `GKR-UX-HOME-OC-AUDIT-001`.

Depois da reconstrução documental de `GKR-UX-HOME-OC-MASTER-001 v1.0.0`, da reconciliação de `GKR-UX-HOME-OC-NARR-001 v0.2.0` e de `GKR-UX-HOME-OC-NAV-001 v0.2.0`, sua função atual é preservar e aprofundar o **contrato especializado de conteúdo, prova e evidência** da Home O/C, sem competir com o Documento Mestre como autoridade de consumo vigente.

Estado de autoridade:

```text
GKR-UX-HOME-OC-MASTER-001 v1.0.0
→ autoridade de consumo vigente da Home O/C

GKR-UX-HOME-OC-NARR-001 v0.2.0
→ detalhe narrativo reconciliado

GKR-UX-HOME-OC-NAV-001 v0.2.0
→ detalhe especializado reconciliado de navegação / Hero / CTAs

GKR-UX-HOME-OC-SYS-001 v0.2.0
→ detalhe especializado reconciliado de conteúdo / prova / evidência
→ não autoriza materialização
```

Seu objetivo permanece definir:

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
- grid ou layout;
- componente;
- implementação;
- publicação;
- disponibilidade operacional;
- UXA-102/V5;
- retomada de Product Engineering;
- Marketing/GTM;
- cadastro ou onboarding;
- materialização da experiência autenticada de Organização ou Coletivo.

Durante a auditoria integral:

```text
DETALHE DE CONTEÚDO E PROVA RECONCILIADO
≠ DESIGN VIGENTE
≠ WIREFRAME AUTORIZADO
≠ UI APROVADA
≠ IMPLEMENTAÇÃO AUTORIZADA
```

Decisão central:

> **Cada movimento precisa provar somente aquilo que afirma. Prova não é decoração de credibilidade; é uma relação verificável entre uma afirmação e aquilo que a sustenta.**

---

## 2. Princípios herdados da Home Pública principal

A segunda Home pertence à mesma Guivos e herda o sistema transversal `GKR-UX-HOME-SYS-001`, sempre interpretado sob a autoridade atual do Master O/C.

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
- claims de segurança, privacidade, conformidade ou Intelligence sem base governada.

### 2.5 Pouca prova real é melhor que muita simulação

No estágio inicial:

> **Poucas evidências fortes e verdadeiras são superiores a uma superfície cheia de sinais de escala artificiais.**

A falta temporária de determinada prova não autoriza a criação de uma prova fictícia.

---

## 3. Classificação obrigatória de verdade editorial

Antes de qualquer conteúdo dinâmico, exemplo, história, métrica ou relação chegar à Home, ele deve ser enquadrável internamente em uma das categorias abaixo.

### 3.1 FATO GOVERNADO

Afirmação sustentada pelo Canon, por decisão arquitetural vigente ou por estado operacional verificável.

Exemplos de natureza:

- definição de Pessoa, Organização e Coletivo;
- arquitetura de Produtos vigente;
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

Uma futura materialização, se autorizada, não deve usar nomes, logos, fotografias realistas ou números que façam um cenário ilustrativo parecer um case verdadeiro.

### 3.5 ESTADO FUTURO OU CAPACIDADE NÃO DISPONÍVEL

Algo governado como direção, arquitetura ou intenção, mas ainda não necessariamente disponível em produção.

Sua comunicação pública precisa respeitar verdade operacional.

Arquitetura futura não equivale a disponibilidade atual.

---

## 4. Regra contra mistura de níveis de verdade

Os cinco níveis acima podem coexistir na mesma Home, mas não podem ser apresentados de forma indistinguível.

Evitar:

```text
história real
+ cenário ilustrativo
+ Produto futuro
+ métrica projetada

apresentados como se todos fossem fatos operacionais equivalentes
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
4. **há responsabilidade, governança e limites na forma como a Guivos conecta ou pretende conectar esse ecossistema, conforme o estado operacional real;**
5. **existe uma arquitetura coerente de capacidades Guivos por trás da narrativa, sem confundir Produto com participante.**

A prova é distribuída pela narrativa.

Não deve existir uma única seção chamada `Provas`, `Clientes`, `Cases` ou `Nossos números` encarregada de legitimar toda a página.

---

## 6. Mapa executivo dos onze movimentos

| Movimento | Função predominante | Necessidade de prova | Conteúdo preferencial |
|---|---|---|---|
| 01 — Abrir o horizonte | tese | baixa | institucional permanente |
| 02 — Tornar capacidades e contribuições reconhecíveis | reconhecimento + realidade | média/alta | evidência real e exemplos reconhecíveis |
| 03 — Da fragmentação à continuidade | hipótese explicativa | média | relações reais quando disponíveis; cenário ilustrativo claramente distinguido quando necessário |
| 04 — Explicar o papel da Guivos | explicação institucional | média | fato governado + arquitetura de atuação |
| 05 — Explicar quem participa | explicação estrutural | baixa/média | fato governado + diversidade de tipos reais quando útil |
| 06 — Mostrar complementaridade sem fabricar match | demonstração relacional | alta | relação documentada ou cenário ilustrativo explicitamente não factual |
| 07 — Mostrar os Domínios de Evolução sem transformá-los em taxonomia visual obrigatória | amplitude contextual | média | repertório real diverso + vocabulário canônico JED-001..009 |
| 08 — Mostrar circulação de valor, supply e escala responsável | demonstração de reciprocidade | alta | evidência de valor contextual; métricas apenas quando interpretáveis |
| 09 — Construir confiança por autoridade, evidência e proteção | autoridade e limites | muito alta | governança, método, fontes, transparência, privacidade, relações e limites verificáveis |
| 10 — Materializar o ecossistema sem virar catálogo | explicação de ecossistema | alta para disponibilidade; média para arquitetura | fatos governados + estado operacional correto |
| 11 — Reabrir o horizonte para participação | navegação e ação | baixa | ação clara, contexto e autonomia |

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

A compreensão da Hero e sua continuidade pública não podem depender de dados pessoais, CNPJ, localização, voz/microfone, câmera, upload, login ou autenticação.

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

# 8. Movimento 02 — Tornar capacidades e contribuições reconhecíveis

## Pergunta implícita

> **“Isso já acontece no mundo real?”**

## Função editorial

Reconhecimento + realidade.

Esse movimento mostra que Organizações e Coletivos já criam ou habilitam conhecimento, Oportunidades reais, experiências, serviços, iniciativas, relações, recursos, infraestrutura e mobilização.

A Guivos ainda não precisa ser protagonista.

## Objeto da prova

> **a existência real das capacidades e iniciativas.**

## Evidências preferenciais

Quando disponíveis:

- uma Organização realizando algo concreto;
- um Coletivo mobilizando algo concreto;
- conhecimento produzido;
- Oportunidade real criada ou habilitada;
- experiência realizada;
- serviço, recurso, infraestrutura ou iniciativa observável;
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

# 9. Movimento 03 — Da fragmentação à continuidade

## Pergunta implícita

> **“E se aquilo que já existe pudesse ganhar mais contexto e continuidade?”**

## Função editorial

Hipótese explicativa.

O movimento apresenta continuidade sem afirmar causalidade garantida.

## Formas de sustentação

### Preferência A — relação real documentada

Uma sequência verdadeira pode demonstrar que:

- uma experiência revelou um novo Momento, interesse ou necessidade;
- conhecimento ampliou percepção;
- uma conexão tornou uma Oportunidade real visível;
- uma iniciativa encontrou capacidade complementar;
- um Mecanismo ajudou a remover uma barreira ou explicar como uma Possibilidade podia contribuir.

A narrativa deve documentar apenas aquilo que realmente pode ser sustentado.

### Preferência B — cenário ilustrativo

Quando não houver uma sequência real adequada, pode-se explicar:

```text
experiência
→ pode abrir contexto para aprendizado
→ que pode tornar uma conexão mais provável
→ que pode revelar uma Possibilidade, um Mecanismo ou uma Oportunidade real
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

# 10. Movimento 04 — Explicar o papel da Guivos

## Pergunta implícita

> **“Qual é, então, o papel da Guivos?”**

## Função editorial

Explicação institucional.

## Objeto da prova

O movimento não precisa provar grandeza.

Precisa demonstrar coerência entre a tese e a arquitetura governada.

Pode se apoiar em fatos governados sobre o papel da Guivos:

- ampliar percepção;
- organizar contexto;
- aproximar participantes e relações legítimas;
- tornar Possibilidades mais visíveis;
- tornar Oportunidades reais mais encontráveis quando houver base;
- ajudar a explicar Mecanismos quando necessário;
- apoiar continuidade;
- aproximar capacidades complementares;
- reduzir barreiras de acesso quando capacidades legítimas permitirem;
- preservar autonomia.

## Proteção

Não transformar arquitetura ou intenção em alegação de disponibilidade operacional universal.

A frase:

> `A Guivos conecta...`

precisa ser comunicada de forma compatível com o estágio real do ecossistema no momento da publicação.

## Estado de saída

> **“Entendo o papel que a Guivos pode exercer e ele é diferente de simplesmente intermediar oferta e demanda.”**

---

# 11. Movimento 05 — Explicar quem participa

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
- órgão ou instituição pública;
- fundação;
- associação formal;
- organização social;
- entidade religiosa, cultural ou profissional.

Exemplos possíveis de natureza coletiva:

- movimento;
- rede;
- grupo;
- comunidade compatível com o contrato de Coletivo;
- articulação territorial;
- coletivo profissional, esportivo, cultural, religioso, de causa, interesse ou prática compartilhada.

## Regra

> **Exemplo ajuda a reconhecer o tipo; exemplo não redefine o tipo.**

## Proteções

- `Comunidade` não vira Produto;
- comunidade não é automaticamente sinônimo de Coletivo;
- Organização não equivale a empresa privada;
- Coletivo não equivale a ONG;
- papel momentâneo não substitui tipo estrutural;
- pertencimento não equivale a representação;
- representação não equivale a autoridade irrestrita.

Essas distinções são princípios públicos. Seus mecanismos autenticados não pertencem a esta Home.

## Estado de saída

> **“Entendo quem participa e onde minha realidade pode se encaixar.”**

---

# 12. Movimento 06 — Mostrar complementaridade sem fabricar match

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

> Uma Organização pode possuir conhecimento; um Coletivo pode reunir pessoas interessadas; outra Organização pode possuir uma Oportunidade relacionada ou uma capacidade habilitadora.

Esse exemplo explica arquitetura de possibilidade, não prova que a Guivos já realizou essa composição.

Quando útil, `Direct Supply` e `Enabling Supply` podem ajudar a explicar se uma capacidade materializa diretamente uma Possibilidade/Próximo Passo ou remove uma barreira para a experiência principal. Essas classes permanecem explicativas de Research e não viram taxonomia canônica de Produto, participante, menu ou componente.

## Regra

> **Nunca criar uma falsa parceria ou um match fabricado para demonstrar complementaridade.**

## Estado de saída

> **“Consigo visualizar como capacidades diferentes poderiam se complementar sem que uma delas precise dominar as demais.”**

---

# 13. Movimento 07 — Mostrar os Domínios de Evolução sem transformá-los em taxonomia visual obrigatória

## Pergunta implícita

> **“Em quais grandes contextos da Journey essas capacidades e Possibilidades podem ganhar significado?”**

## Função editorial

Amplitude contextual.

## Fonte de verdade

Os nove **Domínios de Evolução** são o vocabulário canônico do Guivos Journey:

| ID | Domínio |
|---|---|
| JED-001 | Saúde e Bem-estar |
| JED-002 | Trabalho, Carreira e Estudos |
| JED-003 | Vida Financeira |
| JED-004 | Empreendedorismo e Projetos |
| JED-005 | Relacionamentos e Vida Social |
| JED-006 | Espiritualidade, Propósito e Valores |
| JED-007 | Viagens, Lazer, Cultura e Novas Experiências |
| JED-008 | Causas, Voluntariado e Contribuição |
| JED-009 | Organização e Equilíbrio da Vida |

Eles organizam **sobre o que** uma Journey pode tratar. Não determinam relevância individual e não significam score, diagnóstico, mérito, estágio de evolução ou obrigação de materialização em nove cards.

```text
DOMÍNIO
≠ OBJETIVO
≠ MOMENTO
≠ PRÓXIMO PASSO
≠ POSSIBILIDADE
≠ OPORTUNIDADE
≠ EXPERIÊNCIA
≠ EVOLUÇÃO
≠ SCORE
```

`Ainda estou descobrindo` permanece estado transversal legítimo quando não há clareza suficiente.

```text
AINDA ESTOU DESCOBRINDO
≠ DÉCIMO DOMÍNIO
```

O mesmo Domínio entre Pessoa, Organização e Coletivo não cria automaticamente match, relevância, autoridade ou compartilhamento de dados.

## Objeto da prova

Mostrar que capacidades, Possibilidades e formas de participação podem fazer sentido em diferentes áreas da vida, atuação coletiva e trajetória institucional, sem prescrever um destino humano único.

## Conteúdo preferencial

Poucos exemplos reais e suficientemente distintos podem provar amplitude melhor do que uma lista visual exaustiva.

A futura Home, se materializada por autorização posterior, não precisa transformar os nove Domínios em nove cards, nove menus ou classificação completa da vida.

## Cuidados adicionais

Em saúde, finanças, espiritualidade ou outros contextos sensíveis:

- não prometer resultado;
- não criar aconselhamento prescritivo na Home;
- não representar a Guivos como autoridade sobre qual caminho a Pessoa deve seguir;
- distinguir claramente participante, fonte e contexto.

## Regra editorial

> **Os Domínios ampliam vocabulário e contexto; não prescrevem caminho, não fabricam relevância e não obrigam uma taxonomia visual.**

## Estado de saída

> **“Consigo visualizar nossa capacidade fazendo sentido em contextos diferentes sem reduzir evolução a uma classificação rígida.”**

---

# 14. Movimento 08 — Mostrar circulação de valor, supply e escala responsável

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
- diversidade real de contextos conectados;
- Direct Supply ou Enabling Supply quando essa distinção explicar materialmente a contribuição ou a remoção de barreira.

## Métricas

Métricas podem ser utilizadas somente quando responderem uma pergunta relevante.

Exemplos de perguntas legítimas:

- o que está sendo contado?
- em qual período?
- em qual território?
- qual definição de participante?
- qual definição de Oportunidade, experiência ou relação?
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

A escala pode ser comunicada como **arquitetura capaz de acomodar diversidade e expansão**, desde que não seja confundida com atuação já materializada.

## Regras adicionais

```text
MAIS USUÁRIOS
≠ MAIS EVOLUÇÃO

MAIS MEMBROS
≠ COLETIVO MELHOR

MAIS ANÚNCIOS
≠ ORGANIZAÇÃO MAIS RELEVANTE

MAIS DADOS
≠ MAIS COMPREENSÃO

MAIS RECEITA
≠ MAIS IMPACTO

POSIÇÃO COMERCIAL
≠ RELEVÂNCIA
```

Participação não deve ser explicada como perseguição a pontos, créditos ou recompensas. Valor pode ser econômico, institucional, humano, social, contextual, educacional ou relacional, conforme a natureza da relação.

## Regra

> **Escala é ampliação responsável do campo de possibilidades; volume é apenas uma das dimensões possíveis de medição.**

## Estado de saída

> **“Entendo por que participar pode fazer sentido para diferentes partes e por que diversidade importa mais que volume isolado.”**

---

# 15. Movimento 09 — Construir confiança por autoridade, evidência e proteção

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
- critérios de uso de Intelligence;
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

> **Intelligence apoia compreensão. Não governa a decisão humana.**

E deve tornar possível compreender:

```text
o que sabemos
o que foi declarado
o que foi verificado
o que inferimos
o que ainda não sabemos ou permanece contestado
```

A evidência pública pode explicar princípios de autoridade, finalidade, bilateralidade, proteção, contestação e saída. Ela não deve expor RBAC, menus internos, permissões técnicas, payloads, logs, domínios da IA autenticada ou dados privados para “provar” governança.

## Estado de saída

> **“Há critérios, responsabilidade e limites compreensíveis por trás da proposta.”**

---

# 16. Movimento 10 — Materializar o ecossistema sem virar catálogo

## Pergunta implícita

> **“Existe uma arquitetura coerente por trás dessa visão?”**

## Função editorial

Explicação do ecossistema e de suas capacidades.

## Fonte de verdade

A arquitetura governada vigente é:

```text
GUIVOS

├── EXPERIENCE LAYER
│   └── Guivos Journey
│       → experiência e continuidade do participante
│
└── PRODUTOS ESPECIALIZADOS
    ├── Guivos Travel
    ├── Guivos Mall
    ├── Guivos Media
    ├── Guivos Business
    ├── Guivos Ads
    └── Guivos Intelligence
        → Produto Especializado transversal
        → Intelligence Layer do ecossistema
```

`Guivos Journey` não deve ser tratado como Produto comercial equivalente aos Produtos Especializados.

`Guivos Business` não é “o produto das Organizações”. Uma Organização pode participar do ecossistema sem utilizar ou contratar Business.

`Guivos Intelligence` é o **Produto Especializado transversal / Intelligence Layer**. Sua unidade superior de valor é compreensão útil e contextualizada.

```text
COMPREENDER
≠ DECIDIR

INTELLIGENCE
≠ IA
≠ LLM
≠ DASHBOARD
≠ GRAFO
≠ AUTORIDADE SOBRE OUTROS PRODUTOS OU PARTICIPANTES
```

## Função da prova

Aqui a prova não é mostrar uma grade de logos de Produtos.

É demonstrar **coerência arquitetural** e, quando houver publicação futuramente autorizada, **verdade de estado**.

Para cada capacidade apresentada, deve ser possível diferenciar:

- existe como arquitetura governada;
- está em desenvolvimento;
- está disponível;
- está disponível apenas em determinado contexto;
- depende de futura ativação.

## Proteções

- Organização não equivale a Business;
- Pessoa não equivale a Journey;
- Coletivo não possui Produto obrigatório homônimo;
- Intelligence não é produto de vigilância nem autoridade sobre participantes;
- Produto futuro não pode parecer funcionalidade disponível;
- quantidade de Produtos não é prova de maturidade;
- topologia conceitual não é obrigação de cards equivalentes.

## Conteúdo preferencial

Cada Produto ou camada, quando necessário, deve responder:

> **“O que esta capacidade torna possível dentro da tese que já foi compreendida?”**

Não responder primeiro:

- lista de features;
- plano;
- preço;
- integração técnica;
- catálogo comercial.

## Estado de saída

> **“Entendo que existe uma arquitetura única por trás da visão e que os Produtos são capacidades da Guivos, não a definição dos participantes.”**

---

# 17. Movimento 11 — Reabrir o horizonte para participação

## Pergunta vigente

> **Como podemos continuar daqui?**

## Função editorial

Navegação e ação de baixo compromisso.

## Necessidade de prova

Baixa.

A narrativa já deve ter construído contexto suficiente.

Esse movimento precisa provar principalmente **clareza, autonomia e igual legitimidade conceitual dos dois caminhos**.

## Conteúdo

Dois caminhos conceituais distintos e equivalentes em legitimidade:

- **Descobrir como uma Organização pode participar**;
- **Descobrir como um Coletivo pode participar**.

Arquitetura vigente:

```text
HOME PÚBLICA — ORGANIZAÇÕES E COLETIVOS
                ↓
        narrativa compartilhada
                ↓
       M11 — continuidade
          ↙             ↘
 ORGANIZAÇÃO            COLETIVO
     ↓                    ↓
continuidade          continuidade
conceitual própria    conceitual própria
```

Esses caminhos permanecem conceituais até que destinos operacionais sejam formalmente autorizados e comprovados.

## Regra

O clique não significa, por obrigação:

- cadastro;
- compra;
- contratação;
- onboarding;
- criação de conta institucional;
- acesso a tela autenticada;
- transferência para Guivos Business;
- formulário comercial.

A experiência autenticada posterior, quando vier a ser materializada e autorizada, preservará arquitetura própria. Seus jobs, autoridade, IA, superfícies, menus, RBAC e wireframes não são transportados para esta Home.

## Evitar

- `Cadastre sua empresa agora` como fechamento obrigatório;
- `Crie seu coletivo`;
- `Comece a vender`;
- `Alcance nossos usuários`;
- CTA de Organização visualmente superior ao de Coletivo sem razão governada;
- Organização como caminho comercial e Coletivo como caminho social;
- formulário comercial como única saída.

## Estado de saída

> **“Entendi como posso aprofundar a participação sem ser pressionado a converter e sem que meu tipo de participante determine um Produto obrigatório.”**

---

## 18. Relação entre prova e as sete macroexperiências

`GKR-UX-HOME-OC-NARR-001 v0.2.0` organiza os onze movimentos em sete macroexperiências. Este SYS aprofunda a necessidade de prova dentro delas; não altera o mapa narrativo.

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
- Direct/Enabling Supply apenas quando explicativamente úteis;
- nove Domínios como vocabulário canônico, não taxonomia visual obrigatória.

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
- alta clareza de ação, autonomia e igual legitimidade.

Regra:

> **NARR organiza progressão. SYS aprofunda prova. Nenhum dos dois altera sozinho a autoridade do Master vigente.**

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

> **Nunca construir uma parceria que o contrato real não sustenta.**

A relação, quando bilateral, não cria propriedade sobre Coletivo nem acesso automático aos dados de seus membros.

---

## 21. Patrocínio, publicidade e interesse comercial

Uma relação paga, patrocinada ou comercial não deve ser usada como prova neutra sem identificação adequada.

Quando materialmente relevante, distinguir:

- conteúdo orgânico;
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

Patrocínio ou posição comercial não compram relevância contextual nem aparência de prova institucional orgânica.

---

## 22. Dados, Intelligence e prova

A Home não pode sugerir que a Guivos conhece profundamente Pessoas porque possui grande volume de dados.

Guivos Intelligence deve ser explicada como **Produto Especializado transversal / Intelligence Layer**, capaz de apoiar compreensão de contexto de forma responsável sem governar a decisão humana.

Quando dados forem utilizados como evidência, distinguir:

- dado pessoal;
- dado declarado;
- dado observado;
- dado agregado;
- inferência;
- evidência externa;
- informação desconhecida ou contestada.

Não comunicar que Organizações recebem automaticamente dados de Pessoas ou membros de Coletivos.

Não transformar inferência em fato.

Não transformar precisão estatística em autoridade moral sobre a trajetória humana.

A Home pública pode explicar princípios de dados, evidência e Intelligence; não deve expor dados privados, payloads, logs, permissões, RBAC ou superfícies autenticadas como prova.

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
- identificação de Organização responsável por determinada evidência;
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
- Intelligence;
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
- mockups de Produto apresentados como disponibilidade;
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
- eventos ou Oportunidades quando realmente relevantes à narrativa.

Regra herdada:

> **A Guivos é estável; o ecossistema está vivo.**

A Home não se torna um feed institucional de parceiros ou notícias.

---

## 28. Guivos Media como possível fonte editorial

Quando legitimamente autorizado e operacional, Guivos Media pode funcionar como memória e supply editorial de evidências e histórias.

Isso não significa que todo conteúdo de Media seja prova adequada para a Home.

Para chegar à Home, o conteúdo precisa cumprir uma função narrativa específica:

- tornar realidade reconhecível;
- demonstrar complementaridade;
- mostrar amplitude;
- sustentar valor;
- demonstrar autoridade;
- explicar continuidade.

Relação de autoridade:

```text
HOME O/C
→ tese, narrativa, seleção e função da página

GUIVOS MEDIA
→ origem, integridade, contexto e classificação editorial do conteúdo que produz
```

Ser personagem de conteúdo não transforma uma entidade em parceira, cliente ou participante ativo da Guivos.

Conteúdo patrocinado deve permanecer claramente identificável e sujeito às autoridades aplicáveis de Media e Ads.

---

## 29. Responsividade do significado

Desktop e mobile podem exibir quantidades diferentes de evidência simultaneamente em uma futura materialização autorizada.

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

Mobile pode reduzir simultaneidade; não pode reduzir significado, verdade ou qualificação da evidência.

---

## 30. Progressive disclosure da evidência

Nem todo método, fonte ou detalhe precisa ocupar o primeiro nível visual.

É legítimo trabalhar, em eventual materialização autorizada, com:

```text
afirmação compreensível
→ sinal de evidência
→ contexto resumido
→ aprofundamento / fonte / metodologia
```

Desde que a informação essencial não seja escondida de modo enganoso.

A prova pode ser aprofundável; não pode ser opaca.

Essa arquitetura editorial não autoriza agora componente, interação ou layout.

---

## 31. Prova e acessibilidade

Evidência não pode depender exclusivamente de:

- imagem;
- animação;
- hover;
- vídeo sem transcrição;
- cor;
- interação por arraste.

Uma Pessoa utilizando leitor de tela, teclado, redução de movimento ou conexão limitada deve continuar entendendo:

- qual afirmação está sendo feita;
- qual evidência a sustenta;
- qual é seu contexto.

Acessibilidade é parte da integridade da prova, não acabamento posterior.

---

## 32. Anti-padrões gerais

Rejeitar uma futura materialização, somente se e quando autorizada, se ela utilizar prova para produzir qualquer uma destas leituras:

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

apresentado de forma que pareça um case real.

### `Organização usa Business`

convertendo tipo estrutural de participante em Produto obrigatório.

### `Coletivo = comunidade da Guivos`

criando propriedade, Produto ou pertencimento não governados.

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

Se não, ela está claramente apresentada como possibilidade ilustrativa e sem fabricar match?

### Movimento 07

Os nove Domínios ampliam contexto sem virar score, prescrição, match ou taxonomia visual obrigatória?

### Movimento 08

Os números demonstram valor ou apenas tamanho?

### Movimento 09

Há razões verificáveis para confiar ou apenas autodeclaração institucional?

### Movimento 10

A arquitetura `Experience Layer / Produtos Especializados / Intelligence Layer` está clara sem transformar Produtos em catálogo ou disponibilidade fictícia?

### Movimento 11

A continuidade preserva autonomia, igual legitimidade entre Organização e Coletivo e destinos ainda conceituais, ou utiliza toda a prova anterior para pressionar conversão?

---

## 34. Matriz de risco de prova

| Risco | Movimentos mais sensíveis | Proteção |
|---|---|---|
| falsa causalidade | 03, 06, 08 | linguagem probabilística + consequência observável |
| falsa relação | 02, 06, 09 | proveniência e natureza da relação |
| falsa escala | 08, 10 | métricas contextualizadas + estado operacional |
| participante = audiência | 06, 08, 11 | agência, reciprocidade e autonomia |
| Produto = participante | 05, 10 | contrato `quem ≠ como` |
| Intelligence = acesso a Pessoas | 08, 09, 10 | privacidade, finalidade e distinção de dados |
| prova = logo | 02, 09 | contexto da relação |
| ilustração = evidência | 03, 06 | classificação editorial explícita |
| arquitetura = disponibilidade | 04, 10 | estado operacional verificável |
| Domínio = relevância / match | 06, 07 | contexto + autoridade + ausência de inferência automática |
| volume = evolução | 08 | métricas de significado e limites |
| continuidade conceitual = rota operacional | 11 | separar intenção pública de destino autenticado |

---

## 35. Proveniência do antigo P3 e critério atual de integridade

No checkpoint original de 11/08/2026, `OC-GAP-03` foi considerado **resolvido em princípio** quando uma futura equipe de Design conseguia responder, sem inventar estratégia:

1. qual movimento precisa de prova forte e qual pode funcionar por tese;
2. o que cada evidência está tentando provar;
3. quando uma história pode ser usada;
4. quando um cenário precisa ser marcado como ilustrativo;
5. quando uma métrica é admissível;
6. por que um logo isolado não é autoridade;
7. como provar complementaridade sem inventar relações;
8. como mostrar valor sem transformar volume em evolução;
9. como demonstrar confiança por governança, método e limites;
10. como apresentar Produtos respeitando verdade operacional;
11. como operar com poucas provas reais no estágio inicial.

Naquele checkpoint, a sequência era registrada como:

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

Esse quadro permanece como **proveniência histórica**, não como estado operacional atual.

Depois das reconstruções e reauditorias posteriores:

```text
P3 / OC-GAP-03
→ proveniência histórica deste detalhe especializado

P4 / OC-GAP-04
→ não é próximo passo operacional vigente deste documento

GKR-UX-HOME-OC-MASTER-001 v1.0.0
→ autoridade de consumo atual

GKR-UX-HOME-OC-NARR-001 v0.2.0
→ detalhe narrativo reconciliado

GKR-UX-HOME-OC-NAV-001 v0.2.0
→ detalhe navegacional reconciliado

GKR-UX-HOME-OC-SYS-001 v0.2.0
→ detalhe de conteúdo e prova reconciliado

AUDITORIA INTEGRAL DO GKR
→ EM CURSO

MATERIALIZAÇÃO VISUAL NOVA
→ NÃO AUTORIZADA
```

O critério atual de integridade do SYS é preservar conhecimento suficiente para que conteúdo, prova e evidência possam ser avaliados sem inventar estratégia, **sem converter essa prontidão documental em permissão de Design**.

---

## 36. Responsabilidades especializadas ainda preservadas fora deste SYS

Historicamente, o P4 reunia questões como:

- quais trechos do Documento Mestre são copy obrigatória;
- quais trechos são apenas matéria-prima estratégica;
- o que Design pode condensar;
- o que não pode desaparecer;
- qual copy ainda precisa de lapidação;
- critérios formais de aceite do primeiro wireframe;
- instruções consolidadas para ferramentas generativas;
- pacote final de fontes que Design deve receber.

Essas questões pertencem hoje aos respectivos artefatos especializados e à história dos checkpoints. Sua existência **não autoriza** produzir ou retomar agora Handoff, wireframe, Figma, SVG, protótipo, UI, UXA-102/V5 ou implementação.

Qualquer futura retomada de materialização exigirá novo ato governado posterior à auditoria integral e reconciliação com o Master e demais autoridades então vigentes.

---

## 37. Contrato final de conteúdo e prova

> **A Home Pública de Organizações e Coletivos deve construir credibilidade distribuindo evidência de acordo com a função de cada movimento. Realidade prova que capacidades existem; relações reais ou cenários explicitamente ilustrativos ajudam a compreender complementaridade; métricas só sustentam afirmações quando possuem contexto; governança, proveniência e limites sustentam confiança; arquitetura e estado operacional sustentam Journey, Produtos Especializados e Intelligence em seus papéis corretos. Em nenhum ponto a Guivos deve substituir ausência de prova por logos, números, histórias, geografias, relações ou capacidades simuladas.**

Teste final:

> **Se retirarmos o prestígio visual de marcas, números e efeitos, a afirmação ainda continua verdadeira e demonstrável? Se não continuar, a prova escolhida está mascarando uma lacuna em vez de resolvê-la.**

Teste adicional de fronteira:

> **Se uma prova pública só puder ser compreendida expondo dados privados, RBAC, menus, logs, IA autenticada ou fluxo interno, ela está tentando demonstrar a coisa certa pela superfície errada.**

---

## 38. Limites, estado atual e relação com o Lote E

Este documento:

- não altera os onze movimentos do Documento Mestre;
- não altera as sete macroexperiências reconciliadas do NARR;
- não altera a arquitetura de Header, Hero e CTAs reconciliada do NAV;
- não escolhe parceiros, cases, histórias, métricas ou países;
- não autoriza uso público de nenhuma relação existente;
- não define política jurídica de consentimento ou licenciamento de conteúdo;
- não cria wireframe;
- não cria Figma;
- não cria SVG;
- não cria protótipo;
- não cria UI;
- não inicia UXA-102/V5;
- não retoma Product Engineering;
- não inicia implementação;
- não materializa destinos operacionais para Organização ou Coletivo;
- não importa IA, RBAC, menus, jobs ou superfícies autenticadas para a Home pública.

Com a reconciliação desta versão:

- o núcleo de classes de conteúdo, verdade editorial, hierarquia de prova, causalidade, métricas, logos, depoimentos, patrocínio, fallback e verdade operacional permanece preservado;
- os onze movimentos foram alinhados ao Master v1.0.0 e ao NARR v0.2.0;
- o Movimento 07 passa a usar os nove Domínios de Evolução canônicos sem obrigação visual;
- o Movimento 10 usa `Journey = Experience Layer`, Produtos Especializados e `Intelligence = Produto Especializado transversal / Intelligence Layer`;
- o Movimento 11 usa `Como podemos continuar daqui?` e preserva Organização / Coletivo como continuidades conceituais distintas e de igual legitimidade;
- a fronteira pública × autenticada foi reforçada sem importar superfícies protegidas;
- o antigo P3 → P4 permanece história de construção, não sequência operacional vigente;
- este documento não fecha automaticamente SYS/HANDOFF restantes nem o Lote E global.

Estado desta frente:

> **CONTENT / PROOF / EVIDENCE DETAIL RECONCILIADO — `GKR-UX-HOME-OC-SYS-001 v0.2.0` — PRESERVADO PARA APROFUNDAMENTO — MATERIALIZAÇÃO VISUAL NÃO AUTORIZADA DURANTE A AUDITORIA INTEGRAL.**

Próximos incrementos do Lote E devem ser determinados pela matriz de reconciliação do corpus, não pela antiga sequência de prontidão P3 → P4.