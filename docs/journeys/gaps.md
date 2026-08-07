---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.19.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-055
  - UXA-059
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-094 fecha funcionalmente `PER-107` e `TRN-110`, mas não materializa `PER-108`, não valida `TRN-111` e não promove a jornada completa.

## 2. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável → gestão de solicitações | COL-002; TRN-112; COL-003 | materializados | superfícies validadas; TRN-112 integralmente validada | nenhuma nesta ligação |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | materializados | handoffs integralmente validados | aprovação fechada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | materializados | integralmente validada por UXA-092 | nenhuma nesta ligação |
| Meus Coletivos → Central de Atualizações | PER-106; TRN-110; PER-107 | dois SVGs correntes reformulados | **PER-106/PER-107 validados; TRN-110 integralmente validada por UXA-094** | nenhuma nesta ligação específica |
| Central de Atualizações → Início do Participante | PER-107; TRN-111; PER-108 | origem validada; destino não vigente | ausente | reformular/materializar PER-108 e depois validar TRN-111 |

`PER-107/TRN-110` deixam a fila de validação. O próximo bloqueio estrutural de Coletivos passa a ser `PER-108/TRN-111`.

## 3. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | Início do Participante reformulado | GKR-SURF-PER-108; GKR-TRN-111 | referência anterior não promovida | reformulação/materialização em pacote próprio |
| 2 | estados P0B adicionais de Meus Coletivos | GKR-SURF-PER-106 | P0A validado | materializar somente quando mudança de decisão/hierarquia justificar ativo próprio |
| 3 | estados P0B da Central | GKR-SURF-PER-107 | P0A validado | vazio, excesso de volume e baixa conectividade em frente própria quando necessário |
| 4 | participantes e operação interna | GKR-SURF-COL-004 a 007; GKR-TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | GKR-SURF-ORG-004 a 006; GKR-SURF-COL-008 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | GKR-SURF-ORG-001; GKR-SURF-ORG-007 | cobertura parcial | programa específico e validação |

Nenhuma dessas materializações é iniciada pela UXA-094.

## 4. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 | compreensão inicial → Tela Hoje | telas separadas; transição não examinada | validação integrada |
| V2 | publicação → descoberta e mapa/lista/detalhe | pacotes distintos | revalidação integrada |
| V3 | dez estados residuais do Opportunity Boost | 10 SVGs sem validação | pacote específico |
| V4 | efeito externo de oportunidades | fronteira sem tela por definição | contrato e validação específicos |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

`PER-107/TRN-110` não aparecem mais nesta fila porque foram fechados pela UXA-094.

## 5. Efeito da UXA-094

A UXA-094:

- reforma 2 SVGs existentes e cria 0 novos;
- revalida `PER-106` no gatilho atual;
- valida `PER-107`;
- promove `TRN-110` a `integralmente validada`;
- mantém `TRN-111` ausente e `PER-108` não vigente;
- mantém 107 SVGs, 107 associações e 27 perfis;
- eleva validações de 96 para **97**;
- reduz pendências de 11 para **10**, exclusivamente UXA-055;
- eleva para **7** os handoffs integralmente validados no trecho de Coletivos;
- não promove qualquer jornada.

## 6. Critérios preservados

- uma tela genérica não fecha lacuna;
- uma seta presumida não cria transição;
- materialização não equivale a validação;
- uma versão visual reformulada exige revalidação;
- dois endpoints materializados não validam automaticamente a ligação;
- estado `lido` não equivale a ação concluída ou consentimento;
- validação integral documental não equivale a implementação técnica;
- a Central não presume `PER-108` ou canais especializados disponíveis.

## 7. Próximo ato possível

A próxima ação governada é **UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`**, mediante autorização separada.

A UXA-095 não é iniciada por esta atualização.
