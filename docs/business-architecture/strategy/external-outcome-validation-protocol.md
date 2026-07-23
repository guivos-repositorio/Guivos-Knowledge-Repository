---
id: BA-STR-002-EOVP-001
title: External Outcome Validation Protocol
status: active
version: 0.3.0
owner: Guivos Business Architecture
last_updated: 2026-07-23
parent: BA-STR-002
depends_on:
  - BA-STR-002-COR-001
  - GKR-GOV-OUT-001
  - RP-001-PROTOCOL
related:
  - RP-001-EVIDENCE
  - RP-001-REC
  - BA-STR-002-EOVB-001
  - BA-STR-002-EOVB-002
normative: false
execution_status: in-progress
---

# BA-STR-002-EOVP-001 — External Outcome Validation Protocol

## 1. Autoridade e finalidade

Este protocolo define como os 18 candidatos do primeiro Candidate Outcome Register serão confrontados com conhecimento externo antes da Candidate Outcome Evaluation Matrix — COEM.

Ele transforma as dúvidas do COR em um plano de investigação repetível, rastreável e neutro. O protocolo não executa a pesquisa, não valida candidatos por declaração e não substitui a decisão arquitetural da Business Architecture.

## 2. Estado formal

```text
Protocol: governed execution in progress
Scope: 18 candidates and 6 overlap clusters
Candidate state changes: 6 to Under Validation
External evidence registered: 18
External validation: in progress — batches 01 and 02 completed
COEM: not started
Approved Outcomes: 0
Canonical EO/BO codes: 0
Operational authorization: no
```

## 3. Escopo

### Incluído

- oito Candidate Ecosystem Outcomes `ECO-CAND-001` a `ECO-CAND-008`;
- dez Candidate Business Outcomes `BUS-CAND-001` a `BUS-CAND-010`;
- seis clusters de possível sobreposição registrados no COR;
- busca de omissões materiais relacionadas à pergunta arquitetural do `BA-STR-002`;
- evidência favorável, ampliadora, contraditória ou insuficiente;
- avaliação da aplicabilidade e dos limites de generalização das fontes.

### Excluído

- aprovação, rejeição, fusão ou promoção de candidatos;
- aplicação da COEM ou estabilização do AQS-O01;
- criação de códigos `EO-###` ou `BO-###`;
- definição de capacidades, produtos, processos, KPIs, metas ou tecnologias;
- pesquisa filosófica sem impacto direto na decisão arquitetural;
- absorção do Guivos Market Validation System ou de sua execução;
- retomada de `BA-CAP-001`, Product Engineering ou W0-01.

## 4. Perguntas de validação

### Pergunta principal

> O conhecimento externo qualificado sustenta que cada candidato representa um estado permanente, distinto e decisoriamente útil para uma organização orientada à geração sustentável de valor em um ecossistema complexo?

### Perguntas por candidato

1. Existe conceito externo equivalente ou suficientemente próximo?
2. O conceito é tratado como resultado, condição habilitadora, capacidade, princípio, guardrail, propriedade emergente ou etapa?
3. Sua relevância permanece quando produtos, tecnologias e estruturas atuais são substituídos?
4. Há aplicação coerente em diferentes contextos, participantes ou disciplinas?
5. A condição pode ser observada sem ser reduzida a uma única métrica?
6. Sua degradação produz implicação estratégica própria?
7. Há evidência de dependência, redundância ou composição com outro candidato?
8. Quais limitações, controvérsias e contraexemplos restringem a formulação?

### Perguntas de completude

1. Há condição permanente material ausente do COR?
2. Algum conceito recorrente não pode ser representado por nenhum candidato existente?
3. A separação entre Ecosystem Outcome e Business Outcome é sustentada pelas referências?
4. Algum candidato depende de uma camada conceitual não autorizada para fazer sentido?

## 5. Unidades de análise

| Unidade | Finalidade | Resultado esperado da pesquisa |
|---|---|---|
| candidato individual | testar permanência, natureza, independência e utilidade | registro de evidências e síntese provisória |
| cluster de sobreposição | testar fronteiras, composição e redundância | hipótese de manter separado, reformular ou avaliar fusão na COEM |
| conjunto do COR | testar cobertura e omissões | lista rastreável de lacunas ou confirmação de saturação provisória |
| fonte | avaliar contribuição e limitações | registro qualificado no Evidence Registry |

## 6. Governança da pesquisa

| Responsabilidade | Autoridade |
|---|---|
| formular perguntas e limites | Guivos Business Architecture |
| selecionar, avaliar e registrar fontes | Guivos Research |
| preservar neutralidade e rastreabilidade | Guivos Research e GKR |
| interpretar implicações arquiteturais | Guivos Business Architecture |
| decidir abertura da COEM | aprovação separada |
| aprovar ou promover Outcomes | decisão futura após COEM |

