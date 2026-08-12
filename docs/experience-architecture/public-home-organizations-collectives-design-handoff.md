---
id: GKR-UX-HOME-OC-HANDOFF-001
title: Handoff para Design/UX/UI da Home Pública de Organizações e Coletivos
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
  - GKR-UX-HOME-OC-SYS-001
  - GKR-UX-HOME-SYS-001
related:
  - GKR-UX-HOME-HANDOFF-001
  - UXA-014
  - UXA-019
  - UXA-015
  - UXA-016
normative: false
---

# Handoff para Design/UX/UI da Home Pública de Organizações e Coletivos

## 1. Finalidade

Este documento executa o **P4 da prontidão pré-materialização** da Home Pública de Organizações e Coletivos e resolve, em princípio, `OC-GAP-04 — Handoff específico para Design/UX/UI` identificado por `GKR-UX-HOME-OC-AUDIT-001`.

Seu objetivo é transformar a estratégia já governada em um **brief executável de materialização futura**, suficientemente claro para que Design, UX, UI ou uma ferramenta generativa não precisem reinventar decisões de posicionamento, narrativa, participante, prova, confiança ou ação.

Este documento não é um wireframe.

Ele também não é uma especificação visual final.

Ele estabelece:

- significado obrigatório;
- precedência entre fontes;
- liberdade legítima de composição;
- maturidade da copy;
- contrato de prova;
- estados ainda abertos;
- critérios de aceite;
- critérios de rejeição;
- proteções para desktop e mobile;
- proteções para ferramentas generativas;
- limite entre handoff e autorização de materialização.

Decisão central:

> **Design pode transformar a forma, condensar a expressão e criar composição. Não pode redefinir o significado da página.**

---

## 2. O que este handoff não autoriza

A existência deste documento **não autoriza**:

- wireframe;
- Figma;
- SVG;
- protótipo;
- UI final;
- direção visual final;
- grid;
- breakpoint;
- pixel;
- componente;
- biblioteca de componentes;
- fotografia final;
- ilustração final;
- animação específica;
- vídeo;
- copy pública final;
- produção de assets;
- implementação;
- publicação em produção;
- UXA-102/V5;
- Engenharia de Produto.

Após este P4 ainda é obrigatória a execução do **P5 — reauditoria final de prontidão**.

Somente depois do P5 uma decisão humana separada poderá autorizar ou não o início de materialização conceitual.

---

## 3. Estado de entrada

Este handoff parte de cinco artefatos específicos da Home Pública de Organizações e Coletivos.

### 3.1 Documento Mestre

`GKR-UX-HOME-OC-MASTER-001`

Governa:

- tese;
- relação com a Home Pública principal;
- definição dos participantes;
- onze movimentos narrativos;
- papel da Guivos;
- complementaridade;
- valor;
- confiança;
- arquitetura do ecossistema;
- bifurcação final.

### 3.2 Auditoria de prontidão

`GKR-UX-HOME-OC-AUDIT-001`

Governa:

- lacunas de pré-materialização;
- o que pode ser herdado;
- o que exige contrato próprio;
- fronteira com UXA-015 e UXA-016;
- sequência P1 → P5.

### 3.3 Mapa de macroexperiências

`GKR-UX-HOME-OC-NARR-001`

Governa:

- agrupamento dos onze movimentos em sete macroexperiências;
- ritmo semântico;
- estados de entrada e saída;
- anti-agrupamentos;
- equivalência de intenção entre desktop e mobile.

### 3.4 Header, Hero e CTAs

`GKR-UX-HOME-OC-NAV-001`

Governa:

- permanência do Header global;
- estado contextual da página;
- papel da Hero;
- significado de `Iniciar Jornada`;
- relação entre CTA inicial e CTAs finais;
- momento correto da bifurcação Organização / Coletivo.

### 3.5 Conteúdo, prova e evidência

`GKR-UX-HOME-OC-SYS-001`

Governa:

- classes de verdade;
- função de prova por movimento;
- métricas;
- logos;
- histórias;
- relações;
- cenários ilustrativos;
- estados futuros;
- fallback para baixa disponibilidade de evidência.

---

## 4. Hierarquia de precedência

Quando houver dúvida durante materialização futura, utilizar esta ordem:

```text
DOCUMENTO MESTRE
        ↓
MAPA DE MACROEXPERIÊNCIAS
        ↓
HEADER / HERO / CTAs
        ↓
CONTEÚDO / PROVA / EVIDÊNCIA
        ↓
ESTE HANDOFF
```

O handoff **traduz** decisões para Design.

Não as substitui.

Se uma interpretação deste documento entrar em conflito com um contrato anterior específico, prevalece o contrato anterior.

### 4.1 Sistema transversal da Home principal

`GKR-UX-HOME-SYS-001` continua aplicável como contrato transversal de:

- percepção de marca;
- interação;
- movimento;
- acessibilidade;
- resiliência;
- fotografia;
- densidade;
- responsabilidade editorial.

Ele não transfere automaticamente a estrutura narrativa da Home orientada à Pessoa para esta página.

### 4.2 Handoff da Home principal

