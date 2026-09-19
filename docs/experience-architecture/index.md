---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 1.20.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-19
related:
  - PAS-001
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GLPA-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - UXA-001
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-069
  - UXA-070
  - UXA-080
  - UXA-090
  - UXA-092
  - UXA-094
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-A-001
  - GKR-UX-D5-B-001
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-UX-D5-C4A-001
  - GKR-UX-D5-C4B-001
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
  - GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-UX-HOMES-DESIGN-SOURCE-READINESS-AUDIT-001
  - M7.88
normative: false
---

# Arquitetura da Experiência da Guivos

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos em experiências compreensíveis para Pessoas, Coletivos e Organizações. Ela governa hierarquia, decisão, continuidade, confirmação, autoridade, privacidade e proteção antes de design final ou implementação.

## 2. Regra de maturidade

```text
contrato funcional
→ programa governado
→ materialização
→ validação funcional
→ reformulação quando exigida
→ revalidação
→ promoção controlada quando aplicável
→ inspeção integrada
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Cobertura visual e granular

A camada física de wireframes foi removida do corpus vigente por `F-016-A` após prova estrutural e semântica de absorção.

```text
SVGs FÍSICOS EM docs/assets/wireframes/
→ 0

ASSOCIAÇÕES FÍSICAS CORRENTES
→ 0

PERFIS DE RASTREABILIDADE
→ 34
→ preservados apenas como proveniência/semântica

AUTORIDADE VISUAL
→ DESIGN

