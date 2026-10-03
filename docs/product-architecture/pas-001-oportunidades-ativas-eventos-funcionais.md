---
id: PAS-001-OA-EVENT-001
title: Contratos dos Eventos Funcionais da Capacidade de Oportunidades Ativas
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-15
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-OA-LIFECYCLE-001
  - PAS-001-OA-VIEW-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-OA-EVENT-001 — Contratos dos Eventos Funcionais da Capacidade de Oportunidades Ativas

## 1. Autoridade e vínculo

Este documento é a **quarta extensão normativa da Capacidade 06 — Oportunidades Ativas** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade:

- do `PAS-001-OA-FOUNDATION-001 1.0.0`;
- do `PAS-001-OA-LIFECYCLE-001 1.0.0`;
- do `PAS-001-OA-VIEW-001 1.0.0`;
- das seções 2061 a 2368;
- do `PAS-001 0.5.0`.

Esta extensão mantém a capacidade no estado `In progress` e eleva o progresso editorial de referência de `60%` para `80%`.

# 2369. Finalidade dos contratos de eventos

Os contratos deverão governar como fatos reconhecidos sobre oportunidades são registrados, versionados, publicados, consumidos, corrigidos e auditados.

Eles deverão impedir que:

- comandos sejam tratados como fatos;
- sugestões sejam tratadas como decisões;
- estimativas sejam tratadas como confirmações;
- publicidade produza eventos de relevância;
- visualização produza interesse;
- interesse produza compromisso;
- inscrição produza aceitação;
- transações externas redefinam a jornada;
- correções reescrevam silenciosamente o histórico;
- reprocessamentos dupliquem efeitos;
- eventos fora de ordem criem estados impossíveis.

# 2370. Comando, proposta e evento

Os conceitos deverão permanecer distintos.

## Comando funcional

Solicitação para avaliar ou alterar o estado.

Exemplos:

- avaliar oportunidade;
- verificar disponibilidade;
- declarar interesse;
- ocultar oportunidade;
- iniciar inscrição;
- revogar uso de contexto.

## Proposta funcional

Possibilidade ainda sujeita a avaliação ou decisão.

Exemplos:

- oportunidade candidata;
- elegibilidade estimada;
- vínculo sugerido com Próximo Passo;
- alternativa recomendada;
- correção proposta.

## Evento funcional

Fato reconhecido e persistido.

Exemplos:

- `OportunidadeAtivada`;
- `DisponibilidadeDeOportunidadeAtualizada`;
- `InteresseEmOportunidadeDeclarado`;
- `OportunidadeContestada`;
- `PermissaoDeContextoRevogada`.

# 2371. Fluxo funcional

```text
comando, sinal ou informação
→ validação de identidade
→ validação de autoridade
→ validação de finalidade
→ avaliação funcional
→ proposta, quando aplicável
→ decisão
→ persistência suficiente
→ evento reconhecido
→ atualização do agregado
→ produção de recortes
→ processamento pelos consumidores autorizados
```

Nenhum evento material deverá ser publicado antes de persistência funcional suficiente.

# 2372. Princípios obrigatórios

Os eventos deverão observar:

- imutabilidade histórica;
- correção compensatória;
- titularidade explícita;
- autoridade limitada;
- temporalidade múltipla;
- proveniência;
- finalidade;
- minimização;
- sensibilidade;
- versionamento;
- idempotência;
- ordenação;
- concorrência segura;
- explicabilidade;
- auditabilidade;
- neutralidade comercial;
- falha segura;
- controle do participante.

# 2373. Agregado funcional

O agregado principal será o **Registro de Oportunidade**.

Ele deverá concentrar:

- identidade;
- estado funcional;
- estado da informação;
- disponibilidade;
- elegibilidade;
- relevância;
- risco;
- sensibilidade;
- relação comercial;
- relação do participante;
- vínculos;
- permissões;
- versões;
- histórico.

Estados transacionais externos deverão permanecer em agregados ou recortes próprios.

# 2374. Estrutura comum do evento

Todo evento deverá possuir, conforme aplicável:

| Campo | Finalidade |
|---|---|
| `event_id` | Identidade imutável do evento |
| `event_type` | Tipo funcional versionado |
| `event_version` | Versão do contrato |
| `aggregate_id` | Oportunidade afetada |
| `aggregate_version` | Versão resultante do agregado |
| `participant_id` | Titular da avaliação |
| `participant_category` | Pessoa, Organização ou Coletivo |
| `actor_id` | Agente que originou a ação |
| `actor_role` | Papel funcional do ator |
| `authority_scope` | Escopo da autoridade |
| `source_id` | Fonte original |
| `purpose` | Finalidade do processamento |
| `occurred_at` | Momento real do fato |
| `known_at` | Momento em que a Guivos tomou conhecimento |
| `recognized_at` | Momento do reconhecimento funcional |
| `recorded_at` | Momento da persistência |
| `effective_at` | Momento de aplicação funcional |
| `correlation_id` | Correlação do fluxo |
| `causation_id` | Evento ou comando causador |
| `idempotency_key` | Prevenção de duplicidade |
| `sensitivity` | Classificação de sensibilidade |
| `permissions` | Permissões aplicáveis |
| `payload` | Conteúdo funcional minimizado |
| `provenance` | Origem e transformações |
| `metadata` | Dados técnicos não semânticos |

# 2375. Identidade do evento

O `event_id` deverá ser:

- único;
- permanente;
- não reutilizável;
- independente da posição em fila;
- independente do consumidor;
- preservado em reprocessamentos.

Eventos equivalentes não deverão receber novas identidades apenas por retransmissão.

# 2376. Versionamento

O `event_type` deverá representar a semântica funcional.

Exemplo:

```text
OportunidadeAtivada
event_version: 1.0.0
```

Mudanças incompatíveis deverão gerar nova versão contratual.

Mudanças técnicas sem alteração semântica não deverão gerar novo tipo funcional.

# 2377. Titular e participante

Todo evento pessoal deverá possuir titular identificável.

