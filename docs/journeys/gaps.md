---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.29.0
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
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A D5-C1 fecha somente a **identidade arquitetural e os handoffs mínimos** de `Meus Objetivos`, `Meus Próximos Passos` e `Minha Evolução`. Materialização visual, validação ponta a ponta, V5/UXA-102, cobrança real e demais frentes continuam separadas.

## 2. Gates pessoais

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| compreensão inicial → primeira Tela Hoje | PER-007; TRN-007; PER-008 | materializados | integralmente validada por UXA-097 | recorrência e estados alternativos separados |
| Home pública → entrada protegida | PER-001; TRN-001; PER-002 | materializados | parcial | validação integrada |
| escolha → expressão | PER-003; TRN-003; PER-004 | materializados | parcial | validação integrada |
| expressão → inventário | PER-004; TRN-004; PER-005 | materializados | parcial | integração com inventário |
| inventário → processamento | PER-005; TRN-005; PER-006 | materializados | parcial | continuidade entre materializações |
| Conta/Configurações da Pessoa | PER-009; TRN-406/407 | sem SVG dedicado | identidade contratada pela UXA-100-A4 | materialização própria somente se necessária para validar ponta a ponta |
| Hoje ↔ Meus Objetivos | PER-008; TRN-008/009; PER-010 | PER-010 sem SVG | responsabilidade e handoffs contratados pela D5-C1 | materialização e validação ponta a ponta em frente própria |
| Hoje ↔ Meus Próximos Passos | PER-008; TRN-010/011; PER-011 | PER-011 sem SVG | responsabilidade e handoffs contratados pela D5-C1 | materialização e validação ponta a ponta em frente própria |
| Hoje ↔ Minha Evolução | PER-008; TRN-012/013; PER-012 | PER-012 sem SVG | responsabilidade e handoffs contratados pela D5-C1 | materialização e validação ponta a ponta em frente própria |

`PER-010..012` não são estados internos de Hoje. A D5-C1 reconhece responsabilidades próprias, mas não cria SVG nem valida navegação. Também não existem, nesta frente, handoffs diretos `PER-010 ↔ PER-011`, `PER-011 ↔ PER-012` ou `PER-010 ↔ PER-012`.

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
| Pessoa | PER-009; PER-301 a 304; TRN-401 a 407 | PER-009 sem SVG; 3 SVGs canônicos de Planos | PER-301..304 validadas; TRN-401..405 locais; TRN-406/407 contratadas | materialização de PER-009 para validação ponta a ponta; gateway, cobrança real e proration |
| Coletivo | COL-002; COL-301 a 304; TRN-411 a 418 | origem e 3 SVGs canônicos materializados | TRN-417/418 **integrais**; TRN-411..415 locais; TRN-416 parcial | cobrança real e contratação/dimensionamento assistido após BND-002 |
| Organização | ORG-001; ORG-301 a 304; TRN-421 a 428 | origem e 3 SVGs canônicos materializados | TRN-427/428 **integrais**; TRN-421..425 locais; TRN-426 parcial | cobrança real e contratação/dimensionamento assistido após BND-002 |
| fronteira comercial | BND-002 | sem tela por definição | parcial | proposta, contrato, dimensionamento e handoffs operacionais posteriores |

A origem voluntária não é mais um gap de identidade para as três jornadas. Para Pessoa, a lacuna remanescente é de **materialização/validação** de `PER-009`, não de existência semântica do ponto de origem.

`BND-002` é fronteira genérica de contratação/dimensionamento assistido. Não pertence semanticamente a Enterprise, Scale, Coletivo, Organização ou a qualquer plano específico.

## 6. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| Visão Geral do Responsável → gestão de solicitações | COL-002; TRN-112; COL-003 | materializados | integralmente validada | nenhuma nesta ligação |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | materializados | integralmente validada | aprovação fechada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | materializados | integralmente validada | nenhuma nesta ligação |
| Meus Coletivos → Central | PER-106; TRN-110; PER-107 | materializados | integralmente validada | nenhuma nesta ligação |
| Central → Início do Participante | PER-107; TRN-111; PER-108 | materializados | integralmente validada | estados P0B e áreas internas separados |
| Visão Geral → Planos → Visão Geral | COL-002; TRN-417/418; COL-301 | materializados | **integralmente validada por UXA-100-A4** | nenhuma nesta ligação de navegação |

## 7. Fila de materialização por dependência

A fila abaixo não autoriza execução automática. Ela apenas registra dependências e separa lacunas já identificadas.

