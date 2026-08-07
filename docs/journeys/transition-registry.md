---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.15.0
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
  - UXA-096
  - UXA-097
  - UXA-098
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas.

A versão 0.15.0 preserva as 37 transições. A UXA-098 valida `GKR-TRN-203`, `GKR-TRN-204`, `GKR-TRN-210` e `GKR-TRN-211` ponta a ponta, sem criar nova transição.

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
| GKR-TRN-007 | PER-007 | PER-008 | **integralmente validada** | **UXA-097 — primeira Hoje materializada; escolhas, autorização, estado canônico, retorno e idempotência validados** |

### 4.1 Contrato validado de `GKR-TRN-007`

```text
PER-007
→ escolhas compatíveis são confirmadas explicitamente
→ condição de persistência/personalização torna-se efetiva sem ampliação implícita
→ TRN-007
→ PER-008 consulta o estado canônico vigente
→ primeira Tela Hoje não presume avanço nem mudança anterior
```

Regras integradas:

- personalização autorizada usa somente base confirmada, autorizada e vigente;
- sem personalização ou com decisão adiada, Hoje continua acessível sem indicações pessoais;
- `Excluir compreensão e continuar explorando` não pertence a `TRN-007`;
- retirada, exclusão ou mudança posterior prevalecem sobre estado visual obsoleto;
- clique repetido, retorno ou recarga não criam duas jornadas, Próximos Passos ou efeitos de persistência;
- navegar para Hoje não conta como evolução, presença, streak ou confirmação adicional;
- a Tela Hoje recorrente permanece distinta da primeira variante validada pela UXA-097.

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
| GKR-TRN-110 | PER-106 | PER-107 | participante | escolher `Ver atualizações`; abrir Central sem alterar vínculo ou leitura; preservar origem/natureza/autoridade/ação/prazo | vínculo/autorização pertinente; retorno não altera estado; ação substantiva revalida estado canônico; repetição de abertura/leitura é idempotente | UXA-092 na origem; UXA-093 materialização; UXA-094 validação integrada; PER-107 corrente revalidado UXA-096 | **integralmente validada** | — |
| GKR-TRN-111 | PER-107 | PER-108 | participante | escolher `Abrir início do Coletivo`; evento histórico não concede acesso; preservar mesmo Coletivo e vínculo lógico sem alterar leitura, papel, presença ou autoridade | vínculo atual/permissão revalidados; estado canônico prevalece; retorno neutro; repetição idempotente; permissão revogada não é restaurada | UXA-095 materialização/refinamento; UXA-096 validação integrada | **integralmente validada** | — |
| GKR-TRN-112 | COL-002 | COL-003 | responsável | abrir fila especializada preservando Coletivo e escopo | representação/autoridade vigentes; navegação não altera fila | UXA-087; UXA-089; UXA-090 | **integralmente validada** | — |
| GKR-TRN-113 | COL-004 | COL-005 | responsável | comunicar a participantes autorizados | papel e escopo de audiência | UXA-058; UXA-059 | contratada | operação interna não materializada |

### 5.1 Contrato preservado de `GKR-TRN-110`

A UXA-098 não altera `TRN-110`: entrada na Central continua neutra, leitura continua separada de efeito substantivo, ações revalidam estado canônico e segurança material preserva prioridade legítima.

### 5.2 Contrato preservado de `GKR-TRN-111`

A UXA-098 não altera `TRN-111`. Permanecem vigentes as regras de vínculo atual, permissão revalidada, retorno neutro, estado canônico e idempotência estabelecidas pela UXA-096.

## 6. Organização, oportunidades e relações bilaterais

