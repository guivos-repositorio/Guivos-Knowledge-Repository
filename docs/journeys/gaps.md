---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.22.0
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
  - UXA-095
  - UXA-096
  - UXA-097
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-097 fecha a continuidade `PER-007 → TRN-007 → PER-008` sem promover a Jornada da Pessoa ou alterar a fila de materialização de Coletivos.

## 2. Gates pessoais

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| compreensão inicial → primeira Tela Hoje | PER-007; TRN-007; PER-008 | origem reformulada; primeira Hoje materializada | **integralmente validada por UXA-097** | recorrência e estados alternativos separados |
| Home pública → entrada protegida | PER-001; TRN-001; PER-002 | materializados | parcial | validação integrada |
| escolha → expressão | PER-003; TRN-003; PER-004 | materializados | parcial | validação integrada |
| expressão → inventário | PER-004; TRN-004; PER-005 | materializados | parcial | validação integrada |
| inventário → processamento | PER-005; TRN-005; PER-006 | materializados | parcial | validação integrada |

## 3. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável → gestão de solicitações | COL-002; TRN-112; COL-003 | materializados | superfícies e TRN-112 validadas | nenhuma nesta ligação |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | materializados | integralmente validada nos handoffs indicados | aprovação fechada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | materializados | integralmente validada | nenhuma nesta ligação |
| Meus Coletivos → Central | PER-106; TRN-110; PER-107 | materializados | integralmente validada | nenhuma nesta ligação |
| Central → Início do Participante | PER-107; TRN-111; PER-108 | materializados | integralmente validada por UXA-096 | estados P0B e áreas internas permanecem separados |

## 4. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | estados P0B adicionais de Meus Coletivos | PER-106 | P0A validado | ativo próprio somente quando decisão/proteção justificar |
| 2 | estados P0B da Central | PER-107 | P0A validado | vazio, excesso de volume e baixa conectividade em frente própria |
| 3 | estados alternativos do Início do Participante | PER-108 | P0A validado | materializar somente mudança material de decisão/proteção |
| 4 | participantes e operação interna | COL-004 a 007; TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | ORG-004 a 006; COL-008 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | ORG-001; ORG-007 | cobertura parcial | programa específico e validação |

A primeira variante de Hoje exigida para fechar `V1` foi materializada e validada dentro da UXA-097 porque o próprio contrato UXA-010 a registrava como estado distinto necessário ao handoff; ela não altera esta fila de materialização remanescente.

## 5. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| **V1 — encerrado** | compreensão inicial → Tela Hoje | **TRN-007 integralmente validada; primeira Hoje validada** | UXA-097 |
| **V2** | publicação → descoberta e mapa/lista/detalhe | pacotes distintos | revalidação integrada |
| **V3** | dez estados residuais Opportunity Boost | 10 SVGs sem validação | pacote específico |
| **V4** | efeito externo de oportunidades | fronteira sem tela | contrato e validação específicos |
| **V5** | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

O antigo gate V0 (`PER-107` corrente + `PER-108` + `TRN-111`) permanece encerrado pela UXA-096.

## 6. Efeito da UXA-097

A UXA-097:

- cria 1 SVG para a primeira variante de `PER-008`;
- reforma 1 SVG existente de decisão em `PER-007`;
- revalida a variante corrente de decisão;
- valida a primeira Tela Hoje;
- promove `TRN-007` de não examinada para integralmente validada;
- preserva 40 superfícies e 37 transições;
- eleva SVGs e associações de 108 para **109**;
- preserva 28 perfis;
- eleva validações correntes de 98 para **99**;
- preserva **10 pendências**, exclusivamente UXA-055;
- não promove qualquer jornada.

## 7. Critérios preservados

- materialização não equivale a validação por padrão; a nova variante foi validada explicitamente nesta frente;
- conclusão da compreensão não constitui avanço humano por si só;
- personalização não é condição para acessar Hoje;
- afirmações abertas, desconhecidas ou contestadas não viram fatos;
- estado canônico vigente prevalece sobre renderização obsoleta;
- retorno ou repetição não duplica efeito;
- publicidade não pode criar prioridade artificial na primeira Hoje;
- validação integral documental não equivale a implementação técnica.

## 8. Próximo ato possível

Com `V1` encerrada, a próxima prioridade de validação registrada é **V2 — publicação → descoberta e mapa/lista/detalhe**. A UXA-098 dependerá de autorização separada e **não foi iniciada**.