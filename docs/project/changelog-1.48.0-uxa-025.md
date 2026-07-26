---
id: GKR-CHANGELOG-1.48.0
 title: Histórico de Alterações 1.48.0 — Validação do Mapa de Oportunidades
status: active
version: 1.48.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-07-26
related:
  - UXA-024
  - UXA-025
  - GKR-CANON-MATRIX-UXA-025
  - GKR-STATE-001
  - ROADMAP-12.00.0
  - M7.26
normative: false
---

# Histórico de Alterações 1.48.0 — Validação do Mapa de Oportunidades

## 1. Escopo

Este incremento registra a primeira validação funcional e reformulação do wireframe móvel do Mapa de Oportunidades.

## 2. Novo documento

Foi criado:

- `UXA-025 — Validação Funcional e Reformulação do Mapa de Oportunidades`.

O documento conclui que a UXA-024 é funcionalmente válida após reformulação e explicita que a análise não constitui teste de usabilidade, validação cartográfica, design ou desenvolvimento.

## 3. Reformulação gráfica

O arquivo `docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg` foi atualizado para incluir:

- `Agindo como: Minha jornada`;
- `Lista · mesmos filtros`;
- `Pesquisar nesta região`;
- indicação de camadas ativas;
- `Ajustar localização e privacidade`;
- `Por que estou vendo isto?`;
- ação contextual `Ver rota`.

## 4. Contratos consolidados

A validação estabelece que:

- Mapa e Lista formam uma única descoberta;
- busca, filtros, região e seleção devem ser preservados;
- a Lista oferece alternativa equivalente à representação espacial;
- localização exata somente poderá ser temporária e controlada;
- rota externa exige transparência sobre executor e dados;
- proximidade e patrocínio não constituem relevância suficiente;
- conteúdo anterior ao gate permanece geral ou resultante de busca e filtros explícitos;
- localização de participantes e locais sensíveis não será exibida indevidamente.

## 5. Governança atualizada

Foram atualizados:

- visão geral da Arquitetura da Experiência;
- Programa Inicial de Wireframes;
- Registro do Estado Atual;
- Roadmap Arquitetural;
- Painel de Conhecimento;
- Marcos Arquiteturais;
- navegação oficial do portal.

Também foi criado o adendo `GKR-CANON-MATRIX-UXA-025`.

## 6. Novo marco

O incremento estabelece:

> **M7.26 — Mapa de Oportunidades Funcionalmente Validado e Reformulado**

## 7. Limites preservados

Não foram iniciados:

- estados alternativos do Mapa;
- referência do Mapa para computador;
- teste de usabilidade;
- tecnologia cartográfica;
- protótipo navegável;
- design visual;
- Engenharia de Produto;
- reaplicação dos testes dos Resultados Empresariais.
