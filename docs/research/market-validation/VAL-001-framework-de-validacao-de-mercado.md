---
id: VAL-001
title: Framework de Validação de Mercado da Guivos
status: active
version: 1.2.1
owner: Guivos
last_updated: 2026-07-12
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

Estabelecer o método oficial para validar hipóteses de mercado da Guivos antes de decisões relevantes de produto, posicionamento, experiência, adoção, recorrência e monetização.

A validação deverá respeitar o grau de conhecimento que o participante possui sobre a Guivos em cada etapa. A primeira pesquisa conceitual não deverá exigir previsões sobre confiança operacional, frequência de uso, retenção ou recomendação de um produto ainda não experimentado.

## 2. Princípio da Evidência de Mercado

> Nenhuma decisão estratégica de produto será considerada definitiva apenas por consenso interno. Sempre que possível, deverá ser confrontada com evidências obtidas por pesquisa, experimentação ou comportamento real dos participantes.

## 3. Princípio da Co-criação

> A Guivos será construída com base em evidências e na participação das pessoas. A validação não existe para confirmar hipóteses internas, mas para revelar o que faz sentido, o que não faz e o que precisa ser ajustado.

A pesquisa também é uma experiência de marca. Ela deve representar a Guivos com clareza, simplicidade, respeito, transparência e ausência de pressão comercial.

## 4. Princípio da Avaliabilidade

> Uma pergunta somente deverá integrar uma rodada quando o participante possuir informação suficiente para avaliá-la de forma minimamente consciente.

Dimensões dependentes de experiência real — como confiança operacional, recorrência, retenção, satisfação e recomendação — deverão ser priorizadas em protótipos, testes controlados, beta ou produto em uso.

## 5. Escopo da fase inicial

A primeira rodada valida exclusivamente a proposta B2C da Guivos.

Serão avaliados:

1. descoberta tardia de oportunidades potencialmente úteis;
2. ausência de oportunidades adequadas ao momento do participante;
3. esforço atual de busca;
4. clareza da proposta;
5. relevância para a área da vida escolhida;
6. situação prática de primeiro uso;
7. expectativas sobre o que encontrar ou fazer na plataforma;
8. resultado concreto considerado valioso;
9. contribuição percebida para os próximos 12 meses;
10. intenção de experimentar uma primeira versão;
11. interesse em participar de uma primeira experiência;
12. sinais iniciais de monetização;
13. barreiras e diferenças entre segmentos.

Esta rodada não valida produto em uso, confiança operacional comprovada, recorrência, retenção, receita real, usabilidade, arquitetura técnica ou adequação jurídica definitiva.

## 6. Hipóteses centrais

| ID | Hipótese |
|---|---|
| H1 | Pessoas descobrem tarde demais oportunidades que poderiam contribuir para seus objetivos. |
| H2 | Pessoas procuram possibilidades, mas frequentemente não encontram oportunidades compatíveis com seu momento, disponibilidade, localização, recursos ou necessidades. |
| H3 | Uma plataforma que compreenda o momento atual e ajude a identificar próximos passos e oportunidades contextualizadas gera valor percebido. |
| H4 | A proposta pode ser compreendida sem explicação longa, técnica ou promocional. |
| H5 | As pessoas conseguem reconhecer situações concretas em que procurariam a Guivos pela primeira vez. |
| H6 | Próximos Passos, oportunidades contextualizadas e acompanhamento da evolução são percebidos como mais valiosos que listas ou catálogos genéricos. |
| H7 | A Guivos apresenta potencial de contribuição concreta para uma área prioritária da vida do participante. |
| H8 | Uma parcela relevante pretende experimentar uma primeira versão e aceita participar de uma experiência inicial. |
| H9 | Existe potencial de monetização condicionado à demonstração de resultados reais, sem bloquear o valor essencial da experiência gratuita. |

## 7. Método em quatro etapas

### 7.1 Pré-teste

Aplicar o VAL-002 com 10 a 15 pessoas para identificar:

- confusão;
- duração excessiva;
- abandono;
- perguntas enviesadas;
- falhas na numeração ou lógica;
- dificuldade de compreensão;
- opções ausentes ou redundantes.

O pré-teste valida o instrumento, não a aceitação da Guivos.

### 7.2 Entrevistas qualitativas

Realizar inicialmente 20 a 30 entrevistas semiestruturadas, ampliando até saturação dos padrões.

As entrevistas deverão seguir o VAL-003 e registrar sinais comportamentais conforme o VAL-008.

### 7.3 Questionário quantitativo

Aplicar o VAL-002 a:

- mínimo de 200 respostas válidas para decisão inicial;
- meta preferencial de 500 respostas válidas para maior estabilidade e segmentação.

A composição da amostra deverá seguir o VAL-005.

### 7.4 Evidência comportamental

Validar posteriormente por:

- landing page;
- lista de espera;
- conversão em contato;
- participação efetiva em primeira experiência ou beta;
- MVP concierge;
- testes de consentimento e controle;
- uso e retenção reais;
- comportamento de pagamento.

