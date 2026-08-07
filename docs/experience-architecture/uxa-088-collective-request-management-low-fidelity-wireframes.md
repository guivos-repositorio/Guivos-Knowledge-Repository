---
id: UXA-088
title: Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo
status: draft
version: 0.2.0
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
  - UXA-089
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
  - M7.76
normative: false
---

# Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo

## 1. Finalidade

A UXA-088 materializa exclusivamente `GKR-SURF-COL-003 — gestão de solicitações` na perspectiva do responsável do Coletivo.

A família permite responder:

> **Quais solicitações exigem atenção, quais dados posso legitimamente analisar, o que posso decidir dentro da minha autoridade, como pedir informação sem coagir e qual consequência será produzida para a Pessoa?**

A UXA-089 reformulou seis dos sete SVGs e validou funcionalmente toda a família. A materialização não inclui gestão de participantes (`COL-004`) e não promove a Jornada do Coletivo.

## 2. Canal

Canal inicial: **computador protegido**.

A escolha segue UXA-059: triagem, comparação de estados, leitura de dados autorizados e decisões com consequência exigem espaço operacional maior. Derivações móveis permanecem fora deste pacote.

## 3. Estados materializados e validados

A família utiliza sete SVGs para um único ID granular `GKR-SURF-COL-003`.

| Estado | Arquivo | Decisão principal | Validação |
|---|---|---|---|
| fila operacional | `uxa-088-collective-request-management-queue-desktop.svg` | escolher uma solicitação sem alterar prioridade | UXA-089 |
| detalhe comum | `uxa-088-collective-request-management-detail-desktop.svg` | analisar dados autorizados e escolher próximo ato | UXA-089 |
| análise protegida | `uxa-088-collective-request-management-protected-detail-desktop.svg` | analisar exposição mínima dentro de autoridade especializada | UXA-089 |
| pedido adicional | `uxa-088-collective-request-management-additional-information-desktop.svg` | formular pergunta, finalidade e referência temporal sem impor revelação | UXA-089 |
| confirmação de aprovação | `uxa-088-collective-request-management-approve-confirmation-desktop.svg` | confirmar formação do vínculo sem atribuir função automática | UXA-089 |
| confirmação de recusa | `uxa-088-collective-request-management-refuse-confirmation-desktop.svg` | confirmar recusa proporcional sem convertê-la em sanção ou reputação | UXA-089 |
| autoridade insuficiente | `uxa-088-collective-request-management-insufficient-authority-desktop.svg` | não decidir e retornar ou encaminhar legitimamente | UXA-089 |

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

A UXA-089 valida `COL-003` como superfície, mas **não valida as transições `TRN-105` a `109` ou `TRN-112` ponta a ponta**. Esses handoffs exigem inspeção integrada própria.

## 5. Regras da fila

A fila separa, sem transformar volume em desempenho:

- aguardando decisão;
- aguardando informação da Pessoa;
- resposta adicional recebida;
- análise protegida;
- referências temporais distintas por natureza;
- encerradas por aprovação, recusa, cancelamento ou expiração.

Consultar, ordenar ou filtrar não altera prioridade substantiva, decisão ou direito da Pessoa. A versão reformulada distingue `estimativa` de `resposta até` e declara a base da ordenação sem convertê-la em prioridade automática.

## 6. Dados e autoridade

O responsável pode ver somente informações vinculadas à finalidade declarada do pedido e ao seu escopo de autoridade.

Não são inferidos ou exibidos automaticamente:

- conteúdo da Jornada pessoal;
- outros Coletivos da Pessoa;
- contatos privados desnecessários;
- histórico externo de recusas, denúncias ou avaliações;
- atributos sensíveis não autorizados;
- relações institucionais sem pertinência ao pedido.

Em análise protegida, remetente, equipe de análise e autoridade de decisão permanecem separados.

A UXA-089 também consolida que autoridade é verificada pelo escopo concedido e não pode ser criada por checkbox, autodeclaração ou simples acesso à superfície.

## 7. Pedido de informação adicional

O pedido declara:

- pergunta exata;
- finalidade;
- autoridade solicitante;
- formato aceito;
- referência temporal e eventual regra de expiração;
- dados que não são solicitados;
- efeito sobre a decisão.

A interface lembra que a Pessoa pode responder, informar que não consegue confirmar, preferir não responder, contestar ou cancelar conforme o estado aplicável. Solicitar informação não autoriza coletar dado irrelevante nem presumir dever de revelação.

Após UXA-089:

- o cenário usa somente critério objetivo previamente apresentado;
- saúde, diagnóstico e necessidade de acessibilidade ficam fora da decisão de elegibilidade;
- acessibilidade permanece responsabilidade separada de acomodação e nunca critério oculto de entrada;
- `prefiro não responder` não é recusa voluntária.

## 8. Aprovação

Antes da confirmação, o responsável compreende que aprovação:

- forma vínculo de participante conforme contrato;
- não atribui função, moderação, autoridade ou presença obrigatória;
- não ativa notificações ou exposição nominal automaticamente;
- não comprova mérito, reputação ou evolução humana;
- produz efeito na perspectiva da Pessoa;
- não declara `PER-106` como materializada.

A autoridade é verificada antes da confirmação. O checkbox confirma fundamento e consequência; não cria ou amplia permissão.

## 9. Recusa

A recusa exige fundamento proporcional e separa claramente:

- recusa de sanção;
- recusa de reputação;
- recusa de denúncia;
- recusa de bloqueio universal;
- eventual revisão formal, que só pode existir quando houver regra, prazo e autoridade próprios.

A UXA-089 exige que o fundamento utilizado tenha sido previamente apresentado à Pessoa e que a confirmação não funcione como autodeclaração de autoridade.

## 10. Autoridade insuficiente

Quando a pessoa autenticada não possui escopo suficiente, a superfície:

- identifica a ação indisponível;
- explica qual autoridade falta;
- não exibe dados adicionais por tentativa de acesso;
- permite retorno à fila ou à Visão Geral;
- permite consultar somente o escopo concedido;
- oferece encaminhamento somente quando houver autoridade receptora legítima;
- evita atalhos para assumir, solicitar automaticamente ou ampliar permissão.

## 11. Rastreabilidade

| Campo | Resultado após UXA-089 |
|---|---|
| superfície | `GKR-SURF-COL-003` |
| canal | computador protegido |
| novos IDs granulares | 0 |
| SVGs da família | 7 |
| transições novas | 0 |
| origem principal | `GKR-SURF-COL-002` via `GKR-TRN-112` |
| efeitos bilaterais | `GKR-TRN-105` a `GKR-TRN-109` |
| validação funcional da superfície | UXA-089 — aprovada após reformulação controlada |
| handoffs ponta a ponta | pendentes de pacote integrado específico |
| jornada do Coletivo | permanece `draft` |

## 12. Resultado da UXA-089

Após eventual integração da validação:

- `GKR-SURF-COL-003` passa de **materializado; validação pendente** para **validado**;
- seis SVGs são reformulados e todos os sete são validados;
- `GKR-TRN-112` continua parcial apesar de ambos endpoints estarem validados;
- `GKR-TRN-105` a `GKR-TRN-109` continuam parciais até validação integrada;
- `GKR-TRN-108` mantém ainda `PER-106` ausente;
- os 40 IDs de superfície e as 37 transições permanecem inalterados;
- `COL-004`, `PER-106`, `PER-107` e `PER-108` permanecem fora do escopo.

## 13. Limites

A família validada não:

- valida handoffs bilaterais como conjunto;
- fecha a Jornada do Coletivo;
- materializa participantes, comunicação, moderação ou relações institucionais;
- cria revisão formal completa de recusa;
- define política jurídica, API ou esquema de dados;
- cria protótipo navegável;
- executa teste com pessoas;
- altera Resultados Empresariais;
- inicia Engenharia de Produto;
- inicia UXA-090.

## 14. Próximo ato possível

Após integração e autorização separada, o próximo ato recomendado é:

> **UXA-090 — Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos.**

A UXA-090 não é iniciada por este pacote.
