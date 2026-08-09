---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.38.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
related:
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GKR-JOURNEY-DOMAIN-PROPAGATION-D4-001
  - GKR-UX-D5-A-001
  - GKR-UX-D5-B-001
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-UX-D5-C4A-001
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

As vistas consomem explicitamente o eixo transversal dos Domínios de Evolução governado por `PAS-001-DOMAIN-MODEL-001` e reconciliado por `PAS-001-DOMAIN-RECON-001`.

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
→ D4 — Domínios propagados documentalmente nas três jornadas
→ D5-A — Domínios materializados na jornada inicial
→ D5-B — Domínios materializados em Oportunidades
→ D5-C1 — responsabilidades e handoffs de Objetivos, Próximos Passos e Evolução contratados
→ D5-C2 — três responsabilidades materializadas em low-fidelity
→ D5-C3 — três estados-base reformulados e validados localmente
→ D5-C4A — origens visuais em Hoje + contrato integrado dos handoffs, sem promoção
```

D4 e D5 são frentes não numeradas no programa UXA. Nenhuma delas altera a última frente funcional numerada: UXA-101 continua vigente, e UXA-102/V5 permanece não iniciada.

Nenhuma etapa autoriza automaticamente a seguinte.

## 4. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.38.0 | D4 + D5-C4A |
| propagação dos Domínios de Evolução | `active` 1.0.0 | GKR-JOURNEY-DOMAIN-PROPAGATION-D4-001 |
| D5-A — jornada inicial | `active` 1.0.0 | materialização in-place |
| D5-B — Oportunidades | `active` 1.0.0 | materialização in-place |
| D5-C1 — contrato direção/movimento/evolução | `active` 1.0.0 | três responsabilidades + seis handoffs contratados |
| D5-C2 — low-fidelity direção/movimento/evolução | `active` 1.0.0 | 3 SVGs materializados |
| D5-C3 — validação local | `active` 1.0.0 | 3 SVGs reformulados/validados; handoffs preservados |
| D5-C4A — contrato/materialização dos handoffs | `active` 1.0.0 | Hoje recorrente reformulado/revalidado; seis TRNs ainda contratadas |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita preservada |
| Jornada da Pessoa | `draft` | D4; D5-C1/C2/C3/C4A; origem de Planos A4; V4 UXA-101 |
| Jornada do Coletivo | `draft` 0.18.0 | D4; origem de Planos A4 |
| Jornada da Organização | `draft` 0.11.0 | D4; origem de Planos A4 |
| catálogo integrado | `active` | 121 SVGs; 121 validados / 0 pendentes |
| registro de superfícies | `active` | 57 IDs |
| registro de transições | `active` | 66 transições |
| galeria visual integrada | `active` | 121 SVGs / 121 validados |
| galeria de Planos | `active` | 9 SVGs canônicos |
| matriz por SVG | `active` | 121 associações / 34 perfis |
| registro de lacunas | `active` | D5-C4B/V5 e demais continuidades separadas |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 5. Domínios de Evolução nas Jornadas

As três vistas integradas reconhecem explicitamente os nove IDs canônicos:

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

- uma jornada pode ter `0..n` domínios relacionados;
- multidomínio é legítimo;
- `Ainda estou descobrindo` é estado de exploração, não `JED-010`;
- `other_unmapped` preserva área ainda não mapeada;
- domínio candidato não equivale a domínio confirmado;
- domínio não é score, diagnóstico, prioridade humana, autoridade ou prova de evolução;
- mesmo domínio entre participantes não cria match, relevância, compartilhamento ou autorização automática.

A interpretação detalhada por participante está em [Propagação dos Domínios de Evolução nas Jornadas — D4](evolution-domains-d4.md).

## 6. D5-C1/C2/C3/C4A — direção, movimento e evolução na Jornada da Pessoa

A D5-C1 contratou as três responsabilidades especializadas e seus handoffs mínimos:

```text
PER-008 — Hoje
├── TRN-008 → PER-010 — Meus Objetivos → TRN-009 → PER-008
├── TRN-010 → PER-011 — Meus Próximos Passos → TRN-011 → PER-008
└── TRN-012 → PER-012 — Minha Evolução → TRN-013 → PER-008
```

A D5-C2 acrescentou um estado-base low-fidelity para cada responsabilidade:

- `PER-010`: `d5-c2-person-objectives-mobile.svg`;
- `PER-011`: `d5-c2-person-next-steps-mobile.svg`;
- `PER-012`: `d5-c2-person-evolution-mobile.svg`.

A D5-C3 reformula e valida funcionalmente esses três estados-base:

- `PER-010`: estado, prioridade declarada, progresso qualitativo, revisão e privacidade explicitados;
- `PER-011`: `PRONTO` versus `PROPOSTO`, prontidão/dependência, origem e ações coerentes explicitados;
- `PER-012`: período, baseline, direção, inferência, confiança, incerteza e contestação explicitados.

A D5-C4A reforma e revalida localmente o estado recorrente de Hoje sem criar novo SVG. Dentro do bloco existente `Continuando sua jornada`, passam a existir três affordances compactas:

```text
Meus Objetivos
Abrir este passo
Minha Evolução
```

O contrato integrado define:

- origem consciente e autenticada;
- contexto semântico mínimo;
- referência lógica somente quando explicitamente acionada e necessária;
- revalidação de estado, autorização e atualidade no destino;
- retorno sem mutação implícita;
- interrupção sem efeito funcional;
- concorrência resolvida pelo estado vigente;
- idempotência da navegação;
- proteção adicional para `TRN-012/013`, sem transportar área, domínio, interpretação ou evidência sensível por padrão.

A primeira variante de Hoje permanece sem esses aprofundamentos para preservar sua função de orientação inicial sem sobrecarga.

Estado preservado:

- `PER-008` recorrente: **reformulado e revalidado localmente**;
- `PER-010..012`: **validados localmente**;
- `TRN-008..013`: `contratada`, sem validação ponta a ponta;
- nenhum handoff direto entre `PER-010`, `PER-011` e `PER-012` foi criado;
- `PER-008` permanece síntese recorrente e não absorve as três responsabilidades;
- `Minha Evolução` não usa score, ranking, radar obrigatório ou roda da vida.

A separação permanece obrigatória:

```text
Domínio de Evolução
≠ dimensão estrutural do Contexto Vivo
≠ aspecto descritivo da mudança
```

## 7. Continuidade de oportunidades após UXA-101

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

## 8. Etapa transversal de Planos preservada e conectada

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

## 9. Cobertura canônica

| Indicador | Resultado |
|---|---:|
| SVGs canônicos | **121** |
| associações | **121** |
| perfis | **34** |
| validações vigentes de SVG | **121** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **57** |
| transições | **66** |
| IDs com referência visual | **45 de 57** |
| responsabilidades sem SVG dedicado | **10** |
| fronteiras sem tela | **2** |

## 10. Separações obrigatórias

- Domínio de Evolução não equivale a tela, objetivo, score ou prova de evolução;
- dimensão estrutural do Contexto Vivo não equivale a Domínio de Evolução;
- aspecto descritivo da mudança não equivale a Domínio de Evolução;
- mesmo domínio entre participantes não equivale a match automático;
- `PER-010..012` validados localmente não equivalem a continuidade integrada ou implementação;
- `PER-008` recorrente reformulado/revalidado não equivale a promoção de `TRN-008..013`;
- contexto de navegação não amplia consentimento, prioridade, progresso ou autoridade;
- `TRN-008..013` contratadas não equivalem a continuidade validada;
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

## 11. Estado da frente

V1, V2, V3 e V4 estão encerradas nos limites declarados. D4 propaga `JED-001..JED-009`; D5-A e D5-B materializam o eixo em superfícies existentes; D5-C1 contrata `PER-010..012` e `TRN-008..013`; D5-C2 materializa as três superfícies em low-fidelity; D5-C3 reforma e valida localmente os três SVGs; D5-C4A materializa as origens em Hoje e governa o contrato integrado, mantendo os seis handoffs contratados.

A **D5-C4B — validação ponta a ponta de `TRN-008..013`** permanece frente posterior separada. V5/UXA-102, D6, D7 e Engenharia de Produto permanecem fora desta frente.