---
id: VAL-006
title: Dashboard de Indicadores de Validação
status: active
version: 1.1.1
owner: Guivos
last_updated: 2026-07-11
related:
  - VAL-001
  - VAL-002
  - VAL-004
  - VAL-005
  - VAL-007
---

# VAL-006 — Dashboard de Indicadores de Validação

## 1. Objetivo

Definir o painel executivo que será utilizado assim que houver uma base suficiente de respostas da Pesquisa Conceitual B2C da Guivos.

O dashboard deverá:

- medir os KPIs oficiais;
- comparar resultados com as metas;
- identificar divergências entre segmentos;
- verificar qualidade e estabilidade da amostra;
- apoiar a decisão `Go`, `Go com ajustes`, `Pivot parcial` ou `No-Go temporário`;
- preservar rastreabilidade entre cada indicador e a pergunta que o originou.

## 2. Níveis de maturidade da base

| Respostas válidas | Classificação | Uso permitido |
|---:|---|---|
| 10 a 15 | Pré-teste | Revisar clareza, duração, lógica e abandono. Não decidir aceitação de mercado. |
| 16 a 49 | Exploratória | Identificar sinais e problemas evidentes. Não emitir decisão formal. |
| 50 a 199 | Indicativa | Analisar tendências preliminares e segmentos, com cautela. |
| 200 a 499 | Base de decisão inicial | Permite decisão inicial, desde que a amostra tenha diversidade mínima e não apresente concentração crítica. |
| 500 ou mais | Base preferencial | Permite decisão mais robusta e análises segmentadas mais confiáveis. |

A quantidade de respostas, por si só, não torna a amostra estatisticamente representativa da população brasileira. O painel sempre deverá exibir composição, origem e limitações da amostra.

## 3. Regras de validade da resposta

Uma resposta será considerada válida quando:

1. tiver sido concluída;
2. não apresentar padrão evidente de preenchimento aleatório ou automatizado;
3. possuir tempo de resposta plausível;
4. contiver resposta utilizável na pergunta aberta de compreensão (`Q10`);
5. não for duplicação confirmada;
6. respeitar o público da rodada analisada.

O dashboard deverá exibir:

- respostas recebidas;
- respostas concluídas;
- respostas válidas;
- respostas excluídas;
- taxa de conclusão;
- taxa de abandono;
- tempo mediano de preenchimento;
- motivo das exclusões.

## 4. Dicionário oficial de KPIs

### 4.1 Dor relevante

**Pergunta:** `Q6`

```text
Dor relevante (%) = respostas 6.3 + 6.4 + 6.5 / respostas válidas da Q6 × 100
```

**Meta inicial:** `>= 65%`.

Indicador complementar:

```text
Dor alta (%) = respostas 6.4 + 6.5 / respostas válidas da Q6 × 100
```

### 4.2 Esforço atual

**Pergunta:** `Q7`

**Cálculo:** média e mediana da escala de 0 a 10.

**Sinal de problema relevante:** média `>= 6,0`.

Exibir também percentual de notas 8 a 10, distribuição completa e comparação por intensidade da dor.

### 4.3 Compreensão autodeclarada

**Pergunta:** `Q9`

**Cálculo:** média da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

### 4.4 Compreensão correta

**Pergunta:** `Q10`

Cada resposta deverá ser classificada como:

- **1,0 — correta:** reconhece que a Guivos considera o contexto ou momento da pessoa e ajuda a identificar próximos passos, oportunidades ou caminhos para evolução;
- **0,5 — parcialmente correta:** reconhece apenas um elemento central ou apresenta compreensão incompleta;
- **0,0 — incorreta:** descreve a Guivos como catálogo genérico, rede social, marketplace isolado, sistema que decide pela pessoa ou outro conceito incompatível.

```text
Compreensão correta (%) = respostas classificadas como 1,0 / respostas válidas da Q10 × 100
```

