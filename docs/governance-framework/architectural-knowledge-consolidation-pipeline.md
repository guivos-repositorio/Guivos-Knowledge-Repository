---
id: A2-METHOD-001
title: Architectural Knowledge Consolidation Pipeline
status: validated
version: 1.0.0
owner: Guivos Enterprise Architecture
last_updated: 2026-07-02
scope: GKR and GEA
---

# A2-METHOD-001 — Architectural Knowledge Consolidation Pipeline

## Finalidade

Definir o processo oficial pelo qual conhecimento arquitetural evolui desde uma fonte documental até sua eventual promoção à Canon.

O pipeline protege a rastreabilidade, evita promoção prematura de hipóteses, reduz redundâncias e separa claramente extração, convergência, consolidação e validação.

## Fluxo oficial

```text
Documento Canônico
  -> Evidence Analysis
  -> Evidence Matrix
  -> Canonical Consolidation
  -> Architecture Review
  -> Architectural Decision / Validation
  -> Canon
```

## Etapas

### 1. Documento Canônico

Fonte oficial de conhecimento submetida à análise.

Responsabilidades:

- preservar o conteúdo normativo original;
- manter versão, estado, ownership e dependências;
- servir como origem rastreável das evidências.

### 2. Evidence Analysis

Analisa uma única fonte e extrai, quando aplicável:

- afirmações institucionais atômicas;
- significados institucionais;
- invariantes provisórios;
- responsabilidades provisórias;
- objetivos, estados desejados, decisões e relações;
- evidências funcionais, constitucionais, estruturais ou informacionais.

A Evidence Analysis não promove capacidades, não altera automaticamente a Canon e não cria novas camadas arquiteturais.

### 3. Evidence Matrix

Consolida evidências entre múltiplas fontes.

Cada agrupamento deve ser avaliado segundo:

- frequência;
- centralidade;
- consistência;
- confirmação;
- ampliação;
- ausência;
- contradição;
- força e independência das fontes.

A matriz organiza convergência. Ela não substitui a validação arquitetural.

### 4. Canonical Consolidation

Transforma o inventário provisório em um conjunto mínimo e suficiente.

Cada item deve receber uma decisão:

| Decisão | Significado |
|---|---|
| Preserve | Mantém-se praticamente inalterado |
| Merge | É fundido a item semanticamente equivalente |
| Refine | Permanece com redação ou fronteira aprimorada |
| Split | Contém mais de uma responsabilidade ou permanência |
| Remove | É redundante, circunstancial ou sem suporte suficiente |

A consolidação termina quando nenhuma fusão, redução, divisão, refinamento ou remoção adicional puder ocorrer sem perda arquitetural relevante.

### 5. Architecture Review

Avalia a arquitetura ou o conjunto consolidado como sistema.

A revisão deve verificar:

- cobertura;
- consistência;
- lacunas;
- conflitos;
- ambiguidades;
- sobreposições;
- conceitos órfãos;
- dependências;
- readiness para sustentar a próxima camada ou fase.

### 6. Architectural Decision / Validation

Registra formalmente o resultado da revisão.

O registro pode assumir a forma de:

- ADR, quando houver decisão arquitetural;
- AV, quando houver validação de estado arquitetural;
- gate de readiness, quando houver autorização para continuidade.

A decisão deve explicitar escopo, evidências, limitações, riscos, resultado e próximos passos.

### 7. Canon

Somente conhecimento suficientemente consolidado, validado e governado pode ser promovido à Canon.

A promoção deve preservar rastreabilidade até:

```text
Fonte
  -> Evidência
  -> Convergência
  -> Consolidação
  -> Validação
  -> Decisão
  -> Canon
```

## Princípios obrigatórios

### Evidência antes da nomeação

Nenhum conceito, capacidade ou camada deve ser criado apenas por elegância conceitual.

### Convergência antes da consolidação

Recorrência terminológica isolada não é suficiente. Frequência deve ser analisada com centralidade, consistência e independência das fontes.

### Consolidação antes da validação

A revisão arquitetural deve avaliar um conjunto já deduplicado e semanticamente coerente.

### Validação antes da Canon

Nenhum ativo entra na Canon apenas por ter sido documentado ou consolidado.

### Hipóteses fora da Canon

Hipóteses podem orientar observação, mas devem permanecer explicitamente separadas de evidências e decisões validadas.

### Rastreabilidade integral

Toda decisão arquitetural deve ser rastreável às fontes e evidências que a sustentam.

### Suficiência arquitetural

O objetivo é produzir o menor conjunto capaz de explicar integralmente o domínio, sem perda relevante de significado ou responsabilidade.

### Separação entre execução e evolução do método

O método permanece estável durante ciclos de execução. Alterações exigem limitação prática demonstrada, inconsistência comprovada ou melhoria superior validada.

## Estados de maturidade

| Estado | Definição |
|---|---|
| Observed | Evidência identificada em uma fonte |
| Corroborated | Evidência reforçada por múltiplas fontes |
| Consolidated | Elemento deduplicado e semanticamente estabilizado |
| Under Review | Elemento submetido à revisão arquitetural |
| Validated | Elemento aprovado pela revisão aplicável |
| Canonical | Elemento incorporado formalmente à Canon |
| Rejected | Elemento removido ou rejeitado com justificativa |
| Deferred | Elemento adiado por dependência ou insuficiência de evidência |

## Regras para capacidades

- nenhuma Capability nasce diretamente de um documento;
- nenhuma Capability nasce diretamente da Evidence Analysis;
- agrupamentos recorrentes não são automaticamente capacidades;
- candidatas exigem convergência entre fontes e fronteiras próprias;
- promoção exige testes de permanência, essencialidade, independência, reutilização, irredutibilidade e cobertura.

## Aplicabilidade

O pipeline pode ser aplicado a:

- Foundation Architecture;
- Ecosystem Architecture e GEB;
- Business Architecture;
- Product Architecture;
- Data & Intelligence Architecture;
- Technology Architecture;
- Governance Architecture;
- Knowledge Architecture;
- Reference Architectures;
- revisões transversais da GEA.

## Governança

- owner: Guivos Enterprise Architecture;
- alterações estruturais exigem registro de justificativa;
- adaptações locais não podem remover as etapas de convergência, consolidação e validação;
- o pipeline não substitui métodos especializados de pesquisa, modelagem ou implementação;
- o pipeline governa a maturação do conhecimento arquitetural, não a execução operacional.

## Aplicação inicial

A primeira aplicação integral ocorre na `A2-R01 — Foundation Architecture Review`:

1. Foundation Evidence Matrix;
2. Canonical Consolidation dos invariantes e responsabilidades;
3. Architecture Review;
4. validação de readiness;
5. decisão sobre avanço para o Modelo Fundamental.

## Limites

Este método não promove automaticamente `Architecture Reviews` a um domínio arquitetural independente, não cria um novo Evidence Registry e não altera o Permanence Layer Model. Sua função é governar a passagem de conhecimento analisado para conhecimento arquitetural validado.