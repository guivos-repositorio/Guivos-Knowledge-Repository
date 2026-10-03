---
id: GKR-EXT-GOV-DISPOSITION-001
title: Disposição das Fontes Externas de Governança e Arquitetura do GKR
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
  - GKR-LINEAGE-GC-CON-001-001
normative: false
---

# Disposição das Fontes Externas de Governança e Arquitetura do GKR

## 1. Finalidade

Este documento compara fontes externas de governança, arquitetura do repositório e planejamento editorial com as autoridades atualmente integradas no Guivos Knowledge Repository.

A finalidade é definir se cada fonte deve ser:

- absorvida como princípio;
- preservada como antecedente histórico;
- substituída por autoridade posterior;
- encaminhada a outra frente;
- mantida fora do GKR;
- submetida a comparação adicional.

Esta disposição não transforma arquivos externos em autoridades e não altera o estado vigente.

## 2. Fontes externas avaliadas

| Fonte | Estado declarado | Escopo declarado |
|---|---|---|
| `GKR-001 — Governança do Guivos Knowledge Repository` | Aprovado, versão 1.0 | regras permanentes do GKR |
| `Guivos Knowledge Repository Architecture` | Draft, versão 1.0 | arquitetura documental do repositório |
| `Guivos Knowledge Repository` | sem baseline governada comprovada | estrutura física proposta para o repositório |
| `GC-GOV-001 — The Guivos Governance` | versão 0.1 | governança institucional ampla |
| `GC-EDT-001 — Metodologia Editorial` | versão 2.0 | resolução sobre manuscrito vivo, Markdown, Git e PDFs |
| `GC-EDT-002 — Master Editorial Plan` | versões 0.1 a 0.3 | roadmap editorial de uma coleção planejada |

## 3. Autoridades e controles atuais utilizados na comparação

### 3.1 Registro do Estado Atual

`GKR-STATE-001` define a situação transversal vigente. Nenhum PDF externo, README, changelog ou plano substitui essa autoridade.

### 3.2 ADR-006

`ADR-006 — Guivos Knowledge Architecture as a First-Class Architecture` reconhece a GKA e estabelece que conhecimento institucional deve ser descoberto, estruturado, validado, consolidado, promovido, governado e evoluído com evidências rastreáveis.

A arquitetura atual não trata o GKR apenas como diretório documental. Ela governa o processo de maturação do conhecimento.

### 3.3 A2-METHOD-001

`A2-METHOD-001 — Architectural Knowledge Consolidation Pipeline` separa:

- fonte;
- evidência;
- observação;
- regularidade;
- hipótese;
- consolidação;
- validação;
- auditoria;
- Canon.

Nenhuma fonte é promovida automaticamente por declaração de status ou recorrência textual.

### 3.4 GEA-AUDIT-001

`GEA-AUDIT-001 — Architectural Audit Framework` exige integridade documental, semântica, estrutural, metodológica, de governança, navegação e rastreabilidade antes de uma baseline.

### 3.5 Controles mecânicos

O repositório executa validação automatizada de:

- front matter;
- IDs;
- links;
- navegação;
- whitespace;
- build estrito do MkDocs;
- integridade da árvore rastreada.

O P1 propõe ainda um gate semântico próprio, mas permanece fora da `main` enquanto o PR nº 163 não for integrado.

## 4. Comparação de princípios

| Tema | Fontes externas | Estado atual no GKR | Disposição |
|---|---|---|---|
| Fonte oficial | GKR como fonte única da verdade | autoridade distribuída por módulo e Registro do Estado Atual transversal | princípio absorvido e refinado |
| Markdown | formato oficial para conhecimento permanente | padrão operacional predominante | absorvido |
| Git | histórico oficial | commits, branches, PRs e workflows em uso | absorvido |
| Modularidade | um conceito por arquivo e baixo acoplamento | arquitetura federada e contratos entre módulos | absorvido e ampliado |
| Front matter | ID, título, status, versão, owner e data | validado mecanicamente | absorvido e controlado |
| ADRs | toda decisão permanente deveria possuir ADR | ADRs coexistem com registros, matrizes, checkpoints e logs de decisão especializados | princípio limitado a decisões arquiteturais duráveis; regra universal não preservada |
| Mermaid e SVG | formatos preferenciais de diagramas | prática integrada em MkDocs e ativos versionados | absorvido |
| Estrutura estática de diretórios | `geb`, `adr`, `glossary`, `diagrams`, `assets`, `templates`, `roadmap` | repositório evoluiu para múltiplas arquiteturas e domínios | estrutura substituída |
| GEB como artefato principal | GEB concentrava grande parte da arquitetura | GEA e arquiteturas especializadas possuem autoridades próprias | estrutura substituída por modelo federado |
| Evolução contínua | repositório nunca concluído | preservado com estados, versões, marcos e baselines | absorvido e governado |
| Manuscrito vivo | um único manuscrito Markdown e PDF derivado | coerente com Git e arquivos Markdown; PDFs não são autoridades automáticas | princípio absorvido operacionalmente |
| Coleção editorial | volumes e ordem de escrita predefinidos | não constitui roadmap arquitetural vigente | não absorvido como autoridade |

