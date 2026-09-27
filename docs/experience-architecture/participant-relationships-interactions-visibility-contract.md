---
id: GKR-UX-PARTICIPANT-RELATIONSHIPS-INTERACTIONS-001
title: Participantes — Relações, Interações, Conexões e Visibilidade — Contrato Transversal
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-27
normative: true
maturity: cross_participant_contract_candidate
depends_on:
  - GKR-UX-PERSON-JOURNEY-ORCHESTRATION-001
  - GKR-UX-ORGCOL-JOURNEY-ORCHESTRATION-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
---

# Participantes — Relações, Interações, Conexões e Visibilidade — Contrato Transversal

## 1. Finalidade

Este documento governa como os três participantes canônicos — Pessoa, Coletivo e Organização — podem se encontrar, relacionar, interagir e visualizar informação uns dos outros sem transformar encontrabilidade em acesso irrestrito.

Ele governa significado e limites transversais. Não cria por si só nova superfície, transição, mensagem, convite, vínculo ou permissão.

## 2. Participantes e agente humano

Pessoa é participante humano. Coletivo e Organização são participantes contextuais/institucionais operados por Pessoas com papel e autoridade adequados.

```text
PESSOA AUTENTICADA
→ PODE ATUAR COMO ELA MESMA
→ PODE ATUAR EM CONTEXTO DE COLETIVO
→ PODE ATUAR EM CONTEXTO DE ORGANIZAÇÃO
→ SOMENTE COM PAPEL + AUTORIDADE VÁLIDOS
```

## 3. Regra de visibilidade

```text
ENCONTRÁVEL
≠ VISÍVEL EM DETALHE
≠ REVELÁVEL
≠ INTERAGÍVEL
≠ VINCULADO
≠ AUTORIZADO

DADO EXISTENTE
≠ DADO NECESSÁRIO
≠ DADO COMPARTILHÁVEL
```

Toda visualização entre participantes deve responder a finalidade, contexto, papel, autoridade, estado, minimização, proteção e proveniência.

## 4. Matriz canônica corrente

| Relação | Estado corrente | Interação autorizada |
|---|---|---|
| Pessoa ↔ Pessoa | não adjudicada | nenhuma interação bilateral genérica deve ser inferida |
| Pessoa → Coletivo | governada | descobrir, consultar perfil público, revisar, solicitar participação, acompanhar |
| Coletivo → Pessoa solicitante | governada | pedir informação, decidir solicitação, comunicar resultado no fluxo |
| Pessoa participante ↔ Coletivo | governada | vínculo, participação e continuidades autorizadas |
| Pessoa ↔ Organização | governada em oportunidades internas | manifestação/inscrição e continuidade bilateral no mesmo objeto |
| Organização ↔ Coletivo | governada | proposta, avaliação/negociação, relação e continuidade bilateral |
| Organização ↔ Organização | necessidade reconhecida sem contrato próprio | não materializar por analogia |
| Coletivo ↔ Coletivo | necessidade reconhecida sem contrato próprio | não materializar por analogia |

## 5. Pessoa ↔ Coletivo

A Pessoa pode participar de Coletivo conforme o fluxo governado:

```text
DESCOBERTA
→ PERFIL PÚBLICO
→ REVISÃO
→ SOLICITAÇÃO
→ PENDÊNCIA
→ DECISÃO DO RESPONSÁVEL
→ VÍNCULO
→ PARTICIPAÇÃO
```

A Pessoa pode visualizar, conforme autoridade: identidade/perfil público, propósito, condições pertinentes, estado da própria solicitação/vínculo, comunicações destinadas à audiência autorizada, atividades/consultas/decisões/oportunidades acessíveis e seu próprio papel/responsabilidade.

O Coletivo pode visualizar somente o recorte necessário da Pessoa: identidade/referência, dados conscientemente enviados, solicitação, vínculo, papel/responsabilidade aplicável e condições legítimas necessárias à operação/proteção.

O Coletivo não recebe por consequência objetivos privados, inferências da Journey, dados sensíveis desnecessários, outras relações, razões internas de relevância ou histórico pessoal fora da finalidade.

## 6. Iniciativa do Coletivo em relação à Pessoa

O corpus corrente sustenta Pessoa solicitando participação. Não sustenta ainda um mecanismo genérico de convite/adesão unilateral iniciado pelo Coletivo.

```text
CONVITE DO COLETIVO
→ LACUNA A ADJUDICAR

ADICIONAR PESSOA SEM ACEITE
→ NÃO AUTORIZADO POR INFERÊNCIA

PROPOSTA DE PAPEL
≠ ACEITE

SILÊNCIO
≠ ACEITE
```

## 7. Pessoa ↔ Pessoa

### 7.1 Adjudicação corrente

A necessidade de Pessoas perceberem outras Pessoas em contextos compartilhados é compatível com o ecossistema, mas o corpus corrente não prova um objeto bilateral autônomo Pessoa↔Pessoa.

Por isso:

```text
COEXISTÊNCIA EM CONTEXTO COMPARTILHADO
→ PODE SER MATERIALIZADA QUANDO A SUPERFÍCIE / FINALIDADE EXIGIR

RELAÇÃO SOCIAL BILATERAL AUTÔNOMA
→ NÃO ADJUDICADA

NOVO PER-* / GKR-TRN-*
→ NÃO JUSTIFICADO
```

Não criar por inferência:

- follow;
- amizade;
- conexão bilateral;
- chat ou DM;
- solicitação de conexão;
- lista de contatos;
- compartilhamento privado P↔P;
- acesso ao perfil privado de outra Pessoa;
- feed social derivado de conexões.

### 7.2 Pessoas no mesmo contexto

Duas Pessoas podem aparecer uma para a outra quando isso for necessário ao objeto legítimo que compartilham — por exemplo, participação em Coletivo, atividade, consulta, decisão ou outra superfície cuja autoridade exija participantes visíveis.

Essa visibilidade deve ser **contextual**, não uma autorização global sobre a Pessoa.

O recorte pode conter, quando necessário e autorizado:

- identidade ou nome de apresentação;
- imagem pública/de apresentação, se existir e for apropriada;
- papel no contexto;
- vínculo pertinente;
- responsabilidade pertinente;
- contribuição/ação conscientemente pública naquele objeto;
- estado necessário à coordenação.

Não deve revelar por consequência:

- Journey privada;
- objetivos privados;
- dados de contato;
- outros Coletivos/Organizações;
- oportunidades relacionadas;
- inferências pessoais;
- histórico fora do objeto;
- dados sensíveis;
- informação não necessária à finalidade.

### 7.3 Interação mediada

```text
PESSOA A
+
OBJETO / CONTEXTO COMPARTILHADO
+
PESSOA B
→ INTERAÇÃO MEDIADA PELO OBJETO

INTERAÇÃO MEDIADA
≠ CONEXÃO SOCIAL
≠ PERMISSÃO DE CONTATO DIRETO
≠ VÍNCULO PERSISTENTE P↔P
```

Comentários, respostas, menções, mensagens contextuais ou outras mecânicas específicas somente podem existir quando a autoridade do objeto correspondente as contratar. Este documento não as cria genericamente.

### 7.4 Reabertura

Pessoa↔Pessoa deve ser reaberto somente se nova evidência canônica exigir um objeto relacional próprio, como conexão bilateral persistente, mensagem privada, rede de contatos ou outro lifecycle independente do contexto compartilhado.

## 8. Pessoa ↔ Organização

A relação bilateral atualmente comprovada está no processo interno de manifestação/inscrição em oportunidade.

A Organização recebe somente o objeto e o recorte de dados conscientemente autorizados para a finalidade. A Pessoa recebe somente atualização material legitimamente comunicável do mesmo objeto.

```text
PER-204 ↔ ORG-008
→ MESMO OBJETO BILATERAL
→ PERSPECTIVAS DIFERENTES
→ DADOS MINIMIZADOS
→ ESTADO INTERNO PROTEGIDO NÃO ATRAVESSA POR PADRÃO
```

## 9. Organização ↔ Coletivo

ORG-004..006 e COL-008 representam o mesmo objeto relacional sob perspectivas distintas.

A relação pode conter escopo, proposta, resposta, compromissos, consentimentos, contestação, uso de marca quando aplicável, revisão e encerramento.

Uma contraparte não se torna recurso interno da outra e relação institucional não concede acesso irrestrito aos participantes humanos da contraparte.

## 10. O↔O e C↔C

Necessidades conceituais reconhecidas permanecem sem contrato próprio. Não reutilizar O↔C nem criar IDs por simetria.

## 11. Informação de participantes

Quando uma superfície precisa exibir participantes envolvidos, o recorte deve poder justificar:

- quem é pertinente;
- em qual papel;
- qual vínculo;
- qual estado;
- qual responsabilidade pela próxima ação;
- quais dados são necessários;
- qual proveniência;
- qual finalidade;
- qual informação deve permanecer protegida.

## 12. Planos

Plano pode alterar capacidade operacional, cota ou profundidade, mas não pode comprar legitimidade relacional.

```text
PLANO SUPERIOR
≠ MAIS DIREITO SOBRE OUTRA PESSOA
≠ MAIS ACESSO A DADO PESSOAL POR PADRÃO
≠ AUTORIDADE HUMANA SUPERIOR
≠ CONSENTIMENTO
```

Capacidade relacional premium somente pode existir quando explicitamente contratada e compatível com privacidade, autoridade e finalidade.

## 13. Relação com comunicações e notificações

Este contrato responde **quem pode se relacionar, em qual objeto e qual informação pode atravessar**.

O contrato de Comunicações e Notificações responde **quando um evento dessa relação deve produzir atualização, consciência ou alerta e como a continuidade ocorre**.

```text
RELAÇÃO AUTORIZADA
≠ NOTIFICAÇÃO AUTOMÁTICA

EVENTO MATERIAL
≠ NOVA RELAÇÃO
```

## 14. Source lock

Design, IA e implementação não podem inventar conexão, convite, mensagem, visibilidade, permissão, vínculo ou dado compartilhado porque um componente visual comporta essa função.

## 15. Estado

```text
CROSS-PARTICIPANT CONTRACT
→ CANDIDATE

NEW SURFACE IDS
→ NONE

NEW TRANSITION IDS
→ NONE

PERSON↔PERSON AUTONOMOUS SOCIAL RELATIONSHIP
→ NOT ADJUDICATED

PERSON↔PERSON CONTEXTUAL CO-PRESENCE
→ ALLOWED WHEN REQUIRED BY AUTHORIZED SHARED OBJECT

COLLECTIVE-INITIATED MEMBERSHIP
→ NOT ADJUDICATED

PRODUCT ENGINEERING
→ NOT RELEASED
```
