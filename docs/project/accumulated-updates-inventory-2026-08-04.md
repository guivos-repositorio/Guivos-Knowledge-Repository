---
id: GKR-UPDATES-INVENTORY-001
title: Inventário Governado das Atualizações Acumuladas do GKR
status: draft
version: 0.1.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-04
depends_on:
  - GKR-STATE-001
  - GKR-AUD-002
  - GKR-REMEDIATION-002
  - GE2-SYNC-008
related:
  - GKR-UPDATE-PROGRAM-001
  - GEA-000
  - GPA-000
  - GBA-000
  - GEM-000
  - UXA-000
  - VAL-STATUS
  - GOG-001
normative: false
---

# Inventário Governado das Atualizações Acumuladas do GKR

## 1. Finalidade

Este documento inventaria lacunas, divergências e fontes candidatas acumuladas no Guivos Knowledge Repository após a última reconciliação geral de continuidade.

O inventário existe para responder, antes de qualquer atualização ampla:

1. quais informações já estão confirmadas na `main`;
2. quais superfícies globais estão desatualizadas em relação às autoridades vigentes;
3. quais documentos externos poderão fundamentar novos pacotes;
4. quais alegações ainda não possuem evidência suficiente;
5. quais hipóteses devem permanecer em quarentena;
6. quais autoridades serão afetadas;
7. em que ordem as atualizações deverão ocorrer.

Este documento não promove fatos, planos, tecnologias, produtos, territórios, entidades jurídicas ou operações ao estado canônico.

## 2. Autoridade e limites

A autoridade transversal vigente permanece no `GKR-STATE-001 — Registro do Estado Atual`.

Este inventário:

- não altera o marco `M7.72`;
- não atualiza versões globais;
- não redefine a Fundação, o GEB, o Journey, o Economic Model, a Business Architecture ou a Experience Architecture;
- não inicia `UXA-071`;
- não autoriza protótipo, implementação, oferta comercial, coleta de dados, expansão internacional ou constituição institucional;
- não substitui validação jurídica, técnica, econômica, de privacidade ou de mercado;
- não transforma arquivo externo em decisão arquitetural;
- não presume que um plano foi executado;
- não presume que um domínio registrado está operacional;
- não presume que uma entidade projetada foi juridicamente constituída.

## 3. Baseline e janela de análise

| Elemento | Baseline utilizada |
|---|---|
| ramo oficial | `main` |
| commit-base | `066faf5c843a04b08f400f5ff5358fa059b22e88` |
| marco vigente | `M7.72` |
| Registro do Estado Atual | `GKR-STATE-001 1.99.0` |
| último checkpoint geral localizado | `GE2-SYNC-008`, de 19/07/2026 |
| data do inventário | 04/08/2026 |

A análise considera o período entre a reconciliação geral de 19/07/2026 e o estado posterior à integração da UXA-070.

## 4. Classes de evidência

| Classe | Significado | Tratamento permitido |
|---|---|---|
| Confirmado na `main` | informação presente em autoridade ou documento integrado | pode fundamentar correção editorial e sincronização |
| Fonte externa documentada | arquivo ou material identificável, ainda fora do GKR | pode entrar em pacote de intake e avaliação |
| Relato ou intenção sem evidência suficiente | informação mencionada, mas sem documento verificável ou autoridade definida | permanece pendente de fonte |
| Hipótese em quarentena | conceito, produto, mecânica ou expansão ainda não governados | não integra arquitetura ou comunicação pública |
| Histórico ou supersedido | conteúdo válido em estado anterior | deve permanecer rastreável, sem governar o estado atual |

## 5. Parecer executivo

### 5.1 Estado canônico

O núcleo de estado vigente está atualizado no Registro do Estado Atual, Roadmap, Painel de Conhecimento, Marcos Arquiteturais e Arquitetura da Experiência após a UXA-070.

### 5.2 Drift das superfícies globais

As superfícies de entrada, publicação e consolidação não acompanharam a mesma evolução:

- `README.md` permanece no marco `M7.48`;
- `docs/index.md` permanece no marco `M7.48`;
- `CHANGELOG.md` raiz termina no incremento `0.58.0`;
- `mkdocs.yml` publica a Experience Architecture somente até a UXA-046;
- a Matriz de Consolidação Canônica central permanece em `2.17.0`, com cobertura explícita anterior aos adendos mais recentes.

O problema não é ausência das autoridades recentes. É ausência de sincronização entre essas autoridades e as superfícies globais.

