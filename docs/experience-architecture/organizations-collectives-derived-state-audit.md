---
id: GKR-UX-ORGCOL-DERIVED-AUDIT-001
title: Organizações e Coletivos — Auditoria de Derivados Pós-313
status: active
version: 1.0.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-26
normative: false
related:
  - GKR-ORGCOL-POST313-RECON-001
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
---

# Organizações e Coletivos — Auditoria de Derivados Pós-313

## 1. Objetivo

Esta auditoria identifica quais registros derivados ainda carregam snapshots anteriores à reconciliação da PR #313 e define a leitura correta até que cada arquivo seja normalizado diretamente.

Ela não cria nova arquitetura funcional, não define wireframes e não altera a maturidade de artefatos independentes que possuam autoridade própria.

## 2. Resultado executivo

A auditoria encontrou uma deriva transversal: documentos anteriores utilizaram `UXA-015..018` como evidência de que as superfícies principais de Organização e Coletivo já estavam materializadas e validadas.

Após a PR #313, isso não é mais verdadeiro.

O problema aparece em quatro famílias de derivados:

1. registro global de estado;
2. catálogo visual agregado;
3. registro granular de superfícies;
4. jornadas integradas.

## 3. Matriz de divergências

| Derivado | Snapshot anterior | Estado correto pós-313 |
|---|---|---|
| `GKR-STATE-001` | `121 SVGs — 121 validados / 0 pendentes` | inventário físico histórico não equivale a maturidade; referências superseded devem ser excluídas da leitura vigente |
| `GKR-JOURNEY-SCREEN-CATALOG-001` | total canônico `121 / 121 validados` | total físico pode permanecer, mas maturidade deve separar vigente, local, pendente e superseded |
| `GKR-JOURNEY-SURFACE-REGISTRY-001` — `ORG-001` | Visão Geral da Organização = validada por `UXA-015/017` | superfície/responsabilidade conhecida; wireframe oficial e validação vigentes pendentes |
| detalhamento da Organização | `uxa-015-organization-overview-desktop.svg` = materialização vigente | SVG histórico superseded; não usar como baseline |
| registro do Coletivo | referências a `UXA-016/018` | não utilizar esses IDs para afirmar wireframe principal vigente |
| Jornada da Organização | Visão Geral = validada | principal autenticada ainda não definida em wireframe |
| Jornada do Coletivo | `UXA-016/018` como evidência de entrada/referência | remover essa dependência de maturidade; preservar somente evidências independentes |

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
- Research `RP-002`.

Validação local de um fluxo especializado não fecha a experiência principal do participante.

## 5. Organização — estado corrigido

A organização possui fundamentos e capacidades já documentadas, mas a superfície principal autenticada precisa ser reconstruída futuramente.

```text
Fundamento institucional
→ existente

Cadastro / publicação de oportunidades
→ possui materializações próprias

Planos
→ possui materializações próprias

Relação com Coletivos
→ contrato existente; materialização bilateral incompleta

Visão Geral / Home autenticada oficial
→ wireframe pendente

Arquitetura final de navegação
→ pendente
```

O antigo SVG `uxa-015-organization-overview-desktop.svg` é histórico.

## 6. Coletivo — estado corrigido

O Coletivo possui fundamentos, fluxos públicos e algumas capacidades administrativas materializadas em programas posteriores. Isso não significa que a experiência principal autenticada esteja fechada.

```text
Fundamento coletivo
→ existente

Descoberta e perfil público
→ possuem evidências independentes em seus pacotes

Solicitação / gestão de solicitações
→ possuem materializações especializadas

Planos
→ possuem materializações especializadas

Relações institucionais
→ contrato existente; materialização incompleta

Home / Início autenticado oficial
→ wireframe pendente

Arquitetura final de navegação
→ pendente
```

O antigo `UXA-016` não pode ser usado como baseline da Home autenticada final.

## 7. Regra para contagens visuais

A partir desta reconciliação, toda métrica visual deverá responder duas perguntas separadas:

1. quantos arquivos/artefatos físicos existem?
2. quantos artefatos possuem autoridade vigente na maturidade declarada?

Nunca mais utilizar:

```text
quantidade de SVGs físicos
=
quantidade de wireframes vigentes e validados
```

Categorias mínimas recomendadas:

- vigente validado;
- vigente materializado / local;
- pendente;
- histórico superseded.

## 8. Regra para registros granulares

Um identificador de superfície pode continuar estável mesmo quando sua materialização é supersedida.

Portanto:

```text
ID da superfície continua existindo
≠
wireframe anterior continua vigente
```

Isso permite preservar rastreabilidade sem carregar maturidade indevida.

## 9. Regra para Jornadas Integradas

Jornadas `draft` podem conter responsabilidades e relações conhecidas sem possuir wireframe final.

A futura normalização das Jornadas deverá utilizar:

- `contratado` para responsabilidades sustentadas por fundamentos;
- `materializado` somente quando houver referência vigente;
- `validado` somente quando o objeto vigente tiver sido efetivamente validado;
- `superseded` para referências históricas removidas da autoridade atual.

## 10. Gate para futura normalização direta

Ao atualizar cada derivado, a alteração deverá:

1. manter IDs estáveis;
2. preservar evidências independentes;
3. remover `UXA-015..018` como fonte de maturidade vigente;
4. não apagar o histórico físico;
5. separar contagem física de contagem de maturidade;
6. não promover wireframe pendente por inferência;
7. manter as Jornadas da Organização e do Coletivo em `draft`;
8. submeter o diff aos gates semântico e mecânico do GKR.

## 11. Autoridade de interpretação

Para divergências desta auditoria, consultar o registro normativo `GKR-ORGCOL-POST313-RECON-001`.

Este arquivo funciona como mapa operacional da dívida de sincronização derivada.

## 12. Estado final

```text
PR #313
→ verdade temática corrigida

DERIVADOS PRÉ-313
→ alguns snapshots ainda defasados

RECONCILIAÇÃO TRANSVERSAL
→ autoridade explícita criada

NORMALIZAÇÃO DIRETA DE CADA DERIVADO
→ etapa mecânica subsequente
```

A existência dessa dívida documental não autoriza retornar aos SVGs superseded como baseline. O estado vigente permanece: **wireframes principais autenticados de Organização e Coletivo ainda não definidos**.