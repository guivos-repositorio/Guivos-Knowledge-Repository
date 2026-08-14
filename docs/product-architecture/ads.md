---
id: GPA-007
title: Guivos Ads
status: consolidated
version: 1.3.0
owner: Guivos
last_updated: 2026-08-14
related:
  - GLPA-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GEM-007-ADS-ECONOMIC-ROLE-001
  - GEM-007-A1
  - UXA-038
  - GEM-010-A2
  - GPA-001
  - GPA-002
  - GPA-003
  - GPA-005
  - GPA-006
  - M7.40
---

# Guivos Ads

## Papel

Guivos Ads é o produto responsável pela publicidade, mídia patrocinada, patrocínios, impulsionamentos, ativações de marca e soluções comerciais para anunciantes dentro do Ecossistema Guivos.

Sua finalidade econômica predominante é **gerar receita publicitária e comercial para a Guivos**, preservando a finalidade, a autoridade e a experiência das superfícies nas quais a publicidade se manifesta.

Na classificação formal vigente de `GLPA-001`, Guivos Ads permanece na **Service Layer**. Funcionalmente, porém, possui uma postura comercial transversal: opera oportunidades publicitárias dentro de contextos criados por outras superfícies sem absorver a autoridade funcional dessas superfícies.

Tese operacional:

> **Os produtos Guivos criam contextos e experiências. Guivos Ads transforma oportunidades legítimas desses contextos em soluções comerciais para marcas e parceiros.**

## Escopo principal

Guivos Ads suporta progressivamente:

- campanhas publicitárias;
- mídia patrocinada;
- formatos nativos identificados;
- banners e display contextual;
- posições patrocinadas e destaques;
- ativações de marca;
- patrocínios;
- projetos comerciais especiais;
- impulsionamentos;
- segmentação permitida;
- mensuração de campanhas;
- soluções para anunciantes e parceiros;
- Opportunity Boost;
- qualificação comercial inteligente apoiada por Guivos Intelligence, dentro das autoridades aplicáveis.

A existência desses formatos e mecanismos não implica disponibilidade operacional imediata, inventário aberto, preço público ou contratação automática.

## Postura comercial transversal

Guivos Ads não deve ser interpretado como mais uma experiência orientada à jornada da pessoa.

Sua função predominante é comercializar e operar oportunidades publicitárias legítimas originadas em contextos criados por produtos e superfícies do ecossistema.

Relação de referência:

```text
PRODUTO OU SUPERFÍCIE GUIVOS
→ cria o contexto e governa a experiência

GUIVOS ADS
→ transforma oportunidade publicitária permitida em solução comercial

ANUNCIANTE
→ contrata exposição, patrocínio, impulsionamento ou ativação elegível
```

> **O contexto define onde uma marca faz sentido. Ads transforma essa oportunidade em uma solução comercial.**

Essa transversalidade não reclassifica por si só a camada formal estabelecida em `GLPA-001`.

## Modelo de soluções por objetivo

Guivos Ads organiza sua oferta conceitual prioritariamente pelo **objetivo comercial do anunciante**, e não pelo tamanho ou tipo técnico do formato.

### Ampliar presença

Maior visibilidade de marca em contextos compatíveis, por meio de banners, display, espaços especiais, presença contextual, destaques ou outros formatos autorizados.

### Destacar ofertas

Ampliação de visibilidade de marcas, fabricantes, produtos, lançamentos, promoções, hotéis, restaurantes, destinos, lugares, experiências, serviços ou outras ofertas legitimamente inseridas no contexto da superfície.

### Amplificar histórias

Patrocínios, projetos especiais, propriedades editoriais, conteúdo patrocinado identificado e outras relações comerciais compatíveis com Guivos Media.

Ads governa a relação comercial; Media preserva autoridade editorial.

### Impulsionar oportunidades

Distribuição patrocinada adicional de oportunidades, atividades, programas, iniciativas ou experiências elegíveis.

`Opportunity Boost` é o mecanismo candidato já definido para parte desse objetivo.

### Criar ativações

Campanhas especiais, experiências de marca, projetos cocriados, patrocínios especiais, iniciativas integradas e outros formatos comerciais futuros sujeitos às autoridades aplicáveis.

