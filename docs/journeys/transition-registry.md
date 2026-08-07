---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.11.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-070
  - UXA-080
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas.

A versão 0.11.0 preserva as 37 transições e promove exclusivamente `GKR-TRN-110` de `parcial` para `integralmente validada` após a validação funcional integrada da UXA-094. `GKR-TRN-111` permanece `ausente`.

## 2. Convenções de estado

| Estado | Significado |
|---|---|
| integralmente validada | origem, destino, autoridade, dados, efeito, retorno, interrupção e concorrência examinados como uma ligação ponta a ponta no escopo documental |
| localmente validada | examinada dentro do pacote indicado sem comprovação ponta a ponta |
| parcial | cobertura incompleta ou ligação ainda não validada como conjunto |
| contratada | autoridade define a ligação, mas não há materialização suficiente |
| ausente | ligação necessária conhecida sem materialização suficiente |
| não examinada | artefatos existem, mas a ligação não foi validada como conjunto |

Validação integral documental não comprova implementação técnica.

## 3. Contagem

| Família | Quantidade |
|---|---:|
| jornada pessoal | 7 |
| Pessoa em Coletivos e operação do responsável | 13 |
| Organização, oportunidades e relações bilaterais | 11 |
| Opportunity Boost | 6 |
| **Total** | **37** |

## 4. Jornada pessoal

| ID | Origem | Destino | Estado | Evidência / lacuna principal |
|---|---|---|---|---|
| GKR-TRN-001 | PER-001 | PER-002 | parcial | continuidade entre pacotes |
| GKR-TRN-002 | PER-002 | PER-003 | localmente validada | UXA-034/035 |
| GKR-TRN-003 | PER-003 | PER-004 | parcial | ligação UXA-034 → UXA-068 |
| GKR-TRN-004 | PER-004 | PER-005 | parcial | integração expressão–inventário |
| GKR-TRN-005 | PER-005 | PER-006 | parcial | continuidade entre materializações |
| GKR-TRN-006 | PER-006 | PER-007 | localmente validada | UXA-037 |
| GKR-TRN-007 | PER-007 | PER-008 | não examinada | reconciliação com Tela Hoje |

## 5. Pessoa em Coletivos e operação do responsável

| ID | Origem | Destino | Perspectiva | Condição e efeito principal | Gate / retorno | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|---|
| GKR-TRN-101 | PER-101 | PER-102 | visitante | pesquisar/filtrar sem criar vínculo | limpar/voltar | UXA-061 | localmente validada | continuidade entre famílias |
| GKR-TRN-102 | PER-102 | PER-103 | visitante | abrir Perfil Público | conteúdo público; retorno aos resultados | UXA-061; UXA-063 | parcial | ligação entre pacotes |
| GKR-TRN-103 | PER-103 | PER-104 | solicitante potencial | iniciar revisão consciente | autenticação/elegibilidade quando aplicáveis | UXA-063; UXA-065 | parcial | handoff para solicitação |
| GKR-TRN-104 | PER-104 | PER-105 | solicitante | enviar solicitação autorizada | confirmação explícita; cancelamento conforme estado | UXA-065; UXA-067 | parcial | continuidade entre pacotes |
| GKR-TRN-105 | PER-105 | COL-003 | solicitante → responsável | disponibilizar solicitação para análise com mesmo identificador lógico | autoridade vigente; cancelamento/expiração tornam análise obsoleta | UXA-067; UXA-089; UXA-090 | **integralmente validada** | — |
| GKR-TRN-106 | COL-003 | PER-105 | responsável → solicitante | pedir informação adicional sem aprovar | finalidade limitada; Pessoa pode responder, não informar, contestar ou cancelar | UXA-067; UXA-089; UXA-090 | **integralmente validada** | — |
| GKR-TRN-107 | PER-105 | COL-003 | solicitante → responsável | enviar resposta adicional à mesma finalidade | estado ainda elegível; repetição não duplica conteúdo | UXA-067; UXA-089; UXA-090 | **integralmente validada** | — |
| GKR-TRN-108 | COL-003 | PER-106 | responsável → participante | aprovação forma vínculo; PER-105 mostra resultado; navegação posterior é opcional | autoridade e estado vigentes; `Agora não` só interrompe navegação | UXA-089; UXA-090; UXA-092 | **integralmente validada** | — |
| GKR-TRN-109 | COL-003 | PER-105 | responsável → solicitante | recusar com fundamento proporcional; expiração permanece distinta | autoridade vigente; estado revalidado; repetição não duplica recusa | UXA-067; UXA-089; UXA-090 | **integralmente validada** | — |
| GKR-TRN-110 | PER-106 | PER-107 | participante | escolher `Ver atualizações`; abrir Central sem alterar vínculo ou leitura; preservar origem/natureza/autoridade/ação/prazo | vínculo/autorização pertinente; retorno não altera estado; ação substantiva revalida estado canônico; repetição de abertura/leitura é idempotente | UXA-092 na origem; UXA-093 materialização; **UXA-094 validação integrada** | **integralmente validada** | — |
| GKR-TRN-111 | PER-107 | PER-108 | participante | selecionar contexto interno futuro | PER-108 ainda não vigente; nenhum destino fictício | UXA-094 somente na origem validada | **ausente** | Início do Participante em reformulação/materialização pendente |
| GKR-TRN-112 | COL-002 | COL-003 | responsável | abrir fila especializada preservando Coletivo e escopo | representação/autoridade vigentes; navegação não altera fila | UXA-087; UXA-089; UXA-090 | **integralmente validada** | — |
| GKR-TRN-113 | COL-004 | COL-005 | responsável | comunicar a participantes autorizados | papel e escopo de audiência | UXA-058; UXA-059 | contratada | operação interna não materializada |

