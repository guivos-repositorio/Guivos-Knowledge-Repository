---
id: UXA-099
title: Validação Funcional e Reformulação dos Dez Estados Residuais do Opportunity Boost
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-055
depends_on:
  - UXA-038
  - UXA-039
  - UXA-043
  - UXA-045
  - UXA-050
  - UXA-052
  - UXA-054
  - UXA-055
  - GEM-007-A1
  - GEM-010-A2
related:
  - GPA-007
  - M7.86
normative: false
---

# Validação Funcional e Reformulação dos Dez Estados Residuais do Opportunity Boost

## 1. Finalidade

Validar funcionalmente os dez estados móveis materializados pela UXA-055 e fechar a pendência residual do Opportunity Boost sem ampliar o escopo para algoritmo, cobrança, política jurídica final, protótipo, teste com pessoas ou Engenharia de Produto.

A pergunta de validação é:

> **Os dez estados distinguem erro, zero e baixa oferta, preservam a autoridade do último estado confirmado sem manter entrega materialmente insegura, protegem o catálogo orgânico, permitem controles claros e reversíveis e separam denúncia, contestação e preferência sem expor a pessoa ao anunciante?**

## 2. Resultado

O conjunto é considerado **funcionalmente válido após reformulação controlada de dois wireframes e consolidação transversal de idempotência**.

Dos dez SVGs examinados:

- oito são aprovados sem alteração visual;
- dois exigem reformulação mínima;
- nenhum novo SVG, ID de superfície ou ID de transição é criado.

As reformulações incidem somente sobre:

1. `uxa-055-advertiser-update-failure-mobile.svg`;
2. `uxa-055-review-reverse-preferences-mobile.svg`.

## 3. Escopo examinado

| Estado residual | Artefato | Veredito |
|---|---|---|
| erro técnico patrocinado | `uxa-055-sponsored-technical-error-mobile.svg` | válido sem reformulação |
| falha de atualização do anunciante | `uxa-055-advertiser-update-failure-mobile.svg` | reformulado |
| inventário patrocinado indisponível | `uxa-055-sponsored-inventory-unavailable-mobile.svg` | válido sem reformulação |
| baixa oferta orgânica | `uxa-055-low-organic-supply-mobile.svg` | válido sem reformulação |
| mostrar menos deste tipo | `uxa-055-show-less-type-mobile.svg` | válido sem reformulação |
| desativar oportunidades patrocinadas | `uxa-055-disable-sponsored-opportunities-mobile.svg` | válido sem reformulação |
| ocultar campanha específica | `uxa-055-hide-campaign-mobile.svg` | válido sem reformulação |
| revisar e desfazer preferências | `uxa-055-review-reverse-preferences-mobile.svg` | reformulado |
| denunciar conteúdo ou informação | `uxa-055-report-content-mobile.svg` | válido sem reformulação |
| contestar uso indevido de dados | `uxa-055-contest-data-use-mobile.svg` | válido sem reformulação |

## 4. Lacunas identificadas

### 4.1 Alteração material não confirmada mantinha entrega ativa por inércia

O wireframe de falha de atualização apresentava simultaneamente:

- último estado confirmado `ATIVA`;
- capacidade oficial de 40 vagas;
- capacidade candidata de 25 vagas;
- falha ao confirmar a alteração;
- declaração de que nenhuma pausa seria presumida.

A capacidade é informação material. Uma tentativa explícita de reduzi-la cria incerteza suficiente para impedir nova entrega baseada na informação anterior até que a situação seja revisada. Manter a entrega ativa por inércia entraria em tensão com UXA-038, UXA-039, UXA-050 e UXA-054, que impedem entrega com informação material potencialmente desatualizada.

### 4.2 Histórico de preferências incompleto em data e superfície

O wireframe de revisão apresentava data e superfície para a campanha oculta, mas não registrava o mesmo contexto mínimo para todas as escolhas exibidas.

A própria UXA-055 exige que a revisão permita compreender data, superfície e escopo. Sem esse contexto, a pessoa poderia não distinguir quando e onde uma preferência geral ou uma desativação foi aplicada.

### 4.3 Repetição técnica precisava de contrato transversal explícito

Os artefatos já exigiam tentativa consciente e preservação do último estado confirmado, mas ainda não consolidavam a regra de que repetição da mesma tentativa não poderá duplicar:

- alteração;
- transição de estado;
- impressão válida;
- evento válido;
- consumo de orçamento;
- preferência da pessoa.

