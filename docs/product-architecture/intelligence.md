---
id: GPA-006
title: Guivos Intelligence
status: consolidated
version: 1.6.0
owner: Guivos
last_updated: 2026-08-18
related_models:
  - GAI-001
  - GAI-002
related:
  - ADR-007
  - GEA-GRAPH-REFERENCE-001
  - PAS-001-DOMAIN-MODEL-001
  - GKR-INTELLIGENCE-CONTINUITY-001
---

# Guivos Intelligence

## 1. Papel e natureza

Guivos Intelligence é o **produto especializado transversal da Guivos e a Intelligence Layer do ecossistema**.

Sua responsabilidade é transformar dados autorizados, conhecimento, evidências, contextos e relações do ecossistema em **compreensão útil e contextualizada**, incluindo indicadores, análises, insights, possibilidades, recomendações, tendências e outros outputs explicáveis dentro dos limites de autoridade de cada contexto.

Sua unidade superior de valor não é quantidade de dados, número de dashboards ou uso de determinada tecnologia. É a capacidade de **aumentar compreensão para apoiar melhores decisões e ampliar possibilidades sem retirar a autonomia de quem legitimamente decide**.

Princípio superior:

> **Compreender não significa decidir.**

A Intelligence pode compreender, relacionar, interpretar, identificar sinais, agregar, comparar, estimar, recomendar e explicar quando houver finalidade e autoridade adequadas. Ela não adquire automaticamente autoridade para decidir pela Pessoa, pelo Journey, pelo Business, por outro produto especializado ou por uma Organização.

## 2. Duas frentes principais de geração de valor

Guivos Intelligence possui **um único núcleo de inteligência** e duas frentes superiores de atuação.

```text
GUIVOS INTELLIGENCE
│
├── FRENTE PESSOA / JOURNEY
│   → compreender contexto individual autorizado
│   → tornar a Journey mais relevante
│   → revelar possibilidades e apoiar escolhas
│
└── FRENTE BUSINESS / POPULAÇÃO
    → compreender movimentos agregados e protegidos
    → identificar o que emerge na população
    → apoiar decisões empresariais sem expor a Journey individual
```

Essas frentes não são dois produtos e não criam duas autoridades independentes. Elas utilizam o mesmo núcleo de Intelligence com **finalidade, granularidade, autoridade e forma de entrega diferentes**.

## 3. Frente Pessoa / Journey

Na frente Pessoa, Guivos Intelligence apoia o Guivos Journey a compreender melhor o contexto vivo do participante e a revelar possibilidades potencialmente relevantes para sua própria jornada.

A pergunta funcional superior é:

> **O que pode ser relevante para esta pessoa, neste momento, considerando sua própria jornada?**

Quando houver finalidade, autorização e base adequadas, o Intelligence poderá relacionar elementos como:

- objetivos declarados;
- interesses;
- Domínios de Evolução confirmados;
- estado `Ainda estou descobrindo`;
- possibilidades visualizadas, exploradas, ignoradas ou rejeitadas;
- experiências realizadas;
- conteúdos consumidos;
- preferências;
- restrições declaradas;
- disponibilidade;
- localização quando pertinente;
- mudanças ao longo do tempo;
- conhecimento e evidências governadas;
- relações legítimas existentes no ecossistema.

Esses elementos formam sinais contextuais; não constituem automaticamente verdades permanentes sobre a Pessoa.

```text
SINAL ≠ IDENTIDADE
INTERESSE ≠ NECESSIDADE
EXPLORAÇÃO ≠ CONDIÇÃO
```

A Intelligence pode ajudar a Journey a descobrir e relacionar possibilidades provenientes de diferentes áreas do ecossistema, incluindo, conforme pertinência e autoridade:

- conhecimentos;
- conteúdos;
- especialistas;
- coletivos;
- organizações;
- experiências;
- eventos;
- viagens;
- produtos e serviços;
- oportunidades;
- outros recursos legítimos.

Uma possibilidade não se reduz a item comercial.

