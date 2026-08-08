---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.27.1
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-08
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
  - GPA-004
  - GPA-007
  - GEM-004-A1
  - GEM-007-BUSINESS-ECONOMIC-ROLE-001
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
  - UXA-101
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - ROADMAP-12.74.1
  - M7.88
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global proposto após a UXA-101 e o **patch documental de sincronização da taxonomia global de planos**. Em caso de divergência após integração governada, este registro prevalece sobre resumos não normativos.

O patch 2.27.1 não cria UXA, não cria marco, não promove maturidade e não inicia nova frente. `UXA-101` continua sendo a última UXA integrada/proposta da sequência e `M7.88` permanece o marco vigente.

## 2. Estado global

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | saída consciente para fronteira externa validada | UXA-101; M7.88 |
| Patch documental | taxonomia global de planos e separação Organização/Business sincronizadas | GEM-004-A1; GPA-004; UXA-100 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | **53 superfícies/estados/fronteiras e 54 transições** | UXA-100/101 |
| Galeria visual | `active` 0.21.0; **118 SVGs** | UXA-101 |
| Matriz por SVG | `active` 0.17.0; **118 arquivos / 31 perfis** | UXA-101 |
| Jornadas Integradas | `active` 0.31.0; Pessoa, Coletivo e Organização permanecem `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Taxonomia global de planos

| Contexto | Taxonomia vigente | Natureza |
|---|---|---|
| Pessoa | **Free · Plus · Pro** | planos da Pessoa |
| Coletivo | **Livre · Mobiliza · Impacta · Rede** | planos do Coletivo |
| Organização | **Conecta · Eleva · Transforma** | planos da jornada institucional |
| Guivos Business | **Start · Growth · Scale · Enterprise** | planos conceituais do produto especializado; preço/entitlements ainda não definidos |

Regra de leitura:

> **Plano representa profundidade de serviço, capacidade ou complexidade atendida; nunca valor, mérito, prestígio ou nível de evolução do participante.**

A progressão não é obrigatória e não constitui uma escada de evolução.

Separação estrutural obrigatória:

> **Organização Transforma ≠ Guivos Business Enterprise.**

Organização continua sendo um tipo de participante institucional. Guivos Business continua sendo produto especializado da Guivos. Não existe correspondência automática 1:1 entre as duas estruturas.

## 4. Migração taxonômica controlada

| Referência anterior | Referência vigente |
|---|---|
| Coletivo Gestão | Coletivo Mobiliza |
| Coletivo Impacto | Coletivo Impacta |
| Coletivo Enterprise | Coletivo Rede |
| Business Start usado como plano da Organização | Organização Conecta |
| Business Growth usado como plano da Organização | Organização Eleva |
| Business Scale usado como plano da Organização | Organização Transforma |

Preços e capacidades de participantes anteriormente governados permanecem preservados nas novas nomenclaturas. Nenhum preço, entitlement, limite ou SLA foi inventado para Guivos Business.

## 5. Cobertura visual

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

A sincronização taxonômica altera texto/nomenclatura em **6 dos 9 SVGs UXA-100** de Coletivo e Organização, preservando caminhos, IDs, perfis e lógica funcional. Os três SVGs de Pessoa permanecem intactos.

## 6. Resultado da UXA-101 preservado

A UXA-101:

- fecha V4 no limite documental controlável pela Guivos;
- materializa no mesmo SVG de `PER-203` a revisão pré-saída prevista por UXA-007;
- identifica destino externo e responsável antes do handoff;
- explicita dados/contexto que acompanham ou não acompanham a saída;
- exige decisão afirmativa e revalidação do destino conhecido/autorizado;
- bloqueia redirecionamento silencioso quando o destino está ausente, inválido ou materialmente alterado;
- preserva cancelamento/retorno sem penalidade;
- não presume inscrição, reserva, compra, contratação, presença ou evolução externas;
- valida `TRN-205` até `BND-001`;
- confirma `BND-001` como fronteira externa, não superfície Guivos.

Veredito preservado:

> **V4 encerrada no limite de autoridade da Guivos: `TRN-205` validada até `BND-001`, sem apropriar comportamento ou resultado do terceiro.**

## 7. Continuidade de oportunidades

```text
ORG-003
→ TRN-203
→ PER-201 — Mapa
↔ TRN-210
→ PER-202 — Lista
→ TRN-204/211
→ PER-203 — Detalhe
→ estado de revisão de saída em PER-203
→ TRN-205
→ BND-001 — autoridade externa
```

`TRN-203`, `204`, `210`, `211` permanecem integralmente validadas pela UXA-098. `TRN-205` permanece integral no limite de autoridade declarado pela UXA-101.

## 8. Continuidade de Planos e BND-002

As 15 transições internas de Planos permanecem localmente validadas. `TRN-416` e `TRN-426` permanecem **parciais**.

`BND-002` passa a significar exclusivamente:

> **fronteira de contratação/dimensionamento assistido quando uma configuração exige proposta, dimensionamento, contrato, configuração ou análise específica.**

`BND-002` não significa Enterprise, Scale, Rede ou Transforma e não pertence a um único participante.

## 9. Continuidades preservadas

- `TRN-007` permanece integralmente validada pela UXA-097;
- `COM-005` permanece funcionalmente validado pela UXA-099;
- oito transições do trecho governado de Coletivos permanecem integralmente validadas: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`;
- `TRN-304`, `TRN-305` e `TRN-306` permanecem parciais;
- `TRN-416` e `TRN-426` permanecem parciais;
- nenhuma jornada é promovida pelo patch.

