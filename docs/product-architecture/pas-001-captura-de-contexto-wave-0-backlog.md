---
id: PAS-001-CC-W0-BACKLOG-001
title: Backlog Executável da Onda 0 da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-W0-PLAN-001
related:
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-LIFECYCLE-001
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-READINESS-001
---

# PAS-001-CC-W0-BACKLOG-001 — Backlog Executável da Onda 0

> O backlog descreve comportamento, evidência e critérios de aceite. Ele não transforma cada capacidade em microsserviço nem determina tecnologia física.

## 1. Modelo de item

Cada história deverá possuir:

- `story_id`;
- incremento e épico;
- objetivo verificável;
- autoridade normativa;
- comportamento esperado;
- critérios de aceite;
- guardrails;
- contratos e dados afetados;
- dependências;
- testes;
- evidências;
- SLI quando aplicável;
- riscos;
- owner;
- prioridade;
- Definition of Done.

## 2. Priorização

- `P0`: bloqueia fluxo principal, gate ou segurança;
- `P1`: necessário para completar a Onda 0;
- `P2`: melhora robustez sem bloquear o núcleo;
- `Deferred`: explicitamente fora da Onda 0.

## 3. W0-01 — Fundação

| ID | História | Prioridade | Critério principal | Evidência |
|---|---|---:|---|---|
| W0-01-ST-001 | estabelecer estrutura de implementação e módulos lógicos | P0 | estrutura não implica microsserviços e respeita limites do domínio | EV-018 |
| W0-01-ST-002 | definir convenções de branch, commit, versionamento e release | P0 | cada alteração é rastreável a requisito e evidência | EV-018 |
| W0-01-ST-003 | configurar pipeline mínimo de testes e validação de schemas | P0 | falha de contrato bloqueia integração | EV-003 |
| W0-01-ST-004 | definir matriz inicial de owners e aprovadores | P0 | cada gate e risco crítico possui responsável | EV-017 |
| W0-01-ST-005 | criar template versionado de evidência | P0 | template contém todos os campos de validade | EV-017 |
| W0-01-ST-006 | criar registro de riscos, exceções e interrupções | P0 | exceção possui expiração, mitigação e aprovador | EV-017 |
| W0-01-ST-007 | definir política de dados sintéticos | P0 | nenhum dado pessoal real é necessário no desenvolvimento | EV-004 |
| W0-01-ST-008 | inventariar segredos e credenciais por ambiente | P1 | nenhum segredo aparece em código, payload ou log | EV-005 |
| W0-01-ST-009 | validar prontidão das dependências `required_before_build` | P0 | cada dependência possui owner, contrato, fallback e evidência de disponibilidade | EV-017 |

## 4. W0-02 — Núcleo de domínio

| ID | História | Prioridade | Critério principal | Evidência |
|---|---|---:|---|---|
| W0-02-ST-001 | criar `CaptureRecord` com identidade opaca e versão | P0 | agregado rejeita identidade incompatível e versão inválida | EV-001 |
| W0-02-ST-002 | criar `CaptureSession` como entidade temporal interna | P0 | sessão não se torna agregado independente por conveniência | EV-001 |
| W0-02-ST-003 | modelar autoria e representação | P0 | representação expirada não produz efeito | EV-001 |
| W0-02-ST-004 | modelar natureza da informação | P0 | hipótese, interpretação e fato confirmado não se confundem | EV-001 |
| W0-02-ST-005 | implementar transições completas do ciclo | P0 | todas as transições válidas e inválidas possuem teste | EV-002 |
| W0-02-ST-006 | implementar confirmação, rejeição e contestação | P0 | somente autoridade humana competente confirma | EV-001 |
| W0-02-ST-007 | implementar autorização por finalidade e escopo | P0 | autorização ausente, expirada ou incompatível falha com segurança | EV-001 |
| W0-02-ST-008 | implementar correção compensatória | P0 | histórico permanece e estado atual é calculado corretamente | EV-007 |
| W0-02-ST-009 | implementar revogação no domínio | P0 | novos usos ficam bloqueados no escopo revogado | EV-006 |
| W0-02-ST-010 | implementar reconstrução pura | P0 | replay não publica novo fato humano | EV-002 |
| W0-02-ST-011 | implementar catálogo estável de erros | P1 | erros possuem código, retry e significado estáveis | EV-003 |
| W0-02-ST-012 | medir cobertura por invariante e transição | P1 | relatório lista regra, teste e resultado | EV-001/002 |

## 5. W0-03 — Contratos e persistência

