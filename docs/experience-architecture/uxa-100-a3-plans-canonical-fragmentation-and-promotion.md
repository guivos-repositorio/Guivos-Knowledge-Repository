---
id: UXA-100-A3
title: Fragmentação e Promoção Canônica de Planos, Cobrança e Ciclo de Vida
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-100
depends_on:
  - UXA-100-A1
  - UXA-100-A2
  - GEM-004-A1
  - GEM-004-A2
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
normative: false
---

# Fragmentação e Promoção Canônica de Planos, Cobrança e Ciclo de Vida

## 1. Finalidade

A UXA-100-A3 transforma a materialização funcionalmente aprovada pela UXA-100-A2 em uma estrutura canônica de superfícies, estados e transições para **Pessoa, Coletivo e Organização**, preservando a regra de que um estado somente recebe identidade própria quando há mudança material de hierarquia, decisão, autoridade, visibilidade, dados, consequência, risco, continuidade, canal ou recuperação.

A promoção é documental. Ela não cria checkout real, gateway, cobrança, entitlement técnico, política fiscal, pró-rata, período de graça, processo comercial implementado ou Engenharia de Produto.

## 2. Decisão de fragmentação

Os nove SVGs da UXA-100 não serão convertidos em nove telas independentes nem cada estado interno dos boards receberá um ID próprio.

Para cada participante são promovidas quatro famílias canônicas:

1. **Planos e comparação** — plano atual, consumo/capacidade, matriz geral, delta incremental e delta direto atual → alvo;
2. **Revisão de contratação** — seleção afirmativa, preço, periodicidade, recorrência, pagador, beneficiário, início, método autorizado em simulação e confirmação;
3. **Gestão de downgrade e cancelamento** — estado atual/futuro, capacidades afetadas, data efetiva e tratamento de excedentes/compromissos;
4. **Resultado e recuperação** — sucesso, falha, preservação do estado anterior quando necessário, evidência, retorno e nova tentativa.

Não recebem superfície própria:

- comparação incremental isolada, pois preserva a hierarquia e a decisão da superfície de Planos;
- processamento de pagamento, por ser estado transitório sem decisão própria;
- mensagens simples de confirmação;
- preço mensal/anual como telas independentes;
- preview contextual de limite, que permanece gatilho/estado de entrada para Planos e não substitui a superfície de origem;
- Enterprise/Scale como checkout, pois exigem processo comercial governado.

## 3. Novas superfícies canônicas

### 3.1 Pessoa

| ID | Superfície | Materialização principal |
|---|---|---|
| `GKR-SURF-PER-301` | Planos e comparação da Pessoa | tela dedicada + comparação incremental + estados de entrada do board |
| `GKR-SURF-PER-302` | Revisão de contratação da Pessoa | board de fluxo UXA-100 |
| `GKR-SURF-PER-303` | Gestão de downgrade e cancelamento da Pessoa | board de fluxo UXA-100 |
| `GKR-SURF-PER-304` | Resultado e recuperação de plano/cobrança da Pessoa | board de fluxo UXA-100 |

### 3.2 Coletivo

| ID | Superfície | Materialização principal |
|---|---|---|
| `GKR-SURF-COL-301` | Planos e comparação do Coletivo | tela dedicada + comparação incremental + estados de limite do board |
| `GKR-SURF-COL-302` | Revisão de contratação do Coletivo | board de fluxo UXA-100 |
| `GKR-SURF-COL-303` | Gestão de downgrade e cancelamento do Coletivo | board de fluxo UXA-100 |
| `GKR-SURF-COL-304` | Resultado e recuperação de plano/cobrança do Coletivo | board de fluxo UXA-100 |

### 3.3 Organização

| ID | Superfície | Materialização principal |
|---|---|---|
| `GKR-SURF-ORG-301` | Planos e comparação da Organização | tela dedicada + comparação incremental + estados de capacidade do board |
| `GKR-SURF-ORG-302` | Revisão de contratação da Organização | board de fluxo UXA-100 |
| `GKR-SURF-ORG-303` | Gestão de downgrade e cancelamento da Organização | board de fluxo UXA-100 |
| `GKR-SURF-ORG-304` | Resultado e recuperação de plano/cobrança da Organização | board de fluxo UXA-100 |

### 3.4 Fronteira comercial

`GKR-SURF-BND-002 — processo comercial Enterprise/Scale` identifica o handoff para proposta e dimensionamento contratual. É fronteira documental, não checkout nem tela Guivos autônoma.

## 4. Novas transições canônicas

### 4.1 Pessoa

| ID | Origem | Destino | Significado | Estado inicial |
|---|---|---|---|---|
| `GKR-TRN-401` | PER-301 | PER-302 | escolher Plus/Pro e revisar contratação | localmente validada |
| `GKR-TRN-402` | PER-302 | PER-304 | confirmar intenção e receber resultado de cobrança/ativação | localmente validada |
| `GKR-TRN-403` | PER-301 | PER-303 | iniciar downgrade ou cancelamento | localmente validada |
| `GKR-TRN-404` | PER-303 | PER-304 | confirmar mudança de ciclo e registrar resultado | localmente validada |
| `GKR-TRN-405` | PER-304 | PER-301 | retornar ao estado reconciliado de plano/cobrança | localmente validada |

### 4.2 Coletivo

