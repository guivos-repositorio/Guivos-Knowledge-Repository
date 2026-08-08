---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.93.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - PAS-001
  - GLPA-001
  - UXA-001
  - UXA-055
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-069
  - UXA-070
  - UXA-080
  - UXA-085
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-097
  - UXA-098
  - UXA-099
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.87
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos em experiências compreensíveis para Pessoas, Coletivos e Organizações. Ela governa hierarquia, decisão, continuidade, confirmação, autoridade, privacidade e proteção antes de design final ou implementação.

## 2. Regra de maturidade

```text
contrato funcional
→ programa governado
→ materialização
→ validação funcional
→ reformulação quando exigida
→ revalidação
→ promoção controlada quando aplicável
→ inspeção integrada
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs canônicos | **118** |
| associações individuais | **118** |
| perfis de rastreabilidade | **31** |
| com validação funcional vigente | **118** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **53** |
| transições documentais | **54** |
| IDs com referência visual | **42 de 53** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela | **2** |

A UXA-100-A3 incorpora os nove SVGs de Planos já validados pela UXA-100-A2 e cria identidade canônica para doze superfícies, uma fronteira comercial e dezessete transições.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional por padrão;
- uma versão visual reformulada exige validação correspondente;
- publicação ou ativação não equivale a distribuição garantida;
- plano pago não altera relevância, confiança, legitimidade, impacto ou evolução;
- oportunidade pública não é ocultada para vender plano;
- comparação incremental não cria tela própria quando preserva hierarquia/decisão de Planos;
- processamento financeiro transitório não cria superfície própria;
- Enterprise/Scale termina em fronteira comercial, não em checkout fictício;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- validação de superfície não equivale a validação automática de transição;
- validação documental não equivale a implementação técnica.

## 5. Evolução recente

```text
UXA-090 — cinco handoffs elegíveis validados
→ UXA-091 — Meus Coletivos materializada
→ UXA-092 — Meus Coletivos e TRN-108 validados
→ UXA-093 — Central materializada
→ UXA-094 — Central e TRN-110 validadas
→ UXA-095 — Início do Participante materializado; TRN-111 parcial
→ UXA-096 — Central/Início revalidados e TRN-111 validadas ponta a ponta
→ UXA-097 — primeira Hoje materializada; PER-007 revalidada; TRN-007 validada ponta a ponta
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe validados
→ UXA-099 — dez estados residuais Opportunity Boost validados
→ UXA-100/A1 — Planos materializados e inseridos nas três jornadas
→ UXA-100-A2 — 9/9 SVGs de Planos aprovados após 6 reformas controladas
→ UXA-100-A3 — fragmentação mínima e promoção canônica de Planos
```

## 6. Resultado da UXA-100

[UXA-100 — Planos, Cobrança e Pagamentos](uxa-100-plans-billing-payments-functional-program-and-initial-materialization.md) estrutura a frente transversal.

A UXA-100-A3 consolida:

1. quatro famílias canônicas por participante: `*-301` a `*-304`;
2. `BND-002` como fronteira compartilhada Enterprise/Scale;
3. comparação geral e incremental em `*-301`;
4. revisão pré-contratual em `*-302`;
5. downgrade/cancelamento em `*-303`;
6. sucesso/falha e recuperação em `*-304`;
7. 15 transições internas localmente validadas;
8. `TRN-416` e `TRN-426` parciais até processo comercial posterior;
9. 9 SVGs promovidos ao catálogo canônico, perfis R29–R31;
10. jornadas principais preservadas em `draft`.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active` 0.30.0 |
| Jornada da Pessoa | `draft` 0.14.0 |
| Jornada do Coletivo | `draft` 0.15.0 |
| Jornada da Organização | `draft` 0.7.0 |
| catálogo integrado | `active` 0.25.0 |
| galeria visual | `active` 0.20.0 |
| galeria de Planos | `active` 0.3.0 |
| matriz por SVG | `active` 0.16.0 |
| lacunas | `active` 0.25.0 |
| registro de superfícies | `active` 0.16.0 |
| registro de transições | `active` 0.17.0 |
| detalhamento da Pessoa | `active` 0.10.0 |
| detalhamento do Coletivo | `active` 0.7.0 |
| detalhamento da Organização | `active` 0.3.0 |
| detalhamento comercial/fronteira | `active` 0.4.0 |

## 8. Ressalvas vigentes

- 9 responsabilidades permanecem sem SVG dedicado;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` permanecem parciais;
- `TRN-205` permanece parcial para efeito externo;
- `TRN-304`, `TRN-305` e `TRN-306` permanecem parciais na integração patrocinada;
- transições de Planos são locais; `TRN-416/426` permanecem parciais;
- gateway, cobrança real, proration e processo comercial após `BND-002` permanecem fora do escopo;
- estados P0B e áreas P1 permanecem separados;
- Jornadas da Pessoa, Coletivo e Organização continuam `draft`.

## 9. Fila global preservada

```text
V1 — compreensão inicial → Tela Hoje — encerrada pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — encerrada pela UXA-098
→ V3 — dez estados residuais UXA-055 — encerrada pela UXA-099
→ Planos — identidade canônica encerrada pela UXA-100-A3
→ V4 — efeito externo de oportunidades — prioridade global ainda pendente
→ V5 — erros, retornos e interrupções
```

A frente de Planos foi autorizada fora da ordem da fila global sem cancelar V4/V5.

## 10. Próxima evolução possível

A identidade canônica da UXA-100 está concluída documentalmente. Cobrança real, processo comercial Enterprise/Scale e validações ponta a ponta adicionais exigem autorização separada. Nenhuma próxima UXA ou Engenharia de Produto é iniciada automaticamente.