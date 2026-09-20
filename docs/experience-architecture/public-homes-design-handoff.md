---
id: GKR-UX-HOMES-DESIGN-HANDOFF-001
title: Homes Públicas — Handoff Canônico para Design, UX, UI e Ferramentas Generativas
status: active
version: 1.7.2
owner: Experience Architecture
last_updated: 2026-09-20
normative: true
maturity: designer_first_ai_optional_main_canonical_first_class
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-OC-MEDIA-SUPPLY-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-MALL-MEDIA-SUPPLY-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GPA-005
  - GKR-UX-HOME-ADS-MASTER-001
  - GPA-007
  - GKR-UX-HOME-BUSINESS-SOURCELOCK-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GPA-004
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001
  - GKR-UX-HOME-INTELLIGENCE-HANDOFF-001
  - GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001
  - GPA-006
  - GKR-UX-HOMES-OUTCOME-001
---

# Homes Públicas — Handoff Canônico para Design, UX, UI e Ferramentas Generativas

## 0. Estado corrente e gate de produção

Esta autoridade governa o handoff **corrente** das oito Homes. Design e IA opcional devem consumir somente autoridades vigentes no `main` canônico, conforme o Manifesto corrente.

```text
SOURCE OF TRUTH
→ CURRENT CANONICAL MAIN

CURRENT CHECKPOINT
→ CURRENT MAIN
→ RESOLVED AT CONSUMPTION TIME

DESIGN PRODUCTION READINESS
→ ACTIVE

DESIGN PRODUCTION RELEASE
→ GRANTED

SNAPSHOTS / CANDIDATES / CHECKPOINTS HISTÓRICOS
→ NOT OPERATIONAL INPUT
→ NOT REQUIRED FOR DESIGN OR PROTOTYPING

EXTERNAL SNAPSHOT
→ OPTIONAL TRANSPORT ARTIFACT
→ NOT A PRECONDITION FOR EXECUTION

AI
→ OPTIONAL / DESIGNER-CONTROLLED
```

A designer pode trabalhar diretamente a partir do conjunto canônico vigente definido pelo Manifesto. Um snapshot externo só deve ser criado quando houver necessidade concreta de congelamento ou transporte; ele não substitui o `main` como fonte primária de verdade.

### 0.1 Liberdade criativa protegida

O GKR **não congela identidade visual canônica** para estas Homes. A designer pode criar, com originalidade e autonomia, tipografia, paleta, imagens, ilustração, iconografia, grid, ritmo, composição, atmosfera, motion, linguagem gráfica, tratamento de componentes e tom de voz/copy não congelada.

Essas escolhas são **output de Design**, não pré-condição documental. A solução criativa aprovada deve ser documentada no artefato final de Design entregue pela designer, com consistência e handoff suficientes para continuidade.

A liberdade criativa não autoriza alterar significado, papéis de produto, nomenclatura oficial, assinatura institucional quando utilizada, claims factuais, regras econômicas, disponibilidade, dados, parceiros, causalidade, privacidade ou demais contratos governados.

```text
SEMANTIC / FUNCTIONAL TRUTH
→ GKR

VISUAL / CREATIVE EXPRESSION
→ DESIGN

AI TOOL
→ OPTIONAL EXPLORATION INSTRUMENT

HUMAN APPROVAL
→ SELECTS THE DIRECTION
```


### 0.2 Correção de precedência — designer-first / IA opcional

A decisão humana de 2026-09-19 estabelece a seguinte precedência sobre qualquer formulação histórica deste documento que possa sugerir uma ferramenta generativa específica como etapa obrigatória:

```text
DESIGNER
→ CREATIVE AUTHOR
→ MAY WORK MANUALLY

AI
→ OPTIONAL
→ DESIGNER DISCRETION

GKR / CHATGPT
→ DOES NOT CREATE OR ADVANCE DESIGN FILES
→ DOES NOT CREATE OR ADVANCE FIGMA FILES
→ DOES NOT PRESELECT VISUAL DIRECTION

TOOL-SPECIFIC WORDING ELSEWHERE
→ READ AS HISTORICAL / NON-MANDATORY WHEN IN CONFLICT WITH THIS SECTION
```

