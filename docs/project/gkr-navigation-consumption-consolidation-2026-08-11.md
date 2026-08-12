---
id: GKR-NAV-CONSOLIDATION-2026-08-11
title: Consolidação da Navegação de Consumo do GKR
status: draft
version: 1.0.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-11
depends_on:
  - GKR-STATE-001
related:
  - GKR-GOV-CONSUMPTION-001
  - GKR-FUNDAMENTOS-CONSOLIDADO-001
  - GKR-MODELO-EVOLUCAO-CONSOLIDADO-001
  - GKR-UX-HOME-CONSOLIDATED-001
  - GTM-CONSOLIDATED-001
  - GEM-CONSUMPTION-001
  - GEM-M0-M6-CONSUMPTION-001
  - RP-001-CONSUMPTION-001
normative: false
---

# Consolidação da Navegação de Consumo do GKR

## 1. Problema observado

A navegação pública do GKR havia crescido junto com o processo de construção arquitetural.

Como consequência, artefatos com funções muito diferentes apareciam no mesmo nível de leitura:

- documentos mestres;
- contratos funcionais;
- wireframes;
- validações;
- auditorias;
- matrizes;
- adendos;
- changelogs;
- handoffs;
- referências históricas.

A estrutura era adequada para rastreabilidade técnica, mas inadequada como biblioteca de conhecimento para leitura, interpretação e impressão por assunto.

---

## 2. Regra adotada

> **A navegação pública do GKR deve refletir assuntos de consumo, não a árvore histórica de construção do conhecimento.**

Portanto:

```text
MENU PÚBLICO
→ documentos mestres e assuntos de leitura

CORPUS INTERNO
→ contratos, auditorias, validações, matrizes, históricos e fontes técnicas
```

A remoção de um documento do menu não significa exclusão de sua função de rastreabilidade.

---

## 3. Critério de consolidação

Um assunto deve possuir documento consolidado quando:

- sua compreensão exigir abrir muitos arquivos pequenos;
- os arquivos representarem etapas sucessivas de uma mesma decisão;
- existirem versões intermediárias que confundam o estado atual;
- a leitura isolada não for suficiente para impressão executiva;
- a fragmentação transferir para o leitor complexidade que pertence à governança interna.

Subdivisões continuam legítimas quando:

- o assunto possui domínios claramente distintos;
- o documento único se tornaria excessivamente grande ou misturaria responsabilidades diferentes;
- existe necessidade operacional frequente de consulta independente.

---

## 4. Documentos de consumo criados

Foram criadas portas consolidadas para:

1. **Fundamentos da Guivos**;
2. **Modelo Fundamental da Evolução**;
3. **Home Pública da Guivos**;
4. **Go-to-Market da Guivos**;
5. **Economia, Planos e Monetização**;
6. **Planejamento Financeiro M0–M6**;
7. **Pesquisa do Ecossistema**;
8. **Governança do Guivos Knowledge Repository**.

A Validação de Mercado já possuía um documento agregador suficientemente completo e foi mantida como porta única.

---

## 5. Home Pública

A antiga página `UXA-022 — Wireframe de Baixa Fidelidade da Página Inicial Pública da Guivos` foi removida do working tree e da navegação porque não representa a arquitetura vigente da Home.

O estado atual está consolidado em `GKR-UX-HOME-CONSOLIDATED-001`.

Decisão vigente:

> **a Home Pública atual não utiliza wireframe como etapa do processo.**

O SVG associado à antiga UXA-022 permanece apenas como artefato histórico interno enquanto integra instrumentos técnicos legados de rastreabilidade visual. Ele:

- não aparece no menu público;
- não possui autoridade de Design sobre a Home atual;
- não deve ser utilizado como referência corrente;
- não altera a decisão de não trabalhar com wireframe para a Home.

Sua remoção física exige reconciliação própria dos inventários técnicos de SVGs para não produzir contagens falsas ou quebrar instrumentos históricos.

---

## 6. Navegação resultante

A navegação passa a utilizar os seguintes grandes assuntos:

- Comece por aqui;
- Fundamentos da Guivos;
- Ecossistema e Produtos;
- Experiência, Design e Jornadas;
- Pesquisa e Validação;
- Estratégia, Mercado e Crescimento;
- Economia, Planos e Monetização;
- Arquitetura, Dados e IA;
- Governança do Repositório.

A maioria desses grupos possui poucos documentos diretamente consumíveis.

Subgrupos são preservados somente onde continuam úteis, como Produtos Especializados e Opportunity Boost.

---

## 7. Impressão

A navegação não expõe mais a página agregada do plugin `print-site` como item cotidiano.

Cada página de leitura continua oferecendo a ação:

> **Imprimir este assunto**

Assim, um documento consolidado pode ser impresso ou salvo como PDF isoladamente.

A geração agregada do corpus continua configurada para necessidades de arquivo e auditoria.

---

## 8. Hierarquia visual

Os títulos de primeiro nível do menu recebem maior hierarquia tipográfica e peso visual que documentos e subgrupos.

A intenção é tornar imediatamente distinguíveis:

```text
ASSUNTO PRINCIPAL
→ documento
→ eventual subgrupo necessário
```

A alteração é de navegação e legibilidade. Não redefine a identidade visual da Guivos.

---

## 9. O que permanece interno

Continuam no corpus, quando ainda possuem função de rastreabilidade:

- UXAs;
- contratos especializados;
- matrizes;
- registros granulares;
- auditorias;
- validações;
- changelogs;
- adendos;
- documentos de construção;
- materializações históricas.

Eles podem ser encontrados por busca, links internos ou no próprio repositório GitHub, sem ocupar a navegação principal.

---

## 10. Limite desta consolidação

Esta reorganização:

- não altera o propósito da Guivos;
- não redefine participantes;
- não altera a arquitetura de produtos;
- não inicia Engenharia de Produto;
- não inicia materialização visual da Home;
- não transforma metas em resultados;
- não promove mercados candidatos;
- não valida preços por consequência;
- não apaga o histórico Git.

Seu objetivo é reduzir complexidade de consumo e eliminar referências públicas que não representam mais o estado vigente.

---

## 11. Regra para evolução futura do menu

Um novo artefato técnico **não deve entrar automaticamente na navegação pública**.

Antes de adicionar um item ao menu, perguntar:

1. isto é um assunto que alguém precisa abrir diretamente?
2. já existe um documento mestre que deveria absorver essa atualização?
3. o item melhora a leitura ou apenas expõe o processo interno?
4. faz sentido imprimir este arquivo isoladamente?
5. a informação é vigente ou apenas histórica?

Se o documento for fonte técnica de uma decisão já consolidada, a preferência é mantê-lo fora da navegação principal e atualizar o documento mestre correspondente.
