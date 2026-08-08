---
id: UXA-100-A4
title: Origens Administrativas e Handoffs de Entrada em Planos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-100
depends_on:
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
related:
  - UXA-015
  - UXA-017
  - UXA-086
  - UXA-087
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Origens Administrativas e Handoffs de Entrada em Planos

## 1. Finalidade

A UXA-100-A4 fecha exclusivamente a lacuna documental de **origem voluntária para Planos** identificada após a promoção canônica da UXA-100-A3.

As superfícies `PER-301`, `COL-301` e `ORG-301` já estavam validadas e aceitavam conceitualmente acesso por Conta, Configurações ou Administração, porém o registro de transições não possuía identidade canônica suficiente para os handoffs de origem.

Este incremento não cria checkout, cobrança real, gateway, entitlement, política fiscal, proration, processo posterior a `BND-002`, UXA-102/V5 ou Engenharia de Produto.

## 2. Pergunta governada

> Como uma Pessoa, um responsável por Coletivo ou um representante de Organização entra voluntariamente em Planos e retorna ao contexto administrativo sem que navegar para Planos seja confundido com intenção de contratar, upgrade, cobrança ou perda de contexto?

## 3. Achados da auditoria

### 3.1 Pessoa

A autoridade UXA-100 já declara entrada voluntária por `Conta / Configurações`, e o SVG canônico `uxa-100-person-plans-screen-mobile.svg` já apresenta `← Conta`.

Contudo, não existe no registro granular uma identidade própria para essa responsabilidade de Conta/Configurações. Portanto, não é correto inventar uma transição partindo de `PER-008`, `PER-108` ou outra superfície funcionalmente diferente.

### 3.2 Coletivo

`COL-002 — Visão Geral do Responsável` é o ponto inicial protegido de gestão do Coletivo. Sua navegação já prevê `Configurações`, e a superfície tem autoridade suficiente para abrir uma área de Planos sem criar uma nova tela intermediária.

### 3.3 Organização

`ORG-001 — Visão Geral da Organização` é a superfície inicial do contexto institucional e já possui navegação institucional.

A auditoria encontrou um desvio semântico no SVG `uxa-015-organization-overview-desktop.svg`: o cabeçalho lateral ainda dizia `Guivos Business`, em conflito com a autoridade vigente:

```text
Organização ≠ Guivos Business
Organização Transforma ≠ Guivos Business Enterprise
```

Esse desvio precisa ser corrigido antes de usar `ORG-001` como origem segura para Planos.

## 4. Decisão estrutural

A UXA-100-A4 adota a menor mudança que fecha a identidade dos handoffs:

1. criar `GKR-SURF-PER-009` como responsabilidade canônica de **Conta e configurações da Pessoa**, sem SVG dedicado nesta frente;
2. registrar ida e retorno `PER-009 ↔ PER-301`;
3. reutilizar `COL-002` como origem administrativa do Coletivo e registrar `COL-002 ↔ COL-301`;
4. reutilizar `ORG-001` como origem administrativa da Organização e registrar `ORG-001 ↔ ORG-301`;
5. reformular in-place as navegações de `COL-002` e `ORG-001` para tornar Planos explícito;
6. corrigir o rótulo obsoleto `Guivos Business` da Visão Geral da Organização;
7. preservar os 118 SVGs e os 31 perfis de rastreabilidade, sem criar um SVG artificial de Conta.

## 5. Pessoa — origem conhecida, superfície ainda não materializada

### 5.1 Nova responsabilidade canônica

`GKR-SURF-PER-009 — Conta e configurações da Pessoa` representa exclusivamente a responsabilidade protegida de administrar preferências, configurações e acessos de conta suficientes para navegação governada.

Nesta frente:

- não recebe SVG dedicado;
- não define toda a arquitetura de Conta;
- não agrega privacidade, segurança, notificações, dados ou preferências por inferência;
- serve como origem e destino canônicos do acesso voluntário a Planos.

### 5.2 Transições

- `GKR-TRN-406` — `PER-009 → PER-301` — abrir Planos voluntariamente;
- `GKR-TRN-407` — `PER-301 → PER-009` — retornar a Conta sem alteração de plano.

Estado: **contratadas**, pois a autoridade e o retorno são conhecidos, mas `PER-009` ainda não possui materialização suficiente para validação ponta a ponta.

Navegar por `TRN-406`:

- não seleciona plano;
- não cria intenção de contratação;
- não consome cota;
- não altera consentimento;
- não cria cobrança;
- não muda relevância ou jornada pessoal.

