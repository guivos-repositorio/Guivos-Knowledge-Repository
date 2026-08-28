---
id: GKR-FULL-CORPUS-AUDIT-001
title: Auditoria Integral do Guivos Knowledge Repository
status: active
version: 1.0.1
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-27
normative: false
maturity: audit_in_progress
baseline_sha: a05a54071414086456877ee4d0de59c59eefed0a
---

# Auditoria Integral do Guivos Knowledge Repository

## 1. Finalidade

Controlar a auditoria integral do Guivos Knowledge Repository após a expansão recente de Fundação, Marca, Produtos, Experience Architecture, Research, Organizações e Coletivos, Go-to-Market e demais autoridades.

A auditoria deve provar se:

1. o GKR contém apenas a verdade vigente necessária;
2. documentos antigos ainda expressam decisões superadas;
3. documentos substituídos continuam fisicamente no corpus sem função atual;
4. conhecimento relacionado está excessivamente fragmentado;
5. consolidações anteriores perderam detalhes materiais;
6. decisões recentes foram propagadas para todas as autoridades afetadas;
7. o MENU permite uso eficiente por diferentes equipes;
8. todas as Homes continuam coerentes com o estado atual da Guivos;
9. registries, catálogos, diagramas, fluxos, exemplos e contagens refletem os artefatos realmente vigentes;
10. o corpus está íntegro o suficiente para servir de baseline antes da primeira tela autenticada da Pessoa após a Home.

## 2. Regra central

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

Esta auditoria não pretende apagar conhecimento. Ela remove **versões sem função atual** somente depois que todo conteúdo ainda válido estiver absorvido na autoridade correta.

```text
LIMPEZA
≠ PERDA DE CONHECIMENTO

CONSOLIDAÇÃO
≠ RESUMO

EXCLUSÃO DO MAIN
≠ EXCLUSÃO DO HISTÓRICO GIT
```

## 3. Baseline inicial

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

Ela permanece congelada até que a auditoria determine se o mapa lógico proposto continua compatível com o corpus limpo.

## 4. Escopo integral

A auditoria cobre:

- governança do conhecimento;
- Estado Atual e Roadmap;
- Fundação, Fundamento Cristão, Marca e Public Canon;
- Pessoa, Organização e Coletivo;
- Journey e Experience Architecture;
- Mall, Travel, Business, Media, Intelligence e Ads;
- planos, pontos, incentivos, capacidade e economia;
- Research, VAL, RP-002, Field Kit e PMF;
- tecnologia, dados, Grafo, Neo4j, IA e analytics;
- jurídico, privacidade, institucional e internacionalização;
- GTM, Instagram Guivos e Instagram do Fundador;
- registries, catálogos, galleries, matrizes, SVGs e contagens;
- `mkdocs.yml` e navegação;
- todas as Homes públicas.

## 5. Ações documentais

| Ação | Significado |
|---|---|
| `KEEP` | autoridade/conteúdo atual e necessário |
| `UPDATE` | necessário, mas defasado |
| `CONSOLIDATE` | conteúdo deve ser integrado em autoridade mais adequada |
| `REBUILD` | estrutura perdeu coerência; reconstruir preservando conteúdo válido |
| `REMOVE_AFTER_ABSORPTION` | remover depois de absorver conteúdo único válido |
| `REMOVE` | remover porque já não possui função atual |
| `EVIDENCE_KEEP` | manter como suporte probatório vigente |
| `HOLD_REVIEW` | análise ainda insuficiente |

Nenhuma remoção é executada antes de verificar conteúdo único, evidência e referências.

## 6. Achados confirmados

| ID | Classe | Achado | Ação | Estado |
|---|---|---|---|---|
| F-001 | Major | política anterior mantinha histórico/superseded no corpus | `UPDATE` | correção em andamento |
| F-002 | Major | MENU contém arquitetura histórica de construção e alta fragmentação | `REBUILD` | aberto |
| F-003 | Critical | Home principal/Pessoa conflita com assinatura e Movimento 06 vigentes | `REBUILD` | aberto |
| F-004 | Major | Home O/C antecede mudanças estruturais posteriores | `REBUILD` | aberto |
| F-005 | Major | Mall, Travel, Media, Ads, Business e Intelligence precisam de auditoria semântica | `HOLD_REVIEW` | aberto |
| F-006 | Major | UXA-015..018 e SVGs associados continuam fisicamente embora superseded | `REMOVE_AFTER_ABSORPTION` | aberto |
| F-007 | Major | contagens físicas de SVGs não representam maturidade vigente | `UPDATE` | aberto |
| F-008 | Major | Estado Atual e Roadmap dependem de reconciliação posterior | `UPDATE + CONSOLIDATE` | aberto |
| F-009 | Major | autoridades O/C de atores/jobs e IA ainda não foram absorvidas nas autoridades globais/menu final | `UPDATE` | aberto |
| F-010 | Major | checkpoints, snapshots, propagations e reconciliações precisam de teste de função atual | `HOLD_REVIEW` | aberto |
| F-011 | Critical guardrail | nenhuma consolidação pode perder detalhe material | `KEEP_DETAIL` | regra ativa |
| F-012 | Gate | primeira tela pós-Home da Pessoa depende do encerramento da auditoria | `BLOCK` | ativo |

