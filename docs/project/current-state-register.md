---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 1.58.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-07-27
depends_on:
  - GKR-AUD-002
  - GKR-REMEDIATION-002
related:
  - GEA-000
  - PAS-001
  - UXA-000
  - UXA-004
  - UXA-010
  - UXA-011-A1
  - UXA-012
  - UXA-013
  - UXA-014
  - UXA-017
  - UXA-018
  - UXA-019
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - UXA-029
  - UXA-030
  - GEM-CLOSURE-REVIEW-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - ROADMAP-12.5.0
  - M7.31
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro é a superfície oficial do estado global vigente do Repositório de Conhecimento da Guivos quando o incremento correspondente estiver integrado ao ramo principal.

## 2. Estado global vigente

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era de conhecimento | fase de estruturação do conhecimento da Guivos | GE-2 — Knowledge |
| Marco atual | estado móvel do Mapa sem resultados criado | M7.31; UXA-030 |
| Remediação | concluída; validação mecânica permanente ativa | R1–R6 |
| Achados conhecidos | nenhum crítico, maior ou menor aberto | 0 |
| Arquitetura de Negócios | ativa; 18 decisões humanas concluídas | BA-STR-002; COD-018 |
| Resultados Empresariais | 9 em validação, 3 fundidos, 6 rejeitados e zero canônicos | BA-STR-002-COR-001; BA-STR-002-CODR-001 |
| Arquitetura da Experiência | ativa até o estado sem resultados do Mapa | UXA-000 a UXA-030 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Referência móvel da Home | não iniciada | — |
| Início protegido | funcionalmente validado e reformulado; wireframe pendente | UXA-020; UXA-023 |
| Compreensão inicial | contrato estabelecido; validação especializada pendente | UXA-011-A1; UXA-020; UXA-023 |
| Gate de personalização | bloqueado antes de compreensão revisável e autorizada | UXA-011-A1; UXA-020; UXA-023 |
| Tela Hoje | validada e reposicionada como entrada recorrente | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estado sem localização | funcionalmente validado e reformulado | UXA-026; UXA-027 |
| Visualização em Lista do Mapa | funcionalmente validada e reformulada | UXA-028; UXA-029 |
| Estado sem resultados | wireframe móvel criado; validação especializada não iniciada | UXA-030 |
| Demais estados do Mapa | governados; wireframes não iniciados | UXA-025 |
| Referência do Mapa para computador | não iniciada | — |
| Detalhe de Oportunidade | validado e reformulado | UXA-007; UXA-012 |
| Cadastro pela Organização | validado e reformulado | UXA-008; UXA-013 |
| Organizações e Coletivos | fundação, superfícies e relações estabelecidas | UXA-014 a UXA-019 |
| Protótipo, design e testes | não iniciados | — |
| Guivos Journey | especificação ativa; nove capacidades concluídas | PAS-001 1.0.0 |
| Modelo Econômico | arquitetura documental inicial concluída; validações reais pendentes | GEM-001 a GEM-010 |
| Engenharia de Produto | pausada antes de W0-01; execução em 0% | W0-01 |
| Validação de Mercado | trilha paralela preservada; execução pendente | — |

## 3. Estado dos Resultados Empresariais

```text
Human decisions: 18 of 18 — completed
Under Validation: 9
Merged: 3
Rejected: 6
Approved Outcomes: 0
Canonical EO/BO codes: 0
Reapplication of the four tests: not started
AQS-O01: not started
Business Capabilities: not started
```

A fusão de BUS-CAND-010 em BUS-CAND-005 não aprova o candidato de destino, não cria Resultado canônico e não torna reinvestimento obrigatório.

## 4. Sequência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje, jornada sem personalização ou exploração geral
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não entra entre a Home e a Tela Hoje.

## 5. Mapa e estados validados

O Mapa principal permanece uma superfície recorrente com contexto de atuação, pesquisa, filtros, resultados, legenda, privacidade, cartão selecionado e rota contextual.

O estado sem localização preserva posição não acessada, região manual, ausência de marcador pessoal, salvamento e origem específica.

A visualização em Lista, reformulada pela UXA-029, demonstra:

- `LISTA TERRITORIAL DO MAPA · MESMA CONSULTA`;
- `Agindo como: Pessoa`;
- região, busca e filtros preservados;
- total consolidado de filtros;
- quantidade e atualização dos resultados;
- ordenação explícita e explicável;
- cartões comparáveis com incertezas declaradas;
- seleção preservada do Mapa;
- explicação funcional e relação comercial separadas;
- salvamento, origem e Detalhe sem localização;
- retorno ao Mapa sem perda de contexto;
- funcionamento integral sem mapa carregado.

## 6. Estado sem resultados

A UXA-030 materializa a ausência legítima de correspondências para uma consulta concluída.

O estado demonstra:

- região, busca e filtros preservados;
- total consolidado de filtros;
- `0 resultados correspondem a esta consulta`;
- `Consulta concluída · nenhuma falha conhecida`;
- mensagem limitada à consulta atual;
- ampliação de região, alteração de período, revisão de filtros e edição de busca como ações explícitas;
- reversão da última alteração quando aplicável;
- distinção entre ausência, falha de fonte e indisponibilidade temporária;
- equivalência entre Mapa e Lista;
- localização opcional e região manual;
- tratamento textual sem dependência do mapa carregado.

Arquivos vetoriais:

- `docs/assets/wireframes/uxa-024-opportunity-map-mobile.svg`;
- `docs/assets/wireframes/uxa-026-opportunity-map-location-disabled-mobile.svg`;
- `docs/assets/wireframes/uxa-028-opportunity-map-list-mobile.svg`;
- `docs/assets/wireframes/uxa-030-opportunity-map-no-results-mobile.svg`.

O estado sem resultados ainda não foi funcionalmente validado. Wireframe não equivale a teste com usuários, design ou implementação.

## 7. Proteções vigentes

- localização permanece opcional;
- região manual não equivale a posição atual;
- alternar Mapa e Lista não modifica permissões;
- dado ausente não é completado por inferência;
- ordenação funcional e patrocínio permanecem separados;
- salvamento não autoriza rastreamento;
- definir origem não autoriza histórico territorial;
- endereços protegidos não são contornados;
- personalização exige gate próprio;
- zero legítimo não é confundido com falha de fonte;
- filtros e região não são alterados silenciosamente;
- publicidade não preenche artificialmente o estado vazio.

## 8. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente o estado sem resultados;
2. criar referência do Mapa para computador;
3. criar o wireframe gráfico do início protegido;
4. criar a referência móvel da Home;
5. validar a revisão da compreensão inicial;
6. validar a transição para a primeira Tela Hoje;
7. retomar independentemente a reaplicação dos quatro testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
