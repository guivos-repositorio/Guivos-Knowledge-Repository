---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.5.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-005
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Catálogo Integrado de Telas

## 1. Regra de leitura

O catálogo distingue cobertura das superfícies, cobertura das transições e validação da jornada integrada.

```text
superfície validada
≠ transição de entrada validada
≠ transição de saída validada
≠ jornada integrada validada
```

## 2. Inventário agregado por família

| Participante ou camada | Família | Superfícies materializadas | Superfícies validadas | Entrada integrada | Saída integrada | Perspectiva coberta | Lacuna associada |
|---|---|---:|---:|---|---|---|---|
| Pessoa | início protegido geral | 4 | 4 | parcial | parcial | Pessoa | reconciliação ponta a ponta |
| Pessoa | compreensão inicial | 5 | 5 | parcial | não examinada com Tela Hoje | Pessoa | continuidade recorrente |
| Pessoa | expressão guiada | 8 | 8 | parcial | parcial | Pessoa | integração com inventário |
| Pessoa | mapa de oportunidades | referências do pacote | validadas no escopo de origem | não examinada com publicação | parcial com detalhe | Pessoa ou visitante | integração publicação–descoberta |
| Pessoa | lista de oportunidades | referências do pacote | validadas no escopo de origem | parcial com mapa | parcial com detalhe | Pessoa ou visitante | sincronização integrada |
| Pessoa | Detalhe de Oportunidade | 1 referência principal | validada no escopo de origem | parcial | efeito externo não validado | Pessoa ou visitante | fronteira e resultado externo |
| Pessoa em Coletivos | descoberta e busca | 5 | 5 | parcial | parcial | visitante | continuidade entre famílias |
| Pessoa em Coletivos | Perfil Público | 4 | 4 | parcial | parcial | visitante | handoff para solicitação |
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 | parcial | parcial | solicitante | destino operacional do Coletivo |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 | parcial | ausente após decisão | solicitante | `Meus Coletivos` e visão do responsável |
| Coletivo | Visão Geral existente | referências parciais | validadas no escopo de origem | não examinada | não examinada | responsável | Visão Geral do Responsável completa |
| Organização | Visão Geral | 1 referência principal | validada | parcial | parcial | representante institucional | matriz institucional completa |
| Organização | cadastro e estado de publicação | referências do fluxo | validadas no escopo de origem | parcial | não examinada com descoberta | representante institucional | integração com consumo pela Pessoa |
| camada comercial | Opportunity Boost | 46 | 36 | parcial | parcial | anunciante e Pessoa exposta | 10 estados residuais |
| fronteira documental | destino externo identificado | 0 tela | 0 | parcial | não examinada | Pessoa | efeito externo não validado |

As contagens pertencem a escopos distintos e não devem ser somadas como inventário global homogêneo.

## 3. Registros granulares reformulados

A UXA-078 reformula as vistas detalhadas:

- [Registro Granular de Superfícies e Estados](surface-registry.md);
- [Registro Granular de Transições](transition-registry.md).

Estado quantitativo:

| Registro | Quantidade | Estado |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | `draft` |
| transições | 37 | `draft` |
| endpoints em texto livre | 0 | corrigidos documentalmente |

O aumento frente à versão anterior decorre da separação de mapa, lista, detalhe e fronteira externa. Não representa telas ou comportamentos novos.

## 4. Separações obrigatórias

### Coletivos

`GKR-SURF-PER-102` representa exclusivamente Resultados de Busca de Coletivos.

### Oportunidades

- `GKR-SURF-PER-201` — Mapa de Oportunidades;
- `GKR-SURF-PER-202` — Lista de Oportunidades;
- `GKR-SURF-PER-203` — Detalhe de Oportunidade;
- `GKR-SURF-ORG-003` — estado institucional de oportunidade aprovada ou ativa;
- `GKR-SURF-BND-001` — fronteira externa documental.

### Opportunity Boost

`GKR-SURF-COM-005` aponta para UXA-055 como materialização dos dez estados residuais. A validação funcional específica permanece ausente.

## 5. Campos obrigatórios por referência

Cada entrada granular apresenta:

- ID;
- participante ou perspectiva;
- família e posição;
- canal;
- autoridade;
- materialização;
- validação;
- maturidade;
- entrada e saída;
- continuidade;
- lacuna;
- artefato canônico e caminho;
- versão;
- decisão;
- dados e conteúdos;
- gate;
- reversibilidade;
- supersessão;
- observação de escopo.

Valores não demonstrados são registrados como `indeterminado`, `ausente` ou `não examinado`.

## 6. Regra de fonte única

O catálogo e os registros apontam para o artefato canônico. SVGs, textos normativos e wireframes não são copiados para esta seção.

A presença no catálogo não promove maturidade, não valida uma transição e não fecha uma lacuna.

## 7. Estado vigente

A UXA-074 aprovou este catálogo com ressalva não bloqueadora. A UXA-075 promoveu o documento para `active` como inventário agregado por família.

A UXA-078 corrige a organização granular, mas os registros detalhados permanecem `draft` até nova validação funcional específica.
