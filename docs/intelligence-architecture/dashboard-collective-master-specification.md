---
id: GKR-INTELLIGENCE-DASHBOARD-COLLECTIVE-001
title: Dashboard Coletivo — Documento Mestre de Especificação Analítica e Handoff Replit
status: draft
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-09-12
normative: false
maturity: governed_candidate_pre_implementation_dashboard_master
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-JOURNEY-COLLECTIVE-001
  - UXA-014
  - UXA-019
  - GAI-001
  - GAI-002
  - GIA-COG-001
  - GEM-009-MEASUREMENT-CONTRACT-001
related:
  - UXA-100
  - UXA-100-A3
  - UXA-100-A4
---

# Dashboard Coletivo — Documento Mestre de Especificação Analítica e Handoff Replit

## 1. Finalidade

Este documento constitui o **draft governado do Anexo D** de `GKR-INTELLIGENCE-DASHBOARD-KPI-001` para o **Dashboard Coletivo**.

Seu objetivo é consolidar, antes de qualquer implementação, o recorte analítico legítimo da atuação de um Coletivo, de suas atividades, participações, vínculos, decisões, relações, evidências e capacidades dentro das autoridades vigentes.

O Dashboard Coletivo deve apoiar compreensão coletiva sem converter Pessoas em recursos do Coletivo, sem transformar participação em obrigação, sem confundir popularidade com avanço e sem produzir reputação por inferência.

Regra central:

> **O Coletivo pode compreender sua própria atuação, participação autorizada, governança, relações, aprendizados, evidências e capacidade; ele não recebe autoridade geral sobre a Journey, identidade, evolução ou contexto privado das Pessoas participantes.**

Este master não redefine a experiência autenticada principal do Coletivo, não cria Início, menu, Surface Map, State Map, wireframe, RBAC técnico ou implementação.

```text
DASHBOARD COLETIVO
≠ INÍCIO AUTENTICADO DO COLETIVO
≠ SURFACE MAP
≠ STATE MAP
≠ REDE SOCIAL GENÉRICA
≠ GUIVOS BUSINESS
≠ ADS
```

---

## 2. Autoridades de domínio e precedência

| Autoridade | Papel neste master |
|---|---|
| `GKR-INTELLIGENCE-DASHBOARD-KPI-001` | envelope transversal de KPI, acesso, disclosure e handoff |
| `GKR-UX-ORGCOL-AUTH-JOBS-001` | atores, autoridade, limites e jobs autenticados do Coletivo |
| `GKR-UX-ORGCOL-AUTH-IA-001` | domínios de informação e separação entre síntese, atividade, participação, governança, relações, evidência e capacidade |
| `GKR-JOURNEY-COLLECTIVE-001` | continuidade integrada e maturidade dos fluxos especializados do Coletivo |
| `UXA-014` | fundamento funcional de Organização e Coletivo |
| `UXA-019` | autoridade bilateral e ciclo de relações Organização ↔ Coletivo |
| `GAI-001 / GAI-002 / GIA-COG-001` | evidência, natureza de afirmações, explicabilidade e `COMPREENDER ≠ DECIDIR` |
| `GEM-009-MEASUREMENT-CONTRACT-001` | composição obrigatória caso métricas econômicas venham a ser introduzidas |
| `UXA-100 / A3 / A4` | fluxo especializado de Planos e capacidade do Coletivo |

Em caso de conflito, este master preserva a autoridade especializada mais restritiva e mantém o indicador bloqueado até adjudicação própria.

---

## 3. Estado e boundary

```text
GKR-INTELLIGENCE-DASHBOARD-COLLECTIVE-001
→ DRAFT v0.1.0
→ CANDIDATE PRE-IMPLEMENTATION DASHBOARD MASTER

COLETIVO
→ PARTICIPANT TYPE
→ COLETIVO ≠ ORGANIZAÇÃO
→ COLETIVO ≠ GUIVOS BUSINESS

DASHBOARD COLETIVO
→ ANALYTICAL CONSUMPTION SURFACE
→ NOT SOURCE OF TRUTH
→ NOT AUTHENTICATED START SURFACE
→ NOT OPERATIONAL SYSTEM OF RECORD

REAL DATA CONNECTION
→ NOT AUTHORIZED BY THIS DOCUMENT

REPLIT BUILD
→ NOT AUTHORIZED BY THIS DOCUMENT
→ HANDOFF SPECIFICATION ONLY

PERSON-LEVEL PRIVATE CONTEXT
→ NOT PART OF DEFAULT COLLECTIVE DISCLOSURE

PERSONAL JOURNEY
→ NOT DISCLOSED TO COLLECTIVE BY DEFAULT
```

