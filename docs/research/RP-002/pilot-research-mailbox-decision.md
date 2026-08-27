---
id: RP-002-PILOT-RESEARCH-MAILBOX-DEC-001
title: Piloto — Decisão da Mailbox de Research do Primeiro Dry Run
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_address_decided_pre_provisioning
related:
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-STACK-PROP-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
---

# Piloto — Decisão da Mailbox de Research do Primeiro Dry Run

## 1. Finalidade

Este documento fecha a decisão de nomenclatura do primeiro componente operacional `A1 — Research Mailbox` da arquitetura-alvo do Dry Run Real `N=1` do `RP-002`.

Ele responde somente:

> **Qual endereço institucional deverá ser provisionado e testado como mailbox operacional de Research do primeiro Dry Run?**

A decisão do endereço não prova provisionamento, recebimento, envio, controle de acesso ou owner operacional efetivo da caixa.

## 2. Decisão

Fica definido como endereço primário do primeiro Dry Run:

```text
RESEARCH MAILBOX
→ research@guivos.com

DOMAIN
→ guivos.com

FUNÇÃO
→ Guivos Research / RP-002

TARGET OPERATOR
→ Hostinger Mail

ADDRESS DECISION
→ PASS

PROVISIONING
→ HOLD

END-TO-END
→ HOLD

OPERATIONAL OWNER VERIFICATION
→ HOLD

A1 — RESEARCH MAILBOX
→ PARTIAL / NOT RELEASED
```

## 3. Razões da nomenclatura

`research@guivos.com` é adotado porque:

1. identifica uma função institucional, não uma Pessoa;
2. coincide com o owner funcional já utilizado no RP-002: `Guivos Research`;
3. funciona de forma compreensível em contexto global;
4. evita vincular o piloto a um idioma local no identificador primário;
5. permite continuidade futura sem depender do operador humano atual;
6. é suficientemente específico para separar Research de Privacy, Support, Sales e outras funções;
7. reduz a necessidade de múltiplas caixas no primeiro Dry Run `N=1`.

## 4. Relação com `pesquisa@guivos.com`

Para o primeiro Dry Run:

```text
pesquisa@guivos.com
→ NOT REQUIRED
```

Ele poderá ser avaliado futuramente como alias de entrada em português, caso exista necessidade real de UX ou comunicação local.

Regra:

> **um eventual alias não deve criar uma segunda base operacional, uma segunda fila de governança ou um segundo dossiê de Research.**

Para `N=1`, a arquitetura permanece deliberadamente simples:

```text
ONE FUNCTION
→ ONE PRIMARY MAILBOX
→ research@guivos.com
```

## 5. Escopo permitido da mailbox

A caixa poderá ser usada, depois de provisionada e aprovada, exclusivamente para necessidades operacionais do piloto compatíveis com os documentos vigentes, como:

- recrutamento controlado;
- entrega de notice aplicável;
- registro operacional de aceite/consentimento quando essa for a forma aprovada;
- agendamento;
- comunicação logística da sessão;
- follow-up autorizado;
- encerramento operacional do ciclo.

Ela não deve ser usada por inferência para:

- marketing;
- publicidade;
- newsletter;
- vendas;
- suporte geral da Guivos;
- canal de privacidade/direitos;
- armazenamento do dossiê rico de Research;
- armazenamento de chave de ligação;
- envio de dados identificáveis para IA ou Search.

## 6. Separação de funções

A decisão preserva fronteiras claras:

```text
research@guivos.com
→ OPERAÇÃO DE RESEARCH / PILOTO

privacidade@guivos.com
privacy@guivos.com
→ PRIVACIDADE / DIREITOS
```

Uma solicitação de direitos recebida por `research@guivos.com` não deve ser ignorada.

Quando isso ocorrer, o fluxo deve encaminhar o caso ao processo oficial de privacidade, mantendo rastreabilidade mínima e sem duplicar dados desnecessariamente.

## 7. Dados permitidos por padrão

Depois de liberada, a mailbox deve observar minimização.

Exemplos de dados compatíveis quando necessários:

- nome para comunicação operacional;
- e-mail do participante;
- `participant_id` quando operacionalmente útil;
- confirmação `18+` sem data de nascimento completa por padrão;
- disponibilidade/agendamento;
- estado de recrutamento;
- versão do notice;
- manifestação operacional vinculada ao notice, quando aplicável;
- follow-up estritamente necessário.

Não solicitar por padrão:

- CPF;
- RG;
- endereço residencial completo;
- dados bancários;
- senha;
- credenciais;
- biografia extensa;
- dados sensíveis não necessários;
- transcrição identificável da entrevista;
- dossiê completo do Momento.

## 8. Relação com Identity Vault

A mailbox não substitui o `Identity Vault`.

