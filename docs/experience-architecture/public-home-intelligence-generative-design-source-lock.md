---
id: GKR-UX-HOME-INTELLIGENCE-GENINPUT-001
title: Source Lock Operacional — Home Pública — Guivos Intelligence — Primeira Exploração de Design
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-20
parent: GKR-UX-HOMES-GENINPUT-001
depends_on:
  - GKR-UX-HOME-INTELLIGENCE-HANDOFF-001
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001
  - GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001
  - GPA-006
  - GKR-UX-HOMES-OUTCOME-001
normative: true
---

# Source Lock Operacional — Home Pública — Guivos Intelligence

## 1. Finalidade

Esta instância prepara a primeira exploração de Design da **Home Pública do Guivos Intelligence v1**.

Ela congela o input operacional permitido para arquitetura visual e wireframe low-fi responsivo, transformando o Handoff Canônico em instruções executáveis sem criar nova autoridade semântica.

Estado inicial obrigatório:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

Invariante:

> **GENINPUT TRADUZ O HANDOFF ≠ REDEFINE A HOME**

## 2. Source Lock

- Home: `Guivos Intelligence`.
- Fase: `arquitetura visual + wireframe low-fi responsivo`.
- Checkpoint: `main @ 43ed02030dc03600ce756ce63ea55bd3e742f910`.
- Handoff: `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`.
- Objetivo: validar se a experiência consegue tornar visível como informações dispersas e isoladas podem ganhar contexto, relações e interpretação, produzindo compreensão útil sem transformar Intelligence em IA, dashboard, grafo, sistema de decisão ou previsão do futuro.

## 3. Fontes autorizadas

Fornecer diretamente à etapa de Design somente:

1. este Source Lock Operacional;
2. `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0` — `docs/experience-architecture/public-home-intelligence-design-handoff.md`;
3. `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0` — `docs/experience-architecture/public-home-intelligence-source-lock.md`;
4. `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.1.1` — `docs/experience-architecture/public-home-intelligence-master-document.md`;
5. `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
6. `GPA-006 v2.0.0`.

A arquitetura narrativa detalhada e o contrato transversal de outcome permanecem autoridades do GKR, mas não precisam ser adicionados como documentos extras à ferramenta quando sua função já estiver preservada pelas fontes acima.

Não adicionar automaticamente:

- outras Homes;
- benchmarks externos;
- documentos de pricing;
- telas internas;
- materiais de implementação;
- Neo4j, GraphRAG, Power BI, Guivos.ai ou outros materiais tecnológicos;
- checkpoints históricos;
- rascunhos de conversa.

Consultas adicionais exigem dúvida concreta e ampliação deliberada do Source Lock.

## 4. Unidade de valor e centro semântico

Unidade de valor:

> **compreensão útil e contextualizada.**

Ideia-mãe:

> **Compreender melhor amplia o que você consegue perceber.**

Pergunta-mãe:

> **O que se torna possível quando você compreende melhor o que está acontecendo?**

Apoio inicial:

> **Entenda melhor o que está acontecendo. Amplie o que você consegue perceber.**

Autonomia:

> **Veja mais antes de decidir.**

Fechamento:

> **Perceba antes o que começa a mudar. Enxergue além do que já está evidente.**

> **Novas possibilidades podem se tornar mais visíveis.**

Contrato superior:

```text
INFORMAÇÃO ≠ COMPREENSÃO
COMPREENDER ≠ DECIDIR
```

## 5. Invariantes

Preservar:

1. Guivos Intelligence como Intelligence Layer transversal da Guivos;
2. `compreensão útil e contextualizada` como unidade de valor;
3. informação não é compreensão;
4. compreender não é decidir;
5. Intelligence conecta informações, contexto, relações, conhecimento e evidências para ampliar compreensão;
6. o resultado principal não é mais dados, mas maior capacidade de perceber;
7. informações isoladas mostram apenas parte do que pode ser compreendido;
8. relações podem ajudar a tornar conexões, recorrências, mudanças e movimentos mais visíveis;
9. relação não significa causalidade;
10. padrão não significa causa;
11. sinal não significa certeza;
12. tendência não significa destino;
13. perceber antes não significa prever o futuro;
14. a decisão permanece com a pessoa ou autoridade legítima;
15. explicabilidade integra a proposta de valor;
16. os onze movimentos são funções semânticas obrigatórias, sem exigir onze seções equivalentes;
17. `M03 ≠ M10`;
18. `M04 ≠ M05`;
19. Pessoa/Journey e Business/população permanecem duas frentes distintas;
20. Business não recebe Intelligence individual protegido de uma pessoa;
21. `PERSONALIZAR ≠ EXPOR`;
22. agregado não significa automaticamente seguro;
23. IA é capacidade subordinada;
24. Graph é capacidade subordinada;
25. tecnologia não substitui a definição pública do produto;
26. resultado deve aparecer antes do mecanismo;
27. linguagem compreensível deve vir antes de terminologia analítica;
28. complexidade técnica não deve ser usada como prova visual de sofisticação.

## 6. Arquitetura funcional a preservar

```text
01 — POSSIBILIDADE
Compreender melhor amplia o que pode ser percebido.