Pertencimento, participação, papel aceito, moderação, representação e autoridade permanecem conceitos distintos.

```text
PARTICIPANTE
≠ ADMINISTRADOR
≠ MODERADOR
≠ REPRESENTANTE

PERTENCIMENTO
≠ AUTORIDADE

PARTICIPAÇÃO
≠ OBRIGAÇÃO PERMANENTE
```

---

## 4. Relação com a experiência autenticada do Coletivo

A Arquitetura da Informação autenticada organiza o Coletivo em sete domínios principais e uma capacidade comercial contextual:

```text
Início
Atividades e Oportunidades
Participação
Governança e Proteção
Relações
Aprendizados e Evidências
Coletivo e Autoridade
Planos e Capacidade [especializado / contextual]
```

Este Dashboard não substitui esses domínios.

O `Início` autenticado deve sintetizar propósito, Momento coletivo, atenção material, decisões abertas e Próximos Passos. Ele não deve ser reduzido a painel de números, feed, ranking ou placar de popularidade.

```text
SÍNTESE DO MOMENTO COLETIVO
≠ DASHBOARD

DASHBOARD
→ PODE APOIAR COM LEITURAS ANALÍTICAS AUTORIZADAS
→ NÃO DEFINE O MOMENTO COLETIVO SOZINHO
```

A existência deste master não promove mapa de superfícies, estados, fluxos principais, wireframes ou implementação da experiência autenticada.

---

## 5. Áreas analíticas candidatas

O Dashboard Coletivo é organizado em **nove áreas analíticas**:

1. Visão Analítica Coletiva;
2. Atividades e Oportunidades;
3. Participação e Vínculos;
4. Governança, Decisões e Proteção;
5. Relações Institucionais;
6. Aprendizados, Evidências e Resultados;
7. Planos e Capacidade;
8. Território e Demografia Autorizados;
9. Qualidade, Freshness, Privacidade e Governança do Dado.

A área de Visão Analítica Coletiva compõe leituras das famílias governadas neste master. Ela não constitui família KPI autônoma.

```text
ÁREA DOCUMENTADA
≠ KPI DEFINIDO
≠ DADO DISPONÍVEL
≠ DISCLOSURE AUTORIZADO
≠ IMPLEMENTAÇÃO AUTORIZADA
```

---

## 6. Classes funcionais de consumo

As classes abaixo são conceituais e não constituem RBAC técnico implementado:

| Classe funcional | Escopo candidato |
|---|---|
| Coletivo — visão coletiva | agregados do próprio Coletivo e objetos sob sua autoridade |
| Coletivo — operação | atividades, oportunidades, participação e relações sob escopo legítimo |
| Coletivo — governança/proteção | decisões, consultas, contestação e proteção estritamente necessárias ao papel autorizado |
| Coletivo — aprendizados/prestação de contas | evidências, aprendizados e resultados permitidos |
| Coletivo — capacidade/comercial | plano vigente, capacidade e eventos de plano autorizados |
| Coletivo — Data/BI | exportações ou APIs do próprio recorte quando autorizadas |
| Guivos — operação/suporte | dados necessários à finalidade operacional autorizada |
| Guivos — Intelligence/Data | inputs e outputs necessários à finalidade analítica autorizada |

```text
SER RESPONSÁVEL PELO COLETIVO
≠ ACESSO A TODO DADO DO COLETIVO

PERTENCER AO COLETIVO
≠ ACESSO A DADOS DE OUTROS PARTICIPANTES

DADO AGREGADO
≠ AUTOMATICAMENTE SEGURO PARA DISCLOSURE
```

---

## 7. Vocabulário de KPI e readiness

Prefixo deste master:

```text
COL-KPI-<FAMÍLIA>-NNN
```

Famílias iniciais:

- `ACT` — atividades e oportunidades;
- `PAR` — participação, solicitações e vínculos;
- `GOV` — governança, decisões e proteção;
- `REL` — relações institucionais;
- `EVD` — aprendizados, evidências e resultados;
- `CAP` — planos e capacidade;
- `GEO` — território e demografia autorizados;
- `DQ` — qualidade, freshness, privacidade e governança.

