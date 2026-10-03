---
id: GKR-UXA-104-PER013014-FUNCTIONAL-EXAM-001
title: UXA-104 — Exame Funcional — Continuidade de Arquivo e Perguntas Opcionais
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: functional_exam_complete_candidate_findings
depends_on:
  - UXA-104
  - GKR-UXA-104-PER013014-SCOPE-AUTHORITY-001
  - GKR-UX-PER013-MASTER-001
  - GKR-UX-PER014-MASTER-001
  - GKR-UX-PER003-MASTER-001
  - GKR-UX-PER005-MASTER-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
related:
  - GKR-UX-G1-ENTRY-EXPRESSION-INVENTORY-VALIDATION-001
  - GKR-STATE-001
---

# UXA-104 — Exame Funcional — Continuidade de Arquivo e Perguntas Opcionais

## 1. Finalidade

Este documento registra o exame funcional autorizado da UXA-104 dentro do escopo normativamente adjudicado.

O exame cobre exclusivamente:

- `PER-003 → PER-013 → PER-005` para Arquivo;
- `PER-003 → PER-014 → PER-005` para Perguntas Opcionais;
- `TRN-014..017`;
- revisão consciente;
- remoção, substituição e retorno quando aplicáveis;
- voluntariedade;
- ausência de autorização material implícita;
- critérios verificáveis para eventual exame posterior de maturidade.

Este documento registra **achados candidatos**. Ele não adjudica contrato funcional, não promove maturidade e não libera implementação.

## 2. Pergunta do exame

A pergunta central é:

> As autoridades correntes já definem, com suficiência funcional local, a continuidade de Arquivo e Perguntas Opcionais desde a escolha consciente em `PER-003` até o inventário/autorização em `PER-005`, sem criar processamento ou autorização implícita?

## 3. Resultado sintético

A convergência analítica é:

```text
PER-013
→ FUNCTIONALLY SUFFICIENT CANDIDATE

PER-014
→ FUNCTIONALLY SUFFICIENT CANDIDATE

TRN-014..017
→ FUNCTIONALLY EXAMINED
→ CONTRACTED / UNCHANGED

NEW FUNCTIONAL RULE REQUIRED
→ NONE IDENTIFIED

MATURITY PROMOTIONS
→ 0
```

A lacuna corrente deixa de ser descoberta de regra funcional ausente e passa a ser adjudicação/materialização das responsabilidades candidatas e, somente depois, eventual exame separado de maturidade.

## 4. Exame de PER-013 — Arquivo

### 4.1 Entrada consciente

**Suficiência candidata: SIM.**

A autoridade atual fecha que:

- Arquivo é escolhido conscientemente em `PER-003`;
- escolher Arquivo não abre seletor automaticamente;
- abrir seletor não equivale a upload;
- upload não equivale a autorização material;
- voltar ou interromper permanece possível;
- outra modalidade não herda permissões automaticamente.

### 4.2 Finalidade antes da captura

**Suficiência candidata: SIM.**

Antes da captura material, a Pessoa deve compreender finalidade, ação necessária, proteção de terceiros, limites de disponibilidade técnica e distinção entre origem e extração.

Não há necessidade de inventar formatos, tamanhos ou limites sem autoridade técnica.

### 4.3 Revisão, remoção e substituição

**Suficiência candidata: SIM.**

O contrato já exige:

- reconhecimento da fonte;
- distinção entre origem, metadado necessário, extração e derivação;
- remoção;
- substituição;
- nova revisão após substituição;
- consequência compreensível;
- impossibilidade de manter silenciosamente derivado sem fundamento quando a fonte é removida.

### 4.4 Falha e recuperação

**Suficiência candidata: SIM NO LIMITE FUNCIONAL.**

Estão cobertos:

- falha de seleção;
- falha de upload;
- interrupção;
- perda de conexão;
- duplicação acidental;
- falha de remover/substituir;
- estado indeterminado;
- retry sem duplicação silenciosa.

O mecanismo técnico de idempotência permanece fora do escopo, corretamente.

### 4.5 Handoff para PER-005

**Suficiência candidata: SIM.**

`TRN-015` entrega somente conteúdo revisado e representações legitimamente produzidas, preservando:

- origem;
- identificação da fonte;
- distinção origem/derivado;
- remoções/limitações;
- contexto necessário;
- ausência de autorização material.

`PER-005` permanece responsável por inventário compreensível e autorização específica.

## 5. Exame de PER-014 — Perguntas Opcionais

### 5.1 Voluntariedade

**Suficiência candidata: SIM.**

A autoridade atual diferencia corretamente:

```text
ESCOLHER
≠ RESPONDER

PULAR
≠ RECUSAR A JORNADA

NÃO SEI
≠ INSUFICIÊNCIA

PREFIRO NÃO INFORMAR
≠ ERRO

AUSÊNCIA
≠ DADO A INFERIR
```

### 5.2 Finalidade e minimização

**Suficiência candidata: SIM.**

Cada pergunta exige finalidade compreensível e proporcional. O contrato proíbe cadastro obrigatório disfarçado, curiosidade analítica sem necessidade e coleta sensível apenas por conveniência.

### 5.3 Revisão e correção

**Suficiência candidata: SIM.**

A Pessoa pode:

- revisar;
- corrigir;
- remover;
- pular;
- manter em aberto;
- interromper;
- retomar quando houver suporte legítimo.

Ausência de resposta não pode ser convertida em avaliação negativa.

### 5.4 Falha e retomada

**Suficiência candidata: SIM NO LIMITE FUNCIONAL.**

