---
id: GKR-INTELLIGENCE-DASHBOARD-GUIVOS-001
title: Dashboard Guivos — Documento Mestre de Especificação Analítica e Handoff Replit
status: active
version: 0.1.0
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

O Dashboard Guivos é a superfície analítica interna de visão transversal do ecossistema e da empresa Guivos. Seu objetivo é permitir compreensão executiva e operacional sobre crescimento, participantes, Journey, oportunidades, relações, produtos, economia, território, qualidade e demais dimensões legitimamente disponíveis.

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

Este documento define o que o dashboard deverá ser capaz de representar quando os respectivos contratos, fontes e gates estiverem autorizados. Ele não declara que todos os dados ou produtos já existem operacionalmente.

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

Qualquer acesso individualizado excepcional deve possuir finalidade, autoridade e trilha própria; ele não deve ser inferido da existência deste dashboard.

---

## 4. Arquitetura funcional do dashboard

O Dashboard Guivos deve ser organizado em dez áreas analíticas principais:

1. Visão Executiva;
2. População e Participantes;
3. Aquisição, Ativação e Retenção;
4. Journey, Próximos Passos e Experiências;
5. Oportunidades e Supply;
6. Relações e Ecossistema;
7. Produtos e Adoção;
8. Economia e Planos;
9. Território e Demografia;
10. Qualidade, Freshness e Governança do Dado.

Uma área pode permanecer parcialmente indisponível enquanto seus contratos não estiverem prontos.

```text
SEÇÃO DOCUMENTADA
≠ DADO OPERACIONAL DISPONÍVEL
```

---

## 5. Convenções de KPI

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

Os IDs deste documento identificam contratos analíticos candidatos/definidos documentalmente. Um ID não significa implementação.

---

## 6. Família POP — População e participantes

### 6.1 Catálogo

| ID | Indicador | Definição lógica | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-POP-001 | Pessoas cadastradas | `COUNT(DISTINCT person_id)` no universo válido corrente | pessoas | DEFINED DOCUMENTARILY |
| GUV-KPI-POP-002 | Novas Pessoas | Pessoas cuja criação válida ocorreu no período | pessoas/período | DEFINED DOCUMENTARILY |
| GUV-KPI-POP-003 | Pessoas ativas | Pessoas com ≥1 evento pertencente ao `ACTIVITY_EVENT_SET` aprovado dentro da janela | pessoas | SOURCE/EVENT-SET PENDING |
| GUV-KPI-POP-004 | Pessoas inativas | Pessoas elegíveis sem evento qualificante na janela de atividade | pessoas | SOURCE/EVENT-SET PENDING |
| GUV-KPI-POP-005 | Taxa de ativação de Pessoas | Pessoas que atingiram o evento de ativação / Pessoas elegíveis para ativação | % | ACTIVATION EVENT PENDING |
| GUV-KPI-POP-006 | Crescimento líquido de Pessoas | novas Pessoas válidas − saídas/desativações válidas no período | pessoas/período | EXIT RULE PENDING |
| GUV-KPI-POP-007 | Organizações cadastradas | `COUNT(DISTINCT organization_id)` válido | organizações | DEFINED DOCUMENTARILY |
| GUV-KPI-POP-008 | Organizações ativas | Organizações com atividade qualificante segundo contrato próprio | organizações | ACTIVITY RULE PENDING |
| GUV-KPI-POP-009 | Coletivos cadastrados | `COUNT(DISTINCT collective_id)` válido | coletivos | DEFINED DOCUMENTARILY |
| GUV-KPI-POP-010 | Coletivos ativos | Coletivos com atividade qualificante segundo contrato próprio | coletivos | ACTIVITY RULE PENDING |
| GUV-KPI-POP-011 | Mix de participantes | participação percentual de Pessoa / Organização / Coletivo no universo aplicável | % | DEFINED DOCUMENTARILY |
| GUV-KPI-POP-012 | Taxa de reativação | entidades previamente inativas que retornaram a atividade / inativas elegíveis | % | REACTIVATION RULE PENDING |