### 5.1 Contrato específico de `GKR-TRN-110`

A UXA-094 valida explicitamente:

- gatilho observável em `PER-106`;
- entrada neutra: abrir a Central não muda vínculo nem leitura;
- contexto limitado a vínculos/objetos autorizados;
- retorno seguro a `PER-106`;
- leitura separada do estado substantivo;
- ações revalidando o estado canônico antes de produzir efeito;
- atualização concorrente prevalecendo sobre cartão obsoleto;
- abertura, recarga e confirmação de leitura idempotentes;
- segurança material acima de ação comum;
- preferências sem ocultar aviso essencial além do limite necessário à segurança.

## 6. Organização, oportunidades e relações bilaterais

| ID | Origem | Destino | Estado | Lacuna principal |
|---|---|---|---|---|
| GKR-TRN-201 | ORG-001 | ORG-002 | parcial | ligação com visão institucional |
| GKR-TRN-202 | ORG-002 | ORG-003 | localmente validada | distribuição entre superfícies |
| GKR-TRN-203 | ORG-003 | PER-201 | não examinada | integração publicação–descoberta |
| GKR-TRN-204 | PER-201 | PER-203 | parcial | efeito externo posterior |
| GKR-TRN-205 | PER-203 | BND-001 | parcial | efeito externo não validado |
| GKR-TRN-206 | ORG-004 | COL-008 | contratada | superfícies bilaterais ausentes |
| GKR-TRN-207 | COL-008 | ORG-005 | contratada | interface bilateral ausente |
| GKR-TRN-208 | ORG-005 | ORG-006 | contratada | operação bilateral não materializada |
| GKR-TRN-209 | ORG-006 | ORG-006 | contratada | estados operacionais ausentes |
| GKR-TRN-210 | PER-201 | PER-202 | parcial | sincronização mapa/lista |
| GKR-TRN-211 | PER-202 | PER-203 | parcial | efeito externo posterior |

## 7. Opportunity Boost

| ID | Origem | Destino | Estado | Lacuna principal |
|---|---|---|---|---|
| GKR-TRN-301 | COM-001 | COM-004 | parcial | estados residuais e regras econômicas |
| GKR-TRN-302 | COM-004 | COM-002 | parcial | integração com superfícies orgânicas |
| GKR-TRN-303 | COM-003 | COM-002 | localmente validada | continuidade transversal |
| GKR-TRN-304 | COM-002 | PER-201 | parcial | integração orgânico–patrocinado |
| GKR-TRN-305 | COM-004 | COM-005 | parcial | dez estados residuais UXA-055 |
| GKR-TRN-306 | COM-002 | PER-202 | parcial | retorno patrocinado → lista orgânica |

## 8. Efeito da UXA-094

- transições totais: 37;
- nenhuma transição nova;
- `TRN-110`: parcial → **integralmente validada**;
- `TRN-111`: permanece ausente;
- handoffs integralmente validados no trecho de Coletivos: **7** (`105`, `106`, `107`, `108`, `109`, `110`, `112`).

## 9. Próximo gate

A próxima continuidade autorizável é `PER-107 → PER-108`, condicionada à materialização/reformulação de `PER-108` em **UXA-095**. A UXA-095 não foi iniciada.
