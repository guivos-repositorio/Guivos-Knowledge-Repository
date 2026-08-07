---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.21.0
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
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-096 revalida `PER-107`, valida `PER-108` e fecha `TRN-111` ponta a ponta, sem promover a jornada completa ou materializar áreas internas adicionais.

## 2. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável → gestão de solicitações | COL-002; TRN-112; COL-003 | materializados | superfícies e TRN-112 validadas | nenhuma nesta ligação |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | materializados | integralmente validada nos handoffs indicados | aprovação fechada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | materializados | integralmente validada | nenhuma nesta ligação |
| Meus Coletivos → Central | PER-106; TRN-110; PER-107 | materializados | **integralmente validada** | nenhuma nesta ligação |
| Central → Início do Participante | PER-107; TRN-111; PER-108 | materializados | **integralmente validada por UXA-096** | estados P0B e áreas internas permanecem separados |

## 3. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | estados P0B adicionais de Meus Coletivos | PER-106 | P0A validado | ativo próprio somente quando decisão/proteção justificar |
| 2 | estados P0B da Central | PER-107 | P0A validado | vazio, excesso de volume e baixa conectividade em frente própria |
| 3 | estados alternativos do Início do Participante | PER-108 | P0A validado | materializar somente mudança material de decisão/proteção |
| 4 | participantes e operação interna | COL-004 a 007; TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | ORG-004 a 006; COL-008 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | ORG-001; ORG-007 | cobertura parcial | programa específico e validação |

## 4. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 | compreensão inicial → Tela Hoje | telas separadas | validação integrada |
| V2 | publicação → descoberta e mapa/lista/detalhe | pacotes distintos | revalidação integrada |
| V3 | dez estados residuais Opportunity Boost | 10 SVGs sem validação | pacote específico |
| V4 | efeito externo de oportunidades | fronteira sem tela | contrato e validação específicos |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

O antigo gate V0 (`PER-107` corrente + `PER-108` + `TRN-111`) foi encerrado pela UXA-096.

## 5. Efeito da UXA-096

A UXA-096:

- reforma 2 SVGs existentes e cria 0 SVGs;
- revalida `PER-107`;
- valida `PER-108`;
- promove `TRN-111` de parcial para integralmente validada;
- mantém `TRN-110` integralmente validada;
- preserva 108 SVGs, 108 associações e 28 perfis;
- eleva validações correntes de 96 para **98**;
- reduz pendências para **10**, exclusivamente UXA-055;
- não promove qualquer jornada.

## 6. Critérios preservados

- materialização não equivale a validação;
- evento histórico não concede nem preserva acesso interno;
- vínculo atual e permissões governam a entrada;
- abrir contexto interno não altera vínculo, leitura, papel, presença ou autoridade;
- uma síntese não substitui a Central nem os canais especializados;
- estado canônico prevalece sobre renderização obsoleta;
- repetição de navegação não duplica efeito;
- validação integral documental não equivale a implementação técnica.

## 7. Próximo ato possível

A continuidade até `PER-108` está fechada no escopo documental. A próxima priorização deve partir das lacunas remanescentes; **UXA-097 não foi iniciada**.
