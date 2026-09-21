---
id: GKR-JOURNEY-HANDOFFS-001
title: Handoffs entre Participantes
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
related:
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
normative: false
---

# Handoffs entre Participantes

## 1. Finalidade

Esta vista resume transferências correntes de contexto, decisão ou autoridade entre participantes e superfícies.

A maturidade oficial de cada transição pertence ao `GKR-JOURNEY-TRANSITION-REGISTRY-001`. Esta página não mantém a cronologia de validações UXA como fonte operacional.

## 2. Pessoa → Coletivo → Pessoa

| Transição | Origem → destino | Papel do handoff | Estado corrente |
|---|---|---|---|
| `GKR-TRN-104` | PER-104 → PER-105 | enviar solicitação autorizada | **parcial** |
| `GKR-TRN-105` | PER-105 → COL-003 | disponibilizar a mesma solicitação ao responsável | **integralmente validada** |
| `GKR-TRN-106` | COL-003 → PER-105 | solicitar informação adicional sem aprovar | **integralmente validada** |
| `GKR-TRN-107` | PER-105 → COL-003 | responder à mesma finalidade sem duplicação | **integralmente validada** |
| `GKR-TRN-108` | COL-003 → PER-106 | aprovação forma vínculo e apresenta continuidade | **integralmente validada** |
| `GKR-TRN-109` | COL-003 → PER-105 | recusar solicitação | **integralmente validada** |
| `GKR-TRN-110` | PER-106 → PER-107 | abrir Atualizações sem alterar vínculo/leitura por navegação | **integralmente validada** |
| `GKR-TRN-111` | PER-107 → PER-108 | abrir início do mesmo Coletivo com permissão revalidada | **integralmente validada** |
| `GKR-TRN-112` | COL-002 → COL-003 | responsável abre gestão especializada de solicitações | **integralmente validada** |

A continuidade não autoriza inferir que toda a Jornada de participação esteja integralmente fechada: `TRN-104` permanece parcial e outras transições do domínio preservam seus próprios estados.

## 3. Proteções do handoff Pessoa ↔ Coletivo

Os handoffs validados preservam:

- identidade lógica da solicitação e do vínculo;
- autoridade proporcional ao papel;
- revalidação de vínculo e permissão antes de ações substantivas;
- separação entre leitura, presença, vínculo e autoridade;
- interrupção segura;
- retorno neutro;
- idempotência;
- prevalência do estado canônico mais recente.

```text
HISTÓRICO DE VÍNCULO
≠ AUTORIZAÇÃO ATUAL

NAVEGAR
≠ APROVAR
≠ PARTICIPAR
≠ ALTERAR LEITURA
```

## 4. Organização → Pessoa — oportunidade e fronteira externa

A publicação e descoberta de oportunidade chegam ao Detalhe por transições correntes validadas.

O handoff de autoridade relevante é:

```text
PER-203 — DETALHE
→ REVISÃO CONSCIENTE
→ GKR-TRN-205
→ BND-001 — FRONTEIRA EXTERNA
→ TERCEIRO
```

`GKR-TRN-205` está **integralmente validada até a fronteira de autoridade Guivos**.

Antes da transferência, a experiência deve preservar destino, responsável, dados/contexto envolvidos, limites, revalidação e possibilidade de cancelamento.

Depois da transferência consciente, o processo do terceiro não passa a ser autoridade ou responsabilidade da Guivos.

## 5. Organização ↔ Coletivo

As relações institucionais possuem contratos funcionais, mas a continuidade bilateral ainda não está fechada como experiência ponta a ponta.

Estado corrente das transições principais:

| Transição | Origem → destino | Estado |
|---|---|---|
| `GKR-TRN-206` | ORG-004 → COL-008 | **contratada** |
| `GKR-TRN-207` | COL-008 → ORG-005 | **contratada** |
| `GKR-TRN-208` | ORG-005 → ORG-006 | **contratada** |
| `GKR-TRN-209` | ORG-006 → ORG-006 | **contratada** |

A existência da relação funcional não autoriza inventar superfícies bilaterais, estados operacionais ou efeitos ainda ausentes.

## 6. Regra de leitura

```text
HANDOFF VIEW
→ CURRENT SYNTHESIS

TRANSITION REGISTRY
→ MATURITY AUTHORITY

SURFACE REGISTRY
→ STATE / OWNERSHIP AUTHORITY

HISTORICAL VALIDATION SEQUENCE
→ GIT / PROVENANCE

IMPLEMENTATION
→ NOT INFERRED
```
