---
id: AR-001
title: GKR and GOG Consistency and Diagram Review
status: active
version: 0.2.0
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
| AR-001-F03 | GLPA / PAS | GLPA ainda registra “perfil do participante” e “feed” como responsabilidades permanentes. | Alta | Pendente — Etapa 2 |
| AR-001-F04 | GIA / Roadmap | GIA mantém dependência desatualizada do Architecture Engineering Sprint. | Média | Pendente — Etapa 3 |
| AR-001-F05 | Glossário / PAS | Glossário não contém conceitos funcionais vigentes do PAS. | Alta | Pendente — Etapa 3 |
| AR-001-F06 | Glossário | “Capacidade” não distingue competência de participante, capacidade arquitetural e capacidade funcional de produto. | Alta | Pendente — Etapa 3 |
| AR-001-F07 | GOG / GLPA | Diagrama público não apresentava Platform Layer e relações transversais completas. | Média | **Resolvido no GOG 4.2.0** |
| AR-001-F08 | GOG | Ausência de diagrama da primeira compreensão. | Média | **Resolvido no GOG 4.2.0** |
| AR-001-F09 | PAS | Faltam diagramas Mermaid de Captura de Contexto, Ciclo Cognitivo e Contexto Vivo. | Média | Pendente — Etapa 2 |
| AR-001-F10 | GOG | Public Canon poderia ser confundido com produto lançado. | Baixa | **Resolvido no GOG 4.2.0** |
| AR-001-F11 | GOG | Fluxo prático não explicitava reflexão da compreensão antes da confirmação. | Média | **Resolvido no GOG 4.2.0** |
| AR-001-F12 | GOG / PAS | GOG usa linguagem pública “oportunidades relevantes”; PAS usa internamente “Oportunidade Ativa”. | Baixa | Mantido por decisão editorial; registrar no Glossário/GPD |

## 5. Diagramas existentes — avaliação

| Diagrama | Documento | Estado |
|---|---|---|
| Ciclo Contínuo de Evolução | GOG | Revisado no GOG 4.2.0 |
| Estrutura pública da Guivos | GOG | Revisado no GOG 4.2.0 |
| Primeira compreensão | GOG | Criado no GOG 4.2.0 |
| Funcionamento prático | GOG | Criado no GOG 4.2.0 |
| Arquitetura em camadas | GLPA | Pendente de refinamento terminológico |
| Ciclo Cognitivo | PAS | Pendente de conversão para Mermaid |
| Captura de Contexto | PAS | Pendente de diagrama funcional |
| Contexto Vivo | PAS | Pendente de diagrama funcional |
| Meu Contexto Hoje | PAS/GOG | Avaliar após consolidação da Capacidade 02 |

## 6. Etapa 1 — GOG e Foundation

**Estado:** concluída em 11/07/2026.

### Alterações executadas

- missão sincronizada literalmente com `GEB-P01-F03`;
- visão sincronizada literalmente com `GEB-P01-F04`;
- propósito mantido conforme `GEB-P01-F02`;
- explicação de `Public Canon` adicionada;
- Momento Atual reforçado como contexto presente, não cadastro fixo;
- reflexão da compreensão inserida antes da confirmação;
- diagrama da primeira compreensão criado;
- Ciclo Contínuo revisado;
- diagrama da estrutura pública revisado com Platform Layer;
- diagrama do funcionamento prático criado;
- histórico atualizado para `GOG-001 4.2.0`.

## 7. Etapa 2 — PAS e GLPA

Próximas ações:

1. substituir “perfil do participante” por visão contextual do participante;
2. substituir “feed” como responsabilidade permanente por superfície principal de experiência;
3. revisar limites entre Experience, Intelligence, Service e Platform Layers;
4. adicionar Mermaid para Captura de Contexto;
5. converter Ciclo Cognitivo para Mermaid;
6. adicionar Mermaid para Contexto Vivo;
7. verificar compatibilidade entre o fluxo do PAS e o GOG 4.2.0.

## 8. Etapa 3 — GIA e Glossário

1. remover dependências metodológicas desatualizadas;
2. atualizar conceitos vigentes;
3. distinguir tipos de capacidade;
4. preservar candidatos fora da Canon;
5. registrar o mapeamento entre linguagem pública e interna.

## 9. Etapa 4 — Documentos de estado

Sincronizar Roadmap, Knowledge Board, Milestones, README, GPD, Changelog e navegação somente após as correções conceituais principais.

## 10. Regra de alteração

Nenhuma correção será realizada apenas por preferência editorial. Cada alteração deverá estar ligada a divergência demonstrável, desatualização de estado, ambiguidade relevante, lacuna de compreensão ou necessidade clara de rastreabilidade.

## 11. Ponto de retomada

Iniciar a **Etapa 2 — PAS e GLPA**, corrigindo terminologia e responsabilidades da GLPA e adicionando os três diagramas funcionais prioritários ao PAS.