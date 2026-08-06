---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: draft
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-005
  - UXA-070
  - UXA-075
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Galeria Visual Integrada de Telas

## 1. Finalidade

Esta seção reúne os 97 SVGs canônicos para inspeção humana de assertividade, sequência, coerência e cobertura.

A UXA-083 reformula somente a organização documental da galeria. Nenhum SVG é alterado, nenhuma tela é criada e nenhuma continuidade passa a ser considerada validada por proximidade visual.

## 2. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md) — uma linha para cada um dos 97 arquivos;
- [Catálogo Integrado de Telas](screen-catalog.md) — visão agregada por família;
- [Registro Granular de Superfícies e Estados](surface-registry.md);
- [Registro Granular de Transições](transition-registry.md);
- [Lacunas e Continuidades Ausentes](gaps.md).

## 3. Rota canônica de inspeção

A rota abaixo organiza a leitura documental. Ela não representa uma única jornada de produto.

| Ordem | Página | SVGs | Continuidade examinada |
|---:|---|---:|---|
| 1 | [Pessoa — Fundação, Entrada, Compreensão e Recorrência](screen-gallery-person.md) | 19 | Home → início protegido → expressão → compreensão → Tela Hoje |
| 2 | [Organização e Oportunidades](screen-gallery-opportunities-organization.md) | 9 | publicação institucional → mapa → lista → detalhe → fronteira |
| 3 | [Coletivos](screen-gallery-collectives.md) | 23 | descoberta → perfil → solicitação → pendência → operação ausente |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → ativação → exposição identificada → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
|  | **Total** | **97** | **87 validados localmente; 10 pendentes** |

Cada página contém navegação anterior, índice, matriz e próxima página.

## 4. Sequências funcionais destacadas

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
→ gestão de solicitações
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

A galeria possui SVGs apenas até Solicitação Pendente e uma referência inicial de Coletivo.

## 5. Cobertura auditada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | 97 |
| com validação funcional de origem | 87 |
| pendentes de validação específica | 10 |
| IDs com referência visual direta ou agrupada | 25 de 40 |
| responsabilidades sem SVG dedicado | 14 |
| fronteira documental sem tela por definição | 1 |

## 6. Responsabilidades sem SVG dedicado

- `GKR-SURF-COL-002` — Visão Geral do Responsável;
- `GKR-SURF-COL-003` — gestão completa de solicitações;
- `GKR-SURF-PER-106` — Meus Coletivos;
- `GKR-SURF-PER-107` — Central de Atualizações;
- `GKR-SURF-PER-108` — Início do Participante;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 7. Resolução dos achados da UXA-082

| Achado | Reformulação executada |
|---|---|
| ordem incorreta da Pessoa | página reordenada pela sequência registrada |
| Home e Tela Hoje agrupadas | superfícies separadas em extremos da sequência |
| ausência de rota entre páginas | navegação anterior, índice, matriz e próxima página |
| ausência de rastreabilidade por arquivo | matriz individual para os 97 SVGs |
| versões divergentes | galeria 0.3.0 e páginas 0.2.0 sincronizadas |

## 8. Estado

A galeria permanece `draft` e **reformulada, aguardando revalidação funcional e visual**.

A reformulação não promove a galeria, não valida jornadas, não fecha lacunas e não inicia protótipo ou Engenharia de Produto.

## 9. Próxima transição possível

**UXA-084 — Revalidação Funcional e Visual da Galeria Integrada Reformulada**, mediante autorização separada.
