---
id: PAS-001-PP-LIFECYCLE-001
title: Regras do Ciclo de Vida dos Próximos Passos
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-PP-FOUNDATION-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-PP-LIFECYCLE-001 — Regras do Ciclo de Vida dos Próximos Passos

## 1. Autoridade e vínculo

Este documento é a **segunda extensão normativa da Capacidade 05 — Próximos Passos** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 0 a 1530 consolidadas pelo `PAS-001 0.5.0`, pelas extensões normativas de Contexto Vivo, Objetivos, Eventos de Vida e pelo `PAS-001-PP-FOUNDATION-001 1.0.0`.

Esta extensão mantém a Capacidade 05 no estado `In progress` e eleva seu progresso editorial de referência de `20%` para `40%`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade da especificação-base ou das capacidades concluídas.

# 1531. Ciclo de vida da Capacidade de Próximos Passos

O ciclo de vida deverá governar a evolução de um Próximo Passo desde sua identificação inicial até sua conclusão, substituição, cancelamento, expiração ou arquivamento.

Seu fluxo geral será:

```text
necessidade, objetivo, evento ou condição
→ possibilidade de movimento
→ proposta
→ avaliação
→ confirmação
→ preparação
→ prontidão
→ ativação ou agendamento
→ execução
→ resultado
→ conclusão, substituição, cancelamento ou revisão
→ propagação dos efeitos autorizados
```

O ciclo não deverá pressupor que todo Próximo Passo:

- será confirmado;
- será iniciado;
- possuirá prazo;
- será executado pela mesma pessoa;
- produzirá o resultado esperado;
- representará progresso;
- permanecerá relevante;
- exigirá uma ação imediata.

# 1532. Objetivos do ciclo de vida

O ciclo deverá:

1. preservar a diferença entre hipótese, decisão e execução;
2. impedir ativação automática de passos pessoais;
3. representar prontidão e impedimentos;
4. organizar prioridade sem impor produtividade;
5. preservar temporalidade e dependências;
6. permitir alternativas;
7. acompanhar execução sem vigilância excessiva;
8. reconhecer resultados distintos da conclusão;
9. permitir pausa, cancelamento e substituição;
10. tratar expiração e perda de relevância;
11. preservar contestação e correção;
12. suportar recorrência;
13. governar passos compartilhados;
14. propagar somente recortes necessários;
15. preservar histórico;
16. manter o participante no controle.

# 1533. Princípios do ciclo de vida

## 1533.1 Clareza de estado

O estado apresentado deverá corresponder à condição funcional real do passo.

## 1533.2 Confirmação antes de compromisso

Uma proposta pessoal não deverá ser tratada como decisão assumida.

## 1533.3 Separação de dimensões

Estado, prioridade, prontidão, urgência, prazo, esforço e confiança deverão permanecer distintos.

## 1533.4 Reversibilidade

Alterações deverão ser reversíveis sempre que a natureza do passo permitir.

## 1533.5 Histórico preservado

Correções e substituições não deverão apagar registros anteriores.

## 1533.6 Proporcionalidade

O nível de formalidade deverá ser proporcional ao risco, impacto, sensibilidade e número de participantes.

## 1533.7 Autonomia

O participante deverá poder rejeitar, adiar, pausar, reformular, substituir ou cancelar passos pessoais.

## 1533.8 Neutralidade comercial

Receita, comissão, patrocínio ou estoque não deverão influenciar a ativação, prioridade ou conclusão.

## 1533.9 Falha segura

Falhas deverão reduzir automação e preservar o último estado válido.

## 1533.10 Ausência legítima

O sistema deverá aceitar períodos sem Próximos Passos ativos.

# 1534. Estados funcionais normativos

Os estados funcionais da capacidade serão:

| Estado | Significado |
|---|---|
| Proposto | Hipótese de movimento apresentada para avaliação |
| Confirmado | Movimento reconhecido como válido pelo decisor competente |
| Pronto | Condições mínimas conhecidas para início foram atendidas |
| Agendado | Janela temporal ou compromisso de execução foi definido |
| Em andamento | Execução foi iniciada |
| Bloqueado | Um impedimento inviabiliza a continuidade |
| Pausado | A continuidade foi temporariamente interrompida por decisão |
| Concluído | O movimento foi reconhecido como realizado |
| Cancelado | O movimento não deverá mais ser realizado |
| Substituído | Outro passo passou a cumprir sua função |
| Expirado | O passo perdeu atualidade, janela ou validade funcional |
| Contestado | Formulação, responsabilidade, estado ou resultado foi questionado |
| Corrigido | Informação anterior foi formalmente ajustada |
| Arquivado | O passo saiu da operação cotidiana sem perda histórica |

# 1535. Estado da informação

O estado da informação deverá ser representado separadamente do estado funcional.

Ele poderá ser:

- sugerido;
- declarado;
- parcialmente confirmado;
- confirmado;
- observado;
- desatualizado;
- divergente;
- contestado;
- corrigido;
- desconhecido.

Exemplo:

```text
estado funcional:
Em andamento

estado da informação:
desatualizado
```

O sistema não deverá concluir que a execução parou apenas porque não recebeu atualização recente.

# 1536. Dimensões complementares do ciclo

Além do estado funcional, um Próximo Passo poderá possuir:

- prioridade;
- urgência;
- prontidão;
- acionabilidade;
- nível de compromisso;
- horizonte;
- esforço estimado;
- risco;
- sensibilidade;
- confiança;
- atualidade;
- dependências;
- bloqueios;
- recorrência;
- compartilhamento.

Nenhuma dessas dimensões deverá ser inferida diretamente a partir de outra.

# 1537. Identificação de possibilidade

Uma possibilidade de Próximo Passo poderá ser identificada quando houver:

- objetivo sem movimento definido;
- Evento de Vida que exija adaptação;
- bloqueio a ser compreendido;
- necessidade declarada;
- responsabilidade reconhecida;
- condição de preparação;
- oportunidade compatível;
- resultado anterior insuficiente;
- dependência pendente;
- solicitação explícita de ajuda;
- mudança relevante no Contexto Vivo.

A identificação deverá produzir uma possibilidade ou proposta, não uma decisão assumida.

# 1538. Formulação inicial

A formulação deverá indicar, quando necessário:

- ação, escolha, preparação ou condição;
- resultado imediato esperado;
- titular;
- possível responsável;
- relação contextual;
- horizonte;
- dependências principais;
- riscos conhecidos;
- origem;
- nível de decisão;
- sensibilidade.

Formulações genéricas poderão permanecer como possibilidades ainda não acionáveis.

# 1539. Critério de formulação suficiente

Uma formulação será suficiente quando permitir compreender:

- o movimento pretendido;
- sua relação com a jornada;
- a autoridade para decidir;
- a condição básica de execução;
- o resultado imediato esperado.

A formulação não precisará possuir plano completo, prazo exato ou todas as tarefas derivadas.

# 1540. Proposição

Um Próximo Passo poderá ser proposto por:

- participante;
- representante autorizado;
- Organização;
- Coletivo;
- profissional especializado;
- capacidade do Journey;
- serviço integrado;
- Guivos Intelligence;
- resultado de revisão;
- evento funcional anterior.

A origem e a autoridade deverão permanecer visíveis.

# 1541. Propostas pessoais

Propostas pessoais deverão:

- permanecer opcionais;
- permitir rejeição sem penalidade;
- apresentar justificativa;
- indicar incerteza;
- evitar linguagem de cobrança;
- não criar compromisso automático;
- não reservar recursos;
- não ser compartilhadas como decisão;
- não alterar Objetivos ou Contexto Vivo silenciosamente.

# 1542. Propostas institucionais

Uma Organização poderá propor ou definir Próximos Passos dentro de sua autoridade.

O sistema deverá distinguir:

```text
passo institucional:
definido pela Organização dentro de processo legítimo

passo pessoal:
decidido pelo participante em sua jornada
```

Uma obrigação institucional não deverá ser apresentada como objetivo pessoal voluntário.

# 1543. Propostas da Guivos Intelligence

Uma proposta da Guivos Intelligence deverá apresentar:

- motivo;
- objetivo ou necessidade relacionada;
- contexto considerado;
- limitações;
- dependências;
- esforço estimado;
- riscos relevantes;
- alternativas;
- nível de confiança.

A Intelligence não deverá ocultar que a formulação foi gerada ou assistida por inteligência.

# 1544. Alternativas

A capacidade poderá formular múltiplas alternativas para a mesma necessidade.

As alternativas deverão poder ser:

- comparadas;
- combinadas;
- rejeitadas;
- mantidas para revisão futura;
- substituídas;
- condicionadas a cenários.

A existência de uma alternativa preferida não deverá apagar as demais.

# 1545. Avaliação de proposta

Antes da confirmação, a proposta poderá ser avaliada por:

- adequação ao objetivo;
- compatibilidade contextual;
- acionabilidade;
- autoridade;
- responsabilidade;
- dependências;
- esforço;
- risco;
- temporalidade;
- reversibilidade;
- sensibilidade;
- disponibilidade;
- alternativas;
- impacto sobre outros passos.

# 1546. Resultados possíveis da avaliação

A avaliação poderá resultar em:

- confirmar;
- reformular;
- dividir;
- unificar;
- adiar;
- manter como possibilidade;
- rejeitar;
- solicitar informação;
- solicitar apoio;
- indicar bloqueio;
- encaminhar para profissional;
- arquivar proposta.

# 1547. Confirmação

A confirmação deverá ser realizada pelo decisor competente.

Ela deverá registrar:

- quem confirmou;
- em qual papel;
- em qual momento;
- qual formulação foi confirmada;
- finalidade;
- nível de compromisso;
- condições;
- permissões;
- responsabilidades conhecidas.

# 1548. Confirmação proporcional

A confirmação poderá ser:

- simples;
- explícita;
- reforçada;
- institucional;
- compartilhada;
- condicionada;
- assistida.

Maior formalidade poderá ser exigida quando houver:

- risco elevado;
- obrigação;
- impacto financeiro;
- responsabilidade sobre terceiros;
- compartilhamento externo;
- informação sensível;
- difícil reversão;
- consequência jurídica;
- uso de recursos relevantes.

# 1549. Confirmação condicionada

Um Próximo Passo poderá ser confirmado sob condições.

Exemplo:

```text
confirmado:
participar do programa

condição:
somente se a bolsa for aprovada
```

A confirmação condicionada não deverá produzir ativação antes do atendimento da condição.

# 1550. Confirmação parcial

Em passos compostos ou compartilhados, a confirmação poderá abranger apenas:

- parte da formulação;
- papel específico;
- período;
- recurso;
- subpasso;
- participante;
- finalidade.

A parte não confirmada deverá permanecer separada.

# 1551. Ausência de confirmação

A ausência de resposta não deverá significar:

- confirmação;
- rejeição;
- consentimento;
- compromisso;
- prioridade;
- cancelamento;
- conclusão.

A proposta poderá permanecer pendente, envelhecer ou ser arquivada conforme sua natureza.

# 1552. Rejeição

A rejeição deverá:

- interromper a ativação;
- preservar a proposta no histórico quando necessário;
- permitir motivo opcional;
- não reduzir pontuação;
- não gerar cobrança;
- não ser interpretada como desinteresse geral;
- não impedir propostas futuras distintas.

# 1553. Reformulação

Uma proposta ou passo confirmado poderá ser reformulado quando:

- estiver amplo;
- estiver ambíguo;
- deixar de ser acionável;
- mudar o contexto;
- surgir novo risco;
- houver contestação;
- o resultado esperado mudar;
- o participante preferir outra abordagem.

A reformulação deverá preservar a formulação anterior.

# 1554. Desdobramento

Um Próximo Passo poderá ser dividido quando:

- possuir ações independentes;
- envolver responsáveis diferentes;
- exigir dependências distintas;
- possuir temporalidades diferentes;
- precisar de acompanhamento separado;
- estiver excessivamente amplo.

O passo original deverá permanecer relacionado aos novos passos.

# 1555. Unificação

Próximos Passos poderão ser unificados quando:

- representarem o mesmo movimento;
- tiverem resultado imediato equivalente;
- forem duplicados;
- dependerem das mesmas condições;
- não precisarem de estados separados.

A unificação deverá preservar origem, histórico e relações anteriores.

# 1556. Prontidão

Prontidão representa a existência das condições mínimas conhecidas para iniciar.

Ela poderá considerar:

- informação suficiente;
- decisão concluída;
- autorização;
- recurso;
- disponibilidade;
- competência;
- segurança;
- documento;
- participante responsável;
- dependências essenciais;
- janela temporal.

# 1557. Pronto não significa iniciado

O estado `Pronto` não deverá indicar:

- execução iniciada;
- prioridade máxima;
- obrigação imediata;
- disponibilidade contínua;
- conclusão garantida;
- ausência de risco;
- aceitação de oportunidade específica.

# 1558. Avaliação de prontidão

A avaliação poderá resultar em:

- pronto;
- parcialmente pronto;
- dependência pendente;
- bloqueado;
- informação insuficiente;
- risco não tratado;
- autorização pendente;
- recurso indisponível;
- revisão necessária.

# 1559. Ativação operacional

A ativação representa a entrada do Próximo Passo no conjunto de movimentos considerados para preparação, agendamento ou execução.

A ativação deverá permanecer distinta de:

- confirmação;
- prioridade;
- agendamento;
- início;
- compartilhamento;
- compromisso externo.

# 1560. Critérios de ativação

Um passo poderá ser ativado quando:

- estiver confirmado;
- possuir finalidade atual;
- estiver suficientemente acionável;
- não possuir impedimento crítico oculto;
- estiver dentro da capacidade operacional;
- possuir autorização necessária;
- sua sensibilidade estiver protegida.

# 1561. Limites de ativação simultânea

A capacidade deverá evitar excesso de passos ativos.

O limite deverá considerar:

- preferência do participante;
- carga atual;
- complexidade;
- esforço;
- objetivos concorrentes;
- responsabilidades institucionais;
- acessibilidade;
- eventos recentes;
- risco de fadiga.

Não deverá existir limite universal rígido para todas as pessoas.

# 1562. Portfólio ativo

O portfólio deverá distinguir:

- principal;
- ativo;
- pronto;
- agendado;
- em andamento;
- bloqueado;
- pausado;
- futuro;
- alternativo;
- aguardando condição;
- em revisão.

O sistema deverá evitar apresentar todos como igualmente urgentes.

# 1563. Priorização

A prioridade operacional deverá ser atribuída ou revisada considerando:

- vontade do participante;
- obrigação legítima;
- urgência;
- janela;
- dependência;
- prontidão;
- risco;
- esforço;
- impacto contextual;
- bloqueios removidos;
- Evento de Vida;
- consequência da não realização;
- alternativas.

# 1564. Níveis de prioridade

A prioridade poderá ser representada como:

- crítica;
- alta;
- moderada;
- baixa;
- futura;
- não definida.

Esses níveis deverão ser contextualizados e não deverão representar valor pessoal.

# 1565. Prioridade principal

Um participante poderá definir um passo principal dentro de:

- objetivo;
- área;
- projeto;
- período;
- contexto;
- responsabilidade.

Não deverá existir obrigatoriamente um único passo principal para toda a vida.

# 1566. Repriorização

A prioridade poderá mudar quando:

- o contexto mudar;
- surgir Evento de Vida;
- uma dependência for resolvida;
- uma janela estiver próxima;
- o esforço real se mostrar diferente;
- o risco aumentar;
- outro passo se tornar mais relevante;
- o participante alterar sua decisão;
- uma obrigação legítima surgir.

A mudança deverá ser explicável.

# 1567. Prioridade sugerida

A prioridade sugerida pela Guivos deverá:

- apresentar fatores considerados;
- permitir alteração;
- indicar limitações;
- não utilizar receita;
- não penalizar divergência;
- não ser tratada como decisão final.

# 1568. Sequenciamento

O sequenciamento deverá organizar relações como:

- anterior;
- posterior;
- paralelo;
- alternativo;
- condicional;
- preparatório;
- confirmatório;
- substitutivo;
- recorrente.

A ordem deverá permanecer revisável.

# 1569. Sequência linear

Uma sequência linear poderá ser utilizada quando:

- houver dependência clara;
- a ordem possuir justificativa;
- a execução paralela for inadequada;
- o participante compreender a relação.

A sequência não deverá ser criada apenas por conveniência visual.

# 1570. Execução paralela

Passos poderão ocorrer em paralelo quando:

- não houver dependência impeditiva;
- a carga for compatível;
- não houver risco de conflito;
- os responsáveis forem distintos;
- o participante desejar.

A capacidade deverá evitar paralelismo excessivo.

# 1571. Passos alternativos

Passos alternativos deverão representar diferentes meios para uma finalidade semelhante.

A confirmação de uma alternativa poderá:

- suspender as demais;
- mantê-las como contingência;
- cancelar alternativas incompatíveis;
- preservar alternativas futuras.

# 1572. Passos condicionais

Um passo condicional deverá registrar:

- condição;
- fonte da condição;
- temporalidade;
- forma de verificação;
- consequência do atendimento;
- consequência da não ocorrência;
- data ou gatilho de revisão.

# 1573. Dependências

Uma dependência deverá possuir:

- tipo;
- descrição;
- origem;
- responsável possível;
- estado;
- criticidade;
- temporalidade;
- forma de resolução;
- evidência;
- relação com o passo.

# 1574. Tipos de dependência

As dependências poderão ser:

- informacionais;
- decisórias;
- documentais;
- financeiras;
- técnicas;
- humanas;
- institucionais;
- temporais;
- geográficas;
- jurídicas;
- de segurança;
- de competência;
- de oportunidade;
- relacionais;
- de outro Próximo Passo.

# 1575. Estados das dependências

Uma dependência poderá estar:

- identificada;
- pendente;
- em tratamento;
- atendida;
- dispensada;
- impossível;
- expirada;
- contestada;
- desatualizada.

# 1576. Dependência atendida

O atendimento de uma dependência poderá:

- tornar o passo pronto;
- remover bloqueio;
- permitir agendamento;
- alterar prioridade;
- tornar alternativa desnecessária;
- exigir nova confirmação;
- produzir novo passo.

# 1577. Dependência dispensada

Uma dependência poderá ser dispensada quando:

- deixar de ser necessária;
- houver alternativa legítima;
- a formulação mudar;
- sua exigência tiver sido incorreta;
- a autoridade competente dispensá-la.

A dispensa deverá ser registrada e explicável.

# 1578. Bloqueios

Um bloqueio deverá representar impedimento atual que inviabiliza ou torna inadequada a continuidade.

Ele deverá permanecer distinto de:

- dificuldade;
- esforço elevado;
- baixa prioridade;
- pausa;
- incerteza;
- falta de motivação presumida;
- atraso;
- dependência não crítica.

# 1579. Tipos de bloqueio

Bloqueios poderão ser:

- ausência de decisão;
- falta de informação;
- recurso indisponível;
- ausência de autorização;
- risco não tratado;
- dependência pendente;
- conflito;
- indisponibilidade do responsável;
- condição externa;
- restrição contextual;
- problema técnico;
- questão jurídica;
- evento de segurança;
- divergência de identidade;
- contestação.

# 1580. Registro do bloqueio

O bloqueio deverá registrar:

- origem;
- descrição;
- data;
- impacto;
- criticidade;
- responsável possível;
- ação de resolução, quando existente;
- alternativa;
- condição de revisão;
- evidências;
- sensibilidade.

# 1581. Bloqueio automático permitido

Um bloqueio automático poderá ocorrer quando houver condição objetiva e autorizada, como:

- autorização obrigatória ausente;
- identidade não validada;
- risco crítico;
- recurso indispensável indisponível;
- dependência técnica confirmada;
- prazo legal expirado;
- revogação aplicável.

# 1582. Bloqueios automáticos proibidos

Não deverão ser criados automaticamente por:

- baixa interação;
- ausência de abertura do aplicativo;
- comportamento isolado;
- inferência emocional;
- baixo consumo;
- rejeição de oportunidade comercial;
- comparação com outros participantes;
- ausência de prazo;
- ritmo considerado lento.

# 1583. Desbloqueio

O desbloqueio deverá ocorrer quando:

- o impedimento for resolvido;
- a dependência for atendida;
- a condição mudar;
- a formulação for ajustada;
- uma alternativa for adotada;
- a contestação for resolvida;
- o risco for reduzido;
- a autoridade competente liberar.

O desbloqueio não deverá iniciar automaticamente a execução.

# 1584. Pausa

A pausa representa interrupção deliberada e temporária.

Ela poderá ocorrer por:

- escolha do participante;
- necessidade de recuperação;
- mudança de prioridade;
- Evento de Vida;
- indisponibilidade temporária;
- revisão;
- sobrecarga;
- risco;
- espera;
- decisão institucional legítima.

# 1585. Pausa e bloqueio

```text
Pausado:
continuidade interrompida por decisão

Bloqueado:
continuidade impedida por condição
```

Um passo poderá estar pausado e possuir bloqueios simultaneamente, mas as causas deverão permanecer separadas.

# 1586. Efeitos da pausa

A pausa deverá:

- retirar o passo da atenção imediata;
- suspender notificações não essenciais;
- preservar histórico;
- manter dependências relevantes;
- indicar condição de revisão;
- preservar possibilidade de retomada;
- não representar fracasso.

# 1587. Retomada

A retomada deverá reavaliar:

- formulação;
- atualidade;
- prioridade;
- dependências;
- bloqueios;
- responsabilidade;
- risco;
- prontidão;
- janela temporal;
- contexto atual.

A retomada não deverá assumir que as condições anteriores continuam válidas.

# 1588. Agendamento

Um Próximo Passo poderá ser agendado quando possuir:

- data;
- período;
- janela;
- compromisso;
- gatilho temporal;
- recorrência;
- condição com prazo.

O agendamento deverá registrar a origem e o nível de compromisso.

# 1589. Agendamento sugerido

Uma sugestão de data não deverá ser tratada como agendamento confirmado.

A Guivos deverá diferenciar:

```text
janela sugerida
data escolhida
compromisso confirmado
reserva externa concluída
```

# 1590. Alteração de agendamento

O participante ou autoridade competente poderá:

- antecipar;
- adiar;
- remover data;
- alterar janela;
- mudar recorrência;
- substituir compromisso;
- cancelar agendamento sem cancelar o passo.

# 1591. Prazo vencido

O vencimento do prazo não deverá produzir automaticamente:

- conclusão;
- cancelamento;
- abandono;
- fracasso;
- baixa prioridade;
- punição;
- perda do objetivo.

O sistema deverá avaliar se o passo está atrasado, expirado, ainda válido ou precisa de revisão.

# 1592. Adiamento

O adiamento deverá registrar:

- nova temporalidade, quando conhecida;
- motivo opcional;
- impacto sobre dependências;
- impacto sobre outros passos;
- necessidade de revisão;
- nível de compromisso.

Adiamentos repetidos não deverão ser interpretados automaticamente como falta de interesse.

# 1593. Início da execução

O estado `Em andamento` deverá resultar de:

- declaração do executor;
- ação explícita;
- confirmação institucional;
- integração autorizada;
- evidência objetiva suficiente;
- início de experiência relacionada.

O início não deverá ser inferido apenas pela visualização de conteúdo ou acesso a uma oportunidade.

# 1594. Início parcial

Passos compostos poderão possuir início parcial.

O sistema deverá registrar:

- parte iniciada;
- parte ainda não iniciada;
- responsável;
- temporalidade;
- dependências remanescentes;
- impacto sobre o estado global.

# 1595. Execução

Durante a execução, poderão ser registrados:

- ações realizadas;
- subpassos;
- decisões;
- resultados parciais;
- bloqueios;
- mudanças de escopo;
- esforço real;
- evidências;
- apoio recebido;
- alterações de risco;
- atualização temporal.

A capacidade não deverá exigir acompanhamento excessivo.

# 1596. Acompanhamento proporcional

O nível de acompanhamento deverá considerar:

- duração;
- risco;
- sensibilidade;
- dependências;
- número de participantes;
- preferência do participante;
- impacto institucional;
- necessidade de auditoria.

Passos simples poderão ser acompanhados apenas pelo estado final.

# 1597. Atualização durante execução

Uma atualização poderá alterar:

- formulação;
- resultado imediato;
- responsabilidade;
- prioridade;
- temporalidade;
- dependência;
- bloqueio;
- esforço;
- risco;
- alternativa;
- estado da informação.

Alterações materiais poderão exigir nova confirmação.

# 1598. Mudança de escopo

Uma mudança de escopo deverá ser reconhecida quando o passo passar a representar movimento substancialmente diferente.

A capacidade deverá decidir entre:

- atualizar o passo;
- reformular;
- dividir;
- concluir o passo anterior e criar outro;
- substituir;
- cancelar.

# 1599. Resultado imediato

O resultado imediato representa a consequência observada ou declarada da execução.

Ele poderá ser:

- alcançado;
- parcialmente alcançado;
- não alcançado;
- diferente do esperado;
- ainda desconhecido;
- contestado;
- não aplicável.

# 1600. Resultado não equivale a progresso

Um resultado poderá:

- contribuir para objetivo;
- não alterar objetivo;
- revelar nova informação;
- demonstrar inadequação do passo;
- criar bloqueio;
- indicar necessidade de adaptação;
- produzir Evento de Vida;
- gerar experiência.

A Capacidade de Objetivos deverá avaliar o progresso.

# 1601. Conclusão

Um Próximo Passo poderá ser concluído quando houver reconhecimento suficiente de que o movimento delimitado foi realizado.

A conclusão deverá considerar:

- formulação;
- resultado imediato;
- natureza do passo;
- evidências;
- declaração do responsável;
- autoridade;
- contestações;
- partes componentes.

# 1602. Formas de conclusão

A conclusão poderá ser:

- declarada pelo participante;
- confirmada pelo responsável;
- institucional;
- assistida;
- evidenciada;
- parcial;
- automática autorizada para fato objetivo;
- derivada de integração autorizada.

# 1603. Conclusão automática permitida

Poderá ocorrer para fatos objetivos, como:

- documento enviado;
- inscrição registrada;
- pagamento autorizado concluído;
- entrega confirmada;
- reserva efetivada;
- certificação recebida;
- conexão realizada.

A conclusão automática deverá possuir fonte autorizada e permitir contestação.

# 1604. Conclusão automática proibida

Não deverá ocorrer apenas por:

- acesso a conteúdo;
- clique;
- tempo de tela;
- presença física inferida;
- localização;
- compra;
- consumo;
- atividade isolada;
- ausência de interação;
- comportamento semelhante ao esperado.

# 1605. Conclusão parcial

Um passo composto poderá ser parcialmente concluído.

O sistema deverá distinguir:

- partes concluídas;
- partes pendentes;
- resultado parcial;
- possibilidade de desdobramento;
- necessidade de nova formulação;
- decisão de encerrar o restante.

# 1606. Conclusão sem resultado esperado

Um passo poderá ser concluído mesmo quando o resultado esperado não ocorrer, desde que o movimento tenha sido efetivamente realizado.

Exemplo:

```text
Próximo Passo:
solicitar revisão da decisão

Execução:
solicitação enviada

Resultado:
revisão negada

Estado do passo:
Concluído
```

O resultado deverá permanecer separado da execução.

# 1607. Efeitos da conclusão

A conclusão poderá produzir:

- evidência para Objetivos;
- atualização do Contexto Vivo;
- liberação de dependência;
- desbloqueio de outro passo;
- ativação de alternativa;
- oportunidade de nova decisão;
- registro de experiência;
- sinal para Evolução Contínua;
- necessidade de novo Próximo Passo.

