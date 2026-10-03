---
id: RP-002-PILOT-METHOD-FREEZE-001
title: Piloto — Congelamento Metodológico e Plano de Análise do Dry Run
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: dry_run_method_frozen_pre_execution
related:
  - RP-002-PMF-001
  - RP-002-PILOT-OP-001
  - RP-002-PILOT-DOC-CLOSE-REVIEW-001
---

# Piloto — Congelamento Metodológico e Plano de Análise do Dry Run

## 1. Finalidade

Este documento congela a versão metodológica que deverá reger o primeiro Dry Run Real do `RP-002` quando — e somente quando — a fase operacional for deliberadamente aberta e os gates de liberação estiverem satisfeitos.

Ele não inicia o Dry Run, não libera participante real e não promove PMF.

```text
FIELD KIT
→ v0.1 FROZEN FOR FIRST DRY RUN

DRY RUN SIZE
→ 6 REAL EPISODES WHEN OPERATIONALLY RELEASED

OPERATIONAL IMPLEMENTATION
→ DEFERRED

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED

PMF
→ NOT VALIDATED
```

O objetivo do freeze é impedir que perguntas, critérios, gates, métricas ou regras de decisão sejam alterados silenciosamente depois que os resultados começarem a aparecer.

## 2. Princípio de governança experimental

O Dry Run existe para tentar encontrar falhas no mecanismo da Guivos antes da amostra principal e antes de escala.

Regra:

> **A metodologia não deve se mover para proteger a tese.**

Uma mudança pode ser necessária, mas deve ser explícita, versionada e associada aos episódios afetados.

```text
RESULTADO DESFAVORÁVEL
≠ PERMISSÃO PARA MUDAR CRITÉRIO RETROATIVAMENTE

MUDANÇA METODOLÓGICA
→ NEW VERSION
→ MOTIVE RECORDED
→ AFFECTED EPISODES RECORDED
→ COMPARABILITY LIMIT EXPLICIT
```

## 3. Escopo congelado

Esta versão congela para o primeiro Dry Run:

1. população e exclusões;
2. tamanho do Dry Run;
3. perguntas centrais da entrevista;
4. revisão do Momento `A/B/C/D`;
5. modos experimentais;
6. regra de profundidade proporcional;
7. uso de Possibilidades;
8. Preference Checkpoint;
9. Opportunity QA;
10. gates `G1–G10`;
11. critérios de seleção por modo;
12. papéis contextuais da oportunidade;
13. entrega Guivos;
14. benchmark controlado;
15. benchmark ecológico;
16. estados de ação;
17. follow-ups;
18. estados da experiência;
19. pós-experiência;
20. `Evidence Guivos EG-0..EG-5`;
21. Novo Momento;
22. Longitudinal Lift quando aplicável;
23. métricas e denominadores;
24. stop rules;
25. protocolo de desvio e missingness;
26. saída GO / REVISE / STOP / INCONCLUSIVE.

## 4. Unidade de análise

A unidade metodológica permanece o `Episódio de Jornada em Validação`:

```text
Pessoa
+
Momento real
+
necessidade / incerteza / direção
+
Possibilidades quando úteis
+
Oportunidades avaliadas
+
ação / não ação
+
experiência quando houver
+
contribuição posterior
```

O Episódio é unidade experimental e não entidade canônica da Guivos.

## 5. Hipótese-mãe

A hipótese permanece:

> **Quando uma Pessoa vive um Momento relevante de incerteza, decisão ou transição, a Guivos consegue compreender suficientemente esse contexto, tornar caminhos plausíveis visíveis, encontrar oportunidades reais e acessíveis, explicar por que fazem sentido e produzir valor suficiente para que a Pessoa aja e queira continuar sua Journey depois da experiência.**

Estado:

```text
HYPOTHESIS
→ FROZEN FOR TESTING

FIELD EVIDENCE
→ NOT YET AVAILABLE
```

## 6. Árvore de hipóteses observada

O Dry Run deve conseguir produzir evidência ou contraevidência para:

