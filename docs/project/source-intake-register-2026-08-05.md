---
id: GKR-SOURCE-INTAKE-001
title: Registro de Intake das Fontes Acumuladas
status: draft
version: 0.4.0
owner: Guivos Enterprise Architecture
last_updated: 2026-08-05
depends_on:
  - GKR-STATE-001
  - GKR-UPDATES-INVENTORY-001
  - GKR-UPDATE-PROGRAM-001
related:
  - GKR-AUD-ACCUMULATED-003
  - GKR-CLAIMS-TRACE-001
  - GKR-LINEAGE-GC-CON-001-001
  - GKR-EXT-GOV-DISPOSITION-001
normative: false
---

# Registro de Intake das Fontes Acumuladas

## 1. Finalidade

Este registro cataloga fontes identificadas durante a auditoria das conversas, rascunhos e tratativas acumuladas.

Ele impede que arquivos externos, conversas, PDFs, documentos de trabalho ou alegações operacionais sejam incorporados ao Guivos Knowledge Repository sem proveniência, classificação e decisão explícitas.

O registro não contém a íntegra das fontes e não substitui a análise temática de cada pacote. Alegações verificadas estão detalhadas em [Rastreabilidade Git das Alegações Acumuladas](accumulated-claims-git-traceability-2026-08-05.md).

## 2. Legenda

### 2.1 Estado de verificação

- **verificado e integrado:** existência, conteúdo e integração à `main` confirmados;
- **verificado e proposto:** evidência localizada em PR aberto, ainda não integrada;
- **histórico ou superado:** evidência localizada, mas substituída por versão posterior;
- **linhagem conflitante:** família externa possui colisão de ID, versão ou status;
- **fonte externa localizada:** arquivo identificado fora do GKR;
- **alegação conversacional:** informação ainda dependente de prova;
- **verificação parcial:** parte confirmada, com lacunas restantes;
- **não localizado:** sem evidência suficiente na baseline pesquisada.

### 2.2 Decisão preliminar

- **resolvido:** autoridade e tratamento definidos;
- **reconciliar no P0:** exige proveniência, comparação ou deduplicação;
- **rotear:** deve ser analisado em pacote posterior;
- **quarentena:** promoção bloqueada;
- **operacional:** pertence a runbook;
- **arquivar:** manter apenas como histórico.

## 3. Registro das fontes

