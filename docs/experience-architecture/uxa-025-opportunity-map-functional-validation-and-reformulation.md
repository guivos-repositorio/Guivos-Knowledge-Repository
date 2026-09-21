---
id: UXA-025
title: Contrato Funcional Corrente do Mapa de Oportunidades
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-000
depends_on:
  - UXA-004
  - UXA-009
  - UXA-010
  - UXA-012
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-201
  - GKR-SURF-PER-202
  - GKR-SURF-PER-203
  - UXA-029
  - UXA-098
normative: true
---

# Contrato Funcional Corrente do Mapa de Oportunidades

## 1. Finalidade

Governar `GKR-SURF-PER-201 — Mapa de Oportunidades` como responsabilidade recorrente de descoberta territorial, sem impor tecnologia cartográfica, composição visual ou canal específico.

## 2. Princípios

- localização do dispositivo é opcional;
- região manual é permitida e não equivale a residência ou posição atual;
- busca, região, filtros e seleção formam uma única consulta compreensível;
- Mapa e Lista são modos da mesma descoberta territorial;
- pagamento não altera relevância funcional;
- ausência de resultados não justifica ampliação silenciosa de critérios;
- abrir uma oportunidade não confirma interesse, inscrição, compra ou evolução.

## 3. Contexto territorial

A superfície deve tornar explícito, quando aplicável:

- região ou área consultada;
- origem da região;
- estado de localização autorizado ou não autorizado;
- busca vigente;
- filtros vigentes;
- quantidade de resultados orgânicos quando conhecida;
- seleção corrente.

Nenhuma posição pessoal deve ser presumida quando a localização estiver desativada.

## 4. Busca e atualização territorial

A Pessoa pode alterar conscientemente região, busca e filtros.

Mover ou alterar a área de interesse não deve substituir silenciosamente a consulta sem sinal claro de atualização.

A ação equivalente a “pesquisar nesta área” deve preservar autonomia sobre quando recalcular resultados territoriais.

## 5. Mapa ↔ Lista

```text
PER-201 MAPA
↔
PER-202 LISTA
```

A alternância preserva, quando aplicável:

- região;
- busca;
- filtros;
- seleção;
- identidade das oportunidades;
- contexto de retorno.

A Lista é governada por `UXA-029`.

## 6. Localização e privacidade

A localização pode ser:

- não autorizada;
- temporariamente autorizada;
- aproximada;
- substituída por região manual.

Autorização para localização não implica autorização para histórico territorial, publicidade baseada em trajetória ou rastreamento contínuo.

Rota, quando aplicável, pode solicitar origem separadamente.

## 7. Estado sem resultados

Zero resultados é um estado legítimo da consulta atual.

Ele deve permitir compreender:

- região;
- busca;
- filtros;
- cobertura conhecida quando houver evidência;
- possibilidades de revisão.

A recuperação pode envolver editar região, busca ou filtros. Nenhuma recuperação amplia critérios automaticamente.

## 8. Oportunidade selecionada

Uma seleção territorial pode apresentar contexto suficiente para decidir abrir o Detalhe, preservando distinção entre:

- informação funcional;
- relação comercial;
- conteúdo patrocinado identificado;
- ação de salvar quando autorizada.

A continuidade para `PER-203` é governada pelas transições correntes.

## 9. Acessibilidade e resiliência

A solução de Design deve permitir uso funcional sem depender exclusivamente de representação cartográfica.

Lista, baixa conectividade ou indisponibilidade do mapa não devem eliminar acesso ao catálogo territorial quando os dados necessários estiverem disponíveis.

## 10. Estado

```text
PER-201
→ FUNCTIONALLY VALIDATED

CHANNEL
→ DESIGN-OWNED / MULTICHANNEL

VISUAL BASELINE
→ NONE REQUIRED

MAP ↔ LIST
→ SAME TERRITORIAL QUERY
```
