---
id: PAS-001-CV-EVENT-001
title: Contratos dos Eventos Funcionais do Contexto Vivo
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
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-CV-EVENT-001 — Contratos dos Eventos Funcionais do Contexto Vivo

## 1. Autoridade e vínculo

Este documento é uma **extensão normativa** do `PAS-001 — Guivos Journey Product Architecture Specification`, vinculada à `Capacidade 02 — Contexto Vivo`.

Seu conteúdo deve ser lido como continuidade funcional das seções 28 a 45 do `PAS-001 0.5.0`, das seções 46 a 59 do `PAS-001-CV-STATE-001 1.0.0`, das seções 60 a 83 do `PAS-001-CV-UPDATE-001 1.0.0`, das seções 84 a 113 do `PAS-001-CV-CONFLICT-001 1.0.0` e das seções 114 a 148 do `PAS-001-CV-VIEW-001 1.0.0`.

A separação documental preserva legibilidade e modularidade sem reduzir sua autoridade arquitetural.

# 149. Contratos detalhados dos eventos funcionais do Contexto Vivo

Os eventos funcionais do Contexto Vivo representam fatos relevantes ocorridos na compreensão, atualização, utilização ou governança do contexto de um participante.

Um evento deverá registrar que algo **aconteceu**, e não somente que algo foi solicitado ou pretendido.

Exemplo:

```text
Solicitação:
Confirmar disponibilidade atual
```

```text
Evento:
InformacaoConfirmada
```

> Eventos funcionais preservam o que aconteceu, quando aconteceu, com qual base e quais efeitos foram produzidos.

Eles não determinam, por si mesmos:

- tecnologia de mensageria;
- banco de dados;
- estrutura de filas;
- linguagem de programação;
- formato físico de armazenamento;
- fornecedor de infraestrutura.

# 150. Diferença entre comando, proposta e evento

## 150.1 Comando

Expressa uma intenção de realizar uma ação.

Exemplos:

- confirmar informação;
- atualizar objetivo;
- revogar permissão;
- corrigir disponibilidade;
- encerrar restrição.

Um comando poderá ser aceito, rejeitado, adiado ou exigir confirmação adicional.

## 150.2 Proposta

Expressa uma possível compreensão ou atualização ainda não consolidada.

Exemplos:

- possível mudança de prioridade;
- possível preferência;
- possível conflito;
- possível encerramento de restrição;
- possível Evento de Vida.

## 150.3 Evento

Expressa um fato funcional já reconhecido.

Exemplos:

- `InformacaoConfirmada`;
- `AtualizacaoContextualAplicada`;
- `ConflitoIdentificado`;
- `PermissaoRevogada`;
- `InformacaoEnvelhecida`.

O fluxo poderá ser:

```text
Comando ou sinal
→ avaliação
→ proposta
→ confirmação ou regra aplicável
→ alteração reconhecida
→ evento funcional
```

# 151. Princípios dos eventos funcionais

## 151.1 Fato ocorrido

O nome do evento deverá representar algo que já aconteceu.

Preferir:

```text
InformacaoCorrigida
```

em vez de:

```text
CorrigirInformacao
```

## 151.2 Imutabilidade histórica

Um evento já reconhecido não deverá ser reescrito para representar uma compreensão posterior.

Caso exista erro, deverá ser produzido outro evento que registre:

- correção;
- contestação;
- substituição;
- anulação funcional;
- mudança real.

## 151.3 Temporalidade explícita

O evento deverá distinguir:

- quando o fato ocorreu;
- quando a Guivos tomou conhecimento;
- quando o evento foi registrado;
- desde quando a mudança passou a valer.

## 151.4 Proveniência

Todo evento deverá indicar sua origem funcional.

## 151.5 Finalidade e autorização

Um evento não deverá ampliar automaticamente as finalidades autorizadas para utilização da informação.

## 151.6 Informação mínima

O evento deverá conter somente as informações necessárias para produzir seus efeitos.

Dados sensíveis deverão, sempre que possível, permanecer protegidos no elemento contextual original, sendo referenciados pelo evento em vez de replicados.

