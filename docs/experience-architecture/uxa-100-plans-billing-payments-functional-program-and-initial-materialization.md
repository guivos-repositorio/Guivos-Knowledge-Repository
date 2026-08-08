---
id: UXA-100
title: Programa Funcional, Materialização, Validação e Promoção de Planos, Cobrança e Pagamentos
status: draft
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-000
depends_on:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GEM-004-PAYWALL-POLICY-001
  - GEM-004-UPGRADE-DOWNGRADE-CANCELLATION-POLICY-001
  - GEM-COMMERCIAL-BASELINE-001
  - GEM-003-PAYER-BENEFICIARY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - UXA-011-A1
  - UXA-070
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - GPA-004
  - GKR-STATE-001
normative: false
---

# Programa Funcional, Materialização, Validação e Promoção de Planos, Cobrança e Pagamentos

## 1. Finalidade

A UXA-100 estrutura, materializa, valida e registra canonicamente a experiência documental de **planos, comparação de benefícios, cobrança, pagamento e ciclo de vida comercial** para os participantes já materializados nesta frente:

- Pessoa;
- Coletivo;
- Organização.

Guivos Business é tratado separadamente como **produto especializado**, não como tipo de participante. Sua taxonomia conceitual é governada por `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`, mas esta UXA não cria nova jornada, superfície, transição ou SVG para o produto.

A frente deriva das autoridades econômicas vigentes e **não autoriza oferta pública, cobrança real, gateway, implantação, desenvolvimento, política fiscal final ou publicação de preços como oferta vigente**.

A versão 0.6.0 consolida a taxonomia global aprovada, formaliza **Organização ≠ Guivos Business**, corrige `BND-002` e preserva integralmente a estrutura canônica já promovida pela UXA-100-A3.

## 2. Autoridade conceitual dos planos

A leitura normativa é:

| Contexto | Planos |
|---|---|
| **Pessoa** | Free · Plus · Pro |
| **Coletivo** | Livre · Mobiliza · Impacta · Rede |
| **Organização** | Conecta · Eleva · Transforma |
| **Guivos Business** | Start · Growth · Scale · Enterprise |

Plano significa **profundidade de serviço, capacidade, escopo ou complexidade atendida**.

Plano não significa valor humano, mérito, relevância, legitimidade, impacto automaticamente comprovado ou nível de evolução. Não existe progressão obrigatória entre planos.

## 3. Pergunta funcional

A experiência deve responder, sem coerção:

> **Qual plano está ativo, o que ele inclui, qual limite foi alcançado, quais alternativas gratuitas permanecem válidas, o que muda ao escolher outro plano, quem paga e quem recebe o benefício, qual é a recorrência e o que acontece em sucesso, falha, downgrade ou cancelamento?**

Para a Pessoa existe uma obrigação adicional:

> **Como limitar correspondências personalizadas do Guivos Free sem esconder oportunidades públicas nem transformar pagamento em condição para descobrir oportunidades?**

## 4. Autoridades e limites preservados

### 4.1 Preços candidatos

Valores exibidos permanecem **preços candidatos para simulação documental**, quando já houver autoridade econômica aplicável ao mesmo contexto.

A mudança de nome não cria novo preço, não altera automaticamente limite e não cria entitlement.

Para Guivos Business, esta atualização **não inventa preços ou entitlements**. Referências históricas a Business Start/Growth/Scale dentro da antiga jornada de Organização não podem ser reutilizadas automaticamente como tabela comercial do produto Guivos Business.

### 4.2 Oportunidade pública não é ofuscada

O limite do Guivos Free recai sobre uma **correspondência personalizada adicional após a cota semanal**, não sobre a existência da oportunidade pública.

Permanecem disponíveis, conforme regras públicas aplicáveis:

- Explorar;
- Mapa;
- catálogo público;
- informações públicas essenciais;
- segurança, preço, prazo e responsabilidade da oferta quando publicamente acessíveis.

É proibido ocultar ou desfocar oportunidade pública para pressionar upgrade.

### 4.3 Pagamento não altera relevância

Plano pago não eleva posição orgânica, relevância funcional, veracidade, confiança, legitimidade, impacto ou evolução humana.

### 4.4 Assinatura é distinta de transação

```text
assinatura da plataforma
≠ preço de atividade ou oportunidade
≠ comissão
≠ taxa do meio de pagamento
≠ tributo
```

### 4.5 Parâmetros não definidos

A UXA-100 não inventa:

- gateway ou adquirente;
- bandeira, PIX, boleto ou carteira oficial;
- tokenização;
- prazo de tolerância após falha;
- pró-rata ou crédito entre ciclos;
- política fiscal/tributária definitiva;
- trial com conversão automática.

Nos wireframes, pagamento aparece apenas como **método autorizado em simulação**.

## 5. Decisão estrutural e fragmentação

Planos e cobrança não usam `COM-*`, pois `COM-*` permanece reservado ao Opportunity Boost/publicidade.

A UXA-100-A3 preserva quatro famílias canônicas para cada participante materializado:

1. **`*-301 — Planos e comparação`**;
2. **`*-302 — Revisão de contratação`**;
3. **`*-303 — Gestão de downgrade e cancelamento`**;
4. **`*-304 — Resultado e recuperação`**.

Não recebem superfície própria:

- comparação incremental isolada;
- processamento de pagamento;
- mensagens simples de confirmação;
- periodicidade mensal/anual;
- preview contextual de limite;
- contratação assistida como checkout.

## 6. BND-002 — fronteira corrigida

`BND-002` significa **fronteira de contratação/dimensionamento assistido**.

Ela é acionada quando uma contratação deixa de ser autonomamente configurável e passa a exigir proposta, dimensionamento, análise específica, contrato ou configuração assistida.

`BND-002`:

- não é plano;
- não é checkout;
- não é tela autônoma;
- não pertence semanticamente a Enterprise ou Scale;
- não pertence exclusivamente a um tipo de participante.

`TRN-416` e `TRN-426` preservam seus IDs e maturidade parcial. A correção de significado não constitui promoção nem validação ponta a ponta.

## 7. Espinha dorsal transversal canônica

```text
*-301 Planos e comparação
├── contratação autônoma
│   → *-302 revisão de contratação
│   → *-304 resultado/recuperação
│   → *-301 estado reconciliado
├── downgrade/cancelamento
│   → *-303 revisão do ciclo e consequências
│   → *-304 resultado/recuperação
│   → *-301 estado reconciliado
└── quando necessário
    → BND-002 contratação/dimensionamento assistido
```

## 8. Comparação entre planos

A experiência possui duas leituras complementares:

- **matriz geral**, com todos os planos e capacidades;
- **delta incremental**, mostrando somente o que o plano superior acrescenta ao imediatamente inferior.

```text
plano superior
= tudo o que permanece do plano anterior
+ benefícios/capacidades adicionais deste degrau
```

Benefícios herdados não são reapresentados como novidades.

Quando plano atual e alvo são conhecidos, a interface também apresenta o **delta direto atual → escolhido**. No downgrade, a regra se inverte: a revisão destaca exatamente o que deixa de existir ou terá limite reduzido.

Esta comparação é de capacidade e serviço, nunca de mérito ou evolução do participante.

## 9. Entradas nas jornadas

Existem dois pontos legítimos de entrada:

```text
entrada voluntária
Conta / Administração / Configurações
→ Planos
```

```text
entrada contextual
limite legítimo atingido
→ alternativas gratuitas/operacionais aplicáveis
→ comparar planos
→ Planos
```

O participante **não precisa atingir limite** para consultar ou administrar seu plano.

A UXA-100 não inventa transições de origem quando `Conta/Configurações`, publicação ou correspondência personalizada ainda não possuem identidade canônica suficiente para o handoff.

## 10. Pessoa

### 10.1 Planos candidatos e leitura conceitual

| Plano | Mensal candidato | Anual candidato | Leitura conceitual |
|---|---:|---:|---|
| **Free** | R$ 0,00 | R$ 0,00 | começar sem barreira econômica |
| **Plus** | R$ 24,90 | R$ 249,00 | aprofundar a jornada com mais contexto e continuidade |
| **Pro** | R$ 49,90 | R$ 499,00 | operar a própria jornada com maior profundidade e capacidade analítica |

Correspondências personalizadas completas permanecem com a referência já governada: Free com duas por semana; Plus sem cota semanal fixa, sujeito a uso justo; Pro sem cota semanal fixa, com análise ampliada.

### 10.2 Free com cota esgotada

Após duas correspondências completas abertas na semana, uma correspondência adicional pode preservar categoria, modalidade, localidade, prazo, natureza gratuita/paga, indicação de relação autorizada e período de renovação, enquanto limita a camada personalizada adicional.

