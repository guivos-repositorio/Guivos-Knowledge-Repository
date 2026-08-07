---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.15.0
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

A UXA-096 reforma somente as referências vigentes de `PER-107` e `PER-108`, revalida ambas e fecha `TRN-111` sem acrescentar SVG.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que as jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- 108 SVGs compartilham 28 perfis de rastreabilidade;
- 9 responsabilidades continuam sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- **98 SVGs possuem validação funcional vigente**;
- **10 aguardam validação específica**, exclusivamente UXA-055;
- `TRN-110` e `TRN-111` estão integralmente validadas;
- oito transições do trecho governado de Coletivos estão integralmente validadas: `105`, `106`, `107`, `108`, `109`, `110`, `111`, `112`.

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
|  | **Total** | **108** | **98 validados; 10 pendentes** |

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
→ Central de Atualizações validada
→ TRN-111 integralmente validada
→ Início do Participante validado
```

## 6. Cobertura confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **108** |
| associações individuais | **108** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **98** |
| pendentes de validação específica | **10** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira documental sem tela | 1 |

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 8. Efeito da UXA-096

- 0 SVGs novos e 2 SVGs existentes reformulados;
- 108 SVGs, 28 perfis e 30 IDs com referência visual preservados;
- validações vigentes: 96 → **98**;
- pendências: 12 → **10**, exclusivamente UXA-055;
- `PER-107` e `PER-108` validados na versão corrente;
- `TRN-111` parcial → integralmente validada;
- nenhuma jornada promovida.

## 9. Estado

A galeria está `active` 0.15.0. A página de Coletivos está `active` 0.13.0 e a matriz por SVG está `active` 0.13.0 no pacote proposto pela UXA-096.

O status `active` aprova somente os instrumentos documentais de inspeção. Não inicia protótipo ou Engenharia de Produto.

## 10. Próxima transição possível

A próxima priorização deverá partir das lacunas remanescentes. **UXA-097 não foi iniciada.**
