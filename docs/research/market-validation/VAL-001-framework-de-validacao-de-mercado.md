---
id: VAL-001
title: Framework de Validação de Mercado da Guivos
status: active
version: 1.1.0
owner: Guivos
last_updated: 2026-07-11
related:
  - VAL-002
  - VAL-003
  - VAL-004
  - VAL-005
  - VAL-006
  - VAL-007
  - VAL-008
---

# VAL-001 — Framework de Validação de Mercado da Guivos

## 1. Finalidade

Estabelecer o método oficial para validar hipóteses de mercado da Guivos antes de decisões relevantes de produto, posicionamento, experiência, confiança, recorrência e monetização.

## 2. Princípio da Evidência de Mercado

> Nenhuma decisão estratégica de produto será considerada definitiva apenas por consenso interno. Sempre que possível, deverá ser confrontada com evidências obtidas por pesquisa, experimentação ou comportamento real dos participantes.

## 3. Princípio da Co-criação

> A Guivos será construída com base em evidências e na participação das pessoas. A validação não existe para confirmar hipóteses internas, mas para revelar o que faz sentido, o que não faz e o que precisa ser ajustado.

A pesquisa também é uma experiência de marca. Ela deve representar a Guivos com clareza, simplicidade, respeito, transparência e ausência de pressão comercial.

## 4. Escopo da fase inicial

A primeira rodada valida exclusivamente a proposta B2C da Guivos.

Serão avaliados:

1. existência e intensidade da dor;
2. clareza da proposta;
3. relevância percebida;
4. potencial de transformação percebida;
5. confiança para compartilhar contexto;
6. intenção de uso;
7. potencial de recorrência;
8. interesse em participar de beta;
9. disposição inicial para pagar;
10. barreiras e diferenças entre segmentos.

Esta rodada não valida produto em uso, retenção real, receita real, usabilidade, arquitetura técnica ou adequação jurídica definitiva.

## 5. Hipóteses centrais

| ID | Hipótese |
|---|---|
| H1 | Pessoas perdem oportunidades relevantes porque elas estão fragmentadas, chegam fora do momento adequado ou não são reconhecidas como úteis. |
| H2 | Uma plataforma que compreenda o momento atual e ajude a identificar próximos passos e oportunidades contextualizadas gera valor percebido. |
| H3 | A proposta pode ser compreendida sem explicação longa, técnica ou promocional. |
| H4 | Participantes compartilham contexto quando finalidade, controle, segurança e privacidade são claros. |
| H5 | Próximos Passos e oportunidades contextualizadas são mais valiosos que listas ou catálogos genéricos. |
| H6 | Existe motivo real para retorno recorrente. |
| H7 | Uma parcela relevante aceita participar de teste beta antes do lançamento. |
| H8 | Existe potencial de monetização sem bloquear o valor essencial da experiência gratuita. |

## 6. Método em quatro etapas

### 6.1 Pré-teste

Aplicar o VAL-002 com 10 a 15 pessoas para identificar:

- confusão;
- duração excessiva;
- abandono;
- perguntas enviesadas;
- falhas na numeração ou lógica;
- dificuldade de compreensão;
- opções ausentes ou redundantes.

O pré-teste valida o instrumento, não a aceitação da Guivos.

### 6.2 Entrevistas qualitativas

Realizar inicialmente 20 a 30 entrevistas semiestruturadas, ampliando até saturação dos padrões.

As entrevistas deverão seguir o VAL-003 e registrar sinais comportamentais conforme o VAL-008.

### 6.3 Questionário quantitativo

Aplicar o VAL-002 a:

- mínimo de 200 respostas válidas para decisão inicial;
- meta preferencial de 500 respostas válidas para maior estabilidade e segmentação.

A composição da amostra deverá seguir o VAL-005.

### 6.4 Evidência comportamental

Validar posteriormente por:

- landing page;
- lista de espera;
- conversão em contato;
- participação efetiva no beta;
- MVP concierge;
- uso e retenção reais;
- comportamento de pagamento.

Evidência comportamental pode confirmar ou contrariar intenção declarada.

