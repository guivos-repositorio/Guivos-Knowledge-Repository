---
id: GKR-UX-PER105-MASTER-001
title: Jornada da Pessoa — PER-105 — Solicitação Pendente — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: current_surface_design_definition
depends_on:
  - UXA-056
  - UXA-089
  - UXA-090
  - UXA-092
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-104
  - GKR-SURF-PER-105
  - GKR-SURF-PER-106
  - GKR-SURF-COL-003
  - GKR-TRN-104
  - GKR-TRN-105
  - GKR-TRN-106
  - GKR-TRN-107
  - GKR-TRN-108
  - GKR-TRN-109
---

# Jornada da Pessoa — PER-105 — Solicitação Pendente — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-105 — Solicitação Pendente` para designer humana, IA opcional, Produto, UX, Research, Privacidade e Engenharia.

A superfície permite à Pessoa **acompanhar a mesma solicitação lógica depois do envio, compreender seu estado, responder quando informação adicional for legitimamente necessária, cancelar quando aplicável e compreender o resultado**.

`PER-105` não é a fila operacional do responsável, não decide a solicitação, não cria prioridade, não é prova de participação e não é um feed genérico de atualizações.

## 2. Papel na Journey

```text
PER-104 — REVISÃO E SOLICITAÇÃO
→ SOLICITAÇÃO AUTORIZADA ENVIADA
→ TRN-104 / PARTIAL
→ PER-105 — SOLICITAÇÃO PENDENTE

PER-105
↔ COL-003 — GESTÃO DE SOLICITAÇÕES
→ MESMO IDENTIFICADOR LÓGICO

APROVAÇÃO AUTORIZADA
→ TRN-108 / INTEGRALLY VALIDATED
→ PER-106 — MEUS COLETIVOS
```

Abrir ou consultar `PER-105` não altera fila, prioridade, decisão ou vínculo.

## 3. Job da Pessoa

A superfície deve permitir que a Pessoa:

1. reconheça qual solicitação está acompanhando;
2. reconheça o Coletivo correspondente;
3. compreenda o estado corrente sem inferir resultado;
4. compreenda quem ou qual papel autorizado analisa, quando aplicável;
5. compreenda referência temporal ou prazo legítimo sem promessa;
6. saiba se alguma ação sua é necessária;
7. compreenda qual informação adicional foi solicitada e para qual finalidade;
8. responda somente à mesma finalidade legitimamente contratada;
9. cancele a solicitação quando a autoridade corrente permitir;
10. compreenda aprovação, recusa, expiração ou cancelamento sem ambiguidade;
11. reconheça o fundamento adequado quando exigido;
12. avance para a continuidade legítima sem ser coagida a navegar.

## 4. Objeto persistente: a mesma solicitação

A solicitação mantém o mesmo identificador lógico entre a perspectiva da Pessoa e a operação autorizada do Coletivo.

```text
MUDAR DE SUPERFÍCIE
≠ NOVA SOLICITAÇÃO

PEDIR INFORMAÇÃO
≠ NOVA SOLICITAÇÃO

RESPONDER INFORMAÇÃO
≠ NOVA SOLICITAÇÃO

MUDAR DE PERSPECTIVA
≠ NOVA SOLICITAÇÃO

RESULTADO
≠ NOVA SOLICITAÇÃO
```

A interface não pode representar repetição técnica, reabertura visual ou atualização de estado como pedidos independentes quando a autoridade mantém um único pedido lógico.

## 5. Estados correntes da solicitação

A autoridade `UXA-056` reconhece, conforme aplicabilidade:

- pendente;
- aguardando informação da Pessoa;
- aguardando decisão do Coletivo;
- cancelada pela Pessoa;
- aprovada;
- recusada;
- expirada.

Esses estados pertencem ao ciclo da solicitação. **Estado não cria novo `PER-ID` por inferência.**

### 5.1 Pendente

Deve comunicar que a solicitação existe e ainda não possui decisão final. Pendente não significa aprovação provável, posição de fila, prioridade ou promessa de atendimento.

### 5.2 Aguardando informação da Pessoa

Deve tornar compreensíveis:

- qual informação adicional é necessária;
- por que ela é necessária;
- quem a solicitou dentro da autoridade aplicável;
- eventual prazo legítimo;
- possibilidade de responder, não prosseguir ou cancelar quando aplicável.

Pedido de informação adicional não equivale a aprovação.

### 5.3 Aguardando decisão do Coletivo

Deve indicar que a próxima ação pertence à autoridade responsável do Coletivo. A Pessoa não deve ser induzida a repetir envio para obter prioridade.

### 5.4 Cancelada pela Pessoa

Deve distinguir cancelamento de recusa institucional. Cancelar não produz avaliação negativa automática e não deve ser apresentado como falha pessoal.

### 5.5 Aprovada

A aprovação autorizada **forma o vínculo**. O reconhecimento do resultado na perspectiva da Pessoa deve ser claro.

```text
APROVAÇÃO
→ VÍNCULO FORMADO

ABRIR PER-106 DEPOIS
→ NAVEGAÇÃO OPCIONAL
→ NÃO É O ATO QUE FORMA O VÍNCULO
```

### 5.6 Recusada

A recusa deve apresentar consequência compreensível e fundamento proporcional quando aplicável. Não cria pontuação negativa automática, exposição indevida ou conclusão sobre valor, reputação ou capacidade da Pessoa.

### 5.7 Expirada

Expiração deve ser distinguida de recusa, cancelamento e falha técnica. A superfície não pode inventar motivo, responsabilidade ou possibilidade de nova solicitação quando a autoridade não os fornecer.

## 6. Informações que podem ser exibidas

Quando legitimamente disponíveis e necessárias, `PER-105` pode exibir:

- identidade pública necessária do Coletivo;
- identificador ou referência compreensível da solicitação;
- estado corrente;
- data ou referência temporal relevante;
- prazo aplicável, quando realmente definido;
- papel autorizado responsável pela análise, quando aplicável;
- pedido de informação adicional e sua finalidade;
- informação já fornecida necessária para compreensão do pedido;
- decisão e fundamento adequado, quando existentes;
- consequência do resultado;
- ação legítima disponível à Pessoa.

Referência temporal não cria prioridade automática nem posição de fila.

## 7. Informações que podem ser solicitadas

Informação adicional só pode ser solicitada quando:

- houver finalidade clara e compatível com a solicitação original;
- for necessária e proporcional;
- a autoridade responsável puder legitimamente pedi-la;
- a Pessoa compreender a finalidade antes de responder.

Não solicitar ou reutilizar por conveniência:

- conteúdo protegido da Journey;
- relatos sensíveis não necessários;
- inferências pessoais não autorizadas;
- histórico de buscas;
- dados de outros vínculos;
- localização precisa sem necessidade;
- informação destinada a finalidade diferente.

## 8. Autoridade entre Pessoa e responsável

```text
PESSOA
→ autoridade sobre resposta e cancelamento nos limites contratados

RESPONSÁVEL DO COLETIVO
→ autoridade sobre análise e decisão no escopo legitimamente concedido

VISIBILIDADE
≠ TRANSFERÊNCIA DE AUTORIDADE
```

Nenhuma perspectiva recebe autoridade da outra apenas porque determinada informação se tornou visível.

## 9. Handoffs governados

### 9.1 TRN-105 — solicitação disponível para análise

`PER-105 → COL-003`.

Disponibiliza a mesma solicitação para análise sem criar aprovação, prioridade ou vínculo.

Estado: **integralmente validada**.

### 9.2 TRN-106 — pedido de informação adicional

`COL-003 → PER-105`.

Traz pedido legítimo de informação adicional sem aprovar e sem reiniciar silenciosamente a solicitação.

Estado: **integralmente validada**.

### 9.3 TRN-107 — resposta adicional

`PER-105 → COL-003`.

A resposta pertence à mesma solicitação e à mesma finalidade. Não duplica pedido.

Estado: **integralmente validada**.

### 9.4 TRN-108 — aprovação

`COL-003 → PER-106`.

A decisão autorizada de aprovação forma o vínculo. A navegação posterior é opcional.

Estado: **integralmente validada**.

### 9.5 TRN-109 — recusa

`COL-003 → PER-105`.

Produz resultado explícito e proporcional sem pontuação negativa automática ou exposição indevida.

