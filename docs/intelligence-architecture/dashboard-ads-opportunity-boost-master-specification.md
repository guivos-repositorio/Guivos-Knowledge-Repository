---
id: GKR-INTELLIGENCE-DASHBOARD-ADS-001
title: Dashboard Ads / Opportunity Boost — Documento Mestre de Especificação Analítica e Handoff Replit
status: draft
version: 0.1.0
owner: Guivos Intelligence Architecture
last_updated: 2026-09-13
normative: false
maturity: governed_candidate_pre_implementation_dashboard_master
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GPA-007
  - GEM-007-ADS-ECONOMIC-ROLE-001
  - GEM-007-A1
  - GEM-010-A2
  - GEM-009-MEASUREMENT-CONTRACT-001
  - GEM-007-CROSS-PRODUCT-VALUE-ATTRIBUTION-001
  - GAI-001
  - GAI-002
  - GIA-COG-001
related:
  - RF-06
  - RF-07
  - RF-09
  - UXA-038
  - GKR-UX-HOME-ADS-MASTER-001
---

# Dashboard Ads / Opportunity Boost — Documento Mestre de Especificação Analítica e Handoff Replit

## 1. Finalidade

Este documento constitui o **draft governado do Anexo F** de `GKR-INTELLIGENCE-DASHBOARD-KPI-001` para **Ads / Opportunity Boost Analytics**.

Seu objetivo é consolidar, antes de qualquer implementação, o recorte analítico legítimo pelo qual um anunciante autorizado e as funções internas competentes da Guivos poderão compreender **campanhas e objetos patrocinados, entrega em inventário autorizado, eventos válidos, Opportunity Boost, orçamento e reconciliação, outcomes legitimamente instrumentados, resultados declarados explicitamente identificados como autorrelato, agregados permitidos, qualidade, antifraude, freshness e proveniência**.

O dashboard deve apoiar mensuração comercial responsável sem transformar pagamento em relevância orgânica, evento em resultado, correlação em causalidade, participante em lead vendável ou contexto pessoal protegido em matéria-prima publicitária.

Regra central:

> **Ads pode medir a entrega comercial legitimamente autorizada e os eventos que seu contrato sustenta; não pode comprar relevância orgânica, inferir causalidade sem evidência, ampliar disclosure do participante ou prometer resultado que a mensuração não suporta.**

Este master não cria Home Ads, checkout, campaign manager, buying console, inventário operacional, regra de bidding, modelo de attribution, tabela pública de preços, cobrança real, backend, API, RBAC técnico, Design/UI ou implementação.

```text
ADS / OPPORTUNITY BOOST ANALYTICS
≠ GUIVOS ADS HOME
≠ CAMPAIGN MANAGER
≠ MEDIA BUYING CONSOLE
≠ CHECKOUT
≠ ORGANIC RANKING
≠ PERSONAL RECOMMENDATION
≠ PERSON INTELLIGENCE
≠ SOURCE OF TRUTH
≠ ATTRIBUTION MODEL
```

---

## 2. Autoridades de domínio e precedência

| Autoridade | Papel neste master |
|---|---|
| `GKR-INTELLIGENCE-DASHBOARD-KPI-001` | envelope transversal de KPI, acesso, disclosure e handoff |
| `GPA-007` | autoridade de Produto Guivos Ads, seus limites e relação com superfícies anfitriãs |
| `GKR-UX-HOME-ADS-MASTER-001` | governa exclusivamente a Home Pública Ads v1 e seus limites narrativos/comerciais; não define Ads Analytics |
| `UXA-038` | contrato funcional do Opportunity Boost, incluindo estados, controles e relatório do anunciante |
| `GEM-007-ADS-ECONOMIC-ROLE-001` | papel econômico de Ads, eventos econômicos candidatos, riscos e guardrails |
| `GEM-007-A1` | contrato econômico e entre produtos do Opportunity Boost |
| `GEM-010-A2` | baseline candidata de preços, orçamento e mensuração; não autoriza oferta pública ou faturamento |
| `GEM-009-MEASUREMENT-CONTRACT-001` | contrato mínimo de métrica econômica; permanece autoridade em estado `draft` |
| `GEM-007-CROSS-PRODUCT-VALUE-ATTRIBUTION-001` | princípios de attribution e limites; modelo/janela/pesos/algoritmo continuam não definidos |
| `GAI-001 / GAI-002 / GIA-COG-001` | evidência, proveniência, incerteza, explicabilidade e `COMPREENDER ≠ DECIDIR` |

Em caso de conflito, prevalece a autoridade especializada mais restritiva. O fato de um documento econômico conter parâmetro candidato não converte esse parâmetro em preço vigente, fórmula aprovada, source disponível ou regra operacional.

```text
PARÂMETRO CANDIDATO
≠ PREÇO VIGENTE
≠ FATURAMENTO AUTORIZADO
≠ REGRA OPERACIONAL APROVADA

DOCUMENTO DRAFT DE ATTRIBUTION
≠ MODELO DE ATTRIBUTION DEFINIDO
```

`GKR-UX-HOME-ADS-MASTER-001` está materializado em `docs/experience-architecture/public-home-ads-master-document.md` e governa exclusivamente a **Home Pública do Guivos Ads v1**, voltada à descoberta e qualificação comercial. Este Anexo F governa um recorte analítico distinto e não redefine a Home, sua narrativa, conversão ou futura implementação.