## 10. Dívidas preservadas

- estados P0B de Meus Coletivos, Central e Início do Participante;
- canais P1 e operação interna especializada;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` parciais;
- integrações patrocinadas `TRN-304/305/306`;
- cobrança real e gateway da frente de Planos;
- processo posterior a `BND-002`;
- entradas de Planos a partir de origens ainda sem identidade canônica adequada;
- relação Organização–Coletivo ainda não materializada como conjunto;
- resultado externo posterior a `BND-001` permanece sob autoridade de terceiro;
- preços, entitlements, limites, packaging e unit economics próprios do Guivos Business permanecem não definidos.

## 11. Fila global de validação

| Ordem | Continuidade ou família | Estado |
|---:|---|---|
| V1 | compreensão inicial → Tela Hoje | encerrada por UXA-097 |
| V2 | publicação → descoberta/mapa/lista/detalhe | encerrada por UXA-098 |
| V3 | dez estados residuais UXA-055 | encerrada por UXA-099 |
| Planos | identidade e promoção canônica | encerrada por UXA-100-A3; taxonomia sincronizada no patch 2.27.1 |
| **V4** | efeito externo de oportunidades | **encerrada por UXA-101 até BND-001** |
| V5 | erros, retornos e interrupções | pendente; **não iniciada** |

## 12. Estado documental vigente no patch

| Camada | Estado |
|---|---|
| Arquitetura da Experiência | `active` 0.94.0 |
| Jornadas Integradas | `active` 0.31.0 |
| Jornada da Pessoa | `draft` 0.15.0 |
| Jornada do Coletivo | `draft` 0.16.0 |
| Jornada da Organização | `draft` 0.9.0 |
| catálogo integrado | `active` 0.27.0 |
| galeria visual | `active` 0.21.0 |
| galeria de Planos | `active` 0.4.0 |
| matriz por SVG | `active` 0.17.0 |
| lacunas | `active` 0.27.0 |
| registro de superfícies | `active` 0.18.0 |
| registro de transições | `active` 0.19.0 |
| detalhamento comercial/fronteira | `active` 0.6.0 |
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 13. Preservações

- materialização, validação, promoção e implementação são estados distintos;
- validação até uma fronteira não valida sistema de terceiro;
- publicação não é distribuição garantida;
- relação comercial e plano pago não compram relevância funcional;
- plano não representa valor ou nível de evolução do participante;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- Pessoa, Coletivo e Organização permanecem `draft`;
- Guivos Business não recebe nova jornada, `SURF`, `TRN`, `BND` ou SVG;
- nenhuma etapa autoriza automaticamente a seguinte.

## 14. Próximo ato

A UXA-101 continua encerrando V4. **UXA-102/V5 não foram iniciadas.** A definição comercial própria do Guivos Business e qualquer processo posterior a `BND-002` permanecem frentes separadas. Engenharia de Produto permanece pausada antes de W0-01.
