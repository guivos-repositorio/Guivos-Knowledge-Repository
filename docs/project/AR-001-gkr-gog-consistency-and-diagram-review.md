---
id: AR-001
title: GKR and GOG Consistency and Diagram Review
status: active
version: 0.1.0
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

## 4. Achados iniciais

| ID | Documento | Achado | Severidade | Tratamento proposto |
|---|---|---|---|---|
| AR-001-F01 | GOG / Foundation | A missão pública não reproduz a missão operacional oficial. O GOG inclui “experiências, conexões e conhecimento”, enquanto a Foundation define “oportunidades mais relevantes para seu momento de vida”. | Alta | Restaurar a formulação oficial no bloco institucional e, se necessário, manter a ampliação em parágrafo explicativo separado. |
| AR-001-F02 | GOG / Foundation | A visão pública omite “de referência”, substitui a formulação “Tornar a Guivos” por “Tornar-se” e utiliza “comunidades” onde a Foundation adota “coletivos”. | Alta | Sincronizar literalmente a visão oficial e explicar publicamente o alcance quando necessário. |
| AR-001-F03 | GLPA / PAS | A GLPA ainda registra “perfil do participante” e “feed” como responsabilidades da Experience Layer. O PAS evoluiu para Contexto Vivo e rejeita a redução do Journey a um feed. | Alta | Substituir por “visão do contexto do participante” e “superfície principal de experiência”, preservando feed apenas como possibilidade de interface, não como responsabilidade permanente. |
| AR-001-F04 | GIA / Roadmap | A GIA afirma que a futura GPMA depende do Architecture Engineering Sprint. O foco vigente foi alterado para Product Engineering e o sprint de meta-arquitetura deixou de ser atividade imediata. | Média | Atualizar a condição para validação prática suficiente no PAS e futura decisão arquitetural formal. |
| AR-001-F05 | Glossário / PAS | O Glossário Canônico ainda não contém Contexto Vivo, Interpretação do Contexto, Oportunidade Ativa, Intervenção Contextual, Representação Humilde, Product Engineering e o novo significado de capacidade funcional. | Alta | Atualizar o glossário sem promover LPM, CIE ou outros candidatos à Canon. |
| AR-001-F06 | Glossário | “Capacidade” está definida apenas como competência arquitetural de participante, enquanto o PAS passou a usar “capacidade funcional de produto”. | Alta | Criar distinção explícita entre Capacidade do Participante, Capacidade Arquitetural e Capacidade Funcional de Produto. |
| AR-001-F07 | GOG / GLPA | O diagrama público de estrutura não apresenta a Platform Layer e pode sugerir que Intelligence e soluções se relacionam apenas por meio de Journey. | Média | Redesenhar o diagrama público para mostrar Experience, Intelligence e Soluções como naturezas integradas, sustentadas por uma base de plataforma não pública. |
| AR-001-F08 | GOG | O Guia não possui um diagrama específico para a primeira compreensão: expressão por voz/texto → interpretação → reflexão → confirmação → primeiro valor. | Média | Adicionar diagrama público simples na seção de contexto. |
| AR-001-F09 | PAS | O PAS possui fluxos em blocos de texto, mas ainda carece de diagramas Mermaid para Captura de Contexto, Ciclo Cognitivo e Contexto Vivo. | Média | Inserir diagramas funcionais sem antecipar arquitetura técnica. |
| AR-001-F10 | GOG | O Guia usa corretamente linguagem futura em vários trechos, mas o status `public-canon` pode ser confundido com produto já lançado. | Baixa | Acrescentar explicação visível de que Public Canon significa narrativa institucional oficial, não disponibilidade comercial. |
| AR-001-F11 | GOG | A seção “Como a Guivos funcionará na prática” não mostra explicitamente a etapa de reflexão da compreensão antes da confirmação, embora ela esteja consolidada no PAS. | Média | Inserir “a Guivos apresenta o que compreendeu” antes de revisão/correção. |
| AR-001-F12 | GOG / PAS | O GOG fala em “oportunidades relevantes”; o PAS distingue internamente Oportunidade de Oportunidade Ativa. A simplificação pública é adequada, mas precisa permanecer explicitamente documentada como decisão editorial. | Baixa | Manter linguagem pública simples e registrar o mapeamento no GPD/Glossário. |

## 5. Diagramas existentes — avaliação inicial

| Diagrama | Documento | Estado inicial | Observação |
|---|---|---|---|
| Ciclo Contínuo de Evolução | GOG | Manter com revisão | O ciclo está coerente, mas deve ser comparado com o fluxo funcional central do PAS. |
| Estrutura pública da Guivos | GOG | Revisar | Relações entre camadas e ausência da Platform Layer podem induzir interpretação incompleta. |
| Arquitetura em camadas | GLPA | Manter com refinamento | Estrutura correta; revisar termos Graph/Grafo, perfil e feed. |
| Ciclo Cognitivo | PAS | Converter para Mermaid | Atualmente expresso como bloco textual. |
| Captura de Contexto | PAS | Criar | Necessário para compreensão e futura execução por UX e Produto. |
| Contexto Vivo | PAS | Criar | Deve representar entradas, interpretação, confirmação, dimensões, atualização e uso. |
| Meu Contexto Hoje | PAS/GOG | Avaliar | Pode ser representado como diagrama conceitual, não mockup de tela. |

## 6. Ordem de execução

### Etapa 1 — GOG e Foundation

1. alinhar propósito, missão e visão;
2. revisar terminologia pública;
3. revisar fluxo prático;
4. revisar e adicionar diagramas públicos;
5. esclarecer o significado de Public Canon.

### Etapa 2 — PAS e GLPA

1. alinhar Contexto Vivo, perfil e superfície de experiência;
2. revisar responsabilidades das camadas;
3. adicionar diagramas Mermaid funcionais;
4. validar limites entre Journey, Intelligence, serviços e plataforma.

### Etapa 3 — GIA e Glossário

1. remover dependências metodológicas desatualizadas;
2. atualizar conceitos vigentes;
3. distinguir tipos de capacidade;
4. preservar candidatos fora da Canon.

### Etapa 4 — Documentos de estado

Sincronizar Roadmap, Knowledge Board, Milestones, README, GPD, Changelog e navegação somente após as correções conceituais principais.

## 7. Regra de alteração

Nenhuma correção será realizada apenas por preferência editorial. Cada alteração deverá estar ligada a:

- uma divergência demonstrável;
- uma desatualização de estado;
- uma ambiguidade relevante;
- uma lacuna de compreensão;
- ou uma necessidade clara de rastreabilidade.

## 8. Ponto de retomada

Iniciar pela **Etapa 1 — GOG e Foundation**, corrigindo primeiro Missão e Visão, depois revisando o fluxo público de compreensão do contexto e os diagramas associados.
