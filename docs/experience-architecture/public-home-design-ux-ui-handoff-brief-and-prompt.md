---
id: GKR-UX-HOME-HANDOFF-001
title: Briefing de Handoff para Design, UX, UI e Wireframe da Home Pública — Especificação e Prompt Mestre
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-28
parent: GKR-UX-HOME-VAL-001
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-001
  - GKR-UX-HOME-VAL-001
  - GKR-UX-HOME-BENCH-001
  - GKR-UX-HOME-BENCH-002
  - GEB-P01-F01
  - GEB-P01-F02
  - GEB-P01-F03
  - GEB-P01-F04
  - GEB-P01-F06
  - GPA-005
related:
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-NARR-001
  - GKR-UX-HOME-NARR-005
  - GKR-UX-HOME-SYS-001
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-GTM-BOUNDARY-001
  - GKR-UX-HOME-AUDIT-001
  - GKR-UX-HOME-AUDIT-002
normative: false
maturity: reconciled_design_handoff_pre_materialization
---

# Briefing de Handoff para Design, UX, UI e Wireframe da Home Pública — Especificação e Prompt Mestre

## 1. Finalidade

Este documento transforma a direção conceitualmente validada da Home pública de `guivos.com` em um **contrato de handoff suficientemente detalhado para orientar etapas futuras de arquitetura visual, UX, UI, wireframe, prototipação e materialização em ferramentas como Figma**, sem executar ou autorizar essas etapas nesta frente.

Nesta versão, o handoff foi reconciliado com o Master vigente, a especificação narrativa detalhada, o agrupamento das macroexperiências, a consolidação da Hero, o sistema de conteúdo/prova, as auditorias de prontidão e integridade e a fronteira Arquitetura × Marketing/GTM.

Ele existe para reduzir perda semântica entre estratégia e design e deve continuar rico o suficiente para ser consumido por diferentes equipes sem obrigá-las a reconstruir a lógica da Home a partir de documentos históricos.

Seu objetivo é permitir que um designer, equipe de produto, agência ou sistema generativo receba uma especificação e compreenda com precisão:

- o que a Home precisa fazer a pessoa perceber;
- o que a Hero precisa comunicar;
- qual é a sequência narrativa da página;
- quais emoções e interpretações são desejadas;
- quais provas devem sustentar a narrativa;
- qual é a diferença entre Possibilidade, Mecanismo e Oportunidade real;
- como o Movimento 06 pode representar uma passagem da Possibilidade à Experiência sem afirmar que toda Possibilidade chegará a uma Experiência nem prometer resultado;
- qual deve ser o papel de Pessoas, Organizações e Coletivos;
- qual deve ser o papel futuro do Guivos Media;
- quando os Produtos Especializados podem aparecer;
- por que Journey possui papel distinto no Movimento 08;
- por que Organização não equivale a Guivos Business;
- por que Intelligence é Produto Especializado transversal e não autoridade totalizante;
- como preservar autonomia, confiança e privacidade;
- quais padrões de qualidade das grandes marcas globais devem ser buscados;
- quais diferenciais próprios da Guivos não podem ser diluídos;
- quais anti-padrões invalidam uma proposta;
- como avaliar se um futuro wireframe ou design está aderente;
- como instruir uma ferramenta generativa sem permitir que ela reinvente a estratégia;
- como separar arquitetura conceitual de disponibilidade operacional e GTM.

Este documento funciona em dois modos:

1. **briefing humano** para design, UX, UI, conteúdo e produto;
2. **prompt mestre estruturado** para ferramentas generativas e assistidas por IA.

---

## 2. Limite desta especificação

Este artefato **não é**:

- wireframe;
- desenho de tela;
- arquivo Figma;
- protótipo;
- design system;
- especificação de componente;
- layout final;
- copy pública final;
- contrato de implementação;
- autorização para desenvolvimento;
- autorização para publicação;
- autorização de GTM;
- início de UXA-102/V5;
- início de D6;
- início de D7;
- início de Product Engineering.

Ele define **intenção, requisitos, sequência semântica, critérios, limites, estados de prova e contratos de preservação** para etapas futuras.

A futura equipe de design pode propor soluções visuais diferentes, desde que preserve integralmente o contrato de significado deste documento e das autoridades superiores.

Regra adicional:

```text
HANDOFF PRONTO
≠ MATERIALIZAÇÃO AUTORIZADA

ARQUITETURA / FUTURO WIREFRAME
≠ DISPONIBILIDADE DE LANÇAMENTO

PUBLICAÇÃO / ATIVAÇÃO
→ exige verdade operacional
```

---

## 3. Regra de precedência

Quando houver conflito entre uma ideia visual futura e a documentação, prevalece:

1. Fundação vigente da Guivos;
2. `GKR-UX-HOME-MASTER-001` como autoridade de consumo da Home;
3. contratos funcionais `UXA-020` e `UXA-021`;
4. `GKR-UX-HOME-001`;
5. `GKR-UX-HOME-VAL-001`;
6. `GKR-UX-HOME-NARR-001` e aprofundamentos especializados em seus domínios;
7. `GKR-UX-HOME-SYS-001` para conteúdo, prova, interação e sistema visual;
8. `GKR-UX-HOME-NAV-001` e refinamentos para navegação;
9. `GKR-UX-HOME-GTM-BOUNDARY-001` para fronteira operacional/GTM;
10. este handoff;
11. benchmark;
12. proposta visual;
13. preferência estética isolada.

As auditorias verificam integridade; não criam por si mesmas nova estratégia.

Benchmark nunca substitui identidade própria.

Design nunca deve reescrever a estratégia para acomodar um padrão visual da moda.

---

## 4. Problema que a Home precisa resolver

A Guivos é maior do que a soma dos seus produtos e não pode ser compreendida corretamente como uma lista de serviços.

Se a Home começar por Journey, Travel, Mall, Business, Media, Intelligence, Ads ou qualquer outro Produto Especializado, existe risco de a marca parecer:

- conglomerado de produtos;
- marketplace;
- portal de benefícios;
- empresa de viagens;
- portal de conteúdo;
- plataforma de IA;
- software genérico;
- comunidade sem tese central.

A Home precisa fazer a pessoa **compreender primeiro a ideia da Guivos e somente depois conhecer sua arquitetura de produtos**.

O problema narrativo central é tornar perceptível que:

> **o mundo contém Pessoas, Organizações, Coletivos, conhecimento, caminhos, experiências e Possibilidades que frequentemente permanecem dispersos, invisíveis ou fora de contexto; a Guivos existe para conectar esse universo, tornar Possibilidades mais visíveis e aproximar Oportunidades reais quando houver materialização legítima e fizerem sentido, preservando a autonomia de cada participante.**

Isso impede três reduções:

```text
POSSIBILIDADE
≠ OPORTUNIDADE

ORGANIZAÇÃO
≠ GUIVOS BUSINESS

INTELLIGENCE
≠ AUTORIDADE PARA DECIDIR A VIDA DO PARTICIPANTE
```

---

## 5. Objetivo primário de design

O futuro design da Home deve fazer uma pessoa chegar, percorrer a narrativa e concluir algo próximo de:

> **“Existe mais mundo possível para mim do que eu imaginava — e a Guivos parece ser um ecossistema sério, humano e global capaz de tornar parte desse universo mais visível e conectado sem decidir a minha vida por mim.”**

O design não deve buscar primeiro:

- deslumbramento tecnológico;
- demonstração de funcionalidades;
- conversão imediata;
- densidade de conteúdo;
- exibição do portfólio de produtos.

Ele deve buscar primeiro:

- abertura de horizonte;
- curiosidade;
- amplitude;
- confiança;
- pertencimento;
- percepção de realidade;
- desejo de descoberta.

---

## 6. Hero — sistema semântico validado

A Hero deve preservar três camadas conceituais.

### 6.1 Camada 1 — pergunta-mãe

> **O que se torna possível quando você entra aqui?**

Função:

- abrir horizonte;
- colocar o visitante dentro da ideia;
- gerar auto-projeção;
- produzir curiosidade;
- iniciar a narrativa sem explicar produtos.

A pergunta não é decorativa. A página inteira deve funcionar como sua resposta.

### 6.2 Camada 2 — amplitude e pertencimento

> **Um mundo maior de possibilidades passa a fazer parte do seu.**

Função:

- ampliar escala emocional;
- introduzir pertencimento;
- comunicar que entrar significa entrar em contexto mais amplo;
- evitar interpretar a Guivos como ferramenta de uma única finalidade.

“Mundo maior” não significa consumo infinito, abundância garantida ou disponibilidade irrestrita.

Significa ampliação de campo de visão e de contexto.

### 6.3 Camada 3 — concretização

Formulação de trabalho vigente:

> **A Guivos conecta Pessoas, Organizações, Coletivos, conhecimento, caminhos e experiências para tornar novas Possibilidades mais visíveis e aproximar Oportunidades reais quando elas fizerem sentido.**

A futura etapa de copy poderá lapidar a redação, mas não deve remover:

- conexão;
- pluralidade de participantes;
- Pessoas, Organizações e Coletivos;
- conhecimento;
- caminhos e experiências;
- distinção entre Possibilidade e Oportunidade;
- Oportunidades reais somente quando houver materialização externa legítima e fizerem sentido;
- ausência de promessa de resultado.

Autonomia é princípio transversal da Home e recebe explicitação própria no Movimento 10; não é requisito adicional exclusivo da terceira camada.

### 6.4 Assinatura institucional e limite de linguagem

A expressão histórica:

> `Do possível ao vivido.`

