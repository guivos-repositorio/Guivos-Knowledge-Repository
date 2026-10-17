---
id: GKR-UX-GLOBAL-FOOTER-SURFACE-001
title: Superfície Transversal — Rodapé Global da Guivos
status: proposed
version: 0.2.10
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
maturity: design_candidate
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-GLOBAL-FOOTER-001
---

# Rodapé Global — superfície transversal da Guivos

> **Superfície de projeto candidata.** Este documento define uma arquitetura editorial e de experiência a ser validada para o rodapé de todas as Homes públicas e páginas elegíveis da Guivos. Não substitui a autoridade de cada produto, não aprova novos destinos, não cria páginas jurídicas e não equivale à implementação.

## 0. Precedência sobre a referência visual validada (reconciliação de 16/10/2026)

**Autoridade corrente já existente na `main`:** [Rodapé Institucional Global — Referência Validada](global-institutional-footer.md), `GKR-UX-GLOBAL-FOOTER-001 v1.0.0`, `status: validated-visual-reference`, `normative: true`, baseada na composição aprovada pelo fundador em 14/10/2026. Esta PR não é autorização para redesenhar a composição, suprimir conteúdo aprovado ou substituir seus textos. Os módulos R01–R06 abaixo são **um mapa lógico de responsabilidades** para implementação transversal, e não um novo copywriting, wireframe de substituição ou revisão do Design validado.

**Elementos já fixados e que deverão ser preservados em qualquer composição conforme a referência:**
- assinatura de marca: **Possibility, lived.**;
- posicionamento: **Conectamos pessoas a possibilidades que podem transformar suas vidas.**;
- seções: **Explore o ecossistema**, **Guivos**, **Ajuda** e **Receba novidades**;
- descrição do bloco de novidades: **Acompanhe novas oportunidades, experiências e possibilidades que surgem e evoluem no ecossistema Guivos.**;
- chamada final: **Descubra. Viva. Evolua.**, com destaque cromático em **Evolua.**;
- fundo `#FFFFFF`, paleta oficial, família Goldplay conforme autoridade tipográfica e respiros da referência visual;
- navegação institucional e jurídica, campo voluntário de novidades e canais sociais conforme a referência, **sem presumir destinos ou integração ativos**.

**Complementos em exame neste documento:** `Mapa do Ecossistema` como responsabilidade de navegação referida pela autoridade da Home, aplicação em outras Homes, estados responsivos, ajuda e variações por contexto. O item `Mapa do Ecossistema` não substitui os grupos/itens aprovados no rodapé nem vira link clicável sem destino autorizado. Para qualquer diferença entre o wireframe lógico da §4 e a referência validada, **prevalece a referência validada**, sujeita às autoridades legais, de marca e acessibilidade pertinentes.

**Lacunas de implantação:** a referência corrente não comprova ativo vetorial, links, captação de novidades, publicação, mobile ou integração. O botão/QR de obtenção do app, se proposto em iteração visual posterior, exige registro de conteúdo e destino oficiais antes de integrar a superfície de produção; não presumir que já esteja contemplado pela referência normativa de 14/10. Nenhuma implementação é autorizada por esta reconciliação.

## 1. Papel e princípios

O Rodapé é uma **superfície transversal de orientação, confiança, continuidade e compreensão do ecossistema**, não uma nona Home, uma vitrine extensa de serviços ou um funil compulsório. Sua função é permitir que a Pessoa, Organização ou Coletivo compreenda a Guivos, transite entre superfícies, encontre assistência e acesse informações institucionais e legais verificadas.

- Preservar sensação de ecossistema único, global e territorialmente relevante, sem alegar presença efetiva em países não atendidos.
- Respeitar a liberdade criativa de Design definida pelas autoridades comuns do GKR; esta especificação fixa **funções, agrupamentos, prioridades e limites**, não grade visual, cor, dimensão ou tecnologia.
- Manter consistência estrutural nas oito Homes e páginas internas, com adaptação contextual limitada e rastreável.
- Não antecipar acesso, serviço, recurso social, programa ou página inexistente.
- Preservar a autonomia de navegação e o acesso por teclado, leitura assistiva e dispositivos móveis.

## 2. Estrutura conceitual da superfície

### R01 — Identidade e continuidade

Identidade Guivos, frase curta de posicionamento vinculada ao significado institucional corrente e, **quando adequado ao contexto e autoridade de marca**, assinatura `Possibility, lived.`. Uma mensagem de encerramento não deve substituir o conteúdo narrativo próprio de cada Home.

### R02 — Explore o ecossistema

Área de orientação para os destinos publicamente disponíveis do ecossistema. Candidatos à arquitetura de informação:

- Pessoa e Journey;
- Organizações e Coletivos;
- Mall;
- Travel;
- Business;
- Media;
- Intelligence;
- Ads.

**Regra de presença:** destino só vira link clicável quando URL, finalidade pública e disponibilidade real forem confirmadas. Para superfícies ainda sem página, não usar `#`, links quebrados nem simular lançamento. A relação entre nome de produto, navegação e disponibilidade não autoriza promessa operacional.

### R03 — Mapa do Ecossistema — item obrigatório

**Obrigatório no rodapé:** link textual com nome exato **`Mapa do Ecossistema`**, conforme seção 31 de `GKR-UX-HOME-MASTER-001 v1.0.8`.

O destino, conteúdo e comportamento da futura página **não estão definidos por esta seção**. Antes de ativar o link em produção, resolver URL e arquitetura dessa página por decisão própria. Durante prototipação, o componente pode apresentar estado explicitamente rotulado como demonstração e não deve navegar a destino fictício.

### R04 — Sobre a Guivos

Entrada institucional de entendimento da plataforma, propósito, marca e informações corporativas que estiverem publicadas e aprovadas. A existência de `Sobre`, `Carreiras`, `Imprensa`, `Contato` ou redes sociais é **candidata**, não um inventário de páginas já existentes.

### R05 — Ajuda, confiança e direitos

