---
id: GKR-UX-HOMES-DESIGN-HANDOFF-001
title: Homes Públicas — Handoff Canônico para Design, UX, UI e Ferramentas Generativas
status: active
version: 1.2.0
owner: Experience Architecture
last_updated: 2026-08-16
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
  - GKR-UX-HOME-BUSINESS-SOURCELOCK-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GPA-004
---

# Homes Públicas — Handoff Canônico para Design, UX, UI e Ferramentas Generativas

## 1. Finalidade

Este documento governa o **handoff das sete Homes públicas já convergidas da Guivos para a fase de Design, UX, UI, wireframe e prototipação**.

Seu objetivo é permitir que a pessoa responsável por Design trabalhe com um conjunto pequeno, atual e semanticamente controlado de fontes, sem precisar reconstruir decisões a partir do histórico completo do Guivos Knowledge Repository.

As sete Homes abrangidas por esta versão são:

1. Home Pública — Pessoa;
2. Home Pública — Organizações e Coletivos;
3. Home Pública — Guivos Mall;
4. Home Pública — Guivos Travel;
5. Home Pública — Guivos Media;
6. Home Pública — Guivos Ads;
7. Home Pública — Guivos Business.

Este documento **não desenha as páginas** e não determina solução visual final. Ele define quais decisões precisam ser preservadas, quais fontes têm autoridade, como ferramentas generativas podem ser utilizadas e onde termina a arquitetura governada e começa a liberdade de Design.

A inclusão de Business nesta versão segue a mesma lógica das Homes anteriores:

```text
GKR
→ prepara autoridades, Source Lock, prompt e pacote de entrega

DESIGN / FIGMA MAKE / FERRAMENTA EQUIVALENTE
→ produz a exploração visual fora desta frente canônica

VALIDAÇÃO HUMANA
→ confronta a exploração com o GKR
```

Portanto, **a atualização deste handoff não cria mapa de página, wireframe, direção visual, UI ou protótipo dentro do GKR**.

---

## 2. Autorização da fase de Design

A partir deste handoff, ficam autorizadas para as sete Homes abrangidas, quando executadas pela frente de Design e pelo pacote de entrega vigente:

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

Alguns Documentos Mestres ou Source Locks registram historicamente estados como `materialização não autorizada` ou afirmam que o documento isolado não autoriza wireframe/UI. A presente decisão **supera somente esse estado procedimental para a fase de Design** das Homes abrangidas.

Ela não revoga, substitui ou enfraquece nenhuma decisão semântica, narrativa, funcional, comercial, de produto ou de fronteira registrada nesses documentos.

Regra:

> **O handoff autoriza materializar externamente. Os Documentos Mestres, contratos e Source Locks continuam governando o que não pode ser semanticamente perdido durante a materialização.**

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

A composição operacional de cada emissão é governada por `GKR-UX-HOMES-DESIGN-DELIVERY-001`.

A designer não precisa receber o repositório inteiro como entrada inicial.

### 4.1 Home Pública — Pessoa

Usar o Handoff Canônico comum e as autoridades específicas registradas no Manifesto de Entrega vigente, incluindo Documento Mestre, reconciliação pós-Media e Source Lock + Prompt.

### 4.2 Home Pública — Organizações e Coletivos

Usar o Handoff Canônico comum e as autoridades específicas registradas no Manifesto de Entrega vigente, incluindo Documento Mestre, reconciliação pós-Media e Source Lock + Prompt.

### 4.3 Home Pública — Guivos Mall

Usar o Handoff Canônico comum e as autoridades específicas registradas no Manifesto de Entrega vigente, incluindo Documento Mestre, reconciliação pós-Media e Source Lock + Prompt.

### 4.4 Home Pública — Guivos Travel

Usar o Handoff Canônico comum e as autoridades específicas registradas no Manifesto de Entrega vigente, incluindo Documento Mestre, reconciliação pós-Media e Source Lock + Prompt.

### 4.5 Home Pública — Guivos Media

Usar o Handoff Canônico comum e as autoridades específicas registradas no Manifesto de Entrega vigente, incluindo Documento Mestre, `GPA-005` e Source Lock + Prompt.

### 4.6 Home Pública — Guivos Ads

Usar o Handoff Canônico comum e as autoridades específicas registradas no Manifesto de Entrega vigente, incluindo Documento Mestre, `GPA-007` e Source Lock + Prompt.

