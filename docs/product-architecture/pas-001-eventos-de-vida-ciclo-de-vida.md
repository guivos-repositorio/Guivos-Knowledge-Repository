---
id: PAS-001-EV-LIFECYCLE-001
title: Regras do Ciclo de Vida dos Eventos de Vida
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-EV-FOUNDATION-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-EV-LIFECYCLE-001 — Regras do Ciclo de Vida dos Eventos de Vida

## 1. Autoridade e vínculo

Este documento é a **segunda extensão normativa da Capacidade 04 — Eventos de Vida** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 885 a 956 de `PAS-001-EV-FOUNDATION-001 1.0.0` e da especificação-base `PAS-001 0.5.0`.

Esta extensão consolida identificação, proposição, confirmação, estados, temporalidade, relevância, impactos, relações, correção, contestação, encerramento e propagação dos Eventos de Vida.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade normativa da extensão anterior.

# 957. Ciclo de vida dos Eventos de Vida

O ciclo de vida deverá governar um Evento de Vida desde seu primeiro sinal até seu encerramento, arquivamento, correção ou reabertura.

Ele deverá preservar a sequência:

```text
sinal ou declaração
→ identificação
→ proposição
→ confirmação
→ acompanhamento
→ avaliação de impactos
→ propagação
→ encerramento
→ preservação histórica
```

> Reconhecer que uma mudança ocorreu não significa que todos os seus impactos já sejam conhecidos, confirmados ou aplicáveis.

# 958. Finalidades do ciclo de vida

O ciclo deverá permitir:

1. distinguir sinais de eventos reconhecidos;
2. representar eventos planejados, iniciados e concluídos;
3. preservar origem, autoridade e temporalidade;
4. confirmar eventos proporcionalmente ao impacto;
5. acompanhar mudanças progressivas;
6. avaliar relevância contextual;
7. identificar efeitos possíveis;
8. confirmar impactos individualmente;
9. relacionar eventos;
10. corrigir registros;
11. permitir contestação;
12. encerrar eventos sem apagar seus efeitos;
13. reabrir eventos quando necessário;
14. propagar mudanças com segurança;
15. preservar controle do participante.

# 959. Visão geral dos estados

O ciclo poderá utilizar os seguintes estados:

```text
Sinalizado
→ Proposto
→ Planejado
→ Confirmado
→ Iniciado
→ Em andamento
→ Concluído
```

Estados alternativos ou posteriores:

```text
Interrompido
Cancelado
Contestado
Corrigido
Arquivado
Reaberto
```

As transições não deverão ser obrigatoriamente lineares.

# 960. Estado do evento e estado da informação

A capacidade deverá distinguir:

## Estado do evento

Indica a condição da mudança na vida real.

Exemplos:

- planejado;
- iniciado;
- concluído;
- cancelado.

## Estado da informação

Indica a segurança com que a Guivos compreende o evento.

Exemplos:

- hipótese;
- não confirmado;
- confirmado;
- contestado;
- corrigido.

Um evento poderá estar concluído na vida real e ainda permanecer não confirmado na Guivos.

# 961. Entrada no ciclo de vida

Um possível Evento de Vida poderá entrar no ciclo por:

- declaração do participante;
- conversa;
- atualização do Contexto Vivo;
- experiência;
- integração autorizada;
- informação institucional;
- representante autorizado;
- documento;
- evento relacionado;
- sinal observado;
- hipótese da Guivos Intelligence;
- reconstrução retroativa.

A forma de entrada deverá determinar os efeitos inicialmente permitidos.

# 962. Identificação inicial

A identificação ocorre quando uma informação apresenta potencial suficiente para representar uma mudança relevante.

A capacidade deverá avaliar:

- existência de mudança;
- participante relacionado;
- período;
- origem;
- autoridade;
- possível relevância;
- sensibilidade;
- necessidade de confirmação;
- risco de associação incorreta.

A identificação não deverá significar confirmação.

# 963. Resultado da identificação

A avaliação inicial poderá resultar em:

- informação comum;
- atividade;
- experiência;
- atualização contextual;
- sinal de Evento de Vida;
- Evento de Vida proposto;
- Evento de Vida declarado;
- duplicidade;
- informação insuficiente;
- associação incerta;
- entrada rejeitada.

# 964. `Sinalizado`

O estado `Sinalizado` deverá representar informação que poderá indicar uma mudança, mas ainda não possui base suficiente para ser tratada como Evento de Vida.

Exemplos:

- alteração recorrente de localização;
- mudança de vínculo detectada por integração;
- ausência incomum;
- nova rotina;
- interrupção de atividades;
- comportamento incompatível com o contexto anterior.

Um sinal não deverá atualizar silenciosamente o Contexto Vivo.

# 965. Tratamento de sinais

Um sinal poderá:

- ser mantido temporariamente;
- ser relacionado a outros sinais;
- gerar pergunta;
- produzir proposta;
- ser descartado;
- ser classificado como irrelevante;
- permanecer sem ação.