## 7. Instrumento oficial

O instrumento oficial da primeira rodada é:

- **Documento interno:** `VAL-002 — Pesquisa Conceitual B2C da Guivos`;
- **Título público:** `Construindo a Guivos`;
- **Tempo estimado:** 5 a 7 minutos;
- **Perguntas principais:** 23;
- **Perguntas abertas centrais:** 2 (`Q10` obrigatória e `Q23` opcional);
- **Codificação:** pergunta `n`, alternativa `n.x`;
- **Contato:** opcional, condicional e excluído dos KPIs.

## 8. Ordem lógica da pesquisa

```mermaid
flowchart LR
    A["Perfil mínimo"] --> B["Momento atual"] --> C["Dor e comportamento"] --> D["Apresentação da Guivos"] --> E["Compreensão"] --> F["Valor percebido"] --> G["Confiança"] --> H["Uso e recorrência"] --> I["Beta e monetização"] --> J["Barreiras e feedback"]
```

Perguntas sobre valor, uso e pagamento não devem preceder a apresentação oficial da proposta.

## 9. Indicadores oficiais

| Indicador | Fonte | Meta inicial |
|---|---|---:|
| Dor relevante | Q6 | >= 65% |
| Esforço atual | Q7 | >= 6,0/10 indica problema relevante |
| Compreensão autodeclarada | Q9 | >= 8,0/10 |
| Compreensão correta | Q10 | >= 80% |
| Relevância percebida | Q11 | >= 8,0/10 |
| ITP — Índice de Transformação Percebida | Q13 | >= 8,0/10 |
| Confiança | Q14 | >= 7,0/10 |
| Intenção positiva de uso | Q16 | >= 60% |
| Uso recorrente esperado | Q18 | >= 50% |
| NPS conceitual | Q19 | >= 40 |
| Interesse confirmado no beta | Q20 | >= 35% |
| Disposição para pagar | Q21 | Diagnóstico; não gate isolado |

As fórmulas, segmentações e regras de exibição estão no VAL-006.

## 10. Critérios de decisão

Os resultados serão classificados como:

- `Go`;
- `Go com ajustes`;
- `Pivot parcial`;
- `No-Go temporário`.

Nenhuma decisão formal poderá ser emitida apenas por média geral ou por um único indicador. A decisão deverá seguir os gates e regras combinadas do VAL-007.

## 11. Princípios de qualidade

- não vender durante a pesquisa;
- não sugerir que existe resposta desejada;
- explicar o suficiente para permitir compreensão real;
- utilizar linguagem acessível;
- manter o formulário curto;
- limitar perguntas abertas ao essencial;
- separar comportamento passado de intenção futura;
- preservar respostas negativas e objeções;
- não tratar intenção declarada como adoção comprovada;
- não tratar intenção de pagar como receita comprovada;
- analisar segmentos separadamente;
- registrar origem, limitações e possíveis vieses da amostra;
- excluir perguntas que não influenciem decisões futuras.

## 12. Saídas obrigatórias de cada rodada

1. base bruta preservada;
2. base tratada com critérios de exclusão;
3. dashboard conforme VAL-006;
4. análise qualitativa conforme VAL-004;
5. hipóteses validadas, parciais ou rejeitadas;
6. segmentos de maior e menor aderência;
7. evidências favoráveis e contrárias;
8. decisão conforme VAL-007;
9. recomendações de ajuste;
10. limitações;
11. plano da próxima rodada.

## 13. Limites

Este framework não substitui:

- pesquisa estatística representativa nacional;
- teste de usabilidade;
- validação jurídica;
- análise financeira;
- validação técnica;
- teste de produto em uso real;
- medição de retenção;
- comprovação de receita ou Product-Market Fit.

## 14. Regra de evolução

Qualquer alteração em pergunta, alternativa, cálculo, meta ou critério de decisão deverá:

1. ser versionada;
2. registrar o motivo;
3. preservar comparabilidade quando possível;
4. indicar impactos sobre rodadas anteriores;
5. atualizar conjuntamente VAL-002, VAL-006 e VAL-007 quando houver dependência.