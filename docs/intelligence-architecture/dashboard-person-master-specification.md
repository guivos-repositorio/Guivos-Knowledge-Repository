---
id: GKR-INTELLIGENCE-DASHBOARD-PERSON-001
title: Dashboard Pessoa — Documento Mestre de Especificação Analítica e Handoff Replit
status: active
version: 0.1.2
owner: Guivos Intelligence Architecture
last_updated: 2026-09-13
normative: false
maturity: governed_pre_implementation_dashboard_master
depends_on:
  - GKR-INTELLIGENCE-DASHBOARD-KPI-001
  - GKR-JOURNEY-PERSON-001
  - GKR-UX-D5-A-001
  - GKR-UX-D5-C1-001
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GAI-001
  - GAI-002
  - GIA-COG-001
related:
  - UXA-097
  - UXA-098
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - UXA-100-A4
---

# Dashboard Pessoa — Documento Mestre de Especificação Analítica e Handoff Replit

## 1. Finalidade

Este documento é o **Anexo E** de `GKR-INTELLIGENCE-DASHBOARD-KPI-001` e governa, em nível documental pré-implementação, o **Dashboard Pessoa**.

Seu objetivo é consolidar, antes de qualquer implementação, o recorte analítico legítimo pelo qual uma Pessoa pode compreender **seus próprios dados autorizados, sua Journey, seus históricos, contextos, objetivos, movimentos, trajetórias, participações, relações, eventos e outputs autorizados de Analytics, Graph e Guivos Intelligence**.

O Dashboard Pessoa deve apoiar compreensão individual sem converter a Pessoa em score, perfil determinístico, diagnóstico, ranking, produto comercial ou objeto de decisão automatizada.

Regra central:

> **A Pessoa pode compreender e revisar sua própria trajetória e os outputs legitimamente produzidos sobre ela ou para ela; o dashboard não recebe autoridade para definir quem a Pessoa é, qual deve ser sua prioridade, se houve evolução, qual decisão deve tomar ou qual significado pessoal deve aceitar.**

Este master não redefine a experiência autenticada principal da Pessoa, não substitui `Hoje`, `Meus Objetivos`, `Meus Próximos Passos` ou `Minha Evolução`, não cria menu, Surface Map, State Map, wireframe, RBAC técnico ou implementação.

```text
DASHBOARD PESSOA
≠ HOJE
≠ MEUS OBJETIVOS
≠ MEUS PRÓXIMOS PASSOS
≠ MINHA EVOLUÇÃO
≠ JOURNEY DA PESSOA
≠ GRAPH
≠ GUIVOS INTELLIGENCE
≠ DIAGNÓSTICO
≠ DECISÃO AUTOMATIZADA
```

---

## 2. Autoridades de domínio e precedência

| Autoridade | Papel neste master |
|---|---|
| `GKR-INTELLIGENCE-DASHBOARD-KPI-001` | envelope transversal de KPI, acesso, disclosure e handoff |
| `GKR-JOURNEY-PERSON-001` | continuidade integrada da Journey da Pessoa e limites das superfícies existentes |
| `GKR-UX-D5-A-001` | materialização controlada dos Domínios de Evolução, confirmação, revisabilidade e sensibilidade |
| `GKR-UX-D5-C1-001` | responsabilidades próprias de `Meus Objetivos`, `Meus Próximos Passos` e `Minha Evolução` |
| `PAS-001-DOMAIN-MODEL-001` | semântica canônica dos Domínios de Evolução |
| `PAS-001-DOMAIN-RECON-001` | reconciliação entre Domínio, Contexto Vivo e aspectos descritivos |
| `GAI-001 / GAI-002 / GIA-COG-001` | evidência, natureza de afirmações, autonomia humana, explicabilidade, proveniência e `COMPREENDER ≠ DECIDIR` |
| `UXA-097 / UXA-098` | compreensão inicial, Hoje, descoberta de oportunidades e saída consciente |
| `UXA-100 / A1 / A2 / A3 / A4` | fluxo especializado de Planos da Pessoa |

Em caso de conflito, este master preserva a autoridade especializada mais restritiva e mantém a métrica ou leitura bloqueada até adjudicação própria.

Para intenção, preferência, objetivo e significado pessoal, aplica-se a precedência governada pela arquitetura cognitiva:

```text
DECLARAÇÃO LEGÍTIMA E VIGENTE DA PESSOA
> INFERÊNCIA INCOMPATÍVEL
```

Essa precedência não reescreve evento operacional validado, mas impede que uma inferência substitua silenciosamente o significado pessoal declarado.

---

## 3. Estado e boundary

