---
id: GKR-GLOSSARY-001
title: Glossário Canônico da Guivos
status: consolidated
version: 1.7.0
owner: Guivos
last_updated: 2026-07-04
---

# Glossário Canônico da Guivos

Este glossário estabelece o uso oficial dos principais termos da arquitetura da Guivos.

Quando documentos antigos utilizarem nomenclatura diferente, prevalece a definição registrada aqui, salvo decisão posterior formalmente consolidada no GKR.

## Participante

Entidade capaz de atuar em uma jornada de evolução ou contribuir para a jornada de outros participantes.

Categorias arquiteturais reconhecidas:

- Pessoa;
- Organização;
- Coletivo.

**Uso oficial:** termo central da arquitetura.

**Não confundir com:** usuário, cliente, membro ou perfil.

## Pessoa

Participante individual, autônomo e permanente no ecossistema.

## Organização

Participante institucional que reúne pessoas, recursos, conhecimento e capacidades em torno de uma missão ou objetivo comum.

## Coletivo

Participante formado pela associação de Pessoas e, quando aplicável, Organizações, em torno de um propósito compartilhado.

Pode adotar denominações como movimento, grupo, clube, núcleo, rede, comunidade ou equipe.

## Comunidade

Não é categoria arquitetural independente. Pode ser utilizada como denominação contextual de um Coletivo.

O uso anterior de “Comunidade Guivos” como nome amplo de produto foi substituído por **Guivos Journey**.

## Guivos Journey

Camada principal de experiência do Ecossistema Guivos, responsável por orquestrar a experiência unificada do participante, apoiar sua jornada contínua e apresentar recomendações, oportunidades, objetivos, conteúdos e interações de forma contextual.

Na GLPA, Guivos Journey pertence à **Experience Layer**.

## PAS — Product Architecture Specification

Formato de especificação de produto utilizado para descrever visão, filosofia, responsabilidades, arquitetura funcional, fluxos, inteligência, integrações, modelo econômico, KPIs e roadmap de um componente da Guivos.

## PAS-001 — Guivos Journey

Primeira Product Architecture Specification da Guivos, dedicada a especificar o Guivos Journey como camada principal de experiência do ecossistema.

## GLPA — Guivos Layered Product Architecture

Arquitetura funcional que organiza os componentes da Guivos por camadas de responsabilidade: Experience Layer, Intelligence Layer, Service Layer e Platform Layer.

A GLPA complementa a Arquitetura de Produtos ao diferenciar a natureza funcional dos componentes oficiais.

## Experience Layer

Camada responsável pela experiência unificada do participante.

Na Guivos, a Experience Layer é representada pelo Guivos Journey.

## Intelligence Layer

Camada transversal responsável pela interpretação contextual, recomendações, personalização, inteligência aplicada e aprendizagem do ecossistema.

Na Guivos, a Intelligence Layer é representada pelo Guivos Intelligence.

## Service Layer

Camada responsável por capacidades especializadas do ecossistema.

Na Guivos, inclui Guivos Business, Guivos Mall, Guivos Travel, Guivos Media e Guivos Ads.

## Platform Layer

Camada de capacidades técnicas comuns que sustentam os demais componentes, incluindo APIs, Graph, Auth, Billing, Search, Notifications, Security, dados e infraestrutura.

## Guivos Mall

Produto responsável pela oferta e comercialização de produtos, serviços, gift cards, assinaturas e outros ativos digitais ou físicos do Ecossistema Guivos.

Funciona como o shopping do ecossistema, com curadoria e aderência às jornadas.

Substitui `Guivos Marketplace` como nome oficial do produto comercial.

## Guivos Travel

Produto responsável por viagens e experiências relacionadas a deslocamento, destinos e turismo.

Na GLPA, pertence à Service Layer.

## Guivos Business

Produto responsável pelas soluções da Guivos para empresas e demais organizações.

Na GLPA, pertence à Service Layer.

## Guivos Media

Produto responsável pela produção, organização e distribuição de conteúdo editorial e institucional da Guivos.

Substitui “Guivos Podcast” como nome de produto.

Na GLPA, pertence à Service Layer.

## Guivos Intelligence

Componente responsável por entregar a **Inteligência do Ecossistema Guivos**.

Na GLPA, Guivos Intelligence pertence à **Intelligence Layer** e atua de forma transversal para Journey, Mall, Business, Travel, Media e Ads.

Substitui “Guivos Insights” como nome de produto.

## Inteligência do Ecossistema Guivos

Expressão conceitual e pública para a inteligência que interpreta dados, conhecimento, contexto, conexões, jornadas, experiências e evidências de todo o ecossistema.

