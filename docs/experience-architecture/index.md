---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.90.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - PAS-001
  - GLPA-001
  - UXA-001
  - UXA-055
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-069
  - UXA-070
  - UXA-080
  - UXA-085
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
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
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.84
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
| SVGs existentes | **109** |
| associações individuais | **109** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **99** |
| pendentes de validação específica | **10** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |

As dez pendências remanescentes são exclusivamente os estados residuais da UXA-055.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional por padrão;
- uma versão visual reformulada exige revalidação;
- concluir uma compreensão ou navegar não constitui avanço humano;
- personalização não é condição para acessar Hoje;
- primeira Hoje e Hoje recorrente são variantes do mesmo `PER-008`;
- vínculo, disponibilidade, função, presença e autoridade são estados distintos;
- evento histórico não concede acesso interno atual;
- estado `lido` não equivale a consentimento, presença ou ação concluída;
- estado canônico vigente prevalece sobre estado visual obsoleto;
- validação de superfície não equivale a validação automática de transição;
- validação integral documental não equivale a implementação técnica.

## 5. Evolução recente

```text
UXA-090 — cinco handoffs elegíveis validados
→ UXA-091 — Meus Coletivos materializada
→ UXA-092 — Meus Coletivos e TRN-108 validados
→ UXA-093 — Central materializada
→ UXA-094 — Central e TRN-110 validadas
→ UXA-095 — Início do Participante materializado; TRN-111 parcial
→ UXA-096 — Central/Início revalidados e TRN-111 validada ponta a ponta
→ UXA-097 — primeira Hoje materializada; PER-007 revalidada; TRN-007 validada ponta a ponta
```

## 6. Resultado da UXA-097

[UXA-097 — Validação Integrada da Continuidade Compreensão Inicial → Tela Hoje](uxa-097-initial-understanding-to-today-integrated-continuity-validation.md) resolve a diferença entre a primeira entrada e a Tela Hoje recorrente.

O veredito é:

> **Aprovada após materialização mínima do primeiro estado de Hoje, reformulação controlada de PER-007 e validação integrada de GKR-TRN-007.**

A UXA-097 consolida:

1. primeira variante móvel de `PER-008` sem presumir avanço ou mudança anterior;
2. rota sem personalização explicitamente destinada a Hoje;
3. personalização limitada à base confirmada, autorizada e vigente;
4. continuidade legítima em Hoje sem personalização;
5. estado canônico prevalecendo sobre renderização obsoleta;
6. retorno e repetição sem duplicação de efeito lógico;
7. `PER-007` corrente revalidado;
8. primeira variante de `PER-008` validada;
9. `TRN-007` promovida a integralmente validada.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
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

## 8. Ressalvas vigentes

- 9 responsabilidades permanecem sem SVG dedicado;
- 10 SVGs UXA-055 continuam sem validação específica;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` permanecem parciais;
- estados alternativos adicionais de Hoje permanecem separados;
- estados P0B e áreas P1 permanecem separados;
- áreas internas especializadas a partir do Início do Participante não foram validadas como conjunto;
- Jornadas da Pessoa e do Coletivo continuam `draft`;
- continuidades de outros pacotes permanecem parciais ou não examinadas.

## 9. Prioridades vigentes

```text
V1 — compreensão inicial → Tela Hoje — encerrada pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — próxima prioridade registrada
→ V3 — dez estados residuais UXA-055
```

A trilha validada de Coletivos até `PER-108` permanece inalterada.

## 10. Próxima evolução possível

A próxima prioridade registrada é **V2 — publicação → descoberta/mapa/lista/detalhe**. A UXA-098 não foi iniciada e depende de autorização separada.