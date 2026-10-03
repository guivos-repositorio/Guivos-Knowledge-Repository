---
id: PAS-001-CV-CONFLICT-001
title: Resolução de Conflitos do Contexto Vivo
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-13
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-CV-STATE-001
  - PAS-001-CV-UPDATE-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-CV-CONFLICT-001 — Resolução de Conflitos do Contexto Vivo

## 1. Autoridade e vínculo

Este documento é uma **extensão normativa** do `PAS-001 — Guivos Journey Product Architecture Specification`, vinculada à `Capacidade 02 — Contexto Vivo`.

Seu conteúdo deve ser lido como continuidade funcional das seções 28 a 45 do `PAS-001 0.5.0`, das seções 46 a 59 do `PAS-001-CV-STATE-001 1.0.0` e das seções 60 a 83 do `PAS-001-CV-UPDATE-001 1.0.0`.

A separação documental preserva legibilidade e modularidade sem reduzir sua autoridade arquitetural.

# 84. Resolução detalhada de conflitos no Contexto Vivo

Um conflito ocorre quando duas ou mais informações, interpretações, evidências, permissões ou referências temporais não podem orientar simultaneamente a mesma decisão sem risco de erro, ambiguidade ou uso inadequado.

Conflito não significa necessariamente que uma das informações seja falsa.

Ele poderá indicar:

- mudança real ao longo do tempo;
- contextos diferentes;
- interpretações incompatíveis;
- fontes com alcances distintos;
- informação incorreta;
- ausência de referência temporal;
- divergência entre observação e autodeclaração;
- diferença entre intenção e comportamento;
- limitação de permissão;
- coexistência legítima ainda não compreendida.

> O Contexto Vivo deverá preservar o conflito até possuir base suficiente para explicá-lo, contextualizá-lo ou resolvê-lo.

# 85. Princípios da resolução de conflitos

## 85.1 Não resolução silenciosa

O sistema não deverá escolher automaticamente uma versão e ocultar as demais quando o conflito puder afetar:

- objetivos;
- oportunidades;
- restrições;
- identidade;
- informações sensíveis;
- compartilhamento;
- decisões relevantes;
- interpretação da evolução.

## 85.2 Preservação da proveniência

Cada informação conflitante deverá manter:

- origem;
- autor ou sistema;
- data do fato;
- data de registro;
- contexto de ocorrência;
- finalidade;
- permissão;
- confiança;
- evidências relacionadas;
- confirmações ou contestações.

## 85.3 Prioridade do participante

Declarações atuais e explícitas do participante deverão prevalecer funcionalmente sobre inferências incompatíveis.

Essa prioridade não significa apagar observações ou registros históricos.

Exemplo:

```text
Integração: atividade de corrida registrada
Participante: “Eu não pratico corrida; apenas acompanhei outra pessoa.”
```

Resultado:

- a atividade observada permanece no histórico;
- a preferência por corrida não deverá ser criada;
- eventual inferência anterior deverá ser retirada ou contestada.

## 85.4 Separação entre fato e interpretação

O sistema deverá diferenciar:

```text
Participante visualizou dez cursos de programação
```

de:

```text
Participante deseja mudar de carreira para tecnologia
```

O primeiro é um comportamento observado.
O segundo é uma interpretação que poderá ser conflitante com uma declaração explícita.

## 85.5 Temporalidade antes de contradição

Antes de classificar duas informações como contraditórias, o sistema deverá verificar se elas representam momentos diferentes.

Exemplo:

```text
Janeiro: participante mora em Belo Horizonte
Julho: participante mora em Lisboa
```

Essas informações não são necessariamente conflitantes. Elas poderão representar uma mudança real.

## 85.6 Contextualidade antes de generalização

Preferências, capacidades, restrições e relacionamentos poderão variar conforme a situação.

Exemplo:

> O participante prefere atividades online para estudos e presenciais para esportes.

As duas preferências podem coexistir legitimamente.

