---
id: GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
title: Source Lock — Home Pública — Guivos Intelligence
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-19
parent: GKR-UX-HOME-INTELLIGENCE-MASTER-001
depends_on:
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001
  - GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001
  - GPA-006
  - GKR-UX-HOMES-OUTCOME-001
  - GKR-STATE-001
normative: true
---

# Source Lock — Home Pública — Guivos Intelligence

## 1. Finalidade

Este documento consolida o **Source Lock da Home Pública do Guivos Intelligence v1** após a convergência da arquitetura narrativa em onze movimentos, do Documento Mestre e da correção editorial da copy pública de referência.

Seu papel é:

- congelar as fontes vigentes que podem governar a futura materialização da Home Intelligence;
- eliminar ambiguidades entre formulações anteriores e a copy pública efetivamente aprovada;
- registrar as invariantes que não podem ser reinterpretadas por Design, UX, UI, ferramentas generativas ou implementação futura;
- separar claramente o que está congelado do que continua aberto;
- impedir que lacunas visuais, tecnológicas ou operacionais sejam preenchidas por inferência.

Este Source Lock **não é**:

- autorização de Design;
- wireframe;
- UI;
- protótipo;
- handoff para ferramenta generativa;
- especificação técnica;
- prova de implementação;
- prova de performance;
- autorização de publicação.

Regra:

> **Source Lock congela a fonte. Não autoriza, por si só, a materialização.**

## 2. Checkpoint do Source Lock

```text
HOME
Guivos Intelligence v1

FASE
Source Lock pré-Design

CHECKPOINT DO GKR
main @ 31f985625c312e3d0bdc3836dbf34fa39c762d80

gh-pages
Deployed 31f985625 with MkDocs 1.6.1

DOCUMENTO MESTRE
GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.1.1

ARQUITETURA NARRATIVA
GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.1

PRODUCT SOURCE LOCK
GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0

ARQUITETURA DE PRODUTO
GPA-006 v2.0.0
```

Objetivo do lock:

> preservar uma fonte pública única, coerente e auditável para a futura materialização da Home Intelligence, sem reabrir decisões já validadas nem antecipar tecnologia, Design ou operação ainda não comprovados.

## 3. Pacote de fontes autorizado

Para qualquer futura materialização da Home Intelligence, o pacote inicial de autoridade deve ser restrito a:

1. `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001` — este Source Lock;
2. `GKR-UX-HOME-INTELLIGENCE-MASTER-001` v0.1.1 — `docs/experience-architecture/public-home-intelligence-master-document.md`;
3. `GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001` v0.2.1 — `docs/experience-architecture/public-home-intelligence-conceptual-architecture.md`;
4. `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001` v1.0.0 — `docs/product-architecture/intelligence-product-source-lock.md`;
5. `GPA-006` v2.0.0 — `docs/product-architecture/intelligence.md`;
6. `GKR-UX-HOMES-OUTCOME-001` v1.0.0 — princípio transversal de resultado das Homes.

Não adicionar automaticamente:

- versões `0.1.0`, `0.2.0`, `1.1.0` ou outras formulações supersedidas;
- rascunhos de conversa;
- checkpoints históricos;
- outras Homes;
- benchmarks externos;
- documentos de pricing;
- materiais de Neo4j, GraphRAG, Power BI, Guivos.ai ou IA não requeridos para resolver dúvida concreta;
- telas internas;
- documentos de implementação.

Qualquer ampliação do pacote exige dúvida específica e decisão deliberada.

## 4. Ordem de autoridade

Quando houver dúvida futura, aplicar:

```text
NÍVEL 0
GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
→ governa o que está congelado para materialização

NÍVEL 1
GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.1.1
→ governa narrativa pública, copy de referência e fronteiras da Home

NÍVEL 2
GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.1
→ governa função, ordem e separação dos onze movimentos

NÍVEL 3
GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0
→ governa a tradução pública permitida da autoridade do produto

NÍVEL 4
GPA-006 v2.0.0
→ governa identidade, unidade de valor, responsabilidades e autoridade do produto

TRANSVERSAL
GKR-UX-HOMES-OUTCOME-001 v1.0.0
→ governa resultado antes de feature

HISTÓRICO
→ explica como decisões foram construídas
→ não substitui o estado vigente
```

Se uma formulação histórica divergir da versão vigente do Documento Mestre ou deste Source Lock, prevalece o estado vigente salvo nova decisão explicitamente governada.

## 5. Centro semântico congelado

Unidade de valor:

> **compreensão útil e contextualizada.**

Ideia-mãe:

> **Compreender melhor amplia o que você consegue perceber.**

Pergunta-mãe:

> **O que se torna possível quando você compreende melhor o que está acontecendo?**

Expressão de apoio inicial:

> **Entenda melhor o que está acontecendo. Amplie o que você consegue perceber.**

Expressão de autonomia:

> **Veja mais antes de decidir.**

Fechamento aspiracional:

> **Perceba antes o que começa a mudar. Enxergue além do que já está evidente.**

Complemento de fechamento:

> **Novas possibilidades podem se tornar mais visíveis.**

Contrato superior:

```text
INFORMAÇÃO ≠ COMPREENSÃO
COMPREENDER ≠ DECIDIR
```

## 6. Regra editorial congelada

> **Primeiro mostre o que a pessoa consegue enxergar. Depois explique como o Intelligence torna isso possível.**

Consequentemente:

```text
RESULTADO
ANTES DO
MECANISMO

LINGUAGEM COMPREENSÍVEL
ANTES DA
TERMINOLOGIA ANALÍTICA
```

Termos como contexto, evidência, padrão, tendência, movimento, inferência e relação podem ser utilizados quando ajudarem a compreensão, mas não devem ser requisito para compreender o benefício.

## 7. Arquitetura pública congelada — 11 movimentos

```text
01 — POSSIBILIDADE
O que se torna possível quando você compreende melhor o que está acontecendo?

02 — NECESSIDADE
Ter mais informação não significa entender melhor.

03 — VALOR PRÓPRIO
Entenda o que informações isoladas não conseguem mostrar.

04 — RESULTADOS
Veja o que está conectado.
Perceba o que se repete.
Entenda o que está mudando.
Veja o que começa a ganhar força.

05 — MATERIALIZAÇÃO
Veja o que você não enxergaria olhando cada informação separadamente.

06 — FORMAÇÃO DA COMPREENSÃO
Informações fazem mais sentido quando você consegue enxergar o contexto ao redor delas.

07 — APLICAÇÃO
Onde essa compreensão pode ser útil na prática?

08 — CONFIANÇA
Não veja apenas a conclusão. Entenda de onde ela veio.

09 — AUTONOMIA
Veja mais antes de decidir.

10 — INTELIGÊNCIA CONECTADA
Uma informação pode mostrar mais quando você entende com o que ela se relaciona.

11 — HORIZONTE AMPLIADO
Perceba antes o que começa a mudar. Enxergue além do que já está evidente.
```

Os onze movimentos são funções semânticas, não obrigação de onze blocos visuais equivalentes.

Congelar também:

```text
M03
→ DEFINE POR QUE INTELLIGENCE EXISTE

M10
→ APROFUNDA POR QUE AS RELAÇÕES IMPORTAM

M04
→ MOSTRA OS RESULTADOS

M05
→ DEMONSTRA OS RESULTADOS
```

A futura materialização pode agrupar movimentos, desde que preserve significado, sequência de compreensão e capacidade de reconhecimento de cada função.

## 8. Copy pública congelada semanticamente

### Movimento 02

> **O que faz diferença é conseguir juntar informações que estão espalhadas e entender o que elas mostram quando vistas em conjunto.**

### Movimento 03