`GKR-UX-HOME-HANDOFF-001` pode ser utilizado como referência de disciplina de entrega.

Não deve ser usado como especificação substituta desta página.

### 4.3 UXA-015 e UXA-016

Podem informar verdade funcional sobre:

- autoridade;
- responsabilidades;
- autonomia;
- dados;
- governança;
- funcionamento interno de Organização ou Coletivo.

Não podem ser tratados como referência de layout, composição ou linguagem visual desta Home pública.

Regra:

```text
HOME PÚBLICA — ORGANIZAÇÕES E COLETIVOS
≠ DASHBOARD DA ORGANIZAÇÃO
≠ INÍCIO DO COLETIVO AUTENTICADO
```

---

## 5. Tese que Design deve materializar

A página responde à pergunta:

> **O que podemos tornar possível juntos?**

A resposta não é:

- compre este produto;
- cadastre sua empresa;
- anuncie para usuários;
- crie uma comunidade;
- encontre clientes;
- patrocine uma causa;
- contrate Business;
- acesse dados de pessoas.

A resposta é perceptiva:

> **capacidades que hoje existem separadamente podem encontrar pessoas, contextos e outras capacidades, criando novas possibilidades de participação e continuidade sem retirar autonomia dos participantes.**

Design deve fazer essa tese ser compreendida **antes** de intensificar ação ou produto.

---

## 6. Estado mental desejado no início e no fim

### Entrada

O visitante pode chegar pensando:

- `Não sei por que minha organização estaria na Guivos.`
- `Isto parece uma plataforma para pessoas.`
- `Não sei o que um coletivo significa aqui.`
- `Talvez seja outra ferramenta B2B.`
- `Talvez seja publicidade, marketplace ou comunidade.`

### Saída

A página deve permitir algo próximo de:

> **Entendo por que nossa Organização ou Coletivo pertence a esse ecossistema, entendo nosso papel, entendo como podemos gerar e receber valor, entendo por que a Guivos é diferente de um canal isolado e quero descobrir como participar.**

A página falha se o visitante chegar ao CTA final sem essa mudança de compreensão.

---

## 7. Significados que não podem ser removidos

Qualquer materialização futura precisa preservar semanticamente os onze movimentos, mesmo que não existam onze blocos visuais.

### M01 — possibilidade

A página precisa abrir o horizonte antes de explicar solução.

### M02 — capacidade existente e fragmentação

O visitante precisa reconhecer que Organizações e Coletivos já produzem valor, mas que iniciativas e capacidades frequentemente permanecem desconectadas.

### M03 — continuidade possível

Precisa existir a ideia de que uma possibilidade pode abrir contexto para outra, sem prometer causalidade automática.

### M04 — papel da Guivos

A Guivos conecta, organiza contexto e amplia continuidade; não substitui participantes nem se apropria de sua agência.

### M05 — quem participa

Pessoa, Organização e Coletivo precisam permanecer distinguíveis.

### M06 — complementaridade

Aquilo que falta para um participante pode existir na capacidade de outro, sem reduzir o ecossistema a oferta versus consumo.

### M07 — múltiplas dimensões

Evolução não é apenas carreira, compra, impacto social ou produtividade.

### M08 — valor e escala responsável

Valor pode circular. Escala aumenta possibilidades quando preserva contexto e significado.

### M09 — confiança

Responsabilidade, transparência, governança, privacidade, proveniência, limites e autonomia precisam fazer parte da experiência.

### M10 — capacidades da Guivos

Produtos aparecem como infraestrutura conectada do ecossistema, não como catálogo e não como equivalentes aos participantes.

### M11 — participação

Organização e Coletivo recebem caminhos próprios somente após compreensão suficiente e com igual legitimidade.

---

## 8. Os onze movimentos não são onze seções obrigatórias

Regra já governada:

> **movimento narrativo é função semântica; seção visual é decisão de composição.**

Design pode:

- combinar movimentos compatíveis;
- fazer um movimento atravessar mais de uma composição;
- usar transições contínuas;
- alternar densidade;
- representar um significado por texto, mídia, evidência, espaço ou interação;
- condensar listas;
- reduzir repetição.

Design não pode:

- apagar função semântica para encurtar a página;
- inverter a progressão principal;
- antecipar produto antes de contexto;
- antecipar bifurcação Organização / Coletivo;
- esconder confiança depois do catálogo;
- transformar os movimentos em cards independentes sem continuidade.

---

## 9. Sete macroexperiências — contrato de materialização

### 9.1 Macroexperiência 01 — Abrir o campo de possibilidades

Movimento:

- M01.

Entrada:

> visitante ainda não sabe o que esta página representa.

Saída cognitiva desejada:

> **`Nossa capacidade pode fazer parte de um campo maior de possibilidades.`**

Obrigatório:

- possibilidade;
- amplitude;
- baixa carga explicativa;
- protagonismo da pergunta.

Pode variar:

- mídia;
- quantidade de texto;
- ritmo;
- CTA de continuidade;
- composição.

Rejeitar se:

- começar por produto;
- começar por formulário;
- começar por `fale com vendas`;
- apresentar Organização e Coletivo como dois planos;
- parecer landing page de aquisição B2B.