Sinais sensíveis deverão possuir retenção reduzida e finalidade estrita.

# 966. Acúmulo de sinais

Múltiplos sinais convergentes poderão aumentar a confiança de que uma mudança ocorreu.

Ainda assim, a convergência não deverá:

- substituir autoridade;
- produzir diagnóstico;
- confirmar evento pessoal sensível;
- criar objetivo;
- impor prioridade;
- justificar compartilhamento externo.

# 967. Proposição do Evento de Vida

O estado `Proposto` deverá representar uma possível formulação do evento apresentada para avaliação.

Exemplo:

> Identificamos que sua situação profissional pode ter mudado. Você encerrou seu vínculo com a organização?

A proposta deverá informar:

- origem;
- fato ou sinais utilizados;
- período estimado;
- confiança;
- possíveis impactos;
- necessidade de confirmação;
- efeitos que poderão ocorrer.

# 968. Formulação do evento

A formulação deverá descrever a mudança de forma:

- objetiva;
- não valorativa;
- temporalmente situada;
- proporcional;
- compreensível;
- revisável;
- minimizada.

Exemplo adequado:

> Encerramento de vínculo profissional com a organização.

Exemplo inadequado:

> Fracasso profissional e perda de estabilidade.

# 969. Preservação da expressão original

Quando o evento for declarado, a capacidade deverá preservar:

- expressão original;
- formulação funcional;
- data da declaração;
- significado atribuído;
- correções posteriores.

A formulação funcional não deverá substituir o relato do participante.

# 970. Duplicidade na proposição

Antes de criar novo evento, a capacidade deverá verificar:

- eventos semelhantes;
- período;
- titular;
- origem;
- participantes relacionados;
- transição representada;
- eventos compostos existentes.

A existência de eventos semelhantes poderá resultar em:

- atualização;
- relação;
- unificação;
- novo evento independente;
- rejeição por duplicidade.

# 971. Associação incerta

Quando não houver segurança sobre o participante ou evento correto, a entrada deverá permanecer pendente.

A capacidade não deverá:

- associar por aproximação;
- expor informação a outro participante;
- atualizar contexto;
- alterar objetivos;
- produzir notificação sensível;
- confirmar o evento.

# 972. Autoridade na proposição

Uma fonte poderá propor Evento de Vida mesmo quando não possuir autoridade para confirmá-lo integralmente.

Exemplo:

```text
Fonte:
aplicativo de localização

Pode propor:
possível mudança de residência

Não pode confirmar:
mudança permanente, motivação ou impacto familiar
```

# 973. Evento declarado

Quando o participante declarar diretamente uma mudança pessoal, o evento poderá ser admitido como declarado.

A declaração deverá ser suficiente para fatos pessoais que não dependam de comprovação externa, salvo quando:

- houver conflito relevante;
- a finalidade exigir confirmação institucional;
- houver risco para terceiros;
- existir obrigação legal;
- o evento possuir consequência institucional específica.

# 974. Evento informado por terceiro

Um terceiro somente poderá informar evento quando possuir:

- relação legítima;
- finalidade;
- autorização ou base adequada;
- autoridade compatível;
- identificação suficiente.

A informação deverá permanecer limitada ao que o terceiro pode afirmar.

# 975. Evento integrado

Um evento recebido por integração deverá preservar:

- sistema de origem;
- identificador externo;
- contrato;
- participante;
- autoridade;
- data do fato;
- data de recebimento;
- transformação aplicada;
- confiança;
- permissões.

A disponibilidade técnica da informação não deverá ampliar sua autoridade.

# 976. Evento inferido

Eventos inferidos deverão permanecer como hipótese ou proposta.

A inferência deverá indicar:

- sinais utilizados;
- método funcional;
- confiança;
- possíveis explicações alternativas;
- limitações;
- necessidade de confirmação;
- efeitos proibidos antes da confirmação.

# 977. Confirmação do Evento de Vida

A confirmação deverá reconhecer que a mudança representada ocorreu, está ocorrendo ou está legitimamente planejada.

A confirmação deverá abranger:

- identidade do evento;
- titular;
- formulação;
- temporalidade;
- natureza;
- origem;
- escopo.

A confirmação do evento não deverá confirmar automaticamente todos os impactos.

# 978. Formas de confirmação

Um evento poderá ser confirmado por:

- participante;
- representante autorizado;
- organização competente;
- fonte institucional;
- documento;
- integração autorizada;
- evidências convergentes, quando permitido;
- combinação de fontes.

A forma deverá permanecer visível.

# 979. Confirmação proporcional

A confirmação poderá ser:

## Direta

O participante confirma explicitamente.

## Institucional

Uma fonte competente confirma o fato sob seu escopo.

## Assistida

A Guivos apresenta uma formulação e o participante ajusta ou confirma.

## Automática autorizada

