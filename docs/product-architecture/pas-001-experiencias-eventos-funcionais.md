---
id: PAS-001-EXP-EVENT-001
title: Contratos dos Eventos Funcionais da Capacidade de Experiências
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-17
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-EXP-FOUNDATION-001
  - PAS-001-EXP-LIFECYCLE-001
  - PAS-001-EXP-VIEW-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - PAS-001-IC-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-007
---

# PAS-001-EXP-EVENT-001 — Contratos dos Eventos Funcionais da Capacidade de Experiências

## 1. Autoridade e vínculo

Este documento é a **quarta extensão normativa da Capacidade 08 — Experiências** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser interpretado como continuidade do `PAS-001-EXP-FOUNDATION-001 1.0.0`, do `PAS-001-EXP-LIFECYCLE-001 1.0.0`, do `PAS-001-EXP-VIEW-001 1.0.0`, do `PAS-001 0.5.0`, das seções 1 a 3651, dos contratos finais das Capacidades 02 a 07, da `GLPA-001` e da `GIA-000`.

Esta extensão mantém a Capacidade 08 como `In progress` e eleva o progresso editorial de referência de `60%` para `80%`.

As Capacidades 02, 03, 04, 05, 06 e 07 permanecem `Functionally complete`. A Capacidade 09 — Evolução Contínua permanece `Planned`.

A aprovação desta extensão não autoriza integrações técnicas irrestritas. Os contratos de integração e o contrato final deverão ser consolidados em extensões posteriores.


# 3652. Finalidade dos contratos de eventos

Os contratos de eventos deverão definir como fatos funcionais relacionados a Experiências são:

- reconhecidos;
- persistidos;
- versionados;
- publicados;
- consumidos;
- ordenados;
- corrigidos;
- revogados;
- propagados;
- reconstruídos;
- auditados.

O contrato deverá impedir que sinais técnicos, comandos, propostas, reservas, compras, presença presumida, declarações sem autoridade, inferências, registros comerciais ou efeitos externos sejam tratados como experiência efetivamente vivida.

# 3653. Pergunta central

Os contratos deverão responder:

> **Como fatos relacionados a uma experiência podem ser reconhecidos, persistidos, publicados e consumidos sem transformar intenção, atividade, presença, declaração de terceiro, inferência, entrega ou resultado em vivência, satisfação, significado ou transformação?**

# 3654. Sinal, comando, proposta, declaração, evento e efeito

Deverão permanecer distintos:

- **sinal**: informação que pode justificar avaliação;
- **comando**: solicitação para avaliar ou alterar estado;
- **proposta**: possibilidade ainda sujeita a decisão;
- **declaração**: informação atribuída a um ator;
- **evento funcional**: fato reconhecido e persistido que ocorreu no domínio;
- **efeito**: consequência produzida por consumidor autorizado.

Exemplo:

```text
localização observada
≠ possível experiência identificada
≠ experiência candidata
≠ ocorrência em validação
≠ presença confirmada
≠ participação confirmada
≠ experiência concluída
```

# 3655. Fluxo funcional de reconhecimento

O fluxo de referência será:

```text
sinal, comando, proposta ou declaração
→ validação de identidade
→ validação de autoridade
→ validação de finalidade
→ classificação de sensibilidade
→ avaliação funcional
→ decisão
→ persistência suficiente
→ evento reconhecido
→ atualização versionada do agregado
→ produção de recortes minimizados
→ publicação
→ consumo autorizado
→ efeito observável
```

Nenhum evento material deverá ser publicado antes da persistência funcional suficiente.

# 3656. Princípios obrigatórios

Os eventos deverão observar:

- imutabilidade histórica;
- correção compensatória;
- titularidade explícita;
- autoridade limitada;
- finalidade específica;
- temporalidade múltipla;
- proveniência;
- minimização;
- sensibilidade;
- versionamento;
- idempotência;
- ordenação;
- concorrência segura;
- atomicidade;
- explicabilidade;
- auditabilidade;
- neutralidade comercial;
- proteção de terceiros;
- falha segura;
- controle do participante.

# 3657. Agregado funcional principal

O agregado funcional principal será denominado:

> **Registro de Experiência**

O agregado deverá preservar:

- identidade permanente;
- titularidade;
- participantes e papéis;
- modalidade;
- origem;
- finalidade;
- estado funcional;
- estado da informação;
- estado da ocorrência;
- temporalidades;
- presença;
- participação;
- envolvimento;
- agência;
- autonomia;
- entregas;
- resultados;
- efeitos;
- percepção;
- satisfação;
- evidências;
- memórias;
- significado;
- reflexão;
- autorizações;
- compartilhamentos;
- relações comerciais;
- contestações;
- correções;
- revogações;
- versões;
- histórico;
- falhas.

# 3658. Identidade permanente do agregado

Cada Registro de Experiência deverá possuir identidade permanente.

Correções, novas evidências, mudanças de percepção, alteração de satisfação, inclusão de memória ou revisão de significado não deverão criar novo agregado quando permanecerem relacionadas à mesma experiência.

Mudança material de titularidade, finalidade, atividade, contexto ou identidade temporal poderá exigir novo agregado.

# 3659. Estrutura comum do evento

Todo evento funcional deverá conter, conforme aplicável:

| Campo | Finalidade |
|---|---|
| `event_id` | Identidade imutável do evento |
| `event_type` | Tipo funcional |
| `event_version` | Versão do contrato |
| `aggregate_id` | Registro de Experiência afetado |
| `aggregate_version` | Versão resultante |
| `expected_version` | Versão anterior esperada |
| `participant_id` | Titular ou participante principal |
| `participant_category` | Pessoa, Organização ou Coletivo |
| `actor_id` | Agente que originou o fato |
| `actor_role` | Papel funcional do ator |
| `authority_scope` | Escopo de autoridade |
| `source_id` | Fonte original |
| `purpose` | Finalidade específica |
| `occurred_at` | Momento real do fato |
| `declared_at` | Momento da declaração |
| `known_at` | Momento do conhecimento |
| `recognized_at` | Momento do reconhecimento funcional |
| `recorded_at` | Momento da persistência |
| `published_at` | Momento da publicação |
| `effective_at` | Momento de aplicação |
| `correlation_id` | Fluxo relacionado |
| `causation_id` | Evento ou comando causador |
| `idempotency_key` | Prevenção de duplicidade |
| `sensitivity` | Classificação de sensibilidade |
| `permissions` | Permissões aplicáveis |
| `provenance` | Origem e transformações |
| `commercial_relation` | Relação comercial aplicável |
| `payload` | Conteúdo funcional minimizado |
| `authorized_consumers` | Consumidores autorizados |
| `retention_policy` | Política de retenção |
| `uncertainty` | Incertezas conhecidas |
| `metadata` | Dados técnicos sem semântica de domínio |

