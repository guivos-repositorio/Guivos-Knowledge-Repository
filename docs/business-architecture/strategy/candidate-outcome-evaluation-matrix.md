---
id: BA-STR-002-COEM-001
title: Candidate Outcome Evaluation Matrix
status: active
version: 0.2.0
owner: Guivos Business Architecture
last_updated: 2026-07-24
parent: BA-STR-002
depends_on:
  - BA-STR-002-COR-001
  - BA-STR-002-EOVP-001
  - GKR-GOV-OUT-001
related:
  - BA-STR-002-EOVB-001
  - BA-STR-002-EOVB-002
  - RP-001-EVIDENCE
normative: false
execution_status: in-progress
---

# BA-STR-002-COEM-001 — Candidate Outcome Evaluation Matrix

## 1. Autoridade e finalidade

Esta matriz aplica os testes obrigatórios do `GKR-GOV-OUT-001` aos 18 candidatos do primeiro Candidate Outcome Register.

Ela transforma evidências e interpretações provisórias em avaliações comparáveis, preservando a diferença entre:

1. resultado de cada teste;
2. disposição recomendada pela matriz;
3. decisão humana sobre o estado do candidato;
4. futura consolidação de Outcomes aprovados na Canon.

A COEM não promove candidatos automaticamente. Uma disposição `Approve`, `Reject`, `Merge`, `Defer` ou `Reformulate` registrada aqui permanece recomendação até decisão humana explícita.

## 2. Estado formal

```text
Matrix: in progress
Candidates in scope: 18
Candidates evaluated: 6
Clusters evaluated: 2 of 6
Current batch: trust
Candidate state changes: 0
Approved Outcomes: 0
Canonical EO/BO codes: 0
AQS-O01: not started
Operational authorization: no
```

## 3. Escopo deste incremento

### Incluído

- definição da escala comum dos quatro testes obrigatórios;
- preservação da calibração aplicada a `ECO-CAND-001`, `ECO-CAND-003` e `ECO-CAND-005`;
- aplicação a `ECO-CAND-006`, `ECO-CAND-008` e `BUS-CAND-004`;
- avaliação conjunta do cluster `confiança`;
- rastreabilidade cumulativa às evidências `RP1-EV-001` a `RP1-EV-018`;
- continuidade do padrão que será aplicado aos outros 12 candidatos.

### Excluído

- mudança de estado dos candidatos;
- criação de códigos canônicos `EO-###` ou `BO-###`;
- estabilização do AQS-O01;
- definição dos catálogos canônicos;
- matriz canônica de sustentação;
- definição de capacidades, produtos, KPIs ou metas;
- retomada de `BA-CAP-001`, Product Engineering ou W0-01.

## 4. Testes obrigatórios

| Teste | Pergunta aplicada | Evidência mínima esperada |
|---|---|---|
| Essential Test | Sem essa condição, o propósito da Guivos continua alcançável de forma sustentável? | relação material com propósito e consequência de ausência |
| Decision Test | Sua degradação contínua exigiria revisão estratégica? | decisão própria de prioridade, investimento, limite ou capacidade |
| Replacement Test | Continua válida após substituição dos produtos e tecnologias atuais? | formulação independente dos meios atuais |
| Outcome Quality Test | Atende às propriedades e ao teste de admissibilidade do BA-STR-002? | permanência, nível correto, independência, observabilidade, rastreabilidade e não redundância |

## 5. Escala de avaliação

| Resultado | Significado |
|---|---|
| Pass | o teste é atendido com evidência e formulação suficientes |
| Partial | o núcleo é material, mas a formulação, fronteira ou natureza arquitetural precisa ser corrigida |
| Fail | o candidato não atende ao teste em sua natureza ou formulação atual |
| Inconclusive | a evidência existente não permite conclusão responsável |

Não há pesos numéricos. Um total aritmético poderia ocultar falhas estruturais, especialmente confusão entre Outcome, capacidade, processo, princípio, guardrail ou etapa de jornada.

## 6. Regra de disposição

| Disposição | Uso na matriz |
|---|---|
| Approve | todos os testes materiais passam e não há reformulação substantiva pendente |
| Reject | o conceito não deve integrar o catálogo de Outcomes e não precisa ser preservado em outro candidato |
| Merge | o conteúdo material deve ser incorporado a outro candidato para evitar redundância |
| Defer | a decisão depende de evidência ou arquitetura ainda indisponível, sem bloquear o BA-STR-002 |
| Reformulate | o núcleo pode permanecer candidato, mas a formulação atual falha em natureza, fronteira ou precisão |

