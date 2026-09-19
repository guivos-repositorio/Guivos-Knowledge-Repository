---
id: GKR-UX-HOME-MALL-MASTER-001
title: Home Pública — Guivos Mall — Documento Mestre
status: active
version: 1.1.0
owner: Experience Architecture
last_updated: 2026-09-19
parents:
  - GKR-UX-HOME-MASTER-001
  - GPA-002
  - GKR-STATE-001
related:
  - GPA-002
  - GPA-003
  - GPA-004
  - GEM-005
  - GKR-UX-HOMES-DESIGN-SOURCE-READINESS-REMEDIATION-001
normative: false
maturity: source_ready_for_external_design_manual_first_ai_optional
---

# Home Pública — Guivos Mall — Documento Mestre

## 1. Finalidade e autoridade

Este documento consolida a arquitetura estratégica, narrativa e funcional da **Home Pública do Guivos Mall**.

A Home do Mall é uma apresentação pública especializada de uma capacidade da Guivos. Ela deve preservar a percepção da Guivos como um ecossistema maior do que a soma de seus produtos e, ao mesmo tempo, permitir que a experiência se torne comercial de forma natural quando a pessoa estiver pronta para explorar produtos, serviços, Gift Cards, ofertas e demais possibilidades disponíveis.

Este documento governa **somente a Home do Guivos Mall**.

Ele não materializa wireframe, UI, protótipo, frontend, backend ou implementação e não autoriza automaticamente nenhuma dessas etapas.

## 2. Premissa central

> **O Guivos Mall não é a Guivos transformada em e-commerce. É uma das capacidades do ecossistema Guivos, tornando produtos, serviços, presentes e outras possibilidades comercialmente acessíveis quando fizerem sentido na vida das pessoas.**

A Home precisa equilibrar quatro dimensões:

```text
identidade Guivos
+
descoberta
+
comércio
+
confiança
```

O comércio é parte essencial da experiência, mas não deve ser a primeira ou única percepção da página.

## 3. Papel da Home

A Home deve apresentar o Mall antes de simplesmente expor um catálogo.

Sua progressão conceitual é:

```text
Existe algo que pode fazer sentido para este momento
↓
O Guivos Mall reúne possibilidades concretas para isso
↓
A pessoa pode explorar, entender e escolher com autonomia
```

A Home deve ajudar quem quer descobrir sem dificultar quem já sabe o que procura.

> **Descoberta para quem quer explorar. Busca direta para quem já sabe o que procura.**

## 4. Relação entre Guivos e Mall

A pessoa não deve sentir que saiu da Guivos e entrou em uma loja independente.

```text
GUIVOS
→ amplia e conecta possibilidades

GUIVOS MALL
→ torna produtos, serviços, presentes
  e possibilidades comerciais acessíveis
  dentro desse ecossistema
```

O Mall deve possuir identidade especializada suficiente para ser reconhecível, sem se transformar em uma marca desconectada da Guivos.

> **O Mall é uma capacidade da Guivos. Não uma Guivos separada.**

## 5. Pergunta-mãe

A pergunta que governa a Home é:

# O que pode fazer parte do seu próximo momento?

Ela deve comportar uma necessidade, um desejo, uma compra planejada, uma descoberta, um produto, um serviço, uma experiência ou um presente sem reduzir a primeira relação com o Mall a “o que você quer comprar?”.

## 6. Hero

### Headline

> **O que pode fazer parte do seu próximo momento?**

### Apoio

> **Produtos, serviços e presentes para diferentes momentos da vida — para descobrir, escolher e compartilhar.**

### CTAs iniciais

- **Explorar o Mall**;
- **Ver Gift Cards**.

O Hero não deve ser dominado por desconto, preço, pontos, publicidade, campanha promocional ou um produto específico.

Esses elementos podem aparecer posteriormente na Home.

> **O Hero define o significado permanente do Mall; campanhas comerciais são camadas temporárias.**

## 7. Header da Home

O Header precisa preservar simultaneamente a identidade Guivos e a objetividade esperada de um ambiente comercial.

Estrutura conceitual:

```text
GUIVOS | MALL

Shopping
Gift Cards

Buscar
Perfil
Carrinho
```

### Guivos

Retorna à Home principal da Guivos.

### Mall

Identifica claramente a especialidade atual.

### Shopping

Direciona para o universo comercial de produtos do Mall.

### Gift Cards

