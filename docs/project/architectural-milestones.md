---
id: GKR-ARCHITECTURAL-MILESTONES-001
title: Marcos Arquiteturais
status: active
version: 4.99.0
owner: Guivos
last_updated: 2026-07-26
depends_on:
  - GKR-STATE-001
related:
  - ROADMAP-12.1.0
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
  - M7.20
  - M7.21
  - M7.22
  - M7.23
  - M7.24
  - M7.25
  - M7.26
  - M7.27
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
| M7.27 | Concluído neste incremento | primeiro estado alternativo do Mapa criado para localização desativada |

## 3. Marco vigente

### Estado do Mapa sem Localização Criado — M7.27

Critérios atendidos:

- localização do dispositivo preservada como opcional;
- exploração territorial mantida por cidade ou região manual;
- linguagem de exploração geral utilizada sem gate de personalização;
- busca, filtros, Mapa e Lista preservados;
- marcador de posição pessoal removido;
- resultados relacionados à região e à busca explícita;
- distância pessoal omitida sem origem válida;
- ativação de localização aproximada apresentada como ação secundária;
- revisão de privacidade disponível antes da ativação;
- origem manual permitida para rota quando aplicável;
- recusa de localização sem bloqueio de Detalhe ou salvamento;
- arquivo vetorial móvel criado em 390 por 844 pixels;
- validação funcional especializada preservada como ato posterior;
- tecnologia, design, protótipo, testes e desenvolvimento não iniciados;
- Resultados Empresariais preservados em 18 decisões e zero Resultados canônicos;
- Engenharia de Produto preservada antes de W0-01.

## 4. Marcos anteriores preservados

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
| Arquitetura da Experiência | ativa; primeiro estado alternativo do Mapa materializado; validações e estados posteriores aguardando autorização |
| Arquitetura de Produtos | planejada; não iniciada |
| Revisão entre Arquiteturas | planejada |

A Arquitetura da Experiência permanece preparatória e não inicia formalmente a Revisão da Arquitetura de Produtos.

## 6. Próximos atos possíveis

Após integração e nova autorização, poderão ocorrer em incrementos separados:

### Arquitetura da Experiência

1. validar funcionalmente o estado de localização desativada;
2. criar o estado alternativo em Lista;
3. criar o estado sem resultados;
4. criar referência do Mapa para computador;
5. criar o wireframe do início protegido;
6. criar a referência móvel da Home;
7. validar a revisão da compreensão inicial;
8. validar a transição para a primeira Tela Hoje.

### Arquitetura de Negócios

1. reaplicar os quatro testes;
2. ajustar o AQS-O01;
3. consolidar catálogos canônicos;
4. criar matriz de sustentação entre Resultados;
5. preparar Capacidades Empresariais.

Nenhum ato é iniciado automaticamente.

## 7. Regra de transição

Wireframe não equivale a validação funcional, design ou implementação. Validação funcional não equivale a teste de usabilidade. Fusão de candidato não equivale a aprovação. Cada transição exige evidência registrada e autorização própria.
