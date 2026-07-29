---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 1.70.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-07-28
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
  - GPA-007
  - UXA-000
  - UXA-004
  - UXA-038
  - UXA-039
  - UXA-040
  - UXA-041
  - GEM-004-A1
  - GEM-004-A2
  - GEM-007-A1
  - GEM-010-A1
  - GEM-010-A2
  - GEM-OPPORTUNITY-BOOST-REVIEW-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - ROADMAP-12.17.0
  - M7.43
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro é a superfície oficial do estado global vigente do Repositório de Conhecimento da Guivos quando o incremento correspondente estiver integrado ao ramo principal.

## 2. Estado global vigente

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era de conhecimento | fase de estruturação do conhecimento da Guivos | GE-2 — Knowledge |
| Marco atual | wireframes do fluxo do anunciante do Opportunity Boost funcionalmente validados e reformulados | M7.43; UXA-040; UXA-041 |
| Remediação | concluída; validação mecânica permanente ativa | R1–R6 |
| Achados conhecidos | nenhum crítico, maior ou menor aberto | 0 |
| Arquitetura de Negócios | ativa; 18 decisões humanas concluídas | BA-STR-002; COD-018 |
| Resultados Empresariais | 9 em validação, 3 fundidos, 6 rejeitados e zero canônicos | BA-STR-002-COR-001; BA-STR-002-CODR-001 |
| Arquitetura da Experiência | ativa até UXA-041 | UXA-000 a UXA-041 |
| Home pública | validada e materializada para computador | UXA-020 a UXA-022 |
| Início protegido móvel | validado e reformulado | UXA-023; UXA-034; UXA-035 |
| Compreensão inicial móvel | validada e reformulada em cinco estados | UXA-036; UXA-037 |
| Tela Hoje | validada como entrada recorrente | UXA-002; UXA-006; UXA-010 |
| Mapa e estados | validados, inclusive referência desktop | UXA-024 a UXA-033 |
| Organizações e Coletivos | fundação, superfícies e relações estabelecidas | UXA-014 a UXA-019 |
| Planos para Pessoas | Free, Plus e Pro candidatos | GEM-004-A1 |
| Planos para Coletivos | Livre, Gestão, Impacto e Enterprise candidatos | GEM-004-A1 |
| Planos para Organizações | Business Start, Growth e Scale candidatos | GEM-004-A1 |
| Opportunity Boost econômico | add-on publicitário candidato separado dos planos | GEM-007-A1 |
| Experiência do Boost | funcionalmente validada e reformulada | UXA-038; UXA-039 |
| Fluxo do anunciante do Boost | cinco wireframes para computador funcionalmente validados e reformulados | UXA-040; UXA-041 |
| Preço do Boost | faixas de orçamento, CPM e CPC candidatos | GEM-010-A2 |
| Guivos Ads | papel econômico ampliado e Opportunity Boost registrado | GPA-007; GEM-007-ADS-ECONOMIC-ROLE-001 |
| Protótipo, design e testes | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01; execução em 0% | W0-01 |
| Validação de Mercado | trilha preservada; preços, planos e Boost ainda não testados | — |

## 3. Estado dos Resultados Empresariais

```text
Human decisions: 18 of 18 — completed
Under Validation: 9
Merged: 3
Rejected: 6
Approved Outcomes: 0
Canonical EO/BO codes: 0
Reapplication of the four tests: not started
AQS-O01: not started
Business Capabilities: not started
```

Nenhum Resultado canônico foi criado. A fusão de candidatos não representa aprovação.

## 4. Sequência pessoal vigente

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

Oferta de plano ou publicidade não entra no início protegido, processamento, revisão, autorização ou Próximo Passo pessoal.

## 5. Baseline comercial de planos

### 5.1 Pessoas

| Plano | Mensal | Anual | Ampliação principal |
|---|---:|---:|---|
| Guivos Free | R$ 0,00 | R$ 0,00 | catálogo público e 2 correspondências personalizadas por semana |
| Guivos Plus | R$ 24,90 | R$ 249,00 | correspondências, filtros, alertas e histórico ampliados |
| Guivos Pro | R$ 49,90 | R$ 499,00 | análises, integrações, relatórios e suporte avançados |

### 5.2 Coletivos

| Plano | Mensal | Anual | Limite principal |
|---|---:|---:|---|
| Coletivo Livre | R$ 0,00 | R$ 0,00 | 1 atividade e 1 oportunidade gratuitas por mês; 2 ativas |
| Coletivo Gestão | R$ 89,90 | R$ 899,00 | 4 atividades, 4 oportunidades e 6 ativas; monetização permitida |
| Coletivo Impacto | R$ 249,90 | R$ 2.499,00 | 15 atividades, 15 oportunidades e 20 ativas |
| Coletivo Enterprise | sob consulta | contrato anual | capacidade contratada, categorias personalizáveis, API, SSO e SLA |

### 5.3 Organizações

