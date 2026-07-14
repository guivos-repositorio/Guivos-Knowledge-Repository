---
title: Roadmap Arquitetural
status: active
version: 7.0.0
owner: Guivos
last_updated: 2026-07-14
---

# Roadmap Arquitetural

Este roadmap acompanha a evolução do GKR, da arquitetura empresarial e das frentes de especificação executável da Guivos.

## Estado atual

- **Era vigente:** `GE-2 — Knowledge`.
- **Marco vigente:** `M5.9 — Chat Continuity and Repository Reconciliation Completed`.
- **Frente operacional vigente:** `Product Engineering`.
- **Especificação-base ativa:** `PAS-001 — Guivos Journey 0.5.0`.
- **Capacidades concluídas:** `02 — Contexto Vivo` e `03 — Objetivos`.
- **Capacidade ativa:** `04 — Eventos de Vida`.
- **Extensões normativas ativas de Eventos de Vida:** `PAS-001-EV-FOUNDATION-001 1.0.0` e `PAS-001-EV-LIFECYCLE-001 1.0.0`.
- **Arquitetura funcional:** `GLPA-001 1.1.1`.
- **Intelligence Architecture:** `GIA-000 1.3.0`.
- **Glossário Canônico:** `1.8.0`.
- **Guia Oficial:** `GOG-001 4.2.1`.
- **GKA-000:** Parte V pendente.
- **A2-R02:** em espera operacional.
- **Guivos Economic Model:** planejado.

## Direção vigente

O trabalho permanece na `Capacidade 04 — Eventos de Vida` do `PAS-001 — Guivos Journey`.

> A unidade de trabalho é a capacidade funcional completa, não uma funcionalidade isolada ou descrição de tela.

## Capacidades concluídas

### Capacidade 02 — Contexto Vivo

O `PAS-001 0.5.0` e as oito extensões normativas do Contexto Vivo consolidaram estados, atualização, conflitos, interface, eventos, integrações, KPIs, cenários e contrato final.

A Capacidade 02 permanece **Functionally complete** e não deverá ser reaberta sem lacuna crítica, evidência operacional ou decisão formal.

### Capacidade 03 — Objetivos

As sete extensões normativas de Objetivos consolidaram fundamentos, ciclo de vida, critérios, progresso, visão, eventos, integrações, 62 KPIs, 12 guardrails, cenários e contrato final.

O `PAS-001-OBJ-CONTRACT-001 1.0.0` substitui normativamente o estado anterior e confirma a Capacidade 03 como **Functionally complete**.

## Avanço da Capacidade 04

### Fundamentos

A extensão `PAS-001-EV-FOUNDATION-001 1.0.0` consolidou:

- pergunta central, objetivo funcional, valor entregue e singularidade;
- definição de Evento de Vida e distinções conceituais;
- tipos, titularidade, participantes afetados, origem e autoridade;
- temporalidade, estados, relações, relevância e impacto inicial;
- responsabilidades, limites, entradas e estrutura funcional;
- relações com Contexto Vivo, Objetivos e demais capacidades;
- sensibilidade, informações de terceiros, explicabilidade e controle do participante.

### Ciclo de vida

A extensão `PAS-001-EV-LIFECYCLE-001 1.0.0` consolidou:

- entrada, identificação, sinalização, proposição e declaração;
- autoridade, integrações, inferências e confirmação proporcional;
- estados `Planejado`, `Confirmado`, `Iniciado`, `Em andamento`, `Concluído`, `Interrompido`, `Cancelado`, `Contestado`, `Corrigido`, `Arquivado` e `Reaberto`;
- estado do evento separado do estado da informação;
- temporalidade exata, aproximada, indeterminada e retroativa;
- relevância contextual e revisável;
- impactos propostos e confirmados por unidade afetada;
- relações, causalidade, correlação, cadeias, eventos compostos, unificação e separação;
- correção, contestação, encerramento, arquivamento e reabertura;
- propagação por recortes mínimos, idempotência, prevenção de ciclos e falha segura.

O próximo bloco consolidará a visualização e o controle funcional dos Eventos de Vida: linha do tempo, detalhamento, impactos, revisões, eventos planejados, conteúdo sensível, histórico e ações do participante.

## Progresso das capacidades do Journey

| Capacidade | Estado | Progresso de referência |
|---|---|---|
| 01 — Captura de Contexto | Substantially complete | 95% |
| 02 — Contexto Vivo | Functionally complete | 100% |
| 03 — Objetivos | Functionally complete | 100% |
| 04 — Eventos de Vida | In progress | 40% |
| 05 — Próximos Passos | Planned | 0% |
| 06 — Oportunidades Ativas | Planned / concept consolidated | 10% |
| 07 — Intervenções Contextuais | Planned / concept consolidated | 10% |
| 08 — Experiências | Planned | 0% |
| 09 — Evolução Contínua | Planned | 0% |

Os percentuais são referências editoriais de acompanhamento, não medição automatizada.

## Backlog posterior

1. concluir funcionalmente o Journey;
2. desenvolver o Guivos Economic Model;
3. especificar Guivos Mall;
4. especificar Guivos Business;
5. especificar Guivos Intelligence;
6. especificar Guivos Ads;
7. especificar Guivos Media;
8. especificar Guivos Travel;
9. desenvolver Commercial Model;
10. desenvolver Go-to-Market.

### Entregáveis operacionais de validação

- gerar o formulário definitivo de aplicação;
- construir a planilha automática de tratamento, KPIs, IGV, gates e decisão.

Esses entregáveis podem ser executados como frente operacional independente, sem substituir a prioridade arquitetural da Capacidade 04.

## Restrições

- não retornar à meta-arquitetura como foco imediato;
- não promover LPM, CIE, GPMA ou outros candidatos diretamente à Canon;
- não tratar conceitos candidatos como componentes técnicos obrigatórios;
- preservar rastreabilidade entre decisões funcionais e arquiteturas vigentes;
- não reabrir as Capacidades 02 ou 03 sem fundamento formal;
- não reduzir Evento de Vida a qualquer atividade, experiência ou atualização comum;
- não tratar evento planejado como ocorrido;
- não transformar sinal ou inferência em Evento de Vida confirmado;
- não confundir confirmação do evento com confirmação de todos os impactos;
- não fabricar precisão temporal;
- não presumir causalidade por proximidade temporal;
- não aplicar impactos indiscriminadamente a todo o contexto ou portfólio de objetivos;
- não criar objetivo pessoal ativo ou impor prioridade a partir de Evento de Vida;
- não encerrar impactos automaticamente quando o evento for concluído;
- não explorar comercialmente vulnerabilidades ou eventos sensíveis;
- não iniciar o próximo produto antes de conclusão funcional suficiente do Journey.

## Ponto exato de retomada

Retomar na **Capacidade 04 — Eventos de Vida**.

Próxima entrega:

1. estrutura da linha do tempo;
2. visão geral e agrupamentos;
3. cartões e detalhamento do evento;
4. estados, temporalidade, relevância e impactos;
5. eventos planejados e em andamento;
6. ações de confirmação, correção, contestação, arquivamento e reabertura;
7. proteção de conteúdo sensível e privacidade visual;
8. revisões, histórico, sincronização e falha segura.
