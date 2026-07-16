---
id: PAS-001-IC-CONTRACT-001
title: KPIs, Guardrails, Cenários e Contrato Final da Capacidade de Intervenções Contextuais
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-16
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-IC-FOUNDATION-001
  - PAS-001-IC-LIFECYCLE-001
  - PAS-001-IC-VIEW-001
  - PAS-001-IC-EVENT-001
  - PAS-001-IC-INTEGRATION-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-IC-CONTRACT-001 — KPIs, Guardrails, Cenários e Contrato Final da Capacidade de Intervenções Contextuais

## 1. Autoridade e vínculo

Este documento é a **sexta extensão normativa e o contrato final da Capacidade 07 — Intervenções Contextuais** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser interpretado como continuidade das cinco extensões anteriores da Capacidade 07, do `PAS-001 0.5.0`, das seções 1 a 3271, dos contratos finais das Capacidades 02 a 06, da `GLPA-001` e da `GIA-000`.

Esta extensão substitui normativamente o estado `In progress` da Capacidade 07 por `Functionally complete` e eleva seu progresso editorial de referência de `90%` para `100%`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade da especificação-base ou das capacidades concluídas.

# 3272. Bloco final da Capacidade de Intervenções Contextuais

Este documento consolida:

- 80 KPIs em 16 famílias;
- baseline funcional;
- segmentação mínima da baseline;
- painel de saúde;
- cinco níveis de desempenho;
- 28 guardrails de tolerância zero;
- cenários funcionalmente ideais;
- cenários alternativos;
- cenários limite;
- critérios de conclusão;
- lacunas bloqueantes e não bloqueantes;
- critérios de reabertura;
- contrato funcional final.

Os indicadores deverão avaliar a qualidade da capacidade e do sistema, nunca o mérito, valor, produtividade, fé, disciplina, sucesso ou evolução humana do participante.

# 3273. Finalidade dos indicadores

Os indicadores deverão avaliar se a capacidade:

1. reconhece oportunidades legítimas de manifestação;
2. seleciona corretamente entre agir, perguntar, informar, sugerir, lembrar, alertar, confirmar, aguardar, observar ou silenciar;
3. preserva finalidade e autoridade;
4. utiliza contexto mínimo;
5. respeita atenção e interruptibilidade;
6. distingue importância e urgência;
7. protege conteúdo sensível;
8. controla fadiga e frequência;
9. respeita horários protegidos;
10. utiliza canais adequados;
11. preserva a autonomia do participante;
12. mantém relações comerciais transparentes;
13. integra capacidades sem transferir decisão;
14. opera com confiabilidade;
15. permite correção e revogação;
16. assegura explicabilidade e auditoria;
17. reconhece o silêncio como resultado legítimo;
18. evita manipulação e pressão indevida.

# 3274. Princípios de medição

A medição deverá observar:

- finalidade funcional;
- proporcionalidade;
- não julgamento;
- minimização;
- proteção de dados;
- segmentação por contexto;
- distinção entre fatos e estimativas;
- temporalidade;
- explicabilidade;
- revisão periódica;
- prevalência dos guardrails;
- inexistência de metas arbitrárias;
- separação entre comportamento humano e desempenho sistêmico.

Nenhum resultado médio positivo poderá compensar violação crítica de guardrail.

# 3275. Unidades de medição

As métricas poderão utilizar:

- quantidade;
- taxa;
- proporção;
- tempo;
- distribuição;
- cobertura;
- recorrência;
- severidade;
- latência;
- atualidade;
- completude;
- esforço;
- concentração;
- divergência;
- correções;
- contestações;
- revogações;
- falhas;
- repetições;
- supressões;
- adiamentos;
- silêncios.

As análises deverão ser segmentadas, quando necessário, por comportamento, finalidade, canal, sensibilidade, urgência, horário, origem, autoridade, integração, categoria, fadiga, estado funcional e tipo de participante.

# 3276. Famílias de indicadores

Os KPIs serão organizados em 16 famílias:

1. identificação, avaliação e admissão;
2. finalidade e autoridade;
3. contexto, relevância e proporcionalidade;
4. atenção e interruptibilidade;
5. importância, urgência e temporalidade;
6. sensibilidade, privacidade e terceiros;
7. fadiga, frequência e repetição;
8. seleção de comportamento;
9. programação, espera e prontidão;
10. canais, apresentação e entrega;
11. resposta, autonomia e controle;
12. transparência e neutralidade comercial;
13. integrações, sincronização e revogação;
14. confiabilidade, consistência e recuperação;
15. explicabilidade, auditoria e acessibilidade;
16. silêncio, ausência e equilíbrio sistêmico.

# 3277. Família 1 — Identificação, avaliação e admissão

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-001` | Oportunidades identificadas com origem e finalidade preliminar | Mede rastreabilidade inicial |
| `IC-KPI-002` | Candidaturas com elementos mínimos para avaliação | Mede admissibilidade |
| `IC-KPI-003` | Duplicidades semânticas reconhecidas antes da admissão | Mede prevenção de repetição |
| `IC-KPI-004` | Admissões com critérios, limitações e comportamento registrados | Avalia integridade decisória |
| `IC-KPI-005` | Intervenções apresentadas sem admissão funcional | Mede atalho crítico de ciclo |

# 3278. Família 2 — Finalidade e autoridade

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-006` | Intervenções com finalidade específica e compreensível | Mede legitimidade |
| `IC-KPI-007` | Fontes e atores com autoridade validada | Mede governança |
| `IC-KPI-008` | Afirmações aceitas além da autoridade declarada | Mede ampliação indevida |
| `IC-KPI-009` | Mudanças materiais de finalidade submetidas a nova avaliação | Mede controle de reutilização |
| `IC-KPI-010` | Excesso de autoridade com efeitos bloqueados e corrigidos | Avalia resposta de governança |

