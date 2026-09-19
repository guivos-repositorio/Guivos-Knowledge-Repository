# LEIA PRIMEIRO — Guivos Mall — Emissão v5

## 1. Checkpoint congelado

- emissão: `GUIVOS-HOMES-DESIGN-HANDOFF-v5`
- origem canônica: `main @ aa1b524c20f6707d007208222ba8581af097c38d`
- Home: `Guivos Mall`
- diretório: `03-HOME-MALL`
- natureza deste guia: operacional / não normativo

Este guia não substitui, resume nem reescreve as autoridades listadas. Ele apenas congela o contexto desta emissão e organiza a execução externa.

## 2. Estado da execução

```text
V5 SNAPSHOT
→ EMITTED CONTEXT

DESIGN PRODUCTION RELEASE
→ NOT_GRANTED

FIGMA MAKE / DESIGN EXECUTION
→ NOT_RELEASED BY THIS SNAPSHOT ALONE

INITIAL OUTPUT STATE
→ EXPLORAÇÃO / NÃO CANÔNICA
```

## 3. Ordem obrigatória de leitura

1. `../00-COMUM/01-Handoff-Canonico-das-Homes.md` — GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.5.0
2. `../00-COMUM/02-GENINPUT-Source-Lock-e-Prompt.md` — GKR-UX-HOMES-GENINPUT-001 v2.0.0
3. `../00-COMUM/03-Design-Production-Readiness-e-Contrato-Figma.md` — GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.0.0
4. `../00-COMUM/04-Fluxo-Operacional-de-Entrega.md` — GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v2.0.0
5. `01-Documento-Mestre.md` — GKR-UX-HOME-MALL-MASTER-001 v1.0.0
6. `02-Reconciliacao-Media-Editorial.md` — GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0

Não adicione documentos específicos de outra Home à mesma execução sem decisão humana explícita.

## 4. Fontes congeladas e blobs

- `../00-COMUM/01-Handoff-Canonico-das-Homes.md` — `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.5.0` — blob `e16961cba058ac6fc941de9fcb89f0887f936fe1`
- `../00-COMUM/02-GENINPUT-Source-Lock-e-Prompt.md` — `GKR-UX-HOMES-GENINPUT-001 v2.0.0` — blob `4429547ecc77743167b64090f797da4a21d60c22`
- `../00-COMUM/03-Design-Production-Readiness-e-Contrato-Figma.md` — `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.0.0` — blob `2596440e57dee04e7262c8cdf802afe177c2943e`
- `../00-COMUM/04-Fluxo-Operacional-de-Entrega.md` — `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v2.0.0` — blob `d4b6189910db144981f0a770a70e9e273b67d969`
- `01-Documento-Mestre.md` — `GKR-UX-HOME-MALL-MASTER-001 v1.0.0` — blob `9b1f7e9fddd0c38215cc5e37ad0e385ea439f286`
- `02-Reconciliacao-Media-Editorial.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0` — blob `986cf6bb35cccd71f9ea681836a29e14281dae7c`

Qualquer divergência entre este guia e uma fonte listada deve ser resolvida em favor da fonte. Pare a execução e registre a divergência; não improvise uma solução semântica.

## 5. Matriz operacional desta Home

- `CANONICAL` — pergunta-mãe “O que pode fazer parte do seu próximo momento?”; Shopping e Gift Cards como portas distintas; descoberta + comércio + confiança; Hero permanente não dominado por promoção; MALL-HS-01..06; oferta, recomendação, destaque e patrocínio distintos.
- `DESIGN_CREATIVE` — composição comercial, direção de arte, visual de produtos, ritmo, navegação e componentes.
- `CONTENT_CANDIDATE` — copy de apoio e labels comerciais não congelados.
- `DESIGN_HYPOTHESIS` — alternativas de descoberta, ofertas, Shopping/Gift Cards, densidade de catálogo e apresentação comercial sem alterar elegibilidade, confiança, preço, estoque ou natureza de recomendação/patrocínio.
- `PROTOTYPE_PLACEHOLDER` — produtos, preços, marcas, campanhas e conteúdos para teste.
- `REAL_DATA_REQUIRED` — preço, pontos, estoque, elegibilidade, desconto, marca/parceiro, avaliação, disponibilidade e campanha reais.
- `OPEN_QUESTION` — catálogo vivo, campanhas e condições comerciais futuras.
- `PROHIBITED_INFERENCE` — inventar estoque/preço, converter marca em parceria, simular recomendação personalizada, fundir pontos com Gift Card ou mascarar mídia paga.