## 85.7 Proporcionalidade

O esforço de resolução deverá ser proporcional ao impacto do conflito.

Conflitos sem efeito sobre a experiência atual poderão permanecer registrados para revisão futura.

# 86. Tipos funcionais de conflito

## 86.1 Conflito direto

Duas informações afirmam condições incompatíveis para o mesmo elemento, no mesmo período e contexto.

Exemplo:

```text
Disponibilidade: sábado pela manhã
Disponibilidade: sábado indisponível
```

## 86.2 Conflito temporal

As informações poderão ser verdadeiras, mas não está claro qual representa o momento atual.

Exemplo:

```text
Objetivo: concluir graduação
Objetivo: interromper temporariamente os estudos
```

## 86.3 Conflito contextual

Duas informações aparentam divergência porque seus contextos de aplicação não foram diferenciados.

Exemplo:

```text
Prefere atividades individuais
Prefere atividades coletivas
```

Após contextualização:

- atividade física: coletiva;
- estudos: individual.

## 86.4 Conflito entre declaração e comportamento

O participante declara uma preferência, mas o comportamento observado parece diferente.

Exemplo:

- declarou preferência por experiências presenciais;
- passou a participar apenas de atividades online.

O comportamento não deverá substituir automaticamente a declaração.

## 86.5 Conflito entre fontes

Duas fontes autorizadas fornecem informações incompatíveis.

Exemplo:

- calendário indica disponibilidade;
- agenda profissional indica compromisso no mesmo horário.

## 86.6 Conflito entre fato e inferência

Uma inferência entra em divergência com uma informação declarada ou comprovada.

Exemplo:

- inferência: possível busca por novo emprego;
- declaração: deseja permanecer no trabalho atual.

## 86.7 Conflito semântico

Duas informações utilizam termos diferentes que poderão representar o mesmo conceito ou conceitos distintos.

Exemplo:

- “trabalho autônomo”;
- “empreendedorismo”;
- “prestação de serviços”;
- “projeto próprio”.

O sistema deverá evitar unificação sem compreender o significado atribuído pelo participante.

## 86.8 Conflito de granularidade

Uma informação ampla entra em tensão com outra mais específica.

Exemplo:

```text
Disponibilidade: finais de semana
Disponibilidade: domingo à tarde indisponível
```

A informação específica poderá complementar a ampla, em vez de substituí-la.

## 86.9 Conflito entre dimensões

Elementos de dimensões diferentes criam tensão funcional.

Exemplo:

- Direção: iniciar pós-graduação;
- Restrições: ausência de disponibilidade durante a semana;
- Preferências: somente atividades presenciais.

Não existe necessariamente erro. Existe uma condição que precisa ser considerada na construção de caminhos possíveis.

## 86.10 Conflito de permissão

Uma informação é válida, mas seu uso está autorizado para uma finalidade e proibido para outra.

Exemplo:

- localização permitida para eventos;
- localização proibida para publicidade.

## 86.11 Conflito de sensibilidade

Uma fonte fornece informação sensível que o participante não confirmou ou não autorizou para persistência.

## 86.12 Conflito de evolução

Diferentes evidências sugerem resultados incompatíveis.

Exemplo:

- curso concluído;
- participante relata não ter desenvolvido a competência esperada.

Conclusão da experiência e evolução percebida deverão permanecer distintas.

# 87. Registro funcional de um conflito

Todo conflito relevante deverá possuir um registro próprio.

| Atributo | Finalidade |
|---|---|
| Identificador | Distinguir o conflito |
| Elementos envolvidos | Indicar as informações em tensão |
| Tipo de conflito | Classificar sua natureza |
| Dimensões afetadas | Limitar a análise |
| Contexto | Explicar onde a divergência ocorre |
| Período | Identificar a referência temporal |
| Fontes | Preservar proveniência |
| Impacto potencial | Avaliar risco de utilização |
| Sensibilidade | Determinar controles |
| Estado do conflito | Indicar sua condição atual |
| Ação necessária | Definir confirmação, revisão ou observação |
| Decisões afetadas | Identificar recomendações ou ações dependentes |
| Resultado | Registrar como foi tratado |
| Explicação | Permitir compreensão pelo participante |
| Data de resolução | Registrar encerramento, quando houver |