```text
MAILBOX
→ canal operacional

IDENTITY VAULT
→ registro mínimo estruturado de identidade/operação

RESEARCH BASE
→ conteúdo pseudonimizado da pesquisa
```

Informações necessárias recebidas por e-mail devem ser transferidas somente para o ambiente apropriado e segundo a política de retenção que ainda será congelada.

A existência histórica da mensagem na mailbox deve ser considerada na avaliação de retenção e exclusão.

## 9. Operador-alvo

A arquitetura-alvo já selecionou Hostinger Mail para a mailbox de Research.

Esta decisão apenas fixa:

```text
TARGET OPERATOR
→ Hostinger Mail
```

Ela não afirma que `research@guivos.com` já existe nem promove o operador para esse novo propósito sem verificação.

O uso previamente comprovado do Hostinger Mail nos canais de privacidade é evidência de capacidade operacional do serviço, mas não substitui o teste específico desta caixa e desta finalidade.

## 10. Owner funcional

Owner-alvo:

```text
GUIVOS RESEARCH
→ PILOT OWNER DO RP-002
```

A função já existe na governança do piloto.

Entretanto, `A1` somente poderá registrar owner operacional como `PASS` depois que o acesso real à mailbox estiver comprovado sem registrar no GKR:

- senha;
- token;
- recovery code;
- credencial;
- segredo;
- Pessoa nominal desnecessária.

## 11. Gates de A1

### A1-1 — endereço decidido

```text
research@guivos.com
→ PASS
```

### A1-2 — provisionamento

Critério:

- mailbox existente no domínio `guivos.com`;
- login funcional sob controle autorizado;
- sem registrar credenciais no GKR.

Estado:

```text
HOLD
```

### A1-3 — recebimento externo

Critério:

- mensagem sintética enviada de origem externa;
- recebimento confirmado na mailbox.

Estado:

```text
HOLD
```

### A1-4 — resposta externa

Critério:

- resposta enviada pela mailbox;
- retorno recebido pelo remetente externo.

Estado:

```text
HOLD
```

### A1-5 — owner funcional

Critério:

- Guivos Research / Pilot Owner consegue operar a caixa;
- acesso comprovado sem exposição de credenciais.

Estado:

```text
HOLD
```

### A1-6 — segregação funcional

Critério:

- mailbox não redireciona por padrão para caixa pessoal incompatível;
- finalidade Research distinguível dos canais de Privacy;
- ausência de uso de marketing/vendas no teste.

Estado:

```text
HOLD
```

## 12. Teste sintético exigido

Depois do provisionamento, executar um teste sem dados pessoais reais de participante.

Identificador recomendado:

```text
T-RESEARCH-001
```

Fluxo mínimo:

```text
REMETENTE EXTERNO
→ research@guivos.com
→ RECEBIMENTO
→ ACESSO PELA FUNÇÃO GUIVOS RESEARCH
→ RESPOSTA
→ RETORNO AO REMETENTE
```

A mensagem deve declarar explicitamente que se trata de teste sintético e não contém dados pessoais reais de participante.

## 13. Evidência suficiente para promover A1

A1 somente pode passar a `PASS` quando houver evidência material de:

```text
ADDRESS
→ DECIDED

PROVISIONING
→ PASS

INBOUND
→ PASS

OUTBOUND / REPLY
→ PASS

FUNCTIONAL OWNER
→ PASS

FUNCTIONAL SEGREGATION
→ PASS
```

Não registrar no GKR screenshot, log ou conteúdo que exponha credencial ou dado pessoal desnecessário.

## 14. Relação com P3-C

Esta decisão não promove `P3-C`.

Ela define um operador e uma finalidade candidatos para um componente específico, mas `P3-C — destinatários / operadores reais` depende do conjunto efetivo do stack e das verificações aplicáveis.

Estado preservado:

```text
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

## 15. Próximo ato material

Com o endereço decidido, o próximo ato é:

```text
research@guivos.com
→ PROVISIONAR NO HOSTINGER MAIL
→ TESTAR T-RESEARCH-001
→ COMPROVAR OWNER FUNCIONAL
→ COMPROVAR SEGREGAÇÃO
```

Até esse ciclo estar completo:

```text
A1
→ PARTIAL / HOLD
```

## 16. Estado final desta decisão

```text
RESEARCH MAILBOX ADDRESS
→ research@guivos.com
→ APPROVED

A1-1 ADDRESS DECISION
→ PASS

A1-2 PROVISIONING
→ HOLD

A1-3 INBOUND
→ HOLD

A1-4 OUTBOUND / REPLY
→ HOLD

A1-5 FUNCTIONAL OWNER
→ HOLD

A1-6 SEGREGATION
→ HOLD

A1 OVERALL
→ PARTIAL / HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
