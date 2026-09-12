---
id: GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
title: Dashboard Guivos — Documento Mestre de Especificação Analítica e Handoff Replit
status: active
version: 0.1.3
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_pre_implementation_dashboard_master
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GKR-STATE-001
  - GPA-006
  - GAI-001
  - GAI-002
  - GIA-COG-001
  - GEM-009-MEASUREMENT-CONTRACT-001
related:
  - GEA-GRAPH-REFERENCE-001
---

# Dashboard Guivos — Documento Mestre de Especificação Analítica e Handoff Replit

## 1. Finalidade

Este documento é o **Anexo A** de `GKR-INTELLIGENCE-DASHBOARD-KPI-001` e governa, em nível documental pré-implementação, o **Dashboard Guivos**.

O Dashboard Guivos é a superfície analítica interna de visão transversal do ecossistema e da empresa Guivos. Seu objetivo é permitir compreensão executiva e operacional sobre crescimento, participantes, Journey, oportunidades, relações, produtos, economia, território, Ads em nível resumido, qualidade e demais dimensões legitimamente disponíveis.

Ele não é:

- source of truth;
- banco de dados;
- ferramenta de investigação irrestrita de Pessoas;
- dashboard Business;
- dashboard de Organização;
- dashboard de Coletivo;
- dashboard pessoal;
- substituto do Guivos Intelligence;
- autorização de uso de dados reais;
- autorização de implementação.

Regra central:

> **O Dashboard Guivos deve oferecer a visão mais completa necessária à governança do ecossistema sem transformar acesso interno em acesso irrestrito a dados individuais.**

---

## 2. Estado e boundary

```text
GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
→ ACTIVE
→ PRE-IMPLEMENTATION DASHBOARD MASTER

DASHBOARD GUIVOS
→ DOCUMENTARILY SPECIFIED
→ INTERNAL GUIVOS ANALYTICS SURFACE

REAL DATA CONNECTION
→ NOT AUTHORIZED BY THIS DOCUMENT

REPLIT BUILD
→ NOT AUTHORIZED BY THIS DOCUMENT
→ HANDOFF SPECIFICATION ONLY

PERSON-LEVEL PRIVATE CONTEXT
→ NOT PART OF DEFAULT DASHBOARD DISCLOSURE

ECONOMIC KPIs
→ REQUIRE COMPOSITION WITH GEM-009
```

Este documento define o que o dashboard deverá ser capaz de representar quando os respectivos contratos, fontes e gates estiverem autorizados. Ele não declara que todos os dados, eventos, relações ou produtos já existem operacionalmente.

---

## 3. Público e classes de acesso

O Dashboard Guivos é destinado a usuários internos autorizados da Guivos.

As classes abaixo são **funcionais**, não roles técnicas implementadas:

| Classe funcional | Escopo esperado |
|---|---|
| Visão executiva | indicadores agregados transversais e tendências estratégicas |
| Operação / Produto | métricas dos domínios sob responsabilidade |
| Growth / GTM | aquisição, ativação, canais e crescimento autorizados |
| Economia / Financeiro | métricas econômicas e transacionais autorizadas |
| Data / Intelligence | análise, qualidade, proveniência e outputs necessários à finalidade autorizada |
| Privacidade / Governança | controles, qualidade de disclosure, auditoria e exceções pertinentes |

Princípio de acesso:

```text
SER INTERNO DA GUIVOS
≠ TER ACESSO A TODO DADO

VISÃO EXECUTIVA
≠ CONTEXTO PRIVADO INDIVIDUAL

DATA / INTELLIGENCE ACCESS
≠ DISCLOSURE IRRESTRITO
```

Qualquer acesso individualizado excepcional deve possuir finalidade, autoridade e trilha próprias; ele não deve ser inferido da existência deste dashboard.

---

## 4. Arquitetura funcional do dashboard

O Dashboard Guivos deve ser organizado em **onze áreas analíticas principais**:

1. Visão Executiva;
2. População e Participantes;
3. Aquisição, Ativação e Retenção;
4. Journey, Próximos Passos e Experiências;
5. Oportunidades e Supply;
6. Relações e Ecossistema;
7. Produtos e Adoção;
8. Economia e Planos;
9. Território e Demografia;
10. Ads / Opportunity Boost — resumo interno;
11. Qualidade, Freshness e Governança do Dado.

Uma área pode permanecer parcial ou integralmente indisponível enquanto seus contratos não estiverem prontos.

