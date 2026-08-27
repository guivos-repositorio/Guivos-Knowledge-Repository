---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.32.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-26
related:
  - UXA-005
  - UXA-070
  - UXA-080
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
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
---

# Catálogo Integrado de Telas

## 1. Regra de leitura

```text
SVG existente
≠ superfície granular adicional por padrão
≠ wireframe vigente automaticamente
≠ transição integralmente validada automaticamente
≠ jornada integrada validada
≠ implementação técnica
```

Após a reconciliação pós-PR #313/#314, aplica-se também:

```text
CONTAGEM FÍSICA DE SVGs
≠ CONTAGEM DE WIREFRAMES VIGENTES
≠ CONTAGEM DE WIREFRAMES VALIDADOS
```

`UXA-015..018` e seus SVGs associados permanecem fisicamente no repositório para rastreabilidade, mas são históricos `superseded` e não podem sustentar maturidade atual da experiência autenticada principal de Organização ou Coletivo.

A D5-C1 contratou `PER-010 — Meus Objetivos`, `PER-011 — Meus Próximos Passos` e `PER-012 — Minha Evolução`. A D5-C2 criou um SVG low-fidelity para cada uma dessas responsabilidades sem criar novo ID granular e sem promover `TRN-008..013`. A D5-C3 reforma in-place e valida funcionalmente os três estados-base, mantendo as transições contratadas.

## 2. Inventário agregado por família

A coluna `SVGs` abaixo é **inventário físico**. Ela não é, por si só, indicador de maturidade vigente.

| Participante ou camada | Família | SVGs físicos | Estado de validação que pode ser afirmado | Continuidade integrada | Lacuna associada |
|---|---|---:|---|---|---|
| Pessoa | Home pública | 1 | validado | entrada protegida parcial | continuidade entre pacotes |
| Pessoa | início protegido | 4 | 4 validados | parcial | reconciliação ponta a ponta |
| Pessoa | expressão guiada | 8 | 8 validados | parcial | integração com inventário |
| Pessoa | compreensão inicial | 5 | 5 validados | **TRN-007 integralmente validada** | handoffs anteriores ainda parciais |
| Pessoa | Tela Hoje | 2 | 2 validados | primeira entrada validada; `TRN-008/010/012` contratadas | estados alternativos e handoffs especializados ainda não validados ponta a ponta |
| Pessoa | Meus Objetivos | **1** | **validado localmente pela D5-C3** | `TRN-008/009` contratadas | validação integrada do handoff |
| Pessoa | Meus Próximos Passos | **1** | **validado localmente pela D5-C3** | `TRN-010/011` contratadas | validação integrada do handoff |
| Pessoa | Minha Evolução | **1** | **validado localmente pela D5-C3** | `TRN-012/013` contratadas | estados sensíveis adicionais quando aplicáveis; validação integrada do handoff |
| Pessoa | oportunidades orgânicas | 7 | **7 validados; Detalhe revalidado pela UXA-101** | publicação/descoberta, Mapa/Lista/Detalhe e saída até BND-001 integrados | processo externo posterior separado |
| Pessoa | Conta/Configurações | **0** | sem SVG | TRN-406/407 contratadas | materialização própria de PER-009 somente se necessária |
| Pessoa | Planos, comparação e cobrança | **3** | **3 validados no pacote próprio** | TRN-401 a 405 locais; origem voluntária contratada | gateway/proration e materialização de PER-009 |
| Pessoa em Coletivos | descoberta e busca | 5 | 5 validados no recorte próprio | parcial | continuidade entre famílias |
| Pessoa em Coletivos | Perfil Público | 4 | 4 validados no recorte próprio | parcial | handoff para solicitação |
| Pessoa em Coletivos | revisão e solicitação | 5 | 5 validados | parcial | handoff bilateral |
| Pessoa em Coletivos | Solicitação Pendente | 8 | 8 validados | TRN-105/106/107/108/109 nos gates aplicáveis | outras continuidades separadas |
| Pessoa em Coletivos | Meus Coletivos | 1 | validado | TRN-108 e TRN-110 integralmente validadas | P0B separado |
| Pessoa em Coletivos | Central de Atualizações | 1 | validado | TRN-110 e TRN-111 integralmente validadas | P0B/P1 separados |
| Pessoa em Coletivos | Início do Participante | 1 | validado por UXA-095/096 no recorte da Pessoa participante; não deriva de UXA-016/018 | TRN-111 integralmente validada | P0B e áreas internas separadas |
| Coletivo | referência inicial histórica | 1 | `UXA-016/018` superseded; artefato físico não é wireframe principal vigente | não utilizável como baseline atual | **wireframe principal autenticado pendente** |
| Coletivo | Visão Geral do Responsável | 1 | UXA-086/087 preservam evidência local do pacote administrativo; **não constituem baseline final da UX principal** | TRN-112 e contratos de Planos preservam maturidade própria | arquitetura principal autenticada pendente |
| Coletivo | gestão de solicitações | 7 | 7 validados no fluxo especializado | handoffs aplicáveis integralmente validados | operação interna posterior |
| Coletivo | Planos, comparação e cobrança | **3** | **3 validados no fluxo especializado** | contratos de origem/retorno preservam maturidade própria; TRN-411 a 415 locais; TRN-416 parcial | contratação/dimensionamento assistido e cobrança real; origem principal final pendente |
| Organização | visão geral e cadastro | 2 | **ORG-001 histórico/superseded como wireframe principal; cadastro preserva validação própria por UXA-008/013** | publicação–descoberta preservada; contratos de Planos têm maturidade própria | **wireframe principal autenticado e matriz institucional completa pendentes** |
| Organização | Planos, comparação e cobrança | **3** | **3 validados no fluxo especializado** | contratos de origem/retorno preservam maturidade própria; TRN-421 a 425 locais; TRN-426 parcial | contratação/dimensionamento assistido e cobrança real; origem principal final pendente |
| camada comercial | Opportunity Boost | 46 | **46 validados no escopo próprio** | parcial | TRN-304/305/306 e integrações específicas |
| fronteira documental | destinos externos/comerciais | 0 | não aplicável | BND-001 examinada; BND-002 parcial | processo externo posterior; contratação/dimensionamento assistido |
| **Total físico do catálogo** |  | **121** | **maturidade agregada não pode ser inferida; recomputação governada pendente** |  |  |

