---
id: VAL-006
title: Dashboard de Indicadores de Validação
status: active
version: 1.3.0
owner: Guivos
last_updated: 2026-07-19
related:
  - VAL-001
  - VAL-002
  - VAL-004
  - VAL-005
  - VAL-007
---

# VAL-006 — Dashboard de Indicadores de Validação

## 1. Objetivo

Definir o painel executivo utilizado quando houver base suficiente de respostas da Pesquisa Oficial B2C da Guivos.

O dashboard deverá:

- medir os KPIs oficiais da versão vigente;
- comparar resultados com metas explícitas;
- identificar diferenças entre segmentos;
- verificar qualidade e estabilidade da amostra;
- apoiar decisão `Go`, `Go com ajustes`, `Pivot parcial` ou `No-Go temporário`;
- preservar rastreabilidade entre indicador e pergunta;
- diferenciar percepção conceitual de evidência comportamental;
- analisar separadamente pessoas com e sem objetivo claro.

## 2. Níveis de maturidade da base

| Respostas válidas | Classificação | Uso permitido |
|---:|---|---|
| 10 a 15 | Pré-teste | Revisar clareza, duração, lógica e abandono. Não decidir aceitação. |
| 16 a 49 | Exploratória | Identificar sinais e problemas evidentes. Não emitir decisão formal. |
| 50 a 199 | Indicativa | Analisar tendências preliminares e segmentos, com cautela. |
| 200 a 499 | Base de decisão inicial | Permite decisão inicial com diversidade mínima e vieses tratados. |
| 500 ou mais | Base preferencial | Permite decisão mais robusta e segmentações mais estáveis. |

A quantidade de respostas não torna automaticamente a amostra representativa da população brasileira. O painel deverá exibir composição, origem e limitações.

## 3. Regras de validade da resposta

Uma resposta será considerada válida quando:

1. tiver sido concluída;
2. estiver vinculada à versão do instrumento;
3. não apresentar padrão evidente de preenchimento aleatório ou automatizado;
4. possuir tempo de resposta plausível;
5. contiver resposta utilizável na pergunta aberta de compreensão (`Q11`);
6. não for duplicação confirmada;
7. respeitar o público da rodada.

O dashboard deverá exibir:

- respostas recebidas;
- respostas concluídas;
- respostas válidas;
- respostas excluídas;
- taxa de conclusão;
- taxa de abandono;
- tempo médio e mediano;
- versão do instrumento;
- motivo das exclusões.

## 4. Dicionário oficial de KPIs

### 4.1 Descoberta tardia relevante

**Pergunta:** `Q8`

A alternativa `8.6 — Não me recordo` será excluída do denominador.

```text
Descoberta tardia relevante (%) =
(respostas 8.3 + 8.4 + 8.5) / respostas 8.1 a 8.5 × 100
```

Indicador complementar:

```text
Descoberta tardia alta (%) =
(respostas 8.4 + 8.5) / respostas 8.1 a 8.5 × 100
```

Exibir separadamente o percentual de `8.6` e a base elegível.

### 4.2 Lacuna de adequação de oportunidades

**Pergunta:** `Q9`

As alternativas `9.6 — Não procurei possibilidades nesse período` e `9.7 — Não me recordo` serão excluídas do denominador.

```text
Lacuna de adequação (%) =
(respostas 9.3 + 9.4 + 9.5) / respostas 9.1 a 9.5 × 100
```

Indicador complementar:

```text
Lacuna de adequação alta (%) =
(respostas 9.4 + 9.5) / respostas 9.1 a 9.5 × 100
```

Exibir separadamente ausência de busca, não recordação e base elegível.

### 4.3 Índice de Fricção de Oportunidades — IFO

```text
IFO = média entre Descoberta tardia relevante e Lacuna de adequação
```

**Meta inicial:** `>= 65%`.

O IFO somente receberá semáforo quando os dois componentes possuírem base suficiente.

O IFO não mede todas as dificuldades da jornada. Mede especificamente fricção temporal e inadequação das opções encontradas.

### 4.4 Esforço atual

**Pergunta:** `Q10`

**Cálculo:** média e mediana da escala de 0 a 10.

**Sinal de problema relevante:** média `>= 6,0`.

Exibir também:

- percentual de notas 8 a 10;
- distribuição completa;
- comparação com IFO;
- comparação por momento atual (`Q5`).

