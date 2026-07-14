---
id: PAS-001-PP-EVENT-001
title: Contratos dos Eventos Funcionais da Capacidade de Próximos Passos
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-PP-FOUNDATION-001
  - PAS-001-PP-LIFECYCLE-001
  - PAS-001-PP-VIEW-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-PP-EVENT-001 — Contratos dos Eventos Funcionais da Capacidade de Próximos Passos

## 1. Autoridade e vínculo

Este documento é a **quarta extensão normativa da Capacidade 05 — Próximos Passos** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 0 a 1796 consolidadas pelo `PAS-001 0.5.0`, pelas extensões normativas de Contexto Vivo, Objetivos, Eventos de Vida e pelos documentos `PAS-001-PP-FOUNDATION-001 1.0.0`, `PAS-001-PP-LIFECYCLE-001 1.0.0` e `PAS-001-PP-VIEW-001 1.0.0`.

Esta extensão mantém a Capacidade 05 no estado `In progress` e eleva seu progresso editorial de referência de `60%` para `80%`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade da especificação-base ou das capacidades concluídas.

# 1797. Contratos dos eventos funcionais dos Próximos Passos

Os eventos funcionais deverão representar fatos reconhecidos sobre a evolução de um Próximo Passo.

Seu fluxo conceitual será:

```text
comando
→ validação
→ proposta, quando necessária
→ decisão funcional
→ evento reconhecido
→ atualização do estado
→ produção de recortes
→ processamento pelas capacidades consumidoras
```

Um evento funcional não deverá representar apenas:

- intenção de alteração;
- solicitação pendente;
- hipótese não confirmada;
- recomendação;
- clique;
- visualização;
- tentativa técnica;
- mensagem ainda não processada.

# 1798. Objetivos dos contratos

Os contratos deverão:

1. distinguir comandos, propostas e fatos reconhecidos;
2. preservar titularidade;
3. identificar atores e autoridades;
4. representar temporalidades;
5. preservar imutabilidade histórica;
6. permitir correção compensatória;
7. controlar transições de estado;
8. evitar duplicidades;
9. ordenar alterações concorrentes;
10. sustentar recorrência;
11. governar passos compartilhados;
12. propagar somente recortes necessários;
13. preservar privacidade;
14. permitir auditoria;
15. operar com falha segura;
16. manter o participante no controle.

# 1799. Comando, proposta e evento

## Comando funcional

Solicitação para que determinada alteração seja avaliada.

Exemplo:

```text
ConfirmarProximoPasso
```

## Proposta funcional

Possibilidade apresentada para decisão.

Exemplo:

```text
ProximoPassoProposto
```

## Evento funcional

Fato reconhecido após validação e aplicação suficiente.

Exemplo:

```text
ProximoPassoConfirmado
```

# 1800. Regras de distinção

1. Comando não representa fato ocorrido.
2. Proposta não representa decisão assumida.
3. Evento representa alteração funcional reconhecida.
4. Rejeição de comando não deverá produzir o evento solicitado.
5. Falha técnica não deverá produzir sucesso funcional.
6. Evento somente deverá ser publicado após persistência suficiente.
7. Consumidor não deverá reinterpretar comando como evento.
8. Notificação não deverá substituir evento funcional.
9. Visualização não deverá confirmar execução.
10. Recomendação da Guivos Intelligence deverá permanecer proposta.

# 1801. Imutabilidade histórica

Eventos funcionais reconhecidos não deverão ser reescritos.

Quando houver erro, deverão ser produzidos novos eventos capazes de:

- contestar;
- corrigir;
- compensar;
- reverter efeitos permitidos;
- recompor recortes;
- atualizar consumidores;
- preservar o fato de que a informação anterior existiu.

A imutabilidade não impede exclusão ou anonimização quando houver fundamento legítimo, mas essas operações deverão possuir tratamento próprio e auditável.

# 1802. Princípios dos contratos

## 1802.1 Titularidade

Todo evento deverá possuir titular identificável.

## 1802.2 Autoridade

O ator deverá possuir autoridade para realizar a alteração.

## 1802.3 Temporalidade explícita

Tempo do fato, do conhecimento e do processamento deverão permanecer distintos.

## 1802.4 Proveniência

Origem, fonte e transformações deverão ser preservadas.

## 1802.5 Finalidade

O evento deverá estar associado a finalidade funcional legítima.

## 1802.6 Minimização

O payload deverá conter somente o necessário.

## 1802.7 Idempotência

Reprocessamento não deverá duplicar efeitos.

## 1802.8 Versionamento

Contratos deverão evoluir de forma controlada.

## 1802.9 Explicabilidade

O significado e os efeitos deverão ser reconstruíveis.

## 1802.10 Falha segura

Falhas deverão preservar o último estado válido.

# 1803. Estrutura funcional comum

Todo evento deverá possuir, conforme aplicável:

| Campo | Finalidade |
|---|---|
| `event_id` | Identificador único do evento |
| `event_type` | Tipo funcional reconhecido |
| `schema_version` | Versão do contrato |
| `aggregate_id` | Identificador do Próximo Passo ou agregado |
| `participant_id` | Titular do passo |
| `participant_category` | Pessoa, Organização ou Coletivo |
| `actor_id` | Ator que originou a alteração |
| `actor_role` | Papel funcional do ator |
| `authority` | Escopo de autoridade utilizado |
| `source` | Origem da informação |
| `occurred_at` | Momento funcional do fato |
| `known_at` | Momento em que o fato se tornou conhecido |
| `recognized_at` | Momento de reconhecimento pela capacidade |
| `effective_at` | Momento de aplicação funcional |
| `correlation_id` | Identificador da operação relacionada |
| `causation_id` | Evento ou comando causador |
| `command_id` | Comando que originou o processamento |
| `idempotency_key` | Chave para prevenção de duplicidade |
| `expected_version` | Versão esperada do agregado |
| `purpose` | Finalidade do tratamento |
| `sensitivity` | Classificação de sensibilidade |
| `permissions` | Usos e consumidores autorizados |
| `payload` | Dados específicos do evento |
| `metadata` | Informações técnicas auxiliares |

