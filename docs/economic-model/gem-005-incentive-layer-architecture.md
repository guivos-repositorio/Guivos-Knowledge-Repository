---
id: GEM-005-INCENTIVE-LAYER-ARCHITECTURE-001
title: Arquitetura das Camadas de Incentivo
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Arquitetura das Camadas de Incentivo

## 1. Objetivo

Separar progresso, reconhecimento e recompensa econômica para que cada registro possua significado, evidência, responsabilidade e ciclo de vida próprios.

## 2. Camada I — Progresso

Representa avanço em atividade, jornada, objetivo ou experiência.

Exemplos:

- etapa concluída;
- marco alcançado;
- histórico de participação;
- continuidade voluntária;
- aprendizagem registrada.

Propriedades:

- não possui valor monetário;
- não é transferível;
- não pode ser vendido;
- não cria obrigação financeira;
- não deve depender de gasto;
- não representa valor humano;
- não deve ser apagado por simples inatividade.

## 3. Camada II — Reconhecimento

Representa contribuição ou participação reconhecida em contexto determinado.

Exemplos:

- selo;
- certificado;
- agradecimento;
- credencial verificável;
- reconhecimento comunitário;
- registro de voluntariado.

Propriedades:

- fonte identificada;
- critério documentado;
- contexto explícito;
- evidência proporcional;
- possibilidade de correção;
- não pode ser comprado;
- não constitui reputação universal;
- não cria recompensa econômica automática.

## 4. Camada III — Recompensa econômica

Representa benefício resgatável ou utilidade com responsabilidade econômica ou operacional.

Exemplos:

- pontos resgatáveis;
- desconto;
- voucher;
- produto;
- serviço;
- experiência;
- acesso ampliado;
- benefício patrocinado;
- doação direcionada.

Propriedades:

- fonte de financiamento ou capacidade identificada;
- responsabilidade pela entrega;
- evento elegível;
- regra de emissão;
- validade;
- resgate;
- reversão;
- disputa;
- registro separado das demais camadas.

## 5. Separação canônica

```text
progresso ≠ reconhecimento ≠ recompensa econômica
```

Uma pessoa poderá possuir progresso ou reconhecimento sem receber recompensa econômica.

## 6. Relações permitidas

```text
progresso → pode habilitar reconhecimento
reconhecimento → pode compor elegibilidade futura
recompensa → pode apoiar continuidade
```

Cada relação exige regra explícita. Nenhuma relação representa conversão automática.

## 7. Relações não admissíveis

```text
pagamento → reconhecimento
compra → mérito humano
pontos → valor da pessoa
patrocínio → alteração de evidência
ranking → autoridade universal
```

## 8. Registro canônico

```yaml
incentive_layer_record_id: string
layer:
  progress |
  recognition |
  economic_reward
context: string
subject_or_beneficiary: string
source: string
event_reference: string
evidence_level: string
monetary_value_defined: false
transferable: false
conversion_rule: none_by_default
validity: string | null
appeal_available: true
status: string
```

## 9. Regra de decomposição

Quando um mecanismo possuir mais de uma função, deverá ser decomposto em registros distintos.

Exemplo:

```text
participação voluntária validada
→ registro de participação
→ certificado contextual
→ recompensa patrocinada opcional
```

A retirada ou expiração da recompensa não apaga o histórico legítimo nem o reconhecimento comprovado.

## 10. Riscos controlados

- saldo único representando conceitos incompatíveis;
- aquisição de reconhecimento por pagamento;
- perda de progresso por expiração econômica;
- ranking geral baseado em gasto;
- influência do financiador sobre evidências;
- recompensa tratada como prova de impacto;
- reconhecimento sem contexto;
- dupla contagem entre camadas.

## 11. Fora do escopo

- cálculo de progresso por produto;
- critérios finais de reconhecimento;
- quantidade de pontos;
- conversão entre camadas;
- interfaces;
- implementação técnica.
