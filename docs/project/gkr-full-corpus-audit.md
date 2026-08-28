---
id: GKR-FULL-CORPUS-AUDIT-001
title: Auditoria Integral do Guivos Knowledge Repository
status: active
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-27
normative: false
maturity: audit_in_progress
baseline_sha: a05a54071414086456877ee4d0de59c59eefed0a
---

# Auditoria Integral do Guivos Knowledge Repository

## 1. Finalidade

Controlar a auditoria integral do Guivos Knowledge Repository iniciada após a expansão recente da Fundação, Marca, Produtos, Experience Architecture, Research, Organizações e Coletivos, Go-to-Market e demais autoridades.

A auditoria existe para responder, de forma demonstrável:

1. o GKR contém apenas a verdade vigente necessária?
2. documentos antigos ainda expressam decisões superadas?
3. documentos substituídos continuam fisicamente no corpus sem função atual?
4. conhecimento relacionado está excessivamente fragmentado?
5. consolidações anteriores perderam detalhes materiais?
6. decisões recentes foram propagadas para todas as autoridades afetadas?
7. o MENU permite uso eficiente por diferentes equipes?
8. todas as Homes continuam coerentes com o estado atual da Guivos?
9. registries, catálogos, diagramas, fluxos, exemplos e contagens refletem os artefatos realmente vigentes?
10. o corpus está suficientemente íntegro para servir de baseline antes de avançar para a primeira tela autenticada da Pessoa após a Home?

## 2. Regra desta auditoria

```text
GIT
→ histórico completo

GKR VIGENTE
→ verdade atual
→ detalhe máximo material
→ autoridade clara
→ navegação simples
→ nenhuma dependência de cronologia histórica
```

Esta auditoria não pretende apagar conhecimento.

Ela pretende remover **versões sem função atual** depois que todo conteúdo ainda válido estiver absorvido na autoridade correta.

```text
LIMPEZA
≠ PERDA DE CONHECIMENTO

CONSOLIDAÇÃO
≠ RESUMO

EXCLUSÃO DO MAIN
≠ EXCLUSÃO DO HISTÓRICO GIT
```

## 3. Baseline inicial

A auditoria foi aberta contra:

```text
repository
→ guivos-repositorio/Guivos-Knowledge-Repository

main
→ a05a54071414086456877ee4d0de59c59eefed0a

última autoridade integrada antes da auditoria
→ PR #338
→ Arquitetura da Informação autenticada de Organizações e Coletivos
```

Existe uma branch pré-auditoria não canônica:

```text
agent/gkr-orgcol-authenticated-surface-map-v1
→ commit 15c8e39941fcdb00de1b462b987054e8a6c6c18a
→ NÃO VALIDADA
→ NÃO MESCLADA
→ NÃO É AUTORIDADE
```

Ela permanece congelada até que a auditoria determine se o mapa lógico proposto ainda é compatível com o corpus limpo.

## 4. Escopo integral

A auditoria cobre, no mínimo:

### 4.1 Governança do conhecimento

- framework de auditoria;
- pipeline de consolidação;
- regras de autoridade;
- estados documentais;
- política de histórico;
- critérios de remoção;
- rastreabilidade;
- mecanismos de baseline.

### 4.2 Estado global

- Estado Atual;
- Roadmap;
- reconciliações globais;
- propagations;
- checkpoints;
- snapshots;
- registros de integração;
- claims de maturidade global.

### 4.3 Fundação, marca e identidade pública

- Fundação;
- essência, propósito, missão e visão;
- Fundamento Cristão;
- sistema verbal;
- assinatura institucional;
- assinatura pessoal do fundador;
- autoridade pública da Guivos;
- autoridade pública do fundador;
- naming;
- proteção marcária;
- claims públicos.

### 4.4 Participantes e Experience Architecture

- Pessoa;
- Organização;
- Coletivo;
- relações entre participantes;
- Domínios de Evolução;
- jornadas;
- superfícies;
- transições;
- registries;
- catálogos;
- galerias;
- materializações;
- validações;
- gaps.