```text
SEÇÃO DOCUMENTADA
≠ DADO OPERACIONAL DISPONÍVEL
```

---

## 5. Convenções de KPI e status

Prefixo deste master:

```text
GUV-KPI-<FAMÍLIA>-NNN
```

Famílias iniciais:

- `POP` — população e participantes;
- `ENG` — aquisição, ativação, retenção e uso;
- `JNY` — Journey e experiência;
- `OPP` — oportunidades e supply;
- `REL` — relações e Graph Analytics;
- `PRD` — produtos e adoção;
- `ECO` — economia, planos e transações;
- `GEO` — território e demografia;
- `ADS` — resumo Ads / Opportunity Boost;
- `DQ` — data quality, freshness e governança.

Os IDs identificam contratos analíticos candidatos. Um ID não significa implementação.

### 5.1 Vocabulário de status

Este documento usa exclusivamente o vocabulário do master global:

| Status | Semântica |
|---|---|
| `proposed` | necessidade/definição candidata ainda incompleta; não build-ready |
| `source_pending` | definição lógica suficientemente delimitada para continuar, mas source/data contract ou equivalente ainda impede readiness |
| `defined` | contrato mínimo transversal documentalmente preenchido; ainda não significa implementação autorizada |
| `approved-equivalent` | autoridade especializada aplicável fornece estado equivalente aceito pelo gate governado |

Regras:

```text
PROPOSED
→ NÃO IMPLEMENTAR COMO KPI CANÔNICO

SOURCE_PENDING
→ NÃO IMPLEMENTAR COM DADO REAL

DEFINED
→ AINDA REQUER CONTRATOS DE DOMÍNIO + BUILD AUTHORIZATION
```

Na versão `v0.1.3`, **nenhum KPI deste catálogo é declarado `defined` ou `approved-equivalent` por inferência**.

---

## 6. Família POP — População e participantes

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-POP-001 | Pessoas cadastradas | contagem distinta da entidade Pessoa no universo válido corrente | pessoas | source_pending | participant source + validade/exclusões |
| GUV-KPI-POP-002 | Novas Pessoas | Pessoas cuja criação válida ocorreu no período | pessoas/período | source_pending | participant source + temporal contract |
| GUV-KPI-POP-003 | Pessoas ativas | Pessoas com ≥1 evento do `ACTIVITY_EVENT_SET` aprovado na janela | pessoas | proposed | activity event set + janela + source |
| GUV-KPI-POP-004 | Pessoas inativas | Pessoas elegíveis sem evento qualificante na janela | pessoas | proposed | activity/inactivity contract |
| GUV-KPI-POP-005 | Taxa de ativação de Pessoas | Pessoas que atingiram ativação / Pessoas elegíveis | % | proposed | activation event + denominator |
| GUV-KPI-POP-006 | Crescimento líquido de Pessoas | novas Pessoas válidas − saídas/desativações válidas | pessoas/período | proposed | exit/deactivation contract |
| GUV-KPI-POP-007 | Organizações cadastradas | contagem distinta de Organizações válidas | organizações | source_pending | organization source + validade |
| GUV-KPI-POP-008 | Organizações ativas | Organizações com atividade qualificante | organizações | proposed | organization activity contract |
| GUV-KPI-POP-009 | Coletivos cadastrados | contagem distinta de Coletivos válidos | coletivos | source_pending | collective source + validade |
| GUV-KPI-POP-010 | Coletivos ativos | Coletivos com atividade qualificante | coletivos | proposed | collective activity contract |
| GUV-KPI-POP-011 | Mix de participantes | distribuição Pessoa / Organização / Coletivo no universo aplicável | % | source_pending | sources + denominator + scope |
| GUV-KPI-POP-012 | Taxa de reativação | entidades previamente inativas que retornam / inativas elegíveis | % | proposed | reactivation contract |

### 6.1 Necessidade candidata preservada — escolhas / declarações das Pessoas

O inventário global preserva como necessidade candidata a possibilidade de leituras relacionadas a **escolhas e declarações das Pessoas**. Este Anexo A mantém essa necessidade como proveniência de escopo, sem promovê-la a KPI, data contract ou autorização de disclosure.

```text
ESCOLHAS / DECLARAÇÕES DAS PESSOAS
→ CANDIDATE NEED PRESERVED
→ BLOCKED / NOT BUILD-READY
→ KPI ID = NOT ASSIGNED
→ FORMULA = NOT ADJUDICATED
→ SOURCE = NOT ADJUDICATED
→ POPULATION / DENOMINATOR = NOT ADJUDICATED
→ ACCESS / DISCLOSURE = NOT ADJUDICATED
→ REPLIT MUST NOT INFER IMPLEMENTATION
```

