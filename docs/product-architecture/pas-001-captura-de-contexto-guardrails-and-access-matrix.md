---
id: PAS-001-CC-UIC-GUARDRAILS-ACCESS-001
title: Guardrails Técnicos e Matriz de Acesso da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-UIC-001
related:
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-LIFECYCLE-001
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-SCHEMAS-001
  - PAS-001-CC-UIC-STORAGE-INDEX-001
---

# PAS-001-CC-UIC-GUARDRAILS-ACCESS-001 — Guardrails Técnicos e Matriz de Acesso

> **Estado:** `Draft 0.1.0 — Guardrails and access controls technically defined`.
>
> Este documento resolve logicamente `UIC01-GAP-010` ao transformar guardrails funcionais em pontos de aplicação, falhas seguras, evidências e testes verificáveis.

## 1. Princípio central

> **Acesso técnico não equivale a autoridade funcional.**

Um ator pode possuir acesso operacional a um recurso e ainda assim não possuir autoridade para confirmar, autorizar, interpretar, propagar, corrigir, revogar ou transformar aquele recurso.

## 2. Modelo de decisão de acesso

Toda decisão material deverá avaliar conjuntamente:

1. identidade e nível de garantia;
2. papel do ator;
3. autoridade funcional declarada;
4. finalidade vigente;
5. operação solicitada;
6. participante e contexto de representação;
7. natureza e sensibilidade da informação;
8. estado do ciclo de vida;
9. restrições de terceiros, menores ou dispositivo compartilhado;
10. canal e contexto de apresentação;
11. política de retenção e revogação;
12. decisão do consumidor competente.

A ausência de qualquer elemento obrigatório resulta em negação segura.

## 3. Pontos de aplicação

| Ponto | Responsabilidade |
|---|---|
| Entrada/edge | autenticação, rate limit, integridade de transporte e contexto mínimo |
| Command handler | autoridade, finalidade, idempotência e versão esperada |
| Agregado de domínio | invariantes, transições e autoria funcional |
| Política de conteúdo | sensibilidade, retenção, mídia, indexação e apresentação |
| Publicação de evento | persistência suficiente, causalidade e schema |
| Consumidor | decisão própria, minimização e uso compatível |
| Busca | escopo pré-recuperação, redaction e política de índice |
| Projeção/cache | validade, revogação e expiração |
| Administração | separação de deveres, justificativa e auditoria |
| Observabilidade | telemetria sem conteúdo proibido |

Guardrail crítico não poderá depender de um único ponto quando uma falha produzir exposição material.

## 4. Matriz técnica de guardrails

