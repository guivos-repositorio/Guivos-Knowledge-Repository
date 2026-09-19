---
id: GKR-UX-HOME-INTELLIGENCE-HANDOFF-001
title: Handoff Canônico para Design — Home Pública — Guivos Intelligence
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-19
parent: GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
depends_on:
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001
  - GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001
  - GPA-006
  - GKR-UX-HOMES-OUTCOME-001
normative: true
---

# Handoff Canônico para Design — Home Pública — Guivos Intelligence

## 1. Finalidade

Este documento estabelece o **Handoff Canônico da Home Pública Guivos Intelligence v1 para Design**.

Seu papel é transferir para a materialização visual somente a autoridade necessária para transformar o estado conceitual congelado em experiência de interface, sem reabrir produto, promessa, narrativa, copy, fronteiras, claims, privacidade, maturidade ou autoridade de decisão.

Regra central:

> **DESIGN RECEBE AUTORIDADE DE MATERIALIZAÇÃO ≠ AUTORIDADE DE REDEFINIÇÃO**

Este Handoff:

- consome o Home Source Lock vigente;
- fixa o contrato que Design deve preservar;
- explicita as liberdades reais de composição;
- define os limites que não podem ser reinterpretados por UX, UI, Figma, ferramenta generativa ou implementação futura;
- estabelece critérios objetivos para o próximo gate de materialização.

Este Handoff **não é**:

- wireframe;
- layout final;
- UI;
- protótipo;
- Design System;
- GENINPUT;
- prompt para ferramenta generativa;
- especificação técnica;
- implementação;
- autorização de publicação.

## 2. Base exata do Handoff

Este Handoff foi preparado a partir do estado reconciliado:

```text
main
43a8b0b07c6b7fe6690f422dc26844d0e22c5ea8

PR #288
GKR: congelar Source Lock da Home Intelligence v1
→ merged

HOME SOURCE LOCK
GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0
→ active
→ normative: true
```

O Handoff não altera a autoridade superior congelada nesse estado.

## 3. Cadeia de autoridade

Para Design, aplicar a seguinte ordem:

```text
NÍVEL 0
GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0
→ governa o que está congelado para materialização

NÍVEL 1
GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.1.1
→ governa narrativa pública, copy e fronteiras da Home

NÍVEL 2
GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.1
→ governa função, ordem e separação dos 11 movimentos

NÍVEL 3
GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0
→ governa a tradução pública permitida do produto

NÍVEL 4
GPA-006 v2.0.0
→ governa identidade, unidade de valor, responsabilidades e autoridade do produto

TRANSVERSAL
GKR-UX-HOMES-OUTCOME-001 v1.0.0
→ governa resultado antes de feature
```

Checkpoints históricos, outras Homes, benchmarks externos, rascunhos de conversa, telas internas, materiais de pricing ou documentos tecnológicos não entram automaticamente no pacote de Design.

## 4. Missão de Design

A missão é tornar perceptível, compreensível e tangível a seguinte progressão:

```text
ENTENDA MELHOR
→ VEJA O QUE ESTAVA SEPARADO
→ PERCEBA O QUE SE REPETE E MUDA
→ VEJA ISSO DE FORMA CONCRETA
→ ENTENDA DE ONDE VEIO A LEITURA
→ PRESERVE SUA DECISÃO
→ AMPLIE O QUE CONSEGUE PERCEBER
```

A experiência deve comunicar primeiro **o que a pessoa consegue enxergar** e somente depois **como o Intelligence torna isso possível**.

```text
RESULTADO
ANTES DO
MECANISMO

LINGUAGEM COMPREENSÍVEL
ANTES DA
TERMINOLOGIA ANALÍTICA
```

## 5. Centro semântico obrigatório

Unidade de valor:

> **compreensão útil e contextualizada.**

Ideia-mãe:

> **Compreender melhor amplia o que você consegue perceber.**

Pergunta-mãe:

> **O que se torna possível quando você compreende melhor o que está acontecendo?**

Apoio inicial:

> **Entenda melhor o que está acontecendo. Amplie o que você consegue perceber.**

Autonomia:

> **Veja mais antes de decidir.**

Fechamento:

> **Perceba antes o que começa a mudar. Enxergue além do que já está evidente.**

