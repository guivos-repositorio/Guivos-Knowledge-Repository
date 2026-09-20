---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.49.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-18
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
  - GKR-UX-D5-C4B-001
  - UXA-070
  - UXA-080
  - UXA-090
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A3
  - UXA-100-A4
  - UXA-101
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-SUPPLY-VALUE-001
  - RP-002
normative: false
---

# Jornadas Integradas

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


## 1. Finalidade

Esta seção reúne as jornadas da Pessoa, do Coletivo e da Organização para leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas. Ela não substitui contratos, wireframes, validações ou registros canônicos.

As vistas consomem explicitamente o eixo transversal dos Domínios de Evolução governado por `PAS-001-DOMAIN-MODEL-001` e reconciliado por `PAS-001-DOMAIN-RECON-001`.

A investigação de supply, oportunidades reais e testes de relevância de Organizações e Coletivos está exposta também como referência de leitura em [Organizações e Coletivos — Supply, Rede e Modelo de Valor](../experience-architecture/organizations-collectives-supply-and-value.md). Essa referência contém exemplos mundiais, perfis sintéticos, gates, descartes, evidência e limites de PMF; permanece Research consolidado pré-validação de campo.

## 2. Vistas disponíveis

- [Propagação dos Domínios de Evolução nas Jornadas — D4](evolution-domains-d4.md)
- [Catálogo de Telas](screen-catalog.md)
- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Atlas de oportunidades, supply e relevância de Organizações e Coletivos](../experience-architecture/organizations-collectives-supply-and-value.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e Continuidades Ausentes](gaps.md)

## 3. Topologia corrente

```text
PESSOA
→ HOME PÚBLICA
→ ENTRADA PROTEGIDA
→ COMPREENSÃO / HOJE
→ OBJETIVOS / PRÓXIMOS PASSOS / EVOLUÇÃO
→ OPORTUNIDADES
→ EXPERIÊNCIAS / FRONTEIRAS EXTERNAS

COLETIVO
→ HOME PÚBLICA
→ EXPERIÊNCIA AUTENTICADA
→ PARTICIPAÇÃO / RESPONSABILIDADE / SOLICITAÇÕES / CONTINUIDADE

ORGANIZAÇÃO
→ HOME PÚBLICA
→ EXPERIÊNCIA AUTENTICADA
→ CAPACIDADES / OPORTUNIDADES / RELAÇÕES / CONTINUIDADE
```

A maturidade de cada superfície e transição é determinada pelos registries e autoridades correntes, não pela sequência histórica de UXAs que levou até elas.

## 4. Estado documental corrente

| Camada | Estado corrente |
|---|---|
| Journey da Pessoa | contratos e continuidade documentados; implementação separada |
| Journey do Coletivo | topologia autenticada e fluxos correntes documentados |
| Journey da Organização | topologia autenticada e fluxos correntes documentados |
| Domínios de Evolução | autoridade corrente |
| Catálogo de telas | catálogo funcional corrente; sem inventário histórico de SVGs |
| Registro de superfícies | autoridade granular corrente |
| Registro de transições | autoridade granular corrente |
| Protótipo/implementação | somente quando explicitamente autorizado |

```text
HISTORICAL UXA SEQUENCE
→ NOT REQUIRED FOR DESIGN / AI

PHYSICAL SVG HISTORY
→ NOT REQUIRED FOR DESIGN / AI

CURRENT REGISTRIES
→ AUTHORITATIVE FOR PROTOTYPING
```

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

## 6. D5-C — direção, movimento e evolução na Jornada da Pessoa

A estrutura governada é:

```text
PER-008 — Hoje recorrente
├── TRN-008 → PER-010 — Meus Objetivos → TRN-009 → PER-008
├── TRN-010 → PER-011 — Meus Próximos Passos → TRN-011 → PER-008
└── TRN-012 → PER-012 — Minha Evolução → TRN-013 → PER-008
```

A D5-C2 acrescentou um estado-base low-fidelity para cada responsabilidade. A D5-C3 reformulou e validou funcionalmente os três estados-base. A D5-C4A reformulou/revalidou Hoje recorrente e governou o contrato dos seis handoffs.

A D5-C4B valida integralmente, no limite documental:

- `TRN-008/009` — Hoje recorrente ↔ Meus Objetivos;
- `TRN-010/011` — Hoje recorrente ↔ Meus Próximos Passos;
- `TRN-012/013` — Hoje recorrente ↔ Minha Evolução.

A validação cobre origem, destino, autoridade, contexto mínimo, efeitos proibidos, retorno, interrupção, concorrência e idempotência. Para Evolução, cobre também minimização e preservação da natureza epistemológica.

A primeira variante de Hoje permanece sem obrigação de materializar os três aprofundamentos. Quando o affordance não estiver presente, a transição de entrada simplesmente não é instanciada naquele estado visual.

