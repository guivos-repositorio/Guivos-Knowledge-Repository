---
id: GKR-JOURNEY-SURFACE-REGISTRY-001
title: Registro Granular de Superfícies e Estados
status: active
version: 0.16.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-070
  - UXA-080
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
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
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
normative: false
---

# Registro Granular de Superfícies e Estados

## 1. Finalidade

Este registro atribui identificadores estáveis a superfícies, estados, responsabilidades conhecidas e fronteiras documentais das Jornadas Integradas.

A versão 0.16.0 incorpora a promoção canônica da UXA-100-A3: quatro famílias de Planos por participante e uma fronteira compartilhada para processo comercial Enterprise/Scale. A fragmentação segue a UXA-059 e não converte cada estado do board em tela independente.

## 2. Convenções

- `ausente`: responsabilidade conhecida sem materialização necessária;
- `indeterminado`: evidência insuficiente;
- `não examinado`: integração ainda não avaliada;
- `parcial`: cobertura incompleta;
- `materializado`: referência existente sem implicar validação;
- `validado`: superfície examinada funcionalmente;
- `local`: validação limitada ao pacote de origem.

## 3. Contagem

| Categoria | Quantidade |
|---|---:|
| Pessoa | 23 |
| Coletivo | 12 |
| Organização | 11 |
| camada comercial | 5 |
| fronteira documental | 2 |
| **Total** | **53** |

## 4. Inventário principal

| ID | Superfície, estado ou responsabilidade | Perspectiva e família | Canal | Maturidade | Autoridade | Materialização | Validação | Detalhamento obrigatório |
|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-001 | Home pública | visitante; início protegido | público | validado | UXA-020 | UXA-022 | UXA-021 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-002 | entrada protegida | Pessoa | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-003 | escolha de modalidade | Pessoa | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-004 | expressão por texto ou voz | Pessoa | protegido | validado | UXA-068 | UXA-068 | UXA-069 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-005 | inventário e autorização | Pessoa | protegido | validado | UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-006 | processamento visível | Pessoa | protegido | validado | UXA-023 | UXA-036 | UXA-037 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-007 | compreensão inicial revisável | Pessoa | protegido | **validado** | UXA-023 | UXA-036; decisão refinada UXA-097 | UXA-037; variante corrente revalidada UXA-097 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-008 | Tela Hoje | Pessoa autenticada | protegido | **validado** | UXA-002; UXA-011-A1 | UXA-006 recorrente; primeira variante UXA-097 | UXA-010 recorrente; primeira variante UXA-097 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-101 | Explorar Coletivos | visitante | móvel | validado | UXA-056 | UXA-060 | UXA-061 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-102 | Resultados de Busca de Coletivos | visitante | móvel | validado | UXA-056 | UXA-060 | UXA-061 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-103 | Perfil Público do Coletivo | visitante | móvel | validado | UXA-056 | UXA-062 | UXA-063 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-104 | revisão e solicitação | solicitante | móvel | validado | UXA-056 | UXA-064 | UXA-065 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-105 | Solicitação Pendente | solicitante | móvel | validado | UXA-056 | UXA-066; UXA-091/092 no aprovado | UXA-067; UXA-092 no aprovado | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-106 | Meus Coletivos | participante | móvel | **validado** | UXA-056; UXA-059 | UXA-091; reformulações UXA-092/094 | UXA-092; gatilho revalidado UXA-094 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-107 | Central de Atualizações | participante | móvel | **validado** | UXA-058; UXA-059 | UXA-093; reformulações UXA-094/095/096 | UXA-094; versão corrente revalidada UXA-096 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-108 | Início do Participante | participante | móvel | **validado** | UXA-016; UXA-018; UXA-056; UXA-058; UXA-059 | UXA-095; reformulação UXA-096 | **UXA-096** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-201 | Mapa de Oportunidades | Pessoa/visitante | móvel e computador | validado | UXA-004 | UXA-024 | UXA-025 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-202 | Lista de Oportunidades | Pessoa/visitante | móvel e computador | validado | UXA-004 | UXA-028 | UXA-029 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-203 | Detalhe de Oportunidade | Pessoa/visitante | móvel e computador | validado | UXA-004; UXA-007 | UXA-007 | UXA-012 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-301 | Planos e comparação da Pessoa | Pessoa autenticada | móvel/protegido | **validado** | GEM-004-A1/A2; UXA-100-A3 | UXA-100/A1 | **UXA-100-A2; promoção UXA-100-A3** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-302 | revisão de contratação da Pessoa | Pessoa/pagador autorizado | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-303 | gestão de downgrade e cancelamento da Pessoa | Pessoa titular | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-304 | resultado e recuperação de plano/cobrança da Pessoa | Pessoa titular | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-COL-001 | presença pública existente | visitante/responsável | público e protegido | materializado | UXA-014; UXA-056 | UXA-016 | UXA-018; UXA-063 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-002 | Visão Geral do Responsável | responsável | computador protegido | validado | UXA-014; UXA-059 | UXA-086/087 | UXA-087 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-003 | gestão de solicitações | responsável | computador protegido | validado | UXA-056; UXA-059 | UXA-088/089 | UXA-089; handoffs UXA-090/092 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-004 | participantes e vínculos | responsável | protegido | programado | UXA-059 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-005 | comunicação oficial | responsável | protegido | programado | UXA-058; UXA-059 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-006 | atividades, consultas e decisões | responsável | protegido | programado | UXA-059 | parcial/dispersa | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-007 | proteção e moderação | responsável | protegido | contratado | UXA-058 | parcial | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-008 | relações institucionais | responsável | protegido | contratado | UXA-019 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-301 | Planos e comparação do Coletivo | responsável autorizado | computador/protegido | **validado** | GEM-004-A1/A2; UXA-100-A3 | UXA-100/A1 | **UXA-100-A2; promoção UXA-100-A3** | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-302 | revisão de contratação do Coletivo | responsável financeiro autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-303 | gestão de downgrade e cancelamento do Coletivo | responsável autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-304 | resultado e recuperação de plano/cobrança do Coletivo | responsável autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-ORG-001 | Visão Geral da Organização | representante | protegido | validado | UXA-014 | UXA-015 | UXA-017 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-002 | cadastro de oportunidade | representante | protegido | validado | UXA-004 | UXA-008 | UXA-013 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-003 | oportunidade aprovada/ativa | representante | protegido | validado | UXA-004 | UXA-008 | UXA-013 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-004 | proposta de relação com Coletivo | representante | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-005 | avaliação e negociação bilateral | representantes | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-006 | relação ativa e revisão | representantes | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-007 | resultados e evidências institucionais | representante | protegido | indeterminado | referências dispersas | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-301 | Planos e comparação da Organização | representante autorizado | computador/protegido | **validado** | GEM-004-A1/A2; UXA-100-A3 | UXA-100/A1 | **UXA-100-A2; promoção UXA-100-A3** | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-302 | revisão de contratação da Organização | autoridade financeira identificada | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-303 | gestão de downgrade e cancelamento da Organização | representante autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-304 | resultado e recuperação de plano/cobrança da Organização | representante autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | **UXA-100-A2; promoção UXA-100-A3** | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-COM-001 | configuração do anunciante | anunciante | protegido | materializado | UXA-038 | UXA-040 | UXA-041 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-002 | cartão patrocinado e explicação | Pessoa exposta | público/protegido | validado | UXA-038 | UXA-042 | UXA-043 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-003 | estados patrocinados de lista/mapa | Pessoa exposta | público/protegido | validado | UXA-038 | UXA-044 | UXA-045 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-004 | gestão de campanha ativa | anunciante | protegido | materializado | UXA-038 | UXA-046/053 | UXA-047/054 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-005 | dez estados residuais | anunciante/Pessoa | diversos | **validado** | UXA-038 | UXA-055 | **UXA-099** | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-BND-001 | fronteira externa identificada | Pessoa | externo | indeterminado | UXA-004; UXA-007 | — | — | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-BND-002 | processo comercial Enterprise/Scale | Coletivo/Organização | fronteira comercial | contratado | GEM-004-A1/A2; UXA-100-A3 | CTA/handoff nos boards UXA-100 | parcial; processo posterior não materializado | [Comercial](surface-registry-commercial-boundary-details.md) |

