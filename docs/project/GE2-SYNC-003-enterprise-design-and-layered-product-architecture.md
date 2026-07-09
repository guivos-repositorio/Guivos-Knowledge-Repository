---
id: GE2-SYNC-003
title: Enterprise Design and Layered Product Architecture Sync
status: completed
version: 1.0.0
owner: Guivos
last_updated: 2026-07-04
scope: Enterprise Design, PAS-001 and GLPA
supersedes_partial:
  - GE2-SYNC-002
---

# GE2-SYNC-003 — Enterprise Design and Layered Product Architecture Sync

## 1. Finalidade

Esta matriz registra as decisões tomadas após a sincronização `GE2-SYNC-002`, durante a transição temporária da discussão da GKA para a especificação funcional, operacional e econômica da Guivos.

Seu objetivo é preservar as decisões sobre a nova fase de trabalho, a especificação do Guivos Journey, a mudança metodológica para decisões executáveis e a descoberta da `Guivos Layered Product Architecture (GLPA)`.

Este artefato não substitui o `GKA-000`, não encerra a GE-2 e não autoriza a criação da pasta `docs/knowledge-architecture/`.

## 2. Resumo executivo

| Campo | Valor |
|---|---|
| Era | `GE-2 — Knowledge` |
| Sprint | `0.28.0 — Guivos Knowledge Architecture Foundation` |
| Modo GE-2 | `Institutional Consolidation Mode` |
| Documento GKA atual | `GKA-000 — Parte V — Evolução Institucional` |
| Nova frente registrada | Enterprise Design & Business Specification |
| Produto em especificação | PAS-001 — Guivos Journey |
| Decisão estrutural registrada | GLPA — Guivos Layered Product Architecture |
| Estado da sincronização | Completed |
| Ponto de retomada | Continuar PAS-001 a partir da GLPA |

## 3. Decisões registradas desde GE2-SYNC-002

| ID | Decisão | Classificação | Status | Impacto |
|---|---|---|---|---|
| D-026 | Encerrar temporariamente o ciclo de meta-planejamento e iniciar especificação executável da Guivos | Método de trabalho | Aprovada | Alto |
| D-027 | Tratar a nova frente como `Enterprise Design & Business Specification` | Programa operacional | Aprovada | Alto |
| D-028 | Priorizar a arquitetura funcional dos produtos antes do modelo econômico detalhado | Sequenciamento | Aprovada | Alto |
| D-029 | Iniciar pela especificação oficial do Guivos Journey | Produto | Aprovada | Alto |
| D-030 | Utilizar `PAS — Product Architecture Specification` como formato inicial dos produtos | Método de produto | Aprovada | Alto |
| D-031 | Criar `PAS-001 — Guivos Journey` como primeira especificação de produto | Produto | Aprovada | Alto |
| D-032 | Definir o Journey como camada de experiência e orquestração do ecossistema, não como produto convencional equivalente aos demais | Arquitetura de produto | Aprovada | Alto |
| D-033 | Reconhecer `Guivos Intelligence` como camada transversal de inteligência do ecossistema | Arquitetura de produto | Aprovada | Alto |
| D-034 | Organizar Business, Mall, Travel, Media e Ads como camadas ou serviços especializados | Arquitetura de produto | Aprovada | Alto |
| D-035 | Registrar a `GLPA — Guivos Layered Product Architecture` como arquitetura de referência da nova fase | Arquitetura de produto | Aprovada | Alto |
| D-036 | Retomar o trabalho pelo PAS-001 a partir da consolidação da GLPA | Ponto de retomada | Aprovada | Alto |

## 4. Nova fase registrada

A Guivos entra em uma frente temporária de especificação executável denominada:

> **Enterprise Design & Business Specification**

Essa frente tem por objetivo transformar a arquitetura institucional já consolidada em especificações funcionais, operacionais, econômicas e comerciais suficientes para orientar Produto, UX, Engenharia, Comercial, Marketing e futuros investidores.

A frente não substitui a GE-2. Ela permanece subordinada à governança do GKR e deverá ser sincronizada com a GKA após a conclusão do GKA-000.

## 5. Backlog executivo aprovado

Ordem de trabalho acordada:

1. Arquitetura funcional dos produtos;
2. Guivos Economic Model;
3. Commercial Model;
4. Go-to-Market.

Ordem inicial dos produtos:

1. Guivos Journey;
2. Guivos Mall;
3. Guivos Business;
4. Guivos Intelligence;
5. Guivos Ads;
6. Guivos Media;
7. Guivos Travel.

## 6. PAS-001 — Guivos Journey

`PAS-001 — Guivos Journey` foi iniciado como especificação oficial do produto/camada de experiência.

### Estrutura inicial

1. Product Philosophy;
2. Visão do Produto;
3. Missão;
4. Objetivos Estratégicos;
5. Público-alvo;
6. Proposta de Valor;
7. Arquitetura Funcional;
8. Fluxos Operacionais;
9. Inteligência Artificial;
10. Integrações;
11. Modelo Econômico;
12. KPIs;
13. Roadmap.

