---
id: PAS-001
title: Guivos Journey Product Architecture Specification
status: draft
version: 0.3.0
owner: Guivos
last_updated: 2026-07-04
related:
  - GPA-001
  - GLPA-001
  - GE2-SYNC-004
  - GE2-SYNC-005
---

# PAS-001 — Guivos Journey Product Architecture Specification

## 0. Product Philosophy

### 0.1 Filosofia do Produto

O Guivos Journey não foi concebido para maximizar tempo de uso, consumo de conteúdo ou interação superficial.

Sua finalidade é ajudar participantes a alcançar resultados concretos no mundo real, conectando-os às oportunidades mais relevantes para seus objetivos, contexto e momento de vida.

O sucesso do Journey não será medido pela quantidade de tempo que um participante permanece na plataforma, mas pela quantidade e qualidade do valor gerado fora dela.

### 0.2 Objetivo Fundamental

Toda funcionalidade do Journey deverá responder positivamente à seguinte pergunta:

> Esta funcionalidade aumenta a capacidade do participante de compreender seu contexto, decidir melhor ou avançar em sua jornada?

Se a resposta for negativa, ela não deve fazer parte do núcleo do produto.

### 0.3 Papel da Inteligência

A Inteligência do Ecossistema Guivos existe para:

- reduzir esforço;
- ampliar possibilidades;
- contextualizar informações;
- recomendar oportunidades;
- acelerar decisões;
- explicar caminhos possíveis;
- reconhecer mudanças relevantes;
- aprender com evidências autorizadas.

Ela não existe para:

- manipular comportamento;
- substituir decisões humanas;
- maximizar permanência na plataforma;
- induzir consumo desnecessário;
- criar dependência artificial;
- tratar inferências como fatos definitivos.

### 0.4 Papel do Participante

O participante permanece no controle da própria jornada.

A plataforma pode escutar, organizar, sugerir, explicar, recomendar, lembrar e acompanhar.

A decisão final permanece humana.

### 0.5 Papel do Ecossistema

O Journey não é proprietário das oportunidades.

Ele é a camada de experiência e orquestração que conecta Pessoas, Organizações, Coletivos, recursos, conteúdos, produtos e experiências de maneira inteligente.

### 0.6 Papel dos Demais Componentes

- Journey é a experiência;
- Mall fornece recursos comerciais;
- Business fornece oportunidades e relações institucionais;
- Media fornece conhecimento e inspiração;
- Travel fornece experiências presenciais e viagens;
- Ads conecta oferta e demanda patrocinada;
- Intelligence fornece inteligência transversal.

## 1. Visão do Produto

### 1.1 Definição

O Guivos Journey é a camada principal de experiência do Ecossistema Guivos.

Ele representa a interface por meio da qual participantes interagem com oportunidades, organizações, experiências, conteúdos, produtos e serviços disponíveis no ecossistema.

Mais do que um aplicativo ou feed, o Journey é um sistema de descoberta contextual de oportunidades e acompanhamento contínuo da evolução.

### 1.2 Propósito

O propósito do Guivos Journey é reduzir a distância entre o contexto atual de um participante e os caminhos disponíveis para avançar, utilizando inteligência contextual, conexões relevantes e oportunidades acionáveis.

### 1.3 Papel dentro do Ecossistema

O Journey é o núcleo da experiência do participante e atua como camada de orquestração.

Ele integra capacidades provenientes de Business, Mall, Media, Travel, Intelligence e Ads em uma experiência única e contínua.

### 1.4 O que o Journey não é

O Journey não é:

- uma rede social tradicional;
- um marketplace convencional;
- um buscador genérico;
- um agregador de eventos;
- uma plataforma exclusiva de cursos;
- um aplicativo de produtividade;
- um sistema de tarefas;
- um assistente que decide pelo participante;
- o executor direto de todos os serviços especializados do ecossistema.

### 1.5 Proposta de Valor

> Ajudar cada participante a descobrir, no momento certo, as melhores oportunidades para avançar em direção aos seus objetivos, reunindo em uma única experiência aquilo que normalmente estaria disperso em muitas plataformas.

Essa proposta combina:

- descoberta;
- contexto;
- continuidade;
- acionabilidade;
- confiança.

### 1.6 Princípios de Produto

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

