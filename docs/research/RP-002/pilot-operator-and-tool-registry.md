---
id: RP-002-PILOT-OPS-REG-001
title: Piloto — Registro de Operadores, Ferramentas e Fluxos de Dados
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: partial_real_stack_registry
related:
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-PRIV-CH-TEST-001
  - RP-002-PILOT-NOTICE-CONSENT-001
---

# Piloto — Registro de Operadores, Ferramentas e Fluxos de Dados

## 1. Finalidade

Este documento materializa o registro progressivo de operadores, ferramentas e fluxos de dados do Dry Run Real / piloto `RP-002`.

Ele existe para impedir que uma ferramenta seja promovida ao stack real apenas porque está disponível tecnicamente.

Regra:

> **Disponibilidade técnica não equivale a aprovação para tratamento de dados do piloto.**

O registro avança somente com evidência operacional e revisão proporcional.

## 2. Estado executivo

```text
P3-C1 — OPERADOR DO CANAL DE PRIVACIDADE
→ PARTIAL PASS

P3-C2 — FORM / RECRUITMENT TOOL
→ HOLD

P3-C3 — IDENTITY STORAGE
→ HOLD

P3-C4 — RESEARCH STORAGE
→ HOLD

P3-C5 — GENERAL AI TOOL
→ HOLD

P3-C6 — SEARCH / WEB TOOLS
→ HOLD

P3-C — DESTINATÁRIOS / OPERADORES REAIS
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

`P3-C1` é parcial porque o serviço de e-mail está comprovadamente operacional, mas o registro contratual interno e as salvaguardas específicas da conta ainda devem ser reconciliados antes da liberação final do piloto.

## 3. Critérios de registro por operador

Para cada componente real, registrar:

| Campo | Obrigação |
|---|---|
| `tool_or_operator` | serviço ou operador real |
| `purpose` | finalidade delimitada |
| `data_categories` | categorias de dados recebidas |
| `direct_identifiers_allowed` | se identificadores diretos são permitidos |
| `sensitive_data_allowed` | se dados sensíveis são permitidos |
| `international_transfer` | estado conhecido da transferência internacional |
| `contract_or_DPA_status` | evidência contratual/DPA disponível |
| `approved_scope` | escopo estrito aprovado |
| `status` | estado operacional |
| `notes` | limitações e blockers |

## 4. OP-001 — Hostinger Mail

### 4.1 Evidência operacional

Os canais oficiais:

- `privacidade@guivos.com`;
- `privacy@guivos.com`;

foram provisionados e passaram pelo teste sintético end-to-end registrado em `RP-002-PILOT-PRIV-CH-TEST-001`.

A resposta sintética do canal exibiu identificação operacional de **Hostinger Mail**.

Isso comprova o uso do serviço para os canais de privacidade; não autoriza outros produtos Hostinger para outras finalidades do piloto.

### 4.2 Relação de processamento declarada pelo fornecedor

A Hostinger publica Data Processing Addendum em que declara, para Customer Data dos serviços cobertos, atuação como `Processor`, enquanto o cliente atua como `Controller` ou `Processor`, conforme aplicável.

Fonte oficial:

<https://www.hostinger.com/br/legal/dpa>

O DPA também prevê subprocessadores e disciplina o processamento de Customer Data conforme os serviços cobertos e instruções documentadas do cliente.

### 4.3 Transferência internacional

A política de privacidade da Hostinger informa que informações pessoais podem ser mantidas, processadas ou armazenadas no Reino Unido, Países Baixos, Lituânia, Chipre e outras jurisdições quando necessário à prestação dos serviços.

Fonte oficial:

<https://www.hostinger.com/br/legal/politica-de-privacidade>

Consequência:

```text
INTERNATIONAL TRANSFER
→ POSSIBLE / MATERIAL
```

Este registro **não afirma a localização física exata de uma mensagem ou mailbox individual**.

### 4.4 Registro do operador

| Campo | Estado |
|---|---|
| `tool_or_operator` | Hostinger Mail / serviço coberto pela relação Hostinger |
| `purpose` | canal oficial de privacidade e atendimento de direitos/esclarecimentos |
| `data_categories` | endereço de e-mail, conteúdo da solicitação, metadados mínimos de comunicação e resposta |
| `direct_identifiers_allowed` | `YES — somente porque o próprio canal de direitos exige identificação/contato proporcional` |
| `sensitive_data_allowed` | `NO BY DEFAULT` |
| `international_transfer` | `POSSIBLE / MATERIAL` |
| `contract_or_DPA_status` | DPA público verificado; vínculo/aceite da conta deve permanecer evidenciado internamente |
| `approved_scope` | `privacy mailbox only` |
| `status` | `CONDITIONALLY APPROVED / OPERATIONALLY VERIFIED` |
| `notes` | não usar como repositório do dossiê de Research; minimizar conteúdo recebido; não solicitar senha/documento sem necessidade específica |

## 5. Limite da aprovação do OP-001

A aprovação operacional é restrita a:

```text
SOLICITAÇÃO DE PRIVACIDADE
→ RECEBIMENTO
→ TRIAGEM
→ RESPOSTA
→ FECHAMENTO
```

Ela não autoriza automaticamente:

- recrutamento do piloto por e-mail;
- armazenamento do Identity Vault;
- armazenamento da Research Base;
- envio de dossiê pseudonimizado por e-mail;
- compartilhamento de oportunidades ou benchmark;
- tratamento regular de dados sensíveis;
- anexos identificáveis desnecessários.

## 6. Gmail conectado — classificação correta

Uma conta Gmail conectada foi utilizada como **remetente externo sintético** para testar os canais de privacidade.

Isso prova o teste do lado remetente, mas não aprova Gmail/Google Workspace como componente do stack de participante.

```text
GMAIL / TEST SENDER
→ SYNTHETIC EXTERNAL TEST ONLY
→ NOT APPROVED AS PILOT DATA OPERATOR
```

Não registrar no GKR mensagens individuais, IDs privados, conteúdo identificável ou credenciais.

## 7. Google Drive — disponibilidade não equivale a aprovação

A auditoria encontrou infraestrutura documental da Guivos em Google Drive, inclusive pasta institucional de conhecimento.

Não foi encontrado artefato dedicado ao `RP-002` / piloto que autorize tratar o Drive existente como Identity Vault ou Research Storage.

Estado:

```text
GOOGLE DRIVE
→ TECHNICALLY AVAILABLE
→ NOT APPROVED FOR PARTICIPANT DATA
```

Nenhuma planilha, documento ou pasta existente deve receber dados reais do piloto por conveniência.

## 8. FORM / RECRUITMENT TOOL

```text
STATUS
→ TBD / HOLD
```

Antes de aprovação, definir:

- ferramenta;
- finalidade;
- campos coletados;
- minimização;
- acesso;
- operador;
- transferência;
- retenção;
- exclusão;
- relação com consentimento.

## 9. IDENTITY STORAGE

```text
STATUS
→ TBD / HOLD
```

Requisitos mínimos:

- acesso restrito;
- identificadores diretos separados da Research Base;
- chave de ligação controlada;
- correção e exclusão executáveis;
- retenção definida;
- trilha mínima de acesso quando aplicável;
- nenhum acesso para Supply Researcher/Verifier por padrão.

## 10. RESEARCH STORAGE

```text
STATUS
→ TBD / HOLD
```

Requisitos mínimos:

- pseudônimo em vez de identidade direta;
- campos proporcionais ao episódio;
- ausência de dado sensível desnecessário;
- exportação/eliminação possíveis;
- permissões por função;
- retenção definida;
- separação material do Identity Vault.

## 11. GENERAL AI TOOL

```text
STATUS
→ TBD / HOLD
```

A futura aprovação precisa registrar, no mínimo:

- fornecedor/produto real;
- finalidade por tarefa;
- tratamento de conteúdo submetido;
- política contratual aplicável;
- transferência internacional;
- identificadores diretos proibidos por padrão;
- contexto mínimo pseudonimizado;
- dado sensível desnecessário proibido;
- retenção/controles do produto efetivamente contratado.

Uma ferramenta de IA não recebe automaticamente a Journey completa.

## 12. SEARCH / WEB TOOLS

```text
STATUS
→ TBD / HOLD
```

Objetivo futuro:

- localizar supply público;
- verificar fontes;
- checar freshness;
- validar elegibilidade e fatos críticos.

Regra:

> **pesquisa de supply deve usar contexto mínimo e, por padrão, não precisa de identidade direta da Pessoa.**

Antes de aprovação, definir quais ferramentas externas recebem queries e se as queries podem conter informação pessoal ou contextual identificável.

## 13. Mapa atual do fluxo de dados

Somente o seguinte fluxo externo está comprovado/aprovável nesta etapa:

```text
TITULAR / TESTE SINTÉTICO
→ privacidade@guivos.com ou privacy@guivos.com
→ HOSTINGER MAIL
→ TRIAGEM PELO OWNER FUNCIONAL
→ RESPOSTA
```

Todo o restante continua bloqueado:

```text
RECRUTAMENTO
→ TBD

