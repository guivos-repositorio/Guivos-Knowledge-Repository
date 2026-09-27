---
id: GKR-UX-OPPORTUNITY-POST-SUBMIT-BILATERAL-CONTINUITY-001
title: Oportunidades Internas — Continuidade Bilateral Pós-Envio — Contrato Funcional Candidato
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: functional_contract_candidate
depends_on:
  - GKR-UX-PERSON-INTERNAL-OPPORTUNITY-APPLICATION-CONTRACT-001
  - GKR-UX-ORG-OPPORTUNITY-APPLICATIONS-CONTRACT-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# Oportunidades Internas — Continuidade Bilateral Pós-Envio — Contrato Funcional Candidato

## 1. Finalidade

Este contrato define a continuidade funcional do mesmo objeto bilateral interno depois do envio inicial consciente da Pessoa.

Ele não cria superfície, não adjudica `GKR-TRN-*` e não transforma toda atualização de estado em transição.

```text
TRN-213
→ ENVIO INICIAL PER-204 → ORG-008
→ PRESERVADO

PÓS-ENVIO
→ MESMO OBJETO BILATERAL
→ DUAS AUTORIDADES
→ EVENTOS MATERIAIS EXPLÍCITOS
→ IDs DE TRANSIÇÃO AINDA NÃO ADJUDICADOS
```

## 2. Fronteira de responsabilidade

`PER-204` governa a experiência da Pessoa sobre manifestação de interesse ou inscrição interna.

`ORG-008` governa a experiência institucional autorizada sobre o recorte recebido desse mesmo objeto.

A continuidade pós-envio não concede a nenhuma das partes acesso irrestrito ao estado privado da outra.

```text
MESMO OBJETO
≠ MESMA PERSPECTIVA

ESTADO BILATERAL
≠ ESTADO INTERNO COMPLETO DA ORGANIZAÇÃO

DADO EXISTENTE
≠ DADO AUTORIZADO A ATRAVESSAR A FRONTEIRA
```

## 3. Organização → Pessoa

Uma continuidade material da Organização para a Pessoa existe quando uma mudança sob autoridade de `ORG-008` precisa alterar legitimamente o estado compreensível ou acionável em `PER-204`.

Eventos candidatos incluem, quando aplicáveis:

- confirmação material de recebimento;
- solicitação legítima de complemento;
- correção institucional que afete a compreensão da Pessoa;
- mudança material que exija ação da Pessoa;
- decisão institucional comunicável;
- cancelamento ou encerramento com fundamento;
- atualização necessária para resolver estado anteriormente indeterminado.

Não constituem, por si sós, nova continuidade material:

- abrir ou consultar o objeto;
- filtrar ou ordenar objetos;
- navegação interna da Organização;
- nota interna não compartilhável;
- avaliação protegida;
- mudança de interface sem mudança bilateral confirmada.

## 4. Pessoa → Organização após o envio inicial

Depois de `TRN-213`, uma nova continuidade material da Pessoa para a Organização existe somente quando uma ação consciente em `PER-204` altera legitimamente o objeto que `ORG-008` pode receber.

Eventos candidatos incluem, quando aplicáveis:

- resposta a solicitação legítima de complemento;
- correção autorizada de informação própria;
- fornecimento adicional autorizado para a mesma finalidade;
- retirada de manifestação;
- cancelamento ou retirada de inscrição;
- contestação ou resposta material que deva integrar o objeto bilateral.

Não constituem, por si sós, nova continuidade material:

- abrir `PER-204`;
- consultar estado;
- retornar a `PER-203`;
- navegar pela Journey;
- editar rascunho ainda não enviado;
- desistir antes de uma nova submissão material.

## 5. Regra de materialidade

Uma mudança atravessa a fronteira somente quando satisfaz cumulativamente:

1. existe evento real no objeto bilateral;
2. a parte de origem possui autoridade para produzi-lo;
3. a parte de destino possui finalidade legítima para recebê-lo;
4. o evento altera estado, informação ou ação material do destino;
5. o recorte de dados é necessário e autorizado;
6. há proveniência suficiente;
7. o evento não pode ser representado legitimamente como simples navegação ou estado local.

Ausência de qualquer critério preserva o evento no contexto local ou como estado indeterminado.

## 6. Payload mínimo

A continuidade material deve carregar somente o necessário para interpretar o evento, conforme aplicável:

