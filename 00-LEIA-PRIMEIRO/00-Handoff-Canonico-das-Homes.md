---
id: GKR-UX-HOMES-DESIGN-HANDOFF-001
title: Homes Públicas — Handoff Canônico para Design, UX, UI e Ferramentas Generativas
status: active
version: 1.1.0
owner: Experience Architecture
last_updated: 2026-08-14
normative: true
depends_on:
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
---

# Homes Públicas — Handoff Canônico para Design, UX, UI e Ferramentas Generativas

## 1. Finalidade

Este documento governa o **handoff das seis Homes públicas já convergidas da Guivos para a fase de Design, UX, UI, wireframe e prototipação**.

Seu objetivo é permitir que Design trabalhe com um conjunto pequeno, atual e semanticamente controlado de fontes, sem precisar reconstruir decisões a partir do histórico completo do Guivos Knowledge Repository.

As seis Homes abrangidas por esta versão são:

1. Home Pública — Pessoa;
2. Home Pública — Organizações e Coletivos;
3. Home Pública — Guivos Mall;
4. Home Pública — Guivos Travel;
5. Home Pública — Guivos Media;
6. Home Pública — Guivos Ads.

Este documento **não desenha as páginas** e não determina solução visual final. Ele define quais decisões precisam ser preservadas, quais fontes têm autoridade, como ferramentas generativas podem ser utilizadas e onde termina a arquitetura governada e começa a liberdade de Design.

---

## 2. Autorização da fase de Design

A partir deste handoff, ficam autorizadas para as seis Homes abrangidas:

- exploração em Figma Make e ferramentas equivalentes;
- arquitetura visual;
- wireframes de baixa fidelidade;
- exploração de UX;
- exploração de direção visual;
- UI de alta fidelidade;
- protótipos de navegação e interação;
- estudos responsivos para desktop e mobile;
- validação das soluções contra os contratos do GKR.

Esta autorização é **procedimental e limitada à fase de Design**.

Ela não autoriza automaticamente:

- desenvolvimento frontend ou backend;
- publicação em produção;
- alteração de arquitetura de produto;
- mudança de modelo econômico;
- criação de funcionalidades não governadas;
- alteração de posicionamento;
- Marketing/GTM;
- novas promessas, métricas, parceiros, ofertas ou claims não sustentados;
- merge de implementação.

Alguns Documentos Mestres registram historicamente estados como `materialização não autorizada` ou afirmam que o documento isolado não autoriza wireframe/UI. A presente decisão **supera somente esse estado procedimental para a fase de Design**.

Ela não revoga, substitui ou enfraquece nenhuma decisão semântica, narrativa, funcional, de produto ou de fronteira registrada nesses documentos.

Regra:

> **O handoff autoriza materializar. Os Documentos Mestres continuam governando o que não pode ser semanticamente perdido durante a materialização.**

---

## 3. Princípio central

> **Figma Make e outras ferramentas generativas são instrumentos de exploração e materialização, não fontes de decisão sobre a arquitetura das Homes.**

Consequência:

```text
GKR
→ define significado, função, narrativa, fronteiras e invariantes

DESIGN + FERRAMENTAS GENERATIVAS
→ exploram como esses contratos podem ganhar forma

VALIDAÇÃO
→ verifica se a forma preservou o significado
```

Uma solução visual produzida por IA, Figma Make, plugin, template, benchmark ou referência externa **não se torna canônica por ter sido gerada**.

Somente após validação humana contra o GKR uma direção pode ser aceita como evolução da experiência.

---

## 4. Pacote oficial de handoff

O pacote obrigatório possui **13 documentos de autoridade**: este documento comum e dois documentos específicos por Home. A emissão operacional adiciona um Source Lock por Home conforme o Manifesto Canônico de Entrega.

### 4.1 Home Pública — Pessoa

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` — este documento;
2. `docs/experience-architecture/public-home-master-document.md`;
3. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md`.

### 4.2 Home Pública — Organizações e Coletivos

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` — este documento;
2. `docs/experience-architecture/public-home-organizations-collectives-master-document.md`;
3. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md`.

### 4.3 Home Pública — Guivos Mall

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` — este documento;
2. `docs/experience-architecture/public-home-mall-master-document.md`;
3. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md`.

### 4.4 Home Pública — Guivos Travel

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` — este documento;
2. `docs/experience-architecture/public-home-travel-master-document.md`;
3. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md`.

