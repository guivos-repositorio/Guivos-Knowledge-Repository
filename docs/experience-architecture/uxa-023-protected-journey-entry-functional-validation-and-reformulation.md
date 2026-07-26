---
id: UXA-023
title: Validação Funcional e Reformulação do Início Protegido da Jornada
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-020
depends_on:
  - UXA-001
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-020
related:
  - UXA-005
  - UXA-006
  - UXA-010
  - UXA-021
  - UXA-022
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
normative: false
---

# Validação Funcional e Reformulação do Início Protegido da Jornada

## 1. Finalidade

Este documento registra a primeira validação funcional detalhada do **início protegido da jornada pessoal da Guivos**.

A superfície começa somente depois que a pessoa escolhe conscientemente `Iniciar minha jornada` na Página Inicial pública. Ela termina quando uma compreensão inicial suficientemente clara, revisável e autorizada é apresentada para decisão da própria pessoa.

A validação examina:

- transição consciente entre a Home pública e o ambiente protegido;
- explicação anterior à autenticação e à coleta;
- autenticação e recuperação de acesso;
- privacidade, finalidade e autorizações específicas;
- relato por texto, voz, arquivos e perguntas progressivas;
- compartilhamento mínimo e progressivo;
- revisão do conteúdo recebido;
- processamento visível e interrompível;
- pausa, retomada, correção, retirada e exclusão;
- proteção de informações sensíveis e de terceiros;
- apresentação da compreensão inicial;
- bloqueio de personalização antes do gate;
- transição posterior para a Tela Hoje.

## 2. Pergunta funcional

> **Como permitir que uma pessoa conte seu Momento Atual com segurança, autonomia e clareza, sem exigir exposição excessiva, consentimento genérico, processamento invisível ou personalização anterior à revisão da compreensão inicial?**

A experiência somente será válida quando a pessoa compreender:

1. onde está e por que saiu da Home pública;
2. o que poderá compartilhar;
3. o que não precisa compartilhar;
4. para quais finalidades cada informação poderá ser utilizada;
5. quando autenticação e autorização serão necessárias;
6. o que será salvo, processado, transcrito ou extraído;
7. como pausar, corrigir, limitar, retirar ou excluir;
8. como a Guivos distinguirá fatos, fontes, inferências e desconhecidos;
9. que concluir o relato não garante recomendação, oportunidade ou resultado;
10. que a Tela Hoje somente receberá personalização material depois de confirmação suficiente.

## 3. Cenários avaliados

A validação considera os seguintes cenários:

### 3.1 Pessoa visitante que decide iniciar

A pessoa chega pela Home pública, conhece previamente o que acontecerá e escolhe entrar no ambiente protegido.

### 3.2 Pessoa que ainda não possui conta

A pessoa precisa compreender a finalidade do fluxo antes de criar uma conta e não deverá ser pressionada a autenticar sem saber o que virá depois.

### 3.3 Pessoa com conta existente

A pessoa poderá entrar, recuperar acesso ou retornar à Home sem iniciar coleta.

### 3.4 Pessoa que não aceita uma finalidade

A recusa de uma finalidade opcional não deverá bloquear todo o ecossistema. A pessoa poderá explorar sem personalização ou utilizar somente funções compatíveis com as autorizações concedidas.

### 3.5 Pessoa que escolhe texto

A pessoa poderá escrever livremente, responder perguntas progressivas ou combinar as duas formas.

### 3.6 Pessoa que escolhe voz

A gravação, a transcrição, a revisão, a correção e a remoção deverão permanecer explícitas e separadas.

### 3.7 Pessoa que envia arquivo

A pessoa deverá conhecer a finalidade, a extração prevista, a presença de dados de terceiros, a retenção e a forma de remoção antes do processamento material.

### 3.8 Pessoa que informa pouco

A experiência deverá aceitar uma compreensão inicial limitada, declarar insuficiência quando necessário e evitar exigir uma biografia completa.

### 3.9 Pessoa que pausa ou abandona

A pessoa poderá sair sem culpa, retomar posteriormente ou excluir o rascunho.

### 3.10 Pessoa com relato em processamento

A superfície deverá informar o estado real, as fontes consideradas, as ações disponíveis e eventuais falhas, sem simular compreensão imediata.

### 3.11 Pessoa com compreensão inicial disponível

A pessoa deverá revisar fatos, inferências, desconhecidos, finalidades e controles antes de qualquer transição personalizada.

### 3.12 Pessoa que exige proteção adicional