02 — NECESSIDADE
Ter mais informação não significa entender melhor.

03 — VALOR PRÓPRIO
Entenda o que informações isoladas não conseguem mostrar.

04 — RESULTADOS
Veja o que está conectado.
Perceba o que se repete.
Entenda o que está mudando.
Veja o que começa a ganhar força.

05 — MATERIALIZAÇÃO
Indicadores / comparações / contexto / relações / leituras.

06 — FORMAÇÃO DA COMPREENSÃO
Informações + contexto + relações + conhecimento e evidências → compreensão.

07 — APLICAÇÃO
Onde essa compreensão pode ser útil na prática.

08 — CONFIANÇA
Não veja apenas a conclusão. Entenda de onde ela veio.

09 — AUTONOMIA
Veja mais antes de decidir.

10 — INTELIGÊNCIA CONECTADA
Uma informação pode mostrar mais quando você entende com o que ela se relaciona.

11 — HORIZONTE AMPLIADO
Perceba antes o que começa a mudar.
Enxergue além do que já está evidente.
```

Os onze movimentos governam função e progressão. Design pode agrupá-los, condensá-los, distribuí-los em mais de um elemento ou materializá-los com outra geometria desde que nenhuma função seja perdida.

Separações obrigatórias:

```text
M03
→ define por que Intelligence existe

M10
→ aprofunda por que relações importam

M04
→ mostra os resultados perceptíveis

