---
id: GPA-002
title: Guivos Mall
status: consolidated
version: 1.2.0
owner: Guivos
last_updated: 2026-08-12
former_name: Guivos Marketplace
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

## Limites

Guivos Mall não é o ambiente principal da jornada do participante, a operação especializada em viagens, a solução B2B, a unidade editorial, a camada de inteligência ou a plataforma de publicidade.

## Relações principais

- pode receber demanda originada no Guivos Journey;
- pode comercializar itens relacionados ao Guivos Travel, preservando a especialização do produto Travel;
- pode oferecer catálogos, benefícios e recompensas vinculados ao Guivos Business;
- utiliza Guivos Intelligence para personalização, curadoria e análise;
- pode receber campanhas do Guivos Ads, desde que identificadas e aderentes ao propósito.

## Home pública especializada

A apresentação pública especializada do produto é governada por `GKR-UX-HOME-MALL-MASTER-001` — **Home Pública — Guivos Mall — Documento Mestre**.

Essa Home preserva a identidade da Guivos antes de assumir naturalmente o comportamento comercial do Mall e mantém como pergunta-mãe:

> **O que pode fazer parte do seu próximo momento?**

A autoridade da Home trata exclusivamente da superfície pública do Mall. Página de produto, página de Perfil, Carrinho, Checkout e demais experiências internas permanecem fora daquele escopo.

A existência do Documento Mestre não autoriza automaticamente wireframe, protótipo, UI, frontend, backend ou implementação.

## Frentes públicas atuais do Mall

A Home especializada reconhece duas portas comerciais atuais:

### Shopping

É a frente de marketplace/shopping do Mall, capaz de reunir produtos de diferentes categorias, incluindo tecnologia, celulares, eletrônicos, eletrodomésticos, móveis, cama, mesa e banho, automóveis e demais itens efetivamente disponíveis.

### Gift Cards

É a frente dedicada a vouchers, serviços, experiências e presentes, incluindo Gift Cards de terceiros efetivamente disponíveis e o **Gift Card Guivos**.

Shopping e Gift Cards representam as duas portas atuais do produto e não constituem limite arquitetural definitivo para futuras capacidades do Mall.

## Preço e utilização de pontos

O Mall trabalha com preço monetário e, nas ofertas elegíveis, com preço em pontos.

A oferta deve mostrar somente as formas de aquisição realmente disponíveis para aquele item. Um produto pode, por exemplo, apresentar:

```text
R$ 1.899,00
ou
18.990 pts
```

A presença dessa representação não cria, por si só, pagamento híbrido `dinheiro + pontos`, taxa de conversão, regra de expiração, transferência ou qualquer outra mecânica econômica que dependa de autoridade própria.

O saldo total de pontos da pessoa pertence à informação global de conta/perfil e não deve ser repetido nos cards ou no corpo da Home quando já estiver visível junto ao perfil no Header.

```text
PERFIL
→ quanto a pessoa possui

PRODUTO / OFERTA
→ quanto custa em dinheiro
→ quanto custa em pontos, quando elegível
```

## Relação com o Programa de Pontos do Guivos Business

A utilização de pontos no Mall está relacionada ao Programa de Pontos do Guivos Business.

O fluxo comercial de referência é:

```text
EMPRESA
↓
GUIVOS BUSINESS
↓
PROGRAMA DE PONTOS
↓
PESSOA RECEBE O BENEFÍCIO
↓
pode utilizar em ofertas elegíveis do
MALL / TRAVEL
↓
A PESSOA ESCOLHE COMO UTILIZAR
```

Neste fluxo específico utiliza-se **Empresa** para designar a empresa cliente do Guivos Business e evitar confusão com a ontologia ampla de Organização e Coletivo da Guivos. Essa escolha não substitui `Organização` como tipo estrutural de participante.

Pontos possuem função transacional e de benefício. Eles não representam nível de evolução da pessoa.

```text
mais pontos
≠
mais evolução
```

O Programa de Pontos também permanece semanticamente separado do Gift Card Guivos.

```text
Programa de Pontos
≠
Gift Card Guivos
```

## Transparência comercial da Home

Na superfície pública do Mall, as seguintes classificações devem permanecer distintas:

```text
Em destaque
→ curadoria ou destaque geral

Recomendado para você
→ personalização ou relevância contextual

Oferta
→ condição comercial

Patrocinado
→ exposição decorrente de relação comercial
```

Patrocínio não deve ser apresentado como recomendação orgânica, e publicidade deve permanecer identificada.

## Gift Card Guivos

O Gift Card Guivos ocupa um papel próprio dentro da frente de Gift Cards.

Sua direção conceitual na Home é:

> **Presenteie com possibilidades.**

> **Você escolhe presentear. Quem recebe continua livre para escolher.**

Ele pertence ao território de presente, possibilidade, autonomia e escolha e não deve ser confundido com pontos, recompensa de evolução ou gamificação.

As regras econômicas e operacionais específicas do Gift Card não são definidas por este documento de arquitetura do produto quando dependerem de autoridade própria.

## Decisão de nomenclatura

`Guivos Mall` substitui `Guivos Marketplace` como nome oficial do produto.

A mudança preserva a responsabilidade arquitetural já consolidada e define uma marca comercial mais clara para o shopping de produtos e serviços de múltiplos fornecedores da Guivos.