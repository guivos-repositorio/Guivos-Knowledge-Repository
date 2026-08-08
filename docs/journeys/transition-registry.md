---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.19.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
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
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A2
  - UXA-100-A3
  - UXA-101
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas. A versão 0.19.0 preserva as **54 transições** e suas maturidades, sincronizando apenas a semântica de `TRN-416`, `TRN-426` e `BND-002` com a autoridade conceitual vigente de planos.

## 2. Convenções de estado

| Estado | Significado |
|---|---|
| integralmente validada | origem, destino, autoridade, dados, efeito, retorno, interrupção e concorrência examinados como uma ligação ponta a ponta **dentro do limite de autoridade declarado** |
| localmente validada | examinada dentro do pacote indicado sem comprovação ponta a ponta |
| parcial | cobertura incompleta ou ligação ainda não validada como conjunto |
| contratada | autoridade define a ligação, mas não há materialização suficiente |
| ausente | ligação necessária conhecida sem materialização suficiente |
| não examinada | artefatos existem, mas a ligação não foi validada como conjunto |

Validação integral documental não comprova implementação técnica nem estende a autoridade da Guivos sobre sistemas de terceiros.

## 3. Contagem

| Família | Quantidade |
|---|---:|
| jornada pessoal | 7 |
| Pessoa em Coletivos e operação do responsável | 13 |
| Organização, oportunidades e relações bilaterais | 11 |
| Opportunity Boost | 6 |
| Planos, cobrança e ciclo de vida | 17 |
| **Total** | **54** |

## 4. Jornada pessoal

| ID | Origem | Destino | Estado | Evidência / lacuna principal |
|---|---|---|---|---|
| GKR-TRN-001 | PER-001 | PER-002 | parcial | continuidade entre pacotes |
| GKR-TRN-002 | PER-002 | PER-003 | localmente validada | UXA-034/035 |
| GKR-TRN-003 | PER-003 | PER-004 | parcial | ligação UXA-034 → UXA-068 |
| GKR-TRN-004 | PER-004 | PER-005 | parcial | integração expressão–inventário |
| GKR-TRN-005 | PER-005 | PER-006 | parcial | continuidade entre materializações |
| GKR-TRN-006 | PER-006 | PER-007 | localmente validada | UXA-037 |
| GKR-TRN-007 | PER-007 | PER-008 | **integralmente validada** | UXA-097 |

`TRN-007` preserva consentimento, estado canônico, retorno e idempotência; navegar para Hoje não cria avanço ou autorização adicional.

## 5. Pessoa em Coletivos e operação do responsável

| ID | Origem | Destino | Perspectiva | Condição e efeito principal | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|
| GKR-TRN-101 | PER-101 | PER-102 | visitante | pesquisar/filtrar sem criar vínculo | UXA-061 | localmente validada | continuidade entre famílias |
| GKR-TRN-102 | PER-102 | PER-103 | visitante | abrir Perfil Público | UXA-061/063 | parcial | ligação entre pacotes |
| GKR-TRN-103 | PER-103 | PER-104 | solicitante potencial | iniciar revisão consciente | UXA-063/065 | parcial | handoff para solicitação |
| GKR-TRN-104 | PER-104 | PER-105 | solicitante | enviar solicitação autorizada | UXA-065/067 | parcial | continuidade entre pacotes |
| GKR-TRN-105 | PER-105 | COL-003 | solicitante → responsável | disponibilizar solicitação com mesmo identificador lógico | UXA-067/089/090 | **integralmente validada** | — |
| GKR-TRN-106 | COL-003 | PER-105 | responsável → solicitante | pedir informação adicional sem aprovar | UXA-067/089/090 | **integralmente validada** | — |
| GKR-TRN-107 | PER-105 | COL-003 | solicitante → responsável | responder à mesma finalidade sem duplicação | UXA-067/089/090 | **integralmente validada** | — |
| GKR-TRN-108 | COL-003 | PER-106 | responsável → participante | aprovação forma vínculo; navegação posterior é opcional | UXA-089/090/092 | **integralmente validada** | — |
| GKR-TRN-109 | COL-003 | PER-105 | responsável → solicitante | recusar com fundamento proporcional | UXA-067/089/090 | **integralmente validada** | — |
| GKR-TRN-110 | PER-106 | PER-107 | participante | abrir Central sem alterar vínculo ou leitura | UXA-092/093/094/096 | **integralmente validada** | — |
| GKR-TRN-111 | PER-107 | PER-108 | participante | abrir início do mesmo Coletivo com permissão revalidada | UXA-095/096 | **integralmente validada** | — |
| GKR-TRN-112 | COL-002 | COL-003 | responsável | abrir fila especializada preservando escopo | UXA-087/089/090 | **integralmente validada** | — |
| GKR-TRN-113 | COL-004 | COL-005 | responsável | comunicar a participantes autorizados | UXA-058/059 | contratada | operação interna não materializada |

