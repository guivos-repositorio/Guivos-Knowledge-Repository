---
id: GKR-UX-PERSON-INTERNAL-OPPORTUNITY-APPLICATION-CONTRACT-001
title: Jornada da Pessoa — Manifestação de Interesse e Inscrição Interna em Oportunidades — Contrato Funcional Candidato
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: functional_contract_candidate
depends_on:
  - GKR-UX-PUBLISHER-APPLICATION-CONTRACT-001
  - GKR-UX-PER203-MASTER-001
  - GKR-JOURNEY-PERSON-FUNCTIONAL-COMPLETENESS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# Jornada da Pessoa — Manifestação de Interesse e Inscrição Interna em Oportunidades — Contrato Funcional Candidato

## 1. Finalidade

Este documento define a responsabilidade funcional candidata da perspectiva da Pessoa quando uma oportunidade permitir manifestação de interesse ou inscrição **dentro da Guivos**.

A adjudicação posterior confirmou esta responsabilidade como `GKR-SURF-PER-204`, preservando o contrato funcional aqui definido.

```text
CONTRATO FUNCIONAL
≠ NOVO PER-ID AUTOMÁTICO

MUDANÇA DE RESPONSABILIDADE
≠ TRN-ID AUTOMÁTICO

PROCESSO INTERNO
≠ BND-001
```

A identidade canônica corrente é `GKR-SURF-PER-204`. A entrada interna a partir de `PER-203` é `GKR-TRN-212`; a continuidade externa por `TRN-205 → BND-001` permanece separada.

## 2. Origem e fronteira com PER-203

`PER-203 — Detalhe de Oportunidade` permanece responsável por compreensão, condições materiais, relevância contextual autorizada, salvar, comparar e revisão de saída externa.

Quando a oportunidade oferecer processo interno legítimo, a Pessoa pode iniciar conscientemente uma continuidade própria.

```text
PER-203
→ OPORTUNIDADE COM PROCESSO INTERNO LEGÍTIMO
→ AÇÃO CONSCIENTE
→ TRN-212
→ PER-204 — MANIFESTAÇÃO DE INTERESSE / INSCRIÇÃO INTERNA
```

Abrir ou visualizar `PER-203` não cria interesse, inscrição ou candidatura.

A continuidade externa permanece:

```text
PER-203
→ TRN-205
→ BND-001
→ AUTORIDADE EXTERNA
```

## 3. Job próprio

A responsabilidade candidata permite que a Pessoa:

1. escolha conscientemente manifestar interesse ou inscrever-se quando o modo estiver disponível;
2. compreenda o publicador, a finalidade e os dados envolvidos;
3. revise o que será compartilhado;
4. forneça somente informações legitimamente necessárias;
5. autorize e envie conscientemente;
6. acompanhe o estado material do objeto interno;
7. responder a solicitação legítima de informação quando aplicável;
8. corrigir informação própria quando permitido;
9. retirar manifestação ou inscrição quando permitido;
10. compreender decisão ou encerramento sem promessa de resultado;
11. retornar à oportunidade e à Journey sem perder contexto legítimo.

Esse job persiste além do ato inicial de `PER-203`; por isso foi adjudicado como responsabilidade própria em `PER-204` e não deve ser absorvido por conveniência pelo Detalhe.

## 4. Dois modos, dois objetos

### 4.1 Manifestação de interesse

É intenção leve, consciente e reversível quando legitimamente oferecida.

Ciclo candidato:

```text
NÃO MANIFESTADO
→ REVISÃO MÍNIMA
→ CONFIRMAÇÃO CONSCIENTE
→ PROCESSAMENTO
→ INTERESSE CONFIRMADO
→ ACOMPANHAMENTO QUANDO MATERIAL
→ RETIRADA QUANDO APLICÁVEL
```

Manifestação de interesse:

```text
≠ INSCRIÇÃO
≠ CANDIDATURA
≠ ELEGIBILIDADE
≠ SELEÇÃO
≠ PARTICIPAÇÃO
```

Ela não autoriza automaticamente perguntas adicionais, formulário de inscrição, avaliação seletiva ou uso secundário dos dados.

### 4.2 Inscrição

É submissão consciente de um conjunto definido de informações para finalidade identificada.

Ciclo candidato:

```text
INTENÇÃO DE INSCREVER-SE
→ COMPREENSÃO DA FINALIDADE
→ PREENCHIMENTO / FORNECIMENTO LEGÍTIMO
→ REVISÃO PRÉ-ENVIO
→ AUTORIZAÇÃO
→ ENVIO
→ PROCESSAMENTO
→ RECEBIMENTO CONFIRMADO OU ESTADO INDETERMINADO
→ ACOMPANHAMENTO
→ SOLICITAÇÃO DE INFORMAÇÃO QUANDO LEGÍTIMA
→ DECISÃO / ENCERRAMENTO QUANDO APLICÁVEL
```

