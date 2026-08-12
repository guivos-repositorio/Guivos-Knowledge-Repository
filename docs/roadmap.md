---
id: ROADMAP-12.76.0
title: Roadmap Arquitetural — Consolidação Documental P0–P9
status: active
version: 12.76.0
owner: Guivos
last_updated: 2026-08-12
supersedes_partial:
  - ROADMAP-12.75.0
related:
  - GKR-STATE-001
  - GKR-P9-GLOBAL-CONSOLIDATION-001
  - GOG-001
  - UXA-101
  - GTM-007
  - GTM-008
  - GKR-HOME-P5
  - GKR-HOME-DECISION-NO-WIREFRAME-001
  - M7.88
---

# Roadmap Arquitetural — Consolidação Documental P0–P9

## 1. Autoridade

Este roadmap registra o estado global após a ressincronização documental de agosto de 2026 e a decisão humana pós-P5 sobre a continuidade da Home Pública de Organizações e Coletivos. O estado oficial permanece em `GKR-STATE-001`.

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
| Home de Organizações e Coletivos — P1–P5 | concluída no limite de prontidão documental |
| continuidade pós-P5 da Home de Organizações e Coletivos | **sem wireframe; próxima forma de materialização não definida e sujeita a autorização humana separada** |

## 3. Sequência funcional preservada

```text
UXA-097 — compreensão inicial → Tela Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — estados residuais Opportunity Boost
→ UXA-100 — Planos
→ UXA-101 — saída consciente → BND-001
→ UXA-102/V5 — PENDENTE, NÃO INICIADA
```

Nenhuma frente P0–P9 nem a decisão pós-P5 da Home cria nova UXA.

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

A sequência P1–P5 específica da Home Pública de Organizações e Coletivos permanece historicamente válida. `GKR-HOME-P5` registrou prontidão suficiente para uma decisão humana sobre a etapa seguinte; `GKR-HOME-DECISION-NO-WIREFRAME-001`, posterior, determinou que **wireframe não será utilizado como etapa de continuidade dessa Home**.

Essa decisão não reescreve P1–P5, não deprecia `UXA-022` da Main Home e não autoriza automaticamente Figma, protótipo, UI, implementação ou publicação.

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
- UXA-102/V5;
- Product Engineering;
- definição, por decisão humana separada, do caminho de materialização da Home de Organizações e Coletivos **sem wireframe**.

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
- Home de Organizações e Coletivos → escolha humana separada de um caminho de materialização que **não passe por wireframe**.

## 7. Preservação

`ressincronização documental concluída ≠ produto implementado ≠ operação comprovada`.

Para a Home de Organizações e Coletivos, adicionalmente:

`P5 concluído ≠ wireframe autorizado ≠ Figma autorizado ≠ UI autorizada ≠ implementação autorizada ≠ publicação autorizada`.