Eventos relacionados a Organização ou Coletivo deverão preservar:

- categoria;
- autoridade;
- vínculo;
- escopo;
- participantes afetados;
- conteúdos privados.

O fornecedor não deverá assumir a titularidade da avaliação de relevância do participante.

# 2378. Ator, papel e autoridade

O evento deverá distinguir:

- quem realizou a ação;
- em qual papel;
- com qual autoridade;
- para qual finalidade.

Exemplo:

```text
actor_id: organização responsável
actor_role: fornecedor
authority_scope: disponibilidade e condições próprias
```

Esse ator não deverá confirmar:

- interesse;
- relevância pessoal absoluta;
- prioridade;
- evolução;
- resultado humano.

# 2379. Fonte e proveniência

A proveniência deverá registrar:

- sistema de origem;
- registro original;
- agente original;
- momento original;
- transformações;
- verificações;
- estimativas;
- correções;
- limitações;
- relações comerciais conhecidas.

A Guivos Intelligence não deverá aparecer como fonte de um fato externo que apenas estimou.

# 2380. Finalidade

Todo evento deverá possuir finalidade funcional compatível.

Finalidades possíveis incluem:

- avaliação;
- apresentação;
- comparação;
- acompanhamento;
- inscrição;
- proteção;
- auditoria;
- sincronização;
- correção;
- revogação.

Um evento reconhecido para uma finalidade não deverá autorizar usos incompatíveis.

# 2381. Sensibilidade

Eventos sensíveis deverão utilizar:

- payload minimizado;
- identificadores protegidos;
- recortes específicos;
- retenção proporcional;
- acesso restrito;
- títulos neutros;
- logs sem narrativas excessivas;
- ausência de uso publicitário.

# 2382. Temporalidades

Os eventos deverão distinguir:

- tempo do fato;
- tempo da declaração;
- tempo do registro externo;
- tempo do conhecimento;
- tempo do reconhecimento;
- tempo da persistência;
- tempo da aplicação;
- tempo da propagação;
- tempo da correção.

# 2383. Eventos retroativos

Um evento retroativo deverá preservar:

```text
occurred_at: momento real conhecido ou aproximado
known_at: momento em que a Guivos tomou conhecimento
recognized_at: momento da validação funcional
effective_at: momento a partir do qual os efeitos foram aplicados
```

A retroatividade não deverá fabricar reconstruções impossíveis.

# 2384. Temporalidade aproximada

Quando o momento exato não for conhecido, deverão ser registrados:

- intervalo;
- precisão;
- fonte;
- confiança;
- limitações.

A capacidade não deverá converter período aproximado em data exata.

# 2385. Correlação

O `correlation_id` deverá reunir eventos do mesmo fluxo.

Exemplo:

```text
BuscaDeOportunidadesRealizada
→ OportunidadeIdentificada
→ CandidaturaDeOportunidadeCriada
→ AvaliacaoDeOportunidadeIniciada
→ OportunidadeAtivada
```

# 2386. Causalidade funcional

O `causation_id` deverá apontar o evento ou comando diretamente responsável.

Correlação temporal isolada não deverá ser registrada como causalidade.

# 2387. Famílias de eventos

Os contratos serão organizados em 19 famílias:

1. identificação e candidatura;
2. fonte e autoridade;
3. avaliação e completude;
4. disponibilidade;
5. elegibilidade;
6. relevância;
7. risco e sensibilidade;
8. transparência comercial;
9. ativação;
10. apresentação;
11. interação do participante;
12. inscrição e fatos externos;
13. vínculos e alternativas;
14. manutenção e encerramento;
15. contestação e correção;
16. permissões e revogação;
17. propagação e integrações;
18. visualização e notificações;
19. falhas e reconstrução.

# 2388. Família 1 — Identificação e candidatura

Eventos principais:

- `OportunidadeIdentificada`;
- `CandidaturaDeOportunidadeCriada`;
- `CandidaturaDeOportunidadeRejeitada`;
- `OportunidadesPotencialmenteDuplicadasIdentificadas`;
- `OportunidadesUnificadas`.

# 2389. OportunidadeIdentificada

Deverá representar o reconhecimento de um possível meio.

Payload mínimo:

- descrição mínima;
- tipo;
- origem;
- fonte;
- possível público;
- finalidade de avaliação;
- momento da identificação;
- confiança inicial.

Não deverá representar:

- candidatura admitida;
- relevância;
- disponibilidade;
- apresentação.

# 2390. CandidaturaDeOportunidadeCriada

Deverá representar que a oportunidade atingiu os requisitos mínimos para avaliação.

Payload:

- identidade funcional;
- fonte;
- finalidade;
- público possível;
- condições conhecidas;
- lacunas;
- riscos preliminares;
- relação comercial conhecida.

# 2391. CandidaturaDeOportunidadeRejeitada

Deverá registrar:

- motivo;
- autoridade da decisão;
- evidências;
- possibilidade de revisão;
- efeitos aplicados;
- eventual bloqueio da fonte.

Motivos possíveis:

- fraude;
- proibição;
- identidade insuficiente;
- fonte inválida;
- finalidade incompatível;
- publicidade disfarçada;
- exploração de vulnerabilidade;
- relação comercial ocultada.

# 2392. Duplicidade semântica

A duplicidade deverá considerar identidade, fornecedor, janela, condições, público e finalidade.

O evento não deverá unificar automaticamente oportunidades apenas semelhantes.

# 2393. OportunidadesUnificadas

Deverá registrar:

- registros de origem;
- identidade canônica;
- diferenças preservadas;
- fontes;
- relações do participante;
- histórico;
- vínculos recompostos.

# 2394. Família 2 — Fonte e autoridade

Eventos principais:

- `FonteDeOportunidadeRegistrada`;
- `FonteDeOportunidadeValidada`;
- `FonteDeOportunidadeRejeitada`;
- `AutoridadeDeFonteDeOportunidadeAlterada`;
- `ConflitoDeInteresseDeFonteIdentificado`;
- `FonteDeOportunidadeTornadaIndisponivel`.