| ID | Fonte identificada | Proveniência | Status na origem | Sensibilidade | Verificação atual | Risco principal | Destino | Ação exigida |
|---|---|---|---|---|---|---|---|---|
| SRC-001 | PR nº 163 — Ressincronização Semântica Global | Git | draft | interno | verificado e proposto; head `3191a732` | confusão com estado integrado | P1 | manter draft e autorizar merge separadamente |
| SRC-002 | Inventário Governado das Atualizações Acumuladas | Git | draft 0.1.0 | interno | integrado, não normativo | interpretação como execução | P0 | preservar sem autorização automática |
| SRC-003 | Programa Controlado P0–P9 | Git | draft 0.1.0 | interno | integrado, não normativo | sequência tratada como autorização | P0 | autorização independente por pacote |
| SRC-004 | Arquitetura Neo4j, Graph Analytics e Power BI | externo | recomendação 1.0 | interno | fonte externa localizada | recomendação descrita como implantação | P2 | ADR, benchmark, custos, segurança e gates |
| SRC-005 | Plano Fase 4 — Proteção Corporativa | externo | plano 1.0 | confidencial | fonte externa localizada | plano descrito como execução | P3 | separar diretriz, evidência e sigilo |
| SRC-006 | GKR-001 — Governança do GKR | externo | aprovado 1.0 | interno | histórico; princípios parcialmente absorvidos | PDF tratado como autoridade atual | resolvido no P0 | usar `GKR-EXT-GOV-DISPOSITION-001`; não importar diretamente |
| SRC-007 | Guivos Knowledge Repository Architecture | externo | draft 1.0 | interno | proposta substituída | estrutura estática tratada como vigente | resolvido no P0 | preservar como antecedente histórico |
| SRC-008 | GC-GOV-001 — The Guivos Governance | externo | draft 0.1 | interno | hipótese externa de governança | papéis e instâncias tratados como existentes | P9 ou pacote de governança | avaliar futuramente sem promover estruturas organizacionais |
| SRC-009 | GC-EDT-002 — Master Editorial Plan | externo | 0.1 a 0.3 | interno | plano editorial externo | roadmap tratado como backlog autorizado | P9 | preservar como candidato editorial |
| SRC-010 | Família GC-CON-001 | externo | 0.1 a 0.7 e múltiplos 1.0 | a classificar | `external_lineage_conflicted`; importação direta bloqueada | colisão de ID, versão e status | futura consolidação temática | inventário físico, hashes e pipeline completo |
| SRC-011 | Rascunho externo do Contexto Vivo | externo | draft | interno | autoridade Git verificada; rascunho não comparado | duplicação ou contradição | P0 | comparar com `PAS-001-CV-CONTRACT-001` |
| SRC-012 | `PAS-001-CV-CONTRACT-001` e Capacidade 02 | Git | concluído documentalmente | interno | verificado e integrado | confusão com produto implementado | resolvido | preservar limite de maturidade |
| SRC-013 | VAL-002, VAL-006 e VAL-007 | Git e externo | versões diversas | interno | atuais: 2.1.0, 1.3.1 e 1.3.1; externos 1.1.0 superados | instrumento confundido com execução | P4 | verificar pré-teste, publicação, coleta e base |
| SRC-014 | Formulário B2C, IGV e KPIs | Git, rascunho e conversa | desenho | interno | desenho verificado; operação não | indicador descrito como resultado | P4 | separar definição, readiness, coleta e Outcome |
| SRC-015 | COEM e ECO-CAND-001 | Git | COEM concluída; `Reformulate` | interno | PRs nº 72 e 73 verificados | reformulação descrita como Outcome | resolvido | preservar `Under Validation` e ausência de código canônico |
| SRC-016 | GEM-009 | Git | integrado | interno | PR nº 55 verificado | métrica descrita como resultado | resolvido | preservar ausência de valores e metas reais |
| SRC-017 | GEM-010 e GEM-010-A2 | Git | arquitetura e parâmetros candidatos | interno | PR nº 56 e commit `e5f757a` verificados | cenário descrito como orçamento ou oferta | resolvido/P8 | preservar estado candidato |
| SRC-018 | Fundação Guivos e `guivos.org` | conversa | conceito e intenção | a classificar | não localizado como entidade constituída | conceito descrito como operação | P5 | exigir governança e prova jurídica |
| SRC-019 | Voluntariado, causas e pontos patrocinados | conversa | hipótese | a classificar | alegação conversacional | riscos financeiros e sociais não avaliados | P5 | manter como hipótese |
| SRC-020 | Internacionalização e polos | conversa | estratégia | confidencial | operação territorial não localizada | intenção descrita como operação | P7 | matriz territorial de evidências |
| SRC-021 | Domínios internacionais | conversa e plano | recomendação | confidencial | verificação parcial | titularidade e disponibilidade mutáveis | P3/P7 | inventário restrito comprovado |
| SRC-022 | Telefones regionais e Lisboa | conversa | intenção | confidencial | canal ativo não localizado | canal projetado descrito como ativo | P7 | exigir titularidade e capacidade de atendimento |
| SRC-023 | Guivos Mall versus Marketplace | Git e conversa | Mall vigente | público | commit `a68bab2` e `GPA-002` verificados | material externo com nome antigo | resolvido/P9 | usar Mall; varrer materiais históricos |
| SRC-024 | Sete componentes oficiais | Git e conversa | arquitetura oficial | público | `GPA-000` 1.30.0 verificado | arquitetura confundida com operação | resolvido/P8 | preservar distinção de maturidade |
| SRC-025 | Guivos.ai e IA própria | conversa | intenção | confidencial | produto operacional não localizado | intenção descrita como serviço existente | P8 | definir autoridade e maturidade |
| SRC-026 | Passport, Life Map, rankings, tribos e recompensas | histórico | hipóteses | a classificar | verificação parcial | retorno por repetição | quarentena | pacote e decisão próprios |
| SRC-027 | Grafo Global de Transformação Humana | conversa | conceito | interno | verificação parcial | conceito, banco, IA e blockchain misturados | P2/P8 | separar camadas |
| SRC-028 | Blockchain para proteção do grafo | conversa | ideia técnica | interno | decisão não localizada | solução prematura | P2 | análise de ameaças e chaves |
| SRC-029 | Integração Strava em tempo real | conversa | hipótese | confidencial | integração não localizada | consentimento e localização | P6/P8 | DPIA, API e consentimento |
| SRC-030 | Perfis públicos e comunicação do fundador | conversa | operacional | público | verificação parcial | pessoa e marca confundidas | P9 | separar claims institucionais |
| SRC-031 | `gh`, autenticação e workspace Codex | conversa operacional | procedimento | interno | verificação parcial | configuração tratada como arquitetura | runbook | documentar sem tokens |
| SRC-032 | “De acordo” como autorização | conversa | autorização contextual | interno | verificação parcial | perda de escopo entre conversas | governança | registrar pacote, branch e limites |
| SRC-033 | UXA-071 e seção integrada de telas | Git e conversa | próximo passo não iniciado | interno | estado confirmado | início incidental | fora do P0 | autorização específica posterior |
| SRC-034 | Product Engineering W0-01 | Git | pausada | interno | estado confirmado | documentação confundida com retomada | fora do P0 | preservar pausa |
| SRC-035 | Resultados, clientes, parceiros e faturamento | conversa | exemplos ou intenções | confidencial | Outcome canônico não localizado | claims sem evidência | P4/P6/P9 | contratos, métricas e autorização |
| SRC-036 | Rastreabilidade Git das Alegações | Git | draft 0.4.0 | interno | verificado e proposto | leitura sem limites | P0 | manter vinculada ao audit e intake |
| SRC-037 | Resolução da linhagem GC-CON-001 | Git | draft 0.1.0 | interno | verificado e proposto | resolução confundida com consolidação temática | P0 | preservar bloqueio e não promover conteúdo |
| SRC-038 | Disposição das fontes de governança e arquitetura | Git | draft 0.1.0 | interno | verificado e proposto | disposição confundida com nova política normativa | P0 | usar apenas para classificação de fontes |
| SRC-039 | GC-EDT-001 — Metodologia Editorial 2.0 | externo | resolução 2.0 | interno | histórico alinhado à prática atual | documento externo tratado como política integrada | resolvido no P0 | preservar como antecedente; autoridade atual permanece no Git |

