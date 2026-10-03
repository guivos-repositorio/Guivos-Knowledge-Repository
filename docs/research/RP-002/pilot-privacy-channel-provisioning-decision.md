---
id: RP-002-PILOT-PRIV-CH-DEC-001
title: Piloto — Decisão de Provisionamento do Canal de Privacidade
status: active
version: 1.0.1
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: operational_decision_approved_pending_provisioning
related:
  - RP-002-PILOT-CTRL-DEC-001
  - RP-002-PILOT-PRIV-001
  - RP-002-PILOT-OP-001
  - RP-002-PMF-001
---

# Piloto — Decisão de Provisionamento do Canal de Privacidade

## 1. Finalidade

Este documento registra a decisão operacional autorizada sobre **como deverá ser materializado o canal oficial de privacidade e exercício de direitos do titular** para o Dry Run Real e o piloto `RP-002`.

Ele não declara que o canal já existe.

A função deste registro é transformar o blocker genérico `P2B — Canal oficial de privacidade` em uma pendência operacional objetiva, verificável e testável.

## 2. Contexto verificado

A auditoria anterior registrou que:

- `Guivos Ltda — CNPJ 43.530.598/0001-33` é a identidade institucional pública verificada;
- Guivos Ltda foi posteriormente formalmente designada controladora do piloto em `RP-002-PILOT-CTRL-DEC-001`;
- não havia sido localizado um canal explicitamente designado para privacidade/direitos do titular;
- não se deveria transformar automaticamente e-mail comercial, suporte, WhatsApp ou contato genérico em canal de privacidade.

Verificação operacional adicional realizada em 27/08/2026 encontrou evidência de uso real de endereço sob o domínio `@guivos.com`, mas **não encontrou evidência operacional suficiente para tratar como canais atuais**:

```text
privacidade@guivos.com
privacy@guivos.com
dpo@guivos.com
```

Essa ausência de evidência não prova tecnicamente que tais aliases jamais tenham sido configurados em algum provedor; ela apenas significa que **não existe evidência suficiente, nas fontes verificadas, para tratá-los como canais operacionais atuais**.

Por minimização, o GKR não precisa registrar o endereço individual usado apenas para confirmar que o domínio possui uso operacional.

## 3. Decisão de arquitetura do canal

Fica aprovada a seguinte direção:

```text
TIPO
→ canal dedicado de privacidade

DOMÍNIO
→ @guivos.com

IDIOMA PRIMÁRIO DO ALIAS
→ português

ALIAS-ALVO
→ privacidade@guivos.com

CONTROLADOR
→ Guivos Ltda

ESCOPO INICIAL
→ Dry Run Real e piloto RP-002

ESTADO DO ALIAS
→ TARGET APPROVED / NOT YET VERIFIED AS PROVISIONED
```

A escolha de `privacidade@guivos.com` como alias-alvo é uma **decisão de governança e nomenclatura**, e não uma declaração de que a caixa, alias ou roteamento já esteja tecnicamente criado.

## 4. Por que `privacidade@guivos.com`

Para o primeiro piloto, o canal deve ser:

- semanticamente explícito;
- fácil de encontrar e compreender por Pessoas no Brasil;
- independente de uma pessoa física específica;
- transferível entre responsáveis internos sem alterar o endereço público;
- adequado para constar em aviso de privacidade, política, convite e materiais do piloto;
- compatível com crescimento futuro da operação de privacidade.

Nenhum endereço individual já existente será promovido a canal oficial de direitos do titular apenas por estar operacional.

Regra:

> **canal institucional de privacidade deve sobreviver à troca de operador humano.**

## 5. Estado do gate P2B

A decisão de alias reduz incerteza, mas **não fecha o gate**.

Estado vigente:

```text
P2B-1 — ARQUITETURA / NOMENCLATURA DO CANAL
→ PASS

P2B-2 — ALIAS / CAIXA EFETIVAMENTE PROVISIONADO
→ HOLD

P2B-3 — ENTREGA DE MENSAGEM VALIDADA
→ HOLD

P2B-4 — MONITORAMENTO / OWNER OPERACIONAL DEFINIDO
→ HOLD

P2B — CANAL OFICIAL DE PRIVACIDADE
→ HOLD
```

`P2B` somente poderá ser promovido a `PASS` quando todos os subgates críticos estiverem verificados na prática.

## 6. Requisitos mínimos de provisionamento

O canal deverá existir tecnicamente como uma das formas abaixo:

1. caixa postal própria;
2. alias com entrega confiável a uma caixa monitorada;
3. grupo/distribution address com acesso restrito e owner definido.

A escolha técnica pode variar, desde que preserve:

- recebimento confiável;
- rastreabilidade mínima;
- controle de acesso;
- continuidade operacional;
- possibilidade de remoção de acesso quando alguém deixa a função;
- não exposição desnecessária de dados pessoais.

## 7. Owner operacional

O controlador permanece:

```text
GUIVOS LTDA
```

Para o período inicial do piloto, deve existir uma função operacional responsável por monitorar o canal.

Até que uma pessoa/função seja explicitamente atribuída e confirmada, o estado permanece:

```text
PRIVACY CHANNEL OWNER
→ TBD / HOLD
```

O owner operacional não se confunde com o controlador.

## 8. Processo mínimo de atendimento

O canal deverá suportar o seguinte fluxo:

```text
RECEBER SOLICITAÇÃO
↓
REGISTRAR DATA E TIPO
↓
VALIDAR ESCOPO / IDENTIDADE NA MEDIDA NECESSÁRIA
↓
LOCALIZAR DADOS OU REGISTRO RELACIONADO
↓
EXECUTAR AÇÃO CABÍVEL
↓
RESPONDER À PESSOA
↓
REGISTRAR FECHAMENTO
```

Tipos mínimos previstos:

- esclarecimento sobre tratamento;
- confirmação/acesso;
- correção;
- oposição/limitação quando aplicável;
- exclusão quando cabível;
- revogação de consentimento quando esse for o fundamento aplicável à operação em questão;
- informação sobre compartilhamento;
- incidente ou preocupação de privacidade.

Este documento não define a base legal do piloto.

## 9. Teste obrigatório antes de PASS

Antes da entrada de `Participant 001`, deverá ser executado um teste sintético controlado.

### Teste T-PRIV-001

```text
REMETENTE DE TESTE
→ endereço externo ao domínio Guivos

DESTINO
→ privacidade@guivos.com

ASSUNTO
→ Teste sintético — solicitação de privacidade RP-002

CONTEÚDO
→ pedido fictício sem dados pessoais reais de participante
```

O teste deverá comprovar:

1. mensagem recebida;
2. owner consegue acessar;
3. mensagem não cai silenciosamente em spam/quarentena sem processo de recuperação;
4. resposta pode ser enviada pelo canal ou por fluxo oficial claramente relacionado;
5. registro mínimo do pedido pode ser mantido;
6. o pedido pode ser encerrado.

Resultado esperado:

```text
DELIVERY
→ PASS

ACCESS
→ PASS

RESPONSE
→ PASS

CLOSURE
→ PASS
```

## 10. Teste de continuidade

Além do primeiro envio, deve ser verificado que o canal não depende exclusivamente de credencial pessoal irreversível.

Critério:

> **se o operador atual ficar indisponível, Guivos Ltda deve conseguir reassumir o canal sem alterar o endereço informado ao participante.**

## 11. Publicação e transparência

Após provisionamento e antes da coleta real, o canal deverá aparecer nos materiais aplicáveis do piloto, incluindo pelo menos:

- aviso de privacidade do piloto;
- material de informação/recrutamento quando houver coleta posterior;
- instruções de exercício de direitos;
- política pública, se a revisão concluir que ela deve ser atualizada para cobrir o RP-002.

