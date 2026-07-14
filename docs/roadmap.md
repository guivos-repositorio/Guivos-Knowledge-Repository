---
title: Roadmap Arquitetural
status: active
version: 5.9.0
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
- **Extensões normativas ativas:** `PAS-001-CV-STATE-001 1.0.0`, `PAS-001-CV-UPDATE-001 1.0.0`, `PAS-001-CV-CONFLICT-001 1.0.0`, `PAS-001-CV-VIEW-001 1.0.0`, `PAS-001-CV-EVENT-001 1.0.0` e `PAS-001-CV-INTEGRATION-001 1.0.0`.
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

A extensão normativa `PAS-001-CV-CONFLICT-001 1.0.0` consolidou:

- princípios, tipos e estados funcionais de conflito;
- registro próprio e fluxo de resolução;
- critérios de comparação e ordem funcional de consideração;
- resultados possíveis e participação do participante;
- conflitos entre declarações, integrações, organizações, comportamentos, dimensões, permissões e temporalidades;
- impactos sobre capacidades consumidoras e decisões existentes;
- resolução automática permitida e proibida;
- explicabilidade, reabertura e critérios de resolução confiável.

A extensão normativa `PAS-001-CV-VIEW-001 1.0.0` consolidou:

- objetivos e princípios de `Meu Contexto Hoje`;
- síntese do momento e visualização das oito dimensões;
- estados linguísticos e níveis progressivos de detalhamento;
- confirmação, correção, contestação e tratamento de inferências;
- conflitos, envelhecimento, informações sensíveis e permissões por finalidade;
- integrações, histórico e evidências de evolução;
- priorização de atenção e prevenção de sobrecarga;
- explicação de recomendações e consequências de alterações;
- recuperação, falhas, consistência entre canais, acessibilidade e privacidade visual;
- eventos relacionados e critérios funcionais de aceitação.

A extensão normativa `PAS-001-CV-EVENT-001 1.0.0` consolidou:

- distinção entre comandos, propostas e fatos reconhecidos;
- princípios de imutabilidade histórica, temporalidade, proveniência, minimização e reprocessamento seguro;
- estrutura comum, identidade, correlação, ordenação e versionamento dos eventos;
- categorias e contratos de atualização, confirmação, revisão, envelhecimento e conflitos;
- contratos de permissões, integrações, recortes contextuais, propagação e reavaliação de decisões;
- separação entre eventos de interação e eventos de mudança contextual;
- contratos de ocultação, desfazimento, remoção, dimensão e contexto atualizados;
- regras para informações sensíveis, inferências, eventos retroativos, correções, duplicidade e falhas de processamento;
- explicabilidade, retenção e critérios funcionais de aceitação.

A extensão normativa `PAS-001-CV-INTEGRATION-001 1.0.0` consolidou:

- objetivos, princípios, tipos, modos e contrato funcional das integrações;
- identificação do participante, proveniência e autoridade limitada das fontes;
- integração com as capacidades 01 a 09 do Journey;
- integração com Guivos Intelligence, Platform Layer, Business, Mall, Travel, Media e Ads;
- classes, qualidade, transformações e limites das fontes externas;
- proteção de informações de terceiros, sensíveis e temporárias de sessão;
- autorização, pausa, revogação, falhas e degradação controlada;
- sincronização divergente, frequência, explicabilidade e auditoria;
- prevenção de ciclos indevidos e exclusão inadequada de oportunidades;
- integração com conversas, notificações, busca e jornadas relacionadas.

O próximo bloco definirá os KPIs, indicadores de qualidade e critérios de desempenho funcional do Contexto Vivo.

## Reconciliação de continuidade

A `GE2-SYNC-007` concluiu a leitura do estado atual do repositório e a comparação com o extrato final da conversa anterior.

Resultados:

- nenhuma decisão arquitetural madura ausente foi identificada;
- Contexto Vivo e Market Validation estavam incorporados;
- divergências editoriais demonstráveis foram autorizadas para correção;
- formulário e planilha de validação permanecem entregáveis operacionais futuros;
- o ponto de retomada do Product Engineering foi preservado e avançado para os KPIs e critérios de desempenho funcional do Contexto Vivo.

## Progresso das capacidades do Journey

| Capacidade | Estado | Progresso de referência |
|---|---|---|
| 01 — Captura de Contexto | Substantially complete | 95% |
| 02 — Contexto Vivo | In progress | 96% |
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

1. KPIs, indicadores de qualidade e critérios de desempenho funcional;
2. cenários ideal, alternativo e limite;
3. contrato da capacidade.
