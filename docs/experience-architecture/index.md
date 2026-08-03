---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.53.0
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
  - UXA-057
  - GEM-007-A1
  - GEM-010-A2
  - M7.59
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos do Repositório em experiências compreensíveis para Pessoas, Organizações e Coletivos.

Ela governa jornadas, superfícies, navegação, voluntariedade, privacidade, explicabilidade, publicidade identificada, participação, avaliação e critérios para wireframes, protótipos e testes posteriores.

## 2. Limite da frente

Esta frente não inicia Engenharia de Produto, não define tecnologia, não cria design visual final e não autoriza produção.

## 3. Ordem funcional pessoal

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ relato e autorização específica
→ compreensão inicial como hipótese
→ revisão, correção e decisões de persistência
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

Oferta de plano, publicidade, participação em Coletivo e pedido de avaliação não entram no início protegido nem substituem o Próximo Passo pessoal.

## 4. Documentos ativos por responsabilidade

| Responsabilidade | Documentos principais |
|---|---|
| Fundação, mapas e padrões | UXA-001, UXA-003, UXA-003-A1, UXA-005, UXA-009, UXA-011 e UXA-011-A1 |
| Home, início protegido e compreensão | UXA-020 a UXA-023 e UXA-034 a UXA-037 |
| Tela Hoje | UXA-002, UXA-006 e UXA-010 |
| Explorar e Mapa | UXA-004 e UXA-024 a UXA-033 |
| Oportunidades | UXA-007, UXA-008, UXA-012 e UXA-013 |
| Organizações e Coletivos | UXA-014 a UXA-019 |
| Descoberta e participação em Coletivos | [UXA-056](uxa-056-collective-discovery-public-profile-and-participation-functional-contract.md) |
| Avaliação e reputação | [UXA-057](uxa-057-evaluation-and-reputation-functional-contract.md) |
| Opportunity Boost | UXA-038 a UXA-055 |

## 5. Estado atual

| Elemento | Situação | Referência |
|---|---|---|
| Arquitetura da Experiência | ativa até avaliação e reputação | UXA-000 a UXA-057 |
| Resultados Empresariais | 18 decisões e zero Resultado canônico | BA-STR-002; COD-018 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |
| Home pública | validada e materializada para computador | UXA-020 a UXA-022 |
| Início protegido móvel | validado e reformulado | UXA-023; UXA-034; UXA-035 |
| Compreensão inicial móvel | validada e reformulada em cinco estados | UXA-036; UXA-037 |
| Tela Hoje | validada; transição inicial ainda não revisada | UXA-002; UXA-006; UXA-010 |
| Mapa | estados orgânicos e patrocinados móveis e desktop validados | UXA-024 a UXA-033; UXA-044; UXA-045 |
| Coletivos | descoberta, perfil público, participação, avaliação e reputação contratados; novos wireframes não iniciados | UXA-014 a UXA-019; UXA-056; UXA-057 |
| Opportunity Boost | 46 wireframes materializados; 36 validados por pacote e 10 pendentes | UXA-038 a UXA-055 |
| Protótipo, design e testes | não iniciados | — |

## 6. Descoberta e participação em Coletivos

A UXA-056 estabelece busca e exploração intencional ao lado de sugestões contextuais explicadas.

Permanecem separados:

- perfil público;
- Início do participante;
- gestão do responsável;
- acompanhar;
- solicitar entrada;
- participar;
- frequentar atividade;
- aceitar função;
- pausar ou sair.

Seguidores, participantes confirmados, presença em atividade, colaboradores e moderadores não serão combinados em uma contagem genérica. A lista nominal não será pública por padrão.

## 7. Avaliação e reputação

A UXA-057 define reputação como evidência contextualizada, não como placar moral.

Objetos separados:

- experiência de participação em Coletivo;
- experiência específica com Organização ou unidade;
- atividade;
- curso ou programa;
- oportunidade;
- relação institucional ou coletiva em escopo governado.

A primeira versão:

- exige experiência elegível para agregação verificada;
- utiliza critérios específicos e escala semântica;
- não adota estrelas universais como representação principal;
- não cria reputação pública de pessoas;
- distingue avaliação, comentário, recomendação, depoimento, denúncia e contestação;
- apresenta amostra, período, distribuição e versão;
- declara base insuficiente sem produzir nota implícita;
- permite resposta oficial sem apagar crítica legítima;
- preserva avaliações anteriores diante de alteração material;
- limita a influência sobre busca e jornada;
- impede que publicidade, plano ou popularidade comprem confiança.

A UXA-057 registra 24 estados para futuros wireframes. Nenhum deles foi materializado.

## 8. Opportunity Boost

Os pacotes UXA-038 a UXA-054 validam contrato, configuração, divulgação, Lista, Mapa, gestão e relatório nos canais materializados.

A UXA-055 acrescenta dez estados residuais móveis ainda pendentes de validação funcional.

O conjunto preserva:

- primeiro resultado orgânico;
- publicidade distinta de recomendação;
- critérios sem ampliação silenciosa;
- baixa oferta orgânica reduzindo publicidade;
- preferências reversíveis;
- anunciante sem lista de pessoas;
- atribuição candidata sem causalidade;
- autorrelato distinto de evento instrumentado.

Pagamento não altera razão orgânica, confiança, impacto, avaliação ou recomendação.

## 9. Gate de persistência e personalização

Criar conta, digitar, gravar, participar, avaliar ou aceitar uma afirmação não autoriza automaticamente persistência ou personalização para outra finalidade.

Conteúdo protegido não será reutilizado silenciosamente para publicidade, descoberta de Coletivos ou reputação.

## 10. Gate de alinhamento à Fundação

Toda superfície deverá demonstrar aderência à Essência, Propósito, Missão Operacional, Visão, Constituição e Princípios Permanentes da Guivos.

Falha material impede avanço para wireframe, protótipo, design, teste, especificação técnica ou desenvolvimento.

## 11. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. definir interações, recomendações e conexões na UXA-058;
2. materializar wireframes de descoberta, perfil público, participação, `Meus Coletivos`, avaliação, comunicação e gestão;
3. validar funcionalmente esses futuros conjuntos;
4. definir limiar estatístico, política jurídica e moderação operacional de avaliações;
5. validar funcionalmente os dez estados residuais da UXA-055;
6. validar transversalmente os 46 wireframes do Opportunity Boost, se priorizado;
7. preparar protótipo e plano de teste;
8. retomar Home móvel e transição para a primeira Tela Hoje.

Nenhum ato é iniciado automaticamente.