---
id: GEA-GRAPH-REFERENCE-001
title: Arquitetura de Referência de Grafo e Inteligência
status: active
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-08
depends_on:
  - GEA-000
  - ADR-003
  - ADR-005
  - ADR-007
  - GPA-005
related:
  - GKR-STATE-001
  - GKR-RESYNCHRONIZATION-BASELINE-2026-08-08-001
normative: true
---

# Arquitetura de Referência de Grafo e Inteligência

## 1. Finalidade

Esta arquitetura posiciona a camada de grafo dentro da Guivos Enterprise Architecture e define como ela poderá apoiar Guivos Intelligence, Graph Analytics, GraphRAG e consumo analítico sem confundir tecnologia, produto, conhecimento, evidência e implementação.

É uma **Arquitetura de Referência**. Ela descreve a melhor forma conhecida de realizar determinadas capacidades no estado atual do conhecimento, mas não comprova infraestrutura, integração, dados ou produção.

## 2. Princípio central

```text
realidade e eventos autorizados
→ dados com proveniência
→ relações governadas
→ grafo
→ análise / recuperação
→ evidência e inteligência derivadas
→ consumo autorizado
→ decisão humana ou capacidade de produto
```

O grafo organiza relações. Ele não transforma automaticamente relações em verdade, causalidade, recomendação, mérito ou autoridade.

## 3. Posição na GEA

A propriedade conceitual permanece distribuída:

| Objeto | Arquitetura proprietária |
|---|---|
| significado de Pessoa, Coletivo, Organização, oportunidade e demais entidades | arquitetura de domínio aplicável |
| capacidades e proposta de valor de Guivos Intelligence | Product Architecture / Intelligence Layer |
| conhecimento, evidência, promoção e Canon | Guivos Knowledge Architecture |
| finalidade, permissão e proteção de dados | arquiteturas de governança, dados, privacidade e segurança aplicáveis |
| grafo lógico e padrões de inteligência | Guivos Intelligence Architecture / arquitetura responsável correspondente |
| tecnologia Neo4j | Technology and Engineering Architecture, governada por ADR-007 como referência |
| infraestrutura e deployment | Technology and Engineering Architecture / Enterprise Delivery |
| dashboards e BI | produto/capacidade consumidora, sem redefinir a fonte da verdade |

## 4. Arquitetura lógica

```text
[Fontes e Sistemas de Registro]
          |
          v
[Ingestão / Contratos / Proveniência]
          |
          +---------------------------+
          |                           |
          v                           v
[Persistência operacional]     [Camada analítica tabular]
          |                           |
          +------------+--------------+
                       |
                       v
              [Camada de Grafo]
              [Neo4j — referência]
                       |
          +------------+-------------+
          |            |             |
          v            v             v
 [Graph Queries] [Graph Analytics] [GraphRAG/Retrieval]
                       |             |
                       +------+------+
                              |
                              v
                    [Guivos Intelligence]
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
         Journey          Produtos        BI/Executivo
      autorizado        autorizados        agregado
```

O desenho é lógico. Não determina fornecedor de nuvem, topologia física ou pipeline implementado.

## 5. Neo4j — papel autorizado nesta referência

Por `ADR-007`, Neo4j é a tecnologia primária de referência para a camada de grafo.

Pode ser avaliado para:

- persistência de entidades e relações cuja representação em grafo seja justificável;
- travessias e consultas relacionais;
- knowledge graph/context graph;
- análises estruturais;
- projeções de grafo para algoritmos;
- recuperação híbrida de contexto para GraphRAG;
- geração de visões ou datasets derivados para consumidores autorizados.

Neo4j não é declarado como:

- banco único de toda a Guivos;
- substituto universal de banco relacional;
- data warehouse/lakehouse;
- fonte automática de verdade sobre a Pessoa;
- mecanismo de decisão autônoma;
- implantação já existente.

## 6. Modelo de grafo — contrato conceitual mínimo

Um futuro modelo físico deverá derivar das autoridades de domínio. Nesta referência, somente o contrato mínimo é autorizado.

### 6.1 Entidades

Nós podem representar objetos governados como, quando aplicável:

- Pessoas;
- Coletivos;
- Organizações;
- oportunidades e programas;
- produtos e capacidades;
- territórios e contextos permitidos;
- evidências e fontes;
- eventos ou estados relevantes;
- conceitos de conhecimento institucional.

Esta lista não autoriza materializar todos esses objetos no mesmo grafo nem armazenar dados pessoais indiscriminadamente.

