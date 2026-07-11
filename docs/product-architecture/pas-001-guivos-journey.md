---
id: PAS-001
title: Guivos Journey Product Architecture Specification
status: draft
version: 0.4.0
owner: Guivos
last_updated: 2026-07-04
related:
  - GPA-001
  - GLPA-001
  - GE2-SYNC-004
  - GE2-SYNC-005
  - GE2-SYNC-006
---

# PAS-001 — Guivos Journey Product Architecture Specification

## 0. Product Philosophy

### 0.1 Filosofia do Produto

O Guivos Journey não foi concebido para maximizar tempo de uso, consumo de conteúdo ou interação superficial.

Sua finalidade é ajudar participantes a alcançar resultados concretos no mundo real, conectando-os às oportunidades mais relevantes para seus objetivos, contexto e momento de vida.

O sucesso do Journey será medido pela quantidade e qualidade do valor gerado fora da plataforma.

### 0.2 Objetivo Fundamental

Toda capacidade do Journey deverá responder positivamente:

> Esta capacidade aumenta a condição do participante de compreender seu contexto, decidir melhor ou avançar em sua jornada?

Se a resposta for negativa, ela não deve fazer parte do núcleo do produto.

### 0.3 Papel da Inteligência

A Inteligência do Ecossistema Guivos existe para reduzir esforço, ampliar possibilidades, contextualizar informações, reconhecer mudanças, recomendar oportunidades, explicar caminhos e aprender com evidências autorizadas.

Ela não existe para manipular comportamento, substituir decisões humanas, maximizar permanência, induzir consumo desnecessário ou tratar inferências como fatos definitivos.

### 0.4 Papel do Participante

O participante permanece no controle da própria jornada.

A plataforma pode escutar, organizar, sugerir, explicar, recomendar, lembrar e acompanhar. A decisão final permanece humana.

### 0.5 Papel do Ecossistema

O Journey é a camada de experiência e orquestração que conecta Pessoas, Organizações, Coletivos, oportunidades, conteúdos, produtos, serviços e experiências.

- Journey é a experiência;
- Intelligence fornece inteligência transversal;
- Business fornece oportunidades e relações institucionais;
- Mall fornece recursos comerciais;
- Media fornece conhecimento e inspiração;
- Travel fornece viagens e experiências presenciais;
- Ads conecta oferta e demanda patrocinada.

## 1. Visão do Produto

### 1.1 Definição

O Guivos Journey é a Experience Layer do Ecossistema Guivos.

Mais do que um aplicativo ou feed, é um sistema de descoberta contextual de oportunidades e acompanhamento contínuo da evolução.

### 1.2 Propósito

Reduzir a distância entre o contexto atual de um participante e os caminhos disponíveis para avançar, utilizando inteligência contextual, conexões relevantes e oportunidades acionáveis.

### 1.3 Proposta de Valor

> Ajudar cada participante a descobrir, no momento certo, as melhores oportunidades para avançar em direção aos seus objetivos, reunindo em uma única experiência aquilo que normalmente estaria disperso em muitas plataformas.

A proposta combina descoberta, contexto, continuidade, acionabilidade e confiança.

### 1.4 O que o Journey não é

O Journey não é uma rede social tradicional, marketplace convencional, buscador genérico, agregador de eventos, plataforma exclusiva de cursos, aplicativo de produtividade, sistema de tarefas ou assistente que decide pelo participante.

### 1.5 Princípios de Produto

1. O participante é protagonista da própria jornada.
2. Toda interação deve gerar valor perceptível.
3. A inteligência deve reduzir esforço, não aumentar complexidade.
4. Recomendações devem ser contextualizadas e explicáveis.
5. O sucesso é medido por impacto no mundo real, não por tempo de tela.
6. A experiência deve evoluir continuamente com o participante.
7. O Journey deve incentivar ação no mundo real.
8. O participante controla sua jornada.
9. A compreensão deve ser progressiva, natural e revisável.
10. Voz e demais canais multimodais devem reduzir dependência de formulários extensos.
11. O Journey deve saber quando agir e quando permanecer em silêncio.
12. Receita, popularidade ou patrocínio não devem superar relevância contextual.

