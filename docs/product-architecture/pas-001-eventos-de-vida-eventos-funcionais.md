---
id: PAS-001-EV-EVENT-001
title: Contratos dos Eventos Funcionais da Capacidade de Eventos de Vida
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-EV-FOUNDATION-001
  - PAS-001-EV-LIFECYCLE-001
  - PAS-001-EV-VIEW-001
  - PAS-001-CV-EVENT-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-EVENT-001
  - PAS-001-OBJ-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-EV-EVENT-001 — Contratos dos Eventos Funcionais da Capacidade de Eventos de Vida

## 1. Autoridade e vínculo

Este documento é a **quarta extensão normativa da Capacidade 04 — Eventos de Vida** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 885 a 956 de `PAS-001-EV-FOUNDATION-001 1.0.0`, das seções 957 a 1061 de `PAS-001-EV-LIFECYCLE-001 1.0.0`, das seções 1062 a 1144 de `PAS-001-EV-VIEW-001 1.0.0` e da especificação-base `PAS-001 0.5.0`.

Esta extensão consolida os contratos dos eventos funcionais da Capacidade de Eventos de Vida, incluindo identificação, proposição, confirmação, atualização, temporalidade, relevância, impactos, relações, contestação, correção, encerramento, propagação, idempotência, ordenação, versionamento, auditoria e falha segura.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade normativa das extensões anteriores.

# 1145. Contratos dos eventos funcionais

Os contratos dos eventos funcionais deverão representar fatos reconhecidos durante o ciclo de vida dos Eventos de Vida.

Eles deverão permitir reconstruir:

```text
o que ocorreu
→ quem reconheceu
→ quando ocorreu
→ quando a Guivos tomou conhecimento
→ qual autoridade sustentou o reconhecimento
→ quais efeitos foram aplicados
→ quais capacidades foram notificadas
```

> Um evento funcional representa um fato reconhecido pela capacidade. Ele não representa uma intenção futura, uma solicitação ainda não processada ou uma interpretação não confirmada.

# 1146. Finalidades dos contratos

Os contratos deverão:

1. registrar fatos imutáveis;
2. preservar origem e autoridade;
3. distinguir comando, proposta e evento;
4. representar temporalidade real e temporalidade de conhecimento;
5. permitir correção compensatória;
6. impedir efeitos duplicados;
7. sustentar propagação controlada;
8. preservar permissões e sensibilidade;
9. apoiar explicabilidade;
10. permitir auditoria;
11. controlar falhas e reprocessamento;
12. manter consistência entre capacidades e canais.

# 1147. Comando, proposta e evento

## Comando

Representa solicitação de alteração.

Exemplos:

- confirmar Evento de Vida;
- atualizar data;
- contestar impacto;
- arquivar evento;
- reabrir evento.

## Proposta

Representa uma possibilidade apresentada para avaliação.

Exemplos:

- possível Evento de Vida;
- impacto sugerido;
- relação causal proposta;
- mudança de relevância sugerida.

## Evento funcional

Representa um fato reconhecido após processamento adequado.

Exemplos:

- `EventoDeVidaConfirmado`;
- `ImpactoDeEventoDeVidaContestado`;
- `EventoDeVidaArquivado`.

```text
comando
→ validação
→ decisão funcional
→ evento reconhecido
→ efeitos
```

# 1148. Regras da distinção

1. Receber um comando não significa que a alteração foi realizada.
2. Produzir uma proposta não significa que ela foi aceita.
3. Um evento somente deverá ser publicado após o reconhecimento do fato.
4. Falha de processamento não deverá produzir evento de sucesso.
5. Uma solicitação rejeitada poderá produzir evento próprio de rejeição.
6. A interface não deverá apresentar comando pendente como alteração concluída.

# 1149. Imutabilidade histórica

Um evento funcional reconhecido não deverá ser reescrito para alterar o passado.

Quando houver erro, deverá ser produzido novo evento que:

- identifique o evento anterior;
- descreva a correção;
- preserve a versão incorreta;
- recomponha efeitos;
- notifique consumidores relevantes.

```text
Evento original
→ erro identificado
→ evento de correção
→ efeitos recompostos
```

# 1150. Princípios dos eventos funcionais

Os contratos deverão observar:

- imutabilidade;
- temporalidade explícita;
- proveniência;
- autoridade limitada;
- titularidade;
- minimização;
- finalidade;
- sensibilidade;
- explicabilidade;
- versionamento;
- correlação;
- causalidade;
- idempotência;
- propagação controlada;
- falha segura.

# 1151. Estrutura comum

Todo evento funcional deverá possuir, conforme aplicabilidade:

| Campo | Finalidade |
|---|---|
| `event_id` | Identificar unicamente o evento |
| `event_type` | Informar o tipo funcional |
| `schema_version` | Identificar a versão do contrato |
| `aggregate_id` | Identificar o Evento de Vida relacionado |
| `participant_id` | Identificar o titular |
| `participant_category` | Pessoa, Organização ou Coletivo |
| `actor_id` | Identificar quem provocou ou reconheceu a alteração |
| `actor_role` | Informar o papel do ator |
| `authority` | Limitar o significado do reconhecimento |
| `source` | Informar a origem |
| `occurred_at` | Informar quando o fato ocorreu |
| `known_at` | Informar quando a Guivos tomou conhecimento |
| `recognized_at` | Informar quando o fato foi reconhecido funcionalmente |
| `effective_at` | Informar quando os efeitos passam a ser aplicáveis |
| `correlation_id` | Relacionar eventos da mesma operação |
| `causation_id` | Identificar o evento causador |
| `command_id` | Relacionar o comando originador |
| `idempotency_key` | Impedir efeito duplicado |
| `purpose` | Informar a finalidade |
| `sensitivity` | Aplicar proteção adequada |
| `permissions` | Limitar consumidores e usos |
| `payload` | Representar o fato específico |
| `metadata` | Registrar informações auxiliares mínimas |

# 1152. Identidade do titular

O contrato deverá identificar corretamente:

- titular do Evento de Vida;
- categoria do participante;
- contexto organizacional ou coletivo;
- representação autorizada, quando aplicável.

Identidade incerta deverá impedir eventos de:

- confirmação;
- impacto;
- conclusão;
- compartilhamento;
- correção material;
- propagação externa.

# 1153. Ator

O ator poderá ser:

- participante;
- representante autorizado;
- organização;
- profissional;
- integração;
- capacidade do Journey;
- Guivos Intelligence;
- operação administrativa autorizada;
- processo técnico.

O ator técnico não deverá ser apresentado como autoridade humana quando apenas executou uma decisão.

# 1154. Autoridade

O evento deverá informar o que o ator ou a fonte possui autoridade para reconhecer.

Exemplo:

```text
Fonte:
instituição de ensino

Autoridade:
confirmar conclusão institucional

Sem autoridade:
confirmar transformação pessoal ou impacto emocional
```

# 1155. Temporalidades

Os eventos deverão distinguir:

## Tempo do fato

Quando a mudança ocorreu na realidade.

## Tempo de conhecimento

Quando a Guivos recebeu a informação.

## Tempo de reconhecimento

Quando a capacidade admitiu o fato.

## Tempo de aplicação

Quando os efeitos foram ou serão aplicados.

Essas temporalidades poderão ser diferentes.

# 1156. Temporalidade aproximada

Quando o tempo do fato não for exato, o evento deverá representar:

- precisão conhecida;
- intervalo;
- aproximação;
- incerteza;
- origem da estimativa.

Não deverá ser registrada data exata fictícia.

# 1157. Eventos retroativos

Um evento retroativo deverá preservar:

- data real ou aproximada do fato;
- data de conhecimento posterior;
- data de reconhecimento;
- decisões anteriormente tomadas sem essa informação;
- efeitos históricos e atuais;
- limites da reconstrução.

# 1158. Correlação

Eventos relacionados à mesma operação deverão compartilhar `correlation_id`.

Exemplo:

```text
EventoDeVidaConfirmado
ImpactoDeEventoDeVidaProposto
RecorteDeEventoDeVidaRecomposto
CapacidadeConsumidoraDeEventoDeVidaNotificada
```

# 1159. Causalidade funcional

O campo `causation_id` deverá identificar o evento que provocou diretamente outro evento funcional.

Ele não deverá ser utilizado para afirmar causalidade humana ou existencial sem base suficiente.

# 1160. Versionamento

O versionamento deverá permitir:

- evolução do contrato;
- compatibilidade entre produtores e consumidores;
- leitura de eventos históricos;
- migração controlada;
- identificação de campos novos, alterados ou descontinuados.

Alterações incompatíveis deverão gerar nova versão principal do contrato.

# 1161. Finalidade

Cada evento deverá possuir finalidade compatível com:

- sua criação;
- processamento;
- propagação;
- retenção;
- auditoria;
- explicação.

Um evento registrado para acompanhamento pessoal não deverá ser reutilizado automaticamente para publicidade, avaliação organizacional ou finalidade comercial.

# 1162. Sensibilidade

O evento deverá informar o nível de sensibilidade necessário para:

- armazenamento;
- visualização;
- logs;
- notificações;
- propagação;
- retenção;
- auditoria;
- acesso administrativo.

O conteúdo sensível não deverá ser copiado integralmente para todos os consumidores.

# 1163. Permissões

As permissões deverão limitar:

- consumidor;
- finalidade;
- ação;
- período;
- nível de detalhe;
- possibilidade de redistribuição;
- retenção.

A existência do evento não representa autorização universal de acesso.

# 1164. Famílias de eventos

Os eventos serão organizados nas famílias:

1. identificação e proposição;
2. declaração e confirmação;
3. planejamento;
4. início e acompanhamento;
5. temporalidade;
6. relevância;
7. impactos;
8. relações;
9. correção e contestação;
10. interrupção, cancelamento e conclusão;
11. arquivamento e reabertura;
12. unificação e desdobramento;
13. permissões e compartilhamentos;
14. propagação;
15. visão e interação;
16. processamento e falhas.

# 1165. `PossivelEventoDeVidaIdentificado`

Deverá registrar que uma informação foi reconhecida como possível sinal de Evento de Vida.

## Conteúdo mínimo

- participante possível;
- origem;
- sinais utilizados;
- período;
- confiança;
- sensibilidade;
- finalidade;
- limitações.