# 1804. Identidade do agregado

O `aggregate_id` deverá identificar o registro de Próximo Passo ao qual o evento pertence.

Eventos de:

- recorrência;
- ocorrência;
- dependência;
- bloqueio;
- delegação;
- compartilhamento;
- contestação;

poderão possuir identificadores próprios, mantendo relação explícita com o Próximo Passo principal.

# 1805. Categoria do participante

O contrato deverá distinguir:

- Pessoa;
- Organização;
- Coletivo.

A categoria deverá determinar regras de:

- titularidade;
- representação;
- autoridade;
- confirmação;
- responsabilidade;
- compartilhamento;
- contestação;
- retenção.

# 1806. Ator e papel

O evento deverá distinguir, conforme aplicável:

- titular;
- proponente;
- decisor;
- responsável;
- executor;
- apoiador;
- aprovador;
- representante;
- fonte;
- sistema;
- profissional especializado;
- capacidade produtora.

A presença técnica do ator não deverá ampliar sua autoridade funcional.

# 1807. Autoridade

O campo de autoridade deverá registrar:

- tipo de autoridade;
- escopo;
- origem;
- validade;
- participante representado;
- limitações;
- possibilidade de revogação.

Um ator autorizado a informar execução não deverá ser automaticamente autorizado a:

- alterar titularidade;
- definir prioridade pessoal;
- compartilhar conteúdo;
- cancelar o passo;
- concluir objetivo relacionado.

# 1808. Temporalidades

Os contratos deverão distinguir:

- tempo da intenção;
- tempo da proposição;
- tempo da decisão;
- tempo da ativação;
- tempo do início;
- tempo da execução;
- tempo do resultado;
- tempo da conclusão;
- tempo do conhecimento;
- tempo do processamento;
- tempo da aplicação;
- tempo da correção.

# 1809. Temporalidade aproximada e retroativa

Datas aproximadas deverão utilizar:

- intervalo;
- período;
- precisão declarada;
- marcador de incerteza.

Eventos retroativos deverão registrar:

- quando o fato ocorreu;
- quando foi informado;
- quando foi reconhecido;
- quando passou a produzir efeitos no sistema;
- quais decisões anteriores não poderão ser reconstruídas integralmente.

# 1810. Correlação e causalidade funcional

A correlação deverá agrupar eventos pertencentes à mesma operação.

A causalidade deverá indicar qual comando ou evento produziu determinada alteração.

Exemplo:

```text
EventoDeVidaConfirmado
→ ReavaliacaoDeProximosPassosSolicitada
→ PrioridadeDeProximoPassoAlterada
```

A causalidade funcional não deverá representar causalidade humana universal.

# 1811. Versionamento

O `schema_version` deverá permitir:

- evolução compatível;
- identificação de contratos obsoletos;
- transformação controlada;
- coexistência temporária;
- auditoria;
- rejeição segura de versões incompatíveis.

Mudanças de significado deverão exigir nova versão relevante do contrato.

# 1812. Finalidade, sensibilidade e permissões

Todo evento material deverá registrar:

- finalidade;
- sensibilidade;
- consumidores autorizados;
- campos compartilháveis;
- período de uso;
- restrições;
- possibilidade de revogação;
- exigências de retenção.

Eventos sensíveis não deverão circular em barramentos amplos sem minimização.

# 1813. Famílias de eventos

Os contratos serão organizados nas seguintes famílias:

1. identificação e proposição;
2. declaração e confirmação;
3. estrutura e formulação;
4. ativação e prontidão;
5. prioridade e sequenciamento;
6. dependências;
7. bloqueios;
8. temporalidade e agenda;
9. execução e resultados;
10. encerramento;
11. contestação e correção;
12. recorrência;
13. responsabilidades e delegação;
14. compartilhamento e revogação;
15. propagação;
16. visão e interação;
17. falhas e recuperação.

# 1814. `PossivelProximoPassoIdentificado`

Representa que uma possibilidade de movimento foi identificada.

Deverá conter:

- titular;
- origem;
- contexto considerado;
- possível formulação;
- relação com objetivo, evento ou necessidade;
- confiança;
- sensibilidade;
- justificativa.

Não deverá:

- criar compromisso;
- ativar o passo;
- gerar prioridade confirmada;
- atribuir responsabilidade;
- reservar recursos.

# 1815. `ProximoPassoProposto`

Representa uma hipótese formalizada para avaliação.

Deverá conter:

- formulação;
- proponente;
- resultado imediato esperado;
- justificativa;
- alternativas conhecidas;
- dependências principais;
- risco;
- horizonte;
- finalidade;
- nível de confiança.

O evento representa a existência da proposta, não sua aceitação.

# 1816. `PropostaDeProximoPassoRejeitada`

Representa a rejeição de uma proposta.

Deverá conter:

- proposta rejeitada;
- decisor;
- data;
- motivo opcional;
- recorrência permitida ou bloqueada;
- necessidade de arquivamento.

Não deverá produzir penalidade, julgamento ou redução de valor do participante.

# 1817. `ProximoPassoDeclarado`

Representa a declaração direta de intenção ou decisão pelo participante ou autoridade competente.

Deverá preservar:

- expressão original;
- formulação estruturada;
- ator;
- nível de compromisso;
- temporalidade;
- condições;
- incertezas;
- finalidade.

