---
id: PAS-001-CC-UIC-001
title: Unidade de Implementação da Capacidade de Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
parent: PAS-001-ENGINEERING-HANDOFF-001
capability: PAS-001-CC
normative: true
related:
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-LIFECYCLE-001
  - PAS-001-CC-EVENT-INTEGRATION-001
  - PAS-001-CC-CONTRACT-001
  - GIA-000
  - GLPA-001
---

# PAS-001-CC-UIC-001 — Unidade de Implementação da Capacidade de Captura de Contexto

> **Estado:** `Draft 0.1.0`.
>
> Esta unidade traduz tecnicamente a capacidade funcional de Captura de Contexto sem alterar sua autoridade, seus contratos, seus estados, seus eventos ou seus guardrails. O documento não autoriza implementação em produção e não decide tecnologias específicas.

# 7001. Pergunta central

> Como implementar tecnicamente a Captura de Contexto preservando finalidade, autoridade, sessão, entrada original, transcrição, interpretação, síntese, confirmação, autorização, persistência, correção e revogação como conceitos distintos e verificáveis?

# 7002. Autoridade, finalidade e escopo

## 7002.1 Autoridades normativas

A interpretação deverá respeitar a seguinte ordem:

1. Foundation e Princípios Permanentes;
2. `GIA-000`;
3. `GLPA-001`;
4. [`PAS-001 1.0.0`](pas-001-guivos-journey.md);
5. [`PAS-001-CAPABILITY-MAP-001 1.0.1`](pas-001-guivos-journey-mapa-final-capacidades.md);
6. [`PAS-001-ENGINEERING-HANDOFF-001`](pas-001-guivos-journey-engineering-handoff.md) e seu overlay efetivo;
7. [`PAS-001-CC-LIFECYCLE-001`](pas-001-captura-de-contexto-ciclo-de-vida.md);
8. [`PAS-001-CC-EVENT-INTEGRATION-001`](pas-001-captura-de-contexto-eventos-integracoes-funcionais.md);
9. [`PAS-001-CC-CONTRACT-001`](pas-001-captura-de-contexto-kpis-cenarios-contrato-final.md);
10. esta UIC;
11. especificações técnicas derivadas;
12. código, schemas, infraestrutura e configuração.

Em caso de conflito, prevalece a autoridade normativa superior. A solução técnica deverá ser corrigida antes de qualquer tentativa de reinterpretar o contrato funcional.

## 7002.2 Finalidade

A UIC-01 deverá:

- decompor a Captura de Contexto em unidades técnicas rastreáveis;
- preservar distinções entre entrada, transcrição, interpretação, síntese e confirmação;
- definir agregados, identidades e invariantes candidatos;
- mapear comandos, propostas, sinais e eventos;
- delimitar produtores e consumidores autorizados;
- classificar persistência temporária, confirmada e derivada;
- incorporar finalidade, autorização, correção e revogação;
- orientar observabilidade, auditoria e testes;
- registrar dependências da Onda 0;
- produzir critérios de prontidão para implementação.

## 7002.3 Escopo incluído

O escopo inicial cobre:

1. sessões de captura;
2. explicação de finalidade;
3. entradas textuais, por voz, imagem, vídeo, arquivo, formulário, sensor ou integração autorizada;
4. preservação de conteúdo original;
5. transcrição e normalização;
6. interpretação assistida;
7. síntese revisável;
8. confirmação total ou parcial;
9. persistência temporária ou autorizada;
10. correção, contestação e revogação;
11. recortes fornecidos a consumidores;
12. eventos, auditoria, observabilidade e testes.

## 7002.4 Escopo excluído nesta versão

A versão `0.1.0` não decide:

- linguagem de programação;
- framework de aplicação;
- provedor de nuvem;
- banco de dados específico;
- broker específico;
- tecnologia de transcrição;
- tecnologia de armazenamento multimodal;
- topologia final de serviços;
- desenho visual definitivo;
- cronograma de implementação;
- autorização de produção.

# 7003. Responsabilidade técnica da unidade

A UIC-01 é responsável por traduzir a capacidade para mecanismos que permitam:

- iniciar uma sessão com finalidade explícita;
- explicar uso, retenção e possibilidades de correção;
- receber entradas por canais autorizados;
- preservar a fonte original e sua proveniência;
- gerar representações derivadas sem promovê-las a fato;
- apresentar síntese para revisão;
- registrar confirmação delimitada;
- registrar autorização por finalidade;
- persistir temporária ou definitivamente conforme autoridade;
- corrigir sem apagar histórico necessário;
- revogar e propagar efeitos aplicáveis;
- disponibilizar somente recortes minimizados aos consumidores.

