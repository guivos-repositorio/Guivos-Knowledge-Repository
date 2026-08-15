---
id: ROADMAP-12.79.0
title: Roadmap Arquitetural — Consolidação Documental P0–P9
status: active
version: 12.79.0
owner: Guivos
last_updated: 2026-08-15
supersedes_partial:
  - ROADMAP-12.78.0
related:
  - GKR-STATE-001
  - GKR-P9-GLOBAL-CONSOLIDATION-001
  - GOG-001
  - GPA-004
  - GPA-004-FUNCTIONAL-PORTFOLIO-001
  - GKR-BUSINESS-CONTINUITY-001
  - UXA-101
  - GTM-007
  - GTM-008
  - GKR-HOME-P5
  - GKR-HOME-DECISION-NO-WIREFRAME-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V2-SNAPSHOT-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GKR-UX-HOME-ADS-GENINPUT-001
  - M7.88
---

# Roadmap Arquitetural — Consolidação Documental P0–P9

## 1. Autoridade

Este roadmap registra o estado global após a ressincronização documental de agosto de 2026, a convergência das seis Homes públicas atualmente entregáveis, a autorização procedimental de sua fase de Design, a ressincronização da autoridade do Guivos Business em `GPA-004` v1.6.0 e o início conceitual controlado da Home Pública do Business. O estado oficial permanece em `GKR-STATE-001`.

A decisão pós-P5 de 2026-08-12 que afastava wireframe da continuidade da Home de Organizações e Coletivos permanece preservada como histórico em `GKR-HOME-DECISION-NO-WIREFRAME-001`, mas foi posteriormente superada **somente quanto à autorização procedimental da fase de Design** por `GKR-UX-HOMES-DESIGN-HANDOFF-001`.

A ressincronização do Business é uma frente de autoridade de produto. Ela explicita o formato funcional já validado, corrige a leitura residual de “jornadas corporativas” e não reabre os snapshots de Design v1/v2, não inicia UXA-102 e não altera o marco M7.88.

A Home Business é uma frente separada de Experience Architecture. Seu **Checkpoint 2 está validado como base conceitual**, enquanto o **Checkpoint 3 permanece não convergido** e precisa de reformulação antes dos contratos de autoridade, conversão, Documento Mestre e Source Lock.

## 2. Estado vigente

| Elemento | Estado |
|---|---|
| Era | GE-2 — Knowledge |
| marco funcional | **M7.88** |
| última UXA | **UXA-101** |
| UXA-102/V5 | **não iniciada** |
| SVGs | **121** |
| associações | **121** |
| perfis | **34** |
| superfícies/estados/fronteiras | **57** |
| transições | **66** |
| Engenharia de Produto | pausada antes de W0-01 |
| programa P0–P9 | documentalmente consolidado após integração de P9 |
| Guivos Business — autoridade de produto | **GPA-004 v1.6.0; duas ofertas principais: Programas de Incentivo + Guivos Journey custeado pela Empresa; contrato parte da Empresa; Business distinto de Organização e independente de Ads** |
| Home Pública — Guivos Business | **iniciada conceitualmente; Checkpoint 2 validado como base; Checkpoint 3 não convergido; sem Documento Mestre/Source Lock** |
| Home Pública — Pessoa | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Organizações e Coletivos | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente; P1–P5 preservados como histórico |
| Home Pública — Guivos Mall | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Guivos Travel | Documento Mestre + reconciliação pós-Media + Source Lock; Design autorizado proceduralmente |
| Home Pública — Guivos Media | Documento Mestre + GPA-005 + Source Lock; Design autorizado proceduralmente |
| Home Pública — Guivos Ads | Documento Mestre + GPA-007 + Source Lock; Design autorizado proceduralmente |
| handoff comum das seis Homes | **GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.1.0 ativo** |
| pacote externo para Design | **GKR-UX-HOMES-DESIGN-DELIVERY-001 v2.0.0 — 19 fontes canônicas + 6 guias operacionais** |
| snapshot externo v2 | **`delivery/design-handoff-v2` @ `486f1c5e784be6cf3db9b2fbcbc47da39f9e9016`** |
| snapshot externo v1 | **preservado em `delivery/design-handoff-v1` @ `8e2a356ca84ba980e588258757800cde2a946f40`** |