Acesso simples às rotas efetivamente disponibilizadas de suporte, acessibilidade, privacidade, termos, preferências e canais de reporte. Não inventar canais de suporte, garantias legais, promessas de resposta, telefones, endereços ou contatos.

Os links legais definitivos, jurisdição, entidade editorial, cookies e meios de exercer direitos exigem validação por Legal/Privacidade e disponibilidade real.

### R05A — Receba novidades — função preservada da referência aprovada

O bloco **Receba novidades** é parte do rodapé validado em `GKR-UX-GLOBAL-FOOTER-001`, não uma opção editorial a ser omitida pelo wireframe lógico desta PR. Deve preservar título, descrição oficial, campo de e-mail, botão de envio e canais sociais conforme a referência, com adaptação responsiva sem exclusão de função.

Esse bloco é **distinto** de Ajuda e da faixa institucional inferior. A presença visual aprovada não comprova captação real, consentimento, integração, assinatura concluída, destinos ou contas oficiais das redes. Não ativar o formulário nem links sem validação de finalidade, privacidade e comportamento.

A designação R05A é **submódulo editorial desta proposta**, não ID de superfície nem alteração de `GKR-SURF` ou `GKR-TRN`.

### R06 — Faixa institucional inferior

Conjunto de informações factuais e revisadas que podem incluir identificação corporativa apropriada, direitos de marca, ano, políticas e controles de idioma/região quando estes existirem e forem operacionais. Não exibir país, moeda, seletor, número de CNPJ, símbolo de certificação ou texto de conformidade como adorno ou suposição.

## 3. Tratamento por tipo de página

| Superfície | Aplicação do rodapé |
|---|---|
| Home Pessoa | Completo, após a narrativa e o Movimento 11, sem repetir nem enfraquecer o CTA da Home |
| Home Organizações e Coletivos | Mesmo esqueleto, sem insinuar que selos pendentes estão concedidos |
| Homes Mall e Travel | Mesmo esqueleto; não prometer liquidação, parceiros, estoque ou disponibilidade não contratados |
| Homes Business, Media, Intelligence e Ads | Mesma arquitetura; não transformar itens de navegação em claims de operação |
| Páginas públicas internas | Rodapé completo ou condensado conforme extensão, mantendo `Mapa do Ecossistema` quando o contexto permitir |
| Formulários e fluxos autenticados sensíveis | Variante compacta de confiança e links legais, sem distrações e sem vazamento de estado privado; requisitos próprios devem ser validados |
| Telas de erro e indisponibilidade | Acesso mínimo a ajuda verificada, navegação e políticas quando possível |

A variação contextual altera **densidade e prioridade**, nunca o conteúdo normativo ou a existência de produtos.

## 4. Wireframe lógico — não visual final

```text
┌────────────────────────────────────────────────────────────────────┐
│ GUIVOS          Explore o ecossistema  Sobre  Ajuda  Receba novidades│
│ Posicionamento Destinos ativos        Guivos Apoio  E-mail / canais│
│                 Mapa do Ecossistema (destino a validar)             │
├────────────────────────────────────────────────────────────────────┤
│ Identificação factual  •  Privacidade/Termos aprovados  •  Controles│
└────────────────────────────────────────────────────────────────────┘
```

**Mobile:** módulos em sequência sem colunas comprimidas; agrupamentos expansíveis são opcionais, desde que nomeados e operáveis por teclado, sem ocultar links legais essenciais. **Desktop:** design pode usar distribuição em colunas, hierarquia editorial e presença imagética discreta. **Acessibilidade:** landmark de rodapé, títulos, links com propósito identificável, foco visível, contraste, leitura linear, movimento reduzido e alvos de toque adequados.

## 5. Arquitetura de dados e implementação

- **Única fonte de configuração de links**, com `id`, rótulo, finalidade, rota absoluta/interna, idioma, mercado, `available`, `approved` e versão de origem. Não inferir publicação a partir da existência de um Master.
- **Componente compartilhado** para todas as Homes, evitando oito rodapés divergentes; variações `full`, `compact` e `minimal` somente quando justificadas por contexto.
- Nenhum link deve existir funcionalmente sem URL validada; navegação externa deve identificar destino e observar boas práticas de segurança.
- Idioma e região devem refletir suporte real, não dropdowns demonstrativos apresentados como funcionalidade ativa.
- Pode usar fotografia, iconografia e visualização, mas os elementos não podem eclipsar navegação e informações de confiança.

## 6. Gates e critérios de aceite

| Gate | Necessário para declarar concluído |
|---|---|
| FTR-01 | Ratificação humana da arquitetura de informação e módulos |
| FTR-02 | Destinos e URLs ativas verificadas, sobretudo `Mapa do Ecossistema` |
| FTR-03 | Revisão Brand e coerência das oito Homes |
| FTR-04 | Revisão Legal/Privacidade de elementos legais e institucionais |
| FTR-05 | Design responsivo e validação de acessibilidade, inclusive teclado/leitor de tela |
| FTR-06 | Implementação de componente compartilhado e cobertura de rotas públicas elegíveis |
| FTR-07 | Testes de links, estados indisponíveis, mobile, regressão e navegação assistiva |
| FTR-08 | Aprovação de publicação e evidência de deploy real |

**Estado inicial:** `FTR-01..08 = NOT_ADJUDICATED`. A estrutura é uma proposta documentada para deliberação, não autorização de implantação ou anúncio de disponibilidade.

**Linha de base auditada em 16/10/2026:** os oito gates seguem **sem ratificação formal de conclusão**. O quadro abaixo indica evidência parcial, não aprovação tácita. A referência visual `GKR-UX-GLOBAL-FOOTER-001 v1.0.0` é válida e não precisa ser revalidada por esta PR.

