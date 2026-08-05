---
id: UXA-073
title: Reformulação, Navegação e Sincronização das Jornadas Integradas
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - UXA-071
  - UXA-072
  - GKR-JOURNEYS-001
related:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-SCENARIOS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.47.0
  - M7.72
normative: false
---

# Reformulação, Navegação e Sincronização das Jornadas Integradas

## 1. Finalidade

A UXA-073 executa a remediação obrigatória determinada pela UXA-072 sobre a primeira materialização documental das **Jornadas Integradas**.

O pacote corrige a acessibilidade da seção no GKR, sincroniza os registros centrais e reformula os mapas para separar evidências que anteriormente apareciam combinadas.

A UXA-073 não declara as jornadas funcionalmente validadas. Ela prepara uma versão reformulada e rastreável para nova validação em pacote separado.

## 2. Base e escopo

Base de criação: `main` em `6756a12b2e5f907277f6fbe282ef508211abce57`.

Foram reformulados:

1. `docs/journeys/index.md`;
2. `docs/journeys/person.md`;
3. `docs/journeys/collective.md`;
4. `docs/journeys/organization.md`;
5. `docs/journeys/handoffs.md`;
6. `docs/journeys/scenarios.md`;
7. `docs/journeys/screen-catalog.md`;
8. `docs/journeys/gaps.md`.

Foram sincronizados:

- `mkdocs.yml`;
- `docs/project/current-state-register.md`;
- `docs/roadmap.md`;
- `docs/experience-architecture/index.md`.

## 3. Modelo de evidência obrigatório

A reformulação separa cinco dimensões:

| Dimensão | Regra |
|---|---|
| maturidade primária | um único estado controlado da UXA-070 |
| autoridade contratual | documento que governa a responsabilidade |
| referência materializada | documento, wireframe ou SVG existente |
| evidência de validação | pacote que validou a referência materializada |
| continuidade integrada | validada, parcial, ausente ou não examinada |

```text
cobertura das superfícies
≠ cobertura das transições
≠ validação da jornada integrada
```

## 4. Correções executadas

| Achado da UXA-072 | Correção da UXA-073 | Estado |
|---|---|---|
| F01 — seção ausente da navegação | seção de primeiro nível adicionada ao `mkdocs.yml` | corrigido |
| F02 — Registro do Estado Atual contraditório | GKR-STATE-001 atualizado para versão 2.00.0 | corrigido |
| F03 — roadmap desatualizado | ROADMAP-12.47.0 publicado | corrigido |
| F04 — índice UXA desatualizado | UXA-000 atualizado para versão 0.67.0 | corrigido |
| F05 — maturidades compostas | campos de evidência separados | corrigido |
| F06 — tela validada confundida com jornada validada | conclusões permitidas e proibidas registradas | corrigido |
| F07 — handoffs assimétricos | maturidade de origem e destino separada | corrigido |
| F08 — cenários excedendo evidência | cabeçalhos de evidência adicionados aos seis cenários | corrigido |
| F09 — catálogo sem continuidade integrada | entradas e saídas integradas registradas separadamente | corrigido |
| F10 — status documental inconsistente | mapas mantidos em `draft`; lacunas declaradas observacionais e `active` | corrigido |

## 5. Estado dos artefatos após a reformulação

| Artefato | Versão | Status | Interpretação permitida |
|---|---:|---|---|
| visão geral das Jornadas Integradas | 0.2.0 | draft | seção reformulada e navegável |
| jornada da Pessoa | 0.2.0 | draft | evidências separadas; validação pendente |
| jornada do Coletivo | 0.2.0 | draft | assimetrias explícitas; validação pendente |
| jornada da Organização | 0.2.0 | draft | cobertura institucional separada; validação pendente |
| handoffs | 0.2.0 | draft | origem, destino, retorno e lacuna separados |
| cenários | 0.2.0 | draft | hipóteses documentais com limites explícitos |
| catálogo | 0.2.0 | draft | superfícies e transições não confundidas |
| lacunas | 0.2.0 | active | registro observacional, não promocional |

## 6. Navegação

`Jornadas Integradas` passa a existir como seção própria de primeiro nível no GKR publicado, com acesso a:

- visão geral;
- Pessoa;
- Coletivo;
- Organização;
- handoffs;
- cenários;
- catálogo de telas;
- lacunas.

A Arquitetura da Experiência também referencia a sequência UXA-070 a UXA-073.

## 7. Sincronização do estado global

O estado oficial passa a reconhecer:

```text
UXA-070 — programa funcional concluído
→ UXA-071 — primeira materialização integrada
→ UXA-072 — validação não aprovada até reformulação
→ UXA-073 — reformulação, navegação e sincronização executadas
→ UXA-074 — nova validação funcional, ainda não iniciada
```

## 8. Critérios para a próxima validação

A futura UXA-074 deverá verificar, no mínimo:

1. presença e ordem da seção na navegação publicada;
2. ausência de contradições entre GKR-STATE-001, roadmap e UXA-000;
3. uso de um único estado de maturidade primária por linha;
4. separação entre autoridade, materialização e validação;
5. explicitação das continuidades parciais, ausentes e não examinadas;
6. assimetrias de handoff sem falsa equivalência bilateral;
7. cenários limitados à evidência disponível;
8. catálogo distinguindo superfícies de transições;
9. status `draft` preservado para mapas ainda não revalidados;
10. registro de lacunas permanecendo observacional.

## 9. Limites preservados

A UXA-073 não cria:

- novas telas de produto;
- novos SVGs ou wireframes;
- `Meus Coletivos`;
- Central de Atualizações;
- Visão Geral do Responsável;
- fluxo bilateral Organização–Coletivo;
- protótipo navegável;
- aplicação ou motor de simulação;
- teste com pessoas;
- modelo de IA;
- Engenharia de Produto.

Nenhum contrato, wireframe ou SVG canônico foi modificado.

## 10. Resultado controlado

> **A remediação documental foi executada. A validação funcional continua pendente.**

A integração deste pacote não promove os mapas para `active` e não inicia automaticamente a UXA-074.

## 11. Próxima transição autorizável

**UXA-074 — Nova Validação Funcional das Jornadas Integradas Reformuladas**, mediante autorização separada.
