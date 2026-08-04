---
id: GKR-CCM-UXA-060-A1
title: Adendo de Consolidação Canônica — UXA-060
status: draft
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-03
parent: GKR-CCM-001
depends_on:
  - UXA-005
  - UXA-056
  - UXA-059
  - UXA-060
related:
  - GKR-STATE-001
  - ROADMAP-12.36.0
  - GKR-ARCHITECTURAL-MILESTONES-001
  - GKR-KNOWLEDGE-BOARD-001
  - GKR-CHANGELOG-1.84.0
  - M7.62
normative: false
---

# Adendo de Consolidação Canônica — UXA-060

## 1. Finalidade

Este adendo registra a consolidação proposta do incremento UXA-060 sem alterar a autoridade dos contratos UXA-056 a UXA-059 ou declarar os novos wireframes funcionalmente validados.

## 2. Incremento examinado

| Elemento | Estado proposto |
|---|---|
| UXA-060 | criada em versão 0.1.0 |
| Canal | móvel |
| SVGs novos | 5 |
| Validação funcional especializada | não iniciada |
| Protótipo, teste e desenvolvimento | não iniciados |
| Marco | M7.62 |

## 3. Artefatos materializados

| Artefato | Responsabilidade |
|---|---|
| `uxa-060-collective-explore-mobile.svg` | exploração geral, busca, categorias, área e origens |
| `uxa-060-collective-search-results-mobile.svg` | consulta, filtros, ordenação, orgânico e patrocinado |
| `uxa-060-collective-search-filters-mobile.svg` | revisão consciente de filtros sem alterar busca |
| `uxa-060-collective-search-no-results-mobile.svg` | zero confirmado, cobertura e recuperação |
| `uxa-060-collective-discovery-origin-mobile.svg` | explicação de publicidade, critérios, exclusões e controles |

## 4. Autoridades preservadas

| Responsabilidade | Autoridade preservada |
|---|---|
| descoberta, busca, origem e ordenação | UXA-056 |
| interação, recomendação e distinção de origens | UXA-058 |
| programa e limite de materialização | UXA-059 |
| convenções de wireframes | UXA-005 |
| publicidade identificada e controles | UXA-038 a UXA-055, no escopo aplicável |
| Mapa e Lista territorial | UXA-024 a UXA-033 |

## 5. Decisões consolidadas

- exploração permanece útil sem personalização;
- busca direta e exploração por categoria coexistem;
- área manual não equivale a localização precisa;
- o primeiro resultado da busca é orgânico;
- publicidade aparece identificada antes do conteúdo;
- publicidade não altera a ordenação orgânica;
- origem é visível por item;
- filtros preservam busca e área até confirmação;
- preferência publicitária não é filtro;
- zero confirmado não é erro;
- publicidade não preenche artificialmente uma busca vazia;
- visualização não cria vínculo, acompanhamento ou contato;
- contagem de participantes não funciona como ranking;
- Coletivos protegidos permanecem fora da busca geral;
- o Perfil Público é continuidade pendente, não tela criada.

## 6. Cobertura contratual

| Estado da UXA-056/059 | Cobertura UXA-060 |
|---|---|
| busca e exploração com resultados | coberto |
| busca sem resultados | coberto |
| filtros | coberto |
| origem da descoberta | coberto |
| publicidade identificada | coberto condicionalmente |
| consulta preservada | coberto |
| localização precisa não obrigatória | coberto |
| destino Perfil Público | apenas ponto de saída |
| falha de busca | não coberto |
| cobertura parcial e baixa conectividade | não cobertas |

## 7. Contagens preservadas

A consolidação deverá manter separadas:

- Opportunity Boost: 46 wireframes materializados, 36 validados por pacote e 10 pendentes;
- Coletivos — descoberta e busca: 5 wireframes materializados e 5 pendentes de validação;
- demais wireframes de Coletivos: não iniciados.

Os cinco novos SVGs não integram retrospectivamente a validação transversal da UXA-050.

## 8. Baselines não alteradas

Permanecem inalterados:

- 18 decisões humanas;
- 9 candidatos de Resultados em validação;
- 3 candidatos fundidos;
- 6 candidatos rejeitados;
- zero Resultados canônicos;
- planos e preços candidatos;
- parâmetros candidatos do Opportunity Boost;
- pausa da Engenharia de Produto antes de W0-01.

## 9. Limites da consolidação

O adendo não:

- valida funcionalmente os cinco SVGs;
- cria Perfil Público;
- cria participação;
- autoriza publicidade real;
- define algoritmo de busca;
- define política final de categorias, localização ou recomendação;
- cria protótipo, teste, design final ou implementação.

## 10. Próximo gate

O próximo gate recomendado é a UXA-061, destinada à validação funcional especializada dos cinco wireframes.

Qualquer reformulação deverá preservar os artefatos originais no histórico e atualizar explicitamente a matriz de cobertura.