**não funciona como assinatura complementar da Home nem como segunda assinatura institucional da Guivos.**

Quando a assinatura institucional for aplicada, deve obedecer à autoridade de Marca vigente:

- `Possibility, lived.`;
- `Possibilidade, vivida.` como formulação oficial em português.

A função narrativa antes associada a `Do possível ao vivido` é hoje expressa pelo **Movimento 06 — Da Possibilidade à Experiência**.

---

## 7. Cinco pilares obrigatórios

Toda proposta futura deve ser auditada contra:

### 7.1 Possibilidade

A Home deve sugerir que existe mais do que aquilo que está visível hoje.

Não deve prometer que qualquer Possibilidade será acessível, relevante ou realizável.

### 7.2 Pertencimento

A pessoa deve perceber que um universo maior pode passar a fazer parte de seu contexto.

Não é “mais conteúdo”. É “mais mundo”.

### 7.3 Conexão

A Guivos deve parecer valiosa porque conecta elementos que normalmente existem fragmentados.

### 7.4 Realidade

A tese precisa ser demonstrada com pessoas, histórias, Organizações, Coletivos, experiências, movimentos e evidências reais sempre que houver material governado disponível.

### 7.5 Autonomia

A Guivos amplia possibilidades; não define o destino.

Qualquer design ou copy que pareça dizer “sabemos o que é melhor para você” falha.

---

## 8. Princípio de protagonismo

Regra interna obrigatória:

> **A Guivos não precisa ser o centro da história. Ela precisa ampliar o mundo em que a história pode acontecer.**

Consequências:

- Pessoas não podem parecer figurantes de uma plataforma;
- Organizações não podem ser reduzidas a logos decorativos;
- Coletivos não podem aparecer apenas como prova social;
- experiências não devem parecer mercadorias sem contexto;
- a marca Guivos não deve se apropriar causalmente de toda transformação mostrada;
- quem cria uma Oportunidade continua autor daquilo que cria;
- a Pessoa continua agente de sua escolha e experiência.

A Guivos deve aparecer como conexão, contexto, infraestrutura e facilitadora.

---

## 9. Cadeia conceitual que o design deve sustentar

A progressão perceptiva vigente é:

```text
ENTRAR
→ AMPLIAR
→ DESCOBRIR
→ COMPREENDER / CONECTAR
→ ESCOLHER
→ EXPERIMENTAR
→ APRENDER / EVOLUIR
```

A página não precisa exibir essas palavras literalmente.

Ela precisa fazer a experiência percorrer esse raciocínio.

### ENTRAR
Perceber que “aqui” representa um universo, não apenas uma URL.

### AMPLIAR
Sentir que o campo de Possibilidades ficou maior.

### DESCOBRIR
Encontrar algo real que não estava no campo de visão.

### COMPREENDER / CONECTAR
Entender relações, contexto e por que elementos antes dispersos podem fazer sentido juntos.

### ESCOLHER
Preservar controle e liberdade.

### EXPERIMENTAR
Perceber que algumas Possibilidades podem chegar a experiências concretas por escolha e diferentes mecanismos, inclusive por Oportunidades reais quando existirem.

### APRENDER / EVOLUIR
Reconhecer contribuição, aprendizado ou novo Momento sem impor uma definição universal de sucesso.

---

## 10. Motivação primária desejada

O primeiro desejo que a Home deve gerar é:

> **descobrir.**

A pessoa não precisa chegar querendo:

- comprar;
- criar conta;
- contratar;
- viajar;
- consumir um produto;
- usar IA;
- preencher um diagnóstico.

O design deve criar curiosidade suficiente para que a pessoa queira continuar explorando.

A conversão inicial deve ser entendida como **continuidade voluntária da descoberta**, não como pressão transacional.

---

## 11. Arquitetura narrativa da Home

Esta seção define **funções obrigatórias de narrativa**, não blocos visuais finais.

### 11.1 Movimento 01 — Abrir o Horizonte / Hero

Objetivo:

- apresentar pergunta-mãe;
- comunicar amplitude;
- introduzir a Guivos sem listar produtos;
- fazer continuar descobrindo.

Deve gerar futuro, curiosidade, sofisticação, humanidade e pertencimento.

Não deve gerar campanha motivacional, promessa mágica, confusão com IA ou marketplace.

### 11.2 Movimento 02 — Possibilidades Reais

A primeira grande resposta à Hero deve ser realidade, não arquitetura interna.

Pode mostrar, quando houver acervo governado:

- Pessoa descobrindo algo;
- Organização criando uma Oportunidade legítima;
- Coletivo mobilizando participantes;
- experiência acontecendo;
- conhecimento alterando perspectiva;
- história cujo efeito continua depois do evento inicial.

Pergunta de validação:

> **“Estou vendo uma Possibilidade acontecendo ou apenas uma marca falando sobre possibilidades?”**

### 11.3 Movimento 03 — Amplitude

A Home deve fazer perceber que existem múltiplas formas legítimas de movimento.

Exemplos conceituais, não taxonomia final:

- conhecer;
- aprender;
- criar;
- cuidar;
- trabalhar;
- viajar;
- experimentar;
- contribuir;
- conectar-se;
- participar;
- descobrir.

Nenhuma delas representa definição universal de evolução.

#### 11.3.1 Domínios de Evolução — vocabulário, não taxonomia da Home

A Journey reconhece nove Domínios de Evolução:

1. Saúde e Bem-estar;
2. Trabalho, Carreira e Estudos;
3. Vida Financeira;
4. Empreendedorismo e Projetos;
5. Relacionamentos e Vida Social;
6. Espiritualidade, Propósito e Valores;
7. Viagens, Lazer, Cultura e Novas Experiências;
8. Causas, Voluntariado e Contribuição;
9. Organização e Equilíbrio da Vida.

`Ainda estou descobrindo` é estado transversal, não décimo domínio.

Na Home pública, os Domínios podem funcionar como **vocabulário opcional de amplitude e cobertura da Journey**, quando necessário. Eles não devem automaticamente virar:

- nove cards;
- nove categorias da Home;
- menu principal;
- diagnóstico da Pessoa;
- score de equilíbrio;
- “roda da vida” obrigatória.

A futura materialização deve justificar qualquer uso dos Domínios pelo papel narrativo que cumprem, e não pela existência da taxonomia na Journey.

### 11.4 Movimento 04 — Desconexão

A pessoa deve compreender gradualmente:

> **Possibilidades existem, mas frequentemente permanecem dispersas, invisíveis ou fora de contexto.**

O design pode representar relações, contrastes ou histórias que demonstrem fragmentação sem recorrer obrigatoriamente a diagramas técnicos.

### 11.5 Movimento 05 — Guivos / Conexão

Somente depois de Possibilidade e realidade, aprofundar:

- conexão;
- contexto;
- descoberta;
- relação entre participantes;
- continuidade.

O visitante deve concluir:

> **“Agora entendo por que esse ecossistema precisa existir.”**

### 11.6 Movimento 06 — Da Possibilidade à Experiência

Este movimento possui cadeia própria e não deve ser confundido com o modelo editorial genérico das histórias:

```text
POSSIBILIDADE
→ MECANISMO
→ OPORTUNIDADE REAL, quando houver materialização externa legítima
→ ESCOLHA
→ EXPERIÊNCIA
→ CONTRIBUIÇÃO / APRENDIZADO
→ NOVO MOMENTO
```

Regras:

```text
POSSIBILIDADE
≠ OPORTUNIDADE

EXPERIÊNCIA
≠ RESULTADO GARANTIDO
```

Uma Possibilidade pode ou não chegar a uma Experiência. A cadeia acima representa uma passagem possível e governada, não um funil universal, destino inevitável ou progressão garantida. Nem toda Possibilidade exige Oportunidade externa. Mecanismo pode ser conhecimento, relação, recurso, ferramenta ou outra capacidade que apoia a passagem. A narrativa deve distinguir correlação, contribuição e causalidade e nunca afirmar que a Guivos causou toda mudança quando isso não puder ser sustentado.

### 11.7 Movimento 07 — Pertencimento

Ampliar o campo para mostrar que Pessoas, Organizações e Coletivos descobrem, criam, conectam, compartilham e participam.

A Guivos não é relação binária `plataforma → usuário`.

É ecossistema de participantes.

### 11.8 Movimento 08 — Ecossistema / Produtos

Produtos entram **depois da compreensão do ecossistema**.

A leitura vigente é:

```text
GUIVOS
│
├── JOURNEY
│   └── experiência e continuidade da jornada
│
├── MALL / TRAVEL / BUSINESS / MEDIA / ADS
│   └── Produtos Especializados com responsabilidades próprias
│
└── INTELLIGENCE
    └── Produto Especializado transversal de inteligência / Intelligence Layer
```

Todos os sete permanecem Produtos Especializados.

Regras de preservação:

- Journey não deve virar card equivalente por convenção;
- Organização ≠ Business;
- Business é Produto Especializado B2B;
- Intelligence é Produto Especializado transversal / Intelligence Layer;
- `COMPREENDER ≠ DECIDIR`;
- Movimento 08 explica coerência entre responsabilidades; não replica o launcher.

Regra:

> **produtos servem à ideia; a ideia não serve ao catálogo de produtos.**

### 11.9 Movimento 09 — Autoridade

Autoridade deve ser baseada em evidência.

Fontes possíveis quando reais:

- histórias verificadas;
- parceiros;
- Organizações participantes;
- Coletivos;
- cidades e países;
- experiências realizadas;
- conteúdo editorial;
- dados com fonte e data;
- evolução longitudinal de histórias;
- metodologia e transparência.

