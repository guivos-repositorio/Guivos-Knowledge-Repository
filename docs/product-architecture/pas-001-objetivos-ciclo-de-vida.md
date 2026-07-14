---
id: PAS-001-OBJ-LIFECYCLE-001
title: Regras do Ciclo de Vida dos Objetivos
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-13
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-OBJ-FOUNDATION-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-CV-STATE-001
  - PAS-001-CV-EVENT-001
  - PAS-001-CV-INTEGRATION-001
  - GLPA-001
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-OBJ-LIFECYCLE-001 — Regras do Ciclo de Vida dos Objetivos

## 1. Autoridade e vínculo

Este documento é a **segunda extensão normativa da Capacidade 03 — Objetivos** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade funcional das seções 366 a 403 do `PAS-001-OBJ-FOUNDATION-001 1.0.0` e da especificação-base `PAS-001 0.5.0`.

A separação modular preserva legibilidade, rastreabilidade e evolução independente sem reduzir a autoridade normativa desta extensão.

# 404. Regras detalhadas do ciclo de vida dos objetivos

O ciclo de vida de um objetivo deverá representar sua evolução desde a primeira manifestação até sua conclusão, retirada, substituição ou arquivamento.

Esse ciclo deverá preservar:

- autoria;
- significado;
- origem;
- temporalidade;
- prioridade;
- contexto;
- alterações;
- critérios de sucesso;
- conflitos;
- permissões;
- histórico.

> Um objetivo não deverá ser tratado como registro estático. Sua formulação, importância, viabilidade e significado poderão mudar ao longo da jornada.

# 405. Unidade funcional do objetivo

Cada objetivo deverá existir como unidade funcional própria.

Um objetivo não deverá ser representado apenas como texto livre ou atributo genérico da dimensão `Direção`.

Cada unidade deverá possuir, quando aplicável:

| Atributo | Finalidade |
|---|---|
| Identificador | Distinguir o objetivo |
| Participante titular | Definir autoria |
| Formulação atual | Representar a direção vigente |
| Expressão original | Preservar a linguagem do participante |
| Natureza | Resultado, transformação, desenvolvimento, manutenção, redução, exploração, experiência ou contribuição |
| Origem | Identificar de onde surgiu |
| Estado funcional | Representar o ciclo de vida |
| Prioridade | Indicar importância relativa atual |
| Horizonte temporal | Informar referência de tempo |
| Motivação | Explicar por que importa |
| Critérios de sucesso | Definir sinais de avanço ou conclusão |
| Contexto relacionado | Associar momento, capacidades, restrições e preferências |
| Relações | Vincular outros objetivos |
| Conflitos | Preservar tensões relevantes |
| Confiança | Diferenciar declaração, confirmação e hipótese |
| Sensibilidade | Aplicar proteção |
| Finalidades autorizadas | Limitar utilização |
| Permissões | Controlar consumidores e compartilhamentos |
| Histórico | Preservar alterações |
| Revisão prevista | Definir quando reavaliar |

Nem todos os atributos deverão ser obrigatórios desde a criação.

# 406. Origens funcionais de um objetivo

Um objetivo poderá surgir por:

1. declaração direta do participante;
2. aprofundamento durante a Captura de Contexto;
3. conversa com a Guivos;
4. transformação consciente de uma intenção;
5. transformação de sonho ou possibilidade;
6. impacto de Evento de Vida;
7. experiência realizada;
8. recomendação profissional;
9. proposta de organização;
10. sugestão da Guivos Intelligence;
11. relação com outro objetivo;
12. revisão de objetivo anterior.

A origem deverá permanecer identificada durante todo o ciclo de vida.

# 407. Autoridade conforme a origem

## 407.1 Declaração do participante

Poderá originar objetivo confirmado, desde que exista clareza suficiente sobre a direção expressa.

## 407.2 Inferência da Guivos

Poderá originar somente:

- hipótese;
- pergunta;
- possibilidade;
- proposta de formulação;
- sugestão de revisão.

Não poderá criar objetivo confirmado ou ativo.

## 407.3 Organização ou profissional

Poderá originar:

- recomendação;
- requisito institucional;
- resultado esperado pela organização;
- plano externo;
- proposta de desenvolvimento.

O sistema deverá distinguir esse conteúdo de um objetivo pessoal.

## 407.4 Comportamento observado

Poderá justificar exploração ou confirmação, mas não ativação automática.

Exemplos:

- pesquisar cursos não cria objetivo de estudar;
- visualizar vagas não cria objetivo de mudar de emprego;
- comprar equipamento não cria objetivo esportivo;
- consumir conteúdo religioso não cria objetivo espiritual.

# 408. Gatilhos de criação

O processo de criação poderá ser iniciado quando:

- o participante disser que deseja algo;
- uma intenção se tornar recorrente;
- um sonho começar a orientar escolhas;
- uma possibilidade receber atenção consciente;
- um Evento de Vida gerar nova direção;
- um objetivo amplo for desdobrado;
- uma recomendação externa for aceita;
- um objetivo anterior for reformulado;
- a pessoa solicitar ajuda para organizar uma direção.

A existência de um gatilho não significa que o objetivo deverá ser criado automaticamente.

# 409. Fluxo funcional de criação

```text
Manifestação identificada
→ natureza avaliada
→ autoria e origem verificadas
→ intenção, sonho, possibilidade ou objetivo diferenciados
→ formulação inicial preservada
→ contexto mínimo associado
→ confirmação solicitada quando necessária
→ objetivo criado no estado adequado
→ permissões e finalidades aplicadas
→ evento funcional registrado
```

O estado inicial poderá ser:

- `Mencionado`;
- `Possibilidade`;
- `Em exploração`;
- `Proposto`;
- `Confirmado`.

A criação não deverá resultar automaticamente em estado `Ativo`.

# 410. Criação por declaração direta

Quando o participante expressar claramente uma direção, a Guivos deverá:

1. preservar a declaração original;
2. verificar se representa intenção, possibilidade ou objetivo;
3. confirmar a formulação quando houver ambiguidade;
4. identificar a finalidade de uso;
5. registrar o horizonte, caso informado;
6. associar contexto relevante;
7. perguntar sobre prioridade somente quando necessário;
8. evitar exigir plano completo.

Exemplo:

> “Quero aprender inglês para trabalhar no exterior.”

A representação poderá ser:

```text
Objetivo:
Desenvolver inglês profissional

Motivação:
Acessar oportunidades internacionais

Origem:
Declaração direta

Estado:
Confirmado
```

# 411. Criação por conversa

Durante uma conversa, a Guivos deverá distinguir:

- relato sobre algo desejado;
- reflexão temporária;
- hipótese;
- comparação de alternativas;
- intenção real;
- objetivo assumido.

Perguntas adequadas poderão incluir:

- “Isso representa algo que você deseja buscar agora?”
- “Você está apenas considerando essa possibilidade ou quer registrá-la como objetivo?”
- “Essa formulação representa corretamente o que você deseja?”
- “Você quer que isso oriente recomendações e próximos passos?”

A continuidade da conversa não deverá ser interpretada como confirmação implícita.

# 412. Criação a partir de sonho

Um sonho deverá poder permanecer preservado sem ativação operacional.

Fluxo possível:

```text
Sonho registrado
→ exploração autorizada
→ possibilidade identificada
→ objetivo intermediário formulado
→ confirmação
→ ativação
```

Exemplo:

```text
Sonho:
Construir uma empresa global

Objetivo exploratório:
Compreender modelos de expansão internacional

Objetivo ativo:
Validar a Guivos em um mercado estrangeiro
```

A Guivos não deverá reduzir automaticamente um sonho amplo a um objetivo operacional específico.

# 413. Criação por recomendação externa

Quando uma organização, profissional ou instituição propuser um objetivo, a interface deverá informar:

- quem propôs;
- por que propôs;
- se existe obrigação institucional;
- quais consequências existem;
- quais informações serão utilizadas;
- se o objetivo será pessoal, institucional ou compartilhado.

O participante poderá:

- aceitar;
- rejeitar;
- reformular;
- manter apenas como recomendação;
- adiar;
- limitar o compartilhamento.

A recusa não deverá ser interpretada automaticamente como falta de comprometimento.

# 414. Objetivo institucional e objetivo pessoal

Uma mesma direção poderá possuir representações diferentes.

Exemplo:

```text
Objetivo institucional:
Concluir treinamento obrigatório

Objetivo pessoal:
Desenvolver capacidade de liderança
```

O sistema deverá preservar:

- titularidade;
- finalidade;
- critérios;
- permissões;
- responsabilidade;
- forma de conclusão.

O cumprimento de um objetivo institucional não prova que o participante assumiu o mesmo resultado como objetivo pessoal.

# 415. Detecção de duplicidade

