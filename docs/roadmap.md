---
title: Roadmap Arquitetural
status: active
version: 5.5.0
owner: Guivos
last_updated: 2026-07-13
---

# Roadmap Arquitetural

Este roadmap acompanha a evolução do GKR, da arquitetura empresarial e das frentes de especificação executável da Guivos.

## Estado atual

- **Era vigente:** `GE-2 — Knowledge`.
- **Marco vigente:** `M5.9 — Chat Continuity and Repository Reconciliation Completed`.
- **Frente operacional vigente:** `Product Engineering`.
- **Sincronização vigente:** `GE2-SYNC-007`.
- **Revisão vigente:** `AR-001`, concluída na versão `0.5.0`.
- **Especificação ativa:** `PAS-001 — Guivos Journey 0.5.0`.
- **Extensões normativas ativas:** `PAS-001-CV-STATE-001 1.0.0` e `PAS-001-CV-UPDATE-001 1.0.0`.
- **Arquitetura funcional:** `GLPA-001 1.1.1`.
- **Intelligence Architecture:** `GIA-000 1.3.0`.
- **Glossário Canônico:** `1.8.0`.
- **Guia Oficial:** `GOG-001 4.2.1`.
- **Capacidade ativa:** `02 — Contexto Vivo`.
- **GKA-000:** Parte V pendente.
- **A2-R02:** em espera operacional.
- **Guivos Economic Model:** planejado.

## Direção vigente

O trabalho permanece na `Capacidade 02 — Contexto Vivo` do `PAS-001 — Guivos Journey`.

> A unidade de trabalho é a capacidade funcional completa, não uma funcionalidade isolada ou descrição de tela.

Novos frameworks estruturais não serão desenvolvidos enquanto os produtos oficiais não possuírem especificação funcional suficiente.

## Avanço da Capacidade 02

O `PAS-001 0.5.0` consolidou:

- responsabilidades e limites;
- fronteiras funcionais entre Journey, Intelligence, Platform e capacidades consumidoras;
- categorias de entrada;
- requisitos mínimos e regras de admissão;
- saídas funcionais;
- eventos funcionais iniciais;
- contrato funcional das saídas.

A extensão normativa `PAS-001-CV-STATE-001 1.0.0` consolidou:

- estrutura comum de estado;
- estados funcionais das oito dimensões;
- transições e impactos controlados entre dimensões.

A extensão normativa `PAS-001-CV-UPDATE-001 1.0.0` consolidou:

- elemento contextual como unidade mínima de atualização;
- gatilhos e fluxo funcional de atualização;
- resultados possíveis da avaliação;
- confirmação proporcional ao impacto;
- regras conforme origem e evidência;
- classes temporais e estados de envelhecimento;
- horizontes e revisões por dimensão;
- prevenção de fadiga de confirmação;
- atualizações silenciosas permitidas e proibidas;
- efeitos das permissões;
- propagação, reprocessamento e atualizações retroativas;
- distinção entre correção e mudança real;
- eventos funcionais relacionados.

O próximo bloco definirá a resolução detalhada de conflitos entre informações, interpretações, fontes e temporalidades.

## Reconciliação de continuidade

A `GE2-SYNC-007` concluiu a leitura do estado atual do repositório e a comparação com o extrato final da conversa anterior.

Resultados:

- nenhuma decisão arquitetural madura ausente foi identificada;
- Contexto Vivo e Market Validation estavam incorporados;
- divergências editoriais demonstráveis foram autorizadas para correção;
- formulário e planilha de validação permanecem entregáveis operacionais futuros;
- o ponto de retomada do Product Engineering foi preservado e avançado para resolução de conflitos do Contexto Vivo.

## Progresso das capacidades do Journey

| Capacidade | Estado | Progresso de referência |
|---|---|---|
| 01 — Captura de Contexto | Substantially complete | 95% |
| 02 — Contexto Vivo | In progress | 75% |
| 03 — Objetivos | Planned | 0% |
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

Esses entregáveis podem ser executados como frente operacional independente, sem substituir a prioridade arquitetural do Contexto Vivo.

## Restrições

- não retornar à meta-arquitetura como foco imediato;
- não promover LPM, CIE, GPMA ou outros candidatos diretamente à Canon;
- não tratar conceitos candidatos como componentes técnicos obrigatórios;
- preservar rastreabilidade entre decisões funcionais e arquiteturas vigentes;
- não iniciar o próximo produto antes de conclusão funcional suficiente do atual.

## Ponto exato de retomada

Retomar na **Capacidade 02 — Contexto Vivo**.

Próxima entrega:

1. resolução detalhada de conflitos;
2. comportamentos da interface `Meu Contexto Hoje`;
3. contratos detalhados dos eventos;
4. integrações;
5. KPIs;
6. cenários ideal, alternativo e limite;
7. contrato da capacidade.
