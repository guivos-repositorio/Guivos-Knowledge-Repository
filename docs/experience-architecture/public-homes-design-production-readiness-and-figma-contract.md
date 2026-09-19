---
id: GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
title: Homes Públicas — Prontidão de Produção de Design e Contrato de Consumo Documental
status: active
version: 2.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: v6_tool_neutral_design_readiness_under_remediation
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
  - GKR-UX-HOMES-DESIGN-CONSUMPTION-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-BRAND-SIGNATURE-001
  - GOG-001
---

# Homes Públicas — Prontidão de Produção de Design e Contrato de Consumo Documental

## 1. Finalidade

Esta autoridade prepara as oito Homes públicas para consumo profissional por uma designer humana e, opcionalmente, por sistemas de IA de apoio.

O objetivo é reduzir a zero os findings materiais documentais antes da entrega, sem transformar documentação em direção artística e sem impor ferramenta, protótipo intermediário ou processo de criação visual.

O arquivo mantém seu path histórico por estabilidade de referências; a autoridade corrente é tool-neutral e deve ser lida junto de `GKR-UX-HOMES-DESIGN-CONSUMPTION-001`.

## 2. Resultado executivo

Estado corrente:

- arquitetura semântica das oito Homes: preservada;
- snapshot v5: congelado e histórico;
- fluxo Figma Make → aprovação → Figma definitivo: removido do processo governado;
- designer: autora primária da expressão visual;
- sistemas de IA: apoio opcional, consumindo as mesmas fontes;
- identidade visual: deliberadamente Design-owned;
- pacote v6: próximo pacote corrente, ainda dependente da remediação 8/8, validação e emissão;
- GKR: não cria, edita nem governa arquivos Figma.

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

A designer decide como registra e mantém suas escolhas criativas no ambiente de trabalho contratado. O GKR não define estrutura de arquivo, ferramenta, biblioteca ou workflow visual. Revisão e aceite da entrega pertencem ao processo humano/contratual de Design; o GKR continua autoridade apenas sobre significado, função, limites e verdade.

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

### F-05 — contrato de entrega de Design estava excessivamente acoplado à ferramenta

Decisão: substituir o contrato de arquivo/Figma por critérios tool-neutral de consumo documental e conformidade semântica, preservando a autonomia profissional da designer.

### F-06 — conteúdo aberto precisava de classificação por estágio

Decisão: toda informação não consolidada deve usar uma das classes da seção 8.

### F-07 — ausência de identidade visual canônica

Reclassificação humana: **não é gap**. É liberdade deliberada de Design.

## 6. Pacote fonte candidato v6 por Home

Cinco autoridades comuns acompanham todas as Homes:

1. `GKR-UX-HOMES-DESIGN-CONSUMPTION-001 v1.0.0`;
2. `GKR-UX-HOMES-DESIGN-HANDOFF-001 v2.0.0`;
3. `GKR-UX-HOMES-GENINPUT-001 v3.0.0`;
4. `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v2.0.0`;
5. `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.0`.

Fontes específicas:

### Pessoa
- `GKR-UX-HOME-MASTER-001 v1.1.0`;
- `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`.

### Organizações e Coletivos
- `GKR-UX-HOME-OC-MASTER-001 v1.1.0`;
- `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`.

### Mall
- `GKR-UX-HOME-MALL-MASTER-001 v1.0.1`;
- `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`.

O guia v6 da Home deve explicitar `MALL-HS-01..06`, preservando tese, condições de dados, ausência/erro, campanhas, personalização autorizada e identificação de patrocínio.

### Travel
- `GKR-UX-HOME-TRAVEL-MASTER-001 v1.0.1`;
- `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`.

O guia v6 da Home deve explicitar `TRAVEL-HS-01..06`, preservando baseline pública, serviço operacional, prova de destino/experiência, dados de oferta, indisponibilidade e campanha/patrocínio.

### Media
- `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.1`;
- `GPA-005 v1.2.0`.

### Ads
- `GKR-UX-HOME-ADS-MASTER-001 v1.0.1`;
- `GPA-007 v1.3.0`.

### Business
- `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.0.0`;
- `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.0`;
- `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
- `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
- `GPA-004 v1.6.0`.

### Intelligence
- `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
- `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
- `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.0`;
- `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
- `GPA-006 v2.0.0`.

### 6.9 Fechamento de fontes do candidato

```text
HOMES COM MASTER
→ 8 / 8

FONTES CANÔNICAS DO MANIFESTO V6
→ 27 / 27 DECLARADAS

AUTORIDADES COMUNS
→ 5 / 5

SOURCE LOCK / HANDOFF ESPECÍFICO VIGENTE
→ BUSINESS = INCLUDED
→ INTELLIGENCE = INCLUDED

PESSOA / O-C
→ MASTERS VIGENTES ABSORVEM A VERDADE DE CONSUMO
→ APROFUNDAMENTOS PERMANECEM CONSULTÁVEIS, NÃO CARREGADOS POR PADRÃO EM IA

MATERIAL DOCUMENT GAP IDENTIFIED IN SOURCE COMPOSITION
→ 0