```text
HOME PÚBLICA ADS
→ DESCOBERTA / EXPLICAÇÃO / QUALIFICAÇÃO COMERCIAL

ADS ANALYTICS
→ CONSUMO ANALÍTICO AUTORIZADO

HOME ADS
≠ DASHBOARD ADS
≠ CAMPAIGN MANAGER
≠ CHECKOUT
```

---

## 3. Estado e boundary

```text
GKR-INTELLIGENCE-DASHBOARD-ADS-001
→ DRAFT v0.1.0
→ CANDIDATE PRE-IMPLEMENTATION DASHBOARD MASTER

GUIVOS ADS
→ SERVICE LAYER PRODUCT
→ COMMERCIAL AUTHORITY OVER AUTHORIZED AD RELATION / INVENTORY / MEASUREMENT
→ NOT AUTHORITY OVER HOST PRODUCT ORGANIC MEANING

DASHBOARD ADS
→ ANALYTICAL CONSUMPTION SURFACE
→ NOT SOURCE OF TRUTH
→ NOT CAMPAIGN OPERATION SYSTEM
→ NOT BILLING LEDGER
→ NOT ATTRIBUTION ENGINE

REAL DATA CONNECTION
→ NOT AUTHORIZED BY THIS DOCUMENT

REPLIT BUILD
→ NOT AUTHORIZED BY THIS DOCUMENT
→ HANDOFF SPECIFICATION ONLY

PROCESSING AUTHORIZED
≠ DISCLOSURE AUTHORIZED

ADVERTISER RELATIONSHIP
≠ ACCESS TO PRIVATE PERSON JOURNEY
```

---

## 4. Separação entre orgânico, patrocinado e mensuração

A autoridade vigente exige separação explícita entre relevância orgânica e distribuição paga.

```text
PAGAMENTO
≠ RELEVÂNCIA ORGÂNICA
≠ RECOMENDAÇÃO
≠ PRÓXIMO PASSO
≠ QUALIDADE
≠ CONFIANÇA
≠ IMPACTO

INVENTÁRIO PATROCINADO
≠ RANKING ORGÂNICO

EXPOSIÇÃO PATROCINADA
≠ PERTINÊNCIA PESSOAL
```

A superfície anfitriã preserva autoridade sobre contexto, segurança, acessibilidade, densidade, controles e finalidade funcional. Ads governa a relação comercial publicitária, o inventário autorizado, a identificação e a mensuração comercial compatível.

Este dashboard não pode usar performance paga para reescrever métricas orgânicas nem apresentar posição patrocinada como recomendação da Guivos.

---

## 5. Áreas analíticas candidatas

Ads / Opportunity Boost Analytics é organizado em **dez áreas analíticas**:

1. Visão Analítica do Anunciante;
2. Campanhas e Objetos Patrocinados;
3. Entrega e Inventário Patrocinado;
4. Eventos e Ações Válidas;
5. Opportunity Boost;
6. Orçamento e Reconciliação Econômica;
7. Outcomes Instrumentados e Resultados Declarados;
8. Público Permitido e Disclosure;
9. Qualidade, Tráfego Inválido e Antifraude;
10. Qualidade do Dado, Freshness, Proveniência e Limitações.

A **Visão Analítica do Anunciante** compõe leituras das famílias governadas e não constitui namespace KPI autônomo.

`Attribution` permanece tema transversal **bloqueado** nesta versão e não cria família KPI própria.

```text
ÁREA DOCUMENTADA
≠ KPI DEFINED
≠ DADO DISPONÍVEL
≠ FATURAMENTO
≠ RESULTADO COMPROVADO
≠ CAUSALIDADE
≠ IMPLEMENTAÇÃO AUTORIZADA
```

---

## 6. Classes funcionais de consumo

As classes são conceituais e não constituem RBAC técnico implementado:

| Classe funcional | Escopo candidato |
|---|---|
| Anunciante — visão própria | campanhas, Boosts, orçamento, entrega, eventos e agregados próprios autorizados |
| Organização / Coletivo anunciante | somente o recorte publicitário legitimamente vinculado ao participante e à oportunidade |
| Guivos Ads — operação | recorte necessário à operação, qualidade, reconciliação e suporte publicitário |
| Guivos — Financeiro/Economia | métricas econômicas autorizadas e auditáveis conforme contrato aplicável |
| Guivos — Intelligence/Data | inputs e outputs necessários à mensuração, antifraude e análise autorizadas |
| Superfície anfitriã | somente leituras necessárias ao seu contexto, segurança e governança quando houver autoridade |
| Service account / Replit | somente payloads necessários à renderização autorizada |

```text
ANUNCIANTE
≠ ACESSO A LISTA DE VISUALIZADORES
≠ ACESSO A RELATO PESSOAL
≠ ACESSO A MOMENTO ATUAL
≠ ACESSO A PRÓXIMO PASSO
≠ ACESSO A MENSAGEM PRIVADA
≠ ACESSO A INFERÊNCIA SENSÍVEL

DADO SOBRE CAMPANHA
≠ DIREITO AUTOMÁTICO A DADO INDIVIDUAL DO PARTICIPANTE
```

---

## 7. Vocabulário de KPI e readiness

Prefixo deste master:

```text
ADS-KPI-<FAMÍLIA>-NNN
```

Famílias iniciais:

