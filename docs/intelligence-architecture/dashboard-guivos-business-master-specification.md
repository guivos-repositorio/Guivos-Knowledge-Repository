---
id: GKR-INTELLIGENCE-DASHBOARD-BUSINESS-001
title: Dashboard Guivos Business — Documento Mestre de Especificação Analítica e Handoff Replit
status: active
version: 0.1.3
owner: Guivos Intelligence Architecture
last_updated: 2026-10-11
normative: false
maturity: governed_pre_implementation_dashboard_master
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GPA-004
  - GPA-004-FUNCTIONAL-PORTFOLIO-001
  - GPA-006
  - GAI-001
  - GAI-002
  - GIA-COG-001
  - GEM-009-MEASUREMENT-CONTRACT-001
related:
  - GTM-002
  - GTM-003
  - BA-STR-002
---

# Dashboard Guivos Business — Documento Mestre de Especificação Analítica e Handoff Replit

## 1. Finalidade

Este documento é o **Anexo B** de `GKR-INTELLIGENCE-DASHBOARD-KPI-001` e governa, em nível documental pré-implementação, o **Dashboard Guivos Business**.

Seu objetivo é consolidar, antes de qualquer implementação, o recorte analítico legítimo do produto especializado B2B Guivos Business a partir das autoridades correntes do GKR.

O Dashboard Guivos Business deve permitir que uma empresa cliente autorizada compreenda o que ocorreu na relação Business e no recorte de população legitimamente abrangido por essa relação, sem transformar a empresa em proprietária da Journey, do contexto privado ou da evolução individual das Pessoas.

Regra central:

> **A empresa pode compreender programas, participação, concessões, orçamento, utilização, acessos custeados e movimentos agregados autorizados; ela não recebe autoridade sobre a Journey individual nem um Intelligence individual por Pessoa.**

Este documento não transforma métricas candidatas em fatos operacionais, não autoriza conexão com dados reais e não substitui as autoridades de Business, Economy, Journey, Intelligence, Privacy, GTM ou Dados.

---

## 2. Autoridades de domínio e leitura de precedência

A construção documental deste Anexo B deriva, no mínimo, das seguintes autoridades:

| Autoridade | Papel neste master |
|---|---|
| `GPA-004 — Guivos Business` | identidade, limites e ofertas do produto Business |
| `GPA-004-FUNCTIONAL-PORTFOLIO-001` | objetos funcionais, orçamento, Pontos, Journey custeado, Intelligence e integrações |
| `GKR-INTELLIGENCE-DASHBOARD-KPI-001` | envelope transversal de KPI, acesso, disclosure e handoff |
| `GPA-006 — Guivos Intelligence` | interpretação e compreensão contextual sem substituir autonomia |
| `GAI-001 / GAI-002 / GIA-COG-001` | evidência, explicabilidade, natureza de evidência e fronteira `COMPREENDER ≠ DECIDIR` |
| `GEM-009-MEASUREMENT-CONTRACT-001` | composição obrigatória para métricas econômicas quando aplicável |
| `GTM-002` | funil Business, contratos, crescimento comercial e distinção Business/Organização/Parceria Estratégica |
| `GTM-003` | baseline gerencial de contratos e ARR de planejamento, com limites explícitos |
| `BA-STR-002` | separação Outcome, KPI, meta e resultado observado |

Em caso de conflito, este master não redefine a autoridade especializada. Ele deve preservar o estado mais restritivo e abrir adjudicação própria.

---

## 3. Estado e boundary

```text
GKR-INTELLIGENCE-DASHBOARD-BUSINESS-001
→ ACTIVE
→ PRE-IMPLEMENTATION DASHBOARD MASTER

GUIVOS BUSINESS
→ PRODUCT SPECIALIZED B2B
→ NOT PARTICIPANT TYPE
→ ORGANIZAÇÃO ≠ GUIVOS BUSINESS

DASHBOARD BUSINESS
→ ANALYTICAL CONSUMPTION SURFACE
→ NOT SOURCE OF TRUTH
→ NOT ERP / HRIS / CRM OF THE CLIENT

REAL DATA CONNECTION
→ NOT AUTHORIZED BY THIS DOCUMENT

REPLIT BUILD
→ NOT AUTHORIZED BY THIS DOCUMENT
→ HANDOFF SPECIFICATION ONLY

PERSON-LEVEL PRIVATE CONTEXT
→ NOT PART OF DEFAULT BUSINESS DISCLOSURE

JOURNEY INDIVIDUAL
→ NOT DISCLOSED TO COMPANY BY DEFAULT

INTELLIGENCE BY PERSON
→ NOT AUTHORIZED BY DEFAULT
```

A existência de uma relação Business não concede à empresa acesso irrestrito a Pessoas, Organizações, Coletivos, relações, dados demográficos, dados geográficos, Journey ou Intelligence.

---

## 4. Escopo funcional do Dashboard Business

O dashboard é organizado em **nove áreas analíticas**:

1. Visão Executiva da Relação Business;
2. Programas de Incentivo;
3. Participação e Eventos Elegíveis;
4. Benefícios, Concessões e Orçamento;
5. Utilização de Pontos Guivos — leitura agregada;
6. Journey custeado pela empresa — acesso e uso agregado protegido;
7. Intelligence e Movimentos Agregados Autorizados;
8. Contrato, Plano, Funil Comercial e Continuidade;
9. Qualidade, Freshness, Privacidade e Governança do Dado.

