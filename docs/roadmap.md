---
id: ROADMAP-12.83.0
title: Roadmap Arquitetural — Estado Governado pós-PR #300
status: active
version: 12.83.0
owner: Guivos
last_updated: 2026-08-21
supersedes_partial:
  - ROADMAP-12.82.0
related:
  - GKR-STATE-001
  - GKR-GLOBAL-INTEGRITY-POST300-001
  - GKR-P9-GLOBAL-CONSOLIDATION-001
  - GOG-001
  - GPA-004
  - GPA-004-FUNCTIONAL-PORTFOLIO-001
  - GKR-BUSINESS-CONTINUITY-001
  - GKR-UX-HOME-BUSINESS-NARRATIVE-001
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-BUSINESS-SOURCELOCK-001
  - GKR-UX-HOME-BUSINESS-GENINPUT-001
  - GKR-BUSINESS-HOME-CONTINUITY-005
  - GPA-006
  - GIA-000
  - GKR-INTELLIGENCE-CONTINUITY-001
  - GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001
  - GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
  - GKR-UX-HOME-INTELLIGENCE-HANDOFF-001
  - GKR-UX-HOME-INTELLIGENCE-GENINPUT-001
  - GKR-INTELLIGENCE-HOME-CONTINUITY-001
  - UXA-101
  - GTM-007
  - GTM-008
  - GKR-HOME-P5
  - GKR-HOME-DECISION-NO-WIREFRAME-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V2-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V3-SNAPSHOT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GKR-UX-HOME-ADS-GENINPUT-001
  - GKR-BRAND-SIGNATURE-001
  - GKR-BRAND-DIGITAL-ASSETS-INDEX-001
  - GKR-CHRISTIAN-FOUNDATION-001
  - M7.88
---

# Roadmap Arquitetural — Estado Governado pós-PR #300

## 1. Autoridade

Este roadmap traduz o estado corrente de `GKR-STATE-001 v2.42.0` em frentes governadas possíveis. Ele substitui a leitura operacional defasada de `ROADMAP-12.82.0` sem reabrir decisões integradas.

A reorganização desta edição preserva deliberadamente os detalhes válidos do roadmap anterior. Síntese e reordenação não funcionam como revogação de autoridade ou de gap já registrado.

```text
ROADMAP = POSSIBILIDADES GOVERNADAS DE AVANÇO
ROADMAP ≠ AUTORIZAÇÃO AUTOMÁTICA
SÍNTESE ≠ APAGAMENTO DE GAP
REORGANIZAÇÃO ≠ REVOGAÇÃO DE DECISÃO
```

A Reconciliação Global de Integridade pós-#300 corrige derivados e não cria nova UXA, novo marco funcional ou autorização de implementação.

## 2. Baseline vigente

| Elemento | Estado |
|---|---|
| Era | **GE-2 — Knowledge** |
| Estado global | **GKR-STATE-001 v2.42.0** |
| Marco funcional | **M7.88** |
| Última UXA | **UXA-101** |
| Próxima UXA | **UXA-102/V5 — não iniciada** |
| SVGs | **121 — 121 validados / 0 pendentes** |
| Associações | **121** |
| Perfis | **34** |
| Superfícies/estados/fronteiras | **57** |
| Transições | **66** |
| Engenharia de Produto | **pausada antes de W0-01** |
| Homes públicas | **8 convergidas documentalmente** |
| Design Delivery | **v4.0.0 — 39 arquivos externos** |
| Design produzido automaticamente | **não** |

## 3. Programa P0–P9

O programa P0–P9 está **documentalmente consolidado**.

Ele não deve ser reaberto genericamente. Novas evidências ou decisões devem entrar pelo domínio correspondente.

```text
P0–P9 CONSOLIDADO
≠ NEGÓCIO IMPLEMENTADO
≠ MERCADO VALIDADO
≠ TECNOLOGIA EM PRODUÇÃO
≠ OPERAÇÃO JURÍDICA/FISCAL CONCLUÍDA
```

## 4. Experience Architecture e Journey

Sequência funcional preservada:

```text
UXA-097
→ UXA-098
→ UXA-099
→ UXA-100
→ UXA-101
→ UXA-102/V5 — NOT_STARTED
```

D5-A, D5-B, D5-C1, D5-C2, D5-C3, D5-C4A e D5-C4B permanecem frentes não numeradas já integradas nos limites documentais próprios.

Próximas frentes possíveis, **somente mediante autorização separada**:

- UXA-102/V5 — erros, retornos e interrupções;
- materialização de `PER-009`, se houver necessidade funcional real;
- maturidade das transições internas de Planos ainda parciais;
- handoffs Journey → Mall;
- handoffs Journey → Travel;
- maturação de handoffs internos de Produtos Especializados;
- integrações patrocinadas ainda parciais conforme autoridade vigente;
- evolução de proveniência/explicabilidade de Intelligence nas superfícies;
- processo posterior a `BND-002`, somente quando houver autoridade contratual/assistida própria.

Nenhuma dessas frentes é iniciada por este roadmap.

## 5. Homes, Media, Ads e Design

Oito Homes estão documentalmente convergidas:

1. Pessoa;
2. Organizações e Coletivos;
3. Mall;
4. Travel;
5. Media;
6. Ads;
7. Business;
8. Intelligence.

A Home de Organizações e Coletivos preserva P1–P5 como histórico válido. `GKR-HOME-DECISION-NO-WIREFRAME-001` permanece histórico, mas sua proibição procedimental foi posteriormente superada **somente para a fase externa de Design** pelo handoff comum. Significado, narrativa e produto não foram reabertos.

A reconciliação pós-Media permanece válida: Guivos Media pode abastecer editorialmente outras superfícies sem assumir autoridade sobre finalidade, narrativa ou operação dessas superfícies.

A Home Ads preserva arquitetura própria, B2B e comercial. Ads mantém autoridade sobre publicidade, patrocínio, inventário permitido e mensuração, sem adquirir autoridade funcional sobre as superfícies anfitriãs e sem transformar contexto pessoal protegido em matéria-prima publicitária.

O handoff canônico v1.3.0 e o Design Delivery v4 permitem uma frente externa controlada, mas:

```text
HANDOFF ≠ DESIGN PRODUZIDO
SNAPSHOT ≠ OUTPUT APROVADO
OUTPUT EXTERNO ≠ CANON
CANON ≠ IMPLEMENTAÇÃO
```

Snapshot vigente:

```text
delivery/design-handoff-v4
commit = dfed980d8cfb39bbe4694e58d7c86ca0692266dc
tree   = 270e404cf0b5bf0d5d543bbbb0c5bd6a1f4602df
31 fontes canônicas + 8 guias = 39 arquivos
```

Snapshots históricos preservados:

- v3: `7b2b20c035551e3b1206af987aaddda710757166`;
- v2: `486f1c5e784be6cf3db9b2fbcbc47da39f9e9016`;
- v1: `8e2a356ca84ba980e588258757800cde2a946f40`.

As branches de entrega são snapshots reproduzíveis e **não devem ser mescladas na `main` para duplicar fontes canônicas**. Evolução material de fonte obrigatória deve gerar avaliação de nova emissão, não substituição silenciosa de snapshot distribuído.

Próximos atos visuais dependem de autorização humana específica e seleção de direção material.

## 6. Guivos Business

Estado preservado:

```text
GPA-004 = v1.6.0
OFERTAS PRINCIPAIS
├── Programas de Incentivo
└── Guivos Journey custeado pela Empresa
```

Direção humana preservada:

> **Como podemos ajudar os seres humanos a terem uma vida melhor?**

A empresa amplia condições e possibilidades; não define evolução individual nem adquire autoridade sobre a Journey da pessoa.

Leitura funcional dos planos:

```text
START      → operar
GROWTH     → acompanhar e compreender
SCALE      → interpretar e integrar
ENTERPRISE → governar em alta complexidade e escala
```

A arquitetura diferencia:

```text
OFERTA
≠ PLANO BUSINESS
≠ ESCALA / PARTICIPANTES / ACESSOS
≠ ORÇAMENTO PRÉ-PAGO DE INCENTIVO
≠ MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
```

