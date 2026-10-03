---
id: GE2-SYNC-004
title: Context, Participant Model and Architecture Engineering Sync
status: completed
version: 1.0.0
owner: Guivos
last_updated: 2026-07-04
scope: Multimodal context, participant model, intelligence engines and architecture engineering pause
supersedes_partial:
  - GE2-SYNC-003
---

# GE2-SYNC-004 — Context, Participant Model and Architecture Engineering Sync

## 1. Finalidade

Esta matriz registra as decisões e hipóteses desenvolvidas após `GE2-SYNC-003`, durante o aprofundamento da arquitetura funcional do Guivos Journey e da Intelligence Layer.

Ela preserva:

- a captura multimodal de contexto;
- o uso prioritário de voz como forma natural de expressão do participante;
- o conceito de Modelo Vivo do Participante;
- o Context Intelligence Engine;
- a família candidata de Intelligence Engines;
- a futura Guivos Participant Model Architecture;
- a hierarquia documental PAS, JFA e FDS;
- a transição metodológica para um Architecture Engineering Sprint;
- o ponto exato de retomada após a pausa.

Este documento não promove automaticamente novos conceitos à Canon e não cria, neste momento, GTF, GCM, GPMA, GAME, GLS, GDP ou GDF como arquiteturas permanentes.

## 2. Resumo executivo

| Campo | Estado |
|---|---|
| Era | `GE-2 — Knowledge` |
| Marco | `M5.5 — Context and Architecture Engineering Checkpoint` |
| Frente | `Enterprise Design & Business Specification` |
| Especificação vigente | `PAS-001 — Guivos Journey` |
| Arquitetura funcional vigente | `GLPA-001` |
| Novo foco registrado | Contexto multimodal e Modelo Vivo do Participante |
| Método seguinte | Architecture Engineering Sprint |
| Estado da sessão | Paused with checkpoint |
| Ponto de retomada | Projetar a taxonomia e o meta-modelo definitivo do GKR antes de criar novos documentos permanentes |

## 3. Decisões consolidadas

| ID | Decisão | Estado | Classificação |
|---|---|---|---|
| D-037 | A captura do Momento Atual não deve depender de formulário sequencial como fluxo principal | Aprovada | Product Experience |
| D-038 | Voz deve ser um canal prioritário de captura de contexto, por permitir expressão mais natural e rica | Aprovada | Product Experience |
| D-039 | A captura de contexto deve ser multimodal | Aprovada | Functional Architecture |
| D-040 | O Journey deve construir compreensão progressiva, sem exigir conhecimento completo do participante no primeiro acesso | Aprovada | Product Principle Candidate |
| D-041 | Criar o conceito de `Context Intelligence Engine (CIE)` como capacidade candidata da Intelligence Layer | Aprovada para modelagem | Intelligence Architecture Candidate |
| D-042 | Tratar o contexto do participante como estado vivo e continuamente atualizável | Aprovada para modelagem | Participant Model Candidate |
| D-043 | Adotar `Living Participant Model (LPM)` / Modelo Vivo do Participante como nome provisório oficial da descoberta | Aprovada para modelagem | Concept Candidate |
| D-044 | O participante deve poder visualizar, corrigir, complementar, limitar e controlar o contexto utilizado pela Guivos | Aprovada | Governance Principle Candidate |
| D-045 | A futura GPMA deverá abranger Pessoa, Organização e Coletivo como especializações do conceito Participante | Aprovada para investigação | Architecture Candidate |
| D-046 | PAS define o produto/camada; JFA define sua arquitetura funcional; FDS detalha domínios funcionais | Aprovada | Documentation Hierarchy |
| D-047 | Antes de criar novos documentos estruturais, executar um Architecture Engineering Sprint para projetar a taxonomia definitiva do GKR | Aprovada | Method |
| D-048 | Novos conceitos estruturais devem seguir `Discovery -> Engineering -> Canon -> Specification -> Implementation` | Aprovada como fluxo de trabalho | Governance Method Candidate |

## 4. Captura multimodal de contexto

A captura de contexto deve permitir que o participante expresse seu Momento Atual, objetivos, limitações, interesses e prioridades por meios naturais e complementares.