# 3660. Identidade do evento

O `event_id` deverá ser:

- único;
- permanente;
- imutável;
- não reutilizável;
- independente da fila;
- independente do consumidor;
- preservado em retransmissões, correções e auditorias.

Eventos equivalentes não deverão receber novas identidades apenas por retentativa.

# 3661. Tipo e versão contratual

O `event_type` deverá representar semântica funcional estável.

Exemplo:

```text
ExperienciaConcluida
event_version: 1.0.0
```

Mudança incompatível deverá produzir nova versão contratual. Mudança técnica sem alteração semântica não deverá gerar novo tipo funcional.

# 3662. Versão do agregado

Toda alteração material deverá avançar `aggregate_version`.

`expected_version` deverá permitir detectar:

- sobrescrita silenciosa;
- aplicação duplicada;
- regressão de estado;
- concorrência;
- perda de correção;
- evento fora de ordem.

# 3663. Titular, participante, ator e terceiro afetado

Deverão permanecer distintos:

- titular da experiência;
- participante;
- ator que originou o fato;
- fonte;
- executor;
- organização relacionada;
- profissional;
- terceiro afetado;
- consumidor.

Pagamento, patrocínio, organização, fornecimento ou acesso técnico não transferem titularidade.

# 3664. Papéis funcionais

O evento deverá declarar o papel do ator, incluindo, conforme aplicável:

- participante;
- titular;
- representante autorizado;
- convidado;
- observador;
- facilitador;
- executor;
- fonte;
- avaliador;
- organização;
- profissional;
- sistema;
- produto especializado;
- operador;
- auditor;
- processo de reconciliação.

# 3665. Autoridade

A autoridade deverá indicar o que o ator podia legitimamente:

- declarar;
- solicitar;
- confirmar;
- negar;
- avaliar;
- executar;
- compartilhar;
- corrigir;
- revogar.

A posse de dados, acesso técnico ou relação comercial não deverá ampliar autoridade.

# 3666. Limites de autoridade pessoal e institucional

O participante possui autoridade principal sobre:

- própria presença;
- própria participação;
- própria percepção;
- própria satisfação;
- próprias memórias;
- próprio significado;
- próprias permissões.

Organizações e profissionais poderão confirmar fatos institucionais dentro do próprio escopo, mas não deverão declarar percepção, satisfação, significado, transformação, evolução, mérito ou fé do participante.

# 3667. Fonte

A fonte deverá declarar:

- identidade;
- tipo;
- responsável;
- autoridade;
- validade;
- confiabilidade;
- método de obtenção;
- relação comercial;
- cadeia de transformação.

Fonte sem autoridade suficiente poderá originar candidatura, mas não confirmação material.

# 3668. Finalidade

Todo evento deverá possuir finalidade específica e limitada.

Não serão suficientes finalidades genéricas como:

- aumentar engajamento;
- elevar conversão;
- melhorar retenção;
- gerar receita;
- personalizar ofertas;
- ampliar tempo de tela;
- otimizar publicidade.

Finalidade comercial não deverá justificar uso de contexto pessoal ou sensível.

# 3669. Temporalidades

O contrato deverá distinguir, quando aplicável:

- momento previsto;
- momento real do fato;
- momento da presença;
- momento da participação;
- momento da declaração;
- momento da observação;
- momento do conhecimento;
- momento da avaliação;
- momento do reconhecimento;
- momento da persistência;
- momento da publicação;
- momento da aplicação;
- momento da entrega;
- momento do resultado;
- momento da percepção;
- momento da memória;
- momento da correção;
- momento da revogação;
- momento da propagação.

# 3670. Fato, declaração, conhecimento e registro

O momento real do fato deverá permanecer distinto do momento da declaração, do conhecimento e do registro.

Eventos retrospectivos deverão preservar essa diferença e não poderão ser apresentados como recebidos em tempo real.

# 3671. Precisão temporal

A precisão original deverá ser preservada:

- instante;
- intervalo;
- data;
- mês;
- ano;
- período aproximado;
- desconhecido.

Datas aproximadas não deverão ser convertidas silenciosamente em datas exatas.

# 3672. Correlação

`correlation_id` deverá relacionar eventos do mesmo fluxo funcional.

Correlação não deverá representar causalidade.

# 3673. Causalidade funcional

`causation_id` somente deverá indicar causalidade demonstrável.

Proximidade temporal, localização, abertura de aplicativo, clique, compra, presença ou conteúdo visualizado não deverão ser tratados como causa suficiente de participação, satisfação, significado ou transformação.

# 3674. Proveniência

A proveniência deverá permitir reconstruir:

```text
fonte original
→ captura ou declaração
→ validação
→ transformação
→ avaliação
→ decisão
→ persistência
→ evento
→ consumidor
→ efeito
```

# 3675. Sensibilidade

A sensibilidade deverá governar:

- payload;
- logs;
- consumidores;
- retenção;
- visualização;
- notificação;
- compartilhamento;
- exportação;
- auditoria;
- proteção de terceiros.

Experiências relacionadas a saúde, religião, finanças, trauma, luto, vulnerabilidade, violência, situação jurídica ou localização protegida deverão receber proteção reforçada.

# 3676. Minimização do payload

O payload deverá conter somente o necessário para a finalidade declarada.

Narrativas integrais, mídias, localização precisa, nomes de terceiros, percepção, satisfação, memória e significado deverão ser excluídos quando um recorte funcional for suficiente.

# 3677. Relação comercial

Eventos influenciados por:

- publicidade;
- patrocínio;
- comissão;
- afiliação;
- campanha;
- exclusividade;
- participação na receita;
- fornecimento;

deverão declarar a relação comercial.

A relação comercial não deverá alterar ocorrência, presença, participação, percepção, satisfação, significado, prioridade funcional ou propagação.