| Prioridade documental | Lacuna | IDs relacionados | Estado visual | Gate |
|---:|---|---|---|---|
| D5-C visual | Meus Objetivos | PER-010; TRN-008/009 | sem SVG | programa visual próprio + materialização + validação |
| D5-C visual | Meus Próximos Passos | PER-011; TRN-010/011 | sem SVG | programa visual próprio + materialização + validação |
| D5-C visual | Minha Evolução | PER-012; TRN-012/013 | sem SVG | programa visual próprio + materialização + validação; preservar separação domínio/dimensão/aspecto |
| 1 | estados P0B adicionais de Meus Coletivos | PER-106 | P0A validado | ativo próprio somente quando decisão/proteção justificar |
| 2 | estados P0B da Central | PER-107 | P0A validado | vazio, excesso de volume e baixa conectividade em frente própria |
| 3 | estados alternativos do Início do Participante | PER-108 | P0A validado | materializar somente mudança material de decisão/proteção |
| 4 | participantes e operação interna | COL-004 a 007; TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| 5 | relação Organização–Coletivo | ORG-004 a 006; COL-008 | sem SVGs | materialização e validação bilateral |
| 6 | matriz institucional completa | ORG-001; ORG-007 | cobertura parcial | programa específico e validação |
| 7 | Conta/Configurações da Pessoa | PER-009; TRN-406/407 | sem SVG dedicado | materializar somente se arquitetura de Conta exigir superfície própria; validar handoffs depois |
| 8 | contratação/dimensionamento assistido | BND-002; TRN-416/426 | fronteira registrada | contrato comercial/operacional suficiente |

A presença das três linhas `D5-C visual` antes da fila numerada não redefine a prioridade das lacunas históricas. Elas representam continuidades diretamente dependentes do contrato D5-C1 e exigem autorização própria por responsabilidade.

## 8. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 — encerrado | compreensão inicial → Tela Hoje | TRN-007 integral | UXA-097 |
| V2 — encerrado | publicação → descoberta e Mapa/Lista/Detalhe | TRN-203/204/210/211 integrais | UXA-098 |
| V3 — encerrado | dez estados residuais Opportunity Boost | 10 SVGs validados | UXA-099 |
| Planos — identidade canônica encerrada | fragmentação e promoção canônica | 12 superfícies da frente + 17 transições internas | UXA-100-A3 |
| Planos — origem voluntária encerrada | Conta/Administração → Planos → retorno | PER-009 + 6 handoffs; 4 integrais e 2 contratados | UXA-100-A4 |
| V4 — encerrado | Detalhe → fronteira externa | TRN-205 integral até BND-001 | UXA-101 |
| D5-C1 — contrato arquitetural | Hoje ↔ Objetivos/Próximos Passos/Evolução | PER-010..012 + TRN-008..013 contratados | materializações visuais separadas; não equivalem a V5 |
| V5 | erros, retornos e interrupções | cobertura dispersa | validação por jornada; **não iniciada** |

## 9. Efeito acumulado vigente

A baseline corrente após D5-C1 passa a ser:

- SVGs canônicos permanecem **118**;
- associações permanecem **118**;
- perfis permanecem **31**;
- superfícies/estados/fronteiras passam a **57**;
- transições passam a **66**;
- IDs com referência visual permanecem **42**, agora de 57;
- responsabilidades sem SVG dedicado passam a **13**;
- fronteiras sem tela permanecem **2**;
- `PER-009`, `PER-010`, `PER-011` e `PER-012` permanecem sem SVG dedicado;
- `TRN-008..013` e `TRN-406/407` permanecem contratadas;
- `TRN-417/418` e `TRN-427/428` permanecem integralmente validadas no limite documental de navegação;
- nenhum SVG novo é criado pela D5-C1;
- `TRN-416/426` permanecem parciais;
- nenhuma implementação técnica é criada.

## 10. Critérios preservados

- validação de superfície não equivale a validação automática de transição;
- validação até uma fronteira não valida comportamento de terceiro;
- navegar para Objetivos não cria ou confirma Objetivo;
- navegar para Próximos Passos não inicia ou conclui movimento;
- navegar para Minha Evolução não presume mudança, progresso ou reconhecimento;
- domínio não é score, diagnóstico, identidade ou prova de evolução;
- dimensão estrutural do Contexto Vivo não é Domínio de Evolução;
- aspecto descritivo da mudança não é Domínio de Evolução;
- navegar para Planos não equivale a selecionar plano ou iniciar cobrança;
- oportunidade pública não é ocultada para vender plano;
- plano pago não compra relevância, confiança, impacto, legitimidade ou evolução;
- contratação assistida não recebe checkout fictício;
- repetição da mesma intenção não duplica efeito lógico;
- validação documental não equivale a implementação técnica.

## 11. Próximo ato possível

A D5-C1 encerra a identidade arquitetural de `PER-010..012` e `TRN-008..013`. Materializar `Meus Objetivos`, `Meus Próximos Passos` ou `Minha Evolução` exige autorização separada por responsabilidade. Materialização de `PER-009`, V5/UXA-102, D6, D7, integrações patrocinadas, cobrança real, processo posterior a `BND-002` e demais lacunas permanecem separadas. Nenhuma próxima frente é iniciada automaticamente.