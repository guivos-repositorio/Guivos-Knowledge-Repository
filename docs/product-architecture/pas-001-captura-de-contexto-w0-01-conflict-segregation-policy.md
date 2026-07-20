---
id: PAS-001-CC-W0-01-CONFLICT-SEGREGATION-001
title: Política de Conflitos e Segregação dos Owners do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-OWNER-APPOINTMENT-001
related:
  - PAS-001-CC-W0-01-MINIMUM-TEAM-001
  - PAS-001-CC-W0-RISK-001
---

# PAS-001-CC-W0-01-CONFLICT-SEGREGATION-001 — Política de Conflitos e Segregação

## 1. Objetivo

Impedir concentração indevida de autoridade, autoaprovação de controles críticos, ocultação de conflitos e dependência operacional incompatível com a Onda 0.

## 2. Tipos de conflito

- financeiro: remuneração, fornecedor ou participação influencia decisão;
- societário: interesse de sócio diverge do dever técnico;
- hierárquico: pessoa não consegue bloquear superior sem proteção;
- operacional: autor, aprovador e operador são a mesma pessoa;
- evidencial: produtor é único aprovador da prova;
- tecnológico: candidato favorece tecnologia por vínculo ou preferência não declarada;
- temporal: disponibilidade insuficiente gera aprovações formais sem revisão real;
- informacional: acesso excede necessidade do papel;
- pessoal: relação que compromete independência material.

## 3. Declaração obrigatória

Cada candidato e owner deverá declarar:

- vínculos profissionais e societários relevantes;
- fornecedores com os quais possui relação;
- tecnologias sobre as quais recebe benefício;
- outros projetos concorrentes ou conflitantes;
- relações hierárquicas entre owners;
- limitações de disponibilidade;
- qualquer condição que possa afetar julgamento independente.

Ausência de conflito declarado não elimina revisão posterior.

## 4. Segregações mínimas

1. autor não é único aprovador de mudança crítica;
2. produtor de evidência não é seu único aprovador;
3. administrador GitHub não aprova sozinho sua própria ampliação de acesso;
4. Engineering não aprova sozinho segurança ou privacidade;
5. Security não altera propósito ou confirma fato humano;
6. Quality não modifica resultado para permitir gate;
7. patrocinador não substitui competência técnica;
8. fornecedor não controla simultaneamente execução, evidência e governança;
9. risco critical exige governança e autoridade técnica competente;
10. produção permanece fora de qualquer delegação do W0-01.

## 5. Matriz de incompatibilidades

| Acúmulo | Estado | Condição |
|---|---|---|
| Architecture + Engineering | permitido provisoriamente | revisão de Security e Quality |
| Engineering + Platform/DevOps | permitido provisoriamente | validade limitada e revisão de acesso |
| Architecture + Data | permitido antes do W0-03 | competência e revisão de Security |
| Engineering + Security/Privacy | proibido no modelo mínimo | somente exceção formal com revisão externa |
| Engineering + Quality/Evidence | proibido como aprovação da própria prova | colaboração em teste permitida |
| Security + Quality | possível com cautela | não pode eliminar independência de gate |
| todos os papéis em uma pessoa | proibido | não excepcionável para autorização |

## 6. Tratamentos

Um conflito poderá ser tratado por:

- recusa da pessoa na decisão específica;
- coaprovação independente;
- revisão externa;
- redução de escopo;
- acesso temporário;
- separação de papéis;
- substituição;
- suspensão;
- rejeição da nomeação.

## 7. Registro

```yaml
conflict_id: string
person: string
role: string
type: financial | corporate | hierarchical | operational | evidential | technological | temporal | informational | personal
description: string
affected_decisions: string[]
severity: low | medium | high | critical
mitigation: string[]
recusal_required: boolean
independent_reviewer: string | null
approver: string
review_at: date
status: declared | mitigated | active | suspended | closed
```

## 8. Gatilhos de suspensão

Suspender o papel quando:

- conflito high ou critical não possuir mitigação;
- declaração for falsa ou materialmente incompleta;
- pessoa aprovar controle crítico próprio sem revisão exigida;
- fornecedor usar posição para direcionar contratação;
- acesso for utilizado fora do escopo;
- independência de Quality ou Security for comprometida;
- pressão de prazo impedir revisão real.

## 9. Exceções

Exceção deverá possuir:

- escopo limitado;
- justificativa;
- risco;
- controle compensatório;
- revisão independente;
- validade;
- aprovador competente;
- condição de encerramento.

Não são excepcionáveis:

- todos os papéis em uma única pessoa;
- vazamento entre participantes;
- autoridade humana indevida;
- uso de dados reais não autorizado;
- evidência deliberadamente falsa;
- produção implícita.

## 10. Evidência

A EV-017 deverá registrar conflitos declarados, tratamentos, recusas, revisores independentes, validade e estado.

## 11. Limites

Esta política não define vínculo, remuneração, contratação ou nomes. Ela estabelece controles para futuras nomeações e permanece sem autorizar o W0-01.