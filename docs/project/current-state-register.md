---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.08.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-05
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
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
  - UXA-082
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GEM-004-A1
  - GEM-007-A1
  - GEM-010-A2
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - ROADMAP-12.55.0
  - M7.72
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente quando o incremento correspondente estiver integrado ao ramo principal.

Em caso de divergência entre resumos, este documento prevalece sobre painéis e marcos não normativos.

## 2. Estado global

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | galeria visual validada como inventário, não aprovada para promoção e lacunas repriorizadas por dependência | UXA-082; M7.72 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | 40 entradas e 37 transições em instrumentos `active` | UXA-076 a UXA-080 |
| Galeria visual | 97 SVGs reunidos; `draft` 0.2.0; reformulação obrigatória | UXA-081; UXA-082 |
| Jornadas Integradas | visão geral e instrumentos ativos; Pessoa, Coletivo e Organização em `draft` | UXA-070 a UXA-082 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Resultados Empresariais

| Estado dos candidatos | Quantidade |
|---|---:|
| decisões humanas registradas | 18 |
| em validação | 9 |
| fundidos | 3 |
| rejeitados | 6 |
| Resultados Empresariais canônicos | 0 |

As UXA-070 a UXA-082 não alteram decisões empresariais, critérios de canonicidade ou evidências de mercado.

## 4. Baseline comercial candidata

Permanecem candidatos, sem promoção canônica automática:

- planos para Pessoas, Coletivos e Organizações;
- Opportunity Boost como add-on publicitário;
- premissas candidatas de orçamento, CPM e CPC;
- Guivos Ads como operador econômico do mecanismo publicitário.

A galeria ou sua validação não comprova preço, demanda, conversão, receita ou viabilidade.

## 5. Cobertura visual confirmada

| Família | SVGs | Validados | Pendentes |
|---|---:|---:|---:|
| fundação pública e experiência recorrente | 2 | 2 | 0 |
| início protegido, compreensão e expressão guiada | 17 | 17 | 0 |
| oportunidades orgânicas | 7 | 7 | 0 |
| Organização | 2 | 2 | 0 |
| Coletivo — referência inicial | 1 | 1 | 0 |
| Coletivos — cobertura móvel | 22 | 22 | 0 |
| Opportunity Boost | 46 | 36 | 10 |
| **Total** | **97** | **87** | **10** |

Os dez pendentes pertencem à UXA-055.

## 6. Cobertura perante os IDs granulares

| Condição | Quantidade |
|---|---:|
| IDs com referência visual direta ou agrupada | 25 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira documental sem tela por definição | 1 |
| **Total** | **40** |

A quantidade de SVGs é maior porque uma responsabilidade pode possuir vários estados e dispositivos.

## 7. Sequência do ambiente documental

```text
UXA-070 a UXA-075 — Jornadas Integradas estruturadas e promovidas seletivamente
→ UXA-076 a UXA-080 — registros granulares estruturados, corrigidos, revalidados e promovidos
→ UXA-081 — galeria visual materializada e cobertura auditada
→ UXA-082 — galeria validada como inventário, promoção bloqueada e lacunas repriorizadas
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 8. Resultado da UXA-082

A UXA-082 confirmou que a galeria é utilizável como inventário e ponto de acesso aos 97 SVGs, mas não a aprovou como sequência integrada ou matriz de assertividade.

Achados bloqueadores:

1. ordem funcional incorreta na página da Pessoa;
2. Home pública e Tela Hoje agrupadas em um mesmo bloco;
3. ausência de rota integrada de inspeção;
4. associação agrupada insuficiente para leitura por SVG;
5. divergência de versões documentais.

A galeria permanece `draft` 0.2.0 e exige reformulação controlada.

## 9. Prioridade operacional de Coletivos

A primeira frente futura de materialização foi reorganizada por dependência:

| Ordem | Superfície | ID | Estado visual |
|---:|---|---|---|
| 1 | Visão Geral do Responsável | GKR-SURF-COL-002 | ausente |
| 2 | gestão completa de solicitações | GKR-SURF-COL-003 | apenas efeitos na visão da Pessoa |
| 3 | Meus Coletivos | GKR-SURF-PER-106 | ausente |
| 4 | Central de Atualizações | GKR-SURF-PER-107 | ausente |
| 5 | Início do Participante | GKR-SURF-PER-108 | reformulação pendente |

A ordem respeita `GKR-TRN-112`, `GKR-TRN-108`, `GKR-TRN-110` e `GKR-TRN-111`. Nenhuma superfície foi iniciada.

## 10. Dívidas de validação separadas

Permanecem em fila própria:

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- validação dos dez estados da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

Esses itens não equivalem automaticamente a ausência de novas telas.

## 11. Estado documental

| Camada | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` |
| Pessoa, Coletivo e Organização | `draft` |
| handoffs e cenários | `active` |
| catálogo integrado | `active` 0.7.0 |
| galeria visual | `draft` 0.2.0; não aprovada para promoção |
| lacunas | `active` 0.7.0 |
| registro de superfícies | `active` 0.3.0 |
| registro de transições | `active` 0.3.0 |
| quatro detalhamentos | `active` 0.2.0 |
| protótipo navegável | não iniciado |
| aplicação ou motor | não iniciado |
| teste com pessoas | não iniciado |
| Engenharia de Produto | não iniciada |

## 12. Lacunas vigentes

Permanecem abertas:

- Visão Geral do Responsável;
- gestão bilateral de solicitações;
- Meus Coletivos;
- Central de Atualizações;
- Início do Participante reformulado;
- operação interna do Coletivo;
- relação Organização–Coletivo;
- matriz institucional completa;
- compreensão inicial → Tela Hoje;
- validação dos dez estados da UXA-055;
- publicação–descoberta de oportunidades;
- sincronização entre mapa, lista e detalhe;
- efeitos externos;
- erros, retornos e interrupções integrados.

## 13. Preservações

- visual existente não equivale a decisão visual aprovada;
- inclusão na galeria não altera maturidade;
- superfície validada não equivale a jornada validada;
- promoção do instrumento não promove os objetos;
- status `active` não equivale a completude;
- status `draft` da galeria preserva a reformulação e revalidação pendentes.

## 14. Próxima transição autorizável

**UXA-083 — Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção.**

A UXA-083 não está iniciada e dependerá de autorização separada.