**Meta inicial:** `>= 80%`.

Exibir separadamente compreensão correta, parcial e incorreta.

### 4.5 Relevância percebida

**Pergunta:** `Q11`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

### 4.6 Índice de Transformação Percebida — ITP

**Pergunta:** `Q13`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

O ITP mede a crença de que a proposta poderia gerar melhoria concreta em alguma área da vida nos próximos 12 meses. Não mede transformação real.

### 4.7 Confiança para compartilhar contexto

**Pergunta:** `Q14`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 7,0`.

Exibir também percentual de notas 0 a 5, fatores de confiança da `Q15` e relação entre confiança e intenção de uso.

### 4.8 Intenção positiva de uso

**Pergunta:** `Q16`

```text
Intenção positiva (%) = respostas 16.4 + 16.5 / respostas válidas da Q16 × 100
```

**Meta inicial:** `>= 60%`.

### 4.9 Potencial de recorrência

**Perguntas:** `Q17` e `Q18`

```text
Uso recorrente esperado (%) = respostas 18.1 + 18.2 + 18.3 / respostas válidas da Q18 × 100
```

**Meta inicial:** `>= 50%`.

Indicadores complementares:

- uso diário ou algumas vezes por semana: `18.1 + 18.2`;
- uso apenas por necessidade específica: `18.5`;
- ausência de motivo de retorno: `17.9`;
- ranking dos motivos de retorno da `Q17`.

Como a `Q17` é fechada, o indicador será denominado **potencial de recorrência**, e não recorrência espontânea.

### 4.10 NPS conceitual

**Pergunta:** `Q19`

- promotores: notas 9 e 10;
- neutros: 7 e 8;
- detratores: 0 a 6.

```text
NPS conceitual = % promotores - % detratores
```

**Meta inicial:** `>= 40`.

### 4.11 Interesse no beta

**Pergunta:** `Q20`

```text
Interesse confirmado no beta (%) = respostas 20.1 / respostas válidas da Q20 × 100
```

**Meta inicial:** `>= 35%`.

Exibir também interesse ampliado (`20.1 + 20.2`) e conversão efetiva em contato.

### 4.12 Disposição inicial para pagar

**Pergunta:** `Q21`

Exibir:

- não pagaria (`21.1`);
- pagamento condicionado a resultado (`21.2`);
- percentual por faixa de preço (`21.3` a `21.6`);
- recusa em responder (`21.7`).

Monetização é indicador diagnóstico e não gate isolado na primeira rodada.

### 4.13 Barreiras principais

**Pergunta:** `Q22`

Exibir ranking e percentual de cada barreira, destacando ausência de necessidade, desconfiança, incompreensão, dúvida sobre relevância, resistência ao acompanhamento de informações pessoais e preço.

## 5. Índice Geral de Validação — IGV

O IGV é uma síntese executiva. Não substitui a leitura por hipótese nem pode aprovar a proposta sozinho.

### 5.1 Normalização

- percentuais permanecem na escala de 0 a 100;
- médias de 0 a 10 são multiplicadas por 10;
- valores são limitados ao intervalo de 0 a 100.

### 5.2 Pesos

| Dimensão | Indicador | Peso |
|---|---|---:|
| Dor | Dor relevante (`Q6`) | 15% |
| Compreensão | Compreensão correta (`Q10`) | 20% |
| Relevância | Média da `Q11` | 15% |
| Transformação percebida | ITP (`Q13`) | 15% |
| Confiança | Média da `Q14` | 10% |
| Intenção de uso | Intenção positiva (`Q16`) | 10% |
| Recorrência | Uso recorrente esperado (`Q18`) | 10% |
| Beta | Interesse confirmado (`Q20`) | 5% |

```text
IGV = soma dos indicadores normalizados × respectivos pesos
```

Monetização e NPS permanecem fora do IGV na primeira rodada.

### 5.3 Leitura do IGV

| IGV | Leitura executiva |
|---:|---|
| 80 a 100 | Aceitação geral forte, sujeita aos gates críticos. |
| 70 a 79,9 | Aceitação promissora com ajustes identificáveis. |
| 55 a 69,9 | Validação parcial; exige revisão relevante e nova rodada. |
| Abaixo de 55 | Evidência insuficiente ou baixa aderência na rodada. |

## 6. Gates críticos

Mesmo com IGV alto, uma decisão `Go` não poderá ser emitida quando houver:

- compreensão correta abaixo de 65%;
- confiança média abaixo de 6,0;
- dor relevante abaixo de 50%;
- intenção positiva de uso abaixo de 45%;
- base inferior a 200 respostas válidas;
- concentração crítica da amostra sem análise segmentada;
- indícios relevantes de viés, duplicidade ou baixa qualidade.

## 7. Estrutura mínima do dashboard

### 7.1 Cabeçalho executivo

- rodada e período de coleta;
- total recebido, concluído e válido;
- nível de maturidade da base;
- IGV;
- decisão preliminar;
- gates atendidos;
- principal força;
- principal risco.

### 7.2 Qualidade da amostra

- taxa de conclusão;
- taxa de abandono;
- tempo mediano;
- distribuição por idade, estado ou Distrito Federal e situação principal;
- consolidação dos estados por região, quando útil;
- concentração por canal de aquisição;
- concentração geográfica;
- exclusões e motivos.

### 7.3 Problema

- dor relevante e dor alta;
- esforço médio e mediano;
- áreas prioritárias (`Q4`);
- dificuldades (`Q5`);
- canais atuais (`Q8`).

### 7.4 Compreensão e valor

- compreensão autodeclarada;
- compreensão correta, parcial e incorreta;
- relevância;
- ITP;
- aspecto de maior valor (`Q12`).

### 7.5 Confiança

- média e distribuição da confiança;
- fatores de confiança (`Q15`);
- confiança por segmento;
- relação entre confiança e intenção de uso.

### 7.6 Adoção e recorrência

- intenção positiva de uso;
- motivos de retorno (`Q17`);
- frequência esperada (`Q18`);
- NPS conceitual;
- interesse no beta;
- conversão em contato opcional.

### 7.7 Monetização e barreiras

- disposição para pagar;
- faixas de preço;
- ranking das barreiras (`Q22`);
- barreiras por segmento;
- comentários opcionais da `Q23`.

## 8. Segmentações obrigatórias

Os KPIs principais deverão permitir corte por:

- faixa etária (`Q1`);
- estado ou Distrito Federal (`Q2`);
- região derivada do estado (`Q2`);
- situação principal (`Q3`);
- área prioritária de evolução (`Q4`);
- intensidade da dor (`Q6`);
- nível de confiança (`Q14`);
- intenção de uso (`Q16`).

Participantes fora do Brasil deverão ser analisados separadamente da base nacional.

Estados com menos de 30 respostas deverão ser destacados como base reduzida e não deverão receber conclusão isolada. O painel deverá identificar concentração excessiva em São Paulo, Minas Gerais ou qualquer outra unidade federativa.

## 9. Semáforo dos indicadores

- **Verde:** atingiu a meta de `Go` definida no VAL-007;
- **Amarelo:** está na faixa de `Go com ajustes`;
- **Vermelho:** está na faixa de `Pivot parcial / No-Go temporário`;
- **Cinza:** base insuficiente ou indicador ainda não calculável.

## 10. Saída executiva obrigatória

Cada atualização do dashboard deverá produzir:

1. fotografia da amostra;
2. resultados dos KPIs;
3. semáforo por dimensão;
4. IGV;
5. gates críticos;
6. leitura por segmento e por estado quando houver base suficiente;
7. evidências favoráveis e contrárias;
8. decisão preliminar conforme VAL-007;
9. recomendações de ajuste;
10. limitações e próxima ação.