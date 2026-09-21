---
id: GKR-JOURNEY-SURFACE-REGISTRY-001
title: Registro Granular de Superfícies e Estados
status: active
version: 0.32.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
related:
  - UXA-087
  - UXA-089
  - UXA-090
  - UXA-092
  - UXA-094
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
  - GKR-UX-D5-C4B-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-UX-ORGCOL-AUTH-NAV-MAT-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001
  - GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
---

# Registro Granular de Superfícies e Estados


## 1. Finalidade

Este registro atribui identificadores estáveis a superfícies, estados, responsabilidades conhecidas e fronteiras documentais das Jornadas Integradas.

`GKR-UX-D5-C1-001` governa o contrato funcional corrente de `GKR-SURF-PER-010 — Meus Objetivos`, `GKR-SURF-PER-011 — Meus Próximos Passos` e `GKR-SURF-PER-012 — Minha Evolução`. A sequência histórica de materialização visual permanece no Git; `GKR-UX-D5-C4B-001` registra a validação integrada corrente de `TRN-008..013` no limite documental.

A reconciliação pós-PR #313/#314 corrige a leitura de Organização e Coletivo: `UXA-015..018` são históricos `superseded`; referências administrativas ou especializadas posteriores não podem ser promovidas por inferência a wireframe principal autenticado final.

Para Organização e Coletivo, `GKR-UX-ORGCOL-AUTH-IA-001` está definido em sua maturidade própria de Arquitetura da Informação, enquanto `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.1.0` define o mapa lógico-documental canônico de superfícies. Em atos governados posteriores, `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.1.0`, `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0` e `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0` consolidam estados, fluxos e navegação documental. A autorização, entrega e validação low-fidelity O/C posteriores (`GKR-UX-ORGCOL-AUTH-WIREFRAME-AUTH-001`, `...DELIVERY-001`, `...VALIDATION-001`) adicionam evidência visual funcional sem promover a maturidade individual dos `GKR-SURF-*`.

## 2. Convenções

- `ausente`: responsabilidade conhecida sem materialização necessária;
- `indeterminado`: evidência insuficiente;
- `não examinado`: integração ainda não avaliada;
- `parcial`: cobertura incompleta ou materialização válida apenas em recorte específico;
- `contratado`: responsabilidade/ligação governada sem validação funcional suficiente;
- `materializado`: referência existente sem implicar validação;
- `validado`: superfície examinada funcionalmente no escopo explicitado;
- `local`: validação limitada ao pacote de origem;
- `histórico/superseded`: artefato preservado por rastreabilidade sem autoridade vigente para o estado que pretendia definir.

## 2.1 Separação de contextos

A leitura corrente da experiência distingue explicitamente:

```text
PESSOA
COLETIVO
ORGANIZAÇÃO
BUSINESS
```

Pessoa, Coletivo e Organização são contextos de participante. **Guivos Business é produto especializado B2B**, com experiência própria, e não deve ser confundido com Organização.

Os identificadores `GKR-SURF-COM-*` permanecem estáveis por rastreabilidade histórica, mas o prefixo `COM` **não define um contexto "Comercial" concorrente com Business**. No corpus vigente, esses cinco IDs pertencem ao recorte de **Guivos Ads / Opportunity Boost**.

Os identificadores `GKR-SURF-BND-*` representam **fronteiras documentais**, não participantes nem produtos.

Consequentemente:

```text
COM-* ≠ GUIVOS BUSINESS
COM-* → ADS / OPPORTUNITY BOOST

BND-* ≠ GUIVOS BUSINESS
BND-* → FRONTEIRAS DOCUMENTAIS

GUIVOS BUSINESS
→ CONTEXTO DE PRODUTO PRÓPRIO
→ GOVERNADO POR GPA-004 + AUTORIDADES BUSINESS
```

## 3. Contagem

