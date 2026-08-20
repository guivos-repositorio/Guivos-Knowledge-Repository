---
id: GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
title: Homes Públicas — Registro do Snapshot Externo de Design v4
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-20
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOME-INTELLIGENCE-HANDOFF-001
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
  - GKR-UX-HOME-INTELLIGENCE-GENINPUT-001
  - GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001
  - GPA-006
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V3-SNAPSHOT-001
  - GKR-INTELLIGENCE-HOME-CONTINUITY-001
normative: false
---

# Homes Públicas — Registro do Snapshot Externo de Design v4

## 1. Finalidade

Este registro fecha o ato pós-merge previsto por `GKR-UX-HOMES-DESIGN-DELIVERY-001` v4.0.0 e registra a materialização efetiva da emissão externa v4 do handoff das oito Homes públicas convergidas.

Ele não cria nova arquitetura, não modifica decisões canônicas e não substitui o Manifesto Canônico de Entrega. Sua função é registrar o fato operacional reproduzível da emissão.

A emissão v4 adiciona **Guivos Intelligence** ao mesmo método de entrega já utilizado para Pessoa, Organizações e Coletivos, Mall, Travel, Media, Ads e Business, preservando cada Home como contexto de trabalho isolado.

---

## 2. Checkpoint canônico de origem

```text
repository: guivos-repositorio/Guivos-Knowledge-Repository
main canônica de origem: f900318af746ba25e3bb18d18bfddee5654620c7
```

Esse checkpoint já contém integrados à `main`:

- `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.3.0;
- `GKR-UX-HOMES-DESIGN-DELIVERY-001` v4.0.0;
- `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001` v1.3.0;
- as 25 fontes canônicas preservadas da emissão v3;
- `GKR-UX-HOME-INTELLIGENCE-GENINPUT-001` v1.0.0;
- `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001` v1.0.0;
- `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001` v1.0.0;
- `GKR-UX-HOME-INTELLIGENCE-MASTER-001` v0.1.1;
- `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001` v1.0.0;
- `GPA-006` v2.0.0.

As 31 fontes obrigatórias foram revalidadas no mesmo checkpoint antes da materialização.

---

## 3. Snapshot externo materializado

```text
branch: delivery/design-handoff-v4
snapshot commit: dfed980d8cfb39bbe4694e58d7c86ca0692266dc
snapshot tree: 270e404cf0b5bf0d5d543bbbb0c5bd6a1f4602df
parent canônico: f900318af746ba25e3bb18d18bfddee5654620c7
```

O commit do snapshot possui como pai direto o checkpoint canônico de origem acima.

A branch externa contém somente o pacote de distribuição. Ela não é uma cópia operacional do repositório inteiro e não constitui fonte canônica paralela à `main`.

---

## 4. Composição confirmada

A árvore congelada foi materializada com exatamente:

```text
31 FONTES CANÔNICAS CONGELADAS
+
8 GUIAS OPERACIONAIS LEIA-PRIMEIRO
=
39 ARQUIVOS EXTERNOS
```

As oito Homes são:

1. Pessoa;
2. Organizações e Coletivos;
3. Guivos Mall;
4. Guivos Travel;
5. Guivos Media;
6. Guivos Ads;
7. Guivos Business;
8. Guivos Intelligence.

Os **31 arquivos canônicos** do pacote reutilizam diretamente os blobs do checkpoint `f900318af746ba25e3bb18d18bfddee5654620c7`. Eles não foram resumidos, reescritos ou reinterpretados para formar o snapshot.

Os únicos conteúdos novos do pacote externo são os **oito guias operacionais `LEIA-PRIMEIRO`**, sem autoridade normativa e destinados exclusivamente a ordenar leitura, isolamento de contexto e execução externa futura.

Nenhum arquivo de wireframe, tela, SVG visual, UI, protótipo ou exploração visual foi incluído ou criado pelo ato de emissão.

---

## 5. Home Pública — Guivos Intelligence

Intelligence entra na v4 como a oitava Home e possui exatamente o contexto específico previsto pelo Manifesto v4, além do Handoff Canônico comum.

Sua pasta externa contém:

```text
08-HOME-INTELLIGENCE/
├── 00-LEIA-PRIMEIRO-INTELLIGENCE.md
├── 01-Source-Lock-Operacional-Prompt.md
├── 02-Handoff-Especifico.md
├── 03-Source-Lock-da-Home.md
├── 04-Documento-Mestre.md
├── 05-Product-Source-Lock.md
└── 06-GPA-006-Guivos-Intelligence.md
```

A ordem operacional preservada é:

```text
HANDOFF CANÔNICO COMUM
↓
GENINPUT / SOURCE LOCK OPERACIONAL
↓
HANDOFF ESPECÍFICO INTELLIGENCE
↓
HOME SOURCE LOCK
↓
DOCUMENTO MESTRE
↓
PRODUCT SOURCE LOCK
↓
GPA-006
↓
EXECUÇÃO FUTURA NA FRENTE EXTERNA DE DESIGN
↓
OUTPUT = EXPLORAÇÃO
```

O pacote preserva explicitamente:

```text
INTELLIGENCE ≠ JOURNEY
INTELLIGENCE ≠ BUSINESS
COMPREENDER ≠ DECIDIR
SINAL ≠ CERTEZA
TENDÊNCIA ≠ DESTINO
PERCEBER ANTES ≠ PREVER O FUTURO
```

Também permanecem preservados os 11 movimentos funcionais, a explicabilidade, a autonomia da pessoa, a assimetria de privacidade e a proibição de claims preditivos ou causais indevidos.

---

## 6. Integridade das emissões anteriores

As emissões anteriores permanecem históricas e intactas.

```text
v1: delivery/design-handoff-v1
v2: delivery/design-handoff-v2
v3: delivery/design-handoff-v3
v4: delivery/design-handoff-v4
```

A v4 não move, reescreve nem substitui retroativamente as árvores congeladas de v1, v2 ou v3.

A adição da Home Intelligence ocorre somente na emissão v4.

---

## 7. Regra de autoridade

`delivery/design-handoff-v4` é um artefato externo reproduzível de distribuição.

Não é:

- fonte canônica paralela à `main`;
- nova decisão de produto;
- nova decisão narrativa;
- autorização de Engenharia;
- autorização de publicação;
- aprovação automática de qualquer output visual;
- autorização para misturar documentos específicos das oito Homes na mesma execução generativa;
- autorização para redefinir Intelligence a partir de tecnologia, Journey ou Business.

A autoridade permanece nos documentos canônicos da `main`.

Cada Home deve ser trabalhada como contexto isolado, conforme o Manifesto v4 e o Handoff Canônico.

---

## 8. Tratamento oficial do ZIP

O `.zip` é somente um **formato de conveniência para transferência humana** do snapshot externo.

Regras:

1. o binário `.zip` **não é fonte canônica**;
2. o binário `.zip` **não deve ser versionado como autoridade no GKR**;
3. quando gerado, deve derivar exclusivamente da árvore congelada `270e404cf0b5bf0d5d543bbbb0c5bd6a1f4602df` do commit `dfed980d8cfb39bbe4694e58d7c86ca0692266dc`;
4. sua estrutura interna deve preservar exatamente a separação por Home definida em `GKR-UX-HOMES-DESIGN-DELIVERY-001` v4.0.0;
5. gerar, baixar, recomprimir ou transportar o ZIP não altera o snapshot oficial;
6. em qualquer divergência entre um ZIP de conveniência e a branch congelada, prevalece `delivery/design-handoff-v4` no snapshot commit registrado neste documento.

Portanto:

> **O snapshot Git é a referência reproduzível; o ZIP é apenas sua embalagem transportável.**

Nenhum ZIP binário é introduzido na `main` por este registro.

---

## 9. Limite da emissão

A materialização do pacote v4 **não produziu Design**.

Não foram criados neste ato:

- tela;
- mapa visual;
- wireframe;
- arquitetura visual;
- direção visual;
- layout;
- componentes de UI;
- Design tokens;
- protótipo;
- implementação frontend;
- aprovação visual final.

Qualquer saída futura eventualmente produzida por uma frente externa de Design a partir deste pacote começa obrigatoriamente como:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO**

até revisão e aprovação humanas posteriores.

---

## 10. Síntese

> **A emissão externa v4 está materializada, reproduzível e separada em oito contextos de Home; 31 fontes canônicas permanecem byte-preservadas a partir da `main`, oito guias operacionais organizam a execução, Intelligence entra como oitava Home com suas fronteiras próprias, e o ZIP permanece apenas uma embalagem derivada da árvore congelada.**

Estado desta frente:

> **DESIGN HANDOFF V4 MATERIALIZADO — 8 HOMES — 31 FONTES CANÔNICAS + 8 GUIAS = 39 ARQUIVOS EXTERNOS — SNAPSHOT `dfed980d8cfb39bbe4694e58d7c86ca0692266dc` — TREE `270e404cf0b5bf0d5d543bbbb0c5bd6a1f4602df` — V1/V2/V3 PRESERVADAS — SEM TELA, WIREFRAME, UI, PROTÓTIPO OU DESIGN PRODUZIDO.**
