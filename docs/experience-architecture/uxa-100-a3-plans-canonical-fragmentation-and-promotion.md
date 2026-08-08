---
id: UXA-100-A3
title: Fragmentação e Promoção Canônica de Planos, Cobrança e Ciclo de Vida
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-100
depends_on:
  - UXA-100-A1
  - UXA-100-A2
  - GEM-004-A1
  - GEM-004-A2
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - GPA-004
normative: false
---

# Fragmentação e Promoção Canônica de Planos, Cobrança e Ciclo de Vida

## 1. Finalidade

A UXA-100-A3 transforma a materialização funcionalmente aprovada pela UXA-100-A2 em uma estrutura canônica de superfícies, estados e transições para **Pessoa, Coletivo e Organização**, preservando a regra de que um estado somente recebe identidade própria quando há mudança material de hierarquia, decisão, autoridade, visibilidade, dados, consequência, risco, continuidade, canal ou recuperação.

A promoção é documental. Ela não cria checkout real, gateway, cobrança, entitlement técnico, política fiscal, pró-rata, período de graça, processo comercial implementado ou Engenharia de Produto.

A versão 0.2.0 sincroniza a estrutura com `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`: atualiza a leitura dos planos, formaliza **Organização ≠ Guivos Business** e corrige `BND-002` como fronteira genérica de contratação/dimensionamento assistido. Nenhum `SURF`, `TRN`, `BND` ou SVG é criado, removido ou promovido por esta sincronização.

## 2. Decisão de fragmentação

Os nove SVGs da UXA-100 não serão convertidos em nove telas independentes nem cada estado interno dos boards receberá um ID próprio.

Para cada participante são preservadas quatro famílias canônicas:

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
- contratação assistida como checkout, pois exige processo comercial governado quando acionada.

## 3. Superfícies canônicas preservadas

### 3.1 Pessoa

| ID | Superfície | Materialização principal |
|---|---|---|
| `GKR-SURF-PER-301` | Planos e comparação da Pessoa | tela dedicada + comparação incremental + estados de entrada do board |
| `GKR-SURF-PER-302` | Revisão de contratação da Pessoa | board de fluxo UXA-100 |
| `GKR-SURF-PER-303` | Gestão de downgrade e cancelamento da Pessoa | board de fluxo UXA-100 |
| `GKR-SURF-PER-304` | Resultado e recuperação de plano/cobrança da Pessoa | board de fluxo UXA-100 |

Taxonomia: **Free · Plus · Pro**.

### 3.2 Coletivo

| ID | Superfície | Materialização principal |
|---|---|---|
| `GKR-SURF-COL-301` | Planos e comparação do Coletivo | tela dedicada + comparação incremental + estados de limite do board |
| `GKR-SURF-COL-302` | Revisão de contratação do Coletivo | board de fluxo UXA-100 |
| `GKR-SURF-COL-303` | Gestão de downgrade e cancelamento do Coletivo | board de fluxo UXA-100 |
| `GKR-SURF-COL-304` | Resultado e recuperação de plano/cobrança do Coletivo | board de fluxo UXA-100 |

Taxonomia: **Livre · Mobiliza · Impacta · Rede**.

### 3.3 Organização

| ID | Superfície | Materialização principal |
|---|---|---|
| `GKR-SURF-ORG-301` | Planos e comparação da Organização | tela dedicada + comparação incremental + estados de capacidade do board |
| `GKR-SURF-ORG-302` | Revisão de contratação da Organização | board de fluxo UXA-100 |
| `GKR-SURF-ORG-303` | Gestão de downgrade e cancelamento da Organização | board de fluxo UXA-100 |
| `GKR-SURF-ORG-304` | Resultado e recuperação de plano/cobrança da Organização | board de fluxo UXA-100 |

Taxonomia: **Conecta · Eleva · Transforma**.

### 3.4 Guivos Business não cria superfície nesta frente

