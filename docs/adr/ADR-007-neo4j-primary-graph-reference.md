---
id: ADR-007
title: Neo4j como Tecnologia Primária de Referência para Grafo
status: approved
date: 2026-08-08
owner: Guivos
supersedes: null
related:
  - GEA-000
  - GPA-005
  - ADR-003
  - ADR-005
  - GKR-RESYNCHRONIZATION-BASELINE-2026-08-08-001
---

# ADR-007 — Neo4j como Tecnologia Primária de Referência para Grafo

## Contexto

A Guivos concebe dados, contexto, conhecimento e relações como ativos que precisam preservar significado, proveniência, autoridade e conexões entre Pessoas, Coletivos, Organizações, oportunidades, produtos, evidências e demais objetos governados.

Nas discussões arquiteturais anteriores, Neo4j e Amazon Neptune foram comparados como alternativas para a camada de grafo. A decisão validada foi seguir com **Neo4j** como referência primária, sem transformar essa escolha em afirmação de implantação.

A decisão é compatível com a arquitetura atual porque:

- a Product Architecture reconhece Guivos Intelligence como Intelligence Layer;
- a GEA separa conceitos permanentes de tecnologia de referência e implementação;
- a Guivos precisa suportar análise estrutural de relações sem reduzir o conhecimento a tabelas ou métricas isoladas;
- Graph Analytics e recuperação fundamentada em relações são capacidades candidatas coerentes com a evolução de Intelligence;
- o repositório exige independência tecnológica: a validade conceitual da Guivos não pode depender de um fornecedor específico.

## Decisão

A Guivos adota **Neo4j como tecnologia primária de referência para a camada de grafo** da arquitetura empresarial.

A decisão significa:

```text
Neo4j = referência tecnológica escolhida para grafo
```

Ela não significa:

```text
Neo4j escolhido
≠ instância criada
≠ Aura contratada
≠ cluster provisionado
≠ dados migrados
≠ integração implementada
≠ GraphRAG implementado
≠ GDS em produção
≠ Power BI conectado
≠ produção autorizada
```

## Escopo da referência

Neo4j poderá ser avaliado, em atos posteriores, para:

- persistência e consulta de relações governadas;
- knowledge graph e context graph;
- graph analytics;
- algoritmos e machine learning sobre estruturas de grafo por meio de capacidades como Neo4j Graph Data Science;
- recuperação de contexto baseada em relações para fluxos GraphRAG;
- suporte a Guivos Intelligence e capacidades analíticas autorizadas;
- produção de datasets ou visões agregadas para camadas analíticas externas.

Nenhum desses usos é declarado implementado por esta ADR.

## Relação com Guivos Intelligence

Neo4j é uma tecnologia candidata de realização da camada de grafo. **Guivos Intelligence continua sendo o Produto Especializado/camada de inteligência e não é substituído pelo banco de grafo.**

```text
Guivos Intelligence
→ governa capacidade e proposta de valor de inteligência

Neo4j
→ tecnologia de referência possível para persistência, consulta e análise relacional
```

Dados, modelos, políticas, proveniência, autorização e resultados continuam pertencendo às arquiteturas responsáveis; a tecnologia não cria autoridade própria sobre eles.

## Alternativas

### Amazon Neptune

Permanece alternativa arquitetural possível para revisões futuras, especialmente se requisitos de plataforma, integração de nuvem, operação ou custo mudarem materialmente.

Não é a referência primária escolhida neste ciclo.

### Bancos relacionais, data warehouse e lakehouse

Permanecem adequados para objetos e workloads próprios. A escolha de Neo4j não implica substituir automaticamente persistência transacional, armazenamento analítico tabular, lakehouse, warehouse ou mecanismos de busca.

### Vector stores

Busca vetorial pode coexistir com grafo. A escolha de Neo4j não determina, por si só, que todo embedding ou índice vetorial deverá residir no grafo.

## Guardrails

1. conceito de grafo não depende de Neo4j;
2. dado pessoal ou sensível não entra no grafo apenas porque tecnicamente é possível;
3. toda relação material deverá possuir semântica, origem e autoridade compreensíveis;
4. inferência não deverá ser confundida com fato observado;
5. GraphRAG deverá recuperar evidência/contexto governado, não produzir autoridade nova;
6. Graph Data Science não poderá converter correlação ou centralidade em valor humano, mérito, ranking social ou verdade;
7. outputs analíticos para Business Intelligence deverão respeitar finalidade, agregação e autorização;
8. escolha de provedor gerenciado, região, tier, SLA, backup, DR, residência de dados e custo exige decisão posterior;
9. qualquer escrita de resultados algorítmicos de volta ao grafo exige política de proveniência e reversibilidade;
10. produção exige segurança, privacidade, observabilidade, capacidade, custo e operação validados.

## Estado de maturidade

| Estado | Situação em 2026-08-08 |
|---|---|
| necessidade de arquitetura de grafo | reconhecida |
| tecnologia primária de referência | **Neo4j selecionado** |
| modelo de grafo físico | não aprovado nesta ADR |
| POC | não comprovada |
| infraestrutura provisionada | não comprovada |
| dados reais carregados | não comprovados |
| GDS implementado | não comprovado |
| GraphRAG implementado | não comprovado |
| integração Power BI | não comprovada |
| produção | não autorizada |

## Referências técnicas externas

- Neo4j Documentation: https://neo4j.com/docs/
- Neo4j Graph Data Science: https://neo4j.com/docs/graph-data-science/current/
- Neo4j GraphRAG for Python: https://neo4j.com/docs/neo4j-graphrag-python/current/

As referências externas documentam capacidades do fornecedor e não comprovam uso pela Guivos.

## Consequências

A partir desta decisão:

- documentos de arquitetura podem usar Neo4j como referência primária de grafo;
- comparações futuras não devem voltar a tratar a tecnologia como “indefinida” sem nova evidência/ADR;
- implementação continua dependente da Technology and Engineering Architecture e de autorização própria;
- Guivos Intelligence e a arquitetura conceitual permanecem independentes do fornecedor;
- requisitos futuros podem provocar revisão formal desta decisão.

## Estado

**Decisão aprovada como Arquitetura de Referência. Implementação não autorizada.**
