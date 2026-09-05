---
id: GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
title: Matriz de Rastreabilidade Visual por SVG
status: superseded
version: 0.27.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-05
parent: GKR-JOURNEY-SCREEN-GALLERY-001
depends_on:
  - UXA-083
  - UXA-084
  - UXA-085
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
  - UXA-100-A2
  - UXA-100-A3
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-UX-D5-C4A-001
  - GKR-UX-D5-C4B-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
maturity: historical_provenance_only
---

# Matriz de Rastreabilidade Visual por SVG

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


## 1. Finalidade

Esta matriz preserva os **34 perfis de rastreabilidade** e a proveniência dos ciclos visuais anteriores, mas não representa mais uma camada física vigente.

O cleanup `F-016-A` removeu os **119/119 SVGs** que ainda existiam em `docs/assets/wireframes/`. A cobertura funcional foi provada antes da remoção: cada asset possuía perfil rastreável e referência textual em Experience Architecture, e cada perfil físico possuía receiver textual corrente fora da família de galeria.

```text
SVGs FÍSICOS VIGENTES
→ 0

ASSOCIAÇÕES FÍSICAS VIGENTES
→ 0

PERFIS DE RASTREABILIDADE PRESERVADOS
→ 34
→ PROVENIÊNCIA / RASTREABILIDADE SEMÂNTICA
→ NÃO AUTORIDADE VISUAL
```

R09 e R11 já eram perfis sem SVG após `F-006`; os demais perfis deixam de ter associação física após `F-016-A`.

## 2. Estado do instrumento

A D5-C2 elevou o inventário físico para **121 associações** e **34 perfis** ao materializar um estado-base para `PER-010`, `PER-011` e `PER-012`. A D5-C3 reformou esses três ativos in-place e validou funcionalmente os perfis `R32`, `R33` e `R34`. A D5-C4A reformulou e revalidou localmente o SVG recorrente de `PER-008` no perfil `R05`. A D5-C4B promove a maturidade integrada de `TRN-008..013` sem alterar associação SVG→perfil. `PER-009` continua sem perfil visual próprio.

A reconciliação preserva a leitura de `BND-002` como fronteira genérica de contratação/dimensionamento assistido, a separação `Organização ≠ Guivos Business` e a distinção entre Domínio de Evolução, dimensão estrutural do Contexto Vivo e aspecto descritivo da mudança.

Para Organização e Coletivo, os perfis históricos continuam úteis para localizar artefatos e contratos, mas não podem ser usados para declarar os wireframes principais autenticados como definidos ou validados.

## 3. Perfis de rastreabilidade

