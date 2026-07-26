---
id: UXA-009
title: Diretriz de Linguagem Clara e Rótulos Completos
status: draft
version: 0.1.0
owner: Guivos Experience Architecture
last_updated: 2026-07-26
parent: UXA-000
related:
  - UXA-001
  - UXA-005
  - UXA-006
  - UXA-007
  - UXA-008
normative: false
---

# UXA-009 — Diretriz de Linguagem Clara e Rótulos Completos

## 1. Finalidade

Esta diretriz estabelece que a experiência da Guivos deve ser compreensível sem exigir que a pessoa conheça siglas, códigos internos, nomes técnicos ou expressões abreviadas.

A regra se aplica a:

- telas e wireframes;
- notificações;
- mensagens de orientação;
- cartões e detalhes;
- formulários;
- textos de ajuda;
- apresentações e respostas de acompanhamento;
- documentos públicos ou destinados a participantes não técnicos.

## 2. Regra principal

Todo conceito deverá ser apresentado por extenso na primeira ocorrência.

Uma sigla ou identificador técnico poderá aparecer depois do nome completo somente quando:

1. for necessário para rastreabilidade;
2. voltar a ser utilizado no mesmo contexto;
3. não competir com a compreensão da mensagem;
4. estiver claramente identificado como referência técnica.

Exemplo adequado:

> Arquitetura da Experiência da Guivos — referência técnica UXA-000.

Exemplo inadequado:

> UXA-000 ativo; próximo gate UXA-005.

## 3. Regras para textos visíveis na interface

A interface destinada ao participante deverá:

- usar palavras completas;
- evitar códigos internos;
- evitar siglas não explicadas;
- evitar títulos cortados;
- evitar palavras reduzidas apenas para caber no espaço;
- quebrar o texto em linhas quando necessário;
- ajustar o espaço do componente antes de reduzir a clareza;
- mostrar datas, preços, prazos e condições de forma completa;
- preservar acesso ao conteúdo integral quando houver limitação real de espaço.

## 4. Truncamento

Rótulos de ação, nomes de etapas, condições comerciais, alertas, preços e prazos não poderão ser truncados.

Reticências poderão ser utilizadas somente para conteúdo extenso produzido por terceiros, como descrições ou comentários, desde que exista uma ação clara para abrir o texto completo.

Não deverão ser truncados:

- nome da ação principal;
- nome da etapa;
- validade do preço;
- custo total;
- condição de cancelamento;
- requisito de elegibilidade;
- razão de relevância;
- alerta de risco ou privacidade;
- identidade da Organização ou do Coletivo.

## 5. Datas, horários e valores

Sempre que a precisão for material, a interface deverá preferir:

- `31 de julho de 2026` em vez de `31/07`;
- `às 19 horas` em vez de `19h`, quando houver espaço;
- `R$ 79,90 por mês` em vez de `R$ 79,90/mês`;
- `custo total estimado de R$ 479,40` em vez de apresentar apenas o valor recorrente.

Formatos compactos poderão existir em calendários, tabelas ou espaços reduzidos, desde que o formato completo esteja disponível no detalhe.

## 6. Nomes geográficos e institucionais

Nomes reduzidos, como siglas de cidades, estados, órgãos ou programas, deverão ser apresentados por extenso na primeira ocorrência.

Exemplo:

> Coletivo Belo Horizonte Mais Verde.

A forma reduzida poderá ser utilizada posteriormente quando for conhecida, necessária e não ambígua.

## 7. Documentação técnica

Códigos como `UXA-009`, números de solicitações de integração e versões continuarão existindo para governança do repositório.

Nas respostas e apresentações, eles deverão aparecer como informação secundária, após a explicação humana do que representam.

## 8. Critérios de revisão

Antes de aprovar uma tela, verificar:

1. a pessoa entende o conteúdo sem consultar glossário?;
2. todas as ações estão escritas por completo?;
3. algum texto está visualmente cortado?;
4. datas, valores e validades estão claros?;
5. siglas foram explicadas na primeira ocorrência?;
6. códigos internos estão fora da superfície principal?;
7. o texto completo continua acessível em telas menores?;
8. a linguagem descreve o que acontecerá após cada ação?

## 9. Aplicação imediata

Esta diretriz orienta a correção dos três wireframes iniciais:

- tela Hoje;
- detalhe da oportunidade;
- cadastro de oportunidade pela Organização.

Ela não altera a estrutura funcional aprovada para revisão e não autoriza design visual final, protótipo navegável ou desenvolvimento.