## 151.7 Explicabilidade

Eventos relevantes deverão sustentar explicações futuras ao participante.

## 151.8 Reprocessamento seguro

Uma capacidade consumidora deverá conseguir reconhecer quando já processou determinado evento, evitando produzir o mesmo efeito funcional repetidamente.

# 152. Estrutura comum de um evento

Todo evento funcional deverá possuir um conjunto mínimo de atributos.

| Atributo | Finalidade |
|---|---|
| Identificador do evento | Distinguir o fato ocorrido |
| Tipo do evento | Indicar sua natureza |
| Versão do contrato | Permitir evolução controlada |
| Participante relacionado | Identificar a jornada afetada |
| Data do fato | Informar quando ocorreu no mundo real |
| Data de conhecimento | Informar quando a Guivos tomou conhecimento |
| Data de registro | Informar quando o evento foi reconhecido |
| Origem | Indicar quem ou o que produziu a informação |
| Ator | Identificar quem iniciou ou confirmou a ação |
| Elementos afetados | Limitar o escopo da alteração |
| Dimensões afetadas | Identificar impactos dimensionais |
| Estado anterior relevante | Preservar o ponto de partida |
| Novo estado relevante | Registrar o resultado |
| Motivo | Explicar por que o evento ocorreu |
| Evidências | Indicar a base da decisão |
| Confiança | Representar a força da compreensão |
| Sensibilidade | Aplicar proteção proporcional |
| Finalidade | Limitar os usos permitidos |
| Permissões | Registrar controles aplicáveis |
| Correlação | Relacionar eventos da mesma jornada funcional |
| Causa imediata | Indicar o evento ou ação que produziu este evento |
| Impactos previstos | Informar capacidades e decisões potencialmente afetadas |
| Explicação resumida | Sustentar transparência ao participante |

Nem todos os atributos deverão ser expostos diretamente na interface.

# 153. Identidade e correlação

## 153.1 Identificador do evento

Cada evento deverá possuir identificação única.

## 153.2 Identificador de correlação

Eventos que façam parte do mesmo fluxo deverão ser relacionados.

Exemplo:

```text
Mudança profissional declarada
→ Momento atualizado
→ Identidade em transição
→ Objetivo possivelmente impactado
→ Recorte contextual recomposto
```

## 153.3 Identificador de causa

O evento deverá indicar, quando aplicável, qual ação ou evento produziu diretamente sua ocorrência.

Isso permitirá diferenciar:

- causa inicial;
- efeitos derivados;
- reprocessamentos;
- consequências posteriores.

# 154. Ordenação funcional

Não será necessária uma ordem universal entre todos os eventos da Guivos.

Deverá existir ordem funcional suficiente para compreender:

- a evolução de cada participante;
- a evolução de cada elemento contextual;
- a sequência de um conflito;
- a alteração de uma permissão;
- a progressão de uma atualização;
- os efeitos sobre uma decisão.

Quando dois eventos não puderem ser ordenados com segurança, o sistema deverá preservar essa incerteza.

# 155. Versionamento dos contratos

Cada tipo de evento deverá possuir uma versão de contrato.

Uma nova versão será necessária quando houver alteração incompatível em:

- significado;
- atributos obrigatórios;
- regras de interpretação;
- efeitos funcionais;
- restrições de uso.

Novos atributos opcionais poderão ser adicionados sem alterar o significado central, desde que consumidores anteriores permaneçam capazes de compreender o evento.

Um evento antigo deverá continuar sendo interpretado conforme a versão vigente no momento de sua produção.

# 156. Categorias de eventos

Os eventos do Contexto Vivo serão organizados em sete grupos.

| Grupo | Finalidade |
|---|---|
| Atualização contextual | Registrar propostas, aplicações e alterações |
| Confirmação e revisão | Controlar atualidade e participação da pessoa |
| Temporalidade | Registrar envelhecimento, expiração e arquivamento |
| Conflitos | Preservar divergências e suas resoluções |
| Permissões e integrações | Controlar autorização, finalidade e fontes externas |
| Recortes e propagação | Informar capacidades consumidoras |
| Interação e transparência | Registrar ações em `Meu Contexto Hoje` |