# 3678. Incerteza

Todo evento baseado em informação incompleta, estimada ou inferida deverá declarar:

- tipo de incerteza;
- fundamento;
- limites;
- informação ausente;
- possibilidade de contestação;
- efeitos suspensos.

Incerteza não deverá ser removida por conveniência de interface ou consumo.

# 3679. Famílias de eventos

Os eventos deverão ser organizados, no mínimo, nas seguintes famílias:

1. identificação e candidatura;
2. identidade, titularidade, autoridade e finalidade;
3. ocorrência e reconhecimento histórico;
4. planejamento, preparação e prontidão;
5. início, presença e participação;
6. envolvimento, agência e continuidade;
7. pausa, retomada e encerramento;
8. recorrência, séries e episódios;
9. entregas, resultados e efeitos;
10. percepção e satisfação;
11. evidências e proveniência;
12. memórias, mídias e autoria;
13. significado, reflexão e candidaturas;
14. participantes e experiências compartilhadas;
15. visualização e controle;
16. privacidade, permissões e compartilhamento;
17. relações comerciais e execução externa;
18. contestação, correção e revogação;
19. sincronização, falha, recuperação e reconstrução.

# 3680. Família 1 — Identificação e candidatura

Deverão incluir, entre outros:

- `PossivelExperienciaIdentificada`;
- `SinalDeExperienciaRecebido`;
- `ExperienciaCandidataCriada`;
- `ExperienciaCandidataAtualizada`;
- `ExperienciasCandidatasUnificadas`;
- `DuplicidadeDeExperienciaReconhecida`;
- `ExperienciaCandidataRejeitada`;

Identificação não deverá representar ocorrência, planejamento, presença ou participação.

A candidatura somente deverá existir quando houver elementos mínimos para avaliação e não autorizará exposição, notificação, compartilhamento ou uso comercial.

# 3681. Evento de possível experiência identificada

Deverão incluir, entre outros:

- `PossivelExperienciaIdentificada`;

O evento deverá registrar origem, titular potencial, atividade ou situação possível, temporalidade, contexto mínimo, autoridade conhecida, sensibilidade, relação comercial e incerteza.

# 3682. Deduplicação semântica

Deverão incluir, entre outros:

- `ExperienciasCandidatasUnificadas`;
- `DuplicidadeDeExperienciaReconhecida`;

A duplicidade deverá ser avaliada por significado funcional, participantes, temporalidade, atividade, contexto e fonte, não apenas por identificador técnico.

# 3683. Família 2 — Identidade, titularidade, autoridade e finalidade

Deverão incluir, entre outros:

- `IdentidadeDeExperienciaValidada`;
- `IdentidadeDeExperienciaContestada`;
- `TitularidadeDeExperienciaReconhecida`;
- `AutoridadeDeFonteValidada`;
- `AutoridadeDeFonteLimitada`;
- `AutoridadeDeFonteRejeitada`;
- `ExcessoDeAutoridadeReconhecido`;
- `FinalidadeDeExperienciaValidada`;
- `FinalidadeDeExperienciaLimitada`;
- `FinalidadeDeExperienciaRejeitada`;

Mudança material de titularidade ou finalidade deverá produzir nova avaliação e poderá exigir novo agregado.

# 3684. Excesso de autoridade

Deverão incluir, entre outros:

- `ExcessoDeAutoridadeReconhecido`;

Quando uma fonte, produtor ou consumidor exceder autoridade:

- novos efeitos incompatíveis deverão ser bloqueados;
- consumidores afetados deverão ser identificados;
- o participante deverá poder contestar;
- efeitos anteriores deverão ser reavaliados;
- a correção deverá preservar histórico.

# 3685. Família 3 — Ocorrência e reconhecimento histórico

Deverão incluir, entre outros:

- `ValidacaoDeOcorrenciaIniciada`;
- `OcorrenciaDeExperienciaConsideradaPossivel`;
- `OcorrenciaDeExperienciaConsideradaProvavel`;
- `OcorrenciaDeExperienciaParcialmenteConfirmada`;
- `OcorrenciaDeExperienciaConfirmada`;
- `OcorrenciaDeExperienciaNaoConfirmada`;
- `OcorrenciaDeExperienciaDivergente`;
- `OcorrenciaDeExperienciaInconclusiva`;
- `ReconhecimentoHistoricoDeExperienciaIniciado`;
- `ExperienciaHistoricaReconhecida`;

Ocorrência deverá permanecer distinta de presença, participação, conclusão, resultado e satisfação.

# 3686. Confirmação de ocorrência

Deverão incluir, entre outros:

- `OcorrenciaDeExperienciaConfirmada`;

A confirmação deverá registrar fontes, autoridade, escopo confirmado, temporalidade, participantes abrangidos, evidências e limitações.

A confirmação da experiência não confirmará automaticamente a participação individual de todos os associados.

# 3687. Reconhecimento histórico

Deverão incluir, entre outros:

- `ReconhecimentoHistoricoDeExperienciaIniciado`;
- `ExperienciaHistoricaReconhecida`;

A reconstrução retrospectiva deverá preservar:

- fontes;
- lacunas;
- datas conhecidas;
- datas estimadas;
- eventos ausentes;
- incertezas;
- momento da reconstrução;
- responsável pela validação.

# 3688. Família 4 — Planejamento, preparação e prontidão

Deverão incluir, entre outros:

- `ExperienciaPlanejada`;
- `PlanejamentoDeExperienciaAtualizado`;
- `PreparacaoDeExperienciaIniciada`;
- `CondicaoDeExperienciaSatisfeita`;
- `CondicaoDeExperienciaPendente`;
- `ExperienciaPreparada`;
- `ExperienciaPronta`;
- `ProntidaoDeExperienciaRevogada`;

Planejamento, reserva, inscrição, compra, autorização ou preparação não deverão representar início ou ocorrência.

# 3689. Evento de experiência pronta

Deverão incluir, entre outros:

- `ExperienciaPronta`;

`ExperienciaPronta` deverá indicar apenas que condições mínimas conhecidas foram satisfeitas. Não representará início, presença ou participação.

# 3690. Família 5 — Início, presença e participação

Deverão incluir, entre outros:

- `ExperienciaIniciada`;
- `PresencaEmExperienciaDeclarada`;
- `PresencaEmExperienciaConfirmada`;
- `PresencaEmExperienciaContestada`;
- `ParticipacaoEmExperienciaIniciada`;
- `ParticipacaoEmExperienciaConfirmada`;
- `ParticipacaoEmExperienciaNegada`;
- `PapelDeParticipanteAtualizado`;
- `ParticipanteRetiradoDaExperiencia`;

Início, presença e participação deverão permanecer estados e eventos independentes.

# 3691. Presença

Deverão incluir, entre outros:

- `PresencaEmExperienciaDeclarada`;
- `PresencaEmExperienciaConfirmada`;
- `PresencaEmExperienciaContestada`;

Presença deverá declarar participante, fonte, período, modalidade, precisão, autoridade e limitações.

Check-in, localização ou acesso técnico poderão sustentar presença, mas não participação integral.

# 3692. Participação

Deverão incluir, entre outros:

- `ParticipacaoEmExperienciaIniciada`;
- `ParticipacaoEmExperienciaConfirmada`;
- `ParticipacaoEmExperienciaNegada`;

A participação deverá ser individualizada. Confirmação de um participante não deverá confirmar os demais.

# 3693. Família 6 — Envolvimento, agência e continuidade

Deverão incluir, entre outros:

- `EnvolvimentoEmExperienciaDeclarado`;
- `NivelDeEnvolvimentoAtualizado`;
- `AgenciaDoParticipanteRegistrada`;
- `AutonomiaDoParticipanteLimitada`;
- `ContinuidadeDeExperienciaReconhecida`;
- `ContinuidadeDeExperienciaContestada`;
- `AcompanhamentoDeExperienciaIniciado`;
- `AcompanhamentoDeExperienciaEncerrado`;

Envolvimento, agência e autonomia são dimensões distintas e não deverão ser inferidas silenciosamente.

# 3694. Inferência de envolvimento

Deverão incluir, entre outros:

- `NivelDeEnvolvimentoAtualizado`;

Quando derivado por inferência, o evento deverá declarar modelo, dados utilizados, limitações, incerteza e possibilidade de contestação.

Tempo de permanência não deverá confirmar envolvimento.

# 3695. Família 7 — Pausa, retomada e encerramento

Deverão incluir, entre outros:

- `ExperienciaPausada`;
- `ExperienciaRetomada`;
- `ExperienciaConcluida`;
- `ExperienciaInterrompida`;
- `ExperienciaCancelada`;
- `ExperienciaExpirada`;
- `ExperienciaArquivada`;
- `MotivoDeEncerramentoAtualizado`;

Conclusão deverá permanecer distinta de resultado, satisfação, significado e transformação.

# 3696. Pausa e retomada

Deverão incluir, entre outros:

- `ExperienciaPausada`;
- `ExperienciaRetomada`;

A pausa deverá registrar motivo conhecido, continuidade preservada ou perdida, participantes afetados e condições de retomada.

Retomada após encerramento material deverá produzir novo episódio ou novo agregado quando não houver continuidade legítima.

# 3697. Conclusão, interrupção, cancelamento e expiração

Deverão incluir, entre outros:

- `ExperienciaConcluida`;
- `ExperienciaInterrompida`;
- `ExperienciaCancelada`;
- `ExperienciaExpirada`;

Os quatro eventos deverão ser semanticamente distintos.

Experiência interrompida não deverá ser apresentada como concluída. Experiência cancelada antes do início não deverá ser apresentada como vivida.

# 3698. Família 8 — Recorrência, séries e episódios

Deverão incluir, entre outros:

- `SerieDeExperienciasCriada`;
- `RegraDeRecorrenciaDefinida`;
- `RegraDeRecorrenciaAlterada`;
- `EpisodioDeExperienciaCriado`;
- `EpisodioDeExperienciaIniciado`;
- `EpisodioDeExperienciaConcluido`;
- `EpisodioDeExperienciaCancelado`;
- `EpisodioAusenteReconhecido`;
- `SerieDeExperienciasEncerrada`;

Série e episódios deverão possuir identidades próprias. A série não absorverá estados individuais dos episódios.

# 3699. Episódios

Deverão incluir, entre outros:

- `EpisodioDeExperienciaCriado`;
- `EpisodioDeExperienciaIniciado`;
- `EpisodioDeExperienciaConcluido`;
- `EpisodioDeExperienciaCancelado`;

Cada episódio deverá preservar participantes, presença, participação, entrega, resultado, percepção, evidências, memórias, correções e revogações próprios.

# 3700. Recorrência não representa evolução

Deverão incluir, entre outros:

- `RegraDeRecorrenciaDefinida`;
- `SerieDeExperienciasEncerrada`;

Quantidade, frequência ou continuidade de episódios não deverá produzir evento de evolução, mérito ou transformação.

# 3701. Família 9 — Entregas, resultados e efeitos

Deverão incluir, entre outros:

- `EntregaDeExperienciaRegistrada`;
- `EntregaDeExperienciaConfirmada`;
- `EntregaDeExperienciaContestada`;
- `UsoDeEntregaRegistrado`;
- `ResultadoDeExperienciaRegistrado`;
- `ResultadoDeExperienciaConfirmado`;
- `ResultadoDeExperienciaContestado`;
- `EfeitoPositivoRegistrado`;
- `EfeitoNegativoRegistrado`;
- `EfeitoNeutroRegistrado`;
- `EfeitoAmbivalenteRegistrado`;

Entrega, uso, resultado e efeito deverão permanecer distintos.

# 3702. Entregas

Deverão incluir, entre outros:

- `EntregaDeExperienciaRegistrada`;
- `EntregaDeExperienciaConfirmada`;
- `EntregaDeExperienciaContestada`;

O executor poderá confirmar a própria entrega dentro de seu escopo. Entrega não confirmará utilização, resultado ou satisfação.

# 3703. Resultados

Deverão incluir, entre outros:

- `ResultadoDeExperienciaRegistrado`;
- `ResultadoDeExperienciaConfirmado`;
- `ResultadoDeExperienciaContestado`;

Resultados deverão declarar fonte, período, escopo, método, limitações, causalidade e incerteza.

Correlação temporal não deverá ser tratada como causalidade.

# 3704. Efeitos

Deverão incluir, entre outros:

- `EfeitoPositivoRegistrado`;
- `EfeitoNegativoRegistrado`;
- `EfeitoNeutroRegistrado`;
- `EfeitoAmbivalenteRegistrado`;

Efeitos positivos, negativos, neutros e ambivalentes deverão ser registráveis sem pressão por narrativa positiva.

# 3705. Família 10 — Percepção e satisfação

Deverão incluir, entre outros:

- `PercepcaoDeExperienciaDeclarada`;
- `PercepcaoDeExperienciaAtualizada`;
- `PercepcaoDeExperienciaRemovida`;
- `SatisfacaoComExperienciaDeclarada`;
- `SatisfacaoComExperienciaAtualizada`;
- `SatisfacaoComExperienciaRemovida`;
- `ParticipantePreferiuNaoAvaliar`;
- `AvaliacaoDeExperienciaContestada`;

Percepção e satisfação deverão ser opcionais, atribuídas ao participante e independentes.

# 3706. Ausência de avaliação

Deverão incluir, entre outros:

- `ParticipantePreferiuNaoAvaliar`;

Ausência de percepção ou satisfação não deverá ser convertida em neutralidade, insatisfação, desinteresse ou falha.

# 3707. Família 11 — Evidências e proveniência

Deverão incluir, entre outros:

- `EvidenciaDeExperienciaAssociada`;
- `EvidenciaDeExperienciaValidada`;
- `EvidenciaDeExperienciaLimitada`;
- `EvidenciaDeExperienciaContestada`;
- `EvidenciaDeExperienciaInvalidada`;
- `IntegridadeDeEvidenciaVerificada`;
- `ProvenienciaDeEvidenciaAtualizada`;
- `ValidadeDeEvidenciaExpirada`;

Toda evidência deverá declarar exatamente o que sustenta e o que não sustenta.

# 3708. Escopo da evidência

Deverão incluir, entre outros:

- `EvidenciaDeExperienciaValidada`;
- `EvidenciaDeExperienciaLimitada`;

Fotografia poderá sustentar presença em determinado contexto, mas não deverá confirmar participação integral, satisfação, significado ou transformação.

# 3709. Família 12 — Memórias, mídias e autoria

Deverão incluir, entre outros:

- `MemoriaDeExperienciaCriada`;
- `MemoriaDeExperienciaAtualizada`;
- `MemoriaDeExperienciaRemovida`;
- `MidiaDeExperienciaAssociada`;
- `MidiaDeExperienciaRemovida`;
- `AutoriaDeMemoriaReconhecida`;
- `PermissaoDeMidiaAtualizada`;
- `MemoriaCompartilhada`;
- `CompartilhamentoDeMemoriaRevogado`;

Memória deverá permanecer distinta de evidência e preservar autoria, permissões e proteção de terceiros.

# 3710. Memória criada por inteligência

Deverão incluir, entre outros:

- `MemoriaDeExperienciaCriada`;

Guivos Intelligence poderá auxiliar organização ou síntese somente quando explicitamente solicitado e identificado.

A memória não deverá ser apresentada como escrita, sentida ou lembrada pelo participante quando não tiver sido validada por ele.

# 3711. Família 13 — Significado, reflexão e candidaturas

Deverão incluir, entre outros:

- `SignificadoDeExperienciaDeclarado`;
- `SignificadoDeExperienciaAtualizado`;
- `SignificadoDeExperienciaRemovido`;
- `ReflexaoSobreExperienciaRegistrada`;
- `ReflexaoSobreExperienciaAtualizada`;
- `ReflexaoSobreExperienciaRemovida`;
- `CandidaturaAEventoDeVidaCriada`;
- `CandidaturaATransformacaoCriada`;

Significado e reflexão deverão ser opcionais, revisáveis e privados por padrão.

# 3712. Candidaturas limitadas

Deverão incluir, entre outros:

- `CandidaturaAEventoDeVidaCriada`;
- `CandidaturaATransformacaoCriada`;

Os eventos deverão representar apenas candidatura para avaliação pelas capacidades competentes.

Não deverão confirmar Evento de Vida, transformação ou Evolução Contínua.

# 3713. Família 14 — Participantes e experiências compartilhadas

Deverão incluir, entre outros:

- `ParticipanteAssociadoAExperiencia`;
- `ParticipanteConvidadoParaExperiencia`;
- `ConviteDeExperienciaAceito`;
- `ConviteDeExperienciaRecusado`;
- `ParticipacaoIndividualAtualizada`;
- `ExperienciaCompartilhadaReconhecida`;
- `ExperienciaColetivaReconhecida`;
- `ExperienciaInstitucionalReconhecida`;
- `NarrativaColetivaAutorizada`;
- `ParticipanteRetirouAssociacao`;

Estado coletivo não deverá substituir estados individuais.

# 3714. Proteção dos participantes

Deverão incluir, entre outros:

- `ParticipanteAssociadoAExperiencia`;
- `ParticipanteRetirouAssociacao`;

Associação deverá preservar fundamento, autoridade, visibilidade e permissões.

Um participante deverá poder contestar ou retirar associação pessoal sem apagar fatos legitimamente mantidos por outros titulares.

# 3715. Narrativa coletiva

Deverão incluir, entre outros:

- `NarrativaColetivaAutorizada`;

Narrativa coletiva deverá exigir autoridade e escopo explícitos. Ela não deverá substituir memórias, percepções ou significados individuais.

# 3716. Família 15 — Visualização e controle

Deverão incluir, entre outros:

- `ExperienciaVisualizada`;
- `DetalhesDeExperienciaAcessados`;
- `ModoDeVisualizacaoAlterado`;
- `FiltroDeExperienciasAplicado`;
- `ExplicacaoDeExperienciaAcessada`;
- `ExplicacaoDeReconstrucaoAcessada`;
- `ExperienciaOcultada`;
- `ExperienciaReexibida`;
- `ExperienciaArquivadaPeloParticipante`;
- `ExportacaoDeExperienciaSolicitada`;

Eventos de visualização deverão avaliar o funcionamento da interface, não interesse, satisfação ou valor da experiência.

# 3717. Visualização não representa interesse

Deverão incluir, entre outros:

- `ExperienciaVisualizada`;
- `DetalhesDeExperienciaAcessados`;

