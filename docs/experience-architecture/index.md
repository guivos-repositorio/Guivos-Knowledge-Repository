---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.96.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
related:
  - PAS-001
  - GLPA-001
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
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
  - UXA-100-A4
  - UXA-101
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.88
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

## 3. Cobertura visual e granular

| Indicador | Resultado |
|---|---:|
| SVGs canônicos | **118** |
| associações individuais | **118** |
| perfis de rastreabilidade | **31** |
| com validação funcional vigente | **118** |
| pendentes de validação específica | **0** |
| superfícies/estados/fronteiras | **54** |
| transições documentais | **60** |
| IDs com referência visual | **42 de 54** |
| responsabilidades sem SVG dedicado | **10** |
| fronteiras sem tela | **2** |

A UXA-100-A4 adiciona somente `PER-009` como responsabilidade sem SVG e seis handoffs de navegação; os 118 ativos visuais permanecem em quantidade constante.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional por padrão;
- uma versão visual reformulada exige validação correspondente;
- publicação ou ativação não equivale a distribuição garantida;
- plano pago não altera relevância, confiança, legitimidade, impacto ou evolução;
- oportunidade pública não é ocultada para vender plano;
- navegar para Planos não equivale a escolher plano ou iniciar cobrança;
- Pessoa utiliza `Free · Plus · Pro`;
- Coletivo utiliza `Livre · Mobiliza · Impacta · Rede`;
- Organização utiliza `Conecta · Eleva · Transforma`;
- Guivos Business utiliza `Start · Growth · Scale · Enterprise` como Produto Especializado separado;
- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- `BND-002` representa contratação/dimensionamento assistido quando o autoatendimento não for suficiente e não pertence semanticamente a plano específico;
- estado intermediário não cria superfície própria quando preserva responsabilidade, autoridade e decisão principal;
- fronteira externa não é tela da Guivos;
- validação até uma fronteira não valida comportamento de terceiro;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- validação documental não equivale a implementação técnica.

## 5. Evolução recente

```text
UXA-097 — primeira Hoje e TRN-007
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe
→ UXA-099 — dez estados residuais Opportunity Boost
→ UXA-100/A1/A2/A3 — Planos nas três jornadas e promoção canônica
→ UXA-101 — revisão consciente de saída e TRN-205 até BND-001
→ UXA-100-A4 — reconciliação das origens administrativas de Planos
```

A UXA-100-A4 é uma subfrente da UXA-100 e não altera a última frente funcional numerada: UXA-101 continua vigente e UXA-102/V5 permanece não iniciada.

## 6. Resultado da UXA-100-A4

[UXA-100-A4 — Origens Administrativas e Handoffs de Entrada em Planos](uxa-100-a4-plans-entry-origin-and-navigation-handoffs.md) consolida:

1. `PER-009 — Conta e configurações da Pessoa`, sem SVG dedicado;
2. `TRN-406/407` contratadas entre `PER-009` e `PER-301`;
3. `TRN-417/418` integralmente validadas entre `COL-002` e `COL-301`;
4. `TRN-427/428` integralmente validadas entre `ORG-001` e `ORG-301`;
5. navegação de `COL-002` reformulada in-place para explicitar Planos;
6. `ORG-001` reformulada in-place, removendo o rótulo obsoleto `Guivos Business` e explicitando Planos;
7. retorno explícito às origens em `COL-301` e `ORG-301`;
8. 118 SVGs e 31 perfis preservados;
9. nenhuma alteração de maturidade em `TRN-401..405`, `TRN-411..416` ou `TRN-421..426`;
10. nenhuma implementação de cobrança, entitlement, `BND-002`, V5 ou Engenharia de Produto.

## 7. Resultado da UXA-101 preservado

[UXA-101 — Validação da Saída Consciente para Fronteira Externa](uxa-101-conscious-external-boundary-validation.md) continua encerrando V4 no limite controlável pela Guivos.

A frente consolida revisão pré-saída em `PER-203`, identificação do destino externo, minimização de dados/contexto, confirmação afirmativa, revalidação, bloqueio de redirecionamento inválido, retorno seguro e `TRN-205` validada até `BND-001`.

## 8. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active` 0.33.0 |
| Jornada da Pessoa | `draft` 0.16.0 |
| Jornada do Coletivo | `draft` 0.17.0 |
| Jornada da Organização | `draft` 0.10.0 |
| catálogo integrado | `active` 0.28.0 |
| galeria visual | `active` 0.22.0 |
| galeria de Planos | `active` 0.5.0 |
| matriz por SVG | `active`; 118 associações / 31 perfis |
| lacunas | `active` 0.28.0 |
| registro de superfícies | `active` 0.19.0 |
| registro de transições | `active` 0.20.0 |
| detalhamento comercial/fronteira | `active` |

## 9. Ressalvas vigentes

- 10 responsabilidades permanecem sem SVG dedicado, incluindo `PER-009`;
- `TRN-406/407` permanecem contratadas até materialização suficiente de Conta;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` permanecem parciais;
- `TRN-304`, `TRN-305` e `TRN-306` permanecem parciais na integração patrocinada;
- `TRN-416/426` permanecem parciais;
- gateway, cobrança real, proration e processo de contratação/dimensionamento assistido após `BND-002` permanecem fora do escopo;
- processo externo após `BND-001` permanece sob autoridade de terceiro;
- Jornadas da Pessoa, Coletivo e Organização continuam `draft`.

## 10. Fila global preservada

```text
V1 — encerrada pela UXA-097
→ V2 — encerrada pela UXA-098
→ V3 — encerrada pela UXA-099
→ Planos — identidade canônica encerrada pela UXA-100-A3
→ V4 — encerrada pela UXA-101 até BND-001
→ Planos — origem voluntária reconciliada pela UXA-100-A4
→ V5 — pendente e não iniciada
```

## 11. Próxima evolução possível

Materialização de `PER-009`, V5/UXA-102, cobrança real, contratação/dimensionamento assistido após `BND-002` e demais validações exigem autorização separada. Nenhuma delas é iniciada automaticamente por esta reconciliação.
