---
id: GKR-JOURNEY-SURFACE-REGISTRY-001
title: Registro Granular de Superfícies e Estados
status: active
version: 0.6.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-070
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-086
  - UXA-087
  - UXA-088
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-SURFACE-DETAIL-COLLECTIVE-001
  - GKR-JOURNEY-SURFACE-DETAIL-ORGANIZATION-001
  - GKR-JOURNEY-SURFACE-DETAIL-COMMERCIAL-001
normative: false
---

# Registro Granular de Superfícies e Estados

## 1. Finalidade

Este registro atribui identificadores estáveis a superfícies, estados, responsabilidades conhecidas e fronteiras documentais das Jornadas Integradas.

A versão 0.6.0 preserva as 40 entradas e registra a materialização de `GKR-SURF-COL-003` pela UXA-088. Nenhum novo identificador é criado.

## 2. Convenções

- `ausente`: responsabilidade conhecida sem materialização necessária;
- `indeterminado`: evidência insuficiente para valor seguro;
- `não examinado`: integração ainda não avaliada como conjunto;
- `parcial`: cobertura incompleta;
- `materializado`: referência visual ou estrutural existente sem implicar validação;
- `validado`: superfície examinada funcionalmente no escopo indicado;
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

A UXA-088 não altera a contagem; preenche uma entrada já reservada.

## 4. Inventário principal