AUTORIDADE FUNCIONAL
→ DOCUMENTAÇÃO TEXTUAL / EXPERIENCE ARCHITECTURE
```

A remoção física não altera por si só maturidade funcional de superfícies, estados ou transições. Nomes `.svg` ainda citados em documentos preservados devem ser lidos exclusivamente como proveniência histórica.

`F-016-A = RESOLVED` após Semantic #832, Mechanical #1090 e prova read-only pós-delete v2. `F-016 = RESOLVED` após adjudicação, cleanup documental 26/26, reconciliação estrutural e prova pós-delete, sem autorização automática de nova materialização.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional;
- validação local de superfície não equivale por si só a continuidade integrada;
- validação integrada documental não equivale a implementação técnica;
- perfil de rastreabilidade não equivale por si só a aprovação da superfície;
- uma versão visual reformulada exige validação correspondente;
- publicação ou ativação não equivale a distribuição garantida;
- plano pago não altera relevância, confiança, legitimidade, impacto ou evolução;
- oportunidade pública não é ocultada para vender plano;
- navegar para Planos não equivale a escolher plano ou iniciar cobrança;
- Pessoa utiliza `Free · Plus · Pro`;
- Coletivo utiliza `Livre · Mobiliza · Impacta · Rede`;
- Organização utiliza `Conecta · Eleva · Transforma`;
- Guivos Business utiliza `Start · Growth · Scale · Enterprise` como Produto Especializado separado;
- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- `BND-002` representa contratação/dimensionamento assistido e não plano específico;
- fronteira externa não é tela da Guivos;
- validação até uma fronteira não valida comportamento de terceiro;
- Domínio de Evolução organiza sobre o que a jornada trata e não representa diagnóstico, identidade, score, Objetivo, Próximo Passo ou prova de evolução;
- domínio candidato permanece distinto de domínio confirmado;
- ausência de domínio confirmado é estado legítimo;
- multidomínio é legítimo quando houver autoridade e finalidade adequadas;
- domínio da oportunidade ≠ domínio confirmado da Pessoa ≠ relevância contextual ≠ recomendação;
- `PER-008 — Hoje` sintetiza e encaminha, mas não substitui Objetivos, Próximos Passos ou Evolução Contínua;
- acesso visual a uma superfície especializada não cria, inicia, confirma ou reconhece objeto funcional;
- contexto de navegação é mínimo e não amplia consentimento ou autoridade;
- Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo ≠ aspecto descritivo da mudança;
- `Minha Evolução` ≠ roda da vida obrigatória ≠ ranking ≠ diagnóstico ≠ percentual global da Pessoa.

## 5. Evolução recente

```text
UXA-097 — primeira Hoje e TRN-007
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe
→ UXA-099 — dez estados residuais Opportunity Boost
→ UXA-100/A1/A2/A3 — Planos nas três jornadas e promoção canônica
→ UXA-101 — revisão consciente de saída e TRN-205 até BND-001
→ UXA-100-A4 — reconciliação das origens administrativas de Planos
→ D4 — propagação documental dos Domínios nas três jornadas
→ D5-A — Domínios em Expressão Guiada, Compreensão Inicial e Hoje
→ D5-B — Domínios na camada de Oportunidades
→ D5-C1 — contrato das superfícies de direção, movimento e evolução
→ D5-C2 — low-fidelity de Meus Objetivos, Meus Próximos Passos e Minha Evolução
→ D5-C3 — validação funcional e reformulação dos três SVGs
→ D5-C4A — origens visuais em Hoje + contrato integrado dos seis handoffs
→ D5-C4B — validação integrada individual e promoção de TRN-008..013
→ O/C Surface Map — DEFINED / CANONICAL DOCUMENTARY
→ O/C State Map — DEFINED / CANONICAL DOCUMENTARY
→ Public Homes Design Production Release — GRANTED / GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.1.0
→ Public Homes Source Readiness Audit — IN_PROGRESS / GKR-UX-HOMES-DESIGN-SOURCE-READINESS-AUDIT-001
→ Public Homes Design Handoff v5 Snapshot — FROZEN / HISTORICAL FOR NEW DESIGN START / 34 FILES / 26/26 BYTE-PRESERVED
→ Public Homes v6 Source Package — NOT_EMITTED
→ External Designer Start — DEFERRED UNTIL FINAL SOURCE READINESS PASS
→ GKR / ChatGPT Figma Execution — NOT TO BE PERFORMED
```

D4 e D5 são frentes não numeradas. UXA-101 continua a última frente funcional numerada e UXA-102/V5 permanece não iniciada. A definição documental do State Map O/C não altera esse estado.

### 5.1 D5-A

[GKR-UX-D5-A-001](d5-a-evolution-domains-guided-expression-initial-understanding-today.md) consolida Área da jornada candidata/revisável em Expressão Guiada e Compreensão Inicial e contexto discreto em Hoje, sem nova superfície ou transição.

### 5.2 D5-B

[GKR-UX-D5-B-001](d5-b-evolution-domains-opportunities-layer.md) consolida `0..n` Áreas relacionadas no cadastro institucional, filtro explícito em Mapa/Lista e separação entre área da oportunidade e relevância pessoal no Detalhe.

### 5.3 D5-C1

[GKR-UX-D5-C1-001](d5-c1-direction-movement-evolution-surface-contract.md) consolida três responsabilidades especializadas (`PER-010..012`), seis handoffs mínimos (`TRN-008..013`) e nenhuma navegação direta inventada entre as três superfícies.

### 5.4 D5-C2

[GKR-UX-D5-C2-001](d5-c2-direction-movement-evolution-low-fidelity-wireframes.md) materializa um estado-base móvel para cada responsabilidade e cria três perfis de rastreabilidade (`R32..R34`).

### 5.5 D5-C3

[GKR-UX-D5-C3-001](d5-c3-direction-movement-evolution-functional-validation.md) reforma e valida localmente os três estados-base, preservando autonomia, prioridade declarada, prontidão, incerteza, privacidade e ausência de score humano.

### 5.6 D5-C4A

[GKR-UX-D5-C4A-001](d5-c4a-direction-movement-evolution-handoff-contract.md) reformula `uxa-006-hoje-mobile.svg`, materializa `Meus Objetivos`, `Abrir este passo` e `Minha Evolução` no estado recorrente de Hoje e governa identidade, contexto mínimo, revalidação, retorno, interrupção, concorrência, idempotência, autoridade e sensibilidade.

### 5.7 D5-C4B

[GKR-UX-D5-C4B-001](d5-c4b-direction-movement-evolution-integrated-handoff-validation.md) aplica individualmente os gates de validação integrada e promove:

- `TRN-008` — Hoje recorrente → Meus Objetivos;
- `TRN-009` — Meus Objetivos → Hoje;
- `TRN-010` — Hoje recorrente → Meus Próximos Passos;
- `TRN-011` — Meus Próximos Passos → Hoje;
- `TRN-012` — Hoje recorrente → Minha Evolução;
- `TRN-013` — Minha Evolução → Hoje.

As seis ficam **integralmente validadas no limite documental**. A primeira variante de Hoje não é obrigada a exibir os três affordances especializados.

## 6. Resultado da UXA-100-A4 preservado

[UXA-100-A4](uxa-100-a4-plans-entry-origin-and-navigation-handoffs.md) continua governando `PER-009`, `TRN-406/407`, `TRN-417/418` e `TRN-427/428`. No snapshot físico anterior, `PER-009` não possuía SVG dedicado; após `F-016-A`, toda a camada física foi removida e essa ausência específica permanece somente como proveniência histórica. Cobrança real, entitlement e processo posterior a `BND-002` continuam fora do escopo.

## 7. Resultado da UXA-101 preservado

[UXA-101](uxa-101-conscious-external-boundary-validation.md) continua encerrando V4 no limite controlável pela Guivos: revisão pré-saída em `PER-203`, destino externo, minimização de dados/contexto, confirmação afirmativa, revalidação, retorno seguro e `TRN-205` validada até `BND-001`.

## 8. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active` 0.48.0; Jobs + IA + Surface Map + State Map + Priority Flows + Navigation Materialization O/C reconciliados |
| Jornada da Pessoa | `draft`; PER-010..012 validados localmente; TRN-008..013 integrais |
| Jornada do Coletivo | `draft` 0.23.0; low-fidelity validado; high-fidelity eligibility `PASS`; autorização high-fidelity não concedida |
| Jornada da Organização | `draft` 0.16.0; low-fidelity validado; high-fidelity eligibility `PASS`; autorização high-fidelity não concedida |
| atores, autoridades e jobs autenticados O/C | `GKR-UX-ORGCOL-AUTH-JOBS-001 v1.4.0`; **ACTIVE / DEFINED** |
| Arquitetura da Informação autenticada O/C | `GKR-UX-ORGCOL-AUTH-IA-001 v1.3.0`; **ACTIVE / DEFINED PRE-SURFACE-MAP** |
| mapa lógico autenticado O/C | `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.0.0`; **DEFINED / CANONICAL DOCUMENTARY** |
| mapa de estados autenticado O/C | `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.0.0`; **DEFINED / CANONICAL DOCUMENTARY**; não cria/promove `GKR-TRN-*` nem materializa Priority Flows |
| fluxos prioritários autenticados O/C | `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0`; **DEFINED / CANONICAL DOCUMENTARY**; não cria/promove `GKR-TRN-*` nem materializa navegação |
| elegibilidade de Navigation Materialization O/C | `GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001 v1.0.0`; **PASS / ACTIVE / CANONICAL** |
| Navigation Materialization autenticada O/C | `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0`; **DEFINED / CANONICAL DOCUMENTARY** |
| autorização de wireframes low-fidelity O/C | `GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001 v1.0.0`; **GRANTED / ACTIVE / NORMATIVE** |
| entrega low-fidelity O/C | `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0`; **EXECUTED** |
| validação funcional low-fidelity O/C | `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`; **PASS / 0 MATERIAL FINDINGS** |
| referência visual low-fidelity corrente O/C | **DELIVERY v0.1.0 + VALIDATION v1.0.0** |
| elegibilidade high-fidelity O/C | `GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001 v1.0.0`; **PASS / PRE-AUTHORIZATION** |
| autorização high-fidelity O/C | **NOT_GRANTED / REQUIRES SEPARATE HUMAN ACT** |
| catálogo integrado | `active` 0.37.0; **0 SVGs físicos após F-016-A**; maturidade funcional preservada por autoridades textuais |
| proveniência visual histórica | documentos de galeria/matriz removidos do corpus corrente; recuperáveis no histórico Git; sem autoridade visual |
| lacunas | `active` 0.37.0; ciclo low-fidelity O/C fechado; high-fidelity eligibility = PASS; autorização high-fidelity permanece não concedida |
| registro de superfícies | `active` 0.26.0; 57 IDs; maturidade por item; crosswalk O/C sem promoção automática |
| registro de transições | `active`; 66 transições; State Map não promove maturidade por inferência |
| detalhamento da Pessoa | `active`; PER-008 recorrente e PER-010..012 com continuidade D5-C validada |
| D5-A | `active` 1.1.0 |
| D5-B | `active` 1.1.0 |
| D5-C1 | `active` 1.0.0 |
| D5-C2 | `active` 1.1.0 |
| D5-C3 | `active` 1.1.0 |
| D5-C4A | `active` 1.1.0 |
| D5-C4B | `active` 1.1.0 |