Inscrição não significa elegibilidade, seleção, participação ou resultado.

## 5. Revisão pré-envio

Antes de qualquer envio material, a Pessoa deve compreender, conforme aplicável:

- qual oportunidade está em causa;
- quem é o publicador responsável;
- se a ação é manifestação de interesse ou inscrição;
- finalidade do compartilhamento;
- quais dados serão enviados;
- quais informações são obrigatórias ou opcionais quando legitimamente definidas;
- autorizações aplicáveis;
- consequência imediata do envio;
- possibilidade de corrigir, cancelar ou retirar quando existente;
- que envio não garante elegibilidade, seleção, participação ou resultado.

Ausência de ação, navegação, salvamento, tempo de permanência ou explicação de relevância não equivalem a autorização.

## 6. Dados e minimização

O objeto da Pessoa pode utilizar somente dados necessários, autorizados e proporcionais ao modo.

```text
DADO NA JOURNEY
≠ DADO DA INSCRIÇÃO

DADO USADO PARA PERSONALIZAÇÃO
≠ DADO COMPARTILHÁVEL COM PUBLICADOR

INFERÊNCIA GUIVOS
≠ DECLARAÇÃO DA PESSOA
```

Não atravessam por padrão: Journey completa, objetivos privados não necessários, Próximos Passos, histórico amplo, razões internas de recomendação, inferências, perfil psicológico, outras relações, itens salvos/comparados, navegação desnecessária, score, ranking ou reputação.

## 7. Autoridade

```text
AUTENTICAÇÃO
≠ AUTORIZAÇÃO DE ENVIO

AUTORIZAÇÃO DE ENVIO
≠ CONSENTIMENTO PARA MARKETING

INSCRIÇÃO
≠ ACESSO À JOURNEY

INSCRIÇÃO
≠ VÍNCULO PERMANENTE
```

A Pessoa conserva autoridade sobre informações próprias dentro dos limites legais e operacionais aplicáveis. O publicador recebe apenas o recorte autorizado pelo contrato bilateral.

## 8. Estados funcionais candidatos

Os estados devem ser usados apenas quando o modo e a oportunidade os legitimarem.

Podem incluir:

- intenção não enviada;
- revisão pré-envio;
- processamento;
- enviado;
- recebimento confirmado;
- falha recuperável;
- estado indeterminado;
- informação adicional solicitada;
- aguardando ação da Pessoa;
- em análise;
- decisão pendente;
- aceito/selecionado quando a autoridade do publicador sustentar essa decisão;
- não selecionado/recusado;
- retirado pela Pessoa;
- cancelado pelo publicador com base legítima;
- expirado;
- bloqueado por proteção, privacidade ou autoridade;
- contestado;
- encerrado.

A manifestação de interesse não herda automaticamente os estados seletivos da inscrição.

## 9. Processamento, confirmação e duplicidade

```text
INTENÇÃO
≠ ENVIO

ENVIO
≠ RECEBIMENTO CONFIRMADO

RECEBIMENTO
≠ ANÁLISE

ANÁLISE
≠ DECISÃO

DECISÃO
≠ PARTICIPAÇÃO
≠ RESULTADO
```

Quando não houver confirmação suficiente, a experiência deve assumir estado indeterminado em vez de fabricar sucesso ou falha.

Repetição após falha ou incerteza não pode criar objeto bilateral duplicado silenciosamente.

## 10. Acompanhamento e continuidade

Depois do envio confirmado, a Pessoa deve poder compreender o estado material que legitimamente lhe pertence.

O acompanhamento não autoriza revelar processos internos protegidos do publicador, avaliações de terceiros, dados de outras Pessoas ou lógica privada sem fundamento.

Mudanças materiais que exigirem ação da Pessoa devem indicar o que mudou, por que a ação é necessária e qual continuidade legítima existe.

## 11. Correção e informação adicional

Quando permitido:

- a Pessoa pode corrigir informação própria;
- o publicador pode solicitar apenas informação adicional necessária e compatível com a finalidade;
- a Pessoa pode responder, recusar quando houver escolha legítima ou compreender a consequência material da não resposta;
- nova finalidade ou novo recorte de dados exige autoridade própria.

Solicitação adicional não converte manifestação de interesse em inscrição silenciosamente.

## 12. Retirada, cancelamento e reversibilidade

A Pessoa deve poder retirar manifestação ou inscrição quando a natureza do processo permitir.

```text
RETIRAR INTERESSE
≠ CANCELAR INSCRIÇÃO

CANCELAR INSCRIÇÃO
≠ SAIR DA GUIVOS

ENCERRAR PROCESSO
≠ APAGAR AUTOMATICAMENTE TODOS OS DADOS
```