| Gate | Evidência existente | Lacuna objetiva para concluir | Estado corrente |
|---|---|---|---|
| FTR-01 | Módulos R01–R06 e R05A documentados; referência visual aprovada | Ratificação específica da arquitetura transversal, variantes e integração de `Mapa do Ecossistema` | DOCUMENTED / NOT_ADJUDICATED |
| FTR-02 | Lista editorial de destinos no rodapé validado; Home Master §31 exige `Mapa do Ecossistema` | Mapa de URLs verificadas, disponibilidade de cada destino e tratamento de ausências | NOT_VERIFIED |
| FTR-03 | Assinaturas e sistema visual fixados pela referência aprovada, prevalência explícita neste candidato | Revisão de consistência da composição nas oito Homes e variantes, com evidência por contexto | PARTIAL_EVIDENCE / NOT_ADJUDICATED |
| FTR-04 | Textos institucionais e jurídicos registrados na referência visual | Verificação Legal/Privacidade de URLs, identificação, captação voluntária, avisos e canais | NOT_VERIFIED |
| FTR-05 | Diretrizes de acessibilidade e adaptação responsiva descritas | Protótipos/implementações mobile e tablet, teste de contraste, teclado e tecnologias assistivas | NOT_TESTED |
| FTR-06 | Proposta de componente compartilhado e configuração única | Implementação real auditada, cobertura das superfícies públicas elegíveis e configuração dos destinos | NOT_IMPLEMENTATION_EVIDENCED |
| FTR-07 | Critérios de testes descritos | Execução reproduzível de navegação, formulário, links, estados vazios/falhos, regressão e mobile | NOT_EXECUTED |
| FTR-08 | Referência visual aprovada pelo fundador | Aprovação de publicação **e** evidência verificável de deploy real | NOT_PUBLISHED_EVIDENCED |

**Regras de decisão:** `FTR-01` não é automaticamente satisfeito pela aprovação visual de 14/10; `FTR-03` possui base de marca, mas não auditoria completa das oito Homes; `FTR-02` não se satisfaz por rótulos de link ou rotas fictícias; `FTR-06..08` exigem evidência de interface, teste e deploy, não apenas texto. O link do `Mapa do Ecossistema` é obrigação arquitetural da Home Pessoa, mas seu destino ainda não está validado. O QR/app, se incorporado após 14/10, deverá ser reconciliado com uma referência visual posterior identificada, sem inventar QR real ou disponibilidade em lojas.

**Sequência admissível:** conclusão documental da PR apenas como **candidata não normativa** após checks de CI e exame de precedência; decisão humana FTR-01/FTR-03; confirmação de destinos e responsabilidade jurídica FTR-02/FTR-04; materialização e provas FTR-05..08 em trilha própria. Merge documental **não equivale** a autorização de execução.



## 6.1. Reconciliação documental de FTR-01 e FTR-03 nas oito Homes — 16/10/2026

**Natureza:** exame de compatibilidade documental da proposta transversal com os oito Documentos Mestres públicos. Não é ratificação humana de FTR-01, não comprova reprodução visual ou cobertura real nas oito Homes e não encerra FTR-03. Mantém a referência `GKR-UX-GLOBAL-FOOTER-001 v1.0.0` como autoridade visual e verbal aprovada.

### FTR-01 — arquitetura de informação e módulos

| Função | Fonte de precedência | Síntese candidata para uso transversal | Limite |
|---|---|---|---|
| Identidade e posicionamento | Rodapé Institucional Global validado, guia de marca | **R01** mantém logotipo, `Possibility, lived.` e a mensagem institucional textual exata | Não substituir a assinatura de marca nem a mensagem validada |
| Exploração do ecossistema | Rodapé validado + Home Pessoa §31 | **R02** preserva a coluna `Explore o ecossistema`; **R03** adiciona a obrigação de `Mapa do Ecossistema` no rodapé | Obrigação do item não comprova página, URL ou link ativo; não retirar itens previamente aprovados |
| Informação institucional | Rodapé validado | **R04** preserva grupo `Guivos` e itens editoriais aprovados | Não pressupor páginas de Carreiras, Imprensa ou Comunidade publicadas |
| Ajuda e direitos | Rodapé validado + competências Legal/Privacidade | **R05** preserva grupo `Ajuda`, separando apoio e links jurídicos | Destinos e textos legais definitivos exigem verificação competente |
| Novidades e canais | Rodapé validado | **R05A** preserva `Receba novidades`, texto aprovado, campo, ação e ícones sociais | Formulário, tratamento de dados e canais não estão operacionais por inferência |
| Faixa inferior | Rodapé validado | **R06** mantém identificação corporativa, links jurídicos e `Descubra. Viva. Evolua.` | Número de registro, símbolo, informações e links devem seguir a referência factual e revisão pertinente |
| Componentização | Proposta transversal | Um contrato semântico compartilhável com densidade contextual nas páginas elegíveis | Não impor grid, breakpoint ou paridade visual fictícia; implementação depende de FTR-05..08 |

**Resultado FTR-01:** `CONTENT_AND_MODULE_CROSSWALK = DOCUMENTED`; `ARCHITECTURE_RATIFICATION = PENDING`. A composição validada em 14/10 **não ratifica automaticamente** o acréscimo `Mapa do Ecossistema` ou variantes compactas nas oito Homes. A decisão humana deverá confirmar localização, convivência com os itens aprovados, variantes contextuais e tratamento de destino ausente.

### FTR-03 — confronto individual com os oito Masters ativos

| Home | Documento Mestre ativo conferido | Convergência de arquitetura de rodapé | Risco contextual e limite |
|---|---|---|---|
| Pessoa | `GKR-UX-HOME-MASTER-001 v1.0.8` | §31 exige link `Mapa do Ecossistema`; rodapé pós-narrativa, sem absorver Movimento 11 | Não criar página do Mapa nem alterar o CTA narrativo por inferência |
| Organizações e Coletivos | `GKR-UX-HOME-OC-MASTER-001 v1.0.7` | Usa identidade pública Guivos e rodapé compartilhado, incluindo decisão de Mapa | Não converter Coletivo em Organização/Business nem exibir selos pendentes |
| Mall | `GKR-UX-HOME-MALL-MASTER-001 v1.1.4` | Identidade e navegação comuns compatíveis | Saldo de pontos pertence ao contexto global de conta, não ao rodapé público; não prometer paridade ou checkout |
| Travel | `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.6` | Identidade e navegação comuns compatíveis | Não antecipar reserva, disponibilidade, preços em pontos ou acordos de resgate |
| Business | `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.10` | Identidade institucional comum sem alterar a Home B2B | Não confundir plano recorrente, recursos para incentivos e orçamento separado; liberdade criativa interna preservada |
| Media | `GKR-UX-HOME-MEDIA-MASTER-001 v1.0.3` | Identidade transversal compatível | Não apresentar canal editorial, podcast, rede ou página como efetivamente publicada sem fonte |
| Intelligence | `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v0.2.14` | Identidade transversal compatível | Não transformar IA em autoridade individual nem prometer sistemas operacionais não comprovados |
| Ads | `GKR-UX-HOME-ADS-MASTER-001 v1.0.3` | Identidade transversal compatível | Não converter navegação, marca ou rodapé em inventário de anúncios, oferta ativa ou distribuição garantida |

