---
id: VAL-007
title: Critérios de Decisão da Validação
status: active
version: 1.1.0
owner: Guivos
last_updated: 2026-07-11
related:
  - VAL-001
  - VAL-002
  - VAL-006
---

# VAL-007 — Critérios de Decisão da Validação

## 1. Finalidade

Transformar os resultados da validação B2C em decisões objetivas, rastreáveis e resistentes a interpretações seletivas ou excessivamente otimistas.

A decisão deverá considerar simultaneamente:

- qualidade da amostra;
- KPIs principais;
- gates críticos;
- diferenças entre segmentos;
- evidências favoráveis e contrárias;
- limitações metodológicas;
- comentários qualitativos relevantes.

## 2. Elegibilidade para decisão

Uma rodada somente poderá receber decisão formal quando:

1. possuir pelo menos 200 respostas válidas;
2. tiver passado pelo pré-teste do instrumento;
3. apresentar distribuição mínima por idade, região e situação principal;
4. não possuir concentração crítica em um único canal de aquisição sem análise separada;
5. tiver a `Q10` classificada conforme a rubrica de compreensão;
6. apresentar cálculo completo dos KPIs do VAL-006;
7. registrar exclusões, limitações e possíveis vieses.

Bases com menos de 200 respostas podem gerar leitura exploratória ou indicativa, mas não decisão formal.

## 3. Estados possíveis

### 3.1 Go

A proposta apresenta evidências consistentes de:

- problema relevante;
- compreensão adequada;
- valor percebido;
- confiança suficiente;
- intenção de uso;
- potencial de recorrência;
- interesse real em aprofundar a validação.

`Go` autoriza avançar para nova etapa de validação ou MVP controlado. Não autoriza construir todo o ecossistema de uma vez.

### 3.2 Go com ajustes

A proposta apresenta aderência promissora, mas exige correções específicas antes da próxima etapa.

Os ajustes podem envolver:

- narrativa;
- público prioritário;
- confiança e privacidade;
- proposta de valor;
- recorrência;
- escopo inicial;
- monetização;
- canais de aquisição.

### 3.3 Pivot parcial

A dor existe, porém uma parte relevante da solução, narrativa, público, mecanismo de valor ou proposta de recorrência precisa mudar.

O pivot deverá preservar as evidências válidas e formular novas hipóteses testáveis.

### 3.4 No-Go temporário

As evidências são fracas, contraditórias, insuficientes ou metodologicamente inadequadas.

A decisão interrompe expansão de escopo e investimento relevante até que novas hipóteses sejam formuladas e testadas.

`No-Go temporário` não significa encerramento definitivo da Guivos. Significa que a hipótese ou a forma atual de apresentá-la não foi suficientemente validada.

## 4. Faixas oficiais por indicador

| Dimensão | Go | Go com ajustes | Pivot parcial / No-Go temporário |
|---|---:|---:|---:|
| Dor relevante — Q6 | >= 65% | 50% a 64,9% | < 50% |
| Esforço médio — Q7 | >= 6,0 | 5,0 a 5,9 | < 5,0 |
| Compreensão autodeclarada — Q9 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Compreensão correta — Q10 | >= 80% | 65% a 79,9% | < 65% |
| Relevância média — Q11 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| ITP médio — Q13 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Confiança média — Q14 | >= 7,0 | 6,0 a 6,9 | < 6,0 |
| Intenção positiva de uso — Q16 | >= 60% | 45% a 59,9% | < 45% |
| Uso recorrente esperado — Q18 | >= 50% | 35% a 49,9% | < 35% |
| NPS conceitual — Q19 | >= 40 | 10 a 39 | < 10 |
| Interesse confirmado no beta — Q20 | >= 35% | 20% a 34,9% | < 20% |

A disposição para pagar da `Q21` será analisada separadamente e não definirá, isoladamente, a decisão da primeira rodada.

## 5. Gates críticos

Uma decisão `Go` exige todos os gates abaixo:

| Gate | Condição mínima |
|---|---|
| G1 — Base elegível | >= 200 respostas válidas |
| G2 — Compreensão | compreensão correta >= 80% |
| G3 — Problema | dor relevante >= 65% |
| G4 — Valor | relevância média >= 8,0 e ITP >= 8,0 |
| G5 — Confiança | confiança média >= 7,0 |
| G6 — Adoção | intenção positiva de uso >= 60% |
| G7 — Recorrência | uso recorrente esperado >= 50% |
| G8 — Qualidade | ausência de viés crítico não tratado |

O NPS conceitual e o interesse no beta reforçam a decisão, mas não compensam falha em compreensão, problema, confiança ou adoção.

