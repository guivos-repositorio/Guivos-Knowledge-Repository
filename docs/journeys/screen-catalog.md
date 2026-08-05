---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
  - UXA-005
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
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

## 2. Inventário reformulado por família

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

## 3. Campos obrigatórios por referência

Cada entrada futura do catálogo deverá registrar:

- ID da tela ou estado;
- nome compreensível;
- participante e perspectiva;
- jornada e posição;
- canal;
- caminho do SVG ou documento;
- autoridade contratual;
- pacote de materialização;
- pacote de validação;
- versão;
- maturidade primária;
- transição de entrada e sua evidência;
- transição de saída e sua evidência;
- caminhos alternativos;
- estados de erro, retorno ou exceção;
- autoridade da decisão;
- dependências;
- lacunas conhecidas.

## 4. Regra de fonte única

O catálogo aponta para o artefato canônico. SVGs, textos normativos e wireframes não são copiados para esta seção.

A presença no catálogo não promove maturidade, não valida uma transição e não fecha uma lacuna.

Esta vista permanece `draft` até nova validação funcional.