A UIC-01 não decide se um conteúdo será incorporado ao Contexto Vivo. Ela apenas produz material candidato, rastreável e autorizado para avaliação própria da capacidade receptora.

# 7004. Decisões proibidas

A implementação não poderá:

1. interpretar entrada como confirmação;
2. tratar transcrição como verdade;
3. tratar interpretação como fato humano;
4. tratar síntese como perfil integral;
5. persistir definitivamente sem autoridade aplicável;
6. incorporar conteúdo automaticamente ao Contexto Vivo;
7. criar Objetivo, Evento de Vida ou Próximo Passo automaticamente;
8. inferir diagnóstico clínico, jurídico, financeiro, moral ou espiritual;
9. ampliar finalidade por conveniência técnica;
10. reutilizar dados sensíveis para publicidade;
11. transformar silêncio em consentimento;
12. apagar histórico necessário para representar correção;
13. concluir revogação antes da propagação exigida;
14. expor conteúdo sensível em logs, índices ou traces;
15. converter ausência de erro técnico em confirmação funcional;
16. usar frequência de captura como medida de valor humano;
17. criar identidade determinística por inferência;
18. permitir que Intelligence confirme fatos ou decisões do participante;
19. permitir que um consumidor altere a autoridade da captura;
20. transformar um canal de entrada em autoridade funcional.

# 7005. Unidade de consistência e agregados candidatos

## 7005.1 Hipótese inicial

A primeira hipótese de domínio estabelece `CaptureRecord` como raiz de rastreabilidade e `CaptureSession` como ciclo operacional de interação. Essa hipótese deverá ser validada antes de atingir `Domain model proposed`.

## 7005.2 Agregados, entidades e objetos candidatos

| Elemento | Papel candidato | Natureza inicial | Autoridade funcional relacionada |
|---|---|---|---|
| `CaptureRecord` | Raiz de rastreabilidade da captura | Agregado candidato | Registro da captura |
| `CaptureSession` | Ciclo operacional da interação | Entidade ou agregado candidato | Sessão de captura |
| `CapturePurpose` | Finalidade apresentada e autorizada | Objeto de valor | Finalidade |
| `CaptureInput` | Entrada original e metadados | Entidade | Material recebido |
| `CaptureMediaReference` | Referência protegida a conteúdo multimodal | Objeto de valor | Fonte original |
| `CaptureTranscript` | Representação transcrita | Entidade derivada | Transcrição |
| `CaptureInterpretation` | Leitura derivada e incerta | Entidade derivada | Interpretação |
| `CaptureSynthesis` | Síntese apresentada ao participante | Entidade versionada | Síntese |
| `CaptureConfirmation` | Confirmação delimitada | Entidade ou registro | Confirmação |
| `CaptureAuthorization` | Permissão por finalidade | Entidade ou política vinculada | Autorização |
| `CaptureSlice` | Recorte minimizado para consumidor | Projeção autorizada | Integração |
| `CaptureCorrection` | Correção compensatória | Registro imutável | Correção |
| `CaptureContest` | Contestação do conteúdo ou derivação | Registro | Contestação |
| `CaptureRevocation` | Revogação e propagação | Registro coordenador | Revogação |
| `CaptureProcessingAttempt` | Execução técnica de processamento | Registro técnico | Operação |
| `CaptureDeliveryRecord` | Entrega de síntese ou recorte | Registro técnico | Integração |

## 7005.3 Questões obrigatórias de modelagem

A evolução da unidade deverá confirmar:

- limite transacional de `CaptureRecord`;
- relação cardinal entre registro e sessões;
- identidade técnica de cada entrada;
- imutabilidade da fonte original;
- versionamento de transcrições e sínteses;
- granularidade da confirmação;
- vínculo entre autorização e finalidade;
- estratégia de consistência para correção e revogação;
- reconstrução de projeções;
- proteção de conteúdo multimodal;
- separação entre dados funcionais e telemetria técnica.

# 7006. Invariantes iniciais

