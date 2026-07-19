---
id: VAL-007
title: Critérios de Decisão da Validação
status: active
version: 1.3.1
owner: Guivos
last_updated: 2026-07-19
related:
  - VAL-001
  - VAL-002
  - VAL-004
  - VAL-005
  - VAL-006
---

# VAL-007 — Critérios de Decisão da Validação

## 1. Finalidade

Transformar os resultados da validação B2C em decisões objetivas, rastreáveis e resistentes a interpretações seletivas ou excessivamente otimistas.

A decisão deverá considerar simultaneamente:

- qualidade da amostra;
- qualidade do instrumento;
- KPIs principais;
- gates críticos;
- diferenças entre segmentos;
- distribuição geográfica;
- evidências favoráveis e contrárias;
- limitações metodológicas;
- comentários qualitativos relevantes.

## 2. Elegibilidade para decisão

Uma rodada somente poderá receber decisão formal quando:

1. possuir pelo menos 200 respostas válidas;
2. tiver passado pelo pré-teste da versão aplicada;
3. apresentar diversidade mínima por idade, estado, situação principal e estágio de clareza;
4. identificar e tratar concentração crítica em estado ou canal;
5. tiver a `Q11` classificada conforme a rubrica de compreensão;
6. apresentar cálculo completo dos KPIs do VAL-006;
7. registrar versão, exclusões, denominadores, limitações e vieses;
8. não apresentar falha grave de compreensão ou carga cognitiva do instrumento.

Bases com menos de 200 respostas podem gerar leitura exploratória ou indicativa, mas não decisão formal.

A ausência de respostas em todos os estados não impede decisão inicial. O alcance geográfico deverá ser declarado com precisão.

## 3. Estados possíveis

### 3.1 Go

A proposta apresenta evidências consistentes de:

- fricção relevante na descoberta e adequação de oportunidades;
- compreensão adequada;
- relevância contextual;
- aplicação prática reconhecível;
- contribuição percebida;
- intenção de experimentar;
- interesse real em aprofundar a validação.

`Go` autoriza avançar para nova etapa de validação ou MVP controlado. Não autoriza construir todo o ecossistema de uma vez.

### 3.2 Go com ajustes

A proposta apresenta aderência promissora, mas exige correções específicas antes da próxima etapa.

Os ajustes podem envolver narrativa, público prioritário, proposta de valor, situação de primeiro uso, escopo inicial, barreiras, canais, experiência da pesquisa ou expansão geográfica.

### 3.3 Pivot parcial

Existe fricção ou valor em segmentos específicos, mas parte relevante da solução, narrativa, público, mecanismo de valor ou situação de uso precisa mudar.

O pivot deverá preservar evidências válidas e formular novas hipóteses testáveis.

### 3.4 No-Go temporário

As evidências são fracas, contraditórias, insuficientes ou metodologicamente inadequadas.

A decisão interrompe expansão de escopo e investimento relevante até que novas hipóteses sejam formuladas e testadas.

## 4. Faixas oficiais por indicador

| Dimensão | Go | Go com ajustes | Pivot parcial / No-Go temporário |
|---|---:|---:|---:|
| IFO — Q8 + Q9 | >= 65% | 50% a 64,9% | < 50% |
| Esforço médio — Q10 | >= 6,0 | 5,0 a 5,9 | < 5,0 |
| Compreensão correta — Q11 | >= 80% | 65% a 79,9% | < 65% |
| Relevância contextual — Q12 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Contribuição percebida — Q15 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Intenção positiva — Q16 | >= 60% | 45% a 59,9% | < 45% |
| Interesse confirmado — Q17 | >= 35% | 20% a 34,9% | < 20% |

Descoberta tardia (`Q8`) e lacuna de adequação (`Q9`) deverão ser exibidas separadamente, mesmo quando consolidadas no IFO.

Momento atual (`Q5`), mudança desejada (`Q6`), situação de primeiro uso (`Q13`), utilidade esperada (`Q14`) e barreira (`Q18`) orientam interpretação e ajustes, mas não possuem meta universal isolada.

## 5. Gates críticos

Uma decisão `Go` exige todos os gates abaixo:

| Gate | Condição mínima |
|---|---|
| G1 — Base elegível | >= 200 respostas válidas |
| G2 — Compreensão | compreensão correta >= 80% |
| G3 — Problema | IFO calculável e >= 65% |
| G4 — Valor | relevância >= 8,0 e contribuição >= 8,0 |
| G5 — Adoção | intenção positiva >= 60% |
| G6 — Qualidade | ausência de viés crítico não tratado e denominadores explícitos |
| G7 — Cobertura | concentração geográfica identificada e considerada |
| G8 — Instrumento | pré-teste concluído sem falha grave de leitura, lógica ou abandono |

O interesse na primeira experiência reforça a decisão, mas não compensa falha em compreensão, problema, valor ou intenção.

## 6. Regra combinada de decisão

### 6.1 Go

Emitir `Go` quando:

- todos os gates críticos forem atendidos;
- pelo menos 5 dos 7 indicadores estiverem na faixa `Go`;
- nenhum indicador crítico estiver na faixa vermelha;
- o IGV for `>= 80`;
- descoberta tardia e lacuna de adequação tiverem bases interpretáveis;
- não houver segmento majoritário com rejeição substancial ocultada pela média;
- o alcance geográfico estiver explicitado.

### 6.2 Go com ajustes

Emitir `Go com ajustes` quando:

- a base for elegível;
- nenhum gate estrutural estiver gravemente comprometido;
- o IGV estiver entre `70` e `79,9`; ou
- houver até três indicadores na faixa amarela e nenhum gate crítico vermelho;
- os ajustes necessários forem específicos e testáveis.