Nenhum efeito deverá ser aplicado fora do contrato da capacidade responsável.

# 1608. Cancelamento

O cancelamento representa decisão de não prosseguir com o passo.

Ele poderá ocorrer por:

- escolha;
- perda de necessidade;
- mudança de contexto;
- risco;
- inviabilidade;
- obrigação removida;
- substituição não formalizada;
- duplicidade;
- erro;
- revogação;
- decisão institucional competente.

# 1609. Efeitos do cancelamento

O cancelamento deverá:

- interromper novas ações dependentes;
- preservar histórico;
- informar participantes necessários;
- revisar compromissos;
- recompor recortes;
- tratar recursos reservados;
- manter resultados já produzidos;
- não apagar experiências relacionadas.

# 1610. Cancelamento não representa fracasso

O cancelamento poderá representar:

- adaptação;
- proteção;
- mudança de prioridade;
- correção;
- perda legítima de relevância;
- decisão racional;
- resolução por outro meio.

Não deverá produzir julgamento automático.

# 1611. Substituição

Um passo deverá ser marcado como `Substituído` quando outro passo passar a cumprir função equivalente ou mais adequada.

A relação deverá registrar:

- passo anterior;
- passo substituto;
- motivo;
- momento;
- efeitos migrados;
- dependências transferidas;
- responsabilidades;
- histórico.

# 1612. Substituição parcial

Parte de um Próximo Passo poderá ser substituída.

O sistema deverá:

- preservar a parte mantida;
- criar ou associar substituto;
- revisar dependências;
- revisar prioridade;
- preservar resultados anteriores;
- evitar duplicidade.

# 1613. Expiração

Um Próximo Passo poderá expirar quando:

- a janela temporal encerrar;
- a condição deixar de existir;
- a oportunidade ficar indisponível;
- a informação se tornar desatualizada;
- o objetivo mudar;
- o evento relacionado deixar de ser relevante;
- o passo não possuir mais utilidade funcional.

# 1614. Expiração automática

A expiração automática poderá ocorrer quando houver regra objetiva e previamente conhecida.

Exemplos:

- prazo de inscrição encerrado;
- autorização vencida;
- janela contratual concluída;
- evento relacionado cancelado.

A expiração deverá ser contestável quando a fonte puder estar incorreta.

# 1615. Expiração e cancelamento

```text
Expirado:
perdeu validade ou atualidade por condição

Cancelado:
foi deliberadamente encerrado
```

O sistema não deverá substituir um pelo outro silenciosamente.

# 1616. Contestação

Poderão ser contestados:

- formulação;
- titularidade;
- responsabilidade;
- autoridade;
- prioridade;
- estado;
- temporalidade;
- bloqueio;
- conclusão;
- cancelamento;
- expiração;
- compartilhamento;
- resultado;
- evidência.

# 1617. Efeitos da contestação

A contestação deverá:

- registrar o ponto questionado;
- limitar efeitos críticos;
- suspender automações quando necessário;
- preservar versões;
- solicitar revisão;
- indicar estado da informação;
- proteger o participante;
- evitar sobrescrita silenciosa.

# 1618. Resolução de contestação

A contestação poderá resultar em:

- manutenção;
- correção;
- reformulação;
- mudança de estado;
- divisão;
- substituição;
- cancelamento;
- reabertura;
- remoção de responsabilidade;
- revisão de recortes;
- registro de divergência não resolvida.

# 1619. Correção

A correção deverá tratar informação incorreta sem apagar o histórico.

Poderão ser corrigidos:

- formulação;
- titular;
- papel;
- data;
- prioridade;
- estado;
- dependência;
- bloqueio;
- origem;
- autoridade;
- resultado;
- conclusão;
- sensibilidade;
- permissão.

# 1620. Correção compensatória

Quando a informação anterior já tiver produzido efeitos, a correção deverá:

- preservar o registro original;
- registrar nova versão ou evento;
- identificar o erro;
- recompor estados;
- revisar efeitos;
- notificar consumidores;
- corrigir recortes;
- preservar auditoria.

# 1621. Reabertura

Um Próximo Passo concluído, cancelado, expirado ou arquivado poderá ser reaberto quando:

- houver erro;
- surgir nova condição;
- a execução precisar continuar;
- a conclusão tiver sido parcial;
- uma contestação for aceita;
- o contexto tornar o movimento novamente relevante.

A reabertura deverá distinguir continuidade de nova ocorrência.

# 1622. Novo passo ou reabertura

Deverá ser criado novo passo quando houver:

- nova finalidade;
- novo resultado imediato;
- novo ciclo temporal;
- novo responsável;
- mudança substancial de contexto;
- nova obrigação;
- execução independente.

A reabertura será adequada quando o movimento original continuar semanticamente válido.

# 1623. Arquivamento

O arquivamento deverá retirar o passo da operação cotidiana.

Ele poderá ocorrer após:

- conclusão;
- cancelamento;
- substituição;
- expiração;
- rejeição;
- longa inatividade legítima;
- decisão do participante.

# 1624. Arquivamento não equivale a exclusão

O arquivamento deverá preservar:

- histórico;
- estados anteriores;
- resultados;
- evidências;
- relações;
- dependências históricas;
- impactos;
- auditoria;
- recortes ainda necessários.

# 1625. Recorrência

Um Próximo Passo recorrente deverá possuir:

- unidade de ocorrência;
- frequência;
- período;
- regra de repetição;
- condição de pausa;
- condição de encerramento;
- forma de conclusão por ocorrência;
- tolerância;
- tratamento de ocorrências não realizadas.

# 1626. Recorrência e hábito

A recorrência deverá representar repetição operacional.

Ela não deverá concluir automaticamente:

- formação de hábito;
- mudança comportamental;
- evolução;
- aderência;
- identidade;
- transformação pessoal.

# 1627. Ocorrências recorrentes

Cada ocorrência poderá possuir:

- data;
- estado;
- executor;
- resultado;
- evidência;
- motivo de não realização;
- contestação;
- correção.

O registro agregado não deverá apagar ocorrências individuais relevantes.

# 1628. Ocorrência não realizada

Uma ocorrência não realizada poderá ser:

- adiada;
- dispensada;
- cancelada;
- perdida;
- bloqueada;
- não aplicável;
- desconhecida.

Ela não deverá gerar punição ou conclusão sobre disciplina pessoal.

# 1629. Pausa da recorrência

A pausa deverá:

- interromper novas ocorrências;
- preservar as anteriores;
- indicar condição de retomada;
- suspender notificações;
- manter a possibilidade de encerramento;
- evitar geração retroativa automática.

# 1630. Encerramento da recorrência

A recorrência poderá terminar por:

- período concluído;
- quantidade alcançada;
- condição atingida;
- decisão;
- substituição;
- perda de necessidade;
- mudança de contexto;
- Evento de Vida;
- risco;
- obrigação encerrada.

