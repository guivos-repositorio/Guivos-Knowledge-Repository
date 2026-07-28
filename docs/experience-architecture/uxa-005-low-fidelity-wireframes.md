---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.18.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-28
parent: UXA-000
related:
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-003-A1
  - UXA-004
  - UXA-006
  - UXA-007
  - UXA-008
  - UXA-009
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
  - UXA-036
  - PAS-001
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade

## 1. Finalidade

Este programa materializa hipóteses de Arquitetura da Experiência em wireframes de baixa fidelidade. O objetivo é validar organização, hierarquia, conteúdo, ações e continuidade antes de identidade visual ou implementação.

## 2. Regra de ordem

Os identificadores preservam a ordem histórica de criação. Eles não determinam a ordem das telas.

```text
Página Inicial pública
→ explicação do ambiente protegido
→ acesso, quando necessário
→ escolha e rascunho mínimo
→ revisão e autorização específica
→ processamento visível e interrompível
→ compreensão inicial apresentada como hipótese
→ revisão da compreensão
→ decisões separadas sobre persistência e personalização
→ Tela Hoje
→ Hoje | Jornada | Explorar | Mapa | Eu
```

## 3. Artefatos pela ordem funcional

1. Página Inicial e início da jornada — UXA-020;
2. validação da Home pública — UXA-021;
3. wireframe da Home para computador — UXA-022;
4. validação do início protegido — UXA-023;
5. wireframe móvel do início protegido — UXA-034;
6. validação do wireframe móvel do início protegido — UXA-035;
7. wireframe móvel da compreensão inicial — UXA-036;
8. wireframe da Tela Hoje — UXA-006;
9. wireframe móvel do Mapa — UXA-024;
10. validações e estados do Mapa — UXA-025 a UXA-033;
11. wireframe do Detalhe — UXA-007;
12. wireframe do Cadastro pela Organização — UXA-008.

## 4. Natureza dos artefatos

Os wireframes:

- são hipóteses estruturais para revisão;
- utilizam conteúdo ilustrativo;
- representam prioridade e relação funcional, não acabamento;
- não definem componentes técnicos;
- não constituem especificação de implementação;
- não autorizam protótipo de alta fidelidade.

Wireframe gráfico não equivale a validação funcional. Validação funcional não equivale a teste de usabilidade, design ou desenvolvimento.

## 5. O que deverá ser validado

### 5.1 Início protegido

- A pessoa entende que saiu da Home pública?
- Nenhum relato pessoal é solicitado antes da explicação?
- Dados de acesso e conteúdo da jornada são distinguíveis?
- Os estados são compreendidos como possíveis, não formulário obrigatório?
- O acesso aparece somente quando necessário?
- Criar conta permanece separado de autorizar processamento?
- Texto, voz, arquivo e perguntas são alternativas equivalentes?
- Compartilhamento mínimo é legítimo?
- Pausar, salvar, sair e excluir possuem efeitos distintos?
- A revisão antecede autorização específica?
- Autorizações começam desmarcadas?
- Recusar impede processamento?

### 5.2 Compreensão inicial

- O processamento utiliza somente itens autorizados?
- A pessoa reconhece o que está dentro e fora do processamento?
- A finalidade é compreensível?
- Interromper possui consequência clara?
- A compreensão é percebida como hipótese, não diagnóstico?
- Momento Atual, avanço e Próximo Passo são distinguíveis?
- Origem, natureza, confiança e lacunas são compreensíveis?
- Ausência de evidência é declarada sem produzir avanço artificial?
- A pessoa consegue confirmar uma afirmação e rejeitar outra?
- Corrigir interpretação não altera silenciosamente o relato original?
- Retirar autorização, remover interpretação e excluir conteúdo são distintos?
- Persistência e personalização são decisões independentes?
- Nenhuma opção começa marcada?
- Continuar sem personalização permanece uma alternativa real?
- A transição para a Tela Hoje preserva a condição escolhida?
- Base insuficiente evita pressão para compartilhar mais?

### 5.3 Mapa e superfícies recorrentes

- Mapa e Lista representam a mesma consulta?
- Quantidade, filtros e ordenação são compreensíveis?
- Relação comercial está separada da relevância?
- Dados ausentes são apresentados sem inferência?
- Cobertura, falha e indisponibilidade são distinguíveis?
- Em computador, filtros, Mapa, Lista e seleção parecem partes da mesma consulta?

### 5.4 Autonomia e continuidade