A experiência deverá permitir interrupção segura, linguagem apropriada, encaminhamento a ajuda quando aplicável e bloqueio de usos incompatíveis com a proteção necessária.

## 4. Diagnóstico do contrato anterior

O contrato anterior estabelecia corretamente a separação entre Home pública, início protegido e Tela Hoje. Entretanto, ainda permaneciam riscos funcionais.

### 4.1 Explicação e autenticação não possuíam ordem suficientemente explícita

A pessoa poderia interpretar a criação de conta como condição para descobrir o que seria solicitado. A explicação do fluxo deverá anteceder a autenticação, embora a coleta e a persistência continuem bloqueadas até a proteção apropriada.

### 4.2 Consentimento poderia ser interpretado como autorização ampla

Uma única confirmação genérica não deverá autorizar gravação, transcrição, análise de arquivos, conexão de fontes externas, formação de compreensão persistente e personalização.

### 4.3 O mínimo suficiente ainda não possuía limite operacional claro

A experiência poderia incentivar exposição excessiva para obter uma suposta compreensão completa. A pessoa deverá poder iniciar com pouco, sem perda artificial ou linguagem de insuficiência pessoal.

### 4.4 As modalidades poderiam competir como exigências

Texto, voz, arquivos e perguntas progressivas são alternativas. Nenhuma modalidade deverá ser apresentada como superior, obrigatória ou necessária para provar comprometimento.

### 4.5 Original, transcrição, extração e interpretação poderiam se confundir

A pessoa precisa distinguir:

- conteúdo original fornecido;
- transcrição ou extração automática;
- correções realizadas;
- interpretação produzida pela Guivos;
- informação derivada mantida após remoção do original, quando houver fundamento e explicação aplicáveis.

### 4.6 Pausa e exclusão não estavam suficientemente separadas

Pausar, salvar rascunho, retirar uma autorização, remover um item, apagar o relato e encerrar a jornada possuem efeitos diferentes e deverão ser explicados separadamente.

### 4.7 Processamento poderia parecer invisível ou inevitável

A pessoa deverá saber quando o conteúdo está apenas salvo, aguardando revisão, autorizado para processamento, em processamento, com falha ou pronto para compreensão inicial.

### 4.8 Informações de terceiros exigiam proteção mais explícita

Arquivos, imagens, áudios e relatos poderão conter informações de outras pessoas. A interface deverá alertar, permitir remoção e limitar extração e uso ao necessário.

### 4.9 A compreensão insuficiente não possuía saída suficientemente clara

Quando a base for insuficiente, a pessoa poderá contar mais, corrigir, manter uma jornada sem personalização material ou voltar à exploração geral.

### 4.10 A transição para a Tela Hoje poderia parecer automática

A Tela Hoje somente poderá receber personalização depois que a pessoa revisar a compreensão inicial e autorizar usos compatíveis.

## 5. Decisão de reformulação

O início protegido da jornada deverá seguir esta sequência:

```text
Home pública
→ decisão voluntária de iniciar
→ explicação do ambiente protegido e das alternativas
→ autenticação ou criação de conta
→ resumo de privacidade, finalidades e controles
→ escolha da modalidade de relato
→ compartilhamento mínimo e progressivo
→ revisão do que foi recebido
→ autorização específica para processamento aplicável
→ processamento visível, interrompível e corrigível
→ compreensão inicial apresentada
→ revisão, correção, limitação e decisão da pessoa
→ Tela Hoje, jornada sem personalização material ou exploração geral
```

A sequência não deverá ser convertida em um formulário linear obrigatório. Etapas poderão ser omitidas, retomadas ou apresentadas progressivamente quando isso preservar compreensão e autonomia.

## 6. Hierarquia funcional reformulada

A ordem preferencial da experiência será:

```text
identificação do ambiente protegido
→ explicação curta do que acontecerá
→ alternativas legítimas antes da autenticação
→ autenticação e recuperação de acesso
→ finalidades, privacidade e controles
→ escolha de modalidade
→ relato mínimo e progressivo
→ revisão dos conteúdos recebidos
→ autorização específica de processamento
→ estado de processamento e possibilidade de interrupção
→ compreensão inicial revisável
→ decisão sobre uso e continuidade
```

## 7. Transição consciente a partir da Home

Ao selecionar `Iniciar minha jornada`, a pessoa deverá chegar a uma superfície que declare:

- que a Home pública foi deixada;
- que o ambiente seguinte poderá receber informações pessoais;
- que nenhuma gravação, upload ou coleta foi iniciada automaticamente;
- que a pessoa poderá conhecer o processo antes de entrar;
- que poderá voltar à Home ou explorar sem personalização.

