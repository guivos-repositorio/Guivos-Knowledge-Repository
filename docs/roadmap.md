---
id: ROADMAP-12.79.0
title: Roadmap Arquitetural — Consolidação Documental P0–P9
status: active
version: 12.79.0
owner: Guivos
last_updated: 2026-08-15
supersedes_partial:
  - ROADMAP-12.78.0
related:
  - GKR-STATE-001
  - GKR-P9-GLOBAL-CONSOLIDATION-001
  - GOG-001
  - GPA-004
  - UXA-101
  - GTM-007
  - GTM-008
  - GKR-HOME-P5
  - GKR-HOME-DECISION-NO-WIREFRAME-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V2-SNAPSHOT-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GKR-UX-HOME-ADS-GENINPUT-001
  - M7.88
---

# Roadmap Arquitetural — Consolidação Documental P0–P9

## 1. Autoridade

Este roadmap registra o estado global após a ressincronização documental de agosto de 2026, a convergência das seis Homes públicas atualmente entregáveis, a autorização procedimental de sua fase de Design e a reconciliação canônica do Guivos Business em `GPA-004` v1.5.0. O estado oficial permanece em `GKR-STATE-001`.

A decisão pós-P5 de 2026-08-12 que afastava wireframe da continuidade da Home de Organizações e Coletivos permanece preservada como histórico em `GKR-HOME-DECISION-NO-WIREFRAME-001`, mas foi posteriormente superada **somente quanto à autorização procedimental da fase de Design** por `GKR-UX-HOMES-DESIGN-HANDOFF-001`.

A reconciliação do Business é uma frente de autoridade de produto. Ela não reabre os snapshots de Design v1/v2, não cria automaticamente a Home Pública do Business, não inicia UXA-102 e não altera o marco M7.88.

## 2. Estado vigente

| Elemento | Estado |
|---|---|
| Era | GE-2 — Knowledge |
| marco funcional | **M7.88** |
| última UXA | **UXA-101** |
| UXA-102/V5 | **não iniciada** |
| SVGs | **121** |
| associações | **121** |
| perfis | **34** |
| superfícies/estados/fronteiras | **57** |
| transições | **66** |
| Engenharia de Produto | pausada antes de W0-01 |
| programa P0–P9 | documentalmente consolidado após integração de P9 |
| Guivos Business — autoridade de produto | **GPA-004 v1.5.0 reconciliado; Business distinto de Organização e independente de Ads** |
| Home Pública — Guivos Business | **não iniciada; requer frente própria de Experience Architecture** |
| Home Pública — Pessoa | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Organizações e Coletivos | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente; P1–P5 preservados como histórico |
| Home Pública — Guivos Mall | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Guivos Travel | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Guivos Media | Documento Mestre + GPA-005 + Source Lock; Design autorizado proceduralmente |
| Home Pública — Guivos Ads | Documento Mestre + GPA-007 + Source Lock; Design autorizado proceduralmente |
| handoff comum das seis Homes | **GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.1.0 ativo** |
| pacote externo para Design | **GKR-UX-HOMES-DESIGN-DELIVERY-001 v2.0.0 — 19 fontes canônicas + 6 guias operacionais** |
| snapshot externo v2 | **`delivery/design-handoff-v2` @ `486f1c5e784be6cf3db9b2fbcbc47da39f9e9016`** |
| snapshot externo v1 | **preservado em `delivery/design-handoff-v1` @ `8e2a356ca84ba980e588258757800cde2a946f40`** |

## 3. Sequência funcional preservada

```text
UXA-097 — compreensão inicial → Tela Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — estados residuais Opportunity Boost
→ UXA-100 — Planos
→ UXA-101 — saída consciente → BND-001
→ UXA-102/V5 — PENDENTE, NÃO INICIADA
```

A convergência das Homes públicas, o handoff de Design e a reconciliação do Guivos Business constituem frentes separadas da sequência UXA e **não criam nova UXA, não alteram M7.88 e não retomam Engenharia de Produto**.

## 4. Consolidação temática