```text
POSSIBILIDADE ≠ ITEM PARA VENDA
```

A Intelligence não cria a Journey pela Pessoa.

```text
INTELLIGENCE
→ compreende / relaciona / identifica / sugere / explica

JOURNEY
→ governa a experiência, a pertinência e a apresentação dentro de sua autoridade

PESSOA
→ escolhe o próprio caminho
```

## 4. Contexto Vivo e temporalidade

O Intelligence deve trabalhar com contexto vivo, temporal e revisável, não com perfil humano rígido.

Uma Pessoa pode mudar interesses, prioridades, objetivos, disponibilidade, localização, restrições e significados ao longo do tempo.

```text
PERFIL FIXO
✕

CONTEXTO VIVO
✓
```

Informações contextuais podem estar, conforme aplicável:

- atuais;
- possivelmente desatualizadas;
- substituídas;
- retiradas;
- expiradas;
- contestadas;
- incertas.

Em questões de intenção, preferência, objetivo e significado pessoal, a declaração legítima da Pessoa deve prevalecer sobre inferência incompatível quando essa autoridade pertencer à própria Pessoa.

O Intelligence deve admitir correção, contestação, atualização e retirada quando aplicáveis, sem obrigar o participante a compreender detalhes técnicos de modelos, pesos, embeddings ou grafos.

## 5. Frente Business / População

Na frente Business, Guivos Intelligence transforma sinais legitimamente utilizáveis em **compreensão agregada, protegida e contextualizada de populações** vinculadas à relação Business.

A pergunta funcional superior é:

> **O que está emergindo dentro desta população e o que a empresa pode compreender a partir disso?**

A empresa não deve receber um “Intelligence por funcionário”. O valor está em compreender o todo e seus movimentos, não em reconstruir a vida individual das Pessoas.

Famílias de leitura candidatas já autorizadas conceitualmente incluem:

- participação;
- adesão;
- recorrência;
- utilização;
- alcance;
- interesses agregados;
- movimentos temporais;
- temas emergentes;
- distribuições;
- comparações entre períodos;
- tendências;
- aderência entre interesse agregado e oferta disponível;
- lacunas aparentes;
- subutilização conhecida pela Guivos;
- benchmarks autorizados;
- insights explicáveis para decisão empresarial.

A empresa pode utilizar essas leituras para investigar onde pode ampliar condições, benefícios, iniciativas, acessos e possibilidades.

```text
COMPREENDER A POPULAÇÃO
≠ VIGIAR INDIVÍDUOS
```

Guivos Intelligence não substitui os sistemas internos da empresa e não depende, como arquitetura padrão, de importar bases completas de RH, folha, absenteísmo, produtividade, CRM ou ERP.

A empresa pode combinar, em seu próprio ambiente analítico, indicadores Guivos com seus KPIs internos quando exportação ou integração estiver autorizada e disponível.

```text
RESULTADO OBSERVADO NA GUIVOS
≠ RESULTADO OPERACIONAL INTERNO DA EMPRESA
```

Correlação ou tendência observada na Guivos não constitui prova automática de causalidade, impacto humano ou melhoria de KPI interno.

## 6. Assimetria entre personalização e exposição

A arquitetura do Intelligence estabelece uma assimetria intencional:

```text
PROFUNDIDADE DE COMPREENSÃO
≠ PROFUNDIDADE DE EXPOSIÇÃO

AUTORIDADE PARA PERSONALIZAR
≠ AUTORIDADE PARA COMPARTILHAR
```

O Intelligence pode utilizar contexto individual autorizado para tornar a experiência da própria Pessoa mais relevante. Isso não cria autorização para entregar a mesma granularidade a uma empresa, Organização ou outro terceiro.

Regra superior:

```text
INDIVIDUAL
→ serve prioritariamente à própria Pessoa

AGREGADO E PROTEGIDO
→ pode servir ao Business quando finalidade e autoridade permitirem
```

Mais capacidade comercial não compra mais autoridade sobre a vida da Pessoa.