### 9.2 Macroexperiência 02 — Reconhecer o que existe e perceber a desconexão

Movimentos:

- M02;
- M03.

Entrada:

> visitante percebe possibilidade, mas ainda não reconheceu o problema sistêmico.

Saída desejada:

> **`Já fazemos parte disso de alguma forma; o que falta é mais continuidade entre capacidades e acontecimentos.`**

Obrigatório:

- reconhecimento antes de crítica;
- fragmentação;
- continuidade como possibilidade;
- realidade concreta quando disponível.

Pode variar:

- histórias;
- exemplos;
- fotografia;
- vídeo;
- pequenos recortes editoriais;
- representação de conexões.

Rejeitar se:

- afirmar que canais atuais são inúteis;
- atacar redes, sites, campanhas ou comunidades existentes;
- prometer que a Guivos produzirá uma cadeia automática de transformação;
- usar `antes/depois` fictício.

### 9.3 Macroexperiência 03 — Entender a Guivos e quem participa

Movimentos:

- M04;
- M05.

Entrada:

> visitante reconheceu o problema, mas ainda não entende o papel da Guivos e a ontologia do ecossistema.

Saída desejada:

> **`Entendo o que a Guivos faz e entendo por que Pessoa, Organização e Coletivo são participantes diferentes.`**

Obrigatório:

- Guivos como conexão/contexto/continuidade;
- Pessoa ≠ Organização ≠ Coletivo;
- participante ≠ produto;
- autonomia do participante.

Pode variar:

- representação relacional;
- quantidade de exemplos;
- forma de explicar os três participantes;
- uso de texto ou ilustração conceitual.

Rejeitar se:

- Organização = Business;
- Pessoa = Journey;
- Coletivo = produto Comunidade;
- criar três tiers comerciais;
- representar Guivos como controladora da jornada humana.

### 9.4 Macroexperiência 04 — Perceber complementaridade e ampliar contextos

Movimentos:

- M06;
- M07.

Entrada:

> visitante entende os participantes, mas ainda não visualiza como suas capacidades podem se relacionar.

Saída desejada:

> **`Existem muitas combinações possíveis e elas podem fazer sentido em diferentes dimensões da vida.`**

Obrigatório:

- complementaridade;
- relações multidirecionais;
- múltiplas dimensões;
- ausência de caminho prescritivo.

Pode variar:

- cenários ilustrativos claramente tratados como exemplos;
- histórias reais;
- contextos locais e globais;
- movimento de descoberta.

Rejeitar se:

- cenário parecer parceria real sem ser;
- Organização sempre der e Pessoa sempre receber;
- Coletivo existir apenas como intermediário social;
- reduzir evolução a carreira, consumo ou impacto social;
- prescrever espiritualidade, propósito ou estilo de vida.

### 9.5 Macroexperiência 05 — Compreender valor, diversidade e escala

Movimento:

- M08.

Entrada:

> visitante percebe complementaridade, mas precisa entender por que participar também faz sentido para si.

Saída desejada:

> **`Todos podem gerar e receber valor; mais diversidade pode ampliar o campo de possibilidades.`**

Obrigatório:

- reciprocidade;
- valor multidirecional;
- escala com responsabilidade;
- contexto antes de volume.

Pode variar:

- histórias;
- exemplos;
- evidência institucional;
- métricas governadas quando realmente necessárias.

Rejeitar se:

- `acesse milhões de usuários`;
- tamanho virar sinônimo de impacto;
- volume virar sinônimo de evolução;
- globalidade for simulada por países não ativos;
- parede de números substituir compreensão.

### 9.6 Macroexperiência 06 — Encontrar confiança e compreender as capacidades da Guivos

Movimentos:

- M09;
- M10.

Entrada:

> visitante entende o potencial e agora precisa decidir se a Guivos parece séria e capaz de sustentar essa ambição.

Saída desejada:

> **`Há responsabilidade e infraestrutura por trás da visão, sem que os produtos sejam a própria Guivos.`**

Obrigatório:

- confiança antes de intensificação de produto;
- governança;
- transparência;
- privacidade;
- limites;
- autonomia;
- hierarquia correta do ecossistema;
- verdade operacional sobre produtos.

Pode variar:

- evidências;
- método;
- arquitetura conceitual;
- densidade;
- representação de produtos/capacidades.

Rejeitar se:

- virar carrossel de produtos;
- Business for `produto das empresas`;
- Intelligence sugerir acesso irrestrito a pessoas;
- produtos futuros parecerem disponíveis hoje;
- logo wall substituir autoridade;
- confiança aparecer como selo sem proveniência.

### 9.7 Macroexperiência 07 — Escolher como continuar participando

Movimento:

- M11.

Entrada:

> visitante já entende significado, papel, valor e confiança.

Saída desejada:

> **`Quero descobrir a jornada adequada à nossa natureza de participante.`**

Obrigatório:

- dois caminhos com igual legitimidade;
- Organização;
- Coletivo;
- descoberta antes de conversão;
- permanência do ecossistema comum.

Pode variar:

- microcopy;
- forma de apresentar os dois caminhos;
- composição;
- transição para destinos futuros.

