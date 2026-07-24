---
id: BA-STR-002-COEM-001
title: Candidate Outcome Evaluation Matrix
status: active
version: 0.1.0
owner: Guivos Business Architecture
last_updated: 2026-07-23
parent: BA-STR-002
depends_on:
  - BA-STR-002-COR-001
  - BA-STR-002-EOVP-001
  - GKR-GOV-OUT-001
related:
  - BA-STR-002-EOVB-001
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
Matrix: initiated
Candidates in scope: 18
Candidates evaluated: 3
Clusters evaluated: 1 of 6
Current batch: agency and evolution
Candidate state changes: 0
Approved Outcomes: 0
Canonical EO/BO codes: 0
AQS-O01: not started
Operational authorization: no
```

## 3. Escopo deste incremento

### Incluído

- definição da escala comum dos quatro testes obrigatórios;
- aplicação inicial a `ECO-CAND-001`, `ECO-CAND-003` e `ECO-CAND-005`;
- avaliação conjunta do cluster `agência e evolução`;
- rastreabilidade às evidências `RP1-EV-001` a `RP1-EV-009`;
- calibração do padrão que será aplicado aos outros 15 candidatos.

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
| ECO-CAND-006 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| ECO-CAND-007 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| ECO-CAND-008 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-001 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-002 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-003 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
| BUS-CAND-004 | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Under Validation |
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

## 11. Avaliação conjunta do cluster

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

## 12. Gate do incremento

| Critério | Resultado |
|---|---|
| quatro testes obrigatórios aplicados | 3/3 — Pass |
| evidência externa rastreável | Pass |
| contradições e limites preservados | Pass |
| disposição singular por candidato | Pass |
| distinção entre recomendação e decisão | Pass |
| promoção automática bloqueada | Pass |
| candidatos avaliados | 3/18 — In progress |
| clusters avaliados | 1/6 — In progress |
| AQS-O01 iniciado | No |
| Outcomes canônicos definidos | 0 |

## 13. Próximo passo governado

Submeter as três disposições calibradas à revisão humana. Se o padrão for aceito, continuar a COEM pelo cluster `confiança`, aplicando a mesma escala a `ECO-CAND-006`, `ECO-CAND-008` e `BUS-CAND-004`, sem executar as disposições deste lote automaticamente.
