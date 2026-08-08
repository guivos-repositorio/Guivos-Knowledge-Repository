---
id: GPA-SPECIALIZED-EXPERIENCE-POLICY-001
title: Política de Representação e Handoffs entre Produtos
status: approved
version: 1.0.1
owner: Guivos
last_updated: 2026-08-08
related:
  - GLPA-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-059
  - UXA-101
---

# Política de Representação e Handoffs entre Produtos

## 1. Finalidade

Esta política define quando Journey, Intelligence, Business, Mall, Travel, Media e Ads devem ficar perceptíveis na experiência e quando uma passagem entre componentes exige um handoff explícito.

O objetivo é preservar uma experiência Guivos unificada sem esconder mudanças materiais de responsabilidade, autoridade, dados ou consequência.

## 2. Princípio central

**Produto arquitetural não equivale automaticamente a tela, item de menu, marca visível ou etapa de jornada.**

O participante deve perceber um produto especializado quando essa informação muda de forma material sua expectativa sobre quem executa o serviço, quem possui autoridade, quais dados serão usados, que consequência ocorrerá ou como ele poderá retornar/recuperar a ação.

## 3. Modos de responsabilidade

| Modo | Significado | Exemplo |
|---|---|---|
| host de experiência | organiza interação e controles visíveis | Journey em Hoje e exploração |
| responsável especializado | executa a capacidade de negócio dominante | Business em administração B2B; Ads em campanha patrocinada |
| apoio transversal | fornece capacidade sem assumir a decisão primária da tela | Intelligence em interpretação e recomendação |
| capacidade comum | sustenta produtos sem ser produto público independente | Platform/Billing/Auth |
| autoridade externa | terceiro fora do Ecossistema Guivos | destino de `BND-001` |

## 4. Níveis de visibilidade

### Nível 0 — interno e não perceptível
Use quando o produto apenas fornece uma capacidade técnica ou interna e sua identificação não muda a decisão do participante.

### Nível 1 — proveniência ou explicação
Use quando o participante precisa entender por que determinada compreensão, recomendação, ordenação ou análise apareceu.

### Nível 2 — identificação contextual
Use quando existe responsabilidade especializada relevante, mas sem mudança de ambiente ou decisão principal.

### Nível 3 — handoff interno explícito
Use quando o participante muda materialmente de responsabilidade dentro da própria Guivos, como uma futura passagem de Journey para Mall ou Travel.

### Nível 4 — fronteira externa
Use quando a autoridade passa para um terceiro fora do Ecossistema Guivos.

## 5. Regras por componente

### Guivos Journey
- é o host principal da experiência e não precisa repetir seu nome em todas as superfícies;
- deve tornar visível a mudança de responsabilidade quando outro produto passa a dominar a decisão;
- não absorve execução comercial, viagem, publicidade, conteúdo editorial ou inteligência apenas porque apresenta esses elementos.

### Guivos Intelligence
- não exige uma tela própria para cada uso;
- deve ter proveniência/explicabilidade quando inferência, recomendação ou priorização material influenciar a decisão;
- não pode ser apresentado como autoridade que decide objetivo, desejo ou verdade sobre a pessoa.

### Guivos Business
- deve ficar perceptível quando a pessoa está em contexto institucional/B2B, administração de organização, programa corporativo ou relação institucional material;
- pode operar por superfícies integradas à experiência Guivos sem exigir um aplicativo separado.

### Guivos Mall
- deve tornar-se explícito quando o contexto muda para comércio, carrinho, pedido, assinatura, compra ou outra relação transacional sob autoridade Mall;
- recomendação ou menção de produto dentro do Journey não significa entrada no Mall;
- uma futura passagem Journey → Mall é handoff interno e não `BND-001`.

### Guivos Travel
- deve tornar-se explícito quando o contexto muda para planejamento, operação de viagem, reserva, roteiro ou experiência turística sob autoridade Travel;
- oportunidade relacionada a viagem no Journey não é, por si só, uma superfície Travel;
- uma futura passagem Journey → Travel é handoff interno quando a autoridade continua na Guivos.

