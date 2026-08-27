---
id: GKR-ORGCOL-POST313-RECON-001
title: Reconciliação Transversal Pós-313 — Organizações e Coletivos
status: active
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-26
normative: true
related:
  - GKR-STATE-001
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - UXA-014
  - UXA-019
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
---

# Reconciliação Transversal Pós-313 — Organizações e Coletivos

## 1. Finalidade

Este registro reconcilia os derivados transversais do GKR após a PR #313, que corrigiu o estado de Organizações e Coletivos e estabeleceu que os wireframes principais da experiência autenticada ainda não foram oficialmente definidos.

A função deste documento é impedir que snapshots anteriores do catálogo de telas, registro de superfícies, jornadas integradas ou registro global sejam interpretados como autoridade superior ao estado corrigido.

## 2. Regra de precedência

No escopo de Organizações e Coletivos, quando houver divergência entre um registro derivado anterior e o estado estabelecido pela PR #313, prevalece a seguinte cadeia:

```text
UXA-014 — fundamentos funcionais
+
UXA-019 — relações Organização ↔ Coletivo
+
GKR-UX-ORGCOL-STATE-001 — visão geral e estado atual
+
GKR-UX-ORGCOL-UX-STATE-001 — estado de UX e wireframes
↓
este registro de reconciliação transversal
↓
catálogos, matrizes, jornadas e snapshots derivados anteriores
```

Este documento não substitui os fundamentos. Ele corrige somente a leitura de maturidade dos derivados.

## 3. Estado vigente dos wireframes principais

O estado obrigatório é:

```text
Visão geral / início autenticado da Organização
→ wireframe oficial NÃO DEFINIDO

Visão geral / início autenticado do Coletivo
→ wireframe oficial NÃO DEFINIDO

Arquitetura final de informação e navegação interna
→ PENDENTE

Validação de wireframe principal
→ NÃO REALIZADA EM OBJETO VIGENTE

UI / protótipo / teste de usabilidade dessas superfícies
→ PENDENTE
```

A existência de fundamentos, fluxos especializados, telas locais, Planos, cadastro de oportunidades, gestão de solicitações ou Home pública não altera esse estado.

## 4. Registros históricos superseded

A PR #313 estabeleceu:

```text
UXA-015 → superseded
UXA-016 → superseded
UXA-017 → superseded
UXA-018 → superseded
```

Os SVGs associados a UXA-015 e UXA-016 permanecem fisicamente no repositório por rastreabilidade histórica, mas não constituem:

- wireframe oficial vigente;
- baseline de produto;
- especificação de UI;
- referência aprovada para Engenharia;
- evidência atual de validação funcional;
- autorização para inferir arquitetura final de navegação.

## 5. Efeito sobre o Registro do Estado Atual

O `GKR-STATE-001` anterior à PR #313 registrava, entre outros snapshots:

```text
SVGs → 121 — 121 validados / 0 pendentes
```

Essa formulação deixa de ser válida como claim global de maturidade visual.

A PR #313 não apaga os arquivos físicos. Portanto:

- o inventário físico pode continuar contendo 121 SVGs;
- dois SVGs associados a `UXA-015` e `UXA-016` são agora referências históricas superseded;
- o número físico de arquivos não pode mais ser usado como sinônimo de número de wireframes vigentes ou validados;
- qualquer contagem de “SVGs validados vigentes” deverá ser recalculada a partir do conjunto atual de autoridades, em vez de derivada automaticamente do total físico.

Até essa recomputação, a formulação correta é:

> **O GKR preserva o inventário físico histórico, mas a maturidade visual vigente deve excluir referências superseded e não pode ser resumida por `121/121 validados`.**

## 6. Efeito sobre o Catálogo Integrado de Telas

O `GKR-JOURNEY-SCREEN-CATALOG-001` anterior à PR #313 contém snapshots como:

- `Coletivo | referência inicial | 1 | validado`;
- `Organização | visão geral e cadastro | 2 | 2 validados`;
- `Total canônico | 121 | 121 validados; 0 pendentes`.

Esses trechos não podem mais ser interpretados literalmente no escopo corrigido.

Correção de leitura:

### 6.1 Organização

O cadastro de oportunidade e outras superfícies especializadas mantêm sua maturidade própria quando sustentadas por autoridades não superseded.

A antiga Visão Geral da Organização derivada de `UXA-015/017` não é wireframe vigente e não pode ser contabilizada como tela principal validada.

### 6.2 Coletivo

Fluxos especializados posteriores — por exemplo descoberta pública, solicitação, gestão de solicitações, Planos e outras materializações que possuam autoridade própria — preservam sua maturidade local.

A antiga referência geral de `UXA-016/018` não define a experiência autenticada final do Coletivo.

### 6.3 Total agregado

O total físico histórico pode permanecer registrado, mas a coluna de maturidade precisa distinguir pelo menos:

```text
vigente e validado
materializado/local
pendente
histórico superseded
```

O agregado `121 validados / 0 pendentes` fica supersedido como resumo de maturidade.

## 7. Efeito sobre o Registro Granular de Superfícies

O `GKR-JOURNEY-SURFACE-REGISTRY-001` anterior à reconciliação utiliza `UXA-015/017` para classificar `GKR-SURF-ORG-001 — Visão Geral da Organização` como validada.

