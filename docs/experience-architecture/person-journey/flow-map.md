---
id: GKR-UX-PERSON-JOURNEY-FLOW-001
title: Jornada da Pessoa — Mapa Completo de Superfícies para Design
status: active
version: 0.1.8
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-25
normative: false
maturity: current_documentation_sequence
depends_on:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-UX-PERSON-JOURNEY-READ-FIRST-001
  - GKR-UX-HOME-MASTER-001
---

# Jornada da Pessoa — Mapa Completo de Superfícies para Design

## 1. Finalidade

Este documento organiza **todas as superfícies/responsabilidades correntes da Pessoa que deverão receber documentação própria para Design e IA**, sem criar novas telas nem alterar o Registry.

A Home pública `PER-001` já possui Documento Mestre próprio e funciona como origem pública da Journey. Por isso, esta coleção começa em `PER-002`.

```text
PER-001 — HOME PÚBLICA
→ autoridade já existente
→ fora da contagem desta nova coleção

PER-002..304
→ 26 superfícies/responsabilidades da Pessoa a documentar
```

## 2. Espinha dorsal da entrada e compreensão

```text
PER-001 — HOME PÚBLICA
→ TRN-001
→ PER-002 — ENTRADA PROTEGIDA
→ TRN-002
→ PER-003 — ESCOLHA DE MODALIDADE
→ TRN-003
→ PER-004 — EXPRESSÃO POR TEXTO OU VOZ
→ TRN-004
→ PER-005 — INVENTÁRIO E AUTORIZAÇÃO
→ TRN-005
→ PER-006 — PROCESSAMENTO VISÍVEL
→ TRN-006
→ PER-008 — HOJE
→ TRN-007
→ PER-008 — HOJE
```

Estado corrente das transições:

| Transição | Origem → destino | Estado corrente |
|---|---|---|
| `TRN-001` | PER-001 → PER-002 | parcial |
| `TRN-002` | PER-002 → PER-003 | localmente validada |
| `TRN-003` | PER-003 → PER-004 | parcial |
| `TRN-004` | PER-004 → PER-005 | parcial |
| `TRN-005` | PER-005 → PER-006 | parcial |
| `TRN-006` | PER-006 → PER-007 | localmente validada |
| `TRN-007` | PER-007 → PER-008 | integralmente validada |

Regra corrente de `PER-003`:

```text
VALIDATED MODALITY CHOICES
→ TEXT
→ VOICE
→ FILE
→ OPTIONAL GUIDED QUESTIONS

COMBINATION
→ ALLOWED
→ NOT REQUIRED

TEXT / VOICE
→ TRN-003 → PER-004

FILE / OPTIONAL GUIDED QUESTIONS
→ DOWNSTREAM CONTINUITY NOT FULLY CONTRACTED
→ MUST NOT BE INVENTED
```

## 3. Continuidade recorrente a partir de Hoje

```text
PER-008 — HOJE
├── TRN-008 → PER-010 — MEUS OBJETIVOS → TRN-009 → PER-008
├── TRN-010 → PER-011 — MEUS PRÓXIMOS PASSOS → TRN-011 → PER-008
└── TRN-012 → PER-012 — MINHA EVOLUÇÃO → TRN-013 → PER-008
```

`PER-010`, `PER-011` e `PER-012` são capacidades especializadas. O modelo corrente **não registra navegação direta entre elas**.

```text
PER-010 ↔ PER-011
PER-011 ↔ PER-012
PER-010 ↔ PER-012
→ NÃO CONTRATADAS COMO HANDOFF DIRETO
```

## 4. Família de Oportunidades

```text
PER-201 — MAPA DE OPORTUNIDADES
↔ PER-202 — LISTA DE OPORTUNIDADES
→ PER-203 — DETALHE DE OPORTUNIDADE
→ estado de revisão consciente dentro de PER-203
→ TRN-205
→ BND-001 — FRONTEIRA EXTERNA
→ TERCEIRO
```

Regras estruturais:

- Mapa e Lista representam modos da mesma descoberta territorial;
- alternar Mapa ↔ Lista não cria nova Journey;
- a revisão consciente não cria nova superfície;
- `BND-001` não é tela Guivos;
- resultado posterior ao handoff pertence ao terceiro.

## 5. Família de Coletivos na perspectiva da Pessoa

```text
PER-101 — EXPLORAR COLETIVOS
→ PER-102 — RESULTADOS DE BUSCA
→ PER-103 — PERFIL PÚBLICO DO COLETIVO
→ PER-104 — REVISÃO E SOLICITAÇÃO
→ PER-105 — SOLICITAÇÃO PENDENTE
↔ COL-003 — GESTÃO DE SOLICITAÇÕES PELO RESPONSÁVEL
→ aprovação
→ PER-106 — MEUS COLETIVOS
→ PER-107 — CENTRAL DE ATUALIZAÇÕES
→ PER-108 — INÍCIO DO PARTICIPANTE
```

