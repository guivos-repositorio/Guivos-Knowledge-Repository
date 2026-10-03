---
id: PAS-001-CV-UPDATE-001
title: Regras de Atualização e Envelhecimento do Contexto Vivo
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-13
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-CV-STATE-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-CV-UPDATE-001 — Regras de Atualização e Envelhecimento do Contexto Vivo

## 1. Autoridade e vínculo

Este documento é uma **extensão normativa** do `PAS-001 — Guivos Journey Product Architecture Specification`, vinculada à `Capacidade 02 — Contexto Vivo`.

Seu conteúdo deve ser lido como continuidade funcional das seções 28 a 45 do `PAS-001 0.5.0` e das seções 46 a 59 do `PAS-001-CV-STATE-001 1.0.0`.

A separação documental preserva legibilidade e modularidade sem reduzir sua autoridade arquitetural.

# 60. Regras detalhadas de atualização e envelhecimento do Contexto Vivo

O Contexto Vivo deverá permanecer útil sem exigir que o participante reconstrua continuamente sua história.

Atualizar não significa substituir automaticamente uma informação anterior. Significa avaliar se uma nova entrada:

- confirma o que já era compreendido;
- complementa a representação;
- altera parte do contexto;
- encerra uma condição anterior;
- cria uma hipótese;
- identifica conflito;
- exige revisão;
- não possui relevância suficiente para integração.

> Nenhuma informação deverá ser considerada permanentemente atual apenas porque foi verdadeira em algum momento.

# 61. Unidade funcional de atualização

A unidade mínima de atualização será o **elemento contextual**, e não toda a dimensão.

Exemplo:

Na dimensão Restrições, o participante poderá possuir simultaneamente:

- disponibilidade reduzida durante a semana;
- orçamento limitado;
- mobilidade sem restrição;
- restrição temporária de saúde.

Uma alteração na disponibilidade não deverá reabrir ou modificar automaticamente os demais elementos.

Cada elemento contextual deverá preservar:

| Atributo | Função |
|---|---|
| Conteúdo | O que está sendo representado |
| Dimensão | Onde o elemento está organizado |
| Estado funcional | Sua condição atual |
| Origem | De onde veio |
| Tipo de origem | Declaração, integração, inferência ou evidência |
| Data de ocorrência | Quando aconteceu no mundo real |
| Data de registro | Quando entrou na Guivos |
| Início de validade | Quando passou a representar a realidade |
| Fim de validade | Quando deixou ou poderá deixar de valer |
| Última confirmação | Quando foi validado |
| Confiança | Força da compreensão |
| Sensibilidade | Nível de proteção necessário |
| Finalidade | Para que poderá ser utilizado |
| Permissão | Quais usos estão autorizados |
| Revisão prevista | Quando deverá ser reavaliado |
| Evidências relacionadas | O que sustenta a compreensão |
| Estado histórico | Como se relaciona com versões anteriores |

A dimensão poderá apresentar uma síntese, mas sua atualização deverá ocorrer sobre os elementos efetivamente afetados.

# 62. Gatilhos de atualização

Uma avaliação de atualização poderá ser iniciada por diferentes gatilhos.

## 62.1 Declaração direta

O participante informa uma mudança, correção ou nova condição.

Exemplos:

- “Mudei de emprego.”
- “Não quero mais priorizar esse objetivo.”
- “Agora só tenho disponibilidade aos sábados.”
- “Essa informação não está correta.”

Declarações explícitas deverão possuir prioridade sobre inferências conflitantes.

## 62.2 Confirmação

O participante confirma que uma informação ainda representa sua realidade.

A confirmação deverá:

- atualizar a data de confirmação;
- manter ou elevar a confiança;
- preservar o histórico anterior;
- recalcular a necessidade de próxima revisão.

## 62.3 Contestação

O participante rejeita uma compreensão existente.

A informação contestada deverá:

- deixar de orientar decisões de alto impacto;
- ser marcada como contestada;
- interromper inferências dependentes;
- permanecer disponível apenas para auditoria ou histórico, quando aplicável;
- gerar necessidade de correção ou remoção.

## 62.4 Evento de Vida

Uma mudança relevante poderá indicar que determinados elementos precisam ser atualizados.

Exemplo:

```text
Mudança de cidade
→ localização atual
→ disponibilidade territorial
→ relacionamentos locais
→ oportunidades próximas
```