## Objetivo, solução e formato

A arquitetura deve preservar três níveis distintos:

```text
OBJETIVO
↓
SOLUÇÃO
↓
FORMATO
```

Exemplo:

```text
OBJETIVO
Destacar um lançamento

SOLUÇÃO
Presença patrocinada contextual no Mall

FORMATOS POSSÍVEIS
Banner + posição patrocinada + produto em destaque
```

Formato é consequência da solução comercial e não deve definir sozinho a arquitetura do produto.

## Inventário publicitário contextual

Guivos Ads pode operar inventário publicitário em superfícies anfitriãs quando houver autorização, pertinência e capacidade compatíveis.

Princípio:

> **A superfície anfitriã define onde a publicidade pode existir. Guivos Ads define como o inventário publicitário autorizado é comercializado, operado, identificado e mensurado.**

A existência de uma superfície não transforma toda a superfície em inventário publicitário.

A elegibilidade de um anúncio depende também de sua pertinência ao contexto em que será exibido.

> **Capacidade financeira não implica elegibilidade publicitária.**

## Relação com Guivos Mall

Mall preserva autoridade sobre produto, categoria, busca, oferta, preço, estoque, transação e experiência comercial.

Ads pode operar, quando autorizado:

- banners contextuais;
- posições patrocinadas;
- marcas e fabricantes em destaque;
- produtos patrocinados;
- promoções;
- espaços especiais de categoria ou descoberta.

Pagamento não poderá alterar automaticamente busca, ordenação ou relevância orgânica do Mall.

## Relação com Guivos Travel

Travel preserva autoridade sobre destino, lugar, experiência, serviço, disponibilidade, preço, operação e reserva.

Ads pode operar, quando autorizado:

- destinos promovidos;
- hotéis e hospedagens patrocinadas;
- restaurantes;
- experiências e atrações;
- transportes, transfers e serviços relacionados;
- promoções, destaques e ativações pertinentes.

Pagamento não poderá transformar automaticamente uma oferta na melhor opção de viagem nem substituir critérios funcionais do Travel.

## Relação com Guivos Media

Guivos Ads pode comercializar patrocínios, ativações e distribuição patrocinada relacionadas ao Media.

Separação obrigatória:

```text
GUIVOS ADS
→ autoridade comercial publicitária

GUIVOS MEDIA
→ autoridade editorial
```

Patrocínio pode ser contratado. Conclusão editorial, relevância orgânica e autoridade editorial não podem ser compradas.

Conteúdo patrocinado deverá ser identificado.

## Relação com Guivos Journey

Journey preserva relevância orgânica, controles pessoais, contexto autorizado, Próximo Passo e autonomia do participante.

Ads pode operar exposição patrocinada em inventário permitido, incluindo Opportunity Boost quando aplicável.

> **Exposição pode ser patrocinada. Pertinência pessoal não.**

Ads não poderá utilizar pagamento para alterar Próximo Passo, recomendação individual ou ranking orgânico do Journey.

## Relação com Guivos Intelligence

Guivos Intelligence pode apoiar Ads em:

- interpretação de intenção comercial declarada;
- classificação e roteamento de leads;
- identificação de contexto comercial potencial;
- mensuração agregada;
- antifraude;
- enriquecimento operacional autorizado;
- análise de demanda;
- identificação de oportunidades futuras de produto Ads.

A inteligência deve utilizar finalidade legítima e dados permitidos.

Não poderá transformar em matéria-prima publicitária:

- relato pessoal protegido;
- compreensão inicial;
- Momento Atual;
- Próximo Passo individual;
- vulnerabilidade;
- mensagens privadas;
- inferências sensíveis;
- histórico sensível de localização;
- qualquer contexto individual sem base legítima compatível.

> **Guivos Intelligence ajuda a compreender a oportunidade comercial; não transforma o contexto pessoal protegido dos participantes em matéria-prima publicitária.**

## Conversão comercial inteligente

A entrada comercial do Guivos Ads deve privilegiar uma experiência progressiva, adaptativa e contextual de qualificação, em vez de um formulário estático longo.