## 6. Coletivo — origem administrativa reaproveitada

### 6.1 Origem

`COL-002 — Visão Geral do Responsável` já governa contexto, representação e navegação de gestão. A navegação passa a apresentar explicitamente `Planos e cobrança` como destino protegido, sem transformar a Visão Geral em tela comercial.

### 6.2 Transições

- `GKR-TRN-417` — `COL-002 → COL-301` — abrir Planos preservando Coletivo e autoridade representada;
- `GKR-TRN-418` — `COL-301 → COL-002` — retornar à Visão Geral sem alterar plano ou capacidade.

Estado: **integralmente validadas no limite documental da Guivos** por esta frente, porque origem, destino, autoridade, contexto, ausência de efeito comercial na simples navegação, retorno, interrupção e repetição idempotente são verificáveis no mesmo conjunto.

A validação da navegação não valida cobrança real nem as transições `TRN-411` a `TRN-416` além de suas maturidades existentes.

## 7. Organização — origem institucional reaproveitada

### 7.1 Correção semântica obrigatória

O SVG de `ORG-001` é reformulado sem criar novo ativo:

- `Guivos Business` deixa de aparecer como identidade da superfície;
- a navegação institucional passa a incluir `Planos e cobrança`;
- `Organização` permanece o contexto do participante institucional.

### 7.2 Transições

- `GKR-TRN-427` — `ORG-001 → ORG-301` — abrir Planos preservando Organização, unidade e autoridade;
- `GKR-TRN-428` — `ORG-301 → ORG-001` — retornar à Visão Geral sem alteração comercial.

Estado: **integralmente validadas no limite documental da Guivos** pelas mesmas propriedades de navegação segura aplicadas ao Coletivo.

A validação não converte Organização em Guivos Business e não promove `TRN-426`.

## 8. Contrato transversal de navegação

Os seis handoffs obedecem às regras:

```text
abrir Planos ≠ escolher plano
abrir Planos ≠ iniciar cobrança
retornar ≠ cancelar assinatura
repetir navegação ≠ duplicar efeito
contexto administrativo ≠ autoridade financeira automática
Organização ≠ Guivos Business
```

Em ida e retorno devem ser preservados, quando aplicáveis:

- participante representado;
- unidade ou Coletivo selecionado;
- papel e escopo de autoridade;
- estado anterior de plano;
- ausência de mutação comercial sem ação afirmativa posterior;
- possibilidade de interromper e retornar sem penalidade.

## 9. Efeito nas contagens

| Indicador | Antes | Após UXA-100-A4 |
|---|---:|---:|
| SVGs canônicos | 118 | **118** |
| associações individuais | 118 | **118** |
| perfis | 31 | **31** |
| superfícies/estados/fronteiras | 53 | **54** |
| transições documentais | 54 | **60** |
| IDs com referência visual | 42 | **42** |
| responsabilidades sem SVG dedicado | 9 | **10** |
| fronteiras sem tela | 2 | **2** |

A única nova identidade de superfície é `PER-009`. Os SVGs de Coletivo e Organização são reformulados in-place e não alteram a contagem visual.

## 10. Maturidade preservada

- Pessoa, Coletivo e Organização continuam `draft`;
- `TRN-401` a `405`, `411` a `415` e `421` a `425` preservam maturidade local;
- `TRN-416` e `TRN-426` continuam parciais;
- `BND-002` continua fronteira sem tela;
- cobrança real, gateway, proration e entitlement continuam não implementados;
- `PER-009` permanece sem materialização visual específica;
- UXA-102/V5 permanece não iniciada;
- Engenharia de Produto permanece pausada antes de W0-01.

## 11. Veredito

> **PASS — a origem voluntária de Planos pode ser canonizada sem criar novas telas de Planos nem uma tela artificial de Configurações. Coletivo e Organização possuem origens administrativas suficientes para handoffs bidirecionais validados; Pessoa recebe apenas a identidade de responsabilidade necessária, mantendo seus handoffs contratados até futura materialização própria.**

## 12. Próximo ato possível

Após integração desta frente, os próximos gaps permanecem separados:

- eventual materialização de `PER-009`, somente se a arquitetura de Conta justificar superfície própria;
- maturidade das transições internas de contratação/ciclo;
- processo posterior a `BND-002`;
- cobrança real e execução financeira;
- UXA-102/V5.

Nenhum deles é iniciado automaticamente por esta frente.