---

## 1. Finalidade

Este documento governa o **handoff das oito Homes públicas já convergidas da Guivos para a fase de Design, UX, UI, wireframe e prototipação**.

Seu objetivo é permitir que Design trabalhe com um conjunto pequeno, atual e semanticamente controlado de fontes, sem reconstruir decisões a partir do histórico completo do Guivos Knowledge Repository.

As oito Homes abrangidas por esta versão são:

1. Home Pública — Pessoa;
2. Home Pública — Organizações e Coletivos;
3. Home Pública — Guivos Mall;
4. Home Pública — Guivos Travel;
5. Home Pública — Guivos Media;
6. Home Pública — Guivos Ads;
7. Home Pública — Guivos Business;
8. Home Pública — Guivos Intelligence.

Este documento **não desenha as páginas** e não determina solução visual final. Ele define quais decisões precisam ser preservadas, quais fontes têm autoridade, como ferramentas generativas podem ser utilizadas e onde termina a arquitetura governada e começa a liberdade de Design.

```text
GKR
→ define significado, função, narrativa, fronteiras, Source Locks e invariantes

DESIGNER / FERRAMENTA DE DESIGN / IA OPCIONAL
→ produz a solução visual fora desta frente canônica

VALIDAÇÃO HUMANA
→ confronta forma e significado contra o GKR
```

Portanto, a atualização deste handoff **não cria mapa de página, wireframe, direção visual, UI ou protótipo dentro do GKR**.

---

## 2. Regime da fase de Design

Este Handoff constitui a autoridade procedimental comum para criação e prototipação das oito Homes.

A execução fica liberada quando coexistirem:

1. conjunto canônico corrente identificado pelo Manifesto;
2. Master e autoridades específicas da Home no mesmo checkpoint do `main`;
3. ausência de finding material aberto nas autoridades correntes;
4. `DESIGN PRODUCTION RELEASE = GRANTED`.

Não é necessário materializar snapshot para iniciar Design.

Podem ser executados:

- criação manual pela designer e, opcionalmente, exploração assistida por IA;
- arquitetura visual;
- wireframes de baixa fidelidade;
- exploração de UX e direção visual;
- UI de alta fidelidade;
- protótipos de navegação e interação;
- estudos responsivos desktop e mobile;
- validação das soluções contra os contratos correntes do GKR;
- consolidação dos artefatos finais de Design nas ferramentas escolhidas pela designer.

O release de Design não autoriza automaticamente desenvolvimento, publicação em produção, mudança de produto/economia, claims não sustentados ou Product Engineering.

> **O Handoff governa COMO criar. O Manifesto governa QUAIS fontes correntes usar. O Source Lock governa COMO isolar o contexto. O Design Production Release humano governa QUANDO iniciar.**

## 3. Princípio central

> **A designer é autora da solução. Ferramentas de IA, quando utilizadas, são instrumentos opcionais de exploração e não fontes de decisão sobre a arquitetura das Homes.**

Uma solução visual produzida manualmente ou com apoio de IA, plugin, template, benchmark ou referência externa não se torna canônica apenas por existir. Somente após validação humana contra o GKR uma direção pode ser promovida.

---

## 4. Pacote oficial de handoff

A composição operacional de cada emissão é governada por `GKR-UX-HOMES-DESIGN-DELIVERY-001`.

### 4.1 Pessoa

Usar o Handoff comum e as autoridades específicas registradas no Manifesto vigente, incluindo Documento Mestre, reconciliação pós-Media e Source Lock + Prompt.

### 4.2 Organizações e Coletivos

Usar o Handoff comum e as autoridades específicas registradas no Manifesto vigente, incluindo Documento Mestre, reconciliação pós-Media e Source Lock + Prompt.

### 4.3 Guivos Mall

Usar o Handoff comum e as autoridades específicas registradas no Manifesto vigente, incluindo Documento Mestre, reconciliação pós-Media e Source Lock + Prompt.

### 4.4 Guivos Travel

Usar o Handoff comum e as autoridades específicas registradas no Manifesto vigente, incluindo Documento Mestre, reconciliação pós-Media e Source Lock + Prompt.