Não é apenas um chatbot, modelo de linguagem ou mecanismo de recomendação isolado.

## Grafo Global da Guivos

Modelo conceitual que organiza participantes, organizações, coletivos, objetivos, Momentos Atuais, Próximos Passos, oportunidades, experiências, conhecimentos, relacionamentos e evidências por meio de conexões contextuais e evolutivas.

O grafo representa um patrimônio cumulativo do ecossistema. Sua ontologia formal, modelo lógico e implementação técnica ainda dependem de detalhamento e validação.

## Guivos Ads

Produto responsável por publicidade, mídia patrocinada e soluções para anunciantes dentro do Ecossistema Guivos.

Na GLPA, pertence à Service Layer.

## Guivos Economic Model

Domínio planejado do GKR responsável por descrever princípios econômicos, fontes de receita, planos, incentivos, sustentabilidade financeira, limites de monetização e relações entre propósito, impacto e geração de valor.

Seu princípio inicial estabelece que planos pagos podem acelerar, ampliar e personalizar jornadas, mas não devem bloquear a evolução de participantes gratuitos.

## Enterprise Design & Business Specification

Frente de especificação executável da Guivos dedicada a transformar arquitetura institucional em decisões de produto, operação, modelo econômico, modelo comercial e Go-to-Market.

## Guivos Knowledge Architecture

Arquitetura responsável por governar como o conhecimento institucional da Guivos é descoberto, estruturado, validado, consolidado, promovido à Canon, revisado e evoluído.

A GKA não determina o que é verdadeiro. Ela governa o processo de produção, validação e evolução do conhecimento institucional.

## Guivos Evolution Framework

Estrutura que registra as grandes eras de maturidade institucional da Guivos e explica como a organização evolui ao longo de sua história.

## GE-1 — Foundation & Architecture

Primeira era de evolução institucional da Guivos, dedicada à estruturação das fundações, arquiteturas, produtos, guia público e Canon inicial.

## GE-2 — Knowledge

Segunda era de evolução institucional da Guivos, dedicada à produção sistemática de conhecimento institucional por meio da Guivos Knowledge Architecture.

## Institutional Writing

Modo de redação institucional em que um ativo arquitetural é escrito para consolidar conhecimento já suficientemente maduro, sem promover novas hipóteses automaticamente à Canon.

## Institutional Consolidation Mode

Modo de trabalho da GE-2 em que o foco deixa de ser descobrir novos conceitos e passa a ser institucionalizar, revisar e consolidar conhecimento já suficientemente maduro.

## Capítulo Institucional

Unidade documental completa de um ativo arquitetural, desenvolvida por planejamento, redação completa, revisão em cinco níveis, aprovação e atualização do GKR.

## Revisão em Cinco Níveis

Critério de revisão aplicado a capítulos institucionais, composto por Precisão Conceitual, Precisão Arquitetural, Precisão Editorial, Precisão Institucional e Precisão Sistêmica.

## Regra da Pergunta Única

Diretriz editorial segundo a qual cada seção de um documento arquitetural deve responder uma única pergunta arquitetural que nenhuma outra seção responde.

## Competência Institucional

Autoridade institucional atribuída a uma arquitetura sobre determinado fenômeno, ativo, critério ou mecanismo.

Competência não é execução operacional.

## Responsabilidade Institucional

Dever permanente assumido por uma arquitetura perante a organização.

Responsabilidade expressa pelo que a arquitetura responde, não apenas pelo que ela contém.

## Diretriz Institucional

Interpretação operacional de um princípio permanente, utilizada para orientar decisões institucionais sem descer ao nível de processo ou implementação.

## Conhecimento Definicional

Categoria de conhecimento institucional em investigação, relacionada à definição precisa de termos, conceitos e distinções arquiteturais.

Permanece vinculada à hipótese `H-GKM-001` até validação metodológica futura.

## Conhecimento Normativo

Categoria de conhecimento institucional em investigação, relacionada a princípios, diretrizes, critérios e normas institucionais que orientam decisões permanentes.

Permanece vinculada à hipótese `H-GKM-001` até validação metodológica futura.

## Conhecimento Explicativo

Categoria de conhecimento institucional em investigação, relacionada a modelos que buscam explicar fenômenos arquiteturais ou institucionais.

Modelos explicativos exigem demonstração e validação mais rigorosas que definições conceituais isoladas.

## Governar

Exercer autoridade institucional sobre princípios, critérios, limites e evolução de determinado domínio arquitetural.

## Gerenciar

Conduzir atividades operacionais, recursos, rotinas ou fluxos dentro de processos definidos.

