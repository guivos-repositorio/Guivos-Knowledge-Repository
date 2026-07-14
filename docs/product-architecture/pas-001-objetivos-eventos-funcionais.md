---
id: PAS-001-OBJ-EVENT-001
title: Contratos dos Eventos Funcionais da Capacidade de Objetivos
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-OBJ-FOUNDATION-001
  - PAS-001-OBJ-LIFECYCLE-001
  - PAS-001-OBJ-PROGRESS-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-CV-EVENT-001
  - PAS-001-CV-INTEGRATION-001
  - PAS-001-CV-CONTRACT-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-OBJ-EVENT-001 — Contratos dos Eventos Funcionais da Capacidade de Objetivos

## 1. Autoridade e vínculo

Este documento é a **quinta extensão normativa da Capacidade 03 — Objetivos** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 366 a 403 do `PAS-001-OBJ-FOUNDATION-001 1.0.0`, das seções 404 a 469 do `PAS-001-OBJ-LIFECYCLE-001 1.0.0`, das seções 470 a 531 do `PAS-001-OBJ-PROGRESS-001 1.0.0`, das seções 532 a 612 do `PAS-001-OBJ-VIEW-001 1.0.0` e da especificação-base `PAS-001 0.5.0`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade normativa desta extensão.

# 613. Contratos dos eventos funcionais da Capacidade de Objetivos

Os eventos funcionais deverão registrar fatos reconhecidos durante o ciclo de vida dos objetivos.

Eles deverão permitir que a Guivos:

- preserve o histórico;
- explique alterações;
- sincronize capacidades consumidoras;
- recomponha recortes;
- evite efeitos duplicados;
- trate correções e contestações;
- reavalie decisões dependentes;
- opere com falha segura.

> Um evento funcional registra algo que foi reconhecido como ocorrido. Ele não deverá representar apenas uma solicitação, tentativa, hipótese ou intenção futura.

# 614. Escopo dos eventos

Os contratos abrangerão eventos relacionados a:

1. manifestação de direção;
2. criação e proposição;
3. confirmação e ativação;
4. formulação e estrutura;
5. prioridade;
6. relações e conflitos;
7. revisão e envelhecimento;
8. pausa e bloqueio;
9. critérios de sucesso;
10. linhas de base;
11. evidências;
12. progresso;
13. marcos;
14. conclusão;
15. retirada e arquivamento;
16. Eventos de Vida;
17. permissões e compartilhamentos;
18. propagação;
19. correções;
20. falhas funcionais.

# 615. Comando, proposta e evento

## 615.1 Comando

Representa uma solicitação de ação.

Exemplos:

- criar objetivo;
- alterar prioridade;
- registrar evidência;
- concluir objetivo;
- revogar compartilhamento.

O comando poderá ser:

- aceito;
- rejeitado;
- adiado;
- encaminhado para confirmação;
- convertido em proposta;
- impedido por regra funcional.

## 615.2 Proposta

Representa uma possível alteração que ainda depende de avaliação ou confirmação.

Exemplos:

- objetivo sugerido pela Guivos;
- prioridade sugerida;
- conclusão sugerida;
- relação sugerida entre objetivos;
- progresso inferido.

## 615.3 Evento funcional

Representa um fato reconhecido.

Exemplos:

- `ObjetivoConfirmado`;
- `ObjetivoAtivado`;
- `PrioridadeAlterada`;
- `EvidenciaDeObjetivoRegistrada`;
- `ObjetivoConcluido`.

```text
Comando:
Concluir objetivo

→ avaliação funcional

Proposta:
Conclusão sugerida

→ confirmação do participante

Evento:
ObjetivoConcluido
```

Comando, proposta e evento não deverão ser tratados como equivalentes.

# 616. Princípios dos eventos funcionais

## 616.1 Imutabilidade histórica

O evento reconhecido não deverá ser alterado para aparentar que outro fato ocorreu.

Correções deverão produzir novos eventos.

## 616.2 Temporalidade explícita

Todo evento deverá distinguir, quando relevante:

- momento do fato;
- momento em que a Guivos tomou conhecimento;
- momento em que o evento foi reconhecido;
- momento em que seus efeitos foram aplicados.

## 616.3 Proveniência

Todo evento deverá identificar:

- origem;
- ator;
- canal;
- capacidade produtora;
- autoridade funcional.

## 616.4 Autoria e controle

Eventos que atribuam direção, prioridade, progresso pessoal ou conclusão ao participante deverão preservar sua autoria ou confirmação.

## 616.5 Minimização

O evento deverá conter apenas informações necessárias para registrar o fato e produzir seus efeitos legítimos.

## 616.6 Explicabilidade

Alterações materiais deverão poder ser explicadas a partir dos eventos correspondentes.

## 616.7 Idempotência

O reprocessamento do mesmo evento não deverá produzir efeitos funcionais duplicados.

## 616.8 Propagação controlada

Cada capacidade consumidora deverá receber apenas o recorte necessário.

## 616.9 Separação entre fato e interpretação

Eventos declarativos, observacionais, inferenciais e institucionais deverão permanecer diferenciados.

## 616.10 Ausência de avaliação humana

Eventos não deverão classificar o valor, caráter, ambição ou potencial do participante.

# 617. Estrutura comum do evento

Todo evento funcional deverá possuir, quando aplicável:

| Campo | Finalidade |
|---|---|
| Identificador do evento | Distinguir o fato registrado |
| Tipo do evento | Definir seu significado funcional |
| Versão do contrato | Preservar interpretação |
| Participante titular | Identificar a quem o objetivo pertence |
| Objetivo relacionado | Limitar o escopo |
| Ator | Identificar quem originou ou confirmou |
| Autoridade do ator | Informar o que esse ator pode declarar |
| Capacidade produtora | Identificar a responsabilidade funcional |
| Origem | Preservar proveniência |
| Canal | Informar onde ocorreu |
| Data do fato | Registrar quando aconteceu |
| Data de conhecimento | Registrar quando foi conhecido |
| Data de reconhecimento | Registrar quando foi validado |
| Correlação | Relacionar eventos da mesma operação |
| Causalidade | Indicar evento ou condição anterior |
| Finalidade | Limitar usos |
| Permissões | Limitar consumidores |
| Sensibilidade | Aplicar proteção |
| Estado anterior | Apoiar explicação da transição |
| Estado resultante | Informar o efeito reconhecido |
| Dados mínimos do fato | Representar o acontecimento |
| Confiança | Diferenciar certeza e interpretação |
| Motivo | Explicar a alteração quando necessário |
| Efeitos esperados | Orientar consumidores |
| Identificador de idempotência | Impedir repetição indevida |

