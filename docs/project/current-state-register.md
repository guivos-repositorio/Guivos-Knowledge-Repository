---
id: GKR-STATE-001
title: Registro do Estado Atual
status: active
version: 1.63.0
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
  - UXA-031
  - UXA-032
  - UXA-033
  - UXA-034
  - UXA-035
  - GEM-CLOSURE-REVIEW-001
  - BA-STR-002
  - BA-STR-002-COR-001
  - BA-STR-002-CODR-001
  - COD-018
  - ROADMAP-12.10.0
  - M7.36
normative: true
---

# Registro do Estado Atual

## 1. Autoridade

Este registro é a superfície oficial do estado global vigente do Repositório de Conhecimento da Guivos quando o incremento correspondente estiver integrado ao ramo principal.

## 2. Estado global vigente

| Elemento | Estado em linguagem clara | Referência técnica |
|---|---|---|
| Era de conhecimento | fase de estruturação do conhecimento da Guivos | GE-2 — Knowledge |
| Marco atual | wireframe móvel do início protegido funcionalmente validado e reformulado | M7.36; UXA-034; UXA-035 |
| Remediação | concluída; validação mecânica permanente ativa | R1–R6 |
| Achados conhecidos | nenhum crítico, maior ou menor aberto | 0 |
| Arquitetura de Negócios | ativa; 18 decisões humanas concluídas | BA-STR-002; COD-018 |
| Resultados Empresariais | 9 em validação, 3 fundidos, 6 rejeitados e zero canônicos | BA-STR-002-COR-001; BA-STR-002-CODR-001 |
| Arquitetura da Experiência | ativa até a validação do início protegido móvel | UXA-000 a UXA-035 |
| Página Inicial pública | validada e materializada para computador | UXA-020; UXA-021; UXA-022 |
| Referência móvel da Home | não iniciada | — |
| Início protegido móvel | funcionalmente validado e reformulado em quatro estados | UXA-020; UXA-023; UXA-034; UXA-035 |
| Referência do início protegido para computador | não iniciada | — |
| Compreensão inicial | contrato estabelecido; materialização e validação especializadas pendentes | UXA-011-A1; UXA-020; UXA-023; UXA-035 |
| Gate de persistência e personalização | bloqueado antes de compreensão apresentada, revisada e autorizada | UXA-011-A1; UXA-023; UXA-034; UXA-035 |
| Tela Hoje | validada e reposicionada como entrada recorrente | UXA-002; UXA-006; UXA-010 |
| Mapa de Oportunidades | funcionalmente validado e reformulado | UXA-004; UXA-024; UXA-025 |
| Estado sem localização | funcionalmente validado e reformulado | UXA-026; UXA-027 |
| Visualização em Lista do Mapa | funcionalmente validada e reformulada | UXA-028; UXA-029 |
| Estado sem resultados | funcionalmente validado e reformulado | UXA-030; UXA-031 |
| Referência do Mapa para computador | funcionalmente validada e reformulada | UXA-032; UXA-033 |
| Referência para tablet | não iniciada | — |
| Demais estados do Mapa | governados; wireframes não iniciados | UXA-025 |
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
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ compreensão inicial revisável
→ decisão sobre persistência e personalização
→ Tela Hoje, jornada sem personalização ou exploração geral
→ Hoje | Jornada | Explorar | Mapa | Eu
```

O Mapa não entra entre a Home e a Tela Hoje.

## 5. Início protegido móvel validado

A UXA-023 permanece como contrato funcional. A UXA-034 reformulada e a UXA-035 estabelecem quatro estados móveis de 390 por 844 pixels:

1. explicação anterior ao relato;
2. acesso somente quando necessário;
3. escolha de modalidade e rascunho mínimo;
4. revisão anterior ao processamento específico.

O conjunto demonstra:

- relato pessoal separado de dados técnicos e de acesso;
- estados nomeados, pausáveis e retomáveis, sem formulário linear obrigatório;
- ação inicial com destino explícito;
- sessão válida sem repetição do acesso;
- texto, voz, arquivo e perguntas opcionais sem seleção automática;
- explicação anterior para voz e arquivo;
- compartilhamento mínimo;
- efeitos distintos de pausa, salvamento, saída e exclusão;
- inventário antes do processamento;
- autorizações inicialmente desmarcadas;
- uso limitado à preparação de compreensão inicial temporária e revisável;
- recusa sem processamento;
- persistência e personalização bloqueadas até a revisão da compreensão inicial;
- exploração sem personalização disponível.

Arquivos vetoriais:

- `docs/assets/wireframes/uxa-034-protected-entry-explanation-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-access-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-sharing-mobile.svg`;
- `docs/assets/wireframes/uxa-034-protected-entry-review-mobile.svg`.

A validação não conclui política jurídica, segurança técnica, autenticação, armazenamento, voz, arquivos, IA, compreensão inicial gráfica, referência para computador, protótipo, teste com usuários ou implementação.

## 6. Mapa e estados validados

O Mapa principal, o uso sem localização, a Lista territorial, o estado sem resultados e a referência para computador permanecem funcionalmente validados e reformulados pelas UXA-024 a UXA-033.

## 7. Proteções vigentes

- nenhum relato é solicitado antes da explicação;
- dados de acesso não são tratados como conteúdo da jornada;
- autenticação não autoriza processamento;
- acesso aparece somente quando necessário;
- modalidades permanecem equivalentes;
- voz e arquivo exigem explicação anterior;
- compartilhamento mínimo é legítimo;
- pausa, salvar, sair e excluir possuem efeitos distintos;
- revisão antecede processamento;
- autorizações são específicas e inicialmente desmarcadas;
- recusa não inicia processamento;
- persistência e personalização dependem do gate;
- localização permanece opcional;
- publicidade não aumenta relevância pessoal;
- Engenharia de Produto permanece pausada.

## 8. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. criar a referência móvel da Página Inicial pública;
2. materializar a revisão da compreensão inicial;
3. validar a transição para a primeira Tela Hoje;
4. criar estados especializados de texto, voz e arquivos;
5. criar referência do início protegido para computador;
6. criar estados de processamento, pausa, falha e retomada;
7. retomar independentemente a reaplicação dos quatro testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