Ações iniciais de referência:

- `Continuar com segurança`;
- `Entender como funciona`;
- `Voltar à Página Inicial`;
- `Explorar sem personalização`.

## 8. Autenticação e criação de conta

A autenticação será necessária antes de persistência associada a uma pessoa, gravação de voz, envio de arquivos, conexão de fontes externas, processamento persistente ou personalização material.

Antes da autenticação, a pessoa poderá visualizar:

- etapas do fluxo;
- modalidades disponíveis;
- resumo de privacidade;
- controles de correção e exclusão;
- exigências de proteção aplicáveis;
- alternativas de exploração geral.

A criação de conta não deverá autorizar automaticamente nenhuma modalidade de processamento.

O fluxo deverá prever:

- entrada em conta existente;
- criação de conta;
- recuperação de acesso;
- retorno seguro à Home;
- explicação quando o acesso estiver restrito;
- proteção contra exposição de existência de conta ou dados pessoais.

## 9. Finalidades, privacidade e autorizações

A experiência deverá apresentar um resumo em linguagem clara e permitir acesso a detalhes adicionais.

Cada finalidade material deverá responder:

- qual informação será utilizada;
- para que será utilizada;
- qual ação ou superfície poderá ser afetada;
- por quanto tempo poderá ser mantida;
- como corrigir, limitar, retirar ou excluir;
- quais efeitos ocorrerão caso a pessoa não autorize.

Autorizações deverão ser específicas quando aplicáveis a:

- gravação de voz;
- transcrição;
- manutenção do áudio original;
- análise de arquivos;
- extração de informações;
- conexão de fonte externa;
- formação de compreensão persistente;
- personalização de possibilidades e Próximos Passos;
- uso futuro de informações para reconhecer mudanças.

A recusa de uma autorização opcional não deverá ser apresentada como falha da pessoa.

## 10. Compartilhamento mínimo e progressivo

A pessoa não precisará relatar toda a sua vida para começar.

O mínimo inicial poderá conter:

- o que está acontecendo agora;
- o que deseja compreender ou mudar;
- uma necessidade, possibilidade ou prioridade principal;
- limites ou preferências relevantes;
- o que não deseja receber ou considerar.

Perguntas adicionais somente deverão aparecer quando:

- a utilidade estiver explicada;
- a resposta reduzir uma incerteza material;
- a pessoa puder adiar ou recusar;
- existirem opções como `não sei`, `prefiro não informar` e `isso não se aplica`;
- a ausência de resposta não gerar culpa ou urgência artificial.

## 11. Relato por texto

A modalidade de texto deverá permitir:

- texto livre;
- perguntas progressivas opcionais;
- salvamento explícito de rascunho;
- revisão antes do processamento;
- edição e remoção de trechos;
- marcação de conteúdo que não deverá ser utilizado para personalização;
- interrupção sem perda não informada.

A interface não deverá interpretar o ato de digitar como autorização para processamento material.

## 12. Relato por voz

Antes de iniciar a gravação, a pessoa deverá receber informação clara sobre:

- início e fim da gravação;
- finalidade;
- transcrição;
- manutenção ou descarte do áudio original;
- revisão anterior ao uso material;
- correção, regravação e remoção;
- possíveis limitações de reconhecimento;
- risco de registrar informações de terceiros.

Durante a gravação, o estado deverá permanecer evidente. Depois da gravação, a pessoa poderá:

- ouvir, quando aplicável;
- revisar a transcrição;
- corrigir a transcrição;
- remover o áudio original;
- remover a transcrição;
- regravar;
- autorizar somente o conteúdo revisado.

Áudio e transcrição deverão possuir controles separados quando seus efeitos forem diferentes.

## 13. Relato por arquivos

Antes do envio, a pessoa deverá conhecer:

- formatos aceitos em etapa futura;
- finalidade do arquivo;
- tipos de informação que poderão ser extraídos;
- limites de leitura;
- tratamento de informações sensíveis ou de terceiros;
- retenção;
- remoção do arquivo e das informações derivadas;
- possibilidade de revisão antes do uso material.

Depois do envio, a superfície deverá mostrar:

- nome e tipo do arquivo;
- estado de envio;
- finalidade associada;
- extrações propostas;
- falhas ou limitações;
- controles para substituir ou remover.

O arquivo não autoriza leitura irrestrita nem uso de todas as informações nele contidas.

## 14. Revisão do que foi recebido

