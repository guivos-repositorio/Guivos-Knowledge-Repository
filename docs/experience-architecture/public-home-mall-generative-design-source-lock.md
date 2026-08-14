---
id: GKR-UX-HOME-MALL-GENINPUT-001
title: Source Lock Operacional — Home Pública — Guivos Mall — Primeira Exploração de Design
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-13
parent: GKR-UX-HOMES-GENINPUT-001
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-MALL-MEDIA-SUPPLY-001
normative: true
---

# Source Lock Operacional — Home Pública — Guivos Mall

## 1. Finalidade

Esta instância prepara a primeira exploração de Design da **Home Pública do Guivos Mall**. Ela congela as fontes vigentes para arquitetura visual e wireframe low-fi responsivo sem alterar a arquitetura comercial, narrativa ou de confiança do produto.

Estado inicial:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

## 2. Source Lock

- Home: `Guivos Mall`.
- Fase: `arquitetura visual + wireframe low-fi responsivo`.
- Checkpoint: `main @ 6a4e2b2ea73c90726c3292867fdb71a91e0689db`.
- Objetivo: validar a relação entre descoberta, comércio, confiança, busca direta, conteúdo editorial e ação comercial em desktop e mobile.

## 3. Fontes autorizadas

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.0.0 — `docs/experience-architecture/public-homes-design-handoff.md`;
2. `GKR-UX-HOME-MALL-MASTER-001` v1.0.0 — `docs/experience-architecture/public-home-mall-master-document.md`;
3. `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001` v1.0.0 — `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md`.

Não adicionar automaticamente outras Homes, benchmarks de e-commerce, telas internas, catálogo real, campanhas ou materiais históricos.

## 4. Invariantes

Preservar:

1. a pergunta-mãe **“O que pode fazer parte do seu próximo momento?”**;
2. o Mall como capacidade da Guivos, não uma loja desconectada do ecossistema;
3. `descoberta + comércio + confiança` como equilíbrio estrutural;
4. comércio essencial, mas não como primeira e única percepção;
5. descoberta para quem quer explorar e busca/acesso direto para quem já sabe o que procura;
6. as portas `Shopping | Gift Cards` conforme governadas;
7. os onze movimentos como progressão, não como onze prateleiras equivalentes;
8. produto, preço, vendedor, disponibilidade, condição comercial, pontos e compra sob autoridade do Mall;
9. conteúdo editorial sob autoridade do Media quando originado nele;
10. publicidade e exposição paga sob autoridade do Ads;
11. conteúdo editorial, recomendação, oferta e publicidade permanecendo distinguíveis;
12. conteúdo podendo criar contexto, mas nunca mascarar intenção de venda;
13. preço, desconto, disponibilidade, avaliação, estoque e condição comercial nunca sendo inventados;
14. compra permanecendo simples e familiar mesmo quando há contexto editorial.

## 5. Liberdades de Design

Podem ser explorados:

- grid e composição;
- hierarquia entre descoberta e acesso direto;
- Header, busca e navegação;
- tratamento das portas Shopping e Gift Cards;
- agrupamento dos movimentos;
- escalas de produto e conteúdo;
- tipografia provisória;
- direção de imagem;
- tratamento de criadores, marcas, categorias e universos;
- componentes comerciais provisórios;
- ritmo entre editorial e oferta;
- desktop e mobile com soluções próprias.

A ferramenta pode propor forma comercial sem transformar a Home em catálogo genérico.

## 6. Proibições de inferência

Não inventar:

- produtos disponíveis;
- vendedores;
- marcas parceiras;
- estoque;
- preço;
- desconto;
- cashback;
- pontuação;
- prazo;
- frete;
- avaliações;
- número de compras;
- selos;
- campanhas;
- benefícios;
- Gift Cards vigentes;
- recomendações personalizadas como se já existissem;
- conteúdo patrocinado disfarçado de recomendação orgânica.

Não usar storytelling para substituir informação comercial objetiva.

## 7. Placeholders

Utilizar, quando necessário:

- `[PRODUTO — PLACEHOLDER]`;
- `[PREÇO — NÃO DEFINIDO]`;
- `[OFERTA — NÃO VIGENTE / EXEMPLO]`;
- `[CONTEÚDO EDITORIAL — A DEFINIR]`;
- `[CRIADOR / MARCA — A DEFINIR]`;
- `[GIFT CARD — PLACEHOLDER]`.