Retenção legítima deve ser explicável e limitada à finalidade/base aplicável. Retirada não pode gerar punição algorítmica artificial em outras oportunidades.

## 13. Falhas e recuperação

Devem existir tratamentos proporcionais para:

- falha antes do envio;
- falha durante processamento;
- confirmação ausente;
- oportunidade alterada ou encerrada;
- autorização insuficiente;
- informação obrigatória legitimamente ausente;
- conflito entre estado local e estado bilateral;
- indisponibilidade temporária;
- tentativa duplicada;
- condição de proteção ou privacidade.

Recuperação deve preservar o trabalho da Pessoa quando legítimo e seguro, sem presumir envio.

## 14. Retorno à oportunidade e à Journey

A Pessoa deve poder retornar à oportunidade e ao contexto anterior quando aplicável.

Retorno não significa:

- desfazer decisão do publicador;
- reabrir processo encerrado;
- restaurar oportunidade expirada;
- converter processo interno em externo;
- confirmar resultado.

`PER-203` permanece referência da oportunidade; `PER-204` governa o objeto bilateral interno. O retorno contextual é necessário, mas não recebe `TRN-213` sem adjudicação própria.

## 15. Relação com relevância

Relevância usada para ajudar a Pessoa a compreender uma oportunidade não atravessa automaticamente para o publicador.

```text
RELEVÂNCIA PARA A PESSOA
≠ SCORE DO CANDIDATO

MATCH
≠ RANKING

EXPLICAÇÃO DE PERTINÊNCIA
≠ CRITÉRIO DE SELEÇÃO
```

Qualquer avaliação institucional futura exige finalidade, dados, autoridade, explicabilidade e contestabilidade próprias.

## 16. Planos e capacidade comercial

Planos podem futuramente governar capacidade operacional quando houver autoridade específica.

Eles não podem, por si só:

- ampliar dados pessoais acessíveis ao publicador;
- mudar finalidade da inscrição;
- criar consentimento;
- alterar organicamente relevância;
- aumentar chance de seleção;
- transformar plano pago em prioridade humana.

```text
PLANO MAIOR
≠ MAIS DIREITO SOBRE DADOS DA PESSOA
```

## 17. Acessibilidade e linguagem

A experiência deve:

- tornar finalidade, publicador, ação e estado compreensíveis;
- não depender apenas de cor, posição ou ícone;
- preservar alternativas de cancelamento/retorno;
- distinguir informação obrigatória de opcional quando legitimamente definida;
- evitar urgência artificial, promessa de seleção ou julgamento de valor humano.

## 18. IA e source lock

IA, designer ou implementação não podem inventar:

- formulário universal;
- campos obrigatórios;
- documentos;
- critérios seletivos;
- score ou ranking;
- decisão automática;
- motivos de recusa;
- novas finalidades;
- novos consentimentos;
- notificações;
- integrações;
- entitlement;
- Surface ID;
- Transition ID.

```text
GAP
→ SINALIZAR
→ NÃO INVENTAR
```

## 19. Identidade adjudicada

A responsabilidade satisfaz os critérios de job próprio, estados persistentes, acompanhamento, correção/retirada, recuperação e continuidade independente do Detalhe. O Registry a identifica como `GKR-SURF-PER-204`.

A mudança consciente de responsabilidade a partir de `PER-203` é `GKR-TRN-212`. Isso não cria inscrição por navegação: a oportunidade deve suportar processo interno legítimo e a Pessoa deve escolher prosseguir conscientemente.

O retorno a `PER-203` continua funcionalmente necessário, mas não recebe identidade de transição dedicada por simetria. `TRN-213` permanece não criado até prova de necessidade própria.

## 20. Lacunas preservadas

Permanecem abertas:

- eventual identidade dedicada para retorno, somente se necessidade própria for comprovada;
- campos e documentos por tipo de oportunidade;
- regras específicas de elegibilidade/seleção;
- notificações;
- integrações;
- retenção quantitativa;
- requisitos jurisdicionais;
- entitlement;
- analytics/KPIs;
- protótipo;
- implementação.

## 21. Estado governado

```text
RESPONSABILIDADE FUNCIONAL DA PESSOA
→ CONTRATO FUNCIONAL CANDIDATO COM IDENTIDADE ADJUDICADA

SURFACE ID
→ GKR-SURF-PER-204

TRANSITION ID DE ENTRADA
→ GKR-TRN-212

TRANSITION ID DE RETORNO DEDICADO
→ NONE / NÃO JUSTIFICADO

PER-203
→ PRESERVADO

TRN-205 / BND-001
→ PRESERVADOS PARA PROCESSO EXTERNO

VISUAL BASELINE
→ NONE

PROTOTYPE
→ NOT AUTHORIZED

PRODUCT ENGINEERING
→ NOT RELEASED
```
