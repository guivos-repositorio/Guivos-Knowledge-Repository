---
id: GKR-CLAIMS-TRACE-001
title: Rastreabilidade Git das Alegações Acumuladas
status: draft
version: 0.5.3
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-STATE-001
  - GKR-AUD-ACCUMULATED-003
  - GKR-SOURCE-INTAKE-001
related:
  - GPA-000
  - GPA-002
  - GEM-009
  - GEM-010
  - GEM-010-A2
  - PAS-001-CV-CONTRACT-001
  - BA-STR-002-CODR-001
  - VAL-002
  - VAL-006
  - VAL-007
  - ADR-006
  - A2-METHOD-001
  - GEA-AUDIT-001
  - GKR-LINEAGE-GC-CON-001-001
  - GKR-EXT-GOV-DISPOSITION-001
  - GKR-EXT-CV-RECON-001
  - GKR-VAL-OPS-AUD-001
normative: false
---

# Rastreabilidade Git das Alegações Acumuladas

## 1. Finalidade

Este documento vincula alegações registradas em conversas e fontes externas a evidências verificáveis no GitHub e às disposições formais produzidas durante o P0.

Uma evidência comprova somente o que o arquivo, commit, pull request ou resolução declara. Ela não amplia maturidade, não transforma hipótese em resultado e não autoriza implementação, operação, oferta, cobrança ou publicação externa.

## 2. Baseline e método

A verificação foi realizada em 2026-08-05 contra:

- `main` em `6280022eaf2c4153dafd0528acd24b2d219e0c18`;
- histórico de commits e pull requests;
- conteúdo atual dos arquivos integrados;
- fontes externas catalogadas no intake;
- decisões de linhagem, disposição e reconciliação deste PR.

O método inclui localização, inspeção, confirmação de ancestralidade, leitura de status e limites, comparação com autoridades, reconstrução de linhagem e disposição explícita.

Uma busca sem resultado não prova inexistência. O estado aplicável é `not_located`.

## 3. Estados de verificação

| Estado | Significado |
|---|---|
| `verified_integrated` | integrado à ancestralidade da `main` |
| `verified_proposed` | localizado em PR aberto |
| `verified_historical` | histórico ou substituído |
| `partially_verified` | parte comprovada, parte pendente |
| `not_located` | não localizado na baseline pesquisada |
| `external_only` | localizado somente fora do GKR |
| `lineage_conflicted` | colisão externa de ID, versão ou status |
| `superseded_external` | proposta externa substituída |
| `operational_evidence_pending` | desenho existe, execução não comprovada |
| `quarantined` | promoção bloqueada |

## 4. Matriz de rastreabilidade

