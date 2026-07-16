---
id: PAS-001-IC-EVENT-001
title: Contratos dos Eventos Funcionais da Capacidade de Intervenções Contextuais
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

# PAS-001-IC-EVENT-001 — Contratos dos Eventos Funcionais da Capacidade de Intervenções Contextuais

## 1. Autoridade e vínculo

Este documento é a **quarta extensão normativa da Capacidade 07 — Intervenções Contextuais** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser interpretado como continuidade do `PAS-001-IC-FOUNDATION-001 1.0.0`, do `PAS-001-IC-LIFECYCLE-001 1.0.0`, do `PAS-001-IC-VIEW-001 1.0.0`, do `PAS-001 0.5.0`, das seções 1 a 3064, dos contratos finais das Capacidades 02 a 06, da `GLPA-001` e da `GIA-000`.

Esta extensão mantém a Capacidade 07 como `In progress` e eleva o progresso editorial de referência de `60%` para `80%`.

As Capacidades 02, 03, 04, 05 e 06 permanecem `Functionally complete`. A Capacidade 08 — Experiências permanece `Planned`.

# 3065. Finalidade dos contratos de eventos

Os contratos deverão definir como fatos funcionais relacionados a Intervenções Contextuais são:

- reconhecidos;
- persistidos;
- publicados;
- consumidos;
- ordenados;
- corrigidos;
- propagados;
- reconstruídos;
- auditados.

O contrato deverá impedir que comandos, propostas, tentativas, sinais técnicos ou registros comerciais sejam tratados como fatos funcionais concluídos.

# 3066. Distinção entre comando, proposta e evento

Deverão permanecer distintos:

- **comando**: solicitação para que algo seja avaliado ou executado;
- **proposta**: possibilidade ainda sujeita a decisão funcional;
- **evento**: fato reconhecido e persistido que já ocorreu no domínio.

Exemplo:

Solicitar avaliação de intervenção
≠
Propor apresentação de alerta
≠
Intervenção admitida
≠
Intervenção apresentada
≠
Intervenção entregue

# 3067. Persistência antes da publicação

Um evento material somente deverá ser publicado após persistência funcional suficiente.

Nenhum consumidor deverá receber como fato definitivo algo que ainda dependa de:

- validação;
- autorização;
- confirmação;
- gravação;
- reconciliação;
- conclusão externa.

# 3068. Agregado funcional

O agregado principal será denominado:

> **Registro de Intervenção Contextual**

Ele deverá preservar:

- identidade;
- participante;
- finalidade;
- origem;
- autoridade;
- contexto mínimo;
- comportamento;
- sensibilidade;
- estado funcional;
- estado da informação;
- temporalidade;
- autorização;
- programação;
- entrega;
- resposta;
- fadiga;
- preferências;
- histórico;
- correções;
- revogações;
- falhas.

# 3069. Identidade permanente do agregado

Cada Registro de Intervenção Contextual deverá possuir identidade permanente.

Correções, reavaliações, adiamentos e mudanças de canal não deverão criar novo agregado quando a finalidade funcional permanecer a mesma.

Mudança material de finalidade, destinatário, comportamento ou impacto deverá produzir novo agregado.

# 3070. Estrutura comum do evento

Todo evento funcional deverá conter, conforme aplicável:

- identificador do evento;
- tipo;
- versão contratual;
- identificador do agregado;
- versão anterior esperada;
- nova versão;
- participante;
- ator;
- papel;
- autoridade;
- fonte;
- finalidade;
- comportamento;
- canal;
- sensibilidade;
- correlação;
- causalidade;
- chave de idempotência;
- temporalidades;
- proveniência;
- relação comercial;
- permissões;
- payload minimizado;
- consumidores autorizados;
- política de retenção.

# 3071. Identificador do evento

O identificador deverá ser:

- único;
- imutável;
- não reutilizável;
- independente do identificador externo;
- preservado em correções e auditorias.

# 3072. Versão contratual

Todo evento deverá declarar a versão de seu contrato.

Consumidores deverão:

- reconhecer versões compatíveis;
- rejeitar versões incompatíveis de forma segura;
- preservar eventos desconhecidos;
- permitir reprocessamento posterior.

# 3073. Versão do agregado

Cada alteração material deverá avançar a versão do agregado.

A versão deverá impedir:

- sobrescrita silenciosa;
- aplicação duplicada;
- regressão de estado;
- concorrência não detectada;
- perda de correção.

