---
id: GKR-CLAIMS-TRACE-001
title: Rastreabilidade Git das Alegações Acumuladas
status: draft
version: 0.4.0
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
normative: false
---

# Rastreabilidade Git das Alegações Acumuladas

## 1. Finalidade

Este documento vincula alegações registradas em conversas e fontes externas a evidências verificáveis no GitHub e às disposições formais produzidas durante o P0.

A existência de uma evidência comprova somente o que o arquivo, commit, pull request ou resolução de intake declara. Ela não amplia maturidade, não transforma hipótese em resultado e não autoriza implementação, operação, oferta, cobrança ou publicação externa.

## 2. Baseline e método

A verificação foi realizada em 2026-08-05 contra:

- repositório `guivos-repositorio/Guivos-Knowledge-Repository`;
- `main` no commit `6280022eaf2c4153dafd0528acd24b2d219e0c18`;
- histórico de commits e pull requests;
- conteúdo atual dos arquivos na `main`;
- fontes externas catalogadas em `GKR-SOURCE-INTAKE-001`;
- decisões de linhagem e disposição registradas neste PR.

Foram utilizados:

1. localização do identificador ou termo;
2. inspeção do commit ou pull request;
3. confirmação de merge ou ancestralidade na `main`;
4. localização do path atual;
5. leitura de status, versão, escopo e limites;
6. comparação com a alegação acumulada;
7. reconstrução de linhagem externa quando não havia autoridade Git;
8. disposição explícita entre fonte histórica e autoridade vigente.

Uma busca sem resultado não comprova ausência absoluta. Nesses casos, o resultado é `not_located`, e não prova de inexistência.

## 3. Estados de verificação

| Estado | Significado |
|---|---|
| `verified_integrated` | evidência localizada e integrada à ancestralidade da `main` |
| `verified_proposed` | evidência localizada em PR aberto, ainda não integrada |
| `verified_historical` | evidência localizada, mas histórica ou substituída |
| `partially_verified` | parte da alegação foi comprovada; parte permanece sem evidência |
| `not_located` | identificador ou artefato não localizado na baseline pesquisada |
| `external_only` | fonte localizada apenas fora do repositório |
| `lineage_conflicted` | família externa possui colisão de ID, versão ou status |
| `superseded_external` | proposta externa substituída por autoridades integradas posteriores |
| `quarantined` | item não pode ser promovido sem decisão governada própria |

## 4. Matriz de rastreabilidade

