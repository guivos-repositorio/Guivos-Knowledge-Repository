---
id: ROADMAP-12.54.0
title: Roadmap Arquitetural — Galeria Visual Integrada Materializada
status: active
version: 12.54.0
owner: Guivos
last_updated: 2026-08-05
supersedes_partial:
  - ROADMAP-12.53.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.72
---

# Roadmap Arquitetural — Galeria Visual Integrada Materializada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | galeria única criada para inspeção dos 97 SVGs e auditoria de cobertura granular | UXA-081; M7.72 |
| Registros granulares | 40 superfícies e 37 transições em instrumentos `active` | UXA-080 |
| Galeria visual | `draft` 0.1.0; aguarda revisão funcional e visual | UXA-081 |
| SVGs auditados | 97 existentes; 87 validados; 10 pendentes | UXA-081 |
| cobertura granular visual | 25 de 40 IDs | UXA-081 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência das Jornadas Integradas

```text
UXA-070 — programa funcional
→ UXA-071 — seção integrada
→ UXA-072 — validação não aprovada
→ UXA-073 — reformulação
→ UXA-074 — revalidação
→ UXA-075 — promoção seletiva
→ UXA-076 — registros granulares
→ UXA-077 — validação bloqueada
→ UXA-078 — correções
→ UXA-079 — revalidação granular
→ UXA-080 — promoção dos instrumentos
→ UXA-081 — galeria visual e auditoria
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-081

| Entrega | Estado |
|---|---|
| Galeria Visual Integrada de Telas | criada em `draft` 0.1.0 |
| Catálogo Integrado de Telas | sincronizado para `active` 0.6.0 |
| Registro de Lacunas | sincronizado para `active` 0.6.0 |
| 97 SVGs | incorporados por referência |
| 87 SVGs validados | identificados |
| 10 SVGs da UXA-055 | preservados como pendentes |
| 25 IDs com cobertura visual | identificados |
| 14 responsabilidades sem SVG | identificadas |
| fronteira externa sem tela | preservada |

## 5. Prioridades evidenciadas

A auditoria não escolhe automaticamente uma lacuna, mas evidencia três blocos:

### Bloco A — continuidade de Coletivos

- Visão Geral do Responsável;
- gestão bilateral de solicitações;
- Meus Coletivos;
- Central de Atualizações;
- Início do Participante.

### Bloco B — relações institucionais

- proposta Organização–Coletivo;
- negociação bilateral;
- relação ativa e revisão;
- resultados e evidências institucionais.

### Bloco C — continuidades existentes ainda não validadas

- compreensão inicial → Tela Hoje;
- publicação → mapa/lista/detalhe;
- efeito externo;
- erros, retornos e interrupções;
- dez estados residuais da UXA-055.

A ordem entre os blocos dependerá de validação e decisão governada.

## 6. Limites

A UXA-081 não:

- cria novas telas;
- modifica SVGs;
- fecha lacunas;
- promove jornadas;
- inicia protótipo;
- inicia teste com pessoas;
- inicia aplicação ou Engenharia de Produto.

## 7. Próxima iniciativa possível

> **UXA-082 — Validação Funcional e Visual da Galeria Integrada e Priorização Governada das Lacunas**

O objetivo futuro será verificar assertividade visual, coerência entre sequências e selecionar a próxima lacuna com critérios explícitos.

A UXA-082 depende de autorização separada.

## 8. Regra de autorização

A integração da UXA-081 registrará somente a galeria e a auditoria. Ela não iniciará a UXA-082 nem qualquer materialização de lacuna.
