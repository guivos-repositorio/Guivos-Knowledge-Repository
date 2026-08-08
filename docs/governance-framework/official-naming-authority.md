---
id: GKR-OFFICIAL-NAMING-AUTHORITY-001
title: Autoridade Oficial de Naming da Guivos
status: proposed
version: 1.0.0
owner: Guivos
last_updated: 2026-08-08
depends_on:
  - GPA-000
related:
  - GPA-001
  - GPA-002
  - GPA-003
  - GPA-004
  - GPA-005
  - GPA-006
  - GPA-007
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-BRAND-ASSET-GOVERNANCE-001
normative: true
---

# Autoridade Oficial de Naming da Guivos

## 1. Finalidade

Este documento registra os nomes canônicos que podem ser utilizados como nomenclatura vigente no Guivos Knowledge Repository para os objetos expressamente cobertos.

A autoridade é **semântica e documental**. Ela não constitui prova de registro de marca, disponibilidade registral, domínio adquirido, empresa constituída, lançamento público ou operação comercial.

## 2. Marca institucional

| Objeto | Nome canônico no GKR | Estado de naming | Observação |
|---|---|---|---|
| ecossistema/identidade institucional | **Guivos** | `canonical` | nome institucional usado pelo corpus; proteção jurídica deve ser comprovada separadamente |
| repositório oficial de conhecimento | **Guivos Knowledge Repository** | `canonical` | nome do repositório e sistema documental |

Esta tabela afirma nomenclatura, não titularidade jurídica.

## 3. Produtos Especializados

A arquitetura de produtos reconhece sete Produtos Especializados com os seguintes nomes canônicos:

| ID | Nome canônico | Camada predominante | Alias legado permitido | Estado |
|---|---|---|---|---|
| GPA-001 | **Guivos Journey** | Experience | — | `canonical` |
| GPA-002 | **Guivos Mall** | Service | `Guivos Marketplace` somente em histórico/migração | `canonical` |
| GPA-003 | **Guivos Travel** | Service | — | `canonical` |
| GPA-004 | **Guivos Business** | Service | — | `canonical` |
| GPA-005 | **Guivos Media** | Service | — | `canonical` |
| GPA-006 | **Guivos Intelligence** | Intelligence | — | `canonical` |
| GPA-007 | **Guivos Ads** | Service | — | `canonical` |

A lista de produtos não deve ser expandida a partir de uma conversa, domínio, iniciativa experimental, página, campanha ou funcionalidade sem autoridade arquitetural correspondente.

## 4. Migração Guivos Marketplace → Guivos Mall

`GPA-002` estabelece:

```text
nome oficial vigente = Guivos Mall
former_name = Guivos Marketplace
```

Consequentemente, `Guivos Marketplace` é `superseded` para uso corrente.

O alias pode permanecer somente em:

- histórico;
- registro de migração;
- campos `former_name`;
- explicação explícita da substituição;
- evidência externa reproduzida com contexto.

Não deve ser usado como nome atual do produto em navegação, arquitetura vigente, comunicação institucional atual, tabelas, diagramas ou novas decisões.

## 5. Papéis estruturais não são produtos

Os papéis estruturais permanecem:

- Pessoa;
- Coletivo;
- Organização.

Eles não devem receber prefixo de produto por conveniência sem autoridade própria.

Em especial:

```text
Organização ≠ Guivos Business
Coletivo ≠ Guivos Journey
Pessoa ≠ Guivos Journey
```

Um produto pode apoiar ou hospedar uma experiência de participante sem transformar o participante no produto.

## 6. Planos

A nomenclatura vigente de planos é governada por `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`:

| Contexto | Naming vigente |
|---|---|
| Pessoa | **Free · Plus · Pro** |
| Coletivo | **Livre · Mobiliza · Impacta · Rede** |
| Organização | **Conecta · Eleva · Transforma** |
| Guivos Business | **Start · Growth · Scale · Enterprise** |

Esta autoridade de naming não redefine preço, entitlement, capacidade ou condição comercial.

## 7. Relações que não criam naming de produto

Os seguintes conceitos não são automaticamente Produtos Especializados ou marcas autônomas:

- oportunidade;
- Parceria Estratégica;
- Coletivo;
- Organização;
- campanha;
- programa;
- benefício;
- grafo;
- GraphRAG;
- Neo4j;
- Power BI;
- camada de plataforma;
- mecanismo de pagamento;
- tecnologia de infraestrutura.

A criação de uma marca, subproduto ou nome público para qualquer um desses objetos exige ato específico.

## 8. Domínios não definem autoridade de nome

A existência ou intenção de uso de um domínio não cria, por si só, nome canônico.

```text
hostname disponível/adquirido
≠ nome de produto aprovado
```

Da mesma forma:

```text
nome canônico
≠ hostname obrigatoriamente adquirido
```

O relacionamento entre marca e ativo digital deve ser registrado pelo modelo `GKR-DIGITAL-ASSET-CONTROL-001` quando houver evidência apropriada.

## 9. Padrões para novos nomes

Toda proposta de nome novo deve responder, antes de canonicalização:

1. **o que está sendo nomeado?** produto, capacidade, programa, entidade, campanha, serviço ou propriedade editorial;
2. **por que precisa de nome próprio?**;
3. **qual responsabilidade ele diferencia?**;
4. **há colisão semântica com participante, produto, plano ou camada existente?**;
5. **há nome anterior?**;
6. **há dependências de marca/domínio?**;
7. **o nome é globalmente compreensível no contexto pretendido?**;
8. **o jurídico precisa validar registrabilidade/risco?**;
9. **quais documentos e superfícies serão consumidores?**;
10. **qual estado inicial: candidate, approved_internal ou canonical?**

## 10. Critérios de nomenclatura

Como regra, nomes devem buscar:

- clareza de responsabilidade;
- memorabilidade compatível com a marca-mãe;
- baixa ambiguidade com papéis estruturais;
- possibilidade de tradução/uso internacional sem alterar essência;
- não prometer resultado, mérito ou impacto que o produto não possa comprovar;
- não induzir autoridade técnica, jurídica ou econômica inexistente;
- consistência entre arquitetura, produto, comunicação e operação.

## 11. Precedência

Quando um derivado atual conflitar com esta matriz ou com uma autoridade temática mais específica:

1. a autoridade temática vigente prevalece;
2. o derivado deve ser sincronizado;
3. a referência antiga pode permanecer somente como histórico inequívoco;
4. nenhuma correção deve transformar alias antigo em nova decisão econômica, técnica ou jurídica.

## 12. Naming não comprova proteção jurídica

Os estados `canonical` desta autoridade significam apenas:

> **este é o nome que o GKR deve usar atualmente para o objeto identificado.**

Eles não significam:

- marca depositada;
- marca concedida;
- classe definida;
- cobertura internacional;
- domínio adquirido;
- username reservado;
- ausência de oposição ou conflito;
- autorização jurídica para lançamento em qualquer território.

Essas afirmações exigem evidência própria.

## 13. Critério de atualização

Este documento deve ser atualizado quando:

- um nome canônico mudar;
- um produto for criado, fundido, renomeado ou aposentado por autoridade competente;
- um alias legado precisar ser formalizado;
- uma colisão entre naming de participante, produto, plano ou iniciativa for identificada;
- uma autoridade superior alterar a arquitetura de produtos.

A mudança deve ser propagada aos consumidores e aos gates de nomenclatura quando apropriado.
