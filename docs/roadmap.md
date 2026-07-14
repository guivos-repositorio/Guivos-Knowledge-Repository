---
title: Roadmap Arquitetural
status: active
version: 7.4.0
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
- **Capacidades concluídas:** `02 — Contexto Vivo`, `03 — Objetivos` e `04 — Eventos de Vida`.
- **Próxima capacidade:** `05 — Próximos Passos`, ainda documentalmente `Planned`.
- **Contrato final de Eventos de Vida:** `PAS-001-EV-CONTRACT-001 1.0.0`.
- **Arquitetura funcional:** `GLPA-001 1.1.1`.
- **Intelligence Architecture:** `GIA-000 1.3.0`.
- **Glossário Canônico:** `1.8.0`.
- **Guia Oficial:** `GOG-001 4.2.1`.
- **GKA-000:** Parte V pendente.
- **A2-R02:** em espera operacional.
- **Guivos Economic Model:** planejado.

## Direção vigente

O próximo trabalho deverá iniciar a `Capacidade 05 — Próximos Passos` do `PAS-001 — Guivos Journey`.

A ativação normativa ocorrerá com a criação da primeira extensão específica da capacidade.

> A unidade de trabalho é a capacidade funcional completa, não uma funcionalidade isolada ou descrição de tela.

## Capacidades concluídas

### Capacidade 02 — Contexto Vivo

O `PAS-001 0.5.0` e as oito extensões normativas do Contexto Vivo consolidaram estados, atualização, conflitos, interface, eventos, integrações, KPIs, cenários e contrato final.

A Capacidade 02 permanece **Functionally complete** e não deverá ser reaberta sem lacuna crítica, evidência operacional, incidente ou decisão formal.

### Capacidade 03 — Objetivos

As sete extensões normativas de Objetivos consolidaram fundamentos, ciclo de vida, critérios, progresso, visão, eventos, integrações, 62 KPIs, 12 guardrails, cenários e contrato final.

O `PAS-001-OBJ-CONTRACT-001 1.0.0` confirma a Capacidade 03 como **Functionally complete**.

### Capacidade 04 — Eventos de Vida

As seis extensões normativas consolidaram integralmente a semântica funcional da capacidade.

#### Fundamentos

`PAS-001-EV-FOUNDATION-001 1.0.0` definiu pergunta central, objetivo, valor, singularidade, conceito, tipos, titularidade, origem, autoridade, temporalidade, impacto, responsabilidades, limites, sensibilidade e controle do participante.

#### Ciclo de vida

`PAS-001-EV-LIFECYCLE-001 1.0.0` definiu identificação, proposição, confirmação, estados, transições, temporalidade, relevância, impactos, relações, correção, contestação, encerramento, arquivamento, reabertura, propagação e falha segura.

#### Visualização e controle

`PAS-001-EV-VIEW-001 1.0.0` definiu linha do tempo, cartões, detalhamento, eventos planejados, impactos, ações, privacidade visual, histórico, acessibilidade, explicabilidade e consistência entre canais.

#### Contratos dos eventos funcionais

`PAS-001-EV-EVENT-001 1.0.0` definiu comandos, propostas, fatos reconhecidos, imutabilidade histórica, temporalidades, autoridade, contratos de eventos e impactos, idempotência, ordenação, concorrência, auditoria e falha segura.

#### Integrações funcionais

`PAS-001-EV-INTEGRATION-001 1.0.0` definiu finalidade, minimização, identidade, autoridade, proveniência, qualidade, transformações, sincronização, divergências, integrações com capacidades, produtos, serviços e fontes externas, pausa, revogação, degradação controlada e neutralidade comercial.

#### KPIs, guardrails, cenários e contrato final

`PAS-001-EV-CONTRACT-001 1.0.0` consolidou:

- sessenta KPIs em treze famílias;
- dezoito guardrails de tolerância zero;
- baseline funcional antes de metas permanentes;
- painel de saúde e níveis `Crítico`, `Instável`, `Adequado`, `Confiável` e `Maduro`;
- cenários funcionalmente ideal, alternativo e limite;
- critérios de conclusão funcional;
- lacunas bloqueantes e não bloqueantes;
- contrato final de propósito, titularidade, responsabilidades, limites, entradas, admissão, representação, estados, saídas, visão, eventos, integrações, permissões, privacidade, falhas, explicabilidade e indicadores;
- regra de reabertura somente por fundamento crítico ou decisão formal.

O contrato final substitui normativamente o estado `In progress` da Capacidade 04 por **Functionally complete**.

## Progresso das capacidades do Journey

| Capacidade | Estado | Progresso de referência |
|---|---|---|
| 01 — Captura de Contexto | Substantially complete | 95% |
| 02 — Contexto Vivo | Functionally complete | 100% |
| 03 — Objetivos | Functionally complete | 100% |
| 04 — Eventos de Vida | Functionally complete | 100% |
| 05 — Próximos Passos | Planned — próxima frente | 0% |
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

Esses entregáveis podem ser executados como frente operacional independente, sem substituir a prioridade arquitetural da Capacidade 05.

## Restrições

- não retornar à meta-arquitetura como foco imediato;
- não promover LPM, CIE, GPMA ou outros candidatos diretamente à Canon;
- não tratar conceitos candidatos como componentes técnicos obrigatórios;
- preservar rastreabilidade entre decisões funcionais e arquiteturas vigentes;
- não reabrir as Capacidades 02, 03 ou 04 sem fundamento formal;
- não reduzir Evento de Vida a qualquer atividade, experiência ou atualização comum;
- não tratar evento planejado como ocorrido;
- não transformar sinal ou inferência em Evento de Vida confirmado;
- não confundir confirmação do evento com confirmação de todos os impactos;
- não fabricar precisão temporal;
- não presumir causalidade por proximidade temporal;
- não aplicar impactos indiscriminadamente;
- não criar objetivo pessoal ativo ou impor prioridade a partir de Evento de Vida;
- não encerrar impactos automaticamente quando o evento for concluído;
- não transformar linha do tempo em feed social, diário integral ou instrumento de avaliação pessoal;
- não expor eventos sensíveis em interfaces, notificações ou ambientes inadequados;
- não utilizar ranking, pontuação, cobrança ou gamificação coercitiva em Eventos de Vida;
- não reescrever eventos históricos;
- não duplicar eventos, impactos, notificações ou revisões;
- não permitir ampliação de autoridade por consumidores ou integrações;
- não declarar revogação concluída antes da propagação efetiva;
- não utilizar acesso técnico como autoridade funcional;
- não transformar compra, reserva, calendário, localização ou atividade em confirmação automática de mudança humana;
- não utilizar Eventos de Vida sensíveis para publicidade;
- não manter uso após revogação;
- não tratar indisponibilidade de fonte como ausência de evento;
- não permitir que médias ocultem violações de guardrails;
- não iniciar o próximo produto antes da conclusão funcional suficiente do Journey.

## Ponto exato de retomada

Retomar na **Capacidade 05 — Próximos Passos**.

Próxima entrega:

1. pergunta central;
2. objetivo funcional;
3. valor entregue;
4. singularidade;
5. princípios;
6. definição de Próximo Passo;
7. distinções entre Próximo Passo, tarefa, objetivo, oportunidade, intervenção, compromisso e recomendação;
8. titularidade e responsabilidade;
9. tipos funcionais;
10. origem e autoridade;
11. estados iniciais;
12. prioridade operacional;
13. temporalidade;
14. dependências;
15. relação com Contexto Vivo, Objetivos e Eventos de Vida;
16. limites da Guivos Intelligence;
17. controle do participante.