Rejeitar se:

- um caminho parecer premium e outro secundário;
- `crie sua empresa` ou `crie seu coletivo`;
- formulário obrigatório;
- preço/plano antecipado;
- CTA comercial dominante;
- escolha aparecer antes da narrativa comum.

---

## 10. Header global

A página utiliza o **mesmo Header global da Guivos**.

Não criar:

- `Guivos Business` como marca do Header;
- Header corporativo separado;
- navegação B2B paralela;
- submarca `Guivos para Empresas`;
- troca de identidade para linguagem institucional tradicional.

`Organizações e Coletivos` deve ser reconhecível como contexto atual da navegação.

`Guivos` / Home permanece caminho natural de retorno à Home Pública principal.

---

## 11. `Iniciar Jornada`

`Iniciar Jornada` continua significando **Guivos Journey**.

Não significa:

- cadastrar Organização;
- cadastrar Coletivo;
- iniciar onboarding institucional;
- contratar plano;
- criar campanha;
- falar com vendas.

A materialização futura deve reduzir ambiguidade suficiente para que um visitante institucional não interprete esse CTA como seu caminho principal de cadastro.

Design pode resolver essa ambiguidade por hierarquia, contexto e relação espacial.

Não pode mudar arbitrariamente o significado do CTA.

---

## 12. Hero

Pergunta de trabalho de alta confiança:

> **O que podemos tornar possível juntos?**

A Hero deve:

- abrir possibilidade;
- parecer parte da mesma Guivos;
- reconhecer um `nós` amplo;
- evitar linguagem de aquisição;
- funcionar com e sem mídia rica;
- manter significado sem animação.

### 12.1 CTA da Hero

Função:

> **continuar a descoberta dentro da própria narrativa.**

Não deve:

- antecipar Organização versus Coletivo;
- iniciar cadastro;
- abrir pricing;
- abrir formulário comercial;
- exigir decisão de tipo antes de compreensão.

A redação literal do CTA pode ser lapidada futuramente desde que sua função permaneça esta.

---

## 13. Bifurcação final

A separação entre Organização e Coletivo acontece somente depois da narrativa compartilhada.

Intenções governadas:

> **Descobrir como participar como Organização**

> **Descobrir como participar como Coletivo**

Esses textos ainda podem receber lapidação editorial.

A intenção não pode mudar para:

- comprar;
- contratar;
- anunciar;
- cadastrar imediatamente;
- criar conta como única continuação.

Os destinos futuros são jornadas públicas específicas de compreensão e participação antes de qualquer operação obrigatória.

---

## 14. Maturidade da copy

Nem todo texto do Documento Mestre deve chegar literalmente à página.

### 14.1 Alta estabilidade semântica

Não reabrir sem decisão estratégica:

- `O que podemos tornar possível juntos?` como pergunta-mãe;
- Pessoa / Organização / Coletivo como tipos estruturais;
- Guivos como conexão, contexto e continuidade;
- participante ≠ produto;
- Organização ≠ Business;
- Comunidade não é produto Guivos;
- autonomia;
- confiança;
- Intelligence não equivale a acesso às pessoas;
- bifurcação tardia.

### 14.2 Copy de trabalho

Podem ser condensados ou reescritos para materialização:

- parágrafos explicativos;
- listas de exemplos;
- transições;
- subtítulos;
- microcopy;
- exemplos de dimensões;
- formulações longas de valor;
- legendas conceituais.

Regra:

> **condensar texto é permitido; condensar significado, não.**

### 14.3 Copy pública final

Ainda não está congelada.

O futuro processo de conteúdo pode aprimorar:

- naturalidade;
- ritmo;
- concisão;
- clareza internacional;
- legibilidade mobile;
- tradução;
- microcopy de ação.

Não pode introduzir:

- claims não governados;
- superlativos sem prova;
- linguagem de aquisição como tese;
- causalidade garantida;
- promessa de escala operacional inexistente.

---

## 15. Conteúdo que pode ser condensado

Design e Conteúdo podem reduzir:

- listas longas de tipos de Organização;
- listas longas de tipos de Coletivo;
- listas de dimensões da vida;
- listas de capacidades;
- exemplos redundantes;
- explicações repetidas de autonomia;
- repetição verbal de `não é produto` quando a própria composição já comunicar corretamente.

A redução é válida quando a saída cognitiva do movimento permanece preservada.

---

## 16. Conteúdo que não pode desaparecer por simplificação

Mesmo numa materialização muito concisa, precisam permanecer perceptíveis:

1. possibilidade;
2. capacidade existente;
3. fragmentação;
4. continuidade possível;
5. papel da Guivos;
6. Pessoa / Organização / Coletivo;
7. complementaridade;
8. múltiplos contextos de evolução;
9. reciprocidade de valor;
10. escala responsável;
11. confiança;
12. autonomia;
13. capacidades da Guivos sem catálogo;
14. dois caminhos finais com igual legitimidade.

---

## 17. Contrato de verdade para Design

Design não recebe permissão para criar prova.

Recebe **funções de prova**.

Toda evidência apresentada como real precisa ser sustentada por conteúdo governado.