**Cobertura da auditoria documental:** 8/8 Masters examinados para fronteiras de semântica e autoridade; **não** significa oito protótipos/implementações validados, 8/8 de aprovação de Design, nem resultados de testes. A ausência de contradição semântica evidente no recorte do rodapé não substitui a auditoria de conteúdo e layout de cada Home.

**Resultado FTR-03:** `MASTER_CONTEXT_CROSSWALK = 8/8_DOCUMENTED`; `BRAND_REFERENCE = VALIDATED_FOR_FOOTER`; `EIGHT_HOME_VISUAL_REVIEW = NOT_EVIDENCED`; `FTR-03 = NOT_ADJUDICATED`.

### Gates humanos remanescentes sem inventar decisão

1. **FTR-01/D1 — posição aceita:** registrar o rótulo `Mapa do Ecossistema` ao final da coluna `Explore o ecossistema`; **a decisão sobre exibição de um item sem destino real em produção permanece pendente de FTR-02**, e nenhum link operacional pode ser presumido.
2. **FTR-01/D2:** aprovar a semântica de variantes `full`, `compact` e `minimal` sem suprimir acesso jurídico essencial; versão mobile depende de design e testes.
3. **FTR-03/D1:** confrontar a composição real em cada uma das oito Homes com a referência validada; registrar capturas, revisão de Brand/Design e diferenças legítimas.
4. **FTR-03/D2:** resolver eventual conflito entre a referência aprovada em 14/10 e iterações visuais posteriores (por exemplo, acesso ao app por QR Code), **somente mediante nova evidência visual identificável**, não por lembrança editorial ou inferência de publicação.

**Critério de avanço:** após deliberação documentada de FTR-01, examinar FTR-03 com evidência visual 8/8; FTR-02/04/05/06/07/08 mantêm seus requisitos independentes. Não iniciar implementação, fazer merge de funcionalidades ou declarar publicação por esta análise.

## 6.2. FTR-01 — proposta decisória de localização do Mapa e FTR-03 — protocolo de evidência (16/10/2026)

### Localização do `Mapa do Ecossistema` — solução preferencial para apreciação humana

**Proposta:** acrescentar o item textual **`Mapa do Ecossistema` ao final da coluna `Explore o ecossistema`**, depois dos oito destinos aprovados (Pessoa e Journey; Organizações e Coletivos; Mall; Travel; Business; Media; Intelligence; Ads). O item será separado dos destinos por espaçamento editorial discreto, sem criar uma quinta coluna, nova faixa institucional ou CTA dominante.

**Justificativa:** a intenção é orientar a Pessoa sobre o conjunto do ecossistema; por isso o agrupamento de exploração é semanticamente mais adequado que `Guivos` (institucional), `Ajuda` (suporte) ou `Receba novidades` (captação voluntária). A ordem dos oito produtos e participantes, as assinaturas e a faixa inferior já aprovadas devem permanecer intactas. Tipografia Goldplay, fundo `#FFFFFF`, espaçamentos, paleta e composição da referência visual conservam precedência.

**Estado do link:** a obrigação documental do item não autoriza URL fictícia. Enquanto não existir destino público real, aprovado e testado, o Design pode representar um item **explicitamente inativo em protótipo**, identificado como demonstração, sem href enganoso, `#` ou promessa de navegação; a política de exibição do item em produção depende de FTR-02 e deliberação FTR-01. O requisito de existência na arquitetura não deve ser falsamente relatado como link operacional.

**Deliberação específica FTR-01/D1 — posicionamento (16/10/2026):** após a apresentação da proposta na PR #670 e seu merge documental, o fundador respondeu **"de acordo, segue"** à continuidade da formalização. A concordância é registrada **somente quanto à direção editorial proposta**: inserir o rótulo **`Mapa do Ecossistema` ao final de `Explore o ecossistema`**, depois dos oito destinos, preservando os agrupamentos e o conteúdo visual já validado. **Estado: FTR-01/D1 — POSITION_ACCEPTED (escopo delimitado).**

**Não coberto pela concordância:** não há aprovação de URL, clique funcional, simulação de link em produção, variante móvel/compacta, medidas pixel-perfect, revisão visual da imagem de 14/10, redesign das demais colunas ou declaração de prontidão do rodapé. `FTR-01` como gate integral **permanece PARTIAL / NOT_CLOSED**; `FTR-01/D2` (variantes e estados) e evidência visual de aplicação requerem tratamento próprio. `FTR-02` permanece bloqueado até existir destino validado. A decisão verbal nesta conversa é a fonte da concordância e **não se confunde com assinatura formal de outros responsáveis**.

### FTR-03 — matriz objetiva de evidência por Home

Para cada uma das **oito Homes** (Pessoa; Organizações e Coletivos; Mall; Travel; Business; Media; Intelligence; Ads), a revisão deverá conter uma linha de evidência verificável com:

1. referência ao Master, versão e data de exame;
2. URL do protótipo ou arquivo com captura real da área final da página, identificável por versão;
3. estado desktop e mobile, **sem confundir protótipo com produção**;
4. checklist da presença e literalidade de `Possibility, lived.`, `Conectamos pessoas a possibilidades que podem transformar suas vidas.`, `Descubra. Viva. Evolua.`, quatro agrupamentos editoriais, destinos e faixa jurídica;
5. colocação e estado funcional/indisponível de `Mapa do Ecossistema`, quando a proposta tiver sido aprovada;
6. contraste visual com a referência de 14/10/2026, respeitando `#FFFFFF`, tipografia, símbolos e hierarquia;
7. registro de divergências e decisões contextuais aprovadas, revisor de Brand/Design e desfecho datado;
8. identificação separada de variações posteriores **somente com evidência identificada**, incluindo eventual botão/QR de aplicativo: QR ilustrativo não é QR oficial, e não demonstra disponibilização nas lojas.

**Critério de conclusão:** `FTR-03` só pode ser declarado concluído com **8/8 evidências individuais verificadas** e análise das divergências; a auditoria documental 8/8 já realizada não substitui essas provas. A revisão responsiva funcional e de acessibilidade pertence também a FTR-05 e permanece pendente.

**Matriz atual de prova:** `8/8_MASTERS_DOCUMENTALLY_RECONCILED`; `0/8_HOME_RENDER_EVIDENCES_VERIFIED_IN_THIS_REVIEW` (a última contagem descreve **evidência efetivamente examinada nesta revisão**, não afirma ausência de protótipos externos); `FTR-01/D1 = POSITION_ACCEPTED`, `FTR-01 = PARTIAL_NOT_CLOSED`; `FTR-03 = NOT_ADJUDICATED`; `FTR-02 = URL_NOT_VERIFIED`. Este registro não autoriza implementação, publicação ou alteração normativa de marca.

## 6.3. FTR-01/D2 — contrato candidato de variantes responsivas (16/10/2026)

**Finalidade:** registrar uma opção de arquitetura semântica de variantes para avaliação de Design, Produto, Brand e Acessibilidade. **Não há mockup mobile/tablet homologado nem variante ratificada por esta seção.** A referência oficial de 14/10/2026 continua definindo a composição desktop, seu conteúdo, fundo `#FFFFFF`, paleta, Goldplay e assinaturas.

### Regras comuns invariantes

- **Identidade:** manter logotipo, `Possibility, lived.`, mensagem de posicionamento e assinatura final `Descubra. Viva. Evolua.` sem reescrever ou converter esta última em assinatura institucional.
- **Quatro grupos editoriais distintos:** `Explore o ecossistema`, `Guivos`, `Ajuda`, `Receba novidades`; preservar também identificação e links jurídicos da faixa inferior. Reorganizar espacialmente não significa excluir função.
- **Mapa:** no grupo `Explore o ecossistema`, depois dos oito destinos, conforme FTR-01/D1. Ausência de URL validada proíbe link de produção que simule navegação; FTR-02 continua independente.
- **Integridade funcional:** os mesmos destinos realmente disponíveis e informações públicas verificadas devem permanecer alcançáveis em qualquer viewport. Não criar URLs, canais, captação efetiva, consentimento presumido, botão funcional ou QR oficial por conveniência visual.
- **Adaptação por conteúdo:** pontos de quebra, largura, altura e disposição dependem de ensaio de texto real, zoom, fonte, tamanho de toque e dispositivos-alvo; nenhum breakpoint ou comprimento de card é token normativo nesta proposta.
- **Acesso essencial:** políticas legais, contato de suporte efetivamente disponível e identificação institucional não podem desaparecer em versões reduzidas nem depender exclusivamente de hover, gesto ou animação.
- **Acessibilidade:** ordem de leitura linear compreensível, títulos de agrupamento, foco visível, teclado, leitores de tela, alvos tocáveis e estados explícitos; ícones sociais/QR exigem rótulos acessíveis quando forem legitimamente habilitados.

### Matriz de variantes — hipótese de aplicação por contexto, não por pixel fixo

| Variante | Contexto preferencial | Organização candidata | O que nunca pode ser suprimido |
|---|---|---|---|
| `full` | Homes públicas e páginas informacionais extensas; tela larga | Reproduzir hierarquia aprovada: bloco de marca, navegação em três grupos, bloco de novidades, divisor e faixa inferior | Textos da referência, coluna de novidades, grupos, assinatura final, informação jurídica |
| `full` refluído | Homes e páginas públicas em largura intermediária/tablet | Reorganizar os mesmos blocos em linhas/colunas conforme espaço efetivo; `Receba novidades` pode ocupar linha própria | Todos os blocos e links verificados, sem colunas comprimidas ou campo ilegível |
| `full` empilhado | Home pública em viewport estreita/mobile | Empilhar marca e texto, grupos, novidades e faixa inferior com ordem semântica explícita; apresentação expansível de grupos só após prova de acessibilidade e descoberta | Nenhum grupo essencial apagado; link jurídico acessível; não esconder conteúdo aprovado sob ícones mudos |
| `compact` | Páginas internas públicas de fluxo prolongado, mediante justificativa contextual | Reduzir densidade visual e redistribuir blocos, sem alterar identidade e acesso a navegação/ajuda/direitos; tratamento de novidades precisa de decisão específica | Identidade, navegação essencial, suporte e direitos; não fingir aprovação de exclusão do bloco `Receba novidades` |
| `minimal` | Fluxos sensíveis/autenticados, estados de erro ou indisponibilidade, somente se autorizados em contexto próprio | Mínimo de identificação, ajuda real e informações legais, sem expor estado privado; aplicação excepcional, não padrão das oito Homes | Acesso legal e suporte pertinente; não reaproveitar indiscriminadamente o `full` como superfície de coleta |

**Limite importante:** `compact` e `minimal` são **variantes hipotéticas**, não exceções já autorizadas ao conteúdo visual aprovado. Especialmente `Receba novidades`: nenhuma omissão, recolhimento ou deslocamento que altere seu papel editorial será considerado aprovado antes de decisão humana explícita. Para as **oito Homes públicas**, a base candidata é `full` responsivo (refluído ou empilhado segundo o espaço), não `minimal`.

### Estados e comportamentos que exigem decisão/execução futura

