---
id: BA-STR-002-COR-001
title: Candidate Outcome Register
status: active
version: 0.30.0
owner: Guivos Business Architecture
last_updated: 2026-07-26
parent: BA-STR-002
depends_on:
  - BA-FND-001
  - BA-STR-001
  - GKR-GOV-OUT-001
related:
  - BA-STR-002-EOVP-001
  - BA-STR-002-EOVB-001
  - BA-STR-002-EOVB-002
  - BA-STR-002-EOVB-003
  - BA-STR-002-EOVB-004
  - BA-STR-002-EOVB-005
  - BA-STR-002-EOVB-006
  - BA-STR-002-COEM-001
  - BA-STR-002-CODR-001
  - COD-003
  - COD-004
  - COD-005
  - COD-006
  - COD-007
  - COD-008
  - COD-009
  - COD-010
  - COD-011
  - COD-012
  - COD-013
  - COD-014
  - COD-015
  - COD-016
  - COD-017
  - COD-018
  - GEM-CLOSURE-REVIEW-001
  - M7.20
normative: false
---

# BA-STR-002-COR-001 — Candidate Outcome Register

## 1. Autoridade e finalidade

Este registro reúne as hipóteses de Ecosystem Outcomes e Business Outcomes do `BA-STR-002` antes de promoção à Canon.

O COR preserva origem, formulações, dúvidas, sobreposições, decisões e rastreabilidade sem transformar candidatos em resultados aprovados.

## 2. Estado formal

```text
Register: discovery, external validation, COEM coverage and human decisions complete
Candidates: 18
Ecosystem candidates: 8
Business candidates: 10
Approved Outcomes: 0
Canonical EO/BO codes: 0
Under Validation: 9
Merged: 3
Rejected: 6
External validation: completed — batches 01 to 06
COEM: completed — 18 of 18 candidates; 6 of 6 clusters
Human decisions: 18 of 18
AQS-O01 practical validation: not started
Operational authorization: no
```

## 3. Limites

Este registro não:

- cria códigos canônicos `EO-###` ou `BO-###`;
- comprova transformação, impacto, causalidade ou sustentabilidade;
- define capacidades, produtos, processos, KPIs, metas ou tecnologias;
- substitui pesquisa, validação de mercado ou evidência comportamental;
- conclui o `BA-STR-002`;
- retoma Product Engineering ou autoriza o W0-01.

Estados `Merged` e `Rejected` preservam candidatos, formulações, evidências e histórico.

## 4. Convenção

| Estado | Regra |
|---|---|
| `Under Validation` | candidato ativo aguardando nova avaliação ou consolidação posterior |
| `Merged` | candidato incorporado a outro por decisão humana, com rastreabilidade preservada |
| `Rejected` | candidato retirado do futuro catálogo de Outcomes, sem apagar conceito, evidências ou destino arquitetural |

## 5. Candidate Ecosystem Outcomes

### ECO-CAND-001 — Compreensão contextual suficiente

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | Pessoas, Organizações e Coletivos conseguem compreender seu Momento Atual, necessidades, objetivos, restrições e possibilidades com suficiência para decisões conscientes. |
| Formulação candidata vigente | Pessoas, Organizações e Coletivos formam e revisam uma compreensão contextual suficientemente fundamentada sobre sua situação, objetivos, necessidades, restrições e possibilidades, fortalecendo sua capacidade de realizar escolhas conscientes. |
| Origem | GEB-P01-F01; GEB-P01-F02; GEB-P01-F05; BA-STR-001 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Under Validation |
| Decisão | `COD-001 — Aceitar Reformulate` |
| Questão de validação | A compreensão contextual possui implicação estratégica independente suficiente ou deve permanecer condição sustentadora de agência? |