Qualquer futura materialização deverá ser precedida pela adjudicação das autoridades aplicáveis de Pessoa, Journey, Privacidade e Dados, incluindo finalidade, natureza da evidência, população, granularidade, retenção e disclosure.

O Replit **não pode decidir sozinho** o que significa `ativo`.

```text
LOGIN
≠ NECESSARIAMENTE ATIVIDADE RELEVANTE

CADASTRO EXISTENTE
≠ USUÁRIO ATIVO
```

---

## 7. Família ENG — Aquisição, ativação e retenção

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-ENG-001 | Conclusão de cadastro | cadastros concluídos / cadastros iniciados | % | proposed | event contract + denominator |
| GUV-KPI-ENG-002 | Tempo até ativação | tempo entre elegibilidade inicial e evento de ativação | tempo | proposed | activation event |
| GUV-KPI-ENG-003 | WAU | Pessoas únicas ativas em janela móvel de 7 dias | pessoas | proposed | activity event set |
| GUV-KPI-ENG-004 | MAU | Pessoas únicas ativas em janela móvel de 30 dias | pessoas | proposed | activity event set |
| GUV-KPI-ENG-005 | Stickiness WAU/MAU | `WAU / MAU` | razão/% | proposed | ENG-003/004 definidos |
| GUV-KPI-ENG-006 | Retenção D7 | coorte ativada com atividade qualificante na janela D7 / coorte ativada | % | proposed | cohort + activity contract |
| GUV-KPI-ENG-007 | Retenção D30 | coorte ativada com atividade qualificante na janela D30 / coorte ativada | % | proposed | cohort + activity contract |
| GUV-KPI-ENG-008 | Retenção D90 | coorte ativada com atividade qualificante na janela D90 / coorte ativada | % | proposed | cohort + activity contract |
| GUV-KPI-ENG-009 | Taxa de reengajamento | inativos elegíveis que retornam / inativos elegíveis | % | proposed | inactivity + reengagement contract |
| GUV-KPI-ENG-010 | Origem de aquisição | distribuição de novos participantes por source/medium/campaign autorizado | distribuição | proposed | attribution contract |

`Churn` não deve ser usado como sinônimo universal de inatividade. Somente usar churn quando cancelamento/abandono possuir definição própria.

---

## 8. Família JNY — Journey e experiência

Este conjunto deve preservar a centralidade humana e evitar transformar evolução em score universal.

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-JNY-001 | Pessoas com Journey iniciada | Pessoas com evento legítimo de início de Journey | pessoas | proposed | event contract |
| GUV-KPI-JNY-002 | Pessoas com Momento atualizado | Pessoas com atualização válida de Momento no período | pessoas | proposed | Moment source + validity |
| GUV-KPI-JNY-003 | Objetivos ativos | objetivos em estado válido ativo | objetivos | proposed | objective state contract |
| GUV-KPI-JNY-004 | Próximos Passos ativos | próximos passos em estado válido ativo | próximos passos | proposed | state contract |
| GUV-KPI-JNY-005 | Próximos Passos concluídos | próximos passos concluídos no período | próximos passos | proposed | completion event contract |
| GUV-KPI-JNY-006 | Taxa de conclusão de Próximos Passos | concluídos / próximos passos elegíveis | % | proposed | denominator + exclusions |
| GUV-KPI-JNY-007 | Experiências iniciadas | experiências com início válido | experiências | proposed | event contract |
| GUV-KPI-JNY-008 | Experiências concluídas | experiências com conclusão válida | experiências | proposed | event contract |
| GUV-KPI-JNY-009 | Evidências registradas | evidências válidas registradas | evidências | proposed | evidence validity/source |
| GUV-KPI-JNY-010 | Distribuição por Domínio de Evolução | distribuição candidata por Domínio de Evolução, incluindo estados não mapeados/sem domínio conforme autoridade vigente | distribuição | proposed | buckets + population + denominator + null/unmapped treatment + source/disclosure |
| GUV-KPI-JNY-011 | Participação recorrente | Pessoas com participação qualificante em ≥2 períodos definidos | pessoas/% | proposed | recurrence/window contract |