Regras:
- nenhuma classe pode ser promovida a `CANONICAL` por inferência;
- `DESIGN_HYPOTHESIS` é reversível e testável;
- `PROTOTYPE_PLACEHOLDER` nunca pode parecer verdade pública;
- `REAL_DATA_REQUIRED` exige fonte real antes de apresentação factual;
- `OPEN_QUESTION` não é autorização para inventar;
- `PROHIBITED_INFERENCE` deve ser tratado como limite explícito.

## 6. Prompt inicial para Figma Make / IA de Design

Você está trabalhando **exclusivamente na Home Guivos Mall da Guivos**, usando o snapshot v5 congelado acima.

Leia primeiro as quatro autoridades comuns e depois todas as fontes específicas desta Home.

Sua função é **explorar soluções de Design originais**, não decidir arquitetura, produto, fatos ou estratégia da Guivos.

Preserve integralmente tudo classificado como `CANONICAL`.

Você possui ampla liberdade criativa em `DESIGN_CREATIVE`: identidade visual, tipografia, paleta, imagens, composição, grid, iconografia, motion, aparência dos componentes e demais decisões estéticas não congeladas podem ser propostas com originalidade.

Quando testar uma solução ainda não aprovada, marque-a mentalmente e na explicação como `DESIGN_HYPOTHESIS`. Ela deve ser reversível e não pode alterar significado, autoridade, regras, dados ou fronteiras do produto.

Trate `CONTENT_CANDIDATE` como proposta sujeita a aprovação humana. Não transforme copy candidata em texto canônico.

Use `PROTOTYPE_PLACEHOLDER` somente quando necessário para testar estrutura, volume, hierarquia ou comportamento, deixando claro que é provisório.

Nunca invente `REAL_DATA_REQUIRED`: preços, disponibilidade, parceiros, métricas, cases, pessoas, depoimentos, resultados, performance ou qualquer outro fato devem permanecer ausentes, claramente ilustrativos ou identificados como dependentes de fonte real.

Registre `OPEN_QUESTION` em vez de resolvê-la silenciosamente.

Nunca viole `PROHIBITED_INFERENCE`.

Entregue uma exploração visual coerente, sofisticada, original e responsiva, sem se sentir obrigado a copiar layouts, estilos ou identidades preexistentes. O objetivo é expressar o propósito desta Home com criatividade, preservando os contratos do GKR.

Todo resultado desta etapa começa como:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

## 7. Autoauditoria obrigatória antes de apresentar a exploração

Confirme:
- [ ] trabalhei somente com esta Home + quatro fontes comuns;
- [ ] preservei todos os itens `CANONICAL`;
- [ ] usei liberdade estética sem criar nova regra de produto;
- [ ] identifiquei minhas hipóteses de Design;
- [ ] não inventei fatos, preços, disponibilidade, parceiros, métricas ou provas;
- [ ] placeholders não parecem dados reais;
- [ ] questões abertas foram sinalizadas;
- [ ] nenhuma inferência proibida entrou na solução;
- [ ] a solução contempla desktop e mobile/responsividade;
- [ ] o resultado permanece explicitamente não canônico até aprovação humana.

## 8. Próximo gate

Este snapshot **não autoriza execução por si só**. A execução externa somente começa após ato humano separado de `DESIGN PRODUCTION RELEASE = GRANTED`.
