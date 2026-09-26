---
id: GKR-UX-PER301-MASTER-001
title: Jornada da Pessoa — PER-301 — Planos e Comparação — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-26
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-PLANS-PERSON-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-SURF-PER-009
  - GKR-SURF-PER-301
  - GKR-SURF-PER-302
  - GKR-SURF-PER-303
  - GKR-TRN-401
  - GKR-TRN-403
  - GKR-TRN-406
  - GKR-TRN-407
---

# Jornada da Pessoa — PER-301 — Planos e Comparação — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de `PER-301 — Planos e Comparação` para Design, IA opcional, Produto, UX, Privacidade e Engenharia.

`PER-301` permite à Pessoa autenticada **compreender o plano atual, comparar Free, Plus e Pro, entender diferenças relevantes e decidir conscientemente se permanece como está ou inicia uma revisão de mudança**.

A superfície é de compreensão e decisão. Não é checkout.

## 2. Autoridades correntes

A leitura de `PER-301` deve preservar conjuntamente:

- `GKR-PLANS-PERSON-001` — planos, preços, capacidades e limites vigentes;
- `GEM-004-PLAN-TAXONOMY-AUTHORITY-001` — taxonomia de planos;
- `GKR-JOURNEY-TRANSITION-REGISTRY-001` — maturidade das transições;
- `GKR-SURF-PER-301` — responsabilidade especializada da superfície.

Nenhuma referência visual histórica substitui essas autoridades.

## 3. Taxonomia vigente

```text
PESSOA
├── FREE
├── PLUS
└── PRO
```

Essa taxonomia não deve ser misturada com planos de Coletivo, Organização ou Guivos Business.

## 4. Preços de referência vigentes

| Plano | Mensal | Anual |
|---|---:|---:|
| **Free** | R$ 0,00 | R$ 0,00 |
| **Plus** | R$ 24,90 | R$ 249,00 |
| **Pro** | R$ 49,90 | R$ 499,00 |

Os valores integram a baseline comercial de referência vigente. Oferta pública, cobrança e condições finais permanecem sujeitas aos gates comerciais, jurídicos, fiscais e operacionais aplicáveis.

Design e IA não podem inventar promoção, desconto, parcelamento, economia percentual, trial, taxa, imposto ou preço alternativo.

## 5. Papel funcional

A Pessoa deve conseguir:

1. reconhecer seu plano atual quando essa informação estiver disponível por autoridade corrente;
2. compreender o que Free, Plus e Pro representam;
3. comparar capacidades e limites;
4. perceber o delta relevante entre plano atual e alternativa;
5. permanecer no plano atual sem penalidade de navegação;
6. iniciar conscientemente uma revisão de contratação quando aplicável;
7. iniciar conscientemente revisão de downgrade/cancelamento quando aplicável;
8. retornar à Conta sem alterar o plano.

## 6. Free

**Preço:** R$ 0,00/mês · R$ 0,00/ano.

Finalidade: participação real, compreensão inicial, descoberta pública e acompanhamento essencial sem pagamento.

Inclui, conforme autoridade comercial corrente:

- Página Inicial pública e exploração geral;
- início protegido e compreensão inicial revisável;
- jornada essencial;
- acesso ao catálogo público no Explorar e Mapa;
- 2 correspondências personalizadas completas por semana;
- histórico essencial;
- controles de dados, permissões, correção, exportação, exclusão e saída;
- participação em atividades e oportunidades gratuitas ou pagas conforme condições do publicador.

Limites principais:

- cota semanal não acumulativa;
- cota consumida quando a Pessoa abre a correspondência completa;
- esgotamento não bloqueia Explorar, Mapa, busca manual ou informações públicas essenciais.

## 7. Plus

**Preço:** R$ 24,90/mês · R$ 249,00/ano.

Finalidade: ampliar personalização, conveniência, histórico, alertas e organização da jornada individual.

Acrescenta ao Free:

- correspondências personalizadas completas sem cota semanal fixa, sujeitas a uso justo;
- explicação completa da relação entre oportunidade e contexto autorizado;
- filtros avançados;
- alertas personalizados;
- histórico ampliado;
- planos salvos, lembretes e acompanhamento ampliado;
- exportação padrão;
- capacidade ampliada de processamento e Intelligence;
- integrações limitadas quando autorizadas;
- suporte ampliado.

Limites principais:

- uso individual e intransferível;
- não inclui serviço profissional humano;
- não inclui uso comercial nem administração de Organização ou Coletivo.

## 8. Pro

**Preço:** R$ 49,90/mês · R$ 499,00/ano.

Finalidade: maior profundidade analítica, integração autorizada, relatórios e acompanhamento avançado.

Acrescenta ao Plus:

- análises aprofundadas e comparativas;
- organização autorizada entre diferentes áreas da jornada;
- maior capacidade de processamento e Intelligence;
- relatórios pessoais ampliados;
- exportações avançadas;
- integrações autorizadas ampliadas;
- suporte prioritário;
- acesso antecipado a capacidades aprovadas para teste, quando aplicável e informado.

