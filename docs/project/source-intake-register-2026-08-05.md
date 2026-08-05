---
id: GKR-SOURCE-INTAKE-001
title: Registro de Intake das Fontes Acumuladas
status: draft
version: 0.3.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-STATE-001
  - GKR-UPDATES-INVENTORY-001
  - GKR-UPDATE-PROGRAM-001
related:
  - GKR-AUD-ACCUMULATED-003
  - GKR-CLAIMS-TRACE-001
normative: false
---

# Registro de Intake das Fontes Acumuladas

## 1. Finalidade

Este registro cataloga as fontes identificadas durante a auditoria das conversas, rascunhos e tratativas acumuladas.

Sua função é impedir que arquivos externos, conversas, PDFs, documentos de trabalho ou alegações operacionais sejam incorporados ao Guivos Knowledge Repository sem proveniência, classificação e decisão explícitas.

O registro não contém a íntegra das fontes e não substitui a análise temática de cada pacote. Alegações verificadas no Git estão detalhadas em [Rastreabilidade Git das Alegações Acumuladas](accumulated-claims-git-traceability-2026-08-05.md).

## 2. Legenda

### 2.1 Estado de verificação

- **verificado e integrado:** existência, conteúdo e integração à `main` confirmados;
- **verificado e proposto:** evidência localizada em PR aberto, ainda não integrada;
- **histórico ou superado:** evidência localizada, mas substituída por versão posterior;
- **fonte externa localizada:** arquivo identificado no acervo de trabalho, ainda fora do GKR;
- **alegação conversacional:** informação registrada em conversa, ainda dependente de prova Git ou documental;
- **verificação parcial:** parte da informação foi confirmada, mas falta vínculo completo;
- **não localizado:** sem evidência suficiente na baseline pesquisada; não significa prova de inexistência.

### 2.2 Decisão preliminar

- **resolvido:** já possui tratamento suficiente no cânone ou em PR específico;
- **reconciliar no P0:** exige lineage, proveniência, status ou deduplicação;
- **rotear:** deve ser analisado em pacote temático posterior;
- **quarentena:** não pode ser promovido sem decisão independente;
- **operacional:** pertence a runbook ou suporte, não ao estado arquitetural;
- **arquivar:** preservar apenas como histórico, sem autoridade vigente.

## 3. Registro das fontes

