---
id: PAS-001-CC-UIC-NFR-SECURITY-001
title: Requisitos Não Funcionais, SLOs e Threat Model da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-UIC-001
related:
  - PAS-001-CC-UIC-CONTRACTS-001
  - PAS-001-CC-UIC-SCHEMAS-001
  - PAS-001-CC-UIC-STORAGE-INDEX-001
  - PAS-001-CC-UIC-GUARDRAILS-ACCESS-001
---

# PAS-001-CC-UIC-NFR-SECURITY-001 — Requisitos Não Funcionais, SLOs e Threat Model

> **Estado:** `Draft 0.1.0 — NFR, SLO and threat model technically defined`.
>
> Os valores deste documento são metas lógicas iniciais para a Onda 0. Devem ser validados em carga e não autorizam produção sem evidência.

## 1. Objetivo

Definir condições mensuráveis de disponibilidade, desempenho, resiliência, segurança, privacidade, recuperação, observabilidade e operação para que a UIC-01 possa ser considerada tecnicamente pronta para iniciar implementação planejada.

## 2. Classes de criticidade

| Classe | Exemplos | Tratamento |
|---|---|---|
| C0 — proteção imediata | revogação, bloqueio de acesso, suspensão de consumidor | prioridade máxima e falha fechada |
| C1 — integridade funcional | confirmação, autorização, correção, publicação material | consistência e durabilidade reforçadas |
| C2 — captura principal | submissão de entrada, sessão, transcrição | disponibilidade alta com degradação controlada |
| C3 — derivados e experiência | interpretação, busca, recomendações e projeções | podem degradar sem alterar fatos |
| C4 — administração e análise | relatórios, métricas agregadas e manutenção | podem ser adiados, sempre auditados |

## 3. Requisitos não funcionais

### 3.1 Disponibilidade

- operações C0 e C1 deverão possuir caminho operacional independente de componentes não essenciais;
- indisponibilidade da Intelligence não poderá impedir revogação, correção ou acesso a fatos confirmados;
- indisponibilidade da busca não poderá impedir leitura autorizada por referência direta quando aplicável;
- componentes de experiência poderão degradar sem aceitar estados inválidos;
- manutenção deverá preservar bloqueios de revogação.

### 3.2 Consistência

- invariantes do agregado exigem consistência forte no ponto de decisão;
- projeções, índices e consumidores podem ser eventualmente consistentes, desde que o estado de atraso seja observável;
- revogação deverá ser aplicada no enforcement central antes da convergência distribuída;
- correções não podem produzir duas versões simultaneamente atuais;
- conflitos de versão deverão ser rejeitados com erro estável.

### 3.3 Durabilidade

- evento funcional aceito não poderá ser confirmado antes da persistência suficiente definida pela implementação;
- conteúdo protegido e registro funcional deverão possuir integridade correlacionável;
- perda de derivado reconstruível não equivale a perda de fato funcional;
- confirmações de aplicação de correção e revogação deverão ser duráveis;
- snapshots não substituem histórico sem política formal.

### 3.4 Escalabilidade

- participantes e cargas deverão ser isoláveis por partição lógica sem alterar identidade funcional;
- crescimento de mídia não poderá degradar comandos C0;
- consultas e processamento assíncrono deverão possuir limites por consumidor e finalidade;
- backlog deverá ser observável por idade e criticidade;
- escalabilidade não poderá depender de redução de controles de autorização.

### 3.5 Latência

- a aceitação do comando deve separar resposta síncrona de conclusão distribuída;
- operações críticas deverão expor estado pendente quando não concluídas;
- transcrição, interpretação e indexação poderão ser assíncronas;
- a experiência deverá distinguir conteúdo recebido, processado, confirmado e propagado.

### 3.6 Idempotência e concorrência

- todas as operações materiais deverão possuir chave de idempotência ou identidade funcional equivalente;
- repetição não poderá duplicar fato, autorização, correção ou revogação;
- concorrência usa versão esperada ou mecanismo logicamente equivalente;
- conflito não será resolvido por last-write-wins em fatos humanos;
- retries deverão respeitar códigos retryable e limites.

### 3.7 Privacidade e segurança

