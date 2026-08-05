---
id: UXA-080
title: Promoção Controlada dos Registros Granulares e Sincronização Pós-Revalidação
status: active
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-05
parent: UXA-000
depends_on:
  - UXA-070
  - UXA-076
  - UXA-077
  - UXA-078
  - UXA-079
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
related:
  - GKR-JOURNEY-SURFACE-DETAIL-PERSON-001
  - GKR-JOURNEY-SURFACE-DETAIL-COLLECTIVE-001
  - GKR-JOURNEY-SURFACE-DETAIL-ORGANIZATION-001
  - GKR-JOURNEY-SURFACE-DETAIL-COMMERCIAL-001
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-GAPS-001
  - GKR-STATE-001
  - ROADMAP-12.53.0
  - M7.72
normative: false
---

# Promoção Controlada dos Registros Granulares e Sincronização Pós-Revalidação

## 1. Finalidade

A UXA-080 executa a decisão de status posterior ao parecer da UXA-079.

A UXA-079 aprovou, com ressalvas no escopo funcional documental, os registros granulares reformulados. Essa aprovação confirmou a integridade do instrumento de registro, mas não declarou jornadas completas, continuidade ponta a ponta ou implementação.

Este pacote decide explicitamente:

1. quais instrumentos granulares podem ser promovidos para `active`;
2. quais vistas continuam em `draft`;
3. como a promoção é sincronizada no estado global, roadmap e índices;
4. quais ressalvas e lacunas continuam abertas;
5. quais frentes permanecem não iniciadas.

## 2. Base

Base de criação:

```text
main
d635b0b319264ce0562cfb85b07288dc3214f002
```

Parecer governante: UXA-079, com resultado **aprovado com ressalvas no escopo funcional documental**.

## 3. Regra de promoção

O status `active` significa que o artefato é uma referência documental vigente, revalidada e aprovada para o escopo que declara.

Ele não significa:

- jornada completa;
- validação ponta a ponta;
- implementação de tela, estado ou transição;
- ausência de lacunas;
- alteração da maturidade individual das entradas;
- prontidão para protótipo;
- prontidão para Engenharia de Produto;
- canonicidade superior às autoridades referenciadas.

A promoção do registro não promove automaticamente os objetos registrados.

## 4. Decisão por artefato

| Artefato | Estado anterior | Decisão | Versão após decisão | Justificativa |
|---|---|---|---:|---|
| `docs/journeys/surface-registry.md` | `draft` | promover para `active` | 0.3.0 | inventário de 40 entradas revalidado e aprovado como instrumento documental |
| `docs/journeys/transition-registry.md` | `draft` | promover para `active` | 0.3.0 | registro de 37 transições e 74 endpoints revalidado e aprovado |
| `docs/journeys/surface-registry-person-details.md` | `draft` | promover para `active` | 0.2.0 | detalhamento obrigatório integrante do registro aprovado |
| `docs/journeys/surface-registry-collective-details.md` | `draft` | promover para `active` | 0.2.0 | detalhamento obrigatório integrante do registro aprovado |
| `docs/journeys/surface-registry-organization-details.md` | `draft` | promover para `active` | 0.2.0 | detalhamento obrigatório integrante do registro aprovado |
| `docs/journeys/surface-registry-commercial-boundary-details.md` | `draft` | promover para `active` | 0.2.0 | detalhamento obrigatório integrante do registro aprovado |
| `docs/journeys/person.md` | `draft` | manter `draft` | inalterada | continuidade pessoal ponta a ponta permanece incompleta |
| `docs/journeys/collective.md` | `draft` | manter `draft` | inalterada | operação do responsável e continuidades internas permanecem incompletas |
| `docs/journeys/organization.md` | `draft` | manter `draft` | inalterada | relação bilateral e matriz institucional permanecem incompletas |

## 5. Resultado quantitativo preservado

| Registro | Quantidade | Estado após promoção |
|---|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 40 | instrumento `active`; maturidades individuais preservadas |
| transições documentais | 37 | instrumento `active`; estados individuais preservados |
| referências de endpoint | 74 | resolvidas por IDs registrados |
| endpoints em texto livre | 0 | permanece aprovado |

A promoção não aumenta contagens e não cria novos comportamentos.

## 6. Ressalvas preservadas

### 6.1 Campos de transição agregados

Condição e ação, efeito e dados, além de reversibilidade, interrupção e tempo, continuam agrupados em colunas compostas.

### 6.2 Cobertura seletiva

Os registros continuam seletivos e não exaustivos. O status `active` não os transforma em inventário completo do ecossistema.

### 6.3 Camada comercial

O prefixo `COM` continua sendo agrupamento documental. Ele não cria participante estrutural adicional nem concede autoridade comercial sobre reputação, relevância ou decisão humana.

### 6.4 Continuidade integrada

Estados `parcial`, `ausente`, `contratada` e `não examinada` permanecem exatamente registrados. A promoção do instrumento não converte essas classificações em continuidade validada.

## 7. Lacunas preservadas

Permanecem abertas:

- continuidade entre compreensão inicial e Tela Hoje;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- operação bilateral de solicitações;
- relação Organização–Coletivo materializada;
- matriz institucional completa;
- validação dos dez estados residuais do Opportunity Boost;
- integração publicação–descoberta de oportunidades;
- sincronização integrada entre mapa, lista e detalhe;
- efeitos externos de oportunidades;
- matriz integrada de erros, retornos e interrupções.

## 8. Sincronização do estado global

A sequência passa a ser registrada como:

```text
UXA-076 — registros granulares materializados em draft
→ UXA-077 — validação granular não aprovada até correção obrigatória
→ UXA-078 — reformulação controlada executada
→ UXA-079 — revalidação aprovada com ressalvas no escopo funcional documental
→ UXA-080 — promoção controlada dos instrumentos granulares executada
```

A sincronização alcança:

- GKR-STATE-001 versão 2.06.0;
- ROADMAP-12.53.0;
- UXA-000 versão 0.73.0;
- GKR-JOURNEYS-001 versão 0.8.0;
- versões e status dos seis artefatos granulares promovidos.

## 9. Limites preservados

A UXA-080 não cria nem inicia:

- promoção das jornadas da Pessoa, Coletivo ou Organização;
- fechamento de lacunas;
- novos contratos, wireframes ou SVGs;
- protótipo navegável;
- aplicação ou motor de simulação;
- teste com pessoas;
- componentes técnicos;
- modelo de IA;
- APIs ou banco de dados;
- Engenharia de Produto.

Nenhuma entrada individual é reclassificada pela promoção.

## 10. Resultado controlado

> **Os dois registros granulares e seus quatro detalhamentos passam a possuir status documental vigente controlado, enquanto as três vistas de jornada permanecem em rascunho por incompletude explícita.**

## 11. Próxima evolução possível

Uma evolução posterior poderá tratar o próximo incremento das Jornadas Integradas, desde que definido e autorizado em pacote próprio.

Nenhuma nova UXA, frente de produto ou implementação é iniciada por este pacote.