Um conflito não deverá ser representado apenas por um marcador técnico sem explicação funcional.

# 88. Estados funcionais de um conflito

## 88.1 Identificado

A divergência foi detectada, mas ainda não foi avaliada.

## 88.2 Em análise

As fontes, temporalidades, contextos e impactos estão sendo comparados.

## 88.3 Contextualizado

A divergência foi explicada por diferenças legítimas de contexto.

As informações podem coexistir.

## 88.4 Sequenciado temporalmente

As informações foram organizadas como estados válidos em períodos diferentes.

## 88.5 Aguardando confirmação

A resolução depende do participante ou de fonte autorizada.

## 88.6 Aguardando evidência

Não existem elementos suficientes para uma conclusão responsável.

## 88.7 Suspenso

O conflito não precisa ser resolvido naquele momento ou sua resolução foi adiada.

## 88.8 Resolvido por correção

Uma informação foi reconhecida como incorreta.

## 88.9 Resolvido por mudança real

A informação anterior estava correta, mas foi substituída por uma nova condição.

## 88.10 Resolvido por prevalência funcional

Uma informação passa a orientar determinada finalidade, sem eliminar as demais.

## 88.11 Contestação persistente

O participante continua rejeitando uma informação ou interpretação.

## 88.12 Arquivado

O conflito não afeta mais o contexto atual e permanece apenas para histórico ou auditoria.

# 89. Gatilhos de identificação de conflito

Um conflito poderá ser identificado quando:

- uma nova declaração contradisser elemento ativo;
- duas integrações apresentarem valores incompatíveis;
- o participante contestar uma interpretação;
- uma informação antiga continuar ativa após mudança declarada;
- uma recomendação depender de dados divergentes;
- uma capacidade consumidora devolver incompatibilidade;
- sinais recorrentes divergirem de preferência declarada;
- existirem datas sobrepostas para estados incompatíveis;
- uma informação estiver autorizada para finalidade diferente da solicitada;
- uma evidência não sustentar a conclusão atribuída;
- duas dimensões criarem bloqueio ou tensão relevante.

# 90. Fluxo funcional de resolução

```text
Conflito identificado
→ preservar informações envolvidas
→ validar origem e autorização
→ comparar temporalidades
→ comparar contextos e granularidade
→ distinguir fato, declaração, evidência e inferência
→ avaliar impacto e sensibilidade
→ verificar possibilidade de coexistência
→ decidir necessidade de confirmação
→ contextualizar, sequenciar, corrigir, substituir, suspender ou manter aberto
→ atualizar recortes contextuais
→ reavaliar decisões dependentes
→ registrar explicação e histórico
```

A resolução deverá responder:

1. as informações tratam do mesmo elemento?
2. representam o mesmo período?
3. foram produzidas para o mesmo contexto?
4. possuem a mesma natureza?
5. estão autorizadas para a finalidade atual?
6. podem coexistir?
7. qual delas poderá orientar a decisão atual?
8. o participante precisa confirmar?
9. quais ações anteriores foram afetadas?
10. como explicar o resultado?

# 91. Critérios de comparação entre informações

## 91.1 Atualidade

Informação mais recente não deverá prevalecer automaticamente.

A data será relevante apenas quando as duas informações representarem o mesmo contexto e houver indício de mudança real.

## 91.2 Especificidade

Uma informação específica poderá refinar uma informação geral.

Exemplo:

```text
Prefere atividades gratuitas
```

e:

```text
Aceita pagar por cursos profissionais
```

As duas podem coexistir em contextos diferentes.

## 91.3 Proximidade com o participante