```text
GKR-INTELLIGENCE-DASHBOARD-PERSON-001
→ ACTIVE v0.1.2
→ PRE-IMPLEMENTATION DASHBOARD MASTER

PESSOA
→ PARTICIPANT TYPE
→ SUJEITO PRIMÁRIO DE SUA PRÓPRIA JOURNEY

DASHBOARD PESSOA
→ ANALYTICAL CONSUMPTION SURFACE
→ NOT SOURCE OF TRUTH
→ NOT AUTHENTICATED HOME / TODAY SURFACE
→ NOT OPERATIONAL SYSTEM OF RECORD
→ NOT A HUMAN EVALUATION ENGINE

REAL DATA CONNECTION
→ NOT AUTHORIZED BY THIS DOCUMENT

REPLIT BUILD
→ NOT AUTHORIZED BY THIS DOCUMENT
→ HANDOFF SPECIFICATION ONLY

PROCESSING AUTHORIZED
≠ DISCLOSURE AUTHORIZED

SELF-SERVICE ANALYTICS
≠ UNRESTRICTED ACCESS TO EVERY DATASET KNOWN BY GUIVOS
```

O fato de a Pessoa ser o sujeito da leitura não transforma dados de terceiros, Organizações, Coletivos ou relações bilaterais em informação automaticamente exibível.

---

## 4. Relação com a experiência autenticada da Pessoa

A Journey vigente distingue responsabilidades especializadas:

```text
PER-008 — Hoje
→ síntese recorrente

PER-010 — Meus Objetivos
→ direção e controle de objetivos

PER-011 — Meus Próximos Passos
→ movimentos contextuais e seu controle

PER-012 — Minha Evolução
→ trajetórias, mudanças, continuidades, evidências e interpretações
```

O Dashboard Pessoa não substitui nenhuma dessas responsabilidades.

```text
HOJE
→ SINTETIZA O MOMENTO E CONTINUIDADES RELEVANTES

MEUS OBJETIVOS
→ GOVERNA OBJETIVOS

MEUS PRÓXIMOS PASSOS
→ GOVERNA MOVIMENTOS CONTEXTUAIS

MINHA EVOLUÇÃO
→ GOVERNA TRAJETÓRIAS E INTERPRETAÇÕES

DASHBOARD PESSOA
→ PODE APOIAR COM LEITURAS ANALÍTICAS AUTORIZADAS
→ NÃO REDEFINE AS RESPONSABILIDADES ACIMA
```

A existência deste master não cria nova Home autenticada, não transforma `Hoje` em dashboard e não promove novas superfícies ou transições.

---

## 5. Áreas analíticas candidatas

O Dashboard Pessoa é organizado em **nove áreas analíticas**:

1. Visão Analítica Pessoal;
2. Contexto e Domínios da Journey;
3. Objetivos e Direções;
4. Próximos Passos e Movimento;
5. Evolução e Trajetórias;
6. Participações, Relações e Experiências;
7. Intelligence, Graph e Explicabilidade;
8. Planos e Capacidade;
9. Qualidade, Freshness, Privacidade e Governança do Dado.

A área de **Visão Analítica Pessoal** compõe leituras das famílias governadas neste master. Ela não constitui família KPI autônoma.

Históricos e eventos são tratados como **dimensão temporal transversal** e não criam família KPI própria nesta versão.

```text
ÁREA DOCUMENTADA
≠ KPI DEFINIDO
≠ DADO DISPONÍVEL
≠ AFIRMAÇÃO VERDADEIRA
≠ RECOMENDAÇÃO OBRIGATÓRIA
≠ IMPLEMENTAÇÃO AUTORIZADA
```

---

## 6. Classes funcionais de consumo

As classes abaixo são conceituais e não constituem RBAC técnico implementado:

| Classe funcional | Escopo candidato |
|---|---|
| Pessoa — visão própria | leituras dos próprios dados, Journey, históricos e outputs autorizados |
| Pessoa — revisão e controle | contestação, revisão, confirmação, retirada ou correção quando a autoridade permitir |
| Pessoa — exportação própria | exportações do próprio recorte quando finalidade, segurança e contrato permitirem |
| Guivos — suporte | dados estritamente necessários à finalidade legítima de suporte |
| Guivos — Intelligence/Data | inputs e outputs necessários à finalidade analítica autorizada |
| Service account / Replit | somente payloads necessários à renderização autorizada |

```text
SER A PRÓPRIA PESSOA
≠ ACESSO AUTOMÁTICO A DADOS PRIVADOS DE TERCEIROS

DADO SOBRE UMA RELAÇÃO
≠ DADO EXCLUSIVAMENTE DA PESSOA

OUTPUT SOBRE A PESSOA
≠ DIREITO AUTOMÁTICO DE COMPARTILHAMENTO COM TERCEIROS

PROCESSAMENTO INTERNO AUTORIZADO
≠ DISCLOSURE IRRESTRITO
```

Organização, Coletivo, Business ou anunciante não herdam acesso a este dashboard ou a seus detalhes por possuírem relação com a Pessoa.

---

## 7. Vocabulário de KPI e readiness

Prefixo deste master:

```text
PER-KPI-<FAMÍLIA>-NNN
```

Famílias iniciais:

- `CTX` — contexto e Domínios da Journey;
- `OBJ` — objetivos e direções;
- `MOV` — Próximos Passos e movimento;
- `EVO` — evolução e trajetórias;
- `REL` — participações, relações e experiências;
- `INT` — outputs autorizados de Intelligence, Graph e Analytics;
- `CAP` — planos e capacidade;
- `DQ` — qualidade, freshness, privacidade e governança.

