---
id: AR-001
title: GKR and GOG Consistency and Diagram Review
status: active
version: 0.4.0
owner: Guivos
last_updated: 2026-07-11
scope: conceptual consistency, document synchronization, editorial quality and diagrams
---

# AR-001 — GKR and GOG Consistency and Diagram Review

## 1. Finalidade

Esta revisão verifica divergências, desatualizações, sobreposições, lacunas editoriais e necessidades de diagramas entre o `GOG-001 — Guia Oficial da Guivos` e os principais documentos do Guivos Knowledge Repository.

A revisão não promove novos conceitos. Seu objetivo é alinhar o que já foi consolidado, corrigir referências legadas e melhorar a compreensão do ecossistema.

## 2. Documentos prioritários

1. `GOG-001 — Guia Oficial da Guivos`;
2. `PAS-001 — Guivos Journey`;
3. `GLPA-001 — Guivos Layered Product Architecture`;
4. `GIA-000 — Guivos Intelligence Architecture`;
5. `GKR-GLOSSARY-001 — Glossário Canônico`;
6. Foundation: Propósito, Missão e Visão;
7. Roadmap, Knowledge Board, Architectural Milestones, README, GPD e MkDocs.

## 3. Critérios da revisão

### 3.1 Consistência conceitual

- uma definição oficial por conceito;
- ausência de definições concorrentes;
- distinção entre linguagem pública, interna, arquitetural e técnica;
- preservação de propósito, missão e visão oficiais.

### 3.2 Consistência documental

- versões e estados sincronizados;
- referências e dependências atuais;
- nomenclatura oficial dos produtos;
- eliminação de termos legados quando não forem históricos.

### 3.3 Qualidade editorial

- clareza para leitores leigos e especialistas;
- redução de repetições;
- exemplos proporcionais;
- títulos e sequência lógica;
- distinção entre estado atual, visão futura e hipótese.

### 3.4 Diagramas

Um diagrama deve ser criado ou revisado quando reduzir significativamente o esforço de compreensão, esclarecer responsabilidades ou revelar relações que o texto isolado deixa ambíguas.

## 4. Achados e estado de tratamento

| ID | Documento | Achado | Severidade | Estado |
|---|---|---|---|---|
| AR-001-F01 | GOG / Foundation | Missão pública não reproduzia a missão operacional oficial. | Alta | **Resolvido no GOG 4.2.0** |
| AR-001-F02 | GOG / Foundation | Visão pública divergia da formulação oficial e utilizava “comunidades” no lugar de “coletivos”. | Alta | **Resolvido no GOG 4.2.0** |
| AR-001-F03 | GLPA / PAS | GLPA registrava “perfil do participante” e “feed” como responsabilidades permanentes. | Alta | **Resolvido na GLPA 1.1.0 e PAS 0.4.1** |
| AR-001-F04 | GIA / Roadmap | GIA mantinha dependência desatualizada do Architecture Engineering Sprint. | Média | **Resolvido na GIA 1.3.0** |
| AR-001-F05 | Glossário / PAS | Glossário não continha conceitos funcionais vigentes do PAS. | Alta | **Resolvido no Glossário 1.8.0** |
| AR-001-F06 | Glossário | “Capacidade” não distinguia competência de participante, capacidade arquitetural e capacidade funcional de produto. | Alta | **Resolvido no Glossário 1.8.0** |
| AR-001-F07 | GOG / GLPA | Diagrama público não apresentava Platform Layer e relações transversais completas. | Média | **Resolvido no GOG 4.2.0 e refinado na GLPA 1.1.0** |
| AR-001-F08 | GOG | Ausência de diagrama da primeira compreensão. | Média | **Resolvido no GOG 4.2.0** |
| AR-001-F09 | PAS | Faltavam diagramas Mermaid de Captura de Contexto, Ciclo Cognitivo e Contexto Vivo. | Média | **Resolvido no PAS 0.4.1** |
| AR-001-F10 | GOG | Public Canon poderia ser confundido com produto lançado. | Baixa | **Resolvido no GOG 4.2.0 e Glossário 1.8.0** |
| AR-001-F11 | GOG | Fluxo prático não explicitava reflexão da compreensão antes da confirmação. | Média | **Resolvido no GOG 4.2.0** |
| AR-001-F12 | GOG / PAS | GOG usa linguagem pública “oportunidades relevantes”; PAS usa internamente “Oportunidade Ativa”. | Baixa | **Mapeamento registrado no Glossário 1.8.0** |

## 5. Diagramas — estado atual