# 3279. Família 3 — Contexto, relevância e proporcionalidade

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-011` | Decisões baseadas no contexto mínimo necessário | Mede minimização |
| `IC-KPI-012` | Contextos utilizados com origem, validade e limitações conhecidas | Mede qualidade contextual |
| `IC-KPI-013` | Intervenções reavaliadas após mudança material | Mede atualidade |
| `IC-KPI-014` | Intervenções cuja utilidade supera justificadamente o custo da interrupção | Mede proporcionalidade |
| `IC-KPI-015` | Contexto excessivo utilizado sem necessidade funcional | Mede exposição indevida |

# 3280. Família 4 — Atenção e interruptibilidade

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-016` | Avaliações de atenção tratadas como estimativas limitadas | Mede precisão semântica |
| `IC-KPI-017` | Interruptibilidade avaliada por contexto, canal e momento | Mede adequação da interrupção |
| `IC-KPI-018` | Disponibilidade técnica tratada como interruptibilidade | Mede colapso proibido |
| `IC-KPI-019` | Intervenções adiadas diante de baixa interruptibilidade | Avalia proteção de atenção |
| `IC-KPI-020` | Atenção interpretada como consentimento ou intenção | Mede violação crítica |

# 3281. Família 5 — Importância, urgência e temporalidade

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-021` | Importância e urgência representadas separadamente | Mede clareza |
| `IC-KPI-022` | Urgências com risco, prazo ou obrigação material demonstrável | Mede fundamento |
| `IC-KPI-023` | Urgências fabricadas por campanha, estoque ou pressão comercial | Mede manipulação |
| `IC-KPI-024` | Intervenções apresentadas dentro de sua validade temporal | Mede atualidade |
| `IC-KPI-025` | Reavaliações realizadas antes de manifestações atrasadas | Mede segurança temporal |

# 3282. Família 6 — Sensibilidade, privacidade e terceiros

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-026` | Intervenções sensíveis corretamente classificadas | Mede cobertura protetiva |
| `IC-KPI-027` | Títulos, prévias e canais compatíveis com a sensibilidade | Mede privacidade visual |
| `IC-KPI-028` | Dados de terceiros minimizados e protegidos | Mede proteção relacional |
| `IC-KPI-029` | Perfis paralelos de terceiros identificados e bloqueados | Mede violação crítica |
| `IC-KPI-030` | Conteúdo sensível utilizado em publicidade ou pressão comercial | Mede exploração proibida |

# 3283. Família 7 — Fadiga, frequência e repetição

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-031` | Fadiga avaliada antes de repetição ou escalonamento | Mede prevenção |
| `IC-KPI-032` | Intervenções agrupadas ou adiadas diante de fadiga elevada | Mede redução de pressão |
| `IC-KPI-033` | Repetições sustentadas por mudança material ou regra autorizada | Mede legitimidade |
| `IC-KPI-034` | Frequência dentro dos limites globais, por categoria e canal | Mede controle |
| `IC-KPI-035` | Fadiga utilizada para aumentar intensidade ou persuasão | Mede violação crítica |

# 3284. Família 8 — Seleção de comportamento

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-036` | Decisões com comportamento principal explícito | Mede clareza funcional |
| `IC-KPI-037` | Perguntas limitadas à informação necessária | Mede minimização |
| `IC-KPI-038` | Alertas baseados em risco ou mudança material | Mede legitimidade |
| `IC-KPI-039` | Ações materiais com autorização e executor identificados | Mede controle |
| `IC-KPI-040` | Sugestões ou lembretes tratados como obrigação | Mede ampliação indevida |

# 3285. Família 9 — Programação, espera e prontidão

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-041` | Programações com janela, fuso, validade e cancelamento | Mede completude |
| `IC-KPI-042` | Horários protegidos respeitados | Mede aderência |
| `IC-KPI-043` | Condições de espera e retomada explicitamente registradas | Mede previsibilidade |
| `IC-KPI-044` | Prontidão revalidada antes da entrega | Mede segurança |
| `IC-KPI-045` | Intervenções expiradas apresentadas sem nova avaliação | Mede falha temporal |

# 3286. Família 10 — Canais, apresentação e entrega

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-046` | Canais selecionados por finalidade, urgência e sensibilidade | Mede adequação |
| `IC-KPI-047` | Apresentação, envio, entrega e visualização preservados como fatos distintos | Mede consistência semântica |
| `IC-KPI-048` | Entregas parciais claramente identificadas | Mede veracidade |
| `IC-KPI-049` | Estado consistente entre superfícies e canais | Mede sincronização |
| `IC-KPI-050` | Falhas de entrega apresentadas como sucesso | Mede violação operacional |

# 3287. Família 11 — Resposta, autonomia e controle

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-051` | Respostas processadas dentro do escopo declarado | Mede integridade |
| `IC-KPI-052` | Respostas ambíguas bloqueadas antes de efeitos materiais | Mede segurança |
| `IC-KPI-053` | Adiamento, silêncio, recusa, ocultação e bloqueio disponíveis | Mede autonomia |
| `IC-KPI-054` | Ausência de resposta tratada sem inferência de recusa | Mede não julgamento |
| `IC-KPI-055` | Recusas processadas sem penalidade ou pressão adicional | Mede respeito ao participante |

# 3288. Família 12 — Transparência e neutralidade comercial

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-056` | Comunicações comerciais explicitamente identificadas | Mede transparência |
| `IC-KPI-057` | Patrocínio, comissão e publicidade declarados | Mede completude econômica |
| `IC-KPI-058` | Relações comerciais influenciando urgência ou intensidade | Mede interferência crítica |
| `IC-KPI-059` | Guivos Ads separado das intervenções funcionais | Mede separação arquitetural |
| `IC-KPI-060` | Contexto sensível utilizado para segmentação comercial | Mede exploração proibida |

