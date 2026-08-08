---
id: GKR-RESYNCHRONIZATION-BASELINE-2026-08-08-001
title: Baseline Governada de Ressincronização do Repositório — 2026-08-08
status: in-progress
version: 0.1.0
owner: Guivos
last_updated: 2026-08-08
related:
  - GKR-UPDATE-PROGRAM-001
  - GKR-STATE-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
  - GTM-000
  - GKR-LEGACY-NOMENCLATURE-RECONCILIATION-001
normative: false
---

# Baseline Governada de Ressincronização do Repositório — 2026-08-08

## 1. Finalidade

Este checkpoint reconcilia o programa controlado de atualização do Guivos Knowledge Repository com os avanços efetivamente integrados desde o inventário acumulado iniciado em agosto de 2026 e com os avanços validados que ainda precisam virar autoridade corrente.

Ele não declara o GKR completamente atualizado. Seu objetivo é separar quatro estados:

1. **integrado na `main`** — já faz parte da autoridade corrente;
2. **validado, mas ainda não integrado** — possui base suficiente para atualização governada;
3. **referência/plano** — orientação escolhida ou hipótese de arquitetura sem comprovação de implantação/operação;
4. **dependente de evidência** — não pode ser promovido a fato sem fonte operacional, jurídica, comercial, técnica ou empírica suficiente.

## 2. Baseline técnica do checkpoint

- repositório: `guivos-repositorio/Guivos-Knowledge-Repository`;
- branch-base: `main`;
- SHA-base: `9a0de25e664aab65b83c76ca5414c444dad893ae`;
- data: `2026-08-08`;
- programa de origem: `GKR-UPDATE-PROGRAM-001`;
- nenhuma alteração desta baseline autoriza implementação, operação, campanha, contratação, cobrança, investimento ou merge automático.

## 3. Avanços já incorporados após o inventário inicial

### 3.1 Arquitetura da experiência

A sequência UXA posterior ao checkpoint anterior avançou até UXA-101, incluindo:

- UXA-097 — compreensão inicial → primeira Tela Hoje;
- UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe;
- UXA-099 — validação dos dez estados residuais do Opportunity Boost;
- UXA-100/A1/A2/A3 — frente de Planos, Cobrança e Pagamentos, materialização, auditoria e promoção canônica;
- UXA-101 — revisão consciente e saída até `BND-001`.

O estado integrado preserva 118 SVGs canônicos, 118 associações, 31 perfis, 53 superfícies/estados/fronteiras e 54 transições. Engenharia de Produto permanece pausada e V5 não foi iniciada.

### 3.2 Taxonomia de planos e fronteira Organização × Business