## Efeitos permitidos

- iniciar avaliação;
- relacionar sinais;
- produzir pergunta;
- criar proposta.

## Efeitos proibidos

- atualizar Contexto Vivo;
- alterar Objetivos;
- compartilhar como evento confirmado;
- produzir diagnóstico.

# 1166. `EventoDeVidaProposto`

Deverá registrar que uma formulação foi apresentada para avaliação.

## Conteúdo mínimo

- formulação proposta;
- expressão ou sinais de origem;
- titular possível;
- temporalidade estimada;
- confiança;
- impactos possíveis;
- necessidade de confirmação.

A proposta deverá permanecer distinguível de evento confirmado.

# 1167. `EventoDeVidaRejeitado`

Deverá registrar que uma proposta não foi aceita.

## Motivos possíveis

- evento não ocorreu;
- titular incorreto;
- formulação inadequada;
- data incorreta;
- duplicidade;
- ausência de relevância;
- participante não deseja o registro;
- fonte sem autoridade.

A rejeição deverá interromper efeitos derivados não confirmados.

# 1168. `EventoDeVidaDeclarado`

Deverá registrar que o participante ou representante autorizado declarou uma mudança.

## Conteúdo mínimo

- expressão original;
- formulação inicial;
- declarante;
- autoridade;
- temporalidade;
- significado atribuído;
- sensibilidade;
- impactos percebidos.

A declaração poderá anteceder confirmação estrutural.

# 1169. `EventoDeVidaPlanejado`

Deverá registrar uma mudança futura reconhecida como planejamento ou compromisso concreto.

## Conteúdo mínimo

- tipo de evento;
- previsão;
- confiança;
- condições;
- origem;
- preparações autorizadas;
- possibilidade de adiamento ou cancelamento.

O evento não deverá indicar que a mudança já ocorreu.

# 1170. `EventoDeVidaConfirmado`

Deverá registrar que a existência, ocorrência ou previsão do evento foi reconhecida.

## Pré-condições

- titular identificado;
- formulação suficiente;
- autoridade adequada;
- temporalidade representável;
- finalidade válida;
- permissões aplicadas.

## Conteúdo mínimo

- evento confirmado;
- forma de confirmação;
- escopo confirmado;
- elementos pendentes;
- temporalidade;
- autoridade.

Confirmar o evento não deverá confirmar automaticamente seus impactos.

# 1171. Confirmação parcial

Quando apenas parte do evento for confirmada, o contrato deverá indicar:

- elementos confirmados;
- elementos pendentes;
- elementos rejeitados;
- efeitos permitidos;
- necessidade de revisão.

# 1172. `EventoDeVidaIniciado`

Deverá registrar o início efetivo da mudança.

## Conteúdo mínimo

- data ou período de início;
- origem;
- estado anterior;
- condição inicial;
- impactos já observados;
- previsões pendentes.

# 1173. `EventoDeVidaAtualizado`

Deverá registrar nova informação sobre evento em andamento ou já reconhecido.

A atualização poderá envolver:

- estado;
- duração;
- descrição;
- participantes;
- previsão;
- evidências;
- relevância;
- impactos;
- significado atribuído.

Cada atualização deverá produzir nova versão funcional.

# 1174. Atualização sem mudança material

Informações auxiliares sem impacto funcional relevante poderão ser registradas como atualização técnica ou metadado, sem produzir propagação ampla.

A classificação deverá ser explicável.

# 1175. `EventoDeVidaAdiado`

Deverá registrar alteração da previsão de evento planejado.

## Conteúdo mínimo

- previsão anterior;
- nova previsão;
- motivo opcional;
- confiança;
- preparações afetadas;
- consumidores que deverão reavaliar decisões.

Adiamento não deverá ser tratado como cancelamento.

# 1176. `TemporalidadeDeEventoDeVidaCorrigida`

Deverá registrar correção de data ou período anteriormente reconhecido como incorreto.

O evento deverá preservar:

- temporalidade anterior;
- nova temporalidade;
- origem da correção;
- efeitos recompostos;
- decisões afetadas.

# 1177. `RelevanciaDeEventoDeVidaAlterada`

Deverá registrar mudança material na relevância contextual do evento.

## Conteúdo mínimo

- relevância anterior;
- nova relevância;
- fatores considerados;
- origem;
- confiança;
- unidades afetadas;
- efeitos operacionais.

A relevância não deverá ser alterada por interesse comercial.

# 1178. `ImpactoDeEventoDeVidaProposto`

Deverá registrar um possível efeito do evento sobre outra unidade funcional.

## Conteúdo mínimo

- evento de origem;
- unidade afetada;
- tipo de impacto;
- intensidade estimada;
- temporalidade;
- evidências;
- confiança;
- capacidade responsável;
- necessidade de confirmação.

Nenhuma alteração definitiva deverá ser presumida.

# 1179. `ImpactoDeEventoDeVidaConfirmado`

Deverá registrar que um impacto foi reconhecido.

## Pré-condições

- unidade afetada identificada;
- autoridade adequada;
- evidência proporcional;
- capacidade responsável;
- finalidade compatível.

## Conteúdo mínimo

