---
id: A2-METHOD-001
title: Architectural Knowledge Consolidation Pipeline
status: validated
version: 2.0.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-27
scope: GKR and GEA
normative: true
---

# A2-METHOD-001 — Architectural Knowledge Consolidation Pipeline

## 1. Finalidade

Definir o processo oficial pelo qual conhecimento arquitetural evolui desde uma fonte documental até sua eventual promoção à Canon e, quando uma autoridade é substituída, como seu conteúdo vigente é absorvido antes da remoção do corpus atual.

O pipeline protege simultaneamente:

- rastreabilidade;
- separação entre evidência, hipótese e Canon;
- atualidade;
- completude;
- redução de redundância;
- concentração da verdade vigente em autoridades claras;
- remoção controlada de versões que perderam função atual.

Princípio de arquivo:

> **Git preserva a história. GKR preserva o conhecimento vigente.**

## 2. Modos oficiais

### 2.1 Discovery Mode

É o modo de investigação arquitetural.

Permite:

- questionar conceitos existentes;
- extrair evidências;
- registrar observações;
- identificar regularidades;
- formular hipóteses;
- buscar contraexemplos;
- fundir, refinar, adiar ou rejeitar candidatos.

Nenhum conteúdo produzido em Discovery Mode é automaticamente canônico.

### 2.2 Canon Mode

É o modo de preservação e publicação arquitetural.

Permite apenas:

- consolidar conhecimento com suporte suficiente;
- atualizar rastreabilidade necessária;
- corrigir inconsistências comprovadas;
- registrar decisões formais vigentes;
- publicar novas versões e baselines;
- substituir autoridades anteriores de forma explícita;
- remover do corpus atual aquilo que perdeu função depois da absorção do conteúdo válido.

A passagem de Discovery Mode para Canon Mode exige evidência, consolidação, validação e governança formal.

## 3. Fluxo oficial de maturação

```text
Fonte oficial
  → Evidence Extraction
  → Observações
  → Regularidades
  → Hipóteses
  → Testes e revisão
  → Evidence Matrix
  → Canonical Consolidation
  → Readiness Assessment
  → Architectural Validation
  → Architectural Audit
  → Baseline / Canon
```

## 4. Fluxo oficial de atualização de conhecimento já existente

Quando o GKR evolui e um conhecimento vigente precisa ser atualizado, o fluxo é:

```text
DETECTAR MUDANÇA
→ IDENTIFICAR AUTORIDADES AFETADAS
→ CLASSIFICAR CONFLITO / DUPLICAÇÃO / DEFASAGEM
→ EXTRAIR TODO CONTEÚDO AINDA VÁLIDO
→ RECONCILIAR COM A NOVA VERDADE
→ CONSOLIDAR NA AUTORIDADE VIGENTE
→ PROPAGAR PARA DEPENDÊNCIAS REAIS
→ VALIDAR SEMÂNTICA E MECANICAMENTE
→ REMOVER REFERÊNCIAS OBSOLETAS
→ REMOVER ARTEFATOS SEM FUNÇÃO ATUAL
→ PRESERVAR HISTÓRICO PELO GIT
```

A antiga prática de manter indefinidamente `master + addendum + propagation + reconciliation + checkpoint` é considerada dívida quando todos esses arquivos tratam da mesma verdade atual.

## 5. Etapas de maturação

### 5.1 Fonte oficial

Documento ou corpus submetido à análise.

Deve preservar conteúdo, versão, estado, ownership e localização rastreável enquanto estiver sob análise.

### 5.2 Evidence Extraction

Extrai apenas aquilo que o corpus afirma explicitamente.

Cada evidência deve conter:

- identificador;
- fonte e localização;
- trecho literal quando necessário;
- elementos explícitos.

Interpretação não pertence a esta etapa.

### 5.3 Observações

Registram fatos verificáveis identificados nas evidências.

Toda observação deve indicar quais evidências a sustentam.

### 5.4 Regularidades

Agrupam padrões recorrentes sustentados por múltiplas observações.

Regularidade não é hipótese e não é Canon.

### 5.5 Hipóteses

Explicações provisórias para as regularidades encontradas.

Hipóteses devem permanecer separadas de decisões validadas e ser submetidas a explicações alternativas, incompatibilidades e contraexemplos.

### 5.6 Evidence Matrix

Consolida evidências, observações, regularidades, hipóteses e resultados de revisão entre fontes.

Cada agrupamento deve ser avaliado segundo frequência, centralidade, consistência, confirmação, ampliação, ausência, contradição e independência das fontes.

### 5.7 Canonical Consolidation

Transforma o inventário provisório em um conjunto mínimo e suficiente **sem perder informação material**.

Cada item recebe uma decisão:

| Decisão | Significado |
|---|---|
| Preserve | Mantém-se praticamente inalterado |
| Merge | É fundido a item equivalente |
| Refine | Permanece com redação ou fronteira aprimorada |
| Split | Contém mais de uma responsabilidade ou natureza |
| Remove | É redundante, circunstancial ou sem suporte suficiente |
| Defer | Depende de evidências ou arquiteturas ainda não disponíveis |

Regra obrigatória:

> **Consolidar não significa resumir.**

Se dois documentos forem fundidos, o destino deve preservar tudo que continuar materialmente válido, inclusive:

- fluxos;
- diagramas;
- tabelas;
- estados alternativos;
- critérios de aceite;
- regras de bloqueio;
- exemplos e contraexemplos;
- guardrails;
- riscos;
- dependências;
- limitações e incertezas.

### 5.8 Readiness Assessment

Verifica se o conjunto consolidado está pronto para sustentar validação e arquiteturas dependentes.

### 5.9 Architectural Validation

Avalia cobertura, coerência, lacunas, conflitos, ambiguidades, dependências e riscos.

### 5.10 Architectural Audit

Verifica aplicação do método, rastreabilidade, integridade dos registros, atualidade, completude e aderência às decisões superiores.

### 5.11 Baseline e Canon

Somente conhecimento consolidado, validado, auditado e governado pode ser incorporado à Canon ou congelado em baseline.

## 6. Pipeline de absorção e remoção

Quando uma autoridade ou artefato perde função atual, a remoção deve obedecer ao pipeline abaixo.

### 6.1 Detectar

Identificar um ou mais sinais:

- `superseded`;
- `deprecated`;
- checkpoint antigo;
- snapshot de construção;
- adendo já incorporável;
- reconciliação já absorvível;
- duplicação sem fronteira própria;
- conteúdo contradito por autoridade posterior;
- artefato visual que deixou de ser baseline;
- versão intermediária mantida apenas por histórico.

### 6.2 Classificar

Classificar o artefato como:

- autoridade ainda vigente;
- evidência necessária;
- conteúdo parcialmente válido;
- duplicação;
- histórico sem função atual.

### 6.3 Extrair conteúdo vigente

Antes de qualquer exclusão, identificar todo conteúdo ainda necessário.

A análise deve perguntar:

- existe definição única?
- existe regra ainda vigente?
- existe exemplo ainda útil?
- existe diagrama não reproduzido?
- existe estado alternativo ou exceção ainda necessária?
- existe evidência que sustenta claim atual?
- algum documento atual aponta para este artefato como autoridade?

### 6.4 Absorver

Mover semanticamente o conhecimento válido para a autoridade atual correta.

Absorção pode exigir atualização de:

- documento mestre;
- registry;
- jornada integrada;
- política;
- modelo de produto;
- Home;
- roadmap;
- Estado Atual;
- menu;
- diagrama;
- catálogo;
- matriz.

### 6.5 Reconciliar dependências

Corrigir:

- links;
- `depends_on`;
- `related`;
- IDs;
- contagens;
- galerias;
- navegação;
- diagramas;
- referências textuais;
- claims de maturidade.

### 6.6 Validar

Executar validações aplicáveis sobre o mesmo head que contém absorção e remoção planejada.

A remoção não recebe `PASS` por intenção. Deve ser provado que o corpus remanescente é suficiente.

### 6.7 Remover do corpus vigente

Depois da absorção e reconciliação, remover arquivos sem função atual do branch canônico.

Isso inclui, quando aplicável:

- Markdown;
- SVG;
- assets auxiliares;
- entradas de MENU;
- referências em registries;
- contagens derivadas.

### 6.8 Preservar histórico

A rastreabilidade histórica permanece disponível por:

- commits;
- PRs;
- branches históricas quando existentes;
- tags/releases quando aplicáveis.

Não é necessário duplicar a função do Git dentro da navegação atual do GKR.

## 7. Princípios obrigatórios

### 7.1 Primazia da evidência

Nenhum conceito, capacidade, relação ou camada pode ser promovido por preferência, elegância ou recorrência terminológica isolada.

### 7.2 Primazia da realidade

Os documentos representam a realidade arquitetural descoberta. Quando evidências consolidadas demonstrarem inadequação documental, o documento deve ser revisado por processo formal.

### 7.3 Convergência antes da consolidação

Um único trecho pode gerar uma evidência, mas não autoriza sozinho a promoção de um conceito permanente.

### 7.4 Separação de camadas

Evidência, observação, regularidade, hipótese, consolidação e Canon são estados distintos e não podem ser tratados como equivalentes.

### 7.5 Hipóteses fora da Canon

