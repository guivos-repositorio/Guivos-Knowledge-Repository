---
id: GKR-JOURNEY-SCREEN-GALLERY-001
title: Galeria Visual Integrada de Telas
status: active
version: 0.12.0
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
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
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

A UXA-093 adiciona a referência móvel de `GKR-SURF-PER-107 — Central de Atualizações` sem reformular ativos existentes e sem executar validação funcional da nova superfície.

## 2. Estado do instrumento

A galeria permanece `active` como instrumento de inspeção. Esse status não significa que suas demais transições ou jornadas estejam automaticamente aprovadas.

Ressalvas vigentes:

- 107 SVGs compartilham 27 perfis de rastreabilidade;
- 10 responsabilidades continuam sem SVG dedicado;
- uma fronteira permanece corretamente sem tela;
- 11 SVGs aguardam validação específica: dez da UXA-055 e a nova referência UXA-093;
- `PER-105` aprovado e `PER-106` permanecem validados na versão corrente;
- `GKR-TRN-108` está integralmente validada;
- `PER-107` está materializada, mas não validada;
- `GKR-TRN-110` permanece parcial mesmo com ambos os endpoints materializados;
- `GKR-TRN-111` permanece ausente por `PER-108` não vigente;
- as cinco transições validadas pela UXA-090 permanecem integralmente validadas.

## 3. Instrumentos de inspeção

- [Matriz de Rastreabilidade Visual por SVG](screen-gallery-traceability-matrix.md) — uma associação para cada um dos 107 arquivos;
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
| 3 | [Coletivos](screen-gallery-collectives.md) | 33 | descoberta → perfil → solicitação → pendência → gestão responsável → resultado aprovado → Meus Coletivos → Central de Atualizações |
| 4 | [Opportunity Boost — Configuração e Exposição](screen-gallery-opportunity-boost-exposure.md) | 20 | configuração → ativação → exposição identificada → retorno orgânico |
| 5 | [Opportunity Boost — Operação, Relatórios e Resíduos](screen-gallery-opportunity-boost-operations.md) | 26 | gestão → relatório → estados residuais |
|  | **Total** | **107** | **96 validados funcionalmente; 11 pendentes** |

As páginas são instrumentos documentais ativos. A presença ou a validação de um SVG não valida automaticamente toda continuidade que ele representa.

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
→ gestão de solicitações
→ resultado aprovado em PER-105
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

O trecho de aprovação até `PER-106` está validado no escopo de `TRN-108`. `PER-107` passa a estar materializada pela UXA-093, porém ainda não validada, `TRN-110` permanece parcial e `PER-108` continua com reformulação pendente. A sequência completa de Coletivos não está validada como jornada ponta a ponta.

## 6. Cobertura confirmada

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| com validação funcional vigente | 96 |
| pendentes de validação específica | 11 |
| IDs com referência visual direta ou agrupada | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |
| fronteira documental sem tela por definição | 1 |

Os onze pendentes são os dez estados residuais da UXA-055 e a nova referência de `PER-107` da UXA-093.

## 7. Responsabilidades sem SVG dedicado

- `GKR-SURF-PER-108` — Início do Participante;
- `GKR-SURF-COL-004` a `GKR-SURF-COL-008`;
- `GKR-SURF-ORG-004` a `GKR-SURF-ORG-007`.

`GKR-SURF-BND-001` permanece intencionalmente sem tela Guivos.

## 8. Efeito da UXA-093

A UXA-093:

- adiciona 1 SVG, elevando o total para 107;
- mantém o inventário granular em 40 superfícies e 37 transições;
- eleva os perfis de rastreabilidade de 26 para 27;
- eleva os IDs com referência visual de 28 para 29;
- reduz responsabilidades sem SVG dedicado de 11 para 10;
- mantém 96 validações funcionais vigentes;
- eleva pendências de 10 para 11 por adicionar um novo SVG ainda não validado;
- materializa `PER-107`;
- preserva `TRN-110` como parcial e `TRN-111` como ausente.

## 9. Estado

A galeria está `active` 0.12.0. A página de Coletivos está `active` 0.10.0 e a matriz por SVG está `active` 0.10.0 no pacote proposto pela UXA-093.

O status `active` aprova somente os instrumentos documentais de inspeção. Não valida jornadas ponta a ponta, não inicia protótipo ou Engenharia de Produto e não autoriza UXA-094 automaticamente.

## 10. Próxima transição possível

**UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de `GKR-TRN-110`**, mediante autorização separada.

A UXA-094 não é iniciada por esta atualização da galeria.