- `CAM` — campanhas e objetos patrocinados;
- `DEL` — entrega e inventário patrocinado;
- `EVT` — eventos e ações válidas;
- `BST` — Opportunity Boost;
- `FIN` — orçamento e reconciliação econômica;
- `OUT` — outcomes instrumentados e resultados declarados;
- `AUD` — público permitido, segmentação e disclosure agregado;
- `QF` — qualidade, tráfego inválido e antifraude;
- `DQ` — qualidade do dado, freshness, proveniência e governança.

Estados:

| Status | Significado |
|---|---|
| `proposed` | significado/contrato incompleto; não build-ready |
| `source_pending` | semântica suficiente, mas source/data contract bloqueia readiness |
| `defined` | contrato documental mínimo completo; ainda exige demais gates |
| `approved-equivalent` | autoridade especializada fornece estado equivalente aceito pelo gate |

Nesta versão, **todos os KPIs candidatos permanecem `proposed / NOT_READY`**.

---

## 8. Attribution explicitamente bloqueada

`GEM-007-CROSS-PRODUCT-VALUE-ATTRIBUTION-001` define princípios e estados conceituais, mas não define janela, first-touch, last-touch, multi-touch, pesos, percentual, algoritmo ou regra contábil.

`GEM-010-A2` registra uma baseline candidata de attribution por clique para validação, sem transformar essa hipótese em modelo canônico vigente.

Portanto:

```text
ATTRIBUTION
→ BLOCKED / MODEL NOT DEFINED
→ NO CANONICAL WINDOW
→ NO FIRST-TOUCH RULE
→ NO LAST-TOUCH RULE
→ NO MULTI-TOUCH MODEL
→ NO WEIGHTS
→ NO PERCENTAGE
→ NO ALGORITHM
→ NO ACCOUNTING RULE

ADS-KPI-ATT-*
→ NOT CREATED IN THIS VERSION
```

Estados conceituais como `direct`, `assisted`, `shared`, `unresolved` e `not_attributable` podem ser preservados como vocabulário futuro, mas não autorizam cálculo.

```text
ASSOCIAÇÃO TEMPORAL
≠ ATTRIBUTION VALIDADA

ATTRIBUTION
≠ CAUSALIDADE

CLIQUES / IMPRESSÕES / EXPOSIÇÃO
≠ CRÉDITO CAUSAL
```

---

## 9. Família CAM — Campanhas e objetos patrocinados

Esta família organiza apenas objetos publicitários legitimamente reconhecidos pelo contrato futuro.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-CAM-001 | Campanhas válidas | campanhas em estados semanticamente válidos no recorte autorizado | campanhas | proposed | campaign lifecycle + source |
| ADS-KPI-CAM-002 | Campanhas ativas | campanhas em estado ativo válido na janela | campanhas | proposed | active-state contract |
| ADS-KPI-CAM-003 | Campanhas por estado | distribuição pelas classes governadas do lifecycle aplicável | distribuição | proposed | lifecycle taxonomy |
| ADS-KPI-CAM-004 | Objetos patrocinados válidos | oportunidades, ofertas, conteúdos ou outros objetos aprovados para relação publicitária | objetos | proposed | object eligibility + source |
| ADS-KPI-CAM-005 | Eventos de lifecycle no período | aprovação, programação, pausa, limitação, suspensão, conclusão, cancelamento ou reconciliação conforme autoridade aplicável | eventos/período | proposed | event semantics + temporal contract |

```text
CAMPANHA CADASTRADA
≠ CAMPANHA APROVADA
≠ CAMPANHA ATIVA

OBJETO APROVADO NO PRODUTO ANFITRIÃO
≠ CAMPANHA ADS AUTOMATICAMENTE APROVADA

PAGAMENTO
≠ ADMISSÃO
≠ VERIFICAÇÃO
≠ MODERAÇÃO
```

---

## 10. Família DEL — Entrega e inventário patrocinado

Esta família separa entrega técnica, validade, visibilidade e frequência.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-DEL-001 | Impressões servidas | unidades tecnicamente entregues segundo contrato futuro | impressões | proposed | instrumentation + source |
| ADS-KPI-DEL-002 | Impressões válidas | entregas após remoção de tráfego/eventos inválidos | impressões | proposed | validity contract + antifraud |
| ADS-KPI-DEL-003 | Impressões visíveis | unidades que atendem critério de visibilidade aplicável | impressões | proposed | viewability definition + source |
| ADS-KPI-DEL-004 | Alcance estimado agregado | pessoas/dispositivos únicos estimados sem exposição individual | estimativa agregada | proposed | identity resolution + privacy + methodology |
| ADS-KPI-DEL-005 | Entrega por superfície anfitriã | distribuição da entrega patrocinada entre superfícies autorizadas | distribuição | proposed | surface taxonomy + serving source |
| ADS-KPI-DEL-006 | Unidades patrocinadas entregues | quantidade de unidades de inventário patrocinado legitimamente servidas | unidades | proposed | inventory contract + source |
| ADS-KPI-DEL-007 | Frequência média | média de exposições válidas no recorte autorizado, preservando que população/unidade única, janela e metodologia ainda exigem contrato próprio | média | proposed | frequency definition + unique-unit methodology + window + source |

```text
IMPRESSÃO SERVIDA
≠ IMPRESSÃO VÁLIDA
≠ IMPRESSÃO VISÍVEL
≠ ATENÇÃO
≠ INTERESSE
≠ RESULTADO

ALCANCE ESTIMADO
≠ PESSOAS IDENTIFICADAS PARA O ANUNCIANTE

FREQUÊNCIA MÉDIA
≠ LIMITE DE FREQUÊNCIA DEFINIDO
≠ GARANTIA DE ALCANCE
```

