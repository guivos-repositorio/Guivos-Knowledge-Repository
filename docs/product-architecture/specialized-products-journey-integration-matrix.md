---
id: GPA-SPECIALIZED-JOURNEY-MATRIX-001
title: Matriz de Integração dos Produtos com as Jornadas
status: consolidated
version: 1.0.1
owner: Guivos
last_updated: 2026-08-08
related:
  - GPA-000
  - GLPA-001
  - GPA-001
  - GPA-002
  - GPA-003
  - GPA-004
  - GPA-005
  - GPA-006
  - GPA-007
  - PAS-001
  - PAS-001-OA-INTEGRATION-001
  - UXA-101
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GPA-SPECIALIZED-EXPERIENCE-POLICY-001
---

# Matriz de Integração dos Produtos com as Jornadas

## 1. Finalidade

Esta matriz liga a Arquitetura de Produtos da Guivos à Arquitetura da Experiência sem transformar nomes de produtos em telas artificiais.

Ela responde, para cada componente oficial, quatro perguntas:

1. qual responsabilidade arquitetural o produto possui;
2. onde essa responsabilidade já aparece nas jornadas canônicas;
3. quando existe um handoff interno entre produtos;
4. quais integrações continuam apenas conceituais ou incompletas.

A matriz usa somente autoridades integradas à `main` na data desta edição, incluindo a UXA-101 e sua validação da saída consciente até `BND-001`. PRs em rascunho ou ainda não mescladas não alteram este baseline.

## 2. Autoridade e limites

A hierarquia usada nesta matriz é:

1. `GLPA-001` define as camadas e responsabilidades permanentes;
2. `GPA-001` a `GPA-007` definem os sete componentes oficiais;
3. `PAS-001` e seus contratos definem capacidades funcionais do Journey;
4. registros de superfícies, transições e rastreabilidade definem o que já foi materializado ou validado na experiência;
5. esta matriz reconcilia as quatro camadas acima, sem promover maturidade por associação.

Mapeamento não equivale a validação. Um produto pode ser o responsável arquitetural por uma capacidade sem que a transição ou a superfície correspondente esteja validada ponta a ponta.

## 3. Vocabulário de integração

| Termo | Definição |
|---|---|
| host de experiência | componente que organiza a interação visível e o controle apresentado ao participante |
| responsável especializado | produto cuja responsabilidade de negócio domina naquele contexto |
| produto de apoio | componente que fornece inteligência, conteúdo, mídia ou outra capacidade sem assumir a decisão principal da superfície |
| handoff interno | passagem material de responsabilidade entre dois componentes da própria Guivos |
| fronteira externa | passagem para autoridade de terceiro fora do Ecossistema Guivos |
| suporte implícito | capacidade interna que não exige mudança de tela nem identificação permanente do produto |
| integração conceitual | relação arquitetural prevista, ainda sem superfície ou transição canônica suficiente |

## 4. Baseline dos sete componentes

| Componente | Camada | Papel na experiência atual | Evidência canônica principal | Estado de integração com jornadas |
|---|---|---|---|---|
| Guivos Journey | Experience Layer | host e orquestrador da experiência unificada | famílias `PER-*` e `COL-*`; integração com oportunidades, organizações, planos e coletivos | forte e amplamente materializada |
| Guivos Intelligence | Intelligence Layer | apoio transversal de interpretação, personalização, análise e explicabilidade | compreensão inicial, Tela Hoje, oportunidades e mensuração; sem navegação própria obrigatória | forte, porém majoritariamente implícita |
| Guivos Business | Service Layer | responsabilidade especializada por organizações, B2B e relações institucionais | `ORG-001..007`, `ORG-301..304`, relação institucional `COL-008`; `TRN-203` conecta publicação à descoberta | materializada parcialmente e pouco identificada como produto |
| Guivos Mall | Service Layer | comércio de produtos, serviços e ativos transacionáveis | nenhuma família `SURF` ou `TRN` dedicada no registro vigente | integração conceitual; materialização ausente |
| Guivos Travel | Service Layer | viagens, roteiros, experiências e reservas | nenhuma família `SURF` ou `TRN` dedicada no registro vigente | integração conceitual; materialização ausente |
| Guivos Media | Service Layer | conteúdo editorial e institucional | conteúdo pode ser consumido dentro do Journey, mas não há superfície canônica própria atribuída a Media | integração conceitual/embutida; responsabilidade visual não consolidada |
| Guivos Ads | Service Layer | publicidade e distribuição patrocinada identificada | `COM-001..005`; 46 SVGs de Opportunity Boost; transições `TRN-301..306` | forte materialização; integração orgânico–patrocinado ainda parcial |