### 6.2 Regra crítica de atividade

O Replit **não pode decidir sozinho** o que significa `ativo`.

Antes da implementação de POP-003, 004, 008, 010 e 012 deve existir um contrato explícito de eventos qualificantes, por tipo de participante.

```text
LOGIN
≠ NECESSARIAMENTE ATIVIDADE RELEVANTE

CADASTRO EXISTENTE
≠ USUÁRIO ATIVO
```

---

## 7. Família ENG — Aquisição, ativação e retenção

| ID | Indicador | Definição lógica | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-ENG-001 | Conclusão de cadastro | cadastros concluídos / cadastros iniciados | % | EVENT CONTRACT PENDING |
| GUV-KPI-ENG-002 | Tempo até ativação | tempo entre elegibilidade inicial e evento de ativação | tempo | ACTIVATION EVENT PENDING |
| GUV-KPI-ENG-003 | WAU | Pessoas únicas ativas em janela móvel de 7 dias | pessoas | ACTIVITY EVENT SET PENDING |
| GUV-KPI-ENG-004 | MAU | Pessoas únicas ativas em janela móvel de 30 dias | pessoas | ACTIVITY EVENT SET PENDING |
| GUV-KPI-ENG-005 | Stickiness WAU/MAU | `WAU / MAU` | razão/% | DEPENDS ENG-003/004 |
| GUV-KPI-ENG-006 | Retenção D7 | coorte ativada com atividade qualificante na janela D7 / coorte ativada | % | COHORT CONTRACT PENDING |
| GUV-KPI-ENG-007 | Retenção D30 | coorte ativada com atividade qualificante na janela D30 / coorte ativada | % | COHORT CONTRACT PENDING |
| GUV-KPI-ENG-008 | Retenção D90 | coorte ativada com atividade qualificante na janela D90 / coorte ativada | % | COHORT CONTRACT PENDING |
| GUV-KPI-ENG-009 | Taxa de reengajamento | inativos elegíveis que retornam no período / inativos elegíveis | % | RULE PENDING |
| GUV-KPI-ENG-010 | Origem de aquisição | distribuição de novos participantes por source/medium/campaign autorizado | distribuição | ATTRIBUTION CONTRACT PENDING |

`Churn` não deve ser usado como sinônimo universal de inatividade. Somente usar churn quando existir relação ou contrato em que cancelamento/abandono seja semanticamente definido.

---

## 8. Família JNY — Journey e experiência

Este conjunto deve preservar a centralidade humana e evitar transformar evolução em score universal.

| ID | Indicador | Definição lógica | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-JNY-001 | Pessoas com Journey iniciada | Pessoas com evento legítimo de início de Journey | pessoas | EVENT CONTRACT PENDING |
| GUV-KPI-JNY-002 | Pessoas com Momento atualizado | Pessoas com atualização válida de Momento no período | pessoas | SOURCE CONTRACT PENDING |
| GUV-KPI-JNY-003 | Objetivos ativos | objetivos em estado válido `active` | objetivos | STATE CONTRACT PENDING |
| GUV-KPI-JNY-004 | Próximos Passos ativos | próximos passos em estado válido ativo | próximos passos | STATE CONTRACT PENDING |
| GUV-KPI-JNY-005 | Próximos Passos concluídos | próximos passos concluídos no período | próximos passos | STATE CONTRACT PENDING |
| GUV-KPI-JNY-006 | Taxa de conclusão de Próximos Passos | próximos passos concluídos / próximos passos elegíveis | % | DENOMINATOR CONTRACT PENDING |
| GUV-KPI-JNY-007 | Experiências iniciadas | experiências com início válido | experiências | EVENT CONTRACT PENDING |
| GUV-KPI-JNY-008 | Experiências concluídas | experiências com conclusão válida | experiências | EVENT CONTRACT PENDING |
| GUV-KPI-JNY-009 | Evidências registradas | evidências válidas registradas no período | evidências | SOURCE CONTRACT PENDING |
| GUV-KPI-JNY-010 | Distribuição por Domínio de Evolução | distribuição autorizada pelos nove `JED-*` | distribuição | DEFINED DOCUMENTARILY |
| GUV-KPI-JNY-011 | Participação recorrente | Pessoas com participação qualificante em ≥2 períodos definidos | pessoas/% | WINDOW CONTRACT PENDING |

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