Eventos de interação não deverão ser automaticamente tratados como evidências de mudança contextual.

# 157. Contrato de `AtualizacaoContextualProposta`

## Finalidade

Registrar que uma possível alteração foi identificada, mas ainda não foi incorporada ao Contexto Vivo.

## Gatilhos

- inferência da Intelligence Layer;
- comportamento recorrente;
- integração externa;
- Evento de Vida ainda não confirmado;
- conflito que indique possível mudança;
- informação incompleta.

## Conteúdo mínimo

- elemento possivelmente afetado;
- dimensão;
- estado atual;
- mudança proposta;
- origem;
- evidências;
- confiança;
- impacto;
- necessidade de confirmação;
- validade da proposta.

## Efeito funcional

Nenhuma alteração definitiva deverá ocorrer.

A proposta poderá:

- aguardar confirmação;
- receber novas evidências;
- ser descartada;
- ser transformada em conflito;
- ser aplicada por regra de baixo impacto.

# 158. Contrato de `AtualizacaoContextualAplicada`

## Finalidade

Registrar que uma mudança foi validada e incorporada ao Contexto Vivo.

## Conteúdo mínimo

- elemento alterado;
- estado anterior;
- novo estado;
- tipo de alteração;
- data de início de validade;
- base da alteração;
- confirmação utilizada;
- permissões aplicáveis;
- capacidades potencialmente afetadas.

## Efeito funcional

- atualizar a dimensão correspondente;
- preservar o estado anterior;
- recalcular a síntese contextual;
- avaliar propagação;
- reavaliar decisões dependentes;
- disponibilizar explicação ao participante.

# 159. Contrato de `AtualizacaoContextualRejeitada`

## Finalidade

Registrar que uma proposta de atualização não foi aceita.

## Motivos possíveis

- contestação do participante;
- falta de autorização;
- evidência insuficiente;
- origem inadequada;
- duplicidade;
- interpretação incorreta;
- conflito ainda não resolvido;
- ausência de relevância;
- expiração da proposta.

## Efeito funcional

A proposta rejeitada não deverá alterar o contexto vigente.

Inferências dependentes deverão ser revistas.

# 160. Contrato de `InformacaoConfirmada`

## Finalidade

Registrar que o participante ou uma fonte autorizada confirmou a vigência de uma informação.

## Conteúdo mínimo

- elemento confirmado;
- ator da confirmação;
- data;
- finalidade;
- escopo da confirmação;
- validade estimada;
- confiança resultante.

## Efeito funcional

- atualizar a última confirmação;
- elevar ou manter confiança;
- recalcular horizonte de revisão;
- encerrar solicitação de confirmação relacionada;
- preservar histórico.

A confirmação para uma finalidade não deverá ser interpretada como autorização universal.

# 161. Contrato de `InformacaoComplementada`

## Finalidade

Registrar a adição de detalhes que não substituem o significado principal do elemento.

Exemplo:

```text
Preferência:
atividades coletivas
```

complementada por:

```text
principalmente aos finais de semana
```

## Efeito funcional

O elemento anterior permanece válido e recebe maior especificidade.

# 162. Contrato de `InformacaoCorrigida`

## Finalidade

Registrar que uma informação anterior estava incorreta.

## Conteúdo mínimo

- informação incorreta;
- informação correta;
- origem do erro;
- data da correção;
- decisões potencialmente afetadas;
- necessidade de reparação funcional.

## Efeito funcional

- impedir novos usos da informação incorreta;
- atualizar recortes contextuais;
- reavaliar decisões relevantes;
- preservar que a Guivos utilizou anteriormente uma informação incorreta;
- diferenciar correção de mudança real.

# 163. Contrato de `MudancaContextualDeclarada`

## Finalidade

Registrar que o participante informou uma mudança real em seu contexto.

## Conteúdo mínimo

