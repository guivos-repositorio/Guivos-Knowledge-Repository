---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.5.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
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
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - PAS-001
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade

## 1. Finalidade

Este programa materializa hipóteses de Arquitetura da Experiência em wireframes de baixa fidelidade. O objetivo é validar organização, hierarquia, conteúdo, ações e continuidade entre superfícies antes de qualquer decisão de identidade visual ou implementação.

## 2. Regra de ordem

Os identificadores preservam a ordem histórica de criação dos documentos. Eles não determinam a ordem em que as telas aparecem para a pessoa.

A ordem funcional da primeira entrada é:

```text
Página Inicial pública da Guivos
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje
```

A correção formal está registrada em [Correção da Ordem Funcional da Primeira Entrada Pessoal](uxa-003-a1-first-entry-functional-order.md).

## 3. Artefatos pela ordem funcional

1. **Página Inicial da Guivos e Início da Jornada** — identificador UXA-020, com o contrato entre Home, ambiente protegido e Tela Hoje;
2. **Validação Funcional e Reformulação da Página Inicial Pública** — identificador UXA-021;
3. **Wireframe de Baixa Fidelidade da Página Inicial Pública** — identificador UXA-022, com arquivo gráfico vetorial para computador;
4. **Validação Funcional do Início Protegido da Jornada** — identificador UXA-023;
5. **Wireframe de Baixa Fidelidade da Tela Hoje** — identificador UXA-006, utilizado somente depois da compreensão inicial suficiente e autorizada;
6. **Wireframe de Baixa Fidelidade do Detalhe de Oportunidade** — identificador UXA-007;
7. **Wireframe de Baixa Fidelidade do Cadastro de Oportunidade pela Organização** — identificador UXA-008.

A Página Inicial pública antecede o início protegido, e ambos antecedem a Tela Hoje.

## 4. Natureza dos artefatos

Os wireframes:

- são hipóteses estruturais para revisão;
- utilizam conteúdo ilustrativo, não dados reais;
- representam prioridade e relação funcional, não acabamento;
- podem ser alterados sem migração de produto;
- não definem componentes técnicos;
- não constituem especificação de implementação;
- não substituem os contratos especializados do Guivos Journey;
- não autorizam protótipo de alta fidelidade.

Wireframes textuais e arquivos gráficos vetoriais possuem a mesma natureza preparatória. Um arquivo gráfico materializa a hierarquia para inspeção, mas não equivale a identidade visual, protótipo navegável ou desenvolvimento.

## 5. O que deverá ser validado

### 5.1 Compreensão

- A finalidade de cada superfície é compreendida rapidamente?
- A diferença entre Página Inicial pública, início protegido e Tela Hoje é clara?
- A pessoa compreende como iniciar sua jornada e o que acontecerá com o relato?
- A pessoa reconhece que a Home pública não coleta relatos pessoais?
- O participante reconhece o que merece atenção na Tela Hoje?
- Preço, condições, elegibilidade e relação comercial estão claros?
- A Organização entende o que precisa informar e por quê?
- Ações principais e alternativas são distinguíveis?
- Identificadores técnicos podem ser ignorados sem prejudicar a leitura?

### 5.2 Hierarquia

- O item mais importante ocupa a posição correta?
- A Home apresenta propósito e descrição concreta antes das soluções comerciais?
- Os caminhos pessoal, geral e institucional permanecem distintos?
- O ecossistema é organizado por finalidade, e não como lista plana?
- Informações secundárias permanecem acessíveis sem competir com a decisão?
- A tela evita excesso de cartões e blocos?
- Estados vazios e ausência legítima permanecem possíveis?

### 5.3 Autonomia

- A pessoa consegue conhecer o ecossistema sem iniciar a jornada?
- A pessoa escolhe entre texto, voz, arquivos, perguntas progressivas ou adiamento no ambiente protegido?
- O participante consegue adiar, salvar, ocultar, contestar ou ajustar relevância?
- O fluxo evita pressionar contratação ou inscrição?
- A Organização consegue salvar rascunho, revisar e corrigir antes do envio?

### 5.4 Continuidade

- A Home conduz naturalmente ao início protegido, à compreensão inicial e à Tela Hoje?
- A Tela Hoje conduz naturalmente ao Próximo Passo, oportunidade, Coletivo ou controle aplicável?
- O detalhe de oportunidade preserva contexto, origem e condições antes da ação?
- O cadastro organizacional produz informações suficientes para cartões, detalhe, mapa, busca e comparação?