`UXA-038` exige que o relatório do anunciante preserve `frequência média` e que repetição excessiva seja controlada por limite de frequência por campanha e superfície. Este master preserva a necessidade analítica, mas **não inventa** população única, fórmula, janela, threshold ou source: esses elementos permanecem gates para definição futura do KPI.

A densidade candidata citada em `GEM-007-A1` não é promovida por este master a threshold operacional ou KPI aprovado.

---

## 11. Família EVT — Eventos e ações válidas

Os eventos abaixo preservam a distinção entre exposição, interação, declaração e fluxo posterior.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-EVT-001 | Cliques válidos | interações não fraudulentas que abrem destino legítimo | cliques | proposed | click validity + source |
| ADS-KPI-EVT-002 | Visualizações de detalhe | aberturas válidas do detalhe do objeto promovido | eventos | proposed | event contract + source |
| ADS-KPI-EVT-003 | Salvamentos válidos | salvamentos por ação afirmativa quando legitimamente instrumentados | eventos | proposed | event semantics + source |
| ADS-KPI-EVT-004 | Interesses declarados | declarações explícitas de interesse no fluxo autorizado | eventos | proposed | declared-event semantics + source |
| ADS-KPI-EVT-005 | Inícios de inscrição | início legítimo de fluxo de inscrição quando instrumentado | eventos | proposed | registration-start contract + source |
| ADS-KPI-EVT-006 | Contratações instrumentadas | eventos de contratação somente quando legitimamente instrumentados e confirmados | eventos | proposed | transaction authority + source |
| ADS-KPI-EVT-007 | Distribuição de ações válidas | composição agregada dos tipos de ação válida permitidos | distribuição | proposed | event taxonomy + denominator |

```text
CLIQUE
≠ INTENÇÃO

DETALHE VISUALIZADO
≠ INTERESSE

SALVAMENTO
≠ INSCRIÇÃO

INTERESSE DECLARADO
≠ CONTRATAÇÃO

INÍCIO DE INSCRIÇÃO
≠ PARTICIPAÇÃO
≠ RESULTADO

EVENTO VÁLIDO
≠ EVENTO FATURÁVEL SEM CONTRATO
```

---

## 12. Família BST — Opportunity Boost

Opportunity Boost é mecanismo especializado de Ads e não representa toda a identidade do produto.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-BST-001 | Boosts válidos | campanhas Opportunity Boost em estados semanticamente válidos | boosts | proposed | GEM-007-A1 lifecycle + source |
| ADS-KPI-BST-002 | Boosts ativos | Boosts em estado ativo válido | boosts | proposed | active-state + eligibility |
| ADS-KPI-BST-003 | Boosts pausados/limitados/suspensos | Boosts interrompidos pelos estados governados correspondentes | boosts | proposed | lifecycle + reason taxonomy |
| ADS-KPI-BST-004 | Boosts concluídos e reconciliados | Boosts que atingiram encerramento e reconciliação legitimamente registrados | boosts | proposed | reconciliation contract |
| ADS-KPI-BST-005 | Boosts por motivo de interrupção | distribuição agregada dos motivos autorizados de pausa/limitação/suspensão | distribuição | proposed | reason taxonomy + disclosure |

```text
BOOST
≠ ORGÂNICO
≠ RECOMENDAÇÃO
≠ GARANTIA DE ALCANCE
≠ GARANTIA DE INSCRIÇÃO
≠ GARANTIA DE RESULTADO

ELEGIBILIDADE PARA BOOST
≠ GARANTIA DE INVENTÁRIO
≠ AUTORIZAÇÃO AUTOMÁTICA DE COBRANÇA
```

Entitlements de Organização permanecem subordinados à reconciliação específica prevista em `GEM-007-A1`.

---

## 13. Família FIN — Orçamento e reconciliação econômica

Esta família não transforma parâmetros candidatos de `GEM-010-A2` em tabela pública ou preço vigente.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-FIN-001 | Orçamento autorizado | valor legitimamente autorizado para a campanha segundo contrato aplicável | moeda | proposed | economic contract + source |
| ADS-KPI-FIN-002 | Orçamento consumido reconciliável | valor associado a entrega/eventos elegíveis antes da reconciliação final, conforme regra aprovada futura | moeda | proposed | billing basis + GEM-009 + source |
| ADS-KPI-FIN-003 | Saldo remanescente | diferença legitimamente calculada entre orçamento autorizado e consumo reconciliável/reconciliado | moeda | proposed | formula + reconciliation source |
| ADS-KPI-FIN-004 | Créditos/compensações registrados | créditos, devoluções ou compensações com fonte e finalidade preservadas | moeda/eventos | proposed | credit/refund taxonomy + accounting |
| ADS-KPI-FIN-005 | Campanhas com reconciliação pendente | campanhas encerradas que ainda não possuem reconciliação econômica concluída | campanhas | proposed | reconciliation lifecycle + source |

```text
ORÇAMENTO AUTORIZADO
≠ RECEITA

ORÇAMENTO CONSUMIDO
≠ RECEITA RECONHECIDA

EVENTO VÁLIDO
≠ EVENTO FATURÁVEL

EVENTO FATURÁVEL
≠ RECEITA CONTÁBIL AUTOMÁTICA

CRÉDITO
≠ PONTOS GUIVOS
```

CPM, CPC, faixas de orçamento, taxa de serviço, tributos e margens permanecem sujeitos às autoridades econômicas e seus gates. Este master não os congela.

