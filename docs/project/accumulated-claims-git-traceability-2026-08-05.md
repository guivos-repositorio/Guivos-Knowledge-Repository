---
id: GKR-CLAIMS-TRACE-001
title: Rastreabilidade Git das Alegações Acumuladas
status: draft
version: 0.3.0
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
normative: false
---

# Rastreabilidade Git das Alegações Acumuladas

## 1. Finalidade

Este documento vincula alegações registradas em conversas e fontes externas a evidências verificáveis no GitHub.

A existência de uma evidência Git comprova somente o que o arquivo, commit ou pull request declara. Ela não amplia maturidade, não transforma hipótese em resultado e não autoriza implementação, operação, oferta, cobrança ou publicação externa.

## 2. Baseline e método

A verificação foi realizada em 2026-08-05 contra:

- repositório `guivos-repositorio/Guivos-Knowledge-Repository`;
- `main` no commit `6280022eaf2c4153dafd0528acd24b2d219e0c18`;
- histórico de commits e pull requests do repositório;
- conteúdo atual dos arquivos na `main`;
- fontes externas catalogadas em `GKR-SOURCE-INTAKE-001`.

Foram utilizados:

1. localização do identificador ou termo;
2. inspeção do commit ou pull request;
3. confirmação de merge ou ancestralidade na `main`;
4. localização do path atual;
5. leitura de status, versão, escopo e limites;
6. comparação com a alegação acumulada.

Uma busca sem resultado não comprova ausência absoluta. Nesses casos, o resultado é registrado como `não localizado na baseline pesquisada`, e não como inexistente.

## 3. Estados de verificação

| Estado | Significado |
|---|---|
| `verified_integrated` | evidência localizada e integrada à ancestralidade da `main` |
| `verified_proposed` | evidência localizada em PR aberto, ainda não integrada |
| `verified_historical` | evidência localizada, mas superada por versão posterior |
| `partially_verified` | parte da alegação foi comprovada; parte permanece sem evidência |
| `not_located` | identificador ou artefato não localizado na baseline pesquisada |
| `external_only` | fonte localizada apenas fora do repositório |
| `quarantined` | item não pode ser promovido sem decisão governada própria |

## 4. Matriz de rastreabilidade

