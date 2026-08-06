---
id: ROADMAP-12.55.0
title: Roadmap Arquitetural — Galeria Não Aprovada e Lacunas Repriorizadas
status: active
version: 12.55.0
owner: Guivos
last_updated: 2026-08-05
supersedes_partial:
  - ROADMAP-12.54.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-014
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-037
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
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.72
---

# Roadmap Arquitetural — Galeria Não Aprovada e Lacunas Repriorizadas

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | galeria validada como inventário, não aprovada para promoção e fila de lacunas corrigida por dependência | UXA-082; M7.72 |
| Registros granulares | 40 superfícies e 37 transições em instrumentos `active` | UXA-080 |
| Galeria visual | `draft` 0.2.0; reformulação obrigatória | UXA-082 |
| SVGs auditados | 97 existentes; 87 validados; 10 pendentes | UXA-081; UXA-082 |
| cobertura granular visual | 25 de 40 IDs | UXA-081 |
| Jornadas principais | Pessoa, Coletivo e Organização em `draft` | Jornadas Integradas |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência das Jornadas Integradas

```text
UXA-070 — programa funcional
→ UXA-071 — seção integrada
→ UXA-072 — validação não aprovada
→ UXA-073 — reformulação
→ UXA-074 — revalidação
→ UXA-075 — promoção seletiva
→ UXA-076 — registros granulares
→ UXA-077 — validação bloqueada
→ UXA-078 — correções
→ UXA-079 — revalidação granular
→ UXA-080 — promoção dos instrumentos
→ UXA-081 — galeria visual e auditoria
→ UXA-082 — validação da galeria não aprovada e priorização por dependência
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Resultado da UXA-082

| Dimensão | Resultado |
|---|---|
| inventário dos 97 SVGs | confirmado |
| vínculos canônicos | mecanicamente utilizáveis |
| galeria como sequência integrada | não aprovada |
| galeria como matriz de assertividade por tela | não aprovada |
| promoção da galeria | bloqueada |
| fila de lacunas | reorganizada por dependência |
| novas telas | não iniciadas |

Achados bloqueadores:

1. ordem funcional incorreta na página da Pessoa;
2. Home pública e Tela Hoje agrupadas no mesmo bloco;
3. ausência de rota integrada de inspeção;
4. rastreabilidade agrupada insuficiente por SVG;
5. divergência de versões documentais.

## 5. Próxima trilha documental

```text
reformular a galeria
→ revalidar a sequência de inspeção
→ promover somente se aprovada
→ iniciar, em ato separado, a lacuna priorizada
```

A próxima etapa autorizável é a reformulação controlada. Revalidação, promoção e materialização futura permanecem atos separados.

## 6. Prioridade futura de materialização

A continuidade operacional de Coletivos deverá respeitar:

```text
GKR-SURF-COL-002 — Visão Geral do Responsável
→ GKR-SURF-COL-003 — gestão completa de solicitações
→ GKR-SURF-PER-106 — Meus Coletivos
→ GKR-SURF-PER-107 — Central de Atualizações
→ GKR-SURF-PER-108 — Início do Participante
```

A ordem deriva das transições `GKR-TRN-112`, `GKR-TRN-108`, `GKR-TRN-110` e `GKR-TRN-111`.

Nenhuma dessas superfícies foi iniciada pela UXA-082.

## 7. Dívidas de validação em trilha própria

- compreensão inicial → Tela Hoje;
- publicação → mapa, lista e detalhe;
- dez estados residuais da UXA-055;
- efeito externo de oportunidades;
- erros, retornos e interrupções integrados.

A existência de telas nessas frentes não comprova continuidade.

## 8. Limites

A UXA-082 não:

- modifica SVGs;
- corrige a galeria;
- promove jornadas;
- fecha lacunas;
- inicia materialização;
- inicia protótipo;
- inicia teste com pessoas;
- inicia aplicação ou Engenharia de Produto.

## 9. Próxima iniciativa possível

> **UXA-083 — Reformulação Controlada da Galeria Visual Integrada e da Sequência de Inspeção**

A UXA-083 deverá corrigir os cinco achados da UXA-082 sem modificar os SVGs canônicos.

A etapa depende de autorização separada.

## 10. Regra de autorização

A integração da UXA-082 registrará somente o parecer, a fila corrigida e a sincronização documental. Ela não iniciará a UXA-083 nem qualquer lacuna priorizada.
