---
id: GKR-HOMES-DESIGN-INPUT-V6-GUIDES-001
title: Homes Públicas — Especificação dos Guias LEIA-PRIMEIRO v6
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: false
maturity: guide_blueprints_complete_pre_snapshot
depends_on:
  - GKR-HOMES-DESIGN-INPUT-HARDENING-V6-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
related:
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
---

# Homes Públicas — Especificação dos Guias LEIA-PRIMEIRO v6

## 1. Finalidade

Esta especificação define o conteúdo obrigatório dos oito `LEIA-PRIMEIRO` do pacote externo v6.

Os guias são **human-first**:

```text
DESIGNER HUMANA
→ CONSUMIDORA PRIMÁRIA

AI
→ CONSUMIDOR OPCIONAL
→ MESMA VERDADE
→ APÊNDICE SECUNDÁRIO
```

Os guias não desenham páginas, não escolhem identidade visual e não adicionam significado novo.

## 2. Regra de materialização pós-merge

Antes do merge, esta especificação pode fechar conteúdo, ordem e classes.

Somente após o merge e autorização humana separada para emissão v6 podem ser preenchidos:

- SHA canônico de origem;
- SHA/blob de cada fonte;
- commit/tree do snapshot;
- timestamp da emissão;
- prova de 26/26 byte preservation.

```text
CONTEÚDO DO GUIA
→ PREPARÁVEL ANTES DO MERGE

CHECKPOINT / SHAs
→ SOMENTE PÓS-MERGE

NÃO INVENTAR CHECKPOINT FUTURO
```

## 3. Estrutura obrigatória de cada guia

Cada `LEIA-PRIMEIRO` deve conter, nesta ordem:

1. Home e finalidade;
2. status do pacote;
3. ordem curta de leitura;
4. Master vigente;
5. fontes específicas;
6. resumo `CANONICAL`;
7. `DESIGN_CREATIVE`;
8. `CONTENT_CANDIDATE`;
9. `DESIGN_HYPOTHESIS`;
10. `PROTOTYPE_PLACEHOLDER`;
11. `REAL_DATA_REQUIRED`;
12. `OPEN_QUESTION`;
13. `PROHIBITED_INFERENCE`;
14. acessibilidade/responsividade;
15. critérios de autoauditoria humana;
16. checkpoint + SHAs da emissão;
17. apêndice opcional de IA.

O guia deve começar explicitamente por:

> **Leia o Documento Mestre antes de desenhar. Use as fontes complementares para aprofundar limites e dúvidas; não reconstrua a Home a partir do histórico.**

## 4. Autoridades comuns v6

Todos os guias devem apontar para:

1. `GKR-UX-HOMES-DESIGN-HANDOFF-001 v1.6.0`;
2. `GKR-UX-HOMES-GENINPUT-001 v2.1.0` — somente necessário para IA opcional;
3. `GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001 v1.1.0`;
4. `GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001 v3.0.0`.

## 5. Guia 01 — Home Pessoa

### Ordem curta

1. `GKR-UX-HOME-MASTER-001 v1.1.0`;
2. `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001 v1.0.0`;
3. autoridades comuns.

### CANONICAL

- Home pública institucional, predominantemente orientada à Pessoa;
- pergunta-mãe: **“O que se torna possível quando você entra aqui?”**;
- possibilidade antes de produto;
- Hero = descoberta;
- Journey possui porta própria;
- participante ≠ produto;
- 11 movimentos são funções de significado, não 11 seções;
- 7 macroexperiências não são 7 seções obrigatórias;
- autonomia, prova e confiança são transversais;
- sem falsa personalização;
- Intelligence não decide pela Pessoa.

### DESIGN_CREATIVE

Identidade visual, tipografia, cor, imagem, ilustração, iconografia, composição, grid, ritmo, motion, componentes, agrupamento físico, densidade, progressive disclosure, responsividade e copy não congelada.

### CONTENT_CANDIDATE

Terceira camada da Hero, CTA exploratório, labels e microcopy não congelados.

### DESIGN_HYPOTHESIS

Alternativas de Hero, agrupamento dos movimentos, launcher, densidade, mídia, prova, progressão e relação narrativa/módulos.

### PROTOTYPE_PLACEHOLDER

Histórias, imagens, conteúdo editorial e evidências ainda não selecionadas, sempre reconhecíveis como provisórias.

### REAL_DATA_REQUIRED

Pessoa, Organização, Coletivo, parceiro, métrica, case, depoimento, país, resultado, disponibilidade ou prova apresentados como reais.

### OPEN_QUESTION

Copy pública final, rodapé integral, disponibilidade operacional e decisões específicas de lançamento.

### PROHIBITED_INFERENCE

