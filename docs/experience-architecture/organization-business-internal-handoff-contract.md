---
id: GKR-UX-ORGANIZATION-BUSINESS-HANDOFF-CONTRACT-001
title: Organização → Guivos Business — Contrato Canônico de Handoff
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: contracted_internal_handoff
depends_on:
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
  - GPA-SPECIALIZED-JOURNEY-MATRIX-001
  - GPA-004
  - GKR-JOURNEY-BUSINESS-001
related:
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# Organização → Guivos Business — Contrato Canônico de Handoff

## 1. Finalidade

Fechar semanticamente `SP-GAP-004` sem confundir Organização com Guivos Business e sem criar superfície ou transição granular por inferência.

## 2. Separação estrutural

```text
ORGANIZAÇÃO
→ PARTICIPANTE ESTRUTURAL

GUIVOS BUSINESS
→ PRODUTO ESPECIALIZADO B2B

ORGANIZAÇÃO
≠ GUIVOS BUSINESS

PLANO DE ORGANIZAÇÃO
≠ PLANO BUSINESS
```

Uma Organização pode existir e operar no ecossistema sem contratar Guivos Business.

## 3. Quando o handoff existe

O handoff ocorre somente quando há **contexto B2B próprio e relação de produto identificável**, com mudança explícita da responsabilidade dominante para Guivos Business.

Exemplos de contextos materiais:

- contratação de Programas de Incentivo;
- contratação de Journey custeado pela empresa;
- contratação de ambas as ofertas;
- configuração de capacidade, escala, Intelligence, integração, governança ou serviço sob contrato Business.

Não constituem handoff por si só:

- possuir perfil de Organização;
- publicar oportunidade;
- operar superfícies `ORG-*`;
- possuir plano `Conecta`, `Eleva` ou `Transforma`;
- atravessar `BND-002`;
- aparecer em contexto institucional comum.

## 4. Contrato mínimo

| Campo | Contrato |
|---|---|
| origem | jornada institucional da Organização ou outra superfície Guivos legitimamente autorizada |
| destino | Guivos Business, quando uma relação B2B própria passa a governar a decisão dominante |
| trigger | ação afirmativa e consciente para conhecer, configurar, contratar ou operar oferta Business própria |
| identidade | preservar a mesma Organização/empresa quando aplicável, sem criar novo tipo estrutural de participante |
| contexto | somente o contexto institucional necessário para a finalidade Business |
| dados | somente dados necessários, autorizados e compatíveis com o contrato/finalidade B2B |
| autoridade | a jornada de Organização preserva autoridade institucional; Business governa a relação B2B especializada |
| consequência | entrada no contexto Business próprio; nenhum plano, contrato, pagamento ou entitlement é presumido por este handoff |
| retorno | retorno neutro ao contexto institucional de origem quando materializado, sem apagar contrato ou efeito legitimamente confirmado |
| recuperação | falha/indisponibilidade não cria contratação; repetição não duplica efeito material quando houver implementação |
| transparência | a mudança para contexto Business deve ser perceptível antes de qualquer consequência comercial |
| maturidade | contratado; não materializado como `SURF/TRN` dedicado |

## 5. BND-002

`BND-002` não substitui este handoff.

```text
BND-002
→ DIMENSIONAMENTO / CONTRATAÇÃO ASSISTIDA GENÉRICA
→ NÃO É BUSINESS
→ NÃO PROVA ENTRADA EM BUSINESS
```

Se uma experiência Business futura utilizar `BND-002`, isso dependerá de contrato específico de contexto; a fronteira genérica não transforma o processo posterior em Business automaticamente.

## 6. Planos

```text
ORGANIZAÇÃO
→ Conecta · Eleva · Transforma

BUSINESS
→ Start · Growth · Scale · Enterprise

EQUAL OR SIMILAR PRICING
≠ FUNCTIONAL EQUIVALENCE
```

## 7. Relação com Journey

Business pode custear acesso ao Guivos Journey, mas isso não transfere controle sobre a Journey individual.

```text
EMPRESA PAGA O ACESSO
≠ EMPRESA CONTROLA A JOURNEY
```

Journey preserva trajetória, pertinência, escolhas, próximos passos e contexto individual dentro de suas autoridades.

## 8. Não inferências

```text
ORGANIZATION PROFILE
≠ BUSINESS CUSTOMER

ORG-*
≠ BUSINESS SURFACE

BND-002
≠ BUSINESS HANDOFF

BUSINESS HANDOFF CONTRACT
≠ NEW SURFACE
≠ NEW TRN-ID
≠ CONTRACT SIGNED
≠ PAYMENT
≠ ENTITLEMENT
≠ IMPLEMENTATION
```

## 9. Materialização futura

Nova superfície ou transição dedicada somente deverá existir se uma necessidade real de navegação, autoridade, consequência, recuperação ou dados exigir materialização própria.

Até esse momento:

```text
SP-GAP-004
→ SEMANTIC CONTRACT CLOSED

DEDICATED SURF/TRN
→ NOT CREATED
```

## 10. Estado

```text
ORGANIZATION → GUIVOS BUSINESS
→ CONTRACTED INTERNAL HANDOFF

NEW SURFACES
→ 0

NEW TRANSITIONS
→ 0

PRODUCT ENGINEERING
→ NOT RELEASED
```
