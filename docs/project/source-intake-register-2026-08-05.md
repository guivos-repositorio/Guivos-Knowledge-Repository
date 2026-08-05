---
id: GKR-SOURCE-INTAKE-001
title: Registro de Intake das Fontes Acumuladas
status: draft
version: 0.5.6
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
  - GKR-EXT-CV-RECON-001
  - GKR-VAL-OPS-AUD-001
normative: false
---

# Registro de Intake das Fontes Acumuladas

## 1. Finalidade

Este registro cataloga fontes identificadas durante a auditoria das conversas, rascunhos e tratativas acumuladas.

Ele impede que arquivos externos, conversas, PDFs ou alegações operacionais sejam incorporados ao Guivos Knowledge Repository sem proveniência, classificação e decisão explícitas.

## 2. Estados utilizados

- **verificado e integrado:** presente na `main`;
- **verificado e proposto:** presente em PR aberto;
- **histórico ou superado:** substituído por autoridade posterior;
- **linhagem conflitante:** colisão de ID, versão ou status;
- **fonte externa:** localizada fora do GKR;
- **verificação parcial:** parte confirmada;
- **não localizado:** sem evidência suficiente;
- **evidência operacional pendente:** desenho existe, execução não comprovada;
- **quarentena:** promoção bloqueada.

## 3. Registro das fontes

| ID | Fonte | Origem | Verificação e disposição | Sensibilidade | Destino ou ação |
|---|---|---|---|---|---|
| SRC-001 | PR nº 163 — P1 | Git | proposto; draft; head `3191a732` | interno | revisão e merge separados |
| SRC-002 | Inventário acumulado | Git | integrado, não normativo | interno | preservar |
| SRC-003 | Programa P0–P9 | Git | integrado, não normativo | interno | autorização por pacote |
| SRC-004 | Neo4j, Graph Analytics e Power BI | externo | recomendação, não implantação | interno | P2 |
| SRC-005 | Plano de Proteção Corporativa | externo | plano, não execução | confidencial | P3 e revisão de sigilo |
| SRC-006 | GKR-001 — Governança | externo | histórico; princípios parcialmente absorvidos | interno | resolvido por `GKR-EXT-GOV-DISPOSITION-001` |
| SRC-007 | GKR Architecture Draft | externo | proposta substituída | interno | preservar como antecedente |
| SRC-008 | GC-GOV-001 | externo | hipótese de governança 0.1 | interno | P9 ou pacote próprio |
| SRC-009 | GC-EDT-002 | externo | plano editorial 0.1 a 0.3 | interno | P9; não é backlog autorizado |
| SRC-010 | Família GC-CON-001 | externo | `external_lineage_conflicted`; importação bloqueada | a classificar | inventário, hashes e consolidação futura |
| SRC-011 | Rascunho do Contexto Vivo | externo | histórico; núcleo absorvido; sem conflito residual | interno | resolvido por `GKR-EXT-CV-RECON-001` |
| SRC-012 | PAS-001-CV-CONTRACT-001 | Git | integrado 1.0.0 | interno | autoridade vigente |
| SRC-013 | VAL-002, VAL-006 e VAL-007 | Git e externo | atuais confirmados; drafts 1.1.0 superados | interno | P4 para operação |
| SRC-014 | Formulário B2C, IGV e KPIs | Git e conversa | desenho verificado; execução não comprovada | interno | P4; pacote de evidência operacional |
| SRC-015 | COEM e ECO-CAND-001 | Git | COEM concluída; `Reformulate`; sem Outcome | interno | resolvido com limites |
| SRC-016 | GEM-009 | Git | integrado; sem resultados reais | interno | resolvido |
| SRC-017 | GEM-010 e A2 | Git | arquitetura e parâmetros candidatos | interno | resolvido/P8 |
| SRC-018 | Fundação Guivos e guivos.org | conversa | entidade não comprovada | a classificar | P5 |
| SRC-019 | Voluntariado e pontos patrocinados | conversa | hipótese | a classificar | P5 |
| SRC-020 | Internacionalização e polos | conversa | operação não comprovada | confidencial | P7 |
| SRC-021 | Domínios internacionais | conversa e plano | verificação parcial | confidencial | P3/P7 |
| SRC-022 | Telefones regionais e Lisboa | conversa | canal ativo não comprovado | confidencial | P7 |
| SRC-023 | Mall versus Marketplace | Git | Mall oficial; Marketplace histórico | público | resolvido; varredura externa |
| SRC-024 | Sete componentes oficiais | Git | integrados em GPA-000 | público | resolvido no nível arquitetural |
| SRC-025 | Guivos.ai | conversa | produto operacional não comprovado | confidencial | P8 |
| SRC-026 | Passport, Life Map, rankings e tribos | histórico | hipóteses | a classificar | quarentena |
| SRC-027 | Grafo Global de Transformação Humana | conversa | conceito parcialmente verificado | interno | P2/P8 |
| SRC-028 | Blockchain para proteção do grafo | conversa | ideia não aprovada | interno | P2 |
| SRC-029 | Integração Strava | conversa | integração não comprovada | confidencial | P6/P8 |
| SRC-030 | Perfis e comunicação do fundador | conversa | operacional | público | P9 |
| SRC-031 | `gh`, autenticação e Codex | conversa operacional | procedimento | interno | runbook |
| SRC-032 | “De acordo” como autorização | conversa | autorização contextual | interno | registrar escopo e branch |
| SRC-033 | UXA-071 e seção de telas | Git e conversa | não iniciada | interno | fora do P0 |
| SRC-034 | Product Engineering W0-01 | Git | pausada | interno | fora do P0 |
| SRC-035 | Resultados, clientes e faturamento | conversa | Outcome não comprovado | confidencial | P4/P6/P9 |
| SRC-036 | Claims Trace | Git | draft; verificado neste PR | interno | P0 |
| SRC-037 | Resolução GC-CON-001 | Git | draft 0.1.0 | interno | P0; não é consolidação temática |
| SRC-038 | Disposição de governança externa | Git | draft 0.1.0 | interno | P0 |
| SRC-039 | GC-EDT-001 2.0 | externo | resolução histórica alinhada à prática | interno | antecedente, não política integrada |
| SRC-040 | Reconciliação do Contexto Vivo | Git | draft 0.1.0; comparação concluída | interno | P0 |
| SRC-041 | Auditoria operacional VAL | Git | draft 0.1.0; evidência pendente | interno | P4 |

