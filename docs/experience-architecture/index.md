---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.89.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.83
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
| com validação funcional vigente | **98** |
| pendentes de validação específica | **10** |
| IDs com referência visual | **30 de 40** |
| responsabilidades sem SVG dedicado | **9** |

As dez pendências remanescentes são exclusivamente os estados residuais da UXA-055.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional;
- uma versão visual reformulada exige revalidação;
- vínculo, disponibilidade, função, presença e autoridade são estados distintos;
- evento histórico não concede acesso interno atual;
- `Meus Coletivos` organiza vínculos e estados relacionados;
- a Central preserva origem, natureza, contexto, autoridade, leitura, ação e prazo;
- o Início do Participante sintetiza o contexto interno sem replicar Central ou canais especializados;
- estado `lido` não equivale a consentimento, presença ou ação concluída;
- abrir o Início não confirma presença nem cria função ou autoridade;
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
```

## 6. Resultado da UXA-096

[UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de TRN-111](uxa-096-participant-home-functional-validation-per107-revalidation-and-trn111-integrated-validation.md) reforma duas referências existentes, sem criar SVG ou ID.

O veredito é:

> **Aprovada após reformulação controlada e validação integrada de `GKR-TRN-111`.**

A UXA-096 consolida:

1. vínculo atual e permissão revalidados ao abrir o Início;
2. evento histórico incapaz de conceder ou preservar acesso;
3. `PER-107` validado na versão corrente;
4. `PER-108` validado;
5. retorno neutro sem alteração implícita de leitura;
6. estado canônico mais recente prevalecendo sobre renderização antiga;
7. repetição, retorno e recarga sem duplicação de efeito;
8. `TRN-111` promovida a integralmente validada;
9. oito handoffs integralmente validados no trecho governado de Coletivos.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
|---|---|
| Jornadas Integradas | `active` 0.24.0 |
| Jornada da Pessoa | `draft` 0.9.0 |
| Jornada do Coletivo | `draft` 0.12.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.20.0 |
| galeria visual | `active` 0.15.0 |
| página de Coletivos | `active` 0.13.0 |
| matriz por SVG | `active` 0.13.0 |
| lacunas | `active` 0.21.0 |
| registro de superfícies | `active` 0.13.0 |
| registro de transições | `active` 0.13.0 |
| detalhamento da Pessoa | `active` 0.8.0 |

## 8. Ressalvas vigentes

- 9 responsabilidades permanecem sem SVG dedicado;
- 10 SVGs UXA-055 continuam sem validação específica;
- estados P0B e áreas P1 permanecem separados;
- áreas internas especializadas a partir do Início não foram validadas como conjunto;
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
→ PER-107 — validado
→ TRN-111 — integralmente validada
→ PER-108 — validado
```

## 10. Próxima evolução possível

A próxima priorização deverá partir das lacunas remanescentes. **UXA-097 não foi iniciada e depende de autorização separada.**
