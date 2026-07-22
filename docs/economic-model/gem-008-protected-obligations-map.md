---
id: GEM-008-PROTECTED-OBLIGATIONS-MAP-001
title: Mapa de Obrigações Protegidas
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Mapa de Obrigações Protegidas

## 1. Objetivo

Identificar compromissos que deverão ser protegidos antes de expansão, reinvestimento discricionário ou utilização de recursos como caixa livre.

## 2. Categorias

### OP-01 — Participantes

- reembolsos;
- disputas;
- cancelamentos;
- dados e portabilidade;
- benefícios legitimamente adquiridos;
- suporte necessário para evitar dano;
- comunicação de incidentes.

### OP-02 — Parceiros e fornecedores

- repasses;
- serviços entregues;
- devoluções;
- disputas;
- encerramento de relacionamento;
- obrigações de dados e confidencialidade futuras.

### OP-03 — Recompensas e benefícios

- emissões cobertas;
- reservas de resgate;
- benefícios em processamento;
- reversões e contestações;
- encerramento do financiador.

### OP-04 — Recursos vinculados

- patrocínios;
- grants;
- fundos sociais;
- campanhas;
- programas organizacionais;
- recursos de finalidade específica.

### OP-05 — Segurança e continuidade

- resposta a incidentes;
- recuperação;
- preservação de dados;
- migração;
- substituição de capacidade crítica;
- encerramento ordenado.

### OP-06 — Especializadas futuras

- obrigações jurídicas;
- fiscais;
- contábeis;
- trabalhistas;
- regulatórias;
- contratuais.

## 3. Estados

```yaml
obligation_status:
  identified |
  pending_definition |
  protected_candidate |
  coverage_required |
  coverage_not_validated |
  at_risk |
  fulfilled |
  closed
```

## 4. Regra central

```text
recurso recebido para obrigação
≠ recurso livre para expansão
```

## 5. Precedência

Obrigações protegidas deverão preceder:

- expansão;
- promoção;
- distribuição futura de resultado;
- reinvestimento discricionário;
- novas emissões de recompensa;
- crescimento sem capacidade.

## 6. Registro conceitual

```yaml
obligation_id: string
category: string
beneficiary: string
responsible_scope: string
source: string | null
restricted: boolean
coverage_validated: false
due_condition: string
closure_condition: string
evidence:
  - string
```

## 7. Fora do escopo

- passivos reconhecidos;
- valores;
- vencimentos reais;
- contratos;
- contabilização;
- execução.