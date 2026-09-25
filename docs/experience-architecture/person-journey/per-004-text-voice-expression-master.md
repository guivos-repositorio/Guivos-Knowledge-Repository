---
id: GKR-UX-PER004-MASTER-001
title: Jornada da Pessoa — PER-004 — Expressão por Texto ou Voz — Documento Mestre de Superfície
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-25
normative: false
maturity: current_surface_design_definition
depends_on:
  - GKR-UX-PERSON-JOURNEY-READ-FIRST-001
  - GKR-UX-PERSON-JOURNEY-FLOW-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - UXA-069
  - PAS-001-CC-LIFECYCLE-001
related:
  - GKR-UX-PER003-MASTER-001
  - GKR-JOURNEY-PERSON-001
  - UXA-023
  - UXA-035
  - PER-003
  - PER-004
  - PER-005
  - TRN-003
  - TRN-004
---

# Jornada da Pessoa — PER-004 — Expressão por Texto ou Voz — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-004 — Expressão por Texto ou Voz` para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

A superfície existe para permitir que a Pessoa expresse seu Momento Atual por texto ou voz, preserve autoria e origem, revise o que produziu, peça ajuda temporária quando desejar e conclua o rascunho sem transformar captura, transcrição, síntese, compreensão, persistência ou personalização em conceitos equivalentes.

Este documento não cria tela, layout, wireframe, UI, protótipo, sistema visual ou implementação.

```text
PER-003 — ESCOLHA DE MODALIDADE
→ TRN-003
→ PER-004 — EXPRESSÃO POR TEXTO OU VOZ
→ TRN-004
→ PER-005 — INVENTÁRIO E AUTORIZAÇÃO
```

## 2. Papel na Jornada

`PER-004` é a responsabilidade de expressão e revisão anterior ao inventário.

Ela governa:

- expressão livre por texto;
- preparação e gravação por voz;
- transcrição, quando aplicável;
- revisão e correção;
- pausa, retomada e descarte;
- ajuda temporária solicitada;
- pergunta adaptativa opcional;
- separação revisável de focos;
- síntese temporária e revisável;
- decisão de seguir somente com conteúdos de origem ou incluir item derivado revisado;
- handoff para `PER-005`.

Ela não governa:

- autorização específica para preparar compreensão inicial;
- processamento material de compreensão;
- persistência da compreensão;
- personalização;
- objetivos;
- próximos passos;
- evolução;
- execução downstream de arquivo;
- execução downstream da modalidade “Perguntas Opcionais” de `PER-003`.

## 3. Entrada legítima

A entrada corrente em `PER-004` ocorre por `TRN-003`, em estado parcial.

A continuidade contratada é clara para:

```text
PER-003 / TEXTO
→ TRN-003
→ PER-004 / EXPRESSÃO POR TEXTO

PER-003 / VOZ
→ TRN-003
→ PER-004 / EXPRESSÃO POR VOZ
```

As escolhas Arquivo e Perguntas Opcionais permanecem válidas em `PER-003`, mas sua continuidade downstream específica ainda não está integralmente contratada.

Portanto:

```text
PER-004
→ NÃO ABSORVE ARQUIVO POR INFERÊNCIA
→ NÃO ABSORVE A MODALIDADE PERGUNTAS DE PER-003 POR INFERÊNCIA
```

## 4. Distinção crítica sobre “Perguntas”

Existem dois conceitos diferentes que não podem ser confundidos.

### 4.1 Perguntas Opcionais em PER-003

São uma modalidade validada de início em `PER-003`.

Sua continuidade downstream própria ainda não está integralmente contratada.

### 4.2 Pergunta adaptativa em PER-004

É uma ajuda temporária opcional que pode aparecer dentro de um fluxo já iniciado por Texto ou Voz, somente após solicitação consciente de ajuda.

```text
PER-003 / PERGUNTAS OPCIONAIS
≠
PER-004 / PERGUNTA ADAPTATIVA DE APOIO
```

A segunda não fecha a lacuna da primeira.

## 5. Estados funcionais da superfície

O Design deve ser capaz de acomodar, quando aplicável, os seguintes estados funcionais dentro da mesma responsabilidade:

1. orientação comum;
2. rascunho por texto;
3. preparação para voz;
4. gravação em andamento;
5. pausa de gravação;
6. revisão de transcrição;
7. retorno ao texto;
8. ajuda temporária ainda não solicitada;
9. pergunta adaptativa opcional;
10. separação revisável de focos;
11. síntese temporária;
12. decisão de seguir somente com origem ou incluir derivado;
13. pausa do rascunho;
14. retomada;
15. descarte com confirmação;
16. estado pronto para `TRN-004`.

```text
ESTADOS FUNCIONAIS
≠ TELAS CANÔNICAS
≠ NOVOS PER-IDs
```

## 6. Camadas semânticas obrigatoriamente separadas

A experiência deve distinguir quatro camadas:

| Camada | Natureza | Limite |
|---|---|---|
| conteúdo de origem | texto, voz ou correção fornecida pela Pessoa | permanece distinguível e revisável |
| ajuda temporária solicitada | organização, pergunta, separação, síntese provisória | não prepara compreensão inicial |
| preparação da compreensão inicial | uso posterior de itens revisados | pertence ao inventário/autorização de `PER-005` |
| persistência e personalização | uso continuado | permanecem bloqueadas até gates posteriores |

```text
DIGITAR
≠ AUTORIZAR ANÁLISE AUTOMÁTICA

GRAVAR
≠ AUTORIZAR COMPREENSÃO

TRANSCRIÇÃO
≠ DECLARAÇÃO CONFIRMADA

SÍNTESE
≠ COMPREENSÃO INICIAL

CONTINUAR
≠ AUTORIZAR PROCESSAMENTO
```

## 7. Expressão por Texto

O fluxo por texto deve:

- permitir expressão livre;
- aceitar relato curto ou longo sem julgamento;
- permitir edição antes da continuidade;
- permitir complementação;
- permitir exclusão;
- preservar autoria;
- evitar manipulação por sugestões;
- ser acessível;
- permitir fluxo livre ou apoio opcional;
- manter conteúdo de origem distinguível;
- não interpretar silêncio ou pouca informação como falha.

A experiência deve evitar:

- análise aparente durante a digitação;
- classificação automática não solicitada;
- síntese apresentada como fato;
- pressão para escrever mais;
- mensagem de “contexto insuficiente” como culpa da Pessoa;
- transformar texto mais longo em sinal de melhor qualidade.

## 8. Ajuda temporária no Texto

A ajuda de organização deve iniciar como não solicitada.

A Pessoa pode escolher conscientemente algo equivalente a:

> Solicitar ajuda temporária para organizar este rascunho.

A ação deve explicar que:

- usa somente o rascunho atual;
- produz ajuda revisável;
- não inicia compreensão inicial;
- não persiste compreensão;
- não personaliza superfícies futuras.

A continuidade condicional pode seguir:

```text
SOLICITAR AJUDA TEMPORÁRIA
→ se houver lacuna material: pergunta opcional
→ se houver assuntos possivelmente distintos: separação revisável
→ caso contrário: síntese temporária
```

Nenhum desses caminhos é obrigatório.

## 9. Preparação para Voz

Antes de iniciar gravação, a Pessoa deve compreender:

- que o microfone ainda não está ativo;
- para que a gravação será usada;
- que poderá existir transcrição;
- que transcrição não equivale a confirmação;
- que haverá controle sobre o tratamento do áudio;
- que gravação e transcrição não autorizam compreensão inicial.

As alternativas correntes de tratamento do áudio são mutuamente exclusivas:

- manter o áudio somente até a decisão após a revisão;
- apagar automaticamente o áudio quando a transcrição estiver disponível.

Nenhuma opção vem selecionada.

A ação de iniciar gravação deve permanecer indisponível até existir uma escolha válida.

## 10. Gravação em andamento

Durante gravação:

- microfone ativo deve estar perceptível;
- tempo deve estar visível quando útil;
- tratamento do áudio deve permanecer compreensível;
- pausa deve ser possível;
- encerrar deve ser possível;
- descarte destrutivo exige confirmação;
- troca para texto não pode provocar perda silenciosa;
- orientação não deve interromper nem avaliar o relato.

Ações devem distinguir:

- pausar;
- interromper e decidir sobre esta parte;
- concluir e gerar transcrição;
- descartar com consequência visível.

