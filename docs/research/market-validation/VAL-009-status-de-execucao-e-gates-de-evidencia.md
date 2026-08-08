---
id: VAL-009
title: Estado de Execução e Gates de Evidência da Validação de Mercado
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-08-08
depends_on:
  - VAL-001
  - VAL-002
  - VAL-004
  - VAL-005
  - VAL-006
  - VAL-007
  - VAL-008
related:
  - GKR-UPDATE-PROGRAM-001
  - GTM-000
normative: true
---

# VAL-009 — Estado de Execução e Gates de Evidência da Validação de Mercado

## 1. Finalidade

Este documento separa, de forma normativa, quatro estados que não podem ser confundidos na validação de mercado da Guivos:

```text
método definido
≠ instrumento pronto
≠ aplicação executada
≠ resultado validado
```

Seu objetivo é impedir que preparação metodológica, divulgação, intenção de coleta ou volume não auditado de respostas sejam apresentados como validação positiva da proposta.

## 2. Baseline metodológica vigente

Na `main` auditada em 2026-08-08, a Guivos já possui:

- `VAL-001` — framework de validação;
- `VAL-002` — pesquisa oficial B2C, versão documental 2.1.0;
- `VAL-003` — guia do entrevistador;
- `VAL-004` — consolidação e análise;
- `VAL-005` — plano de amostragem;
- `VAL-006` — dashboard/indicadores;
- `VAL-007` — critérios de decisão;
- `VAL-008` — sinais comportamentais.

A metodologia determina, entre outros:

- pesquisa conceitual B2C inicial;
- 19 perguntas;
- duração estimada de 3 a 5 minutos;
- pré-teste de 10 a 15 participantes antes da decisão formal;
- mínimo de 200 respostas válidas para decisão inicial;
- meta preferencial de 500 respostas válidas;
- análise por estado/região e segmentos;
- cálculo de IFO, compreensão, relevância, contribuição, intenção, interesse e IGV;
- decisão `Go`, `Go com ajustes`, `Pivot parcial` ou `No-Go temporário` somente após os gates aplicáveis.

Esses itens constituem **autoridade metodológica**, não resultado observado.

## 3. Estado factual reconciliado em 2026-08-08

| Objeto | Estado | O que pode ser afirmado |
|---|---|---|
| framework de validação | `documented_active` | existe método governado |
| instrumento B2C VAL-002 2.1.0 | `documented_active` | existe instrumento documental vigente |
| plano de amostragem | `documented_active` | existem regras e metas de amostra |
| critérios de decisão | `documented_active` | existem gates e faixas objetivas |
| pré-teste concluído | `evidence_pending` | não há evidência integrada suficiente para afirmar conclusão |
| formulário/plataforma de coleta efetivamente operacional | `evidence_pending` | eventual link ou comunicação não comprova operação, versão ou controle |
| período real de aplicação | `unknown` | não há registro integrado suficiente |
| respostas recebidas | `unknown` | nenhum número é promovido sem export/registro verificável |
| respostas válidas | `unknown` | depende de tratamento VAL-004/005 |
| KPIs calculados | `not_established` | não há cálculo integrado reproduzível |
| IGV calculado | `not_established` | não há cálculo integrado reproduzível |
| decisão de mercado | `not_authorized` | não há base integrada para Go/Go com ajustes/Pivot/No-Go |
| disposição a pagar | `not_tested_by_concept_survey` | permanece fora do instrumento conceitual |
| retenção/recorrência | `not_tested_by_concept_survey` | depende de comportamento posterior |

`evidence_pending` não significa que o evento não ocorreu; significa que **o GKR ainda não possui evidência suficiente para tratá-lo como fato governado**.

## 4. ChatsFontes e comunicação de pesquisa

Conversas históricas podem registrar:

- elaboração do convite para participar da pesquisa;
- intenção de aplicação;
- referência a endereço público de pesquisa;
- ajustes de duração e linguagem;
- intenção de validar inicialmente B2C.

Essas fontes são úteis para reconstruir contexto e decisões editoriais, mas não comprovam, por si só:

- que o endpoint estava operacional na data;
- que a versão publicada era exatamente VAL-002 2.1.0;
- quantidade de respostas;
- qualidade da amostra;
- conclusão do pré-teste;
- consentimento aplicado;
- resultado de KPI;
- aceitação de mercado.

Portanto, ChatsFontes entra como **proveniência histórica/contextual**, não como substituto dos dados de execução.

## 5. Gate E0 — identificação da rodada

Antes de incorporar qualquer resultado, criar uma identidade de rodada contendo:

- `round_id`;
- objetivo;
- público;
- território;
- versão exata do instrumento;
- canal/plataforma;
- data de abertura;
- data de fechamento ou corte;
- responsável;
- política de exclusão;
- versão do tratamento.

Sem `round_id`, resultados não devem ser misturados entre períodos ou versões.

## 6. Gate E1 — instrumento aplicado