1. Toda sessão possui finalidade explícita e rastreável.
2. Entrada original permanece distinta de qualquer representação derivada.
3. Transcrição permanece distinta da entrada original.
4. Interpretação permanece distinta de fato e confirmação.
5. Síntese é revisável, versionada e contestável.
6. Confirmação é limitada ao conteúdo apresentado e à finalidade declarada.
7. Autorização não é inferida pela simples utilização da interface.
8. Persistência temporária não equivale a incorporação ao Contexto Vivo.
9. Persistência confirmada exige referência de autoridade e finalidade.
10. Correções produzem registros compensatórios e preservam proveniência.
11. Revogações bloqueiam novos usos e propagam efeitos aplicáveis.
12. Consumidores recebem recortes minimizados por padrão.
13. Reprocessamento idempotente não duplica sessões, entradas ou eventos.
14. Falha parcial não poderá ser apresentada como captura concluída.
15. Índices e projeções não se tornam sistemas de registro.
16. Resultados de IA preservam modelo, versão, confiança e proveniência.
17. Conteúdo sensível não poderá aparecer em logs operacionais comuns.
18. Retenção deverá ser declarada por classe de ativo.
19. Expiração de dado temporário deverá ser verificável.
20. A mesma confirmação não poderá autorizar finalidades diferentes por inferência.
21. Revogação deverá impedir novos recortes após a data efetiva.
22. Contestação deverá coexistir com a evidência original sem silenciosamente reescrevê-la.
23. Nenhum evento técnico poderá ser promovido a evento funcional sem autoridade.
24. Nenhuma métrica técnica poderá calcular valor ou evolução humana.

# 7007. Modelo de estados e transições

## 7007.1 Estados funcionais preservados

A implementação deverá representar, no mínimo:

- `Not initiated`;
- `Explaining purpose`;
- `Awaiting participant`;
- `Capturing`;
- `Paused`;
- `Processing`;
- `Reflecting understanding`;
- `Awaiting review`;
- `Partially confirmed`;
- `Confirmed`;
- `Correction requested`;
- `Limited`;
- `Temporary`;
- `Abandoned`;
- `Expired`;
- `Contested`;
- `Revoked`;
- `Closed`;
- `Failed`.

## 7007.2 Metadados mínimos da transição

Toda transição deverá declarar:

- estado anterior;
- estado resultante;
- comando ou causa;
- ator autorizado;
- autoridade;
- finalidade;
- precondições;
- validações;
- evento funcional resultante;
- efeitos técnicos;
- efeitos externos;
- comportamento em falha;
- idempotency key;
- timestamp funcional;
- timestamp de registro;
- política de retomada.

## 7007.3 Regras iniciais

1. `Capturing` exige finalidade explicada.
2. `Processing` exige ao menos uma entrada válida ou justificativa técnica registrada.
3. `Awaiting review` exige síntese versionada.
4. `Partially confirmed` registra escopo confirmado e não confirmado.
5. `Confirmed` não implica persistência definitiva automática.
6. `Temporary` exige expiração e finalidade restrita.
7. `Correction requested` bloqueia usos incompatíveis até avaliação.
8. `Revoked` bloqueia novos usos sob a autorização revogada.
9. `Closed` não impede correção ou contestação quando normativamente permitida.
10. `Failed` deverá registrar etapa, causa, impacto e possibilidade de retomada.

# 7008. Comandos candidatos

| Comando | Ator candidato | Finalidade | Resultado possível |
|---|---|---|---|
| `StartCaptureSession` | Participante ou ator autorizado | Iniciar sessão | Sessão iniciada |
| `ExplainCapturePurpose` | Journey Experience | Registrar explicação | Finalidade explicada |
| `SubmitCaptureInput` | Participante ou integração autorizada | Receber entrada | Entrada recebida |
| `AttachCaptureMedia` | Participante ou dispositivo autorizado | Vincular mídia | Mídia vinculada |
| `PauseCaptureSession` | Participante ou sistema autorizado | Pausar | Sessão pausada |
| `ResumeCaptureSession` | Participante ou sistema autorizado | Retomar | Sessão retomada |
| `RequestCaptureProcessing` | Journey Domain | Solicitar processamento | Processamento solicitado |
| `RecordCaptureTranscript` | Serviço autorizado | Registrar transcrição | Transcrição produzida |
| `RecordCaptureInterpretation` | Intelligence ou regra autorizada | Registrar interpretação | Interpretação produzida |
| `PresentCaptureSynthesis` | Journey Experience | Apresentar síntese | Síntese apresentada |
| `ConfirmCaptureSynthesis` | Participante ou representante autorizado | Confirmar conteúdo | Confirmação registrada |
| `PartiallyConfirmCaptureSynthesis` | Participante | Confirmar parcialmente | Confirmação parcial registrada |
| `RequestCaptureCorrection` | Participante ou representante | Solicitar correção | Correção solicitada |
| `RegisterCaptureCorrection` | Autoridade competente | Registrar correção | Correção registrada |
| `AuthorizeCapturePersistence` | Participante ou autoridade aplicável | Autorizar persistência | Autorização registrada |
| `PersistCaptureTemporarily` | Journey Domain | Manter temporariamente | Persistência temporária registrada |
| `IssueCaptureSlice` | Journey Domain | Disponibilizar recorte | Recorte emitido |
| `ContestCaptureRecord` | Participante ou representante | Contestar | Contestação registrada |
| `RevokeCaptureAuthorization` | Participante ou autoridade aplicável | Revogar usos | Revogação iniciada |
| `ConfirmRevocationPropagation` | Integração autorizada | Confirmar propagação | Revogação propagada |
| `CloseCaptureSession` | Participante ou sistema autorizado | Encerrar | Sessão encerrada |
| `ExpireCaptureSession` | Política temporal | Expirar | Sessão expirada |
| `AbandonCaptureSession` | Participante ou política | Abandonar | Sessão abandonada |

