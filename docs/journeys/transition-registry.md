---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.29.1
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-21
related:
  - UXA-087
  - UXA-089
  - UXA-090
  - UXA-092
  - UXA-094
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-099
  - GKR-PLANS-PERSON-001
  - GKR-PLANS-COLLECTIVE-001
  - GKR-PLANS-ORGANIZATION-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - UXA-101
  - GKR-UX-D5-C1-001
  - GKR-UX-D5-C4B-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-BUSINESS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições correntes das Jornadas Integradas. A maturidade declarada em cada linha é o estado operativo a ser usado por Design e prototipação; a sequência histórica de validação não é necessária para consumo.

A contagem permanece em **66 transições**. `TRN-008..013` passam a **integralmente validadas**.

## 2. Convenções de estado

| Estado | Significado |
|---|---|
| integralmente validada | origem, destino, autoridade, dados, efeito, retorno, interrupção e concorrência examinados como uma ligação ponta a ponta **dentro do limite de autoridade declarado** |
| localmente validada | examinada dentro do pacote indicado sem comprovação ponta a ponta |
| parcial | cobertura incompleta ou ligação ainda não validada como conjunto |
| contratada | autoridade define a ligação, mas a ligação ainda não possui validação ponta a ponta suficiente |
| ausente | ligação necessária conhecida sem materialização suficiente |
| não examinada | artefatos existem, mas a ligação não foi validada como conjunto |

Validação integral documental não comprova implementação técnica nem estende a autoridade da Guivos sobre sistemas de terceiros.

## 3. Contagem

| Família | Quantidade |
|---|---:|
| jornada pessoal | 13 |
| Pessoa em Coletivos e operação do responsável | 13 |
| Organização, oportunidades e relações bilaterais | 11 |
| Opportunity Boost | 6 |
| Planos, cobrança e ciclo de vida | 23 |
| **Total** | **66** |

## 4. Jornada pessoal

| ID | Origem | Destino | Estado | Evidência / lacuna principal |
|---|---|---|---|---|
| GKR-TRN-001 | PER-001 | PER-002 | parcial | continuidade entre pacotes |
| GKR-TRN-002 | PER-002 | PER-003 | localmente validada | UXA-035 + contratos correntes de entrada protegida |
| GKR-TRN-003 | PER-003 | PER-004 | parcial | integração entrada protegida → expressão guiada ainda parcial |
| GKR-TRN-004 | PER-004 | PER-005 | parcial | integração expressão–inventário |
| GKR-TRN-005 | PER-005 | PER-006 | parcial | continuidade entre materializações |
| GKR-TRN-006 | PER-006 | PER-007 | localmente validada | UXA-037 |
| GKR-TRN-007 | PER-007 | PER-008 | **integralmente validada** | UXA-097 |
| GKR-TRN-008 | PER-008 | PER-010 | **integralmente validada** | GKR-UX-D5-C4B-001 — Hoje recorrente → acesso a Objetivos; contexto mínimo, revalidação, retorno, interrupção, concorrência e idempotência examinados |
| GKR-TRN-009 | PER-010 | PER-008 | **integralmente validada** | GKR-UX-D5-C4B-001 — retorno `‹ Hoje` neutro; não salva edição incompleta, não altera prioridade/progresso e reconsulta estado canônico |
| GKR-TRN-010 | PER-008 | PER-011 | **integralmente validada** | GKR-UX-D5-C4B-001 — `Abrir este passo` preserva somente referência lógica mínima quando vigente; fallback neutro/atualizado |
| GKR-TRN-011 | PER-011 | PER-008 | **integralmente validada** | GKR-UX-D5-C4B-001 — retorno não marca passo como visto/aceito/iniciado/executado/concluído; Hoje reconsulta estado vigente |
| GKR-TRN-012 | PER-008 | PER-012 | **integralmente validada** | GKR-UX-D5-C4B-001 — entrada genérica/neutra; sem trajetória/domínio/interpretação/evidência sensível por padrão; privacidade revalidada |
| GKR-TRN-013 | PER-012 | PER-008 | **integralmente validada** | GKR-UX-D5-C4B-001 — retorno não confirma interpretação/evolução; natureza epistemológica, minimização e permissões preservadas |

`TRN-007` preserva consentimento, estado canônico, retorno e idempotência; navegar para Hoje não cria avanço ou autorização adicional.

`TRN-008..013` são handoffs de navegação protegida integralmente validados no limite documental. Abrir uma responsabilidade especializada não cria, confirma ou altera automaticamente o objeto funcional correspondente. Retornar a Hoje não equivale a concluir, aceitar, reconhecer evolução ou conceder nova autorização.

