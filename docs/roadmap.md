---
title: Roadmap Arquitetural
status: active
version: 2.2.0
owner: Guivos
last_updated: 2026-06-30
---

# Roadmap Arquitetural

Este roadmap acompanha a evolução do Guivos Knowledge Repository e da Guivos Enterprise Architecture.

## Baseline vigente

`M1 — Research Foundation Complete` — estado `frozen`.

## Checkpoint ativo

`M2.0 — Architectural Evolution Hypothesis` — estado `experimental`.

## Modelo institucional vigente

`GEA-PLM-001 — Permanence Layer Model` — estado `validated`.

## Direção estratégica

O GKR representa a Guivos em sua capacidade máxima e estado de maturidade. A realização ocorre progressivamente por Reference Architectures, Enterprise Programs e Enterprise Delivery.

```mermaid
graph LR
    PA[Permanent Architecture] --> RA[Reference Architecture]
    RA --> EP[Enterprise Programs]
    EP --> ED[Enterprise Delivery]
    ED --> L[Resultados e Aprendizado]
```

## Fase M1 — Fundamentos concluídos

### Infraestrutura do GKR

- [x] Inicializar o repositório no GitHub.
- [x] Criar README e CHANGELOG.
- [x] Criar página inicial da documentação.
- [x] Configurar MkDocs.
- [x] Configurar Mermaid.
- [x] Configurar GitHub Pages.
- [x] Configurar geração de PDF como publicação derivada.
- [x] Criar Baseline M1.
- [x] Formalizar o GKR como representação canônica da Guivos em seu estado de maturidade.
- [ ] Consolidar governança completa do GKR.

### Foundation e Ecosystem Architecture

- [x] Consolidar Parte I — Fundação.
- [x] Consolidar Parte II — Modelo Fundamental.
- [x] Adotar princípios de maturidade institucional, visão antes da execução e realização progressiva.
- [ ] Consolidar Modelo dos Participantes.
- [ ] Consolidar Modelo das Oportunidades.
- [ ] Consolidar Modelo das Experiências.
- [ ] Consolidar Modelo dos Relacionamentos.
- [ ] Consolidar Modelo do Conhecimento do Ecossistema.

### Product Architecture

- [x] Consolidar estrutura superior do Ecossistema Guivos.
- [x] Consolidar Guivos Journey.
- [x] Consolidar Guivos Marketplace como produto com nome provisório.
- [x] Consolidar Guivos Travel.
- [x] Consolidar Guivos Business.
- [x] Consolidar Guivos Media.
- [x] Consolidar Guivos Intelligence.
- [x] Consolidar Guivos Ads.
- [ ] Revisar nome definitivo do Guivos Marketplace.

### Business Architecture

A ordem segue dependências arquiteturais, conforme o ADR-004.

1. [x] `BA-FND-001` — Business Architecture Foundations.
2. [x] `BA-STR-001` — Business Transformation Model.
3. [ ] `BA-STR-002` — Business Outcomes.
   - [x] Pergunta arquitetural.
   - [x] Modelo conceitual.
   - [x] Propriedades, limites e governança inicial.
   - [x] Validar provisoriamente a necessidade de uma camada anterior aos Outcomes.
   - [x] Definir Outcome Governance Method.
   - [x] Definir estrutura do COR, External Validation, COEM e AQS-O01.
   - [ ] Construir Candidate Outcome Register — COR.
   - [ ] Realizar validação externa dos grupos candidatos.
   - [ ] Aplicar Candidate Outcome Evaluation Matrix — COEM.
   - [ ] Validar e estabilizar AQS-O01.
   - [ ] Definir catálogo de Ecosystem Outcomes.
   - [ ] Definir catálogo de Business Outcomes.
   - [ ] Consolidar matriz de sustentação.
4. [ ] `BA-CAP-001` — Core Business Capabilities.
5. [ ] `BA-CAP-002` — Capability Map.
6. [ ] `BA-STR-003` — Value Chains.
7. [ ] `BA-ORG-001` — Organizational Model.
8. [ ] `BA-ORG-002` — Operating Model.
9. [ ] `BA-EXE-001` — Business Processes.
10. [ ] `BA-EXE-002` — KPIs & Metrics.

### Research Foundation

- [x] Criar o domínio `Research` no GKR.
- [x] Criar a estrutura do `RP-001 — Ecosystem Research Program`.
- [x] Consolidar conceitualmente o Research Protocol.
- [x] Definir critérios de qualidade das fontes.
- [x] Definir níveis de evidência.
- [x] Registrar princípios de neutralidade e suficiência arquitetural.
- [x] Encerrar a fase de construção metodológica do RP-001.
- [x] Congelar o método para execução, sujeito apenas a limitações concretas identificadas na prática.
- [x] Concluir o Ciclo 1 conceitual do Estado da Arte com oito perspectivas.
- [x] Criar a MS-001 em estado `draft`.
- [x] Formalizar o princípio de rastreabilidade no ADR-005.

## Fase M2 — Validation & Refinement

Objetivo: confrontar hipóteses, modelos e arquiteturas com evidências, aplicação, contraexemplos e resultados observáveis antes de promoção à Canon.

### M2.0 — Architectural Evolution Hypothesis

