---
id: GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
title: Homes Públicas — Prontidão de Produção de Design e Contrato Designer/IA
status: active
version: 1.2.13
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: designer_first_ai_optional_source_finalization
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-HOME-MASTERS-REMEDIATION-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-BRAND-SIGNATURE-001
  - GOG-001
---

# Homes Públicas — Prontidão de Produção de Design e Contrato Designer/IA


## 0. Correção de precedência — autoria da designer

Esta versão substitui qualquer leitura anterior que tratasse uma ferramenta generativa específica como fase necessária.

```text
DESIGNER
→ AUTHOR OF THE VISUAL SOLUTION
→ MANUAL WORK IS FIRST-CLASS

AI
→ OPTIONAL
→ DESIGNER-CONTROLLED

GKR / CHATGPT
→ DOES NOT CREATE THE DESIGN FILE
→ DOES NOT PRESELECT VISUAL DIRECTION

FINAL DESIGN TOOL
→ CONTRACTUAL / DESIGNER WORKFLOW DECISION
```

## 1. Finalidade

Esta autoridade prepara as oito Homes públicas da Guivos para uma contratação real de Design em que a designer cria manualmente com liberdade e pode usar sistemas de IA opcionalmente, sem ferramenta obrigatória definida pelo GKR.

O objetivo é reduzir a zero os findings materiais documentais antes do release de produção, sem transformar documentação em direção artística.

## 2. Resultado executivo

Baseline auditada: `main @ fada353688e26047a8eb8f45a8de67af0aa9b3d0`.

Estado desta revisão:

- arquitetura semântica das oito Homes: documentada e reconciliada;
- método de handoff: reconciliado pós-auditoria;
- template generativo: expandido para oito Homes;
- contrato de consumo, criação e entrega de Design: definido por esta autoridade;
- pacote v5: preparado pelo Manifesto v5, ainda dependente de emissão pós-merge;
- Design Production Release: não concedido por este documento.

## 3. Princípio superior — significado governado, criatividade livre

A Guivos não quer engessar a designer. Identidade visual não é um input canônico obrigatório desta frente.

Pertencem à liberdade criativa da designer:

- tipografia e escalas tipográficas;
- paleta e relações cromáticas;
- fotografia, vídeo, imagem gerada, ilustração e iconografia;
- grid, composição, densidade, respiro e ritmo;
- componentes e linguagem gráfica;
- motion, microinterações e atmosfera;
- tratamento visual de Header, Hero, CTAs e seções;
- tom de voz, headlines de apoio e microcopy quando não houver texto literal congelado;
- forma de tornar as oito Homes reconhecíveis como uma família sem repetir o mesmo template.

Não existe obrigação de reproduzir visual histórico, snapshot antigo, palette anterior, fonte anterior ou estética pré-existente.

Depois da aprovação humana da direção criativa, a solução escolhida passa a ser a baseline criativa daquela entrega e deve ser documentada no artefato final entregue pela designer. Mudança material posterior de conceito de Hero, linguagem visual, arquitetura de navegação, composição global ou direção criativa exige nova aprovação humana antes do aceite final; refinamentos não materiais permanecem sob autonomia da designer.

## 4. O que permanece governado

A liberdade visual não pode alterar:

- nomes oficiais de Guivos e Produtos Especializados;
- papéis de Pessoa, Organização e Coletivo;
- papel e fronteira de cada Home;
- `Possibilidade ≠ Oportunidade`;
- `COMPREENDER ≠ DECIDIR` e demais invariantes de Intelligence;
- distinção entre relevância orgânica, publicidade, recomendação e destaque;
- regras de autonomia, privacidade, causalidade e explicabilidade;
- realidade operacional, disponibilidade, preço, parceiro, case, métrica ou prova;
- assinatura institucional quando utilizada: `Possibility, lived.` / `Possibilidade, vivida.`;
- copy explicitamente classificada como congelada por autoridade específica.

## 5. Auditoria de produção — findings de baseline

### F-01 — snapshot v4 superado

O snapshot v4 nasceu de `f900318af746ba25e3bb18d18bfddee5654620c7`; a baseline desta auditoria está 785 commits à frente. Cinco das 31 fontes do v4 sofreram alteração, incluindo Handoff comum, Masters Pessoa/O/C e seus GENINPUTs.

