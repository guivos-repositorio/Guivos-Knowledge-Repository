---
id: RP-002-PILOT-RESEARCH-MAILBOX-DEC-001
title: Piloto — Decisão da Mailbox de Research do Primeiro Dry Run
status: active
version: 1.1.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_component_verified
related:
  - RP-002-PILOT-STACK-DEC-001
  - RP-002-PILOT-STACK-PROP-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-RESEARCH-MAILBOX-TEST-001
---

# Piloto — Decisão da Mailbox de Research do Primeiro Dry Run

## 1. Finalidade

Este documento registra a decisão e o estado operacional do componente `A1 — Research Mailbox` da arquitetura-alvo do Dry Run Real `N=1` do `RP-002`.

A decisão original definiu `research@guivos.com` como endereço institucional primário. O ciclo posterior de provisionamento, teste ponta a ponta, owner funcional e segregação foi concluído e está evidenciado em `RP-002-PILOT-RESEARCH-MAILBOX-TEST-001`.

## 2. Decisão e estado atual

```text
RESEARCH MAILBOX
→ research@guivos.com

DOMAIN
→ guivos.com

FUNCTION
→ Guivos Research / RP-002

OPERATOR
→ Hostinger Mail

ADDRESS DECISION
→ PASS

PROVISIONING
→ PASS

END-TO-END
→ PASS

OPERATIONAL OWNER VERIFICATION
→ PASS

FUNCTIONAL SEGREGATION
→ PASS

A1 — RESEARCH MAILBOX
→ PASS
```

O fechamento de `A1` não libera, isoladamente, Participante 001 ou o Dry Run Real.

## 3. Razões da nomenclatura

`research@guivos.com` permanece adotado porque:

1. identifica uma função institucional, não uma Pessoa;
2. coincide com o owner funcional já utilizado no RP-002: `Guivos Research`;
3. funciona de forma compreensível em contexto global;
4. evita vincular o piloto a um idioma local no identificador primário;
5. permite continuidade futura sem depender do operador humano atual;
6. separa Research de Privacy, Support, Sales e outras funções;
7. reduz a necessidade de múltiplas caixas no primeiro Dry Run `N=1`.

## 4. Relação com `pesquisa@guivos.com`

Para o primeiro Dry Run:

```text
pesquisa@guivos.com
→ NOT REQUIRED
```

Ele poderá ser avaliado futuramente como alias de entrada em português caso exista necessidade real de UX ou comunicação local.

Regra:

> **um eventual alias não deve criar uma segunda base operacional, uma segunda fila de governança ou um segundo dossiê de Research.**

Para `N=1`:

```text
ONE FUNCTION
→ ONE PRIMARY MAILBOX
→ research@guivos.com
```

## 5. Escopo permitido

A mailbox pode ser usada exclusivamente para necessidades operacionais do piloto compatíveis com os documentos vigentes, como:

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
- canal oficial de privacidade/direitos;
- armazenamento do dossiê rico de Research;
- armazenamento de chave de ligação;
- envio de dados identificáveis para IA ou Search.

## 6. Separação de funções

A fronteira funcional permanece:

```text
research@guivos.com
→ OPERAÇÃO DE RESEARCH / PILOTO

privacidade@guivos.com
privacy@guivos.com
→ PRIVACIDADE / DIREITOS
```

Uma solicitação de direitos recebida por `research@guivos.com` não deve ser ignorada. Ela deve ser encaminhada ao processo oficial de privacidade com rastreabilidade mínima e sem duplicação desnecessária de dados.

## 7. Dados permitidos por padrão

A mailbox deve observar minimização.

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

## 9. Evidência operacional

O `T-RESEARCH-001` comprovou tecnicamente o fluxo ponta a ponta de recebimento e resposta externa.

A confirmação operacional complementar registrou que:

```text
FUNCTIONAL OPERATOR
→ Guivos Research / Pilot Owner do RP-002

DEFAULT FORWARDING TO INCOMPATIBLE PERSONAL MAILBOX
→ NO

RESEARCH PURPOSE SEPARATE FROM PRIVACY
→ YES

MARKETING / SALES USE IN TEST
→ NO
```

A conexão técnica disponível do Hostinger Mail não expõe a configuração interna de `research@guivos.com`. Por isso, owner funcional e ausência de forwarding incompatível são registrados como evidência operacional declarada, e não como inspeção técnica direta da configuração.

Nenhuma credencial é registrada no GKR.

## 10. Gates de A1

```text
A1-1 — ADDRESS DECISION
→ PASS

A1-2 — PROVISIONING
→ PASS

A1-3 — INBOUND
→ PASS

A1-4 — OUTBOUND / REPLY
→ PASS

A1-5 — FUNCTIONAL OWNER
→ PASS

A1-6 — FUNCTIONAL SEGREGATION
→ PASS

A1 — RESEARCH MAILBOX
→ PASS
```

## 11. Relação com P3 e P4

O fechamento de A1 não promove por inferência os gates que dependem do stack completo.

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

## 12. Próximo ato material

Com `A1` encerrado, a sequência operacional aprovada passa para:

```text
A3 — IDENTITY VAULT
→ CONFIGURAR ARMAZENAMENTO LOCAL CRIPTOGRAFADO
→ VERIFICAR PERMISSÕES
→ MANTER SEM CLOUD SYNC POR PADRÃO
```

`A2 — Notice / consent flow` permanece em `HOLD` e deverá ser congelado em etapa compatível com o stack real.

## 13. Estado final desta decisão

```text
RESEARCH MAILBOX ADDRESS
→ research@guivos.com
→ APPROVED

A1 — RESEARCH MAILBOX
→ PASS

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```