- [x] Registrar o Checkpoint M2.0.
- [x] Definir ciclo experimental de maturidade.
- [x] Preservar GMM, GKS, GKVF e KVS fora da Canon.
- [x] Reduzir expansão metodológica sem necessidade prática.
- [ ] Retomar essas hipóteses apenas quando uma lacuna institucional comprovada exigir.

### M2.1 — Validação do RP-001

- [ ] Iniciar o Evidence Registry.
- [ ] Registrar fontes primárias, revisões qualificadas e padrões oficiais.
- [ ] Associar evidências e contraevidências aos MECs.
- [ ] Revisar equivalências terminológicas entre disciplinas.
- [ ] Identificar contraexemplos e limites de contexto.
- [ ] Reavaliar níveis de evidência.
- [ ] Refinar a MS-001.

### M2.2 — Tradução para o EPC

- [ ] Definir fenômenos candidatos sustentados pela MS-001 refinada.
- [ ] Construir o Ecosystem Phenomena Catalog — EPC.
- [ ] Registrar convergências, divergências e limitações por fenômeno.
- [ ] Aplicar critérios de saturação.

### M2.3 — Tradução arquitetural

- [ ] Produzir Architectural Recommendations para o BA-STR-002.
- [ ] Derivar o Candidate Outcome Register — COR a partir do EPC.
- [ ] Realizar External Validation.
- [ ] Aplicar COEM.
- [ ] Estabilizar AQS-O01.
- [ ] Definir catálogos de Ecosystem Outcomes e Business Outcomes.

## Fase M3 — Progressive Realization

Objetivo: transformar a arquitetura de maturidade da Guivos em arquiteturas de referência, programas corporativos e entregas executáveis, sem reduzir a visão institucional.

### M3.0 — Institutional Architecture Consolidation

- [x] Criar `GEA-PLM-001 — Permanence Layer Model`.
- [x] Definir Permanent Architecture.
- [x] Definir Reference Architecture.
- [x] Definir Enterprise Programs.
- [x] Definir Enterprise Delivery.
- [x] Formalizar Institutional Permanence.
- [x] Formalizar Vision First.
- [x] Formalizar Architectural Gravity.
- [x] Formalizar Progressive Realization.
- [x] Formalizar Layer Integrity.
- [x] Atualizar GEA, Foundation, README e Knowledge Board.

### M3.1 — Reference Architecture

- [ ] Classificar ativos existentes pela camada de permanência.
- [ ] Consolidar visão de maturidade da plataforma.
- [ ] Consolidar Data & Intelligence Architecture.
- [ ] Consolidar Technology Architecture.
- [ ] Consolidar arquitetura de IA.
- [ ] Consolidar arquitetura de dados e grafos.
- [ ] Consolidar segurança, integração, observabilidade e escalabilidade.
- [ ] Consolidar arquitetura de referência dos produtos.

### M3.2 — Enterprise Programs

- [ ] Definir portfólio executivo de programas.
- [ ] Definir programa de Platform Engineering.
- [ ] Definir programa de Product Portfolio.
- [ ] Definir programa de AI, Data & Knowledge.
- [ ] Definir programa de Business Growth.
- [ ] Definir programa de Global Expansion.
- [ ] Definir objetivos, dependências, marcos e indicadores de cada programa.

### M3.3 — Enterprise Delivery

- [ ] Definir repositórios e ferramentas de execução.
- [ ] Definir backlog, releases e ciclos de entrega.
- [ ] Manter tecnologias específicas fora da Permanent Architecture.
- [ ] Garantir rastreabilidade entre entrega, programa e arquitetura de referência.
- [ ] Registrar aprendizados que justifiquem revisões arquiteturais.

## Governance e Knowledge Architecture

- [x] Consolidar princípio de Architectural Ownership.
- [x] Consolidar ordem por dependências arquiteturais.
- [x] Iniciar validações arquiteturais com o AV-001.
- [x] Iniciar Governance Framework do GKR com Outcome Governance Method.
- [x] Adotar o Architectural Traceability Principle.
- [x] Criar o Baseline M1.
- [x] Criar o Checkpoint M2.0.
- [x] Criar o Permanence Layer Model.
- [ ] Consolidar governança de ADRs e AVs.
- [ ] Consolidar padrões do GKR.
- [ ] Consolidar versionamento arquitetural.
- [ ] Consolidar Knowledge Architecture.
- [ ] Consolidar processo de evolução contínua.

## Hipóteses preservadas fora da Canon

- Sistema Humano de Evolução;
- transformação como fenômeno fundamental;
- mudança de estado como unidade mínima;
- Worldview;
- Knowledge-Centric Enterprise;
- Modelo Explicativo Integrado — MEI;
- Enterprise Theory;
- Research Question Map;
- organização do conhecimento por perguntas;
- Knowledge Objects;
- Grafo de Conhecimento Arquitetural;
- Knowledge Twin;
- Expected Behaviors;
- Roadmap Epistemológico;
- pipeline de maturidade do conhecimento;
- catálogo definitivo de invariantes;
- Guivos Meta-Model — GMM;
- Guivos Knowledge System — GKS;
- Knowledge Validation Framework — GKVF;
- Knowledge Validation Standards — KVS.

## Próxima Sprint

Iniciar a **M3.1 — Reference Architecture**, classificando os ativos existentes por camada de permanência e descrevendo a Guivos em sua capacidade máxima, sem recorrer a limitações de MVP ou de implementação corrente.
