---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.31.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
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
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A D5-C1 fechou a identidade arquitetural de `Meus Objetivos`, `Meus Próximos Passos` e `Minha Evolução`; a D5-C2 fechou a ausência visual do estado-base; a D5-C3 fecha a **validação funcional local dos três SVGs**. A lacuna remanescente passa a ser a validação integrada de `TRN-008..013` e, quando necessário, estados sensíveis/alternativos específicos. V5/UXA-102, D6, D7, cobrança real e demais frentes continuam separadas.

## 2. Gates pessoais

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| compreensão inicial → primeira Tela Hoje | PER-007; TRN-007; PER-008 | materializados | integralmente validada por UXA-097 | recorrência e estados alternativos separados |
| Home pública → entrada protegida | PER-001; TRN-001; PER-002 | materializados | parcial | validação integrada |
| escolha → expressão | PER-003; TRN-003; PER-004 | materializados | parcial | validação integrada |
| expressão → inventário | PER-004; TRN-004; PER-005 | materializados | parcial | integração com inventário |
| inventário → processamento | PER-005; TRN-005; PER-006 | materializados | parcial | continuidade entre materializações |
| Conta/Configurações da Pessoa | PER-009; TRN-406/407 | sem SVG dedicado | identidade contratada pela UXA-100-A4 | materialização própria somente se necessária para validar ponta a ponta |
| Hoje ↔ Meus Objetivos | PER-008; TRN-008/009; PER-010 | **SVG D5-C2 reformulado e validado pela D5-C3** | PER-010 validado localmente; handoffs contratados | validação integrada de TRN-008/009 |
| Hoje ↔ Meus Próximos Passos | PER-008; TRN-010/011; PER-011 | **SVG D5-C2 reformulado e validado pela D5-C3** | PER-011 validado localmente; handoffs contratados | validação integrada de TRN-010/011 |
| Hoje ↔ Minha Evolução | PER-008; TRN-012/013; PER-012 | **SVG D5-C2 reformulado e validado pela D5-C3** | PER-012 validado localmente; handoffs contratados | validação integrada de TRN-012/013; estados sensíveis adicionais quando aplicáveis |

`PER-010..012` não são estados internos de Hoje. A presença de `‹ Hoje` nos wireframes não valida `TRN-008..013`. Também não existem handoffs diretos governados entre as três superfícies especializadas.

## 3. Gates de oportunidade e descoberta

| Continuidade | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| publicação/ativação → descoberta | ORG-003; TRN-203; PER-201 | materializados | **integralmente validada por UXA-098** | integração patrocinada separada |
| Mapa → Lista | PER-201; TRN-210; PER-202 | materializados | **integralmente validada** | nenhuma nesta ligação |
| Mapa → Detalhe | PER-201; TRN-204; PER-203 | materializados | **integralmente validada** | saída externa governada por UXA-101 |
| Lista → Detalhe | PER-202; TRN-211; PER-203 | materializados | **integralmente validada** | saída externa governada por UXA-101 |
| Detalhe → fronteira externa | PER-203; TRN-205; BND-001 | Detalhe reformulado; fronteira sem tela | **integralmente validada até a fronteira Guivos por UXA-101** | processo e resultado posteriores pertencem ao terceiro |
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
| Pessoa | PER-009; PER-301 a 304; TRN-401 a 407 | PER-009 sem SVG; 3 SVGs de Planos | PER-301..304 validadas; TRN-401..405 locais; TRN-406/407 contratadas | PER-009; gateway, cobrança real e proration |
| Coletivo | COL-002; COL-301 a 304; TRN-411 a 418 | materializados | TRN-417/418 integrais; TRN-411..415 locais; TRN-416 parcial | cobrança real e processo após BND-002 |
| Organização | ORG-001; ORG-301 a 304; TRN-421 a 428 | materializados | TRN-427/428 integrais; TRN-421..425 locais; TRN-426 parcial | cobrança real e processo após BND-002 |
| fronteira comercial | BND-002 | sem tela por definição | parcial | proposta, contrato, dimensionamento e handoffs posteriores |

`BND-002` permanece fronteira genérica de contratação/dimensionamento assistido e não plano específico.

## 6. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral → gestão de solicitações | COL-002; TRN-112; COL-003 | materializados | integralmente validada | nenhuma nesta ligação |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | materializados | integralmente validada | aprovação fechada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | materializados | integralmente validada | nenhuma nesta ligação |
| Meus Coletivos → Central | PER-106; TRN-110; PER-107 | materializados | integralmente validada | nenhuma nesta ligação |
| Central → Início do Participante | PER-107; TRN-111; PER-108 | materializados | integralmente validada | estados P0B e áreas internas separados |
| Visão Geral → Planos → Visão Geral | COL-002; TRN-417/418; COL-301 | materializados | integralmente validada por UXA-100-A4 | nenhuma nesta ligação |

