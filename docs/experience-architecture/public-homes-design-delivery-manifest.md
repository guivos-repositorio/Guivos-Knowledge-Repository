---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 5.1.3
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: v5_frozen_v6_candidate_pre_snapshot
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-UX-HOMES-DESIGN-SOURCE-COMPLETENESS-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V6-CANDIDATE-001
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este Manifesto registra o pacote externo v5 já emitido e congelado e aponta para o pacote v6 candidato atualmente em finalização documental. O v5 permanece reproduzível como snapshot histórico; novas execuções devem aguardar a adjudicação do v6.

O snapshot v4 permanece histórico e reproduzível, mas não é pacote atual porque seu checkpoint foi superado.

## 2. Princípio do v5

O v5 elimina GENINPUTs operacionais de checkpoints superados do pacote de produção. Em seu lugar, cada Home recebe um `LEIA-PRIMEIRO / SOURCE LOCK OPERACIONAL` gerado no momento da emissão a partir das autoridades pós-auditoria.

A ausência de identidade visual canônica não é lacuna: estética e sistema visual são responsabilidade criativa da designer.

## 3. Composição canônica — 26 fontes únicas

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.6.1`;
2. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v2.1.3`;
3. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.1.2`;
4. `docs/experience-architecture/public-homes-design-delivery-operational-flow.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.1`.

### 3.2 Pessoa

5. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001 v1.0.2`;
6. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### 3.3 Organizações e Coletivos

7. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001 v1.0.0`;
8. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### 3.4 Mall

9. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.0.0`;
10. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.5 Travel

11. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001 v1.0.0`;
12. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.6 Media

13. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.1`;
14. `docs/product-architecture/media.md` — `GPA-005 v1.2.0`.

### 3.7 Ads

15. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001 v1.0.1`;
16. `docs/product-architecture/ads.md` — `GPA-007 v1.3.0`.

### 3.8 Business

17. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.0.0`;
18. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001 v1.0.0`;
19. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
20. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
21. `docs/product-architecture/business.md` — `GPA-004 v1.6.0`.

### 3.9 Intelligence

22. `docs/experience-architecture/public-home-intelligence-design-handoff.md` — `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
23. `docs/experience-architecture/public-home-intelligence-source-lock.md` — `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
24. `docs/experience-architecture/public-home-intelligence-master-document.md` — `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.1.1`;
25. `docs/product-architecture/intelligence-product-source-lock.md` — `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
26. `docs/product-architecture/intelligence.md` — `GPA-006 v2.0.0`.

## 4. Oito guias operacionais

A emissão v5 gerou oito arquivos adicionais `00-LEIA-PRIMEIRO.md`, um por Home. Cada guia funciona como Source Lock operacional daquele snapshot e deve conter:

- Home e objetivo;
- commit canônico de origem;
- lista exata de fontes e SHAs;
- ordem de leitura;
- invariantes específicos;
- liberdades criativas;
- matriz das oito classes operacionais de informação;
- proibições de inferência;
- prompt inicial histórico do v5 para ferramenta generativa; no v6, o guia será tool-neutral e IA será opcional;
- estado inicial `EXPLORAÇÃO / NÃO CANÔNICA`;
- checklist de autoauditoria.

## 5. Estrutura externa

`GUIVOS-HOMES-DESIGN-HANDOFF-v5/` deve conter `00-COMUM` e oito diretórios isolados: Pessoa, Organizações-e-Coletivos, Mall, Travel, Media, Ads, Business e Intelligence.

Os 26 arquivos canônicos devem reutilizar os blobs do mesmo checkpoint pós-merge. Os oito guias podem ser materializados especificamente para a emissão.

Contagem planejada: `26 FONTES CANÔNICAS + 8 GUIAS = 34 ARQUIVOS EXTERNOS`.

### 5.1 Integridade, formato e transporte

A emissão v5 preserva as seguintes regras:

1. os 26 documentos canônicos são extraídos do **mesmo commit pós-merge**;
2. seus conteúdos são reutilizados sem resumo, reescrita ou adaptação para caber no pacote;
3. IDs, versões e conteúdo interno não mudam por causa do nome externo do arquivo;
4. os oito `LEIA-PRIMEIRO` são artefatos operacionais da emissão e não reescrevem as autoridades que listam;
5. o snapshot registra commit de origem, commit/tree da emissão e relação reproduzível entre ambos;
6. `delivery/design-handoff-v5` permanece separada de v1–v4;
7. v1–v4 permanecem snapshots históricos imutáveis e não são reescritos para representar v5;
8. Markdown (`.md`) é o formato primário para leitura humana e input de IA;
9. PDF pode existir como conveniência de leitura humana, mas não substitui Markdown como fonte;
10. ZIP pode ser gerado como embalagem de transferência, mas não constitui autoridade canônica;
11. qualquer ZIP deriva exclusivamente do snapshot v5 validado e preserva sua estrutura;
12. em divergência entre ZIP e snapshot Git, prevalece o snapshot Git registrado;
13. nenhum arquivo específico de outra Home é misturado no diretório de execução de uma Home por conveniência;
14. nenhuma referência externa passa a integrar as 26 fontes canônicas sem nova adjudicação.

```text
SNAPSHOT GIT V5
→ REPRODUCIBLE AUTHORITY OF THE EXTERNAL PACKAGE

ZIP
→ TRANSFER CONVENIENCE ONLY

PDF
→ HUMAN READING AID ONLY

MARKDOWN
→ PRIMARY SOURCE FORMAT
```

### 5.2 Mudança de fonte após a emissão

Se qualquer uma das 26 fontes sofrer mudança depois do snapshot, classificar o impacto.

```text
NON-MATERIAL CHANGE
→ MAY PRESERVE SNAPSHOT AFTER RECORDED REVIEW

MATERIAL CHANGE TO MEANING / INVARIANT / COPY LOCK / SOURCE PACKAGE / PROMPT / ACCEPTANCE
→ AFFECTED HOME PACKAGE INVALIDATED FOR NEW EXECUTION
→ REISSUE / REVALIDATE BEFORE CONTINUING
```

Uma alteração puramente criativa da designer, em qualquer ferramenta, que não modifica o contrato do GKR não exige reemissão do pacote fonte.

## 6. Regra para ferramentas generativas

Não carregar documentos específicos de múltiplas Homes na mesma execução.

O contexto de cada execução deve ser:

```text
00-COMUM
+
00-LEIA-PRIMEIRO / SOURCE LOCK DA HOME
+
FONTES ESPECÍFICAS DA HOME
```

A identidade visual é livre; fatos e arquitetura não são.

## 7. Materiais fora do pacote inicial

- snapshots v1–v4;
- GENINPUTs históricos de checkpoint;
- benchmarks;
- rascunhos de conversa;
- documentação de Engenharia;
- pricing não formalizado;
- assets ou brand book visual inexistentes como suposta obrigação.

Referências adicionais entram somente para resolver dúvida concreta e permanecem `INSPIRATION_ONLY` ou fonte adicional explicitamente declarada, conforme sua natureza.

## 8. Gate de emissão

O gate de emissão foi executado e validado:

1. `main` pós-merge capturada em `aa1b524c20f6707d007208222ba8581af097c38d`;
2. 26/26 fontes, IDs e versões confirmados;
3. 26/26 blobs canônicos confirmados no mesmo checkpoint;
4. oito Source Locks operacionais / `LEIA-PRIMEIRO` gerados;
5. `delivery/design-handoff-v5` materializada;
6. estrutura, isolamento e reproduzibilidade validados;
7. snapshot registrado em `GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001`.

O gate humano posterior foi satisfeito por `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.0.0`. O snapshot permanece congelado; a nova autoridade libera seu uso para a fase de Design sem reescrever o pacote.

## 9. Estado

```text
V5
→ EMITTED / MATERIALIZED / VALIDATED

SNAPSHOT
→ delivery/design-handoff-v5
→ commit f2e8375258fda4f37aea27a5e5ec5e83f5c1a66d
→ tree 67bacb135166e7f3e85bfb4c52602ba89a515a1e

DESIGN PRODUCTION RELEASE
→ GRANTED / GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.0.0

EXTERNAL DESIGNER PRODUCTION
→ DESIGN PRODUCTION RELEASE GRANTED
→ MANUAL FIRST-CLASS

AI
→ OPTIONAL / DESIGNER-CONTROLLED

V6 PACKAGE
→ CANDIDATE DEFINED
→ SNAPSHOT NOT EMITTED
```