Abertura, visualização, permanência, rolagem ou repetição de acesso não deverão produzir eventos de interesse, aceitação, satisfação ou significado.

# 3718. Família 16 — Privacidade, permissões e compartilhamento

Deverão incluir, entre outros:

- `NivelDePrivacidadeAlterado`;
- `TituloNeutroAplicado`;
- `ProtecaoVisualExigida`;
- `LocalizacaoDeExperienciaMinimizada`;
- `PermissaoDeExperienciaConcedida`;
- `PermissaoDeExperienciaLimitada`;
- `PermissaoDeExperienciaRevogada`;
- `CompartilhamentoDeExperienciaConcedido`;
- `CompartilhamentoDeExperienciaLimitado`;
- `CompartilhamentoDeExperienciaRevogado`;
- `ProtecaoDeTerceiroAplicada`;

Permissões e compartilhamentos deverão declarar destinatário, finalidade, escopo, conteúdo, duração e possibilidade de revogação.

# 3719. Compartilhamento granular

Deverão incluir, entre outros:

- `CompartilhamentoDeExperienciaConcedido`;
- `CompartilhamentoDeExperienciaLimitado`;

Compartilhar a existência da experiência não deverá autorizar automaticamente título, participantes, localização, mídias, percepção, satisfação, memória ou significado.

# 3720. Proteção de terceiros

Deverão incluir, entre outros:

- `ProtecaoDeTerceiroAplicada`;

A proteção deverá minimizar nomes, imagens, localização, relações, conteúdos e identificadores de terceiros quando não houver autoridade suficiente.

# 3721. Família 17 — Relações comerciais e execução externa

Deverão incluir, entre outros:

- `RelacaoComercialDeExperienciaDeclarada`;
- `PatrocinioDeExperienciaDeclarado`;
- `ComissaoDeExperienciaDeclarada`;
- `ExecucaoExternaDeExperienciaIniciada`;
- `EntregaExternaDeExperienciaConfirmada`;
- `FalhaDeExecutorExternoRegistrada`;
- `ResultadoExternoRecebido`;
- `AutoridadeDeExecutorExternoLimitada`;

Relação comercial deverá permanecer transparente e não alterar semântica funcional.

# 3722. Execução externa

Deverão incluir, entre outros:

- `ExecucaoExternaDeExperienciaIniciada`;
- `EntregaExternaDeExperienciaConfirmada`;
- `FalhaDeExecutorExternoRegistrada`;

Executor externo deverá confirmar apenas fatos dentro de sua autoridade. Retorno externo não deverá redefinir percepção, satisfação, memória ou significado.

# 3723. Família 18 — Contestação, correção e revogação

Deverão incluir, entre outros:

- `ExperienciaContestada`;
- `ParticipacaoEmExperienciaContestada`;
- `ResultadoDeExperienciaContestado`;
- `AssociacaoContextualContestada`;
- `CorrecaoDeExperienciaProposta`;
- `CorrecaoDeExperienciaAplicada`;
- `CorrecaoDeExperienciaRejeitada`;
- `RevogacaoDeExperienciaSolicitada`;
- `RevogacaoDeExperienciaIniciada`;
- `RevogacaoDeExperienciaParcialmentePropagada`;
- `RevogacaoDeExperienciaConcluida`;
- `RetencaoResidualDeExperienciaReconhecida`;

Contestação deverá limitar efeitos incompatíveis. Correção deverá ser compensatória. Revogação deverá possuir propagação verificável.

# 3724. Contestação

Deverão incluir, entre outros:

- `ExperienciaContestada`;
- `ParticipacaoEmExperienciaContestada`;
- `ResultadoDeExperienciaContestado`;
- `AssociacaoContextualContestada`;

O evento deverá registrar objeto contestado, ator, autoridade, fundamento opcional, efeitos suspensos, consumidores afetados e estado da análise.

# 3725. Correção compensatória

Deverão incluir, entre outros:

- `CorrecaoDeExperienciaProposta`;
- `CorrecaoDeExperienciaAplicada`;
- `CorrecaoDeExperienciaRejeitada`;

A correção deverá preservar evento anterior, valor anterior, valor corrigido, ator, autoridade, fundamento, temporalidades e consumidores afetados.

Eventos históricos não deverão ser reescritos.

# 3726. Revogação

Deverão incluir, entre outros:

- `RevogacaoDeExperienciaSolicitada`;
- `RevogacaoDeExperienciaIniciada`;
- `RevogacaoDeExperienciaParcialmentePropagada`;
- `RevogacaoDeExperienciaConcluida`;

O fluxo de referência será:

```text
solicitada
→ validada
→ iniciada
→ propagada parcialmente
→ confirmada pelos consumidores aplicáveis
→ concluída
```

A conclusão não deverá ocorrer antes da propagação suficiente.

# 3727. Retenção residual

Deverão incluir, entre outros:

- `RetencaoResidualDeExperienciaReconhecida`;

Retenção residual legítima deverá declarar base, escopo, conteúdo, duração, consumidores e limitações de uso.

# 3728. Família 19 — Sincronização, falha, recuperação e reconstrução

Deverão incluir, entre outros:

- `SincronizacaoDeExperienciaIniciada`;
- `SincronizacaoDeExperienciaConcluida`;
- `ConflitoDeVersaoDeExperienciaDetectado`;
- `EventoDeExperienciaDuplicadoIgnorado`;
- `EventoDeExperienciaForaDeOrdemRecebido`;
- `FalhaDeExperienciaRegistrada`;
- `FalhaParcialDeExperienciaRegistrada`;
- `RecuperacaoDeExperienciaIniciada`;
- `EstadoDeExperienciaReconstruido`;
- `ReconciliacaoDeExperienciaConcluida`;
- `FalhaSeguraDeExperienciaAcionada`;

Sincronização e recuperação deverão preservar identidade, versões, histórico, correções e revogações.

# 3729. Idempotência

A mesma chave de idempotência deverá produzir, no máximo, um efeito funcional material.

Retentativas não deverão criar:

- novo Registro de Experiência;
- episódio duplicado;
- participante duplicado;
- entrega duplicada;
- resultado duplicado;
- memória duplicada;
- compartilhamento duplicado;
- intervenção duplicada;
- candidatura duplicada.

# 3730. Duplicidade semântica

