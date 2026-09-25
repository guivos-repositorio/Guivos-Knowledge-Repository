---
id: GKR-UX-PER003-MASTER-001
title: Jornada da Pessoa — PER-003 — Escolha de Modalidade — Documento Mestre de Superfície
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
  - UXA-020
  - UXA-023
  - UXA-035
  - UXA-069
  - PAS-001-CC-LIFECYCLE-001
related:
  - GKR-UX-PER002-MASTER-001
  - GKR-JOURNEY-PERSON-001
  - PER-002
  - PER-003
  - PER-004
  - TRN-002
  - TRN-003
---

# Jornada da Pessoa — PER-003 — Escolha de Modalidade — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a **definição corrente de consumo de `PER-003 — Escolha de Modalidade`** para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

A superfície existe para permitir que a Pessoa escolha **como deseja iniciar sua expressão principal do Momento Atual**, preservando equivalência entre canais, autonomia, reversibilidade e clareza sobre o que acontecerá em seguida.

Este documento não cria layout, tela final, wireframe, UI, protótipo, sistema visual ou implementação.

```text
PER-002 — ENTRADA PROTEGIDA
→ TRN-002
→ PER-003 — ESCOLHA DE MODALIDADE
→ TRN-003
→ PER-004 — EXPRESSÃO GUIADA
```

## 2. Papel na Jornada

`PER-003` é a superfície de **decisão de canal principal de expressão**.

Ela não deve capturar o relato substantivo em si como responsabilidade principal. Seu papel é permitir que a Pessoa escolha conscientemente entre os canais principais atualmente reconhecidos:

```text
CANAL PRINCIPAL 1
→ TEXTO

CANAL PRINCIPAL 2
→ VOZ
```

A escolha prepara o handoff para `PER-004`, onde a expressão efetivamente acontece.

## 3. Reconciliação corrente das modalidades

As autoridades anteriores preservam texto, voz, arquivos e perguntas progressivas como capacidades possíveis da Captura de Contexto. Entretanto, o Registry corrente da Pessoa e `UXA-069` fixam `PER-003` como escolha entre **texto e voz**.

Portanto:

```text
PER-003
→ ESCOLHA PRINCIPAL = TEXTO OU VOZ

PERGUNTAS GUIADAS
→ RECURSO OPCIONAL DE APOIO
→ NÃO SÃO CANAL PRINCIPAL INDEPENDENTE NESTA SUPERFÍCIE

ARQUIVOS
→ CAPACIDADE AUXILIAR / CONDICIONAL
→ NÃO SÃO CANAL PRINCIPAL INDEPENDENTE NESTA SUPERFÍCIE
```

Uma mudança futura nessa taxonomia exige alteração explícita nas autoridades correntes; Design ou IA não podem transformar capacidades auxiliares em novas modalidades principais por conveniência.

## 4. Job principal da Pessoa

A Pessoa precisa conseguir responder:

- posso começar escrevendo ou falando?
- as duas opções têm valor equivalente?
- escolher voz ativa o microfone imediatamente?
- escolher texto inicia processamento imediatamente?
- posso mudar de ideia antes de começar?
- perguntas guiadas serão obrigatórias?
- arquivo é necessário para prosseguir?
- o que acontece depois da escolha?

## 5. Origem

`PER-003` é alcançada por `TRN-002` a partir de `PER-002`.

O handoff deve preservar:

- sessão legítima quando aplicável;
- contexto protegido;
- finalidade corrente;
- controles apresentados;
- ausência de autorização ampla por autenticação;
- ausência de relato material ainda não iniciado;
- possibilidade de interrupção.

```text
TRN-002
→ LOCALLY VALIDATED

PER-003 ENTRY
→ NÃO PRESUME MODALIDADE
→ NÃO PRESUME CAPTURA
→ NÃO PRESUME PROCESSAMENTO
```

## 6. Destino

O destino funcional próprio de `PER-003` é `PER-004 — Expressão Guiada`, via `TRN-003`.

`TRN-003` permanece parcial. Portanto, este Master governa o que precisa ser preservado na escolha, mas não promove a integração completa entre escolha e expressão.

