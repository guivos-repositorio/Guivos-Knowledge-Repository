---
id: GKR-JOURNEY-SURFACE-DETAIL-COLLECTIVE-001
title: Detalhamento Obrigatório das Superfícies do Coletivo
status: active
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: GKR-JOURNEY-SURFACE-REGISTRY-001
related:
  - UXA-070
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
normative: false
---

# Detalhamento Obrigatório das Superfícies do Coletivo

## 1. Finalidade

Este arquivo integra o `GKR-JOURNEY-SURFACE-REGISTRY-001` e registra campos obrigatórios por identificador. Ele não altera a contagem de entradas.

A UXA-088 materializou `GKR-SURF-COL-003` em sete estados desktop e a UXA-089 reformulou seis deles e validou funcionalmente toda a família.

## 2. Campos por identificador

| ID | Artefato canônico e caminho | Versão | Entrada | Decisão principal | Saída | Dados e conteúdos | Gate | Reversibilidade | Supersessão | Continuidade | Lacuna | Observação de escopo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GKR-SURF-COL-001 | UXA-016 e UXA-062 | indeterminado | criação ou acesso público | consultar presença pública ou acessar visão prevista | descoberta e participação | identidade, propósito, atividades e estados conforme perspectiva | público para consulta; autoridade para áreas protegidas | retornar ou encerrar consulta | nenhuma identificada | parcial | separação entre vista pública e operação | não substitui Visão Geral do Responsável |
| GKR-SURF-COL-002 | UXA-086; validação UXA-087 | materialização 0.1.0; validação 0.1.0 | acesso protegido com representação válida | compreender momento operacional e escolher área autorizada | GKR-TRN-112 para solicitações | identidade, propósito, representação, escopo e sínteses no limite necessário | representação válida e escopo concedido | permanecer, adiar, contestar prioridade ou retornar | nenhuma identificada | parcial; destino validado como superfície, transição ainda não validada | continuidade para COL-003 | referência desktop validada; não substitui gestão especializada |
| GKR-SURF-COL-003 | UXA-088 — `docs/experience-architecture/uxa-088-collective-request-management-low-fidelity-wireframes.md`; validação UXA-089; efeitos na Pessoa em UXA-066/067 | materialização 0.2.0; validação 0.1.0 | GKR-TRN-105 ou GKR-TRN-112; resposta adicional via GKR-TRN-107 | analisar solicitação e escolher aguardar, pedir informação, aprovar ou recusar dentro da autoridade | GKR-TRN-106, GKR-TRN-108 ou GKR-TRN-109; permanência na fila quando não houver decisão | dados autorizados da solicitação; estado; referência temporal; critérios previamente apresentados; fundamento; resposta adicional; dados protegidos mínimos quando aplicável | representação válida; finalidade limitada; autoridade específica verificada; confirmação antes de aprovação ou recusa | voltar sem decidir; aguardar; pedir informação; descartar rascunho; interromper por autoridade insuficiente | referências na perspectiva da Pessoa não são supersedidas | superfície validada; continuidade bilateral ainda parcial | handoffs bilaterais e continuidade pós-aprovação para PER-106 | sete SVGs desktop validados; acessibilidade separada de elegibilidade; cancelamento pela Pessoa e expiração são eventos refletidos |
| GKR-SURF-COL-004 | ausente; autoridade UXA-059 | indeterminado | vínculo formado | indeterminado | gestão, saída ou contestação | indeterminado | papel e autoridade esperados; não materializados | indeterminado | nenhuma identificada | ausente | continuidade interna | não iniciado pela UXA-089 |
| GKR-SURF-COL-005 | ausente; autoridade UXA-058/059 | indeterminado | vínculo e autoridade | indeterminado | atualizações aos participantes | indeterminado | papel, audiência e finalidade esperados | indeterminado | nenhuma identificada | ausente | superfície e regras operacionais | não iniciado pela UXA-089 |
| GKR-SURF-COL-006 | UXA-059 | indeterminado | governança interna | indeterminado por atividade | resultados e próximas decisões | conteúdos dispersos | autoridade contextual esperada | indeterminado | nenhuma identificada | não examinado | matriz operacional integrada | não iniciado pela UXA-089 |
| GKR-SURF-COL-007 | UXA-058 | indeterminado | evento protegido | avaliar evento dentro de competência limitada | decisão ou encaminhamento | evidências mínimas, relato, estado e encaminhamento | autoridade protegida; finalidade limitada | contestar, corrigir ou encaminhar conforme contrato | nenhuma identificada | não examinado | fluxo protegido completo | não iniciado pela UXA-089 |
| GKR-SURF-COL-008 | ausente; autoridade UXA-019 | indeterminado | proposta institucional | avaliar, negociar, aceitar ou recusar proposta | negociação e decisão bilateral | finalidade, compromissos, recursos, limites e dados previstos | autoridade do responsável e aprovação bilateral | recusar, ajustar, pausar ou encerrar conforme contrato | nenhuma identificada | ausente | relação Organização–Coletivo | não iniciado pela UXA-089 |

## 3. Regras preservadas

- valores sem evidência permanecem `indeterminado`, `ausente` ou `não examinado`;
- validação de `COL-003` não autoriza completar `COL-004` a `COL-008` por analogia;
- efeitos validados em ambas as perspectivas não equivalem a validação do handoff como conjunto;
- autoridade é verificada por escopo concedido e não por autodeclaração;
- autoridade insuficiente impede a decisão e não concede dados adicionais.

## 4. Estado

O detalhamento está `active` 0.6.0. `COL-002` e `COL-003` estão validadas no escopo de suas superfícies. A continuidade bilateral e a Jornada do Coletivo continuam incompletas.