Uma disposição não altera o status do COR neste incremento.

## 7. Matriz cumulativa

| Candidato | Essential | Decision | Replacement | Outcome Quality | Disposição recomendada | Estado decisório |
|---|---|---|---|---|---|---|
| ECO-CAND-001 | Partial | Pass | Pass | Partial | Reformulate | Pending human decision |
| ECO-CAND-003 | Pass | Pass | Pass | Partial | Reformulate | Pending human decision |
| ECO-CAND-005 | Partial | Pass | Pass | Partial | Merge into ECO-CAND-003 | Pending human decision |
| ECO-CAND-002 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| ECO-CAND-004 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| ECO-CAND-006 | Partial | Pass | Pass | Partial | Reformulate | Pending human decision |
| ECO-CAND-007 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| ECO-CAND-008 | Pass | Pass | Pass | Partial | Reformulate | Pending human decision |
| BUS-CAND-001 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-002 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-003 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-004 | Pass | Pass | Pass | Partial | Reformulate | Pending human decision |
| BUS-CAND-005 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-006 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-007 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-008 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-009 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-010 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |

## 8. Avaliação — ECO-CAND-001

### Formulação avaliada

Pessoas, Organizações e Coletivos conseguem compreender seu Momento Atual, necessidades, objetivos, restrições e possibilidades com suficiência para decisões conscientes.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | compreensão insuficiente degrada escolhas conscientes, mas o propósito não depende de transformar compreensão em resultado autônomo; ela pode operar como condição de agência |
| Decision | Pass | degradação persistente exigiria revisão de explicabilidade, captura de contexto, apoio à decisão e capacidades relacionadas |
| Replacement | Pass | a condição permanece válida sem depender de produto, canal, tecnologia ou jornada atual |
| Outcome Quality | Partial | é observável e decisória, porém a evidência a classifica predominantemente como processo ou habilitador; “suficiência” é contextual e pode redundar com agência |

### Evidências determinantes

- `RP1-EV-001` e `RP1-EV-002` sustentam compreensão reflexiva e *sensemaking* como mecanismos que informam ação;
- `RP1-EV-003` bloqueia introspecção ou autorrelato como prova suficiente;
- o lote `BA-STR-002-EOVB-001` identifica dependência funcional de agência.

### Disposição recomendada

`Reformulate`.

Preservar o conceito como condição revisável que sustenta agência efetiva. A futura formulação não deve prometer autoconhecimento completo nem tratar declaração subjetiva como evidência única.

### Limite da recomendação

O candidato permanece `Under Validation`. A matriz não decide ainda se a condição será um Outcome próprio ou uma dimensão do candidato de agência.

## 9. Avaliação — ECO-CAND-003

### Formulação avaliada

Participantes preservam liberdade de escolha e capacidade de definir, revisar ou recusar seus próprios próximos passos de evolução.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Pass | sem liberdade real para definir, revisar ou recusar caminhos, a Guivos deixaria de sustentar transformação autodeterminada |
| Decision | Pass | degradação contínua exigiria revisão de incentivos, padrões de decisão, desenho de capacidades e limites de intervenção |
| Replacement | Pass | agência permanece válida independentemente dos meios atuais |
| Outcome Quality | Partial | o núcleo é permanente, observável e decisório, mas a formulação mistura condição do ecossistema com capacidade exercida pelo participante e precisa incorporar contexto, competência e co-agência |

### Evidências determinantes

- `RP1-EV-004` sustenta formas pessoal, proxy e coletiva de agência;
- `RP1-EV-005` demonstra dependência de competência, pertencimento e contexto;
- `RP1-EV-006` impede reduzir agência a voz ou escolha formal.

### Disposição recomendada

`Reformulate`.

Preservar o núcleo como **agência efetiva e situada**, observada pela existência de condições reais de escolha, revisão, recusa e ação, sem transformar autonomia em adesão, conclusão de tarefas ou isolamento social.

### Limite da recomendação

O candidato permanece `Under Validation`. Uma formulação candidata revisada deverá retornar à matriz antes de qualquer recomendação `Approve`.

## 10. Avaliação — ECO-CAND-005

### Formulação avaliada

Participantes mantêm condições para reconhecer mudanças, aprender e iniciar novos ciclos de evolução coerentes com suas próprias escolhas.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | renovação adaptativa é importante para sustentabilidade do propósito, mas pode ser expressão temporal da agência em vez de Outcome independente |
| Decision | Pass | incapacidade persistente de ajustar, pausar, abandonar ou reiniciar caminhos exigiria revisão estratégica das condições oferecidas pelo ecossistema |
| Replacement | Pass | a condição permanece relevante após substituição dos meios atuais |
| Outcome Quality | Partial | é permanente e observável por múltiplos sinais, mas descreve regulação e processo contínuo e apresenta forte sobreposição com agência |