Até haver escala operacional, poucas provas verdadeiras são melhores que grandeza simulada.

### 11.10 Movimento 10 — Autonomia e Confiança

A experiência precisa demonstrar:

- a pessoa pode explorar;
- pode não continuar;
- não precisa entregar dados para compreender a Guivos;
- nenhuma recomendação pessoal é simulada publicamente;
- Intelligence amplia compreensão sem substituir decisão;
- nenhum resultado é garantido.

### 11.11 Movimento 11 — Descoberta

O CTA final deve ser semanticamente compatível com:

> **“Quero descobrir o que existe aqui.”**

A redação final será definida depois.

O CTA da Hero e demais CTAs de exploração pública pertencem à continuidade da própria Home. Eles devem permanecer semanticamente distintos de `Iniciar Jornada`, que pertence ao Header como porta própria da Journey e representa uma transição governada para experiência protegida.

```text
CTA PÚBLICO DA HOME / HERO
→ descoberta e continuidade pública
→ sem coleta de contexto pessoal
→ sem onboarding

INICIAR JORNADA
→ Header
→ porta própria da Journey
→ transição governada

JOURNEY PROTEGIDA
→ contexto pessoal somente depois da transição governada
```

A exploração pública não deve solicitar localização, narrativa ou relato pessoal, ativar voz/microfone ou câmera, solicitar upload/arquivo, autenticação avulsa ou qualquer outro dado/contexto pessoal como condição para continuar descobrindo. Também não deve iniciar onboarding autonomamente.

Evitar linguagem que transforme a relação inicial em pressão comercial ou que duplique `Iniciar Jornada` como CTA dominante da Hero.

---

## 12. Regra central da página

> **A Home da Guivos não deve explicar um ecossistema para depois mostrar possibilidades. Deve mostrar possibilidades até que a pessoa naturalmente compreenda por que esse ecossistema precisa existir.**

Esta frase deve ser usada como critério de revisão de qualquer futuro wireframe.

Os onze movimentos são funções; as sete macroexperiências são agrupamentos de referência. Nenhum dos dois conjuntos deve ser automaticamente materializado como número equivalente de blocos pesados.

---

## 13. Conteúdo e prova

### 13.1 Hierarquia de prova

A hierarquia vigente é:

```text
prova direta
> história documentada
> evidência institucional
> métrica
> depoimento
> afirmação institucional
```

Quanto maior a afirmação, maior deve ser a proximidade da evidência.

### 13.2 Modelo editorial das histórias

O modelo editorial transversal é:

```text
CONTEXTO
→ POSSIBILIDADE
→ DECISÃO
→ EXPERIÊNCIA
→ CONSEQUÊNCIA
→ CONTINUIDADE
```

Pergunta editorial:

> **E depois?**

Esse modelo **não obriga Mecanismo nem Oportunidade real em toda história**. A cadeia enriquecida com Mecanismo pertence especificamente ao Movimento 06.

### 13.3 Vídeo

Vídeo forte deve responder a pelo menos uma pergunta:

- o que aconteceu?;
- qual Possibilidade apareceu?;
- quem decidiu?;
- quem tornou aquilo possível?;
- qual experiência foi vivida?;
- qual consequência foi observada?;
- o que aconteceu depois?;
- que novo contexto surgiu?

Vídeo não deve ser decoração cinematográfica sem informação.

### 13.4 Fotografia

Preferir situações reais, contextuais e identificáveis.

Evitar:

- stock genérico;
- pessoas sorrindo sem história;
- luxo como sinônimo de evolução;
- dramatização artificial de sofrimento;
- hologramas e clichês de IA;
- imagens desconectadas do conteúdo.

### 13.5 Histórias longitudinais

Quando possível, mostrar não apenas “o evento”, mas “o que aconteceu depois”.

Esse modelo gera autoridade superior a depoimentos instantâneos, desde que preserve consentimento/autorização aplicável, privacidade, proveniência, contexto, causalidade correta e direito de correção/retirada quando aplicável.

### 13.6 Transparência editorial e conteúdo patrocinado

Conteúdo real não se torna prova orgânica apenas porque é verdadeiro. A futura Home deve preservar classificação e identificação perceptível entre:

```text
CONTEÚDO ORGÂNICO
≠ CONTEÚDO EDITORIAL
≠ CONTEÚDO PATROCINADO
```

Conteúdo patrocinado pode participar da Home quando houver legitimidade editorial e autorização aplicável, mas deve permanecer **identificável como patrocinado** e nunca comprar aparência de prova orgânica, recomendação pessoal ou relevância contextual automática.

A identificação não deve depender apenas de hover, gesto opcional, metadado invisível ou conhecimento prévio do visitante.

---

## 14. Guivos Media na futura experiência

O Guivos Media pode funcionar como fonte editorial de realidade para a Home, sujeito a futura autorização técnica e editorial específica.

Conteúdos potenciais:

- histórias reais;
- vídeos;
- entrevistas;
- documentários;
- séries;
- acontecimentos;
- experiências;
- Pessoas, Organizações e Coletivos;
- conhecimento contextual;
- continuidade e “e depois?”.

A Home não deve virar feed infinito.

Regra de elegibilidade editorial:

> **cada conteúdo deve ajudar a provar ou aprofundar Possibilidade, Experiência, conexão, pertencimento, consequência, continuidade ou autoridade.**

Se serve apenas para aumentar volume, não pertence à Home.

Quando houver conteúdo patrocinado, sua origem/classificação deve permanecer perceptível e separada de conteúdo orgânico ou editorial; patrocínio não converte conteúdo em prova automática nem em recomendação pessoal.

Integração técnica Media → Home não é autorizada por este documento.

---

## 15. Direção visual — percepção, não estilo fechado

O futuro design deve parecer:

- global;
- sofisticado;
- contemporâneo;
- simples;
- humano;
- confiante;
- amplo;
- vivo;
- tecnológico sem frieza;
- aspiracional sem elitismo;
- editorial sem parecer portal de notícias;
- premium sem depender de luxo;
- cinematográfico quando houver conteúdo que justifique;
- claro mesmo quando a infraestrutura por trás for complexa.

Não deve parecer:

- dashboard;
- painel SaaS na abertura;
- landing page de infoproduto;
- marketplace promocional;
- portal de descontos;
- rede social genérica;
- site de agência;
- interface futurista baseada em neon e holograma;
- manifesto abstrato sem prova;
- catálogo de cards homogêneos.

---

## 16. Princípios de composição futura

### 16.1 Uma ideia dominante por momento
Evitar múltiplas mensagens competindo pela atenção.

### 16.2 Respiro como sinal de confiança
Complexidade institucional não deve gerar densidade visual compulsiva.

### 16.3 Hierarquia inequívoca
A pessoa deve saber o que ler, sentir e fazer em cada momento.

### 16.4 Movimento com significado
Animação e transição só devem existir se ajudarem a comunicar entrada, ampliação, conexão, passagem, continuidade ou transformação de contexto.

### 16.5 Realidade acima de ornamento
Uma história verdadeira é mais valiosa que um efeito sofisticado sem conteúdo.

### 16.6 Escala sem frieza
A página deve parecer global sem depender apenas de mapas, globos ou números grandes. Escala também pode ser demonstrada por diversidade de participantes, contextos e relações.

### 16.7 Macroexperiência ≠ template de seção
As sete macroexperiências não devem virar sete blocos corporativos idênticos.

### 16.8 Produto ≠ card equivalente por convenção
A composição deve respeitar responsabilidades distintas, especialmente o papel de Journey e a transversalidade do Intelligence.

---

## 17. UX e interação

### 17.1 Exploração antes de cadastro
O visitante deve compreender a Guivos sem criar conta.

### 17.2 Sem falsa personalização
A Home pública não pode sugerir que conhece o Momento pessoal do visitante antes de contexto autorizado.

### 17.3 Progressive disclosure
Revelar profundidade progressivamente, sem explicar toda a arquitetura no primeiro campo visual.

### 17.4 Controle perceptível
O visitante deve perceber liberdade de explorar, avançar, voltar ou sair.

### 17.5 Interação não pode substituir clareza
A mensagem central deve continuar compreensível sem animação, vídeo ou interação complexa.

Conteúdo essencial não pode depender de hover, clique, swipe, gesto opcional ou outra interação para ser compreendido. Progressive disclosure pode organizar profundidade, mas nunca compensar falta de clareza.

### 17.6 CTA compatível com descoberta
CTAs iniciais privilegiam continuidade e exploração, não urgência comercial artificial.

O CTA da Hero e os CTAs de continuidade pública devem permanecer distintos de `Iniciar Jornada`: a Hero continua a narrativa pública; `Iniciar Jornada` continua sendo a porta própria da Journey no Header. Explorar Possibilidades na Home não pode exigir a entrada na Journey.

Nenhum CTA de exploração pública pode solicitar localização, relato/narrativa pessoal, ativar voz/microfone ou câmera, solicitar upload/arquivo, autenticação avulsa ou outro dado/contexto pessoal, nem iniciar onboarding autonomamente. Contexto pessoal pertence à experiência protegida posterior à transição governada de `Iniciar Jornada`.

### 17.7 Navegação persistente sem dominância
O Header deve permanecer disponível sem dominar a Hero. Sem definir layout final, a futura materialização deve preservar o inventário semântico governado por `GKR-UX-HOME-NAV-001`:

