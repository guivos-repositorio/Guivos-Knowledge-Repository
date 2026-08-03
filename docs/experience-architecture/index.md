---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.52.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-03
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
  - UXA-049
  - UXA-050
  - UXA-051
  - UXA-052
  - UXA-053
  - UXA-054
  - UXA-055
  - UXA-056
  - GEM-007-A1
  - GEM-010-A2
  - M7.58
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
| Opportunity Boost | [contrato](uxa-038-opportunity-boost-functional-experience-contract.md), [validação](uxa-039-opportunity-boost-functional-validation-and-reformulation.md), [configuração desktop](uxa-040-opportunity-boost-advertiser-flow-low-fidelity-wireframes.md), [validação desktop](uxa-041-opportunity-boost-advertiser-wireframe-functional-validation-and-reformulation.md), [cartão e explicação](uxa-042-opportunity-boost-sponsored-card-and-explanation-low-fidelity-wireframes.md), [validação do cartão](uxa-043-opportunity-boost-sponsored-card-functional-validation-and-reformulation.md), [Lista e Mapa](uxa-044-opportunity-boost-sponsored-list-and-map-low-fidelity-wireframes.md), [validação territorial](uxa-045-opportunity-boost-sponsored-list-map-functional-validation-and-reformulation.md), [gestão desktop](uxa-046-opportunity-boost-active-campaign-management-low-fidelity-wireframes.md), [validação da gestão desktop](uxa-047-opportunity-boost-active-campaign-management-functional-validation-and-reformulation.md), [relatório agregado](uxa-048-opportunity-boost-aggregated-report-low-fidelity-wireframes.md), [validação do relatório](uxa-049-opportunity-boost-aggregated-report-functional-validation-and-reformulation.md), [validação transversal](uxa-050-opportunity-boost-complete-wireframe-set-functional-validation.md), [configuração móvel](uxa-051-opportunity-boost-mobile-advertiser-configuration-low-fidelity-wireframes.md), [validação da configuração móvel](uxa-052-opportunity-boost-mobile-advertiser-configuration-functional-validation-and-reformulation.md), [gestão móvel](uxa-053-opportunity-boost-mobile-active-campaign-management-low-fidelity-wireframes.md), [validação da gestão móvel](uxa-054-opportunity-boost-mobile-active-campaign-management-functional-validation-and-reformulation.md) e [estados residuais](uxa-055-opportunity-boost-residual-states-low-fidelity-wireframes.md) |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 e [descoberta, perfil público e participação](uxa-056-collective-discovery-public-profile-and-participation-functional-contract.md) |

## 5. Estado atual

| Elemento | Situação | Referência |
|---|---|---|
| Arquitetura da Experiência | ativa até o contrato de participação em Coletivos | UXA-000 a UXA-056 |
| Resultados Empresariais | 18 decisões e zero Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |
| Página Inicial pública | validada e materializada para computador | UXA-020 a UXA-022 |
| Início protegido móvel | validado e reformulado | UXA-023; UXA-034; UXA-035 |
| Compreensão inicial móvel | validada e reformulada em cinco estados | UXA-036; UXA-037 |
| Tela Hoje | validada; transição inicial ainda não revisada | UXA-002; UXA-006; UXA-010 |
| Mapa | estados orgânicos e patrocinados móveis e desktop funcionalmente validados | UXA-024 a UXA-033; UXA-044; UXA-045 |
| Coletivos | descoberta, perfil público e participação contratados; novos wireframes não iniciados | UXA-014 a UXA-019; UXA-056 |
| Opportunity Boost | 46 wireframes materializados; 36 validados por pacote e 10 estados residuais aguardando validação | UXA-038 a UXA-055 |
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

A UXA-040 reformulada e a UXA-041 validam cinco referências do fluxo inicial do anunciante para computador.

A UXA-042 reformulada e a UXA-043 validam seis referências do cartão, da explicação e do Boost Social Financiado.

A UXA-044 reformulada e a UXA-045 validam quatro referências territoriais patrocinadas.

A UXA-046 reformulada e a UXA-047 validam seis referências de gestão para computador.

A UXA-048 reformulada e a UXA-049 validam quatro referências do relatório agregado.

A UXA-050 valida transversalmente 25 wireframes e consolida identidade, versão aprovada, transições, controles, origem, histórico, mensuração e cobertura por canal.