| Claim | Alegação auditada | Evidência | Path ou superfície | Resultado | Limite preservado |
|---|---|---|---|---|---|
| CLM-001 | O P1 foi criado e está em revisão | PR nº 163; head auditado `3191a7326c022336617b2dffbc7f632cccb1592f` | branch `agent/p1-global-semantic-resynchronization` | `verified_proposed` | PR permanece draft e não integrado |
| CLM-002 | GEM-009 foi integrado | PR nº 55; merge `e73bb3509e5ec987129e231b737df38c83c52512` | `docs/economic-model/gem-009-economic-metrics.md` | `verified_integrated` | métricas documentais; sem valores reais, metas ou resultados |
| CLM-003 | GEM-010 foi integrado | PR nº 56; merge `a2d7aed787c36e94f77afb7bc77d2c0a84f56720` | família GEM-010 | `verified_integrated` | arquitetura conceitual; parâmetros e aprovações pendentes |
| CLM-004 | O Opportunity Boost possui preços definidos | commit `e5f757a9917dfe4ce025a98267eb0f33d628d314` | `gem-010-a2-opportunity-boost-pricing-budget-and-measurement.md` | `partially_verified` | faixas candidatas; nenhuma oferta, cobrança ou implementação autorizada |
| CLM-005 | A COEM foi concluída | PR nº 72; merge `2c836a4b373e7428455bad3b49411f365d9936d3` | Candidate Outcome Register | `verified_integrated` | 18 candidatos avaliados; nenhum Outcome canônico |
| CLM-006 | O Contexto Vivo foi funcionalmente concluído | commits `73ea9e7ab44a7314323a2a54b9bbe2576098229a` e `05b05041c9586193b704ab3822f8755b9b5879f9` | `pas-001-contexto-vivo-cenarios-contrato-final.md` | `verified_integrated` | conclusão documental; não equivale a produto implementado |
| CLM-007 | `PAS-001-CV-CONTRACT-001` 1.0.0 é autoridade do Contexto Vivo | front matter e histórico Git | mesmo path do CLM-006 | `verified_integrated` | rascunhos externos não substituem a extensão normativa |
| CLM-008 | VAL-002 está na versão 2.1.0 | PR nº 42; merge `859ea63f93ed68a5243929d7d2a8fd2a487145ea` | `VAL-002-pesquisa-oficial-da-guivos.md` | `verified_integrated` | instrumento não comprova aplicação, amostra ou resultado |
| CLM-009 | VAL-006 está na versão 1.3.1 | arquivo atual da `main` | `VAL-006-dashboard-de-indicadores.md` | `verified_integrated` | define cálculo; não contém resultados comprovados |
| CLM-010 | VAL-007 está na versão 1.3.1 | arquivo atual da `main` | `VAL-007-criterios-de-decisao.md` | `verified_integrated` | decisão formal exige pré-teste e ao menos 200 respostas válidas |
| CLM-011 | Os documentos VAL 1.1.0 externos são vigentes | comparação com CLM-008 a CLM-010 | fontes externas SRC-013 e SRC-014 | `verified_historical` | versões externas estão superadas |
| CLM-012 | GEM-009 contém resultados econômicos reais | arquivo e PR nº 55 | `gem-009-economic-metrics.md` | `partially_verified` | taxonomia e fórmulas existem; resultados reais não |
| CLM-013 | GEM-010 representa orçamento ou previsão oficial | PR nº 56 | família GEM-010 | `partially_verified` | cenários não autorizam orçamento, valuation ou captação |
| CLM-014 | `GC-CON-001` está integrado como autoridade vigente | busca Git sem resultado + inventário externo + resolução de linhagem | `GKR-LINEAGE-GC-CON-001-001` | `lineage_conflicted` | nenhum PDF externo é reconhecido como release canônica |
| CLM-015 | `GKR-001 — Governança do GKR` externo é a autoridade atual | comparação com `GKR-STATE-001`, `ADR-006`, `A2-METHOD-001`, `GEA-AUDIT-001` e controles do Git | `GKR-EXT-GOV-DISPOSITION-001` | `verified_historical` | princípios parcialmente absorvidos; PDF não é autoridade vigente |
| CLM-016 | A arquitetura Neo4j foi implantada | fonte externa SRC-004 | acervo externo | `external_only` | recomendação não comprova contratação, migração ou operação |
| CLM-017 | A proteção corporativa foi executada | plano externo SRC-005 | acervo externo | `external_only` | plano não comprova marca, domínio, DNS ou certificado |
| CLM-018 | Fundação Guivos está constituída e operando | conversas SRC-018 e SRC-019 | sem evidência jurídica vinculada | `not_located` | conceito não equivale a entidade constituída |
| CLM-019 | A Guivos já opera internacionalmente | conversas SRC-020 a SRC-022 | sem matriz territorial de evidências | `not_located` | domínio, número ou cadastro não comprovam operação |
| CLM-020 | UXA-071 foi iniciada | `GKR-STATE-001` e ausência de artefato | Registro do Estado Atual | `not_located` | UXA-071 permanece não iniciada |
| CLM-021 | Product Engineering foi retomada | `GKR-STATE-001` | Registro do Estado Atual | `not_located` | pausa antes de W0-01 preservada |
| CLM-022 | Existe Outcome empresarial canônico | estado atual e Candidate Outcome Register | superfícies de estado | `not_located` | candidatos não equivalem a Outcome canônico |
| CLM-023 | `ECO-CAND-001` foi aprovado como Outcome | PR nº 73; merge `765faa4d790a495229dc85727f0512e13f612f1d` | Candidate Outcome Decision Register | `partially_verified` | `Reformulate` aceito; permanece `Under Validation` |
| CLM-024 | Guivos Marketplace permanece o nome oficial | commit `a68bab26be82b428c491cbd15915536e960f1a61` | `docs/product-architecture/mall.md` | `verified_historical` | Guivos Mall é oficial; Marketplace é `former_name` |
| CLM-025 | A estrutura oficial é Journey, Mall, Travel, Business, Media, Intelligence e Ads | `GPA-000` 1.30.0 | `docs/product-architecture/index.md` | `verified_integrated` | arquitetura documental não comprova operação comercial |
| CLM-026 | Existe uma única versão externa `GC-CON-001 1.0` final | múltiplos PDFs `v1.0` com planejamento, manuscritos, blocos, partes e consolidação | `GKR-LINEAGE-GC-CON-001-001` | `lineage_conflicted` | versão 1.0 não reconhecida; ID bloqueado para importação direta |
| CLM-027 | A resolução editorial externa encerrou PDFs incrementais | `GC-EDT-001` 2.0 | fonte externa e disposição P0 | `verified_historical` | regra está alinhada à prática; documento externo não é política integrada |
| CLM-028 | O draft externo de arquitetura descreve o GKR atual | comparação com ADR-006, arquiteturas atuais e estrutura da `main` | `GKR-EXT-GOV-DISPOSITION-001` | `superseded_external` | proposta estática foi substituída pela arquitetura federada |
| CLM-029 | `GC-GOV-001` define a governança institucional vigente | draft externo 0.1 | `GKR-EXT-GOV-DISPOSITION-001` | `external_only` | conselhos, curadoria e squads não são estruturas comprovadas |
| CLM-030 | `GC-EDT-002` é o backlog editorial autorizado | família externa 0.1 a 0.3 | `GKR-EXT-GOV-DISPOSITION-001` | `external_only` | plano editorial não autoriza roadmap, volume ou prioridade atual |
| CLM-031 | A árvore externa chamada `Guivos Knowledge Repository` representa a implementação atual | comparação com a estrutura real da `main` | `GKR-EXT-GOV-DISPOSITION-001` | `superseded_external` | layout é histórico e não comprova produtos ou diretórios vigentes |