### 4.5 Produtos e ecossistema

- Journey;
- Mall;
- Travel;
- Business;
- Media;
- Intelligence;
- Ads;
- relações entre Produtos Especializados e participantes.

### 4.6 Economia

- planos;
- preços quando governados;
- pontos;
- capacidade;
- entitlements;
- cobrança;
- Opportunity Boost;
- monetização;
- limites de relevância e neutralidade econômica.

### 4.7 Research e Validation

- VAL;
- RP-002;
- Field Kit;
- PMF;
- supply;
- Evidence Guivos;
- metodologia;
- stack privacy-first;
- registros intermediários;
- evidências que precisam permanecer.

### 4.8 Dados, tecnologia e IA

- GEA;
- Product Engineering;
- Neo4j;
- Grafo Global;
- Guivos Intelligence;
- GraphRAG;
- modelos de IA;
- API;
- dados;
- analytics;
- Power BI;
- privacidade por arquitetura.

### 4.9 Jurídico, privacidade e institucional

- P5/P6 e derivados;
- controlador;
- direitos;
- privacy channels;
- notices;
- retenção;
- Fundação Guivos;
- internacionalização;
- gates jurídicos e operacionais.

### 4.10 Go-to-Market e presença pública

- GTM;
- Instagram Guivos;
- Instagram do Fundador;
- comunicação institucional;
- comunicação pessoal;
- Public Canon;
- fronteiras entre marketing, publicidade, conteúdo e produto.

### 4.11 MENU e navegação

- `mkdocs.yml`;
- estrutura por domínio;
- rotas por equipe;
- duplicações de entrada;
- documentos sem rota útil;
- documentos históricos em menu;
- nomenclatura editorial.

### 4.12 Homes

- Home principal / Pessoa;
- Home Organizações e Coletivos;
- Home Mall;
- Home Travel;
- Home Media;
- Home Ads;
- Home Business;
- Home Intelligence.

## 5. Escala de ação

Cada artefato auditado recebe uma das ações:

| Ação | Interpretação nesta auditoria |
|---|---|
| `KEEP` | autoridade/conteúdo atual e necessário |
| `UPDATE` | necessário, mas defasado |
| `CONSOLIDATE` | conteúdo deve ser integrado em autoridade mais adequada |
| `REBUILD` | estrutura perdeu coerência; reconstruir preservando conteúdo válido |
| `REMOVE_AFTER_ABSORPTION` | remover depois de absorver conteúdo único válido |
| `REMOVE` | remover porque já não possui função atual |
| `EVIDENCE_KEEP` | manter como suporte probatório vigente |
| `HOLD_REVIEW` | ainda não há análise suficiente |

## 6. Achados confirmados — abertura da auditoria

### F-001 — Regra de histórico do corpus conflita com a necessidade atual

**Classe:** Major  
**Estado:** correção em andamento  
**Ação:** `UPDATE`

O GKR vinha preservando documentos e artefatos históricos/superseded dentro do próprio corpus para rastreabilidade.

A evolução do repositório mostrou que essa prática cria:

- versões concorrentes;
- navegação cronológica;
- dependência de reconciliações posteriores;
- contagens físicas que deixam de representar maturidade;
- risco de equipes utilizarem material sem autoridade.

Nova regra normativa proposta nesta auditoria:

> **Git preserva história; GKR vigente preserva verdade atual.**

Arquivos afetados inicialmente:

- `architectural-audit-framework.md`;
- `architectural-knowledge-consolidation-pipeline.md`.

### F-002 — MENU contém arquitetura histórica de construção

**Classe:** Major  
**Estado:** aberto  
**Ação:** `REBUILD`

O `mkdocs.yml` contém, entre outras evidências:

