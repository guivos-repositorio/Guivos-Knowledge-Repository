---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-005
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Catálogo Integrado de Telas

## 1. Regra de leitura

O catálogo distingue cobertura visual, cobertura das superfícies, cobertura das transições e validação da jornada integrada.

```text
SVG existente
≠ superfície granular adicional
≠ transição validada
≠ jornada integrada validada
```

A inspeção direta dos 97 arquivos está disponível na [Galeria Visual Integrada de Telas](screen-gallery.md).

## 2. Inventário agregado por família

| Participante ou camada | Família | SVGs existentes | Validação visual registrada | Entrada integrada | Saída integrada | Lacuna associada |
|---|---|---:|---|---|---|---|
| Pessoa | Home pública e Tela Hoje | 2 | 2 validados | parcial | continuidade não examinada como conjunto | compreensão inicial → Tela Hoje |
| Pessoa | início protegido | 4 | 4 validados | parcial | parcial | reconciliação ponta a ponta |
| Pessoa | compreensão inicial | 5 | 5 validados | parcial | não examinada com Tela Hoje | continuidade recorrente |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | parcial | integração com inventário |
| Pessoa | oportunidades orgânicas | 7 | 7 validados nos pacotes de origem | publicação não examinada | efeito externo parcial | publicação, sincronização e fronteira |
| Pessoa em Coletivos | descoberta e busca | 5 | 5 validados | parcial | parcial | continuidade entre famílias |
| Pessoa em Coletivos | Perfil Público | 4 | 4 validados | parcial | parcial | handoff para solicitação |
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 validados | parcial | parcial | destino operacional do Coletivo |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados na perspectiva da Pessoa | parcial | ausente após decisão | Meus Coletivos e visão do responsável |
| Coletivo | referência inicial | 1 | 1 validado | não examinada | não examinada | Visão Geral do Responsável |
| Organização | visão geral e cadastro de oportunidade | 2 | 2 validados | parcial | publicação–descoberta não examinada | matriz institucional completa |
| camada comercial | Opportunity Boost | 46 | 36 validados; 10 pendentes | parcial | parcial | estados residuais da UXA-055 |
| fronteira documental | destino externo identificado | 0 | não aplicável | parcial | não examinada | efeito externo |
| **Total de SVGs** |  | **97** | **87 validados; 10 pendentes** |  |  |  |

As contagens pertencem a escopos distintos. Variações de estado e dispositivo não devem ser somadas como novas superfícies.

## 3. Estado dos registros granulares

A UXA-080 promoveu os instrumentos revalidados:

| Registro | Quantidade | Estado |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | `active` 0.3.0 |
| transições documentais | 37 | `active` 0.3.0 |
| referências de endpoint | 74 | resolvidas |
| endpoints em texto livre | 0 | aprovado |
| detalhamentos obrigatórios | 4 | `active` 0.2.0 |

- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)

O status `active` aprova os instrumentos documentais. Ele não promove automaticamente os objetos registrados.

## 4. Auditoria de cobertura visual

| Condição | IDs |
|---|---:|
| com referência visual direta ou agrupada | 25 |
| sem SVG dedicado | 14 |
| fronteira intencionalmente sem tela | 1 |
| **Total** | **40** |

Os 14 IDs sem SVG dedicado concentram-se principalmente na continuidade de Coletivos e nas relações institucionais:

- Meus Coletivos;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- operação da gestão de solicitações;
- participantes e vínculos;
- comunicação oficial;
- atividades, consultas e decisões;
- proteção e moderação;
- relações institucionais do Coletivo;
- proposta, negociação e relação ativa Organização–Coletivo;
- resultados e evidências institucionais.

`GKR-SURF-BND-001` permanece corretamente sem tela Guivos.

## 5. Separações obrigatórias

### Coletivos

`GKR-SURF-PER-102` representa exclusivamente Resultados de Busca de Coletivos.

### Oportunidades

- `GKR-SURF-PER-201` — Mapa de Oportunidades;
- `GKR-SURF-PER-202` — Lista de Oportunidades;
- `GKR-SURF-PER-203` — Detalhe de Oportunidade;
- `GKR-SURF-ORG-003` — estado institucional de oportunidade aprovada ou ativa;
- `GKR-SURF-BND-001` — fronteira externa documental.

### Opportunity Boost

`GKR-SURF-COM-005` aponta para UXA-055. Seus dez SVGs permanecem materializados sem validação funcional específica.

## 6. Regra de fonte única

A galeria incorpora os SVGs por referência aos caminhos canônicos em `docs/assets/wireframes/`. Ela não duplica ou modifica os arquivos.

A presença na galeria ou no catálogo:

- não altera maturidade;
- não valida transição;
- não fecha lacuna;
- não declara assertividade visual;
- não autoriza implementação.

## 7. Estado vigente

- catálogo: `active` 0.6.0;
- galeria visual: `draft` 0.1.0;
- registros granulares: `active`;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

A galeria aguarda revisão funcional e visual específica.
