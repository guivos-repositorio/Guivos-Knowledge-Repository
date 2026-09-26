---
id: GKR-UX-PER302-MASTER-001
title: Jornada da Pessoa — PER-302 — Revisão de Contratação — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-PLANS-PERSON-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-301
  - GKR-SURF-PER-302
  - GKR-SURF-PER-304
  - GKR-TRN-401
  - GKR-TRN-402
---

# Jornada da Pessoa — PER-302 — Revisão de Contratação — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de `PER-302 — Revisão de Contratação` para Design, IA opcional, Produto, UX, Privacidade e Engenharia.

`PER-302` existe para que a Pessoa autenticada **revise conscientemente a mudança de plano pretendida antes de qualquer continuidade que possa produzir efeito comercial**.

A superfície governa compreensão e confirmação consciente da intenção. Não comprova checkout, pagamento, processamento financeiro ou ativação de entitlement.

## 2. Autoridades correntes

A leitura de `PER-302` deve preservar conjuntamente:

- `GKR-JOURNEY-SURFACE-DETAIL-PERSON-001` — contrato detalhado da superfície;
- `GKR-PLANS-PERSON-001` — planos, preços, capacidades e limites;
- `GEM-004-PLAN-TAXONOMY-AUTHORITY-001` — taxonomia vigente;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001` — maturidade das transições.

Nenhuma referência visual histórica substitui essas autoridades.

## 3. Papel funcional

A Pessoa deve conseguir:

1. reconhecer qual mudança iniciou em `PER-301`;
2. revisar o plano alvo;
3. revisar preço e recorrência quando legitimamente aplicáveis;
4. compreender pagador e beneficiário somente no limite da autoridade disponível;
5. distinguir revisão de contratação de pagamento concluído;
6. confirmar conscientemente a continuidade;
7. retornar sem contratar;
8. não sofrer alteração de plano apenas por entrar, revisar ou voltar.

## 4. Entrada — TRN-401

`GKR-TRN-401: PER-301 → PER-302`.

Estado: **localmente validada**.

A entrada ocorre após ação afirmativa em `PER-301` sobre uma mudança que exige revisão de contratação.

Entrar em `PER-302`:

- não contrata;
- não cobra;
- não ativa entitlement;
- não confirma pagamento;
- não autoriza inventar meio de pagamento;
- não torna a decisão irreversível.

Este Master não promove a maturidade de `TRN-401`.

## 5. Contexto mínimo recebido

A continuidade pode preservar somente o contexto necessário e autorizado, como:

- plano de origem, quando relevante e conhecido;
- plano alvo;
- preço de referência aplicável;
- recorrência escolhida quando a escolha existir e estiver governada;
- contexto mínimo de pagador/beneficiário quando legitimamente disponível.

A superfície não deve inferir dados financeiros ausentes.

## 6. Plano alvo

O plano alvo deve corresponder à taxonomia vigente da Pessoa:

```text
FREE
PLUS
PRO
```

`PER-302` não cria plano, variante comercial ou pacote adicional.

A revisão deve deixar claro qual plano está sendo considerado sem transformar essa apresentação em contratação consumada.

## 7. Preço

O preço apresentado deve vir da autoridade comercial vigente.

Baseline corrente:

| Plano | Mensal | Anual |
|---|---:|---:|
| **Free** | R$ 0,00 | R$ 0,00 |
| **Plus** | R$ 24,90 | R$ 249,00 |
| **Pro** | R$ 49,90 | R$ 499,00 |

Esses valores são referências comerciais vigentes. Este Master não comprova cobrança implementada.

Não inventar:

- desconto;
- promoção;
- cupom;
- taxa;
- imposto;
- parcelamento;
- economia percentual;
- trial;
- preço personalizado.

## 8. Recorrência

Quando a contratação pretendida distinguir mensal e anual, a recorrência deve ser explicitamente compreensível antes da continuidade.

A superfície não deve inferir:

- data de renovação;
- renovação automática implementada;
- data de cobrança;
- ciclo financeiro já iniciado;
- regra de proration.

## 9. Pagador e beneficiário

O registry reconhece `pagador/beneficiário` como conteúdo possível de `PER-302`.

Essa distinção não autoriza inventar arquitetura de gifting, dependentes, terceiros pagadores ou faturamento empresarial.

Quando não houver autoridade suficiente para distinguir papéis, a experiência deve permanecer no mínimo necessário e não fabricar relações.

Quando pagador e beneficiário forem diferentes, a continuidade substantiva exige que o confirmante seja **pagador autorizado**. Autenticação da Pessoa, isoladamente, não comprova autoridade financeira. Se essa autorização não puder ser estabelecida por fonte legítima, a continuidade por `TRN-402` deve permanecer bloqueada.

## 10. Revisão consciente

Antes da continuidade, a Pessoa deve conseguir compreender materialmente:

- o que está escolhendo;
- qual plano é alvo;
- qual preço de referência se aplica;
- qual recorrência foi selecionada, quando aplicável;
- a data de início aplicável;
- as informações vigentes sobre cancelamento e downgrade;
- que a ação seguinte é uma continuidade comercial e não mera navegação;
- que processamento e resultado ainda não estão comprovados nesta superfície.

## 11. Confirmação

A confirmação deve ser uma ação afirmativa, inequívoca e contextual, realizada por **pagador autorizado**. A superfície não pode habilitar continuidade substantiva quando a autoridade do pagador necessária não estiver comprovada.

Ela não pode ser produzida por:

- carregamento da tela;
- rolagem;
- seleção anterior em `PER-301`;
- foco em componente;
- retorno à superfície;
- opção pré-confirmada com efeito substantivo;
- inatividade.

Confirmar a continuidade em `PER-302` não permite afirmar que pagamento ou ativação foram concluídos.

## 12. Saída — TRN-402

`GKR-TRN-402: PER-302 → PER-304`.

Estado: **localmente validada**.

A transição representa continuidade após confirmação consciente dentro do fluxo documental.

A lacuna principal permanece: **processamento financeiro real**.

Portanto, `TRN-402` não pode ser descrita como prova de:

- pagamento aprovado;
- cobrança realizada;
- assinatura ativada;
- entitlement persistido;
- emissão fiscal;
- transação liquidada.

Este Master não promove a maturidade de `TRN-402`.

## 13. Retorno sem contratar

A reversibilidade é requisito explícito de `PER-302`.

A Pessoa pode voltar sem contratar.

O retorno:

- preserva o estado comercial anterior;
- não deve gerar cobrança;
- não deve criar assinatura;
- não deve ser tratado como falha;
- não deve exigir justificativa;
- não deve ocultar a alternativa de permanecer como está.

## 14. Estados internos de experiência

Sem novos IDs, Design pode representar estados como:

- carregamento;
- revisão disponível;
- plano alvo conhecido;
- recorrência conhecida;
- recorrência ainda não selecionada quando necessária;
- contexto comercial incompleto;
- pronta para confirmação;
- confirmação em continuidade;
- indisponibilidade temporária;
- erro recuperável;
- retorno voluntário.

Estado interno não cria nova superfície nem nova transição.

## 15. Dados incompletos ou inconsistentes

Se plano, preço, recorrência ou outro dado material necessário não puder ser confirmado por autoridade corrente:

```text
NÃO INFERIR
→ NÃO FABRICAR
→ NÃO CONFIRMAR SILENCIOSAMENTE
→ PRESERVAR RETORNO
```

A experiência deve bloquear uma confirmação enganosa quando faltar informação material indispensável.

## 16. Idempotência

Reabrir `PER-302`, revisar novamente ou repetir navegação não deve duplicar efeito comercial.

A confirmação de interface não pode ser usada como prova de processamento financeiro duplicável ou concluído.

## 17. Cobrança e meios de pagamento

Este Master não define nem comprova:

- cartão;
- Pix;
- boleto;
- carteira;
- gateway;
- tokenização;
- antifraude;
- autorização financeira;
- captura;
- liquidação;
- recorrência técnica;
- cobrança automática.

Nenhum desses elementos deve ser criado apenas para “completar” uma tela de contratação.

## 18. Fiscal e proration

Permanecem lacunas:

- regras fiscais;
- tributos;
- emissão fiscal;
- proration;
- créditos;
- compensações;
- estornos;
- cálculo entre ciclos.

A revisão não deve apresentar cálculos não governados como fatos.

## 19. Entitlement

`PER-302` não ativa capacidade.

A mudança efetiva de entitlement depende de autoridade e implementação posteriores.

A Pessoa não deve receber indicação de “plano ativo” apenas porque confirmou continuidade nesta superfície.

## 20. Autonomia e ausência de pressão

A revisão não deve usar:

- urgência inventada;
- escassez artificial;
- vergonha;
- perda fictícia;
- opção paga pré-confirmada;
- confirmação ambígua;
- obstáculos artificiais para voltar;
- claims de resultado garantido.

## 21. Privacidade e minimização

Somente dados necessários à revisão consciente podem ser apresentados ou solicitados.

Dados financeiros, identidade de terceiros e demais informações sensíveis exigem finalidade e autoridade próprias.

`PER-302` não é autorização genérica para coleta financeira.

## 22. Linguagem

A linguagem deve distinguir:

- **revisar** de contratar;
- **confirmar continuidade** de pagamento aprovado;
- **preço de referência** de valor efetivamente cobrado;
- **recorrência escolhida** de renovação técnica implementada;
- **intenção** de entitlement ativo.

## 23. Acessibilidade

Plano alvo, preço, recorrência, consequências da continuidade, retorno e ação afirmativa devem ser compreensíveis sem depender exclusivamente de cor, posição, ícone, animação ou som.

A confirmação deve ter nome e contexto semanticamente compreensíveis por tecnologias assistivas.

## 24. Conteúdo sintético

Prototipação pode usar conteúdo sintético claramente identificado, mas não pode inventar como autoridade:

- identidade real de pagador;
- dados de cartão;
- cobrança;
- transação;
- desconto;
- imposto;
- status de pagamento;
- entitlement;
- renovação.

## 25. Liberdade criativa de Design

Não existe baseline visual canônica imposta por este Master.

A designer mantém liberdade sobre composição, hierarquia, componentes, responsividade, motion, microinterações e forma de revisão, preservando:

- clareza da intenção;
- dados comerciais autorizados;
- ação afirmativa;
- reversibilidade;
- acessibilidade;
- ausência de efeito financeiro inventado;
- autoridades correntes de marca.

## 26. Limites para IA

IA não pode:

- alterar plano ou preço;
- inventar promoção;
- inventar meio de pagamento;
- simular cobrança;
- afirmar aprovação financeira;
- ativar entitlement;
- inventar proration;
- promover `TRN-401/402`;
- criar novos IDs;
- impor baseline visual;
- iniciar Product Engineering.

## 27. Critérios de aceite funcional

O consumo de `PER-302` é aceitável quando:

1. a entrada ocorre a partir de intenção afirmativa governada;
2. plano alvo é identificável;
3. preço vem da autoridade corrente;
4. recorrência é clara quando aplicável;
5. dados ausentes não são inferidos;
6. pagador/beneficiário não são expandidos além da autoridade;
7. pagador autorizado é requisito para confirmação substantiva;
8. data de início é apresentada quando aplicável e autorizada;
9. informações vigentes sobre cancelamento e downgrade são apresentadas antes da continuidade;
10. revisão precede continuidade;
11. confirmação é afirmativa;
12. entrar na superfície não contrata;
13. revisar não contrata;
14. voltar não contrata;
15. retorno é possível sem penalidade artificial;
16. TRN-401 permanece localmente validada;
17. TRN-402 permanece localmente validada;
18. processamento financeiro real não é presumido;
19. gateway não é inventado;
20. meio de pagamento não é inventado;
21. fiscal não é inventado;
22. proration não é inventada;
23. entitlement não é ativado por inferência;
24. repetição não duplica efeito;
25. autonomia é preservada;
26. privacidade e minimização são preservadas;
27. acessibilidade é preservada;
28. Design mantém liberdade criativa;
29. nenhum novo ID é criado;
30. Product Engineering permanece não liberado.

## 28. Lacunas abertas

Permanecem fora deste Master:

- processamento financeiro real;
- gateway;
- meios de pagamento;
- autorização/captura/liquidação;
- antifraude;
- fiscal;
- proration;
- estorno;
- persistência de entitlement;
- regras técnicas de renovação;
- resultado/recuperação de `PER-304`;
- implementação ponta a ponta;
- validação integral de `TRN-401/402`.

## 29. Estado

```text
PER-302
→ DOCUMENTED IN GOVERNED SCOPE

MASTER
→ GKR-UX-PER302-MASTER-001 v0.1.0
→ CURRENT CANDIDATE

TRN-401
→ LOCALLY VALIDATED / UNCHANGED

TRN-402
→ LOCALLY VALIDATED / UNCHANGED

CHECKOUT / FINANCIAL PROCESSING
→ NOT PROVEN

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Próxima superfície da coleção após a incorporação deste Master: `PER-303 — Downgrade e Cancelamento`.
