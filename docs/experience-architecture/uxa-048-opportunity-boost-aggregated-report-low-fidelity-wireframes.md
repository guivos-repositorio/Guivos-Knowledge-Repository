---
id: UXA-048
title: Wireframes de Baixa Fidelidade do Relatório Agregado do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-01
parent: UXA-047
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
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.50
normative: false
---

# Wireframes de Baixa Fidelidade do Relatório Agregado do Opportunity Boost

## 1. Finalidade

Este documento materializa o relatório agregado do Opportunity Boost para computador e aplicativo móvel.

O pacote demonstra como o anunciante poderá consultar entrega, interação, atribuição candidata, autorrelato, reconciliação e limitações de interpretação sem:

- confundir impressão ou clique com conversão;
- apresentar atribuição candidata como causalidade comprovada;
- transformar autorrelato em evento instrumentado;
- preencher ausência de dado com zero;
- revelar pessoas expostas, identificadores individuais ou lista de visualizadores;
- misturar origem orgânica e patrocinada silenciosamente;
- inferir impacto humano, evolução, confiança ou qualidade;
- apresentar saldo como crédito, estorno ou devolução confirmada;
- prometer precisão que a instrumentação não sustenta;
- iniciar algoritmo, cobrança real, protótipo ou Engenharia de Produto.

## 2. Pergunta funcional do conjunto

> **O anunciante distingue entrega, interação, atribuição candidata e resultado declarado, compreende o período e a atualização de cada dado, identifica ausências e limitações e consulta reconciliação sem interpretar o relatório como prova de conversão, causalidade ou impacto humano?**

A pergunta ainda deverá ser respondida por validação funcional especializada dos wireframes.

## 3. Artefatos

| Artefato | Estado principal | Canal | Dimensão |
|---|---|---|---:|
| visão geral agregada | dados provisórios durante campanha | web para computador | 1.440 × 1.024 |
| atribuição e autorrelato | interpretação e proveniência | web para computador | 1.440 × 1.024 |
| visão geral agregada | resumo móvel durante campanha | aplicativo móvel | 390 × 844 |
| reconciliação e ausência de dados | encerramento e dados não disponíveis | aplicativo móvel | 390 × 844 |

Todos os artefatos utilizam baixa fidelidade, dados ilustrativos e rótulos textuais independentes de cor.

## 4. Artefatos visuais

### 4.1 Visão geral agregada para computador

![Visão geral agregada para computador](../assets/wireframes/uxa-048-aggregated-report-overview-desktop.svg)

`docs/assets/wireframes/uxa-048-aggregated-report-overview-desktop.svg`

Demonstra:

- campanha, status, período consultado e última atualização;
- aviso de dados provisórios;
- orçamento total, utilizado e saldo não utilizado;
- impressões válidas e visíveis;
- frequência média e tráfego inválido removido;
- cliques válidos, visualizações de detalhe e salvamentos;
- interesse agregado e início de inscrição quando instrumentado;
- separação visual das quatro camadas;
- ausência de lista de visualizadores;
- acesso à metodologia e ao histórico.

### 4.2 Atribuição candidata e autorrelato para computador

![Atribuição candidata e autorrelato para computador](../assets/wireframes/uxa-048-aggregated-report-attribution-desktop.svg)

`docs/assets/wireframes/uxa-048-aggregated-report-attribution-desktop.svg`

Demonstra:

- janela candidata e evento compatível;
- origem patrocinada, orgânica e indeterminada separadas;
- proibição de dupla atribuição silenciosa;
- atribuição como associação técnica, não prova causal;
- autorrelato com responsável, data e texto declarado;
- distinção entre dado instrumentado, calculado, declarado e indisponível;
- limitações de cobertura e atualização;
- ausência de inferência de impacto humano.

### 4.3 Visão geral agregada móvel

![Visão geral agregada móvel](../assets/wireframes/uxa-048-aggregated-report-overview-mobile.svg)

