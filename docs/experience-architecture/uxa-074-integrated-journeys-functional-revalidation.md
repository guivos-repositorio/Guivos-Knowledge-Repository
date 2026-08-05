---
id: UXA-074
title: Nova Validação Funcional das Jornadas Integradas Reformuladas
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
  - ROADMAP-12.47.0
  - M7.72
normative: false
---

# Nova Validação Funcional das Jornadas Integradas Reformuladas

## 1. Finalidade

A UXA-074 executa a nova validação funcional da seção **Jornadas Integradas** após a reformulação, a inclusão na navegação e a sincronização realizadas pela UXA-073.

O objetivo é verificar se os dez achados registrados pela UXA-072 foram efetivamente tratados e se a seção já funciona como instrumento documental de leitura, comparação de perspectivas, rastreabilidade, inspeção de handoffs e exposição de lacunas dentro do Guivos Knowledge Repository.

Esta validação não corresponde a:

- teste de usabilidade com pessoas;
- execução de software;
- validação de uma aplicação ou motor de simulação;
- confirmação de que todas as jornadas estão completas;
- fechamento automático de lacunas;
- promoção automática dos mapas para `active`;
- autorização de protótipo ou Engenharia de Produto.

## 2. Base auditada

Base da validação: `main` em `96d9a7e5316127141165bca0c19332911f14d026`.

Foram examinados:

1. `mkdocs.yml`;
2. `docs/project/current-state-register.md`;
3. `docs/roadmap.md`;
4. `docs/experience-architecture/index.md`;
5. `docs/experience-architecture/uxa-070-journey-simulation-environment-functional-program.md`;
6. `docs/experience-architecture/uxa-071-integrated-journeys-map-materialization.md`;
7. `docs/experience-architecture/uxa-072-integrated-journeys-functional-validation-and-reformulation.md`;
8. `docs/experience-architecture/uxa-073-integrated-journeys-reformulation-navigation-and-synchronization.md`;
9. `docs/journeys/index.md`;
10. `docs/journeys/person.md`;
11. `docs/journeys/collective.md`;
12. `docs/journeys/organization.md`;
13. `docs/journeys/handoffs.md`;
14. `docs/journeys/scenarios.md`;
15. `docs/journeys/screen-catalog.md`;
16. `docs/journeys/gaps.md`.

## 3. Método

Cada critério recebeu uma das classificações:

| Resultado | Significado |
|---|---|
| aprovado | requisito demonstrado sem correção obrigatória |
| aprovado com ressalva | requisito demonstrado, com limite não bloqueador explicitado |
| parcial | parte do requisito demonstrada e parte ainda insuficiente |
| reprovado | requisito não atendido ou contradito pela evidência |
| não aplicável | requisito fora do escopo documental |

A validação diferencia três objetos:

```text
validade funcional da seção documental
≠ completude das jornadas representadas
≠ prontidão para protótipo ou implementação
```

## 4. Parecer executivo

> **Resultado: aprovado com ressalvas no escopo documental.**

A UXA-073 eliminou os quatro bloqueios estruturais e tratou os seis achados complementares registrados pela UXA-072.

A seção agora:

- está acessível como área de primeiro nível no GKR;
- possui estado global, roadmap e índice UXA coerentes com a sequência vigente;
- utiliza os estados controlados da UXA-070;
- separa maturidade, autoridade, materialização, validação e continuidade integrada;
- diferencia superfícies validadas de transições e jornadas integradas;
- explicita assimetrias entre Pessoa, Coletivo e Organização;
- limita cenários à evidência disponível;
- distingue inventário de telas e cobertura de transições;
- preserva os mapas como `draft` durante a validação;
- mantém as lacunas como registro observacional e não promocional.

As ressalvas não reabrem a reformulação obrigatória. Elas delimitam que:

1. a aprovação se aplica ao funcionamento da seção como instrumento documental;
2. os mapas não demonstram jornadas completas ou validadas ponta a ponta;
3. a matriz de handoffs permanece uma síntese e não substitui um registro exaustivo de cada transição;
4. o catálogo permanece agregado por famílias e ainda não é um cadastro individual completo de cada tela e estado;
5. a integração deste parecer exigirá sincronização posterior dos registros centrais e decisão explícita sobre promoção de status.

