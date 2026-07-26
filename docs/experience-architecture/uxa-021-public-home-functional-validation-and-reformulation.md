---
id: UXA-021
title: Validação Funcional e Reformulação da Página Inicial Pública da Guivos
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-000
depends_on:
  - UXA-001
  - UXA-009
  - UXA-011
  - UXA-020
related:
  - UXA-002
  - UXA-003
  - UXA-006
  - UXA-010
  - UXA-011-A1
normative: false
---

# Validação Funcional e Reformulação da Página Inicial Pública da Guivos

## 1. Finalidade

Este documento registra a primeira validação funcional detalhada da **Página Inicial pública da Guivos** e reformula sua hierarquia para que uma pessoa compreenda, sem compartilhar informações pessoais:

1. o que é a Guivos;
2. como o ecossistema pode ser utilizado;
3. quais caminhos estão disponíveis;
4. o que acontecerá caso decida iniciar uma jornada;
5. que explorar a Guivos não exige autenticação ou personalização;
6. que nenhuma decisão será tomada pela pessoa.

A validação não trata a Home como design visual final. Ela avalia a responsabilidade funcional, a ordem do conteúdo, as ações, os estados e os limites da superfície pública.

## 2. Pergunta funcional da Home

A Página Inicial deverá responder, no menor esforço razoável:

> **O que é a Guivos, como ela pode apoiar pessoas, Organizações e Coletivos, e qual caminho posso escolher agora sem entregar informações pessoais?**

Uma pessoa não deverá precisar conhecer previamente os nomes dos produtos ou o vocabulário arquitetural da Guivos para compreender a proposta.

## 3. Gate obrigatório da Fundação

A superfície foi avaliada segundo:

- Essência da Guivos;
- Propósito;
- Missão Operacional;
- Visão de Longo Prazo;
- Constituição da Guivos;
- Princípios Permanentes;
- presença companheira;
- autonomia e voluntariedade;
- privacidade e compartilhamento mínimo;
- transparência comercial;
- acessibilidade;
- ausência de coerção, vigilância ou intimidade artificial;
- coerência entre Guivos Journey, Guivos Mall, Guivos Travel, Guivos Business, Guivos Media, Guivos Intelligence e Guivos Ads.

Falha material em qualquer dimensão impede avanço para protótipo, design, testes, especificação técnica ou desenvolvimento.

## 4. Cenários utilizados na validação

### 4.1 Primeira visita sem conhecimento prévio

Uma pessoa chega à Home por pesquisa, indicação ou comunicação pública e ainda não sabe:

- o que a Guivos faz;
- o que significa iniciar uma jornada;
- quais soluções fazem parte do ecossistema;
- se precisará criar conta;
- se receberá uma oferta comercial;
- quais dados serão solicitados.

### 4.2 Exploração sem intenção de iniciar jornada

Uma pessoa deseja apenas conhecer conteúdos, produtos, serviços, viagens, Organizações, Coletivos ou oportunidades gerais.

Ela não deverá ser bloqueada, pressionada ou tratada como perfil incompleto.

### 4.3 Chegada por uma solução específica

Uma pessoa chega por referência ao Guivos Mall, Guivos Travel, Guivos Media, Guivos Business ou outra solução e precisa compreender que essa solução integra um ecossistema maior, sem ser desviada de forma obrigatória para a jornada pessoal.

### 4.4 Pessoa autenticada com jornada ativa

Uma pessoa já possui jornada iniciada, mas acessa voluntariamente a Home institucional. A superfície deverá reconhecer o estado de entrada sem revelar informações pessoais e oferecer acesso claro à Tela Hoje.

### 4.5 Representante de Organização ou participante de Coletivo

Uma pessoa busca conhecer como a Guivos se relaciona com Organizações ou Coletivos. Ela deverá encontrar caminhos institucionais claros sem confundir essas experiências com a jornada pessoal.

### 4.6 Acessibilidade, baixa conectividade e operação internacional

A proposta precisa continuar compreensível:

- com texto ampliado;
- por navegação assistiva;
- sem imagens ou animações;
- com conexão limitada;
- em outro idioma;
- quando alguma solução ainda não estiver disponível na região.

## 5. Diagnóstico da versão inicial

A versão anterior estabeleceu corretamente:

- separação entre Home pública, início protegido da jornada e Tela Hoje;
- convite voluntário para iniciar;
- exploração sem personalização;
- bloqueio de coleta pública;
- explicação de privacidade e controle;
- apresentação das sete soluções oficiais;
- manutenção da Tela Hoje como entrada recorrente.