- marca / acesso à Home;
- `Sobre`;
- `Organizações e Coletivos`;
- compartilhar como utilitário;
- idioma/região por controle compacto;
- launcher do ecossistema;
- `Login`;
- `Iniciar Jornada` como CTA de maior hierarquia no Header e porta própria da Journey.

O launcher deve permanecer compacto e conter conceitualmente:

- Travel;
- Ads;
- Media;
- Business;
- Intelligence;
- Mall.

Journey pertence ao ecossistema, aparece no Movimento 08 e pode possuir acessos contextuais, mas **não integra o launcher na hipótese vigente**.

Durante o scroll, o Header pode compactar funcionalmente para reduzir ocupação e preservar contraste, mas sua hierarquia semântica e pressão comercial devem permanecer estáveis. `Iniciar Jornada` permanece disponível sem ganhar pressão perceptiva com a profundidade da rolagem: não pode pulsar, crescer para capturar atenção, surgir apenas depois como gatilho de conversão, virar banner sticky, bloquear conteúdo ou repetir-se desnecessariamente em múltiplas posições.

### 17.8 Estado conceitual ≠ disponibilidade operacional
Um destino pode existir na arquitetura de navegação antes de estar disponível no lançamento. A versão publicada não pode apresentar link, CTA ou estado enganoso.

### 17.9 Rodapé e Mapa do Ecossistema
O rodapé deve preservar um link `Mapa do Ecossistema` ou equivalente posteriormente validado, sem antecipar, desenhar ou especificar a futura página de destino nesta frente.

### 17.10 Equivalência desktop/mobile
Desktop e mobile devem preservar a mesma hierarquia semântica e os mesmos caminhos essenciais. O mobile pode reorganizar a navegação em drawer, grupos progressivos ou solução equivalente, mas não pode eliminar encontrabilidade de produtos essenciais, `Sobre`, `Organizações e Coletivos`, idioma/região, `Login` ou `Iniciar Jornada`.

Além da equivalência semântica, o mobile deve constituir solução semântica própria — não simples empilhamento do desktop — favorecendo foco e sequência sem reduzir a tese.

### 17.11 Autonomia operacional da interação

A futura experiência deve permitir que a pessoa mantenha controle perceptível sobre ritmo e navegação. Portanto:

- scroll permanece normal e não bloqueante;
- não há espera forçada por animação, vídeo ou transição;
- mídia opcional pode ser ignorada;
- não há áudio automático;
- não há modais não solicitados;
- não há notificações simuladas;
- alvos não se movem inesperadamente;
- navegação não desaparece de forma imprevisível;
- não há dark patterns, urgência artificial ou interação coercitiva.

Movimento e sofisticação devem ampliar percepção, nunca transformar o visitante em espectador obrigatório.

---

## 18. Acessibilidade e resiliência

A futura materialização deve ser concebida desde o início para:

- navegação por teclado;
- leitores de tela;
- texto ampliado;
- contraste adequado;
- foco visível;
- legendas;
- transcrição;
- descrição de conteúdo quando necessária;
- redução de movimento;
- baixa conectividade;
- fallback de mídia;
- responsividade;
- tradução e internacionalização;
- alvos de toque adequados;
- ordem semântica de leitura;
- ausência de dependência exclusiva de hover, clique ou gesto opcional.

Texto ampliado deve preservar leitura e compreensão, sem exigir tamanhos fixos incompatíveis com a necessidade do visitante.

Se vídeo não carregar, a tese da Home deve continuar íntegra.

Se animação estiver desabilitada, a sequência deve continuar compreensível.

Se evidência ainda não existir, a solução deve reduzir claim ou usar estado honesto, nunca preencher lacuna com ficção.

---

## 19. Internacionalização

A mensagem e a futura solução visual devem funcionar além do Brasil.

Evitar dependência estrutural de:

- gírias;
- trocadilhos intraduzíveis;
- imagens estereotipadas de um único país;
- definição cultural única de sucesso;
- luxo ou consumo como marcador universal;
- convenções que não sobrevivam à tradução.

A copy deverá ser validada nativamente por idioma.

A arquitetura visual deverá tolerar expansão e contração de texto, scripts diferentes, nomes extensos e diferenças regulatórias por mercado.

Idioma e região são preferências distintas.

---

## 20. Benchmark — o que deve ser igualado

A Guivos não deve copiar estética de players específicos.

Deve buscar paridade de qualidade em atributos independentes de escala empresarial:

- ambição narrativa;
- clareza da ideia-mãe;
- simplicidade;
- segurança visual;
- disciplina de mensagem;
- sofisticação;
- consequência antes de funcionalidade;
- demonstração cedo;
- coerência;
- linguagem global;
- confiança.

Referências analisadas incluem Runway, Linear, Vercel, Stripe, Notion, Anthropic, Canva, Framer, Apple, Palantir, Perplexity e NVIDIA.

Síntese comparativa:

> **As gigantes mostram o futuro que suas tecnologias, produtos ou infraestruturas tornam possível. A Guivos pode mostrar o futuro que novas Possibilidades podem tornar possível na vida real.**

Benchmark é evidência comparativa, não autoridade para copiar estrutura visual.

---

## 21. Diferenciais que não podem ser perdidos no design

### 21.1 Evolução humana sem promessa de transformação
A Guivos pode mostrar mudanças de contexto, experiência e trajetória, sem declarar causalidade ou resultado garantido.

### 21.2 Pertencimento
O visitante não apenas “usa”; pode passar a fazer parte de um universo maior.

### 21.3 Continuidade
A história não precisa terminar no clique ou transação.

### 21.4 Pessoas + Organizações + Coletivos
A página deve representar ecossistema, não somente consumidor final.

### 21.5 Autoridade sem domínio sobre a vida
A Guivos pode ser institucionalmente forte e ainda preservar autonomia.

### 21.6 Mundo real
A prova mais valiosa sai da tela e chega à experiência.

### 21.7 Ecossistema maior que os produtos
Nenhum produto pode se tornar sinônimo da marca inteira.

### 21.8 Possibilidade não é Oportunidade
Possibilidade pode existir como caminho, recurso, experiência ou conexão a considerar; Oportunidade requer materialização concreta em contexto legítimo.

### 21.9 Compreensão não é decisão
Intelligence amplia compreensão; não substitui autoridade de Pessoas, Organizações ou Produtos.

---

## 22. O que a Guivos ainda não pode simular

A futura Home não deve fabricar:

- milhões de usuários inexistentes;
- presença global inexistente;
- histórias fictícias apresentadas como reais;
- empresas participantes inexistentes;
- números sem fonte;
- depoimentos inventados;
- casos de sucesso não comprovados;
- personalização não existente;
- disponibilidade operacional futura como se fosse atual;
- Oportunidade real quando existe apenas Possibilidade conceitual;
- causalidade que não possa ser sustentada.

A marca pode parecer global em qualidade desde o início.

A prova precisa corresponder à realidade do estágio operacional.

---

## 23. Anti-padrões de rejeição imediata

Uma proposta futura deve ser rejeitada ou revista se:

1. abre com lista de produtos;
2. abre explicando IA ou tecnologia;
3. parece marketplace;
4. parece portal de benefícios;
5. parece coaching ou autoajuda;
6. promete transformação pessoal;
7. apresenta Guivos como quem sabe o que é melhor para a pessoa;
8. exige cadastro para entender o ecossistema;
9. depende de stock genérico como principal prova humana;
10. usa luxo, consumo, compras, viagens acumuladas, pontos, rankings, streaks ou produtividade como definição ou proxy de evolução;
11. transforma a Home em feed infinito;
12. coloca patrocinador como prova automática de relevância pessoal;
13. apresenta dezenas de cards sem narrativa;
14. usa efeitos visuais para compensar ausência de tese;
15. copia reconhecidamente outro player;
16. reduz Pessoas, Organizações ou Coletivos a decoração;
17. esconde o papel da Guivos atrás de abstração excessiva;
18. torna a experiência incompreensível sem animação;
19. parece local ou improvisada quando a ambição é global;
20. simula maturidade operacional inexistente;
21. usa `Do possível ao vivido.` como segunda assinatura institucional da Home;
22. confunde Possibilidade com Oportunidade;
23. transforma Organização em Business;
24. transforma Intelligence na Guivos inteira ou em autoridade decisória;
25. achata Journey em card equivalente por convenção;
26. usa a cadeia do Movimento 06 como modelo editorial obrigatório para toda história;
27. bloqueia arquitetura conceitual apenas porque um destino ainda não está lançado;
28. publica destino indisponível como se estivesse operacional;
29. transforma automaticamente os nove Domínios de Evolução em nove cards, categorias da Home, menu, diagnóstico, score ou “roda da vida”;
30. esconde conteúdo essencial atrás de hover, clique, swipe ou gesto opcional, ou usa interação para compensar falta de clareza;
31. usa `Iniciar Jornada` como CTA dominante da Hero ou torna a descoberta pública dependente da entrada na Journey;
32. solicita localização, relato/narrativa pessoal, ativa voz/microfone ou câmera, solicita upload/arquivo, autenticação avulsa ou outro dado/contexto pessoal para continuar a exploração pública;
33. inicia onboarding a partir de CTA público sem a transição governada de `Iniciar Jornada` para a Journey protegida;
34. apresenta conteúdo patrocinado sem identificação perceptível ou o mistura a conteúdo orgânico/editorial de forma que compre aparência de prova orgânica;
35. bloqueia scroll, força espera por animação, inicia áudio automaticamente, abre modal não solicitado, simula notificação, move alvo inesperadamente, esconde navegação de forma imprevisível ou usa qualquer dark pattern;
36. usa tamanhos de texto fixos que impeçam texto ampliado de permanecer legível e compreensível;
37. trata a chegada da Possibilidade à Experiência como inevitável, universal ou garantida;
38. aumenta progressivamente a pressão perceptiva/comercial de `Iniciar Jornada` durante o scroll, inclusive por pulso, crescimento, banner sticky, gatilho tardio de conversão, bloqueio ou repetição desnecessária.