| Diagrama | Documento | Estado |
|---|---|---|
| Ciclo Contínuo de Evolução | GOG | Revisado no GOG 4.2.0 |
| Estrutura pública da Guivos | GOG | Revisado no GOG 4.2.0 |
| Primeira compreensão | GOG | Criado no GOG 4.2.0 |
| Funcionamento prático | GOG | Criado no GOG 4.2.0 |
| Arquitetura em camadas | GLPA | Revisado na GLPA 1.1.0 |
| Aplicação das camadas ao Journey | PAS | Criado no PAS 0.4.1 |
| Filosofia operacional | PAS | Convertido para Mermaid no PAS 0.4.1 |
| Relação contínua com a vida real | PAS | Convertido para Mermaid no PAS 0.4.1 |
| Ciclo Cognitivo | PAS | Convertido para Mermaid no PAS 0.4.1 |
| Captura de Contexto | PAS | Criado no PAS 0.4.1 |
| Interpretação do Contexto | PAS | Criado no PAS 0.4.1 |
| Contexto Vivo | PAS | Criado no PAS 0.4.1 |
| Ciclo de vida da informação | PAS | Convertido para state diagram no PAS 0.4.1 |
| Meu Contexto Hoje | PAS | Criado como diagrama conceitual no PAS 0.4.1 |

## 6. Etapa 1 — GOG e Foundation

**Estado:** concluída em 11/07/2026.

Principais resultados:

- propósito, missão e visão sincronizados com a Foundation;
- significado de Public Canon esclarecido;
- Momento Atual reforçado como contexto presente, não cadastro fixo;
- reflexão da compreensão inserida antes da confirmação;
- diagramas públicos criados e revisados;
- `GOG-001` atualizado para `4.2.0`.

## 7. Etapa 2 — PAS e GLPA

**Estado:** concluída em 11/07/2026.

Principais resultados:

- “perfil” substituído por visão autorizada do contexto;
- “feed” removido como responsabilidade permanente;
- superfície principal de experiência adotada como formulação neutra;
- limites entre Journey, Intelligence, serviços e Platform refinados;
- diagramas funcionais prioritários criados;
- `GLPA-001` atualizada para `1.1.0`;
- `PAS-001` atualizado para `0.4.1`.

## 8. Etapa 3 — GIA e Glossário

**Estado:** concluída em 11/07/2026.

### Alterações executadas na GIA 1.3.0

- remoção da dependência do Architecture Engineering Sprint;
- substituição pela exigência de evidência prática do Product Engineering, validação de responsabilidade permanente e decisão arquitetural formal;
- registro de Interpretação do Contexto e Contexto Vivo como conceitos funcionais vigentes no PAS;
- distinção entre Contexto Vivo e o candidato LPM;
- atualização do CIE para propor atualizações do Contexto Vivo, sem promovê-lo a componente obrigatório;
- explicitação dos limites entre Journey, Intelligence, Service e Platform Layers;
- preservação de CIE, LPM, GPMA e Intelligence Engines como candidatos ou hipóteses.

### Alterações executadas no Glossário 1.8.0

- reorganização do glossário por domínios conceituais;
- inclusão de Contexto, Captura de Contexto, Interpretação do Contexto e Contexto Vivo;
- inclusão de Representação Humilde, Meu Contexto Hoje, Proveniência, Confiança, Temporalidade e Explicabilidade;
- inclusão de Oportunidade Ativa, Evento de Vida, Intervenção Contextual e Distância para Evolução;
- distinção entre Capacidade do Participante, Capacidade Arquitetural e Capacidade Funcional de Produto;
- inclusão do Princípio da Singularidade Funcional e Contrato da Capacidade;
- inclusão de Product Engineering e Ciclo Cognitivo do Domínio;
- inclusão de Public Canon;
- registro de “oportunidade relevante” como linguagem pública preferencial para Oportunidade Ativa;
- preservação explícita de CIE e LPM fora da Canon técnica.

## 9. Etapa 4 — Documentos de estado

**Estado:** próxima.

Sincronizar:

1. Roadmap;
2. Knowledge Board;
3. Architectural Milestones;
4. README;
5. `docs/index.md`;
6. GPD;
7. Changelog;
8. MkDocs;
9. referências de versão e ponto exato de retomada.

## 10. Regra de alteração

Nenhuma correção será realizada apenas por preferência editorial. Cada alteração deverá estar ligada a divergência demonstrável, desatualização de estado, ambiguidade relevante, lacuna de compreensão ou necessidade clara de rastreabilidade.

## 11. Ponto de retomada

Iniciar a **Etapa 4 — Documentos de estado**, sincronizando versões, marcos, índices, navegação, histórico e ponto exato de retomada após as correções conceituais concluídas nas Etapas 1, 2 e 3.
