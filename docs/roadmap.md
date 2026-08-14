---
id: ROADMAP-12.77.0
title: Roadmap Arquitetural — Consolidação Documental P0–P9
status: active
version: 12.77.0
owner: Guivos
last_updated: 2026-08-14
supersedes_partial:
  - ROADMAP-12.76.0
related:
  - GKR-STATE-001
  - GKR-P9-GLOBAL-CONSOLIDATION-001
  - GOG-001
  - UXA-101
  - GTM-007
  - GTM-008
  - GKR-HOME-P5
  - GKR-HOME-DECISION-NO-WIREFRAME-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - M7.88
---

# Roadmap Arquitetural — Consolidação Documental P0–P9

## 1. Autoridade

Este roadmap registra o estado global após a ressincronização documental de agosto de 2026, a convergência das cinco Homes públicas atualmente entregáveis e a autorização procedimental de sua fase de Design. O estado oficial permanece em `GKR-STATE-001`.

A decisão pós-P5 de 2026-08-12 que afastava wireframe da continuidade da Home de Organizações e Coletivos permanece preservada como histórico em `GKR-HOME-DECISION-NO-WIREFRAME-001`, mas foi posteriormente superada **somente quanto à autorização procedimental da fase de Design** por `GKR-UX-HOMES-DESIGN-HANDOFF-001`.

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
| Home Pública — Pessoa | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Organizações e Coletivos | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente; P1–P5 preservados como histórico |
| Home Pública — Guivos Mall | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Guivos Travel | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Guivos Media | Documento Mestre + GPA-005 + Source Lock; Design autorizado proceduralmente |
| handoff comum das cinco Homes | **GKR-UX-HOMES-DESIGN-HANDOFF-001 ativo** |
| pacote externo para Design | **GKR-UX-HOMES-DESIGN-DELIVERY-001 v1.1.0 — 16 fontes canônicas + 5 guias operacionais** |
| Home Guivos Ads | **não iniciada** |

## 3. Sequência funcional preservada

```text
UXA-097 — compreensão inicial → Tela Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — estados residuais Opportunity Boost
→ UXA-100 — Planos
→ UXA-101 — saída consciente → BND-001
→ UXA-102/V5 — PENDENTE, NÃO INICIADA
```

A convergência das Homes públicas e o handoff de Design constituem Experience Architecture e **não criam nova UXA, não alteram M7.88 e não retomam Engenharia de Produto**.

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

Na Experience Architecture pública, cinco Homes atingiram convergência documental suficiente para handoff controlado à fase de Design:

1. Pessoa;
2. Organizações e Coletivos;
3. Guivos Mall;
4. Guivos Travel;
5. Guivos Media.

A Home de Organizações e Coletivos preserva P1–P5 como histórico válido. `GKR-HOME-P5` registrou prontidão para decisão humana; a decisão pós-P5 inicialmente afastou wireframe; `GKR-UX-HOMES-DESIGN-HANDOFF-001`, posterior, passou a autorizar wireframe low-fi e demais explorações de Design para as cinco Homes. A superação é exclusivamente procedimental e não altera significado, narrativa ou produto.

A reconciliação pós-Media estabeleceu que Guivos Media pode abastecer editorialmente outras superfícies sem assumir autoridade sobre a finalidade, narrativa ou operação dessas superfícies.

O pacote de entrega v1 é governado por `GKR-UX-HOMES-DESIGN-DELIVERY-001`: 16 fontes canônicas congeladas no checkpoint `4fee04c4da8d099ac3c415c870391011ceb28e6d`, separadas por Home, acrescidas de cinco guias operacionais `LEIA-PRIMEIRO` no snapshot externo.

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
- seleção e validação humana das direções visuais das cinco Homes;
- promoção de qualquer output de Design a estado canônico;
- Home Guivos Ads, ainda sem Documento Mestre específico nesta frente;
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
- cinco Homes convergidas → exploração de Design controlada por Home e por Source Lock;
- Home Guivos Ads → nova frente de Experience Architecture somente por autorização humana própria.

## 7. Handoff e entrega para Design

O estado governado é:

```text
GKR
→ fonte de verdade e arquitetura

GKR-UX-HOMES-DESIGN-HANDOFF-001
→ autorização procedimental + regras de Design

SOURCE LOCK DE CADA HOME
→ contexto permitido por execução

GKR-UX-HOMES-DESIGN-DELIVERY-001
→ composição e integridade do pacote externo

branch delivery/design-handoff-v1
→ snapshot de distribuição
→ não é fonte canônica paralela

OUTPUT DE DESIGN
→ EXPLORAÇÃO
→ requer validação humana antes de qualquer promoção
```

A branch de entrega não deve ser mesclada na `main` para duplicar os documentos canônicos. Se qualquer fonte obrigatória evoluir materialmente, deve ser avaliada a emissão de nova versão do pacote em vez de substituição silenciosa de arquivos dentro do snapshot v1.

## 8. Preservação

`ressincronização documental concluída ≠ produto implementado ≠ operação comprovada`.

`Design autorizado ≠ solução aprovada ≠ output canônico ≠ implementação ≠ publicação`.

Para Organizações e Coletivos:

`decisão histórica sem wireframe ≠ proibição procedimental vigente`, pois o handoff posterior de Design governa esse limite específico.

Para a Home Guivos Ads:

`produto especializado existente ≠ Home específica construída ≠ Design autorizado automaticamente`.