- impacto confirmado;
- unidade afetada;
- intensidade;
- início;
- duração;
- origem;
- efeitos aplicáveis.

# 1180. `ImpactoDeEventoDeVidaRejeitado`

Deverá registrar que um impacto proposto foi considerado inadequado.

A rejeição poderá decorrer de:

- ausência de impacto;
- unidade incorreta;
- intensidade inadequada;
- temporalidade incorreta;
- falta de autoridade;
- contestação do participante.

# 1181. `ImpactoDeEventoDeVidaContestado`

Deverá registrar questionamento sobre impacto anteriormente reconhecido ou proposto.

A contestação deverá:

- identificar o impacto;
- informar o motivo;
- limitar efeitos críticos;
- reduzir confiança;
- notificar a capacidade responsável;
- preservar o histórico.

# 1182. `ImpactoDeEventoDeVidaEncerrado`

Deverá registrar que determinado efeito deixou de permanecer ativo.

O encerramento do impacto deverá ser independente da conclusão do evento.

# 1183. `ImpactoDeEventoDeVidaReaberto`

Deverá registrar o retorno de impacto anteriormente encerrado.

O contrato deverá preservar o ciclo anterior e informar se:

- o impacto reapareceu;
- nunca havia realmente terminado;
- existe nova evidência;
- ocorreu novo ciclo relacionado.

# 1184. `DimensaoContextualPotencialmenteImpactada`

Deverá registrar que uma dimensão do Contexto Vivo poderá exigir avaliação.

A capacidade não deverá aplicar diretamente a atualização contextual.

# 1185. `ObjetivoPotencialmenteImpactado`

Deverá registrar que determinado objetivo poderá necessitar de revisão.

O evento deverá indicar:

- objetivo;
- tipo de impacto;
- confiança;
- temporalidade;
- urgência funcional;
- evidências;
- ação esperada da Capacidade de Objetivos.

# 1186. `RevisaoPorEventoDeVidaSolicitada`

Deverá registrar solicitação para que outra capacidade reavalie sua unidade funcional.

## Conteúdo mínimo

- capacidade destinatária;
- unidade afetada;
- evento causador;
- recorte mínimo;
- ação solicitada;
- prioridade operacional;
- prazo funcional, quando aplicável.

A solicitação não deverá declarar que a revisão foi concluída.

# 1187. `RelacaoEntreEventosDeVidaProposta`

Deverá registrar possível relação entre eventos.

Tipos possíveis:

- causalidade;
- consequência;
- precedência;
- composição;
- correlação;
- dependência;
- reversão;
- agravamento;
- redução;
- simultaneidade.

A relação deverá permanecer proposta até base suficiente.

# 1188. `RelacaoEntreEventosDeVidaConfirmada`

Deverá registrar relação reconhecida entre eventos.

## Conteúdo mínimo

- eventos relacionados;
- tipo de relação;
- direção;
- evidências;
- autoridade;
- temporalidade;
- confiança;
- limitações.

# 1189. `RelacaoEntreEventosDeVidaContestado`

Deverá registrar contestação sobre relação anteriormente reconhecida.

A contestação poderá suspender interpretações e decisões baseadas na relação.

# 1190. Relação causal

Eventos de relação causal deverão exigir base superior à simples proximidade temporal.

O contrato deverá informar:

- natureza da evidência;
- autoridade;
- alternativas consideradas;
- nível de confiança;
- limitações.

# 1191. `EventoDeVidaConcluido`

Deverá registrar que a mudança atingiu seu encerramento funcional.

## Conteúdo mínimo

- data ou período de conclusão;
- autoridade;
- estado final;
- impactos ativos;
- impactos encerrados;
- revisões pendentes;
- possibilidade de reabertura.

Conclusão do evento não deverá concluir automaticamente objetivos ou impactos.

# 1192. `EventoDeVidaInterrompido`

Deverá registrar que evento em andamento foi suspenso antes de sua conclusão.

O contrato deverá informar:

- momento;
- condição atual;
- efeitos já produzidos;
- impactos persistentes;
- possibilidade de retomada;
- decisões dependentes.

# 1193. `EventoDeVidaCancelado`

Deverá registrar que evento planejado deixou de ocorrer.

## Conteúdo mínimo

- planejamento anterior;
- momento do cancelamento;
- preparações afetadas;
- impactos a reverter;
- decisões dependentes;
- autoridade.

Cancelamento não deverá ser classificado como fracasso pessoal.

# 1194. `EventoDeVidaContestado`

Deverá registrar contestação material sobre o evento.

A contestação poderá envolver:

- existência;
- formulação;
- titularidade;
- temporalidade;
- origem;
- autoridade;
- relevância;
- sensibilidade;
- compartilhamento;
- uso.

# 1195. Efeitos do evento contestado

Conforme risco, deverão ser aplicados:

- suspensão de novos impactos;
- redução de confiança;
- limitação de recortes;
- interrupção de decisões críticas;
- solicitação de revisão;
- notificação de consumidores.

# 1196. `EventoDeVidaCorrigido`

Deverá registrar correção material do evento.

## Conteúdo mínimo

- evento ou versão anterior;
- campos incorretos;
- valores corrigidos;
- origem;
- autoridade;
- efeitos recompostos;
- consumidores afetados.

