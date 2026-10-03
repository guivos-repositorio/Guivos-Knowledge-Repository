---
id: GKR-UX-EVALUATION-REPUTATION-SURFACE-RESPONSIBILITY-ADJUDICATION-001
title: Avaliação e Reputação — Adjudicação Canônica de Responsabilidades de Superfície
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-03
normative: true
maturity: responsibility_adjudicated_no_surface_id
depends_on:
  - GKR-UX-EVALUATION-REPUTATION-AUTHORITY-001
  - UXA-057
related:
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-GAPS-001
---

# Avaliação e Reputação — Adjudicação Canônica de Responsabilidades de Superfície

## 1. Finalidade

Adjudicar as responsabilidades de superfície do domínio de Avaliação e Reputação sem confundir responsabilidade funcional com tela, rota, ID ou implementação.

Este ato responde ao gate humano específico autorizado em 03/10/2026 e não seleciona cobertura inicial por objeto sem evidência real suficiente.

## 2. Decisão estrutural

```text
RESPONSIBILITY
≠ SCREEN
≠ ROUTE
≠ SURF-ID

CAPABILITY
≠ NEW SURFACE BY DEFAULT
```

As responsabilidades UXA-057 ficam adjudicadas em quatro contratos funcionais distintos.

## 3. R-A — Registro protegido da avaliação

Responsabilidade canônica pela criação, revisão consciente, submissão, persistência e integridade privada da avaliação.

Objeto autoritativo:

```text
R1
→ PRIVATE AUTHORITATIVE REVIEW OBJECT
```

R-A deve preservar, quando aplicável:

- elegibilidade;
- objeto, edição, etapa, período e unidade da experiência;
- critérios e versão;
- autoria protegida;
- visibilidade escolhida/permitida;
- comentário opcional;
- revisão consciente antes do envio;
- confirmação inequívoca;
- idempotência;
- falha distinta de envio confirmado;
- proveniência de evidência;
- histórico e relações de governança.

R-A não é atribuída a `PER-009`, `PER-108`, `PER-203` ou qualquer outra superfície existente por analogia.

## 4. R-B — Continuidade da autora

Responsabilidade canônica pelo acesso permanente e protegido da autora às próprias avaliações legítimas.

R-B deve permitir, conforme política aplicável:

- localizar avaliações próprias sem depender do objeto original ainda estar público;
- distinguir rascunho, enviada, publicada, contestada, em revisão, limitada, retirada e estados equivalentes autorizados;
- atualizar a mesma experiência sem duplicação artificial;
- alterar visibilidade quando permitido;
- retirar conteúdo quando permitido;
- consultar histórico material;
- denunciar resposta inadequada;
- contestar moderação;
- recorrer quando houver decisão recorrível.

`PER-009` pode futuramente funcionar como **ponto administrativo de acesso**, mas não é autoridade canônica de R-B e não recebe painel por analogia.

## 5. R-C — Resposta e contestação do responsável

Responsabilidade canônica administrativa por objeto/edição para consulta legitimamente permitida, resposta oficial e contestação fundamentada.

R-C exige:

- mandato ou representação verificável;
- objeto e edição corretos;
- competência delimitada;
- proteção da identidade da autora;
- distinção entre resposta e contestação;
- fundamento/evidência para contestação;
- ausência de poder para editar a avaliação;
- ausência de poder para remover crítica por discordância;
- trilha de histórico material.

`COL-002` e `ORG-001` podem futuramente atuar como **entradas administrativas contextuais**, mediante extensão expressa; não recebem R-C por analogia.

## 6. R-D — Governança especializada

Responsabilidade canônica por denúncia, triagem, moderação, medidas proporcionais, restauração e recurso.

R-D é independente da parte avaliada e da resposta oficial.

Deve preservar:

- competência especializada;
- prevenção de conflito;
- proveniência da denúncia/contestação;
- decisão fundamentada;
- proporcionalidade;
- proteção;
- registro de decisão;
- comunicação segura;
- recurso por instância distinta quando aplicável.