---

## 14. Família OUT — Outcomes instrumentados e resultados declarados

Esta família preserva outcome observado como objeto distinto de attribution e impacto e mantém **resultado declarado pelo anunciante** como evidência/autorreporte explicitamente separado de evento instrumentado.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-OUT-001 | Outcomes finais instrumentados | eventos finais legitimamente instrumentados pelo produto responsável | outcomes | proposed | outcome semantics + source authority |
| ADS-KPI-OUT-002 | Outcomes por tipo autorizado | distribuição agregada segundo taxonomia de outcome legitimamente definida | distribuição | proposed | outcome taxonomy + disclosure |
| ADS-KPI-OUT-003 | Outcomes confirmados | outcomes cuja confirmação atende ao contrato de evidência aplicável | outcomes | proposed | confirmation + evidence |
| ADS-KPI-OUT-004 | Outcomes não resolvidos | eventos finais cuja relação, confirmação ou responsabilidade permanece não resolvida | outcomes | proposed | unresolved-state contract |
| ADS-KPI-OUT-005 | Resultados declarados pelo anunciante | resultados fornecidos pelo anunciante, preservados como autorrelato com origem explícita e sem reclassificação como evento instrumentado | declarações | proposed | declared-evidence semantics + provenance + review/disclosure |

```text
OUTCOME OBSERVADO
≠ OUTCOME ATRIBUÍDO A ADS
≠ CAUSALIDADE
≠ IMPACTO

RESULTADO DECLARADO PELO ANUNCIANTE
≠ OUTCOME INSTRUMENTADO
≠ RESULTADO CONFIRMADO PELA GUIVOS
≠ ATTRIBUTION
≠ CAUSALIDADE
≠ IMPACTO

CONTRATAÇÃO
≠ SATISFAÇÃO
≠ ENTREGA
≠ IMPACTO
```

`UXA-038` exige que o relatório preserve uma seção de **Resultado declarado**, identificada explicitamente como autorrelato e distinguível de evento instrumentado. O autorrelato pode ser armazenado e exibido quando legitimamente autorizado, mas não ganha, por existir, status de outcome instrumentado, confirmação, attribution ou causalidade.

Nenhum outcome pode receber crédito causal de Ads sem modelo de attribution futuramente adjudicado.

---

## 15. Família AUD — Público permitido, segmentação e disclosure

Esta família serve à auditoria do uso de critérios autorizados e à leitura agregada; não cria listas individuais para anunciantes.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-AUD-001 | Entrega por critério permitido | distribuição agregada da entrega segundo critérios publicitários autorizados | distribuição | proposed | allowed-segmentation taxonomy + privacy |
| ADS-KPI-AUD-002 | Entrega geográfica agregada | distribuição territorial somente no nível permitido e protegido | distribuição | proposed | geography + threshold + reidentification controls |
| ADS-KPI-AUD-003 | Entrega por idioma/modalidade/categoria | agregados segundo dimensões objetivas permitidas | distribuição | proposed | taxonomy + minimum population |
| ADS-KPI-AUD-004 | Segmentos suprimidos por política | quantidade de recortes não expostos por finalidade, sensibilidade ou threshold | quantidade | proposed | disclosure policy + audit source |

São proibidos como matéria-prima publicitária nesta baseline:

- relato pessoal protegido;
- compreensão inicial;
- Momento Atual;
- avanço ou Próximo Passo individual;
- inferências sensíveis ou vulnerabilidade;
- mensagens privadas;
- histórico sensível de localização;
- pontuações opacas;
- listas individuais entregues ao anunciante.

```text
SEGMENTO PERMITIDO
≠ PERFIL INDIVIDUAL

AGREGADO
≠ AUTOMATICAMENTE SEGURO

PROCESSAMENTO PARA ENTREGA
≠ DISCLOSURE AO ANUNCIANTE
```

---

## 16. Família QF — Qualidade, tráfego inválido e antifraude

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-QF-001 | Eventos invalidados | eventos removidos por regra legítima de validade/antifraude | eventos | proposed | invalid-event taxonomy + source |
| ADS-KPI-QF-002 | Cliques invalidados | cliques classificados como não válidos segundo contrato futuro | cliques | proposed | fraud/validity rule + auditability |
| ADS-KPI-QF-003 | Impressões invalidadas | impressões que não atendem ao contrato de validade aplicável | impressões | proposed | validity/viewability contract |
| ADS-KPI-QF-004 | Casos antifraude em revisão | casos operacionais abertos sob processo autorizado de investigação | casos | proposed | antifraud lifecycle + access |
| ADS-KPI-QF-005 | Campanhas afetadas por qualidade/política | campanhas pausadas, limitadas ou suspensas por razão governada | campanhas | proposed | reason taxonomy + source |
| ADS-KPI-QF-006 | Entrega após condição inválida detectada | eventos potencialmente ocorridos após encerramento, indisponibilidade ou limite, sujeitos a reconciliação | eventos | proposed | timing + source integrity + reconciliation |

```text
TRÁFEGO INVÁLIDO
≠ PARTICIPANTE INVÁLIDO

SINAL DE FRAUDE
≠ CULPA CONFIRMADA

CASO EM REVISÃO
≠ CONCLUSÃO
```

Antifraude pode usar inteligência operacional autorizada, mas não cria autorização para explorar contexto pessoal protegido.

---

