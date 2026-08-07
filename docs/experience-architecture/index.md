---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.80.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.74
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
| SVGs existentes | 98 |
| associações individuais | 98 |
| perfis de rastreabilidade | 24 |
| com validação funcional registrada | 88 |
| pendentes de validação específica | 10 |
| IDs com referência visual | 26 de 40 |
| responsabilidades sem SVG dedicado | 13 |

Os dez pendentes remanescentes são exclusivamente os estados residuais da UXA-055.

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
- materialização não equivale a validação funcional;
- validação de superfície não equivale a validação de transição;
- presença ou ordem na galeria não valida jornada.

## 5. Evolução das Jornadas Integradas

```text
UXA-070 a UXA-075 — seção integrada estruturada e promovida seletivamente
UXA-076 a UXA-080 — registros granulares estruturados e promovidos
UXA-081 — galeria integrada criada e cobertura auditada
UXA-082 — galeria não aprovada e lacunas repriorizadas
UXA-083 — galeria reformulada e matriz individual criada
UXA-084 — galeria e matriz revalidadas com ressalvas
UXA-085 — instrumentos visuais promovidos com ressalvas preservadas
UXA-086 — Visão Geral do Responsável do Coletivo materializada
UXA-087 — Visão Geral do Responsável reformulada e validada funcionalmente
```

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

Visitante, solicitante, responsável, representante, anunciante e patrocinador permanecem papéis contextuais.

## 6. Resultado da UXA-087

[UXA-087 — Validação Funcional e Reformulação da Visão Geral do Responsável do Coletivo](uxa-087-collective-responsible-overview-functional-validation-and-reformulation.md) aprova `GKR-SURF-COL-002` após corrigir quatro falhas da materialização original:

1. estado e escopo de autoridade passam a ser explícitos;
2. a atenção principal passa a mostrar prazo verificável;
3. adiamento e contestação legítimos tornam-se visíveis;
4. retorno ao contexto anterior torna-se explícito.

A UXA-087 não adiciona SVG, não materializa `GKR-SURF-COL-003`, não valida `GKR-TRN-112` ponta a ponta e não promove a jornada do Coletivo.

## 7. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` 0.15.0 |
| Pessoa, Coletivo e Organização | `draft` |
| catálogo integrado | `active` 0.12.0 |
| galeria visual | `active` 0.7.0 |
| página de Coletivos | `active` 0.5.0 |
| demais páginas visuais | `active` 0.3.0 |
| matriz por SVG | `active` 0.5.0 |
| lacunas | `active` 0.12.0 |
| registro de superfícies | `active` 0.5.0 |
| registro de transições | `active` 0.4.0 |
| detalhamento do Coletivo | `active` 0.4.0 |
| demais detalhamentos | `active` 0.2.0 |

## 8. Ressalvas vigentes

- perfis agregados não substituem análise exclusiva por estado;
- 13 responsabilidades permanecem sem SVG dedicado;
- dez estados da UXA-055 permanecem sem validação específica;
- `GKR-TRN-112` permanece parcial;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- uma superfície validada não torna a jornada validada.

## 9. Prioridade de Coletivos

```text
GKR-SURF-COL-002 — validada
→ GKR-SURF-COL-003 — gestão completa de solicitações, ausente
→ GKR-SURF-PER-106 — Meus Coletivos
→ GKR-SURF-PER-107 — Central de Atualizações
→ GKR-SURF-PER-108 — Início do Participante
```

A UXA-087 não autoriza o avanço automático para `COL-003`.

## 10. Dívidas de validação e materialização

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- `GKR-SURF-COL-003` permanece como próxima materialização por dependência.

## 11. Limites

A UXA-087 não cria protótipo, implementação, teste com pessoas, componentes técnicos ou Engenharia de Produto.

## 12. Próxima evolução possível

**UXA-088 — Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo (`GKR-SURF-COL-003`)**, mediante autorização separada.

A UXA-088 não foi iniciada.