Comando representa solicitação. Nenhum comando será tratado como fato reconhecido antes da validação, da autoridade e do registro suficiente.

# 7009. Eventos funcionais e técnicos

## 7009.1 Eventos funcionais candidatos

A nomenclatura final deverá permanecer consistente com o catálogo funcional vigente. As famílias iniciais incluem:

- `CaptureSessionStarted`;
- `CapturePurposeExplained`;
- `CaptureInputReceived`;
- `CaptureMediaAttached`;
- `CaptureSessionPaused`;
- `CaptureSessionResumed`;
- `CaptureProcessingRequested`;
- `CaptureTranscriptProduced`;
- `CaptureInterpretationProduced`;
- `CaptureSynthesisProduced`;
- `CaptureSynthesisPresented`;
- `CaptureSynthesisPartiallyConfirmed`;
- `CaptureSynthesisConfirmed`;
- `CaptureCorrectionRequested`;
- `CaptureCorrectionRegistered`;
- `CapturePersistenceAuthorized`;
- `TemporaryCapturePersistenceRegistered`;
- `CaptureSliceIssued`;
- `CaptureRecordContested`;
- `CaptureAuthorizationRevoked`;
- `CaptureRevocationPropagated`;
- `CaptureSessionClosed`;
- `CaptureSessionAbandoned`;
- `CaptureSessionExpired`;
- `CaptureFailureRegistered`.

## 7009.2 Eventos técnicos candidatos

Eventos técnicos poderão registrar:

- upload concluído;
- transcodificação concluída;
- processamento iniciado;
- processamento finalizado;
- retry agendado;
- timeout ocorrido;
- mensagem entregue;
- mensagem duplicada descartada;
- projeção atualizada;
- índice removido;
- dado temporário eliminado;
- chave rotacionada;
- alerta operacional disparado.

Evento técnico não comprova entrada humana, confirmação, autorização, correção ou revogação.

## 7009.3 Envelope mínimo

```yaml
event_id:
event_type:
event_version:
aggregate_id:
capture_record_id:
capture_session_id:
participant_id:
actor_id:
authority:
purpose:
source:
occurred_at:
recorded_at:
correlation_id:
causation_id:
idempotency_key:
sensitivity:
provenance:
authorization_reference:
retention_policy:
schema_version:
```

## 7009.4 Regras de entrega

- produtores deverão utilizar idempotency key quando aplicável;
- consumidores deverão tolerar duplicidade;
- ordenação deverá ser definida por agregado ou fluxo necessário;
- replay não poderá gerar nova confirmação ou autorização;
- falha de entrega deverá ser observável;
- eventos incompatíveis com o schema deverão ser isolados;
- consumidores deverão preservar correlação e causalidade;
- correções e revogações deverão possuir prioridade operacional definida.

# 7010. Interfaces produtoras

Produtores candidatos:

| Produtor | Pode produzir | Limite |
|---|---|---|
| Participante | Entradas, confirmações, correções, contestações e revogações | Somente sua autoridade ou representação válida |
| Representante autorizado | Ações delegadas | Exige escopo e validade da representação |
| Journey Experience | Interações e comandos de superfície | Não confirma fatos em nome do participante |
| Dispositivo autorizado | Entradas e metadados técnicos | Não interpreta finalidade |
| Integração externa autorizada | Entradas delimitadas | Exige proveniência e finalidade |
| Guivos Intelligence | Transcrições, interpretações e propostas derivadas | Não confirma fatos ou autorizações |
| Journey Domain | Eventos de domínio após validação | Não amplia autoridade |
| Platform | Fatos técnicos sob sua responsabilidade | Não cria evento funcional humano |