### 5.3 Recorrência

O `GKR-AUD-002`, de 24/07/2026, já havia identificado drift semelhante em README, página inicial, navegação e matriz. A remediação corrigiu o estado daquele ciclo, mas a validação permanente não contém um controle semântico capaz de impedir recorrência.

### 5.4 Atualizações externas

Foram identificadas duas fontes externas documentadas com potencial de incorporação:

1. arquitetura recomendada para Neo4j, Graph Analytics e consumo executivo no Power BI;
2. plano de proteção corporativa de marca, domínios e ativos digitais.

As duas fontes representam recomendações ou planos. Nenhuma delas comprova implementação, contratação, registro, titularidade, operação, disponibilidade ou conformidade concluídas.

### 5.5 Atualizações sem evidência suficiente

Não foi localizada evidência suficiente para declarar como oficiais:

- situação operacional atual de `guivos.ai`;
- novos domínios adquiridos ou ativados;
- constituição jurídica da Fundação Guivos ou operação de `guivos.org`;
- expansão operacional para Colômbia ou outro país;
- parceiros contratados, clientes, campanhas, contas oficiais ou integrações em produção;
- política jurídica e de privacidade publicada para voz, arquivos, localização, calendário ou integrações.

## 6. Matriz de lacunas

| ID | Severidade | Achado | Classe | Autoridades ou superfícies afetadas | Tratamento proposto |
|---|---|---|---|---|---|
| GKR-GAP-001 | Major | `README.md` declara `M7.48`, enquanto o estado vigente é `M7.72` | confirmado na `main` | README; GKR-STATE-001 | sincronização global imediata |
| GKR-GAP-002 | Major | `docs/index.md` declara `M7.48` e estados antigos do Opportunity Boost | confirmado na `main` | Home documental; GKR-STATE-001 | sincronização global imediata |
| GKR-GAP-003 | Major | `CHANGELOG.md` raiz termina em `0.58.0`, enquanto existem registros temáticos até `1.94.0` | confirmado na `main` | changelog raiz; changelogs temáticos | definir política e índice de histórico |
| GKR-GAP-004 | Major | `mkdocs.yml` publica Experience Architecture somente até UXA-046 | confirmado na `main` | navegação; UXA-047 a UXA-070 | rebaseline da navegação |
| GKR-GAP-005 | Major | Matriz de Consolidação Canônica central não consolida os adendos recentes | confirmado na `main` | GKR-CANON-MATRIX-001; adendos posteriores | consolidação central controlada |
| GKR-GAP-006 | Major | validação mecânica não verifica coerência semântica entre estado, entradas, navegação e matriz | confirmado na `main` | `scripts/validate_gkr.py`; workflow | criar validação semântica separada |
| GKR-GAP-007 | Major | último checkpoint geral localizado é o GE2-SYNC-008, anterior às frentes posteriores | confirmado na `main` | GEA; estado; arquitetura; público | nova reconciliação geral após pacotes |
| GKR-GAP-008 | Major | Guia Oficial público está em `4.2.1`, de 11/07/2026, anterior às mudanças recentes de experiência e governança | confirmado na `main` | GOG-001; public/index; UXA | revisar somente após dependências jurídicas e operacionais |
| GKR-GAP-009 | Major | Arquitetura de Produtos central está em `1.30.0`, de 18/07/2026, e o próprio GEA registra rebaseline pendente | confirmado na `main` | GPA-000; produtos especializados | rebaseline posterior a evidências e capacidades |
| GKR-GAP-010 | Major | arquitetura Neo4j existe como documento externo, sem classificação no GKR | fonte externa documentada | GEA; Technology Architecture; Intelligence; Reference Architecture; ADRs | intake técnico e decisão de referência |
| GKR-GAP-011 | Major | plano de proteção de marca e domínios existe externamente, sem registro governado no GKR | fonte externa documentada | Governança; marca; ativos digitais; segurança | intake jurídico-operacional e modelo de inventário |
| GKR-GAP-012 | Major | baseline de Market Validation está em 12/07/2026; resultados ou operações posteriores não foram reconciliados | confirmado e fonte posterior pendente | VAL-STATUS; Research; Business Architecture | intake de evidências e atualização metodológica |
| GKR-GAP-013 | Major | não existe política pública canônica suficiente para voz, transcrição, arquivos, localização, calendário e integrações | ausência documental | público; privacidade; dados; tecnologia; experiência | pacote jurídico, de dados e privacidade |
| GKR-GAP-014 | Pending evidence | situação atual de `guivos.ai` não foi comprovada | evidência insuficiente | produto; domínio; público; tecnologia | solicitar fonte operacional e de titularidade |
| GKR-GAP-015 | Pending evidence | Fundação Guivos e `guivos.org` não possuem estado jurídico e operacional comprovado | evidência insuficiente | arquitetura institucional; governança; econômico; público | solicitar documentos e decisão institucional |
| GKR-GAP-016 | Pending evidence | expansão para Colômbia ou outros territórios não possui base verificável suficiente | evidência insuficiente | internacionalização; marca; jurídico; operação | intake territorial antes de qualquer anúncio |
| GKR-GAP-017 | Minor | Guivos Mall já substitui Guivos Marketplace, mas exige auditoria transversal de consistência | confirmado na `main` | Product Architecture; público; glossário; histórico | auditoria de referências, sem nova decisão |
| GKR-GAP-018 | Minor | overlays, changelogs e roadmaps históricos estão dispersos e coexistem com dois ZIPs antigos na raiz | confirmado na `main` | navegação; histórico; política de arquivo | definir política de arquivo; não excluir automaticamente |
| GKR-GAP-019 | Pending evidence | contas, campanhas, parceiros, clientes, fornecedores e integrações operacionais recentes não possuem inventário oficial | evidência insuficiente | operação; público; negócio; tecnologia | intake operacional com fontes e datas |
| GKR-GAP-020 | Quarantine | conceitos como Passport, Mapa de Vida, rankings, tribos e recompensas não constituem decisões atuais | hipótese | produto; experiência; econômico; proteção comportamental | avaliação separada antes de qualquer promoção |