# 618. Campos obrigatórios mínimos

Todo evento deverá possuir:

- identificador;
- tipo;
- versão;
- participante ou titular funcional;
- data de reconhecimento;
- origem;
- capacidade produtora;
- finalidade;
- dados mínimos necessários;
- identificação de correlação ou idempotência.

Eventos que alterem um objetivo deverão também possuir:

- objetivo relacionado;
- estado anterior;
- estado resultante;
- ator ou autoridade;
- efeitos funcionais aplicáveis.

# 619. Identidade do participante

Antes de reconhecer evento que produza efeito material, deverá existir segurança funcional suficiente sobre:

- participante correto;
- categoria do participante;
- papel do ator;
- autoridade para a ação;
- objetivo correto.

As categorias oficiais permanecem:

- Pessoa;
- Organização;
- Coletivo.

Associação incerta deverá impedir eventos de alto impacto.

# 620. Ator e autoridade

O ator poderá ser:

- participante titular;
- representante autorizado;
- organização;
- profissional;
- capacidade da Guivos;
- Guivos Intelligence;
- integração externa;
- processo institucional autorizado.

A autoridade deverá ser limitada.

Exemplos:

| Ator | Autoridade possível |
|---|---|
| Participante | Declarar, confirmar, corrigir, contestar, retirar e concluir objetivo pessoal |
| Organização | Confirmar requisito ou resultado institucional |
| Profissional | Emitir recomendação ou evidência sob sua competência |
| Guivos Intelligence | Produzir hipótese, sugestão ou interpretação |
| Integração externa | Confirmar fatos abrangidos pelo contrato da fonte |
| Capacidade consumidora | Solicitar recorte ou informar efeito dependente |

Nenhum ator deverá receber autoridade maior apenas por disponibilidade técnica.

# 621. Temporalidade

Os eventos deverão distinguir:

## Data do fato

Quando a mudança ou resultado ocorreu.

## Data de conhecimento

Quando a informação chegou à Guivos.

## Data de reconhecimento

Quando o fato foi admitido funcionalmente.

## Data de aplicação

Quando os efeitos foram incorporados.

Exemplo:

```text
Mudança de objetivo ocorreu:
01/06

Participante informou:
10/06

Evento reconhecido:
10/06

Recortes recompostos:
10/06
```

A Guivos não deverá registrar como se soubesse em 01/06 aquilo que somente conheceu em 10/06.

# 622. Correlação

Eventos relacionados à mesma operação deverão possuir identificador de correlação.

Exemplo:

```text
ObjetivoReformulado
→ RecorteDeObjetivosRecomposto
→ CapacidadeConsumidoraNotificada
→ DecisaoDependenteReavaliada
```

A correlação deverá permitir compreender o encadeamento sem transformar todos os fatos em um único evento indivisível.

# 623. Causalidade

O evento deverá informar, quando aplicável, o fato que o originou.

Exemplos:

- `ObjetivoImpactadoPorEventoDeVida` causado por `EventoDeVidaConfirmado`;
- `ObjetivoEmRevisao` causado por `ObjetivoEnvelhecido`;
- `PrioridadeAlterada` causada por confirmação de sugestão;
- `ObjetivoConcluidoReaberto` causado por contestação da conclusão.

A causalidade não deverá ser inventada quando não houver base suficiente.

# 624. Versionamento

Cada contrato deverá possuir versão.

Uma alteração de contrato deverá indicar se:

- preserva compatibilidade;
- exige transformação;
- altera significado;
- altera campos obrigatórios;
- altera efeitos;
- exige reprocessamento.

Eventos históricos deverão continuar interpretáveis conforme a versão com que foram reconhecidos.

# 625. Idempotência

O reprocessamento do mesmo evento não deverá:

- criar objetivo duplicado;
- alterar prioridade repetidamente;
- registrar o mesmo marco várias vezes;
- duplicar conclusão;
- revogar compartilhamento já revogado;
- notificar repetidamente sem necessidade;
- gerar múltiplos Próximos Passos equivalentes.

A chave de idempotência poderá considerar:

- tipo do evento;
- objetivo;
- origem;
- fato;
- versão;
- período;
- identificador externo.

# 626. Sensibilidade e minimização

Eventos relacionados a objetivos sensíveis deverão evitar registrar conteúdo desnecessário.

Exemplo:

```text
Evento compartilhado:
ObjetivoSensivelAtualizado

Recorte permitido:
Objetivo pessoal de saúde teve seu estado alterado

Conteúdo não permitido:
Descrição clínica completa sem finalidade
```

A sensibilidade deverá acompanhar o evento e seus recortes derivados.

# 627. Permissões e finalidade

O reconhecimento de um evento não deverá autorizar uso irrestrito de seu conteúdo.

Cada evento deverá preservar:

- finalidade original;
- consumidores permitidos;
- restrições;
- duração;
- efeitos de revogação.

Um evento poderá permanecer no histórico sem continuar disponível para novas decisões.

# 628. Famílias de eventos

Os eventos serão organizados nas seguintes famílias:

| Família | Finalidade |
|---|---|
| Direção | Registrar manifestação, intenção, sonho ou possibilidade |
| Existência do objetivo | Criar, propor, confirmar e ativar |
| Estrutura | Reformular, desdobrar, unificar e substituir |
| Prioridade | Sugerir, confirmar e alterar prioridade |
| Relações e conflitos | Registrar relações e tensões |
| Atualidade | Revisar e envelhecer |
| Operação | Pausar, retomar, bloquear e desbloquear |
| Critérios | Governar critérios de sucesso |
| Evidências | Registrar e contestar bases de interpretação |
| Progresso | Declarar, avaliar, inferir e contestar progresso |
| Marcos | Definir, alcançar, substituir ou dispensar |
| Conclusão | Sugerir, confirmar, contestar e reabrir |
| Encerramento | Retirar, arquivar e reativar |
| Integração | Recompor recortes e notificar consumidores |
| Controle | Alterar permissões e compartilhamentos |
| Exceção | Corrigir fatos e registrar falhas |

# 629. `ManifestacaoDeDirecaoIdentificada`

## Significado

Registra que uma manifestação relacionada a uma possível direção foi reconhecida.

Ela poderá representar:

- intenção;
- sonho;
- possibilidade;
- dúvida;
- objetivo mencionado;
- mudança de direção.

## Condições mínimas

- participante identificado;
- expressão preservada;
- origem conhecida;
- natureza ainda não necessariamente confirmada.

## Dados mínimos