| Claim | Alegação auditada | Evidência | Resultado | Limite preservado |
|---|---|---|---|---|
| CLM-001 | O P1 foi criado e está em revisão | PR nº 163; head `3191a7326c022336617b2dffbc7f632cccb1592f` | `verified_proposed` | draft e não integrado |
| CLM-002 | GEM-009 foi integrado | PR nº 55; merge `e73bb3509e5ec987129e231b737df38c83c52512` | `verified_integrated` | métricas documentais; sem resultados reais |
| CLM-003 | GEM-010 foi integrado | PR nº 56; merge `a2d7aed787c36e94f77afb7bc77d2c0a84f56720` | `verified_integrated` | arquitetura conceitual |
| CLM-004 | Opportunity Boost possui preços definidos | commit `e5f757a9917dfe4ce025a98267eb0f33d628d314` | `partially_verified` | faixas candidatas; sem oferta ou cobrança |
| CLM-005 | A COEM foi concluída | PR nº 72 | `verified_integrated` | 18 candidatos; nenhum Outcome |
| CLM-006 | Contexto Vivo foi funcionalmente concluído | commits `73ea9e7` e `05b0504` | `verified_integrated` | conclusão documental, não produto implementado |
| CLM-007 | `PAS-001-CV-CONTRACT-001` é autoridade | contrato 1.0.0 integrado | `verified_integrated` | rascunhos externos não o substituem |
| CLM-008 | VAL-002 está em 2.1.0 | PR nº 42 | `verified_integrated` | instrumento não comprova aplicação |
| CLM-009 | VAL-006 está em 1.3.1 | arquivo atual da `main` | `verified_integrated` | modelo de cálculo, não resultado |
| CLM-010 | VAL-007 está em 1.3.1 | arquivo atual da `main` | `verified_integrated` | decisão exige pré-teste e 200 respostas válidas |
| CLM-011 | VAL externos 1.1.0 são vigentes | comparação com a `main` | `verified_historical` | versões externas superadas |
| CLM-012 | GEM-009 contém resultados econômicos reais | arquivo e PR nº 55 | `partially_verified` | taxonomia existe; resultados não |
| CLM-013 | GEM-010 representa orçamento oficial | PR nº 56 | `partially_verified` | cenários não autorizam orçamento ou valuation |
| CLM-014 | `GC-CON-001` está integrado | busca Git + inventário externo | `lineage_conflicted` | nenhuma release canônica reconhecida |
| CLM-015 | PDF `GKR-001` é a autoridade atual | comparação com autoridades integradas | `verified_historical` | princípios parcialmente absorvidos |
| CLM-016 | Neo4j foi implantado | fonte externa SRC-004 | `external_only` | recomendação não comprova operação |
| CLM-017 | Proteção corporativa foi executada | plano externo SRC-005 | `external_only` | plano não comprova ativos |
| CLM-018 | Fundação está constituída | conversas SRC-018 e SRC-019 | `not_located` | conceito não equivale a entidade |
| CLM-019 | Guivos opera internacionalmente | conversas SRC-020 a SRC-022 | `not_located` | canais isolados não comprovam operação |
| CLM-020 | UXA-071 foi iniciada | `GKR-STATE-001` e ausência de artefato | `not_located` | permanece não iniciada |
| CLM-021 | Product Engineering foi retomada | `GKR-STATE-001` | `not_located` | pausa antes de W0-01 |
| CLM-022 | Existe Outcome empresarial canônico | estado atual e COR | `not_located` | candidatos não são Outcomes |
| CLM-023 | `ECO-CAND-001` foi aprovado | PR nº 73 | `partially_verified` | `Reformulate`; continua `Under Validation` |
| CLM-024 | Marketplace permanece nome oficial | commit `a68bab2` | `verified_historical` | Mall é oficial |
| CLM-025 | Sete componentes oficiais estão definidos | `GPA-000` 1.30.0 | `verified_integrated` | arquitetura não prova operação |
| CLM-026 | Existe uma única versão externa `GC-CON-001 1.0` | múltiplos PDFs incompatíveis | `lineage_conflicted` | 1.0 não reconhecida; ID bloqueado |
| CLM-027 | Resolução editorial encerrou PDFs incrementais | `GC-EDT-001` 2.0 | `verified_historical` | alinhada à prática, não política integrada |
| CLM-028 | Draft externo descreve o GKR atual | comparação com ADR-006 e `main` | `superseded_external` | arquitetura federada substituiu a proposta |
| CLM-029 | `GC-GOV-001` é governança vigente | draft externo 0.1 | `external_only` | papéis organizacionais não comprovados |
| CLM-030 | `GC-EDT-002` é backlog autorizado | família externa 0.1 a 0.3 | `external_only` | plano não autoriza roadmap atual |
| CLM-031 | Árvore externa representa implementação atual | comparação com estrutura real | `superseded_external` | layout histórico não comprova produtos |
| CLM-032 | O princípio de evolução independente do rascunho não foi incorporado | contrato final, regra 365 e dimensões da seção 350 | `verified_integrated` | núcleo foi absorvido; PDF não é autoridade |
| CLM-033 | A pesquisa B2C possui base operacional suficiente para decisão | busca Git e acervo; `GKR-VAL-OPS-AUD-001` | `operational_evidence_pending` | desenho pronto; pré-teste, coleta, base, KPIs e decisão não comprovados |

## 5. Correções decorrentes

A matriz confirma:

1. GEM-009, GEM-010, COEM, Contexto Vivo e produtos possuem os limites registrados;
2. instrumentos VAL atuais substituem drafts externos;
3. Guivos Mall e os sete componentes são autoridades documentais;
4. `GC-CON-001` permanece bloqueado por colisão;
5. `GKR-001` é antecedente histórico, não autoridade vigente;
6. arquitetura e árvore externas estão substituídas;
7. `GC-GOV-001` e `GC-EDT-002` permanecem externos;
8. o núcleo do rascunho do Contexto Vivo foi absorvido pelo contrato final;
9. o rascunho não reabre a Capacidade 02;
10. readiness VAL não equivale a execução ou resultado;
11. Neo4j, proteção, Fundação e internacionalização permanecem sem promoção.

## 6. Lacunas restantes do P0

- inventário físico e hashes de `GC-CON-001`;
- eventual comparação temática do corpus com autoridades integradas;
- evidências operacionais VAL;
- inventário restrito de marcas, domínios e ativos;
- prova jurídica e territorial;
- varredura de materiais Marketplace;
- runbook GitHub/Codex;
- classificação de sensibilidade das fontes externas.

A comparação do Contexto Vivo e a disposição geral de governança estão concluídas no nível necessário ao P0.

## 7. Regra de uso

Resumos futuros deverão preservar o estado e o limite de cada claim.

Exemplos corretos:

- “ECO-CAND-001 foi reformulado e continua em validação”;
- “os PDFs GC-CON-001 têm linhagem conflitante”;
- “o rascunho do Contexto Vivo antecedeu regras absorvidas pelo contrato final”;
- “o programa VAL está documentalmente pronto, mas sem evidência operacional suficiente”.

## 8. Checkpoint congelado

```text
Claims trace: GKR-CLAIMS-TRACE-001 0.5.3
Source intake reference: GKR-SOURCE-INTAKE-001 0.5.4
Claims traced: 33
Unqualified promotions allowed: 0
Current-state changes: 0
```

## 9. Declaração de não promoção

Esta rastreabilidade não altera marco, versões ou autoridades. Ela reduz erro de continuidade e promoção sem prova.
