---
id: UXA-102
title: UXA-102 / V5 — Erros, Retornos e Interrupções — Escopo Candidato
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: false
maturity: scope_candidate
depends_on:
  - UXA-101
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
---

# UXA-102 / V5 — Erros, Retornos e Interrupções — Escopo Candidato

## 1. Estado desta abertura

Esta é a abertura governada da UXA-102/V5.

A formulação **“Erros, Retornos e Interrupções”** é tratada aqui como **escopo candidato**. Ela não existia como contrato canônico no `main` antes desta abertura e não deve ser lida como decisão retroativa.

```text
UXA-101
→ última UXA funcional concluída

UXA-102 / V5
→ STARTED
→ SCOPE_CANDIDATE
→ NOT ADJUDICATED
→ NOT IMPLEMENTED
```

## 2. Problema

A arquitetura corrente possui transições com diferentes níveis de maturidade, mas a existência de origem, destino e estado nominal não garante que o comportamento esteja suficientemente governado quando:

- a Pessoa interrompe voluntariamente;
- uma falha conhecida ocorre antes, durante ou depois do handoff;
- não é possível determinar se o efeito ocorreu;
- a Pessoa retorna depois de abandono, timeout, fechamento ou perda de contexto;
- uma ação é repetida;
- o destino mudou ou deixou de estar disponível;
- a autoridade mudou;
- o estado local e o estado remoto divergem;
- a operação precisa ser retomada sem duplicar efeitos.

A UXA-102/V5 examina essas condições transversalmente.

## 3. Baseline corrente

O `GKR-JOURNEY-TRANSITION-REGISTRY-001` contém **76 IDs únicos de transição**.

Distribuição corrente:

| Família | Quantidade |
|---|---:|
| Jornada pessoal | 17 |
| Pessoa em Coletivos e operação do responsável | 14 |
| Organização, oportunidades e relações bilaterais | 16 |
| Opportunity Boost | 6 |
| Planos, cobrança e ciclo de vida | 23 |
| **Total** | **76** |

A contagem anterior de 72 estava mecanicamente desatualizada: `TRN-014..017` já existiam na família da Pessoa, mas não haviam sido incorporadas à tabela de contagem.

## 4. Questão central

> Para cada transição corrente, o que deve acontecer quando o fluxo é interrompido, falha, fica indeterminado, retorna ou é repetido, de forma que a Guivos preserve estado verdadeiro, autoridade correta, segurança e idempotência sem fabricar sucesso?

## 5. Cinco dimensões mínimas de exame

### V5.1 — interrupção voluntária

Examinar:

- cancelar;
- voltar;
- fechar;
- adiar;
- abandonar sem confirmação;
- permanecer na origem.

Regra candidata:

```text
INTERRUPÇÃO VOLUNTÁRIA
≠ FALHA
≠ SUCESSO
≠ EFEITO CONCLUÍDO
```

### V5.2 — falha conhecida

Examinar falhas como:

- validação rejeitada;
- destino indisponível;
- autorização insuficiente;
- processamento recusado;
- erro de rede conhecido;
- dependência indisponível.

O estado precisa dizer o que falhou e o que não ocorreu.

### V5.3 — resultado indeterminado

Examinar situações em que:

- houve tentativa;
- não existe confirmação confiável do efeito;
- repetir imediatamente pode duplicar consequência.

Regra candidata:

```text
UNKNOWN RESULT
≠ FAILURE
≠ SUCCESS
```

### V5.4 — retorno e retomada

Examinar:

- retorno à origem;
- retomada no destino;
- contexto expirado;
- objeto alterado;
- permissão revogada;
- revalidação necessária;
- estado antigo incompatível com o atual.

Retomar não significa reproduzir automaticamente a última ação.

### V5.5 — repetição segura e idempotência

Examinar:

- duplo clique;
- retry;
- refresh;
- replay;
- repetição após timeout;
- repetição após retorno;
- concorrência entre dispositivos/sessões.

Regra candidata:

```text
REPEAT
≠ DUPLICATE EFFECT

RETRY
≠ NEW INTENT BY DEFAULT
```

## 6. Unidade de análise

A UXA-102 não presume que todas as 76 transições precisem da mesma solução.

Cada transição será classificada quanto a:

1. natureza do efeito;
2. autoridade da origem;
3. autoridade do destino;
4. reversibilidade;
5. persistência;
6. risco de duplicidade;
7. dependência externa;
8. necessidade de reconciliação;
9. retorno legítimo;
10. falha conhecida;
11. resultado indeterminado;
12. idempotência.

## 7. Classes candidatas de efeito

Para facilitar o exame, uma transição pode ser classificada como:

- **N — navegação neutra**: sem mutação material esperada;
- **C — criação/commit**: pode criar objeto ou estado persistente;
- **M — mutação**: altera objeto/estado existente;
- **H — handoff**: transfere responsabilidade entre autoridades;
- **B — boundary**: alcança fronteira externa;
- **F — financeira/comercial**: pode produzir efeito econômico ou entitlement;
- **D — distribuição/projeção**: altera disponibilidade/visibilidade sem necessariamente alterar o objeto fonte.

Uma transição pode pertencer a mais de uma classe.

Essas classes são ferramentas de análise, não novos IDs nem estados do Registry.

## 8. Fora do escopo desta abertura

Esta abertura não:

- cria novas transições;
- cria novas superfícies;
- promove maturidade das 76 transições;
- define comportamento interno de terceiros após `BND-001` ou `BND-002`;
- implementa gateway, cobrança ou integração;
- decide Product Engineering;
- cria wireframes;
- autoriza protótipo;
- altera regras de UXA-057;
- cria métricas operacionais;
- presume observabilidade técnica já existente.

## 9. Princípios iniciais

A análise deve preservar:

```text
ATTEMPT
≠ SUCCESS

NO RESPONSE
≠ FAILURE

RETURN
≠ ROLLBACK BY DEFAULT

RETRY
≠ DUPLICATE EFFECT

CLIENT STATE
≠ CANONICAL STATE

LOCAL CACHE
≠ AUTHORITY

NAVIGATION BACK
≠ UNDO

EXTERNAL RETURN
≠ EXTERNAL RESULT CONFIRMED

TIMEOUT
≠ SAFE TO REPEAT WITHOUT RECONCILIATION
```

## 10. Método

A UXA-102/V5 será conduzida em quatro blocos:

```text
V5-A
→ INVENTÁRIO E CLASSIFICAÇÃO DAS 76 TRANSIÇÕES

V5-B
→ EXAME DE FALHA / INTERRUPÇÃO / RETORNO POR FAMÍLIA

V5-C
→ STRESS TEST TRANSVERSAL E RECONCILIAÇÃO

V5-D
→ ADJUDICAÇÃO E EVENTUAL ATUALIZAÇÃO DE AUTORIDADES
```

Nenhuma passagem de bloco equivale a implementação.

## 11. Primeiro gate

O primeiro gate de UXA-102 é:

> validar se as 76 transições correntes estão corretamente inventariadas e classificadas para o exame V5, antes de propor qualquer mudança normativa.

## 12. Estado

```text
UXA-102 / V5
→ STARTED
→ SCOPE_CANDIDATE
→ BASELINE = 76 TRANSITIONS
→ V5-A NEXT

PRODUCT ENGINEERING
→ PAUSED / NOT RELEASED

PROTOTYPE
→ NOT AUTHORIZED

IMPLEMENTATION
→ NOT AUTHORIZED
```
