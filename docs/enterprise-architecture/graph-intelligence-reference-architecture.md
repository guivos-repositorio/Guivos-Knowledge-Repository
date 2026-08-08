---
id: GEA-GRAPH-REFERENCE-001
title: Arquitetura de Referência de Grafo e Inteligência
status: active
version: 0.1.1
owner: Guivos Enterprise Architecture
last_updated: 2026-08-08
depends_on:
  - GEA-000
  - ADR-003
  - ADR-005
  - ADR-007
  - GPA-006
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

Pode ser avaliado para persistência e consulta de relações governadas, knowledge/context graph, travessias, análises estruturais, projeções para algoritmos, recuperação híbrida para GraphRAG e produção de visões derivadas para consumidores autorizados.

Neo4j não é declarado como banco único da Guivos, substituto universal de persistências operacionais/analíticas, fonte automática de verdade sobre a Pessoa, mecanismo autônomo de decisão ou implantação já existente.

## 6. Contrato conceitual mínimo do grafo

Um futuro modelo físico deverá derivar das autoridades de domínio.

Nós poderão representar, somente quando houver finalidade e autorização, objetos como Pessoas, Coletivos, Organizações, oportunidades, programas, produtos, capacidades, territórios, evidências, fontes, eventos, estados e conceitos.

Toda relação material deverá preservar, conforme aplicável:

- tipo semântico;
- fonte/origem;
- autoridade;
- finalidade;
- temporalidade/validade;
- natureza observada, declarada, calculada ou inferida;
- versão;
- política de acesso;
- possibilidade de correção/contestação.

Separação obrigatória:

```text
fato/evento observado
≠ relação declarada
≠ relação calculada
≠ inferência de modelo
≠ hipótese
≠ recomendação
```

Inferência não sobrescreve silenciosamente a evidência de origem.

## 7. Graph Analytics

Neo4j Graph Data Science é capacidade técnica de referência para análise de estruturas de grafo.

Casos candidatos, sujeitos a finalidade, incluem comunidades/estruturas, caminhos, conectividade, similaridade estrutural, centralidades, previsão legítima de relações e análise de redes do ecossistema.

Guardrails:

- centralidade ≠ importância humana;
- score ≠ valor, mérito ou evolução;
- comunidade algorítmica ≠ identidade ou pertencimento real;
- previsão de link ≠ relação existente;
- correlação ≠ causalidade;
- resultado técnico não compra relevância funcional.

Quando materialmente relevante, o resultado deverá registrar algoritmo, versão, parâmetros, dataset/projeção, data, finalidade e proveniência.

## 8. GraphRAG

GraphRAG é padrão candidato para recuperar contexto e relações governadas antes da geração por modelo de linguagem.

```text
intenção autorizada
→ escopo/finalidade
→ recuperação textual, vetorial e/ou relacional
→ subgrafo/evidências permitidos
→ composição de contexto
→ modelo gerador
→ resposta com proveniência e limites
```

Regras:

1. GraphRAG não promove automaticamente conteúdo à Canon;
2. LLM não cria fato porque uma relação existe no grafo;
3. retrieval respeita autoridade, finalidade e permissão;
4. conteúdo protegido não muda de finalidade por conveniência técnica;
5. fato, inferência e síntese permanecem distinguíveis;
6. resposta gerada não volta ao grafo como verdade sem validação;
7. embeddings e índices possuem ciclo de vida próprio;
8. correção/exclusão da fonte exige estratégia para derivados.

## 9. Guivos Intelligence

Guivos Intelligence continua sendo Produto Especializado e Intelligence Layer; Neo4j é tecnologia de referência e não substitui o produto.

Intelligence poderá consumir consultas relacionais, métricas estruturais, tendências agregadas, resultados de algoritmos e contexto GraphRAG quando autorizado. Poderá produzir insights explicáveis, evidências agregadas, sinais analíticos, recomendações no limite de sua autoridade e datasets derivados autorizados.

