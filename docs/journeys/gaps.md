---
id: GKR-JOURNEY-GAPS-001
title: Lacunas e Continuidades Ausentes
status: active
version: 0.34.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-26
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
  - GKR-UX-D5-C4A-001
  - GKR-UX-D5-C4B-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
---

# Lacunas e Continuidades Ausentes

## 1. Natureza do registro

Este documento é observacional e não promocional. A D5-C1 fechou a identidade arquitetural de `Meus Objetivos`, `Meus Próximos Passos` e `Minha Evolução`; a D5-C2 fechou a ausência visual do estado-base; a D5-C3 fechou a validação funcional local dos três SVGs; a D5-C4A fechou a ausência de origem visual inequívoca no estado recorrente de Hoje e governou o contrato semântico; a D5-C4B fecha a **lacuna específica de validação integrada de `TRN-008..013`** no limite documental.

A reconciliação pós-PR #313/#314 adiciona duas lacunas explícitas que haviam sido ocultadas por artefatos prematuros:

- arquitetura da informação + wireframe principal autenticado da Organização;
- arquitetura da informação + wireframe principal autenticado do Coletivo.

`UXA-015..018` permanecem históricos `superseded`. Estados sensíveis/alternativos específicos, V5/UXA-102, D6, D7, cobrança real e demais frentes continuam separadas.

## 2. Gates pessoais

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| compreensão inicial → primeira Tela Hoje | PER-007; TRN-007; PER-008 | materializados | integralmente validada por UXA-097 | recorrência e estados alternativos separados |
| Home pública → entrada protegida | PER-001; TRN-001; PER-002 | materializados | parcial | validação integrada |
| escolha → expressão | PER-003; TRN-003; PER-004 | materializados | parcial | validação integrada |
| expressão → inventário | PER-004; TRN-004; PER-005 | materializados | parcial | integração com inventário |
| inventário → processamento | PER-005; TRN-005; PER-006 | materializados | parcial | continuidade entre materializações |
| Conta/Configurações da Pessoa | PER-009; TRN-406/407 | sem SVG dedicado | identidade contratada pela UXA-100-A4 | materialização própria somente se necessária para validar ponta a ponta |
| Hoje ↔ Meus Objetivos | PER-008; TRN-008/009; PER-010 | Hoje recorrente D5-C4A + PER-010 validado D5-C3 | **TRN-008/009 integralmente validadas por D5-C4B** | nenhuma nesta ligação; estados alternativos separados |
| Hoje ↔ Meus Próximos Passos | PER-008; TRN-010/011; PER-011 | Hoje recorrente D5-C4A + PER-011 validado D5-C3 | **TRN-010/011 integralmente validadas por D5-C4B** | nenhuma nesta ligação; estados alternativos separados |
| Hoje ↔ Minha Evolução | PER-008; TRN-012/013; PER-012 | Hoje recorrente D5-C4A + PER-012 validado D5-C3 | **TRN-012/013 integralmente validadas por D5-C4B** | estados sensíveis adicionais quando aplicáveis |

`PER-010..012` não são estados internos de Hoje. Para `TRN-008/010/012`, a validação se aplica ao estado recorrente de Hoje quando o affordance estiver presente e aplicável; a primeira variante UXA-097 não é obrigada a expor os três acessos. Não existem handoffs diretos governados entre as três superfícies especializadas.

## 3. Gates de oportunidade e descoberta

| Continuidade | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| publicação/ativação → descoberta | ORG-003; TRN-203; PER-201 | materializados | **integralmente validada por UXA-098** | integração patrocinada separada |
| Mapa → Lista | PER-201; TRN-210; PER-202 | materializados | **integralmente validada** | nenhuma nesta ligação |
| Mapa → Detalhe | PER-201; TRN-204; PER-203 | materializados | **integralmente validada** | saída externa governada por UXA-101 |
| Lista → Detalhe | PER-202; TRN-211; PER-203 | materializados | **integralmente validada** | saída externa governada por UXA-101 |
| Detalhe → fronteira externa | PER-203; TRN-205; BND-001 | Detalhe reformulado; fronteira sem tela | **integralmente validada até a fronteira Guivos por UXA-101** | processo e resultado posteriores pertencem ao terceiro |
| patrocinado → Mapa/Lista orgânicos | COM-002; TRN-304/306; PER-201/PER-202 | materializados | parcial | integração orgânico–patrocinado específica |