### Canais candidatos

- voz;
- conversa por texto;
- documentos autorizados;
- imagens autorizadas;
- localização autorizada;
- calendário autorizado;
- wearables e aplicativos de saúde ou esporte autorizados;
- integrações profissionais ou sociais autorizadas;
- histórico de interações e experiências da própria Guivos.

### Regra principal

A voz deve ser tratada como canal prioritário, mas não exclusivo.

O participante deve poder descrever sua realidade com suas próprias palavras. A Guivos poderá interpretar essa expressão e propor uma estrutura de contexto, que deverá permanecer revisável e controlável pelo participante.

## 5. Modelo Vivo do Participante

O `Living Participant Model (LPM)` é registrado como conceito candidato para representar, de forma dinâmica e contextual, o que a Guivos compreende sobre um participante ao longo do tempo.

O LPM não é:

- cadastro estático;
- perfil público;
- CRM convencional;
- prontuário irrestrito;
- mecanismo de vigilância;
- propriedade da Guivos.

O modelo poderá incluir, conforme autorização e relevância:

- identidade;
- contexto;
- Momento Atual;
- objetivos;
- Próximos Passos;
- interesses;
- competências;
- preferências;
- limitações;
- disponibilidade;
- relacionamentos;
- experiências;
- evidências de evolução;
- histórico;
- confiança e proveniência das informações;
- permissões e restrições de uso.

## 6. Princípios candidatos preservados fora da Canon

### H-GPM-001 — Memória Evolutiva

A Guivos não coleta informações apenas para preencher cadastros; ela constrói e aperfeiçoa progressivamente uma representação contextual do participante, utilizando dados autorizados, relevantes e governados.

### H-GPM-002 — Compreensão Progressiva

A Guivos não busca conhecer completamente o participante no primeiro contato. A compreensão é construída progressivamente por interações naturais, experiências e evidências autorizadas.

### H-GPM-003 — Soberania do Participante

O participante deve poder visualizar, corrigir, complementar, limitar e controlar as informações utilizadas para personalizar sua jornada, observadas obrigações legais e operacionais.

### H-GPM-004 — Evolução Assistida

Toda funcionalidade permanente da Guivos deve contribuir para compreender melhor o participante, ampliar sua capacidade de decisão ou facilitar sua evolução por meio de oportunidades, experiências, conexões e conhecimento.

### H-GPM-005 — Evolução Contínua

Experiências relevantes podem gerar evidências que enriquecem a compreensão do participante e melhoram a aderência de futuras recomendações.

Essas formulações permanecem como hipóteses e princípios candidatos até investigação, delimitação e validação arquitetural.

## 7. Context Intelligence Engine

O `Context Intelligence Engine (CIE)` é registrado como capacidade candidata da Intelligence Layer responsável por:

- receber entradas multimodais autorizadas;
- interpretar linguagem natural e sinais contextuais;
- identificar elementos explícitos e inferências provisórias;
- propor atualizações do Modelo Vivo do Participante;
- registrar proveniência, temporalidade e confiança;
- solicitar confirmação quando necessário;
- preservar explicabilidade;
- respeitar consentimento e limites de uso.

O CIE não deve alterar silenciosamente fatos sensíveis ou permanentes sobre o participante sem critérios de confirmação e governança.

## 8. Família candidata de Intelligence Engines

A seguinte família foi identificada para futura modelagem dentro da Guivos Intelligence Architecture:

| Sigla | Nome | Responsabilidade candidata |
|---|---|---|
| CIE | Context Intelligence Engine | Compreender contexto e atualizar modelos vivos |
| RIE | Recommendation Intelligence Engine | Priorizar e explicar recomendações |
| MIE | Matching Intelligence Engine | Relacionar participantes, oportunidades, organizações e recursos |
| LIE | Learning Intelligence Engine | Aprender com experiências e evidências autorizadas |
| PIE | Prediction Intelligence Engine | Produzir antecipações e cenários probabilísticos governados |
| TIE | Trust Intelligence Engine | Avaliar confiabilidade, reputação, risco e qualidade |
| KIE | Knowledge Intelligence Engine | Interpretar e aplicar conhecimento institucional, científico e do ecossistema |