---

## 24. Entregáveis esperados da futura etapa de design

**Somente quando houver autorização explícita**, o trabalho deverá produzir no mínimo:

- mapa narrativo da Home;
- wireframe desktop;
- wireframe mobile como solução semântica própria, não simples empilhamento do desktop, preservando foco, sequência, hierarquia e caminhos essenciais;
- racional de cada movimento narrativo;
- hierarquia de informação;
- pontos de prova real;
- slots editoriais;
- governança dos slots de histórias reais/longitudinais, contemplando consentimento/autorização aplicável, privacidade, proveniência, contexto/causalidade correta e correção/retirada quando aplicável;
- estratégia de Hero;
- comportamento sem vídeo;
- proposta de CTA por estágio;
- mapa de papéis dos CTAs distinguindo exploração pública da Home de `Iniciar Jornada` / entrada na Journey;
- estados de exploração pública sem coleta de contexto pessoal, sem ativação de voz/microfone ou câmera, sem upload e sem onboarding autônomo;
- relação entre Home e Produtos Especializados;
- representação de Pessoas, Organizações e Coletivos;
- proposta de navegação;
- estados responsivos;
- estados vazios ou sem evidência disponível;
- estados de destino disponível / ainda não ativado sem falsa disponibilidade;
- estados de identificação e diferenciação entre conteúdo orgânico, editorial e patrocinado;
- estados de interação que preservem scroll normal, ritmo próprio e ausência de coerção;
- estados do Header durante scroll demonstrando compactação funcional sem aumento da pressão perceptiva/comercial de `Iniciar Jornada`;
- estados de texto ampliado preservando legibilidade e compreensão;
- princípios de movimento;
- critérios de acessibilidade;
- inventário preliminar de componentes;
- tratamento dos Domínios de Evolução, quando utilizados, com justificativa narrativa e sem taxonomia automática;
- riscos e decisões ainda abertas;
- tabela de rastreabilidade entre proposta e movimentos/requisitos.

A entrega não deve apenas “parecer bonita”.

Ela deve demonstrar aderência explícita ao contrato narrativo.

---

## 25. Matriz de aceitação para wireframe/design futuro

Avaliar cada proposta de `0` a `5` em:

- pergunta-mãe preservada;
- possibilidade percebida;
- pertencimento percebido;
- papel da Guivos compreensível;
- realidade demonstrada cedo;
- conexão compreendida;
- autonomia preservada;
- Possibilidade ≠ Oportunidade;
- Movimento 06 coerente, condicional quanto à chegada à Experiência e sem promessa;
- Pessoas / Organizações / Coletivos preservados;
- produtos subordinados à ideia;
- Journey com papel distinto;
- Business ≠ Organização;
- Intelligence transversal sem substituir decisão;
- autoridade por evidência;
- modelo editorial com consequência e continuidade;
- governança de histórias reais/longitudinais preservando consentimento/autorização aplicável, privacidade, proveniência, contexto/causalidade correta e correção/retirada quando aplicável;
- evolução não reduzida a luxo, consumo, compras, viagens acumuladas, pontos, rankings, streaks ou produtividade;
- conteúdo patrocinado identificável e distinguível de orgânico/editorial;
- diferenciação de marketplace/IA/coaching;
- escala global percebida;
- humanidade;
- simplicidade;
- clareza;
- desejo de descoberta;
- acessibilidade estrutural;
- suporte a texto ampliado preservando legibilidade e compreensão;
- robustez sem vídeo/animação;
- conteúdo essencial independente de hover, clique ou gesto opcional;
- autonomia de interação: scroll não bloqueante, sem espera forçada, áudio automático, modal não solicitado, notificação simulada ou dark pattern;
- potencial de internacionalização;
- Domínios de Evolução preservados como vocabulário opcional de amplitude, sem materialização automática;
- CTA da Hero / exploração pública distinto de `Iniciar Jornada`;
- exploração pública sem coleta de localização ou relato, sem ativação de voz/microfone ou câmera, sem upload, autenticação ou outro contexto pessoal;
- onboarding inexistente antes da transição governada para Journey protegida;
- Header persistente preservando marca/Home, `Sobre`, `Organizações e Coletivos`, compartilhar, idioma/região, launcher, `Login` e `Iniciar Jornada`;
- Journey com `Iniciar Jornada` como porta própria e CTA de maior hierarquia no Header;
- pressão perceptiva/comercial de `Iniciar Jornada` estável durante o scroll, sem escalada por profundidade da página;
- launcher compacto contendo Travel, Ads, Media, Business, Intelligence e Mall, sem Journey;
- produtos do launcher acessíveis sem dominar a primeira percepção;
- `Sobre` e `Organizações e Coletivos` claramente encontráveis;
- idioma/região disponível sem poluir o Header;
- compartilhar permanecendo utilitário;
- `Login` disponível sem disputar a narrativa;
- rodapé preservando `Mapa do Ecossistema` como link, sem antecipar a página e sem fechar prematuramente a composição adicional;
- desktop e mobile preservando a mesma hierarquia semântica e os mesmos caminhos essenciais;
- mobile como solução semântica própria, não simples empilhamento do desktop, favorecendo foco e sequência sem reduzir a tese;
- distinção entre destino conceitual governado e disponibilidade operacional;
- verdade operacional nos estados que serão publicados.

### Gate recomendado

Nenhuma proposta deve avançar apenas por nota média alta se obtiver menos de `4/5` em qualquer item crítico:

- papel da Guivos compreensível;
- autonomia;
- produtos subordinados à ideia;
- diferenciação de categorias erradas;
- realidade/prova;
- pergunta-mãe e tese preservadas;
- Possibilidade ≠ Oportunidade;
- Movimento 06 sem inevitabilidade entre Possibilidade e Experiência;
- ausência de promessa de resultado;
- evolução livre de proxies de consumo, luxo ou produtividade;
- governança de histórias reais/longitudinais preservada;
- transparência de conteúdo patrocinado;
- autonomia de interação e ausência de dark patterns;
- estabilidade da pressão perceptiva/comercial de `Iniciar Jornada` durante o scroll;
- acessibilidade com suporte a texto ampliado;
- conteúdo essencial independente de interação opcional;
- mobile como solução semântica própria;
- limites dos Domínios de Evolução preservados;
- CTA público distinto de `Iniciar Jornada` e livre de coleta de contexto pessoal, ativação de voz/microfone ou câmera e upload;
- onboarding somente após transição governada para Journey protegida;
- contrato de navegação vigente preservado;
- verdade operacional daquilo que será publicado.

---

## 26. Perguntas obrigatórias de revisão

Antes de aprovar um futuro wireframe, perguntar:

1. O visitante entende a ideia da Guivos antes dos produtos?
2. A página responde progressivamente “o que se torna possível?”
3. A realidade aparece cedo ou só há discurso?
4. A Guivos parece ecossistema ou catálogo?
5. A pessoa sente amplitude sem promessa vazia?
6. Existe pertencimento?
7. O papel de Pessoas, Organizações e Coletivos está equilibrado?
8. A Guivos aparece como facilitadora, não heroína absoluta?
9. A pessoa conserva controle?
10. A tecnologia está subordinada à consequência humana?
11. A proposta poderia ser confundida com marketplace, IA ou coaching?
12. A página parece global sem ser genérica?
13. Existe sofisticação sem complexidade?
14. O design continua funcionando sem vídeos?
15. Os produtos entram na hora certa?
16. Journey mantém papel distinto no Movimento 08?
17. Business está separado de Organização?
18. Intelligence amplia compreensão sem assumir decisão?
19. Autoridade é comprovada ou autodeclarada?
20. A página desperta vontade de descobrir?
21. A solução é própria da Guivos ou poderia receber outro logo sem mudar nada?
22. Possibilidade e Oportunidade permanecem distintas?
23. O modelo editorial registra decisão, consequência e continuidade quando aplicável?
24. A cadeia com Mecanismo está corretamente restrita ao Movimento 06, sem virar requisito de toda história?
25. Algum estado publicado finge disponibilidade que ainda não existe?
26. Alguma indisponibilidade de lançamento foi usada indevidamente para impedir a arquitetura conceitual?
27. O Header preserva marca/Home, `Sobre`, `Organizações e Coletivos`, compartilhar, idioma/região, launcher, `Login` e `Iniciar Jornada`?
28. Journey permanece fora do launcher e `Iniciar Jornada` é sua porta própria no Header?
29. O launcher contém Travel, Ads, Media, Business, Intelligence e Mall de forma compacta e não dominante?
30. O rodapé mantém `Mapa do Ecossistema` como link sem detalhar a futura página nem fechar prematuramente sua composição adicional?
31. Desktop e mobile preservam os mesmos caminhos essenciais e a mesma hierarquia semântica?
32. Se os nove Domínios de Evolução forem usados, permanecem vocabulário opcional de amplitude ou foram convertidos indevidamente em taxonomia/diagnóstico da Home?
33. A tese e todo conteúdo essencial permanecem compreensíveis sem hover, clique, swipe ou gesto opcional?
34. O CTA da Hero permanece uma porta de descoberta pública distinta de `Iniciar Jornada`?
35. A pessoa consegue continuar a exploração pública sem informar localização ou relato pessoal, sem ativar voz/microfone ou câmera, sem enviar upload/arquivo, sem autenticar-se ou fornecer outro contexto pessoal?
36. Algum CTA público inicia onboarding ou contexto pessoal antes da transição governada para Journey protegida?
37. Conteúdo patrocinado permanece claramente identificável e separado de conteúdo orgânico/editorial, sem comprar aparência de prova ou recomendação?
38. O visitante mantém controle de scroll e ritmo, sem espera forçada, áudio automático, modal não solicitado, notificação simulada, alvo móvel imprevisível ou dark pattern?
39. Com texto ampliado, a experiência preserva legibilidade, compreensão e acesso ao conteúdo essencial?
40. A proposta evita tratar luxo, consumo, compras, viagens acumuladas, pontos, rankings, streaks ou produtividade como definição ou proxy de evolução?
41. Histórias reais/longitudinais preservam consentimento/autorização aplicável, privacidade, proveniência, contexto/causalidade correta e direito de correção/retirada quando aplicável?
42. O mobile é uma solução semântica própria, com foco e sequência, e não simples empilhamento do desktop, sem perder hierarquia ou caminhos essenciais?
43. O Movimento 06 deixa explícito que uma Possibilidade pode ou não chegar a uma Experiência, sem virar funil ou destino inevitável?
44. Durante o scroll, `Iniciar Jornada` permanece disponível sem ganhar pressão perceptiva/comercial por pulso, crescimento, banner sticky, gatilho tardio ou repetição desnecessária?

