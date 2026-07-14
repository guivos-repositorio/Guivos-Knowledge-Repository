---
id: PAS-001-CV-KPI-001
title: KPIs e Desempenho Funcional do Contexto Vivo
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-13
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-CV-STATE-001
  - PAS-001-CV-UPDATE-001
  - PAS-001-CV-CONFLICT-001
  - PAS-001-CV-VIEW-001
  - PAS-001-CV-EVENT-001
  - PAS-001-CV-INTEGRATION-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-CV-KPI-001 — KPIs e Desempenho Funcional do Contexto Vivo

## 1. Autoridade e vínculo

Este documento é uma **extensão normativa** do `PAS-001 — Guivos Journey Product Architecture Specification`, vinculada à `Capacidade 02 — Contexto Vivo`.

Seu conteúdo deve ser lido como continuidade funcional das seções 28 a 45 do `PAS-001 0.5.0`, das seções 46 a 59 do `PAS-001-CV-STATE-001 1.0.0`, das seções 60 a 83 do `PAS-001-CV-UPDATE-001 1.0.0`, das seções 84 a 113 do `PAS-001-CV-CONFLICT-001 1.0.0`, das seções 114 a 148 do `PAS-001-CV-VIEW-001 1.0.0`, das seções 149 a 208 do `PAS-001-CV-EVENT-001 1.0.0` e das seções 209 a 262 do `PAS-001-CV-INTEGRATION-001 1.0.0`.

A separação documental preserva legibilidade e modularidade sem reduzir sua autoridade arquitetural.

# 263. KPIs, indicadores de qualidade e critérios de desempenho funcional do Contexto Vivo

Os indicadores do Contexto Vivo deverão demonstrar se a Guivos consegue compreender, atualizar, proteger e utilizar o contexto de um participante de forma:

- relevante;
- atual;
- confiável;
- explicável;
- controlável;
- segura;
- proporcional;
- útil para as demais capacidades.

O desempenho do Contexto Vivo não deverá ser medido pela quantidade de informações armazenadas.

> Um Contexto Vivo de qualidade contém somente as informações necessárias, suficientemente atuais e autorizadas para produzir valor ao participante.

# 264. Objetivos da medição

A medição deverá permitir:

1. identificar informações incompletas que prejudiquem a jornada;
2. detectar envelhecimento de elementos relevantes;
3. avaliar a qualidade das atualizações;
4. acompanhar conflitos e contestações;
5. verificar cumprimento de permissões;
6. medir explicabilidade e controle;
7. avaliar esforço exigido do participante;
8. controlar falhas de integração e propagação;
9. medir utilidade para capacidades consumidoras;
10. impedir que crescimento de uso reduza segurança ou qualidade.

# 265. Princípios de mensuração

## 265.1 Qualidade antes de volume

Mais elementos contextuais não significam melhor compreensão.

A medição deverá priorizar:

- adequação;
- atualidade;
- proveniência;
- finalidade;
- utilidade;
- controle.

## 265.2 Medição por finalidade

Uma informação poderá estar adequada para uma finalidade e inadequada para outra.

Exemplo:

> Uma localização informada há três meses poderá ser suficiente para compreender o histórico de uma viagem, mas inadequada para recomendar um evento próximo hoje.

## 265.3 Métricas explicáveis

Todo indicador deverá possuir:

- definição;
- fórmula;
- fonte;
- periodicidade;
- responsável;
- limitações;
- interpretação;
- ação esperada.

## 265.4 Ausência de pontuação humana

Os indicadores deverão avaliar a qualidade da capacidade e de seus processos.

Eles não deverão classificar o valor, caráter, potencial ou qualidade do participante.

## 265.5 Segmentação obrigatória

Resultados agregados deverão ser analisados, quando aplicável, por:

- dimensão;
- origem;
- sensibilidade;
- finalidade;
- capacidade consumidora;
- integração;
- canal;
- tipo de participante;
- região;
- período.

A média geral não deverá ocultar falhas concentradas em grupos específicos.

## 265.6 Indicadores combinados

Nenhum indicador isolado deverá determinar a qualidade integral do Contexto Vivo.

# 266. Unidades de medição

As métricas poderão utilizar diferentes unidades.