### ECO-CAND-002 — Acesso real a possibilidades legítimas e manejáveis

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | Participantes encontram possibilidades legítimas, compreensíveis e relevantes para seu contexto, seus objetivos e seu momento de vida. |
| Formulação candidata vigente | Pessoas, Organizações e Coletivos dispõem de acesso real a possibilidades legítimas, compreensíveis e manejáveis, compatíveis com seu contexto, objetivos, restrições e fatores de conversão, preservando liberdade substantiva para compará-las e escolhê-las sem que a abundância de opções seja tratada como evidência de valor. |
| Origem | GEB-P01-F01; GEB-P01-F02; GEB-P01-F04; GEB-P01-F06 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Under Validation |
| Decisão | `COD-004 — Aceitar Reformulate` |
| Questão de validação | A formulação revisada é observável por restrições e fatores de conversão sem transformar volume de opções em evidência de acesso ou valor? |

### ECO-CAND-003 — Agência efetiva e situada

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | Participantes preservam liberdade de escolha e capacidade de definir, revisar ou recusar seus próprios próximos passos de evolução. |
| Formulação candidata vigente | O ecossistema preserva condições reais, contextualmente adequadas e não coercitivas para que Pessoas, Organizações e Coletivos exerçam agência efetiva e situada ao definir, revisar, pausar, recusar, abandonar ou renovar seus próprios próximos passos diante de mudanças, aprendizados e limites legítimos, individualmente ou em relações de co-agência. |
| Origem | GEB-P01-F01; GEB-P01-F03; GEB-P01-F05; GEB-P01-F06; ECO-CAND-005 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Under Validation |
| Decisões | `COD-002 — Aceitar Reformulate`; `COD-003 — ECO-CAND-005 Merged into ECO-CAND-003` |
| Questão de validação | A formulação combinada é observável sem converter agência em engajamento, persistência ou conclusão de tarefas? |

### ECO-CAND-004 — Realização de experiências de valor

| Campo | Registro |
|---|---|
| Definição original preservada | Participantes conseguem converter oportunidades escolhidas em experiências vividas que produzem valor percebido e potencial de evolução. |
| Origem | GEB-P01-F01; GEB-P01-F06; BA-STR-001; GEM-001 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Rejected |
| Decisão | `COD-005 — Aceitar Reject` |
| Destino arquitetural preservado | arquitetura da Jornada, realização de valor em uso e fonte de evidências para Outcomes |
| Questão de validação | Resolvida quanto à candidatura autônoma. |

### ECO-CAND-005 — Continuidade da evolução autodeterminada

| Campo | Registro |
|---|---|
| Definição original preservada | Participantes mantêm condições para reconhecer mudanças, aprender e iniciar novos ciclos de evolução coerentes com suas próprias escolhas. |
| Origem | GEB-P01-F01; GEB-P01-F02; GEB-P01-F03; GEB-P01-F06 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Merged |
| Merged into | ECO-CAND-003 |
| Decisão | `COD-003 — Aceitar Merge into ECO-CAND-003` |
| Questão de validação | Resolvida quanto à independência; formulação combinada do alvo pendente de nova COEM. |

### ECO-CAND-006 — Saúde relacional no ecossistema

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | Participantes formam e preservam relações relevantes que ampliam cooperação, acesso a oportunidades e geração recíproca de valor. |
| Formulação candidata vigente | O ecossistema sustenta condições para que Pessoas, Organizações e Coletivos estabeleçam e preservem relações voluntárias, diversas e reciprocamente construtivas, capazes de ampliar cooperação, acesso e valor recíproco sem restringir autonomia, excluir terceiros ou produzir dano material. |
| Origem | GEB-P01-F01; GEB-P01-F04; GEB-P01-F06; GEM-001 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Under Validation |
| Decisão | `COD-006 — Aceitar Reformulate` |
| Questão de validação | A formulação revisada possui unidade, observabilidade e implicação estratégica próprias sem se sobrepor a acesso, proteção ou legitimidade institucional? |