Para marcar uma rodada como `instrument_deployed`, deve existir evidência suficiente de:

1. questionário efetivamente disponibilizado;
2. versão aplicada identificável;
3. lógica e perguntas reconciliáveis com VAL-002;
4. período de aplicação conhecido;
5. política de privacidade/consentimento aplicável conhecida;
6. canal de coleta identificado;
7. ausência de mudança silenciosa durante a rodada ou mapeamento de versões quando houver mudança.

Um link isolado não satisfaz o gate.

## 7. Gate E2 — pré-teste

Para registrar `pretest_completed`:

- 10 a 15 participantes conforme baseline vigente, salvo decisão metodológica posterior;
- data e versão conhecidas;
- duração observada;
- abandonos/problemas de compreensão registrados;
- problemas encontrados;
- alterações realizadas ou justificativa para nenhuma alteração;
- confirmação de que mudança material gerou nova versão quando aplicável.

Sem isso, o pré-teste permanece `evidence_pending`.

## 8. Gate E3 — base recebida

Para registrar respostas recebidas:

- export bruto preservado de forma apropriada;
- data/hora de corte;
- quantidade recebida;
- identificador anônimo ou mecanismo de deduplicação permitido;
- versão do instrumento por resposta quando houver mais de uma;
- origem/canal quando disponível;
- separação de contatos pessoais da base analítica quando aplicável.

O GKR não precisa armazenar dados pessoais brutos. Pode referenciar a evidência em repositório/sistema adequado.

## 9. Gate E4 — base válida

A quantidade de respostas válidas somente pode ser publicada após aplicação reproduzível das regras do VAL-004/VAL-005.

O registro deve apresentar:

```text
recebidas
- incompletas excluídas
- duplicadas/automatizadas excluídas
- incompatíveis excluídas ou segregadas
= válidas
```

Toda exclusão material deve possuir regra e contagem.

## 10. Gate E5 — qualidade da amostra

Antes de uma decisão formal:

- mínimo de 200 respostas válidas;
- diversidade mínima exigida por VAL-007;
- concentração por estado/canal identificada;
- estados com base pequena tratados adequadamente;
- participantes fora do Brasil segregados quando aplicável;
- vieses e limitações descritos;
- tempo e abandono avaliados.

500 respostas permanecem meta preferencial, não pré-condição absoluta quando VAL-007 autorizar decisão com 200+ válidas e demais gates satisfeitos.

## 11. Gate E6 — cálculo reproduzível

Cada KPI deve registrar:

- fórmula;
- numerador;
- denominador;
- exclusões;
- base elegível;
- valor;
- faixa VAL-007;
- segmentações relevantes.

IFO deve preservar Q8 e Q9 separadamente além da leitura composta.

IGV deve ser calculado conforme a autoridade vigente e não por média informal reconstruída posteriormente.

## 12. Gate E7 — decisão

Nenhuma decisão `Go`, `Go com ajustes`, `Pivot parcial` ou `No-Go temporário` pode ser registrada apenas com base em percepção geral.

A decisão exige:

- gates VAL-007 avaliados;
- KPIs e IGV reproduzíveis;
- evidências favoráveis e contrárias;
- limitações;
- segmentos divergentes;
- alcance territorial permitido da conclusão;
- autoridade humana responsável;
- data;
- ato recomendado para a próxima etapa.

Se a decisão humana contrariar o critério técnico, a divergência deve ser explícita.

## 13. Estados de maturidade da rodada

```text
planned
→ instrument_ready
→ instrument_deployed
→ pretest_completed
→ data_received
→ data_cleaned
→ metrics_calculated
→ decision_ready
→ decision_recorded
→ behavior_followup
```

Uma rodada pode permanecer em qualquer estágio sem que isso represente falha.

É proibido saltar documentalmente de `instrument_ready` para `decision_recorded`.

## 14. Evidência comportamental posterior

A pesquisa conceitual não comprova:

- ativação real;
- retenção;
- recorrência;
- recomendação espontânea;
- disposição efetiva para pagar;
- conversão comercial;
- impacto de evolução.

Esses itens devem usar beta, protótipo, comportamento, transação ou experimento apropriado.

## 15. Relação com GTM

GTM pode usar os resultados somente com rótulo compatível:

```text
candidate_target
≠ market_validated_target
≠ realized
```

A existência de targets GTM não deve ser usada para preencher lacunas da pesquisa. Da mesma forma, resultado positivo da pesquisa não transforma projeção de receita em realizado.

## 16. Próximo ato verificável

A próxima promoção factual do P4 depende de um pacote de evidência contendo, no mínimo:

1. rodada identificada;
2. versão aplicada;
3. evidência de pré-teste, se realizado;
4. export/contagem da base;
5. regras de limpeza;
6. composição da amostra;
7. KPIs calculados;
8. IGV;
9. gates;
10. decisão e limitações.

Até esse pacote existir, o GKR deve comunicar **metodologia pronta / execução e resultado pendentes de evidência**.