Momento pessoal presumido, diagnóstico, falsa personalização, escala inventada, causalidade exagerada, `Organização = Business`, produto antes da tese, Intelligence decidindo pela Pessoa.

## 6. Guia 02 — Organizações e Coletivos

### Ordem curta

1. `GKR-UX-HOME-OC-MASTER-001 v1.1.0`;
2. `GKR-UX-HOME-OC-MEDIA-SUPPLY-001 v1.0.0`;
3. autoridades comuns.

### CANONICAL

- pergunta-mãe: **“O que podemos tornar possível juntos?”**;
- Organização e Coletivo são participantes distintos;
- narrativa compartilhada antes da bifurcação;
- 11 movimentos / 7 macroexperiências são significado, não layout;
- bilateralidade, autoridade, proteção e evidência;
- participantes respondem “quem”; capacidades/produtos respondem “como”.

### DESIGN_CREATIVE

Expressão visual, mídia, composição, ritmo, sistema gráfico, componentes, relações e forma da bifurcação sem hierarquia indevida.

### CONTENT_CANDIDATE

CTA exploratório e copy de apoio não congelada.

### DESIGN_HYPOTHESIS

Representação de capacidades, relações, macroexperiências e bifurcação Organização/Coletivo.

### PROTOTYPE_PLACEHOLDER

Organizações, Coletivos, iniciativas, histórias e evidências não selecionadas.

### REAL_DATA_REQUIRED

Identidade, iniciativa, parceria, relação, métrica, prova, história e capacidade apresentadas como reais.

### OPEN_QUESTION

Copy final, rodapé e disponibilidade concreta dos destinos posteriores.

### PROHIBITED_INFERENCE

`Organização = Business`, Coletivo = comunidade Guivos, relevância comprável, parceria fictícia, CTA comercial dominante na abertura ou coleta prematura de dados.

## 7. Guia 03 — Guivos Mall

### Ordem curta

1. `GKR-UX-HOME-MALL-MASTER-001 v1.1.0`;
2. `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001 v1.0.0`;
3. autoridades comuns.

### CANONICAL

- pergunta-mãe: **“O que pode fazer parte do seu próximo momento?”**;
- Shopping e Gift Cards são portas distintas;
- descoberta + comércio + confiança;
- Hero permanente não dominado por promoção;
- `MALL-HS-01..06`;
- oferta, recomendação, destaque e patrocínio permanecem distinguíveis;
- pontos não são medida de evolução.

### DESIGN_CREATIVE

Direção de arte, produto em cena, composição comercial, navegação, cards ou outras soluções, motion e responsividade.

### CONTENT_CANDIDATE

Copy de apoio e labels comerciais não congelados.

### DESIGN_HYPOTHESIS

Formas de descoberta, organização de ofertas, transição Shopping/Gift Cards, densidade e apresentação comercial.

### PROTOTYPE_PLACEHOLDER

Produtos, preços, marcas, campanhas e conteúdos de teste claramente provisórios.

### REAL_DATA_REQUIRED

Preço, pontos, estoque, elegibilidade, desconto, avaliação, marca/parceiro, disponibilidade e campanha reais.

### OPEN_QUESTION

Catálogo vivo, campanhas e condições comerciais futuras.

### PROHIBITED_INFERENCE

Inventar estoque/preço, transformar marca em parceria, falsa recomendação pessoal, fundir pontos e Gift Card ou esconder mídia paga como relevância orgânica.

## 8. Guia 04 — Guivos Travel

### Ordem curta

1. `GKR-UX-HOME-TRAVEL-MASTER-001 v1.1.0`;
2. `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001 v1.0.0`;
3. autoridades comuns.

### CANONICAL

- pergunta-mãe: **“Até onde o seu próximo momento pode levar você?”**;
- inspiração + operação real + acesso direto;
- serviços, destinos e experiências são territórios distintos;
- Hero permanente não dominado por oferta;
- `TRAVEL-HS-01..06`;
- não obrigar contratação conjunta.

### DESIGN_CREATIVE

Fotografia, vídeo, mapa, composição, ritmo, navegação, tipografia, motion, componentes e organização dos serviços.

### CONTENT_CANDIDATE

Copy de apoio, labels e CTAs não congelados.

### DESIGN_HYPOTHESIS

Exploração por destino, serviço, inspiração, mapa, busca ou jornada visual.

### PROTOTYPE_PLACEHOLDER

Destinos, imagens, tarifas, experiências e conteúdos explicitamente provisórios.

### REAL_DATA_REQUIRED

Destino, imagem documental, experiência, tarifa, data, vaga, fornecedor, parceiro, condição comercial e disponibilidade reais.

### OPEN_QUESTION

Inventário, tarifa, disponibilidade, cobertura geográfica, campanhas e condições comerciais futuras.

