---
id: ROADMAP-12.57.0
title: Roadmap Arquitetural — Galeria Revalidada com Ressalvas e Aguardando Promoção
status: active
version: 12.57.0
owner: Guivos
last_updated: 2026-08-06
supersedes_partial:
  - ROADMAP-12.56.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.72
---

# Roadmap Arquitetural — Galeria Revalidada com Ressalvas e Aguardando Promoção

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | galeria e matriz revalidadas com ressalvas no escopo documental de inspeção | UXA-084; M7.72 |
| Registros granulares | 40 superfícies e 37 transições em instrumentos `active` | UXA-080 |
| Galeria visual | `draft` 0.4.0; aprovada com ressalvas | UXA-084 |
| páginas visuais | cinco páginas `draft` 0.2.0; revalidadas como conjunto | UXA-084 |
| matriz por SVG | 97 arquivos associados a 23 perfis; `draft` 0.2.0; aprovada com ressalvas | UXA-084 |
| SVGs auditados | 97 existentes; 87 validados localmente; 10 pendentes | UXA-081 a UXA-084 |
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
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-084

| Dimensão | Resultado |
|---|---|
| ordem da Pessoa | aprovada |
| Home e Tela Hoje | separação aprovada |
| rota entre páginas | aprovada |
| rastreabilidade por SVG | 97 associações confirmadas |
| perfis documentais | 23; aceitos com ressalva de agregação |
| versões documentais | sincronizadas |
| SVGs modificados | 0 |
| novas telas | 0 |
| promoção da galeria | não executada |

## 5. Ressalvas preservadas

- 14 responsabilidades sem SVG dedicado;
- uma fronteira sem tela por definição;
- dez estados da UXA-055 sem validação específica;
- continuidades entre pacotes parciais ou não examinadas;
- perfis agregados não substituem análise exclusiva por estado;
- aprovação do instrumento não equivale a jornada validada.

## 6. Próxima trilha documental

```text
promover a galeria e a matriz somente por ato separado
→ manter lacunas e dívidas de validação abertas
→ iniciar, em ato posterior e independente, a primeira lacuna priorizada
```

Promoção e materialização continuam atos governados distintos.

## 7. Prioridade futura de materialização

```text
GKR-SURF-COL-002 — Visão Geral do Responsável
→ GKR-SURF-COL-003 — gestão completa de solicitações
→ GKR-SURF-PER-106 — Meus Coletivos
→ GKR-SURF-PER-107 — Central de Atualizações
→ GKR-SURF-PER-108 — Início do Participante
```

Nenhuma dessas superfícies foi iniciada pela UXA-084.

## 8. Dívidas de validação em trilha própria

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 9. Limites

A UXA-084 não modifica SVGs, não cria telas, não promove jornadas, não fecha lacunas, não inicia protótipo, teste com pessoas, aplicação ou Engenharia de Produto.

## 10. Próxima iniciativa possível

> **UXA-085 — Promoção Controlada da Galeria Visual Integrada e Sincronização Pós-Revalidação**

A UXA-085 poderá promover somente os instrumentos aprovados, preservando todas as ressalvas e ausências.

A etapa depende de autorização separada.
