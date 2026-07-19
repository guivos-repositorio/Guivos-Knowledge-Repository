---
id: VAL-001
title: Framework de Validação de Mercado da Guivos
status: active
version: 1.3.1
owner: Guivos
last_updated: 2026-07-19
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

Estabelecer o método oficial para validar hipóteses de mercado da Guivos antes de decisões relevantes de produto, posicionamento, experiência, adoção e monetização.

A validação deverá respeitar o conhecimento que cada participante possui sobre a Guivos e sobre a própria situação. A primeira pesquisa conceitual não poderá pressupor objetivo, plano ou próximo passo previamente definidos.

## 2. Princípio da Evidência de Mercado

> Nenhuma decisão estratégica de produto será considerada definitiva apenas por consenso interno. Sempre que possível, deverá ser confrontada com evidências obtidas por pesquisa, experimentação ou comportamento real.

## 3. Princípio da Co-criação

> A Guivos será construída com base em evidências e na participação das pessoas. A validação não existe para confirmar hipóteses internas, mas para revelar o que faz sentido, o que não faz e o que precisa ser ajustado.

A pesquisa também é uma experiência de marca. Deve representar a Guivos com clareza, simplicidade, respeito, transparência e ausência de pressão comercial.

## 4. Princípio da Avaliabilidade

> Uma pergunta somente deverá integrar uma rodada quando o participante possuir informação suficiente para avaliá-la de forma minimamente consciente.

Dimensões dependentes de experiência real — como confiança operacional, recorrência, retenção, satisfação, recomendação e disposição efetiva para pagar — deverão ser priorizadas em protótipos, testes controlados, beta ou produto em uso.

## 5. Princípio da Brevidade Útil

> A pesquisa deverá coletar somente o necessário para apoiar decisões reais, com o menor esforço possível para o participante.

A brevidade não significa superficialidade. Significa distribuir a validação entre instrumentos adequados:

- pesquisa quantitativa curta;
- entrevistas qualitativas;
- pré-teste;
- primeira experiência;
- evidência comportamental;
- testes posteriores de produto e monetização.

O questionário público não deverá tentar executar todas essas funções ao mesmo tempo.

## 6. Escopo da fase inicial

A primeira rodada valida exclusivamente a proposta B2C da Guivos.

Serão avaliados:

1. descoberta tardia de oportunidades potencialmente úteis;
2. ausência de opções adequadas ao momento do participante;
3. esforço atual para encontrar algo relevante;
4. clareza do momento atual e da mudança desejada;
5. compreensão da proposta;
6. relevância para a área escolhida;
7. situação prática de primeiro uso;
8. resultados considerados úteis;
9. contribuição percebida;
10. intenção de experimentar uma primeira versão;
11. interesse em participar de uma primeira experiência;
12. barreiras e diferenças entre segmentos.

Esta rodada não valida produto em uso, confiança operacional comprovada, recorrência, retenção, receita real, usabilidade, arquitetura técnica ou adequação jurídica definitiva.

## 7. Hipóteses centrais

| ID | Hipótese |
|---|---|
| H1 | Pessoas conhecem tarde demais oportunidades que poderiam contribuir para suas necessidades ou objetivos. |
| H2 | Pessoas procuram possibilidades, mas não encontram opções compatíveis com seu tempo, localização, orçamento ou necessidade. |
| H3 | Pessoas possuem diferentes níveis de clareza e nem sempre sabem exatamente o que desejam. |
| H4 | Uma plataforma que compreenda o momento e apresente possibilidades contextualizadas gera valor percebido. |
| H5 | A proposta pode ser compreendida por meio de uma apresentação curta, direta e não promocional. |
| H6 | As pessoas conseguem reconhecer situações concretas em que procurariam a Guivos. |
| H7 | Compreensão do momento, exploração de possibilidades, organização de caminhos e descoberta contextual são percebidas como úteis. |
| H8 | Uma parcela relevante pretende experimentar uma primeira versão e aceita participar de uma experiência inicial. |

## 8. Método em quatro etapas

### 8.1 Pré-teste

Aplicar o VAL-002 com 10 a 15 pessoas para identificar:

- confusão;
- duração excessiva;
- abandono;
- perguntas enviesadas;
- excesso de alternativas;
- alternativas redundantes ou ausentes;
- dificuldade de leitura;
- interpretação incorreta da apresentação;
- falhas de numeração ou lógica.

O pré-teste valida o instrumento, não a aceitação da Guivos.

### 8.2 Entrevistas qualitativas

Realizar inicialmente 20 a 30 entrevistas semiestruturadas, ampliando até saturação dos padrões.

As entrevistas deverão seguir o VAL-003 e registrar sinais comportamentais conforme o VAL-008.

### 8.3 Questionário quantitativo

Aplicar o VAL-002 a:

- mínimo de 200 respostas válidas para decisão inicial;
- meta preferencial de 500 respostas válidas para maior estabilidade e segmentação.

A composição da amostra deverá seguir o VAL-005.

### 8.4 Evidência comportamental

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

## 9. Instrumento oficial

O instrumento oficial da primeira rodada é:

- **Documento interno:** `VAL-002 — Pesquisa Oficial B2C da Guivos`;
- **Título público:** `Construindo a Guivos`;
- **Versão:** `2.1.0`;
- **Tempo estimado:** 3 a 5 minutos;
- **Perguntas principais:** 19;
- **Perguntas abertas:** `Q11` obrigatória e `Q19` opcional;
- **Escolhas múltiplas:** somente `Q7` e `Q14`, com até duas seleções;
- **Contato:** opcional, condicional e excluído dos KPIs.

## 10. Ordem lógica da pesquisa

```mermaid
flowchart LR
    A["Perfil mínimo"] --> B["Área, momento e mudança desejada"] --> C["Dificuldades e oportunidades"] --> D["Apresentação curta da Guivos"] --> E["Compreensão"] --> F["Aplicação e valor"] --> G["Intenção"] --> H["Barreiras e comentário final"]
```

Perguntas sobre valor e intenção não devem preceder a apresentação oficial da proposta.

## 11. Indicadores oficiais

| Indicador | Fonte | Meta inicial |
|---|---|---:|
| Índice de Fricção de Oportunidades — IFO | Q8 + Q9 | >= 65% |
| Esforço atual | Q10 | >= 6,0/10 indica problema relevante |
| Compreensão correta | Q11 | >= 80% |
| Relevância contextual | Q12 | >= 8,0/10 |
| Contribuição percebida | Q15 | >= 8,0/10 |
| Intenção positiva de experimentar | Q16 | >= 60% |
| Interesse confirmado na primeira experiência | Q17 | >= 35% |

O IFO combina descoberta tardia (`Q8`) e ausência de opção adequada após busca (`Q9`). Os dois componentes deverão ser apresentados separadamente.

Momento atual (`Q5`), mudança desejada (`Q6`), dificuldades (`Q7`), situação de primeiro uso (`Q13`), utilidade esperada (`Q14`) e barreira principal (`Q18`) são indicadores diagnósticos.

As fórmulas, segmentações e regras de exibição estão no VAL-006.

## 12. Critérios de decisão

Os resultados serão classificados como:

- `Go`;
- `Go com ajustes`;
- `Pivot parcial`;
- `No-Go temporário`.

Nenhuma decisão formal poderá ser emitida apenas por média geral ou por um único indicador. A decisão deverá seguir os gates e regras combinadas do VAL-007.

## 13. Princípios de qualidade

- conversar diretamente com o participante usando linguagem simples;
- utilizar “você” nos enunciados públicos;
- redigir alternativas como voz do participante quando aplicável;
- limitar cada pergunta a uma ideia principal;
- evitar enunciados longos;
- evitar alternativas excessivas ou muito semelhantes;
- manter exemplos curtos;
- não vender durante a pesquisa;
- não sugerir que existe resposta desejada;
- medir somente situações que a pessoa possa reconhecer ou recordar;
- separar comportamento passado de intenção futura;
- distinguir ausência de busca de ausência de opção adequada;
- preservar respostas negativas e objeções;
- não tratar intenção declarada como adoção comprovada;
- não tratar contribuição percebida como transformação real;
- analisar segmentos separadamente;
- registrar origem, limitações e possíveis vieses da amostra;
- excluir perguntas que não influenciem decisões futuras.

## 14. Saídas obrigatórias de cada rodada

1. base bruta preservada;
2. base tratada com critérios de exclusão;
3. dashboard conforme VAL-006;
4. análise qualitativa conforme VAL-004;
5. hipóteses validadas, parciais ou rejeitadas;
6. segmentos de maior e menor aderência;
7. leitura separada de descoberta tardia e lacuna de adequação;
8. níveis de clareza e mudanças desejadas prioritárias;
9. situações de primeiro uso prioritárias;
10. resultados considerados úteis;
11. evidências favoráveis e contrárias;
12. decisão conforme VAL-007;
13. recomendações de ajuste;
14. limitações;
15. plano da próxima rodada.

## 15. Limites

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

## 16. Regra de evolução

Qualquer alteração em pergunta, alternativa, cálculo, meta ou critério de decisão deverá:

1. ser versionada;
2. registrar o motivo;
3. preservar comparabilidade quando possível;
4. indicar impactos sobre rodadas anteriores;
5. atualizar conjuntamente VAL-002, VAL-004, VAL-006 e VAL-007 quando houver dependência;
6. passar por novo pré-teste quando alterar carga de leitura, quantidade de alternativas ou interpretação das perguntas.