### 6.2 Relações

Toda relação material deverá possuir, conforme aplicável:

- tipo semântico;
- origem/fonte;
- autoridade;
- finalidade;
- temporalidade/validade;
- grau de certeza ou natureza observada/inferida;
- versão;
- política de acesso;
- possibilidade de contestação/correção quando relacionada a pessoa ou entidade externa.

### 6.3 Separação observação × inferência

```text
fato/evento observado
≠ relação declarada
≠ relação calculada
≠ inferência de modelo
≠ hipótese
≠ recomendação
```

Nenhuma inferência deverá sobrescrever silenciosamente a evidência de origem.

## 7. Graph Analytics

Neo4j Graph Data Science é capacidade técnica de referência para análise de estruturas de grafo.

Casos candidatos incluem, somente após validação de finalidade:

- detecção de comunidades ou estruturas;
- caminhos e conectividade;
- similaridade estrutural;
- centralidades usadas como medida técnica contextualizada;
- previsão de relações em casos legítimos;
- análise de redes de ecossistema;
- suporte a pesquisa e intelligence agregada.

Proibições:

- centralidade ≠ importância humana;
- PageRank ou score semelhante ≠ valor, mérito ou evolução;
- comunidade algorítmica ≠ identidade social ou pertencimento real;
- previsão de link ≠ relação existente;
- correlação de grafo ≠ causalidade;
- score técnico não poderá comprar ou substituir relevância governada.

Resultados analíticos deverão registrar algoritmo, versão, parâmetros, dataset/projeção, data e finalidade quando materialmente relevantes.

## 8. GraphRAG

GraphRAG é padrão candidato para recuperar contexto e relações governadas antes da geração por modelo de linguagem.

Arquitetura de referência:

```text
pergunta/intenção autorizada
→ definição de escopo e finalidade
→ recuperação textual/vetorial/relacional aplicável
→ subgrafo/evidências permitidos
→ composição de contexto
→ modelo gerador
→ resposta com proveniência e limites
```

Regras:

1. GraphRAG não promove automaticamente conteúdo à Canon;
2. LLM não cria fato porque uma relação apareceu no grafo;
3. retrieval respeita autoridade, finalidade e permissão;
4. conteúdo protegido não entra no contexto de outra finalidade sem base apropriada;
5. resposta deverá distinguir evidência, inferência e síntese quando isso afetar decisão;
6. resposta gerada não deverá ser escrita de volta como verdade sem processo de validação;
7. embeddings e índices são derivados técnicos e possuem ciclo de vida próprio;
8. exclusão/correção da fonte deverá possuir estratégia de propagação aos derivados.

## 9. Guivos Intelligence

Guivos Intelligence é o consumidor/produtor governado de capacidades de inteligência e continua separado da tecnologia de grafo.

Pode consumir, quando autorizado:

- consultas relacionais;
- métricas estruturais;
- tendências agregadas;
- resultados de algoritmos;
- contexto recuperado por GraphRAG;
- dados provenientes de outras arquiteturas.

Pode produzir:

- insights explicáveis;
- evidências agregadas;
- sinais analíticos;
- recomendações no limite da autoridade do produto;
- datasets derivados autorizados.

Não poderá:

- substituir Journey como experiência da Pessoa;
- transformar analytics agregado em exposição de contexto individual;
- criar ranking humano universal;
- redefinir conceito de domínio;
- conceder acesso por interesse comercial.

## 10. Power BI e consumo executivo

Power BI é tratado nesta arquitetura como **camada consumidora de Business Intelligence**, não como fonte de verdade do grafo.

Padrão preferencial de referência:

```text
fontes governadas
→ transformação/serving analítico autorizado
→ modelo semântico/visão agregada
→ Power BI
```

Uma conexão direta Power BI ↔ Neo4j não é requisito arquitetural e não é declarada existente. A forma de integração deverá ser escolhida posteriormente segundo:

- suporte técnico vigente;
- segurança e autenticação;
- volume e latência;
- semântica de consulta;
- custo;
- necessidade de refresh;
- agregação e minimização;
- observabilidade;
- independência do fornecedor.

Dashboards executivos deverão preferir métricas agregadas e rastreáveis. Contexto individual protegido não deve ser disponibilizado apenas porque o BI consegue consultá-lo.

## 11. Coexistência com outras persistências

A arquitetura é poliglota por necessidade, não por moda.

