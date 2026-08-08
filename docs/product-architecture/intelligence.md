---
id: GPA-006
title: Guivos Intelligence
status: consolidated
version: 1.4.0
owner: Guivos
last_updated: 2026-08-08
related_models:
  - GAI-001
  - GAI-002
related:
  - ADR-007
  - GEA-GRAPH-REFERENCE-001
---

# Guivos Intelligence

## Papel

Guivos Intelligence é o produto responsável por entregar a **Inteligência do Ecossistema Guivos**.

Essa inteligência transforma dados, contexto, evidências, conhecimento e conexões do ecossistema em recomendações, indicadores, tendências e análises úteis.

Seu papel inclui aprender continuamente com fontes confiáveis, conhecimento produzido pelo ecossistema, movimentação autorizada dos participantes e relações organizadas no Grafo Global da Guivos.

## Escopo principal

- inteligência artificial;
- Grafo Global da Guivos;
- analytics;
- indicadores;
- recomendações;
- modelos preditivos;
- benchmarks;
- tendências;
- interpretação do contexto dos participantes;
- conhecimento estratégico do ecossistema;
- integração de estudos, pesquisas, livros, normas e fontes institucionais confiáveis;
- aprendizado com experiências e evidências produzidas pelo ecossistema;
- aprendizado contextual com objetivos, mudanças e movimentações autorizadas;
- explicabilidade e registro de incertezas.

## Modelos orientadores

- `GAI-001 — Guivos Artificial Intelligence Knowledge Model` define o fluxo de dados, informação, conhecimento, contexto e recomendação;
- `GAI-002 — Manifesto da Inteligência do Ecossistema Guivos` define propósito, princípios, Grafo Global, autonomia, limites e patrimônio cumulativo.

## Grafo e tecnologia de referência

O **Grafo Global da Guivos** é conceito e capacidade do ecossistema; não é sinônimo de um fornecedor de banco de dados.

Por `ADR-007`, **Neo4j é a tecnologia primária de referência para a camada de grafo**, e `GEA-GRAPH-REFERENCE-001` governa a relação entre grafo, Graph Analytics, GraphRAG, Guivos Intelligence e consumo analítico.

A separação obrigatória é:

```text
Grafo Global da Guivos = modelo/capacidade de conexões governadas
Guivos Intelligence = produto e Intelligence Layer
Neo4j = tecnologia de referência para realização da camada de grafo
```

A escolha de Neo4j não declara instância, POC, cluster, Aura, dados carregados, Graph Data Science, GraphRAG, integração com Power BI ou produção implementados.

## Relação com Graph Analytics

Graph Analytics pode apoiar análises estruturais do ecossistema quando houver finalidade e dados autorizados.

Resultados como centralidade, comunidades, similaridade ou previsão de relações são **medidas técnicas contextualizadas** e não podem ser convertidos automaticamente em valor humano, mérito, evolução, pertencimento, confiança ou verdade.

## Relação com GraphRAG

GraphRAG é padrão candidato de recuperação de contexto e relações governadas antes de uma geração por modelo de linguagem.

Ele não substitui:

- a Guivos Knowledge Architecture;
- a Canon;
- validação de evidências;
- proveniência;
- permissões;
- distinção entre fato, inferência e síntese.

Uma resposta gerada não se torna conhecimento canônico apenas por ter usado o grafo como contexto.

## Consumo analítico e Power BI

Guivos Intelligence poderá disponibilizar, quando autorizado, métricas e visões agregadas para Business Intelligence e dashboards executivos.

Power BI é consumidor analítico possível, não fonte de verdade da Inteligência do Ecossistema. A forma técnica de integração permanece pendente de decisão posterior e deverá respeitar finalidade, minimização, autorização, segurança, volume, custo e rastreabilidade.

## Limites

Guivos Intelligence não substitui os produtos que executam jornadas, transações, viagens, soluções empresariais, conteúdo editorial ou publicidade.

Também não deverá decidir o que uma pessoa deve querer, impor objetivos, substituir profissionais especializados, utilizar fontes como verdade automática, tratar inferências como certezas ou priorizar venda em prejuízo do participante.

A camada de grafo também não concede autoridade adicional sobre Pessoas, Coletivos, Organizações ou demais atores.

## Relações principais

- Guivos Journey, para compreensão de contexto, próximos passos e oportunidades;
- Guivos Business, para análises, indicadores e inteligência organizacional;
- Guivos Mall, para relevância, curadoria e organização de ofertas;
- Guivos Travel, para contexto e recomendação de experiências;
- Guivos Media, para organização e descoberta de conhecimento;
- Guivos Ads, para relevância, transparência e mensuração responsável.

## Decisão de nomenclatura

`Guivos Intelligence` permanece como nome oficial do produto.

`Inteligência do Ecossistema Guivos` é a expressão conceitual e pública para a inteligência entregue por esse produto.

## Estado de maturidade

A responsabilidade superior do produto, o modelo conceitual de aprendizagem, o Grafo Global como modelo de conexões e os princípios do manifesto estão consolidados.

Neo4j está em estado `reference_selected` como tecnologia primária de referência para grafo.

Ontologia formal, arquitetura física de dados, modelo de grafo físico, POC, infraestrutura, mecanismos técnicos de consentimento, atualização de conhecimento, auditoria algorítmica, Graph Analytics operacional, GraphRAG operacional, Power BI integrado e explicabilidade operacional ainda dependem de detalhamento, validação, autorização e implementação.