### Evidências determinantes

- `RP1-EV-007` sustenta desenvolvimento plástico, contextual e multidirecional;
- `RP1-EV-008` e `RP1-EV-009` sustentam ajuste, desengajamento e reengajamento adaptativos;
- o lote externo não demonstrou independência suficiente em relação a `ECO-CAND-003`.

### Disposição recomendada

`Merge into ECO-CAND-003`.

Incorporar continuidade adaptativa como dimensão temporal da agência efetiva: participantes devem poder revisar, pausar, abandonar e reiniciar caminhos diante de mudanças e limites legítimos.

### Limite da recomendação

Nenhuma fusão é executada neste incremento. `ECO-CAND-005` permanece rastreável e `Under Validation` até decisão humana explícita.

## 11. Avaliação conjunta do cluster agência e evolução

### Síntese

```text
compreensão contextual revisável
→ sustenta agência efetiva e situada
→ agência inclui revisar, pausar, recusar e renovar caminhos
```

Os três candidatos são materialmente relevantes, mas a matriz não sustenta três Outcomes pares:

- compreensão funciona principalmente como condição habilitadora;
- agência possui a implicação estratégica mais autônoma;
- continuidade adaptativa funciona como dimensão temporal da agência;
- os três permanecem independentes de produtos e tecnologias;
- a principal insuficiência está na natureza arquitetural e na redundância, não na relevância.

### Resultado calibrado

| Elemento | Resultado |
|---|---|
| candidatos avaliados | 3 de 18 |
| recomendações `Reformulate` | 2 |
| recomendações `Merge` | 1 |
| recomendações `Approve` | 0 |
| mudanças de estado | 0 |
| código canônico criado | 0 |

## 12. Avaliação — ECO-CAND-006

### Formulação avaliada

Participantes formam e preservam relações relevantes que ampliam cooperação, acesso a oportunidades e geração recíproca de valor.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | relações podem ampliar acesso, cooperação e valor recíproco, mas o propósito não depende de maximizar conexão; redes também podem excluir, restringir autonomia e distribuir benefícios de forma desigual |
| Decision | Pass | degradação persistente da qualidade, diversidade ou reciprocidade relacional exigiria revisão da arquitetura de participação, incentivos, mediação e capacidades de parceria |
| Replacement | Pass | a condição relacional permanece válida independentemente de produto, canal, tecnologia ou mecanismo social atual |
| Outcome Quality | Partial | o núcleo é permanente, ecossistêmico e observável, porém “relevantes e fortalecedoras” pressupõe benefício e agrega relação, mecanismo e efeito sem explicitar diversidade, reciprocidade e ausência de dano material |

### Evidências determinantes

- `RP1-EV-010` sustenta pontes relacionais como acesso a informação e oportunidades;
- `RP1-EV-011` sustenta recursos funcionais incorporados às relações;
- `RP1-EV-012` impede usar densidade, coesão ou confiança como prova suficiente e exige observar exclusão, restrição e efeitos sobre terceiros.

### Disposição recomendada

`Reformulate`.

Preservar o núcleo como **saúde relacional no ecossistema**: relações capazes de ampliar acesso, cooperação e valor recíproco com diversidade estrutural, autonomia e limites contra exclusão ou dano material.

### Limite da recomendação

O candidato permanece `Under Validation`. A reformulação não transforma número de conexões, intensidade de vínculos ou coesão em evidência de saúde relacional.

## 13. Avaliação — ECO-CAND-008

### Formulação avaliada

Participantes interagem em condições de transparência, segurança, privacidade, justiça, contestabilidade e respeito à sua autonomia.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Pass | participação sem proteção, justiça, contestabilidade ou autonomia comprometeria a legitimidade do ecossistema e tornaria seu propósito insustentável |
| Decision | Pass | degradação contínua exigiria revisão estratégica de riscos, direitos, governança, desenho de capacidades e limites operacionais, além de remediação pontual |
| Replacement | Pass | a necessidade de participação protegida permanece válida após substituição de produtos e tecnologias |
| Outcome Quality | Partial | a condição vivida é permanente e observável, mas a formulação agrega múltiplos guardrails, controles e percepções; segurança e privacidade são geridas, enquanto confiança e justiça não decorrem automaticamente de conformidade |

### Evidências determinantes