Para `GUV-KPI-JNY-010`, a futura adjudicação dos buckets deve preservar explicitamente, conforme as autoridades vigentes, os nove `JED-*`, **`Ainda estou descobrindo`**, `other_unmapped` e `null / sem domínio associado`. Esta versão não define o denominador, a forma de agregação, o tratamento de `null`, a ordem dos buckets ou o disclosure; por isso o KPI permanece `proposed`.

Guardrails:

```text
MAIS PRÓXIMOS PASSOS CONCLUÍDOS
≠ PESSOA MELHOR

MAIS ATIVIDADE
≠ MAIS EVOLUÇÃO

EXPERIÊNCIA CONCLUÍDA
≠ IMPACTO COMPROVADO
```

---

## 9. Família OPP — Oportunidades e supply

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-OPP-001 | Oportunidades criadas | oportunidades válidas criadas no período | oportunidades | source_pending | opportunity source + validity |
| GUV-KPI-OPP-002 | Oportunidades publicadas | oportunidades que atingiram estado publicado | oportunidades | proposed | state contract |
| GUV-KPI-OPP-003 | Oportunidades ativas | oportunidades no estado ativo | oportunidades | proposed | active-state contract |
| GUV-KPI-OPP-004 | Oportunidades encerradas | oportunidades encerradas no período | oportunidades | proposed | closed-state contract |
| GUV-KPI-OPP-005 | Visualizações | eventos válidos de visualização | eventos | proposed | event contract |
| GUV-KPI-OPP-006 | Interesses / salvamentos | eventos válidos de interesse | eventos/pessoas | proposed | event contract |
| GUV-KPI-OPP-007 | Inscrições / aplicações | inscrições válidas associadas a oportunidades | inscrições | proposed | event/status contract |
| GUV-KPI-OPP-008 | Compras / vendas | transações válidas atribuídas a oportunidades | transações | proposed | GEM-009 + transaction/attribution |
| GUV-KPI-OPP-009 | Participações iniciadas | participações válidas iniciadas | participações | proposed | participation contract |
| GUV-KPI-OPP-010 | Participações concluídas | participações concluídas | participações | proposed | completion contract |
| GUV-KPI-OPP-011 | Conversão view → interesse | Pessoas com interesse / Pessoas com view elegível | % | proposed | funnel population rules |
| GUV-KPI-OPP-012 | Conversão interesse → inscrição | inscrições / interesses elegíveis | % | proposed | funnel population rules |
| GUV-KPI-OPP-013 | Conversão inscrição → transação | transações / inscrições elegíveis | % | proposed | GEM-009 + attribution |
| GUV-KPI-OPP-014 | Conversão transação → participação | participações iniciadas / transações elegíveis | % | proposed | GEM-009 + transaction eligibility + participation contract |
| GUV-KPI-OPP-015 | Conclusão de participação | participações concluídas / iniciadas elegíveis | % | proposed | participation contract |
| GUV-KPI-OPP-016 | Taxa de preenchimento | capacidade ocupada / capacidade disponibilizada | % | proposed | capacity contract |
| GUV-KPI-OPP-017 | Tempo até primeiro engajamento | publicação → primeiro evento qualificante | tempo | proposed | event contract |
| GUV-KPI-OPP-018 | Supply por Domínio | oportunidades ativas por `JED-*` | distribuição | proposed | state + domain mapping |
| GUV-KPI-OPP-019 | Supply por território | oportunidades ativas por geografia autorizada | distribuição | proposed | geography/disclosure contract |

`Venda`, `transação`, `inscrição`, `participação` e `conclusão` são eventos distintos e não devem ser colapsados. Qualquer KPI cujo denominador dependa de transação elegível deve compor com o contrato econômico aplicável.

---

## 10. Família REL — Relações e Graph Analytics

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-REL-001 | Relações Pessoa ↔ Organização | relações válidas correntes desse tipo | relações | proposed | relation contract |
| GUV-KPI-REL-002 | Relações Pessoa ↔ Coletivo | relações válidas correntes desse tipo | relações | proposed | relation contract |
| GUV-KPI-REL-003 | Relações Organização ↔ Coletivo | relações válidas correntes desse tipo | relações | proposed | relation contract |
| GUV-KPI-REL-004 | Novas relações | relações iniciadas no período | relações/período | proposed | relation lifecycle |
| GUV-KPI-REL-005 | Relações ativas | relações que satisfazem regra de atividade/validade | relações | proposed | active relation rule |
| GUV-KPI-REL-006 | Participantes conectados | participantes com ≥1 relação válida / participantes elegíveis | % | proposed | graph/relation contract |