### 4.5 Home Pública — Guivos Media

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` — este documento;
2. `docs/experience-architecture/public-home-media-master-document.md`;
3. `docs/product-architecture/media.md` (`GPA-005`).

### 4.6 Home Pública — Guivos Ads

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001` — este documento;
2. `docs/experience-architecture/public-home-ads-master-document.md`;
3. `docs/product-architecture/ads.md` (`GPA-007`).

A designer não precisa receber o repositório inteiro como entrada inicial.

---

## 5. Ordem de autoridade

Quando os documentos forem consumidos por uma pessoa ou por uma ferramenta generativa, a ordem de autoridade é:

```text
NÍVEL 0 — HANDOFF CANÔNICO
GKR-UX-HOMES-DESIGN-HANDOFF-001
→ governa processo, autorização, fontes e uso de IA

NÍVEL 1 — DOCUMENTO MESTRE DA HOME
→ governa identidade, significado, narrativa, experiência e invariantes da Home

NÍVEL 2 — CONTRATO COMPLEMENTAR VIGENTE
→ reconciliação pós-Media
  ou GPA-005 no caso da Home Media
  ou GPA-007 no caso da Home Ads
→ governa relações especializadas sem substituir o Documento Mestre

NÍVEL 3 — DOCUMENTOS ESPECIALIZADOS
→ consultados somente quando uma dúvida concreta exigir aprofundamento

NÍVEL 4 — HISTÓRICO
→ explica como uma decisão foi construída
→ não substitui o estado vigente
```

Se houver conflito aparente entre uma antiga proibição procedimental de materialização e este documento, prevalece este handoff **somente quanto à autorização da fase de Design**.

Se houver conflito sobre significado da Home, prevalece o Documento Mestre correspondente, salvo decisão posterior explicitamente governada.

---

## 6. Controle semântico do input generativo

Toda execução em Figma Make ou ferramenta generativa deve começar por um **Source Lock**.

O Source Lock registra:

- Home em trabalho;
- objetivo da execução;
- fase: arquitetura visual, wireframe, UX, UI ou protótipo;
- documento de handoff utilizado;
- Documento Mestre utilizado;
- contrato complementar utilizado;
- versões dos documentos;
- commit ou checkpoint do GKR de onde os arquivos foram extraídos;
- decisões adicionais autorizadas especificamente para aquela execução;
- questões ainda abertas.

Regra:

> **A ferramenta deve saber de quais fontes pode aprender antes de receber liberdade para propor forma.**

Não utilizar como input indiscriminado:

- todo o GKR;
- todas as seis Homes simultaneamente;
- documentos históricos misturados a documentos vigentes;
- rascunhos de conversa sem status governado;
- benchmark como se fosse requisito;
- output anterior de IA como se fosse fonte canônica.

Exceções devem ser deliberadas e registradas.

---

## 7. Estrutura obrigatória do prompt de exploração

O prompt enviado a uma ferramenta generativa deve conter, nesta ordem conceitual:

### A. Objetivo

Qual Home está sendo trabalhada e qual artefato precisa ser produzido.

### B. Fontes autorizadas

Listar o handoff, o Documento Mestre e o contrato complementar com seus IDs e versões.

### C. Invariantes

Repetir os contratos que não podem ser reinterpretados naquela execução.

### D. Liberdades de Design

Explicitar o que pode ser explorado livremente.

### E. Proibições de inferência

Explicitar o que não pode ser inventado para preencher lacunas.

### F. Estado da saída

Declarar que o resultado é **exploratório e não canônico** até validação.

### G. Questões abertas

Quando uma fonte não responde algo, a ferramenta deve sinalizar a lacuna em vez de criar uma decisão de produto por conta própria.

---

## 8. O que ferramentas generativas podem explorar

Desde que preservados os contratos da Home, podem propor:

- grid;
- composição;
- agrupamento visual dos movimentos;
- quantidade de dobras;
- hierarquia visual;
- densidade;
- ritmo;
- tipografia;
- escala tipográfica;
- direção de fotografia e vídeo;
- uso de cor;
- fundos e atmosferas;
- componentes;
- comportamento responsivo;
- soluções para Header e navegação;
- microinterações;
- motion;
- tratamento de CTAs;
- relação entre conteúdo e espaço;
- alternativas desktop e mobile;
- protótipos de interação.

