---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.81.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.75
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
| SVGs existentes | 105 |
| associações individuais | 105 |
| perfis de rastreabilidade | 25 |
| com validação funcional registrada | 88 |
| pendentes de validação específica | 17 |
| IDs com referência visual | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |

Os 17 pendentes são os dez estados residuais da UXA-055 e os sete estados de `GKR-SURF-COL-003` materializados pela UXA-088.

## 4. Decisões estruturais preservadas

- conteúdo de origem permanece separado da ajuda temporária;
- ajuda ocorre somente após solicitação consciente;
- texto e voz são modalidades equivalentes;
- síntese não substitui fonte;
- desconhecido não é fato;
- solicitação não é aprovação;
- pedido adicional não é obrigação de revelar;
- recusa não é reputação ou sanção;
- autoridade insuficiente não pode ser contornada pela interface;
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
UXA-088 — Gestão de Solicitações do Responsável materializada em sete estados desktop
```

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

Visitante, solicitante, responsável, representante, anunciante e patrocinador permanecem papéis contextuais.

## 6. Resultado da UXA-088

[UXA-088 — Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo](uxa-088-collective-request-management-low-fidelity-wireframes.md) materializa `GKR-SURF-COL-003` em sete estados:

1. fila operacional;
2. detalhe comum;
3. análise protegida;
4. pedido de informação adicional;
5. confirmação de aprovação;
6. confirmação de recusa;
7. autoridade insuficiente.

A UXA-088 fornece evidência do lado responsável para `GKR-TRN-105` a `GKR-TRN-109` e materializa o destino de `GKR-TRN-112`.

Ela não valida funcionalmente os sete novos estados, não valida os handoffs ponta a ponta, não materializa `GKR-SURF-PER-106`, não promove a Jornada do Coletivo e não inicia protótipo ou Engenharia de Produto.

## 7. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` 0.16.0 |
| Pessoa, Coletivo e Organização | `draft` |
| catálogo integrado | `active` 0.13.0 |
| galeria visual | `active` 0.8.0 |
| página de Coletivos | `active` 0.6.0 |
| demais páginas visuais | `active` 0.3.0 |
| matriz por SVG | `active` 0.6.0 |
| lacunas | `active` 0.13.0 |
| registro de superfícies | `active` 0.6.0 |
| registro de transições | `active` 0.5.0 |
| detalhamento do Coletivo | `active` 0.5.0 |
| demais detalhamentos | `active` 0.2.0 |

## 8. Ressalvas vigentes

- perfis agregados não substituem análise exclusiva por estado;
- 12 responsabilidades permanecem sem SVG dedicado;
- dez estados da UXA-055 permanecem sem validação específica;
- sete estados da UXA-088 permanecem sem validação funcional específica;
- `GKR-TRN-105` a `GKR-TRN-109` e `GKR-TRN-112` permanecem parciais;
- `GKR-SURF-PER-106` continua ausente;
- continuidades entre pacotes permanecem parciais ou não examinadas;
- uma superfície materializada não torna a jornada validada.

## 9. Prioridade de Coletivos

```text
GKR-SURF-COL-002 — validada
→ GKR-SURF-COL-003 — materializada; validação pendente
→ GKR-SURF-PER-106 — Meus Coletivos, ausente
→ GKR-SURF-PER-107 — Central de Atualizações, ausente
→ GKR-SURF-PER-108 — Início do Participante, reformulação pendente
```

A UXA-088 não autoriza o avanço automático para `PER-106`.

## 10. Dívidas de validação e materialização

- sete estados da UXA-088 — validação funcional específica;
- handoffs bilaterais de solicitação — validação integrada;
- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados;
- `GKR-SURF-PER-106` permanece ausente como próxima materialização a jusante, após o gate de `COL-003`.

## 11. Limites

A UXA-088 não cria protótipo, implementação, teste com pessoas, componentes técnicos ou Engenharia de Produto. Também não materializa `PER-106`, `PER-107`, `PER-108` ou `COL-004` a `COL-008`.

## 12. Próxima evolução possível

**UXA-089 — Validação Funcional da Gestão de Solicitações do Responsável do Coletivo**, mediante autorização separada.

A UXA-089 não foi iniciada.
