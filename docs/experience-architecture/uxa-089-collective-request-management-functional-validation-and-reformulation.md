---
id: UXA-089
title: Validação Funcional Corrente da Gestão de Solicitações do Coletivo
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
parent: UXA-000
depends_on:
  - UXA-014
  - UXA-056
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-UX-ORGCOL-AUTH-STATE-MAP-001
related:
  - GKR-SURF-COL-003
  - GKR-TRN-105
  - GKR-TRN-106
  - GKR-TRN-107
  - GKR-TRN-108
  - GKR-TRN-109
  - GKR-TRN-112
normative: false
---

# Validação Funcional Corrente da Gestão de Solicitações do Coletivo

## 1. Finalidade

Governar a responsabilidade funcional de `GKR-SURF-COL-003 — gestão de solicitações` sem depender de materializações históricas.

A superfície permite que uma pessoa legitimamente responsável pelo Coletivo analise uma solicitação e escolha, dentro de sua autoridade:

```text
AGUARDAR
PEDIR INFORMAÇÃO
APROVAR
RECUSAR
```

Nenhuma dessas ações é presumida por leitura, navegação, passagem do tempo ou destaque visual.

## 2. Contexto e autoridade

Antes de qualquer decisão, a experiência deve tornar compreensíveis:

- Coletivo e contexto ativo;
- papel/representação da pessoa responsável;
- escopo de autoridade aplicável;
- estado corrente da solicitação;
- referência temporal adequada ao estado;
- critérios previamente apresentados à Pessoa;
- dados mínimos necessários à decisão.

Autoridade insuficiente bloqueia a decisão substantiva sem fabricar delegação.

## 3. Referências temporais

Tempo deve ser tipado conforme significado. Não usar uma única coluna genérica para misturar:

- estimativa de decisão;
- prazo para resposta;
- data de envio;
- vencimento legítimo;
- última atualização.

Referência temporal não cria prioridade automática nem posição de fila.

## 4. Minimização de dados

A análise recebe apenas os dados necessários à finalidade e ao critério aplicável.

Informação protegida exige autoridade e finalidade proporcionais. Conteúdo da Jornada pessoal não é exposto por conveniência operacional.

## 5. Ações correntes

### 5.1 Aguardar

Mantém o estado sem produzir aprovação, recusa, prioridade ou promessa.

### 5.2 Pedir informação

Solicita informação adicional com finalidade clara sem aprovar nem reiniciar silenciosamente a solicitação.

### 5.3 Aprovar

Exige confirmação consciente e autoridade válida. O vínculo é formado pelo efeito autorizado da decisão, não pelo clique posterior de navegação.

### 5.4 Recusar

Exige fundamento proporcional e consequência compreensível. Recusa não cria avaliação negativa automática da Pessoa.

## 6. Retorno e reversibilidade

É sempre legítimo voltar sem decidir.

Rascunho de decisão não deve produzir efeito antes de confirmação. Quando o estado corrente mudar durante a análise, a experiência deve revalidá-lo antes de aplicar ação material.

## 7. Continuidade

A superfície participa dos handoffs governados por `UXA-090` e pelo Transition Registry.

```text
PER-105 ↔ COL-003
→ mesmo pedido lógico
→ mesmo estado canônico
→ efeitos explícitos
→ sem duplicação silenciosa
```

`TRN-108` é validada posteriormente no contrato corrente de `UXA-092`.

## 8. Estado

```text
GKR-SURF-COL-003
→ FUNCTIONALLY VALIDATED

VISUAL BASELINE
→ NONE REQUIRED

MAIN O/C EXPERIENCE
→ GOVERNED BY CURRENT AUTHENTICATED AUTHORITIES

IMPLEMENTATION
→ NOT PROVEN BY THIS DOCUMENT
```