A quantidade de movimentos narrativos ou funcionais governados por uma Home **não implica a mesma quantidade de blocos visuais equivalentes**.

> **Movimento narrativo é contrato de progressão. Seção visual é decisão de Design.**

---

## 9. O que ferramentas generativas não podem decidir

Sem nova decisão governada, não podem:

- redefinir o papel de uma Home;
- trocar ou reinterpretar sua pergunta-mãe quando houver uma governada;
- transformar produtos em protagonistas antes da tese quando o Documento Mestre proíbe isso;
- alterar o protagonista da experiência;
- inventar produtos, serviços, funcionalidades ou fluxos;
- modificar taxonomias e ontologias canônicas;
- transformar Guivos Podcast em produto independente;
- confundir Guivos Media e Guivos Blog;
- confundir conteúdo editorial, recomendação, oferta e publicidade;
- atribuir ao Media autoridade operacional de Travel ou Mall;
- atribuir a Ads autoridade editorial, relevância orgânica ou pertinência pessoal;
- garantir transformação, impacto ou resultado causal não comprovado;
- inventar métricas, números, avaliações, cases, parceiros, depoimentos ou disponibilidade;
- criar campanhas como se fossem vigentes;
- preencher ausência de conteúdo real com evidência fictícia;
- converter exemplos explicativos em regras de UI obrigatórias;
- tornar benchmark externo padrão visual da Guivos;
- substituir simplicidade de experiência por exposição da complexidade interna do ecossistema.

Quando a ferramenta precisar de informação inexistente, deve produzir uma **hipótese identificada**, nunca uma falsa decisão.

---

## 10. Placeholder, copy e conteúdo fictício

Ferramentas podem usar conteúdo provisório para testar hierarquia, desde que ele seja explicitamente identificado como placeholder.

Não utilizar como se fossem reais:

- nomes de parceiros não confirmados;
- indicadores de impacto;
- número de usuários;
- preços;
- descontos;
- avaliações;
- destinos disponíveis;
- inventário comercial;
- dados de campanhas;
- histórias de pessoas;
- depoimentos;
- estatísticas;
- provas sociais.

Copy proposta por IA pode ser usada como material de exploração de Content Design, mas não substitui copy final governada.

---

## 11. Mesma família, personalidades diferentes

As seis Homes devem pertencer claramente à mesma Guivos, mas não devem parecer seis páginas produzidas pela simples substituição de textos dentro de um template único.

```text
MESMA FAMÍLIA
≠
MESMO TEMPLATE
```

A coerência deve nascer de princípios comuns, qualidade, linguagem, comportamento e identidade do ecossistema.

A expressão visual pode variar conforme o papel de cada superfície:

- **Pessoa** — amplitude, possibilidade e abertura;
- **Organizações e Coletivos** — participação, capacidade, responsabilidade e confiança;
- **Mall** — descoberta, comércio e confiança;
- **Travel** — inspiração, operação real e acesso direto;
- **Media** — descoberta editorial, curadoria, profundidade e humanidade;
- **Ads** — clareza comercial, contexto, tecnologia aplicada e conversão sem atrito.

Nenhuma Home deve ser visualmente reduzida ao estereótipo do seu setor.

---

## 12. Princípios comuns das Homes

A materialização deve preservar a percepção da Guivos como:

- orientada ao futuro e às possibilidades;
- simples na experiência;
- confiável;
- capaz de operar em escala ampla e global;
- tecnológica sem ser fria;
- sofisticada sem ser complexa;
- humana sem recorrer a clichês;
- maior do que a soma dos próprios produtos.

A Home não deve ser construída prioritariamente como uma lista de serviços. No caso específico do Ads, sua natureza comercial permite linguagem mais direta e orientada a objetivos, sem convertê-lo em catálogo técnico de mídia.

---

## 13. Fluxo recomendado de Design

### Etapa 1 — Source Lock e compreensão

- confirmar os três documentos autorizados da Home;
- registrar versões e checkpoint;
- identificar invariantes, liberdades e questões abertas.

### Etapa 2 — Arquitetura visual

- mapa de página;
- hierarquia;
- agrupamento dos movimentos;
- wireframe low-fi desktop e mobile.

### Gate de UX

Validar estrutura e significado antes de investir em refinamento visual.

### Etapa 3 — Direção visual

Explorar linguagem, tipografia, mídia, composição, ritmo, cor e atmosfera.

### Etapa 4 — UI

