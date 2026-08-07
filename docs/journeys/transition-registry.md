---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.12.0
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
  - UXA-095
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas.

A versão 0.12.0 preserva as 37 transições. A UXA-095 torna `GKR-TRN-111` observável entre a Central reformulada e o novo Início do Participante, promovendo-a exclusivamente de `ausente` para `parcial`.

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
| GKR-TRN-110 | PER-106 | PER-107 | participante | escolher `Ver atualizações`; abrir Central sem alterar vínculo ou leitura; preservar origem/natureza/autoridade/ação/prazo | vínculo/autorização pertinente; retorno não altera estado; ação substantiva revalida estado canônico; repetição de abertura/leitura é idempotente | UXA-092 na origem; UXA-093 materialização; UXA-094 validação integrada | **integralmente validada** | — |
| GKR-TRN-111 | PER-107 | PER-108 | participante | escolher `Abrir início do Coletivo` em vínculo existente; preservar mesmo Coletivo e mesmo vínculo sem alterar leitura, papel, presença ou autoridade | origem corrente reformulada e destino novo exigem revalidação/validação integrada; retorno e concorrência ainda não examinados como conjunto | UXA-094 na origem anterior; **UXA-095 materialização/refinamento** | **parcial** | validar PER-107 corrente, PER-108 e handoff ponta a ponta |
| GKR-TRN-112 | COL-002 | COL-003 | responsável | abrir fila especializada preservando Coletivo e escopo | representação/autoridade vigentes; navegação não altera fila | UXA-087; UXA-089; UXA-090 | **integralmente validada** | — |
| GKR-TRN-113 | COL-004 | COL-005 | responsável | comunicar a participantes autorizados | papel e escopo de audiência | UXA-058; UXA-059 | contratada | operação interna não materializada |

### 5.1 Contrato preservado de `GKR-TRN-110`

A UXA-095 não altera o contrato validado de `TRN-110`: entrada em `PER-107` continua neutra, leitura continua separada de efeito substantivo, ações revalidam estado canônico e segurança material preserva prioridade legítima.

### 5.2 Refinamento de `GKR-TRN-111`

A UXA-095 representa:

```text
PER-107
→ “Abrir início do Coletivo”
→ nenhum vínculo, leitura, papel, presença ou autoridade é alterado
→ PER-108
→ contexto do mesmo Coletivo e vínculo é preservado
```

A representação não valida retorno, concorrência, estado obsoleto, ações internas ou interrupções como um contrato integrado.

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

## 8. Efeito da UXA-095

- transições totais: 37;
- nenhuma transição nova;
- `TRN-110`: permanece **integralmente validada**;
- `TRN-111`: `ausente` → **parcial**;
- handoffs integralmente validados no trecho anterior: **7** (`105`, `106`, `107`, `108`, `109`, `110`, `112`), sem nova promoção.

## 9. Próximo gate

A próxima continuidade autorizável é a validação integrada de `PER-107 → PER-108`, condicionada à revalidação do SVG corrente de `PER-107` e à validação funcional de `PER-108` em **UXA-096**. A UXA-096 não foi iniciada.