# 1631. Passos compartilhados

Um Próximo Passo compartilhado deverá preservar:

- titularidade;
- objetivo comum;
- responsabilidades individuais;
- decisões necessárias;
- participantes;
- permissões;
- conteúdo privado;
- dependências;
- temporalidade;
- possibilidade de saída.

# 1632. Confirmação compartilhada

A confirmação deverá ocorrer por participante ou papel.

O sistema deverá representar:

- confirmado por todos;
- confirmado por parte;
- pendente;
- rejeitado por parte;
- responsabilidade não assumida;
- divergência.

A confirmação de um participante não deverá obrigar os demais.

# 1633. Execução compartilhada

A execução poderá ser:

- conjunta;
- distribuída;
- coordenada;
- delegada;
- dependente;
- independente.

O estado global deverá derivar dos estados necessários, sem apagar condições individuais.

# 1634. Saída de participante

Um participante poderá sair quando aplicável.

A saída deverá:

- remover responsabilidade futura;
- preservar ações anteriores;
- revisar dependências;
- revisar titularidade;
- proteger conteúdo privado;
- informar os demais participantes necessários;
- evitar exposição adicional.

# 1635. Delegação

A delegação deverá registrar:

- delegante;
- executor;
- autoridade;
- escopo;
- prazo;
- permissões;
- possibilidade de rejeição;
- responsabilidade residual;
- condição de conclusão.

Delegar execução não deverá transferir automaticamente titularidade ou decisão.

# 1636. Aceitação da delegação

O executor deverá poder:

- aceitar;
- rejeitar;
- solicitar esclarecimento;
- negociar prazo;
- limitar escopo;
- informar impedimento;
- transferir quando autorizado.

A atribuição silenciosa não deverá criar responsabilidade.

# 1637. Compartilhamento

O compartilhamento poderá abranger:

- formulação;
- estado;
- responsabilidade;
- prazo;
- dependência;
- bloqueio;
- resultado;
- evidência;
- atualização.

Cada campo deverá respeitar finalidade e minimização.

# 1638. Compartilhamento sensível

Passos sensíveis deverão exigir:

- finalidade específica;
- confirmação adequada;
- escopo mínimo;
- consumidor identificado;
- período;
- revogação;
- proteção visual;
- registro de acesso.

# 1639. Revogação de compartilhamento

A revogação deverá:

- interromper novos acessos;
- interromper novos usos;
- recompor recortes;
- notificar consumidores;
- acompanhar propagação;
- preservar obrigações legítimas;
- indicar pendências.

# 1640. Propagação

A propagação deverá fornecer às capacidades consumidoras apenas o necessário.

Exemplos:

```text
Objetivos:
evidência ou solicitação de revisão

Contexto Vivo:
mudança contextual observada

Eventos de Vida:
possível mudança relevante identificada

Oportunidades Ativas:
necessidade de meio compatível

Intervenções Contextuais:
ação, decisão ou revisão pendente

Experiências:
participação planejada ou realizada
```

# 1641. Responsabilidade das capacidades consumidoras

Cada capacidade deverá:

- validar o recorte;
- aplicar seu próprio contrato;
- não ampliar significado;
- não tratar solicitação como decisão;
- confirmar processamento;
- preservar finalidade;
- tratar revogação;
- registrar falhas.

# 1642. Prevenção de ciclos

Deverão ser evitados ciclos como:

```text
Objetivo gera Próximo Passo
→ Próximo Passo produz atualização
→ atualização recria o mesmo Próximo Passo
→ novas notificações duplicadas
```

A prevenção deverá utilizar:

- identificador;
- correlação;
- causalidade;
- origem;
- versão;
- idempotência;
- consumidor;
- finalidade.

# 1643. Duplicidade

Dois registros poderão ser considerados duplicados quando representarem:

- mesmo titular;
- mesma finalidade;
- mesmo movimento;
- mesmo resultado imediato;
- temporalidade compatível;
- mesma origem ou cadeia causal.

A similaridade textual isolada não deverá ser suficiente.

# 1644. Tratamento da duplicidade

A duplicidade poderá resultar em:

- unificação;
- relação;
- manutenção separada;
- cancelamento do duplicado;
- correção;
- contestação;
- solicitação de confirmação.

O tratamento deverá preservar histórico e responsabilidades.

# 1645. Idempotência

O reprocessamento da mesma entrada não deverá gerar:

- novo Próximo Passo;
- nova confirmação;
- nova prioridade;
- novo agendamento;
- nova conclusão;
- nova notificação;
- nova propagação material;
- nova responsabilidade.

# 1646. Ordenação

A capacidade deverá distinguir:

- ordem de proposição;
- ordem de confirmação;
- ordem planejada;
- ordem real de execução;
- ordem de processamento;
- ordem de conclusão;
- ordem de conhecimento.

Mensagens fora de ordem deverão ser reconciliadas.

# 1647. Concorrência

Alterações concorrentes deverão utilizar:

- versão esperada;
- comparação de estado;
- identificação do ator;
- temporalidade;
- conflito explícito;
- preservação de versões;
- resolução assistida quando necessária.

Sobrescritas silenciosas não deverão ocorrer.

# 1648. Retroatividade

Um passo poderá ser registrado após sua execução.

O registro deverá preservar:

- data da decisão, quando conhecida;
- data do início;
- data da conclusão;
- data do conhecimento pela Guivos;
- fonte;
- confiança;
- efeitos já ocorridos;
- limites da reconstrução.

# 1649. Passo executado sem registro anterior

Uma ação já realizada poderá gerar registro retroativo quando for útil para:

- explicar resultado;
- fornecer evidência;
- liberar dependência;
- registrar responsabilidade;
- preservar histórico;
- apoiar revisão de objetivo.

A capacidade não deverá criar retroativamente compromisso que não existiu.

# 1650. Mudança de contexto

Mudanças no Contexto Vivo poderão provocar:

- revisão de acionabilidade;
- repriorização;
- pausa;
- bloqueio;
- cancelamento;
- substituição;
- alteração de risco;
- revisão de temporalidade;
- necessidade de nova confirmação.

# 1651. Impacto de Evento de Vida

Quando um Evento de Vida afetar Próximos Passos, a capacidade deverá:

- identificar passos potencialmente afetados;
- avaliar individualmente;
- propor mudanças;
- evitar decisões em massa;
- preservar passos não afetados;
- explicar a relação;
- solicitar confirmação quando necessário.

# 1652. Evento de Vida crítico

Um Evento de Vida crítico poderá justificar:

- suspensão temporária;
- redução de notificações;
- revisão prioritária;
- proteção de sensibilidade;
- limitação de automações;
- retirada de cobranças;
- recomendação de apoio especializado.

Ele não deverá gerar automaticamente novos compromissos.

# 1653. Objetivo alterado

Quando um Objetivo for pausado, reformulado, concluído, retirado ou substituído, seus Próximos Passos deverão ser reavaliados.

Eles poderão:

- permanecer válidos;
- mudar de relação;
- ser pausados;
- ser concluídos;
- ser cancelados;
- ser substituídos;
- permanecer sem objetivo formal.