IDENTIDADE
→ TBD

EPISÓDIO DE RESEARCH
→ TBD

IA
→ TBD

SEARCH / WEB
→ TBD
```

## 14. Transferência internacional — estado do stack

| Componente | Estado |
|---|---|
| Hostinger Mail | `POSSIBLE / MATERIAL — supplier policy verified` |
| Gmail sintético | fora do stack de participante |
| Google Drive | não aprovado |
| Form/recruitment | TBD |
| Identity Storage | TBD |
| Research Storage | TBD |
| General AI | TBD |
| Search/Web | TBD |

A futura análise de transferência deve refletir **o produto e contrato efetivamente usados**, não a marca abstrata do fornecedor.

## 15. DPA e contratos

Para `OP-001`:

```text
PUBLIC DPA
→ VERIFIED

ACCOUNT / CONTRACT RELATIONSHIP
→ OPERATIONALLY IMPLIED BY ACTIVE SERVICE
→ INTERNAL EVIDENCE STILL REQUIRED FOR FINAL RELEASE
```

Não armazenar comprovantes contratuais privados no GKR.

O GKR deve registrar apenas o estado da verificação.

## 16. Dados sensíveis

Nenhum operador do stack inicial recebe autorização genérica para dados sensíveis.

```text
SENSITIVE DATA
→ NO BY DEFAULT
```

Se uma futura tarefa exigir isso, a ferramenta e a base legal devem ser reavaliadas especificamente.

## 17. Requisitos de acesso

O fato de uma ferramenta existir não prova que suas permissões reais estejam corretas.

Para cada componente aprovado, ainda será necessário verificar:

- owner;
- usuários autorizados;
- menor privilégio;
- MFA/controles disponíveis quando aplicável;
- possibilidade de correção;
- possibilidade de exclusão;
- exportação;
- revogação de acesso;
- residual scan após exclusão quando tecnicamente possível.

## 18. Relação com P3

Este registro promove apenas uma parte do blocker:

```text
P3-C1 — HOSTINGER MAIL / PRIVACY CHANNEL
→ PARTIAL PASS

P3-C OVERALL
→ HOLD
```

P3 não chega a `PASS` enquanto o stack que efetivamente tocará dados do participante permanecer indefinido.

## 19. Relação com o Notice v0.1

O `RP-002-PILOT-NOTICE-CONSENT-001` continua `draft`.

Na próxima revisão ele poderá incorporar Hostinger Mail como operador/destinatário do canal de privacidade, mas não deve ser promovido ainda porque:

- Form/recruitment está TBD;
- Identity Storage está TBD;
- Research Storage está TBD;
- IA está TBD;
- Search/Web está TBD;
- retenção exata permanece pendente;
- P2C permanece HOLD;
- revisão jurídica/privacidade final permanece pendente.

## 20. Decisão

O registro de operadores deixa de estar totalmente vazio.

O primeiro operador real comprovado é o serviço de e-mail utilizado pelos canais oficiais de privacidade.

A decisão não amplia o escopo do piloto nem libera dados reais.

Checkpoint:

```text
OP-001 HOSTINGER MAIL
→ CONDITIONALLY APPROVED FOR PRIVACY CHANNEL ONLY

P3-C
→ HOLD

P3
→ CONDITIONAL

P4
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```