# 2395. FonteDeOportunidadeValidada

Deverá registrar:

- identidade;
- tipo da fonte;
- autoridade;
- escopo;
- validade;
- confiança;
- método de validação;
- limitações;
- conflitos de interesse.

# 2396. FonteDeOportunidadeRejeitada

A rejeição deverá limitar:

- novas candidaturas;
- atualizações;
- confirmações;
- propagação;
- apresentação.

Registros históricos legítimos deverão ser preservados.

# 2397. Alteração de autoridade

Mudança de autoridade deverá:

- preservar versão anterior;
- registrar fundamento;
- reavaliar eventos dependentes;
- limitar fatos anteriormente aceitos quando necessário;
- não apagar histórico.

# 2398. Conflito de interesse

Conflitos deverão registrar:

- natureza;
- agente;
- relação econômica;
- impacto possível;
- controles aplicados;
- necessidade de transparência;
- revisão da neutralidade.

# 2399. Família 3 — Avaliação e completude

Eventos principais:

- `AvaliacaoDeOportunidadeIniciada`;
- `CompletudeDeOportunidadeAvaliada`;
- `InformacaoAdicionalDeOportunidadeSolicitada`;
- `InformacaoDeOportunidadeRecebida`;
- `AvaliacaoDeOportunidadeSuspensa`;
- `AvaliacaoDeOportunidadeConcluida`.

# 2400. AvaliacaoDeOportunidadeIniciada

Deverá registrar:

- critérios aplicáveis;
- finalidade;
- fontes;
- campos necessários;
- permissões;
- prazo de validade da avaliação;
- condições pendentes.

# 2401. CompletudeDeOportunidadeAvaliada

Estados possíveis:

- suficiente;
- parcialmente suficiente;
- insuficiente;
- exige verificação;
- divergente.

A completude não deverá representar qualidade ou relevância.

# 2402. Informação adicional

Solicitações deverão aplicar minimização.

Não deverão solicitar dados sensíveis apenas para aumentar conversão ou precisão comercial.

# 2403. Avaliação suspensa

A suspensão deverá registrar:

- causa;
- estado preservado;
- automações interrompidas;
- condição de retomada;
- efeitos sobre apresentações.

# 2404. Família 4 — Disponibilidade

Eventos principais:

- `DisponibilidadeDeOportunidadeAvaliada`;
- `DisponibilidadeDeOportunidadeConfirmada`;
- `DisponibilidadeDeOportunidadeLimitada`;
- `AberturaFuturaDeOportunidadeRegistrada`;
- `ListaDeEsperaDeOportunidadeRegistrada`;
- `OportunidadeTornadaIndisponivel`;
- `OportunidadeDisponibilizadaNovamente`;
- `DisponibilidadeDeOportunidadeContestada`;
- `DisponibilidadeDeOportunidadeExpirada`.

# 2405. DisponibilidadeDeOportunidadeAvaliada

Payload mínimo:

- estado;
- fonte;
- momento da verificação;
- validade;
- capacidade;
- limitações;
- confiança;
- possibilidade de alteração.

# 2406. Disponibilidade confirmada

Somente uma fonte autorizada deverá confirmar disponibilidade objetiva.

A confirmação não deverá garantir:

- reserva;
- acesso;
- elegibilidade;
- permanência da vaga;
- benefício.

# 2407. Disponibilidade limitada

Deverá distinguir:

- quantidade confirmada;
- quantidade estimada;
- capacidade limitada;
- alta procura;
- janela curta;
- limite por participante.

O evento não deverá produzir urgência pessoal automaticamente.

# 2408. Abertura futura

Deverá registrar:

- data ou condição;
- precisão;
- fonte;
- confiança;
- validade;
- controle de notificações.

# 2409. Lista de espera

Deverá representar condição própria.

Não deverá produzir eventos de:

- vaga reservada;
- aceitação;
- inscrição aprovada;
- acesso garantido.

# 2410. Indisponibilidade

Deverá registrar:

- causa;
- início;
- possível retorno;
- fonte;
- impacto;
- alternativas;
- processos externos existentes.

# 2411. Disponibilização novamente

O retorno à disponibilidade deverá exigir:

- nova verificação;
- nova versão;
- reavaliação de condições;
- reavaliação de relevância;
- revisão de apresentações pendentes.

# 2412. Família 5 — Elegibilidade

Eventos principais:

- `ElegibilidadeDeOportunidadeAvaliada`;
- `ElegibilidadeCondicionadaRegistrada`;
- `ElegibilidadeDeOportunidadeConfirmada`;
- `ElegibilidadeDeOportunidadeNaoConfirmada`;
- `ElegibilidadeDeOportunidadeContestada`;
- `ElegibilidadeDeOportunidadeExpirada`;
- `DecisaoExternaDeElegibilidadeRegistrada`.

# 2413. ElegibilidadeDeOportunidadeAvaliada

Deverá registrar:

- requisitos;
- condições conhecidas;
- informações utilizadas;
- lacunas;
- estado;
- confiança;
- autoridade decisória final;
- validade.

# 2414. Elegibilidade estimada

Estados como `possivelmente elegível` deverão permanecer estimativas.

Não poderão produzir:

- inscrição automática;
- aprovação presumida;
- contato sem autorização;
- exposição de condição sensível.

# 2415. Elegibilidade condicionada

Deverá registrar:

- condição;
- responsável pela verificação;
- prazo;
- evidência necessária;
- consequência se não atendida;
- possibilidade de contestação.

# 2416. Elegibilidade confirmada

Somente deverá ser publicada quando a fonte possuir autoridade para confirmar.

A confirmação deverá permanecer distinta de:

- aprovação;
- aceitação;
- contratação;
- benefício recebido.

# 2417. Decisão externa

Uma organização poderá comunicar:

- aprovada;
- rejeitada;
- pendente;
- exige informação;
- lista de espera.

O evento deverá preservar que a decisão é externa.