# 1654. Oportunidade indisponível

A indisponibilidade de uma oportunidade deverá levar à avaliação de:

- alternativa;
- adiamento;
- substituição;
- manutenção do passo;
- mudança de meio;
- expiração;
- cancelamento.

O Próximo Passo não deverá ser cancelado automaticamente quando puder ser realizado por outro meio.

# 1655. Falhas de processamento

Uma falha poderá ocorrer em:

- criação;
- confirmação;
- atualização;
- prioridade;
- agendamento;
- propagação;
- conclusão;
- cancelamento;
- revogação;
- sincronização;
- integração;
- notificação.

# 1656. Falha segura

Em caso de falha, a capacidade deverá:

- preservar o último estado válido;
- evitar falsa confirmação;
- evitar falsa conclusão;
- suspender automações críticas;
- registrar pendência;
- permitir tentativa posterior;
- oferecer alternativa manual;
- informar o participante quando relevante.

# 1657. Falha parcial

Quando apenas parte do processamento ocorrer, o sistema deverá distinguir:

- operação concluída;
- operação pendente;
- consumidores processados;
- consumidores pendentes;
- efeitos aplicados;
- efeitos não aplicados;
- necessidade de compensação.

Não deverá declarar sucesso integral.

# 1658. Sincronização divergente

Quando canais apresentarem estados diferentes, a capacidade deverá:

- preservar versões;
- identificar a mais recente;
- avaliar autoridade;
- impedir sobrescrita;
- indicar sincronização pendente;
- limitar decisões críticas;
- solicitar revisão quando necessário.

# 1659. Explicabilidade do ciclo

O participante deverá poder compreender:

- por que o passo foi proposto;
- quem o propôs;
- quem confirmou;
- por que está ativo;
- como a prioridade foi definida;
- quais dependências existem;
- por que está bloqueado;
- qual ação alterou seu estado;
- quais capacidades receberam recortes;
- como corrigir ou contestar;
- como cancelar, substituir ou arquivar.

# 1660. Histórico

O histórico deverá registrar:

- criação;
- propostas;
- formulações;
- confirmações;
- rejeições;
- prioridade;
- prontidão;
- agendamentos;
- dependências;
- bloqueios;
- pausas;
- retomadas;
- execução;
- resultados;
- conclusões;
- cancelamentos;
- substituições;
- expirações;
- contestações;
- correções;
- compartilhamentos;
- revogações;
- falhas.

# 1661. Retenção

A retenção deverá considerar:

- finalidade;
- sensibilidade;
- estado;
- obrigação legítima;
- dependências;
- histórico necessário;
- contestação;
- auditoria;
- controle do participante;
- exclusão aplicável.

Propostas rejeitadas poderão possuir retenção reduzida.

# 1662. Privacidade durante o ciclo

A capacidade deverá:

- utilizar títulos neutros;
- limitar notificações;
- ocultar detalhes sensíveis;
- proteger dispositivos compartilhados;
- minimizar terceiros;
- separar conteúdo pessoal e institucional;
- aplicar permissões por finalidade;
- respeitar revogação;
- evitar exposição em calendários públicos.

# 1663. Intervenções durante o ciclo

A Capacidade 05 poderá solicitar à Capacidade 07:

- confirmação;
- lembrete;
- revisão;
- esclarecimento;
- alerta de prazo;
- aviso de bloqueio;
- proposta de alternativa;
- redução de carga;
- silêncio.

A Capacidade 07 deverá decidir a forma, o momento e o canal.

# 1664. Prevenção de fadiga

A capacidade deverá evitar:

- notificações repetidas;
- perguntas já respondidas;
- múltiplas revisões simultâneas;
- cobrança por atraso;
- excesso de passos ativos;
- fragmentação artificial;
- alertas para propostas não confirmadas;
- gamificação coercitiva;
- comparação com outros participantes.

# 1665. Métricas iniciais do ciclo

O ciclo poderá acompanhar:

- propostas criadas;
- propostas rejeitadas;
- confirmações;
- reformulações;
- passos prontos;
- bloqueios;
- tempo bloqueado;
- pausas;
- retomadas;
- conclusões;
- cancelamentos;
- substituições;
- expirações;
- contestações;
- correções;
- duplicidades;
- falhas;
- esforço de confirmação;
- notificações evitadas.

As métricas deverão avaliar a capacidade, não o participante.

# 1666. Eventos funcionais do ciclo

A capacidade poderá produzir:

- `PossivelProximoPassoIdentificado`;
- `ProximoPassoFormulado`;
- `ProximoPassoProposto`;
- `ProximoPassoRejeitado`;
- `ProximoPassoConfirmado`;
- `ConfirmacaoDeProximoPassoCondicionada`;
- `ProximoPassoReformulado`;
- `ProximoPassoDesdobrado`;
- `ProximosPassosUnificados`;
- `ProximoPassoAtivado`;
- `ProntidaoDeProximoPassoAvaliada`;
- `ProximoPassoPreparado`;
- `ProximoPassoPriorizado`;
- `PrioridadeDeProximoPassoAlterada`;
- `SequenciaDeProximosPassosDefinida`;
- `DependenciaDeProximoPassoRegistrada`;
- `DependenciaDeProximoPassoAtendida`;
- `DependenciaDeProximoPassoDispensada`;
- `ProximoPassoBloqueado`;
- `ProximoPassoDesbloqueado`;
- `ProximoPassoPausado`;
- `ProximoPassoRetomado`;
- `ProximoPassoAgendado`;
- `AgendamentoDeProximoPassoAlterado`;
- `ProximoPassoAdiado`;
- `ProximoPassoIniciado`;
- `ProximoPassoAtualizado`;
- `ResultadoDeProximoPassoRegistrado`;
- `ProximoPassoConcluido`;
- `ProximoPassoConcluidoParcialmente`;
- `ProximoPassoCancelado`;
- `ProximoPassoSubstituido`;
- `ProximoPassoExpirado`;
- `ProximoPassoContestado`;
- `ContestacaoDeProximoPassoResolvida`;
- `ProximoPassoCorrigido`;
- `ProximoPassoReaberto`;
- `ProximoPassoArquivado`;
- `RecorrenciaDeProximoPassoCriada`;
- `OcorrenciaDeProximoPassoRegistrada`;
- `RecorrenciaDeProximoPassoPausada`;
- `RecorrenciaDeProximoPassoEncerrada`;
- `ResponsabilidadeDeProximoPassoDelegada`;
- `DelegacaoDeProximoPassoAceita`;
- `DelegacaoDeProximoPassoRejeitada`;
- `CompartilhamentoDeProximoPassoAutorizado`;
- `CompartilhamentoDeProximoPassoRevogado`;
- `RecorteDeProximoPassoPropagado`;
- `PropagacaoDeProximoPassoFalhou`;
- `SincronizacaoDeProximoPassoPendente`;
- `SincronizacaoDeProximoPassoConcluida`.

# 1667. Transições válidas principais

