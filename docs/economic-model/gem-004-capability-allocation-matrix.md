---
id: GEM-004-CAPABILITY-ALLOCATION-MATRIX-001
title: Matriz de Alocação de Capacidades
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-004
---

# Matriz de Alocação de Capacidades

## 1. Objetivo

Estabelecer como cada capacidade futura deverá ser classificada entre acesso gratuito, ampliação paga, acesso financiado, acesso de parceiros ou paywall proibido.

## 2. Estados canônicos

| Estado | Significado | Condição principal |
|---|---|---|
| `universal_free` | integra o valor gratuito obrigatório | necessário para participação, direitos ou valor essencial |
| `free_limited` | disponível gratuitamente com limite legítimo | gratuito continua útil e o limite é transparente |
| `paid_extension` | ampliação paga de capacidade existente | valor adicional identificável |
| `paid_specialized` | serviço ou capacidade especializada | custo, competência ou responsabilidade adicional |
| `organization_funded` | financiada por organização | beneficiário e limites de autoridade claros |
| `sponsor_funded` | financiada por patrocinador ou programa | finalidade e independência preservadas |
| `partner_access` | destinada a parceiro ou profissional | acesso proporcional ao papel |
| `temporarily_unlocked` | acesso temporário transparente | duração, encerramento e conversão claros |
| `prohibited_paywall` | não pode ser condicionado a pagamento | direito, segurança ou controle essencial |
| `not_assessed` | classificação pendente | não pode avançar para oferta |

## 3. Registro mínimo

```yaml
capability_id: string
name: string
product: string
value_object: string
allocation_state: string
essentiality:
  essential | important | optional | specialized
free_baseline_impact: string
payer: string | null
beneficiary: string
data_involved:
  - string
limits:
  - string
transition_effects:
  - string
risks:
  - string
validation_status: not_started
owner: unassigned
```

## 4. Perguntas obrigatórias

- Qual valor é produzido?
- A capacidade é essencial?
- O gratuito permanece útil sem a ampliação?
- O pago amplia ou apenas desfaz limitação artificial?
- Existem dados ou riscos adicionais?
- Quem paga e quem se beneficia?
- Quem pode cancelar ou contestar?
- O que ocorre no downgrade?
- A perda de acesso pode causar dano?
- Existe alternativa gratuita legítima?

## 5. Critérios para `universal_free`

A classificação é obrigatória quando a capacidade for necessária para:

- participação básica;
- segurança;
- transparência;
- correção e controle de dados;
- consentimento e revogação;
- cancelamento;
- contestação;
- acesso a registros essenciais;
- retorno ao gratuito;
- prevenção de dano material.

## 6. Critérios para `free_limited`

O limite deverá:

- refletir capacidade, custo ou risco real;
- ser informado antes do uso;
- possuir unidade compreensível;
- não impedir benefício básico;
- não reduzir segurança;
- permitir acompanhamento;
- evitar surpresa ou bloqueio abrupto;
- possuir tratamento de exceção quando necessário para evitar dano.

## 7. Critérios para `paid_extension`

A capacidade deverá:

- ampliar uma dimensão legítima;
- possuir valor adicional demonstrável;
- não ser direito básico;
- permitir downgrade;
- informar dados e limites;
- possuir hipótese de pagamento;
- não depender de influência ou urgência artificial.

## 8. Critérios para acesso financiado

Deverão ser registrados:

- financiador;
- beneficiário;
- finalidade;
- duração;
- dados acessíveis ao financiador;
- condição de término;
- continuidade no gratuito;
- conflito de interesse;
- proteção contra discriminação.

## 9. Conflitos de classificação

Quando uma capacidade puder pertencer a mais de um estado, prevalecerá:

1. `prohibited_paywall` sobre qualquer classificação paga;
2. `universal_free` sobre conveniência econômica;
3. o limite mais protetivo para dados e autonomia;
4. a classificação que preserve retorno ao gratuito;
5. `not_assessed` quando evidência for insuficiente.

## 10. Revisão de classificação

Mudanças materiais exigirão:

- justificativa;
- comparação antes/depois;
- impacto no gratuito;
- impacto em dados e direitos;
- evidência;
- plano de transição;
- comunicação;
- aprovação formal;
- possibilidade de reversão.

## 11. Fora do escopo

- inventário funcional completo por produto;
- limites numéricos;
- preço;
- interface;
- implementação de feature flags ou entitlement.
