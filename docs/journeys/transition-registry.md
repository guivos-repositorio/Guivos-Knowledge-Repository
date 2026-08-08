---
id: GKR-JOURNEY-TRANSITION-REGISTRY-001
title: Registro Granular de Transições
status: active
version: 0.17.0
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
  - UXA-099
  - UXA-100
  - UXA-100-A2
  - UXA-100-A3
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-GAPS-001
normative: false
---

# Registro Granular de Transições

## 1. Finalidade

Este registro atribui identificadores estáveis às transições documentais conhecidas nas Jornadas Integradas.

A versão 0.17.0 adiciona dezessete transições canônicas da frente de Planos após a fragmentação da UXA-100-A3. A validação funcional dos SVGs pela UXA-100-A2 sustenta validação local das ligações internas, mas não comprova gateway, execução financeira ou processo comercial Enterprise/Scale.

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

### 6.1 Contrato V2 preservado

A UXA-100-A3 não altera as validações da UXA-098. Elegibilidade à descoberta continua sem garantia de impressão, posição, recomendação, alcance ou relevância individual. Mapa e Lista continuam modos da mesma consulta e o efeito externo posterior permanece em `GKR-TRN-205`.

### 6.2 Fronteira comercial preservada

Opportunity Boost não altera o contrato orgânico: pagamento amplia distribuição publicitária identificada, não relevância funcional. `TRN-304` e `TRN-306` permanecem parciais.

## 7. Opportunity Boost

| ID | Origem | Destino | Estado | Lacuna principal |
|---|---|---|---|---|
| GKR-TRN-301 | COM-001 | COM-004 | parcial | regras econômicas e integração ponta a ponta |
| GKR-TRN-302 | COM-004 | COM-002 | parcial | integração com superfícies orgânicas |
| GKR-TRN-303 | COM-003 | COM-002 | localmente validada | continuidade transversal |
| GKR-TRN-304 | COM-002 | PER-201 | parcial | integração orgânico–patrocinado |
| GKR-TRN-305 | COM-004 | COM-005 | **parcial** | **COM-005 validado pela UXA-099; ligação origem→estado residual ainda não examinada ponta a ponta** |
| GKR-TRN-306 | COM-002 | PER-202 | parcial | retorno patrocinado → lista orgânica |

### 7.1 Efeito da UXA-099 sobre `TRN-305`

A UXA-099 valida os destinos residuais de `COM-005`, inclusive erro, inventário, baixa oferta, falha material e controles da pessoa. Isso não comprova a ligação completa a partir de `COM-004` para todos os estados e contextos. `TRN-305` permanece parcial até validação específica de origem, destino, autoridade, efeito, retorno, interrupção e concorrência.

## 8. Planos, cobrança e ciclo de vida

### 8.1 Pessoa

| ID | Origem | Destino | Condição e efeito principal | Estado | Lacuna |
|---|---|---|---|---|---|
| GKR-TRN-401 | PER-301 | PER-302 | selecionar Plus/Pro afirmativamente e abrir revisão com preço, recorrência, pagador, beneficiário e início | **localmente validada** | gateway e execução financeira não implementados |
| GKR-TRN-402 | PER-302 | PER-304 | confirmar intenção; resultado distingue confirmação de falha sem ativação presumida | **localmente validada** | processamento financeiro real fora do escopo |
| GKR-TRN-403 | PER-301 | PER-303 | abrir downgrade/cancelamento sem ocultar permanência no plano atual | **localmente validada** | regra financeira entre ciclos ainda indefinida |
| GKR-TRN-404 | PER-303 | PER-304 | confirmar mudança após revisar capacidades, data efetiva e estado futuro | **localmente validada** | execução do entitlement não implementada |
| GKR-TRN-405 | PER-304 | PER-301 | retornar ao plano reconciliado, preservando estado anterior em falha | **localmente validada** | persistência técnica não examinada |

