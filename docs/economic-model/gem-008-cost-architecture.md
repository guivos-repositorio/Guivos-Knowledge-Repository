---
id: GEM-008-COST-ARCHITECTURE-001
title: Arquitetura de Custos
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Arquitetura de Custos

## 1. Objetivo

Consolidar categorias e comportamentos de custo necessários para analisar sustentabilidade sem estabelecer valores, rateios, centros de custo ou contabilização.

## 2. Categorias

### C-01 — Diretos

Relacionados a entrega, transação, programa ou evento identificável:

- produto ou serviço;
- logística;
- fornecedor;
- benefício ou recompensa;
- atendimento específico;
- implantação;
- produção;
- cancelamento e reembolso.

### C-02 — Estruturais

- equipe;
- tecnologia;
- infraestrutura;
- administração;
- governança;
- operação corporativa;
- marca;
- conhecimento institucional.

### C-03 — Aquisição e distribuição

- mídia;
- vendas;
- canais;
- relacionamento;
- distribuição;
- integração comercial.

### C-04 — Qualidade e confiança

- curadoria;
- verificação;
- moderação;
- suporte;
- contestação;
- privacidade;
- segurança;
- acessibilidade;
- prevenção de fraude.

### C-05 — Risco

- fraude;
- inadimplência;
- chargeback;
- reembolso;
- indisponibilidade;
- incidente;
- responsabilidade;
- compensação;
- perda de confiança.

### C-06 — Coordenação

- negociação;
- integração;
- comunicação;
- disputa;
- reconciliação;
- gestão entre produtos e parceiros.

### C-07 — Oportunidade

Recursos consumidos que deixam de ser aplicados em alternativas potencialmente superiores.

### C-08 — Social e externalidade

- exclusão;
- dano;
- sobrecarga;
- impacto comunitário ou ambiental;
- dependência induzida;
- transferência silenciosa de risco.

## 3. Comportamentos candidatos

- fixo;
- variável;
- semivariável;
- incremental;
- recorrente;
- não recorrente;
- por evento;
- por capacidade;
- por participante;
- por organização;
- por parceiro;
- por território;
- excepcional.

## 4. Regras

- gratuidade não elimina custo;
- custo compartilhado deverá permanecer visível;
- custo de risco não será omitido por não ter ocorrido ainda;
- custo de oportunidade não será tratado como desembolso realizado;
- externalidade material poderá bloquear mecanismo economicamente positivo;
- receita não será analisada sem custos necessários à sua entrega;
- custo candidato não equivale a valor contabilizado;
- ausência de valor mantém o item como hipótese documental.

## 5. Registro conceitual

```yaml
cost_scope_id: string
category: string
behavior: not_assessed
origin: string
beneficiary: string
responsible_scope: string
shared: boolean
risk_related: boolean
amount_defined: false
allocation_defined: false
evidence:
  - string
```

## 6. Fora do escopo

- valores;
- centros de custo;
- plano de contas;
- rateio;
- transfer pricing;
- reconhecimento contábil;
- orçamento.