| Unidade | Exemplo |
|---|---|
| Participante | pessoas com contexto suficiente para determinada jornada |
| Elemento contextual | objetivo, preferência, restrição ou capacidade |
| Dimensão | Direção, Momento, Restrições ou outra |
| Atualização | tentativa de alterar elemento contextual |
| Conflito | divergência registrada |
| Permissão | autorização por finalidade |
| Integração | fonte interna ou externa |
| Recorte contextual | conjunto enviado a uma capacidade consumidora |
| Evento funcional | fato reconhecido |
| Decisão dependente | recomendação ou ação baseada no contexto |
| Sessão | interação temporal com a Guivos |

O denominador utilizado deverá ser declarado em cada indicador.

# 267. Famílias de indicadores

Os indicadores serão organizados em nove famílias:

1. cobertura e adequação;
2. atualidade e temporalidade;
3. confiança e proveniência;
4. atualização e correção;
5. conflitos;
6. permissões e segurança;
7. transparência e controle;
8. integração e propagação;
9. utilidade funcional.

# 268. Cobertura adequada do contexto

Cobertura não representa preenchimento integral das oito dimensões.

Ela representa a existência de informações suficientes para determinada finalidade.

## 268.1 Taxa de Cobertura Funcional — TCF

```text
TCF =
participantes com contexto suficiente para a finalidade
÷
participantes que tentaram utilizar a finalidade
× 100
```

Exemplos de finalidade:

- construir um Próximo Passo;
- encontrar oportunidade compatível;
- explicar uma recomendação;
- evitar atividade incompatível com restrição.

## 268.2 Interpretação

Uma TCF baixa poderá indicar:

- captura insuficiente;
- integração indisponível;
- exigência excessiva de informações;
- finalidade mal definida;
- critérios de suficiência inadequados.

A solução não deverá ser simplesmente solicitar mais dados.

# 269. Taxa de lacuna crítica

Mede a proporção de jornadas em que uma informação ausente impede uma ação relevante.

```text
TLC =
jornadas bloqueadas por ausência de informação crítica
÷
jornadas avaliadas
× 100
```

A lacuna deverá ser classificada por:

- dimensão;
- finalidade;
- causa;
- possibilidade de alternativa;
- impacto.

Lacunas críticas recorrentes deverão gerar revisão da Captura de Contexto ou do contrato da capacidade consumidora.

# 270. Taxa de excesso contextual

Mede a existência de informações mantidas ou solicitadas sem finalidade ativa.

```text
TEC =
elementos ativos sem finalidade legítima identificada
÷
elementos contextuais ativos
× 100
```

Esse indicador deverá tender ao mínimo possível.

Ele apoia:

- minimização;
- redução de risco;
- simplificação;
- prevenção de perfis excessivos.

# 271. Atualidade funcional

A atualidade deverá ser medida em relação à finalidade.

## 271.1 Taxa de Atualidade Adequada — TAA

```text
TAA =
elementos utilizados dentro do horizonte de atualidade aplicável
÷
elementos utilizados em decisões
× 100
```

## 271.2 Taxa de Uso de Informação Envelhecida — TUIE

```text
TUIE =
decisões que utilizaram elemento envelhecido sem tratamento adequado
÷
decisões que utilizaram contexto
× 100
```

Para decisões críticas, essa taxa deverá possuir tolerância zero quando a informação envelhecida exigir confirmação.

# 272. Elementos críticos próximos de revisão

```text
ECPR =
elementos críticos próximos de revisão
÷
elementos críticos ativos
× 100
```

Esse indicador é preventivo.

Seu crescimento não significa necessariamente falha, mas exige capacidade operacional de revisão sem gerar fadiga.

# 273. Tempo de atualização contextual

## 273.1 Tempo até reconhecimento

Período entre o recebimento de uma informação válida e sua incorporação funcional.

```text
Tempo de reconhecimento =
data da AtualizacaoContextualAplicada
−
data de conhecimento
```

## 273.2 Tempo até disponibilidade

Período entre a atualização aplicada e a disponibilização do novo recorte às capacidades afetadas.

```text
Tempo de propagação =
data da capacidade notificada
−
data da atualização aplicada
```

Os tempos deverão ser analisados por:

- impacto;
- sensibilidade;
- origem;
- capacidade consumidora;
- necessidade de confirmação.

# 274. Classes funcionais de urgência

## Classe A — Imediata

Aplicável a:

- revogação;
- contestação sensível;
- correção de informação crítica;
- restrição de segurança;
- compartilhamento indevido;
- conflito que possa causar prejuízo.