A documentação dessas áreas não declara que todas já possuem dados, source contracts, APIs ou entitlement operacional.

```text
ÁREA DOCUMENTADA
≠ DADO DISPONÍVEL
≠ ACESSO AUTORIZADO
≠ IMPLEMENTAÇÃO AUTORIZADA
```

---

## 5. Classes funcionais de consumo

As classes abaixo são conceituais e não constituem RBAC técnico implementado:

| Classe funcional | Escopo candidato |
|---|---|
| Business — visão executiva | agregados da própria relação contratual e dos programas autorizados |
| Business — operação de programa | programas, campanhas, regras, eventos e benefícios sob sua autoridade |
| Business — financeiro/orçamento | orçamento, concessões e métricas econômicas contratualmente autorizadas |
| Business — People/Benefits | agregados necessários à finalidade legítima do programa, sem contexto privado individual |
| Business — Data/BI | exportações ou APIs autorizadas do próprio recorte Business, quando contratadas |
| Guivos — operação/CS | dados necessários à implantação, suporte e continuidade da relação |
| Guivos — Intelligence/Data | inputs e outputs necessários à finalidade analítica autorizada |

Invariante:

```text
EMPRESA CLIENTE
≠ AUTORIDADE SOBRE TODA PESSOA VINCULADA

FINANCIAR BENEFÍCIO
≠ POSSUIR O CONTEXTO DA PESSOA

CUSTEAR JOURNEY
≠ POSSUIR JOURNEY

DADO AGREGADO
≠ AUTOMATICAMENTE EXIBÍVEL
```

---

## 6. Vocabulário de KPI e readiness

Prefixo deste master:

```text
BUS-KPI-<FAMÍLIA>-NNN
```

Famílias iniciais:

- `PRG` — programas e campanhas;
- `PAR` — participação e eventos;
- `BUD` — orçamento, concessões e benefícios;
- `PTS` — utilização agregada de Pontos Guivos;
- `JNY` — Journey custeado;
- `INT` — Intelligence agregado;
- `COM` — contrato, plano, funil e continuidade;
- `DQ` — qualidade, freshness e governança.

A **Visão Executiva da Relação Business** não constitui família KPI autônoma nesta versão. Ela compõe leituras autorizadas a partir das famílias governadas acima e não cria namespace `BUS-KPI-EXE-*`.

Estados usados:

| Status | Significado |
|---|---|
| `proposed` | significado ou contrato ainda incompleto; não build-ready |
| `source_pending` | semântica suficientemente delimitada, mas source/data contract ou equivalente bloqueia readiness |
| `defined` | contrato documental mínimo completo; ainda requer gates de domínio e autorização de build |
| `approved-equivalent` | autoridade especializada fornece estado equivalente aceito pelo gate |

Nesta versão, **nenhum KPI é declarado `defined` ou `approved-equivalent` por inferência**.

Todos os KPIs abaixo permanecem `NOT_READY` para implementação canônica enquanto não cumprirem o envelope mínimo do master global e seus contratos especializados.

---

## 7. Família PRG — Programas e campanhas

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| BUS-KPI-PRG-001 | Programas ativos | programas Business em estado ativo válido no recorte contratual | programas | proposed | lifecycle/state contract + source |
| BUS-KPI-PRG-002 | Campanhas ativas | campanhas em estado ativo válido | campanhas | proposed | campaign state contract + source |
| BUS-KPI-PRG-003 | Programas por finalidade | distribuição por finalidade empresarial legítima governada | distribuição | proposed | taxonomy + disclosure |
| BUS-KPI-PRG-004 | Programas iniciados no período | programas com início válido na janela | programas/período | proposed | temporal + event contract |
| BUS-KPI-PRG-005 | Programas encerrados no período | programas encerrados validamente na janela | programas/período | proposed | close-state contract |

O dashboard não deve converter conceitos subjetivos como “comprometimento” em métricas próprias. A empresa deve traduzi-los em eventos e condições observáveis antes de qualquer regra.

---

## 8. Família PAR — Participação e eventos

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| BUS-KPI-PAR-001 | Pessoas elegíveis | Pessoas incluídas legitimamente no escopo do programa/custeio | pessoas | proposed | eligibility + relation + disclosure contract |
| BUS-KPI-PAR-002 | Participantes únicos | Pessoas com ao menos uma participação válida no período | pessoas | proposed | participation event + population |
| BUS-KPI-PAR-003 | Taxa de participação | participantes únicos / Pessoas elegíveis | % | proposed | PAR-001/002 + denominator rules |
| BUS-KPI-PAR-004 | Eventos elegíveis confirmados | eventos válidos recebidos/produzidos para regras Business | eventos | proposed | event taxonomy + validation + source |
| BUS-KPI-PAR-005 | Recorrência de participação | Pessoas com participação qualificante em janelas repetidas | pessoas/% | proposed | recurrence/window contract |
| BUS-KPI-PAR-006 | Participação por programa/campanha | distribuição de participações válidas por objeto Business | distribuição | proposed | scope + event contract |

A arquitetura padrão não requer importação integral de bases de RH, folha, absenteísmo, produtividade, vendas, CRM ou ERP. Integrações podem transmitir o evento mínimo legítimo necessário.