# 3289. Família 13 — Integrações, sincronização e revogação

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-061` | Integrações com finalidade, autoridade e escopo definidos | Mede admissibilidade |
| `IC-KPI-062` | Sincronizações versionadas e idempotentes | Mede consistência |
| `IC-KPI-063` | Divergências reconhecidas e reconciliadas explicitamente | Mede integridade |
| `IC-KPI-064` | Revogações propagadas aos consumidores relevantes | Mede eficácia |
| `IC-KPI-065` | Revogações declaradas concluídas antes da propagação | Mede violação crítica |

# 3290. Família 14 — Confiabilidade, consistência e recuperação

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-066` | Efeitos duplicados por reprocessamento | Mede idempotência |
| `IC-KPI-067` | Estados impossíveis por eventos fora de ordem | Mede ordenação |
| `IC-KPI-068` | Conflitos resolvidos sem sobrescrita silenciosa | Mede concorrência |
| `IC-KPI-069` | Recuperações com último estado válido preservado | Mede resiliência |
| `IC-KPI-070` | Fluxos reconstruíveis após falha | Mede recuperabilidade |

# 3291. Família 15 — Explicabilidade, auditoria e acessibilidade

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-071` | Intervenções com justificativas de motivo e momento disponíveis | Mede transparência |
| `IC-KPI-072` | Proveniência reconstruível desde a fonte até o efeito | Mede rastreabilidade |
| `IC-KPI-073` | Contestações e correções com fundamento visível | Mede justiça funcional |
| `IC-KPI-074` | Controles acessíveis por teclado, leitor de tela e linguagem clara | Mede inclusão |
| `IC-KPI-075` | Esforço para compreender, adiar, silenciar ou contestar | Mede acessibilidade cognitiva |

# 3292. Família 16 — Silêncio, ausência e equilíbrio sistêmico

| KPI | Indicador | Avaliação |
|---|---|---|
| `IC-KPI-076` | Avaliações que resultam legitimamente em silêncio | Mede capacidade de não manifestação |
| `IC-KPI-077` | Ausências legítimas preservadas sem preenchimento artificial | Mede integridade |
| `IC-KPI-078` | Silêncio tratado como falha de engajamento | Mede pressão sistêmica |
| `IC-KPI-079` | Distribuição de comportamentos sem concentração artificial em notificações | Mede equilíbrio |
| `IC-KPI-080` | Intervenções criadas apenas para aumentar atividade ou tempo de tela | Mede desvio de finalidade |

# 3293. Baseline funcional

Antes de estabelecer metas permanentes, a Guivos deverá construir baseline real.

A baseline deverá considerar:

- comportamento selecionado;
- canal;
- finalidade;
- fonte e autoridade;
- estado funcional;
- atenção;
- interruptibilidade;
- importância;
- urgência;
- sensibilidade;
- fadiga;
- frequência;
- horário;
- relação comercial;
- integração;
- tipo de participante;
- categoria de intervenção;
- volume operacional;
- maturidade do produto.

Metas não deverão ser copiadas de redes sociais, sistemas publicitários, plataformas de engajamento ou produtos orientados à maximização de notificações.

# 3294. Segmentação e janelas da baseline

A baseline deverá utilizar janelas compatíveis com:

- intervenções imediatas;
- intervenções programadas;
- recorrências;
- mudanças materiais;
- períodos de silêncio;
- horários protegidos;
- períodos de alta sensibilidade;
- ciclos de integração;
- correções;
- revogações.

Comparações deverão evitar misturar categorias, canais, sensibilidades ou finalidades materialmente distintas.

# 3295. Painel de saúde da capacidade

O painel deverá apresentar, no mínimo:

1. identificação, avaliação e admissão;
2. finalidade e autoridade;
3. contexto e proporcionalidade;
4. atenção e interruptibilidade;
5. importância e urgência;
6. sensibilidade e privacidade;
7. fadiga e frequência;
8. comportamento selecionado;
9. programação e prontidão;
10. canais e entrega;
11. autonomia e controles;
12. neutralidade comercial;
13. integrações e revogação;
14. confiabilidade e recuperação;
15. explicabilidade e acessibilidade;
16. silêncio e equilíbrio;
17. guardrails.

O painel não deverá gerar pontuação de mérito, disciplina, produtividade, fé, valor ou evolução do participante.

# 3296. Níveis de desempenho funcional

## Crítico

Existem violações de guardrail, riscos materiais ou perda relevante de controle.

## Instável

A capacidade opera, mas apresenta falhas recorrentes, inconsistências, pressão excessiva ou proteção insuficiente.

## Adequado

Os contratos centrais funcionam e os riscos críticos estão controlados.

## Confiável

A capacidade opera com consistência, explicabilidade, baixa incidência de falhas e controle efetivo.

## Maduro

A capacidade possui baseline estável, integração segura, silêncio funcional preservado e melhoria sistêmica contínua.

Nenhum nível superior poderá ser atribuído enquanto houver guardrail crítico violado.

# 3297. Guardrails de tolerância zero

A capacidade possuirá 28 guardrails obrigatórios:

1. intervenção sem finalidade específica;
2. ação material sem autorização vigente;
3. ampliação da autoridade de fonte, organização, profissional ou integração;
4. coleta excessiva ou desnecessária de contexto;
5. pergunta sensível sem finalidade e proteção proporcionais;
6. atenção tratada como consentimento;
7. visualização tratada como interesse;
8. ausência de resposta tratada como recusa;
9. adiamento tratado como rejeição;
10. silêncio tratado como falha;
11. sugestão ou lembrete transformado em obrigação;
12. alerta sem risco, prazo ou mudança material;
13. urgência fabricada por campanha, estoque, escassez comercial ou meta;
14. fadiga utilizada para aumentar pressão, intensidade ou frequência;
15. desrespeito injustificado a horário protegido;
16. exposição de conteúdo sensível em título, prévia ou dispositivo compartilhado;
17. uso de contexto sensível para publicidade, precificação ou persuasão;
18. publicidade apresentada como pergunta, alerta, lembrete ou intervenção funcional;
19. relação comercial alterando prioridade, intensidade ou canal;
20. acesso organizacional irrestrito à jornada pessoal;
21. formação de perfil paralelo de terceiro;
22. conclusão de operação externa sem retorno autorizado;
23. efeito material duplicado por reprocessamento;
24. estado impossível produzido por evento fora de ordem;
25. sobrescrita silenciosa de conflito;
26. revogação declarada concluída antes da propagação suficiente;
27. falha parcial apresentada como sucesso integral;
28. uso de medo, culpa, vergonha, fé, mérito, disciplina ou valor humano para pressionar o participante.

# 3298. Tratamento de violação de guardrail

Uma violação deverá produzir:

1. interrupção do fluxo afetado;
2. bloqueio de novos efeitos;
3. limitação de automação;
4. preservação de evidências;
5. classificação de severidade;
6. registro auditável;
7. notificação interna;
8. comunicação ao participante quando necessária;
9. correção ou compensação;
10. propagação aos consumidores;
11. análise de causa;
12. validação da recuperação;
13. revisão contratual ou técnica.

Nenhuma média positiva poderá neutralizar a violação.

# 3299. Cenários funcionalmente ideais

Os cenários ideais deverão demonstrar que a capacidade:

- manifesta-se somente quando adequado;
- permanece em silêncio quando necessário;
- utiliza o comportamento menos intrusivo suficiente;
- protege atenção, autonomia e sensibilidade;
- mantém finalidade e autoridade;
- preserva neutralidade comercial;
- permite explicação e controle;
- opera com falha segura.

# 3300. Cenário ideal — Silêncio após avaliação

Fluxo funcional:

> sinal recebido → finalidade validada → relevância insuficiente ou custo de interrupção elevado → silêncio selecionado → decisão registrada → possibilidade de reavaliação futura

O silêncio não deverá ser tratado como perda de oportunidade, falha ou baixa conversão.

# 3301. Cenário ideal — Pergunta mínima

A pergunta deverá:

- solicitar somente a informação necessária;
- declarar finalidade;
- explicar efeitos da resposta;
- permitir recusa;
- permitir resposta posterior;
- não bloquear indevidamente o participante;
- não gerar consequência material diante de ambiguidade.

# 3302. Cenário ideal — Lembrete de compromisso conhecido

O lembrete deverá recuperar algo previamente conhecido e autorizado.

Ele não deverá:

- criar compromisso;
- alterar prioridade;
- produzir culpa;
- escalar intensidade sem fundamento;
- repetir-se sem mudança material.

# 3303. Cenário ideal — Alerta com risco real

O alerta deverá apresentar:

- risco ou mudança material;
- fonte;
- validade;
- impacto;
- urgência real;
- limitações;
- ações disponíveis;
- possibilidade de obter detalhes.

Promoção, estoque ou campanha não deverão fundamentar o alerta.

# 3304. Cenário ideal — Ação material autorizada

Fluxo funcional:

> condição reconhecida → ação avaliada → autorização vigente confirmada → executor identificado → escopo delimitado → ação solicitada → retorno externo recebido → resultado objetivo registrado

A intervenção não deverá declarar conclusão antes da confirmação do executor.

# 3305. Cenário ideal — Intervenção sensível

Deverá utilizar:

- título neutro;
- conteúdo minimizado;
- canal protegido;
- autenticação proporcional;
- ausência de prévia pública;
- horário adequado;
- retenção limitada;
- possibilidade de silêncio;
- proibição de publicidade derivada.

# 3306. Cenário ideal — Apresentação de Oportunidade Ativa

Oportunidades Ativas deverá fornecer relevância, disponibilidade, elegibilidade, risco, custos, temporalidade e relação comercial.

Intervenções Contextuais deverá decidir:

- se apresentar;
- quando apresentar;
- por qual canal;
- com qual intensidade;
- quando aguardar;
- quando silenciar.

Patrocínio não deverá alterar essa decisão.

# 3307. Cenário ideal — Apoio durante Evento de Vida

A intervenção deverá:

- respeitar a sensibilidade;
- evitar interpretação emocional automática;
- utilizar linguagem proporcional;
- reduzir frequência;
- oferecer controle;
- impedir exploração comercial;
- permitir encaminhamento humano quando apropriado.

# 3308. Cenário ideal — Intervenção recorrente

A recorrência deverá possuir:

- finalidade;
- frequência;
- janela;
- limite;
- validade;
- condição de revisão;
- controle do participante;
- comportamento diante de fadiga;
- encerramento explícito.

# 3309. Cenário ideal — Comunicação institucional ou coletiva

O cenário deverá distinguir:

- obrigação institucional;
- convite;
- benefício;
- alerta;
- comunicação geral;
- contexto coletivo;
- decisão individual;
- dados públicos e privados.

Obrigação institucional não deverá ser apresentada como interesse pessoal.

# 3310. Cenário ideal — Consistência entre canais

Ao migrar entre aplicativo, e-mail, notificação, canal conversacional ou calendário:

- a identidade da intervenção deverá permanecer;
- o estado deverá permanecer consistente;
- respostas anteriores deverão ser preservadas;
- silêncio e bloqueios deverão ser respeitados;
- conteúdo sensível deverá continuar protegido.

# 3311. Cenário ideal — Contestação, correção e revogação

Fluxo funcional:

> intervenção apresentada → fundamento contestado → novos efeitos limitados → avaliação realizada → erro reconhecido → correção compensatória publicada → consumidores notificados → revogação propagada quando aplicável

O histórico anterior não deverá ser apagado.

# 3312. Cenário ideal — Execução externa

O produto executor deverá governar:

- validação;
- transação;
- pagamento;
- reserva;
- contratação;
- entrega;
- resultado operacional.

Intervenções Contextuais deverá preservar somente os fatos necessários à manifestação e ao acompanhamento autorizado.

# 3313. Cenários alternativos

Cenários alternativos representam condições em que o fluxo ideal não está disponível, mas ainda existe caminho seguro e legítimo.

# 3314. Cenário alternativo — Contexto incompleto

A capacidade deverá poder:

- perguntar o mínimo necessário;
- utilizar hipótese explicitamente limitada;
- reduzir intensidade;
- selecionar canal passivo;
- aguardar;
- silenciar.

Ela não deverá fabricar precisão.

# 3315. Cenário alternativo — Identidade incerta

Diante de associação incerta:

- efeitos pessoais deverão ser limitados;
- conteúdo sensível deverá ser bloqueado;
- poderá ser solicitada confirmação;
- o estado anterior deverá ser preservado;
- a associação deverá ser corrigível.

# 3316. Cenário alternativo — Canal indisponível

A capacidade poderá:

- utilizar canal alternativo autorizado;
- aguardar;
- registrar falha;
- reduzir conteúdo;
- manter a intervenção na Central;
- cancelar a entrega sem cancelar o agregado.

# 3317. Cenário alternativo — Fontes conflitantes

A capacidade deverá:

- preservar as versões;
- identificar autoridades;
- apresentar incerteza;
- bloquear afirmações definitivas;
- solicitar confirmação;
- limitar urgência;
- registrar reconciliação.

# 3318. Cenário alternativo — Fadiga elevada

A capacidade deverá priorizar:

1. silêncio;
2. agrupamento;
3. adiamento;
4. canal passivo;
5. redução de intensidade;
6. resumo periódico.

Fadiga não poderá justificar pressão adicional.

# 3319. Cenário alternativo — Integração temporariamente indisponível

O sistema deverá:

- preservar o último estado válido;
- sinalizar limitação;
- impedir falsa atualização;
- utilizar dados anteriores somente dentro da validade;
- permitir nova tentativa;
- degradar para pergunta ou silêncio.

# 3320. Cenário alternativo — Entrega parcial

A capacidade deverá declarar:

- partes entregues;
- partes pendentes;
- canais afetados;
- risco de duplicidade;
- possibilidade de repetição;
- efeitos já aplicados.

A entrega parcial não representa sucesso integral.

# 3321. Cenário alternativo — Resposta ambígua

A resposta deverá:

- ser registrada como ambígua;
- não produzir efeito material;
- gerar solicitação de esclarecimento quando necessário;
- preservar o estado anterior;
- permitir desistência.

# 3322. Cenário alternativo — Ausência de resposta

A ausência poderá produzir:

- espera;
- silêncio;
- encerramento;
- agrupamento;
- repetição limitada e autorizada.

Não deverá produzir julgamento ou penalidade.

# 3323. Cenários limite

Cenários limite deverão demonstrar que a capacidade preserva controle e segurança mesmo diante de alta complexidade, pressão temporal ou informação insuficiente.

# 3324. Cenário limite — Risco crítico com contexto limitado

A capacidade deverá:

- identificar a limitação;
- utilizar apenas fatos disponíveis;
- evitar diagnóstico;
- apresentar fonte e incerteza;
- oferecer ação segura e reversível;
- encaminhar a autoridade competente;
- evitar linguagem alarmista desnecessária.

# 3325. Cenário limite — Conteúdo sensível em dispositivo compartilhado

A intervenção deverá:

- ocultar o conteúdo;
- utilizar título neutro;
- exigir autenticação;
- impedir ação rápida irreversível;
- reduzir persistência local;
- permitir acesso posterior em ambiente protegido.

# 3326. Cenário limite — Obrigação institucional e preferência pessoal

A capacidade deverá distinguir:

- legitimidade da obrigação;
- autoridade da organização;
- prazo real;
- canal autorizado;
- preferência pessoal;
- possibilidade de contestação;
- consequência objetiva.

Preferência não elimina obrigação legítima, e obrigação não transfere titularidade da jornada.

# 3327. Cenário limite — Sistema externo indisponível próximo ao prazo

A capacidade deverá:

- informar indisponibilidade;
- preservar o prazo real;
- oferecer canal alternativo;
- registrar tentativa;
- evitar declarar conclusão;
- limitar repetição;
- solicitar apoio humano quando necessário.

# 3328. Cenário limite — Contestação após entrega

A contestação deverá poder:

- limitar reapresentações;
- bloquear ações pendentes;
- preservar evidências;
- reavaliar consumidores;
- corrigir significado;
- comunicar efeitos já irreversíveis;
- propagar a decisão.

# 3329. Cenário limite — Revogação durante processamento

A revogação deverá:

- bloquear novos usos;
- interromper etapas ainda reversíveis;
- identificar efeitos já concluídos;
- notificar consumidores;
- preservar evidências mínimas;
- permanecer pendente até propagação suficiente.

# 3330. Cenário limite — Múltiplas intervenções urgentes

A capacidade deverá:

- validar cada urgência;
- eliminar duplicidades;
- agrupar quando possível;
- preservar diferenças de sensibilidade;
- evitar competição por atenção;
- apresentar ordem explicável;
- permitir acesso ao conjunto completo.

# 3331. Cenário limite — Dependência de terceiro

A capacidade deverá distinguir:

- titular;
- terceiro;
- autoridade;
- informação compartilhável;
- autorização;
- responsabilidade;
- estado próprio de cada parte.

O terceiro não deverá receber perfil independente ou acesso à jornada integral.

# 3332. Cenário limite — Versão incompatível ou evento fora de ordem

O sistema deverá:

- preservar o evento;
- impedir aplicação insegura;
- registrar incompatibilidade;
- aguardar dependência;
- reconciliar versões;
- evitar estado impossível;
- permitir reprocessamento posterior.

# 3333. Critérios de conclusão funcional

A Capacidade 07 será considerada funcionalmente concluída quando:

1. possuir singularidade definida;
2. distinguir sinal, candidatura, admissão, manifestação e silêncio;
3. selecionar comportamentos funcionalmente distintos;
4. governar finalidade;
5. limitar autoridade;
6. utilizar contexto mínimo;
7. avaliar relevância e proporcionalidade;
8. governar atenção;
9. governar interruptibilidade;
10. distinguir importância e urgência;
11. proteger sensibilidade;
12. governar fadiga e frequência;
13. respeitar horários protegidos;
14. selecionar canais adequados;
15. governar programação e prontidão;
16. separar apresentação, entrega, visualização e resposta;
17. preservar autonomia;
18. permitir adiamento, silêncio, recusa, ocultação e bloqueio;
19. governar comunicações comerciais;
20. proteger terceiros;
21. governar organizações e profissionais;
22. integrar as demais capacidades;
23. limitar Guivos Intelligence;
24. limitar Platform Layer;
25. governar produtos executores;
26. possuir eventos versionados;
27. operar com idempotência e ordenação;
28. governar conflitos e concorrência;
29. permitir contestação e correção;
30. propagar revogações;
31. possuir falha segura;
32. assegurar reconstrução;
33. possuir 80 KPIs em 16 famílias;
34. possuir baseline e painel de saúde;
35. possuir níveis de desempenho;
36. possuir 28 guardrails;
37. possuir cenários ideal, alternativo e limite;
38. preservar explicabilidade e auditoria;
39. manter o participante no controle;
40. não possuir lacuna funcional bloqueante conhecida.

# 3334. Lacunas não bloqueantes

Não impedem a conclusão funcional:

- implementação técnica;
- schemas físicos;
- APIs;
- banco de dados;
- infraestrutura definitiva de eventos;
- modelos finais de autorização;
- design visual definitivo;
- textos finais de interface;
- dashboards operacionais;
- metas numéricas posteriores à baseline;
- testes automatizados;
- contratos específicos de fornecedores;
- integrações específicas por canal;
- políticas regulatórias por país;
- infraestrutura definitiva de notificações;
- modelos operacionais de atendimento;
- documentação de suporte;
- observabilidade produtiva definitiva.

Esses itens pertencem às fases de design, engenharia, segurança, dados, operação e validação.

# 3335. Lacunas bloqueantes

Seriam bloqueantes:

- ausência de titularidade;
- ausência de finalidade;
- ausência de autoridade;
- inexistência de silêncio funcional;
- incapacidade de distinguir atenção e consentimento;
- incapacidade de distinguir importância e urgência;
- ausência de controle de fadiga;
- inexistência de horários protegidos;
- ausência de proteção sensível;
- ação material sem autorização;
- relação comercial oculta;
- publicidade disfarçada de intervenção;
- exploração de vulnerabilidade;
- ausência de controle do participante;
- ausência de contestação ou correção;
- ausência de revogação;
- transferência de decisão à Intelligence ou às integrações;
- inexistência de idempotência;
- ausência de falha segura;
- utilização da intervenção para avaliar valor humano.

Nenhuma lacuna funcional bloqueante é conhecida na baseline normativa proposta.

# 3336. Finalidade do contrato final

O contrato final governa como a Guivos decide se, quando, como e com qual intensidade deverá manifestar-se diante do participante.

A capacidade deverá apoiar atenção e decisão sem transformar a jornada em:

- caixa de entrada infinita;
- sistema de vigilância;
- feed de engajamento;
- mecanismo de pressão;
- canal publicitário;
- mecanismo de culpa;
- ranking de produtividade;
- avaliação moral.

# 3337. Singularidade funcional

A singularidade da Capacidade de Intervenções Contextuais é:

> **Governar responsavelmente a decisão entre manifestar-se e permanecer em silêncio, utilizando o comportamento, o momento, o canal e a intensidade menos intrusivos capazes de produzir utilidade legítima.**

Ela não governa:

- direção existencial;
- definição de Objetivos;
- decisão de Próximo Passo;
- relevância de Oportunidades Ativas;
- transações;
- experiência vivida;
- evolução humana.

# 3338. Titularidade

Toda intervenção pessoal deverá possuir participante titular identificável.

A titularidade não poderá ser transferida por:

- organização;
- profissional;
- patrocinador;
- fornecedor;
- anunciante;
- integração;
- produto especializado;
- executor externo;
- autoridade técnica;
- representante sem escopo suficiente.

# 3339. Responsabilidades

A capacidade será responsável por:

- identificar oportunidades de intervenção;
- criar e avaliar candidaturas;
- validar finalidade e autoridade;
- selecionar contexto mínimo;
- avaliar relevância e proporcionalidade;
- avaliar atenção e interruptibilidade;
- representar importância e urgência;
- classificar sensibilidade;
- avaliar fadiga e frequência;
- selecionar comportamento;
- programar ou aguardar;
- selecionar canal e intensidade;
- apresentar e acompanhar entrega;
- registrar resposta;
- reconhecer silêncio;
- permitir controles;
- produzir eventos;
- integrar produtores e consumidores;
- governar correções e revogações;
- preservar histórico.

# 3340. Limites

A capacidade não será responsável por:

- criar Objetivos;
- confirmar Próximos Passos;
- definir relevância de oportunidades;
- decidir pelo participante;
- executar transações diretamente;
- confirmar experiência;
- medir evolução humana;
- diagnosticar;
- substituir profissionais;
- impor manifestação;
- fabricar urgência;
- operar publicidade disfarçada;
- atribuir mérito, fé, disciplina, produtividade ou valor moral.

# 3341. Entradas

A capacidade poderá receber:

- solicitações;
- sinais;
- mudanças de Contexto Vivo;
- Objetivos;
- Eventos de Vida;
- Próximos Passos;
- Oportunidades Ativas;
- preferências;
- horários protegidos;
- atenção estimada;
- restrições;
- riscos;
- prazos;
- fontes externas;
- fatos institucionais;
- comunicações profissionais;
- resultados operacionais;
- contestações;
- correções;
- revogações;
- relações comerciais.

# 3342. Admissão

Uma entrada somente deverá produzir candidatura quando houver:

- participante ou público possível;
- origem identificável;
- finalidade preliminar;
- autoridade possível;
- comportamento potencial;
- temporalidade;
- sensibilidade;
- ausência de proibição imediata.

Uma candidatura somente deverá ser admitida após avaliação suficiente de:

- finalidade;
- autoridade;
- relevância;
- proporcionalidade;
- atenção;
- interruptibilidade;
- importância;
- urgência;
- sensibilidade;
- fadiga;
- frequência;
- canal;
- risco;
- reversibilidade.

# 3343. Saídas

A capacidade poderá produzir:

- silêncio;
- ação;
- pergunta;
- informação;
- sugestão;
- lembrete;
- alerta;
- confirmação;
- espera;
- observação;
- programação;
- apresentação;
- entrega;
- resposta registrada;
- adiamento;
- recusa;
- ocultação;
- bloqueio;
- contestação;
- correção;
- revogação;
- eventos funcionais;
- justificativas;
- histórico;
- solicitações a executores externos.

# 3344. Estados e dimensões

O contrato final preserva separadamente:

1. estado funcional;
2. estado da informação;
3. autorização;
4. temporalidade;
5. comportamento selecionado;
6. atenção;
7. interruptibilidade;
8. importância;
9. urgência;
10. sensibilidade;
11. fadiga;
12. frequência;
13. programação;
14. canal;
15. entrega;
16. relação do participante;
17. operação externa;
18. integração;
19. correção;
20. revogação.

Nenhuma dimensão deverá substituir automaticamente as demais.

# 3345. Seleção de comportamento

Cada decisão deverá selecionar exatamente um comportamento principal entre:

- agir;
- perguntar;
- informar;
- sugerir;
- lembrar;
- alertar;
- confirmar;
- aguardar;
- observar;
- silenciar.

O comportamento escolhido deverá ser o menos intrusivo capaz de atender legitimamente à finalidade.

# 3346. Silêncio

Silêncio é resultado funcional válido.

Ele deverá ser selecionado quando:

- a utilidade não superar o custo de interrupção;
- a finalidade não estiver suficientemente definida;
- a autoridade for insuficiente;
- o momento for inadequado;
- a fadiga estiver elevada;
- o conteúdo for excessivamente sensível;
- o canal adequado estiver indisponível;
- não houver ação útil;
- a preferência do participante assim determinar.

# 3347. Atenção e interruptibilidade

Atenção deverá representar somente capacidade provável de receber e compreender.

Interruptibilidade deverá representar adequação contextual da interrupção.

Nenhuma delas representa:

- consentimento;
- interesse;
- intenção;
- disponibilidade pessoal;
- obrigação de resposta.

# 3348. Importância, urgência e temporalidade

Importância representa impacto ou significado.

Urgência representa proximidade temporal de ação necessária.

Urgência somente poderá decorrer de:

- risco;
- segurança;
- prazo real;
- perda objetiva;
- obrigação;
- mudança material;
- necessidade declarada.

Campanha, estoque, escassez promocional ou meta não constituem urgência funcional.

# 3349. Sensibilidade e privacidade

A capacidade deverá aplicar:

- minimização;
- finalidade específica;
- título neutro;
- prévia protegida;
- autenticação proporcional;
- canal adequado;
- horário apropriado;
- retenção limitada;
- proteção de terceiros;
- bloqueio de publicidade derivada;
- controle de compartilhamento;
- revogação.

# 3350. Fadiga e frequência

Fadiga elevada deverá produzir:

- redução de frequência;
- redução de intensidade;
- agrupamento;
- adiamento;
- canal passivo;
- suspensão;
- silêncio.

Ela nunca deverá justificar aumento de pressão.

# 3351. Temporalidade e canais

A capacidade deverá selecionar canais conforme:

- finalidade;
- urgência;
- sensibilidade;
- atenção;
- interruptibilidade;
- acessibilidade;
- preferência;
- ambiente;
- horário;
- confiabilidade.

Disponibilidade técnica não representa adequação do canal.

# 3352. Autonomia e controles

O participante deverá poder:

- responder;
- solicitar detalhes;
- adiar;
- silenciar;
- recusar;
- ocultar;
- bloquear;
- contestar;
- corrigir;
- revogar;
- controlar categorias;
- controlar canais;
- controlar frequência;
- definir horários protegidos;
- limitar fontes e organizações;
- ativar modo discreto.

# 3353. Autoridade e papéis

Deverão permanecer distintos:

- participante;
- representante;
- fonte;
- avaliador;
- organização;
- profissional;
- patrocinador;
- anunciante;
- sistema;
- executor;
- auditor.

Acesso técnico ou disponibilidade de dados não amplia autoridade funcional.

# 3354. Relações com as capacidades do Journey

A capacidade deverá:

- solicitar informação mínima à Captura de Contexto;
- receber recortes do Contexto Vivo;
- utilizar Objetivos como direção;
- reconhecer mudanças por Eventos de Vida;
- apoiar Próximos Passos sem confirmá-los;
- receber relevância de Oportunidades Ativas;
- apoiar Experiências sem declará-las;
- impedir que frequência de intervenção seja tratada como Evolução Contínua.

Cada capacidade deverá governar sua própria decisão.

# 3355. Guivos Intelligence

Guivos Intelligence poderá:

- detectar candidaturas;
- estimar relevância;
- avaliar temporalidade;
- identificar fadiga;
- sugerir comportamento;
- sugerir canal;
- produzir resumo;
- detectar conflito;
- propor silêncio;
- explicar decisões.

Ela não poderá:

- impor manifestação;
- ignorar preferências;
- fabricar urgência;
- presumir consentimento;
- executar ação material sem contrato;
- explorar vulnerabilidade;
- ampliar autoridade.

# 3356. Platform Layer

A Platform Layer poderá sustentar:

- identidade;
- autorização;
- eventos;
- filas;
- programação;
- entrega;
- confirmação técnica;
- preferências;
- observabilidade;
- auditoria;
- idempotência;
- segurança.

Ela não deverá definir relevância, importância, urgência ou valor humano.

# 3357. Produtos, organizações e profissionais

Produtos especializados deverão governar suas próprias operações.

Organizações e profissionais somente poderão originar comunicações dentro de sua autoridade.

A capacidade deverá impedir:

- acesso irrestrito à jornada;
- transferência de decisão;
- diagnóstico fabricado;
- promessa de resultado;
- obrigação falsa;
- exposição indevida;
- publicidade disfarçada.

# 3358. Neutralidade comercial

A capacidade deverá preservar:

- publicidade identificada;
- Guivos Ads separado das intervenções funcionais;
- patrocínio como metadado;
- comissão sem influência sobre urgência;
- ausência de prioridade baseada em receita;
- contexto sensível fora da segmentação publicitária;
- alternativas não patrocinadas preservadas;
- silêncio sem preenchimento comercial.

# 3359. Privacidade e proteção de terceiros

A capacidade não deverá formar perfil independente de terceiro.

Informações de terceiros somente poderão ser utilizadas quando:

- necessárias;
- legitimamente aplicáveis;
- minimizadas;
- protegidas;
- limitadas à finalidade;
- passíveis de correção e revogação.

# 3360. Confiabilidade

A capacidade deverá operar com:

- contratos versionados;
- persistência antes da publicação;
- idempotência;
- deduplicação semântica;
- ordenação;
- concorrência segura;
- correção compensatória;
- sincronização reconciliável;
- prevenção de ciclos;
- último estado válido;
- degradação controlada;
- falha segura;
- reconstrução.

# 3361. Explicabilidade e auditoria

O participante deverá poder compreender:

- por que a intervenção ocorreu;
- por que ocorreu naquele momento;
- qual comportamento foi selecionado;
- quais dados foram utilizados;
- qual fonte originou;
- qual autoridade existia;
- quais incertezas permaneceram;
- qual relação comercial existia;
- quais consumidores receberam;
- quais efeitos foram produzidos;
- como controlar, contestar ou revogar.

A auditoria deverá reconstruir:

> sinal ou solicitação → candidatura → avaliação → admissão ou silêncio → comportamento → programação → apresentação → entrega → resposta → correção, revogação ou encerramento

# 3362. Contestação, correção e revogação

A contestação deverá limitar efeitos quando material.

A correção deverá ser compensatória e preservar o histórico anterior.

A revogação deverá:

- interromper novos usos;
- bloquear novas manifestações;
- impedir novos compartilhamentos;
- alcançar consumidores relevantes;
- permanecer pendente até propagação suficiente.

# 3363. Critérios de reabertura normativa

A capacidade poderá ser reaberta quando houver:

- nova responsabilidade funcional;
- mudança incompatível de contrato;
- nova categoria de comportamento;
- novo risco material;
- alteração regulatória com efeito arquitetural;
- evidência de lacuna bloqueante;
- nova categoria de participante;
- nova integração estrutural;
- conflito com outra capacidade concluída;
- necessidade de major version.

Implementação técnica, refinamento visual ou definição posterior de metas não exigem reabertura normativa por si mesmos.

# 3364. Regras fundamentais finais

1. Sinal não representa necessidade.
2. Identificação não representa candidatura.
3. Candidatura não representa admissão.
4. Admissão não representa apresentação.
5. Programação não representa entrega.
6. Envio não representa entrega.
7. Entrega não representa visualização.
8. Visualização não representa compreensão.
9. Compreensão não representa concordância.
10. Atenção não representa consentimento.
11. Disponibilidade técnica não representa interruptibilidade.
12. Importância não representa urgência.
13. Urgência comercial não representa urgência funcional.
14. Pergunta não representa obrigação.
15. Sugestão não cria compromisso.
16. Lembrete não cria compromisso novo.
17. Alerta exige fundamento material.
18. Ação material exige autorização.
19. Silêncio é resultado funcional legítimo.
20. Espera não representa abandono.
21. Ausência de resposta não representa recusa.
22. Adiamento não representa rejeição.
23. Recusa não representa fracasso.
24. Fadiga reduz pressão.
25. Horários protegidos prevalecem sobre intervenções não críticas.
26. Conteúdo sensível exige proteção reforçada.
27. Publicidade permanece separada.
28. Comissão não cria urgência.
29. Patrocínio não aumenta prioridade.
30. Contexto sensível não alimenta publicidade.
31. Organizações não recebem a jornada integral.
32. Terceiros não formam perfis paralelos.
33. Produtos especializados governam suas operações.
34. Intervenções Contextuais governa a manifestação, não a transação.
35. Guivos Intelligence pode sugerir, mas não impor.
36. Platform Layer transporta, mas não define relevância humana.
37. Integrações não transferem titularidade.
38. Reprocessamento não duplica efeitos.
39. Eventos fora de ordem não criam estados impossíveis.
40. Conflitos não são sobrescritos silenciosamente.
41. Correções não reescrevem o passado.
42. Revogação somente termina após propagação suficiente.
43. Falha parcial não representa sucesso integral.
44. Métricas avaliam o sistema.
45. O participante permanece no controle.

# 3365. Conclusão e continuidade normativa

`PAS-001-IC-CONTRACT-001 1.0.0` é registrado como a **sexta extensão normativa e o contrato final da Capacidade 07 — Intervenções Contextuais**.

A extensão:

- preserva as cinco extensões anteriores;
- preserva o `PAS-001 0.5.0`;
- mantém as Capacidades 02 a 06 como `Functionally complete`;
- substitui o estado da Capacidade 07 de `In progress` para `Functionally complete`;
- eleva seu progresso editorial de `90%` para `100%`;
- preserva a Capacidade 08 como `Planned`;
- consolida 80 KPIs em 16 famílias;
- consolida 28 guardrails de tolerância zero;
- consolida baseline, painel de saúde e níveis de desempenho;
- consolida cenários ideal, alternativo e limite;
- declara inexistência de lacuna funcional bloqueante conhecida;
- consolida singularidade, titularidade, responsabilidades, limites, entradas, admissão e saídas;
- assegura neutralidade comercial, privacidade, confiabilidade, explicabilidade e auditoria;
- estabelece critérios de reabertura;
- conclui funcionalmente a Capacidade 07.

Após a consolidação, o próximo ponto oficial será:

> **Capacidade 08 — Experiências**, inicialmente com fundamentos, singularidade, definição da experiência vivida, distinção entre atividade, participação, entrega, resultado, satisfação, evidência, memória, significado, transformação e Evento de Vida, além de titularidade, temporalidade, sensibilidade, relações, estados, limites e integrações iniciais.

A Capacidade 08 permanece `Planned` até a aprovação de sua primeira extensão normativa.
