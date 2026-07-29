---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.34.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-28
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
  - GEM-007-A1
  - GEM-010-A2
  - M7.40
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
| Opportunity Boost | [contrato funcional](uxa-038-opportunity-boost-functional-experience-contract.md) |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 |

## 5. Estado atual

| Elemento | Situação | Referência |
|---|---|---|
| Arquitetura da Experiência | ativa até Opportunity Boost | UXA-000 a UXA-038 |
| Resultados Empresariais | 18 decisões e zero Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |
| Página Inicial pública | validada e materializada para computador | UXA-020 a UXA-022 |
| Início protegido móvel | validado e reformulado | UXA-023; UXA-034; UXA-035 |
| Compreensão inicial móvel | validada e reformulada em cinco estados | UXA-036; UXA-037 |
| Tela Hoje | validada; transição inicial ainda não revisada | UXA-002; UXA-006; UXA-010 |
| Mapa | estados móveis e referência desktop validados | UXA-024 a UXA-033 |
| Opportunity Boost | experiência funcional definida; validação e wireframes pendentes | UXA-038 |
| Protótipo, design e testes | não iniciados | — |

## 6. Início protegido e compreensão

O início protegido preserva explicação anterior ao relato, dados de acesso separados, modalidades equivalentes, revisão, autorização específica e recusa sem processamento.

A compreensão inicial preserva:

- processamento temporário e interrompível;
- ausência de tarefa oculta;
- afirmações individualizadas por natureza, origem e confiança;
- hipótese sem diagnóstico;
- revisão sem resposta padrão;
- relato original separado da interpretação;
- persistência e personalização como decisões independentes;
- base insuficiente sem pressão.

## 7. Tela Hoje

A Tela Hoje é a superfície recorrente posterior à compreensão suficiente, revisada e autorizada conforme a condição escolhida.

A validação da transição entre a compreensão e a primeira Tela Hoje ainda não foi iniciada.

## 8. Explorar e Mapa

`Explorar` organiza descoberta ampla por listas, busca, categorias e filtros gerais.

`Mapa` organiza descoberta territorial e preserva uso sem localização, visualização em Lista, estado sem resultados e referência para computador.

## 9. Opportunity Boost

O [UXA-038](uxa-038-opportunity-boost-functional-experience-contract.md) estabelece:

- distribuição somente em inventário patrocinado separado;
- selo `Patrocinado` ou `Impulsionado` antes da interação;
- superfícies permitidas em Explorar, busca, listas, categorias, Mapa, detalhe separado e página do anunciante;
- bloqueio no início protegido, compreensão, consentimento, Tela Hoje como Próximo Passo e Jornada pessoal;
- densidade candidata de até 20%;
- proibição de duas unidades patrocinadas consecutivas;
- posição paga sem substituição do primeiro resultado orgânico;
- explicação `Por que estou vendo isto?`;
- controles de ocultar, ajustar preferências e denunciar;
- marcador próprio e filtro no Mapa;
- painel do anunciante com métricas agregadas;
- identificação acessível sem depender apenas de cor.

Pagamento não altera razão orgânica, confiança, impacto ou recomendação.

## 10. Gate de persistência e personalização

Criar conta, digitar, gravar, enviar arquivo, concluir relato ou aceitar uma afirmação não autoriza automaticamente persistência ou personalização.

A mesma proteção impede que conteúdo protegido seja reutilizado silenciosamente para publicidade.

## 11. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 12. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente UXA-038;
2. criar wireframes do fluxo do anunciante, cartão, Mapa e relatório;
3. testar disclosure, densidade, frequência e controles;
4. criar a referência móvel da Home;
5. validar a transição para a primeira Tela Hoje;
6. criar estados especializados de processamento, pausa, falha e retomada;
7. criar referência do início protegido e da compreensão para computador;
8. criar referência para tablet;
9. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