# 3074. Participante, ator e destinatário

Deverão permanecer distintos:

- participante titular;
- ator que iniciou o fato;
- destinatário da manifestação;
- terceiro afetado;
- organização relacionada;
- executor externo.

Uma organização não deverá ser tratada automaticamente como titular da jornada individual.

# 3075. Papel funcional

O evento deverá identificar o papel do ator, incluindo:

- participante;
- representante autorizado;
- fonte;
- avaliador;
- sistema;
- organização;
- profissional;
- operador;
- auditor;
- produto especializado.

# 3076. Autoridade

A autoridade deverá indicar o que o ator podia legitimamente:

- declarar;
- solicitar;
- confirmar;
- avaliar;
- executar;
- corrigir;
- revogar.

A presença de dados ou acesso técnico não deverá ampliar autoridade.

# 3077. Fonte

A fonte deverá ser identificada por:

- origem;
- tipo;
- responsável;
- autoridade;
- validade;
- confiabilidade;
- relação comercial;
- cadeia de transformação.

# 3078. Finalidade

Todo evento deverá possuir finalidade específica.

Finalidades genéricas como:

- melhorar engajamento;
- aumentar conversão;
- gerar receita;
- personalizar experiência;
- otimizar retenção;

não deverão justificar uso de contexto pessoal ou sensível.

# 3079. Temporalidades

O contrato deverá distinguir:

- momento do fato;
- momento da solicitação;
- momento da observação;
- momento do conhecimento;
- momento da avaliação;
- momento do reconhecimento;
- momento da persistência;
- momento da publicação;
- momento da aplicação;
- momento da entrega;
- momento da resposta;
- momento da propagação;
- momento da correção.

# 3080. Tempo do fato e tempo do registro

O momento em que algo ocorreu deverá permanecer distinto do momento em que foi registrado.

Eventos retroativos deverão preservar essa diferença.

# 3081. Correlação

A correlação deverá permitir relacionar eventos pertencentes ao mesmo fluxo funcional.

Ela não deverá representar causalidade automaticamente.

# 3082. Causalidade funcional

A causalidade somente deverá ser declarada quando existir relação funcional demonstrável.

Proximidade temporal, abertura de aplicativo, clique ou localização não deverão ser tratados como causa suficiente.

# 3083. Proveniência

A proveniência deverá permitir reconstruir:

fonte original
→ registro
→ validação
→ transformação
→ avaliação
→ decisão
→ evento
→ consumidor
→ efeito

# 3084. Sensibilidade

O evento deverá classificar sua sensibilidade para governar:

- payload;
- logs;
- consumidores;
- retenção;
- visualização;
- notificação;
- auditoria;
- compartilhamento.

# 3085. Minimização do payload

O payload deverá conter somente o necessário para a finalidade declarada.

Narrativas integrais, diagnósticos, histórias pessoais, informações religiosas, financeiras, jurídicas ou de terceiros deverão ser excluídos quando um recorte funcional for suficiente.

# 3086. Relação comercial

Eventos influenciados por:

- publicidade;
- patrocínio;
- comissão;
- afiliação;
- campanha;
- exclusividade;
- participação na receita;

deverão declarar essa relação.

A relação comercial não deverá elevar relevância, urgência ou prioridade funcional.

# 3087. Famílias de eventos

Os eventos deverão ser organizados, no mínimo, nas seguintes famílias:

1. identificação e candidatura;
2. validação de finalidade e autoridade;
3. avaliação contextual;
4. admissão e rejeição;
5. seleção de comportamento;
6. programação e prontidão;
7. apresentação e entrega;
8. resposta e relação do participante;
9. atenção, fadiga e frequência;
10. preferências, canais e horários protegidos;
11. sensibilidade e privacidade;
12. relações comerciais;
13. execução externa;
14. contestação e correção;
15. cancelamento, expiração e encerramento;
16. revogação e propagação;
17. sincronização e integração;
18. visualização e leitura;
19. falha, recuperação e reconstrução.

# 3088. Eventos de identificação

Deverão incluir, entre outros:

- `OportunidadeDeIntervencaoIdentificada`;
- `SinalDeIntervencaoRecebido`;
- `SolicitacaoDeIntervencaoRecebida`;
- `MudancaContextualRelacionada`;
- `PrazoFuncionalReconhecido`;
- `RiscoMaterialReconhecido`.

Identificação não deverá representar candidatura ou admissão.

# 3089. Evento de oportunidade identificada