- seção `Histórico de Construção das Jornadas Integradas`;
- múltiplas entradas organizadas por sequência de UXAs;
- comentário declarando preservação de documentos técnicos e históricos no corpus;
- alta granularidade de processo de construção.

Isso é incompatível com o uso pretendido do GKR como base de conhecimento para equipes diversas.

O MENU final deverá permitir leitura por:

- domínio;
- participante;
- produto;
- responsabilidade;
- necessidade de trabalho;
- rota por equipe quando útil.

Ele não deve exigir conhecer:

- ordem de PRs;
- número de rodada;
- história de construção;
- IDs superseded.

### F-003 — Home principal / Pessoa conflita com autoridade verbal atual

**Classe:** Critical  
**Estado:** aberto  
**Ação:** `REBUILD`

O Documento Mestre atual da Home principal ainda contém `Do possível ao vivido.` como assinatura complementar institucional e utiliza `Do Possível ao Vivido` no Movimento 06.

As autoridades posteriores estabelecem:

```text
GUIVOS
→ Possibility, lived.
→ Possibilidade, vivida.
→ #PossibilityLived

FUNDADOR
→ Do possível ao vivido.
→ assinatura pessoal/autoral
→ não é assinatura institucional da Guivos
```

O Movimento 06 vigente foi reconciliado como:

```text
Da Possibilidade à Experiência
```

preservando a função:

```text
POSSIBILIDADE
→ ESCOLHA
→ EXPERIÊNCIA
→ NOVO CONTEXTO
```

Consequência:

> a Home principal não pode ser tratada como baseline consistente até ser reconstruída contra as autoridades atuais.

### F-004 — Home de Organizações e Coletivos antecede mudanças estruturais relevantes

**Classe:** Major  
**Estado:** aberto  
**Ação:** `REBUILD`

O Documento Mestre da Home pública de Organizações e Coletivos antecede:

- aprofundamentos do RP-002;
- reconciliação do estado real de Organização/Coletivo;
- definição mais recente de atores, autoridades e jobs;
- Arquitetura da Informação autenticada;
- atualizações de marca e autoridade pública;
- consolidação dos nove Domínios de Evolução.

A Home deve ser confrontada integralmente com essas autoridades antes de permanecer como master.

### F-005 — Demais Homes precisam de revalidação sistemática

**Classe:** Major  
**Estado:** aberto  
**Ação:** `HOLD_REVIEW`

Homes a auditar:

| Home | Estado inicial da auditoria |
|---|---|
| Mall | `HOLD_REVIEW` |
| Travel | `HOLD_REVIEW` |
| Media | `HOLD_REVIEW` |
| Ads | `HOLD_REVIEW` |
| Business | `HOLD_REVIEW` |
| Intelligence | `HOLD_REVIEW` |

A data antiga não prova conflito. Cada documento será comparado semanticamente com autoridades posteriores antes de decidir `KEEP`, `UPDATE` ou `REBUILD`.

### F-006 — Artefatos superseded ainda existem fisicamente

**Classe:** Major  
**Estado:** aberto  
**Ação:** `REMOVE_AFTER_ABSORPTION`

Exemplos confirmados:

- `UXA-015`;
- `UXA-016`;
- `UXA-017`;
- `UXA-018`;
- SVG histórico da antiga Visão Geral da Organização;
- SVG histórico do antigo Início do Coletivo.

O estado atual já declara esses objetos como superseded para a UX principal autenticada.

Antes de removê-los será necessário:

1. extrair qualquer semântica ainda válida;
2. verificar se ela já está em `UXA-014`, jornadas atuais, estado O/C, atores/jobs ou IA;
3. atualizar links e dependências;
4. atualizar catálogo, gallery, registry, traceability e contagens;
5. executar validação;
6. então remover arquivos físicos.

### F-007 — Contagens físicas não representam mais maturidade vigente

**Classe:** Major  
**Estado:** aberto  
**Ação:** `UPDATE`

O catálogo ainda preserva `121 SVGs físicos` e explica que a antiga claim `121 validados / 0 pendentes` está superseded.

