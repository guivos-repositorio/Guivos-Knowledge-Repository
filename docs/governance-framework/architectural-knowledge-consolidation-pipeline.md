---
id: A2-METHOD-001
title: Architectural Knowledge Consolidation Pipeline
status: validated
version: 1.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-07-04
scope: GKR and GEA
---

# A2-METHOD-001 — Architectural Knowledge Consolidation Pipeline

## Finalidade

Definir o processo oficial pelo qual conhecimento arquitetural evolui desde uma fonte documental até sua eventual promoção à Canon.

O pipeline protege a rastreabilidade, evita promoção prematura de hipóteses, reduz redundâncias e separa claramente descoberta, convergência, consolidação, validação e publicação canônica.

## Modos oficiais

### Discovery Mode

É o modo de investigação arquitetural.

Permite:

- questionar conceitos existentes;
- extrair evidências;
- registrar observações;
- identificar regularidades;
- formular hipóteses;
- buscar contraexemplos;
- fundir, refinar, adiar ou rejeitar candidatos.

Nenhum conteúdo produzido em Discovery Mode é automaticamente canônico.

### Canon Mode

É o modo de preservação e publicação arquitetural.

Permite apenas:

- consolidar conhecimento com suporte suficiente;
- atualizar rastreabilidade;
- corrigir inconsistências comprovadas;
- registrar decisões formais;
- publicar novas versões e baselines.

A passagem de Discovery Mode para Canon Mode exige evidência, consolidação, validação e governança formal.

## Fluxo oficial

```text
Fonte oficial
  -> Evidence Extraction
  -> Observações
  -> Regularidades
  -> Hipóteses
  -> Testes e revisão
  -> Evidence Matrix
  -> Canonical Consolidation
  -> Readiness Assessment
  -> Architectural Validation
  -> Architectural Audit
  -> Baseline / Canon
```

## Etapas

### 1. Fonte oficial

Documento ou corpus submetido à análise.

Deve preservar conteúdo, versão, estado, ownership e localização rastreável.

### 2. Evidence Extraction

Extrai apenas aquilo que o corpus afirma explicitamente.

Cada evidência deve conter:

- identificador;
- fonte e localização;
- trecho literal;
- elementos explícitos.

Interpretação não pertence a esta etapa.

### 3. Observações

Registram fatos verificáveis identificados nas evidências.

Toda observação deve indicar quais evidências a sustentam.

### 4. Regularidades

Agrupam padrões recorrentes sustentados por múltiplas observações.

Regularidade não é hipótese e não é Canon.

### 5. Hipóteses

Explicações provisórias para as regularidades encontradas.

Hipóteses devem permanecer separadas de decisões validadas e ser submetidas a explicações alternativas, incompatibilidades e contraexemplos.

### 6. Evidence Matrix

Consolida evidências, observações, regularidades, hipóteses e resultados de revisão entre fontes.

Cada agrupamento deve ser avaliado segundo frequência, centralidade, consistência, confirmação, ampliação, ausência, contradição e independência das fontes.

### 7. Canonical Consolidation

Transforma o inventário provisório em um conjunto mínimo e suficiente.

Cada item recebe uma decisão:

| Decisão | Significado |
|---|---|
| Preserve | Mantém-se praticamente inalterado |
| Merge | É fundido a item equivalente |
| Refine | Permanece com redação ou fronteira aprimorada |
| Split | Contém mais de uma responsabilidade ou natureza |
| Remove | É redundante, circunstancial ou sem suporte suficiente |
| Defer | Depende de evidências ou arquiteturas ainda não disponíveis |

### 8. Readiness Assessment

Verifica se o conjunto consolidado está pronto para sustentar validação e arquiteturas dependentes.

### 9. Architectural Validation

Avalia cobertura, coerência, lacunas, conflitos, ambiguidades, dependências e riscos.

### 10. Architectural Audit

Verifica aplicação do método, rastreabilidade, integridade dos registros e aderência às decisões superiores.

### 11. Baseline e Canon

Somente conhecimento consolidado, validado, auditado e governado pode ser incorporado à Canon ou congelado em baseline.

## Princípios obrigatórios

### Primazia da evidência

Nenhum conceito, capacidade, relação ou camada pode ser promovido por preferência, elegância ou recorrência terminológica isolada.

### Primazia da realidade

Os documentos representam a realidade arquitetural descoberta. Quando evidências consolidadas demonstrarem inadequação documental, o documento deve ser revisado por processo formal.

### Convergência antes da consolidação

Um único trecho pode gerar uma evidência, mas não autoriza sozinho a promoção de um conceito permanente.

### Separação de camadas

Evidência, observação, regularidade, hipótese, consolidação e Canon são estados distintos e não podem ser tratados como equivalentes.

### Hipóteses fora da Canon

Hipóteses podem orientar investigação, mas devem permanecer explicitamente identificadas até validação.

### Rastreabilidade integral

Toda decisão arquitetural deve ser rastreável às fontes, evidências, análises e decisões que a sustentam.

### Suficiência arquitetural

O objetivo é produzir o menor conjunto capaz de explicar integralmente o domínio sem perda relevante de significado.

### Estabilidade durante a execução

O método permanece congelado durante um ciclo de análise. Alterações exigem limitação prática comprovada.

## Estados de maturidade

| Estado | Definição |
|---|---|
| Extracted | Evidência literal registrada |
| Observed | Observação ligada a evidências |
| Patterned | Regularidade identificada |
| Hypothesized | Explicação provisória registrada |
| Corroborated | Hipótese reforçada por múltiplas fontes |
| Consolidated | Elemento deduplicado e estabilizado |
| Under Review | Elemento submetido à revisão arquitetural |
| Validated | Elemento aprovado pela validação aplicável |
| Canonical | Elemento incorporado formalmente à Canon |
| Rejected | Elemento rejeitado com justificativa |
| Deferred | Elemento adiado por dependência ou insuficiência |

## Aplicabilidade

O pipeline pode ser aplicado a:

- Foundation Architecture;
- Fundamental Model;
- Core Capability Model;
- Business Architecture;
- Product Architecture;
- Guivos Economic Model;
- Intelligence Architecture;
- Data, Technology, Governance e Knowledge Architectures;
- revisões transversais da GEA.

## Aplicação vigente

A aplicação ativa ocorre em `A2-R02 — Fundamental Model Review`, por meio do documento `A2-R02-FMEM-001 — Fundamental Model Evidence Matrix`.

O corpus principal é composto por `KU-FM-001`, `KU-FM-002` e `KU-FM-003`. A extração de evidências ainda não foi iniciada.

## Limites

Este método governa a maturação do conhecimento arquitetural. Ele não substitui métodos especializados de pesquisa, modelagem, engenharia, implementação ou operação.