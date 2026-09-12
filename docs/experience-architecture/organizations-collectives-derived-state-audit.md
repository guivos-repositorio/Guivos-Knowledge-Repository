---
id: GKR-UX-ORGCOL-DERIVED-AUDIT-001
title: Organizações e Coletivos — Auditoria de Derivados Pós-313
status: active
version: 1.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-09-05
normative: false
related:
  - GKR-ORGCOL-POST313-RECON-001
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
---

# Organizações e Coletivos — Auditoria de Derivados Pós-313

## 1. Objetivo

Esta auditoria registra a deriva transversal identificada após a PR #313 e acompanha sua normalização direta nas autoridades derivadas.

Ela não cria nova arquitetura funcional, não define wireframes e não altera a maturidade de artefatos independentes que possuam autoridade própria.

A versão 1.1.0 também reconcilia o registro com as autoridades posteriores já integradas:

- `GKR-UX-ORGCOL-AUTH-JOBS-001` — atores, autoridades e jobs autenticados;
- `GKR-UX-ORGCOL-AUTH-IA-001` — Arquitetura da Informação autenticada definida pré-surface-map.

## 2. Resultado executivo

```text
UXA-015..018
→ REMOVIDOS DO CORPUS CORRENTE POR F-006
→ PROVENIÊNCIA PRESERVADA NO HISTÓRICO GIT

JOBS AUTENTICADOS O/C
→ DEFINIDOS

ARQUITETURA DA INFORMAÇÃO AUTENTICADA O/C
→ DEFINIDA PRÉ-SURFACE-MAP

MAPA FINAL DE SUPERFÍCIES
→ PENDENTE

WIREFRAMES PRINCIPAIS AUTENTICADOS
→ PENDENTES / AUTORIDADE DE DESIGN

F-016-A
→ RESOLVED
→ PHYSICAL SVG COUNT = 0
```

## 3. Matriz de divergências e estado atual

| Derivado | Snapshot anterior | Estado correto atual | Situação da normalização |
|---|---|---|---|
| `GKR-STATE-001` | `121 SVGs — 121 validados / 0 pendentes` | camada física removida; maturidade não inferida | normalizado |
| `GKR-JOURNEY-SCREEN-CATALOG-001` | inventário físico 121/119 em checkpoints anteriores | **0 SVGs físicos após F-016-A** | normalizado |
| antiga galeria visual integrada | leitura agregada de validação | removida do corpus corrente; proveniência no histórico Git | normalizado |
| antiga matriz visual | associação visual podia ser lida como vigência | removida do corpus corrente; perfis históricos recuperáveis no Git | normalizado |
| `GKR-JOURNEY-SURFACE-REGISTRY-001` — `ORG-001` | Visão Geral validada por `UXA-015/017` | responsabilidade conhecida; materialização histórica removida; Design governa futura materialização | normalizado |
| registro do Coletivo | `UXA-016/018` como evidência da UX principal | não utilizar esses IDs para afirmar wireframe principal vigente | normalizado |
| Jornada da Organização | Visão Geral = validada | Jobs + IA existem; mapa funcional ainda não canônico; materialização pertence a Design | normalizado |
| Jornada do Coletivo | `UXA-016/018` como evidência principal | Jobs + IA existem; mapa funcional ainda não canônico; materialização pertence a Design | normalizado |

## 3A. Snapshot histórico pós-F-006 / pré-F-016-A

| Derivado | Snapshot anterior | Estado registrado naquele checkpoint | Situação naquele checkpoint |
|---|---|---|---|
| `GKR-STATE-001` | `121 SVGs — 121 validados / 0 pendentes` | inventário físico ≠ maturidade; Jobs + IA O/C reconhecidos | normalizado |
| `GKR-JOURNEY-SCREEN-CATALOG-001` | total canônico `121 / 121 validados` | **119 físicos pós-F-006**; maturidade por item; claim antiga superseded | normalizado |
| `GKR-JOURNEY-SCREEN-GALLERY-001` | leitura agregada de validação | **119 SVGs físicos pós-F-006**; inventário ≠ autoridade visual | normalizado |
| `GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001` | associação visual podia ser lida como vigência | **119 associações / 34 perfis estáveis**; associação ≠ autoridade visual | normalizado |
| `GKR-JOURNEY-SURFACE-REGISTRY-001` — `ORG-001` | Visão Geral validada por `UXA-015/017` | responsabilidade conhecida; materialização histórica superseded; wireframe atual pendente | normalizado no limite de maturidade |
| registro do Coletivo | `UXA-016/018` como evidência da UX principal | não utilizar esses IDs para afirmar wireframe principal vigente | normalizado no limite de maturidade |
| Jornada da Organização | Visão Geral = validada | Jobs + IA atuais existem; mapa/wireframe principal pendentes | estado visual corrigido; propagação explícita da IA ainda auditada no Bloco H |
| Jornada do Coletivo | `UXA-016/018` como evidência principal | Jobs + IA atuais existem; mapa/wireframe principal pendentes | estado visual corrigido; propagação explícita da IA ainda auditada no Bloco H |
| `GKR-UX-ORGCOL-STATE-001` | sequência ainda tratava Jobs/IA como futuros | Jobs + IA definidos; próximo nível é surface map | normalizado no Bloco H |
| `GKR-ORGCOL-POST313-RECON-001` | IA ainda constava como pendente | IA definida pré-surface-map; precedência restrita à supersessão histórica | normalizado no Bloco H |

