---
id: ROADMAP-12.49.0
title: Roadmap Arquitetural — Registros Granulares das Jornadas Integradas
status: active
version: 12.49.0
owner: Guivos
last_updated: 2026-08-05
supersedes_partial:
  - ROADMAP-12.48.0
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
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.72
---

# Roadmap Arquitetural — Registros Granulares das Jornadas Integradas

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | Jornadas Integradas aprovadas com ressalvas, promovidas seletivamente e detalhadas granularmente | UXA-074 a UXA-076; M7.72 |
| Início protegido geral | 4 SVGs materializados e validados no escopo de origem | UXA-034; UXA-035 |
| Compreensão inicial | 5 SVGs materializados e validados no escopo de origem | UXA-036; UXA-037 |
| Expressão guiada | 8 SVGs materializados, reformulados e validados no escopo de origem | UXA-068; UXA-069 |
| Fundação de Organizações e Coletivos | estruturada | UXA-014 a UXA-019 |
| Contratos de Coletivos | concluídos | UXA-056 a UXA-058 |
| Programa de Coletivos | 88 estados em P0A–P2 | UXA-059 |
| Coletivos materializados | 22 SVGs materializados e validados na perspectiva coberta | UXA-060 a UXA-067 |
| Opportunity Boost | 46 materializados; 36 validados; 10 pendentes | UXA-038 a UXA-055 |
| Jornadas Integradas | seção e instrumentos de apoio `active`; vistas de Pessoa, Coletivo e Organização `draft` | UXA-070 a UXA-075 |
| Registros granulares | superfícies e transições materializadas em `draft` | UXA-076 |
| Resultados Empresariais | 18 decisões; zero canônicos | BA-STR-002-CODR-001 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência concluída da jornada pessoal relacionada

```text
UXA-020 e UXA-023 — início protegido contratado e reformulado
→ UXA-034 e UXA-035 — escolha, rascunho, inventário e autorização materializados e validados
→ UXA-068 — expressão guiada materializada
→ UXA-069 — expressão guiada reformulada e validada
→ UXA-036 e UXA-037 — processamento e compreensão inicial materializados e validados
```

A ordem funcional permanece:

```text
escolha
→ expressão guiada
→ inventário e autorização
→ processamento
→ compreensão inicial
→ continuidade recorrente
```

A continuidade integrada entre todos os pacotes ainda não está completa, especialmente na ligação com a Tela Hoje.

## 4. Cobertura relacionada

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Início protegido geral | 4 | 4 | 0 |
| Compreensão inicial | 5 | 5 | 0 |
| Expressão Guiada do Momento Atual | 8 | 8 | 0 |
| **Subtotal relacionado** | **17** | **17** | **0** |

As contagens demonstram cobertura de superfícies nos respectivos pacotes. Não demonstram automaticamente cobertura de transições ou validação ponta a ponta.

## 5. Estado de Coletivos preservado

```text
UXA-056 — descoberta, Perfil Público e participação contratados
→ UXA-057 — avaliação e reputação contratadas
→ UXA-058 — interação, recomendação e conexão contratadas
→ UXA-059 — programa de wireframes priorizado
→ UXA-060 a UXA-067 — cinco primeiras referências P0A materializadas e validadas na perspectiva da Pessoa
```

Permanecem ausentes:

- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- operação completa das solicitações pelo Coletivo;
- continuidade bilateral após `Solicitação Pendente`.

## 6. Sequência das Jornadas Integradas

```text
UXA-070 — programa funcional concluído
→ UXA-071 — primeira materialização documental integrada
→ UXA-072 — validação funcional não aprovada até reformulação
→ UXA-073 — reformulação, navegação e sincronização executadas
→ UXA-074 — revalidação aprovada com ressalvas no escopo documental
→ UXA-075 — promoção seletiva e sincronização pós-validação executadas
→ UXA-076 — registros granulares materializados em draft
→ UXA-077 — validação granular, somente mediante autorização separada
→ protótipo, somente mediante autorização posterior
→ Engenharia de Produto, somente após gates próprios
```

Nenhuma etapa inicia automaticamente a seguinte.

## 7. Resultado da UXA-076

A UXA-076 cria:

- um registro granular de superfícies, estados, responsabilidades e ausências conhecidas;
- um registro granular de transições, incluindo ligações localmente validadas, parciais, contratadas, ausentes e não examinadas;
- identificadores estáveis para rastrear lacunas e handoffs;
- vínculos entre catálogo agregado, matriz de handoffs e fila de lacunas.

Os registros permanecem `draft` e não:

- validam jornadas ponta a ponta;
- materializam interfaces ausentes;
- fecham lacunas;
- promovem as vistas de Pessoa, Coletivo ou Organização;
- iniciam protótipo ou implementação.

## 8. Estado documental após UXA-076

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | active |
| Pessoa, Coletivo e Organização | draft por incompletude explícita |
| handoffs, cenários e catálogo agregado | active dentro dos limites da UXA-074 |
| lacunas | active, observacional e não promocional |
| registro granular de superfícies | draft |
| registro granular de transições | draft |
| validação granular | não iniciada |

## 9. Ressalvas e lacunas vigentes

Permanecem abertas:

- validação funcional dos registros granulares;
- ligação entre compreensão inicial e Tela Hoje;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- operação bilateral de solicitações;
- relação Organização–Coletivo materializada;
- matriz institucional completa;
- 10 estados residuais do Opportunity Boost;
- efeitos externos de oportunidades;
- matriz integrada de erros, retornos e interrupções.

## 10. Próxima iniciativa documental possível

A próxima iniciativa possível é:

> **UXA-077 — Validação Funcional do Registro Granular de Transições e Superfícies**

O pacote futuro deverá verificar:

- unicidade e estabilidade dos identificadores;
- correspondência entre registros e fontes canônicas;
- classificação correta de maturidade e estado de transição;
- ausência de ligações inventadas;
- cobertura dos campos exigidos pela UXA-070;
- coerência com handoffs, catálogo e lacunas;
- limites de uso dos registros.

## 11. Frentes preservadas

Não são reabertas automaticamente:

- UXA-077;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante;
- Visão Geral do Responsável;
- relação bilateral Organização–Coletivo;
- estados residuais do Opportunity Boost;
- Resultados Empresariais;
- preços ou baseline comercial;
- política jurídica;
- protótipo;
- testes com pessoas;
- aplicação ou motor de simulação;
- Engenharia de Produto.

## 12. Regra de autorização

A integração da UXA-076 registrará a materialização granular. Ela não iniciará a UXA-077 e não autorizará qualquer frente de produto ou implementação.

Cada pacote exige autorização própria para criação e autorização separada para integração.