## 5. Resultado dos critérios da UXA-073

| Critério | Resultado | Evidência | Conclusão |
|---|---|---|---|
| presença e ordem da seção na navegação | aprovado | `mkdocs.yml` contém `Jornadas Integradas` como seção de primeiro nível e UXA-070 a UXA-073 na Arquitetura da Experiência | bloqueio F01 encerrado |
| ausência de contradições nos registros centrais | aprovado | GKR-STATE-001 2.00.0, ROADMAP-12.47.0 e UXA-000 0.67.0 descrevem a mesma sequência | bloqueios F02 a F04 encerrados |
| um único estado de maturidade primária por linha | aprovado | tabelas usam estados individuais da seção 10 da UXA-070 | bloqueio F05 encerrado |
| separação entre autoridade, materialização e validação | aprovado | colunas independentes nas vistas de Pessoa, Coletivo e Organização | modelo de evidência aplicado |
| continuidade parcial, ausente ou não examinada explícita | aprovado | todas as vistas registram limites sem preenchimento por inferência | falsa completude removida |
| handoffs sem falsa equivalência bilateral | aprovado com ressalva | origem e destino possuem maturidades distintas e assimetrias explícitas | F07 encerrado; registro exaustivo continua futuro |
| cenários limitados à evidência disponível | aprovado | seis cenários possuem nós, transições, interrupção e conclusões permitidas ou proibidas | F08 encerrado |
| catálogo distinguindo superfícies de transições | aprovado com ressalva | entradas e saídas integradas aparecem separadas | F09 encerrado; granularidade individual permanece futura |
| mapas preservados como `draft` | aprovado | visão geral e seis vistas analíticas permanecem `draft` | promoção automática não ocorreu |
| lacunas observacionais e não promocionais | aprovado | GKR-JOURNEY-GAPS-001 está `active` com natureza explicitamente observacional | F10 encerrado |

## 6. Verificação dos achados da UXA-072

### 6.1 UXA-072-F01 — Seção ausente da navegação

**Estado:** encerrado.

`Jornadas Integradas` existe na navegação de primeiro nível com acesso a:

- Visão Geral;
- Pessoa;
- Coletivo;
- Organização;
- Handoffs;
- Cenários;
- Catálogo de Telas;
- Lacunas.

A Arquitetura da Experiência também contém a sequência UXA-070 a UXA-073.

### 6.2 UXA-072-F02 — Registro do Estado Atual contraditório

**Estado:** encerrado na base auditada.

O GKR-STATE-001 versão 2.00.0 reconhece:

- UXA-070 concluída;
- UXA-071 integrada;
- UXA-072 não aprovada até reformulação;
- UXA-073 executada;
- UXA-074 como próxima validação ainda não iniciada na base auditada.

A integração da própria UXA-074 constituirá novo evento de estado e deverá ser sincronizada em pacote posterior.

### 6.3 UXA-072-F03 — Roadmap desatualizado

**Estado:** encerrado na base auditada.

O ROADMAP-12.47.0 registra a sequência correta e não trata UXA-071 como futura.

### 6.4 UXA-072-F04 — Índice UXA desatualizado

**Estado:** encerrado na base auditada.

A UXA-000 versão 0.67.0 reconhece a materialização, a primeira validação e a reformulação.

### 6.5 UXA-072-F05 — Estados de maturidade compostos

**Estado:** encerrado.

Foram encontrados os seguintes estados primários, todos pertencentes à taxonomia da UXA-070:

- `contratado`;
- `programado`;
- `materializado`;
- `validado`;
- `reformulação pendente`;
- `não iniciado`;
- `indeterminado`.

Autoridade, referência materializada, evidência de validação e continuidade integrada são registradas separadamente.

### 6.6 UXA-072-F06 — Validação de tela confundida com validação de jornada

**Estado:** encerrado.

A seção declara explicitamente:

```text
superfície validada
≠ transição de entrada validada
≠ transição de saída validada
≠ jornada integrada validada
```

As contagens de 17 referências pessoais, 22 referências de Coletivos e 46 referências do Opportunity Boost permanecem vinculadas aos escopos de origem e não são usadas como prova de completude integrada.