O Evento de Vida deverá gerar uma avaliação das dimensões possivelmente afetadas, não a alteração automática de todas elas.

## 62.5 Experiência ou resultado

Uma experiência realizada poderá:

- fortalecer uma capacidade;
- alterar uma preferência;
- reduzir uma restrição;
- criar um relacionamento;
- gerar evidência de evolução;
- modificar uma direção.

A participação isolada não autoriza todas essas conclusões. Cada efeito deverá possuir evidência própria.

## 62.6 Integração autorizada

Uma fonte externa poderá enviar nova informação ou atualização.

O sistema deverá avaliar:

- validade da autorização;
- finalidade permitida;
- atualidade da fonte;
- compatibilidade com o contexto existente;
- necessidade de confirmação;
- qualidade da informação.

## 62.7 Sinal de interação

Comportamentos dentro da Guivos poderão criar uma hipótese de atualização.

Exemplo:

> A pessoa passou a salvar oportunidades relacionadas a ciclismo.

Esse sinal poderá gerar:

```text
Possível interesse em ciclismo
```

mas não:

```text
Preferência confirmada por ciclismo
```

## 62.8 Passagem do tempo

A passagem do tempo poderá alterar:

- atualidade;
- confiança;
- validade operacional;
- necessidade de revisão;
- possibilidade de utilização.

Ela não deverá transformar automaticamente uma informação verdadeira em falsa.

# 63. Fluxo funcional de atualização

Toda atualização relevante deverá seguir o fluxo:

```text
Nova entrada
→ validação de origem e autorização
→ identificação dos elementos afetados
→ comparação com o contexto vigente
→ análise de impacto e sensibilidade
→ decisão sobre necessidade de confirmação
→ atualização, hipótese, conflito ou descarte
→ preservação do histórico
→ geração de nova síntese contextual
→ comunicação proporcional ao participante
```

A atualização somente deverá ser aplicada quando houver base suficiente para determinar:

1. qual elemento será afetado;
2. qual mudança ocorreu;
3. desde quando a mudança vale;
4. qual é sua origem;
5. qual é seu nível de confiança;
6. quais finalidades estão autorizadas;
7. quais capacidades consumidoras poderão ser impactadas.

# 64. Resultados possíveis de uma avaliação

Uma nova entrada poderá produzir um dos seguintes resultados.

## 64.1 Confirmar

A nova informação reforça um elemento existente sem alterar seu significado principal.

## 64.2 Complementar

A nova informação adiciona detalhe relevante.

Exemplo:

```text
Preferência declarada: atividade esportiva coletiva
```

passa a conter:

```text
Preferência contextual: atividades coletivas aos finais de semana
```

## 64.3 Atualizar

O elemento continua existindo, mas alguma característica mudou.

Exemplo:

```text
Disponibilidade: noites durante a semana
```

torna-se:

```text
Disponibilidade: manhãs de sábado
```

## 64.4 Substituir

Uma nova informação passa a representar melhor a realidade atual.

A versão anterior deverá ser preservada como histórica ou substituída.

## 64.5 Encerrar

Uma condição deixou de existir.

Exemplo:

```text
Restrição temporária ativa
→ restrição resolvida
```

## 64.6 Suspender

O elemento permanece relevante, mas não deverá orientar ações temporariamente.

## 64.7 Criar hipótese

A entrada sugere uma possível mudança, mas não possui força suficiente para alterar o contexto vigente.

## 64.8 Identificar conflito

Duas ou mais informações incompatíveis precisam ser avaliadas.

## 64.9 Marcar para revisão

Não existe evidência de mudança, mas a atualidade deixou de ser suficiente.

## 64.10 Descartar

A entrada é irrelevante, duplicada, não autorizada, sem qualidade suficiente ou incompatível com a finalidade.

O descarte funcional não exige necessariamente eliminação imediata de registros técnicos de auditoria, quando sua preservação for legítima e necessária.

# 65. Confirmação proporcional ao impacto

Nem toda atualização exigirá confirmação explícita.

A necessidade de confirmação deverá considerar:

- sensibilidade;
- permanência;
- impacto sobre recomendações;
- impacto sobre acesso a oportunidades;
- possibilidade de prejuízo;
- confiança da origem;
- existência de evidências convergentes;
- reversibilidade da atualização.

