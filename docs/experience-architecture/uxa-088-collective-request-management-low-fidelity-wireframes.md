---
id: UXA-088
title: Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-000
depends_on:
  - UXA-014
  - UXA-056
  - UXA-059
  - UXA-066
  - UXA-067
  - UXA-086
  - UXA-087
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-COL-002
  - GKR-SURF-COL-003
  - GKR-TRN-105
  - GKR-TRN-106
  - GKR-TRN-107
  - GKR-TRN-108
  - GKR-TRN-109
  - GKR-TRN-112
  - GKR-JOURNEY-GAPS-001
  - M7.75
normative: false
---

# Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo

## 1. Finalidade

A UXA-088 materializa exclusivamente `GKR-SURF-COL-003 — gestão de solicitações` na perspectiva do responsável do Coletivo.

A família deverá permitir responder:

> **Quais solicitações exigem atenção, quais dados posso legitimamente analisar, o que posso decidir dentro da minha autoridade, como pedir informação sem coagir e qual consequência será produzida para a Pessoa?**

A UXA-088 não valida funcionalmente a família, não materializa gestão de participantes (`COL-004`) e não promove a Jornada do Coletivo.

## 2. Canal

Canal inicial: **computador protegido**.

A escolha segue UXA-059: triagem, comparação de estados, leitura de dados autorizados e decisões com consequência exigem espaço operacional maior. Derivações móveis permanecem fora deste pacote.

## 3. Estados materializados

A família utiliza sete SVGs para um único ID granular `GKR-SURF-COL-003`.

| Estado | Arquivo | Decisão principal |
|---|---|---|
| fila operacional | `uxa-088-collective-request-management-queue-desktop.svg` | escolher uma solicitação sem alterar prioridade |
| detalhe comum | `uxa-088-collective-request-management-detail-desktop.svg` | analisar dados autorizados e escolher próximo ato |
| análise protegida | `uxa-088-collective-request-management-protected-detail-desktop.svg` | analisar exposição mínima dentro de autoridade especializada |
| pedido adicional | `uxa-088-collective-request-management-additional-information-desktop.svg` | formular pergunta, finalidade e prazo sem impor revelação |
| confirmação de aprovação | `uxa-088-collective-request-management-approve-confirmation-desktop.svg` | confirmar formação do vínculo sem atribuir função automática |
| confirmação de recusa | `uxa-088-collective-request-management-refuse-confirmation-desktop.svg` | confirmar recusa proporcional sem convertê-la em sanção ou reputação |
| autoridade insuficiente | `uxa-088-collective-request-management-insufficient-authority-desktop.svg` | não decidir e retornar ou encaminhar legitimamente |

Expiração e cancelamento pela Pessoa são eventos refletidos na fila e no histórico do processo. Não são decisões equivalentes do responsável e não recebem SVG próprio nesta materialização.

## 4. Continuidade bilateral

```text
COL-002 — Visão Geral do Responsável
→ COL-003 — fila de solicitações
→ detalhe comum ou protegido
→ aguardar, pedir informação, aprovar ou recusar
→ Pessoa recebe o estado correspondente em PER-105
→ aprovação poderá seguir futuramente para PER-106
```

A UXA-088 materializa os endpoints responsáveis das transições `TRN-105`, `106`, `107`, `108`, `109` e o destino de `TRN-112`, mas **não valida nenhuma dessas transições ponta a ponta**.

## 5. Regras da fila

A fila deverá separar, sem transformar volume em desempenho:

- aguardando decisão;
- aguardando informação da Pessoa;
- resposta adicional recebida;
- análise protegida;
- próximas do prazo informado;
- encerradas por aprovação, recusa, cancelamento ou expiração.

Consultar, ordenar ou filtrar não poderá alterar prioridade substantiva, decisão ou direito da Pessoa. Qualquer ordenação automática deverá ser explicável e contestável quando materialmente relevante.

## 6. Dados e autoridade

