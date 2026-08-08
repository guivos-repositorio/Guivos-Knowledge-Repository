---
id: GPA-003
title: Guivos Travel
status: consolidated
version: 1.2.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GLPA-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
---

# Guivos Travel

## Papel

Guivos Travel é o produto responsável por viagens e experiências relacionadas a deslocamento, destinos e turismo dentro do Ecossistema Guivos.

## Escopo principal

- destinos;
- roteiros;
- hospedagens;
- passeios;
- experiências locais;
- parceiros de turismo;
- planejamento de viagens;
- ofertas e jornadas relacionadas a viagens;
- reserva e operação especializada quando pertencentes à Guivos.

## Integração com a experiência

O Journey pode descobrir, recomendar ou contextualizar oportunidades relacionadas a viagem sem que isso transforme a superfície em Guivos Travel.

O registro atual de superfícies e transições não possui uma família canônica dedicada a Travel. Consequentemente:

- não existe ainda `SURF` ou `TRN` canônico de Journey → Travel;
- uma futura mudança para planejamento, roteiro ou reserva sob autoridade Travel deverá ser modelada como handoff interno;
- a passagem só se torna fronteira externa quando a autoridade efetivamente deixa a Guivos e passa para terceiro;
- uma oportunidade de viagem em `PER-203` continua sendo Detalhe de Oportunidade do Journey até que exista mudança material de responsabilidade.

A lacuna está registrada como `SP-GAP-002` na [Matriz de Integração dos Produtos com as Jornadas](specialized-products-journey-integration-matrix.md).

## Limites

Guivos Travel não substitui o Guivos Journey, o Guivos Mall, o Guivos Business, o Guivos Media, o Guivos Intelligence ou o Guivos Ads.

Seu domínio principal é a operação especializada de viagens e experiências turísticas.

Capacidades comuns de identidade, billing, pagamentos, segurança e integrações pertencem à Platform Layer quando compartilhadas.

## Relações principais

- recebe participantes e recomendações originadas no Guivos Journey após handoff adequado;
- pode utilizar recursos comerciais do Guivos Mall sem perder autoridade sobre a lógica de viagem;
- pode atender programas corporativos do Guivos Business;
- utiliza conteúdo do Guivos Media;
- utiliza Guivos Intelligence para personalização e análise dentro dos limites autorizados;
- pode receber campanhas do Guivos Ads.

## Regra de representação

Travel deve ficar perceptível quando a decisão dominante passa a ser planejamento, reserva, roteiro, deslocamento ou operação turística sob sua responsabilidade.

A regra completa está em [Política de Representação e Handoffs entre Produtos](specialized-products-experience-and-handoff-policy.md).

## Estado de integração

A responsabilidade arquitetural do Travel está consolidada. Sua relação com Journey e demais produtos está definida conceitualmente, porém a integração visual/navegacional canônica permanece não materializada.

Este rebaseline não cria fluxo de reserva, nova superfície ou transição.
