---
id: PAS-001-CC-W0-01-OWNERS-001
title: Matriz de Owners e Aprovadores do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-CHARTER-001
related:
  - PAS-001-CC-W0-RISK-001
  - PAS-001-CC-W0-EVIDENCE-001
---

# PAS-001-CC-W0-01-OWNERS-001 — Matriz de Owners e Aprovadores

> Owner lógico não equivale a owner nominal. A execução permanece bloqueada até que os papéis obrigatórios sejam atribuídos a pessoas identificadas e autorizadas.

## 1. Papéis nominais conhecidos

| Papel | Pessoa | Estado | Autoridade |
|---|---|---|---|
| Patrocinador executivo | Guilherme Oliveira | definido | aprovar prioridade, orçamento e continuidade |
| Autoridade de produto e propósito | Guilherme Oliveira | definido | preservar propósito, experiência e limites humanos |
| Aprovador de governança Guivos | Guilherme Oliveira | definido | aceitar marcos, riscos críticos e decisões de avanço |
| Administrador inicial da organização GitHub | Guilherme Oliveira | provisório | administrar acesso até delegação formal |

## 2. Papéis técnicos obrigatórios

| Papel | Pessoa | Estado | Bloqueio associado |
|---|---|---|---|
| Architecture Owner | a designar | bloqueante | ADRs, limites de domínio e coerência arquitetural |
| Engineering Owner / Tech Lead | a designar | bloqueante | execução, qualidade técnica e integração |
| Security & Privacy Owner | a designar | bloqueante | dados, autoridade, segredos, risco e privacidade |
| Quality & Evidence Owner | a designar | bloqueante | método, reprodução, validade e gates |
| Platform/DevOps Owner | a designar | bloqueante para execução técnica | repositório, pipeline, ambientes e credenciais |
| Data Owner | a designar | necessário antes do W0-03 | persistência, retenção, restore e integridade |

## 3. Requisitos para uma atribuição válida

Uma atribuição somente é válida quando registra:

- nome completo;
- conta GitHub;
- papel;
- autoridade concedida;
- responsabilidades;
- limites;
- substituto ou mecanismo de delegação;
- data de início;
- validade ou condição de revisão;
- aprovador da atribuição;
- confirmação explícita da pessoa.

Termos genéricos como `equipe técnica`, `fornecedor`, `Guivos` ou `desenvolvedores` não satisfazem owner nominal.

## 4. Matriz RACI inicial

| Entrega | Guilherme | Architecture | Engineering | Security/Privacy | Quality/Evidence | Platform/DevOps |
|---|---|---|---|---|---|---|
| propósito e escopo | A | C | I | C | I | I |
| ADR-TCC-001 | I | A | R | C | C | C |
| ADR-TCC-006 | C | A | R | R | C | I |
| branch protection | I | C | C | C | I | A/R |
| pipeline mínimo | I | C | A | C | C | R |
| dados sintéticos | I | C | R | A | C | I |
| template de evidência | I | C | C | C | A/R | I |
| riscos critical | A | C | C | R | C | I |
| encerramento do W0-01 | A | R | R | R | R | C |

Legenda: `A` accountable, `R` responsible, `C` consulted, `I` informed.

## 5. Autoridade de revisão por tipo de alteração

| Alteração | Aprovação mínima |
|---|---|
| estrutura, automação ou documentação técnica | Engineering Owner |
| domínio ou contrato funcional | Engineering + Architecture |
| segurança, identidade, dados ou autoridade | Security/Privacy + Architecture |
| pipeline, ambiente ou credencial | Platform/DevOps + Security/Privacy |
| método ou resultado de evidência | Quality/Evidence |
| risco high | owner técnico + Architecture/Security conforme tema |
| risco critical | Governança Guivos + autoridade técnica competente |
| propósito ou regra humana | Guilherme Oliveira + Architecture |

## 6. Segregação mínima

- autor não deverá ser único aprovador de alteração crítica;
- quem produz evidência não deverá ser seu único aprovador;
- administrador técnico não poderá assumir autoridade funcional humana;
- patrocinador não substitui revisão técnica especializada;
- fornecedor externo não recebe autoridade de governança por padrão;
- acesso administrativo deverá ser limitado, rastreável e revogável.

## 7. Ausência temporária e delegação

Delegação deverá registrar:

```yaml
delegation_id: string
role: string
from_person: string
to_person: string
scope: string[]
starts_at: datetime
expires_at: datetime
reason: string
approver: string
status: proposed | active | expired | revoked
```

Delegação sem expiração é inválida para W0-01.

## 8. Critérios de bloqueio

A execução do W0-01 não poderá começar quando:

- qualquer papel técnico obrigatório estiver sem pessoa;
- pessoa não tiver acesso compatível com o papel;
- autoridade não estiver clara;
- conflito de interesse não estiver tratado;
- delegação estiver expirada;
- risco critical não possuir owner competente;
- aprovador e executor forem a mesma pessoa em controle crítico sem revisão independente.

## 9. Evidência esperada

A atribuição deverá produzir parte de EV-017 contendo:

- matriz assinada ou aprovada;
- contas GitHub vinculadas;
- CODEOWNERS coerente;
- papéis sem conflito material;
- autoridades de interrupção;
- validade e revisão;
- hash do artefato;
- status `passed` somente quando todos os papéis bloqueantes estiverem atribuídos.

## 10. Estado atual

| Critério | Estado |
|---|---|
| patrocinador nominal | atendido |
| autoridade de produto nominal | atendido |
| governança nominal | atendido |
| Architecture Owner nominal | pendente — bloqueante |
| Engineering Owner nominal | pendente — bloqueante |
| Security & Privacy Owner nominal | pendente — bloqueante |
| Quality & Evidence Owner nominal | pendente — bloqueante |
| Platform/DevOps Owner nominal | pendente — bloqueante |

O estado atual não autoriza execução técnica.