A declaração poderá ainda exigir confirmação quando houver risco ou impacto relevante.

# 1818. `ProximoPassoConfirmado`

Representa que o Próximo Passo foi reconhecido como decisão válida.

Deverá conter:

- formulação confirmada;
- decisor;
- autoridade;
- nível de compromisso;
- condições;
- responsabilidades conhecidas;
- finalidade;
- permissões.

Não deverá significar automaticamente:

- ativação;
- prontidão;
- agendamento;
- início;
- compartilhamento;
- contratação;
- conclusão.

# 1819. `ConfirmacaoDeProximoPassoCondicionada`

Representa confirmação dependente de condição futura.

Deverá conter:

- condição;
- fonte;
- estado da condição;
- forma de verificação;
- validade;
- consequência do atendimento;
- consequência da não ocorrência.

A ativação não deverá ocorrer antes do atendimento da condição.

# 1820. `ProximoPassoConfirmadoParcialmente`

Representa confirmação limitada a:

- parte do passo;
- subpasso;
- período;
- responsabilidade;
- participante;
- recurso;
- finalidade.

A parte não confirmada deverá permanecer explicitamente pendente.

# 1821. `ProximoPassoReformulado`

Representa alteração material da formulação.

Deverá conter:

- formulação anterior;
- nova formulação;
- motivo;
- ator;
- impacto sobre resultado esperado;
- impacto sobre dependências;
- necessidade de nova confirmação;
- versão anterior.

# 1822. `ProximoPassoDesdobrado`

Representa a divisão de um passo em movimentos independentes.

Deverá conter:

- passo original;
- passos derivados;
- critérios de divisão;
- responsabilidades;
- dependências migradas;
- estado residual do original;
- relação histórica.

# 1823. `ProximosPassosUnificados`

Representa a consolidação de registros equivalentes.

Deverá conter:

- passos de origem;
- passo resultante;
- justificativa;
- origens preservadas;
- responsabilidades;
- estados;
- dependências;
- histórico;
- duplicidades evitadas.

# 1824. `ProximoPassoAtivado`

Representa a entrada do passo no portfólio operacional atual.

Deverá conter:

- ator;
- finalidade;
- escopo de ativação;
- horizonte;
- prioridade inicial, quando existente;
- condições;
- capacidade operacional considerada.

Ativação não deverá significar prontidão ou início.

# 1825. `ProntidaoDeProximoPassoAvaliada`

Representa avaliação das condições de início.

O resultado poderá ser:

- pronto;
- parcialmente pronto;
- dependência pendente;
- bloqueado;
- informação insuficiente;
- autorização pendente;
- risco não tratado;
- revisão necessária.

Deverá conter as condições avaliadas e suas fontes.

# 1826. `ProximoPassoPreparado`

Representa que preparações relevantes foram concluídas.

Deverá conter:

- elementos preparados;
- dependências atendidas;
- responsáveis;
- temporalidade;
- evidências;
- prontidão resultante.

Preparação não deverá iniciar automaticamente a execução.

# 1827. `ProximoPassoPriorizado`

Representa atribuição inicial de prioridade operacional.

Deverá conter:

- nível;
- escopo;
- ator;
- fatores considerados;
- origem da prioridade;
- validade;
- possibilidade de revisão.

# 1828. `PrioridadeDeProximoPassoAlterada`

Representa mudança na prioridade.

Deverá conter:

- prioridade anterior;
- nova prioridade;
- motivo;
- ator;
- escopo;
- fatores considerados;
- impactos sobre outros passos.

Receita, patrocínio ou comissão não poderão constituir fator funcional.

# 1829. `SequenciaDeProximosPassosDefinida`

Representa estabelecimento de relação sequencial.

A relação poderá ser:

- anterior;
- posterior;
- paralela;
- alternativa;
- condicional;
- preparatória;
- confirmatória;
- substitutiva;
- recorrente.

Deverá conter justificativa e possibilidade de revisão.

# 1830. `DependenciaDeProximoPassoRegistrada`

Representa a criação de uma dependência.

Deverá conter:

- tipo;
- descrição;
- criticidade;
- origem;
- responsável possível;
- estado;
- temporalidade;
- forma de resolução;
- evidências;
- sensibilidade.

# 1831. `DependenciaDeProximoPassoAtendida`

Representa que determinada condição necessária foi satisfeita.

Deverá indicar:

- dependência;
- forma de atendimento;
- fonte;
- autoridade;
- temporalidade;
- evidência;
- efeitos possíveis sobre prontidão e bloqueios.

# 1832. `DependenciaDeProximoPassoDispensada`

Representa que a dependência deixou de ser necessária.

Deverá conter:

- autoridade;
- motivo;
- alternativa;
- efeitos;
- risco residual;
- possibilidade de contestação.

# 1833. `ProximoPassoBloqueado`

Representa impedimento atual à continuidade.

Deverá conter:

- bloqueio;
- origem;
- criticidade;
- impacto;
- condição de resolução;
- responsável possível;
- revisão prevista;
- alternativas;
- sensibilidade.

# 1834. `ProximoPassoDesbloqueado`

Representa que o impedimento deixou de inviabilizar a continuidade.

Deverá indicar:

- bloqueio resolvido;
- forma de resolução;
- ator;
- evidência;
- prontidão resultante;
- necessidade de nova confirmação.

O desbloqueio não deverá iniciar automaticamente o passo.

# 1835. `ProximoPassoPausado`

Representa interrupção deliberada e temporária.

Deverá conter:

- ator;
- motivo opcional;
- início da pausa;
- condição ou data de revisão;
- efeitos sobre notificações;
- efeitos sobre recorrência;
- compartilhamentos afetados.