---

## 27. Prompt Mestre para futura construção assistida por IA

O bloco abaixo é uma base futura para ferramenta generativa de design, Figma assistido por IA ou sistema equivalente. **Seu uso depende de autorização explícita de materialização.**

```text
TAREFA
Crie uma proposta de arquitetura visual, UX/UI e wireframe para a Home pública de guivos.com com base rigorosa na estratégia abaixo. Não reinvente o posicionamento e não transforme a Guivos em marketplace, portal de benefícios, site de viagens, plataforma de IA, rede social, coaching ou catálogo de produtos.

OBJETIVO CENTRAL
A Home deve fazer a pessoa perceber que existe um mundo maior de Possibilidades além do que está visível em seu contexto atual e que a Guivos conecta Pessoas, Organizações, Coletivos, conhecimento, caminhos e experiências para tornar novas Possibilidades mais visíveis e aproximar Oportunidades reais quando elas fizerem sentido, preservando a autonomia do participante.

PERGUNTA-MÃE DA HERO
“O que se torna possível quando você entra aqui?”

SEGUNDA CAMADA
“Um mundo maior de possibilidades passa a fazer parte do seu.”

TERCEIRA CAMADA — SIGNIFICADO OBRIGATÓRIO
“A Guivos conecta Pessoas, Organizações, Coletivos, conhecimento, caminhos e experiências para tornar novas Possibilidades mais visíveis e aproximar Oportunidades reais quando elas fizerem sentido.”
Preserve conexão, pluralidade de participantes, conhecimento, caminhos/experiências, Possibilidade ≠ Oportunidade e ausência de promessa de resultado.

ASSINATURA
Não use “Do possível ao vivido.” como assinatura complementar ou segunda assinatura institucional da Home. A assinatura institucional, quando aplicável, deve seguir a autoridade de Marca vigente. O Movimento 06 chama-se “Da Possibilidade à Experiência”.

PILARES NÃO NEGOCIÁVEIS
1. Possibilidade.
2. Pertencimento.
3. Conexão.
4. Realidade.
5. Autonomia.

PRINCÍPIO DE PROTAGONISMO
“A Guivos não precisa ser o centro da história. Ela precisa ampliar o mundo em que a história pode acontecer.”

CADEIA PERCEPTIVA
ENTRAR → AMPLIAR → DESCOBRIR → COMPREENDER / CONECTAR → ESCOLHER → EXPERIMENTAR → APRENDER / EVOLUIR.

MOTIVAÇÃO PRIMÁRIA
DESCOBRIR.

SEQUÊNCIA NARRATIVA
1. Hero — abrir horizonte.
2. Possibilidades Reais — provar cedo.
3. Amplitude — mostrar caminhos sem taxonomia rígida.
4. Desconexão — mostrar fragmentação sem FOMO.
5. Guivos / Conexão — explicar papel do ecossistema.
6. Da Possibilidade à Experiência — Possibilidade → Mecanismo → eventual Oportunidade real legítima → escolha → eventual Experiência → contribuição/aprendizado → novo Momento. Uma Possibilidade pode ou não chegar a uma Experiência; esta é uma passagem possível e governada, não funil universal, destino inevitável nem promessa de resultado.
7. Pertencimento — Pessoas, Organizações e Coletivos como participantes ativos.
8. Ecossistema / Produtos — Journey com experiência/continuidade; Mall, Travel, Business, Media e Ads com responsabilidades próprias; Intelligence como Produto Especializado transversal / Intelligence Layer. Todos os sete continuam Produtos Especializados. Organização ≠ Business. COMPREENDER ≠ DECIDIR.
9. Autoridade — evidência, fonte, contexto e transparência.
10. Autonomia e Confiança — liberdade, privacidade e ausência de falsa personalização.
11. Descoberta — continuidade voluntária.

DOMÍNIOS DE EVOLUÇÃO
A Journey reconhece nove Domínios: Saúde e Bem-estar; Trabalho, Carreira e Estudos; Vida Financeira; Empreendedorismo e Projetos; Relacionamentos e Vida Social; Espiritualidade, Propósito e Valores; Viagens, Lazer, Cultura e Novas Experiências; Causas, Voluntariado e Contribuição; Organização e Equilíbrio da Vida. “Ainda estou descobrindo” é estado transversal, não décimo domínio. Na Home, use os Domínios apenas como vocabulário opcional de amplitude/cobertura quando necessário. Não os transforme automaticamente em nove cards, nove categorias, menu principal, diagnóstico, score de equilíbrio ou “roda da vida”.

MODELO EDITORIAL DAS HISTÓRIAS
CONTEXTO → POSSIBILIDADE → DECISÃO → EXPERIÊNCIA → CONSEQUÊNCIA → CONTINUIDADE.
Não torne Mecanismo obrigatório em toda história; a cadeia com Mecanismo é específica do Movimento 06.
Histórias reais/longitudinais exigem consentimento/autorização aplicável, privacidade, proveniência, contexto, causalidade correta e direito de correção/retirada quando aplicável.

REGRA CENTRAL
“A Home da Guivos não deve explicar um ecossistema para depois mostrar possibilidades. Deve mostrar possibilidades até que a pessoa naturalmente compreenda por que esse ecossistema precisa existir.”

PERCEPÇÃO VISUAL DESEJADA
Global, sofisticada, contemporânea, simples, humana, confiante, ampla, viva, tecnológica sem frieza, aspiracional sem elitismo, editorial sem parecer portal de notícias, premium sem depender de luxo e clara apesar da complexidade do ecossistema.

NÃO FAZER
- não abrir com lista de produtos;
- não abrir explicando IA, grafo, dados ou arquitetura técnica;
- não usar stock genérico como prova principal;
- não usar hologramas, cérebros digitais ou clichês futuristas;
- não prometer transformação pessoal;
- não simular conhecer o visitante antes de contexto autorizado;
- não criar personalização falsa;
- não exigir conta para compreender a proposta;
- não criar feed infinito;
- não criar catálogo uniforme de cards como estrutura dominante;
- não achatar Journey em card equivalente;
- não confundir Organização com Business;
- não transformar Intelligence em autoridade totalizante;
- não confundir Possibilidade com Oportunidade;
- não tratar luxo, consumo, compras, viagens acumuladas, pontos, rankings, streaks ou produtividade como definição ou proxy de evolução;
- não materializar automaticamente os nove Domínios como nove cards/categorias, menu, diagnóstico, score ou “roda da vida”;
- não ocultar conteúdo essencial atrás de hover, clique, swipe ou gesto opcional;
- não usar Iniciar Jornada como CTA dominante da Hero nem obrigar entrada na Journey para explorar a Home;
- não transformar o Movimento 06 em passagem inevitável até uma Experiência;
- não aumentar a pressão perceptiva/comercial de Iniciar Jornada durante o scroll por pulso, crescimento, banner sticky, gatilho tardio de conversão, bloqueio de conteúdo ou repetição desnecessária;
- não solicitar localização, narrativa/relato pessoal, upload/arquivo, autenticação ou outro contexto pessoal para continuar a descoberta pública;
- não ativar voz/microfone ou câmera nem solicitar/usar upload para explicar a Guivos ou condicionar a descoberta pública;
- não iniciar onboarding a partir de CTA público antes da transição governada para Journey protegida;
- não apresentar conteúdo patrocinado como orgânico/editorial nem omitir sua identificação perceptível;
- não bloquear scroll, forçar espera por animação, iniciar áudio automaticamente, abrir modal não solicitado, simular notificação, mover alvo inesperadamente, esconder navegação de forma imprevisível ou usar dark patterns;
- não usar tamanhos fixos que impeçam texto ampliado de permanecer legível e compreensível;
- não simular escala, usuários, histórias, parceiros, métricas ou disponibilidade inexistentes;
- não copiar visualmente benchmarks.

CONTEÚDO E PROVA
Priorize Pessoas reais, histórias reais, Organizações reais, Coletivos reais, experiências reais, conhecimento contextualizado e consequências observáveis. Sempre que possível mostre “o que aconteceu depois”. Histórias reais/longitudinais só podem participar quando preservarem consentimento/autorização aplicável, privacidade, proveniência, contexto, causalidade correta e direito de correção/retirada quando aplicável. Guivos Media pode futuramente alimentar slots editoriais, mas a Home não deve virar portal de conteúdo. Preserve distinção clara entre conteúdo orgânico, editorial e patrocinado. Conteúdo patrocinado deve permanecer identificável e nunca adquirir aparência de prova orgânica, recomendação pessoal ou relevância automática.

PRODUTOS
Os sete Produtos Especializados só ganham protagonismo institucional após a tese maior estar compreendida. Preserve responsabilidades diferentes. Journey possui experiência e continuidade. Intelligence é transversal sem deixar de ser Produto Especializado. Business não representa automaticamente Organizações.

NAVEGAÇÃO E GTM
Preserve o contrato semântico de navegação vigente. O Header deve permanecer persistentemente disponível sem dominar a Hero e manter marca/Home, Sobre, Organizações e Coletivos, compartilhar, idioma/região, launcher do ecossistema, Login e Iniciar Jornada. Sobre deve permanecer facilmente encontrável; Organizações e Coletivos deve possuir porta clara; compartilhar deve permanecer utilitário; idioma/região deve permanecer disponível de forma compacta e sem poluir o Header; Login deve permanecer disponível sem disputar a narrativa. Iniciar Jornada é o CTA de maior hierarquia no Header e a porta própria da Journey. Journey não integra o launcher. O launcher deve conter Travel, Ads, Media, Business, Intelligence e Mall de forma compacta, acessível e sem dominar a primeira percepção. Durante o scroll, o Header pode compactar funcionalmente, mas não pode aumentar progressivamente a pressão comercial/perceptiva de Iniciar Jornada; sua disponibilidade permanece persistente sem pulso, crescimento para capturar atenção, banner sticky, surgimento tardio como gatilho de conversão, bloqueio ou repetição desnecessária. O rodapé deve preservar Mapa do Ecossistema somente como link, sem antecipar a página de destino; sua composição adicional permanece deliberadamente aberta nesta frente. Desktop e mobile devem preservar a mesma hierarquia semântica e os mesmos caminhos essenciais; o mobile deve ser solução semântica própria, não simples empilhamento do desktop, favorecendo foco e sequência sem reduzir a tese. Arquitetura conceitual/wireframe não depende de todos os destinos estarem lançados; a versão publicada, porém, nunca pode apresentar destino, CTA ou estado como operacional quando não estiver legitimamente disponível.

CTA PÚBLICO × JOURNEY
O CTA da Hero pertence à continuidade pública da própria Home e deve ser semanticamente distinto de Iniciar Jornada. Não use Iniciar Jornada como CTA dominante da Hero. Iniciar Jornada permanece no Header como porta própria da Journey e transição governada para experiência protegida. A descoberta pública não depende da entrada na Journey.

A exploração pública deve continuar sem coleta de contexto pessoal: não peça localização, narrativa/relato pessoal, upload/arquivo, autenticação ou outro dado/contexto pessoal e não inicie onboarding autonomamente. Não ative voz/microfone ou câmera nem solicite/use upload para explicar a Guivos ou condicionar a exploração pública. Contexto pessoal só começa depois da transição governada para Journey protegida.

UX
Permita exploração sem cadastro. Use progressive disclosure para organizar profundidade, nunca para esconder a tese essencial. Conteúdo essencial deve permanecer compreensível sem hover, clique, swipe ou gesto opcional; interação não pode compensar falta de clareza. Preserve liberdade de avançar, voltar ou sair e controle do próprio ritmo. Scroll não pode ser bloqueado; não force espera por animação; não inicie áudio automaticamente; não abra modais sem solicitação; não simule notificações; não mova alvos inesperadamente; não esconda navegação de forma imprevisível; não use dark patterns. Garanta compreensão sem vídeo, sem animação e em baixa conectividade.

ACESSIBILIDADE
Planeje teclado, foco, leitores de tela, **texto ampliado**, contraste, legendas, transcrição, redução de movimento, fallback de mídia, alvos de toque, responsividade e internacionalização desde o wireframe. Texto ampliado deve preservar legibilidade e compreensão; não dependa de tamanhos fixos incompatíveis com a necessidade do visitante.

BENCHMARK — QUALIDADES A IGUALAR
Busque ambição narrativa, clareza, simplicidade, segurança visual, sofisticação, consequência antes de funcionalidade, demonstração cedo, coerência, linguagem global e confiança. Use referências globais como evidência comparativa, nunca como identidade a copiar.

DIFERENCIAL GUIVOS
“As gigantes mostram o futuro que suas tecnologias, produtos ou infraestruturas tornam possível. A Guivos pode mostrar o futuro que novas Possibilidades podem tornar possível na vida real.”

ENTREGUE
1. arquitetura narrativa;
2. wireframe desktop;
3. wireframe mobile como solução semântica própria, não simples empilhamento do desktop, preservando foco, sequência, hierarquia e caminhos essenciais;
4. racional dos movimentos;
5. hierarquia de conteúdo;
6. estratégia da Hero;
7. slots de prova e histórias com classificação orgânico/editorial/patrocinado quando aplicável e governança de histórias reais/longitudinais;
8. representação de Pessoas, Organizações e Coletivos;
9. tratamento do Movimento 08 e responsabilidades dos Produtos;
10. CTAs coerentes com descoberta/autonomia e explicitamente separados entre exploração pública e Iniciar Jornada;
11. comportamento com e sem vídeo;
12. princípios de movimento e controles de ritmo sem scroll bloqueado, espera forçada ou interação coercitiva;
13. estados responsivos;
14. acessibilidade, incluindo estado de texto ampliado preservando legibilidade e compreensão;
15. inventário preliminar de componentes;
16. decisões abertas;
17. estados honestos para destinos ainda não ativados;
18. tabela de rastreabilidade contra os requisitos;
19. proposta de navegação rastreável ao contrato vigente, cobrindo Header, launcher, Journey, rodapé, equivalência desktop/mobile e estabilidade de pressão do CTA durante scroll;
20. justificativa de qualquer uso dos Domínios de Evolução, demonstrando que não foram convertidos automaticamente em taxonomia/diagnóstico da Home;
21. estados de exploração pública sem coleta de contexto pessoal, sem ativação de voz/microfone ou câmera, sem upload e sem onboarding antes da transição governada para Journey protegida;
22. estados de identificação perceptível para conteúdo patrocinado e distinção de conteúdo orgânico/editorial.

CRITÉRIO FINAL
A solução deve fazer alguém pensar primeiro “existe mais mundo possível aqui”, depois “isso acontece de verdade”, depois “entendo por que a Guivos conecta isso”, depois “continuo livre para escolher”, e somente então “quero descobrir o que existe aqui”.
```