Evidência comportamental pode confirmar ou contrariar intenção declarada.

## 8. Instrumento oficial

O instrumento oficial da primeira rodada é:

- **Documento interno:** `VAL-002 — Pesquisa Conceitual B2C da Guivos`;
- **Título público:** `Construindo a Guivos`;
- **Tempo estimado:** 5 a 7 minutos;
- **Perguntas principais:** 22;
- **Perguntas abertas centrais:** 2 (`Q12` obrigatória e `Q22` opcional);
- **Codificação:** pergunta `n`, alternativa `n.x`;
- **Contato:** opcional, condicional e excluído dos KPIs.

## 9. Ordem lógica da pesquisa

```mermaid
flowchart LR
    A["Perfil mínimo"] --> B["Área e resultado desejado"] --> C["Dificuldades, descoberta tardia e adequação"] --> D["Apresentação da Guivos"] --> E["Compreensão"] --> F["Aplicação prática"] --> G["Valor e contribuição"] --> H["Intenção e primeira experiência"] --> I["Barreiras e monetização"] --> J["Feedback final"]
```

Perguntas sobre valor, intenção e pagamento não devem preceder a apresentação oficial da proposta.

## 10. Indicadores oficiais

| Indicador | Fonte | Meta inicial |
|---|---|---:|
| Índice de Fricção de Oportunidades — IFO | Q8 + Q9 | >= 65% |
| Esforço atual | Q10 | >= 6,0/10 indica problema relevante |
| Compreensão autodeclarada | Q11 | >= 8,0/10 |
| Compreensão correta | Q12 | >= 80% |
| Relevância contextual | Q13 | >= 8,0/10 |
| Contribuição percebida | Q17 | >= 8,0/10 |
| Intenção positiva de experimentar | Q18 | >= 60% |
| Interesse confirmado na primeira experiência | Q19 | >= 35% |
| Disposição para pagar | Q21 | Diagnóstico; não gate isolado |

O IFO combina dois componentes observáveis: descoberta tardia de oportunidades potencialmente úteis (`Q8`) e ausência de oportunidades adequadas após busca (`Q9`). As bases válidas de cada componente deverão ser exibidas separadamente.

Situação de primeiro uso (`Q14`), expectativas sobre a plataforma (`Q15`), resultado concreto de valor (`Q16`) e barreira principal (`Q20`) são indicadores diagnósticos e orientam posicionamento, escopo inicial e desenho do MVP.

As fórmulas, segmentações e regras de exibição estão no VAL-006.

## 11. Critérios de decisão

Os resultados serão classificados como:

- `Go`;
- `Go com ajustes`;
- `Pivot parcial`;
- `No-Go temporário`.

Nenhuma decisão formal poderá ser emitida apenas por média geral ou por um único indicador. A decisão deverá seguir os gates e regras combinadas do VAL-007.

## 12. Princípios de qualidade

- não vender durante a pesquisa;
- não sugerir que existe resposta desejada;
- explicar o suficiente para permitir compreensão real;
- utilizar linguagem acessível;
- manter o formulário curto;
- limitar perguntas abertas ao essencial;
- separar comportamento passado de intenção futura;
- medir somente situações que o participante possa reconhecer ou recordar;
- distinguir ausência de busca de ausência de oportunidade adequada;
- conectar perguntas de valor à área e ao resultado declarados pelo participante;
- não exigir avaliação de aspectos operacionais ainda não demonstrados;
- preservar respostas negativas e objeções;
- não tratar intenção declarada como adoção comprovada;
- não tratar contribuição percebida como transformação real;
- não tratar intenção de pagar como receita comprovada;
- analisar segmentos separadamente;
- registrar origem, limitações e possíveis vieses da amostra;
- excluir perguntas que não influenciem decisões futuras.

## 13. Saídas obrigatórias de cada rodada

1. base bruta preservada;
2. base tratada com critérios de exclusão;
3. dashboard conforme VAL-006;
4. análise qualitativa conforme VAL-004;
5. hipóteses validadas, parciais ou rejeitadas;
6. segmentos de maior e menor aderência;
7. leitura separada de descoberta tardia e lacuna de adequação;
8. situações de primeiro uso prioritárias;
9. resultados concretos mais valorizados;
10. evidências favoráveis e contrárias;
11. decisão conforme VAL-007;
12. recomendações de ajuste;
13. limitações;
14. plano da próxima rodada.

## 14. Limites

Este framework não substitui:

- pesquisa estatística representativa nacional;
- teste de usabilidade;
- validação jurídica;
- análise financeira;
- validação técnica;
- teste de produto em uso real;
- medição de confiança operacional;
- medição de recorrência e retenção;
- comprovação de receita ou Product-Market Fit.

## 15. Regra de evolução

Qualquer alteração em pergunta, alternativa, cálculo, meta ou critério de decisão deverá:

1. ser versionada;
2. registrar o motivo;
3. preservar comparabilidade quando possível;
4. indicar impactos sobre rodadas anteriores;
5. atualizar conjuntamente VAL-002, VAL-006 e VAL-007 quando houver dependência.