| Pacote | Resultado documental |
|---|---|
| P0 | intake/evidência preservado |
| P1/P1.1 | semântica e nomenclaturas integradas |
| P2 | Neo4j como referência de grafo |
| P3 | naming/marca/ativos governados |
| P4 | metodologia e gates de validação integrados |
| P5 | arquitetura institucional/jurídica integrada |
| P6 | privacidade e verdade operacional governadas |
| P7 | internacionalização e gates territoriais integrados |
| P8 | sete Produtos Especializados rebaselineados |
| P9 | estado transversal, matriz e Public Canon reconciliados |

Na Experience Architecture pública, seis Homes atingiram convergência documental suficiente para handoff controlado à fase de Design:

1. Pessoa;
2. Organizações e Coletivos;
3. Guivos Mall;
4. Guivos Travel;
5. Guivos Media;
6. Guivos Ads.

A Home de Organizações e Coletivos preserva P1–P5 como histórico válido. `GKR-HOME-P5` registrou prontidão para decisão humana; a decisão pós-P5 inicialmente afastou wireframe; `GKR-UX-HOMES-DESIGN-HANDOFF-001`, posterior, passou a autorizar wireframe low-fi e demais explorações de Design. A superação é exclusivamente procedimental e não altera significado, narrativa ou produto.

A reconciliação pós-Media estabeleceu que Guivos Media pode abastecer editorialmente outras superfícies sem assumir autoridade sobre a finalidade, narrativa ou operação dessas superfícies.

A Home Guivos Ads possui arquitetura própria, B2B e comercial, com `GKR-UX-HOME-ADS-MASTER-001`, `GPA-007` v1.3.0 e `GKR-UX-HOME-ADS-GENINPUT-001`. Ads preserva a autoridade das superfícies anfitriãs, organiza soluções por objetivo comercial e conduz a qualificação inteligente sem transformar contexto pessoal protegido em matéria-prima publicitária.

O Guivos Business teve sua autoridade de produto reconciliada em `GPA-004` v1.5.0. O estado canônico preserva:

```text
Organização ≠ Guivos Business
Guivos Business ≠ Guivos Ads
custeio empresarial da Journey ≠ propriedade ou controle da Journey
Programa de Pontos ≠ identidade do Business ≠ medida de evolução
Intelligence apoiando Business ≠ Intelligence como módulo Business
```

Uma empresa pode contratar Business e Ads simultaneamente, mas como **relações comerciais independentes**. Business governa capacidades B2B próprias; Ads governa publicidade, patrocínio, impulsionamento e exposição comercial paga. Nenhuma contratação concede automaticamente autoridade, inventário, capacidades ou direitos do outro produto.

O Programa de Pontos permanece reconhecido arquiteturalmente como capacidade Business, com financiamento empresarial e uso em ofertas elegíveis sob regras próprias. A reconciliação não presume operação em produção, taxa de conversão, expiração, reembolso, pagamento híbrido ou tratamento financeiro não governado.

Guivos Business pode estruturar arranjos empresariais que custeiem acesso, benefícios, incentivos ou capacidades vinculadas ao Journey, mas esse custeio não transfere à empresa autoridade sobre a Journey nem acesso ao contexto pessoal protegido. Guivos Intelligence pode apoiar análises empresariais autorizadas e indicadores agregados sem se tornar módulo Business e sem converter contexto pessoal protegido em ativo empresarial.

O pacote de entrega v2 é governado por `GKR-UX-HOMES-DESIGN-DELIVERY-001`: 19 fontes canônicas extraídas da `main` canônica `603aa7f37435ac376f7a202669ad4ac1d7d13a83`, separadas por Home, acrescidas de seis guias operacionais `LEIA-PRIMEIRO`, totalizando 25 arquivos no snapshot externo `486f1c5e784be6cf3db9b2fbcbc47da39f9e9016`.

A emissão v1 continua preservada no snapshot `8e2a356ca84ba980e588258757800cde2a946f40` e não foi reescrita pela v2.

## 5. Lacunas não fechadas por documentação

Continuam dependentes de evidência ou autorização própria:

- resultados reais de mercado e PMF;
- implementação tecnológica e grafo em produção;
- fatos registrários de marca/domínios;
- constituição jurídica de eventual veículo social;
- controles legais/privacidade em produção;
- piloto e operação internacional;
- cobrança/gateway real;
- handoffs especializados ainda não materializados;
- seleção e validação humana das direções visuais das seis Homes;
- promoção de qualquer output de Design a estado canônico;
- implementação operacional da experiência inteligente de qualificação do Guivos Ads;
- implementação operacional de campanhas, inventário, pricing e mensuração do Guivos Ads;
- regras econômicas/operacionais ainda abertas do Programa de Pontos Business;
- arquitetura narrativa, Documento Mestre, conversão e Source Lock da Home Pública do Guivos Business;
- implementação de analytics/Intelligence Business e seus contratos técnicos de dados;
- UXA-102/V5;
- Product Engineering.

## 6. Próximos caminhos possíveis

Após P9, não existe “P10” automático.

O próximo ato deve nascer de uma necessidade concreta e autoridade própria. Exemplos:

- evidência de pesquisa → VAL;
- decisão de implantação → ADR/Engineering;
- fato jurídico/institucional → gates P5;
- controle operacional/privacy → gates P6;
- readiness/piloto territorial → gates P7;
- nova continuidade funcional → UXA-102 somente por autorização humana separada;
- implementação → Product Engineering somente por reativação explícita;
- seis Homes convergidas → exploração de Design controlada por Home e por Source Lock;
- Guivos Ads → validar direção de Design, operação comercial e experiência inteligente em atos próprios, sem inferir implementação automática;
- Guivos Business → iniciar, em frente própria, tese, protagonista, problema, promessa, arquitetura narrativa, contratos de autoridade, conversão e posterior Documento Mestre da Home, sem tratá-lo como extensão da Home de Organizações nem como contêiner do Ads.

## 7. Handoff e entrega para Design

O estado governado é:

```text
GKR
→ fonte de verdade e arquitetura

GKR-UX-HOMES-DESIGN-HANDOFF-001
→ autorização procedimental + regras de Design para seis Homes

SOURCE LOCK DE CADA HOME
→ contexto permitido por execução

GKR-UX-HOMES-DESIGN-DELIVERY-001 v2.0.0
→ composição e integridade do pacote externo

GKR-UX-HOMES-DESIGN-DELIVERY-V2-SNAPSHOT-001
→ registro factual do snapshot emitido

branch delivery/design-handoff-v2
→ snapshot de distribuição vigente
→ não é fonte canônica paralela

branch delivery/design-handoff-v1
→ snapshot histórico preservado

OUTPUT DE DESIGN
→ EXPLORAÇÃO
→ requer validação humana antes de qualquer promoção
```

As branches de entrega não devem ser mescladas na `main` para duplicar documentos canônicos. Se qualquer fonte obrigatória evoluir materialmente, deve ser avaliada nova emissão do pacote em vez de substituição silenciosa de arquivos dentro de um snapshot já distribuído.

A futura Home do Guivos Business **não entra automaticamente no snapshot v2 existente**. Sua eventual convergência e inclusão em nova emissão de Design dependerão de Documento Mestre, contratos complementares, Source Lock, validação e autorização próprias.

## 8. Preservação

`ressincronização documental concluída ≠ produto implementado ≠ operação comprovada`.

`Design autorizado ≠ solução aprovada ≠ output canônico ≠ implementação ≠ publicação`.

Para Organizações e Coletivos:

`decisão histórica sem wireframe ≠ proibição procedimental vigente`, pois o handoff posterior de Design governa esse limite específico.

Para Guivos Ads:

`Home convergida ≠ campanha operacional ≠ inventário disponível ≠ pricing público ≠ Intelligence implementado ≠ contratação automática`.

Para Guivos Business:

`Organização ≠ Business ≠ Ads`.

`custeio da Journey ≠ propriedade da Journey ≠ acesso ao contexto pessoal protegido`.

`Programa de Pontos reconhecido arquiteturalmente ≠ operação financeira implementada ≠ medida de evolução`.

`Intelligence apoiando Business ≠ módulo Business ≠ acesso irrestrito a dados pessoais`.

`GPA-004 reconciliado ≠ Home Business convergida ≠ inclusão automática em pacote de Design`.