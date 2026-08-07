---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.24.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - ROADMAP-12.71.0
  - M7.85
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente quando o incremento correspondente estiver integrado ao ramo principal. Em caso de divergência, prevalece sobre resumos não normativos.

## 2. Estado global proposto pela UXA-098

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | publicação, descoberta e Mapa/Lista/Detalhe validados | UXA-098; M7.85 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | 40 superfícies e 37 transições | UXA-076 a UXA-098 |
| Galeria visual | `active` 0.16.0; 109 SVGs | sem alteração em UXA-098 |
| Página da Pessoa | `active` 0.4.0; 20 SVGs | sem alteração em UXA-098 |
| Página de Coletivos | `active` 0.13.0 | UXA-096 |
| Matriz por SVG | 109 arquivos / 28 perfis | sem alteração em UXA-098 |
| Jornadas Integradas | `active` 0.26.0; Pessoa, Coletivo e Organização em `draft` | UXA-098 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **109** |
| associações individuais | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **99** |
| pendentes de validação específica | **10** |
| IDs granulares com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |

As dez pendências são exclusivamente os estados residuais UXA-055. A UXA-098 não altera a cobertura visual.

## 4. Resultado da UXA-098

A UXA-098:

- preserva sem alteração visual `ORG-003`, `PER-201`, `PER-202` e `PER-203`;
- promove `TRN-203` de não examinada para integralmente validada;
- promove `TRN-204`, `TRN-210` e `TRN-211` de parciais para integralmente validadas;
- formaliza que ativação cria elegibilidade à descoberta, não distribuição garantida;
- preserva uma única identidade lógica e o estado canônico da oportunidade;
- valida Mapa e Lista como a mesma consulta;
- valida as duas rotas internas Mapa/Lista → Detalhe;
- separa o efeito externo posterior em `TRN-205`;
- preserva a fronteira entre relevância orgânica e inventário patrocinado;
- não cria SVG, superfície ou transição;
- não promove Jornada da Pessoa, do Coletivo ou da Organização.

Veredito:

> **Aprovada sem reformulação visual, com formalização contratual integrada da publicação, descoberta e continuidade Mapa/Lista/Detalhe.**

## 5. Continuidade V2 validada

```text
ORG-003 — oportunidade aprovada e ativa
→ TRN-203 — candidata à descoberta, sem exposição garantida
→ PER-201 — Mapa
↔ TRN-210 — mesma consulta
→ PER-202 — Lista

PER-201 → TRN-204 → PER-203
PER-202 → TRN-211 → PER-203
```

## 6. Regras integradas da UXA-098

- a Organização mantém autoridade sobre declaração e manutenção da oportunidade, não sobre relevância individual;
- envio não significa aprovação e aprovação não significa ativação automática;
- oportunidade ativa e vigente pode entrar como candidata à descoberta, sem garantia de impressão, posição, recomendação ou alcance;
- Mapa e Lista preservam contexto de atuação, região, busca, filtros, seleção e permissões aplicáveis;
- alternar Mapa/Lista não cria autorização, personalização ou efeito comercial;
- Mapa e Lista conduzem à mesma oportunidade lógica em `PER-203`;
- estado canônico mais recente prevalece sobre cartão ou detalhe obsoleto;
- pausa, expiração, indisponibilidade ou mudança material interrompem ou atualizam ação substantiva;
- abertura do Detalhe não equivale a interesse, inscrição, recomendação ou evolução;
- repetição e sincronização do mesmo estado são idempotentes;
- pagamento não altera relevância funcional ou posição orgânica.

## 7. Handoffs de Coletivos preservados

Oito transições permanecem integralmente validadas no trecho governado de Coletivos:

`GKR-TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

## 8. Dívidas preservadas

- estados P0B de Meus Coletivos, Central e Início do Participante;
- canais P1 e operação interna especializada;
- dez estados residuais UXA-055;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda parciais na jornada pessoal;
- `TRN-205` efeito externo de oportunidades;
- `TRN-304` e `TRN-306` integração patrocinada com Mapa/Lista;
- erros, retornos e interrupções em outras jornadas;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada como conjunto.

## 9. Fila vigente de validação

| Ordem | Continuidade ou família | Estado |
|---:|---|---|
| V1 | compreensão inicial → Tela Hoje | encerrada por UXA-097 |
| V2 | publicação → descoberta/mapa/lista/detalhe | **encerrada por UXA-098** |
| V3 | dez estados residuais UXA-055 | **próxima prioridade registrada** |
| V4 | efeito externo de oportunidades | pendente |
| V5 | erros, retornos e interrupções | pendente |

## 10. Estado documental

| Camada | Estado |
|---|---|
| Arquitetura da Experiência | `active` 0.91.0 |
| Jornadas Integradas | `active` 0.26.0 |
| Jornada da Pessoa | `draft` 0.11.0 |
| Jornada do Coletivo | `draft` 0.12.0 |
| Jornada da Organização | `draft` 0.4.0 |
| catálogo integrado | `active` 0.21.0 |
| galeria visual | `active` 0.16.0 |
| página da Pessoa | `active` 0.4.0 |
| página de Coletivos | `active` 0.13.0 |
| matriz por SVG | `active` 0.14.0 |
| lacunas | `active` 0.23.0 |
| registro de superfícies | `active` 0.14.0 |
| registro de transições | `active` 0.15.0 |
| detalhamento da Pessoa | `active` 0.9.0 |
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 11. Preservações

- materialização não equivale a validação funcional por padrão;
- publicação não é distribuição garantida;
- relação comercial não compra relevância funcional;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- abrir Detalhe não cria interesse, inscrição ou evolução;
- validação integral documental não equivale a implementação;
- Pessoa, Coletivo e Organização permanecem `draft`;
- nenhuma etapa autoriza automaticamente a seguinte.

## 12. Próxima transição autorizável

Com `V2` encerrada, a próxima prioridade registrada é **V3 — dez estados residuais UXA-055**. A UXA-099 não foi iniciada e dependerá de autorização separada.