Decisão: v4 permanece histórico e não pode ser entregue como pacote atual.

### F-02 — gates temporais da Auditoria Integral estavam obsoletos

Handoff, Manifest, Template e Flow ainda continham linguagem de suspensão durante auditoria, embora a auditoria global esteja concluída.

Decisão: reconciliar os quatro documentos para estado pós-auditoria.

### F-03 — template ainda descrevia cinco Homes

Decisão: `GKR-UX-HOMES-GENINPUT-001 v2.0.0` cobre as oito Homes.

### F-04 — Source Locks operacionais apontavam checkpoints antigos

Pessoa/O-C já estavam explicitamente reclassificados como evidência histórica; Mall, Travel, Media, Business, Ads e Intelligence também registravam checkpoints anteriores.

Decisão: o pacote v5 não usa GENINPUT histórico como autoridade operacional. Cada `LEIA-PRIMEIRO` do v5 funciona como Source Lock operacional daquela Home e registra o checkpoint exato da emissão.

### F-05 — aceite final do Design não estava suficientemente determinístico

Decisão: este documento estabelece o contrato mínimo de produção e aceite sem definir estética.

### F-06 — conteúdo aberto precisava de classificação por estágio

Decisão: toda informação não consolidada deve usar uma das classes da seção 8.

### F-07 — ausência de identidade visual canônica

Reclassificação humana: **não é gap**. É liberdade deliberada de Design.

## 6. Pacote fonte corrente / candidato v6 por Home

Cinco autoridades comuns acompanham todas as Homes:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001`;
2. `GKR-UX-HOMES-GENINPUT-001`;
3. `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001` — este documento;
4. `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001`;
5. `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001`.

As versões exatas do conjunto corrente são fixadas em `GKR-UX-HOMES-DESIGN-DELIVERY-V6-CANDIDATE-001`. O snapshot v5 permanece histórico e suas versões emitidas são preservadas por `GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001` e pelo Manifesto na seção histórica correspondente.

Fontes específicas:

### Pessoa
- `GKR-UX-HOME-MASTER-001 v1.0.3`;
- `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### Organizações e Coletivos
- `GKR-UX-HOME-OC-MASTER-001 v1.0.3`;
- `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### Mall
- `GKR-UX-HOME-MALL-MASTER-001 v1.1.1`;
- `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`.

Contrato corrente que o guia/Source Lock v6 deve explicitar:
- `MALL-HS-01 BASELINE_PUBLIC` — tese, pergunta-mãe, identidade Guivos e descoberta são base permanente;
- `MALL-HS-02 COMMERCIAL_DATA_AVAILABLE` — produto/oferta/preço/pontos/marca/parceiro somente com fonte aplicável;
- `MALL-HS-03 COMMERCIAL_DATA_UNAVAILABLE_OR_ERROR` — ausência não pode virar oferta, estoque, preço ou parceria fictícia;
- `MALL-HS-04 CAMPAIGN_ACTIVE` — campanha é temporária e não redefine a identidade da Home;
- `MALL-HS-05 PERSONALIZATION_AUTHORIZED` — recomendação pessoal exige base e autoridade; sem isso, usar descoberta/curadoria geral;
- `MALL-HS-06 SPONSORED_EXPOSURE` — exposição paga permanece identificada e não se disfarça de relevância orgânica.

### Travel
- `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.3`;
- `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

Contrato corrente que o guia/Source Lock v6 deve explicitar:
- `TRAVEL-HS-01 BASELINE_PUBLIC` — pergunta-mãe, identidade Guivos, inspiração e acesso a serviços são a base;
- `TRAVEL-HS-02 OPERATIONAL_SERVICE` — serviços governados podem ser apresentados sem inferir disponibilidade universal;
- `TRAVEL-HS-03 DESTINATION_OR_EXPERIENCE_PROVEN` — destino/imagem/experiência apresentados como reais exigem lastro;
- `TRAVEL-HS-04 OFFER_DATA_AVAILABLE` — preço, pontos, condição e disponibilidade somente quando sustentados;
- `TRAVEL-HS-05 OFFER_DATA_UNAVAILABLE_OR_ERROR` — ausência/erro não se convertem em tarifa, vaga, parceiro ou condição fictícios;
- `TRAVEL-HS-06 CAMPAIGN_OR_SPONSORED` — campanha é temporária e patrocínio permanece identificado.