- menor privilégio e finalidade obrigatória;
- conteúdo sensível ausente de logs comuns;
- segregação entre ambientes e participantes;
- segredos fora de contratos funcionais;
- criptografia em trânsito e repouso;
- acessos administrativos justificados e auditáveis;
- proteção contra enumeração, replay, exfiltração e injeção de instruções;
- revogação e correção testáveis ponta a ponta.

### 3.8 Observabilidade

Cada fluxo material deverá possuir:

- `correlation_id`;
- `causation_id` quando aplicável;
- versão do contrato;
- código de decisão;
- latência por estágio;
- estado de consumidor;
- classificação de erro;
- métricas sem conteúdo proibido;
- alerta baseado em criticidade.

### 3.9 Acessibilidade e localização

- mensagens de estado e erro deverão ser compreensíveis sem expor detalhes sensíveis;
- fluxos de confirmação e revogação devem ser acessíveis;
- conteúdo multimodal deverá prever alternativas quando aplicável;
- datas, idiomas e fusos deverão ser inequívocos;
- tradução não poderá alterar natureza, autoridade ou finalidade.

### 3.10 Interoperabilidade e portabilidade

- contratos lógicos independentes de protocolo físico;
- schemas versionados e testáveis;
- exportação preserva identidade, natureza, fonte, versão e estado;
- migração não poderá reativar conteúdo revogado;
- dependências proprietárias deverão possuir estratégia de saída antes da produção.

## 4. SLOs iniciais da Onda 0

Os valores abaixo são objetivos candidatos. A implementação deverá confirmar ou ajustar por evidência antes de produção.

| SLO | Classe | Meta inicial | Janela | Observação |
|---|---|---:|---|---|
| Disponibilidade de comandos C0/C1 | obrigatória | >= 99,9% | 30 dias | exclui manutenção formal apenas se bloqueios permanecerem ativos |
| Disponibilidade de captura C2 | meta | >= 99,5% | 30 dias | degradação deverá ser explícita |
| Aceitação síncrona p95 de comando sem mídia | meta | <= 800 ms | 15 min | sem contar processamento assíncrono |
| Aceitação síncrona p99 | meta | <= 2 s | 15 min | ambiente nominal |
| Bloqueio central após revogação aceita | obrigatória | <= 5 s p99 | contínua | novos usos bloqueados |
| Propagação de revogação para consumidores críticos | obrigatória | <= 60 s p99 | contínua | consumidor indisponível permanece pendente e alertado |
| Propagação de correção para consumidores críticos | obrigatória | <= 5 min p99 | contínua | estado anterior não apresentado como atual |
| Atualização de projeção principal | meta | <= 30 s p95 | 15 min | atraso observável |
| Atualização de índice protegido | meta | <= 2 min p95 | 15 min | busca pode indicar processamento |
| Detecção de consumidor atrasado C0/C1 | obrigatória | <= 2 min | contínua | gera alerta |
| RPO do registro funcional | obrigatória | <= 1 min | incidente | alvo inicial |
| RTO do registro funcional | obrigatória | <= 60 min | incidente | validado por restore |
| RPO de derivados reconstruíveis | meta | <= 24 h | incidente | sem perda de fatos |
| Reconstrução de agregado individual p95 | meta | <= 10 s | teste | tamanho de referência definido na Onda 0 |
| Erros com conteúdo sensível em logs | obrigatória | 0 | contínua | violação crítica |
| Acesso entre participantes | obrigatória | 0 | contínua | violação crítica |
| Mensagem incompatível processada materialmente | obrigatória | 0 | contínua | quarentena obrigatória |

## 5. Indicadores de erro e orçamento

- cada SLO deverá possuir SLI definido por fonte e consulta;
- erro de medição não poderá ser tratado como sucesso;
- consumo de orçamento de erro C0 deverá suspender mudanças de risco;
- violações C0/C1 exigem incidente e análise causal;
- indisponibilidade causada por negação segura não será automaticamente classificada como falha de segurança;
- relatórios deverão separar indisponibilidade, degradação, rejeição válida e erro interno.

## 6. Degradação controlada

