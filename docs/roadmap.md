---
id: ROADMAP-12.67.0
title: Roadmap Arquitetural — Central de Atualizações Validada
status: active
version: 12.67.0
owner: Guivos
last_updated: 2026-08-07
supersedes_partial:
  - ROADMAP-12.66.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-055
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.81
---

# Roadmap Arquitetural — Central de Atualizações Validada

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Central de Atualizações validada e TRN-110 fechada; PER-108 permanece próximo bloqueio | UXA-094; M7.81 |
| Registros granulares | 40 superfícies e 37 transições | UXA-094 |
| Galeria visual | `active` 0.13.0; 107 SVGs | UXA-094 |
| página de Coletivos | `active` 0.11.0 | UXA-094 |
| matriz por SVG | 107 arquivos / 27 perfis; `active` 0.11.0 | UXA-094 |
| validações funcionais vigentes de SVG | **97** | UXA-094 e pacotes anteriores |
| pendentes de validação específica | **10, exclusivamente UXA-055** | UXA-055; UXA-094 |
| handoffs integralmente validados em Coletivos | **7** | UXA-090; UXA-092; UXA-094 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência governada

```text
UXA-086 — COL-002 materializada
→ UXA-087 — COL-002 validada
→ UXA-088 — COL-003 materializada
→ UXA-089 — COL-003 validada
→ UXA-090 — cinco handoffs validados
→ UXA-091 — PER-106 materializada
→ UXA-092 — PER-106 e TRN-108 validadas
→ UXA-093 — PER-107 materializada
→ UXA-094 — PER-107 validada e TRN-110 validada ponta a ponta
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-094

| Dimensão | Resultado |
|---|---|
| GKR-SURF-PER-106 | permanece validado após reformulação do gatilho |
| GKR-SURF-PER-107 | validado após reformulação controlada |
| SVGs reformulados | 2 existentes; 0 novos |
| GKR-TRN-110 | `integralmente validada` |
| GKR-TRN-111 | `ausente` |
| GKR-SURF-PER-108 | reformulação/materialização pendente |
| SVGs totais | 107 |
| perfis | 27 |
| validações vigentes | 97 |
| pendentes | 10, exclusivamente UXA-055 |
| jornadas promovidas | 0 |
| Engenharia iniciada | não |

## 5. Contrato validado da Central

A Central mantém origem, natureza, contexto, autoridade, leitura, ação e prazo separados. Segurança material precede ação comum. Preferências podem modular atenção não essencial, mas não ocultar entrega mínima necessária de aviso essencial de segurança.

`Lido` não significa concordância, consentimento, presença, aceitação, resposta ou conclusão.

## 6. Continuidade validada

```text
PER-106 — Meus Coletivos
→ “Ver atualizações”
→ entrada neutra, sem alterar vínculo ou leitura
→ PER-107 — Central de Atualizações
→ ação substantiva revalida estado canônico
→ retorno seguro para PER-106
```

Abertura, retorno, recarga ou confirmação de leitura repetida não podem duplicar efeito lógico.

## 7. Trilha governada de Coletivos

```text
COL-002 — validada
→ TRN-112 — integralmente validada
→ COL-003 — validada
↔ TRN-105/106/107/109 — integralmente validadas
→ TRN-108 — integralmente validada
→ PER-106 — validado
→ TRN-110 — integralmente validada
→ PER-107 — validado
→ TRN-111 — ausente
→ PER-108 — reformulação/materialização pendente
```

## 8. Dívidas preservadas

- `PER-108` e `TRN-111`;
- P0B da Central: vazio, excesso de volume e baixa conectividade;
- P0B adicional de Meus Coletivos;
- áreas P1 de comunicação especializada;
- dez estados residuais da UXA-055;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- operação interna restante do Coletivo.

## 9. Limites

A UXA-094 não materializa `PER-108`, não valida `TRN-111`, não cria SVG/ID/transição, não promove jornadas e não inicia protótipo, teste com pessoas ou Engenharia.

## 10. Próxima iniciativa possível

> **UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`**

A UXA-095 depende de autorização separada e não é iniciada por este pacote.