| Perfil | Superfície(s) | Entrada | Saída | Retorno ou interrupção | Lacuna | Validação / estado vigente |
|---|---|---|---|---|---|---|
| R01 | PER-001 | entrada pública | TRN-001 | permanecer/retornar | continuidade pública → protegida | UXA-021 |
| R02 | PER-002/003/005 | TRN-001 | TRN-002 a 005 | voltar/trocar/editar/recusar | integração inicial | UXA-035 |
| R03 | PER-004 | TRN-003 | TRN-004 | trocar/editar/descartar | expressão → inventário | UXA-069 |
| R04 | PER-006/007 | TRN-005/006 | TRN-007 | revisar/recusar/retornar | handoffs pessoais anteriores | UXA-037; decisão corrente e TRN-007 UXA-097 |
| R05 | PER-008 | TRN-007 ou acesso recorrente | continuidade recorrente; **TRN-008/010/012 integrais quando affordance aplicável estiver presente** | revisar/navegar/retornar; **TRN-009/011/013 integrais** | estados alternativos de Hoje | UXA-010 recorrente; primeira entrada e TRN-007 UXA-097; estado recorrente D5-C4A; **TRN-008..013 D5-C4B** |
| R06 | PER-201 | TRN-203/304 | TRN-204/210 | voltar/alternar | integração patrocinada parcial | UXA-025/027/031/033; TRN-203/204/210 UXA-098 |
| R07 | PER-202 | TRN-210/306 | TRN-211 | retornar ao mapa | integração patrocinada parcial | UXA-029; TRN-210/211 UXA-098 |
| R08 | PER-203 | TRN-204/211 | TRN-205 → BND-001 | voltar ao detalhe; bloquear saída inválida; retorno externo sem presumir resultado | processo externo posterior à fronteira | UXA-012; entradas UXA-098; reformulação, revisão consciente e TRN-205 UXA-101 |
| R09 | ORG-001 | entrada institucional semântica | TRN-201 ou contrato especializado TRN-427 | cancelar/retornar; TRN-428 no contrato de Planos | materialização visual fora da autoridade documental | `UXA-015/017` removidos do corpus corrente; perfil preservado somente como proveniência histórica sem SVG; TRN-427/428 mantêm maturidade contratual própria |
| R10 | ORG-002/003 | TRN-201 | TRN-202/203 | editar/retirar/pausar | ligações institucionais restantes | UXA-013; TRN-203 UXA-098 |
| R11 | COL-001 | busca ou presença pública; entrada autenticada funcional conforme autoridades vigentes | TRN-103 no recorte público aplicável | retornar/sair | **presença pública ≠ UX principal autenticada** | `UXA-016/018` removidos do corpus corrente; perfil preservado somente como proveniência histórica sem SVG; UXA-063 preserva validação do perfil público no recorte próprio |
| R12 | PER-101/102 | exploração | TRN-101/102 | limpar/voltar/refazer | descoberta → perfil | UXA-061 |
| R13 | PER-103/COL-001 | TRN-102 | TRN-103 | retornar | solicitação | UXA-063 |
| R14 | PER-104 | TRN-103 | TRN-104 | cancelar/retornar | handoff | UXA-065 |
| R15 | PER-105 | TRN-104/106/109 | TRN-105/107/108 | cancelar/responder/aguardar | outras continuidades separadas | UXA-067; aprovado UXA-092 |
| R16 | COM-001 | anunciante | TRN-301 | editar/cancelar | regras econômicas | UXA-041 |
| R17 | COM-001 | TRN-301 | TRN-301 | editar/cancelar | continuidade comercial | UXA-052 |
| R18 | COM-002 | TRN-302/303 | TRN-304/306 | ignorar/retornar | orgânico ↔ patrocinado | UXA-043 |
| R19 | COM-003 | entrega elegível | TRN-303 | retornar | continuidade patrocinada | UXA-045 |
| R20 | COM-004 | TRN-301 | TRN-302/305 | pausar/revisar/encerrar | estados residuais | UXA-047 |
| R21 | COM-004 | campanha | retorno à gestão | reconciliar/revisar | atribuição | UXA-049 |
| R22 | COM-004 | TRN-301 | TRN-302/305 | pausar/revisar/encerrar | integração com resíduos | UXA-054 |
| R23 | COM-005 | TRN-305 | conforme estado | retornar/revisar/desfazer/tentar novamente | TRN-305 ponta a ponta permanece parcial | UXA-099 |
| R24 | COL-002 | representação válida | TRN-112 ou contrato especializado TRN-417 | permanecer/retornar; TRN-418 no contrato de Planos | **Jobs + IA autenticada definidos em `pre-surface-map`; mapa final de superfícies + wireframe principal autenticado pendentes** | UXA-087 preserva evidência administrativa local; TRN-112 UXA-090; TRN-417/418 preservam maturidade contratual própria; **não é baseline final da UX principal** |
| R25 | COL-003 | TRN-105/107/112 | TRN-106/108/109 | voltar/aguardar/interromper | handoffs fechados nos gates | UXA-089/090/092 |
| R26 | PER-106 | TRN-108 ou acesso recorrente | TRN-110 | trocar categoria/voltar | P0B separado | UXA-092; gatilho revalidado UXA-094 |
| R27 | PER-107 | TRN-110 ou atualização autorizada | PER-105/PER-106; TRN-111 | retornar/ajustar preferência | P0B separado | UXA-094; versão corrente UXA-096; TRN-111 UXA-096 |
| R28 | PER-108 | TRN-111 | áreas internas próprias do Coletivo | voltar à Central; pausar/sair conforme fluxo próprio | estados P0B/P1 e áreas internas | UXA-096; TRN-111 UXA-096 |
| R29 | PER-301/302/303/304 | PER-009 via TRN-406 ou limite contextual legítimo | TRN-401 a 405; TRN-407 para Conta | manter plano, voltar, tentar novamente, preservar Free | **PER-009 sem materialização**; gateway/proration | UXA-100-A2/A3; origem/retorno contratados UXA-100-A4 |
| R30 | COL-301/302/303/304 | COL-002 como responsabilidade semântica via TRN-417 ou limite legítimo | TRN-411 a 416; TRN-418 para contexto administrativo | manter plano, aguardar, ajustar excedentes, retornar | contratação/dimensionamento após BND-002; cobrança real; origem principal final pendente | UXA-100-A2/A3; TRN-417/418 preservam maturidade do **contrato especializado**, não do wireframe principal |
| R31 | ORG-301/302/303/304 | ORG-001 como responsabilidade semântica via TRN-427 ou capacidade legítima | TRN-421 a 426; TRN-428 para contexto institucional | manter plano, ajustar capacidade, retornar | contratação/dimensionamento após BND-002; cobrança real; origem principal final pendente | UXA-100-A2/A3; TRN-427/428 preservam maturidade do **contrato especializado**, não do wireframe principal |
| R32 | PER-010 | **TRN-008 integral** | **TRN-009 integral** | revisar objetivo; voltar para Hoje; interromper sem alteração | estados alternativos e handoffs diretos com PER-011/012 permanecem separados | **GKR-UX-D5-C3-001 — superfície; GKR-UX-D5-C4B-001 — TRN-008/009 integrais** |
| R33 | PER-011 | **TRN-010 integral** | **TRN-011 integral** | revisar, adiar, não seguir; voltar para Hoje | estados adicionais e handoffs diretos com PER-010/012 permanecem separados | **GKR-UX-D5-C3-001 — superfície; GKR-UX-D5-C4B-001 — TRN-010/011 integrais** |
| R34 | PER-012 | **TRN-012 integral** | **TRN-013 integral** | revisar leitura, pausar acompanhamento, ajustar privacidade; voltar para Hoje | estados sensíveis adicionais e handoffs diretos com PER-010/011 permanecem separados | **GKR-UX-D5-C3-001 — superfície; GKR-UX-D5-C4B-001 — TRN-012/013 integrais** |