A correção deverá ser compensatória, não destrutiva.

# 1197. `EventoDeVidaArquivado`

Deverá registrar retirada do evento da operação cotidiana.

O evento deverá informar:

- motivo;
- impactos ainda ativos;
- consumidores que permanecem autorizados;
- restrições de novos usos;
- condição de consulta histórica.

# 1198. `EventoDeVidaReaberto`

Deverá registrar retomada do mesmo ciclo funcional.

## Conteúdo mínimo

- evento anterior;
- motivo;
- novo estado;
- temporalidade;
- impactos reativados;
- revisões necessárias;
- consumidores notificados.

# 1199. `EventosDeVidaUnificados`

Deverá registrar que dois ou mais registros representavam a mesma mudança.

O contrato deverá preservar:

- identificadores anteriores;
- fontes;
- evidências;
- versões;
- temporalidades;
- efeitos já produzidos;
- evento resultante.

# 1200. `EventoDeVidaDesdobrado`

Deverá registrar separação de evento composto ou excessivamente amplo em eventos independentes.

O contrato deverá informar:

- evento original;
- eventos resultantes;
- critérios de separação;
- relações preservadas;
- impactos redistribuídos;
- consumidores afetados.

# 1201. `EventoCompostoDeVidaCriado`

Deverá registrar estrutura que organiza uma transição ampla.

O evento composto deverá:

- manter componentes acessíveis;
- não substituir seus ciclos;
- não ocultar impactos específicos;
- permitir inclusão e remoção controlada de componentes.

# 1202. `ComponenteDeEventoCompostoAtualizado`

Deverá registrar alteração na composição de evento amplo.

A atualização deverá preservar o histórico das relações.

# 1203. `CompartilhamentoDeEventoDeVidaAutorizado`

Deverá registrar autorização de recorte para consumidor específico.

## Conteúdo mínimo

- consumidor;
- finalidade;
- recorte;
- duração;
- sensibilidade;
- permissões;
- condição de revogação.

# 1204. `CompartilhamentoDeEventoDeVidaRevogado`

Deverá registrar retirada da autorização para novos usos.

O evento deverá iniciar:

- interrupção de novos compartilhamentos;
- recomposição de recortes;
- notificação de consumidores;
- acompanhamento da propagação;
- preservação de obrigações legítimas.

# 1205. `PropagacaoDeRevogacaoDeEventoIniciada`

Deverá indicar que a revogação ainda está sendo processada.

Não deverá ser apresentado ao participante como revogação totalmente concluída.

# 1206. `PropagacaoDeRevogacaoDeEventoConcluida`

Deverá registrar que todos os consumidores necessários confirmaram o tratamento da revogação.

# 1207. `RecorteDeEventoDeVidaRecomposto`

Deverá registrar alteração do conteúdo fornecido a consumidores.

Gatilhos possíveis:

- confirmação;
- correção;
- contestação;
- mudança de sensibilidade;
- alteração de impacto;
- conclusão;
- arquivamento;
- revogação.

# 1208. `CapacidadeConsumidoraDeEventoDeVidaNotificada`

Deverá registrar que uma capacidade recebeu informação suficiente para reavaliar sua própria unidade.

O evento não deverá afirmar que a capacidade consumidora já concluiu a reavaliação.

# 1209. `ReavaliacaoDependenteDeEventoIniciada`

Deverá registrar início do processamento por capacidade consumidora.

# 1210. `ReavaliacaoDependenteDeEventoConcluida`

Deverá registrar que a capacidade consumidora concluiu sua decisão.

O contrato deverá indicar:

- unidade reavaliada;
- decisão;
- efeitos;
- evento causador;
- versão utilizada.

# 1211. Eventos originados pela visão

A visão funcional poderá emitir comandos que resultem em eventos como:

- `EventoDeVidaConfirmado`;
- `EventoDeVidaAtualizado`;
- `EventoDeVidaAdiado`;
- `EventoDeVidaCancelado`;
- `EventoDeVidaConcluido`;
- `EventoDeVidaContestado`;
- `EventoDeVidaArquivado`;
- `EventoDeVidaReaberto`.

O canal de origem deverá ser registrado sem alterar o significado funcional do evento.

# 1212. Eventos conversacionais

Alterações realizadas em canal conversacional deverão utilizar os mesmos contratos funcionais da visão principal.

A conversa não deverá criar uma linha paralela de estado.

# 1213. Eventos de leitura e interação

Eventos como:

- visualização;
- abertura de detalhes;
- solicitação de explicação;
- aplicação de filtro;

poderão ser registrados para operação da experiência.

Eles não deverão ser tratados como:

- confirmação;
- interesse permanente;
- impacto;
- relevância;
- mudança contextual.

# 1214. Eventos compostos de processamento

Uma operação poderá produzir vários eventos funcionalmente relacionados.

Exemplo:

```text
EventoDeVidaConfirmado
→ ImpactoDeEventoDeVidaProposto
→ RecorteDeEventoDeVidaRecomposto
→ CapacidadeConsumidoraDeEventoDeVidaNotificada
```

Cada fato deverá permanecer identificável.