Antes de criar um objetivo, a capacidade deverá verificar:

- formulações semelhantes;
- objetivos ativos relacionados;
- versões anteriores;
- objetivos concluídos reabertos;
- objetivos substituídos;
- diferenças de contexto;
- diferenças de horizonte;
- diferenças de finalidade.

Objetivos semelhantes não deverão ser automaticamente unificados.

Exemplo:

```text
Objetivo A:
Aprender inglês para viagens

Objetivo B:
Desenvolver inglês técnico para trabalho
```

Eles poderão coexistir, ser relacionados ou ser reunidos por decisão do participante.

# 416. Resultados da avaliação de duplicidade

A análise poderá resultar em:

- novo objetivo independente;
- complemento de objetivo existente;
- reformulação;
- reativação;
- desdobramento;
- associação entre objetivos;
- possível duplicidade aguardando confirmação;
- unificação autorizada.

Nenhuma unificação deverá apagar históricos ou critérios distintos.

# 417. Confirmação funcional

A confirmação deverá demonstrar que o participante reconhece determinada formulação como representação legítima de sua direção.

A confirmação deverá possuir:

- objetivo apresentado;
- formulação compreensível;
- finalidade;
- usos previstos;
- data;
- canal;
- escopo;
- ator;
- nível de confiança resultante.

Confirmar a existência do objetivo não significa:

- definir prioridade;
- autorizar publicidade;
- aceitar um plano;
- comprometer-se com prazo;
- permitir compartilhamento irrestrito.

# 418. Quando a confirmação é obrigatória

A confirmação será obrigatória quando o objetivo:

- tiver origem inferencial;
- tiver sido proposto por terceiro;
- resultar de comportamento observado;
- possuir conteúdo sensível;
- orientar decisão de alto impacto;
- substituir objetivo ativo;
- alterar prioridade principal;
- produzir compartilhamento externo;
- gerar compromisso institucional;
- apresentar formulação diferente da expressão original.

# 419. Confirmação simplificada

Objetivos declarados diretamente poderão receber confirmação simplificada.

Exemplo:

> Você quer registrar “melhorar minha saúde” como um objetivo da sua jornada?

Ações:

- Sim, registrar.
- Quero ajustar a formulação.
- É apenas uma possibilidade.
- Não quero registrar.
- Revisar depois.

A interface não deverá induzir a ativação como opção padrão inevitável.

# 420. Ausência de confirmação

Quando não houver confirmação:

- o objetivo não deverá ser ativado;
- a manifestação poderá permanecer como intenção, possibilidade ou proposta;
- nenhuma recomendação crítica deverá depender dela;
- o participante não deverá ser pressionado;
- a solicitação poderá ser retomada somente quando relevante.

Ausência de resposta não significa concordância.

# 421. Ativação do objetivo

Um objetivo poderá ser ativado quando:

1. tiver autoria ou aceitação consciente;
2. possuir direção compreensível;
3. tiver finalidade autorizada;
4. não estiver impedido por conflito crítico;
5. puder orientar alguma capacidade da jornada;
6. o participante autorizar seu uso operacional.

A ativação não deverá exigir:

- prazo;
- plano completo;
- indicador quantitativo;
- oportunidade disponível;
- viabilidade totalmente comprovada.

# 422. Ativação parcial por finalidade

Um objetivo poderá estar ativo para determinadas finalidades e não para outras.

Exemplo:

```text
Objetivo:
Explorar mudança de carreira

Próximos Passos:
Autorizado

Oportunidades profissionais:
Autorizado

Compartilhamento com empresas:
Não autorizado

Publicidade personalizada:
Não autorizado
```

A ativação deverá respeitar permissões específicas.

# 423. Correção e mudança real

A capacidade deverá diferenciar:

## Correção

A representação anterior estava incorreta.

Exemplo:

> O objetivo nunca foi mudar de cidade; era apenas viajar por um período.

## Mudança real

A representação anterior estava correta, mas deixou de representar a direção atual.

Exemplo:

> Antes eu queria permanecer na empresa; agora desejo buscar outra oportunidade.

A correção deverá reparar usos indevidos quando necessário.

A mudança real deverá preservar a validade histórica do objetivo anterior.

# 424. Reformulação

A reformulação ocorre quando o significado central permanece relacionado, mas a representação precisa mudar.

Poderá envolver:

- maior clareza;
- redução de escopo;
- ampliação;
- mudança de horizonte;
- mudança de resultado;
- mudança de motivação;
- adaptação ao contexto;
- substituição de critério de sucesso.

Exemplo:

```text
Formulação anterior:
Melhorar minha carreira

Formulação atual:
Conquistar uma posição de gestão operacional
```

A reformulação deverá preservar o vínculo com a versão anterior.

# 425. Desdobramento de objetivo

Um objetivo amplo poderá ser dividido em objetivos relacionados.

Exemplo:

```text
Objetivo amplo:
Expandir a Guivos internacionalmente

Objetivos relacionados:
- selecionar o primeiro país;
- validar a proposta de valor;
- estruturar presença comercial;
- adequar operação e marca.
```

O desdobramento não deverá transformar automaticamente cada parte em tarefa.

Cada objetivo derivado deverá possuir:

- significado próprio;
- relação com o objetivo maior;
- estado;
- prioridade;
- critérios;
- autorização.

# 426. Unificação de objetivos

Objetivos poderão ser unificados quando:

- representam a mesma direção;
- possuem critérios compatíveis;
- o participante compreender a mudança;
- históricos forem preservados;
- não existirem permissões incompatíveis;
- relações anteriores forem recompostas.

A unificação deverá produzir uma nova representação, sem apagar os objetivos de origem.

# 427. Modelo funcional de prioridade

A prioridade representa a importância relativa de um objetivo no contexto atual.

Ela deverá ser separada de:

- urgência;
- estado;
- valor humano;
- viabilidade;
- obrigação;
- ordem de criação.

Um objetivo prioritário poderá estar bloqueado.

Um objetivo de baixa prioridade poderá continuar ativo.

# 428. Fatores de priorização

A Guivos poderá apoiar a análise considerando:

- importância declarada;
- urgência;
- prazo externo;
- impacto esperado;
- relação com necessidade básica;
- dependências;
- custo de adiamento;
- oportunidade temporal;
- capacidades disponíveis;
- restrições;
- esforço;
- risco;
- relação com outros objetivos;
- valores e significado declarados.

Esses fatores deverão ser apresentados como apoio, não como decisão definitiva.

# 429. Prioridade declarada e prioridade sugerida

## Prioridade declarada

Definida diretamente pelo participante.

## Prioridade sugerida

Proposta pela Guivos com base em critérios explicáveis.

Exemplo:

> Este objetivo pode exigir atenção mais próxima porque possui prazo de inscrição e depende de uma ação nesta semana.

A sugestão não deverá alterar automaticamente a prioridade registrada.

# 430. Urgência não é prioridade

Um objetivo poderá ser urgente sem ser o mais importante.

Exemplo:

```text
Objetivo urgente:
Renovar uma certificação próxima do vencimento

Objetivo principal:
Conseguir uma nova oportunidade profissional
```

A capacidade deverá preservar as duas dimensões.

# 431. Prioridade contextual

Um objetivo poderá ganhar prioridade apenas em determinado contexto.

Exemplos:

- objetivo de viagem durante período de férias;
- objetivo financeiro após Evento de Vida;
- objetivo de saúde durante recuperação;
- objetivo profissional durante processo seletivo.

A prioridade contextual deverá possuir:

- motivo;
- período;
- condição de encerramento;
- impacto sobre outros objetivos.

# 432. Alteração de prioridade

Uma prioridade poderá ser alterada por:

- declaração do participante;
- Evento de Vida;
- novo prazo;
- conflito;
- mudança de restrição;
- objetivo concluído;
- oportunidade temporária;
- revisão periódica.

Alterações sugeridas pela Guivos exigirão confirmação quando afetarem a ordem de atuação das capacidades consumidoras.

# 433. Portfólio de objetivos

A capacidade deverá permitir uma visão conjunta dos objetivos.

O portfólio poderá demonstrar:

- objetivos ativos;
- prioridades;
- horizontes;
- relações;
- conflitos;
- dependências;
- objetivos pausados;
- objetivos em exploração;
- objetivos próximos de revisão.

O portfólio não deverá criar pontuação geral de sucesso pessoal.

# 434. Limites de simultaneidade

A Guivos poderá alertar quando muitos objetivos disputarem recursos relevantes.

Exemplo:

> Você possui cinco objetivos de alta prioridade que dependem do mesmo período e disponibilidade.

A capacidade poderá sugerir:

- sequência;
- redução temporária;
- pausa;
- revisão de prioridade;
- agrupamento;
- escolha contextual.