Estado: **integralmente validada**.

### 9.6 TRN-104 — entrada em PER-105

`PER-104 → PER-105` permanece **partial**. Este Master não promove `TRN-104`.

## 10. Ações e controles

Conforme estado e autoridade, a Pessoa pode:

- consultar a solicitação;
- compreender o estado;
- revisar pedido de informação adicional;
- responder informação adicional;
- cancelar quando aplicável;
- reconhecer decisão;
- navegar para continuidade legítima;
- retornar sem produzir efeito indevido.

Nenhuma ação destrutiva, envio adicional ou cancelamento deve ser inferido por simples navegação.

## 11. Cancelamento

Cancelar uma solicitação já enviada pertence ao ciclo de `PER-105`, quando aplicável.

A experiência deve:

- exigir ação consciente;
- explicar consequência material antes do efeito;
- não confundir cancelamento com recusa;
- não fabricar nova solicitação;
- não atribuir culpa, reputação ou score;
- refletir o estado real após confirmação.

## 12. Prazo, espera, fila e prioridade

A superfície pode comunicar prazo ou referência temporal somente quando houver base legítima.

```text
TEMPO DECORRIDO
≠ PRIORIDADE

PRAZO
≠ POSIÇÃO NA FILA

CONSULTAR
≠ ACELERAR

REABRIR A TELA
≠ NOVA ANÁLISE
```

Não prometer SLA, aprovação ou ordem de atendimento ausentes das autoridades.

## 13. Regras materiais alteradas

Se regra material for alterada depois da solicitação e antes da ativação do vínculo, a autoridade corrente exige **nova revisão antes da ativação**.

A superfície deve tornar a mudança reconhecível e encaminhar a revisão legítima sem presumir consentimento. Este requisito não autoriza criar nova superfície ou transição ausente do Registry.

## 14. Estados internos de experiência

A designer pode representar, dentro de `PER-105`, estados como:

- carregamento/revalidação;
- solicitação pendente;
- aguardando informação da Pessoa;
- edição/resposta de informação adicional;
- envio da resposta em processamento;
- aguardando decisão;
- cancelamento em revisão;
- cancelamento em processamento;
- aprovada;
- recusada;
- expirada;
- erro recuperável;
- estado incerto exigindo revalidação;
- regra material alterada exigindo nova revisão.

Esses estados não criam novas superfícies canônicas.

## 15. Processamento, idempotência e recuperação

Durante efeitos assíncronos:

- mostrar processamento real quando necessário;
- impedir que repetição involuntária pareça criar nova solicitação ou resposta;
- não apresentar sucesso antes de confirmação real;
- preservar contexto em erro recuperável;
- revalidar estado quando o resultado estiver incerto;
- não converter demora em recusa;
- não fabricar aprovação, cancelamento, expiração ou vínculo.

A implementação técnica detalhada de idempotência permanece fora deste Documento Mestre.

## 16. Privacidade e minimização

A superfície deve preservar:

- finalidade explícita;
- minimização;
- acesso proporcional;
- separação entre Journey pessoal e operação do Coletivo;
- ausência de exposição de conteúdo protegido por conveniência operacional;
- ausência de reutilização silenciosa de dados para finalidade diferente.

Participação pretendida ou solicitação pendente não autoriza acesso irrestrito ao contexto pessoal.

## 17. Linguagem e claims

Evitar linguagem que:

- prometa aprovação;
- indique prioridade sem base;
- trate espera como mérito ou demérito;
- trate recusa como avaliação da Pessoa;
- confunda pedido de informação com pré-aprovação;
- confunda aprovação com clique posterior;
- trate solicitação como participação antes do resultado;
- atribua motivo não informado a expiração ou demora.

Preferir linguagem factual, proporcional e orientada ao estado real.

## 18. Acessibilidade

Estado, pedido de ação, prazo, decisão, erro e consequência devem ser compreensíveis sem depender exclusivamente de:

- cor;
- posição;
- animação;
- ícone;
- som.

Mudanças de estado e mensagens críticas devem ser perceptíveis por tecnologias assistivas, com ordem de foco e controles compatíveis com a ação.

## 19. Dados reais e conteúdo sintético