A **Visão Analítica Coletiva** compõe indicadores dessas famílias e não cria namespace próprio nesta versão.

Estados usados:

| Status | Significado |
|---|---|
| `proposed` | significado ou contrato ainda incompleto; não build-ready |
| `source_pending` | semântica fechada o suficiente, mas source/data contract ainda bloqueia readiness |
| `defined` | contrato documental mínimo completo; ainda requer gates de domínio e build |
| `approved-equivalent` | autoridade especializada fornece estado equivalente aceito pelo gate |

Nesta versão, **todos os KPIs candidatos permanecem `proposed / NOT_READY`**.

---

## 8. Reputação — bloqueio explícito

O master global preserva `Reputação` como conceito ainda não definido para este dashboard.

Consequentemente:

```text
REPUTAÇÃO
→ BLOCKED
→ NOT A KPI FAMILY
→ NO FORMULA
→ NO SCORE
→ NO RANKING
→ NO AUTOMATIC DERIVATION FROM ACTIVITY OR PARTICIPATION
```

Qualquer futura métrica de reputação exigirá, por ato próprio e antes de materialização:

- definição semântica;
- finalidade legítima;
- fórmula;
- população e unidade de análise;
- autoridade de leitura;
- contestação e correção;
- riscos de incentivo e discriminação;
- proteção contra retaliação;
- governança e responsável;
- critérios de validade e expiração;
- explicabilidade proporcional.

```text
MAIS MEMBROS
≠ MAIOR REPUTAÇÃO

MAIS ATIVIDADE
≠ MAIOR REPUTAÇÃO

MAIS PUBLICAÇÕES
≠ MAIOR REPUTAÇÃO

PAUSA / RECUSA / SAÍDA
≠ REPUTAÇÃO NEGATIVA
```

Este draft não cria `COL-KPI-REP-*`.

---

## 9. Família ACT — Atividades e Oportunidades

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| COL-KPI-ACT-001 | Atividades válidas | atividades do Coletivo em estados válidos dentro do recorte autorizado | atividades | proposed | activity taxonomy + lifecycle + source |
| COL-KPI-ACT-002 | Atividades ativas | atividades em estado ativo válido na janela | atividades | proposed | active-state + temporal contract |
| COL-KPI-ACT-003 | Atividades concluídas no período | atividades com conclusão operacional válida no período | atividades/período | proposed | completion event + window |
| COL-KPI-ACT-004 | Oportunidades válidas | oportunidades do Coletivo em estados válidos | oportunidades | proposed | opportunity state + source |
| COL-KPI-ACT-005 | Oportunidades ativas | oportunidades em estado ativo válido na janela | oportunidades | proposed | active-state + temporal contract |
| COL-KPI-ACT-006 | Distribuição por Domínio de Evolução | distribuição autorizada de atividades/oportunidades por `JED-*` aplicável | distribuição | proposed | domain-link semantics + denominator |

Regras:

```text
ATIVIDADE REALIZADA
≠ RESULTADO
≠ IMPACTO

ATIVIDADE EM JED-*
≠ PARTICIPANTE CLASSIFICADO NESSE DOMÍNIO

PUBLICAÇÃO
≠ DISTRIBUIÇÃO GARANTIDA
≠ RELEVÂNCIA
```

---

## 10. Família PAR — Participação, solicitações e vínculos

Esta família mede somente relações de participação legitimamente vinculadas ao Coletivo.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| COL-KPI-PAR-001 | Solicitações válidas | solicitações de participação válidas no recorte autorizado | solicitações | proposed | request lifecycle + source |
| COL-KPI-PAR-002 | Solicitações abertas | solicitações ainda abertas em estado válido | solicitações | proposed | open-state contract |
| COL-KPI-PAR-003 | Vínculos ativos | vínculos de pertencimento em estado ativo válido | vínculos | proposed | belonging lifecycle + source |
| COL-KPI-PAR-004 | Participantes únicos | Pessoas distintas com vínculo/participação válida segundo contrato aplicável | pessoas | proposed | population + purpose + disclosure |
| COL-KPI-PAR-005 | Participações válidas | eventos de participação válidos no período e finalidade autorizada | eventos | proposed | participation taxonomy + source |
| COL-KPI-PAR-006 | Pausas e saídas no período | eventos legítimos de pausa/saída sem valoração reputacional | eventos | proposed | pause/exit semantics + temporal contract |
| COL-KPI-PAR-007 | Papéis aceitos por classe | distribuição agregada de papéis voluntariamente aceitos quando legítima e segura | distribuição | proposed | role semantics + disclosure |