- referência estável do objeto bilateral;
- oportunidade correspondente;
- tipo de evento;
- origem/autoria institucional ou da Pessoa;
- instante material quando necessário;
- estado bilateral resultante ou sinal de indeterminação;
- recorte de informação conscientemente fornecido ou legitimamente comunicável;
- referência à solicitação anterior quando houver resposta;
- consequência ou ação requerida quando aplicável;
- proveniência e evidência mínima de processamento.

Não atravessam automaticamente:

- Journey completa;
- contexto privado de personalização;
- notas internas;
- avaliações protegidas;
- dados de terceiros;
- score/ranking;
- inferências não autorizadas;
- campos não necessários à finalidade.

## 7. Solicitação de complemento

Solicitação de complemento é evento material somente quando:

- a informação é necessária;
- a finalidade permanece compatível;
- a Organização possui autoridade;
- a Pessoa consegue compreender o que é pedido e por quê;
- recusa ou ausência de resposta possui consequência explicável quando aplicável.

Nova finalidade ou novo recorte incompatível não pode ser tratado como simples complemento.

A resposta da Pessoa é evento material separado da solicitação e exige ação consciente.

## 8. Decisão e comunicação

Decisão institucional atravessa para `PER-204` somente quando pertence à autoridade da Organização e é legitimamente comunicável.

```text
DECISÃO COMUNICADA
≠ PARTICIPAÇÃO

ACEITE/SELEÇÃO
≠ RESULTADO FINAL

ESTADO INTERNO
≠ DIREITO AUTOMÁTICO DE EXPOSIÇÃO
```

Motivos protegidos, dados de terceiros ou lógica privada não atravessam sem fundamento próprio.

## 9. Retirada, cancelamento e encerramento

Retirada iniciada pela Pessoa e cancelamento/encerramento iniciado pela Organização são eventos distintos, com proveniência preservada.

Nenhum deles deve ser reescrito como recusa da outra parte.

A continuidade deve distinguir:

- quem iniciou;
- qual objeto foi afetado;
- qual estado bilateral resultou;
- quais efeitos ainda permanecem legítimos;
- se há retenção necessária e explicável.

## 10. Confirmação, idempotência e concorrência

Cada evento material deve suportar processamento idempotente.

```text
RETRY
≠ NOVO EVENTO MATERIAL

ENVIO LOCAL
≠ RECEBIMENTO CONFIRMADO

INTERFACE ATUALIZADA
≠ ESTADO BILATERAL CONFIRMADO
```

Duplicidade, concorrência, falha parcial ou confirmação ausente devem preservar o último estado confirmado e usar estado indeterminado quando necessário.

Eventos conflitantes exigem reconciliação sem fabricação de ordem, decisão ou sucesso.

## 11. Navegação e retornos contextuais

Este contrato não adjudica transições para:

- `PER-204 → PER-203`;
- `ORG-008 → ORG-003`.

Esses retornos permanecem contextuais enquanto não houver evidência de mudança de responsabilidade que exija transição própria.

## 12. Critério para futura adjudicação de TRN

A direção `ORG-008 → PER-204` pode justificar uma transição própria se a continuidade material descrita neste contrato for confirmada como handoff estável entre responsabilidades.

A direção `PER-204 → ORG-008` pós-envio pode justificar outra transição própria se ficar demonstrado que não é apenas repetição de `TRN-213`, mas uma continuidade recorrente com semântica própria.

Nenhum número é reservado neste documento.

```text
GKR-TRN-215
→ NÃO ADJUDICADA

GKR-TRN-216
→ NÃO ADJUDICADA
```

## 13. Não criado por este contrato

Este contrato não cria:

- nova superfície;
- campos/documentos específicos por oportunidade;
- critérios de elegibilidade ou seleção;
- automação decisória;
- score/ranking;
- notificações;
- integração externa;
- entitlement por plano;
- analytics/KPI;
- retorno dedicado;
- baseline visual;
- protótipo;
- implementação técnica.

## 14. Estado

```text
OBJETO BILATERAL PÓS-ENVIO
→ CONTRATO FUNCIONAL CANDIDATO

PER-204
→ PRESERVADA

ORG-008
→ PRESERVADA

TRN-213
→ PRESERVADA / ENVIO INICIAL

NOVOS TRN IDs
→ NONE

VISUAL BASELINE
→ NONE

PROTOTYPE
→ NOT AUTHORIZED

PRODUCT ENGINEERING
→ NOT RELEASED
```