- expressão original;
- natureza preliminar;
- data;
- origem;
- canal;
- confiança;
- sensibilidade.

## Efeitos permitidos

- iniciar exploração;
- propor formulação;
- solicitar confirmação;
- relacionar ao Contexto Vivo.

## Efeitos proibidos

- ativar objetivo;
- definir prioridade;
- compartilhar externamente;
- concluir que existe compromisso.

# 630. `ObjetivoCriado`

## Significado

Registra a criação da unidade funcional de um objetivo.

## Condições mínimas

- titular identificado;
- direção representável;
- origem registrada;
- estado inicial definido;
- finalidade legítima.

## Estado inicial possível

- Mencionado;
- Possibilidade;
- Em exploração;
- Proposto;
- Confirmado.

## Efeitos

- criar identificador próprio;
- iniciar histórico;
- permitir relação com critérios, conflitos e permissões;
- refletir a existência no portfólio adequado.

## Proibição

O evento não deverá significar que o objetivo está ativo.

# 631. `ObjetivoProposto`

## Significado

Registra que uma formulação foi apresentada ao participante para avaliação.

## Origem possível

- Guivos Intelligence;
- profissional;
- organização;
- capacidade da Guivos;
- aprofundamento de conversa;
- desdobramento de objetivo amplo.

## Dados mínimos

- formulação proposta;
- expressão ou evidência de origem;
- proponente;
- finalidade;
- usos pretendidos;
- necessidade de confirmação.

## Estado resultante

`Proposto`.

## Proibição

O objetivo proposto não deverá orientar decisões críticas antes da confirmação.

# 632. `ObjetivoConfirmado`

## Significado

Registra que o participante reconheceu determinada formulação como representação legítima de sua direção.

## Condições

- formulação apresentada;
- titular identificado;
- confirmação consciente;
- escopo compreensível;
- data e canal registrados.

## Dados mínimos

- formulação confirmada;
- expressão original;
- ator confirmador;
- escopo;
- finalidade;
- permissões vigentes.

## Efeito

O objetivo poderá tornar-se elegível para ativação.

## Não efeitos

A confirmação não deverá automaticamente:

- ativar o objetivo;
- definir prioridade;
- autorizar publicidade;
- autorizar compartilhamento externo;
- definir prazo;
- aceitar plano completo.

# 633. `ObjetivoNaoConfirmado`

## Significado

Registra que uma formulação proposta não foi confirmada.

Poderá decorrer de:

- rejeição;
- adiamento;
- classificação como possibilidade;
- necessidade de ajuste;
- falta de reconhecimento.

## Efeitos

- impedir ativação;
- manter manifestação em exploração, quando apropriado;
- interromper efeitos dependentes;
- preservar a proposta no histórico conforme autorização.

## Regra

Ausência de resposta não deverá ser registrada como rejeição definitiva sem base explícita.

# 634. `ObjetivoAtivado`

## Significado

Registra que um objetivo confirmado foi autorizado a orientar capacidades da jornada.

## Condições

- objetivo confirmado;
- finalidade autorizada;
- permissões definidas;
- ausência de conflito crítico impeditivo;
- titular ou autoridade competente.

## Dados mínimos

- finalidades ativas;
- consumidores permitidos;
- data efetiva;
- limitações;
- horizonte de validade, quando aplicável.

## Efeitos

- recompor recortes;
- permitir Próximos Passos;
- permitir seleção contextual de oportunidades;
- permitir acompanhamento conforme permissões;
- notificar consumidores relevantes.

## Regra

A ativação poderá ser parcial por finalidade.

# 635. `ObjetivoReformulado`

## Significado

Registra que a representação vigente do objetivo foi alterada, preservando continuidade funcional.

## Dados mínimos

- formulação anterior;
- nova formulação;
- motivo;
- data efetiva;
- elementos preservados;
- critérios afetados;
- relações afetadas;
- permissões afetadas.

## Efeitos

- criar nova versão;
- preservar a anterior;
- recompor recortes;
- revisar critérios e Próximos Passos;
- notificar consumidores.

## Regra

A reformulação não deverá apagar a expressão original.

# 636. `ObjetivoDesdobrado`

## Significado

Registra que um objetivo amplo originou objetivos relacionados.

## Dados mínimos

- objetivo de origem;
- objetivos derivados;
- relação funcional;
- motivo;
- critérios preservados ou separados;
- autorizações individuais.

## Efeitos

- criar unidades próprias;
- preservar relação com o objetivo maior;
- permitir estados e prioridades independentes.

## Proibição

O desdobramento não deverá converter automaticamente objetivos derivados em tarefas ou objetivos ativos.

# 637. `ObjetivosUnificados`

## Significado

Registra que objetivos anteriormente distintos passaram a possuir uma representação unificada.

## Condições

- confirmação adequada;
- compatibilidade de finalidade;
- permissões reconciliadas;
- históricos preservados;
- ausência de conflito impeditivo.

## Dados mínimos

- objetivos de origem;
- novo objetivo;
- elementos preservados;
- critérios recompostos;
- relações transferidas;
- motivo.

## Regra

Os objetivos de origem deverão permanecer historicamente identificáveis.

# 638. `PrioridadeSugerida`

## Significado

Registra uma proposta explicável de prioridade.

## Origem possível

- prazo;
- urgência;
- Evento de Vida;
- importância declarada;
- dependência;
- custo de adiamento;
- oportunidade temporal;
- conflito.

## Dados mínimos

- prioridade sugerida;
- critérios utilizados;
- período;
- objetivos afetados;
- confiança;
- proponente.

## Efeito

Apresentar sugestão ao participante.

## Proibição

Não deverá alterar a prioridade vigente.

# 639. `PrioridadeConfirmada`

## Significado

Registra que o participante confirmou uma prioridade proposta.

## Dados mínimos

- prioridade anterior;
- prioridade confirmada;
- origem da proposta;
- período;
- motivo;
- objetivos afetados.

## Efeitos

- permitir alteração operacional;
- recompor ordenações;
- reavaliar decisões dependentes.

# 640. `PrioridadeAlterada`

## Significado

Registra a mudança efetiva da prioridade de um objetivo.

## Origem possível

- declaração direta;
- confirmação de sugestão;
- Evento de Vida;
- revisão;
- mudança de contexto.

## Dados mínimos

- prioridade anterior;
- prioridade resultante;
- data efetiva;
- duração, quando contextual;
- motivo;
- ator.

## Efeitos

- reavaliar Próximos Passos;
- reordenar oportunidades;
- preservar objetivos de menor prioridade;
- registrar impacto.

