---
id: VAL-007
title: Critérios de Decisão da Validação
status: active
version: 1.3.0
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
- KPIs principais;
- gates críticos;
- distribuição dos momentos atuais;
- diferenças entre segmentos;
- distribuição geográfica;
- evidências favoráveis e contrárias;
- limitações metodológicas;
- comentários qualitativos.

## 2. Elegibilidade para decisão

Uma rodada somente poderá receber decisão formal quando:

1. possuir pelo menos 200 respostas válidas;
2. tiver passado pelo pré-teste;
3. apresentar diversidade mínima por idade, estado e situação principal;
4. identificar concentração crítica em estado ou canal;
5. tiver a `Q11` classificada conforme a rubrica;
6. apresentar cálculo dos KPIs do VAL-006;
7. apresentar separadamente área, momento atual e mudança desejada;
8. registrar versão, exclusões, denominadores, limitações e vieses.

Bases menores podem gerar leitura exploratória ou indicativa, mas não decisão formal.

A ausência de respostas em todos os estados não impede decisão inicial, mas o alcance geográfico deverá ser declarado.

## 3. Estados possíveis

### 3.1 Go

A proposta apresenta evidências consistentes de:

- fricção relevante;
- compreensão adequada;
- relevância contextual;
- aplicações práticas reconhecíveis;
- contribuição percebida;
- intenção de experimentar;
- interesse real em aprofundar a validação;
- aderência em mais de um estágio de clareza ou recorte inicial explicitamente definido.

`Go` autoriza próxima etapa de validação ou MVP controlado. Não autoriza construir todo o ecossistema.

### 3.2 Go com ajustes

A proposta apresenta aderência promissora, mas exige correções específicas.

Os ajustes podem envolver:

- narrativa;
- público prioritário;
- estágio de clareza prioritário;
- proposta de valor;
- mecanismo de exploração;
- mecanismo de descoberta;
- adequação das oportunidades;
- situação de primeiro uso;
- escopo inicial;
- barreiras;
- canais;
- expansão geográfica.

### 3.3 Pivot parcial

Existe problema ou valor em segmento específico, mas parte relevante da solução, narrativa, público, estágio atendido, mecanismo de valor ou situação de uso precisa mudar.

O pivot deverá preservar evidências válidas e formular novas hipóteses.

### 3.4 No-Go temporário

As evidências são fracas, contraditórias, insuficientes ou metodologicamente inadequadas.

A decisão interrompe expansão de escopo e investimento relevante até novas hipóteses serem testadas.

## 4. Faixas oficiais por indicador

| Dimensão | Go | Go com ajustes | Pivot parcial / No-Go temporário |
|---|---:|---:|---:|
| IFO — Q8 + Q9 | >= 65% | 50% a 64,9% | < 50% |
| Esforço médio — Q10 | >= 6,0 | 5,0 a 5,9 | < 5,0 |
| Compreensão correta — Q11 | >= 80% | 65% a 79,9% | < 65% |
| Relevância contextual — Q12 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Contribuição percebida — Q16 | >= 8,0 | 7,0 a 7,9 | < 7,0 |
| Intenção positiva — Q17 | >= 60% | 45% a 59,9% | < 45% |
| Interesse confirmado — Q18 | >= 35% | 20% a 34,9% | < 20% |

Descoberta tardia e lacuna de adequação deverão ser exibidas separadamente.

Momento atual (`Q5`), mudança desejada (`Q6`), primeiro uso (`Q13`), expectativas (`Q14`), resultado concreto (`Q15`) e barreira (`Q19`) orientam diagnóstico, mas não possuem meta universal.

## 5. Gates críticos

Uma decisão `Go` exige:

| Gate | Condição mínima |
|---|---|
| G1 — Base elegível | >= 200 respostas válidas |
| G2 — Compreensão | compreensão correta >= 80% |
| G3 — Problema | IFO calculável e >= 65% |
| G4 — Valor | relevância >= 8,0 e contribuição >= 8,0 |
| G5 — Adoção | intenção positiva >= 60% |
| G6 — Qualidade | ausência de viés crítico não tratado |
| G7 — Cobertura | concentração geográfica identificada |
| G8 — Segmentação do momento | pessoas com e sem objetivo claro analisadas separadamente |

O interesse na primeira experiência reforça a decisão, mas não compensa falha em compreensão, problema, valor ou intenção.

Confiança operacional, recorrência, retenção, recomendação e monetização não integram os gates.

## 6. Regra combinada de decisão

### 6.1 Go

Emitir `Go` quando:

- todos os gates críticos forem atendidos;
- pelo menos 5 dos 7 indicadores estiverem na faixa `Go`;
- nenhum indicador crítico estiver vermelho;
- o IGV for `>= 80`;
- descoberta tardia e lacuna de adequação tiverem bases interpretáveis;
- não houver segmento majoritário com rejeição substancial ocultada pela média;
- o alcance geográfico estiver limitado à amostra;
- a proposta demonstrar valor para pessoas sem objetivo claro ou o MVP declarar explicitamente que atenderá outro estágio inicial.

### 6.2 Go com ajustes

Emitir `Go com ajustes` quando:

- a base for elegível;
- nenhum gate estrutural estiver gravemente comprometido;
- o IGV estiver entre `70` e `79,9`; ou
- houver até dois indicadores amarelos e nenhum gate crítico vermelho;
- os ajustes forem específicos e testáveis.

Também poderá ocorrer com IGV acima de 80 quando houver:

- concentração excessiva em um estado;
- segmentos polarizados;
- aderência restrita a um estágio de clareza;
- diferença relevante entre descoberta tardia e adequação;
- barreira crítica;
- compreensão desigual entre pessoas com e sem objetivo definido.

