---
id: GKR-JOURNEY-HANDOFFS-001
title: Handoffs entre Participantes
status: active
version: 0.10.0
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
  - UXA-096
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
| TRN-110 | PER-106 | escolhe `Ver atualizações` sem alterar vínculo/leitura | PER-107 | UXA-094; PER-107 corrente revalidado UXA-096 | **integralmente validada** |
| TRN-111 | PER-107 | escolhe `Abrir início do Coletivo` com vínculo atual elegível | PER-108 | **UXA-095/096** | **integralmente validada** |
| TRN-112 | COL-002 | acessa gestão de solicitações | COL-003 | UXA-090 | **integralmente validada** |

## 3. Contrato preservado de TRN-110

A UXA-096 revalida a Central corrente sem modificar o contrato validado da entrada em `PER-107`: vínculo/leitura permanecem inalterados, ações substantivas revalidam estado canônico e repetição não duplica efeito lógico.

## 4. Contrato validado de TRN-111

A UXA-096 fecha:

```text
PER-107
→ “Abrir início do Coletivo”
→ vínculo atual e permissão são revalidados
→ histórico não concede nem preserva acesso
→ vínculo, leitura, papel, presença e autoridade não mudam
→ PER-108
```

Foram examinados:

- identidade do Coletivo e do vínculo lógico;
- estado canônico atual;
- perda de permissão, pausa, saída e remoção;
- retorno neutro à Central;
- leitura separada do efeito substantivo;
- ações internas revalidadas antes do efeito;
- repetição e recarga idempotentes.

## 5. Estado vigente

Oito handoffs do trecho de Coletivos estão integralmente validados: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

Validação integral documental não equivale a implementação técnica.

## 6. Próxima frente

A próxima priorização deverá partir das lacunas remanescentes. **UXA-097 não foi iniciada.**