Direciona para o universo de vouchers, serviços, experiências e presentes.

### Buscar

É uma função estrutural da experiência comercial e deve permitir acesso direto para quem já sabe o que procura.

### Perfil

Permanece como acesso global. O Header pode exibir informação resumida da conta, inclusive o saldo de pontos quando essa informação já fizer parte do componente global de perfil.

### Carrinho

Permanece acessível no Header, sem que sua arquitetura ou comportamento façam parte deste documento.

> **Presença no Header não significa que Perfil ou Carrinho pertençam ao escopo funcional desta Home.**

## 8. Fronteira rígida de escopo

Este documento termina na Home.

```text
HOME DO MALL
→ apresenta uma possibilidade
→ a pessoa escolhe avançar
→ outra experiência começa
```

Estão deliberadamente fora do escopo atual:

- página de detalhe de produto;
- página de Perfil;
- arquitetura do Carrinho;
- Checkout;
- pedidos;
- fluxos pós-compra;
- especificação operacional interna das experiências que começam após a saída da Home.

A Home pode direcionar para essas experiências, mas não as define.

## 9. Arquitetura narrativa em 11 movimentos

A Home é governada pela seguinte sequência:

```text
01 — ABRIR O HORIZONTE
O que pode fazer parte do seu próximo momento?

02 — VIDA REAL
necessidades, desejos, momentos e experiências

03 — APRESENTAR O MALL
uma capacidade comercial da Guivos

04 — DUAS PORTAS ATUAIS
Shopping | Gift Cards

05 — SHOPPING
busca + categorias + produtos + ofertas

06 — PREÇO E PONTOS
R$ + pontos quando elegível

07 — DESCOBERTA
relevância sem pressão

08 — GIFT CARDS
serviços e experiências

09 — GIFT CARD GUIVOS
presente + autonomia

10 — PROVA E CONFIANÇA
inventário + marcas + transparência + autoridade

11 — ECOSSISTEMA E ESCOLHA
Mall como parte da Guivos + CTAs finais
```

## 10. Movimento 01 — Abrir o horizonte

A primeira percepção é possibilidade, não compra.

A Home deve provocar a leitura:

> **“Talvez exista aqui algo que faça sentido para o que estou vivendo, procurando ou querendo agora.”**

Ela não deve abrir como um banner promocional genérico nem como uma grade de produtos desconectada da Guivos.

## 11. Movimento 02 — Reconhecer a vida real

Mensagem de direção:

> **Algumas coisas resolvem. Outras facilitam. Outras simplesmente fazem parte de um momento.**

A Home reconhece que a vida envolve necessidades, desejos, objetos, serviços, experiências e relações.

Exemplos narrativos possíveis:

- um celular pode conectar;
- um notebook pode apoiar trabalho ou aprendizado;
- um móvel pode transformar um espaço;
- um eletrodoméstico pode facilitar a rotina;
- um automóvel pode ampliar mobilidade;
- um serviço pode fazer parte de uma experiência;
- um presente pode marcar uma relação.

Proteção conceitual:

> **Produto não é evolução. Produtos e serviços podem fazer parte da vida e das experiências das pessoas.**

A Home não deve romantizar consumo nem afirmar que adquirir bens representa evolução humana.

## 12. Movimento 03 — Apresentar o Guivos Mall

Direção de título:

# Um lugar para encontrar o que pode fazer sentido agora.

Definição pública de trabalho:

> **O Guivos Mall reúne produtos, serviços, Gift Cards e outras possibilidades comerciais dentro do ecossistema Guivos.**

Nesse ponto, a pessoa deve compreender o papel da especialidade e sua relação com a Guivos maior.

## 13. Movimento 04 — Apresentar as duas portas atuais

Direção:

# Escolha como quer explorar.

### Shopping

> **Produtos para diferentes necessidades, desejos e momentos.**

O Shopping comporta o marketplace comercial do Mall, incluindo categorias como tecnologia, celulares, eletrônicos, eletrodomésticos, móveis, cama, mesa e banho, automóveis e demais itens efetivamente disponíveis.

### Gift Cards

> **Serviços, experiências e possibilidades para usar ou presentear.**

A área inclui Gift Cards de terceiros disponíveis no Mall e o próprio Gift Card Guivos.

Proteção de evolução do produto:

> **Shopping e Gift Cards são as duas portas atuais do Mall; não constituem limite definitivo para todas as futuras capacidades da especialidade.**

