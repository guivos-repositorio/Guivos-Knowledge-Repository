---
id: UXA-000
title: Arquitetura da Experiência da Guivos
status: active
version: 0.86.0
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
  - UXA-058
  - UXA-059
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
  - UXA-091
  - UXA-092
  - UXA-093
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SCREEN-GALLERY-001
  - GKR-JOURNEY-SCREEN-TRACEABILITY-MATRIX-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - M7.80
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
| SVGs existentes | 107 |
| associações individuais | 107 |
| perfis de rastreabilidade | 27 |
| com validação funcional vigente | 96 |
| pendentes de validação específica | 11 |
| IDs com referência visual | 29 de 40 |
| responsabilidades sem SVG dedicado | 10 |

Os onze pendentes correspondem aos dez estados residuais da UXA-055 e à referência de `PER-107` materializada pela UXA-093.

## 4. Decisões estruturais preservadas

- conteúdo de origem permanece separado da ajuda temporária;
- ajuda ocorre somente após solicitação consciente;
- texto e voz são modalidades equivalentes;
- síntese não substitui fonte;
- desconhecido não é fato;
- solicitação não é aprovação;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- pausa não reduz reputação;
- pedido adicional não é obrigação de revelar;
- acessibilidade não é critério oculto de elegibilidade;
- recusa não é reputação ou sanção;
- autoridade é concedida e verificada, não criada por confirmação;
- estado obsoleto não pode sobrescrever estado canônico mais recente;
- repetição de interação ou entrega não pode duplicar efeito lógico;
- `Meus Coletivos` separa participação, acompanhamento, solicitação, convite e pausa;
- `Meus Coletivos` não é ranking, score, sequência obrigatória, feed unificado ou Central de Atualizações;
- a Central de Atualizações preserva origem, natureza, contexto, autoridade, leitura, necessidade de ação e prazo;
- estado `lido` não equivale a concordância, consentimento, presença ou ação concluída;
- ordenação de atualizações não pode ser dominada por engajamento, popularidade, compra de plano ou publicidade silenciosa;
- aprovação forma vínculo antes da navegação posterior;
- aprovação não cria função, autoridade, notificação ou presença obrigatória;
- uma versão visual reformulada exige revalidação;
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
UXA-091 — Meus Coletivos materializada e continuidade pós-aprovação refinada
UXA-092 — Meus Coletivos e resultado aprovado reformulados/revalidados; TRN-108 validada integralmente
UXA-093 — Central de Atualizações materializada como referência P0A móvel
```

## 6. Resultado da UXA-093

[UXA-093 — Materialização Controlada da Central de Atualizações](uxa-093-collective-updates-center-materialization.md) materializa `GKR-SURF-PER-107` em um único SVG móvel, sem alterar ativos previamente validados e sem executar validação funcional da nova superfície.

A UXA-093 consolida:

1. Central como triagem de mudanças, não feed social genérico;
2. origem, tipo, contexto, autoridade, leitura, necessidade de ação e prazo como dimensões distintas;
3. ordenação legítima por segurança, ação, prazo, preferência e recência;
4. proibição de prioridade baseada em engajamento, popularidade, compra de plano ou publicidade silenciosa;
5. leitura separada de concordância, presença, consentimento ou ação concluída;
6. `PER-107` materializada, porém não validada;
7. `TRN-110` parcial mesmo com ambos os endpoints materializados;
8. `TRN-111` ausente porque `PER-108` permanece sem materialização vigente.

## 7. Instrumentos vigentes propostos

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` 0.21.0 |
| Jornada da Pessoa | `draft` 0.6.0 |
| Jornada do Coletivo | `draft` 0.10.0 |
| Jornada da Organização | `draft` |
| catálogo integrado | `active` 0.17.0 |
| galeria visual | `active` 0.12.0 |
| página de Coletivos | `active` 0.10.0 |
| demais páginas visuais | `active` 0.3.0 |
| matriz por SVG | `active` 0.10.0 |
| lacunas | `active` 0.18.0 |
| registro de superfícies | `active` 0.10.0 |
| registro de transições | `active` 0.10.0 |
| detalhamento da Pessoa | `active` 0.5.0 |
| detalhamento do Coletivo | `active` 0.6.0 |

## 8. Ressalvas vigentes

- 10 responsabilidades permanecem sem SVG dedicado;
- 11 SVGs permanecem sem validação específica vigente: dez UXA-055 + PER-107;
- `GKR-SURF-PER-107` está materializada, mas não validada;
- `GKR-TRN-110` permanece parcial;
- `GKR-TRN-111` permanece ausente;
- `GKR-SURF-PER-108` continua com reformulação pendente;
- estados P0B adicionais de `Meus Coletivos` e da Central permanecem separados;
- Jornadas da Pessoa e do Coletivo continuam `draft`;
- continuidades entre outros pacotes permanecem parciais ou não examinadas.

## 9. Prioridade de Coletivos

```text
GKR-SURF-COL-002 — validada
→ GKR-TRN-112 — integralmente validada
→ GKR-SURF-COL-003 — validada
↔ GKR-TRN-105/106/107/109 — integralmente validadas com PER-105
→ PER-105 aprovado — validado
→ GKR-TRN-108 — integralmente validada
→ GKR-SURF-PER-106 — validado
→ GKR-TRN-110 — parcial
→ GKR-SURF-PER-107 — materializado; validação pendente
→ GKR-TRN-111 — ausente
→ GKR-SURF-PER-108 — reformulação pendente
```

## 10. Dívidas de validação e materialização

- validar `PER-107` e `TRN-110` em frente posterior;
- `PER-108` em frente posterior;
- estados P0B adicionais de `PER-106` e `PER-107`;
- áreas P1 de comunicação especializada;
- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

## 11. Limites

A UXA-093 cria somente um novo SVG para `PER-107`. Não cria protótipo, implementação, teste com pessoas, componente técnico ou Engenharia de Produto. Também não valida `PER-107`/`TRN-110`, não materializa `PER-108`, estados P0B ou `COL-004` a `COL-008`.

## 12. Próxima evolução possível

**UXA-094 — Validação Funcional da Central de Atualizações e Revalidação de `GKR-TRN-110`**, mediante autorização separada.

A UXA-094 não foi iniciada.
