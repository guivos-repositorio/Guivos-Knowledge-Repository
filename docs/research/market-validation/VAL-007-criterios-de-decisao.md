---
id: VAL-007
title: Critérios de Decisão da Validação
status: active
version: 1.2.1
owner: Guivos
last_updated: 2026-07-12
related:
  - VAL-001
  - VAL-002
  - VAL-005
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
- distribuição geográfica por estado ou Distrito Federal;
- evidências favoráveis e contrárias;
- limitações metodológicas;
- comentários qualitativos relevantes.

## 2. Elegibilidade para decisão

Uma rodada somente poderá receber decisão formal quando:

1. possuir pelo menos 200 respostas válidas;
2. tiver passado pelo pré-teste do instrumento;
3. apresentar distribuição mínima por idade, estado ou Distrito Federal e situação principal;
4. identificar e tratar concentração crítica em um único estado ou canal de aquisição;
5. tiver a `Q12` classificada conforme a rubrica de compreensão;
6. apresentar cálculo completo dos KPIs do VAL-006, incluindo os dois componentes do IFO;
7. registrar versão do instrumento, exclusões, denominadores, limitações e possíveis vieses.

Bases com menos de 200 respostas podem gerar leitura exploratória ou indicativa, mas não decisão formal.

A ausência de respostas em todos os estados não impede uma decisão inicial. Entretanto, a decisão deverá declarar claramente o alcance geográfico da amostra e não poderá ser apresentada como validação nacional quando houver concentração relevante em poucas unidades federativas.

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

Os ajustes podem envolver narrativa, público prioritário, proposta de valor, mecanismo de descoberta, adequação das oportunidades, situação de primeiro uso, escopo inicial, barreiras, monetização, canais de aquisição ou expansão geográfica.

### 3.3 Pivot parcial

Existe fricção de oportunidade, porém uma parte relevante da solução, narrativa, público, mecanismo de valor, situação de uso ou contribuição esperada precisa mudar.

O pivot deverá preservar as evidências válidas e formular novas hipóteses testáveis.

### 3.4 No-Go temporário

As evidências são fracas, contraditórias, insuficientes ou metodologicamente inadequadas.

A decisão interrompe expansão de escopo e investimento relevante até que novas hipóteses sejam formuladas e testadas.

`No-Go temporário` não significa encerramento definitivo da Guivos. Significa que a hipótese ou a forma atual de apresentá-la não foi suficientemente validada.

## 4. Faixas oficiais por indicador

| Dimensão | Go | Go com ajustes | Pivot parcial / No-Go temporário |
|---|---:|---:|---:|
| IFO — Q8 + Q9 | >= 65% | 50% a 64,9% | < 50% |
| Esforço médio — Q10 | >= 6,0 | 5,0 a 5,9 | < 5,0 |
| Compreensão autodeclarada — Q11 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Compreensão correta — Q12 | >= 80% | 65% a 79,9% | < 65% |
| Relevância contextual — Q13 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Contribuição percebida — Q17 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Intenção positiva de experimentar — Q18 | >= 60% | 45% a 59,9% | < 45% |
| Interesse confirmado na primeira experiência — Q19 | >= 35% | 20% a 34,9% | < 20% |

A disposição para pagar da `Q21` será analisada separadamente e não definirá, isoladamente, a decisão da primeira rodada.

Descoberta tardia (`Q8`) e lacuna de adequação (`Q9`) deverão ser exibidas separadamente, mesmo quando consolidadas no IFO.

Situação de primeiro uso (`Q14`), expectativas sobre a plataforma (`Q15`), resultado concreto de valor (`Q16`) e barreira principal (`Q20`) deverão orientar a interpretação e os ajustes, mas não possuem meta universal única nesta rodada.

## 5. Gates críticos

Uma decisão `Go` exige todos os gates abaixo:

| Gate | Condição mínima |
|---|---|
| G1 — Base elegível | >= 200 respostas válidas |
| G2 — Compreensão | compreensão correta >= 80% |
| G3 — Problema | IFO calculável e >= 65% |
| G4 — Valor | relevância contextual >= 8,0 e contribuição percebida >= 8,0 |
| G5 — Adoção | intenção positiva de experimentar >= 60% |
| G6 — Qualidade | ausência de viés crítico não tratado e denominadores explicitados |
| G7 — Cobertura geográfica | concentração por estado identificada e considerada na decisão |

O interesse na primeira experiência reforça a decisão, mas não compensa falha em compreensão, problema, valor ou intenção.

Confiança operacional, recorrência, retenção e recomendação não integram os gates desta rodada porque dependem de experiência real com a plataforma.

## 6. Regra combinada de decisão

### 6.1 Go

Emitir `Go` quando:

- todos os gates críticos forem atendidos;
- pelo menos 6 dos 8 indicadores estiverem na faixa `Go`;
- nenhum indicador crítico estiver na faixa vermelha;
- o IGV for `>= 80`;
- descoberta tardia e lacuna de adequação tiverem bases interpretáveis;
- não houver segmento majoritário com rejeição substancial ocultada pela média geral;
- o alcance geográfico da conclusão estiver explicitamente limitado à composição da amostra.

### 6.2 Go com ajustes

Emitir `Go com ajustes` quando:

- a base for elegível;
- nenhum gate estrutural estiver gravemente comprometido;
- o IGV estiver entre `70` e `79,9`; ou
- houver até três indicadores na faixa amarela e nenhum gate crítico vermelho;
- os ajustes necessários forem específicos e testáveis.

Também pode ocorrer com IGV acima de 80 quando houver concentração excessiva em um estado, forte divergência entre unidades federativas, segmentos polarizados, diferença relevante entre descoberta tardia e lacuna de adequação ou barreira crítica que exija correção antes do MVP.

### 6.3 Pivot parcial

Emitir `Pivot parcial` quando:

- o IFO indicar problema, mas compreensão, aplicação prática, relevância, contribuição ou intenção estiverem abaixo do necessário;
- apenas um dos componentes do IFO demonstrar fricção consistente;
- o IGV estiver entre `55` e `69,9`;
- houver um segmento, área ou estado claramente promissor e outros com baixa aderência;
- a proposta atual precisar de mudança relevante, mas as evidências sustentarem continuidade da investigação.

### 6.4 No-Go temporário

Emitir `No-Go temporário` quando:

- IFO estiver abaixo de 50%; ou
- compreensão correta estiver abaixo de 65%; ou
- intenção positiva de experimentar estiver abaixo de 45%; ou
- o IGV estiver abaixo de 55; ou
- IFO ou IGV não puder ser calculado por falha grave da base; ou
- a qualidade da base impedir interpretação confiável; ou
- não houver segmento com aderência suficiente para justificar pivot específico.

Relevância ou contribuição abaixo de 7,0 deverão gerar, no mínimo, investigação de pivot. A classificação final dependerá da combinação com IFO, compreensão e intenção.

## 7. Regras de interpretação

1. Nenhum indicador isolado aprova a proposta.
2. Descoberta tardia e ausência de oportunidade adequada representam problemas diferentes e não deverão ser fundidas sem leitura separada.
3. `Não procurei oportunidades` não equivale a `não encontrei oportunidade adequada`.
4. `Não me recordo` não deverá ser tratado como ausência do problema.
5. Oportunidades que nunca chegaram ao conhecimento do participante não podem ser declaradas como perdidas por ele.
6. Compreensão baixa invalida a interpretação de interesse alto.
7. Intenção declarada não equivale a adoção comprovada.
8. Contribuição percebida não equivale a transformação real.
9. Interesse na primeira experiência deve ser comparado com conversão em contato e participação efetiva.
10. Disposição para pagar deve ser validada posteriormente por comportamento de compra.
11. Situações de primeiro uso e resultados concretos devem orientar o recorte do MVP.
12. Preocupações espontâneas com privacidade ou confiança devem ser registradas, mas não transformadas em gate operacional antes de existir experiência demonstrável.
13. Médias gerais não devem ocultar segmentos ou estados com resultados muito diferentes.
14. Resultados positivos em amostra concentrada não autorizam generalização nacional.
15. Estados com menos de 30 respostas não deverão receber conclusão isolada.
16. Participantes fora do Brasil deverão ser analisados separadamente da base nacional.
17. Evidência comportamental posterior poderá confirmar ou contrariar a pesquisa declarativa.