## 5. Divisões controladas

- `PER-007` mantém compreensão, persistência e personalização como decisões separadas;
- `PER-008` possui variante inicial e recorrente sob o mesmo ID, ambas validadas em seus escopos;
- `PER-106` é central de participações e estados relacionados, não feed;
- `PER-107` é triagem de atualizações e sua versão corrente está validada pela UXA-096;
- `PER-108` é síntese interna validada e não replica Central ou canais especializados;
- `PER/COL/ORG-301` incorporam comparação geral, comparação incremental e delta direto; comparação não cria superfície própria;
- `PER/COL/ORG-302` concentram revisão afirmativa da contratação; processamento transitório não cria ID;
- `PER/COL/ORG-303` concentram downgrade e cancelamento porque compartilham a revisão do ciclo, preservando consequências específicas por modo;
- `PER/COL/ORG-304` agrupam sucesso e falha como estados de resultado/recuperação, sem confundir seus efeitos;
- `BND-002` encerra o autoatendimento antes do processo comercial Enterprise/Scale;
- `COM-005` está funcionalmente validado pela UXA-099; sua validação não promove automaticamente `TRN-305`;
- `BND-001` e `BND-002` são endpoints documentais, não telas.

## 6. Efeito da UXA-100-A3

- superfícies/estados/fronteiras: **40 → 53**;
- Pessoa: **19 → 23**;
- Coletivo: **8 → 12**;
- Organização: **7 → 11**;
- fronteiras documentais: **1 → 2**;
- 12 superfícies de Planos promovidas com validação funcional da UXA-100-A2;
- 1 fronteira comercial adicionada sem simular checkout;
- 9 SVGs de Planos passam ao conjunto canônico;
- nenhuma jornada principal é promovida;
- nenhuma implementação é inferida.

## 7. Estado

O registro permanece `active`. Seu status aprova o instrumento documental e a identidade canônica proposta pela UXA-100-A3, não a implementação das superfícies.