## 14. Movimento 05 — Shopping

Direção:

# Encontre o que procura. Descubra também o que pode fazer sentido.

Nesse momento, a Home pode assumir deliberadamente comportamentos comerciais conhecidos.

Podem aparecer na Home:

- busca;
- grandes categorias;
- produtos reais;
- ofertas;
- novidades;
- destaques;
- marcas;
- preços;
- preços em pontos quando elegíveis.

> **A narrativa diferencia o Mall. A compra deve permanecer simples e familiar.**

A Guivos não precisa reinventar comportamentos universais de e-commerce para demonstrar diferenciação.

## 15. Categorias e territórios de descoberta

A Home não deve ser transformada imediatamente em uma taxonomia gigantesca de pequenos acessos.

Pode trabalhar grandes territórios de descoberta, por exemplo:

```text
Tecnologia
Casa
Mobilidade
Lazer
Estilo de vida
Outras possibilidades
```

Esses territórios não substituem a taxonomia comercial real.

Exemplo:

```text
Tecnologia
→ Celulares
→ Computadores
→ TVs
→ Áudio
→ Eletrônicos

Casa
→ Eletrodomésticos
→ Móveis
→ Cama, Mesa e Banho
→ Utilidades
→ Decoração

Mobilidade
→ Automóveis
→ Acessórios
→ demais categorias aplicáveis
```

Busca direta e acesso a categorias continuam disponíveis para quem já sabe o que procura.

## 16. Movimento 06 — Produtos, preço e pontos

O Mall admite aquisição em dinheiro e utilização de pontos nas ofertas em que cada modalidade estiver efetivamente disponível.

Exemplo conceitual:

```text
Smartphone XYZ

R$ 1.899,00
ou
18.990 pts
```

Se apenas dinheiro estiver disponível, somente o preço monetário deve aparecer. Se determinada modalidade não for elegível para uma oferta, ela não deve ser simulada ou exibida.

Este documento não cria pagamento híbrido `dinheiro + pontos`, taxa de conversão, regras de emissão, expiração, transferência ou qualquer outra mecânica econômica não autorizada em autoridade própria.

### Saldo da pessoa

O saldo total de pontos **não deve ser repetido nos cards ou no corpo da Home** quando já estiver disponível junto ao componente global de perfil no Header.

```text
PERFIL
→ quanto a pessoa possui

PRODUTO / OFERTA
→ quanto custa em dinheiro
→ quanto custa em pontos, quando elegível
```

Regra:

> **Saldo de pontos é informação global da conta; preço em pontos é informação específica da oferta.**

## 17. Natureza dos pontos e relação com Guivos Business

Os pontos possuem função transacional e de benefício. Eles não representam evolução pessoal.

A conexão comercial vigente é:

```text
EMPRESA
↓
GUIVOS BUSINESS
↓
PROGRAMA DE PONTOS
↓
PESSOA RECEBE O BENEFÍCIO
↓
pode utilizar em ofertas elegíveis do
MALL / TRAVEL
↓
A PESSOA ESCOLHE COMO UTILIZAR
```

Neste fluxo comercial específico, utiliza-se deliberadamente **Empresa** para identificar a empresa cliente do Guivos Business e evitar confusão com a ontologia ampla de **Organização** e **Coletivo** da Guivos.

Essa escolha terminológica é local ao fluxo comercial e não substitui a ontologia global:

```text
Organização
= tipo estrutural amplo de participante

Empresa
= termo utilizado no contexto comercial específico
  do Guivos Business e do Programa de Pontos
```

Proteções:

```text
mais pontos
≠
mais evolução
```

```text
Programa de Pontos
≠
Gift Card Guivos
```

A empresa pode conceder o benefício; a pessoa preserva a decisão sobre como utilizar seus pontos dentro das possibilidades elegíveis do programa.

## 18. Personalidade comercial

A personalidade comercial do Mall deve ser:

> **relevante, clara, convidativa e confiável — sem pressão desnecessária.**

O Mall pode trabalhar preço, descontos, ofertas, campanhas, condições comerciais, benefícios, pontos e publicidade.

Isso não deve criar uma identidade baseada em urgência permanente ou manipulação.

Princípio:

> **Preço claro. Oportunidade visível. Decisão preservada.**

## 19. Promoções e campanhas

Promoções e campanhas são legítimas e podem fazer parte da Home.