### ECO-CAND-007 — Participação inclusiva, digna e efetiva

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | Participantes de diferentes culturas, crenças, países e contextos conseguem participar do ecossistema com dignidade, acolhimento e acesso a valor essencial. |
| Formulação candidata vigente | Pessoas, Organizações e Coletivos, em diferentes culturas, crenças, países e contextos, dispõem de condições reais para participar do ecossistema de forma digna e efetiva, com capacidade de uso, respeito, voz e contestabilidade, mediante redução de barreiras materiais evitáveis e preservação de requisitos legítimos de elegibilidade, segurança e conformidade. |
| Origem | GEB-P01-F02; GEB-P01-F04; GEB-P01-F05; GEM-001 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Under Validation |
| Decisão | `COD-007 — Aceitar Reformulate` |
| Questão de validação | A formulação revisada possui unidade e observabilidade próprias sem acumular direitos, guardrails constitucionais ou capacidades de acessibilidade como sub-Outcomes? |

### ECO-CAND-008 — Participação protegida, justa e contestável

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | Participantes interagem em condições de transparência, segurança, privacidade, justiça, contestabilidade e respeito à sua autonomia. |
| Formulação candidata vigente | Pessoas, Organizações e Coletivos participam do ecossistema em condições verificáveis de proteção, justiça e contestabilidade, com vulnerabilidades evitáveis reduzidas, possibilidade efetiva de compreender e questionar decisões, obter reparação diante de danos ou falhas e preservar sua autonomia, sem que conformidade, ausência de incidentes ou confiança declarada sejam tratadas como prova suficiente. |
| Origem | GEB-P01-F05; GEB-P01-F06; GEM-001; GEM-CLOSURE-REVIEW-001 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Under Validation |
| Decisão | `COD-008 — Aceitar Reformulate` |
| Questão de validação | A formulação revisada possui unidade e observabilidade próprias sem converter guardrails, controles ou confiança percebida em sub-Outcomes? |

## 6. Candidate Business Outcomes

### BUS-CAND-001 — Aderência permanente ao propósito

| Campo | Registro |
|---|---|
| Definição original preservada | A Guivos mantém decisões, investimentos, relações e evolução institucional coerentes com seu propósito e seus princípios permanentes. |
| Origem | BA-FND-001; BA-STR-001; GEB-P01-F03; GEB-P01-F05 |
| Participantes afetados | Ecossistema como um todo |
| Status | Rejected |
| Decisão | `COD-009 — Aceitar Reject` |
| Destino arquitetural preservado | princípio constitucional permanente; obrigação de governança e accountability; critério de admissibilidade; prevenção e correção de mission drift |
| Questão de validação | Resolvida quanto à candidatura autônoma. |

### BUS-CAND-002 — Relevância contínua das respostas

| Campo | Registro |
|---|---|
| Definição original preservada | As respostas organizadas pela Guivos permanecem relevantes diante da mudança de contextos, necessidades e prioridades dos participantes. |
| Origem | BA-FND-001; BA-STR-001; GEB-P01-F01; GEB-P01-F06 |
| Participantes afetados | Pessoa, Organização e Coletivo |
| Status | Merged |
| Merged into | BUS-CAND-003 |
| Decisão | `COD-010 — Aceitar Merge into BUS-CAND-003` |
| Questão de validação | Resolvida quanto à independência; formulação combinada do alvo pendente de nova COEM. |

### BUS-CAND-003 — Habilitação consistente e contextualmente relevante de valor legítimo

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | A Guivos entrega valor legítimo com qualidade, segurança e continuidade suficientes para sustentar experiências relevantes. |
| Formulação candidata vigente | A Guivos sustenta condições para habilitar valor legítimo com consistência e relevância contextual, detectando mudanças materiais e ajustando proposições, capacidades e respostas de forma coerente, sem presumir controle unilateral sobre o valor realizado pelos participantes nem tratar personalização, satisfação pontual, disponibilidade técnica ou velocidade de resposta como prova suficiente. |
| Origem | BA-STR-001; GEM-001; GEM-008; GEM-CLOSURE-REVIEW-001; BUS-CAND-002 |
| Participantes afetados | Pessoa, Organização, Coletivo e parceiros |
| Status | Under Validation |
| Decisões relacionadas | `COD-010 — BUS-CAND-002 Merged into BUS-CAND-003`; `COD-011 — Aceitar Reformulate` |
| Questão de validação | A formulação revisada possui unidade, observabilidade e implicação estratégica próprias sem acumular propriedades de entrega, capacidades e valor realizado por terceiros como sub-Outcomes? |