## 6. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo, estado informativo ou área auxiliar |
| texto sublinhado | ação secundária ou explicação |
| círculos numerados | etapas de fluxo |
| linha contínua | agrupamento ou separação estrutural |

Cor, iconografia e tipografia não possuem significado definitivo neste programa.

## 7. Dimensões iniciais

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Página Inicial pública da Guivos | web para computador | 1.440 × 2.200 |
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1.440 × 1.024 |

As dimensões servem somente para verificar densidade e hierarquia iniciais. Responsividade e adaptação a outros dispositivos permanecem pendentes.

A referência gráfica da Página Inicial pública representa o estado principal para visitante sem jornada. A versão móvel e as variações por estado permanecem atos posteriores separados.

## 8. Relação entre os wireframes

```text
Página Inicial pública da Guivos
→ início voluntário da jornada
→ ambiente protegido para relato multimodal do Momento Atual
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

Antes da compreensão inicial confirmada, a Home e as soluções do ecossistema poderão apresentar somente conteúdo geral, institucional, editorial ou resultante de busca explícita, sem afirmar relevância pessoal.

## 9. Artefatos especializados

| Nome completo | Identificador | Superfície | Artefato visual |
|---|---|---|---|
| [Página Inicial da Guivos e Início da Jornada](uxa-020-home-and-journey-entry.md) | UXA-020 | Home e início protegido | wireframes textuais no documento |
| [Validação Funcional da Página Inicial Pública](uxa-021-public-home-functional-validation-and-reformulation.md) | UXA-021 | Home pública | hierarquia funcional validada |
| [Wireframe da Página Inicial Pública](uxa-022-public-home-low-fidelity-wireframe.md) | UXA-022 | Home pública | [arquivo gráfico vetorial](../assets/wireframes/uxa-022-public-home-desktop.svg) |
| [Validação do Início Protegido da Jornada](uxa-023-protected-journey-entry-functional-validation-and-reformulation.md) | UXA-023 | início protegido | contrato funcional validado; wireframe gráfico pendente |
| [Wireframe da Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | Tela Hoje recorrente | [arquivo gráfico vetorial](../assets/wireframes/uxa-006-hoje-mobile.svg) |
| [Wireframe do Detalhe de Oportunidade](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | detalhe da oportunidade | [arquivo gráfico vetorial](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg) |
| [Wireframe do Cadastro pela Organização](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | cadastro pela Organização | [arquivo gráfico vetorial](../assets/wireframes/uxa-008-organization-opportunity-registration-desktop.svg) |

## 10. Resultado da Página Inicial pública

O wireframe gráfico da Página Inicial pública materializa:

- cabeçalho orientado por intenção;
- propósito e descrição concreta da Guivos;
- ação de iniciar a jornada;
- alternativa de exploração sem personalização;
- garantia curta de ausência de coleta pública;
- explicação do funcionamento em etapas;
- caminhos pessoal, geral e institucional;
- ecossistema agrupado por finalidade;
- possibilidades gerais identificadas;
- confiança, privacidade, transparência e controle;
- rodapé institucional.

O arquivo representa conteúdo ilustrativo e não cria textos finais, ofertas reais ou componentes de interface.

## 11. Limites

Este programa não:

- aprova a navegação como definitiva;
- define marca, paleta, tipografia ou ilustração;
- define textos finais de interface;
- cria componentes de sistema de design;
- conclui acessibilidade ou responsividade;
- cria protótipo navegável;
- executa teste de usabilidade;
- define preço ou oferta comercial real;
- define formatos técnicos de voz ou arquivos;
- inicia Engenharia de Produto.

## 12. Próximos pontos de decisão

Os próximos pontos deverão ser autorizados separadamente e poderão:

1. criar o wireframe gráfico do início protegido da jornada;
2. criar a referência móvel da Página Inicial pública;
3. detalhar estados de texto, voz e arquivos;
4. validar a compreensão inicial e seus controles;
5. detalhar a primeira Tela Hoje após a transição;
6. selecionar estados alternativos e exceções para novos wireframes;
7. autorizar ou não a criação de um protótipo navegável de baixa fidelidade;
8. retomar, de forma independente, a reaplicação dos quatro testes dos Resultados Empresariais.

Nenhuma etapa posterior é iniciada automaticamente.