Declaração explícita e atual deverá ter maior peso funcional sobre inferências.

## 91.4 Adequação da fonte

A autoridade de uma fonte depende do tipo de informação.

Exemplos:

- instituição de ensino poderá confirmar conclusão de curso;
- ela não poderá definir se o curso gerou evolução pessoal;
- plataforma esportiva poderá confirmar atividade registrada;
- ela não poderá definir objetivo de saúde.

## 91.5 Qualidade da evidência

Uma informação sustentada por evidência verificável poderá possuir maior confiança em relação ao fato observado.

Isso não autoriza extrapolações sobre intenção, identidade ou preferência.

## 91.6 Confirmação

Informação confirmada poderá orientar mais finalidades do que uma hipótese não confirmada.

## 91.7 Sensibilidade

Quanto maior a sensibilidade, menor deverá ser a possibilidade de prevalência automática.

## 91.8 Permissão

Uma informação mais confiável não poderá ser utilizada quando não existir autorização para a finalidade solicitada.

# 92. Ordem funcional de consideração

Não deverá existir uma hierarquia absoluta válida para todos os casos.

Como orientação inicial:

1. permissões e limitações vigentes;
2. contestação explícita do participante;
3. declaração atual e consciente;
4. fato diretamente observado e autorizado;
5. evidência de fonte adequada à natureza da informação;
6. declaração histórica ainda válida;
7. evidências convergentes;
8. inferência confirmada;
9. inferência não confirmada;
10. sinal comportamental isolado.

Essa ordem não elimina a necessidade de avaliar temporalidade, contexto, sensibilidade e finalidade.

# 93. Resultados possíveis da resolução

## 93.1 Coexistência contextual

As informações são mantidas em contextos diferentes.

## 93.2 Sequenciamento temporal

As informações são organizadas em períodos sucessivos.

## 93.3 Complementação

Uma informação adiciona detalhe à outra.

## 93.4 Correção

Uma informação incorreta é corrigida.

## 93.5 Substituição

Uma condição atual substitui a anterior sem apagar seu histórico.

## 93.6 Prevalência para finalidade específica

Uma informação orienta uma finalidade, enquanto outra poderá continuar válida para uso diferente.

## 93.7 Suspensão de uso

Nenhuma informação deverá orientar decisão até que o conflito seja esclarecido.

## 93.8 Redução de confiança

A representação permanece disponível, mas com menor confiança.

## 93.9 Solicitação de confirmação

O participante é consultado.

## 93.10 Manutenção do conflito

O sistema reconhece que ainda não existe base suficiente para resolução.

## 93.11 Descarte

Uma informação é descartada funcionalmente por:

- falta de autorização;
- baixa qualidade;
- duplicidade;
- erro comprovado;
- irrelevância;
- incompatibilidade de finalidade.

# 94. Participação da pessoa na resolução

O participante deverá ser envolvido quando o conflito:

- afetar objetivo principal;
- alterar identidade relevante;
- bloquear oportunidades;
- envolver informação sensível;
- modificar restrição;
- afetar compartilhamento;
- alterar finalidade autorizada;
- puder causar prejuízo;
- não puder ser resolvido por contextualização objetiva;
- tiver sido contestado diretamente.

A solicitação deverá apresentar:

1. o que está divergente;
2. de onde veio cada informação;
3. por que a Guivos precisa esclarecer;
4. como a resposta afetará a experiência;
5. possibilidade de não responder;
6. possibilidade de limitar ou remover informações.

# 95. Formas de pergunta para resolução

## 95.1 Confirmação temporal

> Você informou anteriormente que tinha disponibilidade durante a semana. Agora entendemos que isso pode ter mudado. Qual situação representa melhor seu momento atual?

## 95.2 Contextualização

> Você indicou preferência por atividades individuais, mas também demonstrou interesse em grupos esportivos. Essa preferência muda conforme o tipo de atividade?

## 95.3 Correção