## 5. Matriz participante × etapa × produto

| Participante / etapa | Host de experiência | Responsável especializado dominante | Apoios relevantes | Evidência atual | Situação |
|---|---|---|---|---|---|
| Pessoa — entrada, compreensão e Hoje | Journey | Journey | Intelligence; Platform | `PER-001..008`, `TRN-001..007` | materializada |
| Pessoa — explorar oportunidades | Journey | Journey | Intelligence; Business como origem possível; Ads quando patrocinado | `PER-201..203`, `TRN-203/204/210/211` e `COM-002/003` | materializada, com handoffs parciais de Ads |
| Pessoa — coletivos e participação | Journey | Journey | Business somente quando houver relação institucional | `PER-101..108`, `COL-001..008` | materializada em parte |
| Pessoa — planos | Journey | Journey | Platform/Billing | `PER-301..304`, `TRN-401..405` | materializada localmente |
| Coletivo — presença e gestão | Journey | Journey | Business nas relações institucionais | `COL-001..008` | materializada em parte |
| Coletivo — planos | Journey | Journey | Business no processo comercial Enterprise quando aplicável; Platform/Billing | `COL-301..304`, `TRN-411..416`, `BND-002` | materializada localmente; Enterprise parcial |
| Organização — visão e publicação de oportunidades | experiência Guivos integrada | Business | Journey; Intelligence; Platform | `ORG-001..003`, `TRN-201..203` | materializada; `TRN-203` integralmente validada |
| Organização — relações com Coletivos | experiência Guivos integrada | Business | Journey | `ORG-004..006`, `COL-008`, `TRN-206..209` | contratada, não materializada suficientemente |
| Organização — planos | experiência Guivos integrada | Business | Journey; Platform/Billing | `ORG-301..304`, `TRN-421..426`, `BND-002` | materializada localmente; Scale parcial |
| Anunciante — Opportunity Boost | experiência Guivos integrada | Ads | Business para identidade institucional; Intelligence para mensuração permitida; Journey como contexto de exposição | `COM-001..005`, `TRN-301..306` | fortemente materializada; continuidade orgânica parcial |
| Pessoa — compra de produto/serviço | a definir no handoff | Mall | Journey; Intelligence; Platform/Billing | sem `SURF/TRN` dedicado | lacuna |
| Pessoa — planejamento/reserva de viagem | a definir no handoff | Travel | Journey; Intelligence; Media; Platform | sem `SURF/TRN` dedicado | lacuna |
| Pessoa — experiência editorial própria | Journey quando embutida; Media se contexto independente | Media | Journey; Intelligence; Ads quando patrocinado | sem família canônica própria | lacuna de responsabilidade visual |

## 6. Handoffs internos já identificáveis

| Origem de responsabilidade | Destino de responsabilidade | Evidência | Estado | Leitura de produto |
|---|---|---|---|---|
| Business / publicação institucional | Journey / descoberta por Pessoas | `GKR-TRN-203` | integralmente validada | handoff interno já comprovado documentalmente |
| Ads / exposição patrocinada | Journey / mapa orgânico | `GKR-TRN-304` | parcial | handoff interno conhecido, ainda não validado como conjunto |
| Ads / exposição patrocinada | Journey / lista orgânica | `GKR-TRN-306` | parcial | handoff interno conhecido, ainda não validado como conjunto |
| Ads / campanha ativa | Ads / estado residual | `GKR-TRN-305` | parcial | destino `COM-005` validado; ligação completa ainda parcial |
| Journey | Mall | nenhuma transição canônica dedicada | ausente | integração prevista pela GLPA, ainda não materializada |
| Journey | Travel | nenhuma transição canônica dedicada | ausente | integração prevista pela GLPA, ainda não materializada |
| Media | Journey | relação arquitetural de conteúdo | conceitual | conteúdo pode ser embutido sem exigir handoff navegacional |
| Intelligence | demais produtos | relação de serviço transversal | não navegacional | não deve virar `TRN` apenas por uso de inteligência |

