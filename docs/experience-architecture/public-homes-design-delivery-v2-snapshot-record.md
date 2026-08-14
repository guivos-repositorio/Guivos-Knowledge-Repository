---
id: GKR-UX-HOMES-DESIGN-DELIVERY-V2-SNAPSHOT-001
title: Homes Públicas — Registro do Snapshot Externo de Design v2
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-14
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOME-ADS-GENINPUT-001
normative: false
---

# Homes Públicas — Registro do Snapshot Externo de Design v2

## 1. Finalidade

Este registro fecha o ato pós-merge previsto por `GKR-UX-HOMES-DESIGN-DELIVERY-001` v2.0.0 e registra a materialização efetiva da emissão externa v2 do handoff de Design das seis Homes públicas convergidas.

Ele não cria nova arquitetura e não substitui o Manifesto Canônico de Entrega. Sua função é registrar o fato operacional reproduzível da emissão.

## 2. Checkpoint canônico de origem

```text
repository: guivos-repositorio/Guivos-Knowledge-Repository
main canônica de origem: 603aa7f37435ac376f7a202669ad4ac1d7d13a83
```

Esse commit já contém, integrados à `main`:

- `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.1.0;
- `GKR-UX-HOMES-DESIGN-DELIVERY-001` v2.0.0;
- `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001` v1.1.0;
- `GKR-UX-HOME-ADS-GENINPUT-001` v1.0.0;
- as autoridades específicas requeridas pelas seis Homes.

## 3. Snapshot externo materializado

```text
branch: delivery/design-handoff-v2
snapshot commit: 486f1c5e784be6cf3db9b2fbcbc47da39f9e9016
snapshot tree: 650ecb5286cbd5d8d99f274fb0d9dc697b830fa4
parent canônico: 603aa7f37435ac376f7a202669ad4ac1d7d13a83
```

A branch externa contém somente o pacote de distribuição, não uma cópia operacional do repositório inteiro.

## 4. Composição confirmada

A árvore foi auditada e contém exatamente:

```text
19 FONTES CANÔNICAS
+
6 GUIAS OPERACIONAIS LEIA-PRIMEIRO
=
25 ARQUIVOS EXTERNOS
```

As seis Homes são:

1. Pessoa;
2. Organizações e Coletivos;
3. Guivos Mall;
4. Guivos Travel;
5. Guivos Media;
6. Guivos Ads.

A pasta do Ads contém:

```text
06-HOME-ADS/
├── 00-LEIA-PRIMEIRO-ADS.md
├── 01-Documento-Mestre.md
├── 02-GPA-007-Guivos-Ads.md
└── 03-Source-Lock-Prompt.md
```

## 5. Integridade histórica da v1

A emissão v1 permanece intacta:

```text
branch: delivery/design-handoff-v1
snapshot commit: 8e2a356ca84ba980e588258757800cde2a946f40
```

A v2 não move, reescreve nem substitui retroativamente a v1.

## 6. Regra de autoridade

`delivery/design-handoff-v2` é artefato externo reproduzível de distribuição.

Não é:

- fonte canônica paralela à `main`;
- autorização de Engenharia;
- autorização de publicação;
- aprovação automática de qualquer output visual;
- autorização para misturar documentos específicos das seis Homes na mesma execução generativa.

A autoridade permanece nos documentos canônicos da `main`.

## 7. Uso

O fluxo operacional permanece:

```text
BAIXAR O ZIP
↓
abrir 00-LEIA-PRIMEIRO
↓
escolher UMA Home
↓
abrir o LEIA-PRIMEIRO daquela Home
↓
seguir os 3 documentos específicos
↓
usar Source Lock + Prompt
↓
Figma Make / ferramenta equivalente
↓
OUTPUT = EXPLORAÇÃO
```

## 8. Síntese

> **A emissão externa v2 está materializada, reproduzível e separada por Home; a v1 permanece preservada e a `main` continua sendo a única fonte canônica.**

Estado desta frente:

> **DESIGN HANDOFF V2 MATERIALIZADO — 6 HOMES — 25 ARQUIVOS EXTERNOS — SNAPSHOT `486f1c5e784be6cf3db9b2fbcbc47da39f9e9016` — V1 PRESERVADA.**
