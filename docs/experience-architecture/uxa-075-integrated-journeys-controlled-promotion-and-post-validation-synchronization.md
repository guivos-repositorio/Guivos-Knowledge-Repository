---
id: UXA-075
title: Promoção Controlada e Sincronização Pós-Validação das Jornadas Integradas
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - UXA-071
  - UXA-072
  - UXA-073
  - UXA-074
  - GKR-JOURNEYS-001
related:
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-HANDOFFS-001
  - GKR-JOURNEY-SCENARIOS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.48.0
  - M7.72
normative: false
---

# Promoção Controlada e Sincronização Pós-Validação das Jornadas Integradas

## 1. Finalidade

A UXA-075 executa a decisão de status e a sincronização posterior ao parecer da UXA-074.

A UXA-074 aprovou, com ressalvas, a seção **Jornadas Integradas** como instrumento documental de leitura, rastreabilidade e governança. Essa aprovação não declarou jornadas completas e não autorizou promoção automática de todos os artefatos.

Este pacote decide explicitamente:

1. quais documentos podem ser promovidos para `active`;
2. quais devem permanecer `draft`;
3. como o resultado da UXA-074 passa a ser registrado no estado global;
4. quais ressalvas continuam abertas;
5. qual evolução documental poderá ser considerada posteriormente.

## 2. Base

Base de criação: `main` em `522cdcfa9b8825d406a4cd0f282a36ae4c968c1f`.

Parecer governante: UXA-074, com resultado **aprovado com ressalvas no escopo documental**.

## 3. Regra de promoção

O status `active` significa que o artefato é uma referência documental vigente e aprovada para o escopo que declara.

Ele não significa:

- jornada completa;
- validação ponta a ponta;
- ausência de lacunas;
- prontidão para protótipo;
- prontidão para Engenharia de Produto;
- canonicidade superior às autoridades referenciadas.

Um artefato permanece `draft` quando sua função principal é representar uma jornada ainda incompleta, mesmo que a forma de registrar essa incompletude tenha sido aprovada.

## 4. Decisão por artefato

| Artefato | Estado anterior | Decisão | Justificativa |
|---|---|---|---|
| `docs/journeys/index.md` | draft | promover para `active` | a seção foi aprovada como área documental navegável e governada |
| `docs/journeys/person.md` | draft | manter `draft` | a jornada pessoal ainda não possui continuidade integrada ponta a ponta |
| `docs/journeys/collective.md` | draft | manter `draft` | operação do responsável, vínculo e continuidades bilaterais permanecem incompletos |
| `docs/journeys/organization.md` | draft | manter `draft` | relação Organização–Coletivo e matriz institucional completa permanecem ausentes |
| `docs/journeys/handoffs.md` | draft | promover para `active` | a matriz resumida foi aprovada como instrumento vigente, com ressalva de não exaustividade |
| `docs/journeys/scenarios.md` | draft | promover para `active` | os cenários foram aprovados como hipóteses documentais governadas e limitadas pela evidência |
| `docs/journeys/screen-catalog.md` | draft | promover para `active` | o catálogo agregado foi aprovado, com granularidade individual futura |
| `docs/journeys/gaps.md` | active | manter `active` | registro observacional e não promocional já aprovado |

## 5. Versões após a decisão

| Artefato | Versão | Status |
|---|---:|---|
| visão geral | 0.3.0 | active |
| Pessoa | 0.3.0 | draft |
| Coletivo | 0.3.0 | draft |
| Organização | 0.3.0 | draft |
| handoffs | 0.3.0 | active |
| cenários | 0.3.0 | active |
| catálogo | 0.3.0 | active |
| lacunas | 0.3.0 | active |

## 6. Ressalvas preservadas

### 6.1 Handoffs

A matriz é vigente como síntese governada, mas não é um cadastro exaustivo de cada transição, dado, efeito, tempo e interrupção.

### 6.2 Catálogo

O catálogo é vigente como inventário agregado por família, mas ainda não contém uma linha individual para cada tela, estado e transição.

### 6.3 Jornadas incompletas

Permanecem abertas, entre outras:

- continuidade entre compreensão inicial e Tela Hoje;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- gestão bilateral de solicitações;
- relação Organização–Coletivo materializada;
- matriz institucional completa;
- 10 estados residuais do Opportunity Boost;
- efeitos externos de oportunidades.

Essas lacunas não invalidam a seção documental, mas impedem promover as vistas de Pessoa, Coletivo e Organização como jornadas vigentes completas.

## 7. Sincronização do estado global

A sequência passa a ser registrada como:

```text
UXA-070 — programa funcional concluído
→ UXA-071 — primeira materialização documental integrada
→ UXA-072 — primeira validação não aprovada
→ UXA-073 — reformulação, navegação e sincronização executadas
→ UXA-074 — revalidação aprovada com ressalvas no escopo documental
→ UXA-075 — promoção seletiva e sincronização pós-validação executadas
```

A sincronização alcança:

- GKR-STATE-001 versão 2.01.0;
- ROADMAP-12.48.0;
- UXA-000 versão 0.68.0;
- navegação da Arquitetura da Experiência;
- versões e status dos oito artefatos em `docs/journeys/`.

## 8. Limites preservados

A UXA-075 não cria nem inicia:

- protótipo navegável;
- aplicação ou motor de simulação;
- teste com pessoas;
- componentes técnicos;
- modelo de IA;
- APIs ou banco de dados;
- Product Engineering;
- fechamento de qualquer lacuna de produto;
- materialização de novas telas ou transições.

Nenhum contrato, wireframe ou SVG canônico é alterado.

## 9. Resultado controlado

> **A seção Jornadas Integradas e seus instrumentos documentais de apoio passam a possuir status vigente controlado, enquanto as três vistas de jornada permanecem em rascunho por incompletude explícita.**

A promoção seletiva não altera a maturidade das superfícies referenciadas e não transforma hipóteses documentais em jornadas completas.

## 10. Próxima evolução documental possível

Uma evolução posterior poderá ser:

**UXA-076 — Registro Granular de Transições e Superfícies das Jornadas Integradas**, mediante autorização separada.

Esse pacote poderá detalhar, individualmente:

- cada tela e estado;
- transições de entrada e saída;
- dados transferidos;
- efeito e tempo;
- retorno, interrupção e contestação;
- autoridade e evidência aplicável.

A UXA-076 não é iniciada por este pacote.
