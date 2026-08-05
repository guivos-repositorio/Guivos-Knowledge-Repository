---
id: GKR-JOURNEYS-001
title: Jornadas Integradas
status: active
version: 0.8.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
related:
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
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - GKR-JOURNEY-SECTION-CLARIFICATION-001
normative: false
---

# Jornadas Integradas

## 1. Finalidade

Esta seção reúne, por referência, as jornadas da **Pessoa**, do **Coletivo** e da **Organização** para permitir leitura contínua, comparação de perspectivas, inspeção de handoffs e identificação de lacunas.

Ela não substitui contratos, programas, wireframes, validações ou registros canônicos. Em caso de divergência, prevalece o artefato de origem.

## 2. Como utilizar

1. escolha o participante ou cenário;
2. percorra os nós e transições;
3. confira separadamente maturidade, autoridade, materialização e validação;
4. verifique se a continuidade integrada foi examinada;
5. observe retornos, contestações e interrupções;
6. consulte o catálogo agregado;
7. localize superfícies e transições por ID;
8. considere os pareceres das UXA-077 e UXA-079, as correções da UXA-078 e a promoção da UXA-080;
9. acompanhe as lacunas sem tratá-las como fechadas.

## 3. Vistas disponíveis

- [Jornada da Pessoa](person.md)
- [Jornada do Coletivo](collective.md)
- [Jornada da Organização](organization.md)
- [Handoffs entre participantes](handoffs.md)
- [Cenários integrados](scenarios.md)
- [Catálogo de telas](screen-catalog.md)
- [Registro Granular de Superfícies e Estados](surface-registry.md)
- [Registro Granular de Transições](transition-registry.md)
- [Lacunas e continuidades ausentes](gaps.md)

## 4. Pacotes granulares

- [UXA-076 — materialização granular](../experience-architecture/uxa-076-integrated-journeys-granular-transition-and-surface-registry.md);
- [UXA-077 — validação funcional não aprovada](../experience-architecture/uxa-077-granular-registry-functional-validation.md);
- [UXA-078 — reformulação controlada](../experience-architecture/uxa-078-controlled-granular-registry-reformulation.md);
- [UXA-079 — revalidação funcional aprovada com ressalvas](../experience-architecture/uxa-079-granular-registry-functional-revalidation.md);
- [UXA-080 — promoção controlada dos registros granulares](../experience-architecture/uxa-080-controlled-granular-registry-promotion-and-post-revalidation-synchronization.md).

Resultado vigente:

```text
materialização granular
→ validação não aprovada
→ reformulação dos cinco achados
→ revalidação aprovada com ressalvas
→ promoção controlada dos instrumentos
→ registros vigentes sem promoção das jornadas ou fechamento de lacunas
```

## 5. Estado pós-promoção

| Camada | Estado | Referência |
|---|---|---|
| programa funcional | concluído | UXA-070 |
| primeira materialização documental | integrada | UXA-071 |
| primeira validação funcional | não aprovada até reformulação | UXA-072 |
| reformulação e navegação | executadas | UXA-073 |
| revalidação da seção | aprovada com ressalvas documentais | UXA-074 |
| promoção da seção | executada seletivamente | UXA-075 |
| primeira materialização granular | executada em `draft` | UXA-076 |
| primeira validação granular | não aprovada | UXA-077 |
| reformulação granular | executada | UXA-078 |
| revalidação granular | aprovada com ressalvas | UXA-079 |
| promoção granular | executada somente para os instrumentos de registro | UXA-080 |
| protótipo navegável | não iniciado | — |
| aplicação ou motor | não iniciado | — |
| Engenharia de Produto | não iniciada | W0-01 |

## 6. Resultado quantitativo

| Registro | Quantidade | Estado após UXA-080 |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | instrumento `active` 0.3.0 |
| transições documentais | 37 | instrumento `active` 0.3.0 |
| referências de endpoint | 74 | todas resolvidas por IDs registrados |
| endpoints em texto livre | 0 | aprovado |
| detalhamentos obrigatórios | 4 | instrumentos `active` 0.2.0 |

A promoção não declara novas telas implementadas e não altera as classificações internas.

## 7. Domínios separados

### 7.1 Coletivos

`GKR-SURF-PER-102` representa exclusivamente Resultados de Busca de Coletivos.

### 7.2 Oportunidades

| ID | Responsabilidade |
|---|---|
| GKR-SURF-ORG-003 | estado institucional de oportunidade aprovada ou ativa |
| GKR-SURF-PER-201 | Mapa de Oportunidades |
| GKR-SURF-PER-202 | Lista de Oportunidades |
| GKR-SURF-PER-203 | Detalhe de Oportunidade |
| GKR-SURF-BND-001 | fronteira externa identificada |

### 7.3 Opportunity Boost

`GKR-SURF-COM-005` e `GKR-TRN-305` apontam para UXA-055. Os dez estados residuais continuam sem validação funcional específica.

## 8. Regra da promoção granular

O status `active` dos registros significa que eles são instrumentos documentais vigentes e aprovados no escopo declarado.

A promoção não:

- altera a maturidade das 40 entradas;
- altera os estados das 37 transições;
- converte lacunas em continuidades;
- promove as jornadas da Pessoa, Coletivo ou Organização;
- cria implementação.

Permanecem como ressalvas:

- campos de transição agregados;
- cobertura seletiva e não exaustiva;
- `COM` como agrupamento documental.

## 9. Modelo de evidência

Cada nó ou família separa:

| Campo | Significado |
|---|---|
| maturidade primária | um único estado controlado da UXA-070 |
| autoridade contratual | documento que governa a responsabilidade |
| referência materializada | documento, wireframe ou SVG existente |
| evidência de validação | pacote que validou a referência materializada |
| continuidade integrada | validada, parcial, ausente ou não examinada |

O registro de superfícies também explicita artefato e caminho, versão, decisão, dados, gate, reversibilidade, supersessão e observação de escopo.

```text
cobertura das superfícies
≠ cobertura das transições
≠ validação da jornada integrada
```

## 10. Regra de leitura

Uma sequência exibida é hipótese documental rastreável. Ela somente poderá ser declarada como jornada integrada completa quando nós, transições, autoridades, dados, retornos, interrupções e estados alternativos tiverem evidência suficiente.

Valores desconhecidos permanecem `indeterminado`, `ausente` ou `não examinado`.

## 11. Estado dos artefatos

- esta visão geral permanece `active`;
- as vistas de Pessoa, Coletivo e Organização permanecem `draft`;
- handoffs, cenários e catálogo permanecem `active` nos limites da UXA-074;
- os dois registros granulares estão `active` 0.3.0;
- os quatro detalhamentos granulares estão `active` 0.2.0;
- o registro de lacunas permanece `active` por ser observacional;
- inclusão ou promoção nesta seção não altera maturidade ou canonicidade das entradas.

## 12. Escopo vigente

O status `active` desta seção e dos registros não declara:

- jornadas completas;
- validação ponta a ponta;
- fechamento de lacunas;
- prontidão para protótipo;
- prontidão para implementação.

Nenhuma nova iniciativa é iniciada ou identificada automaticamente pela UXA-080. Qualquer incremento posterior dependerá de definição e autorização separadas.