### Guivos Media
- conteúdo editorial pode ser embutido no Journey sem criar handoff;
- Media deve ser identificado quando autoria, origem editorial ou independência do contexto forem relevantes;
- um contexto editorial próprio só deve ganhar superfície/transição dedicada se houver mudança material de responsabilidade ou navegação.

### Guivos Ads
- toda natureza patrocinada deve permanecer identificável;
- pagamento não compra relevância orgânica, recomendação pessoal nem autoridade;
- integração Ads → Journey deve preservar a separação entre inventário patrocinado e contexto orgânico.

## 6. Contrato mínimo de handoff interno

| Campo | Pergunta obrigatória |
|---|---|
| origem | de qual superfície/responsabilidade o participante vem? |
| destino | qual produto passa a responder pela decisão dominante? |
| trigger | qual ação afirmativa ou evento legítimo inicia a passagem? |
| identidade | qual entidade lógica precisa permanecer a mesma? |
| contexto | que contexto é realmente necessário no destino? |
| dados | quais dados podem atravessar e sob qual autorização/finalidade? |
| autoridade | quem pode executar, negar, corrigir ou reverter a ação? |
| consequência | o que muda ao concluir o handoff? |
| retorno | para onde a pessoa retorna sem perder estado legítimo? |
| recuperação | como falha, indisponibilidade, expiração e repetição são tratadas? |
| transparência | que mudança precisa ser visível para não induzir expectativa falsa? |
| maturidade | contratado, materializado, localmente validado ou integralmente validado? |

## 7. Fragmentação de superfícies

A mudança de produto responsável não cria automaticamente uma nova tela.

A decisão de fragmentação deve separar apenas quando houver mudança material de hierarquia, decisão primária, autoridade, visibilidade, dados, consequência, risco, navegação, canal ou recuperação.

## 8. Dados, contexto e autoridade

Handoff interno não autoriza compartilhamento irrestrito entre produtos. Aplicam-se finalidade, minimização, autorização vigente quando necessária, proveniência e separação de autoridade.

Journey não se torna autoridade transacional porque apresentou uma oferta. Intelligence não se torna autoridade sobre a pessoa porque produziu uma inferência. Ads não ganha acesso a contexto protegido porque financiou distribuição.

## 9. Retorno e recuperação

Todo handoff material deve definir retorno neutro, reconciliação com estado canônico, comportamento em indisponibilidade, idempotência, preservação apenas de contexto ainda autorizado e ausência de sucesso presumido em falha.

## 10. Distinção obrigatória: interno × externo

`BND-001` é reservado à passagem para autoridade externa.

Não usar `BND-001` para Journey → Mall, Journey → Travel, Business → Journey, Ads → Journey, Media → Journey ou chamadas internas a Intelligence.

Na baseline vigente, a UXA-101 valida `GKR-TRN-205` somente até essa fronteira: a pessoa revisa a saída, identifica destino e responsável, entende os limites de dados/contexto e pode voltar ou permanecer no detalhe em caso de falha. O processo executado depois de `BND-001` continua sob autoridade do terceiro e não é validado por essa transição.

## 11. Representação em wireframes e documentação

Para novos artefatos, recomenda-se registrar no documento de origem, quando aplicável:

```text
experience_host: Guivos Journey | produto especializado
primary_product: Journey | Business | Mall | Travel | Media | Ads
supporting_products: Intelligence | outros
handoff_type: none | internal | external
```

Esses metadados são documentais e não obrigam branding ou elementos decorativos na UI.

## 12. Maturidade e validação

Mapear produto responsável não valida superfície; identificar handoff não valida transição; materializar wireframe não implementa produto; validação documental não comprova execução técnica.

## 13. Efeito desta política

Esta política consolida a regra de representação dos sete componentes sem criar novos IDs de superfície, transições, SVGs, UXA posterior ou Engenharia de Produto.

A versão 1.0.1 apenas sincroniza a fronteira externa com a UXA-101 já integrada, sem alterar as regras de handoff interno da versão 1.0.0.

A aplicação atual está registrada na [Matriz de Integração dos Produtos com as Jornadas](specialized-products-journey-integration-matrix.md).