---

## 9. Família BUD — Orçamento, concessões e benefícios

A leitura funcional validada de orçamento empresarial é:

```text
CARREGADO
CONCEDIDO
DISPONÍVEL
```

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| BUS-KPI-BUD-001 | Orçamento carregado | total válido carregado para financiar programas no recorte autorizado | unidade econômica aplicável | proposed | GEM-009 + economic/source contract |
| BUS-KPI-BUD-002 | Orçamento concedido | total validamente alocado/consumido pela empresa no momento da concessão | unidade econômica aplicável | proposed | GEM-009 + grant contract |
| BUS-KPI-BUD-003 | Orçamento disponível | saldo empresarial ainda não concedido conforme contrato aplicável | unidade econômica aplicável | proposed | GEM-009 + balance/reversal rules |
| BUS-KPI-BUD-004 | Concessões realizadas | resultados de benefício validamente concedidos no período | concessões | proposed | result taxonomy + event contract |
| BUS-KPI-BUD-005 | Pessoas beneficiadas | Pessoas distintas com concessão válida | pessoas | proposed | grant + eligibility + disclosure |
| BUS-KPI-BUD-006 | Valor de Impacto Liberado | valor disponibilizado para ação elegível, quando aplicável | unidade econômica | proposed | authority específica + GEM-009 |

`VALOR DE IMPACTO LIBERADO` não deve ser apresentado como impacto realizado, impacto comprovado, evolução ou resultado causal.

Nenhuma equivalência Pontos Guivos ↔ moeda pode ser inferida deste dashboard.

---

## 10. Família PTS — utilização agregada de Pontos Guivos

A autoridade vigente permite leitura administrativa agregada de utilização efetiva, preservando a separação entre orçamento empresarial e saldo pessoal.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| BUS-KPI-PTS-001 | Pontos concedidos | quantidade de Pontos Guivos validamente concedidos pelo programa | pontos | proposed | points grant contract + source |
| BUS-KPI-PTS-002 | Pontos efetivamente utilizados | quantidade de Pontos Guivos do recorte aplicável efetivamente utilizados em possibilidades elegíveis | pontos | proposed | usage attribution + source |
| BUS-KPI-PTS-003 | Distribuição de utilização | participação dos pontos efetivamente utilizados entre Mall, Travel e Journey | % | proposed | usage source + attribution + disclosure |
| BUS-KPI-PTS-004 | Utilização por período | pontos efetivamente utilizados por janela temporal autorizada | pontos/período | proposed | temporal + attribution contract |

Para `BUS-KPI-PTS-003`, o denominador conceitual é **somente pontos efetivamente utilizados**. Pontos guardados ou expirados não entram nesse denominador. O resultado exibido deve fechar 100% entre as categorias autorizadas.

A empresa não recebe histórico individual de consumo das Pessoas por meio desta métrica.

---

## 11. Família JNY — Journey custeado pela empresa

A empresa pode custear acesso ao **Guivos Journey existente**; isso não cria Journey corporativo.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| BUS-KPI-JNY-001 | Acessos Journey custeados | acessos validamente custeados pela empresa no recorte contratual | acessos | proposed | sponsorship/access contract |
| BUS-KPI-JNY-002 | Pessoas com acesso custeado | Pessoas distintas com acesso elegível custeado | pessoas | proposed | eligibility + access source |
| BUS-KPI-JNY-003 | Ativação agregada do acesso | Pessoas que atingiram evento de ativação autorizado / Pessoas elegíveis com acesso | % | proposed | activation + denominator + privacy |
| BUS-KPI-JNY-004 | Participação agregada no Journey | leitura agregada de participação autorizada na população custeada | pessoas/% | proposed | Journey authority + disclosure threshold |
| BUS-KPI-JNY-005 | Tendência temporal de utilização | evolução agregada autorizada do uso do acesso custeado | série temporal | proposed | event/window/disclosure contract |

Não são métricas autorizadas por este master:

- score individual de evolução;
- Journey individual;
- intenção individual;
- tema pessoal específico;
- vulnerabilidade;
- explicação individual de pertinência;
- ranking humano.

---

## 12. Família INT — Intelligence agregado

Guivos Intelligence permanece produto/capacidade transversal e não se torna módulo Business.

Leituras candidatas, quando autorizadas e protegidas:

| ID | Indicador / leitura candidata | Natureza | Status | Gate principal |
|---|---|---|---|---|
| BUS-KPI-INT-001 | Interesses de evolução agregados | distribuição/contexto agregado | proposed | Journey + Intelligence + privacy/disclosure |
| BUS-KPI-INT-002 | Tendências temporais agregadas | tendência | proposed | source + window + disclosure |
| BUS-KPI-INT-003 | Temas emergentes agregados | synthesis/output Intelligence | proposed | evidence + method + explanation |
| BUS-KPI-INT-004 | Aderência entre interesses agregados e iniciativas/benefícios cadastrados | comparação contextual | proposed | matching semantics + disclosure |
| BUS-KPI-INT-005 | Lacunas de cobertura | leitura contextual | proposed | coverage model + evidence |
| BUS-KPI-INT-006 | Sinais de subutilização | sinal analítico | proposed | usage semantics + evidence |

Regras obrigatórias:

```text
INTERESSE ≠ CONDIÇÃO
INTENÇÃO ≠ DIAGNÓSTICO
TEMA ≠ PROBLEMA
ESCOLHA ≠ CAUSA
CORRELAÇÃO ≠ CAUSALIDADE
COMPREENDER ≠ DECIDIR
```

Qualquer output inferido, estimado ou predito deve preservar sua natureza, explicabilidade e incerteza proporcional.

---

## 13. Família COM — contrato, plano, funil e continuidade

Guivos Business possui planos `Start`, `Growth`, `Scale` e `Enterprise`, mas preços e entitlements finais não estão congelados pelas autoridades atuais.

O funil comercial governado por `GTM-002` preserva a sequência:

```text
conta-alvo mapeada
→ descoberta qualificada
→ proposta
→ contrato ganho
→ sucesso inicial
→ renovação / expansão
```

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| BUS-KPI-COM-001 | Contas-alvo mapeadas | contas Business classificadas como alvo segundo regra vigente | contas | proposed | ICP/target rule + source |
| BUS-KPI-COM-002 | Descobertas qualificadas | relações que atingiram estágio de descoberta qualificada | relações | proposed | stage-entry contract |
| BUS-KPI-COM-003 | Propostas | propostas comerciais válidas emitidas | propostas | proposed | proposal lifecycle/source |
| BUS-KPI-COM-004 | Contratos ganhos | contratos que atingiram estado ganho válido | contratos | proposed | contract state + source |
| BUS-KPI-COM-005 | Conversão proposta → contrato | contratos ganhos / propostas elegíveis | % | proposed | cohort/window + denominator |
| BUS-KPI-COM-006 | Contratos ativos | contratos Business em estado ativo válido | contratos | proposed | contract lifecycle |
| BUS-KPI-COM-007 | Renovação | contratos elegíveis renovados / contratos elegíveis | % | proposed | renewal + denominator |
| BUS-KPI-COM-008 | Expansão | relações com expansão válida no período | contratos/valor | proposed | expansion contract + GEM-009 when monetary |
| BUS-KPI-COM-009 | Downgrade | relações com redução contratual válida | contratos/valor | proposed | downgrade contract + GEM-009 when monetary |
| BUS-KPI-COM-010 | Churn contratual | contratos que atingem cancelamento/encerramento qualificante | contratos/% | proposed | churn/cancellation contract |
| BUS-KPI-COM-011 | Valor anual contratado | valor anual contratado reconhecido para finalidade gerencial autorizada | moeda | proposed | GEM-009 + contract value rules |
| BUS-KPI-COM-012 | Mix por plano | distribuição de contratos ativos por plano Business | distribuição | proposed | plan entitlement/source |

As metas M6–M60 e envelopes de ARR de `GTM-002`/`GTM-003` são **baselines de planejamento**, não valores realizados e não preços oficiais de planos. Caso apareçam na superfície futura, devem ser identificados explicitamente como baseline/target e separados de realizado.

---

## 14. Família DQ — qualidade, freshness, privacidade e governança

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| BUS-KPI-DQ-001 | Freshness compliance | contratos/datasets dentro do SLA / monitorados | % | proposed | freshness/SLA contract |
| BUS-KPI-DQ-002 | Indicadores indisponíveis | KPIs esperados sem dado utilizável | quantidade | proposed | registry + availability rules |
| BUS-KPI-DQ-003 | Supressões de disclosure | células/segmentos protegidos por política | quantidade | proposed | disclosure engine/policy |
| BUS-KPI-DQ-004 | Eventos rejeitados | eventos Business rejeitados por validação | eventos | proposed | validation taxonomy |
| BUS-KPI-DQ-005 | Completude de proveniência | outputs com proveniência suficiente / outputs avaliados | % | proposed | provenance contract |

Qualidade deve qualificar a confiança da leitura e não criar aparência de precisão onde o dado é insuficiente.

---

## 15. Filtros candidatos

Filtros somente podem reduzir o escopo autorizado. Entre os candidatos, sujeitos a contrato próprio:

- período e comparação de período;
- programa;
- campanha;
- finalidade/tipo de programa;
- população elegível quando legitimamente segmentável;
- tipo de resultado/benefício;
- Journey custeado versus Programa de Incentivo;
- plano Business;
- território quando permitido;
- canal/origem comercial quando contratualmente definido.

```text
FILTRO NA UI
→ SUBCONJUNTO DO ACCESS SCOPE
→ NUNCA AMPLIA DISCLOSURE
```

---

## 16. Drill-down

Estrutura candidata:

```text
N0 — RELAÇÃO BUSINESS
→ N1 — OFERTA / FAMÍLIA ANALÍTICA
→ N2 — PROGRAMA / CAMPANHA / PERÍODO / SEGMENTO AUTORIZADO
→ N3 — OBJETO OPERACIONAL BUSINESS AUTORIZADO
```

Pessoa individual **não é nível padrão de drill-down**.

Um caso operacional que exija identificação individual deve possuir finalidade, base de autoridade, minimização e trilha próprias; não deve ser inferido do dashboard analítico.

---

## 17. Estados obrigatórios de visualização

```text
LOADING
NO_DATA
INSUFFICIENT_DATA
SUPPRESSED_BY_POLICY
SOURCE_DELAYED
NOT_ENTITLED
ERROR
AVAILABLE
```

