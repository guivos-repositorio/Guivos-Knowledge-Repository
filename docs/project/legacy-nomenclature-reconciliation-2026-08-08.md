---
id: GKR-LEGACY-NOMENCLATURE-RECONCILIATION-001
title: Reconciliação transversal de nomenclaturas legadas — 2026-08-08
status: in-progress
version: 0.1.0
owner: Guivos
last_updated: 2026-08-08
---

# Reconciliação transversal de nomenclaturas legadas — 2026-08-08

## 1. Objetivo

Este registro governa a etapa `P1.1 — Reconciliação de Nomenclaturas Legadas` da ressincronização ampla do Guivos Knowledge Repository.

O objetivo é impedir que nomenclaturas substituídas continuem sendo apresentadas como autoridade vigente em documentos, tabelas, jornadas, superfícies, wireframes, exemplos, matrizes, arquitetura de produto ou materiais públicos do GKR.

A limpeza não deve destruir evidência histórica. Termos antigos podem permanecer quando o documento for inequivocamente histórico, superseded, arquivado ou quando a própria autoridade canônica precisar registrar a substituição.

## 2. Baseline auditada

- repositório: `guivos-repositorio/Guivos-Knowledge-Repository`;
- branch-base: `main`;
- SHA-base: `9a0de25e664aab65b83c76ca5414c444dad893ae`;
- data da baseline: `2026-08-08`;
- autoridade principal de planos: `GEM-004-PLAN-TAXONOMY-CONCEPTUAL-AUTHORITY-001`;
- integração que consolidou a autoridade corrente: PR `#207`.

## 3. Taxonomia vigente de planos

| Papel / produto | Taxonomia vigente |
|---|---|
| Pessoa | Free · Plus · Pro |
| Coletivo | Livre · Mobiliza · Impacta · Rede |
| Organização | Conecta · Eleva · Transforma |
| Guivos Business | Start · Growth · Scale · Enterprise |

Regras estruturais obrigatórias:

- `Pessoa`, `Coletivo` e `Organização` são papéis estruturais de participante;
- `Guivos Business` é Produto Especializado/contrato e não um quarto tipo de participante;
- `Organização ≠ Guivos Business`;
- `Organização Transforma ≠ Guivos Business Enterprise`;
- escolha de plano representa profundidade, capacidade, escopo e complexidade de serviço, nunca valor humano, mérito ou status da pessoa.

## 4. Substituições já comprovadas

As seguintes nomenclaturas são legadas quando usadas para afirmar a taxonomia atual:

| Nomenclatura legada | Autoridade vigente |
|---|---|
| Coletivo Gestão | Coletivo Mobiliza |
| Coletivo Impacto | Coletivo Impacta |
| Coletivo Enterprise | Coletivo Rede |
| Organização Start | Organização Conecta |
| Organização Growth | Organização Eleva |
| Organização Scale | Organização Transforma |

`Start`, `Growth`, `Scale` e `Enterprise` não são termos globalmente obsoletos. Eles permanecem vigentes exclusivamente como tiers do Produto Especializado `Guivos Business`. Por isso, qualquer ocorrência desses tokens exige classificação por contexto antes de alteração.

## 5. Regra de correção

A reconciliação segue quatro classes:

1. **autoridade corrente incorreta** — corrigir para a nomenclatura vigente;
2. **derivado corrente incorreto** — corrigir e alinhar ao documento de autoridade;
3. **evidência histórica legítima** — preservar, mantendo a condição histórica explícita;
4. **ocorrência ambígua** — não substituir automaticamente; abrir revisão semântica.

É proibida substituição textual cega de palavras genéricas como `gestão`, `impacto`, `rede`, `Start`, `Growth`, `Scale` ou `Enterprise` fora de contexto de plano/tier.

## 6. Escopo transversal

A auditoria deve alcançar, quando aplicável:

- autoridades econômicas e de planos;
- arquitetura de produtos;
- Guivos Journey e matrizes de integração;
- arquitetura de experiência e UXA;
- registros de superfícies, estados e transições;
- wireframes e SVGs com labels textuais;
- GTM, targets, pricing e projeções;
- documentos públicos e glossário;
- material de arquitetura empresarial;
- exemplos e tabelas derivados;
- registros de projeto e roadmaps históricos, preservando sua natureza de evidência.

## 7. Controle mecânico

Foi introduzido `scripts/validate_legacy_nomenclature.py` e integrado ao workflow `GKR Mechanical Validation`.

O gate:

- bloqueia nomenclatura comprovadamente legada quando afirmada em superfície corrente;
- informa ocorrências históricas/referenciais sem falhá-las;
- sinaliza `Start/Growth/Scale/Enterprise` fora de contextos explicitamente Business/econômicos/GTM para revisão humana;
- evita mass-replace semântico.

O primeiro ciclo do gate é também instrumento de inventário: as ocorrências reveladas pelo CI serão classificadas individualmente antes do fechamento desta etapa.

## 8. Critério de conclusão da P1.1

A etapa somente pode ser considerada concluída quando:

1. todas as violações vivas conhecidas estiverem corrigidas;
2. ocorrências ambíguas relevantes tiverem sido classificadas;
3. referências históricas legítimas estiverem preservadas de forma inequívoca;
4. nenhum documento corrente reatribuir `Start/Growth/Scale` a Organização;
5. nenhum documento corrente usar os nomes antigos de Coletivo como taxonomia vigente;
6. `Organization ≠ Guivos Business` permanecer preservado em todos os derivados tocados;
7. o gate mecânico passar;
8. os demais gates semântico e mecânico do GKR permanecerem verdes.

## 9. Relação com a ressincronização ampla

A P1.1 antecede P2–P9 para evitar propagação de taxonomia obsoleta às próximas consolidações.

Depois de concluída, a sequência recomendada permanece:

`P2 → P8 → P3 → P4 → P5 → P6 → reconciliação P7 → P9`.

Nenhuma implantação técnica, contratação, campanha, alteração societária, investimento ou merge é autorizado por este registro.