### PROHIBITED_INFERENCE

Destino fictício operado, cobertura mundial não comprovada, bundle obrigatório, parceria presumida, falsa personalização ou patrocínio disfarçado.

## 9. Guia 05 — Guivos Media

### Ordem curta

1. `GKR-UX-HOME-MEDIA-MASTER-001 v1.1.0`;
2. `GPA-005 v1.2.0`;
3. autoridades comuns.

### CANONICAL

- pergunta-mãe: **“O que você pode descobrir quando vê além do que já conhece?”**;
- curadoria antes de cronologia;
- conteúdo antes de formato;
- descoberta antes de classificação;
- 11 movimentos;
- Media ≠ Blog / portal / feed / streaming;
- autoridade editorial permanece com Media.

### DESIGN_CREATIVE

Identidade editorial, tipografia, imagem, vídeo, ritmo, hierarquia, busca, navegação, motion e microinterações.

### CONTENT_CANDIDATE

Headlines, labels e formulações editoriais não congeladas.

### DESIGN_HYPOTHESIS

Curadoria, destaque, descoberta, busca, agrupamento editorial e continuidade.

### PROTOTYPE_PLACEHOLDER

Conteúdo, história, autor, imagem e vídeo usados para testar composição.

### REAL_DATA_REQUIRED

Pessoa, autor, entrevista, história, imagem documental, vídeo, data, local, parceria, patrocínio, audiência e resultado apresentados como reais.

### OPEN_QUESTION

Lineup editorial, conteúdo de lançamento, propriedades não materializadas e assets finais.

### PROHIBITED_INFERENCE

História fictícia como real, feed cronológico como identidade, falsa personalização, conteúdo patrocinado sem identificação ou formato convertido em arquitetura do produto.

## 10. Guia 06 — Guivos Ads

### Ordem curta

1. `GKR-UX-HOME-ADS-MASTER-001 v1.1.0`;
2. `GPA-007 v1.3.0`;
3. autoridades comuns.

### CANONICAL

- contexto antes de formato;
- objetivo comercial legítimo antes de especificação técnica;
- princípio de abertura: **“Sua marca dentro do contexto certo.”**;
- **“O contexto define onde uma marca faz sentido. Ads transforma essa oportunidade em uma solução comercial.”**;
- sete movimentos;
- capacidade financeira ≠ elegibilidade;
- publicidade identificada;
- autoridade da superfície anfitriã;
- contexto pessoal protegido fora da comercialização;
- qualificação progressiva.

### DESIGN_CREATIVE

Expressão B2B, visualização de contextos, mídia, composição, interação da qualificação, motion, componentes e responsividade.

### CONTENT_CANDIDATE

Pergunta de Hero não congelada, headline de apoio e microcopy comercial.

### DESIGN_HYPOTHESIS

Qualificação progressiva, visualização dos contextos, apresentação de soluções e sequência comercial.

### PROTOTYPE_PLACEHOLDER

Marca, campanha, formato, investimento, mockup e cenário comercial ilustrativos.

### REAL_DATA_REQUIRED

Preço, CPM/CPC, alcance, inventário, performance, case, parceiro, cliente e disponibilidade comercial.

### OPEN_QUESTION

Pricing futuro, catálogo vivo de formatos, capacidade por superfície, inventário e condições comerciais.

### PROHIBITED_INFERENCE

Compra de relevância pessoal, segmentação por contexto protegido, performance inventada, CPM/CPC como promessa ou autoridade Ads sobre conteúdo/experiência anfitriã.

## 11. Guia 07 — Guivos Business

### Ordem curta

1. `GKR-UX-HOME-BUSINESS-MASTER-001 v1.1.0`;
2. `GKR-UX-HOME-BUSINESS-SOURCELOCK-001 v1.1.0`;
3. `GKR-UX-HOME-BUSINESS-CONVERSION-002 v1.0.0`;
4. `GKR-UX-HOME-BUSINESS-AUTHORITY-001 v1.0.0`;
5. `GPA-004 v1.6.0`;
6. autoridades comuns.

### CANONICAL

- pergunta-mãe: **“O que sua empresa pode tornar possível para as pessoas?”**;
- 10 movimentos;
- autonomia: empresa apoia, pessoa escolhe;
- quatro planos vigentes;
- Pontos Guivos fora da Home pública;
- contratação online como direção vigente;
- Intelligence precisa tornar valor tangível e compreensível;
- dashboard/KPI/gráfico não são obrigação visual.

### DESIGN_CREATIVE

Identidade visual, composição, planos, configurador, representação do Intelligence, tipografia, paleta, mídia, motion, componentes e responsividade.

### CONTENT_CANDIDATE

