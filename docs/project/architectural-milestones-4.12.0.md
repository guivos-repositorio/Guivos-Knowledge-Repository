---
id: ARCHITECTURAL-MILESTONES-OVERLAY-4.12.0
title: Architectural Milestones — Estado Efetivo 4.12.0
status: active
version: 4.12.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - ARCHITECTURAL-MILESTONES-OVERLAY-4.11.0
related:
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - M5.13
---

# Architectural Milestones — Estado Efetivo 4.12.0

> O registro-base de marcos permanece preservado. Este overlay registra `M5.12`, acrescenta `M5.13` e atualiza o próximo marco candidato.

## M5.12 — Capture Context Engineering Unit Initiated

**Data:** 2026-07-19  
**Estado:** Alcançado  
**Frente:** Product Engineering

A primeira Unidade de Implementação de Capacidade foi iniciada com fontes normativas mapeadas, responsabilidade técnica, decisões proibidas, agregados candidatos, comandos, eventos, segurança, observabilidade, riscos e lacunas.

O marco representa `Normative sources mapped — 20%` e não domínio concluído.

## M5.13 — Capture Context Domain Model Proposed

**Data:** 2026-07-19  
**Estado:** Alcançado  
**Frente:** Product Engineering  
**Autoridade derivada:** PAS-001-CC-UIC-DOMAIN-001

### Critérios cumpridos

A UIC-01 atingiu:

- estado efetivo `Draft 0.2.0`;
- estado técnico `Domain model proposed`;
- progresso de referência `40%`;
- capacidade funcional preservada em `Functionally complete`.

### Evidências

- `CaptureRecord` confirmado como Aggregate Root;
- `CaptureSession` confirmada como entidade interna;
- cardinalidade registro–sessão definida;
- identidade permanente de `CaptureInput` definida;
- entidades e objetos de valor classificados;
- 31 invariantes estruturais confirmadas;
- matriz comando–agregado–invariantes–evento;
- consistência imediata e eventual delimitada;
- concorrência otimista e idempotência definidas;
- reconstrução inicial proposta;
- seis diagramas técnicos publicados;
- `UIC01-GAP-001` resolvido;
- `UIC01-GAP-002` resolvido;
- 28 testes obrigatórios de domínio registrados.

### Significado do marco

M5.13 significa que a Captura de Contexto possui modelo de domínio tecnicamente proposto e revisável. O marco não significa:

- prontidão para implementação;
- ciclo técnico integralmente definido;
- contratos técnicos completos;
- escolha tecnológica;
- autorização de produção;
- reabertura da arquitetura funcional.

## Próximo marco candidato

### M5.14 — Capture Context Technical Lifecycle Defined

Condições mínimas:

1. definir máquinas de estado independentes;
2. concluir matriz completa de transições;
3. mapear precondições e invariantes por transição;
4. definir compensações;
5. definir timeouts e expirações;
6. tratar pausas, retomadas e falhas parciais;
7. concluir testes de transição;
8. elevar UIC-01 para `Lifecycle technically defined — 60%`.

## Ponto de retomada

> Definir tecnicamente o ciclo de vida da UIC-01.