## 4. Elementos que permanecem válidos

A correção não invalida automaticamente materiais independentes e posteriores.

Permanecem no estado próprio, conforme suas autoridades específicas:

- cadastro de oportunidade pela Organização;
- publicação e descoberta de oportunidades;
- Mapa, Lista e Detalhe de Oportunidades;
- gestão de solicitações de Coletivos;
- superfícies públicas de descoberta/perfil que não dependam de `UXA-016/018`;
- Planos e fluxos comerciais com autoridade própria;
- Opportunity Boost;
- Home pública de Organizações e Coletivos;
- fundamentos de `UXA-014`;
- relações de `UXA-019`;
- atores, autoridades e jobs de `GKR-UX-ORGCOL-AUTH-JOBS-001`;
- Arquitetura da Informação de `GKR-UX-ORGCOL-AUTH-IA-001`;
- Research `RP-002`.

Validação local de um fluxo especializado não fecha a experiência principal do participante.

## 5. Organização — estado corrigido

A Organização possui fundamentos, atores, autoridades, jobs e Arquitetura da Informação já documentados.

```text
Fundamento institucional
→ existente

Atores / autoridades / jobs
→ definidos

Arquitetura da Informação
→ definida pré-surface-map

Cadastro / publicação de oportunidades
→ possui materializações próprias

Planos
→ possui materializações próprias

Relação com Coletivos
→ contrato existente; materialização bilateral incompleta

Visão Geral
→ domínio de IA definido semanticamente
→ mapa/composição final pendentes
→ wireframe principal autenticado pendente

Mapa final de superfícies
→ pendente
```

O antigo SVG `antigo ativo visual F-006 de ORG-001` é histórico `superseded` e permanece fisicamente enquanto não houver autorização humana separada e explícita para seu cleanup; `F-006` permanece aberto durante eventual remoção e os gates pós-cleanup.

## 6. Coletivo — estado corrigido

O Coletivo possui fundamentos, atores, autoridades, jobs, Arquitetura da Informação, fluxos públicos e capacidades administrativas especializadas em diferentes níveis de maturidade.

```text
Fundamento coletivo
→ existente

Atores / autoridades / jobs
→ definidos

Arquitetura da Informação
→ definida pré-surface-map

Descoberta e perfil público
→ possuem evidências independentes em seus pacotes

Solicitação / gestão de solicitações
→ possuem materializações especializadas

Planos
→ possuem materializações especializadas

Relações institucionais
→ contrato existente; materialização incompleta

Início
→ domínio de IA definido semanticamente
→ mapa/composição final pendentes
→ wireframe principal autenticado pendente

Mapa final de superfícies
→ pendente
```

O antigo SVG `antigo ativo visual F-006 de COL-001` é histórico `superseded` e não pode ser usado como baseline da experiência autenticada final.

## 7. Regra para contagens visuais

Toda métrica visual deve responder duas perguntas separadas:

1. quantos arquivos/artefatos físicos existem?
2. quantos artefatos possuem autoridade vigente na maturidade declarada?

Nunca utilizar:

```text
QUANTIDADE DE SVGs FÍSICOS
=
QUANTIDADE DE WIREFRAMES VIGENTES E VALIDADOS
```

Estado comprovado no Bloco I:

| Indicador | Estado |
|---|---:|
| SVGs físicos | **121** |
| associações físicas | **121** |
| perfis de rastreabilidade | **34** |
| duplicatas exatas por blob SHA | **0** |
| near-duplicates | **NOT_CERTIFIED** |
| total agregado de wireframes vigentes | **NOT_CERTIFIED** |
| total agregado de wireframes validados vigentes | **NOT_CERTIFIED** |
| total agregado de pendências visuais | **NOT_CERTIFIED** |

Categorias semânticas mínimas continuam:

- vigente validado;
- vigente materializado / local;
- pendente;
- histórico superseded.

## 8. Regra para registros granulares

Um identificador de superfície pode continuar estável mesmo quando sua materialização é supersedida.

Portanto:

```text
ID DA SUPERFÍCIE CONTINUA EXISTINDO
≠
WIREFRAME ANTERIOR CONTINUA VIGENTE
```

Isso preserva rastreabilidade sem carregar maturidade indevida.

## 9. Regra para Jornadas Integradas

Jornadas `draft` podem conter responsabilidades e relações conhecidas sem possuir wireframe final.

A leitura atual deve distinguir:

- `definido semanticamente` para domínios e responsabilidades sustentados por Jobs/IA;
- `contratado` para responsabilidades/ligação sem validação funcional visual suficiente;
- `materializado` somente quando houver referência vigente;
- `validado` somente quando o objeto vigente tiver sido efetivamente validado;
- `local` para validação limitada a pacote especializado;
- `superseded` para referências históricas sem autoridade atual.

A existência da IA atual não permite reativar a conclusão visual de `UXA-015..018`.

## 10. Conteúdo material de UXA-015..018

O Bloco H recuperou pelo diff da PR #313 o conteúdo anterior à supersessão.

### Semântica funcional absorvida nas autoridades atuais

Foi comprovada absorção substancial de:

- contexto e autoridade;
- responsabilidade material;
- capacidade vinculada a compromissos;
- oportunidades/atividades subordinadas ao propósito/responsabilidade;
- bilateralidade e autonomia;
- evidência e limites de contribuição;
- pertencimento e participação voluntária;
- papéis e governança;
- proteção, contestação, pausa e saída;
- Próximos Passos justificados;
- neutralidade frente a métricas de popularidade/comercialização.

### Conteúdo que não deve ser promovido automaticamente

Permanece histórico, salvo decisão futura própria:

- hierarquias específicas da antiga composição de tela;
- blocos e ordem visual da materialização superseded;
- linguagem de interface aprovada apenas naquele objeto histórico;
- conclusão histórica de validação funcional;
- estados alternativos detalhados quando ainda não absorvidos como requisito vigente por autoridade posterior.

Consequência:

> **F-006 está resolvido. F-016-A também está resolvido; futuras remoções Markdown dependem de classificação e autorização próprias.**

## 11. Gate para normalização e cleanup

Após o fechamento de F-006, qualquer derivado deve:

1. tratar `UXA-015..018` somente como proveniência histórica quando necessário;
2. reconhecer Jobs + IA atuais para a experiência autenticada;
3. separar inventário físico de maturidade visual;
4. não promover wireframe por inferência;
5. manter as Jornadas da Organização e do Coletivo em `draft`;
6. aplicar a fronteira `DOCUMENTAÇÃO ≠ DESIGN` aberta por F-016;
7. submeter qualquer cleanup físico posterior a autorização humana separada e validações no head exato.

Para `F-016-A`, o cleanup 119/119 foi aplicado e validado; a contagem física corrente é zero e a subfrente está `RESOLVED`.

## 12. Autoridade de interpretação

Para divergências de supersessão pós-313, consultar o registro normativo `GKR-ORGCOL-POST313-RECON-001`.

Para o estado atual mais amplo, prevalecem `GKR-STATE-001`, `GKR-UX-ORGCOL-STATE-001`, `GKR-UX-ORGCOL-UX-STATE-001`, `GKR-UX-ORGCOL-AUTH-JOBS-001` e `GKR-UX-ORGCOL-AUTH-IA-001` em seus respectivos escopos.

## 13. Estado final desta auditoria derivada

```text
PR #313
→ VERDADE VISUAL TEMÁTICA CORRIGIDA

NORMALIZAÇÃO DOS DERIVADOS CENTRAIS
→ SUBSTANCIALMENTE CONCLUÍDA

JOBS + IA AUTENTICADA
→ DEFINIDOS E PROPAGADOS NAS JORNADAS DRAFT

MAPA FINAL DE SUPERFÍCIES
→ PENDENTE

WIREFRAMES PRINCIPAIS
→ PENDENTES / DESIGN AUTHORITY

F-006
→ RESOLVED
→ CLEANUP 6/6 APPLIED AND VALIDATED

F-007
→ RESOLVED NO LIMITE SEMÂNTICO/INVENTÁRIO DO BLOCO I

F-016
→ RESOLVED
→ DOCUMENTATION_DEMATERIALIZATION_COMPLETE
→ LEGACY_VISUAL_PRODUCERS_REMOVED_26_OF_26
→ POST_DELETE_PROOF_SUCCESS

F-016-A
→ PHYSICAL_CLEANUP_APPLIED_119_OF_119
→ PHYSICAL_SVG_COUNT_0
→ POST_DELETE_PROOF_V2_SUCCESS
→ RESOLVED
```

A existência de qualquer dívida documental residual não autoriza retornar a SVGs superseded como baseline nem transforma o inventário físico em autoridade de Design.