A **Visão Analítica Pessoal** compõe indicadores dessas famílias e não cria namespace próprio nesta versão.

Estados usados:

| Status | Significado |
|---|---|
| `proposed` | significado ou contrato ainda incompleto; não build-ready |
| `source_pending` | semântica fechada o suficiente, mas source/data contract ainda bloqueia readiness |
| `defined` | contrato documental mínimo completo; ainda requer gates de domínio e build |
| `approved-equivalent` | autoridade especializada fornece estado equivalente aceito pelo gate |

Nesta versão, **todos os KPIs candidatos permanecem `proposed / NOT_READY`**.

---

## 8. Proibição de score humano global

Nenhuma família deste master pode ser combinada por conveniência para fabricar um valor global da Pessoa.

```text
PESSOA
≠ SCORE
≠ RANKING
≠ PERCENTUAL GLOBAL DE EVOLUÇÃO
≠ ÍNDICE UNIVERSAL DE SUCESSO
≠ DIAGNÓSTICO
≠ PERFIL DETERMINÍSTICO
≠ AVALIAÇÃO ESPIRITUAL
≠ PERFIL COMERCIAL DE VULNERABILIDADE
```

Também permanecem inválidas as equivalências:

```text
MAIS OBJETIVOS CONCLUÍDOS
≠ MAIOR VALOR HUMANO

MAIS PRÓXIMOS PASSOS EXECUTADOS
≠ MAIOR EVOLUÇÃO

MAIS PARTICIPAÇÃO
≠ MELHOR TRAJETÓRIA

MAIS OUTPUTS DE INTELLIGENCE
≠ MELHOR COMPREENSÃO

MAIS DOMÍNIOS ATIVOS
≠ VIDA MAIS COMPLETA
```

Qualquer futura pontuação especializada exigirá autoridade própria, finalidade legítima, fórmula, validação, riscos, contestação, explicabilidade e limitação de claims. Este documento não autoriza nenhuma.

---

## 9. Família CTX — Contexto e Domínios da Journey

Esta família mede somente aspectos que possam apoiar a Pessoa a compreender o contexto autorizado de sua própria Journey.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| PER-KPI-CTX-001 | Domínios confirmados vigentes | `domain_link` legitimamente confirmados e vigentes para os objetos autorizados | vínculos | proposed | domain semantics + confirmation + source |
| PER-KPI-CTX-002 | Domínios candidatos em revisão | sugestões de domínio ainda não confirmadas pela Pessoa | vínculos | proposed | candidate-state + purpose + source |
| PER-KPI-CTX-003 | Revisões de domínio no período | eventos legítimos de confirmação, rejeição, adição, retirada ou revisão | eventos/período | proposed | lifecycle + temporal contract |
| PER-KPI-CTX-004 | Contextos sem classificação de domínio | objetos legitimamente mantidos sem `domain_link` confirmado | objetos | proposed | population + no-classification state |
| PER-KPI-CTX-005 | Distribuição própria por domínio | distribuição de objetos autorizados da própria Journey por domínio confirmado | distribuição | proposed | denominator + sensitivity + purpose |

Regras:

```text
DOMÍNIO CANDIDATO
≠ DOMÍNIO CONFIRMADO

DOMÍNIO CONFIRMADO
≠ IDENTIDADE
≠ DIAGNÓSTICO
≠ PRIORIDADE
≠ OBJETIVO
≠ EVOLUÇÃO
≠ RELEVÂNCIA AUTOMÁTICA

SEM DOMÍNIO CONFIRMADO
→ ESTADO LEGÍTIMO
```

A quantidade de domínios não possui direcionalidade de valor.

Saúde, espiritualidade, finanças e outros contextos sensíveis exigem finalidade, minimização e proteção próprias mesmo quando a própria Pessoa é o consumidor.

---

## 10. Família OBJ — Objetivos e Direções

Esta família não redefine `PER-010 — Meus Objetivos` e não cria objetivo pela observação analítica.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| PER-KPI-OBJ-001 | Objetivos válidos | objetivos próprios em estados semanticamente válidos | objetivos | proposed | objective lifecycle + source |
| PER-KPI-OBJ-002 | Objetivos ativos | objetivos em estado ativo válido na janela | objetivos | proposed | active-state contract |
| PER-KPI-OBJ-003 | Objetivos em revisão/pausa | objetivos legitimamente em revisão ou pausa | objetivos | proposed | review/pause semantics |
| PER-KPI-OBJ-004 | Encerramentos no período | eventos de conclusão, retirada ou outro encerramento legitimamente diferenciado | eventos/período | proposed | closure taxonomy + temporal contract |
| PER-KPI-OBJ-005 | Objetivos com critérios explicitados | objetivos com critérios de sucesso legitimamente registrados | objetivos | proposed | criteria semantics + source |
| PER-KPI-OBJ-006 | Objetivos com evidências associadas | objetivos com evidências válidas associadas ao recorte autorizado | objetivos | proposed | evidence contract + source |