## 3. Sequência funcional preservada

```text
UXA-097 — compreensão inicial → Tela Hoje
→ UXA-098 — publicação → descoberta → Mapa/Lista → Detalhe
→ UXA-099 — estados residuais Opportunity Boost
→ UXA-100 — Planos
→ UXA-101 — saída consciente → BND-001
→ UXA-102/V5 — PENDENTE, NÃO INICIADA
```

A convergência das Homes públicas, o handoff de Design, a ressincronização do Guivos Business e a construção conceitual da Home Business constituem frentes separadas da sequência UXA e **não criam nova UXA, não alteram M7.88 e não retomam Engenharia de Produto**.

## 4. Consolidação temática

| Pacote | Resultado documental |
|---|---|
| P0 | intake/evidência preservado |
| P1/P1.1 | semântica e nomenclaturas integradas |
| P2 | Neo4j como referência de grafo |
| P3 | naming/marca/ativos governados |
| P4 | metodologia e gates de validação integrados |
| P5 | arquitetura institucional/jurídica integrada |
| P6 | privacidade e verdade operacional governadas |
| P7 | internacionalização e gates territoriais integrados |
| P8 | sete Produtos Especializados rebaselineados |
| P9 | estado transversal, matriz e Public Canon reconciliados |

Na Experience Architecture pública, seis Homes atingiram convergência documental suficiente para handoff controlado à fase de Design:

1. Pessoa;
2. Organizações e Coletivos;
3. Guivos Mall;
4. Guivos Travel;
5. Guivos Media;
6. Guivos Ads.

A Home de Organizações e Coletivos preserva P1–P5 como histórico válido. `GKR-HOME-P5` registrou prontidão para decisão humana; a decisão pós-P5 inicialmente afastou wireframe; `GKR-UX-HOMES-DESIGN-HANDOFF-001`, posterior, passou a autorizar wireframe low-fi e demais explorações de Design. A superação é exclusivamente procedimental e não altera significado, narrativa ou produto.

A reconciliação pós-Media estabeleceu que Guivos Media pode abastecer editorialmente outras superfícies sem assumir autoridade sobre a finalidade, narrativa ou operação dessas superfícies.

A Home Guivos Ads possui arquitetura própria, B2B e comercial, com `GKR-UX-HOME-ADS-MASTER-001`, `GPA-007` v1.3.0 e `GKR-UX-HOME-ADS-GENINPUT-001`. Ads preserva a autoridade das superfícies anfitriãs, organiza soluções por objetivo comercial e conduz a qualificação inteligente sem transformar contexto pessoal protegido em matéria-prima publicitária.

O Guivos Business está ressincronizado em `GPA-004` v1.6.0. O estado canônico preserva:

```text
Organização ≠ Guivos Business
Empresa no contrato Business ≠ novo tipo estrutural de participante
Guivos Business ≠ Guivos Ads
custeio empresarial da Journey ≠ propriedade ou controle da Journey
Programa de Pontos ≠ identidade do Business ≠ medida de evolução
Intelligence apoiando Business ≠ Intelligence como módulo Business
```

A arquitetura comercial do Business parte da **Empresa**, enquanto `Organização` permanece o tipo estrutural de participante na ontologia global. A direção humana validada é “Como podemos ajudar os seres humanos a terem uma vida melhor?”: a empresa amplia condições e possibilidades; não define evolução individual nem adquire autoridade sobre a Journey da pessoa.

### 4.1 Formato vigente do Guivos Business

O produto possui **duas ofertas principais**:

```text
GUIVOS BUSINESS
├── PROGRAMAS DE INCENTIVO
└── GUIVOS JOURNEY CUSTEADO PELA EMPRESA
```

Pontos Guivos, Guivos Intelligence, integrações/eventos, transações/liquidação e governança/gestão empresarial são capacidades relacionadas. Elas apoiam as ofertas sem criar automaticamente novas famílias comerciais.

