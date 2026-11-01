---
id: GKR-UX-HOME-INTELLIGENCE-GAI-TEMPORAL-RECON-001
title: Reconciliação proposta — Home Guivos Intelligence e perspectivas temporais da Guivos AI
status: proposed_non_normative
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-11-01
parent: GKR-UX-HOME-INTELLIGENCE-MASTER-001
depends_on:
  - GPA-006
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
normative: false
---

# Reconciliação proposta — Home Guivos Intelligence × perspectivas temporais da Guivos AI

**Natureza:** análise de delta semântico e proposta de adendo; **não altera** o Documento Mestre, Source Lock, HandOff, Design, contratos operacionais ou governança de autorização.

## 1. Documentos confrontados
- [Documento Mestre da Home Intelligence](public-home-intelligence-master-document.md), frontmatter v0.2.14, 11 movimentos, ativo; autoridade narrativa subordinada a GPA-006.
- [Home Source Lock Intelligence](public-home-intelligence-source-lock.md), frontmatter v1.1.16, ativo; suas restrições permanecem válidas.
- [Guivos Intelligence — GPA-006](../product-architecture/intelligence.md), frontmatter v2.0.3; texto interno mantém referência de autoridade a v2.0.2, divergência de versionamento a ser conferida antes de alterar a cadeia normativa.
- Conceito de Guivos AI compartilhado pela direção: **retrospectiva (o que aconteceu?), contextual (o que acontece?), prospectiva (o que pode acontecer?)**, sob limites de evidência e autoridade.

**Constatação:** o Master já contempla relações, sinais, contexto, interpretação, mudanças, explicabilidade, contestabilidade e horizonte ampliado. Não utiliza explicitamente os termos `retrospectiva` e `prospectiva` nem estrutura as três perspectivas como modelo conceitual complementar. Isso constitui **oportunidade de explicitação**, não ausência absoluta de temporalidade no produto.

## 2. Definição candidata das três perspectivas
| Perspectiva | Pergunta pública | Fontes pertinentes | Limite epistemológico |
| --- | --- | --- | --- |
| Retrospectiva | O que aconteceu? | Experiências, oportunidades, decisões e padrões efetivamente registrados em escopo autorizado | Registro não prova intenção, causa ou completude da trajetória |
| Contextual | O que está acontecendo? | Momento atual, objetivos, circunstâncias, relações, recursos e barreiras | Contexto pode estar desatualizado, contestado ou ser inferido |
| Prospectiva | O que pode acontecer? | Cenários, caminhos possíveis, oportunidades disponíveis, condições e incertezas | Possibilidade não é previsão determinística nem promessa de resultado |

**Invariantes:** as perspectivas são **lentes complementares, não três motores obrigatórios, produtos independentes, estágios fixos, fluxo obrigatório ou promessa de previsão**. Podem ser usadas individualmente ou em combinação, conforme finalidade, dados autorizados e capacidade efetiva. `COMPREENDER ≠ DECIDIR`, `RESULTADO ESPERADO ≠ RESULTADO COMPROVADO` e `COMPREENSÃO PROFUNDA ≠ EXPOSIÇÃO PROFUNDA` permanecem preservados.

