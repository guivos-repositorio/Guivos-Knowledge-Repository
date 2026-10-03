---
id: PAS-001-ENGINEERING-HANDOFF-001
title: Handoff Arquitetural do Guivos Journey para Product Engineering
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
parent: PAS-001
normative: true
related:
  - GIA-000
  - GLPA-001
  - PAS-001
  - PAS-001-CAPABILITY-MAP-001
  - GE2-SYNC-008
---

# PAS-001-ENGINEERING-HANDOFF-001 — Handoff Arquitetural do Guivos Journey para Product Engineering

> **Estado:** `Draft 0.1.0`.
>
> Este documento inicia a tradução controlada da arquitetura funcional consolidada do Guivos Journey para unidades técnicas implementáveis, testáveis, seguras, observáveis e evolutivas. Ele não altera o `PAS-001 1.0.0`, o Mapa Final `1.0.1`, os contratos finais ou as 54 extensões normativas.

# 6001. Pergunta central

> Como transformar as nove capacidades funcionalmente concluídas do Guivos Journey em uma arquitetura técnica implementável, testável, segura, observável e evolutiva, sem transferir ou redefinir suas autoridades funcionais?

# 6002. Autoridade, finalidade e escopo

## 6002.1 Finalidade

O Handoff estabelece a ponte entre Product Architecture e Product Engineering.

Ele deverá:

- decompor responsabilidades funcionais em unidades técnicas rastreáveis;
- identificar agregados, entidades, objetos de valor, projeções e registros;
- mapear comandos, propostas, sinais, eventos funcionais e eventos técnicos;
- delimitar interfaces produtoras e consumidoras;
- orientar persistência, busca, grafo, APIs e mensageria;
- incorporar identidade, autorização, privacidade e segurança;
- estabelecer observabilidade, testes e critérios técnicos de prontidão;
- ordenar dependências e ondas de implementação;
- produzir backlog técnico rastreável às autoridades normativas.

## 6002.2 Escopo incluído

O escopo inicial cobre:

1. as nove capacidades do Guivos Journey;
2. os contratos funcionais entre capacidades;
3. as relações com Guivos Intelligence;
4. as relações com Service Layers;
5. as responsabilidades da Platform Layer;
6. identidade, autorização, auditoria e privacidade;
7. persistência, busca, grafo e eventos;
8. observabilidade, testes e operação;
9. dependências e ordem recomendada de implementação;
10. artefatos técnicos derivados.

## 6002.3 Escopo excluído nesta versão

A versão `0.1.0` não decide:

- linguagem de programação;
- framework de aplicação;
- provedor de nuvem;
- banco de dados específico;
- broker específico;
- topologia final de microsserviços;
- organização final dos times;
- estimativas comerciais;
- cronograma contratual;
- desenho visual definitivo das interfaces;
- estratégia definitiva de rollout.

Essas decisões dependerão de ADRs e especificações técnicas derivadas.

# 6003. Hierarquia normativa

A interpretação deverá respeitar a seguinte ordem:

1. Foundation e Princípios Permanentes;
2. `GIA-000`;
3. `GLPA-001`;
4. [`PAS-001 1.0.0`](pas-001-guivos-journey.md);
5. [`PAS-001-CAPABILITY-MAP-001 1.0.1`](pas-001-guivos-journey-mapa-final-capacidades.md);
6. contratos finais de cada capacidade;
7. extensões normativas especializadas;
8. este Handoff;
9. especificações técnicas derivadas;
10. ADRs, schemas, código e infraestrutura.

Quando houver conflito:

- a autoridade superior prevalece;
- a implementação deve ser interrompida no ponto conflitante;
- o conflito deve ser registrado com evidência;
- nenhuma decisão técnica poderá corrigir silenciosamente uma decisão funcional;
- o `PAS-001` somente será reaberto mediante conflito funcional demonstrado.

# 6004. Princípios permanentes da implementação