## Regra

Prioridade não deverá alterar automaticamente o valor, estado ou validade do objetivo.

# 641. `RelacaoEntreObjetivosDefinida`

## Significado

Registra uma relação funcional reconhecida entre objetivos.

## Tipos possíveis

- depende de;
- apoia;
- complementa;
- compete com;
- substitui;
- deriva de;
- contribui parcialmente;
- pertence a direção maior.

## Dados mínimos

- objetivos envolvidos;
- tipo;
- origem;
- confirmação;
- efeitos;
- validade.

Relações sugeridas não deverão produzir efeitos materiais antes da confirmação exigida.

# 642. `ConflitoEntreObjetivosIdentificado`

## Significado

Registra uma tensão relevante entre dois ou mais objetivos.

## Dados mínimos

- objetivos envolvidos;
- tipo;
- recursos disputados;
- período;
- impacto;
- origem;
- confiança;
- decisões dependentes.

## Efeitos

- tornar conflito visível;
- limitar automações incompatíveis;
- solicitar revisão;
- propagar incerteza.

## Proibição

Não deverá escolher silenciosamente o objetivo prevalente.

# 643. `ConflitoEntreObjetivosResolvido`

## Significado

Registra um tratamento funcional do conflito.

## Resultados possíveis

- coexistência;
- sequência;
- prioridade contextual;
- pausa;
- reformulação;
- redução de escopo;
- retirada;
- manutenção consciente;
- adiamento.

## Dados mínimos

- conflito;
- decisão;
- ator;
- efeitos;
- período;
- possibilidade de revisão.

A resolução deverá permanecer reabrível quando novas condições surgirem.

# 644. `RevisaoDeObjetivoSolicitada`

## Significado

Registra que existe motivo funcional para revisar determinado elemento do objetivo.

## Motivos possíveis

- envelhecimento;
- Evento de Vida;
- conflito;
- bloqueio;
- critério desatualizado;
- permissão expirada;
- prioridade possivelmente inadequada;
- conclusão sugerida.

## Dados mínimos

- objetivo;
- elemento afetado;
- motivo;
- impacto;
- urgência;
- possibilidade de adiamento;
- efeito da ausência de resposta.

## Regra

A solicitação deverá limitar-se aos elementos afetados.

# 645. `ObjetivoRevisado`

## Significado

Registra que uma revisão foi concluída.

## Resultados possíveis

- confirmação sem alteração;
- prioridade alterada;
- reformulação;
- critério atualizado;
- pausa;
- retomada;
- retirada;
- conclusão;
- nova revisão futura.

## Dados mínimos

- elementos avaliados;
- estado anterior;
- resultado;
- ator;
- data;
- efeitos;
- limitações.

# 646. `ObjetivoEnvelhecido`

## Significado

Registra redução de segurança sobre a atualidade do objetivo.

## Condições possíveis

- passagem do tempo;
- mudança de contexto;
- Evento de Vida;
- dependência alterada;
- prioridade não revisada;
- permissão expirada.

## Dados mínimos

- classe temporal;
- estado de atualidade anterior;
- novo estado;
- finalidade afetada;
- impacto;
- necessidade de revisão.

## Regra

O evento não deverá significar que o objetivo é falso, retirado ou inválido.

# 647. `ObjetivoPausado`

## Significado

Registra interrupção temporária do uso operacional.

## Dados mínimos

- motivo, quando informado;
- data efetiva;
- finalidades suspensas;
- critérios de retomada;
- efeitos sobre capacidades consumidoras.

## Efeitos

- interromper novos Próximos Passos automáticos;
- deixar de priorizar oportunidades;
- preservar histórico e validade;
- recompor recortes.

## Regra

A pausa não deverá ser classificada como fracasso ou desistência.

# 648. `ObjetivoRetomado`

## Significado

Registra a retomada de um objetivo pausado.

## Condições

- objetivo ainda representativo;
- permissões válidas;
- contexto minimamente adequado;
- conflitos críticos tratados.

## Dados mínimos

- ciclo retomado;
- revisão realizada;
- formulação vigente;
- prioridade;
- consumidores reativados.

A retomada poderá exigir reformulação antes da reativação operacional.

# 649. `ObjetivoBloqueado`

## Significado

Registra a existência de impedimento atual.

## Dados mínimos

- causa;
- impacto;
- data;
- condição de desbloqueio;
- alternativas;
- revisão prevista;
- dependências afetadas.

## Regra

O bloqueio não deverá representar incapacidade pessoal nem retirada do objetivo.

# 650. `ObjetivoDesbloqueado`

## Significado

Registra que a condição impeditiva deixou de existir ou foi reduzida.

## Dados mínimos

- bloqueio anterior;
- condição resolvida;
- evidência;
- data;
- limitações restantes.

## Regra

O desbloqueio não deverá ativar objetivo pausado ou desatualizado automaticamente.

# 651. `CriterioDeSucessoProposto`

## Significado

Registra uma possível forma de reconhecer progresso ou conclusão.

## Dados mínimos

- objetivo;
- descrição;
- natureza;
- proponente;
- forma de avaliação;
- evidências possíveis;
- efeito pretendido.

## Estado resultante

`Proposto`.

O critério não deverá orientar conclusão pessoal antes da confirmação.

# 652. `CriterioDeSucessoConfirmado`

## Significado

Registra que um critério foi aceito como base legítima de acompanhamento.

## Dados mínimos

- critério;
- objetivo;
- ator;
- natureza;
- regra de atendimento;
- efeito sobre progresso;
- efeito sobre conclusão;
- permissões.

Confirmar o critério não autoriza automaticamente compartilhamento das evidências.

# 653. `CriterioDeSucessoRevisado`

## Significado

Registra alteração de critério vigente.

## Dados mínimos

- critério anterior;
- novo critério;
- motivo;
- data efetiva;
- resultados preservados;
- impactos sobre progresso e conclusão.

A revisão não deverá apagar resultados legitimamente reconhecidos sob o critério anterior.

# 654. `CriterioDeSucessoRetirado`

## Significado

Registra que determinado critério deixou de orientar o objetivo.

## Efeitos

- interromper novos usos;
- preservar histórico;
- reavaliar conclusões dependentes, quando necessário;
- manter outros critérios válidos.

A retirada do critério não deverá retirar automaticamente o objetivo.

# 655. `LinhaDeBaseRegistrada`

## Significado

Registra a condição inicial conhecida para determinado critério ou ciclo.

## Dados mínimos

- objetivo;
- critério;
- condição inicial;
- origem;
- data;
- confiança;
- contexto;
- limitações;
- sensibilidade.

