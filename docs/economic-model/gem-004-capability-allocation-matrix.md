---
id: GEM-004-CAPABILITY-ALLOCATION-MATRIX-001
title: Matriz de Alocação de Capacidades
status: active
version: 0.3.0
owner: Guivos Economic Model
last_updated: 2026-08-08
parent: GEM-004
related:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-COMMERCIAL-BASELINE-001
  - M7.39
---

# Matriz de Alocação de Capacidades

## 1. Objetivo

Estabelecer como cada capacidade é classificada entre acesso gratuito, ampliação paga, acesso financiado, acesso de parceiros ou paywall proibido. A versão 0.3.0 sincroniza os exemplos com a taxonomia global de planos sem alterar a natureza das capacidades já governadas.

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
| publicação monetizada por Coletivo | `paid_extension` | Mobiliza ou superior na baseline vigente |
| indicadores históricos e de impacto | `paid_extension` | Impacta ou Rede |
| capacidades institucionais ampliadas | `paid_extension` | Eleva ou Transforma conforme catálogo |
| API, SSO, Power BI e SLA | `paid_specialized` | quando incluídos ou dimensionados em Rede/Transforma; Business depende de autoridade própria |
| acesso patrocinado de Pessoa ou Coletivo | `sponsor_funded` | prazo e finalidade declarados |
| acesso financiado por Organização | `organization_funded` | financiador sem acesso indevido |

A taxonomia `Guivos Business Start · Growth · Scale · Enterprise` não recebe alocação de entitlement nesta versão. Nenhuma capacidade pode ser atribuída a esses planos por analogia com Conecta/Eleva/Transforma.

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

A classificação deve responder qual valor é produzido, se a capacidade é essencial, se o gratuito permanece útil, se o pago amplia valor real, quais dados/riscos surgem, quem paga/beneficia/cancela/contesta, o que ocorre no downgrade, qual alternativa gratuita existe e se o pagamento alteraria indevidamente ranking ou relevância.

## 6. Critérios de proteção

`prohibited_paywall` prevalece sobre classificação paga; `universal_free` prevalece sobre conveniência econômica; dados/autonomia usam o limite mais protetivo; catálogo público e retorno ao gratuito são preservados; evidência insuficiente resulta em `not_assessed`.

Limites gratuitos devem refletir capacidade/custo/risco real, ser informados antes do uso e não bloquear segurança ou benefício básico. Extensões pagas precisam possuir valor adicional demonstrável, permitir downgrade e não depender de influência, urgência artificial ou compra de relevância.

## 7. Acesso financiado

Devem ser registrados financiador, beneficiário, finalidade, duração, capacidades financiadas, dados acessíveis, condição de término, continuidade no gratuito, conflitos de interesse e proteção contra discriminação.

## 8. Revisão de classificação

Mudanças materiais exigem justificativa, comparação antes/depois, impacto no gratuito/catálogo/dados/direitos, evidência, plano de transição, comunicação, aprovação e possibilidade de reversão.

## 9. Regra taxonômica

Plano indica profundidade, capacidade ou complexidade atendida, nunca valor do participante. `Organização Transforma ≠ Guivos Business Enterprise`, e nenhuma equivalência automática de entitlement é permitida entre planos de Organização e Guivos Business.

## 10. Estado

`active allocation baseline — taxonomy synchronized; candidate participant capabilities classified; Guivos Business entitlements not assessed`.