| ID | Superfície, estado ou responsabilidade | Perspectiva e família | Canal | Maturidade | Autoridade | Materialização | Validação | Detalhamento obrigatório |
|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-001 | Home pública | visitante público; início protegido | público | validado | UXA-020 | UXA-022 | UXA-021 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-002 | entrada protegida | Pessoa; início protegido | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-003 | escolha de modalidade | Pessoa; início protegido | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-004 | expressão por texto ou voz | Pessoa; expressão guiada | protegido | validado | UXA-068 | UXA-068 | UXA-069 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-005 | inventário dos conteúdos e autorização | Pessoa; início protegido | protegido | validado | UXA-023 | UXA-034 | UXA-035 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-006 | processamento visível | Pessoa; compreensão inicial | protegido | validado | UXA-023 | UXA-036 | UXA-037 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-007 | compreensão inicial revisável | Pessoa; compreensão inicial | protegido | validado | UXA-023 | UXA-036 | UXA-037 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-008 | Tela Hoje | Pessoa autenticada; experiência recorrente | protegido | validado | UXA-002 | UXA-006 | UXA-010 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-101 | Explorar Coletivos | visitante; descoberta de Coletivos | móvel | validado | UXA-056 | UXA-060 | UXA-061 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-102 | Resultados de Busca de Coletivos | visitante; descoberta de Coletivos | móvel | validado | UXA-056 | UXA-060 | UXA-061 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-103 | Perfil Público do Coletivo | visitante; presença pública de Coletivo | móvel | validado | UXA-056 | UXA-062 | UXA-063 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-104 | revisão e solicitação | solicitante; participação em Coletivo | móvel | validado | UXA-056 | UXA-064 | UXA-065 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-105 | Solicitação Pendente | solicitante; participação em Coletivo | móvel | validado | UXA-056 | UXA-066 | UXA-067 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-106 | Meus Coletivos | participante; continuidade em Coletivo | não definido | não iniciado | UXA-059 | — | — | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-107 | Central de Atualizações | participante; continuidade em Coletivo | não definido | não iniciado | UXA-059 | — | — | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-108 | Início do Participante | participante; operação interna de Coletivo | não definido | reformulação pendente | UXA-059 | referência anterior não promovida | — | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-201 | Mapa de Oportunidades | Pessoa ou visitante; descoberta de oportunidades | móvel e computador | validado | UXA-004 | UXA-024 | UXA-025 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-202 | Lista de Oportunidades | Pessoa ou visitante; descoberta de oportunidades | móvel e computador | validado | UXA-004 | UXA-028 | UXA-029 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-PER-203 | Detalhe de Oportunidade | Pessoa ou visitante; decisão sobre oportunidade | móvel e computador | validado | UXA-004; UXA-007 | UXA-007 | UXA-012 | [surface-registry-person-details.md](surface-registry-person-details.md) |
| GKR-SURF-COL-001 | Visão Geral ou presença pública existente | visitante e responsável; presença pública de Coletivo | público e protegido | materializado | UXA-014; UXA-056 | UXA-016 e referências relacionadas | UXA-018; UXA-063 no escopo aplicável | [surface-registry-collective-details.md](surface-registry-collective-details.md) |
| GKR-SURF-COL-002 | Visão Geral do Responsável | responsável; operação de Coletivo | computador protegido | validado | UXA-014; UXA-056; UXA-058; UXA-059 | UXA-086; reformulação UXA-087 | UXA-087 | [surface-registry-collective-details.md](surface-registry-collective-details.md) |
| GKR-SURF-COL-003 | gestão de solicitações | responsável; participação em Coletivo | computador protegido | materializado; validação pendente | UXA-056; UXA-059 | UXA-088; 7 SVGs desktop; efeitos na Pessoa em UXA-066 | UXA-067 somente na perspectiva da Pessoa; responsável pendente | [surface-registry-collective-details.md](surface-registry-collective-details.md) |
| GKR-SURF-COL-004 | participantes e vínculos | responsável; vínculos de Coletivo | protegido | programado | UXA-059 | — | — | [surface-registry-collective-details.md](surface-registry-collective-details.md) |
| GKR-SURF-COL-005 | comunicação oficial | responsável; comunicação de Coletivo | protegido | programado | UXA-058; UXA-059 | — | — | [surface-registry-collective-details.md](surface-registry-collective-details.md) |
| GKR-SURF-COL-006 | atividades, consultas e decisões | responsável; operação de Coletivo | protegido | programado | UXA-059 | parcial ou dispersa | — | [surface-registry-collective-details.md](surface-registry-collective-details.md) |
| GKR-SURF-COL-007 | proteção e moderação | responsável; proteção de Coletivo | protegido | contratado | UXA-058 | cobertura parcial | — | [surface-registry-collective-details.md](surface-registry-collective-details.md) |
| GKR-SURF-COL-008 | relações institucionais | responsável; relações institucionais | protegido | contratado | UXA-019 | — | — | [surface-registry-collective-details.md](surface-registry-collective-details.md) |
| GKR-SURF-ORG-001 | Visão Geral da Organização | representante institucional; visão geral institucional | protegido | validado | UXA-014 | UXA-015 | UXA-017 | [surface-registry-organization-details.md](surface-registry-organization-details.md) |
| GKR-SURF-ORG-002 | cadastro de oportunidade | representante institucional; cadastro de oportunidades | protegido | validado | UXA-004 | UXA-008 | UXA-013 | [surface-registry-organization-details.md](surface-registry-organization-details.md) |
| GKR-SURF-ORG-003 | oportunidade aprovada para ativação ou ativa | representante institucional; ciclo institucional de oportunidade | protegido | validado | UXA-004 | UXA-008 | UXA-013 | [surface-registry-organization-details.md](surface-registry-organization-details.md) |
| GKR-SURF-ORG-004 | proposta de relação com Coletivo | representante institucional; relações institucionais | protegido | contratado | UXA-019 | — | — | [surface-registry-organization-details.md](surface-registry-organization-details.md) |
| GKR-SURF-ORG-005 | avaliação e negociação bilateral | representante e responsável; relações institucionais | protegido | contratado | UXA-019 | — | — | [surface-registry-organization-details.md](surface-registry-organization-details.md) |
| GKR-SURF-ORG-006 | relação ativa e revisão | representante e responsável; relações institucionais | protegido | contratado | UXA-019 | — | — | [surface-registry-organization-details.md](surface-registry-organization-details.md) |
| GKR-SURF-ORG-007 | resultados e evidências institucionais | representante institucional; evidências institucionais | protegido | indeterminado | referências dispersas | — | — | [surface-registry-organization-details.md](surface-registry-organization-details.md) |
| GKR-SURF-COM-001 | configuração do fluxo do anunciante | anunciante; Opportunity Boost | protegido | materializado | UXA-038 | UXA-040 | UXA-041 | [surface-registry-commercial-boundary-details.md](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-002 | cartão patrocinado e explicação | Pessoa exposta; Opportunity Boost | público e protegido | validado | UXA-038 | UXA-042 | UXA-043 | [surface-registry-commercial-boundary-details.md](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-003 | estados patrocinados de lista e mapa | Pessoa exposta; Opportunity Boost | público e protegido | validado | UXA-038 | UXA-044 | UXA-045 | [surface-registry-commercial-boundary-details.md](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-004 | gestão da campanha ativa | anunciante; Opportunity Boost | protegido | materializado | UXA-038 | UXA-046 | validação correspondente não consolidada nesta seção | [surface-registry-commercial-boundary-details.md](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-005 | dez estados residuais | anunciante e Pessoa exposta; Opportunity Boost | diversos | materializado | UXA-038 | UXA-055 | — | [surface-registry-commercial-boundary-details.md](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-BND-001 | fronteira externa identificada | Pessoa; fronteira documental | externo | indeterminado | UXA-004; UXA-007 | — | — | [surface-registry-commercial-boundary-details.md](surface-registry-commercial-boundary-details.md) |

## 5. Detalhamentos obrigatórios

Os quatro detalhamentos integram este registro:

- [Pessoa](surface-registry-person-details.md);
- [Coletivo](surface-registry-collective-details.md);
- [Organização](surface-registry-organization-details.md);
- [Camada comercial e fronteira](surface-registry-commercial-boundary-details.md).

## 6. Divisões controladas

- `GKR-SURF-COL-002` representa somente a visão geral validada do responsável;
- `GKR-SURF-COL-003` representa exclusivamente gestão de solicitações e não substitui `COL-004` participantes e vínculos;
- `GKR-SURF-PER-105` permanece a perspectiva da Pessoa sobre a solicitação;
- `GKR-SURF-COM-005` continua sem validação funcional específica;
- `GKR-SURF-BND-001` é endpoint documental, não tela Guivos.

## 7. Regras de uso

- o inventário e seus detalhamentos formam um único registro lógico;
- valores desconhecidos permanecem explícitos;
- materialização não equivale a validação funcional;
- validação de superfície não comprova continuidade integrada;
- responsabilidade sem interface continua `ausente`;
- o status `active` aprova o instrumento, não a completude das jornadas.

## 8. Efeito da UXA-088

A UXA-088 altera exclusivamente a maturidade observacional de `GKR-SURF-COL-003`: passa a `materializado; validação pendente`, com sete SVGs desktop. Nenhum outro ID muda de maturidade por analogia e nenhuma transição é promovida a validada.
