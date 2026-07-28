---
id: GEM-010-A1
title: Premissas de Precificação e Validação Comercial
status: active
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-28
parent: GEM-010
depends_on:
  - GEM-004-A1
  - GEM-004-A2
  - GEM-009
  - GEM-010
related:
  - GEM-COMMERCIAL-BASELINE-001
  - M7.39
normative: true
---

# Premissas de Precificação e Validação Comercial

## 1. Finalidade

Este documento registra os preços candidatos como premissas rastreáveis do modelo financeiro e define como deverão ser validados antes de planejamento aprovado ou oferta pública.

Preço candidato não é preço comprovado, receita, margem, caixa, disposição a pagar ou autorização de cobrança.

## 2. Tabela de parâmetros candidatos

### Pessoas

| Plano | Mensal | Anual | Estado |
|---|---:|---:|---|
| Guivos Free | R$ 0,00 | R$ 0,00 | baseline gratuito |
| Guivos Plus | R$ 24,90 | R$ 249,00 | candidato para validação |
| Guivos Pro | R$ 49,90 | R$ 499,00 | candidato para validação |

### Coletivos

| Plano | Mensal | Anual | Estado |
|---|---:|---:|---|
| Coletivo Livre | R$ 0,00 | R$ 0,00 | baseline gratuito limitado |
| Coletivo Gestão | R$ 89,90 | R$ 899,00 | candidato para validação |
| Coletivo Impacto | R$ 249,90 | R$ 2.499,00 | candidato para validação |
| Coletivo Enterprise | sob consulta | contrato anual | dimensionamento obrigatório |

### Organizações

| Plano | Mensal | Anual | Estado |
|---|---:|---:|---|
| Guivos Business Start | R$ 299,00 | R$ 2.990,00 | candidato para validação |
| Guivos Business Growth | R$ 799,00 | R$ 7.990,00 | candidato para validação |
| Guivos Business Scale | a partir de R$ 1.990,00 | contrato anual | dimensionamento obrigatório |

## 3. Premissas comerciais

- os valores estão denominados em BRL;
- o Brasil é o mercado inicial de referência;
- o plano mensal é recorrente;
- o plano anual é antecipado;
- o preço anual equivale aproximadamente a dez mensalidades;
- o desconto anual candidato não poderá ser apresentado como economia garantida quando condições mudarem;
- Enterprise e Scale exigem proposta, capacidade e contrato;
- acesso financiado possui preço contratual separado do beneficiário;
- comissão, taxa do meio de pagamento, impostos e repasses não estão incluídos nesta tabela;
- não existe trial com conversão automática na baseline inicial;
- preços internacionais exigirão poder de compra, tributos, moeda, meios de pagamento e estratégia local próprios.

## 4. Natureza das premissas

| Parâmetro | Classificação | Evidência atual |
|---|---|---|
| preços mensais e anuais | hipótese aprovada para teste | decisão de arquitetura comercial |
| desconto anual | hipótese | comparação com dez mensalidades |
| cotas de Pessoas | hipótese de utilidade e conversão | não testada |
| cotas de Coletivos | hipótese de capacidade e valor | não testada |
| cotas de Organizações | hipótese de segmentação | não testada |
| demanda por Enterprise ou Scale | hipótese | não testada |
| disposição a pagar | desconhecida | pesquisa pendente |
| taxa de conversão | desconhecida | instrumentação pendente |
| custos de servir | desconhecidos | modelagem pendente |
| margem de contribuição | desconhecida | custos e tributos pendentes |
| retenção e churn | desconhecidos | operação inexistente |

## 5. Drivers obrigatórios de custo

### Pessoas

- processamento e inteligência;
- armazenamento de histórico não essencial;
- notificações e alertas;
- integrações;
- suporte;
- pagamentos;
- segurança e privacidade;
- prevenção de abuso.

### Coletivos

- número de membros;
- administradores;
- atividades e oportunidades;
- inscrições;
- transações;
- armazenamento;
- mensagens e notificações;
- indicadores e relatórios;
- integrações;
- suporte e moderação;
- risco de fraude, disputa e reembolso.

### Organizações

- administradores e usuários financiados;
- unidades;
- oportunidades e programas;
- Coletivos relacionados;
- processamento analítico;
- exportações e Power BI;
- API e SSO;
- implantação;
- SLA;
- suporte dedicado;
- segurança, auditoria e conformidade.

## 6. Faixas candidatas para pesquisa

As faixas abaixo servem somente para pesquisa de sensibilidade e não criam novos preços aprovados.

| Plano | Faixa inferior | Baseline | Faixa superior |
|---|---:|---:|---:|
| Guivos Plus | R$ 19,90 | R$ 24,90 | R$ 29,90 |
| Guivos Pro | R$ 39,90 | R$ 49,90 | R$ 59,90 |
| Coletivo Gestão | R$ 69,90 | R$ 89,90 | R$ 119,90 |
| Coletivo Impacto | R$ 199,90 | R$ 249,90 | R$ 349,90 |
| Business Start | R$ 249,00 | R$ 299,00 | R$ 399,00 |
| Business Growth | R$ 649,00 | R$ 799,00 | R$ 999,00 |