## 5. Disposição individual

### 5.1 `GKR-001 — Governança do Guivos Knowledge Repository`

#### Conteúdo preservável

O documento registra princípios que permanecem materialmente válidos:

- GKR como fonte oficial;
- Markdown como formato permanente;
- Git como histórico;
- modularidade;
- baixo acoplamento;
- evolução contínua;
- front matter;
- rastreabilidade;
- ADRs para decisões arquiteturais duráveis;
- Mermaid e SVG como formatos preferenciais.

#### Desvios e limitações

- apresenta status `Aprovado` fora da governança Git atual;
- usa `GKR-001` no título e também a referência `GKR-GOVERNANCE-RULES-001`, criando ambiguidade de identidade;
- descreve uma estrutura de diretórios antiga e incompleta;
- trata o GEB como artefato arquitetural central, anterior à GEA federada atual;
- não incorpora GKA, pipeline de evidência, maturidade, auditoria transversal, current-state register ou gates automatizados;
- formula ADR como mecanismo universal, enquanto o GKR atual utiliza registros decisórios especializados quando apropriado.

#### Decisão

```text
status_in_gkr: historical_governance_source
principles_partially_absorbed: yes
current_authority: no
direct_import: no
```

O arquivo deve ser preservado como antecedente histórico e fonte de proveniência. Não deve ser copiado integralmente para um novo documento normativo.

### 5.2 `Guivos Knowledge Repository Architecture`

#### Conteúdo preservável

- independência de ferramenta;
- Markdown;
- modularidade;
- rastreabilidade por Git, changelog, ADR e versões;
- uso do MkDocs;
- separação de domínios.

#### Desvios e limitações

- é declarado Draft 1.0;
- apresenta estrutura estática anterior à expansão do repositório;
- posiciona o GEB como principal artefato arquitetural;
- não contém a GKA como arquitetura de primeira classe;
- não distingue evidência, hipótese, conhecimento consolidado e Canon;
- não representa as arquiteturas atuais de Produto, Experiência, Inteligência, Economia, Negócios e Evolução;
- não representa os controles mecânicos e semânticos atuais.

#### Decisão

```text
status_in_gkr: superseded_architecture_proposal
historical_value: yes
current_authority: no
direct_import: no
```

`ADR-006`, as arquiteturas integradas e a estrutura real da `main` substituem essa proposta como descrição vigente.

### 5.3 `Guivos Knowledge Repository`

O arquivo apresenta uma árvore física extensa proposta para o repositório.

A árvore não corresponde à estrutura atual e contém produtos, especificações e diretórios planejados que não devem ser inferidos como existentes ou autorizados.

#### Decisão

```text
status_in_gkr: historical_repository_layout_proposal
current_layout_authority: no
implementation_evidence: no
```

O arquivo pode ser preservado apenas como registro histórico de intenção estrutural.

### 5.4 `GC-GOV-001 — The Guivos Governance`

O documento trata governança institucional ampla, incluindo conselho, curadoria, arquitetura, squads e fluxo entre evidência, hipótese, princípio, decisão, implementação, métricas e aprendizado.

#### Limitações

- versão 0.1;
- externo ao GKR;
- papéis e instâncias organizacionais não possuem comprovação de constituição ou operação;
- mistura governança corporativa, conhecimento, arquitetura e execução;
- não possui relação formal com as autoridades atuais;
- pode antecipar estruturas organizacionais inexistentes.

#### Decisão

```text
status_in_gkr: external_governance_hypothesis
route: future_governance_package
current_authority: no
organizational_claims_authorized: no
```