### 17.1 Classes internas

Distinguir durante produção:

1. fato governado;
2. evidência verificável;
3. interpretação editorial;
4. cenário ilustrativo;
5. estado futuro ou capacidade ainda não disponível.

A experiência pública não precisa exibir esses rótulos técnicos, mas jamais pode fazer uma classe mais fraca parecer uma classe mais forte.

---

## 18. Cenários ilustrativos

Cenário ilustrativo pode ajudar a explicar complementaridade.

Pode mostrar, conceitualmente:

```text
uma Organização oferece conhecimento
→ um Coletivo aproxima pessoas interessadas
→ outra capacidade cria uma experiência
→ surgem novas possibilidades
```

Mas deve permanecer inequivocamente um exemplo conceitual quando não corresponder a uma relação real.

Nunca utilizar:

- logos reais em combinação fictícia;
- nomes reais sugerindo parceria inexistente;
- números inventados;
- screenshots simulados como produção;
- depoimentos fictícios;
- países marcados como operação ativa sem confirmação.

---

## 19. Logos

Logo não é prova automática.

Só utilizar quando houver:

- relação real;
- contexto compreensível;
- permissão aplicável;
- função narrativa legítima.

Evitar:

- parede de logos;
- logos sem explicação;
- associação implícita maior que a relação real;
- marcas usadas apenas para emprestar prestígio.

---

## 20. Métricas

Toda métrica precisa de, no mínimo:

- definição;
- fonte;
- período;
- método ou contexto suficiente;
- limite de interpretação.

Não utilizar métricas apenas porque `números grandes parecem prova`.

Rejeitar:

- usuários sem definição;
- alcance sem período;
- países sem critério;
- crescimento sem baseline;
- impacto sem método;
- transformação atribuída causalmente à Guivos sem base.

---

## 21. Depoimentos e histórias

Histórias são preferíveis quando demonstram contexto, possibilidade, escolha, experiência e continuidade.

A Guivos não deve aparecer como heroína automática.

Depoimento isolado:

- pode apoiar;
- não substitui evidência;
- não prova autoridade institucional sozinho.

Evitar linguagem de `case de sucesso` quando ela pressupuser uma definição universal de sucesso ou atribuir causalidade excessiva.

---

## 22. Estágio inicial com pouca evidência

Se a Guivos ainda possuir pouca evidência real para determinado movimento:

> **reduzir a força da afirmação antes de inventar prova.**

Fallback legítimo:

- tese forte;
- exemplos do mundo real sem alegar participação na Guivos;
- arquitetura canônica;
- transparência sobre estágio;
- poucas evidências profundas;
- cenário ilustrativo claramente indicado quando necessário.

Nunca preencher espaço visual com prova simulada apenas para a página parecer madura.

---

## 23. Produtos e capacidades

Design deve evitar a leitura:

```text
GUIVOS
=
coleção de produtos independentes
```

A hierarquia semântica permanece:

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

A futura composição pode traduzir essa arquitetura de diferentes formas.

Não precisa reproduzir uma árvore literal.

Mas precisa impedir:

- equivalência visual entre participante e produto;
- Business como destino obrigatório de Organizações;
- Intelligence como produto de vigilância;
- produtos como protagonista anterior à tese.

---

## 24. Intelligence

Intelligence deve ser percebida como capacidade transversal de compreensão responsável.

Não comunicar:

- acesso automático a membros de Coletivos;
- dossiê de Pessoas;
- segmentação invasiva;
- controle de jornada;
- decisão automatizada como autoridade final.

Quando houver representação de dados, contexto ou sinais, Design deve preservar a percepção:

> **Inteligência apoia compreensão; não retira a agência humana.**

---

## 25. Comunidades e Coletivos

Não criar um produto `Comunidade` por inferência visual.

Uma comunidade existente no mundo pode participar como Coletivo quando sua natureza for compatível.

Coletivos:

- preservam identidade;
- preservam autonomia;
- não são `criados pela Guivos` por definição;
- não precisam parecer fóruns ou grupos de rede social;
- não devem ser reduzidos a causas sociais.

---

## 26. Organização não significa empresa privada

A linguagem e composição precisam acomodar com legitimidade:

- grande empresa;
- pequena organização local;
- universidade;
- instituição;
- fundação;
- ONG;
- governo;
- associação formal;
- entidade religiosa;
- organização cultural;
- estrutura internacional.

Se a página parecer criada principalmente para diretores comerciais de empresas privadas, houve desvio.

---

## 27. Coletivo não significa ONG informal

A composição deve acomodar:

- grupo profissional;
- rede;
- movimento;
- coletivo esportivo;
- coletivo cultural;
- comunidade territorial;
- articulação acadêmica;
- coletivo espiritual;
- grupo empreendedor;
- causa;
- interesse compartilhado.

Se a página parecer exclusivamente social/assistencial, houve desvio.

---

## 28. Percepção visual herdada

A página pertence à mesma Guivos.

Deve preservar a direção transversal:

> **Futuro sem ficção. Tecnologia sem frieza. Sofisticação sem elitismo. Escala sem ruído. Humanidade sem clichê.**

Percepções desejadas:

- futuro;
- possibilidade;
- globalidade;
- confiança;
- simplicidade;
- humanidade;
- sofisticação;
- vida;
- precisão;
- amplitude.

---

## 29. O que a página não deve parecer

Rejeitar propostas que pareçam predominantemente:

- landing page de SaaS B2B;
- página `para empresas` convencional;
- pricing page;
- página de vendas;
- portal de parceiros;
- dashboard autenticado;
- CRM;
- plataforma de mídia programática;
- marketplace;
- job board;
- rede social;
- construtor de comunidades;
- campanha de responsabilidade social;
- brochure corporativo;
- apresentação para investidores;
- catálogo de produtos;
- mural de cases;
- mural de logos.

---

## 30. O que a página deve parecer

A percepção deve ser de:

> **uma segunda porta pública para a mesma Guivos, criada para quem possui capacidade de mobilizar ou realizar e quer compreender como essa capacidade pode participar de um ecossistema maior.**

O visitante deve sentir que está entrando em algo maior do que uma solução isolada.

Não que está comprando uma ferramenta.

---

## 31. Fotografia e mídia

Herdar do sistema transversal:

- contexto real;
- ação;
- naturalidade;
- diversidade;
- direção editorial;
- qualidade;
- humanidade.

Evitar:

- handshake corporativo;
- reunião genérica com pessoas apontando para notebook;
- executivos sorrindo sem contexto;
- `startup stock photo`;
- felicidade genérica;
- estética publicitária sem relação com o significado.

Pessoas devem aparecer fazendo algo que ajude a compreender o universo.

---

## 32. Movimento e interação

Interação deve servir a:

- revelar;
- conectar;
- dar continuidade;
- demonstrar mudança de contexto.

Regra:

> **movimento deve carregar significado.**

Não utilizar animação apenas para parecer tecnológica.

A página deve continuar compreensível com animações desativadas.

---

## 33. Acessibilidade e resiliência

A futura materialização deve contemplar:

- teclado;
- leitores de tela;
- foco visível;
- contraste adequado;
- `prefers-reduced-motion` ou equivalente;
- legendas;
- transcrições;
- fallback de mídia;
- baixa conectividade;
- ausência de autoplay de áudio;
- experiência funcional sem vídeo.

Conteúdo essencial não pode depender de gesto opcional.

---

## 34. Desktop e mobile

Desktop e mobile podem usar composições diferentes.

Devem produzir as mesmas saídas cognitivas.

Mobile não é:

- desktop encolhido;
- tese reduzida;
- versão sem prova;
- versão sem confiança;
- versão sem participantes.

Mobile pode:

- serializar relações que desktop apresenta simultaneamente;
- reduzir densidade;
- usar revelação progressiva;
- simplificar mídia;
- alterar ritmo.

Não pode remover significado estrutural.

---

## 35. Ritmo

A materialização deve evitar uma página composta por blocos de mesma densidade.

A alternância pode trabalhar:

- impacto;
- reconhecimento;
- descoberta;
- compreensão;
- prova;
- respiro;
- confiança;
- reabertura.

Princípio:

> **uma ideia dominante por momento perceptivo.**

---

## 36. Liberdade legítima de Design

Dentro dos contratos anteriores, Design pode decidir futuramente:

- composição;
- grid;
- hierarquia tipográfica;
- uso de imagem;
- uso de vídeo;
- ilustração;
- ritmo de scroll;
- espaços;
- densidade;
- transições;
- agrupamento visual;
- comportamento responsivo;
- modo de representar relação entre participantes;
- modo de representar o ecossistema;
- modo de apresentar evidência;
- expressão de cada macroexperiência.

Essas decisões permanecem abertas até uma etapa de materialização autorizada.

---

## 37. Liberdade que Design não possui

Design não pode decidir por conta própria:

- que a página será B2B;
- que `Organizações` significa empresas privadas;
- que Coletivo significa ONG;
- que a Guivos cria comunidades;
- que Business é o produto das Organizações;
- que Journey é irrelevante nesta página;
- que Intelligence permite acesso a pessoas;
- que a bifurcação deve aparecer na Hero;
- que o CTA principal será `Fale com vendas`;
- que produtos devem aparecer imediatamente;
- que confiança pode ser removida por falta de espaço;
- que cenário fictício pode parecer real;
- que escala global pode ser simulada;
- que os onze movimentos são opcionais.

---

## 38. Estados ainda abertos

O handoff não fecha:

- layout;
- wireframe;
- direção visual final;
- quantidade de telas/frame;
- assets;
- imagens;
- vídeos;
- ilustrações;
- animações;
- copy final;
- conteúdo real específico;
- parceiros específicos;
- histórias específicas;
- métricas específicas;
- países operacionais;
- URLs finais;
- onboarding;
- planos;
- preços;
- disponibilidade de produtos no lançamento;
- calendário de GTM.

Essas aberturas não impedem a conclusão documental do P4.

---

## 39. Critérios de aceite de um futuro wireframe conceitual

Um futuro wireframe só deve ser considerado semanticamente aderente se:

