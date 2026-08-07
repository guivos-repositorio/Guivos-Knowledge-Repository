---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.14.0
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
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os **108 SVGs canônicos** para inspeção humana de assertividade, sequência, coerência e cobertura.

A UXA-095 adiciona uma referência móvel de `PER-108 — Início do Participante` e reforma minimamente `PER-107` para tornar `TRN-111` observável.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que as jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- 108 SVGs compartilham 28 perfis de rastreabilidade;
- 9 responsabilidades continuam sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- **96 SVGs possuem validação funcional vigente**;
- **12 aguardam validação específica**: 10 UXA-055 + PER-107 corrente + PER-108;
- `TRN-110` permanece integralmente validada;
- `TRN-111` está **parcial**;
- sete transições do trecho anterior de Coletivos permanecem integralmente validadas: `105`, `106`, `107`, `108`, `109`, `110`, `112`.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md)
- [Catálogo Integrado de Telas](screen-catalog.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e Continuidades Ausentes](gaps.md)

## 4. Rota canônica de inspeção

| Ordem | Página | SVGs | Continuidade examinada |
|---:|---|---:|---|
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | 19 | Home → início protegido → expressão → compreensão → Tela Hoje |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 9 | publicação → mapa → lista → detalhe → fronteira |
| 3 | [Coletivos](screen-gallery-collectives.md) | **34** | descoberta → solicitação → gestão → Meus Coletivos → Central → Início |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → exposição → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
|  | **Total** | **108** | **96 validados; 12 pendentes** |

## 5. Sequência de Coletivos

```text
explorar e buscar
→ Perfil Público
→ revisão e solicitação
→ Solicitação Pendente
→ gestão responsável
→ resultado aprovado
→ Meus Coletivos
→ TRN-110 integralmente validada
→ Central de Atualizações
→ TRN-111 parcial
→ Início do Participante materializado
```

## 6. Cobertura confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **108** |
| associações individuais | **108** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **96** |
| pendentes de validação específica | **12** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira documental sem tela | 1 |

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 8. Efeito da UXA-095

- +1 SVG novo e 1 SVG existente reformulado;
- 108 SVGs, 28 perfis e 30 IDs com referência visual;
- validações vigentes: 97 → **96** pela reformulação pendente de PER-107;
- pendências: 10 → **12**;
- `PER-108` materializado;
- `TRN-111` ausente → parcial;
- nenhuma jornada promovida.

## 9. Estado

A galeria está `active` 0.14.0. A página de Coletivos está `active` 0.12.0 e a matriz por SVG será `active` 0.12.0 no pacote proposto pela UXA-095.

O status `active` aprova somente os instrumentos documentais de inspeção. Não inicia protótipo ou Engenharia de Produto.

## 10. Próxima transição possível

**UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de GKR-TRN-111**, mediante autorização separada.

A UXA-096 não foi iniciada.
