---
id: GKR-UX-PER303-MASTER-001
title: Jornada da Pessoa — PER-303 — Downgrade e Cancelamento — Documento Mestre de Superfície
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
  - GKR-SURF-PER-303
  - GKR-SURF-PER-304
  - GKR-TRN-403
  - GKR-TRN-404
---

# Jornada da Pessoa — PER-303 — Downgrade e Cancelamento — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de `PER-303 — Downgrade e Cancelamento` para Design, IA opcional, Produto, UX, Privacidade e Engenharia.

`PER-303` existe para que a **Pessoa titular** compreenda e controle conscientemente uma redução ou encerramento de plano, conhecendo consequências materiais antes de qualquer continuidade que possa alterar capacidades ou renovação.

A superfície não executa por inferência downgrade, cancelamento, estorno, proration ou alteração técnica de entitlement.

## 2. Autoridades correntes

A leitura de `PER-303` deve preservar conjuntamente:

- `GKR-JOURNEY-SURFACE-DETAIL-PERSON-001` — contrato detalhado da superfície;
- `GKR-PLANS-PERSON-001` — planos, capacidades e limites;
- `GEM-004-PLAN-TAXONOMY-AUTHORITY-001` — taxonomia vigente;
- `GEM-004-A2` — política comercial de oferta, upgrade, downgrade e cancelamento;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001` — maturidade das transições.

Nenhuma referência visual histórica substitui essas autoridades.

## 3. Papel funcional

A Pessoa titular deve conseguir:

1. reconhecer o plano atual quando confirmado por fonte corrente;
2. distinguir downgrade de cancelamento;
3. compreender o plano futuro ou estado posterior aplicável;
4. compreender capacidades que deixarão de estar disponíveis;
5. compreender a data efetiva quando governada;
6. compreender impactos sobre histórico, relatórios e integrações;
7. identificar exportação disponível;
8. compreender a preservação do baseline gratuito quando aplicável;
9. manter o plano atual sem penalidade artificial;
10. confirmar conscientemente a continuidade;
11. não sofrer efeito substantivo apenas por entrar, revisar ou voltar.

## 4. Titularidade e gate

`GKR-SURF-PER-303` é responsabilidade da **Pessoa titular**.

Autenticação, isoladamente, não autoriza alteração de assinatura de terceiro.

Antes de habilitar continuidade substantiva, a experiência deve possuir autoridade legítima para reconhecer a titularidade aplicável. Se isso não puder ser estabelecido, a continuidade deve permanecer bloqueada sem fabricar autoridade.

## 5. Entrada — TRN-403

`GKR-TRN-403: PER-301 → PER-303`.

Estado: **localmente validada**.

A entrada representa decisão afirmativa de revisar downgrade ou cancelamento.

Entrar em `PER-303`:

- não altera plano;
- não cancela assinatura;
- não interrompe renovação;
- não reduz entitlement;
- não apaga dados;
- não produz estorno;
- não define proration.

Este Master não promove a maturidade de `TRN-403`.

## 6. Contexto mínimo

A superfície pode utilizar somente contexto necessário e autorizado, como:

- plano atual;
- plano futuro pretendido, quando houver;
- capacidades afetadas;
- data efetiva autorizada;
- impactos materiais conhecidos;
- possibilidades de exportação;
- baseline posterior aplicável.

Dados ausentes não devem ser inferidos.

## 7. Downgrade — revisão obrigatória

Antes de um downgrade, a Pessoa deve conseguir compreender:

- capacidades que deixarão de estar disponíveis;
- data efetiva;
- histórico e relatórios afetados;
- integrações que serão desativadas;
- exportação disponível;
- baseline gratuito preservado.

Esses elementos derivam da política comercial corrente e não são opcionais quando materialmente aplicáveis.

Se uma consequência obrigatória necessária não puder ser determinada por autoridade corrente, a experiência não deve fabricar a resposta nem apresentar confirmação enganosa.

## 8. Preservações após downgrade

A política corrente protege, no mínimo:

- acesso aos dados essenciais;
- oportunidades públicas no catálogo, que não devem desaparecer por causa do downgrade;
- novas correspondências segundo a cota vigente do Guivos Free;
- personalização compatível com autorizações vigentes e capacidades gratuitas.

Relatórios pagos podem depender de política futura de retenção para exportação ou modo de leitura. Essa regra não deve ser inventada.

## 9. Cancelamento — requisitos

O cancelamento deve:

- estar disponível na mesma área de contratação;
- não exigir contato humano quando a contratação foi autônoma, salvo obrigação legítima;
- apresentar data efetiva;
- informar o plano ou estado posterior;
- preservar exportação e direitos;
- permitir registro da solicitação;
- não ser artificialmente mais difícil que contratar.

A interrupção efetiva de renovação futura pertence ao efeito confirmado do cancelamento e não deve ser declarada antes de resultado real.

## 10. Retenção opcional

Ofertas de retenção podem existir somente quando houver autoridade comercial própria e quando forem:

- opcionais;
- não bloqueadoras;
- não coercitivas;
- não baseadas em culpa, medo ou ameaça;
- incapazes de ocultar a ação principal de cancelar.

Este Master não cria oferta de retenção, desconto ou benefício.

## 11. Consequências explícitas

A revisão deve distinguir claramente:

- o que muda;
- o que permanece;
- quando a mudança deve produzir efeito, quando a data for conhecida;
- quais capacidades serão perdidas;
- quais dados/direitos permanecem;
- quais exportações estão disponíveis;
- qual plano ou baseline posterior é aplicável.

Consequência desconhecida deve permanecer desconhecida, não simulada.

## 12. Data efetiva

A data efetiva deve ser apresentada quando governada por fonte corrente.

Este Master não autoriza calcular ou inventar:

- encerramento imediato;
- fim do ciclo;
- data proporcional;
- crédito de período restante;
- cobrança residual;
- período de graça.

Se a data efetiva for material para a decisão e não puder ser determinada, a confirmação substantiva deve ser bloqueada até haver autoridade suficiente.

## 13. Proration

Proration, crédito e data de cobrança entre ciclos permanecem pendentes de definição financeira, contábil, fiscal e técnica.

A experiência não deve prometer:

- cobrança proporcional;
- crédito automático;
- devolução proporcional;
- saldo compensatório;
- regra de corte entre ciclos.

## 14. Estorno e reembolso

Este Master não define:

- direito automático a estorno;
- valor de reembolso;
- prazo de reembolso;
- método de devolução;
- crédito futuro;
- compensação financeira.

Qualquer tratamento monetário depende de autoridade própria.

## 15. Exportação

Quando exportação estiver disponível pela autoridade corrente, ela deve permanecer acessível sem ser transformada em obstáculo artificial para downgrade ou cancelamento.

A Pessoa não deve ser obrigada a exportar para poder continuar.

A ausência de exportação específica não autoriza exclusão silenciosa de dados.

## 16. Manter plano

Manter o plano atual é uma decisão válida.

A Pessoa deve conseguir abandonar a revisão sem:

- perder capacidades;
- alterar recorrência;
- registrar cancelamento;
- gerar cobrança;
- sofrer pressão artificial;
- justificar sua decisão.

## 17. Confirmação consciente

A continuidade substantiva exige ação afirmativa, inequívoca e contextual da Pessoa titular.

Não constituem confirmação:

- entrar na superfície;
- rolar;
- visualizar consequências;
- abrir exportação;
- retornar;
- inatividade;
- seleção prévia em `PER-301`;
- oferta de retenção recusada.

## 18. Saída — TRN-404

`GKR-TRN-404: PER-303 → PER-304`.

Estado: **localmente validada**.

A transição representa continuidade após revisão e confirmação consciente.

Sua lacuna principal permanece: **execução do entitlement**.

Portanto, `TRN-404` não comprova:

- downgrade efetivado;
- cancelamento efetivado;
- renovação interrompida;
- entitlement alterado;
- proration aplicada;
- estorno realizado;
- persistência técnica concluída.

O resultado pertence a `PER-304`.

Este Master não promove a maturidade de `TRN-404`.

## 19. Estados internos

Sem novos IDs, Design pode representar estados como:

- carregamento;
- revisão disponível;
- titularidade confirmada;
- titularidade insuficiente;
- downgrade em revisão;
- cancelamento em revisão;
- consequências completas;
- consequência material pendente;
- pronta para confirmação;
- continuidade em andamento;
- retorno voluntário;
- indisponibilidade;
- erro recuperável.

Estado interno não cria nova superfície nem nova transição.

## 20. Dados incompletos

Quando faltar informação material necessária:

```text
NÃO INFERIR
→ NÃO FABRICAR
→ NÃO CONFIRMAR SILENCIOSAMENTE
→ PRESERVAR O PLANO ATUAL
→ PRESERVAR RETORNO
```

A superfície deve favorecer segurança comercial e autonomia sobre falsa completude.

## 21. Idempotência

Reabrir a revisão ou repetir navegação não deve duplicar solicitação, cancelamento ou downgrade.

Uma confirmação de interface não deve ser usada como prova de execução repetível ou concluída.

## 22. Dados e direitos

Downgrade ou cancelamento não autorizam:

- apagar automaticamente histórico;
- retirar direitos de acesso já preservados por política;
- excluir oportunidades públicas do catálogo;
- revogar consentimentos não relacionados;
- ampliar coleta de dados.

Retenção, exclusão e portabilidade seguem autoridades próprias.

## 23. Autonomia e ausência de pressão

A superfície não deve usar:

- culpa;
- medo;
- ameaça;
- urgência inventada;
- perda fictícia;
- obstáculos artificiais;
- caminhos ocultos;
- ação principal disfarçada;
- confirmação pré-selecionada;
- assimetria deliberada entre contratar e cancelar.

## 24. Privacidade e minimização

Somente dados necessários à gestão da assinatura e à compreensão das consequências podem ser utilizados.

Inferências sensíveis não devem ser usadas para impedir cancelamento, personalizar pressão de retenção ou manipular permanência.

## 25. Linguagem

A linguagem deve distinguir:

- **revisar downgrade** de downgrade efetivado;
- **revisar cancelamento** de cancelamento efetivado;
- **data efetiva prevista/autorizada** de execução confirmada;
- **consequência comercial** de processamento técnico;
- **solicitação** de resultado;
- **manter plano** de falha.

## 26. Acessibilidade

Plano atual/futuro, capacidades afetadas, data efetiva, exportação, consequências, manter plano e ação afirmativa devem ser compreensíveis sem depender exclusivamente de cor, posição, ícone, animação ou som.

A ação de cancelar não pode ser semanticamente escondida de tecnologias assistivas.

## 27. Conteúdo sintético

Prototipação pode usar conteúdo sintético claramente identificado, mas não pode inventar como autoridade:

- plano real da Pessoa;
- data efetiva;
- estorno;
- proration;
- reembolso;
- status de cancelamento;
- status de downgrade;
- entitlement;
- renovação interrompida.

## 28. Liberdade criativa de Design

Não existe baseline visual canônica imposta por este Master.

A designer mantém liberdade sobre composição, hierarquia, componentes, responsividade, motion e microinterações, preservando:

- titularidade;
- consequências explícitas;
- reversibilidade;
- ação afirmativa;
- cancelamento acessível;
- acessibilidade;
- ausência de efeito inventado;
- autoridades correntes de marca.

## 29. Limites para IA

IA não pode:

- inventar data efetiva;
- inventar consequência;
- inventar proration;
- inventar estorno/reembolso;
- executar ou afirmar cancelamento;
- executar ou afirmar downgrade;
- afirmar entitlement alterado;
- criar oferta de retenção sem autoridade;
- promover `TRN-403/404`;
- criar novos IDs;
- impor baseline visual;
- iniciar Product Engineering.

## 30. Critérios de aceite funcional

O consumo de `PER-303` é aceitável quando:

1. a Pessoa titular é a autoridade para continuidade;
2. autenticação isolada não substitui titularidade;
3. entrada não altera plano;
4. downgrade e cancelamento são distinguíveis;
5. plano atual é afirmado somente quando conhecido;
6. plano futuro/estado posterior é apresentado quando aplicável;
7. capacidades perdidas são apresentadas;
8. data efetiva é apresentada quando governada;
9. impactos em histórico/relatórios são apresentados;
10. integrações afetadas são apresentadas;
11. exportação disponível é apresentada;
12. baseline gratuito preservado é apresentado quando aplicável;
13. dados essenciais são preservados conforme política;
14. oportunidades públicas não são removidas por downgrade;
15. cancelamento permanece acessível;
16. contratação autônoma não exige contato humano para cancelar, salvo obrigação legítima;
17. retenção não bloqueia cancelamento;
18. manter plano é decisão válida;
19. confirmação é afirmativa;
20. consequência material desconhecida não é inventada;
21. proration não é inventada;
22. estorno/reembolso não são inventados;
23. TRN-403 permanece localmente validada;
24. TRN-404 permanece localmente validada;
25. resultado pertence a PER-304;
26. entitlement não é alterado por inferência;
27. repetição não duplica efeito;
28. autonomia é preservada;
29. privacidade e minimização são preservadas;
30. acessibilidade é preservada;
31. Design mantém liberdade criativa;
32. nenhum novo ID é criado;
33. Product Engineering permanece não liberado.

## 31. Lacunas abertas

Permanecem fora deste Master:

- proration;
- crédito entre ciclos;
- data de cobrança entre ciclos;
- estorno;
- reembolso monetário;
- período de graça;
- execução real de entitlement;
- persistência técnica;
- confirmação técnica de interrupção de renovação;
- política final de retenção/exportação de relatórios pagos;
- implementação ponta a ponta;
- validação integral de `TRN-403/404`;
- resultado e recuperação de `PER-304`.

## 32. Estado

```text
PER-303
→ DOCUMENTED IN GOVERNED SCOPE

MASTER
→ GKR-UX-PER303-MASTER-001 v0.1.0
→ CURRENT CANDIDATE

TRN-403
→ LOCALLY VALIDATED / UNCHANGED

TRN-404
→ LOCALLY VALIDATED / UNCHANGED

PRORATION / REFUND / ENTITLEMENT EXECUTION
→ NOT PROVEN

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Próxima superfície da coleção após a incorporação deste Master: `PER-304 — Resultado e Recuperação de Plano/Cobrança`.