| Categoria | Quantidade |
|---|---:|
| Pessoa | 27 |
| Coletivo | 12 |
| Organização | 11 |
| Guivos Business | 0 IDs próprios neste Registry |
| Ads / Opportunity Boost (`COM-*`, prefixo legado) | 5 |
| fronteira documental | 2 |
| **Total de IDs registrados** | **57** |

A contagem de IDs permanece estrutural. Ela não implica que todos estejam materializados ou validados.

## 4. Inventário principal

| ID | Superfície, estado ou responsabilidade | Perspectiva e família | Canal | Maturidade | Autoridade | Materialização | Validação | Detalhamento obrigatório |
|---|---|---|---|---|---|---|---|---|
| GKR-SURF-PER-001 | Home pública | visitante; início protegido | público | validado | UXA-020; GKR-UX-HOME-MASTER-001 | Design-owned / sem baseline visual corrente | UXA-021 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-002 | entrada protegida | Pessoa | protegido | validado | UXA-020; UXA-023 | sem baseline visual corrente | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-003 | escolha de modalidade | Pessoa | protegido | validado | UXA-020; UXA-023 | sem baseline visual corrente | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-004 | expressão por texto ou voz | Pessoa | protegido | validado | UXA-069; GKR-JOURNEY-PERSON-001 | sem baseline visual corrente | UXA-069 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-005 | inventário e autorização | Pessoa | protegido | validado | UXA-023 | sem baseline visual corrente | UXA-035 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-006 | processamento visível | Pessoa | protegido | validado | UXA-023 | sem baseline visual corrente | UXA-037 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-007 | compreensão inicial revisável | Pessoa | protegido | **validado** | UXA-023; UXA-097 | sem baseline visual corrente; contrato funcional consolidado por UXA-097 | UXA-037; UXA-097 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-008 | Tela Hoje | Pessoa autenticada | protegido | **validado** | UXA-002; UXA-011-A1; UXA-097 | sem baseline visual corrente; primeira continuidade governada por UXA-097 | UXA-010; UXA-097 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-009 | Conta e configurações da Pessoa | Pessoa autenticada; administração pessoal | protegido | contratado | UXA-100; UXA-100-A1; UXA-100-A4 | — | — | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-010 | Meus Objetivos | Pessoa autenticada; direção e objetivos | protegido | **contrato funcional corrente / handoffs validados** | PAS-001-OBJ-VIEW-001; GKR-UX-D5-C1-001 | histórico visual preservado no Git | **TRN-008/009 validadas por GKR-UX-D5-C4B-001** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-011 | Meus Próximos Passos | Pessoa autenticada; movimentos contextuais | protegido | **contrato funcional corrente / handoffs validados** | PAS-001-PP-VIEW-001; GKR-UX-D5-C1-001 | histórico visual preservado no Git | **TRN-010/011 validadas por GKR-UX-D5-C4B-001** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-012 | Minha Evolução | Pessoa autenticada; trajetórias e evolução contínua | protegido | **contrato funcional corrente / handoffs validados** | PAS-001-EC-VIEW-001; GKR-UX-D5-C1-001 | histórico visual preservado no Git | **TRN-012/013 validadas por GKR-UX-D5-C4B-001** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-101 | Explorar Coletivos | visitante | móvel | validado | UXA-056 | sem baseline visual corrente | UXA-061 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-102 | Resultados de Busca de Coletivos | visitante | móvel | validado | UXA-056 | sem baseline visual corrente | UXA-061 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-103 | Perfil Público do Coletivo | visitante | móvel | validado | UXA-056 | sem baseline visual corrente | UXA-063 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-104 | revisão e solicitação | solicitante | móvel | validado | UXA-056 | sem baseline visual corrente | UXA-065 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-105 | Solicitação Pendente | solicitante | móvel | validado | UXA-056; UXA-092 | sem baseline visual corrente | UXA-067; UXA-092 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-106 | Meus Coletivos | participante | móvel | **validado** | UXA-056; UXA-059; UXA-092/094 | sem baseline visual corrente | UXA-092/094 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-107 | Central de Atualizações | participante | móvel | **validado** | UXA-058; UXA-059; UXA-094/096 | sem baseline visual corrente | UXA-094/096 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-108 | Início do Participante | participante | móvel | **validado no recorte da Pessoa participante** | UXA-056; UXA-058; UXA-059; UXA-096 | sem baseline visual corrente | UXA-096 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-201 | Mapa de Oportunidades | Pessoa/visitante | móvel e computador | validado | UXA-004; UXA-098 | sem baseline visual corrente | UXA-025; integração UXA-098 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-202 | Lista de Oportunidades | Pessoa/visitante | móvel e computador | validado | UXA-004 | UXA-028 | UXA-029; integração UXA-098 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-203 | Detalhe de Oportunidade + revisão consciente de saída | Pessoa/visitante | móvel e computador | **validado** | UXA-004; UXA-098; UXA-101 | sem baseline visual corrente; revisão consciente governada por UXA-101 | UXA-012; entradas UXA-098; **saída UXA-101** | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-301 | Planos e comparação da Pessoa | Pessoa autenticada | móvel/protegido | **validado** | GEM-004-A1/A2; GEM-004-PLAN-TAXONOMY-AUTHORITY-001; UXA-100-A3 | UXA-100/A1 | UXA-100-A2/A3 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-302 | revisão de contratação da Pessoa | Pessoa/pagador autorizado | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-303 | gestão de downgrade e cancelamento da Pessoa | Pessoa titular | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-PER-304 | resultado e recuperação de plano/cobrança da Pessoa | Pessoa titular | móvel/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Pessoa](surface-registry-person-details.md) |
| GKR-SURF-COL-001 | presença pública e entrada coletiva | visitante/responsável | público e protegido | parcial | GKR-UX-HOME-OC-MASTER-001; GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001; GKR-UX-ORGCOL-AUTH-STATE-MAP-001 | `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` quando a entrada cruza para experiência autenticada; expressão pública final pertence a Design | `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0 = PASS` no recorte autenticado | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-002 | Visão Geral do Responsável | responsável | computador protegido | parcial / materialização local | UXA-014; UXA-059; UXA-100-A4 | `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` como materialização principal low-fidelity; UXA-087 permanece validação administrativa local | `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0 = PASS`; UXA-087 permanece validação local anterior | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-003 | gestão de solicitações | responsável | computador protegido | validado | UXA-056; UXA-059; UXA-089/090/092 | sem baseline visual corrente; fluxo especializado preservado funcionalmente | UXA-089/090/092 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-004 | participantes e vínculos | responsável | protegido | programado | UXA-059 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-005 | comunicação oficial | responsável | protegido | programado | UXA-058; UXA-059 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-006 | atividades, consultas e decisões | responsável | protegido | programado | UXA-059 | parcial/dispersa | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-007 | proteção e moderação | responsável | protegido | contratado | UXA-058 | parcial | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-008 | relações institucionais | responsável | protegido | contratado | UXA-019 | — | — | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-301 | Planos e comparação do Coletivo — Livre · Mobiliza · Impacta · Rede | responsável autorizado | computador/protegido | **validado no fluxo especializado** | GEM-004-A1/A2; GEM-004-PLAN-TAXONOMY-AUTHORITY-001; UXA-100-A3; UXA-100-A4 | UXA-100/A1; retorno contratado por UXA-100-A4 | UXA-100-A2/A3; navegação no escopo próprio A4 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-302 | revisão de contratação do Coletivo | responsável financeiro autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-303 | gestão de downgrade e cancelamento do Coletivo | responsável autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-COL-304 | resultado e recuperação de plano/cobrança do Coletivo | responsável autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Coletivo](surface-registry-collective-details.md) |
| GKR-SURF-ORG-001 | Visão Geral da Organização | representante | protegido | low-fidelity validado / high-fidelity separado | GKR-UX-ORGCOL-AUTH-IA-001; GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001; GKR-UX-ORGCOL-AUTH-STATE-MAP-001; GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 | `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0`; materialização visual final pertence a Design | `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0 = PASS` | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-002 | cadastro de oportunidade | representante | protegido | validado | UXA-004; UXA-013 | sem baseline visual corrente | UXA-013 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-003 | oportunidade aprovada/ativa | representante | protegido | validado | UXA-004; UXA-013; UXA-098 | sem baseline visual corrente | UXA-013; integração UXA-098 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-004 | proposta de relação com Coletivo | representante | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-005 | avaliação e negociação bilateral | representantes | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-006 | relação ativa e revisão | representantes | protegido | contratado | UXA-019 | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-007 | resultados e evidências institucionais | representante | protegido | indeterminado | referências dispersas | — | — | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-301 | Planos e comparação da Organização — Conecta · Eleva · Transforma | representante autorizado | computador/protegido | **validado no fluxo especializado** | GEM-004-A1/A2; GEM-004-PLAN-TAXONOMY-AUTHORITY-001; UXA-100-A3; UXA-100-A4 | UXA-100/A1; retorno contratado por UXA-100-A4 | UXA-100-A2/A3; navegação no escopo próprio A4 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-302 | revisão de contratação da Organização | autoridade financeira identificada | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-303 | gestão de downgrade e cancelamento da Organização | representante autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-ORG-304 | resultado e recuperação de plano/cobrança da Organização | representante autorizado | computador/protegido | **validado** | GEM-004-A2; UXA-100-A3 | UXA-100 | UXA-100-A2/A3 | [Organização](surface-registry-organization-details.md) |
| GKR-SURF-COM-001 | configuração do anunciante | anunciante | protegido | **validado localmente** | GPA-007; UXA-038; UXA-041 | sem baseline visual corrente | UXA-041 | [Ads / Opportunity Boost e Fronteiras](surface-registry-ads-boundaries-details.md) |
| GKR-SURF-COM-002 | cartão patrocinado e explicação | Pessoa exposta | público/protegido | validado | GPA-007; UXA-038; UXA-043 | sem baseline visual corrente | UXA-043 | [Ads / Opportunity Boost e Fronteiras](surface-registry-ads-boundaries-details.md) |
| GKR-SURF-COM-003 | presença patrocinada em lista/mapa | Pessoa exposta | público/protegido | validado | GPA-007; UXA-038; UXA-045 | sem baseline visual corrente | UXA-045 | [Ads / Opportunity Boost e Fronteiras](surface-registry-ads-boundaries-details.md) |
| GKR-SURF-COM-004 | gestão ativa/relatório | anunciante | protegido | validado | GPA-007; UXA-038; UXA-047/049/054 | sem baseline visual corrente | UXA-047/049/054 | [Ads / Opportunity Boost e Fronteiras](surface-registry-ads-boundaries-details.md) |
| GKR-SURF-COM-005 | estados residuais Opportunity Boost | anunciante/Pessoa | misto | **validado** | GPA-007; UXA-038; UXA-099 | sem baseline visual corrente | UXA-099 | [Ads / Opportunity Boost e Fronteiras](surface-registry-ads-boundaries-details.md) |
| GKR-SURF-BND-001 | fronteira de destino externo de oportunidade | Pessoa → terceiro | externo | **examinado** | UXA-004/007/101 | sem tela por definição | **UXA-101; TRN-205 validada até a fronteira** | [Ads / Opportunity Boost e Fronteiras](surface-registry-ads-boundaries-details.md) |
| GKR-SURF-BND-002 | fronteira de contratação/dimensionamento assistido | Coletivo/Organização → processo assistido quando necessário | externo ao autoatendimento | parcial | GEM-004-PLAN-TAXONOMY-AUTHORITY-001; UXA-100-A3 | sem tela por definição | parcial; TRN-416/TRN-426 preservadas | [Ads / Opportunity Boost e Fronteiras](surface-registry-ads-boundaries-details.md) |

