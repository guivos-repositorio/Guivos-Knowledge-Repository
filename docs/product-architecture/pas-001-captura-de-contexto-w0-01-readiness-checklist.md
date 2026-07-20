---
id: PAS-001-CC-W0-01-READINESS-001
title: Checklist de Prontidão para Execução Controlada do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-CHARTER-001
related:
  - PAS-001-CC-W0-01-OWNERS-001
  - PAS-001-CC-W0-01-REPO-001
  - PAS-001-CC-W0-01-PIPELINE-001
  - PAS-001-CC-W0-01-SYNTHETIC-DATA-001
  - PAS-001-CC-W0-01-EVIDENCE-001
  - PAS-001-CC-W0-01-DECISIONS-001
---

# PAS-001-CC-W0-01-READINESS-001 — Checklist de Prontidão

> O checklist separa pacote documental concluído de execução autorizada. Item documentado não é item implementado.

## 1. Estados

- `defined`: contrato documental existe;
- `assigned`: pessoa nominal aceitou o papel;
- `configured`: controle foi aplicado;
- `verified`: teste reproduzível comprovou o controle;
- `blocked`: pré-condição ausente;
- `not_applicable`: exclusão justificada e aprovada.

## 2. Gate A — Autoridade e owners

| ID | Critério | Estado atual | Bloqueia execução |
|---|---|---|---:|
| A-01 | patrocinador nominal | defined | não |
| A-02 | autoridade de produto nominal | defined | não |
| A-03 | governança nominal | defined | não |
| A-04 | Architecture Owner nominal | blocked | sim |
| A-05 | Engineering Owner nominal | blocked | sim |
| A-06 | Security & Privacy Owner nominal | blocked | sim |
| A-07 | Quality & Evidence Owner nominal | blocked | sim |
| A-08 | Platform/DevOps Owner nominal | blocked | sim |
| A-09 | autoridades de interrupção aceitas | defined | sim até assigned |

## 3. Gate B — Decisões

| ID | Critério | Estado atual | Exigido para |
|---|---|---|---|
| B-01 | ADR-TCC-001 com método e owner | defined | autorização W0-01 |
| B-02 | ADR-TCC-001 accepted | blocked | início W0-02 |
| B-03 | ADR-TCC-006 com método e owner | defined | autorização W0-01 |
| B-04 | ADR-TCC-006 accepted | blocked | início W0-02 |
| B-05 | recorte ADR-TCC-008 definido | defined | execução W0-01 |
| B-06 | recorte ADR-TCC-010 definido | defined | execução W0-01 |
| B-07 | planos ADR-TCC-002/004 definidos | defined | encerramento W0-01 |

## 4. Gate C — Repositório e branches

| ID | Critério | Estado atual | Bloqueia encerramento |
|---|---|---|---:|
| C-01 | nome e finalidade do repositório definidos | defined | sim |
| C-02 | criação privada autorizada | blocked | sim |
| C-03 | repositório criado como privado | blocked | sim |
| C-04 | `main` protegida | blocked | sim |
| C-05 | push direto bloqueado | blocked | sim |
| C-06 | checks obrigatórios configurados | blocked | sim |
| C-07 | CODEOWNERS nominal | blocked | sim |
| C-08 | template de PR instalado | blocked | sim |
| C-09 | teste de bloqueio reproduzível | blocked | sim |

## 5. Gate D — Pipeline

| ID | Critério | Estado atual | Bloqueia encerramento |
|---|---|---|---:|
| D-01 | contrato independente da stack | defined | sim |
| D-02 | secret scan ativo | blocked | sim |
| D-03 | synthetic-data scan ativo | blocked | sim |
| D-04 | governance validation ativo | blocked | sim |
| D-05 | evidence manifest validation ativo | blocked | sim |
| D-06 | checks específicos da stack | blocked | sim |
| D-07 | falha deliberada bloqueia merge | blocked | sim |
| D-08 | nenhum workflow implanta produção | defined | sim até verified |

## 6. Gate E — Dados e segredos

| ID | Critério | Estado atual | Bloqueia encerramento |
|---|---|---|---:|
| E-01 | política de dados sintéticos | defined | sim |
| E-02 | catálogo mínimo criado | blocked | sim |
| E-03 | geradores versionados | blocked | sim |
| E-04 | nenhuma fixture da VAL-002 | defined | sim até verified |
| E-05 | inventário de segredos | blocked | sim |
| E-06 | credenciais por ambiente | blocked | sim |
| E-07 | teste de dado proibido bloqueado | blocked | sim |
| E-08 | mídia sintética catalogada | blocked | sim quando aplicável |

## 7. Gate F — Evidências e riscos

| ID | Critério | Estado atual | Bloqueia encerramento |
|---|---|---|---:|
| F-01 | schema de evidência definido | defined | sim |
| F-02 | schema implementado e validado | blocked | sim |
| F-03 | EV-017 produzida | blocked | sim |
| F-04 | EV-018 produzida | blocked | sim |
| F-05 | riscos high/critical com owner | blocked | sim |
| F-06 | exceções com validade | defined | sim até verified |
| F-07 | resultados falhos preservados | defined | sim até verified |
| F-08 | decisão de encerramento separada | blocked | sim |

## 8. Gate G — Dependências anteriores ao build

| Dependência | Estado documental | Estado operacional |
|---|---|---|
| CC-W0-001 identidade e representação | definida | não disponível/validada |
| CC-W0-002 autoridade contextual | definida | não disponível/validada |
| CC-W0-003 registro transacional | definida | não disponível/validada |
| CC-W0-005 idempotência | definida | não disponível/validada |
| CC-W0-006 registro de schemas | definida | não disponível/validada |
| CC-W0-015 classificação de sensibilidade | definida | não disponível/validada |
| CC-W0-016 catálogo de erros | definida | não disponível/validada |

O W0-01 deverá atribuir owner, contrato, fallback, limite e evidência de disponibilidade para cada dependência.

## 9. Decisão de autorização

A autorização de execução exige:

- todos os itens A bloqueantes em `assigned`;
- B-01, B-03, B-05 e B-06 aprovados;
- C-02 aprovada;
- riscos critical com autoridade de tratamento;
- nenhuma tentativa de uso de dado real;
- decisão escrita com escopo e validade.

## 10. Decisão de encerramento

O encerramento exige:

- todos os itens obrigatórios em `configured` ou `verified`;
- ADR-TCC-001 e ADR-TCC-006 accepted;
- EV-017 e EV-018 passed ou exceção válida permitida;
- nenhum risco critical aberto sem tratamento;
- dependências anteriores ao build com status explícito;
- relatório de limitações;
- declaração de que W0-02 não inicia automaticamente.

## 11. Estado consolidado atual

| Dimensão | Estado |
|---|---|
| pacote documental do W0-01 | definido |
| owners técnicos nominais | pendentes |
| autorização de execução | bloqueada |
| repositório de implementação | não criado |
| pipeline | não configurado |
| ADRs tecnológicos | não decididos |
| evidências operacionais | não produzidas |
| W0-01 executado | 0% |
| produção | não autorizada |

## 12. Próxima decisão permitida

A próxima decisão poderá autorizar somente a atribuição dos owners nominais e, depois de revalidados os critérios, a execução controlada do W0-01. Nenhum avanço para W0-02 é implícito.