A PR #207 consolidou a autoridade conceitual atual:

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`;
- Guivos Business: `Start · Growth · Scale · Enterprise`.

Regras:

- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- `BND-002` é fronteira genérica de contratação/dimensionamento assistido;
- plano representa capacidade/escopo/complexidade de serviço, não valor humano ou status.

### 3.3 Go-to-Market, crescimento, receita e valuation

As PRs #208 e #209 integraram o domínio GTM e seus horizontes de referência.

A autoridade corrente inclui, em condição de alvo candidato/cenário onde aplicável:

- sequência territorial `Belo Horizonte → São Paulo → Portugal`;
- Lisboa como primeira base internacional candidata; Porto posterior mediante gate;
- separação `Organização ≠ Parceria Estratégica`;
- Parceria Estratégica como relação corporativa da Guivos com contraparte externa;
- relação voltada diretamente a Pessoas/Coletivos classificada sob Organização quando exercer esse papel;
- parceria estratégica não exige receita direta e pode gerar alcance, escala, infraestrutura, tecnologia, integração, apoio, comunicação, acesso territorial ou capacidade;
- horizonte histórico de 1 milhão de Pessoas em cinco anos;
- targets M12/M36/M60 governados como candidatos/cenários, não promessas;
- valuation histórico candidato de R$ 10 milhões a R$ 15 milhões, com âncora interna de R$ 12 milhões;
- projeção econômica separada de realizado, contrato, faturamento e caixa.

## 4. Estado reconciliado do programa P0–P9

| Pacote | Estado em 2026-08-08 | Leitura governada | Próximo ato |
|---|---|---|---|
| P0 — intake/evidência | **concluído/reconstruído** | fontes acumuladas foram inventariadas e a retomada foi reconciliada com o repositório | preservar como evidência |
| P1 — ressincronização semântica | **concluído, com reforços posteriores** | taxonomia/UXA/GTM receberam novas autoridades depois do P1 original | não reabrir genericamente |
| P1.1 — nomenclaturas legadas | **em revisão** | PR #210 executa auditoria transversal e cria gate permanente | concluir gates e decidir integração separadamente |
| P2 — tecnologia e grafo | **validado como direção; não integrado como arquitetura de referência suficiente** | Neo4j foi escolhido como referência de grafo, mas implantação/provisionamento/produção não podem ser presumidos | criar arquitetura de referência e ADR/status claros |
| P3 — marca, naming, domínios e ativos | **parcialmente governado; pacote não fechado** | decisões e planos existem, mas registro/proteção/execução exigem evidência | auditoria temática e matriz de autoridade |
| P4 — validação de mercado | **método/instrumentos disponíveis; resultado real pendente** | metodologia B2C, métricas e gates podem ser consolidados; aceitação real exige dados | integrar método e preservar resultados como pendentes até evidência |
| P5 — institucional/Fundação/jurídico | **não consolidado** | hipóteses e modelos discutidos não equivalem a estrutura jurídica implementada | inventário + evidências antes de autoridade |
| P6 — verdade operacional, privacidade e superfícies legais | **dependente de evidência** | não declarar operação, textos legais, consentimentos ou conformidade que não estejam comprovados | intake operacional/jurídico específico |
| P7 — internacionalização | **parcialmente integrada pelo GTM** | Brasil→Portugal e gates territoriais existem; pacote completo ainda precisa reconciliação | consolidar estratégia internacional sem repetir GTM |
| P8 — Produtos Especializados | **arquitetura-base existente; ressincronização pendente** | sete Produtos Especializados estão definidos; PR #203 é anterior à autoridade atual e não deve ser integrada como está | reconstruir matriz Produto×Journey/Handoff contra a `main` atual |
| P9 — consolidação global/Public Canon | **bloqueado pelos pacotes anteriores** | estado corrente e material público ainda podem carregar versões anteriores | executar somente após P2–P8 relevantes |

## 5. Dívida transversal de nomenclatura

A auditoria P1.1 confirmou que a existência de uma autoridade nova não garante, por si só, que todos os derivados tenham sido atualizados.

Foram detectados resíduos de:

- nomes antigos de planos de Coletivo;
- antigos tiers Business usados como planos de Organização;
- interpretação antiga de `BND-002`;
- documentos de auditoria UXA ainda narrando taxonomia superseded;
- aliases de produto, como `Guivos Marketplace`, cujo nome oficial atual é `Guivos Mall`.

A correção está isolada na PR #210 para não contaminar os demais pacotes antes de validação.

## 6. Dívida de estado e Public Canon

O `GKR-STATE-001` continua sendo a autoridade transversal integrada, porém alguns números de versão de documentos derivados ficaram atrás das revisões mais recentes. Isso é uma dívida de sincronização documental, não evidência de que as decisões mais novas não existam.

O material público também não deve ser atualizado incrementalmente a cada conversa. A reconciliação do Public Canon pertence a P9 e deve ocorrer depois das autoridades temáticas, para evitar publicar conceitos provisórios ou contraditórios.

## 7. Produtos Especializados

A arquitetura oficial corrente reconhece sete Produtos Especializados:

1. Guivos Journey;
2. Guivos Mall;
3. Guivos Travel;
4. Guivos Business;
5. Guivos Media;
6. Guivos Intelligence;
7. Guivos Ads.

A ressincronização P8 deverá preservar:

- Journey como Experience Layer;
- Intelligence como Intelligence Layer;
- Business, Mall, Travel, Media e Ads como Service Layers;
- capacidades compartilhadas na Platform Layer;
- handoffs explícitos, sem transformar produtos em participantes;
- Organização ≠ Guivos Business;
- Business sem preço/entitlement inventado onde ainda não existe autoridade própria.

A antiga PR #203 é fonte de diagnóstico e trabalho intermediário, não candidata de merge direto após a mudança de autoridade.

## 8. Tecnologia e grafo

A direção validada permite documentar Neo4j como tecnologia de referência escolhida para a arquitetura de grafo da Guivos, mas exige separação rigorosa entre:

```text
referência escolhida
≠ POC
≠ provisionado
≠ integrado
≠ produção
```

P2 deverá relacionar grafo, Guivos Intelligence, Graph Analytics, GraphRAG e consumo analítico sem inventar provedor, região, tier, SLA, volume, custo, backup, residência, latência ou estado de implantação.

## 9. Ordem de atualização a partir deste checkpoint

A ordem governada recomendada é:

```text
P1.1 — fechar deriva de nomenclatura
→ P2 — arquitetura tecnológica/grafo
→ P8 — rebaseline dos Produtos Especializados
→ P3 — marca/naming/domínios/ativos
→ P4 — validação de mercado
→ P5 — institucional/Fundação/jurídico
→ P6 — verdade operacional/legal/privacidade
→ P7 — reconciliação internacional
→ P9 — estado global, navegação e Public Canon
```

P2 e P8 podem ser preparados em PRs draft independentes enquanto P1.1 passa pelos gates, desde que não incorporem nomenclatura obsoleta e não sejam mesclados antes da reconciliação necessária.

## 10. Princípios de ressincronização

1. conversa validada não é automaticamente fato operacional;
2. plano não é execução;
3. arquitetura de referência não é implantação;
4. preço candidato não é disposição a pagar;
5. projeção não é realizado;
6. valuation interno não é oferta nem valor contábil;
7. registro de domínio não é proteção global sem evidência;
8. hipótese societária não é estrutura jurídica constituída;
9. nomenclatura antiga pode permanecer somente como histórico/migração claramente identificado;
10. autoridade mais recente prevalece sobre derivados obsoletos;
11. PR antiga não deve ser mesclada quando sua base conceitual foi superseded;
12. cada pacote possui gate próprio e decisão de merge própria.

## 11. Critério de encerramento da ressincronização ampla

O programa somente poderá ser considerado encerrado quando:

- os pacotes aplicáveis P2–P8 forem reconciliados ou explicitamente classificados como dependentes de evidência;
- nomenclaturas vigentes estiverem sincronizadas;
- `GKR-STATE-001` refletir as autoridades temáticas finais;
- navegação e índices não apontarem para autoridade superseded como corrente;
- Public Canon for reconstruído a partir da autoridade consolidada;
- gates mecânicos e semânticos passarem;
- nenhuma lacuna empírica/operacional for promovida silenciosamente a fato.

Este checkpoint inicia a nova fase de atualização, mas não a declara concluída.
