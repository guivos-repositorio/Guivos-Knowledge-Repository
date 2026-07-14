---
title: Roadmap Arquitetural
status: active
version: 7.3.0
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
- **Extensões normativas ativas de Eventos de Vida:** `PAS-001-EV-FOUNDATION-001 1.0.0`, `PAS-001-EV-LIFECYCLE-001 1.0.0`, `PAS-001-EV-VIEW-001 1.0.0`, `PAS-001-EV-EVENT-001 1.0.0` e `PAS-001-EV-INTEGRATION-001 1.0.0`.
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

### Visualização e controle

A extensão `PAS-001-EV-VIEW-001 1.0.0` consolidou:

- visão geral, resumo linguístico, linha do tempo e orientação temporal;
- escalas, agrupamentos, filtros, cartões e detalhamento progressivo;
- separação visual entre sinais, propostas, eventos planejados e eventos ocorridos;
- apresentação distinta do estado do evento e do estado da informação;
- temporalidade aproximada sem falsa precisão;
- relevância, origem, autoridade, confiança, evidências e impactos;
- relações com Contexto Vivo, Objetivos e capacidades consumidoras;
- eventos compostos, cadeias, participantes relacionados e informações de terceiros;
- controles de eventos planejados, atualizações, conclusão, interrupção, arquivamento e reabertura;
- correção, contestação, unificação, separação e revisão individual de impactos;
- fila de atenção, alertas, prevenção de fadiga e controle de notificações;
- privacidade visual, títulos neutros, dispositivos compartilhados e compartilhamentos;
- explicabilidade, acessibilidade, consistência entre canais, histórico, sincronização e falha segura.

### Contratos dos eventos funcionais

A extensão `PAS-001-EV-EVENT-001 1.0.0` consolidou:

- distinção entre comando, proposta e evento funcional reconhecido;
- imutabilidade histórica e correção compensatória;
- estrutura comum, campos obrigatórios, titular, ator, fonte e autoridade;
- tempos do fato, conhecimento, reconhecimento e aplicação;
- finalidade, sensibilidade, permissões, correlação, causalidade e versionamento;
- famílias e contratos de identificação, proposição, declaração, planejamento e confirmação;
- contratos de início, atualização, adiamento, temporalidade e relevância;
- contratos de impactos, dimensões contextuais, objetivos e revisões dependentes;
- relações propostas, confirmadas e contestadas, incluindo causalidade explicável;
- conclusão, interrupção, cancelamento, contestação, correção, arquivamento e reabertura;
- unificação, desdobramento e eventos compostos;
- autorização, revogação, recomposição de recortes e propagação;
- idempotência, duplicidade semântica, ordenação, concorrência e versão esperada;
- retenção, logs, falhas de processamento, recuperação e auditoria;
- responsabilidades de produtores, consumidores, Guivos Intelligence e Platform Layer.

### Integrações funcionais

A extensão `PAS-001-EV-INTEGRATION-001 1.0.0` consolidou:

- finalidade explícita, minimização, titularidade preservada, autoridade limitada e neutralidade comercial;
- tipos, modos e contrato funcional comum das integrações;
- identidade, associação, papéis, proveniência, qualidade, confiança e transformações rastreáveis;
- temporalidade da fonte, do fato, do recebimento, do processamento e da aplicação;
- sincronização, prevenção de ciclos, divergências e hierarquia não absoluta das fontes;
- integração com Captura de Contexto, Contexto Vivo e Objetivos;
- integração com Próximos Passos, Oportunidades Ativas e Intervenções Contextuais;
- integração com Experiências e Evolução Contínua;
- saídas permitidas e limites da Guivos Intelligence;
- responsabilidades técnicas da Platform Layer;
- integrações com Guivos Business, Mall, Travel, Media e Ads;
- serviços profissionais, educacionais, de saúde, financeiros, calendários, localização, esportes, organizações sociais, comunidades religiosas, serviços jurídicos e fontes públicas;
- integrações pessoais e temporárias, pausa, revogação e distinção entre uso futuro e fato histórico;
- degradação controlada, fonte indisponível, informação incompleta, retroatividade, correção externa e recuperação;
- eventos compartilhados, proteção de terceiros, explicabilidade, auditoria, retenção e métricas sistêmicas.

O próximo bloco consolidará KPIs, guardrails, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão e contrato final da Capacidade de Eventos de Vida.

## Progresso das capacidades do Journey

| Capacidade | Estado | Progresso de referência |
|---|---|---|
| 01 — Captura de Contexto | Substantially complete | 95% |
| 02 — Contexto Vivo | Functionally complete | 100% |
| 03 — Objetivos | Functionally complete | 100% |
| 04 — Eventos de Vida | In progress | 90% |
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
- não transformar a linha do tempo em feed social, diário integral ou instrumento de avaliação pessoal;
- não apresentar impactos propostos como aplicados;
- não expor eventos sensíveis em cartões, notificações, dispositivos compartilhados ou ambientes organizacionais;
- não utilizar ranking, pontuação, cobrança ou gamificação coercitiva em Eventos de Vida;
- não apresentar comandos ou propostas pendentes como fatos reconhecidos;
- não reescrever eventos históricos para corrigir o passado;
- não publicar evento de sucesso quando parte crítica da operação falhar;
- não duplicar eventos, impactos, notificações ou revisões durante reprocessamento;
- não permitir que consumidores ampliem a autoridade ou o significado do recorte recebido;
- não declarar revogação concluída antes da propagação efetiva;
- não utilizar acesso técnico como autoridade funcional;
- não usar disponibilidade de dado como autorização de uso;
- não importar histórico integral por padrão;
- não transformar compra, reserva, calendário, localização ou atividade em confirmação automática de Evento de Vida;
- não utilizar Eventos de Vida sensíveis para publicidade;
- não manter uso após revogação;
- não tratar indisponibilidade de fonte como ausência de evento;
- não manter versões paralelas silenciosas entre canais;
- não explorar comercialmente vulnerabilidades ou eventos sensíveis;
- não iniciar o próximo produto antes de conclusão funcional suficiente do Journey.

## Ponto exato de retomada

Retomar na **Capacidade 04 — Eventos de Vida**.

Próxima entrega:

1. objetivos, princípios e unidades de medição;
2. famílias de KPIs de qualidade e desempenho funcional;
3. guardrails obrigatórios de tolerância zero;
4. baseline, painel de saúde e níveis de desempenho;
5. cenários funcionalmente ideal;
6. cenários alternativos;
7. cenários limite;
8. critérios de conclusão funcional e lacunas bloqueantes ou não bloqueantes;
9. contrato final da Capacidade 04;
10. decisão sobre conclusão funcional e ativação da Capacidade 05 — Próximos Passos.