| ID | História | Prioridade | Critério principal | Evidência |
|---|---|---:|---|---|
| W0-03-ST-001 | implementar envelope comum de comandos | P0 | autoridade não é ampliada pelo payload | EV-003 |
| W0-03-ST-002 | implementar respostas e erros versionados | P0 | consumidor diferencia rejeição, conflito e retry | EV-003 |
| W0-03-ST-003 | implementar eventos funcionais separados de eventos técnicos | P0 | evento técnico nunca vira fato funcional | EV-003 |
| W0-03-ST-004 | validar schemas e fixtures válidas/inválidas | P0 | incompatibilidade é rejeitada ou isolada | EV-003/015 |
| W0-03-ST-005 | persistir agregado transacionalmente | P0 | estado e versão são atômicos | EV-007 |
| W0-03-ST-006 | aplicar concorrência otimista | P0 | versão divergente não sobrescreve estado atual | EV-007 |
| W0-03-ST-007 | implementar registro de idempotência | P0 | mesma chave e mesmo payload retornam resultado anterior | EV-003 |
| W0-03-ST-008 | rejeitar chave idempotente com payload material diferente | P0 | conflito não gera novo efeito | EV-003 |
| W0-03-ST-009 | publicar eventos após persistência confiável | P0 | falha de publicação é recuperável sem duplicidade material | EV-003 |
| W0-03-ST-010 | implementar quarentena de mensagem incompatível | P1 | mensagem não altera estado e permanece rastreável | EV-015 |
| W0-03-ST-011 | construir matriz produtor/consumidor | P1 | cada versão suportada é explícita | EV-015 |
| W0-03-ST-012 | implementar snapshot lógico opcional | P2 | snapshot preserva integridade e não inclui conteúdo excluído | EV-008 |

## 6. W0-04 — Dados protegidos

| ID | História | Prioridade | Critério principal | Evidência |
|---|---|---:|---|---|
| W0-04-ST-001 | separar registro funcional e conteúdo protegido | P0 | registro não contém mídia ou texto sensível proibido | EV-016 |
| W0-04-ST-002 | implementar referências opacas e temporárias | P0 | referência não permite enumeração nem acesso sem política | EV-004/009 |
| W0-04-ST-003 | registrar hash, tamanho, tipo e proveniência | P0 | integridade pode ser verificada sem expor conteúdo | EV-009 |
| W0-04-ST-004 | aplicar classificação de sensibilidade | P0 | classe governa canal, log, retenção e índice | EV-016 |
| W0-04-ST-005 | implementar retenção e expiração por classe | P0 | descarte é comprovável e não converte temporário em persistente | EV-016 |
| W0-04-ST-006 | implementar exclusão por camada | P0 | índice, cache, storage e derivados possuem ação explícita | EV-016 |
| W0-04-ST-007 | implementar quarentena de mídia não confiável | P0 | conteúdo não processado não alcança consumidores | EV-009 |
| W0-04-ST-008 | testar backup e restore com tombstones | P0 | restore não reativa conteúdo revogado ou excluído | EV-008 |
| W0-04-ST-009 | testar rotação e invalidação de chave | P1 | conteúdo permanece protegido e exclusão criptográfica é demonstrável | EV-008/016 |
| W0-04-ST-010 | registrar derivados vinculados à fonte | P1 | derivado órfão é detectado e tratado | EV-016 |

## 7. W0-05 — Acesso, correção e revogação

| ID | História | Prioridade | Critério principal | Evidência |
|---|---|---:|---|---|
| W0-05-ST-001 | avaliar ator, participante, finalidade, escopo e validade | P0 | acesso técnico isolado não concede autoridade | EV-004 |
| W0-05-ST-002 | aplicar menor privilégio por operação | P0 | resposta contém somente dados necessários | EV-004 |
| W0-05-ST-003 | tratar representação, menores e terceiros | P0 | modo de representação é explícito e verificável | EV-004 |
| W0-05-ST-004 | registrar consumidores e seus compromissos | P0 | consumidor declara finalidade, retenção, correção e revogação | EV-014 |
| W0-05-ST-005 | coordenar correção com consumidores afetados | P0 | entrega não equivale a aplicação confirmada | EV-014 |
| W0-05-ST-006 | coordenar revogação com bloqueio central | P0 | novos usos bloqueados antes da conclusão distribuída | EV-006 |
| W0-05-ST-007 | acompanhar confirmações e retenções residuais | P0 | residual possui fundamento, escopo e validade | EV-006 |
| W0-05-ST-008 | implementar kill switch de consumidor | P0 | consumidor comprometido deixa de receber novos recortes | EV-014 |
| W0-05-ST-009 | implementar acesso administrativo JIT e auditado | P0 | administrador não confirma nem autoriza em nome da pessoa | EV-012 |
| W0-05-ST-010 | testar dispositivo compartilhado e sessão abandonada | P1 | conteúdo não permanece exposto ao próximo usuário | EV-004 |