Métricas como densidade, centralidade, comunidades, caminhos, padrões de conexão e isolated-node rate permanecem:

```text
GRAPH ANALYTICS CANDIDATE
→ NOT DEFAULT KPI
→ REQUIRE PURPOSE + INTERPRETATION + PRIVACY + VALIDATION CONTRACT
```

Nenhuma centralidade deve ser apresentada como importância humana, reputação ou valor da Pessoa.

---

## 11. Família PRD — Produtos e adoção

Produtos Especializados e Experience Layer devem continuar semanticamente distintos.

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-PRD-001 | Usuários ativos por produto | usuários únicos com evento qualificante por produto | usuários | proposed | product activity contract |
| GUV-KPI-PRD-002 | Adoção por produto | usuários que adotaram produto / população elegível | % | proposed | adoption event + denominator |
| GUV-KPI-PRD-003 | Uso cross-product | usuários ativos em ≥2 produtos no período | usuários/% | proposed | product activity contracts |
| GUV-KPI-PRD-004 | Distribuição de uso do ecossistema | participação relativa de atividade por produto/camada | distribuição | proposed | event normalization contract |

A lista de produtos/camadas deve vir das autoridades correntes do GKR, não ser hard-coded como verdade eterna no Replit.

---

## 12. Família ECO — Economia, planos e transações

Todos os KPIs desta seção exigem composição com `GEM-009-MEASUREMENT-CONTRACT-001` e demais autoridades econômicas aplicáveis.

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-ECO-001 | Planos vendidos | contratos/assinaturas válidas iniciadas no período | quantidade | proposed | GEM-009 + plan lifecycle |
| GUV-KPI-ECO-002 | Planos ativos | relações de plano ativas na referência | quantidade | proposed | GEM-009 + active contract |
| GUV-KPI-ECO-003 | Novas assinaturas | novas relações pagas válidas no período | quantidade | proposed | GEM-009 |
| GUV-KPI-ECO-004 | Cancelamentos | cancelamentos válidos no período | quantidade | proposed | GEM-009 + cancellation contract |
| GUV-KPI-ECO-005 | Receita | receita reconhecida segundo contrato econômico aplicável | moeda | proposed | GEM-009 + recognition rules |
| GUV-KPI-ECO-006 | MRR | receita mensal recorrente conforme contrato econômico | moeda/mês | proposed | GEM-009 |
| GUV-KPI-ECO-007 | ARR | anualização autorizada de receita recorrente | moeda/ano | proposed | GEM-009 |
| GUV-KPI-ECO-008 | Receita média por relação | receita aplicável / relações pagas elegíveis | moeda | proposed | GEM-009 + denominator |
| GUV-KPI-ECO-009 | Valor transacionado de oportunidades | soma de transações elegíveis associadas a oportunidades | moeda | proposed | GEM-009 + attribution |
| GUV-KPI-ECO-010 | Taxa de reembolso | reembolsos / base elegível definida | % | proposed | GEM-009 + denominator |
| GUV-KPI-ECO-011 | Mix de planos | distribuição de relações ativas por plano | % | proposed | GEM-009 + plan taxonomy |
| GUV-KPI-ECO-012 | Receita por produto | receita atribuível por Produto Especializado | moeda/distribuição | proposed | GEM-009 + attribution |

Nenhuma equivalência Pontos ↔ moeda deve ser inferida neste dashboard.

---

## 13. Família GEO — Território e demografia

Todas as leituras devem respeitar minimização, thresholds e finalidade.

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-GEO-001 | Pessoas por território | Pessoas agregadas por geografia autorizada | distribuição | proposed | disclosure + geography contract |
| GUV-KPI-GEO-002 | Organizações por território | Organizações agregadas por geografia | distribuição | proposed | geography contract |
| GUV-KPI-GEO-003 | Coletivos por território | Coletivos agregados por geografia | distribuição | proposed | geography contract |
| GUV-KPI-GEO-004 | Oportunidades por território | oportunidades por geografia | distribuição | proposed | opportunity + geography contract |
| GUV-KPI-GEO-005 | Distribuição demográfica autorizada | população agregada por dimensão legítima | distribuição | proposed | privacy/data/disclosure contract |
| GUV-KPI-GEO-006 | Completude geográfica | registros elegíveis com geografia utilizável / registros elegíveis | % | proposed | source + usability rule |

```text
MAPA
≠ AUTORIZAÇÃO DE PRECISÃO MÁXIMA

DADO GEOGRÁFICO DISPONÍVEL
≠ DADO GEOGRÁFICO EXIBÍVEL
```

