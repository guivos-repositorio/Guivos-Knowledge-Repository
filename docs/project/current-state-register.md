---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.21.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
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
  - UXA-095
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - ROADMAP-12.68.0
  - M7.82
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente quando o incremento correspondente estiver integrado ao ramo principal. Em caso de divergência, prevalece sobre resumos não normativos.

## 2. Estado global proposto pela UXA-095

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | Início do Participante materializado; TRN-111 observável e parcial | UXA-095; M7.82 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | 40 superfícies e 37 transições | UXA-076 a UXA-095 |
| Galeria visual | `active` 0.14.0; 108 SVGs | UXA-081 a UXA-095 |
| Página de Coletivos | `active` 0.12.0 | UXA-095 |
| Matriz por SVG | 108 arquivos / 28 perfis | UXA-083 a UXA-095 |
| Jornadas Integradas | `active` 0.23.0; Pessoa, Coletivo e Organização em `draft` | UXA-070 a UXA-095 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **108** |
| associações individuais | **108** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **96** |
| pendentes de validação específica | **12** |
| IDs granulares com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |

As doze pendências são: dez estados residuais UXA-055, o SVG corrente reformulado de `PER-107` e o novo `PER-108`.

## 4. Resultado da UXA-095

A UXA-095:

- cria `uxa-095-collective-participant-home-mobile.svg` como referência vigente de `PER-108`;
- reforma minimamente o SVG de `PER-107` para incluir `Abrir início do Coletivo`;
- não cria ID de superfície ou transição;
- não valida a nova superfície ou a nova versão visual da origem;
- promove somente `TRN-111` de `ausente` para `parcial`.

Veredito:

> **Materialização controlada concluída no escopo documental; validação funcional pendente.**

## 5. Continuidade representada

```text
PER-107 — Central de Atualizações
→ Pessoa escolhe “Abrir início do Coletivo”
→ vínculo, leitura, papel, presença e autoridade permanecem inalterados
→ PER-108 — Início do Participante
→ mesmo Coletivo e mesmo vínculo permanecem em contexto
```

A ligação ainda não possui validação integrada de retorno, concorrência, estado obsoleto, ações internas e interrupções.

## 6. Handoffs integralmente validados preservados

Sete transições permanecem integralmente validadas no trecho anterior:

- `GKR-TRN-105`;
- `GKR-TRN-106`;
- `GKR-TRN-107`;
- `GKR-TRN-108`;
- `GKR-TRN-109`;
- `GKR-TRN-110`;
- `GKR-TRN-112`.

`GKR-TRN-111` permanece **parcial**.

## 7. Prioridade operacional de Coletivos

| Ordem | Superfície ou continuidade | Estado |
|---:|---|---|
| 1 | COL-002 — Visão Geral do Responsável | validada |
| 2 | COL-003 — gestão de solicitações | validada |
| 3 | TRN-105/106/107/108/109/110/112 | integralmente validadas |
| 4 | PER-106 — Meus Coletivos | validado |
| 5 | PER-107 — Central de Atualizações | contrato validado; **SVG corrente UXA-095 pendente de revalidação** |
| 6 | TRN-111 | **parcial** |
| 7 | PER-108 — Início do Participante | **materializado; validação pendente** |

## 8. Dívidas preservadas

- revalidar `PER-107` corrente, validar `PER-108` e `TRN-111` ponta a ponta;
- estados P0B de Meus Coletivos e Central;
- canais P1 e operação interna especializada;
- dez estados residuais UXA-055;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- operação interna restante do Coletivo.

## 9. Estado documental

| Camada | Estado |
|---|---|
| Jornadas Integradas | `active` 0.23.0 |
| Jornada da Pessoa | `draft` 0.8.0 |
| Jornada do Coletivo | `draft` 0.11.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.19.0 |
| galeria visual | `active` 0.14.0 |
| página de Coletivos | `active` 0.12.0 |
| matriz por SVG | `active` 0.12.0 |
| lacunas | `active` 0.20.0 |
| registro de superfícies | `active` 0.12.0 |
| registro de transições | `active` 0.12.0 |
| detalhamento da Pessoa | `active` 0.7.0 |
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 10. Preservações

- materialização não equivale a validação funcional;
- uma versão reformulada exige revalidação;
- pertencimento, disponibilidade, função, presença e autoridade permanecem estados separados;
- `PER-107` continua triagem pessoal, não feed social;
- `PER-108` é síntese interna e não replica canais especializados;
- Pessoa e Coletivo permanecem `draft`;
- nenhuma etapa autoriza automaticamente a seguinte.

## 11. Próxima transição autorizável

**UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de GKR-TRN-111.**

A UXA-096 não foi iniciada e depende de autorização separada.