## 7. Fronteira externa não é handoff interno

`GKR-SURF-BND-001` representa uma autoridade externa ao Ecossistema Guivos.

Consequentemente:

- Journey → Mall não usa `BND-001` quando Mall permanece sob autoridade Guivos;
- Journey → Travel não usa `BND-001` quando Travel permanece sob autoridade Guivos;
- Business → Journey e Ads → Journey são handoffs internos;
- somente a passagem para um terceiro com autoridade própria deve ser tratada como fronteira externa.

Na baseline vigente, a UXA-101 valida integralmente `GKR-TRN-205` no trecho controlável `PER-203 → BND-001`, incluindo revisão consciente, destino, responsabilidade, dados/contexto, retorno e falha segura. Essa validação não inclui nem presume o processo, resultado ou confirmação executados pelo sistema do terceiro após a fronteira.

## 8. Registro de gaps de integração

| Gap | Descrição | Produto(s) | Tratamento correto |
|---|---|---|---|
| SP-GAP-001 | Journey → Mall sem contrato canônico de entrada, autoridade, dados, retorno e recuperação | Journey, Mall | UXA futura antes de criar novas telas/transições |
| SP-GAP-002 | Journey → Travel sem contrato canônico de planejamento/reserva e retorno | Journey, Travel | UXA futura antes de materialização |
| SP-GAP-003 | Media sem regra consolidada para distinguir conteúdo embutido de contexto editorial próprio | Journey, Media | aplicar política de representação e depois decidir necessidade de UXA |
| SP-GAP-004 | superfícies de Organização não registram diretamente a responsabilidade de Business | Business, Journey | esta matriz passa a fornecer a rastreabilidade de produto sem alterar IDs existentes |
| SP-GAP-005 | Intelligence participa de decisões importantes sem taxonomia uniforme de proveniência/explicabilidade por superfície | Intelligence, Journey | aplicar política; materializar somente onde a explicação for material |
| SP-GAP-006 | página de Guivos Ads declarava design/validação pendentes apesar da materialização de Opportunity Boost | Ads | corrigido no rebaseline desta frente |
| SP-GAP-007 | registros `SURF/TRN` não possuem coluna nativa de produto responsável | todos | usar esta matriz como ponte; alterar registros somente se uma frente futura justificar mudança de schema |
| SP-GAP-008 | diferença entre handoff interno e fronteira externa não estava consolidada em política única de produto | todos | resolvido por `GPA-SPECIALIZED-EXPERIENCE-POLICY-001` |

## 9. Regra de leitura

Uma superfície não recebe um novo ID só porque outro produto passou a apoiá-la.

Uma nova superfície ou transição só deve ser proposta quando houver mudança material de hierarquia, decisão primária, autoridade, visibilidade, dados, consequência, risco, navegação, canal ou recuperação. A mudança de produto responsável é um sinal para análise, não uma justificativa automática para fragmentação.

## 10. Resultado desta consolidação

Esta matriz:

- torna explícita a responsabilidade dos sete componentes sobre jornadas já existentes;
- diferencia produto responsável, produto de apoio e host de experiência;
- identifica handoffs internos já existentes e lacunas reais;
- reconhece a UXA-101 como autoridade vigente da saída consciente para `BND-001` sem converter fronteira externa em handoff interno;
- não cria novos `SURF`, `TRN` ou SVGs;
- não inicia UXA posterior;
- não inicia Engenharia de Produto;
- não transforma integração conceitual de Mall, Travel ou Media em implementação ou validação.

A regra operacional complementar está em [Política de Representação e Handoffs entre Produtos](specialized-products-experience-and-handoff-policy.md).