- A pessoa pode adiar, recusar, pausar ou sair sem culpa?
- Compartilhar pouco não é tratado como insuficiência pessoal?
- Não autorizar possui consequência clara e não punitiva?
- O início protegido conduz à compreensão revisável, não diretamente à persistência?
- A compreensão revisada conduz à Tela Hoje ou à exploração geral?
- Mapa e Lista preservam consulta, quantidade, atualização, ordenação e seleção?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo ou estado informativo |
| texto sublinhado | ação secundária ou explicação |
| estado textual nomeado | posição funcional sem obrigatoriedade linear |
| caixa de seleção vazia | autorização ou escolha ainda não concedida |
| declaração textual | estado de relato, processamento, hipótese ou decisão |
| ação com consequência | interrupção, pausa, saída, exclusão ou recusa explícita |
| rótulo de natureza | confirmado, inferido, desconhecido ou contestado |
| confiança em texto | intensidade de inferência sem equivaler a certeza |
| ausência de marcador | posição da pessoa não utilizada |
| faixa compartilhada | painéis pertencem à mesma consulta |

Cor, iconografia e tipografia não possuem significado definitivo.

## 7. Dimensões iniciais

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Home pública | web para computador | 1.440 × 2.200 |
| Início protegido — quatro estados | aplicativo móvel | 390 × 844 cada |
| Compreensão inicial — quatro estados | aplicativo móvel | 390 × 844 cada |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Mapa e estados móveis | aplicativo móvel | 390 × 844 |
| Mapa com e sem resultados | web para computador | 1.440 × 1.024 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1.440 × 1.024 |

## 8. Relação entre os wireframes

```text
Página Inicial pública
→ decisão voluntária
→ explicação do ambiente protegido
→ acesso, somente quando necessário
→ modalidade e rascunho mínimo
→ revisão e autorização específica
→ processamento visível
→ hipótese inicial
→ revisão da hipótese
→ decisões sobre persistência e personalização
→ Tela Hoje ou exploração geral
→ Mapa e demais superfícies recorrentes
```

A sequência protegida é pausável e retomável. A compreensão poderá ser rejeitada ou excluída sem impedir exploração geral.

## 9. Artefatos especializados

| Nome | ID | Superfície | Artefato |
|---|---|---|---|
| Página Inicial e Início | UXA-020 | primeira entrada | contrato textual |
| Validação da Home | UXA-021 | Home | hierarquia validada |
| Wireframe da Home | UXA-022 | Home | arquivo vetorial |
| Contrato do Início Protegido | UXA-023 | início protegido | validação funcional |
| Wireframe do Início Protegido | UXA-034 | início protegido | quatro arquivos vetoriais reformulados |
| Validação do Wireframe Protegido | UXA-035 | início protegido | validação funcional especializada |
| Compreensão Inicial | UXA-036 | compreensão | quatro arquivos vetoriais |
| Tela Hoje | UXA-006 | recorrente | arquivo vetorial |
| Mapa e estados | UXA-024 a UXA-032 | Mapa | arquivos vetoriais móveis e desktop |
| Validações do Mapa | UXA-025, UXA-027, UXA-029, UXA-031 e UXA-033 | Mapa | validações funcionais |
| Detalhe | UXA-007 | detalhe | arquivo vetorial |
| Cadastro | UXA-008 | cadastro | arquivo vetorial |

## 10. Resultados materializados

O início protegido é funcionalmente válido após reformulação pelas UXA-034 e UXA-035.

A compreensão inicial foi materializada pela UXA-036 com processamento visível, hipótese corrigível, revisão por afirmação e decisões separadas sobre persistência e personalização. Sua validação especializada permanece pendente.

## 11. Limites

Este programa não define marca, tecnologia, autenticação, armazenamento, gravação, transcrição, upload, IA, inferências sensíveis, textos finais, responsividade, tablet, acessibilidade técnica, protótipo, teste de usabilidade ou Engenharia de Produto.

## 12. Próximos pontos de decisão

Os próximos pontos exigem autorizações separadas:

1. validar funcionalmente o wireframe móvel da compreensão inicial;
2. criar a referência móvel da Home;
3. detalhar a primeira Tela Hoje após a transição;
4. criar estados de processamento, pausa, falha e retomada;
5. criar referência do início protegido e da compreensão para computador;
6. criar estados especializados de texto, voz e arquivos;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhuma etapa posterior é iniciada automaticamente.