| Claim | Alegação auditada | Evidência Git | Path ou superfície | Resultado | Limite preservado |
|---|---|---|---|---|---|
| CLM-001 | O P1 foi criado e está em revisão | PR nº 163; head auditado `3191a7326c022336617b2dffbc7f632cccb1592f` | branch `agent/p1-global-semantic-resynchronization` | `verified_proposed` | PR permanece draft e não integrado |
| CLM-002 | GEM-009 foi integrado | PR nº 55; merge `e73bb3509e5ec987129e231b737df38c83c52512` | `docs/economic-model/gem-009-economic-metrics.md` | `verified_integrated` | métricas permanecem documentais; sem valores reais, metas ou resultados |
| CLM-003 | GEM-010 foi integrado | PR nº 56; merge `a2d7aed787c36e94f77afb7bc77d2c0a84f56720` | família GEM-010 em `docs/economic-model/` | `verified_integrated` | arquitetura conceitual; parâmetros, orçamento e aprovações pendentes |
| CLM-004 | O Opportunity Boost possui preços definidos | commit `e5f757a9917dfe4ce025a98267eb0f33d628d314` na ancestralidade da `main` | `docs/economic-model/gem-010-a2-opportunity-boost-pricing-budget-and-measurement.md` | `partially_verified` | existem faixas candidatas; não há tabela pública, oferta, checkout, faturamento ou implementação autorizados |
| CLM-005 | A COEM foi concluída | PR nº 72; merge `2c836a4b373e7428455bad3b49411f365d9936d3` | `docs/business-architecture/strategy/candidate-outcome-register.md` | `verified_integrated` | cobertura de 18 candidatos concluída; nenhum Outcome canônico ou autorização operacional criado |
| CLM-006 | O Contexto Vivo foi funcionalmente concluído | commits `73ea9e7ab44a7314323a2a54b9bbe2576098229a` e `05b05041c9586193b704ab3822f8755b9b5879f9`, ambos ancestrais da `main` | `docs/product-architecture/pas-001-contexto-vivo-cenarios-contrato-final.md` | `verified_integrated` | conclusão documental da Capacidade 02; não equivale a produto implementado |
| CLM-007 | `PAS-001-CV-CONTRACT-001` 1.0.0 é autoridade do Contexto Vivo | front matter do contrato final no commit `73ea9e7ab44a7314323a2a54b9bbe2576098229a` | mesmo path do CLM-006 | `verified_integrated` | rascunhos externos devem ser comparados com esta extensão normativa e não substituí-la |
| CLM-008 | VAL-002 está na versão 2.1.0 | PR nº 42; merge `859ea63f93ed68a5243929d7d2a8fd2a487145ea` | `docs/research/market-validation/VAL-002-pesquisa-oficial-da-guivos.md` | `verified_integrated` | instrumento pronto para pré-teste; não comprova aplicação, amostra ou resultado |
| CLM-009 | VAL-006 está na versão 1.3.1 | arquivo atual da `main` | `docs/research/market-validation/VAL-006-dashboard-de-indicadores.md` | `verified_integrated` | dashboard define cálculo e maturidade da base; não contém resultados empresariais comprovados |
| CLM-010 | VAL-007 está na versão 1.3.1 | arquivo atual da `main` | `docs/research/market-validation/VAL-007-criterios-de-decisao.md` | `verified_integrated` | decisão formal exige pré-teste, base elegível e ao menos 200 respostas válidas |
| CLM-011 | Os documentos VAL 1.1.0 do rascunho externo são vigentes | comparação com CLM-008 a CLM-010 | fontes externas catalogadas como SRC-013 e SRC-014 | `verified_historical` | versões externas não devem ser reutilizadas como instrumento oficial |
| CLM-012 | GEM-009 contém resultados econômicos reais | leitura do arquivo atual e do PR nº 55 | `docs/economic-model/gem-009-economic-metrics.md` | `partially_verified` | taxonomia e fórmulas existem; valores reais, baselines empíricas, metas e sustentabilidade comprovada não existem nessa autoridade |
| CLM-013 | GEM-010 representa orçamento ou previsão oficial | leitura do PR nº 56 | família GEM-010 | `partially_verified` | contrato de cenários existe; não autoriza orçamento, valuation, captação, dívida, preço ou projeção oficial |
| CLM-014 | O corpus `GC-CON-001` está integrado como autoridade vigente | buscas exatas de código e commits sem resultado na baseline | variantes externas catalogadas como SRC-010 | `not_located` | múltiplas variantes externas permanecem em quarentena até resolução de linhagem |
| CLM-015 | `GKR-001 — Governança do GKR` externo é a autoridade integrada | fonte externa catalogada como SRC-006; vínculo Git exato ainda não localizado | acervo externo | `external_only` | status “aprovado” dentro do PDF não substitui integração e autoridade no repositório |
| CLM-016 | A arquitetura Neo4j foi implantada | fonte externa catalogada como SRC-004; nenhuma prova de provisionamento analisada neste P0 | acervo externo | `external_only` | documento é recomendação para P2; não comprova contratação, migração, segurança ou operação |
| CLM-017 | A proteção corporativa foi executada | plano externo catalogado como SRC-005 | acervo externo | `external_only` | plano não comprova registro de marca, domínio, DNS, certificado ou titularidade |
| CLM-018 | Fundação Guivos está constituída e operando | conversas catalogadas como SRC-018 e SRC-019 | sem evidência Git ou jurídica vinculada | `not_located` | conceito e intenção permanecem separados de entidade jurídica e programa ativo |
| CLM-019 | A Guivos já opera internacionalmente | conversas catalogadas como SRC-020 a SRC-022 | sem matriz territorial de evidências vinculada | `not_located` | domínio, número, perfil ou cadastro isolado não comprovam operação |
| CLM-020 | UXA-071 foi iniciada | `GKR-STATE-001` 1.99.0 e ausência de artefato UXA-071 na baseline | Registro do Estado Atual | `not_located` | UXA-071 permanece não iniciada; a seção integrada de telas não pertence ao P0 |
| CLM-021 | Product Engineering foi retomada | `GKR-STATE-001` 1.99.0 | Registro do Estado Atual | `not_located` | Engenharia de Produto permanece pausada antes de W0-01 |
| CLM-022 | Existe Outcome empresarial canônico | Registro do Estado Atual e limites do Candidate Outcome Register | superfícies de estado e estratégia | `not_located` | candidatos e validações não equivalem a Outcome empresarial canônico |
| CLM-023 | `ECO-CAND-001` foi aprovado como Outcome | PR nº 73; merge `765faa4d790a495229dc85727f0512e13f612f1d` | `docs/business-architecture/strategy/candidate-outcome-decision-register.md` | `partially_verified` | decisão humana aceitou `Reformulate`; candidato permanece `Under Validation`, sem código canônico, AQS-O01 ou Outcome aprovado |
| CLM-024 | Guivos Marketplace permanece o nome oficial | commit `a68bab26be82b428c491cbd15915536e960f1a61` na ancestralidade da `main` | `docs/product-architecture/mall.md` | `verified_historical` | `Guivos Mall` substituiu `Guivos Marketplace`; o nome anterior permanece apenas como `former_name` ou referência histórica |
| CLM-025 | A estrutura oficial é Journey, Mall, Travel, Business, Media, Intelligence e Ads | arquivo `GPA-000` 1.30.0 na `main` | `docs/product-architecture/index.md` | `verified_integrated` | consolidação arquitetural dos componentes não comprova implementação ou operação comercial de todos eles |