`0` não substitui `NO_DATA`.

`NOT_ENTITLED` não significa indisponibilidade técnica.

`SUPPRESSED_BY_POLICY` não deve ser apresentado como erro.

---

## 18. Contratos lógicos esperados

Sem definir schema físico, o Dashboard Business poderá futuramente consumir contratos lógicos equivalentes a:

- Business Account / Contract Aggregate;
- Program Aggregate;
- Campaign Aggregate;
- Eligible Population Aggregate;
- Participation/Event Aggregate;
- Grant/Benefit Aggregate;
- Business Budget Aggregate;
- Points Usage Aggregate;
- Sponsored Journey Access Aggregate;
- Authorized Journey Population Aggregate;
- Business Commercial Funnel Aggregate;
- Intelligence Aggregate Output;
- Data Quality / Freshness Status.

Cada payload deverá carregar, quando aplicável, `metric_id`, período, valor, unidade, escopo populacional, source version, freshness, natureza da evidência, access class, suppression state, proveniência e confidence/uncertainty quando material.

---

## 19. Integrações empresariais

A arquitetura padrão deve operar por minimização:

```text
SISTEMA EMPRESARIAL
→ EVENTO MÍNIMO NECESSÁRIO
→ GUIVOS BUSINESS
→ REGRA / PROCESSAMENTO AUTORIZADO
→ MÉTRICA / OUTPUT AUTORIZADO
```

Não é requisito deste master importar bases completas de RH, folha, absenteísmo, produtividade, vendas, CRM ou ERP.

Exportação estruturada/API para Power BI, Tableau, Looker, Data Lake ou ambiente equivalente é direção funcional reconhecida, mas depende de entitlement, contrato de dados, segurança, escopo e autorização específicos.

```text
DADO GUIVOS EXPORTADO
→ PODE SER COMBINADO PELA EMPRESA COM KPI INTERNO

RESULTADO OBSERVADO NA GUIVOS
≠ RESULTADO OPERACIONAL INTERNO DA EMPRESA
```

---

## 20. Orientação futura para Replit

Quando houver autorização formal de build, a AI/ferramenta de construção deverá:

1. não inventar KPI, fórmula, preço, entitlement, threshold, source, schema ou permissão;
2. usar os `BUS-KPI-*` como identificadores estáveis, não labels visuais;
3. bloquear KPIs `proposed` e `source_pending` para consumo canônico com dado real;
4. separar baseline/meta, realizado e forecast;
5. preservar Business ≠ Organização;
6. preservar Business ≠ Ads;
7. preservar Intelligence como autoridade transversal, não módulo Business;
8. não criar score individual de evolução;
9. não expor Journey individual;
10. não inferir causalidade de tendências e correlações;
11. tratar filtros como restrição adicional;
12. validar escopo no serving/backend, não somente no cliente;
13. separar mock adapters de real adapters;
14. exibir `NO_DATA`, `INSUFFICIENT_DATA`, `SUPPRESSED_BY_POLICY`, `NOT_ENTITLED` e `SOURCE_DELAYED` separadamente;
15. preservar versão, freshness e proveniência quando exigido;
16. não transformar baseline de GTM em dado realizado;
17. não hard-code preços ou entitlements ainda `TBD`;
18. não conectar browser diretamente a sistemas empresariais ou bancos de origem;
19. não implementar exportação individual por conveniência;
20. registrar a versão deste master usada na build.

---

## 21. Critérios de aceite para futuro handoff

Antes de qualquer release `READY FOR BUILD`:

```text
[ ] KPI selecionado = defined OU approved-equivalent
[ ] pergunta e finalidade estão fechadas
[ ] população e elegibilidade estão definidas
[ ] fórmula/numerador/denominador estão definidos quando aplicáveis
[ ] janela temporal e granularidade estão definidas
[ ] source/data contract está definido
[ ] access/disclosure scope está definido
[ ] thresholds de proteção estão definidos quando aplicáveis
[ ] filtros e drill-down permitidos estão definidos
[ ] exportação/API está definida quando aplicável
[ ] null/zero/no-data estão definidos
[ ] freshness e quality checks estão definidos
[ ] métricas econômicas compõem com GEM-009
[ ] Journey preserva autoridade da Pessoa
[ ] Intelligence preserva natureza da evidência e explicabilidade
[ ] baseline/meta e realizado estão separados
[ ] Design/build authorization foi emitida
```

---

## 22. Itens explicitamente bloqueados nesta versão

```text
REAL DATA
→ NOT AUTHORIZED

BACKEND / API FÍSICA
→ NOT DEFINED HERE

TECHNICAL RBAC
→ NOT IMPLEMENTED

FINAL VISUAL DESIGN
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

BUSINESS PLAN PRICES
→ NOT DEFINED HERE

FINAL ENTITLEMENTS
→ NOT DEFINED HERE

POINTS ↔ MONEY CONVERSION RATE
→ NOT CANONICALLY DEFINED HERE

INDIVIDUAL JOURNEY DISCLOSURE TO COMPANY
→ NOT AUTHORIZED

INDIVIDUAL EVOLUTION SCORE
→ NOT AUTHORIZED

CROSS-COMPANY / CROSS-TENANT ACCESS
→ NOT AUTHORIZED

ADS ANALYTICS
→ OUTSIDE THIS MASTER
→ ANNEX F REMAINS SEPARATE
```