Falha de carregar, registrar, corrigir, remover, perda de conexão e estado indeterminado estão cobertos.

Retomada não pode inventar resposta, restaurar conteúdo removido ou alterar `não sei`/`prefiro não informar`.

### 5.5 Handoff para PER-005

**Suficiência candidata: SIM.**

`TRN-017` entrega somente o conjunto revisado, preservando proveniência, pulos/aberturas relevantes, remoções e ausência de autorização material.

## 6. Exame de TRN-014

`TRN-014 — PER-003 → PER-013`

| Dimensão | Resultado candidato |
|---|---|
| origem | suficiente |
| destino | suficiente |
| ação consciente | suficiente |
| efeito | suficiente |
| dados/contexto | suficiente |
| autorização material | explicitamente ausente |
| retorno/interrupção | suficiente |
| falha | suficiente |
| idempotência funcional | suficiente no limite documental |

Conclusão:

```text
TRN-014
→ FUNCTIONALLY SUFFICIENT CANDIDATE
→ MATURITY UNCHANGED
→ CONTRACTED
```

## 7. Exame de TRN-015

`TRN-015 — PER-013 → PER-005`

| Dimensão | Resultado candidato |
|---|---|
| conteúdo revisado | suficiente |
| proveniência | suficiente |
| origem × derivado | suficiente |
| remoções/substituições | suficiente |
| autorização material | preservada para PER-005 |
| retorno/interrupção | suficiente |
| falha/estado indeterminado | suficiente no limite funcional |
| duplicação silenciosa | proibida funcionalmente |

Conclusão:

```text
TRN-015
→ FUNCTIONALLY SUFFICIENT CANDIDATE
→ MATURITY UNCHANGED
→ CONTRACTED
```

## 8. Exame de TRN-016

`TRN-016 — PER-003 → PER-014`

| Dimensão | Resultado candidato |
|---|---|
| escolha consciente | suficiente |
| opcionalidade | suficiente |
| respostas automáticas | proibidas |
| consentimento presumido | proibido |
| outras modalidades | preservadas |
| retorno/interrupção | suficiente |
| falha | suficiente |

Conclusão:

```text
TRN-016
→ FUNCTIONALLY SUFFICIENT CANDIDATE
→ MATURITY UNCHANGED
→ CONTRACTED
```

## 9. Exame de TRN-017

`TRN-017 — PER-014 → PER-005`

| Dimensão | Resultado candidato |
|---|---|
| respostas revisadas | suficiente |
| proveniência | suficiente |
| pulos/aberturas | preserváveis quando material |
| remoções | suficiente |
| ausência × inferência | distinguida |
| autorização material | preservada para PER-005 |
| falha/retomada | suficiente |
| duplicação silenciosa | não suportada |

Conclusão:

```text
TRN-017
→ FUNCTIONALLY SUFFICIENT CANDIDATE
→ MATURITY UNCHANGED
→ CONTRACTED
```

## 10. Compatibilidade com G1

O exame não altera:

- `TRN-001` como `partial`;
- `TRN-003/004/005` como `locally validated`;
- G2–G5;
- `PER-004`, `PER-005` ou `PER-006`;
- Product Engineering.

A cadeia G1 completa continua **não integralmente validada**.

## 11. Lacunas que permanecem legitimamente fora

Não são lacunas funcionais impeditivas deste exame:

### Arquivo

- formatos reais;
- tamanho/quantidade;
- storage;
- retenção;
- malware scanning;
- OCR/parser;
- criptografia;
- infraestrutura.

### Perguntas

- catálogo concreto;
- árvore concreta;
- quantidade de perguntas;
- regras técnicas de adaptação;
- persistência;
- sincronização.

### Ambas

- materialização visual final;
- implementação;
- evidência de produção;
- mecanismo técnico de idempotência;
- teste real.

## 12. Critérios para eventual gate de maturidade

Um exame posterior de maturidade somente deve ocorrer após adjudicação humana dos achados funcionais e materialização das responsabilidades funcionais aplicáveis.

Critérios candidatos para esse gate incluem:

1. origem e destino estáveis;
2. responsabilidade de cada superfície inequívoca;
3. revisão consciente preservada;
4. voluntariedade preservada;
5. retorno/interrupção governados;
6. falha e estado indeterminado governados;
7. remoção/substituição governadas quando aplicáveis;
8. proveniência preservada;
9. autorização material mantida em `PER-005`;
10. ausência de nova regra funcional aberta;
11. nenhuma dependência de mecanismo técnico específico para afirmar o contrato funcional.

## 13. Resultado do exame

```text
UXA-104 FUNCTIONAL EXAM
→ COMPLETE

FINDINGS
→ CANDIDATE
→ NOT ADJUDICATED

PER-013 / PER-014
→ FUNCTIONALLY SUFFICIENT CANDIDATES

TRN-014..017
→ FUNCTIONALLY SUFFICIENT CANDIDATES
→ CONTRACTED / UNCHANGED

NEW FUNCTIONAL GAP
→ NONE IDENTIFIED

MATURITY PROMOTIONS
→ 0

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED
```

## 14. Próximo gate

O próximo gate humano é:

```text
ADJUDICATE UXA-104 FUNCTIONAL EXAM FINDINGS?

IF YES
→ MATERIALIZE FUNCTIONAL AUTHORITY / RECONCILE CURRENT AUTHORITIES
→ KEEP TRN-014..017 UNCHANGED
→ ONLY THEN CONSIDER SEPARATE MATURITY EXAM

IF NO
→ REOPEN FUNCTIONAL FINDINGS
```
