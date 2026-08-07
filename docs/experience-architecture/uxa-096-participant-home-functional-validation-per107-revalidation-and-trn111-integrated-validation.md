---
id: UXA-096
title: Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de TRN-111
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-016
  - UXA-018
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-094
  - UXA-095
related:
  - GKR-SURF-PER-107
  - GKR-SURF-PER-108
  - GKR-TRN-110
  - GKR-TRN-111
  - M7.83
normative: false
---

# Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de TRN-111

## 1. Finalidade

A UXA-096 valida a referência móvel vigente de `GKR-SURF-PER-108 — Início do Participante`, revalida a versão corrente de `GKR-SURF-PER-107 — Central de Atualizações` reformulada pela UXA-095 e examina `GKR-TRN-111` ponta a ponta.

A frente não materializa novos estados, superfícies, transições ou áreas P1. Reformulações são permitidas somente quando necessárias para fechar lacunas da validação.

## 2. Baseline

A iniciativa parte da `main` após UXA-095:

- GKR-STATE 2.21.0;
- M7.82;
- 108 SVGs;
- 108 associações;
- 28 perfis;
- 96 validações funcionais vigentes;
- 12 pendências = 10 UXA-055 + `PER-107` corrente + `PER-108`;
- `TRN-110` integralmente validada;
- `TRN-111` parcial;
- Pessoa e Coletivo em `draft`;
- Engenharia de Produto pausada antes de W0-01.

## 3. Lacunas encontradas

A inspeção da materialização UXA-095 identificou três lacunas relevantes.

### 3.1 Evento histórico não pode conceder acesso

O CTA `Abrir início do Coletivo` aparecia dentro de um item histórico de confirmação. Sem uma regra explícita, uma atualização antiga poderia sugerir acesso mesmo após pausa, saída, remoção ou perda de permissão.

**Reformulação:** `PER-107` passa a mostrar o estado atual do vínculo e declara que o acesso ao Início é revalidado ao abrir. O histórico não preserva acesso.

### 3.2 Terminologia de participação

`PER-108` utilizava `membro` como termo genérico. O contrato UXA-056 preserva `participante confirmado` como estado funcional canônico e admite `membro` apenas quando fizer sentido para o Coletivo e sua regra estiver clara.

**Reformulação:** a superfície passa a declarar `vínculo atual: participante confirmado` e `papel: participante`.

### 3.3 Contestação não é edição da fonte

O comando `Corrigir ou contestar` poderia sugerir capacidade de alterar diretamente uma informação oficial.

**Reformulação:** o comando passa a `Informar problema ou contestar`, preservando a autoridade da fonte e o direito de contestação.

## 4. Validação funcional de PER-107 corrente

A versão corrente da Central é aprovada porque:

1. origem, natureza, contexto, autoridade, data, leitura, ação e prazo permanecem distinguíveis;
2. segurança material continua acima de ação comum;
3. confirmação de leitura continua separada de consentimento, presença ou conclusão;
4. preferências não ocultam indevidamente aviso essencial;
5. `Abrir início do Coletivo` é ação opcional e neutra;
6. o CTA depende do **vínculo atual**, não do fato histórico que originou o item;
7. pausa, encerramento, remoção ou perda de permissão prevalecem sobre uma atualização antiga;
8. abrir o Início não altera leitura, papel, presença, disponibilidade ou autoridade;
9. repetição de abertura/leitura é idempotente;
10. ações substantivas revalidam estado e permissão antes do efeito.

Resultado de `PER-107`: **validado na versão corrente após reformulação controlada**.

`TRN-110` permanece integralmente validada; a reformulação não altera seu contrato de entrada neutra na Central.

## 5. Validação funcional de PER-108

A referência do Início é aprovada porque preserva separadamente:

- propósito do Coletivo;
- estado atual do vínculo;
- papel atual;
- função aceita;
- autoridade;
- momento coletivo e fonte;
- próxima atividade e presença;
- consulta, contribuição e autoridade decisória;
- áreas internas especializadas;
- notificações, pausa, saída, denúncia e proteção.

### 5.1 Invariantes validados