## 65.1 Matriz funcional inicial

| Impacto | Sensibilidade | Exemplo | Regra |
|---|---|---|---|
| Baixo | Baixa | ajuste de preferência de formato | poderá ser atualizado com explicação e opção de correção |
| Médio | Baixa ou média | mudança de disponibilidade | confirmar quando afetar oportunidades relevantes |
| Alto | Qualquer | alteração de objetivo principal | confirmação explícita |
| Qualquer | Alta | saúde, religião, renda ou vulnerabilidade | confirmação proporcional e finalidade clara |
| Alto | Alta | restrição de saúde afetando experiências | confirmação explícita antes do uso decisório |
| Baixo | Inferência | possível interesse em novo tema | manter como hipótese |
| Alto | Inferência | possível mudança profissional ou financeira | não atualizar sem confirmação |

## 65.2 Atualização reversível

Mudanças de baixo impacto e facilmente reversíveis poderão ser aplicadas com transparência, desde que o participante consiga:

- visualizar;
- compreender;
- corrigir;
- desfazer;
- limitar o uso.

## 65.3 Atualização crítica

Uma atualização será crítica quando puder:

- excluir oportunidades relevantes;
- alterar prioridade principal;
- mudar a interpretação de uma restrição;
- modificar a forma de tratamento de informação sensível;
- afetar compartilhamento;
- gerar decisão de alto impacto.

Atualizações críticas não deverão ocorrer silenciosamente.

# 66. Regras conforme a origem

## 66.1 Declaração atual do participante

Deverá ser tratada como fonte prioritária sobre inferências anteriores.

Ainda assim, poderá exigir esclarecimento quando:

- estiver incompleta;
- for ambígua;
- conflitar com outra declaração atual;
- possuir impacto elevado;
- não indicar quando a mudança começou.

## 66.2 Declaração histórica

Não deverá ser tratada como vigente sem avaliação de atualidade.

## 66.3 Inferência da Intelligence Layer

Deverá ser registrada como hipótese ou compreensão proposta.

A inferência deverá possuir:

- evidências utilizadas;
- explicação;
- confiança;
- limites;
- dimensões afetadas;
- necessidade de confirmação.

## 66.4 Dados de integração

Não deverão prevalecer automaticamente sobre uma contestação do participante.

Exemplo:

Uma plataforma esportiva registra atividade de corrida. O participante informa que estava apenas acompanhando outra pessoa.

O registro externo permanece como atividade observada, mas não como preferência ou objetivo.

## 66.5 Informação organizacional

Dados fornecidos por uma organização poderão comprovar participação, conclusão ou vínculo, desde que autorizados.

A organização não deverá definir unilateralmente:

- identidade integral;
- objetivo pessoal;
- preferência;
- evolução subjetiva;
- valor da experiência para a pessoa.

## 66.6 Evidências convergentes

Múltiplas fontes compatíveis poderão elevar a confiança, mas não eliminar a necessidade de confirmação quando o impacto ou a sensibilidade exigirem.

# 67. Classes temporais da informação

Cada elemento deverá possuir uma classe temporal adequada.

## 67.1 Estrutural

Informação com tendência de maior estabilidade, mas ainda revisável.

Exemplos:

- formação concluída;
- experiência profissional anterior;
- certificação obtida;
- papel familiar histórico.

Informação estrutural não significa permanente nem imutável.

## 67.2 Semiestável

Pode permanecer válida por períodos longos, mas mudanças são possíveis.

Exemplos:

- área profissional;
- preferências de aprendizagem;
- rede de relacionamentos relevante;
- capacidades disponíveis.

## 67.3 Dinâmica

Pode mudar com frequência.

Exemplos:

- disponibilidade;
- prioridade;
- localização atual;
- orçamento disponível;
- interesse momentâneo.

## 67.4 Temporária

Possui duração limitada ou condição de encerramento esperada.

Exemplos:

- recuperação de saúde;
- viagem;
- curso em andamento;
- restrição de agenda;
- projeto específico.

## 67.5 Vinculada a evento

Sua validade depende de um Evento de Vida ou marco identificado.

Exemplo:

> A disponibilidade reduzida permanece enquanto durar determinado projeto.

## 67.6 Histórica

Representa algo verdadeiro no passado, mas que não deverá orientar automaticamente o contexto atual.

## 67.7 Sem temporalidade suficiente

