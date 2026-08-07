---
id: GKR-JOURNEY-SURFACE-REGISTRY-001
title: Registro Granular de Superfícies e Estados
status: active
version: 0.11.0
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
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
normative: false
---

# Registro Granular de Superfícies e Estados

## 1. Finalidade

Este registro atribui identificadores estáveis a superfícies, estados, responsabilidades conhecidas e fronteiras documentais das Jornadas Integradas.

A versão 0.11.0 preserva as 40 entradas. A UXA-094 não cria ID: reforma e revalida `PER-106`, valida `PER-107` e preserva `PER-108` como responsabilidade ainda não materializada na forma vigente.

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
| Pessoa | 19 |
| Coletivo | 8 |
| Organização | 7 |
| camada comercial | 5 |
| fronteira documental | 1 |
| **Total** | **40** |

## 4. Inventário principal

| ID | Superfície, estado ou responsabilidade | Perspectiva e família | Canal | Maturidade | Autoridade | Materialização | Validação | Detalhamento obrigatório |
|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-001 | Home pública | visitante; início protegido | público | validado | UXA-020 | UXA-022 | UXA-021 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-002 | entrada protegida | Pessoa | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-003 | escolha de modalidade | Pessoa | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-004 | expressão por texto ou voz | Pessoa | protegido | validado | UXA-068 | UXA-068 | UXA-069 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-005 | inventário e autorização | Pessoa | protegido | validado | UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-006 | processamento visível | Pessoa | protegido | validado | UXA-023 | UXA-036 | UXA-037 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-007 | compreensão inicial revisável | Pessoa | protegido | validado | UXA-023 | UXA-036 | UXA-037 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-008 | Tela Hoje | Pessoa autenticada | protegido | validado | UXA-002 | UXA-006 | UXA-010 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-101 | Explorar Coletivos | visitante | móvel | validado | UXA-056 | UXA-060 | UXA-061 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-102 | Resultados de Busca de Coletivos | visitante | móvel | validado | UXA-056 | UXA-060 | UXA-061 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-103 | Perfil Público do Coletivo | visitante | móvel | validado | UXA-056 | UXA-062 | UXA-063 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-104 | revisão e solicitação | solicitante | móvel | validado | UXA-056 | UXA-064 | UXA-065 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-105 | Solicitação Pendente | solicitante | móvel | validado | UXA-056 | UXA-066; UXA-091/092 no aprovado | UXA-067; UXA-092 no aprovado | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-106 | Meus Coletivos | participante | móvel | **validado** | UXA-056; UXA-059 | UXA-091; reformulações UXA-092/094 | UXA-092; gatilho revalidado UXA-094 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-107 | Central de Atualizações | participante | móvel | **validado** | UXA-058; UXA-059 | UXA-093; reformulação UXA-094 | **UXA-094** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-108 | Início do Participante | participante | não definido | reformulação pendente | UXA-059 | referência anterior não promovida | — | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-201 | Mapa de Oportunidades | Pessoa/visitante | móvel e computador | validado | UXA-004 | UXA-024 | UXA-025 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-202 | Lista de Oportunidades | Pessoa/visitante | móvel e computador | validado | UXA-004 | UXA-028 | UXA-029 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-203 | Detalhe de Oportunidade | Pessoa/visitante | móvel e computador | validado | UXA-004; UXA-007 | UXA-007 | UXA-012 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-COL-001 | presença pública existente | visitante/responsável | público e protegido | materializado | UXA-014; UXA-056 | UXA-016 | UXA-018; UXA-063 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-002 | Visão Geral do Responsável | responsável | computador protegido | validado | UXA-014; UXA-059 | UXA-086/087 | UXA-087 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-003 | gestão de solicitações | responsável | computador protegido | validado | UXA-056; UXA-059 | UXA-088/089 | UXA-089; handoffs UXA-090/092 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-004 | participantes e vínculos | responsável | protegido | programado | UXA-059 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-005 | comunicação oficial | responsável | protegido | programado | UXA-058; UXA-059 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-006 | atividades, consultas e decisões | responsável | protegido | programado | UXA-059 | parcial/dispersa | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-007 | proteção e moderação | responsável | protegido | contratado | UXA-058 | parcial | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-008 | relações institucionais | responsável | protegido | contratado | UXA-019 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-ORG-001 | Visão Geral da Organização | representante | protegido | validado | UXA-014 | UXA-015 | UXA-017 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-002 | cadastro de oportunidade | representante | protegido | validado | UXA-004 | UXA-008 | UXA-013 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-003 | oportunidade aprovada/ativa | representante | protegido | validado | UXA-004 | UXA-008 | UXA-013 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-004 | proposta de relação com Coletivo | representante | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-005 | avaliação e negociação bilateral | representantes | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-006 | relação ativa e revisão | representantes | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-007 | resultados e evidências institucionais | representante | protegido | indeterminado | referências dispersas | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-COM-001 | configuração do anunciante | anunciante | protegido | materializado | UXA-038 | UXA-040 | UXA-041 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-002 | cartão patrocinado e explicação | Pessoa exposta | público/protegido | validado | UXA-038 | UXA-042 | UXA-043 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-003 | estados patrocinados de lista/mapa | Pessoa exposta | público/protegido | validado | UXA-038 | UXA-044 | UXA-045 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-004 | gestão de campanha ativa | anunciante | protegido | materializado | UXA-038 | UXA-046 | não consolidada aqui | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-005 | dez estados residuais | anunciante/Pessoa | diversos | materializado | UXA-038 | UXA-055 | — | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-BND-001 | fronteira externa identificada | Pessoa | externo | indeterminado | UXA-004; UXA-007 | — | — | [Comercial](surface-registry-commercial-boundary-details.md) |

## 5. Divisões controladas

- `PER-106` é central de participações e estados relacionados, não feed;
- `PER-107` é triagem de atualizações, não substitui canais especializados ou `PER-108`;
- `PER-108` permanece responsabilidade sem tela vigente;
- `COM-005` continua sem validação funcional específica;
- `BND-001` é endpoint documental, não tela.

## 6. Efeito da UXA-094

- 40 IDs preservados;
- `PER-106` permanece validado após reformulação do gatilho;
- `PER-107` passa a validado;
- `PER-108` permanece reformulação pendente;
- a validação de `TRN-110` é registrada no instrumento próprio de transições.

## 7. Estado

O registro permanece `active`. Seu status aprova o instrumento documental, não a implementação das superfícies.
