---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.26.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-30
related:
  - UXA-005
  - UXA-070
  - UXA-080
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
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
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os **119 SVGs físicos remanescentes do inventário visual** para inspeção humana de assertividade, sequência, coerência e cobertura.

Após a reconciliação pós-PR #313/#314, a presença de um SVG na galeria não significa que ele permaneça como wireframe vigente. Em particular, os artefatos associados a `UXA-015..018` são históricos `superseded` e permanecem apenas para rastreabilidade.

A D5-C2 adicionou três estados-base low-fidelity para `PER-010 — Meus Objetivos`, `PER-011 — Meus Próximos Passos` e `PER-012 — Minha Evolução`. A D5-C3 os reforma in-place e os valida funcionalmente no limite local de cada superfície, sem promover automaticamente outras famílias.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que as jornadas, os SVGs históricos ou a UX principal de todos os participantes estejam automaticamente aprovados.

Ressalvas vigentes:

- **119 SVGs físicos** permanecem no corpus corrente; os perfis R09/R11 preservam somente proveniência sem ativo F-006;
- o inventário físico inclui artefatos históricos `superseded`;
- **121 SVGs físicos ≠ 121 wireframes vigentes ≠ 121 wireframes validados**;
- o resumo histórico `121 validados / 0 pendentes` está **superseded como claim de maturidade vigente**;
- uma nova contagem agregada de wireframes vigentes/validados não é inferida sem recomputação governada;
- o materialização visual da Organização pertence exclusivamente a Design;
- o materialização visual do Coletivo pertence exclusivamente a Design;
- fluxos especializados independentes preservam sua maturidade documental quando sustentados por autoridade própria;
- **10 responsabilidades** permanecem registradas sem SVG dedicado no snapshot estrutural;
- **duas fronteiras** permanecem corretamente sem tela;
- `PER-010..012` preservam validação local pela D5-C3;
- `TRN-406/407` estão contratadas porque `PER-009` ainda não foi materializada;
- `TRN-417/418` e `TRN-427/428` preservam a maturidade de seus contratos especializados de navegação, sem provar wireframe principal vigente de Coletivo ou Organização;
- `TRN-205` está validada até `BND-001` pela UXA-101, sem validar o processo externo posterior;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem parciais;
- as transições comerciais internas de Planos preservam a maturidade própria do pacote;
- as transições do trecho governado de Coletivos preservam apenas a maturidade sustentada pelas autoridades vigentes e pelos fluxos independentes.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md)
- [Catálogo Integrado de Telas](screen-catalog.md)
- [Planos, Comparação e Cobrança — Galeria Canônica](screen-gallery-plans-billing.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e Continuidades Ausentes](gaps.md)

## 4. Rota de inspeção física

| Ordem | Página | SVGs físicos | Continuidade examinada |
|---:|---|---:|---|
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | **23** | Home → início protegido → expressão → compreensão → primeira Hoje → recorrência → Objetivos/Próximos Passos/Evolução |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 8 | publicação → mapa/lista → detalhe → revisão de saída → fronteira; inclui histórico visual de ORG-001 |
| 3 | [Coletivos](screen-gallery-collectives.md) | 33 | descoberta → solicitação → gestão → Meus Coletivos → Central → Início; inclui histórico visual superseded |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → exposição → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
| 6 | [Planos, Comparação e Cobrança](screen-gallery-plans-billing.md) | **9** | contratos especializados de origem/retorno → plano atual → comparação → contratação/ciclo → resultado/recuperação |
|  | **Total físico** | **119** | **maturidade agregada requer recomputação governada** |

## 5. Cobertura física confirmada

| Indicador | Resultado |
|---|---:|
| SVGs físicos existentes e referenciados | **119** |
| associações individuais físicas | **119** |
| perfis de rastreabilidade | **34** |
| wireframes vigentes/validados agregados | **não inferir; recomputação governada pendente** |
| superfícies/estados/fronteiras | **57** |
| transições documentais | **66** |
| IDs com referência visual no snapshot | **45 de 57** |
| responsabilidades sem SVG dedicado no snapshot | **10** |
| fronteiras documentais sem tela | **2** |

Essas contagens preservam o inventário e a rastreabilidade física. Não anulam supersessões documentais posteriores.

## 6. Responsabilidades sem SVG dedicado e wireframes principais pendentes

No snapshot estrutural, permanecem sem SVG dedicado:

- `GKR-SURF-PER-009`;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

Além disso, após a reconciliação:

- `GKR-SURF-ORG-001` possui artefato histórico, mas sua materialização visual não é definida pela documentação e pertence exclusivamente a Design;
- a experiência principal autenticada do Coletivo possui artefatos históricos/locais, mas sua materialização visual pertence exclusivamente a Design.

`GKR-SURF-BND-001` e `GKR-SURF-BND-002` permanecem intencionalmente sem tela Guivos. O estado de revisão de saída pertence a `PER-203` e não altera essa regra.

## 7. Fronteiras de validação

A existência de 121 SVGs físicos não implica que todas as 66 transições, todas as superfícies ou todas as jornadas estejam integralmente validadas. Em particular:

- `PER-010`, `PER-011` e `PER-012` estão **validados localmente pela D5-C3**;
- `TRN-008..013` preservam seu estado documental próprio;
- `TRN-406/407` permanecem contratadas;
- `TRN-417/418` e `TRN-427/428` preservam a validade de contratos especializados de navegação, não de uma composição visual principal ainda pendente;
- `TRN-205` é integral somente **até a fronteira de autoridade Guivos**;
- `TRN-401` a `405`, `411` a `415` e `421` a `425` preservam maturidade local no pacote de Planos;
- `TRN-304`, `305`, `306`, `416` e `426` permanecem parciais;
- cobrança real, gateway, proration e processo após `BND-002` permanecem fora do escopo;
- `UXA-015..018` não podem ser usadas como evidência vigente de validação dos wireframes principais de Organização e Coletivo.

O status `active` aprova somente o instrumento documental de inspeção. Não inicia protótipo ou Engenharia de Produto.

## 8. Estado após o cleanup F-006

Os dois SVGs F-006 foram removidos do corpus corrente. A proveniência permanece no histórico Git. A auditoria repo-wide passa a aplicar a regra estrutural de que documentação funcional não deve materializar interface.

```text
DOCUMENTAÇÃO
→ CONTRATO FUNCIONAL / CONTEÚDO / ESTADOS / REGRAS / CRITÉRIOS

DESIGN
→ AUTORIDADE EXCLUSIVA DE MATERIALIZAÇÃO VISUAL
```

Pessoa, Coletivo e Organização continuam `draft`. Para Organização e Coletivo, Jobs + Arquitetura da Informação autenticada estão definidos documentalmente em estado **pre-surface-map** por `GKR-UX-ORGCOL-AUTH-IA-001`; permanecem pendentes o mapa final de superfícies/estados e os wireframes principais autenticados. V5/UXA-102, D6 e D7 não foram iniciadas e nenhuma implementação técnica é iniciada automaticamente.