---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.25.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - ROADMAP-12.72.0
  - M7.86
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente quando o incremento correspondente estiver integrado ao ramo principal. Em caso de divergência, prevalece sobre resumos não normativos.

## 2. Estado global proposto pela UXA-099

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | dez estados residuais Opportunity Boost validados | UXA-099; M7.86 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | 40 superfícies e 37 transições | UXA-076 a UXA-099 |
| Galeria visual | `active` 0.17.0; 109 SVGs | UXA-099 |
| Página da Pessoa | `active` 0.4.0; 20 SVGs | sem alteração em UXA-099 |
| Página de Coletivos | `active` 0.13.0 | sem alteração em UXA-099 |
| Matriz por SVG | `active` 0.15.0; 109 arquivos / 28 perfis | UXA-099 |
| Jornadas Integradas | `active` 0.27.0; Pessoa, Coletivo e Organização em `draft` | UXA-099 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | **109** |
| associações individuais | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **109** |
| pendentes de validação específica | **0** |
| IDs granulares com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |
| fronteira sem tela por definição | 1 |

A UXA-099 encerra as dez pendências específicas da UXA-055 sem criar SVGs, associações, perfis, superfícies ou transições.

## 4. Resultado da UXA-099

A UXA-099:

- valida funcionalmente os dez estados residuais materializados pela UXA-055;
- aprova oito SVGs sem alteração visual;
- reforma `uxa-055-advertiser-update-failure-mobile.svg` para impedir entrega futura por inércia quando uma alteração material declarada não puder ser confirmada;
- reforma `uxa-055-review-reverse-preferences-mobile.svg` para apresentar data, superfície e escopo de todas as escolhas exibidas;
- consolida repetição funcionalmente idempotente sem definir mecanismo técnico;
- preserva a separação entre erro técnico, zero inventário e baixa oferta orgânica;
- preserva catálogo, busca, região, filtros e ordenação orgânicos;
- preserva denúncia, contestação e preferência como fluxos distintos;
- valida `GKR-SURF-COM-005` no escopo dos dez estados;
- não promove `GKR-TRN-305` a validação integral;
- não altera `TRN-205`, `TRN-304` ou `TRN-306`;
- não promove Jornada da Pessoa, do Coletivo ou da Organização.

Veredito:

> **Aprovada após reformulação controlada de dois wireframes e consolidação transversal de idempotência.**

## 5. Contrato residual validado

```text
erro técnico patrocinado
→ orgânico permanece utilizável; erro não vira zero

zero inventário patrocinado elegível
→ critérios não são ampliados; orgânico permanece intacto

baixa oferta orgânica
→ publicidade é reduzida, nunca compensada por densidade

alteração material do anunciante sem confirmação
→ versão confirmada preservada
→ candidata não aplicada
→ entrega futura pausada automaticamente por proteção
→ retomada somente após confirmação válida e nova verificação

preferências da pessoa
→ ocultar campanha | mostrar menos | desativar patrocinados
→ revisar e desfazer com data, superfície e escopo

integridade e privacidade
→ denúncia de conteúdo ≠ contestação de uso de dados
```

A repetição da mesma intenção não duplica versão, transição, impressão válida, evento válido, consumo de orçamento ou preferência.

## 6. Fronteiras preservadas

- `COM-005` está validado como conjunto de estados, mas isso não valida automaticamente `TRN-305` ponta a ponta;
- `TRN-205` continua parcial para efeito externo posterior;
- `TRN-304` e `TRN-306` continuam parciais na integração patrocinada com Mapa/Lista;
- pagamento amplia distribuição publicitária identificada, não relevância funcional;
- publicação não garante impressão, posição, recomendação ou alcance;
- validação funcional documental não cria algoritmo, cobrança, campanha real ou implementação.

## 7. Continuidades anteriores preservadas

A UXA-099 não reabre as validações anteriores:

- `TRN-203`, `TRN-204`, `TRN-210` e `TRN-211` permanecem integralmente validadas pela UXA-098;
- `TRN-007` permanece integralmente validada pela UXA-097;
- oito transições do trecho governado de Coletivos permanecem integralmente validadas: `TRN-105`, `106`, `107`, `108`, `109`, `110`, `111` e `112`.

## 8. Dívidas preservadas

- estados P0B de Meus Coletivos, Central e Início do Participante;
- canais P1 e operação interna especializada;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda parciais na jornada pessoal;
- `TRN-205` efeito externo de oportunidades;
- `TRN-304` e `TRN-306` integração patrocinada com Mapa/Lista;
- `TRN-305` continuidade para os estados residuais ainda não validada ponta a ponta;
- erros, retornos e interrupções em outras jornadas;
- operação interna restante do Coletivo;
- relação Organização–Coletivo ainda não materializada como conjunto.

## 9. Fila vigente de validação

| Ordem | Continuidade ou família | Estado |
|---:|---|---|
| V1 | compreensão inicial → Tela Hoje | encerrada por UXA-097 |
| V2 | publicação → descoberta/mapa/lista/detalhe | encerrada por UXA-098 |
| V3 | dez estados residuais UXA-055 | **encerrada por UXA-099** |
| V4 | efeito externo de oportunidades | **próxima prioridade registrada** |
| V5 | erros, retornos e interrupções | pendente |

## 10. Estado documental

| Camada | Estado |
|---|---|
| Arquitetura da Experiência | `active` 0.92.0 |
| Jornadas Integradas | `active` 0.27.0 |
| Jornada da Pessoa | `draft` 0.11.0 |
| Jornada do Coletivo | `draft` 0.12.0 |
| Jornada da Organização | `draft` 0.4.0 |
| catálogo integrado | `active` 0.22.0 |
| galeria visual | `active` 0.17.0 |
| página da Pessoa | `active` 0.4.0 |
| página de Coletivos | `active` 0.13.0 |
| página Opportunity Boost — Operação, Relatórios e Resíduos | `active` 0.4.0 |
| matriz por SVG | `active` 0.15.0 |
| lacunas | `active` 0.24.0 |
| registro de superfícies | `active` 0.15.0 |
| detalhamento comercial/fronteira | `active` 0.3.0 |
| registro de transições | `active` 0.16.0 |
| detalhamento da Pessoa | `active` 0.9.0 |
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 11. Preservações

- materialização não equivale a validação funcional por padrão;
- uma versão visual reformulada exige validação correspondente;
- publicação não é distribuição garantida;
- relação comercial não compra relevância funcional;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- preferência negativa prevalece sobre entrega contratada;
- abrir Detalhe não cria interesse, inscrição ou evolução;
- validação integral documental não equivale a implementação;
- Pessoa, Coletivo e Organização permanecem `draft`;
- nenhuma etapa autoriza automaticamente a seguinte.

## 12. Próxima transição autorizável

Com `V3` encerrada, a próxima prioridade registrada é **V4 — efeito externo de oportunidades**, atualmente associado a `TRN-205`. A UXA-100 não foi iniciada e dependerá de autorização separada.
