---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.6.0
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
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os 98 SVGs canônicos para inspeção humana de assertividade, sequência, coerência e cobertura.

A organização documental foi reformulada pela UXA-083, revalidada pela UXA-084 e promovida como instrumento documental pela UXA-085. A UXA-086 acrescenta uma nova referência de baixa fidelidade para `GKR-SURF-COL-002`, sem validar funcionalmente a superfície ou a continuidade associada.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que todos os SVGs estejam funcionalmente validados.

Ressalvas vigentes:

- 98 SVGs compartilham 24 perfis de rastreabilidade;
- 13 responsabilidades continuam sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- dez estados da UXA-055 continuam sem validação funcional específica;
- o SVG da UXA-086 também aguarda validação funcional específica;
- continuidades entre pacotes permanecem parciais ou não examinadas.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md) — uma linha para cada um dos 98 arquivos;
- [Catálogo Integrado de Telas](screen-catalog.md) — visão agregada por família;
- [Registro Granular de Superfícies e Estados](surface-registry.md);
- [Registro Granular de Transições](transition-registry.md);
- [Lacunas e Continuidades Ausentes](gaps.md).

## 4. Rota canônica de inspeção

A rota abaixo organiza a leitura documental. Ela não representa uma única jornada de produto.

| Ordem | Página | SVGs | Continuidade examinada |
|---:|---|---:|---|
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | 19 | Home → início protegido → expressão → compreensão → Tela Hoje |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 9 | publicação institucional → mapa → lista → detalhe → fronteira |
| 3 | [Coletivos](screen-gallery-collectives.md) | 24 | descoberta → perfil → solicitação → pendência → Visão Geral do Responsável |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → ativação → exposição identificada → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
|  | **Total** | **98** | **87 validados funcionalmente; 11 pendentes** |

As páginas são instrumentos documentais ativos. A presença de um SVG não valida automaticamente a continuidade que ele representa.

## 5. Sequências funcionais destacadas

### Pessoa

```text
Home pública
→ entrada protegida
→ escolha de modalidade
→ expressão guiada
→ inventário e autorização
→ processamento
→ compreensão inicial revisável
→ Tela Hoje
```

A passagem final continua `não examinada` como conjunto.

### Organização e oportunidades

```text
Visão Geral da Organização
→ cadastro e ativação
→ mapa
→ lista sincronizada
→ detalhe
→ fronteira externa
```

A publicação e a descoberta permanecem em pacotes distintos.

### Coletivos

```text
explorar e buscar
→ Perfil Público
→ revisão e solicitação
→ Solicitação Pendente
→ Visão Geral do Responsável
→ gestão completa de solicitações
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

A galeria agora possui referência visual para a Visão Geral do Responsável. A gestão completa de solicitações e as superfícies posteriores permanecem ausentes ou parciais.

## 6. Cobertura confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | 98 |
| associações individuais | 98 |
| perfis de rastreabilidade | 24 |
| com validação funcional registrada | 87 |
| pendentes de validação específica | 11 |
| IDs com referência visual direta ou agrupada | 26 de 40 |
| responsabilidades sem SVG dedicado | 13 |
| fronteira documental sem tela por definição | 1 |

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-COL-003` — gestão completa de solicitações;
- `GKR-SURF-PER-106` — Meus Coletivos;
- `GKR-SURF-PER-107` — Central de Atualizações;
- `GKR-SURF-PER-108` — Início do Participante;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 8. Efeito da UXA-086

`GKR-SURF-COL-002` deixa de constar como responsabilidade sem SVG dedicado. A nova referência:

- está associada ao perfil `R24`;
- possui autoridade em UXA-014, UXA-056, UXA-058 e UXA-059;
- permanece sem validação funcional específica;
- não fecha `GKR-TRN-112`;
- não cria `GKR-SURF-COL-003`.

## 9. Estado

A galeria está `active` 0.6.0. A página de Coletivos está `active` 0.4.0 e a matriz por SVG está `active` 0.4.0.

O status `active` aprova somente os instrumentos documentais de inspeção. Não valida jornadas ponta a ponta, não promove superfícies ou transições e não inicia protótipo ou Engenharia de Produto.

## 10. Próxima transição possível

**UXA-087 — Validação Funcional da Visão Geral do Responsável do Coletivo**, mediante autorização separada.

A UXA-087 não é iniciada por esta atualização da galeria.