Limites principais:

- permanece plano individual;
- não substitui diagnóstico ou aconselhamento profissional;
- não garante oportunidade, resultado ou evolução.

## 9. Comparação funcional

| Tema | Free | Plus | Pro |
|---|---|---|---|
| Correspondências personalizadas | 2/semana | ampliadas, uso justo | ampliadas + análise aprofundada |
| Histórico | essencial | ampliado | ampliado + relatórios |
| Filtros | básicos | avançados | avançados e combinados |
| Alertas | gerais | personalizados | personalizados e prioritários |
| Exportação | essencial | padrão | avançada |
| Integrações | não incluídas | limitadas | ampliadas |
| Intelligence | essencial | ampliada | avançada |
| Suporte | padrão | ampliado | prioritário |

A comparação deve ser legível como diferença de capacidades, não como julgamento de valor sobre a Pessoa.

## 10. Plano atual

Quando o plano atual for conhecido por fonte corrente, a superfície pode identificá-lo.

A identificação:

- não altera entitlement;
- não renova assinatura;
- não confirma pagamento;
- não transforma o plano atual em recomendação;
- não deve ocultar alternativas gratuitas;
- não autoriza inferir status financeiro não disponível.

Se o estado corrente não puder ser confirmado, a interface deve evitar apresentar um plano como ativo por inferência.

## 11. Delta entre planos

A comparação pode enfatizar o que muda entre o plano atual e uma alternativa, desde que preserve a autoridade comercial.

```text
DELTA
→ CAPACIDADES / LIMITES / PREÇO DE REFERÊNCIA

DELTA
≠ PRESSÃO
≠ SCORE DE ADEQUAÇÃO
≠ GARANTIA DE RESULTADO
≠ RECOMENDAÇÃO AUTOMÁTICA
```

## 12. Permanecer como está

Não escolher mudança é uma decisão válida.

A superfície deve permitir compreender e sair sem:

- criar contratação;
- iniciar cobrança;
- marcar intenção comercial como aceite;
- reduzir acesso vigente;
- gerar urgência artificial.

## 13. TRN-401 — Planos → Revisão de Contratação

`GKR-TRN-401: PER-301 → PER-302`.

Estado: **localmente validada**.

A transição deve ocorrer após ação afirmativa sobre uma mudança que exige revisão de contratação.

Ela não significa que a contratação foi concluída.

`PER-302` permanece responsável pela revisão consciente da contratação.

## 14. TRN-403 — Planos → Downgrade / Cancelamento

`GKR-TRN-403: PER-301 → PER-303`.

Estado: **localmente validada**.

A transição abre revisão especializada de downgrade/cancelamento.

Ela não:

- executa cancelamento;
- executa downgrade;
- define data efetiva;
- calcula proration;
- produz estorno;
- altera entitlement.

Essas consequências não devem ser antecipadas sem autoridade.

## 15. TRN-406 — Conta → Planos

`GKR-TRN-406: PER-009 → PER-301`.

Estado: **contratada**.

Abrir Planos voluntariamente continua sendo navegação administrativa. Não constitui seleção, contratação, cobrança ou alteração de entitlement.

Este Master não promove a maturidade de TRN-406.

## 16. TRN-407 — Planos → Conta

`GKR-TRN-407: PER-301 → PER-009`.

Estado: **contratada**.

Retornar à Conta é neutro quanto a efeitos comerciais.

Retornar não equivale a cancelar, contratar, confirmar, alterar plano ou desfazer efeito já confirmado em outra responsabilidade.

Este Master não promove a maturidade de TRN-407.

## 17. Autenticação

`PER-301` opera em contexto autenticado quando trata estado atual e decisão de mudança da Pessoa.

Autenticação não significa autorização financeira automática.

Este Master não define login, sessão, MFA, credenciais ou recuperação de conta.

## 18. Estados internos de experiência

Sem criar novos IDs, Design pode representar estados como:

- carregamento;
- comparação disponível;
- plano atual conhecido;
- plano atual não confirmável;
- seleção temporária para comparação;
- continuidade para revisão;
- retorno de revisão;
- indisponibilidade temporária;
- erro recuperável.

Estado visual interno não é nova superfície nem nova transição.

## 19. Seleção temporária

Destacar ou selecionar uma alternativa para compreender diferenças não deve ser tratado como contratação.

Ação comercial substantiva exige continuidade consciente para a responsabilidade apropriada.

## 20. Cobrança e implementação financeira

Não estão comprovados por este Master:

- gateway;
- autorização de cartão;
- Pix ou boleto;
- processamento financeiro real;
- antifraude;
- fiscal;
- nota fiscal;
- proration;
- estorno;
- persistência técnica de entitlement;
- renovação automática implementada.

Esses itens não podem ser inferidos a partir da existência de preços.

## 21. Reversibilidade e idempotência

Reabrir `PER-301`, alternar comparações ou retornar à Conta não deve duplicar efeito comercial.