A preferência é por linguagem factual, como:

- `20% de desconto`;
- `Condição especial`;
- `Oferta válida até 15 de agosto`.

Expressões de urgência podem existir somente quando verdadeiras e necessárias, mas não devem constituir a voz permanente do Mall.

```text
IDENTIDADE DO MALL
permanece

+

CAMPANHA COMERCIAL
muda
```

Black Friday, Natal, datas especiais ou campanhas temáticas podem alterar temporariamente a superfície comercial sem redefinir o significado da especialidade.

## 20. Movimento 07 — Descoberta e relevância

Direção:

# Nem toda escolha começa com uma busca.

O Mall pode tornar possibilidades relevantes mais encontráveis.

Guivos Journey e Guivos Intelligence podem apoiar contexto e relevância quando houver base legítima, consentimento e regras aplicáveis.

A relação desejada é:

```text
contexto legítimo
↓
relevância
↓
possibilidade
↓
pessoa escolhe
```

Não:

```text
qualquer comportamento
↓
pressão comercial
↓
compra
```

A inteligência deve melhorar relevância, não transformar toda informação da jornada em gatilho de venda.

## 21. Transparência de destaque, recomendação, oferta e publicidade

Quatro conceitos devem permanecer semanticamente diferentes:

```text
EM DESTAQUE
→ curadoria ou destaque geral

RECOMENDADO PARA VOCÊ
→ personalização ou relevância contextual

OFERTA
→ condição comercial

PATROCINADO
→ exposição decorrente de relação comercial
```

Consequências:

- patrocínio não pode comprar aparência de recomendação orgânica;
- uma oferta não é automaticamente uma recomendação;
- conteúdo em destaque não é necessariamente personalizado;
- publicidade deve permanecer identificada.

Guivos Ads pode ampliar visibilidade, mas não deve comprar confiança ou mascarar exposição paga como relevância espontânea.

## 22. Movimento 08 — Gift Cards

Direção:

# Algumas possibilidades não vêm dentro de uma caixa.

A Home introduz uma dimensão do Mall que ultrapassa mercadorias físicas.

Entre os Gift Cards já previstos na oferta do Mall estão vouchers de serviços e experiências como cinema, Uber, iFood, Netflix e outros parceiros efetivamente disponíveis.

Mensagem de apoio:

> **Para usar. Para experimentar. Para compartilhar.**

A apresentação deve permitir tanto a intenção direta — por exemplo, buscar um Gift Card específico — quanto a descoberta por intenção de presentear.

## 23. Movimento 09 — Gift Card Guivos

O Gift Card Guivos possui papel próprio e deve receber protagonismo diferenciado dentro da área de Gift Cards.

Direção principal:

# Presenteie com possibilidades.

Mensagem central:

> **Você escolhe presentear. Quem recebe continua livre para escolher.**

Seu território semântico é:

```text
PRESENTE
↓
POSSIBILIDADE
↓
AUTONOMIA
↓
ESCOLHA
```

O Gift Card Guivos não deve ser apresentado como pontos, evolução, gamificação ou simples mecanismo de acúmulo de saldo.

Este documento não presume regras específicas de valor, resgate, validade, transferência ou cobertura do Gift Card que não estejam autorizadas em produto próprio.

## 24. Movimento 10 — Prova — faceta de evidência

A Home precisa demonstrar que o Mall é concreto, não apenas afirmar que ele existe.

As fontes principais de prova são:

```text
OFERTA REAL
+
DIVERSIDADE REAL
+
MARCAS / PARCEIROS REAIS
+
INTEGRAÇÕES REAIS
```

A Home pode mostrar produtos reais de diferentes categorias, Gift Cards existentes, marcas efetivamente disponíveis, parceiros formalmente reconhecidos e modalidades de pontos efetivamente aplicáveis.

A amplitude deve ser demonstrada pela realidade disponível, não por números de escala inventados.

## 25. Marcas e parceiros

A Home deve distinguir duas condições:

```text
MARCA DISPONÍVEL
→ produtos daquela marca podem ser encontrados no Mall

PARCEIRO
→ existe relação formal com a Guivos
```

A presença de produtos de uma marca no catálogo não autoriza a Guivos a apresentá-la automaticamente como parceira institucional.

Essa distinção é parte da política de confiança e precisão da Home.

## 26. Movimento 10 — Confiança — faceta de proteção

Direção:

# Escolher também depende de confiar.

