---
id: GEM-006-RESPONSIBILITY-REFUND-DISPUTE-MAP-001
title: Mapa de Responsabilidade, Reembolso e Disputa
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-006
---

# Mapa de Responsabilidade, Reembolso e Disputa

## 1. Objetivo

Definir responsabilidades mínimas por oferta, entrega, suporte, garantia, reembolso, chargeback, disputa, evidência e comunicação de incidentes.

## 2. Perguntas obrigatórias

Cada relacionamento deverá esclarecer:

- quem vende;
- quem presta;
- quem entrega;
- quem garante;
- quem atende;
- quem reembolsa;
- quem substitui;
- quem responde por dano;
- quem valida evidências;
- quem mantém registros;
- quem comunica incidentes;
- quem recebe e encaminha a contestação.

## 3. Princípios

```text
visibilidade da Guivos
não elimina responsabilidade do parceiro
```

```text
responsabilidade do parceiro
não elimina deveres próprios da Guivos
```

```text
recebimento do pagamento
não define sozinho responsabilidade por entrega
```

## 4. Tipos de falha

- oferta incorreta;
- indisponibilidade;
- atraso;
- entrega parcial;
- serviço inadequado;
- cancelamento;
- produto defeituoso;
- risco à segurança;
- cobrança divergente;
- desconto inválido;
- recompensa indisponível;
- uso indevido de dados;
- promessa não autorizada;
- fraude;
- falha de integração.

## 5. Tratamentos candidatos

- correção;
- nova entrega;
- substituição;
- reembolso parcial;
- reembolso integral;
- crédito futuro condicionado;
- cancelamento;
- suspensão da oferta;
- suspensão do parceiro;
- investigação;
- encaminhamento especializado.

Nenhum tratamento financeiro final é aprovado neste documento.

## 6. Registro mínimo de disputa

```yaml
dispute_id: string
relationship_id: string
offer_id: string | null
participant_or_actor: string
issue_type: string
responsibility_candidates:
  - string
evidence:
  - string
status: open
interim_protection:
  - string
resolution: null
appeal_available: true
owner: string
```

## 7. Reembolsos e repasses

Antes de ativação futura deverão ser identificados:

- origem do valor;
- destino do valor;
- valor pertencente a terceiro;
- efeito sobre comissão;
- efeito sobre recompensa;
- efeito sobre repasse;
- efeito de chargeback;
- autoridade para decidir;
- prazo futuro aplicável.

## 8. Proteção do participante

A disputa não poderá ser bloqueada por:

- dificuldade artificial de contato;
- transferência indefinida entre Guivos e parceiro;
- exigência desproporcional de evidência;
- perda de acesso a registros próprios;
- cláusula ou comunicação obscura;
- retaliação.

## 9. Fora do escopo

- política jurídica final;
- prazo;
- valor;
- canal operacional;
- sistema de tickets;
- parceiro real.
