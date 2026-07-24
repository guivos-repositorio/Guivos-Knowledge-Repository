---
id: BA-STR-002-COEM-001
title: Candidate Outcome Evaluation Matrix
status: active
version: 0.6.0
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
  - BA-STR-002-EOVB-003
  - BA-STR-002-EOVB-004
  - BA-STR-002-EOVB-005
  - BA-STR-002-EOVB-006
  - RP-001-EVIDENCE
normative: false
execution_status: completed
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
Matrix: completed
Candidates in scope: 18
Candidates evaluated: 18
Clusters evaluated: 6 of 6
Current batch: coverage completion
Candidate state changes: 0
Approved Outcomes: 0
Canonical EO/BO codes: 0
AQS-O01: not started
Operational authorization: no
```

## 3. Escopo deste incremento

### Incluído

- definição da escala comum dos quatro testes obrigatórios;
- preservação das treze avaliações dos cinco clusters anteriores;
- aplicação a `ECO-CAND-002`, `ECO-CAND-004`, `ECO-CAND-007`, `BUS-CAND-001` e `BUS-CAND-008`;
- avaliação conjunta do cluster `oportunidade e experiência`;
- sínteses individuais de inclusão e dignidade, propósito e parcerias;
- rastreabilidade cumulativa às evidências `RP1-EV-001` a `RP1-EV-060`;
- conclusão da cobertura matricial dos 18 candidatos e seis clusters.

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
| ECO-CAND-002 | Pass | Pass | Pass | Partial | Reformulate | Pending human decision |
| ECO-CAND-004 | Partial | Pass | Pass | Fail | Reject | Pending human decision |
| ECO-CAND-006 | Partial | Pass | Pass | Partial | Reformulate | Pending human decision |
| ECO-CAND-007 | Pass | Pass | Pass | Partial | Reformulate | Pending human decision |
| ECO-CAND-008 | Pass | Pass | Pass | Partial | Reformulate | Pending human decision |
| BUS-CAND-001 | Partial | Pass | Pass | Fail | Reject | Pending human decision |
| BUS-CAND-002 | Partial | Pass | Pass | Partial | Merge into BUS-CAND-003 | Pending human decision |
| BUS-CAND-003 | Partial | Pass | Pass | Partial | Reformulate | Pending human decision |
| BUS-CAND-004 | Pass | Pass | Pass | Partial | Reformulate | Pending human decision |
| BUS-CAND-005 | Pass | Pass | Pass | Partial | Reformulate | Pending human decision |
| BUS-CAND-006 | Fail | Partial | Pass | Fail | Reject | Pending human decision |
| BUS-CAND-007 | Partial | Pass | Pass | Fail | Reject | Pending human decision |
| BUS-CAND-008 | Partial | Pass | Pass | Fail | Reject | Pending human decision |
| BUS-CAND-009 | Partial | Pass | Pass | Fail | Reject | Pending human decision |
| BUS-CAND-010 | Partial | Pass | Pass | Partial | Merge into BUS-CAND-005 | Pending human decision |

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

## 16. Avaliação — BUS-CAND-003

### Formulação avaliada

A Guivos entrega valor legítimo com qualidade, segurança e continuidade suficientes para sustentar experiências relevantes.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | capacidade consistente de habilitar valor legítimo é material ao propósito, mas valor é contextual e cocriado; a Guivos não controla unilateralmente sua realização por participantes e stakeholders |
| Decision | Pass | degradação persistente da qualidade, segurança, continuidade ou legitimidade da entrega exigiria revisão de prioridades, capacidades, proposições, controles e relações econômicas |
| Replacement | Pass | a necessidade de habilitar valor legítimo e consistente permanece válida independentemente dos produtos, canais ou tecnologias atuais |
| Outcome Quality | Partial | a formulação é permanente e decisória, porém combina capacidade organizacional, propriedades de qualidade, guardrails e resultado vivido por terceiros, sem uma unidade observável própria |

### Evidências determinantes

- `RP1-EV-019` sustenta valor como contextual e cocriado, bloqueando a leitura de entrega unilateral;
- `RP1-EV-020` trata consistência, conformidade e melhoria como resultados de um sistema de gestão da qualidade;
- `RP1-EV-021` amplia valor para utilidades e relações distributivas entre múltiplos stakeholders.

### Disposição recomendada

`Reformulate`.

Preservar a condição empresarial de **habilitar valor legítimo com consistência**, distinguindo-a do valor efetivamente realizado pelos participantes. Qualidade, segurança e continuidade devem sustentar a formulação como propriedades verificáveis, sem serem acumuladas como sub-Outcomes.

### Limite da recomendação

O candidato permanece `Under Validation`. A reformulação não transfere à Guivos controle sobre valor contextual, não substitui Outcomes do ecossistema e não converte satisfação pontual ou disponibilidade técnica em prova suficiente.

## 17. Avaliação — BUS-CAND-005

### Formulação avaliada

A Guivos mantém recursos, capacidade e equilíbrio econômico suficientes para cumprir obrigações e preservar o valor essencial ao longo do tempo.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Pass | sem continuidade econômica suficiente para cumprir obrigações e preservar valor essencial, o propósito não pode ser sustentado ao longo do tempo |
| Decision | Pass | degradação contínua exigiria revisão própria de modelo econômico, compromissos, prioridades, riscos, reservas, dependências e capacidade institucional |
| Replacement | Pass | a condição permanece válida após substituição de receitas, produtos, estruturas, tecnologias e mecanismos financeiros atuais |
| Outcome Quality | Partial | o núcleo é permanente, observável e decisório, mas a formulação agrega viabilidade econômica, continuidade operacional, capacidade organizacional e sustentabilidade estratégica sem fronteiras explícitas |

### Evidências determinantes

- `RP1-EV-022` distingue continuidade operacional como capacidade governada de manter entregas aceitáveis durante disrupções;
- `RP1-EV-023` limita *going concern* a uma avaliação contábil prospectiva, não à definição integral de sustentabilidade;
- `RP1-EV-024` amplia sustentabilidade para criação de valor em múltiplos horizontes e dimensões;
- `RP1-EV-028` a `RP1-EV-031` relacionam resiliência à continuidade sem reduzi-la a estabilidade, caixa ou retorno ao estado anterior.

### Disposição recomendada

`Reformulate`.

Preservar **continuidade econômica sustentável** como condição empresarial autônoma, centrada na capacidade de cumprir obrigações e sustentar valor essencial em múltiplos horizontes. Continuidade operacional, resiliência e equilíbrio financeiro devem permanecer dimensões ou capacidades sustentadoras, não sinônimos do Outcome.

### Limite da recomendação

O candidato permanece `Under Validation`. A formulação revisada deverá evitar uma métrica financeira única, promessa de permanência absoluta ou confusão entre sobrevivência contábil, disponibilidade operacional e geração sustentável de valor.

## 18. Avaliação — BUS-CAND-010

### Formulação avaliada

A Guivos mantém condições para reinvestir valor legitimamente capturado no fortalecimento de capacidades, conhecimento e valor entregue ao ecossistema.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | renovação de capacidades pode exigir investimento, mas o propósito pode continuar por diferentes fontes e formas de financiamento; reinvestimento interno não é condição universal nem intrinsecamente responsável |
| Decision | Pass | incapacidade persistente de financiar renovação ou alocação destrutiva de recursos exigiria revisão estratégica de capital, prioridades, riscos e alternativas de financiamento |
| Replacement | Pass | a necessidade de alocar recursos para renovação permanece válida, embora os mecanismos, fontes e objetos de investimento possam mudar integralmente |
| Outcome Quality | Partial | o conceito é decisório e observável, mas descreve predominantemente uma condição financeira e um mecanismo governado de alocação, com forte dependência da continuidade econômica |

### Evidências determinantes

- `RP1-EV-025` mostra que fundos internos podem ser materiais quando há restrições de financiamento;
- `RP1-EV-026` demonstra custos de agência e risco de sobreinvestimento, bloqueando a presunção de benefício automático;
- `RP1-EV-027` trata alocação de capital, estratégia e sustentabilidade como responsabilidades de governança.

### Disposição recomendada

`Merge into BUS-CAND-005`.

Incorporar a capacidade governada de financiar renovação e preservar opções de investimento como dimensão de continuidade econômica sustentável. Reinvestimento deve permanecer decisão de alocação condicionada por adicionalidade, riscos, obrigações e alternativas legítimas de uso ou financiamento.

### Limite da recomendação

Nenhuma fusão é executada neste incremento. `BUS-CAND-010` permanece rastreável e `Under Validation`; maior retenção ou gasto não constitui evidência de responsabilidade, eficácia ou geração futura de valor.

## 19. Avaliação conjunta do cluster valor e continuidade

### Síntese

```text
capacidades e proposições habilitam valor contextual
→ relações legítimas permitem captura econômica
→ continuidade preserva obrigações e valor essencial
→ alocação governada financia renovação quando justificável
→ capacidades renovadas ampliam futuras condições de valor
```

O cluster descreve um ciclo de sustentação, não três Outcomes empresariais equivalentes:

- `BUS-CAND-003` mistura a condição empresarial de habilitar valor com propriedades de entrega e valor realizado por terceiros;
- `BUS-CAND-005` possui a unidade decisória mais próxima de um Business Outcome autônomo, embora ainda precise de fronteiras explícitas;
- `BUS-CAND-010` descreve principalmente mecanismo governado de alocação e financiamento da renovação;
- a relação causal e econômica entre os três não elimina suas diferenças de natureza;
- a recomendação de fusão preserva rastreabilidade e depende de decisão humana posterior.

### Resultado cumulativo

| Elemento | Resultado |
|---|---|
| candidatos avaliados | 9 de 18 |
| clusters avaliados | 3 de 6 |
| recomendações `Reformulate` | 7 |
| recomendações `Merge` | 2 |
| recomendações `Approve` | 0 |
| mudanças de estado | 0 |
| código canônico criado | 0 |

## 20. Avaliação — BUS-CAND-006

### Formulação avaliada

A Guivos amplia alcance e valor sem degradar qualidade, proteção, capacidade, diversidade de dependências ou continuidade.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Fail | o propósito pode permanecer alcançável de forma sustentável sem crescimento em determinado período; expansão não é condição universal nem obrigatória |
| Decision | Partial | degradação causada por uma expansão exigiria revisão estratégica, mas ausência ou desaceleração de crescimento não exige revisão por si mesma; a implicação decisória pertence aos limites e Outcomes que a expansão não pode degradar |
| Replacement | Pass | a possibilidade de ampliar alcance e valor continua compreensível após substituição dos produtos e tecnologias atuais |
| Outcome Quality | Fail | a formulação descreve trajetória estratégica opcional e agrega critérios de admissibilidade, capacidades e propriedades de continuidade, em vez de estado empresarial permanente e autônomo |

### Evidências determinantes

- `RP1-EV-032` sustenta a tensão entre exploração de novas possibilidades e uso das competências existentes;
- `RP1-EV-033` reclassifica capacidades dinâmicas como processos de reconfiguração, sem garantia de resultado permanente;
- `RP1-EV-034` e `RP1-EV-035` mostram que crescimento é condicionado por rentabilidade, retenção, ativos, financiamento, conhecimento e capacidade gerencial;
- `RP1-EV-036` demonstra que a relação entre alto crescimento e sobrevivência é contingente;
- `RP1-EV-028` a `RP1-EV-031` sustentam resiliência como propriedade e capacidade adaptativa, não como sinônimo de expansão.

### Disposição recomendada

`Reject`.

Retirar crescimento do futuro catálogo de Business Outcomes. Preservar **expansão responsável** como trajetória estratégica opcional, sujeita a capacidade demonstrada, adicionalidade e critérios de não degradação. Incorporar resiliência e adaptação legítima à reformulação de `BUS-CAND-005` e às futuras capacidades sustentadoras.

### Limite da recomendação

O candidato permanece `Under Validation`. A recomendação não proíbe crescimento, não rejeita a importância de ampliar alcance e valor e não executa qualquer mudança de estado; ela rejeita apenas a formulação de crescimento como Outcome permanente.

## 21. Avaliação conjunta do cluster resiliência

### Síntese

```text
continuidade econômica sustentável
→ exige capacidades de antecipação, resposta e adaptação
→ preserva opções estratégicas e valor essencial
→ expansão pode ser escolhida quando capacidade e contexto permitem
→ novos riscos e dependências retornam ao gate de continuidade
```

O cluster descreve uma condição permanente e uma trajetória opcional, não dois Outcomes equivalentes:

- `BUS-CAND-005` permanece recomendado para reformulação como eixo de continuidade econômica sustentável;
- resiliência funciona como propriedade do eixo e como conjunto de capacidades sustentadoras;
- `BUS-CAND-006` combina decisão de expansão, restrições de responsabilidade e propriedades de continuidade;
- não crescimento deliberado pode ser estratégia legítima;
- a avaliação conjunta não reabre nem reconta `BUS-CAND-005`.

### Resultado cumulativo

| Elemento | Resultado |
|---|---|
| candidatos avaliados | 10 de 18 |
| clusters avaliados | 4 de 6 |
| recomendações `Reformulate` | 7 |
| recomendações `Merge` | 2 |
| recomendações `Reject` | 1 |
| recomendações `Approve` | 0 |
| mudanças de estado | 0 |
| código canônico criado | 0 |

## 22. Avaliação — BUS-CAND-002

### Formulação avaliada

As respostas organizadas pela Guivos permanecem relevantes diante da mudança de contextos, necessidades e prioridades dos participantes.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | respostas relevantes são materiais à geração de valor, mas o propósito não exige que relevância seja um estado empresarial autônomo; ela emerge do ajuste entre contexto, capacidades, proposições e valor vivido |
| Decision | Pass | degradação persistente da relevância exigiria revisão estratégica de inteligência, prioridades, proposições, capacidades de resposta e critérios de valor |
| Replacement | Pass | a necessidade de produzir respostas contextualmente relevantes permanece válida após substituição dos produtos, canais e tecnologias atuais |
| Outcome Quality | Partial | o conceito é observável e decisório, porém descreve qualidade emergente e percebida, com forte sobreposição à habilitação consistente de valor de `BUS-CAND-003` |

### Evidências determinantes

- `RP1-EV-037` relaciona relevância à geração, disseminação e resposta organizacional à inteligência;
- `RP1-EV-038` relaciona orientação de mercado a desempenho sem demonstrar Outcome autônomo;
- `RP1-EV-039` impede reduzir relevância a reação aos pedidos expressos dos participantes atuais;
- a avaliação de `BUS-CAND-003` já preserva valor como contextual e distingue habilitação empresarial de realização por terceiros.

### Disposição recomendada

`Merge into BUS-CAND-003`.

Incorporar **relevância contextual contínua** como propriedade observável da condição empresarial de habilitar valor legítimo com consistência. A formulação resultante deve exigir detecção de mudanças e resposta coerente sem prometer relevância universal, permanente ou unilateralmente controlada.

### Limite da recomendação

Nenhuma fusão é executada neste incremento. `BUS-CAND-002` permanece rastreável e `Under Validation`; personalização, satisfação pontual ou resposta rápida não constituem prova suficiente de relevância.

## 23. Avaliação — BUS-CAND-007

### Formulação avaliada

A Guivos transforma evidências, conhecimento e resultados observados em decisões que preservam coerência e melhoram continuamente sua geração de valor.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | aprender e renovar capacidades é necessário à sustentabilidade do propósito em ambientes mutáveis, mas aprendizagem descreve o meio institucional de adaptação, não o estado permanente de resultado |
| Decision | Pass | incapacidade persistente de interpretar, integrar, institucionalizar ou usar conhecimento exigiria revisão estratégica de governança, memória, diversidade, incentivos e capacidades |
| Replacement | Pass | a necessidade de aprendizagem institucional permanece válida independentemente das fontes de evidência, estruturas, métodos ou tecnologias atuais |
| Outcome Quality | Fail | a formulação descreve processos multinível e uma capacidade dinâmica, combina mecanismo com melhoria presumida e não possui unidade de Outcome independente |

### Evidências determinantes

- `RP1-EV-040` modela aprendizagem como processos entre níveis individual, grupal e organizacional;
- `RP1-EV-041` define capacidade absortiva como habilidade cumulativa de reconhecer, assimilar e aplicar conhecimento;
- `RP1-EV-042` demonstra miopia temporal, espacial e de falhas, bloqueando a presunção de melhoria contínua;
- a análise de resiliência já posiciona antecipação, resposta e adaptação como capacidades sustentadoras.

### Disposição recomendada

`Reject`.

Retirar aprendizado institucional do futuro catálogo de Business Outcomes. Preservá-lo como capacidade sustentadora de sensing, interpretação, memória, contestação, renovação e adaptação, vinculada aos Outcomes que vierem a exigir resposta a mudanças.

### Limite da recomendação

O candidato permanece `Under Validation`. A recomendação não reduz a importância de aprender, não autoriza sua remoção da arquitetura e não considera coleta de dados, analytics, IA ou retrospectivas como evidência suficiente de aprendizagem institucional.

## 24. Avaliação — BUS-CAND-009

### Formulação avaliada

A Guivos preserva identidade e coerência arquitetural enquanto se adapta legitimamente a países, culturas, idiomas e contextos distintos.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | coerência e adequação são necessárias à atuação legítima em contextos diversos, mas não constituem condição empresarial universal separada; sua materialidade depende da estratégia e do contexto de atuação |
| Decision | Pass | fragmentação persistente ou inadequação contextual exigiria revisão estratégica de identidade, autoridade, governança, internacionalização e desenho de capacidades |
| Replacement | Pass | a tensão entre coerência e adaptação permanece válida depois da substituição de produtos, estruturas e tecnologias |
| Outcome Quality | Fail | a formulação combina princípio arquitetural, escolha estratégica contingente e critério de admissibilidade; não há estado único nem solução superior observável em todos os contextos |

### Evidências determinantes

- `RP1-EV-043` sustenta desempenho quando o grau de padronização se ajusta ao ambiente;
- `RP1-EV-044` mostra que transferência transnacional depende de contextos sociais, organizacionais e relacionais;
- `RP1-EV-045` registra resultados mistos sobre padronização, adaptação e desempenho;
- tradução, presença local e variação de produto não comprovam adequação legítima.

### Disposição recomendada

`Reject`.

Retirar coerência global com adequação contextual do futuro catálogo de Business Outcomes. Preservar o conteúdo como princípio arquitetural e critério governado para internacionalização, desenho de capacidades e avaliação de mudanças, relacionado à aderência ao propósito e à legitimidade institucional.

### Limite da recomendação

O candidato permanece `Under Validation`. A recomendação não impõe padronização global, não proíbe adaptação local e não antecipa a avaliação de `BUS-CAND-001`; ela corrige somente a classificação do conceito como Outcome autônomo.

## 25. Avaliação conjunta do cluster adaptação

### Síntese

```text
mudanças de contexto e sinais externos
→ capacidades de sensing, absorção e aprendizagem
→ escolhas governadas de resposta
→ coerência e adequação funcionam como critérios
→ relevância emerge na habilitação e realização de valor
→ novos efeitos alimentam aprendizagem e revisão
```

O cluster descreve um sistema adaptativo, não três Outcomes equivalentes:

- `BUS-CAND-002` expressa uma propriedade emergente da habilitação consistente de valor;
- `BUS-CAND-007` descreve predominantemente capacidade institucional multinível;
- `BUS-CAND-009` combina princípio arquitetural e critério de decisão contingente;
- os três permanecem relevantes após substituição dos meios atuais, mas falham em autonomia ou natureza arquitetural;
- a fusão recomendada preserva relevância em `BUS-CAND-003`, enquanto as rejeições preservam aprendizagem e adequação em suas camadas corretas.

### Resultado cumulativo

| Elemento | Resultado |
|---|---|
| candidatos avaliados | 13 de 18 |
| clusters avaliados | 5 de 6 |
| recomendações `Reformulate` | 7 |
| recomendações `Merge` | 3 |
| recomendações `Reject` | 3 |
| recomendações `Approve` | 0 |
| mudanças de estado | 0 |
| código canônico criado | 0 |

## 26. Avaliação — ECO-CAND-002

### Formulação avaliada

Participantes encontram possibilidades legítimas, compreensíveis e relevantes para seu contexto, seus objetivos e seu momento de vida.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Pass | sem possibilidades reais de acesso, compreensão e escolha, o ecossistema não amplia de forma material as condições para transformação autodeterminada |
| Decision | Pass | degradação persistente do acesso real exigiria revisão estratégica de curadoria, elegibilidade, acessibilidade, fatores de conversão, diversidade e capacidades de resposta |
| Replacement | Pass | a condição permanece válida independentemente de catálogo, recomendação, marketplace, canal ou tecnologia |
| Outcome Quality | Partial | o núcleo é permanente, ecossistêmico e observável, mas “encontram possibilidades” sugere disponibilidade ou descoberta nominal e não explicita liberdade real, restrições e capacidade de conversão |

### Evidências determinantes

- `RP1-EV-046` distingue oportunidades reais de funcionamentos efetivamente realizados;
- `RP1-EV-047` separa escopo de escolha, ato de escolher, restrições e fatores de conversão;
- `RP1-EV-048` demonstra que mais opções podem reduzir escolha, satisfação e desempenho;
- volume de ofertas, exposição ou recomendação não comprova acesso real.

### Disposição recomendada

`Reformulate`.

Preservar o núcleo como **acesso real a possibilidades legítimas e manejáveis**: participantes dispõem de condições para compreender, converter, comparar e escolher possibilidades compatíveis com seu contexto, sem transformar abundância de opções em prova de valor.

### Limite da recomendação

O candidato permanece `Under Validation`. A reformulação não promete acesso irrestrito, escolha, realização da experiência ou transformação posterior.

## 27. Avaliação — ECO-CAND-004

### Formulação avaliada

Participantes conseguem converter oportunidades escolhidas em experiências vividas que produzem valor percebido e potencial de evolução.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | experiências são o momento em que participantes podem realizar valor, mas o propósito não depende de transformar cada realização episódica em condição permanente autônoma |
| Decision | Pass | incapacidade persistente de participantes realizarem valor exigiria revisão estratégica das possibilidades, capacidades, barreiras, relações e experiências sustentadas pelo ecossistema |
| Replacement | Pass | experiência e valor em uso permanecem materiais depois da substituição dos produtos, canais e tecnologias atuais |
| Outcome Quality | Fail | a formulação descreve conversão, episódio vivido, avaliação subjetiva e efeito potencial em sequência; mistura etapa de jornada, experiência e promessa de evolução sem unidade permanente própria |

### Evidências determinantes

- `RP1-EV-049` posiciona o participante como criador primário do valor em uso e a organização como facilitadora;
- `RP1-EV-050` demonstra dimensões simbólicas, afetivas, estéticas e utilitárias da experiência;
- `RP1-EV-051` separa experiência momento a momento de avaliação retrospectiva;
- o `BA-STR-002` já distingue Outcome, experiência e resultado observado.

### Disposição recomendada

`Reject`.

Retirar realização de experiências de valor do futuro catálogo de Ecosystem Outcomes. Preservar experiência como momento de realização de valor, unidade arquitetural da jornada e fonte de evidência para os Outcomes, sem prometer transformação causal ou efeito duradouro.

### Limite da recomendação

O candidato permanece `Under Validation`. A recomendação não reduz a centralidade das experiências nem as incorpora a `ECO-CAND-002`; corrige apenas sua classificação como Outcome permanente autônomo.

## 28. Avaliação conjunta do cluster oportunidade e experiência

### Síntese

```text
possibilidades legítimas e manejáveis
→ fatores reais de acesso e conversão
→ compreensão e escolha autônoma
→ experiência realizada
→ valor vivido e avaliação
→ evidências para novos ciclos e decisões
```

O cluster descreve condições e ocorrências relacionadas, não dois Outcomes pares nem um catálogo organizado como jornada:

- `ECO-CAND-002` preserva uma condição permanente de liberdade real de acesso;
- `ECO-CAND-004` descreve predominantemente episódio de realização e avaliação de valor;
- acesso não garante escolha, experiência ou transformação;
- experiência não prova causalidade, permanência ou efeito posterior;
- a distinção entre oportunidade real e funcionamento realizado permanece rastreável sem promover ambos a Outcomes.

## 29. Avaliação — ECO-CAND-007

### Formulação avaliada

Participantes de diferentes culturas, crenças, países e contextos conseguem participar do ecossistema com dignidade, acolhimento e acesso a valor essencial.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Pass | participação estruturalmente excludente ou indigna contradiz o propósito, a universalidade responsável e a legitimidade do ecossistema |
| Decision | Pass | degradação persistente exigiria revisão estratégica de barreiras, elegibilidade, acessibilidade, representação, voz, proteção, capacidades e alocação de recursos |
| Replacement | Pass | inclusão e dignidade permanecem materiais independentemente dos meios atuais |
| Outcome Quality | Partial | a condição vivida é permanente e observável, mas a formulação combina diversidade, direitos, acolhimento, acesso e valor essencial, misturando Outcome, guardrails constitucionais e capacidades |

### Evidências determinantes

- `RP1-EV-052` relaciona dignidade, não discriminação, acessibilidade, autonomia e participação plena;
- `RP1-EV-053` demonstra que disponibilidade técnica não comprova inclusão;
- `RP1-EV-054` separa participação efetiva de informação, consulta simbólica e tokenismo;
- cadastro, tradução, presença global ou representação nominal não comprovam participação inclusiva.

### Disposição recomendada

`Reformulate`.

Preservar o núcleo como **participação inclusiva, digna e efetiva**, observável na remoção de barreiras materiais, capacidade de uso, respeito, voz e contestabilidade. Direitos, guardrails e capacidades de acessibilidade devem sustentar a condição sem serem acumulados em sua definição.

### Limite da recomendação

O candidato permanece `Under Validation`. A reformulação não promete acesso universal imediato, elimina requisitos legítimos nem reduz inclusão a presença, cadastro ou representação.

## 30. Avaliação — BUS-CAND-001

### Formulação avaliada

A Guivos mantém decisões, investimentos, relações e evolução institucional coerentes com seu propósito e seus princípios permanentes.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | aderência ao propósito é indispensável à legitimidade institucional, mas sua ausência constitui violação constitucional e de governança, não falta de um resultado empresarial autônomo |
| Decision | Pass | sinais persistentes de mission drift exigiriam revisão estratégica, accountability, correção de autoridade, portfólio, investimentos e relações |
| Replacement | Pass | a obrigação permanece válida depois da substituição dos produtos, estruturas e tecnologias |
| Outcome Quality | Fail | a formulação descreve orientação superior, conformidade constitucional e dever permanente de governança; promovê-la a Outcome faria o propósito medir a aderência a si próprio |

### Evidências determinantes

- `RP1-EV-055` distingue propósito como razão de ser de sua declaração;
- `RP1-EV-056` registra ambiguidade conceitual e impede confundir propósito com efeitos de desempenho;
- `RP1-EV-057` posiciona prevenção de mission drift em governança, controle e accountability;
- coerência declarada não comprova prática institucional.

### Disposição recomendada

`Reject`.

Retirar aderência permanente ao propósito do futuro catálogo de Business Outcomes. Preservá-la como princípio constitucional, obrigação de governança e critério de admissibilidade para decisões, capacidades, produtos, relações e Outcomes.

### Limite da recomendação

O candidato permanece `Under Validation`. A recomendação não relativiza o propósito nem reduz sua autoridade; impede apenas que um dever constitucional seja tratado como resultado empresarial.

## 31. Avaliação — BUS-CAND-008

### Formulação avaliada

A rede de parceiros permanece qualificada, alinhada, diversa e capaz de gerar valor recíproco sem transferir indevidamente autoridade ou risco.

### Aplicação dos testes

| Teste | Resultado | Fundamentação |
|---|---|---|
| Essential | Partial | relações de parceria podem sustentar valor e escala, mas o propósito não depende de uma rede ou composição específica e pode exigir diferentes formas de provisão ao longo do tempo |
| Decision | Pass | degradação persistente de valor, alinhamento, diversidade, autoridade ou risco exigiria revisão estratégica do portfólio, critérios de entrada, governança, controles, aprendizagem e saída |
| Replacement | Pass | a necessidade de governar dependências e relações externas permanece válida independentemente dos parceiros, contratos, produtos e tecnologias atuais |
| Outcome Quality | Fail | a formulação agrega qualificação, alinhamento, diversidade, reciprocidade, autoridade e risco em uma condição gerida; sua unidade depende de capacidades de alianças e governança relacional |

### Evidências determinantes

- `RP1-EV-058` demonstra que recursos e rendas relacionais podem residir entre organizações;
- `RP1-EV-059` reclassifica gestão de alianças e aprendizagem acumulada como capacidade;
- `RP1-EV-060` distingue riscos relacionais e de desempenho e combina confiança com controles;
- quantidade, duração ou ausência de conflito não comprovam saúde, e encerramento pode ser legítimo.

### Disposição recomendada

`Reject`.

Retirar saúde das relações de parceria do futuro catálogo de Business Outcomes. Preservar o conteúdo na arquitetura de capacidades, governança de parceiros e critérios de portfólio, relacionado à habilitação de valor, legitimidade e continuidade quando houver dependências externas materiais.

### Limite da recomendação

O candidato permanece `Under Validation`. A recomendação não reduz a importância estratégica das parcerias nem exige internalização; corrige sua classificação e preserva decisões de entrada, evolução e saída.

## 32. Resultado final da COEM

| Elemento | Resultado |
|---|---|
| candidatos avaliados | 18 de 18 |
| clusters avaliados | 6 de 6 |
| recomendações `Reformulate` | 9 |
| recomendações `Merge` | 3 |
| recomendações `Reject` | 6 |
| recomendações `Approve` | 0 |
| recomendações `Defer` | 0 |
| mudanças de estado | 0 |
| código canônico criado | 0 |

A ausência de recomendações `Approve` não invalida a matriz. Ela demonstra que o primeiro COR cumpriu a função de ampliar cobertura e expor sobreposições, enquanto a COEM corrigiu fronteiras entre Outcome, capacidade, experiência, princípio, guardrail e trajetória estratégica.

As dezoito disposições permanecem propostas arquiteturais. A conclusão da cobertura não autoriza decisão em lote, alteração do COR, estabilização do AQS-O01 ou consolidação canônica.

## 33. Gate do incremento

| Critério | Resultado |
|---|---|
| quatro testes obrigatórios aplicados | 18/18 — Pass |
| evidência externa rastreável | Pass |
| contradições e limites preservados | Pass |
| disposição singular por candidato | Pass |
| distinção entre recomendação e decisão | Pass |
| promoção automática bloqueada | Pass |
| candidatos avaliados | 18/18 — Complete |
| clusters avaliados | 6/6 — Complete |
| COEM concluída | Yes |
| AQS-O01 iniciado | No |
| Outcomes canônicos definidos | 0 |

## 34. Próximo passo governado

Submeter as dezoito disposições cumulativas à decisão humana individual e rastreável. Somente após esse ato poderão ser alterados os estados do COR e iniciado o ajuste prático do AQS-O01. Nenhuma recomendação deve ser executada por inferência, contagem de testes ou conclusão da cobertura, e nenhum código canônico `EO-###` ou `BO-###` deve ser criado antes da consolidação governada.
