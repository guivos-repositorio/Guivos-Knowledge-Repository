---
id: GKR-UX-HOME-PERSON-GENINPUT-001
title: Source Lock Operacional — Home Pública — Pessoa — Primeira Exploração de Design
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-13
parent: GKR-UX-HOMES-GENINPUT-001
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001
normative: true
---

# Source Lock Operacional — Home Pública — Pessoa

## 1. Finalidade

Esta é a instância operacional de `GKR-UX-HOMES-GENINPUT-001` para iniciar a **primeira exploração de Design da Home Pública principal da Guivos, com perspectiva predominante da Pessoa**.

Ela não cria nova arquitetura. Seu papel é congelar as fontes vigentes, explicitar o que precisa ser preservado e fornecer um prompt controlado para Figma Make ou ferramenta generativa equivalente.

A saída desta execução nasce com estado:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

## 2. Source Lock

### Home

`Home Pública — Pessoa`

### Fase autorizada nesta instância

`arquitetura visual + wireframe low-fi responsivo`

### Objetivo

Produzir uma primeira materialização estrutural da Home em desktop e mobile, suficiente para validar:

- hierarquia;
- progressão narrativa;
- ritmo;
- agrupamento dos movimentos;
- relação entre texto, imagem, conteúdo e ação;
- comportamento do Header e navegação em nível conceitual;
- preservação da percepção institucional da Guivos.

Não é objetivo desta execução fechar direção visual, UI final, design system, copy final ou implementação.

### Checkpoint do GKR

`main @ 6a4e2b2ea73c90726c3292867fdb71a91e0689db`

Qualquer execução posterior em outro checkpoint deve gerar novo Source Lock ou registrar explicitamente a reconciliação das diferenças.

## 3. Fontes autorizadas

### Fonte de processo

- ID: `GKR-UX-HOMES-DESIGN-HANDOFF-001`
- versão: `1.0.0`
- path: `docs/experience-architecture/public-homes-design-handoff.md`

### Fonte arquitetural principal

- ID: `GKR-UX-HOME-MASTER-001`
- versão: `0.1.0`
- path: `docs/experience-architecture/public-home-master-document.md`

### Fonte complementar vigente

- ID: `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001`
- versão: `1.0.0`
- path: `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md`

### Regra de entrada

Para esta primeira execução, **não adicionar automaticamente** documentos históricos, benchmarks, antigos wireframes, prompts, auditorias ou outras Homes.

Se uma dúvida concreta exigir aprofundamento, a nova fonte deve ser declarada antes de entrar no contexto da ferramenta.

## 4. Invariantes da Home

A ferramenta deve preservar:

1. a Guivos como ecossistema maior do que a soma dos produtos;
2. percepção de futuro, possibilidade, simplicidade, confiança e escala ampla/global;
3. tecnologia sem frieza e sofisticação sem complexidade;
4. perspectiva predominante da Pessoa;
5. possibilidade antes de produto;
6. autonomia antes de dependência;
7. a pergunta-mãe e a função narrativa registradas no Documento Mestre;
8. os onze movimentos como progressão sem obrigar onze blocos visuais equivalentes;
9. produtos aparecendo como manifestações/capacidades da Guivos, não como catálogo inicial de sete cards equivalentes;
10. evidência real, conteúdo editorial, conteúdo institucional e ação mantendo naturezas distinguíveis;
11. Media podendo abastecer editorialmente a Home sem adquirir autoridade sobre sua narrativa institucional;
12. ausência de promessa causal de transformação garantida;
13. acessibilidade, responsividade e performance como requisitos da solução, não correções posteriores.

## 5. Liberdades de Design

A ferramenta e Design podem explorar:

- grid;
- composição;
- número de dobras;
- agrupamento visual dos movimentos;
- escala e hierarquia;
- densidade;
- ritmo;
- uso de espaço vazio;
- tipografia provisória;
- direção de imagem e vídeo;
- fundos e atmosfera;
- componentes;
- modo de materializar Header e navegação;
- microinterações conceituais;
- desktop e mobile com soluções próprias;
- assimetria e variação de escala quando fortalecerem significado.

`Mesma família Guivos` não significa reproduzir a composição das Homes Mall, Travel ou Media.

## 6. Proibições de inferência

A ferramenta não pode inventar ou assumir como vigente:

- novos produtos ou serviços;
- funcionalidades não governadas;
- números de usuários;
- métricas de impacto;
- parceiros;
- depoimentos;
- cases;
- avaliações;
- campanhas;
- disponibilidade comercial;
- preços;
- rankings;
- promessas de transformação;
- taxonomias novas;
- uma comunidade Guivos como requisito da Home;
- gamificação como protagonista da Home;
- conteúdo fictício apresentado como evidência real.

Não transformar a Home em:

- landing page SaaS;
- catálogo de serviços;
- dashboard;
- portal de produtos;
- feed social;
- manifesto institucional excessivamente textual.

## 7. Conteúdo e placeholders

Placeholder é permitido somente para testar arquitetura.

Quando um conteúdo real não estiver disponível, usar rótulos explícitos como:

- `[HISTÓRIA REAL — A DEFINIR]`;
- `[IMAGEM DOCUMENTAL — A DEFINIR]`;
- `[CONTEÚDO EDITORIAL — A DEFINIR]`;
- `[PROVA VERIFICÁVEL — A DEFINIR]`.