Antes do processamento material, a pessoa deverá visualizar um inventário compreensível:

- textos fornecidos;
- respostas rápidas;
- gravações;
- transcrições;
- arquivos;
- extrações propostas;
- fontes externas conectadas;
- itens removidos ou limitados.

A revisão deverá permitir:

- editar;
- remover;
- substituir;
- limitar finalidade;
- marcar como sensível;
- declarar informação de terceiro;
- continuar sem determinado item;
- voltar e compartilhar menos.

## 15. Estados funcionais do relato

O ambiente protegido deverá distinguir pelo menos:

| Estado | Significado |
|---|---|
| não iniciado | nenhuma informação pessoal foi recebida |
| autenticação pendente | a pessoa ainda não entrou ou criou conta |
| privacidade pendente | finalidades e controles ainda não foram compreendidos ou decididos |
| rascunho | conteúdo salvo, mas ainda não autorizado para processamento material |
| aguardando revisão | conteúdo recebido e disponível para correção |
| autorizado para processamento | a pessoa autorizou as finalidades aplicáveis |
| em processamento | a Guivos está organizando a compreensão inicial |
| ação necessária | existe falha, conflito, proteção adicional ou decisão pendente |
| compreensão disponível | síntese inicial pronta para revisão |
| pausado | o processo foi interrompido sem avanço automático |
| exclusão solicitada | a pessoa pediu remoção e deverá visualizar o efeito aplicável |
| encerrado | o relato ou a jornada foi encerrado conforme a decisão da pessoa |

Nenhum estado deverá ser substituído por mensagens vagas como `Estamos cuidando de tudo` ou `Quase lá` sem informação verificável.

## 16. Processamento visível e interrompível

Durante o processamento, a pessoa deverá saber:

- quais conteúdos foram autorizados;
- quais fontes estão sendo utilizadas;
- qual finalidade está ativa;
- se existe transcrição ou extração pendente;
- se ocorreu falha;
- se alguma informação exige revisão;
- como pausar, cancelar, remover ou substituir.

A Guivos não deverá prometer compreensão instantânea, completa ou infalível.

Quando o processamento não puder continuar, a superfície deverá explicar o que ocorreu e oferecer alternativas legítimas, como tentar novamente, remover um item, utilizar outra modalidade ou continuar sem personalização.

## 17. Pausa, retomada, retirada e exclusão

A experiência deverá distinguir:

### 17.1 Pausar

Interrompe o fluxo sem autorizar avanço automático.

### 17.2 Salvar rascunho

Mantém conteúdo para retomada, com efeito e prazo explicados.

### 17.3 Retirar uma autorização

Impede usos futuros incompatíveis e informa os efeitos sobre conteúdos e compreensões já produzidos.

### 17.4 Remover um item

Exclui ou desassocia texto, áudio, transcrição, arquivo, extração ou fonte específica conforme o efeito explicado.

### 17.5 Apagar o relato e recomeçar

Remove o conjunto aplicável e reinicia a experiência sem preservar interpretações como fatos silenciosos.

### 17.6 Encerrar a jornada

Interrompe a continuidade pessoal e informa separadamente o destino dos dados, relações e processos existentes.

A interface deverá explicar o que pode ser removido imediatamente, o que poderá exigir tratamento adicional e por quê, sem utilizar linguagem jurídica como substituto da compreensão funcional.

## 18. Informações sensíveis e de terceiros

A experiência deverá aplicar proteção adicional quando:

- a pessoa indicar conteúdo sensível;
- texto, voz ou arquivo mencionar outra pessoa;
- existir risco de exposição, coerção ou dano;
- a pessoa não possuir autoridade suficiente para compartilhar determinado conteúdo;
- a finalidade proposta exceder o necessário.

A proteção poderá incluir:

- alerta antes do envio;
- redução de escopo;
- ocultação de visualização;
- remoção de trechos;
- bloqueio de processamento incompatível;
- encaminhamento a ajuda ou canal apropriado;
- suspensão temporária da etapa.

A Guivos não deverá inferir autorização de terceiros a partir do envio realizado por uma única pessoa.

## 19. Compreensão inicial apresentada

A compreensão inicial deverá seguir a estrutura:

```text
o que você contou
→ o que foi recebido de fontes autorizadas
→ o que compreendemos até agora
→ o que foi inferido
→ o que permanece desconhecido ou contestado
→ como cada informação poderá ser utilizada
→ seus controles e alternativas
```

A pessoa poderá responder:

- `Está correto`;
- `Faz sentido parcialmente`;
- `Não faz sentido`;
- `Quero corrigir`;
- `Remover esta informação`;
- `Não usar para personalização`;
- `Contar mais`;
- `Continuar sem recomendações pessoais`;
- `Apagar e recomeçar`.

Confirmação parcial será válida. Informações não confirmadas não poderão ser promovidas silenciosamente a fatos.

## 20. Gate para personalização e Tela Hoje

A transição personalizada somente será válida quando existirem:

1. base suficiente para uma leitura inicial limitada;
2. origem e finalidade identificadas;
3. distinção entre confirmado, observado, externo autorizado, inferido, desconhecido e contestado;
4. revisão real pela pessoa;
5. correção ou limitação possível;
6. autorização compatível com o uso;
7. ausência de conflito material não resolvido;
8. explicação de incertezas e alternativas.

Quando o gate não for atendido, a pessoa poderá:

- contar mais;
- corrigir ou remover informações;
- manter o relato pausado;
- continuar a jornada sem personalização material;
- explorar o ecossistema sem personalização;
- encerrar e excluir o relato.

A Tela Hoje não deverá ser apresentada como recompensa pela exposição de mais dados.

## 21. Acessibilidade e proteção operacional

A experiência deverá prever:

- navegação por teclado;
- leitores de tela;
- texto ampliado;
- linguagem simples;
- alternativas textuais à voz;
- alternativa sem upload de arquivo;
- tempo suficiente para leitura e decisão;
- ausência de contagem regressiva artificial;
- confirmação antes de ações destrutivas;
- recuperação compreensível de falhas;
- versão essencial para baixa conectividade em etapa posterior.

## 22. Resultado da validação

O início protegido da jornada foi considerado **funcionalmente válido após reformulação**.

A validação confirma que a superfície pode avançar como hipótese arquitetural porque:

- explica o processo antes da autenticação e da coleta;
- impede coleta automática na transição da Home;
- separa criação de conta de autorização de processamento;
- exige finalidades compreensíveis e autorizações específicas quando aplicáveis;
- preserva compartilhamento mínimo e progressivo;
- trata texto, voz, arquivos e perguntas como alternativas;
- exige revisão anterior ao processamento material;
- torna estados e falhas visíveis;
- permite pausa, retomada, retirada, correção e exclusão;
- protege informações sensíveis e de terceiros;
- distingue conteúdo original, transcrição, extração e interpretação;
- apresenta compreensão inicial revisável;
- bloqueia personalização antes do gate;
- preserva exploração geral e jornada sem personalização como alternativas legítimas.

## 23. Critérios de aceite para wireframe posterior

Um wireframe do início protegido somente poderá avançar quando demonstrar:

- transição clara a partir da Home;
- explicação anterior à autenticação;
- ausência de coleta automática;
- finalidades e controles compreensíveis;
- escolha de modalidade sem coerção;
- compartilhamento mínimo;
- revisão de textos, transcrições e arquivos;
- estados de rascunho, processamento, falha, pausa e exclusão;
- compreensão inicial com fontes e incertezas;
- alternativas sem personalização;
- confirmação antes da Tela Hoje;
- acessibilidade e proteção adicional.

## 24. Limites

Esta validação não:

- cria wireframe gráfico do início protegido;
- cria referência móvel da Home;
- define textos finais de interface;
- define tecnologia de autenticação;
- define formatos, limites ou mecanismos técnicos de voz e arquivos;
- define armazenamento, criptografia ou infraestrutura;
- define modelo de inteligência artificial;
- autoriza inferências sensíveis;
- substitui análise jurídica, de segurança, privacidade ou acessibilidade especializada;
- cria protótipo navegável;
- executa testes com usuários;
- inicia Engenharia de Produto ou desenvolvimento;
- inicia a reaplicação dos testes dos Resultados Empresariais.

## 25. Próximo ponto de decisão

Depois da integração deste incremento e de nova autorização, os atos seguintes permanecem separados:

1. criar o wireframe gráfico de baixa fidelidade do início protegido da jornada;
2. criar a referência móvel da Página Inicial pública;
3. detalhar estados especializados de texto, voz e arquivos;
4. validar funcionalmente a revisão da compreensão inicial;
5. validar a transição entre a compreensão confirmada e a Tela Hoje;
6. selecionar estados alternativos e exceções para novos wireframes;
7. retomar, de forma independente, a reaplicação dos quatro testes dos Resultados Empresariais.

Nenhuma integração ou etapa posterior é iniciada automaticamente.