```text
ENTERPRISE
≠ ACESSO MAIS PROFUNDO À JOURNEY INDIVIDUAL
```

## 7. Núcleo funcional compartilhado

As responsabilidades funcionais do Guivos Intelligence atualmente consolidadas são:

1. **Contexto** — organizar sinais autorizados em contexto interpretável, vivo e temporal;
2. **Conhecimento** — relacionar contexto com conhecimento governado, fontes e evidências;
3. **Relações** — compreender conexões entre participantes, objetivos, oportunidades, experiências, conhecimento, produtos e demais objetos autorizados;
4. **Compreensão** — transformar dados, contexto, conhecimento, relações e temporalidade em leitura útil;
5. **Relevância** — apoiar a avaliação de pertinência contextual sem transformar relevância em obrigação ou prioridade comercial;
6. **Descoberta de possibilidades** — identificar caminhos e recursos potencialmente relevantes no ecossistema;
7. **Agregação** — transformar sinais legitimamente utilizáveis em visões populacionais protegidas;
8. **Insights e tendências** — identificar padrões, mudanças, sinais, movimentos emergentes e interpretações úteis;
9. **Explicabilidade** — informar por que algo foi apresentado, quais bases foram consideradas, quais limitações existem e o que a leitura não significa;
10. **Aprendizado governado** — atualizar compreensão ao longo do tempo sem tratar armazenamento irrestrito como requisito de inteligência.

Essas responsabilidades são **capacidades funcionais de produto**. Elas não declaram microserviços, componentes físicos ou uma família técnica obrigatória de engines.

`GIA-000` mantém `Context Intelligence Engine`, `Recommendation Intelligence Engine`, `Matching Intelligence Engine`, `Learning Intelligence Engine`, `Prediction Intelligence Engine`, `Trust Intelligence Engine` e `Knowledge Intelligence Engine` como candidatos técnicos/arquiteturais, não como componentes implementados ou automaticamente promovidos por esta versão de `GPA-006`.

## 8. Classes de input

Guivos Intelligence distingue a natureza das informações utilizadas.

### 8.1 Declarado

Aquilo que uma Pessoa ou autoridade legítima informou explicitamente.

```text
DECLARADO
= alguém afirmou diretamente
```

Declaração não é necessariamente eterna, mas possui autoridade própria sobre intenção, preferência e significado pessoal quando aplicável.

### 8.2 Observado

Evento efetivamente registrado dentro de um contexto autorizado.

Exemplos incluem visualização, participação, utilização, acesso, transação, conclusão ou outro evento verificável.

```text
OBSERVADO
= evento registrado

OBSERVADO
≠ interpretação automática da intenção
```

### 8.3 Operacional

Dados necessários para funcionamento do ecossistema, como elegibilidade, disponibilidade, idioma, país, moeda, plano, programa, configuração, permissões, status e território.

Relevância pode depender de viabilidade contextual, não apenas de afinidade temática.

### 8.4 Calculado

Resultado reproduzível de transformação conhecida sobre dados disponíveis, como participação, recorrência, percentual, distribuição, média, variação ou crescimento.

### 8.5 Inferido

Interpretação que tenta representar algo não diretamente declarado ou observado.

```text
INFERIDO
≠ DECLARADO
≠ FATO
≠ DIAGNÓSTICO
```

### 8.6 Predito

Estimativa sobre estado futuro.

```text
PREVISÃO
≠ FUTURO DETERMINADO
```

### 8.7 Conhecimento externo ou governado

Conhecimento proveniente de universidades, pesquisas, instituições, especialistas, literatura, normas, bases públicas, conhecimento canônico da Guivos ou outras fontes adequadas.

A existência de uma publicação não garante autoridade universal nem incorporação automática.

## 9. Proveniência, finalidade e autoridade de uso

O fato de a Guivos conhecer uma informação não significa que o Intelligence possa utilizá-la para qualquer finalidade ou compartilhá-la com qualquer consumidor.