> Encontramos duas localizações diferentes associadas ao seu contexto atual. Alguma delas está incorreta?

## 95.4 Mudança real

> Essas informações representam momentos diferentes da sua vida?

## 95.5 Limitação de finalidade

> Você permite que essa informação seja utilizada para encontrar oportunidades ou prefere mantê-la apenas no seu histórico?

## 95.6 Contestação

> Você indicou que essa compreensão está incorreta. Deseja corrigi-la, removê-la ou apenas impedir seu uso?

As perguntas não deverão acusar o participante de incoerência.

# 96. Ausência de resposta

Quando o participante não responder:

- a ausência não será interpretada como confirmação;
- informações críticas poderão deixar de orientar decisões;
- o conflito poderá permanecer aberto;
- recomendações dependentes poderão ser suspensas;
- usos de baixo impacto poderão continuar com indicação de incerteza;
- nova solicitação somente deverá ocorrer quando houver finalidade real;
- o sistema deverá evitar repetição excessiva.

# 97. Conflitos entre declaração e integração

Quando uma integração divergir da declaração do participante:

1. a integração permanecerá como registro daquilo que observou;
2. a declaração atual deverá orientar intenções, preferências e contexto subjetivo;
3. o sistema verificará se existe erro técnico ou diferença de contexto;
4. informações sensíveis não deverão prevalecer automaticamente;
5. a integração poderá ser marcada como contestada;
6. a fonte poderá continuar sendo utilizada para outros fatos não conflitantes.

Exemplo:

```text
Calendário: horário livre
Participante: “Esse período está reservado para cuidar da minha família.”
```

Resultado:

- o horário não deverá ser tratado como disponível;
- o calendário não precisa ser considerado incorreto;
- a interpretação de disponibilidade deverá ser corrigida.

# 98. Conflitos entre organizações e participantes

Organizações poderão informar:

- vínculo;
- participação;
- conclusão;
- presença;
- certificação;
- resultado institucional.

O participante poderá informar:

- significado da experiência;
- satisfação;
- impacto pessoal;
- intenção;
- objetivo;
- percepção de evolução.

Exemplo:

```text
Organização: curso concluído
Participante: “Não desenvolvi a competência esperada.”
```

Resultado:

- conclusão permanece como fato;
- evolução não deverá ser presumida;
- as duas informações coexistem.

# 99. Conflitos entre comportamento e preferência

Comportamentos observados poderão:

- sugerir revisão;
- gerar hipótese;
- indicar exploração;
- revelar mudança possível.

Eles não deverão, isoladamente:

- substituir preferência declarada;
- criar objetivo;
- definir identidade;
- concluir intenção;
- ampliar finalidade de uso.

Uma divergência recorrente poderá gerar uma pergunta contextual:

> Você informou preferência por atividades presenciais, mas recentemente utilizou mais opções online. Sua preferência mudou ou isso ocorreu por uma necessidade temporária?

# 100. Conflitos temporais

Para resolver conflitos temporais, o sistema deverá tentar identificar:

- início de cada condição;
- fim de validade;
- momento da mudança;
- existência de sobreposição;
- data do fato;
- data de registro;
- período em que a Guivos desconhecia a mudança.

Exemplo:

```text
Estado anterior: empregado
Mudança real: desligamento em maio
Informação recebida: julho
```

O histórico deverá registrar:

- que o estado mudou em maio;
- que a Guivos tomou conhecimento em julho;
- que decisões entre maio e julho foram tomadas com informação incompleta.

# 101. Conflitos semânticos e de linguagem

A Guivos deverá considerar que participantes podem utilizar termos:

- vagos;
- regionais;
- profissionais;
- religiosos;
- culturais;
- subjetivos;
- metafóricos;
- com significados próprios.

Exemplo:

> “Quero ter mais liberdade.”

Isso poderá significar:

- liberdade financeira;
- flexibilidade profissional;
- autonomia de tempo;
- mudança de cidade;
- independência familiar;
- exploração pessoal.