# 2418. Família 6 — Relevância

Eventos principais:

- `RelevanciaDeOportunidadeAvaliada`;
- `RelevanciaDeOportunidadeReavaliada`;
- `RelevanciaDeOportunidadeCondicionada`;
- `RelevanciaDeOportunidadeReduzida`;
- `RelevanciaDeOportunidadeContestada`;
- `JustificativaDeRelevanciaProduzida`.

# 2419. RelevanciaDeOportunidadeAvaliada

Deverá registrar:

- relações funcionais consideradas;
- critérios favoráveis;
- critérios desfavoráveis;
- restrições;
- incertezas;
- contexto utilizado;
- fatores excluídos;
- resultado da avaliação.

# 2420. Fatores proibidos

O payload não deverá utilizar como fundamento funcional positivo:

- comissão;
- patrocínio;
- margem;
- investimento publicitário;
- estoque contratado;
- probabilidade de clique;
- tempo de tela;
- vulnerabilidade.

# 2421. Relevância condicionada

Deverá registrar claramente a condição.

Exemplo:

```text
Relevância: condicionada
Condição: confirmação de disponibilidade para o período informado
```

# 2422. Reavaliação

Mudanças em contexto, objetivo, Evento de Vida, Próximo Passo, orçamento, localização, risco ou disponibilidade poderão causar reavaliação.

A capacidade consumidora deverá governar sua própria decisão.

# 2423. JustificativaDeRelevanciaProduzida

A justificativa deverá ser:

- compreensível;
- minimizada;
- verificável;
- não manipulativa;
- comercialmente transparente;
- contestável.

# 2424. Família 7 — Risco e sensibilidade

Eventos principais:

- `RiscoDeOportunidadeAvaliado`;
- `RiscoMaterialDeOportunidadeIdentificado`;
- `NivelDeRiscoDeOportunidadeAlterado`;
- `SensibilidadeDeOportunidadeClassificada`;
- `ProtecaoReforcadaDeOportunidadeAplicada`;
- `ApresentacaoDeOportunidadeLimitadaPorRisco`.

# 2425. RiscoDeOportunidadeAvaliado

Deverá registrar:

- categoria;
- nível;
- fonte;
- evidências;
- incerteza;
- mitigação;
- autoridade;
- necessidade de análise profissional.

# 2426. Risco material

Risco elevado poderá produzir:

- pausa;
- limitação de apresentação;
- solicitação de confirmação;
- bloqueio de automação;
- análise especializada;
- cancelamento.

# 2427. Sensibilidade

A classificação deverá governar:

- busca;
- títulos;
- notificações;
- compartilhamento;
- indexação;
- retenção;
- acesso organizacional;
- publicidade.

# 2428. Proteção reforçada

O evento deverá registrar as proteções aplicadas, sem expor o conteúdo sensível no próprio log técnico.

# 2429. Família 8 — Transparência comercial

Eventos principais:

- `RelacaoComercialDeOportunidadeDeclarada`;
- `PatrocinioDeOportunidadeDeclarado`;
- `ComissaoDeOportunidadeDeclarada`;
- `RelacaoComercialDeOportunidadeAlterada`;
- `RelacaoComercialOcultadaIdentificada`;
- `NeutralidadeComercialDeOportunidadeReavaliada`.

# 2430. Relação comercial declarada

Deverá registrar:

- tipo;
- agentes;
- beneficiários;
- escopo;
- período;
- condição;
- impacto potencial;
- forma de apresentação.

# 2431. Patrocínio

O evento de patrocínio não deverá:

- elevar relevância;
- alterar prioridade;
- ocultar alternativas;
- produzir interesse;
- autorizar contexto sensível.

# 2432. Comissão

A comissão deverá permanecer metadado de transparência, não critério de relevância.

# 2433. Relação ocultada

A identificação de relação comercial ocultada deverá:

- limitar apresentação;
- suspender automações comerciais;
- registrar incidente;
- reavaliar oportunidades afetadas;
- preservar evidências;
- notificar governança.

# 2434. Alteração comercial

Mudanças deverão produzir nova versão e reavaliação da apresentação, sem alterar compatibilidade por si mesmas.

# 2435. Família 9 — Ativação

Eventos principais:

- `OportunidadeAtivada`;
- `OportunidadeAtivadaComCondicao`;
- `AtivacaoDeOportunidadeRejeitada`;
- `AtivacaoDeOportunidadeRevista`;
- `OportunidadeDesativada`.

# 2436. OportunidadeAtivada

Deverá registrar:

- critérios atendidos;
- disponibilidade;
- elegibilidade;
- relevância;
- risco;
- relação comercial;
- validade;
- limitações;
- confiança.

Ativação não representa apresentação.

# 2437. Ativação condicionada

Deverá registrar:

- condição;
- impacto da pendência;
- validade;
- ações permitidas;
- ações bloqueadas;
- apresentação proporcional.

# 2438. Ativação rejeitada

Motivos poderão incluir:

- fonte inválida;
- risco incompatível;
- finalidade ilegítima;
- baixa relevância;
- indisponibilidade;
- ausência de transparência;
- proteção insuficiente.

# 2439. Desativação

A desativação deverá ser distinguida de:

- pausa;
- indisponibilidade;
- expiração;
- cancelamento;
- encerramento.

# 2440. Família 10 — Apresentação

Eventos principais:

- `ApresentacaoDeOportunidadeSolicitada`;
- `ApresentacaoDeOportunidadeAutorizada`;
- `OportunidadeApresentada`;
- `ApresentacaoDeOportunidadeAdiada`;
- `ApresentacaoDeOportunidadeSilenciada`;
- `ApresentacaoDeOportunidadeBloqueada`.

# 2441. Solicitação de apresentação

Oportunidades Ativas poderá solicitar avaliação à Capacidade de Intervenções Contextuais.

A solicitação deverá conter:

- relevância;
- janela real;
- risco;
- sensibilidade;
- alternativas;
- necessidade de decisão;
- restrições de canal.