EXACT-HEAD ID / VERSION / PATH / BLOB VALIDATION
→ REQUIRED BEFORE SNAPSHOT V6
```

A exclusão de aprofundamentos do contexto inicial não os invalida. Eles podem ser consultados deliberadamente para dúvida concreta.

## 7. Regra de isolamento para IA

IA é opcional e nunca constitui gate de Design.

Quando utilizada, deve trabalhar uma Home por vez e consumir `00-LEIA-PRIMEIRO` da Home + autoridades comuns + fontes específicas daquela Home.

A designer pode trabalhar sem IA. Quando houver output de IA, ele nasce como proposta de apoio e não como autoridade, aprovação ou identidade canônica.

## 8. Classes obrigatórias de informação

Toda informação relevante usada pela designer ou por sistema de IA de apoio deve estar tratável em uma destas oito classes:

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

Por isso, o Figma final deve testar envelopes realistas de conteúdo, incluindo quando aplicável:

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

Regras de integridade: conteúdo conceitual não pode parecer prova real; logos de terceiros exigem relação/autorização; preço, avaliação, usuários, disponibilidade e resultados não podem ser inventados; conteúdo provisório deve permanecer distinguível; assets externos devem respeitar licença; mídia essencial precisa de fallback.

Ferramenta, organização de arquivos e método de produção pertencem à designer e ao contrato externo de Design.

## 10. IA de apoio — opcional e sem gate obrigatório

Não existe etapa obrigatória de exploração generativa.

A designer pode criar manualmente desde o início. Se optar por IA, a ferramenta pode apoiar brainstorming, síntese, alternativas, conteúdo candidato ou exploração visual, desde que use as fontes governadas, preserve classes de informação, não invente fatos/produto/operação, mantenha hipóteses reversíveis e não substitua autoria humana.

## 11. Contrato mínimo da entrega externa de Design

Esta autoridade não determina como o arquivo visual deve ser estruturado.

A entrega deve preservar significado, hierarquia funcional e boundaries; contemplar desktop/mobile/responsividade no escopo contratado; considerar acessibilidade e reduced motion; distinguir conteúdo real, candidato e provisório; evitar claims ou dados inventados; suportar variação de conteúdo; e registrar assets/licenças aplicáveis no processo externo.

Auto Layout, components, libraries, variants, naming conventions e organização interna da ferramenta são decisões profissionais da designer, salvo requisito contratual separado. Não são autoridade do GKR.

## 12. Coerência entre as oito Homes

Objetivo: uma mesma Guivos, oito expressões adequadas ao papel de cada Home.

```text
MESMA FAMÍLIA
≠ MESMO TEMPLATE

PERSONALIDADE DIFERENTE
≠ MARCA DIFERENTE
```

A coerência pode emergir de qualidade, princípios, interação, linguagem e sistema criado pela designer. Não é necessário forçar mesmas cores, mesmos blocos ou mesma composição.

## 13. Critérios de prontidão para criação pela designer

Antes da entrega documental: zero divergência material entre fontes; papéis inequívocos; liberdade criativa separada de verdade canônica; dados reais necessários e perguntas abertas identificados; nenhuma escolha estética tratada como obrigação sem autoridade; fontes suficientes para criação sem reconstrução de arquitetura.

## 14. Critérios semânticos de revisão da entrega de Design

Uma entrega visual pode ser contrastada com o GKR para verificar papel e tese da Home, função dos movimentos, ausência de produto/dado/promessa inventados, preservação de autonomia/privacidade/causalidade, distinção entre publicidade/editorial/recomendação/relevância e não conversão de placeholders em prova.

Qualidade estética, originalidade, craft e direção visual pertencem ao processo humano de Design, não ao GKR.

## 15. Gate para o pacote corrente v6

O v5 permanece congelado e não será reescrito.

```text
REMEDIAR AUTORIDADES COMUNS
↓
REVISAR 8/8 MASTERS
↓
AUDITAR COMPLETUDE E PRESCRIÇÕES ESTÉTICAS
↓
VALIDAR SEMANTIC + MECHANICAL
↓
REVISÃO INDEPENDENTE
↓
ZERO FINDING MATERIAL ABERTO
↓
MERGE GOVERNADO
↓
CAPTURAR MAIN PÓS-MERGE
↓
GERAR 8 LEIA-PRIMEIRO TOOL-NEUTRAL
↓
MATERIALIZAR SNAPSHOT V6
↓
VALIDAR REPRODUTIBILIDADE
↓
ENTREGAR À DESIGNER
```

Nenhuma etapa cria ou edita Figma pelo GKR.

## 16. Estado

```text
DESIGN PRODUCTION READINESS
→ UNDER V6 TOOL-NEUTRAL REMEDIATION

VISUAL IDENTITY CANONICALIZATION
→ NOT REQUIRED / DESIGN-OWNED

V5 SNAPSHOT
→ FROZEN / HISTORICAL

V6 SNAPSHOT
→ NOT YET EMITTED

GKR FIGMA MATERIALIZATION
→ OUT OF PROCESS

DESIGNER
→ PRIMARY CREATIVE AUTHOR

AI
→ OPTIONAL SUPPORT
```