Também pode ocorrer com IGV acima de 80 quando houver concentração geográfica, segmentos polarizados, diferença relevante entre os componentes do IFO ou barreira crítica.

### 6.3 Pivot parcial

Emitir `Pivot parcial` quando:

- o IFO indicar problema, mas compreensão, relevância, contribuição ou intenção estiverem abaixo do necessário;
- apenas um componente do IFO demonstrar fricção consistente;
- o IGV estiver entre `55` e `69,9`;
- houver área, estágio de clareza ou segmento claramente promissor e outros com baixa aderência;
- a proposta precisar de mudança relevante, mas as evidências sustentarem continuidade.

### 6.4 No-Go temporário

Emitir `No-Go temporário` quando:

- IFO estiver abaixo de 50%; ou
- compreensão correta estiver abaixo de 65%; ou
- intenção positiva estiver abaixo de 45%; ou
- IGV estiver abaixo de 55; ou
- IFO ou IGV não puder ser calculado por falha grave da base; ou
- a qualidade da base impedir interpretação confiável; ou
- não houver segmento com aderência suficiente para justificar pivot específico.

Relevância ou contribuição abaixo de 7,0 deverão gerar, no mínimo, investigação de pivot.

## 7. Regras de interpretação

1. Nenhum indicador isolado aprova a proposta.
2. Descoberta tardia e busca sem opção adequada representam problemas diferentes.
3. `Não procurei` não equivale a `não encontrei`.
4. `Não me lembro` não equivale a ausência do problema.
5. Oportunidades desconhecidas não podem ser declaradas como perdidas pela pessoa.
6. Compreensão baixa invalida interpretação de interesse alto.
7. Intenção declarada não equivale a adoção comprovada.
8. Contribuição percebida não equivale a transformação real.
9. Interesse na primeira experiência deve ser comparado com conversão em contato e participação efetiva.
10. Situação de primeiro uso e utilidade esperada orientam o recorte do MVP.
11. Médias gerais não devem ocultar estágios de clareza, segmentos ou estados divergentes.
12. Resultados positivos em amostra concentrada não autorizam generalização nacional.
13. Estados com menos de 30 respostas não deverão receber conclusão isolada.
14. Participantes fora do Brasil deverão ser analisados separadamente.
15. Evidência comportamental posterior poderá confirmar ou contrariar a pesquisa.
16. Tempo excessivo ou abandono alto pode indicar falha do instrumento, não rejeição da proposta.

## 8. Matriz de diagnóstico

| Sinal observado | Leitura provável | Ação recomendada |
|---|---|---|
| Descoberta tardia alta + lacuna alta | Existe fricção de acesso no tempo certo e de adequação. | Priorizar descoberta contextual e adequação. |
| Descoberta tardia alta + lacuna baixa | O principal problema parece ser acesso ou timing. | Priorizar alertas e descoberta antecipada. |
| Descoberta tardia baixa + lacuna alta | As pessoas encontram opções, mas elas não fazem sentido. | Priorizar contexto, filtragem e adequação. |
| IFO alto + compreensão baixa | O problema existe, mas a narrativa falha. | Revisar apresentação e repetir o teste. |
| Compreensão alta + primeiro uso pouco reconhecido | A ideia é clara, mas a aplicação não está evidente. | Refinar casos de uso. |
| Relevância alta + contribuição baixa | A proposta interessa, mas não demonstra impacto suficiente. | Revisar mecanismo de valor. |
| Contribuição alta + intenção baixa | Existe valor percebido, mas há barreira de adoção. | Investigar esforço, formato e objeções. |
| Intenção alta + participação baixa | Curiosidade não se converte em compromisso. | Revisar convite e primeira experiência. |
| Utilidade concentrada em uma função | O valor inicial pode ser mais focado. | Priorizar essa função no MVP. |
| Alta aderência entre pessoas em exploração | A descoberta pode ser um caso de uso central. | Testar experiência de exploração guiada. |
| Alta aderência entre pessoas com objetivo claro | O valor pode estar em execução e oportunidade. | Testar próximos passos e matching. |
| Abandono alto antes da apresentação | Existe carga cognitiva no diagnóstico inicial. | Reduzir enunciados ou alternativas. |
| Abandono alto após a apresentação | A narrativa ou o bloco de valor pode estar pesado. | Revisar apresentação e perguntas posteriores. |
| Médias boas + estados polarizados | A aderência geográfica é desigual. | Investigar diferenças e limitar conclusão. |

## 9. Evidências obrigatórias para o registro da decisão

Cada rodada deverá registrar:

- identificação e período;
- versão do instrumento;
- quantidade recebida, concluída e válida;
- duração média e mediana;
- taxa e ponto de abandono;
- composição e origem da amostra;
- distribuição por estado e região;
- bases elegíveis de Q8 e Q9;
- descoberta tardia, lacuna e IFO;
- KPIs e respectivas faixas;
- IGV;
- gates atendidos e não atendidos;
- áreas, momentos, mudanças desejadas e situações de uso prioritárias;
- segmentos de maior e menor aderência;
- evidências favoráveis e contrárias;
- barreiras principais;
- limitações e vieses;
- alcance permitido da conclusão;
- decisão aprovada;
- mudanças autorizadas;
- hipóteses para a próxima rodada;
- responsável e data.

## 10. Autoridade da decisão

O dashboard produz recomendação técnica. A decisão final deverá ser formalmente aprovada pela governança responsável da Guivos e registrada no GKR.

Qualquer decisão que contrarie os critérios objetivos deverá apresentar justificativa explícita, riscos assumidos e evidências adicionais.