- estado anterior;
- nova condição;
- data efetiva da mudança;
- dimensões possivelmente afetadas;
- nível de detalhe autorizado;
- efeitos esperados.

## Efeito funcional

A declaração deverá iniciar avaliações seletivas sobre os elementos relacionados.

Ela não deverá atualizar automaticamente todas as dimensões potencialmente afetadas.

# 164. Contrato de `InformacaoSubstituida`

## Finalidade

Registrar que uma nova informação passou a representar a condição atual.

## Efeito funcional

- tornar a nova informação vigente;
- transformar a anterior em histórica;
- manter sequência temporal;
- reprocessar recortes e decisões dependentes.

A substituição não significa que a informação anterior estava errada.

# 165. Contrato de `InformacaoEncerrada`

## Finalidade

Registrar que uma condição deixou de existir ou deixou de ser aplicável.

Exemplos:

- restrição resolvida;
- objetivo concluído;
- disponibilidade temporária encerrada;
- vínculo encerrado.

## Efeito funcional

A informação deixa de orientar novas decisões, permanecendo disponível no histórico conforme autorização e necessidade legítima.

# 166. Contrato de `InformacaoSuspensa`

## Finalidade

Registrar que um elemento permanece relevante, mas não deverá orientar ações temporariamente.

Exemplos:

- objetivo pausado;
- preferência temporariamente desconsiderada;
- uso suspenso durante conflito;
- integração pausada.

## Conteúdo mínimo

- motivo;
- início da suspensão;
- condição de revisão;
- usos interrompidos;
- histórico preservado.

# 167. Contrato de `InformacaoContestada`

## Finalidade

Registrar que o participante rejeitou ou questionou uma informação ou interpretação.

## Efeito imediato

- reduzir ou suspender seu uso;
- impedir decisões críticas dependentes;
- iniciar correção, explicação ou resolução de conflito;
- preservar a contestação;
- informar capacidades consumidoras relevantes.

A contestação não deverá depender de comprovação pelo participante.

# 168. Contrato de `ConfirmacaoSolicitada`

## Finalidade

Registrar que uma informação precisa ser confirmada antes de determinado uso ou decisão.

## Conteúdo mínimo

- elemento;
- motivo da confirmação;
- impacto;
- prazo ou contexto de necessidade;
- possibilidade de adiamento;
- efeito da ausência de resposta.

## Efeito funcional

A solicitação não altera o contexto.

# 169. Contrato de `RevisaoNecessaria`

## Finalidade

Registrar que um elemento perdeu atualidade, completude ou confiança suficiente para determinada finalidade.

## Motivos possíveis

- passagem do tempo;
- Evento de Vida;
- evidência divergente;
- condição temporária;
- conflito;
- mudança de finalidade;
- decisão crítica dependente.

## Efeito funcional

O uso poderá:

- continuar com cautela;
- ser limitado;
- ser suspenso;
- exigir confirmação.

# 170. Contrato de `RevisaoAdiada`

## Finalidade

Registrar que o participante optou por revisar a informação posteriormente.

## Conteúdo mínimo

- elemento;
- data do adiamento;
- nova condição de revisão;
- usos que poderão continuar;
- usos que permanecerão suspensos.

Adiar não significa confirmar.

# 171. Contrato de `InformacaoProximaDeRevisao`

## Finalidade

Sinalizar aproximação do horizonte de revisão.

## Efeito funcional

- preparar solicitação contextual;
- evitar surpresa;
- permitir revisão agrupada;
- não reduzir automaticamente a validade atual.

# 172. Contrato de `InformacaoEnvelhecida`

## Finalidade

Registrar perda relevante de segurança temporal.

## Efeito funcional

- reduzir confiança de atualidade;
- limitar decisões de alto impacto;
- gerar revisão;
- indicar incerteza nos recortes contextuais.

O evento não declara que a informação se tornou falsa.

# 173. Contrato de `InformacaoExpirada`

## Finalidade

Registrar que a validade conhecida chegou ao fim.

Exemplos:

- autorização temporária;
- restrição com data definida;
- disponibilidade de período específico;
- integração com prazo limitado.

## Efeito funcional

A informação deixa de orientar o contexto atual, salvo nova confirmação ou regra legítima.

# 174. Contrato de `InformacaoArquivada`

## Finalidade

Registrar que uma informação deixou o contexto operacional.

## Efeito funcional

Ela poderá permanecer somente para:

- histórico;
- explicabilidade;
- auditoria legítima;
- obrigações aplicáveis.

Informação arquivada não deverá ser entregue como parte do contexto vigente.

# 175. Contrato de `ConflitoIdentificado`

## Finalidade

Registrar a existência de informações incompatíveis ou insuficientemente contextualizadas.

## Conteúdo mínimo

- elementos envolvidos;
- tipo de conflito;
- fontes;
- temporalidades;
- dimensões;
- impacto potencial;
- usos temporariamente permitidos;
- usos suspensos.

## Efeito funcional

Capacidades consumidoras deverão receber indicação de incerteza quando o conflito afetar suas decisões.

# 176. Contrato de `ConflitoClassificado`

## Finalidade

Registrar a natureza funcional do conflito.

Classes possíveis:

- direto;
- temporal;
- contextual;
- entre fontes;
- entre declaração e comportamento;
- entre fato e inferência;
- semântico;
- de granularidade;
- entre dimensões;
- de permissão;
- de sensibilidade;
- de evolução.

A classificação poderá ser revista posteriormente.

# 177. Contrato de `ConflitoContextualizado`

## Finalidade

Registrar que informações aparentemente incompatíveis foram diferenciadas por contexto.

Exemplo:

- preferência por experiência online em estudos;
- preferência por experiência presencial em esportes.

## Efeito funcional

As informações poderão coexistir sem redução indevida de confiança.

# 178. Contrato de `ConflitoTemporalmenteSequenciado`

## Finalidade

Registrar que informações diferentes representam períodos sucessivos.

## Conteúdo mínimo

- estado anterior;
- período de validade;
- nova condição;
- momento da mudança;
- data em que a Guivos tomou conhecimento.

# 179. Contrato de `ConflitoAguardandoConfirmacao`

## Finalidade

Registrar que a resolução depende de manifestação do participante ou de fonte autorizada.

## Efeito funcional

Decisões de alto impacto deverão permanecer suspensas quando dependerem diretamente do conflito.

# 180. Contrato de `ConflitoResolvido`

## Finalidade

Registrar a conclusão funcional de um conflito.

## Resultado possível

- coexistência contextual;
- sequenciamento temporal;
- correção;
- substituição;
- prevalência por finalidade;
- suspensão de uso;
- descarte;
- redução de confiança.

## Conteúdo mínimo

- resolução adotada;
- justificativa;
- ator ou regra responsável;
- informações preservadas;
- usos liberados;
- usos limitados;
- decisões reavaliadas;
- possibilidade de reabertura.

# 181. Contrato de `ConflitoReaberto`

## Finalidade

Registrar que uma resolução anterior deixou de ser suficiente.

## Gatilhos

- nova evidência;
- contestação;
- mudança de permissão;
- correção da fonte;
- mudança real;
- nova finalidade;
- erro na resolução anterior.

A resolução anterior deverá permanecer no histórico.

# 182. Contrato de `UsoSuspensoPorConflito`

## Finalidade

Registrar que determinada informação deixou temporariamente de orientar uma finalidade específica.

## Conteúdo mínimo

- elemento;
- conflito;
- finalidade suspensa;
- capacidades afetadas;
- condição de retomada.

O elemento poderá continuar sendo utilizado para outras finalidades autorizadas e não afetadas.

# 183. Contrato de `PermissaoAlterada`

## Finalidade

Registrar qualquer mudança de autorização associada a um elemento contextual.

## Tipos de alteração

- concessão;
- ampliação;
- redução;
- limitação;
- revogação;
- expiração;
- mudança de duração;
- mudança de destinatário.

## Efeito funcional