M05
→ demonstra esses resultados de forma concreta
```

## 7. Copy congelada e CTAs

Preservar literalmente, salvo quebra de linha ou distribuição visual sem alteração de sentido:

Pergunta-mãe:

> **O que se torna possível quando você compreende melhor o que está acontecendo?**

Apoio:

> **Entenda melhor o que está acontecendo. Amplie o que você consegue perceber.**

Autonomia:

> **Veja mais antes de decidir.**

Fechamento:

> **Perceba antes o que começa a mudar. Enxergue além do que já está evidente.**

> **Novas possibilidades podem se tornar mais visíveis.**

CTA principal:

> **Veja o que suas informações podem mostrar**

CTA secundário:

> **Conheça o Guivos Intelligence**

Copy de apoio não congelada pode ser tratada apenas como hipótese de Content Design e deve permanecer identificável como hipótese durante a exploração.

## 8. Direção de experiência

Direção semântica:

> **clareza emergindo da complexidade.**

Transformações visuais de referência:

```text
DISPERSÃO → RELAÇÃO
RUÍDO → PADRÃO
ESTADO → MUDANÇA
SINAL → MOVIMENTO PERCEPTÍVEL
NÚMERO → CONTEXTO
CONCLUSÃO → EXPLICAÇÃO
INFORMAÇÃO → COMPREENSÃO
```

A primeira impressão deve ser de **ampliação de percepção e compreensão**, não de software analítico, dashboard ou IA autônoma.

## 9. Liberdades de Design

Podem ser explorados:

- composição e grid;
- quantidade física de macroblocos;
- hierarquia visual;
- ritmo e densidade;
- tipografia provisória;
- fotografia, vídeo, ilustração e abstrações visuais;
- gráficos e visualizações conceituais;
- relações e redes visuais quando semanticamente úteis;
- indicadores e comparações;
- séries temporais;
- cards analíticos;
- tratamento de explicabilidade;
- tratamento visual das frentes Pessoa e Business;
- Header e navegação;
- tratamento dos CTAs congelados;
- responsividade desktop/mobile;
- microinterações;
- progressive disclosure;
- transições e motion conceituais;
- passagem visual de dispersão para compreensão.

Liberdade visual não autoriza alteração semântica.

## 10. Materialização analítica

Podem ser usados:

- KPI;
- indicador;
- percentual;
- variação;
- série temporal;
- comparação;
- distribuição;
- relação;
- mini gráfico;
- card analítico;
- recorrência;
- mudança;
- movimento emergente;
- sequência interpretativa;
- rede relacional.

Uma progressão de referência para demonstração é:

```text
INDICADOR
→ COMPARAÇÃO
→ CONTEXTO
→ RELAÇÃO
→ LEITURA
```

Exemplo conceitual autorizado:

```text
UTILIZAÇÃO
72% → 64%

ISOLADAMENTE
“houve queda”