# 2442. Autorização de apresentação

A decisão pertence à Capacidade de Intervenções Contextuais.

Ela poderá decidir:

- apresentar;
- perguntar;
- lembrar;
- aguardar;
- silenciar;
- não interromper.

# 2443. OportunidadeApresentada

Deverá registrar:

- participante;
- canal;
- momento;
- finalidade;
- versão;
- justificativa;
- relação comercial;
- alternativas exibidas;
- decisão da intervenção.

# 2444. Apresentação silenciada

O silêncio deverá ser um resultado legítimo.

Não deverá ser tratado como falha operacional.

# 2445. Família 11 — Interação do participante

Eventos principais:

- `OportunidadeVisualizada`;
- `OportunidadeSalva`;
- `OportunidadeRemovidaDosSalvos`;
- `InteresseEmOportunidadeDeclarado`;
- `InteresseEmOportunidadeRetirado`;
- `OportunidadeDescartada`;
- `OportunidadeOcultada`;
- `LimitacaoDeOportunidadesSemelhantesRegistrada`.

# 2446. OportunidadeVisualizada

Deverá representar somente acesso ao conteúdo.

Não poderá produzir automaticamente:

- interesse;
- prioridade;
- contato;
- inscrição;
- recomendação mais intensa;
- publicidade semelhante.

# 2447. OportunidadeSalva

Deverá representar preservação para consulta posterior.

Não deverá:

- criar compromisso;
- iniciar inscrição;
- autorizar fornecedor;
- alterar Próximo Passo;
- compartilhar dados.

# 2448. InteresseEmOportunidadeDeclarado

Deverá depender de manifestação inequívoca.

Payload:

- oportunidade;
- participante;
- escopo do interesse;
- finalidade;
- contatos autorizados;
- validade;
- dados que poderão ser compartilhados.

# 2449. Interesse retirado

Deverá:

- interromper novos contatos autorizáveis;
- preservar fatos históricos;
- recompor recortes;
- não produzir penalidade;
- não representar fracasso.

# 2450. Descarte

O motivo deverá ser opcional.

O descarte não deverá alimentar julgamento ou pontuação do participante.

# 2451. Ocultação

Deverá registrar o escopo:

- oportunidade;
- fornecedor;
- categoria;
- origem;
- campanha;
- período;
- oportunidades semelhantes.

# 2452. Família 12 — Inscrição e fatos externos

Eventos principais:

- `InscricaoEmOportunidadeIniciada`;
- `InscricaoEmOportunidadeEnviada`;
- `InscricaoEmOportunidadeCancelada`;
- `AceitacaoExternaDeOportunidadeRegistrada`;
- `RecusaExternaDeOportunidadeRegistrada`;
- `ContratacaoRelacionadaRegistrada`;
- `PagamentoRelacionadoRegistrado`;
- `ParticipacaoRelacionadaRegistrada`;
- `ResultadoExternoRelacionadoRegistrado`.

# 2453. InscricaoEmOportunidadeIniciada

Deverá registrar:

- destino;
- finalidade;
- dados necessários;
- custos;
- termos;
- responsabilidade externa;
- autorização.

# 2454. InscricaoEmOportunidadeEnviada

Deverá exigir confirmação proporcional.

Payload:

- destinatário;
- campos enviados;
- versão;
- protocolo;
- momento;
- termos aceitos;
- limitações.

# 2455. Aceitação externa

A aceitação não deverá confirmar:

- contratação;
- participação;
- benefício;
- Próximo Passo concluído;
- objetivo progredido;
- transformação.

# 2456. Contratação relacionada

A transação pertence ao produto ou fornecedor responsável.

Oportunidades Ativas deverá receber somente o recorte necessário.

# 2457. Participação relacionada

Participação não deverá confirmar:

- satisfação;
- resultado;
- progresso;
- evolução;
- Evento de Vida.

# 2458. Resultado externo

O resultado externo deverá ser encaminhado às capacidades responsáveis para avaliação própria.

# 2459. Família 13 — Vínculos e alternativas

Eventos principais:

- `VinculoComProximoPassoProposto`;
- `VinculoComProximoPassoRegistrado`;
- `VinculoComProximoPassoRemovido`;
- `AlternativaDeOportunidadeRegistrada`;
- `OportunidadeSubstitutaRegistrada`;
- `ComparacaoDeOportunidadesProduzida`.

# 2460. Vínculo proposto

Uma proposta não deverá criar ou confirmar Próximo Passo.

# 2461. Vínculo registrado

Deverá identificar a função:

- meio principal;
- alternativa;
- recurso;
- fornecedor;
- conteúdo;
- local;
- financiamento;
- experiência;
- apoio institucional.

# 2462. Alterações da oportunidade vinculada

Poderão produzir solicitação de reavaliação sobre:

- prontidão;
- dependência;
- bloqueio;
- custo;
- risco;
- agenda;
- alternativa.

# 2463. Alternativa registrada

Deverá preservar diferenças materiais de:

- custo;
- fornecedor;
- localização;
- modalidade;
- risco;
- elegibilidade;
- relação comercial;
- prazo.

# 2464. Comparação produzida

A comparação deverá registrar critérios, pesos quando aplicáveis, incertezas e campos ausentes.

Não deverá declarar vencedor universal sem fundamento legítimo.

# 2465. Família 14 — Manutenção e encerramento

Eventos principais:

- `OportunidadePausada`;
- `OportunidadeRetomada`;
- `OportunidadeTornadaIndisponivel`;
- `OportunidadeDisponibilizadaNovamente`;
- `OportunidadeExpirada`;
- `OportunidadeEncerrada`;
- `OportunidadeCancelada`;
- `OportunidadeArquivada`;
- `OportunidadeReaberta`.

# 2466. Pausa

Deverá registrar:

- causa;
- escopo;
- início;
- condição de retomada;
- apresentações suspensas;
- processos externos preservados.

# 2467. Retomada

Deverá exigir revalidação proporcional.

# 2468. Expiração