Fluxo conceitual:

```text
ANUNCIANTE
→ declara o que deseja tornar mais visível
→ informa objetivo e contexto
→ experiência adapta perguntas
→ Intelligence pode interpretar contexto autorizado
→ Ads qualifica a oportunidade
→ operação comercial avalia elegibilidade e solução
```

A experiência pode começar por categorias como marca, produto, lançamento, promoção, lugar, estabelecimento, destino, experiência, serviço, história, conteúdo, oportunidade, atividade, programa, iniciativa ou projeto.

O anunciante não precisa conhecer previamente a taxonomia interna de produtos Guivos para avançar.

O resultado pode apresentar contexto e soluções potenciais, mas deve ser tratado como entendimento inicial. O envio representa manifestação de interesse, não aprovação de campanha, garantia de inventário, contratação, publicação ou autorização automática.

## Opportunity Boost

O Opportunity Boost é o mecanismo candidato de distribuição patrocinada de oportunidades, atividades e programas.

Sua responsabilidade inclui:

- receber configuração e orçamento;
- avaliar elegibilidade publicitária;
- distribuir somente em inventário patrocinado permitido;
- identificar a natureza comercial;
- limitar frequência e orçamento;
- medir eventos válidos;
- remover tráfego inválido;
- permitir pausa, cancelamento e reconciliação.

Sequência de referência:

```text
oportunidade aprovada e ativa
→ anunciante elegível
→ público permitido, orçamento e duração
→ avaliação publicitária e de segurança
→ inventário patrocinado identificado
→ mensuração de eventos válidos
→ encerramento e reconciliação
```

Opportunity Boost é um mecanismo do Ads e não deve ser confundido com a identidade integral do produto.

## Home Pública do Guivos Ads

A arquitetura estratégica, comercial, narrativa e funcional da Home Pública do produto é governada por `GKR-UX-HOME-ADS-MASTER-001` — **Home Pública — Guivos Ads — Documento Mestre**.

A Home v1 é primordialmente B2B e deve organizar a descoberta comercial por objetivo, contexto, solução e formato.

Arquitetura narrativa de referência:

```text
01 — oportunidade comercial
02 — contextos do ecossistema
03 — soluções por objetivo
04 — superfícies elegíveis
05 — formatos e possibilidades
06 — publicidade dentro do contexto certo
07 — conversão comercial inteligente
```

A Home não constitui tabela pública de preços, checkout de mídia, painel operacional de campanhas ou autorização para oferta comercial automática.

## Limites

Guivos Ads não substitui Journey, Mall, Travel, Business, Media ou Intelligence.

O produto não poderá:

- comprar relevância orgânica;
- alterar Próximo Passo pessoal por interesse comercial;
- utilizar compreensão protegida para segmentação;
- transformar pagamento em recomendação;
- conceder ao anunciante acesso indevido ao participante;
- prometer conversão, alcance, impacto ou resultado sem evidência e autoridade;
- ocultar publicidade ou patrocínio;
- transformar todas as superfícies Guivos em funis de venda;
- assumir autoridade editorial do Media;
- assumir autoridade transacional do Mall;
- assumir autoridade operacional do Travel;
- assumir autoridade experiencial do Journey;
- assumir autoridade analítica do Intelligence.

## Relações principais

- Journey preserva relevância orgânica, controles pessoais e proteção da jornada;
- Business preserva identidade e responsabilidade institucional quando aplicável;
- Intelligence apoia qualificação, análise e mensuração autorizadas sem segmentação sensível;
- Mall preserva busca, oferta e transação;
- Travel preserva contexto de viagem, operação e reserva;
- Media preserva autoridade editorial;
- a superfície anfitriã preserva contexto, acessibilidade, segurança, densidade e finalidade funcional;
- Ads preserva relação publicitária, campanha, inventário autorizado, identificação e mensuração comercial;
- possui Home Pública especializada governada por `GKR-UX-HOME-ADS-MASTER-001`.

## Estado

`home_architecture_converged — public Ads Home concept and smart commercial qualification defined; commercial validation, final pricing, inventory operation, design and implementation remain pending`.