# 1836. `ProximoPassoRetomado`

Representa retomada após pausa.

Deverá conter nova avaliação de:

- atualidade;
- formulação;
- prioridade;
- prontidão;
- dependências;
- bloqueios;
- risco;
- responsabilidade;
- temporalidade.

# 1837. `ProximoPassoAgendado`

Representa definição confirmada de temporalidade operacional.

Deverá conter:

- data, janela ou condição;
- ator;
- nível de compromisso;
- origem;
- fuso;
- recorrência;
- vínculo externo, quando existente.

# 1838. `AgendamentoDeProximoPassoAlterado`

Representa modificação de data, janela ou compromisso.

Deverá preservar:

- valor anterior;
- novo valor;
- ator;
- motivo opcional;
- dependências afetadas;
- participantes informados;
- integração externa.

# 1839. `ProximoPassoAdiado`

Representa deslocamento deliberado da realização para momento posterior.

Deverá conter:

- temporalidade anterior;
- nova temporalidade ou condição;
- impacto;
- necessidade de revisão;
- ator;
- nível de compromisso.

Adiamento não deverá ser interpretado como desinteresse.

# 1840. `ProximoPassoIniciado`

Representa início reconhecido da execução.

Deverá conter:

- executor;
- forma de reconhecimento;
- temporalidade;
- fonte;
- autoridade;
- parte iniciada;
- evidência, quando necessária.

Visualização, clique ou consumo de conteúdo não deverão produzir esse evento isoladamente.

# 1841. `ProximoPassoAtualizado`

Representa alteração relevante durante a execução.

Poderá atualizar:

- formulação;
- escopo;
- responsabilidade;
- temporalidade;
- dependência;
- bloqueio;
- esforço;
- risco;
- resultado parcial;
- estado da informação.

Alterações materiais poderão exigir nova confirmação.

# 1842. `ResultadoDeProximoPassoRegistrado`

Representa consequência observada ou declarada da execução.

O resultado poderá ser:

- alcançado;
- parcialmente alcançado;
- não alcançado;
- diferente do esperado;
- desconhecido;
- contestado;
- não aplicável.

Resultado não deverá representar progresso automático do objetivo.

# 1843. `ProximoPassoConcluido`

Representa reconhecimento de que o movimento delimitado foi realizado.

Deverá conter:

- responsável pelo reconhecimento;
- autoridade;
- temporalidade;
- resultado imediato;
- evidências;
- partes componentes;
- dependências liberadas;
- consumidores a serem notificados.

# 1844. `ProximoPassoConcluidoParcialmente`

Representa conclusão de parte de um passo composto.

Deverá conter:

- partes concluídas;
- partes pendentes;
- resultado parcial;
- decisão sobre desdobramento;
- responsabilidades;
- impacto sobre o estado global.

# 1845. `ProximoPassoCancelado`

Representa decisão de não prosseguir.

Deverá conter:

- ator;
- autoridade;
- motivo opcional;
- compromissos afetados;
- dependências;
- recursos;
- compartilhamentos;
- resultados preservados.

Cancelamento não deverá representar fracasso.

# 1846. `ProximoPassoSubstituido`

Representa que outro passo passou a cumprir sua função.

Deverá conter:

- passo anterior;
- passo substituto;
- motivo;
- dependências migradas;
- responsabilidades;
- resultados anteriores;
- temporalidade;
- histórico.

# 1847. `ProximoPassoExpirado`

Representa perda de atualidade, janela ou validade funcional.

Deverá conter:

- regra;
- fonte;
- momento;
- motivo;
- possibilidade de reabertura;
- alternativas;
- possibilidade de contestação.

Expiração não deverá ser confundida com cancelamento.

# 1848. `ProximoPassoContestado`

Representa questionamento sobre:

- formulação;
- titularidade;
- responsabilidade;
- prioridade;
- estado;
- temporalidade;
- bloqueio;
- resultado;
- conclusão;
- cancelamento;
- expiração;
- compartilhamento.

Deverá limitar efeitos críticos quando necessário.

# 1849. `ContestacaoDeProximoPassoResolvida`

Representa resultado da análise da contestação.

Poderá resultar em:

- manutenção;
- correção;
- reformulação;
- mudança de estado;
- substituição;
- cancelamento;
- reabertura;
- remoção de responsabilidade;
- divergência não resolvida.

# 1850. `ProximoPassoCorrigido`

Representa correção compensatória de informação anterior.

Deverá conter:

- campo ou significado corrigido;
- valor anterior;
- novo valor;
- motivo;
- ator;
- autoridade;
- eventos afetados;
- recortes recompostos;
- consumidores notificados.

# 1851. `ProximoPassoReaberto`

Representa retomada de passo anteriormente encerrado.

Deverá conter:

- estado anterior;
- motivo;
- ator;
- nova temporalidade;
- contexto atual;
- dependências;
- necessidade de nova confirmação;
- distinção entre continuidade e novo ciclo.

# 1852. `ProximoPassoArquivado`

Representa retirada do passo da operação cotidiana.

Deverá preservar:

- histórico;
- estados;
- resultados;
- evidências;
- relações;
- compartilhamentos legítimos;
- possibilidade de consulta;
- possibilidade de reabertura.

# 1853. `RecorrenciaDeProximoPassoCriada`

Representa criação de repetição operacional.

Deverá conter:

- frequência;
- período;
- unidade de ocorrência;
- condição de pausa;
- condição de encerramento;
- forma de conclusão;
- tolerância;
- responsável.

# 1854. `OcorrenciaDeProximoPassoRegistrada`

Representa uma ocorrência individual da recorrência.

Deverá conter:

- recorrência;
- data;
- estado;
- executor;
- resultado;
- evidência;
- correção ou contestação;
- relação com outras ocorrências.