Regras:

```text
SOLICITAÇÃO
≠ PERTENCIMENTO

PERTENCIMENTO
≠ FUNÇÃO
≠ MODERAÇÃO
≠ REPRESENTAÇÃO

PARTICIPAÇÃO
≠ CONSENTIMENTO PARA TODO USO DE DADO

PAUSA / SAÍDA
→ NÃO É FALHA POR PADRÃO
```

Pessoa individual não é nível padrão de drill-down deste dashboard.

---

## 11. Família GOV — Governança, decisões e proteção

Esta família exige proteção reforçada porque pode envolver decisões, conflitos, moderação, contestação e segurança.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| COL-KPI-GOV-001 | Decisões abertas | decisões coletivas formalmente abertas segundo a regra de governança aplicável | decisões | proposed | decision/governance contract |
| COL-KPI-GOV-002 | Consultas abertas | consultas legitimamente abertas e ainda vigentes | consultas | proposed | consultation semantics + authority |
| COL-KPI-GOV-003 | Decisões concluídas | decisões com encerramento válido no período | decisões/período | proposed | decision lifecycle + temporal contract |
| COL-KPI-GOV-004 | Contestações/revisões abertas | processos de contestação ou revisão materialmente abertos | processos | proposed | contestation semantics + restricted disclosure |
| COL-KPI-GOV-005 | Casos de proteção/moderação abertos | casos legitimamente classificados e acessíveis somente ao papel autorizado | casos | proposed | protection taxonomy + sensitivity + access |
| COL-KPI-GOV-006 | Casos revisados/encerrados | casos concluídos segundo processo governado | casos/período | proposed | lifecycle + evidence + restricted disclosure |

```text
CONSULTA
≠ VOTAÇÃO UNIVERSAL
≠ OBRIGAÇÃO DE RESPOSTA

ACESSO TÉCNICO
≠ AUTORIDADE DE GOVERNANÇA

CONTAGEM DE CASOS DE PROTEÇÃO
≠ DISCLOSURE AUTOMATICAMENTE SEGURO
```

Nenhum destes indicadores autoriza exposição de denúncia, conflito, vulnerabilidade ou identidade de Pessoa além do mínimo necessário à finalidade e autoridade aplicáveis.

---

## 12. Família REL — Relações institucionais

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| COL-KPI-REL-001 | Relações ativas | relações institucionais do Coletivo em estado ativo válido | relações | proposed | UXA-019 + lifecycle/source |
| COL-KPI-REL-002 | Relações por contraparte/tipo | distribuição agregada por classe legitimamente definida | distribuição | proposed | taxonomy + disclosure |
| COL-KPI-REL-003 | Propostas de relação abertas | propostas bilaterais ainda abertas em estado válido | propostas | proposed | bilateral state contract |
| COL-KPI-REL-004 | Relações em revisão | relações com revisão material válida em andamento | relações | proposed | review-state contract |
| COL-KPI-REL-005 | Relações pausadas/encerradas no período | eventos válidos de pausa/encerramento | relações/período | proposed | lifecycle + temporal contract |

```text
APOIO
≠ PROPRIEDADE

PATROCÍNIO
≠ GOVERNO

INFRAESTRUTURA
≠ AUTORIDADE SOBRE PERTENCIMENTO
```

Quantificar uma relação não transfere ao patrocinador, Organização ou contraparte autoridade sobre a governança interna do Coletivo.

---

## 13. Família EVD — Aprendizados, evidências e resultados

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| COL-KPI-EVD-001 | Aprendizados registrados | aprendizados coletivos válidos e documentados no recorte autorizado | aprendizados | proposed | learning semantics + source |
| COL-KPI-EVD-002 | Evidências registradas | evidências coletivas válidas associadas ao recorte | evidências | proposed | evidence validity + source |
| COL-KPI-EVD-003 | Contribuições registradas | contribuições legitimamente registradas sem ranking automático de Pessoas | contribuições | proposed | contribution semantics + source |
| COL-KPI-EVD-004 | Resultados autorizados | resultados com definição e evidência suficientes para a afirmação permitida | resultados | proposed | claim/evidence contract |
| COL-KPI-EVD-005 | Itens sem evidência suficiente | objetos cuja afirmação pretendida não possui evidência suficiente | itens | proposed | evidence sufficiency contract |
| COL-KPI-EVD-006 | Revisões/correções de evidência | eventos de revisão ou correção materialmente válidos | eventos | proposed | provenance + correction lifecycle |

