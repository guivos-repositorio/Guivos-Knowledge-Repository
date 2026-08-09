---
id: GPA-006
title: Guivos Intelligence
status: consolidated
version: 1.5.0
owner: Guivos
last_updated: 2026-08-08
related_models:
  - GAI-001
  - GAI-002
related:
  - ADR-007
  - GEA-GRAPH-REFERENCE-001
  - PAS-001-DOMAIN-MODEL-001
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
- classificação explicável de **Domínios de Evolução candidatos** conforme `PAS-001-DOMAIN-MODEL-001`;
- identificação de relações multidomínio sem impor prioridade humana;
- conhecimento estratégico do ecossistema;
- integração de estudos, pesquisas, livros, normas e fontes institucionais confiáveis;
- aprendizado com experiências e evidências produzidas pelo ecossistema;
- aprendizado contextual com objetivos, mudanças e movimentações autorizadas;
- explicabilidade e registro de incertezas.

## Domínios de Evolução do Journey

`PAS-001-DOMAIN-MODEL-001` estabelece o vocabulário canônico dos nove Domínios de Evolução usados pelo Guivos Journey:

1. Saúde e Bem-estar;
2. Trabalho, Carreira e Estudos;
3. Vida Financeira;
4. Empreendedorismo e Projetos;
5. Relacionamentos e Vida Social;
6. Espiritualidade, Propósito e Valores;
7. Viagens, Lazer, Cultura e Novas Experiências;
8. Causas, Voluntariado e Contribuição;
9. Organização e Equilíbrio da Vida.

Guivos Intelligence poderá sugerir domínios, subáreas e relações como **candidatos explicáveis** quando houver finalidade e base adequadas.

Deverão permanecer distintos:

```text
domínio candidato ≠ domínio confirmado
domínio ≠ identidade
domínio ≠ diagnóstico
domínio ≠ prioridade humana
domínio ≠ score
domínio ≠ prova de evolução
```

A declaração direta do participante, quando aplicável e legítima, deverá prevalecer sobre inferência incompatível.

A Intelligence deverá preservar a possibilidade de:

- múltiplos domínios simultâneos;
- estado “Ainda estou descobrindo”;
- área ainda não mapeada;
- contestação;
- retirada;
- incerteza;
- ausência legítima de classificação.

## Modelos orientadores

- `GAI-001 — Guivos Artificial Intelligence Knowledge Model` define o fluxo de dados, informação, conhecimento, contexto e recomendação;
- `GAI-002 — Manifesto da Inteligência do Ecossistema Guivos` define propósito, princípios, Grafo Global, autonomia, limites e patrimônio cumulativo;
- `PAS-001-DOMAIN-MODEL-001` define o vocabulário de Domínios de Evolução do Journey e os limites para classificação e uso desse contexto.

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

Os Domínios de Evolução constituem vocabulário semântico candidato a compor uma futura ontologia do grafo, mas a sua aprovação documental **não declara modelo físico de grafo implementado**.

## Relação com Graph Analytics

Graph Analytics pode apoiar análises estruturais do ecossistema quando houver finalidade e dados autorizados.

Resultados como centralidade, comunidades, similaridade ou previsão de relações são **medidas técnicas contextualizadas** e não podem ser convertidos automaticamente em valor humano, mérito, evolução, pertencimento, confiança ou verdade.

Da mesma forma, afinidade de uma Pessoa, Coletivo ou Organização com determinado Domínio de Evolução não poderá ser convertida automaticamente em ranking, perfil determinístico ou conclusão sobre identidade.

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

Analytics por Domínio de Evolução deverá respeitar agregação, finalidade e proteção, especialmente quando envolver saúde, espiritualidade, condição emocional, finanças, emprego, família, vulnerabilidade ou outras informações sensíveis.

## Limites

Guivos Intelligence não substitui os produtos que executam jornadas, transações, viagens, soluções empresariais, conteúdo editorial ou publicidade.

Também não deverá decidir o que uma pessoa deve querer, impor objetivos, substituir profissionais especializados, utilizar fontes como verdade automática, tratar inferências como certezas ou priorizar venda em prejuízo do participante.

No uso de Domínios de Evolução, não deverá:

- confirmar domínio por conta própria quando a autoridade exigir participante ou fonte qualificada;
- diagnosticar saúde ou condição emocional;
- medir fé ou proximidade de Deus;
- inferir propósito de vida como verdade;
- transformar Vida Financeira em score de sucesso ou solvência pessoal;
- transformar Relacionamentos em score de valor social;
- transformar Voluntariado em ranking moral;
- utilizar domínio sensível para publicidade comportamental;
- criar um score global de evolução.

A camada de grafo também não concede autoridade adicional sobre Pessoas, Coletivos, Organizações ou demais atores.

## Relações principais

- Guivos Journey, para compreensão de contexto, Domínios de Evolução, próximos passos e oportunidades;
- Guivos Business, para análises, indicadores e inteligência organizacional;
- Guivos Mall, para relevância, curadoria e organização de ofertas;
- Guivos Travel, para contexto e recomendação de experiências;
- Guivos Media, para organização e descoberta de conhecimento;
- Guivos Ads, para relevância, transparência e mensuração responsável, sem usar domínio sensível como autorização de targeting.

## Decisão de nomenclatura

`Guivos Intelligence` permanece como nome oficial do produto.

`Inteligência do Ecossistema Guivos` é a expressão conceitual e pública para a inteligência entregue por esse produto.

## Estado de maturidade

A responsabilidade superior do produto, o modelo conceitual de aprendizagem, o Grafo Global como modelo de conexões, os princípios do manifesto e a relação semântica com os Domínios de Evolução estão consolidados documentalmente.

Neo4j está em estado `reference_selected` como tecnologia primária de referência para grafo.

A taxonomia dos Domínios de Evolução está governada no `PAS-001-DOMAIN-MODEL-001`, mas classificação operacional por IA, ontologia formal completa, arquitetura física de dados, modelo de grafo físico, POC, infraestrutura, mecanismos técnicos de consentimento, atualização de conhecimento, auditoria algorítmica, Graph Analytics operacional, GraphRAG operacional, Power BI integrado e explicabilidade operacional ainda dependem de detalhamento, validação, autorização e implementação.