1. possibilidade vier antes de produto;
2. a página não parecer uma landing page de vendas B2B;
3. a ordem semântica dos onze movimentos permanecer preservada;
4. os onze movimentos estiverem representados, ainda que agrupados;
5. as sete macroexperiências produzirem as saídas cognitivas governadas;
6. o Header permanecer parte da mesma Guivos;
7. `Iniciar Jornada` não parecer onboarding de Organização/Coletivo;
8. a Hero não antecipar cadastro nem bifurcação;
9. Pessoa, Organização e Coletivo permanecerem distinguíveis;
10. participante não for confundido com produto;
11. Organização não for confundida com Business;
12. Comunidade não for apresentada como produto Guivos;
13. complementaridade não virar oferta versus consumo;
14. evolução não for reduzida a uma única dimensão;
15. valor for multidirecional;
16. escala não for apresentada como volume vazio;
17. confiança aparecer antes ou governando a apresentação das capacidades;
18. privacidade, limites e autonomia forem perceptíveis;
19. Intelligence não sugerir acesso irrestrito a pessoas;
20. produtos aparecerem dentro da hierarquia correta do ecossistema;
21. nenhum produto futuro parecer operacional sem base;
22. Organização e Coletivo receberem caminhos finais equivalentes em legitimidade;
23. os caminhos finais significarem descoberta, não conversão obrigatória;
24. conteúdo essencial funcionar sem animação;
25. conteúdo essencial funcionar sem mídia rica;
26. mobile preservar significado;
27. não houver evidência, parceiro, métrica ou país inventado;
28. UXA-015 e UXA-016 não forem mimetizados como estrutura pública;
29. a proposta funcionar para diferentes tipos de Organização;
30. a proposta funcionar para diferentes tipos de Coletivo.

---

## 40. Critérios de rejeição imediata

Rejeitar ou devolver para revisão antes de refinamento visual se a proposta:

- abrir com `soluções para sua empresa`;
- abrir com cards de produtos;
- abrir com dois botões `Empresa` / `Coletivo`;
- abrir com formulário;
- usar pricing como estrutura;
- tratar Organização como cliente e Pessoa como audiência;
- tratar Coletivo como canal de distribuição;
- prometer acesso a usuários;
- prometer dados de comunidades;
- representar Intelligence como vigilância;
- transformar Guivos em marketplace;
- transformar Guivos em rede social;
- transformar a página em campanha ESG/CSR;
- representar escala por mapa de países sem verdade operacional;
- usar logos sem contexto;
- usar cases fictícios;
- usar números inventados;
- eliminar confiança para reduzir comprimento;
- colocar produtos antes de explicar a Guivos;
- usar estética de dashboard autenticado;
- copiar UXA-015 ou UXA-016;
- criar uma identidade visual corporativa paralela à Guivos.

---

## 41. Teste de neutralidade entre tipos de Organização

Avaliar a proposta mentalmente com:

- multinacional;
- pequena empresa local;
- universidade;
- prefeitura ou outro governo;
- fundação;
- ONG;
- associação;
- instituição cultural;
- entidade religiosa.

Pergunta:

> **todos conseguem se reconhecer como Organização sem que a página pareça escrita principalmente para um diretor comercial?**

Se não, revisar.

---

## 42. Teste de neutralidade entre tipos de Coletivo

Avaliar com:

- comunidade territorial;
- grupo profissional;
- movimento;
- coletivo esportivo;
- rede cultural;
- comunidade acadêmica;
- coletivo espiritual;
- grupo empreendedor;
- articulação de causa;
- rede internacional de interesse.

Pergunta:

> **todos conseguem se reconhecer sem que a página pareça restrita a ativismo ou assistência social?**

Se não, revisar.

---

## 43. Teste de protagonismo da Pessoa

Mesmo sendo uma página orientada a Organizações e Coletivos, a Pessoa não pode virar objeto passivo.

Pergunta:

> **a composição preserva a ideia de que pessoas vivem e decidem suas próprias jornadas, ou parece que Organizações e Coletivos administram a evolução delas?**

A segunda interpretação é inválida.

---

## 44. Teste de não comercialização excessiva

Pergunta:

> **se retirarmos logos, preços, formulários e linguagem comercial, a página ainda explica por que Organizações e Coletivos pertencem à Guivos?**

A resposta deve ser sim.

---

## 45. Teste de Guivos maior que os produtos

Pergunta:

> **se ocultarmos temporariamente os nomes Journey, Travel, Mall, Media, Business, Ads e Intelligence, a tese da Guivos continua compreensível?**

A resposta deve ser sim.

Se não, os produtos assumiram protagonismo excessivo.

---

## 46. Teste de verdade

Antes de aprovar qualquer prova futura, perguntar:

1. isto é fato governado?
2. é evidência verificável?
3. é interpretação editorial?
4. é apenas cenário ilustrativo?
5. é uma capacidade futura?
6. a forma visual faz parecer algo mais forte do que realmente é?

Se a sexta resposta for sim, revisar.

---

## 47. Teste de acessibilidade sem perda de tese

Simular:

- sem vídeo;
- sem animação;
- com movimento reduzido;
- navegação por teclado;
- leitura sequencial;
- tela pequena;
- baixa conectividade.

