---
id: VAL-006
title: Dashboard de Indicadores de Validação
status: active
version: 1.2.0
owner: Guivos
last_updated: 2026-07-12
related:
  - VAL-001
  - VAL-002
  - VAL-004
  - VAL-005
  - VAL-007
---

# VAL-006 — Dashboard de Indicadores de Validação

## 1. Objetivo

Definir o painel executivo utilizado quando houver uma base suficiente de respostas da Pesquisa Conceitual B2C da Guivos.

O dashboard deverá:

- medir os KPIs oficiais da versão vigente do instrumento;
- comparar resultados com metas explícitas;
- identificar divergências entre segmentos;
- verificar qualidade e estabilidade da amostra;
- apoiar a decisão `Go`, `Go com ajustes`, `Pivot parcial` ou `No-Go temporário`;
- preservar rastreabilidade entre cada indicador e a pergunta que o originou;
- diferenciar percepção conceitual de evidência comportamental.

## 2. Níveis de maturidade da base

| Respostas válidas | Classificação | Uso permitido |
|---:|---|---|
| 10 a 15 | Pré-teste | Revisar clareza, duração, lógica e abandono. Não decidir aceitação de mercado. |
| 16 a 49 | Exploratória | Identificar sinais e problemas evidentes. Não emitir decisão formal. |
| 50 a 199 | Indicativa | Analisar tendências preliminares e segmentos, com cautela. |
| 200 a 499 | Base de decisão inicial | Permite decisão inicial, desde que a amostra tenha diversidade mínima e não apresente concentração crítica não tratada. |
| 500 ou mais | Base preferencial | Permite decisão mais robusta e análises segmentadas mais confiáveis. |

A quantidade de respostas, por si só, não torna a amostra estatisticamente representativa da população brasileira. O painel sempre deverá exibir composição, origem e limitações da amostra.

## 3. Regras de validade da resposta

Uma resposta será considerada válida quando:

1. tiver sido concluída;
2. estiver vinculada à versão do instrumento utilizada;
3. não apresentar padrão evidente de preenchimento aleatório ou automatizado;
4. possuir tempo de resposta plausível;
5. contiver resposta utilizável na pergunta aberta de compreensão (`Q11`);
6. não for duplicação confirmada;
7. respeitar o público da rodada analisada.

O dashboard deverá exibir:

- respostas recebidas;
- respostas concluídas;
- respostas válidas;
- respostas excluídas;
- taxa de conclusão;
- taxa de abandono;
- tempo mediano de preenchimento;
- versão do instrumento;
- motivo das exclusões.

## 4. Dicionário oficial de KPIs

### 4.1 Dor relevante

**Pergunta:** `Q8`

```text
Dor relevante (%) = respostas 8.3 + 8.4 + 8.5 / respostas válidas da Q8 × 100
```

**Meta inicial:** `>= 65%`.

Indicador complementar:

```text
Dor alta (%) = respostas 8.4 + 8.5 / respostas válidas da Q8 × 100
```

### 4.2 Esforço atual

**Pergunta:** `Q9`

**Cálculo:** média e mediana da escala de 0 a 10.

**Sinal de problema relevante:** média `>= 6,0`.

Exibir também percentual de notas 8 a 10, distribuição completa e comparação por intensidade da dor.

### 4.3 Compreensão autodeclarada

**Pergunta:** `Q10`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

### 4.4 Compreensão correta

**Pergunta:** `Q11`

Cada resposta deverá ser classificada como:

- **1,0 — correta:** reconhece que a Guivos considera o momento, contexto ou objetivo da pessoa e ajuda a organizar caminhos, identificar próximos passos ou encontrar oportunidades relevantes para sua evolução;
- **0,5 — parcialmente correta:** reconhece apenas um elemento central ou apresenta compreensão incompleta;
- **0,0 — incorreta:** descreve a Guivos como catálogo genérico, rede social, marketplace isolado, sistema que decide pela pessoa ou outro conceito incompatível.

```text
Compreensão correta (%) = respostas classificadas como 1,0 / respostas válidas da Q11 × 100
```

**Meta inicial:** `>= 80%`.

Exibir separadamente compreensão correta, parcial e incorreta.

### 4.5 Relevância contextual

**Pergunta:** `Q12`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

A leitura deverá ser vinculada à área de evolução selecionada na `Q4`.

### 4.6 Contribuição percebida

**Pergunta:** `Q16`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