A supersessão do wireframe principal da Organização não invalida `ORG-002/003` nem o fluxo especializado de publicação/descoberta, que possuem autoridades próprias.

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
| Coletivo | COL-002; COL-301 a 304; TRN-411 a 418 | pacote de Planos materializado; origem administrativa principal final pendente | TRN-417/418 preservam maturidade do contrato especializado; TRN-411..415 locais; TRN-416 parcial | **wireframe principal autenticado do Coletivo**; cobrança real e processo após BND-002 |
| Organização | ORG-001; ORG-301 a 304; TRN-421 a 428 | pacote de Planos materializado; ORG-001 histórico superseded como wireframe principal | TRN-427/428 preservam maturidade do contrato especializado; TRN-421..425 locais; TRN-426 parcial | **wireframe principal autenticado da Organização**; cobrança real e processo após BND-002 |
| fronteira comercial | BND-002 | sem tela por definição | parcial | proposta, contrato, dimensionamento e handoffs posteriores |

`BND-002` permanece fronteira genérica de contratação/dimensionamento assistido e não plano específico.

```text
CONTRATO DE ORIGEM/RETORNO DE PLANOS
≠ WIREFRAME PRINCIPAL VIGENTE
```

## 6. Gates de Coletivos

| Lacuna | IDs relacionados | Estado visual | Estado funcional | Continuidade remanescente |
|---|---|---|---|---|
| arquitetura principal autenticada do Coletivo | COL-001/COL-002 e áreas internas | **pendente; UXA-016/018 superseded; UXA-086/087 apenas evidência administrativa local** | fundamentos e contratos existentes | arquitetura da informação → mapa de superfícies → wireframe → validação |
| Visão administrativa local → gestão de solicitações | COL-002; TRN-112; COL-003 | origem local + fluxo especializado materializado | TRN-112 preserva maturidade documental própria | integração final deverá ser revista contra a futura arquitetura principal |
| solicitação ↔ operação responsável | PER-105; TRN-105/106/107/109; COL-003 | materializados | integralmente validada | aprovação fechada em TRN-108 |
| continuidade pós-aprovação | PER-105; TRN-108; PER-106 | materializados | integralmente validada | nenhuma nesta ligação |
| Meus Coletivos → Central | PER-106; TRN-110; PER-107 | materializados | integralmente validada | nenhuma nesta ligação |
| Central → Início do Participante | PER-107; TRN-111; PER-108 | materializados | integralmente validada no recorte da Pessoa participante | estados P0B e áreas internas separados |
| contexto administrativo → Planos → contexto administrativo | COL-002; TRN-417/418; COL-301 | pacote especializado materializado | TRN-417/418 preservam maturidade do contrato especializado | integração final deverá ser revista contra a futura arquitetura principal |

## 7. Fila por dependência

A fila não autoriza execução automática.

| Grupo | Lacuna | IDs relacionados | Estado visual | Gate |
|---|---|---|---|---|
| P0B | Meus Coletivos | PER-106 | P0A validado | ativo próprio quando decisão/proteção justificar |
| P0B | Central | PER-107 | P0A validado | vazio, excesso de volume e baixa conectividade |
| P0B | Início do Participante | PER-108 | P0A validado | mudança material de decisão/proteção |
| UX principal | Coletivo autenticado | COL-001/COL-002; COL-004 a 008 | **wireframe principal pendente** | papéis/jobs → arquitetura da informação → mapa de superfícies → fluxos → wireframe → validação |
| UX principal | Organização autenticada | ORG-001; ORG-004 a 007 | **wireframe principal pendente** | papéis/jobs → arquitetura da informação → mapa de superfícies → fluxos → wireframe → validação |
| operação interna | Coletivo | COL-004 a 007; TRN-113 | sem SVGs dedicados | programa, materialização e validação |
| bilateral | Organização–Coletivo | ORG-004 a 006; COL-008 | sem SVGs | materialização e validação bilateral |
| institucional | matriz completa | ORG-001; ORG-007 | cobertura parcial; ORG-001 histórico não é baseline | programa específico e validação |
| Conta | Conta/Configurações | PER-009; TRN-406/407 | sem SVG | materializar se arquitetura exigir |
| comercial | contratação assistida | BND-002; TRN-416/426 | fronteira registrada | contrato comercial/operacional suficiente |
| patrocinado | integração orgânico–patrocinado | TRN-304/305/306 | materializados parcialmente | validação ponta a ponta específica |