---

## 14. Família ADS — Resumo Ads / Opportunity Boost

Esta é uma **área analítica principal de resumo interno**, mas o detalhamento deverá pertencer ao futuro master específico de Ads / Opportunity Boost.

| ID | Indicador | Definição candidata | Status | Dependência / gate principal |
|---|---|---|---|---|
| GUV-KPI-ADS-001 | Campanhas ativas | campanhas em estado ativo válido | proposed | Ads master + campaign state |
| GUV-KPI-ADS-002 | Investimento | valor elegível de spend no período | proposed | Ads master + GEM-009/economic contract |
| GUV-KPI-ADS-003 | Impressões | eventos válidos de impressão | proposed | Ads master + event contract |
| GUV-KPI-ADS-004 | Cliques | eventos válidos de clique | proposed | Ads master + event contract |
| GUV-KPI-ADS-005 | Conversões | eventos de conversão atribuídos conforme contrato | proposed | attribution contract |
| GUV-KPI-ADS-006 | CTR | cliques elegíveis / impressões elegíveis | proposed | Ads master + denominator rules |
| GUV-KPI-ADS-007 | CPA | spend elegível / aquisições/conversões elegíveis | proposed | Ads + attribution + economic contract |
| GUV-KPI-ADS-008 | ROAS | retorno atribuível / spend elegível | proposed | attribution + economic contract |

```text
BOOSTED PERFORMANCE
≠ IMPACTO CAUSAL COMPROVADO

CORRELAÇÃO
≠ CAUSALIDADE
```

---

## 15. Família DQ — Qualidade, freshness e governança

| ID | Indicador | Definição lógica candidata | Unidade | Status | Dependência / gate principal |
|---|---|---|---|---|---|
| GUV-KPI-DQ-001 | Freshness compliance | datasets/contratos dentro do SLA / datasets monitorados | % | proposed | SLA/source contract |
| GUV-KPI-DQ-002 | Completude de campos críticos | campos críticos preenchidos / esperados | % | proposed | data contract |
| GUV-KPI-DQ-003 | Taxa de duplicidade | duplicados confirmados / registros avaliados | % | proposed | data quality contract |
| GUV-KPI-DQ-004 | Indicadores indisponíveis | KPIs esperados sem dado utilizável na janela | quantidade | proposed | expected registry + availability rules |
| GUV-KPI-DQ-005 | Supressões de disclosure | células/segmentos ocultados por proteção | quantidade | proposed | disclosure policy/engine |
| GUV-KPI-DQ-006 | KPIs com fonte vencida | KPIs cujo freshness ultrapassou limite | quantidade | proposed | freshness contract |

Esses indicadores qualificam confiança na leitura; não devem criar aparência de precisão onde o dado é insuficiente.

---

## 16. Filtros globais

Filtros candidatos:

- período;
- comparação de período;
- tipo de participante;
- Produto Especializado / camada;
- Domínio de Evolução;
- país / região / estado / cidade quando autorizado;
- tipo/categoria de oportunidade;
- plano, quando economicamente definido;
- source / medium / campaign quando houver attribution contract;
- estado de atividade;
- Organização / Coletivo somente quando a autoridade permitir o recorte.

```text
FILTRO DISPONÍVEL NA UI
→ DEVE SER SUBCONJUNTO DO ACCESS SCOPE
```

O cliente não pode ampliar escopo enviando filtros arbitrários ao serving/backend.

---

## 17. Drill-down

```text
N0 — ECOSSISTEMA
→ N1 — FAMÍLIA / DOMÍNIO
→ N2 — SEGMENTO / TERRITÓRIO / PRODUTO
→ N3 — OBJETO OPERACIONAL AUTORIZADO
```

Pessoa individual não é nível padrão de drill-down.

Qualquer drill-down individual futuro exige autoridade separada e finalidade específica.

---

## 18. Contrato de visualização semântica

Este documento não define UI visual final, mas orienta a escolha semântica futura:

| Necessidade | Visualização semântica candidata |
|---|---|
| valor atual | KPI card + contexto temporal |
| tendência | série temporal |
| composição | barras / stacked / distribuição |
| funil | funnel ou etapas sequenciais com taxas |
| coorte | matriz/cohort chart |
| território | mapa somente com granularidade autorizada |
| ranking operacional | tabela ordenada quando não implicar ranking humano |
| relações | visualização Graph somente quando necessária e protegida |
| qualidade | status table / health indicators |

