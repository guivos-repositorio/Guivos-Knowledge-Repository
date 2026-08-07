---
id: ROADMAP-12.60.0
title: Roadmap Arquitetural — Visão Geral do Responsável Validada
status: active
version: 12.60.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.59.0
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
  - UXA-087
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.74
---

# Roadmap Arquitetural — Visão Geral do Responsável Validada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Visão Geral do Responsável reformulada e validada | UXA-087; M7.74 |
| Registros granulares | 40 superfícies e 37 transições | UXA-080; UXA-087 |
| Galeria visual | `active` 0.7.0; 98 SVGs | UXA-087 |
| página de Coletivos | `active` 0.5.0 | UXA-087 |
| matriz por SVG | 98 arquivos associados a 24 perfis; `active` 0.5.0 | UXA-087 |
| validações funcionais registradas | 88 | pacotes de origem e UXA-087 |
| pendentes de validação específica | 10 | UXA-055 |
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
→ UXA-087 — reformulação e validação funcional de GKR-SURF-COL-002
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-087

| Dimensão | Resultado |
|---|---|
| superfície validada | GKR-SURF-COL-002 — Visão Geral do Responsável |
| veredito | aprovada após reformulação controlada |
| SVGs adicionados | 0 |
| SVGs reformulados | 1 |
| SVGs totais | 98 |
| perfis documentais totais | 24 |
| validações funcionais | 88 |
| pendentes | 10, exclusivamente UXA-055 |
| GKR-TRN-112 | parcial; origem validada, destino ausente |
| GKR-SURF-COL-003 | não materializada |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Reformulações aprovadas

A UXA-087 corrige quatro pontos do wireframe sem alterar sua responsabilidade:

- estado e escopo de autoridade explícitos;
- prazo verificável na atenção principal;
- adiamento e contestação legítimos sem penalidade;
- retorno explícito ao contexto anterior.

## 6. Ressalvas preservadas

- 13 responsabilidades permanecem sem SVG dedicado;
- uma fronteira permanece sem tela por definição;
- dez estados da UXA-055 continuam sem validação específica;
- `GKR-TRN-112` possui origem validada, mas destino operacional ausente;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- validação de uma superfície não equivale a jornada validada.

## 7. Trilha documental vigente

```text
GKR-SURF-COL-002 materializada
→ GKR-SURF-COL-002 reformulada e validada
→ GKR-SURF-COL-003 permanece próxima lacuna de materialização
→ materializar GKR-SURF-COL-003 somente mediante autorização separada
→ validar a operação e o handoff em pacote posterior
```

Materialização, validação de superfície e validação de transição continuam atos governados distintos.

## 8. Prioridade de Coletivos

```text
GKR-SURF-COL-002 — validada
→ GKR-SURF-COL-003 — gestão completa de solicitações ainda ausente
→ GKR-SURF-PER-106 — Meus Coletivos
→ GKR-SURF-PER-107 — Central de Atualizações
→ GKR-SURF-PER-108 — Início do Participante
```

O avanço para `COL-003` não é autorizado automaticamente pela UXA-087.

## 9. Dívidas de validação e materialização

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- gestão completa de solicitações do responsável ainda sem materialização.

## 10. Limites

A UXA-087 não materializa a fila completa de solicitações, não promove jornadas, não inicia protótipo, teste com pessoas, aplicação, motor ou Engenharia de Produto.

## 11. Próxima iniciativa possível

> **UXA-088 — Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo (`GKR-SURF-COL-003`)**

A UXA-088 depende de autorização separada e não é iniciada por este pacote.
