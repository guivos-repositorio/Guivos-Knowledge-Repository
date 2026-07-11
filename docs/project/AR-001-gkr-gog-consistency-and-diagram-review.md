---
id: AR-001
title: GKR and GOG Consistency and Diagram Review
status: active
version: 0.3.0
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
| AR-001-F04 | GIA / Roadmap | GIA mantém dependência desatualizada do Architecture Engineering Sprint. | Média | Pendente — Etapa 3 |
| AR-001-F05 | Glossário / PAS | Glossário não contém conceitos funcionais vigentes do PAS. | Alta | Pendente — Etapa 3 |
| AR-001-F06 | Glossário | “Capacidade” não distingue competência de participante, capacidade arquitetural e capacidade funcional de produto. | Alta | Pendente — Etapa 3 |
| AR-001-F07 | GOG / GLPA | Diagrama público não apresentava Platform Layer e relações transversais completas. | Média | **Resolvido no GOG 4.2.0 e refinado na GLPA 1.1.0** |
| AR-001-F08 | GOG | Ausência de diagrama da primeira compreensão. | Média | **Resolvido no GOG 4.2.0** |
| AR-001-F09 | PAS | Faltavam diagramas Mermaid de Captura de Contexto, Ciclo Cognitivo e Contexto Vivo. | Média | **Resolvido no PAS 0.4.1** |
| AR-001-F10 | GOG | Public Canon poderia ser confundido com produto lançado. | Baixa | **Resolvido no GOG 4.2.0** |
| AR-001-F11 | GOG | Fluxo prático não explicitava reflexão da compreensão antes da confirmação. | Média | **Resolvido no GOG 4.2.0** |
| AR-001-F12 | GOG / PAS | GOG usa linguagem pública “oportunidades relevantes”; PAS usa internamente “Oportunidade Ativa”. | Baixa | Mantido por decisão editorial; registrar no Glossário/GPD |

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

**Estado:** concluída em 11/07/2026.

### Alterações executadas na GLPA 1.1.0

- substituição de `perfil do participante` por `visão autorizada do contexto do participante`;
- remoção de `feed` como responsabilidade permanente;
- adoção de `superfície principal de experiência` como formulação neutra;
- esclarecimento de que feed, conversa, mapa e painel são possíveis superfícies, não a definição do Journey;
- refinamento do diagrama em camadas;
- explicitação das relações transversais entre Intelligence e serviços especializados;
- esclarecimento de que o Journey não é intermediário técnico obrigatório;
- definição dos limites de Contexto Vivo entre Journey, Intelligence e Platform;
- reforço de que os diagramas funcionais não prescrevem topologia técnica.

### Alterações executadas no PAS 0.4.1

- alinhamento da definição do Journey à Experience Layer;
- inclusão de limites funcionais específicos do Contexto Vivo;
- conversão da sequência comportamental para Mermaid;
- conversão da relação contínua com a vida real para Mermaid;
- conversão do Ciclo Cognitivo para Mermaid;
- criação do fluxo funcional da Captura de Contexto;
- criação do fluxo funcional da Interpretação do Contexto;
- criação do fluxo funcional do Contexto Vivo;
- conversão do ciclo de vida da informação para `stateDiagram-v2`;
- criação do diagrama conceitual `Meu Contexto Hoje`;
- inclusão de ressalvas para impedir leitura dos diagramas como arquitetura técnica definitiva.

### Validação entre PAS e GOG

Os fluxos agora preservam a mesma sequência conceitual:

```text
Expressão autorizada
→ interpretação e organização
→ apresentação da compreensão
→ confirmação, correção ou limitação
→ objetivos e Próximos Passos
→ oportunidades relevantes
→ experiência
→ resultados e evidências
→ atualização da compreensão
```

O GOG mantém linguagem pública simplificada. O PAS preserva distinções internas como Oportunidade Ativa, Intervenção Contextual e Contexto Vivo.

## 8. Etapa 3 — GIA e Glossário

**Estado:** próxima.

1. remover da GIA a dependência desatualizada do Architecture Engineering Sprint;
2. alinhar LPM e CIE à validação prática vigente sem promovê-los à Canon;
3. atualizar conceitos funcionais vigentes no Glossário;
4. distinguir Capacidade do Participante, Capacidade Arquitetural e Capacidade Funcional de Produto;
5. registrar Contexto Vivo, Interpretação do Contexto, Oportunidade Ativa, Intervenção Contextual e Representação Humilde;
6. registrar o mapeamento entre linguagem pública e interna;
7. preservar candidatos e hipóteses fora da Canon.

## 9. Etapa 4 — Documentos de estado

Sincronizar Roadmap, Knowledge Board, Milestones, README, GPD, Changelog e navegação somente após as correções conceituais principais.

## 10. Regra de alteração

Nenhuma correção será realizada apenas por preferência editorial. Cada alteração deverá estar ligada a divergência demonstrável, desatualização de estado, ambiguidade relevante, lacuna de compreensão ou necessidade clara de rastreabilidade.

## 11. Ponto de retomada

Iniciar a **Etapa 3 — GIA e Glossário**, corrigindo a dependência metodológica da GIA e consolidando no Glossário as distinções e conceitos funcionais já vigentes no PAS.