Hipóteses podem orientar investigação, mas devem permanecer explicitamente identificadas até validação.

### 7.6 Rastreabilidade integral

Toda decisão arquitetural deve ser rastreável às fontes, evidências, análises e decisões que a sustentam na medida necessária para sustentar a verdade vigente.

Rastreabilidade não exige manter documentos substituídos no corpus atual quando o Git já preserva sua história.

### 7.7 Suficiência arquitetural

O objetivo é produzir o menor conjunto de autoridades capaz de explicar integralmente o domínio sem perda relevante de significado.

`MENOR CONJUNTO DE AUTORIDADES ≠ MENOR QUANTIDADE DE DETALHE`.

### 7.8 Estabilidade durante a execução

O método permanece congelado durante um ciclo de análise. Alterações exigem limitação prática comprovada.

### 7.9 Verdade vigente sem cadeia histórica

Uma pessoa deve conseguir responder “o que vale hoje?” lendo a autoridade vigente e seus suportes atuais, sem reconstruir cronologia de PRs.

### 7.10 Propagação não substitui atualização

Um documento de propagação pode ser útil durante uma transição, mas não deve permanecer como correção permanente de um master desatualizado.

```text
PROPAGAÇÃO TEMPORÁRIA
→ atualizar master afetado
→ validar dependências
→ remover propagação quando não possuir função própria
```

### 7.11 Evidência não é lixo histórico

Documentos de evidência permanecem quando necessários para sustentar:

- gate;
- claim;
- compliance;
- decisão de risco;
- validação;
- estado operacional.

A regra de limpeza não autoriza apagar suporte probatório vigente.

## 8. Estados de maturidade do conhecimento

| Estado | Definição |
|---|---|
| Extracted | Evidência literal registrada |
| Observed | Observação ligada a evidências |
| Patterned | Regularidade identificada |
| Hypothesized | Explicação provisória registrada |
| Corroborated | Hipótese reforçada por múltiplas fontes |
| Consolidated | Elemento deduplicado e estabilizado |
| Under Review | Elemento submetido à revisão arquitetural |
| Validated | Elemento aprovado pela validação aplicável |
| Canonical | Elemento incorporado formalmente à Canon |
| Rejected | Elemento rejeitado com justificativa |
| Deferred | Elemento adiado por dependência ou insuficiência |

Estados de maturidade não devem ser usados como desculpa para acumular versões substituídas. Quando um elemento `Canonical` é substituído, a versão anterior permanece no Git e deixa o corpus atual após a absorção necessária.

## 9. Aplicabilidade

O pipeline pode ser aplicado a:

- Foundation Architecture;
- Fundamental Model;
- Core Capability Model;
- Business Architecture;
- Product Architecture;
- Guivos Economic Model;
- Intelligence Architecture;
- Experience Architecture;
- Data, Technology, Governance e Knowledge Architectures;
- Brand e Go-to-Market quando houver dependência arquitetural;
- Research e Validation quando seus outputs alimentarem autoridades do GKR;
- revisões transversais da GEA;
- auditorias integrais do próprio corpus.

## 10. Aplicação ao GKR como base multiequipe

Quando o GKR for consumido por Marketing, Publicidade, Comercial, Produto, UX, Design, Dev, Jurídico/Privacidade, Research ou liderança, a consolidação deve priorizar:

- autoridade clara;
- leitura atual;
- fronteiras entre domínios;
- caminhos de navegação adequados à função;
- reutilização da mesma fonte por equipes distintas;
- ausência de cópias paralelas da mesma verdade.

Uma rota de navegação por equipe pode apontar para autoridades compartilhadas, mas não deve duplicá-las.

## 11. Critério de encerramento de uma consolidação

Uma consolidação só está encerrada quando:

1. a autoridade destino contém todo conteúdo atual necessário;
2. conflitos foram resolvidos explicitamente;
3. dependências foram reconciliadas;
4. exemplos, fluxos e guardrails materiais foram preservados;
5. artefatos substituídos não são mais necessários para interpretar o estado atual;
6. links e contagens não dependem deles;
7. validações aplicáveis passaram;
8. o artefato obsoleto foi removido do corpus atual quando não possui função própria;
9. a navegação aponta para a nova autoridade;
10. o Git permanece como histórico suficiente da transição.

## 12. Limites

Este método governa a maturação e consolidação do conhecimento arquitetural. Ele não substitui métodos especializados de pesquisa, modelagem, design, engenharia, implementação, operação, privacidade, segurança ou validação jurídica.

Também não autoriza que uma auditoria documental promova uma condição operacional inexistente.

```text
DOCUMENTADO
≠ IMPLEMENTADO
≠ TESTADO
≠ OPERACIONAL
≠ VALIDADO EM CAMPO
```
