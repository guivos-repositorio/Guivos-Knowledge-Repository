---
id: GKR-ARCHITECTURAL-MILESTONES-001
title: Marcos Arquiteturais
status: active
version: 5.0.0
owner: Guivos
last_updated: 2026-07-27
depends_on:
  - GKR-STATE-001
related:
  - ROADMAP-12.2.0
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - UXA-000
  - UXA-004
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-024
  - UXA-025
  - UXA-026
  - UXA-027
  - M7.20
  - M7.21
  - M7.22
  - M7.23
  - M7.24
  - M7.25
  - M7.26
  - M7.27
  - M7.28
normative: false
---

# Marcos Arquiteturais

## 1. Autoridade

Este registro apresenta os marcos arquiteturais vigentes em visão consolidada.

## 2. Linha de maturidade consolidada

| Faixa ou marco | Estado | Resultado principal |
|---|---|---|
| A0–A1 | Concluído | fundação do Repositório e macroestrutura institucional |
| M3–M4 | Concluído | Arquitetura de Fundação congelada e Arquitetura do Conhecimento estabelecida |
| M5–M5.18 | Concluído | arquitetura funcional e publicação do Guivos Journey |
| M6.0–M6.10 | Concluído | desenvolvimento e fechamento documental do Modelo Econômico |
| M7.0–M7.20 | Concluído | validação externa, Matriz de Avaliação e 18 decisões humanas |
| M7.3–M7.3.5 | Concluído | auditoria, remediação e retomada governada |
| M7.19.1–M7.19.11 | Concluído | Arquitetura da Experiência e experiências institucionais e coletivas |
| M7.21 | Concluído | Home pública, início protegido e Tela Hoje separados |
| M7.22 | Concluído | Home pública validada e reformulada |
| M7.23 | Concluído | wireframe gráfico da Home para computador criado |
| M7.24 | Concluído | início protegido da jornada validado e reformulado |
| M7.25 | Concluído | wireframe móvel do Mapa de Oportunidades criado |
| M7.26 | Concluído | Mapa de Oportunidades funcionalmente validado e reformulado |
| M7.27 | Concluído | primeiro estado alternativo do Mapa criado para localização desativada |
| M7.28 | Concluído neste incremento | estado sem localização funcionalmente validado e reformulado |

## 3. Marco vigente

### Estado do Mapa sem Localização Validado e Reformulado — M7.28

Critérios atendidos:

- Mapa preservado como superfície recorrente;
- localização do dispositivo mantida como opcional;
- exploração territorial mantida por cidade ou região manual;
- declaração `Posição não acessada` adicionada;
- região manual diferenciada explicitamente da posição pessoal;
- linguagem de exploração geral utilizada sem gate de personalização;
- busca, filtros, Mapa e Lista preservados;
- marcador e posição pessoal presumida removidos;
- resultados relacionados à região e à busca explícita;
- distância pessoal omitida sem origem válida;
- salvamento demonstrado sem ativação de localização;
- origem manual demonstrada para rota;
- ativação de localização aproximada apresentada como ação secundária e opcional;
- revisão de privacidade disponível antes da ativação;
- recusa de localização sem bloqueio de Detalhe ou salvamento;
- arquivo vetorial móvel reformulado em 390 por 844 pixels;
- demais estados gráficos e referência para computador preservados como atos separados;
- tecnologia, design, protótipo, testes e desenvolvimento não iniciados;
- Resultados Empresariais preservados em 18 decisões e zero Resultados canônicos;
- Engenharia de Produto preservada antes de W0-01.

## 4. Marcos anteriores preservados

### Estado do Mapa sem Localização Criado — M7.27

A UXA-026 permanece como origem histórica do estado, posteriormente reformulado e validado pela UXA-027.

### Mapa de Oportunidades Validado e Reformulado — M7.26

O Mapa principal permanece funcionalmente validado, com Mapa e Lista sincronizados, filtros, resultados, privacidade e rota contextual.

### Wireframe Móvel do Mapa Criado — M7.25

A primeira referência gráfica móvel permanece como base histórica da reformulação registrada em UXA-024 e UXA-025.

### Início Protegido da Jornada Validado — M7.24

O início protegido permanece funcionalmente validado, com coleta consciente, revisão, estados verificáveis e personalização bloqueada antes do gate.

### Wireframe Gráfico da Home Criado — M7.23

A Home pública permanece validada e materializada em referência vetorial para computador, sem representar responsividade, design ou implementação.

### Página Inicial Pública Validada — M7.22

A Home explica concretamente a Guivos, oferece exploração sem personalização, distingue caminhos e não coleta relato pessoal.

### Página Inicial e Início da Jornada Estabelecidos — M7.21

A primeira entrada permanece separada entre Home pública, ambiente protegido e Tela Hoje.

### Décima Oitava Decisão Humana — M7.20

COD-018 permanece integrado, com BUS-CAND-010 fundido em BUS-CAND-005 e nenhum Resultado aprovado ou canonicalizado.

## 5. Estado das revisões arquiteturais

| Revisão | Estado em linguagem clara |
|---|---|
| Arquitetura de Fundação | concluída e congelada |
| Modelo Fundamental | pronto e pausado operacionalmente |
| Arquitetura de Negócios | ativa; decisões humanas concluídas e reaplicação aguardando autorização |
| Arquitetura da Experiência | ativa; estado sem localização validado; estados e transições posteriores aguardando autorização |
| Arquitetura de Produtos | planejada; não iniciada |
| Revisão entre Arquiteturas | planejada |

A Arquitetura da Experiência permanece preparatória e não inicia formalmente a Revisão da Arquitetura de Produtos.

## 6. Próximos atos possíveis

Após integração e nova autorização, poderão ocorrer em incrementos separados:

### Arquitetura da Experiência

1. criar o estado alternativo em Lista;
2. criar o estado sem resultados;
3. criar referência do Mapa para computador;
4. criar o wireframe do início protegido;
5. criar a referência móvel da Home;
6. validar a revisão da compreensão inicial;
7. validar a transição para a primeira Tela Hoje.

### Arquitetura de Negócios

1. reaplicar os quatro testes;
2. ajustar o AQS-O01;
3. consolidar catálogos canônicos;
4. criar matriz de sustentação entre Resultados;
5. preparar Capacidades Empresariais.

Nenhum ato é iniciado automaticamente.

## 7. Regra de transição

Wireframe não equivale a validação funcional, design ou implementação. Validação funcional não equivale a teste de usabilidade. Fusão de candidato não equivale a aprovação. Cada transição exige evidência registrada e autorização própria.