- `H1 — Problema`;
- `H2 — Compreensão do Momento`;
- `H3 — Valor da Possibilidade`;
- `H4 — Supply real`;
- `H5 — Gates`;
- `H6 — Fit contextual`;
- `H7 — Superioridade de decisão`;
- `H8 — Ação`;
- `H9 — Experiência`;
- `H10 — Pós-experiência`;
- `H11 — Continuidade` quando legitimamente observável;
- `H12 — Confiança`;
- `H13 — Valor econômico` apenas se surgir compromisso econômico real; o Dry Run não deve fabricar esse sinal.

Nem toda hipótese precisa ser resolvida em seis episódios.

## 7. Tamanho do Dry Run

Tamanho congelado:

```text
N = 6 REAL EPISODES
```

Função do `N=6`:

- detectar falhas operacionais e metodológicas;
- verificar se métricas podem ser observadas de forma confiável;
- identificar etapas excessivamente custosas ou invasivas;
- detectar gate escapes;
- testar benchmark e cegamento;
- testar se follow-up é operacionalmente viável;
- gerar decisão sobre revisão do método antes da amostra principal.

Não usar `N=6` para reivindicar PMF estatístico.

O tamanho de eventual amostra principal não é definido por este documento e deverá ser aprovado separadamente depois do relatório do Dry Run.

## 8. Cobertura desejada dos seis Episódios

A seleção deve buscar diversidade metodológica, sem transformar cobertura em quota rígida quando isso criar episódio artificial.

Target:

- pelo menos `1` episódio `Direct`;
- pelo menos `2` episódios `Exploratory` ou com baixa direção inicial;
- pelo menos `2` episódios `Decisional`;
- `Longitudinal` somente se histórico anterior existir legitimamente e alterar materialmente a análise;
- diversidade entre Famílias A, B e C;
- Família D somente quando segura e operacionalmente adequada.

O modo pertence ao Episódio, não à identidade da Pessoa.

## 9. População inicial

Adultos `18+` vivendo Momentos reais em territórios de menor risco regulatório.

Famílias:

```text
A — trabalho / carreira / aprendizagem
B — descoberta / novas experiências
C — comunidade / participação / contribuição
D — decisão contextual segura
```

Exclusões permanecem:

- menores de idade;
- emergência ou crise aguda;
- violência ou risco imediato;
- aconselhamento clínico individual;
- diagnóstico;
- decisão jurídica individual complexa;
- recomendação financeira de alto risco;
- imigração complexa com consequência jurídica material;
- inferência religiosa não autorizada;
- episódio considerado inadequado pelo Safety Owner.

## 10. Perguntas centrais congeladas

A entrevista proporcional parte das seguintes perguntas:

1. O que está acontecendo hoje que torna essa questão importante?
2. Por que isso é relevante agora?
3. O que você está tentando compreender, decidir ou fazer?
4. O que já tentou?
5. Onde procurou ajuda ou informação?
6. O que foi mais difícil?
7. Existe alguma condição que faria uma alternativa não funcionar?
8. O que seria especialmente importante para funcionar bem?
9. Se encontrássemos algo adequado, você poderia agir nas próximas semanas?
10. Existe algo material que não perguntamos?

A formulação conversacional pode variar para fluidez, mas o construto medido não deve ser alterado silenciosamente.

## 11. Profundidade proporcional

```text
NÍVEL 0 — factual
NÍVEL 1 — contextual
NÍVEL 2 — decisório
NÍVEL 3 — longitudinal
```

Regra congelada:

> **subir de nível somente quando a informação adicional puder alterar materialmente o valor entregue.**

`Context Cost` deve observar quando o esforço de captura deixa de ser proporcional ao benefício.

## 12. Revisão do Momento

A síntese precisa voltar à Pessoa antes de pesquisa de supply.

Classificação:

```text
A — precisa
B — suficientemente precisa
C — correção material
D — falha de compreensão
```

Regra:

```text
A/B
→ pode prosseguir

C/D
→ supply bloqueado até correção
```

A classificação deve registrar a avaliação da Pessoa sobre a síntese, não a autoconfiança do operador Guivos.

## 13. Modos experimentais

### Direct

Direção clara e baixa incerteza sobre o que se busca.

### Exploratory

