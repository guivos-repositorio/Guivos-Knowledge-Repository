---
id: PAS-001-CC-W0-01-APPOINTMENT-RECORD-001
title: Registro Formal de Nomeação dos Owners Técnicos
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-OWNER-APPOINTMENT-001
related:
  - PAS-001-CC-W0-01-CANDIDATE-ASSESSMENT-001
  - PAS-001-CC-W0-01-EVIDENCE-001
---

# PAS-001-CC-W0-01-APPOINTMENT-RECORD-001 — Registro Formal de Nomeação

## 1. Finalidade

Definir o artefato obrigatório que transforma uma recomendação aprovada em nomeação rastreável. Registro incompleto, sem aceite ou sem conta GitHub não produz owner nominal válido.

## 2. Schema canônico

```yaml
appointment_id: string
person:
  full_name: string
  github_account: string
  professional_reference: string | null
role: architecture_owner | engineering_owner | security_privacy_owner | quality_evidence_owner | platform_devops_owner | data_owner
employment_model: contractor | employee | partner | cofounder | advisor | other
scope:
  wave: W0
  increments: string[]
  repositories: string[]
authority:
  approve: string[]
  block: string[]
  stop: string[]
responsibilities: string[]
limitations: string[]
forbidden_actions: string[]
delegation:
  allowed: boolean
  rules: string[]
  maximum_days: integer | null
conflicts:
  declared: string[]
  mitigations: string[]
access_requirements: string[]
starts_at: date
review_at: date
expires_at: date | null
approvers: string[]
assessment_reference: string
risk_references: string[]
evidence_references: string[]
accepted_by_person: boolean
accepted_at: datetime | null
status: proposed | accepted | active | suspended | revoked | expired
integrity_hash: string
```

## 3. Campos obrigatórios

São obrigatórios:

- nome completo;
- conta GitHub individual;
- papel;
- escopo;
- autoridade;
- responsabilidades;
- limites;
- ações proibidas;
- início e revisão;
- aprovadores;
- avaliação vinculada;
- conflitos;
- aceite explícito;
- hash.

## 4. Autoridade

A autoridade deverá distinguir:

- o que a pessoa pode aprovar;
- o que pode bloquear;
- o que pode interromper;
- o que exige coaprovação;
- o que permanece fora de sua competência.

Exemplo: Security & Privacy pode interromper fluxo por vazamento ou segredo exposto, mas não pode confirmar fato humano nem alterar propósito do produto.

## 5. Limites mínimos por papel

### Architecture

Não pode alterar propósito, base humana ou regra funcional sem governança competente.

### Engineering

Não pode aprovar sozinho segurança, privacidade ou evidência que produziu.

### Security & Privacy

Não pode assumir autoridade humana, produto ou decisão de negócio fora do risco.

### Quality & Evidence

Não pode modificar resultado para permitir gate nem apagar execução falha.

### Platform/DevOps

Não pode implantar produção, ampliar acesso ou criar credencial compartilhada.

### Data

Não pode reduzir retenção, exclusão ou integridade por conveniência operacional sem decisão.

## 6. Aceite

O aceite deverá confirmar que a pessoa:

- leu os documentos aplicáveis;
- compreendeu autoridade e limites;
- aceita responsabilidades;
- aceita autoridade de interrupção;
- declarou conflitos;
- aceita revisão e destituição;
- concorda com confidencialidade e propriedade intelectual aplicáveis;
- utilizará conta individual e acesso rastreável.

Aceite verbal sem registro não é válido.

## 7. Ativação

Uma nomeação `accepted` muda para `active` somente quando:

- acesso compatível existir;
- proteção de branch e CODEOWNERS estiverem coerentes, quando aplicável;
- nenhum conflito bloqueante permanecer;
- o papel estiver incluído na EV-017;
- o aprovador confirmar a ativação;
- a validade não tiver expirado.

## 8. Revisão

Revisar no mínimo:

- antes da autorização do W0-01;
- no encerramento do W0-01;
- após incidente;
- após alteração de vínculo;
- após acúmulo ou separação de papéis;
- antes de W0-03 para Data Owner;
- quando a data de revisão vencer.

## 9. Suspensão e revogação

O registro deverá indicar motivo, escopo afetado, contenção, acessos revogados, substituição e decisão de retomada.

Suspensão não apaga decisões anteriores. Revogação exige remoção ou revisão de acessos e delegações.

## 10. Registro de histórico

Mudança de nomeação cria nova versão ou evento de atualização. Não sobrescrever silenciosamente:

- aceite;
- conflito;
- limite;
- autoridade;
- validade;
- suspensão;
- revogação.

## 11. Evidência

O registro ativo deverá compor EV-017 com hash verificável, referência da avaliação, aceite, aprovadores e estado de acesso.

## 12. Limites

Este documento fornece o schema e o método. Nenhum registro nominal é criado neste ciclo e nenhum acesso é concedido.