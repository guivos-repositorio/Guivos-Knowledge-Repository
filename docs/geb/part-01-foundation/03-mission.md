---
id: GEB-P01-F03
title: Missão Operacional
status: approved-draft
version: 0.2.0
owner: Guivos
last_updated: 2026-07-01
dependencies:
  - 01-essence.md
  - 02-purpose.md
related_adrs:
  - ADR-002
---

# Missão Operacional

## Missão

Ajudar cada participante a evoluir continuamente por meio das oportunidades mais relevantes para seu momento de vida.

## Função da missão

A missão operacional traduz o propósito em critério de execução.

Enquanto o propósito responde por que a Guivos existe, a missão operacional responde como a plataforma atua diariamente.

## Critério de validação

Toda funcionalidade, produto, algoritmo, interface, campanha ou parceria deverá responder positivamente à pergunta:

> Esta decisão ajuda um participante a dar seu próximo passo de evolução?

Se a resposta for negativa, a decisão deve ser reavaliada.

## Consequência arquitetural

A missão operacional orienta diretamente:

- o modelo de jornada;
- o conceito de próximo passo;
- o modelo de oportunidades;
- a inteligência artificial;
- o desenho da experiência do usuário;
- a governança do ecossistema.

---

## Evidence Analysis — A2

### Estado da análise

| Campo | Valor |
|---|---|
| Fase | `A2 — Functional Architecture Discovery` |
| Data | 01/07/2026 |
| Resultado | Evidence Extraction concluída |
| Afirmações institucionais atômicas | 19 |
| Grupos de significado institucional | 5 |
| Invariantes provisórios | 5 |
| Responsabilidades institucionais | 6 |
| Core Capabilities promovidas | 0 |

### Significados institucionais

1. A missão traduz o propósito em execução diária.
2. O próximo passo de evolução é o principal critério operacional.
3. Decisões que não contribuam para a jornada devem ser reavaliadas.
4. Jornada, oportunidades, IA, experiência e governança devem permanecer alinhadas.
5. A relevância depende do momento de vida do participante.

### Invariantes provisórios

| ID | Invariante |
|---|---|
| INV-F03-01 | A execução diária deve permanecer orientada à evolução contínua do participante. |
| INV-F03-02 | Toda decisão relevante deve demonstrar contribuição para o próximo passo. |
| INV-F03-03 | Decisões sem aderência à jornada devem ser reavaliadas. |
| INV-F03-04 | IA e experiência do usuário devem permanecer subordinadas à missão. |
| INV-F03-05 | A governança do ecossistema deve operar segundo o propósito e a jornada. |

### Responsabilidades institucionais

| ID | Responsabilidade |
|---|---|
| RESP-F03-01 | Traduzir o propósito em critérios verificáveis de execução. |
| RESP-F03-02 | Avaliar decisões pela contribuição ao próximo passo de evolução. |
| RESP-F03-03 | Reavaliar funcionalidades, produtos, algoritmos, interfaces, campanhas e parcerias sem aderência. |
| RESP-F03-04 | Orientar o modelo de jornada e o modelo de oportunidades pela missão. |
| RESP-F03-05 | Orientar IA e experiência do usuário pela missão. |
| RESP-F03-06 | Governar o ecossistema segundo a jornada de evolução. |

### Evidence Convergence

A Missão reforça fortemente progressão da jornada e governança de aderência. Também amplia a subordinação tecnológica ao explicitar IA, algoritmo e experiência do usuário como elementos orientados pela missão.

O documento acrescenta duas formulações provisórias: tradução do propósito em execução diária e orientação de IA e UX pela missão.

Como depende da Essência e do Propósito e permanece em `approved-draft`, seu peso é de consolidação interna da Foundation.

### Confidence Assessment

| Critério | Avaliação |
|---|---|
| Consistência | Muito alta |
| Originalidade | Média |
| Relevância arquitetural | Muito alta |
| Impacto na convergência | Muito alto |

### Limites

Nenhuma Core Capability é criada. Os elementos operacionais citados permanecem evidências de responsabilidade e governança.