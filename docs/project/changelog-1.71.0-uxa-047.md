---
id: GKR-CHANGELOG-1.71.0-UXA-047
title: Histórico 1.71.0 — Validação da Gestão da Campanha Ativa
status: active
version: 1.71.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-01
depends_on:
  - UXA-046
  - UXA-047
related:
  - GKR-STATE-001
  - ROADMAP-12.23.0
  - M7.49
normative: false
---

# Histórico 1.71.0 — Validação da Gestão da Campanha Ativa

## 1. Resumo

Este incremento valida funcionalmente e reformula os seis wireframes de gestão da campanha ativa do Opportunity Boost.

## 2. Artefatos criados ou atualizados

- UXA-046 elevada para 0.2.0;
- UXA-047 criada;
- campanha programada reformulada;
- campanha ativa reformulada;
- campanha limitada reformulada;
- campanha pausada reformulada;
- alteração material reformulada;
- encerramento e cancelamento reformulados;
- adendo canônico da UXA-047.

## 3. Lacunas corrigidas

- programação sem gate suficientemente explícito antes do início;
- indicadores operacionais sem período de referência associado;
- limitação ainda próxima de pausa;
- pausa confundida com interrupção financeira definitiva;
- retomada indisponível sem controle visível;
- cancelamento da alteração material ambíguo;
- botão de cancelamento aparentemente executável antes das confirmações;
- estados finais incompletos e misturados ao fluxo voluntário;
- relatório agregado apresentado de forma potencialmente antecipada.

## 4. Resultado funcional

O conjunto é considerado funcionalmente válido após reformulação.

Agora ficam demonstrados:

- início condicionado à permanência dos gates;
- orçamento total, reservado, utilizado e saldo não utilizado separados;
- indicadores operacionais com recorte temporal e atualização;
- campanha limitada ainda ativa, com entrega reduzida;
- limite diário preservado e período sem prorrogação automática;
- pausa interrompendo novos eventos, sem apagar eventos válidos;
- período podendo continuar e expirar durante a pausa;
- retomada bloqueada até resolução e verificação da causa;
- descarte de alteração sem retomada automática;
- cancelamento bloqueado até motivo e confirmações completas;
- suspensão por política distinguida dos demais estados finais;
- registro operacional preservado sem criar relatório agregado;
- saldo e reconciliação mantidos como candidatos.

## 5. Estado global proposto

- GKR-STATE-001 1.76.0;
- ROADMAP-12.23.0;
- M7.49 — Gestão da Campanha Ativa Funcionalmente Validada e Reformulada;
- Arquitetura da Experiência ativa até UXA-047;
- Engenharia de Produto pausada antes de W0-01.

## 6. Não iniciado

Não foram iniciados relatório agregado, estados móveis, algoritmo, perfil publicitário, política final de cancelamento e saldo, design final, protótipo, teste, campanha real, checkout, cobrança ou Engenharia de Produto.

## 7. Próximo passo

Criar, após integração e nova autorização, o wireframe do relatório agregado do Opportunity Boost.