# 1855. `OcorrenciaDeProximoPassoNaoRealizadaClassificada`

Representa classificação operacional de ocorrência não realizada.

Poderá ser:

- adiada;
- dispensada;
- cancelada;
- bloqueada;
- não aplicável;
- perdida;
- desconhecida.

Não deverá produzir julgamento de disciplina, mérito ou evolução.

# 1856. `RecorrenciaDeProximoPassoPausada`

Representa suspensão temporária de novas ocorrências.

Deverá conter:

- início;
- ator;
- condição de retomada;
- notificações suspensas;
- regra sobre ocorrências futuras;
- histórico preservado.

# 1857. `RecorrenciaDeProximoPassoEncerrada`

Representa finalização da recorrência.

Poderá ocorrer por:

- período concluído;
- quantidade alcançada;
- condição atingida;
- decisão;
- substituição;
- perda de necessidade;
- Evento de Vida;
- risco;
- encerramento de obrigação.

# 1858. `ResponsabilidadeDeProximoPassoDelegada`

Representa proposta ou efetivação de delegação.

Deverá conter:

- delegante;
- executor proposto;
- escopo;
- autoridade;
- prazo;
- permissões;
- responsabilidade residual;
- possibilidade de rejeição.

# 1859. `DelegacaoDeProximoPassoAceita`

Representa que o executor assumiu o escopo delegado.

Deverá conter:

- executor;
- escopo aceito;
- temporalidade;
- condições;
- prazo;
- limitações;
- permissões.

# 1860. `DelegacaoDeProximoPassoRejeitada`

Representa que a responsabilidade proposta não foi assumida.

A rejeição não deverá criar responsabilidade residual indevida para o executor proposto.

# 1861. `CompartilhamentoDeProximoPassoAutorizado`

Representa autorização para compartilhar recorte específico.

Deverá conter:

- consumidor;
- finalidade;
- campos;
- período;
- sensibilidade;
- possibilidade de redistribuição;
- condição de revogação;
- ator autorizador.

# 1862. `CompartilhamentoDeProximoPassoRevogado`

Representa interrupção de novos acessos e usos autorizáveis.

Deverá conter:

- compartilhamento;
- ator;
- momento;
- consumidores afetados;
- obrigações preservadas;
- propagação necessária;
- pendências.

# 1863. Propagação da revogação

A propagação deverá utilizar:

- `PropagacaoDeRevogacaoDeProximoPassoIniciada`;
- `PropagacaoDeRevogacaoDeProximoPassoConcluida`.

A conclusão somente deverá ser reconhecida quando os consumidores necessários confirmarem o processamento.

# 1864. Produção e propagação de recortes

Poderão ser utilizados:

- `RecorteDeProximoPassoProduzido`;
- `RecorteDeProximoPassoPropagado`;
- `ProcessamentoDeRecorteDeProximoPassoConfirmado`.

O recorte deverá conter somente os campos necessários à finalidade do consumidor.

# 1865. Reavaliações dependentes

A capacidade poderá produzir:

- `ReavaliacaoDependenteDeProximoPassoSolicitada`;
- `ReavaliacaoDependenteDeProximoPassoIniciada`;
- `ReavaliacaoDependenteDeProximoPassoConcluida`.

A solicitação não deverá determinar a decisão da capacidade consumidora.

# 1866. Eventos produzidos pela visão

A superfície `Meus Próximos Passos` poderá originar comandos e eventos referentes a:

- consulta;
- confirmação;
- rejeição;
- reformulação;
- prioridade;
- agendamento;
- início;
- resultado;
- conclusão;
- cancelamento;
- contestação;
- correção;
- arquivamento;
- reabertura;
- delegação;
- compartilhamento.

O canal visual não deverá possuir contratos semânticos próprios divergentes.

# 1867. Eventos conversacionais

Canais conversacionais poderão produzir os mesmos contratos funcionais.

A conversa deverá distinguir:

- pergunta;
- interpretação;
- proposta;
- confirmação;
- comando;
- evento reconhecido;
- resposta informativa.

Linguagem ambígua deverá gerar esclarecimento proporcional.

# 1868. Eventos de leitura e interação

Eventos como:

- tela acessada;
- cartão visualizado;
- explicação consultada;
- proposta aberta;
- notificação dispensada;

poderão existir para observabilidade da experiência.

Eles não deverão alterar automaticamente:

- confirmação;
- prioridade;
- início;
- resultado;
- conclusão;
- responsabilidade;
- compartilhamento.

# 1869. Eventos compostos

Operações como:

- substituir um passo;
- corrigir conclusão;
- revogar compartilhamento;
- unificar registros;
- desdobrar passo composto;

poderão produzir múltiplos eventos atômicos relacionados pela mesma correlação.

# 1870. Atomicidade funcional

Uma operação deverá ser considerada funcionalmente concluída somente quando seus efeitos mínimos obrigatórios forem aplicados.

Exemplo de substituição:

```text
novo passo criado
→ passo anterior marcado como substituído
→ relação registrada
→ dependências revisadas
→ recortes recompostos
```

Falha em etapa crítica deverá manter a operação pendente ou compensá-la.

# 1871. Eventos pendentes

O sistema poderá registrar estado operacional pendente quando:

- persistência principal ocorreu;
- propagação não terminou;
- integração externa está indisponível;
- confirmação adicional é necessária;
- consumidor ainda não respondeu.

Pendente não deverá ser apresentado como concluído.

# 1872. Idempotência

A mesma solicitação não deverá produzir novamente:

- Próximo Passo;
- confirmação;
- ativação;
- prioridade;
- dependência;
- bloqueio;
- agendamento;
- início;
- conclusão;
- cancelamento;
- notificação;
- responsabilidade;
- compartilhamento.

