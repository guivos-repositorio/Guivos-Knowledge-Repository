---
id: GPA-002
title: Guivos Mall
status: consolidated
version: 1.2.0
owner: Guivos
last_updated: 2026-08-08
former_name: Guivos Marketplace
related:
  - GLPA-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
---

# Guivos Mall

## Papel

Guivos Mall é o produto responsável pela oferta e comercialização de produtos, serviços, gift cards, assinaturas e outros ativos digitais ou físicos do Ecossistema Guivos.

Seu papel é funcionar como o shopping do ecossistema, reunindo ofertas de diferentes fornecedores com curadoria e aderência às jornadas apoiadas pela Guivos.

## Escopo principal

- catálogo comercial curado;
- produtos físicos e digitais;
- gift cards;
- assinaturas;
- serviços comercializáveis;
- pedidos;
- ofertas e promoções;
- relacionamento transacional com compradores e vendedores;
- integração com jornadas, experiências, benefícios e parceiros do ecossistema.

## Princípio de aderência

Guivos Mall não deve funcionar como um catálogo genérico de ofertas.

A simples existência de um produto, serviço ou promoção não justifica sua presença no ecossistema. Cada oferta deve possuir relação demonstrável com jornadas, experiências, necessidades, benefícios ou objetivos legítimos de pessoas e organizações.

## Integração com a experiência

A GLPA prevê que o Journey possa originar demanda para Mall, mas o registro atual de superfícies e transições ainda não possui uma família canônica dedicada ao produto.

Portanto, nesta edição:

- recomendação ou menção de produto dentro do Journey não significa entrada no Mall;
- não existe ainda `SURF` ou `TRN` canônico de Journey → Mall;
- uma futura entrada no contexto transacional do Mall deverá ser tratada como handoff interno da Guivos;
- esse handoff deverá definir trigger, identidade, contexto, dados, autoridade, consequência, retorno e recuperação antes de ser promovido;
- `BND-001` não deve ser usado quando a autoridade permanece dentro da Guivos.

A lacuna está registrada como `SP-GAP-001` na [Matriz de Integração dos Produtos com as Jornadas](specialized-products-journey-integration-matrix.md).

## Limites

Guivos Mall não é o ambiente principal da jornada do participante, a operação especializada em viagens, a solução B2B, a unidade editorial, a camada de inteligência ou a plataforma de publicidade.

Capacidades compartilhadas de billing/pagamento pertencem à Platform Layer; Mall preserva a semântica comercial de produto, pedido, compra, vendedor e demais relações de seu domínio.

## Relações principais

- pode receber demanda originada no Guivos Journey após handoff interno validado;
- pode comercializar itens relacionados ao Guivos Travel, preservando a especialização do produto Travel;
- pode oferecer catálogos e benefícios vinculados ao Guivos Business;
- utiliza Guivos Intelligence para personalização, curadoria e análise dentro dos limites autorizados;
- pode receber campanhas do Guivos Ads, desde que identificadas e aderentes ao propósito.

## Regra de representação

Mall deve tornar-se perceptível quando a experiência muda materialmente para compra, pedido, assinatura ou outra relação transacional sob sua autoridade.

A regra completa de visibilidade e handoff está em [Política de Representação e Handoffs entre Produtos](specialized-products-experience-and-handoff-policy.md).

## Estado de integração

A responsabilidade superior do Mall está consolidada. A integração com Journey está arquiteturalmente prevista, porém **a materialização canônica Journey → Mall permanece ausente**.

Nenhuma tela, transição, carrinho, checkout ou fluxo de compra é promovido por este rebaseline.

## Decisão de nomenclatura

`Guivos Mall` substitui `Guivos Marketplace` como nome oficial do produto.

A mudança preserva a responsabilidade arquitetural já consolidada e define uma marca comercial mais clara para o shopping de produtos e serviços de múltiplos fornecedores da Guivos.
