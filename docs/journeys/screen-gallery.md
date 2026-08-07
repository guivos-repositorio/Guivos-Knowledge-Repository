---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.8.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-005
  - UXA-070
  - UXA-075
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os **105 SVGs canônicos** para inspeção humana de assertividade, sequência, coerência e cobertura.

A UXA-088 acrescenta sete referências desktop para `GKR-SURF-COL-003 — gestão de solicitações` sem validar funcionalmente a família.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que todos os SVGs estejam funcionalmente validados nem que suas transições estejam aprovadas.

Ressalvas vigentes:

- 105 SVGs compartilham 25 perfis de rastreabilidade;
- 12 responsabilidades continuam sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- dez estados da UXA-055 continuam sem validação funcional específica;
- sete estados da UXA-088 aguardam validação funcional específica;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- `GKR-TRN-105` a `GKR-TRN-109` e `GKR-TRN-112` continuam sem validação ponta a ponta.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md) — uma linha para cada um dos 105 arquivos;
- [Catálogo Integrado de Telas](screen-catalog.md);
- [Registro Granular de Superfícies e Estados](surface-registry.md);
- [Registro Granular de Transições](transition-registry.md);
- [Lacunas e Continuidades Ausentes](gaps.md).

## 4. Rota canônica de inspeção

| Ordem | Página | SVGs | Continuidade examinada |
|---:|---|---:|---|
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | 19 | Home → início protegido → expressão → compreensão → Tela Hoje |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 9 | publicação institucional → mapa → lista → detalhe → fronteira |
| 3 | [Coletivos](screen-gallery-collectives.md) | 31 | descoberta → perfil → solicitação → pendência → visão do responsável → gestão de solicitações |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → ativação → exposição identificada → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
|  | **Total** | **105** | **88 validados funcionalmente; 17 pendentes** |

## 5. Sequências funcionais destacadas

### Pessoa

```text
Home pública → entrada protegida → expressão → compreensão → Tela Hoje
```

A passagem final continua `não examinada` como conjunto.

### Organização e oportunidades

```text
Visão Geral da Organização → cadastro e ativação → mapa → lista → detalhe → fronteira externa
```

### Coletivos

```text
explorar e buscar
→ Perfil Público
→ revisão e solicitação
→ Solicitação Pendente
→ Visão Geral do Responsável — validada
→ gestão de solicitações — materializada; validação pendente
→ Meus Coletivos — ausente
→ Central de Atualizações — ausente
→ Início do Participante — reformulação pendente
```

## 6. Cobertura confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | 105 |
| associações individuais | 105 |
| perfis de rastreabilidade | 25 |
| com validação funcional registrada | 88 |
| pendentes de validação específica | 17 |
| IDs com referência visual direta ou agrupada | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |
| fronteira documental sem tela por definição | 1 |

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-PER-106` — Meus Coletivos;
- `GKR-SURF-PER-107` — Central de Atualizações;
- `GKR-SURF-PER-108` — Início do Participante;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 8. Efeito da UXA-088

`GKR-SURF-COL-003` deixa de estar visualmente ausente e recebe sete referências desktop sob o perfil `R25`:

- fila operacional;
- detalhe comum;
- análise protegida;
- pedido adicional;
- confirmação de aprovação;
- confirmação de recusa;
- autoridade insuficiente.

A materialização não valida os sete SVGs. `TRN-112` passa a possuir ambos os endpoints materializados, mas continua não validada; `TRN-105` a `109` ganham evidência bilateral sem promoção de estado funcional.

## 9. Estado

A galeria está `active` 0.8.0. A página de Coletivos está `active` 0.6.0 e a matriz por SVG deverá ser sincronizada para `active` 0.6.0.

O status `active` aprova somente o instrumento documental. Não valida jornadas ponta a ponta, não inicia protótipo ou Engenharia de Produto e não autoriza UXA-089 automaticamente.

## 10. Próxima transição possível

**UXA-089 — Validação Funcional da Gestão de Solicitações do Responsável do Coletivo**, mediante autorização separada.

A UXA-089 não é iniciada por esta atualização da galeria.