A Pessoa pode:

- comparar;
- mudar o foco da comparação;
- não prosseguir;
- retornar à Conta;
- reabrir Planos.

Nenhum desses atos isolados equivale a contratação ou cancelamento.

## 22. Autonomia e ausência de pressão

A superfície não deve usar:

- contagem regressiva inventada;
- escassez artificial;
- vergonha por permanecer no Free;
- bloqueio indevido de alternativas gratuitas;
- ranking de planos como medida de valor pessoal;
- claims de sucesso garantido;
- upgrade automático;
- opção pré-confirmada que produza efeito financeiro.

## 23. Privacidade e minimização

A comparação deve usar somente informações necessárias para:

- reconhecer contexto autenticado;
- apresentar plano atual quando legitimamente conhecido;
- comparar capacidades;
- encaminhar uma decisão consciente.

Não deve expor histórico financeiro detalhado, credenciais ou dados sensíveis sem finalidade e autoridade próprias.

## 24. Linguagem

A linguagem deve distinguir:

- **comparar** de contratar;
- **escolher para revisar** de confirmar;
- **preço de referência** de cobrança executada;
- **plano atual** de plano recomendado;
- **capacidade** de garantia de resultado.

## 25. Acessibilidade

Comparação, plano atual, preço, diferenças e ações devem ser compreensíveis sem depender exclusivamente de cor, posição, ícone, animação ou som.

Tabelas e agrupamentos devem preservar leitura por tecnologias assistivas e não depender apenas de disposição visual lado a lado.

## 26. Conteúdo sintético

Prototipação pode usar dados sintéticos claramente fictícios, mas não pode inventar como autoridade:

- preço;
- desconto;
- promoção;
- plano atual;
- cobrança;
- renovação;
- entitlement;
- método de pagamento;
- status financeiro.

Os preços deste Master são autoridades documentais vigentes, não dados sintéticos.

## 27. Liberdade criativa de Design

Não existe baseline visual canônica imposta por este Master.

A designer mantém liberdade sobre composição, hierarquia visual, componentes, densidade, cards, tabela, responsividade, motion, microinterações e apresentação comparativa, preservando:

- taxonomia;
- preços vigentes;
- capacidades e limites;
- autonomia;
- acessibilidade;
- distinção entre comparação e efeito comercial;
- autoridades correntes de marca.

## 28. Limites para IA

IA não pode:

- inventar quarto plano;
- renomear Free, Plus ou Pro;
- alterar preços;
- inventar desconto/promoção/trial;
- declarar um plano “melhor” para a Pessoa sem autoridade;
- criar pressão de upgrade;
- iniciar cobrança;
- simular entitlement como confirmado;
- promover transições;
- criar novos IDs;
- impor baseline visual;
- iniciar Product Engineering.

## 29. Critérios de aceite funcional

O consumo de `PER-301` é aceitável quando:

1. Free, Plus e Pro são preservados;
2. preços correntes são preservados;
3. capacidades correntes são preservadas;
4. limites correntes são preservados;
5. plano atual só é afirmado quando conhecido;
6. comparação não é contratação;
7. seleção temporária não é confirmação;
8. permanecer no plano atual é válido;
9. Free permanece alternativa real;
10. não há pressão artificial de upgrade;
11. TRN-401 permanece localmente validada;
12. TRN-403 permanece localmente validada;
13. TRN-406 permanece contratada;
14. TRN-407 permanece contratada;
15. PER-302 permanece revisão de contratação;
16. PER-303 permanece revisão de downgrade/cancelamento;
17. gateway não é inventado;
18. fiscal não é inventado;
19. proration não é inventada;
20. entitlement técnico não é inventado;
21. navegação repetida não duplica efeito;
22. privacidade e minimização são preservadas;
23. acessibilidade é preservada;
24. Design mantém liberdade criativa;
25. nenhum novo ID é criado;
26. Product Engineering permanece não liberado.

## 30. Lacunas abertas

Permanecem fora deste Master:

- execução financeira real;
- gateway;
- meios de pagamento;
- fiscal;
- proration;
- estorno;
- persistência técnica de entitlement;
- política operacional de renovação;
- regras técnicas de cobrança;
- implementação ponta a ponta;
- validação integral de TRN-401/403;
- promoção de TRN-406/407;
- revisão de contratação de PER-302;
- downgrade/cancelamento de PER-303;
- resultado/recuperação de PER-304.

## 31. Estado

```text
PER-301
→ DOCUMENTED IN GOVERNED SCOPE

MASTER
→ GKR-UX-PER301-MASTER-001 v0.1.0
→ CURRENT CANDIDATE

PLANS
→ FREE / PLUS / PRO

TRN-401 / TRN-403
→ LOCALLY VALIDATED / UNCHANGED

TRN-406 / TRN-407
→ CONTRACTED / UNCHANGED

FINANCIAL EXECUTION
→ NOT PROVEN

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED
```

Próxima superfície da coleção após a incorporação deste Master: `PER-302 — Revisão de Contratação`.
