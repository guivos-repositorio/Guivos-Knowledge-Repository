---
id: GPA-SPECIALIZED-EXPERIENCE-POLICY-001
title: Política de Representação e Handoffs entre Produtos Especializados
status: approved
version: 2.0.0
owner: Guivos
last_updated: 2026-08-08
depends_on:
  - GPA-000
  - GLPA-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
related:
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-059
  - UXA-101
normative: true
---

# Política de Representação e Handoffs entre Produtos Especializados

## 1. Finalidade

Esta política define quando Journey, Mall, Travel, Business, Media, Intelligence e Ads devem ficar perceptíveis na experiência e quando uma passagem entre responsabilidades exige handoff explícito.

O objetivo é preservar uma experiência Guivos unificada sem esconder mudanças materiais de responsabilidade, autoridade, dados, consequência, contrato ou recuperação.

## 2. Separação estrutural obrigatória

```text
Pessoa / Coletivo / Organização
= papéis estruturais de participante

Journey / Mall / Travel / Business / Media / Intelligence / Ads
= Produtos Especializados/camadas de produto
```

Produto não é participante e participante não é produto.

Em especial:

- Organização ≠ Guivos Business;
- oportunidade/programa de uma Organização ≠ Guivos Business;
- plano de Organização é `Conecta · Eleva · Transforma`;
- tier de Guivos Business é `Start · Growth · Scale · Enterprise`;
- uma Organização pode existir e operar no ecossistema sem contratar Guivos Business;
- Parceria Estratégica corporativa da Guivos não é Produto Especializado nem quarto tipo de participante.

## 3. Princípio central

**Produto arquitetural não equivale automaticamente a tela, item de menu, marca visível ou etapa de jornada.**

O participante deve perceber uma mudança de produto quando essa informação altera materialmente sua expectativa sobre:

- quem executa a capacidade dominante;
- quem possui autoridade;
- qual relação/contrato está sendo exercido;
- quais dados/contextos são utilizados;
- qual consequência poderá ocorrer;
- como retorno, correção ou recuperação funcionam.

## 4. Modos de responsabilidade

| Modo | Significado | Exemplo vigente |
|---|---|---|
| host de experiência | organiza interação e controles visíveis | Journey em Hoje e descoberta |
| responsável especializado | executa a capacidade dominante do produto | Ads em Opportunity Boost |
| apoio transversal | fornece capacidade sem assumir a decisão primária da tela | Intelligence em interpretação autorizada |
| capacidade comum | sustenta produtos sem ser produto público independente | Platform/Auth/Billing conforme autoridade |
| autoridade externa | terceiro fora da autoridade Guivos | destino posterior a `BND-001` |

Guivos Business somente assume o modo de responsável especializado quando houver contexto B2B próprio e relação de produto identificável. A mera existência de uma Organização ou de uma superfície `ORG-*` não o ativa.

## 5. Níveis de visibilidade

### Nível 0 — interno e não perceptível

Use quando o produto apenas fornece capacidade interna e sua identificação não altera a decisão do participante.

### Nível 1 — proveniência ou explicação

Use quando o participante precisa compreender origem, inferência, recomendação, priorização ou outra contribuição material.

### Nível 2 — identificação contextual

Use quando há responsabilidade especializada relevante, mas sem mudança de ambiente ou decisão principal.

### Nível 3 — handoff interno explícito

Use quando a responsabilidade dominante muda entre Produtos Especializados ainda sob autoridade Guivos.

### Nível 4 — fronteira externa

Use quando a autoridade passa para terceiro fora da Guivos. `BND-001` pertence a esta classe.

### Fronteira assistida — BND-002

`BND-002` é uma fronteira genérica de contratação/dimensionamento assistido quando uma configuração deixa de ser resolvível por autoatendimento.

Ela:

- não é plano;
- não é produto;
- não é sinônimo de Business, Enterprise, Scale, Rede ou Transforma;
- não prova mudança de produto;
- não deve ser reutilizada como handoff Journey/Organização → Guivos Business sem contrato específico adicional.

## 6. Regras por Produto Especializado

### 6.1 Guivos Journey

- é o host principal da experiência;
- não precisa repetir seu nome em todas as superfícies;
- torna explícita a mudança quando outro produto passa a dominar materialmente a decisão;
- não absorve comércio, viagem, publicidade, conteúdo editorial ou inteligência apenas porque os apresenta.

### 6.2 Guivos Intelligence

- atua transversalmente e não exige tela própria para cada uso;
- deve preservar proveniência/explicabilidade quando inferência, recomendação ou priorização influenciar decisão material;
- não decide objetivo, desejo, valor ou verdade sobre a Pessoa;
- consumo por outro produto não cria handoff navegacional por si só.

### 6.3 Guivos Business

- é produto B2B especializado, separado do participante Organização;
- deve ficar perceptível quando existir relação Business própria — contratação, módulo, programa, capacidade ou operação B2B atribuível ao produto;
- não deve ser inferido apenas porque o ator é empresa, universidade, instituto, clínica, associação ou outra Organização;
- publicação de oportunidade para Pessoas/Coletivos permanece função de Organização quando esse for o objeto da relação;
- futura passagem de jornada institucional comum para Business requer contrato/handoff próprio e não pode ser deduzida de `ORG-*`, `TRN-203` ou `BND-002`.

