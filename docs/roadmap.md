---
id: ROADMAP-12.51.0
title: Roadmap Arquitetural — Reformulação Granular Controlada Concluída
status: active
version: 12.51.0
owner: Guivos
last_updated: 2026-08-05
supersedes_partial:
  - ROADMAP-12.50.0
related:
  - GKR-STATE-001
  - GPA-007
  - UXA-000
  - UXA-014
  - UXA-015
  - UXA-016
  - UXA-017
  - UXA-018
  - UXA-019
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
  - UXA-055
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-061
  - UXA-062
  - UXA-063
  - UXA-064
  - UXA-065
  - UXA-066
  - UXA-067
  - UXA-068
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.72
---

# Roadmap Arquitetural — Reformulação Granular Controlada Concluída

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | cinco bloqueios da validação granular corrigidos documentalmente; revalidação ainda não iniciada | UXA-077; UXA-078; M7.72 |
| Início protegido geral | 4 SVGs materializados e validados no escopo de origem | UXA-034; UXA-035 |
| Compreensão inicial | 5 SVGs materializados e validados no escopo de origem | UXA-036; UXA-037 |
| Expressão guiada | 8 SVGs materializados, reformulados e validados no escopo de origem | UXA-068; UXA-069 |
| Fundação de Organizações e Coletivos | estruturada | UXA-014 a UXA-019 |
| Contratos de Coletivos | concluídos | UXA-056 a UXA-058 |
| Programa de Coletivos | 88 estados em P0A–P2 | UXA-059 |
| Coletivos materializados | 22 SVGs materializados e validados na perspectiva coberta | UXA-060 a UXA-067 |
| Opportunity Boost | 46 materializados; 36 validados; 10 estados da UXA-055 pendentes | UXA-038 a UXA-055 |
| Jornadas Integradas | seção e instrumentos de apoio `active`; vistas principais `draft` | UXA-070 a UXA-075 |
| Registro granular de superfícies | 40 entradas em `draft` 0.2.0 | UXA-076; UXA-078 |
| Registro granular de transições | 37 entradas em `draft` 0.2.0 | UXA-076; UXA-078 |
| Revalidação granular | não iniciada | UXA-079 |
| Resultados Empresariais | 18 decisões; zero canônicos | BA-STR-002-CODR-001 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência das Jornadas Integradas

```text
UXA-070 — programa funcional concluído
→ UXA-071 — primeira materialização documental integrada
→ UXA-072 — validação funcional não aprovada até reformulação
→ UXA-073 — reformulação, navegação e sincronização executadas
→ UXA-074 — revalidação aprovada com ressalvas no escopo documental
→ UXA-075 — promoção seletiva e sincronização pós-validação executadas
→ UXA-076 — registros granulares materializados em draft
→ UXA-077 — validação granular não aprovada até correção obrigatória
→ UXA-078 — reformulação controlada executada
→ UXA-079 — revalidação, somente mediante autorização separada
→ promoção granular, somente se o parecer futuro permitir e mediante novo ato
→ protótipo, somente mediante autorização posterior
→ Engenharia de Produto, somente após gates próprios
```

Nenhuma etapa inicia automaticamente a seguinte.

## 4. Correções concluídas pela UXA-078

| Achado | Correção documental |
|---|---|
| endpoints sem ID | todos os endpoints passam a IDs registrados; fronteira externa recebe `GKR-SURF-BND-001` |
| busca de Coletivos usada como oportunidades | mapa, lista e detalhe recebem IDs próprios |
| publicação institucional misturada com detalhe | `GKR-SURF-ORG-003` e `GKR-SURF-PER-203` são separados |
| estados residuais com fonte incorreta | `GKR-SURF-COM-005` e `GKR-TRN-305` apontam para UXA-055 |
| campos obrigatórios ausentes | matriz por ID registra artefato, caminho, versão, decisão, dados, gate, reversibilidade, supersessão e escopo |

## 5. Estado quantitativo reformulado

| Registro | Antes | Depois | Estado |
|---|---:|---:|---|
| superfícies, estados, responsabilidades ou fronteiras | 36 | 40 | `draft` |
| transições | 34 | 37 | `draft` |
| endpoints em texto livre | 2 | 0 | corrigidos documentalmente |

A variação quantitativa não significa novas funcionalidades. Ela expressa divisão de responsabilidades anteriormente misturadas.

## 6. Domínios separados

### Coletivos

`GKR-SURF-PER-102` permanece exclusivo da busca de Coletivos.

### Oportunidades

```text
GKR-SURF-ORG-003 — estado institucional
→ GKR-SURF-PER-201 — mapa
↔ GKR-SURF-PER-202 — lista
→ GKR-SURF-PER-203 — detalhe
→ GKR-SURF-BND-001 — fronteira externa
```

A sequência é documental e permanece parcial ou não examinada conforme cada transição.

### Opportunity Boost

A fonte específica dos dez estados residuais é UXA-055. A validação desses estados continua pendente.

## 7. Estado documental após UXA-078

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | `active` |
| Pessoa, Coletivo e Organização | `draft` por incompletude explícita |
| handoffs, cenários e catálogo agregado | `active` dentro dos limites da UXA-074 |
| lacunas | `active`, observacional e não promocional |
| registro granular de superfícies | `draft` 0.2.0; reformulado |
| registro granular de transições | `draft` 0.2.0; reformulado |
| revalidação granular | não iniciada |
| protótipo, aplicação e motor | não iniciados |
| Engenharia de Produto | não iniciada |

## 8. Lacunas preservadas

Permanecem abertas:

- ligação entre compreensão inicial e Tela Hoje;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- operação bilateral de solicitações;
- relação Organização–Coletivo materializada;
- matriz institucional completa;
- validação dos dez estados residuais do Opportunity Boost;
- integração publicação–descoberta;
- sincronização integrada entre mapa, lista e detalhe;
- efeitos externos de oportunidades;
- matriz integrada de erros, retornos e interrupções.

## 9. Próxima iniciativa possível

A próxima iniciativa documental possível é:

> **UXA-079 — Revalidação Funcional dos Registros Granulares Reformulados**

O pacote futuro deverá verificar:

- resolução completa dos endpoints;
- coerência dos novos IDs;
- separação real entre Coletivos, oportunidades e publicação institucional;
- rastreabilidade de UXA-055;
- presença e qualidade dos campos obrigatórios;
- ausência de novas inferências;
- coerência entre registros, catálogo, lacunas e estado global.

## 10. Frentes preservadas

Não são reabertas automaticamente:

- UXA-079;
- promoção dos registros;
- lacunas de produto;
- Resultados Empresariais;
- preços ou baseline comercial;
- política jurídica;
- protótipo;
- testes com pessoas;
- aplicação ou motor de simulação;
- Engenharia de Produto.

## 11. Regra de autorização

A integração da UXA-078 registrará somente a reformulação documental. Ela não iniciará a UXA-079, não aprovará os registros e não autorizará frente de produto ou implementação.

Cada pacote exige autorização própria para criação e autorização separada para integração.