### 6.7 UXA-072-F07 — Handoffs assimétricos

**Estado:** encerrado com ressalva não bloqueadora.

A matriz registra:

- maturidade da origem;
- maturidade do destino;
- autoridade;
- evidência da transição;
- retorno ou contestação;
- lacuna aplicável.

A visão do responsável do Coletivo e a relação bilateral Organização–Coletivo permanecem explicitamente ausentes.

**Ressalva:** a matriz é uma síntese por handoff prioritário. Um registro futuro, nó a nó, ainda poderá detalhar dados transferidos, efeito, tempo e interrupção de cada transição sem invalidar a estrutura atual.

### 6.8 UXA-072-F08 — Cenários excedendo a evidência

**Estado:** encerrado.

Cada cenário registra:

- finalidade;
- participantes e perspectivas;
- nós materializados;
- nós apenas contratados;
- transições validadas;
- transições não validadas como conjunto;
- ponto de interrupção;
- conclusão permitida;
- conclusão proibida.

Nenhum cenário é declarado completo.

### 6.9 UXA-072-F09 — Catálogo sem continuidade integrada

**Estado:** encerrado com ressalva não bloqueadora.

O catálogo diferencia:

- superfícies materializadas;
- superfícies validadas;
- entrada integrada;
- saída integrada;
- perspectiva coberta;
- lacuna associada.

**Ressalva:** o inventário atual permanece agregado por família. O cadastro individual de cada tela, estado e transição continua sendo uma evolução documental possível, não uma condição para a validade da seção atual.

### 6.10 UXA-072-F10 — Status documental inconsistente

**Estado:** encerrado.

A regra está explícita:

- mapas reformulados permanecem `draft` até validação aprovada e promoção governada;
- o registro de lacunas permanece `active` por ser observacional;
- navegação não promove maturidade;
- status somente muda por pacote autorizado.

## 7. Validação por artefato

### 7.1 `docs/journeys/index.md`

**Resultado:** aprovado.

A visão geral define finalidade, modelo de evidência, estado da seção, regra de leitura e regra de promoção.

Ela não se apresenta como fonte canônica e não confunde navegabilidade com validação.

### 7.2 `docs/journeys/person.md`

**Resultado:** aprovado.

A jornada pessoal diferencia validações locais e continuidade integrada.

A transição para Tela Hoje permanece `não examinada` como conjunto, e a jornada em Coletivos é interrompida explicitamente após `Solicitação Pendente`.

### 7.3 `docs/journeys/collective.md`

**Resultado:** aprovado.

A vista distingue presença pública, operação do responsável e handoffs críticos.

Estados apresentados à Pessoa não são tratados como materialização da operação interna do Coletivo.

### 7.4 `docs/journeys/organization.md`

**Resultado:** aprovado.

A vista diferencia fundação, visão geral, oportunidades, relação bilateral, Opportunity Boost e resultados institucionais.

A relação Organização–Coletivo permanece contratada e não materializada.

### 7.5 `docs/journeys/handoffs.md`

**Resultado:** aprovado com ressalva.

A falsa simetria foi removida e as lacunas bilaterais estão visíveis.

O detalhamento exaustivo de todos os campos de transição poderá ser desenvolvido futuramente sem reabrir a remediação atual.

### 7.6 `docs/journeys/scenarios.md`

**Resultado:** aprovado.

Os seis cenários são hipóteses documentais limitadas pela evidência e possuem conclusões permitidas e proibidas.

### 7.7 `docs/journeys/screen-catalog.md`

**Resultado:** aprovado com ressalva.

O catálogo cumpre a função de inventário agregado e diferencia superfícies de transições.

A expansão para registros individuais permanece futura.

### 7.8 `docs/journeys/gaps.md`

**Resultado:** aprovado.

O documento é observacional, possui gates de fechamento e não promove maturidade por inclusão ou proximidade.

## 8. Escopo exato da aprovação

A UXA-074 aprova:

- a seção `Jornadas Integradas` como área documental navegável;
- o modelo separado de evidência;
- a exposição das perspectivas de Pessoa, Coletivo e Organização;
- a representação controlada de continuidades parciais, ausentes e não examinadas;
- a matriz resumida de handoffs;
- os cenários como hipóteses documentais governadas;
- o catálogo agregado de superfícies e transições;
- o registro observacional de lacunas.