| ID | Guardrail | Risco controlado | Ponto primário | Regra técnica | Falha segura | Evidência |
|---|---|---|---|---|---|---|
| GR-001 | Intelligence não confirma fatos humanos | inferência tratada como confirmação | comando + domínio | ator `intelligence` não recebe autoridade `confirm` | rejeitar sem alterar agregado | erro estável + teste |
| GR-002 | Interpretação não é fato | hipótese exibida como verdade | domínio + apresentação | `information_nature` obrigatório e preservado | apresentar rótulo ou ocultar | evento + teste de UI/contrato |
| GR-003 | Finalidade limita uso | reutilização incompatível | política + consumidor | operação deve constar em `allowed_operations` | negar e registrar código | decisão de política |
| GR-004 | Proibição prevalece | conflito entre permissões | política | `prohibited_operations` vence | negar | teste determinístico |
| GR-005 | Minimização por consumidor | excesso de dados | slice builder | somente campos autorizados | retornar recorte menor ou negar | manifesto de slice |
| GR-006 | Recorte não vira Contexto Vivo automaticamente | incorporação sem decisão | consumidor Contexto Vivo | resposta própria obrigatória | manter como recebido, não incorporado | consumer response |
| GR-007 | Comando não é fato | intenção confundida com ocorrência | domínio | fato somente após transição aceita | nenhuma publicação material | teste de rejeição |
| GR-008 | Evento técnico não é funcional | telemetria tratada como domínio | publicação | envelopes e canais separados | isolar mensagem | schema + contrato |
| GR-009 | Entrega não é efeito | ack de transporte tratado como aplicação | consumidor | confirmação funcional separada | manter pendente | consumer confirmation |
| GR-010 | Correção é compensatória | sobrescrita de história | domínio + projeções | nova versão/evento causal | preservar original e marcar superseded | replay test |
| GR-011 | Revogação bloqueia novos usos | continuidade de acesso | policy enforcement | deny imediato antes da conclusão distribuída | negar | métrica de propagação |
| GR-012 | Replay não cria manifestação | duplicação semântica | reconstrução | modo replay não publica novo fato humano | rejeitar publicação nova | teste de replay |
| GR-013 | ID é opaco | enumeração e inferência | geração + APIs | sem significado e sem sequência previsível | negar identificador inválido | teste de enumeração |
| GR-014 | Logs não contêm conteúdo bruto | vazamento operacional | observabilidade | redaction por schema/política | descartar campo | teste de logs |
| GR-015 | Menores exigem proteção reforçada | tratamento inadequado | política | flag + finalidade + autoridade reforçadas | negar | decisão e auditoria |
| GR-016 | Terceiros exigem proveniência | uso sem base | ingestão + política | `third_party_data` e origem obrigatórios | quarentena | teste de ingestão |
| GR-017 | Representação é limitada | abuso de representante | autenticação + política | `representation_id`, escopo e validade | negar | trilha de representação |
| GR-018 | Dispositivo compartilhado reduz exposição | revelação local | apresentação | modo protegido, reautenticação e redaction | ocultar conteúdo | teste de sessão |
| GR-019 | Busca não amplia autoridade | recuperação indevida | query planner | autorização antes da recuperação | zero resultado | teste de isolamento |
| GR-020 | Índice não é sistema de registro | divergência tratada como verdade | busca | resposta referencia fonte funcional | marcar indisponível | teste de fonte ausente |
| GR-021 | Derivado exige fonte | conteúdo órfão | ingestão de derivados | `source_reference` obrigatório | quarentena | inventário de órfãos |
| GR-022 | Administração não substitui participante | confirmação administrativa indevida | console/admin | ações funcionais proibidas salvo contrato específico | negar | trilha de auditoria |
| GR-023 | Suporte vê mínimo necessário | exposição por atendimento | acesso administrativo | visão redigida por caso | ocultar | relatório de acesso |
| GR-024 | Exportação preserva natureza | interpretação exportada como fato | exportador | incluir tipo, fonte, versão e estado | bloquear exportação incompleta | teste de exportação |
| GR-025 | Retenção residual não permite uso | reutilização de backup/resíduo | storage/policy | estado residual excluído de consultas comuns | negar | teste de restauração |
| GR-026 | Schema não amplia autoridade | campo novo muda poder | validação | campos desconhecidos não alteram decisão | ignorar seguro ou rejeitar | compatibility test |
| GR-027 | Erro não expõe conteúdo | vazamento em mensagens | error mapping | detalhes sensíveis proibidos | erro genérico rastreável | teste de erro |
| GR-028 | Consumidor comprometido é isolável | propagação de exposição | integração | revoke consumer + stop delivery | suspender entrega | runbook + teste |
| GR-029 | Importação é não confiável | conteúdo malicioso | ingestão | validação, sandbox e classificação | quarentena | scanner evidence |
| GR-030 | Prompt injection não concede autoridade | conteúdo controla agente | orchestration | instruções capturadas são dados, não política | ignorar instrução e sinalizar | teste adversarial |

## 5. Matriz de atores e autoridades

Legenda: `P` permitido sob política; `N` negado; `C` condicionado a contrato/representação; `R` somente leitura minimizada.

| Ator | Capturar | Interpretar | Confirmar | Autorizar | Corrigir | Revogar | Consumir recorte | Administrar |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Participante | P | P | P | P | P | P | P | N |
| Representante | C | C | C | C | C | C | C | N |
| Journey Experience | P | N | N | N | N | N | R | N |
| Journey Domain | P | P | N | N | C | C | P | N |
| Contexto Vivo | N | P | N | N | N | N | P | N |
| Guivos Intelligence | N | P | N | N | N | N | R | N |
| Platform Layer | N | N | N | N | N | N | R técnico | C técnico |
| Suporte | N | N | N | N | N | N | R redigido | C limitado |
| Auditor | N | N | N | N | N | N | R evidencial | N |
| Administrador técnico | N | N | N | N | N | N | R técnico | C segregado |
| Organização/profissional externo | C | C | N | N | N | N | C | N |
| Consumidor autorizado | N | C | N | N | N | N | C | N |

A tabela não concede permissão isoladamente. Cada célula permitida depende de finalidade, sensibilidade, estado e escopo.

## 6. Matriz de estados do ciclo de vida

| Estado | Leitura | Alteração | Propagação | Busca |
|---|---|---|---|---|
| Draft/provisional | participante e fluxo competente | permitida por comando válido | restrita | privada/temporária |
| Submitted | escopo autorizado | somente transições válidas | pendente | metadados limitados |
| Interpreted | preserva natureza | nova interpretação versionada | recorte rotulado | protegida |
| Awaiting confirmation | participante/representante | confirmar ou rejeitar | não como fato confirmado | protegida e rotulada |
| Confirmed | autorizada por finalidade | correção compensatória | conforme consumidor | conforme política |
| Authorized | escopo e prazo explícitos | alteração de autorização | permitido no escopo | purpose_scoped |
| Corrected | estado atual + histórico | novas compensações | propagar correção | índice atualizado |
| Revocation pending | leitura restrita para conclusão | somente processo de revogação | novos usos bloqueados | removido/bloqueado |
| Revoked | evidência mínima permitida | nenhuma operação funcional comum | proibida | proibida |
| Retained residual | administração segregada | política técnica | proibida | proibida |
| Expired | evidência mínima | renovação exige nova autoridade | proibida | removida |