## 4. Decisões consolidadas

### Resolvidos no nível de autoridade

- P1 localizado e separado;
- GEM-009 e GEM-010;
- COEM e ECO-CAND-001;
- Contexto Vivo e contrato final;
- versões VAL vigentes;
- Mall e sete componentes;
- disposição de GKR-001 e arquitetura externa;
- colisão de `GC-CON-001`;
- absorção do núcleo conceitual do rascunho do Contexto Vivo.

### Evidência ainda pendente

- pré-teste, formulário, coleta, base e decisão VAL;
- ativos corporativos e territoriais;
- constituição institucional;
- implementação tecnológica;
- operação de produtos e canais;
- inventário físico e hashes de fontes externas.

## 5. Controles por desvio

| Desvio | Controle vigente |
|---|---|
| superfícies globais | PR nº 163 |
| conversa versus Git | Git prevalece |
| aprovação externa | disposição explícita de autoridade |
| colisão GC-CON-001 | ID bloqueado e gates de consolidação |
| recomendação versus implementação | ADR e evidência técnica |
| desenho versus resultado VAL | `GKR-VAL-OPS-AUD-001` |
| plano versus execução | comprovantes |
| entidade e operação territorial | prova jurídica e matriz territorial |
| procedimento operacional | runbook |
| hipóteses antigas | quarentena |
| conteúdo sensível | classificação antes de publicação |

## 6. Prioridades restantes do P0

### Alta

1. decidir armazenamento ou referência das fontes históricas;
2. inventariar hashes de `GC-CON-001`, caso haja intake físico;
3. classificar sigilo de planos e ativos;
4. separar runbook GitHub/Codex;
5. registrar eventual evidência VAL recebida sem expor dados pessoais.

### Roteadas

- P2: tecnologia e grafo;
- P3: proteção corporativa;
- P4: execução da validação;
- P5: Fundação;
- P6: legal, privacidade e claims;
- P7: internacionalização;
- P8: produtos e hipóteses;
- P9: comunicação e editorial.

## 7. Campos obrigatórios para novas fontes

Toda nova fonte deverá informar:

- ID de intake;
- nome e origem;
- data e responsável;
- versão;
- hash ou localização;
- sensibilidade;
- status na origem e no GKR;
- autoridade afetada;
- divergências;
- destino;
- decisão e commit.

## 8. Regra de resolução

Um item somente é resolvido por decisão verificável de absorção, referência, substituição, arquivo, rejeição, quarentena, classificação operacional, duplicidade ou bloqueio de linhagem.

## 9. Checkpoint congelado

```text
Source intake: GKR-SOURCE-INTAKE-001 0.5.6
Claims trace: GKR-CLAIMS-TRACE-001
Sources catalogued: 41
Authority changes: none
Current-state changes: none
```

## 10. Declaração de não autoridade

Este registro classifica fontes. Ele não altera `GKR-STATE-001`, M7.72, UXA-071 ou a pausa da Engenharia de Produto.