## 17. Família DQ — Qualidade do dado, freshness, proveniência e governança

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| ADS-KPI-DQ-001 | Freshness compliance | contratos/datasets dentro da freshness governada / monitorados | % | proposed | freshness contract |
| ADS-KPI-DQ-002 | Indicadores indisponíveis | KPIs esperados sem dado utilizável | quantidade | proposed | registry + availability rules |
| ADS-KPI-DQ-003 | Completude de proveniência | leituras com proveniência suficiente / leituras avaliadas | % | proposed | provenance contract |
| ADS-KPI-DQ-004 | Conflitos de fonte não resolvidos | leituras com divergência material de origem/transformação | leituras | proposed | source conflict + authority |
| ADS-KPI-DQ-005 | Supressões de disclosure | leituras protegidas ou indisponíveis por política/finalidade | quantidade | proposed | disclosure policy |
| ADS-KPI-DQ-006 | Reconciliações de dado pendentes | campanhas/eventos cuja consistência ainda exige reconciliação | itens | proposed | reconciliation lifecycle |

```text
0
≠ NO_DATA

DADO MAIS RECENTE
≠ DADO AUTOMATICAMENTE MAIS VERDADEIRO

AUSÊNCIA DE EVIDÊNCIA
≠ RESULTADO NEGATIVO
```

---

## 18. Eventos, conversão e faturabilidade

A arquitetura deve preservar quatro conceitos separados:

```text
EVENTO BRUTO
→ registro técnico ainda não qualificado

EVENTO VÁLIDO
→ atende ao contrato de validade aplicável

EVENTO FATURÁVEL
→ atende adicionalmente à base econômica aprovada

OUTCOME
→ evento/estado final definido pelo produto responsável
```

Nenhuma equivalência é automática.

```text
EVENTO BRUTO
≠ EVENTO VÁLIDO

EVENTO VÁLIDO
≠ EVENTO FATURÁVEL

EVENTO FATURÁVEL
≠ OUTCOME

OUTCOME
≠ IMPACTO
```

O termo `conversão` somente poderá ser usado quando o evento final, a instrumentação, a janela aplicável e os claims permitidos estiverem explicitamente definidos. Enquanto attribution continuar bloqueada, `conversão atribuível` não pode ser promovida por conveniência a KPI canônico deste master.

---

## 19. Pricing, budget e billing — limites

`GEM-010-A2` contém faixas e bases **candidatas** de validação.

Este master preserva, mas não operacionaliza:

- orçamento mínimo candidato;
- duração candidata;
- CPM candidato;
- CPC candidato;
- serviço gerenciado com taxa `TBD`;
- limites/avisos candidatos;
- créditos futuros;
- regras futuras de devolução/compensação.

```text
CANDIDATE CPM / CPC
≠ APPROVED PRICE

CANDIDATE BUDGET RANGE
≠ PRODUCT OFFER

BUDGET ANALYTICS
≠ BILLING LEDGER

DASHBOARD
≠ ACCOUNTING AUTHORITY
```

Métricas econômicas futuras deverão compor com `GEM-009-MEASUREMENT-CONTRACT-001` na versão e no status aplicáveis, além das validações jurídica, fiscal, contábil, financeira, privacidade e segurança pertinentes.

---

## 20. Filtros candidatos

Filtros somente restringem o recorte já autorizado:

- período e comparação de período;
- campanha;
- objeto patrocinado;
- estado de campanha;
- Opportunity Boost;
- estado de Boost;
- superfície anfitriã;
- tipo de inventário patrocinado;
- tipo de evento válido;
- região/idioma/modalidade/categoria quando permitidos;
- estado de reconciliação;
- status de validade/qualidade;
- source/freshness;
- outcome autorizado;
- natureza de evidência (`instrumentado` / `declarado`) quando aplicável.

```text
FILTRO
→ SUBCONJUNTO DO ACCESS SCOPE
→ NUNCA AMPLIA DISCLOSURE
→ NUNCA CONVERTE SEGMENTAÇÃO EM PERFIL INDIVIDUAL
```

Não haverá filtro por contexto pessoal protegido, vulnerabilidade, Momento Atual, Próximo Passo individual ou inferência sensível.

---

## 21. Drill-down

Estrutura candidata:

```text
N0 — ANUNCIANTE / ESCOPO ADS AUTORIZADO
→ N1 — FAMÍLIA ANALÍTICA
→ N2 — CAMPANHA / BOOST / OBJETO / PERÍODO / SUPERFÍCIE / SEGMENTO AUTORIZADO
→ N3 — EVENTO AGREGADO / ESTADO / EVIDÊNCIA / RECONCILIAÇÃO AUTORIZADA
```

O drill-down não cria direito de abrir Pessoa individual.

```text
AGREGADO DE CAMPANHA
≠ LISTA DE PESSOAS

CLIQUE / INTERESSE / INSCRIÇÃO AGREGADA
≠ LEAD INDIVIDUAL VENDÁVEL

RELAÇÃO PUBLICITÁRIA
≠ ACESSO À JOURNEY PRIVADA
```

Exceções de identificação necessárias a transações ou fluxos legítimos pertencem ao contrato do produto responsável e não são concedidas por este dashboard.

---

## 22. Estados obrigatórios de visualização

```text
LOADING
NO_DATA
INSUFFICIENT_DATA
INSUFFICIENT_EVIDENCE
SUPPRESSED_BY_POLICY
SOURCE_DELAYED
UNDER_REVIEW
RECONCILIATION_PENDING
NOT_ENTITLED
ERROR
AVAILABLE
```