1. Capacidade não equivale a microsserviço.
2. Tela não representa autoridade funcional.
3. Banco de dados não define domínio.
4. Evento técnico não substitui evento funcional.
5. API não amplia autorização.
6. Integração não transfere decisão.
7. Disponibilidade técnica não significa legitimidade funcional.
8. Persistência não transforma inferência em fato.
9. Sincronização não transforma proposta em decisão.
10. IA apoia; não assume autoridade humana.
11. Receita, patrocínio e comissão não determinam relevância.
12. A ausência de ação pode ser resultado legítimo.
13. O silêncio pode ser comportamento correto.
14. Correções preservam o histórico.
15. Revogações devem ser propagadas.
16. Falha parcial não deve ser apresentada como sucesso integral.
17. Cada consumidor realiza sua própria avaliação funcional.
18. Segurança, privacidade e acessibilidade são requisitos arquiteturais.
19. Dados sensíveis não devem alimentar perfis paralelos.
20. Nenhum componente técnico poderá calcular valor humano.

# 6005. Modelo de unidade de trabalho por capacidade

Cada capacidade deverá ser traduzida por uma Unidade de Implementação de Capacidade, denominada `UIC`.

## 6005.1 Conteúdo mínimo da UIC

| Campo | Obrigatoriedade | Finalidade |
|---|---|---|
| Identidade da capacidade | Obrigatório | Preservar vínculo com o PAS-001 |
| Pergunta central | Obrigatório | Delimitar o problema funcional |
| Autoridade própria | Obrigatório | Explicitar decisões que pertencem à capacidade |
| Decisões proibidas | Obrigatório | Impedir transferência de autoridade |
| Agregados candidatos | Obrigatório | Identificar unidades de consistência |
| Entidades e objetos de valor | Obrigatório | Estruturar domínio sem antecipar tecnologia |
| Comandos | Obrigatório | Representar solicitações de alteração |
| Propostas e sinais | Quando aplicável | Preservar incerteza e não confirmação |
| Eventos funcionais | Obrigatório | Representar fatos reconhecidos |
| Eventos técnicos | Obrigatório | Sustentar integração e operação |
| Estados e transições | Obrigatório | Manter ciclo de vida verificável |
| Interfaces produtoras | Obrigatório | Delimitar origens autorizadas |
| Interfaces consumidoras | Obrigatório | Delimitar usos permitidos |
| Persistência | Obrigatório | Definir necessidade, temporalidade e integridade |
| Busca e projeções | Quando aplicável | Suportar leitura sem transferir autoridade |
| Relações de grafo | Quando aplicável | Representar conexões rastreáveis |
| Superfícies | Obrigatório | Mapear experiências consumidoras |
| Permissões | Obrigatório | Aplicar finalidade, papel e contexto |
| Observabilidade | Obrigatório | Permitir operação e auditoria |
| Estratégia de testes | Obrigatório | Verificar contratos e guardrails |
| Riscos | Obrigatório | Registrar falhas e impactos |
| Critérios de prontidão | Obrigatório | Autorizar avanço técnico |

## 6005.2 Estados da UIC

Uma UIC poderá estar em:

- `Not initiated`;
- `Normative sources mapped`;
- `Domain model proposed`;
- `Contracts proposed`;
- `Security and privacy reviewed`;
- `Test strategy defined`;
- `Technically ready for implementation`;
- `Implementation in progress`;
- `Implemented`;
- `Validated in controlled environment`;
- `Production ready`;
- `Operationally validated`;
- `Blocked`;
- `Reopened`.

Nenhum estado técnico altera o estado funcional da capacidade.

# 6006. Contextos técnicos candidatos

| Contexto | Responsabilidade técnica | Não poderá |
|---|---|---|
| Journey Experience | Superfícies, composição e interação | Decidir autoridade funcional |
| Journey Domain | Regras, agregados e invariantes | Absorver decisões de outras capacidades |
| Journey Orchestration | Coordenar processos e sagas | Criar pipeline humano obrigatório |
| Intelligence | Classificar, estimar, explicar e propor | Confirmar fatos ou decisões sem autoridade |
| Platform | Infraestrutura transversal | Redefinir significado funcional |
| Identity and Authorization | Identidade, papéis, finalidades e políticas | Presumir consentimento |
| Event Infrastructure | Transporte, entrega, ordenação e replay | Converter evento técnico em fato humano |
| Search | Indexação, consulta e recuperação | Tornar índice fonte primária de verdade |
| Knowledge Graph | Relações, proveniência e navegação | Criar perfil determinístico |
| Notifications | Entrega multicanal | Decidir oportunidade de intervenção |
| Audit and Compliance | Evidências, trilhas e retenção | Expor conteúdo além da finalidade |
| Service Integration | Integração com Mall, Travel, Business, Media e Ads | Transferir relevância ou decisão humana |