O sistema não deverá selecionar um significado sem contexto suficiente.

# 102. Conflitos entre dimensões

Conflitos entre dimensões não deverão ser resolvidos apagando uma delas.

Exemplo:

```text
Direção: iniciar um negócio
Capacidades: experiência suficiente
Restrições: ausência de capital
Momento: transição profissional
```

A função do Contexto Vivo será representar a tensão.

As capacidades de Objetivos e Próximos Passos poderão utilizar essa representação para construir alternativas compatíveis.

# 103. Conflitos de permissão e finalidade

Quando existir incompatibilidade entre uso pretendido e permissão:

- a permissão vigente prevalece;
- o dado não deverá ser entregue à capacidade consumidora;
- a decisão deverá ser recalculada sem aquele elemento;
- o sistema poderá solicitar nova autorização;
- a recusa não deverá impedir usos não relacionados;
- nenhuma autorização deverá ser presumida por conveniência.

Exemplo:

> Uma restrição financeira poderá ser utilizada para evitar oportunidades incompatíveis, mas não para segmentar publicidade, quando essa finalidade não tiver sido autorizada.

# 104. Impacto sobre capacidades consumidoras

Enquanto um conflito relevante estiver aberto, o recorte contextual deverá informar:

- existência do conflito;
- elementos envolvidos;
- confiança reduzida;
- usos permitidos;
- usos suspensos;
- necessidade de confirmação;
- validade temporária da representação.

Capacidades consumidoras não deverão receber apenas um valor consolidado que esconda a divergência.

Exemplo:

```text
Disponibilidade:
- sábado pela manhã — declaração anterior;
- sábado indisponível — sinal recente não confirmado;
- estado: conflito aguardando confirmação;
- uso: não agendar automaticamente;
```

# 105. Reavaliação de decisões existentes

A identificação ou resolução de conflito deverá gerar avaliação sobre:

- oportunidades ativas;
- Próximos Passos;
- intervenções;
- experiências em andamento;
- filtros;
- alertas;
- compartilhamentos;
- recomendações;
- decisões dependentes.

A resolução não deverá alterar retroativamente decisões passadas como se o conflito nunca tivesse existido.

# 106. Resolução automática permitida

Poderá ocorrer sem participação direta quando houver:

- duplicidade exata;
- correção técnica sem alteração de significado;
- diferença temporal claramente identificada;
- contextualização já explicitamente definida;
- informação expirada por data conhecida;
- substituição anteriormente confirmada;
- incompatibilidade de permissão objetiva;
- fonte sem autorização válida;
- erro técnico verificável.

Toda resolução automática deverá ser auditável e reversível quando aplicável.

# 107. Resolução automática proibida

Não deverá ocorrer automaticamente quando envolver:

- identidade;
- saúde;
- religião;
- política;
- renda;
- vulnerabilidade;
- objetivo principal;
- restrição de alto impacto;
- encerramento de relacionamento relevante;
- conclusão de evolução;
- contestação explícita;
- alteração de autorização;
- bloqueio relevante de oportunidades;
- interpretação subjetiva do significado de uma experiência.

# 108. Explicabilidade da resolução

O participante deverá conseguir compreender:

- qual conflito existia;
- quais informações estavam envolvidas;
- de onde vieram;
- qual delas está orientando a experiência;
- por que essa decisão foi tomada;
- se alguma informação foi corrigida, substituída ou limitada;
- quais capacidades foram afetadas;
- como contestar ou reabrir a resolução.

Exemplo:

> Consideramos sua disponibilidade atual como sábado à tarde porque você confirmou essa informação em 10/07. A disponibilidade anterior permanece apenas no histórico.

# 109. Reabertura de conflitos

Um conflito resolvido poderá ser reaberto quando:

- surgir nova evidência;
- o participante contestar o resultado;
- uma fonte corrigir informação;
- houver mudança real;
- a permissão for alterada;
- a resolução anterior tiver sido baseada em informação incompleta;
- nova finalidade exigir avaliação diferente.