Para `TRN-008`, `TRN-010` e `TRN-012`, a validação aplica-se ao **estado recorrente de PER-008 quando o affordance correspondente estiver presente e aplicável**. A primeira variante de Hoje da UXA-097 não é obrigada a materializar esses três acessos.

O modelo corrente não registra handoffs diretos `PER-010 ↔ PER-011`, `PER-011 ↔ PER-012` ou `PER-010 ↔ PER-012`. Relação semântica entre capacidades não equivale automaticamente a navegação direta.

## 5. Pessoa em Coletivos e operação do responsável

| ID | Origem | Destino | Perspectiva | Condição e efeito principal | Evidência | Estado | Lacuna |
|---|---|---|---|---|---|---|---|
| GKR-TRN-101 | PER-101 | PER-102 | visitante | pesquisar/filtrar sem criar vínculo | UXA-056 | localmente validada | continuidade entre responsabilidades |
| GKR-TRN-102 | PER-102 | PER-103 | visitante | abrir Perfil Público | UXA-056 | parcial | ligação ponta a ponta ainda parcial |
| GKR-TRN-103 | PER-103 | PER-104 | solicitante potencial | iniciar revisão consciente | UXA-056 | parcial | handoff para solicitação |
| GKR-TRN-104 | PER-104 | PER-105 | solicitante | enviar solicitação autorizada | UXA-056 | parcial | continuidade até estado pendente |
| GKR-TRN-105 | PER-105 | COL-003 | solicitante → responsável | disponibilizar solicitação com mesmo identificador lógico | UXA-056/089/090 | **integralmente validada** | — |
| GKR-TRN-106 | COL-003 | PER-105 | responsável → solicitante | pedir informação adicional sem aprovar | UXA-056/089/090 | **integralmente validada** | — |
| GKR-TRN-107 | PER-105 | COL-003 | solicitante → responsável | responder à mesma finalidade sem duplicação | UXA-056/089/090 | **integralmente validada** | — |
| GKR-TRN-108 | COL-003 | PER-106 | responsável → participante | aprovação forma vínculo; navegação posterior é opcional | UXA-089/090/092 | **integralmente validada** | — |
| GKR-TRN-109 | COL-003 | PER-105 | responsável → solicitante | recusar com fundamento proporcional | UXA-056/089/090 | **integralmente validada** | — |
| GKR-TRN-110 | PER-106 | PER-107 | participante | abrir Central sem alterar vínculo ou leitura | UXA-092/093/094/096 | **integralmente validada** | — |
| GKR-TRN-111 | PER-107 | PER-108 | participante | abrir início do mesmo Coletivo com permissão revalidada | UXA-096 | **integralmente validada** | — |
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

Abrir Planos voluntariamente é navegação administrativa e não constitui seleção de plano, contratação, cobrança ou alteração de entitlement.

### 8.1 Pessoa

| ID | Origem | Destino | Estado | Lacuna |
|---|---|---|---|---|
| GKR-TRN-401 | PER-301 | PER-302 | **localmente validada** | gateway/execução financeira |
| GKR-TRN-402 | PER-302 | PER-304 | **localmente validada** | processamento financeiro real |
| GKR-TRN-403 | PER-301 | PER-303 | **localmente validada** | regra financeira entre ciclos |
| GKR-TRN-404 | PER-303 | PER-304 | **localmente validada** | execução do entitlement |
| GKR-TRN-405 | PER-304 | PER-301 | **localmente validada** | persistência técnica |
| GKR-TRN-406 | PER-009 | PER-301 | **contratada** | `PER-009` ainda sem materialização visual suficiente para validação ponta a ponta |
| GKR-TRN-407 | PER-301 | PER-009 | **contratada** | retorno canônico conhecido; origem/destino de Conta ainda sem materialização própria |

`TRN-406/407` formalizam exclusivamente a origem e o retorno voluntários. Repetir a navegação não duplica efeito, e retornar não equivale a cancelar assinatura ou alterar plano.

### 8.2 Coletivo

| ID | Origem | Destino | Estado | Lacuna |
|---|---|---|---|---|
| GKR-TRN-411 | COL-301 | COL-302 | **localmente validada** | gateway/execução financeira |
| GKR-TRN-412 | COL-302 | COL-304 | **localmente validada** | processamento financeiro real |
| GKR-TRN-413 | COL-301 | COL-303 | **localmente validada** | regra financeira entre ciclos |
| GKR-TRN-414 | COL-303 | COL-304 | **localmente validada** | execução operacional/transacional |
| GKR-TRN-415 | COL-304 | COL-301 | **localmente validada** | persistência técnica |
| GKR-TRN-416 | COL-301 | BND-002 | **parcial** | processo posterior de contratação/dimensionamento assistido não materializado |
| GKR-TRN-417 | COL-002 | COL-301 | **integralmente validada** | navegação administrativa sem mutação comercial; contexto e autoridade preservados pelo contrato corrente |
| GKR-TRN-418 | COL-301 | COL-002 | **integralmente validada** | retorno à Visão Geral sem alteração de plano/capacidade; contrato corrente |