Eventos tecnicamente diferentes, mas funcionalmente equivalentes, deverão ser detectados quando não houver diferença material de titular, atividade, temporalidade, contexto, finalidade ou efeito.

# 3731. Ordenação

Eventos fora de ordem deverão preservar:

- momento real do fato;
- momento do conhecimento;
- causalidade declarada;
- versão do agregado;
- estado atual válido;
- necessidade de reconciliação.

Ordem de chegada não deverá substituir ordem funcional.

# 3732. Evento tardio

Um evento tardio não deverá regredir automaticamente o agregado.

Exemplo:

```text
ExperienciaConcluida
recebido antes de
ExperienciaIniciada
```

O sistema deverá reconciliar temporalidades e versões antes de aplicar efeitos.

# 3733. Concorrência

Atualizações simultâneas deverão utilizar:

- versão esperada;
- controle otimista;
- autoridade das fontes;
- prioridade funcional;
- registro de conflito;
- reconciliação;
- revisão do participante, quando necessária.

Uma declaração não deverá apagar silenciosamente outra declaração válida.

# 3734. Atomicidade

Operações materiais deverão produzir estado consistente.

Exemplo de compartilhamento:

```text
permissão validada
→ recorte criado
→ destinatário registrado
→ propagação iniciada
→ confirmação suficiente
→ compartilhamento reconhecido
```

Falha intermediária não deverá ser apresentada como compartilhamento concluído.

# 3735. Publicação

Um evento material somente poderá ser publicado quando:

1. identidade estiver suficientemente validada;
2. autoridade estiver delimitada;
3. finalidade estiver declarada;
4. persistência funcional tiver ocorrido;
5. versão do agregado tiver sido avançada;
6. payload estiver minimizado;
7. sensibilidade estiver classificada;
8. consumidores autorizados estiverem definidos;
9. chave de idempotência estiver disponível;
10. relação comercial aplicável estiver declarada.

# 3736. Consumo

Consumidores não deverão reinterpretar o evento além de sua semântica.

`ExperienciaConcluida` não autoriza concluir que:

- resultado foi alcançado;
- participante ficou satisfeito;
- houve aprendizagem;
- ocorreu transformação;
- deve haver publicação;
- deve haver recomendação comercial.

# 3737. Consumidor incompatível

Consumidor sem finalidade, autoridade, compatibilidade contratual ou permissão deverá rejeitar o evento de forma segura e registrar a incompatibilidade.

# 3738. Produtores autorizados

Poderão produzir eventos dentro de sua autoridade:

- participante;
- representante autorizado;
- Guivos Journey;
- Guivos Intelligence;
- Platform Layer;
- produto especializado;
- organização;
- profissional;
- executor externo;
- integração autorizada;
- processo de reconciliação;
- processo de auditoria.

Capacidade técnica de publicação não representa autoridade funcional.

# 3739. Consumidores autorizados

Poderão consumir recortes compatíveis:

- Captura de Contexto;
- Contexto Vivo;
- Objetivos;
- Eventos de Vida;
- Próximos Passos;
- Oportunidades Ativas;
- Intervenções Contextuais;
- Evolução Contínua;
- Guivos Intelligence;
- Platform Layer;
- produtos especializados;
- organizações e profissionais autorizados;
- canais;
- sistemas externos autorizados.

Cada consumidor deverá receber somente o recorte necessário.

# 3740. Compatibilidade contratual

Consumidores deverão:

- reconhecer versões compatíveis;
- rejeitar versões incompatíveis;
- preservar eventos desconhecidos quando aplicável;
- permitir reprocessamento posterior;
- não descartar silenciosamente evento material.

# 3741. Retenção

A retenção deverá considerar:

- finalidade;
- sensibilidade;
- obrigação aplicável;
- auditoria;
- proteção do participante;
- proteção de terceiros;
- contestação;
- correção;
- revogação;
- estado do agregado.

Memórias, reflexões e significados opcionais deverão possuir retenção mais restritiva que fatos operacionais necessários.

# 3742. Exclusão e anonimização

Exclusão, anonimização e retenção deverão permanecer distintas.

A exclusão de conteúdo opcional não deverá apagar silenciosamente eventos necessários à auditoria, mas o conteúdo residual deverá ser minimizado e protegido.

# 3743. Falha segura

Na ausência de condições suficientes, o sistema deverá preferir:

- não publicar;
- manter estado anterior válido;
- registrar pendência;
- bloquear consumidor incompatível;
- suspender propagação;
- proteger conteúdo sensível;
- solicitar revisão;
- registrar falha parcial.

Falha parcial não deverá ser apresentada como sucesso integral.

# 3744. Recuperação

A recuperação deverá:

- preservar eventos válidos;
- evitar duplicidade;
- reconstruir versões;
- reaplicar correções;
- reaplicar revogações;
- reconciliar eventos fora de ordem;
- registrar lacunas;
- explicar limitações.

# 3745. Reconstrução do agregado

O estado atual deverá poder ser reconstruído a partir do histórico válido de eventos, sem depender exclusivamente do valor persistido mais recente.

# 3746. Explicabilidade

Todo evento material deverá permitir explicar:

- o que ocorreu;
- quem declarou;
- qual autoridade existia;
- qual fonte foi utilizada;
- qual finalidade foi aplicada;
- quando o fato ocorreu;
- quando foi conhecido;
- por que foi reconhecido;
- quais incertezas permaneceram;
- quais consumidores receberam;
- quais efeitos foram produzidos;
- quais correções ou revogações existem.

# 3747. Auditoria

A auditoria deverá reconstruir:

```text
sinal, comando ou declaração
→ candidatura
→ validação
→ planejamento ou reconhecimento histórico
→ início
→ presença e participação
→ conclusão, interrupção ou cancelamento
→ entrega e resultado
→ percepção e satisfação
→ evidência e memória
→ significado opcional
→ contestação, correção ou revogação
→ propagação
```

# 3748. Observabilidade

A observabilidade deverá permitir detectar:

- publicação sem autoridade;
- finalidade genérica;
- payload excessivo;
- evento duplicado;
- conflito de versão;
- evento fora de ordem;
- consumidor incompatível;
- correção incompleta;
- revogação não propagada;
- exposição de terceiros;
- falha parcial apresentada como sucesso.

# 3749. Métricas dos eventos