`0` não substitui `NO_DATA`.

`INSUFFICIENT_EVIDENCE` não deve ser renderizado como baixa performance confirmada.

`UNDER_REVIEW` não deve aparecer como fraude confirmada.

`RECONCILIATION_PENDING` não deve aparecer como receita final ou saldo definitivamente devido.

`NOT_ENTITLED` descreve capacidade comercial quando aplicável e não cria autorização de cobrança nem retira direitos superiores de privacidade, contestação ou correção.

---

## 23. Contratos lógicos esperados

Sem definir schema físico, a superfície poderá futuramente consumir contratos equivalentes a:

- Advertiser Scope Projection;
- Campaign / Sponsored Object Projection;
- Sponsored Delivery Aggregate;
- Valid Event Aggregate;
- Opportunity Boost Projection;
- Budget / Reconciliation Projection;
- Authorized Outcome Projection;
- Advertiser Declared Result Projection;
- Allowed Audience Aggregate;
- Invalid Traffic / Antifraud Status;
- Data Quality / Freshness / Provenance Status.

Não existe `Person Advertising Profile` universal autorizado por este master.

Cada payload deverá carregar, quando aplicável:

- identificador do KPI/output;
- período e temporalidade;
- advertiser/campaign/object scope;
- valor/unidade quando existir;
- source/version;
- natureza do evento ou evidência;
- estado de validade;
- estado econômico/reconciliação quando aplicável;
- proveniência;
- freshness;
- sensibilidade/access class;
- aggregation/disclosure state;
- confidence/uncertainty quando material;
- claims permitidos e limitações;
- status de attribution quando aplicável, preservando `unresolved`/`not_attributable` sem inventar modelo.

Para resultado declarado pelo anunciante, o payload deverá preservar explicitamente a origem `advertiser_declared` ou equivalente governado, sem convertê-la em instrumentação da Guivos, confirmação independente ou attribution.

---

## 24. Privacidade, segmentação e disclosure

O dashboard opera sob finalidade, minimização, necessidade e proteção contra reidentificação.

```text
AUTORIDADE PARA ENTREGAR ANÚNCIO
≠ AUTORIDADE PARA REVELAR IDENTIDADE

AUTORIDADE PARA MEDIR AGREGADO
≠ AUTORIDADE PARA ENTREGAR LISTA INDIVIDUAL

AUTORIDADE PARA PROCESSAR ANTIFRAUDE
≠ AUTORIDADE PARA EXPLORAR CONTEXTO PESSOAL

SEGMENTAÇÃO PERMITIDA
≠ VIGILÂNCIA
```

A Pessoa não será reduzida a conversão, lead, score de propensão ou vulnerabilidade por conveniência analítica.

Qualquer futura personalização publicitária deverá possuir autoridade própria, finalidade legítima, categorias permitidas, categorias proibidas, explicabilidade proporcional, minimização, controles e consentimentos/base legal quando aplicáveis.

---

## 25. Relação com Guivos Intelligence

Guivos Intelligence poderá apoiar, quando legitimamente autorizado:

- interpretação de intenção comercial declarada;
- classificação/roteamento de leads comerciais do próprio anunciante;
- identificação de contexto comercial potencial;
- mensuração agregada;
- antifraude;
- enriquecimento operacional autorizado;
- análise de demanda;
- identificação de oportunidades futuras de produto Ads.

Mas:

```text
INTELLIGENCE PARA ADS
≠ PERSON INTELLIGENCE PARA O ANUNCIANTE

INFERÊNCIA COMERCIAL
≠ FATO

SINAL ANTIFRAUDE
≠ CULPA

RECOMENDAÇÃO DE OPERAÇÃO ADS
≠ RECOMENDAÇÃO PESSOAL AO PARTICIPANTE
```

Outputs de Intelligence usados em análise devem preservar natureza, estado epistemológico/derivacional, confiança, incerteza, proveniência e limitações quando materiais.

---

## 26. Orientação futura para Replit

Quando houver autorização formal de build, a ferramenta deverá:

1. não inventar KPI, fórmula, preço, CPM, CPC, budget threshold, entitlement, source, schema ou permissão;
2. usar `ADS-KPI-*` como IDs estáveis e não como labels visuais;
3. bloquear KPIs `proposed` e `source_pending` para consumo canônico com dado real;
4. preservar Ads Analytics ≠ Ads Home ≠ campaign manager ≠ checkout ≠ billing ledger;
5. separar orgânico de patrocinado em todos os contratos e visualizações;
6. não transformar pagamento em relevância, recomendação, confiança ou impacto;
7. distinguir impressão servida, válida e visível;
8. preservar frequência média como leitura candidata sem inventar fórmula, unidade única, janela ou limite de frequência;
9. distinguir clique, interesse, inscrição, contratação, outcome e impacto;
10. distinguir resultado declarado/autorreporte de outcome instrumentado, confirmação, attribution, causalidade e impacto;
11. distinguir evento bruto, válido, faturável e outcome;
12. não criar modelo de attribution, janela, first-touch, last-touch, multi-touch, pesos, percentual ou algoritmo;
13. preservar `ATTRIBUTION = BLOCKED` enquanto a autoridade não for adjudicada;
14. não congelar os valores candidatos de `GEM-010-A2` como tabela de preço vigente;
15. preservar orçamento ≠ receita e evento faturável ≠ receita contábil automática;
16. não expor listas individuais de visualizadores, clickers ou participantes ao anunciante por conveniência;
17. não usar contexto pessoal protegido ou inferência sensível para segmentação;
18. aplicar thresholds/supressões quando definidos pela política futura;
19. validar scope e disclosure no serving/backend, não apenas no cliente;
20. separar mock adapters de real adapters;
21. preservar estados `NO_DATA`, `INSUFFICIENT_DATA`, `INSUFFICIENT_EVIDENCE`, `SUPPRESSED_BY_POLICY`, `UNDER_REVIEW`, `RECONCILIATION_PENDING`, `NOT_ENTITLED` e `SOURCE_DELAYED`;
22. preservar versão, temporalidade, freshness, proveniência e validade;
23. não transformar sinal antifraude em conclusão de culpa;
24. manter superfície anfitriã como autoridade de contexto, segurança, acessibilidade e densidade;
25. não implementar campaign creation, media buying ou checkout a partir deste master;
26. não usar este master para redefinir ou materializar a Home Pública Ads;
27. registrar a versão deste master usada na build.