Construir alta fidelidade, componentes, estados essenciais e comportamento responsivo.

### Etapa 5 — Protótipo

Materializar navegação, microinterações e motion quando realmente contribuírem para a experiência.

### Gate final

Confrontar a solução com:

1. este handoff;
2. Documento Mestre;
3. contrato complementar;
4. Source Lock vigente da execução;
5. acessibilidade;
6. performance;
7. coerência entre as seis Homes.

---

## 14. Classificação dos outputs

Todo artefato produzido deve possuir um estado explícito:

```text
EXPLORAÇÃO
→ proposta ainda não validada

CANDIDATO
→ direção selecionada para avaliação

VALIDADO EM UX
→ estrutura aceita, UI ainda pode evoluir

VALIDADO EM UI
→ direção visual aceita

APROVADO PARA HANDOFF DE ENGENHARIA
→ somente após decisão específica posterior
```

Nenhum output de Figma Make deve nascer com o estado `canônico` ou `aprovado`.

---

## 15. Registro mínimo de cada exploração

Cada execução relevante deve conseguir responder:

- qual Home foi trabalhada;
- qual problema estava sendo explorado;
- quais documentos alimentaram a execução;
- qual checkpoint do GKR foi utilizado;
- qual ferramenta foi usada;
- quais decisões foram preservadas;
- quais hipóteses foram introduzidas;
- quais dúvidas continuam abertas;
- qual é o estado do output.

Isso permite reproduzir, revisar e rejeitar uma direção sem perder rastreabilidade.

---

## 16. Materiais históricos e referências externas

Documentos históricos permanecem importantes para auditoria e aprofundamento, mas não pertencem ao input inicial obrigatório.

Benchmarks, referências visuais, concorrentes, moodboards e estudos de mercado podem apoiar exploração visual, porém:

> **referência inspira; não governa.**

Se um documento especializado for necessário para resolver uma dúvida, ele deve ser adicionado ao Source Lock daquela execução e sua função deve ser explicitada.

---

## 17. Critérios de aceite do handoff

O processo está alinhado quando:

1. Design consegue iniciar sem navegar pelo histórico completo do GKR;
2. cada Home possui exatamente suas fontes obrigatórias identificadas;
3. frases históricas de não autorização não bloqueiam a fase atual de Design;
4. essas frases não são usadas como justificativa para alterar decisões semânticas;
5. a ferramenta generativa recebe fontes governadas e não um corpus indiscriminado;
6. o output distingue decisão canônica de hipótese de Design;
7. as seis Homes parecem pertencer à mesma Guivos sem virar o mesmo template;
8. nenhuma ferramenta inventa produto, feature, dado, prova ou promessa para preencher layout;
9. os movimentos governados de cada Home permanecem preservados sem obrigação de seções visuais equivalentes;
10. a solução é validada em UX antes do refinamento final de UI;
11. acessibilidade, mobile e performance participam da validação;
12. nenhum output visual passa a governar o GKR sem decisão explícita posterior.

---

## 18. Regra para novas Homes

Novas Homes especializadas, incluindo futuras superfícies ainda não convergidas, devem adotar este mesmo método:

```text
DOCUMENTO MESTRE
+
CONTRATO COMPLEMENTAR NECESSÁRIO
+
GKR-UX-HOMES-DESIGN-HANDOFF-001
↓
SOURCE LOCK
↓
EXPLORAÇÃO
↓
VALIDAÇÃO UX
↓
VALIDAÇÃO UI
```

A composição exata do par específico pode variar conforme a arquitetura do produto, mas deve ser declarada antes de qualquer exploração generativa.

---

## 19. Síntese

O objetivo deste handoff não é restringir criatividade visual.

É impedir que liberdade de materialização seja confundida com liberdade para redesenhar o significado das Homes.

> **O GKR governa o significado. Design governa a materialização. Ferramentas generativas ampliam a exploração. A validação reconecta forma e significado.**

A versão 1.1.0 amplia o handoff para a Home Pública — Guivos Ads e preserva sua natureza comercial distinta sem transferir ao Ads a autoridade funcional das superfícies anfitriãs.

Estado desta frente:

> **HANDOFF DAS SEIS HOMES PARA DESIGN AUTORIZADO — INPUT GENERATIVO SOB CONTROLE SEMÂNTICO — IMPLEMENTAÇÃO NÃO INCLUÍDA NESTE ESCOPO.**