## 6. Regra combinada de decisão

### 6.1 Go

Emitir `Go` quando:

- todos os gates críticos forem atendidos;
- pelo menos 8 dos 11 indicadores da tabela estiverem na faixa `Go`;
- nenhum indicador crítico estiver na faixa vermelha;
- o IGV for `>= 80`;
- não houver segmento majoritário com rejeição substancial ocultada pela média geral.

### 6.2 Go com ajustes

Emitir `Go com ajustes` quando:

- a base for elegível;
- nenhum gate estrutural estiver gravemente comprometido;
- o IGV estiver entre `70` e `79,9`; ou
- houver até três indicadores na faixa amarela e nenhum gate crítico vermelho;
- os ajustes necessários forem específicos e testáveis.

Também pode ocorrer com IGV acima de 80 quando houver concentração de amostra, forte divergência entre segmentos ou barreira crítica que exija correção antes do MVP.

### 6.3 Pivot parcial

Emitir `Pivot parcial` quando:

- a dor for relevante, mas compreensão, valor, confiança, adoção ou recorrência estiverem abaixo do necessário;
- o IGV estiver entre `55` e `69,9`;
- houver um segmento claramente promissor e outros com baixa aderência;
- a proposta atual precisar de mudança relevante, mas as evidências sustentarem continuidade da investigação.

### 6.4 No-Go temporário

Emitir `No-Go temporário` quando:

- dor relevante estiver abaixo de 50%; ou
- compreensão correta estiver abaixo de 65%; ou
- intenção positiva de uso estiver abaixo de 45%; ou
- confiança média estiver abaixo de 6,0; ou
- o IGV estiver abaixo de 55; ou
- a qualidade da base impedir interpretação confiável;
- não houver segmento com aderência suficiente para justificar pivot específico.

## 7. Regras de interpretação

1. Nenhum indicador isolado aprova a proposta.
2. Compreensão baixa invalida a interpretação de interesse alto.
3. Intenção declarada não equivale a comportamento real.
4. Uso recorrente esperado não equivale a retenção comprovada.
5. NPS conceitual não equivale a satisfação com produto em uso.
6. Interesse no beta deve ser comparado com a conversão real em contato e participação.
7. Disposição para pagar deve ser validada posteriormente por comportamento de compra.
8. Médias gerais não devem ocultar segmentos com resultados muito diferentes.
9. Resultados positivos em amostra concentrada não autorizam generalização nacional.
10. Evidência comportamental posterior poderá confirmar ou contrariar a pesquisa declarativa.

## 8. Matriz de diagnóstico

| Sinal observado | Leitura provável | Ação recomendada |
|---|---|---|
| Dor alta + compreensão baixa | O problema existe, mas a narrativa falha. | Reescrever apresentação e repetir teste de compreensão. |
| Dor alta + valor baixo | A solução proposta não responde bem ao problema. | Revisar proposta de valor e casos de uso. |
| Valor alto + confiança baixa | Interesse existe, mas o modelo de dados gera receio. | Reforçar controle, privacidade e transparência. |
| Valor alto + recorrência baixa | A proposta parece útil, mas episódica. | Revisar motivos de retorno e escopo inicial. |
| Uso alto + beta baixo | Curiosidade não se converte em compromisso. | Testar CTA, público e fricção de adesão. |
| Beta alto + pagamento baixo | Há potencial de uso, mas valor econômico ainda não está claro. | Validar produto gratuito e resultados antes do preço. |
| Médias boas + segmentos polarizados | A proposta atende nichos de forma desigual. | Priorizar segmento com melhor aderência. |
| Compreensão alta + dor baixa | A ideia é clara, mas o problema não é prioritário. | Revisar público, momento ou problema. |

## 9. Evidências obrigatórias para o registro da decisão

Cada rodada deverá registrar:

- identificação e período da rodada;
- quantidade recebida, concluída e válida;
- composição da amostra;
- origem dos respondentes;
- KPIs e respectivas faixas;
- IGV;
- gates atendidos e não atendidos;
- segmentos de maior e menor aderência;
- evidências favoráveis;
- evidências contrárias;
- barreiras principais;
- limitações e vieses;
- decisão aprovada;
- mudanças autorizadas;
- hipóteses para a próxima rodada;
- responsável e data.

## 10. Autoridade da decisão

O dashboard produz uma recomendação técnica. A decisão final deverá ser formalmente aprovada pela governança responsável da Guivos e registrada no GKR.

Qualquer decisão que contrarie os critérios objetivos deverá apresentar justificativa explícita, riscos assumidos e evidências adicionais.