### BUS-CAND-004 — Legitimidade institucional sustentada

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | A Guivos preserva confiança e legitimidade suficientes para manter relações voluntárias, transparentes e duradouras no ecossistema. |
| Formulação candidata vigente | A legitimidade institucional da Guivos é sustentada perante participantes e stakeholders por conduta coerente, governança responsável, transparência, contestabilidade e reparação verificáveis, sem presumir controle unilateral sobre avaliações socialmente conferidas nem tratar reputação, conformidade, satisfação, confiança declarada ou longevidade das relações como prova suficiente. |
| Origem | GEB-P01-F05; GEB-P01-F06; GEM-001; GEM-CLOSURE-REVIEW-001 |
| Participantes afetados | Pessoa, Organização, Coletivo e parceiros |
| Status | Under Validation |
| Decisão | `COD-012 — Aceitar Reformulate` |
| Confiança institucional | preservada como avaliação relacional associada; nenhum novo candidato criado |
| Observações | Conduta, governança, controles, transparência, contestabilidade e reparação permanecem meios ou propriedades sustentadoras, não sub-Outcomes. |
| Questão de validação | A formulação revisada possui unidade, observabilidade e implicação estratégica próprias sem converter meios de governança ou avaliações socialmente conferidas em prova automática de legitimidade? |

### BUS-CAND-005 — Continuidade econômica sustentável

| Campo | Registro |
|---|---|
| Definição originalmente avaliada | A Guivos mantém recursos, capacidade e equilíbrio econômico suficientes para cumprir obrigações e preservar o valor essencial ao longo do tempo. |
| Formulação candidata vigente | A Guivos sustenta condições econômicas suficientes para cumprir obrigações e preservar valor essencial em múltiplos horizontes, mantendo opções legítimas de financiamento, alocação e renovação sem presumir permanência absoluta nem tratar receita, margem, caixa, disponibilidade operacional ou crescimento isolados como prova suficiente. |
| Origem | BA-STR-001; GEM-001; GEM-008; GEM-CLOSURE-REVIEW-001; BUS-CAND-010 |
| Participantes afetados | Ecossistema como um todo |
| Status | Under Validation |
| Decisões relacionadas | `COD-013 — Aceitar Reformulate`; `COD-018 — BUS-CAND-010 Merged into BUS-CAND-005` |
| Conteúdo incorporado de BUS-CAND-010 | financiamento responsável da renovação; adicionalidade; riscos; obrigações protegidas; custo de oportunidade; alternativas legítimas de uso ou financiamento; avaliação anterior e posterior da alocação |
| Observações | Continuidade operacional, resiliência, equilíbrio financeiro, reservas, financiamento, alocação e renovação permanecem dimensões ou capacidades sustentadoras, não sub-Outcomes. Reinvestimento proposto, aprovado, realizado e eficaz são estados distintos. |
| Questão de validação | A formulação combinada possui unidade, observabilidade e implicação estratégica próprias sem depender de métrica financeira única, disponibilidade operacional, promessa de permanência absoluta ou reinvestimento automático? |

### BUS-CAND-006 — Crescimento responsável e resiliente