Contratação e operação permanecem separadas:

```text
CONTRATAÇÃO
→ ONLINE

MODELO DE IMPLEMENTAÇÃO / OPERAÇÃO
→ SELF-SERVICE
→ COM APOIO DO SUPORTE
→ GERENCIADO
```

`Self-service / Com apoio do suporte / Gerenciado ≠ Start / Growth / Scale / Enterprise`.

A segunda oferta continua sendo o **Guivos Journey existente, custeado pela empresa**. Não são formatos vigentes Journey para Empresas, Journey Business, Journey Corporativo, Journey Patrocinado, jornadas criadas/controladas pela empresa, trilhas obrigatórias ou cursos corporativos bonificados dentro do Journey.

### 6.1 Pontos e impacto

O Programa de Pontos permanece capacidade Business. A equivalência econômica previamente validada **permanece preservada e não constitui gap deste roadmap**; esta edição não redefine seu parâmetro numérico.

```text
pontos Business ≠ pagamento de plano Journey
pontos ≠ compra de pertinência
pontos ≠ recomendação
pontos ≠ prioridade
pontos ≠ evolução
```

A empresa carrega/financia orçamento. A concessão à pessoa é consumo/alocação do orçamento empresarial; o uso posterior pela pessoa é evento distinto. A distribuição de uso considera apenas usos efetivos e fecha 100% entre Mall, Travel e Journey, excluindo não utilizados/expirados.

`VALOR DE IMPACTO LIBERADO ≠ impacto realizado ≠ impacto comprovado`.

Na Home Pública do Guivos Business, Pontos foram deliberadamente retirados da narrativa. Isso não remove a capacidade funcional do produto.

### 6.2 Business × Ads × Intelligence

Uma empresa pode contratar Business e Ads simultaneamente, mas como relações comerciais independentes.

```text
Organização ≠ Business
Business ≠ Ads
Intelligence apoiando Business ≠ Intelligence como módulo Business
```

Intelligence Business utiliza dados/eventos legitimamente gerados ou conhecidos dentro da Guivos. A empresa pode combinar externamente essas saídas com KPIs internos. A Guivos não depende de importar bases corporativas completas e não usa comparações internas antes/depois como atalho para causalidade.

### 6.3 Home Business

Cadeia preservada:

```text
Narrative
→ Authority Contracts
→ Conversion v2
→ Documento Mestre
→ Source Lock
→ GENINPUT
→ Handoff comum v1.3.0
→ Design Delivery v4
```

Pergunta-mãe vigente:

> **O que sua empresa pode tornar possível para as pessoas?**

Promessa:

> **Mais possibilidades para as pessoas. Mais capacidade para sua empresa.**

A Home preserva Journey antes de Incentivos, autonomia da pessoa, Pontos fora da narrativa pública, Intelligence limitado ao ecossistema Guivos, comparação Start/Growth/Scale/Enterprise, configurador comercial e contratação online com os três modelos de implementação/operação.

Gaps reais que permanecem abertos quando não houver autoridade posterior:

- preços finais;
- limites e entitlements finais;
- SLA;
- preço/faixa de escala e preço de acessos Journey custeados pela empresa;
- detalhamento operacional final dos modelos Self-service / Com apoio / Gerenciado;
- regras econômicas/operacionais restantes de Pontos sem autoridade própria já aprovada;
- arquitetura técnica de analytics/Intelligence Business;
- exportação/API e contratos técnicos;
- evidência operacional/comercial real;
- direção visual validada e output canônico da Home Business, quando houver frente visual autorizada.

## 7. Guivos Intelligence

Estado preservado:

```text
GPA-006 = v2.0.0
GIA-000 = v1.5.0
Product Source Lock = integrado
Home = convergida documentalmente
```

Duas frentes superiores:

```text
Pessoa / Journey
Business / População
```

Guardrails preservados:

```text
INTELLIGENCE ≠ JOURNEY
INTELLIGENCE ≠ BUSINESS
COMPREENDER ≠ DECIDIR
CONHECER ≠ UTILIZAR ≠ COMPARTILHAR
PERSONALIZAR ≠ EXPOR
ENTITLEMENT ≠ AUTORIDADE
PAGAMENTO ≠ PERTINÊNCIA
INFERÊNCIA ≠ FATO
SINAL ≠ CERTEZA
TENDÊNCIA ≠ DESTINO
PERCEBER ANTES ≠ PREVER O FUTURO
TECNOLOGIA ≠ PRODUTO
```

`GIA-000 v1.5.0` preserva CIE, LPM, GPMA e família de Intelligence Engines como candidatos técnicos/arquiteturais. Não declara arquitetura física, modelo final de IA, MLOps, serving técnico, APIs, ontologia física ou grafo em produção.

Product Source Lock, Narrative, Documento Mestre, Home Source Lock, Handoff e GENINPUT permanecem autoridades distintas. A Home Intelligence está no snapshot v4 sem tela, wireframe, UI, protótipo ou Design produzido.

Gaps reais:

- thresholds mínimos de agregação/coorte e técnicas de proteção;
- modelo físico de dados;
- ontologia lógica completa e ontologia física;
- contrato operacional de inferência, explicabilidade e aprendizado;
- governança operacional de benchmarks e evidência causal;
- estratégia de inferência e benchmark empírico;
- stack final de IA;
- MLOps/serving técnico;
- APIs;
- integração Power BI/consumidores analíticos em produção;
- pricing/packaging final;
- eventual oferta B2B autônoma do Intelligence;
- evidência operacional de qualidade e valor;
- output visual validado/canônico da Home Intelligence, quando houver frente visual autorizada.

`Neo4j = reference_selected`, não implementação comprovada.

## 8. Marca e proteção marcária

Autoridade verbal:

```text
Possibility, lived.      = canonical
Possibilidade, vivida.   = canonical
#PossibilityLived        = canonical
Do possível ao vivido.   = bordão canônico / não segunda assinatura
```

Portfólio GUIVOS existente nas classes 09, 35, 39 e 42 permanece reconciliado.

As assinaturas permanecem:

```text
CLEAR
35 = FILE
42 = FILE
```

O próximo gate de execução é **Human Filing Authorization**, não novo clearance.

Antes da execução:

- confirmar rota/taxa/desconto no INPI;
- confirmar titular/cadastro;
- revalidar busca se houver intervalo material;
- confirmar disponibilidade das especificações no e-Marcas;
- incluir AIaaS somente se houver evidência de atividade efetiva/objeto compatível;
- obter autorização humana explícita de gasto e protocolo.

```text
FILE ≠ FILING_AUTHORIZED
CLEAR ≠ REGISTRO
```

## 9. Fundamento Cristão

`GKR-CHRISTIAN-FOUNDATION-001 v1.0.0` está ativo e integrado.

```text
Evolução com propósito = preservado
primary_use = internal_governance
classification = public
authority_profile = public_foundational
external_reuse_automatic = false
```

A próxima necessidade não é doutrinária. Melhorias futuras somente devem ocorrer se houver necessidade concreta de governança, interpretação ou navegação e exigem decisão explícita quando afetarem fundamento, passagens ou invariantes.

## 10. Mercado e evidência

Continuam dependentes de evidência real:

- aplicação e resultados da validação B2C;
- PMF;
- disposição a pagar;
- retenção/recorrência;
- uso real e resultados de ofertas;
- evidência de transformação/impacto sem confundir correlação com causalidade.

Nova evidência deve entrar pela família VAL correspondente.

## 11. Tecnologia e implementação

Product Engineering permanece pausada antes de W0-01.

Não estão automaticamente autorizados:

- stack final;
- provisionamento Neo4j;
- POC;
- APIs;
- GraphRAG;
- GDS;
- MLOps;
- pipelines;
- banco de produção;
- observabilidade;
- deploy;
- integração real com Power BI.

A reativação exige ato explícito de Product Engineering.

## 12. Institucional, jurídico, privacidade e internacionalização

Continuam abertos conforme autoridades próprias:

- escolha/constituição de eventual veículo social;
- atos societários/jurídicos ainda não comprovados;
- superfícies legais em produção;
- inventário real de cookies/SDKs/operadores/transferências;
- controles LGPD operacionais;
- piloto Lisboa;
- estrutura fiscal/pagamentos/equipe internacional;
- Porto ou novo país somente após gates próprios.