## 9. Ressalvas vigentes

- o inventário físico corrente é `0 SVGs / 0 associações`; `121` pertence exclusivamente ao snapshot histórico anterior à desmaterialização e não representa inventário ou maturidade vigente;
- a recomputação governada de maturidade visual agregada permanece aberta;
- artefatos históricos `superseded`, incluindo os associados a `UXA-015..018`, permanecem recuperáveis no histórico Git e não devem ser promovidos a autoridade corrente;
- o snapshot físico/associativo anterior registrava 10 responsabilidades sem SVG dedicado, incluindo `PER-009`; essa contagem é proveniência histórica e não constitui déficit visual corrente após a remoção integral da camada física;
- `TRN-008..013` estão integralmente validadas documentalmente, não implementadas;
- `TRN-406/407` permanecem contratadas;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` permanecem parciais;
- `TRN-304`, `TRN-305` e `TRN-306` permanecem parciais na integração patrocinada;
- `TRN-416/426` permanecem parciais;
- gateway, cobrança real, proration e processo após `BND-002` permanecem fora do escopo;
- processo externo após `BND-001` permanece sob autoridade de terceiro;
- Jornadas da Pessoa, Coletivo e Organização continuam `draft`;
- D6 e D7 permanecem não iniciadas;
- V5/UXA-102 permanece não iniciada.

## 10. Fila global preservada

```text
V1 — encerrada pela UXA-097
→ V2 — encerrada pela UXA-098
→ V3 — encerrada pela UXA-099
→ Planos — identidade canônica encerrada pela UXA-100-A3
→ V4 — encerrada pela UXA-101 até BND-001
→ Planos — origem voluntária reconciliada pela UXA-100-A4
→ D5-A — Domínios na jornada inicial materializados in-place
→ D5-B — Domínios na camada de Oportunidades materializados sem nova superfície
→ D5-C1 — responsabilidades e handoffs mínimos contratados
→ D5-C2 — três superfícies materializadas em low-fidelity
→ D5-C3 — três superfícies reformuladas e validadas localmente
→ D5-C4A — Hoje recorrente reformulado/revalidado + contrato dos seis handoffs
→ D5-C4B — seis handoffs integralmente validados no limite documental
→ O/C Surface Map — DEFINED / CANONICAL DOCUMENTARY
→ O/C State Map — DEFINED / CANONICAL DOCUMENTARY
→ O/C Priority Flows — DEFINED / CANONICAL DOCUMENTARY
→ O/C Navigation Materialization Eligibility — PASS / ACTIVE / CANONICAL
→ O/C Navigation Materialization — DEFINED / CANONICAL DOCUMENTARY / v1.0.0
→ O/C Low-Fidelity Wireframe Authorization — GRANTED / v1.0.0
→ O/C Low-Fidelity Wireframe Delivery — EXECUTED / v0.1.0
→ O/C Low-Fidelity Functional Validation — PASS / v1.0.0
→ O/C Current Low-Fidelity Reference — DELIVERY v0.1.0 + VALIDATION v1.0.0
→ O/C High-Fidelity Eligibility — PASS / v1.0.0
→ O/C High-Fidelity Design Authorization — NOT_GRANTED
→ V5 — pendente e não iniciada
```

D5-A/B/C1/C2/C3/C4A/C4B e a frente documental O/C não consomem nem antecipam V5.

## 11. Próxima evolução possível

A D5-C4B encerra somente a lacuna D5-C de continuidade especializada da Pessoa. O Bloco 2 também reconciliou Jobs + IA autenticada de Organização/Coletivo; `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.0.0` define o **Surface Map lógico-documental canônico** e `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.0.0` define o **State Map funcional canônico documental**. Os **Priority Flows** estão definidos documentalmente em `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0`; a elegibilidade de Navigation Materialization está `PASS` em `GKR-UX-ORGCOL-AUTH-NAV-MAT-ELIGIBILITY-001 v1.0.0`; e a própria Navigation Materialization está definida canonicamente em `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0`. Os Authenticated Wireframes low-fidelity foram autorizados, entregues e funcionalmente validados com `PASS` em `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`. O pacote Delivery + Validation é a referência corrente low-fidelity O/C. A adjudicação `GKR-UX-ORGCOL-AUTH-HIFI-ELIGIBILITY-001 v1.0.0` conclui `PASS`; o próximo gate possível é somente uma decisão humana separada de autorização high-fidelity. D6, D7, materialização de `PER-009`, V5/UXA-102, cobrança real, integrações patrocinadas e demais validações permanecem independentes e exigem autorização própria. Nenhuma é iniciada automaticamente.

### Public Homes — Design Handoff v5 Snapshot

[GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001](public-homes-design-delivery-v5-snapshot-record.md) registra a emissão externa reproduzível v5 das oito Homes, com 26 fontes canônicas byte-preservadas e oito guias operacionais. O registro preserva que **a emissão isoladamente** não concedeu Design Release.

### Public Homes — Design Production Release

[GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001](public-homes-design-production-release.md) registra `DESIGN PRODUCTION RELEASE = GRANTED`, preserva a futura produção externa pela designer e explicita que o GKR/ChatGPT não cria artefatos Figma. O início operacional da designer está postergado até o fechamento da auditoria final de prontidão das fontes.

### Public Homes — Final Source Readiness for Designer and AI

[GKR-UX-HOMES-DESIGN-SOURCE-READINESS-AUDIT-001](public-homes-designer-ai-source-readiness-audit.md) governa a revisão final 8/8 dos Masters, fontes específicas e autoridades comuns antes de um novo pacote v6. O objetivo é `P0 = 0`, `P1 = 0`, consumibilidade humana/AI `PASS` e nenhuma definição visual pré-imposta.