### Princípios iniciais do Journey

- O usuário é protagonista da própria jornada;
- toda interação deve gerar valor perceptível;
- a inteligência deve reduzir esforço, não aumentar complexidade;
- recomendações devem ser contextualizadas e explicáveis;
- o sucesso é medido por impacto na vida real, não por tempo de tela;
- a experiência deve evoluir continuamente com o usuário.

## 7. GLPA — Guivos Layered Product Architecture

A GLPA registra que o Ecossistema Guivos não deve ser compreendido apenas como uma lista horizontal de produtos equivalentes.

A arquitetura funcional da plataforma passa a ser organizada por camadas:

```text
Guivos
  -> Experience Layer
       -> Guivos Journey
  -> Intelligence Layer
       -> Guivos Intelligence
  -> Service Layer
       -> Guivos Business
       -> Guivos Mall
       -> Guivos Travel
       -> Guivos Media
       -> Guivos Ads
  -> Platform Layer
       -> API, Graph, Auth, Billing, Search, AI, Notifications
```

## 8. Responsabilidades por camada

| Camada | Componente | Responsabilidade |
|---|---|---|
| Experience Layer | Guivos Journey | Experiência unificada do participante, orquestração, descoberta, objetivos, jornada e recomendações visíveis |
| Intelligence Layer | Guivos Intelligence | Interpretação contextual, recomendações, inteligência aplicada e aprendizagem transversal |
| Service Layer | Guivos Business | Relação com organizações e oportunidades institucionais |
| Service Layer | Guivos Mall | Produtos, serviços, compras, assinaturas e ativos comerciais |
| Service Layer | Guivos Travel | Viagens, experiências presenciais e reservas |
| Service Layer | Guivos Media | Conteúdo, histórias, formação e comunicação editorial |
| Service Layer | Guivos Ads | Publicidade, patrocínios, campanhas e ativações comerciais |
| Platform Layer | Capacidades comuns | API, autenticação, grafo, billing, busca, notificações, dados, segurança e infraestrutura |

## 9. Decisões de responsabilidade funcional

- Algoritmos de recomendação pertencem à Intelligence Layer.
- Telas e experiência visível pertencem à Experience Layer.
- Compras e transações pertencem ao Mall.
- Cadastro e gestão de organizações pertencem ao Business.
- Anúncios e mídia patrocinada pertencem ao Ads.
- Conteúdos editoriais pertencem ao Media.
- Reservas e experiências de viagem pertencem ao Travel.
- Capacidades técnicas compartilhadas pertencem à Platform Layer.

## 10. Organização institucional sugerida

A comunicação institucional poderá distinguir:

### Experiência

- Guivos Journey.

### Inteligência

- Guivos Intelligence.

### Soluções

- Guivos Business;
- Guivos Mall;
- Guivos Travel;
- Guivos Media;
- Guivos Ads.

Essa organização evita tratar componentes de naturezas distintas como produtos equivalentes.

## 11. Hipóteses e decisões preservadas

| ID | Hipótese ou decisão | Estado | Observação |
|---|---|---|---|
| H-GEF-001 | Entidades permanentes do Ecossistema Guivos tendem a evoluir preservando sua identidade enquanto ampliam progressivamente sua capacidade de cumprir seu propósito | Hipótese transversal | Não registrar como Canon neste momento |
| D-035 | GLPA como arquitetura em camadas da plataforma | Aprovada | Registrada para orientar PAS e Product Architecture |
| D-036 | Retomar PAS-001 a partir da GLPA | Aprovada | Ponto exato de retomada |

## 12. Documentos sincronizados

| Documento | Status |
|---|---|
| `docs/project/GE2-SYNC-003-enterprise-design-and-layered-product-architecture.md` | Criado |
| `docs/product-architecture/layered-product-architecture.md` | Criado |
| `docs/product-architecture/pas-001-guivos-journey.md` | Criado |
| `docs/product-architecture/index.md` | Atualizado |
| `docs/product-architecture/journey.md` | Atualizado |
| `README.md` | Atualizado |
| `docs/index.md` | Atualizado |
| `docs/project/knowledge-board.md` | Atualizado |
| `docs/roadmap.md` | Atualizado |
| `docs/project/architectural-milestones.md` | Atualizado |
| `docs/glossary.md` | Atualizado |
| `CHANGELOG.md` | Atualizado |
| `mkdocs.yml` | Atualizado |

## 13. Ponto exato de retomada

Retomar pela consolidação da `GLPA — Guivos Layered Product Architecture` dentro do `PAS-001 — Guivos Journey`.

Em seguida, continuar a arquitetura funcional completa do Journey antes de avançar para Modelo Econômico, Mall, Business, Ads, Media, Travel e Go-to-Market.

## 14. Regra de preservação

Esta matriz registra decisões de produto, operação e arquitetura funcional tomadas durante a nova frente de especificação executável. Ela não encerra a GKA, não publica o GKA-000, não altera a Canon da GE-2 e não autoriza a criação de `docs/knowledge-architecture/` antes da aprovação integral do GKA-000.