Não existem informações adequadas para determinar se o elemento ainda é vigente.

# 68. Estados de atualidade e envelhecimento

O envelhecimento deverá representar perda de segurança temporal, não falsidade automática.

## 68.1 Atual

Existem evidências suficientes de que o elemento representa o contexto vigente.

## 68.2 Próximo de revisão

O elemento ainda pode ser utilizado, mas está se aproximando de seu horizonte de revisão.

## 68.3 Revisão recomendada

A informação poderá continuar sendo utilizada em atividades de baixo impacto, com cautela e indicação de incerteza.

## 68.4 Possivelmente envelhecida

A atualidade deixou de ser suficiente para orientar decisões relevantes.

## 68.5 Envelhecida

A informação não deverá orientar novas decisões sem confirmação ou evidência adicional.

## 68.6 Expirada

A validade conhecida terminou.

Uma informação expirada poderá permanecer no histórico, mas não no contexto vigente.

## 68.7 Substituída

Uma nova informação passou a representar a condição atual.

## 68.8 Arquivada

A informação deixou o contexto operacional e permanece somente para história, explicabilidade ou obrigações legítimas.

# 69. Horizonte de revisão

Não deverá existir um único prazo de validade para todas as informações.

O horizonte de revisão deverá considerar:

- dimensão;
- tipo de elemento;
- classe temporal;
- sensibilidade;
- origem;
- impacto;
- última confirmação;
- frequência histórica de mudança;
- condição de encerramento;
- finalidade de uso.

## 69.1 Exemplos iniciais

| Informação | Tendência de revisão |
|---|---|
| Objetivo principal | frequente ou após mudança relevante |
| Disponibilidade | frequente |
| Restrição temporária | próxima ao encerramento previsto |
| Preferência contextual | após sinais divergentes ou período relevante |
| Capacidade certificada | baixa frequência, salvo exigência de atualização |
| Localização atual | quando necessária para uma finalidade |
| Relacionamento ativo | quando sua relevância deixar de estar clara |
| Resultado histórico | não envelhece como fato histórico |
| Autorização temporária | expira na data definida |

Esses exemplos não definem prazos técnicos universais.

# 70. Regras de envelhecimento por dimensão

## 70.1 Identidade

Papéis ativos deverão ser revistos quando existirem sinais de transição, encerramento ou nova autodefinição.

Papéis históricos não deverão desaparecer, mas deixarão de orientar o contexto atual.

## 70.2 Momento

Deverá possuir revisão mais frequente, pois representa a condição atual predominante.

Eventos de Vida deverão reabrir sua avaliação.

## 70.3 Direção

Objetivos e prioridades exigirão revisão quando:

- não houver atividade por período relevante;
- ocorrer mudança de contexto;
- surgir objetivo concorrente;
- houver conclusão, suspensão ou abandono;
- a pessoa indicar perda de sentido.

## 70.4 Capacidades

Uma capacidade poderá permanecer no histórico, mesmo quando sua disponibilidade atual estiver incerta.

Deverão ser diferenciadas:

- existência da capacidade;
- nível atual;
- disponibilidade;
- evidência;
- atualização necessária.

## 70.5 Restrições

Restrições temporárias não deverão permanecer ativas indefinidamente.

O sistema deverá solicitar revisão quando:

- a data estimada de encerramento chegar;
- houver nova evidência;
- a restrição continuar bloqueando oportunidades;
- o participante apresentar comportamento incompatível.

## 70.6 Preferências

Preferências poderão envelhecer quando:

- forem antigas;
- existirem sinais recorrentes divergentes;
- o contexto de aplicação mudar;
- o participante explorar novas possibilidades.

Mudança comportamental isolada não será suficiente para substituir uma preferência declarada.

## 70.7 Relacionamentos

A ausência de interação não significa automaticamente encerramento.

O envelhecimento deverá afetar a confiança sobre a relevância atual, não declarar inexistência do vínculo.

## 70.8 Evolução

Evidências históricas de evolução não envelhecem como fatos ocorridos.

O que poderá envelhecer é a interpretação de que determinado progresso ainda representa a condição atual.

# 71. Revisões iniciadas pela Guivos

A Guivos poderá solicitar revisão quando:

- uma informação crítica estiver envelhecida;
- uma recomendação depender de informação incerta;
- um Evento de Vida indicar possível mudança;
- houver conflito;
- uma autorização estiver próxima de expirar;
- uma restrição temporária puder ter terminado;
- um objetivo permanecer sem atividade;
- um elemento estiver impedindo oportunidades relevantes.

A solicitação deverá ser:

- contextual;
- curta;
- explicável;
- proporcional;
- não repetitiva;
- adiável quando não houver risco;
- dispensável quando a informação não for necessária.

Exemplo:

> Você informou anteriormente que só podia participar de atividades aos sábados. Isso ainda representa sua disponibilidade?

# 72. Fadiga de confirmação

O sistema não deverá transformar controle em excesso de perguntas.

Para evitar fadiga:

1. informações relacionadas poderão ser revisadas em conjunto;
2. perguntas deverão ocorrer em momentos naturais da jornada;
3. revisões sem impacto imediato poderão ser adiadas;
4. informações não necessárias não deverão ser revalidadas;
5. o participante poderá definir preferências de revisão;
6. confirmações repetidas sem nova evidência deverão ser evitadas;
7. perguntas de alta prioridade deverão ser diferenciadas das opcionais.

A ausência de resposta não deverá ser interpretada como confirmação.

# 73. Atualizações silenciosas permitidas

Poderão ocorrer sem confirmação explícita:

- atualização da data de uma evidência observada;
- registro de histórico de interação;
- correção técnica sem alteração de significado;
- mudança automática de autorização quando uma data de expiração conhecida for alcançada;
- marcação de uma informação como próxima de revisão;
- redução de confiança temporal;
- arquivamento operacional após substituição confirmada;
- atualização reversível de baixo impacto, com transparência.

Essas mudanças deverão continuar auditáveis.

# 74. Atualizações silenciosas proibidas

Não deverão ocorrer silenciosamente:

- criação ou substituição de objetivo principal;
- atribuição de identidade relevante;
- criação de condição de saúde;
- inferência religiosa, política, financeira ou de vulnerabilidade;
- ativação de restrição que bloqueie oportunidades;
- alteração de autorização;
- ampliação de finalidade;
- compartilhamento com nova capacidade ou organização;
- conclusão de que houve evolução;
- encerramento de relacionamento relevante;
- alteração que possa causar prejuízo significativo.

# 75. Efeito das permissões sobre a atualização

Uma mudança de permissão deverá possuir efeito prioritário.

## 75.1 Revogação

Após revogação:

- novos usos deverão ser interrompidos;
- capacidades consumidoras deverão deixar de receber o elemento;
- inferências dependentes deverão ser reavaliadas;
- recortes contextuais deverão ser recompostos;
- dados técnicos deverão seguir as regras de retenção e exclusão aplicáveis.

## 75.2 Limitação de finalidade

A informação poderá permanecer válida para uma finalidade e indisponível para outra.

Exemplo:

> O participante permite utilizar sua localização aproximada para encontrar eventos, mas não para publicidade.

## 75.3 Não persistência

Informações de sessão temporária não deverão integrar o Contexto Vivo persistente.

## 75.4 Exclusão

A exclusão deverá considerar:

- direito do participante;
- obrigações legais;
- dependências;
- histórico mínimo necessário;
- impossibilidade de reconstrução indevida;
- retirada das capacidades consumidoras.

# 76. Propagação das atualizações

Uma atualização aceita deverá gerar uma análise de impacto.

```text
Elemento atualizado
→ dimensão principal
→ dimensões potencialmente relacionadas
→ capacidades consumidoras
→ oportunidades e ações em andamento
→ necessidade de nova decisão
```

A propagação deverá respeitar três regras:

1. **não presumir efeitos indiretos**;
2. **enviar somente o recorte necessário**;
3. **não reutilizar fora da finalidade autorizada**.

Exemplo:

Uma nova restrição de mobilidade poderá afetar oportunidades presenciais, mas não deverá alterar automaticamente objetivos, capacidades ou identidade.

# 77. Reprocessamento de decisões existentes

Quando uma atualização relevante ocorrer, o sistema deverá avaliar se existem:

- oportunidades ativas incompatíveis;
- Próximos Passos desatualizados;
- intervenções programadas;
- experiências em andamento;
- recomendações que perderam relevância;
- alertas que devem ser cancelados;
- novas possibilidades antes indisponíveis.