A UXA-074 não aprova como completos:

- a jornada pessoal ponta a ponta;
- a continuidade entre compreensão inicial e Tela Hoje;
- a jornada bilateral de participação em Coletivos;
- a operação do responsável pelo Coletivo;
- `Meus Coletivos`;
- Central de Atualizações;
- Início do Participante reformulado;
- Visão Geral do Responsável;
- a relação bilateral Organização–Coletivo;
- a matriz institucional completa;
- os 10 estados residuais do Opportunity Boost;
- efeitos externos de oportunidades;
- uma aplicação ou motor de simulação.

## 9. Ressalvas controladas

### UXA-074-R01 — Matriz de handoffs resumida

**Severidade:** não bloqueadora.

A matriz atende ao requisito de assimetria e autoridade, mas ainda não é um registro individual exaustivo de todas as transições.

### UXA-074-R02 — Catálogo agregado por família

**Severidade:** não bloqueadora.

O catálogo atende à separação entre superfícies e transições, porém ainda não contém uma linha individual para cada tela ou estado.

### UXA-074-R03 — Promoção de status não executada

**Severidade:** governança posterior.

Os mapas permanecem `draft` porque esta validação não possui autorização para promovê-los automaticamente.

### UXA-074-R04 — Sincronização pós-validação pendente

**Severidade:** governança posterior.

GKR-STATE-001, roadmap, UXA-000 e navegação descrevem corretamente a base anterior à integração da UXA-074. Após a integração deste parecer, deverão ser sincronizados para registrar o novo estado.

### UXA-074-R05 — Lacunas de produto preservadas

**Severidade:** não bloqueadora para a seção documental.

As lacunas impedem declarar jornadas completas, mas não impedem a seção de funcionar como instrumento de leitura e governança.

## 10. Critérios de aceitação

A validação é considerada aprovada com ressalvas porque:

- [x] a seção está presente e ordenada na navegação;
- [x] os registros centrais são coerentes na base auditada;
- [x] a taxonomia da UXA-070 é respeitada;
- [x] maturidade, autoridade, materialização e validação estão separadas;
- [x] continuidade integrada possui estado explícito;
- [x] assimetrias de handoff são visíveis;
- [x] cenários possuem limites de evidência;
- [x] catálogo diferencia superfície de transição;
- [x] mapas permaneceram `draft` durante a validação;
- [x] lacunas permanecem observacionais;
- [x] nenhum contrato, SVG ou wireframe canônico foi alterado;
- [x] nenhum protótipo, aplicação, teste com pessoas ou Engenharia de Produto foi iniciado.

## 11. Preservações

Permanecem vigentes:

- superfície validada não equivale a jornada integrada validada;
- contrato bilateral não equivale a interface bilateral;
- retorno visível para a Pessoa não comprova operação do responsável;
- ausência de materialização permanece ausência;
- cenário documental não executa lógica de negócio;
- inclusão na navegação não altera canonicidade;
- publicidade não compra autoridade, legitimidade ou reputação;
- mapa documental não cria transição inexistente;
- uma lacuna somente fecha por pacote governado;
- nenhuma etapa inicia automaticamente a seguinte.

## 12. Resultado controlado

> **A seção Jornadas Integradas está funcionalmente aprovada, com ressalvas, como instrumento documental de leitura, rastreabilidade e governança.**

Este resultado não declara as jornadas completas e não altera automaticamente o status dos mapas.

## 13. Próxima transição recomendada

A próxima transição recomendada é:

**UXA-075 — Promoção Controlada e Sincronização Pós-Validação das Jornadas Integradas**, mediante autorização separada.

Esse pacote futuro deverá decidir explicitamente:

1. quais artefatos podem ser promovidos de `draft` para `active`;
2. quais permanecem `draft` por representarem jornadas incompletas;
3. como registrar o resultado da UXA-074 no GKR-STATE-001;
4. como atualizar o roadmap e a UXA-000;
5. como incluir a UXA-074 na navegação da Arquitetura da Experiência;
6. quais ressalvas permanecem abertas;
7. qual próxima evolução documental poderá ser considerada.

A UXA-075 não está iniciada.