`OportunidadeDeIntervencaoIdentificada` deverá registrar:

- origem;
- finalidade preliminar;
- participante;
- possível comportamento;
- temporalidade;
- sensibilidade;
- autoridade conhecida;
- relação comercial conhecida.

# 3090. Eventos de candidatura

Deverão incluir:

- `CandidaturaDeIntervencaoCriada`;
- `CandidaturaDeIntervencaoAtualizada`;
- `CandidaturaDeIntervencaoUnificada`;
- `CandidaturaDeIntervencaoRejeitada`;
- `DuplicidadeDeIntervencaoReconhecida`.

# 3091. Criação de candidatura

A candidatura somente deverá ser criada quando possuir elementos mínimos para avaliação.

Ela não deverá autorizar:

- entrega;
- notificação;
- execução;
- compartilhamento;
- criação de urgência.

# 3092. Deduplicação semântica

A duplicidade deverá ser avaliada por significado, não apenas por identificador.

Intervenções equivalentes originadas por sistemas diferentes deverão ser unificadas quando não houver diferença material.

# 3093. Eventos de finalidade

Deverão incluir:

- `FinalidadeDeIntervencaoValidada`;
- `FinalidadeDeIntervencaoLimitada`;
- `FinalidadeDeIntervencaoRejeitada`;
- `FinalidadeDeIntervencaoAlterada`.

Mudança material de finalidade deverá produzir nova avaliação e, quando necessário, novo agregado.

# 3094. Eventos de autoridade

Deverão incluir:

- `AutoridadeDeIntervencaoValidada`;
- `AutoridadeDeIntervencaoLimitada`;
- `AutoridadeDeIntervencaoRejeitada`;
- `ExcessoDeAutoridadeReconhecido`.

# 3095. Excesso de autoridade

Quando uma fonte ou consumidor exceder autoridade:

- novos efeitos deverão ser bloqueados;
- consumidores deverão ser notificados;
- o evento deverá ser contestável;
- os efeitos anteriores deverão ser reavaliados;
- a correção deverá preservar histórico.

# 3096. Eventos de avaliação contextual

Deverão incluir:

- `AvaliacaoDeIntervencaoIniciada`;
- `ContextoMinimoSelecionado`;
- `RelevanciaDeIntervencaoAvaliada`;
- `TemporalidadeDeIntervencaoAvaliada`;
- `AtencaoDoParticipanteAvaliada`;
- `InterruptibilidadeAvaliada`;
- `ImportanciaDeIntervencaoAvaliada`;
- `UrgenciaDeIntervencaoAvaliada`;
- `RiscoDeIntervencaoAvaliado`;
- `ReversibilidadeDeIntervencaoAvaliada`;
- `AlternativasDeIntervencaoAvaliadas`.

# 3097. Avaliação de relevância

`RelevanciaDeIntervencaoAvaliada` deverá registrar:

- critérios;
- contexto utilizado;
- contexto excluído;
- limitações;
- incerteza;
- alternativas;
- custo de interrupção.

Receita não deverá integrar positivamente a avaliação.

# 3098. Avaliação de atenção

`AtencaoDoParticipanteAvaliada` deverá ser tratada como estimativa limitada.

Não poderá declarar consentimento ou intenção.

# 3099. Avaliação de interruptibilidade

`InterruptibilidadeAvaliada` deverá considerar:

- horário;
- ambiente;
- canal;
- sensibilidade;
- urgência;
- preferência;
- possibilidade de adiamento.

Disponibilidade técnica do canal não deverá representar interruptibilidade.

# 3100. Avaliação de urgência

`UrgenciaDeIntervencaoAvaliada` deverá registrar o fundamento real da urgência.

Não poderá utilizar como fundamento:

- promoção;
- comissão;
- estoque;
- campanha;
- meta comercial;
- pressão social.

# 3101. Eventos de sensibilidade

Deverão incluir:

- `SensibilidadeDeIntervencaoClassificada`;
- `SensibilidadeDeIntervencaoElevada`;
- `ProtecaoVisualDeIntervencaoExigida`;
- `CanalProtegidoExigido`;
- `RetencaoDeIntervencaoLimitada`.

# 3102. Eventos de fadiga e frequência

Deverão incluir:

- `FadigaDeIntervencaoAvaliada`;
- `FrequenciaDeIntervencaoAvaliada`;
- `LimiteDeFrequenciaAplicado`;
- `IntervencoesAgrupadas`;
- `IntervencaoSuprimidaPorFadiga`;
- `IntervencaoAdiadaPorFadiga`;
- `IntensidadeReduzidaPorFadiga`.