Permitida apenas quando:

- o fato for objetivo;
- a fonte possuir autoridade;
- a finalidade estiver autorizada;
- o impacto for reversível;
- não houver conflito;
- não houver sensibilidade incompatível.

# 980. Confirmação parcial

O participante poderá confirmar parte do evento.

Exemplo:

```text
Confirmado:
mudança de cidade

Ainda não confirmado:
caráter permanente da mudança
```

A capacidade deverá preservar os elementos pendentes separadamente.

# 981. Ausência de confirmação

Quando o participante não responder, a capacidade poderá:

- manter como proposta;
- adiar;
- reduzir uso;
- manter apenas como sinal;
- descartar após período adequado;
- solicitar confirmação em momento mais apropriado.

Ausência de resposta não deverá ser tratada como confirmação ou rejeição definitiva.

# 982. Rejeição da proposta

O participante poderá indicar:

- evento não ocorreu;
- formulação incorreta;
- pessoa errada;
- período incorreto;
- informação sensível demais;
- não deseja registrar;
- prefere manter temporário.

A rejeição deverá interromper efeitos derivados não confirmados.

# 983. `Planejado`

O estado `Planejado` representa mudança futura reconhecida como intenção concreta, compromisso ou ocorrência prevista.

Exemplos:

- mudança de residência marcada;
- casamento agendado;
- início de curso confirmado;
- encerramento organizacional previsto.

O estado deverá possuir:

- data ou período estimado;
- confiança da previsão;
- fonte;
- condições;
- possibilidade de cancelamento;
- impactos preparatórios autorizados.

# 984. Efeitos de evento planejado

Um evento planejado poderá:

- gerar preparação;
- solicitar revisão futura;
- alterar recomendações temporais;
- reservar capacidade;
- informar risco;
- apoiar Próximos Passos.

Ele não deverá:

- atualizar estado final;
- concluir transição;
- comprovar resultado;
- aplicar todos os impactos posteriores.

# 985. `Confirmado`

O estado `Confirmado` indica que a existência ou previsão do evento foi reconhecida, mas a mudança poderá ainda não ter iniciado.

Exemplo:

> Contratação confirmada com início previsto para o próximo mês.

# 986. `Iniciado`

O estado `Iniciado` indica que a transição começou.

O início deverá possuir:

- data;
- evidência ou declaração;
- condição inicial;
- impactos já observados;
- aspectos ainda pendentes.

# 987. `Em andamento`

O estado `Em andamento` deverá ser utilizado para eventos progressivos ou transições que ainda produzem mudanças.

Exemplos:

- mudança de país;
- tratamento informado;
- processo de separação;
- reestruturação organizacional;
- transição de carreira.

A capacidade deverá permitir atualizações sem criar novo evento para cada etapa.

# 988. Atualização de evento em andamento

Uma atualização poderá registrar:

- novo marco;
- alteração de previsão;
- aumento ou redução de impacto;
- mudança de participantes;
- nova evidência;
- interrupção;
- extensão;
- mudança de significado;
- conclusão parcial.

# 989. `Concluído`

O estado `Concluído` indica que a mudança representada atingiu seu encerramento funcional.

Exemplos:

- mudança residencial finalizada;
- formação concluída;
- desligamento efetivado;
- reestruturação encerrada.

A conclusão do evento não significa que seus impactos terminaram.

# 990. Evento concluído com impactos contínuos

Um evento poderá estar concluído enquanto seus efeitos permanecem ativos.

Exemplo:

```text
Evento:
mudança para outro país

Estado:
concluído

Impactos ainda ativos:
adaptação cultural, documentação, rede de apoio e carreira
```

Evento e impactos deverão possuir temporalidades independentes.

# 991. `Interrompido`

Um evento em andamento poderá ser interrompido antes de sua conclusão.

A interrupção deverá indicar:

- momento;
- motivo, quando informado;
- efeitos já produzidos;
- condição atual;
- possibilidade de retomada;
- impactos pendentes.

# 992. `Cancelado`

O estado `Cancelado` deverá ser utilizado para evento planejado que deixou de ocorrer.

O cancelamento deverá:

- preservar o planejamento;
- cancelar efeitos preparatórios inadequados;
- reavaliar decisões dependentes;
- distinguir cancelamento de adiamento;
- evitar linguagem de fracasso.

# 993. Adiamento

Um evento planejado poderá ser adiado sem ser cancelado.

O adiamento deverá atualizar:

- previsão;
- confiança;
- impactos temporais;
- Próximos Passos;
- oportunidades dependentes;
- revisão futura.

# 994. `Contestado`

O estado `Contestado` deverá indicar questionamento sobre:

- existência;
- formulação;
- titularidade;
- temporalidade;
- origem;
- impacto;
- participantes relacionados;
- uso;
- compartilhamento.

O evento contestado não deverá ser apagado imediatamente.

# 995. `Corrigido`