### 4.5 Compreensão correta

**Pergunta:** `Q11`

Cada resposta deverá ser classificada como:

- **1,0 — correta:** reconhece que a Guivos considera o momento da pessoa, inclusive sem objetivo claro, e ajuda a compreender, organizar ou explorar caminhos, ações possíveis ou oportunidades, preservando a decisão da pessoa;
- **0,5 — parcialmente correta:** reconhece apenas parte dos elementos centrais, sem contradição material;
- **0,0 — incorreta:** descreve catálogo genérico, marketplace isolado, rede social, sistema que define a pessoa ou solução que decide por ela.

```text
Compreensão correta (%) =
respostas classificadas como 1,0 / respostas válidas da Q11 × 100
```

**Meta inicial:** `>= 80%`.

Exibir correta, parcial, genérica, incorreta e não respondida.

### 4.6 Relevância contextual

**Pergunta:** `Q12`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

A leitura deverá ser vinculada a:

- área (`Q4`);
- momento atual (`Q5`);
- mudança desejada (`Q6`).

### 4.7 Contribuição percebida

**Pergunta:** `Q16`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

Este indicador mede crença de contribuição potencial. Não mede transformação real.

### 4.8 Intenção positiva de experimentar

**Pergunta:** `Q17`

```text
Intenção positiva (%) =
(respostas 17.4 + 17.5) / respostas válidas da Q17 × 100
```

**Meta inicial:** `>= 60%`.

Exibir:

- intenção negativa (`17.1 + 17.2`);
- indecisão (`17.3`);
- intenção positiva (`17.4 + 17.5`).

### 4.9 Interesse confirmado na primeira experiência

**Pergunta:** `Q18`

```text
Interesse confirmado (%) =
respostas 18.1 / respostas válidas da Q18 × 100
```

**Meta inicial:** `>= 35%`.

Exibir também:

- interesse ampliado (`18.1 + 18.2`);
- conversão efetiva em contato;
- participação real posterior.

## 5. Indicadores diagnósticos

### 5.1 Área prioritária

**Pergunta:** `Q4`

Exibir ranking e percentual, incluindo:

- ainda não sabe qual área merece atenção;
- ausência de área prioritária;
- outras áreas.

### 5.2 Momento atual

**Pergunta:** `Q5`

Exibir ranking e cruzamentos com área e mudança desejada.

Agrupamentos analíticos possíveis:

- **clareza alta:** `5.1`;
- **exploração:** `5.2 + 5.3 + 5.7 + 5.9`;
- **necessidade concreta:** `5.4`;
- **retomada:** `5.5`;
- **manutenção ou fortalecimento:** `5.6`;
- **sem busca de mudança:** `5.8`;
- **outra situação:** `5.10`.

Os agrupamentos não substituem a distribuição por alternativa.

### 5.3 Mudança desejada

**Pergunta:** `Q6`

Exibir ranking geral e cruzamentos com área e momento atual.

### 5.4 Dificuldades atuais

**Pergunta:** `Q7`

Exibir:

- frequência de cada dificuldade;
- quantidade média selecionada;
- combinações recorrentes;
- destaque para dificuldade de entender o que deseja (`7.4`);
- destaque para ausência de grandes dificuldades (`7.13`).

### 5.5 Situação de primeiro uso

**Pergunta:** `Q13`

Exibir ranking e percentual por situação, destacando:

- mudança sem direção;
- exploração antes da decisão;
- objetivo sem caminho;
- necessidade sem opção adequada;
- transição de vida;
- excesso de opções;
- retomada ou manutenção;
- conexão com pessoas ou organizações;
- acompanhamento;
- uso apenas por necessidade específica;
- incapacidade de imaginar uso.

### 5.6 Expectativas sobre a plataforma

**Pergunta:** `Q14`

Exibir ranking, percentual e combinações mais frequentes.

### 5.7 Resultado concreto de valor

**Pergunta:** `Q15`

Exibir ranking do principal resultado considerado útil.

### 5.8 Barreiras principais

**Pergunta:** `Q19`

Exibir ranking, percentual e cruzamentos com momento atual e intenção.

Destacar:

- ausência de necessidade;
- proposta genérica ou incompreendida;
- dúvida sobre adequação;
- dúvida sobre compreensão do momento;
- preocupação com informações pessoais;
- suficiência de outras soluções;
- falta de tempo ou interesse;
- resistência a refletir ou acompanhar aspectos pessoais;
- esforço inicial;
- ausência de barreira.