Esses contextos são candidatos arquiteturais. Não representam decisão automática de implantação ou microsserviço.

# 6007. Modelo de autoridade e ownership

Cada ativo técnico deverá declarar:

- `functional_owner`;
- `system_of_record`;
- `authorized_producers`;
- `authorized_consumers`;
- `purpose`;
- `subject`;
- `sensitivity`;
- `source_authority`;
- `provenance`;
- `valid_from`;
- `valid_until`;
- `retention_policy`;
- `correction_policy`;
- `revocation_policy`;
- `audit_policy`.

## 6007.1 Regras de ownership

1. Ownership técnico não equivale a autoridade funcional.
2. O sistema de registro preserva fatos reconhecidos, não interpretações universais.
3. Uma projeção não poderá se tornar fonte primária por conveniência operacional.
4. Caches, índices e modelos de IA deverão preservar referência à origem.
5. Consumidores não poderão reutilizar dados para finalidades não autorizadas.
6. Revogação deverá bloquear novos usos e propagar efeitos aplicáveis.
7. Retenção residual deverá ser explícita e auditável.

# 6008. Agregados candidatos por capacidade

| Nº | Capacidade | Agregado funcional de referência | Agregados ou registros técnicos candidatos |
|---:|---|---|---|
| 01 | Captura de Contexto | Registro de Captura de Contexto | CaptureRecord, CaptureSession, CaptureInput, CaptureSynthesis |
| 02 | Contexto Vivo | Contexto Vivo | LivingContext, ContextDimension, ContextStatement, ContextConflict |
| 03 | Objetivos | Objetivo | Goal, GoalDirection, SuccessCriterion, GoalProgressRecord |
| 04 | Eventos de Vida | Evento de Vida | LifeEvent, LifeEventCandidate, ImpactAssessment |
| 05 | Próximos Passos | Próximo Passo | NextStep, Dependency, Blocker, ImmediateOutcome |
| 06 | Oportunidades Ativas | Registro de Oportunidade | OpportunityRecord, EligibilityAssessment, AvailabilityAssessment, ParticipantOpportunityRelation |
| 07 | Intervenções Contextuais | Registro de Intervenção | InterventionCandidate, InterventionDecision, DeliveryAttempt, AttentionWindow |
| 08 | Experiências | Registro de Experiência | ExperienceRecord, ExperienceEpisode, ParticipationRecord, ExperienceOutcome |
| 09 | Evolução Contínua | Trajetória de Evolução | EvolutionTrajectory, EvolutionSegment, Baseline, Observation, Interpretation |

Os nomes técnicos são provisórios. Cada UIC deverá confirmar:

- limite transacional;
- invariantes;
- identidade;
- ciclo de vida;
- eventos publicados;
- consistência necessária;
- estratégia de reconstrução;
- dados sensíveis;
- retenção e revogação.

# 6009. Separação entre comandos, propostas, sinais e eventos

| Natureza | Significado técnico-funcional | Pode alterar estado diretamente |
|---|---|---|
| Comando | Solicitação de alteração | Não, depende de validação |
| Proposta | Possibilidade apresentada | Não |
| Sinal | Indicação incompleta | Não |
| Entrada | Material recebido | Não |
| Observação | Registro de algo percebido | Não necessariamente |
| Interpretação | Leitura atribuída | Não necessariamente |
| Evidência | Elemento de sustentação | Não necessariamente |
| Evento funcional | Fato reconhecido e persistido | Sim, conforme contrato |
| Evento de integração | Publicação governada para consumidores | Não amplia o fato original |
| Evento técnico | Ocorrência operacional | Não representa fato humano |

## 6009.1 Envelope mínimo de evento funcional

Todo evento funcional deverá incluir, conforme aplicável:

- `event_id`;
- `event_type`;
- `event_version`;
- `aggregate_id`;
- `aggregate_version`;
- `participant_id`;
- `actor_id`;
- `authority`;
- `purpose`;
- `occurred_at`;
- `recognized_at`;
- `recorded_at`;
- `source`;
- `provenance`;
- `correlation_id`;
- `causation_id`;
- `idempotency_key`;
- `sensitivity`;
- `permissions`;
- `confidence`;
- `uncertainty`;
- `retention`;
- `revocation_reference`.

