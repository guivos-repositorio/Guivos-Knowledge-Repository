---
id: ROADMAP-12.65.0
title: Roadmap Arquitetural — Meus Coletivos e Continuidade Pós-Aprovação Validadas
status: active
version: 12.65.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.64.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-055
  - UXA-056
  - UXA-059
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.79
---

# Roadmap Arquitetural — Meus Coletivos e Continuidade Pós-Aprovação Validadas

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Meus Coletivos e continuidade pós-aprovação validadas; Central de Atualizações permanece ausente | UXA-092; M7.79 |
| Registros granulares | 40 superfícies e 37 transições | UXA-080; UXA-092 |
| Galeria visual | `active` 0.11.0; 106 SVGs | UXA-092 |
| página de Coletivos | `active` 0.9.0 | UXA-092 |
| matriz por SVG | 106 arquivos / 26 perfis; `active` 0.9.0 | UXA-092 |
| validações funcionais vigentes de SVG | 96 | UXA-092 e pacotes anteriores |
| pendentes de validação específica | 10, exclusivamente UXA-055 | UXA-055; UXA-092 |
| handoffs integralmente validados no fluxo de solicitação | 6 | UXA-090; UXA-092 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência das Jornadas Integradas

```text
UXA-070 a UXA-075 — estruturação e promoção seletiva das Jornadas Integradas
→ UXA-076 a UXA-080 — registros granulares
→ UXA-081 a UXA-085 — galeria e matriz governadas
→ UXA-086 — COL-002 materializada
→ UXA-087 — COL-002 reformulada e validada
→ UXA-088 — COL-003 materializada
→ UXA-089 — COL-003 reformulada e validada
→ UXA-090 — cinco handoffs elegíveis validados ponta a ponta
→ UXA-091 — PER-106 materializada e continuidade pós-aprovação refinada
→ UXA-092 — PER-106 e resultado aprovado reformulados e validados; TRN-108 validada integralmente
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-092

| Dimensão | Resultado |
|---|---|
| GKR-SURF-PER-106 | validado após reformulação controlada |
| SVG de PER-106 | reformulado; nenhum novo ativo |
| estado aprovado de PER-105 | reformulado novamente e revalidado |
| GKR-TRN-108 | integralmente validada |
| GKR-TRN-110 | parcial; PER-107 ausente |
| GKR-SURF-PER-107 | ausente |
| GKR-SURF-PER-108 | reformulação pendente |
| SVGs totais | 106 |
| perfis totais | 26 |
| validações vigentes | 96 |
| pendentes | 10, exclusivamente UXA-055 |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato validado de Meus Coletivos

`PER-106` organiza estados independentes:

- Participando;
- Acompanhando;
- Solicitações;
- Convites;
- Participações pausadas;
- histórico quando necessário.

A superfície não apresenta essas categorias como progressão e não cria ranking, pontuação de engajamento, sequência obrigatória, função automática, autoridade automática, presença obrigatória ou notificação automática.

Informação pública mínima pode aparecer no próprio contexto do Coletivo, mas `PER-106` não cria contagem de não lidos e não substitui `PER-107 — Central de Atualizações`.

## 6. Continuidade pós-aprovação validada

```text
COL-003 — aprovação confirmada por autoridade vigente
→ resultado aprovado em PER-105
→ vínculo já formado
→ ação opcional “Ver em Meus Coletivos”
→ PER-106 — mesmo vínculo confirmado visível
```

A aprovação independe do clique posterior. A Pessoa pode escolher `Agora não` sem cancelar, enfraquecer ou repetir o vínculo. Reabrir `Meus Coletivos` não pode gerar segunda participação lógica.

## 7. Trilha governada

```text
COL-002 validada
→ TRN-112 integralmente validada
→ COL-003 validada
↔ TRN-105/106/107/109 integralmente validadas com PER-105
→ TRN-108 integralmente validada com PER-105 e PER-106
→ PER-106 validada
→ somente depois avaliar materialização de PER-107
```

## 8. Prioridade de Coletivos

```text
COL-002 — validada
→ COL-003 — validada
→ TRN-105/106/107/108/109/112 — integralmente validadas
→ PER-105 aprovado — reformulado e revalidado
→ PER-106 — validada
→ TRN-110 — parcial
→ PER-107 — ausente
→ PER-108 — reformulação pendente
```

## 9. Dívidas preservadas

- materialização de `PER-107 — Central de Atualizações`;
- estados P0B adicionais de `Meus Coletivos`;
- `PER-108` ainda não materializada na forma vigente;
- dez estados da UXA-055 sem validação;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- operação interna restante do Coletivo.

## 10. Limites

A UXA-092 não materializa `PER-107`, `PER-108` ou estados P0B adicionais de `PER-106`, não valida `TRN-110`, não cria novo SVG, ID ou transição, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia.

## 11. Próxima iniciativa possível

> **UXA-093 — Materialização Controlada da Central de Atualizações (`GKR-SURF-PER-107`)**

A UXA-093 depende de autorização separada e não é iniciada por este pacote.