## Executar

Realizar ações concretas, tarefas ou implementações específicas.

## Princípio da Responsabilidade Arquitetural

Diretriz segundo a qual toda arquitetura de primeira classe deve possuir uma responsabilidade institucional única, permanente e claramente distinguível das demais arquiteturas.

## Princípio da Autocoerência Arquitetural

Diretriz segundo a qual toda arquitetura da Guivos deve submeter sua própria evolução aos princípios, métodos e critérios que estabelece para os demais ativos arquiteturais.

## Princípio da Continuidade Evolutiva

Hipótese transversal segundo a qual entidades permanentes do Ecossistema Guivos tendem a evoluir preservando sua identidade enquanto ampliam progressivamente sua capacidade de cumprir seu propósito.

Permanece como hipótese `H-GEF-001` até validação futura.

## Modelo Fundamental da Aprendizagem Institucional

Hipótese arquitetural de alta maturidade segundo a qual a transformação de experiências em patrimônio intelectual pode representar o fenômeno central governado pela Guivos Knowledge Architecture.

Permanece fora da Canon até validação sistêmica durante o desenvolvimento do GKA-000.

## Modelo Explicativo

Representação estruturada que busca explicar um fenômeno central da arquitetura.

Modelos explicativos exigem validação mais rigorosa que definições conceituais isoladas.

## Canon

Conjunto oficial de conhecimentos institucionais atualmente mais confiáveis para fundamentar decisões permanentes da Guivos, derivados de evidências rastreáveis e aprovados por processos formais de governança.

A Canon é estável, mas revisável quando evidências consistentes demonstrarem que deixou de representar adequadamente a realidade observada.

## Identidade

Representa quem é o participante dentro do ecossistema.

A identidade permanece estável enquanto papéis, capacidades, relacionamentos e contextos podem mudar.

## Papel

Conjunto temporário e contextual de responsabilidades exercidas por um participante.

## Capacidade

Competência arquitetural que permite a um participante produzir valor no ecossistema.

Capacidades não são permissões técnicas nem funcionalidades de interface.

## Jornada

Sequência contínua de estados, decisões, experiências e resultados vividos por um participante ao longo do tempo.

A Guivos apoia a jornada; não a controla.

## Momento Atual

Representa o estado presente do participante e o contexto relevante para compreender sua realidade.

## Objetivo

Resultado ou direção que o participante deseja alcançar.

## Próximo Passo

Decisão ou hipótese de evolução mais relevante para o Momento Atual e os Objetivos do participante.

O Próximo Passo não é uma Oportunidade.

## Oportunidade

Iniciativa ou mecanismo estruturado capaz de apoiar a realização de um Próximo Passo por meio de uma Experiência.

## Experiência

Materialização da participação de um ou mais participantes em uma Oportunidade.

## Evidência de Evolução

Sinal, resultado ou mudança que permite compreender como uma Experiência alterou a jornada de um participante.

## Relacionamento

Vínculo reconhecido entre dois ou mais participantes, formado ou fortalecido por interações, experiências ou objetivos compartilhados.

## Conhecimento do Ecossistema

Conjunto organizado de padrões, aprendizados e evidências produzidos pelas experiências vividas pelos participantes.

Dados são registros. Conhecimento é compreensão. Inteligência é interpretação aplicada.

## Inteligência Artificial

Conjunto de tecnologias que pode apoiar interpretação, recomendação, análise e automação.

Na Guivos, a inteligência artificial é um meio técnico dentro da Inteligência do Ecossistema Guivos e não substitui a autonomia do participante.

## Discovery Mode

Modo de investigação arquitetural em que evidências, observações, regularidades e hipóteses podem ser examinadas sem promoção automática à Canon.

## Canon Mode

Modo de preservação e publicação em que apenas conhecimento consolidado, rastreável, validado e governado pode alterar a Canon.

## Usuário

Termo técnico aceitável em contextos de software, autenticação, sessão ou interface.

Não deve substituir Participante na arquitetura conceitual.

## Cliente

Termo comercial utilizado quando uma Pessoa ou Organização mantém relação de compra, contratação ou assinatura com a Guivos.

Cliente é uma relação comercial, não uma categoria de participante.

## GEA

Guivos Enterprise Architecture. Conjunto integrado das arquiteturas oficiais da Guivos.

## GKA

Guivos Knowledge Architecture.

## GKR

Guivos Knowledge Repository. Sistema oficial de descoberta, consolidação, governança e evolução do conhecimento da Guivos.

## GEB

Guivos Ecosystem Blueprint. Artefato do GKR que especifica a arquitetura conceitual do ecossistema Guivos.