```text
MAIS MEMBROS
≠ MAIS AVANÇO

MAIS PUBLICAÇÕES
≠ MAIS CONTRIBUIÇÃO

ATIVIDADE
≠ RESULTADO

RESULTADO
≠ IMPACTO

CORRELAÇÃO
≠ CAUSALIDADE
```

Nenhuma métrica desta família cria score universal de impacto, reputação, legitimidade ou valor de Pessoa.

---

## 14. Família CAP — Planos e capacidade

O Coletivo possui fluxo especializado de Planos com taxonomia `Livre / Mobiliza / Impacta / Rede`.

O nome comercial `Impacta` não constitui prova de impacto produzido.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| COL-KPI-CAP-001 | Plano coletivo vigente | classificação do plano vigente quando contratualmente confirmada | categoria | proposed | plan source + entitlement contract |
| COL-KPI-CAP-002 | Uso de capacidade | uso da capacidade definida pelo plano no ciclo aplicável | unidade/% | proposed | entitlement + cycle + source |
| COL-KPI-CAP-003 | Capacidade disponível | capacidade ainda disponível conforme contrato de plano | unidade/% | proposed | entitlement + balance semantics |
| COL-KPI-CAP-004 | Eventos de alteração de plano | upgrades/downgrades/cancelamentos confirmados no período | eventos | proposed | plan lifecycle + source |

```text
PLANO PAGO
≠ RELEVÂNCIA
≠ LEGITIMIDADE
≠ AUTORIDADE
≠ IMPACTO
≠ ACESSO AO CONTEXTO PESSOAL

PLANO "IMPACTA"
≠ IMPACTO COMPROVADO
```

Preço, entitlement, quota ou benefício não congelado não pode ser inventado pelo dashboard.

Qualquer métrica monetária futura relacionada a plano, apoio, patrocínio ou outra relação econômica deve compor com `GEM-009-MEASUREMENT-CONTRACT-001` e com o contrato de domínio aplicável.

---

## 15. Família GEO — território e demografia autorizados

Leituras territoriais e demográficas devem operar por minimização e proteção contra reidentificação.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| COL-KPI-GEO-001 | Distribuição territorial autorizada | distribuição agregada de participação/vínculos por recorte territorial legítimo | distribuição | proposed | geography source + disclosure threshold |
| COL-KPI-GEO-002 | Cobertura territorial de atividades | distribuição das atividades/oportunidades por território aplicável | distribuição | proposed | object geography semantics |
| COL-KPI-GEO-003 | Perfil demográfico agregado autorizado | distribuição agregada apenas de atributos permitidos para finalidade legítima | distribuição | proposed | privacy + purpose + thresholds + source |

```text
DEMOGRAFIA DISPONÍVEL
≠ DEMOGRAFIA NECESSÁRIA
≠ DEMOGRAFIA EXIBÍVEL

SEGMENTO PEQUENO
→ PODE EXIGIR SUPRESSÃO
```

O Coletivo não recebe dados demográficos individuais por padrão por meio deste dashboard.

Domínio de Evolução de uma atividade não pode ser usado para inferir atributo sensível ou classificação pessoal dos participantes.

---

## 16. Família DQ — qualidade, freshness, privacidade e governança

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| COL-KPI-DQ-001 | Freshness compliance | contratos/datasets dentro do SLA / monitorados | % | proposed | freshness/SLA contract |
| COL-KPI-DQ-002 | Indicadores indisponíveis | KPIs esperados sem dado utilizável | quantidade | proposed | registry + availability rules |
| COL-KPI-DQ-003 | Supressões de disclosure | células/segmentos protegidos por política | quantidade | proposed | disclosure policy |
| COL-KPI-DQ-004 | Eventos rejeitados | eventos coletivos rejeitados por validação | eventos | proposed | validation taxonomy |
| COL-KPI-DQ-005 | Completude de proveniência | outputs com proveniência suficiente / outputs avaliados | % | proposed | provenance contract |

Qualidade qualifica confiança; não deve fabricar aparência de precisão.

---

## 17. Filtros candidatos