| ID | Fonte identificada | Proveniência | Status declarado na origem | Sensibilidade preliminar | Verificação atual | Desvio ou risco | Destino | Ação exigida |
|---|---|---|---|---|---|---|---|---|
| SRC-001 | PR nº 163 — Ressincronização Semântica Global | Git | draft | interno | verificado e proposto; head auditado `3191a732` | conteúdo correto poderia ser confundido com estado já integrado | P1 | manter draft; revisar e autorizar merge separadamente |
| SRC-002 | Inventário Governado das Atualizações Acumuladas | Git | draft 0.1.0 | interno | verificado e integrado como documento não normativo | pode ser interpretado como execução dos pacotes | P0 | preservar como inventário, sem autorização automática |
| SRC-003 | Programa Controlado de Atualização P0–P9 | Git | draft 0.1.0 | interno | verificado e integrado como documento não normativo | sequência pode ser tratada como autorização automática | P0 | exigir autorização independente por pacote |
| SRC-004 | Documento de arquitetura Neo4j, Graph Analytics e Power BI | acervo externo | versão 1.0; recomendação arquitetural | interno | fonte externa localizada | recomendação pode ser descrita como decisão ou implantação | P2 | produzir ADR, benchmark, custos, segurança e gates |
| SRC-005 | Plano de Execução da Fase 4 — Proteção Corporativa | acervo externo | versão 1.0; plano interno | confidencial | fonte externa localizada | plano não prova marcas, domínios, DNS ou certificados efetivados | P3 | separar diretriz, execução e comprovantes; revisar sigilo |
| SRC-006 | GKR-001 — Governança do Guivos Knowledge Repository | acervo externo | aprovado 1.0 | interno | fonte externa localizada; vínculo Git exato não localizado | aprovação declarada fora do Git pode competir com governança vigente | P0 | comparar cláusula a cláusula e decidir absorção ou arquivo histórico |
| SRC-007 | Guivos Knowledge Repository Architecture | acervo externo | draft 1.0 | interno | fonte externa localizada | arquitetura histórica pode divergir da estrutura atual | P0 | mapear o que foi absorvido, substituído ou descartado |
| SRC-008 | GC-GOV-001 — The Guivos Governance | acervo externo | draft 0.1 | interno | fonte externa localizada | fluxo de governança ainda não é autoridade por si só | P0/P9 | comparar com governança integrada e evitar duplicação |
| SRC-009 | GC-EDT-002 — Master Editorial Plan | acervo externo | draft 0.1 | interno | fonte externa localizada | plano editorial pode ser confundido com backlog autorizado | P9 | preservar como candidato; revisar dependências e autoria |
| SRC-010 | Família GC-CON-001 — corpus conceitual | acervo externo | variantes com status e versões diferentes | a classificar | fonte externa localizada; ID exato não localizado no Git pesquisado | colisão de ID e linhagem ambígua | P0 | inventariar todas as cópias, comparar hashes e declarar relação entre versões |
| SRC-011 | Rascunho do Contexto Vivo e princípio de evolução independente | acervo externo | rascunho e formulações conceituais | interno | autoridade Git do Contexto Vivo verificada; rascunho externo não reconciliado | versão externa pode duplicar ou contradizer autoridade integrada | P0 | comparar com `PAS-001-CV-CONTRACT-001` e arquivar variantes superadas |
| SRC-012 | Contrato `PAS-001-CV-CONTRACT-001` e Capacidade 02 do Contexto Vivo | Git e conversa | integrado e concluído documentariamente | interno | verificado e integrado; commit `73ea9e7`; path confirmado | conclusão documental pode ser confundida com produto implementado | resolvido no P0 | preservar limite de maturidade e usar a autoridade integrada |
| SRC-013 | Instrumentos VAL-002, VAL-006 e VAL-007 | Git, rascunho e conversa | versões diversas | interno | versões atuais verificadas: 2.1.0, 1.3.1 e 1.3.1; rascunho 1.1.0 superado | instrumento pode ser confundido com pesquisa executada | P4 | usar versões da `main`; verificar pré-teste, publicação, coleta, amostra e resultados |
| SRC-014 | Formulário B2C, IGV e KPIs de aceitação | Git, rascunho e conversa | desenho de validação | interno | desenho e critérios verificados no Git; operação não verificada | indicador definido pode ser apresentado como resultado | P4 | distinguir definição, readiness, coleta e Outcome |
| SRC-015 | COEM e ECO-CAND-001 | Git e conversa histórica | COEM concluída; decisão `Reformulate`; sem Outcome | interno | verificado e integrado pelos PRs nº 72 e nº 73 | conclusão da cobertura ou reformulação pode reaparecer como Outcome aprovado | resolvido no P0 | preservar `Under Validation`, ausência de código canônico, AQS-O01 e Outcome |
| SRC-016 | GEM-009 | Git e conversa histórica | integrado | interno | verificado e integrado pelo PR nº 55; path confirmado | métricas documentais podem ser confundidas com resultados reais | resolvido no P0 | usar autoridade vigente e preservar ausência de valores, metas e resultados |
| SRC-017 | GEM-010 e GEM-010-A2 | Git e conversa histórica | arquitetura integrada; preços candidatos | interno | verificado e integrado pelo PR nº 56 e commit `e5f757a` | cenário ou faixa candidata pode ser tratada como orçamento, preço público ou operação | resolvido no P0/P8 | preservar parâmetros como candidatos, sem oferta ou cobrança |
| SRC-018 | Fundação Guivos e `guivos.org` | conversas | conceito e intenção institucional | a classificar | não localizado como entidade constituída ou operação comprovada | risco de tratar projeto como entidade existente | P5 | exigir arquitetura institucional, governança, prova jurídica e readiness |
| SRC-019 | Voluntariado, causas e pontos patrocinados | conversas | hipótese de programa social | a classificar | alegação conversacional | impacto, financiamento, fraude, contabilidade e proteção de vulneráveis não avaliados | P5 | manter como hipótese; desenvolver modelo e controles antes de aprovação |
| SRC-020 | Internacionalização, polos BH/SP e país inicial | conversas | estratégia e intenção | confidencial | não localizado como operação territorial comprovada | presença, cadastro ou número não comprovam operação | P7 | criar matriz de evidências territoriais e readiness |
| SRC-021 | Estratégia de domínios internacionais | conversas e plano | recomendação | confidencial | verificação parcial | disponibilidade, titularidade e uso podem mudar; risco de exposição | P3/P7 | inventariar ativos comprovados em registro restrito |
| SRC-022 | Números telefônicos regionais e Lisboa | conversas | intenção operacional | confidencial | não localizado como canal ativo comprovado | canal projetado pode ser descrito como ativo | P7 | exigir titularidade, contrato, roteamento e capacidade de atendimento |
| SRC-023 | Guivos Mall versus Guivos Marketplace | Git e conversas | Mall vigente; Marketplace histórico | público | verificado e integrado pelo commit `a68bab2`; `GPA-002` 1.1.0 | materiais externos antigos podem manter nomenclatura superada | resolvido no P0/P9 | usar Guivos Mall oficialmente; varrer somente materiais externos e históricos |
| SRC-024 | Guivos Journey, Mall, Travel, Business, Media, Intelligence e Ads | Git e conversas | estrutura arquitetural oficial | público | verificado e integrado em `GPA-000` 1.30.0 | consolidação documental pode ser confundida com operação comercial de todos os componentes | resolvido no P0/P8 | preservar os sete componentes e distinguir arquitetura de implementação e operação |
| SRC-025 | Guivos.ai e IA própria | conversas | intenção de produto | confidencial | não localizado como produto ou serviço operacional comprovado | intenção pode ser confundida com produto, modelo ou serviço existente | P8 | definir autoridade, maturidade, escopo, dependências e claims permitidos |
| SRC-026 | Passport, Life Map, rankings, tribos e recompensas | conversas e materiais históricos | hipóteses variadas | a classificar | verificação parcial | conceitos em quarentena podem retornar por repetição | quarentena | não promover sem pacote, hipótese, riscos e decisão próprios |
| SRC-027 | Grafo Global de Transformação Humana | conversas | conceito arquitetural | interno | verificação parcial | conceito, banco de grafo, IA e blockchain podem ser misturados | P2/P8 | separar modelo conceitual, dados, tecnologia, segurança e produto |
| SRC-028 | Blockchain para proteção do grafo | conversas | ideia técnica | interno | não localizado como decisão ou arquitetura aprovada | blockchain não protege conteúdo por si só; risco de solução prematura | P2 | tratar como hipótese; analisar ameaças, criptografia e governança de chaves |
| SRC-029 | Integração Strava e atividade em tempo real | conversas | hipótese de integração | confidencial | não localizado como integração aprovada ou implementada | dependência de API, consentimento, localização e segurança | P6/P8 | exigir DPIA, autorização de plataforma e arquitetura de consentimento |
| SRC-030 | Perfis públicos, Instagram e avaliação no Google | conversas | comunicação operacional | público | verificação parcial | mensagem pessoal pode ser confundida com posicionamento oficial | P9 | separar comunicação do fundador, marca e claims institucionais |
| SRC-031 | Instalação do `gh`, autenticação e workspace Codex | GitHub e conversas operacionais | procedimento operacional | interno | verificação parcial | configuração transitória pode ser tratada como arquitetura | runbook | documentar fora do estado canônico; nunca registrar tokens |
| SRC-032 | Conversas de continuidade que usam “de acordo” como autorização | conversas | autorização contextual | interno | verificação parcial | autorização pode perder escopo ao mudar de conversa | governança | registrar pacote, branch, limites e ato autorizado antes da execução |
| SRC-033 | UXA-071 e seção integrada de telas e jornadas | Git e conversa | próximo passo recomendado; não iniciado | interno | estado confirmado | risco de início incidental durante a auditoria | fora do P0 | manter não iniciada até encerramento e autorização específica |
| SRC-034 | Product Engineering W0-01 | Git | pausada antes do início | interno | estado confirmado | documentação pode ser confundida com retomada | fora do P0 | preservar pausa até autorização explícita |
| SRC-035 | Resultados empresariais, clientes, parceiros e faturamento | conversas | intenções ou exemplos | confidencial | não localizado como Outcome canônico comprovado | risco de claims públicos sem evidência | P4/P6/P9 | exigir contratos, métricas, período e autorização de divulgação |
| SRC-036 | Rastreabilidade Git das Alegações Acumuladas | Git | draft 0.3.0 | interno | verificado e proposto no PR nº 164 | evidência pode ser lida sem os limites de cada claim | P0 | manter vinculada ao audit e ao intake; revisar antes do merge |