Enterprise e Scale deverão ser pesquisados por composição de valor, capacidade e contrato, não por um único preço de prateleira.

## 7. Perguntas de validação

### Pessoas

- o gratuito entrega valor suficiente antes da oferta?
- duas correspondências personalizadas por semana permitem benefício real?
- a pessoa compreende que o catálogo público continua disponível?
- Plus e Pro possuem diferenciação reconhecível?
- quais capacidades motivam pagamento sem pressão?
- o preço é aceitável para uso recorrente?

### Coletivos

- uma atividade e uma oportunidade mensais tornam o Livre útil?
- quatro atividades e quatro oportunidades justificam o Gestão?
- seis publicações ativas são suficientes para pequena operação?
- quinze atividades e quinze oportunidades segmentam adequadamente o Impacto?
- monetização, pagamentos, indicadores e integrações justificam assinatura?
- quais Coletivos precisam de acesso patrocinado?

### Organizações

- Start atende operação inicial real?
- Growth oferece ganho operacional e analítico claro?
- cotas por mês e publicações ativas refletem uso institucional?
- Power BI, API, SSO, unidades e SLA justificam Scale?
- o comprador prefere preço por plano, unidade, usuário, programa ou capacidade?

## 8. Métricas necessárias

- ativação do gratuito;
- utilidade percebida;
- frequência de uso;
- consumo das cotas;
- incidência de limite atingido;
- escolha da alternativa gratuita;
- abertura de comparação;
- intenção declarada;
- início de checkout;
- conversão;
- ativação das capacidades pagas;
- retenção;
- downgrade;
- cancelamento;
- churn involuntário;
- custo de servir;
- margem de contribuição;
- tickets e reclamações;
- disputas e reembolsos;
- satisfação após compra;
- acesso financiado concedido e encerrado.

## 9. Unit economics mínimos

Para cada plano deverão existir, quando houver dados:

```text
receita líquida por plano
− tributos
− taxas de pagamento
− custos variáveis de processamento
− suporte variável
− perdas, reembolsos e chargebacks
= margem de contribuição
```

Também deverão ser medidos:

- CAC por segmento e canal;
- custo de ativação;
- custo mensal de servir;
- receita média por conta;
- retenção;
- churn;
- LTV com premissas declaradas;
- payback;
- utilização das capacidades;
- subsídio do gratuito;
- concentração de receita.

Nenhuma média poderá ocultar segmentos com custo ou risco materialmente diferente.

## 10. Gates de avanço

Uma oferta somente poderá avançar para teste quando:

1. o gratuito passar no teste de utilidade real;
2. capacidades e limites estiverem implementáveis;
3. custo de servir possuir estimativa rastreável;
4. fluxo de cobrança e cancelamento estiver definido;
5. proteção de dados e segurança estiverem revisadas;
6. implicações jurídicas, fiscais e contábeis forem avaliadas;
7. suporte e disputa possuírem owner;
8. protocolo de teste definir população, duração, métricas e parada;
9. nenhuma oportunidade pública essencial for ocultada;
10. nenhuma publicação existente perder visibilidade para pressionar upgrade.

## 11. Critérios de parada ou revisão

O teste deverá ser interrompido ou revisto quando houver:

- gratuito sem utilidade real;
- confusão recorrente entre catálogo público e personalização paga;
- reclamação material sobre conteúdo desfocado;
- conversão associada a pressão, medo ou vulnerabilidade;
- custo de servir incompatível com preço;
- margem persistentemente inadequada;
- uso muito abaixo da capacidade contratada;
- cancelamento ou disputa acima do aceitável;
- Coletivos sociais excluídos sem alternativa financiada;
- Organizações recebendo dados ou autoridade indevidos;
- incapacidade operacional de cumprir SLA ou compromissos.

Thresholds numéricos deverão ser aprovados em protocolo futuro.

## 12. Cenários financeiros futuros

O modelo deverá comparar, no mínimo:

- cenário conservador;
- cenário-base;
- cenário de maior adoção;
- sensibilidade de preço;
- sensibilidade de conversão;
- sensibilidade de churn;
- custo crescente de inteligência;
- subsídio do gratuito;
- acesso patrocinado;
- mix mensal e anual;
- mix entre Pessoas, Coletivos e Organizações;
- Enterprise e Scale contratados;
- falha de pagamento e reembolso.

## 13. Limites

Este documento não aprova:

- previsão de receita;
- orçamento;
- meta de conversão;
- margem;
- valuation;
- tributo;
- política contábil;
- comissão;
- gateway;
- contrato;
- oferta pública;
- implementação.