A validação identificou, contudo, riscos funcionais que exigem reformulação.

### 5.1 A abertura permanecia abstrata

A frase `Toda jornada começa no momento em que você está agora` comunica propósito, mas não explica sozinha o que é a Guivos.

Uma pessoa poderia interpretar a Home como serviço de aconselhamento, terapia, rede social, curso, marketplace ou assistente genérico.

A frase de propósito deverá ser acompanhada por uma descrição concreta da função do ecossistema.

### 5.2 A ação principal aparecia antes da compreensão suficiente

`Iniciar minha jornada` é uma ação coerente, mas pode ser ambígua para quem ainda não sabe o que acontecerá depois.

A ação deverá permanecer visível, acompanhada por uma explicação curta e por uma alternativa equivalente de exploração sem personalização.

### 5.3 O ecossistema aparecia como lista plana

Apresentar sete produtos com a mesma importância pode:

- sobrecarregar a primeira visita;
- transformar a Home em catálogo corporativo;
- sugerir que todas as soluções possuem a mesma finalidade e o mesmo público;
- apresentar Guivos Ads como benefício pessoal genérico;
- reduzir a compreensão do propósito comum.

As soluções deverão ser organizadas por finalidade e tipo de relação com a Guivos.

### 5.4 A Home não distinguia suficientemente os caminhos de entrada

A pessoa precisa compreender que poderá:

- iniciar uma jornada pessoal;
- explorar o ecossistema sem personalização;
- conhecer caminhos para Organizações e Coletivos;
- entrar em uma conta existente.

Esses caminhos não deverão competir como ações principais equivalentes.

### 5.5 Privacidade poderia parecer aviso isolado

A proteção de dados não deverá aparecer apenas como bloco jurídico ou defensivo.

Ela deverá ser demonstrada no comportamento da própria superfície:

- ausência de coleta pública;
- explicação anterior à transição;
- ausência de personalização simulada;
- identificação de publicidade;
- acesso visível a privacidade, segurança e acessibilidade.

### 5.6 Exemplos e oportunidades gerais poderiam simular relevância

Qualquer conteúdo, oportunidade, produto, serviço, viagem ou atividade apresentado antes da personalização poderá ser confundido com indicação pessoal.

A origem, o caráter geral e a eventual relação comercial deverão permanecer explícitos.

### 5.7 A Home não possuía tratamento suficiente para pessoas já autenticadas

A ação principal precisa variar conforme o estado real sem transformar a Home em painel pessoal.

Uma pessoa com jornada ativa deverá encontrar `Ir para a Tela Hoje`, enquanto a apresentação pública da Guivos permanece preservada.

## 6. Decisões de reformulação

### 6.1 O primeiro campo visual deverá explicar a Guivos concretamente

O primeiro campo visual deverá conter:

1. identidade da Guivos;
2. uma frase de propósito;
3. uma descrição concreta do ecossistema;
4. a ação principal adequada ao estado;
5. uma ação alternativa de exploração geral;
6. uma garantia curta de que a Home não coleta relatos pessoais.

Formulação de referência, não definitiva:

> **Toda jornada começa no momento em que você está agora.**
>
> A Guivos é um ecossistema que ajuda pessoas a compreender seu momento, organizar objetivos e conhecer possibilidades de produtos, serviços, experiências, conteúdos, Organizações e Coletivos, mantendo cada decisão sob seu controle.

A formulação não poderá prometer transformação, diagnóstico, oportunidade ou resultado.

### 6.2 Ações principais deverão ser limitadas e hierarquizadas

Para visitante sem jornada:

- ação principal: `Iniciar minha jornada`;
- ação secundária: `Explorar sem personalização`;
- ação utilitária: `Entrar`.

Para pessoa autenticada com jornada ativa:

- ação principal: `Ir para a Tela Hoje`;
- ação secundária: `Conhecer o ecossistema`.

Para pessoa autenticada com relato em andamento:

- ação principal: `Continuar minha jornada`;
- ação secundária: `Explorar sem personalização`.

A ação `Continuar depois` não deverá aparecer como comando permanente da Home, pois fechar ou sair já constitui uma escolha legítima.

### 6.3 A Home deverá explicar o funcionamento antes de apresentar produtos

A sequência curta será:

```text
você conhece a Guivos
→ decide se deseja iniciar
→ conta seu momento em ambiente protegido
→ revisa o que foi compreendido
→ considera possibilidades explicadas
→ escolhe seus próprios Próximos Passos
```

