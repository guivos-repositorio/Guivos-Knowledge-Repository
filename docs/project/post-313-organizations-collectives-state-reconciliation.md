---
id: GKR-ORGCOL-POST313-RECON-001
title: Reconciliação Transversal Pós-313 — Organizações e Coletivos
status: active
version: 1.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-30
normative: true
related:
  - GKR-STATE-001
  - GKR-UX-ORGCOL-STATE-001
  - GKR-UX-ORGCOL-UX-STATE-001
  - GKR-UX-ORGCOL-AUTH-JOBS-001
  - GKR-UX-ORGCOL-AUTH-IA-001
  - UXA-014
  - UXA-019
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-COLLECTIVE-001
---

# Reconciliação Transversal Pós-313 — Organizações e Coletivos

## 1. Finalidade

Este registro preserva a reconciliação transversal aberta após a PR #313, que corrigiu o estado de Organizações e Coletivos e estabeleceu que os antigos `UXA-015..018` não constituem autoridade vigente dos wireframes principais autenticados.

Sua função atual é dupla:

1. preservar a regra normativa de supersessão dos artefatos históricos `UXA-015..018` e impedir regressão de maturidade;
2. reconciliar essa correção histórica com as autoridades posteriores já integradas de atores, autoridades, jobs e Arquitetura da Informação autenticada.

Este documento não deve congelar o corpus no snapshot imediatamente posterior à PR #313. Autoridades posteriores válidas precisam ser reconhecidas diretamente.

## 2. Regra de precedência

No escopo de Organizações e Coletivos, a leitura vigente é:

```text
GKR-STATE-001 — verdade transversal atual
+
UXA-014 — fundamentos funcionais
+
UXA-019 — relações Organização ↔ Coletivo
+
GKR-UX-ORGCOL-STATE-001 — visão geral e estado temático atual
+
GKR-UX-ORGCOL-UX-STATE-001 — estado de UX e wireframes
+
GKR-UX-ORGCOL-AUTH-JOBS-001 — atores, autoridades e jobs autenticados
+
GKR-UX-ORGCOL-AUTH-IA-001 — Arquitetura da Informação autenticada
↓
este registro, no limite da supersessão pós-313 e da prevenção de regressão
↓
catálogos, matrizes, jornadas e snapshots derivados
```

Este registro não substitui as autoridades temáticas posteriores. Sua precedência permanece restrita ao conflito histórico que corrigiu: materialização/validação indevidamente atribuída a `UXA-015..018`.

## 3. Estado vigente da experiência autenticada

O estado obrigatório em 2026-08-30 é:

```text
ATORES / AUTORIDADES / JOBS AUTENTICADOS
→ DEFINIDOS DOCUMENTALMENTE
→ GKR-UX-ORGCOL-AUTH-JOBS-001

ARQUITETURA DA INFORMAÇÃO AUTENTICADA
→ DEFINIDA
→ MATURIDADE: authenticated_information_architecture_defined_pre_surface_map
→ GKR-UX-ORGCOL-AUTH-IA-001

MAPA FINAL DE SUPERFÍCIES E ESTADOS
→ NÃO DEFINIDO COMO AUTORIDADE VIGENTE

WIREFRAME PRINCIPAL DA ORGANIZAÇÃO
→ NÃO DEFINIDO

WIREFRAME PRINCIPAL DO COLETIVO
→ NÃO DEFINIDO

VALIDAÇÃO DE WIREFRAME PRINCIPAL
→ NÃO REALIZADA EM OBJETO VIGENTE

UI / PROTÓTIPO / TESTES / HANDOFF TÉCNICO
→ NÃO DEFINIDOS / NÃO AUTORIZADOS POR ESTA RECONCILIAÇÃO
```

A existência de IA não equivale a sitemap final, menu visual, mapa de superfícies, wireframe, UI, RBAC técnico ou implementação.

```text
ARQUITETURA DA INFORMAÇÃO DEFINIDA
≠ EXPERIÊNCIA VISUAL PRINCIPAL DEFINIDA
```

## 4. Registros históricos superseded

A PR #313 estabeleceu:

```text
UXA-015 → superseded
UXA-016 → superseded
UXA-017 → superseded
UXA-018 → superseded
```