Depois da limpeza física, todas as contagens deverão ser recomputadas a partir do corpus remanescente.

Nenhuma nova contagem será inferida antes da remoção controlada.

### F-008 — Estado Atual e Roadmap dependem de reconciliação posterior

**Classe:** Major  
**Estado:** aberto  
**Ação:** `UPDATE + CONSOLIDATE`

Existe uma reconciliação global posterior criada para suplementar versões anteriores de Estado Atual e Roadmap.

Pela nova regra, a solução final não deve ser manter permanentemente:

```text
ESTADO ANTIGO
+ ROADMAP ANTIGO
+ ADENDO DE RECONCILIAÇÃO
```

O conteúdo válido do adendo deve ser absorvido nas autoridades globais atualizadas; depois, o adendo deve ser removido se não restar função própria.

### F-009 — Recentes autoridades O/C ainda não estão integradas à navegação final

**Classe:** Major  
**Estado:** aberto  
**Ação:** `UPDATE`

Autoridades recentes:

- atores, autoridades e jobs da experiência autenticada;
- Arquitetura da Informação autenticada.

Elas são canônicas, porém o MENU ainda não passou por reconciliação global posterior a essas integrações.

### F-010 — Fragmentação por checkpoints, snapshots, propagations e reconciliações precisa ser auditada

**Classe:** Major  
**Estado:** aberto  
**Ação:** `HOLD_REVIEW → CONSOLIDATE/REMOVE_AFTER_ABSORPTION` quando comprovado

Famílias candidatas incluem:

- checkpoints de continuidade;
- snapshots de Design/Homes;
- propagation records;
- addenda globais;
- reconciliações temáticas já absorvíveis;
- registros intermediários de Research;
- decisões procedimentais que perderam função depois de uma autoridade posterior.

Nenhum arquivo desta família será excluído apenas pelo nome. Cada um será testado por conteúdo único e função atual.

### F-011 — Consolidação não pode repetir a perda de detalhe observada em revisões anteriores

**Classe:** Critical guardrail  
**Estado:** regra ativa  
**Ação:** `KEEP_DETAIL`

A auditoria considera falha qualquer consolidação que torne o corpus aparentemente menor, porém remova conhecimento atual necessário.

Obrigatório preservar, quando material:

- diagramas;
- exemplos;
- contraexemplos;
- fluxos ponta a ponta;
- estados alternativos;
- critérios de aceite;
- critérios de bloqueio;
- responsabilidades;
- limites de autoridade;
- guardrails;
- métricas e thresholds;
- distinções semânticas;
- evidências e limitações.

### F-012 — Primeira tela pós-Home da Pessoa permanece bloqueada pela auditoria

**Classe:** Gate  
**Estado:** BLOCKED  
**Ação:** nenhuma materialização antes do fechamento

Não iniciar:

- definição final da primeira tela;
- novo wireframe;
- nova UXA numerada;
- UI;
- protótipo;
- Product Engineering.

A tela só poderá ser escrita depois de:

1. corpus auditado;
2. Home principal reconciliada;
3. fluxo da Pessoa reavaliado;
4. material histórico removido/reclassificado;
5. registries atualizados;
6. MENU final reconciliado;
7. auditoria final sem Critical/Major aberto relacionado ao fluxo.

## 7. Matriz de trabalho