```text
CONHECER
≠ UTILIZAR
≠ COMPARTILHAR
```

Informações materialmente relevantes devem preservar, conforme aplicável:

- origem;
- natureza;
- autoridade;
- contexto;
- finalidade;
- temporalidade;
- confiabilidade;
- proveniência;
- versão;
- possibilidade de correção ou contestação;
- restrições de uso;
- restrições de compartilhamento.

A finalidade legítima deve preceder a seleção de dados.

```text
FINALIDADE LEGÍTIMA
→ DADOS NECESSÁRIOS
→ MENOR GRANULARIDADE SUFICIENTE
→ PROCESSAMENTO
→ OUTPUT AUTORIZADO
```

O Grafo Global não autoriza utilização irrestrita de todas as relações tecnicamente disponíveis.

## 10. Arquitetura dos outputs

Guivos Intelligence produz diferentes classes de output, e cada uma possui autoridade própria.

### 10.1 Descrição

- **Indicador** — medida calculada sobre fenômeno observável;
- **Distribuição** — como determinado fenômeno se reparte;
- **Comparação** — diferença entre períodos, populações ou recortes comparáveis e autorizados;
- **Estado observado** — declaração ou evento apresentado preservando sua natureza.

### 10.2 Interpretação

- **Padrão** — regularidade observada;
- **Sinal** — mudança ou ocorrência que merece atenção, ainda com evidência limitada;
- **Movimento Emergente** — mudança que começa a ganhar consistência dentro de determinada população ao longo do tempo;
- **Insight** — interpretação contextual relevante produzida a partir de indicadores, relações, padrões, conhecimento ou mudanças observadas.

### 10.3 Projeção

- **Tendência** — direção consistente observada ao longo do tempo;
- **Estimativa** — valor aproximado ou esperado;
- **Previsão** — estimativa sobre estado futuro, sempre acompanhada de horizonte, base e incerteza quando materialmente relevante.

### 10.4 Orientação

- **Possibilidade** — caminho, recurso, experiência ou conexão que pode ser considerado;
- **Oportunidade** — possibilidade concreta disponível em determinado contexto;
- **Recomendação** — sugestão contextual, não decisão;
- **Caminho a explorar** — direção possível para investigação ou reflexão, especialmente quando ainda não há base para recomendação específica.

### 10.5 Referência

- **Benchmark** — comparação autorizada com histórico, grupos comparáveis, ecossistema ou referência externa, com metodologia e limites adequados.

### 10.6 Transparência

- explicação;
- proveniência;
- incerteza;
- limitações;
- o que determinada leitura não significa.

Princípio superior:

> **Todo output do Guivos Intelligence deve preservar a diferença entre o que foi observado, o que foi calculado, o que foi interpretado e o que está sendo sugerido.**

Quanto maior a distância entre o dado de origem e a conclusão apresentada, maior deve ser a explicabilidade e a representação de incerteza.

## 11. Movimento Emergente

`Movimento Emergente` é um conceito funcional relevante para a frente Business.

```text
SINAL INICIAL
→ RECORRÊNCIA
→ PERSISTÊNCIA
→ AMPLIAÇÃO
→ MOVIMENTO EMERGENTE
```

Ele descreve algo que começa a ganhar consistência na população e pode justificar investigação empresarial.

```text
MOVIMENTO EMERGENTE
≠ DIAGNÓSTICO
≠ CAUSA
≠ NECESSIDADE COMPROVADA
```

A função do Intelligence é revelar perguntas relevantes e possibilidades de ação, não fabricar diagnóstico coletivo.

## 12. Relação entre interesse agregado e oferta empresarial

Uma capacidade relevante do Intelligence Business é relacionar, de forma agregada e protegida:

```text
O QUE EMERGE NA POPULAÇÃO
↕
O QUE A EMPRESA DISPONIBILIZA
```

Leituras possíveis incluem:

- interesse alto + oferta adequada → cobertura potencialmente adequada;
- interesse alto + oferta limitada → possível lacuna;
- oferta alta + utilização baixa → possível problema de descoberta, aderência ou utilização;
- interesse crescente → possibilidade de revisão ou criação de iniciativa.

Essas leituras são interpretações; não são prova automática de causa.

## 13. Explicabilidade

Outputs relevantes devem poder responder proporcionalmente:

- o que está sendo mostrado;
- por que apareceu;
- quais elementos foram considerados;
- se a base foi declarada, observada, calculada ou inferida;
- qual incerteza permanece;
- quais limitações existem;
- o que a leitura não significa.

Na frente Pessoa, a explicação deve ser compreensível e permitir correção quando aplicável.

Na frente Business, a explicação deve reduzir risco de que gestores convertam movimentos agregados em diagnóstico, causalidade ou conclusão individual indevida.

Explicabilidade não exige expor pesos internos, embeddings, scores intermediários ou todos os eventos processados quando isso não for necessário para compreensão proporcional.

## 14. Privacidade, agregação e proteção populacional

A frente Business deve operar sobre populações e recortes protegidos.

```text
SEM NOME
≠ ANÔNIMO

AGREGADO
≠ AUTOMATICAMENTE SEGURO
```

A proteção deve considerar risco de reidentificação contextual, especialmente em grupos pequenos, cruzamentos excessivamente específicos e temas sensíveis.

Sem congelar limites quantitativos nesta versão, a arquitetura admite mecanismos como:

- supressão;
- agregação;
- generalização;
- limitação de cruzamentos;
- redução de precisão quando necessário;
- não geração de determinado output quando a finalidade ou a proteção forem insuficientes.

Um dado tecnicamente agregável não é automaticamente um indicador empresarial legítimo.

```text
TECNICAMENTE AGREGÁVEL
≠ LEGITIMAMENTE ÚTIL PARA BUSINESS
```

## 15. Temas sensíveis

A sensibilidade deve considerar conteúdo, contexto, finalidade e possibilidade de inferência, não apenas o tipo técnico do campo.

Um tema sensível pode ser utilizado, quando autorizado e apropriado, para apoiar a própria Pessoa na Journey.

```text
APOIAR A PESSOA
≠ EXPOR O TEMA À EMPRESA
```

Business não deve receber por padrão:

- Journey individual;
- objetivos pessoais identificáveis;
- Next Step individual;
- intenções individuais;
- conteúdo privado;
- explicação individual de pertinência;
- inferências sensíveis individualizadas;
- histórico pessoal detalhado;
- ranking humano;
- score de evolução;
- perfil psicológico;
- diagnóstico.

Guivos Intelligence também não deve produzir a partir de comportamento na Guivos conclusões automáticas como “funcionários ansiosos”, “equipe desmotivada”, “população financeiramente vulnerável” ou equivalentes sem autoridade e base adequadas.

## 16. Domínios de Evolução do Journey

`PAS-001-DOMAIN-MODEL-001` continua governando o vocabulário canônico dos nove Domínios de Evolução utilizados pelo Guivos Journey:

1. Saúde e Bem-estar;
2. Trabalho, Carreira e Estudos;
3. Vida Financeira;
4. Empreendedorismo e Projetos;
5. Relacionamentos e Vida Social;
6. Espiritualidade, Propósito e Valores;
7. Viagens, Lazer, Cultura e Novas Experiências;
8. Causas, Voluntariado e Contribuição;
9. Organização e Equilíbrio da Vida.

Intelligence poderá sugerir domínios, subáreas e relações como **candidatos explicáveis** quando houver finalidade e base adequadas.

```text
domínio candidato ≠ domínio confirmado
domínio ≠ identidade
domínio ≠ diagnóstico
domínio ≠ prioridade humana
domínio ≠ score
domínio ≠ prova de evolução
```

A declaração direta do participante, quando aplicável e legítima, deverá prevalecer sobre inferência incompatível.

Devem permanecer possíveis múltiplos domínios simultâneos, estado `Ainda estou descobrindo`, área ainda não mapeada, contestação, retirada, incerteza e ausência legítima de classificação.