# 3103. Fadiga elevada

Fadiga elevada deverá produzir redução de pressão.

Não deverá produzir:

- escalonamento comercial;
- linguagem mais persuasiva;
- repetição agressiva;
- troca para canal mais intrusivo.

# 3104. Eventos de admissão

Deverão incluir:

- `IntervencaoAdmitida`;
- `IntervencaoAdmitidaComCondicao`;
- `IntervencaoRejeitada`;
- `IntervencaoEncaminhadaParaAvaliacaoHumana`;
- `IntervencaoSilenciadaAposAvaliacao`.

# 3105. Evento de intervenção admitida

`IntervencaoAdmitida` deverá declarar que a manifestação atingiu limiar funcional suficiente.

Não deverá representar:

- apresentação;
- entrega;
- visualização;
- resposta;
- autorização para transação.

# 3106. Admissão condicionada

A condição deverá ser explícita, incluindo:

- horário;
- redução de fadiga;
- nova autorização;
- confirmação de informação;
- resolução de conflito;
- disponibilidade de canal;
- avaliação humana.

# 3107. Eventos de seleção de comportamento

Deverão incluir:

- `ComportamentoDeIntervencaoSelecionado`;
- `ComportamentoDeIntervencaoAlterado`;
- `AgirSelecionado`;
- `PerguntarSelecionado`;
- `InformarSelecionado`;
- `SugerirSelecionado`;
- `LembrarSelecionado`;
- `AlertarSelecionado`;
- `ConfirmarSelecionado`;
- `AguardarSelecionado`;
- `ObservarSelecionado`;
- `SilenciarSelecionado`.

# 3108. Seleção de comportamento

A seleção deverá declarar exatamente um comportamento principal.

Comportamentos auxiliares deverão permanecer identificados e não poderão ocultar a decisão principal.

# 3109. Evento de agir selecionado

`AgirSelecionado` somente poderá ocorrer com:

- autorização vigente;
- executor identificado;
- escopo delimitado;
- risco compatível;
- reversibilidade suficiente.

# 3110. Evento de perguntar selecionado

`PerguntarSelecionado` deverá registrar:

- informação necessária;
- finalidade;
- efeitos da resposta;
- efeitos da ausência;
- possibilidade de recusa;
- possibilidade de resposta posterior.

# 3111. Evento de alertar selecionado

`AlertarSelecionado` deverá declarar:

- risco ou mudança material;
- fonte;
- validade;
- impacto;
- urgência;
- limites;
- ações disponíveis.

# 3112. Eventos de programação

Deverão incluir:

- `IntervencaoProgramada`;
- `IntervencaoReprogramada`;
- `JanelaDeEntregaDefinida`;
- `IntervencaoAguardandoCondicao`;
- `CondicaoDeRetomadaReconhecida`;
- `IntervencaoExpiradaAntesDaEntrega`.

# 3113. Programação

`IntervencaoProgramada` deverá registrar:

- data, período ou condição;
- fuso horário;
- canal;
- validade;
- regra de reavaliação;
- condição de cancelamento;
- horário protegido aplicável.

# 3114. Eventos de prontidão

Deverão incluir:

- `IntervencaoPronta`;
- `ProntidaoDeIntervencaoRevogada`;
- `IntervencaoBloqueadaAntesDaEntrega`;
- `AutorizacaoDeIntervencaoExpirada`;
- `InformacaoDeIntervencaoDesatualizada`.

# 3115. Verificação anterior à entrega

Antes da entrega, deverão ser revalidados:

- autorização;
- validade;
- horário;
- canal;
- sensibilidade;
- fadiga;
- preferências;
- mudanças materiais;
- revogações;
- conflitos.

# 3116. Eventos de apresentação

Deverão incluir:

- `IntervencaoApresentada`;
- `PerguntaContextualApresentada`;
- `InformacaoContextualApresentada`;
- `SugestaoContextualApresentada`;
- `LembreteContextualApresentado`;
- `AlertaContextualApresentado`;
- `ConfirmacaoContextualSolicitada`.

Apresentação não representa entrega técnica confirmada ou visualização.

# 3117. Eventos de entrega

Deverão incluir:

- `EntregaDeIntervencaoIniciada`;
- `IntervencaoEnviada`;
- `IntervencaoParcialmenteEntregue`;
- `IntervencaoEntregue`;
- `EntregaDeIntervencaoConfirmada`;
- `EntregaDeIntervencaoFalhou`;
- `EntregaDeIntervencaoCancelada`.

# 3118. Confirmação técnica de entrega

`EntregaDeIntervencaoConfirmada` não deverá representar:

- leitura;
- compreensão;
- concordância;
- interesse;
- resposta;
- consentimento;
- ação externa.

# 3119. Entrega parcial

A entrega parcial deverá identificar:

- componentes entregues;
- componentes pendentes;
- destinatários afetados;
- risco de duplicidade;
- possibilidade de repetição;
- efeitos já aplicados.

# 3120. Eventos de visualização

Deverão incluir:

- `CentralDeIntervencoesVisualizada`;
- `FilaDeAtencaoVisualizada`;
- `IntervencaoVisualizada`;
- `DetalhamentoDeIntervencaoVisualizado`;
- `JustificativaDeIntervencaoVisualizada`;
- `JustificativaTemporalVisualizada`;
- `HistoricoDeIntervencaoVisualizado`.

Visualização não deverá alterar interesse ou prioridade.

# 3121. Eventos de resposta

Deverão incluir:

- `IntervencaoRespondida`;
- `RespostaDeIntervencaoAceita`;
- `RespostaDeIntervencaoRecusada`;
- `RespostaDeIntervencaoAdiada`;
- `DetalhesDeIntervencaoSolicitados`;
- `RespostaDeIntervencaoAmbigua`;
- `ConfirmacaoParcialRecebida`.

# 3122. Resposta ambígua

Uma resposta ambígua não deverá produzir efeito material.

Ela deverá gerar:

- solicitação de esclarecimento;
- limitação de automação;
- preservação do estado anterior;
- registro de incerteza.

# 3123. Ausência de resposta

A ausência de resposta poderá gerar:

- espera;
- encerramento;
- repetição limitada;
- agrupamento;
- silêncio.

Não deverá produzir recusa, desinteresse ou julgamento.

# 3124. Eventos de adiamento

Deverão incluir:

- `IntervencaoAdiadaPeloParticipante`;
- `IntervencaoAdiadaPeloSistema`;
- `DataDeRetomadaDefinida`;
- `CondicaoDeRetomadaDefinida`;
- `AdiamentoSemDataRegistrado`.

# 3125. Adiamento e recusa

Adiamento não representa recusa.

Recusa não representa:

- incapacidade;
- falha;
- falta de disciplina;
- ausência de valor;
- desinteresse definitivo.

# 3126. Eventos de silêncio

Deverão incluir:

- `IntervencaoSilenciada`;
- `IntervencaoSilenciadaPeloParticipante`;
- `IntervencaoSilenciadaPorFadiga`;
- `IntervencaoSilenciadaPorSensibilidade`;
- `CategoriaDeIntervencaoSilenciada`;
- `CanalDeIntervencaoSilenciado`;
- `PeriodoDeSilencioDefinido`.

# 3127. Silêncio como evento

O silêncio deverá ser reconhecido como decisão funcional válida.

Ele não deverá ser contabilizado como falha de engajamento.

# 3128. Eventos de recusa, ocultação e bloqueio

Deverão incluir:

- `IntervencaoRecusadaPeloParticipante`;
- `IntervencaoOcultadaPeloParticipante`;
- `EscopoDeIntervencaoBloqueado`;
- `FonteDeIntervencaoBloqueada`;
- `OrganizacaoDeIntervencaoBloqueada`;
- `CanalDeIntervencaoBloqueado`;
- `EscopoDeIntervencaoDesbloqueado`.

# 3129. Eventos de preferências

Deverão incluir:

- `PreferenciaDeFrequenciaAlterada`;
- `PreferenciaDeCanalAlterada`;
- `PreferenciaDeCategoriaAlterada`;
- `PreferenciaDeIntensidadeAlterada`;
- `HorarioProtegidoConfigurado`;
- `HorarioProtegidoRemovido`;
- `ModoDiscretoAtivado`;
- `ModoDiscretoDesativado`;
- `ResumoDeIntervencoesConfigurado`.

# 3130. Aplicação de preferências

Preferências deverão produzir efeitos somente dentro de seu escopo.

Alteração de preferência não deverá reescrever eventos anteriores.

# 3131. Eventos comerciais

Deverão incluir:

- `RelacaoComercialDeIntervencaoDeclarada`;
- `PatrocinioDeIntervencaoDeclarado`;
- `ComissaoDeIntervencaoDeclarada`;
- `PublicidadeDeIntervencaoIdentificada`;
- `RelacaoComercialOcultaReconhecida`;
- `InterferenciaComercialBloqueada`.

# 3132. Relação comercial oculta

A ocultação de relação comercial deverá:

- limitar apresentação;
- gerar incidente de governança;
- exigir correção;
- impedir classificação funcional neutra;
- notificar consumidores afetados.

# 3133. Eventos de execução externa

Deverão incluir:

- `ExecucaoExternaSolicitada`;
- `ExecucaoExternaAutorizada`;
- `ExecucaoExternaIniciada`;
- `ExecucaoExternaConcluida`;
- `ExecucaoExternaFalhou`;
- `ResultadoExternoRecebido`;
- `EstadoExternoAtualizado`.

# 3134. Autoridade do executor externo

O produto ou sistema externo deverá governar sua própria operação.

Intervenções Contextuais não deverá declarar conclusão antes do retorno autorizado do executor.

# 3135. Eventos de contestação

Deverão incluir:

- `IntervencaoContestada`;
- `FundamentoDeIntervencaoContestado`;
- `UrgenciaDeIntervencaoContestada`;
- `FonteDeIntervencaoContestada`;
- `UsoDeContextoContestado`;
- `RelacaoComercialContestada`;
- `EfeitosDeIntervencaoLimitados`.

# 3136. Efeitos da contestação

Uma contestação material deverá poder:

- suspender repetição;
- limitar automação;
- bloquear execução;
- reduzir confiança;
- exigir avaliação humana;
- preservar evidências;
- notificar consumidores.

# 3137. Eventos de correção

Deverão incluir:

- `CorrecaoDeIntervencaoSolicitada`;
- `ErroDeIntervencaoReconhecido`;
- `CorrecaoDeIntervencaoAplicada`;
- `EfeitosDeIntervencaoRecompostos`;
- `ConsumidoresDeIntervencaoNotificados`;
- `IntervencaoReavaliadaAposCorrecao`.

# 3138. Correção compensatória

Correções deverão produzir novos eventos.

Não deverão:

- apagar evento anterior;
- alterar o passado;
- ocultar erro;
- remover autoria;
- perder consumidores afetados.

# 3139. Eventos de cancelamento e expiração

Deverão incluir:

- `IntervencaoCancelada`;
- `IntervencaoExpirada`;
- `IntervencaoEncerrada`;
- `IntervencaoReaberta`;
- `NovoCicloDeIntervencaoCriado`.

# 3140. Reabertura e novo ciclo

A reabertura somente deverá ocorrer quando finalidade e identidade funcional forem preservadas.

Mudança material deverá criar novo ciclo ou novo agregado.

# 3141. Eventos de revogação

Deverão incluir:

- `RevogacaoDeIntervencaoSolicitada`;
- `NovosUsosDeIntervencaoBloqueados`;
- `RevogacaoDeIntervencaoEmPropagacao`;
- `ConsumidorDeIntervencaoRevogado`;
- `RevogacaoDeIntervencaoPropagada`;
- `FalhaDePropagacaoDeRevogacaoReconhecida`.

# 3142. Conclusão da revogação

A revogação somente deverá ser considerada concluída quando houver confirmação suficiente de que:

- novas avaliações foram interrompidas;
- novas entregas foram bloqueadas;
- novos compartilhamentos cessaram;
- consumidores relevantes aplicaram o bloqueio;
- pendências foram identificadas.

# 3143. Eventos de integração e sincronização

Deverão incluir:

- `IntegracaoDeIntervencaoConectada`;
- `IntegracaoDeIntervencaoPausada`;
- `IntegracaoDeIntervencaoDesconectada`;
- `SincronizacaoDeIntervencaoIniciada`;
- `SincronizacaoDeIntervencaoConcluida`;
- `SincronizacaoDeIntervencaoPendente`;
- `ConflitoDeSincronizacaoReconhecido`;
- `SincronizacaoDeIntervencaoReconciliada`.

# 3144. Idempotência

Eventos materiais deverão possuir chave de idempotência.

O reprocessamento não deverá duplicar:

- candidatura;
- admissão;
- programação;
- apresentação;
- entrega;
- pergunta;
- lembrete;
- alerta;
- resposta;
- execução;
- contestação;
- correção;
- revogação.

