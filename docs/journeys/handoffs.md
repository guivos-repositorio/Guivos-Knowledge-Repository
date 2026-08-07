---
id: GKR-JOURNEY-HANDOFFS-001
title: Handoffs entre Participantes
status: active
version: 0.9.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-019
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-090
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Handoffs entre Participantes

## 1. Finalidade

Esta vista identifica pontos em que a próxima decisão ou contexto passa para outra superfície ou autoridade legítima. Nenhum handoff é considerado validado apenas porque as superfícies existem.

## 2. Matriz governada de Coletivos

| ID | Origem | Evento | Destino | Evidência | Estado |
|---|---|---|---|---|---|
| TRN-104 | PER-104 | envia solicitação | PER-105 | UXA-065/067 | parcial |
| TRN-105 | PER-105 | solicitação disponível para análise | COL-003 | UXA-090 | **integralmente validada** |
| TRN-106 | COL-003 | pede informação adicional | PER-105 | UXA-090 | **integralmente validada** |
| TRN-107 | PER-105 | envia informação adicional | COL-003 | UXA-090 | **integralmente validada** |
| TRN-108 | COL-003 | aprova, forma vínculo e apresenta resultado | PER-106 via PER-105 | UXA-092 | **integralmente validada** |
| TRN-109 | COL-003 | recusa solicitação | PER-105 | UXA-090 | **integralmente validada** |
| TRN-110 | PER-106 | escolhe `Ver atualizações` sem alterar vínculo/leitura | PER-107 | UXA-094 | **integralmente validada** |
| TRN-111 | PER-107 | escolhe `Abrir início do Coletivo` em vínculo existente | PER-108 | **UXA-095** | **parcial** |
| TRN-112 | COL-002 | acessa gestão de solicitações | COL-003 | UXA-090 | **integralmente validada** |

## 3. Contrato preservado de TRN-110

A UXA-095 não modifica o contrato validado da entrada em `PER-107`: vínculo/leitura permanecem inalterados, ações substantivas revalidam estado canônico e repetição não duplica efeito lógico.

## 4. Materialização de TRN-111

A UXA-095 torna explícito:

```text
PER-107
→ “Abrir início do Coletivo”
→ vínculo, leitura, papel, presença e autoridade não mudam
→ PER-108
```

A ligação permanece parcial porque:

- o SVG da origem foi reformulado após sua validação;
- o destino é novo e ainda não validado;
- retorno, concorrência, estado obsoleto e ações internas não foram examinados como conjunto.

## 5. Estado vigente

Sete handoffs do trecho anterior de Coletivos permanecem integralmente validados: `TRN-105`, `106`, `107`, `108`, `109`, `110` e `112`.

`TRN-111` é adicionalmente **materializada de forma parcial**, não integralmente validada.

Validação integral documental não equivale a implementação técnica.

## 6. Próxima frente

**UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de TRN-111**, mediante autorização separada.
