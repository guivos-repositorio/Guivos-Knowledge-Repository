---
id: GKR-UXA-105-TRN001-SCOPE-EXAM-001
title: UXA-105 — Exame de Escopo — Continuidade Home Pública → Entrada Protegida
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: scope_exam_complete_candidate_findings
depends_on:
  - GKR-STATE-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-PER002-MASTER-001
  - UXA-020
  - UXA-023
  - UXA-035
related:
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
  - GKR-UX-PER002-MAT-ELIGIBILITY-001
  - GKR-UX-PER002-PROTOTYPE-REVALIDATION-001
  - GKR-TRN-001
---

# UXA-105 — Exame de Escopo — Continuidade Home Pública → Entrada Protegida

## 1. Finalidade

Este documento registra o exame de escopo autorizado para a UXA-105.

O exame testa se existe uma frente funcional suficientemente delimitada para tratar a lacuna remanescente de G1 em:

```text
TRN-001
→ PER-001 — HOME PÚBLICA
→ PER-002 — ENTRADA PROTEGIDA
→ CURRENT MATURITY = PARTIAL
```

Este documento **não adjudica o escopo**, não inicia exame funcional, não promove maturidade, não cria nova superfície e não libera Design ou Product Engineering.

## 2. Baseline corrente

As autoridades correntes já estabelecem:

- Home pública como superfície institucional e não personalizada;
- `Iniciar Jornada` como porta própria e persistente da Journey;
- decisão voluntária da Pessoa antes de entrar em contexto protegido;
- `PER-002` como primeira responsabilidade protegida após a Home;
- autenticação como gate/estado interno de `PER-002`, não como nova superfície;
- conclusão da autenticação diferente de conclusão de `PER-002`;
- `PER-003` como primeira superfície distinta downstream;
- ausência de coleta/processamento material de relato na Home;
- necessidade de explicação, autonomia, retorno e controles antes da continuidade protegida;
- `TRN-002` já localmente validada.

A lacuna explícita corrente do Registry permanece:

> **`TRN-001` = partial — continuidade entre pacotes.**

## 3. Pergunta do exame de escopo

> A UXA-105 deve examinar exclusivamente a continuidade funcional entre `PER-001` e `PER-002`, fechando a fronteira pública → protegida sem reabrir Home, autenticação interna, `TRN-002` ou demais transições de G1?

## 4. Evidência de necessidade

A frente é materialmente justificável porque:

1. `TRN-001` é a única transição ainda `PARTIAL` em G1;
2. todas as demais transições centrais de G1 estão pelo menos `LOCALLY VALIDATED`;
3. Home e `PER-002` possuem responsabilidades correntes suficientes para exame específico;
4. a lacuna descrita não exige nova superfície;
5. a lacuna não exige implementação técnica para ser examinada funcionalmente;
6. fechar `TRN-001` localmente não equivale a validar G1 integralmente ponta a ponta.

## 5. Escopo candidato

O escopo candidato da UXA-105 é exclusivamente:

- `TRN-001 — PER-001 → PER-002`;
- decisão consciente de iniciar a Journey a partir da Home pública;
- distinção entre explorar a Home e entrar no ambiente protegido;
- continuidade sem coleta automática de relato;
- explicação suficiente da mudança de contexto;
- preservação de autonomia, retorno, interrupção e não prosseguimento;
- distinção entre Login de relação existente e início de primeira entrada;
- tratamento de falha/indisponibilidade da entrada protegida;
- ausência de autorização material implícita;
- critérios verificáveis para eventual exame posterior de maturidade.

## 6. Fora do escopo candidato

Permanecem fora da UXA-105:

- redesign ou reabertura narrativa da Home;
- composição visual da Home;
- `PER-002 → PER-003` / `TRN-002`;
- autenticação como produto/superfície própria;
- provedores de identidade, MFA, sessão técnica ou recuperação técnica;
- `PER-003` e downstream;
- `TRN-003..017`;
- G2–G5;
- protótipo novo;
- implementação;
- Product Engineering;
- promoção automática de `TRN-001`;
- declaração de G1 integralmente validada.

## 7. Fronteira funcional candidata

```text
PER-001 — HOME PÚBLICA
→ PESSOA ESCOLHE INICIAR JORNADA
→ CONTEXTO MUDA DE PÚBLICO PARA PROTEGIDO
→ NENHUM RELATO MATERIAL É PRESUMIDO / COLETADO AUTOMATICAMENTE
→ PER-002 — ENTRADA PROTEGIDA

LOGIN DE RELAÇÃO EXISTENTE
→ ROTA DE RETOMADA
→ NÃO É O MESMO JOB DE PRIMEIRA ENTRADA

TRN-001
→ NÃO AUTORIZA PROCESSAMENTO MATERIAL
→ NÃO AUTORIZA PERSONALIZAÇÃO
→ NÃO CRIA NOVA SUPERFÍCIE
```

## 8. Critérios candidatos para o exame funcional

Um exame funcional posterior, se autorizado, deverá verificar:

1. origem e destino inequívocos;
2. ação consciente que dispara a mudança de contexto;
3. informação mínima necessária antes da entrada protegida;
4. distinção entre navegação pública e ambiente protegido;
5. distinção entre primeira entrada e retomada/login;
6. ausência de relato/processamento automático;
7. retorno e interrupção;
8. falha e indisponibilidade;
9. estado indeterminado quando a mudança de contexto não puder ser confirmada;
10. retry/reentrada sem duplicação de efeito lógico;
11. acessibilidade e linguagem;
12. preservação de `TRN-002` e das autoridades downstream.

## 9. Resultado do scope exam

A convergência analítica é:

```text
UXA-105 SCOPE EXAM
→ COMPLETE

CANDIDATE SCOPE
→ TRN-001 ONLY
→ PER-001 → PER-002
→ PUBLIC → PROTECTED CONTINUITY

SCOPE FINDINGS
→ CANDIDATE / NOT ADJUDICATED

NEW SURFACE
→ NONE REQUIRED

TRN-001
→ PARTIAL / UNCHANGED

MATURITY PROMOTIONS
→ 0

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 10. Próximo gate

```text
ADJUDICATE UXA-105 SCOPE?

IF YES
→ MATERIALIZE NORMATIVE SCOPE AUTHORITY
→ KEEP TRN-001 PARTIAL / UNCHANGED
→ NEXT SEPARATE GATE = AUTHORIZE FUNCTIONAL EXAM

IF NO
→ REOPEN SCOPE FINDINGS
```