A reabertura deverá preservar a resolução anterior e explicar por que ela deixou de ser suficiente.

# 110. Eventos funcionais relacionados

O processo poderá produzir:

- `ConflitoIdentificado`;
- `ConflitoClassificado`;
- `ConflitoContextualizado`;
- `ConflitoTemporalmenteSequenciado`;
- `ConflitoAguardandoConfirmacao`;
- `ConflitoSuspenso`;
- `ConflitoResolvido`;
- `ConflitoReaberto`;
- `InformacaoPrevalenteDefinida`;
- `InformacaoContestada`;
- `InformacaoCorrigida`;
- `InformacaoSubstituida`;
- `UsoSuspensoPorConflito`;
- `RecorteContextualAtualizado`;
- `DecisaoDependenteReavaliada`.

Os eventos são funcionais e não prescrevem tecnologia específica.

# 111. Cenário exemplificativo

## Situação inicial

O participante declarou:

- objetivo principal: conseguir novo emprego;
- preferência: trabalho remoto;
- localização: Belo Horizonte;
- disponibilidade: período noturno.

Posteriormente:

- uma integração registra endereço em Lisboa;
- o participante visualiza oportunidades presenciais;
- uma conversa indica que ele começou um novo emprego.

## Conflitos identificados

1. localização atual;
2. permanência do objetivo de conseguir emprego;
3. preferência por trabalho remoto;
4. disponibilidade noturna.

## Tratamento

A Guivos não deverá concluir automaticamente que:

- o participante se mudou;
- o objetivo foi concluído;
- a preferência mudou;
- a disponibilidade deixou de existir.

Ela poderá perguntar:

> Entendemos que sua situação profissional e sua localização podem ter mudado. Você gostaria de atualizar essas informações?

## Possível resolução

O participante informa:

- mudou-se temporariamente para Lisboa;
- começou um emprego, mas ainda procura uma oportunidade melhor;
- continua preferindo trabalho remoto;
- não possui mais disponibilidade noturna.

Resultado:

- localização: Lisboa, temporária;
- objetivo: ativo, com significado atualizado;
- preferência remota: confirmada;
- disponibilidade noturna: encerrada;
- histórico preservado;
- oportunidades e Próximos Passos reavaliados.

# 112. Critérios de resolução confiável

Um conflito será considerado adequadamente tratado quando:

- todas as informações relevantes forem preservadas;
- temporalidade e contexto forem avaliados;
- fato e inferência estiverem diferenciados;
- permissões forem respeitadas;
- a fonte adequada for considerada;
- o participante for envolvido quando necessário;
- nenhuma informação sensível prevalecer silenciosamente;
- capacidades consumidoras receberem indicação de incerteza;
- decisões dependentes forem reavaliadas;
- o resultado puder ser explicado;
- histórico e contestação permanecerem disponíveis;
- a resolução puder ser reaberta.

# 113. Regras fundamentais de conflito

1. Divergência não significa falsidade.
2. Informações de momentos diferentes não são necessariamente contraditórias.
3. Contextos diferentes poderão permitir coexistência.
4. Declaração atual prevalece sobre inferência incompatível.
5. Comportamento observado não substitui automaticamente intenção declarada.
6. A autoridade da fonte depende da natureza da informação.
7. Permissão prevalece sobre confiança ou conveniência.
8. Conflitos sensíveis não deverão ser resolvidos silenciosamente.
9. Ausência de resposta não equivale a concordância.
10. Uma resolução poderá ser específica para determinada finalidade.
11. O histórico não deverá ser reescrito.
12. Todo conflito relevante deverá ser explicável e contestável.

Com isso, fica especificada a **resolução detalhada de conflitos entre informações, interpretações, fontes, dimensões e temporalidades**.

O próximo bloco da Capacidade 02 é a definição dos **comportamentos funcionais da interface `Meu Contexto Hoje`**.