EM CONTEXTO
→ quando começou?
→ em quais grupos?
→ ocorreu junto com quais outras mudanças?
→ é recorrente ou pontual?
```

Este exemplo é exclusivamente conceitual.

Guardrails:

```text
VISUAL ANALÍTICO ≠ DASHBOARD COMO PRODUTO
EXEMPLO CONCEITUAL ≠ DADO OPERACIONAL REAL
VISUALIZAÇÃO ≠ CLAIM COMPROVADO
```

> **Todo exemplo analítico deve demonstrar um tipo de leitura, e não provar que aquela leitura já está operacionalmente disponível.**

## 11. Confiança, explicabilidade e autonomia

A exploração deve encontrar uma forma perceptível de comunicar:

- o que foi observado;
- o que mudou;
- quais informações foram consideradas;
- como podem estar relacionadas;
- o que é fato;
- o que é interpretação;
- até onde a leitura pode ir;
- quais limites permanecem.

Contrato:

```text
RESULTADO / LEITURA
→ DE ONDE VEIO?
→ COMO FOI CONSTRUÍDO?
→ QUAIS INFORMAÇÕES ESTÃO RELACIONADAS?
→ O QUE É FATO?
→ O QUE É INTERPRETAÇÃO?
→ ATÉ ONDE ESSA LEITURA PODE IR?
```

Invariantes:

```text
COMPREENDER ≠ DECIDIR
MAIS COMPREENSÃO ≠ MENOS AUTONOMIA
RELAÇÃO ≠ CAUSA
CORRELAÇÃO ≠ CAUSALIDADE
INFERÊNCIA ≠ FATO
```

## 12. Duas frentes

### Pessoa / Journey

> **Entenda melhor por que determinadas informações, recomendações ou possibilidades podem aparecer em determinado contexto.**

```text
INTELLIGENCE → produz compreensão
JOURNEY → governa a experiência
PESSOA → escolhe
```

### Business / população

> **Compreenda padrões, mudanças e movimentos em populações de forma agregada e protegida.**

```text
INTELLIGENCE → produz leitura populacional
BUSINESS → governa a relação empresarial
EMPRESA → decide
```

A exploração pode escolher como representar essas duas frentes, mas não pode apagar a assimetria de privacidade nem sugerir Intelligence individual de funcionário disponível para a empresa.

## 13. Proibições de inferência

Não inventar como vigentes:

- número de usuários;
- clientes;
- organizações;
- parceiros;
- logos;
- cases;
- depoimentos;
- métricas;
- ganhos percentuais;
- precisão;
- acurácia;
- previsões comprovadas;
- redução de risco;
- aumento de produtividade;
- ROI;
- benchmarks;
- dados pessoais;
- scores humanos;
- diagnósticos;
- integrações;
- APIs;
- dashboards reais;
- disponibilidade de Neo4j;
- disponibilidade de GraphRAG;
- disponibilidade de Power BI;
- disponibilidade de Guivos.ai;
- modelos de IA específicos;
- infraestrutura técnica;
- planos;
- preços;
- limites;
- SLA;
- entitlements;
- funcionalidades não formalizadas.

Não transformar:

```text
INTELLIGENCE → IA AUTÔNOMA
INTELLIGENCE → DASHBOARD
INTELLIGENCE → CHATBOT
INTELLIGENCE → GRAFO
INTELLIGENCE → SOFTWARE DE RH
INTELLIGENCE → MONITORAMENTO DE FUNCIONÁRIO
INTELLIGENCE → MOTOR DE DECISÃO
INTELLIGENCE → SISTEMA DE PREVISÃO DO FUTURO
```

Também não comunicar que Intelligence:

- prevê o futuro;
- sabe o que vai acontecer;
- garante decisões melhores;
- encontra a decisão certa;
- determina causalidade automaticamente;
- diagnostica pessoas;
- cria score humano de evolução;
- revela Journey individual à empresa;
- comprova produtividade, redução de risco ou performance sem evidência vigente.

## 14. Placeholders

Quando necessário para testar hierarquia, usar rótulos explícitos, por exemplo:

- `[INDICADOR — EXEMPLO CONCEITUAL]`;
- `[SÉRIE TEMPORAL — DADOS FICTÍCIOS]`;
- `[RELAÇÃO — REPRESENTAÇÃO CONCEITUAL]`;
- `[COMPARAÇÃO — EXEMPLO]`;
- `[LEITURA — HIPÓTESE EXPLICATIVA]`;
- `[SINAL — EXEMPLO NÃO OPERACIONAL]`;
- `[CONTEXTO — PLACEHOLDER]`;
- `[DADO POPULACIONAL — FICTÍCIO]`;
- `[EXPLICAÇÃO — EXEMPLO]`.

Exemplos explicativos não devem ser convertidos em evidência, maturidade ou disponibilidade operacional.

## 15. Antiestética

Evitar como identidade principal:

- cérebro digital;
- rosto humano com circuitos;
- rede neural genérica;
- hologramas;
- HUD de ficção científica;
- dashboard com dezenas de gráficos;
- nuvem de pontos sem significado;
- código como decoração;
- globo conectado sem função;
- grafo decorativo;
- robô ou chatbot como protagonista.

Princípio:

> **O produto deve parecer sofisticado porque ajuda a compreender melhor, não porque parece tecnicamente complexo.**

## 16. Pacote entregue à ferramenta

Fornecer somente:

1. este Source Lock Operacional;
2. Handoff Canônico do Intelligence;
3. Home Source Lock do Intelligence;
4. Documento Mestre do Intelligence;
5. Product Source Lock do Intelligence;
6. `GPA-006 — Guivos Intelligence`.

## 17. Prompt controlado

```text
Você está trabalhando na primeira exploração de Design da Home Pública do Guivos Intelligence.

OBJETIVO
Crie uma arquitetura visual e wireframe low-fi responsivo para desktop e mobile que materialize Guivos Intelligence como uma camada de inteligência capaz de transformar informações dispersas e isoladas em compreensão útil e contextualizada. A experiência deve ajudar o visitante a perceber como informações podem se relacionar, o que se repete, o que está mudando, o que começa a ganhar força e como uma determinada leitura foi construída. Não produza UI final e não trate a saída como produto operacional pronto.

