---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.88.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.82
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
| SVGs existentes | **108** |
| associações individuais | **108** |
| perfis de rastreabilidade | **28** |
| com validação funcional vigente | **96** |
| pendentes de validação específica | **12** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |

As pendências são 10 estados UXA-055, a Central corrente reformulada e o novo Início do Participante.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional;
- uma versão visual reformulada exige revalidação;
- vínculo, disponibilidade, função, presença e autoridade são estados distintos;
- `Meus Coletivos` organiza vínculos e estados relacionados;
- a Central preserva origem, natureza, contexto, autoridade, leitura, ação e prazo;
- o Início do Participante sintetiza o contexto interno sem replicar Central ou canais especializados;
- estado `lido` não equivale a consentimento, presença ou ação concluída;
- abrir o Início não confirma presença nem cria função ou autoridade;
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
```

## 6. Resultado da UXA-095

[UXA-095 — Materialização Controlada do Início do Participante e Refinamento de TRN-111](uxa-095-participant-home-materialization-and-trn111-refinement.md) cria uma nova referência móvel para `PER-108` e reforma minimamente `PER-107` para expor o handoff.

O veredito é:

> **Materialização controlada concluída no escopo documental; validação funcional pendente.**

A UXA-095 consolida:

1. `PER-108` como síntese móvel de propósito, vínculo, momento, atividade, consulta e autonomia;
2. `Abrir início do Coletivo` como gatilho explícito em `PER-107`;
3. entrada neutra sem alteração de leitura, vínculo, papel, presença ou autoridade;
4. separação entre Início, Central e canais especializados;
5. `TRN-111` de ausente para parcial;
6. revalidação obrigatória da Central corrente e validação do novo Início em pacote posterior.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active` 0.23.0 |
| Jornada da Pessoa | `draft` 0.8.0 |
| Jornada do Coletivo | `draft` 0.11.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.19.0 |
| galeria visual | `active` 0.14.0 |
| página de Coletivos | `active` 0.12.0 |
| matriz por SVG | `active` 0.12.0 |
| lacunas | `active` 0.20.0 |
| registro de superfícies | `active` 0.12.0 |
| registro de transições | `active` 0.12.0 |
| detalhamento da Pessoa | `active` 0.7.0 |

## 8. Ressalvas vigentes

- 9 responsabilidades permanecem sem SVG dedicado;
- 10 SVGs UXA-055 continuam sem validação específica;
- `PER-107` corrente e `PER-108` aguardam validação;
- `TRN-111` permanece parcial;
- estados P0B e áreas P1 permanecem separados;
- Jornadas da Pessoa e do Coletivo continuam `draft`;
- continuidades de outros pacotes permanecem parciais ou não examinadas.

## 9. Prioridade de Coletivos

```text
COL-002 — validada
→ TRN-112 — integralmente validada
→ COL-003 — validada
↔ TRN-105/106/107/109 — integralmente validadas
→ TRN-108 — integralmente validada
→ PER-106 — validado
→ TRN-110 — integralmente validada
→ PER-107 — contrato validado; SVG corrente pendente
→ TRN-111 — parcial
→ PER-108 — materializado; validação pendente
```

## 10. Próxima evolução possível

**UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de GKR-TRN-111**, mediante autorização separada.

A UXA-096 não foi iniciada.
