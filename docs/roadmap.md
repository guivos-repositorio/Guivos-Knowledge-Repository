---
title: Roadmap Arquitetural
status: active
version: 7.5.0
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
- **Capacidade ativa:** `05 — Próximos Passos`, `In progress`, 20%.
- **Fundamentos de Próximos Passos:** `PAS-001-PP-FOUNDATION-001 1.0.0`.
- **Arquitetura funcional:** `GLPA-001 1.1.1`.
- **Intelligence Architecture:** `GIA-000 1.3.0`.
- **Glossário Canônico:** `1.8.0`.
- **Guia Oficial:** `GOG-001 4.2.1`.
- **GKA-000:** Parte V pendente.
- **A2-R02:** em espera operacional.
- **Guivos Economic Model:** planejado.

## Direção vigente

O próximo trabalho deverá consolidar o ciclo de vida da `Capacidade 05 — Próximos Passos`.

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

- `PAS-001-EV-FOUNDATION-001 1.0.0` definiu fundamentos, conceito, tipos, titularidade, autoridade, temporalidade, impacto, responsabilidades, limites, sensibilidade e controle.
- `PAS-001-EV-LIFECYCLE-001 1.0.0` definiu identificação, proposição, confirmação, estados, transições, relevância, impactos, relações, correção, contestação, encerramento, propagação e falha segura.
- `PAS-001-EV-VIEW-001 1.0.0` definiu linha do tempo, detalhamento, eventos planejados, impactos, ações, privacidade visual, histórico e explicabilidade.
- `PAS-001-EV-EVENT-001 1.0.0` definiu comandos, propostas, fatos reconhecidos, imutabilidade, contratos, idempotência, ordenação, auditoria e falha segura.
- `PAS-001-EV-INTEGRATION-001 1.0.0` definiu finalidade, minimização, identidade, autoridade, proveniência, integrações, revogação e degradação controlada.
- `PAS-001-EV-CONTRACT-001 1.0.0` consolidou 60 KPIs, 18 guardrails, baseline, painel de saúde, cenários e contrato final.

A Capacidade 04 permanece **Functionally complete**.

## Capacidade ativa

### Capacidade 05 — Próximos Passos

`PAS-001-PP-FOUNDATION-001 1.0.0` é a primeira extensão normativa da capacidade e substitui o estado `Planned` da linha da Capacidade 05 no `PAS-001 0.5.0` por `In progress`.

Os fundamentos consolidam:

- pergunta central, objetivo funcional, valor e singularidade;
- Próximo Passo como decisão ou hipótese de movimento contextual;
- acionabilidade e natureza contextual do termo “próximo”;
- distinções entre Próximo Passo, objetivo, tarefa, ação, plano, oportunidade, intervenção, recomendação e compromisso;
- titularidade, papéis funcionais, responsabilidade, origem e autoridade;
- tipos e classificações funcionais;
- estados iniciais e separação entre estado funcional e estado da informação;
- prioridade operacional, sequenciamento, dependências e bloqueios;
- temporalidade, esforço, risco, segurança e sensibilidade;
- entradas, estrutura, saídas e fluxo funcional inicial;
- relações com Contexto Vivo, Objetivos, Eventos de Vida, Oportunidades, Intervenções, Experiências e Evolução Contínua;
- limites da Guivos Intelligence e da Platform Layer;
- controle do participante e ausência legítima de Próximo Passo.

A capacidade está `In progress`, com progresso editorial de referência de `20%`.

## Progresso das capacidades do Journey

| Capacidade | Estado | Progresso de referência |
|---|---|---|
| 01 — Captura de Contexto | Substantially complete | 95% |
| 02 — Contexto Vivo | Functionally complete | 100% |
| 03 — Objetivos | Functionally complete | 100% |
| 04 — Eventos de Vida | Functionally complete | 100% |
| 05 — Próximos Passos | In progress | 20% |
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
- não reduzir Próximo Passo a objetivo, tarefa, oportunidade, recomendação ou compromisso;
- não apresentar proposta como decisão assumida;
- não apresentar confirmação como execução iniciada;
- não criar listas infinitas ou ações artificiais para aumentar engajamento;
- não impor produtividade, prioridade pessoal ou responsabilidade silenciosa;
- não concluir objetivo automaticamente pela conclusão de um passo;
- não utilizar oportunidade, receita, patrocínio ou publicidade para determinar prioridade;
- não tratar bloqueio, pausa, cancelamento ou expiração como incapacidade ou fracasso;
- não fabricar prazos ou precisão temporal;
- não transformar atividade observada em conclusão automática;
- não utilizar vulnerabilidade para indução comercial;
- proteger passos sensíveis e informações de terceiros;
- preservar autonomia, explicabilidade e controle do participante;
- não iniciar o próximo produto antes da conclusão funcional suficiente do Journey.

## Ponto exato de retomada

Retomar no **ciclo de vida dos Próximos Passos**.

Próxima entrega:

1. criação e proposição;
2. confirmação, prontidão e ativação;
3. prioridade e sequenciamento;
4. dependências e bloqueios;
5. pausa, execução e conclusão;
6. cancelamento, substituição e expiração;
7. contestação e correção;
8. recorrência;
9. compartilhamento;
10. propagação.