A Home pode demonstrar compromissos como:

### Informações claras

Preço, condição e disponibilidade devem ser compreensíveis antes da decisão.

### Origem identificada

A pessoa deve conseguir compreender quem está oferecendo aquilo que encontra.

### Publicidade transparente

Conteúdos patrocinados permanecem identificados.

### Autonomia

Recomendações ampliam possibilidades; não substituem a decisão da pessoa.

A Home não precisa se tornar uma página jurídica, de suporte ou de políticas operacionais. Ela comunica o compromisso; detalhes pertencem às experiências apropriadas.

Devem ser evitadas alegações genéricas como `100% seguro`, `melhor preço`, `maior marketplace` ou equivalentes quando não houver base objetiva suficiente.

## 27. Autoridade do Mall

A autoridade do Mall não deve depender de superlativos.

Ela deve emergir de:

```text
amplitude
+
curadoria
+
integração
+
clareza
+
responsabilidade
```

Síntese de direção:

> **Amplitude para escolher. Contexto para entender. Clareza para decidir.**

## 28. Escala

A Home deve parecer estruturalmente preparada para crescer globalmente sem afirmar escala que ainda não existe.

A arquitetura deve conseguir absorver, conforme a evolução real do produto:

- novos países;
- idiomas;
- moedas;
- categorias;
- fornecedores;
- parceiros;
- Gift Cards;
- novas modalidades comerciais.

> **Parecer estruturalmente preparada para o mundo é diferente de afirmar que já domina o mundo.**

## 29. Movimento 11 — Ecossistema

Próximo ao encerramento, a Home deve restabelecer a percepção de que o Mall faz parte de algo maior.

Direção:

# Mais do que uma loja isolada.

Relações conceituais:

```text
Journey
→ contexto e continuidade

Mall
→ produtos, serviços e presentes

Travel
→ viagens e experiências especializadas

Business
→ capacidades empresariais e benefícios

Intelligence
→ relevância e compreensão

Ads
→ visibilidade comercial identificada
```

Essas capacidades não devem ser apresentadas obrigatoriamente como cards iguais nem como uma lista de produtos concorrendo por protagonismo.

O objetivo é demonstrar integração.

## 30. Encerramento e escolha final

A Home retorna à pergunta inicial:

# E agora, o que pode fazer parte do seu próximo momento?

CTAs finais de direção:

- **Explorar Shopping**;
- **Ver Gift Cards**;
- **Presentear com Guivos**.

Neste ponto, os CTAs podem ser diretamente comerciais porque a narrativa já construiu contexto, prova e confiança.

## 31. O que a Home do Mall não deve se tornar

A Home não deve parecer:

- clone da Amazon, Mercado Livre ou outro marketplace;
- catálogo genérico sem contexto;
- página tomada exclusivamente por promoções;
- programa de pontos;
- sistema de recompensa por evolução;
- sequência infinita de banners;
- ambiente construído para induzir consumo;
- página institucional abstrata que dificulta comprar;
- especificação de páginas internas do produto.

> **A Home deve ser Guivos antes de parecer catálogo, mas precisa se tornar comércio naturalmente quando a pessoa estiver pronta para explorar.**

## 32. Contrato de fronteira com páginas internas

Os seguintes elementos podem existir como acessos, sinais ou conteúdos resumidos na Home sem trazer suas experiências internas para este contrato:

```text
produto exibido
→ a Home pode mostrar produto, preço e preço em pontos elegível
→ o detalhe do produto começa fora da Home

perfil no Header
→ a Home pode mostrar acesso e resumo global já existente
→ a página de Perfil começa fora da Home

carrinho no Header
→ a Home pode mostrar acesso
→ funcionamento e página do Carrinho começam fora da Home

checkout
→ não pertence à Home
```

Esta fronteira deve ser preservada em futuras evoluções documentais da Home Mall.

## 33. Tese final

A formulação que consolida a Home é:

> **A vida também é feita das coisas que escolhemos, usamos, experimentamos e compartilhamos. O Guivos Mall aproxima produtos, serviços e presentes de diferentes momentos da vida — para que cada pessoa possa encontrar o que faz sentido quando fizer sentido.**

Expressão comercial complementar:

> **Encontrar. Entender. Escolher.**

Proteção estratégica:

> **O Guivos Mall não existe para convencer pessoas de que precisam de mais coisas. Existe para tornar mais fácil encontrar, compreender e escolher entre possibilidades comerciais que podem fazer sentido para elas.**

