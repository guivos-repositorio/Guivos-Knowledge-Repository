---
id: GKR-KNOWLEDGE-BOARD-001
title: Painel de Conhecimento
status: active
version: 12.3.0
owner: Guivos
last_updated: 2026-07-27
depends_on:
  - GKR-STATE-001
related:
  - ROADMAP-12.3.0
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - UXA-000
  - UXA-004
  - UXA-011-A1
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - UXA-028
  - M7.29
normative: false
---

# Painel de Conhecimento

## 1. Autoridade

Este painel resume o portfólio arquitetural vigente. O estado oficial é declarado pelo Registro do Estado Atual.

## 2. Estado institucional vigente

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | visualização em Lista do Mapa materializada em wireframe móvel | M7.29; UXA-028 |
| Remediação | concluída | R1–R6 |
| Resultados Empresariais | 18 de 18 decisões; nenhum Resultado canônico | BA-STR-002-CODR-001 |
| Candidatos | 9 em validação, 3 fundidos e 6 rejeitados | BA-STR-002-COR-001 |
| Continuidade econômica sustentável | formulação combinada em validação | BUS-CAND-005; COD-018 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Início protegido da jornada | funcionalmente validado e reformulado | UXA-020; UXA-023 |
| Wireframe do início protegido | não iniciado | — |
| Referência móvel da Home | não iniciada | — |
| Tela Hoje | entrada recorrente após compreensão confirmada | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estado de localização desativada | funcionalmente validado e reformulado | UXA-026; UXA-027 |
| Visualização em Lista do Mapa | wireframe móvel criado; validação especializada pendente | UXA-028 |
| Demais estados alternativos | governados; wireframes não iniciados | UXA-025 |
| Personalização | bloqueada antes de contexto suficiente, revisável e autorizado | UXA-011-A1; UXA-020; UXA-023 |
| Protótipo, design e testes | não iniciados | — |
| Capacidades Empresariais | não iniciadas | — |
| Engenharia de Produto | pausada | W0-01 |

## 3. Portfólio por situação

### Concluído ou consolidado

- Arquitetura de Fundação congelada;
- Guivos Journey funcionalmente concluído;
- Modelo Econômico documentado inicialmente;
- remediação e validação mecânica concluídas;
- validação externa dos 18 candidatos concluída;
- decisões humanas 1 a 18 registradas;
- BUS-CAND-010 fundido em BUS-CAND-005;
- Tela Hoje, Detalhe de Oportunidade e Cadastro pela Organização validados;
- Fundação de Organizações e Coletivos estabelecida;
- Visão Geral da Organização e Início do Coletivo validados;
- relações entre Organizações e Coletivos detalhadas;
- Página Inicial pública validada e reformulada;
- wireframe gráfico da Home para computador criado;
- início protegido da jornada validado e reformulado;
- posição do Mapa na navegação recorrente consolidada;
- wireframe gráfico móvel do Mapa criado;
- Mapa de Oportunidades funcionalmente validado e reformulado;
- estado sem localização criado, validado e reformulado;
- visualização em Lista do Mapa criada.

### Em validação

- nove formulações candidatas de Resultados Empresariais;
- formulações combinadas de agência, habilitação de valor e continuidade econômica;
- fronteiras entre Resultados, princípios, capacidades e propriedades sustentadoras.

### Aguardando autorização

#### Arquitetura da Experiência

- validação funcional da visualização em Lista;
- estado sem resultados;
- referência do Mapa para computador;
- wireframe gráfico do início protegido da jornada;
- referência móvel da Página Inicial pública;
- detalhamento de estados especializados de texto, voz e arquivos;
- validação da revisão da compreensão inicial;
- validação da transição para a primeira Tela Hoje.

#### Arquitetura de Negócios

- reaplicação dos quatro testes às formulações revisadas e combinadas;
- ajuste prático do AQS-O01;
- consolidação dos catálogos canônicos;
- matriz de sustentação entre Resultados;
- preparação da Arquitetura de Capacidades Empresariais.

### Pausado ou não iniciado

- Engenharia de Produto;
- protótipo navegável e design visual;
- testes de usabilidade;
- provas de conceito, ambientes, integrações e produção.

## 4. Sequência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## 5. Estado de localização desativada validado

A UXA-026 e a UXA-027 demonstram:

- exploração geral sem personalização;
- localização do dispositivo desativada;
- confirmação `Posição não acessada`;
- região escolhida manualmente e distinta da posição pessoal;
- pesquisa e filtros preservados;
- Mapa e Lista sincronizados;
- área territorial sem marcador ou posição presumida;
- resultados explicados pela região e pela busca;
- distância pessoal omitida sem origem válida;
- ativação opcional de localização aproximada;
- salvamento sem localização;
- origem manual para rota;
- continuidade para o Detalhe.

## 6. Visualização em Lista do Mapa

A UXA-028 demonstra:

- Lista selecionada dentro da superfície Mapa;
- região, busca e filtros preservados;
- quantidade e ordenação explícitas;
- cartões comparáveis;
- oportunidade selecionada preservada;
- explicação de origem e relação comercial separadas;
- salvamento, definição de origem e Detalhe;
- retorno ao Mapa sem perda de contexto;
- uso integral sem localização;
- alternativa textual para acessibilidade, baixa conectividade e falha cartográfica.

A Lista não duplica `Explorar` e sua validação funcional especializada permanece pendente.

## 7. Proteções preservadas

- a Home pública não coleta relato pessoal;
- iniciar a jornada é voluntário;
- autenticação antecede persistência associada a uma pessoa;
- autorização genérica não libera todos os usos;
- informações não confirmadas não viram fatos;
- exploração sem personalização permanece disponível;
- publicidade não aumenta relevância pessoal;
- localização é opcional;
- recusa de localização não bloqueia exploração;
- região manual não equivale a posição atual;
- localização de participantes não aparece no Mapa;
- residências e locais sensíveis permanecem protegidos;
- rastreamento contínuo não é obrigatório;
- salvamento não autoriza rastreamento;
- origem manual não autoriza histórico territorial;
- alternância entre Mapa e Lista não altera permissões;
- proximidade não equivale a relevância;
- rota não contorna endereço protegido;
- wireframes e validações funcionais não equivalem a design ou implementação.

## 8. Distribuição dos candidatos

| Estado | Quantidade | Interpretação |
|---|---:|---|
| Em validação | 9 | formulações revisadas ou combinadas aguardando nova avaliação |
| Fundidos | 3 | conteúdos incorporados a candidatos-alvo com rastreabilidade |
| Rejeitados | 6 | retirados do catálogo futuro com destinos preservados |
| Aprovados | 0 | nenhuma aprovação ocorreu |

## 9. Próximo movimento

Após integração, nenhum movimento é automático. A próxima ação poderá ser escolhida entre validação funcional da Lista, estado sem resultados, referência do Mapa para computador, wireframe do início protegido, referência móvel da Home, validação da compreensão inicial ou retomada independente dos testes dos Resultados Empresariais.
