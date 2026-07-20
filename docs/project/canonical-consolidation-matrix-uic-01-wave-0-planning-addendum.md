---
id: CANONICAL-CONSOLIDATION-MATRIX-UIC-01-W0-PLANNING-ADDENDUM
title: Matriz de Consolidação Canônica — Addendum de Planejamento da Onda 0
status: active
version: 1.37.0
owner: Guivos
last_updated: 2026-07-19
related:
  - PAS-001-CC-UIC-001
  - PAS-001-CC-W0-PLAN-001
  - PRODUCT-ARCHITECTURE-OVERLAY-1.37.0
  - M5.17
---

# Matriz de Consolidação Canônica — Addendum de Planejamento da Onda 0

> Este addendum preserva a matriz-base e todos os addenda anteriores. Prevalece apenas sobre estado de planejamento, marco, backlog de execução e ponto de retomada da UIC-01.

## 1. Precedência por tema

| Tema | Autoridade efetiva |
|---|---|
| domínio | PAS-001-CC-UIC-DOMAIN-001 |
| lifecycle | PAS-001-CC-UIC-LIFECYCLE-001 |
| contratos | PAS-001-CC-UIC-CONTRACTS-001 |
| schemas | PAS-001-CC-UIC-SCHEMAS-001 |
| armazenamento e índice | PAS-001-CC-UIC-STORAGE-INDEX-001 |
| guardrails e acesso | PAS-001-CC-UIC-GUARDRAILS-ACCESS-001 |
| NFR, SLO e threat model | PAS-001-CC-UIC-NFR-SECURITY-001 |
| readiness e gates | PAS-001-CC-UIC-READINESS-001 |
| plano da Onda 0 | PAS-001-CC-W0-PLAN-001 |
| backlog | PAS-001-CC-W0-BACKLOG-001 |
| dependências | PAS-001-CC-W0-DEPENDENCY-001 |
| ambientes e integração | PAS-001-CC-W0-ENV-001 |
| provas técnicas | PAS-001-CC-W0-POC-001 |
| evidências | PAS-001-CC-W0-EVIDENCE-001 |
| riscos e interrupções | PAS-001-CC-W0-RISK-001 |
| decisões tecnológicas | PAS-001-CC-W0-TECH-DECISIONS-001 |
| estado da UIC-01 | Unidade de Engenharia 0.6.0 |
| Engineering Handoff | 0.6.0 |
| estado global | Product Architecture 1.37.0 |
| Roadmap | 11.18.0 |
| Knowledge Board | 11.18.0 |
| marco | M5.17 |

## 2. Estado consolidado

| Elemento | Estado |
|---|---|
| UIC-01 | Draft 0.6.0 |
| Readiness arquitetural | 100% |
| Planejamento da Onda 0 | concluído |
| Implementação | não iniciada |
| Gaps arquiteturais abertos | 0 |
| Marco | M5.17 |
| Próxima decisão | autorizar W0-01 |

## 3. Conteúdo do plano

| Dimensão | Quantidade/estado |
|---|---|
| incrementos | 8 |
| histórias | 80 |
| dependências | 16 classificadas |
| ambientes | 6 |
| POCs | 6 |
| evidências | 18 |
| gates | 5 |
| riscos iniciais | 20 |
| dossiers tecnológicos | 10 |

## 4. Decisões preservadas

- `CaptureRecord` é o agregado;
- `CaptureSession` é entidade temporal interna;
- fato, interpretação e hipótese permanecem distintos;
- somente autoridade humana competente confirma;
- correção é compensatória;
- revogação bloqueia novos usos;
- índice e projeção não são sistema de registro;
- conteúdo multimodal fica separado do registro funcional;
- acesso depende de finalidade e autoridade;
- Intelligence não confirma nem autoriza;
- produção exige processo independente.

## 5. Não precede

Este addendum não substitui:

- PAS-001 1.0.0;
- Mapa Final de Capacidades 1.0.1;
- autoridades funcionais da Jornada;
- contratos e schemas 0.4.0;
- readiness 0.5.0;
- programa VAL;
- políticas corporativas futuras;
- decisão tecnológica formal.

## 6. Dossiers tecnológicos

ADR-TCC-001 a ADR-TCC-010 estão identificados como questões de decisão. Eles não são ADRs aceitos.

Uma decisão somente adquire precedência quando:

- possuir ADR próprio;
- apresentar evidência;
- declarar consequências;
- ser aprovada pela autoridade competente;
- não violar autoridade normativa superior.

## 7. Gaps

- `UIC01-GAP-001` a `UIC01-GAP-010` permanecem encerrados;
- novo gap técnico usa `UIC01-IMP-GAP-###`;
- novo gap não reabre automaticamente decisão arquitetural;
- conflito normativo exige Stop-L4 e decisão formal.

## 8. Interpretação obrigatória

- planning complete não equivale a execution authorized;
- 100% arquitetural não equivale a 100% de implementação;
- história planejada não equivale a comportamento existente;
- evidência planejada não equivale a evidência produzida;
- owner lógico não equivale a owner nominal;
- ambiente definido não equivale a ambiente provisionado;
- POC especificada não equivale a POC validada;
- dossier não equivale a ADR aceito.

## 9. Ponto de retomada

> Propor execução controlada do W0-01 — Fundação do Projeto, sem iniciar código, POCs ou ADRs automaticamente.