```text
OBJETIVO ATIVO
≠ PRIORIDADE AUTOMÁTICA

OBJETIVO CONCLUÍDO
≠ PROVA DE EVOLUÇÃO GLOBAL

OBJETIVO RETIRADO
≠ FALHA

PRIORIDADE DECLARADA
≠ VALOR HUMANO
≠ OBRIGAÇÃO
≠ URGÊNCIA AUTOMÁTICA
```

Este master não cria percentual automático de progresso.

---

## 11. Família MOV — Próximos Passos e Movimento

Esta família não substitui `PER-011 — Meus Próximos Passos` e não transforma sugestão em decisão.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| PER-KPI-MOV-001 | Próximos Passos válidos | movimentos próprios em estados semanticamente válidos | passos | proposed | next-step lifecycle + source |
| PER-KPI-MOV-002 | Próximos Passos prontos | passos em estado `PRONTO` ou equivalente governado | passos | proposed | readiness semantics |
| PER-KPI-MOV-003 | Propostas em revisão | propostas ainda não aceitas/confirmadas pela Pessoa | propostas | proposed | proposal-state + source |
| PER-KPI-MOV-004 | Passos bloqueados ou pausados | movimentos legitimamente bloqueados ou pausados | passos | proposed | blocked/pause semantics |
| PER-KPI-MOV-005 | Eventos de conclusão no período | conclusões operacionais válidas no período | eventos/período | proposed | completion event + temporal contract |
| PER-KPI-MOV-006 | Dependências abertas | dependências materialmente abertas segundo contrato aplicável | dependências | proposed | dependency semantics + source |

```text
PROPOSTO
≠ ACEITO
≠ DECIDIDO

PRONTO
≠ OBRIGATÓRIO
≠ URGENTE

CONCLUÍDO
≠ EVOLUÇÃO COMPROVADA

BLOQUEADO / PAUSADO
≠ FALHA
```

Períodos sem Próximos Passos ativos permanecem legítimos.

---

## 12. Família EVO — Evolução e Trajetórias

Esta família deve preservar integralmente o limite de `PER-012 — Minha Evolução`.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| PER-KPI-EVO-001 | Trajetórias em acompanhamento | trajetórias próprias legitimamente abertas para acompanhamento | trajetórias | proposed | trajectory semantics + source |
| PER-KPI-EVO-002 | Leituras de trajetória por estado | distribuição por estados legitimamente definidos, como estabilidade, manutenção, oscilação, recuperação ou reorientação quando aplicáveis | distribuição | proposed | state taxonomy + evidence |
| PER-KPI-EVO-003 | Trajetórias com baseline definido | trajetórias cujo baseline está explicitamente definido e válido | trajetórias | proposed | baseline contract |
| PER-KPI-EVO-004 | Leituras com evidência suficiente | interpretações de trajetória que atendem ao contrato de evidência aplicável | leituras | proposed | evidence sufficiency |
| PER-KPI-EVO-005 | Leituras contestadas/em revisão | interpretações legitimamente contestadas ou em revisão | leituras | proposed | contestation/review lifecycle |
| PER-KPI-EVO-006 | Revisões/correções no período | eventos válidos de revisão, correção ou substituição de interpretação | eventos/período | proposed | provenance + temporal contract |

```text
TRAJETÓRIA
≠ SCORE

MUDANÇA
≠ MELHORA

ESTABILIDADE
≠ AUSÊNCIA DE VALOR

REGRESSÃO, QUANDO LEGITIMAMENTE DEFINIDA
≠ FALHA HUMANA

CORRELAÇÃO
≠ CAUSALIDADE
```

Ausência de mudança ou de evolução reconhecida permanece estado legítimo.

Qualquer interpretação inferida deve permanecer distinguível de fato confirmado e carregar confiança, incerteza, evidência, limitações e possibilidade de contestação quando material.

---

## 13. Família REL — Participações, relações e experiências

Esta família organiza somente relações e eventos legitimamente pertencentes ao recorte autorizado da própria Pessoa.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| PER-KPI-REL-001 | Relações próprias ativas | relações legitimamente vinculadas à Pessoa e em estado ativo válido | relações | proposed | relationship semantics + source |
| PER-KPI-REL-002 | Participações válidas | participações próprias legitimamente registradas | participações | proposed | participation taxonomy + source |
| PER-KPI-REL-003 | Experiências registradas | experiências próprias com registro válido para a finalidade autorizada | experiências | proposed | experience semantics + source |
| PER-KPI-REL-004 | Eventos de entrada, pausa ou saída | eventos de relação/participação legitimamente diferenciados | eventos/período | proposed | lifecycle + temporal contract |
| PER-KPI-REL-005 | Relações por classe autorizada | distribuição própria por classes sem revelar dados privados de contrapartes | distribuição | proposed | taxonomy + disclosure |
| PER-KPI-REL-006 | Resultados externos confirmados | resultados externos somente quando houver confirmação e source legitimamente autorizado | resultados | proposed | external authority + confirmation + source |