### 4.7 Home Pública — Guivos Business

O contexto inicial de Business é deliberadamente mais amplo porque suas fronteiras comerciais e de autoridade são distribuídas por documentos especializados já convergidos.

Usar somente o pacote definido pelo Manifesto de Entrega vigente, baseado em:

1. `GKR-UX-HOME-BUSINESS-SOURCELOCK-001`;
2. `GKR-UX-HOME-BUSINESS-MASTER-001`;
3. `GKR-UX-HOME-BUSINESS-CONVERSION-002`;
4. `GKR-UX-HOME-BUSINESS-AUTHORITY-001`;
5. `GPA-004`;
6. Source Lock Operacional + Prompt específico de Business emitido para a rodada de Design.

Não substituir esse contexto por documentos históricos, conversão v1, materiais de Ads, benchmarks ou rascunhos de conversa.

---

## 5. Ordem de autoridade

Quando os documentos forem consumidos por uma pessoa ou por uma ferramenta generativa, a ordem geral é:

```text
NÍVEL 0 — HANDOFF CANÔNICO
GKR-UX-HOMES-DESIGN-HANDOFF-001
→ governa processo, autorização, fontes e uso de IA

NÍVEL 1 — SOURCE LOCK / DOCUMENTO MESTRE DA HOME
→ governa identidade, significado, narrativa, experiência e invariantes congelados

NÍVEL 2 — CONTRATO COMPLEMENTAR VIGENTE
→ reconciliação pós-Media
  ou GPA-005 no caso da Home Media
  ou GPA-007 no caso da Home Ads
  ou Conversão + Contratos de Autoridade + GPA-004 no caso da Home Business

NÍVEL 3 — DOCUMENTOS ESPECIALIZADOS
→ consultados somente quando uma dúvida concreta exigir aprofundamento

NÍVEL 4 — HISTÓRICO
→ explica como uma decisão foi construída
→ não substitui o estado vigente
```

No caso de Business, a ordem detalhada entre Source Lock, Documento Mestre, Conversão, Contratos de Autoridade e `GPA-004` é a registrada em `GKR-UX-HOME-BUSINESS-SOURCELOCK-001`.

Se houver conflito aparente entre uma antiga proibição procedimental de materialização e este documento, prevalece este handoff **somente quanto à autorização da fase de Design**.

Se houver conflito sobre significado da Home, prevalecem as autoridades específicas vigentes da Home conforme o Source Lock correspondente.

---

## 6. Controle semântico do input generativo

Toda execução em Figma Make ou ferramenta generativa deve começar por um **Source Lock operacional específico da Home**.

O Source Lock registra:

- Home em trabalho;
- objetivo da execução;
- documento de handoff utilizado;
- Documento Mestre utilizado;
- contratos complementares utilizados;
- versões dos documentos;
- commit ou checkpoint do GKR de onde os arquivos foram extraídos;
- decisões adicionais autorizadas especificamente para aquela execução;
- questões ainda abertas.

Regra:

> **A ferramenta deve saber de quais fontes pode aprender antes de receber liberdade para propor forma.**

Não utilizar como input indiscriminado:

- todo o GKR;
- todas as sete Homes simultaneamente;
- documentos históricos misturados a documentos vigentes;
- rascunhos de conversa sem status governado;
- benchmark como se fosse requisito;
- output anterior de IA como se fosse fonte canônica.

Exceções devem ser deliberadas e registradas.

---

## 7. Estrutura obrigatória do prompt de exploração

O prompt enviado à ferramenta generativa deve conter, nesta ordem conceitual:

### A. Objetivo
Qual Home está sendo trabalhada e qual artefato a frente de Design deseja explorar.

### B. Fontes autorizadas
Listar as fontes do pacote daquela Home com IDs e versões.

### C. Invariantes
Repetir os contratos que não podem ser reinterpretados naquela execução.

### D. Liberdades de Design
Explicitar o que a frente de Design pode explorar livremente.

### E. Proibições de inferência
Explicitar o que não pode ser inventado para preencher lacunas.

### F. Estado da saída
Declarar que o resultado é **exploratório e não canônico** até validação.

### G. Questões abertas
Quando uma fonte não responde algo, a ferramenta deve sinalizar a lacuna em vez de criar uma decisão de produto por conta própria.