Os SVGs associados a `UXA-015` e `UXA-016` permanecem fisicamente no repositório por rastreabilidade histórica enquanto a auditoria integral decide seu destino final.

Eles não constituem:

- wireframe oficial vigente;
- baseline de produto;
- especificação de UI;
- referência aprovada para Engenharia;
- evidência atual de validação funcional;
- autorização para inferir mapa final de superfícies ou navegação.

A auditoria integral preserva a regra adicional:

> **Nenhum artefato histórico será removido sem prova de absorção de todo conteúdo material ainda válido e sem autorização humana separada e explícita; se autorizado, o cleanup físico e a reconciliação das referências ocorrerão na mesma transação.**

## 5. Conteúdo material histórico e absorção atual

A auditoria do Bloco H recuperou o conteúdo pré-supersessão de `UXA-015..018` pelo diff da PR #313.

Os princípios funcionais centrais permanecem representados nas autoridades atuais, incluindo:

### Organização

- contexto, unidade, papel e autoridade;
- responsabilidade material atual;
- capacidade e condições para cumprir compromissos;
- oportunidades e programas subordinados à responsabilidade institucional;
- relações e bilateralidade;
- evidência, limitações e prestação de contas;
- correção, contestação, pausa e encerramento;
- Próximos Passos justificáveis;
- neutralidade diante de métricas comerciais isoladas.

### Coletivo

- propósito compartilhado;
- pertencimento e participação voluntária;
- separação entre pertencimento, disponibilidade, responsabilidade e autoridade;
- atividades subordinadas ao propósito;
- papéis aceitos legitimamente;
- governança, moderação, proteção e contestação;
- recursos e relações sem perda de autonomia;
- avanço/aprendizado sustentado por evidência;
- pausa, recusa e saída legítimas;
- Próximos Passos compatíveis com a governança.

Esses elementos aparecem de forma distribuída em `UXA-014`, `UXA-019`, `GKR-UX-ORGCOL-AUTH-JOBS-001` e `GKR-UX-ORGCOL-AUTH-IA-001`.

Entretanto, hierarquias específicas de tela, listas históricas de estados, linguagem de interface e conclusões de validação de `UXA-015..018` **não são promovidas automaticamente a decisões atuais**. A remoção física desses artefatos continua condicionada a autorização humana separada e explícita. `F-006` permanece aberto durante autorização, cleanup, reconciliação, recomputação, validações e novo review; seu fechamento somente poderá ser decidido depois desses gates.

## 6. Efeito sobre o Registro do Estado Atual

O `GKR-STATE-001` anterior à PR #313 registrava, entre outros snapshots:

```text
SVGs → 121 — 121 validados / 0 pendentes
```

Essa formulação não é válida como claim global de maturidade visual.

A verdade vigente separa:

```text
INVENTÁRIO FÍSICO
≠ AUTORIDADE VISUAL VIGENTE
≠ MATURIDADE VALIDADA
```

O `GKR-STATE-001` atual já reconhece Jobs + IA autenticada e não utiliza `121/121 validados` como estado visual vigente.

## 7. Efeito sobre Catálogo, Galeria e Matriz de Rastreabilidade

Os instrumentos ativos foram normalizados para separar inventário físico de maturidade:

- `GKR-JOURNEY-SCREEN-CATALOG-001` registra 121 SVGs como inventário físico e trata a claim antiga como superseded;
- `GKR-JOURNEY-SCREEN-GALLERY-001` registra 121 SVGs físicos para inspeção, sem convertê-los em 121 wireframes vigentes;
- `GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001` registra 121 associações físicas e 34 perfis, com associação ≠ autoridade visual vigente;
- `GKR-JOURNEY-SURFACE-REGISTRY-001` mantém IDs estáveis e maturidade por objeto.

Para Organização e Coletivo:

- `ORG-001` mantém responsabilidade semântica, mas o antigo `UXA-015/017` não é baseline vigente;
- `COL-001` mantém rastreabilidade, mas `UXA-016/018` não define a experiência autenticada final;
- fluxos especializados posteriores preservam apenas sua maturidade própria.

O total físico pode permanecer 121 enquanto os dois SVGs históricos estiverem no corpus. Nenhuma contagem agregada de wireframes vigentes/validados é inferida sem recomputação governada.

## 8. Efeito sobre o Registro Granular de Superfícies

Um identificador estável pode sobreviver à supersessão de uma materialização.

