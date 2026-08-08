---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.26.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-07
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
  - GPA-007
  - UXA-000
  - UXA-055
  - UXA-056
  - UXA-058
  - UXA-059
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - ROADMAP-12.73.0
  - M7.87
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global proposto quando o incremento correspondente estiver integrado ao ramo principal. Enquanto a PR #200 permanecer fora da `main`, a autoridade vigente da `main` continua no commit integrado anterior. Em caso de divergência após integração, este registro prevalece sobre resumos não normativos.

## 2. Estado global proposto pela UXA-100-A3

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | Planos fragmentados e promovidos canonicamente | UXA-100-A3; M7.87 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | **53 superfícies/estados/fronteiras e 54 transições** | UXA-100-A3 |
| Galeria visual | `active` 0.20.0; **118 SVGs** | UXA-100-A3 |
| Matriz por SVG | `active` 0.16.0; **118 arquivos / 31 perfis** | UXA-100-A3 |
| Jornadas Integradas | `active` 0.30.0; Pessoa, Coletivo e Organização em `draft` | UXA-100-A3 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **118** |
| associações individuais | **118** |
| perfis de rastreabilidade | **31** |
| com validação funcional vigente | **118** |
| pendentes de validação específica | **0** |
| IDs granulares com referência visual | **42 de 53** |
| responsabilidades sem SVG dedicado | **9** |
| fronteiras sem tela por definição | **2** |

A UXA-100-A3 promove os nove SVGs de Planos previamente aprovados pela UXA-100-A2, sem criar novos arquivos visuais nesta subetapa.

## 4. Resultado da UXA-100

A frente UXA-100:

- materializa tela de Planos, board de fluxo e comparação incremental para Pessoa, Coletivo e Organização;
- integra Planos às três jornadas `draft`;
- valida funcionalmente 9/9 SVGs, com seis reformas controladas;
- promove os nove ativos ao conjunto canônico;
- cria quatro famílias canônicas por participante: Planos/comparação, revisão de contratação, downgrade/cancelamento e resultado/recuperação;
- cria `BND-002` como fronteira documental Enterprise/Scale;
- registra 17 novas transições com maturidade explícita;
- preserva oportunidade pública no Free;
- preserva separação entre assinatura, transação, comissão, taxa e tributo;
- não implementa cobrança, gateway ou entitlement.

Veredito:

> **Fragmentação mínima e promoção canônica aprovadas documentalmente: 12 superfícies de Planos, uma fronteira comercial, 17 transições e nove SVGs incorporados ao catálogo canônico.**

## 5. Estrutura canônica de Planos

### Pessoa

`PER-301` a `PER-304`; `TRN-401` a `TRN-405` localmente validadas.

### Coletivo

`COL-301` a `COL-304`; `TRN-411` a `TRN-415` localmente validadas; `TRN-416` parcial para `BND-002`.

### Organização

`ORG-301` a `ORG-304`; `TRN-421` a `TRN-425` localmente validadas; `TRN-426` parcial para `BND-002`.

Comparação incremental permanece em `*-301`; processamento financeiro permanece transitório; sucesso e falha pertencem a `*-304` como estados diferentes da mesma responsabilidade.

## 6. Proteções da frente

- oportunidade pública não é ocultada para vender plano;
- Guivos Free mantém utilidade real e catálogo público;
- plano pago não compra relevância, confiança, legitimidade, impacto ou evolução;
- preço de assinatura não se confunde com preço de oportunidade, comissão, taxa ou tributo;
- nenhuma opção paga é pré-selecionada;
- downgrade/cancelamento mostra consequência e data aplicável;
- falha não presume ativação nem permite perda silenciosa de dados;
- Enterprise/Scale termina em `BND-002`, sem checkout fictício;
- trial com conversão automática continua fora da baseline;
- pró-rata, grace period e regras fiscais finais permanecem indefinidos.

## 7. Continuidades anteriores preservadas

- `TRN-203`, `TRN-204`, `TRN-210` e `TRN-211` permanecem integralmente validadas pela UXA-098;
- `TRN-007` permanece integralmente validada pela UXA-097;
- `COM-005` permanece funcionalmente validado pela UXA-099;
- oito transições do trecho governado de Coletivos permanecem integralmente validadas: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`;
- `TRN-205`, `TRN-304`, `TRN-305` e `TRN-306` permanecem parciais e fora do escopo da promoção de Planos.

## 8. Dívidas preservadas

- estados P0B de Meus Coletivos, Central e Início do Participante;
- canais P1 e operação interna especializada;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` parciais;
- `TRN-205` efeito externo de oportunidades;
- `TRN-304`, `TRN-305` e `TRN-306` integrações patrocinadas pendentes;
- cobrança real e gateway da frente de Planos;
- processo comercial posterior a `BND-002`;
- entradas de Planos a partir de origens ainda sem identidade canônica adequada;
- relação Organização–Coletivo ainda não materializada como conjunto.

## 9. Fila global de validação

| Ordem | Continuidade ou família | Estado |
|---:|---|---|
| V1 | compreensão inicial → Tela Hoje | encerrada por UXA-097 |
| V2 | publicação → descoberta/mapa/lista/detalhe | encerrada por UXA-098 |
| V3 | dez estados residuais UXA-055 | encerrada por UXA-099 |
| Planos | identidade e promoção canônica | **encerrada por UXA-100-A3** |
| V4 | efeito externo de oportunidades | prioridade global preservada; pendente |
| V5 | erros, retornos e interrupções | pendente |

A frente de Planos foi autorizada separadamente e não cancela V4/V5.

## 10. Estado documental proposto

| Camada | Estado |
|---|---|
| Arquitetura da Experiência | `active` 0.93.0 |
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
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 11. Preservações

- materialização, validação, promoção e implementação são estados distintos;
- uma versão visual reformulada exige validação correspondente;
- publicação não é distribuição garantida;
- relação comercial não compra relevância funcional;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- validação local não equivale a transição ponta a ponta;
- Pessoa, Coletivo e Organização permanecem `draft`;
- nenhuma etapa autoriza automaticamente a seguinte.

## 12. Próxima transição autorizável

Com a identidade canônica de Planos encerrada pela UXA-100-A3, qualquer próximo ato — integração da PR, cobrança real, processo Enterprise/Scale, V4 ou outra frente — exige autorização humana separada. **UXA-101 não foi iniciada.**