### 4.5 Guivos Media

Usar o Handoff comum e as autoridades específicas registradas no Manifesto vigente, incluindo Documento Mestre, `GPA-005` e Source Lock + Prompt.

### 4.6 Guivos Ads

Usar o Handoff comum e as autoridades específicas registradas no Manifesto vigente, incluindo Documento Mestre, `GPA-007` e Source Lock + Prompt.

### 4.7 Guivos Business

O contexto de Business permanece deliberadamente mais amplo. Usar somente o pacote definido pelo Manifesto vigente, baseado em:

1. `GKR-UX-HOME-BUSINESS-SOURCELOCK-001`;
2. `GKR-UX-HOME-BUSINESS-MASTER-001`;
3. `GKR-UX-HOME-BUSINESS-CONVERSION-002`;
4. `GKR-UX-HOME-BUSINESS-AUTHORITY-001`;
5. `GPA-004`;
6. Source Lock Operacional + Prompt específico de Business.

### 4.8 Guivos Intelligence

Intelligence possui cadeia específica já convergida e deve ser materializado sem ser confundido com tecnologia, dashboard ou mecanismo de decisão.

Ordem operacional corrente, subordinada às versões exatas fixadas pelo Manifesto vigente:

```text
N0 — MANIFESTO + SOURCE LOCK CORRENTES
     → fixam checkpoint, fontes autorizadas e estado da exploração

N1 — GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.1.10
     → congela significado e invariantes da Home

N2 — GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.1.11
     → traduz a Home para o contrato de Design

N3 — GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.9
     + GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.4
     + GKR-UX-HOMES-OUTCOME-001 v1.0.0
     → preservam narrativa, valor, copy e função pública

N4 — GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.1
     + GPA-006 v2.0.1
     → governam significado e limites superiores do produto
```

Documentos históricos, candidates, snapshots e GENINPUTs superados não entram no input operacional.

---

## 5. Ordem geral de autoridade

```text
NÍVEL 0 — HANDOFF CANÔNICO COMUM
→ governa processo, autorização, fontes e uso de ferramentas generativas

NÍVEL 1 — SOURCE LOCK / HANDOFF / GENINPUT ESPECÍFICOS DA HOME
→ governam o que pode ser materializado naquela Home e naquela rodada

NÍVEL 2 — DOCUMENTO MESTRE E CONTRATOS COMPLEMENTARES VIGENTES
→ governam significado, narrativa, experiência e fronteiras

NÍVEL 3 — AUTORIDADES SUPERIORES DE PRODUTO
→ resolvem dúvidas sobre identidade, autoridade e limites

FORA DA CADEIA OPERACIONAL — HISTÓRICO / PROVENIÊNCIA
→ não carregar em Design ou IA
→ consultar somente para auditoria do repositório
```

Se houver conflito sobre significado da Home, prevalecem as autoridades específicas vigentes da Home conforme seu Source Lock.

---

## 6. Controle semântico do input generativo

Toda execução deve começar por um **Source Lock operacional específico da Home**.

O Source Lock deve registrar:

- Home;
- objetivo da execução;
- Handoff utilizado;
- Documento Mestre e contratos aplicáveis;
- versões;
- commit/checkpoint do GKR;
- decisões adicionais autorizadas para a execução;
- questões abertas.

> **A ferramenta deve saber de quais fontes pode aprender antes de receber liberdade para propor forma.**

Não utilizar como input indiscriminado:

- todo o GKR;
- todas as oito Homes simultaneamente;
- documentos históricos misturados a documentos vigentes;
- rascunhos de conversa sem status governado;
- benchmark como requisito;
- output anterior de IA como fonte canônica.

---

## 7. Estrutura obrigatória do prompt

O prompt de exploração deve conter:

1. **Objetivo** — Home e artefato a explorar;
2. **Fontes autorizadas** — IDs e versões;
3. **Invariantes** — contratos que não podem ser reinterpretados;
4. **Liberdades de Design** — o que pode ser explorado;
5. **Proibições de inferência** — o que não pode ser inventado;
6. **Estado da saída** — `EXPLORAÇÃO / NÃO CANÔNICA`;
7. **Questões abertas** — lacunas devem ser sinalizadas, não preenchidas como decisão.

