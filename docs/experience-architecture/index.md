---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.76.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.72
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
→ revalidação
→ promoção controlada
→ inspeção integrada
→ protótipo e teste, quando autorizados
→ Engenharia de Produto, quando autorizada
```

Nenhuma etapa autoriza automaticamente a seguinte.

## 3. Cobertura visual

| Indicador | Resultado |
|---|---:|
| SVGs existentes | 97 |
| validados nos pacotes de origem | 87 |
| pendentes de validação específica | 10 |
| IDs com referência visual | 25 de 40 |
| perfis de rastreabilidade | 23 |
| SVGs com associação individual | 97 |

## 4. Decisões estruturais preservadas

- conteúdo de origem permanece separado da ajuda temporária;
- ajuda ocorre somente após solicitação consciente;
- texto e voz são modalidades equivalentes;
- síntese não substitui fonte;
- desconhecido não é fato;
- solicitação não é aprovação;
- publicidade não compra relevância, reputação ou autoridade;
- correção documental não equivale a aprovação funcional;
- promoção do instrumento não promove os objetos;
- presença ou ordem na galeria não valida jornada.

## 5. Evolução das Jornadas Integradas

```text
UXA-070 a UXA-075 — seção integrada estruturada e promovida seletivamente
UXA-076 a UXA-080 — registros granulares estruturados e promovidos
UXA-081 — galeria integrada criada e cobertura auditada
UXA-082 — galeria não aprovada e lacunas repriorizadas
UXA-083 — galeria reformulada e matriz individual criada
```

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

Visitante, solicitante, responsável, representante, anunciante e patrocinador permanecem papéis contextuais.

## 6. Resultado da UXA-083

[UXA-083 — Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção](uxa-083-controlled-integrated-gallery-and-inspection-sequence-reformulation.md) resolve documentalmente os cinco bloqueios da UXA-082.

Foram executados:

1. correção da ordem da Pessoa;
2. separação entre Home pública e Tela Hoje;
3. navegação integrada entre cinco páginas;
4. matriz com associação individual dos 97 SVGs;
5. sincronização de versões e resumos.

A galeria permanece `draft` e exige revalidação.

## 7. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` |
| Pessoa, Coletivo e Organização | `draft` |
| catálogo integrado | `active` 0.8.0 |
| galeria visual | `draft` 0.3.0; reformulada |
| cinco páginas visuais | `draft` 0.2.0 |
| matriz por SVG | `draft` 0.1.0 |
| lacunas | `active` 0.8.0 |
| registro de superfícies | `active` 0.3.0 |
| registro de transições | `active` 0.3.0 |
| detalhamentos granulares | `active` 0.2.0 |

## 8. Prioridade futura de materialização

```text
GKR-SURF-COL-002 — Visão Geral do Responsável
→ GKR-SURF-COL-003 — gestão completa de solicitações
→ GKR-SURF-PER-106 — Meus Coletivos
→ GKR-SURF-PER-107 — Central de Atualizações
→ GKR-SURF-PER-108 — Início do Participante
```

Nenhuma superfície foi iniciada pela UXA-083.

## 9. Dívidas de validação

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 10. Limites

A UXA-083 não altera SVGs, contratos, protótipo ou implementação; não promove jornadas e não fecha lacunas.

## 11. Próxima evolução possível

**UXA-084 — Revalidação Funcional e Visual da Galeria Integrada Reformulada**, mediante autorização separada.