## 5. Correções decorrentes

A matriz permite corrigir as seguintes classificações do intake:

1. GEM-009 deixa de ser alegação e passa a `verified_integrated`;
2. GEM-010 deixa de ser alegação e passa a `verified_integrated`;
3. COEM deixa de ser alegação e passa a `verified_integrated`, sem Outcome;
4. Contexto Vivo e seu contrato final passam a `verified_integrated`;
5. VAL-002, VAL-006 e VAL-007 passam a usar as versões atuais da `main`;
6. o rascunho VAL externo 1.1.0 passa a `verified_historical`;
7. preços do Opportunity Boost passam a ser descritos somente como parâmetros candidatos;
8. `ECO-CAND-001` passa a ter decisão `Reformulate` verificada, mantendo `Under Validation`;
9. `Guivos Mall` é confirmado como nome oficial, com Marketplace apenas como nome anterior;
10. os sete componentes oficiais são confirmados no nível arquitetural;
11. `GC-CON-001` permanece bloqueado por risco de colisão e ausência de vínculo Git resolvido;
12. Neo4j, proteção corporativa, Fundação e internacionalização permanecem sem promoção.

## 6. Lacunas restantes do P0

Ainda precisam de reconciliação específica:

- lineage completo das variantes `GC-CON-001`;
- relação entre o documento externo `GKR-001` e a governança atualmente integrada;
- localização e classificação do draft histórico da arquitetura do GKR;
- destino do plano editorial `GC-EDT-002` e do draft `GC-GOV-001`;
- comparação do rascunho externo do Contexto Vivo com a extensão normativa integrada;
- confirmação de evidência operacional de pré-teste, formulário publicado, coleta e base VAL;
- inventário restrito de marcas, domínios e ativos efetivamente titulados;
- prova jurídica e operacional de iniciativas institucionais ou territoriais;
- varredura de materiais externos que ainda usam `Guivos Marketplace`;
- separação formal do runbook GitHub/Codex do conhecimento arquitetural.

## 7. Regra de uso

Qualquer resumo futuro que mencione uma alegação desta matriz deverá preservar o estado e o limite da mesma linha.

Exemplos:

- correto: “GEM-010 possui arquitetura conceitual integrada; parâmetros e aprovações permanecem pendentes”;
- incorreto: “o modelo financeiro está aprovado”;
- correto: “a COEM cobriu 18 candidatos sem criar Outcome canônico”;
- incorreto: “os resultados empresariais foram validados”;
- correto: “existem preços candidatos documentados para o Opportunity Boost”;
- incorreto: “a Guivos já vende o Opportunity Boost”;
- correto: “ECO-CAND-001 foi reformulado e continua em validação”;
- incorreto: “ECO-CAND-001 é um Outcome aprovado”;
- correto: “Guivos Mall é o nome oficial; Guivos Marketplace é histórico”;
- incorreto: “Mall e Marketplace são dois produtos vigentes”.

## 8. Declaração de não promoção

Esta rastreabilidade não altera versões, status, marco ou autoridade dos documentos verificados. Ela registra a relação entre alegações e evidências para reduzir repetição, erro de continuidade e promoção sem prova.