## 6. Índice Geral de Validação — IGV

O IGV é síntese executiva. Não substitui leitura por hipótese nem aprova a proposta sozinho.

### 6.1 Normalização

- percentuais permanecem de 0 a 100;
- médias de 0 a 10 são multiplicadas por 10;
- valores são limitados ao intervalo de 0 a 100.

### 6.2 Pesos

| Dimensão | Indicador | Peso |
|---|---|---:|
| Problema | IFO (`Q8 + Q9`) | 15% |
| Compreensão | Compreensão correta (`Q11`) | 20% |
| Relevância | Média da `Q12` | 20% |
| Contribuição | Média da `Q16` | 20% |
| Intenção | Intenção positiva (`Q17`) | 20% |
| Primeira experiência | Interesse confirmado (`Q18`) | 5% |

```text
IGV = soma dos indicadores normalizados × respectivos pesos
```

Esforço e indicadores diagnósticos permanecem fora do IGV.

Quando o IFO não puder ser calculado, o IGV também permanecerá incompleto e não poderá sustentar `Go`.

### 6.3 Leitura do IGV

| IGV | Leitura executiva |
|---:|---|
| 80 a 100 | Aceitação geral forte, sujeita aos gates. |
| 70 a 79,9 | Aceitação promissora com ajustes. |
| 55 a 69,9 | Validação parcial; exige revisão relevante. |
| Abaixo de 55 | Evidência insuficiente ou baixa aderência. |

## 7. Gates críticos

Mesmo com IGV alto, `Go` não poderá ser emitido quando houver:

- compreensão correta abaixo de 65%;
- IFO abaixo de 50%;
- relevância abaixo de 7,0;
- contribuição abaixo de 7,0;
- intenção positiva abaixo de 45%;
- IFO ou IGV não calculável;
- base inferior a 200 respostas válidas;
- concentração crítica sem análise;
- indícios relevantes de viés, duplicidade ou baixa qualidade.

Confiança operacional, recorrência, retenção, recomendação e monetização não integram os gates desta rodada porque dependem de experiência real.

## 8. Estrutura mínima do dashboard

### 8.1 Cabeçalho executivo

- rodada e período;
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
- tempo médio e mediano;
- distribuição por idade, estado e situação principal;
- regiões;
- concentração por canal;
- concentração geográfica;
- exclusões e motivos.

### 8.3 Momento e problema

- área (`Q4`);
- momento atual (`Q5`);
- mudança desejada (`Q6`);
- dificuldades (`Q7`);
- descoberta tardia (`Q8`);
- lacuna de adequação (`Q9`);
- IFO;
- esforço (`Q10`);
- bases elegíveis, não recordação e ausência de busca.

### 8.4 Compreensão

- compreensão correta, parcial, genérica e incorreta (`Q11`);
- principais padrões de compreensão;
- confusões recorrentes;
- diferença entre pessoas com e sem objetivo claro.

### 8.5 Aplicação prática e valor

- relevância (`Q12`);
- primeiro uso (`Q13`);
- expectativas (`Q14`);
- resultado concreto (`Q15`);
- contribuição (`Q16`).

### 8.6 Intenção e primeira experiência

- intenção (`Q17`);
- interesse confirmado e ampliado (`Q18`);
- conversão em contato.

### 8.7 Barreiras e feedback

- barreiras (`Q19`);
- barreiras por segmento;
- comentários opcionais (`Q20`).

## 9. Segmentações mínimas

Os KPIs deverão permitir corte por:

- faixa etária (`Q1`);
- estado (`Q2`);
- região (`Q2`);
- situação principal (`Q3`);
- área (`Q4`);
- momento atual (`Q5`);
- mudança desejada (`Q6`);
- descoberta tardia (`Q8`);
- lacuna de adequação (`Q9`);
- intensidade do IFO;
- primeiro uso (`Q13`);
- intenção (`Q17`);
- interesse na primeira experiência (`Q18`);
- barreira principal (`Q19`).

## 10. Compatibilidade

A versão `1.3.0` acompanha o VAL-002 `2.0.0`.

Dashboards de instrumentos `1.x` não deverão ser combinados diretamente com a versão atual sem transformação explícita.
