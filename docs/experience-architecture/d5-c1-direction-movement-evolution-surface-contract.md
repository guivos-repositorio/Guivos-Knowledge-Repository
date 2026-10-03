---
id: GKR-UX-D5-C1-001
title: Direção, Movimento e Evolução — Contrato Funcional Corrente
status: active
version: 2.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-20
parent: UXA-000
normative: false
related:
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - PAS-001-EC-VIEW-001
  - PAS-001-DOMAIN-MODEL-001
  - PAS-001-DOMAIN-RECON-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-D5-C4B-001
---

# Direção, Movimento e Evolução — Contrato Funcional Corrente

## 1. Finalidade

Esta autoridade reúne o contrato corrente das três responsabilidades especializadas da Jornada da Pessoa:

- `GKR-SURF-PER-010 — Meus Objetivos`;
- `GKR-SURF-PER-011 — Meus Próximos Passos`;
- `GKR-SURF-PER-012 — Minha Evolução`.

Ela governa significado, fronteiras, entradas, retornos, autonomia, privacidade e relação com os Domínios de Evolução. Não governa layout, UI, implementação ou identidade visual.

## 2. Autoridade e precedência

A semântica funcional permanece governada por:

- `PAS-001-OBJ-VIEW-001` para Objetivos;
- `PAS-001-PP-VIEW-001` para Próximos Passos;
- `PAS-001-EC-VIEW-001` para Evolução Contínua;
- `PAS-001-DOMAIN-MODEL-001` e `PAS-001-DOMAIN-RECON-001` para Domínios de Evolução.

Este documento traduz essas autoridades para a Experience Architecture.

## 3. Responsabilidades

| ID | Responsabilidade | Papel |
|---|---|---|
| `GKR-SURF-PER-010` | Meus Objetivos | compreender, organizar e controlar direções e objetivos |
| `GKR-SURF-PER-011` | Meus Próximos Passos | compreender, organizar e controlar movimentos contextuais |
| `GKR-SURF-PER-012` | Minha Evolução | compreender e controlar trajetórias, mudanças, continuidades, evidências e interpretações |

`PER-008 — Hoje` permanece síntese recorrente e porta de aprofundamento. Ele não absorve as três responsabilidades especializadas.

## 4. Domínios de Evolução

Objetivos, Próximos Passos e trajetórias de Evolução podem possuir `0..n domain_link`.

Em todos os casos:

```text
DOMÍNIO
≠ prioridade
≠ diagnóstico
≠ mérito
≠ obrigação
≠ prontidão
≠ prova de evolução
≠ recomendação comercial
```

Para Evolução, devem permanecer distintos:

```text
DOMÍNIO DE EVOLUÇÃO
→ sobre o que a trajetória trata

TRAJETÓRIA
→ unidade temporal/contextual acompanhada

ASPECTO DESCRITIVO
→ natureza complementar da mudança

DIMENSÃO DO CONTEXTO VIVO
→ eixo estrutural contextual relacionado
```

## 5. Entradas e retornos

```text
PER-008
→ TRN-008
→ PER-010
→ TRN-009
→ PER-008

PER-008
→ TRN-010
→ PER-011
→ TRN-011
→ PER-008

PER-008
→ TRN-012
→ PER-012
→ TRN-013
→ PER-008
```

Abrir uma responsabilidade especializada não cria, confirma ou altera automaticamente o objeto funcional correspondente.

Retornar a Hoje:

- não altera Objetivo;
- não confirma sugestão;
- não inicia ou conclui Próximo Passo;
- não reconhece evolução;
- não modifica prioridade;
- não concede nova autorização.

## 6. Sem handoffs diretos presumidos

O modelo corrente não cria automaticamente:

```text
PER-010 ↔ PER-011
PER-011 ↔ PER-012
PER-010 ↔ PER-012
```

Relação semântica entre capacidades não equivale a necessidade de navegação direta.

## 7. Privacidade, autonomia e sensibilidade

As três responsabilidades podem conter informação sensível. A experiência deve preservar:

- minimização;
- autenticação proporcional;
- ocultação de conteúdo sensível quando necessário;
- controle de compartilhamento;
- distinção entre declarado, observado, inferido e confirmado;
- correção, contestação e retirada;
- retorno seguro;
- ausência de publicidade contextual baseada em vulnerabilidade.

`domain_link` sensível não é autorização para tratamento adicional.

## 8. Estado corrente

As responsabilidades estão registradas nos Surface Registries e os seis handoffs mínimos estão **integralmente validados no limite documental** por `GKR-UX-D5-C4B-001`.

```text
PER-010 / PER-011 / PER-012
→ CURRENT FUNCTIONAL RESPONSIBILITIES

TRN-008..013
→ INTEGRALLY VALIDATED / DOCUMENTARY BOUNDARY

IMPLEMENTATION
→ NOT INFERRED
```