A mudança deverá interromper novos usos antes de qualquer nova decisão dependente.

## Classe B — Prioritária

Aplicável a:

- mudança de objetivo principal;
- disponibilidade que afeta ação próxima;
- integração crítica indisponível;
- oportunidade em andamento.

## Classe C — Regular

Aplicável a:

- complemento;
- preferência de baixo impacto;
- atualização sem decisão imediata;
- informação histórica.

Os prazos técnicos serão definidos posteriormente, mas o comportamento funcional por classe é obrigatório.

# 275. Confiança contextual

## 275.1 Taxa de Elementos com Confiança Adequada — TECA

```text
TECA =
elementos utilizados com confiança suficiente para a finalidade
÷
elementos utilizados
× 100
```

Confiança não deverá ser definida apenas por quantidade de fontes.

Ela deverá considerar:

- natureza da informação;
- fonte;
- confirmação;
- atualidade;
- contexto;
- conflitos;
- evidências.

## 275.2 Taxa de Hipóteses Tratadas como Fato — THTF

```text
THTF =
hipóteses utilizadas como fatos confirmados
÷
hipóteses utilizadas
× 100
```

Esse indicador deverá possuir tolerância zero em decisões críticas.

# 276. Completude de proveniência

## Índice de Proveniência Completa — IPC

```text
IPC =
elementos ativos com origem, data, natureza e finalidade identificadas
÷
elementos ativos
× 100
```

Para elementos utilizados em decisões, o objetivo funcional deverá ser de completude integral.

Informação sem proveniência suficiente não deverá orientar decisão relevante.

# 277. Qualidade das atualizações

## 277.1 Taxa de Atualização Aplicada Corretamente — TAAC

```text
TAAC =
atualizações aplicadas sem correção posterior atribuída ao processo
÷
atualizações aplicadas
× 100
```

## 277.2 Taxa de Reversão — TRV

```text
TRV =
atualizações desfeitas
÷
atualizações aplicadas
× 100
```

Uma taxa elevada poderá indicar:

- confirmação insuficiente;
- interpretação incorreta;
- interface confusa;
- origem inadequada;
- propagação prematura.

A reversão também poderá representar bom controle do participante. Portanto, deverá ser analisada junto ao motivo.

# 278. Taxa de correção pelo participante

```text
TCP =
elementos corrigidos pelo participante
÷
elementos visualizados em Meu Contexto Hoje
× 100
```

Esse indicador não deverá ser interpretado isoladamente como negativo.

Uma taxa inicial maior poderá demonstrar:

- visibilidade;
- facilidade de correção;
- confiança no mecanismo de controle.

O problema ocorre quando as correções se concentram em:

- mesma dimensão;
- mesma fonte;
- mesmo modelo;
- mesmo tipo de inferência;
- mesma capacidade consumidora.

# 279. Taxa de contestação de inferências

```text
TCI =
inferências contestadas
÷
inferências apresentadas ao participante
× 100
```

Deverá ser analisada por:

- tipo de inferência;
- modelo ou processo;
- dimensão;
- confiança declarada;
- impacto;
- sensibilidade.

Uma contestação elevada exige revisão do processo inferencial, não restrição do direito de contestar.

# 280. Conflitos contextuais

## 280.1 Taxa de Conflitos Abertos — TCA

```text
TCA =
conflitos abertos
÷
elementos contextuais ativos
× 100
```

## 280.2 Taxa de Conflitos Críticos — TCC

```text
TCC =
conflitos críticos não resolvidos
÷
conflitos abertos
× 100
```

## 280.3 Tempo de Resolução de Conflito — TRC

```text
TRC =
data de resolução
−
data de identificação
```

Os conflitos deverão ser segmentados por:

- tipo;
- impacto;
- dimensão;
- fonte;
- necessidade de participação;
- resultado.

# 281. Qualidade da resolução de conflitos

## Taxa de Reabertura de Conflitos — TRC2

```text
TRC2 =
conflitos reabertos
÷
conflitos resolvidos
× 100
```

A reabertura poderá indicar:

- nova mudança real;
- evidência posterior;
- resolução inadequada;
- confirmação insuficiente.

O motivo deverá acompanhar o indicador.

# 282. Permissões e finalidade

## 282.1 Taxa de Uso Autorizado — TUA