## 7. Divergências e não divergências

### 7.1 Divergências confirmadas

- marco das páginas de entrada versus Registro do Estado Atual;
- alcance da navegação versus documentos integrados;
- changelog raiz versus históricos temáticos;
- matriz central versus adendos posteriores;
- validação mecânica existente versus necessidade de coerência semântica.

### 7.2 Não divergências confirmadas

- `Guivos Mall` já é o nome oficial do produto;
- `Guivos Marketplace` já está classificado como nome anterior;
- planos e preços continuam candidatos, sem oferta ou cobrança autorizadas;
- Opportunity Boost continua mecanismo candidato, sem campanha real autorizada;
- Business Outcomes continuam sem resultado canônico;
- Product Engineering continua pausada antes de `W0-01`;
- UXA-071 continua não iniciada;
- o programa de simulação não equivale a mapa, protótipo ou aplicação.

## 8. Fontes externas candidatas

### 8.1 Arquitetura Neo4j

Fonte identificada:

- título: `Guivos_Arquitetura_Neo4j.pdf`;
- versão declarada: `1.0`;
- data declarada: `23/07/2026`;
- natureza: decisão ou recomendação de arquitetura ainda não integrada.

Conteúdo candidato:

- Neo4j AuraDB Professional como núcleo relacional inicial;
- região primária recomendada em São Paulo;
- Graph Analytics em computação separada;
- Guivos Intelligence e GraphRAG;
- indicadores materializados em Lakehouse ou Warehouse para Power BI;
- implantação progressiva por evidência de valor, qualidade, custo, latência, SLA e criticidade;
- controles de IDs, LGPD, consentimento, retenção, backup, observabilidade e menor privilégio.

Classificação deste inventário:

> **Fonte de referência técnica candidata. Não comprova provisionamento, execução, contrato, custo real, produção ou escala.**

### 8.2 Proteção corporativa de marca e ativos digitais

Fonte identificada:

- título: `Plano de Execução — Fase 4: Proteção Corporativa da Marca e dos Ativos Digitais Guivos`;
- versão declarada: `1.0`;
- data declarada: `21/06/2026`;
- classificação declarada: uso interno e consultores autorizados;
- natureza: plano executivo e operacional sujeito a validação jurídica especializada.

Conteúdo candidato:

- titularidade corporativa de marcas e domínios;
- estratégia de classes e territórios;
- Sistema de Madri, TMCH e bloqueio preventivo;
- classificação de criticidade dos domínios;
- MFA, locks, DNSSEC, renovação, logs e segregação de acessos;
- política de naming e lançamento;
- monitoramento e resposta a incidentes;
- ondas territoriais apenas indicativas.

