---
id: GKR-UX-HOME-TRAVEL-GENINPUT-001
title: Source Lock Operacional — Home Pública — Guivos Travel — Primeira Exploração de Design
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-13
parent: GKR-UX-HOMES-GENINPUT-001
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001
normative: true
---

# Source Lock Operacional — Home Pública — Guivos Travel

## 1. Finalidade

Esta instância prepara a primeira exploração de Design da **Home Pública do Guivos Travel**. Ela congela fontes e fronteiras para arquitetura visual e wireframe low-fi responsivo, preservando a convivência entre inspiração, operação real e acesso direto aos serviços.

Estado inicial:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

## 2. Source Lock

- Home: `Guivos Travel`.
- Fase: `arquitetura visual + wireframe low-fi responsivo`.
- Checkpoint: `main @ 6a4e2b2ea73c90726c3292867fdb71a91e0689db`.
- Objetivo: validar como desejo, descoberta de destinos/experiências e acesso operacional convivem sem transformar o Travel em agência genérica ou revista de viagem.

## 3. Fontes autorizadas

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.0.0 — `docs/experience-architecture/public-homes-design-handoff.md`;
2. `GKR-UX-HOME-TRAVEL-MASTER-001` v1.0.0 — `docs/experience-architecture/public-home-travel-master-document.md`;
3. `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001` v1.0.0 — `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md`.

Não incluir automaticamente telas de busca/reserva/checkout, inventário, tarifas, destinos operacionais, benchmarks de OTAs ou outras Homes.

## 4. Invariantes

Preservar:

1. a pergunta-mãe **“Até onde o seu próximo momento pode levar você?”**;
2. Travel como capacidade da Guivos, não empresa de turismo desconectada;
3. `inspiração + operação real + acesso direto aos serviços`;
4. inspiração para quem quer descobrir e acesso direto para quem já sabe o que precisa;
5. os serviços operacionais e suas regras conforme governados, sem inventar disponibilidade;
6. os onze movimentos como progressão narrativa, não onze ofertas equivalentes;
7. descoberta de lugares e experiências sem esconder a realidade operacional;
8. Media podendo fornecer histórias, pessoas, lugares, cultura e contexto;
9. Media não podendo afirmar disponibilidade, preço, serviço ou contratação;
10. Travel mantendo autoridade sobre operação, disponibilidade, preço, elegibilidade e oferta;
11. conteúdo editorial e oferta comercial permanecendo distinguíveis;
12. nenhuma imagem ou história devendo induzir que um destino, hotel, voo ou experiência esteja disponível quando isso não estiver confirmado;
13. mobile precisando funcionar para inspiração e acesso direto, não apenas reproduzir desktop verticalmente.

## 5. Liberdades de Design

Podem ser explorados:

- Hero e atmosfera de descoberta;
- grid e composição;
- relação entre destino, experiência e serviço;
- Header, navegação e acesso direto;
- agrupamento dos movimentos;
- módulos editoriais e operacionais;
- direção de fotografia e vídeo;
- mapas conceituais quando úteis à narrativa, sem inventar disponibilidade;
- tipografia provisória;
- CTAs;
- componentes de serviço em baixa fidelidade;
- soluções distintas para desktop e mobile.

## 6. Proibições de inferência

Não inventar:

- destinos disponíveis;
- hotéis;
- voos;
- empresas de ônibus;
- pacotes;
- experiências contratáveis;
- preços;
- datas;
- disponibilidade;
- promoções;
- avaliações;
- parceiros;
- pontos;
- condições de cancelamento;
- políticas;
- rotas;
- tempo de viagem;
- inventário operacional.

Não transformar conteúdo editorial em promessa de disponibilidade.

## 7. Placeholders

Usar rótulos claros:

- `[DESTINO EDITORIAL — EXEMPLO]`;
- `[SERVIÇO — PLACEHOLDER]`;
- `[PREÇO — NÃO DEFINIDO]`;
- `[DISPONIBILIDADE — NÃO CONFIRMADA]`;
- `[EXPERIÊNCIA — EXEMPLO NÃO OPERACIONAL]`;
- `[CONTEÚDO MEDIA — A DEFINIR]`.

## 8. Pacote entregue à ferramenta

Fornecer:

1. este Source Lock;
2. Handoff Canônico;
3. Documento Mestre do Travel;
4. Reconciliação pós-Media do Travel.

## 9. Prompt controlado

```text
Você está trabalhando na primeira exploração de Design da Home Pública do Guivos Travel.

OBJETIVO
Crie uma arquitetura visual e wireframe low-fi responsivo para desktop e mobile que permita validar inspiração, descoberta, operação real e acesso direto aos serviços. Não produza UI final nem telas internas de reserva/checkout.

FONTES
Use somente os documentos anexados e este Source Lock como fonte de decisão. Se faltar informação, sinalize a lacuna ou use hipótese explicitamente rotulada.

INVARIANTES
- preserve “Até onde o seu próximo momento pode levar você?”;
- Travel é uma capacidade da Guivos, não uma agência separada;
- equilibre inspiração + operação real + acesso direto aos serviços;
- permita descoberta para quem ainda não sabe para onde ir e acesso direto para quem já sabe o que precisa;
- preserve a função dos onze movimentos sem gerar onze ofertas equivalentes;
- conteúdo do Media pode explicar pessoas, lugares, cultura e experiências;
- somente Travel pode afirmar disponibilidade, preço, serviço, elegibilidade e contratação;
- editorial e oferta comercial devem permanecer distinguíveis;
- não sugira disponibilidade por causa de uma imagem ou história;
- mobile deve preservar tanto inspiração quanto acesso direto.

LIBERDADE
Explore grid, Hero, composição, ritmo, mídia, destinos como matéria narrativa, componentes operacionais low-fi, Header, navegação, CTAs e responsividade.

NÃO INVENTE
Destinos disponíveis, hotéis, voos, ônibus, pacotes, experiências contratáveis, preços, datas, promoções, avaliações, parceiros ou inventário. Use placeholders rotulados.

ANTI-TEMPLATE
Evite tanto a landing page de agência genérica quanto o portal puramente editorial de viagens. A experiência deve mostrar desejo e possibilidade sem esconder que existe operação real.

ENTREGUE
1. mapa resumido da página;
2. wireframe low-fi desktop;
3. wireframe low-fi mobile;
4. explicação do equilíbrio inspiração × operação × acesso direto;
5. indicação clara de onde conteúdo Media pode abastecer a narrativa;
6. hipóteses introduzidas;
7. lacunas encontradas;
8. autoauditoria dos invariantes.

STATUS
EXPLORAÇÃO. Nenhum destino, serviço ou oferta representado pode ser entendido como disponibilidade real sem validação operacional posterior.
```

## 10. Autoauditoria

Antes de promover uma direção a `CANDIDATO`, confirmar:

- a primeira percepção combina possibilidade de viajar e pertencimento à Guivos?;
- quem quer descobrir encontra inspiração?;
- quem já sabe o que precisa encontra caminho direto?;
- a operação não foi escondida pelo editorial?;
- o editorial não foi confundido com disponibilidade?;
- os onze movimentos continuam funcionais?;
- nenhum preço, destino, parceiro ou serviço foi fabricado?;
- a solução evita estereótipo de agência e de revista?;
- mobile preserva descoberta e ação?;
- acessibilidade e performance permanecem plausíveis?;
- hipóteses estão rotuladas?

## 11. Próxima etapa

Após seleção humana de um candidato, registrar decisões e lacunas antes de direção visual/UI. Dados operacionais reais só podem entrar por fonte específica declarada em novo Source Lock.

## 12. Síntese

> **A ferramenta pode explorar como uma viagem se torna desejável e acessível; não pode transformar inspiração em disponibilidade nem inventar a operação que somente o Travel pode afirmar.**
