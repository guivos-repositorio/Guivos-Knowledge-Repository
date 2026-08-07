---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.91.0
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
  - UXA-098
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.85
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

As dez pendências remanescentes são exclusivamente os estados residuais da UXA-055. A UXA-098 não cria nem altera artefatos visuais.

## 4. Decisões estruturais preservadas

- materialização não equivale a validação funcional por padrão;
- uma versão visual reformulada exige revalidação;
- publicação ou ativação não equivale a distribuição garantida;
- a Organização não define relevância individual;
- Mapa e Lista são representações da mesma consulta;
- abrir Detalhe não equivale a interesse, inscrição ou evolução;
- relação comercial não altera relevância funcional;
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
→ UXA-098 — publicação, descoberta, Mapa, Lista e Detalhe validados como continuidade integrada
```

## 6. Resultado da UXA-098

[UXA-098 — Validação Integrada da Continuidade Publicação → Descoberta, Mapa, Lista e Detalhe](uxa-098-publication-discovery-map-list-detail-integrated-validation.md) encerra a prioridade V2 sem reformulação visual.

O veredito é:

> **Aprovada sem reformulação visual, com formalização contratual integrada da publicação, descoberta e continuidade Mapa/Lista/Detalhe.**

A UXA-098 consolida:

1. `TRN-203`: oportunidade aprovada e ativa torna-se candidata à descoberta, sem exposição garantida;
2. `TRN-210`: Mapa e Lista preservam a mesma consulta, contexto e permissões;
3. `TRN-204` e `TRN-211`: Mapa/Lista conduzem ao mesmo Detalhe canônico;
4. estado material vigente prevalece sobre cartões ou detalhes obsoletos;
5. repetição e sincronização permanecem idempotentes;
6. patrocínio e relevância funcional permanecem separados;
7. efeito externo posterior permanece em `TRN-205`;
8. nenhum SVG, superfície ou transição é criado.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
|---|---|
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

## 8. Ressalvas vigentes

- 9 responsabilidades permanecem sem SVG dedicado;
- 10 SVGs UXA-055 continuam sem validação específica;
- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` permanecem parciais;
- `TRN-205` permanece parcial para efeito externo;
- `TRN-304` e `TRN-306` permanecem parciais na integração patrocinada;
- estados P0B e áreas P1 permanecem separados;
- Jornadas da Pessoa, do Coletivo e da Organização continuam `draft`.

## 9. Prioridades vigentes

```text
V1 — compreensão inicial → Tela Hoje — encerrada pela UXA-097
→ V2 — publicação → descoberta/mapa/lista/detalhe — encerrada pela UXA-098
→ V3 — dez estados residuais UXA-055 — próxima prioridade
```

A trilha validada de Coletivos até `PER-108` permanece inalterada.

## 10. Próxima evolução possível

A próxima prioridade registrada é **V3 — dez estados residuais UXA-055**. A UXA-099 não foi iniciada e depende de autorização separada.