O responsável poderá ver somente informações vinculadas à finalidade declarada do pedido e ao seu escopo de autoridade.

Não serão inferidos ou exibidos automaticamente:

- conteúdo da Jornada pessoal;
- outros Coletivos da Pessoa;
- contatos privados desnecessários;
- histórico externo de recusas, denúncias ou avaliações;
- atributos sensíveis não autorizados;
- relações institucionais sem pertinência ao pedido.

Em análise protegida, remetente, equipe de análise e autoridade de decisão permanecem separados.

## 7. Pedido de informação adicional

O pedido deverá declarar:

- pergunta exata;
- finalidade;
- autoridade solicitante;
- formato aceito;
- prazo e eventual regra de expiração;
- dados que não são solicitados;
- efeito da pausa sobre a decisão.

A interface deverá lembrar que a Pessoa pode responder, preferir não informar, contestar ou cancelar. Solicitar informação não autoriza coletar dado irrelevante nem presumir dever de revelação.

## 8. Aprovação

Antes da confirmação, o responsável deverá compreender que aprovação:

- forma vínculo de participante conforme contrato;
- não atribui função, moderação, autoridade ou presença obrigatória;
- não ativa notificações ou exposição nominal automaticamente;
- não comprova mérito, reputação ou evolução humana;
- produz efeito na perspectiva da Pessoa, mas a continuidade para `PER-106` permanece não materializada.

## 9. Recusa

A recusa deverá exigir fundamento proporcional e separar claramente:

- recusa de sanção;
- recusa de reputação;
- recusa de denúncia;
- recusa de bloqueio universal;
- eventual revisão formal, que só poderá existir quando houver regra, prazo e autoridade próprios.

## 10. Autoridade insuficiente

Quando a pessoa autenticada não possuir escopo suficiente, a superfície deverá:

- identificar a ação indisponível;
- explicar qual autoridade falta;
- não exibir dados adicionais por tentativa de acesso;
- permitir retorno à fila ou à Visão Geral;
- oferecer encaminhamento somente quando houver autoridade receptora legítima;
- evitar atalhos para assumir ou ampliar permissão.

## 11. Rastreabilidade

| Campo | Resultado da UXA-088 |
|---|---|
| superfície | `GKR-SURF-COL-003` |
| canal | computador protegido |
| novos IDs granulares | 0 |
| novos SVGs | 7 |
| transições novas | 0 |
| origem principal | `GKR-SURF-COL-002` via `GKR-TRN-112` |
| efeitos bilaterais | `GKR-TRN-105` a `GKR-TRN-109` |
| validação funcional | pendente de pacote específico |
| jornada do Coletivo | permanece `draft` |

## 12. Efeito esperado sobre os registros

Após eventual integração:

- `GKR-SURF-COL-003` passa de programado/ausente para **materializado; validação pendente**;
- `GKR-TRN-112` passa a possuir os dois endpoints materializados, mas continua sem validação funcional ponta a ponta;
- `GKR-TRN-105` a `GKR-TRN-109` ganham evidência na perspectiva do responsável, mas continuam parciais até validação integrada;
- os 40 IDs de superfície e as 37 transições permanecem inalterados;
- `COL-004`, `PER-106`, `PER-107` e `PER-108` permanecem fora do escopo.

## 13. Limites

A UXA-088 não:

- valida funcionalmente os sete novos SVGs;
- fecha a Jornada do Coletivo;
- materializa participantes, comunicação, moderação ou relações institucionais;
- cria revisão formal completa de recusa;
- define política jurídica, API ou esquema de dados;
- cria protótipo navegável;
- executa teste com pessoas;
- altera Resultados Empresariais;
- inicia Engenharia de Produto;
- inicia UXA-089.

## 14. Próximo ato possível

Após integração e autorização separada, o próximo ato recomendado é:

> **UXA-089 — Validação Funcional da Gestão de Solicitações do Responsável do Coletivo.**

A UXA-089 não é iniciada por este pacote.