---

## 8. Liberdades de Design

Desde que preservados os contratos da Home, Design pode explorar:

- grid e composição;
- agrupamento visual dos movimentos;
- quantidade de dobras e seções físicas;
- hierarquia, densidade e ritmo;
- tipografia e escala;
- fotografia, vídeo e visualizações;
- cor, fundos e atmosferas;
- componentes;
- comportamento responsivo;
- Header e navegação;
- microinterações e motion;
- tratamento de CTAs;
- relação entre conteúdo e espaço;
- alternativas desktop e mobile;
- protótipos de interação.


Estas liberdades são deliberadamente amplas. Não existe requisito prévio de paleta, fonte, estilo fotográfico, sistema de ilustração, estética de ícones ou template visual comum imposto pelo GKR. A coerência entre as oito Homes deve resultar da qualidade da solução escolhida e dos princípios comuns da Guivos, sem transformar as páginas no mesmo template.

Tom de voz, headlines de apoio, microcopy e formulações editoriais não congeladas também podem ser propostas por Design/Content Design. Até aprovação humana, esse material deve permanecer classificado como `CONTENT_CANDIDATE` e não pode introduzir promessa, dado, disponibilidade ou claim não sustentado.
> **Movimento narrativo é contrato de progressão. Seção visual é decisão de Design.**

---

## 9. Limites de inferência

Sem nova decisão governada, ferramentas e Design não podem:

- redefinir o papel de uma Home;
- reinterpretar pergunta-mãe ou copy congelada;
- alterar protagonista da experiência;
- inventar produtos, serviços, funções ou fluxos;
- modificar taxonomias/ontologias canônicas;
- confundir Media e Blog;
- atribuir ao Media autoridade operacional de Travel ou Mall;
- atribuir a Ads autoridade editorial ou pertinência pessoal;
- transformar Business em Ads, HR software, LMS/LXP, plataforma de pontos ou controle individual;
- transformar Journey custeado pela empresa em Journey controlado pela empresa;
- garantir transformação, impacto ou resultado causal não comprovado;
- inventar métricas, cases, parceiros, depoimentos, disponibilidade ou prova social;
- tornar benchmark externo padrão visual da Guivos;
- expor a complexidade interna do ecossistema como se fosse a experiência do produto.

Quando faltar informação, produzir **hipótese identificada**, nunca falsa decisão.

---

## 10. Placeholder e conteúdo fictício

Placeholder é permitido para testar hierarquia, desde que explicitamente identificado.

Nunca representar como reais: parceiros/clientes não confirmados, indicadores de impacto, usuários, preços, descontos, avaliações, destinos, inventário, campanhas, histórias, depoimentos, estatísticas, provas sociais, KPIs de Intelligence, limites de planos, SLA, entitlements, integrações ou disponibilidade não formalizada.

Copy gerada pode apoiar exploração de Content Design, mas não substitui copy governada.

---

## 11. Mesma família, personalidades diferentes

```text
MESMA FAMÍLIA ≠ MESMO TEMPLATE
```

A coerência deve nascer de princípios comuns, qualidade, linguagem, comportamento e identidade do ecossistema. A expressão pode variar:

- **Pessoa** — amplitude, possibilidade e abertura;
- **Organizações e Coletivos** — participação, capacidade, responsabilidade e confiança;
- **Mall** — descoberta, comércio e confiança;
- **Travel** — inspiração, operação real e acesso direto;
- **Media** — descoberta editorial, curadoria, profundidade e humanidade;
- **Ads** — clareza comercial, contexto, tecnologia aplicada e conversão sem atrito;
- **Business** — evolução humana, possibilidade, capacidade empresarial, inteligência e escala global sem aparência de SaaS B2B genérico;
- **Intelligence** — **clareza emergindo da complexidade**; compreensão contextualizada, estrutura, precisão, relações, temporalidade e explicabilidade, com futuro sem previsão determinista.

Nenhuma Home deve ser reduzida ao estereótipo do seu setor.

---

## 12. Princípios comuns

A materialização deve preservar a Guivos como:

- orientada ao futuro e às possibilidades;
- simples na experiência;
- confiável;
- capaz de operar em escala ampla e global;
- tecnológica sem ser fria;
- sofisticada sem ser complexa;
- humana sem clichês;
- maior do que a soma dos próprios produtos.

A Home não deve ser prioritariamente uma lista de serviços.

---

## 13. Contrato específico — Guivos Intelligence

A materialização de Intelligence deve preservar:

```text
UNIDADE DE VALOR
→ compreensão útil e contextualizada

INFORMAÇÃO ≠ COMPREENSÃO
COMPREENDER ≠ DECIDIR
RELAÇÃO ≠ CAUSA
CORRELAÇÃO ≠ CAUSALIDADE
SINAL ≠ CERTEZA
TENDÊNCIA ≠ DESTINO
PERCEBER ANTES ≠ PREVER O FUTURO
TECNOLOGIA ≠ PRODUTO
```

### 13.1 Onze movimentos

Os **11 movimentos semânticos** da Home são obrigatórios como progressão funcional, mas não exigem 11 seções físicas.

Contratos de distinção:

```text
M03 ≠ M10
M04 ≠ M05
```

- M03 define por que Intelligence existe;
- M10 aprofunda por que relações importam;
- M04 mostra os resultados perceptíveis;
- M05 demonstra esses resultados de forma concreta;
- M08 deve dar peso real à explicabilidade e origem da leitura;
- M09 preserva autonomia e autoridade de decisão;
- M11 amplia horizonte sem afirmar previsão do futuro.

### 13.2 Duas frentes

Pessoa/Journey:

```text
INTELLIGENCE → produz compreensão
JOURNEY → governa a experiência
PESSOA → escolhe
```

Business/população:

```text
INTELLIGENCE → produz leitura populacional protegida
BUSINESS → governa a relação empresarial
EMPRESA → decide
```

A assimetria de privacidade é obrigatória: o que Intelligence pode conhecer para servir a pessoa não se converte automaticamente em informação revelável a uma organização.

### 13.3 Tecnologia subordinada

Intelligence não deve ser materializado como definição de:

- IA/LLM;
- chatbot;
- dashboard;
- Power BI;
- grafo;
- Neo4j;
- GraphRAG;
- API;
- relatório;
- motor autônomo de decisão;
- previsão do futuro;
- monitoramento individual/HR software.

Tecnologias podem explicar capacidades, nunca substituir o produto.

### 13.4 Linguagem visual

Direção conceitual:

```text
DISPERSÃO → RELAÇÃO
RUÍDO → PADRÃO
ESTADO → MUDANÇA
SINAL → MOVIMENTO PERCEPTÍVEL
NÚMERO → CONTEXTO
CONCLUSÃO → EXPLICAÇÃO
INFORMAÇÃO → COMPREENSÃO
```

Evitar: cérebro digital, rosto com circuitos, rede neural genérica, hologramas, HUD sci-fi, dashboard com dezenas de gráficos, nuvem de pontos sem função, código decorativo, globo conectado sem função, grafo decorativo, robô/chatbot protagonista.

### 13.5 Dados e exemplos

```text
EXEMPLO CONCEITUAL ≠ EVIDÊNCIA OPERACIONAL
PLACEHOLDER ≠ DADO REAL
VISUALIZAÇÃO ≠ CLAIM COMPROVADO
```

Cada exemplo analítico demonstra **um tipo de leitura**, não prova que a capacidade está operacional em produção.

---

## 14. Fluxo recomendado

```text
PACOTE OFICIAL DA EMISSÃO VIGENTE
↓
LEIA-PRIMEIRO COMUM
↓
ESCOLHER UMA HOME
↓
LEIA-PRIMEIRO DA HOME
↓
FONTES CANÔNICAS ISOLADAS
↓
SOURCE LOCK / HANDOFF / GENINPUT ESPECÍFICOS
↓
OUTPUT = EXPLORAÇÃO
↓
VALIDAÇÃO HUMANA
```

A emissão do pacote não substitui a execução de Design.

---

## 15. Estados dos outputs

