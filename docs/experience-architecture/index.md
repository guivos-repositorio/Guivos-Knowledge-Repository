---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.85.0
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
  - UXA-092
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.79
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
| com validação funcional vigente | 96 |
| pendentes de validação específica | 10 |
| IDs com referência visual | 28 de 40 |
| responsabilidades sem SVG dedicado | 11 |

Os dez pendentes remanescentes correspondem exclusivamente aos estados residuais da UXA-055.

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
- `Meus Coletivos` separa participação, acompanhamento, solicitação, convite e pausa;
- `Meus Coletivos` não é ranking, score, sequência obrigatória, feed unificado ou Central de Atualizações;
- aprovação forma vínculo antes da navegação posterior;
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
UXA-092 — Meus Coletivos e resultado aprovado reformulados/revalidados; TRN-108 validada integralmente
```

## 6. Resultado da UXA-092

[UXA-092 — Validação Funcional de Meus Coletivos e Revalidação da Continuidade Pós-Aprovação](uxa-092-my-collectives-functional-validation-and-post-approval-continuity-revalidation.md) valida `GKR-SURF-PER-106`, revalida o estado aprovado corrente de `PER-105` e fecha `GKR-TRN-108` como continuidade integral após reformulação controlada dos mesmos dois SVGs existentes.

A UXA-092 consolida:

1. aprovação registrada antes de qualquer navegação posterior;
2. `Ver em Meus Coletivos` como ação opcional, com `Agora não` sem cancelar vínculo;
3. `Meus Coletivos` como central de participações e estados relacionados, não como lista indiscriminada de vínculos;
4. separação entre participação, acompanhamento, solicitação, convite e pausa;
5. ausência de ranking, pontuação, comparação, sequência obrigatória ou contagem própria de não lidos;
6. não antecipação de `PER-107 — Central de Atualizações`;
7. `TRN-108` integralmente validada e `TRN-110` ainda parcial.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` 0.20.0 |
| Jornada da Pessoa | `draft` 0.5.0 |
| Jornada do Coletivo | `draft` 0.10.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.16.0 |
| galeria visual | `active` 0.11.0 |
| página de Coletivos | `active` 0.9.0 |
| demais páginas visuais | `active` 0.3.0 |
| matriz por SVG | `active` 0.9.0 |
| lacunas | `active` 0.17.0 |
| registro de superfícies | `active` 0.9.0 |
| registro de transições | `active` 0.9.0 |
| detalhamento da Pessoa | `active` 0.4.0 |
| detalhamento do Coletivo | `active` 0.6.0 |

## 8. Ressalvas vigentes

- 11 responsabilidades permanecem sem SVG dedicado;
- dez SVGs permanecem sem validação específica vigente, todos UXA-055;
- `GKR-TRN-110` permanece parcial;
- `GKR-SURF-PER-107` continua ausente;
- `GKR-SURF-PER-108` continua com reformulação pendente;
- estados P0B adicionais de `Meus Coletivos` permanecem separados;
- Jornadas da Pessoa e do Coletivo continuam `draft`;
- continuidades entre outros pacotes permanecem parciais ou não examinadas.

## 9. Prioridade de Coletivos

```text
GKR-SURF-COL-002 — validada
→ GKR-TRN-112 — integralmente validada
→ GKR-SURF-COL-003 — validada
↔ GKR-TRN-105/106/107/109 — integralmente validadas com PER-105
→ PER-105 aprovado — reformulado e revalidado
→ GKR-TRN-108 — integralmente validada
→ GKR-SURF-PER-106 — validado
→ GKR-TRN-110 — parcial
→ GKR-SURF-PER-107 — ausente
→ GKR-SURF-PER-108 — reformulação pendente
```

## 10. Dívidas de validação e materialização

- `PER-107` e `PER-108` em frentes posteriores;
- estados P0B adicionais de `PER-106`;
- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 11. Limites

A UXA-092 não cria novo SVG, protótipo, implementação, teste com pessoas, componente técnico ou Engenharia de Produto. Também não materializa `PER-107`, `PER-108` ou `COL-004` a `COL-008`.

## 12. Próxima evolução possível

**UXA-093 — Materialização Controlada da Central de Atualizações (`GKR-SURF-PER-107`)**, mediante autorização separada.

A UXA-093 não foi iniciada.