```text
ESCOLHA DE TEXTO
→ HANDOFF PARA ESTADO DE EXPRESSÃO POR TEXTO EM PER-004

ESCOLHA DE VOZ
→ HANDOFF PARA PREPARAÇÃO DE VOZ EM PER-004

ESCOLHA
≠ CAPTURA CONCLUÍDA
≠ RELATO ENVIADO
≠ AUTORIZAÇÃO DE PROCESSAMENTO
```

## 7. Estado inicial

A entrada em `PER-003` deve começar sem modalidade predefinida por inferência.

```text
DEFAULT
→ NO PRIMARY MODALITY SELECTED
```

Não é permitido:

- selecionar texto por padrão apenas por simplicidade;
- selecionar voz por padrão por conveniência de dispositivo;
- inferir preferência com base em uso anterior sem autoridade explícita;
- iniciar microfone automaticamente;
- posicionar uma opção como moralmente superior;
- esconder a alternativa equivalente.

## 8. Modalidade Texto

A opção Texto deve comunicar, em nível proporcional, que:

- a Pessoa poderá escrever livremente;
- poderá começar com pouco;
- texto mais longo não significa melhor contexto;
- poderá editar antes de avançar;
- perguntas guiadas, quando aparecerem, são opcionais;
- digitar não equivale a autorizar processamento material;
- conteúdo permanece distinguível como expressão de origem;
- a continuidade ocorrerá em `PER-004`.

```text
ESCOLHER TEXTO
→ DEFINE CANAL PRINCIPAL
→ NÃO ENVIA RELATO
→ NÃO INICIA ANÁLISE
→ NÃO CRIA COMPREENSÃO INICIAL
```

## 9. Modalidade Voz

A opção Voz deve comunicar, antes de qualquer ativação de microfone, que:

- gravação será explícita;
- início e fim serão perceptíveis;
- poderá existir transcrição;
- áudio e transcrição podem ter controles distintos;
- será possível revisar e corrigir a transcrição quando aplicável;
- voz é opção, não obrigação;
- escolher voz não ativa gravação automaticamente;
- a continuidade ocorrerá em preparação de voz dentro de `PER-004`.

```text
ESCOLHER VOZ
→ DEFINE CANAL PRINCIPAL
→ MICROFONE AINDA NÃO ATIVADO
→ GRAVAÇÃO AINDA NÃO INICIADA
→ TRANSCRIÇÃO AINDA NÃO INICIADA
```

## 10. Equivalência entre Texto e Voz

Texto e voz devem possuir **valor funcional equivalente**.

A solução não deve comunicar que:

- voz é mais profunda;
- texto é mais superficial;
- falar é mais autêntico;
- escrever é mais racional;
- uma opção produz resultado melhor;
- uma opção acelera evolução;
- uma opção aumenta chances de recomendação.

```text
TEXTO
≠ MENOR QUALIDADE

VOZ
≠ MAIOR PROFUNDIDADE

CANAL
≠ MÉRITO
≠ COMPROMETIMENTO
```

## 11. Perguntas guiadas

Perguntas progressivas não constituem modalidade principal independente em `PER-003`.

Elas podem ser apresentadas posteriormente quando:

- a utilidade estiver explicada;
- reduzirem incerteza material;
- forem opcionais;
- permitirem `não sei`, `prefiro não informar` ou equivalente;
- a Pessoa puder pular;
- não funcionarem como cadastro obrigatório disfarçado.

Em `PER-003`, Design pode informar que ajuda guiada poderá existir, mas não deve exigir que a Pessoa escolha antecipadamente um “modo questionário” como condição de entrada.

## 12. Arquivos e documentos

Arquivos permanecem capacidade auxiliar/condicional da Captura de Contexto.

`PER-003` não deve exigir upload nem apresentar arquivo como terceira modalidade principal sem nova autoridade.

Quando arquivos forem utilizados posteriormente, deverão respeitar:

- necessidade;
- finalidade;
- proporcionalidade;
- proteção;
- proveniência;
- retenção limitada;
- revisão;
- possibilidade de remoção;
- ausência de extração irrestrita.

