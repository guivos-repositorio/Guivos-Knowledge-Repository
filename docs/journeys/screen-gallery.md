---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.16.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
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
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os **109 SVGs canônicos** para inspeção humana de assertividade, sequência, coerência e cobertura.

A UXA-097 adiciona a primeira variante de `PER-008 — Tela Hoje`, reforma somente o estado de decisão de `PER-007` e valida `TRN-007` ponta a ponta. A Tela Hoje recorrente permanece inalterada.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que as jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- 109 SVGs compartilham 28 perfis de rastreabilidade;
- 9 responsabilidades continuam sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- **99 SVGs possuem validação funcional vigente**;
- **10 aguardam validação específica**, exclusivamente UXA-055;
- `TRN-007`, `TRN-110` e `TRN-111` estão integralmente validadas nos respectivos escopos;
- oito transições do trecho governado de Coletivos permanecem integralmente validadas: `105`, `106`, `107`, `108`, `109`, `110`, `111`, `112`.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md)
- [Catálogo Integrado de Telas](screen-catalog.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e Continuidades Ausentes](gaps.md)

## 4. Rota canônica de inspeção

| Ordem | Página | SVGs | Continuidade examinada |
|---:|---|---:|---|
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | **20** | Home → início protegido → expressão → compreensão → primeira Hoje → recorrência |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 9 | publicação → mapa → lista → detalhe → fronteira |
| 3 | [Coletivos](screen-gallery-collectives.md) | 34 | descoberta → solicitação → gestão → Meus Coletivos → Central → Início |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → exposição → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
|  | **Total** | **109** | **99 validados; 10 pendentes** |

## 5. Sequência pessoal fechada no gate UXA-097

```text
compreensão inicial revisável
→ escolhas explícitas
→ TRN-007 integralmente validada
→ primeira Tela Hoje
→ recorrência separada
```

A validação do trecho não promove a Jornada da Pessoa porque handoffs anteriores continuam parciais.

## 6. Sequência de Coletivos preservada

```text
explorar e buscar
→ Perfil Público
→ revisão e solicitação
→ Solicitação Pendente
→ gestão responsável
→ resultado aprovado
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

## 7. Cobertura confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **109** |
| associações individuais | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **99** |
| pendentes de validação específica | **10** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira documental sem tela | 1 |

## 8. Responsabilidades sem SVG dedicado

- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 9. Efeito da UXA-097

- 1 SVG novo e 1 SVG existente reformulado;
- SVGs: 108 → **109**;
- associações: 108 → **109**;
- perfis: **28**, sem novo perfil;
- validações vigentes: 98 → **99**;
- pendências: **10**, exclusivamente UXA-055;
- `PER-007` corrente revalidado;
- primeira variante de `PER-008` validada;
- `TRN-007` não examinada → integralmente validada;
- nenhuma jornada promovida.

## 10. Estado

A galeria está `active` 0.16.0. A página da Pessoa está `active` 0.4.0 e a matriz por SVG passa a `active` 0.14.0 no pacote proposto pela UXA-097.

O status `active` aprova somente os instrumentos documentais de inspeção. Não inicia protótipo ou Engenharia de Produto.

## 11. Próxima transição possível

Com `V1` fechada, a prioridade vigente passa a `V2 — publicação → descoberta/mapa/lista/detalhe`. **UXA-098 não foi iniciada.**