A lacuna D5-C de `TRN-008..013` não integra mais esta fila após D5-C4B.

## 8. Fila de validação

| Prioridade | Continuidade ou família | Estado atual | Gate |
|---:|---|---|---|
| V1 — encerrado | compreensão inicial → Tela Hoje | TRN-007 integral | UXA-097 |
| V2 — encerrado | publicação → descoberta e Mapa/Lista/Detalhe | TRN-203/204/210/211 integrais | UXA-098 |
| V3 — encerrado | dez estados residuais Opportunity Boost | 10 SVGs validados | UXA-099 |
| Planos — identidade | fragmentação e promoção canônica | encerrada | UXA-100-A3 |
| Planos — origem voluntária | contratos de Conta/Administração → Planos → retorno | maturidades próprias preservadas; **não provar UI principal de Organização/Coletivo** | UXA-100-A4 + reconciliação pós-313/314 |
| V4 — encerrado | Detalhe → fronteira externa | TRN-205 integral até BND-001 | UXA-101 |
| D5-C1 | contrato arquitetural | PER-010..012 + TRN-008..013 contratados | concluído |
| D5-C2 | materialização low-fidelity | 3 SVGs materializados | concluído |
| D5-C3 | validação/reformulação local | PER-010..012 validados | concluído localmente |
| D5-C4A | origens + contrato dos handoffs | Hoje recorrente reformulado/revalidado | concluído sem promoção |
| D5-C4B — encerrado | validação integrada de TRN-008..013 | **6 transições integralmente validadas** | GKR-UX-D5-C4B-001 |
| ORGCOL-UX | UX principal de Organização e Coletivo | **wireframes principais pendentes** | sequência governada de arquitetura/UX |
| V5 | erros, retornos e interrupções | cobertura dispersa | **não iniciada** |

## 9. Baseline após reconciliação pós-313/314

- SVGs físicos no inventário: **121**;
- associações físicas: **121**;
- perfis: **34**;
- antiga claim agregada `121 validações funcionais vigentes / 0 pendências`: **superseded como maturidade atual**;
- nova contagem agregada de wireframes vigentes/validados: **não inferida; recomputação governada pendente**;
- superfícies/estados/fronteiras: **57**;
- transições: **66**;
- IDs com referência visual no snapshot: **45 de 57**;
- responsabilidades sem SVG dedicado no snapshot: **10**;
- fronteiras sem tela: **2**;
- `PER-008` recorrente reformulado/revalidado localmente;
- `PER-010..012` materializados, reformulados e validados localmente;
- `TRN-008..013` preservam validação documental própria;
- `TRN-417/418` e `TRN-427/428` preservam maturidade de contratos especializados, sem provar wireframes principais vigentes;
- `TRN-406/407` contratadas;
- wireframe principal autenticado da Organização: **pendente**;
- wireframe principal autenticado do Coletivo: **pendente**;
- nenhuma implementação técnica criada.

## 10. Critérios preservados

- validação integrada documental não equivale a implementação técnica;
- navegar para Objetivos não cria ou confirma Objetivo;
- navegar para Próximos Passos não inicia ou conclui movimento;
- navegar para Minha Evolução não presume mudança, progresso ou reconhecimento;
- `Abrir este passo` pode preservar referência lógica mínima, mas não inicia o passo;
- contexto de navegação não amplia consentimento, autorização, prioridade ou progresso;
- domínio não é score, diagnóstico, identidade ou prova de evolução;
- dimensão estrutural do Contexto Vivo não é Domínio de Evolução;
- aspecto descritivo da mudança não é Domínio de Evolução;
- navegar para Planos não equivale a selecionar plano ou iniciar cobrança;
- plano pago não compra relevância, confiança, impacto, legitimidade ou evolução;
- existência física de SVG não equivale a vigência;
- fluxo especializado validado não equivale a jornada principal validada.

## 11. Próximo ato possível

A D5-C4B encerra a lacuna específica dos seis handoffs pessoais. A reconciliação pós-313/314 reabre corretamente como lacunas explícitas apenas aquilo que havia sido antecipado indevidamente: a UX principal autenticada de Organização e Coletivo.

Isso não inicia automaticamente V5/UXA-102, D6, D7, Product Engineering ou qualquer outra lacuna. A futura construção de Organização/Coletivo deve seguir: fundamentos → papéis/jobs → arquitetura da informação → mapa de superfícies → fluxos/estados → wireframes → validação → UI → protótipo → testes → handoff.