O Contexto Vivo não executará essas decisões, mas deverá informar às capacidades responsáveis que o contexto utilizado mudou.

# 78. Atualizações retroativas

Uma informação poderá ser registrada depois do momento em que aconteceu.

Exemplo:

> O participante informa hoje que mudou de emprego há dois meses.

O sistema deverá distinguir:

- data do fato;
- data em que foi informado;
- período em que o contexto anterior deixou de representar a realidade;
- decisões tomadas com a compreensão disponível à época.

A atualização retroativa não deverá reescrever silenciosamente a história como se a Guivos já soubesse da mudança.

# 79. Correção e mudança real

O sistema deverá distinguir:

## Correção

A informação anterior estava errada.

```text
Localização registrada incorretamente
→ informação corrigida
```

## Mudança real

A informação anterior estava correta, mas deixou de representar a realidade.

```text
Participante morava em Belo Horizonte
→ mudou-se para Lisboa
```

Na correção, o histórico deverá indicar erro.

Na mudança real, o histórico deverá preservar os dois estados e suas respectivas temporalidades.

# 80. Critérios de atualização confiável

Uma atualização será considerada funcionalmente confiável quando:

- possuir origem identificada;
- estiver autorizada;
- indicar o elemento afetado;
- diferenciar fato, evidência e inferência;
- possuir referência temporal;
- aplicar confirmação proporcional;
- preservar histórico;
- respeitar finalidade;
- não produzir impactos automáticos indevidos;
- permitir explicação ao participante;
- ser reversível quando aplicável;
- atualizar capacidades consumidoras de forma controlada.

# 81. Eventos funcionais relacionados

O processo poderá produzir eventos como:

- `AtualizacaoContextualProposta`;
- `AtualizacaoContextualAplicada`;
- `AtualizacaoContextualRejeitada`;
- `ConfirmacaoSolicitada`;
- `InformacaoConfirmada`;
- `InformacaoContestada`;
- `InformacaoComplementada`;
- `InformacaoSubstituida`;
- `InformacaoEncerrada`;
- `InformacaoSuspensa`;
- `InformacaoProximaDeRevisao`;
- `InformacaoEnvelhecida`;
- `InformacaoExpirada`;
- `RevisaoAdiada`;
- `PermissaoRevogada`;
- `RecorteContextualRecomposto`;
- `CapacidadeConsumidoraNotificada`.

Esses eventos permanecem funcionais e não prescrevem tecnologia de mensageria.

# 82. Cenário exemplificativo

## Situação inicial

O participante informa:

- objetivo: melhorar a saúde;
- preferência: atividade coletiva;
- disponibilidade: sábado pela manhã;
- restrição: evitar atividades de alto impacto por três meses.

## Durante o período

A Guivos poderá recomendar:

- grupos de caminhada;
- pedal leve;
- atividades coletivas compatíveis;
- eventos aos sábados.

## Após três meses

A restrição se torna elegível para revisão.

A Guivos pergunta:

> A recomendação de evitar atividades de alto impacto ainda deve ser considerada?

### Caso o participante confirme

A restrição permanece ativa e recebe nova referência temporal.

### Caso informe que foi resolvida

A restrição passa para resolvida, e a capacidade de Oportunidades Ativas poderá reavaliar novas opções.

### Caso não responda

A restrição não será automaticamente removida. Ela poderá ser marcada como possivelmente envelhecida e deixar de orientar decisões de alto impacto até nova confirmação.

# 83. Regras fundamentais de envelhecimento

1. Tempo reduz certeza de atualidade, não prova falsidade.
2. Informações históricas permanecem verdadeiras em relação ao passado.
3. Elementos temporários exigem condição de revisão ou encerramento.
4. Ausência de resposta não equivale a confirmação.
5. Informação envelhecida não deverá orientar decisões críticas.
6. Revisões deverão ocorrer apenas quando houver finalidade real.
7. O participante deverá compreender por que uma atualização é solicitada.
8. Atualizações deverão ser seletivas.
9. Mudanças de autorização possuem prioridade sobre conveniência operacional.
10. O sistema deverá preservar o que sabia, quando sabia e por que atualizou.

Com isso, ficam especificadas as **regras detalhadas de atualização e envelhecimento do Contexto Vivo**.

O próximo bloco da Capacidade 02 é a **resolução detalhada de conflitos entre informações, interpretações, fontes e temporalidades**.
