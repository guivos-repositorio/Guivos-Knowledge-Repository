---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.44.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-01
related:
  - PAS-001
  - GLPA-001
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-008
  - UXA-009
  - UXA-010
  - UXA-011
  - UXA-011-A1
  - UXA-012
  - UXA-013
  - UXA-014
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - UXA-019
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
  - UXA-031
  - UXA-032
  - UXA-033
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
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
  - M7.50
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos do Repositório em experiências compreensíveis para Pessoas, Organizações e Coletivos.

Ela governa jornadas, superfícies, navegação, voluntariedade, privacidade, compreensão, explicabilidade, publicidade identificada e critérios para wireframes, protótipos e testes posteriores.

## 2. Limite da frente

Esta frente não inicia Engenharia de Produto, não define tecnologia, não cria design visual final e não autoriza produção.

## 3. Ordem funcional pessoal

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ processamento temporário visível e interrompível
→ compreensão inicial apresentada como hipótese
→ revisão, correção, abertura, limitação ou rejeição
→ decisão separada sobre persistência
→ decisão separada sobre personalização
→ Tela Hoje, jornada sem personalização ou exploração geral
→ Hoje | Jornada | Explorar | Mapa | Eu
```

Oferta de plano e Opportunity Boost não entram no início protegido, compreensão, autorização ou Próximo Passo pessoal.

## 4. Documentos ativos por responsabilidade

| Responsabilidade | Documentos principais |
|---|---|
| Fundação, mapas e padrões | UXA-001, UXA-003, UXA-003-A1, UXA-005, UXA-009, UXA-011 e UXA-011-A1 |
| Página Inicial pública | [contrato](uxa-020-home-and-journey-entry.md), [validação](uxa-021-public-home-functional-validation-and-reformulation.md) e [wireframe](uxa-022-public-home-low-fidelity-wireframe.md) |
| Início protegido | [contrato](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md), [wireframe](uxa-034-protected-journey-entry-low-fidelity-wireframe.md) e [validação](uxa-035-protected-journey-entry-wireframe-functional-validation-and-reformulation.md) |
| Compreensão inicial | [contrato transversal](uxa-011-a1-moment-progress-and-next-step-explainability.md), [wireframe](uxa-036-initial-understanding-low-fidelity-wireframe.md) e [validação](uxa-037-initial-understanding-wireframe-functional-validation-and-reformulation.md) |
| Tela Hoje | UXA-002, UXA-006 e UXA-010 |
| Explorar e Mapa | UXA-004 e UXA-024 a UXA-033 |
| Opportunity Boost | [contrato reformulado](uxa-038-opportunity-boost-functional-experience-contract.md), [validação funcional](uxa-039-opportunity-boost-functional-validation-and-reformulation.md), [wireframes do anunciante](uxa-040-opportunity-boost-advertiser-flow-low-fidelity-wireframes.md), [validação dos wireframes](uxa-041-opportunity-boost-advertiser-wireframe-functional-validation-and-reformulation.md), [cartão e explicação](uxa-042-opportunity-boost-sponsored-card-and-explanation-low-fidelity-wireframes.md), [validação do cartão e explicação](uxa-043-opportunity-boost-sponsored-card-functional-validation-and-reformulation.md), [estados patrocinados de Lista e Mapa](uxa-044-opportunity-boost-sponsored-list-and-map-low-fidelity-wireframes.md), [validação desses estados](uxa-045-opportunity-boost-sponsored-list-map-functional-validation-and-reformulation.md), [gestão da campanha ativa](uxa-046-opportunity-boost-active-campaign-management-low-fidelity-wireframes.md), [validação da gestão](uxa-047-opportunity-boost-active-campaign-management-functional-validation-and-reformulation.md) e [relatório agregado](uxa-048-opportunity-boost-aggregated-report-low-fidelity-wireframes.md) |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 |

## 5. Estado atual

| Elemento | Situação | Referência |
|---|---|---|
| Arquitetura da Experiência | ativa até a materialização do relatório agregado do Boost | UXA-000 a UXA-048 |
| Resultados Empresariais | 18 decisões e zero Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |
| Página Inicial pública | validada e materializada para computador | UXA-020 a UXA-022 |
| Início protegido móvel | validado e reformulado | UXA-023; UXA-034; UXA-035 |
| Compreensão inicial móvel | validada e reformulada em cinco estados | UXA-036; UXA-037 |
| Tela Hoje | validada; transição inicial ainda não revisada | UXA-002; UXA-006; UXA-010 |
| Mapa | estados orgânicos e patrocinados móveis e desktop funcionalmente validados | UXA-024 a UXA-033; UXA-044; UXA-045 |
| Opportunity Boost | experiência, fluxo do anunciante, cartão, explicação, Lista, Mapa e gestão ativa validados; relatório agregado materializado e aguardando validação | UXA-038 a UXA-048 |
| Protótipo, design e testes | não iniciados | — |

## 6. Início protegido e compreensão

O início protegido preserva explicação anterior ao relato, dados de acesso separados, modalidades equivalentes, revisão, autorização específica e recusa sem processamento.

A compreensão inicial preserva processamento temporário e interrompível, ausência de tarefa oculta, afirmações individualizadas, hipótese sem diagnóstico, revisão sem resposta padrão, relato original separado da interpretação, decisões independentes e base insuficiente sem pressão.

## 7. Tela Hoje

A Tela Hoje é a superfície recorrente posterior à compreensão suficiente, revisada e autorizada conforme a condição escolhida.

A validação da transição entre a compreensão e a primeira Tela Hoje ainda não foi iniciada.

## 8. Explorar e Mapa

`Explorar` organiza descoberta ampla por listas, busca, categorias e filtros gerais.

`Mapa` organiza descoberta territorial e preserva uso sem localização, visualização em Lista, estado sem resultados e referência para computador.

Os estados patrocinados preservam a mesma consulta, separam contagens orgânicas e pagas, distinguem filtros de oportunidades e preferência publicitária e exigem `Pesquisar nesta área` antes de atualizar a consulta após movimentação do Mapa.

## 9. Opportunity Boost

A UXA-038 reformulada e a UXA-039 estabelecem gates explicáveis, objetivo único, critérios utilizados e excluídos, alcance sem garantia, prévia separada do orgânico, pausa por alteração material, estados completos, Boost Social Financiado identificado, controles reversíveis, proteção da densidade, Mapa separado e relatório em quatro camadas.

A UXA-040 reformulada e a UXA-041 validam cinco referências do fluxo inicial do anunciante.

A UXA-042 reformulada e a UXA-043 validam seis referências do cartão, da explicação e do Boost Social Financiado.

A UXA-044 reformulada e a UXA-045 validam quatro referências territoriais patrocinadas.

A UXA-046 reformulada e a UXA-047 validam seis referências de gestão:

1. campanha programada;
2. campanha ativa;
3. campanha limitada;
4. campanha pausada;
5. alteração material;
6. encerramento e cancelamento.

O conjunto validado demonstra:

- programação sem entrega e ativação condicionada aos gates;
- estado ativo com resumo operacional datado, sem garantia de resultado;
- limitação como entrega reduzida, sem acelerar orçamento ou ampliar período;
- pausa interrompendo novos eventos sem apagar eventos válidos;
- retomada bloqueada até resolução e verificação da causa;
- alteração material sem aprovação ou retomada automática;
- cancelamento bloqueado até motivo e confirmações completas;
- estados finais separados, incluindo suspensão por política;
- saldo e reconciliação mantidos como candidatos.

A UXA-048 materializa quatro referências do relatório agregado:

1. visão geral para computador;
2. atribuição candidata e autorrelato para computador;
3. visão geral móvel;
4. reconciliação e ausência de dados móvel.

O relatório separa entrega, interação, atribuição candidata e autorrelato, identifica proveniência e períodos, preserva origem orgânica, apresenta ausência como `não disponível`, proíbe lista de visualizadores e não infere causalidade ou impacto humano.

Os quatro wireframes da UXA-048 ainda exigem validação funcional própria.

Pagamento não altera razão orgânica, confiança, impacto ou recomendação.

## 10. Gate de persistência e personalização

Criar conta, digitar, gravar, enviar arquivo, concluir relato ou aceitar uma afirmação não autoriza automaticamente persistência ou personalização.

A mesma proteção impede que conteúdo protegido seja reutilizado silenciosamente para publicidade.

## 11. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 12. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente e reformular os wireframes da UXA-048;
2. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
3. criar estados móveis adicionais de gestão, se priorizados;
4. criar estados de erro, inventário insuficiente e preferência publicitária;
5. testar relatório, atribuição, autorrelato, reconciliação, disclosure, densidade, frequência, marcadores, localização, orçamento e controles;
6. criar a referência móvel da Home;
7. validar a transição para a primeira Tela Hoje;
8. criar referência para computador e tablet quando priorizada.

Nenhum ato é iniciado automaticamente.