| Campo | Registro |
|---|---|
| Definição original preservada | A Guivos amplia alcance e valor sem degradar qualidade, proteção, capacidade, diversidade de dependências ou continuidade. |
| Origem | GEB-P01-F04; BA-STR-001; GEM-008; GEM-CLOSURE-REVIEW-001 |
| Participantes afetados | Ecossistema como um todo |
| Status | Rejected |
| Decisão | `COD-014 — Aceitar Reject` |
| Destino arquitetural preservado | expansão responsável como trajetória estratégica opcional; capacidade demonstrada, adicionalidade e critérios de não degradação como gates; resiliência e adaptação legítima como propriedades de continuidade ou capacidades sustentadoras |
| Observações | A rejeição não proíbe crescimento e não trata ausência de expansão como falha automática. |
| Questão de validação | Resolvida quanto à candidatura autônoma. |

### BUS-CAND-007 — Aprendizado e adaptação institucionais

| Campo | Registro |
|---|---|
| Definição original preservada | A Guivos transforma evidências, conhecimento e resultados observados em decisões que preservam coerência e melhoram continuamente sua geração de valor. |
| Origem | GEB-P01-F05; GEB-P01-F06; BA-STR-001; GEM-CLOSURE-REVIEW-001 |
| Participantes afetados | Ecossistema como um todo |
| Status | Rejected |
| Decisão | `COD-015 — Aceitar Reject` |
| Destino arquitetural preservado | aprendizado institucional como capacidade sustentadora multinível; sensing, interpretação, absorção, memória, contestação, renovação e adaptação como dimensões governadas |
| Evidência insuficiente | coleta de dados, analytics, IA, reuniões ou retrospectivas não comprovam aprendizagem institucional |
| Observações | A rejeição não reduz a importância de aprender e não remove aprendizagem ou adaptação da arquitetura. |
| Questão de validação | Resolvida quanto à candidatura autônoma. |

### BUS-CAND-008 — Saúde das relações de parceria

| Campo | Registro |
|---|---|
| Definição original preservada | A rede de parceiros permanece qualificada, alinhada, diversa e capaz de gerar valor recíproco sem transferir indevidamente autoridade ou risco. |
| Origem | GEB-P01-F06; GEM-001; GEM-CLOSURE-REVIEW-001 |
| Participantes afetados | Organizações, Coletivos, parceiros e participantes atendidos |
| Status | Rejected |
| Decisão | `COD-016 — Aceitar Reject` |
| Destino arquitetural preservado | governança das relações de parceria, gestão de alianças, dependências externas, confiança, controles, riscos relacionais e de desempenho e critérios de portfólio na futura arquitetura de capacidades |
| Evidência insuficiente | quantidade de parceiros, duração contratual ou ausência de conflito não comprovam saúde relacional |
| Observações | A rejeição não reduz a importância estratégica das parcerias e não exige internalização; entrada, evolução, renovação, substituição e saída permanecem decisões legítimas e governadas. |
| Questão de validação | Resolvida quanto à candidatura autônoma. |

### BUS-CAND-009 — Coerência global com adequação contextual

| Campo | Registro |
|---|---|
| Definição original preservada | A Guivos preserva identidade e coerência arquitetural enquanto se adapta legitimamente a países, culturas, idiomas e contextos distintos. |
| Origem | GEB-P01-F02; GEB-P01-F04; GEB-P01-F06; BA-FND-001 |
| Participantes afetados | Pessoa, Organização e Coletivo em diferentes contextos |
| Status | Rejected |
| Decisão | `COD-017 — Aceitar Reject` |
| Destino arquitetural preservado | coerência global com adequação contextual como princípio arquitetural e critério governado para internacionalização, localização, desenho de capacidades e avaliação de mudanças |
| Evidência insuficiente | tradução, presença local ou variação nominal de produto não comprovam adequação legítima |
| Observações | A rejeição não impõe padronização global, não proíbe adaptação local e não exige internacionalização; padronização, adaptação, integração e autonomia local permanecem decisões governadas conforme contexto e autoridade. |
| Questão de validação | Resolvida quanto à candidatura autônoma. |

### BUS-CAND-010 — Capacidade de reinvestimento responsável