## 3. Reconciliação proposta por movimento
| Movimento vigente | Estado constatado no Master | Delta proposto | Tipo de intervenção |
| --- | --- | --- | --- |
| M01 Possibilidade | Abre pelo benefício de compreender | Preservar linguagem e não antecipar taxonomia | Sem alteração necessária |
| M02 Necessidade | Informação isolada não equivale a compreender | Permitir menção à dimensão temporal da informação sem acrescentar jargão | Complemento opcional |
| M03 Valor próprio | Conecta informações e padrões | Indicar que relações atravessam situações anteriores, presentes e futuras possíveis | Complemento pontual |
| M04 Resultados | Relações, repetições, mudanças e sinais | Mostrar exemplos separados: registrado, contexto presente, caminho possível | Complemento de exemplos |
| M05 Materialização | Comparações e indicadores conceituais | Propor representação visual das três lentes; não apresentar KPI fictício como desempenho verificado | Candidato visual, sem design autorizado por este adendo |
| **M06 Formação** | Contexto + relações + conhecimento/evidências → compreensão | **Principal ponto de inserção semântica:** três perspectivas como modos de interpretar a informação | **Adendo de conceito recomendado** |
| M07 Aplicação | Casos de compreensão sem apropriar outros produtos | Demonstrar aplicações individual/populacional somente nos respectivos limites | Complemento contextual |
| M08 Confiança | Origem, fatos, interpretação, limites | Explicitar temporalidade, incerteza e distinção entre dado registrado, leitura atual e cenário | Complemento de guardrails |
| M09 Autonomia | Compreender não é decidir | Preservar; nenhuma decisão automática por projeção | Sem mudança estrutural |
| M10 Inteligência conectada | Relações entre contextos e informações | Explicitar conexão temporal quando útil, sem causalidade inventada | Complemento pontual |
| M11 Horizonte ampliado | Sinais e possibilidades sem previsão garantida | Vincular prospectiva a caminhos e condições, não a futuro certo | Complemento de linguagem |

**Conclusão de arquitetura:** preservar **11 movimentos**, sem criar artificialmente M12 ou substituir a identidade do produto por "Guivos AI".

## 4. Proposta de microcopy para avaliação editorial
**Título opcional da representação temporal:** “Compreender o que passou. Interpretar o presente. Explorar o que pode vir.”

**Descrição candidata:** “Experiências registradas, contexto atual e caminhos possíveis oferecem perspectivas diferentes de uma mesma realidade. A Guivos Intelligence pode relacioná-las para ampliar a compreensão e apoiar escolhas, considerando evidências, limites e a autonomia de cada participante.”

**Rótulos:** `Retrospectiva — O que aconteceu?`; `Contextual — O que acontece?`; `Prospectiva — O que pode acontecer?`.

Evitar afirmações de previsão precisa, capacidade implementada, acesso irrestrito a histórico individual, causalidade ou identificação pessoal em dados populacionais.

## 5. Guardrails interproduto e de Guivos AI
1. **Guivos Intelligence ≠ Guivos AI**: IA pode apoiar o Intelligence, mas não substitui sua autoridade de produto.
2. **Pessoa / Journey:** revisões e interpretações pessoais devem continuar contestáveis e validadas; contexto individual não é aberto a Business por conveniência analítica.
3. **Business / população:** leituras retrospectivas e prospectivas devem respeitar agregação protegida, finalidade, autorização e incerteza; não expor trajetória íntima individual.
4. **Organizações e Coletivos:** compreensão temporal não cria direito a históricos ou dados individuais de outras Pessoas.
5. **IA e governança:** documentação de schema, execução, provas e gates da Guivos AI não constitui funcionalidade pública pronta; proibir afirmações de homologação, operações ou eficácia não comprovada.
6. **Sem previsão determinística:** inferência, tendência, cenário e oportunidade real são categorias distintas.
7. **Fonte de autoridade:** eventual alteração ao Master depende de revisão governada de GPA-006/Source Lock e de seus controles de publicação.

## 6. Delta recomendado para governança
- **Prioridade P1:** avaliar inclusão do modelo das três lentes no M06, com suporte visual contextual no M05 e ressalvas em M08/M11.
- **Prioridade P2:** ajustes pontuais em M03, M04, M07 e M10, evitando repetição.
- **Preservar:** M01, M02 e M09 em sua função; distinções entre Intelligence, Journey e Business; cópia de referência e os 11 movimentos.
- **Antes de mudar autoridade normativa:** verificar divergência de versão `GPA-006 v2.0.3` no frontmatter versus menção interna `v2.0.2`, efetuar revisão de impacto em Source Lock e handoff e confirmar fluxo de aprovação. **Este documento não libera alterações automáticas nesses arquivos.**

## 7. Estado da etapa
Reconciliação **documental proposta**, sem revisão institucional concluída nem aprovação editorial dos ajustes. O Master e o Source Lock originais não foram editados; nenhum design, protótipo ou sistema operacional foi alterado. Os bloqueios e decisões pendentes da Guivos AI continuam independentes e sem ampliação de autorização.
