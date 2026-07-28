---
id: ROADMAP-12.10.0
title: Roadmap Arquitetural — Início Protegido Móvel Validado
status: active
version: 12.10.0
owner: Guivos
last_updated: 2026-07-27
supersedes_partial:
  - ROADMAP-12.9.0
related:
  - GKR-STATE-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - UXA-000
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
  - UXA-029
  - UXA-030
  - UXA-031
  - UXA-032
  - UXA-033
  - UXA-034
  - UXA-035
  - M7.36
---

# Roadmap Arquitetural — Início Protegido Móvel Validado

## 1. Autoridade

Este documento governa a sequência global de evolução arquitetural do Repositório de Conhecimento da Guivos. O estado transversal vigente é declarado pelo Registro do Estado Atual.

## 2. Estado atual

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era | fase de conhecimento | GE-2 — Knowledge |
| Marco | wireframe móvel do início protegido funcionalmente validado e reformulado | M7.36; UXA-034; UXA-035 |
| Remediação | concluída | R1–R6 |
| Resultados Empresariais | 18 de 18 decisões; nenhum Resultado canônico | BA-STR-002-CODR-001 |
| Candidatos | 9 em validação, 3 fundidos e 6 rejeitados | BA-STR-002-COR-001 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Início protegido móvel | funcionalmente validado e reformulado em quatro estados | UXA-023; UXA-034; UXA-035 |
| Referência móvel da Home | não iniciada | — |
| Compreensão inicial | contrato estabelecido; materialização pendente | UXA-011-A1; UXA-023; UXA-035 |
| Tela Hoje | entrada recorrente posterior ao gate | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | estados móveis e referência desktop validados | UXA-024 a UXA-033 |
| Protótipo, design e testes | não iniciados | — |
| Engenharia de Produto | pausada antes de W0-01 | W0-01 |

## 3. Sequência executada

1. Guivos Journey concluído funcionalmente e publicado;
2. Modelo Econômico documentado inicialmente;
3. validação externa e Matriz de Avaliação concluídas;
4. decisões humanas 1 a 18 registradas;
5. remediação do repositório concluída;
6. Arquitetura da Experiência integrada;
7. Tela Hoje, Detalhe e Cadastro validados;
8. experiências de Organizações e Coletivos estruturadas e validadas;
9. Home pública, início protegido e Tela Hoje separados;
10. Home pública validada e materializada para computador;
11. Mapa principal, estados móveis e referência desktop criados e validados;
12. wireframe móvel do início protegido criado;
13. wireframe móvel do início protegido funcionalmente validado e reformulado.

## 4. Sequência pessoal vigente

```text
Página Inicial pública
→ decisão voluntária de iniciar ou explorar
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ compreensão inicial revisável
→ decisão sobre persistência e personalização
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## 5. Resultado da validação do início protegido

A UXA-034 reformulada e a UXA-035 estabelecem:

- relato pessoal separado de dados técnicos e de acesso;
- estados nomeados, pausáveis e retomáveis;
- ausência de formulário linear obrigatório;
- acesso apresentado somente quando necessário;
- sessão válida sem repetição da etapa de acesso;
- ações com destino e efeito explícitos;
- texto, voz, arquivo e perguntas opcionais sem preferência automática;
- explicação anterior para voz e arquivo;
- compartilhamento mínimo legítimo;
- pausa, salvar, sair e excluir com efeitos distintos;
- inventário antes do processamento;
- autorizações específicas e inicialmente desmarcadas;
- preparação apenas de compreensão inicial temporária e revisável;
- recusa sem processamento;
- persistência e personalização bloqueadas até a revisão da compreensão.

## 6. Proteções preservadas

- nenhum relato é solicitado antes da explicação;
- dados de acesso não constituem conteúdo da jornada;
- autenticação não autoriza processamento;
- modalidades não competem como exigências;
- compartilhar pouco é legítimo;
- voz e arquivos exigem explicação anterior;
- revisão antecede autorização;
- não autorizar impede processamento;
- persistência e personalização dependem do gate;
- exploração sem personalização permanece disponível;
- informações de terceiros não são exigidas;
- wireframe, validação, protótipo, design, testes e desenvolvimento permanecem atos separados.

## 7. Estado dos Resultados Empresariais

```text
External validation: completed
Initial four-test evaluation: completed
Human decisions: completed — 18 of 18
Under Validation: 9
Merged: 3
Rejected: 6
Approved Outcomes: 0
Canonical codes: 0
Reapplication of the four tests: not started
AQS-O01: not started
Canonical consolidation: not started
```

A fusão de BUS-CAND-010 em BUS-CAND-005 não aprova o candidato-alvo e não torna reinvestimento obrigatório.

## 8. Próximas etapas candidatas

### 8.1 Arquitetura da Experiência

Após integração e nova autorização, poderá ocorrer separadamente:

1. criar a referência móvel da Home;
2. materializar a revisão da compreensão inicial;
3. validar a transição para a primeira Tela Hoje;
4. criar estados especializados de texto, voz e arquivos;
5. criar a referência do início protegido para computador;
6. criar estados de processamento, pausa, falha e retomada;
7. criar referência para tablet, caso priorizada.

### 8.2 Arquitetura de Negócios

Permanece pendente, em ato independente:

```text
reaplicação dos quatro testes
→ ajuste prático do AQS-O01
→ decisão sobre catálogos canônicos
→ matriz de sustentação entre Resultados
→ preparação da Arquitetura de Capacidades Empresariais
```

Nenhuma frente avança automaticamente.

## 9. Regras transversais preservadas

- nenhum candidato é aprovado por fusão ou reformulação;
- Resultados canônicos continuam em zero;
- reinvestimento não é obrigação automática;
- personalização exige compreensão revisável e autorizada;
- exploração geral continua disponível;
- localização não é condição universal de uso;
- publicidade não aumenta relevância pessoal;
- Validação de Mercado mantém execução própria e paralela.
