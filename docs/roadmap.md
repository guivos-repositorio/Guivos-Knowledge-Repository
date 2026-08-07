---
id: ROADMAP-12.59.0
title: Roadmap Arquitetural — Visão Geral do Responsável Materializada
status: active
version: 12.59.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.58.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-014
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-037
  - UXA-055
  - UXA-056
  - UXA-069
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.73
---

# Roadmap Arquitetural — Visão Geral do Responsável Materializada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Visão Geral do Responsável materializada; validação pendente | UXA-086; M7.73 |
| Registros granulares | 40 superfícies e 37 transições | UXA-080; UXA-086 |
| Galeria visual | `active` 0.6.0; 98 SVGs | UXA-086 |
| página de Coletivos | `active` 0.4.0 | UXA-086 |
| matriz por SVG | 98 arquivos associados a 24 perfis; `active` 0.4.0 | UXA-086 |
| validações funcionais registradas | 87 | pacotes de origem |
| pendentes de validação específica | 11 | UXA-055; UXA-086 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência das Jornadas Integradas

```text
UXA-070 a UXA-075 — estruturação e promoção seletiva das Jornadas Integradas
→ UXA-076 a UXA-080 — registros granulares e promoção dos instrumentos
→ UXA-081 — galeria visual e auditoria
→ UXA-082 — validação não aprovada e priorização por dependência
→ UXA-083 — reformulação da galeria e matriz por SVG
→ UXA-084 — revalidação aprovada com ressalvas
→ UXA-085 — promoção controlada dos instrumentos visuais
→ UXA-086 — materialização de GKR-SURF-COL-002
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-086

| Dimensão | Resultado |
|---|---|
| superfície materializada | GKR-SURF-COL-002 — Visão Geral do Responsável |
| canal inicial | computador |
| novos SVGs | 1 |
| SVGs totais | 98 |
| novo perfil de rastreabilidade | R24 |
| perfis documentais totais | 24 |
| validação funcional do novo SVG | pendente |
| GKR-TRN-112 | parcial; não validada |
| GKR-SURF-COL-003 | não materializada |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Ressalvas preservadas

- 13 responsabilidades permanecem sem SVG dedicado;
- uma fronteira permanece sem tela por definição;
- dez estados da UXA-055 continuam sem validação específica;
- a referência da UXA-086 também aguarda validação específica;
- `GKR-TRN-112` possui apenas a origem materializada;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- materialização não equivale a validação funcional.

## 6. Trilha documental vigente

```text
instrumentos visuais promovidos
→ primeira lacuna priorizada materializada pela UXA-086
→ validar funcionalmente GKR-SURF-COL-002 em pacote próprio
→ somente depois decidir sobre correções, promoção ou avanço para GKR-SURF-COL-003
```

Materialização e validação continuam atos governados distintos.

## 7. Prioridade de Coletivos

```text
GKR-SURF-COL-002 — materializada; validação pendente
→ GKR-SURF-COL-003 — gestão completa de solicitações ainda ausente
→ GKR-SURF-PER-106 — Meus Coletivos
→ GKR-SURF-PER-107 — Central de Atualizações
→ GKR-SURF-PER-108 — Início do Participante
```

O avanço para `COL-003` não é autorizado pela materialização da UXA-086.

## 8. Dívidas de validação

- UXA-086 — Visão Geral do Responsável do Coletivo;
- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 9. Limites

A UXA-086 não materializa a fila completa de solicitações, não promove jornadas, não inicia protótipo, teste com pessoas, aplicação, motor ou Engenharia de Produto.

## 10. Próxima iniciativa possível

> **UXA-087 — Validação Funcional da Visão Geral do Responsável do Coletivo**

A UXA-087 depende de autorização separada e não é iniciada por este pacote.