```text
TUA =
usos com permissão e finalidade válidas
÷
usos de elementos contextuais
× 100
```

O objetivo funcional é `100%`.

## 282.2 Taxa de Uso Não Autorizado — TUNA

```text
TUNA =
usos sem autorização válida
÷
usos contextuais
× 100
```

A tolerância funcional é zero.

Qualquer ocorrência deverá ser tratada como incidente crítico.

# 283. Efetividade de revogação

## 283.1 Taxa de Revogação Propagada — TRP

```text
TRP =
revogações aplicadas a todos os consumidores afetados
÷
revogações registradas
× 100
```

## 283.2 Tempo de Efetivação da Revogação — TER

```text
TER =
data de interrupção completa dos novos usos
−
data efetiva da revogação
```

Enquanto a revogação não estiver totalmente propagada, o sistema deverá:

- suspender usos críticos;
- indicar processamento pendente;
- evitar afirmar conclusão ao participante.

# 284. Incidentes de finalidade

Deverão ser registrados separadamente:

- uso fora da finalidade;
- compartilhamento indevido;
- ampliação silenciosa de autorização;
- retenção além do necessário;
- reconstrução indevida após remoção;
- uso publicitário não autorizado;
- exposição de informação sensível.

Esses incidentes não deverão ser diluídos em métricas médias.

# 285. Transparência de `Meu Contexto Hoje`

## 285.1 Taxa de Explicação Disponível — TED

```text
TED =
elementos utilizados em decisões com explicação acessível
÷
elementos utilizados em decisões
× 100
```

## 285.2 Taxa de Origem Visível — TOV

```text
TOV =
elementos apresentados com origem compreensível
÷
elementos apresentados
× 100
```

## 285.3 Taxa de Ação de Controle Disponível — TACD

```text
TACD =
elementos controláveis com ação adequada disponível
÷
elementos que admitem controle
× 100
```

# 286. Compreensão do participante

A compreensão poderá ser avaliada por perguntas curtas e contextuais.

Exemplos:

- “Você entendeu por que esta informação aparece?”
- “Está claro como ela está sendo utilizada?”
- “Você sabe como corrigir ou limitar esse uso?”

## Índice de Compreensão Contextual — ICC

```text
ICC =
respostas que indicam compreensão suficiente
÷
respostas válidas
× 100
```

Esse indicador deverá ser complementado por testes de usabilidade e comportamento real.

# 287. Taxa de correção concluída

```text
TCCO =
tentativas de correção concluídas funcionalmente
÷
tentativas de correção iniciadas
× 100
```

Falhas deverão ser classificadas por:

- interface;
- regra de negócio;
- confirmação;
- integração;
- propagação;
- erro técnico;
- abandono.

# 288. Esforço para atualização

## 288.1 Tempo de Atualização pelo Participante — TAP

Tempo necessário para confirmar, corrigir ou atualizar um elemento.

## 288.2 Número de Etapas por Ação — NEA

Quantidade de etapas necessárias para executar controle básico.

## 288.3 Taxa de Abandono de Atualização — TAA2

```text
TAA2 =
atualizações iniciadas e não concluídas
÷
atualizações iniciadas
× 100
```

Uma atualização sensível poderá exigir mais etapas, mas deverá permanecer compreensível.

# 289. Fadiga de confirmação

## Índice de Solicitações de Revisão — ISR

```text
ISR =
solicitações de confirmação ou revisão
÷
participantes ativos no período
```

O indicador deverá ser analisado junto a:

- taxa de resposta;
- adiamento;
- abandono;
- repetição;
- relevância da solicitação;
- momento da jornada.

Mais confirmações não significam melhor qualidade.

# 290. Taxa de repetição desnecessária

```text
TRD =
perguntas sobre informação já vigente e suficiente
÷
perguntas contextuais realizadas
× 100
```

Essa taxa deverá ser reduzida continuamente.

Ela indica falha de:

- integração;
- sincronização;
- recuperação de contexto;
- desenho conversacional;
- definição de suficiência.

# 291. Qualidade das integrações

## 291.1 Taxa de Integrações Saudáveis — TIS

```text
TIS =
integrações operando dentro do contrato funcional
÷
integrações ativas
× 100
```

## 291.2 Taxa de Associação Incorreta — TAI

```text
TAI =
informações associadas ao participante incorreto
÷
informações integradas
× 100
```

