---
id: GKR-UX-PER304-MASTER-001
title: Jornada da Pessoa — PER-304 — Resultado e Recuperação de Plano/Cobrança — Documento Mestre de Superfície
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
  - GEM-004-A2
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-301
  - GKR-SURF-PER-302
  - GKR-SURF-PER-303
  - GKR-SURF-PER-304
  - GKR-TRN-402
  - GKR-TRN-404
  - GKR-TRN-405
---

# Jornada da Pessoa — PER-304 — Resultado e Recuperação de Plano/Cobrança — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de `PER-304 — Resultado e Recuperação de Plano/Cobrança` para Design, IA opcional, Produto, UX, Privacidade e Engenharia.

`PER-304` existe para comunicar de forma inequívoca o resultado conhecido de uma tentativa de contratação, alteração, downgrade, cancelamento ou tratamento de cobrança e, quando necessário, oferecer recuperação legítima sem fabricar sucesso.

A superfície não transforma intenção, clique, retorno técnico incompleto ou confirmação de interface em prova financeira, contratual ou de entitlement.

## 2. Autoridades correntes

A leitura deve preservar conjuntamente:

- `GKR-JOURNEY-SURFACE-DETAIL-PERSON-001`;
- `GKR-PLANS-PERSON-001`;
- `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`;
- `GEM-004-A2`;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001`.

Nenhuma referência visual histórica substitui essas autoridades.

## 3. Papel funcional

A Pessoa titular deve conseguir:

1. reconhecer qual operação originou o resultado;
2. distinguir sucesso confirmado, falha, pendência e estado indeterminado;
3. compreender o estado comercial efetivamente confirmado;
4. compreender o que mudou e o que permaneceu;
5. recuperar uma falha quando houver caminho legítimo;
6. corrigir meio de pagamento quando essa capacidade existir;
7. preservar dados e direitos durante falha;
8. retornar a Planos e Comparação;
9. não receber alegação de sucesso sem evidência suficiente.

## 4. Titularidade e gate

`GKR-SURF-PER-304` pertence à **Pessoa titular**.

A superfície deve preservar autenticação e autoridade adequadas ao resultado exibido. Não deve expor dados financeiros, de cobrança ou assinatura a ator sem autoridade legítima.

## 5. Entradas governadas

### 5.1 TRN-402

`GKR-TRN-402: PER-302 → PER-304`.

Estado: **localmente validada**.

Lacuna: **processamento financeiro real**.

A entrada representa continuidade após revisão de contratação, mas não comprova:

- pagamento aprovado;
- autorização financeira;
- captura;
- liquidação;
- assinatura ativa;
- entitlement persistido;
- emissão fiscal.

### 5.2 TRN-404

`GKR-TRN-404: PER-303 → PER-304`.

Estado: **localmente validada**.

Lacuna: **execução do entitlement**.

A entrada representa continuidade após revisão de downgrade/cancelamento, mas não comprova:

- downgrade efetivado;
- cancelamento efetivado;
- renovação interrompida;
- entitlement alterado;
- proration;
- estorno;
- persistência técnica.

Este Master não promove `TRN-402` ou `TRN-404`.

## 6. Princípio do resultado comprovável

`PER-304` deve comunicar somente estado suportado por fonte legítima.

```text
INTENÇÃO
≠ PROCESSAMENTO

PROCESSAMENTO
≠ SUCESSO

SUCESSO DE INTERFACE
≠ RESULTADO FINANCEIRO

RESULTADO FINANCEIRO
≠ ENTITLEMENT PERSISTIDO

SOLICITAÇÃO DE CANCELAMENTO
≠ CANCELAMENTO EFETIVADO
```

Quando a confirmação necessária estiver ausente, o estado deve permanecer pendente, indeterminado ou falho conforme evidência disponível.

## 7. Resultado confirmado

Quando houver confirmação suficiente, a superfície pode comunicar o resultado estritamente confirmado, por exemplo:

- plano corrente confirmado;
- operação concluída;
- alteração efetiva confirmada;
- cancelamento efetivo confirmado;
- renovação futura interrompida, se realmente confirmada;
- cobrança aprovada, se realmente confirmada;
- entitlement corrente, se realmente confirmado.

A interface deve evitar ampliar uma confirmação parcial para outros efeitos ainda não comprovados.

## 8. Resultado parcial ou pendente

Quando somente parte da cadeia estiver confirmada, a experiência deve distinguir o que já é conhecido do que permanece pendente.

Exemplo conceitual:

```text
DECISÃO REGISTRADA
→ CONFIRMADA