| Necessidade | Classe de tecnologia possível |
|---|---|
| transação operacional | persistência transacional adequada |
| arquivos/objetos | object storage adequado |
| analytics tabular/histórico | warehouse/lakehouse ou camada analítica adequada |
| busca textual | mecanismo de busca/indexação adequado |
| embeddings | índice vetorial interno ou externo adequado |
| relações complexas e travessias | grafo / Neo4j como referência primária |

A seleção física de cada componente pertence à Technology and Engineering Architecture.

## 12. Segurança, privacidade e governança

P2 não autoriza dado real no grafo. Uma futura implantação deverá definir, no mínimo:

- classificação de dados;
- finalidade;
- base/autorização aplicável;
- minimização;
- segregação e isolamento;
- controle de acesso;
- autenticação e autorização;
- criptografia aplicável;
- gestão de segredos;
- trilha de auditoria;
- retenção;
- correção e exclusão;
- propagação para índices/embeddings/derivados;
- backup e restauração;
- recuperação de desastre;
- residência de dados;
- resposta a incidentes;
- observabilidade;
- revisão de dependências e supply chain.

## 13. Escala e desempenho

O objetivo de escala global da Guivos não autoriza números técnicos inventados.

Antes de escolher tier, cluster, memória ou capacidade, uma etapa de dimensionamento deverá registrar:

- entidades e relações esperadas;
- taxa de escrita;
- padrões de consulta;
- profundidade de travessia;
- concorrência;
- workload analítico;
- workload GraphRAG;
- tamanho de projeções GDS;
- necessidades de disponibilidade;
- objetivos de recuperação;
- regiões e residência;
- custo aceitável;
- crescimento e sazonalidade.

## 14. Estados de maturidade

A evolução técnica deve usar estados explícitos:

```text
reference_selected
→ poc_authorized
→ poc_validated
→ provisioned
→ integrated_nonproduction
→ production_candidate
→ production_approved
→ production
```

Nenhuma etapa pode ser inferida pela anterior.

### Estado em 2026-08-08

| Componente | Estado |
|---|---|
| Neo4j como referência | `reference_selected` |
| modelo lógico detalhado | `not_started` |
| modelo físico | `not_started` |
| POC | `not_evidenced` |
| Aura/Server/cluster | `not_selected` |
| Graph Data Science | `reference_capability` |
| GraphRAG | `reference_pattern` |
| integração com Guivos Intelligence | `not_implemented` |
| integração com Power BI | `not_implemented` |
| dados reais em grafo | `not_evidenced` |
| produção | `not_authorized` |

## 15. Gates para POC

Antes de uma POC deverão existir:

1. problema e hipótese claramente definidos;
2. dataset sintético ou legitimamente autorizado;
3. modelo lógico mínimo;
4. métricas de sucesso;
5. limites de custo;
6. critérios de segurança e privacidade;
7. comparação com alternativa simples quando aplicável;
8. plano de descarte/limpeza dos dados;
9. owner técnico;
10. decisão explícita autorizando a POC.

## 16. Gates para produção

Uma eventual produção exige, além de POC validada:

- arquitetura física aprovada;
- fornecedor/deployment e região aprovados;
- análise de custo/capacidade;
- autenticação/autorização;
- backup/restore testados;
- DR e objetivos de continuidade;
- observabilidade e alertas;
- performance/carga;
- privacidade e segurança especializadas;
- retenção/exclusão;
- runbook e ownership operacional;
- contrato/SLA quando aplicável;
- plano de migração e rollback;
- gate explícito de produção.

## 17. Referências técnicas externas

As referências abaixo descrevem capacidades atuais do fornecedor, não implementação Guivos:

- documentação geral: https://neo4j.com/docs/
- Graph Data Science: https://neo4j.com/docs/graph-data-science/current/
- GraphRAG for Python: https://neo4j.com/docs/neo4j-graphrag-python/current/

## 18. Decisões orientadas

Esta arquitetura orienta:

- posição de Neo4j na GEA;
- relação entre grafo e Guivos Intelligence;
- separação de Graph Analytics e GraphRAG;
- padrão de consumo analítico/Power BI;
- gates para POC e produção;
- linguagem de maturidade da arquitetura de grafo.

Não orienta:

- contratação de fornecedor;
- escolha de cloud/region/tier;
- desenho físico final;
- esquema Cypher final;
- SLA;
- orçamento;
- migração;
- implementação;
- produção.

## 19. Estado

`active_reference_architecture — Neo4j selected as primary graph reference; implementation not authorized`.