Não deverá impor quantidade máxima universal de objetivos.

# 435. Tipos de conflito entre objetivos

Conflitos poderão ser:

- temporais;
- financeiros;
- geográficos;
- de energia;
- de atenção;
- de capacidade;
- de relacionamento;
- de prazo;
- de recursos;
- de valores declarados;
- de exclusividade;
- de prioridade;
- de sensibilidade;
- entre objetivo pessoal e institucional.

# 436. Registro funcional de conflito

Cada conflito deverá registrar:

- objetivos envolvidos;
- tipo;
- origem;
- contexto;
- recursos disputados;
- impacto;
- urgência;
- temporalidade;
- alternativas;
- participação necessária;
- decisão provisória;
- resultado;
- possibilidade de revisão.

O conflito não deverá reduzir automaticamente a validade de nenhum objetivo.

# 437. Detecção de conflito

Um conflito poderá ser detectado por:

- declaração do participante;
- análise do Contexto Vivo;
- sobreposição de prazos;
- restrição incompatível;
- uso concorrente de recursos;
- Evento de Vida;
- recomendação externa;
- tentativa de gerar Próximos Passos incompatíveis.

A detecção automática deverá produzir alerta ou proposta, não decisão silenciosa.

# 438. Resolução de conflitos

A resolução poderá resultar em:

- coexistência;
- sequência temporal;
- prioridade contextual;
- pausa de um objetivo;
- reformulação;
- redução de escopo;
- compartilhamento de recursos;
- substituição;
- retirada;
- manutenção consciente do conflito;
- adiamento da decisão.

A Guivos deverá explicar consequências e preservar a decisão do participante.

# 439. Conflito entre objetivo pessoal e organizacional

Quando existir tensão entre objetivo pessoal e institucional, a interface deverá distinguir:

- quem é titular de cada objetivo;
- quais obrigações existem;
- quais consequências são institucionais;
- quais informações serão compartilhadas;
- qual decisão pertence ao participante.

A organização não deverá acessar objetivos pessoais não autorizados para avaliar adesão ou desempenho.

# 440. Conflito de valores declarados

Quando um objetivo parecer incompatível com valores ou princípios declarados pelo participante, a Guivos poderá perguntar:

> Você deseja revisar como esse objetivo se relaciona com aquilo que considera importante?

A capacidade não deverá:

- presumir incoerência moral;
- retirar o objetivo;
- impor interpretação;
- utilizar valores sensíveis para manipulação.

# 441. Revisão de objetivo

A revisão deverá avaliar se o objetivo continua representando:

- direção atual;
- significado;
- prioridade;
- horizonte;
- resultado desejado;
- critérios de sucesso;
- permissões;
- compatibilidade contextual.

A revisão não deverá exigir reconstrução integral do objetivo.

# 442. Gatilhos de revisão

Uma revisão poderá ser iniciada por:

- solicitação do participante;
- passagem do tempo;
- Evento de Vida;
- mudança de prioridade;
- conflito;
- bloqueio prolongado;
- ausência de atividade relevante;
- novo resultado;
- mudança de permissão;
- conclusão parcial;
- objetivo relacionado alterado;
- recomendação que deixou de fazer sentido.

Ausência de atividade, isoladamente, não prova perda de interesse.

# 443. Fluxo funcional de revisão

```text
Gatilho identificado
→ impacto avaliado
→ objetivo atual apresentado
→ elementos relevantes destacados
→ participante confirma, ajusta ou adia
→ estado, prioridade ou formulação atualizados
→ recortes recompostos
→ capacidades consumidoras notificadas
→ histórico preservado
```

A revisão deverá focar apenas nos elementos afetados.

# 444. Resultados da revisão

Uma revisão poderá resultar em:

- confirmação sem alteração;
- alteração de prioridade;
- reformulação;
- mudança de horizonte;
- ajuste de critério de sucesso;
- pausa;
- retomada;
- bloqueio;
- conclusão;
- retirada;
- substituição;
- manutenção em exploração;
- nova revisão futura.

# 445. Envelhecimento de objetivo

O envelhecimento representa perda de segurança sobre a atualidade do objetivo.

Ele não significa que o objetivo se tornou falso ou inválido.

Um objetivo poderá envelhecer quando:

- não recebe confirmação por período relevante;
- o contexto mudou;
- um Evento de Vida ocorreu;
- suas dependências foram alteradas;
- a prioridade não é revista;
- os critérios de sucesso deixaram de ser aplicáveis;
- as permissões expiraram.

