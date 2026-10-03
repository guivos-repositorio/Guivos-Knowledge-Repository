---
id: GEM-007-SHARED-CAPABILITY-AND-COST-BOUNDARIES-001
title: Fronteiras de Capacidades e Custos Compartilhados
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-007
---

# Fronteiras de Capacidades e Custos Compartilhados

## 1. Objetivo

Identificar capacidades transversais e categorias de custo que poderão atender vários produtos, sem definir rateio, centro de custo, transfer pricing, orçamento ou implementação.

## 2. Capacidades compartilhadas candidatas

| Capacidade | Produtos consumidores candidatos | Responsabilidade superior candidata |
|---|---|---|
| autenticação e identidade | todos | Platform Layer futura |
| busca e descoberta | Journey, Mall, Travel, Media, Business | capacidade comum futura |
| notificações | Journey, Mall, Travel, Business, Media | capacidade comum futura |
| billing e pagamentos | produtos econômicos aplicáveis | capacidade comum futura |
| atendimento | todos conforme evento | produto owner + capacidade comum |
| segurança e antifraude | todos | governança e plataforma futuras |
| dados e consentimento | todos | autoridade de dados futura |
| Grafo Global | Journey, Intelligence e consumidores autorizados | Intelligence / arquitetura de dados futura |
| analytics | todos conforme finalidade | Intelligence + produto responsável |
| infraestrutura | todos | Platform/DevOps futuro |
| governança | todos | Guivos Governance |
| marca | todos | autoridade institucional |

## 3. Categorias de custo

### Diretos

- produção específica;
- atendimento de evento;
- comissão ou custo de parceiro futuro;
- entrega;
- aquisição de inventário ou capacidade;
- campanha;
- implantação;
- suporte especializado.

### Compartilhados

- tecnologia;
- segurança;
- dados;
- governança;
- marca;
- atendimento transversal;
- infraestrutura;
- qualidade;
- jurídico e conformidade futuros;
- operações corporativas.

### Custos de risco

- fraude;
- chargeback;
- reembolso;
- indisponibilidade;
- incidente;
- erro de recomendação;
- perda de confiança;
- dependência de parceiro;
- retrabalho.

## 4. Regras

- custo compartilhado não é custo inexistente;
- uso de capacidade não transfere sua autoridade;
- produto líder deverá registrar dependências;
- capacidade crítica deverá possuir plano futuro de continuidade;
- custo direto e custo comum deverão permanecer distinguíveis;
- subsídio deverá ser identificado e governado;
- gratuidade não significa ausência de custo;
- receita de produto não poderá ser analisada sem custos de capacidades utilizadas.

## 5. Contrato conceitual de dependência

```yaml
shared_capability_id: string
name: string
status: candidate
functional_owner: not_defined
consumer_products:
  - string
purpose: string
criticality: not_assessed
data_involved:
  - string
direct_cost_categories:
  - string
shared_cost_categories:
  - string
allocation_defined: false
transfer_pricing_defined: false
continuity_defined: false
substitution_defined: false
```

## 6. Subsídio cruzado

Poderá existir futuramente para sustentar:

- gratuito universal;
- segurança;
- conteúdo;
- suporte;
- Intelligence;
- impacto social;
- infraestrutura;
- experimentação.

Exigirá origem, finalidade, beneficiário, limite, evidência, owner e revisão.

## 7. Dependências do GEM-008

- custos estruturais;
- reservas;
- política de financiamento do gratuito;
- critérios de subsídio;
- resiliência;
- capacidade;
- reinvestimento;
- concentração econômica;
- sustentabilidade.

## 8. Fora do escopo

- valores;
- orçamento;
- rateio;
- centro de custo;
- centro de resultado;
- transfer pricing;
- P&L;
- fornecedores;
- arquitetura técnica;
- operação.
