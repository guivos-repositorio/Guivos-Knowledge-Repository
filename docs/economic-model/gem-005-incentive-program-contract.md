---
id: GEM-005-INCENTIVE-PROGRAM-CONTRACT-001
title: Contrato Canônico de Programa de Incentivo
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Contrato Canônico de Programa de Incentivo

## 1. Objetivo

Estabelecer a estrutura mínima para registrar programas futuros de forma comparável, rastreável e subordinada aos guardrails econômicos, ao baseline gratuito e à proteção comportamental.

## 2. Natureza

O contrato é conceitual. Não é API, ledger, carteira, regulamento promocional, contrato comercial, regra fiscal, modelo contábil ou autorização de emissão e resgate.

## 3. Estrutura

```yaml
incentive_program_id: string
name: string
status:
  candidate |
  conceptually_defined |
  validation_required |
  approved_for_test |
  suspended |
  retired

purpose:
  desired_behavior: string
  expected_value: string
  prohibited_outcomes:
    - string

participants:
  eligible_actors:
    - string
  excluded_or_protected_groups:
    - string
  participation_voluntary: true

incentive:
  layer:
    progress |
    recognition |
    economic_reward
  family_id: string
  reward_type: string
  monetary_value_defined: false
  transferable: false
  cash_convertible: false
  tradable: false

earning:
  eligible_events:
    - string
  evidence_required:
    - string
  evidence_level: string
  limits:
    - string
  duplicate_control: string

funding:
  source_type: string | null
  funder: string | null
  coverage_confirmed: false
  economic_responsibility: string | null
  restricted_purpose: string | null
  termination_treatment: string

lifecycle:
  eligibility: string
  verification: string
  issuance: string
  availability: string
  expiration: string | null
  reservation: string | null
  redemption: string | null
  reversal: string
  dispute: string

benefit:
  supplier: string | null
  availability_status: not_assessed
  delivery_responsibility: string | null
  substitution_rule: string | null
  cancellation_rule: string | null

governance:
  data_involved:
    - string
  fraud_risks:
    - string
  behavioral_risks:
    - string
  conflicts:
    - string
  disclosures:
    - string
  appeal_available: true
  interruption_conditions:
    - string

validation:
  value_status: not_started
  behavioral_status: not_started
  funding_status: not_started
  operational_status: not_started
  legal_status: not_started
  fiscal_status: not_started
  accounting_status: not_started
  labor_status: not_started
  regulatory_status: not_started
```

## 4. Campos obrigatórios

Não poderão ser omitidos:

- propósito e comportamento desejado;
- resultados proibidos;
- atores elegíveis e grupos protegidos;
- camada e família;
- natureza do benefício;
- evento e evidência;
- controle de duplicidade;
- financiador e cobertura, quando econômicos;
- responsabilidade pela entrega;
- ciclo de vida;
- validade, resgate, reversão e disputa;
- dados;
- riscos comportamentais e de fraude;
- disclosures;
- contestação;
- condições de interrupção;
- dependências especializadas.

## 5. Regras de status

### Candidate

Hipótese registrada sem avaliação suficiente.

### Conceptually defined

Programa compatível com o GEM-005 em nível documental.

### Validation required

Depende de evidência de valor, comportamento, financiamento, operação ou análise especializada.

### Approved for test

Estado futuro que exigirá aprovação separada, protocolo, owner, limite, público, cobertura confirmada e critérios de parada.

### Suspended

Interrompido por risco, incidente, fraude, dano, conflito, indisponibilidade, cobertura insuficiente ou evidência inadequada.

### Retired

Encerrado ou substituído por decisão futura.

## 6. Condições de interrupção

- recompensa econômica sem cobertura;
- regras não compreensíveis;
- pontos tratados como dinheiro ou mérito;
- compra de reconhecimento;
- pressão comportamental incompatível;
- impacto desproporcional em grupo protegido;
- evidência insuficiente para o risco;
- duplicidade material;
- parceiro não entrega;
- saldo inconsistente;
- uso de dados incompatível;
- contestação indisponível;
- reversão arbitrária;
- dependência especializada não atendida;
- risco não controlado.

## 7. Rastreabilidade

Cada programa futuro deverá apontar para:

- família IF;
- camada correspondente;
- fluxo de valor VF;
- família de receita RF relacionada, quando existir;
- arquétipo de acesso AM relacionado;
- evento elegível;
- fonte de evidência;
- fonte de financiamento;
- benefício;
- políticas de validade e reversão;
- riscos;
- gates;
- decisões e versões.

## 8. Separação de registros

Quando um programa combinar progresso, reconhecimento e recompensa, deverá possuir registros distintos para cada camada.

## 9. Regra de precedência

Quando houver conflito entre o programa e propósito, dignidade, baseline gratuito, autonomia, privacidade, segurança, acessibilidade, autoridade humana ou política de proteção comportamental, prevalece o limite mais protetivo.

## 10. Fora do escopo

- instâncias operacionais;
- parâmetros quantitativos;
- valores;
- contratos;
- configurações técnicas;
- execução.