Pergunta:

> **a pessoa ainda entende a mesma Guivos e chega às mesmas saídas cognitivas?**

A resposta deve ser sim.

---

## 48. Instruções para ferramentas generativas futuras

Se uma ferramenta generativa for utilizada após autorização de materialização, o prompt ou contexto deve incluir explicitamente:

- a hierarquia de fontes;
- os onze movimentos;
- as sete macroexperiências;
- o contrato Header/Hero/CTAs;
- as classes de verdade;
- os critérios de rejeição;
- os anti-padrões;
- a proibição de inventar evidências.

A ferramenta não deve receber apenas o Documento Mestre bruto.

---

## 49. Anti-padrões específicos para geração automática

Instruir ferramentas a não:

- transformar cada parágrafo em card;
- criar onze seções idênticas;
- criar sete containers rígidos só porque existem sete macroexperiências;
- inventar fotos de `parceiros` identificáveis;
- gerar logos;
- gerar métricas;
- gerar países de atuação;
- gerar testimonials;
- gerar dashboards;
- adicionar pricing;
- adicionar formulário de lead;
- criar navbar B2B;
- transformar produtos em uma grade principal;
- usar estética genérica de SaaS;
- usar gradiente de IA como atalho de inovação;
- usar grafo/rede neural como representação automática de conexão;
- representar pessoas como audiência de anúncios.

---

## 50. O que uma ferramenta generativa pode propor futuramente

Após autorização, pode explorar:

- diferentes composições para a mesma macroexperiência;
- ritmo de scroll;
- hierarquia de texto;
- visualizações conceituais de complementaridade;
- formas de representar escala sem mapas genéricos;
- transições entre fragmentação e continuidade;
- maneiras de tornar confiança perceptível;
- diferentes soluções desktop/mobile;
- diferentes intensidades de mídia.

Toda proposta continua sujeita aos critérios de aceite deste handoff.

---

## 51. Handoff mínimo para uma futura sessão de Design

Uma sessão futura de materialização deve receber, no mínimo:

1. `GKR-UX-HOME-OC-MASTER-001`;
2. `GKR-UX-HOME-OC-NARR-001`;
3. `GKR-UX-HOME-OC-NAV-001`;
4. `GKR-UX-HOME-OC-SYS-001`;
5. `GKR-UX-HOME-OC-HANDOFF-001`;
6. `GKR-UX-HOME-SYS-001` como contrato transversal;
7. estado operacional verdadeiro de conteúdo/evidências disponível naquele momento.

Não iniciar materialização usando somente screenshots de referências externas.

---

## 52. Saída esperada do P4

Com este handoff, Design não deve mais precisar decidir estrategicamente:

- qual é a tese;
- quem são os participantes;
- quando produtos aparecem;
- quando a bifurcação acontece;
- o que `Iniciar Jornada` significa;
- que tipo de prova é admissível;
- como tratar cenários;
- se confiança é necessária;
- se Business representa Organizações;
- se Comunidade é produto;
- se Intelligence dá acesso a pessoas.

Essas decisões já estão governadas.

Design continua responsável por materializar forma, ritmo, clareza, hierarquia e experiência quando essa etapa for autorizada.

---

## 53. Estado do bloqueador OC-GAP-04

Resultado deste P4:

> **OC-GAP-04 — Handoff específico para Design/UX/UI: RESOLVIDO EM PRINCÍPIO, SUJEITO À REAUDITORIA P5.**

Isso não significa que a Home está automaticamente liberada para wireframe.

Ainda é necessário confrontar P1, P2, P3 e P4 com os quatro bloqueadores originais e verificar se não restaram contradições ou lacunas materiais.

---

## 54. Próximo gate

Próxima etapa:

> **P5 — Reauditoria final de prontidão pré-materialização.**

O P5 deve verificar pelo menos:

- `OC-GAP-01` — macroexperiências;
- `OC-GAP-02` — Header, Hero e CTAs;
- `OC-GAP-03` — conteúdo, prova e evidência;
- `OC-GAP-04` — handoff para Design/UX/UI;
- coerência transversal com o Documento Mestre;
- coerência com a Home Pública principal;
- fronteira com superfícies autenticadas;
- ausência de materialização prematura.

Resultado admissível do P5:

```text
READY FOR SEPARATE HUMAN DECISION
ON CONCEPTUAL WIREFRAME
```

ou:

```text
STILL BLOCKED
```

Nenhum desses estados equivale a autorização automática de materialização.

---

## 55. Contrato final do handoff

> **A Home Pública de Organizações e Coletivos deve ser materializada como uma segunda porta narrativa para a mesma Guivos: reconhecer capacidades que já existem, revelar a fragmentação entre elas, mostrar como pessoas, Organizações e Coletivos podem se complementar, demonstrar valor e confiança, apresentar a infraestrutura somente quando houver contexto suficiente e, apenas no final, permitir que Organização e Coletivo descubram como continuar participando. Design possui liberdade para transformar essa progressão em experiência, mas não para substituí-la por uma landing page B2B, catálogo de produtos, dashboard, marketplace, rede social, campanha institucional ou narrativa de aquisição.**
