---
id: GEM-008-SHARED-COST-BOUNDARIES-001
title: Fronteiras de Custos Compartilhados
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Fronteiras de Custos Compartilhados

## 1. Objetivo

Definir como capacidades e custos comuns deverão permanecer visíveis entre produtos sem antecipar rateios, transfer pricing ou centros de custo.

## 2. Capacidades candidatas

| Capacidade | Consumidores candidatos | Risco de omissão |
|---|---|---|
| identidade e autenticação | todos | produto parece mais eficiente do que é |
| dados e consentimento | todos | risco e conformidade ficam invisíveis |
| segurança e antifraude | todos | custo de proteção não é considerado |
| infraestrutura | todos | dependência técnica é ignorada |
| notificações | Journey, Mall, Travel, Business e Media | custo de comunicação é deslocado |
| atendimento | todos conforme evento | responsabilidade difusa |
| busca e descoberta | Journey, Mall, Travel, Media e Business | custo de distribuição omitido |
| Intelligence e analytics | consumidores autorizados | capacidade transversal apropriada indevidamente |
| governança e marca | todos | custo institucional não observado |
| billing futuro | produtos econômicos aplicáveis | custo transacional omitido |

## 3. Regras

- custo compartilhado não é custo inexistente;
- uso de capacidade não transfere autoridade funcional;
- produto líder deverá registrar dependências utilizadas;
- custos diretos e comuns deverão permanecer distinguíveis;
- subsídio e compartilhamento deverão ser identificados;
- capacidade crítica deverá possuir tratamento de continuidade;
- receita local não poderá ser avaliada ignorando capacidades comuns;
- rateio indefinido não autoriza alocação arbitrária;
- dupla contagem de custo também deverá ser evitada.

## 4. Contrato conceitual

```yaml
shared_cost_boundary_id: string
capability_id: string
functional_owner: not_defined
consumer_scopes:
  - string
purpose: string
criticality: not_assessed
cost_categories:
  - string
allocation_defined: false
transfer_pricing_defined: false
continuity_defined: false
substitution_defined: false
```

## 5. Questões futuras

- qual capacidade é essencial?
- quais produtos dependem dela?
- quais custos são incrementais ou estruturais?
- existe alternativa?
- a concentração é aceitável?
- como evitar incentivo local incompatível com o ecossistema?

## 6. Fora do escopo

- método de rateio;
- valores;
- centros de custo;
- contratos internos;
- arquitetura técnica;
- orçamento;
- implementação.