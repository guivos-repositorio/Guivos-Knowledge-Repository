---
id: GKR-CANON-MATRIX-UXA-033
title: Adendo à Matriz de Consolidação Canônica — Validação da Referência Desktop do Mapa
status: active
version: 0.1.0
owner: Guivos
last_updated: 2026-07-27
depends_on:
  - GKR-STATE-001
  - UXA-032
  - UXA-033
related:
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
  - UXA-031
  - ROADMAP-12.8.0
  - M7.34
normative: true
---

# Adendo à Matriz de Consolidação Canônica — Validação da Referência Desktop do Mapa

## 1. Finalidade

Este adendo registra a consolidação canônica da validação funcional especializada da referência do Mapa de Oportunidades para computador.

## 2. Decisão consolidada

| Dimensão | Decisão canônica |
|---|---|
| Estado | funcionalmente válida após reformulação |
| Posição | superfície recorrente `Mapa`; não integra a primeira entrada obrigatória |
| Paridade | disposição pode variar; significado permanece equivalente ao canal móvel |
| Consulta | filtros, Mapa, Lista e seleção utilizam a mesma região, busca, filtros e atualização |
| Filtros | resumo e controles detalhados devem ser semanticamente idênticos |
| Disposição | visão dividida é o estado padrão em tela ampla |
| Foco | `Focar no Mapa` e `Focar na Lista` preservam consulta, seleção e permissões |
| Retorno | estados concentrados oferecem `Voltar à visão dividida` |
| Movimento | mover o Mapa não executa nova consulta; `Pesquisar nesta área` é condicional |
| Seleção | marcador, cartão e painel contextual usam o mesmo vínculo textual |
| Lista | cartões visíveis apresentam comparação, origem, explicação e relação comercial |
| Painel contextual | recolhível; não substitui o Detalhe nem elimina a comparação |
| Estado zero | diagnóstico no Mapa e Lista; recuperação concentrada em `Consulta e filtros` |
| Localização | opcional; região manual não equivale a posição pessoal |
| Relação comercial | separada da origem funcional, ordenação e seleção |
| Resiliência | Lista, filtros e diagnóstico permanecem operáveis sem mapa carregado |

## 3. Riscos corrigidos

A validação corrigiu:

1. contradição entre filtros resumidos e valores detalhados;
2. ambiguidade das ações `Ampliar Mapa` e `Ampliar Lista`;
3. `Pesquisar nesta área` sem estado de movimento pendente;
4. vínculo insuficiente entre marcador, cartão e painel selecionado;
5. cartões secundários sem origem e explicação consistentes;
6. painel selecionado sem condição de recolhimento;
7. repetição concorrente das ações de recuperação no estado zero.

## 4. Reformulações incorporadas

A UXA-032 passa a demonstrar:

- versão 0.2.0 e estado ativo;
- faixa `Consulta territorial ativa`;
- filtros com valores idênticos em resumo e detalhe;
- `Visão dividida ativa`;
- `Focar no Mapa` e `Focar na Lista`;
- regra `Voltar à visão dividida`;
- `Área atual · resultados atualizados`;
- condição explícita para `Pesquisar nesta área`;
- `Marcador 1 · selecionada`;
- cartões comparáveis com `Por que aparece aqui?`;
- `Entender ordenação`;
- relação comercial rotulada;
- painel contextual recolhível;
- recuperação concentrada no painel de consulta;
- seleção anterior explicável no total zero.

## 5. Proteções preservadas

- mais espaço visual não autoriza mais coleta;
- localização não é ativada automaticamente;
- região manual não é tratada como residência;
- foco não altera consulta ou permissões;
- movimento do Mapa não atualiza resultados silenciosamente;
- seleção não altera relevância ou ordenação;
- relação comercial não é confundida com relevância funcional;
- publicidade não preenche o estado zero;
- endereço protegido não é revelado;
- personalização continua dependente de gate;
- acessibilidade funcional não equivale a conformidade técnica concluída.

## 6. Limites

Este adendo não define pontos de quebra, tablet, tecnologia cartográfica, algoritmo, cobertura real, design, protótipo, teste com usuários, acessibilidade técnica ou desenvolvimento.

## 7. Marco

A integração deste incremento estabelece o marco **M7.34 — Referência do Mapa para Computador Funcionalmente Validada e Reformulada**.
