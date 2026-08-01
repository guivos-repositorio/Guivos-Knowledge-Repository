---
id: GKR-CHANGELOG-1.69.0-UXA-045
title: Histórico 1.69.0 — Validação dos Estados Patrocinados de Lista e Mapa
status: active
version: 1.69.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-01
depends_on:
  - UXA-044
  - UXA-045
related:
  - GKR-STATE-001
  - ROADMAP-12.21.0
  - M7.47
normative: false
---

# Histórico 1.69.0 — Validação dos Estados Patrocinados de Lista e Mapa

## 1. Resumo

Este incremento valida funcionalmente e reformula os quatro wireframes patrocinados de Lista e Mapa do Opportunity Boost.

## 2. Artefatos criados ou atualizados

- UXA-044 elevada para 0.2.0;
- UXA-045 criada;
- Lista patrocinada móvel reformulada;
- Lista patrocinada para computador reformulada;
- Mapa patrocinado móvel reformulado;
- Mapa patrocinado para computador reformulado;
- adendo canônico da UXA-045.

## 3. Lacunas corrigidas

- contagem ambígua entre orgânico e pago;
- preferência publicitária confundida com filtro de negócio;
- percentual de densidade exposto como controle da pessoa;
- efeito da ocultação entre Lista e Mapa pouco explícito;
- marcador selecionado sem vínculo funcional com o cartão;
- movimentação do Mapa sem gate de nova pesquisa.

## 4. Resultado funcional

O conjunto é considerado funcionalmente válido após reformulação.

Agora ficam demonstrados:

- oito oportunidades orgânicas e uma patrocinada exibida no exemplo;
- filtros de oportunidades separados da preferência publicitária;
- ocultação sincronizada sem redução do catálogo orgânico;
- marcador e cartão patrocinados com identificador comum;
- seleção no Mapa sem alteração da ordem da Lista;
- gate `Pesquisar nesta área`;
- movimentação sem consulta automática ou autorização de localização;
- proximidade sem afinidade ou recomendação.

## 5. Estado global proposto

- GKR-STATE-001 1.74.0;
- ROADMAP-12.21.0;
- M7.47 — Estados Patrocinados de Lista e Mapa Funcionalmente Validados e Reformulados;
- Arquitetura da Experiência ativa até UXA-045;
- Engenharia de Produto pausada antes de W0-01.

## 6. Não iniciado

Não foram iniciados gestão de campanha ativa, relatório agregado, algoritmo, tecnologia cartográfica, perfil publicitário, design final, protótipo, teste, campanha real, checkout, cobrança ou Engenharia de Produto.

## 7. Próximo passo

Criar, após integração e nova autorização, os wireframes de gestão da campanha ativa do Opportunity Boost.
