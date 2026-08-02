---
id: UXA-049
title: Validação Funcional e Reformulação dos Wireframes do Relatório Agregado do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-01
parent: UXA-048
depends_on:
  - UXA-005
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
  - UXA-042
  - UXA-043
  - UXA-044
  - UXA-045
  - UXA-046
  - UXA-047
  - UXA-048
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.51
normative: false
---

# Validação Funcional e Reformulação dos Wireframes do Relatório Agregado do Opportunity Boost

## 1. Finalidade

Este documento valida funcionalmente os quatro wireframes criados pela UXA-048 e registra as reformulações necessárias para que o anunciante interprete entrega, interação, atribuição candidata, autorrelato, ausência de dados e reconciliação sem converter agregados em rastreamento individual, causalidade, impacto humano ou direito financeiro confirmado.

A pergunta de validação é:

> **O anunciante distingue as quatro camadas do relatório, reconhece a proveniência e o estado de cada dado, compreende quando uma contagem não pode ser exibida, preserva origem orgânica e patrocinada sem dupla atribuição e consulta reconciliação sem misturar eventos heterogêneos ou inferir devolução, causalidade e impacto?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação**.

A validação não aprova política final de atribuição, limiar definitivo de agregação, antifraude, política jurídica, fiscal ou contábil, tratamento definitivo do saldo, exportação real, design visual final, acessibilidade técnica, protótipo, teste com usuários ou Engenharia de Produto.

## 3. Escopo examinado

Foram examinados:

1. visão geral agregada para computador;
2. atribuição candidata e autorrelato para computador;
3. visão geral agregada móvel;
4. reconciliação e ausência de dados móvel;
5. separação entre entrega, interação, atribuição candidata e autorrelato;
6. período, atualização e estado do dado;
7. proveniência instrumentada, calculada, declarada, indisponível e em revisão;
8. origem patrocinada, orgânica e indeterminada;
9. ausência de dado sem zero artificial;
10. privacidade, agregação e supressão de contagens;
11. eventos válidos, invalidados e em revisão;
12. orçamento utilizado, saldo candidato e reconciliação;
13. preservação de histórico e regra vigente;
14. linguagem, acessibilidade e consistência entre computador e aplicativo móvel.

## 4. Lacunas identificadas

### 4.1 Contagens pequenas sem proteção de agregação explícita

Os wireframes declaravam ausência de identificação individual, porém exibiam divisões pequenas por origem e autorrelato sem demonstrar o gate de agregação.

Mesmo sem nomes, uma contagem pequena combinada com contexto conhecido poderá facilitar reidentificação ou produzir falsa precisão.

### 4.2 Proveniência pouco visível no resumo móvel

A visão móvel apresentava as quatro camadas, mas o tipo de dado — instrumentado, calculado ou declarado — não acompanhava cada bloco de forma suficientemente direta.

### 4.3 Atribuição apresentada como linhas semelhantes a eventos individuais

A tabela de atribuição utilizava linhas por evento e origem. Embora ilustrativa, a estrutura poderia ser interpretada como rastreamento de uma sequência individual.

Também faltava identificar de forma dominante a versão da regra candidata aplicada ao período consultado.

### 4.4 Reconciliação somando eventos heterogêneos

O estado móvel apresentava `eventos válidos`, `invalidados` e `em revisão` como um total único.

Somar impressões, cliques, salvamentos e outros eventos com significados diferentes cria um número sem unidade funcional clara.

### 4.5 Estado provisório e reconciliado insuficientemente separados

O relatório indicava dados provisórios, mas precisava mostrar que encerramento da campanha não torna automaticamente todos os dados reconciliados.

Também era necessário distinguir `em revisão`, `parcialmente reconciliado` e `reconciliado` sem usar o estado como promessa financeira.

### 4.6 Autorrelato ainda próximo de evidência independente

O conteúdo declarado era corretamente identificado, porém precisava informar de modo mais visível que:

- não foi verificado automaticamente pela Guivos;
- não será somado aos eventos instrumentados;
- poderá ter quantidade suprimida por agregação;
- não comprova causalidade ou impacto.

### 4.7 Regra de atribuição sem instantâneo suficientemente visível

O histórico era preservado, mas a superfície precisava associar o relatório à versão da regra candidata vigente no período, impedindo leitura retroativa silenciosa após mudança futura.

## 5. Reformulação aprovada

### 5.1 Gate de agregação e supressão

As referências passam a demonstrar que:

- detalhamentos por origem somente são exibidos quando a regra de agregação aplicável permitir;
- contagens abaixo do limiar aparecem como `não exibido por agregação`;
- supressão não equivale a zero;
- o limiar definitivo permanece pendente de política especializada;
- nenhum identificador individual é exposto.

### 5.2 Proveniência junto de cada camada

Cada camada passa a nomear sua origem principal:

- entrega — instrumentada e calculada;
- interação — instrumentada quando disponível;
- atribuição candidata — calculada por regra revisável;
- autorrelato — declarado pelo anunciante e não verificado automaticamente.

### 5.3 Atribuição em agregados, não em linhas individuais

A superfície de atribuição passa a apresentar agrupamentos por tipo de evento e origem candidata, sem identificador, sequência individual ou percurso pessoal.

