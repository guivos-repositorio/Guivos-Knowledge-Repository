---
id: GKR-ARCHITECTURAL-MILESTONES-001
title: Marcos Arquiteturais
status: active
version: 5.6.0
owner: Guivos
last_updated: 2026-07-27
depends_on:
  - GKR-STATE-001
related:
  - ROADMAP-12.8.0
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
  - UXA-028
  - UXA-029
  - UXA-030
  - UXA-031
  - UXA-032
  - UXA-033
  - M7.20
  - M7.21
  - M7.22
  - M7.23
  - M7.24
  - M7.25
  - M7.26
  - M7.27
  - M7.28
  - M7.29
  - M7.30
  - M7.31
  - M7.32
  - M7.33
  - M7.34
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
| M7.23 | Concluído | wireframe da Home para computador criado |
| M7.24 | Concluído | início protegido validado e reformulado |
| M7.25 | Concluído | wireframe móvel do Mapa criado |
| M7.26 | Concluído | Mapa funcionalmente validado e reformulado |
| M7.27 | Concluído | estado sem localização criado |
| M7.28 | Concluído | estado sem localização validado e reformulado |
| M7.29 | Concluído | visualização em Lista criada |
| M7.30 | Concluído | visualização em Lista validada e reformulada |
| M7.31 | Concluído | estado sem resultados criado |
| M7.32 | Concluído | estado sem resultados validado e reformulado |
| M7.33 | Concluído | referência do Mapa para computador criada |
| M7.34 | Concluído neste incremento | referência do Mapa para computador funcionalmente validada e reformulada |

## 3. Marco vigente

### Referência do Mapa para Computador Funcionalmente Validada e Reformulada — M7.34

Critérios atendidos:

- validação registrada em UXA-033;
- UXA-032 elevada para 0.2.0 e estado ativo;
- faixa compartilhada da consulta territorial;
- filtros resumidos e detalhados semanticamente consistentes;
- visão dividida declarada como padrão;
- foco no Mapa ou na Lista com contexto preservado;
- retorno à visão dividida;
- movimento do Mapa sem atualização silenciosa;
- `Pesquisar nesta área` condicionado a movimento pendente;
- seleção `Marcador 1` vinculada no Mapa, cartão e painel;
- cartões secundários comparáveis e explicáveis;
- relação comercial explicitamente rotulada;
- painel contextual recolhível;
- recuperação do total zero concentrada no painel de consulta;
- seleção anterior explicável sem alterar o total zero;
- localização opcional e região manual preservadas;
- Lista integral sem mapa carregado;
- responsividade, tablet, tecnologia, design, protótipo, testes e desenvolvimento não iniciados;
- Resultados Empresariais preservados em 18 decisões e zero Resultados canônicos;
- Engenharia de Produto preservada antes de W0-01.

## 4. Marcos anteriores preservados

### Referência do Mapa para Computador Criada — M7.33

A UXA-032 permanece como a materialização dos dois estados em 1.440 por 1.024 pixels.

### Estado sem Resultados Validado — M7.32

A UXA-030 e a UXA-031 permanecem como contrato do zero legítimo, cobertura verificável e recuperação consciente.

### Lista do Mapa Validada — M7.30

A UXA-028 e a UXA-029 permanecem como contrato da representação textual integral da consulta territorial.

### Estado sem Localização Validado — M7.28

A UXA-026 e a UXA-027 permanecem como contrato do uso sem localização.

### Mapa de Oportunidades Validado — M7.26

O Mapa principal permanece funcionalmente validado, com filtros, resultados, privacidade e rota contextual.

### Início Protegido Validado — M7.24

O início protegido permanece funcionalmente validado, com coleta consciente, revisão e personalização bloqueada antes do gate.

### Página Inicial Pública Validada — M7.22

A Home explica concretamente a Guivos, oferece exploração sem personalização e não coleta relato pessoal.

### Décima Oitava Decisão Humana — M7.20

COD-018 permanece integrado, sem Resultado aprovado ou canonicalizado.

## 5. Estado das revisões arquiteturais

| Revisão | Estado em linguagem clara |
|---|---|
| Arquitetura de Fundação | concluída e congelada |
| Modelo Fundamental | pronto e pausado operacionalmente |
| Arquitetura de Negócios | ativa; decisões humanas concluídas e reaplicação aguardando autorização |
| Arquitetura da Experiência | ativa; referência desktop do Mapa validada e reformulada |
| Arquitetura de Produtos | planejada; não iniciada |
| Revisão entre Arquiteturas | planejada |

A Arquitetura da Experiência permanece preparatória e não inicia formalmente a Revisão da Arquitetura de Produtos.

## 6. Próximos atos possíveis

Após integração e nova autorização, poderão ocorrer em incrementos separados:

### Arquitetura da Experiência

1. criar o wireframe do início protegido;
2. criar a referência móvel da Home;
3. validar a revisão da compreensão inicial;
4. validar a transição para a primeira Tela Hoje;
5. criar outros estados alternativos do Mapa;
6. criar referência específica para tablet, caso priorizada.

### Arquitetura de Negócios

1. reaplicar os quatro testes;
2. ajustar o AQS-O01;
3. consolidar catálogos canônicos;
4. criar matriz de sustentação entre Resultados;
5. preparar Capacidades Empresariais.

Nenhum ato é iniciado automaticamente.

## 7. Regra de transição

Wireframe não equivale a validação funcional, design ou implementação. Validação funcional não equivale a teste de usabilidade. Fusão de candidato não equivale a aprovação. Cada transição exige evidência registrada e autorização própria.
