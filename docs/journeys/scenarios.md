---
id: GKR-JOURNEY-SCENARIOS-001
title: Cenários Integrados de Jornada
status: active
version: 0.8.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-070
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
normative: false
---

# Cenários Integrados de Jornada

## 1. Regra de evidência

Cada cenário distingue nós materializados, nós validados, transições examinadas e ponto de interrupção por lacuna. Uma narrativa compreensível não equivale a fluxo implementado.

## 2. Cenários vigentes

### 2.1 Pessoa inicia sua jornada protegida

As superfícies locais possuem evidência, mas a continuidade completa até Tela Hoje permanece não validada como conjunto.

### 2.2 Pessoa encontra, solicita e recebe resultado de participação

| Campo | Registro |
|---|---|
| nós materializados | explorar, busca, Perfil Público, revisão, PER-105, COL-003, PER-106, PER-107 e **PER-108** |
| nós com validação vigente | até PER-106; contrato anterior de PER-107 validado, mas SVG corrente reformulado aguarda revalidação |
| handoffs integralmente validados | TRN-105, 106, 107, 108, 109, 110 e 112 |
| handoff novo | **TRN-111 parcial** |
| interrupção por lacuna | validação de PER-107 corrente, PER-108 e TRN-111 |
| conclusão permitida | a continuidade está materializada até o Início do Participante |
| conclusão proibida | declarar a jornada interna completa validada ou implementada |

### 2.3 Pessoa recebe aprovação e encontra o vínculo em Meus Coletivos

A sequência aprovação → resultado em PER-105 → vínculo formado → navegação opcional → PER-106 permanece integralmente validada por `TRN-108`.

### 2.4 Pessoa abre a Central de Atualizações

`PER-106 → Ver atualizações → PER-107` permanece integralmente validada em `TRN-110`. A UXA-095 não modifica esse contrato.

### 2.5 Pessoa abre o Início do Participante

| Campo | Registro |
|---|---|
| finalidade | entrar no contexto interno do mesmo Coletivo sem criar obrigação ou autoridade |
| origem | `PER-107` corrente, reformulada por UXA-095 |
| gatilho | `Abrir início do Coletivo` |
| destino | `PER-108 — Início do Participante`, materializado por UXA-095 |
| transição | `TRN-111` **parcial** |
| entrada | não altera leitura, vínculo, papel, disponibilidade, presença ou autoridade |
| conteúdo | propósito, vínculo, momento, ação compartilhada, consulta, atalhos e autonomia |
| separação | Início sintetiza; Central e canais especializados permanecem superfícies próprias |
| retorno/concorrência | ainda não validados como conjunto |
| próximo gate | UXA-096 |

### 2.6 Coletivo solicita informação adicional

`TRN-106` e `TRN-107` permanecem integralmente validadas por UXA-090; a Pessoa pode responder, não informar, contestar ou cancelar conforme estado.

### 2.7 Organização e Coletivo estabelecem relação

O contrato bilateral existe, mas não há fluxo de interface bilateral específico materializado como conjunto.

### 2.8 Organização publica oportunidade e Pessoa acessa

Cadastro, descoberta e detalhe existem em pacotes distintos; publicação → consumo e efeito externo permanecem incompletos.

### 2.9 Sobreposição comercial identificada

A camada comercial permanece separada da autoridade orgânica; dez estados residuais UXA-055 seguem sem validação específica.

## 3. Critério de completude

Um cenário só poderá ser marcado como completo quando todos os seus nós, transições, autoridades, dados, retornos, exceções e saídas estiverem documentados e funcionalmente validados como conjunto.

## 4. Estado vigente

O documento permanece `active` como síntese. A UXA-095 materializa o cenário `PER-107 → PER-108`, mas não o valida ponta a ponta.

A UXA-096 não é iniciada por esta sincronização.
