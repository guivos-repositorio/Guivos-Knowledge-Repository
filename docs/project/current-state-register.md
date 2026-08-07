---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 2.20.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - ROADMAP-12.67.0
  - M7.81
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro declara o estado global vigente quando o incremento correspondente estiver integrado ao ramo principal. Em caso de divergência, prevalece sobre resumos não normativos.

## 2. Estado global

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de estruturação do conhecimento | GE-2 — Knowledge |
| Marco | Central de Atualizações validada; TRN-110 validada ponta a ponta; continuidade seguinte interrompida em PER-108 | UXA-094; M7.81 |
| Fundação | congelada | GEA-000 |
| Journey | funcionalmente estruturado | PAS-001 |
| Registros granulares | 40 superfícies e 37 transições | UXA-076 a UXA-094 |
| Galeria visual | `active` 0.13.0; 107 SVGs | UXA-081 a UXA-094 |
| Página de Coletivos | `active` 0.11.0 | UXA-094 |
| Matriz por SVG | 107 arquivos / 27 perfis | UXA-083 a UXA-094 |
| Jornadas Integradas | `active` 0.22.0; Pessoa, Coletivo e Organização em `draft` | UXA-070 a UXA-094 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes e referenciados | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| com validação funcional vigente | **97** |
| pendentes de validação específica | **10** |
| IDs granulares com referência visual | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |
| fronteira sem tela por definição | 1 |

Os dez pendentes remanescentes correspondem exclusivamente aos estados residuais da UXA-055.

## 4. Resultado da UXA-094

A UXA-094 reformula e revalida dois SVGs existentes:

- `GKR-SURF-PER-106 — Meus Coletivos`, para tornar explícito o gatilho neutro `Ver atualizações`;
- `GKR-SURF-PER-107 — Central de Atualizações`, para corrigir prioridade de segurança, fonte/vigência, preferências, taxonomia acessível e separação entre leitura e efeito substantivo.

Veredito:

> **Aprovada após reformulação controlada e validação integrada de `GKR-TRN-110`.**

Efeitos governados:

- `PER-106` permanece `validado` na versão corrente;
- `PER-107` passa de `materializado` para `validado`;
- `TRN-110` passa de `parcial` para `integralmente validada`;
- `TRN-111` permanece `ausente`;
- `PER-108` permanece com reformulação/materialização pendente;
- nenhum SVG, superfície, transição ou ID é criado ou removido.

## 5. Contrato validado de TRN-110

```text
PER-106 — Meus Coletivos
→ Pessoa escolhe “Ver atualizações”
→ nenhum vínculo ou leitura é alterado pelo clique
→ PER-107 — Central de Atualizações
→ Pessoa compreende origem, natureza, autoridade, leitura, ação e prazo
→ retorna a PER-106 sem consequência oculta
```

Regras vigentes:

- abrir ou reabrir a Central não marca itens como lidos;
- leitura não responde solicitação, aceita convite, confirma presença, concorda com decisão ou conclui tarefa;
- ações substantivas revalidam o estado canônico do objeto antes do efeito;
- estado obsoleto não prevalece sobre atualização mais recente;
- repetir abertura, leitura ou confirmação de leitura não duplica efeito lógico;
- segurança material precede ação comum na ordem de atenção;
- preferência pode modular conteúdo não essencial, mas não ocultar entrega mínima necessária de aviso essencial de segurança;
- engajamento, popularidade, plano pago e publicidade não podem dominar a ordenação.

## 6. Handoffs integralmente validados em Coletivos

Sete transições possuem validação integral documental no trecho corrente:

- `GKR-TRN-105`;
- `GKR-TRN-106`;
- `GKR-TRN-107`;
- `GKR-TRN-108`;
- `GKR-TRN-109`;
- `GKR-TRN-110`;
- `GKR-TRN-112`.

Validação integral documental não equivale a implementação técnica.

## 7. Prioridade operacional de Coletivos

| Ordem | Superfície ou continuidade | Estado |
|---:|---|---|
| 1 | COL-002 — Visão Geral do Responsável | validada |
| 2 | COL-003 — gestão de solicitações | validada |
| 3 | TRN-105/106/107/108/109/112 | integralmente validadas |
| 4 | PER-105 aprovado | validado |
| 5 | PER-106 — Meus Coletivos | validado; gatilho para Central revalidado |
| 6 | TRN-110 | integralmente validada por UXA-094 |
| 7 | PER-107 — Central de Atualizações | validada por UXA-094 |
| 8 | TRN-111 / PER-108 | ausente / reformulação pendente |

## 8. Dívidas preservadas

- `PER-108 — Início do Participante` e `TRN-111`;
- estados P0B da Central: vazio, excesso de volume e baixa conectividade;
- estados P0B adicionais de `Meus Coletivos`;
- áreas P1 de comunicação especializada;
- dez estados residuais da UXA-055;
- compreensão inicial → Tela Hoje;
- publicação → descoberta;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- operação interna restante do Coletivo.

## 9. Estado documental

| Camada | Estado |
|---|---|
| Jornadas Integradas | `active` 0.22.0 |
| Jornada da Pessoa | `draft` 0.7.0 |
| Jornada do Coletivo | `draft` 0.10.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.18.0 |
| galeria visual | `active` 0.13.0 |
| página de Coletivos | `active` 0.11.0 |
| matriz por SVG | `active` 0.11.0 |
| lacunas | `active` 0.19.0 |
| registro de superfícies | `active` 0.11.0 |
| registro de transições | `active` 0.11.0 |
| detalhamento da Pessoa | `active` 0.6.0 |
| detalhamento do Coletivo | `active` 0.6.0 |
| protótipo, aplicação, motor e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 10. Preservações

- materialização não equivale a validação funcional;
- uma versão reformulada exige revalidação;
- leitura não equivale a consentimento, presença ou efeito substantivo;
- autoridade continua concedida e verificada, nunca criada pela interface;
- `PER-107` é triagem pessoal de mudanças, não feed social;
- `PER-108` e canais P1 não são presumidos como existentes;
- Pessoa e Coletivo permanecem `draft`;
- nenhuma etapa autoriza automaticamente a seguinte.

## 11. Próxima transição autorizável

**UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`.**

A UXA-095 não foi iniciada e depende de autorização separada.