A UXA-051 reformulada e a UXA-052 validam cinco referências móveis da configuração do anunciante.

A UXA-053 reformulada e a UXA-054 validam seis referências móveis de gestão.

A UXA-055 materializa dez estados residuais móveis:

1. erro técnico temporário patrocinado;
2. falha de atualização do anunciante;
3. inventário patrocinado indisponível;
4. baixa oferta orgânica;
5. mostrar menos deste tipo;
6. desativar oportunidades patrocinadas;
7. ocultar campanha específica;
8. revisar e desfazer preferências;
9. denunciar conteúdo ou informação;
10. contestar uso indevido de dados.

Os estados residuais preservam:

- erro técnico distinto de zero inventário;
- último estado confirmado diante de atualização não concluída;
- catálogo orgânico acessível durante falha patrocinada;
- critérios sem ampliação automática;
- baixa oferta orgânica reduzindo publicidade;
- filtros de oportunidades separados de preferências publicitárias;
- ocultação, redução e desativação com escopos próprios;
- confirmações inicialmente vazias;
- escolhas revisáveis e reversíveis;
- denúncia separada de contestação de dados;
- identidade, preferência e contestação da pessoa não reveladas ao anunciante.

Os dez artefatos ainda exigem validação funcional especializada.

O conjunto completo demonstra:

- configuração não inicia entrega;
- aprovação não inicia entrega;
- programação depende da permanência dos gates;
- alteração material afeta somente entrega futura;
- limitação, pausa, cancelamento e reconciliação possuem efeitos distintos;
- preferência negativa prevalece sobre entrega contratada;
- ocultar publicidade não reduz catálogo orgânico;
- baixa oferta orgânica reduz publicidade;
- erro, ausência, zero e supressão permanecem distintos;
- anunciante e financiador não recebem lista de pessoas;
- atribuição candidata não é causalidade;
- autorrelato não é evento instrumentado;
- saldo não é devolução confirmada;
- conversão não comprova impacto humano.

Pagamento não altera razão orgânica, confiança, impacto ou recomendação.

A UXA-050 permanece autoridade transversal dos 25 artefatos examinados naquele incremento. A UXA-055 não amplia retroativamente esse escopo.

## 10. Descoberta, perfil público e participação em Coletivos

A UXA-056 define que Coletivos poderão ser encontrados por busca e exploração intencional e também por sugestão contextual explicada.

Permanecem separados:

- resultado de busca;
- exploração por categoria ou território;
- sugestão da Guivos;
- recomendação de uma pessoa;
- convite;
- link compartilhado;
- publicidade.

O contrato também separa:

- perfil público;
- Início do participante;
- gestão do responsável;
- acompanhar;
- solicitar entrada;
- participar;
- frequentar atividade;
- aceitar papel;
- pausar ou sair.

A lista nominal não será pública por padrão. Seguidores, participantes confirmados, presença em atividade, colaboradores e moderadores não serão combinados em uma contagem genérica.

A superfície `Meus Coletivos` organizará participações, acompanhamentos, solicitações, convites e pausas. Avaliação e reputação permanecerão para a UXA-057. Interações, recomendações e conexões permanecerão para a UXA-058.

Nenhum novo wireframe foi criado pela UXA-056.

## 11. Gate de persistência e personalização

Criar conta, digitar, gravar, enviar arquivo, concluir relato ou aceitar uma afirmação não autoriza automaticamente persistência ou personalização.

A mesma proteção impede que conteúdo protegido seja reutilizado silenciosamente para publicidade ou descoberta de Coletivos.

## 12. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 13. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. definir avaliação e reputação de Coletivos, atividades, cursos, oportunidades e Organizações na UXA-057;
2. definir interações, recomendações, conexões, comunicados, discussões, perguntas e respostas na UXA-058;
3. materializar wireframes de descoberta, perfil público, participação, `Meus Coletivos` e gestão;
4. validar funcionalmente esses futuros conjuntos;
5. validar funcionalmente e reformular os dez estados residuais da UXA-055;
6. validar transversalmente os 46 wireframes do Opportunity Boost, se priorizado;
7. definir protocolo de protótipo e plano de teste;
8. criar a referência móvel da Home e validar a transição para a primeira Tela Hoje.

Nenhum ato é iniciado automaticamente.
