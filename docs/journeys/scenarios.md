---
id: GKR-JOURNEY-SCENARIOS-001
title: Cenários Integrados de Jornada
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
related:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-D5-C4B-001
normative: false
---

# Cenários Integrados de Jornada

## 1. Finalidade

Esta vista resume cenários correntes de continuidade entre participantes, superfícies e fronteiras.

Ela não reconstrói a cronologia das UXAs, não substitui os registries e não converte validação documental em implementação técnica.

```text
SCENARIO VIEW
→ CURRENT SYNTHESIS

SURFACE REGISTRY
→ CURRENT STATES / RESPONSIBILITIES

TRANSITION REGISTRY
→ CURRENT TRANSITION MATURITY

HISTORICAL UXA SEQUENCE
→ GIT / PROVENANCE
```

## 2. Pessoa — entrada, compreensão e Hoje

A continuidade corrente é:

```text
HOME PÚBLICA
→ ENTRADA PROTEGIDA
→ EXPRESSÃO GUIADA
→ COMPREENSÃO INICIAL
→ HOJE
```

As transições iniciais anteriores a `PER-007` preservam a maturidade declarada no Transition Registry e não devem ser promovidas por inferência.

A passagem:

```text
PER-007 — COMPREENSÃO INICIAL
→ GKR-TRN-007
→ PER-008 — HOJE
```

está **integralmente validada no limite documental**.

Entrar em Hoje não cria avanço humano, prioridade, personalização, consentimento ou Próximo Passo por si só.

## 3. Pessoa — direção, movimento e evolução

No estado recorrente de Hoje:

```text
PER-008 — HOJE
├── GKR-TRN-008 / 009 ↔ PER-010 — MEUS OBJETIVOS
├── GKR-TRN-010 / 011 ↔ PER-011 — MEUS PRÓXIMOS PASSOS
└── GKR-TRN-012 / 013 ↔ PER-012 — MINHA EVOLUÇÃO
```

`GKR-TRN-008..013` estão integralmente validadas no limite documental.

Abrir ou retornar dessas responsabilidades não cria, confirma, conclui ou altera automaticamente objetivo, passo, prioridade ou evolução.

## 4. Pessoa e Coletivo — descoberta, solicitação e participação

A continuidade governada inclui:

```text
DESCOBERTA
→ PERFIL PÚBLICO
→ REVISÃO
→ SOLICITAÇÃO
→ ANÁLISE DO RESPONSÁVEL
→ RESULTADO
→ MEUS COLETIVOS
→ ATUALIZAÇÕES
→ INÍCIO DO PARTICIPANTE
```

Estado corrente relevante:

- `GKR-TRN-104` permanece parcial;
- `GKR-TRN-105..112` estão integralmente validadas conforme o Transition Registry.

Aprovação, vínculo, leitura, presença e autoridade permanecem conceitos separados. Histórico não preserva acesso quando vínculo ou permissão deixam de ser válidos.

## 5. Organização → oportunidade → descoberta → detalhe

A continuidade corrente é:

```text
ORG-003 — CADASTRO / PUBLICAÇÃO
→ GKR-TRN-203
→ PER-201 — MAPA
↔ GKR-TRN-210
→ PER-202 — LISTA

PER-201
→ GKR-TRN-204
→ PER-203 — DETALHE

PER-202
→ GKR-TRN-211
→ PER-203 — DETALHE
```

`GKR-TRN-203`, `204`, `210` e `211` estão **integralmente validadas**.

Ativação gera elegibilidade à descoberta; não garante distribuição, alcance, posição, recomendação ou resultado.

Mapa e Lista representam a mesma consulta funcional, preservando contexto aplicável.

## 6. Detalhe → fronteira externa

A saída consciente é:

```text
PER-203 — DETALHE
→ REVISÃO CONSCIENTE
→ GKR-TRN-205
→ BND-001 — FRONTEIRA EXTERNA
→ PROCESSO DO TERCEIRO
```

`GKR-TRN-205` está **integralmente validada até a fronteira de autoridade da Guivos**.

A Guivos governa:

- informação suficiente antes da saída;
- identificação de destino e responsável;
- minimização de dados;
- revalidação de estado;
- cancelamento;
- retorno;
- idempotência no limite sob sua autoridade.

O processo e o resultado posteriores pertencem ao terceiro e não são validados pela Guivos.

## 7. Organização ↔ Coletivo

O contrato bilateral existe, mas as transições `GKR-TRN-206..209` preservam a maturidade registrada no Transition Registry.

As superfícies bilaterais e a operação ponta a ponta não devem ser presumidas como completas apenas porque os atores e contratos funcionais existem.

## 8. Opportunity Boost e camada comercial

Os estados residuais do Opportunity Boost possuem validação funcional corrente.

Isso não fecha automaticamente a integração orgânico–patrocinado.

Estado corrente:

```text
GKR-TRN-304
→ PARTIAL

GKR-TRN-305
→ PARTIAL

GKR-TRN-306
→ PARTIAL
```

Pagamento, patrocínio ou inventário comercial não alteram relevância orgânica, autoridade da Pessoa ou maturidade funcional das transições acima.

## 9. Planos e contratação

Pessoa, Coletivo e Organização possuem jornadas e superfícies de Planos próprias.

Guivos Business permanece produto especializado separado, com contratação online e modelo de composição Self-service quando elegível.

Abrir Planos ou um configurador:

- não inicia cobrança;
- não seleciona plano automaticamente;
- não altera consentimento;
- não altera relevância;
- não concede capacidade antes da contratação válida.

## 10. Critério de completude

Um cenário somente é considerado integralmente fechado quando suas transições, estados, autoridades, retornos, interrupções e fronteiras aplicáveis estiverem cobertos por autoridade corrente.

```text
LOCAL VALIDATION
≠ END-TO-END IMPLEMENTATION

DOCUMENTARY VALIDATION
≠ TECHNICAL IMPLEMENTATION

CURRENT SCENARIO
→ USE REGISTRIES AS MATURITY AUTHORITY
```

## 11. Estado

```text
SCENARIOS
→ CURRENT

HISTORICAL UXA NARRATIVE
→ REMOVED FROM CURRENT SYNTHESIS

IMPLEMENTATION
→ NOT INFERRED

PRODUCT ENGINEERING
→ SEPARATE / NOT RELEASED
```