Nenhum Coletivo, responsável, pedido, prazo, critério, informação pessoal, fundamento, decisão ou resultado pode ser inventado e apresentado como real.

Para prototipação, conteúdo sintético é permitido quando:

- claramente fictício;
- não atribuído a pessoa ou entidade real;
- não usado para criar regra de produto;
- não sugere garantia de prazo ou resultado;
- respeita minimização e os estados canônicos.

## 20. Liberdade criativa de Design

Não existe baseline visual canônica imposta por este Master.

A designer possui liberdade sobre composição, agrupamento, densidade, componentes, ritmo, imagens, iconografia, motion, microinterações e responsividade, preservando:

- semântica dos estados;
- autoridade e privacidade;
- acessibilidade;
- handoffs governados;
- distinção entre espera, ação e decisão;
- autoridades atuais de marca, incluindo a tipografia oficial quando aplicável.

## 21. Limites para IA

IA não pode:

- inventar estado, decisão, fundamento, prazo, fila ou prioridade;
- criar novo pedido ao representar mudança de estado;
- responder ou cancelar em nome da Pessoa;
- aprovar ou recusar;
- preencher informação pessoal ausente como fato;
- reutilizar conteúdo protegido da Journey;
- tratar pedido de informação como aprovação;
- tratar recusa como score;
- tratar aprovação como dependente da navegação para `PER-106`;
- promover `TRN-104`;
- rebaixar `TRN-105..109`;
- criar novo `PER-ID`;
- impor baseline visual;
- iniciar Product Engineering.

## 22. Critérios de aceite funcional

O consumo de `PER-105` é aceitável quando:

1. a mesma solicitação lógica é preservada entre perspectivas;
2. o Coletivo é reconhecível;
3. o estado corrente é explícito;
4. consultar não altera fila ou prioridade;
5. prazo não é confundido com posição de fila;
6. pendência não promete aprovação;
7. pedido de informação adicional informa finalidade;
8. pedido de informação não equivale a aprovação;
9. resposta adicional não duplica solicitação;
10. a Pessoa mantém autoridade sobre responder e cancelar nos limites aplicáveis;
11. o responsável mantém autoridade de análise e decisão;
12. informação protegida da Journey não é exposta por conveniência;
13. cancelamento é distinto de recusa;
14. recusa possui consequência proporcional e não cria score negativo;
15. expiração é distinta de recusa e cancelamento;
16. aprovação forma o vínculo;
17. navegação para `PER-106` não é apresentada como ato constitutivo do vínculo;
18. `TRN-105` é preservada como integralmente validada;
19. `TRN-106` é preservada como integralmente validada;
20. `TRN-107` é preservada como integralmente validada;
21. `TRN-108` é preservada como integralmente validada;
22. `TRN-109` é preservada como integralmente validada;
23. `TRN-104` permanece partial;
24. regra material alterada exige nova revisão antes da ativação;
25. erros não fabricam resultado;
26. estados internos não criam novos `PER-ID`s;
27. conteúdo sintético não se apresenta como dado real;
28. acessibilidade não depende apenas de cor ou posição;
29. Design preserva liberdade criativa dentro das autoridades;
30. Product Engineering permanece não liberado.

## 23. Lacunas que não podem ser preenchidas por inferência

Este Master não autoriza inventar:

- política detalhada de decisão do responsável;
- critérios de aceite ausentes;
- SLA ou prioridade;
- posição de fila;
- possibilidade de nova solicitação após recusa ou expiração;
- rota não registrada para nova revisão de regra material;
- arquitetura técnica de notificações;
- novos estados canônicos;
- novas transições;
- novos `PER-ID`s;
- implementação de Product Engineering.

## 24. Estado

```text
PER-105
→ DOCUMENTED

MASTER
→ GKR-UX-PER105-MASTER-001 v0.1.0
→ CURRENT

TRN-104
→ PARTIAL / UNCHANGED

TRN-105
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-106
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-107
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-108
→ INTEGRALLY VALIDATED / UNCHANGED

TRN-109
→ INTEGRALLY VALIDATED / UNCHANGED

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Próxima superfície da coleção após a incorporação deste Master: `PER-106 — Meus Coletivos`.
