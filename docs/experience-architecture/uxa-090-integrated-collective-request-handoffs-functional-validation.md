---
id: UXA-090
title: Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos
status: active
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
  - UXA-088
  - UXA-089
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-105
  - GKR-SURF-PER-106
  - GKR-SURF-COL-002
  - GKR-SURF-COL-003
  - GKR-TRN-105
  - GKR-TRN-106
  - GKR-TRN-107
  - GKR-TRN-108
  - GKR-TRN-109
  - GKR-TRN-112
  - GKR-JOURNEY-GAPS-001
  - M7.77
normative: false
---

# Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos

## 1. Finalidade

A UXA-090 examina como conjunto as ligações já materializadas entre a perspectiva da Pessoa e a operação do responsável do Coletivo.

O objetivo é responder:

> **O mesmo pedido, com o mesmo estado, finalidade, autoridade e consequência, atravessa as duas perspectivas sem coerção, perda de contexto, decisão duplicada ou sobrescrita de um evento mais recente?**

O pacote valida somente os handoffs cujos endpoints já possuem cobertura suficiente:

- `GKR-TRN-105` — solicitação disponível para análise;
- `GKR-TRN-106` — pedido de informação adicional;
- `GKR-TRN-107` — resposta adicional;
- `GKR-TRN-109` — recusa;
- `GKR-TRN-112` — Visão Geral do Responsável → gestão de solicitações.

`GKR-TRN-108` não é fechável nesta frente porque `GKR-SURF-PER-106 — Meus Coletivos` permanece ausente.

## 2. Autoridades utilizadas

A inspeção integra:

- UXA-056 — contrato funcional de participação em Coletivos;
- UXA-066/067 — Solicitação Pendente e seus estados na perspectiva da Pessoa;
- UXA-086/087 — Visão Geral do Responsável;
- UXA-088/089 — gestão de solicitações na perspectiva responsável;
- Registro de Superfícies;
- Registro de Transições;
- Jornada Integrada do Coletivo;
- Registro de Lacunas.

## 3. Critérios do gate integrado

Cada ligação elegível foi examinada em:

1. identidade estável da solicitação;
2. estado canônico compartilhado entre perspectivas;
3. autoridade verificada no momento do efeito;
4. finalidade e minimização dos dados transferidos;
5. correspondência entre ação emitida e consequência recebida;
6. voluntariedade e contestação aplicáveis;
7. referência temporal sem promessa indevida;
8. retorno e interrupção sem decisão implícita;
9. resolução de concorrência entre cancelamento, expiração, resposta e decisão;
10. efeito lógico único diante de repetição ou reenvio;
11. ausência de promoção automática de reputação, função ou autoridade;
12. ausência de dependência em superfície não materializada.

Falha material em identidade, autoridade, concorrência, dados ou consequência impede validação integrada.

## 4. Contrato transversal consolidado

A validação integrada exige as regras abaixo, independentemente de implementação técnica futura.

### 4.1 Identidade estável

Uma solicitação mantém o mesmo identificador lógico enquanto atravessa Pessoa e responsável. Mudança de tela, fila, análise protegida, pedido adicional ou resultado não cria um novo pedido silenciosamente.

### 4.2 Estado canônico

Existe um único estado lógico vigente para a solicitação. As superfícies podem apresentar perspectivas diferentes, mas não podem sustentar estados contraditórios como igualmente válidos.

### 4.3 Revalidação antes de efeito

Antes de um ato com consequência, o estado vigente e a autoridade aplicável precisam continuar válidos. Uma tela aberta anteriormente não congela o direito de decidir.

### 4.4 Concorrência e obsolescência

Quando eventos competem:

- cancelamento confirmado pela Pessoa impede decisão posterior baseada em estado anterior;
- expiração válida impede decisão tardia como se o pedido continuasse pendente;
- resposta adicional recebida substitui o estado de espera anterior sem criar novo pedido;
- recusa já efetivada não pode ser repetida como novo efeito;
- uma ação sobre estado obsoleto deve ser interrompida e o estado atual apresentado.

A UXA-090 define o comportamento esperado, não API, lock, fila ou mecanismo técnico.

### 4.5 Efeito lógico único

Repetição de clique, reenvio, atualização de tela ou repetição de entrega não pode produzir duas decisões, dois pedidos adicionais ou dois vínculos lógicos para a mesma ação confirmada.

### 4.6 Dados mínimos

Somente dados necessários à finalidade do handoff atravessam a fronteira entre perspectivas. Conteúdo da Jornada pessoal, outros Coletivos, atributos sensíveis irrelevantes e contatos privados desnecessários permanecem excluídos.

## 5. Validação de `GKR-TRN-105`

```text
PER-105 — solicitação pendente
→ GKR-TRN-105
→ COL-003 — fila/análise do responsável
```

**Resultado: integralmente validada.**

A ligação é válida porque:

- o mesmo pedido e seu identificador seguem para a operação responsável;
- dados transferidos são os previamente revisados e autorizados;
- disponibilidade para análise não equivale a aprovação;
- abrir ou ordenar a solicitação não muda prioridade substantiva;
- autoridade do responsável é verificada pelo escopo concedido;
- cancelamento ou expiração supervenientes tornam o estado anterior obsoleto;
- nenhuma informação adicional é inferida por simples recebimento.

## 6. Validação de `GKR-TRN-106`

```text
COL-003 — pedido adicional confirmado
→ GKR-TRN-106
→ PER-105 — informação adicional solicitada
```

**Resultado: integralmente validada.**

A ligação é válida porque:

- pergunta, finalidade, autoridade e referência temporal permanecem identificáveis;
- pedir informação não produz aprovação nem obrigação de revelar;
- `prefiro não responder`, contestação e cancelamento permanecem alternativas legítimas;
- acessibilidade não é convertida em critério oculto de entrada;
- pedido emitido sobre solicitação já cancelada, expirada ou encerrada não pode prevalecer;
- repetição do mesmo efeito não cria pedidos adicionais duplicados.

## 7. Validação de `GKR-TRN-107`

```text
PER-105 — resposta ou preferência revisada
→ GKR-TRN-107
→ COL-003 — análise retomada ou atualizada
```

**Resultado: integralmente validada.**

A ligação é válida porque:

- somente conteúdo conscientemente enviado atravessa a fronteira;
- descartar rascunho não produz handoff;
- preferir não informar continua distinto de recusa voluntária;
- a resposta permanece vinculada à pergunta e finalidade correspondentes;
- chegada de conteúdo adicional não cria vínculo nem garante aprovação;
- se o processo tiver sido validamente encerrado antes do recebimento, o conteúdo não reabre a solicitação silenciosamente;
- repetição de entrega não duplica o efeito lógico.

## 8. Validação de `GKR-TRN-109`

```text
COL-003 — recusa confirmada
→ GKR-TRN-109
→ PER-105 — resultado de recusa
```

**Resultado: integralmente validada.**

A ligação é válida porque:

- autoridade e fundamento são verificados antes do efeito;
- a condição utilizada foi previamente apresentada à Pessoa;
- o resultado recebido corresponde à decisão emitida;
- recusa permanece distinta de sanção, reputação, denúncia, cancelamento e expiração;
- nova exploração ou nova solicitação futura não reutiliza confirmação anterior;
- cancelamento ou expiração já vigentes não podem ser sobrescritos por decisão tardia;
- reenvio não cria segunda recusa lógica.

## 9. Validação de `GKR-TRN-112`

```text
COL-002 — Visão Geral do Responsável
→ GKR-TRN-112
→ COL-003 — gestão de solicitações
```

**Resultado: integralmente validada.**

A ligação é válida porque:

- o mesmo Coletivo representado é preservado;
- o escopo concedido atravessa a navegação sem ampliação;
- entrar na fila não executa decisão;
- falta de autoridade bloqueia a operação especializada;
- retorno à Visão Geral permanece disponível;
- a navegação não altera fila, estado da solicitação ou reputação.

## 10. `GKR-TRN-108` permanece parcial

`GKR-TRN-108` não é promovida nesta frente.

A análise identifica duas razões independentes:

1. `GKR-SURF-PER-106 — Meus Coletivos` ainda não está materializada;
2. a aprovação já possui um **resultado observável dentro de `PER-105`** antes da futura continuidade ao ambiente do participante.

Portanto, a UXA-090 preserva a seguinte fronteira:

```text
COL-003 — aprovação confirmada
→ resultado aprovado observável na família PER-105
→ continuidade futura para PER-106 ainda não materializada
```

O registro existente de `TRN-108` continua como dívida arquitetural a ser refinada em conjunto com a futura materialização de `PER-106`. A UXA-090 não cria nova transição nem altera IDs apenas para antecipar essa solução.

## 11. Resultado do gate

| Transição | Antes | Após UXA-090 |
|---|---|---|
| GKR-TRN-105 | parcial | integralmente validada |
| GKR-TRN-106 | parcial | integralmente validada |
| GKR-TRN-107 | parcial | integralmente validada |
| GKR-TRN-108 | parcial | parcial |
| GKR-TRN-109 | parcial | integralmente validada |
| GKR-TRN-112 | parcial | integralmente validada |

A validação de cinco handoffs não promove a Jornada do Coletivo como completa.

## 12. Efeito quantitativo

A UXA-090 não altera cobertura visual:

- SVGs: 105;
- associações individuais: 105;
- perfis de rastreabilidade: 25;
- validações funcionais de SVG: 95;
- pendentes de validação específica: 10, exclusivamente UXA-055;
- superfícies registradas: 40;
- transições registradas: 37.

O novo resultado é qualitativo: **cinco transições passam a possuir validação funcional ponta a ponta**.

## 13. Limites

A UXA-090 não:

- materializa `PER-106`, `PER-107` ou `PER-108`;
- fecha `GKR-TRN-108`;
- cria novo SVG;
- cria novo ID de superfície ou transição;
- implementa sincronização, locks, filas, APIs ou persistência;
- promove a Jornada do Coletivo;
- materializa `COL-004` a `COL-008`;
- altera Resultados Empresariais;
- inicia protótipo, teste com pessoas ou Engenharia de Produto;
- inicia UXA-091.

## 14. Veredito

**Aprovada com formalização contratual integrada.**

`GKR-TRN-105`, `106`, `107`, `109` e `112` possuem autoridade, dados, efeito, retorno, interrupção e resolução de concorrência suficientes para serem classificados como **integralmente validados** no escopo documental da experiência.

`GKR-TRN-108` permanece parcial e bloqueada pela ausência de `PER-106` e pela necessidade de refinar a passagem entre o resultado aprovado em `PER-105` e o ambiente futuro do participante.

## 15. Próxima transição possível

Após eventual integração e autorização separada, a próxima frente recomendada é:

> **UXA-091 — Materialização Controlada de Meus Coletivos (`GKR-SURF-PER-106`) e Refinamento da Continuidade Pós-Aprovação.**

A UXA-091 não é iniciada por esta validação.