| ID | Indicador | Definição lógica | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-OPP-001 | Oportunidades criadas | oportunidades válidas criadas no período | oportunidades | DEFINED DOCUMENTARILY |
| GUV-KPI-OPP-002 | Oportunidades publicadas | oportunidades que atingiram estado publicado | oportunidades | STATE CONTRACT PENDING |
| GUV-KPI-OPP-003 | Oportunidades ativas | oportunidades no estado ativo segundo contrato | oportunidades | STATE CONTRACT PENDING |
| GUV-KPI-OPP-004 | Oportunidades encerradas | oportunidades encerradas no período | oportunidades | STATE CONTRACT PENDING |
| GUV-KPI-OPP-005 | Visualizações | eventos válidos de visualização | eventos | EVENT CONTRACT PENDING |
| GUV-KPI-OPP-006 | Interesses / salvamentos | eventos válidos de interesse | eventos/pessoas | EVENT CONTRACT PENDING |
| GUV-KPI-OPP-007 | Inscrições / aplicações | inscrições válidas associadas a oportunidades | inscrições | EVENT CONTRACT PENDING |
| GUV-KPI-OPP-008 | Compras / vendas | transações válidas atribuídas a oportunidades | transações | ECONOMIC CONTRACT REQUIRED |
| GUV-KPI-OPP-009 | Participações iniciadas | participações válidas iniciadas | participações | EVENT CONTRACT PENDING |
| GUV-KPI-OPP-010 | Participações concluídas | participações concluídas | participações | EVENT CONTRACT PENDING |
| GUV-KPI-OPP-011 | Conversão view → interesse | Pessoas com interesse / Pessoas com view elegível | % | FUNNEL CONTRACT PENDING |
| GUV-KPI-OPP-012 | Conversão interesse → inscrição | inscrições / interesses elegíveis | % | FUNNEL CONTRACT PENDING |
| GUV-KPI-OPP-013 | Conversão inscrição → transação | transações / inscrições elegíveis | % | ECONOMIC + FUNNEL CONTRACT PENDING |
| GUV-KPI-OPP-014 | Conversão transação → participação | participações iniciadas / transações elegíveis | % | EVENT CONTRACT PENDING |
| GUV-KPI-OPP-015 | Conclusão de participação | participações concluídas / iniciadas elegíveis | % | EVENT CONTRACT PENDING |
| GUV-KPI-OPP-016 | Taxa de preenchimento | capacidade efetivamente ocupada / capacidade disponibilizada | % | CAPACITY CONTRACT PENDING |
| GUV-KPI-OPP-017 | Tempo até primeiro engajamento | tempo publicação → primeiro evento qualificante | tempo | EVENT CONTRACT PENDING |
| GUV-KPI-OPP-018 | Supply por Domínio | oportunidades ativas por `JED-*` | distribuição | DOMAIN MAPPING REQUIRED |
| GUV-KPI-OPP-019 | Supply por território | oportunidades ativas por geografia autorizada | distribuição | GEO CONTRACT REQUIRED |

`Venda`, `inscrição`, `participação` e `conclusão` são eventos distintos e não devem ser colapsados.

---

## 10. Família REL — Relações e Graph Analytics

### 10.1 Indicadores relacionais básicos

| ID | Indicador | Definição lógica | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-REL-001 | Relações Pessoa ↔ Organização | relações válidas correntes desse tipo | relações | RELATION CONTRACT PENDING |
| GUV-KPI-REL-002 | Relações Pessoa ↔ Coletivo | relações válidas correntes desse tipo | relações | RELATION CONTRACT PENDING |
| GUV-KPI-REL-003 | Relações Organização ↔ Coletivo | relações válidas correntes desse tipo | relações | RELATION CONTRACT PENDING |
| GUV-KPI-REL-004 | Novas relações | relações iniciadas no período | relações/período | RELATION CONTRACT PENDING |
| GUV-KPI-REL-005 | Relações ativas | relações que satisfazem regra de atividade/validade | relações | ACTIVE RELATION RULE PENDING |
| GUV-KPI-REL-006 | Participantes conectados | participantes com ≥1 relação válida / participantes elegíveis | % | GRAPH CONTRACT PENDING |

