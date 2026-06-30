---
title: Roadmap Arquitetural
status: active
version: 1.8.0
owner: Guivos
last_updated: 2026-06-29
---

# Roadmap Arquitetural

Este roadmap acompanha a evolução do Guivos Knowledge Repository e da Guivos Enterprise Architecture.

## Fase 1 — Infraestrutura do GKR

- [x] Inicializar o repositório no GitHub.
- [x] Criar README e CHANGELOG.
- [x] Criar página inicial da documentação.
- [x] Configurar MkDocs.
- [x] Configurar Mermaid.
- [x] Configurar GitHub Pages.
- [x] Configurar geração de PDF como publicação derivada.
- [ ] Consolidar governança completa do GKR.

## Fase 2 — Foundation e Ecosystem Architecture

- [x] Consolidar Parte I — Fundação.
- [x] Consolidar Parte II — Modelo Fundamental.
- [ ] Consolidar Modelo dos Participantes.
- [ ] Consolidar Modelo das Oportunidades.
- [ ] Consolidar Modelo das Experiências.
- [ ] Consolidar Modelo dos Relacionamentos.
- [ ] Consolidar Modelo do Conhecimento do Ecossistema.

## Fase 3 — Product Architecture

- [x] Consolidar estrutura superior do Ecossistema Guivos.
- [x] Consolidar Guivos Journey.
- [x] Consolidar Guivos Marketplace como produto com nome provisório.
- [x] Consolidar Guivos Travel.
- [x] Consolidar Guivos Business.
- [x] Consolidar Guivos Media.
- [x] Consolidar Guivos Intelligence.
- [x] Consolidar Guivos Ads.
- [ ] Revisar nome definitivo do Guivos Marketplace.

## Fase 4 — Business Architecture

A ordem desta fase segue dependências arquiteturais, conforme o ADR-004.

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

## Fase 5 — Research

- [x] Criar o domínio `Research` no GKR.
- [x] Criar a estrutura do `RP-001 — Ecosystem Research Program`.
- [x] Consolidar conceitualmente o Research Protocol.
- [x] Definir critérios de qualidade das fontes.
- [x] Definir níveis de evidência.
- [x] Registrar princípios de neutralidade e suficiência arquitetural.
- [x] Encerrar a fase de construção metodológica do RP-001.
- [x] Congelar o método para execução, sujeito apenas a limitações concretas identificadas na prática.
- [ ] Executar o Estado da Arte.
  - [x] Análise preliminar de Systems Thinking.
  - [x] Análise preliminar de Complex Adaptive Systems.
  - [x] Análise preliminar de Network Science.
  - [ ] Analisar Ecologia com o template vigente.
  - [ ] Analisar Organizational Theory.
  - [ ] Analisar Service-Dominant Logic.
  - [ ] Analisar Knowledge Management.
  - [ ] Analisar Institutional Economics.
  - [ ] Identificar convergências entre disciplinas.
  - [ ] Identificar divergências conceituais.
  - [ ] Identificar limitações dos modelos atuais.
  - [ ] Identificar lacunas relevantes para a Guivos.
- [ ] Iniciar o Evidence Registry.
- [ ] Construir o Ecosystem Phenomena Catalog — EPC.
- [ ] Produzir a primeira meta-síntese oficial após a conclusão do núcleo interdisciplinar.
- [ ] Produzir modelos explicativos provisórios.
- [ ] Produzir recomendações arquiteturais para o BA-STR-002.
- [ ] Derivar o Candidate Outcome Register — COR a partir do EPC.

O domínio Research produz entendimento, evidências e sínteses. A decisão arquitetural permanece com a arquitetura proprietária.

## Fase 6 — Data & Intelligence Architecture

- [ ] Definir Grafo Global da Guivos.
- [ ] Definir modelo de dados conceitual.
- [ ] Definir arquitetura de IA.
- [ ] Definir mecanismos de contexto, recomendação e aprendizado.
- [ ] Definir analytics e indicadores estratégicos.

## Fase 7 — Technology Architecture

- [ ] Definir arquitetura lógica.
- [ ] Definir front-end, back-end, APIs e integrações.
- [ ] Definir infraestrutura, segurança e DevOps.
- [ ] Definir estratégia de escalabilidade.

## Fase 8 — Governance e Knowledge Architecture

- [x] Consolidar princípio de Architectural Ownership.
- [x] Consolidar ordem por dependências arquiteturais.
- [x] Iniciar validações arquiteturais com o AV-001.
- [x] Iniciar Governance Framework do GKR com Outcome Governance Method.
- [ ] Consolidar governança de ADRs e AVs.
- [ ] Consolidar padrões do GKR.
- [ ] Consolidar versionamento arquitetural.
- [ ] Consolidar Knowledge Architecture.
- [ ] Consolidar processo de evolução contínua.

## Validação arquitetural ativa

`AV-001 — GEA Structure Validation`.

Resultado provisório: nenhuma lacuna estrutural comprovada e nenhuma justificativa suficiente para criar uma camada anterior aos Outcomes.

## Hipóteses preservadas fora da Canon

- Sistema Humano de Evolução;
- transformação como fenômeno fundamental;
- mudança de estado como unidade mínima;
- Worldview;
- Knowledge-Centric Enterprise;
- modelo explicativo definitivo do domínio;
- Research Question Map;
- organização do conhecimento por perguntas;
- Knowledge Objects;
- Grafo de Conhecimento Arquitetural;
- Knowledge Twin;
- pipeline de maturidade do conhecimento.

## Próxima Sprint

Executar a análise de **Ecologia** como quarta disciplina do Estado da Arte do RP-001, aplicando integralmente o template vigente e comparando seus resultados com Systems Thinking, Complex Adaptive Systems e Network Science.