- participante confirmado não implica função aceita;
- função aceita não implica autoridade;
- abrir a superfície não confirma presença;
- vínculo não cria obrigação de participar de atividade;
- contribuição em consulta permanece opcional quando o contrato assim define;
- consulta não converte volume de participação em autoridade decisória;
- síntese do momento não substitui fonte ou Central;
- a Pessoa pode informar problema ou contestar sem editar a fonte oficial;
- atalhos internos não concedem acesso além das permissões atuais;
- retorno à Central não altera leitura;
- estado antigo não preserva permissões;
- silêncio, pausa, saída ou baixa frequência não criam punição reputacional;
- o Início não é feed, ranking, painel de dedicação ou réplica dos canais P1.

Resultado de `PER-108`: **validado após reformulação controlada**.

## 6. Contrato integrado de TRN-111

A continuidade validada é:

```text
PER-107 — Central de Atualizações
→ Pessoa escolhe “Abrir início do Coletivo”
→ vínculo atual e permissão são revalidados
→ evento histórico não concede nem preserva acesso
→ abertura não altera leitura, vínculo, papel, presença, disponibilidade ou autoridade
→ PER-108 — Início do Participante
→ mesmo Coletivo e mesmo vínculo lógico permanecem em contexto
```

### 6.1 Identidade e contexto

A transição preserva:

- identidade do Coletivo;
- identidade lógica do vínculo;
- estado canônico vigente do vínculo;
- permissões contextuais atuais.

Uma atualização antiga pode permanecer no histórico, mas não é autoridade para acesso.

### 6.2 Concorrência e estado obsoleto

Se o vínculo mudar entre a renderização da Central e a abertura do Início:

1. o estado canônico mais recente prevalece;
2. vínculo pausado ou encerrado não é tratado como participação ativa;
3. remoção ou perda de permissão bloqueia conteúdo protegido correspondente;
4. ações internas abertas com estado antigo são revalidadas antes do efeito;
5. a interface deve atualizar, restringir ou redirecionar conforme o novo estado, sem preservar privilégio anterior.

### 6.3 Retorno

Retornar de `PER-108` para `PER-107`:

- não marca automaticamente novos itens como lidos;
- não desfaz confirmação explícita de leitura já realizada;
- não altera vínculo, papel, presença, disponibilidade ou autoridade;
- não cria nova entrada, novo vínculo ou nova solicitação;
- preserva o contexto navegacional quando ainda permitido.

### 6.4 Idempotência e repetição

Abrir, voltar, recarregar ou repetir a navegação:

- não cria efeito substantivo duplicado;
- não duplica vínculo;
- não duplica leitura;
- não cria função, presença ou autoridade;
- não restaura permissão revogada.

## 7. Veredito

> **Aprovada após reformulação controlada e validação integrada de `GKR-TRN-111`.**

Com a UXA-096:

- `PER-107` corrente passa a validado;
- `PER-108` passa a validado;
- `TRN-111` passa de parcial para **integralmente validada**;
- `TRN-110` permanece integralmente validada;
- os oito handoffs `105`, `106`, `107`, `108`, `109`, `110`, `111` e `112` ficam integralmente validados no trecho governado de Coletivos.

## 8. Efeito na cobertura

Após eventual integração:

- SVGs: **108**;
- associações: **108**;
- perfis: **28**;
- validações funcionais vigentes de SVG: **98**;
- pendências específicas: **10**, exclusivamente UXA-055;
- IDs com referência visual: **30/40**;
- responsabilidades sem SVG dedicado: **9**;
- superfícies: **40**;
- transições: **37**;
- handoffs integralmente validados no trecho de Coletivos: **8**.

Nenhum SVG novo, ID novo ou transição nova é criado pela UXA-096.

## 9. Limites preservados

Esta frente não:

- materializa estados P0B do Início, Meus Coletivos ou Central;
- materializa áreas P1 especializadas;
- valida todas as áreas internas acessíveis a partir de `PER-108`;
- promove a Jornada da Pessoa ou a Jornada do Coletivo para além de `draft`;
- resolve as dez pendências UXA-055;
- inicia protótipo navegável, teste com pessoas, W0-01 ou Engenharia de Produto;
- declara implementação de API, sessão, autorização ou controle de concorrência.

## 10. Próxima frente possível

A próxima frente só deverá ser definida após sincronização do estado pós-UXA-096. Nenhuma UXA-097 é iniciada por este documento.