### 6.3 Pivot parcial

Emitir `Pivot parcial` quando:

- o IFO indicar problema, mas compreensão, aplicação prática, relevância, contribuição ou intenção estiverem abaixo do necessário;
- apenas um componente do IFO demonstrar fricção consistente;
- o IGV estiver entre `55` e `69,9`;
- houver segmento, área, estado ou estágio claramente promissor;
- a proposta atual precisar de mudança relevante.

### 6.4 No-Go temporário

Emitir `No-Go temporário` quando:

- IFO estiver abaixo de 50%; ou
- compreensão correta estiver abaixo de 65%; ou
- intenção positiva estiver abaixo de 45%; ou
- o IGV estiver abaixo de 55; ou
- IFO ou IGV não puder ser calculado por falha grave; ou
- a base impedir interpretação confiável; ou
- não houver segmento com aderência suficiente para pivot específico.

Relevância ou contribuição abaixo de 7,0 deverão gerar, no mínimo, investigação de pivot.

## 7. Regras de interpretação

1. Nenhum indicador isolado aprova a proposta.
2. Descoberta tardia e ausência de opção adequada representam problemas diferentes.
3. `Não procurei` não equivale a `não encontrei`.
4. `Não me recordo` não equivale a ausência do problema.
5. Oportunidade desconhecida não pode ser declarada perdida.
6. Ausência de objetivo claro não equivale a ausência de necessidade ou valor.
7. Exploração não equivale a compromisso de agir.
8. Compreensão baixa invalida interesse alto.
9. Intenção declarada não equivale a adoção.
10. Contribuição percebida não equivale a transformação.
11. Interesse inicial deverá ser comparado com conversão e participação real.
12. Situações de primeiro uso e resultados concretos orientam o MVP.
13. Preocupações com privacidade deverão ser registradas sem forçar confiança operacional.
14. Médias não deverão ocultar diferenças por momento atual.
15. Resultados positivos concentrados não autorizam generalização nacional.
16. Estados com menos de 30 respostas não recebem conclusão isolada.
17. Participantes fora do Brasil serão analisados separadamente.
18. Monetização deverá ser validada após demonstração de valor.
19. Evidência comportamental posterior poderá contrariar a pesquisa declarativa.

## 8. Matriz de diagnóstico

| Sinal observado | Leitura provável | Ação |
|---|---|---|
| Descoberta tardia alta + adequação alta | Fricção simultânea de timing e compatibilidade | Priorizar descoberta contextual e matching |
| Descoberta tardia alta + adequação baixa | Problema principal de acesso ou timing | Priorizar alertas e descoberta antecipada |
| Descoberta tardia baixa + adequação alta | Opções existem, mas não fazem sentido | Priorizar contexto e filtragem |
| IFO alto + compreensão baixa | Problema existe, narrativa falha | Reescrever apresentação |
| Muitas pessoas sem direção + relevância alta | Valor pode começar pela exploração, não pelo objetivo | Priorizar compreensão do momento e possibilidades |
| Objetivo claro + relevância alta | Valor pode estar em ação e oportunidade | Priorizar caminhos e oportunidades |
| Pessoas sem direção + compreensão baixa | Texto ainda exige autoconhecimento implícito | Simplificar narrativa e exemplos |
| Compreensão alta + primeiro uso baixo | Ideia clara, aplicação pouco evidente | Refinar casos de uso |
| Relevância alta + contribuição baixa | Interesse sem impacto percebido | Revisar mecanismo de valor |
| Contribuição alta + intenção baixa | Valor reconhecido com barreira de adoção | Investigar esforço, dados e formato |
| Intenção alta + participação baixa | Curiosidade não vira compromisso | Testar CTA e experiência inicial |
| Expectativa concentrada em uma função | MVP pode ser mais focado | Priorizar função e testar profundidade |
| Barreiras concentradas em dados | Receio sobre informações pessoais | Testar consentimento e controle |
| Barreira de esforço inicial alta | Onboarding pode parecer pesado | Reduzir exigência de reflexão e cadastro |
| Médias boas + estados polarizados | Aderência geográfica desigual | Investigar diferenças |
| Compreensão alta + IFO baixo | Fricção investigada pode não ser prioritária | Revisar público ou problema |

## 9. Evidências obrigatórias

Cada rodada deverá registrar:

- identificação e período;
- versão do instrumento;
- quantidade recebida, concluída e válida;
- composição da amostra;
- distribuição geográfica;
- origem dos respondentes;
- bases de Q8 e Q9;
- descoberta tardia, adequação e IFO;
- KPIs e faixas;
- IGV;
- gates;
- áreas prioritárias;
- momentos atuais;
- mudanças desejadas;
- cruzamentos entre área, momento e mudança;
- situações de primeiro uso;
- segmentos de maior e menor aderência;
- evidências favoráveis e contrárias;
- barreiras;
- limitações e vieses;
- alcance geográfico;
- decisão;
- mudanças autorizadas;
- hipóteses seguintes;
- responsável e data.

## 10. Autoridade da decisão

O dashboard produz recomendação técnica. A decisão final deverá ser aprovada pela governança responsável e registrada no GKR.

Qualquer decisão que contrarie os critérios deverá apresentar justificativa, riscos e evidências adicionais.

## 11. Compatibilidade

A versão `1.3.0` acompanha o VAL-002 `2.0.0`.

Critérios anteriores não deverão ser aplicados diretamente a bases da nova versão sem atualização do dashboard e da rubrica.