# 7011. Interfaces consumidoras

Consumidores candidatos:

| Consumidor | Uso permitido | Avaliação obrigatória |
|---|---|---|
| Contexto Vivo | Avaliar recortes candidatos | Própria autoridade e critérios |
| Histórico do participante | Apresentar registros autorizados | Finalidade e sensibilidade |
| Auditoria | Verificar decisões e trilhas | Acesso mínimo necessário |
| Observabilidade | Operar o sistema | Dados minimizados |
| Interface de revisão | Exibir síntese e correções | Identidade e autorização |
| Mecanismo de revogação | Propagar bloqueios e eliminações | Escopo e retenção residual |
| Intelligence | Processar recortes autorizados | Finalidade, modelo e proveniência |
| Produtos Guivos | Consumir recortes específicos | Contrato de integração e avaliação própria |

O recebimento de evento ou recorte não autoriza incorporação automática, decisão humana ou ampliação de finalidade.

# 7012. Persistência e classificação de dados

## 7012.1 Categorias

| Categoria | Característica | Sistema de registro candidato |
|---|---|---|
| Entrada original | Fonte preservada | Capture Record Store |
| Mídia original | Conteúdo protegido | Secure Media Store |
| Transcrição | Derivada e corrigível | Derived Content Store |
| Interpretação | Derivada, incerta e contestável | Interpretation Store |
| Síntese | Revisável e versionada | Capture Record Store |
| Confirmação | Delimitada e auditável | Capture Record Store |
| Autorização | Finalidade e validade | Authorization Store |
| Persistência temporária | Expiração e uso restrito | Temporary Store |
| Eventos | Imutáveis com compensação | Event Store ou log equivalente |
| Projeções | Reconstruíveis | Read Model Store |
| Índices | Recuperação | Search Index |
| Recortes | Minimizados por finalidade | Integration Projection |
| Telemetria | Operação técnica | Observability Platform |

Os nomes dos stores são conceituais e não representam escolha tecnológica.

## 7012.2 Temporalidade

Cada ativo deverá declarar:

- `valid_from`;
- `valid_until`;
- `retention_policy`;
- `temporary_until` quando aplicável;
- `revoked_at` quando aplicável;
- `deleted_at` ou evidência equivalente;
- justificativa de retenção residual;
- política de reconstrução.

## 7012.3 Correção e imutabilidade

- fontes originais não serão silenciosamente sobrescritas;
- transcrições e sínteses utilizarão versões;
- correções produzirão registros compensatórios;
- projeções poderão ser reconstruídas;
- índices deverão refletir correções e revogações;
- auditoria deverá preservar quem, quando, por que e sob qual autoridade.

# 7013. Busca, projeções e grafo

## 7013.1 Busca

A UIC deverá avaliar:

- recuperação por sessão, data, tipo e estado;
- busca protegida em conteúdo sensível;
- tokenização e indexação minimizadas;
- filtragem por finalidade e autorização;
- remoção ou bloqueio de índices após revogação;
- prevenção de exposição por autocomplete, logs ou analytics;
- rastreamento entre resultado e sistema de registro.

## 7013.2 Projeções

Projeções poderão suportar:

- sessões em andamento;
- sínteses aguardando revisão;
- correções pendentes;
- revogações em propagação;
- dados temporários próximos da expiração;
- recortes emitidos e consumidores;
- falhas técnicas por etapa.

Projeções não poderão se tornar autoridade por conveniência operacional.

## 7013.3 Grafo

Relações candidatas:

- `CaptureRecord` contém `CaptureSession`;
- `CaptureSession` recebeu `CaptureInput`;
- `CaptureTranscript` deriva de `CaptureInput`;
- `CaptureInterpretation` deriva de transcrição ou entrada;
- `CaptureSynthesis` deriva de interpretações e entradas;
- `CaptureConfirmation` confirma escopo de uma síntese;
- `CaptureAuthorization` autoriza finalidade específica;
- `CaptureSlice` deriva de conteúdo autorizado;
- consumidor recebeu recorte;
- correção substitui interpretação ou síntese anterior sem apagar proveniência;
- revogação afeta autorização, recortes e consumidores.

