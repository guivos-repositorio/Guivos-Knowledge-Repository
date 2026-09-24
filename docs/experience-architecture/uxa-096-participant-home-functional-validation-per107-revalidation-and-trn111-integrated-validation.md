---
id: UXA-096
title: Validação Funcional Corrente do Início do Participante e TRN-111
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-000
depends_on:
  - UXA-056
  - UXA-058
  - UXA-094
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-107
  - GKR-SURF-PER-108
  - GKR-TRN-110
  - GKR-TRN-111
normative: false
---

# Validação Funcional Corrente do Início do Participante e TRN-111

## 1. Finalidade

Governar `GKR-SURF-PER-108 — Início do Participante`, revalidar sua relação com `PER-107` e validar `TRN-111` ponta a ponta no limite documental.

## 2. Regra de acesso

Evento histórico não concede acesso.

Ao abrir o Início do Coletivo, a Guivos deve revalidar:

- vínculo atual;
- permissão;
- contexto selecionado;
- escopo aplicável.

Pausa, saída, remoção ou perda de permissão prevalecem sobre qualquer atualização histórica.

## 3. Identidade do vínculo

A linguagem canônica deve refletir o estado funcional real.

```text
VÍNCULO ATUAL
→ PARTICIPANTE CONFIRMADO

PAPEL
→ PARTICIPANTE
```

Termos contextuais como “membro” podem existir quando o próprio Coletivo os adotar claramente, sem substituir a semântica estrutural.

## 4. Conteúdo do Início

A superfície pode sintetizar:

- propósito do Coletivo;
- vínculo e papel atuais;
- momento coletivo aplicável;
- comunicação legítima;
- atividades;
- participação;
- controles pertinentes.

Ela não é superdashboard e não absorve todas as áreas internas.

## 5. Contestação

Contestar uma informação não significa editar silenciosamente a fonte oficial.

A experiência deve distinguir:

- corrigir dado sob autoridade da Pessoa;
- contestar informação de terceiro;
- solicitar revisão;
- retornar sem efeito.

## 6. TRN-111

```text
PER-107
→ atualização legítima com continuidade aplicável
→ revalidação de vínculo/permissão
→ PER-108
```

A transição é integralmente validada.

Abrir `PER-108` não cria novo vínculo, não confirma leitura anterior e não concede autoridade adicional.

## 7. Estado

```text
PER-107
→ CURRENT / VALIDATED

PER-108
→ FUNCTIONALLY VALIDATED

TRN-111
→ INTEGRALLY VALIDATED

IMPLEMENTATION
→ SEPARATE GATE
```
