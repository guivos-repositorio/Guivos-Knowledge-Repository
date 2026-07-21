---
id: PAS-001-CC-W0-01-OWNER-READINESS-001
title: Gate de Prontidão dos Owners Técnicos do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-OWNER-APPOINTMENT-001
related:
  - PAS-001-CC-W0-01-READINESS-001
  - PAS-001-CC-W0-01-APPOINTMENT-RECORD-001
  - PAS-001-CC-W0-01-CONFLICT-SEGREGATION-001
---

# PAS-001-CC-W0-01-OWNER-READINESS-001 — Gate de Prontidão dos Owners Técnicos

## 1. Objetivo

Definir os critérios que transformam o framework documental em nomeações aptas a participar de uma futura decisão de autorização do W0-01.

A aprovação deste gate não autoriza execução; apenas remove o bloqueio de owners.

## 2. Estados

- `not_started`: nenhum candidato em avaliação;
- `in_progress`: processo ativo, papéis incompletos;
- `blocked`: requisito obrigatório ausente ou inválido;
- `ready_for_decision`: todos os requisitos documentais e pessoais atendidos;
- `passed`: nomeações ativas e EV-017 aprovada;
- `failed`: requisito material incompatível;
- `expired`: nomeação ou evidência perdeu validade.

## 3. Critérios por papel

| Critério | Architecture | Engineering | Security/Privacy | Quality/Evidence | Platform/DevOps |
|---|---:|---:|---:|---:|---:|
| pessoa identificada | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| conta GitHub individual | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| perfil avaliado | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| exercício técnico | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| competências obrigatórias >= 3 | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| eliminadores ausentes | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| conflito tratado | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| disponibilidade aceita | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| autoridade e limites | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| aceite formal | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |
| acesso compatível | para `active` | para `active` | para `active` | para `active` | para `active` |
| EV-017 vinculada | obrigatório | obrigatório | obrigatório | obrigatório | obrigatório |

## 4. Critérios do modelo mínimo

Para estrutura mínima de três pessoas:

- Pessoa A poderá cobrir Architecture, Engineering e Platform/DevOps provisório;
- Pessoa B cobrirá Security & Privacy;
- Pessoa C cobrirá Quality & Evidence;
- três pessoas deverão ser distintas;
- Platform/DevOps acumulado terá expiração;
- Security e Quality permanecerão independentes de Engineering;
- quóruns e recusas estarão registrados;
- revisão independente existirá para controle crítico.

## 5. Checklist consolidado

### Identidade e avaliação

- [ ] nomes completos registrados;
- [ ] contas GitHub vinculadas;
- [ ] perfis e portfólios avaliados;
- [ ] exercícios concluídos;
- [ ] matriz ponderada aprovada;
- [ ] referências verificadas quando aplicável;
- [ ] eliminadores ausentes.

### Autoridade e vínculo

- [ ] papéis definidos;
- [ ] autoridades de aprovação, bloqueio e stop aceitas;
- [ ] limites e proibições registrados;
- [ ] modelo de vínculo registrado;
- [ ] confidencialidade e propriedade intelectual tratadas;
- [ ] validade e revisão definidas;
- [ ] delegação definida.

### Conflitos e segregação

- [ ] conflitos declarados;
- [ ] mitigações aprovadas;
- [ ] nenhuma pessoa concentra todos os papéis;
- [ ] Security independente;
- [ ] Quality independente;
- [ ] autor e aprovador segregados em controles críticos;
- [ ] administrador não aprova sozinho acesso próprio.

### Ativação

- [ ] registros de nomeação aceitos;
- [ ] acessos compatíveis;
- [ ] CODEOWNERS planejado ou configurado;
- [ ] riscos high/critical com owner;
- [ ] EV-017 atualizada;
- [ ] aprovadores confirmaram ativação;
- [ ] nenhuma validade expirada.

## 6. Bloqueadores

O gate falha ou permanece bloqueado quando:

- papel obrigatório não possui pessoa;
- conta é compartilhada ou ausente;
- competência obrigatória não foi comprovada;
- eliminador foi identificado;
- conflito material está sem tratamento;
- aceite está ausente;
- autoridade é ambígua;
- segregação crítica não existe;
- risco critical não possui owner competente;
- acesso excede o papel;
- EV-017 está ausente, falha ou expirada.

## 7. Pacote de decisão

O pacote deverá conter:

- matriz de papéis;
- avaliações;
- registros de nomeação;
- conflitos e mitigações;
- modelo de equipe;
- quóruns;
- acessos planejados;
- EV-017;
- riscos;
- limitações;
- recomendação;
- validade.

## 8. Decisão

A decisão deverá registrar um dos resultados:

- `passed`: bloqueio de owners removido;
- `conditional`: pendência não crítica com validade, sem autorizar execução;
- `failed`: nomeações insuficientes ou incompatíveis;
- `rework`: avaliação ou estrutura deve ser refeita.

Resultado `passed` permite apenas submeter uma decisão separada de autorização do W0-01.

## 9. Revalidação

Revalidar:

- antes da autorização do W0-01;
- após mudança de pessoa ou papel;
- após suspensão ou incidente;
- após expiração;
- antes do encerramento do W0-01;
- antes de ampliar ambiente ou acesso.

## 10. Estado atual

| Dimensão | Estado |
|---|---|
| framework | definido por este ciclo |
| perfis | definidos por este ciclo |
| candidatos | não identificados |
| avaliações | não iniciadas |
| nomeações | inexistentes |
| EV-017 de owners | não produzida |
| gate | `not_started` |
| execução W0-01 | bloqueada |

## 11. Limites

Este gate não cria nomes, acessos, contratação, repositório, pipeline, ADR, POC, ambiente ou autorização de execução.