Research produz evidências e recomendações. Business Architecture decide como essas evidências afetam os candidatos. Nenhuma fonte externa possui autoridade automática sobre a Canon da Guivos.

## 7. Critérios de fonte

Toda fonte deverá atender ao `RP-001-PROTOCOL` e ser avaliada por relevância, autoridade, rigor, generalidade, permanência, aplicabilidade e transparência.

### Papéis de evidência elegíveis

| Papel | Uso principal |
|---|---|
| pesquisa primária ou obra teórica reconhecida | compreender mecanismo, definição e limites |
| revisão sistemática, meta-análise ou síntese qualificada | identificar convergência e controvérsia |
| padrão, framework ou referência institucional | testar uso consolidado e implicações decisórias |
| estudo comparativo ou caso longitudinal | examinar aplicabilidade e limites contextuais |
| evidência empírica direta já governada por outra trilha | testar aderência ao contexto da Guivos sem absorver a trilha de origem |

Opinião isolada, tendência temporária, material promocional, implementação tecnológica e caso sem possibilidade de comparação não sustentam validação por si mesmos.

## 8. Suficiência e independência da evidência

Uma síntese por candidato somente poderá ser encerrada quando:

- houver pelo menos duas linhas de evidência independentes e qualificadas;
- ao menos uma busca explícita por contradição, limite ou contraexemplo tiver sido registrada;
- a relação entre o conceito externo e a formulação do candidato estiver descrita, não apenas citada;
- divergências relevantes entre fontes estiverem preservadas;
- o nível `E0` a `E4` do `RP-001-PROTOCOL` estiver justificado;
- novas fontes qualificadas deixarem de alterar materialmente a interpretação ou a ausência de saturação estiver declarada.

Quantidade de fontes não substitui qualidade, independência ou relevância. Evidências originadas do mesmo autor, instituição, conjunto de dados ou referencial não contam como linhas independentes apenas por estarem em publicações diferentes.

## 9. Direção da evidência

Cada evidência deverá receber uma das classificações abaixo:

| Direção | Significado |
|---|---|
| Confirma | sustenta a natureza e a formulação central do candidato |
| Amplia | sustenta o núcleo, mas exige dimensão, limite ou participante adicional |
| Contradiz | apresenta argumento ou resultado incompatível com o candidato |
| Reclassifica | indica que o conceito é capacidade, princípio, guardrail, propriedade ou etapa, e não Outcome |
| Relaciona | esclarece dependência ou fronteira sem confirmar o candidato isoladamente |
| Ausência | a busca qualificada não encontrou evidência material aplicável |

Ausência de evidência não equivale automaticamente a evidência de ausência. Contradições não podem ser descartadas por conflito com hipóteses internas.

## 10. Registro mínimo de evidência

Cada registro da execução deverá conter:

| Campo | Regra |
|---|---|
| Evidence ID | identificador estável do RP-001 Evidence Registry |
| candidato ou cluster | um ou mais IDs provisórios do COR |
| referência | identificação verificável da fonte |
| disciplina e papel | campo de origem e papel de evidência |
| conceito ou alegação | conteúdo extraído sem extrapolação |
| direção | classificação da seção 9 |
| critérios de qualidade | avaliação explícita dos sete critérios do RP-001 |
| nível de evidência | `E0` a `E4`, com justificativa |
| aplicabilidade | implicação possível para o BA-STR-002 |
| limitações | escopo, controvérsias e restrições de generalização |
| independência | relação conhecida com outras fontes |
| revisão | responsável e data da revisão |

O registro oficial permanece no `RP-001-EVIDENCE`. O relatório de validação deverá referenciar os IDs dessas evidências, sem criar uma base paralela desconectada.

## 11. Matriz de cobertura dos candidatos

| Candidato | Foco específico da validação |
|---|---|
| ECO-CAND-001 | compreensão como Outcome ou condição de agência |
| ECO-CAND-002 | unidade entre acesso, legitimidade, compreensão e relevância |
| ECO-CAND-003 | observabilidade da agência sem conversão em adesão |
| ECO-CAND-004 | experiência de valor como estado ou evento intermediário |
| ECO-CAND-005 | continuidade como Outcome próprio ou agregação da jornada |
| ECO-CAND-006 | conexão relevante, reciprocidade e papel da confiança |
| ECO-CAND-007 | inclusão e dignidade como estado ou política de acesso |
| ECO-CAND-008 | proteção e confiança como Outcome ou guardrails obrigatórios |
| BUS-CAND-001 | aderência ao propósito como Outcome ou conformidade constitucional |
| BUS-CAND-002 | relevância contínua como Outcome ou atributo de qualidade |
| BUS-CAND-003 | entrega de valor distinta de atividade, qualidade e disponibilidade |
| BUS-CAND-004 | confiança e legitimidade como resultado próprio ou emergente |
| BUS-CAND-005 | continuidade econômica independente de métricas e receitas atuais |
| BUS-CAND-006 | crescimento responsável distinto de resiliência e continuidade |
| BUS-CAND-007 | aprendizado institucional como Outcome ou capacidade |
| BUS-CAND-008 | saúde das parcerias como Outcome ou arquitetura de relações |
| BUS-CAND-009 | adequação contextual como Outcome ou princípio de escalabilidade |
| BUS-CAND-010 | reinvestimento como Outcome próprio ou componente da continuidade |