### 10.2 Graph Analytics avançado

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

| ID | Indicador | Definição lógica | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-PRD-001 | Usuários ativos por produto | usuários únicos com evento qualificante por produto | usuários | ACTIVITY CONTRACT PENDING |
| GUV-KPI-PRD-002 | Adoção por produto | usuários que adotaram produto / população elegível | % | ADOPTION EVENT PENDING |
| GUV-KPI-PRD-003 | Uso cross-product | usuários com atividade qualificante em ≥2 produtos no período | usuários/% | EVENT CONTRACT PENDING |
| GUV-KPI-PRD-004 | Distribuição de uso do ecossistema | participação relativa de atividade por produto/camada | distribuição | EVENT CONTRACT PENDING |

A lista de produtos/camadas consumida por este dashboard deve vir das autoridades correntes do GKR, não ser hard-coded como verdade eterna no Replit.

---

## 12. Família ECO — Economia, planos e transações

Todos os KPIs desta seção exigem composição com `GEM-009-MEASUREMENT-CONTRACT-001` e demais autoridades econômicas aplicáveis.

| ID | Indicador | Definição lógica candidata | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-ECO-001 | Planos vendidos | contratos/assinaturas válidas iniciadas no período | quantidade | GEM-009 REQUIRED |
| GUV-KPI-ECO-002 | Planos ativos | relações de plano ativas na data de referência | quantidade | GEM-009 REQUIRED |
| GUV-KPI-ECO-003 | Novas assinaturas | novas relações pagas válidas no período | quantidade | GEM-009 REQUIRED |
| GUV-KPI-ECO-004 | Cancelamentos | cancelamentos válidos no período | quantidade | GEM-009 REQUIRED |
| GUV-KPI-ECO-005 | Receita | receita reconhecida segundo contrato econômico aplicável | moeda | GEM-009 REQUIRED |
| GUV-KPI-ECO-006 | MRR | receita mensal recorrente conforme contrato econômico | moeda/mês | GEM-009 REQUIRED |
| GUV-KPI-ECO-007 | ARR | anualização autorizada de receita recorrente | moeda/ano | GEM-009 REQUIRED |
| GUV-KPI-ECO-008 | Receita média por relação | receita aplicável / relações pagas elegíveis | moeda | GEM-009 REQUIRED |
| GUV-KPI-ECO-009 | Valor transacionado de oportunidades | soma de transações elegíveis associadas a oportunidades | moeda | GEM-009 REQUIRED |
| GUV-KPI-ECO-010 | Taxa de reembolso | valor ou transações reembolsadas / base elegível | % | GEM-009 REQUIRED |
| GUV-KPI-ECO-011 | Mix de planos | distribuição de relações ativas por plano | % | GEM-009 REQUIRED |
| GUV-KPI-ECO-012 | Receita por produto | receita atribuível por Produto Especializado | moeda/distribuição | GEM-009 + ATTRIBUTION REQUIRED |

Nenhuma equivalência Pontos ↔ moeda deve ser inferida neste dashboard.

---

## 13. Família GEO — Território e demografia

Todas as leituras devem respeitar minimização, thresholds e finalidade.

| ID | Indicador | Definição lógica | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-GEO-001 | Pessoas por território | Pessoas agregadas por geografia autorizada | distribuição | DISCLOSURE CONTRACT REQUIRED |
| GUV-KPI-GEO-002 | Organizações por território | Organizações agregadas por geografia | distribuição | GEO CONTRACT REQUIRED |
| GUV-KPI-GEO-003 | Coletivos por território | Coletivos agregados por geografia | distribuição | GEO CONTRACT REQUIRED |
| GUV-KPI-GEO-004 | Oportunidades por território | oportunidades por geografia | distribuição | GEO CONTRACT REQUIRED |
| GUV-KPI-GEO-005 | Distribuição demográfica autorizada | população agregada por dimensão legitimamente disponível | distribuição | PRIVACY/DATA CONTRACT REQUIRED |
| GUV-KPI-GEO-006 | Completude geográfica | registros elegíveis com geografia utilizável / registros elegíveis | % | SOURCE CONTRACT REQUIRED |