Métricas futuras poderão avaliar:

- eventos sem autoridade;
- eventos sem finalidade;
- eventos duplicados;
- eventos fora de ordem;
- conflitos não reconciliados;
- falhas de idempotência;
- payload excessivo;
- experiências fabricadas por inferência;
- ocorrências confirmadas sem fundamento;
- memórias sem autoria;
- significados atribuídos pelo sistema;
- relações comerciais omitidas;
- correções não propagadas;
- revogações incompletas;
- tempo de recuperação;
- capacidade de reconstrução.

As métricas deverão avaliar o sistema, não o participante.

# 3750. Neutralidade comercial

Eventos comerciais não deverão:

- fabricar ocorrência;
- elevar prioridade funcional;
- ocultar efeitos negativos;
- pressionar satisfação positiva;
- produzir significado;
- produzir transformação;
- ampliar retenção;
- autorizar publicidade sensível.

# 3751. Relação com Intervenções Contextuais

Eventos de Experiências poderão produzir candidaturas de manifestação para Intervenções Contextuais.

A decisão de quando, como ou se manifestar permanecerá pertencendo à Capacidade 07.

# 3752. Relação com Eventos de Vida

Uma experiência poderá produzir `CandidaturaAEventoDeVidaCriada`.

A Capacidade 04 continuará responsável por reconhecer ou rejeitar Evento de Vida.

# 3753. Relação com Evolução Contínua

Uma experiência poderá fornecer evidências ou candidaturas limitadas para Evolução Contínua.

Frequência, quantidade, satisfação, resultado ou significado não deverão confirmar evolução automaticamente.

# 3754. Comportamentos proibidos

Os contratos não deverão:

1. publicar sinal como evento;
2. publicar comando como fato;
3. publicar proposta como ocorrência;
4. publicar evento material antes da persistência;
5. tratar compra como experiência vivida;
6. tratar reserva como início;
7. tratar presença como participação;
8. tratar participação como conclusão;
9. tratar conclusão como resultado;
10. tratar resultado como satisfação;
11. tratar satisfação como significado;
12. tratar significado como transformação;
13. confirmar todos os participantes por declaração individual;
14. ampliar autoridade de organização ou fornecedor;
15. atribuir percepção ao participante;
16. gerar memória em nome do participante;
17. impor significado;
18. ocultar incerteza;
19. reescrever eventos históricos;
20. ocultar correções;
21. declarar revogação antes da propagação;
22. duplicar efeitos em reprocessamento;
23. ignorar versão esperada;
24. sobrescrever conflitos;
25. aplicar evento fora de ordem de forma insegura;
26. publicar payload sensível excessivo;
27. omitir relação comercial;
28. expor terceiros;
29. utilizar experiência sensível para publicidade;
30. avaliar mérito, fé, disciplina, evolução ou valor humano.

# 3755. Critérios de aceite

A extensão será considerada consolidada quando:

1. distinguir sinal, comando, proposta, declaração, evento e efeito;
2. exigir persistência antes da publicação;
3. definir o Registro de Experiência como agregado;
4. definir identidade permanente;
5. definir estrutura comum;
6. definir versionamento;
7. definir titular, ator e papéis;
8. definir autoridade;
9. definir finalidade;
10. definir temporalidades;
11. definir correlação e causalidade;
12. definir proveniência;
13. definir sensibilidade;
14. definir minimização;
15. definir relações comerciais;
16. definir incerteza;
17. definir as 19 famílias;
18. governar identificação e candidatura;
19. governar identidade e titularidade;
20. governar autoridade e finalidade;
21. governar ocorrência;
22. governar reconstrução histórica;
23. governar planejamento e prontidão;
24. governar início e presença;
25. governar participação;
26. governar envolvimento e continuidade;
27. governar pausa e retomada;
28. governar conclusão, interrupção, cancelamento e expiração;
29. governar recorrência e episódios;
30. governar entregas;
31. governar resultados e efeitos;
32. governar percepção;
33. governar satisfação;
34. governar evidências;
35. governar memórias;
36. governar significado e reflexão;
37. governar experiências compartilhadas;
38. governar visualização e controle;
39. governar privacidade;
40. governar compartilhamento;
41. governar proteção de terceiros;
42. governar execução externa;
43. governar contestação;
44. governar correção;
45. governar revogação;
46. governar propagação;
47. assegurar idempotência;
48. assegurar duplicidade semântica;
49. assegurar ordenação;
50. assegurar concorrência;
51. assegurar atomicidade;
52. assegurar falha segura;
53. assegurar recuperação e reconstrução;
54. definir retenção proporcional;
55. definir produtores;
56. definir consumidores;
57. assegurar compatibilidade;
58. assegurar explicabilidade e auditoria;
59. bloquear os 30 comportamentos proibidos;
60. manter o participante no controle.

# 3756. Continuidade normativa

`PAS-001-EXP-EVENT-001 1.0.0` é registrado como a **quarta extensão normativa da Capacidade 08 — Experiências**.

A extensão:

- preserva `PAS-001-EXP-FOUNDATION-001 1.0.0`;
- preserva `PAS-001-EXP-LIFECYCLE-001 1.0.0`;
- preserva `PAS-001-EXP-VIEW-001 1.0.0`;
- preserva o `PAS-001 0.5.0`;
- mantém as Capacidades 02 a 07 como `Functionally complete`;
- mantém a Capacidade 08 como `In progress`;
- eleva o progresso editorial de `60%` para `80%`;
- preserva a Capacidade 09 — Evolução Contínua como `Planned`;
- consolida agregado, estrutura comum e 19 famílias de eventos;
- governa autoridade, finalidade, temporalidades, proveniência, sensibilidade e incerteza;
- assegura idempotência, ordenação, concorrência, atomicidade, reconstrução e falha segura;
- estabelece as integrações funcionais como próxima etapa normativa.

O próximo bloco será:

> **Integrações Funcionais da Capacidade de Experiências com Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Intervenções Contextuais, Evolução Contínua, Guivos Intelligence, Platform Layer, produtos especializados, organizações, profissionais, canais, calendários, localização, dispositivos, mídias, fontes públicas e sistemas externos, incluindo finalidade, minimização, autoridade, sincronização, revogação, propagação, neutralidade comercial, observabilidade e falha segura.**