O estado ou marcação `Corrigido` deverá indicar que parte material do registro anterior foi substituída por informação reconhecida como mais adequada.

A correção deverá preservar:

- versão anterior;
- elemento incorreto;
- nova informação;
- origem da correção;
- data;
- efeitos derivados;
- consumidores notificados.

# 996. `Arquivado`

O arquivamento deverá retirar o evento da operação cotidiana, preservando-o para:

- histórico;
- explicação;
- auditoria;
- evolução;
- consulta autorizada.

Arquivar não deverá eliminar impactos ainda ativos.

# 997. Transições válidas

Exemplos de transições válidas:

```text
Sinalizado → Proposto
Proposto → Confirmado
Proposto → Rejeitado
Planejado → Iniciado
Planejado → Adiado
Planejado → Cancelado
Iniciado → Em andamento
Em andamento → Concluído
Em andamento → Interrompido
Concluído → Arquivado
Concluído → Contestado
Arquivado → Reaberto
```

# 998. Transições inválidas ou condicionadas

Não deverão ocorrer silenciosamente:

- `Sinalizado → Concluído`;
- `Proposto → Em andamento` sem reconhecimento suficiente;
- `Planejado → Concluído` sem confirmação da ocorrência;
- `Contestado → Confirmado` sem tratamento;
- `Cancelado → Concluído` sem reabertura;
- `Arquivado → Em andamento` sem novo ciclo ou reativação.

# 999. Temporalidade do evento

Cada evento deverá distinguir, quando aplicável:

- data do fato;
- início;
- término;
- previsão;
- duração;
- data de conhecimento;
- data de declaração;
- data de confirmação;
- data de atualização;
- período de impacto;
- data de arquivamento.

# 1000. Data exata, aproximada e desconhecida

A temporalidade poderá ser:

- exata;
- aproximada;
- por mês;
- por período;
- relativa;
- ainda desconhecida.

Exemplos:

```text
Exata:
14/07/2026

Aproximada:
início de julho de 2026

Período:
entre março e maio de 2026

Desconhecida:
ocorreu anteriormente, sem data definida
```

A capacidade não deverá fabricar precisão.

# 1001. Evento retroativo

Quando a Guivos conhecer posteriormente um evento passado, deverá registrar:

- data real ou estimada do fato;
- data de conhecimento;
- data de confirmação;
- impactos históricos;
- decisões tomadas sem a informação;
- reavaliações possíveis;
- limites da reconstrução.

# 1002. Evento de duração indeterminada

Eventos progressivos poderão não possuir término conhecido.

A capacidade deverá permitir:

- duração aberta;
- revisões;
- atualização de estado;
- impactos variáveis;
- ausência de pressão por encerramento artificial.

# 1003. Relevância funcional

A relevância deverá representar a possibilidade de o evento alterar materialmente a jornada.

Ela deverá ser avaliada separadamente de:

- intensidade emocional;
- gravidade universal;
- popularidade;
- valor comercial;
- quantidade de informações disponíveis.

# 1004. Fatores de relevância

A avaliação poderá considerar:

- percepção do participante;
- dimensões afetadas;
- objetivos afetados;
- decisões dependentes;
- duração;
- reversibilidade;
- urgência;
- sensibilidade;
- risco;
- número de participantes;
- mudança de disponibilidade;
- mudança de restrições;
- necessidade de apoio.

# 1005. Níveis de relevância

A relevância poderá ser:

- não material;
- baixa;
- moderada;
- alta;
- crítica;
- indeterminada.

O nível deverá possuir justificativa explicável.

# 1006. Relevância não permanente

A relevância poderá mudar.

Um evento inicialmente considerado de baixo impacto poderá tornar-se relevante em razão de:

- efeitos posteriores;
- novo objetivo;
- mudança contextual;
- repetição;
- relação com outro evento;
- ampliação de duração;
- nova percepção do participante.

# 1007. Evento não material

Uma ocorrência poderá deixar de ser tratada como Evento de Vida quando:

- não houver mudança relevante;
- representar apenas atividade;
- tiver impacto pontual irrelevante;
- não possuir relação útil com a jornada;
- o participante não reconhecer relevância;
- o custo de registro superar o benefício.

# 1008. Impacto funcional

Impacto é a alteração confirmada ou possível produzida pelo evento sobre outra unidade funcional.

O impacto poderá afetar:

- Contexto Vivo;
- objetivos;
- prioridades;
- critérios;
- restrições;
- capacidades;
- relacionamentos;
- Próximos Passos;
- oportunidades;
- intervenções;
- experiências;
- evolução;
- permissões.

# 1009. Impacto proposto

Um impacto proposto representa uma possível consequência ainda não reconhecida.

Exemplo:

> Seu novo trabalho poderá reduzir sua disponibilidade para o objetivo de formação. Deseja revisar essa condição?

A proposta não deverá atualizar silenciosamente a unidade afetada.

