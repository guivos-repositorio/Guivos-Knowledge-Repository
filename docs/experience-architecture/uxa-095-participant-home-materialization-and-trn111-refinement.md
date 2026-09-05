---
id: UXA-095
title: Materialização Controlada do Início do Participante e Refinamento de TRN-111
status: active
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-30
parent: UXA-000
depends_on:
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-093
  - UXA-094
related:
  - UXA-096
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-SURF-PER-107
  - GKR-SURF-PER-108
  - GKR-TRN-111
  - M7.82
normative: false
---

# Materialização Controlada do Início do Participante e Refinamento de TRN-111

> **F-016-A — desmaterialização física.** Os SVGs desta frente foram removidos do corpus vigente. Qualquer nome `.svg` remanescente neste documento é **proveniência histórica**, não arquivo disponível, não autoridade visual e não autorização de Design. O contrato funcional permanece governado pelo texto e pelas autoridades funcionais relacionadas.


## 1. Finalidade

A UXA-095 materializa a referência móvel vigente de `GKR-SURF-PER-108 — Início do Participante` e torna observável, em `PER-107 — Central de Atualizações`, a entrada para esse contexto interno.

Esta frente é de **materialização e refinamento**, não de validação funcional. Ela não promove `PER-108` a validado e não promove `TRN-111` a integralmente validada.

## 2. Baseline

A iniciativa parte da `main` após UXA-094:

- GKR-STATE 2.20.0;
- M7.81;
- 107 SVGs;
- 107 associações;
- 27 perfis;
- 97 validações funcionais vigentes;
- 10 pendências, exclusivamente UXA-055;
- `PER-107` validado;
- `TRN-110` integralmente validada;
- `PER-108/TRN-111` ausentes na forma vigente.

## 3. Autoridades utilizadas

A materialização deriva das autoridades funcionais e de continuidade vigentes naquele incremento:

- UXA-056: contrato do Início do Participante e separação entre vínculo, papel, disponibilidade, presença e autoridade;
- UXA-058: separação entre síntese do Início, Central de Atualizações e canais especializados;
- UXA-059: prioridade P0A e orientação mobile-first no programa histórico, hoje subordinado às autoridades atuais;
- UXA-093/094: Central de Atualizações como origem corrente de `TRN-111`.

`UXA-016` e `UXA-018` participaram historicamente do raciocínio que originou esta materialização, especialmente em propósito, pertencimento, momento coletivo, ação compartilhada, voluntariedade, governança, autonomia e proteção. Hoje permanecem somente como proveniência histórica `superseded`: não são dependências nem autoridades funcionais vigentes de `PER-108`, e sua remoção futura, se autorizada pelo gate `F-006`, não reduz a maturidade documental já registrada em `UXA-095/096`.

A referência histórica de `UXA-016` deve, portanto, ser lida como evidência de proveniência do raciocínio original, não como evidência de autoridade vigente.

## 4. Materialização de PER-108

Novo artefato:


A referência principal mostra:

1. nome, propósito e estado de participação;
2. papel atual separado de função aceita e autoridade;
3. síntese do momento com fonte/contestação;
4. próxima ação compartilhada sem inferir presença;
5. consulta aberta sem transformar contribuição em obrigação;
6. atalhos para áreas internas próprias;
7. controle de notificações, pausa, saída, denúncia e proteção.

### 4.1 O que o Início não é

`PER-108` não é:

- feed infinito;
- réplica da Central de Atualizações;
- agenda dominante;
- ranking de participação;
- painel de cobrança de dedicação;
- atribuidor automático de papel, função, presença ou autoridade;
- implementação dos canais P1.

## 5. Refinamento controlado de PER-107

O SVG corrente de `PER-107` recebe apenas uma entrada explícita e opcional no cartão de vínculo:

> `Abrir início do Coletivo`

O refinamento preserva:

- leitura separada de ação substantiva;
- segurança acima de atenção comum;
- preferências controladas;
- retorno para `PER-106`;
- idempotência de abertura/leitura;
- nenhuma alteração automática de vínculo, papel, presença ou autoridade.

Como o SVG validado em UXA-094 foi alterado, **sua validação funcional corrente não é carregada por inferência**. A superfície `PER-107` permanece com contrato previamente validado, mas a representação corrente reformulada fica pendente de revalidação específica.

## 6. Refinamento de TRN-111

A continuidade passa a ser representada como:

```text
PER-107 — Central de Atualizações
→ Pessoa escolhe “Abrir início do Coletivo” em contexto de vínculo existente
→ abrir não altera leitura, vínculo, papel, presença ou autoridade
→ PER-108 — Início do Participante
→ contexto do mesmo Coletivo e do mesmo vínculo é preservado
```

Estado proposto de `GKR-TRN-111`: **parcial**.

A ligação não é promovida a integralmente validada porque:

- a origem visual foi reformulada nesta própria frente e requer revalidação;
- o destino `PER-108` é novo e requer validação funcional;
- retorno, concorrência, estado obsoleto e ações internas ainda precisam ser examinados como conjunto.

## 7. Invariantes da materialização

- vínculo confirmado não implica função aceita;
- função aceita não implica autoridade de governança;
- abrir o Início não confirma presença em atividade;
- atividade é opcional salvo compromisso previamente aceito e legitimamente informado;
- consulta não é votação universal nem obrigação de resposta;
- síntese do momento não substitui fonte ou Central;
- Comunicação, Discussões, Perguntas, Atividades e Decisões permanecem áreas próprias;
- silêncio, recusa, pausa e saída não geram punição reputacional;
- conteúdo patrocinado não domina a experiência interna;
- nenhuma métrica de engajamento define evolução ou pertencimento.

## 8. Estados secundários preservados

Não são materializados nesta frente:

- participante pausado;
- Coletivo sem atividade próxima;
- operação regular sem necessidade material;
- conflito de governança;
- proteção urgente;
- ausência de responsáveis;
- baixa conectividade;
- acessibilidade ampliada;
- encerramento do Coletivo;
- canais P1 especializados.

Esses estados continuam dependências separadas e só justificam novos SVGs quando alterarem materialmente decisão, autoridade, proteção ou consequência.

## 9. Efeito proposto na cobertura

Após eventual integração:

- SVGs: **108**;
- associações: **108**;
- perfis de rastreabilidade: **28**;
- validações funcionais vigentes de SVG: **96**;
- pendências: **12** = 10 UXA-055 + `PER-107` corrente reformulado + novo `PER-108`;
- IDs com referência visual: **30/40**;
- responsabilidades sem SVG dedicado: **9**;
- superfícies: 40;
- transições: 37;
- handoffs integralmente validados no trecho anterior: 7, sem nova promoção;
- `TRN-111`: ausente → **parcial**.

## 10. Veredito

> **Materialização controlada concluída no escopo documental; validação funcional pendente.**

A UXA-095 representa `PER-108` e torna `TRN-111` observável, mas não valida a nova superfície nem a ligação ponta a ponta.

## 11. Limites

Esta frente não:

- valida `PER-108`;
- revalida o SVG corrente de `PER-107`;
- valida integralmente `TRN-111`;
- materializa estados P0B ou canais P1;
- cria novo ID de superfície ou transição;
- promove Jornada da Pessoa ou Jornada do Coletivo;
- inicia protótipo navegável, teste com pessoas, W0-01 ou Engenharia de Produto.

## 12. Próximo gate possível

A próxima frente autorizável após integração da UXA-095 será **UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de TRN-111**.

A UXA-096 não é iniciada por esta frente.
