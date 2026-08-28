---
id: GEA-AUDIT-001
title: Architectural Audit Framework
status: validated
version: 2.0.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-27
scope: Cross-Architecture Governance
normative: true
---

# Architectural Audit Framework

## 1. Finalidade

Definir o processo transversal de auditoria que verifica a integridade de uma revisão arquitetural e, quando aplicado ao Guivos Knowledge Repository, a integridade do **corpus vigente** antes de sua baseline.

A auditoria não cria verdade por inferência, não substitui validação de domínio e não promove maturidade operacional. Ela verifica se o conjunto produzido é íntegro, coerente, rastreável, navegável, suficientemente detalhado e governável.

No GKR, a auditoria também possui uma responsabilidade editorial e estrutural explícita:

> **o corpus publicado deve representar a verdade vigente da Guivos; a história de versões pertence ao Git, não à camada atual de conhecimento.**

Isso significa que documentos, artefatos, snapshots, checkpoints, adendos, reconciliações ou materializações que perderam autoridade não devem permanecer no corpus vigente apenas para registrar como a construção aconteceu.

## 2. Regra de fonte de verdade vigente

A governança do GKR distingue duas camadas:

```text
GIT
→ preserva commits, branches, PRs, versões anteriores e histórico de evolução

GKR NO MAIN / SITE PUBLICADO
→ preserva somente conhecimento vigente, necessário e suficientemente detalhado
```

Consequências obrigatórias:

1. `superseded`, `deprecated`, `historical`, `checkpoint`, `snapshot`, `propagation` ou `reconciliation` não são destinos permanentes por si só;
2. antes de remover um artefato obsoleto, todo conteúdo ainda válido e único deve ser absorvido pela autoridade vigente apropriada;
3. depois da absorção e da validação das referências, o artefato obsoleto deve ser removido do `main`;
4. nenhuma verdade atual pode depender da leitura de uma cadeia histórica de documentos para ser compreendida;
5. a exclusão do corpus vigente não apaga a rastreabilidade, porque o Git preserva o histórico;
6. evidência primária que ainda sustenta uma claim vigente não deve ser removida apenas por ser antiga;
7. um documento antigo pode permanecer quando ainda for a autoridade vigente e estiver consistente com as decisões posteriores;
8. a consolidação não autoriza resumir a ponto de perder fluxos, diagramas, exemplos, guardrails, exceções, estados alternativos ou critérios de decisão ainda válidos.

Regra operacional:

```text
OBSOLETO + CONTEÚDO ÚNICO VÁLIDO
→ ABSORVER
→ REVALIDAR
→ CORRIGIR REFERÊNCIAS
→ REMOVER DO CORPUS VIGENTE
→ HISTÓRICO CONTINUA NO GIT
```

## 3. Posição no ciclo

Para uma revisão arquitetural convencional:

```text
Evidence Analysis
  → Evidence Matrix
  → Canonical Consolidation
  → Readiness Assessment
  → Architectural Validation
  → Architectural Audit
  → Baseline
```

Para uma auditoria integral do GKR:

```text
INVENTÁRIO DO CORPUS
→ MAPA DE AUTORIDADE E DEPENDÊNCIAS
→ DETECÇÃO DE CONFLITOS / FRAGMENTAÇÃO / OBSOLESCÊNCIA
→ ABSORÇÃO DO CONTEÚDO VÁLIDO
→ REESCRITA DAS AUTORIDADES VIGENTES
→ REMOÇÃO DO OBSOLETO
→ RECONCILIAÇÃO DE REFERÊNCIAS E CONTAGENS
→ AUDITORIA DAS HOMES E SUPERFÍCIES PÚBLICAS
→ REARQUITETURA DO MENU
→ VALIDAÇÃO SEMÂNTICA E MECÂNICA
→ AUDITORIA FINAL DE COMPLETUDE
→ BASELINE LIMPA
```

## 4. Princípios

1. auditoria verifica e reconcilia o corpus; não inventa decisões de domínio;
2. validação decide; auditoria testa a integridade e a propagação da decisão;
3. nenhuma baseline pode ser congelada com não conformidade crítica aberta;
4. toda conclusão deve ser sustentada por evidência documental ou evidência operacional explicitamente classificada;
5. o rigor da auditoria deve ser proporcional à permanência e ao alcance do ativo;
6. o método somente evolui quando sua aplicação revela limitação objetiva;
7. o Git é o arquivo histórico; o GKR vigente é a base operacional de conhecimento;
8. consolidação deve reduzir fragmentação **sem reduzir significado**;
9. detalhe útil deve permanecer próximo da autoridade que governa o assunto;
10. nenhuma equipe deve precisar conhecer a ordem histórica de construção para encontrar a verdade vigente;
11. o MENU deve orientar por domínio, responsabilidade e necessidade de trabalho, e não por cronologia de PRs ou rodadas;
12. uma Home somente pode ser considerada consistente quando estiver alinhada às autoridades vigentes de Fundação, Marca, Produto, Participantes, Economia, Privacidade e claims públicas aplicáveis;
13. ausência editorial em uma consolidação não revoga conhecimento válido, mas também não autoriza mantê-lo espalhado indefinidamente;
14. nenhuma limpeza pode apagar evidência necessária para sustentar estado, gate, obrigação, decisão ou claim ainda vigente.

