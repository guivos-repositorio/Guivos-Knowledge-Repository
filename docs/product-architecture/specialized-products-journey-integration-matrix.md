---
id: GPA-SPECIALIZED-JOURNEY-MATRIX-001
title: Matriz de Integração dos Produtos Especializados com as Jornadas
status: consolidated
version: 2.0.0
owner: Guivos
last_updated: 2026-08-08
depends_on:
  - GPA-000
  - GLPA-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
related:
  - GPA-001
  - GPA-002
  - GPA-003
  - GPA-004
  - GPA-005
  - GPA-006
  - GPA-007
  - UXA-101
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
normative: true
---

# Matriz de Integração dos Produtos Especializados com as Jornadas

## 1. Finalidade

Esta matriz reconcilia os sete Produtos Especializados com as jornadas vigentes sem transformar produto em participante, participante em produto ou relação conceitual em tela/transição implementada.

Ela substitui como baseline de trabalho qualquer leitura anterior que atribuía automaticamente as superfícies de Organização ao Guivos Business.

## 2. Separações canônicas

```text
Pessoa / Coletivo / Organização
= papéis estruturais de participante

Journey / Mall / Travel / Business / Media / Intelligence / Ads
= Produtos Especializados/camadas de produto
```

Consequentemente:

- Organização ≠ Guivos Business;
- jornada de Organização ≠ jornada de Business;
- oportunidade publicada por Organização ≠ Guivos Business;
- `TRN-203` é continuidade institucional → descoberta no Journey e **não prova contratação do Guivos Business**;
- planos de Organização são `Conecta · Eleva · Transforma`;
- tiers do Guivos Business são `Start · Growth · Scale · Enterprise`;
- `BND-002` é fronteira genérica de contratação/dimensionamento assistido e não pertence a Business por definição;
- Parceria Estratégica corporativa da Guivos não é Produto Especializado nem quarto tipo de participante.

## 3. Baseline dos sete produtos

| Produto | Camada | Responsabilidade predominante | Relação atual com jornadas | Maturidade de integração |
|---|---|---|---|---|
| Guivos Journey | Experience | experiência unificada, controle apresentado, descoberta e continuidade | host principal das jornadas canônicas | alta materialização documental |
| Guivos Mall | Service | comércio curado de produtos, serviços e ativos transacionáveis | relação arquitetural com Journey; handoff dedicado ainda ausente | conceitual/incompleta |
| Guivos Travel | Service | viagens, experiências, planejamento e reservas | relação arquitetural com Journey; handoff dedicado ainda ausente | conceitual/incompleta |
| Guivos Business | Service | produto B2B contratado para contextos empresariais/institucionais de maior complexidade | pode estruturar jornadas/capacidades próprias; não é proprietário automático das superfícies de Organização | produto consolidado; integração experiencial própria incompleta |
| Guivos Media | Service | produção, organização e distribuição editorial/institucional | pode abastecer Journey e demais produtos; contexto editorial próprio não está consolidado em SURF/TRN | embutida/conceitual |
| Guivos Intelligence | Intelligence | inteligência do ecossistema, interpretação, análise e recomendações governadas | apoio transversal; não exige navegação própria | forte conceitualmente; majoritariamente implícita |
| Guivos Ads | Service | publicidade, mídia patrocinada, ativações e Opportunity Boost | `COM-001..005`, `TRN-301..306`; exposição patrocinada integrada parcialmente a superfícies Journey | materialização documental forte; handoffs parciais |

## 4. Participante × produto

A existência de um participante não ativa automaticamente um Produto Especializado.

| Participante | Produto automático? | Regra |
|---|---|---|
| Pessoa | Journey como host experiencial | outras capacidades entram somente quando o contexto exigir |
| Coletivo | Journey como host experiencial | Ads/Mall/Travel/Media/Intelligence podem apoiar; Business não é presumido |
| Organização | Journey/experiência institucional do ecossistema | Business somente mediante contexto/contrato especializado separado |

Uma Organização pode simultaneamente:

1. existir como participante e publicar oportunidades para Pessoas/Coletivos;
2. contratar Guivos Business para uma necessidade B2B própria;
3. anunciar via Guivos Ads quando elegível;
4. comprar/usar Mall ou Travel;
5. consumir intelligence autorizada.

Essas relações possuem objetos, contratos e métricas distintos.

## 5. Matriz de situações vigentes

| Situação | Host visível | Responsável especializado | Apoios | Evidência | Leitura correta |
|---|---|---|---|---|---|
| Pessoa — entrada/compreensão/Hoje | Journey | Journey | Intelligence/Platform | `PER-001..008`; `TRN-001..007` | Journey |
| Pessoa — descoberta de oportunidades | Journey | Journey | Intelligence; Ads se patrocinado | `PER-201..203`; `TRN-203/204/210/211` | oportunidade pode ter origem em Organização; não implica Business |
| Pessoa — participação em Coletivos | Journey | Journey | capacidades aplicáveis | `PER-101..108`; `COL-*` | Coletivo é participante, não produto |
| Pessoa — planos | Journey | Journey | billing/plataforma | `PER-301..304` | Free/Plus/Pro |
| Coletivo — operação | Journey | Journey | Intelligence/Ads conforme caso | `COL-*` | não atribuir a Business |
| Coletivo — planos | Journey | Journey | billing/plataforma | `COL-301..304` | Livre/Mobiliza/Impacta/Rede; BND-002 genérico |
| Organização — identidade/visão/operação | experiência Guivos | jornada de Organização | Intelligence/Platform conforme finalidade | `ORG-001..007` | **não é Guivos Business por padrão** |
| Organização — publicação de oportunidade | experiência Guivos | Organização como participante/publicador | Journey para descoberta; Ads se impulsionada | `ORG-002/003`; `TRN-203` | Organization → Journey, não Business → Journey |
| Organização — planos | experiência Guivos | jornada de Organização | billing/plataforma | `ORG-301..304` | Conecta/Eleva/Transforma; não Start/Growth/Scale |
| Contrato B2B especializado | experiência a definir por caso | Guivos Business | Journey, Intelligence, Mall, Travel, Media, Ads | produto `GPA-004`; SURF/TRN dedicados insuficientes | integração própria pendente |
| Opportunity Boost | experiência Guivos | Ads | Journey; Intelligence; identidade do anunciante conforme autoridade | `COM-001..005`; `TRN-301..306` | Ads é operador econômico/publicitário; anunciante não vira Business |
| Compra de item/serviço | a definir no handoff | Mall | Journey/Intelligence/Platform | sem família dedicada vigente | gap real |
| Planejamento/reserva de viagem | a definir no handoff | Travel | Journey/Intelligence/Media/Platform | sem família dedicada vigente | gap real |
| Conteúdo editorial | Journey quando embutido; Media quando contexto próprio | Media | Intelligence/Ads conforme finalidade | sem família dedicada própria | fronteira visual pendente |

## 6. Handoffs comprovados e não comprovados

### 6.1 Continuidade institucional → Journey

```text
Organização publica/ativa oportunidade
→ TRN-203
→ inventário elegível de descoberta no Journey
```

`TRN-203` está validada no limite documentado pela Arquitetura da Experiência.

Esse handoff é **Organização como participante/publicador → Journey**, não Guivos Business → Journey.

### 6.2 Ads → Journey

- `TRN-304`: patrocinado → Mapa, parcial;
- `TRN-306`: patrocinado → Lista, parcial;
- `TRN-305`: campanha → estado residual, parcial embora os estados residuais estejam validados.

### 6.3 Journey → Mall

Previsto arquiteturalmente, sem contrato `SURF/TRN` dedicado suficiente.

Não usar `BND-001` se Mall continuar sob autoridade Guivos. Não inventar checkout, carrinho, pedido, pagamento ou retorno.

### 6.4 Journey → Travel

Previsto arquiteturalmente, sem contrato `SURF/TRN` dedicado suficiente.

Não usar `BND-001` se Travel continuar sob autoridade Guivos. Reserva externa de terceiro poderá possuir fronteira própria somente quando a autoridade correspondente for definida.

### 6.5 Journey/Organização → Guivos Business