## 17. Grafo, IA e tecnologias subordinadas

O **Grafo Global da Guivos** é conceito e capacidade do ecossistema; não é sinônimo de Guivos Intelligence nem de um fornecedor de banco de dados.

Por `ADR-007`, Neo4j permanece a tecnologia primária de referência para a camada de grafo, e `GEA-GRAPH-REFERENCE-001` governa a relação entre grafo, Graph Analytics, GraphRAG, Guivos Intelligence e consumo analítico.

Separação obrigatória:

```text
Grafo Global da Guivos
= modelo/capacidade de conexões governadas

Guivos Intelligence
= produto especializado e Intelligence Layer

Neo4j
= tecnologia de referência para realização da camada de grafo
```

Guivos Intelligence também não é apenas inteligência artificial.

```text
GUIVOS INTELLIGENCE
≠ IA
≠ LLM
≠ GUIVOS.AI
≠ DASHBOARD
≠ POWER BI
≠ NEO4J
≠ GRAPHRAG
```

IA, regras, analytics, estatística, grafo, machine learning, modelos preditivos, conhecimento governado e revisão humana podem participar da realização do produto conforme autoridade posterior.

A escolha de Neo4j não declara instância, POC, cluster, Aura, dados carregados, Graph Data Science, GraphRAG, integração com Power BI ou produção implementados.

## 18. Graph Analytics e GraphRAG

Graph Analytics pode apoiar análises estruturais quando houver finalidade e dados autorizados.

Resultados como centralidade, comunidades, similaridade ou previsão de relações são medidas técnicas contextualizadas e não podem ser convertidos automaticamente em valor humano, mérito, evolução, pertencimento, confiança ou verdade.

```text
centralidade ≠ importância humana
score técnico ≠ valor humano
comunidade algorítmica ≠ identidade
previsão de relação ≠ relação existente
```

GraphRAG permanece padrão candidato de recuperação de contexto e relações governadas antes de geração por modelo de linguagem.

Ele não substitui Guivos Knowledge Architecture, Canon, validação de evidências, proveniência, permissões ou distinção entre fato, inferência e síntese.

Uma resposta gerada não se torna conhecimento canônico apenas por ter utilizado grafo como contexto.

## 19. Consumo analítico e Power BI

Guivos Intelligence poderá disponibilizar, quando autorizado, métricas e visões agregadas para Business Intelligence e dashboards executivos.

Power BI é consumidor analítico possível, não fonte de verdade do Intelligence.

A forma técnica de integração permanece dependente de decisão posterior e deverá respeitar finalidade, minimização, autorização, segurança, volume, custo, rastreabilidade e independência do fornecedor.

## 20. Guardrails permanentes

Guivos Intelligence não deverá:

- decidir o que uma Pessoa deve querer;
- impor objetivos ou caminhos;
- manipular escolhas;
- transformar probabilidade em certeza;
- tratar uma única fonte como verdade automática;
- substituir profissionais especializados;
- utilizar contexto pessoal protegido para publicidade comportamental sensível;
- criar score global de evolução;
- transformar Domínios de Evolução em identidade;
- transformar analytics agregado em exposição individual;
- vender acesso à intimidade da Journey como diferenciação comercial;
- utilizar plano comercial como justificativa para reduzir proteção;
- priorizar venda em prejuízo da pertinência;
- converter correlação em causalidade;
- transformar interesse em diagnóstico;
- criar ranking humano universal;
- operar como ferramenta de avaliação individual de RH, promoção, demissão ou classificação de valor humano.

Separações permanentes:

```text
CORRELAÇÃO ≠ CAUSALIDADE
PADRÃO ≠ CAUSALIDADE
INTERESSE ≠ NECESSIDADE
NECESSIDADE ≠ PROBLEMA
EXPLORAÇÃO ≠ CONDIÇÃO
UTILIZAÇÃO ≠ SATISFAÇÃO
MAIOR PARTICIPAÇÃO ≠ MAIOR EVOLUÇÃO
COMPREENDER ≠ VIGIAR
```