Recortes contextuais e capacidades consumidoras deverão ser reavaliados imediatamente.

# 184. Contrato de `PermissaoRevogada`

## Finalidade

Registrar que determinado uso deixou de ser autorizado.

## Conteúdo mínimo

- informação afetada;
- finalidade revogada;
- capacidades consumidoras;
- data efetiva;
- efeitos sobre decisões;
- regras de retenção aplicáveis.

## Efeito funcional

- interromper novos usos;
- impedir novos compartilhamentos;
- recompor recortes;
- reavaliar inferências dependentes;
- informar impactos ao participante.

# 185. Contrato de `IntegracaoAutorizada`

## Finalidade

Registrar a autorização de uma fonte externa.

## Conteúdo mínimo

- integração;
- dados permitidos;
- finalidades;
- duração;
- frequência esperada;
- sensibilidade;
- possibilidade de revogação;
- efeitos esperados no Contexto Vivo.

A autorização da integração não representa autorização irrestrita de todos os dados disponíveis.

# 186. Contrato de `IntegracaoPausada`

## Finalidade

Registrar interrupção temporária de novas coletas ou usos.

## Efeito funcional

- interromper novas atualizações;
- preservar autorização conforme regra aplicável;
- manter fatos legítimos anteriormente registrados;
- informar elementos que poderão envelhecer.

# 187. Contrato de `IntegracaoRevogada`

## Finalidade

Registrar encerramento da autorização da integração.

## Efeito funcional

- interromper coleta;
- interromper novos usos;
- reavaliar elementos derivados;
- preservar ou remover informações conforme autorização, finalidade e retenção legítima;
- atualizar `Meu Contexto Hoje`.

# 188. Contrato de `RecorteContextualRecomposto`

## Finalidade

Registrar que o conjunto de informações fornecido a uma capacidade consumidora foi alterado.

## Gatilhos

- atualização contextual;
- correção;
- conflito;
- envelhecimento;
- revogação;
- nova finalidade;
- mudança de sensibilidade;
- substituição de elemento.

## Conteúdo mínimo

- capacidade consumidora;
- finalidade;
- versão anterior do recorte;
- nova composição;
- elementos adicionados;
- elementos removidos;
- incertezas;
- validade.

O evento não deverá expor dados além do necessário para a finalidade da capacidade consumidora.

# 189. Contrato de `CapacidadeConsumidoraNotificada`

## Finalidade

Registrar que uma capacidade foi informada de mudança relevante.

## Exemplos de consumidoras

- Objetivos;
- Próximos Passos;
- Oportunidades Ativas;
- Intervenções Contextuais;
- Experiências;
- Evolução Contínua;
- Guivos Intelligence;
- serviços especializados autorizados.

## Efeito funcional

A capacidade deverá avaliar suas próprias decisões.

O evento não ordena automaticamente qual decisão deverá ser tomada.

# 190. Contrato de `DecisaoDependenteReavaliada`

## Finalidade

Registrar que uma decisão anterior foi revisada após mudança contextual.

## Conteúdo mínimo

- decisão;
- contexto anterior;
- mudança relevante;
- resultado da reavaliação;
- ação mantida, modificada, suspensa ou cancelada;
- explicação ao participante.

# 191. Eventos de interação de `Meu Contexto Hoje`

Eventos de interação deverão ser separados de eventos que alteram o contexto.

Exemplos:

- `ContextoVisualizado`;
- `DimensaoVisualizada`;
- `ExplicacaoSolicitada`;
- `HistoricoConsultado`.

Esses eventos poderão apoiar:

- auditoria;
- continuidade de experiência;
- melhoria da interface;
- compreensão de necessidades de explicação.

Eles não deverão, isoladamente:

- criar preferência;
- alterar objetivo;
- definir identidade;
- concluir intenção;
- gerar evolução;
- ampliar permissão.

# 192. Contrato de `ExplicacaoSolicitada`

## Finalidade

Registrar que o participante solicitou compreender uma informação ou decisão.

## Conteúdo mínimo