# 3145. Duplicidade semântica

Eventos com identificadores diferentes, mas significado material equivalente, deverão ser reconhecidos como duplicados.

# 3146. Ordenação

A ordenação deverá considerar:

- versão;
- sequência;
- temporalidade;
- causalidade;
- dependências;
- revogações;
- correções;
- estado atual.

# 3147. Eventos fora de ordem

Eventos fora de ordem deverão ser:

- preservados;
- validados;
- retidos quando necessário;
- aplicados somente quando seguros;
- reconciliados;
- auditáveis.

Eles não deverão criar estados impossíveis.

# 3148. Concorrência

Alterações concorrentes deverão utilizar:

- versão esperada;
- detecção de conflito;
- decisão explícita de reconciliação;
- preservação das propostas concorrentes;
- ausência de sobrescrita silenciosa.

# 3149. Atomicidade funcional

Operações compostas deverão declarar:

- efeitos inseparáveis;
- efeitos independentes;
- sequência;
- compensações;
- condição de sucesso;
- condição de falha.

# 3150. Eventos de falha

Deverão incluir:

- `FalhaDeAvaliacaoDeIntervencaoReconhecida`;
- `FalhaDeProgramacaoDeIntervencaoReconhecida`;
- `FalhaDeEntregaDeIntervencaoReconhecida`;
- `FalhaDeExecucaoExternaReconhecida`;
- `FalhaDePersistenciaDeIntervencaoReconhecida`;
- `FalhaDePropagacaoReconhecida`;
- `FalhaParcialDeIntervencaoReconhecida`;
- `IntervencaoRecuperadaDeFalha`.

# 3151. Falha segura

Em falha, o sistema deverá:

- preservar o último estado válido;
- impedir falsa entrega;
- bloquear efeitos críticos;
- evitar duplicidade;
- reduzir automação;
- identificar o impacto;
- permitir recuperação;
- informar limitações.

# 3152. Falha parcial

Falha parcial não deverá ser apresentada como sucesso integral.

O evento deverá declarar:

- etapas concluídas;
- etapas pendentes;
- efeitos aplicados;
- efeitos não aplicados;
- risco de repetição;
- necessidade de compensação.

# 3153. Reconstrução

O estado deverá ser reconstruível a partir de:

- eventos válidos;
- versões;
- decisões;
- permissões;
- preferências;
- correções;
- contestações;
- revogações;
- confirmações;
- falhas;
- reconciliações.

# 3154. Retenção

A retenção deverá ser proporcional a:

- finalidade;
- sensibilidade;
- obrigação legítima;
- necessidade de auditoria;
- contestação;
- segurança;
- revogação.

# 3155. Logs

Logs não deverão conter narrativas pessoais completas quando identificadores e metadados funcionais forem suficientes.

# 3156. Responsabilidades dos produtores

Produtores deverão validar:

- identidade;
- contrato;
- autoridade;
- finalidade;
- temporalidade;
- proveniência;
- sensibilidade;
- minimização;
- idempotência;
- versão.

# 3157. Responsabilidades dos consumidores

Consumidores deverão validar:

- versão;
- finalidade;
- permissões;
- escopo;
- idempotência;
- ordenação;
- revogação;
- sensibilidade;
- autoridade.

Consumidores não deverão ampliar significado ou autoridade.

# 3158. Compatibilidade

Mudanças compatíveis poderão:

- adicionar campos opcionais;
- adicionar tipos não materiais;
- ampliar metadados;
- preservar consumidores anteriores.

Mudanças incompatíveis deverão exigir nova versão contratual.

# 3159. Explicabilidade

Todo efeito material deverá permitir explicar:

- qual fato ocorreu;
- qual fonte originou;
- qual autoridade existia;
- qual finalidade foi aplicada;
- qual contexto foi utilizado;
- qual decisão funcional foi tomada;
- quais consumidores receberam;
- quais efeitos foram produzidos;
- quais incertezas permaneceram.

# 3160. Auditoria

A auditoria deverá reconstruir o fluxo desde:

sinal, solicitação ou mudança
→ candidatura
→ avaliação
→ admissão ou silêncio
→ seleção do comportamento
→ programação
→ apresentação
→ entrega
→ resposta
→ correção, revogação ou encerramento

# 3161. Métricas dos eventos

Métricas futuras poderão avaliar:

- eventos sem autoridade;
- eventos sem finalidade;
- eventos duplicados;
- eventos fora de ordem;
- falhas de idempotência;
- relações comerciais omitidas;
- revogações não propagadas;
- correções incompletas;
- falhas parciais apresentadas como sucesso;
- exposição excessiva de dados sensíveis;
- consumidores incompatíveis;
- tempo de recuperação;
- capacidade de reconstrução.

As métricas deverão avaliar o sistema, não o participante.

# 3162. Comportamentos proibidos

Os contratos não deverão:

1. publicar comando como evento;
2. publicar proposta como fato concluído;
3. publicar evento material antes da persistência;
4. reescrever eventos históricos;
5. ocultar correções;
6. ampliar autoridade da fonte;
7. utilizar finalidade genérica;
8. publicar payload excessivo;
9. omitir relação comercial;
10. inferir consentimento por atenção;
11. inferir interesse por visualização;
12. converter ausência de resposta em recusa;
13. converter adiamento em rejeição;
14. converter silêncio em falha;
15. fabricar urgência comercial;
16. duplicar efeitos no reprocessamento;
17. ignorar versão esperada;
18. sobrescrever conflitos;
19. aplicar evento fora de ordem de forma insegura;
20. declarar revogação antes da propagação;
21. declarar entrega após falha parcial;
22. declarar execução externa sem retorno autorizado;
23. ocultar consumidores afetados;
24. formar perfil paralelo de terceiro;
25. avaliar mérito, fé, disciplina ou valor humano.

# 3163. Critérios de aceite

A extensão será considerada consolidada quando:

1. distinguir comando, proposta e evento;
2. definir persistência anterior à publicação;
3. definir o agregado funcional;
4. definir estrutura comum;
5. definir identidade e versão;
6. definir participante, ator e autoridade;
7. definir fonte e finalidade;
8. definir temporalidades;
9. definir correlação e causalidade;
10. definir proveniência;
11. definir sensibilidade e minimização;
12. definir relações comerciais;
13. definir famílias de eventos;
14. governar identificação e candidatura;
15. governar finalidade e autoridade;
16. governar avaliação contextual;
17. governar atenção, urgência e fadiga;
18. governar admissão;
19. governar seleção de comportamento;
20. governar programação e prontidão;
21. governar apresentação e entrega;
22. governar visualização e resposta;
23. governar ausência de resposta;
24. governar adiamento e silêncio;
25. governar recusa, ocultação e bloqueio;
26. governar preferências;
27. governar execução externa;
28. governar contestação e correção;
29. governar cancelamento e expiração;
30. governar revogação e propagação;
31. governar sincronização;
32. governar idempotência;
33. governar ordenação;
34. governar concorrência;
35. governar atomicidade;
36. governar falha segura;
37. assegurar reconstrução;
38. assegurar retenção proporcional;
39. definir produtores e consumidores;
40. assegurar compatibilidade;
41. assegurar explicabilidade;
42. assegurar auditoria;
43. definir métricas sistêmicas;
44. proibir manipulação;
45. manter o participante no controle.

# 3164. Continuidade normativa

`PAS-001-IC-EVENT-001 1.0.0` é registrado como a **quarta extensão normativa da Capacidade 07 — Intervenções Contextuais**.

A extensão:

- preserva `PAS-001-IC-FOUNDATION-001 1.0.0`;
- preserva `PAS-001-IC-LIFECYCLE-001 1.0.0`;
- preserva `PAS-001-IC-VIEW-001 1.0.0`;
- preserva o `PAS-001 0.5.0`;
- mantém as Capacidades 02 a 06 como `Functionally complete`;
- mantém a Capacidade 07 como `In progress`;
- eleva o progresso editorial de `60%` para `80%`;
- preserva a Capacidade 08 como `Planned`;
- consolida a estrutura comum dos eventos;
- governa autoridade, finalidade, temporalidade, proveniência e sensibilidade;
- consolida os eventos de identificação, avaliação, admissão, comportamento, programação, entrega e resposta;
- governa adiamento, silêncio, contestação, correção e revogação;
- assegura idempotência, ordenação, concorrência, reconstrução e falha segura;
- estabelece as integrações funcionais como próxima etapa normativa.

O próximo bloco será:

> **Integrações funcionais da Capacidade de Intervenções Contextuais com Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, canais, calendários, localização, fontes públicas e sistemas externos, incluindo finalidade, minimização, autoridade, sincronização, revogação, propagação, neutralidade comercial, observabilidade e falha segura.**