### 6.4 Guivos Mall

- deve tornar-se explícito quando o contexto muda para comércio, item, pedido, compra, assinatura ou outra relação transacional sob responsabilidade Mall;
- recomendação ou menção de produto dentro do Journey não significa entrada no Mall;
- Journey → Mall é handoff interno quando a autoridade continua na Guivos;
- nenhum checkout, estoque, pagamento ou operação deve ser presumido enquanto não materializado/governado.

### 6.5 Guivos Travel

- deve tornar-se explícito quando o contexto muda para planejamento, experiência, roteiro, reserva ou operação de viagem sob responsabilidade Travel;
- oportunidade relacionada a viagem no Journey não é, por si só, superfície Travel;
- Journey → Travel é handoff interno quando a autoridade continua na Guivos;
- uma eventual execução externa poderá exigir fronteira própria conforme autoridade futura.

### 6.6 Guivos Media

- conteúdo editorial pode ser embutido no Journey sem handoff se a decisão principal continuar sob Journey;
- autoria/origem editorial devem ficar identificáveis quando relevantes;
- contexto editorial próprio só justifica nova superfície/transição quando houver mudança material de responsabilidade, navegação, dados, consequência ou recuperação.

### 6.7 Guivos Ads

- natureza patrocinada deve permanecer identificável;
- pagamento não compra relevância orgânica, recomendação pessoal, mérito ou autoridade;
- Ads → Journey preserva separação entre distribuição patrocinada e contexto orgânico;
- anunciante não se torna automaticamente Organização, Business ou Parceria Estratégica apenas pela contratação publicitária.

## 7. Contrato mínimo de handoff interno

| Campo | Pergunta obrigatória |
|---|---|
| origem | de qual superfície/responsabilidade o participante vem? |
| destino | qual produto passa a responder pela decisão dominante? |
| trigger | qual ação afirmativa ou evento legítimo inicia a passagem? |
| identidade | qual entidade lógica precisa permanecer a mesma? |
| contexto | qual contexto é realmente necessário no destino? |
| dados | quais dados podem atravessar e sob qual finalidade/autoridade? |
| autoridade | quem pode executar, negar, corrigir ou reverter? |
| consequência | o que muda se o handoff for concluído? |
| retorno | para onde o participante retorna sem perder estado legítimo? |
| recuperação | como falha, indisponibilidade, expiração e repetição são tratadas? |
| transparência | que mudança precisa ser visível para evitar expectativa falsa? |
| maturidade | contratado, materializado, localmente validado ou integralmente validado? |

## 8. Fragmentação de superfícies

Mudança de produto não cria automaticamente nova tela.

Fragmentar somente quando houver mudança material de uma ou mais dimensões:

- responsabilidade;
- autoridade;
- decisão primária;
- contrato/escopo;
- dados;
- consequência;
- risco;
- navegação/canal;
- retorno/recuperação.

## 9. Dados, contexto e autoridade

Handoff interno não autoriza compartilhamento irrestrito entre produtos.

Aplicam-se finalidade, minimização, autorização quando necessária, proveniência e separação de autoridade.

Journey não se torna autoridade transacional porque apresentou uma oferta. Intelligence não se torna autoridade sobre a Pessoa porque produziu inferência. Ads não recebe contexto protegido porque financiou distribuição. Business não recebe dados da Organização ou de Pessoas apenas pela existência de relação institucional.

## 10. Retorno e recuperação

Todo handoff material deve definir:

- retorno neutro;
- reconciliação com estado canônico;
- comportamento em indisponibilidade;
- idempotência quando aplicável;
- preservação somente de contexto ainda autorizado;
- ausência de sucesso presumido após falha.

## 11. Interno × externo

`BND-001` é reservado à passagem para autoridade externa.

Não usar `BND-001` para:

- Journey → Mall;
- Journey → Travel;
- Business → Journey;
- Ads → Journey;
- Media → Journey;
- chamadas internas a Intelligence.

A UXA-101 valida `TRN-205` somente até `BND-001`; execução posterior pertence ao terceiro.

`BND-002` é diferente: representa necessidade de contratação/dimensionamento assistido, sem afirmar por si só qual produto, contrato ou entidade executará o processo posterior.

## 12. Representação documental

Quando útil, novos artefatos podem declarar:

```text
experience_host: Journey | produto especializado | outro contexto governado
primary_product: Journey | Business | Mall | Travel | Media | Ads
supporting_products: Intelligence | outros
handoff_type: none | internal | assisted | external
```

Esses metadados são documentais e não obrigam branding ou elemento visual na interface.

## 13. Maturidade

Mapear produto responsável não valida superfície.

Identificar handoff não valida transição.

Materializar wireframe não implementa produto.

Arquitetura consolidada não comprova operação.

## 14. Efeito da política

Esta política rebaselineia a representação dos sete Produtos Especializados contra a autoridade corrente de participantes e planos.

Ela não cria:

- `SURF`;
- `TRN`;
- `BND`;
- SVG;
- UXA;
- preço/entitlement;
- implementação;
- autorização de Product Engineering.

A aplicação vigente é registrada em `GPA-SPECIALIZED-JOURNEY-MATRIX-001`.