### Media
- `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.1`;
- `GPA-005 v1.2.0`.

### Ads
- `GKR-UX-HOME-ADS-MASTER-001 v1.0.1`;
- `GPA-007 v1.3.0`.

### Business
- `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.1.6`;
- `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.3`;
- `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
- `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.3`;
- `GPA-004 v1.6.0`.

### Intelligence
- `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.1.9`;
- `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.1.8`;
- `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.7`;
- `GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.3`;
- `GKR-UX-HOMES-OUTCOME-001 v1.0.0`;
- `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.1`;
- `GPA-006 v2.0.1`.

O snapshot v5 deve capturar todas as fontes do mesmo commit canônico pós-merge e registrar seus SHAs.

### 6.9 Fechamento de fontes do candidato

A revisão desta frente verificou a composição do Manifesto v5 contra a branch candidata:

```text
HOMES COM MASTER
→ 8 / 8

FONTES CANÔNICAS DO MANIFESTO
→ 26 / 26 EXISTENTES

ID DECLARADO × ID REAL
→ 26 / 26 MATCH

VERSÃO DECLARADA × VERSÃO REAL
→ 26 / 26 MATCH

GENINPUT HISTÓRICO NO PACOTE OPERACIONAL
→ 0

SOURCE LOCK / HANDOFF ESPECÍFICO VIGENTE
→ BUSINESS = INCLUDED
→ INTELLIGENCE = INCLUDED

PESSOA / O-C
→ MASTERS VIGENTES ABSORVEM A VERDADE DE CONSUMO
→ DOCUMENTOS DE APROFUNDAMENTO PERMANECEM NO GKR, MAS NÃO ENTRAM AUTOMATICAMENTE NO CONTEXTO INICIAL DA IA

MATERIAL DOCUMENT GAP IDENTIFIED IN SOURCE CLOSURE
→ 0

FINAL EXACT-HEAD GATE
→ STILL REQUIRED
```

A exclusão de documentos de aprofundamento do pacote inicial não os invalida. Eles podem ser consultados deliberadamente para resolver dúvida concreta, mas não devem ser carregados indiscriminadamente em ferramentas de IA.

## 7. Regra de isolamento para IA

Quando IA for utilizada, trabalhar uma Home por vez. Não carregar documentos específicos das oito Homes simultaneamente.

A ferramenta deve receber: `LEIA-PRIMEIRO/SOURCE LOCK` daquela Home + cinco fontes comuns + fontes específicas daquela Home.

Output inicial obrigatório: `EXPLORAÇÃO / NÃO CANÔNICA`.

## 8. Classes obrigatórias de informação

Toda informação relevante usada pela designer ou por sistema de IA deve estar tratável em uma destas oito classes:

- `CANONICAL` — decisão governada que deve ser preservada;
- `DESIGN_CREATIVE` — campo deliberadamente aberto à criação da designer;
- `CONTENT_CANDIDATE` — copy, tom, label ou formulação editorial proposta e sujeita a aprovação humana;
- `DESIGN_HYPOTHESIS` — solução criada para testar uma interpretação de Design sem se tornar decisão da Guivos;
- `PROTOTYPE_PLACEHOLDER` — conteúdo provisório usado para testar hierarquia, volume, ritmo ou comportamento;
- `REAL_DATA_REQUIRED` — informação factual que exige fonte real antes de poder ser tratada como verdade pública;
- `OPEN_QUESTION` — decisão ainda não necessária ou não governada, com destino explícito;
- `PROHIBITED_INFERENCE` — conteúdo, regra ou claim que não pode ser criado para preencher a solução.

Nenhum item pode mudar de classe silenciosamente. Em especial:

```text
CONTENT_CANDIDATE
≠ CANONICAL UNTIL HUMAN APPROVAL

DESIGN_HYPOTHESIS
≠ PRODUCT DECISION

PROTOTYPE_PLACEHOLDER
≠ PUBLIC TRUTH