Desejo de descobrir ou experimentar sem direção consolidada.

### Decisional

Alternativas e trade-offs materiais já estão presentes.

### Longitudinal

Histórico anterior altera materialmente a orientação atual.

Os modos continuam experimentais e não são taxonomia canônica de Pessoas.

## 14. Possibilidades

A camada de Possibilidade é usada somente quando agrega valor entre Momento e oportunidade.

Target:

```text
2–4 POSSIBILITIES WHEN ABSTRACTION IS USEFUL
```

Cada Possibilidade deve registrar:

- descrição;
- contribuição pretendida;
- mecanismos;
- condições de fit;
- condições de não fit;
- independência de provider;
- valor da abstração.

Pergunta de validação:

> **Isso faz sentido para você considerar agora?**

Não forçar Possibilidade quando a intenção já é suficientemente direta.

## 15. Preference Checkpoint

Quando duas ou mais experiências passam pelos gates e uma preferência material alteraria a seleção, perguntar:

> **Entre esses tipos de experiência, algum desperta mais ou menos interesse?**

Não transformar o checkpoint em inventário antecipado de gostos.

## 16. Opportunity QA

Para cada oportunidade candidata relevante, registrar no mínimo:

- identidade da oportunidade;
- responsável/provider;
- fonte;
- timestamp de verificação;
- descrição;
- modalidade;
- território;
- período/prazo;
- horário quando material;
- custo;
- elegibilidade;
- disponibilidade;
- idioma;
- carga;
- acessibilidade conhecida;
- restrições;
- Possibilidade relacionada quando aplicável;
- mecanismos;
- Evidência Externa;
- limitações;
- relação comercial;
- incertezas materiais.

## 17. Gates congelados

```text
G1 — existe?
G2 — responsável identificável?
G3 — fonte / legitimidade suficiente?
G4 — disponível no período relevante?
G5 — elegibilidade compatível?
G6 — acesso viável?
G7 — risco / restrições aceitáveis?
G8 — materializa caminho legítimo?
G9 — relação comercial transparente?
G10 — informação suficiente para explicação honesta?
```

Regra:

> **`UNKNOWN` material permanece visível e pode bloquear apresentação.**

Um gate crítico omitido que posteriormente se revele incompatível deve entrar em `Gate Escape Rate` e em log de falha.

## 18. Seleção por modo

### Direct

Priorizar:

- compatibilidade;
- qualidade factual;
- acesso;
- conveniência.

### Exploratory

Priorizar:

- diversidade relevante;
- baixo risco;
- baixo compromisso proporcional;
- valor informacional;
- possibilidade de aprender preferência.

### Decisional

Priorizar:

- fit;
- gates;
- trade-offs;
- evidência;
- explicabilidade.

### Longitudinal

Usar histórico apenas quando ele melhorar materialmente a decisão atual.

## 19. Papéis contextuais da oportunidade

Os papéis experimentais permanecem:

```text
Principal
Alternative
Complementary
Sequential
Enabling
Exploratory
```

Eles não formam ranking universal de qualidade.

## 20. Entrega Guivos

A entrega deve mostrar, proporcionalmente:

1. o que foi compreendido;
2. caminho(s) quando Possibilidade agrega valor;
3. oportunidade(s) concreta(s);
4. por que podem fazer sentido;
5. condições e gates;
6. custos e restrições conhecidos;
7. incertezas;
8. evidência externa e limites;
9. alternativas legitimamente descartadas quando isso aumentar confiança;
10. próximo ato possível sem pressão para agir.

Regra:

> **não-fit explicado também é valor.**

## 21. Benchmark controlado

Usar o mesmo snapshot de contexto autorizado para:

- Search baseline;
- IA generalista;
- Guivos.

Sempre que operacionalmente possível:

- normalizar formato;
- remover marca identificável;
- randomizar ordem;
- separar produção do cegamento;
- manter `Nenhum` como resposta legítima.

Dimensões congeladas:

- compreensão;
- utilidade dos caminhos;
- realizabilidade das oportunidades;
- ruído;
- explicação;
- solução que usaria hoje;
- solução que manteria se pudesse escolher somente uma.