## 8. W0-06 — Busca protegida

| ID | História | Prioridade | Critério principal | Evidência |
|---|---|---:|---|---|
| W0-06-ST-001 | implementar política `prohibited` | P0 | conteúdo proibido não produz índice nem embedding | EV-010 |
| W0-06-ST-002 | implementar `metadata_only` | P0 | índice contém apenas metadados autorizados | EV-010 |
| W0-06-ST-003 | implementar índice privado do participante | P0 | consulta não cruza participantes | EV-010 |
| W0-06-ST-004 | aplicar escopo antes da recuperação | P0 | pós-filtro não é proteção suficiente | EV-010 |
| W0-06-ST-005 | redigir snippets por política | P0 | trecho não expõe conteúdo além da finalidade | EV-010 |
| W0-06-ST-006 | remover resultado após revogação | P0 | bloqueio central respeita SLO candidato | EV-006/010 |
| W0-06-ST-007 | atualizar resultado após correção | P0 | estado anterior não aparece como atual | EV-007/010 |
| W0-06-ST-008 | reconstruir índice a partir do registro | P1 | índice não se torna sistema de registro | EV-010 |
| W0-06-ST-009 | avaliar busca vetorial em POC isolada | P2 | embedding é revogável e preserva natureza da informação | EV-010 |

## 9. W0-07 — Segurança, observabilidade e resiliência

| ID | História | Prioridade | Critério principal | Evidência |
|---|---|---:|---|---|
| W0-07-ST-001 | instrumentar SLIs por fluxo crítico | P0 | latência, backlog, erro e propagação são mensuráveis | EV-013 |
| W0-07-ST-002 | implementar logs redigidos e correlação opaca | P0 | zero conteúdo sensível bruto em logs | EV-005 |
| W0-07-ST-003 | testar enumeração e vazamento cruzado | P0 | zero acesso entre participantes | EV-004 |
| W0-07-ST-004 | testar replay, falsificação e downgrade | P0 | evento inválido não altera estado | EV-003/015 |
| W0-07-ST-005 | testar prompt injection textual e multimodal | P0 | conteúdo não concede autoridade nem altera instruções de sistema | EV-011 |
| W0-07-ST-006 | testar consumidor comprometido | P0 | suspensão e kill switch impedem novos efeitos | EV-014 |
| W0-07-ST-007 | testar dependência indisponível e retries | P0 | falha degrada com segurança e sem duplicidade material | EV-013 |
| W0-07-ST-008 | executar carga de referência | P0 | relatório mede p50/p95/p99 e orçamento de erro | EV-013 |
| W0-07-ST-009 | executar restore e replay de desastre | P0 | RPO/RTO são medidos e revogações persistem | EV-008/013 |
| W0-07-ST-010 | criar runbooks C0/C1 | P1 | resposta possui owner, gatilho e comunicação | EV-013/017 |

## 10. W0-08 — Fechamento

| ID | História | Prioridade | Critério principal | Evidência |
|---|---|---:|---|---|
| W0-08-ST-001 | consolidar pacote EV-001 a EV-018 | P0 | cada evidência é reproduzível e versionada | todas |
| W0-08-ST-002 | executar gate de domínio | P0 | todos os itens obrigatórios estão passed ou accepted_exception | relatório do gate |
| W0-08-ST-003 | executar gate de dados | P0 | retenção, exclusão, restore e índice estão comprovados | relatório do gate |
| W0-08-ST-004 | executar gate de segurança | P0 | nenhum bloqueio crítico permanece | relatório do gate |
| W0-08-ST-005 | executar gate de qualidade | P0 | SLIs e SLOs candidatos foram medidos | relatório do gate |
| W0-08-ST-006 | executar gate de governança | P0 | ADRs, riscos, owners e exceções estão válidos | relatório do gate |
| W0-08-ST-007 | registrar decisão de conclusão | P0 | decisão é separada e não autoriza produção | EV-018 |
| W0-08-ST-008 | propor próxima onda | P1 | escopo deriva das evidências, não de expansão automática | EV-017/018 |

## 11. Definition of Done de história

Uma história somente está concluída quando:

- comportamento esperado foi demonstrado;
- critérios de aceite foram executados;
- testes estão versionados;
- evidência vinculada existe;
- risco novo foi registrado;
- logs respeitam minimização;
- documentação e contrato estão coerentes;
- owner aprovou o resultado;
- nenhum escopo não autorizado foi introduzido.

## 12. Itens explicitamente deferred

- busca semântica ampla;
- recomendação automatizada completa;
- todos os tipos de mídia;
- todos os consumidores Guivos;
- operação multi-região de produção;
- otimização de custos de escala global;
- certificação externa;
- lançamento público;
- migração de dados reais em massa.