Regras:

- não usar gráfico apenas porque há dado;
- todo valor temporal deve mostrar janela;
- `%` deve indicar denominador;
- nulo, zero, dado insuficiente e indisponível são estados distintos;
- inferências e predições devem ser qualificadas;
- comparações devem explicitar baseline.

---

## 19. Estados obrigatórios

```text
LOADING
NO_DATA
INSUFFICIENT_DATA
SUPPRESSED_BY_POLICY
SOURCE_DELAYED
ERROR
AVAILABLE
```

`0` não pode substituir `NO_DATA`.

`SUPPRESSED_BY_POLICY` não deve ser apresentado como erro técnico.

---

## 20. Data contracts lógicos esperados

Sem definir schema físico, o Dashboard Guivos deverá poder consumir contratos lógicos equivalentes a:

- Participant Aggregate;
- Participant Activity Aggregate;
- Journey Aggregate;
- Opportunity Aggregate;
- Opportunity Funnel Aggregate;
- Relationship Aggregate;
- Product Usage Aggregate;
- Economic Aggregate;
- Geography/Demography Aggregate;
- Ads Summary Aggregate;
- Data Quality / Freshness Status;
- Graph Analytics Output, quando autorizado;
- Intelligence Output, quando autorizado.

Cada payload deverá carregar, quando aplicável:

- `metric_id`;
- `as_of`;
- `period_start` / `period_end`;
- `value`;
- `unit`;
- `dimensions`;
- `population_scope`;
- `source_version`;
- `freshness`;
- `evidence_nature`;
- `access_class`;
- `suppression_state`;
- `confidence` quando material;
- `provenance_ref`.

---

## 21. Orientação específica para a AI do Replit

Quando a construção for autorizada, a AI do Replit deverá:

1. **não inventar métricas, fórmulas, tabelas, bancos ou permissões**;
2. usar `metric_id` como chave estável e não o label visual;
3. manter cálculos fora do componente visual quando pertencerem ao serving/analytics layer;
4. tratar filtros como restrição adicional, nunca como ampliação de acesso;
5. não confiar em `participant_id`, tenant ou role enviados somente pelo cliente;
6. não conectar diretamente o browser aos bancos de origem;
7. não armazenar credenciais/secrets no frontend;
8. separar mock adapters de real adapters;
9. exibir versão/freshness/proveniência quando exigido;
10. implementar `NO_DATA`, `INSUFFICIENT_DATA`, `SUPPRESSED_BY_POLICY` e `SOURCE_DELAYED` separadamente;
11. impedir exportação quando o contrato não permitir;
12. não habilitar drill-down para Pessoa por conveniência;
13. preservar timezone e janela temporal;
14. não inferir causalidade em labels, tooltips ou summaries;
15. não traduzir `inferido` para `fato`;
16. registrar a versão deste master usada na build;
17. manter componentes bloqueados/TBD claramente identificados em ambiente mock;
18. não promover mock data como dado real;
19. aceitar como build-ready apenas KPIs com status `defined` ou `approved-equivalent` **e** todos os contratos/gates aplicáveis satisfeitos.

---

## 22. Estrutura funcional sugerida para futura construção

Sem definir layout visual:

```text
DASHBOARD GUIVOS

1. CONTEXTO
→ período
→ freshness
→ access scope

2. EXECUTIVE OVERVIEW

3. POPULATION & PARTICIPANTS

4. GROWTH & ENGAGEMENT

5. JOURNEY & EXPERIENCES

6. OPPORTUNITIES & SUPPLY

7. RELATIONSHIPS & ECOSYSTEM

8. PRODUCTS

9. ECONOMY

10. TERRITORY / DEMOGRAPHY

11. ADS SUMMARY

12. DATA QUALITY / GOVERNANCE
```

`CONTEXTO` é moldura operacional da leitura; as **onze áreas analíticas** são os itens 2–12.

A ordem pode ser refinada por Design futuro sem alterar o significado dos contratos.

---

## 23. Critérios de aceite documental para futuro handoff

Antes de declarar qualquer release `READY FOR BUILD`:

```text
[ ] cada KPI selecionado = defined OU approved-equivalent
[ ] todas as dependências/gates do KPI estão satisfeitas
[ ] população e período estão definidos
[ ] access scope está definido
[ ] source/data contract está definido
[ ] regras de supressão estão definidas quando aplicáveis
[ ] filtros permitidos estão definidos
[ ] drill-down permitido está definido
[ ] exportação está definida
[ ] null/zero/no-data estão definidos
[ ] freshness está definida
[ ] critérios de qualidade estão definidos
[ ] KPIs econômicos compõem com GEM-009
[ ] Ads metrics compõem com autoridade Ads aplicável
[ ] Graph Analytics possui finalidade e proteção próprias
[ ] mock vs real está explicitamente classificado
[ ] Design/build authorization foi emitida pelo gate aplicável
```

`proposed` e `source_pending` **não são estados suficientes para build canônico**.

---

## 24. Testes mínimos para futura implementação

A implementação, quando autorizada, deverá provar pelo menos:

1. nenhum usuário recebe dado fora do access scope;
2. alterar parâmetros de cliente não amplia acesso;
3. totais reconciliam com o contrato do KPI;
4. filtros preservam população e denominadores corretos;
5. timezone e fechamento temporal são consistentes;
6. zero, nulo e ausência de dados não são confundidos;
7. small-cell suppression funciona quando aplicável;
8. dados vencidos são sinalizados;
9. exportação respeita a política;
10. drill-down respeita autoridade;
11. proveniência é rastreável;
12. Graph/Intelligence outputs preservam natureza e explicabilidade;
13. mock data não aparece como produção;
14. métricas econômicas usam contratos econômicos vigentes;
15. nenhum texto automático afirma causalidade sem evidência adequada.

---

## 25. Itens explicitamente bloqueados nesta versão

```text
BACKEND FÍSICO
→ NOT DEFINED HERE

DATABASE SELECTION FOR DASHBOARD
→ NOT DEFINED HERE

API ENDPOINTS
→ NOT DEFINED HERE

TECHNICAL RBAC
→ NOT IMPLEMENTED

REAL DATA
→ NOT AUTHORIZED

PERSON-LEVEL INTERNAL EXPLORER
→ NOT AUTHORIZED BY THIS MASTER

CHOICES / DECLARATIONS ANALYTICS
→ CANDIDATE NEED PRESERVED
→ KPI / FORMULA / SOURCE / DISCLOSURE / DATA CONTRACT NOT ADJUDICATED
→ NOT BUILD-READY

FINAL VISUAL DESIGN
→ NOT AUTHORIZED BY THIS MASTER

REPLIT IMPLEMENTATION
→ NOT AUTHORIZED BY THIS MASTER
```

---

## 26. Handoff futuro

Quando autorizado, o pacote de construção deverá incluir:

1. `GKR-INTELLIGENCE-DASHBOARD-KPI-001` vigente;
2. este documento vigente;
3. registry dos KPI IDs selecionados;
4. contratos individuais correspondentes;
5. data/serving contracts;
6. access/disclosure matrix;
7. mock dataset aprovado ou integração real explicitamente autorizada;
8. Design System/especificação visual autorizada;
9. acceptance tests;
10. versão do pacote.

---

## 27. Estado final

```text
GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
→ v0.1.3
→ ACTIVE
→ ANNEX A OF GKR-INTELLIGENCE-DASHBOARD-KPI-001
→ GOVERNED PRE-IMPLEMENTATION DASHBOARD MASTER

DASHBOARD GUIVOS
→ SCOPE + KPI FAMILIES + ACCESS + INTEGRATION + REPLIT HANDOFF SPECIFIED DOCUMENTARILY

ANALYTICAL AREAS
→ 11

KPI STATUS VOCABULARY
→ ALIGNED WITH GLOBAL MASTER

CHOICES / DECLARATIONS OF PERSONS
→ CANDIDATE NEED PRESERVED
→ BLOCKED / NOT BUILD-READY

JNY-010 DOMAIN DISTRIBUTION
→ PROPOSED
→ MUST PRESERVE JED-* + DISCOVERY / UNMAPPED / NULL STATES UNTIL FORMAL ADJUDICATION

TRANSACTION-BASED FUNNEL KPIs
→ REQUIRE APPLICABLE ECONOMIC CONTRACT WHEN TRANSACTION ELIGIBILITY IS MATERIAL

KPI IMPLEMENTATION READINESS
→ NONE CLAIMED BY INFERENCE
→ PROPOSED / SOURCE_PENDING ITEMS REMAIN NOT BUILD-READY

REAL DATA / BACKEND / TECHNICAL RBAC / PRODUCTION
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

NEXT SPECIALIZED MASTER
→ REQUIRES SEPARATE GOVERNED ACT
```