> **Novas possibilidades podem se tornar mais visíveis.**

Contrato superior:

```text
INFORMAÇÃO ≠ COMPREENSÃO
COMPREENDER ≠ DECIDIR
```

## 6. Onze funções semânticas obrigatórias

Design deve preservar as onze funções abaixo, ainda que não as transforme em onze seções físicas equivalentes:

```text
01 — ABRIR A POSSIBILIDADE
     compreender mais

02 — CRIAR A NECESSIDADE
     informação não basta

03 — DEFINIR O VALOR
     entender o que o isolado não mostra

04 — MOSTRAR OS RESULTADOS
     conexão / repetição / mudança / força

05 — DEMONSTRAR OS RESULTADOS
     indicadores / comparações / contexto

06 — EXPLICAR A FORMAÇÃO
     como uma leitura ganha contexto

07 — MOSTRAR UTILIDADE
     onde essa compreensão pode ajudar

08 — CONSTRUIR CONFIANÇA
     de onde veio a leitura

09 — PRESERVAR AUTONOMIA
     compreender antes de decidir

10 — APROFUNDAR RELAÇÕES
     entender o valor das conexões

11 — AMPLIAR O HORIZONTE
     perceber mais cedo e enxergar possibilidades
```

Permitido:

- agrupar movimentos em uma mesma composição;
- distribuir um movimento em mais de um elemento visual;
- usar progressão, scroll, motion ou disclosure para construir a leitura;
- alterar a quantidade física de seções.

Não permitido:

- eliminar função semântica;
- inverter a progressão de compreensão de modo que mecanismo anteceda valor;
- fundir movimentos de forma que suas funções deixem de ser reconhecíveis.

## 7. Separações críticas

### 7.1 Movimento 03 ≠ Movimento 10

```text
M03
→ responde por que Intelligence existe
→ informações isoladas não mostram tudo

M10
→ responde por que relações importam
→ compreender relações amplia a leitura
```

M10 não pode virar repetição visual ou textual de M03.

### 7.2 Movimento 04 ≠ Movimento 05

```text
M04
→ MOSTRA O QUE O INTELLIGENCE PERMITE PERCEBER

M05
→ DEMONSTRA COMO ESSA PERCEPÇÃO GANHA FORMA
```

M04 deve enfatizar:

- o que está conectado;
- o que se repete;
- o que está mudando;
- o que começa a ganhar força.

M05 deve tornar isso tangível por meio de relações como:

```text
INDICADOR
→ COMPARAÇÃO
→ CONTEXTO
→ RELAÇÃO
→ LEITURA
```

## 8. Copy e CTA

A copy do Home Source Lock é referência semântica normativa.

Design pode:

- ajustar quebras de linha;
- reduzir trechos de apoio quando o significado permanecer integral;
- distribuir uma mesma mensagem entre título, apoio, label ou microcopy;
- adaptar cadência ao layout.

Design não pode:

- alterar tese, autoridade, fronteira, maturidade, resultado ou promessa;
- transformar possibilidade em garantia;
- transformar resultado esperado em resultado comprovado;
- inserir claim novo;
- substituir clareza por jargão analítico ou tecnológico.

CTAs congelados:

> **Veja o que suas informações podem mostrar**

> **Conheça o Guivos Intelligence**

Os CTAs não podem ser reinterpretados como promessa de decisão certa, diagnóstico, certeza ou futuro conhecido.

## 9. Duas frentes preservadas

### Pessoa / Journey

Direção pública:

> **Entenda melhor por que determinadas informações, recomendações ou possibilidades podem aparecer em determinado contexto.**

```text
INTELLIGENCE
→ produz compreensão

JOURNEY
→ governa a experiência

PESSOA
→ escolhe
```

### Business / população

Direção pública:

> **Compreenda padrões, mudanças e movimentos em populações de forma agregada e protegida.**

```text
INTELLIGENCE
→ produz leitura populacional

BUSINESS
→ governa a relação empresarial

EMPRESA
→ decide
```

Invariantes:

```text
INTELLIGENCE ≠ JOURNEY
INTELLIGENCE ≠ BUSINESS
```

> **A Empresa não recebe Intelligence individual por funcionário nem acesso à intimidade individual da Journey.**

