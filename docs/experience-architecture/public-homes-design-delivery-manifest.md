---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 5.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: design_delivery_v5_prepared_snapshot_pending
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este Manifesto define o pacote externo v5 que será entregue à frente de Design depois da integração e validação desta remediação.

O snapshot v4 permanece histórico e reproduzível, mas não é pacote atual porque seu checkpoint foi superado.

## 2. Princípio do v5

O v5 elimina GENINPUTs operacionais de checkpoints superados do pacote de produção. Em seu lugar, cada Home recebe um `LEIA-PRIMEIRO / SOURCE LOCK OPERACIONAL` gerado no momento da emissão a partir das autoridades pós-auditoria.

A ausência de identidade visual canônica não é lacuna: estética e sistema visual são responsabilidade criativa da designer.

## 3. Composição canônica — 25 fontes únicas

### 3.1 Fontes comuns

1. `docs/experience-architecture/public-homes-design-handoff.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.5.0`;
2. `docs/experience-architecture/public-homes-generative-source-lock-and-prompt-template.md` — `GKR-UX-HOMES-GENINPUT-001 v2.0.0`;
3. `docs/experience-architecture/public-homes-design-production-readiness-and-figma-contract.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.0.0`.

### 3.2 Pessoa
4. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001 v1.0.2`;
5. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### 3.3 Organizações e Coletivos
6. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001 v1.0.0`;
7. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### 3.4 Mall
8. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.0.0`;
9. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`;
### 3.5 Travel
10. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001 v1.0.0`;
11. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

### 3.6 Media
12. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.0`;
13. `docs/product-architecture/media.md` — `GPA-005 v1.2.0`.

### 3.7 Ads
14. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001 v1.0.0`;
15. `docs/product-architecture/ads.md` — `GPA-007 v1.3.0`.

### 3.8 Business
16. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.0.0`;
17. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001 v1.0.0`;
18. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
19. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
20. `docs/product-architecture/business.md` — `GPA-004 v1.6.0`.

### 3.9 Intelligence
21. `docs/experience-architecture/public-home-intelligence-design-handoff.md` — `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
22. `docs/experience-architecture/public-home-intelligence-source-lock.md` — `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
23. `docs/experience-architecture/public-home-intelligence-master-document.md` — `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.1.1`;
24. `docs/product-architecture/intelligence-product-source-lock.md` — `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
25. `docs/product-architecture/intelligence.md` — `GPA-006 v2.0.0`.

## 4. Oito guias operacionais

A emissão v5 deve gerar oito arquivos adicionais `00-LEIA-PRIMEIRO.md`, um por Home. Cada guia funciona como Source Lock operacional daquele snapshot e deve conter:

- Home e objetivo;
- commit canônico de origem;
- lista exata de fontes e SHAs;
- ordem de leitura;
- invariantes específicos;
- liberdades criativas;
- classes de conteúdo;
- proibições de inferência;
- prompt inicial para Figma Make;
- estado inicial `EXPLORAÇÃO / NÃO CANÔNICA`;
- checklist de autoauditoria.

## 5. Estrutura externa

`GUIVOS-HOMES-DESIGN-HANDOFF-v5/` deve conter `00-COMUM` e oito diretórios isolados: Pessoa, Organizações-e-Coletivos, Mall, Travel, Media, Ads, Business e Intelligence.

Os 25 arquivos canônicos devem reutilizar os blobs do mesmo checkpoint pós-merge. Os oito guias podem ser materializados especificamente para a emissão.

Contagem planejada: `25 FONTES CANÔNICAS + 8 GUIAS = 33 ARQUIVOS EXTERNOS`.

## 6. Regra para ferramentas generativas

Não carregar documentos específicos de múltiplas Homes na mesma execução. A identidade visual é livre; fatos e arquitetura não são.

## 7. Materiais fora do pacote inicial

- snapshots v1-v4;
- GENINPUTs históricos de checkpoint;
- benchmarks;
- rascunhos de conversa;
- documentação de Engenharia;
- pricing não formalizado;
- assets ou brand book visual inexistentes como suposta obrigação.

Referências adicionais entram somente para resolver dúvida concreta.

## 8. Gate de emissão

Somente após merge deste changeset:

1. capturar `main` pós-merge;
2. confirmar 25/25 fontes e versões;
3. confirmar que todos os blobs pertencem ao mesmo checkpoint;
4. gerar oito Source Locks operacionais;
5. materializar branch/snapshot v5;
6. validar estrutura, isolamento e reproduzibilidade;
7. registrar snapshot em autoridade própria;
8. somente então avaliar Design Production Release.

## 9. Estado

`V5 PREPARED / SNAPSHOT PENDING / DESIGN PRODUCTION RELEASE NOT_GRANTED`.
