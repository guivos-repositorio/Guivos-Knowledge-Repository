---
id: GKR-UX-PER003-MASTER-001
title: Jornada da Pessoa — PER-003 — Escolha de Modalidade — Documento Mestre de Superfície
status: active
version: 0.1.1
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
  - UXA-020
  - UXA-023
  - UXA-035
  - PAS-001-CC-LIFECYCLE-001
related:
  - GKR-UX-PER002-MASTER-001
  - GKR-JOURNEY-PERSON-001
  - UXA-069
  - PER-002
  - PER-003
  - PER-004
  - TRN-002
  - TRN-003
---

# Jornada da Pessoa — PER-003 — Escolha de Modalidade — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a **definição corrente de consumo de `PER-003 — Escolha de Modalidade`** para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

A superfície existe para permitir que a Pessoa escolha **como deseja começar a compartilhar seu Momento Atual**, preservando equivalência entre as modalidades já validadas, autonomia, reversibilidade e clareza sobre o que poderá acontecer depois.

Este documento não cria layout, tela final, wireframe, UI, protótipo, sistema visual ou implementação.

```text
PER-002 — ENTRADA PROTEGIDA
→ TRN-002
→ PER-003 — ESCOLHA DE MODALIDADE

PER-003
→ TEXTO
→ VOZ
→ ARQUIVO
→ PERGUNTAS OPCIONAIS

TRN-003
→ PER-004 — EXPRESSÃO POR TEXTO OU VOZ
→ CONTINUIDADE PARCIAL
```

## 2. Papel na Jornada

`PER-003` é a superfície de **decisão de modalidade de compartilhamento**.

Ela não deve transformar a escolha em captura material automática. Seu papel é apresentar as formas correntes de começar, explicar suas consequências imediatas e registrar uma escolha consciente antes de qualquer operação que dependa dessa modalidade.

As quatro escolhas validadas são:

```text
MODALIDADE 1
→ TEXTO

MODALIDADE 2
→ VOZ

MODALIDADE 3
→ ARQUIVO

MODALIDADE 4
→ PERGUNTAS OPCIONAIS
```

## 3. Autoridades e reconciliação corrente

`PER-003` é governada por `UXA-020`, `UXA-023` e `UXA-035`, conforme o Surface Registry corrente.

`UXA-035` preserva explicitamente **texto, voz, arquivo e perguntas opcionais em paridade**, sem modalidade principal pré-selecionada e com possibilidade de combinação sem obrigação.

`UXA-069` não redefine `PER-003`; sua própria tabela de cobertura separa:

```text
PER-003 — ESCOLHA DE MODALIDADE
→ UXA-020 / UXA-023 / UXA-035

PER-004 — EXPRESSÃO GUIADA POR TEXTO OU VOZ
→ UXA-069
```

Portanto, este Master preserva as quatro modalidades validadas e trata `UXA-069` apenas como contexto downstream de `PER-004`.

## 4. Continuidade conhecida e lacuna explícita

O Transition Registry possui `TRN-003 — PER-003 → PER-004` em estado parcial.

`PER-004` é definida correntemente como **Expressão por Texto ou Voz**. Não existe, no estado atual, uma superfície downstream separada contratada para executar de ponta a ponta arquivo ou perguntas opcionais.

Por isso:

```text
TEXTO
→ TRN-003
→ PER-004

VOZ
→ TRN-003
→ PER-004

ARQUIVO
→ ESCOLHA VALIDADA EM PER-003
→ CONTINUIDADE DOWNSTREAM ESPECÍFICA = NÃO CONTRATADA

PERGUNTAS OPCIONAIS
→ ESCOLHA VALIDADA EM PER-003
→ CONTINUIDADE DOWNSTREAM ESPECÍFICA = NÃO CONTRATADA
```

Design e IA **não podem inventar nova superfície, novo `PER-ID` ou novo handoff** para fechar essa lacuna.

A solução visual pode representar as quatro escolhas correntes; a execução completa de arquivo/perguntas depende de autoridade posterior que feche sua continuidade.

## 5. Job principal da Pessoa