REAL_DATA_REQUIRED
≠ LICENSE TO INVENT

OPEN_QUESTION
≠ DESIGN BLOCKER BY DEFAULT
```

### 8.1 Matriz operacional das oito Homes

A matriz abaixo governa a classificação mínima que cada `LEIA-PRIMEIRO / SOURCE LOCK` v5 deverá tornar explícita.

#### Pessoa

- `CANONICAL` — papel institucional da Home; pergunta-mãe **“O que se torna possível quando você entra aqui?”**; possibilidade antes de produto; 11 movimentos; distinção participante × produto; Journey com porta própria; ausência de falsa personalização; autonomia, prova e confiança.
- `DESIGN_CREATIVE` — identidade visual, tipografia, cor, imagem, composição, motion, componentes, agrupamento físico e solução responsiva.
- `DESIGN_HYPOTHESIS` — alternativas de Hero, agrupamento dos 11 movimentos, navegação, densidade, ritmo e interação que podem ser testadas para tornar a tese mais clara sem alterar significado, prioridade semântica ou autonomia.
- `CONTENT_CANDIDATE` — terceira camada de concretização da Hero, CTA exploratório e microcopy não congelada.
- `PROTOTYPE_PLACEHOLDER` — histórias, imagens, conteúdo editorial e evidências ainda não selecionadas, sempre identificadas internamente como provisórias.
- `REAL_DATA_REQUIRED` — qualquer pessoa, organização, coletivo, parceiro, métrica, case, depoimento, país atendido, resultado ou prova apresentada como real.
- `OPEN_QUESTION` — copy pública final, composição integral do rodapé, disponibilidade operacional e decisões de lançamento; não bloqueiam Design quando a solução tolera sua substituição.
- `PROHIBITED_INFERENCE` — Momento pessoal presumido na Home pública, escala inventada, causalidade exagerada, produto antes da tese, `Organização = Business` ou Intelligence decidindo pela Pessoa.

#### Organizações e Coletivos

- `CANONICAL` — pergunta-mãe **“O que podemos tornar possível juntos?”**; Organização e Coletivo como participantes distintos; narrativa compartilhada antes da bifurcação final; 11 movimentos e 7 macroexperiências como significado, não layout; Header global; relevância contextual; autoridade, proteção, bilateralidade e evidência.
- `DESIGN_CREATIVE` — expressão visual, ritmo, mídia, composição, sistema gráfico, componentes e modo de representar a bifurcação final sem hierarquia indevida.
- `DESIGN_HYPOTHESIS` — alternativas para representar visualmente capacidades, relações, macroexperiências e a bifurcação Organização/Coletivo, desde que testáveis e reversíveis e sem criar superioridade, nova autoridade ou nova arquitetura.
- `CONTENT_CANDIDATE` — CTA exploratório da Hero e copy de apoio não congelada.
- `PROTOTYPE_PLACEHOLDER` — Organização, Coletivo, iniciativa, história e evidência ainda não selecionados.
- `REAL_DATA_REQUIRED` — identidade e relação real de Organizações/Coletivos, métricas, parcerias, iniciativas e provas apresentadas como existentes.
- `OPEN_QUESTION` — copy final, composição completa do rodapé e disponibilidade concreta dos destinos posteriores.
- `PROHIBITED_INFERENCE` — `Organização = Business`, Coletivo = comunidade da Guivos, relevância comprável, parceria fictícia, CTA comercial dominante na abertura ou coleta prematura de dados institucionais/pessoais.

#### Guivos Mall

- `CANONICAL` — pergunta-mãe **“O que pode fazer parte do seu próximo momento?”**; Shopping e Gift Cards como portas distintas; descoberta + comércio + confiança; Hero permanente não dominado por promoção; `MALL-HS-01..06`; separação entre oferta, recomendação, destaque e patrocínio.
- `DESIGN_CREATIVE` — composição comercial, direção de arte, visual de produtos, ritmo, navegação, cards ou alternativas que preservem o contrato.
- `DESIGN_HYPOTHESIS` — alternativas de descoberta, organização de ofertas, navegação entre Shopping/Gift Cards, densidade de catálogo e apresentação comercial que podem ser testadas sem alterar elegibilidade, confiança, preço, estoque ou natureza de recomendação/patrocínio.
- `CONTENT_CANDIDATE` — copy de apoio e labels comerciais não congelados.
- `PROTOTYPE_PLACEHOLDER` — produtos, preços, marcas, campanhas e conteúdos usados apenas para testar layout, claramente marcados no arquivo.
- `REAL_DATA_REQUIRED` — preço, preço em pontos, estoque, elegibilidade, desconto, marca/parceiro institucional, avaliação, disponibilidade e campanha apresentados como reais.
- `OPEN_QUESTION` — catálogo vivo, campanhas e condições comerciais futuras; a solução final deve suportar variação sem redesenho.
- `PROHIBITED_INFERENCE` — inventar estoque/preço, converter presença de marca em parceria, simular recomendação personalizada, fundir pontos com Gift Card ou mascarar mídia paga como relevância orgânica.

#### Guivos Travel

- `CANONICAL` — pergunta-mãe **“Até onde o seu próximo momento pode levar você?”**; inspiração + operação real + acesso direto; serviços, destinos e experiências como territórios distintos; Hero permanente não dominado por oferta; `TRAVEL-HS-01..06`.
- `DESIGN_CREATIVE` — fotografia, vídeo, mapas, composição, ritmo, navegação e modo de organizar os serviços sem transformá-los em nove produtos desconectados.
- `DESIGN_HYPOTHESIS` — alternativas de exploração por destino, serviço, inspiração, mapa, busca ou jornada visual que podem ser testadas sem inventar disponibilidade, bundle obrigatório, cobertura ou relação comercial.
- `CONTENT_CANDIDATE` — copy de apoio, labels e CTAs não congelados.
- `PROTOTYPE_PLACEHOLDER` — destinos, imagens, tarifas, experiências e conteúdos usados para teste, desde que explicitamente provisórios.
- `REAL_DATA_REQUIRED` — destino/oferta realmente disponível, tarifa, data, vaga, fornecedor, parceiro, condição comercial e experiência apresentada como real.
- `OPEN_QUESTION` — inventário, tarifa e disponibilidade futuros; o Design deve tolerar substituição e indisponibilidade sem retrabalho estrutural.
- `PROHIBITED_INFERENCE` — destino fictício apresentado como operado, cobertura mundial não comprovada, bundle obrigatório, parceria presumida ou patrocínio disfarçado de recomendação orgânica.

#### Guivos Media

- `CANONICAL` — tese editorial; pergunta-mãe **“O que você pode descobrir quando vê além do que já conhece?”**; curadoria antes de cronologia; 11 movimentos; descoberta antes de classificação; Media ≠ Blog/portal/feed/streaming.
- `DESIGN_CREATIVE` — direção editorial, tipografia, imagem, vídeo, ritmo, navegação, busca, motion e maneira de dar hierarquia ao conteúdo.
- `DESIGN_HYPOTHESIS` — alternativas de curadoria, destaque, descoberta, busca, agrupamento editorial e continuidade entre conteúdos que podem ser testadas sem transformar Media em feed, portal, streaming ou catálogo de formatos.
- `CONTENT_CANDIDATE` — headlines, labels e formulações editoriais não congeladas.
- `PROTOTYPE_PLACEHOLDER` — conteúdo de destaque, história, autor, imagem e vídeo usados para testar composição.
- `REAL_DATA_REQUIRED` — conteúdo, autor, pessoa, história, direitos de mídia, patrocínio, data ou relação apresentados como reais.
- `OPEN_QUESTION` — lineup editorial e conteúdo vivo de lançamento; não bloqueiam a arquitetura se os slots forem robustos.
- `PROHIBITED_INFERENCE` — história fictícia apresentada como real, feed cronológico como identidade, conteúdo patrocinado sem identificação ou formato transformado em arquitetura do produto.

#### Guivos Ads

- `CANONICAL` — tese contexto-first; 7 movimentos; capacidade financeira ≠ elegibilidade; autoridade da superfície anfitriã; publicidade identificada; qualificação progressiva; contexto pessoal protegido fora da comercialização.
- `DESIGN_CREATIVE` — expressão B2B, visualização de contextos, interação da qualificação, mídia, composição e linguagem visual.
- `DESIGN_HYPOTHESIS` — alternativas de qualificação progressiva, visualização dos contextos Guivos, apresentação das soluções e sequência comercial que podem ser testadas sem criar direito automático à exibição, segmentação proibida ou promessa de performance.
- `CONTENT_CANDIDATE` — headline, apoio e microcopy de conversão quando não congelados.
- `PROTOTYPE_PLACEHOLDER` — marca, campanha, formato, investimento e cenário comercial ilustrativos, sem aparência de operação vigente.
- `REAL_DATA_REQUIRED` — preço, CPM/CPC, alcance, inventário, performance, case, marca/parceiro e disponibilidade comercial apresentados como reais.
- `OPEN_QUESTION` — catálogo futuro de formatos, pricing e capacidade operacional por superfície.
- `PROHIBITED_INFERENCE` — compra de relevância pessoal, segmentação por contexto pessoal protegido, performance inventada, CPM/CPC como promessa ou autoridade Ads sobre conteúdo/experiência do produto anfitrião.

#### Guivos Business

- `CANONICAL` — Source Lock Business; pergunta-mãe **“O que sua empresa pode tornar possível para as pessoas?”**; 10 movimentos; quatro planos; exclusão pública de Pontos Guivos; autonomia da Pessoa; contratação/configuração online como direção; CTA e demais itens explicitamente congelados no Source Lock.
- `DESIGN_CREATIVE` — identidade visual, composição, agrupamento dos movimentos, representação dos planos, configurador, visualização de Intelligence e responsividade dentro do Source Lock.
- `DESIGN_HYPOTHESIS` — alternativas de comparação de planos, configuração, progressão comercial, visualização de capacidades e representação do Intelligence que podem ser testadas sem inventar preço, limites, SLA, entitlement ou alterar a autonomia da Pessoa.
- `CONTENT_CANDIDATE` — supporting copy e formulações não classificadas como congeladas.
- `PROTOTYPE_PLACEHOLDER` — preços, limites, entitlements, integrações e exemplos de configuração usados somente para teste.
- `REAL_DATA_REQUIRED` — preço final, limite de plano, SLA, entitlement, integração, disponibilidade por país/moeda, case, métrica ou condição comercial real.
- `OPEN_QUESTION` — detalhes comerciais ainda não formalizados; componentes devem tolerar valores e comprimentos reais sem redesenho.
- `PROHIBITED_INFERENCE` — inventar pricing/limites/SLA, transformar Business em software de RH/LMS/plataforma de pontos ou fazer a empresa decidir a evolução da Pessoa.

#### Guivos Intelligence

- `CANONICAL` — Home Source Lock e Handoff específicos; unidade de valor = compreensão útil e contextualizada; `COMPREENDER ≠ DECIDIR`; 11 movimentos; assimetria Pessoa/Journey × Business/população; copy e CTAs semanticamente congelados conforme o Home Source Lock.
- `DESIGN_CREATIVE` — forma visual de tornar relações, contexto, temporalidade, evidência e explicabilidade compreensíveis, sem obrigação de dashboard, grafo ou estética tecnológica específica.
- `DESIGN_HYPOTHESIS` — alternativas visuais para relações, padrões, mudanças, evidência, temporalidade e explicabilidade que podem ser testadas sem transformar Intelligence em decisão automática, previsão determinística, dashboard obrigatório ou tecnologia específica.
- `CONTENT_CANDIDATE` — somente microajustes/editorial não congelado dentro dos limites expressos pelo Source Lock.
- `PROTOTYPE_PLACEHOLDER` — exemplos analíticos e dados conceituais claramente marcados como ilustrativos.
- `REAL_DATA_REQUIRED` — métrica, resultado, acurácia, case, integração, tecnologia operacional, dado ou capacidade apresentada como existente.
- `OPEN_QUESTION` — expressão visual e exemplos finais; não autorizam inventar tecnologia ou performance.
- `PROHIBITED_INFERENCE` — Intelligence = chatbot/dashboard/Neo4j/IA decisora, previsão determinística, causalidade sem evidência, certeza a partir de tendência ou exposição de contexto pessoal protegido.

### 8.2 Regra de não bloqueio por conteúdo variável

Uma informação classificada como `OPEN_QUESTION`, `REAL_DATA_REQUIRED` ou `PROTOTYPE_PLACEHOLDER` não exige retrabalho posterior de Design quando sua variabilidade é previsível.

Por isso, o artefato final de Design deve ser validado com envelopes realistas de conteúdo, incluindo quando aplicável:

- títulos curtos e longos;
- traduções com expansão de texto;
- valores monetários e em pontos com diferentes comprimentos;
- presença e ausência de imagem;
- presença e ausência de preço/oferta;
- estados de indisponibilidade;
- cards/listas com diferentes quantidades;
- labels de patrocínio/proveniência;
- conteúdos sem prova disponível.

A substituição posterior de conteúdo ou dado dentro desses envelopes deve ser possível **sem reconstrução da arquitetura visual**.

## 9. Conteúdo, imagem e mídia

A designer pode selecionar, produzir ou gerar imagens e mídia de acordo com sua criatividade. O GKR não prescreve estética.

Regras de integridade:

- imagem conceitual não pode ser apresentada como case/evidência real;
- logos de terceiros exigem relação/autorização aplicável;
- preço, avaliação, número de usuários, disponibilidade e resultados não podem ser inventados;
- conteúdo gerado para protótipo deve ser reconhecível internamente como candidato ou placeholder;
- no artefato final, assets externos devem possuir origem/licença ou condição de uso registrada;
- mídia essencial deve possuir fallback e não pode carregar sozinha o significado da página.

## 10. Criação externa da designer — IA opcional

A designer não depende de exploração generativa prévia.

Sequência de referência:

1. compreender o pacote vigente da Home;
2. criar manualmente e/ou usar IA opcionalmente;
3. executar autoauditoria contra Master, Source Lock e autoridades aplicáveis;
4. apresentar a solução para revisão humana;
5. registrar ajustes materiais quando necessários;
6. concluir o artefato final de Design segundo o processo criativo da designer.

```text
MANUAL DESIGN
→ FIRST-CLASS