> **Guivos Intelligence conecta informações que, separadas, mostram apenas parte da história — ajudando você a perceber relações, padrões e mudanças que antes poderiam passar despercebidos.**

> **Veja como as informações se conectam. Perceba o que se repete. Entenda o que está mudando.**

### Movimento 05

> **Perceba quando algo que parecia isolado começa a se repetir e ganhar força.**

> **Vá além do número. Entenda o que ele pode estar mostrando.**

> **Entenda de onde uma conclusão veio — e até onde ela pode ir.**

### Movimento 06

> **Guivos Intelligence observa informações em conjunto, considera o contexto em que elas existem e busca relações que ajudem você a interpretá-las melhor.**

### Movimento 08

Sequência pública de referência:

```text
O que foi observado?
O que mudou?
Quais informações foram consideradas?
Como elas podem estar relacionadas?
O que é fato?
O que é interpretação?
Até onde essa leitura pode ir?
```

### Movimento 09

> **Guivos Intelligence pode mostrar relações, comparar informações e explicar leituras. A decisão continua com você — ou com quem tem autoridade para tomá-la.**

### Movimento 10

> **Guivos Intelligence não olha apenas informações isoladas. Ele considera como acontecimentos, contextos e informações podem estar relacionados para construir uma leitura mais completa.**

### Movimento 11

> **Ao perceber relações, repetições e mudanças com mais contexto, você pode reconhecer sinais mais cedo e ampliar o que consegue considerar.**

As formulações podem receber ajustes microeditoriais no Design posterior somente quando preservarem exatamente seu significado, autoridade e claim.

## 9. CTA congelado

CTA principal:

> **Veja o que suas informações podem mostrar**

CTA secundário:

> **Conheça o Guivos Intelligence**

O CTA não pode prometer:

- futuro conhecido;
- resposta certa;
- decisão certa;
- diagnóstico;
- certeza;
- resultado empresarial comprovado.

## 10. Duas frentes — um único Intelligence

### Pessoa / Journey

Direção pública congelada:

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

Direção pública congelada:

> **Compreenda padrões, mudanças e movimentos em populações de forma agregada e protegida.**

```text
INTELLIGENCE
→ produz leitura populacional

BUSINESS
→ governa a relação empresarial

EMPRESA
→ decide
```

Invariante:

> **A Empresa não recebe Intelligence individual por funcionário nem acesso à intimidade individual da Journey.**

## 11. Direção visual permitida

A futura materialização pode demonstrar:

- conexões;
- repetições;
- mudanças;
- comparação temporal;
- distribuição;
- relações;
- sinais ganhando força;
- contexto de um indicador;
- origem de uma leitura;
- incerteza;
- limite de uma interpretação.

Podem ser explorados conceitualmente:

- KPIs;
- indicadores;
- mini gráficos;
- séries temporais;
- comparações;
- cards analíticos;
- redes e relações;
- fluxos;
- before/after;
- exemplos analíticos;
- escadas de interpretação.

Guardrails:

```text
VISUAL ANALÍTICO ≠ DASHBOARD COMO PRODUTO
EXEMPLO CONCEITUAL ≠ DADO OPERACIONAL REAL
VISUAL EXPLICATIVO ≠ WIREFRAME CANÔNICO
```

Quando não houver dados reais validados, usar exemplos explicitamente rotulados como conceituais.

## 12. Graph, IA e tecnologia

Não existe seção obrigatória congelada de IA, Graph, Neo4j, GraphRAG, Power BI ou Guivos.ai.

Regra:

> **Tecnologias podem aparecer para explicar como determinadas capacidades podem ser realizadas, mas nunca como definição principal do Guivos Intelligence.**

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

Ordem correta:

```text
NECESSIDADE
→ CAPACIDADE
→ ENTREGA
→ RESULTADO
→ MECANISMO
→ TECNOLOGIA
```

> **A tecnologia amplia a capacidade do Intelligence. Não amplia sua autoridade.**