Supporting copy e formulações não congeladas.

### DESIGN_HYPOTHESIS

Comparação de planos, configuração, progressão comercial, capacidades e representação do Intelligence, inclusive gráficos/dashboard apenas se a designer escolher.

### PROTOTYPE_PLACEHOLDER

Preços, limites, entitlements, integrações, empresas e exemplos de configuração.

### REAL_DATA_REQUIRED

Preço final, limite, SLA, entitlement, integração, disponibilidade geográfica/moeda, case, métrica, resultado e condição comercial.

### OPEN_QUESTION

Detalhes comerciais não formalizados, pricing, limites, SLA, integrações, disponibilidade e assets finais.

### PROHIBITED_INFERENCE

Inventar pricing/limites/SLA, transformar Business em HR software/LMS/plataforma de pontos ou entregar decisão sobre evolução da Pessoa à empresa.

## 12. Guia 08 — Guivos Intelligence

### Ordem curta

1. `GKR-UX-HOME-INTELLIGENCE-MASTER-001 v1.0.0`;
2. `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0`;
3. `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001 v1.0.0`;
4. `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001 v1.0.0`;
5. `GPA-006 v2.0.0`;
6. autoridades comuns.

### CANONICAL

- unidade de valor = compreensão útil e contextualizada;
- `COMPREENDER ≠ DECIDIR`;
- 11 movimentos;
- Pessoa/Journey ≠ Business/população;
- relações, temporalidade, evidência, proveniência e explicabilidade;
- Intelligence conecta autoridades, não as absorve;
- tendência ≠ destino; sinal ≠ certeza; correlação ≠ causalidade.

### DESIGN_CREATIVE

Tipografia, cor, composição, imagem, ilustração, visualização, motion, componentes e metáforas visuais.

Nenhum dashboard, grafo, chatbot, cérebro digital, HUD, rede neural ou estética tecnológica é obrigatório.

### CONTENT_CANDIDATE

Microcopy e formulações não congeladas pelas autoridades específicas.

### DESIGN_HYPOTHESIS

Representações de relações, padrões, mudança, temporalidade, evidência e explicabilidade.

### PROTOTYPE_PLACEHOLDER

Dados e exemplos analíticos conceituais claramente ilustrativos.

### REAL_DATA_REQUIRED

Métrica, acurácia, case, integração, tecnologia operacional, dado, resultado ou capacidade apresentada como existente.

### OPEN_QUESTION

Expressão visual, exemplos finais, assets e escolhas de interação.

### PROHIBITED_INFERENCE

Intelligence = chatbot/dashboard/Neo4j, IA decisora, previsão determinística, causalidade sem evidência, certeza a partir de tendência ou exposição de contexto pessoal protegido.

## 13. Acessibilidade e responsividade — regra comum

Todos os oito guias devem exigir:

- desktop, tablet e mobile coerentes quando contratados;
- mobile com menor simultaneidade, não mero empilhamento;
- contraste;
- foco/teclado;
- touch targets;
- texto ampliado;
- ordem semântica;
- reduced motion;
- mídia com fallback;
- internacionalização e expansão de texto;
- significado independente de hover, vídeo ou animação.

## 14. Autoauditoria humana comum

Antes de considerar a criação pronta para revisão:

- [ ] Master foi lido integralmente;
- [ ] significado e papel da Home foram preservados;
- [ ] participante e produto não foram confundidos;
- [ ] nenhum dado real foi inventado;
- [ ] placeholder parece provisório;
- [ ] questões abertas continuam abertas;
- [ ] nenhuma referência externa virou autoridade;
- [ ] liberdade visual foi exercida sem redefinir produto;
- [ ] mobile/responsividade foram tratados;
- [ ] acessibilidade foi considerada;
- [ ] copy candidata não foi promovida silenciosamente;
- [ ] nenhuma inferência proibida entrou na solução.

## 15. Apêndice opcional de IA

Somente quando IA for usada, o guia deverá acrescentar:

1. `execution_id`;
2. objetivo da execução;
3. checkpoint/SHAs;
4. fontes autorizadas;
5. oito classes de informação;
6. prompt controlado;
7. status inicial do output = `EXPLORAÇÃO / NÃO CANÔNICA`;
8. autoauditoria da saída.

O template é `GKR-UX-HOMES-GENINPUT-001 v2.1.0`.

## 16. Estado

```text
GUIDE BLUEPRINTS
→ 8 / 8 COMPLETE

HUMAN-FIRST
→ YES

AI APPENDIX
→ OPTIONAL

POST-MERGE SHAs
→ PENDING BY DESIGN
→ MUST NOT BE INVENTED

V6 EXTERNAL GUIDES
→ NOT_YET_MATERIALIZED
```
