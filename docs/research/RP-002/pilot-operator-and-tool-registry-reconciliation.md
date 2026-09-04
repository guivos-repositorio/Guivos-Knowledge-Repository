---
id: RP-002-PILOT-OPS-REG-002
title: Piloto — Reconciliação do Registro de Operadores, Ferramentas e Fluxos
status: active
version: 1.0.1
owner: Guivos Research
last_updated: 2026-09-04
normative: false
parent: RP-002
maturity: documentary_target_registry_reconciled_pre_configuration
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-RESEARCH-MAILBOX-DEC-001
  - RP-002-PILOT-IDENTITY-VAULT-DEC-001
  - RP-002-PILOT-RESEARCH-BASE-DEC-001
  - RP-002-PILOT-LINKAGE-KEY-DEC-001
  - RP-002-PILOT-OPENAI-API-DEC-001
  - RP-002-PILOT-SEARCH-WEB-DEC-001
---

# Piloto — Reconciliação do Registro de Operadores, Ferramentas e Fluxos

## 1. Finalidade

Este documento reconcilia o registro histórico `RP-002-PILOT-OPS-REG-001`, removido do corpus corrente após absorção e preservado no histórico Git, com as decisões documentais posteriores do stack.

O registro anterior permanece recuperável no histórico Git como evidência do momento em que vários componentes estavam `TBD`. No corpus corrente, este documento é a autoridade documental de reconciliação e prevalece quando houver divergência de status-alvo.

Regra preservada:

> **Target documental não equivale a operador/configuração operacional aprovada.**

## 2. Estado executivo

```text
RECRUITMENT / RESEARCH MAIL
→ Hostinger Mail / research@guivos.com
→ A1 PASS

IDENTITY STORAGE
→ local encrypted Identity Vault target
→ external operator: none by design
→ operational HOLD

RESEARCH STORAGE
→ separate local encrypted Research Base target
→ external operator: none by design
→ operational HOLD

LINKAGE KEY
→ separate local encrypted boundary target
→ external operator: none by design
→ operational HOLD

GENERAL AI
→ OpenAI API dedicated RP-002 project target
→ operational HOLD

SEARCH / WEB
→ OpenAI API Web Search target + original public-source verification
→ operational HOLD

P3-C
→ DOCUMENTARY TARGETS IDENTIFIED
→ FINAL / OPERATIONAL HOLD
```

## 3. OP-001 — Hostinger Mail

### Escopo documental atual

Hostinger Mail é o operador-alvo/real já identificado para:

- `research@guivos.com` — recrutamento, Notice, consentimento operacional, agendamento, logística, follow-up autorizado e fechamento;
- `privacidade@guivos.com`;
- `privacy@guivos.com`.

O canal de Research passou por teste end-to-end e A1 está em `PASS`. Os canais de privacidade e o processo sintético de direitos também possuem evidência própria.

### Registro

| Campo | Estado |
|---|---|
| `tool_or_operator` | Hostinger Mail |
| `purpose` | Research mailbox + privacy/rights mailboxes, cada qual em seu escopo |
| `data_categories` | contato, identidade operacional mínima, Notice/consent status, conteúdo mínimo de direitos/comunicação |
| `direct_identifiers_allowed` | `YES — somente quando necessários ao contato, consentimento ou direitos` |
| `sensitive_data_allowed` | `NO BY DEFAULT` |
| `international_transfer` | `POSSIBLE / MATERIAL` |
| `contract_or_DPA_status` | DPA público verificado; relação da conta deve permanecer evidenciada internamente |
| `approved_scope` | e-mail operacional de Research e privacidade; não Research dossier |
| `status` | `PARTIALLY OPERATIONALLY VERIFIED` |

Fonte pública já registrada no GKR:

<https://www.hostinger.com/br/legal/dpa>

## 4. Recrutamento / formulário

Para o primeiro `N=1`, não é necessário introduzir um form externo separado.

Target documental:

```text
RECRUITMENT INTAKE
→ research@guivos.com
→ minimum fields only

EXTERNAL FORM TOOL
→ NOT REQUIRED FOR PARTICIPANT 001
```

Isso reduz operadores e superfície de dados.

Se um formulário for introduzido no futuro, ele deverá passar por decisão própria antes de receber dados reais.

## 5. TL-001 — Identity Vault local

O Identity Vault é ferramenta/armazenamento local, não operador externo de dados por design.

```text
TOOL TARGET
→ VeraCrypt standard local encrypted volume

DIRECT IDENTITY
→ YES, minimum necessary

CLOUD TRANSFER
→ NO BY DESIGN

STATUS
→ DOCUMENTED TARGET / OPERATIONAL HOLD
```

A configuração real e integridade do software continuam não verificadas nesta fase.

## 6. TL-002 — Research Base local

```text
TOOL TARGET
→ separate VeraCrypt-compatible local encrypted volume target

DIRECT IDENTITY
→ NO BY DEFAULT

PSEUDONYMIZED RESEARCH
→ YES

CLOUD TRANSFER
→ NO BY DESIGN

STATUS
→ DOCUMENTED TARGET / OPERATIONAL HOLD
```

Não é permitido usar Google Drive existente como substituto por conveniência.

## 7. TL-003 — Linkage Key local

```text
TOOL TARGET
→ separate encrypted local boundary

CONTENT
→ minimum participant_id ↔ identity reference linkage

ACCESS
→ more restricted than Research Base

EXTERNAL TRANSFER
→ NO

STATUS
→ DOCUMENTED TARGET / OPERATIONAL HOLD
```