A idempotência é consolidada nesta validação como propriedade funcional, sem definir mecanismo técnico.

## 5. Reformulação aprovada

### 5.1 Falha de atualização do anunciante

Quando a alteração candidata for material e sua confirmação falhar:

1. a última versão confirmada permanece a autoridade histórica e de configuração;
2. a versão candidata não é aplicada;
3. a entrega futura entra em pausa automática de proteção;
4. a pausa registra causa e horário;
5. nenhum novo evento válido de entrega ou gasto futuro é presumido durante a incerteza;
6. eventos válidos anteriores permanecem preservados;
7. o anunciante poderá revisar, descartar ou reenviar conscientemente a alteração;
8. reenvio da mesma alteração não duplica versão, estado, evento ou gasto;
9. retomada dependerá de confirmação válida e nova verificação dos gates aplicáveis.

A pausa protetiva não transforma o rascunho local em estado canônico e não presume que o valor candidato seja verdadeiro. Ela somente impede que uma possível mudança material declarada seja ignorada durante a falha.

### 5.2 Revisão e reversão de preferências

Cada escolha apresentada no histórico deverá mostrar, de forma compatível com seu escopo:

- tipo de controle;
- objeto afetado;
- data de aplicação;
- superfície ou conjunto de superfícies suportadas;
- estado atual;
- possibilidade de revisão e reversão.

As reversões permanecem independentes. Reativar publicidade não restaura campanha expirada, inelegível ou encerrada e não cria personalização retroativa.

### 5.3 Idempotência transversal

A repetição da mesma intenção deverá ser funcionalmente idempotente:

```text
recarregar conteúdo patrocinado
→ não duplica impressão, evento, gasto ou preferência

reenviar a mesma alteração ainda não confirmada
→ não cria duas versões canônicas nem duas transições equivalentes

repetir confirmação já aplicada
→ preserva o mesmo efeito lógico
```

A UXA-099 não define chave técnica, armazenamento, deduplicação, protocolo de rede ou algoritmo de mensuração.

## 6. Validação individual dos dez estados

### 6.1 Erro técnico patrocinado

Confirmado:

- erro técnico é distinguível de zero inventário;
- catálogo orgânico permanece utilizável;
- região, busca e filtros são preservados;
- tentar novamente afeta somente o conteúdo patrocinado;
- continuar sem publicidade é uma saída legítima;
- repetição não autoriza duplicação de impressão, evento ou gasto;
- a pessoa não é identificada ao anunciante.

### 6.2 Falha de atualização do anunciante

Confirmado após reformulação:

- último estado confirmado permanece identificável;
- alteração candidata permanece separada da autoridade canônica;
- mudança material não confirmada não mantém entrega futura por inércia;
- pausa de proteção é distinta de aplicação da candidata;
- tentativa e referência técnica são preservadas;
- revisão precede novo envio;
- reenvio é idempotente;
- suporte não recebe dados de pessoas.

### 6.3 Inventário patrocinado indisponível

Confirmado:

- zero significa contagem apurada;
- zero não é falha técnica;
- critérios não são ampliados automaticamente;
- ordem e catálogo orgânicos permanecem inalterados;
- nova consulta depende de ação explícita da pessoa.

### 6.4 Baixa oferta orgânica

Confirmado:

- pouca oferta orgânica reduz ou elimina publicidade;
- densidade não é compensada;
- critérios, região e filtros permanecem iguais;
- campanha paga não adquire posição orgânica;
- inventário pago disponível não contorna a proteção de densidade.

### 6.5 Mostrar menos deste tipo

Confirmado:

- o tipo publicitário é identificável;
- a preferência é separada de filtros de oportunidades;
- categoria orgânica permanece acessível;
- confirmação começa vazia;
- a escolha é revisável e reversível;
- denúncia e contestação permanecem em fluxos diferentes.

### 6.6 Desativar oportunidades patrocinadas

Confirmado:

- superfícies suportadas são explícitas;
- Tela Hoje e Jornada permanecem fora do inventário;
- busca, filtros e catálogo orgânicos são preservados;
- escolha é reversível;
- confirmação começa vazia;
- ocultação de campanha e denúncia continuam ações distintas.

### 6.7 Ocultar campanha específica

Confirmado:

- somente a campanha identificada é afetada;
- Lista e Mapa preservam consulta, região, filtros e orgânico;
- identidade e motivo da pessoa não são revelados ao anunciante;
- confirmação começa vazia;
- ocultar, reduzir e desativar mantêm escopos diferentes;
- denúncia permanece fluxo de integridade separado.