A Home não deverá sugerir que o acesso às soluções depende de iniciar uma jornada.

### 6.4 Caminhos de entrada deverão permanecer distintos

A superfície apresentará três caminhos compreensíveis:

#### Caminho pessoal

- iniciar ou continuar uma jornada;
- compreender Momento Atual, objetivos e Próximos Passos;
- acessar a Tela Hoje quando aplicável.

#### Exploração geral

- conhecer conteúdos, oportunidades, produtos, serviços, viagens, Organizações, Coletivos e atividades;
- pesquisar sem personalização;
- compreender preços, condições, origem e disponibilidade quando aplicáveis.

#### Caminho institucional e coletivo

- conhecer Guivos Business;
- conhecer experiências de Organizações e Coletivos;
- acessar informações para parceiros, patrocinadores, anunciantes e representantes autorizados;
- não misturar autoridade institucional com contexto pessoal.

### 6.5 O ecossistema será organizado por finalidade

A Home não apresentará as sete soluções como cartões equivalentes e desconectados.

A organização preferencial será:

#### Jornada e possibilidades para pessoas

- **Guivos Journey** — Momento Atual, objetivos, Próximos Passos, experiências e evolução;
- **Guivos Mall** — produtos e serviços com origem, preço e condições transparentes;
- **Guivos Travel** — viagens, destinos e experiências;
- **Guivos Media** — conteúdos, histórias e conhecimento acessível.

#### Organizações, programas e Coletivos

- **Guivos Business** — participação institucional, programas, oportunidades, públicos gerais autorizados e relações responsáveis.

#### Compreensão e transparência

- **Guivos Intelligence** — relações, fontes, contexto, incertezas e explicações, sem apresentar inteligência artificial como autoridade infalível.

#### Publicidade e patrocínio institucional

- **Guivos Ads** — anúncios, publicidade e patrocínios identificados, voltados a relações institucionais e comerciais transparentes.

Guivos Ads não deverá ser apresentado como recomendação pessoal ou como benefício obrigatório da jornada.

### 6.6 Possibilidades gerais serão opcionais e subordinadas

A Home poderá apresentar até três possibilidades gerais quando houver fundamento editorial, institucional, temporal ou regional verificável.

Cada item deverá mostrar, quando aplicável:

- natureza geral, editorial ou patrocinada;
- origem;
- Organização responsável;
- preço, gratuidade ou condição comercial;
- local, modalidade ou disponibilidade;
- prazo real;
- indicação explícita de que não houve personalização.

Nenhum item será incluído para preencher espaço.

### 6.7 Confiança deverá ser demonstrada por controle e transparência

A Home deverá comunicar de forma objetiva:

- a superfície pública não coleta relatos pessoais;
- iniciar a jornada é voluntário;
- a pessoa poderá revisar e corrigir a compreensão;
- inferências serão identificadas;
- publicidade será identificada;
- relações comerciais não determinarão relevância pessoal;
- acessibilidade, privacidade, segurança, termos e contato permanecerão acessíveis.

Provas sociais, números, rankings ou depoimentos somente poderão aparecer quando possuírem fonte, autorização, contexto e finalidade legítimos.

### 6.8 A navegação pública deverá ser curta e orientada por intenção

A navegação de referência poderá conter:

- `Como funciona`;
- `Explorar`;
- `Ecossistema`;
- `Organizações e Coletivos`;
- `Sobre a Guivos`;
- `Entrar`.

A navegação não deverá reproduzir todas as áreas internas da jornada pessoal.

### 6.9 A Home continuará pública após o início da jornada

A pessoa autenticada poderá acessar a Home pela marca ou por opção institucional.

A superfície não exibirá detalhes do Momento Atual, alertas pessoais, oportunidades personalizadas ou informações sensíveis. Esses elementos pertencem à Tela Hoje ou a outras superfícies autenticadas.

## 7. Hierarquia funcional reformulada

```text
identidade, propósito e descrição concreta da Guivos
→ ação principal adequada ao estado e exploração sem personalização
→ explicação simples de como a Guivos atua
→ caminhos pessoal, geral e institucional
→ ecossistema organizado por finalidade
→ possibilidades gerais opcionais e identificadas
→ confiança, privacidade, transparência e controle
→ acesso institucional, ajuda e rodapé
```

A hierarquia deverá continuar compreensível quando blocos opcionais forem removidos.

## 8. Conteúdo prioritário no primeiro campo visual

Sem depender de rolagem extensa, a Home deverá mostrar:

1. marca e identidade da Guivos;
2. o que é a Guivos em linguagem concreta;
3. qual valor funcional o ecossistema pretende oferecer;
4. a ação principal adequada ao estado;
5. a alternativa de explorar sem personalização;
6. que informações pessoais não são coletadas na superfície pública.

O primeiro campo visual não deverá mostrar:

- formulário;
- caixa de texto para relato;
- microfone;
- upload;
- perfil inferido;
- oportunidade descrita como `para você`;
- contagem de usuários, parceiros ou resultados sem contexto verificável;
- anúncio sem identificação.

## 9. Wireframe textual reformulado

```text
┌────────────────────────────────────────────────────┐
│ GUIVOS   Como funciona  Explorar  Ecossistema      │
│           Organizações e Coletivos          Entrar │
├────────────────────────────────────────────────────┤
│ Toda jornada começa no momento em que você está   │
│ agora.                                             │
│                                                    │
│ A Guivos ajuda pessoas a compreender seu momento, │
│ organizar objetivos e conhecer possibilidades,    │
│ mantendo cada decisão sob seu controle.            │
│                                                    │
│ [ Iniciar minha jornada ]                          │
│ [ Explorar sem personalização ]                    │
│ A Home pública não coleta seu relato pessoal.      │
├────────────────────────────────────────────────────┤
│ COMO A GUIVOS ATUA                                 │
│ Conheça → decida iniciar → conte em ambiente       │
│ protegido → revise → considere → escolha.          │
├────────────────────────────────────────────────────┤
│ ESCOLHA UM CAMINHO                                 │
│ [ Minha jornada ]                                  │
│ [ Explorar possibilidades gerais ]                 │
│ [ Organizações e Coletivos ]                       │
├────────────────────────────────────────────────────┤
│ ECOSSISTEMA ORGANIZADO POR FINALIDADE              │
│ Jornada: Journey | Mall | Travel | Media           │
│ Institucional: Business                            │
│ Compreensão: Intelligence                          │
│ Publicidade identificada: Ads                      │
├────────────────────────────────────────────────────┤
│ POSSIBILIDADES GERAIS, QUANDO EXISTIREM            │
│ Conteúdo ou oportunidade geral, com origem,        │
│ condição e indicação de ausência de personalização.│
├────────────────────────────────────────────────────┤
│ PRIVACIDADE, TRANSPARÊNCIA E CONTROLE              │
│ Sem coleta pública de relato. Inferências,         │
│ publicidade e relações comerciais identificadas.  │
├────────────────────────────────────────────────────┤
│ Sobre | Fundação | Segurança | Acessibilidade      │
│ Privacidade | Termos | Contato                     │
└────────────────────────────────────────────────────┘
```

O wireframe é estrutural. Não define cores, tipografia, imagens, componentes, responsividade final ou texto publicitário definitivo.

## 10. Linguagem aprovada

Preferir:

- `A Guivos é um ecossistema`;
- `Iniciar minha jornada`;
- `Explorar sem personalização`;
- `Como a Guivos atua`;
- `Você escolhe seus Próximos Passos`;
- `Possibilidades gerais`;
- `Conteúdo ainda não personalizado`;
- `Publicidade identificada`;
- `Conhecer Organizações e Coletivos`;
- `A Home pública não coleta seu relato pessoal`.

Evitar:

- `A Guivos sabe o que você precisa`;
- `Tudo para sua evolução` sem explicação;
- `Desbloqueie seu potencial`;
- `Complete seu perfil`;
- `As melhores oportunidades para você` antes da personalização;
- `Impacto` sem evidência;
- `Inteligência que decide por você`;
- `Grátis` quando existirem custos obrigatórios;
- `Shopping Guivos` como nome de produto;
- `Anúncios da Guivos` como nome de produto.

Os nomes oficiais permanecem **Guivos Mall** e **Guivos Ads**.

## 11. Estados de entrada validados

### 11.1 Visitante sem autenticação

Ação principal: `Iniciar minha jornada`.

Ação secundária: `Explorar sem personalização`.

Nenhuma informação pessoal será solicitada ou inferida na Home.

### 11.2 Pessoa autenticada sem jornada

Ação principal: `Iniciar minha jornada`.

A superfície poderá informar que a conta está ativa, sem apresentar perfil pessoal ou pressão para conclusão.

### 11.3 Relato protegido em andamento

Ação principal: `Continuar minha jornada`.

A Home não exibirá conteúdo do relato. O acesso encaminhará ao ambiente protegido.

### 11.4 Compreensão inicial aguardando revisão

Ação principal: `Revisar minha compreensão`.