`TRN-416` não significa “ir para Enterprise”. Ele significa sair do autoatendimento quando a contratação concreta exigir assistência. A maturidade permanece parcial.

`TRN-417/418` não promovem `TRN-411..416` nem comprovam cobrança, contratação ou persistência técnica de entitlement.

### 8.3 Organização

| ID | Origem | Destino | Estado | Lacuna |
|---|---|---|---|---|
| GKR-TRN-421 | ORG-301 | ORG-302 | **localmente validada** | gateway/execução financeira |
| GKR-TRN-422 | ORG-302 | ORG-304 | **localmente validada** | processamento financeiro real |
| GKR-TRN-423 | ORG-301 | ORG-303 | **localmente validada** | regra financeira entre ciclos |
| GKR-TRN-424 | ORG-303 | ORG-304 | **localmente validada** | execução institucional |
| GKR-TRN-425 | ORG-304 | ORG-301 | **localmente validada** | persistência técnica |
| GKR-TRN-426 | ORG-301 | BND-002 | **parcial** | processo posterior de contratação/dimensionamento assistido não materializado |
| GKR-TRN-427 | ORG-001 | ORG-301 | **integralmente validada** | navegação institucional sem mutação comercial; Organização/unidade/autoridade preservadas pelo contrato corrente |
| GKR-TRN-428 | ORG-301 | ORG-001 | **integralmente validada** | retorno à Visão Geral sem alteração comercial; contrato corrente |

`TRN-426` não significa “ir para Business Scale”. A Organização permanece participante e Guivos Business permanece produto separado. A maturidade da transição continua parcial.

`ORG-001` usa a nomenclatura institucional corrente; Guivos Business permanece produto especializado separado.

### 8.4 Guivos Business

Guivos Business constitui o quarto contexto corrente desta leitura integrada, mas **não possui IDs `GKR-TRN-*` próprios neste Registry**.

Sua continuidade vigente é governada por:

- `GPA-004 — Guivos Business`;
- `GPA-004-FUNCTIONAL-PORTFOLIO-001`;
- `GKR-PLANS-BUSINESS-001`;
- `GKR-JOURNEY-BUSINESS-001`;
- autoridades correntes da Home Business.

A continuidade funcional de referência é:

```text
HOME BUSINESS
→ OFERTA(S)
→ PLANOS / CAPACIDADE
→ CONFIGURADOR
→ CONTRATAÇÃO ONLINE
→ SELF-SERVICE / SUPORTE / GERENCIADO
→ OPERAÇÃO
```

A ausência de IDs próprios não autoriza reutilizar `ORG-*`, `COL-*`, `COM-*` ou `BND-002` como substitutos de Business.

```text
BUSINESS
≠ ORGANIZAÇÃO
≠ COM-* / ADS
≠ BND-002
```

Novos IDs Business somente devem ser criados quando uma necessidade funcional concreta exigir granularidade adicional e houver ato governado próprio.

## 9. BND-002

`BND-002` é a fronteira genérica de **contratação/dimensionamento assistido**.

A fronteira poderá ser alcançada quando a necessidade real exigir proposta, dimensionamento, análise específica, contrato ou configuração assistida. O nome do plano, isoladamente, não é autoridade suficiente para determinar o handoff.

A correção semântica preservada:

- não transforma `BND-002` em checkout;
- não promove `TRN-416` ou `TRN-426`;
- não cria fluxo de Guivos Business.

## 10. Preservações de maturidade

- transições totais permanecem **66**;
- `TRN-008..013` estão **integralmente validadas** no limite documental;
- `TRN-406/407` ficam **contratadas** até materialização suficiente de `PER-009`;
- `TRN-417/418` e `TRN-427/428` ficam **integralmente validadas** no limite documental de navegação administrativa;
- `TRN-401..405`, `TRN-411..415` e `TRN-421..425` permanecem localmente validadas;
- `TRN-205` permanece integralmente validada até `BND-001`;
- nenhum comportamento posterior a `BND-001` é atribuído à Guivos;
- `TRN-304`, `TRN-305`, `TRN-306`, `TRN-416` e `TRN-426` permanecem parciais;
- validação documental continua distinta de implementação técnica.

## 11. Próximo gate

A maturidade corrente deve ser lida diretamente neste registro e nas autoridades específicas citadas. Frentes futuras ou de implementação permanecem separadas e exigem autorização própria.