A linha de base não deverá ser reconstruída artificialmente sem indicação de incerteza.

# 656. `EvidenciaDeObjetivoRegistrada`

## Significado

Registra uma informação capaz de sustentar interpretação sobre atividade, resultado, progresso, marco ou conclusão.

## Dados mínimos

- tipo;
- origem;
- data do fato;
- data de conhecimento;
- objetivo;
- critério ou marco relacionado;
- confiança;
- finalidade;
- permissões;
- sensibilidade.

## Efeitos possíveis

- iniciar avaliação;
- apoiar marco;
- sustentar conclusão;
- produzir conflito;
- atualizar confiança.

## Regra

Registrar evidência não deverá produzir automaticamente progresso ou conclusão.

# 657. `EvidenciaDeObjetivoContestada`

## Significado

Registra que o participante ou ator autorizado contesta conteúdo, origem, interpretação ou uso de uma evidência.

## Dados mínimos

- evidência;
- aspecto contestado;
- ator;
- data;
- efeito solicitado;
- decisões dependentes.

## Efeitos

- reduzir confiança;
- suspender conclusão dependente;
- iniciar correção;
- notificar consumidores;
- preservar o registro anterior.

# 658. `EvidenciasConflitantesIdentificadas`

## Significado

Registra que evidências relacionadas sustentam interpretações incompatíveis.

## Dados mínimos

- evidências envolvidas;
- objetivo;
- critério;
- tipo de divergência;
- temporalidade;
- impacto;
- decisões afetadas.

## Efeito

Impedir conclusão silenciosa e propagar incerteza.

# 659. `ProgressoDeObjetivoDeclarado`

## Significado

Registra a percepção expressa pelo participante sobre seu progresso.

## Conteúdo possível

- avanço;
- ausência de avanço;
- dificuldade;
- redução;
- resultado parcial;
- manutenção;
- conclusão percebida.

## Dados mínimos

- declaração;
- objetivo;
- período;
- ator;
- contexto;
- confiança declarativa.

A declaração deverá permanecer diferenciada de avaliação institucional ou inferencial.

# 660. `ProgressoDeObjetivoAvaliado`

## Significado

Registra uma avaliação funcional baseada em objetivo, critério, contexto e evidências.

## Dados mínimos

- objetivo;
- critério;
- linha de base;
- evidências;
- período;
- modelo de progresso;
- estado resultante;
- confiança;
- limitações;
- ator avaliador.

## Estados possíveis

- sem evidência suficiente;
- inicial;
- parcial;
- relevante;
- manutenção confirmada;
- resultado alcançado;
- indeterminado;
- contestado;
- redução de resultado.

# 661. `ProgressoDeObjetivoInferido`

## Significado

Registra uma interpretação inferencial ainda não confirmada.

## Dados mínimos

- evidências utilizadas;
- método funcional;
- confiança;
- limitações;
- finalidade;
- necessidade de confirmação;
- efeitos permitidos.

## Efeitos permitidos

- apresentar hipótese;
- solicitar confirmação;
- apoiar exploração.

## Efeitos proibidos

- concluir objetivo pessoal;
- alterar prioridade;
- produzir avaliação institucional;
- comparar participantes;
- compartilhar externamente sem autorização.

# 662. `ProgressoDeObjetivoContestado`

## Significado

Registra contestação da interpretação de progresso.

## Efeitos

- suspender efeitos críticos;
- preservar avaliação anterior;
- reabrir análise;
- revisar evidências;
- recompor recortes;
- notificar consumidores.

A contestação não deverá ser tratada como resistência do participante.

# 663. `ReducaoDeProgressoIdentificada`

## Significado

Registra que determinado resultado ou condição apresentou redução após avanço anterior.

## Dados mínimos

- estado anterior;
- estado atual;
- período;
- evidências;
- confiança;
- contexto;
- possíveis causas, quando autorizadas.

## Regra

O evento não deverá apagar progresso histórico nem classificar fracasso pessoal.

# 664. `MarcoDeObjetivoDefinido`

## Significado

Registra a criação ou confirmação de um resultado intermediário significativo.

## Dados mínimos

- objetivo;
- descrição;
- natureza;
- origem;
- condição de alcance;
- evidências aceitas;
- efeitos;
- autoridade de confirmação.

Marco não deverá ser reduzido a tarefa operacional.

# 665. `MarcoDeObjetivoAlcancado`

## Significado

Registra que a condição do marco foi reconhecida como atendida.

## Dados mínimos

- marco;
- data;
- evidência;
- origem;
- confiança;
- ator confirmador;
- efeito sobre o objetivo.

## Regra

O alcance do marco não deverá concluir o objetivo salvo regra confirmada.

# 666. `MarcoDeObjetivoDispensado`

## Significado

Registra que determinado marco deixou de ser necessário.

## Motivos possíveis

- caminho alternativo;
- reformulação;
- resultado equivalente;
- mudança externa;
- perda de relevância.

## Efeitos

- preservar histórico;
- evitar bloqueio indevido;
- recalcular sequência de marcos;
- manter progresso legítimo.

# 667. `ResultadoParcialReconhecido`

## Significado

Registra que parte relevante do resultado foi alcançada.

## Dados mínimos

- parte alcançada;
- critérios atendidos;
- critérios pendentes;
- evidências;
- impacto;
- decisão sobre continuidade.

## Efeitos possíveis

- reconhecer marco;
- reformular objetivo;
- criar objetivo derivado;
- manter objetivo ativo;
- encerrar parte específica.

# 668. `ConclusaoDeObjetivoSugerida`

## Significado

Registra que existem sinais suficientes para apresentar uma possível conclusão ao participante.

## Dados mínimos

- critérios considerados;
- evidências;
- confiança;
- limitações;
- efeitos previstos;
- necessidade de confirmação.

## Regra

A sugestão não deverá alterar o estado para `Concluído`.

# 669. `ObjetivoConcluido`

## Significado

Registra que o resultado esperado foi reconhecido como suficientemente alcançado ou que o ciclo definido foi encerrado.

## Condições

- objetivo vigente;
- critérios aplicáveis;
- evidências proporcionais;
- ausência de conflito crítico;
- autoridade adequada;
- natureza do objetivo respeitada.

## Dados mínimos

- forma de conclusão;
- ator;
- critérios;
- evidências;
- data;
- resultado;
- efeitos;
- possibilidade de reabertura.

## Formas possíveis

- declarada;
- confirmada por critério;
- institucional;
- automática autorizada;
- conclusão de ciclo;
- exploratória;
- parcial.