FONTES
Utilize exclusivamente os documentos fornecidos neste pacote para decisões sobre Guivos Intelligence. Não reconstrua decisões com conhecimento externo. Quando uma informação não estiver definida, sinalize a lacuna ou formule uma hipótese explicitamente identificada.

TESE CENTRAL
Informação não é o mesmo que compreensão. Guivos Intelligence existe para ajudar a ampliar o que pode ser percebido quando informações, contexto e relações são considerados em conjunto.

INVARIANTES
- preserve “compreensão útil e contextualizada” como unidade de valor;
- preserve INFORMAÇÃO ≠ COMPREENSÃO;
- preserve COMPREENDER ≠ DECIDIR;
- preserve a função dos onze movimentos sem exigir onze seções equivalentes;
- preserve a diferença entre M03 e M10;
- preserve a diferença entre M04 e M05;
- explicabilidade e confiança devem possuir presença real na experiência;
- a decisão permanece humana ou com a autoridade legítima;
- relações não devem ser apresentadas automaticamente como causalidade;
- sinais, tendências e movimentos não devem ser apresentados como futuro conhecido;
- “perceber antes” significa tornar mudanças e sinais mais visíveis, não prever com certeza;
- IA, Graph, Neo4j, GraphRAG, LLMs, dashboards ou analytics não podem se tornar a identidade do produto;
- preserve a distinção Pessoa/Journey e Business/população;
- não exponha contexto individual protegido a organizações;
- tecnologia deve permanecer subordinada ao benefício e à compreensão.

COPY CONGELADA
Preserve literalmente os textos classificados nas fontes como congelados, incluindo pergunta-mãe, abertura, autonomia, horizonte e CTAs. Copy de apoio não congelada pode ser tratada apenas como hipótese de Content Design e deve ser identificada como tal.

DIREÇÃO DE EXPERIÊNCIA
Trabalhe a ideia de “clareza emergindo da complexidade”. Explore transformações como dispersão → relação, ruído → padrão, número → contexto, estado → mudança, sinal → movimento perceptível, conclusão → explicação e informação → compreensão.

MATERIALIZAÇÃO ANALÍTICA
Você pode utilizar indicadores, comparações, variações, séries temporais, distribuições, relações, mini gráficos, cards analíticos e redes conceituais. Cada visualização precisa ajudar a explicar uma leitura, mudança, relação ou resultado. Não use dashboards complexos apenas como decoração tecnológica.

CONFIANÇA E EXPLICABILIDADE
Explore maneiras de mostrar: o que foi observado, quais informações foram consideradas, como podem estar relacionadas, o que é interpretação, quais limites existem e o que uma leitura não significa.

HORIZONTE
Demonstre como sinais isolados podem se tornar recorrências, mudanças perceptíveis ou movimentos que começam a ganhar forma. Não comunique previsão determinística, certeza futura ou resultado garantido.

PESSOA E BUSINESS
Preserve a assimetria de privacidade. No contexto da pessoa, Intelligence pode trabalhar com contexto autorizado para produzir compreensão individual relevante. No contexto empresarial, represente leitura protegida de população, tendências e movimentos agregados autorizados, e não Intelligence individual de funcionários.

LIBERDADE
Explore composição, grid, agrupamento dos movimentos, ritmo, densidade, tipografia provisória, visualizações, fotografia, abstrações, redes relacionais, motion conceitual, Header, CTAs e alternativas desktop/mobile.

NÃO INVENTE
Usuários, clientes, empresas, cases, depoimentos, métricas, resultados comprovados, precisão, ROI, redução de risco, produtividade, previsões, dados pessoais, scores, diagnósticos, preços, planos, integrações, APIs, Neo4j, GraphRAG, Power BI, modelos de IA, infraestrutura ou qualquer disponibilidade operacional não confirmada. Quando necessário, utilize placeholders explicitamente identificados.

ANTI-TEMPLATE
Não construa uma Home genérica de IA, analytics, BI, SaaS, HR tech ou data platform. Não copie OpenAI, Palantir, Tableau, Power BI, Snowflake, Databricks, Neo4j ou qualquer benchmark como template. Referências externas podem inspirar soluções de Design, mas não redefinir a identidade ou arquitetura do Guivos Intelligence.