## 6. Organização, oportunidades e relações bilaterais

| ID | Origem | Destino | Estado | Evidência / lacuna principal |
|---|---|---|---|---|
| GKR-TRN-201 | ORG-001 | ORG-002 | parcial | ligação com visão institucional |
| GKR-TRN-202 | ORG-002 | ORG-003 | localmente validada | distribuição entre superfícies |
| GKR-TRN-203 | ORG-003 | PER-201 | **integralmente validada** | UXA-098 — ativação elegível à descoberta sem garantia de distribuição |
| GKR-TRN-204 | PER-201 | PER-203 | **integralmente validada** | UXA-098 — Mapa → Detalhe com mesma oportunidade e retorno preservado |
| GKR-TRN-205 | PER-203 | BND-001 | **integralmente validada até a fronteira de autoridade Guivos** | **UXA-101 — revisão consciente, destino/responsável, minimização de dados, revalidação, cancelamento, retorno e idempotência examinados; processo externo não é validado** |
| GKR-TRN-206 | ORG-004 | COL-008 | contratada | superfícies bilaterais ausentes |
| GKR-TRN-207 | COL-008 | ORG-005 | contratada | interface bilateral ausente |
| GKR-TRN-208 | ORG-005 | ORG-006 | contratada | operação bilateral não materializada |
| GKR-TRN-209 | ORG-006 | ORG-006 | contratada | estados operacionais ausentes |
| GKR-TRN-210 | PER-201 | PER-202 | **integralmente validada** | UXA-098 — mesma consulta/contexto preservados |
| GKR-TRN-211 | PER-202 | PER-203 | **integralmente validada** | UXA-098 — Lista → Detalhe com identidade e retorno preservados |

### 6.1 Contrato V4 de `GKR-TRN-205`

```text
PER-203
→ “Ver como participar”
→ estado de revisão em PER-203
→ destino externo/responsável + dados/contexto + limites explícitos
→ confirmar conscientemente
→ revalidar destino conhecido/autorizado
→ TRN-205
→ BND-001
→ autoridade externa
```

Regras:

- o estado de revisão permanece em `PER-203`, sem novo ID;
- `BND-001` não é tela da Guivos;
- ausência, invalidade ou alteração material do destino bloqueia redirecionamento silencioso;
- cancelar mantém a Pessoa no Detalhe e não conta como falha;
- a saída não confirma inscrição, reserva, compra, contratação ou evolução;
- retorno não presume resultado externo;
- dados/inferências da jornada não acompanham a saída sem finalidade e autorização adequadas.

## 7. Opportunity Boost

| ID | Origem | Destino | Estado | Lacuna principal |
|---|---|---|---|---|
| GKR-TRN-301 | COM-001 | COM-004 | parcial | regras econômicas e integração ponta a ponta |
| GKR-TRN-302 | COM-004 | COM-002 | parcial | integração com superfícies orgânicas |
| GKR-TRN-303 | COM-003 | COM-002 | localmente validada | continuidade transversal |
| GKR-TRN-304 | COM-002 | PER-201 | parcial | integração orgânico–patrocinado |
| GKR-TRN-305 | COM-004 | COM-005 | **parcial** | COM-005 validado pela UXA-099; ligação origem→estado residual ainda não examinada ponta a ponta |
| GKR-TRN-306 | COM-002 | PER-202 | parcial | retorno patrocinado → lista orgânica |

