---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.25.0
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
  - UXA-099
  - UXA-100
  - UXA-100-A2
  - UXA-100-A3
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A UXA-100-A3 promove canonicamente a frente de Planos depois da validação funcional da UXA-100-A2, mas preserva como lacunas separadas cobrança real, processo comercial Enterprise/Scale, entradas contextuais sem origem canônica própria e as continuidades anteriores ainda não fechadas.

## 2. Gates pessoais

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| compreensão inicial → primeira Tela Hoje | PER-007; TRN-007; PER-008 | materializados | integralmente validada por UXA-097 | recorrência e estados alternativos separados |
| Home pública → entrada protegida | PER-001; TRN-001; PER-002 | materializados | parcial | validação integrada |
| escolha → expressão | PER-003; TRN-003; PER-004 | materializados | parcial | validação integrada |
| expressão → inventário | PER-004; TRN-004; PER-005 | materializados | parcial | integração com inventário |
| inventário → processamento | PER-005; TRN-005; PER-006 | materializados | parcial | continuidade entre materializações |

## 3. Gates de oportunidade e descoberta

| Continuidade | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| publicação/ativação → descoberta | ORG-003; TRN-203; PER-201 | materializados | **TRN-203 integralmente validada por UXA-098** | efeito externo e integração patrocinada separados |
| Mapa → Lista | PER-201; TRN-210; PER-202 | materializados | **integralmente validada** | nenhuma nesta ligação |
| Mapa → Detalhe | PER-201; TRN-204; PER-203 | materializados | **integralmente validada** | TRN-205 externo separado |
| Lista → Detalhe | PER-202; TRN-211; PER-203 | materializados | **integralmente validada** | TRN-205 externo separado |
| Detalhe → efeito externo | PER-203; TRN-205; BND-001 | detalhe materializado; fronteira sem tela | parcial | contrato e validação específicos |
| patrocinado → Mapa/Lista orgânicos | COM-002; TRN-304/306; PER-201/PER-202 | materializados | parcial | integração orgânico–patrocinado específica |

## 4. Gates do Opportunity Boost

| Continuidade ou família | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| dez estados residuais UXA-055 | COM-005 | 10 SVGs | **validado por UXA-099** | nenhuma pendência específica dos SVGs |
| gestão ativa → estados residuais | COM-004; TRN-305; COM-005 | origem e destino materializados | parcial | validação ponta a ponta |
| retorno patrocinado → Mapa | COM-002; TRN-304; PER-201 | materializados | parcial | integração específica |
| retorno patrocinado → Lista | COM-002; TRN-306; PER-202 | materializados | parcial | integração específica |

## 5. Gates de Planos, cobrança e ciclo de vida

| Participante | IDs | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Pessoa | PER-301 a 304; TRN-401 a 405 | 3 SVGs canônicos | superfícies validadas; 5 transições localmente validadas | gateway, cobrança real, proration e entradas de origem ainda não registradas |
| Coletivo | COL-301 a 304; TRN-411 a 416 | 3 SVGs canônicos | superfícies validadas; TRN-411 a 415 locais; TRN-416 parcial | cobrança real e processo Enterprise após BND-002 |
| Organização | ORG-301 a 304; TRN-421 a 426 | 3 SVGs canônicos | superfícies validadas; TRN-421 a 425 locais; TRN-426 parcial | cobrança real e processo Scale após BND-002 |
| fronteira comercial | BND-002 | sem tela por definição | parcial | proposta, contrato, dimensionamento e handoffs operacionais posteriores |

A promoção de Planos não autoriza inferir uma transição a partir de `Conta/Configurações`, criação de publicação ou correspondência personalizada quando a origem ainda não possui identidade canônica adequada.

## 6. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável → gestão de solicitações | COL-002; TRN-112; COL-003 | materializados | integralmente validada | nenhuma nesta ligação |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | materializados | integralmente validada | aprovação fechada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | materializados | integralmente validada | nenhuma nesta ligação |
| Meus Coletivos → Central | PER-106; TRN-110; PER-107 | materializados | integralmente validada | nenhuma nesta ligação |
| Central → Início do Participante | PER-107; TRN-111; PER-108 | materializados | integralmente validada | estados P0B e áreas internas separados |

## 7. Fila de materialização por dependência

| Prioridade | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| 1 | estados P0B adicionais de Meus Coletivos | PER-106 | P0A validado | ativo próprio somente quando decisão/proteção justificar |
| 2 | estados P0B da Central | PER-107 | P0A validado | vazio, excesso de volume e baixa conectividade em frente própria |
| 3 | estados alternativos do Início do Participante | PER-108 | P0A validado | materializar somente mudança material de decisão/proteção |
| 4 | participantes e operação interna | COL-004 a 007; TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | ORG-004 a 006; COL-008 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | ORG-001; ORG-007 | cobertura parcial | programa específico e validação |
| 7 | processo comercial Enterprise/Scale | BND-002; TRN-416/426 | fronteira registrada | materializar somente após contrato comercial/operacional suficiente |

## 8. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 — encerrado | compreensão inicial → Tela Hoje | TRN-007 integral | UXA-097 |
| V2 — encerrado | publicação → descoberta e Mapa/Lista/Detalhe | TRN-203/204/210/211 integrais | UXA-098 |
| V3 — encerrado | dez estados residuais Opportunity Boost | 10 SVGs validados | UXA-099 |
| Planos — identidade encerrada | fragmentação e promoção canônica | 12 superfícies + 17 transições registradas | UXA-100-A3 |
| V4 | efeito externo de oportunidades | TRN-205 parcial | contrato e validação específicos |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada |

## 9. Efeito da UXA-100-A3

- SVGs canônicos: **109 → 118**;
- associações: **109 → 118**;
- perfis: **28 → 31**;
- validações funcionais vigentes: **109 → 118**;
- pendências específicas: **0**;
- superfícies/estados/fronteiras: **40 → 53**;
- transições: **37 → 54**;
- IDs com referência visual: **30 → 42**;
- fronteiras sem tela: **1 → 2**;
- jornadas principais permanecem `draft`;
- nenhuma implementação técnica é criada.

## 10. Critérios preservados

- validação de superfície não equivale a validação automática de transição;
- validação local não equivale a cobrança ponta a ponta;
- oportunidade pública não é ocultada para vender plano;
- plano pago não compra relevância, confiança, impacto, legitimidade ou evolução;
- assinatura permanece separada de transação, comissão, taxa e tributo;
- Enterprise/Scale não recebem checkout fictício;
- repetição da mesma intenção não duplica efeito lógico;
- validação documental não equivale a implementação técnica.

## 11. Próximo ato possível

A identidade canônica da frente de Planos está encerrada pela UXA-100-A3. Permanecem como frentes separadas a cobrança real, o processo após `BND-002`, entradas contextuais adicionais e a fila global previamente existente. Nenhuma próxima frente é iniciada automaticamente.