### 6.8 Revisar e desfazer preferências

Confirmado após reformulação:

- campanha oculta, tipo reduzido e patrocinados desativados aparecem separadamente;
- data, superfície e escopo ficam compreensíveis para cada escolha;
- reversões são independentes;
- reativação não restaura campanha expirada ou inelegível;
- denúncias e contestações não aparecem como preferências.

### 6.9 Denunciar conteúdo ou informação

Confirmado:

- fluxo pertence à integridade da oportunidade;
- motivo não começa selecionado;
- revisão poderá envolver conteúdo, elegibilidade ou segurança;
- identidade da pessoa não é enviada ao anunciante;
- denúncia não altera automaticamente preferência publicitária.

### 6.10 Contestar uso indevido de dados

Confirmado:

- fluxo pertence a privacidade e governança;
- denúncia de conteúdo permanece separada;
- motivo não começa selecionado;
- dados protegidos permanecem explicitamente excluídos;
- contestação e identidade da pessoa não são enviadas ao anunciante;
- explicação `Por que estou vendo isto?` permanece acessível;
- contestação não altera preferência automaticamente.

## 7. Cobertura resultante do Opportunity Boost

Após esta validação, o Opportunity Boost possui:

- **46 wireframes materializados**;
- **46 wireframes funcionalmente validados pelos respectivos pacotes**;
- **0 estados residuais pendentes da UXA-055**;
- 25 artefatos que continuam sob a autoridade transversal histórica da UXA-050, sem ampliação retroativa do escopo daquela validação.

A UXA-099 valida os dez artefatos residuais como um pacote próprio e não reabre os 36 wireframes anteriormente validados.

## 8. Impacto proposto na cobertura global

| Indicador | Resultado após eventual integração |
|---|---:|
| SVGs existentes e referenciados | **109** |
| associações individuais | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **109** |
| pendentes de validação específica | **0** |
| IDs granulares com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| superfícies granulares | **40** |
| transições granulares | **37** |

Nenhum contador de superfície, transição, associação, perfil ou SVG é alterado; somente o estado funcional dos dez SVGs residuais muda.

## 9. Proteções preservadas

- pagamento amplia distribuição identificada, não relevância funcional;
- primeiro resultado orgânico permanece orgânico;
- baixa oferta orgânica reduz publicidade;
- ausência de inventário não amplia critérios;
- erro técnico não é representado como zero;
- mudança material potencial não é ignorada por falha de confirmação;
- preferência negativa prevalece sobre entrega contratada;
- controles da pessoa não reduzem o catálogo orgânico;
- denúncia, contestação e preferência permanecem taxonomias distintas;
- anunciante e financiador não recebem identidade, motivo, preferência ou contestação da pessoa;
- relato protegido, compreensão inicial, Momento Atual, Próximo Passo, mensagens e inferências sensíveis permanecem excluídos de publicidade;
- repetição da mesma intenção não duplica efeito lógico;
- nenhuma campanha, cobrança, algoritmo ou perfil publicitário individual é criado.

## 10. Limites

Esta validação não cria ou aprova:

- política jurídica final de publicidade, denúncia, contestação ou retenção;
- limiar definitivo de agregação e privacidade;
- algoritmo de entrega, leilão, densidade ou frequência;
- antifraude técnico;
- mecanismo técnico de idempotência;
- design visual final;
- acessibilidade técnica;
- protótipo navegável;
- teste com pessoas;
- checkout, faturamento, cobrança ou campanha real;
- implementação de `TRN-304` ou `TRN-306`;
- efeito externo de oportunidades em `TRN-205`;
- Engenharia de Produto.

## 11. Estado funcional

`functionally_valid_after_controlled_reformulation — all ten UXA-055 residual mobile states validated; advertiser material-update failure now enters protective automatic pause, preference history carries complete temporal/surface context, and retries are functionally idempotent`.

## 12. Próximos atos governados

Com a integração futura da UXA-099:

1. `V3 — dez estados residuais UXA-055` poderá ser encerrada;
2. `V4 — efeito externo de oportunidades` passará a ser a próxima prioridade da fila;
3. `TRN-304` e `TRN-306` permanecerão parciais;
4. nenhuma jornada será promovida automaticamente;
5. UXA-100 não será iniciada automaticamente;
6. Engenharia de Produto permanecerá pausada antes de W0-01.
