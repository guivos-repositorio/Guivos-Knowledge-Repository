---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.34.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
related:
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GKR-JOURNEY-DOMAIN-PROPAGATION-D4-001
  - UXA-070
  - UXA-080
  - UXA-085
  - UXA-090
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A3
  - UXA-100-A4
  - UXA-101
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne as jornadas da Pessoa, do Coletivo e da Organização para leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas. Ela não substitui contratos, wireframes, validações ou registros canônicos.

As vistas passam também a consumir explicitamente o eixo transversal dos Domínios de Evolução governado por `PAS-001-DOMAIN-MODEL-001` e reconciliado por `PAS-001-DOMAIN-RECON-001`.

## 2. Vistas disponíveis

- [Propagação dos Domínios de Evolução nas Jornadas — D4](evolution-domains-d4.md)
- [Galeria Visual Integrada de Telas](screen-gallery.md)
- [Planos, Comparação e Cobrança — Galeria Canônica](screen-gallery-plans-billing.md)
- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md)
- [Catálogo de Telas](screen-catalog.md)
- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e Continuidades Ausentes](gaps.md)

## 3. Sequência governada recente

```text
UXA-097 — compreensão inicial → primeira Tela Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — dez estados residuais Opportunity Boost
→ UXA-100/A1/A2/A3 — Planos materializados, validados e promovidos
→ UXA-101 — Detalhe → revisão consciente → BND-001
→ UXA-100-A4 — reconciliação controlada das origens voluntárias de Planos
```

Após essa sequência funcional, a arquitetura do Journey recebeu a canonização e a reconciliação dos Domínios de Evolução. A D4 executa exclusivamente sua propagação documental para as vistas integradas; não altera a ordem numérica das UXAs, não inicia V5 e não cria materialização visual.

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental proposto

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.34.0 | D4 |
| propagação dos Domínios de Evolução | `active` 1.0.0 | GKR-JOURNEY-DOMAIN-PROPAGATION-D4-001 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita preservada |
| Jornada da Pessoa | `draft` 0.17.0 | D4; origem de Planos A4; V4 UXA-101 |
| Jornada do Coletivo | `draft` 0.18.0 | D4; origem de Planos A4 |
| Jornada da Organização | `draft` 0.11.0 | D4; origem de Planos A4 |
| catálogo integrado | `active` | 118 SVGs canônicos |
| registro de superfícies | `active` 0.19.0 | 54 IDs |
| registro de transições | `active` 0.20.0 | 60 transições |
| galeria visual integrada | `active` | 118 SVGs canônicos |
| galeria de Planos | `active` | 9 SVGs canônicos |
| matriz por SVG | `active` | 118 associações / 31 perfis |
| registro de lacunas | `active` 0.28.0 | D5/V5 e demais continuidades permanecem separadas |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Domínios de Evolução nas Jornadas

As três vistas integradas passam a reconhecer explicitamente os nove IDs canônicos:

| ID | Domínio |
|---|---|
| `JED-001` | Saúde e Bem-estar |
| `JED-002` | Trabalho, Carreira e Estudos |
| `JED-003` | Vida Financeira |
| `JED-004` | Empreendedorismo e Projetos |
| `JED-005` | Relacionamentos e Vida Social |
| `JED-006` | Espiritualidade, Propósito e Valores |
| `JED-007` | Viagens, Lazer, Cultura e Novas Experiências |
| `JED-008` | Causas, Voluntariado e Contribuição |
| `JED-009` | Organização e Equilíbrio da Vida |

Regras transversais:

- os mesmos IDs são utilizados por Pessoa, Coletivo e Organização, com semântica adequada à natureza de cada participante;
- uma jornada pode ter `0..n` domínios relacionados;
- multidomínio é legítimo;
- `Ainda estou descobrindo` é estado de exploração, não `JED-010`;
- `other_unmapped` preserva área ainda não mapeada;
- domínio candidato não equivale a domínio confirmado;
- domínio não é score, diagnóstico, prioridade humana, autoridade ou prova de evolução;
- mesmo domínio entre participantes não cria match, relevância, compartilhamento ou autorização automática;
- D4 é documental e não cria superfície, transição ou SVG.