## 3. Instrumentos granulares vigentes

| Registro | Quantidade física | Estado vigente |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | **57** | inventário granular; maturidade por item |
| transições documentais | **66** | maturidade por transição |
| catálogo físico | **121 SVGs** | `active` 0.32.0; inclui artefatos históricos superseded |
| matriz de rastreabilidade | **121 associações físicas / 34 perfis** | associação ≠ autoridade vigente |
| galeria visual | **121 SVGs físicos** | resumo global `121 validados / 0 pendentes` superseded como claim de maturidade |

## 4. Cobertura visual física

| Condição | Quantidade histórica/física |
|---|---:|
| IDs com referência visual direta ou agrupada | **45** |
| responsabilidades sem SVG dedicado | **10** |
| fronteiras intencionalmente sem tela | **2** |
| **Total de IDs** | **57** |

Essas contagens descrevem cobertura física/associativa do snapshot e não resolvem a vigência de cada artefato após supersessões posteriores.

## 5. Efeito acumulado D5-C2 → D5-C3 no snapshot histórico

D5-C2 alterou o inventário físico:

- SVGs físicos registrados: **118 → 121**;
- associações: **118 → 121**;
- perfis: **31 → 34**;
- IDs com referência visual no snapshot: **42 → 45**;
- responsabilidades sem SVG dedicado no snapshot: **13 → 10**.

No momento de D5-C3, o registro declarou:

- validações funcionais de SVG naquele snapshot: **118 → 121**;
- pendências específicas daquele snapshot: **3 → 0**;
- `PER-010`, `PER-011` e `PER-012`: promovidos para **validados localmente**;
- `TRN-008..013`: permaneceram contratadas;
- `PER-009`: permaneceu responsabilidade sem SVG dedicado.

A reconciliação pós-PR #313/#314 **não reescreve a história desse snapshot**, mas supersede seu uso como resumo da maturidade visual atual do repositório, porque `UXA-015..018` deixaram de possuir autoridade vigente.

## 6. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`;
- Hoje sintetiza direção, movimento e continuidade, mas não substitui `PER-010`, `PER-011` ou `PER-012`;
- `PER-010` governa Objetivos, não score de direção ou produtividade;
- `PER-011` governa movimentos contextuais, não uma lista coercitiva de tarefas;
- `PER-012` governa trajetórias de evolução, não roda da vida, ranking ou nota humana;
- em Minha Evolução, Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo ≠ aspecto descritivo da mudança;
- validação local de `PER-010..012` ≠ validação integrada de `TRN-008..013`;
- presença de retorno visual para Hoje ≠ validação dos handoffs;
- D5-C1/C2/C3 não criam handoff direto entre `PER-010`, `PER-011` e `PER-012`;
- revisão de saída é estado do mesmo `PER-203`, não nova tela canônica;
- `BND-001` representa a transferência de autoridade, não o processo do terceiro;
- `PER-009` é responsabilidade de Conta suficiente para handoff e não uma arquitetura completa de Conta;
- `PER-106` organiza participações e não substitui a Central;
- `PER-107` é triagem de atualizações;
- `PER-108` sintetiza contexto interno e não replica canais especializados;
- comparação incremental de Planos não é tela adicional;
- processamento financeiro transitório não é tela própria;
- navegar para Planos não inicia cobrança;
- `BND-002` representa contratação/dimensionamento assistido quando aplicável e não é plano Enterprise ou Scale;
- Coletivo usa `Livre · Mobiliza · Impacta · Rede`;
- Organização usa `Conecta · Eleva · Transforma`;
- Guivos Business usa `Start · Growth · Scale · Enterprise` como Produto Especializado separado;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem continuidades separadas;
- **materialização histórica de Organização/Coletivo ≠ wireframe principal autenticado vigente**;
- **contrato de navegação especializado ≠ definição da arquitetura principal autenticada**.

## 7. Estado do catálogo

- catálogo físico: `active` 0.32.0;
- inventário físico preservado: **121 SVGs**;
- matriz física: **121 associações / 34 perfis**;
- resumo `121 SVGs / 121 validados / 0 pendentes`: **superseded como claim de maturidade vigente**;
- wireframe principal autenticado da Organização: **pendente**;
- wireframe principal autenticado do Coletivo: **pendente**;
- fluxos especializados preservam sua maturidade própria quando sustentados por autoridade independente;
- `PER-010..012`: permanecem validados localmente pela D5-C3;
- `TRN-008..013`: preservam seu estado documental próprio;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

Nenhuma contagem corrigida de wireframes vigentes/validados é inferida nesta reconciliação. Uma nova contagem somente poderá ser publicada após recomputação governada do inventário.