- `RP1-EV-013` trata privacidade como gestão contínua de riscos a indivíduos;
- `RP1-EV-014` trata segurança como ciclo governado de risco, resposta e recuperação;
- `RP1-EV-015` e `RP1-EV-016` separam justiça procedimental, legitimidade, confiança, confiabilidade percebida e aceitação de vulnerabilidade.

### Disposição recomendada

`Reformulate`.

Preservar uma única condição de **participação protegida, justa e contestável**, observável na experiência e nos efeitos sobre participantes. Privacidade, segurança, transparência e autonomia devem permanecer guardrails verificáveis e meios de sustentação, não sub-Outcomes acumulados na definição.

### Limite da recomendação

O candidato permanece `Under Validation`. Proteção absoluta é impossível, cumprimento de controles não prova confiança e percepção de confiança não substitui proteção verificável.

## 14. Avaliação — BUS-CAND-004

### Formulação avaliada

A Guivos preserva confiança e legitimidade suficientes para manter relações voluntárias, transparentes e duradouras no ecossistema.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Pass | perda persistente de confiança ou legitimidade comprometeria relações voluntárias, cooperação e autoridade institucional necessárias à sustentabilidade do propósito |
| Decision | Pass | degradação contínua exigiria revisão própria de conduta, governança, controles, cultura, liderança, reparação e posicionamento institucional |
| Replacement | Pass | confiança e legitimidade permanecem materiais independentemente dos produtos e tecnologias atuais |
| Outcome Quality | Partial | a formulação é permanente, observável e decisória, mas combina dois fenômenos emergentes distintos e ainda os relaciona diretamente à duração das relações, confundindo condição, efeito e evidência |

### Evidências determinantes

- `RP1-EV-016` distingue confiança, confiabilidade percebida e comportamento de assumir risco;
- `RP1-EV-017` define legitimidade como avaliação socialmente conferida e multidimensional;
- `RP1-EV-018` mostra que confiança pode ser degradada por falhas sistêmicas e que sua reparação depende de mudanças materiais, não de comunicação reputacional isolada.

### Disposição recomendada

`Reformulate`.

Separar conceitualmente **confiança institucional** e **legitimidade institucional** dentro da avaliação, definindo qual condição possui unidade suficiente para permanecer como Business Outcome e tratando a outra como dimensão, evidência relacionada ou candidato revisado. Nenhuma delas deve ser reduzida a reputação, conformidade, satisfação ou longevidade contratual.

### Limite da recomendação

O candidato permanece `Under Validation`. A matriz não cria novo candidato, não escolhe antecipadamente qual dimensão prevalece e não atribui à Guivos controle unilateral sobre avaliações socialmente conferidas.

## 15. Avaliação conjunta do cluster confiança

### Síntese

```text
guardrails verificáveis
→ reduzem vulnerabilidades evitáveis
→ sustentam participação protegida e contestável
→ relações saudáveis ampliam cooperação e acesso
→ experiências e coerência institucional influenciam confiança e legitimidade
```

Os três candidatos ocupam camadas diferentes e não devem ser fundidos:

- `ECO-CAND-006` descreve uma condição relacional do ecossistema;
- `ECO-CAND-008` combina uma condição vivida com guardrails que precisam ser separados na redação;
- `BUS-CAND-004` combina duas avaliações institucionais emergentes e conceitualmente distintas;
- os três permanecem relevantes depois da substituição dos meios atuais;
- a insuficiência comum está na precisão e unidade da formulação, não na materialidade estratégica.

### Resultado cumulativo

| Elemento | Resultado |
|---|---|
| candidatos avaliados | 6 de 18 |
| clusters avaliados | 2 de 6 |
| recomendações `Reformulate` | 5 |
| recomendações `Merge` | 1 |
| recomendações `Approve` | 0 |
| mudanças de estado | 0 |
| código canônico criado | 0 |

## 16. Gate do incremento

| Critério | Resultado |
|---|---|
| quatro testes obrigatórios aplicados | 6/6 — Pass |
| evidência externa rastreável | Pass |
| contradições e limites preservados | Pass |
| disposição singular por candidato | Pass |
| distinção entre recomendação e decisão | Pass |
| promoção automática bloqueada | Pass |
| candidatos avaliados | 6/18 — In progress |
| clusters avaliados | 2/6 — In progress |
| AQS-O01 iniciado | No |
| Outcomes canônicos definidos | 0 |

## 17. Próximo passo governado

Submeter as seis disposições cumulativas à revisão humana. Se o padrão permanecer aceito, continuar a COEM pelo próximo cluster governado, sem executar automaticamente nenhuma recomendação, alterar o COR ou criar Outcomes canônicos.