---

## 23. Estado final desta versão

```text
GKR-INTELLIGENCE-DASHBOARD-BUSINESS-001
→ v0.1.2
→ ACTIVE
→ ANNEX B PRE-IMPLEMENTATION MASTER

DOMAIN AUTHORITIES
→ GPA-004 + GPA-004-FUNCTIONAL-PORTFOLIO-001 PRESERVED

ANALYTICAL AREAS
→ 9

KPI FAMILIES
→ PRG / PAR / BUD / PTS / JNY / INT / COM / DQ

KPI IMPLEMENTATION READINESS
→ NONE CLAIMED BY INFERENCE
→ ALL CURRENT KPIs = proposed
→ ALL = NOT_READY

BUSINESS POPULATION
→ ONLY LEGITIMATELY COVERED RELATION / POPULATION

PERSON PRIVATE CONTEXT / INDIVIDUAL JOURNEY
→ NOT DEFAULT BUSINESS DISCLOSURE

REAL DATA / BACKEND / API / TECHNICAL RBAC / PRODUCTION
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

ANNEX C / D / E / F
→ UNCHANGED / NOT MATERIALIZED BY THIS DOCUMENT
```

A materialização documental deste master não autoriza dados reais, implementação, produção, ampliação de disclosure ou promoção automática de qualquer KPI além de seu status governado.

---

## 24. Extensão de auditoria — inteligência executiva e contratos candidatos (proposta)

> **Natureza:** ampliação documental não normativa. Este anexo de auditoria não altera as definições das seções 1–23, não adjudica autoridades de domínio, não cria entitlement, não concede acesso e não autoriza implementação. O vocabulário `proposed / NOT_READY` permanece para **todos os 49 KPIs existentes**. Novos códigos `*-Cxx` são **referências provisórias de análise**, nunca `metric_id` canônico.

### 24.1 Matriz de preservação e reconciliação

| Família | IDs preservados | Quantidade | Aprofundamento candidato |
|---|---|---:|---|
| PRG | BUS-KPI-PRG-001..005 | 5 | capacidade, conclusão, comparecimento, satisfação, reparticipação |
| PAR | BUS-KPI-PAR-001..006 | 6 | ativação, retenção por coorte, tempo até primeiro evento, cobertura |
| BUD | BUS-KPI-BUD-001..006 | 6 | concessão relativa, custos atribuíveis, projeções, concentração |
| PTS | BUS-KPI-PTS-001..004 | 4 | taxa de utilização atribuível, tempo até utilização |
| JNY | BUS-KPI-JNY-001..005 | 5 | cobertura do custeio, continuidade, tempo até ativação |
| INT | BUS-KPI-INT-001..006 | 6 | modalidade, território, horário, capacidade, cenários, evidência |
| COM | BUS-KPI-COM-001..012 | 12 | conversão por etapa, ciclo, receita e adoção inicial |
| DQ | BUS-KPI-DQ-001..005 | 5 | cobertura, consistência, estabilidade, qualidade de projeção |
| **Total** | **49 IDs existentes** | **49** | **nenhuma promoção de status** |

A Visão Executiva da Relação Business é composição de métricas autorizadas, não uma nova família de KPI. Um aprofundamento pode ser dimensão, filtro, comparação ou leitura de KPI existente; **não criar novo ID sem teste de não duplicidade e adjudicação**.

### 24.2 Consumidores e superfícies — hipótese de segregação a adjudicar

| Consumidor funcional | Leituras candidatas | Exclusões e gates |
|---|---|---|
| Empresa cliente — executivo | sua própria relação Business, programas, população autorizada, orçamento, benefícios e resultados agregados | sem carteira comercial Guivos, outras contas ou Journey individual |
| Empresa cliente — operação/finanças/People | objetos e agregados da própria finalidade e atribuição | segregação por papel, escopo e contrato; sem RHIS/CRM implícito |
| Guivos — Comercial / gestão | funil, carteira, contratos, renovação, expansão e valores contratuais | `COM-001..012` dependem de autoridade, acesso e superfície interna definidos |
| Guivos — Customer Success | implantação, adoção, continuidade e relacionamento legitimamente atribuídos | não implica acesso irrestrito a contexto privado |
| Guivos — Intelligence/Data | qualidade, proveniência e outputs estritamente necessários | processamento não equivale a disclosure |

**Achado aberto:** a família `COM` consta deste master, mas os indicadores de funil global não devem ser mostrados à empresa cliente. Preservar os IDs aqui até adjudicação da superfície interna apropriada; não migrar, duplicar ou reclassificar automaticamente. Dados do próprio contrato do cliente podem ser apresentados apenas conforme autoridade de Planos e entitlement.

### 24.3 Camada decisória transversal proposta

Cada leitura executiva candidata deve responder, quando houver evidência e autorização: **o que ocorreu; em comparação a qual referência; o que pode explicar a variação; quais alternativas podem ser examinadas; e como verificar a intervenção**.

Campos adicionais de interpretação, sem substituir `GKR-INTELLIGENCE-KPI-CONTRACT-001`:

- `decision_supported`: decisão humana que o indicador pode informar;
- `comparison_reference`: período, baseline ou meta explicitamente qualificada;
- `investigation_hypotheses`: hipóteses revisáveis, sem causalidade presumida;
- `candidate_actions`: alternativas, nunca execução automática;
- `followup_evidence`: evidência necessária para reavaliar a decisão;
- `uncertainty_and_limitations`: limites, vieses, cobertura e natureza da evidência.

Esses campos são **candidatos de extensão**, não alterações ao contrato transversal vigente. Separar observado, declarado, inferido, estimado e previsto; baseline/meta não é realizado.

### 24.4 Contratos analíticos candidatos — PAR e PRG

| Referência | Questão / método candidato | Bloqueio semântico e de dados |
|---|---|---|
| PAR-001..003 | elegíveis, participantes distintos, participação = participantes únicos válidos / elegíveis × 100 | janela e elegibilidade temporal; coorte, denominador, eventos, disclosure e source |
| PAR-004..006 | eventos válidos, recorrência e distribuição por programa | taxonomia de eventos, deduplicação, janela e atribuição |
| PAR-C01 | ativação = pessoas com primeiro evento válido / coorte elegível × 100 | marco de ativação e janela não adjudicados |
| PAR-C02 | retenção = participantes de coorte que retornam em N períodos / coorte inicial × 100 | coorte, retorno e tratamento de saída não adjudicados |
| PAR-C03 | mediana do tempo entre elegibilidade e primeiro evento | datas válidas, censura e timezone pendentes |
| PAR-C04 | cobertura por programa = elegíveis alcançados / elegíveis do programa | definição de alcance e elegibilidade pendente |
| PRG-001..005 | programas/campanhas ativos, por finalidade, iniciados e encerrados | lifecycle, taxonomia, fontes e janela |
| PRG-C01 | ocupação = vagas confirmadas / capacidade válida × 100 | só aplicável a programas com capacidade |
| PRG-C02 | conclusão = participações concluídas / iniciadas elegíveis × 100 | marco de conclusão não definido |
| PRG-C03 | comparecimento = presenças confirmadas / inscrições válidas × 100 | só aplicável a programas com inscrição/presença |
| PRG-C04 | satisfação declarada = respostas favoráveis / válidas × 100 | instrumento, viés de resposta, proteção |
| PRG-C05 | reparticipação = pessoas que retornam / participantes elegíveis × 100 | possível sobreposição com PAR-005; avaliar antes de criar KPI |

Nenhuma taxa pode usar denominador zero; diferenciar `NO_DATA`, `INSUFFICIENT_DATA` e zero observado.

### 24.5 Contratos analíticos candidatos — BUD e PTS

| Referência | Questão / método candidato | Bloqueio |
|---|---|---|
| BUD-001..006 | carregado, concedido, disponível, concessões, beneficiados e Valor de Impacto Liberado | GEM-009, saldo, estorno, origem, tempo e finalidade |
| BUD-C01 | concessão relativa = concedido / carregado × 100, somente após reconciliação temporal e de saldos | estornos, carregamentos de períodos distintos e saldo anterior |
| BUD-C02 | custo por participante = custos atribuíveis / participantes únicos | composição e atribuição de custos |
| BUD-C03 | custo por participação = custos atribuíveis / participações válidas | custo e eventos comparáveis |
| BUD-C04 | custo por conclusão = custos atribuíveis / conclusões válidas | marco de conclusão e custo |
| BUD-C05 | projeção de necessidade = estimativa sob premissas, compromissos e cenários declarados | modelo, horizonte, incerteza, qualidade |
| BUD-C06 | concentração = orçamento concedido aos maiores programas / total concedido | critério de concentração e janela |
| BUD-C07 | cobertura = beneficiados / elegíveis ao benefício | elegibilidade e atribuição |
| PTS-001..004 | pontos concedidos, efetivamente utilizados, distribuição Mall/Travel/Journey e série temporal | atribuição, fonte, janela, proteção |
| PTS-C01 | utilização atribuível = pontos utilizados elegíveis / pontos concedidos elegíveis × 100 | coorte, saldos, expiração, reversões, atribuição |
| PTS-C02 | mediana do tempo entre concessão e utilização atribuível | eventos, atribuição e censura |

**Invariantes econômicos:** orçamento pré-pago de incentivos ≠ assinatura; concedido ≠ efetivamente utilizado; Pontos ≠ moeda por inferência; `BUD-006` não comprova impacto realizado. O denominador de `PTS-003` continua sendo **somente pontos efetivamente utilizados**, com categorias autorizadas fechando 100% quando aplicável. O contrato `GEM-009-MEASUREMENT-CONTRACT-001` consultado está em `draft`; fórmulas acima não são métricas econômicas aprovadas.

### 24.6 Contratos analíticos candidatos — JNY e INT

| Referência | Leitura candidata | Bloqueio |
|---|---|---|
| JNY-001..005 | acesso custeado, pessoas com acesso, ativação, participação e tendência agregada | autoridade Journey, evento, população, disclosure |
| JNY-C01 | cobertura = pessoas com acesso custeado / elegíveis ao custeio | elegibilidade e janela |
| JNY-C02 | continuidade de coortes com uso autorizado em janelas subsequentes | eventos autorizados, coortes, disclosure |
| JNY-C03 | tempo até ativação a partir da disponibilização | evento de ativação e tempo |
| JNY-C04 | acessos custeados não ativados / acessos elegíveis | sobreposição com JNY-003; não criar sem análise |
| INT-001..006 | interesses, tendências, emergências, aderência, lacunas e subutilização | legitimidade, evidência, explicabilidade, proteção |
| INT-C01..C09 | demanda por área; modalidade; território; horário; custo; capacidade; temas emergentes; resultados; cenários | primeiro testar como dimensões/aprofundamentos de INT-001/003/004/005/006; nenhum ID canônico |