| Objeto | Estado seguro enquanto não houver comprovação | Gate decisivo |
|---|---|---|
| `Mapa do Ecossistema` | Rótulo de protótipo demonstrativo, não link operacional; exibição na produção depende de política aprovada e destino | FTR-01 + FTR-02 |
| Destinos institucionais e sociais | Só habilitar URL oficial verificada; não simular destino indisponível | FTR-02 + FTR-04 |
| `Receba novidades` | Bloco visual preservado; formulário não pode prometer cadastro sem finalidade, consentimento/aviso e integração real | FTR-04 + FTR-06/07 |
| `Obter o app` / QR | Tratar eventual iteração posterior como referência visual separada; não gerar QR fictício nem alegar distribuição | Nova evidência Brand/Design + FTR-02/03 |
| Ícones e controles de expandir | Estado, foco, semântica, leitores de tela e testes reais antes de publicar | FTR-05 + FTR-07 |
| Implantação comum | Nenhuma rota, responsividade, cobertura das oito Homes ou deploy demonstrado por este texto | FTR-06..08 |

### Deliberação FTR-01/D2 e critério de aceite

**Proposta para ratificação:** (1) oito Homes públicas seguem um rodapé `full` com reflow conforme conteúdo e viewport; (2) `compact` só em página interna pública com motivo e conteúdo essencial preservado; (3) `minimal` apenas em fluxos restritos com contrato próprio; (4) não fixar breakpoints sem testes; (5) nenhuma função aprovada pode ser retirada por adaptação responsiva; (6) estados indisponíveis nunca serão apresentados como ações concluídas.

**Evidência necessária para ratificar:** concordância específica sobre as variantes e seu escopo, revisão de hierarquia por Brand/Design, e registro de quaisquer exceções aprovadas. A homologação de viewport, acessibilidade e interação depende de FTR-05/07 e não deve ser confundida com decisão de arquitetura.

**Deliberação delimitada do fundador em 16/10/2026 — FTR-01/D2:** após receber a proposta completa da PR #672, o fundador respondeu **"de acordo, segue"** ao encaminhamento da decisão. Registra-se a aceitação **apenas da regra de arquitetura de variantes**: (i) `full` responsivo como padrão nas oito Homes públicas, inclusive com reflow/empilhamento conforme viewport; (ii) `compact` elegível somente para páginas internas públicas, mediante justificativa por contexto e preservação de identidade, navegação, suporte e direitos; (iii) `minimal` elegível excepcionalmente em fluxos sensíveis, autenticados ou de indisponibilidade, dependente de contrato contextual e da preservação de informação essencial; (iv) breakpoints e métricas não fixados sem testes; (v) nenhum conteúdo ou função validado pode ser excluído automaticamente por responsividade; (vi) indisponibilidade de um destino não pode ser disfarçada de funcionalidade existente.

**Limite da decisão:** o aceite do **padrão e dos critérios de elegibilidade** não concede autorização automática para aplicar `compact` ou `minimal` em uma rota específica, retirar `Receba novidades`, alterar a referência visual institucional, homologar uma versão mobile/tablet ou declarar conformidade de acessibilidade. Exceções por superfície, inclusive qualquer alteração de bloco aprovado, permanecem sujeitas a decisão contextual rastreável. `FTR-02` conserva a dependência de destino real do `Mapa do Ecossistema`.

**Estado resultante:** `FTR-01/D1 = POSITION_ACCEPTED`; `FTR-01/D2 = ARCHITECTURE_VARIANTS_ACCEPTED_SCOPED`; `FTR-01 = PARTIAL_NOT_CLOSED` (revisão de hierarquia e exceções visuais ainda necessárias); `FTR-03 = NOT_ADJUDICATED`; `FTR-05 = NOT_TESTED`; `FTR-06..08 = NOT_EVIDENCED`. A fonte de concordância é o assentimento nesta conversa, sem atribuir aprovações a Brand, Legal, Design ou equipes que não participaram. Nenhuma interface foi implementada por esta deliberação.

## 6.4. FTR-03 — auditoria exploratória do aplicativo Replit (16/10/2026)