Regras:

```text
MAPA
≠ AUTORIZAÇÃO DE PRECISÃO MÁXIMA

DADO GEOGRÁFICO DISPONÍVEL
≠ DADO GEOGRÁFICO EXIBÍVEL
```

---

## 14. Família ADS — Resumo Ads / Opportunity Boost

Esta área é apenas um resumo interno de alto nível. O detalhamento deverá pertencer ao futuro master específico de Ads / Opportunity Boost.

| ID | Indicador | Status |
|---|---|---|
| GUV-KPI-ADS-001 | campanhas ativas | DEPENDS ON ADS MASTER |
| GUV-KPI-ADS-002 | investimento | DEPENDS ON ADS + ECONOMIC CONTRACT |
| GUV-KPI-ADS-003 | impressões | DEPENDS ON ADS MASTER |
| GUV-KPI-ADS-004 | cliques | DEPENDS ON ADS MASTER |
| GUV-KPI-ADS-005 | conversões | DEPENDS ON ATTRIBUTION CONTRACT |
| GUV-KPI-ADS-006 | CTR | DEPENDS ON ADS MASTER |
| GUV-KPI-ADS-007 | CPA | DEPENDS ON ADS + ECONOMIC CONTRACT |
| GUV-KPI-ADS-008 | ROAS | DEPENDS ON ATTRIBUTION + ECONOMIC CONTRACT |

```text
BOOSTED PERFORMANCE
≠ IMPACTO CAUSAL COMPROVADO
```

---

## 15. Família DQ — Qualidade, freshness e governança

| ID | Indicador | Definição lógica | Unidade | Status |
|---|---|---|---|---|
| GUV-KPI-DQ-001 | Freshness compliance | datasets/contratos dentro do SLA de atualização / datasets monitorados | % | SLA CONTRACT PENDING |
| GUV-KPI-DQ-002 | Completude de campos críticos | campos críticos preenchidos / campos críticos esperados | % | DATA CONTRACT PENDING |
| GUV-KPI-DQ-003 | Taxa de duplicidade | registros duplicados confirmados / registros avaliados | % | DATA QUALITY CONTRACT PENDING |
| GUV-KPI-DQ-004 | Indicadores indisponíveis | KPIs esperados sem dado utilizável na janela | quantidade | DEFINED DOCUMENTARILY |
| GUV-KPI-DQ-005 | Supressões de disclosure | células/segmentos ocultados por regra de proteção | quantidade | DISCLOSURE ENGINE PENDING |
| GUV-KPI-DQ-006 | KPIs com fonte vencida | KPIs cujo freshness ultrapassou limite contratado | quantidade | SOURCE CONTRACT PENDING |

Esses indicadores existem para qualificar confiança na leitura, não para criar aparência de precisão onde o dado é insuficiente.

---

## 16. Filtros globais

Filtros candidatos do Dashboard Guivos:

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
- Organização / Coletivo somente para usuários cuja autoridade permita esse recorte.

Regra:

```text
FILTRO DISPONÍVEL NA UI
→ DEVE SER SUBCONJUNTO DO ACCESS SCOPE
```

O cliente não pode ampliar escopo enviando filtros arbitrários ao backend/serving layer.

---

## 17. Drill-down

Níveis semânticos candidatos:

```text
N0 — ECOSSISTEMA
→ N1 — FAMÍLIA / DOMÍNIO
→ N2 — SEGMENTO / TERRITÓRIO / PRODUTO
→ N3 — OBJETO OPERACIONAL AUTORIZADO
```

Pessoa individual não é nível padrão de drill-down deste dashboard.

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

