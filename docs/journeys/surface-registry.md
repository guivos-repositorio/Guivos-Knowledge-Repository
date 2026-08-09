---
id: GKR-JOURNEY-SURFACE-REGISTRY-001
title: Registro Granular de Superfícies e Estados
status: active
version: 0.20.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-09
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
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-C1-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
normative: false
---

# Registro Granular de Superfícies e Estados

## 1. Finalidade

Este registro atribui identificadores estáveis a superfícies, estados, responsabilidades conhecidas e fronteiras documentais das Jornadas Integradas.

A versão 0.20.0 adiciona `GKR-SURF-PER-010 — Meus Objetivos`, `GKR-SURF-PER-011 — Meus Próximos Passos` e `GKR-SURF-PER-012 — Minha Evolução` como responsabilidades contratadas pela D5-C1. Nenhuma delas possui SVG ou validação visual nesta etapa. A contagem passa a 57 IDs.

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
| Pessoa | 27 |
| Coletivo | 12 |
| Organização | 11 |
| camada comercial | 5 |
| fronteira documental | 2 |
| **Total** | **57** |

## 4. Inventário principal

| ID | Superfície, estado ou responsabilidade | Perspectiva e família | Canal | Maturidade | Autoridade | Materialização | Validação | Detalhamento obrigatório |
|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-001 | Home pública | visitante; início protegido | público | validado | UXA-020 | UXA-022 | UXA-021 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-002 | entrada protegida | Pessoa | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-003 | escolha de modalidade | Pessoa | protegido | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-004 | expressão por texto ou voz | Pessoa | protegido | validado | UXA-068 | UXA-068 | UXA-069 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-005 | inventário e autorização | Pessoa | protegido | validado | UXA-023 | UXA-034 | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-006 | processamento visível | Pessoa | protegido | validado | UXA-023 | UXA-036 | UXA-037 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-007 | compreensão inicial revisável | Pessoa | protegido | **validado** | UXA-023 | UXA-036; UXA-097 | UXA-037; UXA-097 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-008 | Tela Hoje | Pessoa autenticada | protegido | **validado** | UXA-002; UXA-011-A1 | UXA-006; UXA-097 | UXA-010; UXA-097 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-009 | Conta e configurações da Pessoa | Pessoa autenticada; administração pessoal | protegido | contratado | UXA-100; UXA-100-A1; UXA-100-A4 | — | — | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-010 | Meus Objetivos | Pessoa autenticada; direção e objetivos | protegido | contratado | PAS-001-OBJ-VIEW-001; GKR-UX-D5-C1-001 | — | — | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-011 | Meus Próximos Passos | Pessoa autenticada; movimentos contextuais | protegido | contratado | PAS-001-PP-VIEW-001; GKR-UX-D5-C1-001 | — | — | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-012 | Minha Evolução | Pessoa autenticada; trajetórias e evolução contínua | protegido | contratado | PAS-001-EC-VIEW-001; GKR-UX-D5-C1-001 | — | — | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-101 | Explorar Coletivos | visitante | móvel | validado | UXA-056 | UXA-060 | UXA-061 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-102 | Resultados de Busca de Coletivos | visitante | móvel | validado | UXA-056 | UXA-060 | UXA-061 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-103 | Perfil Público do Coletivo | visitante | móvel | validado | UXA-056 | UXA-062 | UXA-063 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-104 | revisão e solicitação | solicitante | móvel | validado | UXA-056 | UXA-064 | UXA-065 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-105 | Solicitação Pendente | solicitante | móvel | validado | UXA-056 | UXA-066; UXA-091/092 | UXA-067; UXA-092 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-106 | Meus Coletivos | participante | móvel | **validado** | UXA-056; UXA-059 | UXA-091/092/094 | UXA-092/094 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-107 | Central de Atualizações | participante | móvel | **validado** | UXA-058; UXA-059 | UXA-093/094/095/096 | UXA-094/096 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-108 | Início do Participante | participante | móvel | **validado** | UXA-016; UXA-018; UXA-056; UXA-058; UXA-059 | UXA-095/096 | UXA-096 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-201 | Mapa de Oportunidades | Pessoa/visitante | móvel e computador | validado | UXA-004 | UXA-024 | UXA-025; integração UXA-098 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-202 | Lista de Oportunidades | Pessoa/visitante | móvel e computador | validado | UXA-004 | UXA-028 | UXA-029; integração UXA-098 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-203 | Detalhe de Oportunidade + revisão consciente de saída | Pessoa/visitante | móvel e computador | **validado** | UXA-004; UXA-007 | UXA-007; reformulação UXA-101 | UXA-012; entradas UXA-098; **saída UXA-101** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-301 | Planos e comparação da Pessoa | Pessoa autenticada | móvel/protegido | **validado** | GEM-004-A1/A2; GEM-004-PLAN-TAXONOMY-AUTHORITY-001; UXA-100-A3 | UXA-100/A1 | UXA-100-A2/A3 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-302 | revisão de contratação da Pessoa | Pessoa/pagador autorizado | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-303 | gestão de downgrade e cancelamento da Pessoa | Pessoa titular | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-304 | resultado e recuperação de plano/cobrança da Pessoa | Pessoa titular | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-COL-001 | presença pública existente | visitante/responsável | público e protegido | materializado | UXA-014; UXA-056 | UXA-016 | UXA-018; UXA-063 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-002 | Visão Geral do Responsável | responsável | computador protegido | validado | UXA-014; UXA-059; UXA-100-A4 | UXA-086/087; reformulação UXA-100-A4 | UXA-087; navegação UXA-100-A4 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-003 | gestão de solicitações | responsável | computador protegido | validado | UXA-056; UXA-059 | UXA-088/089 | UXA-089/090/092 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-004 | participantes e vínculos | responsável | protegido | programado | UXA-059 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-005 | comunicação oficial | responsável | protegido | programado | UXA-058; UXA-059 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-006 | atividades, consultas e decisões | responsável | protegido | programado | UXA-059 | parcial/dispersa | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-007 | proteção e moderação | responsável | protegido | contratado | UXA-058 | parcial | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-008 | relações institucionais | responsável | protegido | contratado | UXA-019 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-301 | Planos e comparação do Coletivo — Livre · Mobiliza · Impacta · Rede | responsável autorizado | computador/protegido | **validado** | GEM-004-A1/A2; GEM-004-PLAN-TAXONOMY-AUTHORITY-001; UXA-100-A3; UXA-100-A4 | UXA-100/A1; retorno reformulado UXA-100-A4 | UXA-100-A2/A3; navegação UXA-100-A4 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-302 | revisão de contratação do Coletivo | responsável financeiro autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-303 | gestão de downgrade e cancelamento do Coletivo | responsável autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-304 | resultado e recuperação de plano/cobrança do Coletivo | responsável autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-ORG-001 | Visão Geral da Organização | representante | protegido | validado | UXA-014; UXA-100-A4 | UXA-015; reformulação UXA-100-A4 | UXA-017; navegação UXA-100-A4 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-002 | cadastro de oportunidade | representante | protegido | validado | UXA-004 | UXA-008 | UXA-013 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-003 | oportunidade aprovada/ativa | representante | protegido | validado | UXA-004 | UXA-008 | UXA-013; integração UXA-098 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-004 | proposta de relação com Coletivo | representante | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-005 | avaliação e negociação bilateral | representantes | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-006 | relação ativa e revisão | representantes | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-007 | resultados e evidências institucionais | representante | protegido | indeterminado | referências dispersas | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-301 | Planos e comparação da Organização — Conecta · Eleva · Transforma | representante autorizado | computador/protegido | **validado** | GEM-004-A1/A2; GEM-004-PLAN-TAXONOMY-AUTHORITY-001; UXA-100-A3; UXA-100-A4 | UXA-100/A1; retorno reformulado UXA-100-A4 | UXA-100-A2/A3; navegação UXA-100-A4 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-302 | revisão de contratação da Organização | autoridade financeira identificada | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-303 | gestão de downgrade e cancelamento da Organização | representante autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-304 | resultado e recuperação de plano/cobrança da Organização | representante autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-COM-001 | configuração do anunciante | anunciante | protegido | materializado | UXA-038 | UXA-040 | UXA-041 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-002 | cartão patrocinado e explicação | Pessoa exposta | público/protegido | validado | UXA-038 | UXA-042 | UXA-043 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-003 | presença patrocinada em lista/mapa | Pessoa exposta | público/protegido | validado | UXA-038 | UXA-044 | UXA-045 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-004 | gestão ativa/relatório | anunciante | protegido | validado | UXA-038 | UXA-046/048/053 | UXA-047/049/054 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-COM-005 | estados residuais Opportunity Boost | anunciante/Pessoa | misto | **validado** | UXA-055 | UXA-055 | UXA-099 | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-BND-001 | fronteira de destino externo de oportunidade | Pessoa → terceiro | externo | **examinado** | UXA-004/007/101 | sem tela por definição | **UXA-101; TRN-205 validada até a fronteira** | [Comercial](surface-registry-commercial-boundary-details.md) |
| GKR-SURF-BND-002 | fronteira de contratação/dimensionamento assistido | Coletivo/Organização → processo assistido quando necessário | externo ao autoatendimento | parcial | GEM-004-PLAN-TAXONOMY-AUTHORITY-001; UXA-100-A3 | sem tela por definição | parcial; TRN-416/TRN-426 preservadas | [Comercial](surface-registry-commercial-boundary-details.md) |