```text
ID DA SUPERFÍCIE CONTINUA EXISTINDO
≠ WIREFRAME ANTERIOR CONTINUA VIGENTE
```

`GKR-SURF-ORG-001` continua representando uma responsabilidade institucional conhecida, agora apoiada por fundamento, Jobs e IA atuais, sem wireframe principal vigente.

Para Coletivo, IDs e fluxos especializados preservam seus contratos próprios, mas não podem ser usados para inferir a composição final da experiência principal autenticada.

## 9. Efeito sobre a Jornada Integrada da Organização

A versão anterior à reconciliação apresentava:

```text
Visão Geral da Organização
→ validado
→ referência UXA-015
→ validação UXA-017
```

Esse estado foi supersedido.

A leitura atual é:

```text
FUNDAÇÃO / JOBS / IA
→ DEFINIDOS DOCUMENTALMENTE

VISÃO GERAL COMO DOMÍNIO DE IA
→ DEFINIDA SEMANTICAMENTE

MAPA DE SUPERFÍCIES / COMPOSIÇÃO FINAL
→ PENDENTE

WIREFRAME PRINCIPAL
→ PENDENTE

VALIDAÇÃO DO WIREFRAME PRINCIPAL
→ PENDENTE

JORNADA GERAL
→ DRAFT
```

Fluxos independentes como cadastro de oportunidades, descoberta, Opportunity Boost e Planos mantêm autoridade própria no escopo em que não dependam da materialização superseded.

## 10. Efeito sobre a Jornada Integrada do Coletivo

A versão anterior utilizava `UXA-016/018` como parte da evidência de presença inicial.

A leitura vigente é:

- `UXA-016/018` não sustentam maturidade visual vigente;
- fundamentos, Jobs e IA do Coletivo estão definidos documentalmente;
- superfícies públicas sustentadas por referências independentes preservam maturidade própria;
- superfícies administrativas especializadas posteriores preservam validação local quando houver autoridade específica;
- nenhuma delas equivale à definição do mapa final de superfícies ou do wireframe principal autenticado;
- a Jornada do Coletivo continua `draft`.

## 11. Wireframe principal ≠ fluxo especializado

A distinção permanece obrigatória:

```text
WIREFRAME PRINCIPAL DA EXPERIÊNCIA AUTENTICADA
≠ WIREFRAME LOCAL DE CAPACIDADE ESPECÍFICA
```

É possível existir materialização local de:

- cadastro de oportunidade;
- gestão de solicitações;
- Planos;
- revisão de contratação;
- estados de pedido;
- perfil público;
- descoberta;

sem que exista o wireframe principal autenticado final.

Da mesma forma:

```text
ARQUITETURA DA INFORMAÇÃO
≠ MAPA FINAL DE SUPERFÍCIES
≠ WIREFRAME
```

## 12. Estado das transições especializadas

Transições documentadas em pacotes especializados mantêm sua evidência local, mas não podem ser usadas para afirmar que a composição final da experiência autenticada está fechada.

Em especial:

- origem/retorno de Planos da Organização preserva o contrato especializado, mas deve ser confrontada com o futuro mapa/wireframe principal quando materializado;
- navegação administrativa local do Coletivo permanece evidência dos pacotes específicos, sem determinar a arquitetura visual final;
- nenhuma transição especializada autoriza inferir menu global, dashboard, Home autenticada visual ou implementação completa.

## 13. Estado de maturidade consolidado

| Dimensão | Organização | Coletivo |
|---|---|---|
| fundamento funcional | existente | existente |
| relação entre participantes | existente em conjunto | existente em conjunto |
| atores, autoridades e jobs | **definidos** | **definidos** |
| Arquitetura da Informação autenticada | **definida pré-surface-map** | **definida pré-surface-map** |
| Research de supply / valor | existente | existente |
| jornada integrada | draft | draft |
| fluxos especializados | parciais / alguns validados localmente | parciais / vários validados localmente |
| mapa final de superfícies | **pendente** | **pendente** |
| wireframe principal | **pendente** | **pendente** |
| validação do wireframe principal | **pendente** | **pendente** |
| UI final | pendente | pendente |
| protótipo | pendente | pendente |
| testes de usabilidade | pendente | pendente |
| handoff técnico da experiência principal | pendente | pendente |