## Regra

Objetivos pessoais qualitativos ou transformacionais não deverão ser concluídos apenas por inferência.

# 670. `ConclusaoDeObjetivoContestada`

## Significado

Registra contestação da conclusão.

## Motivos possíveis

- participante não reconhece resultado;
- evidência incorreta;
- critério desatualizado;
- conflito;
- conclusão aplicada indevidamente;
- natureza interpretada incorretamente.

## Efeitos

- suspender efeitos dependentes;
- reabrir avaliação;
- preservar conclusão anterior;
- permitir correção;
- notificar consumidores.

# 671. `ObjetivoConcluidoReaberto`

## Significado

Registra novo momento funcional após conclusão anterior.

## Motivos possíveis

- novo ciclo;
- aprofundamento;
- contexto alterado;
- conclusão corrigida;
- condição deixou de ser suficiente;
- decisão do participante.

## Dados mínimos

- conclusão anterior;
- motivo;
- novo ciclo;
- formulação vigente;
- critérios;
- permissões;
- data.

A reabertura não deverá apagar a conclusão anterior.

# 672. `ObjetivoRetirado`

## Significado

Registra que o participante não deseja mais que o objetivo oriente sua jornada.

## Condições

- autoridade adequada;
- escopo claro;
- data efetiva.

## Efeitos

- interromper novos usos;
- retirar de recortes ativos;
- notificar consumidores;
- revisar decisões dependentes;
- preservar histórico conforme autorização.

## Regra

A retirada não deverá exigir justificativa.

# 673. `ObjetivoSubstituido`

## Significado

Registra que outra formulação ou objetivo passou a representar melhor a direção atual.

## Dados mínimos

- objetivo anterior;
- objetivo substituto;
- motivo;
- elementos transferidos;
- critérios;
- relações;
- permissões;
- data efetiva.

O objetivo anterior deverá permanecer historicamente identificável.

# 674. `ObjetivoArquivado`

## Significado

Registra que o objetivo deixou a operação cotidiana e permanece no histórico.

## Motivos possíveis

- conclusão;
- retirada;
- substituição;
- encerramento institucional;
- decisão do participante.

## Efeitos

- remover de recortes operacionais;
- preservar histórico;
- manter possibilidade de consulta;
- limitar novos usos.

# 675. `ObjetivoReativado`

## Significado

Registra que objetivo retirado ou arquivado iniciou novo momento operacional.

## Condições

- atualidade avaliada;
- formulação revisada;
- contexto considerado;
- permissões válidas;
- conflitos tratados.

## Dados mínimos

- ciclo anterior;
- novo ciclo;
- estado resultante;
- critérios;
- prioridade;
- consumidores autorizados.

A reativação não deverá sobrescrever o ciclo anterior.

# 676. `ObjetivoImpactadoPorEventoDeVida`

## Significado

Registra que um Evento de Vida produziu impacto reconhecido sobre determinado objetivo.

## Impactos possíveis

- revisão;
- alteração de prioridade;
- bloqueio;
- urgência;
- reformulação;
- retirada;
- criação de conflito;
- mudança de horizonte.

## Dados mínimos

- Evento de Vida;
- objetivo;
- impacto;
- confiança;
- elementos afetados;
- necessidade de participação;
- efeitos permitidos.

## Regra

Um Evento de Vida não deverá alterar todos os objetivos automaticamente.

# 677. `PermissaoDeObjetivoAlterada`

## Significado

Registra mudança nas permissões de uso de um objetivo.

## Dados mínimos

- objetivo;
- finalidade;
- consumidores;
- permissão anterior;
- nova permissão;
- data efetiva;
- ator.

## Efeitos

- recompor recortes;
- interromper ou permitir usos;
- notificar consumidores;
- preservar histórico.

# 678. `CompartilhamentoDeObjetivoRevogado`

## Significado

Registra a retirada de autorização para compartilhamento externo.

## Dados mínimos

- objetivo;
- destinatário;
- finalidade;
- elementos afetados;
- data efetiva;
- obrigações residuais legítimas;
- status de propagação.

## Efeitos

- interromper novos compartilhamentos;
- notificar destinatários ou consumidores;
- recompor recortes;
- informar processamento pendente.

A revogação não deverá ser apresentada como concluída antes da propagação efetiva.

# 679. `RecorteDeObjetivosRecomposto`

## Significado

Registra que um recorte fornecido a determinada capacidade foi recalculado.

## Gatilhos possíveis

- ativação;
- reformulação;
- prioridade;
- pausa;
- conclusão;
- retirada;
- permissão;
- conflito;
- envelhecimento;
- contestação.

## Dados mínimos

- consumidor;
- finalidade;
- versão anterior;
- versão resultante;
- elementos incluídos;
- elementos retirados;
- validade;
- limitações.

O evento não deverá expor conteúdo além do necessário ao consumidor.

# 680. `CapacidadeConsumidoraNotificada`

## Significado

Registra que determinada capacidade recebeu informação sobre mudança relevante.

## Dados mínimos

- capacidade;
- evento causador;
- objetivo;
- recorte;
- finalidade;
- ação esperada;
- data;
- status.

## Ações esperadas possíveis

- reavaliar decisão;
- suspender ação;
- cancelar Próximo Passo;
- reordenar oportunidade;
- atualizar intervenção;
- encerrar acompanhamento.

A notificação não significa que a reavaliação foi concluída.

# 681. `DecisaoDependenteDeObjetivoReavaliada`

## Significado

Registra que uma decisão baseada no objetivo foi reavaliada após mudança relevante.

## Dados mínimos

- decisão;
- objetivo;
- evento causador;
- resultado da reavaliação;
- capacidade responsável;
- data;
- efeitos.

## Resultados possíveis

- mantida;
- ajustada;
- suspensa;
- cancelada;
- substituída;
- aguardando informação.

# 682. Eventos da visão `Meus Objetivos`

Eventos originados na visão deverão utilizar os mesmos contratos da capacidade.

Exemplo:

```text
ObjetivoConfirmadoPelaVisao
```

deverá produzir funcionalmente:

```text
ObjetivoConfirmado
origem: Meus Objetivos
canal: aplicativo ou web
```

Sufixos como `PelaVisao` poderão ser utilizados para telemetria ou experiência, mas não deverão criar significado funcional paralelo.

# 683. Eventos conversacionais

Alterações realizadas por conversa deverão registrar:

- conteúdo apresentado;
- confirmação;
- canal;
- ator;
- interpretação;
- efeitos;
- acesso posterior em `Meus Objetivos`.