| Origem | Destino possível |
|---|---|
| Proposto | Confirmado, Rejeitado, Reformulado, Arquivado |
| Confirmado | Pronto, Agendado, Bloqueado, Pausado, Cancelado, Substituído |
| Pronto | Agendado, Em andamento, Bloqueado, Pausado, Cancelado |
| Agendado | Em andamento, Adiado, Bloqueado, Pausado, Cancelado, Expirado |
| Em andamento | Concluído, Bloqueado, Pausado, Cancelado, Substituído, Contestado |
| Bloqueado | Confirmado, Pronto, Agendado, Em andamento, Pausado, Cancelado |
| Pausado | Confirmado, Pronto, Agendado, Em andamento, Cancelado, Substituído |
| Concluído | Contestado, Corrigido, Reaberto, Arquivado |
| Cancelado | Contestado, Corrigido, Reaberto, Arquivado |
| Substituído | Contestado, Corrigido, Arquivado |
| Expirado | Reaberto, Substituído, Cancelado, Arquivado |
| Contestado | Estado anterior corrigido, mantido ou substituído |
| Corrigido | Estado funcional resultante da correção |
| Arquivado | Reaberto quando houver fundamento |

# 1668. Transições condicionadas

Deverão exigir validação adicional:

- proposta para confirmação em passo sensível;
- confirmação para ativação com risco elevado;
- prontidão para início com autorização pendente;
- bloqueado para em andamento sem resolução do bloqueio;
- contestado para concluído;
- cancelado para reaberto;
- expirado para reaberto;
- arquivado para ativo;
- correção com efeitos propagados;
- delegação com responsabilidade externa.

# 1669. Transições proibidas

Não deverão ocorrer automaticamente:

- Proposto → Em andamento;
- Proposto → Concluído;
- Confirmado → Concluído sem execução ou base compatível;
- Bloqueado → Concluído pela mera passagem do tempo;
- Pausado → Cancelado por inatividade;
- Agendado → Concluído pela data;
- Rejeitado → Confirmado sem nova decisão;
- Expirado → Em andamento sem revalidação;
- Contestado → Arquivado para ocultar divergência;
- compra → conclusão de Próximo Passo pessoal;
- recomendação → confirmação;
- oportunidade disponível → ativação.

# 1670. Critérios funcionais de aceite

O ciclo de vida será considerado adequadamente definido quando:

1. distinguir proposta, confirmação, ativação, prontidão, agendamento e execução;
2. preservar estado funcional e estado da informação;
3. permitir rejeição sem penalidade;
4. suportar confirmação simples, condicionada, parcial e compartilhada;
5. representar alternativas;
6. permitir reformulação, desdobramento e unificação;
7. governar prioridade separadamente do estado;
8. representar sequenciamento;
9. possuir dependências e bloqueios próprios;
10. distinguir pausa de bloqueio;
11. representar agendamento, prazo e adiamento;
12. definir início e acompanhamento proporcional;
13. separar execução, resultado, progresso e conclusão;
14. tratar conclusão parcial;
15. suportar cancelamento, substituição e expiração;
16. permitir contestação, correção e reabertura;
17. suportar recorrência sem julgamento;
18. suportar passos compartilhados e delegação;
19. governar compartilhamento e revogação;
20. propagar somente recortes mínimos;
21. impedir ciclos, duplicidades e efeitos repetidos;
22. tratar retroatividade;
23. reagir a Contexto Vivo, Objetivos e Eventos de Vida;
24. operar com falha segura;
25. preservar explicabilidade e histórico;
26. evitar fadiga;
27. proteger passos sensíveis;
28. manter o participante no controle.

# 1671. Regras fundamentais do ciclo de vida

1. Possibilidade não equivale a proposta.
2. Proposta não equivale a decisão.
3. Confirmação não equivale a ativação.
4. Ativação não equivale a prontidão.
5. Prontidão não equivale a início.
6. Agendamento não equivale a execução.
7. Execução não equivale a resultado esperado.
8. Resultado não equivale a progresso.
9. Conclusão do passo não conclui o objetivo.
10. Prioridade é dimensão separada do estado.
11. Urgência não determina prioridade universalmente.
12. Prazo vencido não representa fracasso.
13. Ausência de atualização não representa abandono.
14. Rejeição não gera penalidade.
15. Ausência de resposta não representa confirmação.
16. Bloqueio não representa incapacidade.
17. Pausa não representa fracasso.
18. Cancelamento não representa necessariamente desistência.
19. Substituição preserva relação com o passo anterior.
20. Expiração não deverá ser confundida com cancelamento.
21. Contestação limita efeitos críticos.
22. Correção preserva histórico.
23. Reabertura distingue continuidade de novo ciclo.
24. Recorrência não comprova hábito.
25. Ocorrência não realizada não mede disciplina pessoal.
26. Confirmação compartilhada é individual por papel.
27. Delegação não transfere titularidade.
28. Compartilhamento exige finalidade e minimização.
29. Revogação interrompe novos usos.
30. Recortes não transferem decisão às capacidades consumidoras.
31. Contexto Vivo informa realidade atual.
32. Objetivos governa direção e progresso.
33. Eventos de Vida informa mudanças relevantes.
34. Próximos Passos governa movimentos possíveis.
35. Oportunidades são meios, não decisões.
36. Intervenções governa quando e como a Guivos age.
37. Guivos Intelligence produz hipóteses e sugestões.
38. Platform Layer não redefine estados funcionais.
39. Reprocessamento não pode duplicar efeitos.
40. Mensagens fora de ordem não podem criar estados impossíveis.
41. Falha parcial não equivale a sucesso integral.
42. Vulnerabilidade não influencia prioridade comercial.
43. Receita ou patrocínio não altera o ciclo.
44. Passos sensíveis exigem proteção reforçada.
45. O ciclo deverá apoiar ação real, não maximizar engajamento.
46. O participante permanece no controle.

# 1672. Continuidade normativa

`PAS-001-PP-LIFECYCLE-001 1.0.0` deverá ser registrado como a **segunda extensão normativa da Capacidade 05 — Próximos Passos**.

Ele deverá:

- consolidar o ciclo de vida completo dos Próximos Passos;
- preservar a autoridade do `PAS-001-PP-FOUNDATION-001 1.0.0`;
- manter a Capacidade 05 no estado `In progress`;
- elevar o progresso editorial de referência para `40%`;
- preservar as Capacidades 02, 03 e 04 como `Functionally complete`;
- manter confirmação, ativação, prioridade, prontidão, execução, resultado e conclusão como dimensões distintas.

Com isso, ficam definidas as **regras do ciclo de vida da Capacidade de Próximos Passos**.

O próximo bloco deverá consolidar:

> **a visualização e o controle dos Próximos Passos, incluindo visão geral, portfólio ativo, cartões, detalhamento, propostas, alternativas, prioridade, prontidão, agenda, dependências, bloqueios, execução, resultados, recorrência, passos compartilhados, histórico, privacidade, acessibilidade, explicabilidade e ações do participante.**