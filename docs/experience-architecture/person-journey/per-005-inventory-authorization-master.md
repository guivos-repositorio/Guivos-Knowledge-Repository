---
id: GKR-UX-PER005-MASTER-001
title: Jornada da Pessoa — PER-005 — Inventário e Autorização — Documento Mestre de Superfície
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
  - UXA-023
  - UXA-035
related:
  - GKR-UX-PER004-MASTER-001
  - GKR-JOURNEY-PERSON-001
  - PER-004
  - PER-005
  - PER-006
  - TRN-004
  - TRN-005
---

# Jornada da Pessoa — PER-005 — Inventário e Autorização — Documento Mestre de Superfície

## 1. Finalidade

Este documento consolida a definição corrente de consumo de `PER-005 — Inventário e Autorização` para designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia.

A superfície existe para permitir que a Pessoa veja o que foi recebido, distinga natureza e finalidade dos itens, revise o conjunto aplicável e decida conscientemente quais conteúdos poderão ser usados para preparar uma compreensão inicial temporária e revisável.

Este documento não cria tela, layout, wireframe, UI, protótipo, sistema visual ou implementação.

```text
PER-004 — EXPRESSÃO POR TEXTO OU VOZ
→ TRN-004 / PARCIAL
→ PER-005 — INVENTÁRIO E AUTORIZAÇÃO
→ TRN-005 / PARCIAL
→ PER-006 — PROCESSAMENTO VISÍVEL
```

## 2. Papel na Jornada

`PER-005` é a responsabilidade de revisão e autorização anterior ao processamento material.

Ela governa:

- inventário compreensível do conteúdo recebido;
- distinção entre conteúdo de origem, transcrição, derivado e item removido ou limitado;
- finalidade aplicável a cada uso material;
- seleção consciente dos itens elegíveis;
- autorização específica para preparar compreensão inicial temporária e revisável;
- recusa sem início de processamento;
- revisão, remoção, limitação, retorno e retirada quando aplicável;
- handoff governado para `PER-006`.

Ela não governa:

- processamento material;
- formação ou apresentação da compreensão inicial;
- persistência da compreensão;
- personalização;
- decisão posterior sobre persistência ou personalização;
- implementação de storage, retenção, exclusão ou mecanismos jurídicos finais.

## 3. Entrada legítima

A entrada corrente ocorre por `TRN-004 — PER-004 → PER-005`, que permanece parcial.

O contrato corrente de `PER-004` permite entregar, quando aplicável:

- conteúdos de origem revisados;
- transcrição revisada;
- síntese derivada somente quando conscientemente incluída;
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

A parcialidade de `TRN-004` não é promovida por este Master.

## 4. Job da Pessoa

A Pessoa precisa conseguir responder, antes de qualquer processamento material:

1. o que a Guivos recebeu;
2. qual é a natureza de cada item;
3. qual item poderá ser usado;
4. para qual finalidade;
5. qual resultado intermediário será preparado;
6. o que acontecerá se não autorizar;
7. como corrigir, limitar, remover ou voltar;
8. se existe algo ainda desconhecido, contestado ou não elegível.

## 5. Inventário compreensível

Quando existirem legitimamente, o inventário pode representar:

- textos fornecidos;
- respostas opcionais;
- gravações;
- transcrições;
- arquivos;
- extrações propostas;
- fontes externas conectadas;
- itens derivados revisados;
- itens removidos ou limitados.

A presença nesta lista não autoriza o Design ou a IA a inventar uma modalidade downstream ainda não contratada.

Em especial:

```text
ARQUIVO / PER-003 OPTIONAL QUESTIONS
→ CONTINUIDADE DOWNSTREAM ESPECÍFICA AINDA NÃO INTEGRALMENTE CONTRATADA
→ NÃO MATERIALIZAR POR INFERÊNCIA
```

## 6. Natureza e proveniência

A experiência deve manter distinguíveis, quando aplicável:

| Natureza | Regra |
|---|---|
| conteúdo de origem | fornecido diretamente pela Pessoa |
| gravação | fonte de voz, com tratamento próprio |
| transcrição | representação automática/revisável; não é confirmação automática |
| extração proposta | derivação que exige clareza de origem e revisão aplicável |
| item derivado revisado | conteúdo conscientemente incluído a partir de ajuda temporária |
| removido ou limitado | não pode reaparecer silenciosamente como elegível |
| desconhecido ou contestado | permanece explicitamente não resolvido |

Remover uma representação derivada não pode excluir silenciosamente sua fonte, e remover a fonte não autoriza preservar derivados sem fundamento e explicação aplicáveis.

## 7. Finalidade corrente

Nesta etapa, a finalidade material ilustrada e contratada é:

> usar somente os itens conscientemente autorizados para preparar uma compreensão inicial temporária e revisável.

```text
AUTORIZAR PREPARAÇÃO DA COMPREENSÃO INICIAL
≠ AUTORIZAR PERSISTÊNCIA DA COMPREENSÃO
≠ AUTORIZAR PERSONALIZAÇÃO
≠ AUTORIZAR USO FUTURO IRRESTRITO
```

Persistência e personalização permanecem bloqueadas até gates posteriores.

## 8. Autorizações específicas

As autorizações devem:

- ser específicas;
- iniciar desmarcadas;
- identificar o item ou conjunto legitimamente agrupado;
- identificar a finalidade;
- explicar o resultado intermediário;
- explicar o efeito da recusa;
- não ser inferidas da autenticação;
- não ser inferidas da captura;
- não ser inferidas da revisão;
- não ser inferidas da continuidade para esta superfície.

Uma confirmação genérica não substitui autorizações específicas quando efeitos diferentes exigirem decisões diferentes.

## 9. Seleção de itens

A Pessoa deve poder decidir quais itens elegíveis poderão participar da preparação da compreensão inicial.

O Design deve preservar:

- ausência de seleção automática;
- possibilidade de revisar antes de autorizar;
- possibilidade de retirar item da seleção;
- distinção entre remover do uso atual e excluir a fonte;
- visibilidade de itens limitados ou não elegíveis quando isso for necessário para compreender o estado;
- ausência de pressão para autorizar mais conteúdo.

Mais itens autorizados não significam automaticamente melhor compreensão.

## 10. Recusa

A recusa é uma decisão legítima.

A autoridade corrente distingue:

- autorizar somente os itens marcados para preparar a compreensão inicial;
- não autorizar processamento e voltar a explorar.

```text
NÃO AUTORIZAR
→ NÃO INICIA COMPREENSÃO
→ NÃO INICIA PERSISTÊNCIA
→ NÃO INICIA PERSONALIZAÇÃO
```

A recusa de uma finalidade opcional não deve ser apresentada como erro, falha, perda de comprometimento ou insuficiência da Pessoa.

## 11. Revisão e correção

Antes de autorizar, a Pessoa deve poder, conforme a natureza do item:

- revisar;
- corrigir;
- voltar à origem quando a autoridade permitir;
- remover;
- limitar;
- contestar;
- manter em aberto;
- excluir da seleção de uso atual.

A superfície não deve corrigir silenciosamente conteúdo de origem, transcrição ou derivado.

## 12. Retorno para PER-004

Quando a Pessoa precisar alterar o conteúdo que pertence à responsabilidade de expressão/revisão, o Design pode oferecer retorno compatível com o contrato corrente.

Esse retorno:

- não cria nova autorização;
- não preserva seleção inválida silenciosamente;
- não transforma `TRN-004` em integralmente validada;
- deve exigir nova revisão quando houver mudança material no inventário.

## 13. Pausa, saída, remoção e exclusão

A experiência deve distinguir efeitos diferentes:

- pausar;
- salvar rascunho, somente quando persistência estiver legitimamente definida;
- sair;
- retirar autorização;
- remover item;
- excluir fonte;
- apagar relato e recomeçar;
- voltar a explorar sem processamento.

A ação destrutiva deve explicar sua consequência antes da confirmação.

Este Master não define armazenamento, retenção ou política jurídica final.

## 14. Informações de terceiros e sensibilidade

Quando um item puder conter informação de terceiros ou conteúdo sensível, a experiência deve:

- sinalizar a necessidade de cuidado proporcional;
- permitir revisão e remoção;
- limitar uso ao necessário e autorizado;
- não inferir autorização de terceiros;
- não exigir exposição adicional para prosseguir;
- bloquear uso incompatível quando a proteção aplicável não estiver satisfeita.

## 15. Estados funcionais

O Design deve conseguir acomodar, quando aplicável:

1. inventário recebido;
2. revisão de item;
3. item corrigido;
4. item removido ou limitado;
5. item contestado ou em aberto;
6. nenhuma autorização selecionada;
7. seleção parcial;
8. autorização pronta para confirmação;
9. autorização confirmada;
10. recusa de processamento;
11. ação necessária;
12. pausa;
13. retorno para revisão;
14. estado pronto para `TRN-005`.

```text
ESTADOS FUNCIONAIS
≠ TELAS CANÔNICAS
≠ NOVOS PER-IDs
```

## 16. Estado pronto para processamento

Somente itens revisados e conscientemente autorizados podem compor o handoff material para `PER-006`.

O estado deve preservar, quando aplicável:

- identificador lógico do item;
- natureza;
- proveniência;
- finalidade autorizada;
- limites ou exclusões;
- estado de revisão;
- autorização registrada;
- itens não autorizados fora do conjunto de processamento.

Nenhum dado adicional pode ser inferido como autorizado apenas porque está disponível tecnicamente.

## 17. Handoff para PER-006

`TRN-005 — PER-005 → PER-006` permanece parcial.

```text
INVENTÁRIO REVISADO
→ AUTORIZAÇÃO ESPECÍFICA
→ TRN-005 / PARCIAL
→ PER-006 — PROCESSAMENTO VISÍVEL
```

A passagem não autoriza:

- persistência da compreensão;
- personalização;
- uso futuro irrestrito;
- expansão silenciosa de finalidade.

Referências visuais paralelas não são autoridade corrente para promover `TRN-005`.

## 18. Falhas e ação necessária

A experiência deve prever, sem inventar mecanismo técnico:

- item indisponível;
- origem não identificável;
- conflito entre fonte e derivado;
- autorização incompleta;
- item que exige nova revisão;
- proteção adicional necessária;
- alteração material após seleção;
- falha ao registrar decisão.

Quando não houver base legítima para continuar, o processamento deve permanecer bloqueado.

## 19. Linguagem

A linguagem deve:

- dizer claramente o que será usado e para quê;
- evitar “aceitar tudo” como padrão;
- evitar urgência;
- evitar culpa;
- evitar promessa de compreensão completa;
- distinguir autorização de autenticação;
- distinguir revisão de autorização;
- distinguir autorização de persistência/personalização;
- explicar consequências de recusa ou remoção.

## 20. Acessibilidade

A futura solução deve considerar:

- operação por teclado;
- foco visível;
- associação clara entre item, finalidade e controle;
- estado selecionado não dependente apenas de cor;
- mensagens de erro e ação necessária acessíveis;
- confirmação destrutiva compreensível;
- suporte a zoom e responsividade;
- linguagem compatível com leitura clara.

## 21. Conteúdo sintético para Design

Design pode simular:

- inventário fictício;
- itens de naturezas diferentes;
- transcrição sintética;
- item derivado fictício;
- item removido ou limitado;
- seleção parcial;
- recusa;
- ação necessária;
- handoff simulado para `PER-006`.

Não pode apresentar como real:

- autorização real;
- processamento real;
- persistência real;
- dado pessoal real;
- conexão real de fonte externa;
- extração real;
- exclusão técnica real.

## 22. Liberdade de Design

A designer pode decidir:

- quantidade de frames;
- composição;
- componentes;
- agrupamento visual;
- hierarquia;
- tipografia;
- paleta;
- iconografia;
- densidade;
- motion;
- microinterações;
- responsividade;
- forma visual de inventário, seleção, confirmação e recusa.

O GKR não define baseline visual obrigatório para `PER-005`.

## 23. Uso por IA

Quando IA for usada para explorar `PER-005`, o contexto mínimo deve incluir:

1. `GKR-UX-PERSON-JOURNEY-READ-FIRST-001`;
2. `GKR-UX-PERSON-JOURNEY-FLOW-001`;
3. este Documento Mestre;
4. Surface Registry e detalhamento da Pessoa;
5. Transition Registry;
6. `UXA-023`;
7. `UXA-035`;
8. `GKR-UX-PER004-MASTER-001` para a fronteira de entrada.

A IA não pode:

- pré-selecionar autorizações;
- transformar autenticação em consentimento;
- inventar finalidade;
- inventar persistência;
- antecipar personalização;
- promover `TRN-004` ou `TRN-005`;
- absorver Arquivo/Perguntas Opcionais por inferência;
- criar novo `PER-ID`;
- iniciar processamento;
- materializar `PER-006` como se estivesse definido por este Master.

## 24. Critérios de Aceite Funcional

Uma futura solução visual de `PER-005` é aceitável quando:

1. o inventário é compreensível;
2. natureza e proveniência permanecem distinguíveis;
3. revisão antecede processamento;
4. autorizações iniciam desmarcadas;
5. cada autorização possui finalidade compreensível;
6. somente itens conscientemente selecionados podem ser autorizados;
7. recusa não inicia processamento;
8. autenticação não equivale a autorização;
9. captura não equivale a autorização;
10. persistência e personalização permanecem bloqueadas;
11. remoção/limitação não é confundida com exclusão técnica;
12. itens alterados materialmente exigem nova revisão aplicável;
13. informação de terceiros não é tratada como automaticamente autorizada;
14. `TRN-004` permanece parcial;
15. `TRN-005` permanece parcial;
16. nenhuma nova superfície é criada;
17. Product Engineering permanece não liberado.

## 25. Limites

Este Documento Mestre não:

- cria tela final;
- cria Figma;
- cria protótipo;
- define texto jurídico final;
- conclui política de privacidade;
- define storage;
- define retenção;
- implementa exclusão;
- implementa autorização;
- define modelo de IA;
- executa processamento;
- cria compreensão inicial;
- libera persistência;
- libera personalização;
- fecha continuidade de Arquivo/Perguntas Opcionais;
- altera maturidade de `TRN-004` ou `TRN-005`;
- cria `PER-006`;
- inicia Product Engineering.

## 26. Estado Corrente

```text
PER-005 MASTER
→ CURRENT DESIGN DEFINITION

ENTRY
→ TRN-004 / PARTIAL

JOB
→ REVIEW + AUTHORIZE

INVENTORY
→ CONTENT + NATURE + PROVENANCE + PURPOSE

AUTHORIZATION
→ SPECIFIC
→ INITIALLY UNSELECTED
→ ONLY FOR REVIEWED ELIGIBLE ITEMS

CURRENT MATERIAL PURPOSE
→ PREPARE TEMPORARY / REVIEWABLE INITIAL UNDERSTANDING

REFUSAL
→ LEGITIMATE
→ NO PROCESSING

PERSISTENCE
→ BLOCKED

PERSONALIZATION
→ BLOCKED

TRN-005
→ PARTIAL / UNCHANGED

NEXT DOCUMENTATION TARGET
→ PER-006 — PROCESSAMENTO VISÍVEL

NEW VISUAL MATERIALIZATION
→ NONE

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS DOCUMENT
```
