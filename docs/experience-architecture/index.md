---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.81.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - PAS-001
  - GLPA-001
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-037
  - UXA-038
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
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.75
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos em experiências compreensíveis para Pessoas, Coletivos e Organizações. Ela governa hierarquia, decisão, continuidade, confirmação, autoridade, privacidade e proteção antes de implementação.

## 2. Regra de maturidade

```text
contrato funcional
→ programa governado
→ materialização
→ validação funcional
→ reformulação, quando exigida
→ revalidação
→ promoção controlada quando aplicável
→ inspeção integrada
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 105 |
| associações individuais | 105 |
| perfis de rastreabilidade | 25 |
| com validação funcional registrada | 88 |
| pendentes de validação específica | 17 |
| IDs com referência visual | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |

Os 17 pendentes são dez estados residuais da UXA-055 e sete estados da UXA-088.

## 4. Decisões estruturais preservadas

- desconhecido não é fato;
- solicitação não é aprovação;
- pedido adicional não é obrigação de revelar;
- recusa não é reputação ou sanção;
- autoridade insuficiente não pode ser contornada pela interface;
- publicidade não compra relevância, reputação ou autoridade;
- materialização não equivale a validação funcional;
- validação de superfície não equivale a validação de transição;
- presença ou ordem na galeria não valida jornada.

## 5. Evolução das Jornadas Integradas

```text
UXA-070 a UXA-075 — seção integrada estruturada e promovida seletivamente
UXA-076 a UXA-080 — registros granulares estruturados e promovidos
UXA-081 a UXA-085 — galeria e matriz auditadas, reformuladas, revalidadas e promovidas
UXA-086 — COL-002 materializada
UXA-087 — COL-002 reformulada e validada
UXA-088 — COL-003 materializada em sete estados desktop
```

## 6. Resultado da UXA-088

[UXA-088 — Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo](uxa-088-collective-request-management-low-fidelity-wireframes.md) materializa `GKR-SURF-COL-003` em sete estados:

1. fila operacional;
2. detalhe comum;
3. análise protegida;
4. pedido adicional;
5. confirmação de aprovação;
6. confirmação de recusa;
7. autoridade insuficiente.

A UXA-088 não valida funcionalmente a família, não materializa `PER-106`, não promove a Jornada do Coletivo e não inicia Engenharia.

## 7. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active` 0.16.0 |
| Pessoa, Coletivo e Organização | `draft` |
| catálogo integrado | `active` 0.13.0 |
| galeria visual | `active` 0.8.0 |
| página de Coletivos | `active` 0.6.0 |
| matriz por SVG | `active` 0.6.0 |
| lacunas | `active` 0.13.0 |
| registro de superfícies | `active` 0.6.0 |
| registro de transições | `active` 0.5.0 |
| detalhamento do Coletivo | `active` 0.5.0 |

## 8. Ressalvas vigentes

- 12 responsabilidades permanecem sem SVG dedicado;
- dez estados da UXA-055 e sete da UXA-088 permanecem sem validação específica;
- `TRN-105` a `109` e `TRN-112` permanecem sem validação ponta a ponta;
- `PER-106` continua ausente;
- continuidades entre pacotes permanecem parciais ou não examinadas.

## 9. Prioridade de Coletivos

```text
COL-002 — validada
→ COL-003 — materializada; validação pendente
→ PER-106 — Meus Coletivos, ausente
→ PER-107 — Central de Atualizações, ausente
→ PER-108 — Início do Participante, reformulação pendente
```

## 10. Próxima evolução possível

**UXA-089 — Validação Funcional da Gestão de Solicitações do Responsável do Coletivo**, mediante autorização separada.

A UXA-089 não foi iniciada.