Nem todos os campos serão expostos a todos os consumidores.

# 6010. Persistência e arquitetura de dados

A arquitetura de dados deverá avaliar, por necessidade:

- armazenamento transacional;
- armazenamento documental;
- event store;
- read models;
- índices de busca;
- grafo de conhecimento;
- armazenamento de mídias;
- histórico imutável;
- projeções temporais;
- dados temporários;
- segredos e chaves;
- dados sensíveis;
- retenção e eliminação.

## 6010.1 Regras de persistência

1. A tecnologia deverá ser escolhida após comparação explícita.
2. O histórico não poderá ser sobrescrito silenciosamente.
3. Correções funcionais deverão produzir registros compensatórios quando exigido pelos contratos.
4. Projeções deverão ser reconstruíveis ou reconciliáveis.
5. Dados temporários deverão possuir expiração definida.
6. Dados sensíveis deverão utilizar proteção proporcional.
7. Busca e grafo não poderão manter dados revogados além da retenção autorizada.
8. Backups e réplicas deverão participar da política de retenção e revogação.

# 6011. APIs e integrações

A tradução técnica deverá definir padrões para:

- APIs síncronas;
- eventos assíncronos;
- webhooks;
- importação e exportação;
- sincronização;
- dispositivos e sensores;
- organizações;
- produtos Guivos;
- fontes externas;
- prevenção de ciclos funcionais.

## 6011.1 Contrato mínimo de integração

Cada integração deverá declarar:

- produtor;
- consumidor;
- finalidade;
- autoridade;
- dados permitidos;
- dados proibidos;
- sensibilidade;
- proveniência;
- temporalidade;
- qualidade e confiança;
- idempotência;
- sincronização;
- retenção;
- revogação;
- falha segura;
- observabilidade;
- responsabilidade por decisão própria.

# 6012. Superfícies e canais

As superfícies técnicas poderão incluir:

- aplicativo móvel;
- web;
- interfaces conversacionais;
- voz;
- notificações;
- dashboards;
- interfaces administrativas;
- integrações externas;
- dispositivos conectados.

Toda superfície deverá:

- indicar finalidade;
- apresentar autoridade e origem quando relevante;
- preservar confirmação explícita;
- diferenciar fato, interpretação, proposta e recomendação;
- oferecer correção, contestação, limitação e revogação quando aplicável;
- manter acessibilidade;
- proteger conteúdo sensível em dispositivos compartilhados;
- falhar com segurança.

# 6013. Identidade, autorização, segurança e privacidade

A arquitetura deverá representar:

- participante;
- ator;
- pessoa;
- organização;
- coletivo;
- papel;
- representação;
- delegação;
- finalidade;
- consentimento quando aplicável;
- autorização contextual;
- revogação;
- acesso emergencial;
- proteção de menores;
- dispositivos compartilhados;
- auditoria.

## 6013.1 Requisitos obrigatórios

1. Autenticação não equivale a autorização.
2. Papel não equivale a identidade.
3. Relação contratual não amplia finalidade.
4. Consentimento não deverá ser presumido por uso geral da plataforma.
5. Autorizações deverão ser minimizadas por finalidade e contexto.
6. Acesso a dados sensíveis deverá ser proporcional e auditável.
7. Revogações deverão ser propagadas aos consumidores.
8. Logs não poderão duplicar conteúdo sensível desnecessariamente.
9. Ambientes de teste deverão utilizar dados protegidos ou sintéticos.
10. A arquitetura deverá suportar correção, exportação, limitação e eliminação conforme aplicável.

# 6014. Guivos Intelligence e IA

Guivos Intelligence poderá:

- classificar;
- comparar;
- estimar;
- detectar padrões;
- explicar;
- sintetizar;
- propor;
- priorizar tecnicamente dentro de critérios autorizados;
- solicitar reavaliação funcional.

Guivos Intelligence não poderá:

- declarar identidade definitiva;
- diagnosticar sem autoridade formal e finalidade legítima;
- confirmar objetivo pelo participante;
- reconhecer Evento de Vida sem contrato aplicável;
- criar compromisso;
- contratar oportunidade;
- confirmar experiência vivida;
- reconhecer evolução humana de forma automática e determinística;
- ampliar finalidade por conveniência;
- produzir score de valor humano.

Toda saída de IA deverá preservar:

- modelo ou processo responsável;
- versão;
- entradas autorizadas;
- finalidade;
- proveniência;
- confiança;
- incerteza;
- explicação aplicável;
- possibilidade de contestação;
- decisão humana ou funcional subsequente.

# 6015. Observabilidade e operação

Cada UIC deverá definir:

- logs estruturados;
- métricas técnicas;
- traces distribuídos;
- eventos de auditoria;
- indicadores de disponibilidade;
- indicadores de integridade;
- detecção de duplicidade;
- detecção de eventos fora de ordem;
- monitoramento de concorrência;
- monitoramento de reconstrução;
- propagação de correções;
- propagação de revogações;
- violações de guardrails;
- filas mortas e reconciliação;
- alertas e runbooks.

Observabilidade deverá avaliar o sistema. Não poderá medir valor humano ou transformar comportamento do participante em julgamento moral.

# 6016. Estratégia de testes

| Categoria | Objetivo mínimo |
|---|---|
| Unitário | Verificar regras locais e invariantes |
| Contrato | Verificar schemas e compatibilidade |
| Integração | Verificar fronteiras e finalidades |
| Autorização | Verificar papéis, finalidade e contexto |
| Eventos | Verificar versão, ordem, correlação e causalidade |
| Idempotência | Impedir duplicidade material |
| Concorrência | Impedir sobrescrita silenciosa |
| Reconstrução | Reproduzir estado a partir de fontes válidas |
| Correção | Preservar histórico e efeitos compensatórios |
| Revogação | Bloquear novos usos e propagar efeitos |
| Privacidade | Verificar minimização e exposição |
| Segurança | Verificar ameaças e abuso |
| Acessibilidade | Verificar acesso sem exposição adicional |
| Falha segura | Verificar comportamento diante de indisponibilidade ou incerteza |
| Cenário normativo | Reproduzir cenários dos contratos finais |

Nenhuma UIC poderá ser considerada tecnicamente pronta sem testes dos guardrails de tolerância zero aplicáveis.

# 6017. Dependências e ondas de implementação

| Onda | Escopo | Resultado esperado |
|---:|---|---|
| 0 | Foundation técnica, identidade, autorização, eventos, auditoria e padrões | Capacidades transversais mínimas disponíveis |
| 1 | Captura de Contexto e Contexto Vivo | Compreensão inicial e representação contextual governadas |
| 2 | Objetivos, Eventos de Vida e Próximos Passos | Direções, mudanças e movimentos governados |
| 3 | Oportunidades Ativas e Intervenções Contextuais | Meios e manifestações governados |
| 4 | Experiências e Evolução Contínua | Vivências e trajetórias governadas |
| 5 | Integrações transversais, Intelligence e otimizações | Ecossistema coordenado com explicabilidade |
| 6 | Escala, resiliência e evolução arquitetural | Operação global, resiliente e evolutiva |

A ordem é uma recomendação técnica baseada em dependências. Não representa sequência obrigatória da jornada humana.

# 6018. Matriz inicial de dependências

| Capacidade | Dependências técnicas mínimas | Pode iniciar parcialmente sem |
|---|---|---|
| Captura de Contexto | Identidade, sessão, armazenamento temporário, auditoria | Contexto Vivo completo |
| Contexto Vivo | Identidade, eventos, proveniência, autorização | Objetivos e Eventos de Vida |
| Objetivos | Contexto mínimo autorizado, eventos, histórico | Oportunidades Ativas |
| Eventos de Vida | Contexto mínimo, temporalidade, evidências | Próximos Passos |
| Próximos Passos | Objetivos ou contexto, dependências, eventos | Oportunidades Ativas |
| Oportunidades Ativas | Catálogos, fontes, elegibilidade, risco | Intervenções Contextuais completas |
| Intervenções Contextuais | Canais, atenção, preferências, silêncio | Experiências completas |
| Experiências | Temporalidade, participação, resultados, mídias | Evolução Contínua completa |
| Evolução Contínua | Baselines, evidências, interpretações, histórico | Automação de IA avançada |

# 6019. Artefatos técnicos derivados autorizáveis

Após aprofundamento deste Handoff poderão ser criados:

- Technical Architecture Specification;
- Domain Model;
- Capability Implementation Specifications;
- Event Catalog;
- API Catalog;
- Data Architecture;
- Knowledge Graph Architecture;
- Identity and Authorization Architecture;
- Security and Privacy Architecture;
- Integration Architecture;
- Observability Model;
- Testing Strategy;
- Deployment Architecture;
- Implementation Backlog;
- ADRs de tecnologia;
- protótipos técnicos.

Nenhum artefato derivado poderá alterar silenciosamente as autoridades funcionais.

# 6020. Critérios técnicos de prontidão do Handoff

O Handoff poderá atingir `1.0.0` quando:

1. as nove UICs estiverem definidas;
2. as fontes normativas estiverem rastreadas;
3. autoridades e decisões proibidas estiverem explícitas;
4. agregados e ownership estiverem definidos;
5. comandos, propostas, sinais e eventos estiverem mapeados;
6. estados e transições estiverem tecnicamente representados;
7. integrações estiverem delimitadas;
8. persistência, busca e grafo estiverem avaliados;
9. identidade, autorização, privacidade e segurança estiverem incorporadas;
10. observabilidade estiver definida;
11. estratégias de teste estiverem estabelecidas;
12. dependências estiverem ordenadas;
13. lacunas estiverem classificadas;
14. guardrails críticos estiverem verificáveis;
15. não houver conflito funcional bloqueante.

# 6021. Critérios de reabertura

O Handoff deverá ser reaberto quando:

- um agregado não preservar invariantes funcionais;
- uma integração transferir decisão;
- uma tecnologia impedir correção ou revogação exigida;
- um modelo de dados produzir perfil paralelo;
- uma topologia criar pipeline humano obrigatório;
- um evento técnico for utilizado como fato humano;
- uma decisão de IA ultrapassar sua autoridade;
- um guardrail não puder ser testado;
- houver conflito entre implementação e contrato final;
- uma dependência tornar inviável a operação segura.

# 6022. Lacunas abertas da versão 0.1.0

| ID | Lacuna | Classificação | Próxima ação |
|---|---|---|---|
| EH-GAP-001 | Confirmar limites dos agregados por capacidade | Domain design | Elaborar UICs |
| EH-GAP-002 | Definir catálogo técnico de eventos | Event architecture | Criar inventário derivado |
| EH-GAP-003 | Definir critérios comparativos de persistência | Data architecture | Elaborar matriz de decisão |
| EH-GAP-004 | Definir modelo técnico de autorização contextual | Security architecture | Derivar especificação |
| EH-GAP-005 | Definir estratégia de propagação de revogação | Integration architecture | Elaborar protocolo |
| EH-GAP-006 | Definir modelo de observabilidade de guardrails | Operations | Elaborar catálogo de sinais |
| EH-GAP-007 | Definir estrutura do backlog por onda | Product Engineering | Criar backlog rastreável |
| EH-GAP-008 | Definir critérios de prototipação técnica | Engineering governance | Elaborar política |
| EH-GAP-009 | Definir critérios de seleção tecnológica | ADR governance | Elaborar matriz de ADRs |

# 6023. Estado inicial das capacidades no Handoff

| Nº | Capacidade | Estado funcional | Estado técnico inicial |
|---:|---|---|---|
| 01 | Captura de Contexto | Functionally complete | Normative sources mapped |
| 02 | Contexto Vivo | Functionally complete | Normative sources mapped |
| 03 | Objetivos | Functionally complete | Normative sources mapped |
| 04 | Eventos de Vida | Functionally complete | Normative sources mapped |
| 05 | Próximos Passos | Functionally complete | Normative sources mapped |
| 06 | Oportunidades Ativas | Functionally complete | Normative sources mapped |
| 07 | Intervenções Contextuais | Functionally complete | Normative sources mapped |
| 08 | Experiências | Functionally complete | Normative sources mapped |
| 09 | Evolução Contínua | Functionally complete | Normative sources mapped |

# 6024. Próximo incremento

O próximo incremento deverá criar a estrutura detalhada da `UIC-01 — Captura de Contexto`, incluindo:

- agregados e invariantes;
- comandos, propostas e eventos;
- estados e transições;
- interfaces produtoras e consumidoras;
- persistência temporária e confirmada;
- autorização e finalidade;
- observabilidade;
- testes;
- critérios de prontidão;
- dependências da Onda 0.

A criação da UIC-01 não autoriza implementação em produção e não reduz a necessidade de especificações técnicas derivadas.