## 22. Benchmark ecológico

Registrar como a Pessoa resolveria naturalmente o mesmo Momento sem a Guivos.

Exemplos possíveis:

- Google;
- ChatGPT ou outra IA;
- LinkedIn;
- Instagram;
- marketplace;
- amigo;
- especialista;
- comunidade;
- nenhum recurso.

O benchmark ecológico mede valor líquido sob fricção real e não substitui o benchmark controlado.

## 23. Ação

Estados observáveis:

```text
NENHUMA AÇÃO
PESQUISA ADICIONAL
ABRIU FONTE
SALVOU
CONVERSOU COM ALGUÉM
ENTROU EM CONTATO
AGENDOU
INSCREVEU
COMPROU
COMEÇOU
```

`clicou` isoladamente não é automaticamente ação material.

Para `Action Rate`, classificar como ação material somente comportamento que represente avanço real além de consumo passivo da entrega; a decisão exata deve ser preservada no dicionário do ciclo antes de cálculo final.

## 24. Follow-up

Checkpoints congelados:

```text
T+72h
T+14d
T+30d WHEN MATERIAL
```

Estados da experiência:

```text
CONSIDERADA
→ AÇÃO INICIAL
→ COMPROMISSO
→ PRIMEIRO CONTATO
→ PARTICIPAÇÃO INICIAL
→ EM ANDAMENTO
→ CONCLUÍDA / INTERROMPIDA
→ REFLETIDA
```

Uma oportunidade interrompida não é automaticamente falha humana nem falha da Guivos.

## 25. Pós-experiência

Pergunta principal:

> **Essa experiência contribuiu para o seu Momento Atual?**

Respostas legítimas incluem:

- contribuiu bastante;
- contribuiu em parte;
- não percebo contribuição;
- ainda não consigo avaliar;
- teve efeito negativo;
- resultado misto.

Depois perguntar:

> **De que forma?**

E:

> **O que aconteceu que faz você responder dessa forma?**

## 26. Evidence Guivos experimental

```text
EG-0 — experiência não confirmada
EG-1 — experiência declarada
EG-2 — contribuição declarada
EG-3 — consequência observável descrita
EG-4 — artefato relacionado
EG-5 — confirmação externa compatível
```

Regras:

```text
EG LEVEL
≠ CAUSALITY

EG-5
≠ EVOLUTION PROVEN
```

O nível registra força do suporte para o acontecimento/contribuição relatada, não uma nota de valor da Pessoa.

## 27. Novo Momento

Quando houver experiência/follow-up suficiente, perguntar:

> **Se tivéssemos que descrever seu Momento hoje, o que mudou e o que continua igual?**

O novo estado não sobrescreve silenciosamente o anterior.

## 28. Longitudinal Lift

Quando houver base legítima para testar continuidade:

### A

orientação usando apenas o Momento Atual.

### B

orientação usando:

```text
Momento anterior
+ Possibilidades
+ oportunidade
+ experiência
+ contribuição
+ Momento Atual
```

Pergunta cega:

> **qual é mais útil?**

Se B não vencer de forma material, a complexidade longitudinal deve ser reavaliada.

Não fabricar Episódio longitudinal apenas para preencher cobertura.

## 29. Métricas preliminares congeladas

As seguintes hipóteses de threshold permanecem exploratórias:

| Métrica | Sinal preliminar |
|---|---:|
| `Understanding A+B` | `≥ 80%` |
| Episódios com Possibilidade relevante, quando usada | `≥ 70%` |
| Oportunidades principais sem incompatibilidade crítica omitida | `≥ 90%` |
| Episódios com oportunidade seriamente considerada | `≥ 65%` |
| Guivos first/tied no benchmark central | `≥ 60%` |
| `Action Rate` | `40–50%` como faixa exploratória |
| `Reflection Return` | `≥ 60%` entre elegíveis |

Esses thresholds:

- não são KPIs canônicos;
- não validam PMF em `N=6`;
- não devem ser retroajustados para melhorar o resultado observado.

## 30. Métricas de segurança metodológica

### Gate Escape Rate

