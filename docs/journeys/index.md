---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.21.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
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
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SECTION-CLARIFICATION-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne, por referência, as jornadas da Pessoa, do Coletivo e da Organização para permitir leitura contínua, comparação de perspectivas, inspeção visual, análise de handoffs e identificação de lacunas.

Ela não substitui contratos, wireframes, validações ou registros canônicos.

## 2. Como utilizar

1. abra a [Galeria Visual Integrada](screen-gallery.md);
2. percorra a rota canônica entre as cinco páginas;
3. consulte a [Matriz de Rastreabilidade por SVG](screen-gallery-traceability-matrix.md);
4. use o [Catálogo de Telas](screen-catalog.md) para visão agregada;
5. localize superfícies e transições por ID;
6. confira separadamente maturidade, materialização, validação e continuidade;
7. consulte as [Lacunas](gaps.md) sem confundir transição validada documentalmente com jornada implementada.

## 3. Vistas disponíveis

- [Galeria Visual Integrada de Telas](screen-gallery.md)
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

## 4. Sequência governada

```text
UXA-070 a UXA-075 — seção integrada estruturada, reformulada, revalidada e promovida seletivamente
→ UXA-076 a UXA-080 — registros granulares estruturados, corrigidos, revalidados e promovidos
→ UXA-081 a UXA-085 — galeria e matriz auditadas, reformuladas, revalidadas e promovidas
→ UXA-086 — Visão Geral do Responsável materializada
→ UXA-087 — Visão Geral do Responsável reformulada e validada funcionalmente
→ UXA-088 — Gestão de Solicitações do Responsável materializada em sete estados desktop
→ UXA-089 — Gestão de Solicitações reformulada e validada funcionalmente
→ UXA-090 — cinco handoffs elegíveis de solicitação validados ponta a ponta
→ UXA-091 — Meus Coletivos materializada e continuidade pós-aprovação refinada
→ UXA-092 — Meus Coletivos e resultado aprovado revalidados; TRN-108 validada ponta a ponta
→ UXA-093 — Central de Atualizações materializada como referência P0A móvel
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.21.0 | UXA-093 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.6.0 | UXA-093 |
| Jornada do Coletivo | `draft` 0.10.0 | UXA-092 |
| handoffs e cenários | `active` | UXA-074; UXA-075; síntese atualizada até UXA-093 |
| catálogo integrado | `active` 0.17.0 | UXA-093 |
| registro de superfícies | `active` 0.10.0 | UXA-093 |
| detalhamento da Pessoa | `active` 0.5.0 | UXA-093 |
| registro de transições | `active` 0.10.0 | UXA-093 |
| galeria visual integrada | `active` 0.12.0 | UXA-093 |
| página de Coletivos | `active` 0.10.0 | UXA-093 |
| matriz por SVG | `active` 0.10.0 | UXA-093 |
| registro de lacunas | `active` 0.18.0 | UXA-093 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

Os números de versão desta tabela correspondem ao pacote sincronizado da UXA-093 e dependem da integração governada do mesmo conjunto.

## 6. Resultado da UXA-093

A UXA-093:

- cria 1 SVG móvel para `GKR-SURF-PER-107 — Central de Atualizações`;
- materializa a superfície sem executar validação funcional;
- preserva `PER-105` e `PER-106` sem alteração visual e com suas validações vigentes;
- mantém `GKR-TRN-110` parcial apesar de ambos os endpoints estarem materializados;
- mantém `GKR-TRN-111` ausente porque `PER-108` continua sem materialização vigente;
- não cria IDs de superfície ou transição;
- não materializa estados P0B da Central nem áreas P1;
- não promove qualquer jornada.

A Central é tratada como triagem de mudanças com origem, natureza, autoridade, leitura, necessidade de ação e prazo explícitos, não como feed de engajamento.

## 7. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| com validação funcional vigente | 96 |
| pendentes de validação específica | 11 |
| IDs com referência visual | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |
| fronteira sem tela por definição | 1 |

Os onze pendentes são os dez estados residuais da UXA-055 e a referência P0A de `PER-107` criada pela UXA-093.

## 8. Ressalvas

- perfis agregados não substituem análise exclusiva por estado;
- uma versão visual reformulada exige revalidação;
- `PER-107` está materializada, mas não validada;
- `GKR-TRN-110` permanece parcial até exame ponta a ponta;
- `GKR-TRN-111` permanece ausente por `PER-108` não vigente;
- estados P0B adicionais de `Meus Coletivos` e da Central continuam separados;
- Pessoa e Coletivo permanecem `draft`;
- continuidades entre outros pacotes permanecem parciais ou não examinadas;
- instrumento visual `active`, superfície materializada/validada e transição documentalmente validada não equivalem a implementação.

## 9. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ TRN-112 — integralmente validada
→ gestão de solicitações — validada
↔ TRN-105/106/107/109 com PER-105 — integralmente validadas
→ resultado aprovado PER-105 — validado
→ TRN-108 — integralmente validada
→ Meus Coletivos — validado
→ TRN-110 — parcial
→ Central de Atualizações — materializada; validação pendente
→ TRN-111 — ausente
→ Início do Participante — reformulação pendente
```

## 10. Regra de leitura

```text
visual existente
≠ validação funcional automática
≠ transição ponta a ponta automaticamente validada
≠ validação integral documental igual a implementação
≠ jornada completa
```

Valores desconhecidos permanecem `indeterminado`, `ausente` ou `não examinado`.

## 11. Próxima transição possível

**UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de `GKR-TRN-110`**, mediante autorização separada.

A UXA-094 não foi iniciada.