## 7. Representação

Uma representação válida deverá conter:

- `representation_id` opaco;
- participante representado;
- representante;
- autoridade concedida;
- finalidade;
- prazo;
- restrições;
- forma de comprovação;
- possibilidade de revogação;
- nível de garantia;
- trilha de uso.

Não é permitido herdar toda a autoridade do participante por padrão.

## 8. Menores e pessoas vulneráveis

Requisitos mínimos:

1. classificação explícita;
2. política jurisdicional aplicável;
3. representação ou consentimento adequado;
4. conteúdo e apresentação minimizados;
5. proibição de inferências de alto impacto sem autoridade;
6. revisão reforçada de compartilhamento externo;
7. retenção reduzida quando possível;
8. auditoria de acessos administrativos;
9. revogação e exclusão acessíveis;
10. testes específicos.

## 9. Dispositivos compartilhados

- sessões curtas e reautenticação para conteúdo sensível;
- notificações sem conteúdo revelador;
- cache local minimizado e expirável;
- ocultação de histórico sensível;
- saída remota quando suportada;
- identificação de contexto compartilhado;
- proibição de persistência de segredo em cliente;
- comportamento seguro offline.

## 10. Administração e suporte

Ações administrativas materiais exigem:

- justificativa vinculada a caso;
- menor privilégio;
- separação de deveres quando aplicável;
- sessão reforçada;
- expiração de acesso;
- conteúdo redigido por padrão;
- trilha imutável de acesso permitido;
- revisão periódica;
- mecanismo de suspensão imediata;
- proibição de confirmação humana em nome do participante, salvo representação formal.

## 11. Decisão do consumidor

Todo consumidor deverá responder explicitamente:

- aceitou ou rejeitou o recorte;
- finalidade aplicada;
- versão do contrato;
- campos materialmente utilizados;
- retenção própria permitida;
- correção aplicada;
- revogação aplicada;
- erro ou incompatibilidade;
- evidência temporal.

Receber mensagem não equivale a aceitar conteúdo nem incorporá-lo.

## 12. Códigos de negação mínimos

- `CC_AUTHORITY_DENIED`;
- `CC_PURPOSE_DENIED`;
- `CC_PARTICIPANT_SCOPE_DENIED`;
- `CC_REPRESENTATION_INVALID`;
- `CC_SENSITIVITY_POLICY_DENIED`;
- `CC_LIFECYCLE_STATE_DENIED`;
- `CC_REVOKED_USE_DENIED`;
- `CC_MINOR_PROTECTION_REQUIRED`;
- `CC_THIRD_PARTY_PROVENANCE_REQUIRED`;
- `CC_SHARED_DEVICE_PROTECTION_REQUIRED`;
- `CC_SEARCH_SCOPE_DENIED`;
- `CC_ADMIN_ACTION_DENIED`;
- `CC_CONSUMER_CONTRACT_INCOMPATIBLE`.

## 13. Observabilidade permitida

Métricas mínimas:

- decisões permitidas e negadas por código;
- latência da decisão;
- tentativas fora de escopo;
- acessos administrativos;
- consumidores suspensos;
- revogações pendentes;
- correções não confirmadas;
- consultas sem resultado por política;
- conteúdo em quarentena;
- violações de redaction.

Métricas não poderão incluir conteúdo bruto ou atributos que facilitem reidentificação sem necessidade formal.

## 14. Testes obrigatórios

1. Intelligence tentando confirmar;
2. Platform Layer tentando autorizar;
3. representante expirado;
4. finalidade incompatível;
5. proibição prevalecendo sobre permissão;
6. menor sem proteção reforçada;
7. dado de terceiro sem proveniência;
8. dispositivo compartilhado sem modo protegido;
9. consulta entre participantes;
10. revogação bloqueando busca;
11. suporte acessando conteúdo não redigido;
12. administrador tentando alterar fato humano;
13. consumidor sem decisão própria;
14. evento técnico em canal funcional;
15. correção sobrescrevendo histórico;
16. replay publicando manifestação nova;
17. prompt injection tentando alterar política;
18. exportação sem natureza da informação;
19. erro contendo payload sensível;
20. schema desconhecido tentando ampliar autoridade.

## 15. Evidências mínimas

- matriz de papéis implantada;
- políticas versionadas;
- relatório de acessos administrativos;
- catálogo de negações;
- testes de isolamento e representação;
- testes de menores e terceiros;
- prova de redaction;
- relatório de consumidores e contratos;
- teste adversarial de prompt injection;
- runbook de suspensão de consumidor.

## 16. Gap resolvido

`UIC01-GAP-010 — matriz técnica dos guardrails` passa para `Resolved by technical definition`.

## 17. Limites

Este documento não cria novos papéis empresariais, não concede autoridade por tabela, não substitui contratos funcionais e não autoriza acesso de produção. A implementação deverá provar os mecanismos por testes e evidências antes de qualquer declaração operacional de conformidade.