Cada bloco/KPI deve suportar:

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

Sem definir schema físico, o Dashboard Guivos deverá conseguir consumir contratos lógicos equivalentes a:

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

Quando a construção for autorizada, a AI do Replit deverá seguir estas instruções:

1. **não inventar métricas, fórmulas, tabelas, bancos ou permissões**;
2. usar `metric_id` como chave estável e não o label visual;
3. manter fórmulas fora dos componentes visuais quando o cálculo pertencer ao serving/analytics layer;
4. tratar filtros como restrição adicional, nunca como ampliação de acesso;
5. não confiar em `participant_id`, tenant ou role enviados somente pelo cliente;
6. não conectar diretamente o browser a bancos de origem;
7. não armazenar credenciais ou secrets no frontend;
8. separar mock adapters de real adapters;
9. exibir versão/freshness/proveniência quando a especificação exigir;
10. implementar estados `NO_DATA`, `INSUFFICIENT_DATA`, `SUPPRESSED_BY_POLICY` e `SOURCE_DELAYED` separadamente;
11. impedir exportação quando o contrato do KPI não permitir;
12. não habilitar drill-down para Pessoa por conveniência;
13. preservar timezone e janela temporal do contrato;
14. não inferir causalidade em tooltips, labels ou summaries;
15. não traduzir `inferido` para `fato` na copy;
16. registrar a versão deste master consumida na build;
17. deixar componentes bloqueados/TBD claramente identificados em ambiente de mock;
18. não promover mock data como dado real.

---

## 22. Estrutura funcional sugerida para futura construção

Sem definir layout visual, a ordem semântica recomendada é:

```text
DASHBOARD GUIVOS

1. CONTEXTO
→ período
→ freshness
→ access scope

2. EXECUTIVE OVERVIEW
→ Pessoas / Organizações / Coletivos
→ atividade / ativação / retenção
→ oportunidades
→ economia quando autorizada

3. GROWTH & ENGAGEMENT

4. JOURNEY & EXPERIENCES

5. OPPORTUNITIES & SUPPLY

6. RELATIONSHIPS & ECOSYSTEM

7. PRODUCTS

8. ECONOMY

9. TERRITORY / DEMOGRAPHY

10. ADS SUMMARY

11. DATA QUALITY / GOVERNANCE
```

A ordem pode ser refinada por Design futuro sem alterar o significado dos contratos.

---

## 23. Critérios de aceite documental para futuro handoff

Antes de declarar este dashboard `READY FOR BUILD`, deve existir prova de que:

```text
[ ] cada KPI incluído na build possui status compatível
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

---

## 24. Testes mínimos para futura implementação

A implementação, quando autorizada, deverá provar pelo menos:

1. nenhum usuário recebe dado fora do seu access scope;
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
13. mock data não pode aparecer como produção;
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

FINAL VISUAL DESIGN
→ NOT AUTHORIZED BY THIS MASTER

REPLIT IMPLEMENTATION
→ NOT AUTHORIZED BY THIS MASTER
```

---

## 26. Handoff futuro

Quando autorizado, o pacote de construção do Dashboard Guivos deverá incluir:

1. `GKR-INTELLIGENCE-DASHBOARD-KPI-001` vigente;
2. este documento vigente;
3. registry dos KPI IDs selecionados para a release;
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
→ v0.1.0
→ ACTIVE
→ ANNEX A OF GKR-INTELLIGENCE-DASHBOARD-KPI-001
→ GOVERNED PRE-IMPLEMENTATION DASHBOARD MASTER

DASHBOARD GUIVOS
→ SCOPE + KPI FAMILIES + ACCESS + INTEGRATION + REPLIT HANDOFF SPECIFIED DOCUMENTARILY

KPI IMPLEMENTATION READINESS
→ MIXED
→ INDIVIDUAL STATUS PER KPI

REAL DATA / BACKEND / TECHNICAL RBAC / PRODUCTION
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

NEXT SPECIALIZED MASTER
→ REQUIRES SEPARATE GOVERNED ACT
```