## 4. Registros de desvio vinculados

| Desvio | Fontes principais | Controle |
|---|---|---|
| D-001 — superfícies globais | SRC-001 a SRC-003 | PR nº 163 |
| D-002 — conversa divergente do Git | SRC-001, SRC-032 | Git prevalece para execução |
| D-003 — aprovação externa | SRC-006 a SRC-010, SRC-039 | disposição explícita de autoridade |
| D-004 — linhagem `GC-CON-001` | SRC-010, SRC-037 | bloqueio do ID e gates de consolidação |
| D-005 — recomendação versus implementação | SRC-004, SRC-027, SRC-028 | ADR e evidência técnica |
| D-006 — desenho versus resultado | SRC-013 a SRC-015 | trilha VAL e limites da COEM |
| D-007 — plano versus proteção executada | SRC-005, SRC-021 | comprovantes restritos |
| D-008 — conceito versus entidade | SRC-018, SRC-019 | prova jurídica |
| D-009 — intenção versus operação territorial | SRC-020 a SRC-022 | matriz territorial |
| D-010 — operação versus arquitetura | SRC-031 | runbook |
| D-011 — nomenclatura e componentes | SRC-023, SRC-024 | autoridades GPA |
| D-012 — hipóteses em quarentena | SRC-026 | bloqueio de promoção |
| D-013 — proveniência incompleta | fontes externas e conversacionais abertas | path, hash, versão e responsável |
| D-014 — exposição de conteúdo sensível | SRC-005, SRC-019 a SRC-022, SRC-029, SRC-035 | classificação antes de publicação |
| D-017 — integração sem prova | alegações futuras | `GKR-CLAIMS-TRACE-001` |

## 5. Fila de reconciliação do P0

### Prioridade crítica

1. classificar fontes confidenciais antes de qualquer cópia;
2. manter a trava que impede aprovação externa de substituir autoridade Git;
3. preservar a rastreabilidade `alegação → evidência → autoridade → limite`;
4. impedir importação direta da família `GC-CON-001`.

### Prioridade alta

1. inventariar fisicamente e calcular hashes da família `GC-CON-001`;
2. comparar o rascunho externo do Contexto Vivo com a autoridade integrada;
3. verificar evidências operacionais de pré-teste, formulário, coleta e base VAL;
4. decidir se fontes históricas externas serão armazenadas ou apenas referenciadas;
5. classificar sigilo de planos corporativos e territoriais.

### Prioridade média

1. preparar o intake Neo4j para P2;
2. preparar o plano de proteção para P3;
3. varrer materiais externos com Guivos Marketplace;
4. separar runbook GitHub/Codex;
5. registrar hipóteses sociais, territoriais e de produto sem promoção.

## 6. Campos obrigatórios para novas fontes

Toda nova fonte deverá informar:

- identificador de intake;
- nome original;
- tipo e origem;
- data;
- autor ou responsável;
- versão declarada;
- hash ou localização estável;
- sensibilidade;
- status na origem;
- status reconhecido pelo GKR;
- autoridade potencialmente afetada;
- divergências;
- pacote de destino;
- decisão final;
- commit ou PR de resolução.

## 7. Regra de resolução

Um item somente é resolvido quando recebe uma decisão verificável de:

- absorção;
- referência como evidência;
- substituição;
- arquivo histórico;
- rejeição;
- quarentena;
- classificação operacional;
- duplicidade;
- bloqueio de linhagem.

A ausência de ação não constitui resolução.

## 8. Declaração de não autoridade

Este registro classifica fontes. Ele não valida automaticamente seus conteúdos e não altera `GKR-STATE-001`, M7.72, a pausa da Engenharia de Produto ou o estado não iniciado da UXA-071.