ENTREGUE
1. mapa resumido da página;
2. wireframe low-fi desktop;
3. wireframe low-fi mobile;
4. explicação de como os onze movimentos foram agrupados e materializados;
5. demonstração visual da passagem de informação isolada para compreensão contextualizada;
6. pelo menos uma demonstração de conexão/relação;
7. pelo menos uma demonstração de padrão ou recorrência;
8. pelo menos uma demonstração de mudança temporal ou movimento;
9. uma solução perceptível para confiança/explicabilidade;
10. uma solução perceptível para autonomia humana;
11. uma solução para horizonte ampliado sem previsão determinística;
12. representação coerente das frentes Pessoa e Business;
13. lista das hipóteses introduzidas;
14. lista das lacunas encontradas;
15. autoauditoria dos invariantes.

Para cada macrobloco, indique:
- qual movimento ou movimentos foram materializados;
- qual resultado ficou visível;
- qual liberdade de Design foi utilizada;
- qual guardrail foi preservado.

STATUS DA SAÍDA
EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO. Nenhum dado, capacidade, tecnologia, integração, claim ou resultado apresentado como placeholder pode ser interpretado como vigente. Nenhuma direção de Design se torna canônica sem validação humana contra o GKR.
```

## 18. Autoauditoria

Antes de promover uma direção a `CANDIDATO`, confirmar:

- a primeira impressão é compreensão, e não software/IA/dashboard?;
- informação isolada ≠ compreensão ficou perceptível?;
- M03 e M10 cumprem papéis diferentes?;
- M04 mostra resultados e M05 demonstra esses resultados?;
- os onze movimentos sobreviveram, mesmo que agrupados?;
- há demonstrações concretas de relação, padrão e mudança?;
- visualizações ajudam a compreender em vez de apenas decorar?;
- confiança/explicabilidade possui presença real?;
- o visitante consegue entender de onde uma leitura pode ter vindo?;
- a decisão permanece com a pessoa ou autoridade legítima?;
- relações são mostradas sem implicar causalidade?;
- horizonte ampliado não virou previsão?;
- Pessoa e Business permanecem semanticamente distintos?;
- privacidade individual permanece protegida?;
- IA permanece capacidade subordinada?;
- Graph permanece capacidade subordinada?;
- nenhuma tecnologia virou protagonista?;
- nenhum dado conceitual parece dado real?;
- nenhum claim ou resultado foi inventado?;
- desktop e mobile preservam a progressão narrativa?;
- a página parece Guivos sem parecer cópia das outras Homes?;
- hipóteses estão claramente rotuladas?;
- acessibilidade e performance permanecem plausíveis?

## 19. Critério principal de validação humana

A exploração só pode avançar se uma pessoa sem conhecimento prévio conseguir compreender algo próximo de:

> **Guivos Intelligence ajuda a juntar informações que estavam separadas, perceber como elas se relacionam, entender o que está se repetindo ou mudando e compreender melhor antes de decidir.**

A direção deve ser rejeitada se a impressão principal for:

- “parece uma IA muito avançada”;
- “parece um dashboard”;
- “parece um sistema de previsão”;
- “parece um software de dados”;
- “parece um grafo”.

## 20. Próxima etapa

Após a integração deste GENINPUT, a próxima etapa continua separada e governada.

Este documento, por si só, **não executa Design**.

Antes de qualquer primeira exploração externa, deve ser confirmado o pacote de entrega vigente para Design e o checkpoint canônico que será fornecido à ferramenta.

Nenhuma exploração pode ser promovida a direção canônica sem validação humana contra o GKR.

## 21. Síntese

> **A ferramenta pode explorar como compreensão, relações, mudanças e explicabilidade ganham forma visual; não pode inventar verdade, causalidade, previsão, maturidade, tecnologia ou autoridade de decisão.**