Guivos Business possui taxonomia própria **Start · Growth · Scale · Enterprise**, mas permanece produto especializado, não participante canônico desta materialização.

A UXA-100-A3 não cria `BUS-*`, nova jornada, nova superfície, transição ou SVG para o produto.

A separação é obrigatória:

```text
Organização = participante
Guivos Business = produto especializado
```

Não existe correspondência automática 1:1 entre os respectivos planos.

### 3.5 Fronteira de contratação/dimensionamento assistido

`GKR-SURF-BND-002` identifica o handoff para **contratação/dimensionamento assistido** quando uma configuração deixa de ser autonomamente resolvível e passa a exigir proposta, dimensionamento, análise específica, contrato ou configuração assistida.

`BND-002`:

- não é checkout;
- não é tela Guivos autônoma;
- não é plano;
- não pertence semanticamente a Enterprise ou Scale;
- não pertence exclusivamente a Coletivo, Organização ou Guivos Business.

## 4. Transições canônicas preservadas

### 4.1 Pessoa

| ID | Origem | Destino | Significado | Estado |
|---|---|---|---|---|
| `GKR-TRN-401` | PER-301 | PER-302 | escolher Plus/Pro e revisar contratação | localmente validada |
| `GKR-TRN-402` | PER-302 | PER-304 | confirmar intenção e receber resultado de cobrança/ativação | localmente validada |
| `GKR-TRN-403` | PER-301 | PER-303 | iniciar downgrade ou cancelamento | localmente validada |
| `GKR-TRN-404` | PER-303 | PER-304 | confirmar mudança de ciclo e registrar resultado | localmente validada |
| `GKR-TRN-405` | PER-304 | PER-301 | retornar ao estado reconciliado de plano/cobrança | localmente validada |

### 4.2 Coletivo

| ID | Origem | Destino | Significado | Estado |
|---|---|---|---|---|
| `GKR-TRN-411` | COL-301 | COL-302 | escolher plano autonomamente contratável e revisar contratação | localmente validada |
| `GKR-TRN-412` | COL-302 | COL-304 | confirmar intenção e receber resultado | localmente validada |
| `GKR-TRN-413` | COL-301 | COL-303 | iniciar downgrade ou cancelamento | localmente validada |
| `GKR-TRN-414` | COL-303 | COL-304 | confirmar mudança após tratar excedentes/compromissos | localmente validada |
| `GKR-TRN-415` | COL-304 | COL-301 | retornar ao estado reconciliado | localmente validada |
| `GKR-TRN-416` | COL-301 | BND-002 | encaminhar contratação que exige dimensionamento assistido | parcial |

### 4.3 Organização

| ID | Origem | Destino | Significado | Estado |
|---|---|---|---|---|
| `GKR-TRN-421` | ORG-301 | ORG-302 | escolher plano autonomamente contratável e revisar contratação | localmente validada |
| `GKR-TRN-422` | ORG-302 | ORG-304 | confirmar intenção e receber resultado | localmente validada |
| `GKR-TRN-423` | ORG-301 | ORG-303 | iniciar downgrade ou cancelamento | localmente validada |
| `GKR-TRN-424` | ORG-303 | ORG-304 | confirmar mudança após tratar excedentes | localmente validada |
| `GKR-TRN-425` | ORG-304 | ORG-301 | retornar ao estado reconciliado | localmente validada |
| `GKR-TRN-426` | ORG-301 | BND-002 | encaminhar contratação que exige dimensionamento assistido | parcial |

A mudança de descrição de `TRN-416` e `TRN-426` é semântica e preserva sua maturidade parcial. Ela não constitui revalidação ponta a ponta.

## 5. Por que as transições não são promovidas integralmente

A UXA-100-A2 validou os estados e decisões representados nos nove SVGs, mas não definiu gateway, proration, regra fiscal, período de graça, antifraude ou execução do processo comercial após `BND-002`.

Por isso:

- as quinze ligações internas permanecem **localmente validadas** no pacote UXA-100;
- `TRN-416` e `TRN-426` permanecem **parciais** porque o processo após a fronteira não foi materializado como conjunto;
- nenhuma delas é apresentada como implementação técnica ou operação real.

## 6. Promoção dos nove SVGs preservada

Os nove SVGs funcionalmente aprovados pela UXA-100-A2 permanecem no conjunto canônico:

- 3 telas dedicadas de Planos;
- 3 boards de fluxo;
- 3 comparações incrementais.

As contagens permanecem:

| Indicador | Estado preservado |
|---|---:|
| SVGs canônicos | **118** |
| associações individuais | **118** |
| perfis de rastreabilidade | **31** |
| SVGs com validação funcional vigente | **118** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **53** |
| transições documentais | **54** |
| IDs com referência visual | **42** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela por definição | **2** |

Os perfis permanecem:

- `R29` — Pessoa: PER-301 a PER-304;
- `R30` — Coletivo: COL-301 a COL-304;
- `R31` — Organização: ORG-301 a ORG-304.

Nenhum perfil `R32` ou equivalente é criado para Guivos Business nesta frente.

## 7. Proteções preservadas

- oportunidade pública não é escondida para vender plano;
- limite do Free recai sobre correspondência personalizada adicional, não sobre o catálogo público;
- assinatura não compra relevância, confiança, impacto, legitimidade ou evolução;
- plano representa capacidade/serviço, não valor ou mérito do participante;
- assinatura é separada de preço de oferta, comissão, taxa de pagamento e tributo;
- nenhuma opção paga é pré-selecionada;
- downgrade/cancelamento mostram consequência e data aplicável;
- falha não presume ativação nem autoriza perda de dados;
- contratação assistida não finge checkout autônomo;
- Organização não é confundida com Guivos Business;
- trial com conversão automática continua fora da baseline;
- parâmetros financeiros indefinidos continuam indefinidos.

## 8. Jornadas

A estrutura canônica adicionada anteriormente às jornadas `draft` é preservada, mas **não promove Pessoa, Coletivo ou Organização a `active`**.

A etapa transversal passa a ser lida como:

```text
Planos e comparação
├── contratação autônoma → revisão → resultado/recuperação → Planos
├── downgrade/cancelamento → revisão de ciclo → resultado/recuperação → Planos
└── quando necessário → BND-002 contratação/dimensionamento assistido
```

Entradas voluntárias e contextuais permanecem válidas. A ausência de uma superfície canônica única para `Conta/Configurações` ou para a correspondência personalizada não será preenchida por inferência nesta frente.

## 9. Função, significado e leitura conceitual

A UXA-100-A3 adota integralmente `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`.

Planos significam profundidade de serviço, capacidade, escopo ou complexidade atendida. Não significam valor humano, mérito, prestígio, relevância, legitimidade ou nível de evolução.

A progressão não é obrigatória e o nome do plano não comprova impacto.

## 10. Limites

A UXA-100-A3 não:

- cria superfície canônica para cada texto/estado do board;
- cria checkout, gateway ou cobrança;
- define proration, estorno, período de graça ou tributação;
- materializa o processo após `BND-002`;
- valida `TRN-416` ou `TRN-426` ponta a ponta;
- altera `TRN-205`, `TRN-304`, `TRN-305` ou `TRN-306`;
- cria jornada ou superfícies para Guivos Business;
- promove as jornadas principais;
- inicia protótipo ou Engenharia de Produto;
- inicia UXA-102/V5.

## 11. Veredito

> **A estrutura canônica da UXA-100 é preservada sem novos IDs: quatro famílias por participante, uma fronteira compartilhada de contratação/dimensionamento assistido e nove SVGs mantidos. A taxonomia passa a ser Pessoa Free/Plus/Pro, Coletivo Livre/Mobiliza/Impacta/Rede e Organização Conecta/Eleva/Transforma; Guivos Business permanece produto especializado Start/Growth/Scale/Enterprise sem nova materialização nesta frente.**