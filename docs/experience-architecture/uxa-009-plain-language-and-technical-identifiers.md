---
id: UXA-009
title: Padrão de Linguagem Clara e Identificadores Técnicos
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-000
related:
  - UXA-001
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-008
  - GKR-STATE-001
normative: true
---

# Padrão de Linguagem Clara e Identificadores Técnicos (identificador UXA-009)

## 1. Finalidade

Este padrão garante que documentos, telas, apresentações e comunicações da Guivos possam ser compreendidos sem que a pessoa precise memorizar siglas, códigos ou nomes técnicos em inglês.

Os identificadores permanecem necessários para rastreabilidade arquitetural, mas não deverão substituir o nome completo do elemento.

## 2. Regra principal

Toda primeira menção deverá seguir esta ordem:

```text
nome completo em português
→ termo canônico em inglês, somente quando necessário
→ identificador técnico entre parênteses
```

Exemplo correto:

> Wireframe de Baixa Fidelidade da Tela Hoje (identificador UXA-006).

Exemplo a evitar:

> UXA-006.

Após a primeira menção, poderá ser utilizada uma forma curta compreensível, como `Tela Hoje`, `wireframe da oportunidade` ou `cadastro pela Organização`.

## 3. Identificador não é nome

Códigos como `UXA-006`, `BUS-CAND-010`, `COD-017` e `M7.19.2` são identificadores internos. Eles servem para:

- localizar documentos;
- preservar histórico;
- relacionar decisões;
- controlar versões;
- validar links;
- executar auditorias.

Eles não deverão ser apresentados como se fossem o nome principal de uma tela, decisão, etapa ou documento.

## 4. Padrões obrigatórios de apresentação

| Forma técnica | Forma de leitura preferencial |
|---|---|
| GKR | Repositório de Conhecimento da Guivos (Guivos Knowledge Repository — GKR) |
| UXA-000 | Arquitetura da Experiência da Guivos (identificador UXA-000) |
| UXA-006 | Wireframe de Baixa Fidelidade da Tela Hoje (identificador UXA-006) |
| COR | Registro de Candidatos a Resultados (Candidate Outcome Register — COR) |
| CODR | Registro de Decisões sobre Candidatos a Resultados (Candidate Outcome Decision Register — CODR) |
| COD-017 | Decisão sobre Candidato a Resultado número 17 (identificador COD-017) |
| BUS-CAND-010 | Capacidade de reinvestimento responsável (candidato empresarial BUS-CAND-010) |
| Business Outcomes | Resultados Empresariais (Business Outcomes) |
| Product Engineering | Engenharia de Produto (Product Engineering) |
| Under Validation | Em validação (`Under Validation`) |
| Merged | Incorporado (`Merged`) |
| Rejected | Rejeitado (`Rejected`) |
| PR | solicitação de integração no GitHub (Pull Request — PR) |
| SVG | arquivo gráfico vetorial escalável (Scalable Vector Graphics — SVG) |
| UI | Interface do Usuário (User Interface — UI) |
| UX | Experiência do Usuário (User Experience — UX) |

Quando uma tradução puder alterar o significado canônico, o termo em inglês deverá permanecer depois da explicação em português.

## 5. Regras para títulos e navegação

Títulos e menus deverão:

- começar pelo nome completo;
- apresentar o identificador no final, quando necessário;
- evitar sequências compostas somente por códigos;
- evitar status somente em inglês;
- utilizar palavras que indiquem a natureza do conteúdo: decisão, candidato, registro, wireframe, marco ou versão.

Exemplo preferencial:

> Wireframe da Tela Hoje — Baixa Fidelidade (UXA-006)

Exemplo a evitar:

> UXA-006 — Hoje

## 6. Regras para tabelas e relatórios

Quando houver códigos, a tabela deverá possuir ao menos uma coluna ou texto próximo com o nome completo.

Exemplo:

| Nome completo | Identificador | Estado |
|---|---|---|
| Capacidade de reinvestimento responsável | BUS-CAND-010 | Em validação |

Uma tabela técnica poderá preservar somente identificadores quando estiver claramente classificada como log, inventário mecânico ou registro de integração.

## 7. Regras para respostas ao Fundador e materiais executivos

Respostas, resumos executivos e apresentações deverão:

1. explicar primeiro o que foi decidido ou criado;
2. informar o nome completo;
3. apresentar o identificador apenas como referência secundária;
4. traduzir estados e etapas para português;
5. reduzir códigos em títulos, conclusões e próximos passos;
6. incluir um quadro de significados quando mais de três identificadores forem indispensáveis.

## 8. Termos da Arquitetura da Experiência

Nesta frente, utilizar preferencialmente:

- `Arquitetura da Experiência da Guivos`, em vez de apenas `UXA`;
- `Programa Inicial de Wireframes de Baixa Fidelidade`, em vez de apenas `UXA-005`;
- `Wireframe da Tela Hoje`, em vez de apenas `UXA-006`;
- `Wireframe do Detalhe de Oportunidade`, em vez de apenas `UXA-007`;
- `Wireframe do Cadastro de Oportunidade pela Organização`, em vez de apenas `UXA-008`;
- `Padrão de Linguagem Clara e Identificadores Técnicos`, em vez de apenas `UXA-009`.

## 9. Significado de validade do preço

`Validade do preço` é o período até o qual a Organização declara que o valor informado permanece vigente para uma nova inscrição, contratação ou compra.

Exemplo:

> R$ 79,90 por mês, válido para novas inscrições realizadas até 31/08/2026.

A validade do preço não é:

- duração do serviço;
- prazo da inscrição;
- tempo do contrato;
- vencimento da parcela;
- prazo de cancelamento;
- prazo de reembolso.

Após a data de validade, o preço deverá ser confirmado novamente. Caso o valor seja alterado durante um processo já iniciado, o participante deverá receber a nova condição e confirmar conscientemente antes de continuar.

## 10. Aplicação progressiva

A regra passa a valer imediatamente para:

- novos documentos da Arquitetura da Experiência;
- respostas e apresentações futuras;
- navegação oficial dessa frente;
- revisões dos documentos ativos.

Snapshots históricos e registros imutáveis não serão reescritos apenas para adequação editorial. Eles permanecem como evidência do estado existente no momento em que foram criados.

## 11. Critérios de conformidade

Um documento atende a este padrão quando:

- nenhuma sigla essencial aparece sem explicação na primeira menção;
- nenhum título depende exclusivamente de um identificador;
- estados técnicos possuem explicação em português;
- códigos permanecem disponíveis para rastreabilidade;
- a leitura principal é possível sem consultar um glossário externo;
- termos comerciais, como validade do preço, possuem significado explícito.