## 8. Matriz de diagnóstico

| Sinal observado | Leitura provável | Ação recomendada |
|---|---|---|
| Descoberta tardia alta + lacuna de adequação alta | Existe fricção simultânea de acesso no tempo certo e de compatibilidade com o momento. | Priorizar descoberta contextual e matching no MVP. |
| Descoberta tardia alta + lacuna de adequação baixa | O principal problema parece ser acesso ou timing, não falta de opções compatíveis. | Priorizar alertas, distribuição e descoberta antecipada. |
| Descoberta tardia baixa + lacuna de adequação alta | As pessoas encontram opções, mas elas não fazem sentido para seu contexto. | Priorizar compreensão do momento, filtragem e adequação. |
| IFO alto + compreensão baixa | O problema existe, mas a narrativa falha. | Reescrever apresentação e repetir teste de compreensão. |
| Compreensão alta + primeiro uso pouco reconhecido | A ideia é clara, mas a aplicação prática não está evidente. | Refinar casos de uso e apresentação do MVP. |
| Relevância alta + contribuição baixa | A proposta interessa, mas não demonstra impacto suficiente. | Revisar mecanismo de valor e resultados prometidos. |
| Contribuição alta + intenção baixa | A pessoa reconhece valor, mas existe fricção ou barreira de adoção. | Investigar barreiras, formato e esforço inicial. |
| Intenção alta + participação inicial baixa | Curiosidade não se converte em compromisso. | Testar CTA, proposta da primeira experiência e fricção de adesão. |
| Expectativa concentrada em uma função | O valor inicial pode estar mais focado do que o ecossistema completo. | Priorizar a função no MVP e testar profundidade. |
| Barreiras concentradas em compreensão do momento ou dados | Existe receio sobre funcionamento e informações pessoais. | Testar protótipo de consentimento, controle e explicabilidade. |
| Participação alta + pagamento baixo | Há potencial de uso, mas valor econômico ainda não está claro. | Validar resultados antes do preço. |
| Médias boas + estados polarizados | A proposta apresenta aderência geográfica desigual. | Investigar diferenças e limitar a conclusão ao alcance da amostra. |
| Compreensão alta + IFO baixo | A ideia é clara, mas a fricção investigada não é prioritária. | Revisar público, momento ou problema. |

## 9. Evidências obrigatórias para o registro da decisão

Cada rodada deverá registrar:

- identificação e período da rodada;
- versão do instrumento;
- quantidade recebida, concluída e válida;
- composição da amostra;
- distribuição por estado ou Distrito Federal;
- consolidação por região;
- origem dos respondentes;
- bases elegíveis de Q8 e Q9;
- descoberta tardia, lacuna de adequação e IFO;
- KPIs e respectivas faixas;
- IGV;
- gates atendidos e não atendidos;
- áreas, resultados desejados e situações de primeiro uso prioritários;
- segmentos e estados de maior e menor aderência;
- evidências favoráveis;
- evidências contrárias;
- barreiras principais;
- limitações e vieses;
- alcance geográfico permitido para a conclusão;
- decisão aprovada;
- mudanças autorizadas;
- hipóteses para a próxima rodada;
- responsável e data.

## 10. Autoridade da decisão

O dashboard produz uma recomendação técnica. A decisão final deverá ser formalmente aprovada pela governança responsável da Guivos e registrada no GKR.

Qualquer decisão que contrarie os critérios objetivos deverá apresentar justificativa explícita, riscos assumidos e evidências adicionais.