## 5. Autoridade de planos, jornada pessoal e origem voluntária

A leitura vigente de Planos é:

```text
Pessoa: Free · Plus · Pro
Coletivo: Livre · Mobiliza · Impacta · Rede
Organização: Conecta · Eleva · Transforma
Guivos Business: Start · Growth · Scale · Enterprise
```

`PER-009`, `COL-002` e `ORG-001` continuam identificadores semânticos possíveis de origem/retorno para contratos de Planos. Esses contratos, por si sós, não provam materialização visual. Para `COL-002` e `ORG-001`, a materialização low-fidelity corrente é governada separadamente por `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` + `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`. Isso não substitui IA, Surface Map, State Map, Priority Flows ou Navigation Materialization e não promove maturidade funcional individual.

`PER-010`, `PER-011` e `PER-012` são responsabilidades correntes ligadas a Hoje; sua maturidade deve ser lida diretamente nas autoridades e transições vigentes.

Guivos Business é produto especializado e constitui um contexto corrente de experiência próprio. Sua continuidade é sintetizada em `docs/journeys/business.md` e governada por `GPA-004`, pelo Portfólio Funcional Business, pelas autoridades da Home Business e por `docs/plans/business.md`. A criação dessa vista não cria novos `GKR-SURF-*` neste registro.