A Pessoa precisa conseguir responder:

- quais formas de começar estão disponíveis?
- todas têm valor equivalente?
- posso escrever?
- posso falar?
- posso usar um arquivo?
- posso começar respondendo perguntas opcionais?
- alguma opção começa captura automaticamente?
- posso combinar formas sem ser obrigada?
- posso mudar de ideia antes de iniciar?
- posso sair sem compartilhar?
- o que acontece depois de cada escolha?

## 6. Origem

`PER-003` é alcançada por `TRN-002` a partir de `PER-002`.

O handoff deve preservar:

- sessão legítima quando aplicável;
- contexto protegido;
- finalidade corrente;
- controles apresentados;
- ausência de autorização ampla por autenticação;
- ausência de captura material iniciada por inferência;
- possibilidade de interrupção.

```text
TRN-002
→ LOCALLY VALIDATED

PER-003 ENTRY
→ NO MODALITY PRESELECTED
→ NO CAPTURE STARTED
→ NO MATERIAL PROCESSING STARTED
```

## 7. Estado inicial

A entrada em `PER-003` deve começar sem modalidade predefinida.

Não é permitido:

- selecionar texto por padrão apenas por simplicidade;
- selecionar voz por conveniência do dispositivo;
- selecionar arquivo por existência de upload;
- iniciar perguntas automaticamente como onboarding obrigatório;
- inferir preferência com base em uso anterior sem autoridade explícita;
- iniciar microfone;
- abrir seletor de arquivos;
- iniciar análise;
- posicionar uma modalidade como superior.

## 8. Modalidade Texto

A opção Texto deve comunicar, em nível proporcional, que:

- a Pessoa poderá escrever livremente;
- poderá começar com pouco;
- texto mais longo não significa melhor contexto;
- poderá editar antes de avançar;
- digitar não equivale a autorizar processamento material;
- conteúdo permanece distinguível como expressão de origem;
- a continuidade funcional conhecida ocorre em `PER-004`.

```text
ESCOLHER TEXTO
→ DEFINE MODALIDADE
→ NÃO ENVIA RELATO
→ NÃO INICIA ANÁLISE
→ NÃO CRIA COMPREENSÃO INICIAL
```

## 9. Modalidade Voz

A opção Voz deve comunicar, antes de qualquer ativação de microfone, que:

- gravação será explícita;
- início e fim deverão ser perceptíveis;
- poderá existir transcrição;
- áudio e transcrição podem ter controles distintos;
- será possível revisar e corrigir a transcrição quando aplicável;
- voz é opção, não obrigação;
- escolher voz não ativa gravação automaticamente;
- a continuidade funcional conhecida ocorre em preparação de voz dentro de `PER-004`.

```text
ESCOLHER VOZ
→ DEFINE MODALIDADE
→ MICROFONE AINDA NÃO ATIVADO
→ GRAVAÇÃO AINDA NÃO INICIADA
→ TRANSCRIÇÃO AINDA NÃO INICIADA
```

## 10. Modalidade Arquivo

A opção Arquivo deve permanecer disponível como forma validada de começar.

Antes de qualquer upload, a Pessoa deve conseguir compreender, em nível proporcional:

- para que um arquivo poderá ser usado;
- que escolher Arquivo não abre nem envia documento automaticamente;
- que upload exige ação posterior consciente;
- que o conteúdo de um documento não autoriza leitura irrestrita;
- que informações de terceiros exigem proteção;
- que extrações futuras deverão permanecer revisáveis;
- que formatos, limites e armazenamento não são definidos por este Master.

```text
ESCOLHER ARQUIVO
→ DEFINE MODALIDADE
→ NÃO ABRE FILE PICKER AUTOMATICAMENTE
→ NÃO FAZ UPLOAD
→ NÃO AUTORIZA EXTRAÇÃO
```

A continuidade downstream específica dessa modalidade ainda não está contratada na topologia corrente e não pode ser inventada por Design ou IA.

## 11. Modalidade Perguntas Opcionais

Perguntas opcionais permanecem uma modalidade validada de início.

A experiência deve preservar que:

- o fluxo guiado é opcional;
- cada pergunta deve ter finalidade compreensível;
- perguntas podem ser puladas;
- resposta livre deve permanecer possível quando aplicável;
- `não sei`, `prefiro não informar` ou equivalente devem existir quando materialmente necessários;
- a profundidade não pode virar questionário excessivo;
- o fluxo não pode funcionar como cadastro obrigatório disfarçado;
- a Pessoa pode interromper.

```text
ESCOLHER PERGUNTAS OPCIONAIS
→ DEFINE MODALIDADE
→ NÃO OBRIGA RESPOSTA
→ NÃO INICIA QUESTIONÁRIO COMPULSÓRIO
```

A continuidade downstream específica dessa modalidade ainda não está contratada na topologia corrente e não pode ser inferida como nova superfície.

## 12. Paridade entre as quatro modalidades

Texto, Voz, Arquivo e Perguntas Opcionais devem permanecer em **paridade funcional de escolha**.

Paridade não significa que todas tenham os mesmos controles ou riscos. Significa que nenhuma deve ser apresentada como superior, mais comprometida ou mais capaz de gerar resultado.

A solução não deve comunicar que:

- voz é mais profunda;
- texto é mais superficial;
- arquivo é mais completo;
- perguntas são mais precisas;
- uma modalidade produz resultado melhor;
- uma modalidade acelera evolução;
- uma modalidade aumenta chances de recomendação;
- combinar várias modalidades demonstra maior comprometimento.

```text
MODALIDADE
≠ MÉRITO
≠ COMPROMETIMENTO
≠ QUALIDADE HUMANA
≠ PROMESSA DE RESULTADO
```

## 13. Combinação de modalidades

`UXA-035` permite combinar modalidades sem exigir combinação.

Portanto, Design pode admitir uma escolha composta quando isso permanecer compreensível e reversível.

Regras:

- nenhuma combinação vem pré-selecionada;
- combinar não é obrigatório;
- o efeito de cada modalidade permanece distinguível;
- permissões e autorizações não são herdadas automaticamente entre modalidades;
- remover uma modalidade deve ter consequência compreensível;
- combinação envolvendo arquivo/perguntas não cria automaticamente nova rota downstream.

## 14. Troca de modalidade

Antes de qualquer captura material, a Pessoa deve poder trocar de modalidade sem penalidade.

Depois que existir conteúdo, a troca passa a depender dos contratos da captura correspondente e deve preservar efeitos sobre:

- rascunho;
- áudio;
- transcrição;
- arquivo;
- respostas;
- persistência;
- descarte;
- continuidade.

```text
ANTES DA CAPTURA
→ TROCA = LIVRE

DEPOIS DA CAPTURA
→ EFEITOS DEVEM SER EXPLICADOS
→ NÃO PODE HAVER DESCARTE SILENCIOSO
```

## 15. Informações que devem ser exibidas

A superfície deve tornar compreensível:

- que existem quatro formas validadas de começar;
- que nenhuma vem pré-selecionada;
- que todas têm valor funcional equivalente como escolha;
- consequência imediata de cada modalidade;
- que Voz não inicia microfone na escolha;
- que Arquivo não inicia upload na escolha;
- que Perguntas são opcionais;
- que Texto não inicia análise;
- que é possível voltar ou interromper;
- que combinar modalidades é opcional;
- que a continuidade downstream de arquivo/perguntas ainda não está integralmente contratada no GKR.

## 16. Informações que não devem ser exigidas

`PER-003` não deve exigir:

- descrição substantiva do Momento Atual;
- objetivo;
- prioridade;
- domínio de evolução;
- justificativa da escolha;
- motivo para preferir uma modalidade;
- dado sensível;
- upload antes da escolha consciente;
- permissão de microfone antes da preparação de voz;
- resposta a pergunta antes da escolha do fluxo guiado;
- consentimento de processamento material.

## 17. Captura e persistência

A decisão funcional própria desta superfície é a **seleção explícita de uma ou mais modalidades validadas**.