O grafo não poderá transformar relação, frequência, proximidade ou inferência em identidade definitiva.

# 7014. Superfícies e canais

Superfícies candidatas:

- aplicativo móvel;
- web;
- interface conversacional;
- voz;
- upload de mídia;
- formulários;
- dispositivos autorizados;
- integrações externas;
- interface administrativa restrita;
- interface de revisão e contestação.

Toda superfície deverá:

- explicar finalidade;
- identificar ator e participante;
- apresentar controles de pausa, revisão e encerramento;
- distinguir entrada original de síntese;
- suportar acessibilidade;
- evitar coerção e dark patterns;
- permitir correção e revogação quando aplicável;
- preservar mensagens de falha sem produzir falsa confirmação.

# 7015. Identidade, autorização e finalidade

## 7015.1 Ativos mínimos

Cada ação deverá declarar:

- participante;
- ator;
- papel;
- relação de representação quando aplicável;
- finalidade;
- escopo;
- autoridade;
- duração;
- canal;
- sensibilidade;
- evidência de autorização;
- política de revogação.

## 7015.2 Autorização contextual

A autorização deverá considerar:

- quem executa;
- em nome de quem;
- para qual finalidade;
- sobre qual conteúdo;
- em qual contexto;
- durante qual período;
- para quais consumidores;
- com qual nível de sensibilidade;
- quais correções ou revogações já existem.

## 7015.3 Regras

1. consentimento não será presumido;
2. autorização deverá ser específica e verificável;
3. representação deverá possuir escopo e validade;
4. menor de idade exigirá política própria;
5. dispositivo compartilhado exigirá proteção adicional;
6. acesso administrativo será excepcional e auditado;
7. finalidade comercial não autoriza conteúdo sensível;
8. revogação deverá impedir novos usos incompatíveis;
9. retenção residual deverá ser declarada;
10. consumidores deverão receber apenas o mínimo necessário.

# 7016. Segurança e privacidade

Requisitos iniciais:

- criptografia em trânsito e repouso;
- segregação de conteúdo sensível;
- gestão de chaves e rotação;
- prevenção de conteúdo em logs;
- proteção contra enumeração de registros;
- controle de acesso contextual;
- trilhas de auditoria imutáveis;
- retenção mínima;
- eliminação verificável;
- propagação de revogação;
- proteção de dispositivos compartilhados;
- prevenção de exfiltração por busca;
- classificação de mídia e metadados;
- limites de acesso de suporte;
- resposta a incidente;
- avaliação de terceiros e integrações;
- acessibilidade como requisito arquitetural;
- privacy by design e security by design.

# 7017. Intelligence e processamento assistido

Guivos Intelligence poderá:

- transcrever;
- classificar formato e idioma;
- identificar estrutura candidata;
- produzir interpretação com incerteza;
- gerar síntese revisável;
- detectar conflito ou baixa confiança;
- explicar por que uma síntese foi produzida;
- recomendar revisão humana.

Guivos Intelligence não poderá:

- confirmar fatos;
- confirmar autorização;
- decidir persistência definitiva;
- criar objetivo, evento ou próximo passo automaticamente;
- diagnosticar;
- calcular valor humano;
- ocultar incerteza;
- reutilizar conteúdo fora da finalidade;
- eliminar necessidade de revisão quando o contrato exigir.

Todo resultado deverá registrar:

- modelo;
- versão;
- parâmetros relevantes;
- timestamp;
- entradas de referência;
- confiança ou incerteza;
- explicação disponível;
- política de retenção;
- finalidade;
- possibilidade de contestação.

# 7018. Observabilidade e auditoria

## 7018.1 Métricas técnicas iniciais

- sessões iniciadas;
- sessões concluídas;
- sessões abandonadas;
- sessões expiradas;
- falhas por etapa;
- latência de processamento;
- duplicidades impedidas;
- eventos fora de ordem;
- retries e timeouts;
- sínteses aguardando revisão;
- correções pendentes;
- revogações não propagadas;
- persistências sem autorização detectadas;
- acessos negados;
- violações de guardrail;
- divergências entre estado e projeções;
- reconstruções realizadas;
- dados temporários expirados;
- índices removidos;
- recortes emitidos por finalidade.

## 7018.2 Logs e traces

Logs e traces deverão:

- utilizar identificadores técnicos pseudonimizados;
- evitar conteúdo bruto;
- preservar correlação;
- registrar autoridade e finalidade sem expor conteúdo;
- possuir retenção proporcional;
- permitir auditoria de falhas, correções e revogações;
- separar trilha operacional de trilha normativa.

## 7018.3 Guardrails observáveis

Devem existir sinais para:

- persistência sem autorização;
- uso por finalidade divergente;
- recorte excessivo;
- revogação não propagada;
- índice residual;
- interpretação tratada como fato;
- confirmação criada por ator não autorizado;
- conteúdo sensível em log;
- consumidor não autorizado;
- ausência de proveniência;
- evento funcional sem autoridade.

# 7019. Estratégia de testes

## 7019.1 Categorias obrigatórias

- testes unitários de invariantes;
- testes de máquina de estados;
- testes de contrato;
- testes de schemas;
- testes de idempotência;
- testes de concorrência;
- testes de ordenação;
- testes de replay;
- testes de correção compensatória;
- testes de revogação;
- testes de autorização;
- testes de finalidade;
- testes de minimização;
- testes de persistência temporária;
- testes de reconstrução;
- testes de falha segura;
- testes de privacidade;
- testes de segurança;
- testes de acessibilidade;
- testes de integração;
- testes dos cenários normativos do contrato final.

## 7019.2 Cenários críticos mínimos

1. entrada recebida não gera confirmação;
2. transcrição divergente pode ser corrigida;
3. síntese parcial pode ser confirmada sem confirmar o restante;
4. persistência temporária expira;
5. persistência definitiva sem autorização é rejeitada;
6. retry não duplica entrada;
7. replay não cria nova autorização;
8. consumidor não autorizado não recebe recorte;
9. Contexto Vivo avalia e rejeita recorte sem alterar a captura;
10. revogação bloqueia novo recorte;
11. correção atualiza projeções sem apagar evidência;
12. falha de transcrição não encerra sessão como concluída;
13. evento fora de ordem não viola invariantes;
14. log não contém conteúdo sensível;
15. modelo de IA com baixa confiança exige revisão;
16. representante com autorização expirada é rejeitado;
17. dispositivo compartilhado exige autenticação adicional;
18. índice residual após revogação dispara alerta;
19. contestação permanece visível na trilha;
20. nenhuma métrica atribui valor ao participante.

# 7020. Dependências da Onda 0

| Dependência | Estado inicial | Necessidade para a UIC-01 |
|---|---|---|
| Identidade de participante e ator | Required | Vincular ações e autoridade |
| Representação e delegação | Required | Validar atuação em nome de terceiros |
| Autorização e finalidade | Required | Controlar uso e persistência |
| Envelope de eventos | Required | Padronizar integração |
| Idempotência | Required | Evitar duplicidade |
| Auditoria | Required | Preservar trilhas |
| Criptografia | Required | Proteger conteúdo |
| Retenção e eliminação | Required | Governar temporalidade |
| Observabilidade | Required | Operar e detectar violações |
| Catálogo de erros | Required | Padronizar falhas |
| Versionamento de schemas | Required | Evoluir contratos técnicos |
| Propagação de revogação | Required | Bloquear novos usos |
| Testes de contrato | Required | Verificar guardrails |
| Secure media handling | Required when multimodal | Proteger mídia |
| Search security | Required when indexed | Prevenir exposição |

Essas dependências precisam de contratos mínimos, não de implementação total de toda a Platform Layer.

# 7021. Riscos iniciais

| ID | Risco | Impacto | Mitigação inicial |
|---|---|---|---|
| UIC01-RISK-001 | Mistura entre entrada e interpretação | Alto | Tipos e stores distintos |
| UIC01-RISK-002 | Persistência sem autorização | Crítico | Invariante e policy enforcement |
| UIC01-RISK-003 | Conteúdo sensível em logs | Crítico | Redação, testes e alertas |
| UIC01-RISK-004 | Revogação incompleta | Alto | Protocolo e observabilidade |
| UIC01-RISK-005 | Duplicidade por retry | Médio | Idempotência por comando e evento |
| UIC01-RISK-006 | Índice como fonte primária | Alto | Rastreio ao system of record |
| UIC01-RISK-007 | IA promovida a autoridade | Crítico | Guardrails e revisão |
| UIC01-RISK-008 | Recorte excessivo para consumidor | Alto | Minimização e contratos |
| UIC01-RISK-009 | Perfil paralelo em grafo | Crítico | Finalidade, proveniência e auditoria |
| UIC01-RISK-010 | Falha parcial apresentada como sucesso | Alto | Estados e compensação |
| UIC01-RISK-011 | Representação inválida | Alto | Escopo, validade e auditoria |
| UIC01-RISK-012 | Retenção além do necessário | Alto | Políticas e jobs verificáveis |