## 7. Fila por dependência

A fila não autoriza execução automática.

| Grupo | Lacuna | IDs relacionados | Estado visual | Gate |
|---|---|---|---|---|
| D5-C integração | Hoje ↔ Meus Objetivos | PER-008; PER-010; TRN-008/009 | superfícies validadas | validar identidade, contexto/payload, retorno, interrupção, concorrência, idempotência e autoridade |
| D5-C integração | Hoje ↔ Meus Próximos Passos | PER-008; PER-011; TRN-010/011 | superfícies validadas | validar identidade, contexto/payload, retorno, interrupção, concorrência, idempotência e autoridade |
| D5-C integração | Hoje ↔ Minha Evolução | PER-008; PER-012; TRN-012/013 | superfícies validadas | validar identidade, contexto/payload, retorno, interrupção, concorrência, idempotência, autoridade e sensibilidade |
| P0B | Meus Coletivos | PER-106 | P0A validado | ativo próprio quando decisão/proteção justificar |
| P0B | Central | PER-107 | P0A validado | vazio, excesso de volume e baixa conectividade |
| P0B | Início do Participante | PER-108 | P0A validado | mudança material de decisão/proteção |
| operação interna | Coletivo | COL-004 a 007; TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| bilateral | Organização–Coletivo | ORG-004 a 006; COL-008 | sem SVGs | materialização e validação bilateral |
| institucional | matriz completa | ORG-001; ORG-007 | cobertura parcial | programa específico e validação |
| Conta | Conta/Configurações | PER-009; TRN-406/407 | sem SVG | materializar se arquitetura exigir |
| comercial | contratação assistida | BND-002; TRN-416/426 | fronteira registrada | contrato comercial/operacional suficiente |

## 8. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 — encerrado | compreensão inicial → Tela Hoje | TRN-007 integral | UXA-097 |
| V2 — encerrado | publicação → descoberta e Mapa/Lista/Detalhe | TRN-203/204/210/211 integrais | UXA-098 |
| V3 — encerrado | dez estados residuais Opportunity Boost | 10 SVGs validados | UXA-099 |
| Planos — identidade | fragmentação e promoção canônica | encerrada | UXA-100-A3 |
| Planos — origem voluntária | Conta/Administração → Planos → retorno | 4 integrais e 2 contratados | UXA-100-A4 |
| V4 — encerrado | Detalhe → fronteira externa | TRN-205 integral até BND-001 | UXA-101 |
| D5-C1 | contrato arquitetural | PER-010..012 + TRN-008..013 contratados | concluído |
| D5-C2 | materialização low-fidelity | 3 SVGs materializados | concluído |
| D5-C3 | validação/reformulação local | **PER-010..012 validados; 0 SVGs pendentes** | concluído localmente; TRNs separados |
| V5 | erros, retornos e interrupções | cobertura dispersa | **não iniciada** |

## 9. Baseline após D5-C3

- SVGs canônicos: **121**;
- associações: **121**;
- perfis: **34**;
- validações funcionais vigentes de SVG: **121**;
- pendências específicas de SVG: **0**;
- superfícies/estados/fronteiras: **57**;
- transições: **66**;
- IDs com referência visual: **45 de 57**;
- responsabilidades sem SVG dedicado: **10**;
- fronteiras sem tela: **2**;
- `PER-010..012` materializados, reformulados e validados localmente;
- `TRN-008..013` e `TRN-406/407` contratadas;
- `TRN-417/418` e `TRN-427/428` integralmente validadas no limite documental;
- nenhuma implementação técnica criada.

## 10. Critérios preservados

- validação local de superfície não equivale a validação automática de transição;
- navegar para Objetivos não cria ou confirma Objetivo;
- navegar para Próximos Passos não inicia ou conclui movimento;
- navegar para Minha Evolução não presume mudança, progresso ou reconhecimento;
- domínio não é score, diagnóstico, identidade ou prova de evolução;
- dimensão estrutural do Contexto Vivo não é Domínio de Evolução;
- aspecto descritivo da mudança não é Domínio de Evolução;
- navegar para Planos não equivale a selecionar plano ou iniciar cobrança;
- plano pago não compra relevância, confiança, impacto, legitimidade ou evolução;
- validação documental não equivale a implementação técnica.

## 11. Próximo ato possível

Após integração governada da D5-C3, a validação ponta a ponta de `TRN-008..013` pode constituir frente posterior separada. Isso não inicia automaticamente V5/UXA-102, D6, D7, Product Engineering ou qualquer outra lacuna.