# 1873. Duplicidade semântica

Eventos diferentes tecnicamente poderão representar o mesmo fato.

A detecção deverá considerar:

- titular;
- tipo;
- agregado;
- finalidade;
- temporalidade;
- ator;
- origem;
- payload;
- correlação;
- versão.

A igualdade textual isolada não será suficiente.

# 1874. Ordenação

Os contratos deverão permitir distinguir:

- ordem da decisão;
- ordem do fato;
- ordem do conhecimento;
- ordem de publicação;
- ordem de processamento;
- ordem de aplicação;
- ordem de propagação.

# 1875. Eventos fora de ordem

Quando um evento chegar fora de ordem, o consumidor deverá:

- verificar versão;
- verificar dependências;
- aguardar eventos anteriores;
- reconciliar estado;
- rejeitar aplicação incompatível;
- registrar pendência;
- evitar estado impossível.

# 1876. Concorrência

Alterações simultâneas deverão ser tratadas por:

- versão esperada;
- comparação de estado;
- identificação de atores;
- autoridade;
- temporalidade;
- conflito explícito;
- resolução assistida;
- preservação de versões.

# 1877. Versão esperada

Comandos materiais deverão informar `expected_version` quando necessário.

Se a versão não corresponder, o sistema deverá:

- rejeitar aplicação silenciosa;
- retornar conflito;
- apresentar estado atual;
- permitir nova decisão;
- preservar tentativa para auditoria.

# 1878. Correção compensatória

Uma correção não deverá alterar eventos anteriores.

Ela deverá produzir sequência capaz de:

```text
identificar erro
→ limitar efeitos
→ registrar correção
→ recompor estado
→ recompor recortes
→ notificar consumidores
→ confirmar processamento
```

# 1879. Exclusão e anonimização

Exclusão ou anonimização deverá distinguir:

- remoção da operação cotidiana;
- arquivamento;
- retirada de compartilhamento;
- anonimização de terceiros;
- exclusão de conteúdo;
- retenção legítima;
- preservação de auditoria mínima.

A operação deverá produzir evento auditável compatível com finalidade, legislação e governança.

# 1880. Retenção

A retenção deverá considerar:

- estado;
- finalidade;
- sensibilidade;
- titularidade;
- obrigação legítima;
- dependências;
- contestação;
- auditoria;
- revogação;
- exclusão aplicável.

Propostas rejeitadas poderão possuir retenção reduzida.

# 1881. Logs

Logs deverão conter somente o necessário para:

- rastreamento;
- diagnóstico;
- segurança;
- auditoria;
- recuperação;
- prevenção de duplicidade.

Narrativas pessoais sensíveis não deverão ser copiadas integralmente para logs técnicos.

# 1882. Falhas de processamento

Falhas poderão ocorrer em:

- validação;
- persistência;
- publicação;
- consumo;
- transformação;
- autorização;
- sincronização;
- integração;
- propagação;
- revogação;
- auditoria.

# 1883. `ProcessamentoDeEventoDeProximoPassoFalhou`

Deverá conter:

- evento;
- etapa;
- erro classificado;
- tentativa;
- estado anterior;
- efeitos aplicados;
- efeitos pendentes;
- possibilidade de repetição;
- necessidade de compensação;
- sensibilidade.

# 1884. `PropagacaoDeProximoPassoFalhou`

Deverá registrar:

- recorte;
- consumidor;
- finalidade;
- tentativa;
- erro;
- última confirmação;
- impacto funcional;
- próxima ação;
- estado pendente.

# 1885. Falha segura

Em caso de falha, a capacidade deverá:

- preservar último estado válido;
- evitar falsa confirmação;
- evitar falsa conclusão;
- evitar duplicidade;
- limitar automações;
- manter pendências visíveis;
- permitir recuperação;
- informar o participante quando relevante;
- preservar auditoria.

# 1886. Recuperação

A recuperação poderá utilizar:

- repetição idempotente;
- retomada de fila;
- reprocessamento controlado;
- reconstrução de projeção;
- compensação;
- correção;
- reconciliação;
- intervenção manual.

A recuperação não deverá alterar silenciosamente fatos históricos.

# 1887. Responsabilidades dos produtores

Produtores deverão:

1. validar identidade;
2. validar autoridade;
3. distinguir comando e evento;
4. utilizar contrato vigente;
5. registrar temporalidade;
6. preservar proveniência;
7. aplicar minimização;
8. gerar chave de idempotência;
9. informar correlação;
10. classificar sensibilidade;
11. persistir antes de publicar;
12. registrar falhas;
13. não declarar sucesso prematuramente.

# 1888. Responsabilidades dos consumidores

Consumidores deverão:

1. validar versão;
2. validar finalidade;
3. respeitar permissões;
4. aplicar idempotência;
5. preservar ordenação;
6. não ampliar significado;
7. não transferir decisão;
8. processar revogações;
9. registrar resultado;
10. confirmar processamento real;
11. tratar falhas;
12. limitar retenção;
13. preservar auditoria.

# 1889. Relação com Contexto Vivo

Eventos de Próximos Passos poderão solicitar atualização contextual quando houver:

- nova capacidade;
- nova restrição;
- mudança de disponibilidade;
- resultado relevante;
- alteração de responsabilidade;
- condição externa;
- preferência declarada.

O Contexto Vivo deverá governar a admissão da atualização.

# 1890. Relação com Objetivos

Poderão ser produzidos recortes sobre:

- execução;
- resultado;
- evidência;
- bloqueio;
- dependência;
- conclusão;
- cancelamento;
- necessidade de revisão.

Objetivos deverá avaliar progresso, critérios e conclusão por seus próprios contratos.