# 1010. Impacto confirmado

Um impacto poderá ser confirmado por:

- declaração;
- atualização contextual;
- evidência;
- fonte autorizada;
- confirmação de capacidade responsável;
- combinação proporcional de informações.

A capacidade proprietária da unidade afetada deverá aplicar a alteração por seus próprios contratos.

# 1011. Intensidade do impacto

O impacto poderá ser:

- inexistente;
- baixo;
- moderado;
- alto;
- crítico;
- indeterminado.

A intensidade deverá considerar:

- extensão;
- duração;
- reversibilidade;
- urgência;
- risco;
- quantidade de decisões afetadas;
- percepção do participante.

# 1012. Impactos positivos, negativos e ambivalentes

A capacidade poderá registrar a percepção de impacto como:

- favorável;
- desfavorável;
- ambivalente;
- neutra;
- não avaliada.

A classificação não deverá ser imposta pela Guivos.

# 1013. Impacto automático permitido

Uma atualização automática poderá ocorrer somente quando:

- for objetiva;
- possuir fonte autorizada;
- tiver baixo risco;
- for reversível;
- estiver dentro da finalidade;
- não envolver interpretação pessoal;
- não existir conflito;
- a capacidade receptora permitir.

# 1014. Impactos automáticos proibidos

Não deverão ocorrer automaticamente:

- criação de objetivo pessoal;
- ativação de objetivo;
- imposição de prioridade;
- conclusão de objetivo qualitativo;
- diagnóstico;
- mudança de valor ou identidade;
- alteração de relacionamento sensível;
- compartilhamento externo;
- publicidade baseada em vulnerabilidade.

# 1015. Impactos sobre o Contexto Vivo

O evento poderá propor atualização de:

- Identidade;
- Momento;
- Direção;
- Capacidades;
- Restrições;
- Preferências;
- Relacionamentos;
- Evolução.

O Contexto Vivo deverá decidir:

- admitir;
- confirmar;
- contestar;
- limitar;
- rejeitar;
- envelhecer;
- solicitar informação adicional.

# 1016. Impactos sobre Objetivos

A capacidade poderá informar:

- objetivo potencialmente afetado;
- possível mudança de prioridade;
- necessidade de revisão;
- bloqueio;
- desbloqueio;
- alteração de horizonte;
- conflito;
- critério possivelmente inadequado;
- conclusão potencial;
- retirada possível.

A Capacidade de Objetivos deverá governar a decisão final.

# 1017. Impactos sobre Próximos Passos

Um evento poderá exigir que Próximos Passos sejam:

- mantidos;
- reordenados;
- suspensos;
- cancelados;
- substituídos;
- criados;
- adiados;
- reavaliados.

A Capacidade 04 não deverá gerenciar o ciclo completo dessas ações.

# 1018. Impactos sobre Oportunidades Ativas

O evento poderá alterar:

- elegibilidade;
- localização;
- disponibilidade;
- prazo;
- segurança;
- necessidade;
- relevância;
- acionabilidade.

Oportunidades comerciais não deverão explorar Eventos de Vida sensíveis.

# 1019. Impactos sobre Intervenções Contextuais

O evento poderá aumentar ou reduzir a necessidade de:

- perguntar;
- orientar;
- lembrar;
- alertar;
- acompanhar;
- esperar;
- permanecer em silêncio.

Um evento crítico não deverá gerar automaticamente comunicação invasiva.

# 1020. Impactos sobre Experiências

O evento poderá:

- iniciar experiência;
- interromper experiência;
- alterar participação;
- produzir resultado;
- transformar significado;
- exigir adaptação.

A experiência deverá permanecer uma unidade distinta.

# 1021. Impactos sobre Evolução Contínua

Eventos poderão servir como marcos temporais para compreender:

- transições;
- ciclos;
- mudanças sustentadas;
- surgimento de capacidades;
- novas restrições;
- adaptação;
- continuidade.

A capacidade não deverá classificar automaticamente o evento como evolução positiva ou negativa.

# 1022. Múltiplos impactos

Um único evento poderá produzir impactos diferentes em várias dimensões.

Cada impacto deverá possuir:

- unidade afetada;
- tipo;
- intensidade;
- temporalidade;
- confiança;
- origem;
- estado de confirmação;
- consumidor responsável.

# 1023. Impactos conflitantes

Um evento poderá produzir efeitos simultaneamente favoráveis e desfavoráveis.

Exemplo:

```text
Evento:
promoção profissional

Impactos:
+ aumento de renda
+ desenvolvimento de capacidade
- redução de disponibilidade
- aumento de deslocamento
```

A Guivos deverá preservar a ambivalência.

# 1024. Relações entre eventos

Eventos poderão estar relacionados por:

- causalidade;
- consequência;
- precedência;
- composição;
- correlação;
- dependência;
- substituição;
- reversão;
- agravamento;
- redução;
- simultaneidade.