| Dependência indisponível | Comportamento permitido |
|---|---|
| Intelligence | capturar e confirmar sem interpretação automática; enfileirar derivado |
| Busca | acesso direto autorizado; consultas indisponíveis |
| Projeção | mostrar estado de processamento; consultar origem quando seguro |
| Consumidor externo | manter entrega pendente; não declarar efeito |
| Storage de mídia | rejeitar nova mídia ou armazenar temporariamente somente se política permitir |
| Serviço de transcrição | manter original protegido e estado pendente |
| Observabilidade | bloquear operação material quando a perda de trilha tornar a ação não auditável |
| Política de autorização | negar operação material |

## 7. Recuperação e continuidade

A implementação deverá definir e testar:

1. backup do registro funcional;
2. backup ou reconstrução de conteúdo protegido conforme política;
3. restauração com reaplicação de revogações e correções;
4. recuperação de consumidores e reprocessamento idempotente;
5. reconstrução de projeções e índices;
6. rotação emergencial de chaves;
7. suspensão de consumidor comprometido;
8. operação mínima para C0/C1;
9. comunicação de incidente sem exposição de conteúdo;
10. validação pós-recuperação.

## 8. Threat model

### 8.1 Ativos

- identidade e representação;
- conteúdo original;
- fatos confirmados;
- autorizações;
- correções e revogações;
- histórico funcional;
- chaves e segredos;
- índices e embeddings;
- logs e evidências;
- contratos e schemas;
- canais de integração;
- operações administrativas.

### 8.2 Agentes

- usuário externo não autenticado;
- participante malicioso;
- representante abusivo;
- organização ou profissional externo;
- consumidor comprometido;
- operador interno;
- administrador privilegiado;
- fornecedor de tecnologia;
- modelo ou agente induzido por conteúdo;
- atacante com acesso a backup ou logs.

## 9. Catálogo de ameaças

| ID | Ameaça | Vetor | Impacto | Prevenção | Detecção | Resposta | Risco residual |
|---|---|---|---|---|---|---|---|
| TH-001 | enumeração de registros | IDs previsíveis | exposição entre participantes | IDs opacos + autorização | taxa/anomalia | bloquear e investigar | baixo |
| TH-002 | escalada de privilégio | papel ou token indevido | ação funcional não autorizada | menor privilégio + policy | decisão negada/anomalia | revogar sessão | médio |
| TH-003 | finalidade incompatível | reutilização de recorte | violação de privacidade | purpose binding | auditoria de decisão | negar e notificar | médio |
| TH-004 | vazamento em logs | serialização de payload | exposição massiva | redaction por schema | scanners e testes | remover acesso e rotacionar | médio |
| TH-005 | mistura de participantes | consulta ou cache | violação crítica | partition scope antes da busca | canary/teste | suspender componente | baixo |
| TH-006 | alteração de conteúdo | storage ou trânsito | perda de integridade | hash + criptografia | divergência de hash | quarentena e reconstrução | baixo |
| TH-007 | replay de comando | repetição capturada | duplicação de fato | idempotência + nonce lógico | chave repetida | retornar resultado anterior | baixo |
| TH-008 | evento falsificado | produtor não autorizado | estado inválido | identidade do produtor + schema | assinatura/origem inválida | rejeitar e isolar | médio |
| TH-009 | abuso de representação | escopo amplo/expirado | perda de autonomia | contrato limitado e prazo | uso fora do padrão | revogar representação | médio |
| TH-010 | extração por busca | consultas iterativas | reconstrução de perfil | rate limit + minimização | padrão de consulta | suspender consulta | médio |
| TH-011 | reidentificação de derivado | embedding/metadata | exposição indireta | segregação e finalidade | auditoria de exportação | revogar derivado | médio |
| TH-012 | cache residual | cliente/projeção | conteúdo após revogação | TTL + invalidation | teste pós-revogação | purge | médio |
| TH-013 | revogação incompleta | consumidor offline | novo uso indevido | enforcement central + tracking | consumer pending | bloquear consumidor | médio |
| TH-014 | restore reativa dado | backup antigo | violação de revogação | reaplicar tombstones | teste de restore | isolar restore | baixo |
| TH-015 | importação contaminada | arquivo ou conector | malware/dado falso | sandbox + validação | scanner/quarentena | eliminar e investigar | médio |
| TH-016 | mídia maliciosa | parser/transcoder | execução ou DoS | isolamento e limites | falha/anomalia | bloquear formato/fonte | médio |
| TH-017 | prompt injection | conteúdo capturado | agente altera comportamento | tratar conteúdo como dado | teste adversarial | ignorar instrução | alto |
| TH-018 | exfiltração por modelo | contexto excessivo | vazamento | minimização + egress control | monitor de saída | suspender modelo/fluxo | alto |
| TH-019 | inferência indevida | modelo/classificador | impacto humano | natureza obrigatória + confirmação | revisão/amostra | remover derivado | alto |
| TH-020 | consumidor comprometido | credencial ou sistema | vazamento distribuído | escopo + rotação + kill switch | anomalia/ack ausente | suspender entrega | alto |
| TH-021 | operador interno abusivo | console/admin | acesso indevido | JIT + justificativa + auditoria | revisão de acesso | suspender conta | médio |
| TH-022 | segredo em payload | erro de integração | comprometimento | validação e secret scanning | scanner | rotacionar segredo | baixo |
| TH-023 | downgrade de contrato | versão antiga | bypass de regra | compatibility policy | versão incompatível | quarentena | baixo |
| TH-024 | negação de serviço | mídia/consulta/retry | indisponibilidade | quotas e circuit breaker | saturação | limitar fonte | médio |
| TH-025 | correção não aplicada | consumidor atrasado | informação antiga | tracking e SLO | pendência | bloquear uso sensível | médio |
| TH-026 | exportação incompleta | omissão de metadados | natureza perdida | schema de exportação | validação | rejeitar exportação | baixo |