**Programas de Incentivo** utilizam um núcleo comum de programa, campanha, participante, evento, regra, resultado, orçamento/financiamento e Intelligence. O mesmo núcleo pode atender recortes de funcionários/pessoas vinculadas e clientes sem exigir dois motores de produto distintos.

A segunda oferta é o **Guivos Journey existente, custeado pela empresa**. A empresa viabiliza acesso; a pessoa preserva voluntariedade, escolha, privacidade, pertinência e autoridade sobre a própria Journey. Não são formatos vigentes Journey para Empresas, Journey Business, Journey Corporativo, Journey Patrocinado, jornadas corporativas criadas pela empresa, trilhas obrigatórias ou cursos corporativos bonificados dentro do Journey.

### 4.2 Planos e composição comercial

Os planos vigentes permanecem:

```text
Start
Growth
Scale
Enterprise
```

O plano não define qual oferta pode ser contratada. Sua função é governar profundidade de capacidade, Intelligence, integração, governança, escala e serviço.

A leitura funcional de referência permanece:

```text
START → operar
GROWTH → acompanhar e compreender
SCALE → interpretar e integrar
ENTERPRISE → governar em alta complexidade e escala
```

A arquitetura diferencia:

```text
OFERTA
≠ PLANO BUSINESS
≠ ESCALA / PARTICIPANTES / ACESSOS
≠ ORÇAMENTO PRÉ-PAGO DE INCENTIVO
≠ NÍVEL DE SERVIÇO
```

A composição econômica de referência pode combinar plano Business, escala, ofertas contratadas, orçamento pré-pago e serviços adicionais. Preços, limites e entitlements finais permanecem abertos.

A direção de serviço separa capacidade tecnológica/comercial de participação da Guivos na implantação/operação. `Self-service`, `Assisted` e `Managed` permanecem direções de trabalho, não ofertas finais congeladas.

### 4.3 Pontos, impacto e Intelligence

O Programa de Pontos permanece capacidade Business. A equivalência econômica entre pontos e reais já validada permanece preservada e **não é reaberta** nesta frente. Journey permanece voluntário e com seus planos normais; pontos Business não pagam plano Journey e podem ser usados somente em possibilidades pagas elegíveis de Mall, Travel e Journey sem comprar pertinência, recomendação ou prioridade.

A empresa carrega/financia o orçamento de pontos; a concessão à pessoa constitui consumo/alocação do orçamento empresarial, enquanto o uso posterior é evento distinto. A distribuição de onde os pontos foram **efetivamente utilizados** considera apenas usos realizados e fecha 100% entre Mall, Travel e Journey, excluindo não utilizados e expirados dessa métrica percentual.

Quando uma solução Business expressar recursos disponibilizados a uma ação de impacto, utiliza-se **VALOR DE IMPACTO LIBERADO**. O termo não equivale a impacto realizado, comprovado ou causado.

Guivos Intelligence apoia Business a partir de **dados e eventos gerados ou legitimamente conhecidos dentro do Ecossistema Guivos**. A empresa pode combinar externamente essas saídas com seus indicadores internos, inclusive por exportação estruturada/API quando contratualmente disponível. A Guivos não depende de importar bases internas da empresa para produzir o Intelligence Business e não utiliza comparação interna antes/depois como atalho para declarar causalidade.

Quando Journey é custeado pela empresa, Intelligence pode produzir leitura agregada e protegida de interesses, tendências, temas e movimentos autorizados. A empresa não recebe score individual de evolução, Journey individual ou explicação individual de pertinência.

### 4.4 Relações econômicas e fronteiras

Uma empresa pode contratar Business e Ads simultaneamente, mas como **relações comerciais independentes**. Business governa capacidades B2B próprias; Ads governa publicidade, patrocínio, impulsionamento e exposição comercial paga. Nenhuma contratação concede automaticamente autoridade, inventário, capacidades ou direitos do outro produto.