# 1891. Relação com Eventos de Vida

A capacidade poderá informar:

- mudança relevante identificada durante a execução;
- transição potencial;
- resultado com possível significado de Evento de Vida;
- alteração de condição contextual.

Próximo Passo concluído não deverá criar automaticamente Evento de Vida.

# 1892. Relação com Oportunidades Ativas

A capacidade poderá solicitar:

- meio compatível;
- serviço;
- recurso;
- pessoa;
- organização;
- experiência;
- produto;
- conteúdo.

A oportunidade deverá permanecer distinta do passo e não poderá alterar sua prioridade por interesse comercial.

# 1893. Relação com Intervenções Contextuais

Eventos poderão informar:

- decisão pendente;
- prazo real;
- bloqueio;
- dependência;
- necessidade de confirmação;
- risco;
- fadiga;
- sensibilidade;
- sincronização pendente.

Intervenções deverá decidir agir, perguntar, lembrar, esperar ou silenciar.

# 1894. Relação com Experiências

A execução poderá produzir:

- experiência planejada;
- experiência iniciada;
- participação concluída;
- resultado;
- evidência;
- abandono legítimo;
- mudança de contexto.

Experiências deverá governar a vivência por contrato próprio.

# 1895. Relação com Evolução Contínua

Eventos poderão fornecer:

- resultados;
- evidências;
- mudanças de capacidade;
- adaptações;
- padrões;
- transições;
- aprendizados.

Quantidade de eventos ou passos concluídos não deverá medir evolução humana.

# 1896. Guivos Intelligence

A Guivos Intelligence poderá consumir eventos para:

- sugerir alternativas;
- identificar dependências;
- detectar duplicidades;
- estimar esforço;
- explicar prioridade;
- identificar revisão;
- apoiar organização;
- reduzir fadiga;
- produzir resumo.

Ela não deverá transformar esses eventos em:

- avaliação de mérito;
- pontuação de produtividade;
- compromisso automático;
- diagnóstico;
- prioridade imposta;
- publicidade baseada em vulnerabilidade.

# 1897. Platform Layer

A Platform Layer deverá sustentar:

- armazenamento de eventos;
- publicação;
- filas;
- idempotência;
- versionamento;
- autorização;
- criptografia;
- observabilidade;
- busca;
- auditoria;
- retenção;
- exclusão;
- reconstrução de projeções.

Ela não deverá redefinir o significado dos eventos.

# 1898. Eventos de Pessoa

Eventos pessoais deverão preservar:

- autonomia;
- decisão individual;
- privacidade;
- sensibilidade;
- liberdade de rejeição;
- ausência de cobrança;
- controle de compartilhamento.

# 1899. Eventos de Organização

Eventos organizacionais poderão representar:

- passos institucionais;
- processos;
- responsabilidades;
- aprovações;
- delegações;
- obrigações;
- resultados operacionais.

A Organização não deverá utilizar esses contratos para governar integralmente a jornada pessoal de colaboradores.

# 1900. Eventos de Coletivo

Eventos coletivos deverão respeitar:

- governança declarada;
- autoridade;
- representação;
- decisão coletiva;
- papéis;
- saída de participantes;
- conteúdo privado;
- divergências.

# 1901. Passos compartilhados

Eventos compartilhados deverão distinguir:

- estado global;
- estados individuais;
- responsabilidades;
- confirmações;
- decisões;
- execuções;
- permissões;
- contestações.

Nenhum participante deverá assumir responsabilidade por silêncio.

# 1902. Informações de terceiros

Os contratos deverão:

- minimizar identificação;
- evitar perfil próprio;
- limitar narrativa;
- proteger sensibilidade;
- impedir propagação desnecessária;
- permitir anonimização;
- manter somente o necessário ao passo do titular.

# 1903. Explicabilidade

Deverá ser possível explicar:

- qual comando foi recebido;
- quem o enviou;
- qual autoridade foi utilizada;
- qual validação ocorreu;
- qual evento foi produzido;
- qual estado mudou;
- quais recortes foram enviados;
- quais consumidores processaram;
- quais falhas ocorreram;
- quais correções ou revogações foram aplicadas.

# 1904. Auditoria

A auditoria deverá reconstruir:

```text
entrada
→ comando
→ identidade
→ autoridade
→ validação
→ decisão
→ evento
→ atualização do agregado
→ recortes
→ consumidores
→ processamento
→ correções, falhas ou revogações
```

# 1905. Eventos funcionalmente proibidos

Não deverão existir eventos que representem:

- passo pessoal confirmado por inferência comportamental;
- responsabilidade atribuída por silêncio;
- início por visualização;
- conclusão por clique;
- progresso de objetivo pela conclusão isolada de passo;
- falha pessoal por prazo vencido;
- incapacidade por bloqueio;
- fracasso por pausa ou cancelamento;
- hábito por recorrência;
- evolução por volume de passos;
- prioridade definida por patrocínio;
- publicidade baseada em passo sensível;
- compromisso criado por recomendação;
- compartilhamento irrestrito;
- revogação concluída sem propagação;
- sucesso integral diante de falha parcial.

# 1906. Métricas funcionais dos contratos

Os contratos poderão ser avaliados por:

- eventos processados;
- eventos rejeitados;
- comandos inválidos;
- duplicidades bloqueadas;
- efeitos duplicados;
- conflitos de versão;
- eventos fora de ordem;
- falhas de propagação;
- tempo de processamento;
- compensações;
- correções;
- contestações;
- revogações pendentes;
- usos após revogação;
- eventos sensíveis expostos;
- reconstruções bem-sucedidas;
- consumidores sem confirmação;
- falhas recuperadas.

As métricas deverão avaliar o sistema, não o participante.