## 14. Estado da normalização direta dos derivados

A dívida mecânica registrada originalmente após #313 foi substancialmente absorvida pelos instrumentos atuais.

| Derivado | Estado em 2026-08-30 |
|---|---|
| `GKR-STATE-001` | normalizado; Jobs + IA reconhecidos |
| `GKR-JOURNEY-SCREEN-CATALOG-001` | normalizado quanto à separação físico × maturidade |
| `GKR-JOURNEY-SCREEN-GALLERY-001` | normalizado quanto à separação físico × maturidade |
| `GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001` | normalizado; associação ≠ autoridade |
| `GKR-JOURNEY-SURFACE-REGISTRY-001` | maturidade principal O/C não é inferida dos artefatos superseded |
| Jornada da Organização | normalizada no Bloco H; Jobs + IA atuais reconhecidos; surface map/wireframe principal permanecem pendentes |
| Jornada do Coletivo | normalizada no Bloco H; Jobs + IA atuais reconhecidos; surface map/wireframe principal permanecem pendentes |
| porta temática O/C | reconciliada com Jobs + IA no Bloco H |

Esta tabela não encerra `F-006`. Os testes de absorção, referências e função atual estão concluídos, as dependências funcionais ativas foram reconciliadas e a elegibilidade documental de cleanup está comprovada. A permanência física de `UXA-015..018` e dos SVGs associados continua obrigatória enquanto não houver autorização humana separada; se o cleanup for autorizado, remoção, reconciliação dos instrumentos afetados, recomputação, validações e novo review devem ocorrer antes de qualquer decisão de fechamento.

## 15. Regra para contagens visuais

Toda métrica visual deve responder separadamente:

1. quantos arquivos/artefatos físicos existem;
2. quantos artefatos possuem autoridade vigente na maturidade declarada.

Nunca utilizar:

```text
QUANTIDADE DE SVGs FÍSICOS
=
QUANTIDADE DE WIREFRAMES VIGENTES E VALIDADOS
```

Estado comprovado do inventário no Bloco I:

- SVGs físicos: **121**;
- associações físicas: **121**;
- perfis de rastreabilidade: **34**;
- duplicatas exatas por blob SHA: **0 observadas/provadas no snapshot auditado**;
- near-duplicates: **não certificados**;
- total agregado de wireframes vigentes/validados: **não certificado**.

## 16. Gate de remoção dos históricos

`UXA-015..018` e os dois SVGs associados não serão removidos por conveniência de contagem.

Os gates documentais de classificação do conteúdo material e de ausência de dependência funcional atual estão concluídos. A sequência governada restante é:

1. obter autorização humana separada e explícita para o cleanup físico;
2. se autorizado, remover os quatro documentos `UXA-015..018` e os dois SVGs associados e, na mesma transação, reconciliar links, metadados, catálogo, gallery, registry e traceability afetados;
3. recomputar catálogo, galeria, matriz, associações e contagens físicas sobre a árvore resultante;
4. validar semanticamente e mecanicamente o novo head exato;
5. executar nova revisão repo-wide no novo head;
6. somente depois desses gates decidir o fechamento de `F-006` e o fechamento formal de H/I.

## 17. Próximo gate válido

No limite atual da frente O/C:

```text
FOUNDATIONS / RELATIONS
→ DEFINED

ACTORS / AUTHORITIES / JOBS
→ DEFINED

AUTHENTICATED INFORMATION ARCHITECTURE
→ DEFINED PRE-SURFACE-MAP

FINAL SURFACE MAP
→ NOT DEFINED / HOLD DURING CURRENT AUDIT DECISION

MAIN AUTHENTICATED WIREFRAMES
→ NOT DEFINED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED
```

A branch pré-auditoria `agent/gkr-orgcol-authenticated-surface-map-v1` permanece `HOLD_REVIEW` e não é autoridade.

## 18. Regra final

> **Arquivo físico não é autoridade vigente. Materialização histórica não é wireframe aprovado. Validação antiga não sobrevive à supersessão do objeto que validava. Arquitetura da Informação atual não reativa o wireframe histórico.**

A experiência principal de Organizações e Coletivos somente poderá voltar a ser declarada visualmente materializada/validada quando novos objetos forem definidos, revisados e validados a partir das autoridades atuais e dos gates vigentes.