# 7022. Critérios de prontidão

A UIC-01 poderá atingir `Technically ready for implementation` quando:

1. agregados e limites estiverem definidos;
2. identidades estiverem especificadas;
3. invariantes estiverem verificáveis;
4. estados e transições estiverem completos;
5. comandos e eventos estiverem mapeados;
6. produtores e consumidores estiverem delimitados;
7. persistência estiver classificada;
8. busca, projeções e grafo estiverem delimitados;
9. autorização e finalidade estiverem incorporadas;
10. correção, contestação e revogação estiverem implementáveis;
11. observabilidade estiver definida;
12. estratégia de testes estiver completa;
13. dependências estiverem classificadas;
14. riscos estiverem registrados;
15. guardrails críticos estiverem testáveis;
16. não houver conflito com as autoridades funcionais.

# 7023. Critérios de reabertura

A unidade deverá ser reaberta quando:

- agregado não preservar invariantes;
- nova tecnologia impedir correção ou revogação;
- consumidor ampliar finalidade;
- integração transferir decisão;
- evento técnico for usado como fato humano;
- modelo de IA ultrapassar sua autoridade;
- persistência temporária não puder ser eliminada;
- índice não puder refletir revogação;
- autorização contextual não puder ser verificada;
- cenário normativo não puder ser testado;
- guardrail crítico não puder ser observado;
- conflito com contrato final for demonstrado.

# 7024. Lacunas abertas da versão 0.1.0

| ID | Lacuna | Classificação | Próxima ação |
|---|---|---|---|
| UIC01-GAP-001 | Confirmar limite entre CaptureRecord e CaptureSession | Domain design | Elaborar mapa de agregados |
| UIC01-GAP-002 | Definir identidade técnica da entrada original | Domain design | Especificar identidade e proveniência |
| UIC01-GAP-003 | Definir armazenamento de conteúdo multimodal | Data architecture | Criar matriz comparativa |
| UIC01-GAP-004 | Definir protocolo de transcrição e correção | Intelligence integration | Especificar versionamento |
| UIC01-GAP-005 | Definir política de persistência temporária | Data governance | Criar política temporal |
| UIC01-GAP-006 | Definir propagação técnica de revogação | Integration architecture | Criar protocolo de revogação |
| UIC01-GAP-007 | Definir estratégia de reconstrução | Event architecture | Especificar replay e projeções |
| UIC01-GAP-008 | Definir critérios de busca sensível | Search architecture | Criar política de indexação |
| UIC01-GAP-009 | Definir dependências mínimas da Onda 0 | Platform architecture | Criar contratos mínimos |
| UIC01-GAP-010 | Definir matriz técnica dos guardrails | Engineering governance | Criar catálogo verificável |

# 7025. Estado da unidade

| Dimensão | Estado 0.1.0 |
|---|---|
| Fontes normativas | Mapeadas |
| Responsabilidade técnica | Definida |
| Decisões proibidas | Definidas |
| Agregados | Candidatos |
| Invariantes | Propostas |
| Estados e transições | Estrutura inicial |
| Comandos e eventos | Catálogo inicial |
| Produtores e consumidores | Candidatos delimitados |
| Persistência | Classificação inicial |
| Segurança e privacidade | Requisitos iniciais |
| Observabilidade | Sinais iniciais |
| Testes | Estratégia inicial |
| Dependências | Mapeadas |
| Riscos | Registrados |
| Estado técnico da UIC | `Normative sources mapped` |

# 7026. Próximo incremento

O próximo incremento deverá aprofundar:

> **Agregados, identidades e invariantes da Captura de Contexto.**

Esse trabalho deverá:

- confirmar ou rejeitar `CaptureRecord` como raiz;
- definir relação entre registro e sessão;
- classificar entidades e objetos de valor;
- especificar identidades e chaves;
- formalizar invariantes por comando;
- mapear consistência e concorrência;
- definir estratégia de reconstrução;
- resolver `UIC01-GAP-001` e `UIC01-GAP-002`;
- preparar a transição para `Domain model proposed`.

A aprovação desta versão não autoriza implementação em produção, contratação de tecnologia ou encerramento das lacunas abertas.