## 8. Planos, cobrança e ciclo de vida

A taxonomia vigente para leitura das superfícies é:

```text
Pessoa: Free · Plus · Pro
Coletivo: Livre · Mobiliza · Impacta · Rede
Organização: Conecta · Eleva · Transforma
Guivos Business: Start · Growth · Scale · Enterprise (produto separado; sem transições próprias nesta frente)
```

### 8.1 Pessoa

| ID | Origem | Destino | Estado | Lacuna |
|---|---|---|---|---|
| GKR-TRN-401 | PER-301 | PER-302 | **localmente validada** | gateway/execução financeira |
| GKR-TRN-402 | PER-302 | PER-304 | **localmente validada** | processamento financeiro real |
| GKR-TRN-403 | PER-301 | PER-303 | **localmente validada** | regra financeira entre ciclos |
| GKR-TRN-404 | PER-303 | PER-304 | **localmente validada** | execução do entitlement |
| GKR-TRN-405 | PER-304 | PER-301 | **localmente validada** | persistência técnica |

### 8.2 Coletivo

| ID | Origem | Destino | Estado | Lacuna |
|---|---|---|---|---|
| GKR-TRN-411 | COL-301 | COL-302 | **localmente validada** | gateway/execução financeira |
| GKR-TRN-412 | COL-302 | COL-304 | **localmente validada** | processamento financeiro real |
| GKR-TRN-413 | COL-301 | COL-303 | **localmente validada** | regra financeira entre ciclos |
| GKR-TRN-414 | COL-303 | COL-304 | **localmente validada** | execução operacional/transacional |
| GKR-TRN-415 | COL-304 | COL-301 | **localmente validada** | persistência técnica |
| GKR-TRN-416 | COL-301 | BND-002 | **parcial** | processo posterior de contratação/dimensionamento assistido não materializado |

`TRN-416` não significa “ir para Enterprise”. Ele significa sair do autoatendimento quando a contratação concreta exigir assistência. A maturidade permanece parcial.

### 8.3 Organização

| ID | Origem | Destino | Estado | Lacuna |
|---|---|---|---|---|
| GKR-TRN-421 | ORG-301 | ORG-302 | **localmente validada** | gateway/execução financeira |
| GKR-TRN-422 | ORG-302 | ORG-304 | **localmente validada** | processamento financeiro real |
| GKR-TRN-423 | ORG-301 | ORG-303 | **localmente validada** | regra financeira entre ciclos |
| GKR-TRN-424 | ORG-303 | ORG-304 | **localmente validada** | execução institucional |
| GKR-TRN-425 | ORG-304 | ORG-301 | **localmente validada** | persistência técnica |
| GKR-TRN-426 | ORG-301 | BND-002 | **parcial** | processo posterior de contratação/dimensionamento assistido não materializado |

`TRN-426` não significa “ir para Business Scale”. A Organização permanece participante e Guivos Business permanece produto separado. A maturidade da transição continua parcial.

## 9. BND-002

`BND-002` é a fronteira genérica de **contratação/dimensionamento assistido**.

A fronteira poderá ser alcançada quando a necessidade real exigir proposta, dimensionamento, análise específica, contrato ou configuração assistida. O nome do plano, isoladamente, não é autoridade suficiente para determinar o handoff.

A correção semântica:

- não cria transição;
- não remove transição;
- não altera contagem;
- não promove `TRN-416` ou `TRN-426`;
- não cria fluxo de Guivos Business.

## 10. Preservações de maturidade

- transições totais permanecem **54**;
- `TRN-205` permanece **integralmente validada até `BND-001`**;
- nenhum comportamento posterior a `BND-001` é atribuído à Guivos;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem parciais;
- nenhuma nova transição é criada;
- validação documental continua distinta de implementação técnica.

## 11. Próximo gate

V4 permanece encerrada no limite controlável pela Guivos. V5/UXA-102, integrações patrocinadas, cobrança real e processos posteriores a `BND-002` permanecem frentes separadas e não são iniciados automaticamente.