A tolerância deverá ser zero para associações confirmadas incorretamente.

## 291.3 Taxa de Dados Rejeitados — TDR

```text
TDR =
entradas rejeitadas por invalidade, falta de autorização ou baixa qualidade
÷
entradas recebidas
× 100
```

Essa métrica poderá demonstrar proteção adequada, não necessariamente falha.

# 292. Falhas e degradação controlada

## Taxa de Falha Segura — TFS

```text
TFS =
falhas tratadas sem produzir decisão indevida
÷
falhas funcionais relevantes
× 100
```

Exemplos de tratamento seguro:

- suspensão de decisão;
- solicitação de confirmação;
- uso do último contexto ainda válido;
- alternativa manual;
- transparência sobre indisponibilidade.

# 293. Propagação contextual

## 293.1 Taxa de Consumidores Atualizados — TCA2

```text
TCA2 =
capacidades consumidoras atualizadas após mudança relevante
÷
capacidades que deveriam ser atualizadas
× 100
```

## 293.2 Taxa de Recortes Coerentes — TRC3

```text
TRC3 =
recortes compatíveis com contexto, finalidade e permissão vigentes
÷
recortes fornecidos
× 100
```

## 293.3 Taxa de Efeito Duplicado — TED2

```text
TED2 =
efeitos funcionais duplicados pelo reprocessamento do mesmo evento
÷
eventos reprocessados
× 100
```

A tolerância deverá ser zero para efeitos críticos duplicados.

# 294. Utilidade para capacidades consumidoras

O Contexto Vivo deverá ser avaliado também pela capacidade de apoiar decisões melhores.

## 294.1 Taxa de Recortes Utilizáveis — TRU

```text
TRU =
recortes aceitos como suficientes pela capacidade consumidora
÷
recortes solicitados
× 100
```

## 294.2 Taxa de Reconsulta por Insuficiência — TRI

```text
TRI =
recortes que exigiram nova consulta por ausência de informação necessária
÷
recortes fornecidos
× 100
```

A capacidade consumidora deverá justificar quais elementos faltaram.

# 295. Relevância das decisões apoiadas

## Taxa de Decisões Contextualmente Adequadas — TDCA

```text
TDCA =
decisões avaliadas como compatíveis com o contexto vigente
÷
decisões baseadas no Contexto Vivo
× 100
```

A avaliação poderá utilizar:

- aceitação pelo participante;
- justificativa de recusa;
- correção posterior;
- incompatibilidade detectada;
- evidência de restrição ignorada;
- revisão pela capacidade responsável.

Aceitação não significa necessariamente adequação, e recusa não significa necessariamente inadequação.

# 296. Exclusão indevida de oportunidades

## Taxa de Exclusão Contextual Indevida — TECI

```text
TECI =
oportunidades relevantes excluídas por contexto incorreto, incerto ou excessivo
÷
oportunidades excluídas por regras contextuais
× 100
```

Esse indicador é um guardrail central.

O Contexto Vivo deverá evitar tanto recomendações incompatíveis quanto bloqueios excessivos.

# 297. Taxa de incompatibilidade não detectada

```text
TIND =
oportunidades apresentadas com incompatibilidade contextual relevante
÷
oportunidades apresentadas com uso do Contexto Vivo
× 100
```

Exemplos:

- horário incompatível;
- restrição ignorada;
- localização inadequada;
- finalidade não autorizada;
- condição sensível desconsiderada.

# 298. Indicadores de equilíbrio funcional

A qualidade exige equilíbrio entre objetivos potencialmente conflitantes.

| Dimensão de equilíbrio | Risco de excesso |
|---|---|
| Cobertura | coleta excessiva |
| Atualidade | fadiga de confirmação |
| Personalização | uso invasivo |
| Segurança | bloqueio excessivo |
| Automação | perda de controle |
| Explicabilidade | sobrecarga de informação |
| Integração | dependência externa |
| Histórico | retenção desnecessária |

Os indicadores deverão ser avaliados em conjunto para evitar otimização unilateral.

# 299. Indicadores de justiça e consistência

O desempenho deverá ser comparado entre grupos e contextos, sem utilizar características sensíveis de forma indevida.

Deverão ser observadas diferenças em:

- taxa de correção;
- conflitos;
- exclusão de oportunidades;
- atualidade;
- compreensão;
- falhas de integração;
- tempo de resolução;
- disponibilidade de explicação;
- incidência de inferências contestadas.

