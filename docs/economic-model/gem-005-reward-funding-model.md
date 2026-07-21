---
id: GEM-005-REWARD-FUNDING-MODEL-001
title: Modelo de Financiamento de Recompensas
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-005
---

# Modelo de Financiamento de Recompensas

## 1. Objetivo

Definir como recompensas econômicas futuras deverão possuir fonte, cobertura, responsabilidade e finalidade identificadas antes da emissão.

## 2. Regra de cobertura

```text
nenhuma recompensa resgatável
→ sem fonte, capacidade ou cobertura identificada
```

Intenção de patrocínio, expectativa de receita ou promessa informal não constitui cobertura confirmada.

## 3. Fontes candidatas

### FF-01 — Orçamento Guivos

Recursos próprios destinados a programa específico.

Requisitos:

- autorização;
- limite futuro;
- owner;
- finalidade;
- monitoramento;
- regra de encerramento.

### FF-02 — Patrocinador

Empresa ou instituição financia campanha, público, causa ou conjunto de recompensas.

Requisitos:

- identificação;
- recurso ou capacidade;
- período;
- finalidade;
- independência da Guivos;
- disclosure;
- tratamento do encerramento.

### FF-03 — Parceiro fornecedor

Parceiro disponibiliza desconto, produto, serviço, experiência, inventário ou capacidade.

Requisitos:

- disponibilidade;
- qualidade;
- responsabilidade;
- valor de referência futuro;
- cancelamento;
- substituição;
- dados necessários para entrega.

### FF-04 — Organização contratante

Empresa ou instituição financia benefícios para pessoas ou grupos elegíveis.

Requisitos:

- beneficiários;
- critérios;
- duração;
- limites de acesso a dados;
- autonomia;
- término e continuidade.

### FF-05 — Fundo social ou recurso vinculado

Recursos destinados exclusivamente a causa, comunidade ou finalidade determinada.

Requisitos:

- segregação;
- destinatários;
- finalidade;
- executor;
- prestação de contas futura;
- vedação de uso livre incompatível.

### FF-06 — Receita futura de campanha

Parcela futura de receita poderá financiar recompensa somente após autorização econômica específica.

Requisitos posteriores:

- evento de receita;
- base de cálculo;
- cobertura;
- timing;
- risco de reversão;
- tratamento contábil e fiscal.

### FF-07 — Benefício não monetário

Capacidade, acesso, conteúdo, serviço ou inventário disponibilizado sem desembolso financeiro direto.

A ausência de desembolso não elimina custo, responsabilidade ou necessidade de controle.

### FF-08 — Modelo híbrido

Combinação transparente de duas ou mais fontes.

Deverá evitar:

- dupla contagem;
- cobrança duplicada;
- responsabilidade indefinida;
- uso cruzado de recurso vinculado;
- promessa acima da cobertura.

## 4. Responsabilidade econômica

Cada programa deverá separar:

- financiador;
- emissor;
- operador futuro;
- fornecedor do benefício;
- responsável pela entrega;
- responsável por cancelamento;
- responsável por reversão;
- responsável pela disputa;
- responsável por cobertura residual.

## 5. Formas de contribuição do parceiro

Além de financiamento em dinheiro, parceiros poderão contribuir futuramente com:

- descontos reais;
- produtos;
- serviços;
- experiências;
- vagas;
- capacidade ociosa;
- acesso;
- infraestrutura;
- bolsas;
- conteúdo;
- transporte;
- alimentação;
- equipamentos;
- matching de recompensas;
- campanhas com orçamento restrito.

## 6. Estados de cobertura

```yaml
funding_status:
  unassessed |
  proposed |
  committed |
  confirmed |
  partially_available |
  exhausted |
  suspended |
  terminated
```

Somente `confirmed`, e futuramente `partially_available` dentro do limite disponível, poderá sustentar emissão resgatável.

## 7. Registro mínimo

```yaml
funding_source_id: string
source_type: string
funder: string
program_id: string
purpose: string
coverage_type:
  monetary |
  non_monetary |
  hybrid
coverage_confirmed: false
restricted: boolean
benefit_supplier: string | null
economic_responsibility: string
start_condition: string
end_condition: string
termination_treatment: string
data_access_limits:
  - string
conflicts:
  - string
status: proposed
```

## 8. Encerramento do financiador

O encerramento deverá tratar:

- novas emissões;
- emissões aprovadas;
- saldos disponíveis;
- reservas;
- resgates em processamento;
- benefícios já concedidos;
- comunicação;
- substituição;
- cobertura residual;
- responsabilidades contratuais futuras.

O financiador não poderá revogar arbitrariamente benefício legitimamente adquirido quando houver cobertura e obrigação já constituídas.

## 9. Conflitos

- patrocinador tenta influenciar evidência;
- parceiro oferece benefício sem disponibilidade;
- recurso vinculado é usado em outra finalidade;
- emissão supera cobertura;
- campanha encerra sem tratamento dos saldos;
- financiador exige dados excessivos;
- desconto não representa benefício real;
- responsabilidade é transferida ao participante;
- recompensa é usada como publicidade não identificada.

## 10. Gate de financiamento

Uma fonte somente poderá sustentar programa futuro quando:

- identidade e autoridade estiverem verificadas;
- cobertura estiver confirmada;
- finalidade estiver documentada;
- responsabilidades estiverem atribuídas;
- dados e disclosures estiverem limitados;
- encerramento estiver previsto;
- conflitos estiverem tratados;
- dependências especializadas estiverem registradas.

## 11. Fora do escopo

- orçamento;
- valores;
- percentuais;
- patrocinadores específicos;
- contratos;
- repasses;
- contabilidade;
- tributação;
- operação de fundos;
- implementação.