Classificação deste inventário:

> **Plano candidato. Não comprova titularidade corrigida, depósito, proteção internacional, contratação, ativação de controles ou operação de monitoramento.**

## 9. Autoridades afetadas por futuros pacotes

| Domínio | Documentos existentes potencialmente afetados | Possíveis novos ativos |
|---|---|---|
| Estado e publicação | README; docs/index; CHANGELOG; mkdocs; GKR-STATE; Roadmap; Board; Milestones | regra semântica de sincronização |
| Consolidação | Matriz de Consolidação central e adendos | índice de adendos ou nova edição consolidada |
| Enterprise Architecture | GEA-000; Permanence Layer Model | Technology and Engineering Architecture Foundation |
| Product Architecture | GPA-000; produtos especializados | rebaseline do portfólio |
| Intelligence | GIA-000; knowledge model; manifesto | arquitetura de grafo e analytics |
| Tecnologia | handoff do Journey; referências dispersas | ADR e arquitetura de referência técnica |
| Marca e ativos digitais | ADRs; governança; páginas públicas | programa de governança, inventário redigido e política de naming |
| Mercado | VAL-STATUS; VAL-001 a VAL-008; RP-001 | evidências de execução, resultados e decisões |
| Negócio | GBA-000; BA-STR-002 e registros | impactos somente após gates de evidência |
| Econômico | GEM-000 e contratos candidatos | atualização somente mediante evidência econômica |
| Institucional | GEA; governança; produto; público | eventual arquitetura da Fundação |
| Jurídico, dados e privacidade | contratos funcionais e públicos | políticas, registros de tratamento e transparência |
| Internacionalização | marca, domínios, produto, público e operação | programa territorial governado |
| Public Canon | GOG-001; public/index | nova edição pública após dependências |
| Vocabulário | glossary.md | termos técnicos e institucionais aprovados |

## 10. Dependências críticas

```text
fonte verificável
→ classificação de maturidade
→ autoridade proprietária
→ decisão ou contrato especializado
→ atualização dos consumidores
→ consolidação global
→ publicação pública
```

Não será aceita a sequência inversa:

```text
anúncio ou resumo público
→ tentativa posterior de criar autoridade
```

### 10.1 Tecnologia

```text
fonte Neo4j
→ intake técnico
→ arquitetura proprietária e ADR
→ validação de segurança, privacidade, custo e operação
→ referência de implementação
→ estado global somente após evidência
```

### 10.2 Marca e domínios

```text
plano externo
→ validação jurídica e de titularidade
→ modelo de inventário protegido
→ decisões sobre marcas, domínios e controles
→ atualização institucional e pública limitada
```

### 10.3 Mercado e negócio

```text
instrumento vigente
→ execução identificada
→ dados e qualidade
→ análise e gates
→ registro de evidência
→ eventual revisão de Outcomes, preços, produtos ou GTM
```

### 10.4 Fundação e internacionalização

```text
documento jurídico ou decisão formal
→ estado institucional
→ governança, financiamento e separação de responsabilidades
→ operação territorial e compliance
→ comunicação pública
```

## 11. Critérios de aceite deste inventário

Este inventário será considerado completo para seu escopo quando:

- diferenciar fato, fonte externa, relato, hipótese e histórico;
- registrar as superfícies globais em drift;
- reconhecer o estado vigente sem reabri-lo;
- identificar documentos canônicos afetados;
- impedir promoção automática de planos externos;
- registrar lacunas de evidência;
- relacionar cada lacuna a um pacote futuro;
- preservar a UXA-071 e demais frentes não iniciadas;
- possuir um programa separado com ordem, gates e fronteiras.

## 12. Resultado formal

```text
Inventory target: accumulated Guivos and GKR updates
Repository baseline: main at 066faf5c843a04b08f400f5ff5358fa059b22e88
Current-state authority: GKR-STATE-001 1.99.0 / M7.72
Confirmed global drift: yes
Confirmed thematic implementation: no
External documented candidates: Neo4j architecture; brand and digital-asset protection plan
Pending-evidence areas: domains, guivos.ai, Foundation, internationalization, operations and legal/privacy publication
Hypotheses promoted: 0
Canonical decisions created: 0
Global versions changed: 0
UXA-071 started: no
```

## 13. Continuidade

A ordem controlada dos pacotes está definida no `GKR-UPDATE-PROGRAM-001 — Programa Controlado de Atualização do Repositório`.