---

## 8. O que ferramentas generativas podem explorar

Desde que preservados os contratos da Home, podem propor na frente externa de Design:

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
- transformar Business em Ads, HR software, LMS/LXP, plataforma de pontos ou mecanismo de controle individual;
- transformar Journey custeado pela empresa em Journey controlado pela empresa;
- recolocar Pontos na narrativa pública da Home Business;
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

- nomes de parceiros ou clientes não confirmados;
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
- provas sociais;
- KPIs reais de Intelligence;
- limites de planos;
- SLA;
- entitlements;
- integrações não formalizadas;
- países ou moedas ainda não formalmente disponíveis.

Copy proposta por IA pode ser usada como material de exploração de Content Design, mas não substitui copy final governada.

---

## 11. Mesma família, personalidades diferentes

As sete Homes devem pertencer claramente à mesma Guivos, mas não devem parecer sete páginas produzidas pela simples substituição de textos dentro de um template único.

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
- **Ads** — clareza comercial, contexto, tecnologia aplicada e conversão sem atrito;
- **Business** — evolução humana, possibilidade, capacidade empresarial, inteligência e escala global sem aparência de SaaS B2B genérico.

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

A Home não deve ser construída prioritariamente como uma lista de serviços. No caso específico do Ads, sua natureza comercial permite linguagem mais direta e orientada a objetivos, sem convertê-lo em catálogo técnico de mídia. No Business, capacidade comercial e contratação devem aparecer sem deslocar evolução humana e possibilidades do centro narrativo.

---

## 13. Fluxo recomendado para a frente de Design

A frente externa de Design deve seguir:

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
SOURCE LOCK + PROMPT
↓
OUTPUT = EXPLORAÇÃO
↓
VALIDAÇÃO HUMANA
```

A definição de mapa, wireframe, direção visual, UI ou protótipo pertence à execução de Design e **não é produzida por este handoff nem pelo ato canônico de emissão do pacote**.

---

## 14. Classificação dos outputs

Todo artefato produzido externamente deve possuir um estado explícito:

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
7. as sete Homes parecem pertencer à mesma Guivos sem virar o mesmo template;
8. nenhuma ferramenta inventa produto, feature, dado, prova ou promessa para preencher layout;
9. os movimentos governados de cada Home permanecem preservados sem obrigação de seções visuais equivalentes;
10. a solução é validada humanamente antes de qualquer promoção de estado;
11. acessibilidade, mobile e performance participam da validação de Design;
12. nenhum output visual passa a governar o GKR sem decisão explícita posterior;
13. Business preserva Pontos fora da Home, Journey antes de Incentivos, Intelligence visual, contratação online e seus modelos de implementação/operação;
14. a emissão canônica apenas prepara e entrega o contexto; ela não substitui a execução da designer.

---

## 18. Regra para novas Homes

Novas Homes especializadas, incluindo futuras superfícies ainda não convergidas, devem adotar este mesmo método:

```text
DOCUMENTO MESTRE
+
CONTRATOS COMPLEMENTARES NECESSÁRIOS
+
GKR-UX-HOMES-DESIGN-HANDOFF-001
↓
SOURCE LOCK
↓
EMISSÃO DO PACOTE
↓
EXPLORAÇÃO EXTERNA
↓
VALIDAÇÃO HUMANA
```

A composição exata do contexto específico pode variar conforme a arquitetura do produto, mas deve ser declarada antes de qualquer exploração generativa.

---

## 19. Síntese

O objetivo deste handoff não é restringir criatividade visual.

É impedir que liberdade de materialização seja confundida com liberdade para redesenhar o significado das Homes.

> **O GKR governa o significado. Design governa a materialização. Ferramentas generativas ampliam a exploração. A validação reconecta forma e significado.**

A versão 1.2.0 amplia o handoff para a Home Pública — Guivos Business, preservando o método já aplicado às Homes anteriores e sem produzir material visual dentro desta frente.

Estado desta frente:

> **HANDOFF DAS SETE HOMES PARA DESIGN AUTORIZADO — EMISSÃO E INPUT GENERATIVO SOB CONTROLE SEMÂNTICO — IMPLEMENTAÇÃO NÃO INCLUÍDA NESTE ESCOPO.**
