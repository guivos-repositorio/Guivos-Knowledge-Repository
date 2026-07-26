---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-000
related:
  - UXA-001
  - UXA-002
  - UXA-003
  - UXA-004
  - UXA-006
  - UXA-007
  - UXA-008
  - UXA-009
  - UXA-020
  - PAS-001
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade (identificador UXA-005)

## 1. Finalidade

Este programa materializa hipóteses de arquitetura da experiência em wireframes de baixa fidelidade, permitindo validar organização, hierarquia, conteúdo, ações e continuidade entre superfícies antes de qualquer decisão de identidade visual ou implementação.

Os wireframes e contratos estruturais atualmente incluídos são:

1. **Wireframe de Baixa Fidelidade da Tela Hoje** (identificador UXA-006);
2. **Wireframe de Baixa Fidelidade do Detalhe de Oportunidade** (identificador UXA-007);
3. **Wireframe de Baixa Fidelidade do Cadastro de Oportunidade pela Organização** (identificador UXA-008);
4. **Página Inicial da Guivos e Início da Jornada** (identificador UXA-020), inicialmente representada por wireframe textual de baixa fidelidade.

A HOME passa a anteceder a Tela Hoje na primeira entrada pessoal. Essa mudança de sequência não invalida os wireframes anteriores; ela delimita melhor suas responsabilidades.

## 2. Natureza dos artefatos

Os wireframes:

- são hipóteses estruturais para revisão;
- utilizam conteúdo ilustrativo, não dados reais;
- representam prioridade e relação funcional, não acabamento;
- podem ser alterados sem migração de produto;
- não definem componentes técnicos;
- não constituem especificação de implementação;
- não substituem os contratos especializados da Especificação Arquitetural do Guivos Journey (identificador PAS-001);
- não autorizam protótipo de alta fidelidade.

Wireframes textuais e arquivos gráficos vetoriais possuem a mesma natureza preparatória. A ausência de arquivo gráfico não reduz a necessidade de validar hierarquia, autonomia, estados alternativos e continuidade.

## 3. O que deverá ser validado

### 3.1 Compreensão

- A finalidade da superfície é compreendida rapidamente?
- A diferença entre HOME e Tela Hoje é clara?
- A pessoa compreende como iniciar sua jornada e o que acontecerá com o relato?
- O participante reconhece o que merece atenção na Tela Hoje?
- Preço, condições, elegibilidade e relação comercial estão claros?
- A Organização entende o que precisa informar e por quê?
- Ações principais e alternativas são distinguíveis?
- Identificadores técnicos podem ser ignorados sem prejudicar a leitura?

### 3.2 Hierarquia

- O item mais importante ocupa a posição correta?
- A HOME apresenta propósito e início da jornada antes de soluções comerciais?
- Informações secundárias permanecem acessíveis sem competir com a decisão?
- A tela evita excesso de cartões e blocos?
- Estados vazios e ausência legítima permanecem possíveis?

### 3.3 Autonomia

- A pessoa consegue conhecer o ecossistema sem iniciar a jornada?
- A pessoa escolhe entre texto, voz, arquivos, perguntas progressivas ou adiamento?
- O participante consegue adiar, salvar, ocultar, contestar ou ajustar relevância?
- O fluxo evita pressionar contratação ou inscrição?
- A Organização consegue salvar rascunho, revisar e corrigir antes do envio?

### 3.4 Continuidade

- A HOME conduz naturalmente ao relato, à compreensão inicial e à Tela Hoje?
- A Tela Hoje conduz naturalmente ao Próximo Passo, oportunidade, Coletivo ou controle aplicável?
- O detalhe de oportunidade preserva contexto, origem e condições antes da ação?
- O cadastro organizacional produz informações suficientes para cartões, detalhe, mapa, busca e comparação?

## 4. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo, estado informativo ou área auxiliar |
| texto sublinhado | ação secundária ou explicação |
| círculos numerados | etapas de fluxo |
| linha contínua | agrupamento ou separação estrutural |

Cor, iconografia e tipografia não possuem significado definitivo neste programa.

## 5. Dimensões iniciais de tela

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Página Inicial da Guivos | web responsiva e aplicativo | estrutura textual; dimensões gráficas pendentes |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1440 × 1024 |

As dimensões servem somente para verificar densidade e hierarquia iniciais. Responsividade e adaptação a outros dispositivos permanecem pendentes.

## 6. Relação entre os wireframes

```text
Página Inicial da Guivos
→ início voluntário da jornada
→ relato multimodal do Momento Atual
→ compreensão inicial revisada e confirmada
→ Tela Hoje
→ oportunidade apresentada com razão resumida
→ detalhe da oportunidade
→ decisão consciente de salvar, comparar ou iniciar processo

Organização
→ cadastro governado da oportunidade
→ avaliação e ativação
→ apresentação na Tela Hoje, em Explorar, no Mapa ou em uma intervenção contextual
```

O início da jornada não garante recomendação. O cadastro não garante ativação. A ativação não garante apresentação. A apresentação não representa recomendação definitiva nem contratação.

Antes da compreensão inicial confirmada, a HOME e as soluções do ecossistema poderão apresentar somente conteúdo geral, institucional, editorial ou resultante de busca explícita, sem afirmar relevância pessoal.

## 7. Artefatos especializados

| Nome completo | Identificador | Superfície | Artefato visual |
|---|---|---|---|
| [Página Inicial da Guivos e Início da Jornada](uxa-020-home-and-journey-entry.md) | UXA-020 | HOME e início da jornada | wireframe textual no documento; arquivo gráfico pendente |
| [Wireframe da Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | Tela Hoje | [arquivo gráfico vetorial](../assets/wireframes/uxa-006-hoje-mobile.svg) |
| [Wireframe do Detalhe de Oportunidade](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | Detalhe de oportunidade | [arquivo gráfico vetorial](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg) |
| [Wireframe do Cadastro pela Organização](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | Cadastro pela Organização | [arquivo gráfico vetorial](../assets/wireframes/uxa-008-organization-opportunity-registration-desktop.svg) |

## 8. Limites

Este programa não:

- aprova a navegação como definitiva;
- define marca, paleta, tipografia ou ilustração;
- define textos finais de interface;
- cria componentes de sistema de design;
- conclui acessibilidade;
- cria protótipo navegável;
- executa teste de usabilidade;
- define preço ou oferta comercial real;
- define formatos técnicos de voz ou arquivos;
- inicia Engenharia de Produto.

## 9. Padrão de linguagem

O **Padrão de Linguagem Clara e Identificadores Técnicos** (identificador UXA-009) é obrigatório para revisões e comunicações desta frente.

O nome completo deverá aparecer antes do código, e estados técnicos deverão possuir explicação em português.

## 10. Próximo ponto de decisão

Os próximos pontos deverão ser autorizados separadamente e poderão:

1. validar funcionalmente a HOME e a sequência de primeira entrada;
2. criar o arquivo gráfico vetorial da HOME;
3. detalhar captura por texto, voz e arquivo;
4. validar a compreensão inicial e seus controles;
5. detalhar a primeira Tela Hoje após a transição;
6. selecionar estados alternativos e exceções para novos wireframes;
7. autorizar ou não a criação de um protótipo navegável de baixa fidelidade.