O Journey deve ser compreendido como a Experience Layer da GLPA.

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
- superfície principal de interação;
- descoberta contextual de oportunidades;
- organização da jornada;
- apresentação de recomendações;
- objetivos e Momentos Atuais;
- acompanhamento de evolução;
- comunicação com o participante;
- gamificação e incentivos visíveis;
- integração experiencial com os demais componentes;
- orquestração de intervenções contextuais.

### 2.2 Responsabilidades que não pertencem ao Journey

- processar compras e pagamentos do Mall;
- gerenciar contratos B2B do Business;
- produzir inteligência algorítmica fora da Intelligence Layer;
- operar campanhas de mídia paga do Ads;
- produzir conteúdo editorial do Media;
- executar reservas do Travel;
- manter infraestrutura técnica comum da Platform Layer.

## 3. Captura Multimodal de Contexto

### 3.1 Decisão funcional

A compreensão do Momento Atual não deve depender de um fluxo longo de formulários como mecanismo principal.

O participante deve poder descrever sua realidade, objetivos, limitações e expectativas com suas próprias palavras.

### 3.2 Voz como canal prioritário

A voz deve ser tratada como canal prioritário por permitir expressão mais natural, contextual e detalhada.

A experiência também deve oferecer texto e preenchimento estruturado quando necessário.

### 3.3 Canais multimodais candidatos

- voz;
- conversa por texto;
- documentos autorizados;
- imagens autorizadas;
- localização autorizada;
- calendário autorizado;
- wearables e aplicativos autorizados;
- integrações profissionais autorizadas;
- histórico de interações e experiências da Guivos.

### 3.4 Sequência comportamental

```text
Escutar
  -> Compreender
  -> Refletir a compreensão
  -> Confirmar
  -> Recomendar ou agir
```

A primeira experiência não deve buscar conhecer tudo. Deve gerar confiança suficiente para que o participante perceba que foi compreendido.

### 3.5 Regras

1. O participante não deve revelar mais do que o necessário.
2. Inferências relevantes devem ser explicáveis e revisáveis.
3. Informações sensíveis exigem consentimento e governança superiores.
4. Fatos declarados, dados integrados, evidências e inferências devem ser diferenciados.
5. O participante deve poder corrigir, complementar, ocultar ou limitar o uso das informações.
6. A compreensão inicial deve ser confirmada antes de orientar decisões relevantes.

## 4. Modelo Vivo do Participante — Conceito Candidato

O `Living Participant Model (LPM)` representa provisoriamente a estrutura dinâmica utilizada para consolidar contexto autorizado, temporal, explicável e atualizável.

Ele pode incluir identidade, Momento Atual, objetivos, Próximos Passos, interesses, competências, preferências, limitações, disponibilidade, relacionamentos, experiências, evidências, proveniência, confiança e permissões.

O conceito permanece em Discovery/Engineering e não deve ser tratado como componente técnico obrigatório nesta fase.

## 5. Context Intelligence Engine — Capacidade Candidata

O `Context Intelligence Engine (CIE)` é uma capacidade candidata da Intelligence Layer para interpretar entradas multimodais, propor atualizações do contexto e preservar proveniência, confiança, temporalidade e explicabilidade.

O CIE não deve alterar silenciosamente informações sensíveis ou permanentes.

## 6. Filosofia Operacional do Journey

O Journey deverá operar por cinco responsabilidades permanentes:

1. **Compreender** — construir e atualizar o contexto do participante;
2. **Acompanhar** — reconhecer evolução, mudanças e continuidade ao longo do tempo;
3. **Ativar** — tornar visíveis oportunidades quando elas se tornam relevantes;
4. **Orquestrar** — organizar próximos passos, intervenções e experiências;
5. **Aprender** — incorporar resultados e evidências autorizadas.

## 7. Relação Contínua e Vida Real

O Journey não deve ser especificado apenas como um aplicativo utilizado em sessões isoladas.

Ele representa uma relação contínua entre o participante e a Guivos.

```text
Vida real
  -> mudança relevante
  -> atualização do contexto
  -> nova avaliação
  -> intervenção ou silêncio
  -> experiência
  -> nova evidência
  -> novo contexto
```

O aplicativo é um ponto de contato dessa relação, não o centro da jornada.

## 8. Estado e Eventos de Vida

### 8.1 Estado

Estado representa a realidade atual do participante.

Exemplos:

- profissão atual;
- cidade;
- disponibilidade;
- objetivos;
- hábitos;
- relacionamentos;
- competências.

### 8.2 Evento de Vida

Evento de Vida representa uma mudança relevante capaz de alterar o estado do participante.

Exemplos:

- novo emprego;
- demissão;
- mudança de cidade;
- conclusão de curso;
- nascimento de filho;
- início de atividade esportiva;
- entrada em coletivo;
- nova responsabilidade profissional ou comunitária.

### 8.3 Regras

- eventos podem ser declarados, observados ou recebidos por integração autorizada;
- eventos inferidos devem ser confirmados quando houver impacto relevante;
- nem todo evento exige intervenção;
- o histórico deve preservar temporalidade e origem.

## 9. Oportunidades Ativas

### 9.1 Oportunidade

Oportunidade é uma iniciativa, recurso ou possibilidade existente no ecossistema.

### 9.2 Oportunidade Ativa

Oportunidade Ativa é uma oportunidade que, considerando o contexto atual de um participante, possui potencial imediato de apoiar progresso e merece ser apresentada.

### 9.3 Regra central

O Journey não deve maximizar a quantidade de oportunidades mostradas.

Deve priorizar relevância, momento, acionabilidade, confiança e potencial de evolução.

## 10. Intervenções Contextuais

### 10.1 Definição

Intervenção Contextual é a decisão de agir em determinado momento para gerar valor à jornada.

Notificação é apenas um dos possíveis canais.

### 10.2 Orquestração de Intervenções

A responsabilidade funcional deve decidir:

- quando agir;
- quando perguntar;
- quando esperar;
- quando apenas observar;
- quando permanecer em silêncio.

### 10.3 Princípio da Intervenção Relevante

> A Guivos somente deve interromper o participante quando houver evidências suficientes de que a intervenção possui potencial real de gerar valor.

## 11. Distância para Evolução — Conceito Interno

`Distância para Evolução` representa, internamente, a diferença entre o contexto atual do participante e os caminhos disponíveis para avançar.

Não é uma medida única nem necessariamente numérica nesta fase.

Serve como princípio de produto para evitar excesso de opções e orientar descoberta, priorização e acionabilidade.

### Formulação operacional

> O objetivo do Guivos Journey não é maximizar a quantidade de oportunidades apresentadas, mas reduzir continuamente a distância entre o contexto atual do participante e seu potencial de evolução, ativando apenas oportunidades com maior probabilidade de gerar progresso naquele momento.

A linguagem pública continua utilizando formulações mais simples, como “encontrar as oportunidades certas no momento certo”.

## 12. Fluxo Funcional Central

```text
Captura de contexto
  -> compreensão refletida
  -> confirmação do participante
  -> objetivos e prioridades
  -> eventos e mudanças
  -> avaliação de oportunidades
  -> oportunidades ativas
  -> intervenção contextual
  -> experiência
  -> evidências
  -> atualização do contexto
  -> novo ciclo
```

## 13. Hierarquia Documental de Produto

```text
GPA
  -> PAS
       -> JFA
            -> FDS
       -> UX Specification
       -> Technical Specification
```

- PAS define o produto/camada;
- JFA define domínios funcionais permanentes;
- FDS detalha cada domínio;
- UX define a interação;
- Technical Specification define a implementação.

## 14. Sequência de Especificação Funcional

A próxima evolução seguirá:

1. Captura de Contexto;
2. Construção do Modelo de Contexto;
3. Objetivos;
4. Eventos de Vida;
5. Próximos Passos;
6. Oportunidades Ativas;
7. Intervenções Contextuais;
8. Experiências;
9. Evolução;
10. IA;
11. Integrações;
12. Modelo Econômico;
13. KPIs;
14. Roadmap.

## 15. Ponto de Retomada

A próxima atividade é detalhar funcionalmente a **Captura de Contexto**, começando pela primeira conversa do participante com a Guivos.

Essa especificação deverá responder:

- como o participante inicia por voz ou texto;
- como a Guivos escuta sem conduzir excessivamente;
- como interpreta e reflete o entendimento;
- como o participante confirma, corrige ou limita;
- como consentimento e privacidade são apresentados;
- como o primeiro contexto gera objetivos, prioridades e primeiras oportunidades;
- quais erros, exceções e saídas devem ser tratados.