## 13. Lacunas transversais preservadas

Além dos gaps detalhados por domínio, continuam abertos quando dependerem de realidade ou autorização específica:

- seleção e validação humana de direções visuais das Homes;
- promoção de qualquer output de Design a estado canônico;
- implementação operacional da qualificação inteligente do Guivos Ads;
- campanhas reais, inventário, pricing e mensuração do Guivos Ads;
- cobrança real e gateway;
- handoffs especializados ainda não materializados;
- controles jurídicos/privacidade efetivamente publicados e operacionais;
- piloto e operação internacional;
- UXA-102/V5;
- Product Engineering.

A equivalência econômica de pontos previamente validada **não é classificada como lacuna** por este roadmap.

## 14. Prioridade de governança após a reconciliação

A ordem não é uma fila automática. Quando houver intenção concreta, rotear pelo tipo de necessidade:

| Necessidade real | Autoridade de entrada |
|---|---|
| evidência de mercado | VAL |
| mudança tecnológica | ADR / GEA / Product Engineering |
| marca/ativo/fato registral | Brand / Trademark Evidence |
| filing das assinaturas | Human Filing Authorization |
| ato institucional/jurídico | P5 / gates institucionais |
| privacidade/operação | P6 / LS / OT |
| expansão territorial | P7 / T / PT |
| experiência funcional | UXA autorizada |
| Design | handoff + decisão humana própria |
| implementação | Product Engineering explicitamente reativada |

## 15. Preservações finais

```text
Organização ≠ Guivos Business ≠ Guivos Ads
Empresa como início do contrato Business ≠ novo participante estrutural
oferta ≠ plano ≠ escala ≠ orçamento pré-pago ≠ modelo de implementação/operação
contratação online ≠ modelo de implementação/operação
Self-service / Com apoio / Gerenciado ≠ Start / Growth / Scale / Enterprise
custeio da Journey ≠ propriedade da Journey ≠ acesso ao contexto pessoal protegido
pontos em possibilidade Journey elegível ≠ pagamento de plano Journey ≠ compra de pertinência
Programa de Pontos ≠ presença obrigatória na Home ≠ medida de evolução
equivalência econômica preservada ≠ redefinição nesta frente
VALOR DE IMPACTO LIBERADO ≠ impacto realizado ≠ impacto comprovado
Intelligence Business ≠ ingestão obrigatória de KPIs internos da empresa
Intelligence apoiando Business ≠ módulo Business ≠ acesso irrestrito a dados pessoais
Home Business convergida ≠ output visual aprovado ≠ implementação ≠ publicação
GPA-006 v2.0.0 convergido ≠ Intelligence implementado ≠ modelo de IA selecionado ≠ grafo em produção
Produto Especializado próprio ≠ assinatura própria obrigatória
Intelligence embutido ≠ Intelligence Direto
entitlement ≠ autoridade
maior plano ≠ menor privacidade
Graph / Knowledge / Analytics / AI = capacidades subordinadas ≠ identidade do produto
Neo4j = reference_selected ≠ POC ≠ provisioned ≠ production
GraphRAG = padrão candidato ≠ implementação
Power BI = consumidor possível ≠ fonte de verdade
Guivos.ai = possível superfície ≠ Guivos Intelligence
Product Source Lock + Home Source Lock + Documento Mestre + Handoff + GENINPUT + snapshot v4 ≠ Design produzido ≠ implementação
PERCEBER ANTES ≠ PREVER O FUTURO
```

## 16. Regra de encerramento

Após a reconciliação pós-#300:

```text
NÃO HÁ P10 AUTOMÁTICO
NÃO HÁ UXA-102 AUTOMÁTICA
NÃO HÁ DESIGN AUTOMÁTICO
NÃO HÁ FILING AUTOMÁTICO
NÃO HÁ ENGINEERING AUTOMÁTICA
```

O próximo movimento deve ser escolhido pela necessidade estratégica real, não pela simples existência de uma sequência documental.