AI-ASSISTED DESIGN
→ OPTIONAL

GENERATIVE PROTOTYPE
→ NOT REQUIRED

GKR-CREATED DESIGN
→ NONE
```

## 11. Contrato mínimo do artefato final de Design

O contrato abaixo governa qualidade e editabilidade, não estética.

Cada Home entregue deve possuir:

- versão desktop e mobile completas;
- comportamento intermediário/responsivo resolvido ou documentado;
- frames e layers nomeados de forma compreensível;
- Auto Layout/constraints quando contribuírem para responsividade e manutenção;
- componentes reutilizáveis para padrões recorrentes;
- variants/properties/states quando um componente possuir comportamentos diferentes;
- estados necessários da navegação e interações principais;
- Header, menus/launcher, CTAs e scroll representados conforme aplicável;
- protótipo navegável das interações essenciais;
- tratamento de loading/empty/error/unavailable apenas quando a Home realmente exigir esses estados;
- organização de assets;
- indicação de origem/licença para assets externos aplicáveis;
- fontes tipográficas, plugins, bibliotecas e recursos pagos com licença, origem e condição de continuidade documentadas;
- arquivo final e bibliotecas essenciais acessíveis sob controle da Guivos, sem dependência exclusiva da conta pessoal da designer após o aceite;
- source assets editáveis ou origem reutilizável entregues quando forem necessários para manutenção futura;
- documentação das escolhas criativas aprovadas: cores, tipografia, estilos, componentes e demais foundations criadas pela designer;
- registro de placeholders e conteúdo variável, indicando classe, origem esperada e condição de substituição;
- componentes e layouts testados com envelopes realistas de conteúdo para que preço, tradução, ausência de mídia, indisponibilidade ou troca de copy não exijam redesenho estrutural;
- acessibilidade considerada desde a solução: contraste, foco, teclado, texto ampliado, reduced motion, touch targets, mídia e ordem semântica;
- internacionalização tolerando expansão/contração de texto;
- nenhuma dependência de hover ou motion para entendimento essencial.

A foundations page ou biblioteca visual criada pela designer é **entrega derivada da direção aprovada**, não identidade canônica pré-imposta.

## 12. Coerência entre as oito Homes

Objetivo: uma mesma Guivos, oito expressões adequadas ao papel de cada Home.

```text
MESMA FAMÍLIA
≠ MESMO TEMPLATE