## 13. Combinação e troca de canais

A arquitetura funcional admite continuidade entre voz e texto.

Em `PER-003`, antes de existir conteúdo material, a Pessoa deve poder trocar livremente de escolha.

Depois que conteúdo existir, a troca passa a pertencer ao contrato de `PER-004` e deve preservar efeitos sobre:

- rascunho existente;
- áudio existente;
- transcrição existente;
- persistência;
- descarte;
- continuidade.

```text
ANTES DA CAPTURA
→ TROCA DE TEXTO ↔ VOZ = LIVRE

DEPOIS DA CAPTURA
→ TROCA = GOVERNADA POR PER-004
→ NÃO DECIDIDA POR PER-003
```

## 14. Informações que devem ser exibidas

A superfície deve tornar compreensível:

- que existem dois canais principais correntes: texto e voz;
- que ambos são opcionais e equivalentes;
- o que acontece imediatamente após cada escolha;
- que nenhuma gravação começa na escolha;
- que nenhuma análise material começa na escolha;
- que a Pessoa pode voltar;
- que pode mudar de escolha antes de iniciar captura;
- que compartilhar pouco é legítimo;
- que ajuda guiada pode ser opcional posteriormente;
- que arquivos não são exigência para iniciar.

## 15. Informações que não devem ser exigidas

`PER-003` não deve exigir:

- descrição do Momento Atual;
- objetivo;
- prioridade;
- domínio de evolução;
- justificativa da escolha;
- motivo para preferir texto ou voz;
- dado sensível;
- upload;
- permissão de microfone antes da escolha de voz;
- consentimento de processamento material.

## 16. Captura e persistência

A única decisão funcional própria desta superfície é a **seleção explícita do canal principal**.

Se essa escolha precisar ser mantida tecnicamente para o handoff, a implementação futura deve tratá-la como estado funcional mínimo, sem inferir autorização adicional.

```text
MODALITY SELECTED
→ HANDOFF CONTEXT

MODALITY SELECTED
≠ JOURNEY CONTENT
≠ CONSENT TO PROCESS
≠ PERSONALIZATION AUTHORIZATION
```

Este Master não decide onde ou por quanto tempo a escolha será persistida.

## 17. Ações e controles

A superfície deve permitir, conforme composição de Design:

- escolher Texto;
- escolher Voz;
- trocar escolha antes da captura;
- voltar a `PER-002` quando compatível;
- interromper;
- não prosseguir naquele momento;
- compreender mais sobre cada opção antes de confirmar.

Não deve existir ação genérica redundante que crie destino indeterminado quando as ações de Texto e Voz já são diretas e equivalentes.

## 18. Feedback de seleção

Quando a Pessoa escolher uma modalidade, a solução deve fornecer feedback perceptível e não ambíguo.

O feedback deve informar:

- qual modalidade foi escolhida;
- qual é o próximo efeito;
- que a captura ainda não começou, quando aplicável;
- possibilidade de mudar antes do início material.

A confirmação não precisa assumir uma tela adicional; pode ser resolvida dentro da mesma superfície.

## 19. Falha e indisponibilidade

Se uma modalidade estiver tecnicamente indisponível no futuro, a experiência deve:

- explicar indisponibilidade sem culpar a Pessoa;
- preservar a outra modalidade quando legítima;
- não declarar equivalência se uma opção não está operacional naquele momento;
- não ativar fallback silencioso;
- permitir retorno ou interrupção;
- não coletar dado adicional para compensar a falha sem necessidade.

Exemplo:

```text
VOICE TEMPORARILY UNAVAILABLE
→ INFORM
→ OFFER TEXT WHEN LEGITIMATE
→ DO NOT AUTO-SWITCH
```

## 20. Privacidade e permissões

Escolher Voz não autoriza microfone. Permissão de microfone deve ocorrer apenas quando necessária para iniciar a captura em `PER-004`, com indicação clara de finalidade.

Escolher Texto não autoriza análise do conteúdo futuro.

`PER-003` não deve solicitar permissões de:

- microfone;
- câmera;
- arquivos;
- localização;
- contatos;
- fontes externas;

