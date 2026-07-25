---
id: ROADMAP-11.47.0
title: Roadmap Arquitetural — Sequência Global Reconciliada
status: active
version: 11.47.0
owner: Guivos
last_updated: 2026-07-24
supersedes_partial:
  - ROADMAP-11.46.0
  - ROADMAP-11.45.0
related:
  - GKR-STATE-001
  - GKR-AUD-002
  - GKR-REMEDIATION-002
  - M7.3.1
---

# Roadmap Arquitetural — Sequência Global Reconciliada

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do GKR. O estado transversal vigente é declarado pelo [GKR-STATE-001 — Current State Register](project/current-state-register.md).

Roadmaps e overlays anteriores permanecem no histórico, mas não substituem esta sequência.

## 2. Estado atual

| Elemento | Estado |
|---|---|
| Era | `GE-2 — Knowledge` |
| Marco | `M7.3.1` |
| Frente de controle | remediação documental do GKR |
| R1 — Precedência e estado global | concluído neste incremento |
| R2 — Roadmap e backlog global | concluído neste incremento |
| R3 — Controles centrais | próximo incremento |
| R4 — Navegação | pendente |
| R5 — Validação mecânica | pendente |
| R6 — Retomada governada | bloqueado até resultado `PASS` |
| Frente arquitetural preservada | `A2-R03 — Business Architecture Review` |
| Product Engineering | pausado antes do `W0-01` |

## 3. Sequência executada

### 3.1 Guivos Journey

**Estado:** concluído funcionalmente e publicado.

- `PAS-001 1.0.0 active`;
- nove capacidades funcionalmente concluídas;
- mapa final publicado;
- handoff e planejamento da Onda 0 preservados;
- implementação e W0-01 pausados.

### 3.2 Guivos Economic Model

**Estado:** arquitetura documental inicial concluída.

- módulos `GEM-001` a `GEM-010` encerrados documentalmente;
- revisão de fechamento com resultado `PASS`;
- parâmetros reais, preços, custos, validação empírica, especialidades e operação permanecem pendentes;
- o domínio somente será reaberto por condição material formalmente registrada.

A conclusão do Economic Model definiu a A2-R03 como próxima frente porque Outcomes e Business Capabilities antecedem organização, processos, ofertas e execução.

## 4. Frente de controle atual

A auditoria `GKR-AUD-002` confirmou a integridade da rota e identificou divergências entre documentos centrais e overlays recentes.

A remediação `GKR-REMEDIATION-002` ocorre antes da continuidade da A2-R03:

```text
R1 — precedência e estado global — concluído
→ R2 — roadmap e backlog global — concluído
→ R3 — controles centrais
→ R4 — navegação
→ R5 — validação mecânica
→ R6 — retomada governada
```

## 5. Próxima frente arquitetural retomada

Após o `PASS` da auditoria de correção, retomar `BA-STR-002 — Business Outcomes`:

1. continuar as decisões humanas individuais no Candidate Outcome Decision Register;
2. submeter `ECO-CAND-003` à próxima decisão;
3. concluir as dezessete decisões restantes;
4. reavaliar as formulações reformuladas pelos quatro testes da COEM;
5. aplicar e ajustar o `AQS-O01`;
6. consolidar o catálogo de Ecosystem Outcomes;
7. consolidar o catálogo de Business Outcomes;
8. construir a matriz canônica de sustentação.

Estado atual do ciclo:

- COEM: `18 de 18` candidatos e `6 de 6` clusters;
- decisões humanas: `1 de 18`;
- Outcomes canônicos: `0`;
- `ECO-CAND-001`: `Reformulate` aceito, permanecendo `Under Validation`.

## 6. Business Capabilities

Após a conclusão governada dos Outcomes:

1. desenvolver `BA-CAP-001 — Core Business Capabilities`;
2. desenvolver `BA-CAP-002 — Capability Map`;
3. confirmar dependências, ownership e fronteiras entre capacidades;
4. utilizar o mapa para rebaselinear o portfólio especializado.

Business Capabilities não poderão ser inferidas diretamente dos produtos existentes nem iniciadas antes do gate do `BA-STR-002`.

## 7. Portfólio especializado

A ordem histórica permanece preservada como referência:

1. Guivos Mall;
2. Guivos Business;
3. Guivos Intelligence;
4. Guivos Ads;
5. Guivos Media;
6. Guivos Travel.

Essa ordem não é ainda uma autorização de início. Ela será confirmada ou ajustada após Outcomes e Business Capabilities, considerando:

- valor e transformação sustentados;
- dependências funcionais;
- papéis econômicos já definidos no `GEM-007`;
- capacidade organizacional e operacional;
- riscos e proteção do ecossistema;
- evidências de Market Validation.

Guivos Journey permanece o produto arquitetural já concluído e não integra novamente o backlog de especificação funcional.

## 8. Commercial Model

O Commercial Model será desenvolvido após o rebaseline mínimo do portfólio e deverá transformar autoridades econômicas e de negócio em decisões comerciais governadas, sem confundir:

- família de receita com oferta aprovada;
- arquétipo de plano com preço;
- parceiro elegível com contrato ativo;
- papel econômico com ownership societário;
- cenário financeiro com previsão oficial.

## 9. Go-to-Market

O Go-to-Market será desenvolvido após o Commercial Model e dependerá de:

- proposta de valor validável;
- segmentos e contextos prioritários;
- canais e relações comerciais governados;
- capacidade de entrega e suporte;
- métricas, gates e critérios de interrupção;
- conformidade jurídica, regulatória, fiscal, contábil e de dados aplicável.

## 10. Product Engineering

Product Engineering somente poderá ser retomado por decisão explícita que defina motivo estratégico, escopo, owners, orçamento, capacidade, dependências econômicas e critérios de interrupção.

Até essa decisão:

- `W0-01` permanece em `0%`;
- POCs, ambientes e integrações não são iniciados;
- produção permanece não autorizada;
- a readiness já documentada não é descartada.

## 11. Trilha operacional paralela — Market Validation

Os seguintes entregáveis permanecem pendentes e podem ser executados em incremento próprio, sem substituir a prioridade arquitetural:

1. formulário definitivo de aplicação;
2. planilha automática de tratamento;
3. cálculo de KPIs e Índice Geral de Validação;
4. gates e classificação de aceitação;
5. registro de decisão e evidências.

Os resultados deverão alimentar Outcomes, priorização do portfólio, Economic Model, Commercial Model e Go-to-Market sem promover respostas de pesquisa diretamente à Canon.

## 12. Reconciliação do backlog histórico

| Item histórico | Estado reconciliado |
|---|---|
| concluir funcionalmente o Journey | concluído |
| desenvolver o Guivos Economic Model | concluído documentalmente; validações reais pendentes |
| especificar Mall, Business, Intelligence, Ads, Media e Travel | preservado após Outcomes e Business Capabilities |
| desenvolver Commercial Model | preservado como ciclo posterior |
| desenvolver Go-to-Market | preservado como ciclo posterior ao Commercial Model |
| formulário definitivo de validação | pendente em trilha operacional paralela |
| planilha automática de validação | pendente em trilha operacional paralela |

## 13. Próximo incremento autorizado

Executar `R3 — Controles centrais` do `GKR-REMEDIATION-002`, reconciliando Knowledge Board, Architectural Milestones, Canonical Consolidation Matrix e referências de changelog.

A decisão sobre `ECO-CAND-003` permanece bloqueada até a conclusão de R3, R4 e R5 e o resultado `PASS` da auditoria de correção.
