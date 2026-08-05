---
id: ROADMAP-12.50.0
title: Roadmap Arquitetural — Validação Granular Não Aprovada até Reformulação
status: active
version: 12.50.0
owner: Guivos
last_updated: 2026-08-05
supersedes_partial:
  - ROADMAP-12.49.0
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
  - UXA-077
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-SURFACE-REGISTRY-001
  - GKR-JOURNEY-TRANSITION-REGISTRY-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - M7.72
---

# Roadmap Arquitetural — Validação Granular Não Aprovada até Reformulação

## 1. Autoridade

Este documento governa a sequência global do Repositório. O estado oficial permanece no Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado | Referência |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | validação granular executada e não aprovada até correção obrigatória | UXA-077; M7.72 |
| Início protegido geral | 4 SVGs materializados e validados no escopo de origem | UXA-034; UXA-035 |
| Compreensão inicial | 5 SVGs materializados e validados no escopo de origem | UXA-036; UXA-037 |
| Expressão guiada | 8 SVGs materializados, reformulados e validados no escopo de origem | UXA-068; UXA-069 |
| Fundação de Organizações e Coletivos | estruturada | UXA-014 a UXA-019 |
| Contratos de Coletivos | concluídos | UXA-056 a UXA-058 |
| Programa de Coletivos | 88 estados em P0A–P2 | UXA-059 |
| Coletivos materializados | 22 SVGs materializados e validados na perspectiva coberta | UXA-060 a UXA-067 |
| Opportunity Boost | 46 materializados; 36 validados; 10 pendentes | UXA-038 a UXA-055 |
| Jornadas Integradas | seção e instrumentos de apoio `active`; vistas de Pessoa, Coletivo e Organização `draft` | UXA-070 a UXA-075 |
| Registros granulares | 36 superfícies ou responsabilidades e 34 transições em `draft` | UXA-076 |
| Validação granular | não aprovada até correção de cinco achados | UXA-077 |
| Resultados Empresariais | 18 decisões; zero canônicos | BA-STR-002-CODR-001 |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Jornada pessoal relacionada

```text
UXA-020 e UXA-023 — início protegido contratado e reformulado
→ UXA-034 e UXA-035 — escolha, rascunho, inventário e autorização materializados e validados
→ UXA-068 — expressão guiada materializada
→ UXA-069 — expressão guiada reformulada e validada
→ UXA-036 e UXA-037 — processamento e compreensão inicial materializados e validados
```

A continuidade integrada entre todos os pacotes ainda não está completa, especialmente na ligação com a Tela Hoje, registrada como `GKR-TRN-007` e mantida como não examinada.

## 4. Cobertura preservada

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Início protegido geral | 4 | 4 | 0 |
| Compreensão inicial | 5 | 5 | 0 |
| Expressão Guiada do Momento Atual | 8 | 8 | 0 |
| Coletivos | 22 | 22 | demais famílias não materializadas |
| Opportunity Boost | 46 | 36 | 10 estados da UXA-055 |

As contagens não demonstram automaticamente cobertura de transições ou validação ponta a ponta.

## 5. Estado de Coletivos preservado

Permanecem ausentes:

- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- operação completa das solicitações pelo Coletivo;
- continuidade bilateral após `Solicitação Pendente`.

A busca de Coletivos não poderá ser reutilizada como busca ou catálogo de oportunidades na reformulação granular.

## 6. Sequência das Jornadas Integradas

```text
UXA-070 — programa funcional concluído
→ UXA-071 — primeira materialização documental integrada
→ UXA-072 — validação funcional não aprovada até reformulação
→ UXA-073 — reformulação, navegação e sincronização executadas
→ UXA-074 — revalidação aprovada com ressalvas no escopo documental
→ UXA-075 — promoção seletiva e sincronização pós-validação executadas
→ UXA-076 — registros granulares materializados em draft
→ UXA-077 — validação granular não aprovada até correção obrigatória
→ UXA-078 — reformulação controlada, somente mediante autorização separada
→ nova validação, somente após reformulação
→ protótipo, somente mediante autorização posterior
→ Engenharia de Produto, somente após gates próprios
```

Nenhuma etapa inicia automaticamente a seguinte.

## 7. Resultado da UXA-077

A validação confirmou:

- 36 entradas de superfície, estado, responsabilidade ou ausência;
- 34 transições;
- IDs sem duplicidade dentro de cada registro;
- vocabulário de maturidade aderente à UXA-070;
- preservação de ligações parciais, ausentes, contratadas e não examinadas;
- ausência de promoção ou implementação implícita.

O parecer foi **não aprovado até correção obrigatória** devido a:

1. endpoints sem identificador estável;
2. mistura entre busca de Coletivos e descoberta de oportunidades;
3. mistura entre publicação institucional e Detalhe de Oportunidade;
4. referência incorreta dos dez estados residuais, cuja fonte é UXA-055;
5. campos obrigatórios ausentes no registro de superfícies.

## 8. Estado documental após UXA-077

| Artefato | Estado |
|---|---|
| visão geral das Jornadas Integradas | active |
| Pessoa, Coletivo e Organização | draft por incompletude explícita |
| handoffs, cenários e catálogo agregado | active dentro dos limites da UXA-074 |
| lacunas | active, observacional e não promocional |
| registro granular de superfícies | draft; validação não aprovada |
| registro granular de transições | draft; validação não aprovada |
| reformulação granular | não iniciada |
| protótipo, aplicação e motor | não iniciados |
| Engenharia de Produto | não iniciada |

## 9. Escopo mínimo da UXA-078

Uma reformulação futura deverá:

- resolver todos os endpoints por ID;
- criar superfícies próprias para mapa, lista, cartão e detalhe de oportunidades;
- separar o estado institucional de publicação da superfície percebida pela Pessoa;
- corrigir a rastreabilidade dos estados residuais para UXA-055;
- completar artefato e caminho, versão, decisão, dados, gate, reversibilidade, supersessão e observação de escopo;
- preservar IDs cujo significado não mudar;
- registrar divisões ou supersessões de entradas;
- manter estados desconhecidos e lacunas explícitos.

## 10. Ressalvas e lacunas vigentes

Permanecem abertas:

- cinco achados obrigatórios da UXA-077;
- ligação entre compreensão inicial e Tela Hoje;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- operação bilateral de solicitações;
- relação Organização–Coletivo materializada;
- matriz institucional completa;
- validação dos dez estados residuais do Opportunity Boost;
- efeitos externos de oportunidades;
- matriz integrada de erros, retornos e interrupções.

## 11. Frentes preservadas

Não são reabertas automaticamente:

- UXA-078;
- lacunas de produto;
- estados residuais do Opportunity Boost;
- Resultados Empresariais;
- preços ou baseline comercial;
- política jurídica;
- protótipo;
- testes com pessoas;
- aplicação ou motor de simulação;
- Engenharia de Produto.

## 12. Regra de autorização

A integração da UXA-077 registrará apenas o parecer funcional e a necessidade de reformulação. Ela não corrigirá os registros, não iniciará a UXA-078 e não autorizará qualquer frente de produto ou implementação.

Cada pacote exige autorização própria para criação e autorização separada para integração.
