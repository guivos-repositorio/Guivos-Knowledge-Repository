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
  - PAS-001-ENGINEERING-HANDOFF-001
  - M5.12
---

# Architectural Milestones — Estado Efetivo 4.12.0

> O registro-base de marcos permanece preservado. Este overlay acrescenta `M5.12` e atualiza o próximo marco candidato.

## M5.12 — Capture Context Engineering Unit Defined

**Data:** 2026-07-19  
**Estado:** Alcançado  
**Frente:** Product Engineering  
**Autoridade derivada:** PAS-001-ENGINEERING-HANDOFF-001

### Critério cumprido

A primeira Unidade de Implementação de Capacidade foi definida e registrada como:

- `PAS-001-CC-UIC-001`;
- versão `Draft 0.1.0`;
- estado técnico `Normative sources mapped`;
- capacidade funcional preservada em `Functionally complete`.

### Evidências

- autoridades normativas mapeadas;
- responsabilidade e limites definidos;
- decisões proibidas explicitadas;
- agregados candidatos registrados;
- 24 invariantes iniciais;
- estados e regras de transição preservados;
- comandos e eventos candidatos;
- produtores e consumidores delimitados;
- classificação de persistência, busca, projeções e grafo;
- requisitos de identidade, segurança, privacidade e Intelligence;
- observabilidade e testes definidos em nível inicial;
- dependências da Onda 0;
- 12 riscos e 10 lacunas.

### Significado do marco

M5.12 significa que a Captura de Contexto possui uma unidade técnica normativa inicial. O marco não significa:

- prontidão para implementação;
- escolha tecnológica;
- fechamento do domínio;
- autorização de produção;
- reabertura da arquitetura funcional.

## Próximo marco candidato

### M5.13 — Capture Context Domain Model Proposed

Condições mínimas:

1. confirmar limites entre CaptureRecord e CaptureSession;
2. definir identidade técnica de CaptureInput;
3. classificar entidades e objetos de valor;
4. formalizar invariantes por comando;
5. definir consistência e concorrência;
6. propor estratégia de reconstrução;
7. elevar UIC-01 para `Domain model proposed`.

## Ponto de retomada

> Aprofundar agregados, identidades e invariantes da Captura de Contexto.