Filtros somente podem restringir o escopo autorizado:

- período e comparação de período;
- atividade/oportunidade;
- estado do objeto;
- tipo de participação/vínculo quando legítimo;
- papel aceito agregado quando disclosure permitir;
- classe de decisão/processo de governança;
- relação/contraparte quando disclosure permitir;
- Domínio de Evolução da atividade quando legitimamente aplicável;
- território autorizado;
- plano/ciclo de capacidade;
- natureza de evidência;
- classe de resultado.

```text
FILTRO
→ SUBCONJUNTO DO ACCESS SCOPE
→ NUNCA AMPLIA DISCLOSURE
```

Filtros de proteção, moderação, contestação ou identidade exigem proteção adicional e não são automaticamente disponíveis para toda pessoa responsável pelo Coletivo.

---

## 18. Drill-down

Estrutura candidata:

```text
N0 — COLETIVO AUTORIZADO
→ N1 — FAMÍLIA ANALÍTICA
→ N2 — OBJETO / PERÍODO / SEGMENTO AUTORIZADO
→ N3 — OBJETO OPERACIONAL / RELAÇÃO / PROCESSO AUTORIZADO
```

Pessoa individual não é nível padrão de drill-down.

A identificação excepcional de Pessoa exige finalidade, autoridade, minimização, sensibilidade e trilha próprias fora da inferência automática deste master.

```text
AGREGADO DE PARTICIPAÇÃO
→ NÃO CRIA DIREITO DE ABRIR JOURNEY INDIVIDUAL
```

---

## 19. Estados obrigatórios de visualização

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

`NOT_ENTITLED` não significa erro técnico.

`SUPPRESSED_BY_POLICY` não deve ser mascarado como ausência de ocorrência.

Em famílias sensíveis, a própria existência de um dado pode exigir tratamento de disclosure antes de indicar quantidade.

---

## 20. Contratos lógicos esperados

Sem definir schema físico, o Dashboard Coletivo poderá futuramente consumir contratos equivalentes a:

- Collective Aggregate;
- Activity / Opportunity Aggregate;
- Participation Request Aggregate;
- Membership / Link Aggregate;
- Participation Aggregate;
- Governance Decision / Consultation Aggregate;
- Protection / Moderation Status Aggregate;
- Institutional Relationship Aggregate;
- Learning / Evidence / Authorized Result Aggregate;
- Plan / Capacity Aggregate;
- Geography / Demography Aggregate;
- Data Quality / Freshness Status.

Cada payload deve carregar, quando aplicável, `metric_id`, período, valor, unidade, population scope, source version, freshness, natureza da evidência, access class, suppression state, proveniência e confidence/uncertainty quando material.

---

## 21. Integrações e minimização

O dashboard não pressupõe ingestão integral de bases de membros, mensageria, sistemas externos, CRM, ERP ou fontes de terceiros.

```text
SOURCE AUTORIZADA
→ EVENTO / AGREGADO MÍNIMO NECESSÁRIO
→ CONTRATO DO KPI
→ SERVING AUTORIZADO
→ DASHBOARD COLETIVO
```

Exportação estruturada/API para ferramentas analíticas externas depende de entitlement, contrato de dados, segurança, finalidade e escopo específicos.

---

## 22. Orientação futura para Replit

Quando houver autorização formal de build, a ferramenta deverá:

1. não inventar KPI, fórmula, preço, entitlement, threshold, source, schema ou permissão;
2. usar `COL-KPI-*` como identificadores estáveis, não labels visuais;
3. bloquear KPIs `proposed` e `source_pending` para consumo canônico com dado real;
4. preservar Coletivo ≠ Organização e Coletivo ≠ Guivos Business;
5. não transformar Dashboard em Início autenticado, feed ou rede social genérica;
6. não criar `COL-KPI-REP-*`, ranking ou reputação por inferência;
7. não criar score universal de impacto, legitimidade, contribuição ou valor de Pessoa;
8. não expor Journey individual;
9. não converter pertencimento em papel ou autoridade;
10. não inferir causalidade de correlações;
11. separar atividade, participação, aprendizado, evidência, resultado e impacto;
12. tratar filtros como restrição adicional;
13. validar escopo no serving/backend, não somente no cliente;
14. separar mock adapters de real adapters;
15. preservar `NO_DATA`, `INSUFFICIENT_DATA`, `SUPPRESSED_BY_POLICY`, `NOT_ENTITLED` e `SOURCE_DELAYED`;
16. preservar versão, freshness e proveniência;
17. não hard-code preços ou entitlements não congelados;
18. não converter plano pago em relevância, legitimidade ou impacto;
19. não implementar exportação individual por conveniência;
20. preservar proteção e não retaliação em dados de contestação/moderação;
21. registrar a versão deste master usada na build.