**Fonte e método:** resposta do agente de inspeção **somente leitura** do aplicativo conectado [Guivos — Descoberta de Oportunidades](https://replit.com/@guivos/Guivos-Descoberta-de-Oportunidades), emitida em 16/10/2026. O agente declarou inspeção do roteamento e do componente de rodapé, além de capturas no **preview interno**; relatou repositório do aplicativo sem modificações. **As capturas não foram anexadas ao GKR nesta revisão.** Portanto o presente registro é um *relatório secundário de inspeção*, a ser confrontado com evidência visual primária versionada antes de adjudicar FTR-03. Não equivale a validação independente pelo GKR nem a auditoria de publicação.

### Cobertura das Homes segundo o relato de inspeção

| Home | Rota própria identificada no app | Rodapé / evidência descrita pelo agente | Estado para FTR-03 |
|---|---|---|---|
| Pessoa | `/pessoa` (a rota `/` corresponde a entrada de jornada, não à Home) | Rodapé exploratório compartilhado; agente relata capturas desktop/mobile no preview | **DIVERGÊNCIA REPORTADA**; prova primária não anexada, sem aprovação |
| Organizações e Coletivos | `/organizacoes-coletivos` | Rodapé exploratório compartilhado **mais** rodapé local, segundo inspeção; captura desktop; mobile só início da Home | **DIVERGÊNCIA REPORTADA**; mobile do rodapé não verificado |
| Mall | Nenhuma rota de Home identificada | Fallback recebe rodapé compartilhado, mas não constitui Home Mall | **NÃO AVALIÁVEL VISUALMENTE** |
| Travel | Nenhuma rota de Home identificada | Fallback não constitui Home Travel | **NÃO AVALIÁVEL VISUALMENTE** |
| Business | Nenhuma Home própria identificada | `/planos` e `/planos/fluxos` são superfícies de planos, não Home Business | **NÃO AVALIÁVEL VISUALMENTE** |
| Media | Nenhuma rota de Home identificada | Fallback não constitui Home Media | **NÃO AVALIÁVEL VISUALMENTE** |
| Intelligence | Nenhuma rota de Home identificada | Fallback não constitui Home Intelligence | **NÃO AVALIÁVEL VISUALMENTE** |
| Ads | Nenhuma rota de Home identificada | Fallback não constitui Home Ads | **NÃO AVALIÁVEL VISUALMENTE** |

**Denominador:** `2/8` Homes com rota própria identificada **neste aplicativo**; `6/8` sem rota de Home própria identificada no escopo inspecionado; **`0/8` homologadas em FTR-03**. Não inferir que as seis Homes inexistam em outras bases, apps, documentos ou protótipos. A prova visual mobile da Home O/C continua pendente.

### Divergências e limites relatados

O agente reportou que o componente global `FlowFooter` mostra conteúdo de **proposta exploratória e créditos/licença de imagens**, em vez do conteúdo da referência visual `GKR-UX-GLOBAL-FOOTER-001 v1.0.0`. Relatou não encontrar no rodapé atual:
- `Possibility, lived.`, a mensagem `Conectamos pessoas a possibilidades que podem transformar suas vidas.` ou `Descubra. Viva. Evolua.`;
- os quatro agrupamentos `Explore o ecossistema`, `Guivos`, `Ajuda`, `Receba novidades`;
- `Mapa do Ecossistema` ao final de `Explore o ecossistema` (há um item `Mapa` no cabeçalho, que não equivale ao requisito);
- links jurídicos, campo de novidades e controle de envio, botões/QR de aplicativo.

O fundo branco foi reportado como observado nas capturas disponíveis, **sem homologação cromática ou de tipografia**. O agente relatou também que o domínio público testado nas rotas `/pessoa` e `/organizacoes-coletivos` exibiu uma tela genérica de rota indisponível, em contraste com o preview interno; **causa não determinada**, não presumir deploy funcional. Um workflow do aplicativo constava como falho por conflito de porta no momento da inspeção; esse achado não altera os checks de CI do GKR.

### Encaminhamento que exige evidência primária

1. **Pessoa e O/C:** obter capturas identificadas/versionadas do rodapé desktop e mobile e confrontá-las com a composição de 14/10; separar o rodapé global do duplicado local de O/C antes de alegar paridade visual.
2. **Demais seis Homes:** localizar uma implementação/protótipo específico de cada Home antes de abrir checklist visual; fallback não conta como Home.
3. **Publicação:** examinar distintamente preview interno e rota pública; ausência de destino público validado bloqueia alegação de disponibilidade.
4. **Registro FTR-03:** somente uma matriz de oito evidências primárias com revisão contextual Brand/Design e resultados documentados poderá encerrar o gate. **Nenhum teste FTR-05/FTR-07 nem alteração de aplicativo foi realizado por esta auditoria.**

**Estado:** `FTR-03 = OPEN_WITH_REPORTED_NONCONFORMITIES`; `HOME_ROUTES_IDENTIFIED_IN_REPLIT = 2/8`; `HOME_RENDER_EVIDENCE_PRIMARY_ATTACHED_TO_GKR = 0/8`; `FTR-03_ADJUDICATED = 0/8`; `FTR-05 = NOT_TESTED`. O caráter candidato e não normativo deste documento é preservado; nenhuma autorização de implantação é inferida.

## 7. Fronteiras com trabalhos em andamento

- **Gráfico Vivo:** permanece parte da experiência e narrativa específica, não métrica de rodapé nem painel de contadores.
- **Selos:** não usar selo de reconhecimento como rodapé institucional ou sinal de certificação.
- **Pontos:** não incluir saldo, valor, câmbio ou resgate no rodapé público.
- **Replit:** executar implantação apenas após compatibilização de rotas reais e decisão de Design, sem interromper atualização atual de Organizações e Coletivos.
- **MENU do GKR:** eventual entrada de descoberta documental para esta superfície precisa de aprovação e publicação separadas; o item `Mapa do Ecossistema` é um **link do produto**, não um item do MENU do repositório.

## 8. Decisões de arquitetura pendentes

- Nomes finais e ordem dos grupos, variante compacta e peso editorial da assinatura da marca.
- Página de destino de `Mapa do Ecossistema` e seus critérios de publicação.
- Canais de ajuda e contato efetivamente mantidos.
- Conteúdos legais, informação institucional obrigatória e mercados/idiomas ativos.

Estas decisões devem ser resolvidas com responsáveis pertinentes e evidências, sem preencher lacunas com textos ou URLs fictícios.


## 6.5. FTR-01 — matriz de decisões de hierarquia pendentes (16/10/2026)

**Natureza:** reconciliação de decisões ainda abertas após FTR-01/D1 (posição do Mapa) e FTR-01/D2 (regra de variantes). O aceite desses dois recortes **não encerra o gate FTR-01** e não substitui autoridade visual `GKR-UX-GLOBAL-FOOTER-001 v1.0.0`. Esta matriz oferece opções verificáveis a Design/Brand/Produto sem adjudicar a decisão por inferência.

| Decisão específica | Base já aceita | Questão ainda aberta | Critério para encerramento |
|---|---|---|---|
| **FTR-01/D3 — Hierarquia editorial transversal** | Quatro blocos da referência: marca; `Explore o ecossistema`, `Guivos`, `Ajuda`; `Receba novidades` e faixa jurídica; `#FFFFFF`, Goldplay e tokens oficiais | Como acomodar o item adicional Mapa após os oito destinos sem desfigurar respiro, alinhamento, diferenciação visual e prioridade do bloco de novidades? | Comparativo visual identificado com a referência; deliberação Brand/Design/Produto sobre a variação, sem alterar cópia aprovada por silêncio |
| **FTR-01/D4 — Indisponibilidade editorial do Mapa** | D1 fixa a posição final de `Explore o ecossistema`; FTR-02 não dispõe de URL oficial verificada | Definir se e como exibir o rótulo informativo enquanto o destino está ausente, distinguindo protótipo de produção | Decisão contextual de navegação e contrato de estado; nunca usar href `#`, link quebrado nem indicar serviço em operação |
| **FTR-01/D5 — Exceções por superfície** | D2 admite `full` nas oito Homes, `compact` somente em páginas internas públicas justificadas e `minimal` em fluxos sensíveis contratados | Há alguma rota real que justifique exceção? Qual a diferença admitida, sobretudo para `Receba novidades`? | Lista de rotas reais, justificativa, itens preservados/alterados e autorização expressa por contexto; até lá, **nenhuma exceção aprovada** |
| **FTR-01/D6 — Elementos de iteração visual posterior** | Referência normativa de 14/10 inclui assinatura, conteúdos, formulário, sociais e área jurídica | A composição posterior de botão `Obter o app`/QR dispõe de imagem aprovada identificada e destino oficial? Deverá entrar na referência ou permanecer demonstração? | Fonte visual datada, análise de autoridade da variante, decisão editorial e evidência de URLs oficiais antes de eventual ativação; não alterar referência de 14/10 automaticamente |

**Fora do FTR-01:** executar reflow/zoom/acessibilidade (FTR-05), verificar URLs e titularidade (FTR-02), revisar legal/privacidade (FTR-04), implementar (FTR-06), testar (FTR-07) ou publicar (FTR-08). A inspeção secundária do Replit relatada em FTR-03 não autoriza alterar o aplicativo nesta fase.

**Estado após esta reconciliação:** `FTR-01/D1 = POSITION_ACCEPTED`; `FTR-01/D2 = ARCHITECTURE_VARIANTS_ACCEPTED_SCOPED`; `FTR-01/D3..D6 = DECISION_REQUIRED`; `FTR-01 = PARTIAL_NOT_CLOSED`. A documentação torna o restante decidível, mas **não anuncia decisões que ainda não ocorreram**.


## 6.6. FTR-01/D3 — proposta de hierarquia editorial e visual (16/10/2026)

**Estado:** `PROPOSAL_FOR_DECISION / NOT_ADJUDICATED`. Esta seção traduz a composição da referência oficial `GKR-UX-GLOBAL-FOOTER-001 v1.0.0` em critérios de revisão, sem alterar o documento normativo, autorizar redesign ou definir medidas arbitrárias.

### Ordem de leitura proposta

1. **Identidade Guivos:** marca e assinatura global `Possibility, lived.` com descrição institucional aprovada, preservando sua distinção da frase de jornada da faixa inferior.
2. **Descoberta e orientação:** três grupos editoriais na ordem `Explore o ecossistema`, `Guivos` e `Ajuda`. A leitura deve favorecer identificação dos rótulos e agrupamentos, não parecer um catálogo de produtos nem criar destaque artificial para um destino.
3. **Continuidade opcional:** `Receba novidades` como bloco próprio, com descrição, campo, envio e ícones sociais da referência; não apresentar formulário como funcional ou inscrição realizada sem integração e consentimento verificados.
4. **Responsabilidade e encerramento:** divisor e faixa inferior preservando identificação jurídica, links legais e assinatura `Descubra. Viva. Evolua.`, sem confundi-la com o slogan global.

### Tratamento do Mapa do Ecossistema

O rótulo `Mapa do Ecossistema` ocupa o **último lugar** de `Explore o ecossistema`, após os oito destinos, conforme FTR-01/D1. Sua presença acrescenta uma linha ao grupo, **não** uma coluna nova, nem uma categoria de conteúdo ou destaque em nível superior. O visual deverá demonstrar que a adição conserva legibilidade, ritmo vertical e distância entre blocos e faixa inferior. A política de exibição funcional/inativa permanece em FTR-01/D4 e FTR-02; nenhuma URL é inferida.

### Regras de integridade para comparar composições

| Elemento | Preservar da referência aprovada | Prova necessária para aceitar a hierarquia |
|---|---|---|
| Base e tipografia | Fundo `#FFFFFF`, Goldplay, escala e paleta oficiais, sem inventar novos tokens | Captura comparativa da proposta com a referência e identificação de diferenças |
| Bloco de marca | Identidade, assinatura `Possibility, lived.` e texto institucional | Leitura e presença integral no desktop e no reflow responsivo |
| Navegação | Os três títulos, os oito destinos aprovados, itens institucionais e de ajuda; Mapa ao final por D1 | Sequência editorial legível, sem duplicações ou truncamentos inadvertidos |
| Novidades | Título, texto, formulário e ícones sociais; separador discreto quando houver espaço | Hierarquia própria, sem competir indevidamente com a marca ou sumir por quebra de layout |
| Faixa inferior | Identificação jurídica, políticas/termos e `Descubra. Viva. Evolua.` com símbolo e ênfase aprovados | Sequência clara e acesso preservado, inclusive após empilhamento |
| Relação com a arquitetura D2 | `full` responsivo nas oito Homes; `compact` e `minimal` só por exceção contextual autorizada | Não converter a largura estreita em justificativa automática para omitir blocos |

**Não fixar:** centímetros de respiro, altura, grid numérico, breakpoints, tamanho de botão, métrica de contraste ou hierarquia de tabulação sem arquivos de design e resultados de teste; FTR-05 e FTR-07 exigem sua própria evidência. A comparação deve identificar quais diferenças são apenas reflow e quais mudam decisões de conteúdo/brand.

### Proposta de deliberação FTR-01/D3

Aprovar **somente o princípio de hierarquia**: identidade Guivos → três grupos de navegação → bloco de novidades com tratamento distinto → faixa legal e assinatura de jornada; `Mapa do Ecossistema` como último item de `Explore`, sem peso visual superior; nenhuma supressão automática no mobile; tudo sobre fundo branco e dentro de cores/tipografia oficiais. **A aprovação desta direção não aprova uma imagem nova nem conclui FTR-01.**

**Pendências explícitas:** comparação visual por Brand/Design/Produto; decisão D4 para Mapa sem destino; D5 para exceções por rota; D6 para eventual acesso ao app/QR; evidências de FTR-03 e testes FTR-05..08. Até deliberação expressa: `FTR-01/D3 = PROPOSED_NOT_ACCEPTED`; `FTR-01 = PARTIAL_NOT_CLOSED`.
