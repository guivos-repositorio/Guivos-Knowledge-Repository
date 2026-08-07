---
id: UXA-094
title: Validação Funcional da Central de Atualizações e Revalidação de GKR-TRN-110
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-091
  - UXA-092
  - UXA-093
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-106
  - GKR-SURF-PER-107
  - GKR-SURF-PER-108
  - GKR-TRN-110
  - GKR-TRN-111
  - GKR-JOURNEY-GAPS-001
  - M7.81
normative: false
---

# Validação Funcional da Central de Atualizações e Revalidação de GKR-TRN-110

## 1. Finalidade

A UXA-094 valida funcionalmente a referência móvel vigente de `GKR-SURF-PER-107 — Central de Atualizações` e examina como um único conjunto a continuidade `GKR-TRN-110 — Meus Coletivos → Central de Atualizações`.

A frente responde:

> **A Pessoa consegue sair de Meus Coletivos, compreender o que exige atenção e retornar sem que abertura, leitura, ordenação, preferência ou repetição de interação alterem silenciosamente vínculo, decisão, presença, prioridade ou estado substantivo?**

## 2. Escopo examinado

Foram examinados em conjunto:

- a versão validada de `GKR-SURF-PER-106 — Meus Coletivos`;
- a versão materializada pela UXA-093 de `GKR-SURF-PER-107 — Central de Atualizações`;
- o contrato funcional UXA-058;
- a entrada, contexto, retorno, leitura, ação, ordenação, preferência, concorrência e idempotência de `GKR-TRN-110`;
- a fronteira explícita com `GKR-SURF-PER-108`, que permanece ausente na forma vigente.

Não foram examinados como superfície completa os estados P0B de vazio, excesso de volume ou baixa conectividade.

## 3. Achados funcionais

### 3.1 Origem sem gatilho explícito

A versão de `PER-106` validada pela UXA-092 declarava que a Central de Atualizações era uma superfície própria, mas não oferecia uma ação explícita para acessá-la.

Isso impedia validar `TRN-110` ponta a ponta, porque o destino existia sem um gatilho observável na origem.

### 3.2 Prioridade visual incompatível com o contrato

Na referência UXA-093, um pedido comum de informação aparecia acima de um alerta de segurança. O contrato UXA-058 estabelece que risco ou segurança material precede ações comuns na ordenação de atenção.

### 3.3 Preferência não operacionalizada

A referência declarava que preferências poderiam influenciar a ordem, mas não apresentava controle compreensível para ajustar itens não essenciais.

Ao mesmo tempo, um alerta essencial de segurança não pode ser silenciosamente ocultado por preferência comum.

### 3.4 Taxonomia parcial sem porta para demais categorias

A referência inicial mostrava apenas parte das categorias previstas pelo contrato. Em tela móvel primária isso é aceitável como recorte, desde que exista acesso explícito às demais categorias sem transformar `Tudo` em categoria opaca.

### 3.5 Fonte e limite do alerta de segurança

O alerta apresentava autoridade e motivo, mas não tornava suficientemente explícita a fonte operacional e a vigência/revisão da informação.

## 4. Reformulação controlada

A UXA-094 reforma exatamente dois SVGs existentes e não cria novo ativo visual.

### 4.1 `uxa-091-my-collectives-mobile.svg`

Foi adicionada entrada explícita **`Ver atualizações`** com as seguintes garantias visíveis:

- abrir a Central não altera vínculo;
- abrir a Central não marca itens como lidos;
- a ação é opcional e não cria nova participação, função, autoridade ou obrigação.

### 4.2 `uxa-093-collective-updates-center-mobile.svg`

A referência foi reformulada para:

- apresentar alerta material de segurança antes de solicitação comum;
- incluir fonte e referência de vigência/revisão no alerta;
- nomear a confirmação como **`Confirmar somente leitura`**;
- explicitar que preferência comum não impede entrega mínima necessária de aviso essencial de segurança;
- oferecer `Preferências` e `Ajustar este tipo` para conteúdos não essenciais;
- oferecer `Mais categorias` para acesso à taxonomia completa sem sobrecarregar o P0A móvel;
- declarar o escopo autorizado da Central;
- declarar que abrir a tela não marca nada como lido;
- declarar que ações revalidam o estado do objeto;
- declarar que repetição de abertura ou leitura não duplica efeitos.

## 5. Contrato validado de entrada

`GKR-TRN-110` passa a possuir gatilho explícito na origem:

```text
PER-106 — Meus Coletivos
→ Pessoa escolhe “Ver atualizações”
→ nenhuma mudança de vínculo ou leitura ocorre pelo clique
→ PER-107 — Central de Atualizações
```

A entrada preserva o conjunto de vínculos e objetos para os quais a Pessoa possui relação ou autorização pertinente. Não transporta conteúdo privado da Jornada pessoal nem amplia audiência, papel ou autoridade.

## 6. Contrato validado de retorno

A Pessoa pode retornar de `PER-107` para `PER-106` sem:

- alterar vínculo;
- confirmar presença;
- aceitar convite;
- responder solicitação;
- concluir atividade;
- mudar reputação;
- criar prioridade;
- marcar itens adicionais como lidos.