## 5. Autoridade de planos, jornada pessoal e origem voluntária

A leitura vigente de Planos é:

```text
Pessoa: Free · Plus · Pro
Coletivo: Livre · Mobiliza · Impacta · Rede
Organização: Conecta · Eleva · Transforma
Guivos Business: Start · Growth · Scale · Enterprise
```

A origem voluntária de Planos permanece representada por `PER-009`, `COL-002` e `ORG-001`. A criação de `PER-009` não materializa uma arquitetura completa de Conta nem autoriza preencher outras responsabilidades administrativas por inferência.

A D5-C1 adiciona `PER-010`, `PER-011` e `PER-012` como responsabilidades pessoais especializadas ligadas a Hoje por transições contratadas. Elas não são estados internos de `PER-008` e não possuem SVG nesta etapa.

Guivos Business é produto especializado e não recebe novos IDs neste registro.

`BND-002` não é plano, produto, checkout ou fronteira exclusiva de Enterprise/Scale. Ele identifica a necessidade de contratação/dimensionamento assistido.

## 6. Preservações

- total de IDs passa a **57**;
- `PER-009`, `PER-010`, `PER-011` e `PER-012` permanecem sem SVG dedicado e com maturidade `contratado`;
- os 118 SVGs canônicos permanecem inalterados em quantidade;
- 42 IDs permanecem com referência visual, agora de 57;
- responsabilidades sem SVG dedicado passam a 13;
- `PER-203` permanece validada no recorte de saída externa;
- `BND-001` permanece examinado, sem tela própria;
- `BND-002` permanece parcial, sem tela própria;
- `TRN-416` e `TRN-426` permanecem parciais;
- nenhuma jornada ou Engenharia de Produto é promovida.

## 7. Estado

O registro permanece `active` como inventário granular. O status não promove as jornadas completas nem representa implementação.