## 34. Estado desta autoridade

Este Documento Mestre registra a base conceitual aprovada da Home Pública do Guivos Mall.

Ele:

- preserva a identidade maior da Guivos;
- reconhece Shopping e Gift Cards como as duas portas atuais do Mall;
- incorpora dinheiro e pontos em ofertas elegíveis sem transformar pontos em medida de evolução;
- distingue o Programa de Pontos do Guivos Business do Gift Card Guivos;
- usa **Empresa** no fluxo comercial específico do Programa de Pontos sem substituir a ontologia ampla de Organização;
- protege transparência entre destaque, recomendação, oferta e patrocínio;
- estabelece prova e confiança sem alegações artificiais de escala;
- mantém Página de Produto, Perfil, Carrinho e Checkout fora do escopo;
- não autoriza wireframe, protótipo, UI ou implementação.

Qualquer materialização posterior requer decisão própria e não decorre automaticamente da existência deste documento.

---

## 35. Prontidão documental para Designer e IA

Esta revisão fecha a auditoria de suficiência da **Home Pública — Guivos Mall** para consumo externo de Design.

### 35.1 Resultado da auditoria

```text
HOME MALL
→ SOURCE_READY = PASS

MASTER
→ GKR-UX-HOME-MALL-MASTER-001 v1.1.0

PRODUCT AUTHORITY
→ GPA-002 v1.2.0

MEDIA RECONCILIATION
→ GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0

MATERIAL DOCUMENT GAPS
→ 0

UNRESOLVED SEMANTIC CONFLICTS
→ 0

VISUAL IDENTITY PRE-IMPOSED
→ 0

MANUAL DESIGNER PATH
→ COMPLETE

OPTIONAL AI PATH
→ COMPLETE THROUGH COMMON SOURCE LOCK / BRIEF
```

A auditoria esclareceu que o **Movimento 10 — Prova e Confiança** possui duas facetas complementares no Master — evidência e proteção — sem criar um 12º movimento.

### 35.2 Evidência de suficiência

| Critério | Evidência | Estado |
|---|---|---|
| papel / premissa / relação Guivos × Mall | §§ 1–4 | PASS |
| pergunta-mãe / Hero / CTAs | §§ 5–6 | PASS |
| Header e fronteiras | §§ 7–8 | PASS |
| 11 movimentos | §§ 9–30 | PASS |
| Shopping / categorias | §§ 14–15 | PASS |
| preço / pontos / Business | §§ 16–17 + GPA-002 | PASS |
| personalidade / campanhas | §§ 18–19 | PASS |
| relevância / personalização | § 20 | PASS |
| destaque / recomendação / oferta / publicidade | § 21 | PASS |
| Gift Cards | §§ 22–23 | PASS |
| prova / marcas / confiança | §§ 24–27 | PASS |
| escala sem claim | § 28 | PASS |
| ecossistema / saída | §§ 29–30 | PASS |
| anti-padrões / páginas internas | §§ 31–32 | PASS |
| tese / autoridade | §§ 33–34 | PASS |
| Media editorial | GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 | PASS |

### 35.3 Condições e estados que a solução deve tolerar

#### Visitante sem sessão autenticada

- nenhuma informação de saldo de pontos deve ser presumida;
- nenhuma personalização deve ser apresentada como `Recomendado para você` sem base legítima;
- descoberta, busca, Shopping e Gift Cards podem permanecer compreensíveis no nível público;
- Perfil pode funcionar como acesso global, sem inventar conteúdo de conta.

#### Pessoa autenticada com saldo disponível

- saldo pertence ao componente global de conta/perfil quando essa capacidade existir;
- cards/ofertas mostram custo específico, não repetem saldo global;
- existência de saldo não implica elegibilidade de toda oferta.

#### Oferta somente em dinheiro

- exibir somente preço monetário;
- não criar equivalência em pontos por estimativa;
- não sugerir que pontos poderão ser usados depois.

#### Oferta elegível em pontos

- mostrar pontos somente quando a elegibilidade for real;
- não inferir pagamento híbrido;
- não inferir taxa de conversão;
- não transformar pontos em indicador de evolução.

#### Oferta indisponível

- a solução deve tolerar indisponibilidade, retirada, ausência de estoque ou término de condição;
- não manter preço, desconto ou CTA de compra como se a oferta estivesse disponível;
- a Home deve continuar coerente quando itens mudarem.