Essa classificação fica supersedida.

O estado correto é:

```text
GKR-SURF-ORG-001
→ responsabilidade/superfície institucional conhecida
→ fundamento funcional existente
→ wireframe oficial vigente pendente
→ validação do wireframe oficial pendente
```

A superfície conceitual pode continuar existindo como responsabilidade da Jornada sem possuir materialização oficial.

Para o Coletivo, referências que dependam materialmente de `UXA-016/018` devem ser desconsideradas como evidência de wireframe vigente. Evidências independentes, posteriores e específicas preservam sua maturidade local.

## 8. Efeito sobre a Jornada Integrada da Organização

A versão anterior de `GKR-JOURNEY-ORGANIZATION-001` apresenta:

```text
Visão Geral da Organização
→ validado
→ referência UXA-015
→ validação UXA-017
```

Esse estado fica supersedido.

A leitura vigente passa a ser:

```text
Visão Geral / início autenticado da Organização
→ responsabilidade funcional conhecida
→ wireframe oficial pendente
→ validação do wireframe oficial pendente
→ jornada geral permanece draft
```

Fluxos independentes como cadastro de oportunidades, descoberta e Planos mantêm sua autoridade própria no escopo em que não dependam da materialização superseded.

Qualquer integração cuja validação dependa especificamente da antiga composição visual de `UXA-015` deve ser reavaliada quando o wireframe oficial da Organização for construído.

## 9. Efeito sobre a Jornada Integrada do Coletivo

A versão anterior de `GKR-JOURNEY-COLLECTIVE-001` utiliza `UXA-016/018` como parte da evidência de presença inicial.

A partir da PR #313:

- `UXA-016/018` não sustentam mais maturidade vigente;
- superfícies públicas sustentadas por referências independentes, como os fluxos públicos posteriores, mantêm sua maturidade própria;
- superfícies administrativas especializadas com materializações posteriores preservam validação local quando houver autoridade específica;
- nenhuma dessas materializações equivale à definição da Home / Início autenticado final do Coletivo;
- a Jornada do Coletivo continua `draft`.

## 10. Wireframe principal ≠ fluxo especializado

A reconciliação preserva uma distinção importante:

```text
wireframe principal da experiência autenticada
≠
wireframe local de uma capacidade específica
```

É possível existir materialização local de:

- cadastro de oportunidade;
- gestão de solicitações;
- Planos;
- revisão de contratação;
- estados de pedido;
- perfil público;
- descoberta;

sem que exista arquitetura final da Home autenticada, navegação geral e hierarquia completa do participante.

Portanto, a PR #313 não invalida automaticamente todo artefato visual ligado a Organização ou Coletivo. Ela invalida a interpretação de que os antigos `UXA-015..018` já resolviam a experiência principal.

## 11. Estado das transições que dependem de superfícies principais

Transições documentadas em pacotes especializados mantêm sua evidência local, mas não podem ser usadas para afirmar que a arquitetura final da experiência autenticada está fechada.

Em especial:

- a origem/retorno de Planos da Organização deverá ser revalidada contra o futuro wireframe oficial da Organização se a composição ou navegação mudar;
- a navegação administrativa local do Coletivo permanece evidência de seus pacotes específicos, mas não determina a arquitetura final do Coletivo;
- nenhuma transição especializada autoriza inferir menu global, dashboard, Home autenticada ou arquitetura completa.

## 12. Estado de maturidade consolidado

| Dimensão | Organização | Coletivo |
|---|---|---|
| fundamento funcional | existente | existente |
| relação entre participantes | existente em conjunto | existente em conjunto |
| Research de supply / valor | existente | existente |
| jornada integrada | draft | draft |
| fluxos especializados | parciais / alguns validados localmente | parciais / vários validados localmente |
| arquitetura final de informação autenticada | pendente | pendente |
| mapa final de superfícies | pendente | pendente |
| wireframe principal | **pendente** | **pendente** |
| validação do wireframe principal | **pendente** | **pendente** |
| UI final | pendente | pendente |
| protótipo | pendente | pendente |
| testes de usabilidade | pendente | pendente |
| handoff técnico da experiência principal | pendente | pendente |

## 13. Próxima sincronização mecânica necessária

Os seguintes derivados deverão ser normalizados futuramente para incorporar esta reconciliação diretamente em suas tabelas, sem depender apenas deste overlay:

- `GKR-STATE-001`;
- `GKR-JOURNEY-SCREEN-CATALOG-001`;
- `GKR-JOURNEY-SURFACE-REGISTRY-001`;
- detalhamento de superfícies da Organização;
- detalhamento de superfícies do Coletivo;
- Jornada Integrada da Organização;
- Jornada Integrada do Coletivo;
- galeria/matriz visual, quando seus totais utilizarem maturidade dos artefatos superseded.

Até essa normalização, este documento possui precedência explícita no escopo da divergência.

## 14. Regra final

> **Arquivo físico não é autoridade vigente. Materialização histórica não é wireframe aprovado. Validação antiga não sobrevive à supersessão do objeto que validava.**

A experiência principal de Organizações e Coletivos somente poderá voltar a ser declarada materializada/validada quando novos wireframes forem definidos, revisados e validados a partir do estado atual.