```text
ABRIR DETALHE DE OPORTUNIDADE
≠ INTERESSE
≠ INSCRIÇÃO
≠ PARTICIPAÇÃO
≠ EVOLUÇÃO

SAIR PARA AUTORIDADE EXTERNA
≠ RESULTADO EXTERNO CONFIRMADO

PARTICIPAÇÃO
≠ OBRIGAÇÃO PERMANENTE

PAUSA / SAÍDA
≠ FALHA
```

Uma relação pode conter informações de terceiros. O Dashboard Pessoa não pode converter automaticamente o registro relacional em acesso a conteúdo privado da contraparte.

---

## 14. Família INT — Intelligence, Graph e Analytics

Esta família cobre somente outputs autorizados para consumo pela própria Pessoa.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| PER-KPI-INT-001 | Outputs de Intelligence disponíveis | outputs autorizados, vigentes e servíveis à Pessoa no recorte | outputs | proposed | serving/disclosure eligibility + source |
| PER-KPI-INT-002 | Outputs por natureza | distribuição por natureza governada, como explicação, insight, possibilidade, recomendação ou alerta | distribuição | proposed | output taxonomy + source |
| PER-KPI-INT-003 | Outputs por natureza do input/resultado | distribuição segundo a natureza preservada dos inputs/resultados, sem convertê-la em estado epistemológico/derivacional | distribuição | proposed | input/result nature taxonomy + provenance |
| PER-KPI-INT-004 | Outputs com confiança/incerteza qualificada | outputs materiais com confiança, incerteza e limitações devidamente qualificadas | outputs | proposed | assurance contract |
| PER-KPI-INT-005 | Outputs contestados/em revisão | outputs sob contestação, revisão ou confirmação necessária | outputs | proposed | contestation lifecycle |
| PER-KPI-INT-006 | Outputs superados/expirados | outputs que perderam vigência ou foram substituídos segundo regra governada | outputs | proposed | validity/expiry contract |

Os três eixos permanecem separados e não podem ser colapsados por visualização, filtro ou implementação:

```text
NATUREZA DO INPUT / RESULTADO
→ DECLARADO
→ OBSERVADO
→ OPERACIONAL
→ CALCULADO
→ INFERIDO
→ PREDITO
→ AGREGADO
→ CONHECIMENTO EXTERNO
→ CONHECIMENTO GOVERNADO

ESTADO EPISTEMOLÓGICO / DERIVACIONAL
→ VALIDADO
→ HIPÓTESE
→ CONTESTADO
→ INCERTO
→ SUPERADO
→ EXPIRADO

NATUREZA DO OUTPUT
→ EXPLICAÇÃO
→ INSIGHT
→ POSSIBILIDADE
→ RECOMENDAÇÃO
→ ALERTA
```

`CONHECIMENTO EXTERNO` e `CONHECIMENTO GOVERNADO` permanecem naturezas distintas de input/resultado porque possuem proveniências distintas; nenhum deles é sinônimo de dado pessoal observado.

`PER-KPI-INT-002` organiza natureza do output. `PER-KPI-INT-003` organiza natureza do input/resultado. O estado epistemológico/derivacional permanece campo separado, preservado nos contratos e metadados aplicáveis; este master não o converte em sinônimo de nenhum dos outros dois eixos.

E também:

```text
INFERÊNCIA
≠ FATO

RECOMENDAÇÃO
≠ DECISÃO

POSSIBILIDADE
≠ PREVISÃO GARANTIDA

PREDIÇÃO
≠ DESTINO

GRAPH RELATIONSHIP
≠ CAUSALIDADE

MAIOR QUANTIDADE DE SINAIS
≠ MAIOR VERDADE
```

`Graph`, `Analytics` e `Intelligence` podem contribuir para compreensão, mas nenhum deles recebe autoridade para substituir uma declaração legítima da Pessoa sobre intenção, preferência, objetivo ou significado pessoal.

---

## 15. Família CAP — Planos e capacidade

Planos são uma etapa transversal da Journey, mas não alteram autoridade, relevância ou valor da Pessoa.

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| PER-KPI-CAP-001 | Plano vigente | classificação do plano vigente quando contratualmente confirmada | categoria | proposed | plan source + entitlement contract |
| PER-KPI-CAP-002 | Uso de capacidade | uso de capacidade definida pelo plano no ciclo aplicável | unidade/% | proposed | entitlement + cycle + source |
| PER-KPI-CAP-003 | Capacidade disponível | capacidade ainda disponível conforme contrato de plano | unidade/% | proposed | entitlement + balance semantics |
| PER-KPI-CAP-004 | Eventos de alteração de plano | upgrades, downgrades, cancelamentos ou outros eventos confirmados no período | eventos | proposed | plan lifecycle + source |

```text
PLANO PAGO
≠ RELEVÂNCIA
≠ CONFIANÇA
≠ PRIORIDADE
≠ AUTORIDADE
≠ GARANTIA DE EVOLUÇÃO
≠ CONSENTIMENTO AMPLIADO
```