Não poderá substituir Journey, transformar analytics agregado em exposição individual, criar ranking humano universal, redefinir domínio ou conceder acesso por interesse comercial.

## 10. Power BI e consumo executivo

Power BI é uma **camada consumidora de Business Intelligence**, não fonte de verdade do grafo.

Padrão preferencial:

```text
fontes governadas
→ transformação/serving analítico autorizado
→ modelo semântico ou visão agregada
→ Power BI
```

Conexão direta Power BI ↔ Neo4j não é requisito e não é declarada existente. A futura integração deverá avaliar suporte técnico vigente, autenticação, volume, latência, semântica, refresh, custo, agregação, minimização, observabilidade e independência do fornecedor.

Dashboards executivos deverão preferir métricas agregadas, rastreáveis e adequadas à finalidade.

## 11. Persistência poliglota

A escolha de Neo4j não elimina outras classes de persistência.

| Necessidade | Classe possível |
|---|---|
| transação operacional | persistência transacional adequada |
| arquivos/objetos | object storage adequado |
| analytics tabular/histórico | warehouse/lakehouse ou camada analítica adequada |
| busca textual | mecanismo de busca/indexação adequado |
| embeddings | índice vetorial interno ou externo adequado |
| relações complexas/travessias | grafo / Neo4j como referência primária |

A seleção física de componentes pertence à Technology and Engineering Architecture.

## 12. Segurança, privacidade e governança

P2 não autoriza dado real no grafo. Uma implantação futura deverá definir classificação, finalidade, base/autorização, minimização, segregação, acesso, autenticação, criptografia aplicável, segredos, auditoria, retenção, correção/exclusão, propagação para derivados, backup/restore, DR, residência de dados, incidentes, observabilidade e supply chain.

## 13. Escala e dimensionamento

A ambição de escala global não autoriza números técnicos inventados.

Antes da escolha de tier ou topologia deverão ser conhecidos, no mínimo: entidades/relações esperadas, taxa de escrita, padrões de consulta, travessias, concorrência, workloads Graph Analytics/GraphRAG, tamanho de projeções, disponibilidade, recuperação, regiões/residência, custo aceitável, crescimento e sazonalidade.

## 14. Estados de maturidade

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

Nenhuma etapa é inferida da anterior.

| Componente | Estado em 2026-08-08 |
|---|---|
| Neo4j | `reference_selected` |
| modelo lógico detalhado | `not_started` |
| modelo físico | `not_started` |
| POC | `not_evidenced` |
| Aura/Server/cluster | `not_selected` |
| Graph Data Science | `reference_capability` |
| GraphRAG | `reference_pattern` |
| integração Guivos Intelligence | `not_implemented` |
| integração Power BI | `not_implemented` |
| dados reais no grafo | `not_evidenced` |
| produção | `not_authorized` |

## 15. Gates para POC e produção

Uma POC exige problema/hipótese, dataset sintético ou legitimamente autorizado, modelo mínimo, métricas de sucesso, limite de custo, critérios de segurança/privacidade, comparação adequada, plano de descarte, owner e autorização explícita.

Produção exige, adicionalmente, arquitetura física, deployment/região, custo/capacidade, autenticação/autorização, backup/restore testados, DR, observabilidade, performance, revisão especializada de segurança/privacidade, retenção/exclusão, runbook/ownership, SLA quando aplicável, migração/rollback e gate explícito de produção.

## 16. Referências técnicas externas

- https://neo4j.com/docs/
- https://neo4j.com/docs/graph-data-science/current/
- https://neo4j.com/docs/neo4j-graphrag-python/current/

Elas descrevem capacidades do fornecedor, não implementação Guivos.

## 17. Limites

Esta arquitetura não autoriza contratação, cloud/region/tier, esquema físico final, SLA, orçamento, migração, POC, dados reais, integração, implementação ou produção.

## 18. Estado

`active_reference_architecture — Neo4j selected as primary graph reference; implementation not authorized`.