Este indicador mede a crença de que a Guivos poderia contribuir para o avanço na área escolhida nos próximos 12 meses. Não mede transformação real.

### 4.7 Intenção positiva de experimentar

**Pergunta:** `Q17`

```text
Intenção positiva (%) = respostas 17.4 + 17.5 / respostas válidas da Q17 × 100
```

**Meta inicial:** `>= 60%`.

Exibir também intenção negativa (`17.1 + 17.2`) e indecisão (`17.3`).

### 4.8 Interesse confirmado na primeira experiência

**Pergunta:** `Q18`

```text
Interesse confirmado (%) = respostas 18.1 / respostas válidas da Q18 × 100
```

**Meta inicial:** `>= 35%`.

Exibir também interesse ampliado (`18.1 + 18.2`) e conversão efetiva em contato.

## 5. Indicadores diagnósticos

### 5.1 Área prioritária

**Pergunta:** `Q4`

Exibir ranking e percentual por área da vida.

### 5.2 Resultado desejado

**Pergunta:** `Q5`

Exibir ranking geral e cruzamento com a área escolhida.

### 5.3 Dificuldades atuais

**Pergunta:** `Q6`

Exibir frequência de cada dificuldade, quantidade média selecionada e combinações recorrentes.

### 5.4 Comportamento atual de busca

**Pergunta:** `Q7`

Exibir canais, estratégias utilizadas e percentual de pessoas que tentam descobrir caminhos sem estrutura ou não procuram ativamente.

### 5.5 Situação de primeiro uso

**Pergunta:** `Q13`

Exibir ranking e percentual por situação, destacando:

- falta de clareza sobre o próximo passo;
- dificuldade para encontrar oportunidade;
- mudança de vida;
- descoberta de novas possibilidades;
- excesso de opções;
- organização e acompanhamento;
- conexão com pessoas ou organizações;
- uso apenas por necessidade específica;
- incapacidade de imaginar uso.

### 5.6 Expectativas sobre a plataforma

**Pergunta:** `Q14`

Exibir ranking, percentual e combinações mais frequentes das opções selecionadas.

### 5.7 Resultado concreto de valor

**Pergunta:** `Q15`

Exibir ranking e percentual do principal resultado considerado útil.

### 5.8 Barreiras principais

**Pergunta:** `Q19`

Exibir ranking e percentual de cada barreira, destacando:

- ausência de necessidade;
- proposta genérica ou incompreendida;
- dúvida sobre adequação das oportunidades;
- dúvida sobre capacidade de compreensão do momento;
- preocupação com informações pessoais;
- suficiência de soluções atuais;
- falta de tempo ou interesse;
- resistência ao acompanhamento;
- preço.

### 5.9 Disposição inicial para pagar

**Pergunta:** `Q20`

Exibir:

- não consideraria pagar (`20.1`);
- pagamento condicionado a resultado (`20.2`);
- percentual por faixa de preço (`20.3` a `20.6`);
- avaliação prematura (`20.7`);
- recusa em responder (`20.8`).

Monetização é indicador diagnóstico e não gate isolado na primeira rodada.

## 6. Índice Geral de Validação — IGV

O IGV é uma síntese executiva. Não substitui a leitura por hipótese nem pode aprovar a proposta sozinho.

### 6.1 Normalização

- percentuais permanecem na escala de 0 a 100;
- médias de 0 a 10 são multiplicadas por 10;
- valores são limitados ao intervalo de 0 a 100.

### 6.2 Pesos

| Dimensão | Indicador | Peso |
|---|---|---:|
| Problema | Dor relevante (`Q8`) | 15% |
| Compreensão | Compreensão correta (`Q11`) | 20% |
| Relevância | Média da `Q12` | 20% |
| Contribuição | Média da `Q16` | 20% |
| Intenção | Intenção positiva (`Q17`) | 20% |
| Primeira experiência | Interesse confirmado (`Q18`) | 5% |

```text
IGV = soma dos indicadores normalizados × respectivos pesos
```

Esforço, compreensão autodeclarada, monetização e indicadores diagnósticos permanecem fora do IGV.

### 6.3 Leitura do IGV

| IGV | Leitura executiva |
|---:|---|
| 80 a 100 | Aceitação geral forte, sujeita aos gates críticos. |
| 70 a 79,9 | Aceitação promissora com ajustes identificáveis. |
| 55 a 69,9 | Validação parcial; exige revisão relevante e nova rodada. |
| Abaixo de 55 | Evidência insuficiente ou baixa aderência na rodada. |

