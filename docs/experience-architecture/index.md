---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.95.0
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

A UXA-101 reformula e revalida o SVG canônico do Detalhe de Oportunidade sem alterar as contagens.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional por padrão;
- uma versão visual reformulada exige validação correspondente;
- publicação ou ativação não equivale a distribuição garantida;
- plano pago não altera relevância, confiança, legitimidade, impacto ou evolução;
- oportunidade pública não é ocultada para vender plano;
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
```

## 6. Resultado da UXA-101

[UXA-101 — Validação da Saída Consciente para Fronteira Externa](uxa-101-conscious-external-boundary-validation.md) encerra V4 no limite controlável pela Guivos.

A frente consolida:

1. revisão pré-saída como estado de `PER-203`, sem novo ID;
2. reformulação e revalidação de `uxa-007-opportunity-detail-mobile.svg`;
3. identificação de destino externo e responsável;
4. disclosure proporcional de dados/contexto;
5. confirmação afirmativa e revalidação do destino;
6. bloqueio de redirecionamento silencioso quando o destino não puder ser confirmado;
7. retorno seguro sem presumir efeito externo;
8. `TRN-205` integralmente validada até `BND-001`;
9. `BND-001` examinada como fronteira sem tela Guivos;
10. nenhuma atribuição de inscrição, compra, reserva ou contratação externa à Guivos.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active` 0.32.0 |
| Jornada da Pessoa | `draft` 0.15.0 |
| Jornada do Coletivo | `draft` 0.16.0 |
| Jornada da Organização | `draft` 0.9.0 |
| catálogo integrado | `active` 0.27.0 |
| galeria visual | `active` 0.21.0 |
| galeria de Planos | `active` 0.3.0 |
| matriz por SVG | `active` 0.17.0 |
| lacunas | `active` 0.27.0 |
| registro de superfícies | `active` 0.17.0 |
| registro de transições | `active` 0.18.0 |
| detalhamento comercial/fronteira | `active` 0.5.0 |

## 8. Ressalvas vigentes

- 9 responsabilidades permanecem sem SVG dedicado;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` permanecem parciais;
- `TRN-304`, `TRN-305` e `TRN-306` permanecem parciais na integração patrocinada;
- `TRN-416/426` permanecem parciais;
- gateway, cobrança real, proration e processo de contratação/dimensionamento assistido após `BND-002` permanecem fora do escopo;
- processo externo após `BND-001` permanece sob autoridade de terceiro;
- Jornadas da Pessoa, Coletivo e Organização continuam `draft`.

## 9. Fila global preservada

```text
V1 — encerrada pela UXA-097
→ V2 — encerrada pela UXA-098
→ V3 — encerrada pela UXA-099
→ Planos — identidade canônica encerrada pela UXA-100-A3
→ V4 — encerrada pela UXA-101 até BND-001
→ V5 — pendente e não iniciada
```

## 10. Próxima evolução possível

V5, cobrança real, contratação/dimensionamento assistido após `BND-002` e demais validações exigem autorização separada. A auditoria transversal dos Produtos Especializados pode ocorrer como diagnóstico sem iniciar nova UXA ou Engenharia de Produto.