Princípios abstratos podem ser avaliados futuramente. Papéis, conselhos, squads e níveis de aprovação não serão tratados como estruturas existentes.

### 5.5 `GC-EDT-001 — Metodologia Editorial 2.0`

O documento encerra o modelo de múltiplos PDFs incrementais e prescreve Markdown, Git, manuscrito único e PDF derivado.

#### Decisão

```text
status_in_gkr: external_editorial_resolution
operational_alignment: high
current_authority: no
principle_absorbed_in_practice: yes
```

Sua regra central está alinhada à operação atual. O documento permanece fonte histórica, e não política normativa integrada.

### 5.6 `GC-EDT-002 — Master Editorial Plan`

A família 0.1 a 0.3 descreve volumes, ordem de escrita, metas editoriais, maturidade e roadmap de uma coleção.

#### Limitações

- é um plano editorial externo;
- as versões 0.1, 0.2 e 0.3 alteram escopo e estrutura;
- não representa o roadmap arquitetural vigente;
- menciona UKs, volumes e coleções que exigem reconciliação;
- não autoriza produção, publicação ou prioridade de frentes atuais.

#### Decisão

```text
status_in_gkr: external_editorial_plan
route: P9 or dedicated editorial review
current_authority: no
backlog_authorization: no
```

## 6. Modelo atual de autoridade

A comparação demonstra que a governança vigente não está concentrada em um único documento externo chamado `GKR-001`.

Ela é composta por autoridades complementares:

| Função | Autoridade ou controle atual |
|---|---|
| Estado transversal | `GKR-STATE-001` |
| Decisão sobre a Knowledge Architecture | `ADR-006` |
| Maturação do conhecimento | `A2-METHOD-001` |
| Auditoria arquitetural | `GEA-AUDIT-001` |
| Autoridade de domínio | documento normativo da arquitetura correspondente |
| Decisões especializadas | ADR, decision register, matrix, checkpoint ou log aplicável |
| Histórico | Git, PRs, commits e changelogs |
| Integridade mecânica | workflow e validadores do repositório |
| Navegação pública | MkDocs, sem criar autoridade própria |

Essa distribuição reduz o risco de um documento geral sobrescrever silenciosamente decisões especializadas.

## 7. Decisão consolidada

| Fonte externa | Disposição final | Pode alterar o estado? | Pode ser copiada diretamente? |
|---|---|---:|---:|
| GKR-001 | fonte histórica parcialmente absorvida | não | não |
| GKR Architecture Draft | proposta substituída | não | não |
| GKR repository tree | layout histórico proposto | não | não |
| GC-GOV-001 | hipótese de governança futura | não | não |
| GC-EDT-001 2.0 | resolução editorial externa alinhada à prática | não | não |
| GC-EDT-002 | plano editorial externo | não | não |

## 8. Controles decorrentes

A partir desta disposição:

1. `GKR-001` não será citado como autoridade vigente sem qualificação histórica;
2. a estrutura do PDF de arquitetura não será usada para recriar diretórios ou produtos;
3. papéis organizacionais do `GC-GOV-001` não serão tratados como existentes;
4. o `GC-EDT-002` não será tratado como backlog autorizado;
5. PDFs derivados permanecerão evidência, não fonte normativa;
6. princípios úteis serão vinculados às autoridades integradas que atualmente os implementam;
7. conflitos futuros serão resolvidos em favor da autoridade integrada e do processo governado;
8. qualquer nova política geral deverá demonstrar como convive com autoridades de domínio, sem centralização indevida.

## 9. Pendências residuais

Ainda será necessário, caso se deseje preservar fisicamente as fontes:

- registrar hashes;
- armazenar apenas quando a sensibilidade permitir;
- criar metadados de proveniência;
- definir área histórica ou de evidências;
- evitar publicação de informações confidenciais;
- registrar relação `source → principle → current authority`;
- decidir se uma síntese histórica pública possui valor.

Essas ações não são necessárias para reconhecer que os arquivos externos não são autoridades vigentes.

## 10. Resultado

```text
External governance sources reviewed: 6 families
Current authority collision: resolved
Useful principles: partially absorbed
Static repository architecture: superseded
Corporate governance draft: deferred
Editorial plan: deferred
Direct canonical import: blocked
Current-state change: no
```