R32–R34 preservam as mesmas associações criadas pela D5-C2 e a validação funcional local da D5-C3. A D5-C4B altera somente a maturidade integrada de `TRN-008..013`; não cria, remove ou remapeia perfil visual.

## 4. Associação histórica dos 119 SVGs físicos removidos por F-016-A

A associação física foi encerrada por `F-016-A`.

```text
ANTES DO CLEANUP F-016-A
→ 119 SVGs físicos
→ 119 associações físicas

APÓS O CLEANUP F-016-A
→ 0 SVGs físicos
→ 0 associações físicas
```

Os nomes dos assets e suas associações anteriores permanecem recuperáveis no histórico Git. O corpus vigente preserva somente os perfis e contratos textuais necessários.

## 5. Totais e limites

- SVGs físicos registrados: **121**;
- associações individuais físicas: **121**;
- perfis documentais: **34**;
- antiga claim `121 com validação funcional vigente / 0 pendentes`: **superseded como resumo de maturidade atual**;
- nova contagem agregada de wireframes vigentes/validados: **não inferida; recomputação governada pendente**;
- R09 preserva rastreabilidade histórica de `ORG-001`, sem validação vigente do wireframe principal;
- R11 preserva rastreabilidade histórica do antigo início do Coletivo, sem validação vigente do wireframe principal;
- R24 preserva evidência administrativa local de `COL-002`, não baseline final da UX principal;
- R05 registra a revalidação local do estado recorrente de Hoje pela D5-C4A e a continuidade integrada D5-C4B;
- R32, R33 e R34 preservam validação funcional local pela D5-C3 e referenciam os handoffs da D5-C4B;
- `PER-009` continua sem perfil porque não possui SVG dedicado;
- `BND-001` e `BND-002` permanecem sem SVG por definição de fronteira;
- validação visual não atribui à Guivos comportamento posterior às fronteiras.

## 6. Estado após a reconciliação pós-313/314

A reconciliação preserva as **121 associações físicas e os 34 perfis documentais**. Nenhum vínculo SVG→perfil precisa ser removido para que a autoridade do artefato seja supersedida.

`TRN-008..013` preservam sua maturidade documental própria. `TRN-406/407` permanecem contratadas até materialização de `PER-009`. As transições internas de contratação/ciclo preservam a maturidade anterior, e `TRN-416/426` continuam parciais após `BND-002`.

O wireframe principal autenticado da Organização permanece **pendente**. O wireframe principal autenticado do Coletivo permanece **pendente**. Fluxos especializados independentes preservam a maturidade sustentada por suas autoridades específicas.

Pessoa, Coletivo e Organização continuam `draft`; V5/UXA-102, D6, D7 e Engenharia de Produto permanecem não iniciados.