- elemento ou decisão;
- pergunta apresentada;
- canal;
- nível de detalhamento solicitado;
- resposta fornecida;
- necessidade de esclarecimento adicional.

Solicitar explicação não significa contestar a informação.

# 193. Contrato de `InformacaoOcultada`

## Finalidade

Registrar que o participante decidiu reduzir a exposição visual de uma informação.

Ocultação visual não deverá ser confundida com:

- exclusão;
- revogação;
- limitação de finalidade;
- encerramento;
- contestação.

O evento deverá indicar claramente o alcance da ocultação.

# 194. Contrato de `AlteracaoDesfeita`

## Finalidade

Registrar a reversão de uma alteração anterior.

## Conteúdo mínimo

- alteração revertida;
- motivo;
- estado restaurado;
- data;
- impactos reavaliados;
- limitações de restauração.

Desfazer não deverá apagar o fato de que a alteração ocorreu.

# 195. Contrato de `ElementoRemovido`

## Finalidade

Registrar a remoção funcional de um elemento do Contexto Vivo.

## Conteúdo mínimo

- elemento;
- motivo;
- solicitação ou fundamento;
- capacidades notificadas;
- inferências dependentes;
- retenção residual legítima, quando existir;
- confirmação ao participante.

A remoção deverá evitar reconstrução indevida a partir de dependências antigas.

# 196. Eventos compostos e eventos específicos

Um acontecimento poderá produzir:

1. um evento específico;
2. um evento de dimensão;
3. um evento de contexto geral;
4. eventos de propagação.

Exemplo:

```text
InformacaoCorrigida
→ DimensaoAtualizada
→ ContextoAtualizado
→ RecorteContextualRecomposto
→ CapacidadeConsumidoraNotificada
```

Eventos gerais não deverão substituir eventos específicos.

`ContextoAtualizado` isoladamente não fornece informação suficiente sobre o que ocorreu.

# 197. Contrato de `DimensaoAtualizada`

## Finalidade

Registrar alteração relevante na síntese de uma dimensão.

## Conteúdo mínimo

- dimensão;
- elementos responsáveis;
- estado resumido anterior;
- novo estado resumido;
- confiança;
- atualidade;
- conflitos;
- permissões;
- motivo da mudança.

# 198. Contrato de `ContextoAtualizado`

## Finalidade

Registrar que a representação contextual vigente foi recomposta.

## Conteúdo mínimo

- dimensões modificadas;
- elementos alterados;
- motivo;
- data de referência;
- versão da representação;
- incertezas;
- restrições de uso.

Esse evento não significa que todas as dimensões foram modificadas.

# 199. Eventos e informações sensíveis

Eventos relacionados a informações sensíveis deverão aplicar regras adicionais:

- minimização do conteúdo;
- referência protegida ao elemento original;
- finalidade explícita;
- acesso restrito;
- ausência de detalhes desnecessários;
- histórico controlado;
- rastreabilidade de acesso;
- efeitos imediatos de revogação.

Um evento não deverá expor diretamente uma condição sensível quando for suficiente indicar:

```text
Restrição funcional atualizada
```

com acesso ao detalhe somente por capacidades autorizadas.

# 200. Eventos e inferências

Eventos derivados de inferência deverão indicar:

- que a origem é inferencial;
- modelo ou processo responsável;
- evidências utilizadas;
- confiança;
- limitações;
- confirmação necessária;
- usos permitidos.

Um evento inferencial não deverá ser confundido com um fato declarado.

Exemplo:

```text
AtualizacaoContextualProposta
Origem: inferência
```

e não:

```text
InformacaoConfirmada
```

# 201. Eventos retroativos

Quando uma mudança for informada posteriormente, o evento deverá preservar:

- data efetiva do fato;
- data de conhecimento;
- data de registro;
- período em que a Guivos operou com contexto incompleto;
- decisões potencialmente afetadas.

Eventos retroativos não deverão reescrever o histórico como se a Guivos já possuísse aquela informação.

# 202. Correção de eventos

Quando um evento tiver sido produzido incorretamente, ele não deverá ser apagado silenciosamente.