## 2. Arquitetura em Camadas Aplicada ao Journey

```text
Participante
  -> Guivos Journey
       -> Guivos Intelligence
       -> Guivos Business
       -> Guivos Mall
       -> Guivos Media
       -> Guivos Travel
       -> Guivos Ads
       -> Platform Layer
```

### 2.1 Responsabilidades do Journey

- experiência unificada;
- descoberta contextual;
- organização da jornada;
- apresentação de recomendações;
- objetivos e Momentos Atuais;
- acompanhamento da evolução;
- comunicação com o participante;
- gamificação e incentivos visíveis;
- integração experiencial;
- orquestração de intervenções contextuais.

### 2.2 Responsabilidades externas ao Journey

O Journey não processa pagamentos do Mall, contratos B2B do Business, inteligência algorítmica da Intelligence Layer, campanhas do Ads, produção editorial do Media, reservas do Travel ou infraestrutura comum da Platform Layer.

## 3. Filosofia Operacional do Journey

O Journey opera por cinco responsabilidades permanentes:

1. **Compreender** — construir e atualizar contexto;
2. **Acompanhar** — reconhecer continuidade e mudanças;
3. **Ativar** — tornar oportunidades relevantes visíveis;
4. **Orquestrar** — organizar próximos passos, intervenções e experiências;
5. **Aprender** — incorporar resultados e evidências autorizadas.

Sequência comportamental:

```text
Escutar
  -> Compreender
  -> Refletir a compreensão
  -> Confirmar
  -> Recomendar ou agir
```

## 4. Relação Contínua e Vida Real

O Journey não deve ser especificado apenas como aplicativo utilizado em sessões isoladas.

```text
Vida real
  -> mudança relevante
  -> atualização da compreensão
  -> nova avaliação
  -> intervenção ou silêncio
  -> experiência
  -> nova evidência
  -> novo contexto
```

O aplicativo é um ponto de contato dessa relação, não o centro da jornada.

## 5. Estado, Eventos de Vida e Oportunidades Ativas

### 5.1 Estado

Estado representa a realidade atual compreendida do participante.

### 5.2 Evento de Vida

Evento de Vida representa uma mudança relevante capaz de alterar esse estado.

Eventos podem ser declarados, observados ou recebidos por integração autorizada. Eventos inferidos devem ser confirmados quando houver impacto relevante.

### 5.3 Oportunidade Ativa

Oportunidade Ativa é uma oportunidade que, considerando o contexto atual de um participante, possui potencial imediato de apoiar progresso e merece ser apresentada.

O Journey deve priorizar relevância, momento, acionabilidade, confiança e potencial de evolução, não quantidade.

### 5.4 Intervenção Contextual

Intervenção Contextual é a decisão de agir em determinado momento. Notificação é apenas um canal.

A orquestração deve decidir quando agir, perguntar, esperar, observar ou permanecer em silêncio.

### 5.5 Distância para Evolução

`Distância para Evolução` é um conceito interno de produto que representa a diferença entre o contexto atual do participante e os caminhos disponíveis para avançar.

> O objetivo do Journey não é maximizar oportunidades apresentadas, mas reduzir continuamente essa distância, ativando apenas oportunidades com maior probabilidade de gerar progresso naquele momento.

## 6. Padrão de Especificação por Capacidades

Cada capacidade deverá possuir:

1. pergunta central;
2. objetivo;
3. valor entregue;
4. responsabilidades e limites;
5. entradas;
6. ciclo cognitivo;
7. fluxo do participante;
8. fluxo do sistema;
9. estados;
10. regras de negócio;
11. exceções;
12. privacidade e consentimento;
13. integrações;
14. eventos produzidos;
15. KPIs;
16. cenários ideal, alternativo e limite;
17. contrato da capacidade.

### 6.1 Princípio da Singularidade Funcional

> Cada capacidade funcional existe para resolver um único problema central.