Diferenças significativas deverão gerar investigação de:

- linguagem;
- acessibilidade;
- cobertura de integrações;
- viés de fonte;
- regras inferenciais;
- disponibilidade regional;
- comportamento da capacidade consumidora.

# 300. Indicadores que não deverão ser utilizados isoladamente

Não deverão determinar a qualidade do Contexto Vivo de forma isolada:

- quantidade de dimensões preenchidas;
- número de elementos armazenados;
- frequência de acesso;
- tempo de permanência em `Meu Contexto Hoje`;
- número de integrações conectadas;
- volume de inferências;
- quantidade de notificações;
- taxa de aceitação de recomendações;
- quantidade de dados sensíveis disponíveis.

Essas métricas podem representar atividade, mas não necessariamente valor ou qualidade.

# 301. Guardrails obrigatórios

Os seguintes critérios possuem caráter de proteção obrigatória:

| Guardrail | Tolerância funcional |
|---|---|
| Uso sem autorização | Zero |
| Ampliação silenciosa de finalidade | Zero |
| Informação sensível inferida e ativada sem base adequada | Zero |
| Hipótese utilizada como fato em decisão crítica | Zero |
| Revogação ignorada em novo uso | Zero |
| Efeito crítico duplicado | Zero |
| Ocultação de conflito relevante | Zero |
| Decisão crítica baseada em informação expirada sem tratamento | Zero |
| Exposição indevida de informação de terceiro | Zero |
| Associação confirmada ao participante incorreto | Zero |

Qualquer ocorrência deverá gerar incidente, investigação e correção.

# 302. Níveis de desempenho funcional

## 302.1 Inadequado

Quando existir:

- violação de guardrail;
- uso recorrente de contexto envelhecido;
- falta de explicabilidade;
- correções não propagadas;
- conflitos críticos ocultos;
- elevada exclusão indevida;
- perda de controle do participante.

## 302.2 Parcialmente adequado

Quando:

- os contratos centrais são respeitados;
- ainda existem lacunas relevantes;
- a propagação apresenta atrasos;
- a compreensão varia entre grupos;
- integrações possuem degradação recorrente;
- processos manuais compensam limitações.

## 302.3 Adequado

Quando:

- guardrails são respeitados;
- elementos críticos estão atuais;
- proveniência e finalidade são preservadas;
- correções e revogações propagam corretamente;
- explicações estão disponíveis;
- o esforço do participante é proporcional;
- recortes apoiam decisões coerentes.

## 302.4 Maduro

Quando, além do estado adequado:

- falhas são detectadas preventivamente;
- revisões ocorrem em momentos naturais;
- conflitos são resolvidos com baixo esforço;
- diferenças entre grupos são monitoradas;
- integrações degradam com segurança;
- a qualidade melhora sem ampliar coleta indevida.

# 303. Metas e thresholds

As metas numéricas deverão ser estabelecidas após:

1. protótipo funcional;
2. teste de usabilidade;
3. piloto controlado;
4. baseline comportamental;
5. análise por segmento;
6. validação de capacidade operacional.

Antes da baseline, somente os guardrails de tolerância zero serão normativos.

As demais métricas deverão possuir:

- valor observado;
- faixa esperada;
- tendência;
- limite de alerta;
- limite crítico;
- plano de ação.

# 304. Frequência de acompanhamento

| Indicador | Frequência sugerida |
|---|---|
| Violações de permissão | Contínua |
| Revogações pendentes | Contínua |
| Conflitos críticos | Diária |
| Propagação de atualizações | Diária |
| Atualidade de elementos críticos | Semanal |
| Falhas de integração | Semanal |
| Correções e contestações | Semanal ou mensal |
| Compreensão e esforço | Por rodada de pesquisa |
| Justiça e consistência | Mensal ou trimestral |
| Cobertura funcional | Por capacidade e ciclo de produto |

A frequência final dependerá do risco e volume operacional.

# 305. Fontes de medição

Os indicadores poderão ser calculados a partir de eventos como:

- `AtualizacaoContextualProposta`;
- `AtualizacaoContextualAplicada`;
- `InformacaoConfirmada`;
- `InformacaoCorrigida`;
- `InformacaoContestada`;
- `InformacaoEnvelhecida`;
- `ConflitoIdentificado`;
- `ConflitoResolvido`;
- `ConflitoReaberto`;
- `PermissaoAlterada`;
- `PermissaoRevogada`;
- `RecorteContextualRecomposto`;
- `CapacidadeConsumidoraNotificada`;
- `DecisaoDependenteReavaliada`;
- `ExplicacaoSolicitada`;
- `AlteracaoDesfeita`;
- `ProcessamentoFuncionalFalhou`.

Eventos não deverão ser criados apenas para melhorar indicadores.

# 306. Governança dos indicadores

Cada KPI deverá possuir:

- proprietário funcional;
- responsável operacional;
- fonte oficial;
- regra de cálculo;
- periodicidade;
- segmentações;
- limites de interpretação;
- critérios de alerta;
- plano de resposta;
- histórico de mudanças;
- versão.

Mudanças de fórmula deverão ser versionadas para preservar comparabilidade.

# 307. Painel de saúde do Contexto Vivo

O painel principal deverá apresentar, no mínimo:

## Qualidade

- cobertura funcional;
- atualidade;
- confiança;
- proveniência;
- conflitos.

## Controle

- correções;
- contestações;
- revogações;
- compreensão;
- esforço.

## Segurança

- incidentes;
- violações de finalidade;
- informações sensíveis;
- exclusões indevidas;
- associações incorretas.

## Operação

- tempo de atualização;
- propagação;
- falhas de integração;
- degradação segura;
- efeitos duplicados.

## Valor

- recortes utilizáveis;
- decisões adequadas;
- incompatibilidades detectadas;
- oportunidades indevidamente excluídas.

O painel deverá permitir aprofundamento por dimensão, fonte, finalidade e capacidade consumidora.

# 308. Índice composto de saúde

Poderá existir um **Índice de Saúde do Contexto Vivo — ISCV** para acompanhamento executivo.

Ele não deverá substituir os indicadores componentes.

Uma estrutura inicial poderá agrupar:

```text
ISCV =
qualidade contextual
+ controle do participante
+ segurança
+ desempenho operacional
+ utilidade funcional
```

Os pesos somente deverão ser definidos após baseline real.

Violações de guardrail deverão impedir classificação positiva, independentemente da média composta.

# 309. Critérios de aceite funcional

A medição do Contexto Vivo será considerada adequada quando:

1. avaliar qualidade, e não volume de dados;
2. possuir denominadores claros;
3. diferenciar finalidade e impacto;
4. medir atualidade e proveniência;
5. identificar hipóteses tratadas como fatos;
6. acompanhar correções e contestações;
7. medir conflitos e reaberturas;
8. controlar permissões e revogações;
9. avaliar explicabilidade e compreensão;
10. medir esforço e fadiga;
11. controlar integrações e propagação;
12. detectar efeitos duplicados;
13. medir utilidade para capacidades consumidoras;
14. detectar exclusões indevidas;
15. segmentar resultados para não ocultar desigualdades;
16. possuir guardrails de tolerância zero;
17. evitar metas que incentivem coleta excessiva;
18. versionar fórmulas e interpretações;
19. associar alertas a ações concretas;
20. preservar a centralidade do participante.

# 310. Regras fundamentais de desempenho

1. O Contexto Vivo não será melhor por conter mais informações.
2. Cobertura deverá ser avaliada por finalidade.
3. Atualidade deverá ser proporcional ao impacto.
4. Informação sem proveniência suficiente não deverá orientar decisão relevante.
5. Hipótese não é fato.
6. Contestação não é falha do participante.
7. Correções deverão ser propagadas.
8. Revogações deverão interromper novos usos.
9. Segurança não poderá ser compensada por médias positivas.
10. Explicabilidade deverá acompanhar decisões relevantes.
11. A redução de esforço não poderá eliminar controles necessários.
12. Integrações deverão falhar com segurança.
13. O sistema deverá medir exclusões indevidas, não apenas recomendações inadequadas.
14. Métricas não deverão incentivar coleta excessiva ou manipulação comportamental.
15. O desempenho será adequado somente quando produzir valor sob controle do participante.

Com isso, ficam definidos os **KPIs, indicadores de qualidade e critérios de desempenho funcional do Contexto Vivo**.

O próximo bloco da Capacidade 02 é a definição dos **cenários funcionalmente ideal, alternativo e limite**, seguida pela consolidação do **contrato final da capacidade**.