# 1215. Atomicidade funcional

Quando uma operação depender de vários efeitos inseparáveis, a capacidade deverá:

- concluir todos;
- ou indicar operação incompleta;
- ou compensar os efeitos já aplicados.

Não deverá apresentar sucesso integral quando parte crítica falhar.

# 1216. Eventos pendentes

Quando o fato ainda não estiver reconhecido, a capacidade poderá manter:

- comando pendente;
- proposta pendente;
- processamento pendente;
- propagação pendente.

Esses estados não deverão ser publicados como eventos de sucesso.

# 1217. Idempotência

Todo comando com potencial de repetição deverá possuir chave de idempotência.

O reprocessamento não deverá:

- criar eventos duplicados;
- duplicar impactos;
- repetir notificações;
- reaplicar alterações;
- criar múltiplas revisões idênticas;
- duplicar eventos compostos.

# 1218. Duplicidade semântica

Mesmo com identificadores diferentes, dois eventos poderão representar o mesmo fato.

A capacidade deverá avaliar:

- titular;
- tipo;
- temporalidade;
- origem;
- formulação;
- evento relacionado;
- correlação.

# 1219. Ordenação

Eventos deverão ser processados respeitando dependências funcionais.

Exemplo inválido:

```text
EventoDeVidaConcluido
→ recebido antes de EventoDeVidaIniciado
```

O sistema deverá:

- aguardar;
- reconciliar;
- limitar;
- rejeitar;
- ou solicitar revisão.

# 1220. Eventos fora de ordem

O contrato deverá preservar:

- ordem de ocorrência;
- ordem de conhecimento;
- ordem de processamento.

Essas ordens poderão ser diferentes.

# 1221. Concorrência

Quando duas alterações ocorrerem simultaneamente, a capacidade deverá:

- comparar versões;
- preservar ambas as origens;
- detectar conflito;
- evitar sobrescrita silenciosa;
- solicitar resolução quando necessário.

# 1222. Versão esperada

Comandos materiais deverão poder informar a versão do evento sobre a qual foram emitidos.

Quando a versão estiver desatualizada, a capacidade deverá:

- rejeitar;
- reapresentar estado atual;
- solicitar confirmação;
- ou reconciliar quando seguro.

# 1223. Correção compensatória

Uma correção deverá produzir eventos adicionais que:

- anulam ou limitam efeitos anteriores;
- recompõem recortes;
- reabrem decisões;
- atualizam consumidores;
- preservam a trilha histórica.

# 1224. Exclusão

Quando houver direito ou obrigação de exclusão, a capacidade deverá distinguir:

- retirada de uso operacional;
- anonimização;
- restrição de acesso;
- exclusão de conteúdo;
- preservação mínima por obrigação legítima.

A exclusão não deverá falsificar a sequência dos fatos remanescentes.

# 1225. Retenção

A retenção deverá considerar:

- finalidade;
- sensibilidade;
- estado;
- contestação;
- obrigações legítimas;
- dependências;
- necessidade de explicação;
- controle do participante.

Sinais rejeitados ou sem finalidade deverão possuir retenção reduzida.

# 1226. Logs

Logs técnicos não deverão conter conteúdo sensível integral quando identificadores ou classificações mínimas forem suficientes.

# 1227. Falhas de processamento

Poderão ocorrer falhas de:

- validação;
- identidade;
- autorização;
- temporalidade;
- versão;
- persistência;
- publicação;
- propagação;
- consumidor;
- revogação;
- explicação.

# 1228. `ProcessamentoDeEventoDeVidaFalhou`

Deverá registrar falha operacional relevante.

## Conteúdo mínimo

- operação;
- etapa;
- evento ou comando relacionado;
- causa funcional;
- efeitos aplicados;
- efeitos pendentes;
- possibilidade de reprocessamento;
- risco;
- ação de recuperação.

O evento de falha deverá evitar conteúdo sensível desnecessário.

# 1229. `PropagacaoDeEventoDeVidaFalhou`

Deverá registrar que um ou mais consumidores não processaram o recorte.

O estado deverá permanecer pendente até recuperação ou decisão formal.

# 1230. Falha segura

Em caso de falha:

- o último estado válido deverá ser preservado;
- permissões mais restritivas deverão prevalecer;
- impactos críticos não confirmados deverão ser suspensos;
- conclusão não deverá ser presumida;
- propagação incompleta deverá ser visível;
- reprocessamento deverá respeitar idempotência.

# 1231. Recuperação

A recuperação poderá:

- repetir processamento;
- recompor recorte;
- solicitar nova confirmação;
- compensar efeitos;
- reconciliar versões;
- operar manualmente;
- suspender integração.

# 1232. Responsabilidade do produtor

O produtor deverá:

- emitir somente fatos reconhecidos;
- preencher campos obrigatórios;
- preservar origem;
- aplicar autoridade;
- classificar sensibilidade;
- informar temporalidade;
- fornecer chave de idempotência;
- evitar conteúdo excessivo;
- preservar versão.

# 1233. Responsabilidade do consumidor

O consumidor deverá:

- validar versão;
- validar autorização;
- respeitar finalidade;
- aplicar idempotência;
- não ampliar significado;
- reavaliar sua própria unidade;
- informar falhas;
- tratar revogação;
- preservar correlação;
- não transformar recorte em perfil amplo.