O retorno recompõe a experiência de `Meus Coletivos`; filtros temporários da Central não transformam estados substantivos em `PER-106`.

## 7. Leitura versus estado substantivo

O estado `lido` pertence ao controle de atenção e não substitui o estado do objeto de origem.

Consequentemente:

- ler pedido de informação não responde ao pedido;
- ler convite não aceita o convite;
- ler alteração de atividade não confirma presença;
- ler decisão não equivale a concordância;
- ler alerta não cria nova regra;
- confirmar somente leitura não renuncia a direito;
- ausência de confirmação não produz punição automática.

Ações substantivas seguem para o contexto materializado correspondente e precisam revalidar o estado atual antes de produzir efeito.

## 8. Concorrência e estado obsoleto

Se uma atualização mudar enquanto a Central estiver aberta:

1. o estado canônico mais recente prevalece;
2. uma ação baseada em versão obsoleta deve ser bloqueada ou atualizada antes do efeito;
3. leitura anterior não congela o objeto;
4. alteração posterior pode voltar a exigir atenção sem apagar histórico material;
5. uma atualização retirada ou substituída não pode continuar produzindo efeito a partir de um cartão antigo.

O wireframe documenta a necessidade de revalidação; não define locking, fila, API ou mecanismo técnico.

## 9. Idempotência

Reabrir `PER-107`, repetir o clique de entrada, recarregar a tela ou repetir uma confirmação de leitura não pode:

- criar segunda atualização lógica;
- duplicar vínculo;
- duplicar resposta;
- confirmar presença;
- criar nova autoridade;
- aumentar prioridade;
- alterar reputação.

Uma ação substantiva repetida deve obedecer ao contrato do objeto de origem e ao seu estado canônico.

## 10. Ordenação e preferência

A ordenação validada pode considerar, nessa ordem de natureza:

1. risco ou segurança material;
2. ação explicitamente exigida por compromisso aceito;
3. alteração de atividade futura confirmada;
4. resposta direta;
5. prazo legítimo;
6. preferência escolhida;
7. recência.

Não podem dominar a ordem:

- potencial de engajamento;
- volume de reações;
- popularidade;
- quantidade de mensagens;
- plano pago;
- publicidade;
- interesse comercial não declarado.

Preferências podem reduzir ou reorganizar atenção não essencial, mas não mascarar aviso essencial de segurança no limite necessário à proteção. O motivo dessa exceção deve permanecer compreensível.

## 11. Limite com categorias e P0B

`Mais categorias` é uma porta funcional para a taxonomia completa prevista em UXA-058. A UXA-094 não materializa páginas específicas de Perguntas e Respostas, Discussões, Convites, Recomendações, Contatos ou demais canais P1.

Também permanecem para frente própria:

- estado sem atualizações relevantes;
- excesso de volume e agrupamento;
- baixa conectividade ou falha de sincronização;
- resumo periódico.

Essas dívidas não impedem a validação do P0A corrente nem de `TRN-110`.

## 12. Limite com `PER-108`

`GKR-SURF-PER-108 — Início do Participante` continua sem materialização vigente.

Por isso:

- `GKR-TRN-111` permanece `ausente`;
- a Central não apresenta CTA fictício para `PER-108`;
- a validação de `TRN-110` termina em `PER-107` e seu retorno seguro;
- nenhuma jornada completa do participante é promovida por esta frente.

## 13. Veredito

> **Aprovada após reformulação controlada e validação integrada de `GKR-TRN-110`.**

Após a reformulação:

- `GKR-SURF-PER-106` permanece **validada**, agora com o gatilho corrente revalidado;
- `GKR-SURF-PER-107` passa de **materializado** para **validado**;
- `GKR-TRN-110` passa de **parcial** para **integralmente validada**;
- `GKR-TRN-111` permanece **ausente**;
- `GKR-SURF-PER-108` permanece com reformulação/materialização pendente.

## 14. Efeito quantitativo

A UXA-094 não cria nem remove SVGs, superfícies, transições ou IDs.

Após eventual integração:

- SVGs: 107;
- associações individuais: 107;
- perfis de rastreabilidade: 27;
- SVGs com validação funcional vigente: **97**;
- pendentes de validação específica: **10**, exclusivamente UXA-055;
- IDs granulares com referência visual: 29 de 40;
- responsabilidades sem SVG dedicado: 10;
- superfícies registradas: 40;
- transições registradas: 37;
- transições integralmente validadas no trecho de Coletivos: **7** — `TRN-105`, `106`, `107`, `108`, `109`, `110` e `112`.

## 15. Preservações

A UXA-094 não:

- materializa `PER-108`;
- valida `TRN-111`;
- materializa estados P0B da Central;
- cria áreas P1 de comunicação;
- cria novo SVG, superfície, transição ou ID;
- promove Jornada da Pessoa ou Jornada do Coletivo;
- altera Resultados Empresariais;
- define API, banco, push, fila, locking ou sincronização técnica;
- inicia protótipo, teste com pessoas ou Engenharia de Produto;
- inicia UXA-095.

## 16. Próxima transição possível

Após eventual integração e autorização separada:

> **UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`.**

A UXA-095 não é iniciada por esta validação.
