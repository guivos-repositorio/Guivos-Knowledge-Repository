---
id: UXA-005
title: Programa Inicial de Wireframes de Baixa Fidelidade
status: draft
version: 0.2.0
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
  - PAS-001
normative: false
---

# Programa Inicial de Wireframes de Baixa Fidelidade (identificador UXA-005)

## 1. Finalidade

Este incremento materializa as primeiras hipóteses de arquitetura da experiência em wireframes de baixa fidelidade, permitindo validar organização, hierarquia, conteúdo, ações e continuidade entre superfícies antes de qualquer decisão de identidade visual ou implementação.

Os primeiros wireframes são:

1. **Wireframe de Baixa Fidelidade da Tela Hoje** (identificador UXA-006);
2. **Wireframe de Baixa Fidelidade do Detalhe de Oportunidade** (identificador UXA-007);
3. **Wireframe de Baixa Fidelidade do Cadastro de Oportunidade pela Organização** (identificador UXA-008).

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

## 3. O que deverá ser validado

### 3.1 Compreensão

- a finalidade da tela é compreendida rapidamente?;
- o participante reconhece o que merece atenção?;
- preço, condições, elegibilidade e relação comercial estão claros?;
- a Organização entende o que precisa informar e por quê?;
- ações principais e alternativas são distinguíveis?;
- identificadores técnicos podem ser ignorados sem prejudicar a leitura?.

### 3.2 Hierarquia

- o item mais importante ocupa a posição correta?;
- informações secundárias permanecem acessíveis sem competir com a decisão?;
- a tela evita excesso de cartões e blocos?;
- estados vazios e ausência legítima permanecem possíveis?.

### 3.3 Autonomia

- o participante consegue adiar, salvar, ocultar, contestar ou ajustar relevância?;
- o fluxo evita pressionar contratação ou inscrição?;
- a Organização consegue salvar rascunho, revisar e corrigir antes do envio?.

### 3.4 Continuidade

- a Tela Hoje conduz naturalmente ao Próximo Passo, oportunidade, Coletivo ou controle aplicável?;
- o detalhe de oportunidade preserva contexto, origem e condições antes da ação?;
- o cadastro organizacional produz informações suficientes para cartões, detalhe, mapa, busca e comparação?.

## 4. Convenções de baixa fidelidade

| Elemento | Convenção |
|---|---|
| retângulo com borda | área funcional ou cartão |
| preenchimento escuro | ação principal ou estado selecionado |
| preenchimento cinza | resumo, estado informativo ou área auxiliar |
| texto sublinhado | ação secundária ou explicação |
| círculos numerados | etapas de fluxo |
| linha contínua | agrupamento ou separação estrutural |

Cor, iconografia e tipografia não possuem significado definitivo neste incremento.

## 5. Dimensões iniciais de tela

| Wireframe | Canal | Dimensão de referência |
|---|---|---|
| Tela Hoje | aplicativo móvel | 390 × 844 |
| Detalhe de oportunidade | aplicativo móvel | 390 × 980 |
| Cadastro pela Organização | web para computador | 1440 × 1024 |

As dimensões servem somente para verificar densidade e hierarquia iniciais. Responsividade e adaptação a outros dispositivos permanecem pendentes.

## 6. Relação entre os três wireframes

```text
Tela Hoje
→ oportunidade apresentada com razão resumida
→ detalhe da oportunidade
→ decisão consciente de salvar, comparar ou iniciar processo

Organização
→ cadastro governado da oportunidade
→ avaliação e ativação
→ apresentação na Tela Hoje, em Explorar, no Mapa ou em uma intervenção contextual
```

O cadastro não garante ativação. A ativação não garante apresentação. A apresentação não representa recomendação definitiva nem contratação.

## 7. Artefatos especializados

| Nome completo | Identificador | Superfície | Artefato visual |
|---|---|---|---|
| [Wireframe da Tela Hoje](uxa-006-today-low-fidelity-wireframe.md) | UXA-006 | Tela Hoje | [arquivo gráfico vetorial](../assets/wireframes/uxa-006-hoje-mobile.svg) |
| [Wireframe do Detalhe de Oportunidade](uxa-007-opportunity-detail-low-fidelity-wireframe.md) | UXA-007 | Detalhe de oportunidade | [arquivo gráfico vetorial](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg) |
| [Wireframe do Cadastro pela Organização](uxa-008-organization-opportunity-registration-low-fidelity-wireframe.md) | UXA-008 | Cadastro pela Organização | [arquivo gráfico vetorial](../assets/wireframes/uxa-008-organization-opportunity-registration-desktop.svg) |

## 8. Limites

Este incremento não:

- aprova a navegação como definitiva;
- define marca, paleta, tipografia ou ilustração;
- define textos finais de interface;
- cria componentes de sistema de design;
- conclui acessibilidade;
- cria protótipo navegável;
- executa teste de usabilidade;
- define preço ou oferta comercial real;
- inicia Engenharia de Produto (Product Engineering);
- retoma a decisão sobre **Capacidade de reinvestimento responsável** (candidato empresarial BUS-CAND-010).

## 9. Padrão de linguagem

O **Padrão de Linguagem Clara e Identificadores Técnicos** (identificador UXA-009) é obrigatório para revisões e comunicações desta frente.

O nome completo deverá aparecer antes do código, e estados técnicos deverão possuir explicação em português.

## 10. Próximo ponto de decisão

O próximo ponto deverá decidir, separadamente:

1. aceitar ou reformular a estrutura da Tela Hoje;
2. aceitar ou reformular a hierarquia do detalhe de oportunidade;
3. aceitar ou reformular o fluxo de cadastro da Organização;
4. selecionar estados alternativos e exceções para novos wireframes;
5. autorizar ou não a criação de um protótipo navegável de baixa fidelidade.