### 8.2 Coletivo

| ID | Origem | Destino | Condição e efeito principal | Estado | Lacuna |
|---|---|---|---|---|---|
| GKR-TRN-411 | COL-301 | COL-302 | selecionar Gestão/Impacto e revisar contratação | **localmente validada** | gateway e execução financeira não implementados |
| GKR-TRN-412 | COL-302 | COL-304 | confirmar intenção e receber resultado sem presumir ativação | **localmente validada** | processamento financeiro real fora do escopo |
| GKR-TRN-413 | COL-301 | COL-303 | abrir downgrade/cancelamento com capacidades atuais e futuras | **localmente validada** | regra financeira entre ciclos ainda indefinida |
| GKR-TRN-414 | COL-303 | COL-304 | confirmar após tratar publicações pagas/gratuitas, administradores, núcleos, compromissos e exportação | **localmente validada** | execução operacional/transacional não implementada |
| GKR-TRN-415 | COL-304 | COL-301 | retornar ao estado reconciliado preservando publicações/dados aplicáveis | **localmente validada** | persistência técnica não examinada |
| GKR-TRN-416 | COL-301 | BND-002 | solicitar proposta Enterprise e sair do autoatendimento | **parcial** | processo comercial posterior não materializado |

### 8.3 Organização

| ID | Origem | Destino | Condição e efeito principal | Estado | Lacuna |
|---|---|---|---|---|---|
| GKR-TRN-421 | ORG-301 | ORG-302 | selecionar Growth e revisar contratação | **localmente validada** | gateway e execução financeira não implementados |
| GKR-TRN-422 | ORG-302 | ORG-304 | confirmar intenção e receber resultado sem presumir ativação | **localmente validada** | processamento financeiro real fora do escopo |
| GKR-TRN-423 | ORG-301 | ORG-303 | abrir downgrade/cancelamento com capacidades atuais e futuras | **localmente validada** | regra financeira entre ciclos ainda indefinida |
| GKR-TRN-424 | ORG-303 | ORG-304 | confirmar após selecionar unidades, admins, publicações e Coletivos mantidos, integrações encerradas e dados exportados | **localmente validada** | execução institucional não implementada |
| GKR-TRN-425 | ORG-304 | ORG-301 | retornar ao estado reconciliado preservando direitos/dados aplicáveis | **localmente validada** | persistência técnica não examinada |
| GKR-TRN-426 | ORG-301 | BND-002 | solicitar proposta Business Scale e sair do autoatendimento | **parcial** | processo comercial posterior não materializado |

### 8.4 Regras transversais

- comparação incremental permanece estado de `*-301` e não cria transição própria;
- processamento transitório de pagamento permanece dentro de `*-302 → *-304`;
- falha é estado de `*-304`, preserva o plano anterior e fornece recuperação;
- downgrade/cancelamento não apagam dados silenciosamente nem prometem pró-rata;
- `BND-002` identifica somente a fronteira para proposta comercial;
- plano pago não altera relevância, confiança, impacto, legitimidade ou evolução.

## 9. Efeito da UXA-100-A3

- transições totais: **37 → 54**;
- 15 novas transições internas registradas como **localmente validadas**;
- 2 handoffs para `BND-002` registrados como **parciais**;
- nenhuma nova transição é declarada integralmente validada;
- `TRN-205`, `TRN-304`, `TRN-305` e `TRN-306` permanecem inalteradas;
- oito handoffs integralmente validados no trecho de Coletivos permanecem inalterados;
- validação documental continua distinta de implementação técnica.

## 10. Próximo gate

A promoção canônica de Planos fecha a definição de identidades e ligações da UXA-100. Validação ponta a ponta de cobrança real, processo comercial Enterprise/Scale e entradas contextuais a partir de superfícies ainda não registradas permanecem frentes futuras separadas. Nenhuma próxima UXA é iniciada automaticamente.