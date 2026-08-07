---
id: GKR-JOURNEY-HANDOFFS-001
title: Handoffs entre Participantes
status: active
version: 0.8.0
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
| TRN-110 | PER-106 | escolhe `Ver atualizações` sem alterar vínculo/leitura | PER-107 | **UXA-094** | **integralmente validada** |
| TRN-111 | PER-107 | contexto interno futuro | PER-108 | origem validada; destino não vigente | **ausente** |
| TRN-112 | COL-002 | acessa gestão de solicitações | COL-003 | UXA-090 | **integralmente validada** |

## 3. Contrato de TRN-110

A UXA-094 valida:

- gatilho explícito na origem;
- entrada neutra;
- contexto limitado a vínculos/objetos autorizados;
- retorno sem consequência oculta;
- leitura separada do estado substantivo;
- revalidação do estado canônico antes de ação;
- tratamento documental de estado obsoleto;
- idempotência de abertura e leitura;
- segurança material acima de ação comum;
- preferência sem ocultação indevida de aviso essencial.

## 4. Continuidade ainda aberta

`TRN-111` permanece ausente porque `PER-108 — Início do Participante` não possui materialização vigente. A Central não apresenta CTA fictício para mascarar essa ausência.

## 5. Estado vigente

Sete handoffs do trecho de Coletivos estão integralmente validados: `TRN-105`, `106`, `107`, `108`, `109`, `110` e `112`.

Validação integral documental não equivale a implementação técnica.

## 6. Próxima frente

**UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`PER-108`) e Refinamento de `TRN-111`**, mediante autorização separada.