| Frente | Estado | Resultado esperado |
|---|---|---|
| A — Governança do corpus | IN_PROGRESS | regra de verdade vigente + pipeline de remoção |
| B — Estado Atual e Roadmap | PENDING | autoridades globais atualizadas e sem addendum dependente |
| C — Fundação / Marca / Public Canon | PENDING | autoridade sem contradição e propagations absorvidas |
| D — Home principal / Pessoa | FINDING_CONFIRMED | master reconstruído |
| E — Home Organizações e Coletivos | FINDING_CONFIRMED | master reconstruído |
| F — Homes de Produtos | PENDING | classificação + correções necessárias |
| G — Jornada da Pessoa | PENDING | fluxo vigente consolidado antes da próxima tela |
| H — Organização / Coletivo | PENDING | recentes autoridades integradas e históricos removidos |
| I — Registries / Catálogos / SVGs | PENDING | inventário físico e maturidade recomputados |
| J — Produtos / Economia | PENDING | masters atuais sem fragmentação |
| K — Research / RP-002 | PENDING | método/evidência preservados; intermediários absorvidos quando possível |
| L — Tecnologia / Dados / IA | PENDING | autoridades atuais e fronteiras claras |
| M — Jurídico / Privacidade / Institucional | PENDING | estado documental e operacional corretamente separados |
| N — GTM / presença pública | PENDING | GTM atual e sem duplicações históricas |
| O — MENU / rotas por equipe | PENDING | navegação final multiequipe |
| P — Auditoria final de completude | PENDING | PASS ou PASS WITH MINOR FINDINGS |
| Q — primeira tela pós-Home Pessoa | BLOCKED | somente depois de P |

## 8. Ordem de execução

A ordem é deliberadamente estrutural:

```text
A. governança da verdade vigente
↓
B. autoridades globais
↓
C. autoridades transversais
↓
D/E/F. Homes
↓
G/H/I. Experience Architecture e inventário visual
↓
J/K/L/M/N. domínios especializados
↓
O. MENU final
↓
P. auditoria final
↓
Q. primeira tela da Pessoa
```

O MENU é redesenhado perto do final porque sua estrutura deve refletir **o corpus que restou depois da consolidação**, não o inventário antigo.

## 9. Critérios para eliminar um documento

Um documento pode sair do corpus atual quando todos os critérios aplicáveis forem verdadeiros:

- não é a autoridade vigente;
- não contém evidência necessária ainda única;
- todo conteúdo válido foi absorvido;
- seus exemplos/diagramas úteis foram preservados quando necessários;
- referências foram corrigidas;
- registries/contagens foram atualizados;
- não existe consumidor atual que dependa dele;
- a validação aplicável confirma corpus íntegro sem o arquivo.

## 10. Critérios para consolidar documentos

Uma consolidação é aceita quando:

```text
MENOS FRAGMENTAÇÃO
+ MESMA OU MAIOR CLAREZA
+ MESMO OU MAIOR DETALHE MATERIAL
+ AUTORIDADE MAIS CLARA
+ REFERÊNCIAS MAIS SIMPLES
```

É rejeitada quando produz:

- resumo genérico;
- perda de fluxos;
- perda de critérios;
- perda de exemplos úteis;
- apagamento de guardrails;
- ocultação de divergências reais;
- mistura de autoridade normativa com Research;
- mistura de visão com implementação.

## 11. Requisitos da navegação final

O desenho final deverá permitir que pelo menos estas funções encontrem conhecimento sem reconstruir a história do projeto:

- liderança / estratégia;
- marketing;
- publicidade / Ads;
- comercial;
- produto;
- UX / Experience Architecture;
- Design;
- desenvolvimento / Product Engineering;
- dados / Intelligence;
- Research;
- jurídico / privacidade;
- internacionalização / operação.

Princípio:

> **uma autoridade pode servir várias equipes; não criar cópias por equipe.**

## 12. Requisitos da auditoria das Homes

Cada Home será lida como uma promessa pública implícita sobre:

- quem é a Guivos;
- para quem existe;
- o que torna possível;
- como se relaciona com o ecossistema;
- quais claims pode sustentar;
- qual próximo movimento oferece.

A auditoria verificará:

1. alinhamento à Fundação;
2. assinatura e linguagem de marca;
3. separação Guivos × fundador;
4. papel do participante;
5. papel do Produto Especializado;
6. taxonomias atuais;
7. relação com Journey;
8. neutralidade econômica;
9. limites de privacy/Intelligence;
10. coerência entre Home pública e experiência autenticada;
11. ausência de promessa operacional não comprovada;
12. coerência com demais Homes.