## 11. Pausa

A pausa deve:

- interromper novas entradas;
- interromper gravação;
- preservar o conteúdo recebido dentro da autorização aplicável;
- indicar estado atual;
- permitir retomada;
- permitir encerramento;
- respeitar expiração e segurança.

```text
PAUSA
≠ ABANDONO
≠ RECUSA
≠ REVOGAÇÃO
```

## 12. Retomada

Retomar deve revalidar, quando aplicável:

- continuidade da sessão;
- finalidade;
- autorização aplicável;
- canal;
- conteúdo preservado;
- tempo transcorrido;
- alterações materiais;
- sensibilidade;
- necessidade de nova explicação.

Sessão expirada não pode ser retomada silenciosamente.

## 13. Rascunho e persistência

O destino do rascunho não pode ser inventado.

Enquanto armazenamento não estiver definido por autoridade própria, a experiência deve declarar estado equivalente a:

> Rascunho ainda não persistido.

Uma ação genérica “Salvar e sair” não é legítima sem declarar:

- onde será salvo;
- por quanto tempo;
- associado a qual identidade;
- com qual consequência;
- como remover.

A ação segura corrente é equivalente a:

> Pausar e ver opções de rascunho.

## 14. Transcrição

A transcrição deve permanecer distinta:

- do áudio;
- da entrada original;
- da interpretação;
- da síntese;
- da confirmação.

Estados possíveis incluem:

- pendente;
- em processamento;
- produzida;
- parcial;
- baixa confiança;
- apresentada;
- corrigida pela Pessoa;
- contestada;
- substituída;
- indisponível.

A transcrição automática não é declaração confirmada.

## 15. Revisão da Transcrição

A revisão deve distinguir:

- áudio original;
- transcrição automática;
- correções da Pessoa;
- versão que poderá ser adicionada ao rascunho.

A Pessoa deve poder:

- corrigir;
- contestar;
- voltar à gravação;
- remover áudio com confirmação;
- manter transcrição quando o áudio for removido, quando permitido;
- descartar áudio e transcrição com confirmação;
- usar somente versão revisada para continuidade.

Correção da transcrição não deve corrigir silenciosamente interpretações já produzidas.

## 16. Pergunta adaptativa de apoio

Uma pergunta adaptativa dentro de `PER-004` só pode existir após ajuda temporária solicitada.

Ela deve informar:

- qual lacuna foi identificada;
- por que a resposta pode reduzir incerteza;
- que alternativas são exemplos, não recomendações;
- que nenhuma opção vem marcada;
- que texto livre permanece disponível;
- que é permitido manter a dimensão em aberto;
- que “não sei ainda” é legítimo;
- que “prefiro não informar” é legítimo;
- que responder adiciona conteúdo ao rascunho, mas não autoriza compreensão ou recomendação.

## 17. Separação de Focos

A experiência não deve afirmar de forma conclusiva que existem assuntos separados.

A formulação correta é equivalente a:

> O rascunho pode mencionar mais de um assunto.

A Pessoa pode:

- manter a relação em aberto;
- manter assuntos juntos;
- usar um como foco e outro como condição;
- separar em dois assuntos revisáveis;
- deixar um trecho fora da síntese sem excluí-lo do rascunho;
- editar conteúdo de origem.

Nenhuma organização é aplicada sem ação explícita.

## 18. Síntese Temporária

A síntese deve ser apresentada como organização provisória do rascunho, não como compreensão da Guivos.

Cada bloco deve identificar, quando aplicável:

- natureza;
- origem;
- estado;
- possibilidade de editar;
- possibilidade de remover da síntese.

A síntese:

- não substitui conteúdo de origem;
- não é diagnóstico;
- não é compreensão inicial;
- não será usada automaticamente;
- pode ser descartada sem excluir o rascunho;
- pode conter desconhecidos;
- não transforma ponto em aberto em fato.

## 19. Decisão antes do Inventário

A Pessoa deve poder escolher entre:

1. continuar para o inventário usando somente conteúdos de origem;
2. revisar e adicionar síntese como item derivado;
3. voltar ao rascunho;
4. descartar somente a síntese.

Nenhuma ação implica aceitação silenciosa da organização sugerida.