## 5. Escopo mínimo

| Dimensão | Verificação |
|---|---|
| Documental | Artefatos necessários existem e estão no estado correto |
| Terminológica | Termos, nomes, assinaturas e identificadores são consistentes |
| Estrutural | Dependências, autoridades e ordem do pipeline estão corretas |
| Semântica | Não há conflito material entre fontes, consolidação e decisão |
| Rastreabilidade | Elementos vigentes retornam às evidências necessárias |
| Metodológica | Nenhuma etapa obrigatória foi omitida ou invertida |
| Governança | Status, versão, owner, data, decisão e baseline são explícitos |
| Atualidade | Autoridades antigas foram confrontadas com decisões posteriores |
| Obsolescência | Conteúdo substituído foi absorvido e removido quando cabível |
| Fragmentação | Um mesmo conhecimento não exige leitura desnecessária de múltiplos arquivos |
| Completude | Fluxos, estados, exemplos, diagramas, guardrails e exceções materiais foram preservados |
| Navegação | MENU e rotas de leitura refletem o corpus vigente |
| Multiequipe | Marketing, Publicidade, Comercial, Produto/UX, Design, Dev, Jurídico/Privacidade e Research conseguem localizar suas autoridades |
| Superfícies públicas | Homes e demais claims públicas não promovem estado superior ao vigente |
| Referências | Links, IDs, contagens, galerias e registries não apontam para material removido ou sem autoridade |

## 6. Unidade de análise

A auditoria não deve assumir que `arquivo = autoridade`.

Cada item deve ser classificado segundo sua função real:

- autoridade mestre de domínio;
- autoridade especializada;
- evidência primária;
- registro operacional ainda necessário;
- instrumento metodológico vigente;
- materialização vigente;
- derivado de navegação;
- duplicação;
- fragmento absorvível;
- artefato substituído;
- registro histórico dispensável no corpus atual.

A decisão de permanência é feita pela utilidade e autoridade **atuais**, não pela idade do arquivo.

## 7. Classificação de ação documental

Toda auditoria integral deve atribuir uma ação explícita aos artefatos examinados:

| Ação | Significado |
|---|---|
| `KEEP` | Continua necessário e vigente como está ou com ajuste editorial mínimo |
| `UPDATE` | Continua necessário, mas está defasado frente a autoridades posteriores |
| `CONSOLIDATE` | Conteúdo válido deve ser absorvido por autoridade mais adequada para reduzir fragmentação |
| `REBUILD` | A estrutura atual perdeu coerência e deve ser reconstruída preservando o conteúdo válido |
| `REMOVE_AFTER_ABSORPTION` | Não deve permanecer no corpus atual depois que seu conteúdo válido for absorvido |
| `REMOVE` | Não possui conteúdo atual necessário ou já está integralmente substituído |
| `EVIDENCE_KEEP` | É evidência necessária para sustentar claim/gate vigente, mesmo não sendo uma autoridade de leitura principal |
| `HOLD_REVIEW` | Evidência insuficiente para decidir sem análise adicional |

Nenhum `REMOVE` ou `REMOVE_AFTER_ABSORPTION` é executado antes de verificar referências e conteúdo único.

## 8. Evidências obrigatórias

Uma revisão arquitetural somente pode ser auditada quando possuir, conforme aplicável:

- Evidence Analysis;
- Evidence Matrix;
- Canonical Consolidation;
- Readiness Assessment;
- Architectural Validation;
- Decision Log;
- registro de riscos e recomendações;
- proposta de baseline.

Uma auditoria integral do GKR pode usar como conjunto probatório:

- `main` reconciliado em SHA explícito;
- front matter e conteúdo integral dos documentos;
- dependências, `related`, links e IDs;
- `mkdocs.yml`;
- registries, catálogos, galerias e matrizes;
- PRs/commits quando necessários para esclarecer autoridade atual;
- workflows de validação;
- evidência operacional apenas quando explicitamente necessária e classificada.