---

## 27. Critérios de aceite para futuro handoff

Antes de qualquer release `READY FOR BUILD`:

```text
[ ] KPI selecionado = defined OU approved-equivalent
[ ] pergunta/finalidade fechadas
[ ] população/objeto definidos
[ ] fórmula e componentes definidos
[ ] janela temporal/granularidade definidas
[ ] source/data contract definido
[ ] natureza de evento/evidência definida
[ ] validade/faturabilidade separadas quando aplicáveis
[ ] resultado declarado distinguido de evento instrumentado quando aplicável
[ ] access/disclosure definido
[ ] agregação/supressão definidas
[ ] filtros/drill-down definidos
[ ] null/zero/no-data definidos
[ ] freshness/quality checks definidos
[ ] proveniência definida
[ ] reconciliation semantics definidas quando aplicáveis
[ ] claims suportados/proibidos definidos
[ ] atribuição permanece bloqueada OU possui ato próprio posterior válido
[ ] pricing/billing possui autoridade própria vigente quando aplicável
[ ] contratos de domínio aplicáveis satisfeitos
[ ] validações econômica/financeira/contábil/jurídica/privacidade/segurança satisfeitas quando aplicáveis
[ ] Design/build authorization foi emitida
```

---

## 28. Itens explicitamente bloqueados nesta versão

```text
REAL DATA
→ NOT AUTHORIZED

BACKEND / API FÍSICA
→ NOT DEFINED HERE

TECHNICAL RBAC
→ NOT IMPLEMENTED

ADS HOME / CAMPAIGN MANAGER / BUYING CONSOLE
→ NOT DEFINED BY THIS DOCUMENT

CHECKOUT / BILLING / ACCOUNTING LEDGER
→ NOT AUTHORIZED

FINAL VISUAL DESIGN
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

FINAL PRICING / CPM / CPC / SERVICE FEE
→ NOT APPROVED BY THIS MASTER

LIVE INVENTORY / BIDDING / AUCTION
→ NOT DEFINED

ATTRIBUTION MODEL
→ BLOCKED / NOT DEFINED

ADS-KPI-ATT-*
→ NOT CREATED

CAUSAL IMPACT CLAIMS
→ NOT AUTHORIZED

ORGANIC RANKING INFLUENCE BY PAYMENT
→ PROHIBITED

PERSON NEXT STEP / PERSONAL RECOMMENDATION INFLUENCE BY PAYMENT
→ PROHIBITED

SENSITIVE TARGETING / VULNERABILITY EXPLOITATION
→ PROHIBITED

ADVERTISER ACCESS TO PRIVATE PERSON JOURNEY
→ NOT AUTHORIZED

INDIVIDUAL VIEWER / CLICKER LIST BY CONVENIENCE
→ NOT AUTHORIZED
```

---

## 29. Estado final desta versão

```text
GKR-INTELLIGENCE-DASHBOARD-ADS-001
→ DRAFT v0.1.0
→ ANNEX F CANDIDATE MASTER
→ PRE-IMPLEMENTATION

ANALYTICAL AREAS
→ 10

KPI FAMILIES
→ CAM / DEL / EVT / BST / FIN / OUT / AUD / QF / DQ

CURRENT KPI CANDIDATES
→ 50
→ ALL proposed / NOT_READY

ATTRIBUTION
→ BLOCKED / MODEL NOT DEFINED
→ NO KPI FAMILY MATERIALIZED

PRICING / BILLING PARAMETERS
→ CANDIDATE AUTHORITY PRESERVED
→ NOT PROMOTED TO OPERATIONAL TRUTH

KPI IMPLEMENTATION READINESS
→ NONE CLAIMED BY INFERENCE
→ ALL CURRENT KPIs = proposed
→ ALL = NOT_READY

ADVERTISER AUTHORITY
→ OWN CAMPAIGNS / BOOSTS / BUDGET / AUTHORIZED AGGREGATES
→ NO DEFAULT ACCESS TO PRIVATE PERSON DATA

HOME ADS AUTHORITY
→ GKR-UX-HOME-ADS-MASTER-001 PRESERVED
→ HOME ADS ≠ ADS ANALYTICS

ORGANIC RELEVANCE
→ PRESERVED OUTSIDE PAYMENT

REAL DATA / BACKEND / API / TECHNICAL RBAC / PRODUCTION
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED
```

A promoção deste draft para master materializado exige reconciliação explícita do registry do master global, validação semântica/mecânica e review governado da PR correspondente.
