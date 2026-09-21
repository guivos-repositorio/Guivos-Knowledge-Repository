---
id: UXA-098
title: Validação Integrada Corrente da Publicação à Descoberta e Detalhe
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-000
depends_on:
  - UXA-004
  - UXA-012
  - UXA-013
  - UXA-025
  - UXA-028
  - UXA-029
  - UXA-038
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-ORG-003
  - GKR-SURF-PER-201
  - GKR-SURF-PER-202
  - GKR-SURF-PER-203
  - GKR-TRN-203
  - GKR-TRN-204
  - GKR-TRN-210
  - GKR-TRN-211
normative: false
---

# Validação Integrada Corrente da Publicação à Descoberta e Detalhe

## 1. Finalidade

Validar como conjunto a continuidade:

```text
ORG-003
→ TRN-203
→ PER-201 MAPA
↔ TRN-210
→ PER-202 LISTA

PER-201
→ TRN-204
→ PER-203 DETALHE

PER-202
→ TRN-211
→ PER-203 DETALHE
```

A validação é documental e não comprova algoritmo, distribuição real, tecnologia cartográfica ou implementação.

## 2. Contrato da oportunidade

A mesma oportunidade lógica deve preservar identidade e condições relevantes entre publicação, descoberta e detalhe.

Ativação:

- torna a oportunidade elegível à descoberta;
- não garante distribuição;
- não garante posição;
- não garante relevância pessoal;
- não cria resultado para a Pessoa.

## 3. TRN-203 — publicação → descoberta

Uma oportunidade ativa pode tornar-se elegível a superfícies de descoberta quando os gates aplicáveis estiverem atendidos.

A transição não garante que ela será apresentada a qualquer Pessoa específica.

## 4. Mapa e Lista

Mapa e Lista representam a mesma consulta territorial.

`TRN-210` preserva, quando aplicável:

- região;
- busca;
- filtros;
- seleção;
- identidade das oportunidades;
- contexto de retorno.

Alternar modo não cria uma nova consulta silenciosa.

## 5. Mapa/Lista → Detalhe

`TRN-204` e `TRN-211` preservam a identidade da oportunidade e permitem retorno coerente ao contexto de descoberta.

Abrir Detalhe não confirma interesse, inscrição, compra ou evolução.

## 6. Orgânico e patrocinado

Inventário patrocinado deve permanecer identificado.

Pagamento:

- não altera relevância funcional;
- não compra confiança;
- não muda qualidade;
- não transforma publicidade em recomendação;
- não substitui silenciosamente resultado orgânico.

## 7. Concorrência

Se a oportunidade for alterada, pausada, encerrada ou ficar inelegível durante a navegação, o destino deve revalidar o estado corrente antes de permitir ação material.

## 8. Resultado nas transições

```text
TRN-203
→ INTEGRALLY VALIDATED

TRN-204
→ INTEGRALLY VALIDATED

TRN-210
→ INTEGRALLY VALIDATED

TRN-211
→ INTEGRALLY VALIDATED
```

A validação permanece restrita ao limite documental.

## 9. Limites

Este contrato não:

- define algoritmo de distribuição;
- define tecnologia de mapa;
- cria campanha publicitária;
- implementa cobrança;
- valida saída externa posterior ao Detalhe;
- promove Engenharia de Produto.

A saída consciente do Detalhe para autoridade externa é governada por `UXA-101`.

## 10. Estado

```text
PUBLICATION → DISCOVERY → DETAIL
→ CURRENT / INTEGRATED

VISUAL BASELINE
→ NONE REQUIRED

IMPLEMENTATION
→ SEPARATE GATE
```