## 13. Claims proibidos

Não afirmar como vigente ou comprovado que Guivos Intelligence:

- prevê o futuro;
- sabe o que vai acontecer;
- garante decisões melhores;
- encontra a decisão certa;
- determina causalidade automaticamente;
- diagnostica pessoas;
- cria score humano de evolução;
- revela Journey individual à Empresa;
- comprova aumento de produtividade;
- comprova redução de risco;
- comprova melhoria de performance;
- possui Neo4j operacional em escala sem evidência vigente;
- possui GraphRAG/GDS operacional sem evidência vigente;
- possui Power BI integrado sem evidência vigente;
- possui Guivos.ai operacional sem evidência vigente;
- possui métricas, benchmarks ou casos reais não formalizados.

## 14. Guardrails congelados

```text
INFORMAÇÃO ≠ COMPREENSÃO
COMPREENDER ≠ DECIDIR
INTELLIGENCE ≠ JOURNEY
INTELLIGENCE ≠ BUSINESS
CONHECER ≠ UTILIZAR ≠ COMPARTILHAR
DECLARADO ≠ OBSERVADO ≠ INFERIDO ≠ PREDITO
PERSONALIZAR ≠ EXPOR
CORRELAÇÃO ≠ CAUSALIDADE
RELAÇÃO ≠ CAUSA
PADRÃO ≠ CAUSA
MOVIMENTO ≠ DIAGNÓSTICO
SINAL ≠ CERTEZA
TENDÊNCIA ≠ DESTINO
INFERÊNCIA ≠ FATO
MAIS DADOS ≠ MELHOR INTELLIGENCE
TECNOLOGIA ≠ PRODUTO
RESULTADO ESPERADO ≠ RESULTADO COMPROVADO
PERCEBER ANTES ≠ PREVER O FUTURO
POSSIBILIDADE ≠ RESULTADO GARANTIDO
RECOMENDAÇÃO ≠ ORDEM
```

Privacidade e autoridade permanecem vinculadas às autoridades superiores do produto.

## 15. O que permanece aberto para Design

O Source Lock não congela:

- número físico de seções;
- composição e grid;
- agrupamento visual dos movimentos;
- tipografia;
- fotografia, ilustração ou mídia;
- iconografia;
- motion;
- comportamento responsivo;
- geometria dos gráficos;
- layout de cards e KPIs;
- presença ou ausência de demonstração tecnológica, desde que subordinada;
- microcopy que não altere significado;
- ordem interna de exemplos dentro de um mesmo movimento.

Essas liberdades só se tornam executáveis após Handoff/Design explicitamente autorizado.

## 16. O que este Source Lock não autoriza

A integração deste artefato não autoriza automaticamente:

- atualização do Handoff Canônico;
- Design;
- Figma Make;
- ferramenta generativa;
- wireframe;
- UI;
- protótipo;
- implementação front-end ou back-end;
- publicação comercial;
- Marketing/GTM;
- pricing;
- novos claims;
- promoção silenciosa de maturidade técnica;
- alteração de `GKR-STATE-001` ou Roadmap sem sincronização transversal autorizada.

## 17. Critérios para o próximo gate

Antes de iniciar Design, o futuro Handoff deve preservar:

- o pacote de fontes deste Source Lock;
- a arquitetura em onze movimentos;
- a copy pública vigente;
- os CTAs congelados;
- as duas frentes e suas autoridades;
- `M03 ≠ M10`;
- `M04 ≠ M05`;
- papel subordinado de Graph/IA;
- exemplos analíticos como demonstração, não prova;
- todos os guardrails de privacidade, causalidade, previsão e autonomia.

Próximo ponto elegível após a integração deste Source Lock:

> **Handoff controlado da Home Pública Guivos Intelligence v1 para Design**, mediante autorização separada.

Nenhuma etapa autoriza automaticamente a seguinte.
