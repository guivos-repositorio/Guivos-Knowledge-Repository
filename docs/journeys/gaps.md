---
id: GKR-JOURNEYS-GAPS-001
title: Fila de Lacunas das Jornadas Integradas
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
depends_on:
  - UXA-071
related:
  - UXA-072
  - GKR-JOURNEYS-001
normative: false
---

# Fila de Lacunas das Jornadas Integradas

## 1. Regra

Lacuna é uma ausência conhecida de superfície, transição, autoridade, validação ou cobertura. Ela não será ocultada por tela genérica, conteúdo fictício ou seta presumida.

## 2. Registro prioritário

| ID | Lacuna | Participante | Tipo | Impacto | Dependência | Estado |
|---|---|---|---|---|---|---|
| JG-001 | `Meus Coletivos` | Pessoa/Coletivo | superfície ausente | interrompe continuidade após aprovação | UXA-059 | não iniciada |
| JG-002 | Central de Atualizações | Pessoa/Coletivo | superfície ausente | fragmenta mudanças e comunicações | JG-001 | não iniciada |
| JG-003 | Início do Participante | Pessoa/Coletivo | reformulação | não há entrada recorrente coerente | JG-001; JG-002 | não iniciada |
| JG-004 | Visão Geral do Responsável | Coletivo | superfície ausente | autoridade e trabalho ficam dispersos | UXA-059 | não iniciada |
| JG-005 | matriz visual institucional completa | Organização | cobertura | impede avaliar a jornada institucional ponta a ponta | UXA-014 a UXA-019 | não iniciada |
| JG-006 | fluxo bilateral Organização–Coletivo | Organização/Coletivo | transição visual ausente | negociação, revisão e saída não são inspecionáveis | UXA-019 | não iniciada |
| JG-007 | dez estados residuais do Boost | sobreposição comercial | validação pendente | exceções podem conter falhas funcionais | UXA-055 | materializados; não validados |
| JG-008 | validação do mapa integrado | transversal | validação pendente | sequência e autoridade ainda não foram examinadas como conjunto | UXA-071 | prevista em UXA-072 |
| JG-009 | continuidade ampla após compreensão inicial | Pessoa | cobertura parcial | Tela Hoje, oportunidades e demais jornadas não estão reconciliadas | UXA-002 a UXA-033 | programada |
| JG-010 | saída e encerramento transversais | todos | transição parcial | cancelamento, pausa e encerramento variam entre famílias | contratos aplicáveis | indeterminada |
| JG-011 | acessibilidade técnica da seção | transversal | validação técnica | estrutura ainda precisa de teste assistivo | UXA-072 | não iniciada |
| JG-012 | atualização automática de referências | governança | automação ausente | mudanças de versão exigem reconciliação manual | Engenharia futura | não iniciada |

## 3. Priorização sugerida

### P0 — continuidade interrompida

- JG-001 — `Meus Coletivos`;
- JG-002 — Central de Atualizações;
- JG-003 — Início do Participante;
- JG-008 — validação do mapa integrado.

### P1 — autoridade e operação

- JG-004 — Visão Geral do Responsável;
- JG-005 — matriz institucional;
- JG-006 — relação bilateral;
- JG-010 — saídas transversais.

### P2 — cobertura e qualidade

- JG-007 — estados residuais do Boost;
- JG-009 — continuidade pessoal ampla;
- JG-011 — acessibilidade;
- JG-012 — atualização automatizada.

A priorização não inicia nenhum pacote automaticamente.

## 4. Critério de encerramento

Uma lacuna somente pode ser encerrada quando houver autoridade identificada, materialização ou decisão explícita de não materializar, transições de entrada e saída, dados e gates definidos, validação aplicável e atualização da seção integrada e dos registros globais.