#### Campanha ativa

- campanha pode alterar camada comercial;
- não substitui a identidade permanente do Mall;
- urgência só pode refletir condição verdadeira.

#### Sem campanha ativa

- a Home continua completa sem banner promocional, desconto ou sazonalidade.

#### Conteúdo em destaque

- destaque pode ser curadoria geral;
- não deve parecer personalização quando não for.

#### Recomendação contextual

- só usar `Recomendado para você` quando existir base legítima, regras aplicáveis e consentimento quando necessário;
- contexto protegido da Journey não vira gatilho comercial irrestrito.

#### Patrocinado

- exposição paga deve permanecer identificada;
- não pode adquirir aparência de recomendação orgânica;
- remuneração não determina relevância.

#### Marca disponível

- presença no catálogo não equivale a parceria institucional.

#### Parceiro real

- somente pode ser apresentado como parceiro quando a relação formal estiver sustentada.

#### Gift Card de terceiro

- nome, marca, cobertura, disponibilidade, valor e condições exigem fonte real;
- exemplos conhecidos não devem ser convertidos automaticamente em inventário vigente.

#### Gift Card Guivos

- preservar presente + possibilidade + autonomia;
- não confundir com pontos;
- regras de valor, resgate, validade, transferência e cobertura permanecem fora deste Master quando não governadas.

#### Mídia / imagem ausente

- produto, oferta ou conteúdo editorial deve possuir fallback que preserve compreensão;
- imagem não pode carregar sozinha preço, condição, patrocínio ou natureza da oferta.

#### Baixa conectividade / reduced motion

- entendimento essencial não depende de animação, vídeo, hover ou carrossel automático;
- motion pode enriquecer, não governar significado.

#### Mobile

- mesma arquitetura semântica, menor simultaneidade;
- busca, portas Shopping/Gift Cards, distinções comerciais e CTAs devem permanecer compreensíveis;
- mobile não deve ser mero empilhamento do desktop.

#### Idioma / país / moeda

- solução deve tolerar expansão de texto;
- moeda, preço, disponibilidade, catálogo e condição comercial só podem refletir contexto realmente suportado;
- escala global aspiracional não autoriza afirmar presença operacional.

### 35.4 Acessibilidade e robustez

A solução deve prever:

- navegação por teclado;
- foco visível;
- leitores de tela;
- contraste adequado;
- texto ampliado;
- alvos de toque adequados;
- informação comercial não dependente só de cor;
- preço anterior/atual ou desconto com leitura inequívoca;
- labels de oferta/patrocínio acessíveis;
- reduced motion;
- fallback de mídia;
- nenhuma dependência exclusiva de hover;
- internacionalização;
- comportamento robusto com títulos, marcas e preços de comprimentos variados.

### 35.5 Matriz operacional específica do Mall

#### CANONICAL

- Mall é produto especializado da Guivos, não a Guivos transformada em e-commerce;
- pergunta-mãe: **“O que pode fazer parte do seu próximo momento?”**;
- descoberta + comércio + confiança;
- Hero permanente não dominada por promoção;
- duas portas atuais: Shopping e Gift Cards;
- 11 movimentos;
- Movimento 10 = Prova e Confiança, detalhado em duas facetas;
- preço monetário e pontos apenas quando realmente disponíveis;
- saldo da Pessoa ≠ preço da oferta;
- pontos ≠ evolução;
- Programa de Pontos ≠ Gift Card Guivos;
- destaque ≠ recomendação ≠ oferta ≠ patrocinado;
- marca disponível ≠ parceiro;
- patrocínio ≠ relevância;
- Mall pertence ao ecossistema maior;
- páginas de produto, Perfil, Carrinho e Checkout ficam fora do escopo da Home.

#### DESIGN_CREATIVE

A designer pode criar livremente:

- identidade visual;
- tipografia;
- paleta;
- imagem;
- fotografia;
- vídeo;
- ilustração;
- iconografia;
- composição;
- grid;
- ritmo;
- densidade;
- componentes;
- cards;
- navegação comercial;
- motion;
- campanhas visuais;
- organização das categorias;
- forma de apresentar Shopping/Gift Cards;
- tratamento de ofertas;
- solução desktop/mobile;
- direção de arte;
- linguagem gráfica.

#### CONTENT_CANDIDATE

