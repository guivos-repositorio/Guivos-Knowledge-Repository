---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.20.0
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
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 5. Estado documental

| Camada | Estado | Referência |
|---|---|---|
| visão geral das Jornadas Integradas | `active` 0.20.0 | UXA-092 |
| Pessoa, Coletivo e Organização | `draft` | incompletude explícita |
| Jornada da Pessoa | `draft` 0.5.0 | UXA-092 |
| Jornada do Coletivo | `draft` 0.10.0 | UXA-092 |
| handoffs e cenários | `active` | UXA-074; UXA-075; síntese atualizada até UXA-092 |
| catálogo integrado | `active` 0.16.0 | UXA-092 |
| registro de superfícies | `active` 0.9.0 | UXA-092 |
| detalhamento da Pessoa | `active` 0.4.0 | UXA-092 |
| registro de transições | `active` 0.9.0 | UXA-092 |
| galeria visual integrada | `active` 0.11.0 | UXA-092 |
| página de Coletivos | `active` 0.9.0 | UXA-092 |
| matriz por SVG | `active` 0.9.0 | UXA-092 |
| registro de lacunas | `active` 0.17.0 | UXA-092 |
| protótipo, aplicação e motor | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

Os números de versão desta tabela correspondem ao pacote sincronizado da UXA-092 e dependem da integração governada do mesmo conjunto.

## 6. Resultado da UXA-092

A UXA-092:

- reforma e valida `GKR-SURF-PER-106 — Meus Coletivos`;
- reforma novamente e revalida o estado aprovado corrente de `GKR-SURF-PER-105`;
- promove `GKR-TRN-108` a `integralmente validada`;
- preserva as cinco transições integralmente validadas pela UXA-090;
- mantém `GKR-TRN-110` parcial porque `PER-107` continua ausente;
- não cria ou remove SVGs, superfícies, transições ou IDs;
- não materializa `PER-107` ou `PER-108`;
- não promove qualquer jornada.

A continuidade validada deixa explícito que o vínculo é formado pela aprovação autorizada antes da navegação opcional para `Meus Coletivos`.

## 7. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 106 |
| associações individuais | 106 |
| perfis de rastreabilidade | 26 |
| com validação funcional vigente | 96 |
| pendentes de validação específica | 10 |
| IDs com referência visual | 28 de 40 |
| responsabilidades sem SVG dedicado | 11 |
| fronteira sem tela por definição | 1 |

Os dez pendentes remanescentes são exclusivamente os estados residuais da UXA-055.

## 8. Ressalvas

- perfis agregados não substituem análise exclusiva por estado;
- uma versão visual reformulada exige revalidação;
- `GKR-TRN-110` permanece parcial por `PER-107` ausente;
- estados P0B adicionais de `Meus Coletivos` continuam separados;
- Pessoa e Coletivo permanecem `draft`;
- continuidades entre outros pacotes permanecem parciais ou não examinadas;
- instrumento visual `active`, superfície validada e transição documentalmente validada não equivalem a implementação.

## 9. Prioridade de Coletivos

```text
Visão Geral do Responsável — validada
→ TRN-112 — integralmente validada
→ gestão de solicitações — validada
↔ TRN-105/106/107/109 com PER-105 — integralmente validadas
→ resultado aprovado PER-105 — reformulado e revalidado
→ TRN-108 — integralmente validada
→ Meus Coletivos — validado
→ TRN-110 — parcial
→ Central de Atualizações — ausente
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

**UXA-093 — Materialização Controlada da Central de Atualizações (`GKR-SURF-PER-107`)**, mediante autorização separada.

A UXA-093 não foi iniciada.