```text
EXPLORAÇÃO
→ proposta ainda não validada

CANDIDATO
→ direção selecionada para avaliação

VALIDADO EM UX
→ estrutura aceita; UI ainda pode evoluir

VALIDADO EM UI
→ direção visual aceita

APROVADO PARA HANDOFF DE ENGENHARIA
→ somente após decisão específica posterior
```

Nenhum output generativo nasce `canônico` ou `aprovado`.

---

## 16. Registro mínimo de cada exploração

Registrar:

- Home;
- problema explorado;
- documentos e versões usados;
- checkpoint do GKR;
- ferramenta;
- decisões preservadas;
- hipóteses introduzidas;
- dúvidas abertas;
- estado do output.

---

## 17. Critérios de aceite

O processo está alinhado quando:

1. Design inicia sem reconstruir o histórico completo do GKR;
2. cada Home possui suas fontes obrigatórias identificadas;
3. a ferramenta recebe fontes governadas, não corpus indiscriminado;
4. decisão canônica e hipótese de Design permanecem distintas;
5. as oito Homes pertencem à mesma Guivos sem virar o mesmo template;
6. nenhum produto, feature, dado, prova ou promessa é inventado para preencher layout;
7. movimentos governados permanecem preservados sem obrigação de seções equivalentes;
8. acessibilidade, mobile e performance participam da validação;
9. nenhum output visual passa a governar o GKR sem decisão posterior;
10. Business preserva seus limites vigentes;
11. Intelligence preserva os 11 movimentos, `M03 ≠ M10`, `M04 ≠ M05`, M08, M09, M11 não preditivo e a separação Pessoa/Journey versus Business/população;
12. Intelligence é percebido como compreensão contextualizada — não dashboard, chatbot, IA decisora, predição, HR monitoring ou produto Neo4j;
13. exemplos analíticos fictícios/conceituais permanecem identificados;
14. a emissão canônica prepara e entrega contexto; não substitui a execução da designer.

---

## 18. Regra para novas Homes

Novas Homes devem adotar o mesmo método:

```text
DOCUMENTO MESTRE
+
CONTRATOS COMPLEMENTARES
+
HANDOFF CANÔNICO
↓
SOURCE LOCK / GENINPUT
↓
EMISSÃO DO PACOTE
↓
EXPLORAÇÃO EXTERNA
↓
VALIDAÇÃO HUMANA
```

---

## 19. Síntese

> **O GKR governa o significado. Design governa a materialização. Ferramentas generativas ampliam a exploração. A validação reconecta forma e significado.**

A versão `1.3.0` incorporou formalmente a Home Pública — Guivos Intelligence ao Handoff comum, elevando a governança de sete para oito Homes sem iniciar Design nem emitir, por aquele ato isolado, um novo snapshot de entrega.

Estado histórico daquela frente:

> **HANDOFF DAS OITO HOMES PREPARADO PARA A GERAÇÃO DE ENTREGA V4 — MATERIALIZAÇÃO SOMENTE APÓS O GATE OPERACIONAL DO MANIFESTO/FLUXO VIGENTES — IMPLEMENTAÇÃO NÃO INCLUÍDA.**

---

## 20. Estado corrente

```text
HANDOFF / MÉTODO
→ ACTIVE / CURRENT

8 HOMES
→ COVERED

CANONICAL INPUT
→ CURRENT MAIN + CURRENT MANIFEST

VISUAL IDENTITY
→ DESIGN-OWNED / NOT CANONICALLY PRE-LOCKED

EXTERNAL DESIGNER CREATION
→ MANUAL FIRST-CLASS
→ AI OPTIONAL / DESIGNER-CONTROLLED

DESIGN PRODUCTION RELEASE
→ GRANTED

SNAPSHOT REQUIREMENT
→ NONE

HISTORICAL INPUT
→ EXCLUDED

FINAL DESIGN ACCEPTANCE
→ HUMAN / SEPARATE

IMPLEMENTATION / PRODUCT ENGINEERING
→ NOT RELEASED BY THIS HANDOFF
```


Este documento governa **como** o handoff deve ocorrer. O Manifesto corrente define o conjunto de fontes; histórico e proveniência ficam fora da cadeia de consumo de Design/IA.