# 1907. Critérios funcionais de aceite

Os contratos serão considerados adequadamente definidos quando:

1. distinguirem comando, proposta e evento;
2. preservarem imutabilidade histórica;
3. utilizarem correção compensatória;
4. possuírem estrutura comum;
5. identificarem agregado e titular;
6. distinguirem ator e autoridade;
7. preservarem temporalidades;
8. suportarem retroatividade;
9. possuírem correlação e causalidade;
10. forem versionados;
11. registrarem finalidade e sensibilidade;
12. cobrirem identificação e proposição;
13. cobrirem confirmação simples, condicionada e parcial;
14. cobrirem reformulação, divisão e unificação;
15. cobrirem ativação e prontidão;
16. cobrirem prioridade e sequência;
17. cobrirem dependências e bloqueios;
18. cobrirem agenda, início e execução;
19. separarem resultado, progresso e conclusão;
20. cobrirem cancelamento, substituição e expiração;
21. permitirem contestação, correção e reabertura;
22. suportarem recorrência;
23. suportarem delegação e passos compartilhados;
24. governarem compartilhamento e revogação;
25. produzirem recortes mínimos;
26. aplicarem idempotência;
27. tratarem ordenação e concorrência;
28. operarem com falha segura;
29. preservarem explicabilidade e auditoria;
30. manterem o participante no controle.

# 1908. Regras fundamentais dos eventos funcionais

1. Comando não representa fato.
2. Proposta não representa decisão.
3. Evento representa fato reconhecido.
4. Evento somente deverá ser publicado após persistência suficiente.
5. Eventos históricos não deverão ser reescritos.
6. Correções deverão ser compensatórias.
7. Titular e ator deverão permanecer distintos.
8. A autoridade deverá ser explícita.
9. Acesso técnico não representa autoridade.
10. Tempo do fato e tempo do processamento deverão permanecer separados.
11. Eventos retroativos deverão preservar limites de reconstrução.
12. Correlação não representa causalidade humana universal.
13. Contratos deverão ser versionados.
14. Finalidade deverá limitar o uso.
15. Sensibilidade deverá limitar exposição.
16. Possibilidade não deverá criar compromisso.
17. Proposta rejeitada não gera penalidade.
18. Confirmação não significa ativação.
19. Ativação não significa prontidão.
20. Prontidão não significa início.
21. Agendamento não significa execução.
22. Execução não significa resultado esperado.
23. Resultado não significa progresso.
24. Conclusão do passo não conclui o objetivo.
25. Prioridade deverá permanecer explicável.
26. Receita não deverá alterar prioridade.
27. Dependência atendida não inicia automaticamente o passo.
28. Desbloqueio não inicia automaticamente a execução.
29. Pausa não representa fracasso.
30. Cancelamento não representa valor pessoal.
31. Expiração não equivale a cancelamento.
32. Contestação deverá limitar efeitos críticos.
33. Reabertura deverá distinguir continuidade de novo ciclo.
34. Recorrência não comprova hábito.
35. Ocorrência não realizada não mede disciplina.
36. Delegação não transfere titularidade.
37. Responsabilidade não surge por silêncio.
38. Compartilhamento exige finalidade.
39. Revogação interrompe novos usos.
40. Revogação somente é concluída após propagação efetiva.
41. Reprocessamento não deverá duplicar efeitos.
42. Eventos fora de ordem não deverão criar estados impossíveis.
43. Alterações concorrentes não deverão ser sobrescritas.
44. Falha parcial não equivale a sucesso integral.
45. Logs deverão minimizar conteúdo sensível.
46. Consumidores não deverão ampliar significado.
47. Capacidades consumidoras deverão governar suas próprias decisões.
48. Guivos Intelligence produz hipóteses e explicações, não fatos pessoais não confirmados.
49. Platform Layer sustenta contratos, mas não redefine semântica.
50. Eventos deverão apoiar ação real, não vigilância ou engajamento artificial.
51. As métricas deverão avaliar o sistema.
52. O participante permanece no controle.

# 1909. Continuidade normativa

`PAS-001-PP-EVENT-001 1.0.0` deverá ser registrado como a **quarta extensão normativa da Capacidade 05 — Próximos Passos**.

Ele deverá:

- consolidar os contratos dos eventos funcionais da capacidade;
- preservar a autoridade de `PAS-001-PP-FOUNDATION-001 1.0.0`;
- preservar a autoridade de `PAS-001-PP-LIFECYCLE-001 1.0.0`;
- preservar a autoridade de `PAS-001-PP-VIEW-001 1.0.0`;
- manter a Capacidade 05 no estado `In progress`;
- elevar o progresso editorial de referência para `80%`;
- preservar as Capacidades 02, 03 e 04 como `Functionally complete`;
- manter comandos, propostas e eventos reconhecidos como conceitos distintos;
- manter confirmação, ativação, prontidão, execução, resultado, progresso e conclusão como dimensões independentes.

Com isso, ficam definidos os **contratos dos eventos funcionais da Capacidade de Próximos Passos**, incluindo criação, confirmação, ativação, prontidão, prioridade, dependências, bloqueios, execução, resultados, conclusão, cancelamento, substituição, expiração, contestação, correção, recorrência, responsabilidades, compartilhamento, propagação, idempotência, ordenação, versionamento, auditoria e falha segura.

O próximo bloco deverá consolidar:

> **as integrações funcionais da Capacidade de Próximos Passos com Captura de Contexto, Contexto Vivo, Objetivos, Eventos de Vida, Oportunidades Ativas, Intervenções Contextuais, Experiências, Evolução Contínua, Guivos Intelligence, Platform Layer, produtos especializados, organizações, serviços profissionais e fontes externas.**