Preço, entitlement, quota ou benefício não congelado não pode ser inventado pelo dashboard.

`NOT_ENTITLED` pode descrever indisponibilidade de uma capacidade comercial, mas nunca deve ser utilizado para negar silenciosamente direitos de privacidade, revisão, correção ou acesso que pertençam à Pessoa por autoridade superior aplicável.

---

## 16. Família DQ — qualidade, freshness, privacidade e governança

| ID | Indicador candidato | Definição candidata | Unidade | Status | Gate principal |
|---|---|---|---|---|---|
| PER-KPI-DQ-001 | Freshness compliance | contratos/datasets dentro da freshness governada / monitorados | % | proposed | freshness contract |
| PER-KPI-DQ-002 | Indicadores indisponíveis | KPIs esperados sem dado utilizável | quantidade | proposed | registry + availability rules |
| PER-KPI-DQ-003 | Supressões de disclosure | leituras protegidas ou indisponíveis por política/finalidade | quantidade | proposed | disclosure policy |
| PER-KPI-DQ-004 | Completude de proveniência | outputs com proveniência suficiente / outputs avaliados | % | proposed | provenance contract |
| PER-KPI-DQ-005 | Leituras com evidência insuficiente | afirmações ou interpretações que não atingem suficiência mínima | leituras | proposed | evidence sufficiency |
| PER-KPI-DQ-006 | Conflitos de fonte não resolvidos | leituras com divergência material ainda não reconciliada | leituras | proposed | conflict semantics + authority |

Qualidade qualifica confiança; não fabrica certeza.

```text
AUSÊNCIA DE EVIDÊNCIA SUFICIENTE
→ PODE PRODUZIR AUSÊNCIA LEGÍTIMA DE CONCLUSÃO

DADO MAIS RECENTE
≠ DADO AUTOMATICAMENTE MAIS VERDADEIRO
```

---

## 17. Históricos e eventos como dimensão transversal

O inventário original preserva históricos e eventos como necessidade analítica da Pessoa.

Nesta versão:

```text
HISTÓRICO
→ DIMENSÃO TEMPORAL TRANSVERSAL
→ NOT A KPI FAMILY

EVENTO
→ UNIDADE QUE EXIGE SEMÂNTICA PRÓPRIA
→ NÃO É AUTOMATICAMENTE PROGRESSO, EVOLUÇÃO OU RESULTADO
```

Histórico pode atravessar objetivos, passos, trajetórias, relações, participações, outputs e plano, desde que cada evento preserve:

- natureza;
- timestamp/período;
- source;
- autoridade;
- proveniência;
- validade;
- correções/supersessões quando aplicáveis.

A ausência de evento em uma janela não deve ser interpretada automaticamente como estagnação, abandono ou falha.

---

## 18. Filtros candidatos

Filtros somente podem restringir e organizar o escopo autorizado:

- período e comparação de período;
- Domínio de Evolução confirmado quando aplicável;
- natureza do objeto;
- estado de objetivo;
- estado de Próximo Passo;
- trajetória/estado de leitura legitimamente definido;
- relação/participação/experiência;
- natureza de evidência;
- natureza do input/resultado;
- estado epistemológico/derivacional;
- natureza de output de Intelligence;
- confiança/incerteza quando material;
- estado de contestação/revisão;
- plano/ciclo de capacidade.

```text
FILTRO
→ SUBCONJUNTO DO ACCESS SCOPE
→ NUNCA AMPLIA DISCLOSURE
→ NUNCA CONFUNDE NATUREZA DO INPUT/RESULTADO, ESTADO EPISTEMOLÓGICO/DERIVACIONAL OU NATUREZA DO OUTPUT
```

Filtro por domínio não transforma domínio em identidade ou prioridade.

---

## 19. Drill-down

Estrutura candidata:

```text
N0 — PESSOA AUTORIZADA / PRÓPRIO RECORTE
→ N1 — FAMÍLIA ANALÍTICA
→ N2 — OBJETO / PERÍODO / DOMÍNIO / ESTADO AUTORIZADO
→ N3 — PRÓPRIO OBJETO / EVENTO / EVIDÊNCIA / OUTPUT AUTORIZADO
```

O nível de detalhe não pode ampliar a autoridade.

```text
DADO AGREGADO PRÓPRIO
→ NÃO CRIA ACESSO A DADO PRIVADO DA CONTRAPARTE

RELAÇÃO COM ORGANIZAÇÃO / COLETIVO / BUSINESS
→ NÃO CRIA ACESSO AO CONTEXTO PRIVADO DO OUTRO PARTICIPANTE
```

Drill-down em inferência, predição ou interpretação deve preservar explicabilidade, evidência, confiança, incerteza, limitações e contestação quando aplicáveis.

---

## 20. Estados obrigatórios de visualização

```text
LOADING
NO_DATA
INSUFFICIENT_DATA
INSUFFICIENT_EVIDENCE
SUPPRESSED_BY_POLICY
SOURCE_DELAYED
UNDER_REVIEW
CONTESTED
NOT_ENTITLED
ERROR
AVAILABLE
```

