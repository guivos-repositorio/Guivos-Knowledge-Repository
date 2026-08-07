---
id: GKR-JOURNEY-HANDOFFS-001
title: Handoffs entre Participantes
status: active
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
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
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Handoffs entre Participantes

## 1. Finalidade

Esta vista identifica pontos em que a próxima decisão deixa uma perspectiva e passa para outra autoridade legítima.

Nenhum handoff é considerado validado apenas porque as superfícies de origem e destino existem. A evidência deve abranger a transição, dados transferidos, efeito, retorno, interrupção e contestação.

## 2. Matriz governada

| IDs de transição | Origem e maturidade | Evento | Destino e maturidade | Autoridade | Evidência da transição | Retorno ou contestação | Estado/lacuna |
|---|---|---|---|---|---|---|---|
| GKR-TRN-104 | Pessoa — PER-104 validada | envia solicitação de participação | PER-105 validada | UXA-056 | UXA-065; UXA-067 | cancelamento e acompanhamento | parcial; continuidade entre pacotes |
| GKR-TRN-105 | Pessoa solicitante | solicitação fica disponível para análise | COL-003 validada | UXA-056; UXA-059 | UXA-067; UXA-089; UXA-090 | cancelamento/expiração tornam análise obsoleta | **integralmente validada** |
| GKR-TRN-106 | COL-003 validada | solicita informação adicional | PER-105 validada | UXA-056 | UXA-067; UXA-089; UXA-090 | responder, não informar, contestar ou cancelar | **integralmente validada** |
| GKR-TRN-107 | PER-105 validada | envia informação adicional | COL-003 validada | UXA-056 | UXA-067; UXA-089; UXA-090 | editar antes do envio, desistir; processo encerrado não reabre | **integralmente validada** |
| GKR-TRN-109 | COL-003 validada | recusa solicitação | PER-105 validada | UXA-014; UXA-056 | UXA-067; UXA-089; UXA-090 | fundamento proporcional; nova exploração posterior | **integralmente validada** |
| GKR-TRN-108 | COL-003 validada | aprova e forma vínculo; resultado é mostrado em PER-105 | PER-106 validada | UXA-014; UXA-056 | UXA-089; UXA-092 | Pessoa pode optar por `Agora não`; vínculo já está formado; preferências preservadas | **integralmente validada** |
| GKR-TRN-110 | PER-106 validada | acessar atualizações do vínculo | PER-107 ausente | UXA-056; UXA-059 | origem validada em UXA-092 | permanecer/retornar a Meus Coletivos | **parcial**; destino ausente |
| GKR-TRN-206 | Organização — contratada | propõe relação ou apoio | Coletivo — contratado | UXA-019 | nenhuma superfície bilateral específica | retirada, negociação, recusa e ajuste | materialização bilateral ausente |
| GKR-TRN-207; 208; 209 | Coletivo e Organização — contratados | avaliam, aprovam e revisam relação | autoridades bilaterais | UXA-019 | nenhuma superfície bilateral específica | revisão, pausa e encerramento | operação bilateral ausente |
| GKR-TRN-202; 203 | Organização | publica oportunidade | Pessoa | UXA-004 | publicação e consulta em pacotes distintos | edição/retirada; retorno da Pessoa | integração ponta a ponta não examinada |
| GKR-TRN-204; 205 | Pessoa | acessa oportunidade | destino identificado | UXA-004; UXA-007 | detalhe e fronteira apresentados | retorno a lista ou mapa | efeito externo não validado |
| GKR-TRN-302 | anunciante | entrega promoção identificada | Pessoa exposta | UXA-038 | camada patrocinada identificada | ignorar, retornar ou seguir ação | integração orgânico–patrocinado parcial |

## 3. Continuidade pós-aprovação

A UXA-092 valida a sequência documental:

```text
COL-003 — aprovação confirmada
→ resultado aprovado em PER-105
→ vínculo já formado
→ Pessoa escolhe “Ver em Meus Coletivos” ou “Agora não”
→ PER-106 — mesmo vínculo confirmado visível quando a navegação ocorre
```

A navegação é opcional e não funciona como gate da aprovação. `TRN-108` está integralmente validada no escopo documental; a continuidade seguinte, `TRN-110`, permanece parcial por ausência de `PER-107`.

## 4. Registro granular

O detalhamento individual continua no [Registro Granular de Transições](transition-registry.md), que é a referência por ID para origem, destino, autoridade, dados, gate, reversibilidade, interrupção, tempo, evidência e estado.

## 5. Regras de proteção

- origem materializada não presume destino validado;
- resultado visível não comprova continuidade validada sem gate próprio;
- navegação posterior não deve ser confundida com efeito já confirmado;
- contrato bilateral não equivale a interface bilateral;
- nenhuma seta será criada por proximidade, ordem numérica ou conveniência narrativa;
- um ID estabiliza a referência documental, mas não implementa a transição;
- uma versão visual reformulada exige revalidação;
- validação integral documental não equivale a implementação técnica.

## 6. Estado vigente

A matriz permanece `active` como síntese governada. Seis handoffs do fluxo de solicitação estão integralmente validados por UXA-090/092: `TRN-105`, `106`, `107`, `108`, `109` e `112`.

`TRN-110` permanece parcial enquanto `PER-107 — Central de Atualizações` estiver ausente. A UXA-093 não é iniciada por esta sincronização.