A linguagem utiliza `associação candidata patrocinada`, `origem orgânica preservada` e `origem indeterminada`, evitando tratar o cálculo como origem causal definitiva.

### 5.4 Instantâneo da regra candidata

O relatório passa a mostrar:

- versão da regra candidata;
- período em que a regra foi aplicada;
- janela considerada;
- data da última atualização;
- aviso de que mudança futura não reescreve silenciosamente relatórios anteriores.

### 5.5 Reconciliação por tipo de evento

O estado móvel deixa de apresentar um total heterogêneo.

A referência passa a separar, por exemplo:

- impressões válidas, invalidadas e em revisão;
- cliques válidos e em revisão;
- campo não instrumentado;
- orçamento utilizado sujeito à revisão;
- saldo candidato.

Cada número possui unidade e significado próprios.

### 5.6 Estados de dado e reconciliação

As referências passam a distinguir:

- provisório;
- em revisão;
- parcialmente reconciliado;
- reconciliado;
- não disponível;
- não exibido por agregação.

`Reconciliado` significa conclusão do tratamento operacional definido para os eventos. Não confirma devolução, crédito, estorno, causalidade, impacto ou encerramento jurídico, fiscal e contábil.

### 5.7 Autorrelato com verificação e agregação explícitas

O autorrelato passa a mostrar:

- responsável institucional;
- data e período declarado;
- estado `não verificado automaticamente pela Guivos`;
- ausência de soma com eventos instrumentados;
- possibilidade de supressão da quantidade;
- ausência de valor causal ou de impacto comprovado.

### 5.8 Consistência entre computador e aplicativo móvel

Os dois canais passam a utilizar os mesmos conceitos:

- quatro camadas;
- proveniência textual;
- período e atualização;
- atribuição candidata não causal;
- ausência de dados sem zero;
- supressão por agregação;
- reconciliação sem promessa financeira;
- histórico e regra preservados.

## 6. Critérios funcionais confirmados

Após a reformulação, o conjunto demonstra que:

- entrega, interação, atribuição candidata e autorrelato são camadas independentes;
- cada camada informa proveniência e estado do dado;
- período consultado e atualização permanecem visíveis;
- campanha ativa poderá possuir dados provisórios;
- encerramento não torna todos os dados automaticamente reconciliados;
- `não disponível` não significa zero;
- `não exibido por agregação` não significa ausência de evento;
- detalhamento por origem depende de regra de agregação;
- o limiar final não é antecipado;
- nenhuma linha representa pessoa ou sequência individual;
- atribuição é apresentada em agregados por tipo de evento;
- associação candidata patrocinada não é causalidade;
- origem orgânica permanece preservada;
- origem indeterminada permanece legítima;
- dupla atribuição silenciosa continua proibida;
- versão da regra candidata acompanha o relatório;
- alteração futura da regra não reescreve silenciosamente o passado;
- autorrelato é declarado e não verificado automaticamente;
- autorrelato não é somado a eventos instrumentados;
- quantidade de autorrelato poderá ser suprimida;
- reconciliação separa eventos por tipo e unidade;
- eventos válidos, invalidados e em revisão não são misturados em total heterogêneo;
- orçamento utilizado e saldo candidato permanecem separados;
- reconciliação não confirma devolução, crédito ou estorno;
- nenhuma lista de visualizadores ou dado individual é exibida;
- conversão, impacto humano, qualidade, confiança e evolução não são inferidos;
- nenhum algoritmo, cobrança real, exportação ou implementação é criado.

## 7. Estado dos artefatos reformulados

A referência validada contém:

1. `uxa-048-aggregated-report-overview-desktop.svg`;
2. `uxa-048-aggregated-report-attribution-desktop.svg`;
3. `uxa-048-aggregated-report-overview-mobile.svg`;
4. `uxa-048-aggregated-report-reconciliation-mobile.svg`.

Os artefatos permanecem em baixa fidelidade, com 1.440 × 1.024 pixels para computador e 390 × 844 pixels para aplicativo móvel.

## 8. Proteções preservadas

- pagamento não compra relevância, qualidade, confiança ou impacto;
- relatório não altera ranking orgânico;
- origem orgânica não é apagada;
- dados protegidos não alimentam mensuração publicitária;
- nenhum perfil publicitário individual é criado;
- nenhuma lista de visualizadores é fornecida;
- supressão de contagem não é convertida em zero;
- atribuição candidata não é causalidade;
- autorrelato não é evidência independente;
- saldo não é devolução confirmada;
- Engenharia de Produto permanece pausada.

## 9. Limites

Esta validação não cria:

- política final de atribuição;
- limiar definitivo de agregação e privacidade;
- política final de reconciliação, saldo, crédito, estorno ou disputa;
- estados de erro completos;
- algoritmo de entrega ou leilão;
- antifraude técnico;
- perfil publicitário;
- exportação real;
- design visual final;
- acessibilidade técnica concluída;
- protótipo navegável;
- teste com usuários;
- checkout, faturamento, cobrança ou Engenharia de Produto.

## 10. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
2. criar estados de erro, inventário insuficiente e preferência publicitária;
3. criar estados móveis adicionais de gestão, se priorizados;
4. testar posteriormente relatório, atribuição, autorrelato, agregação e reconciliação com Organizações e Coletivos;
5. iniciar políticas especializadas somente após autorização própria.

Nenhum ato é iniciado automaticamente.