Business pode aumentar circulação econômica em Mall, Travel e possibilidades pagas apresentadas pelo Journey, mas cada produto preserva sua autoridade e sua receita própria. Esse efeito é upside do ecossistema; o Business deve ser economicamente sustentável por si.

### 4.5 Home Pública do Guivos Business — continuidade conceitual

A Home Business foi iniciada conceitualmente, mas ainda não alcançou convergência documental.

`GKR-BUSINESS-CONTINUITY-001` v1.1.0 registra como **base validada do Checkpoint 2**:

- tese: quando uma empresa amplia possibilidades para as pessoas, novas possibilidades também se abrem para a própria empresa;
- protagonista: a empresa é o protagonista comercial e as pessoas são o centro humano do valor criado;
- problema: criar relações mais relevantes, ampliar possibilidades e compreender movimentos sem reduzir pessoas a números, pontos ou mecanismos de controle;
- promessa: **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**;
- pergunta-mãe candidata: **O que sua empresa pode tornar possível para as pessoas?**

O **Checkpoint 3 não está convergido**. Antes de qualquer avanço, duas correções precisam ser incorporadas à arquitetura narrativa:

1. o movimento sobre o Guivos Journey precisa explicar de forma mais clara e impactante o valor de a empresa custear o acesso, sem reduzir a oferta à frase “ampliar o acesso das pessoas ao Guivos Journey”;
2. o movimento que explicava que a Guivos “não precisa substituir os sistemas da empresa” deve ser removido ou reformulado como proposta positiva de valor, pois essa justificativa defensiva não pertence à narrativa pública da Home.

Nenhum dos demais movimentos propostos no Checkpoint 3 deve ser tratado isoladamente como arquitetura aprovada até a nova validação integral da sequência revisada.

O pacote de entrega v2 é governado por `GKR-UX-HOMES-DESIGN-DELIVERY-001`: 19 fontes canônicas extraídas da `main` canônica `603aa7f37435ac376f7a202669ad4ac1d7d13a83`, separadas por Home, acrescidas de seis guias operacionais `LEIA-PRIMEIRO`, totalizando 25 arquivos no snapshot externo `486f1c5e784be6cf3db9b2fbcbc47da39f9e9016`.

A emissão v1 continua preservada no snapshot `8e2a356ca84ba980e588258757800cde2a946f40` e não foi reescrita pela v2.

## 5. Lacunas não fechadas por documentação

Continuam dependentes de evidência ou autorização própria:

- resultados reais de mercado e PMF;
- implementação tecnológica e grafo em produção;
- fatos registrários de marca/domínios;
- constituição jurídica de eventual veículo social;
- controles legais/privacidade em produção;
- piloto e operação internacional;
- cobrança/gateway real;
- handoffs especializados ainda não materializados;
- seleção e validação humana das direções visuais das seis Homes;
- promoção de qualquer output de Design a estado canônico;
- implementação operacional da experiência inteligente de qualificação do Guivos Ads;
- implementação operacional de campanhas, inventário, pricing e mensuração do Guivos Ads;
- preços, limites quantitativos e entitlements finais dos planos Business;
- preço/faixa de escala e preço de acessos Journey custeados pela empresa;
- definição final dos níveis Self-service / Assisted / Managed;
- regras econômicas/operacionais ainda abertas do Programa de Pontos Business que não tenham autoridade própria já aprovada;
- arquitetura técnica de analytics/Intelligence Business, exportação/API e seus contratos;
- thresholds mínimos de agregação/coorte do Intelligence Business;
- arquitetura narrativa convergida, Documento Mestre, conversão e Source Lock da Home Pública do Guivos Business;
- UXA-102/V5;
- Product Engineering.

A equivalência econômica de pontos já validada **não é classificada como lacuna por este roadmap**; esta versão apenas não redefine seu parâmetro numérico.

## 6. Próximos caminhos possíveis

Após P9, não existe “P10” automático.

O próximo ato deve nascer de uma necessidade concreta e autoridade própria. Exemplos:

- evidência de pesquisa → VAL;
- decisão de implantação → ADR/Engineering;
- fato jurídico/institucional → gates P5;
- controle operacional/privacy → gates P6;
- readiness/piloto territorial → gates P7;
- nova continuidade funcional → UXA-102 somente por autorização humana separada;
- implementação → Product Engineering somente por reativação explícita;
- seis Homes convergidas → exploração de Design controlada por Home e por Source Lock;
- Guivos Ads → validar direção de Design, operação comercial e experiência inteligente em atos próprios, sem inferir implementação automática;
- Guivos Business → continuar a arquitetura narrativa da Home Pública preservando o Checkpoint 2, reformulando os movimentos 6 e 9 do Checkpoint 3 e submetendo novamente a sequência completa à validação antes dos contratos de autoridade.

## 7. Handoff e entrega para Design

O estado governado é:

```text
GKR
→ fonte de verdade e arquitetura

GKR-UX-HOMES-DESIGN-HANDOFF-001
→ autorização procedimental + regras de Design para seis Homes

SOURCE LOCK DE CADA HOME
→ contexto permitido por execução

GKR-UX-HOMES-DESIGN-DELIVERY-001 v2.0.0
→ composição e integridade do pacote externo

GKR-UX-HOMES-DESIGN-DELIVERY-V2-SNAPSHOT-001
→ registro factual do snapshot emitido

branch delivery/design-handoff-v2
→ snapshot de distribuição vigente
→ não é fonte canônica paralela

branch delivery/design-handoff-v1
→ snapshot histórico preservado

OUTPUT DE DESIGN
→ EXPLORAÇÃO
→ requer validação humana antes de qualquer promoção
```

As branches de entrega não devem ser mescladas na `main` para duplicar documentos canônicos. Se qualquer fonte obrigatória evoluir materialmente, deve ser avaliada nova emissão do pacote em vez de substituição silenciosa de arquivos dentro de um snapshot já distribuído.

A Home do Guivos Business **não entra automaticamente no snapshot v2 existente**. Sua eventual convergência e inclusão em nova emissão de Design dependerão de arquitetura narrativa aprovada, Documento Mestre, contratos complementares, Source Lock, validação e autorização próprias.

## 8. Preservação

`ressincronização documental concluída ≠ produto implementado ≠ operação comprovada`.

`Design autorizado ≠ solução aprovada ≠ output canônico ≠ implementação ≠ publicação`.

Para Organizações e Coletivos:

`decisão histórica sem wireframe ≠ proibição procedimental vigente`, pois o handoff posterior de Design governa esse limite específico.

Para Guivos Ads:

`Home convergida ≠ campanha operacional ≠ inventário disponível ≠ pricing público ≠ Intelligence implementado ≠ contratação automática`.

Para Guivos Business:

`Organização ≠ Business ≠ Ads`.

`Empresa como início do contrato Business ≠ novo tipo estrutural de participante`.

`duas ofertas principais = Programas de Incentivo + Guivos Journey custeado pela Empresa`.

`oferta ≠ plano ≠ escala ≠ orçamento pré-pago ≠ nível de serviço`.

`custeio da Journey ≠ propriedade da Journey ≠ acesso ao contexto pessoal protegido`.

`pontos em possibilidade Journey elegível ≠ pagamento de plano Journey ≠ compra de pertinência`.

`Programa de Pontos reconhecido arquiteturalmente ≠ medida de evolução`.

`equivalência econômica preservada ≠ redefinição da equivalência nesta frente`.

`VALOR DE IMPACTO LIBERADO ≠ impacto realizado ≠ impacto comprovado`.

`Intelligence Business = dados/eventos gerados na Guivos ≠ ingestão obrigatória de KPIs internos da empresa`.

`Intelligence apoiando Business ≠ módulo Business ≠ acesso irrestrito a dados pessoais`.

`Checkpoint 2 da Home validado como base ≠ Checkpoint 3 convergido ≠ Documento Mestre ≠ Source Lock ≠ Design autorizado`.

`GPA-004 v1.6.0 ressincronizado ≠ Home Business convergida ≠ inclusão automática em pacote de Design`.