# 446. Classes temporais dos objetivos

## Dinâmico

Poderá mudar frequentemente.

Exemplos:

- objetivo de curto prazo;
- objetivo ligado a oportunidade temporária;
- objetivo exploratório.

## Estável

Tende a permanecer válido por período maior.

Exemplos:

- formação acadêmica;
- desenvolvimento profissional;
- organização financeira.

## Contínuo

Busca manutenção ou evolução permanente.

Exemplos:

- manter saúde;
- fortalecer relações;
- desenvolvimento espiritual.

## Eventual

Existe para resultado específico e delimitado.

Exemplos:

- realizar uma viagem;
- concluir certificação;
- participar de projeto.

## Aspiracional

Possui horizonte amplo ou indefinido.

Exemplos:

- construir legado;
- desenvolver empresa global;
- contribuir com determinada causa.

# 447. Estados de atualidade

Um objetivo poderá estar:

- atual;
- próximo de revisão;
- possivelmente desatualizado;
- aguardando confirmação;
- desatualizado para determinada finalidade;
- historicamente válido;
- sem informação suficiente sobre atualidade.

O estado de atualidade deverá permanecer separado do estado funcional.

Um objetivo poderá estar `Ativo` e `Próximo de revisão`.

# 448. Horizonte de revisão

O horizonte deverá considerar:

- tipo de objetivo;
- prazo;
- impacto;
- sensibilidade;
- contexto;
- prioridade;
- volatilidade;
- dependências;
- uso pelas demais capacidades.

Exemplos:

| Objetivo | Horizonte funcional |
|---|---|
| Participar de evento no próximo mês | curto |
| Mudar de carreira | médio, com revisão após mudanças relevantes |
| Manter proximidade familiar | contínuo e contextual |
| Construir empresa global | longo, com revisões de direção |
| Explorar nova atividade | curto ou após experiência |

Não deverá existir prazo universal para todos os objetivos.

# 449. Ausência de resposta à revisão

Quando o participante não responder:

- o objetivo não deverá ser confirmado automaticamente;
- a atualidade poderá ser reduzida;
- decisões de alto impacto poderão ser limitadas;
- usos de baixo impacto poderão continuar com incerteza explícita;
- novas solicitações deverão evitar repetição excessiva;
- o objetivo poderá permanecer ativo, dependendo do risco.

# 450. Uso de objetivo envelhecido

Um objetivo envelhecido poderá:

- continuar no histórico;
- permanecer visível;
- apoiar exploração de baixo impacto;
- exigir confirmação antes de orientar ação relevante;
- deixar de ordenar oportunidades;
- ser temporariamente excluído de recortes críticos.

Ele não deverá ser retirado automaticamente.

# 451. Pausa

A pausa representa interrupção temporária do uso operacional.

Durante a pausa:

- o objetivo permanece válido;
- novos Próximos Passos não deverão ser gerados, salvo solicitação;
- oportunidades não deverão ser priorizadas por ele;
- histórico e relações permanecem;
- critérios de retomada poderão ser registrados.

A pausa não deverá ser apresentada como desistência.

# 452. Retomada

A retomada deverá verificar:

- se a formulação continua atual;
- se o contexto mudou;
- se a prioridade permanece;
- se existem novos conflitos;
- se as permissões continuam válidas;
- se os critérios de sucesso precisam de ajuste.

A retomada poderá produzir reformulação antes da ativação.

# 453. Bloqueio

Um objetivo estará bloqueado quando existe impedimento atual, como:

- falta de recurso;
- restrição;
- dependência não atendida;
- prazo externo;
- conflito;
- condição de saúde;
- autorização ausente;
- indisponibilidade de oportunidade.

O bloqueio deverá indicar:

- causa;
- impacto;
- possibilidade de ação;
- condição de desbloqueio;
- revisão prevista.

O bloqueio não deverá ser interpretado como fracasso.

# 454. Desbloqueio

Um objetivo poderá ser desbloqueado quando:

- a restrição for removida;
- a dependência for concluída;
- a permissão for concedida;
- o conflito for resolvido;
- surgir alternativa;
- o participante reformular o objetivo.

O desbloqueio não deverá ativar automaticamente o objetivo quando ele estiver pausado ou desatualizado.

# 455. Conclusão

Antes de concluir, a capacidade deverá considerar:

- critério de sucesso;
- manifestação do participante;
- evidências disponíveis;
- natureza do objetivo;
- resultados parciais;
- necessidade de continuidade;
- objetivos dependentes.

A conclusão poderá ser:

- declarada pelo participante;
- sugerida pela Guivos;
- confirmada por fonte autorizada;
- reconhecida por critério objetivo.

Objetivos pessoais não deverão ser concluídos exclusivamente por inferência.

# 456. Conclusão parcial

Um objetivo poderá alcançar resultado parcial sem ser concluído.

Exemplo:

```text
Objetivo:
Aprender inglês

Resultado parcial:
Concluir nível intermediário
```

A conclusão parcial poderá gerar:

- marco;
- evidência de evolução;
- reformulação;
- novo critério;
- objetivo derivado;
- manutenção do objetivo principal.

# 457. Conclusão de objetivos contínuos

Objetivos de manutenção ou desenvolvimento contínuo poderão não possuir conclusão definitiva.

Nesses casos, poderão existir:

- ciclos;
- marcos;
- períodos avaliados;
- manutenção confirmada;
- reformulações;
- encerramento voluntário.

Exemplo:

> Manter uma rotina saudável durante o próximo semestre.

A conclusão do ciclo não precisa encerrar permanentemente a direção.

# 458. Retirada

A retirada deverá:

- interromper novos usos;
- retirar o objetivo dos recortes ativos;
- notificar capacidades consumidoras;
- preservar histórico conforme autorização;
- manter relações anteriores;
- permitir explicação;
- possibilitar reativação futura.

A retirada não deverá exigir justificativa.

# 459. Desistência declarada

Quando o participante utilizar o conceito de desistência, a Guivos deverá preservar sua linguagem sem classificá-la negativamente.

A interface poderá perguntar:

- “Você deseja retirar este objetivo?”
- “A direção deixou de fazer sentido ou está inviável neste momento?”
- “Deseja manter no histórico ou reformular?”

A resposta deverá orientar o estado funcional, não uma avaliação pessoal.

# 460. Substituição

Um objetivo poderá ser substituído quando outro representar melhor a direção atual.

A substituição deverá registrar:

- objetivo anterior;
- novo objetivo;
- motivo;
- elementos preservados;
- critérios transferidos;
- relações recompostas;
- data efetiva;
- impacto sobre capacidades consumidoras.

O objetivo anterior deverá tornar-se histórico ou arquivado.

# 461. Arquivamento

O arquivamento retira o objetivo da operação cotidiana.

Poderá ocorrer após:

- conclusão;
- retirada;
- substituição;
- longo período sem uso;
- decisão do participante;
- encerramento institucional.

O arquivamento não deverá apagar:

- autoria;
- versões;
- decisões anteriores;
- experiências relacionadas;
- evidências;
- conflitos resolvidos.

# 462. Reativação

Objetivos retirados ou arquivados poderão ser reativados.

A reativação deverá avaliar:

- atualidade;
- formulação;
- contexto;
- prioridade;
- critérios;
- permissões;
- relações;
- conflitos.

A reativação deverá criar novo momento funcional, preservando o ciclo anterior.

# 463. Impacto de Evento de Vida

Um Evento de Vida poderá:

- criar nova intenção;
- alterar prioridade;
- bloquear objetivo;
- tornar objetivo mais urgente;
- retirar viabilidade;
- mudar motivação;
- gerar reformulação;
- provocar retirada;
- criar conflito;
- exigir revisão.

Nenhum impacto deverá ser aplicado a todos os objetivos de forma automática.

# 464. Propagação para capacidades consumidoras

Mudanças relevantes deverão ser comunicadas às capacidades que utilizam o objetivo.

Exemplos:

| Mudança | Efeito possível |
|---|---|
| Objetivo ativado | permitir Próximos Passos e oportunidades |
| Prioridade elevada | alterar ordenação contextual |
| Objetivo pausado | interromper novas ações |
| Objetivo reformulado | recompor recortes |
| Objetivo concluído | revisar Próximos Passos pendentes |
| Objetivo retirado | interromper usos |
| Permissão revogada | limitar consumidores |
| Conflito identificado | suspender decisões incompatíveis |

Cada capacidade consumidora deverá reavaliar suas próprias decisões.

# 465. Apresentação ao participante

A interface de objetivos deverá permitir visualizar:

- formulação atual;
- expressão original;
- estado;
- prioridade;
- horizonte;
- motivação;
- critérios;
- relações;
- conflitos;
- progresso reconhecido;
- origem;
- permissões;
- histórico;
- capacidades que utilizam o objetivo.