Se essa escolha precisar ser mantida tecnicamente para continuidade, a implementação futura deve tratá-la como estado funcional mínimo, sem inferir autorização adicional.

```text
MODALITY SELECTED
→ HANDOFF / FLOW CONTEXT

MODALITY SELECTED
≠ JOURNEY CONTENT
≠ CONSENT TO PROCESS
≠ PERSONALIZATION AUTHORIZATION
```

Este Master não decide onde ou por quanto tempo a escolha será persistida.

## 18. Ações e controles

A superfície deve permitir, conforme composição de Design:

- escolher Texto;
- escolher Voz;
- escolher Arquivo;
- escolher Perguntas Opcionais;
- combinar modalidades quando a solução optar por suportar a capacidade já validada;
- trocar escolha antes da captura;
- voltar a `PER-002` quando compatível;
- interromper;
- não prosseguir naquele momento;
- compreender mais sobre cada modalidade antes de confirmar.

Não deve existir ação genérica redundante que crie destino indeterminado quando as ações de escolha já são explícitas.

## 19. Feedback de seleção

Quando a Pessoa escolher uma modalidade, a solução deve fornecer feedback perceptível e não ambíguo.

O feedback deve informar:

- qual modalidade foi escolhida;
- se existe combinação;
- qual é o próximo efeito conhecido;
- que captura material ainda não começou, quando aplicável;
- possibilidade de mudar antes do início material;
- quando a continuidade downstream ainda depende de definição posterior.

A confirmação não precisa assumir uma tela adicional; pode ser resolvida dentro da mesma superfície.

## 20. Falha e indisponibilidade

Se uma modalidade estiver tecnicamente indisponível no futuro, a experiência deve:

- explicar indisponibilidade sem culpar a Pessoa;
- preservar outras modalidades legítimas;
- não ativar fallback silencioso;
- não selecionar automaticamente outra opção;
- permitir retorno ou interrupção;
- não coletar dado adicional para compensar a falha sem necessidade.

## 21. Privacidade e permissões

Escolher uma modalidade não concede automaticamente a permissão operacional correspondente.

Regras mínimas:

- Voz não autoriza microfone;
- Arquivo não autoriza abrir seletor, upload ou extração;
- Texto não autoriza análise do conteúdo futuro;
- Perguntas não autorizam inferência automática além da finalidade apresentada;
- nenhuma modalidade autoriza personalização futura por si só.

`PER-003` não deve solicitar permissões materiais antes de a operação que realmente as exige.

## 22. Linguagem e claims

A linguagem deve:

- tratar as quatro modalidades em paridade;
- evitar julgamento;
- evitar promessa de melhor resultado;
- evitar `recomendado para você` sem base legítima;
- evitar `mais completo`, `mais profundo`, `mais inteligente` ou equivalentes;
- indicar consequências imediatas com clareza;
- permitir começar com pouco;
- deixar claro que combinar modalidades é opcional.

## 23. Acessibilidade

A solução deve preservar:

- seleção compreensível sem depender apenas de cor;
- labels inequívocos;
- foco perceptível;
- navegação por teclado;
- leitura por tecnologia assistiva;
- descrição clara das consequências;
- alvo de interação adequado;
- alternativa textual a qualquer explicação audiovisual;
- nenhuma obrigação de voz;
- nenhuma obrigação de upload;
- possibilidade de pular perguntas opcionais.

## 24. Conteúdo sintético para Design

Design e prototipação podem usar conteúdo sintético para demonstrar:

- estado sem seleção;
- Texto selecionado;
- Voz selecionada;
- Arquivo selecionado;
- Perguntas Opcionais selecionadas;
- combinação simulada;
- troca de escolha;
- indisponibilidade simulada;
- retorno;
- handoff simulado para `PER-004` apenas nos caminhos correntemente contratados.

Não podem ser simulados como reais:

- permissão real de microfone;
- gravação real;
- transcrição real;
- upload real;
- extração real;
- resposta pessoal real;
- processamento real;
- preferência inferida real.

## 25. Liberdade de Design

A designer pode decidir:

- composição da escolha;
- cards, botões, listas ou outra estrutura;
- uso de ilustração ou iconografia;
- ordem visual, desde que não crie superioridade funcional;
- quantidade de passos visuais;
- feedback de seleção;
- microinterações;
- motion;
- tipografia;
- paleta;
- grid;
- responsividade;
- linguagem visual.

O GKR não impõe quatro cards, colunas, ícones específicos ou qualquer outra solução estética.

## 26. Uso por IA

Quando IA for usada para explorar `PER-003`, o contexto mínimo deve incluir:

1. `GKR-UX-PERSON-JOURNEY-READ-FIRST-001`;
2. `GKR-UX-PERSON-JOURNEY-FLOW-001`;
3. este Documento Mestre;
4. `GKR-JOURNEY-SURFACE-REGISTRY-001` e o detalhamento da Pessoa;
5. `GKR-JOURNEY-TRANSITION-REGISTRY-001`;
6. `UXA-020`;
7. `UXA-023`;
8. `UXA-035`;
9. `PAS-001-CC-LIFECYCLE-001` quando necessário;
10. `UXA-069` apenas como contexto downstream de `PER-004`, não como autoridade que redefine `PER-003`.

A IA não pode:

- remover uma das quatro modalidades validadas;
- criar quinta modalidade principal;
- transformar perguntas opcionais em questionário obrigatório;
- ativar voz automaticamente;
- iniciar upload automaticamente;
- inferir preferência;
- inventar benefício de uma modalidade;
- inventar continuidade downstream para arquivo/perguntas;
- criar novo `PER-ID`;
- materializar `PER-004` como se já estivesse documentada por este Master.

## 27. Critérios de aceite funcional

Uma futura solução visual de `PER-003` é aceitável quando:

1. Texto, Voz, Arquivo e Perguntas Opcionais permanecem disponíveis;
2. nenhuma modalidade vem selecionada por inferência;
3. as quatro opções têm paridade funcional de escolha;
4. escolher Voz não ativa gravação;
5. escolher Arquivo não inicia upload;
6. escolher Texto não inicia análise;
7. Perguntas permanecem opcionais e puláveis;
8. combinação pode existir, mas nunca é obrigatória;
9. a Pessoa consegue voltar ou interromper;
10. é possível trocar a escolha antes da captura;
11. o handoff `TRN-003 → PER-004` é preservado como continuidade parcial para texto/voz;
12. a lacuna downstream de arquivo/perguntas é preservada, não inventada;
13. nenhuma autorização material é inferida;
14. nenhuma preferência é inferida sem autoridade;
15. indisponibilidade possui fallback explícito e não coercitivo;
16. acessibilidade estrutural é preservada;
17. a solução não cria novo `PER-ID`.

## 28. Limites

Este Documento Mestre não:

- cria tela final;
- define layout;
- define copy final;
- cria Figma;
- cria protótipo;
- implementa captura;
- solicita microfone;
- implementa gravação;
- implementa transcrição;
- implementa upload;
- define formatos de arquivo;
- implementa fluxo de perguntas;
- fecha a continuidade downstream de arquivo/perguntas;
- define persistência da escolha;
- altera `TRN-002` ou `TRN-003`;
- cria nova superfície;
- autoriza Product Engineering.

## 29. Estado corrente

```text
PER-003 MASTER
→ CURRENT DESIGN DEFINITION

VALIDATED MODALITY CHOICES
→ TEXT
→ VOICE
→ FILE
→ OPTIONAL GUIDED QUESTIONS

COMBINATION
→ ALLOWED
→ NOT REQUIRED

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

TRN-003
→ PARTIAL / UNCHANGED

TEXT / VOICE CONTINUITY
→ PER-004 — EXPRESSÃO POR TEXTO OU VOZ

FILE / OPTIONAL QUESTIONS CONTINUITY
→ NOT FULLY CONTRACTED
→ MUST NOT BE INVENTED

NEXT DOCUMENT IN CONSTRUCTION SEQUENCE
→ PER-004 — EXPRESSÃO POR TEXTO OU VOZ

NEW VISUAL MATERIALIZATION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS DOCUMENT
```
