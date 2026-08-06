---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.75.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
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

## 3. Cobertura visual auditada

| Família | SVGs | Validados | Pendentes |
|---|---:|---:|---:|
| fundação pública e experiência recorrente | 2 | 2 | 0 |
| início protegido, compreensão e expressão guiada | 17 | 17 | 0 |
| oportunidades orgânicas | 7 | 7 | 0 |
| Organização | 2 | 2 | 0 |
| Coletivo — referência inicial | 1 | 1 | 0 |
| Coletivos — cobertura móvel | 22 | 22 | 0 |
| Opportunity Boost | 46 | 36 | 10 |
| **Total** | **97** | **87** | **10** |

Os 97 arquivos concentram-se em 25 dos 40 IDs granulares.

## 4. Decisões estruturais preservadas

- conteúdo de origem permanece separado da ajuda temporária;
- ajuda ocorre somente após solicitação consciente;
- texto e voz são modalidades equivalentes;
- rascunho não solicita análise ou salvamento implícitos;
- síntese não substitui fonte;
- desconhecido não é fato;
- solicitação não é aprovação;
- publicidade não compra relevância, reputação ou autoridade;
- correção documental não equivale a aprovação funcional;
- promoção do instrumento não promove os objetos;
- presença na galeria não aprova assertividade visual.

## 5. Evolução das Jornadas Integradas

```text
UXA-070 a UXA-075 — seção integrada materializada, reformulada, validada e promovida seletivamente
UXA-076 a UXA-080 — registros granulares materializados, corrigidos, revalidados e promovidos
UXA-081 — galeria integrada criada e cobertura visual auditada
UXA-082 — galeria não aprovada para promoção e lacunas repriorizadas por dependência
```

Participantes estruturais:

- Pessoa;
- Coletivo;
- Organização.

Visitante, solicitante, responsável, representante, anunciante e patrocinador permanecem perspectivas ou papéis contextuais.

## 6. Resultado da UXA-082

[UXA-082 — Validação Funcional e Visual da Galeria Integrada e Priorização Governada das Lacunas](uxa-082-integrated-gallery-functional-visual-validation-and-gap-prioritization.md) confirma a galeria como inventário visual, mas bloqueia sua promoção.

Achados:

1. a página da Pessoa não segue a ordem funcional;
2. Home pública e Tela Hoje estão agrupadas em um mesmo bloco;
3. não existe rota integrada entre as cinco páginas;
4. a rastreabilidade agrupada não permite assertividade por SVG;
5. versões documentais permaneciam divergentes.

O parecer não altera os SVGs nem invalida as validações locais de origem. Ele limita o uso da galeria até reformulação e nova validação.

## 7. Instrumentos vigentes

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` |
| Pessoa, Coletivo e Organização | `draft` |
| catálogo integrado | `active` 0.7.0 |
| galeria visual | `draft` 0.2.0; não aprovada para promoção |
| lacunas | `active` 0.7.0 |
| registro de superfícies | `active` 0.3.0 |
| registro de transições | `active` 0.3.0 |
| detalhamentos granulares | `active` 0.2.0 |

## 8. Prioridade futura de materialização

A continuidade operacional de Coletivos deverá ser desenvolvida, em atos posteriores, na seguinte ordem:

```text
GKR-SURF-COL-002 — Visão Geral do Responsável
→ GKR-SURF-COL-003 — gestão completa de solicitações
→ GKR-SURF-PER-106 — Meus Coletivos
→ GKR-SURF-PER-107 — Central de Atualizações
→ GKR-SURF-PER-108 — Início do Participante
```

A ordem deriva das autoridades e transições registradas. Nenhuma superfície foi iniciada pela UXA-082.

## 9. Dívidas de validação

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

Essas dívidas permanecem separadas das lacunas de novas telas.

## 10. Limites

A UXA-082 não cria ou altera telas, contratos, SVGs, protótipo ou implementação. Também não promove as jornadas principais, corrige a galeria ou fecha lacunas.

## 11. Próxima evolução possível

**UXA-083 — Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção**, mediante autorização separada.
