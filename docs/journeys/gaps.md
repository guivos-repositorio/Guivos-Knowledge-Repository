---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.23.0
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
  - UXA-098
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-098 fecha a prioridade V2 sem alterar SVGs, promover jornadas ou iniciar efeito externo de oportunidades.

## 2. Gates pessoais

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| compreensão inicial → primeira Tela Hoje | PER-007; TRN-007; PER-008 | materializados | integralmente validada por UXA-097 | recorrência e estados alternativos separados |
| Home pública → entrada protegida | PER-001; TRN-001; PER-002 | materializados | parcial | validação integrada |
| escolha → expressão | PER-003; TRN-003; PER-004 | materializados | parcial | validação integrada |
| expressão → inventário | PER-004; TRN-004; PER-005 | materializados | parcial | validação integrada |
| inventário → processamento | PER-005; TRN-005; PER-006 | materializados | parcial | validação integrada |

## 3. Gates de oportunidade e descoberta

| Continuidade | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| publicação/ativação → descoberta | ORG-003; TRN-203; PER-201 | materializados e validados localmente | **TRN-203 integralmente validada por UXA-098** | efeito externo e integração patrocinada permanecem separados |
| Mapa → Lista | PER-201; TRN-210; PER-202 | materializados e validados localmente | **TRN-210 integralmente validada por UXA-098** | nenhuma nesta ligação |
| Mapa → Detalhe | PER-201; TRN-204; PER-203 | materializados e validados localmente | **TRN-204 integralmente validada por UXA-098** | TRN-205 externo permanece separado |
| Lista → Detalhe | PER-202; TRN-211; PER-203 | materializados e validados localmente | **TRN-211 integralmente validada por UXA-098** | TRN-205 externo permanece separado |
| Detalhe → efeito externo | PER-203; TRN-205; BND-001 | detalhe materializado; fronteira sem tela | parcial | contrato e validação específicos |
| patrocinado → Mapa/Lista orgânicos | COM-002; TRN-304/306; PER-201/PER-202 | materializados | parcial | integração orgânico–patrocinado específica |

## 4. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável → gestão de solicitações | COL-002; TRN-112; COL-003 | materializados | superfícies e TRN-112 validadas | nenhuma nesta ligação |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | materializados | integralmente validada nos handoffs indicados | aprovação fechada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | materializados | integralmente validada | nenhuma nesta ligação |
| Meus Coletivos → Central | PER-106; TRN-110; PER-107 | materializados | integralmente validada | nenhuma nesta ligação |
| Central → Início do Participante | PER-107; TRN-111; PER-108 | materializados | integralmente validada por UXA-096 | estados P0B e áreas internas permanecem separados |

## 5. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | estados P0B adicionais de Meus Coletivos | PER-106 | P0A validado | ativo próprio somente quando decisão/proteção justificar |
| 2 | estados P0B da Central | PER-107 | P0A validado | vazio, excesso de volume e baixa conectividade em frente própria |
| 3 | estados alternativos do Início do Participante | PER-108 | P0A validado | materializar somente mudança material de decisão/proteção |
| 4 | participantes e operação interna | COL-004 a 007; TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | ORG-004 a 006; COL-008 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | ORG-001; ORG-007 | cobertura parcial | programa específico e validação |

## 6. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 — encerrado | compreensão inicial → Tela Hoje | TRN-007 integralmente validada | UXA-097 |
| **V2 — encerrado** | publicação → descoberta e Mapa/Lista/Detalhe | **TRN-203/204/210/211 integralmente validadas** | **UXA-098** |
| **V3** | dez estados residuais Opportunity Boost | 10 SVGs sem validação específica | pacote específico |
| V4 | efeito externo de oportunidades | TRN-205 parcial | contrato e validação específicos |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

## 7. Efeito da UXA-098

A UXA-098:

- não cria nem altera SVG;
- preserva 109 SVGs, 109 associações e 28 perfis;
- preserva 99 validações funcionais vigentes;
- preserva 10 pendências, exclusivamente UXA-055;
- promove `TRN-203`, `TRN-204`, `TRN-210` e `TRN-211` a integralmente validadas;
- preserva 40 superfícies e 37 transições;
- separa publicação de distribuição garantida;
- separa Mapa/Lista/Detalhe de efeito externo posterior;
- preserva a fronteira entre descoberta orgânica e inventário patrocinado;
- não promove qualquer jornada.

## 8. Critérios preservados

- oportunidade ativa torna-se candidata à descoberta; não recebe exposição garantida;
- estado canônico vigente prevalece sobre cartão ou detalhe obsoleto;
- Mapa e Lista representam a mesma consulta;
- alternar modo não cria autorização, personalização ou relevância;
- abrir Detalhe não equivale a interesse, inscrição ou evolução;
- pagamento não altera relevância funcional;
- repetição e sincronização não duplicam oportunidade ou efeito;
- validação integral documental não equivale a implementação técnica.

## 9. Próximo ato possível

Com `V2` encerrada, a próxima prioridade registrada é **V3 — dez estados residuais UXA-055**. Uma eventual UXA-099 dependerá de autorização separada e **não foi iniciada**.