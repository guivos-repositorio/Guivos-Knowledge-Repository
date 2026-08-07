---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.13.0
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
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os **107 SVGs canônicos** para inspeção humana de assertividade, sequência, coerência e cobertura.

A UXA-094 reforma exclusivamente as referências móveis de `PER-106 — Meus Coletivos` e `PER-107 — Central de Atualizações`, sem adicionar ou remover SVG.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que as jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- 107 SVGs compartilham 27 perfis de rastreabilidade;
- 10 responsabilidades continuam sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- **97 SVGs possuem validação funcional vigente**;
- **10 SVGs aguardam validação específica, todos UXA-055**;
- `PER-106` e `PER-107` estão validados na versão corrente;
- `TRN-110` está integralmente validada;
- `TRN-111` permanece ausente por `PER-108` não vigente;
- sete transições do trecho de Coletivos estão integralmente validadas: `105`, `106`, `107`, `108`, `109`, `110`, `112`.

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
| 3 | [Coletivos](screen-gallery-collectives.md) | 33 | descoberta → solicitação → gestão → resultado → Meus Coletivos → Central |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → exposição → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
|  | **Total** | **107** | **97 validados; 10 pendentes** |

## 5. Sequência de Coletivos

```text
explorar e buscar
→ Perfil Público
→ revisão e solicitação
→ Solicitação Pendente
→ gestão responsável
→ resultado aprovado
→ Meus Coletivos
→ TRN-110 validada
→ Central de Atualizações
→ TRN-111 ausente
→ Início do Participante não vigente
```

O trecho até `PER-107` possui os gates indicados nos registros, mas isso não valida a jornada interna posterior como um conjunto completo.

## 6. Cobertura confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| com validação funcional vigente | **97** |
| pendentes de validação específica | **10** |
| IDs com referência visual | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |
| fronteira documental sem tela | 1 |

Os dez pendentes são exclusivamente UXA-055.

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-PER-108` — Início do Participante;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 8. Efeito da UXA-094

- 0 SVG novo e 2 SVGs existentes reformulados;
- 107 SVGs, 27 perfis e 29 IDs com referência visual preservados;
- validações vigentes: 96 → **97**;
- pendências: 11 → **10**;
- `PER-106` revalidado no gatilho corrente;
- `PER-107` validado;
- `TRN-110` promovida a integralmente validada;
- `TRN-111` preservada como ausente.

## 9. Estado

A galeria está `active` 0.13.0. A página de Coletivos está `active` 0.11.0 e a matriz por SVG está `active` 0.11.0 no pacote proposto pela UXA-094.

O status `active` aprova somente os instrumentos documentais de inspeção. Não inicia protótipo ou Engenharia de Produto.

## 10. Próxima transição possível

**UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`**, mediante autorização separada.

A UXA-095 não foi iniciada.
