---
id: GEM-008-SUSTAINABILITY-DIMENSION-TAXONOMY-001
title: Taxonomia das Dimensões de Sustentabilidade
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-22
parent: GEM-008
---

# Taxonomia das Dimensões de Sustentabilidade

## 1. Objetivo

Classificar as dimensões que deverão ser observadas para avaliar a continuidade responsável de produtos, fluxos, programas, capacidades e do ecossistema.

## 2. Dimensões

| Código | Dimensão | Pergunta principal |
|---|---|---|
| SD-01 | valor | o benefício continua real e compatível com o propósito? |
| SD-02 | econômica | fontes, custos, riscos e obrigações são coerentes? |
| SD-03 | financeira | liquidez, compromissos e reservas poderão ser protegidos? |
| SD-04 | operacional | existe capacidade para entregar, suportar e corrigir? |
| SD-05 | tecnológica | infraestrutura, segurança e substituição são adequadas? |
| SD-06 | qualidade e confiança | curadoria, suporte, privacidade e contestação são preservados? |
| SD-07 | parceiros | dependência, qualidade e continuidade da rede são tratadas? |
| SD-08 | gratuito | o baseline universal possui fonte compatível e resiliente? |
| SD-09 | social e ambiental | externalidades são identificadas e reduzidas? |
| SD-10 | governança | autoridade, evidência, revisão e interrupção estão definidas? |

## 3. Estados

```yaml
sustainability_status:
  not_assessed |
  conceptually_supported |
  evidence_required |
  capacity_constrained |
  economically_fragile |
  dependency_exposed |
  remediation_required |
  at_risk |
  unsustainable |
  blocked
```

## 4. Regras de classificação

- uma dimensão favorável não compensa falha grave em outra;
- receita elevada não compensa risco material de segurança ou privacidade;
- atividade e engajamento não comprovam sustentabilidade;
- ausência de dados mantém `not_assessed` ou `evidence_required`;
- `conceptually_supported` não significa validação financeira;
- `blocked` deverá ser usado quando expansão ampliar dano, obrigação não coberta ou fragilidade crítica;
- avaliações deverão indicar escopo, owner, evidência e data.

## 5. Níveis de escopo

- ecossistema;
- produto;
- fluxo de valor;
- programa;
- capacidade compartilhada;
- relacionamento de parceiro;
- território;
- iniciativa social.

## 6. Dependência de métricas

O GEM-009 deverá transformar as dimensões em indicadores observáveis, sem alterar os guardrails ou inferir valores inexistentes.

## 7. Fora do escopo

- score numérico;
- pesos;
- thresholds;
- classificação real de produtos;
- auditoria financeira;
- operação.