Deverá preservar:

- visualizações;
- salvamentos;
- interesses;
- inscrições;
- transações;
- histórico.

# 2469. Encerramento

Deverá registrar término regular e ausência de previsão de retorno.

# 2470. Cancelamento

Deverá registrar decisão explícita do responsável.

Não representa fracasso do participante.

# 2471. Arquivamento

Deverá retirar a oportunidade do uso corrente sem apagar fatos.

# 2472. Reabertura

Deverá exigir:

- nova avaliação;
- nova versão;
- nova validade;
- preservação do ciclo anterior;
- ausência de mudança material que exija novo registro.

# 2473. Família 15 — Contestação e correção

Eventos principais:

- `OportunidadeContestada`;
- `ContestacaoDeOportunidadeEmAnalise`;
- `ContestacaoDeOportunidadeResolvida`;
- `CorrecaoDeOportunidadeProposta`;
- `OportunidadeCorrigida`;
- `EfeitosDeCorrecaoDeOportunidadeAplicados`.

# 2474. OportunidadeContestada

Deverá registrar:

- campo ou decisão contestada;
- contestante;
- fundamento;
- evidências;
- impacto;
- efeitos limitados;
- prazo de revisão.

# 2475. Efeitos da contestação

Poderão incluir:

- suspensão da apresentação;
- bloqueio de automações;
- redução de confiança;
- manutenção de versões;
- notificação de consumidores;
- proteção do participante.

# 2476. OportunidadeCorrigida

A correção deverá ser compensatória.

Deverá preservar:

- valor anterior;
- valor corrigido;
- fonte;
- motivo;
- autoridade;
- temporalidade;
- consumidores afetados;
- necessidade de reprocessamento.

# 2477. Correções retroativas

A correção não deverá alterar silenciosamente o que foi conhecido e apresentado no passado.

# 2478. Família 16 — Permissões e revogação

Eventos principais:

- `UsoDeContextoParaOportunidadesAutorizado`;
- `UsoDeContextoParaOportunidadesLimitado`;
- `PermissaoDeLocalizacaoAlterada`;
- `CompartilhamentoDeOportunidadeAutorizado`;
- `CompartilhamentoDeOportunidadeRevogado`;
- `PermissaoDeContextoRevogada`;
- `RevogacaoDeContextoEmPropagacao`;
- `RevogacaoDeContextoPropagada`.

# 2479. Autorização

Deverá registrar:

- finalidade;
- campos;
- consumidor;
- período;
- frequência;
- redistribuição;
- retenção;
- possibilidade de revogação.

# 2480. Limitação

A limitação poderá alterar:

- categorias;
- fontes;
- precisão de localização;
- frequência;
- período;
- consumidores;
- tipos sensíveis.

# 2481. Revogação

Deverá interromper:

- novas avaliações dependentes;
- novos recortes;
- novos compartilhamentos;
- novas apresentações personalizadas incompatíveis.

# 2482. Revogação pendente

Enquanto houver consumidores pendentes:

- o estado deverá permanecer em propagação;
- novos usos deverão ser bloqueados;
- falhas deverão ser registradas;
- sucesso integral não deverá ser declarado.

# 2483. Revogação concluída

Somente deverá ser reconhecida após confirmação suficiente de propagação.

# 2484. Família 17 — Propagação e integrações

Eventos principais:

- `RecorteDeOportunidadeProduzido`;
- `RecorteDeOportunidadePropagado`;
- `RecorteDeOportunidadeRejeitado`;
- `ReavaliacaoDeProximoPassoSolicitada`;
- `ReavaliacaoDeIntervencaoSolicitada`;
- `ReavaliacaoDeObjetivoSolicitada`;
- `ReavaliacaoPorEventoDeVidaSolicitada`;
- `ProcessamentoDeRecorteDeOportunidadeConfirmado`.

# 2485. Recorte funcional

O recorte deverá conter somente:

- dados necessários;
- finalidade;
- validade;
- autoridade;
- sensibilidade;
- limitações;
- versão.

# 2486. Consumidores

Capacidades consumidoras deverão receber informações, não decisões impostas.

Elas deverão reavaliar seus próprios agregados.

# 2487. Próximos Passos

Oportunidades Ativas poderá solicitar revisão.

Ela não poderá:

- cancelar o passo;
- concluí-lo;
- alterar prioridade;
- assumir responsabilidade.

# 2488. Intervenções Contextuais

Deverá receber elementos suficientes para decidir entre apresentação, pergunta, espera ou silêncio.

# 2489. Objetivos

A oportunidade não deverá confirmar progresso ou conclusão.

# 2490. Eventos de Vida

Mudanças contextuais poderão causar reavaliação, sem autorizar exploração comercial.

# 2491. Família 18 — Visualização e notificações

Eventos principais:

- `VisaoDeOportunidadesAcessada`;
- `BuscaDeOportunidadesRealizada`;
- `FiltroDeOportunidadesAplicado`;
- `OrdenacaoDeOportunidadesAlterada`;
- `DetalheDeOportunidadeAcessado`;
- `ExplicacaoDeRelevanciaSolicitada`;
- `RelacaoComercialConsultada`;
- `HistoricoDeOportunidadeConsultado`;
- `NotificacaoDeOportunidadeEmitida`;
- `NotificacaoDeOportunidadeSilenciada`.

# 2492. Eventos de leitura

Eventos de leitura não deverão alterar:

- relevância;
- interesse;
- prioridade;
- elegibilidade;
- disponibilidade;
- contratação.

# 2493. Busca

Consultas sensíveis deverão utilizar retenção e acesso reforçados.

Não deverão alimentar publicidade.

# 2494. Notificações

O evento deverá registrar:

- finalidade;
- canal;
- conteúdo minimizado;
- sensibilidade;
- motivo;
- controle do participante;
- relação comercial.

# 2495. Notificações publicitárias

Deverão possuir contratos e identificação distintos das notificações funcionais.

# 2496. Família 19 — Falhas e reconstrução

Eventos principais:

- `ProcessamentoDeOportunidadeFalhou`;
- `PropagacaoDeOportunidadeFalhou`;
- `SincronizacaoDeOportunidadePendente`;
- `ConflitoDeVersaoDeOportunidadeIdentificado`;
- `EventoDeOportunidadeForaDeOrdemIdentificado`;
- `DuplicidadeDeEventoDeOportunidadeIgnorada`;
- `ProcessamentoDeOportunidadeRecuperado`;
- `EstadoDeOportunidadeReconstruido`.

# 2497. Falha de processamento

Deverá registrar:

- operação;
- etapa;
- versão;
- impacto;
- efeitos aplicados;
- efeitos não aplicados;
- possibilidade de repetição;
- recuperação prevista.

# 2498. Falha de propagação

Deverá identificar consumidores pendentes.

O fluxo não deverá ser apresentado como integralmente concluído.

# 2499. Sincronização pendente

Deverá preservar o último estado válido e reduzir automações dependentes.

# 2500. Evento fora de ordem

O consumidor deverá:

- verificar versão;
- preservar o evento;
- aguardar dependências;
- impedir transição impossível;
- reconciliar;
- registrar auditoria.

# 2501. Conflito de versão

Não deverá haver sobrescrita silenciosa.

O conflito deverá preservar:

- versão esperada;
- versão atual;
- comandos concorrentes;
- fatos produzidos;
- decisão de reconciliação.

# 2502. Reconstrução

O estado deverá ser reconstruível a partir:

- dos eventos válidos;
- das versões;
- das correções;
- dos eventos compensatórios;
- das permissões;
- das revogações;
- das decisões de reconciliação.

# 2503. Idempotência

Toda operação material deverá utilizar chave de idempotência.

O reprocessamento não poderá duplicar:

- oportunidade;
- candidatura;
- ativação;
- apresentação;
- salvamento;
- interesse;
- inscrição;
- vínculo;
- notificação;
- contestação;
- revogação;
- arquivamento.

# 2504. Duplicidade semântica

Eventos diferentes poderão representar a mesma intenção funcional.

A capacidade deverá detectar duplicidade por:

- participante;
- oportunidade;
- ação;
- finalidade;
- intervalo;
- origem;
- payload funcional.

# 2505. Ordenação

A ordenação deverá considerar:

- versão do agregado;
- causalidade;
- temporalidade;
- dependências;
- estado atual.

# 2506. Estados impossíveis

Não poderão ocorrer:

- apresentação após revogação efetiva;
- ativação após encerramento sem reabertura;
- aceitação antes do envio;
- contratação antes do fato externo correspondente;
- correção antes do fato corrigido;
- disponibilidade posterior à expiração sem nova versão;
- interesse após ocultação ampla sem nova autorização.

# 2507. Concorrência

Alterações concorrentes deverão utilizar versão esperada.

Exemplos:

- participante oculta enquanto fornecedor altera preço;
- fonte encerra enquanto inscrição é enviada;
- revogação ocorre durante propagação;
- correção ocorre durante apresentação.

# 2508. Atomicidade funcional

Operações compostas deverão declarar quais efeitos precisam ocorrer conjuntamente.

Exemplo:

```text
enviar inscrição
→ persistir autorização
→ registrar conteúdo enviado
→ transmitir ao destinatário
→ registrar protocolo
```

Falha intermediária deverá permanecer explícita.

# 2509. Eventos compostos

Um fluxo poderá produzir múltiplos eventos.

Nenhum evento composto deverá ocultar fatos materialmente distintos.

# 2510. Correção compensatória

Eventos históricos não deverão ser alterados ou excluídos para corrigir significado.

A correção deverá produzir novo evento.

# 2511. Exclusão e anonimização

A exclusão deverá distinguir:

- remoção da superfície;
- encerramento;
- arquivamento;
- anonimização;
- eliminação legal;
- preservação mínima para auditoria.

# 2512. Retenção

A retenção deverá considerar:

- finalidade;
- sensibilidade;
- obrigação legal;
- relação externa;
- contestação;
- auditoria;
- revogação;
- necessidade de reconstrução.

# 2513. Logs

Logs técnicos não deverão conter:

- narrativas sensíveis completas;
- diagnósticos inferidos;
- dados de terceiros desnecessários;
- conteúdo espiritual;
- condição financeira detalhada;
- conteúdo jurídico protegido;
- dados de saúde sem necessidade.

# 2514. Responsabilidades do produtor

O produtor deverá:

1. validar identidade;
2. validar autoridade;
3. aplicar finalidade;
4. minimizar payload;
5. preservar proveniência;
6. usar contrato vigente;
7. aplicar idempotência;
8. persistir antes de publicar;
9. classificar sensibilidade;
10. registrar temporalidade;
11. informar limitações;
12. tratar falhas;
13. permitir auditoria;
14. não fabricar significado;
15. não ocultar relações comerciais.

# 2515. Responsabilidades do consumidor

O consumidor deverá:

1. validar contrato;
2. verificar versão;
3. aplicar finalidade;
4. respeitar permissões;
5. verificar idempotência;
6. controlar ordenação;
7. preservar causalidade;
8. não ampliar autoridade;
9. governar sua própria decisão;
10. limitar retenção;
11. tratar revogação;
12. registrar processamento;
13. informar falhas;
14. não duplicar efeitos;
15. não reinterpretar publicidade como relevância.

# 2516. Compatibilidade

Consumidores deverão:

- aceitar versões compatíveis;
- rejeitar versões desconhecidas de forma segura;
- preservar eventos não processados;
- registrar incompatibilidade;
- evitar descarte silencioso;
- permitir reprocessamento posterior.

# 2517. Explicabilidade

O participante deverá poder compreender:

- qual evento ocorreu;
- quem o originou;
- qual fonte foi utilizada;
- qual autoridade existia;
- quais dados foram considerados;
- qual finalidade foi aplicada;
- quais consumidores receberam recortes;
- quais efeitos foram produzidos;
- como contestar;
- como revogar.