## 9. Testes obrigatórios de corpus vigente

### 9.1 Teste de autoridade

Para cada conceito material:

- existe uma autoridade principal identificável?
- documentos de apoio possuem fronteiras claras?
- uma decisão mais recente conflita com a autoridade antiga?
- é necessário ler um adendo para corrigir um documento mestre?

Se a verdade atual depender permanentemente de `master + correção + propagação + reconciliação`, existe dívida de consolidação.

### 9.2 Teste de obsolescência

Para cada artefato marcado ou tratado como histórico/superseded:

1. contém informação atual única?
2. essa informação já está absorvida em autoridade vigente?
3. existem links ou contagens que ainda dependem dele?
4. sua remoção altera evidência necessária?
5. após corrigir dependências, ele ainda possui função atual?

Se a resposta final for não, deve ser removido do corpus atual.

### 9.3 Teste de fragmentação

Uma família falha quando:

- conceitos básicos se repetem em muitos arquivos sem autoridade clara;
- exemplos e regras materiais ficam distantes do documento que governa a decisão;
- múltiplos checkpoints precisam ser lidos para entender o estado vigente;
- a mesma taxonomia possui variações conflitantes;
- uma equipe precisa reconstruir a cronologia para saber o que vale hoje.

### 9.4 Teste de completude

Consolidação somente é válida quando preserva, conforme aplicável:

- definição;
- finalidade;
- atores e autoridades;
- entradas e saídas;
- fluxos;
- estados principais e alternativos;
- exceções;
- restrições;
- critérios de aceite;
- critérios de bloqueio;
- exemplos;
- contraexemplos;
- diagramas;
- relações com outros domínios;
- evidência e limitações;
- o que não pode ser inferido.

`CONSOLIDAR ≠ RESUMIR`.

### 9.5 Teste de Home

Cada Home deve ser confrontada, no mínimo, com:

- Fundação e Propósito vigentes;
- sistema de marca e assinatura vigente;
- autoridade pública institucional e humana aplicável;
- participantes e papéis vigentes;
- Produto Especializado correspondente, quando existir;
- taxonomias vigentes;
- economia/planos/pontos quando material;
- privacidade e limites de claims;
- Research e evidência real quando a Home mencionar resultado, impacto, relevância ou inteligência;
- outras Homes para evitar sobreposição de autoridade.

Resultado por Home:

```text
CURRENT
| UPDATE_REQUIRED
| REBUILD_REQUIRED
```

Uma Home em `draft` pode estar conceitualmente correta; uma Home `active` pode estar defasada. Status sozinho não substitui a auditoria de conteúdo.

### 9.6 Teste de MENU

O MENU deve responder a duas necessidades simultâneas:

1. leitura arquitetural por domínio;
2. acesso prático por função/equipe.

Não deve exigir conhecimento de IDs históricos, número de rodada, PR ou ordem de construção.

Uma rota por equipe pode apontar para as mesmas autoridades sem duplicar conteúdo.

## 10. Classificação de não conformidades

| Classe | Definição | Efeito |
|---|---|---|
| Critical | Compromete decisão, autoridade, rastreabilidade ou integridade do corpus | Bloqueia baseline |
| Major | Lacuna relevante de consistência, atualidade, completude, navegação ou governança | Exige correção antes da baseline |
| Minor | Desvio sem impacto material na decisão | Pode ser corrigido com plano registrado |
| Observation | Oportunidade de melhoria sem não conformidade | Não bloqueia |

Exemplos de `Critical/Major` em auditoria integral:

- Home pública contradiz assinatura ou posicionamento vigente;
- documento mestre é corrigido apenas por adendo posterior;
- artefato superseded continua sendo usado como baseline atual;
- remoção proposta apagaria evidência ainda necessária;
- duas taxonomias concorrentes aparecem como vigentes;
- MENU leva equipe a conteúdo substituído como se fosse atual;
- claims operacionais são promovidas sem evidência.

## 11. Checklist padrão

### Integridade documental

- [ ] Todos os artefatos necessários existem.
- [ ] Identificadores, títulos, versões e status são consistentes.
- [ ] As entradas e saídas de cada etapa estão explícitas.
- [ ] Não há artefatos históricos permanentes sem função atual.

### Integridade semântica

- [ ] Não existem contradições materiais não resolvidas.
- [ ] Nenhum elemento foi promovido além da força das evidências.
- [ ] Absorções, fusões, refinamentos e remoções possuem justificativa.
- [ ] A autoridade vigente contém a formulação atual sem depender de correção histórica externa.

### Rastreabilidade

