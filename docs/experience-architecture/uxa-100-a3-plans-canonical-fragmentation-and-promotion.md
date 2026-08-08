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

A UXA-100-A3 registra a estrutura canônica de superfícies e transições de Planos para **Pessoa, Coletivo e Organização**, preservando fragmentação mínima e maturidade explícita.

A versão 0.2.0 não cria IDs nem promove maturidade. Ela sincroniza a taxonomia global e corrige `BND-002` para sua função genérica de contratação/dimensionamento assistido.

## 2. Taxonomia aplicada

- Pessoa: Free · Plus · Pro;
- Coletivo: Livre · Mobiliza · Impacta · Rede;
- Organização: Conecta · Eleva · Transforma.

Guivos Business Start/Growth/Scale/Enterprise é produto especializado fora desta fragmentação. `Organização Transforma ≠ Guivos Business Enterprise`.

## 3. Decisão de fragmentação preservada

Para cada participante permanecem quatro famílias:

1. **Planos e comparação** — plano atual, consumo/capacidade, matriz, delta incremental e direto;
2. **Revisão de contratação** — seleção afirmativa, preço/periodicidade quando governados, pagador, beneficiário, início e confirmação;
3. **Gestão de downgrade e cancelamento** — estado atual/futuro, capacidades afetadas, data efetiva e excedentes;
4. **Resultado e recuperação** — sucesso, falha, preservação do estado anterior, retorno e nova tentativa.

Não recebem superfície própria comparação incremental, processamento transitório, confirmação simples, periodicidade, preview de limite ou processo assistido.

## 4. Superfícies canônicas preservadas

### Pessoa

- `GKR-SURF-PER-301` — Planos e comparação;
- `GKR-SURF-PER-302` — revisão de contratação;
- `GKR-SURF-PER-303` — downgrade/cancelamento;
- `GKR-SURF-PER-304` — resultado/recuperação.

### Coletivo

- `GKR-SURF-COL-301` — Planos e comparação;
- `GKR-SURF-COL-302` — revisão de contratação;
- `GKR-SURF-COL-303` — downgrade/cancelamento;
- `GKR-SURF-COL-304` — resultado/recuperação.

### Organização

- `GKR-SURF-ORG-301` — Planos e comparação;
- `GKR-SURF-ORG-302` — revisão de contratação;
- `GKR-SURF-ORG-303` — downgrade/cancelamento;
- `GKR-SURF-ORG-304` — resultado/recuperação.

### Fronteira compartilhada

`GKR-SURF-BND-002 — contratação/dimensionamento assistido` identifica o handoff quando uma contratação deixa de ser autonomamente configurável e exige proposta, dimensionamento, contrato, configuração ou análise específica.

`BND-002`:

- não é checkout;
- não é plano;
- não significa Enterprise, Scale, Rede ou Transforma;
- não pertence exclusivamente a Coletivo ou Organização;
- não define preço, capacidade, SLA ou contrato.

## 5. Transições canônicas preservadas

### Pessoa

| ID | Origem | Destino | Significado | Estado |
|---|---|---|---|---|
| `GKR-TRN-401` | PER-301 | PER-302 | escolher Plus/Pro e revisar contratação | localmente validada |
| `GKR-TRN-402` | PER-302 | PER-304 | confirmar intenção e receber resultado | localmente validada |
| `GKR-TRN-403` | PER-301 | PER-303 | iniciar downgrade/cancelamento | localmente validada |
| `GKR-TRN-404` | PER-303 | PER-304 | confirmar mudança de ciclo | localmente validada |
| `GKR-TRN-405` | PER-304 | PER-301 | retornar ao estado reconciliado | localmente validada |

### Coletivo

| ID | Origem | Destino | Significado | Estado |
|---|---|---|---|---|
| `GKR-TRN-411` | COL-301 | COL-302 | escolher mudança autonomamente configurável e revisar | localmente validada |
| `GKR-TRN-412` | COL-302 | COL-304 | confirmar intenção e receber resultado | localmente validada |
| `GKR-TRN-413` | COL-301 | COL-303 | iniciar downgrade/cancelamento | localmente validada |
| `GKR-TRN-414` | COL-303 | COL-304 | confirmar mudança após tratar excedentes | localmente validada |
| `GKR-TRN-415` | COL-304 | COL-301 | retornar ao estado reconciliado | localmente validada |
| `GKR-TRN-416` | COL-301 | BND-002 | solicitar contratação/dimensionamento assistido quando necessário | **parcial** |

### Organização

| ID | Origem | Destino | Significado | Estado |
|---|---|---|---|---|
| `GKR-TRN-421` | ORG-301 | ORG-302 | escolher mudança autonomamente configurável e revisar | localmente validada |
| `GKR-TRN-422` | ORG-302 | ORG-304 | confirmar intenção e receber resultado | localmente validada |
| `GKR-TRN-423` | ORG-301 | ORG-303 | iniciar downgrade/cancelamento | localmente validada |
| `GKR-TRN-424` | ORG-303 | ORG-304 | confirmar mudança após tratar excedentes | localmente validada |
| `GKR-TRN-425` | ORG-304 | ORG-301 | retornar ao estado reconciliado | localmente validada |
| `GKR-TRN-426` | ORG-301 | BND-002 | solicitar contratação/dimensionamento assistido quando necessário | **parcial** |

## 6. Maturidade preservada

`TRN-416` e `TRN-426` continuam parciais porque o processo posterior a `BND-002` não foi materializado/validado como conjunto. A correção semântica da fronteira não constitui validação ponta a ponta.

## 7. Promoção visual preservada

Os mesmos nove SVGs permanecem canônicos:

- 3 telas dedicadas;
- 3 boards de fluxo;
- 3 comparações incrementais.

A sincronização substitui apenas nomenclatura/cópia em Coletivo e Organização. Não cria arquivo ou ID adicional.

Contagens permanecem:

| Indicador | Estado vigente |
|---|---:|
| SVGs canônicos | **118** |
| associações individuais | **118** |
| perfis de rastreabilidade | **31** |
| SVGs com validação funcional vigente | **118** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **53** |
| transições documentais | **54** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela por definição | **2** |

Perfis `R29`, `R30` e `R31` permanecem associados a Pessoa, Coletivo e Organização respectivamente.

## 8. Proteções preservadas

- oportunidade pública não é escondida para vender plano;
- assinatura não compra relevância, confiança, impacto, legitimidade ou evolução;
- assinatura é separada de transação/taxa/tributo;
- nenhuma opção paga é pré-selecionada;
- downgrade/cancelamento mostram consequência e data;
- falha não presume ativação nem perda de dados;
- contratação assistida não finge checkout autônomo;
- parâmetros financeiros indefinidos continuam indefinidos;
- nomes de plano não expressam mérito do participante.

## 9. Jornadas

A estrutura adicionada anteriormente às jornadas `draft` é preservada, sem promoção:

```text
Planos e comparação
├── mudança autônoma → revisão → resultado → Planos
├── downgrade/cancelamento → revisão → resultado → Planos
└── necessidade de contratação assistida → BND-002
```

Guivos Business não recebe quarta jornada ou novos IDs nesta atualização.

## 10. Limites

Esta versão não cria superfície, transição, SVG, checkout, gateway, cobrança, preço/entitlement Business, pró-rata, período de graça, processo posterior a `BND-002`, promoção de jornada, UXA-102/V5 ou Engenharia de Produto.

## 11. Veredito

> **Taxonomia global sincronizada e BND-002 corrigido sem expansão da arquitetura: IDs, contagens, maturidades e nove SVGs permanecem preservados.**