# 1025. Causalidade e correlação

A proximidade temporal não deverá ser suficiente para declarar causalidade.

A capacidade deverá diferenciar:

```text
Relacionado temporalmente
```

de:

```text
Causado por
```

A causalidade deverá possuir base explicável.

# 1026. Cadeias de eventos

Uma mudança poderá originar sequência de eventos.

Exemplo:

```text
desligamento
→ mudança de renda
→ mudança de residência
→ início de nova formação
→ contratação
```

Cada evento deverá permanecer identificável quando possuir significado e impactos próprios.

# 1027. Evento composto

Um evento composto poderá organizar uma transição ampla.

Exemplo:

```text
Transição internacional

Componentes:
- encerramento de vínculo;
- mudança residencial;
- imigração;
- início de trabalho;
- criação de nova rede de apoio.
```

O evento composto não deverá apagar os componentes.

# 1028. Eventos simultâneos

Eventos simultâneos deverão ser tratados sem:

- perguntas excessivas;
- propagação repetida;
- notificações fragmentadas;
- seleção arbitrária de um único evento;
- perda de impactos cruzados.

Revisões compatíveis poderão ser agrupadas.

# 1029. Unificação de eventos duplicados

Eventos duplicados poderão ser unificados quando representarem a mesma mudança.

A unificação deverá preservar:

- identificadores anteriores;
- fontes;
- temporalidades;
- evidências;
- versões;
- efeitos já produzidos;
- correções.

# 1030. Separação de evento

Um evento poderá ser dividido quando sua formulação reunir mudanças funcionalmente independentes.

Exemplo:

```text
Evento original:
mudança profissional e residencial

Eventos resultantes:
- encerramento de vínculo;
- mudança de residência.
```

As relações entre os eventos resultantes deverão ser preservadas.

# 1031. Correção

Uma correção deverá ocorrer quando o registro não representar adequadamente o fato conhecido.

Poderá corrigir:

- titular;
- tipo;
- descrição;
- data;
- origem;
- participantes;
- estado;
- relevância;
- impacto;
- relação.

# 1032. Correção e mudança real

A capacidade deverá distinguir:

## Correção

O registro anterior estava incorreto.

## Mudança real

O evento evoluiu após o registro correto.

Exemplo:

```text
Correção:
a mudança ocorreu em maio, não junho.

Mudança real:
a mudança antes temporária tornou-se permanente.
```

# 1033. Efeitos da correção

Uma correção deverá:

- preservar o registro anterior;
- indicar o elemento corrigido;
- recompor impactos;
- reavaliar decisões;
- notificar consumidores necessários;
- evitar duplicidade;
- permitir auditoria.

# 1034. Contestação

O participante deverá poder contestar:

- classificação como Evento de Vida;
- formulação;
- origem;
- autoridade;
- temporalidade;
- titularidade;
- sensibilidade;
- relevância;
- impacto;
- relação;
- compartilhamento;
- uso.

# 1035. Efeitos da contestação

A contestação deverá, conforme o risco:

- suspender impactos;
- limitar recortes;
- interromper novos usos;
- reduzir confiança;
- solicitar revisão;
- preservar o registro;
- notificar capacidades dependentes;
- impedir decisão crítica.

# 1036. Tratamento da contestação

O tratamento poderá resultar em:

- confirmação do registro;
- correção;
- remoção de impacto;
- alteração de relevância;
- separação de eventos;
- arquivamento;
- retirada de uso;
- exclusão quando aplicável;
- manutenção de divergência explícita.

# 1037. Divergência entre fontes

Quando fontes divergirem, a capacidade deverá preservar:

- cada declaração;
- autoridade;
- temporalidade;
- escopo;
- evidências;
- confiança;
- impacto da divergência.

Nenhuma fonte deverá sobrescrever silenciosamente as demais.

# 1038. Informações de terceiros

Quando o evento envolver terceiros, a capacidade deverá:

- registrar apenas o necessário;
- utilizar descrições genéricas quando possível;
- não criar objetivos ou contexto para o terceiro;
- separar titular e pessoa relacionada;
- limitar acesso;
- impedir inferências indevidas.

# 1039. Eventos sensíveis

Eventos sensíveis deverão possuir controles específicos de:

- título neutro;
- ocultação;
- acesso;
- notificação;
- retenção;
- compartilhamento;
- pesquisa;
- logs;
- explicabilidade;
- contestação.

# 1040. Privacidade visual

A formulação completa de eventos sensíveis não deverá aparecer automaticamente em:

- tela bloqueada;
- notificação;
- e-mail;
- widget;
- dispositivo compartilhado;
- relatório organizacional;
- histórico resumido.

# 1041. Controles do participante

O participante deverá poder:

- confirmar;
- rejeitar;
- corrigir;
- contestar;
- complementar;
- alterar significado pessoal;
- limitar usos;
- ocultar;
- silenciar notificações;
- revogar compartilhamento;
- arquivar;
- consultar histórico.