### 6.2 Ciclo Cognitivo do Domínio

```text
Informação
  -> Interpretação
  -> Compreensão
  -> Contexto
  -> Decisão
  -> Ação
  -> Resultado
  -> Aprendizado
  -> Nova informação
```

## 7. Mapa de Capacidades do Journey

| Capacidade | Pergunta central | Estado |
|---|---|---|
| 01 — Captura de Contexto | Como a Guivos começa a compreender um participante? | Substantially complete |
| 02 — Contexto Vivo | Como a Guivos mantém uma representação viva e confiável do participante? | In progress |
| 03 — Objetivos | Como a Guivos compreende para onde o participante deseja evoluir? | Planned |
| 04 — Eventos de Vida | Como mudanças relevantes alteram a jornada? | Planned / concept consolidated |
| 05 — Próximos Passos | Como grandes objetivos se tornam ações possíveis? | Planned |
| 06 — Oportunidades Ativas | Como decidir quais oportunidades devem aparecer? | Planned / concept consolidated |
| 07 — Intervenções Contextuais | Quando agir e quando permanecer em silêncio? | Planned / concept consolidated |
| 08 — Experiências | Como oportunidades se transformam em evolução real? | Planned |
| 09 — Evolução Contínua | Como a jornada permanece útil durante anos? | Planned |

# Capacidade 01 — Captura de Contexto

## 8. Pergunta central

> Como a Guivos começa a compreender um participante?

## 9. Objetivo e valor entregue

Permitir que o participante expresse sua realidade de forma natural para que a Guivos construa uma compreensão inicial, revisável e útil, sem depender de cadastro longo.

## 10. Formas de início

### 10.1 Voz

Canal prioritário para expressão livre e detalhada.

### 10.2 Texto

Alternativa equivalente para preferência, acessibilidade ou ambiente inadequado para áudio.

### 10.3 Fluxo guiado

Alternativa opcional para quem não sabe por onde começar. Não deve ser o fluxo obrigatório.

## 11. Primeira mensagem

A mensagem inicial deve explicar finalidade, ausência de julgamento, liberdade para não responder e possibilidade de revisão.

Formulação de referência:

> Para apresentar oportunidades realmente úteis, preciso compreender um pouco do seu momento atual. Você pode falar ou escrever livremente. Não é necessário contar nada que não queira, e você poderá revisar tudo o que eu compreender.

## 12. Comportamento durante a escuta

A Guivos deve:

- permitir expressão livre;
- não interromper desnecessariamente;
- preservar o conteúdo original;
- permitir pausar, continuar, apagar ou recomeçar;
- sinalizar captura de áudio;
- permitir ouvir, editar transcrição e excluir áudio quando aplicável;
- não transformar inferência em fato;
- não recomendar antes da confirmação.

## 13. Interpretação inicial e reflexão

A Guivos deverá organizar a compreensão em:

- Momento Atual;
- objetivos mencionados;
- limitações e condições;
- preferências;
- possível prioridade;
- pontos incertos;
- fatos declarados;
- inferências provisórias.

Ela deverá devolver uma síntese compreensível e perguntar se a leitura está correta.

Respostas mínimas:

- está correto;
- parcialmente correto;
- quero corrigir;
- quero acrescentar;
- prefiro não registrar parte disso.

## 14. Controle do participante

Antes da confirmação, o participante poderá:

- editar;
- remover;
- alterar prioridade;
- marcar interpretação como incorreta;
- confirmar inferência;
- limitar uso;
- manter informação temporária;
- impedir recomendações sobre determinado tema.

## 15. Perguntas complementares

Perguntas adicionais somente são permitidas para evitar erro, diferenciar objetivos, identificar restrições, tornar recomendação útil, proteger o participante ou atender obrigação legal.

Devem ser poucas e contextualizadas.

## 16. Priorização inicial

Quando houver vários objetivos, o participante poderá escolher um ou mais, pedir ajuda para comparar ou manter sem prioridade definida.

Sugestões de prioridade devem ser explicadas.

