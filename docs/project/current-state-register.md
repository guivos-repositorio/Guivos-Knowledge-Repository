---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.23.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - ROADMAP-12.70.0
  - M7.84
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente quando o incremento correspondente estiver integrado ao ramo principal. Em caso de divergência, prevalece sobre resumos não normativos.

## 2. Estado global proposto pela UXA-097

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | primeira Tela Hoje e TRN-007 validadas | UXA-097; M7.84 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | 40 superfícies e 37 transições | UXA-076 a UXA-097 |
| Galeria visual | `active` 0.16.0; 109 SVGs | UXA-081 a UXA-097 |
| Página da Pessoa | `active` 0.4.0; 20 SVGs | UXA-097 |
| Página de Coletivos | `active` 0.13.0 | UXA-096 |
| Matriz por SVG | 109 arquivos / 28 perfis | UXA-083 a UXA-097 |
| Jornadas Integradas | `active` 0.25.0; Pessoa, Coletivo e Organização em `draft` | UXA-070 a UXA-097 |
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

As dez pendências são exclusivamente os estados residuais UXA-055.

## 4. Resultado da UXA-097

A UXA-097:

- materializa 1 novo SVG sob o ID existente `PER-008` para a primeira Tela Hoje;
- reforma 1 SVG existente do estado de decisão de `PER-007`;
- revalida a variante corrente de decisão de `PER-007`;
- valida a primeira variante de `PER-008`;
- promove `TRN-007` de não examinada para integralmente validada;
- preserva a Tela Hoje recorrente sem alteração;
- não cria ID de superfície ou transição;
- não promove Jornada da Pessoa ou Jornada do Coletivo.

Veredito:

> **Aprovada após materialização mínima do primeiro estado de Hoje, reformulação controlada de PER-007 e validação integrada de GKR-TRN-007.**

## 5. Continuidade pessoal validada

```text
PER-007 — compreensão inicial revisável
→ pessoa confirma escolhas compatíveis
→ persistência/personalização assumem somente a condição explicitamente escolhida
→ TRN-007
→ PER-008 consulta o estado canônico vigente
→ primeira Tela Hoje não presume avanço, mudança anterior ou urgência
```

Sem autorização de personalização, Hoje permanece acessível sem indicações pessoais. `Excluir compreensão e continuar explorando` permanece fora de `TRN-007`.

## 6. Regras integradas de TRN-007

- somente base confirmada, autorizada e vigente pode sustentar personalização;
- itens em aberto, desconhecidos, rejeitados ou contestados não viram fatos;
- retirada, exclusão ou mudança posterior prevalecem sobre estado visual obsoleto;
- retorno não desfaz escolhas silenciosamente e nova alteração exige ato explícito;
- repetição, recarga ou duplo toque não criam nova jornada, Próximo Passo ou efeito duplicado;
- concluir a compreensão ou abrir Hoje não conta como avanço humano;
- publicidade ou disponibilidade comercial não criam prioridade artificial na primeira entrada.

## 7. Handoffs de Coletivos preservados

Oito transições permanecem integralmente validadas no trecho governado de Coletivos:

`GKR-TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

## 8. Dívidas preservadas

- estados P0B de Meus Coletivos, Central e Início do Participante;
- canais P1 e operação interna especializada;
- dez estados residuais UXA-055;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda parciais na jornada pessoal;
- publicação → descoberta/mapa/lista/detalhe;
- efeito externo de oportunidades;
- erros, retornos e interrupções em outras jornadas;
- estados alternativos adicionais da Tela Hoje;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada como conjunto.

## 9. Fila vigente de validação

| Ordem | Continuidade ou família | Estado |
|---:|---|---|
| V1 | compreensão inicial → Tela Hoje | **encerrada por UXA-097** |
| V2 | publicação → descoberta/mapa/lista/detalhe | próxima prioridade registrada |
| V3 | dez estados residuais UXA-055 | pendente |
| V4 | efeito externo de oportunidades | pendente |
| V5 | erros, retornos e interrupções | pendente |

## 10. Estado documental

| Camada | Estado |
|---|---|
| Jornadas Integradas | `active` 0.25.0 |
| Jornada da Pessoa | `draft` 0.10.0 |
| Jornada do Coletivo | `draft` 0.12.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.21.0 |
| galeria visual | `active` 0.16.0 |
| página da Pessoa | `active` 0.4.0 |
| página de Coletivos | `active` 0.13.0 |
| matriz por SVG | `active` 0.14.0 |
| lacunas | `active` 0.22.0 |
| registro de superfícies | `active` 0.14.0 |
| registro de transições | `active` 0.14.0 |
| detalhamento da Pessoa | `active` 0.9.0 |
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 11. Preservações

- materialização não equivale a validação funcional por padrão;
- personalização não é condição para acessar Hoje;
- atividade na plataforma não é evolução humana;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- evento histórico não concede acesso atual;
- pertencimento, disponibilidade, função, presença e autoridade permanecem estados separados;
- validação integral documental não equivale a implementação;
- Pessoa e Coletivo permanecem `draft`;
- nenhuma etapa autoriza automaticamente a seguinte.

## 12. Próxima transição autorizável

Com `V1` encerrada, a próxima prioridade registrada é **V2 — publicação → descoberta/mapa/lista/detalhe**. A UXA-098 não foi iniciada e dependerá de autorização separada.