Nenhum placeholder deve parecer inventário real.

## 8. Pacote entregue à ferramenta

Fornecer:

1. este Source Lock;
2. Handoff Canônico;
3. Documento Mestre do Mall;
4. Reconciliação pós-Media do Mall.

## 9. Prompt controlado

```text
Você está trabalhando na primeira exploração de Design da Home Pública do Guivos Mall.

OBJETIVO
Crie uma arquitetura visual e wireframe low-fi responsivo para desktop e mobile que permita validar descoberta, comércio, confiança, busca direta e integração contextual de conteúdo editorial. Não trate a saída como UI final nem como loja pronta para produção.

FONTES
Use somente os documentos anexados e este Source Lock para decisões sobre a Guivos e o Mall. Lacunas devem ser sinalizadas; hipóteses devem ser rotuladas.

INVARIANTES
- preserve “O que pode fazer parte do seu próximo momento?”;
- o Mall é uma capacidade da Guivos, não uma loja independente;
- equilibre descoberta + comércio + confiança;
- não abra a experiência apenas com catálogo, preço ou promoção;
- preserve Shopping | Gift Cards conforme os documentos;
- permita acesso direto para quem já sabe o que procura;
- preserve a função dos onze movimentos sem convertê-los em onze prateleiras equivalentes;
- conteúdo editorial pode contextualizar uma possibilidade comercial, mas não pode mascarar venda;
- editorial, recomendação, oferta e publicidade devem continuar distinguíveis;
- Mall governa preço, disponibilidade, vendedor, condição e compra;
- Ads governa exposição paga;
- Media governa integridade editorial do conteúdo que produz;
- mobile deve preservar hierarquia, busca e ação comercial de modo próprio.

LIBERDADE
Explore grid, composição, Header, busca, portas Shopping/Gift Cards, ritmo, escala, tipografia provisória, direção de imagem, componentes e relação entre conteúdo e oferta.

NÃO INVENTE
Produtos, marcas parceiras, vendedores, estoque, preços, descontos, avaliações, frete, pontos, benefícios, campanhas, Gift Cards vigentes ou recomendações personalizadas reais. Use placeholders rotulados.

ANTI-TEMPLATE
Evite transformar a Home em marketplace genérico, grade infinita de cards, página dominada por promoções ou cópia de grandes e-commerces. A experiência precisa continuar pertencendo à família Guivos.

ENTREGUE
1. mapa resumido da página;
2. wireframe low-fi desktop;
3. wireframe low-fi mobile;
4. explicação da hierarquia descoberta × comércio × confiança;
5. explicação de como editorial, recomendação, oferta e publicidade permanecem distinguíveis;
6. hipóteses introduzidas;
7. lacunas encontradas;
8. autoauditoria dos invariantes.

STATUS
EXPLORAÇÃO. Nada produzido se torna canônico ou comercialmente verdadeiro sem validação humana e dados reais.
```

## 10. Autoauditoria

Antes de promover uma direção a `CANDIDATO`, confirmar:

- a primeira percepção é maior do que “loja”?;
- a pessoa pode descobrir e também acessar diretamente o que procura?;
- Shopping e Gift Cards permanecem compreensíveis?;
- a hierarquia não foi reduzida a grade de produtos?;
- os onze movimentos continuam funcionais?;
- conteúdo editorial está separado de oferta e publicidade?;
- nenhuma exposição paga parece orgânica?;
- nenhum preço, desconto, estoque, avaliação ou produto foi fabricado?;
- compra continua simples?;
- mobile preserva busca, hierarquia e ação?;
- acessibilidade e performance são plausíveis?;
- hipóteses estão rotuladas?

## 11. Próxima etapa

Após seleção humana de um candidato, registrar decisões e lacunas antes de direção visual/UI. Qualquer uso de inventário, preço ou campanha real exige fonte operacional específica adicionada a um novo Source Lock.

## 12. Síntese

> **A ferramenta pode explorar como descoberta e comércio convivem; não pode inventar mercado, oferta, confiança ou usar aparência editorial para disfarçar venda.**