## 17. Profundidade progressiva

- nível inicial: contexto mínimo;
- nível intermediário: preferências, disponibilidade, limitações e histórico;
- nível aprofundado: documentos, integrações, evidências, competências e relações autorizadas.

Níveis superiores não são obrigatórios para utilizar o Journey.

## 18. Temas sensíveis

Informações sobre saúde, religião, renda, política, família, deficiência, localização precisa e outros dados sensíveis exigem finalidade clara, consentimento proporcional, possibilidade de recusa e proteção superior.

A Guivos não deve utilizar vulnerabilidades para publicidade, manipulação, diagnóstico ou conclusão profissional indevida.

## 19. Resultado da captura

A capacidade produz:

1. síntese confirmada do Momento Atual;
2. objetivos ou intenções;
3. prioridade inicial, quando definida;
4. limitações e preferências relevantes;
5. autorização de uso para etapas seguintes.

Após a confirmação, a Guivos deverá entregar valor imediato por meio de síntese, possível Próximo Passo, até três oportunidades iniciais ou uma ação simples.

## 20. Exceções

- participante não sabe o que deseja: explorar sem pressionar;
- informação insuficiente: pergunta complementar curta;
- muitos problemas simultâneos: organizar e ajudar a priorizar;
- mudança de ideia: atualizar antes da confirmação;
- recusa em salvar: oferecer sessão temporária com limites claros;
- risco grave ou urgência: aplicar protocolo específico e orientar ajuda adequada.

## 21. Critérios de sucesso

A capacidade é bem-sucedida quando o participante:

- conclui sem fricção excessiva;
- reconhece a síntese como suficientemente correta;
- entende finalidade e uso;
- mantém controle;
- recebe valor inicial coerente;
- não precisa repetir imediatamente o que já explicou.

## 22. Contrato da Capacidade 01

A Capacidade 01 garante que:

- o participante inicia sem cadastro complexo;
- voz, texto e fluxo guiado são opções válidas;
- a Guivos escuta, interpreta, reflete e confirma;
- o participante corrige e governa sua informação;
- o primeiro valor é entregue após confirmação;
- o contexto inicial fica pronto para alimentar a Capacidade 02.

> A primeira conversa termina quando o participante confirma que foi compreendido e recebe um primeiro caminho útil, não quando completa um cadastro.

# Interpretação do Contexto

## 23. Objetivo

Transformar entradas autorizadas em compreensão coerente, explicável e útil, sem decidir pelo participante ou alterar silenciosamente sua representação permanente.

## 24. Tipos interpretados

- fatos;
- intenções;
- objetivos;
- limitações;
- preferências;
- emoções percebidas, sem diagnóstico;
- incertezas;
- hipóteses e inferências.

## 25. Confiança, proveniência e temporalidade

Toda interpretação relevante deve responder:

- de onde veio;
- quando surgiu;
- quem informou;
- se foi inferida;
- se foi confirmada;
- se continua válida.

Níveis funcionais iniciais de confiança:

- muito alta: declaração explícita e atual;
- alta: confirmação recorrente ou evidência convergente;
- média: inferência consistente;
- baixa: hipótese inicial.

Hipóteses de baixa confiança não devem alterar informação permanente sem confirmação.

## 26. Conflitos e reconstrução

Informações conflitantes não devem ser resolvidas silenciosamente.

A Guivos deverá preservar histórico, reconhecer mudança, pedir confirmação quando necessário e reconstruir continuamente sua compreensão.

Uma nova evidência pode confirmar, fortalecer, enfraquecer, complementar, substituir ou invalidar uma interpretação.

## 27. Explicabilidade

O participante poderá perguntar por que a Guivos entende determinado aspecto de sua jornada.

A resposta deverá citar fontes, interações ou evidências relevantes, nunca apenas afirmar que “a IA decidiu”.

# Capacidade 02 — Contexto Vivo

## 28. Pergunta central

> Como a Guivos mantém uma representação viva, confiável, explicável e continuamente evolutiva do participante?