| Plano | Mensal | Anual | Limite principal |
|---|---:|---:|---|
| Business Start | R$ 299,00 | R$ 2.990,00 | 10 novas oportunidades ou programas por mês; 15 ativos |
| Business Growth | R$ 799,00 | R$ 7.990,00 | 50 novos por mês; 75 ativos; até 5 unidades |
| Business Scale | a partir de R$ 1.990,00 | contrato anual | capacidade, unidades, API, SSO, Power BI e SLA contratados |

Todos os valores permanecem candidatos para validação.

## 6. Opportunity Boost

### 6.1 Elegibilidade econômica

- Coletivo Gestão, Impacto e Enterprise podem contratar diretamente;
- Coletivo Livre somente poderá receber Boost Social Financiado;
- Business Start, Growth e Scale podem contratar;
- somente oportunidade aprovada, ativa, atualizada e capaz de atender demanda adicional poderá ser impulsionada.

### 6.2 Parâmetros candidatos

| Modalidade | Orçamento mínimo | Duração candidata |
|---|---:|---:|
| Boost Local | R$ 30,00 | 3 a 7 dias |
| Boost Regional | R$ 100,00 | 7 a 15 dias |
| Boost Ampliado | R$ 300,00 | 15 a 30 dias |
| Boost Gerenciado | a partir de R$ 1.000,00 | conforme contrato |

- CPM candidato: R$ 12,00 a R$ 25,00;
- CPC candidato: R$ 0,80 a R$ 2,50;
- uma campanha utiliza uma base principal, sem cobrança simultânea por CPM e CPC;
- orçamento pré-pago, limitado e sem renovação automática por padrão;
- atribuição por clique candidata de até sete dias;
- atribuição por visualização desativada inicialmente.

### 6.3 Experiência validada

- gate de entrada com bloqueios por plano, aprovação, atualização, capacidade, segurança e responsabilidade;
- objetivo único, sem seleção automática ou promessa de resultado;
- critérios utilizados e proibidos visíveis antes do envio;
- prévia separada de ranking e ordenação orgânicos;
- pausa automática por alteração material, orçamento, capacidade ou expiração;
- estados próprios para inelegibilidade, rejeição, esgotamento e reconciliação;
- Boost Social Financiado com financiador e beneficiário identificados;
- controles reversíveis de ocultação e preferência;
- baixa oferta orgânica reduz publicidade e nunca aumenta densidade;
- marcador e agrupamento próprios no Mapa;
- relatório separado em entrega, interação, atribuição candidata e autorrelato;
- pausa e cancelamento com consequência, saldo e histórico visíveis.

### 6.4 Fluxo visual do anunciante validado

A UXA-040 reformulada e a UXA-041 validam cinco estados para computador:

1. elegibilidade;
2. objetivo e critérios;
3. orçamento e duração;
4. prévia e confirmação;
5. envio para avaliação.

O conjunto demonstra:

- distinção entre `Atendido`, `Atendido com limite` e `Bloqueado`;
- critérios escolhidos e revisáveis;
- público insuficiente sem ampliação automática;
- base principal coerente com o objetivo;
- CPC para objetivo de clique no exemplo;
- primeiro resultado orgânico anterior ao espaço patrocinado;
- confirmação desmarcada;
- envio sem entrega;
- cancelamento com retorno ao rascunho e histórico preservado.

## 7. Proteções vigentes

- gratuito permanece útil;
- catálogo público permanece acessível;
- assinatura, transação e Boost permanecem separados;
- pessoa gratuita pode contratar atividade paga;
- plano pago não aumenta relevância, ranking, impacto ou evidência;
- Boost não compra aderência pessoal;
- compreensão inicial, Momento Atual e Próximo Passo não são usados para segmentação;
- preferência de ocultação não pode ser contornada;
- ausência de inventário orgânico não aumenta densidade publicitária;
- patrocinador ou financiador não recebe autoridade indevida;
- localização permanece opcional;
- cancelamento e retorno ao gratuito permanecem protegidos;
- Engenharia de Produto permanece pausada.

## 8. Limites vigentes

Não foram concluídos:

- cartão patrocinado e explicação como artefatos independentes;
- estados patrocinados para Lista e Mapa;
- wireframes de gestão da campanha ativa;
- wireframe do relatório agregado;
- validação do conjunto completo de wireframes;
- pesquisa de disposição a pagar;
- calibração de CPM, CPC, orçamento, densidade ou frequência;
- política jurídica, fiscal e contábil de publicidade;
- categorias finais e moderação operacional;
- custos de servir, margem e antifraude;
- cancelamento, devolução e disputa finais;
- algoritmo de entrega;
- perfil publicitário ou uso real de dados;
- checkout, gateway, faturamento ou cobrança;
- design, protótipo ou testes;
- piloto ou produção;
- Engenharia de Produto.

## 9. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar wireframes do cartão patrocinado e da explicação de distribuição;
2. criar estados patrocinados para Lista e Mapa;
3. criar wireframes de gestão da campanha ativa;
4. criar wireframe do relatório agregado;
5. validar funcionalmente o conjunto completo de wireframes do Opportunity Boost;
6. validar preços, orçamentos e disposição a pagar;
7. definir política especializada de publicidade e categorias;
8. retomar a referência móvel da Home e a transição para a primeira Tela Hoje;
9. retomar independentemente os testes dos Resultados Empresariais.
