---
id: PAS-001
title: Guivos Journey Product Architecture Specification
status: draft
version: 0.2.0
owner: Guivos
last_updated: 2026-07-04
related:
  - GPA-001
  - GLPA-001
  - GE2-SYNC-004
---

# PAS-001 — Guivos Journey Product Architecture Specification

## 0. Product Philosophy

### 0.1 Filosofia do Produto

O Guivos Journey não foi concebido para maximizar tempo de uso, consumo de conteúdo ou interação superficial.

Sua finalidade é ajudar pessoas a alcançar resultados concretos no mundo real, conectando-as às oportunidades mais relevantes para seus objetivos, contexto e momento de vida.

O sucesso do Journey não será medido pela quantidade de tempo que um usuário permanece na plataforma, mas pela quantidade de valor gerado fora dela.

### 0.2 Objetivo Fundamental

Toda funcionalidade do Journey deverá responder positivamente à seguinte pergunta:

> Esta funcionalidade aumenta a capacidade do usuário de alcançar seus objetivos?

Se a resposta for negativa, ela não deve fazer parte do produto.

### 0.3 Papel da Inteligência Artificial

A Inteligência Artificial da Guivos existe para:

- reduzir esforço;
- ampliar possibilidades;
- contextualizar informações;
- recomendar oportunidades;
- acelerar decisões;
- explicar caminhos possíveis.

Ela não existe para:

- manipular comportamento;
- substituir decisões humanas;
- maximizar permanência na plataforma;
- induzir consumo desnecessário;
- criar dependência artificial.

### 0.4 Papel do Usuário

O usuário permanece no controle da própria jornada.

A plataforma pode sugerir, explicar, organizar, recomendar e lembrar.

A decisão final permanece humana.

### 0.5 Papel do Ecossistema

O Journey não é proprietário das oportunidades.

Ele é a camada de experiência e orquestração que conecta pessoas, organizações, recursos, conteúdos, produtos e experiências de maneira inteligente.

### 0.6 Papel dos Demais Produtos

Os demais componentes do ecossistema existem para fortalecer a experiência do Journey, sem competir com ele.

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

Ele representa a interface através da qual pessoas interagem com oportunidades, organizações, experiências, conteúdos, produtos e serviços disponíveis no ecossistema.

Mais do que um aplicativo ou feed de conteúdo, o Journey é um assistente inteligente de evolução, projetado para compreender o contexto de cada pessoa e conectá-la continuamente às oportunidades mais relevantes para seus objetivos, momento de vida e interesses.

O Journey não substitui a capacidade de decisão do usuário. Seu papel é reduzir o esforço necessário para descobrir, avaliar e acessar oportunidades de desenvolvimento pessoal, profissional, social, espiritual e comunitário.

### 1.2 Propósito

O propósito do Guivos Journey é reduzir a distância entre a situação atual de uma pessoa e os objetivos que ela deseja alcançar, utilizando inteligência contextual, conexões relevantes e oportunidades personalizadas.

O Journey existe para transformar um processo normalmente fragmentado, demorado e baseado em tentativa e erro em uma experiência contínua, personalizada e orientada por contexto.

### 1.3 Papel dentro do Ecossistema Guivos

O Journey é o núcleo da experiência do usuário.

Enquanto os demais componentes possuem funções especializadas, o Journey atua como a camada de orquestração da experiência.

Sua responsabilidade é integrar naturalmente todos os componentes do ecossistema, permitindo que o usuário tenha uma experiência única e contínua, independentemente da origem da oportunidade ou do serviço utilizado.

Em termos funcionais:

- Guivos Business fornece organizações e oportunidades institucionais;
- Guivos Mall fornece produtos, serviços, assinaturas e ativos comerciais;
- Guivos Media fornece conteúdo, inspiração e formação;
- Guivos Travel fornece experiências presenciais, viagens e reservas;
- Guivos Intelligence fornece inteligência, personalização e interpretação contextual;
- Guivos Ads conecta patrocinadores, anunciantes e oportunidades patrocinadas.

O Journey organiza tudo isso em uma única experiência para o usuário.

### 1.4 O que o Journey não é

O Journey não é:

- uma rede social tradicional baseada em engajamento superficial;
- um marketplace convencional;
- um buscador genérico;
- um agregador de eventos;
- uma plataforma exclusiva de cursos;
- um aplicativo de produtividade;
- um sistema de gerenciamento de tarefas;
- um assistente que toma decisões pelo usuário;
- o executor direto de todos os serviços especializados do ecossistema.

Essas funcionalidades podem existir parcialmente no ecossistema, mas nenhuma delas define o propósito do Journey.

### 1.5 Proposta de Valor

O Journey entrega a seguinte proposta de valor:

> Ajudar cada pessoa a descobrir, no momento certo, as melhores oportunidades para evoluir em direção aos seus objetivos, reunindo em uma única experiência tudo o que normalmente estaria disperso em dezenas de plataformas.

Essa proposta combina três elementos:

- descoberta: encontrar oportunidades relevantes sem depender exclusivamente de buscas manuais;
- contexto: considerar objetivos, interesses, localização, histórico e momento de vida;
- continuidade: acompanhar a evolução do usuário ao longo do tempo, ajustando recomendações conforme sua jornada.

### 1.6 Princípios de Produto

Toda evolução do Journey deverá respeitar os seguintes princípios:

1. O usuário é o protagonista da própria jornada.
2. Toda interação deve gerar valor perceptível.
3. A inteligência deve reduzir esforço, não aumentar complexidade.
4. Recomendações devem ser contextualizadas e explicáveis.
5. O sucesso da plataforma é medido pelo impacto na vida das pessoas, não pelo tempo de tela.
6. A experiência deve evoluir continuamente com o usuário.
7. O Journey deve incentivar ação no mundo real, não apenas permanência na tela.
8. O usuário controla sua jornada; a Guivos amplia suas possibilidades.
9. A compreensão do participante deve ser progressiva, natural e revisável.
10. Voz e demais canais multimodais devem reduzir a dependência de formulários extensos.

## 2. Arquitetura em Camadas Aplicada ao Journey

O Journey deve ser compreendido como a Experience Layer da GLPA.

```text
Usuário
  -> Guivos Journey
       -> Guivos Intelligence
       -> Guivos Business
       -> Guivos Mall
       -> Guivos Media
       -> Guivos Travel
       -> Guivos Ads
       -> Platform Layer
```

### 2.1 Responsabilidade do Journey

O Journey é responsável por:

- experiência unificada;
- superfície principal de interação;
- descoberta de oportunidades;
- organização da jornada;
- apresentação de recomendações;
- objetivos e Momentos Atuais;
- acompanhamento de evolução;
- comunicação com o usuário;
- gamificação e incentivos visíveis;
- integração experiencial com os demais componentes.

### 2.2 Responsabilidades que não pertencem ao Journey

O Journey não é responsável por:

- processar compras e pagamentos do Mall;
- gerenciar contratos B2B do Business;
- produzir inteligência algorítmica própria fora da Intelligence Layer;
- operar campanhas de mídia paga do Ads;
- produzir conteúdo editorial do Media;
- executar reservas e operações de viagem do Travel;
- manter infraestrutura técnica comum da Platform Layer.

## 3. Captura Multimodal de Contexto

### 3.1 Decisão funcional

A compreensão do Momento Atual não deve depender de um fluxo longo de formulários como mecanismo principal.

O participante deve poder descrever sua realidade, objetivos, limitações e expectativas com suas próprias palavras.

### 3.2 Voz como canal prioritário

A voz deve ser tratada como canal prioritário por permitir expressão mais natural, contextual e detalhada.

A experiência deve também oferecer alternativas acessíveis, incluindo texto e preenchimento estruturado quando necessário.

### 3.3 Canais multimodais candidatos

- voz;
- conversa por texto;
- documentos autorizados;
- imagens autorizadas;
- localização autorizada;
- calendário autorizado;
- wearables e aplicativos de saúde ou esporte autorizados;
- integrações profissionais autorizadas;
- histórico de interações e experiências da Guivos.

### 3.4 Fluxo conceitual

```text
Participante
  -> Entrada multimodal
  -> Context Intelligence Engine
  -> proposta de interpretação
  -> confirmação, correção ou limitação pelo participante
  -> Modelo Vivo do Participante
  -> Journey e demais camadas autorizadas
```

### 3.5 Regras

1. O participante não deve ser obrigado a revelar informações além do necessário para a experiência escolhida.
2. Inferências relevantes devem ser explicáveis e revisáveis.
3. Informações sensíveis exigem critérios superiores de consentimento e governança.
4. O sistema deve diferenciar fatos declarados, dados integrados, evidências observadas e inferências provisórias.
5. O participante deve poder corrigir, complementar, ocultar ou limitar o uso das informações, observadas restrições legais e operacionais.

## 4. Modelo Vivo do Participante — Conceito Candidato

O `Living Participant Model (LPM)` representa, provisoriamente, a estrutura dinâmica utilizada para consolidar o contexto autorizado de um participante ao longo do tempo.

O LPM não é um cadastro estático nem um perfil público. Ele é uma representação contextual, temporal, explicável e continuamente atualizável.

Elementos candidatos:

- identidade;
- Momento Atual;
- objetivos;
- Próximos Passos;
- interesses;
- competências;
- preferências;
- limitações;
- disponibilidade;
- relacionamentos;
- experiências;
- evidências de evolução;
- proveniência;
- confiança;
- permissões.

O conceito permanece em Discovery/Engineering e deverá ser formalizado apenas após o Architecture Engineering Sprint e futura avaliação da GPMA.

## 5. Context Intelligence Engine — Capacidade Candidata

O `Context Intelligence Engine (CIE)` é uma capacidade candidata da Intelligence Layer para receber entradas multimodais autorizadas, interpretar contexto, propor atualizações do LPM e preservar proveniência, confiança, temporalidade e explicabilidade.

O CIE não pertence à Experience Layer e não deve alterar silenciosamente informações sensíveis ou permanentes sem critérios de confirmação e governança.

## 6. Hierarquia Documental de Produto

O desenvolvimento funcional do Journey seguirá a hierarquia:

```text
GPA
  -> PAS
       -> JFA
            -> FDS
       -> UX Specification
       -> Technical Specification
```

- PAS define o produto/camada;
- JFA define os domínios funcionais permanentes;
- FDS detalha cada domínio funcional;
- UX define a interação;
- Technical Specification define a implementação.

## 7. Ponto de retomada

Este documento está preservado durante o Architecture Engineering Sprint.

Após a definição da taxonomia e do meta-modelo do GKR, a próxima etapa do PAS-001 deverá:

1. confirmar a posição de JFA e FDS na taxonomia oficial;
2. iniciar a JFA do Journey;
3. detalhar o domínio de Captura Multimodal de Contexto;
4. modelar os limites entre Journey, CIE, LPM, Grafo Global e Platform Layer;
5. avançar posteriormente para Missão, Objetivos Estratégicos, Público-alvo, Arquitetura Funcional, Fluxos, Integrações, Modelo Econômico, KPIs e Roadmap.