# 1042. Encerramento funcional

Um evento poderá ser encerrado quando:

- tiver sido concluído;
- tiver sido cancelado;
- tiver sido interrompido definitivamente;
- tiver perdido relevância operacional;
- tiver sido substituído;
- tiver sido corrigido por outro registro.

O encerramento deverá ser diferente de exclusão.

# 1043. Conclusão do evento

A conclusão deverá indicar:

- o que terminou;
- quando;
- quem confirmou;
- quais efeitos permanecem;
- quais impactos foram encerrados;
- quais decisões precisam de revisão;
- se existe possibilidade de reabertura.

# 1044. Encerramento de impactos

Impactos poderão terminar antes ou depois do evento.

A capacidade deverá permitir:

```text
Evento concluído
Impacto ativo
```

ou:

```text
Evento em andamento
Impacto específico encerrado
```

# 1045. Arquivamento

O arquivamento deverá ocorrer quando o evento não necessitar mais de operação ativa.

O evento arquivado poderá permanecer disponível para:

- linha do tempo;
- explicação;
- auditoria;
- análise de evolução;
- reavaliação autorizada.

# 1046. Reabertura

Um evento poderá ser reaberto quando:

- a transição continuar;
- surgirem novos fatos;
- a conclusão estiver incorreta;
- houver contestação;
- efeitos relevantes reaparecerem;
- o evento representar novo ciclo.

A reabertura deverá preservar o ciclo anterior.

# 1047. Novo evento ou reabertura

A capacidade deverá decidir entre:

## Reabrir

Quando existe continuidade funcional do mesmo evento.

## Criar novo evento

Quando existe nova ocorrência independente.

Exemplo:

```text
Nova mudança de cidade:
novo evento

Retomada de mudança interrompida:
possível reabertura
```

# 1048. Propagação

A propagação deverá informar outras capacidades sobre mudanças relevantes no evento ou em seus impactos.

Gatilhos possíveis:

- confirmação;
- início;
- atualização;
- mudança de relevância;
- impacto confirmado;
- conclusão;
- cancelamento;
- contestação;
- correção;
- revogação.

# 1049. Recorte de propagação

Cada consumidor deverá receber somente:

- identificador necessário;
- tipo funcional;
- estado;
- temporalidade;
- impacto relevante;
- confiança;
- sensibilidade;
- permissão;
- ação esperada.

O recorte não deverá conter toda a narrativa do evento.

# 1050. Capacidades consumidoras

Poderão consumir recortes:

- Contexto Vivo;
- Objetivos;
- Próximos Passos;
- Oportunidades Ativas;
- Intervenções Contextuais;
- Experiências;
- Evolução Contínua;
- serviços especializados autorizados.

Cada capacidade deverá reavaliar suas próprias unidades.

# 1051. Propagação para o Contexto Vivo

O Contexto Vivo deverá receber:

- mudança;
- dimensão possivelmente afetada;
- temporalidade;
- origem;
- confiança;
- estado de confirmação;
- impacto autorizado.

Ele deverá governar a atualização do estado contextual.

# 1052. Propagação para Objetivos

A Capacidade de Objetivos deverá receber:

- evento;
- objetivos potencialmente afetados;
- tipo de impacto;
- intensidade;
- temporalidade;
- confiança;
- necessidade de revisão.

Ela não deverá receber ordem para alterar o objetivo.

# 1053. Propagação para outras capacidades

Outras capacidades deverão receber uma solicitação funcional como:

- reavaliar;
- suspender;
- atualizar;
- cancelar;
- aguardar;
- limitar;
- observar.

A propagação não deverá declarar que a decisão dependente já foi alterada.

# 1054. Idempotência

O reprocessamento do mesmo evento não deverá:

- duplicar impactos;
- repetir atualizações;
- gerar vários objetivos;
- cancelar a mesma ação diversas vezes;
- enviar notificações repetidas;
- criar eventos duplicados.

# 1055. Prevenção de ciclos

A capacidade deverá impedir ciclos como:

```text
Evento atualiza Contexto Vivo
→ Contexto Vivo gera o mesmo evento
→ evento atualiza Contexto Vivo novamente
```

Deverão ser utilizados:

- correlação;
- causalidade;
- origem;
- versão;
- idempotência;
- identificação da transformação.

# 1056. Falha de propagação

Quando uma capacidade não receber ou processar o recorte, deverão ser registrados:

- evento causador;
- consumidor;
- efeito esperado;
- estado pendente;
- risco;
- recuperação;
- impacto sobre decisões.

# 1057. Falha segura

Em caso de falha:

- atualizações críticas deverão ser suspensas;
- o último estado válido deverá ser preservado;
- a incerteza deverá ser explícita;
- permissões restritivas deverão prevalecer;
- nenhuma conclusão deverá ser presumida;
- o participante deverá ser informado quando necessário.