OpenAI, Search/Web, GKR e analistas não recebem a Linkage Key.

## 8. OP-002 — OpenAI API

### Target

```text
SERVICE
→ OpenAI API

PROJECT
→ dedicated Guivos / RP-002 project

PURPOSE
→ bounded AI assistance on minimized pseudonymized context

DIRECT IDENTIFIERS
→ NO BY DEFAULT

SENSITIVE DATA
→ NO BY DEFAULT

LINKAGE KEY
→ NEVER
```

### Retenção / controles documentais

A documentação oficial verificada em 2026-08-27 informa:

- dados de API não são usados para treinamento por padrão, salvo opt-in;
- abuse monitoring logs podem reter conteúdo do cliente por até 30 dias por padrão;
- application state depende do endpoint/capability;
- ZDR/MAM dependem de elegibilidade/aprovação e não são presumidos.

Fontes:

- <https://platform.openai.com/docs/models/default-usage-policies-by-endpoint>
- <https://help.openai.com/en/articles/10306912-sharing-feedback-evals-and-api-data-with-openai>
- <https://openai.com/policies/data-processing-addendum/>

### Registro

| Campo | Estado |
|---|---|
| `tool_or_operator` | OpenAI API |
| `purpose` | assistência de IA delimitada para Research pseudonimizado |
| `data_categories` | contexto mínimo pseudonimizado e outputs necessários |
| `direct_identifiers_allowed` | `NO BY DEFAULT` |
| `sensitive_data_allowed` | `NO BY DEFAULT` |
| `international_transfer` | `MATERIAL / MUST BE REVIEWED` |
| `contract_or_DPA_status` | DPA público atual verificado; relação/configuração real da conta ainda deve ser verificada |
| `approved_scope` | target documental only |
| `status` | `DOCUMENTED TARGET / OPERATIONAL HOLD` |

## 9. OP-003 — OpenAI API Web Search

A9 seleciona como target primário a capacidade de Web Search dentro do projeto dedicado da OpenAI API.

```text
PURPOSE
→ locate / verify public supply

QUERY
→ minimized
→ no direct identity by default

SOURCE VERIFICATION
→ original public source when material

STATUS
→ DOCUMENTED TARGET / OPERATIONAL HOLD
```

O uso compartilha a governança contratual e de dados de A8, sem presumir ZDR.

## 10. Public-source websites

Sites públicos originais poderão ser abertos somente para verificação de fatos materiais.

Durante simples verificação:

- não enviar nome da Pessoa;
- não enviar e-mail/telefone;
- não preencher formulário;
- não criar conta;
- não se candidatar;
- não realizar compra/transação;
- não inserir contexto identificável em campos de busca locais.

Como a lista de fontes é variável e orientada pelo supply, elas não recebem autorização genérica como operadores de dados do participante.

Se um site precisar receber dados da Pessoa, isso será um novo fluxo e exigirá decisão própria.

## 11. Google Drive

```text
GOOGLE DRIVE EXISTING
→ available for institutional documentation
→ NOT APPROVED FOR PARTICIPANT DATA
→ NOT IDENTITY VAULT
→ NOT RESEARCH BASE
→ NOT LINKAGE KEY
```

Esse estado permanece inalterado.

## 12. Gmail / remetente sintético

```text
GMAIL
→ synthetic external sender used in prior testing
→ not participant stack operator
```

Não inferir aprovação para dados reais.

## 13. Mapa documental do fluxo

```text
RECRUITMENT / NOTICE / CONSENT
→ research@guivos.com
→ Hostinger Mail
→ Identity Vault minimum record

IDENTITY
→ local encrypted Identity Vault

LINK
→ separate local encrypted Linkage Key

RESEARCH
→ separate local encrypted pseudonymized Research Base

AI TASK
→ select + sanitize minimum context
→ OpenAI API dedicated RP-002 project
→ human review

SEARCH
→ minimized context
→ OpenAI API Web Search
→ verify original public source
→ store material source/facts in Research Base

RIGHTS
→ privacy mailbox
→ reconcile Identity / Linkage / Research
→ apply correction/deletion/retention flow
```

## 14. Transferência internacional

| Componente | Estado documental |
|---|---|
| Hostinger Mail | `POSSIBLE / MATERIAL` |
| Local Identity/Research/Linkage | `NO EXTERNAL TRANSFER BY DESIGN` |
| OpenAI API | `MATERIAL / MUST BE REVIEWED` |
| OpenAI Web Search | `MATERIAL / follows A8 context` |
| Public-source verification | no participant data submission by design |
| Google Drive | not approved for participant data |
| Gmail synthetic | outside participant stack |

## 15. P3-C

O blocker muda de natureza:

```text
BEFORE
→ operators/tools materially TBD

NOW
→ documentary targets identified
→ operational configuration / contract relationship / evidence still pending
```

Portanto:

```text
P3-C DOCUMENTATION
→ TARGET MAP CLOSED

P3-C FINAL / OPERATIONAL
→ HOLD
```

## 16. Estado final

```text
OPERATOR / TOOL DOCUMENTARY REGISTRY
→ RECONCILED

NEW EXTERNAL OPERATORS INTRODUCED WITHOUT DECISION
→ NO

P3-C
→ HOLD

P3-D
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