Todos os 18 candidatos devem possuir síntese individual, inclusive quando fizerem parte de um cluster.

## 12. Testes dos clusters de sobreposição

| Cluster | Candidatos | Hipótese que a evidência deve discriminar |
|---|---|---|
| agência e evolução | ECO-CAND-001, 003 e 005 | condições independentes, composição causal ou Outcome agregado |
| oportunidade e experiência | ECO-CAND-002 e 004 | estados permanentes distintos ou etapas de uma jornada |
| confiança | ECO-CAND-006, 008 e BUS-CAND-004 | condição relacional, guardrail e resultado empresarial distintos ou redundantes |
| valor e continuidade | BUS-CAND-003, 005 e 010 | resultados separáveis ou componentes de sustentabilidade |
| adaptação | BUS-CAND-002, 007 e 009 | relevância, aprendizado e adequação contextual como funções distintas |
| resiliência | BUS-CAND-005 e 006 | continuidade, crescimento e resiliência como conceitos separáveis |

Cada cluster deverá produzir uma análise conjunta depois das sínteses individuais. Similaridade linguística isolada não autoriza fusão, e relação causal não prova independência.

## 13. Tratamento de omissões

Sinais de condição material ausente serão registrados como `Omission Signal`, com:

- formulação provisória;
- fontes e nível de evidência;
- relação com candidatos existentes;
- razão pela qual não cabe no conjunto atual;
- risco arquitetural da omissão;
- recomendação de investigar, incorporar, fundir ou adiar.

Um Omission Signal não entra automaticamente no COR. Sua inclusão exige decisão própria da Business Architecture e preservação da origem externa.

## 14. Estados durante a execução

- os 18 registros permanecem `Candidate` enquanto apenas o protocolo existir;
- um registro somente muda para `Under Validation` quando a execução for autorizada e sua primeira evidência qualificada for registrada;
- a mudança deverá ocorrer individualmente, sem atualização em massa por intenção;
- conclusão da coleta não muda o candidato para `Approved`;
- `Approved`, `Rejected`, `Merged` ou `Deferred` dependem da COEM e de decisão formal posterior.

## 15. Entregáveis da execução futura

1. Evidence Registry atualizado com fontes e extrações rastreáveis;
2. relatório de validação externa por candidato;
3. relatório conjunto dos seis clusters;
4. registro de omissões materiais e contraevidências;
5. recomendação arquitetural por candidato, sem decisão automática;
6. avaliação de cobertura, divergência e saturação;
7. gate de prontidão para iniciar a COEM.

## 16. Gate de saída da validação externa

| Critério | Exigência |
|---|---|
| cobertura | 18 sínteses individuais concluídas |
| sobreposição | seis análises conjuntas concluídas |
| rastreabilidade | toda alegação material ligada ao Evidence Registry |
| qualidade | critérios de fonte e níveis de evidência aplicados |
| neutralidade | contradições, limites e ausências preservados |
| completude | busca de omissões e saturação justificadas |
| separação | nenhuma decisão da COEM antecipada |
| revisão | Research e Business Architecture registram seus pareceres |

O gate poderá resultar em `Ready for COEM`, `Additional Evidence Required` ou `Validation Inconclusive`. Somente o primeiro permite propor, em incremento separado, a abertura da COEM.

## 17. Gate deste incremento

| Critério | Resultado |
|---|---|
| escopo dos 18 candidatos declarado | Pass |
| seis clusters cobertos | Pass |
| critérios de fonte definidos | Pass |
| registro mínimo de evidência definido | Pass |
| contradições e omissões tratadas | Pass |
| regra de mudança de estado definida | Pass |
| validação externa executada | In progress — 6/18 candidatos; 2/6 clusters |
| COEM iniciada | Not started |
| Outcomes promovidos | 0 |

## 18. Próximo passo governado

Continuar a validação em lotes sem reduzir a cobertura final dos 18 candidatos e dos seis clusters. O [lote 01 — agência e evolução](outcome-validation-batch-01-agency-evolution.md) e o [lote 02 — confiança](outcome-validation-batch-02-trust.md) estão concluídos; os outros 12 candidatos e quatro clusters permanecem pendentes.