| Campo | Registro |
|---|---|
| Definição original preservada | A Guivos mantém condições para reinvestir valor legitimamente capturado no fortalecimento de capacidades, conhecimento e valor entregue ao ecossistema. |
| Origem | BA-FND-001; BA-STR-001; GEM-001; GEM-008 |
| Participantes afetados | Ecossistema como um todo |
| Status | Merged |
| Merged into | BUS-CAND-005 |
| Decisão | `COD-018 — Aceitar Merge into BUS-CAND-005` |
| Conteúdo preservado | capacidade governada de financiar renovação e preservar opções de investimento; adicionalidade, riscos, obrigações, alternativas e avaliação de eficácia |
| Evidência insuficiente | maior retenção, gasto ou percentual reinvestido não comprova responsabilidade, eficácia, continuidade ou geração futura de valor |
| Questão de validação | Resolvida quanto à independência; formulação combinada do alvo pendente de nova COEM. |

## 7. Sobreposições e decisões

| Cluster | Candidatos | Estado |
|---|---|---|
| agência e evolução | ECO-CAND-001, 003 e 005 | ECO-CAND-005 fundido em ECO-CAND-003; formulações restantes exigem nova COEM |
| oportunidade e experiência | ECO-CAND-002 e 004 | ECO-CAND-004 rejeitado; experiência preservada na Jornada |
| confiança | ECO-CAND-006, ECO-CAND-008 e BUS-CAND-004 | três camadas preservadas; BUS-CAND-004 reformulado como legitimidade institucional sustentada |
| inclusão | ECO-CAND-007, ECO-CAND-002 e ECO-CAND-008 | formulações revisadas exigem nova COEM |
| propósito | BUS-CAND-001 | rejeitado como Outcome por `COD-009`; autoridade constitucional preservada |
| valor e continuidade | BUS-CAND-003, BUS-CAND-005 e BUS-CAND-010 | BUS-CAND-003 e BUS-CAND-005 reformulados; BUS-CAND-010 fundido em BUS-CAND-005 por `COD-018`; formulações ativas exigem nova COEM |
| adaptação | BUS-CAND-002, BUS-CAND-007 e BUS-CAND-009 | BUS-CAND-002 fundido em BUS-CAND-003; BUS-CAND-007 rejeitado e preservado como capacidade; BUS-CAND-009 rejeitado e preservado como princípio arquitetural e critério governado |
| resiliência | BUS-CAND-005 e BUS-CAND-006 | BUS-CAND-005 preservado como candidato reformulado; BUS-CAND-006 rejeitado e expansão responsável preservada como trajetória opcional |
| parcerias | BUS-CAND-008 | rejeitado como Outcome; governança de parceiros, gestão de alianças e critérios de portfólio preservados como capacidades e decisões governadas |

## 8. Pendências para os próximos ciclos

Antes de qualquer promoção canônica deverão existir:

1. reaplicação dos quatro testes às formulações revisadas e combinadas;
2. aplicação e ajuste do AQS-O01;
3. decisão formal sobre catálogos e códigos canônicos;
4. matriz de sustentação entre Ecosystem Outcomes e Business Outcomes;
5. clareza suficiente para iniciar a arquitetura de Capacidades Empresariais.

## 9. Gate do incremento

| Critério | Resultado |
|---|---|
| `COD-018` registrado | Pass |
| formulação original e evidências preservadas | Pass |
| `BUS-CAND-010` alterado para `Merged` | Pass |
| alvo `BUS-CAND-005` identificado | Pass |
| alvo mantido em `Under Validation` | Pass |
| reinvestimento automático bloqueado | Pass |
| alternativas internas e externas preservadas | Pass |
| distribuição 9/3/6 registrada | Pass |
| decisões humanas 18/18 registradas | Pass |
| promoção automática bloqueada | Pass |
| Outcomes canônicos definidos | Not started |

## 10. Próximo passo governado

Após integração deste incremento e nova autorização, reaplicar os quatro testes às formulações revisadas e combinadas, ajustar o AQS-O01 e preparar a futura consolidação governada dos catálogos.