`0` não substitui `NO_DATA`.

`NO_DATA` não significa ausência de trajetória, valor, esforço ou evolução.

`INSUFFICIENT_EVIDENCE` não deve ser renderizado como conclusão negativa.

`CONTESTED` e `UNDER_REVIEW` não devem ser mascarados como leitura final.

`NOT_ENTITLED` descreve capacidade comercial quando aplicável e não substitui autoridade legal, de privacidade ou de governança superior.

`SUPPRESSED_BY_POLICY` não deve revelar por inferência o conteúdo protegido.

---

## 21. Contratos lógicos esperados

Sem definir schema físico, o Dashboard Pessoa poderá futuramente consumir contratos equivalentes a:

- Person Journey Context Projection;
- Domain Link Projection;
- Objective Aggregate / Projection;
- Next Step Aggregate / Projection;
- Evolution / Trajectory Projection;
- Participation / Relationship / Experience Projection;
- Authorized Intelligence Output Projection;
- Authorized Graph / Analytics Output Projection;
- Plan / Capacity Projection;
- Data Quality / Freshness / Provenance Status.

Esses contratos não constituem um `super perfil` universal da Pessoa.

```text
CONTEXT PACKAGE
→ PURPOSE-LIMITED
→ MINIMIZED
→ AUTHORIZED

CONTEXT PACKAGE
≠ UNIVERSAL PERSON PROFILE
```

Cada payload deve carregar, quando aplicável:

- `metric_id` ou identificador do output;
- período e temporalidade;
- valor/unidade quando existir;
- population/object scope;
- source/version;
- natureza do input/resultado;
- natureza do output quando aplicável;
- estado epistemológico/derivacional;
- proveniência;
- freshness;
- sensibilidade/access class;
- confidence/uncertainty quando material;
- suppression/review/contest state;
- claims permitidos e limitações quando aplicáveis.

---

## 22. Privacidade, controle e disclosure

O Dashboard Pessoa opera sob privacidade por finalidade e minimização.

A própria Pessoa deve possuir os controles governados que forem aplicáveis ao tipo de dado ou output, incluindo confirmação, revisão, contestação, retirada ou correção quando a autoridade especializada permitir.

```text
AUTORIDADE PARA PERSONALIZAR
≠ AUTORIDADE PARA COMPARTILHAR

AUTORIDADE PARA PROCESSAR
≠ AUTORIDADE PARA DISCLOSURE

COMPARTILHAMENTO ANTERIOR
≠ CONSENTIMENTO PERMANENTE

RELAÇÃO INSTITUCIONAL
≠ ACESSO À JOURNEY PRIVADA
```

Nenhuma Organização, Coletivo, relação Business, anunciante, parceiro ou terceiro recebe este recorte por padrão.

Qualquer compartilhamento futuro exige contrato próprio de finalidade, escopo, sensibilidade, temporalidade, revogação e autoridade.

A existência de contexto sensível não autoriza segmentação comercial, publicidade comportamental ou exploração de vulnerabilidade por inferência.

---

## 23. Orientação futura para Replit

Quando houver autorização formal de build, a ferramenta deverá:

1. não inventar KPI, fórmula, preço, entitlement, threshold, source, schema ou permissão;
2. usar `PER-KPI-*` como identificadores estáveis, não labels visuais;
3. bloquear KPIs `proposed` e `source_pending` para consumo canônico com dado real;
4. preservar Dashboard Pessoa ≠ Hoje ≠ Meus Objetivos ≠ Meus Próximos Passos ≠ Minha Evolução;
5. não criar score global, ranking, percentual universal de evolução, diagnóstico ou perfil determinístico;
6. preservar Domínio de Evolução ≠ identidade ≠ prioridade ≠ objetivo ≠ progresso;
7. distinguir candidato de confirmado;
8. distinguir `PROPOSTO` de aceito/decidido em Próximos Passos;
9. não converter conclusão de objetivo/passo em prova de evolução;
10. preservar mudança ≠ melhora e correlação ≠ causalidade;
11. distinguir declarado, observado, operacional, calculado, inferido, predito, agregado, conhecimento externo e conhecimento governado como naturezas distintas;
12. preservar separadamente o estado epistemológico/derivacional e a natureza do output, sem colapsá-los com a natureza do input/resultado;
13. preservar inferência ≠ fato e recomendação ≠ decisão;
14. manter confiança, incerteza, limitações e contestação quando materiais;
15. aplicar precedência da declaração legítima da Pessoa sobre inferência incompatível em significado pessoal;
16. não usar fator comercial para redefinir relevância pessoal;
17. tratar filtros como restrição adicional;
18. validar escopo no serving/backend, não somente no cliente;
19. separar mock adapters de real adapters;
20. preservar `NO_DATA`, `INSUFFICIENT_DATA`, `INSUFFICIENT_EVIDENCE`, `SUPPRESSED_BY_POLICY`, `UNDER_REVIEW`, `CONTESTED`, `NOT_ENTITLED` e `SOURCE_DELAYED`;
21. preservar versão, temporalidade, freshness e proveniência;
22. não hard-code preços ou entitlements não congelados;
23. não implementar compartilhamento com Organização, Coletivo, Business ou terceiro por conveniência;
24. não expor dados privados de contraparte em drill-down relacional;
25. não transformar histórico em placar de produtividade pessoal;
26. registrar a versão deste master usada na build.