Deverá existir um novo evento capaz de indicar:

- evento corrigido;
- erro identificado;
- interpretação correta;
- efeitos a reparar;
- consumidores que precisam ser notificados.

Exemplo:

```text
EventoFuncionalCorrigido
```

A correção técnica não deverá ocultar consequências funcionais já produzidas.

# 203. Duplicidade e repetição

Duas ocorrências visualmente semelhantes poderão representar:

- o mesmo evento recebido novamente;
- duas confirmações distintas;
- duas mudanças sucessivas;
- duas fontes diferentes;
- uma repetição indevida.

O identificador e a correlação deverão permitir distinguir esses casos.

O mesmo evento não deverá gerar repetidamente:

- novas alterações;
- novas notificações;
- novos bloqueios;
- novas oportunidades;
- novas inferências.

# 204. Falha de processamento

Quando uma capacidade não conseguir processar um evento relevante, deverá ser possível registrar:

```text
ProcessamentoFuncionalPendente
```

ou:

```text
ProcessamentoFuncionalFalhou
```

O registro deverá indicar:

- evento original;
- capacidade;
- efeito não produzido;
- risco funcional;
- medida preventiva;
- possibilidade de nova tentativa.

A falha técnica não deverá ser apresentada ao participante como alteração concluída.

# 205. Explicação baseada em eventos

A Guivos deverá conseguir responder:

- o que mudou;
- quando mudou;
- quem informou;
- por que foi alterado;
- qual informação existia antes;
- quais capacidades foram afetadas;
- qual permissão foi utilizada;
- quais decisões foram reavaliadas.

Exemplo:

> Sua disponibilidade foi atualizada para sábado à tarde porque você informou essa mudança em 13/07/2026. A informação anterior permanece no histórico e não será mais utilizada para selecionar eventos futuros.

# 206. Retenção funcional

A retenção dos eventos deverá considerar:

- explicabilidade;
- direitos do participante;
- necessidade operacional;
- obrigações aplicáveis;
- sensibilidade;
- finalidade;
- prevenção de reconstrução indevida;
- histórico legítimo da jornada.

Nem todo evento deverá permanecer disponível indefinidamente.

A política técnica e jurídica de retenção será definida em arquitetura e governança específicas.

# 207. Critérios funcionais de aceitação

Os contratos de eventos serão considerados adequados quando permitirem:

1. distinguir intenção, proposta e fato ocorrido;
2. reconstruir a evolução de um elemento contextual;
3. identificar origem, temporalidade e autorização;
4. explicar alterações ao participante;
5. preservar correções e mudanças reais;
6. representar conflitos sem ocultá-los;
7. impedir que inferências sejam tratadas como fatos;
8. recompor recortes contextuais;
9. informar capacidades consumidoras;
10. reavaliar decisões dependentes;
11. aplicar revogações e limitações;
12. evitar efeitos repetidos;
13. preservar histórico sem reescrevê-lo;
14. proteger informações sensíveis;
15. evoluir os contratos por versionamento.

# 208. Regras fundamentais dos eventos

1. Evento representa fato reconhecido, não intenção futura.
2. Eventos relevantes deverão ser imutáveis em relação ao que ocorreu.
3. Erros deverão ser corrigidos por novos eventos.
4. Data do fato, conhecimento e registro deverão ser diferenciadas.
5. Origem e autorização deverão acompanhar o evento.
6. Eventos deverão conter somente informação necessária.
7. Eventos gerais não substituem eventos específicos.
8. Inferências deverão permanecer identificadas.
9. Permissões poderão limitar consumidores e efeitos.
10. Reprocessamento não deverá produzir efeitos duplicados.
11. Eventos deverão sustentar explicabilidade.
12. A implementação técnica não poderá alterar o significado funcional definido.

Com isso, ficam definidos os **contratos detalhados dos eventos funcionais do Contexto Vivo**.

O próximo bloco da Capacidade 02 é a definição das **integrações funcionais do Contexto Vivo com as demais capacidades, camadas e fontes externas**.
