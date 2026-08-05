---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.4.0
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
| Pessoa em Coletivos | descoberta e busca | 5 | 5 | parcial | parcial | visitante | continuidade entre famílias |
| Pessoa em Coletivos | Perfil Público | 4 | 4 | parcial | parcial | visitante | handoff para solicitação |
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 | parcial | parcial | solicitante | destino operacional do Coletivo |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 | parcial | ausente após decisão | solicitante | `Meus Coletivos` e visão do responsável |
| Coletivo | Visão Geral existente | referências parciais | validadas no escopo de origem | não examinada | não examinada | responsável | Visão Geral do Responsável completa |
| Organização | Visão Geral | 1 referência principal | validada | parcial | parcial | representante institucional | matriz institucional completa |
| Organização | cadastro de oportunidade | referências do fluxo | validadas | parcial | parcial | representante institucional | integração com consumo pela Pessoa |
| camada comercial | Opportunity Boost | 46 | 36 | parcial | parcial | anunciante e Pessoa exposta | 10 estados residuais |

As contagens pertencem a escopos distintos e não devem ser somadas como inventário global homogêneo.

## 3. Registros granulares

A UXA-076 materializa duas vistas detalhadas, mantidas em `draft` até validação específica:

- [Registro Granular de Superfícies e Estados](surface-registry.md);
- [Registro Granular de Transições](transition-registry.md).

O registro de superfícies atribui IDs individuais a telas, estados, responsabilidades programadas e ausências conhecidas.

O registro de transições atribui IDs às ligações documentais, distinguindo transições localmente validadas, parciais, contratadas, ausentes e não examinadas.

## 4. Campos obrigatórios por referência

Cada entrada granular registra, quando aplicável:

- ID da superfície ou estado;
- nome compreensível;
- participante e perspectiva;
- família e posição na jornada;
- canal;
- autoridade contratual;
- pacote de materialização;
- pacote de validação;
- maturidade primária;
- entrada e saída conhecidas;
- continuidade integrada;
- caminhos alternativos;
- estados de erro, retorno ou exceção;
- dependências;
- lacunas conhecidas.

## 5. Regra de fonte única

O catálogo e os registros granulares apontam para o artefato canônico. SVGs, textos normativos e wireframes não são copiados para esta seção.

A presença no catálogo não promove maturidade, não valida uma transição e não fecha uma lacuna.

## 6. Estado vigente

A UXA-074 aprovou este catálogo com ressalva não bloqueadora. A UXA-075 promoveu o documento para `active` como inventário agregado por família.

A UXA-076 materializou a granularidade individual em registros separados. Esses registros permanecem `draft`; portanto, a granularidade está documentada, mas ainda não possui validação funcional própria.