## 10. Prompt injection e conteúdo não confiável

Regras obrigatórias:

- conteúdo capturado nunca é instrução de sistema;
- documentos e mídia não podem alterar política, autoridade ou ferramentas;
- ferramentas disponíveis ao processamento são minimizadas;
- saídas de modelos são consideradas derivadas não confirmadas;
- conteúdo recuperado por busca preserva delimitadores e proveniência;
- chamadas externas exigem política independente do texto capturado;
- testes adversariais cobrem instruções ocultas, documentos e multimodal;
- falha segura produz sinalização, não execução privilegiada.

## 11. Segurança de modelos e Intelligence

- modelo não recebe segredos desnecessários;
- contexto é minimizado por finalidade;
- versão e provedor são rastreáveis;
- saída possui natureza e limitações;
- modelo não confirma nem autoriza;
- dados não podem ser reutilizados para treinamento sem decisão específica;
- egress e retenção do fornecedor devem ser avaliados em ADR tecnológico;
- incidentes devem permitir suspensão rápida do processamento automático.

## 12. Gestão de vulnerabilidades

A Onda 0 deverá definir:

- inventário de componentes;
- classificação de criticidade;
- scanning de dependências, imagens e infraestrutura;
- prazos de correção por severidade;
- exceções temporárias com responsável e expiração;
- teste de segurança antes de mudanças materiais;
- canal de reporte e resposta;
- rastreabilidade entre vulnerabilidade e ativo.

## 13. Critérios mínimos de segurança para readiness

1. threat model revisado;
2. matriz de acesso implementável;
3. fluxos C0 com falha fechada;
4. logs sensíveis proibidos e testados;
5. isolamento entre participantes testado;
6. restore com revogações testado;
7. consumidor comprometido suspensível;
8. prompt injection testada;
9. segredos fora de payloads;
10. SLOs instrumentáveis;
11. runbooks C0/C1 definidos;
12. riscos residuais registrados.

## 14. Evidências mínimas

- relatório de carga;
- relatório de disponibilidade e latência;
- teste de RPO/RTO;
- teste de restore;
- relatório de isolamento;
- scanner de logs;
- teste adversarial de prompt injection;
- exercício de suspensão de consumidor;
- inventário de riscos;
- aprovação dos SLOs da Onda 0.

## 15. Limites

Os valores são objetivos iniciais e não promessas públicas. Este documento não escolhe stack, não substitui avaliação jurídica ou de segurança independente e não declara produção segura antes da existência de evidências reais.