`docs/assets/wireframes/uxa-048-aggregated-report-overview-mobile.svg`

Demonstra:

- resumo vertical das quatro camadas;
- período e atualização no topo;
- entrega e interação em cartões compactos;
- atribuição candidata com aviso textual;
- autorrelato identificado;
- ação para consultar metodologia;
- ausência de pessoas identificadas.

### 4.4 Reconciliação e ausência de dados móvel

![Reconciliação e ausência de dados móvel](../assets/wireframes/uxa-048-aggregated-report-reconciliation-mobile.svg)

`docs/assets/wireframes/uxa-048-aggregated-report-reconciliation-mobile.svg`

Demonstra:

- campanha encerrada aguardando ou concluindo reconciliação;
- eventos válidos, invalidados e ainda em revisão;
- orçamento utilizado e saldo candidato separados;
- tratamento do saldo ainda não definido;
- campo sem instrumentação apresentado como `não disponível`;
- ausência de dado distinta de valor zero;
- histórico preservado;
- relatório sem promessa de devolução ou causalidade.

## 5. Estrutura obrigatória em quatro camadas

### 5.1 Entrega

A camada de entrega apresenta:

- orçamento total;
- orçamento utilizado;
- saldo não utilizado;
- período da campanha;
- período consultado;
- status da campanha;
- impressões válidas;
- impressões visíveis, quando mensuráveis;
- frequência média;
- tráfego inválido removido;
- data e horário de atualização.

Entrega descreve distribuição publicitária. Não representa interesse, conversão, atribuição ou impacto.

### 5.2 Interação

A camada de interação poderá apresentar, quando instrumentado:

- cliques válidos;
- visualizações do detalhe;
- salvamentos;
- declarações de interesse agregadas;
- início de inscrição ou contratação;
- conclusão instrumentada, quando tecnicamente disponível e legitimamente vinculada.

Clique não equivale a interesse confirmado. Início não equivale a conclusão. Conclusão instrumentada não equivale a impacto humano.

### 5.3 Atribuição candidata

A camada de atribuição candidata deverá mostrar:

- evento elegível;
- janela candidata utilizada;
- origem patrocinada preservada;
- origem orgânica preservada;
- origem indeterminada quando não houver base suficiente;
- condição de instrumentação;
- regra contra dupla atribuição silenciosa;
- caráter técnico, revisável e não causal.

Atribuição candidata não afirma que o anúncio causou o evento.

### 5.4 Autorrelato

A camada de autorrelato deverá mostrar:

- informação declarada pelo anunciante;
- responsável pela declaração;
- data da declaração;
- período ao qual se refere;
- campo de observação;
- identificação explícita como informação não instrumentada pela Guivos.

Autorrelato não será somado silenciosamente a eventos instrumentados e não será apresentado como evidência independente.

## 6. Proveniência dos dados

Cada métrica ou informação deverá possuir uma origem compreensível:

| Rótulo | Significado |
|---|---|
| instrumentado | evento registrado por mecanismo técnico definido |
| calculado | valor derivado de eventos ou regras declaradas |
| declarado pelo anunciante | informação fornecida por responsável autorizado |
| não disponível | dado sem instrumentação, cobertura ou base suficiente |
| em revisão | evento ainda sujeito a validação ou reconciliação |

A interface não substituirá `não disponível` por `0`.

## 7. Período, atualização e estado do dado

O relatório deverá distinguir:

- período total da campanha;
- período atualmente consultado;
- data e horário da última atualização;
- dados provisórios;
- dados em revisão;
- dados reconciliados;
- campos ainda indisponíveis.

Uma campanha ativa poderá apresentar dados provisórios. Encerramento não torna todos os dados automaticamente reconciliados.

## 8. Origem orgânica e patrocinada

Quando um evento puder possuir múltiplas origens, a interface deverá:

- preservar registros orgânicos;
- preservar registros patrocinados;
- indicar origem indeterminada quando necessário;
- impedir dupla atribuição silenciosa;
- explicar a janela candidata;
- não reclassificar interação orgânica como patrocinada somente porque a pessoa também foi exposta à campanha.

Correspondência orgânica continua independente de distribuição paga.

## 9. Ausência de dados

Ausência de dado poderá ocorrer por:

- métrica não instrumentada;
- integração indisponível;
- cobertura incompleta;
- evento fora da janela;
- base insuficiente;
- processamento ainda em revisão;
- opção legítima da pessoa ou do anunciante;
- regra de privacidade ou agregação mínima.

A interface deverá explicar o motivo conhecido sem inventar valor, tendência ou causa.

## 10. Privacidade e agregação

O relatório não deverá fornecer:

- lista de visualizadores;
- nomes, perfis ou identificadores de pessoas expostas;
- sequência individual de navegação;
- relatos protegidos;
- compreensão inicial, Momento Atual ou Próximo Passo;
- localização exata ou histórico territorial individual;
- inferências sensíveis;
- segmentação individual retrospectiva.

Resultados serão apresentados de forma agregada e sujeitos a limiares posteriores de privacidade e segurança.

## 11. Reconciliação

A reconciliação deverá separar:

- eventos válidos;
- eventos invalidados;
- eventos ainda em revisão;
- orçamento utilizado associado aos eventos válidos, quando aplicável;
- saldo não utilizado;
- tratamento candidato do saldo;
- data da última revisão;
- histórico de decisões.

Reconciliação não equivale automaticamente a devolução, crédito, estorno ou encerramento jurídico, fiscal e contábil.

## 12. Limitações de interpretação

O relatório deverá declarar que:

- alcance não é compreensão;
- impressão não é atenção garantida;
- clique não é conversão;
- salvamento não é participação;
- início de inscrição não é conclusão;
- atribuição candidata não é causalidade;
- autorrelato não é evento instrumentado;
- conversão não é impacto humano;
- ausência de dado não é zero;
- número agregado não comprova qualidade, confiança ou evolução.

## 13. Acessibilidade e linguagem

- camada, origem e estado do dado serão textuais;
- significado não dependerá de cor;
- valores terão rótulo, unidade e período;
- abreviações técnicas deverão possuir explicação;
- dados ausentes terão motivo legível;
- avisos não usarão culpa, urgência ou escassez artificial;
- tabelas e cartões deverão possuir ordem de leitura coerente;
- atualizações e estados provisórios serão anunciáveis;
- autorrelato será identificado antes do conteúdo declarado.

Esta referência não conclui acessibilidade técnica.

## 14. Proteções preservadas

- pagamento não compra relevância, qualidade, confiança ou impacto;
- relatório não altera ranking orgânico;
- nenhum perfil publicitário individual é criado;
- anunciante não recebe lista de visualizadores;
- dados protegidos não alimentam o relatório;
- origem orgânica não é apagada;
- dupla atribuição silenciosa é proibida;
- saldo não é devolução confirmada;
- relatório não garante entrega, conversão ou resultado;
- Engenharia de Produto permanece pausada.

## 15. Limites

Este incremento não cria:

- validação funcional dos quatro wireframes;
- política final de atribuição;
- política final de reconciliação, saldo, crédito, estorno ou disputa;
- limiar definitivo de agregação e privacidade;
- estados de erro completos;
- algoritmo de entrega ou leilão;
- antifraude técnico;
- perfil publicitário;
- exportação real de dados;
- design visual final;
- protótipo navegável;
- teste com usuários;
- checkout, faturamento, cobrança ou Engenharia de Produto.

## 16. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente e reformular os quatro wireframes da UXA-048;
2. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
3. criar estados de erro, inventário insuficiente e preferência publicitária;
4. criar estados móveis adicionais de gestão, se priorizados;
5. testar posteriormente relatório, atribuição, autorrelato e reconciliação com Organizações e Coletivos.

Nenhum ato é iniciado automaticamente.