## 5. Correções decorrentes

A matriz corrige as seguintes classificações:

1. GEM-009 e GEM-010 são integrados, com limites explícitos;
2. COEM e `ECO-CAND-001` possuem evidência Git sem Outcome aprovado;
3. Contexto Vivo e seu contrato final são autoridades integradas;
4. VAL-002, VAL-006 e VAL-007 utilizam as versões atuais da `main`;
5. rascunhos VAL externos 1.1.0 são históricos;
6. preços do Opportunity Boost são parâmetros candidatos;
7. Guivos Mall e os sete componentes oficiais são confirmados documentalmente;
8. a família `GC-CON-001` recebe estado `external_lineage_conflicted`;
9. nenhum arquivo externo `GC-CON-001 v1.0` é release reconhecida;
10. `GKR-001` é fonte histórica parcialmente absorvida, não autoridade atual;
11. a arquitetura externa do repositório e sua árvore são propostas substituídas;
12. `GC-GOV-001` e `GC-EDT-002` permanecem drafts externos;
13. Neo4j, proteção corporativa, Fundação e internacionalização permanecem sem promoção.

## 6. Lacunas restantes do P0

Ainda precisam de tratamento:

- inventário físico completo e hashes da família `GC-CON-001`;
- comparação conceitual do corpus externo com autoridades integradas;
- comparação do rascunho externo do Contexto Vivo com a extensão normativa;
- evidência operacional de pré-teste, formulário, coleta e base VAL;
- inventário restrito de marcas, domínios e ativos titulados;
- prova jurídica e operacional de iniciativas institucionais ou territoriais;
- varredura de materiais externos que ainda usam `Guivos Marketplace`;
- separação formal do runbook GitHub/Codex;
- classificação de sensibilidade antes de armazenar fontes externas.

A autoridade e a disposição dos documentos gerais de governança e arquitetura já estão resolvidas no P0; somente a preservação física e eventual extração temática permanecem opcionais.

## 7. Regra de uso

Qualquer resumo futuro deverá preservar o resultado e o limite da linha correspondente.

Exemplos:

- correto: “GEM-010 possui arquitetura conceitual integrada; parâmetros e aprovações permanecem pendentes”;
- incorreto: “o modelo financeiro está aprovado”;
- correto: “a COEM cobriu 18 candidatos sem criar Outcome canônico”;
- incorreto: “os resultados empresariais foram validados”;
- correto: “ECO-CAND-001 foi reformulado e continua em validação”;
- incorreto: “ECO-CAND-001 é um Outcome aprovado”;
- correto: “Guivos Mall é o nome oficial; Guivos Marketplace é histórico”;
- incorreto: “Mall e Marketplace são dois produtos vigentes”;
- correto: “os PDFs GC-CON-001 são fontes históricas com linhagem conflitante”;
- incorreto: “GC-CON-001 v1.0 está aprovado no GKR”;
- correto: “GKR-001 antecipou princípios posteriormente absorvidos”;
- incorreto: “o PDF GKR-001 governa atualmente todo o repositório”.

## 8. Declaração de não promoção

Esta rastreabilidade não altera versões, marco, status ou autoridade das arquiteturas. Ela reduz erro de continuidade e promoção sem prova.