`COL-003` pertence ao contexto do Coletivo e não receberá Documento Mestre da Pessoa. Os documentos da Pessoa devem apenas governar o handoff correspondente.

## 6. Conta e Planos

```text
PER-009 — CONTA / CONFIGURAÇÕES DA PESSOA
→ TRN-406
→ PER-301 — PLANOS E COMPARAÇÃO
├── TRN-401 → PER-302 — REVISÃO DE CONTRATAÇÃO → TRN-402 → PER-304
└── TRN-403 → PER-303 — DOWNGRADE / CANCELAMENTO → TRN-404 → PER-304

PER-304 — RESULTADO / RECUPERAÇÃO
→ TRN-405 → PER-301

PER-301
→ TRN-407 → PER-009
```

`PER-009` existe hoje como responsabilidade administrativa contratada para origem/retorno de Planos. Sua documentação **não pode inventar a arquitetura total de Conta e Configurações**.

## 7. Ordem governada de construção dos Documentos Mestres

A ordem abaixo prioriza a espinha dorsal da Journey antes das famílias especializadas.

| Ordem | Superfície | Documento | Situação |
|---:|---|---|---|
| 01 | `PER-002` | Entrada Protegida | **construído / current** |
| 02 | `PER-003` | Escolha de Modalidade | **construído / current** |
| 03 | `PER-004` | Expressão por Texto ou Voz | **construído / current** |
| 04 | `PER-005` | Inventário e Autorização | **construído / current** |
| 05 | `PER-006` | Processamento Visível | **construído / current** |
| 06 | `PER-007` | Compreensão Inicial Revisável | **construído / current** |
| 07 | `PER-008` | Hoje | **construído / current** |
| 08 | `PER-010` | Meus Objetivos | **construído / current** |
| 09 | `PER-011` | Meus Próximos Passos | planejado |
| 10 | `PER-012` | Minha Evolução | planejado |
| 11 | `PER-201` | Mapa de Oportunidades | planejado |
| 12 | `PER-202` | Lista de Oportunidades | planejado |
| 13 | `PER-203` | Detalhe de Oportunidade | planejado |
| 14 | `PER-101` | Explorar Coletivos | planejado |
| 15 | `PER-102` | Resultados de Busca de Coletivos | planejado |
| 16 | `PER-103` | Perfil Público do Coletivo | planejado |
| 17 | `PER-104` | Revisão e Solicitação | planejado |
| 18 | `PER-105` | Solicitação Pendente | planejado |
| 19 | `PER-106` | Meus Coletivos | planejado |
| 20 | `PER-107` | Central de Atualizações | planejado |
| 21 | `PER-108` | Início do Participante | planejado |
| 22 | `PER-009` | Conta / Configurações — recorte governado | planejado |
| 23 | `PER-301` | Planos e Comparação | planejado |
| 24 | `PER-302` | Revisão de Contratação | planejado |
| 25 | `PER-303` | Downgrade e Cancelamento | planejado |
| 26 | `PER-304` | Resultado e Recuperação de Plano/Cobrança | planejado |

## 8. Regra para criação no MENU

Somente documentos efetivamente construídos entram no MENU.

```text
PLANEJADO
→ NÃO CRIA PÁGINA VAZIA
→ NÃO CRIA LINK DE MENU

DOCUMENTADO + VALIDADO
→ PODE ENTRAR NO MENU
```

## 9. Regra para estados internos

Cada Documento Mestre deve detalhar todos os estados necessários da superfície sem criar um documento separado para cada variante.

Exemplos:

- autenticação é estado/gate interno de `PER-002`;
- revisão consciente é estado de `PER-203`;
- comparação de Free/Plus/Pro ocorre dentro de `PER-301`;
- falha/recuperação do processamento financeiro pertence a `PER-304`.

## 10. Estado

```text
PERSON SURFACES IN CURRENT REGISTRY
→ 27

PER-001
→ ALREADY COVERED BY PUBLIC HOME MASTER

NEW SURFACE MASTERS TO BUILD
→ 26

BUILT
→ 8 / 26
→ PER-002
→ PER-003
→ PER-004
→ PER-005
→ PER-006

REMAINING
→ 18 / 26

NEXT DOCUMENTATION TARGET
→ PER-011 — MEUS PRÓXIMOS PASSOS

NEW PER-IDS
→ NONE

DESIGN / PROTOTYPE / IMPLEMENTATION
→ NOT CREATED BY THIS MAP
```