`COL-007` preserva apenas seu escopo atual. Não recebe moderação universal UXA-057 por analogia.

## 7. Exibição pública contextual

`P1` permanece objeto público distinto de `R1`.

```text
R1
→ AUTHORIZED PUBLICATION
→ P1

P1
≠ R1
```

A exibição pública é integração contextual e não uma quinta autoridade canônica de registro.

`PER-103` e `PER-203` podem receber exibição contextual somente mediante extensão explícita do contrato correspondente e apenas para objeto/edição/etapa realmente autorizados.

Organização, atividade, curso/programa e relação institucional permanecem sem detalhe público UXA-057 presumido.

## 8. Cobertura inicial

Este ato **não seleciona cobertura inicial**.

```text
INITIAL COVERAGE
→ NOT SELECTED
→ REQUIRES REAL OBJECT / EDITION / EVIDENCE
```

Uma cobertura futura deve identificar:

- objeto;
- edição/unidade;
- etapa;
- período;
- pessoas elegíveis;
- fonte e categoria de evidência;
- titularidade;
- representação;
- proteção;
- regra contra duplicidade;
- autoridade de publicação;
- resposta/contestação;
- governança e recurso.

## 9. Relação O↔C

`ORG-005` e `COL-008` continuam governados por UXA-019.

```text
NEGOTIATION / RELATIONSHIP MANAGEMENT
≠ UXA-057 PUBLIC REPUTATION
```

Avaliação reputacional de relação O↔C exigirá contrato específico de objeto/execução/evidência e não nasce deste ato.

## 10. Materialização

As quatro responsabilidades estão adjudicadas funcionalmente, mas sua materialização física permanece desacoplada.

```text
R-A
→ RESPONSIBILITY ADJUDICATED
→ NO SURF-ID YET

R-B
→ RESPONSIBILITY ADJUDICATED
→ NO SURF-ID YET

R-C
→ RESPONSIBILITY ADJUDICATED
→ NO SURF-ID YET

R-D
→ RESPONSIBILITY ADJUDICATED
→ NO SURF-ID YET
```

Uma única superfície poderá futuramente materializar mais de uma responsabilidade somente se autoridade, permissões, ciclo de vida e proteção forem compatíveis. A quantidade de responsabilidades não determina a quantidade de telas.

## 11. Handoffs

Nenhum `GKR-TRN-*` é criado por este ato.

Transições futuras exigem origem e destino reais, autoridade, identidade da experiência, revalidação, interrupção, retorno, falha e idempotência comprovados.

## 12. Gates posteriores

Continuam separados:

- seleção de cobertura inicial real;
- extensão explícita de `PER-108`/`PER-203` para entrada contextual, quando aplicável;
- extensão explícita de `PER-103`/`PER-203` para exibição pública, quando aplicável;
- extensão explícita de `PER-009`, `COL-002`, `ORG-001` ou `COL-007`, se necessária;
- política jurídica/operacional de moderação, retenção, recurso, conflito e medidas cautelares;
- eventual criação de `SURF-ID`;
- eventual criação de `TRN-ID`;
- Design;
- implementação;
- Product Engineering.

## 13. Estado

```text
UXA-057 SURFACE RESPONSIBILITIES
→ ADJUDICATED

R-A PROTECTED REVIEW REGISTRATION
→ ADJUDICATED

R-B AUTHOR CONTINUITY
→ ADJUDICATED

R-C OFFICIAL RESPONSE / CONTESTATION
→ ADJUDICATED

R-D SPECIALIZED GOVERNANCE
→ ADJUDICATED

INITIAL COVERAGE
→ NOT SELECTED

NEW SURF-ID
→ 0

NEW TRN-ID
→ 0

DESIGN
→ NOT RELEASED BY THIS ACT

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS ACT
```
