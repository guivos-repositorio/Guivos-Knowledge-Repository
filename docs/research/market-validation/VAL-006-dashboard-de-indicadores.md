---
id: VAL-006
title: Dashboard de Indicadores de Validação
status: active
version: 1.3.1
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
- identificar divergências entre segmentos;
- verificar qualidade e estabilidade da amostra;
- apoiar decisão `Go`, `Go com ajustes`, `Pivot parcial` ou `No-Go temporário`;
- preservar rastreabilidade entre indicador e pergunta;
- diferenciar percepção conceitual de evidência comportamental;
- acompanhar tempo de preenchimento e abandono como sinais de carga cognitiva.

## 2. Níveis de maturidade da base

| Respostas válidas | Classificação | Uso permitido |
|---:|---|---|
| 10 a 15 | Pré-teste | Revisar clareza, duração, lógica, alternativas e abandono. Não decidir aceitação. |
| 16 a 49 | Exploratória | Identificar sinais e problemas evidentes. Não emitir decisão formal. |
| 50 a 199 | Indicativa | Analisar tendências preliminares e segmentos, com cautela. |
| 200 a 499 | Base de decisão inicial | Permite decisão inicial, desde que a amostra tenha diversidade mínima. |
| 500 ou mais | Base preferencial | Permite decisão mais robusta e segmentação mais confiável. |

Quantidade de respostas, isoladamente, não torna a amostra representativa da população brasileira.

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
- percentual concluído em até 3, 5 e mais de 5 minutos;
- versão do instrumento;
- motivos das exclusões.

## 4. Dicionário oficial de KPIs

### 4.1 Descoberta tardia relevante

**Pergunta:** `Q8`

A alternativa `8.5 — Não me lembro` será excluída do denominador.

```text
Descoberta tardia total (%) = respostas 8.2 + 8.3 + 8.4 / respostas 8.1 a 8.4 × 100
```

```text
Descoberta tardia relevante (%) = respostas 8.3 + 8.4 / respostas 8.1 a 8.4 × 100
```

```text
Descoberta tardia alta (%) = respostas 8.4 / respostas 8.1 a 8.4 × 100
```

O componente utilizado no IFO é a descoberta tardia relevante.

### 4.2 Lacuna de adequação de oportunidades

**Pergunta:** `Q9`

As alternativas `9.5 — Não procurei nesse período` e `9.6 — Não me lembro` serão excluídas do denominador.

```text
Busca sem opção adequada total (%) = respostas 9.2 + 9.3 + 9.4 / respostas 9.1 a 9.4 × 100
```

```text
Lacuna de adequação relevante (%) = respostas 9.3 + 9.4 / respostas 9.1 a 9.4 × 100
```

```text
Lacuna de adequação alta (%) = respostas 9.4 / respostas 9.1 a 9.4 × 100
```

O componente utilizado no IFO é a lacuna de adequação relevante.

Exibir separadamente ausência de busca (`9.5`), não recordação (`9.6`) e base elegível.

### 4.3 Índice de Fricção de Oportunidades — IFO

```text
IFO = média entre Descoberta tardia relevante e Lacuna de adequação relevante
```

**Meta inicial:** `>= 65%`.

O IFO somente deverá receber semáforo quando os dois componentes possuírem base suficiente. Caso contrário, permanecerá cinza e os componentes serão apresentados separadamente.

O IFO mede fricção temporal e inadequação das opções encontradas. Não mede todas as dificuldades de evolução.

### 4.4 Esforço atual

**Pergunta:** `Q10`

**Cálculo:** média e mediana da escala de 0 a 10.

**Sinal de problema relevante:** média `>= 6,0`.

Exibir distribuição completa e percentual de notas 8 a 10.

### 4.5 Compreensão correta

**Pergunta:** `Q11`

Cada resposta será classificada como:

- **1,0 — correta:** reconhece contexto ou momento e apoio para compreender, organizar, explorar ou encontrar possibilidades relevantes;
- **0,5 — parcialmente correta:** reconhece apenas parte da proposta;
- **0,0 — incorreta:** reduz a Guivos a catálogo, rede social, marketplace isolado, sistema que decide pela pessoa ou conceito incompatível.

```text
Compreensão correta (%) = respostas classificadas como 1,0 / respostas válidas da Q11 × 100
```

**Meta inicial:** `>= 80%`.

Exibir compreensão correta, parcial, genérica e incorreta.

### 4.6 Relevância contextual

**Pergunta:** `Q12`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

A leitura deverá ser vinculada à área escolhida (`Q4`) e ao momento atual (`Q5`).

### 4.7 Contribuição percebida

**Pergunta:** `Q15`

**Cálculo:** média e mediana da escala de 0 a 10.

**Meta inicial:** `>= 8,0`.

Este indicador mede crença de contribuição, não transformação real.

### 4.8 Intenção positiva de experimentar

**Pergunta:** `Q16`

```text
Intenção positiva (%) = respostas 16.4 + 16.5 / respostas válidas da Q16 × 100
```

**Meta inicial:** `>= 60%`.

Exibir também intenção negativa (`16.1 + 16.2`) e indecisão (`16.3`).

### 4.9 Interesse confirmado na primeira experiência

**Pergunta:** `Q17`

```text
Interesse confirmado (%) = respostas 17.1 / respostas válidas da Q17 × 100
```