## 7. Gates críticos

Mesmo com IGV alto, uma decisão `Go` não poderá ser emitida quando houver:

- compreensão correta abaixo de 65%;
- dor relevante abaixo de 50%;
- relevância contextual abaixo de 7,0;
- contribuição percebida abaixo de 7,0;
- intenção positiva de experimentar abaixo de 45%;
- base inferior a 200 respostas válidas;
- concentração crítica da amostra sem análise segmentada;
- indícios relevantes de viés, duplicidade ou baixa qualidade.

Confiança operacional, recorrência, retenção e recomendação não integram os gates desta rodada porque dependem de experiência real com o produto.

## 8. Estrutura mínima do dashboard

### 8.1 Cabeçalho executivo

- rodada e período de coleta;
- versão do instrumento;
- total recebido, concluído e válido;
- nível de maturidade da base;
- IGV;
- decisão preliminar;
- gates atendidos;
- principal força;
- principal risco.

### 8.2 Qualidade da amostra

- taxa de conclusão;
- taxa de abandono;
- tempo mediano;
- distribuição por idade, estado ou Distrito Federal e situação principal;
- consolidação dos estados por região, quando útil;
- concentração por canal de aquisição;
- concentração geográfica;
- exclusões e motivos.

### 8.3 Problema e comportamento atual

- área prioritária (`Q4`);
- resultado desejado (`Q5`);
- dificuldades (`Q6`);
- comportamento de busca (`Q7`);
- dor relevante e dor alta (`Q8`);
- esforço médio e mediano (`Q9`).

### 8.4 Compreensão

- compreensão autodeclarada (`Q10`);
- compreensão correta, parcial e incorreta (`Q11`);
- principais padrões de compreensão e confusão.

### 8.5 Aplicação prática e valor

- relevância contextual (`Q12`);
- situações de primeiro uso (`Q13`);
- expectativas sobre a plataforma (`Q14`);
- resultados concretos valorizados (`Q15`);
- contribuição percebida (`Q16`).

### 8.6 Intenção e primeira experiência

- intenção positiva de experimentar (`Q17`);
- interesse confirmado e ampliado (`Q18`);
- conversão em contato opcional.

### 8.7 Barreiras e monetização

- ranking das barreiras (`Q19`);
- barreiras por segmento;
- disposição para pagar (`Q20`);
- faixas de preço;
- comentários opcionais da `Q21`.

## 9. Segmentações mínimas

Os KPIs principais deverão permitir corte por:

- faixa etária (`Q1`);
- estado ou Distrito Federal (`Q2`);
- região derivada do estado (`Q2`);
- situação principal (`Q3`);
- área prioritária (`Q4`);
- resultado desejado (`Q5`);
- intensidade da dor (`Q8`);
- situação de primeiro uso (`Q13`);
- intenção de experimentar (`Q17`);
- interesse em primeira experiência (`Q18`);
- barreira principal (`Q19`).

Participantes fora do Brasil deverão ser analisados separadamente da base nacional.

Estados com menos de 30 respostas deverão ser destacados como base reduzida e não deverão receber conclusão isolada. O painel deverá identificar concentração excessiva em São Paulo, Minas Gerais ou qualquer outra unidade federativa.

## 10. Semáforo dos indicadores

- **Verde:** atingiu a meta de `Go` definida no VAL-007;
- **Amarelo:** está na faixa de `Go com ajustes`;
- **Vermelho:** está na faixa de `Pivot parcial / No-Go temporário`;
- **Cinza:** base insuficiente ou indicador ainda não calculável.

## 11. Saída executiva obrigatória

Cada atualização do dashboard deverá produzir:

1. fotografia da amostra;
2. resultados dos KPIs;
3. semáforo por dimensão;
4. IGV;
5. gates críticos;
6. áreas, resultados desejados e situações de primeiro uso prioritários;
7. leitura por segmento e por estado quando houver base suficiente;
8. evidências favoráveis e contrárias;
9. decisão preliminar conforme VAL-007;
10. recomendações de ajuste;
11. limitações e próxima ação.

## 12. Regra de comparabilidade

Resultados produzidos por versões anteriores do VAL-002 não deverão ser combinados diretamente com a versão `1.2.0`. Qualquer comparação histórica deverá utilizar mapeamento explícito de perguntas, alternativas e fórmulas.
