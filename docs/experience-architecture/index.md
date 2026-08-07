---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.87.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.81
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
| SVGs existentes | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| com validação funcional vigente | **97** |
| pendentes de validação específica | **10** |
| IDs com referência visual | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |

Os dez pendentes remanescentes são exclusivamente os estados residuais da UXA-055.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional;
- uma versão visual reformulada exige revalidação;
- estado obsoleto não pode sobrescrever estado canônico mais recente;
- repetição de interação não pode duplicar efeito lógico;
- `Meus Coletivos` separa participação, acompanhamento, solicitação, convite e pausa;
- abrir a Central não altera vínculo nem leitura;
- a Central preserva origem, natureza, contexto, autoridade, leitura, ação e prazo;
- estado `lido` não equivale a concordância, consentimento, presença ou ação concluída;
- segurança material precede ação comum na ordenação de atenção;
- preferência comum não pode ocultar entrega mínima necessária de aviso essencial de segurança;
- engajamento, popularidade, plano pago e publicidade não dominam a ordem;
- validação de superfície não equivale a validação automática de transição;
- validação integral documental não equivale a implementação técnica;
- presença ou ordem na galeria não valida jornada completa.

## 5. Evolução recente

```text
UXA-090 — cinco handoffs elegíveis validados ponta a ponta
→ UXA-091 — Meus Coletivos materializada
→ UXA-092 — Meus Coletivos e TRN-108 validados
→ UXA-093 — Central de Atualizações materializada
→ UXA-094 — Central reformulada/validada e TRN-110 validada ponta a ponta
```

## 6. Resultado da UXA-094

[UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de GKR-TRN-110](uxa-094-collective-updates-center-functional-validation-and-trn110-revalidation.md) reforma dois SVGs existentes, valida `PER-107`, revalida o gatilho corrente de `PER-106` e promove `TRN-110` a `integralmente validada`.

O veredito é:

> **Aprovada após reformulação controlada e validação integrada de `GKR-TRN-110`.**

A UXA-094 consolida:

1. gatilho explícito `Ver atualizações` em `PER-106`;
2. entrada neutra sem mudança de vínculo ou leitura;
3. segurança material antes de ação comum;
4. fonte, autoridade e vigência/revisão no alerta;
5. preferências para conteúdo não essencial, com limite explícito para aviso essencial;
6. acesso às demais categorias sem antecipar canais P1;
7. leitura separada de efeito substantivo;
8. revalidação de estado antes de ação;
9. concorrência resolvida pelo estado canônico mais recente;
10. idempotência de abertura e leitura;
11. `TRN-111/PER-108` preservados como fronteira ainda não materializada.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
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

## 8. Ressalvas vigentes

- 10 responsabilidades permanecem sem SVG dedicado;
- dez SVGs UXA-055 continuam sem validação específica;
- `TRN-111` permanece ausente;
- `PER-108` continua com reformulação/materialização pendente;
- estados P0B da Central e de Meus Coletivos permanecem separados;
- áreas P1 de comunicação especializada não foram materializadas;
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
→ TRN-111 — ausente
→ PER-108 — reformulação/materialização pendente
```

## 10. Próxima evolução possível

**UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`**, mediante autorização separada.

A UXA-095 não foi iniciada.
