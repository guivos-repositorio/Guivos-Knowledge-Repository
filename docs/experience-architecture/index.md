---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.83.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.77
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
| com validação funcional registrada | 95 |
| pendentes de validação específica | 10 |
| IDs com referência visual | 27 de 40 |
| responsabilidades sem SVG dedicado | 12 |

Os dez pendentes remanescentes são exclusivamente os estados residuais da UXA-055. A UXA-090 não altera a cobertura visual.

## 4. Decisões estruturais preservadas

- conteúdo de origem permanece separado da ajuda temporária;
- ajuda ocorre somente após solicitação consciente;
- texto e voz são modalidades equivalentes;
- síntese não substitui fonte;
- desconhecido não é fato;
- solicitação não é aprovação;
- pedido adicional não é obrigação de revelar;
- acessibilidade não é critério oculto de elegibilidade;
- recusa não é reputação ou sanção;
- autoridade é concedida e verificada, não criada por confirmação;
- autoridade insuficiente não pode ser contornada pela interface;
- estado obsoleto não pode sobrescrever estado canônico mais recente;
- repetição de interação ou entrega não pode duplicar efeito lógico;
- publicidade não compra relevância, reputação ou autoridade;
- correção documental não equivale a aprovação funcional;
- promoção do instrumento não promove os objetos;
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
```

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

Visitante, solicitante, responsável, representante, anunciante e patrocinador permanecem papéis contextuais.

## 6. Resultado da UXA-090

[UXA-090 — Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos](uxa-090-integrated-collective-request-handoffs-functional-validation.md) valida como conjunto cinco ligações entre superfícies previamente validadas:

1. `GKR-TRN-105` — solicitação disponível para análise;
2. `GKR-TRN-106` — pedido de informação adicional;
3. `GKR-TRN-107` — resposta adicional;
4. `GKR-TRN-109` — recusa;
5. `GKR-TRN-112` — Visão Geral do Responsável → gestão de solicitações.

A UXA-090 formaliza identidade estável da solicitação, estado canônico, autoridade vigente, dados mínimos, resolução de concorrência e efeito lógico único.

`GKR-TRN-108` permanece parcial porque `GKR-SURF-PER-106` continua ausente e a passagem entre o resultado aprovado em `PER-105` e o ambiente futuro do participante precisa ser refinada junto da materialização.

## 7. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` 0.18.0 |
| Pessoa, Coletivo e Organização | `draft` |
| catálogo integrado | `active` 0.14.0 |
| galeria visual | `active` 0.9.0 |
| página de Coletivos | `active` 0.7.0 |
| demais páginas visuais | `active` 0.3.0 |
| matriz por SVG | `active` 0.7.0 |
| lacunas | `active` 0.15.0 |
| registro de superfícies | `active` 0.7.0 |
| registro de transições | `active` 0.7.0 |
| detalhamento do Coletivo | `active` 0.6.0 |
| Jornada do Coletivo | `draft` 0.8.0 |
| demais detalhamentos | `active` 0.2.0 |

## 8. Ressalvas vigentes

- perfis agregados não substituem análise exclusiva por estado;
- 12 responsabilidades permanecem sem SVG dedicado;
- dez estados da UXA-055 permanecem sem validação específica;
- `GKR-TRN-108` permanece parcial;
- `GKR-SURF-PER-106` continua ausente;
- a Jornada do Coletivo continua `draft`;
- continuidades entre outros pacotes permanecem parciais ou não examinadas;
- uma superfície ou transição validada não torna automaticamente a jornada completa.

## 9. Prioridade de Coletivos

```text
GKR-SURF-COL-002 — validada
→ GKR-TRN-112 — integralmente validada
→ GKR-SURF-COL-003 — validada
↔ GKR-TRN-105/106/107/109 — integralmente validadas com PER-105
→ GKR-TRN-108 — parcial
→ GKR-SURF-PER-106 — Meus Coletivos, ausente
→ GKR-SURF-PER-107 — Central de Atualizações, ausente
→ GKR-SURF-PER-108 — Início do Participante, reformulação pendente
```

A UXA-090 não autoriza avanço automático para `PER-106`.

## 10. Dívidas de validação e materialização

- `GKR-SURF-PER-106` e continuidade pós-aprovação;
- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 11. Limites

A UXA-090 não cria novo SVG, protótipo, implementação, teste com pessoas, componente técnico ou Engenharia de Produto. Também não materializa `PER-106`, `PER-107`, `PER-108` ou `COL-004` a `COL-008`.

## 12. Próxima evolução possível

**UXA-091 — Materialização Controlada de Meus Coletivos (`GKR-SURF-PER-106`) e Refinamento da Continuidade Pós-Aprovação**, mediante autorização separada.

A UXA-091 não foi iniciada.
