---
id: GKR-JOURNEY-HANDOFFS-001
title: Handoffs entre Participantes
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-019
  - UXA-056
  - UXA-066
  - UXA-067
  - UXA-070
  - UXA-072
  - UXA-073
normative: false
---

# Handoffs entre Participantes

## 1. Finalidade

Esta vista identifica pontos em que a próxima decisão deixa uma perspectiva e passa para outra autoridade legítima.

Nenhum handoff é considerado validado apenas porque as superfícies de origem e destino existem. A evidência deve abranger a transição, os dados transferidos, o efeito, o retorno e a possibilidade de contestação.

## 2. Matriz reformulada

| Origem e maturidade | Evento | Destino e maturidade | Autoridade | Evidência da transição | Retorno ou contestação | Lacuna |
|---|---|---|---|---|---|---|
| Pessoa — validado na perspectiva solicitante | envia solicitação de participação | responsável do Coletivo — não materializado | UXA-056; UXA-066 | envio e estado pendente materializados na visão da Pessoa | cancelamento e acompanhamento na visão da Pessoa | operação do responsável ausente |
| responsável do Coletivo — programado | solicita informação adicional | Pessoa — validado na perspectiva solicitante | UXA-056; UXA-066; UXA-067 | retorno materializado somente na visão da Pessoa | Pessoa pode revisar, responder ou não prosseguir | origem operacional não materializada |
| responsável do Coletivo — programado | aprova, recusa ou deixa expirar | Pessoa — validado na perspectiva solicitante | UXA-056; UXA-066; UXA-067 | resultado materializado somente na visão da Pessoa | recusa, cancelamento e expiração permanecem distintos | decisão do responsável não materializada |
| Pessoa — parcial | aceita vínculo formado | governança interna do Coletivo — contratada | UXA-014; UXA-056 | transição contratada, sem continuidade visual bilateral | saída e contestação dependem de regras do vínculo | Meus Coletivos e operação interna ausentes |
| Organização — contratada | propõe relação ou apoio | Coletivo — contratado | UXA-019 | nenhuma superfície bilateral específica | negociação, recusa e encerramento contratados | materialização bilateral ausente |
| Coletivo — contratado | aceita, negocia ou recusa relação | Organização — contratada | UXA-019 | nenhuma superfície bilateral específica | revisão, pausa e encerramento contratados | materialização bilateral ausente |
| Organização — validado no cadastro | publica oportunidade | Pessoa — validado na consulta | UXA-004; UXA-008; UXA-013 | publicação e consulta existem em pacotes distintos | edição ou retirada pela Organização; retorno da Pessoa ao catálogo | integração ponta a ponta não examinada |
| Pessoa — validado na consulta | acessa oportunidade | Organização ou destino identificado — parcial | UXA-004; UXA-007; UXA-012 | detalhe e destino apresentados no escopo existente | retorno à lista ou mapa conforme superfície | efeito externo não validado nesta seção |

## 3. Campos obrigatórios

Cada handoff deverá declarar:

- maturidade da origem;
- maturidade do destino;
- quem inicia;
- quem recebe a próxima decisão;
- autoridade que permite a ação;
- dados que atravessam a fronteira;
- efeito produzido;
- evidência da transição;
- forma de cancelar, corrigir ou contestar;
- estado de interrupção;
- lacuna aplicável.

## 4. Regras de proteção

- origem materializada não presume destino materializado;
- retorno visível para a Pessoa não comprova a existência da operação do responsável;
- contrato bilateral não equivale a interface bilateral;
- nenhuma seta será criada por proximidade, ordem numérica ou conveniência narrativa;
- esta vista permanece `draft` até nova validação funcional.