Não existe na baseline atual um handoff canônico suficiente que prove quando uma Organização deixa uma capacidade institucional comum e inicia uma experiência de Guivos Business contratado.

`BND-002` não preenche essa lacuna automaticamente.

## 7. Business — contrato de separação

Guivos Business pode atender uma Organização, mas não absorve sua identidade no ecossistema.

```text
Organização A
├── papel participante → oportunidades/programas/relacionamentos permitidos
└── contrato separado → Guivos Business, se houver
```

O mesmo ator jurídico pode exercer as duas relações, que devem permanecer rastreáveis separadamente.

A futura experiência Business deverá identificar, quando material:

- contrato/produto ativo;
- escopo e capacidades;
- público beneficiado;
- autoridade do administrador;
- dados utilizados;
- integrações;
- resultados e métricas;
- limites;
- retorno à jornada institucional comum;
- encerramento do contrato sem apagar a Organização participante.

## 8. Intelligence — apoio transversal

Intelligence pode apoiar qualquer produto autorizado sem que isso gere uma transição navegacional.

Quando sua participação afetar materialmente decisão, personalização ou explicação, deverão ser preservados:

- fonte/proveniência;
- finalidade;
- estado observado vs inferido;
- incerteza;
- autoridade;
- correção/contestação aplicável.

## 9. Media — conteúdo embutido vs produto percebido

Conteúdo do Media pode aparecer dentro do Journey sem handoff quando o host e a decisão principal continuam sendo Journey.

Um contexto editorial próprio somente deve receber superfície/transição distinta se houver mudança material de responsabilidade, navegação, dados, consequência, recuperação ou expectativa do participante.

## 10. Mall e Travel — transação não presumida

A arquitetura reconhece os produtos, mas a experiência transacional completa não está materializada nas jornadas atuais.

Não presumir:

- catálogo implementado;
- carrinho;
- checkout;
- reserva;
- estoque;
- pagamento;
- confirmação;
- cancelamento/reembolso;
- integração de terceiro;
- comissão;
- disponibilidade operacional.

## 11. Registro de gaps P8

| Gap | Descrição | Prioridade arquitetural |
|---|---|---|
| SP-GAP-001 | Journey → Mall sem contrato canônico de handoff | futura UXA específica |
| SP-GAP-002 | Journey → Travel sem contrato canônico de handoff | futura UXA específica |
| SP-GAP-003 | Media embutido vs contexto editorial próprio | política de representação antes de materialização |
| SP-GAP-004 | Guivos Business sem handoff próprio claramente separado da jornada de Organização | **alta; evitar regressão Organização=Business** |
| SP-GAP-005 | proveniência/explicabilidade de Intelligence não uniforme por superfície | evolução transversal |
| SP-GAP-006 | página Ads ainda precisa refletir completamente a maturidade UXA já atingida | corrigir no rebaseline P8 |
| SP-GAP-007 | registros SURF/TRN não possuem coluna nativa de produto | usar esta matriz; mudar schema somente se houver necessidade real |
| SP-GAP-008 | handoff interno vs fronteira externa | governado pela política P8 |
| SP-GAP-009 | `BND-002` pode ser indevidamente reutilizado como proxy de Business | proibir associação automática |
| SP-GAP-010 | entitlement de Opportunity Boost para planos atuais de Organização não está reconciliado | autoridade econômica futura; não inventar |

## 12. Princípio de representação

Mudança de produto **não cria automaticamente tela**.

Nova superfície/transição somente é justificável quando houver mudança material em uma ou mais dimensões:

- responsabilidade;
- autoridade;
- decisão principal;
- dados/contexto;
- consequência;
- risco;
- expectativa;
- navegação/canal;
- retorno/recuperação.

## 13. Efeito sobre UXA

P8 é uma reconciliação arquitetural de produtos.

Não cria:

- novo `SURF`;
- novo `TRN`;
- novo SVG;
- nova UXA;
- promoção de jornada;
- implementação.

UXA-102/V5 permanecem não iniciadas e Engenharia de Produto permanece pausada.

## 14. Estado

`specialized_products_rebaselined_against_current_participant_and_plan_authority`.