A simples existência técnica do alias, sem ser comunicado à Pessoa, não satisfaz transparência.

## 12. Relação com P2C

Mesmo depois de o endereço existir, `P2C — Processo de direitos testado no canal real` continua separado.

Estados possíveis:

```text
ALIAS CRIADO
+
ENTREGA FUNCIONA
≠
PROCESSO DE DIREITOS COMPLETO
```

`P2C` requer execução do ciclo sintético de ponta a ponta.

## 13. Relação com base legal

Esta decisão não promove `P4 — Base legal`.

Ainda será necessário definir, com base nas operações reais:

- quais dados serão coletados;
- para quais finalidades;
- quais tratamentos dependem de qual fundamento;
- quais tratamentos são opcionais;
- como retirada/revogação afetará o piloto quando aplicável;
- quais dados deverão ser mantidos por obrigação ou defesa de direitos, quando aplicável.

Estado:

```text
P4 — BASE LEGAL
→ HOLD
```

## 14. Relação com encarregado / DPO

A existência do canal dedicado não decide, sozinha, a aplicabilidade ou obrigatoriedade de encarregado/DPO.

Estado preservado:

```text
ENCARREGADO / DPO
→ APPLICABILITY REVIEW REQUIRED
```

O alias `privacidade@guivos.com` poderá funcionar como porta de entrada institucional independentemente de quem venha a exercer a função operacional adequada, desde que a governança aplicável esteja correta.

## 15. Dados que não devem entrar no GKR

Mesmo após o canal ser criado, o GKR não deve armazenar:

- mensagens reais de titulares;
- nomes de participantes;
- e-mails pessoais;
- pedidos de acesso/correção/exclusão individualizados;
- conteúdo de incidentes com identificação pessoal;
- credenciais;
- tokens;
- configurações secretas do provedor de e-mail.

O GKR poderá registrar somente estados agregados e operacionais, por exemplo:

```text
T-PRIV-001
→ PASS

CANAL
→ OPERATIONAL

OWNER ROLE
→ ASSIGNED
```

sem copiar conteúdo pessoal.

## 16. Atualização consolidada de prontidão

Após esta decisão:

```text
P1A — IDENTIDADE INSTITUCIONAL
→ PASS

P1B — CONTROLADOR FORMAL
→ PASS

P2B-1 — DESENHO DO CANAL
→ PASS

P2B-2 — PROVISIONAMENTO REAL
→ HOLD

P2B-3 — TESTE DE ENTREGA
→ HOLD

P2B-4 — OWNER OPERACIONAL
→ HOLD

P2B — CANAL OFICIAL DE PRIVACIDADE
→ HOLD

P2C — PROCESSO DE DIREITOS TESTADO
→ HOLD

P3 — FINALIDADES / CATEGORIAS
→ PENDING FINALIZATION

P4 — BASE LEGAL
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

## 17. Critério exato para promoção de P2B

`P2B` poderá mudar de `HOLD` para `PASS` somente após evidência operacional de:

```text
privacidade@guivos.com
→ provisionado
→ recebendo mensagens externas
→ owner atribuído
→ acesso controlado
→ continuidade garantida
→ comunicado como canal oficial
```

## 18. Próxima ação operacional fora do GKR

A próxima ação não é documental.

É necessária a materialização técnica do alias/canal no provedor real de e-mail/DNS utilizado pela Guivos.

O GKR não deve marcar essa ação como concluída por intenção.

Somente após o provisionamento real deve ser executado `T-PRIV-001` e atualizado o estado de `P2B`.

## 19. Regra final

> **Decidir o nome do canal reduz ambiguidade. Criar, monitorar e testar o canal produz prontidão operacional.**

Portanto, esta decisão avança a arquitetura de privacidade sem produzir um `PASS` artificial.