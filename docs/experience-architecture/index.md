---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.84.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - PAS-001
  - GLPA-001
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-037
  - UXA-038
  - UXA-055
  - UXA-056
  - UXA-069
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - UXA-080
  - UXA-081
  - UXA-082
  - UXA-083
  - UXA-084
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.78
normative: false
---

# Arquitetura da Experiência da Guivos

## 1. Finalidade

A Arquitetura da Experiência transforma princípios, capacidades e contratos em experiências compreensíveis para Pessoas, Coletivos e Organizações.

Ela governa hierarquia, decisão, continuidade, confirmação, autoridade, privacidade e proteção antes de design visual ou implementação.

## 2. Regra de maturidade

```text
contrato funcional
→ programa governado
→ materialização
→ validação funcional
→ reformulação, quando exigida
→ revalidação ou validação após reformulação
→ promoção controlada quando aplicável
→ inspeção integrada
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 106 |
| associações individuais | 106 |
| perfis de rastreabilidade | 26 |
| com validação funcional vigente | 94 |
| pendentes de validação específica | 12 |
| IDs com referência visual | 28 de 40 |
| responsabilidades sem SVG dedicado | 11 |

Os 12 pendentes são dez estados residuais da UXA-055, o estado aprovado corrente de `PER-105` reformulado pela UXA-091 e `PER-106`.

## 4. Decisões estruturais preservadas

- conteúdo de origem permanece separado da ajuda temporária;
- ajuda ocorre somente após solicitação consciente;
- texto e voz são modalidades equivalentes;
- síntese não substitui fonte;
- desconhecido não é fato;
- solicitação não é aprovação;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- pausa não reduz reputação;
- pedido adicional não é obrigação de revelar;
- acessibilidade não é critério oculto de elegibilidade;
- recusa não é reputação ou sanção;
- autoridade é concedida e verificada, não criada por confirmação;
- estado obsoleto não pode sobrescrever estado canônico mais recente;
- repetição de interação ou entrega não pode duplicar efeito lógico;
- `Meus Coletivos` não é ranking, score, sequência obrigatória ou feed unificado;
- aprovação não cria função, autoridade, notificação ou presença obrigatória;
- uma versão visual reformulada exige revalidação;
- materialização não equivale a validação funcional;
- validação de superfície não equivale a validação de transição;
- validação integral documental não equivale a implementação técnica;
- presença ou ordem na galeria não valida jornada.

## 5. Evolução das Jornadas Integradas

```text
UXA-070 a UXA-075 — seção integrada estruturada e promovida seletivamente
UXA-076 a UXA-080 — registros granulares estruturados e promovidos
UXA-081 a UXA-085 — galeria e matriz governadas
UXA-086 — Visão Geral do Responsável do Coletivo materializada
UXA-087 — Visão Geral do Responsável reformulada e validada funcionalmente
UXA-088 — Gestão de Solicitações do Responsável materializada em sete estados desktop
UXA-089 — Gestão de Solicitações reformulada e validada funcionalmente
UXA-090 — cinco handoffs elegíveis de solicitação validados ponta a ponta
UXA-091 — Meus Coletivos materializada e continuidade pós-aprovação refinada
```

## 6. Resultado da UXA-091

[UXA-091 — Materialização Controlada de Meus Coletivos e Refinamento da Continuidade Pós-Aprovação](uxa-091-my-collectives-materialization-and-post-approval-continuity-refinement.md) materializa `GKR-SURF-PER-106` e modifica exclusivamente a continuidade do estado aprovado de `PER-105`.

A UXA-091 consolida:

1. `Meus Coletivos` como superfície central de vínculos da Pessoa;
2. organização separada de Participando, Acompanhando, Solicitações, Convites e Pausadas;
3. ausência de ranking, pontuação, comparação ou sequência obrigatória;
4. vínculo aprovado preservando função, notificações e presença;
5. passagem explícita `resultado aprovado → Ver em Meus Coletivos → PER-106`;
6. `TRN-108` parcial aguardando revalidação;
7. `TRN-110` parcial por `PER-107` ausente.

A UXA-091 não valida funcionalmente a nova superfície nem a continuidade reformulada.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` 0.19.0 |
| Jornada da Pessoa | `draft` 0.4.0 |
| Jornada do Coletivo | `draft` 0.9.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.15.0 |
| galeria visual | `active` 0.10.0 |
| página de Coletivos | `active` 0.8.0 |
| demais páginas visuais | `active` 0.3.0 |
| matriz por SVG | `active` 0.8.0 |
| lacunas | `active` 0.16.0 |
| registro de superfícies | `active` 0.8.0 |
| registro de transições | `active` 0.8.0 |
| detalhamento da Pessoa | `active` 0.3.0 |
| detalhamento do Coletivo | `active` 0.6.0 |

## 8. Ressalvas vigentes

- 11 responsabilidades permanecem sem SVG dedicado;
- 12 SVGs permanecem sem validação específica vigente;
- `GKR-TRN-108` e `GKR-TRN-110` permanecem parciais;
- `GKR-SURF-PER-107` continua ausente;
- `GKR-SURF-PER-108` continua com reformulação pendente;
- Jornadas da Pessoa e do Coletivo continuam `draft`;
- continuidades entre outros pacotes permanecem parciais ou não examinadas.

## 9. Prioridade de Coletivos

```text
GKR-SURF-COL-002 — validada
→ GKR-TRN-112 — integralmente validada
→ GKR-SURF-COL-003 — validada
↔ GKR-TRN-105/106/107/109 — integralmente validadas com PER-105
→ PER-105 aprovado — reformulado; revalidação pendente
→ GKR-TRN-108 — parcial
→ GKR-SURF-PER-106 — materializado; validação pendente
→ GKR-TRN-110 — parcial
→ GKR-SURF-PER-107 — ausente
→ GKR-SURF-PER-108 — reformulação pendente
```

## 10. Dívidas de validação e materialização

- validação de `PER-106` e revalidação da continuidade pós-aprovação;
- `PER-107` e `PER-108` em frentes posteriores;
- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 11. Limites

A UXA-091 não cria protótipo, implementação, teste com pessoas, componente técnico ou Engenharia de Produto. Também não materializa `PER-107`, `PER-108` ou `COL-004` a `COL-008`.

## 12. Próxima evolução possível

**UXA-092 — Validação Funcional de Meus Coletivos e Revalidação da Continuidade Pós-Aprovação**, mediante autorização separada.

A UXA-092 não foi iniciada.