Nenhuma oportunidade será apresentada como pessoalmente relevante antes da revisão suficiente.

### 11.5 Jornada ativa

Ação principal: `Ir para a Tela Hoje`.

Ação secundária: `Conhecer o ecossistema`.

### 11.6 Representante de Organização ou participante de Coletivo

A Home oferecerá acesso institucional claro, mas não mudará automaticamente o contexto de atuação nem executará ação em nome de uma Organização ou Coletivo.

### 11.7 Chegada por produto ou conteúdo específico

A Home poderá preservar a origem da navegação, por exemplo:

> Você está conhecendo o Guivos Mall, uma das soluções do ecossistema Guivos.

A mensagem não deverá afirmar interesse pessoal, relevância ou recomendação.

## 12. Estados alternativos obrigatórios

Permanecem para detalhamento posterior:

- baixa conectividade com versão essencial;
- texto ampliado e navegação assistiva;
- idioma ou região ainda não suportados integralmente;
- solução indisponível na região;
- ausência de possibilidades gerais;
- conteúdo geral temporariamente indisponível;
- publicidade patrocinada;
- pessoa que recusa todos os mecanismos de medição não essenciais;
- jornada suspensa ou encerrada;
- conta com acesso restrito;
- visitante menor de idade ou pessoa que exige proteção adicional;
- incidente de segurança ou indisponibilidade do início protegido.

A ausência de conteúdo opcional não deverá criar espaços vazios artificiais nem mensagens de culpa.

## 13. Testes funcionais da ação principal

A ação principal será válida somente quando:

- corresponde ao estado real da pessoa;
- explica o destino antes da transição;
- não inicia coleta pública;
- não utiliza urgência artificial;
- mantém alternativa de exploração geral;
- não depende de publicidade ou posição comercial;
- não expõe informação sensível;
- permite voltar sem perda artificial;
- utiliza linguagem compreensível sem identificadores técnicos.

## 14. Testes funcionais do ecossistema

A apresentação do ecossistema será válida somente quando:

- o propósito comum antecede os produtos;
- as soluções são agrupadas por finalidade;
- cada nome oficial é preservado;
- Guivos Mall é descrito como shopping do ecossistema, não como produto chamado Shopping Guivos;
- Guivos Ads é descrito como solução institucional de anúncios e patrocínios;
- Guivos Intelligence não é apresentada como autoridade infalível;
- publicidade e patrocínio são identificados;
- a pessoa pode explorar sem iniciar jornada;
- nenhuma solução é descrita como pessoalmente relevante sem contexto autorizado.

## 15. Resultado da validação

A Página Inicial pública da Guivos foi considerada **funcionalmente válida após reformulação**.

A validação confirma que a superfície pode avançar como hipótese estrutural porque:

- explica concretamente o que é a Guivos;
- preserva o propósito sem depender de linguagem abstrata;
- oferece ação principal e exploração geral sem coerção;
- mantém coleta pessoal fora da superfície pública;
- distingue caminhos pessoais, gerais e institucionais;
- organiza o ecossistema por finalidade;
- preserva Guivos Mall e Guivos Ads como nomes oficiais;
- subordina produtos e oportunidades ao propósito comum;
- identifica publicidade e ausência de personalização;
- adapta a ação principal ao estado real;
- preserva privacidade, acessibilidade e controle.

## 16. Limites

Esta validação não:

- valida funcionalmente o ambiente protegido de início da jornada;
- define textos finais de marketing;
- cria identidade visual;
- cria arquivo gráfico vetorial;
- cria protótipo navegável;
- executa testes com usuários;
- define tecnologia, componentes ou interfaces de programação;
- define formatos técnicos de voz ou arquivos;
- define modelo de inteligência artificial;
- autoriza inferências sensíveis;
- define preços, planos ou disponibilidade comercial;
- inicia Engenharia de Produto ou desenvolvimento;
- inicia a reaplicação dos testes dos Resultados Empresariais.

## 17. Próximo ponto de decisão

Após integração deste incremento e nova autorização, os próximos atos possíveis permanecem separados:

1. criar o arquivo gráfico vetorial de baixa fidelidade da Página Inicial pública;
2. validar funcionalmente a entrada protegida da jornada;
3. detalhar os estados de captura por texto, voz e arquivo;
4. validar a revisão da compreensão inicial;
5. validar a transição entre início protegido e Tela Hoje;
6. retomar, de forma independente, a reaplicação dos quatro testes dos Resultados Empresariais.

Nenhuma etapa posterior é iniciada automaticamente.
