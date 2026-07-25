---
id: ROADMAP-11.48.0
title: Roadmap Arquitetural — Sequência Global Reconciliada
status: active
version: 11.48.0
owner: Guivos
last_updated: 2026-07-24
supersedes_partial:
  - ROADMAP-11.47.0
related:
  - GKR-STATE-001
  - GKR-AUD-002
  - GKR-REMEDIATION-002
  - M7.3.2
---

# Roadmap Arquitetural — Sequência Global Reconciliada

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do GKR. O estado transversal vigente é declarado pelo [GKR-STATE-001 — Current State Register](project/current-state-register.md).

Roadmaps e overlays anteriores permanecem no histórico, mas não substituem esta sequência.

## 2. Estado atual

| Elemento | Estado |
|---|---|
| Era | `GE-2 — Knowledge` |
| Marco | `M7.3.2` |
| Frente de controle | remediação documental do GKR |
| R1 — Precedência e estado global | concluído |
| R2 — Roadmap e backlog global | concluído |
| R3 — Controles centrais | concluído neste incremento |
| R4 — Navegação | próximo incremento |
| R5 — Validação mecânica | pendente |
| R6 — Retomada governada | bloqueado até resultado `PASS` |
| Achados Major abertos | 1 — navegação oficial incompleta |
| Frente arquitetural preservada | `A2-R03 — Business Architecture Review` |
| Product Engineering | pausado antes do `W0-01` |

## 3. Sequência já executada

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

## 4. Remediação do GKR

A auditoria `GKR-AUD-002` confirmou a integridade da rota e identificou divergências entre documentos centrais e overlays recentes.

```text
R1 — precedência e estado global — concluído
→ R2 — roadmap e backlog global — concluído
→ R3 — controles centrais — concluído
→ R4 — navegação
→ R5 — validação mecânica
→ R6 — retomada governada
```

R3 sincronizou Knowledge Board, Architectural Milestones, Matriz de Consolidação Canônica e o registro de reordenamento estratégico.

## 5. Próxima frente arquitetural retomada

Após o `PASS` da remediação, retomar `BA-STR-002 — Business Outcomes`:

1. submeter `ECO-CAND-003` à próxima decisão humana;
2. concluir as dezessete decisões restantes;
3. reavaliar as formulações `Reformulate` pelos quatro testes da COEM;
4. aplicar e ajustar o `AQS-O01`;
5. consolidar o catálogo de Ecosystem Outcomes;
6. consolidar o catálogo de Business Outcomes;
7. construir a matriz canônica de sustentação.

Estado atual:

- COEM: `18 de 18` candidatos e `6 de 6` clusters;
- decisões humanas: `1 de 18`;
- Outcomes canônicos: `0`;
- `ECO-CAND-001`: `Reformulate` aceito, permanecendo `Under Validation`.

## 6. Business Capabilities

Após a conclusão governada dos Outcomes:

1. desenvolver `BA-CAP-001 — Core Business Capabilities`;
2. desenvolver `BA-CAP-002 — Capability Map`;
3. confirmar dependências, ownership e fronteiras;
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

Essa ordem não é autorização de início. Será confirmada ou ajustada após Outcomes e Business Capabilities, considerando valor sustentado, dependências funcionais, papéis econômicos do `GEM-007`, capacidade operacional, riscos e evidências de mercado.

Guivos Journey permanece o produto arquitetural já concluído e não integra novamente o backlog de especificação funcional.

## 8. Commercial Model

Será desenvolvido após o rebaseline mínimo do portfólio e deverá transformar autoridades econômicas e de negócio em decisões comerciais governadas, sem confundir família de receita com oferta, arquétipo de plano com preço, parceiro elegível com contrato ou cenário financeiro com previsão oficial.

## 9. Go-to-Market

Será desenvolvido após o Commercial Model e dependerá de proposta de valor validável, segmentos prioritários, canais governados, capacidade de entrega, métricas, gates e conformidade aplicável.

## 10. Product Engineering

Somente poderá ser retomado por decisão explícita que defina motivo, escopo, owners, orçamento, capacidade, dependências econômicas e critérios de interrupção.

Até essa decisão:

- `W0-01` permanece em `0%`;
- POCs, ambientes e integrações não são iniciados;
- produção permanece não autorizada;
- a readiness documentada não é descartada.

## 11. Trilha operacional paralela — Market Validation

Podem ser executados em incremento próprio:

1. formulário definitivo de aplicação;
2. planilha automática de tratamento;
3. KPIs e Índice Geral de Validação;
4. gates e registro de decisão.

Essa trilha fornece evidências para produtos, Economic Model, Commercial Model e Go-to-Market, sem substituir a prioridade arquitetural.

## 12. Próximo ponto exato

Executar `R4 — Navegação`, atualizando `mkdocs.yml` e tornando os ativos vigentes acessíveis. Em seguida, executar R5 e somente retomar `ECO-CAND-003` se o parecer for `PASS`.
