---
id: GKR-JOURNEY-HANDOFFS-001
title: Handoffs entre Participantes
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-019
  - UXA-056
  - UXA-066
  - UXA-067
  - UXA-070
normative: false
---

# Handoffs entre Participantes

## Finalidade

Esta vista identifica pontos em que a próxima decisão deixa uma perspectiva e passa para outra autoridade legítima.

## Handoffs prioritários

| Origem | Evento | Destino | Autoridade | Estado |
|---|---|---|---|---|
| Pessoa | envia solicitação de participação | responsável autorizado pelo Coletivo | UXA-056; UXA-066 | materializado na visão da Pessoa; visão do responsável ausente |
| Coletivo | solicita informação adicional | Pessoa solicitante | UXA-066; UXA-067 | materializado e validado na visão da Pessoa |
| Coletivo | aprova, recusa ou deixa expirar | Pessoa solicitante | UXA-066; UXA-067 | materializado e validado na visão da Pessoa |
| Pessoa e Coletivo | formam vínculo | governança interna do Coletivo | UXA-014; UXA-056 | transição contratada; continuidade visual ausente |
| Organização | propõe relação ou apoio | Coletivo | UXA-019 | contratada; materialização específica ausente |
| Coletivo | aceita, negocia ou recusa relação | Organização | UXA-019 | contratada; materialização específica ausente |
| Organização | publica oportunidade | Pessoa | UXA-008; UXA-013 | materializada e validada no escopo existente |
| Pessoa | acessa oportunidade | Organização ou destino identificado | UXA-004; UXA-007; UXA-012 | materializada e validada no escopo existente |

## Regra de proteção

Cada handoff deverá declarar:

- quem inicia;
- quem recebe a próxima decisão;
- qual autoridade permite a ação;
- quais dados atravessam a fronteira;
- qual efeito ocorre;
- como cancelar, corrigir ou contestar;
- o que acontece se a jornada for interrompida.

Nenhum handoff poderá ser inferido apenas pela proximidade entre telas.