PERSONALIDADE DIFERENTE
≠ MARCA DIFERENTE
```

A coerência pode emergir de qualidade, princípios, interação, linguagem e sistema criado pela designer. Não é necessário forçar mesmas cores, mesmos blocos ou mesma composição.

## 13. Critérios de aceite da direção/protótipo

Antes de consolidar o artefato final de Design:

- zero divergência material de significado;
- nenhum produto/participante confundido;
- nenhuma informação fictícia apresentada como fato;
- mobile possui solução própria, não mero empilhamento automático;
- a direção criativa foi aprovada por humano;
- copy candidata relevante foi aprovada ou marcada para substituição;
- questões abertas possuem destino explícito.

## 14. Critérios de aceite do Design final

A entrega pode ser aceita quando:

1. as oito Homes contratadas estão completas no escopo combinado;
2. desktop/mobile e responsividade estão resolvidos;
3. componentes e estados recorrentes são reutilizáveis;
4. protótipo demonstra interações essenciais;
5. nenhum asset essencial está ausente;
6. nenhuma fonte, plugin, biblioteca ou asset externo essencial tem condição de uso/continuidade desconhecida;
7. o arquivo, componentes e bibliotecas essenciais podem continuar sob controle da Guivos sem dependência da conta pessoal da designer;
8. não existem claims, parceiros, dados ou disponibilidade fictícios sem rótulo;
9. acessibilidade estrutural está considerada;
10. foundations criadas pela designer estão documentadas no arquivo;
11. a solução permanece fiel aos contratos semânticos;
12. a solução preserva criatividade e originalidade, sem se reduzir a template de benchmark;
13. as oito Homes passaram por revisão integrada de coerência como família Guivos sem obrigação de mesmo template;
14. não há finding material aberto;
15. existe registro formal do aceite final com versão do arquivo, responsável, assets/licenças e controle dos arquivos essenciais pela Guivos.

```text
FINAL DESIGN CANDIDATO
≠ SERVIÇO CONCLUÍDO