## 20. Handoff para PER-005

`TRN-004 — PER-004 → PER-005` permanece parcial.

O handoff deve preservar, quando aplicável:

- conteúdos de origem revisados;
- transcrição revisada;
- síntese derivada somente se conscientemente incluída;
- itens mantidos em aberto;
- origem e natureza;
- escolhas da Pessoa;
- ausência de autorização para processamento material.

```text
PER-004 CONCLUÍDA
→ INVENTÁRIO PRONTO

INVENTÁRIO PRONTO
≠ AUTORIZADO PARA PROCESSAR
```

A autorização específica pertence a `PER-005`.

## 21. Ações e Controles

A superfície deve suportar, conforme estado:

- escrever;
- editar;
- complementar;
- excluir;
- escolher voz;
- preparar voz;
- iniciar gravação;
- pausar;
- retomar;
- concluir gravação;
- revisar transcrição;
- corrigir transcrição;
- descartar com confirmação;
- voltar ao texto;
- solicitar ajuda temporária;
- responder ou pular pergunta;
- manter dimensão em aberto;
- revisar separação;
- revisar síntese;
- usar somente origem;
- incluir derivado revisado;
- voltar;
- sair sem iniciar compreensão.

## 22. Descarte e Exclusão

Toda ação destrutiva deve declarar a consequência antes da confirmação.

A experiência deve distinguir:

- remover da síntese;
- excluir do rascunho;
- remover áudio;
- remover transcrição;
- descartar ambos;
- sair sem salvar;
- manter rascunho.

Remover de uma representação derivada não pode excluir automaticamente a fonte.

## 23. Falhas

Falhas possíveis incluem:

- microfone indisponível;
- permissão negada;
- gravação interrompida;
- transcrição indisponível;
- transcrição parcial;
- baixa confiança;
- sessão expirada;
- retomada inválida;
- ajuda temporária indisponível.

A experiência deve:

- informar o estado;
- preservar o que puder ser preservado legitimamente;
- oferecer alternativa quando possível;
- nunca fabricar transcrição;
- nunca apresentar síntese como se estivesse completa;
- nunca trocar de canal silenciosamente.

## 24. Privacidade e Finalidade

A superfície deve preservar:

- finalidade específica;
- minimização;
- autoria;
- proveniência;
- proteção de terceiros;
- separação entre captura e usos posteriores;
- ausência de consentimento genérico;
- possibilidade de pausar;
- possibilidade de abandonar;
- possibilidade de revisão;
- possibilidade de descarte.

Gravação não autoriza inferir:

- personalidade;
- emoção;
- saúde;
- intenção;
- diagnóstico;
- risco clínico,

sem contrato legítimo específico.

## 25. Linguagem

A linguagem deve:

- permitir começar com pouco;
- não pressionar por profundidade;
- não sugerir que mais conteúdo é melhor;
- não avaliar a Pessoa;
- não diagnosticar;
- não transformar organização temporária em verdade;
- diferenciar fonte, transcrição e derivado;
- declarar consequência antes de perda;
- manter desconhecidos legítimos.

## 26. Acessibilidade

A solução deve considerar:

- uso integral por teclado;
- foco visível;
- labels claros;
- indicação de gravação não dependente somente de cor;
- alternativa ao uso de voz;
- transcrição revisável;
- mensagens de erro acessíveis;
- controles destrutivos claramente identificados;
- ausência de motion indispensável para entender estado;
- suporte a zoom e responsividade.

## 27. Conteúdo Sintético para Design

Design pode simular:

- rascunho fictício;
- áudio simulado;
- transcrição sintética;
- transcrição com erro simulado;
- pergunta adaptativa fictícia;
- separação de focos fictícia;
- síntese temporária fictícia;
- pausa;
- retomada;
- falha;
- descarte;
- handoff simulado para `PER-005`.

Não pode apresentar como real:

- gravação real;
- microfone real;
- transcrição real;
- análise real;
- persistência real;
- compreensão real;
- personalização real;
- autorização real;
- dado pessoal real.

## 28. Liberdade de Design

A designer pode decidir:

- quantidade de frames;
- composição;
- componentes;
- estrutura do editor;
- tratamento visual da gravação;
- tratamento visual da transcrição;
- forma de pausa;
- forma de síntese;
- forma de perguntas;
- iconografia;
- tipografia;
- paleta;
- motion;
- microinterações;
- responsividade.

O GKR não define baseline visual para `PER-004`.

## 29. Uso por IA

Quando IA for usada para explorar `PER-004`, o contexto mínimo deve incluir:

1. `GKR-UX-PERSON-JOURNEY-READ-FIRST-001`;
2. `GKR-UX-PERSON-JOURNEY-FLOW-001`;
3. este Documento Mestre;
4. `GKR-JOURNEY-SURFACE-REGISTRY-001` e detalhamento da Pessoa;
5. `GKR-JOURNEY-TRANSITION-REGISTRY-001`;
6. `UXA-069`;
7. `PAS-001-CC-LIFECYCLE-001`;
8. `GKR-UX-PER003-MASTER-001` para a fronteira de entrada;
9. `UXA-023/035` apenas quando necessário para a fronteira com inventário/autorização.

A IA não pode:

- absorver Arquivo ou a modalidade Perguntas de `PER-003` por inferência;
- transformar ajuda temporária em compreensão;
- iniciar análise automática durante digitação;
- selecionar tratamento do áudio;
- inventar persistência de rascunho;
- confirmar transcrição automaticamente;
- excluir fonte ao remover derivado;
- criar novo `PER-ID`;
- autorizar processamento;
- materializar `PER-005` como se estivesse definido por este Master.

## 30. Critérios de Aceite Funcional

Uma futura solução visual de `PER-004` é aceitável quando:

1. Texto e Voz permanecem equivalentes;
2. origem, transcrição e derivado permanecem distintos;
3. digitar não inicia análise automática;
4. voz não inicia sem ação explícita;
5. tratamento do áudio exige escolha consciente;
6. gravação ativa é perceptível;
7. pausa não equivale a abandono;
8. descarte destrutivo exige consequência visível;
9. transcrição automática não é tratada como confirmada;
10. correção permanece possível;
11. ajuda temporária exige solicitação consciente;
12. pergunta adaptativa é opcional;
13. separação de focos é revisável;
14. síntese é temporária e não substitui origem;
15. a Pessoa pode seguir somente com conteúdos de origem;
16. rascunho não possui destino de persistência inventado;
17. `TRN-004` entrega inventário sem autorização implícita;
18. arquivo/perguntas de `PER-003` não são absorvidos por inferência;
19. nenhuma nova superfície é criada;
20. Product Engineering permanece não liberado.

## 31. Limites

Este Documento Mestre não:

- cria tela final;
- cria Figma;
- cria protótipo;
- define algoritmo;
- define modelo de IA;
- implementa gravação;
- implementa transcrição;
- implementa storage;
- define retenção jurídica final;
- implementa exclusão;
- materializa upload de arquivo;
- fecha a modalidade Perguntas de `PER-003`;
- cria protocolo clínico;
- executa teste com pessoas;
- conclui acessibilidade técnica;
- altera `TRN-003` ou `TRN-004`;
- cria `PER-005`;
- inicia Product Engineering.

## 32. Estado Corrente

```text
PER-004 MASTER
→ CURRENT DESIGN DEFINITION

ENTRY
→ PER-003 / TEXT
→ PER-003 / VOICE

FILE / PER-003 OPTIONAL QUESTIONS
→ NOT ABSORBED
→ DOWNSTREAM GAP PRESERVED

TEXT
→ FREE EXPRESSION
→ EDITABLE
→ NO AUTOMATIC ANALYSIS

VOICE
→ EXPLICIT PREPARATION
→ EXPLICIT RECORDING
→ REVIEWABLE TRANSCRIPTION

TEMPORARY HELP
→ USER-REQUESTED
→ OPTIONAL
→ NOT INITIAL UNDERSTANDING

DRAFT PERSISTENCE
→ NOT INVENTED

TRN-003
→ PARTIAL / UNCHANGED

TRN-004
→ PARTIAL / UNCHANGED

NEXT DOCUMENTATION TARGET
→ PER-005 — INVENTÁRIO E AUTORIZAÇÃO

NEW VISUAL MATERIALIZATION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS DOCUMENT
```