A conversa não deverá produzir contexto paralelo ou evento com contrato diferente.

# 684. Eventos compostos

Uma ação poderá produzir vários eventos relacionados.

Exemplo:

```text
Objetivo retirado
→ ObjetivoRetirado
→ RecorteDeObjetivosRecomposto
→ CapacidadeConsumidoraNotificada
→ DecisaoDependenteDeObjetivoReavaliada
```

Cada evento deverá manter significado próprio.

A falha em uma etapa não deverá fazer parecer que todas foram concluídas.

# 685. Atomicidade funcional

Quando efeitos não puderem ser aplicados integralmente, deverá existir clareza sobre:

- fato reconhecido;
- efeitos já aplicados;
- efeitos pendentes;
- capacidades não atualizadas;
- riscos;
- ação de recuperação.

Exemplo:

> O objetivo foi retirado, mas duas capacidades ainda estão processando a atualização. Novos usos permanecem suspensos.

# 686. Eventos retroativos

Quando um fato passado for conhecido posteriormente, o evento deverá registrar:

- data real do fato;
- data de conhecimento;
- data de reconhecimento;
- decisões anteriores afetadas;
- limites da correção;
- necessidade de reavaliação.

O histórico não deverá ser reescrito como se a informação estivesse disponível anteriormente.

# 687. Correção de eventos

Um evento incorreto deverá ser corrigido por evento compensatório.

O evento de correção deverá indicar:

- evento corrigido;
- erro;
- informação correta;
- ator;
- data;
- efeitos dependentes;
- recortes recompostos.

O evento original deverá permanecer no histórico com indicação de correção.

# 688. Duplicidade

Eventos duplicados deverão ser identificados antes da produção de efeitos.

A detecção deverá considerar:

- objetivo;
- tipo;
- origem;
- fato;
- período;
- identificador externo;
- correlação;
- chave de idempotência.

Duplicidade técnica não deverá resultar em duplicidade funcional.

# 689. Reprocessamento

O reprocessamento poderá ocorrer por:

- recuperação de falha;
- nova versão;
- correção;
- sincronização;
- reconstrução de estado;
- auditoria.

Ele deverá:

- preservar eventos reconhecidos;
- evitar efeitos duplicados;
- registrar a versão utilizada;
- indicar resultados diferentes;
- não ampliar permissões.

# 690. Ordenação funcional

Eventos relacionados ao mesmo objetivo deverão respeitar causalidade funcional.

Exemplo inadequado:

```text
ObjetivoAtivado
antes de
ObjetivoConfirmado
```

Exemplo possível:

```text
ObjetivoConfirmado
→ ObjetivoAtivado
→ RecorteDeObjetivosRecomposto
```

Eventos recebidos fora de ordem deverão ser:

- aguardados;
- reconciliados;
- tratados como conflito;
- rejeitados;
- aplicados com limitação explícita.

# 691. Concorrência de alterações

Alterações simultâneas poderão ocorrer em:

- prioridade;
- formulação;
- permissão;
- critérios;
- conclusão;
- retirada.

A capacidade deverá:

- detectar versões concorrentes;
- preservar todas as propostas;
- evitar sobrescrita silenciosa;
- solicitar resolução quando necessário;
- indicar estado pendente.

# 692. Falha de processamento

Falhas deverão produzir registro funcional quando houver impacto relevante.

O evento poderá indicar:

- operação;
- etapa;
- objetivo;
- erro funcional;
- efeitos aplicados;
- efeitos pendentes;
- risco;
- ação de recuperação;
- necessidade de informar o participante.

Falhas técnicas internas não deverão expor detalhes desnecessários ao participante.

# 693. Falha segura

Quando um evento relevante não puder ser processado com segurança:

- novas decisões dependentes deverão ser suspensas;
- o último estado válido poderá ser preservado;
- incerteza deverá ser explicitada;
- permissões mais restritivas deverão prevalecer;
- conclusão não deverá ser presumida;
- o participante deverá receber informação proporcional.

# 694. Responsabilidade da capacidade produtora

A capacidade produtora deverá:

- validar pré-condições;
- reconhecer o fato;
- produzir o evento;
- preservar origem;
- aplicar permissões;
- definir efeitos esperados;
- evitar duplicidade;
- registrar falha.

Ela não deverá decidir como todas as capacidades consumidoras implementarão seus efeitos.

# 695. Responsabilidade das capacidades consumidoras

Cada consumidora deverá:

- verificar finalidade;
- aceitar somente a versão compatível;
- respeitar permissões;
- aplicar idempotência;
- reavaliar suas decisões;
- registrar resultado;
- informar falha;
- não ampliar significado.

A consumidora não deverá reinterpretar um objetivo confirmado como autorização universal.

# 696. Relação com o Contexto Vivo

Eventos de Objetivos poderão atualizar a dimensão `Direção` do Contexto Vivo.

O Contexto Vivo deverá receber apenas recortes necessários, como:

- objetivo ativo;
- prioridade;
- estado;
- atualidade;
- conflito;
- conclusão;
- retirada.

Ele não deverá absorver integralmente a responsabilidade pelo ciclo de vida dos objetivos.

# 697. Relação com Próximos Passos

A Capacidade 05 poderá consumir eventos como:

- `ObjetivoAtivado`;
- `PrioridadeAlterada`;
- `ObjetivoReformulado`;
- `ObjetivoPausado`;
- `ObjetivoBloqueado`;
- `ObjetivoConcluido`;
- `ObjetivoRetirado`.

Ela deverá reavaliar seus próprios Próximos Passos sem presumir que todo evento exige ação.

# 698. Relação com Oportunidades Ativas

A Capacidade 06 poderá utilizar:

- objetivos ativos;
- prioridade;
- critérios relevantes;
- conflitos;
- permissões;
- estado de atualidade.

Objetivos pausados, retirados ou desatualizados para a finalidade não deverão continuar ordenando oportunidades.

# 699. Relação com Intervenções Contextuais

A Capacidade 07 poderá utilizar eventos para decidir se deverá:

- agir;
- perguntar;
- esperar;
- observar;
- silenciar.

Ela não deverá transformar todo evento em notificação.

# 700. Relação com Experiências

A Capacidade 08 poderá:

- relacionar experiências a objetivos;
- fornecer evidências;
- informar resultados;
- contribuir para marcos.

A experiência realizada não deverá gerar automaticamente `ProgressoDeObjetivoAvaliado`.

# 701. Relação com Evolução Contínua

A Capacidade 09 poderá consumir:

- progresso;
- marcos;
- conclusões;
- reaberturas;
- resultados parciais;
- percepções do participante.