---

## 28. Prompt curto para exploração inicial

**Uso somente quando materialização futura estiver explicitamente autorizada.**

```text
Projete a Home pública da Guivos como entrada para um ecossistema global de Possibilidades humanas e institucionais, não como catálogo de produtos. A pergunta-mãe é “O que se torna possível quando você entra aqui?”. A percepção seguinte deve ser “Um mundo maior de possibilidades passa a fazer parte do seu.” A Guivos conecta Pessoas, Organizações, Coletivos, conhecimento, caminhos e experiências para tornar Possibilidades mais visíveis e aproximar Oportunidades reais quando elas fizerem sentido, preservando autonomia.

Não use `Do possível ao vivido.` como assinatura complementar ou segunda assinatura institucional da Home; essa expressão pertence ao território autoral do fundador. Se houver assinatura institucional da Guivos, ela deve seguir a autoridade de Marca vigente.

Mostre Possibilidade antes de produto, prova antes de autodeclaração e mundo real antes de tecnologia. Possibilidade não é sinônimo de Oportunidade. O Movimento 06 é “Da Possibilidade à Experiência” e deve preservar Mecanismo, com Oportunidade real somente quando houver materialização externa legítima. Uma Possibilidade pode ou não chegar a uma Experiência: o Movimento 06 representa uma passagem possível e governada, não funil universal, destino inevitável ou promessa de resultado. O modelo editorial geral continua Contexto → Possibilidade → Decisão → Experiência → Consequência → Continuidade. Histórias reais/longitudinais exigem consentimento/autorização aplicável, privacidade, proveniência, contexto, causalidade correta e direito de correção/retirada quando aplicável.

No Movimento 08, preserve Journey como experiência/continuidade, Mall/Travel/Business/Media/Ads com responsabilidades próprias e Intelligence como Produto Especializado transversal / Intelligence Layer. Todos os sete são Produtos Especializados. Organização não é Business. Intelligence amplia compreensão e não decide pelo participante.

Os nove Domínios de Evolução da Journey são vocabulário opcional de amplitude/cobertura na Home, quando necessário; não os transforme automaticamente em nove cards/categorias, menu, diagnóstico, score ou “roda da vida”. “Ainda estou descobrindo” é estado transversal, não décimo domínio.

Preserve também o contrato de navegação: Header persistentemente disponível com marca/Home, Sobre, Organizações e Coletivos, compartilhar, idioma/região, launcher, Login e Iniciar Jornada; Journey fora do launcher e Iniciar Jornada como sua porta própria e CTA de maior hierarquia no Header; launcher compacto com Travel, Ads, Media, Business, Intelligence e Mall; Mapa do Ecossistema preservado como link no rodapé sem antecipar sua página, mantendo a composição adicional do rodapé aberta; equivalência semântica entre desktop e mobile, com mobile como solução semântica própria — não simples empilhamento do desktop — favorecendo foco e sequência. Durante o scroll, o Header pode compactar funcionalmente, mas a pressão perceptiva/comercial de Iniciar Jornada não pode aumentar com a profundidade da página: sem pulso, crescimento para capturar atenção, banner sticky, gatilho tardio de conversão, bloqueio ou repetição desnecessária. Destino conceitual governado não significa disponibilidade operacional.

O CTA da Hero pertence à descoberta pública da própria Home e deve ser distinto de Iniciar Jornada; não use Iniciar Jornada como CTA dominante da Hero nem obrigue entrada na Journey para explorar Possibilidades. A exploração pública deve continuar sem localização, relato/narrativa pessoal, upload/arquivo, autenticação ou outro contexto pessoal e sem iniciar onboarding; não ative voz/microfone ou câmera nem solicite/use upload para explicar a Guivos ou condicionar essa exploração. Contexto pessoal começa somente depois da transição governada para Journey protegida.

Conteúdo patrocinado deve ser perceptivelmente identificado e distinguido de conteúdo orgânico/editorial; nunca o apresente como prova orgânica ou recomendação pessoal. Preserve controle do visitante: scroll não bloqueante, sem espera forçada, áudio automático, modal não solicitado, notificação simulada, alvo móvel inesperado ou dark pattern.

Garanta acessibilidade desde a arquitetura: teclado, foco, leitores de tela, **texto ampliado**, contraste, legendas/transcrições quando aplicáveis, reduced motion, fallback de mídia e alvos de toque. Texto ampliado deve permanecer legível e compreensível.

Use progressive disclosure sem esconder a tese essencial. Conteúdo essencial deve permanecer compreensível sem hover, clique, swipe ou gesto opcional; interação não pode compensar falta de clareza. A sensação deve combinar futuro, possibilidade, pertencimento, humanidade, confiança, simplicidade e escala global. A motivação inicial é descobrir. Não criar marketplace, portal de benefícios, coaching, site de IA, feed infinito ou catálogo de cards. Não trate luxo, consumo, compras, viagens acumuladas, pontos, rankings, streaks ou produtividade como definição ou proxy de evolução. Não prometer transformação nem simular personalização ou disponibilidade operacional. A Guivos amplia o horizonte; o caminho continua sendo do participante.
```