Estado:

- `PER-008` recorrente: **reformulado e revalidado localmente**;
- `PER-010..012`: **validados localmente**;
- `TRN-008..013`: **integralmente validadas no limite documental**;
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

A continuidade documental acima não substitui o problema de relevância. O aprofundamento de como uma oportunidade é descoberta, qualificada, descartada ou apresentada para um Momento específico está no [Atlas de oportunidades, supply e relevância](../experience-architecture/organizations-collectives-supply-and-value.md).

## 8. Etapa transversal de Planos preservada e conectada

A espinha dorsal comercial permanece:

```text
*-301 Planos e comparação
├── upgrade → *-302 revisão → *-304 resultado/recuperação → *-301
├── downgrade/cancelamento → *-303 → *-304 → *-301
└── quando autoatendimento não for suficiente → BND-002
```

A origem voluntária possui identidade contratual no fluxo especializado:

```text
PER-009 ↔ PER-301   — TRN-406/407 contratadas
COL-002 ↔ COL-301   — TRN-417/418 validadas no contrato especializado
ORG-001 ↔ ORG-301   — TRN-427/428 validadas no contrato especializado
```

A maturidade de `TRN-417/418` e `TRN-427/428` não promove `COL-002` ou `ORG-001` a wireframes principais autenticados vigentes.

Abrir Planos não seleciona tier, não inicia cobrança e não altera consentimento, capacidade ou relevância. `PER-009` permanece sem SVG dedicado; sua futura materialização é gap separado.

A nomenclatura vigente é:

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`;
- Guivos Business: `Start · Growth · Scale · Enterprise`, como Produto Especializado separado.

`BND-002` é fronteira genérica de contratação/dimensionamento assistido e não plano. As transições comerciais internas continuam localmente validadas; `TRN-416/426` permanecem parciais. Cobrança real e processo posterior a `BND-002` continuam fora do escopo.

## 9. Cobertura documental reconciliada

| Indicador | Resultado |
|---|---:|
| SVGs físicos existentes | **0** |
| associações físicas registradas | **0** |
| perfis documentais | **34** |
| claim agregada anterior `121 validados / 0 pendentes` | **superseded como estado de maturidade vigente** |
| nova contagem agregada de wireframes vigentes/validados | **não inferida; requer recomputação governada** |
| wireframe principal autenticado da Organização | **pendente** |
| wireframe principal autenticado do Coletivo | **pendente** |
| superfícies/estados/fronteiras documentais | **57** |
| transições documentais | **66** |
| IDs com referência visual física | **0 de 57** |
| responsabilidades sem SVG dedicado | **métrica histórica; não usada como cobertura corrente após F-016-A** |
| fronteiras sem tela | **2** |

```text
INVENTÁRIO FÍSICO
≠ VIGÊNCIA
≠ VALIDAÇÃO FUNCIONAL ATUAL
```

## 10. Separações obrigatórias

- Domínio de Evolução não equivale a tela materializada;
- responsabilidade documentada não equivale a wireframe;
- State Map definido não equivale, por si só, a Priority Flow; Priority Flows posteriores não equivalem a navegação materializada;
- contrato de navegação especializado não equivale a wireframe principal vigente;
- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- `BND-002` ≠ Enterprise ou Scale;
- revisão de saída em `PER-203` não cria tela nova;
- validação até `BND-001` não valida sistema de terceiro;
- pagar um plano ou patrocínio não altera relevância funcional;
- `COM-005` validado não promove automaticamente `TRN-305`;
- exemplos reais do atlas não equivalem a parceiros, oportunidades admitidas ou PMF;
- validação documental não equivale a implementação técnica.

## 11. Estado da frente

V1, V2, V3 e V4 estão encerradas nos limites declarados. D4 propaga `JED-001..JED-009`; D5-A e D5-B materializam o eixo em superfícies existentes; D5-C1 contrata `PER-010..012` e `TRN-008..013`; D5-C2 materializa as três superfícies; D5-C3 valida localmente os três SVGs; D5-C4A materializa as origens em Hoje e governa o contrato integrado; D5-C4B promove as seis ligações para integralmente validadas no limite documental.

A reconciliação pós-313/314 e o Bloco H preservam Jobs + IA autenticada como definidos em seus limites próprios. `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.0.0` define o mapa lógico-documental canônico de Organização e Coletivo e `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.0.0` define o mapa funcional de estados autenticados. Os Priority Flows estão definidos por `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0`; permanecem pendentes a navegação materializada e os wireframes principais autenticados, ainda que fluxos especializados preservem validações próprias.

O atlas de supply e relevância documenta Research consolidado e simulações, mas não substitui o Dry Run/Piloto com Pessoas reais.

V5/UXA-102, D6, D7 e Engenharia de Produto permanecem fora desta frente.