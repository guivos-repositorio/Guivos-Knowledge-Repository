---
id: GKR-JOURNEY-SCENARIOS-001
title: Cenários Integrados de Jornada
status: active
version: 0.7.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-070
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
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
| nós materializados | explorar, busca, Perfil Público, revisão, PER-105, COL-003, PER-106 e PER-107 |
| nós validados | superfícies acima nos gates correspondentes; PER-107 por UXA-094 |
| handoffs integralmente validados | TRN-105, 106, 107, 108, 109, 110 e 112 nos escopos aplicáveis |
| interrupção por lacuna | TRN-111 / PER-108 |
| conclusão permitida | o trecho até a Central possui as validações documentais indicadas |
| conclusão proibida | declarar toda a jornada interna do participante validada ou implementada |

### 2.3 Pessoa recebe aprovação e encontra o vínculo em Meus Coletivos

A sequência aprovação → resultado em PER-105 → vínculo formado → navegação opcional → PER-106 está integralmente validada por `TRN-108`.

### 2.4 Pessoa abre a Central de Atualizações

| Campo | Registro |
|---|---|
| finalidade | compreender mudanças sem converter atenção em engajamento ou efeito implícito |
| origem | `PER-106 — Meus Coletivos` validada |
| gatilho | `Ver atualizações` |
| destino | `PER-107 — Central de Atualizações` validada |
| transição | `TRN-110` integralmente validada por UXA-094 |
| entrada | não altera vínculo nem marca itens como lidos |
| leitura | não responde, aceita, confirma presença, concorda ou conclui ação |
| concorrência | estado canônico mais recente prevalece; ação obsoleta é revalidada/bloqueada |
| idempotência | abertura, retorno, recarga e leitura repetida não duplicam efeito lógico |
| ordenação | segurança material precede ação comum; engajamento/plano/publicidade não dominam |
| preferência | pode modular conteúdo não essencial; não oculta aviso essencial além do limite necessário |
| retorno | PER-106 sem consequência oculta |
| interrupção seguinte | `TRN-111/PER-108` |

### 2.5 Coletivo solicita informação adicional

`TRN-106` e `TRN-107` permanecem integralmente validadas por UXA-090; a Pessoa pode responder, não informar, contestar ou cancelar conforme estado.

### 2.6 Organização e Coletivo estabelecem relação

O contrato bilateral existe, mas não há fluxo de interface bilateral específico materializado como conjunto.

### 2.7 Organização publica oportunidade e Pessoa acessa

Cadastro, descoberta e detalhe existem em pacotes distintos; publicação → consumo e efeito externo permanecem incompletos.

### 2.8 Sobreposição comercial identificada

A camada comercial permanece separada da autoridade orgânica; dez estados residuais UXA-055 seguem sem validação específica.

## 3. Critério de completude

Um cenário só poderá ser marcado como completo quando todos os seus nós, transições, autoridades, dados, retornos, exceções e saídas estiverem documentados e funcionalmente validados como conjunto.

## 4. Estado vigente

O documento permanece `active` como síntese. A UXA-094 fecha o cenário específico `PER-106 → PER-107`, mas a jornada completa de Coletivos permanece interrompida em `PER-108/TRN-111`.

A UXA-095 não é iniciada por esta sincronização.