## 4. Registros de desvio vinculados

| Desvio | Fontes principais | Controle |
|---|---|---|
| D-001 — superfícies globais defasadas | SRC-001 a SRC-003 | PR nº 163 e gate semântico |
| D-002 — conversa divergente do Git | SRC-001, SRC-032 | Git prevalece para estado de execução |
| D-003 — aprovação externa | SRC-006 a SRC-010 | intake e decisão explícita de absorção |
| D-004 — linhagem `GC-CON-001` | SRC-010 | deduplicação e resolução de lineage |
| D-005 — recomendação versus implementação | SRC-004, SRC-027, SRC-028 | ADR e evidência técnica |
| D-006 — desenho versus resultado de mercado | SRC-013 a SRC-015 | trilha de evidência VAL e limites da COEM |
| D-007 — plano versus execução de proteção | SRC-005, SRC-021 | comprovantes e registro restrito |
| D-008 — conceito institucional versus entidade | SRC-018, SRC-019 | prova jurídica e readiness |
| D-009 — intenção territorial versus operação | SRC-020 a SRC-022 | matriz territorial de evidências |
| D-010 — operação versus arquitetura | SRC-031 | runbook operacional |
| D-011 — nomenclatura e estrutura de produtos | SRC-023, SRC-024 | CLM-024, CLM-025 e varredura externa |
| D-012 — retorno de hipóteses em quarentena | SRC-026 | bloqueio de promoção automática |
| D-013 — proveniência incompleta | SRC-006 a SRC-011, SRC-018 a SRC-032, SRC-035 | path, commit, versão e responsável |
| D-014 — exposição de conteúdo sensível | SRC-005, SRC-019 a SRC-022, SRC-029, SRC-035 | classificação antes de publicação |
| D-017 — integração histórica sem prova vinculada | alegações futuras | `GKR-CLAIMS-TRACE-001` |

