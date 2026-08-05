---
id: GKR-CHANGELOG-1.91.0
title: Changelog 1.91.0 — Validação da Solicitação Pendente Móvel
status: draft
version: 1.91.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-04
related:
  - UXA-066
  - UXA-067
  - GKR-CCM-UXA-067-A1
  - GKR-STATE-001
  - ROADMAP-12.43.0
  - M7.69
normative: false
---

# Changelog 1.91.0 — Validação da Solicitação Pendente Móvel

## Adicionado

- UXA-067 — Validação Funcional e Reformulação da Solicitação Pendente Móvel em Coletivos;
- adendo de consolidação canônica da UXA-067;
- marco M7.69.

## Reformulado

Os oito SVGs da UXA-066 foram reformulados para:

- substituir ações que pareciam alterar estado por verificação explícita;
- orientar correção de dado material sem edição silenciosa;
- limitar a autoridade da análise protegida;
- distinguir cancelamento da solicitação de cancelamento da atividade interna;
- retirar obrigatoriedade implícita do pedido adicional;
- separar resposta, preferência, contestação e cancelamento;
- separar descarte do rascunho e cancelamento da solicitação;
- tornar o efeito do envio adicional compreensível;
- retirar garantias absolutas sobre tratamento de dados;
- evitar promessa de implementação após aprovação;
- impedir simulação de revisão formal inexistente;
- condicionar nova solicitação após expiração à disponibilidade vigente.

## Validado

- aguardando decisão;
- análise protegida;
- informação adicional solicitada;
- revisão da resposta adicional;
- cancelamento pela Pessoa;
- aprovação;
- recusa;
- expiração.

## Cobertura

- Coletivos: 22 SVGs materializados, 22 validados e 0 pendente;
- Opportunity Boost: 46 materializados, 36 validados e 10 pendentes.

## Preservado

- solicitação não é participação;
- pedido adicional não é obrigação de revelar;
- cancelamento, recusa e expiração permanecem eventos distintos;
- denúncia não é revisão;
- apoio institucional não concede autoridade ou dados;
- política jurídica, protótipo, teste e Engenharia de Produto não foram iniciados;
- Resultados Empresariais e baseline comercial não foram alterados.

## Próximo gate

A UXA-068 — Expressão Guiada do Momento Atual por Texto e Voz permanece recomendada e não iniciada.