salvo se uma autoridade futura demonstrar necessidade específica — hipótese não criada por este documento.

## 21. Linguagem e claims

A linguagem deve:

- tratar os canais com equivalência;
- evitar julgamento;
- evitar promessa de melhor resultado;
- evitar “recomendado para você” sem base legítima;
- evitar “mais completo”, “mais profundo” ou “mais inteligente” para uma modalidade;
- indicar consequências imediatas com clareza;
- permitir começar com pouco.

## 22. Acessibilidade

A solução deve preservar:

- seleção compreensível sem depender apenas de cor;
- labels inequívocos;
- foco perceptível;
- navegação por teclado;
- leitura por tecnologia assistiva;
- descrição clara das consequências;
- alvo de interação adequado;
- alternativa textual a qualquer explicação audiovisual;
- nenhuma obrigação de voz para pessoas que não possam ou não queiram falar.

## 23. Conteúdo sintético para Design

Design e prototipação podem usar conteúdo sintético para demonstrar:

- estado sem seleção;
- Texto selecionado;
- Voz selecionada;
- troca de escolha;
- indisponibilidade simulada de um canal;
- retorno;
- handoff simulado para `PER-004`.

Não podem ser simulados como reais:

- permissão real de microfone;
- gravação real;
- transcrição real;
- dado pessoal real;
- processamento real;
- recomendação real de modalidade;
- preferência inferida real.

## 24. Liberdade de Design

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

O GKR não impõe duas colunas, cards equivalentes, ícones específicos ou qualquer outra solução estética.

## 25. Uso por IA

Quando IA for usada para explorar `PER-003`, o contexto mínimo deve incluir:

1. `GKR-UX-PERSON-JOURNEY-READ-FIRST-001`;
2. `GKR-UX-PERSON-JOURNEY-FLOW-001`;
3. este Documento Mestre;
4. Registry da Pessoa;
5. Transition Registry;
6. `UXA-069`;
7. `PAS-001-CC-LIFECYCLE-001` quando necessário.

A IA não pode:

- criar terceira modalidade principal;
- transformar perguntas em questionário obrigatório;
- ativar voz automaticamente;
- exigir arquivo;
- inferir preferência;
- inventar benefício de uma modalidade;
- criar nova superfície;
- materializar `PER-004` como se já estivesse documentada por este Master.

## 26. Critérios de aceite funcional

Uma futura solução visual de `PER-003` é aceitável quando:

1. Texto e Voz aparecem como canais principais correntes;
2. nenhuma modalidade vem selecionada por inferência;
3. as duas opções têm valor funcional equivalente;
4. escolher Voz não ativa gravação;
5. escolher Texto não inicia análise;
6. perguntas guiadas permanecem opcionais e não são terceiro canal principal;
7. arquivos não são exigidos nem promovidos a modalidade principal;
8. a Pessoa consegue voltar ou interromper;
9. é possível trocar a escolha antes da captura;
10. o handoff para `PER-004` é compreensível;
11. nenhuma autorização material é inferida;
12. nenhuma preferência é inferida sem autoridade;
13. indisponibilidade de canal possui fallback explícito e não coercitivo;
14. acessibilidade estrutural é preservada;
15. a solução não cria novo `PER-ID`.

## 27. Limites

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
- define persistência da escolha;
- altera `TRN-002` ou `TRN-003`;
- cria `PER-004`;
- autoriza Product Engineering.

## 28. Estado corrente

```text
PER-003 MASTER
→ CURRENT DESIGN DEFINITION

PRIMARY MODALITIES
→ TEXT
→ VOICE

GUIDED QUESTIONS
→ OPTIONAL SUPPORT CAPABILITY

FILES
→ AUXILIARY / CONDITIONAL CAPABILITY

TRN-002
→ LOCALLY VALIDATED / UNCHANGED

TRN-003
→ PARTIAL / UNCHANGED

NEXT DOCUMENT IN CONSTRUCTION SEQUENCE
→ PER-004 — EXPRESSÃO POR TEXTO OU VOZ

NEW VISUAL MATERIALIZATION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS DOCUMENT
```
