---
id: RP-002-PILOT-RIGHTS-TEST-001
status: active
version: 1.0.0
owner: Guivos Research
normative: false
maturity: operational_evidence_verified
---

# RP-002 — Fechamento do teste sintético do processo de direitos

## 1. Escopo

Este registro documenta a evidência operacional do teste sintético `P2C-SYN-001` do processo de exercício de direitos aplicável ao RP-002.

O teste não utilizou dados pessoais reais de participante.

## 2. Identificação do caso

- Identificador externo do teste: `P2C-SYN-001`.
- Identificador interno solicitado para o tratamento do caso: `TEST-PRIV-001`.
- Canal operacional: `privacidade@guivos.com`.
- Operador de e-mail: Hostinger Mail.
- Remetente externo utilizado para validação: Gmail institucional de teste.

## 3. Critérios exigidos

O teste somente poderia ser considerado concluído se o processo demonstrasse, de ponta a ponta:

`RECEIPT -> TRIAGE -> CLASSIFICATION -> ACTION/DECISION -> RESPONSE -> CLOSURE`

A resposta operacional deveria conter:

1. classificação `solicitação sintética de direitos / teste RP-002`;
2. identificador `TEST-PRIV-001`;
3. resultado da busca — encontrado ou não encontrado;
4. ação ou decisão decorrente do resultado;
5. status final `ENCERRADO`.

## 4. Evidência observada em 27/08/2026

### 4.1 Recebimento

A mailbox `privacidade@guivos.com` recebeu o pedido sintético e a mensagem complementar relacionada ao mesmo caso.

### 4.2 Triagem e classificação

O caso foi tratado como `solicitação sintética de direitos / teste RP-002` e associado ao identificador `TEST-PRIV-001`.

### 4.3 Busca

Resultado registrado: `não encontrado`.

Nenhum registro real correspondente ao identificador sintético foi localizado.

### 4.4 Ação / decisão

Como nenhum registro real foi localizado:

- nenhuma alteração de dados pessoais reais foi necessária;
- nenhuma exclusão, correção ou outra ação sobre dados reais foi executada.

### 4.5 Resposta

A resposta foi enviada pela própria mailbox oficial `privacidade@guivos.com` ao remetente externo.

O operador retornou status HTTP `204` para a operação de envio e salvou cópia na pasta `Sent`.

### 4.6 Retorno externo

O Gmail externo recebeu a resposta enviada por `privacidade@guivos.com` com os campos exigidos.

### 4.7 Encerramento

Status final comunicado: `ENCERRADO`.

## 5. Resultado do gate

`P2C — Processo sintético de exercício de direitos: PASS`

A evidência comprova o ciclo operacional completo exigido para o teste sintético do RP-002.

## 6. Limites desta evidência

Este PASS:

- comprova o processo sintético testado;
- comprova a capacidade operacional do canal oficial utilizado;
- não constitui parecer jurídico;
- não substitui a validação final de base legal, retenção, Notice ou demais controles de privacidade;
- não libera, isoladamente, Participante 001;
- não libera, isoladamente, o Dry Run Real.

## 7. Estado relacionado após o fechamento

- `P2C`: PASS.
- `P3-C`: HOLD.
- `P3-D`: HOLD.
- `P4`: HOLD.
- `Participant 001`: HOLD.
- `Dry Run Real`: NOT RELEASED.

## 8. Próxima dependência

O fechamento de P2C remove este blocker específico, mas a liberação operacional do RP-002 continua condicionada aos demais gates ainda em HOLD, incluindo a conclusão do A1 da mailbox de Research e os controles subsequentes da arquitetura-alvo aprovada.