Devem permanecer acessíveis: `Explorar oportunidades públicas`, `Ver no Mapa` e `Conhecer o Guivos Plus`.

### 10.3 Superfícies e transições

- `PER-301` — Planos e comparação;
- `PER-302` — revisão de contratação;
- `PER-303` — downgrade/cancelamento;
- `PER-304` — resultado/recuperação;
- `TRN-401` a `TRN-405` — localmente validadas.

![Pessoa — Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

## 11. Coletivo

### 11.1 Planos candidatos e leitura conceitual

A nomenclatura anterior Gestão / Impacto / Enterprise é substituída por Mobiliza / Impacta / Rede, preservando os preços candidatos já governados no mesmo degrau onde aplicável.

| Plano | Mensal candidato | Anual candidato | Atividades/mês | Oportunidades/mês | Ativas | Leitura conceitual |
|---|---:|---:|---:|---:|---:|---|
| **Livre** | R$ 0,00 | R$ 0,00 | 1 gratuita | 1 gratuita | 2 | organizar e agir livremente em escala inicial |
| **Mobiliza** | R$ 89,90 | R$ 899,00 | 4 | 4 | 6 | transformar intenção em mobilização coordenada |
| **Impacta** | R$ 249,90 | R$ 2.499,00 | 15 | 15 | 20 | transformar mobilização em impacto sustentado e evidenciado |
| **Rede** | sob consulta | contrato anual | capacidade contratada | capacidade contratada | capacidade contratada | conectar e coordenar múltiplos núcleos como uma rede |

Ao atingir cota ou tentar publicação paga, permanecem publicações existentes, rascunho, opção de aguardar ciclo, encerramento/agendamento quando aplicável e alternativa gratuita funcionalmente possível.

Antes do downgrade, o Coletivo trata publicações pagas/gratuitas, administradores, núcleos/unidades, compromissos e exportação. Não existe exclusão silenciosa.

### 11.2 Superfícies e transições

- `COL-301` — Planos e comparação;
- `COL-302` — revisão de contratação;
- `COL-303` — downgrade/cancelamento;
- `COL-304` — resultado/recuperação;
- `TRN-411` a `TRN-415` — localmente validadas;
- `TRN-416` — parcial até materialização do processo posterior a `BND-002`.

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

## 12. Organização

### 12.1 Separação obrigatória

Organização é um **tipo de participante do ecossistema**. Guivos Business é um **produto especializado**.

```text
Organização ≠ Guivos Business
Organização Transforma ≠ Guivos Business Enterprise
```

Não existe correspondência automática 1:1 entre os planos das duas estruturas.

### 12.2 Planos candidatos e leitura conceitual

Os preços e capacidades anteriormente governados dentro da jornada de Organização são preservados nos respectivos degraus, agora com a taxonomia correta de Organização. Isso não os transforma em preços do Guivos Business.

| Plano | Mensal candidato | Anual candidato | Novas oportunidades/programas | Ativas | Administradores | Unidades | Leitura conceitual |
|---|---:|---:|---:|---:|---:|---:|---|
| **Conecta** | R$ 299,00 | R$ 2.990,00 | 10/mês | 15 | 3 | 1 | conectar capacidade institucional a pessoas, coletivos e oportunidades |
| **Eleva** | R$ 799,00 | R$ 7.990,00 | 50/mês | 75 | 10 | até 5 | elevar a capacidade institucional de gerar valor e continuidade |
| **Transforma** | a partir de R$ 1.990,00/mês | contrato anual | capacidade contratada | capacidade contratada | conforme contrato | múltiplas | transformar capacidade institucional em impacto sistêmico sustentado |

Quando a Organização atinge capacidade, devem permanecer visíveis limite, consumo, período de renovação, efeito exato da mudança e alternativas de arquivar/agendar/manter rascunho quando aplicáveis.

Antes do downgrade, seleciona unidades, administradores, publicações e Coletivos relacionados mantidos, integrações a encerrar e dados a exportar. Históricos/agregados não são apagados para forçar retenção.

### 12.3 Superfícies e transições

- `ORG-301` — Planos e comparação;
- `ORG-302` — revisão de contratação;
- `ORG-303` — downgrade/cancelamento;
- `ORG-304` — resultado/recuperação;
- `TRN-421` a `TRN-425` — localmente validadas;
- `TRN-426` — parcial até materialização do processo posterior a `BND-002`.

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

## 13. Guivos Business

A taxonomia conceitual do produto é:

| Plano | Leitura conceitual |
|---|---|
| **Start** | começar uma operação Business estruturada |
| **Growth** | expandir a operação Business com controle e continuidade |
| **Scale** | operar o Guivos Business em escala com capacidade compatível |
| **Enterprise** | adaptar o produto Business a contextos empresariais de alta complexidade |

Esta UXA não define preços, limites ou entitlements para esses quatro planos.

Não são criados `BUS-*`, nova jornada canônica, nova superfície, nova transição ou SVG. Uma futura materialização de Guivos Business dependerá de decisão governada própria.

## 14. Pagador e beneficiário

Toda revisão de contratação distingue explicitamente pagador, beneficiário, autoridade de cancelamento e escopo de dados necessário à cobrança.

Pagamento por terceiro não transfere automaticamente autoridade, acesso à jornada pessoal, dados sensíveis ou poder de alterar relevância/recomendação.

## 15. Resultado, falha e recuperação

`*-304` agrupa sucesso e falha porque ambos pertencem à responsabilidade de resultado/recuperação, mas as consequências permanecem distintas.

Falha informa:

- pagamento não confirmado;
- ativação não presumida;
- plano/estado anterior identificável;
- direitos essenciais preservados;
- caminho para tentar novamente/revisar método;
- ausência de duplicação por simples repetição da intenção.

A UXA-100 não define `grace_period`.

## 16. Downgrade e cancelamento

`*-303` mostra estado atual/futuro, capacidades perdidas/reduzidas, excedentes a tratar, data efetiva e alternativas de retorno. Cancelamento interrompe renovação futura, confirma plano posterior e não reativa sem autorização.

A UXA-100 não presume pró-rata, estorno ou crédito entre ciclos.

## 17. Materialização visual canônica preservada

### 17.1 Telas dedicadas

- `uxa-100-person-plans-screen-mobile.svg`;
- `uxa-100-collective-plans-screen-desktop.svg`;
- `uxa-100-organization-plans-screen-desktop.svg`.

### 17.2 Boards de fluxo

- `uxa-100-person-plans-payments-flow-board.svg`;
- `uxa-100-collective-plans-payments-flow-board.svg`;
- `uxa-100-organization-plans-payments-flow-board.svg`.

### 17.3 Comparações incrementais

- `uxa-100-person-plan-incremental-benefits-comparison.svg`;
- `uxa-100-collective-plan-incremental-benefits-comparison.svg`;
- `uxa-100-organization-plan-incremental-benefits-comparison.svg`.

Inspeção: [Planos, Comparação e Cobrança — Galeria Canônica](../journeys/screen-gallery-plans-billing.md).

Os nove SVGs permanecem associados aos perfis `R29`, `R30` e `R31`. Nenhum SVG ou perfil adicional é criado para Guivos Business nesta atualização.

## 18. Resultado da validação e promoção preservado

A UXA-100-A2 permanece responsável pela auditoria histórica dos nove ativos. A UXA-100-A3 preserva a promoção canônica já registrada.

| Indicador | Estado preservado |
|---|---:|
| SVGs canônicos | **118** |
| associações | **118** |
| perfis | **31** |
| validações funcionais vigentes | **118** |
| pendências específicas | **0** |
| superfícies/estados/fronteiras | **53** |
| transições | **54** |
| IDs com referência visual | **42** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela | **2** |

A sincronização de taxonomia não constitui nova auditoria visual nem promoção adicional.

## 19. Fora do escopo

A UXA-100 não:

- valida preços no mercado;
- cria preços ou entitlements para Guivos Business;
- cria checkout real, gateway, nota fiscal, pró-rata, crédito ou grace period;
- implementa entitlement;
- publica oferta comercial;
- materializa o processo posterior a `BND-002`;
- cria `SURF`, `TRN`, `BND` ou SVG nesta sincronização;
- promove Pessoa, Coletivo ou Organização para `active`;
- cria jornada canônica para Guivos Business;
- inicia UXA-102/V5;
- inicia protótipo ou Engenharia de Produto.

## 20. Estado da frente

A UXA-100 permanece `draft` como programa documental, enquanto suas materializações e identidades já promovidas pela UXA-100-A3 preservam a maturidade governada existente.

A distinção é obrigatória:

```text
programa UXA-100 em draft
≠ ativos sem autoridade
≠ autorização de implementação
```

A autoridade conceitual vigente dos planos é `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`.

Nenhuma próxima UXA é iniciada automaticamente.