## 7. F-003 — conflito material da Home principal

O Documento Mestre atual da Home principal ainda usa `Do possível ao vivido.` como assinatura complementar institucional e utiliza `Do Possível ao Vivido` no Movimento 06.

Autoridades posteriores estabelecem:

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

O rótulo vigente do Movimento 06 é:

```text
Da Possibilidade à Experiência
```

A função permanece:

```text
POSSIBILIDADE
→ ESCOLHA
→ EXPERIÊNCIA
→ NOVO CONTEXTO
```

Conclusão provisória já comprovada:

> **Home principal/Pessoa = REBUILD_REQUIRED.**

## 8. F-004 — Home de Organizações e Coletivos

O Documento Mestre vigente antecede, entre outros:

- RP-002;
- reconciliação do estado real de Organização/Coletivo;
- atores, autoridades e jobs autenticados;
- Arquitetura da Informação autenticada;
- atualizações de marca e autoridade pública;
- consolidação dos nove Domínios de Evolução.

Conclusão provisória já comprovada:

> **Home Organizações e Coletivos = REBUILD_REQUIRED.**

## 9. F-005 — demais Homes

| Home | Estado de auditoria |
|---|---|
| Mall | `AUDIT_PENDING` |
| Travel | `AUDIT_PENDING` |
| Media | `AUDIT_PENDING` |
| Ads | `AUDIT_PENDING` |
| Business | `AUDIT_PENDING` |
| Intelligence | `AUDIT_PENDING` |

Data antiga não prova conflito. Cada Home será comparada com autoridades posteriores antes de receber `KEEP`, `UPDATE` ou `REBUILD`.

## 10. F-006/F-007 — artefatos e contagens históricas

Exemplos já confirmados de artefatos sem autoridade visual vigente:

- `UXA-015`;
- `UXA-016`;
- `UXA-017`;
- `UXA-018`;
- SVG da antiga Visão Geral da Organização;
- SVG do antigo Início do Coletivo.

Antes de removê-los:

1. extrair semântica ainda válida;
2. confirmar absorção em autoridades atuais;
3. corrigir links e dependências;
4. atualizar catálogo, gallery, registry e traceability;
5. recomputar contagens;
6. validar o corpus;
7. remover os arquivos físicos.

Nenhuma nova contagem agregada será inferida antes dessa limpeza.

## 11. F-008 — Estado Atual e Roadmap

Existe uma reconciliação global posterior criada para suplementar versões anteriores de Estado Atual e Roadmap.

A auditoria não aceitará como solução final:

```text
ESTADO ANTIGO
+ ROADMAP ANTIGO
+ ADENDO DE RECONCILIAÇÃO
```

O conteúdo válido do adendo deve ser absorvido nas autoridades globais atualizadas. Depois, o adendo deve ser removido se não possuir função própria.

Achados adicionais já confirmados:

- `GKR-STATE-001 v2.44.0` não contém RP-002;
- `GKR-STATE-001 v2.44.0` não contém GTM-009;
- `GKR-STATE-001 v2.44.0` não contém as autoridades de atores/jobs e IA autenticada de O/C;
- `ROADMAP-12.84.0` não contém RP-002;
- `ROADMAP-12.84.0` ainda registra `121 validados / 0 pendentes`, claim já considerada não inferível no Estado Atual posterior.

Portanto:

> **Estado Atual e Roadmap exigem reescrita integral controlada, não novo adendo.**

## 12. F-010 — famílias candidatas a consolidação

Devem ser auditados individualmente, sem exclusão por nome:

- checkpoints de continuidade;
- snapshots de Design/Homes;
- propagation records;
- addenda globais;
- reconciliações temáticas já absorvíveis;
- registros intermediários de Research;
- decisões procedimentais que perderam função após autoridade posterior.