# 1058. Histórico do ciclo de vida

O histórico deverá permitir reconstruir:

```text
origem
→ sinalização
→ proposição
→ confirmação
→ início
→ atualizações
→ impactos
→ contestação ou correção
→ conclusão
→ arquivamento
```

# 1059. Eventos funcionais do ciclo de vida

A capacidade poderá produzir:

- `PossivelEventoDeVidaIdentificado`;
- `EventoDeVidaProposto`;
- `EventoDeVidaRejeitado`;
- `EventoDeVidaPlanejado`;
- `EventoDeVidaConfirmado`;
- `EventoDeVidaIniciado`;
- `EventoDeVidaAtualizado`;
- `EventoDeVidaAdiado`;
- `EventoDeVidaConcluido`;
- `EventoDeVidaInterrompido`;
- `EventoDeVidaCancelado`;
- `EventoDeVidaContestado`;
- `EventoDeVidaCorrigido`;
- `EventoDeVidaArquivado`;
- `EventoDeVidaReaberto`;
- `EventosDeVidaUnificados`;
- `EventoDeVidaDesdobrado`;
- `RelevanciaDeEventoDeVidaAlterada`;
- `ImpactoDeEventoDeVidaProposto`;
- `ImpactoDeEventoDeVidaConfirmado`;
- `ImpactoDeEventoDeVidaEncerrado`;
- `RecorteDeEventoDeVidaRecomposto`;
- `CapacidadeConsumidoraDeEventoDeVidaNotificada`.

# 1060. Critérios funcionais de aceite

O ciclo de vida será considerado adequadamente definido quando:

1. sinais permanecerem distintos de eventos;
2. propostas não produzirem impactos definitivos;
3. declarações preservarem autoria;
4. fontes respeitarem sua autoridade;
5. confirmação e impactos permanecerem separados;
6. eventos planejados não forem tratados como ocorridos;
7. eventos progressivos puderem ser atualizados;
8. estados e transições forem rastreáveis;
9. temporalidade incerta puder ser representada;
10. eventos retroativos preservarem data de conhecimento;
11. relevância permanecer contextual;
12. impactos forem avaliados individualmente;
13. causalidade não for presumida;
14. eventos compostos preservarem componentes;
15. correções preservarem histórico;
16. contestações suspenderem efeitos críticos;
17. conclusão não encerrar automaticamente todos os impactos;
18. arquivamento preservar consulta autorizada;
19. reabertura preservar ciclos anteriores;
20. propagação utilizar recortes mínimos;
21. reprocessamento não duplicar efeitos;
22. falhas reduzirem automação;
23. eventos sensíveis possuírem proteção reforçada;
24. Contexto Vivo e Objetivos preservarem suas responsabilidades;
25. o participante permanecer no controle.

# 1061. Regras fundamentais do ciclo de vida

1. Sinal não equivale a evento.
2. Proposta não equivale a confirmação.
3. Confirmação do evento não confirma todos os impactos.
4. Evento planejado não equivale a evento ocorrido.
5. Estado do evento e estado da informação são dimensões distintas.
6. Declaração pessoal poderá possuir autoridade suficiente sobre a própria vivência.
7. Fonte externa somente poderá afirmar fatos sob seu escopo.
8. Inferência deverá permanecer identificada.
9. Temporalidade não deverá possuir precisão artificial.
10. Relevância deverá ser contextual.
11. Relevância poderá mudar.
12. Evento e impacto possuem ciclos diferentes.
13. Impactos deverão ser avaliados por unidade afetada.
14. Evento não cria objetivo pessoal ativo.
15. Evento não impõe prioridade.
16. Atividade não comprova Evento de Vida.
17. Causalidade não deverá ser presumida por proximidade temporal.
18. Eventos simultâneos não deverão gerar fadiga desnecessária.
19. Correção não deverá reescrever o histórico.
20. Contestação deverá limitar efeitos críticos.
21. Conclusão não elimina impactos persistentes.
22. Arquivamento não equivale a exclusão.
23. Reabertura deverá preservar o ciclo anterior.
24. Propagação deverá utilizar recortes mínimos.
25. Reprocessamento não poderá duplicar efeitos.
26. Falhas deverão reduzir automação.
27. Conteúdo sensível deverá permanecer minimizado.
28. Informações de terceiros não deverão gerar perfis indevidos.
29. Receita não deverá alterar relevância ou impacto.
30. O participante deverá permanecer no controle.

Com isso, ficam definidas as **regras do ciclo de vida dos Eventos de Vida**, abrangendo identificação, proposição, confirmação, estados, temporalidade, relevância, impactos, relações, correção, contestação, encerramento e propagação.

O próximo bloco deverá detalhar:

> **os comportamentos funcionais da visualização e do controle dos Eventos de Vida, incluindo linha do tempo, detalhamento, impactos, revisões, eventos planejados, conteúdo sensível, histórico e ações do participante.**