| ID | Origem | Destino | Estado | Evidência / lacuna principal |
|---|---|---|---|---|
| GKR-TRN-201 | ORG-001 | ORG-002 | parcial | ligação com visão institucional |
| GKR-TRN-202 | ORG-002 | ORG-003 | localmente validada | distribuição entre superfícies |
| GKR-TRN-203 | ORG-003 | PER-201 | **integralmente validada** | **UXA-098 — ativação elegível à descoberta sem garantia de distribuição; estado canônico e idempotência validados** |
| GKR-TRN-204 | PER-201 | PER-203 | **integralmente validada** | **UXA-098 — Mapa → Detalhe com mesma oportunidade, revalidação do estado e retorno preservado** |
| GKR-TRN-205 | PER-203 | BND-001 | parcial | efeito externo não validado |
| GKR-TRN-206 | ORG-004 | COL-008 | contratada | superfícies bilaterais ausentes |
| GKR-TRN-207 | COL-008 | ORG-005 | contratada | interface bilateral ausente |
| GKR-TRN-208 | ORG-005 | ORG-006 | contratada | operação bilateral não materializada |
| GKR-TRN-209 | ORG-006 | ORG-006 | contratada | estados operacionais ausentes |
| GKR-TRN-210 | PER-201 | PER-202 | **integralmente validada** | **UXA-098 — mesma consulta, contexto, região, filtros, seleção e permissões preservados** |
| GKR-TRN-211 | PER-202 | PER-203 | **integralmente validada** | **UXA-098 — Lista → Detalhe com identidade, estado e retorno preservados** |

### 6.1 Contrato validado de `GKR-TRN-203`

```text
ORG-003
→ oportunidade aprovada, ativa e materialmente vigente
→ TRN-203
→ candidata ao inventário descobrível de PER-201
```

Elegibilidade à descoberta não garante impressão, posição, recomendação, alcance ou relevância individual. Pausa, expiração, encerramento ou mudança material prevalecem sobre cartões obsoletos. Reprocessamento do mesmo estado é idempotente.

### 6.2 Contrato validado de `GKR-TRN-210`

Mapa e Lista são representações da mesma consulta. A alternância preserva contexto de atuação, origem, região, busca, filtros, versão conhecida dos resultados, seleção e permissões territoriais. Mudar o modo não cria autorização, personalização, relevância ou efeito comercial.

### 6.3 Contrato validado de `GKR-TRN-204` e `GKR-TRN-211`

Mapa e Lista conduzem ao mesmo `PER-203` canônico. O Detalhe preserva a identidade lógica e a origem de retorno, consulta o estado material vigente antes de ação substantiva e não transforma abertura em interesse, inscrição, recomendação ou evolução.

`TRN-204` e `TRN-211` terminam no Detalhe. O efeito externo posterior permanece exclusivamente em `GKR-TRN-205`.

### 6.4 Fronteira comercial preservada

Opportunity Boost não altera o contrato orgânico: pagamento amplia distribuição publicitária identificada, não relevância funcional. `TRN-304` e `TRN-306` permanecem fora da UXA-098.

## 7. Opportunity Boost

| ID | Origem | Destino | Estado | Lacuna principal |
|---|---|---|---|---|
| GKR-TRN-301 | COM-001 | COM-004 | parcial | estados residuais e regras econômicas |
| GKR-TRN-302 | COM-004 | COM-002 | parcial | integração com superfícies orgânicas |
| GKR-TRN-303 | COM-003 | COM-002 | localmente validada | continuidade transversal |
| GKR-TRN-304 | COM-002 | PER-201 | parcial | integração orgânico–patrocinado |
| GKR-TRN-305 | COM-004 | COM-005 | parcial | dez estados residuais UXA-055 |
| GKR-TRN-306 | COM-002 | PER-202 | parcial | retorno patrocinado → lista orgânica |

## 8. Efeito da UXA-098

- transições totais: 37;
- nenhuma transição nova;
- `TRN-203`: não examinada → **integralmente validada**;
- `TRN-204`: parcial → **integralmente validada**;
- `TRN-210`: parcial → **integralmente validada**;
- `TRN-211`: parcial → **integralmente validada**;
- `TRN-205`, `TRN-304` e `TRN-306` permanecem fora do escopo;
- `TRN-007`, `TRN-110` e `TRN-111` permanecem integralmente validadas;
- oito handoffs integralmente validados no trecho de Coletivos permanecem inalterados.

## 9. Próximo gate

Com `V2` encerrada documentalmente pela UXA-098, a próxima prioridade registrada é `V3 — dez estados residuais UXA-055`. **UXA-099 não foi iniciada.**