# 2518. Auditoria

A auditoria deverá reconstruir:

```text
sinal, comando ou informação
→ identidade
→ autoridade
→ finalidade
→ avaliação
→ proposta, quando aplicável
→ decisão
→ persistência
→ evento
→ atualização do agregado
→ recorte
→ consumidor
→ processamento
→ interação, falha, correção ou revogação
```

# 2519. Métricas iniciais dos contratos

As métricas poderão avaliar:

- eventos sem autoridade;
- eventos sem finalidade;
- contratos incompatíveis;
- duplicidades;
- eventos fora de ordem;
- conflitos de versão;
- falhas parciais;
- propagações pendentes;
- revogações incompletas;
- payloads excessivos;
- eventos sensíveis em logs;
- relações comerciais ausentes;
- correções aplicadas;
- estados reconstruídos;
- consumidores divergentes;
- latência de processamento;
- rejeições seguras;
- incidentes de causalidade indevida.

As métricas deverão avaliar o sistema, não o participante.

# 2520. Comportamentos proibidos

Os contratos não deverão:

1. publicar comando como fato;
2. publicar proposta como decisão;
3. publicar evento antes da persistência;
4. reconhecer interesse por visualização;
5. reconhecer aceitação por inscrição;
6. reconhecer resultado por contratação;
7. reconhecer evolução por participação;
8. fabricar disponibilidade;
9. fabricar elegibilidade;
10. fabricar causalidade;
11. omitir patrocínio ou comissão;
12. elevar relevância por receita;
13. utilizar contexto sensível para publicidade;
14. ampliar autoridade da fonte;
15. reescrever histórico;
16. duplicar efeitos;
17. ignorar ordenação;
18. sobrescrever conflitos;
19. declarar revogação antes da propagação;
20. apresentar falha parcial como sucesso integral.

# 2521. Critérios de aceite

A extensão será considerada consolidada quando:

1. distinguir comando, proposta e evento;
2. definir o agregado;
3. definir estrutura comum;
4. definir identidade e versionamento;
5. governar titular, ator, papel e autoridade;
6. preservar proveniência;
7. aplicar finalidade e sensibilidade;
8. definir temporalidades;
9. definir correlação e causalidade;
10. organizar famílias de eventos;
11. governar identificação e candidatura;
12. governar fonte e autoridade;
13. governar avaliação;
14. governar disponibilidade;
15. governar elegibilidade;
16. governar relevância;
17. governar risco e sensibilidade;
18. governar transparência comercial;
19. governar ativação;
20. governar apresentação;
21. governar interação;
22. governar inscrições e fatos externos;
23. governar vínculos;
24. governar encerramentos;
25. governar contestação e correção;
26. governar permissões e revogação;
27. governar propagação;
28. separar eventos de leitura;
29. tratar falhas e reconstrução;
30. aplicar idempotência, ordenação e concorrência;
31. preservar imutabilidade;
32. proteger logs e retenção;
33. definir responsabilidades de produtores e consumidores;
34. preservar explicabilidade e auditoria;
35. manter o participante no controle.

# 2522. Regras fundamentais

1. Comando não representa fato.
2. Proposta não representa decisão.
3. Evento somente é publicado após persistência suficiente.
4. Evento histórico é imutável.
5. Correção produz evento compensatório.
6. Titular, ator, papel e fonte permanecem distintos.
7. Autoridade é limitada ao contrato.
8. Finalidade precede processamento.
9. Minimização precede publicação.
10. Tempo do fato e tempo do conhecimento permanecem separados.
11. Correlação não representa causalidade.
12. Reprocessamento não duplica efeitos.
13. Eventos fora de ordem não criam estados impossíveis.
14. Conflitos não são sobrescritos silenciosamente.
15. Identificação não representa candidatura.
16. Candidatura não representa ativação.
17. Ativação não representa apresentação.
18. Apresentação não representa visualização.
19. Visualização não representa interesse.
20. Salvamento não representa prioridade.
21. Interesse não representa compromisso.
22. Inscrição não representa aceitação.
23. Aceitação não representa contratação.
24. Contratação não representa participação.
25. Participação não representa resultado.
26. Resultado não representa evolução.
27. Disponibilidade não representa elegibilidade.
28. Elegibilidade não representa aprovação.
29. Relevância não representa obrigação.
30. Patrocínio e comissão não alteram relevância.
31. Publicidade não produz evento funcional neutro.
32. Fonte somente confirma fatos de sua autoridade.
33. Oportunidades sensíveis exigem payload minimizado.
34. Eventos de leitura não alteram estado material.
35. Produtos especializados governam transações e entregas.
36. Capacidades consumidoras governam suas decisões.
37. Revogação interrompe novos usos.
38. Revogação somente termina após propagação.
39. Falha reduz automação.
40. Falha parcial não representa sucesso integral.
41. Métricas avaliam o sistema.
42. O participante permanece no controle.

# 2523. Continuidade normativa

`PAS-001-OA-EVENT-001 1.0.0` deverá ser registrado como a **quarta extensão normativa da Capacidade 06 — Oportunidades Ativas**.

A extensão deverá:

- preservar fundamentos, ciclo de vida e visualização;
- preservar o `PAS-001 0.5.0`;
- manter as Capacidades 02, 03, 04 e 05 como `Functionally complete`;
- manter a Capacidade 06 como `In progress`;
- elevar o progresso editorial de `60%` para `80%`;
- consolidar os contratos das 19 famílias de eventos;
- preservar imutabilidade, autoridade, finalidade e temporalidade;
- governar correção compensatória;
- consolidar idempotência, ordenação, concorrência e reconstrução;
- preservar neutralidade comercial;
- estabelecer as integrações funcionais como próxima etapa.

O bloco seguinte será:

> **Integrações funcionais da Capacidade de Oportunidades Ativas com Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Próximos Passos, Intervenções Contextuais, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer, produtos especializados, organizações, fornecedores, serviços profissionais, fontes públicas e sistemas externos.**