A materialização não pode transformar a Home Intelligence em Home de Journey nem em Home de Business.

## 10. Materialização analítica

Podem ser utilizados para demonstrar valor:

- KPI;
- indicador;
- percentual;
- variação;
- série temporal;
- comparação;
- distribuição;
- tendência;
- mudança;
- relação;
- mini gráfico;
- card analítico;
- movimento emergente;
- sequência interpretativa;
- rede relacional.

Todo elemento analítico deve ajudar o visitante a responder pelo menos uma pergunta:

1. O que consigo ver?
2. O que mudou?
3. O que está relacionado?
4. O que se repete?
5. O que começa a ganhar força?
6. O que ficou mais claro quando o contexto foi considerado?

Guardrails:

```text
VISUAL ANALÍTICO ≠ DASHBOARD COMO PRODUTO
EXEMPLO CONCEITUAL ≠ DADO OPERACIONAL REAL
VISUAL EXPLICATIVO ≠ PROVA DE RESULTADO
```

Na ausência de dados reais formalmente validados, exemplos devem ser identificáveis como conceituais ou ilustrativos e nunca apresentados como evidência operacional.

## 11. Confiança, explicabilidade e autonomia

Design deve preservar visibilidade suficiente para que a experiência comunique:

```text
RESULTADO / LEITURA
→ DE ONDE VEIO?
→ O QUE FOI CONSIDERADO?
→ O QUE MUDOU?
→ COMO AS INFORMAÇÕES PODEM ESTAR RELACIONADAS?
→ O QUE É FATO?
→ O QUE É INTERPRETAÇÃO?
→ ATÉ ONDE A LEITURA PODE IR?
```

A experiência não precisa expor indiscriminadamente mecanismos internos para demonstrar explicabilidade.

Invariantes:

```text
COMPREENDER ≠ DECIDIR
MAIS COMPREENSÃO ≠ MENOS AUTONOMIA
RELAÇÃO ≠ CAUSA
CORRELAÇÃO ≠ CAUSALIDADE
INFERÊNCIA ≠ FATO
```

## 12. Horizonte temporal e claims

A expressão aspiracional pode ser materializada, mas sempre sob:

```text
PERCEBER ANTES ≠ PREVER O FUTURO
SINAL ≠ CERTEZA
TENDÊNCIA ≠ DESTINO
POSSIBILIDADE ≠ RESULTADO GARANTIDO
```

Não materializar como claim vigente ou comprovado que Guivos Intelligence:

- prevê o futuro;
- sabe o que vai acontecer;
- garante decisões melhores;
- encontra a decisão certa;
- determina causalidade automaticamente;
- diagnostica pessoas;
- cria score humano de evolução;
- revela Journey individual à Empresa;
- comprova aumento de produtividade, redução de risco ou melhoria de performance sem evidência vigente;
- possui métricas, benchmarks, integrações ou casos reais não formalizados.

## 13. IA, Graph e tecnologia

Tecnologia permanece subordinada à compreensão.

```text
GUIVOS INTELLIGENCE
≠ IA
≠ LLM
≠ DASHBOARD
≠ POWER BI
≠ GRAFO GLOBAL
≠ NEO4J
≠ GRAPHRAG
≠ API
≠ RELATÓRIO
```

Ordem de materialização:

```text
NECESSIDADE
→ CAPACIDADE
→ ENTREGA
→ RESULTADO
→ MECANISMO
→ TECNOLOGIA
```

IA, Graph, redes, nós e conexões podem aparecer quando explicarem uma capacidade ou relação real da narrativa; não podem ser decoração destinada apenas a sinalizar tecnologia, sofisticação ou IA.

```text
GRAFO GLOBAL ≠ GUIVOS INTELLIGENCE
NEO4J ≠ GRAFO GLOBAL
NEO4J ≠ GUIVOS INTELLIGENCE
```

> **A tecnologia amplia a capacidade do Intelligence. Não amplia sua autoridade.**

## 14. Privacidade e autoridade

Design não pode enfraquecer ou omitir, quando materialmente relevante, os contratos:

```text
CONHECER ≠ UTILIZAR ≠ COMPARTILHAR
DECLARADO ≠ OBSERVADO ≠ INFERIDO ≠ PREDITO
PERSONALIZAR ≠ EXPOR
NO-NAME ≠ ANÔNIMO
AGREGADO ≠ AUTOMATICAMENTE SEGURO
PAGAMENTO ≠ RELEVÂNCIA
ENTITLEMENT ≠ AUTORIDADE
PLANO SUPERIOR ≠ MENOS PRIVACIDADE
TECNOLOGIA ≠ PRODUTO
```

A assimetria de privacidade permanece: Intelligence pode conhecer mais, dentro das autorizações legítimas, para servir à pessoa do que pode revelar a uma organização.

## 15. Liberdades de Design

Dentro das invariantes deste Handoff, Design pode decidir:

- número físico de seções;
- layout;
- grid e composição;
- hierarquia tipográfica;
- fotografia, ilustração e mídia;
- iconografia;
- variantes de componentes;
- cards;
- tratamento visual de KPIs e gráficos;
- agrupamento visual dos onze movimentos;
- arquitetura responsiva;
- motion;
- progressive disclosure;
- densidade;
- posição e forma dos CTAs congelados;
- presença ou ausência de demonstração tecnológica subordinada;
- tratamento de redes e relações quando semanticamente necessário.

Liberdade visual não autoriza alteração semântica.

## 16. Autoridade que não é transferida a Design

Design não recebe autoridade para decidir ou alterar:

- definição do Guivos Intelligence;
- unidade de valor;
- promessa pública;
- pergunta-mãe;
- contrato `COMPREENDER ≠ DECIDIR`;
- fronteira Person/Journey e Business/população;
- privacidade e governança;
- autoridade da pessoa ou da empresa;
- causalidade;
- maturidade tecnológica;
- papel de AI/Graph/Neo4j/GraphRAG;
- novos claims;
- novos dados ou evidências;
- pricing;
- arquitetura técnica;
- estado global do GKR.

## 17. Gate de aceitação da materialização

Qualquer futura proposta de wireframe, UI ou protótipo deve ser rejeitada ou corrigida se falhar em qualquer um dos pontos abaixo:

- [ ] comunica compreensão antes de tecnologia;
- [ ] preserva as onze funções semânticas;
- [ ] mantém M03 distinto de M10;
- [ ] mantém M04 distinto de M05;
- [ ] torna resultados perceptíveis antes de explicar mecanismos;
- [ ] preserva os CTAs congelados;
- [ ] preserva Person/Journey e Business/população sem transferência indevida de autoridade;
- [ ] preserva explicabilidade e autonomia;
- [ ] não converte relação em causa;
- [ ] não converte sinal em certeza;
- [ ] não converte percepção antecipada em previsão do futuro;
- [ ] identifica exemplos conceituais sem apresentá-los como prova real;
- [ ] mantém IA, Graph e tecnologia subordinados;
- [ ] não inventa maturidade, integração, benchmark, métrica ou caso real;
- [ ] não transforma Intelligence em dashboard, IA ou produto tecnológico isolado.

## 18. Próximo gate — GENINPUT Intelligence

Com este Handoff integrado, o próximo artefato elegível é o **GENINPUT Intelligence**, em pacote separado.

```text
HOME SOURCE LOCK
→ HANDOFF CANÔNICO PARA DESIGN
→ GENINPUT INTELLIGENCE
→ MATERIALIZAÇÃO CONTROLADA
```

O GENINPUT deve traduzir este contrato para o formato operacional necessário à ferramenta ou etapa de Design escolhida, sem criar nova autoridade semântica.

Invariante:

> **GENINPUT TRADUZ O HANDOFF ≠ REDEFINE A HOME**

O GENINPUT **não integra este Handoff** e deve ser tratado em PR separada.

## 19. O que a integração deste Handoff não inicia automaticamente

A integração deste documento não inicia automaticamente:

- GENINPUT;
- execução em Figma Make ou outra ferramenta generativa;
- wireframe;
- UI;
- protótipo;
- implementação front-end ou back-end;
- publicação;
- Marketing/GTM;
- pricing;
- mudança de maturidade técnica;
- sincronização transversal de `GKR-STATE-001` ou Roadmap.

Cada etapa posterior exige o gate e a autorização correspondentes.