## 21. Relações atuais com produtos especializados

Esta versão preserva somente os contratos já formalizados em autoridades superiores existentes:

- **Guivos Journey** — Intelligence apoia compreensão de contexto, relevância, possibilidades e recomendações, sem tomar a decisão da Pessoa nem absorver a autoridade da experiência;
- **Guivos Business** — Intelligence não é módulo do Business; pode produzir leituras agregadas e protegidas a partir do que a Guivos legitimamente conhece, sem transformar contexto individual em dado empresarial;
- **Guivos Mall** — pode apoiar relevância, curadoria e descoberta, sem absorver autoridade comercial/transacional do Mall;
- **Guivos Travel** — pode apoiar contexto e recomendação de experiências, sem governar operação de viagem;
- **Guivos Media** — pode apoiar organização e descoberta de conhecimento, sem absorver autoridade editorial;
- **Guivos Ads** — pode apoiar mensuração e contexto autorizado, sem transformar contexto sensível da Pessoa em autorização de targeting.

Os **contratos detalhados e completos Intelligence ↔ Journey, Business, Mall, Travel, Media e Ads ainda não estão convergidos** nesta versão e constituem o próximo checkpoint da frente de produto.

## 22. Decisão de nomenclatura

`Guivos Intelligence` permanece como nome oficial do produto.

`Inteligência do Ecossistema Guivos` permanece como expressão conceitual e pública para a inteligência entregue pelo produto.

Guivos Intelligence não deve ser reduzido a `Guivos Insights`, dashboard ou assistente conversacional.

## 23. Estado de maturidade

Estão consolidados documentalmente nesta versão:

- identidade de Guivos Intelligence como Produto Especializado transversal e Intelligence Layer;
- princípio `Compreender ≠ decidir`;
- unidade de valor baseada em compreensão útil e contextualizada;
- duas frentes principais: Pessoa/Journey e Business/População;
- núcleo funcional compartilhado de dez responsabilidades;
- Contexto Vivo como contexto temporal e revisável;
- taxonomia funcional de inputs;
- princípio `Conhecer ≠ utilizar ≠ compartilhar`;
- finalidade antes da utilização;
- taxonomia funcional de outputs;
- conceito de Movimento Emergente;
- distinção entre possibilidade, oportunidade e recomendação;
- explicabilidade proporcional;
- assimetria entre personalização e exposição;
- leitura Business agregada e protegida;
- limites de segmentação e reidentificação em nível conceitual;
- guardrails de temas sensíveis;
- relação vigente com Domínios de Evolução;
- separação entre produto, grafo, IA, Neo4j, GraphRAG e Power BI.

Continuam dependentes de detalhamento, validação ou autoridade posterior:

- Checkpoint 7 — contratos detalhados com Journey, Business, Mall, Travel, Media e Ads;
- Checkpoint 8 — relação definitiva entre capacidades de produto, engines candidatos, IA, grafo, GraphRAG e analytics;
- Checkpoint 9 — modos de entrega e experiência própria do Intelligence;
- Checkpoint 10 — modelo comercial, licenciamento, incorporação em planos e contratação;
- Checkpoint 11 — governança final, maturidade e gaps;
- Checkpoint 12 — Documento Mestre / `GPA-006` v2 final;
- ontologia formal completa;
- modelo lógico e físico;
- POC;
- infraestrutura;
- mecanismos técnicos de consentimento;
- atualização de conhecimento em produção;
- auditoria algorítmica operacional;
- Graph Analytics operacional;
- GraphRAG operacional;
- integração Power BI implementada;
- explicabilidade operacional por tipo de output;
- limites quantitativos de proteção populacional;
- Home Pública do Guivos Intelligence;
- Source Lock, Design, wireframe, UI ou protótipo da futura Home.

O ponto exato de continuidade está registrado em `GKR-INTELLIGENCE-CONTINUITY-001`.