---

## 23. Critérios de aceite para futuro handoff

Antes de qualquer release `READY FOR BUILD`:

```text
[ ] KPI selecionado = defined OU approved-equivalent
[ ] pergunta/finalidade fechadas
[ ] população/elegibilidade definidas
[ ] fórmula e componentes definidos
[ ] janela temporal/granularidade definidas
[ ] source/data contract definido
[ ] access/disclosure definido
[ ] thresholds de proteção definidos quando aplicáveis
[ ] filtros/drill-down definidos
[ ] null/zero/no-data definidos
[ ] freshness/quality checks definidos
[ ] governança/proteção possui acesso e sensibilidade específicos
[ ] relações preservam bilateralidade e autonomia
[ ] participação preserva voluntariedade
[ ] Journey individual permanece protegida
[ ] natureza da evidência e claims permitidos estão definidos
[ ] reputação permanece bloqueada salvo autoridade própria posterior
[ ] métricas econômicas, se houver, compõem com GEM-009
[ ] Design/build authorization foi emitida
```

---

## 24. Itens explicitamente bloqueados nesta versão

```text
REAL DATA
→ NOT AUTHORIZED

BACKEND / API FÍSICA
→ NOT DEFINED HERE

TECHNICAL RBAC
→ NOT IMPLEMENTED

AUTHENTICATED START / SURFACE MAP / STATE MAP
→ NOT DEFINED BY THIS DOCUMENT

FINAL VISUAL DESIGN
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

PERSON-LEVEL JOURNEY DISCLOSURE
→ NOT AUTHORIZED

REPUTATION KPI / SCORE / RANKING
→ BLOCKED / NOT DEFINED

UNIVERSAL IMPACT / LEGITIMACY / CONTRIBUTION SCORE
→ NOT AUTHORIZED

CROSS-COLLECTIVE ACCESS
→ NOT AUTHORIZED

GUIVOS BUSINESS ANALYTICS
→ OUTSIDE THIS MASTER
→ ANNEX B REMAINS SEPARATE

ORGANIZATION ANALYTICS
→ OUTSIDE THIS MASTER
→ ANNEX C REMAINS SEPARATE

ADS ANALYTICS
→ OUTSIDE THIS MASTER
→ ANNEX F REMAINS SEPARATE
```

---

## 25. Estado final desta versão

```text
GKR-INTELLIGENCE-DASHBOARD-COLLECTIVE-001
→ DRAFT v0.1.0
→ ANNEX D CANDIDATE MASTER
→ PRE-IMPLEMENTATION

AUTHENTICATED EXPERIENCE AUTHORITIES
→ GKR-UX-ORGCOL-AUTH-JOBS-001 + GKR-UX-ORGCOL-AUTH-IA-001 PRESERVED

ANALYTICAL AREAS
→ 9

KPI FAMILIES
→ ACT / PAR / GOV / REL / EVD / CAP / GEO / DQ

REPUTATION
→ BLOCKED
→ NO KPI FAMILY MATERIALIZED

KPI IMPLEMENTATION READINESS
→ NONE CLAIMED BY INFERENCE
→ ALL CURRENT KPIs = proposed
→ ALL = NOT_READY

COLLECTIVE POPULATION
→ ONLY OWN / LEGITIMATELY AUTHORIZED RELATIONS, PARTICIPATIONS AND POPULATIONS

PERSON PRIVATE CONTEXT / INDIVIDUAL JOURNEY
→ NOT DEFAULT COLLECTIVE DISCLOSURE

COLLECTIVE AUTHENTICATED START / SURFACE MAP / STATE MAP
→ NOT MATERIALIZED BY THIS DOCUMENT

REAL DATA / BACKEND / API / TECHNICAL RBAC / PRODUCTION
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

ANNEX E / F
→ UNCHANGED / NOT MATERIALIZED BY THIS DOCUMENT
```

A promoção deste draft para master materializado exige reconciliação explícita do registry do master global, validação semântica/mecânica e review governado da PR correspondente.