PROCESSAMENTO FINANCEIRO
→ PENDENTE

ENTITLEMENT
→ NÃO CONFIRMADO
```

Design pode expressar isso livremente sem converter o exemplo em modelo visual obrigatório.

## 9. Falha

Falha é estado legítimo e recuperável.

A superfície deve comunicar:

- o que falhou, quando conhecido;
- o que não foi alterado;
- se o plano anterior permanece vigente;
- qual ação de recuperação está realmente disponível;
- quando a Pessoa deve aguardar em vez de repetir;
- como retornar sem duplicar efeito.

Erro técnico genérico não deve ser apresentado como recusa financeira quando isso não for conhecido.

## 10. Falha de pagamento

A política comercial determina que falha de pagamento afete primeiro capacidades pagas.

Antes de redução decorrente de falha devem existir:

- comunicação clara;
- possibilidade de correção do meio de pagamento;
- período de tratamento definido futuramente;
- preservação de dados e direitos;
- retorno ao plano gratuito quando aplicável;
- proteção de compromissos transacionais já assumidos.

Como o período de tratamento ainda é lacuna aberta, este Master não define sua duração.

Falha de pagamento não autoriza:

- exposição pública;
- perda de dados próprios;
- interrupção de segurança.

## 11. Correção do meio de pagamento

Quando houver capacidade autorizada de corrigir meio de pagamento, `PER-304` pode encaminhar a Pessoa para essa recuperação.

Este Master não define:

- provedor;
- formulário;
- tokenização;
- armazenamento;
- antifraude;
- autenticação forte;
- retry automático;
- quantidade de tentativas.

A existência visual de uma ação não comprova que o processamento foi concluído.

## 12. Nova tentativa

Nova tentativa somente deve existir quando for tecnicamente e comercialmente legítima.

Repetir ação não deve:

- duplicar cobrança;
- duplicar assinatura;
- duplicar cancelamento;
- duplicar downgrade;
- gerar múltiplos registros substantivos;
- ocultar operação ainda pendente.

Quando o estado anterior estiver indeterminado, a experiência deve evitar induzir repetição cega.

## 13. Idempotência

Recarga, retorno, reabertura ou repetição de navegação não deve reproduzir efeito substantivo.

A experiência deve tratar idempotência como requisito funcional, sem inventar implementação técnica.

## 14. Estado comercial anterior

Na ausência de sucesso confirmado, a superfície não deve declarar alteração do plano corrente.

Quando a autoridade comprovar preservação do estado anterior, isso deve ser comunicado claramente.

Falha não é autorização para remover capacidades, salvo regra vigente e efeito realmente confirmado.

## 15. Entitlement

Entitlement só pode ser apresentado como alterado quando houver confirmação legítima.

`PER-304` não deve inferir entitlement a partir de:

- intenção;
- seleção de plano;
- confirmação em PER-302;
- confirmação em PER-303;
- resposta visual local;
- cobrança apenas iniciada;
- solicitação registrada.

A implementação de entitlement permanece lacuna de execução.

## 16. Downgrade

Em resultado de downgrade, a superfície deve distinguir:

- solicitação registrada;
- mudança programada, quando confirmada;
- mudança efetivada, quando confirmada;
- plano posterior efetivamente vigente;
- capacidades realmente alteradas.

Proration e crédito entre ciclos não podem ser inventados.

## 17. Cancelamento

Em resultado de cancelamento, a superfície deve distinguir:

- solicitação registrada;
- cancelamento efetivado;
- data efetiva confirmada;
- renovação futura efetivamente interrompida;
- plano/estado posterior confirmado.

A Pessoa não deve receber mensagem de cancelamento concluído apenas porque confirmou intenção em `PER-303`.

## 18. Cobrança

A superfície pode comunicar cobrança somente no limite do estado realmente confirmado.

Deve distinguir, quando aplicável e conhecido:

- tentativa;
- autorização;
- aprovação;
- falha;
- processamento pendente;
- liquidação.

Este Master não define a arquitetura do gateway nem cria novos estados financeiros normativos.

## 19. Recibo e confirmação

Quando existir recibo ou confirmação adequada autorizada, a experiência pode torná-lo acessível.

Ausência de recibo não autoriza fabricar documento, identificador fiscal, valor ou status.

## 20. Proration, crédito, estorno e reembolso

Permanecem fora do escopo definido:

- fórmula de proration;
- crédito entre ciclos;
- data de cobrança entre ciclos;
- valor de estorno;
- direito automático a reembolso;
- prazo de reembolso;
- método de devolução.

A superfície só pode exibir qualquer desses elementos quando outra autoridade os tiver definido e uma fonte real confirmar o caso concreto.

## 21. Período de tratamento

O período de tratamento de falha de pagamento permanece a definir.

A experiência não pode inventar:

- número de dias;
- data limite;
- carência;
- quantidade de tentativas;
- suspensão automática;
- momento de retorno ao gratuito.

## 22. Recuperação sem coerção

Recuperação deve resolver erro ou pendência, não converter vulnerabilidade em pressão comercial.

Não usar:

- culpa;
- medo;
- ameaça;
- urgência inventada;
- perda fictícia;
- countdown sem autoridade;
- bloqueio artificial de saída;
- upgrade como condição para corrigir erro.

## 23. Preservação de dados e direitos

Falha, downgrade ou cancelamento não autorizam automaticamente:

- perda de dados próprios;
- exposição pública;
- retirada de segurança;
- eliminação de histórico;
- revogação de direitos não relacionados;
- cancelamento de compromissos transacionais já assumidos.

Retenção, exclusão e portabilidade seguem autoridades próprias.

## 24. Estado sem resultado suficiente

Quando o sistema não puder determinar resultado confiável:

```text
NÃO INVENTAR SUCESSO
→ NÃO INVENTAR FALHA ESPECÍFICA
→ NÃO ALTERAR ESTADO POR INFERÊNCIA
→ EXPLICAR A INCERTEZA
→ OFERECER RECUPERAÇÃO LEGÍTIMA
→ PRESERVAR RETORNO
```

## 25. Saída — TRN-405

`GKR-TRN-405: PER-304 → PER-301`.

Estado: **localmente validada**.

Lacuna: **persistência técnica**.

O retorno a Planos e Comparação deve refletir somente o estado que puder ser legitimamente recuperado.

`TRN-405` não prova persistência técnica por si só.

Este Master não promove a maturidade de `TRN-405`.

## 26. Retorno a PER-301

Ao retornar, `PER-301` deve receber contexto suficiente para representar o plano corrente sem depender de afirmação visual anterior.

O retorno não deve:

- repetir cobrança;
- repetir mutação;
- converter falha em sucesso;
- ocultar pendência;
- selecionar novo plano automaticamente.

## 27. Estados internos

Sem criar novos IDs, Design pode representar:

- carregando resultado;
- resultado confirmado;
- resultado parcial;
- processamento pendente;
- falha recuperável;
- falha sem causa específica conhecida;
- correção disponível;
- nova tentativa permitida;
- tentativa já em andamento;
- estado indeterminado;
- retorno disponível.

Estados internos não criam superfícies ou transições canônicas.

## 28. Privacidade e minimização

Somente dados necessários à compreensão e recuperação do resultado devem ser exibidos.

A superfície deve evitar exposição indevida de:

- dados completos de pagamento;
- identificadores sensíveis;
- dados de terceiros;
- detalhes antifraude;
- informação interna sem utilidade para a Pessoa.

## 29. Linguagem

A linguagem deve distinguir:

- solicitado de concluído;
- pendente de aprovado;
- aprovado de liquidado, quando relevante;
- cobrança de entitlement;
- cancelamento solicitado de efetivado;
- plano pretendido de plano vigente;
- falha conhecida de erro genérico;
- recuperação disponível de recuperação concluída.

## 30. Acessibilidade

Resultado, falha, pendência, consequência, recuperação e retorno devem ser compreensíveis sem depender exclusivamente de cor, ícone, posição, animação ou som.

Mensagens de erro devem indicar ação possível quando houver ação legítima.

## 31. Conteúdo sintético

Prototipação pode usar conteúdo sintético identificado, mas não pode inventar como autoridade:

- pagamento aprovado;
- valor cobrado;
- recibo;
- identificador fiscal;
- data de liquidação;
- entitlement;
- cancelamento efetivado;
- downgrade efetivado;
- proration;
- estorno;
- reembolso;
- período de tratamento.

## 32. Liberdade criativa de Design

Não existe baseline visual canônica imposta por este Master.

Design mantém liberdade sobre composição, componentes, hierarquia, responsividade, motion e microinterações, preservando:

- clareza do resultado;
- distinção entre confirmado e pendente;
- recuperação legítima;
- retorno;
- acessibilidade;
- ausência de efeito inventado;
- autoridades correntes de marca.

## 33. Limites para IA

IA não pode:

- declarar sucesso sem fonte;
- declarar falha financeira específica sem fonte;
- inventar status de pagamento;
- inventar entitlement;
- inventar cancelamento/downgrade efetivado;
- inventar proration/estorno/reembolso;
- inventar período de tratamento;
- criar novos IDs;
- promover `TRN-402/404/405`;
- impor baseline visual;
- liberar Product Engineering.

## 34. Critérios de aceite funcional

O consumo de `PER-304` é aceitável quando:

1. a Pessoa titular é protegida por gate adequado;
2. a operação de origem é compreensível;
3. resultado confirmado exige evidência suficiente;
4. intenção não é tratada como processamento;
5. processamento não é tratado automaticamente como sucesso;
6. cobrança não é tratada automaticamente como entitlement;
7. solicitação de cancelamento não é tratada automaticamente como cancelamento efetivado;
8. estado parcial permanece parcial;
9. pendência permanece explícita;
10. falha é comunicada sem causa inventada;
11. estado anterior é preservado quando não há alteração confirmada;
12. correção de pagamento é oferecida somente quando legítima;
13. nova tentativa não induz duplicidade;
14. idempotência é preservada;
15. falha de pagamento afeta primeiro capacidades pagas conforme política;
16. comunicação precede redução decorrente de falha;
17. dados e direitos são preservados;
18. retorno ao gratuito ocorre somente quando aplicável e confirmado;
19. compromissos transacionais assumidos são protegidos;
20. falha não causa exposição pública;
21. falha não causa perda de dados próprios;
22. falha não interrompe segurança;
23. período de tratamento não é inventado;
24. entitlement não é inventado;
25. downgrade efetivado não é inventado;
26. cancelamento efetivado não é inventado;
27. renovação interrompida não é inventada;
28. proration não é inventada;
29. estorno/reembolso não são inventados;
30. TRN-402 permanece localmente validada;
31. TRN-404 permanece localmente validada;
32. TRN-405 permanece localmente validada;
33. persistência técnica não é presumida;
34. retorno a PER-301 não repete mutação;
35. autonomia é preservada;
36. privacidade e minimização são preservadas;
37. acessibilidade é preservada;
38. Design mantém liberdade criativa;
39. nenhum novo ID é criado;
40. Product Engineering permanece não liberado.

## 35. Lacunas abertas

Permanecem fora deste Master:

- gateway real;
- autorização/captura/liquidação;
- antifraude;
- fiscal;
- proration;
- crédito entre ciclos;
- estorno;
- reembolso monetário;
- período de tratamento;
- recuperação de inadimplência;
- implementação de entitlement;
- persistência técnica;
- regras técnicas de renovação;
- implementação ponta a ponta;
- validação integral de `TRN-402/404/405`;
- teste em produção.

## 36. Estado

```text
PER-304
→ DOCUMENTED IN GOVERNED SCOPE

MASTER
→ GKR-UX-PER304-MASTER-001 v0.1.0
→ CURRENT CANDIDATE

TRN-402
→ LOCALLY VALIDATED / UNCHANGED

TRN-404
→ LOCALLY VALIDATED / UNCHANGED

TRN-405
→ LOCALLY VALIDATED / UNCHANGED

FINANCIAL PROCESSING / ENTITLEMENT / TECHNICAL PERSISTENCE
→ NOT PROVEN

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Com este Master incorporado, a coleção documental planejada de superfícies da Jornada da Pessoa alcança `26 / 26`. Esse fechamento não equivale à liberação de implementação nem elimina as lacunas técnicas e transacionais explicitamente registradas.
