---
id: GKR-JOURNEY-HANDOFFS-001
title: Handoffs entre Participantes
status: active
version: 0.4.0
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
  - UXA-074
  - UXA-075
  - UXA-076
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Handoffs entre Participantes

## 1. Finalidade

Esta vista identifica pontos em que a próxima decisão deixa uma perspectiva e passa para outra autoridade legítima.

Nenhum handoff é considerado validado apenas porque as superfícies de origem e destino existem. A evidência deve abranger a transição, os dados transferidos, o efeito, o retorno e a possibilidade de contestação.

## 2. Matriz governada

| IDs de transição | Origem e maturidade | Evento | Destino e maturidade | Autoridade | Evidência da transição | Retorno ou contestação | Lacuna |
|---|---|---|---|---|---|---|---|
| GKR-TRN-104; GKR-TRN-105 | Pessoa — validado na perspectiva solicitante | envia solicitação de participação | responsável do Coletivo — não materializado | UXA-056; UXA-066 | envio e estado pendente materializados na visão da Pessoa | cancelamento e acompanhamento na visão da Pessoa | operação do responsável ausente |
| GKR-TRN-106 | responsável do Coletivo — programado | solicita informação adicional | Pessoa — validado na perspectiva solicitante | UXA-056; UXA-066; UXA-067 | retorno materializado somente na visão da Pessoa | Pessoa pode revisar, responder ou não prosseguir | origem operacional não materializada |
| GKR-TRN-107 | Pessoa — validado na perspectiva solicitante | envia informação adicional | responsável do Coletivo — programado | UXA-056; UXA-067 | resposta materializada somente na visão da Pessoa | desistência permanece possível | fila operacional não materializada |
| GKR-TRN-108; GKR-TRN-109 | responsável do Coletivo — programado | aprova, recusa ou deixa expirar | Pessoa — validado na perspectiva solicitante | UXA-014; UXA-056; UXA-067 | resultado materializado somente na visão da Pessoa | recusa, cancelamento e expiração permanecem distintos | decisão do responsável e continuidade ausentes |
| GKR-TRN-206 | Organização — contratada | propõe relação ou apoio | Coletivo — contratado | UXA-019 | nenhuma superfície bilateral específica | retirada, negociação, recusa e ajuste contratados | materialização bilateral ausente |
| GKR-TRN-207; GKR-TRN-208; GKR-TRN-209 | Coletivo e Organização — contratados | avaliam, aprovam e revisam relação | autoridades bilaterais | UXA-019 | nenhuma superfície bilateral específica | revisão, pausa e encerramento contratados | operação bilateral ausente |
| GKR-TRN-202; GKR-TRN-203 | Organização — validado no cadastro | publica oportunidade | Pessoa — validado na consulta | UXA-004; UXA-008; UXA-013 | publicação e consulta existem em pacotes distintos | edição ou retirada pela Organização; retorno da Pessoa ao catálogo | integração ponta a ponta não examinada |
| GKR-TRN-204; GKR-TRN-205 | Pessoa — validado na consulta | acessa oportunidade | Organização ou destino identificado — parcial | UXA-004; UXA-007; UXA-012 | detalhe e destino apresentados no escopo existente | retorno à lista ou mapa conforme superfície | efeito externo não validado nesta seção |
| GKR-TRN-302 | anunciante — materializado | entrega promoção identificada | Pessoa exposta — validado localmente | UXA-038 | camada patrocinada identificada | ignorar, retornar ou seguir ação apresentada | integração completa com superfícies orgânicas |

## 3. Registro granular

O detalhamento individual está em [Registro Granular de Transições](transition-registry.md).

Esse registro acrescenta, por ID:

- origem e destino;
- participante e perspectiva;
- tipo de transição;
- condição e ação iniciadora;
- autoridade;
- efeito e dados transferidos;
- gate de autorização;
- reversibilidade;
- interrupção e tempo;
- evidência;
- estado da ligação;
- lacuna associada.

## 4. Regras de proteção

- origem materializada não presume destino materializado;
- retorno visível para a Pessoa não comprova a existência da operação do responsável;
- contrato bilateral não equivale a interface bilateral;
- nenhuma seta será criada por proximidade, ordem numérica ou conveniência narrativa;
- um ID estabiliza a referência documental, mas não implementa a transição.

## 5. Estado vigente

A UXA-074 aprovou esta matriz com ressalva não bloqueadora. A UXA-075 promoveu o documento para `active` como síntese governada dos handoffs prioritários.

A UXA-076 materializou o registro individual das transições, que permanece `draft` até validação específica. Esta matriz continua `active` como síntese e não passa a declarar cobertura exaustiva ou validação ponta a ponta.