## 5. Fila de reconciliação do P0

### Prioridade crítica

1. resolver a linhagem e as colisões da família `GC-CON-001`;
2. classificar fontes confidenciais antes de qualquer cópia;
3. impedir que “aprovado” em arquivo externo substitua aprovação do GKR;
4. manter a rastreabilidade entre alegação, arquivo, commit, autoridade e estado.

### Prioridade alta

1. comparar o rascunho externo do Contexto Vivo com a autoridade integrada;
2. verificar evidências operacionais de pré-teste, formulário publicado, coleta, base e cálculo VAL;
3. registrar destino do documento GKR-001 externo;
4. comparar a arquitetura draft histórica do GKR com a estrutura vigente;
5. classificar o plano editorial `GC-EDT-002` e o draft `GC-GOV-001`.

### Prioridade média

1. preparar o intake do documento Neo4j para P2;
2. preparar o intake do plano de proteção para P3;
3. varrer materiais externos e históricos que ainda usam Guivos Marketplace;
4. separar runbook GitHub/Codex do corpo arquitetural;
5. registrar hipóteses sociais, territoriais e de produto sem promovê-las.

## 6. Campos obrigatórios para novas fontes

Toda nova fonte adicionada a este registro deverá informar:

- identificador de intake;
- nome original;
- tipo de arquivo ou origem;
- data conhecida;
- autor ou responsável conhecido;
- versão declarada;
- hash ou localização estável, quando disponível;
- sensibilidade;
- status declarado na origem;
- status reconhecido pelo GKR;
- autoridade potencialmente afetada;
- divergências conhecidas;
- pacote de destino;
- decisão final;
- commit ou PR de resolução.

## 7. Regra de resolução

Um item somente poderá ser marcado como resolvido quando houver uma das seguintes decisões verificáveis:

1. **absorvido:** conteúdo integrado a uma autoridade, com histórico e PR;
2. **referenciado:** preservado como evidência ou fonte não normativa;
3. **substituído:** relação explícita com a autoridade sucessora;
4. **arquivado:** mantido apenas para memória histórica;
5. **rejeitado:** não compatível com o GKR, com justificativa;
6. **quarentena:** suspenso até critérios adicionais;
7. **operacional:** movido para runbook sem efeito arquitetural;
8. **duplicado:** cópia identificada e ligada ao original.

A ausência de ação não constitui resolução.

## 8. Declaração de não autoridade

Este registro não valida automaticamente o conteúdo das fontes. Ele valida que a fonte foi identificada, classificada e encaminhada para tratamento governado.

Nenhum item desta tabela altera `GKR-STATE-001`, o marco M7.72, a pausa da Engenharia de Produto ou o estado não iniciado da UXA-071.
