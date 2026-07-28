---
id: GEM-004-CAPABILITY-ALLOCATION-MATRIX-001
title: Matriz de Alocação de Capacidades
status: active
version: 0.2.0
owner: Guivos Economic Model
last_updated: 2026-07-28
parent: GEM-004
related:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-COMMERCIAL-BASELINE-001
  - M7.39
---

# Matriz de Alocação de Capacidades

## 1. Objetivo

Estabelecer como cada capacidade deverá ser classificada entre acesso gratuito, ampliação paga, acesso financiado, acesso de parceiros ou paywall proibido.

A versão 0.2.0 incorpora exemplos da baseline comercial candidata.

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

## 3. Exemplos da baseline comercial

| Capacidade | Estado | Regra candidata |
|---|---|---|
| catálogo público de oportunidades | `universal_free` | acesso geral no Explorar e Mapa |
| correspondência personalizada completa | `free_limited` | 2 por semana no Guivos Free |
| correspondências personalizadas adicionais | `paid_extension` | Plus e Pro |
| análise aprofundada e comparativa | `paid_extension` | Pro |
| segurança, privacidade, correção e exclusão | `prohibited_paywall` | disponíveis em todos os planos |
| uma atividade gratuita do Coletivo | `free_limited` | 1 por mês no Coletivo Livre |
| uma oportunidade gratuita do Coletivo | `free_limited` | 1 por mês no Coletivo Livre |
| publicação monetizada por Coletivo | `paid_extension` | Gestão ou superior |
| indicadores históricos e de impacto | `paid_extension` | Impacto ou Enterprise |
| API, SSO, Power BI e SLA | `paid_specialized` | Enterprise ou Scale |
| acesso patrocinado de Pessoa ou Coletivo | `sponsor_funded` | prazo e finalidade declarados |
| acesso financiado por Organização | `organization_funded` | financiador sem acesso indevido |

## 4. Registro mínimo

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
  periodic:
    quantity: number | null
    period: week | month | contract | none
    cumulative: false
  concurrent:
    quantity: number | null
  fair_use: boolean
transition_effects:
  - string
risks:
  - string
validation_status: not_started
owner: unassigned
```

## 5. Perguntas obrigatórias

- Qual valor é produzido?
- A capacidade é essencial?
- O gratuito permanece útil sem a ampliação?
- O pago amplia ou apenas desfaz limitação artificial?
- O catálogo público permanece acessível?
- Existem dados ou riscos adicionais?
- Quem paga e quem se beneficia?
- Quem pode cancelar ou contestar?
- O que ocorre no downgrade?
- A perda de acesso pode causar dano?
- Existe alternativa gratuita legítima?
- O plano pago alteraria indevidamente ranking ou relevância?

## 6. Critérios para `universal_free`

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
- prevenção de dano material;
- acesso geral ao catálogo público.

## 7. Critérios para `free_limited`

O limite deverá:

- refletir capacidade, custo ou risco real;
- ser informado antes do uso;
- possuir unidade compreensível;
- não impedir benefício básico;
- não reduzir segurança;
- permitir acompanhamento;
- evitar surpresa ou bloqueio abrupto;
- não reduzir visibilidade de conteúdo já publicado;
- possuir alternativa gratuita;
- possuir tratamento de exceção quando necessário para evitar dano.

## 8. Critérios para `paid_extension`

A capacidade deverá:

- ampliar dimensão legítima;
- possuir valor adicional demonstrável;
- não ser direito básico;
- permitir downgrade;
- informar dados e limites;
- possuir hipótese de pagamento;
- não depender de influência ou urgência artificial;
- não aumentar relevância orgânica;
- manter assinatura e transação separadas.

## 9. Critérios para acesso financiado

Deverão ser registrados:

- financiador;
- beneficiário;
- finalidade;
- duração;
- capacidades financiadas;
- dados acessíveis ao financiador;
- condição de término;
- continuidade no gratuito;
- conflito de interesse;
- proteção contra discriminação.

## 10. Conflitos de classificação

Quando uma capacidade puder pertencer a mais de um estado, prevalecerá:

1. `prohibited_paywall` sobre qualquer classificação paga;
2. `universal_free` sobre conveniência econômica;
3. o limite mais protetivo para dados e autonomia;
4. a classificação que preserve catálogo público e retorno ao gratuito;
5. `not_assessed` quando evidência for insuficiente.

## 11. Revisão de classificação

Mudanças materiais exigirão:

- justificativa;
- comparação antes/depois;
- impacto no gratuito;
- impacto no catálogo público;
- impacto em dados e direitos;
- evidência;
- plano de transição;
- comunicação;
- aprovação formal;
- possibilidade de reversão.

## 12. Estado

`active allocation baseline — candidate commercial capabilities classified; validation and implementation pending`.