FINAL DESIGN ACCEPTED
→ PRÉ-CONDIÇÃO DE FECHAMENTO OPERACIONAL DA ENTREGA DE DESIGN

TERMOS DE PAGAMENTO / CONTRATO
→ GOVERNADOS FORA DESTE DOCUMENTO
```

## 15. Gate de emissão v5 e release

Antes de qualquer início definitivo:

```text
MERGE DO PACOTE DE PRONTIDÃO
↓
CAPTURAR MAIN PÓS-MERGE
↓
REVALIDAR 26/26 FONTES CANÔNICAS DO MANIFESTO V5
↓
GERAR 8 LEIA-PRIMEIRO / SOURCE LOCKS OPERACIONAIS
↓
MATERIALIZAR SNAPSHOT EXTERNO V5
↓
VALIDAR REPRODUTIBILIDADE / ISOLAMENTO
↓
SEMANTIC + MECHANICAL
↓
REVISÃO INDEPENDENTE
↓
ZERO FINDING MATERIAL ABERTO
↓
ATO HUMANO EXPLÍCITO DE DESIGN PRODUCTION RELEASE
```

O gate humano foi posteriormente satisfeito por `GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.0.0`. A autorização libera o início da fase de Design, sem antecipar os gates internos de direção criativa, aceite final de Design ou implementação.

## 16. Estado

```text
DESIGN PRODUCTION READINESS DOCUMENTATION
→ INTEGRATED / ACTIVE

VISUAL IDENTITY CANONICALIZATION
→ NOT REQUIRED / DELIBERATELY DESIGN-OWNED

V5 SNAPSHOT
→ EMITTED / MATERIALIZED / VALIDATED

DESIGN PRODUCTION RELEASE
→ GRANTED / GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001 v1.1.0

AI-ASSISTED DESIGN
→ AUTHORIZED TO EXECUTE / NOT_STARTED

FINAL DESIGN PRODUCTION
→ NOT_RELEASED / REQUIRES HUMAN DIRECTION APPROVAL
```