---

## 29. Como usar este documento no processo futuro

Fluxo governado de consumo:

```text
FUNDAÇÃO + UXA-020/021
→ GKR-UX-HOME-MASTER-001
→ VAL / NARR / SYS / NAV especializados
→ GKR-UX-HOME-HANDOFF-001
→ AUDITORIA / GATE EXPLÍCITO
→ [SOMENTE SE AUTORIZADO]
   exploração de arquitetura visual
→ wireframe
→ validação contra matriz e rastreabilidade
→ UX/UI
→ protótipo
→ validação de conteúdo e acessibilidade
→ especificação de implementação
```

Nenhuma etapa deve eliminar o vínculo com as autoridades anteriores.

O handoff não deve ser consumido isoladamente contra o Master quando houver futura atualização estratégica.

---

## 30. Gate de passagem para Figma / design

Antes de autorizar materialização, confirmar:

- existe autorização explícita da fase;
- pergunta-mãe continua válida;
- três camadas da Hero estão semanticamente preservadas;
- assinatura institucional vigente está correta e `Do possível ao vivido.` não foi reintroduzido como assinatura da Home;
- cinco pilares continuam aceitos;
- sequência narrativa continua aceita;
- Movimento 06 e distinção Possibilidade/Oportunidade estão corretos, com chegada à Experiência explicitamente condicional;
- modelo editorial continua separado da cadeia específica do Movimento 06;
- evolução não está definida ou inferida por luxo, consumo, compras, viagens acumuladas, pontos, rankings, streaks ou produtividade;
- Movimento 08 e hierarquia dos Produtos estão reconciliados;
- limites dos nove Domínios de Evolução estão preservados, sem taxonomia/diagnóstico automático da Home;
- Business ≠ Organização;
- Intelligence preserva `COMPREENDER ≠ DECIDIR`;
- papel de Guivos Media está delimitado;
- histórias reais/longitudinais preservam consentimento/autorização aplicável, privacidade, proveniência, contexto/causalidade correta e correção/retirada quando aplicável;
- não houve mudança de contrato funcional da Home;
- conteúdo essencial permanece compreensível sem hover, clique ou gesto opcional;
- acessibilidade inclui suporte explícito a texto ampliado com legibilidade e compreensão preservadas;
- conteúdo patrocinado permanece identificável e distinto de orgânico/editorial;
- controles de interação preservam scroll normal, ritmo próprio e ausência de espera forçada, áudio automático, modal não solicitado, notificação simulada ou dark pattern;
- `Iniciar Jornada` permanece persistentemente disponível sem aumento de pressão perceptiva/comercial durante o scroll;
- CTA da Hero / exploração pública permanece distinto de `Iniciar Jornada`;
- exploração pública permanece sem localização, relato/narrativa pessoal, ativação de voz/microfone ou câmera, upload/arquivo, autenticação ou outro contexto pessoal;
- onboarding e contexto pessoal só começam depois da transição governada para Journey protegida;
- não existe nova personalização pública autorizada por inferência;
- disponibilidade real de provas, histórias e métricas está identificada;
- produtos e nomenclaturas vigentes estão reconciliados;
- contrato de navegação vigente foi preservado, incluindo Header, launcher, porta própria da Journey, `Mapa do Ecossistema` no rodapé e equivalência desktop/mobile;
- mobile foi tratado como solução semântica própria, não simples empilhamento do desktop, preservando foco, sequência, hierarquia e caminhos essenciais;
- fronteira arquitetura × GTM foi respeitada;
- estados que serão publicados são operacionalmente verdadeiros;
- escopo da etapa de design está explicitamente autorizado.

Estado atual deste documento:

> **BRIEFING RECONCILIADO — MATERIALIZAÇÃO NÃO AUTORIZADA.**

---

## 31. Síntese executiva para equipes futuras

Se este documento tivesse de ser condensado em regras de controle — sem substituir sua leitura integral — seriam:

1. **Comece pela Possibilidade, não pelo produto.**
2. **Faça a Home inteira responder “o que se torna possível?”.**
3. **Mostre realidade cedo.**
4. **Faça a pessoa sentir que um mundo maior pode passar a fazer parte de seu contexto.**
5. **Explique a Guivos como conexão, não catálogo.**
6. **Deixe Pessoas, Organizações e Coletivos serem protagonistas.**
7. **Preserve Possibilidade ≠ Oportunidade.**
8. **Use Da Possibilidade à Experiência como passagem possível, sem tornar a Experiência inevitável nem prometer resultado.**
9. **Separe o modelo editorial geral da cadeia específica do Movimento 06.**
10. **Preserve a hierarquia dos Produtos e o papel distinto de Journey.**
11. **Não transforme os nove Domínios de Evolução em taxonomia ou diagnóstico da Home por convenção.**
12. **Não confunda Organização com Business.**
13. **Faça Intelligence compreender, não decidir.**
14. **Construa autoridade por prova, transparência, consequência e continuidade.**
15. **Mantenha conteúdo patrocinado identificável e separado de orgânico/editorial.**
16. **Mantenha autonomia e descoberta acima de pressão comercial.**
17. **Preserve scroll, ritmo e controle do visitante; não use dark patterns.**
18. **Garanta texto ampliado legível e compreensível desde a arquitetura.**
19. **Mantenha o CTA da Hero como exploração pública distinta de `Iniciar Jornada`.**
20. **Não colete contexto pessoal, não ative voz/microfone ou câmera, não use upload nem inicie onboarding durante a descoberta pública.**
21. **Não use interação para compensar falta de clareza nem esconda conteúdo essencial atrás de gesto opcional.**
22. **Entregue qualidade global sem copiar a identidade de nenhuma referência.**
23. **Não trate disponibilidade de lançamento como gate da arquitetura conceitual.**
24. **Nunca publique disponibilidade que não exista.**
25. **Não use este handoff como autorização automática de materialização.**
26. **Não defina evolução por luxo, consumo, compras, viagens acumuladas, pontos, rankings, streaks ou produtividade.**
27. **Governe histórias reais/longitudinais com consentimento, privacidade, proveniência, contexto/causalidade correta e direitos aplicáveis de correção/retirada.**
28. **Trate mobile como solução semântica própria, não simples empilhamento do desktop.**
29. **Mantenha `Iniciar Jornada` persistentemente disponível sem aumentar sua pressão perceptiva/comercial com o scroll.**

---

## 32. Formulação final de controle

> **A futura Home da Guivos será considerada aderente quando conseguir transformar uma ideia institucional complexa em uma experiência simples: a pessoa entra, percebe um mundo maior de Possibilidades, vê que esse mundo é real, entende que a Guivos conecta Pessoas, Organizações, Coletivos, conhecimento, caminhos e experiências, compreende que Oportunidades reais são materializações concretas e não sinônimo de Possibilidade, percebe responsabilidades coerentes dentro do ecossistema, preserva a própria autonomia e sente vontade de descobrir o que pode vir depois.**

E, até que exista autorização explícita:

```text
DOCUMENTAÇÃO RECONCILIADA
≠ DESIGN INICIADO

HANDOFF PRONTO
≠ WIREFRAME AUTORIZADO

ARQUITETURA CONCEITUAL
≠ LANÇAMENTO

PUBLICAÇÃO
→ SOMENTE COM VERDADE OPERACIONAL
```