A interpretação detalhada por participante está em [Propagação dos Domínios de Evolução nas Jornadas — D4](evolution-domains-d4.md).

## 6. Continuidade de oportunidades após UXA-101

```text
ORG-003 → TRN-203 → PER-201
PER-201 ↔ TRN-210 ↔ PER-202
PER-201/PER-202 → TRN-204/211 → PER-203
PER-203 → revisão consciente no mesmo estado → TRN-205 → BND-001
```

- UXA-098 valida `TRN-203`, `204`, `210` e `211`;
- UXA-101 valida `TRN-205` até a fronteira de autoridade da Guivos;
- `BND-001` não possui tela Guivos;
- qualquer resultado posterior pertence ao terceiro até reconciliação autorizada e comprovada.

## 7. Etapa transversal de Planos preservada e conectada

A espinha dorsal comercial permanece:

```text
*-301 Planos e comparação
├── upgrade → *-302 revisão → *-304 resultado/recuperação → *-301
├── downgrade/cancelamento → *-303 → *-304 → *-301
└── quando autoatendimento não for suficiente → BND-002
```

A origem voluntária possui identidade canônica:

```text
PER-009 ↔ PER-301   — TRN-406/407 contratadas
COL-002 ↔ COL-301   — TRN-417/418 integralmente validadas
ORG-001 ↔ ORG-301   — TRN-427/428 integralmente validadas
```

Abrir Planos não seleciona tier, não inicia cobrança e não altera consentimento, capacidade ou relevância. `PER-009` permanece sem SVG dedicado; sua futura materialização é gap separado.

A nomenclatura vigente é:

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`;
- Guivos Business: `Start · Growth · Scale · Enterprise`, como Produto Especializado separado.

`BND-002` é fronteira genérica de contratação/dimensionamento assistido e não plano. As transições comerciais internas continuam localmente validadas; `TRN-416/426` permanecem parciais. Cobrança real e processo posterior a `BND-002` continuam fora do escopo.

## 8. Cobertura canônica

A D4 não altera contagens funcionais ou visuais.

| Indicador | Resultado |
|---|---:|
| SVGs canônicos | **118** |
| associações | **118** |
| perfis | **31** |
| validações vigentes | **118** |
| pendentes | **0** |
| superfícies/estados/fronteiras | **54** |
| transições | **60** |
| IDs com referência visual | **42 de 54** |
| responsabilidades sem SVG dedicado | **10** |
| fronteiras sem tela | **2** |

## 9. Separações obrigatórias

- Domínio de Evolução não equivale a tela, objetivo, score ou prova de evolução;
- mesmo domínio entre participantes não equivale a match automático;
- Planos canonicamente registrado não equivale a checkout implementado;
- navegar para Planos não equivale a contratar;
- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- `BND-002` ≠ Enterprise ou Scale;
- revisão de saída em `PER-203` não cria tela nova;
- validação até `BND-001` não valida sistema de terceiro;
- pagar um plano ou patrocínio não altera relevância funcional;
- `COM-005` validado não promove automaticamente `TRN-305`;
- validação documental não equivale a implementação técnica.

## 10. Estado da frente

V1, V2, V3 e V4 estão encerradas nos limites declarados. A identidade da origem voluntária de Planos foi reconciliada pela UXA-100-A4. D4 propaga documentalmente `JED-001..JED-009` para Pessoa, Coletivo e Organização, preservando multidomínio, `Ainda estou descobrindo` e `other_unmapped`.

A materialização dos Domínios na experiência permanece **D5 pendente**. V5/UXA-102 não foi iniciada. D6 (grafo), D7 (Public Canon) e Engenharia de Produto permanecem fora desta frente.