Nunca fabricar nome, número, pessoa, parceiro, organização ou resultado para tornar o wireframe mais convincente.

## 8. Pacote entregue à ferramenta

Para esta execução, fornecer:

1. este Source Lock;
2. `GKR-UX-HOMES-DESIGN-HANDOFF-001`;
3. `GKR-UX-HOME-MASTER-001`;
4. `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001`.

`GKR-UX-HOMES-GENINPUT-001` governa a criação desta instância e permanece como referência operacional do GKR; não precisa ser duplicado no contexto da ferramenta se este Source Lock for entregue integralmente.

## 9. Prompt controlado — primeira exploração

Copiar o bloco abaixo para a ferramenta depois de anexar as fontes autorizadas.

```text
Você está trabalhando na primeira exploração de Design da Home Pública principal da Guivos, com perspectiva predominante da Pessoa.

OBJETIVO
Crie uma proposta de arquitetura visual e wireframe low-fi responsivo para desktop e mobile. A saída deve permitir avaliar hierarquia, progressão narrativa, ritmo, agrupamento dos movimentos e caminhos de ação. Não trate a saída como UI final nem como implementação pronta.

FONTES AUTORIZADAS
Use exclusivamente os documentos anexados e este Source Lock como fonte de decisões sobre a Guivos e esta Home. Se alguma informação necessária não estiver definida, sinalize a lacuna ou use hipótese explicitamente rotulada. Não transforme hipótese em requisito.

INVARIANTES
- a Guivos deve parecer maior do que a soma de seus produtos;
- futuro, possibilidade, simplicidade, confiança e escala ampla/global devem orientar a percepção;
- a Pessoa é a perspectiva predominante;
- possibilidade vem antes de produto;
- preserve a pergunta-mãe e a função dos onze movimentos;
- onze movimentos não significam onze seções visuais equivalentes;
- não abra a experiência com catálogo de produtos ou serviços;
- preserve autonomia e evite promessas de transformação garantida;
- conteúdo do Guivos Media pode fornecer evidência e matéria editorial, mas a Home mantém autoridade institucional;
- mantenha conteúdo institucional, evidência real, editorial e ação semanticamente distinguíveis;
- mobile deve preservar hierarquia, não apenas empilhar o desktop.

LIBERDADE DE DESIGN
Você pode propor grid, composição, dobras, agrupamentos, escala, ritmo, tipografia provisória, direção de imagem, fundos, componentes, Header, navegação, microinterações conceituais e comportamento responsivo.

NÃO INVENTE
Produtos, features, dados, métricas, parceiros, depoimentos, cases, campanhas, preços, avaliações, disponibilidade, provas sociais ou histórias reais. Use placeholders explicitamente rotulados quando necessário.

ANTI-TEMPLATE
Não transforme a Guivos em landing page SaaS, dashboard ou catálogo. Evite hero genérico + três benefícios + grade de cards + CTA final como solução automática. Busque uma experiência própria, narrativa, ampla e contemporânea.

ENTREGUE
1. mapa resumido da página;
2. wireframe low-fi desktop;
3. wireframe low-fi mobile;
4. explicação breve de como os onze movimentos foram agrupados visualmente;
5. lista de hipóteses introduzidas;
6. lista de lacunas encontradas;
7. autoauditoria dos invariantes acima.

STATUS DA SAÍDA
EXPLORAÇÃO. Nada produzido nesta execução se torna canônico, aprovado ou requisito sem validação humana posterior contra o GKR.
```

## 10. Autoauditoria obrigatória

Antes de selecionar a direção como `CANDIDATO`, verificar:

- a primeira leitura fala de possibilidade antes de produtos?;
- a Guivos parece ecossistema, não catálogo?;
- os produtos não dominaram a narrativa?;
- os onze movimentos continuam reconhecíveis em função, mesmo agrupados?;
- existe hierarquia real ou apenas blocos equivalentes?;
- conteúdo fictício está marcado?;
- o Media foi usado como fonte editorial, não como dono da Home?;
- mobile possui decisão própria?;
- a solução evita clichê SaaS?;
- acessibilidade e performance continuam plausíveis?;
- hipóteses estão separadas de requisitos?;
- nenhuma decisão nova de produto foi criada pela ferramenta?

## 11. Saída esperada desta rodada

A rodada pode encerrar com:

```text
EXPLORAÇÃO
→ uma ou mais direções geradas

CANDIDATO
→ direção selecionada para revisão humana de UX
```

Ela não pode encerrar diretamente como `VALIDADO EM UI` ou `APROVADO PARA HANDOFF DE ENGENHARIA`.

## 12. Próxima etapa

Depois da seleção de um candidato, a equipe deve registrar:

- o que foi aceito;
- o que foi rejeitado;
- hipóteses resolvidas;
- decisões novas que exigem governança;
- se o checkpoint das fontes continua vigente.

Somente então deve ser criado o Source Lock da etapa de UX detalhada ou direção visual/UI.

## 13. Síntese

> **Na Home Pública da Pessoa, a ferramenta pode explorar como tornar possibilidade visível; não pode redefinir o que a Guivos significa nem transformar seus produtos no ponto de partida da experiência.**
