---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.22.0
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
  - UXA-096
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - ROADMAP-12.69.0
  - M7.83
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente quando o incremento correspondente estiver integrado ao ramo principal. Em caso de divergência, prevalece sobre resumos não normativos.

## 2. Estado global proposto pela UXA-096

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | Início do Participante validado; TRN-111 integralmente validada | UXA-096; M7.83 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | 40 superfícies e 37 transições | UXA-076 a UXA-096 |
| Galeria visual | `active` 0.15.0; 108 SVGs | UXA-081 a UXA-096 |
| Página de Coletivos | `active` 0.13.0 | UXA-096 |
| Matriz por SVG | 108 arquivos / 28 perfis | UXA-083 a UXA-096 |
| Jornadas Integradas | `active` 0.24.0; Pessoa, Coletivo e Organização em `draft` | UXA-070 a UXA-096 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **108** |
| associações individuais | **108** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **98** |
| pendentes de validação específica | **10** |
| IDs granulares com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |

As dez pendências são exclusivamente os estados residuais UXA-055.

## 4. Resultado da UXA-096

A UXA-096:

- reforma 2 SVGs existentes e cria 0 SVGs;
- revalida a versão corrente de `PER-107`;
- valida `PER-108`;
- promove `TRN-111` de parcial para integralmente validada;
- preserva `TRN-110` integralmente validada;
- não cria ID de superfície ou transição;
- não promove Jornada da Pessoa ou Jornada do Coletivo.

Veredito:

> **Aprovada após reformulação controlada e validação integrada de `GKR-TRN-111`.**

## 5. Continuidade validada

```text
PER-107 — Central de Atualizações
→ Pessoa escolhe “Abrir início do Coletivo”
→ vínculo atual e permissão são revalidados
→ evento histórico não concede nem preserva acesso
→ leitura, vínculo, papel, presença, disponibilidade e autoridade permanecem inalterados
→ PER-108 — Início do Participante
→ mesmo Coletivo e mesmo vínculo lógico permanecem em contexto
```

Retorno é neutro; estado canônico mais recente prevalece; repetição de abertura, retorno ou recarga não duplica efeito lógico.

## 6. Handoffs integralmente validados

Oito transições estão integralmente validadas no trecho governado de Coletivos:

- `GKR-TRN-105`;
- `GKR-TRN-106`;
- `GKR-TRN-107`;
- `GKR-TRN-108`;
- `GKR-TRN-109`;
- `GKR-TRN-110`;
- `GKR-TRN-111`;
- `GKR-TRN-112`.

## 7. Prioridade operacional de Coletivos

| Ordem | Superfície ou continuidade | Estado |
|---:|---|---|
| 1 | COL-002 — Visão Geral do Responsável | validada |
| 2 | COL-003 — gestão de solicitações | validada |
| 3 | TRN-105/106/107/108/109/110/111/112 | integralmente validadas |
| 4 | PER-106 — Meus Coletivos | validado |
| 5 | PER-107 — Central de Atualizações | **validado na versão corrente** |
| 6 | TRN-111 | **integralmente validada** |
| 7 | PER-108 — Início do Participante | **validado** |

## 8. Dívidas preservadas

- estados P0B de Meus Coletivos, Central e Início do Participante;
- canais P1 e operação interna especializada;
- dez estados residuais UXA-055;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções em outras jornadas;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada como conjunto.

## 9. Estado documental

| Camada | Estado |
|---|---|
| Jornadas Integradas | `active` 0.24.0 |
| Jornada da Pessoa | `draft` 0.9.0 |
| Jornada do Coletivo | `draft` 0.12.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.20.0 |
| galeria visual | `active` 0.15.0 |
| página de Coletivos | `active` 0.13.0 |
| matriz por SVG | `active` 0.13.0 |
| lacunas | `active` 0.21.0 |
| registro de superfícies | `active` 0.13.0 |
| registro de transições | `active` 0.13.0 |
| detalhamento da Pessoa | `active` 0.8.0 |
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 10. Preservações

- materialização não equivale a validação funcional;
- evento histórico não concede acesso atual;
- pertencimento, disponibilidade, função, presença e autoridade permanecem estados separados;
- `PER-107` continua triagem pessoal, não feed social;
- `PER-108` é síntese interna e não replica canais especializados;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- validação integral documental não equivale a implementação;
- Pessoa e Coletivo permanecem `draft`;
- nenhuma etapa autoriza automaticamente a seguinte.

## 11. Próxima transição autorizável

A UXA-096 encerra o gate específico até o Início do Participante. A próxima priorização deve partir das lacunas remanescentes. **UXA-097 não foi iniciada e depende de autorização separada.**