- supporting copy;
- labels comerciais não congelados;
- headlines de seção;
- CTA secundário;
- microcopy;
- copy sazonal;
- formulações editoriais fornecidas pelo Media.

#### DESIGN_HYPOTHESIS

- formas de descoberta;
- estrutura de categorias;
- densidade comercial;
- agrupamento de ofertas;
- apresentação de Shopping/Gift Cards;
- modos de expor preço e pontos;
- tratamento visual de recomendação/destaque/patrocínio;
- ritmo entre inspiração e comércio;
- composição de campanhas;
- organização responsiva.

Hipótese visual não pode alterar elegibilidade, preço, estoque, disponibilidade, patrocínio ou natureza da recomendação.

#### PROTOTYPE_PLACEHOLDER

- produto;
- preço;
- desconto;
- pontos;
- marca;
- campanha;
- Gift Card;
- imagem;
- fornecedor;
- avaliação;
- recomendação;
- conteúdo editorial.

Placeholder deve parecer provisório internamente e nunca prova de operação.

#### REAL_DATA_REQUIRED

- produto realmente disponível;
- preço;
- preço em pontos;
- desconto;
- validade;
- estoque/disponibilidade;
- marca;
- parceiro;
- fornecedor;
- Gift Card;
- cobertura;
- moeda;
- país;
- avaliação;
- campanha;
- patrocínio;
- recomendação personalizada;
- integração;
- condição comercial.

#### OPEN_QUESTION

- catálogo vivo;
- inventário de lançamento;
- campanhas;
- preços reais;
- Gift Cards disponíveis;
- parceiros;
- fornecedores;
- condições comerciais;
- expansão geográfica;
- mecânicas econômicas ainda não formalizadas.

Esses itens não bloqueiam Design desde que componentes tolerem substituição/ausência e não apresentem placeholders como realidade.

#### PROHIBITED_INFERENCE

Não inventar ou insinuar:

- estoque;
- preço;
- taxa de conversão ponto/dinheiro;
- pagamento híbrido;
- regra de expiração/transferência de pontos;
- parceiro por simples presença de marca;
- Gift Card disponível sem fonte;
- cobertura global;
- personalização sem base;
- `Recomendado para você` sem contexto legítimo;
- patrocínio como relevância orgânica;
- melhor preço / maior marketplace / 100% seguro sem prova;
- desconto fictício;
- urgência artificial;
- pontos como evolução;
- Gift Card Guivos como pontos;
- catálogo genérico desconectado do propósito;
- Travel absorvido pelo Mall;
- página interna materializada dentro da Home por inferência.

### 35.6 Brief mínimo para a designer

Antes de criar, a designer deve conseguir responder:

1. qual o papel do Mall dentro da Guivos;
2. qual é a pergunta-mãe;
3. por que Hero permanente ≠ campanha;
4. quais são as duas portas atuais;
5. quais são os 11 movimentos;
6. como preço monetário e pontos funcionam no nível da Home;
7. por que saldo ≠ preço;
8. como destaque, recomendação, oferta e patrocínio se distinguem;
9. como marca disponível difere de parceiro;
10. o que pertence à Home e o que começa nas páginas internas;
11. quais fatos comerciais exigem dado real;
12. quais estados de indisponibilidade devem ser tolerados;
13. o que é livre para criação;
14. o que é proibido inferir;
15. como a solução funciona em mobile, reduced motion e baixa conectividade.

### 35.7 Uso opcional de IA

Se a designer usar IA, o contexto deve incluir:

1. autoridades comuns vigentes;
2. `GPA-002`;
3. este Master;
4. `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001`;
5. matriz operacional desta seção;
6. objetivo explícito.

`GEM-007-MALL-ECONOMIC-ROLE-001` pode ser consultado para contexto econômico, mas permanece `draft` e não autoriza transformar eventos, receitas candidatas ou responsabilidades futuras em operação pública vigente.

### 35.8 Fechamento

```text
HOME MALL
→ SOURCE_READY = PASS

DESIGNER
→ CAN START FROM DOCUMENTATION AFTER GLOBAL PACKAGE RELEASE

AI
→ OPTIONAL

FIGMA MAKE
→ NOT REQUIRED

VISUAL DIRECTION
→ DESIGN-OWNED

MATERIAL SEMANTIC GAP
→ 0
```

Este `PASS` é documental. Não valida estoque, pricing, operação comercial, PMF, implementação ou disponibilidade real.