---

## 24. Critérios de aceite para futuro handoff

Antes de qualquer release `READY FOR BUILD`:

```text
[ ] KPI selecionado = defined OU approved-equivalent
[ ] pergunta/finalidade fechadas
[ ] população/objeto definidos
[ ] fórmula e componentes definidos
[ ] janela temporal/granularidade definidas
[ ] source/data contract definido
[ ] natureza do input/resultado definida
[ ] natureza do output definida quando aplicável
[ ] estado epistemológico/derivacional preservado
[ ] access/disclosure definido
[ ] sensibilidade/minimização definidas
[ ] filtros/drill-down definidos
[ ] null/zero/no-data definidos
[ ] freshness/quality checks definidos
[ ] proveniência definida
[ ] confidence/uncertainty definidos quando materiais
[ ] contestação/revisão definida quando aplicável
[ ] precedência da autoridade da Pessoa preservada
[ ] relações não ampliam disclosure da contraparte
[ ] claims suportados/proibidos definidos
[ ] contratos de domínio aplicáveis satisfeitos
[ ] Design/build authorization foi emitida
```

---

## 25. Itens explicitamente bloqueados nesta versão

```text
REAL DATA
→ NOT AUTHORIZED

BACKEND / API FÍSICA
→ NOT DEFINED HERE

TECHNICAL RBAC
→ NOT IMPLEMENTED

AUTHENTICATED HOME / TODAY / SURFACE MAP / STATE MAP
→ NOT DEFINED BY THIS DOCUMENT

FINAL VISUAL DESIGN
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

UNIVERSAL PERSON SCORE / RANKING
→ NOT AUTHORIZED

GLOBAL EVOLUTION PERCENTAGE
→ NOT AUTHORIZED

MEDICAL / PSYCHOLOGICAL DIAGNOSIS
→ NOT AUTHORIZED

SPIRITUAL EVALUATION
→ NOT AUTHORIZED

DETERMINISTIC PERSON PROFILE
→ NOT AUTHORIZED

COMMERCIAL VULNERABILITY PROFILE
→ NOT AUTHORIZED

AUTOMATED PRIORITY / URGENCY / HUMAN DECISION
→ NOT AUTHORIZED

CROSS-PERSON RANKING / COMPARISON
→ NOT AUTHORIZED BY THIS MASTER

ORGANIZATION / COLLECTIVE / BUSINESS ACCESS TO PRIVATE PERSON JOURNEY
→ NOT AUTHORIZED

BEHAVIORAL ADVERTISING FROM SENSITIVE JOURNEY CONTEXT
→ NOT AUTHORIZED

PROFESSIONAL OR INSTITUTIONAL AUTHORITY REPLACEMENT
→ NOT AUTHORIZED

ADS ANALYTICS
→ OUTSIDE THIS MASTER
→ ANNEX F REMAINS SEPARATE
```

---

## 26. Estado final desta versão

```text
GKR-INTELLIGENCE-DASHBOARD-PERSON-001
→ ACTIVE v0.1.2
→ ANNEX E PRE-IMPLEMENTATION MASTER

PERSON JOURNEY AUTHORITY
→ GKR-JOURNEY-PERSON-001 PRESERVED

DIRECTION / MOVEMENT / EVOLUTION AUTHORITIES
→ GKR-UX-D5-C1-001 + SPECIALIZED CONTRACTS PRESERVED

ANALYTICAL AREAS
→ 9

KPI FAMILIES
→ CTX / OBJ / MOV / EVO / REL / INT / CAP / DQ

HISTORY / EVENTS
→ CROSS-CUTTING TEMPORAL DIMENSION
→ NO AUTONOMOUS KPI FAMILY

PERSON GLOBAL SCORE
→ BLOCKED / NOT MATERIALIZED

KPI IMPLEMENTATION READINESS
→ NONE CLAIMED BY INFERENCE
→ ALL CURRENT KPIs = proposed
→ ALL = NOT_READY

PERSON AUTHORITY
→ OWN AUTHORIZED DATA / JOURNEY / OUTPUTS
→ MEANING-PERSONAL DECLARATION PRECEDENCE PRESERVED

THIRD-PARTY PRIVATE DATA
→ NOT AUTOMATICALLY DISCLOSED

PROCESSING AUTHORIZED
≠ DISCLOSURE AUTHORIZED

REAL DATA / BACKEND / API / TECHNICAL RBAC / PRODUCTION
→ NOT AUTHORIZED

REPLIT BUILD
→ NOT AUTHORIZED

ANNEX F
→ UNCHANGED / NOT MATERIALIZED BY THIS DOCUMENT
```

A materialização documental deste master não autoriza dados reais, implementação, produção, disclosure adicional a terceiros ou promoção automática de KPI.