```text
numerador
→ oportunidades apresentadas que depois revelam incompatibilidade crítica omitida

denominador
→ oportunidades apresentadas e com informação posterior suficiente para avaliar escape
```

Objetivo: próximo de zero.

### Opportunity Precision

```text
numerador
→ oportunidades finais consideradas realmente plausíveis pela Pessoa após explicação completa

denominador
→ oportunidades finais apresentadas com avaliação disponível
```

### Exploration Learning

Pergunta:

> Em Episódios exploratórios, a experiência produziu informação útil sobre preferência ou direção?

Registrar `YES / PARTIAL / NO / INCONCLUSIVE` com justificativa qualitativa.

### Context Cost

Registrar fricção de captura em relação ao benefício percebido, observando:

- duração;
- repetição;
- esforço percebido;
- sensibilidade do contexto pedido;
- necessidade real de cada bloco de informação.

Não reduzir Context Cost a uma única nota sem preservar explicação.

### Longitudinal Lift

Calcular apenas nos Episódios em que o teste A/B é legitimamente executável.

## 31. Denominadores e dados faltantes

Regra:

> **não transformar ausência de observação em sucesso nem em fracasso automático.**

Para cada métrica, registrar:

- numerador;
- denominador elegível;
- missing;
- não aplicável;
- inconclusivo;
- motivo quando material.

Exemplos:

```text
SEM FOLLOW-UP ELEGÍVEL
→ não entra no denominador de Reflection Return

POSSIBILIDADE NÃO UTILIZADA POR NÃO AGREGAR VALOR
→ não entra no denominador de relevância de Possibilidade

LONGITUDINAL NÃO APLICÁVEL
→ não penaliza Longitudinal Lift
```

## 32. Evidência qualitativa obrigatória

Nenhuma taxa deve ser analisada sozinha.

Para cada episódio, a análise interna deve preservar de forma pseudonimizada:

- por que `A/B/C/D` foi atribuído;
- por que uma oportunidade foi considerada ou descartada;
- gate que mais alterou a seleção;
- explicação para preferência no benchmark;
- motivo da ação ou não ação quando informado;
- contexto da contribuição ou não contribuição;
- falha metodológica observada;
- contraexemplo relevante.

O GKR recebe apenas consolidação desidentificada posterior.

## 33. Stop Rules congeladas

Interromper e revisar antes de continuar quando houver, entre outros:

- falha crítica de privacidade;
- acesso indevido;
- safety incident;
- oportunidade apresentada com incompatibilidade grave omitida;
- repetição de compreensão `C/D` indicando falha do método;
- cegamento estruturalmente comprometido;
- captura percebida como invasiva;
- ferramenta incapaz de suportar correção/exclusão planejada;
- impossibilidade de estabelecer freshness suficiente;
- necessidade de contexto sensível desproporcional ao benefício.

Um stop rule disparado deve ser registrado mesmo que prejudique a continuidade do ciclo.

## 34. Desvios de protocolo

Classificar desvios como:

```text
MINOR
→ não altera materialmente interpretação do episódio

MAJOR
→ pode alterar resultado, comparabilidade ou segurança metodológica

CRITICAL
→ compromete segurança, privacidade, elegibilidade ou validade suficiente para continuar
```

Cada desvio precisa registrar:

- episódio pseudônimo afetado;
- etapa;
- descrição;
- classificação;
- impacto;
- ação tomada;
- necessidade ou não de versão nova.

Nenhum desvio individual identificável deve ser publicado no GKR.

## 35. Regra de mudança durante o Dry Run

### Sem mudança

Correção puramente editorial que não altera construto, gate, pergunta, ordem material ou avaliação.

### `v0.1.x`

Correção metodológica menor que não altera comparabilidade material e é registrada explicitamente.

### `v0.2.0+`

Mudança material em:

- pergunta central;
- routing;
- gate;
- seleção;
- benchmark;
- follow-up;
- métrica;
- threshold;
- stop rule;
- interpretação de sucesso.

Se uma mudança material ocorrer antes de concluir os seis episódios, os resultados devem ser segmentados por versão e a comparabilidade limitada explicitamente.