Essa família não representa, neste momento, microserviços, produtos ou componentes técnicos obrigatórios. Representa responsabilidades candidatas para modelagem arquitetural.

## 9. Relação entre LPM, Grafo Global e Intelligence

```text
Participante
  -> Captura Multimodal
  -> Context Intelligence Engine
  -> Living Participant Model
  -> Grafo Global da Guivos
  -> Intelligence Engines
  -> Journey e demais camadas
  -> Experiências
  -> Evidências autorizadas
  -> atualização do Living Participant Model
```

O LPM representa a memória contextual de um participante.

O Grafo Global representa a memória relacional do ecossistema.

A Intelligence Layer utiliza ambos para apoiar decisões e recomendações.

## 10. Especializações futuras do modelo de participante

A futura investigação da GPMA deverá considerar:

- `Living Person Model` — Pessoa;
- `Living Organization Model` — Organização;
- `Living Collective Model` — Coletivo.

Essas especializações deverão compartilhar uma base comum, preservando atributos e regras próprias de cada categoria de participante.

## 11. Hierarquia documental aprovada para produto

```text
GPA
  -> PAS
       -> JFA
            -> FDS
       -> UX Specification
       -> Technical Specification
```

| Artefato | Pergunta principal |
|---|---|
| GPA | Como o ecossistema organiza seus produtos e camadas? |
| PAS | O que é o produto/camada e quais responsabilidades possui? |
| JFA | Como o produto funciona por domínios funcionais permanentes? |
| FDS | Como funciona detalhadamente um domínio funcional específico? |
| UX Specification | Como o participante interage com o produto? |
| Technical Specification | Como a solução será implementada? |

## 12. Estruturas candidatas para investigação futura

Foram identificadas, mas não criadas como documentos permanentes:

- `GTF — Guivos Transformation Framework`;
- `GCM — Guivos Conceptual Model`;
- `GPMA — Guivos Participant Model Architecture`;
- evolução detalhada da `GIA — Guivos Intelligence Architecture`;
- `GLS — Guivos Language System`;
- `GDP — Guivos Design Principles`;
- `GDF — Guivos Decision Framework`;
- `GAME — Guivos Architecture Methodology & Engineering`.

A criação de qualquer um desses ativos dependerá do Architecture Engineering Sprint e da demonstração de responsabilidade permanente, ausência de sobreposição e valor institucional claro.

## 13. Architecture Engineering Sprint

### Objetivo

Projetar a estrutura definitiva do GKR antes de expandir o conjunto de documentos permanentes.

### Entregáveis esperados

1. taxonomia oficial de artefatos;
2. categorias documentais;
3. relações de dependência;
4. regras de responsabilidade conceitual;
5. ciclo de vida de artefatos;
6. critérios de promoção à Canon;
7. regras de nomenclatura e identificadores;
8. relação entre Framework, Modelo, Arquitetura, Especificação, Método, Governança e Implementação;
9. ponto oficial de manutenção de cada conceito estrutural.

### Regra de contenção

Até a conclusão desse sprint, novos documentos estruturais devem ser registrados como candidatos no backlog, e não criados automaticamente.

## 14. Ponto exato de retomada

Retomar pelo início do `Architecture Engineering Sprint`.

A primeira atividade será projetar a taxonomia oficial e o meta-modelo do Guivos Knowledge Repository.

Depois dessa definição, decidir quais dos ativos candidatos — GTF, GCM, GPMA, GIA detalhada, GLS, GDP, GDF e GAME — realmente devem existir e em qual ordem.

O trabalho do `PAS-001 — Guivos Journey` permanece preservado e deverá ser retomado após essa decisão estrutural, começando pela JFA e pela Captura Multimodal de Contexto.

## 15. Preservação institucional

- O GKA-000 permanece incompleto na Parte V.
- A pasta `docs/knowledge-architecture/` permanece não autorizada.
- A2-R02 permanece em espera operacional.
- Nenhum princípio candidato deste documento é promovido automaticamente à Canon.
- O Guivos Economic Model permanece planejado e será desenvolvido após dependências conceituais e funcionais suficientes.