**Método candidato de lacunas (`INT-005`):** confrontar interesse agregado legitimamente disponível com oportunidade, modalidade, território, horário, capacidade e critérios de compatibilidade documentados; expor limitações e hipóteses, não um score de necessidade individual. **Temas emergentes (`INT-003`):** separar crescimento observado, mudança de composição, tema novo, dado insuficiente e previsão. `INTERESSE ≠ CONDIÇÃO`; `CORRELAÇÃO ≠ CAUSALIDADE`; `COMPREENDER ≠ DECIDIR`. Custear Journey não dá acesso à Journey individual.

### 24.7 Contratos analíticos candidatos — COM e DQ

| Referência | Leitura candidata | Bloqueio |
|---|---|---|
| COM-001..012 | funil, contratos, conversão, renovação, expansão, downgrade, churn, valor anual e mix | GTM-002, GTM-003, GEM-009, superfície e consumidores |
| COM-C01 | conversão entre etapas do funil | lifecycle, coorte e deduplicação |
| COM-C02 | mediana do ciclo comercial | marcos temporais e encerramento |
| COM-C03 | receita recorrente contratada | contrato econômico; não confundir com ARR realizado |
| COM-C04 | retenção de receita | base e período elegíveis |
| COM-C05 | receita de expansão | mudanças contratuais válidas |
| COM-C06 | concentração de receita | população de contratos e método |
| COM-C07 | adoção inicial pós-contratação | marco de adoção e janela |
| COM-C08 | sinal explicável de risco de renovação | evidência, legitimidade e revisão humana |
| DQ-001..005 | freshness, indisponibilidade, supressão, rejeição e proveniência | SLA, registry, policy, taxonomia, fontes |
| DQ-C01..C06 | instrumentação, consistência de denominadores, cobertura de dados, estabilidade, qualidade de previsão, evidências | fontes, comparabilidade, versões e governança |

Métricas de funil e carteira globais são **candidatas a consumo interno Guivos**, não ao painel da empresa cliente. `GTM-003` fornece **baseline de planejamento**, não receita realizada nem preço oficial de plano Business. `SUPPRESSED_BY_POLICY` não é `ERROR`; `NOT_ENTITLED` não é `NO_DATA`.

### 24.8 Organização de leitura executiva proposta

1. **Visão Executiva:** composição autorizada de cobertura, participação, execução, tendência, lacunas e qualidade; sem namespace novo.
2. **Programas e Participação:** evolução, comparação, coortes e capacidade quando contratáveis.
3. **Benefícios e Orçamento:** carregado/concedido/disponível, alcance e eficiência econômica contratada.
4. **Pontos e Journey custeado:** utilização agregada protegida, sem histórico individual.
5. **Intelligence agregada:** tendências, adequação entre oferta e interesse, lacunas e cenários com incerteza.
6. **Relação contratual do cliente:** plano, vigência e serviços próprios, conforme autoridade de Planos.
7. **Gestão comercial Guivos:** funil e carteira internos, com superfície e acesso a adjudicar.
8. **Qualidade transversal:** atualização, fonte, disponibilidade, proveniência e supressão.

A tela executiva deve oferecer valor, referência, janela, população, natureza da evidência, hipótese e decisão humana possível; não afirmar resultados ou causalidade sem evidência.

### 24.9 Gates de adjudicação e aceite documental

| Gate | Requisito | Estado nesta extensão |
|---|---|---|
| G-BUS-01 | consumidores, superfície COM e matriz de disclosure aprovados | UNRESOLVED |
| G-BUS-02 | elegibilidade, coortes, eventos, janelas, deduplicação | UNRESOLVED |
| G-BUS-03 | contratos de fonte, atualização, qualidade e proveniência | SOURCE_PENDING e semântica parcial |
| G-BUS-04 | orçamento, custo, receita, estornos, Pontos, GEM-009 | BLOCKED_BY:GEM-009 |
| G-BUS-05 | legitimidade de agregados Journey/Intelligence e proteção | BLOCKED_BY:Journey/Intelligence/Privacy |
| G-BUS-06 | candidatos sem duplicidade, IDs canônicos e contratos completos | UNRESOLVED |
| G-BUS-07 | serving, RBAC, exportação e autorização de design/build | NOT_AUTHORIZED |

Para cada KPI que avance futuramente, aplicar o envelope integral de `GKR-INTELLIGENCE-KPI-CONTRACT-001`: identidade; fórmula; população; tempo; dimensões; acesso; source; qualidade; governança; interpretação; handoff. Nenhum `proposed` vira `source_pending` enquanto semântica material permanecer aberta.

**Estado desta extensão:** documentação de auditoria proposta; sem promoção de maturidade, sem conexão de dados, sem implementação, sem autorização de disclosure adicional e sem alteração dos anexos C/D/E/F.
