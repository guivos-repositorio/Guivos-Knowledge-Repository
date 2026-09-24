---
id: UXA-092
title: Validação Funcional Corrente de Meus Coletivos e Continuidade Pós-Aprovação
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-000
depends_on:
  - UXA-056
  - UXA-089
  - UXA-090
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-105
  - GKR-SURF-PER-106
  - GKR-TRN-108
  - GKR-TRN-110
normative: false
---

# Validação Funcional Corrente de Meus Coletivos e Continuidade Pós-Aprovação

## 1. Finalidade

Governar `GKR-SURF-PER-106 — Meus Coletivos` e a continuidade pós-aprovação sem depender de materialização visual histórica.

A regra central é:

> **a aprovação forma o vínculo; navegar depois da aprovação é opcional e não cria o vínculo.**

## 2. Categorias distintas

A experiência não mistura:

- participação confirmada;
- acompanhamento;
- solicitação pendente;
- convite;
- pausa/saída;
- vínculo encerrado.

Essas categorias não formam ranking de dedicação ou mérito.

## 3. Resultado aprovado em PER-105

Quando uma solicitação é aprovada:

1. a decisão autorizada cria o vínculo lógico;
2. o estado aprovado passa a ser reconhecível na perspectiva da Pessoa;
3. abrir `Meus Coletivos` é continuidade opcional;
4. não abrir a superfície não desfaz a aprovação;
5. repetição do evento não duplica vínculo.

## 4. Meus Coletivos

`PER-106` permite reconhecer vínculos atuais e seus estados sem transformar a superfície em feed.

Conteúdo mínimo inclui, quando aplicável:

- Coletivo;
- estado do vínculo;
- papel;
- mudança relevante de estado;
- ações legitimamente disponíveis.

Não expor contexto protegido da Jornada pessoal por conveniência.

## 5. TRN-108

```text
COL-003
→ decisão autorizada de aprovação
→ vínculo formado
→ PER-106 disponível como continuidade opcional
```

`TRN-108` é integralmente validada no limite documental.

A transição não depende do clique de navegação para produzir o vínculo já aprovado.

## 6. Relação com PER-107

Abrir a Central de Atualizações é responsabilidade separada governada por `UXA-094` e `TRN-110`.

`PER-106` não absorve a Central.

## 7. Estado

```text
PER-105 APPROVED STATE
→ CURRENT

PER-106
→ FUNCTIONALLY VALIDATED

TRN-108
→ INTEGRALLY VALIDATED

VISUAL BASELINE
→ NONE REQUIRED
```