- [ ] Todos os elementos consolidados possuem origem suficiente.
- [ ] Toda decisão formal referencia os artefatos avaliados quando necessário.
- [ ] Riscos e limitações permanecem visíveis.
- [ ] A exclusão do corpus não remove a história do Git.

### Consolidação

- [ ] Conteúdo duplicado foi eliminado ou claramente subordinado.
- [ ] Nenhum detalhe material foi perdido na consolidação.
- [ ] Fluxos, exemplos, estados e guardrails foram preservados.
- [ ] Checkpoints/adendos foram absorvidos quando deixaram de possuir função atual.

### Navegação

- [ ] O MENU aponta somente para conhecimento vigente e útil.
- [ ] As rotas principais são compreensíveis sem conhecer a cronologia do projeto.
- [ ] Equipes conseguem localizar seus domínios de trabalho.
- [ ] O mesmo documento pode ser reutilizado por rotas distintas sem duplicação de autoridade.

### Homes

- [ ] Todas as Homes foram auditadas contra as autoridades posteriores.
- [ ] Assinaturas, claims, taxonomias e fronteiras de produto estão atuais.
- [ ] Nenhuma Home confunde visão com disponibilidade real.
- [ ] Nenhuma Home conflita com outra superfície ou participante.

### Governança

- [ ] A validação precede a auditoria aplicável.
- [ ] A auditoria precede a baseline.
- [ ] Nenhuma hipótese foi promovida implicitamente à Canon.
- [ ] Atualizações de navegação, registries e contagens estão reconciliadas.

## 12. Resultado

A auditoria produz um relatório específico da revisão com um dos estados:

| Resultado | Significado |
|---|---|
| PASS | Nenhuma não conformidade Critical ou Major aberta |
| PASS WITH MINOR FINDINGS | Apenas desvios Minor ou Observations registrados |
| FAIL | Existe não conformidade Critical ou Major aberta |

Para uma auditoria integral do GKR, `PASS` exige também:

- nenhuma autoridade atual depender de documento que será removido;
- nenhuma Home possuir conflito material conhecido;
- nenhuma família crítica permanecer fragmentada de forma que altere interpretação;
- MENU refletir o corpus final;
- referências e contagens estarem reconciliadas;
- semantic/mechanical validations concluídas com sucesso sobre o mesmo head final.

## 13. Saída mínima do relatório

```text
Audit target: <review/corpus>
Baseline SHA: <sha>
Evidence set: <artefatos>
Critical findings: <n>
Major findings: <n>
Minor findings: <n>
Observations: <n>
Documents kept: <n>
Documents updated: <n>
Documents consolidated: <n>
Documents removed: <n>
Homes current: <n>
Homes updated/rebuilt: <n>
Menu reconciled: YES | NO
Result: PASS | PASS WITH MINOR FINDINGS | FAIL
Baseline authorization: YES | NO
```

## 14. Regra de baseline

Uma baseline somente pode ser congelada quando:

1. a validação aplicável estiver aprovada;
2. a auditoria resultar em `PASS` ou `PASS WITH MINOR FINDINGS`;
3. não houver achado Critical ou Major aberto;
4. riscos residuais estiverem documentados;
5. os controles do repositório estiverem atualizados;
6. o corpus não depender de histórico obsoleto para expressar a verdade vigente;
7. a navegação refletir a autoridade final;
8. referências e contagens estiverem coerentes com os arquivos físicos remanescentes.

## 15. Regra de encerramento de auditorias temporárias

Relatórios, checklists e registros de execução criados exclusivamente para conduzir uma auditoria podem permanecer no `main` enquanto a auditoria estiver aberta.

Após o fechamento:

```text
RESULTADOS VIGENTES
→ absorvidos por autoridades / estado atual / roadmap / navegação

EVIDÊNCIAS NECESSÁRIAS
→ permanecem quando sustentam claims ou gates vigentes

REGISTRO TEMPORÁRIO DA AUDITORIA
→ removível do corpus atual
→ preservado pelo Git
```

O GKR final não deve transformar seu próprio processo de manutenção em uma camada histórica permanente de navegação.

## 16. Governança do framework

Este framework é transversal e reutilizável. Ele não deve ser duplicado por arquitetura.

Alterações exigem limitação objetiva demonstrada em aplicação prática e registro formal de decisão. A revisão `v2.0.0` incorpora uma limitação observada na evolução real do GKR: marcar documentos como históricos ou superseded, sem absorção e remoção posteriores, permite que o corpus atual acumule versões concorrentes, navegação cronológica e fragmentação de autoridade.

A solução normativa passa a ser:

> **rastreabilidade histórica no Git; conhecimento atual consolidado no GKR.**