| ID | Origem | Destino | Significado | Estado inicial |
|---|---|---|---|---|
| `GKR-TRN-411` | COL-301 | COL-302 | escolher Gestão/Impacto e revisar contratação | localmente validada |
| `GKR-TRN-412` | COL-302 | COL-304 | confirmar intenção e receber resultado | localmente validada |
| `GKR-TRN-413` | COL-301 | COL-303 | iniciar downgrade ou cancelamento | localmente validada |
| `GKR-TRN-414` | COL-303 | COL-304 | confirmar mudança após tratar excedentes/compromissos | localmente validada |
| `GKR-TRN-415` | COL-304 | COL-301 | retornar ao estado reconciliado | localmente validada |
| `GKR-TRN-416` | COL-301 | BND-002 | solicitar proposta Enterprise | parcial |

### 4.3 Organização

| ID | Origem | Destino | Significado | Estado inicial |
|---|---|---|---|---|
| `GKR-TRN-421` | ORG-301 | ORG-302 | escolher Growth e revisar contratação | localmente validada |
| `GKR-TRN-422` | ORG-302 | ORG-304 | confirmar intenção e receber resultado | localmente validada |
| `GKR-TRN-423` | ORG-301 | ORG-303 | iniciar downgrade ou cancelamento | localmente validada |
| `GKR-TRN-424` | ORG-303 | ORG-304 | confirmar mudança após tratar excedentes | localmente validada |
| `GKR-TRN-425` | ORG-304 | ORG-301 | retornar ao estado reconciliado | localmente validada |
| `GKR-TRN-426` | ORG-301 | BND-002 | solicitar proposta Business Scale | parcial |

## 5. Por que as transições não são promovidas integralmente

A UXA-100-A2 validou os estados e decisões representados nos nove SVGs, mas não definiu gateway, proration, regra fiscal, período de graça, antifraude ou execução do processo comercial Enterprise/Scale.

Por isso:

- as quinze ligações internas são **localmente validadas** no pacote UXA-100;
- `TRN-416` e `TRN-426` permanecem **parciais** porque o processo comercial após a fronteira não foi materializado como conjunto;
- nenhuma delas é apresentada como implementação técnica ou operação real.

## 6. Promoção dos nove SVGs

Os nove SVGs funcionalmente aprovados pela UXA-100-A2 passam a integrar o conjunto canônico:

- 3 telas dedicadas de Planos;
- 3 boards de fluxo;
- 3 comparações incrementais.

Efeito proposto:

| Indicador | Antes | Após UXA-100-A3 |
|---|---:|---:|
| SVGs canônicos | 109 | **118** |
| associações individuais | 109 | **118** |
| perfis de rastreabilidade | 28 | **31** |
| SVGs com validação funcional vigente | 109 | **118** |
| pendentes de validação específica | 0 | **0** |
| superfícies/estados/fronteiras | 40 | **53** |
| transições documentais | 37 | **54** |
| IDs com referência visual | 30 | **42** |
| responsabilidades sem SVG dedicado | 9 | **9** |
| fronteiras sem tela por definição | 1 | **2** |

Os três novos perfis de rastreabilidade são:

- `R29` — Pessoa: PER-301 a PER-304;
- `R30` — Coletivo: COL-301 a COL-304;
- `R31` — Organização: ORG-301 a ORG-304.

## 7. Proteções preservadas

- oportunidade pública não é escondida para vender plano;
- limite do Free recai sobre correspondência personalizada adicional, não sobre o catálogo público;
- assinatura não compra relevância, confiança, impacto, legitimidade ou evolução;
- assinatura é separada de preço de oferta, comissão, taxa de pagamento e tributo;
- nenhuma opção paga é pré-selecionada;
- downgrade/cancelamento mostram consequência e data aplicável;
- falha não presume ativação nem autoriza perda de dados;
- Enterprise/Scale não fingem checkout autônomo;
- trial com conversão automática continua fora da baseline;
- parâmetros financeiros indefinidos continuam indefinidos.

## 8. Jornadas

A promoção canônica adiciona superfícies e transições estáveis às jornadas `draft`, mas **não promove Pessoa, Coletivo ou Organização a `active`**.

A etapa transversal torna-se:

```text
Planos e comparação
├── upgrade → revisão de contratação → resultado/recuperação → Planos
├── downgrade/cancelamento → revisão de ciclo → resultado/recuperação → Planos
└── Enterprise/Scale → fronteira de proposta comercial
```

Entradas voluntárias e contextuais permanecem válidas. A ausência de uma superfície canônica única para `Conta/Configurações` ou para a correspondência personalizada não será preenchida por inferência nesta frente.

## 9. Limites

A UXA-100-A3 não:

- cria superfície canônica para cada texto/estado do board;
- cria checkout, gateway ou cobrança;
- define proration, estorno, período de graça ou tributação;
- materializa o processo após `BND-002`;
- valida `TRN-416` ou `TRN-426` ponta a ponta;
- altera `TRN-205`, `TRN-304`, `TRN-305` ou `TRN-306`;
- promove as jornadas principais;
- inicia protótipo ou Engenharia de Produto;
- integra a PR #199 ou a PR #200 à `main`.

## 10. Veredito

> **Promoção canônica aprovada documentalmente com fragmentação mínima: quatro famílias por participante, uma fronteira comercial compartilhada, nove SVGs incorporados ao catálogo canônico e dezessete transições registradas com maturidade explícita.**