A interface não deverá apresentar:

- pontuação de ambição;
- ranking moral;
- comparação depreciativa;
- obrigação de manter todos os objetivos ativos;
- percentual artificial quando não houver critério válido.

# 466. Controle de objetivos sensíveis

Objetivos sensíveis deverão permitir:

- ocultação visual;
- acesso restrito;
- finalidade específica;
- compartilhamento seletivo;
- revogação;
- retirada sem exposição;
- explicações minimizadas;
- ausência de publicidade não autorizada.

Notificações não deverão expor conteúdo sensível em telas bloqueadas ou dispositivos compartilhados.

# 467. Eventos funcionais do ciclo de vida

A capacidade poderá produzir:

- `ManifestacaoDeDirecaoIdentificada`;
- `ObjetivoCriado`;
- `ObjetivoProposto`;
- `ObjetivoConfirmado`;
- `ObjetivoAtivado`;
- `ObjetivoNaoConfirmado`;
- `ObjetivoReformulado`;
- `ObjetivoDesdobrado`;
- `ObjetivosUnificados`;
- `PrioridadeSugerida`;
- `PrioridadeConfirmada`;
- `PrioridadeAlterada`;
- `ConflitoEntreObjetivosIdentificado`;
- `ConflitoEntreObjetivosResolvido`;
- `RevisaoDeObjetivoSolicitada`;
- `ObjetivoRevisado`;
- `ObjetivoEnvelhecido`;
- `ObjetivoPausado`;
- `ObjetivoRetomado`;
- `ObjetivoBloqueado`;
- `ObjetivoDesbloqueado`;
- `MarcoDeObjetivoAlcancado`;
- `ObjetivoConcluido`;
- `ObjetivoRetirado`;
- `ObjetivoSubstituido`;
- `ObjetivoArquivado`;
- `ObjetivoReativado`;
- `ObjetivoImpactadoPorEventoDeVida`;
- `RecorteDeObjetivosRecomposto`.

Os contratos detalhados desses eventos serão especificados posteriormente.

# 468. Critérios funcionais de aceite

Este bloco será considerado adequado quando permitir:

1. criar objetivos sem exigir precisão artificial;
2. preservar origem e autoria;
3. impedir ativação por inferência;
4. confirmar formulação e finalidade;
5. separar confirmação de ativação;
6. detectar duplicidade sem unificação automática;
7. diferenciar correção, mudança e reformulação;
8. desdobrar e unificar objetivos com histórico;
9. tratar prioridade separadamente do estado;
10. distinguir urgência e importância;
11. manter múltiplos objetivos;
12. registrar e resolver conflitos;
13. revisar somente elementos afetados;
14. envelhecer sem declarar falsidade;
15. pausar, bloquear, retomar e desbloquear;
16. reconhecer conclusão parcial e contínua;
17. retirar sem julgamento;
18. substituir, arquivar e reativar;
19. propagar mudanças de forma controlada;
20. proteger objetivos sensíveis.

# 469. Regras fundamentais do ciclo de vida

1. Objetivos pertencem ao participante.
2. Manifestação não significa confirmação.
3. Confirmação não significa ativação universal.
4. Inferência não cria objetivo ativo.
5. Prioridade é contextual e revisável.
6. Urgência não equivale a importância.
7. Múltiplos objetivos podem coexistir.
8. Conflito não invalida automaticamente um objetivo.
9. Ausência de atividade não significa desistência.
10. Envelhecimento não significa falsidade.
11. Pausa não significa fracasso.
12. Bloqueio não significa incapacidade pessoal.
13. Reformulação preserva continuidade.
14. Conclusão depende da natureza do objetivo.
15. Retirada não exige justificativa.
16. Histórico não deverá ser reescrito.
17. Permissões limitam utilização e compartilhamento.
18. Alterações relevantes deverão ser explicáveis.
19. Capacidades consumidoras deverão receber somente recortes autorizados.
20. Nenhuma regra poderá retirar do participante o controle sobre sua direção.

Com isso, ficam definidas as **regras de criação, confirmação, priorização, revisão, conflitos, envelhecimento e ciclo de vida dos objetivos**.

O próximo bloco da Capacidade 03 deverá detalhar:

> **a estrutura funcional dos critérios de sucesso, progresso, marcos, evidências e conclusão dos objetivos.**