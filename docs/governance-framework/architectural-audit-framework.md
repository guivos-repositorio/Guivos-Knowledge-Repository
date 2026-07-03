---
id: GEA-AUDIT-001
title: Architectural Audit Framework
status: validated
version: 1.0.0
owner: Guivos Enterprise Architecture
last_updated: 2026-07-02
scope: Cross-Architecture Governance
---

# Architectural Audit Framework

## Finalidade

Definir o processo transversal de auditoria que verifica a integridade de uma revisão arquitetural antes de sua baseline.

A auditoria não cria conhecimento, não substitui a validação e não altera decisões. Ela verifica se o conjunto produzido é íntegro, coerente, rastreável e governável.

## Posição no ciclo

```text
Evidence Analysis
  -> Evidence Matrix
  -> Canonical Consolidation
  -> Readiness Assessment
  -> Architectural Validation
  -> Architectural Audit
  -> Baseline
```

## Princípios

1. auditoria verifica; não redesenha;
2. validação decide; auditoria testa a integridade da decisão;
3. nenhuma baseline pode ser congelada com não conformidade crítica aberta;
4. toda conclusão deve ser sustentada por evidência documental;
5. o rigor da auditoria deve ser proporcional à permanência do ativo;
6. o método somente evolui quando sua aplicação revela limitação objetiva.

## Escopo mínimo

| Dimensão | Verificação |
|---|---|
| Documental | Artefatos obrigatórios existem e estão no estado correto |
| Terminológica | Termos e identificadores são consistentes |
| Estrutural | Dependências e ordem do pipeline estão corretas |
| Semântica | Não há conflito material entre fontes, consolidação e decisão |
| Rastreabilidade | Elementos consolidados retornam às evidências de origem |
| Metodológica | Nenhuma etapa obrigatória foi omitida ou invertida |
| Governança | Status, versão, owner, data, decisão e baseline são explícitos |
| Navegação | Site, roadmap, board e changelog refletem o estado aprovado |

## Evidências obrigatórias

Uma revisão somente pode ser auditada quando possuir, conforme aplicável:

- Evidence Analysis;
- Evidence Matrix;
- Canonical Consolidation;
- Readiness Assessment;
- Architectural Validation;
- Decision Log;
- registro de riscos e recomendações;
- proposta de baseline.

## Classificação de não conformidades

| Classe | Definição | Efeito |
|---|---|---|
| Critical | Compromete decisão, rastreabilidade ou integridade da arquitetura | Bloqueia baseline |
| Major | Lacuna relevante de consistência ou governança | Exige correção antes da baseline |
| Minor | Desvio sem impacto material na decisão | Pode ser corrigido com plano registrado |
| Observation | Oportunidade de melhoria sem não conformidade | Não bloqueia |

## Checklist padrão

### Integridade documental

- [ ] Todos os artefatos obrigatórios existem.
- [ ] Identificadores, títulos, versões e status são consistentes.
- [ ] As entradas e saídas de cada etapa estão explícitas.

### Integridade semântica

- [ ] Não existem contradições materiais não resolvidas.
- [ ] Nenhum elemento foi promovido além da força das evidências.
- [ ] Absorções, fusões, refinamentos e remoções possuem justificativa.

### Rastreabilidade

- [ ] Todos os elementos consolidados possuem origem.
- [ ] Toda decisão formal referencia os artefatos avaliados.
- [ ] Riscos e limitações permanecem visíveis.

### Governança

- [ ] A validação precede a auditoria.
- [ ] A auditoria precede a baseline.
- [ ] Nenhuma hipótese foi promovida implicitamente à Canon.
- [ ] Atualizações de navegação e controle estão previstas.

## Resultado

A auditoria produz um relatório específico da revisão com um dos estados:

| Resultado | Significado |
|---|---|
| PASS | Nenhuma não conformidade Critical ou Major aberta |
| PASS WITH MINOR FINDINGS | Apenas desvios Minor ou Observations registrados |
| FAIL | Existe não conformidade Critical ou Major aberta |

## Saída mínima do relatório

```text
Audit target: <review>
Evidence set: <artefatos>
Critical findings: <n>
Major findings: <n>
Minor findings: <n>
Observations: <n>
Result: PASS | PASS WITH MINOR FINDINGS | FAIL
Baseline authorization: YES | NO
```

## Regra de baseline

Uma baseline somente pode ser congelada quando:

1. a validação estiver aprovada;
2. a auditoria resultar em `PASS` ou `PASS WITH MINOR FINDINGS`;
3. não houver achado Critical ou Major aberto;
4. riscos residuais estiverem documentados;
5. os controles do repositório estiverem prontos para atualização.

## Governança do framework

Este framework é transversal e reutilizável. Ele não deve ser duplicado por arquitetura. Cada revisão produz apenas seu relatório de auditoria.

Alterações no framework exigem limitação objetiva demonstrada em aplicação prática e registro formal de decisão.