---
id: GKR-UX-PLANS-BUSINESS-CONFIGURATOR-001
title: Planos — Guivos Business — Configurador e Calculadora Self-service — Documento Mestre
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
depends_on:
  - GKR-PLANS-BUSINESS-001
  - GPA-004-FUNCTIONAL-PORTFOLIO-001
  - GEM-004-A1
  - GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001
---

# Planos — Guivos Business — Configurador e Calculadora Self-service — Documento Mestre

## 1. Finalidade

Definir a experiência pela qual uma empresa pode **compreender, configurar, estimar quando houver autoridade de preço e contratar online** o Guivos Business.

O configurador é uma experiência de composição. Ele não é um quinto plano.

## 2. Planos-base

| Plano | Mensal | Anual | Direção |
|---|---:|---:|---|
| **Start** | R$ 299,00 | R$ 2.990,00 | operar |
| **Growth** | R$ 799,00 | R$ 7.990,00 | acompanhar e compreender |
| **Scale** | a partir de R$ 1.990,00 | dimensionado | interpretar e integrar em escala |
| **Enterprise** | sob consulta | sob consulta | governar alta complexidade e escala |

Todos admitem seleção Mensal ou Anual. Quando o valor não estiver numericamente congelado, a calculadora não deve inventá-lo.

## 3. Dados de preenchimento

A composição deve conseguir receber, conforme aplicável:

### Empresa e escala

- população total da empresa;
- população elegível para a configuração;
- quantidade prevista de participantes;
- quantidade de acessos Journey custeados;
- quantidade de unidades/filiais, quando relevante.

### Oferta

- Programas de Incentivo;
- Guivos Journey custeado;
- ambas.

### Capacidades

- profundidade de Intelligence;
- integrações;
- API/exportações;
- governança;
- necessidades de segurança e controle;
- nível de serviço;
- implementação/operação: Self-service, apoio do suporte ou gerenciado.

### Periodicidade

- mensal;
- anual.

### Recursos operacionais

- orçamento pré-pago de incentivo, quando aplicável.

## 4. Modelo de composição

```text
ASSINATURA RECORRENTE / CONTRATUAL
=
PLANO-BASE
+ COMPONENTE DE POPULAÇÃO / ESCALA
+ COMPONENTE DE OFERTA
+ ACESSOS JOURNEY CUSTEADOS
+ CAPACIDADES ADICIONAIS
+ SERVIÇOS ADICIONAIS

RECURSO OPERACIONAL SEPARADO
=
ORÇAMENTO PRÉ-PAGO DE INCENTIVO
```

O orçamento de incentivo deve ser exibido separadamente e nunca mascarado como assinatura.

## 5. Regra da calculadora

A calculadora deve trabalhar com uma tabela econômica versionada e não com números hardcoded pela interface.

```text
BASE(periodicidade, plano)
+
POPULATION_RATE(periodicidade, faixa_autorizada) × base_precificável
+
OFFER_RATE(periodicidade, oferta_autorizada)
+
JOURNEY_ACCESS_RATE(periodicidade) × acessos
+
ADDONS(periodicidade)
+
SERVICE_RATE(periodicidade, modelo_operacional)
=
VALOR RECORRENTE CALCULÁVEL
```

Cada termo só pode produzir número quando houver autoridade econômica correspondente.

## 6. Preço por população

O modelo usa as faixas e tarifas populacionais adjudicadas em `GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001`.

A calculadora deve aplicar cobrança progressiva por faixa e exibir separadamente cada parcela. Acima de 20.000 elegíveis ou quando Scale/Enterprise exigir dimensionamento, deve exibir o componente como dimensionado em vez de inventar valor.

## 7. Produtos e ofertas

O configurador deve mostrar separadamente o impacto econômico de Programas de Incentivo, Journey custeado e combinação de ambos.

As taxas de Programas de Incentivo, Journey custeado e composição conjunta são governadas pela autoridade econômica vigente. Itens futuros não formalizados continuam sem cifra.

## 8. Resultado

Quando todos os componentes necessários possuírem preço vigente, o resultado deve mostrar plano-base, população/escala, oferta(s), acessos Journey, adicionais, serviços, subtotal recorrente, periodicidade, total recorrente, orçamento de incentivo em linha separada e itens sob consulta.

## 9. Configuração parcialmente calculável

Uma composição pode ser parcialmente calculável.

```text
START ANUAL
→ R$ 2.990,00

POPULAÇÃO
→ PREÇO VARIÁVEL AINDA NÃO ADJUDICADO

JOURNEY CUSTEADO
→ PREÇO POR ACESSO AINDA NÃO ADJUDICADO

TOTAL FINAL
→ NÃO CALCULAR POR INFERÊNCIA
```

A interface pode mostrar a parcela conhecida e indicar claramente o que falta para o total.

## 10. Enquadramento de plano

O plano compatível deve ser determinado pela maior capacidade exigida pela configuração e pelos entitlements vigentes.

A calculadora não pode elevar plano com base apenas em maximização de receita.

## 11. Self-service

Self-service significa que a empresa consegue preencher, compreender, comparar, revisar, calcular quando possível, contratar online quando a composição estiver comercialmente apta e seguir para configuração/operação com autonomia quando elegível.

Suporte e Gerenciado continuam sendo modelos de implementação/operação, não novos planos.

## 12. Estados

- composição vazia;
- composição em preenchimento;
- composição válida;
- preço total calculável;
- preço parcialmente calculável;
- item sob consulta;
- plano incompatível com capacidade solicitada;
- revisão antes de contratação;
- erro recuperável.

## 13. Autonomia e transparência

A superfície deve explicar **por que** um componente altera o valor. Não deve esconder taxa variável dentro de um total opaco.

## 14. Critérios de aceite

O configurador é aceitável quando Start/Growth/Scale/Enterprise permanecem intactos; Mensal/Anual é selecionável; população e ofertas podem compor a contratação; valores variáveis dependem de autoridade; orçamento de incentivo fica separado; total não é inventado; Self-service não vira plano; Organização não é confundida com Business; Design mantém liberdade criativa; e Product Engineering não é liberado por este Master.

## 15. Autoridade econômica corrente

A tabela econômica corrente é `GEM-004-BUSINESS-VARIABLE-PRICING-AUTHORITY-001`, que governa faixas populacionais, ofertas, acessos Journey, add-ons, serviços e regra anual dos componentes tabelados. O configurador deve também consumir a matriz de inclusões por tier para impedir dupla cobrança.

```text
ECONOMIC AUTHORITY
→ ADJUDICATED / NORMATIVE

FULL NUMERIC CONFIGURATOR
→ ECONOMICALLY SPECIFIABLE

IMPLEMENTATION
→ NOT RELEASED

PUBLIC OFFER / CHARGING
→ NOT AUTHORIZED
```
