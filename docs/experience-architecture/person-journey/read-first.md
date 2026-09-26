---
id: GKR-UX-PERSON-JOURNEY-READ-FIRST-001
title: Jornada da Pessoa — Leia Primeiro para Design e IA
status: active
version: 0.1.14
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-25
normative: false
maturity: current_design_routing
depends_on:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-UX-PERSON-JOURNEY-FLOW-001
  - GKR-UX-HOME-MASTER-001
---

# Jornada da Pessoa — Leia Primeiro para Design e IA

## 1. Função

Este documento é a porta de entrada para a documentação de Design da **Jornada da Pessoa após a Home pública**.

Ele não cria telas, layout, wireframe, UI, protótipo, sistema visual ou implementação. Sua função é orientar designer humana, IA opcional, Produto, UX, Research, Legal/Privacidade e Engenharia sobre **quais responsabilidades funcionais precisam ser compreendidas antes de qualquer materialização visual**.

```text
HOME PÚBLICA — PESSOA
→ já possui Documento Mestre próprio
→ não é duplicada nesta coleção

JORNADA DA PESSOA
→ documentada por superfície / responsabilidade
→ uma construção por vez
→ sem antecipar forma visual

DESIGNER
→ AUTORA CRIATIVA DA FORMA

IA
→ OPCIONAL / CONTROLADA PELA DESIGNER

PRODUCT ENGINEERING
→ FORA DO ESCOPO DESTA COLEÇÃO
```

## 2. Fonte de verdade

Para cada superfície, a leitura deve partir de:

1. `GKR-JOURNEY-PERSON-001`;
2. `GKR-JOURNEY-SURFACE-REGISTRY-001`;
3. `GKR-JOURNEY-SURFACE-DETAIL-PERSON-001`;
4. `GKR-JOURNEY-TRANSITION-REGISTRY-001`;
5. autoridades funcionais específicas citadas pelo Registry;
6. o Documento Mestre da superfície, quando já construído nesta coleção.

A Home pública continua governada por `GKR-UX-HOME-MASTER-001`.

## 3. Regra de granularidade

Um documento desta coleção corresponde a **uma superfície ou responsabilidade funcional já reconhecida pelo Registry**.

```text
ESTADO INTERNO
≠ NOVA TELA POR INFERÊNCIA
≠ NOVO PER-ID

VARIANTE
≠ NOVA SUPERFÍCIE

MODAL
≠ NOVA SUPERFÍCIE AUTOMATICAMENTE

HANDOFF
≠ NOVA TELA AUTOMATICAMENTE
```

Exemplo: a revisão consciente antes da saída externa permanece um **estado de `PER-203`**, porque a autoridade corrente não cria um novo `PER-ID`.

## 4. O que cada Documento Mestre deve definir

Cada superfície deve ser descrita, quando aplicável, por:

- finalidade;
- papel na Journey;
- origem e destinos legítimos;
- job da Pessoa;
- informações que podem ser exibidas;
- informações que podem ser solicitadas ou capturadas;
- finalidades e autorizações;
- estados internos;
- ações e controles;
- retornos, pausa, recusa e interrupção;
- processamento e feedback visível;
- erros, vazio, indisponibilidade e recuperação;
- permissões e privacidade;
- dados reais necessários;
- conteúdo sintético permitido para prototipação;
- handoffs e efeitos;
- regras de acessibilidade;
- guardrails de linguagem e claims;
- liberdade criativa de Design;
- limites para IA;
- critérios de aceite funcional;
- lacunas que não podem ser preenchidas por inferência.

## 5. Liberdade criativa

O GKR governa significado, responsabilidade, dados, estados, relações, autoridade, limites, evidência e claims sustentáveis.

A designer pode definir:

- tipografia;
- paleta;
- imagens;
- ilustração;
- iconografia;
- grid;
- composição;
- componentes;
- densidade;
- ritmo;
- motion;
- microinterações;
- direção visual;
- linguagem gráfica;
- hierarquia visual;
- responsividade;
- soluções de acessibilidade visual;
- copy não congelada, desde que permaneça semanticamente compatível.

Nenhum Documento Mestre desta coleção deve prescrever estética.

## 6. IA opcional

Quando IA for utilizada, ela deve consumir apenas:

- este Leia Primeiro;
- o mapa corrente do fluxo;
- o Documento Mestre da superfície em construção;
- suas autoridades específicas;
- autoridades comuns estritamente necessárias.

A IA não pode:

- criar nova responsabilidade funcional;
- inventar dado real;
- criar autorização inexistente;
- promover hipótese a regra canônica;
- inferir navegação direta ausente do Transition Registry;
- transformar estado interno em nova tela;
- substituir decisão humana de Design.

## 7. Prototipação e referências existentes

Uma referência visual ou protótipo existente pode ser consultado **somente dentro do limite em que sua autoridade corrente o permite**.

```text
REFERÊNCIA VISUAL LOCAL
≠ BASELINE VISUAL GLOBAL

PROTÓTIPO
≠ PRODUTO IMPLEMENTADO

VALIDAÇÃO DE PROTÓTIPO
≠ AUTORIZAÇÃO DE PRODUCT ENGINEERING
```

## 8. Ordem de construção

A sequência de documentação está definida em `GKR-UX-PERSON-JOURNEY-FLOW-001`.

A regra operacional é:

```text
1 SUPERFÍCIE
→ DOCUMENTAR
→ VALIDAR
→ INCORPORAR AO GKR
→ SÓ ENTÃO AVANÇAR PARA A PRÓXIMA
```

## 9. Estado

```text
PERSON JOURNEY DESIGN DOCUMENTATION
→ FOUNDATION ACTIVE

FLOW MAP
→ DEFINED

SURFACE MASTERS
→ BUILT INCREMENTALLY

CURRENT SURFACE MASTERS
→ PER-002 — ENTRADA PROTEGIDA
→ PER-003 — ESCOLHA DE MODALIDADE
→ PER-004 — EXPRESSÃO POR TEXTO OU VOZ
→ PER-005 — INVENTÁRIO E AUTORIZAÇÃO
→ PER-006 — PROCESSAMENTO VISÍVEL
→ PER-007 — COMPREENSÃO INICIAL REVISÁVEL
→ PER-008 — HOJE
→ PER-010 — MEUS OBJETIVOS
→ PER-011 — MEUS PRÓXIMOS PASSOS
→ PER-012 — MINHA EVOLUÇÃO
→ PER-201 — MAPA DE OPORTUNIDADES
→ PER-202 — LISTA DE OPORTUNIDADES
→ PER-203 — DETALHE DE OPORTUNIDADE
→ PER-101 — EXPLORAR COLETIVOS
→ PER-102 — RESULTADOS DE BUSCA DE COLETIVOS

NEXT DOCUMENTATION TARGET
→ PER-103 — PERFIL PÚBLICO DO COLETIVO
→ NOT_STARTED

VISUAL MATERIALIZATION
→ DESIGN-OWNED

PRODUCT ENGINEERING
→ NOT RELEASED BY THIS COLLECTION
```