Teste obrigatório para cada arquivo:

```text
CONTEÚDO ÚNICO ATUAL?
EVIDÊNCIA AINDA NECESSÁRIA?
AUTORIDADE PRÓPRIA?
DEPENDÊNCIAS ATUAIS?
```

Somente depois desse teste definir `KEEP`, `CONSOLIDATE`, `REMOVE_AFTER_ABSORPTION` ou `REMOVE`.

## 13. Guardrail de detalhe

A auditoria falha se uma consolidação reduzir a quantidade de arquivos às custas de conhecimento atual necessário.

Preservar quando material:

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
- evidências;
- limitações e incertezas.

```text
CONSOLIDAR
≠ RESUMIR
```

## 14. Matriz de trabalho

| Frente | Estado | Resultado esperado |
|---|---|---|
| A — Governança do corpus | `IN_PROGRESS` | regra de verdade vigente + pipeline de remoção |
| B — Estado Atual e Roadmap | `FINDINGS_CONFIRMED` | autoridades globais atualizadas sem addendum dependente |
| C — Fundação / Marca / Public Canon | `PENDING` | autoridade sem contradição e propagations absorvidas |
| D — Home principal / Pessoa | `REBUILD_REQUIRED` | master reconstruído |
| E — Home Organizações e Coletivos | `REBUILD_REQUIRED` | master reconstruído |
| F — Homes de Produtos | `PENDING` | classificação e correções |
| G — Jornada da Pessoa | `PENDING` | fluxo vigente consolidado antes da próxima tela |
| H — Organização / Coletivo | `PENDING` | recentes autoridades integradas e históricos removidos |
| I — Registries / Catálogos / SVGs | `PENDING` | inventário e maturidade recomputados |
| J — Produtos / Economia | `PENDING` | masters atuais sem fragmentação |
| K — Research / RP-002 | `PENDING` | método/evidência preservados; intermediários absorvidos quando possível |
| L — Tecnologia / Dados / IA | `PENDING` | autoridades atuais e fronteiras claras |
| M — Jurídico / Privacidade / Institucional | `PENDING` | documental e operacional separados corretamente |
| N — GTM / presença pública | `PENDING` | autoridades atuais sem duplicação histórica |
| O — MENU / rotas por equipe | `PENDING` | navegação final multiequipe |
| P — Auditoria final | `PENDING` | `PASS` ou `PASS WITH MINOR FINDINGS` |
| Q — primeira tela pós-Home Pessoa | `BLOCKED` | somente depois de P |

## 15. Ordem de execução

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

O MENU é redesenhado perto do final porque deve refletir o corpus que restar depois da consolidação.

## 16. Requisitos da navegação final

A navegação deve permitir acesso eficiente para:

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

## 17. Requisitos da auditoria das Homes

Cada Home será confrontada com:

1. Fundação e Propósito vigentes;
2. assinatura e linguagem de marca;
3. separação Guivos × fundador;
4. papel do participante;
5. Produto Especializado correspondente;
6. taxonomias atuais;
7. relação com Journey;
8. neutralidade econômica;
9. privacy/Intelligence;
10. experiência autenticada relacionada;
11. evidência necessária para claims;
12. demais Homes para evitar sobreposição de autoridade.

Resultados permitidos:

```text
CURRENT
| UPDATE_REQUIRED
| REBUILD_REQUIRED
```

## 18. Preservações obrigatórias

A auditoria não muda por conveniência:

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

Esses estados mudam somente por autoridade/evidência própria.

## 19. Gate para a primeira tela da Pessoa

Não iniciar:

- definição final da primeira tela;
- novo wireframe;
- nova UXA numerada;
- UI;
- protótipo;
- Product Engineering.

O avanço exige:

1. corpus auditado;
2. Home principal reconciliada;
3. fluxo da Pessoa reavaliado;
4. históricos removidos/reclassificados;
5. registries atualizados;
6. MENU final reconciliado;
7. auditoria final sem Critical/Major relacionado ao fluxo.

## 20. Gate de fechamento da auditoria

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

## 21. Estado atual

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

## 22. Destino deste registro

Este arquivo é temporário.

Quando a auditoria fechar:

1. o estado vigente será absorvido por Estado Atual, Roadmap, autoridades temáticas, registries e MENU;
2. evidências necessárias permanecerão em suas famílias próprias;
3. este registro poderá ser removido do corpus atual;
4. seu histórico continuará preservado no Git.