## 29. Definição funcional

O Contexto Vivo não representa a realidade absoluta do participante.

Ele representa a melhor compreensão que a Guivos possui sobre essa realidade em determinado momento, construída a partir de informações, evidências, interpretações e confirmações autorizadas.

Toda representação relevante deve ser:

- contextual;
- temporal;
- explicável;
- revisável;
- controlável pelo participante.

### 29.1 Princípio da Representação Humilde

> A Guivos nunca presume conhecer completamente o participante. Ela mantém continuamente a melhor representação possível de sua realidade, sempre aberta à revisão, ao aprendizado e à confirmação.

## 30. Dimensões de compreensão

O Contexto Vivo é um modelo multidimensional de compreensão, não um supercadastro.

### 30.1 Identidade

Papéis e formas pelas quais o participante se reconhece no momento: profissional, estudante, empreendedor, responsável familiar, voluntário, atleta, mentor ou integrante de coletivos.

### 30.2 Momento

Condições que caracterizam a realidade atual: início de carreira, transição, crescimento, reorganização, mudança, recuperação ou expansão.

### 30.3 Direção

Objetivos, sonhos, prioridades, intenções e possibilidades desejadas.

### 30.4 Capacidades

Conhecimentos, competências, experiências, certificações, recursos e redes disponíveis.

### 30.5 Restrições

Tempo, dinheiro, saúde, disponibilidade, mobilidade, responsabilidades e demais limites atuais.

### 30.6 Preferências

Formas preferidas de viver experiências: online, presencial, individual, coletiva, gratuita, paga, curta ou longa.

### 30.7 Relacionamentos

Pessoas, Organizações e Coletivos relevantes para a jornada.

### 30.8 Evolução

Mudanças, resultados, evidências e diferenças entre estados ao longo do tempo.

## 31. Evolução independente das dimensões

> Cada dimensão do Contexto Vivo evolui de forma independente. Uma alteração poderá impactar outras dimensões, mas não deverá exigir reconstrução completa nem presumir mudanças onde não existam evidências suficientes.

Exemplos:

- uma promoção pode alterar Momento, Capacidades e Direção, sem modificar Preferências;
- o nascimento de um filho pode alterar Momento, Restrições, Disponibilidade e Direção, sem alterar competências profissionais.

## 32. Ciclo de vida da informação

```text
Observada
  -> Interpretada
  -> Confirmada
  -> Ativa
  -> Envelhecida
  -> Substituída
  -> Arquivada
```

Cada item deverá preservar origem, temporalidade, confiança, finalidade, permissões e relação com dimensões afetadas.

## 33. Visão do participante — Meu Contexto Hoje

O participante deverá acessar uma visão simples contendo:

- quem sou neste momento;
- foco principal;
- mudanças recentes;
- objetivos ativos;
- próximos passos;
- capacidades relevantes;
- restrições atuais;
- preferências;
- conexões importantes;
- temas acompanhados;
- informações que podem precisar de atualização;
- última revisão.

Ele deverá conseguir entender:

- o que a Guivos entende;
- por que entende;
- quando atualizou;
- quais fontes foram utilizadas;
- como corrigir, ocultar, limitar ou remover.

## 34. Estado atual da Capacidade 02

Já consolidados:

- definição funcional;
- princípio da Representação Humilde;
- modelo multidimensional;
- oito dimensões iniciais;
- evolução independente;
- ciclo de vida inicial;
- visão conceitual `Meu Contexto Hoje`.

Ainda pendentes:

- responsabilidades e limites completos;
- entradas e saídas;
- regras de envelhecimento;
- resolução detalhada de conflitos;
- eventos produzidos;
- integrações;
- KPIs;
- casos ideal, alternativo e limite;
- contrato da capacidade.

## 35. Ponto de retomada

Retomar na Capacidade 02 — Contexto Vivo, detalhando responsabilidades, entradas, saídas, estados de cada dimensão, regras de atualização e envelhecimento, conflitos, interface, eventos, KPIs, cenários e contrato de aceite.