**Meta inicial:** `>= 35%`.

Exibir interesse ampliado (`17.1 + 17.2`) e conversão efetiva em contato.

## 5. Indicadores diagnósticos

### 5.1 Área escolhida — Q4

Exibir ranking e percentual por área.

### 5.2 Momento atual — Q5

Exibir ranking e comparar:

- objetivo claro;
- exploração;
- percepção de mudança sem definição;
- necessidade específica;
- início, retomada ou fortalecimento;
- ausência de busca por mudança;
- incerteza.

### 5.3 Mudança desejada — Q6

Exibir ranking e cruzamento com `Q4` e `Q5`.

### 5.4 Dificuldades — Q7

Exibir frequência, quantidade média selecionada e combinações recorrentes. A pergunta permite no máximo duas escolhas.

### 5.5 Situação de primeiro uso — Q13

Exibir ranking e percentual, destacando:

- percepção de mudança;
- exploração;
- objetivo sem caminho;
- busca por oportunidade adequada;
- transição importante;
- início, retomada ou acompanhamento;
- incapacidade de imaginar uso.

### 5.6 Utilidade esperada — Q14

Exibir ranking, percentual e combinações das duas opções selecionadas.

### 5.7 Barreiras — Q18

Exibir ranking e percentual por barreira, além de cruzamento com intenção (`Q16`) e interesse (`Q17`).

## 6. Índice Geral de Validação — IGV

O IGV é uma síntese executiva. Não substitui leitura por hipótese nem pode aprovar a proposta sozinho.

### 6.1 Normalização

- percentuais permanecem na escala de 0 a 100;
- médias de 0 a 10 são multiplicadas por 10;
- valores são limitados ao intervalo de 0 a 100.

### 6.2 Pesos

| Dimensão | Indicador | Peso |
|---|---|---:|
| Problema | IFO (`Q8 + Q9`) | 15% |
| Compreensão | Compreensão correta (`Q11`) | 20% |
| Relevância | Média da `Q12` | 20% |
| Contribuição | Média da `Q15` | 20% |
| Intenção | Intenção positiva (`Q16`) | 20% |
| Primeira experiência | Interesse confirmado (`Q17`) | 5% |

```text
IGV = soma dos indicadores normalizados × respectivos pesos
```

Esforço, indicadores diagnósticos e carga cognitiva permanecem fora do IGV.

Quando o IFO não puder ser calculado, o IGV também deverá permanecer incompleto e não poderá sustentar decisão `Go`.

### 6.3 Leitura do IGV

| IGV | Leitura executiva |
|---:|---|
| 80 a 100 | Aceitação geral forte, sujeita aos gates críticos. |
| 70 a 79,9 | Aceitação promissora com ajustes identificáveis. |
| 55 a 69,9 | Validação parcial; exige revisão relevante e nova rodada. |
| Abaixo de 55 | Evidência insuficiente ou baixa aderência. |

## 7. Gates críticos

Mesmo com IGV alto, uma decisão `Go` não poderá ser emitida quando houver:

- compreensão correta abaixo de 65%;
- IFO abaixo de 50%;
- relevância abaixo de 7,0;
- contribuição abaixo de 7,0;
- intenção positiva abaixo de 45%;
- IFO ou IGV não calculável;
- base inferior a 200 respostas válidas;
- concentração crítica da amostra sem análise;
- viés, duplicidade ou baixa qualidade relevante.

Taxa de abandono ou tempo excessivo não invalida automaticamente a proposta, mas pode invalidar o instrumento e exigir nova aplicação.

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

### 8.2 Qualidade da coleta

- taxa de conclusão;
- taxa de abandono;
- tempo médio e mediano;
- respostas por faixa de duração;
- distribuição por idade, estado e situação principal;
- concentração por canal e região;
- exclusões e motivos.

### 8.3 Problema e momento

- área (`Q4`);
- momento (`Q5`);
- mudança desejada (`Q6`);
- dificuldades (`Q7`);
- descoberta tardia (`Q8`);
- lacuna de adequação (`Q9`);
- IFO;
- esforço (`Q10`).

### 8.4 Compreensão

- compreensão correta, parcial, genérica e incorreta (`Q11`);
- padrões de compreensão e confusão.

### 8.5 Aplicação e valor

- relevância (`Q12`);
- primeiro uso (`Q13`);
- utilidade esperada (`Q14`);
- contribuição (`Q15`).

### 8.6 Intenção e barreiras

- intenção (`Q16`);
- primeira experiência (`Q17`);
- barreiras (`Q18`);
- comentários opcionais (`Q19`).

## 9. Segmentações mínimas

Os KPIs principais deverão permitir corte por:

- faixa etária (`Q1`);
- estado e região (`Q2`);
- situação principal (`Q3`);
- área (`Q4`);
- momento (`Q5`);
- mudança desejada (`Q6`);
- descoberta tardia (`Q8`);
- lacuna de adequação (`Q9`);
- situação de primeiro uso (`Q13`);
- intenção (`Q16`);
- interesse (`Q17`);
- barreira (`Q18`).

## 10. Compatibilidade de versões

Resultados do VAL-002 `2.1.0` deverão ser identificados separadamente das versões `1.x` e `2.0.0`.

Qualquer consolidação histórica exigirá mapa explícito de equivalência entre perguntas, alternativas e denominadores.
