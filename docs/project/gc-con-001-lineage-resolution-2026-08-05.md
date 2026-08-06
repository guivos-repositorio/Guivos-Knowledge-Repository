---
id: GKR-LINEAGE-GC-CON-001-001
title: Resolução de Linhagem da Família Externa GC-CON-001
status: draft
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-STATE-001
  - GKR-AUD-ACCUMULATED-003
  - GKR-SOURCE-INTAKE-001
  - GKR-CLAIMS-TRACE-001
related:
  - ADR-006
  - A2-METHOD-001
  - GEA-AUDIT-001
normative: false
---

# Resolução de Linhagem da Família Externa GC-CON-001

## 1. Finalidade

Este documento resolve preliminarmente a colisão de identidade e versão encontrada na família externa `GC-CON-001 — Anthropology of Guivos`.

A resolução trata proveniência, sequência editorial, maturidade e elegibilidade para intake. Ela não aprova o conteúdo antropológico, não cria uma edição canônica e não incorpora os PDFs externos ao Guivos Knowledge Repository.

## 2. Baseline da análise

A família foi identificada no acervo externo com múltiplos arquivos produzidos em 25/06/2026 e apresentados como estrutura, capítulos, manuscrito vivo, planejamento, blocos, partes expandidas, consolidações e Canon Edition.

Foram observados:

- diversos arquivos com o identificador `GC-CON-001`;
- múltiplas peças declaradas como versão `0.1`;
- uma sequência de manuscritos vivos entre `0.2` e `0.7`;
- vários documentos diferentes declarados simultaneamente como versão `1.0`;
- planos e decisões editoriais rotulados como se fossem versões do próprio corpus;
- capítulos, blocos e partes que reutilizam o ID do documento-pai;
- ausência, no acervo analisado, de um único artefato final capaz de representar sozinho toda a alegada versão `1.0`;
- ausência de integração governada dessa família na baseline da `main` pesquisada.

## 3. Não conformidade principal

### 3.1 Colisão de identificador

O mesmo identificador `GC-CON-001` foi utilizado para:

- estrutura editorial;
- capítulos isolados;
- manuscrito vivo;
- decisão de planejamento;
- manuscritos numerados;
- blocos de capítulo;
- partes expandidas;
- consolidação editorial;
- alegada Canon Edition.

Esses artefatos não são semanticamente equivalentes. A reutilização impede determinar, apenas pelo ID, qual conteúdo constitui o documento.

### 3.2 Colisão de versão

A versão `1.0` aparece em diversos artefatos distintos e parciais. Entre eles existem planejamento, plano de capítulo, manuscritos numerados, blocos, partes expandidas e uma consolidação editorial.

Uma versão SemVer representa um estado identificável de um artefato. Ela não pode designar simultaneamente múltiplos snapshots incompatíveis ou incompletos como se todos fossem o mesmo release.

### 3.3 Colisão de status

Termos como `Canon Edition`, `Decisão Editorial`, `Draft de Canon`, `redação definitiva` e `consolidação editorial` são utilizados em documentos diferentes, sem uma cadeia única de aprovação, commit, revisão, baseline ou publicação.

A autodeclaração dentro do PDF não comprova canonização no GKR.

## 4. Reconstrução da linhagem editorial

A ordem abaixo representa a reconstrução mais consistente possível com os arquivos localizados. Ela não declara que todos os documentos da família foram encontrados.

### Fase A — Fragmentos estruturais `0.1`

Inclui, entre outros:

- estrutura editorial do documento;
- capítulos individuais sobre pessoa, singularidade, contexto, possibilidades, escolhas, experiências, relações e organizações;
- drafts editoriais com partes específicas do futuro corpus.

**Classificação:** `historical_fragment`.

Os arquivos registram descoberta e redação inicial. Não constituem versões independentes completas do corpus.

### Fase B — Manuscrito vivo `0.2` a `0.7`

Foram localizados manuscritos declarados como `0.2`, `0.3`, `0.4`, `0.5`, `0.6` e `0.7`, com expansão progressiva de:

- modelo conceitual;
- missão antropológica;
- governança e critérios para módulos;
- resumo executivo;
- fundamentação conceitual;
- contexto do problema humano;
- hipótese de continuidade da jornada.

**Classificação:** `historical_working_manuscript`.

Essa sequência é a aproximação mais clara de uma linhagem versionada. Entretanto, os arquivos permanecem externos, sem prova de integração, revisão e baseline no GKR.

### Fase C — Transição prematura para Canon Edition

Foram localizados documentos chamados:

- Canon Edition Planning;
- plano mestre do Capítulo 1;
- Manuscritos 01 a 06;
- blocos do Capítulo 1;
- partes expandidas;
- consolidação editorial do Capítulo 1.

Diversos desses arquivos usam `v1.0`, apesar de representarem funções e recortes diferentes.

**Classificação:** `historical_canon_candidate_snapshot`.

Nenhum desses arquivos será tratado como release `GC-CON-001 1.0`.

### Fase D — Correção do método editorial

`GC-EDT-001 — Metodologia Editorial 2.0` encerra explicitamente o modelo de múltiplos PDFs incrementais e determina:

- Markdown como fonte oficial;
- um único manuscrito vivo por documento;
- Git como histórico;
- PDF apenas para leitura e distribuição;
- atualização contínua do mesmo `GC-CON-001` até a versão final.

**Classificação:** `external_editorial_resolution`.

Essa resolução é coerente com a operação atual do GKR, mas continua sendo fonte externa e não substitui as autoridades integradas.

### Fase E — Governança atual do GKR

A baseline atual utiliza:

- Git e Markdown;
- arquitetura federada de conhecimento;
- front matter e identificadores verificáveis;
- pipeline de evidência, consolidação, validação, auditoria e Canon;
- validação mecânica de IDs, links, navegação e build;
- Registro do Estado Atual como autoridade transversal.

O conteúdo externo somente pode ingressar por esse processo.

## 5. Inventário representativo

| Grupo | Exemplos identificados | Versão declarada | Classificação desta auditoria |
|---|---|---:|---|
| Estrutura | `GC-CON-001-Anthropology-of-Guivos-Estrutura` | 0.1 | fragmento histórico |
| Capítulos iniciais | Capítulos 1, 2, 3 e 5 | 0.1 | fragmentos históricos |
| Manuscrito vivo | `Anthropology-of-Guivos` | 0.2 a 0.7 | sequência de trabalho externa |
| Planejamento da Canon | `Canon-Edition-Planejamento` | 1.0 | plano histórico; não release |
| Plano de capítulo | `Canon-Edition-Capitulo-1-Plano` | 1.0 | plano histórico; não release |
| Manuscritos numerados | `Canon-Edition-Manuscrito-01` a `06` | 1.0 | snapshots candidatos; não releases |
| Blocos | `Canon-Edition-Capitulo-01-Bloco-*` | 1.0 | fragmentos candidatos |
| Partes expandidas | `Manuscrito-Expandido-Parte-*` | 1.0 | fragmentos candidatos |
| Consolidação | `Capitulo-01-Consolidacao-Editorial` | 1.0 | síntese histórica; não corpus completo |
| Método editorial | `GC-EDT-001-Metodologia-Editorial` | 2.0 | resolução externa de método |
| Plano editorial | `GC-EDT-002-Master-Editorial-Plan` | 0.1 a 0.3 | roadmap editorial externo |

O inventário é representativo e deverá ser expandido com hashes e metadados antes de qualquer intake físico.

## 6. Decisão de linhagem

### 6.1 Estado da família

A família externa `GC-CON-001` recebe o estado:

```text
external_lineage_conflicted
canonical_release_recognized: no
eligible_for_direct_import: no
eligible_as_evidence_source: yes
```

### 6.2 Tratamento dos arquivos `v1.0`

Todos os PDFs parciais declarados como `v1.0` são reclassificados, para fins do GKR, como snapshots históricos de uma tentativa de Canon Edition.

Eles não constituem:

- release canônica;
- baseline aprovada;
- autoridade normativa;
- versão final do corpus;
- prova de absorção pelos modelos atuais.