Ela deverá distinguir conclusão de objetivo de transformação humana ampla.

# 702. Relação com Guivos Intelligence

Guivos Intelligence poderá produzir:

- propostas;
- hipóteses;
- relações sugeridas;
- prioridades sugeridas;
- progresso inferido;
- conclusão sugerida.

Ela não poderá produzir unilateralmente:

- `ObjetivoConfirmado`;
- `ObjetivoAtivado`;
- `PrioridadeConfirmada`;
- conclusão pessoal definitiva;
- retirada;
- compartilhamento externo.

# 703. Explicabilidade por eventos

A Guivos deverá conseguir responder:

- quando o objetivo surgiu;
- quem o propôs;
- quem o confirmou;
- quando foi ativado;
- por que recebeu prioridade;
- quais critérios foram utilizados;
- quais evidências sustentaram progresso;
- por que foi pausado;
- quem reconheceu a conclusão;
- quais capacidades foram notificadas;
- quais efeitos permanecem pendentes;
- como ocorreu uma correção.

# 704. Auditoria funcional

A auditoria deverá permitir reconstruir:

```text
manifestação
→ criação
→ confirmação
→ ativação
→ alterações
→ progresso
→ conclusão ou retirada
→ efeitos nas capacidades consumidoras
```

A auditoria deverá preservar:

- versões;
- causalidade;
- correlação;
- permissões;
- contestações;
- correções;
- falhas;
- reprocessamentos.

# 705. Retenção e privacidade

A retenção dos eventos deverá considerar:

- finalidade;
- obrigação legítima;
- sensibilidade;
- histórico necessário;
- contestação;
- auditoria;
- retirada;
- revogação;
- categoria do participante.

Eventos históricos não deverão permanecer indefinidamente disponíveis para novas finalidades apenas porque foram preservados para auditoria.

# 706. Eventos de Pessoa, Organização e Coletivo

## Pessoa

Ações pessoais deverão preservar autoria e controle individual.

## Organização

Eventos deverão identificar:

- papel do ator;
- autoridade;
- titularidade institucional;
- políticas aplicáveis;
- separação de objetivos pessoais.

## Coletivo

Eventos deverão preservar:

- regras de decisão;
- representação;
- participação;
- agregação;
- possibilidade de saída;
- proteção dos membros.

O mesmo nome de evento poderá possuir requisitos de autoridade diferentes conforme a categoria.

# 707. Eventos proibidos

Não deverão ser produzidos eventos que afirmem, sem base adequada:

- `ObjetivoPessoalInferidoComoConfirmado`;
- `ObjetivoAtivadoPorComportamento`;
- `PrioridadeImposta`;
- `ProgressoComprovadoPorClique`;
- `ConclusaoPessoalAutomaticaPorInferencia`;
- `ObjetivoRetiradoPorInatividade`;
- `FracassoDoParticipanteIdentificado`;
- `AmbicaoInsuficienteDetectada`;
- `CompartilhamentoAutorizadoImplicitamente`.

Esses significados violariam os contratos da capacidade.

# 708. Métricas derivadas dos eventos

Os eventos poderão apoiar indicadores como:

- tempo entre proposição e confirmação;
- taxa de objetivos não confirmados;
- ativações por finalidade;
- alterações de prioridade;
- revisões concluídas;
- envelhecimento;
- conflitos;
- contestações;
- reaberturas;
- falhas de propagação;
- efeitos duplicados evitados.

As métricas deverão avaliar a capacidade e seus processos, não a qualidade do participante.

# 709. Critérios funcionais de aceite

Os contratos serão considerados adequadamente definidos quando:

1. diferenciarem comando, proposta e evento;
2. preservarem autoria, origem e autoridade;
3. registrarem temporalidade explícita;
4. permitirem correlação e causalidade;
5. possuírem versão;
6. evitarem efeitos duplicados;
7. limitarem conteúdo por finalidade;
8. preservarem sensibilidade e permissões;
9. impedirem ativação por inferência;
10. separarem confirmação de ativação;
11. registrarem prioridade sugerida e aplicada separadamente;
12. preservarem conflitos;
13. envelhecerem sem declarar falsidade;
14. diferenciarem evidência e progresso;
15. impedirem conclusão pessoal por inferência;
16. permitirem contestação e correção;
17. preservarem conclusões anteriores após reabertura;
18. propagarem alterações por recortes mínimos;
19. distinguirem notificação de reavaliação concluída;
20. operarem com idempotência;
21. tratarem concorrência e ordenação;
22. registrarem falha e recuperação;
23. permitirem explicação e auditoria;
24. respeitarem Pessoa, Organização e Coletivo;
25. não classificarem o valor humano.

# 710. Regras fundamentais dos eventos

1. Evento registra fato reconhecido, não intenção futura.
2. Comando, proposta e evento são conceitos distintos.
3. Evento histórico não deverá ser reescrito.
4. Correção deverá produzir novo evento.
5. Origem e autoridade deverão acompanhar o fato.
6. Temporalidade deverá distinguir fato, conhecimento e reconhecimento.
7. Confirmação não equivale a ativação.
8. Inferência não produz objetivo ativo.
9. Prioridade sugerida não equivale a prioridade aplicada.
10. Evidência registrada não equivale a progresso.
11. Atividade não produz progresso automaticamente.
12. Progresso inferido não produz conclusão pessoal.
13. Conclusão contestada deverá suspender efeitos críticos.
14. Reabertura não apaga conclusão anterior.
15. Retirada interrompe novos usos.
16. Permissões limitam eventos e consumidores.
17. Recortes deverão conter somente o necessário.
18. Reprocessamento não poderá duplicar efeitos.
19. Falhas deverão reduzir automação, não ampliar suposições.
20. Capacidades consumidoras deverão reavaliar suas próprias decisões.
21. Histórico deverá permanecer explicável.
22. Eventos não poderão classificar o valor do participante.
23. Implementações técnicas deverão preservar o significado funcional.
24. Nenhuma integração poderá aumentar a autoridade de uma fonte.
25. O participante deverá permanecer no controle de sua direção.

Com isso, ficam definidos os **contratos dos eventos funcionais da Capacidade 03 — Objetivos**, incluindo criação, confirmação, ativação, prioridade, revisão, progresso, evidências, conclusão, contestação e propagação.

O próximo bloco deverá detalhar:

> **as integrações funcionais da Capacidade de Objetivos com o Contexto Vivo, Eventos de Vida, Próximos Passos, Oportunidades Ativas, Intervenções Contextuais, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer e serviços especializados.**