# 1234. Relação com Contexto Vivo

Eventos de Vida poderão solicitar atualização contextual, mas o Contexto Vivo deverá produzir seus próprios eventos de:

- atualização;
- confirmação;
- conflito;
- correção;
- envelhecimento;
- recomposição de recorte.

# 1235. Relação com Objetivos

A Capacidade de Eventos de Vida poderá produzir:

- objetivo potencialmente afetado;
- revisão solicitada;
- evidência relacionada;
- conflito possível.

A Capacidade de Objetivos deverá emitir os eventos que governam alterações efetivas do objetivo.

# 1236. Relação com Próximos Passos

A Capacidade 05 poderá receber solicitação de reavaliação.

Ela deverá produzir eventos próprios para:

- criação;
- suspensão;
- cancelamento;
- reordenação;
- substituição;
- conclusão de Próximo Passo.

# 1237. Relação com Oportunidades Ativas

A capacidade poderá informar mudança de:

- localização;
- disponibilidade;
- restrição;
- elegibilidade;
- janela temporal.

Oportunidades Ativas deverá recalcular relevância por seus próprios contratos.

# 1238. Relação com Intervenções Contextuais

Eventos poderão gerar necessidade de:

- agir;
- perguntar;
- esperar;
- observar;
- silenciar.

A decisão de intervenção deverá permanecer sob a Capacidade 07.

# 1239. Relação com Experiências

Uma experiência poderá produzir informação que resulte em possível Evento de Vida.

O evento funcional da experiência e o Evento de Vida deverão permanecer distintos e correlacionados.

# 1240. Relação com Evolução Contínua

Eventos de Vida poderão ser utilizados como marcos temporais autorizados.

Eles não deverão representar automaticamente:

- progresso;
- transformação;
- sucesso;
- regressão;
- valor humano.

# 1241. Papel da Guivos Intelligence

Guivos Intelligence poderá produzir:

- sinais;
- hipóteses;
- classificações sugeridas;
- impactos propostos;
- relações propostas;
- explicações;
- alertas de inconsistência.

Ela não deverá publicar diretamente, sem contrato adequado:

- evento pessoal sensível confirmado;
- impacto pessoal definitivo;
- conclusão de evento;
- alteração de prioridade;
- diagnóstico.

# 1242. Papel da Platform Layer

A Platform Layer deverá apoiar:

- persistência;
- identidade;
- autenticação;
- autorização;
- publicação;
- filas;
- ordenação;
- versionamento;
- idempotência;
- auditoria;
- observabilidade;
- retenção.

Ela não deverá redefinir o significado funcional dos eventos.

# 1243. Pessoa

Eventos de Pessoa deverão preservar:

- autoria;
- autoridade sobre a própria vivência;
- controle de sensibilidade;
- informações de terceiros;
- direito de contestação;
- finalidade limitada.

# 1244. Organização

Eventos organizacionais deverão preservar:

- papel do ator;
- autoridade institucional;
- escopo;
- unidade organizacional;
- política aplicável;
- separação entre fato institucional e impacto pessoal.

# 1245. Coletivo

Eventos de Coletivo deverão preservar:

- regras de participação;
- autoridade de representação;
- processo decisório;
- membros afetados;
- divergências;
- possibilidade de saída.

# 1246. Eventos compartilhados

Quando um evento pertencer a mais de um participante, o contrato deverá definir:

- titularidade;
- perspectivas;
- autoridade de cada parte;
- conteúdo compartilhado;
- conteúdo privado;
- contestações independentes;
- efeitos individuais.

# 1247. Informações de terceiros

Os eventos deverão evitar:

- criar participante implícito;
- registrar diagnóstico de terceiro;
- inferir estado emocional;
- propagar identidade desnecessária;
- ampliar finalidade.

# 1248. Explicabilidade

Cada evento material deverá permitir responder:

- o que foi reconhecido;
- por qual origem;
- com qual autoridade;
- quando ocorreu;
- por que foi processado;
- quais efeitos produziu;
- quais capacidades foram notificadas;
- como contestar ou corrigir.

# 1249. Auditoria

A auditoria deverá permitir reconstruir:

- comando;
- validações;
- proposta;
- decisão;
- evento;
- efeitos;
- propagação;
- falhas;
- reprocessamento;
- correções;
- revogações.

# 1250. Eventos funcionalmente proibidos

Não deverão existir eventos que afirmem automaticamente:

- `EventoDeVidaConfirmadoPorComportamento`;
- `ObjetivoPessoalCriadoPorEvento`;
- `PrioridadePessoalImpostaPorEvento`;
- `ImpactoPessoalConfirmadoSemAutoridade`;
- `EventoPlanejadoTratadoComoConcluido`;
- `CausalidadeConfirmadaPorProximidadeTemporal`;
- `EventoSensivelCompartilhadoImplicitamente`;
- `EventoDeVidaClassificadoComoFracasso`;
- `EventoDeVidaUtilizadoParaExploracaoComercial`;
- `ImpactosEncerradosAutomaticamenteComEvento`;
- `RevogacaoConcluidaSemPropagacao`;
- `EventoReprocessadoComEfeitosDuplicados`.