## 13. Estado inicial das Homes

| Home | Estado nesta abertura | Motivo |
|---|---|---|
| Principal / Pessoa | `REBUILD_REQUIRED` | conflito material já confirmado com assinatura/Movimento 06 vigentes |
| Organizações e Coletivos | `REBUILD_REQUIRED` | antecede mudanças estruturais posteriores |
| Mall | `AUDIT_PENDING` | requer confronto com GPA-002/economia atual |
| Travel | `AUDIT_PENDING` | requer confronto com GPA-003 e arquitetura atual |
| Media | `AUDIT_PENDING` | requer confronto com GPA-005 e papel editorial atual |
| Ads | `AUDIT_PENDING` | requer confronto com GPA-007, neutralidade e supply atual |
| Business | `AUDIT_PENDING` | requer confronto com GPA-004, Organização ≠ Business e Intelligence atual |
| Intelligence | `AUDIT_PENDING` | requer confronto com GPA-006 v2.0.0 e privacy architecture atual |

Nenhuma Home pendente será declarada inconsistente apenas por data; o resultado virá da comparação de conteúdo.

## 14. Preservações obrigatórias durante a auditoria

A auditoria não pode promover ou apagar, por conveniência, estados como:

```text
PMF
→ NOT VALIDATED

RP-002 CONCEPTUAL READINESS
→ PASS

RP-002 METHODOLOGICAL READINESS
→ PASS

FIELD KIT
→ FROZEN FOR FIRST DRY RUN

OPERATIONAL IMPLEMENTATION
→ DEFERRED

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED

UXA-102 / V5
→ NOT_STARTED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01
```

Esses estados somente mudam por autoridade/evidência própria.

## 15. Gate para fechamento

A auditoria somente pode encerrar quando:

- [ ] todas as famílias documentais forem classificadas;
- [ ] autoridades globais estiverem atualizadas;
- [ ] contradições conhecidas forem resolvidas;
- [ ] conteúdo válido de artefatos substituídos estiver absorvido;
- [ ] artefatos sem função atual estiverem removidos;
- [ ] referências e links estiverem reconciliados;
- [ ] contagens físicas e de maturidade tiverem sido recomputadas;
- [ ] todas as Homes tiverem resultado final e correção quando necessária;
- [ ] fluxo vigente da Pessoa estiver reconciliado;
- [ ] fluxo vigente de Organização e Coletivo estiver reconciliado;
- [ ] produtos e autoridades especializadas estiverem sem fragmentação material aberta;
- [ ] MENU estiver reorganizado para uso multiequipe;
- [ ] não houver seção histórica necessária para entender o estado atual;
- [ ] validação semântica final tiver sucesso;
- [ ] validação mecânica final tiver sucesso;
- [ ] não houver achado Critical ou Major aberto.

## 16. Estado atual da auditoria

```text
AUDIT
→ IN_PROGRESS

BASELINE FINAL
→ NOT AUTHORIZED

CORPUS CLEANUP
→ NOT YET COMPLETE

HOME PRINCIPAL
→ REBUILD_REQUIRED

HOME ORGANIZAÇÕES E COLETIVOS
→ REBUILD_REQUIRED

DEMAIS HOMES
→ AUDIT_PENDING

MENU FINAL
→ NOT YET DESIGNED

FIRST PERSON SCREEN AFTER HOME
→ BLOCKED UNTIL AUDIT CLOSES
```

## 17. Destino deste registro

Este arquivo é um instrumento temporário de execução e controle.

Quando a auditoria fechar:

1. o estado vigente será absorvido por Estado Atual, Roadmap, autoridades temáticas, registries e MENU;
2. evidências necessárias permanecerão em suas famílias próprias;
3. este registro poderá ser removido do corpus atual;
4. seu histórico continuará preservado no Git.