## 36. Saída obrigatória após seis Episódios

Produzir relatório desidentificado com quatro blocos.

### Operação

- o processo funcionou?;
- que etapa quebrou?;
- que etapa custou contexto demais?;
- houve falha de supply/freshness?;
- houve incidente?;
- houve desvio de protocolo?.

### Pessoa

- compreensão do Momento;
- clareza;
- relevância;
- oportunidades seriamente consideradas;
- comportamento;
- experiência;
- contribuição;
- Exploration Learning quando aplicável;
- Context Cost.

### Benchmark

- onde Guivos venceu;
- onde empatou;
- onde perdeu;
- por quê;
- qual vantagem reivindicada não apareceu.

### Tese

Classificar:

```text
GO
REVISE
STOP
INCONCLUSIVE
```

## 37. Regra de decisão

### GO

Somente quando houver convergência suficiente de sinais favoráveis e ausência de falha estrutural incompatível com avanço.

`GO` significa avançar a investigação, não declarar PMF.

### REVISE

Quando a tese central continuar plausível, mas o mecanismo apresentar falha corrigível que justifique nova versão.

### STOP

Quando o desenho atual apresentar falha estrutural suficiente para não justificar continuação sem reformulação substantiva.

### INCONCLUSIVE

Quando seis episódios não produzirem evidência suficiente para decidir com integridade.

`INCONCLUSIVE` é resultado válido e não deve ser convertido em `GO` por pressão de cronograma.

## 38. Escada de evidência e limites de inferência

A leitura permanece:

```text
E0 — hipótese
E1 — relato
E2 — preferência
E3 — comportamento
E4 — experiência
E5 — continuidade
E6 — econômica
E7 — rede
```

Regras de inferência:

```text
PARTICIPANTE DISSE
≠ PARTICIPANTE FEZ

PARTICIPANTE FEZ
≠ EXPERIÊNCIA VIVIDA

EXPERIÊNCIA VIVIDA
≠ CONTRIBUIÇÃO

CONTRIBUIÇÃO
≠ CAUSALIDADE

PREFERÊNCIA
≠ PMF

DRY RUN GO
≠ PMF
```

## 39. Relação com a simulação integral já concluída

A simulação sintética dos três Episódios já documentada no `RP-002-PMF-001` permanece como auditoria metodológica pré-campo:

```text
CAREER CASE
→ gates / incompatibility / sequential-complementary roles

COMMUNITY CASE
→ Preference Checkpoint / no inferred taste / no universal ranking

EXPLORATORY CASE
→ diversity / learning / legitimate negative preference
```

Ela não será repetida como se fosse evidência nova e não conta para `N=6`.

## 40. Relação com o fechamento documental do stack

O fechamento documental de privacidade/stack continua válido e separado deste freeze.

Este documento não modifica:

```text
OPERATIONAL IMPLEMENTATION
→ DEFERRED

P3-C
→ HOLD

P3-D
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD

DRY RUN REAL
→ NOT RELEASED
```

Congelar o método não autoriza implementar o stack.

## 41. Estado final

```text
RP-002 CONCEPTUAL READINESS
→ PASS PRESERVED

RP-002 METHODOLOGICAL READINESS
→ PASS PRESERVED

FIELD KIT v0.1
→ FROZEN FOR FIRST DRY RUN

DRY RUN METHOD / ANALYSIS PLAN
→ FROZEN v1.0.0

SIX REAL EPISODES
→ NOT STARTED

OPERATIONAL IMPLEMENTATION
→ DEFERRED

PARTICIPANT 001
→ HOLD

PMF
→ NOT VALIDATED
```

## 42. Próximo ato legítimo após este freeze

Nenhuma nova expansão metodológica deve ser promovida por inércia.

Enquanto a decisão de não iniciar implantação operacional permanecer válida, o próximo ato permitido é apenas:

- auditoria de consistência documental;
- correção de contradição;
- esclarecimento de definição já congelada;
- pesquisa teórica externa que não altere o protocolo sem nova decisão explícita.

A próxima promoção material do RP-002 depende de uma decisão futura de abrir a fase operacional e, depois, de evidência real produzida sob este protocolo.