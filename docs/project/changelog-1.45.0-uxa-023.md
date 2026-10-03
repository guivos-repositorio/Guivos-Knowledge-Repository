---
id: GKR-CHANGELOG-1.45.0
title: Histórico de Alterações 1.45.0 — Validação do Início Protegido da Jornada
status: historical
version: 1.45.0
owner: Guivos
last_updated: 2026-07-26
related:
  - GKR-STATE-001
  - ROADMAP-11.98.0
  - UXA-000
  - UXA-011-A1
  - UXA-020
  - UXA-023
  - GKR-CANON-MATRIX-UXA-023
  - M7.24
normative: false
---

# Histórico de Alterações 1.45.0 — Validação do Início Protegido da Jornada

## Adicionado

- UXA-023 — Validação Funcional e Reformulação do Início Protegido da Jornada;
- cenários de autenticação, recusa, texto, voz, arquivos, pausa, processamento e compreensão inicial;
- diagnóstico funcional do contrato anterior;
- hierarquia reformulada do ambiente protegido;
- sequência entre Home, autenticação, relato, processamento, compreensão e Tela Hoje;
- estados funcionais do relato;
- separação entre conta e autorização;
- revisão anterior ao processamento material;
- proteção de informações sensíveis e de terceiros;
- critérios de aceite para wireframe posterior;
- Adendo da Matriz de Consolidação Canônica para UXA-023;
- marco M7.24 — Início Protegido da Jornada Validado e Reformulado.

## Alterado

- Página Inicial da Guivos e Início da Jornada atualizada para 0.3.0;
- Arquitetura da Experiência atualizada para 0.17.0;
- Registro do Estado Atual atualizado para 1.51.0;
- Roadmap Arquitetural atualizado para 11.98.0;
- Painel de Conhecimento atualizado para 11.98.0;
- Marcos Arquiteturais atualizados para 4.96.0;
- Matriz de Consolidação Canônica atualizada para 2.17.0;
- início protegido registrado como funcionalmente válido após reformulação;
- explicação posicionada antes da autenticação e da coleta;
- criação de conta separada de autorização de processamento;
- compartilhamento mínimo e progressivo tornado obrigatório;
- estados, falhas e controles tornados visíveis;
- personalização bloqueada antes do gate revisável e autorizado.

## Decisões consolidadas

- nenhuma coleta começa automaticamente ao sair da Home;
- autenticação antecede persistência e processamento associado;
- autorização genérica não libera todas as finalidades;
- texto, voz, arquivos e perguntas são alternativas;
- digitação não equivale a autorização de processamento;
- áudio e transcrição possuem controles separados quando aplicável;
- arquivo não autoriza leitura irrestrita;
- conteúdo recebido é revisado antes do processamento material;
- rascunho, revisão, processamento, pausa, exclusão e encerramento são estados distintos;
- informações de terceiros não recebem autorização automática;
- original, transcrição, extração e interpretação permanecem distintos;
- confirmação parcial é válida;
- jornada sem personalização e exploração geral permanecem alternativas;
- Tela Hoje não é recompensa pela exposição de mais dados.

## Preservado

- Home pública sem coleta pessoal;
- wireframe gráfico da Home para computador;
- referência móvel da Home não iniciada;
- Tela Hoje como entrada recorrente após confirmação;
- Resultados Empresariais em 18 de 18 decisões humanas;
- distribuição em 9 candidatos em validação, 3 fundidos e 6 rejeitados;
- Resultados aprovados e códigos canônicos em zero;
- BUS-CAND-005 em validação;
- AQS-O01 e Capacidades Empresariais não iniciados;
- protótipo, design visual, testes e desenvolvimento não iniciados;
- Engenharia de Produto pausada antes de W0-01.

## Limites

Este incremento não cria wireframe do início protegido, referência móvel da Home, texto final, tecnologia de autenticação, formatos técnicos de voz ou arquivos, armazenamento, criptografia, modelo de inteligência artificial, protótipo, teste, componente, implementação, Resultado canônico, AQS-O01 ou Capacidade Empresarial.