# 1251. Métricas funcionais dos contratos

Os contratos poderão ser avaliados por:

- eventos sem campos obrigatórios;
- eventos rejeitados por autoridade insuficiente;
- duplicidades;
- efeitos duplicados;
- eventos fora de ordem;
- conflitos de versão;
- correções;
- contestações;
- propagação incompleta;
- tempo de processamento;
- falhas seguras;
- eventos sensíveis expostos indevidamente;
- revogações pendentes;
- explicações disponíveis.

As métricas deverão avaliar o sistema, não o participante.

# 1252. Critérios funcionais de aceite

Os contratos serão considerados adequadamente definidos quando:

1. comando, proposta e evento permanecerem distintos;
2. eventos representarem fatos reconhecidos;
3. registros históricos forem imutáveis;
4. correções ocorrerem por novos eventos;
5. origem e autoridade forem preservadas;
6. titular e ator forem diferenciados;
7. temporalidades do fato, conhecimento, reconhecimento e aplicação forem separadas;
8. datas aproximadas puderem ser representadas;
9. eventos retroativos não reescreverem decisões anteriores;
10. finalidade, sensibilidade e permissões acompanharem o evento;
11. identificação e proposição não produzirem impactos definitivos;
12. confirmação do evento não confirmar automaticamente impactos;
13. impactos possuírem contratos e ciclo próprios;
14. relações propostas permanecerem distintas das confirmadas;
15. causalidade exigir base explicável;
16. correções e contestações recomporem efeitos;
17. conclusão não encerrar impactos persistentes;
18. arquivamento não equivaler a exclusão;
19. reabertura preservar ciclos anteriores;
20. unificação e desdobramento preservarem rastreabilidade;
21. revogação interromper novos usos;
22. propagação utilizar recortes mínimos;
23. produtores e consumidores preservarem responsabilidades;
24. reprocessamento não duplicar efeitos;
25. eventos fora de ordem forem tratados;
26. concorrência não produzir sobrescrita silenciosa;
27. falhas reduzirem automação;
28. eventos sensíveis possuírem proteção reforçada;
29. Pessoa, Organização e Coletivo possuírem autoridade adequada;
30. o participante puder compreender, corrigir e contestar.

# 1253. Regras fundamentais dos eventos funcionais

1. Evento funcional representa fato reconhecido.
2. Comando não equivale a evento.
3. Proposta não equivale a evento confirmado.
4. Eventos históricos não deverão ser reescritos.
5. Correções deverão produzir novos eventos.
6. Titular, ator e fonte deverão permanecer distintos.
7. Autoridade deverá limitar o significado do evento.
8. Tempo do fato e tempo de conhecimento deverão permanecer separados.
9. Precisão temporal não deverá ser fabricada.
10. Confirmação do evento não confirma todos os impactos.
11. Impacto deverá possuir ciclo próprio.
12. Relação proposta não equivale a relação confirmada.
13. Proximidade temporal não comprova causalidade.
14. Evento planejado não equivale a evento ocorrido.
15. Evento concluído poderá possuir impactos ativos.
16. Evento de Vida não cria objetivo pessoal ativo.
17. Evento de Vida não impõe prioridade.
18. Conteúdo sensível deverá ser minimizado.
19. Informações de terceiros deverão ser protegidas.
20. Finalidade deverá acompanhar o evento.
21. Permissões deverão acompanhar a propagação.
22. Revogação deverá interromper novos usos.
23. Propagação incompleta deverá permanecer visível.
24. Reprocessamento não deverá duplicar efeitos.
25. Ordenação deverá respeitar dependências funcionais.
26. Concorrência não deverá sobrescrever versões silenciosamente.
27. Consumidores não deverão ampliar significado.
28. Platform Layer não redefine semântica.
29. Guivos Intelligence não confirma unilateralmente evento pessoal sensível.
30. Falhas deverão preservar o último estado válido.
31. Métricas deverão avaliar o sistema.
32. Receita não deverá alterar reconhecimento, relevância ou impacto.
33. O participante deverá permanecer no controle.

# 1254. Continuidade normativa

`PAS-001-EV-EVENT-001 1.0.0` deverá ser registrado como a **quarta extensão normativa da Capacidade 04 — Eventos de Vida**.

Ele deverá:

- consolidar os contratos dos eventos funcionais;
- preservar a autoridade das três extensões anteriores;
- manter a capacidade no estado `In progress`;
- elevar o progresso editorial de referência para `80%`;
- manter o `PAS-001 0.5.0` como especificação-base.

Com isso, ficam definidos os **contratos dos eventos funcionais da Capacidade de Eventos de Vida**, incluindo identificação, proposição, confirmação, atualização, temporalidade, relevância, impactos, relações, contestação, correção, encerramento, propagação, idempotência, ordenação, versionamento, auditoria e falha segura.

O próximo bloco deverá detalhar:

> **as integrações funcionais da Capacidade de Eventos de Vida com Captura de Contexto, Contexto Vivo, Objetivos, Próximos Passos, Oportunidades Ativas, Intervenções Contextuais, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer, serviços especializados e fontes externas.**