### 6.3 Bloqueio do identificador

O identificador exato `GC-CON-001` fica bloqueado para nova integração enquanto não houver:

1. inventário físico completo;
2. hashes dos arquivos;
3. comparação de conteúdo;
4. resolução de duplicidade;
5. matriz de conceitos e evidências;
6. comparação com a Foundation, GEB, PAS-001, GKA e demais autoridades vigentes;
7. decisão sobre preservar ou substituir o identificador;
8. um único manuscrito consolidado;
9. validação e auditoria;
10. PR autorizado.

O bloqueio evita criar no Git uma autoridade com o mesmo ID de dezenas de fontes incompatíveis.

### 6.4 Preservação da proveniência

Caso os arquivos sejam incorporados como evidência, cada arquivo deverá receber um identificador de fonte próprio, sem alterar o conteúdo original.

Exemplo de namespace de intake:

```text
SRC-GC-CON-001-001
SRC-GC-CON-001-002
SRC-GC-CON-001-003
```

O código da fonte não transforma o arquivo em conceito, princípio ou documento canônico.

### 6.5 Eventual documento consolidado

Uma futura consolidação poderá preservar o título `Anthropology of Guivos`, mas deverá possuir:

- um único path;
- um único ID reconhecido pelo GKR;
- uma versão inequívoca;
- front matter completo;
- escopo e autoridade explícitos;
- fontes rastreáveis;
- conceitos já absorvidos identificados;
- divergências e rejeições documentadas;
- relação formal com as arquiteturas atuais;
- aprovação pelo pipeline vigente.

A numeração `1.0.0` somente poderá ser usada após a existência desse artefato único e auditado.

## 7. Relação com autoridades integradas

A linhagem externa não substitui:

- Foundation Architecture;
- Fundamental Model;
- Guivos Ecosystem Blueprint;
- Guivos Principles integrados;
- PAS-001 e seus contratos;
- Guivos Evolution Framework;
- Guivos Knowledge Architecture;
- decisões arquiteturais integradas;
- glossário vigente.

Conceitos semelhantes encontrados nos PDFs deverão ser tratados como possíveis fontes ou antecedentes históricos. Sem uma matriz de comparação, semântica semelhante não comprova identidade, precedência ou autoridade.

## 8. Gates para futura consolidação temática

Uma futura frente dedicada deverá executar, no mínimo:

1. **Inventory Gate** — localizar todos os arquivos e registrar hash, nome, data e tamanho;
2. **Lineage Gate** — determinar predecessor, sucessor, duplicata e derivação;
3. **Extraction Gate** — extrair afirmações sem promovê-las;
4. **Deduplication Gate** — separar repetição editorial de evidência independente;
5. **Authority Gate** — comparar cada conceito com autoridades integradas;
6. **Conflict Gate** — resolver contradições e terminologia histórica;
7. **Consolidation Gate** — produzir um único candidato;
8. **Validation Gate** — avaliar cobertura, coerência, riscos e dependências;
9. **Audit Gate** — verificar IDs, versões, rastreabilidade e ausência de promoção implícita;
10. **Publication Gate** — integrar somente por PR autorizado.

## 9. Efeitos desta resolução

### Autorizados

- registrar a colisão como comprovada;
- classificar os PDFs como fontes históricas externas;
- bloquear integração direta com o ID conflitante;
- encaminhar o conteúdo a uma futura consolidação temática;
- corrigir o intake e a rastreabilidade do P0.

### Não autorizados

- selecionar um dos PDFs como versão final por conveniência;
- concatenar arquivos e chamar o resultado de Canon;
- promover conceitos por recorrência textual;
- substituir documentos integrados;
- criar princípio, Outcome, capability, produto ou requisito;
- iniciar UXA-071 ou Product Engineering;
- alterar `GKR-STATE-001` ou o marco vigente.

## 10. Resultado

```text
Target: external GC-CON-001 family
Identity collision: confirmed
Version collision: confirmed
Canonical v1.0: not recognized
Direct import: blocked
Historical preservation: required
Future thematic consolidation: required
Current-state change: no
```
