---
title: Roadmap Arquitetural
status: active
version: 6.7.0
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
- **Capacidade concluída:** `02 — Contexto Vivo`.
- **Capacidade ativa:** `03 — Objetivos`.
- **Extensões normativas ativas de Objetivos:** `PAS-001-OBJ-FOUNDATION-001 1.0.0`, `PAS-001-OBJ-LIFECYCLE-001 1.0.0`, `PAS-001-OBJ-PROGRESS-001 1.0.0`, `PAS-001-OBJ-VIEW-001 1.0.0`, `PAS-001-OBJ-EVENT-001 1.0.0` e `PAS-001-OBJ-INTEGRATION-001 1.0.0`.
- **Arquitetura funcional:** `GLPA-001 1.1.1`.
- **Intelligence Architecture:** `GIA-000 1.3.0`.
- **Glossário Canônico:** `1.8.0`.
- **Guia Oficial:** `GOG-001 4.2.1`.
- **GKA-000:** Parte V pendente.
- **A2-R02:** em espera operacional.
- **Guivos Economic Model:** planejado.

## Direção vigente

O trabalho permanece na `Capacidade 03 — Objetivos` do `PAS-001 — Guivos Journey`.

> A unidade de trabalho é a capacidade funcional completa, não uma funcionalidade isolada ou descrição de tela.

## Capacidade 02 concluída

O `PAS-001 0.5.0` e as oito extensões normativas do Contexto Vivo consolidaram estados, atualização, conflitos, interface, eventos, integrações, KPIs, cenários e contrato final.

A Capacidade 02 permanece **Functionally complete** e não deverá ser reaberta sem lacuna crítica, evidência operacional ou decisão formal.

## Avanço da Capacidade 03

A extensão `PAS-001-OBJ-FOUNDATION-001 1.0.0` consolidou fundamentos, distinções conceituais, responsabilidades, limites, entradas, estados, relações, conflitos, critérios de sucesso e integrações iniciais.

A extensão `PAS-001-OBJ-LIFECYCLE-001 1.0.0` consolidou criação, confirmação, ativação, prioridade, conflitos, revisão, envelhecimento e ciclo de vida.

A extensão `PAS-001-OBJ-PROGRESS-001 1.0.0` consolidou critérios de sucesso, linhas de base, progresso, marcos, evidências, resultados parciais, conclusão, contestação e reabertura.

A extensão `PAS-001-OBJ-VIEW-001 1.0.0` consolidou a visão `Meus Objetivos`, incluindo portfólio, detalhamento, controles, explicações, revisões, alertas, privacidade, consistência entre canais e histórico.

A extensão `PAS-001-OBJ-EVENT-001 1.0.0` consolidou contratos de eventos, autoridade, temporalidade, causalidade, correlação, idempotência, propagação, correção, auditoria e falha segura.

A extensão `PAS-001-OBJ-INTEGRATION-001 1.0.0` consolidou:

- princípios, tipos, modos e contrato funcional comum das integrações;
- requisitos de admissão, identidade, autoridade, proveniência, qualidade e transformações;
- temporalidade, sincronização, consistência entre fontes e prevenção de ciclos;
- integração com Captura de Contexto, Contexto Vivo e Eventos de Vida;
- integração com Próximos Passos, Oportunidades Ativas e Intervenções Contextuais;
- integração com Experiências e Evolução Contínua;
- saídas permitidas, limites e explicabilidade da Guivos Intelligence;
- responsabilidades da Platform Layer para identidade, autorização, grafo, APIs, busca, notificações, armazenamento e observabilidade;
- integrações com Guivos Business, Mall, Travel, Media e Ads;
- integrações com serviços sociais, profissionais, educacionais, esportivos, de saúde, calendários e fontes financeiras;
- integrações temporárias, pausa, revogação, falha, degradação controlada e sincronização divergente;
- explicabilidade, auditoria, métricas, eventos e integrações proibidas.

O próximo bloco consolidará KPIs, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão e contrato final da capacidade.

## Progresso das capacidades do Journey

| Capacidade | Estado | Progresso de referência |
|---|---|---|
| 01 — Captura de Contexto | Substantially complete | 95% |
| 02 — Contexto Vivo | Functionally complete | 100% |
| 03 — Objetivos | In progress | 95% |
| 04 — Eventos de Vida | Planned / concept consolidated | 10% |
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

Esses entregáveis podem ser executados como frente operacional independente, sem substituir a prioridade arquitetural da Capacidade 03.

## Restrições

- não retornar à meta-arquitetura como foco imediato;
- não promover LPM, CIE, GPMA ou outros candidatos diretamente à Canon;
- não tratar conceitos candidatos como componentes técnicos obrigatórios;
- preservar rastreabilidade entre decisões funcionais e arquiteturas vigentes;
- não transformar inferência, comportamento ou interesse comercial em objetivo ativo;
- não confundir atividade com progresso ou conclusão;
- não utilizar percentuais sem base legítima;
- não concluir objetivos pessoais apenas por inferência;
- não transformar `Meus Objetivos` em painel de cobrança, produtividade, ranking ou comparação pessoal;
- não expor objetivos sensíveis em notificações ou superfícies não autorizadas;
- não tratar comando ou proposta como evento reconhecido;
- não reprocessar eventos com efeitos duplicados;
- não ampliar permissões, titularidade, finalidade ou autoridade durante integração;
- não permitir que receita, patrocínio ou oferta comercial alterem prioridade funcional;
- não reabrir a Capacidade 02 sem fundamento formal;
- não iniciar o próximo produto antes de conclusão funcional suficiente do Journey.

## Ponto exato de retomada

Retomar na **Capacidade 03 — Objetivos**.

Próxima entrega:

1. KPIs e indicadores de qualidade e desempenho funcional;
2. cenário funcionalmente ideal;
3. cenários alternativos;
4. cenários limite e falha segura;
5. critérios de conclusão funcional;
6. contrato final da capacidade.