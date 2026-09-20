---
id: GKR-JOURNEY-SCREEN-CATALOG-001
title: Catálogo Integrado de Telas
status: active
version: 0.38.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-18
related:
  - UXA-070
  - UXA-080
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
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - UXA-100-A4
  - UXA-101
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C2-001
  - GKR-UX-D5-C3-001
  - GKR-UX-D5-C4B-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
  - GKR-UX-ORGCOL-AUTH-PRIORITY-FLOWS-001
  - GKR-ORGCOL-POST313-RECON-001
normative: false
---

# Catálogo Integrado de Telas

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


## 1. Regra de leitura

Este catálogo descreve **responsabilidades funcionais correntes**, não a história dos arquivos visuais que já existiram.

```text
SURFACE / RESPONSIBILITY
≠ WIREFRAME FINAL
≠ IMPLEMENTATION

CURRENT REGISTRY
→ FUNCTIONAL AUTHORITY

HISTORICAL SVG COUNTS
→ NOT CURRENT INPUT
→ NOT DESIGN / AI INPUT
```

A materialização visual pertence à fase de Design.

## 2. Inventário funcional corrente

O inventário corrente é governado pelos registries:

- `GKR-JOURNEY-SURFACE-REGISTRY-001`;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001`;
- detalhes de Pessoa, Coletivo, Organização e fronteiras comerciais;
- autoridades autenticadas específicas quando aplicáveis.

Não usar contagens históricas de SVGs, perfis ou associações como proxy de maturidade ou cobertura.

## 3. Instrumentos granulares vigentes

| Registro | Quantidade física | Estado vigente |
|---|---:|---|
| superfícies/estados/responsabilidades/fronteiras | **57** | inventário granular; maturidade por item |
| transições documentais | **66** | maturidade por transição; `TRN-008..013` integrais |
| catálogo físico | **0 SVGs** | `active` 0.37.0; camada física removida por F-016-A |
| perfis históricos de rastreabilidade | **34 perfis históricos** | instrumento de matriz removido; proveniência recuperável no histórico Git |
| galeria visual histórica | **0 SVGs físicos** | documentos de galeria removidos do corpus corrente; proveniência preservada no histórico Git |

## 4. Cobertura para Design e prototipação

```text
PHYSICAL VISUAL BASELINE
→ NONE IMPOSED BY GKR

DESIGNER
→ CREATES VISUAL MATERIALIZATION

FUNCTIONAL COVERAGE
→ READ FROM CURRENT SURFACE + TRANSITION REGISTRIES

HISTORICAL VISUAL INVENTORY
→ EXCLUDED
```

## 6. Separações obrigatórias

- primeira Tela Hoje e Tela Hoje recorrente são variantes do mesmo `PER-008`;
- Hoje sintetiza direção, movimento e continuidade, mas não substitui `PER-010`, `PER-011` ou `PER-012`;
- `PER-010` governa Objetivos, não score de direção ou produtividade;
- `PER-011` governa movimentos contextuais, não uma lista coercitiva de tarefas;
- `PER-012` governa trajetórias de evolução, não roda da vida, ranking ou nota humana;
- em Minha Evolução, Domínio de Evolução ≠ dimensão estrutural do Contexto Vivo ≠ aspecto descritivo da mudança;
- validação local de `PER-010..012` e validação integrada de `TRN-008..013` são maturidades distintas, ambas atualmente documentadas por suas autoridades próprias;
- presença de retorno visual para Hoje, isoladamente, não teria validado os handoffs; a promoção vigente deriva de D5-C4B;
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

- catálogo físico: `active` 0.37.0;
- inventário físico corrente após F-016-A: **0 SVGs**;
- Surface Map lógico-documental O/C: **definido/canônico por `GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001 v1.0.0`**;
- State Map funcional O/C: **definido/canônico por `GKR-UX-ORGCOL-AUTH-STATE-MAP-001 v1.0.0`**;
- Priority Flows O/C: **DEFINED / CANONICAL DOCUMENTARY**;
- navegação materializada O/C: **pendente / não materializada**;
- wireframes principais autenticados O/C: **não iniciados**;
- materialização visual da Organização: **autoridade exclusiva de Design; não é requisito documental**;
- materialização visual do Coletivo: **autoridade exclusiva de Design; não é requisito documental**;
- fluxos especializados preservam sua maturidade própria quando sustentados por autoridade independente;
- `PER-010..012`: permanecem validados localmente pela D5-C3;
- `TRN-008..013`: **integralmente validadas documentalmente pela D5-C4B**;
- jornadas da Pessoa, Coletivo e Organização: `draft`;
- protótipo e Engenharia de Produto: não iniciados.

Nenhuma contagem corrigida de wireframes vigentes/validados é inferida nesta reconciliação. Uma nova contagem somente poderá ser publicada após recomputação governada do inventário.