`BND-002` não é plano, produto, checkout ou fronteira exclusiva de Enterprise/Scale. Ele identifica a necessidade de contratação/dimensionamento assistido.

## 6. Preservações e correções

- total de IDs permanece **57**;
- `PER-010`, `PER-011` e `PER-012` preservam sua maturidade corrente;
- `PER-009` permanece contratado e sem SVG dedicado;
- a antiga conclusão agregada `121 validados / 0 pendentes` **não é mais vigente**;
- uma nova contagem de wireframes vigentes/validados **não é inferida** sem recomputação governada;
- `PER-203` permanece validada no recorte de saída externa;
- `BND-001` permanece examinado, sem tela própria;
- `BND-002` permanece parcial, sem tela própria;
- `TRN-416` e `TRN-426` permanecem parciais;
- wireframe principal autenticado da Organização → **LOW-FIDELITY DELIVERY v0.1.0 + VALIDATION v1.0.0 / PASS**;
- wireframe principal autenticado do Coletivo → **LOW-FIDELITY DELIVERY v0.1.0 + VALIDATION v1.0.0 / PASS**;
- fluxos especializados preservam sua maturidade quando sustentados por autoridade independente;
- nenhuma jornada ou Engenharia de Produto é promovida.

## 7. Estado

O registro permanece `active` como inventário granular. A maturidade deve ser lida por superfície e por escopo de autoridade, nunca pela mera existência física de SVG. Para Organização e Coletivo, Jobs e Arquitetura da Informação permanecem definidos em seus limites próprios; `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.1.0` define o mapa lógico-documental canônico de superfícies e `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.1.0` define o mapa funcional de estados canônico e `GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001 v1.0.0` define os Priority Flows canônicos documentais. A Navigation Materialization está definida canonicamente em `GKR-UX-ORGCOL-AUTH-NAV-MAT-001 v1.0.0`; os wireframes principais autenticados low-fidelity foram entregues em `GKR-UX-ORGCOL-AUTH-WIREFRAME-DELIVERY-001 v0.1.0` e validados com `PASS` em `GKR-UX-ORGCOL-AUTH-WIREFRAME-VALIDATION-001 v1.0.0`. A autorização de Design high-fidelity O/C está `GRANTED`, mas a execução permanece `NOT_STARTED` e depende de ato separado; protótipo e implementação não são promovidos por esse estado.