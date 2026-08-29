---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 4.1.0
owner: Experience Architecture
last_updated: 2026-08-29
normative: true
maturity: design_delivery_manifest_preserved_new_emissions_suspended_during_full_corpus_audit
depends_on:
  - GKR-STATE-001
  - GKR-FULL-CORPUS-AUDIT-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
related:
  - GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001
  - GKR-UX-HOME-PERSON-GENINPUT-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-OC-MEDIA-SUPPLY-001
  - GKR-UX-HOME-OC-GENINPUT-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-MALL-MEDIA-SUPPLY-001
  - GKR-UX-HOME-MALL-GENINPUT-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001
  - GKR-UX-HOME-TRAVEL-GENINPUT-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GPA-005
  - GKR-UX-HOME-MEDIA-GENINPUT-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GPA-007
  - GKR-UX-HOME-ADS-GENINPUT-001
  - GKR-UX-HOME-BUSINESS-SOURCELOCK-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-BUSINESS-CONVERSION-002
  - GKR-UX-HOME-BUSINESS-AUTHORITY-001
  - GPA-004
  - GKR-UX-HOME-BUSINESS-GENINPUT-001
  - GKR-UX-HOME-INTELLIGENCE-HANDOFF-001
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-GENINPUT-001
  - GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001
  - GPA-006
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 0. Gate vigente durante a Auditoria Integral do GKR

Este Manifesto preserva o método e a composição documental utilizados nas emissões históricas de Design.

A emissão v4, posteriormente materializada e registrada por `GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001`, permanece um **fato histórico reproduzível de seu checkpoint**. A preparação e a emissão daquele snapshot não constituem autorização atual para reutilizar o pacote, criar nova emissão ou iniciar nova exploração visual.

Durante a Auditoria Integral:

```text
MANIFESTO / MÉTODO DE ENTREGA
→ PRESERVADO

SNAPSHOTS V1–V4
→ PRESERVADOS COMO HISTÓRICO

NOVA EMISSÃO / REEMISSÃO OPERACIONAL
→ SUSPENSA

ENTREGA PARA DESIGN / FIGMA / WIREFRAME / UI / PROTÓTIPO
→ NÃO AUTORIZADA COMO NOVA EXECUÇÃO
```

A linguagem das seções abaixo sobre preparação da v4, próximo ato, liberação do pacote e execução em Design descreve o regime daquele checkpoint e deve ser lida como proveniência operacional.

Uma futura emissão exige novo ato governado após os gates aplicáveis da auditoria, revalidação do corpus então vigente e novo checkpoint reproduzível.

```text
MANIFESTO EXISTENTE
≠ PACOTE ATUALMENTE LIBERADO

SNAPSHOT HISTÓRICO
≠ BASELINE VISUAL VIGENTE

REEMISSÃO
≠ ATUALIZAÇÃO AUTOMÁTICA
```

---

## 1. Finalidade

Este manifesto define a **preparação da emissão v4 do snapshot oficial a ser entregue à pessoa responsável por Design, UX e UI das oito Homes públicas já convergidas da Guivos**.

A emissão v4 incorpora a **Home Pública — Guivos Intelligence** ao mesmo método de entrega já utilizado para Pessoa, Organizações e Coletivos, Mall, Travel, Media, Ads e Business.

Ela não cria mapa, wireframe, direção visual, UI ou protótipo no GKR. Sua função é operacional:

- fixar quais fontes canônicas entram no próximo handoff;
- separar cada Home em contexto próprio;
- determinar a ordem de leitura;
- entregar Source Lock + Prompt controlado;
- preservar as fronteiras específicas de Intelligence;
- permitir que Design/Figma Make produza exploração fora desta frente canônica;
- manter o resultado inicial como `EXPLORAÇÃO`.

Regra:

> **O GKR emite o contexto controlado. A frente de Design materializa. A emissão não é o Design.**

E, para esta revisão:

> **MANIFESTO V4 PREPARADO ≠ SNAPSHOT V4 EMITIDO.**

---

## 2. Relação com a emissão v3

A v4 é uma nova geração e **não substitui retroativamente a emissão v3**.

A composição canônica registrada pelo Manifesto v3 é:

```text
25 FONTES CANÔNICAS
+
7 GUIAS OPERACIONAIS LEIA-PRIMEIRO
=
32 ARQUIVOS NO SNAPSHOT EXTERNO V3
```

A branch `delivery/design-handoff-v3` permanece uma referência histórica separada e não deve ser reescrita para representar v4.

A v4 deve nascer em nova emissão, a partir de conteúdo integrado à `main` e de um checkpoint único reconciliado após o merge desta preparação.

```text
V3 → PRESERVADA
V4 → NOVA EMISSÃO / NOVO CHECKPOINT / NOVO PACOTE
```

---

## 3. Checkpoint da emissão v4

Esta revisão **não antecipa** o SHA canônico da futura emissão.

Após integração em `main`, o ato de materialização deverá registrar em documento/artefato operacional próprio:

```text
main canônica de origem: <SHA PÓS-MERGE>
branch externa: delivery/design-handoff-v4
snapshot commit: <SHA DO SNAPSHOT>
snapshot tree: <TREE DO SNAPSHOT>
```

A branch externa deverá nascer de conteúdo já integrado à `main`, conter somente o pacote externo de distribuição e não constituir fonte canônica paralela.

Regra:

> **Cada entrega é um snapshot reproduzível. Se o GKR evoluir materialmente, uma nova versão do pacote deve ser emitida; arquivos de checkpoints diferentes não devem ser misturados sem reconciliação explícita.**

---

## 4. Composição canônica da v4: 31 fontes únicas

A v4 preserva integralmente as **25 fontes canônicas** listadas na v3 e acrescenta **6 fontes específicas de Guivos Intelligence** necessárias ao contexto mínimo isolado da Home.

### 4.1 Documento comum

1. `docs/experience-architecture/public-homes-design-handoff.md`
   - ID: `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.3.0;
   - função: governa autorização da fase de Design, ordem de autoridade, liberdade de materialização e controle de ferramentas generativas para oito Homes.

### 4.2 Home Pública — Pessoa

2. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001`;
3. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001`;
4. `docs/experience-architecture/public-home-person-generative-design-source-lock.md` — `GKR-UX-HOME-PERSON-GENINPUT-001`.

### 4.3 Home Pública — Organizações e Coletivos

5. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001`;
6. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001`;
7. `docs/experience-architecture/public-home-organizations-collectives-generative-design-source-lock.md` — `GKR-UX-HOME-OC-GENINPUT-001`.

### 4.4 Home Pública — Guivos Mall

8. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001`;
9. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001`;
10. `docs/experience-architecture/public-home-mall-generative-design-source-lock.md` — `GKR-UX-HOME-MALL-GENINPUT-001`.

### 4.5 Home Pública — Guivos Travel

11. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001`;
12. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001`;
13. `docs/experience-architecture/public-home-travel-generative-design-source-lock.md` — `GKR-UX-HOME-TRAVEL-GENINPUT-001`.

### 4.6 Home Pública — Guivos Media

14. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001`;
15. `docs/product-architecture/media.md` — `GPA-005`;
16. `docs/experience-architecture/public-home-media-generative-design-source-lock.md` — `GKR-UX-HOME-MEDIA-GENINPUT-001`.

### 4.7 Home Pública — Guivos Ads

17. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001`;
18. `docs/product-architecture/ads.md` — `GPA-007`;
19. `docs/experience-architecture/public-home-ads-generative-design-source-lock.md` — `GKR-UX-HOME-ADS-GENINPUT-001`.

### 4.8 Home Pública — Guivos Business

20. `docs/experience-architecture/public-home-business-source-lock.md` — `GKR-UX-HOME-BUSINESS-SOURCELOCK-001`;
21. `docs/experience-architecture/public-home-business-master-document.md` — `GKR-UX-HOME-BUSINESS-MASTER-001`;
22. `docs/experience-architecture/public-home-business-conversion-authority-v2.md` — `GKR-UX-HOME-BUSINESS-CONVERSION-002`;
23. `docs/experience-architecture/public-home-business-authority-contracts.md` — `GKR-UX-HOME-BUSINESS-AUTHORITY-001`;
24. `docs/product-architecture/business.md` — `GPA-004`;
25. `docs/experience-architecture/public-home-business-generative-design-source-lock.md` — `GKR-UX-HOME-BUSINESS-GENINPUT-001`.

Business continua com contexto específico maior porque suas fronteiras vigentes são distribuídas por Source Lock, Documento Mestre, Conversão, Contratos de Autoridade e `GPA-004`.

### 4.9 Home Pública — Guivos Intelligence

26. `docs/experience-architecture/public-home-intelligence-generative-design-source-lock.md`
   - ID: `GKR-UX-HOME-INTELLIGENCE-GENINPUT-001` v1.0.0;
   - função: Source Lock Operacional + Prompt controlado da primeira exploração.

27. `docs/experience-architecture/public-home-intelligence-design-handoff.md`
   - ID: `GKR-UX-HOME-INTELLIGENCE-HANDOFF-001` v1.0.0;
   - função: contrato específico entre a Home congelada e a materialização visual.

28. `docs/experience-architecture/public-home-intelligence-source-lock.md`
   - ID: `GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001` v1.0.0;
   - função: autoridade congelada da Home para materialização.

29. `docs/experience-architecture/public-home-intelligence-master-document.md`
   - ID: `GKR-UX-HOME-INTELLIGENCE-MASTER-001` v0.1.1;
   - função: significado público, narrativa, copy e limites consolidados.

30. `docs/product-architecture/intelligence-product-source-lock.md`
   - ID: `GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001` v1.0.0;
   - função: fronteira pública superior do produto Intelligence.

31. `docs/product-architecture/intelligence.md`
   - ID: `GPA-006` v2.0.0;
   - função: autoridade superior de produto.

O contrato narrativo `GKR-UX-HOME-INTELLIGENCE-NARRATIVE-001 v0.2.1` e o princípio transversal `GKR-UX-HOMES-OUTCOME-001 v1.0.0` continuam autoridades do GKR. Conforme o GENINPUT de Intelligence, não precisam ser adicionados como arquivos extras à ferramenta quando suas funções já estiverem preservadas pelas fontes acima. Isso reduz duplicação sem reduzir autoridade.

---

## 5. Decisão operacional: separar a entrega por Home

A entrega externa **não deve apresentar as 31 fontes como conjunto indiferenciado**.

O uso operacional deve ser separado em oito contextos independentes de trabalho.

Princípio:

> **Uma Home = um contexto de trabalho isolado.**

A única fonte comum às oito Homes é `GKR-UX-HOMES-DESIGN-HANDOFF-001`, mantida em `00-LEIA-PRIMEIRO`.

Os `LEIA-PRIMEIRO` específicos são arquivos operacionais de embalagem, não documentos canônicos do GKR e não novas autoridades arquiteturais.

---

## 6. Estrutura oficial planejada do pacote externo v4

```text
GUIVOS-HOMES-DESIGN-HANDOFF-v4/
├── 00-LEIA-PRIMEIRO/
│   └── 00-Handoff-Canonico-das-Homes.md
│
├── 01-HOME-PESSOA/
│   ├── 00-LEIA-PRIMEIRO-PESSOA.md
│   ├── 01-Documento-Mestre.md
│   ├── 02-Reconciliacao-Pos-Media.md
│   └── 03-Source-Lock-Prompt.md
│
├── 02-HOME-ORGANIZACOES-E-COLETIVOS/
│   ├── 00-LEIA-PRIMEIRO-ORGANIZACOES-E-COLETIVOS.md
│   ├── 01-Documento-Mestre.md
│   ├── 02-Reconciliacao-Pos-Media.md
│   └── 03-Source-Lock-Prompt.md
│
├── 03-HOME-MALL/
│   ├── 00-LEIA-PRIMEIRO-MALL.md
│   ├── 01-Documento-Mestre.md
│   ├── 02-Reconciliacao-Pos-Media.md
│   └── 03-Source-Lock-Prompt.md
│
├── 04-HOME-TRAVEL/
│   ├── 00-LEIA-PRIMEIRO-TRAVEL.md
│   ├── 01-Documento-Mestre.md
│   ├── 02-Reconciliacao-Pos-Media.md
│   └── 03-Source-Lock-Prompt.md
│
├── 05-HOME-MEDIA/
│   ├── 00-LEIA-PRIMEIRO-MEDIA.md
│   ├── 01-Documento-Mestre.md
│   ├── 02-GPA-005-Guivos-Media.md
│   └── 03-Source-Lock-Prompt.md
│
├── 06-HOME-ADS/
│   ├── 00-LEIA-PRIMEIRO-ADS.md
│   ├── 01-Documento-Mestre.md
│   ├── 02-GPA-007-Guivos-Ads.md
│   └── 03-Source-Lock-Prompt.md
│
├── 07-HOME-BUSINESS/
│   ├── 00-LEIA-PRIMEIRO-BUSINESS.md
│   ├── 01-Source-Lock-Semantico.md
│   ├── 02-Documento-Mestre.md
│   ├── 03-Conversao-Global.md
│   ├── 04-Contratos-de-Autoridade.md
│   ├── 05-GPA-004-Guivos-Business.md
│   └── 06-Source-Lock-Prompt.md
│
└── 08-HOME-INTELLIGENCE/
    ├── 00-LEIA-PRIMEIRO-INTELLIGENCE.md
    ├── 01-Source-Lock-Operacional-Prompt.md
    ├── 02-Handoff-Especifico.md
    ├── 03-Source-Lock-da-Home.md
    ├── 04-Documento-Mestre.md
    ├── 05-Product-Source-Lock.md
    └── 06-GPA-006-Guivos-Intelligence.md
```

Composição planejada:

```text
31 FONTES CANÔNICAS CONGELADAS
+
8 GUIAS OPERACIONAIS LEIA-PRIMEIRO
=
39 ARQUIVOS NO SNAPSHOT EXTERNO V4
```

A contagem só deve ser promovida a estado de emissão depois que os 31 paths forem reconfirmados no checkpoint pós-merge e os oito guias forem materializados.

---

## 7. Conteúdo mínimo dos `LEIA-PRIMEIRO`

Cada guia operacional deve informar:

- Home em trabalho;
- Handoff Canônico comum como primeira leitura;
- documentos específicos do contexto;
- ordem de leitura;
- arquivo que contém o prompt controlado;
- proibição de misturar documentos específicos de outras Homes;
- output inicial sempre `EXPLORAÇÃO`;
- ausência de autoridade da ferramenta para redefinir arquitetura/significado;
- checkpoint congelado da emissão v4.

Para Intelligence, a ordem operacional é:

```text
1. HANDOFF CANÔNICO COMUM
↓
2. GENINPUT / SOURCE LOCK OPERACIONAL
↓
3. HANDOFF ESPECÍFICO INTELLIGENCE
↓
4. HOME SOURCE LOCK
↓
5. DOCUMENTO MESTRE
↓
6. PRODUCT SOURCE LOCK
↓
7. GPA-006
↓
8. EXECUÇÃO NA FRENTE DE DESIGN
↓
9. OUTPUT = EXPLORAÇÃO
```

A leitura pode ser reordenada pelo `LEIA-PRIMEIRO` para compreensão humana, mas a autoridade semântica permanece a definida pelos documentos vigentes.

---

## 8. Regra de carregamento em ferramentas generativas

Não carregar simultaneamente documentos específicos das oito Homes na mesma execução.

Para Intelligence, utilizar somente o contexto específico acima. Não adicionar automaticamente:

- toda a documentação técnica de IA;
- Neo4j;
- GraphRAG;
- Power BI;
- Guivos.ai;
- Journey detalhado;
- Business detalhado;
- benchmarks;
- rascunhos de conversa.

Tecnologias e documentos adicionais só entram para resolver dúvida concreta e devem permanecer subordinados à definição do produto.

---

## 9. Contratos de Intelligence que o pacote deve preservar

```text
UNIDADE DE VALOR = COMPREENSÃO ÚTIL E CONTEXTUALIZADA
INFORMAÇÃO ≠ COMPREENSÃO
COMPREENDER ≠ DECIDIR
RELAÇÃO ≠ CAUSA
CORRELAÇÃO ≠ CAUSALIDADE
SINAL ≠ CERTEZA
TENDÊNCIA ≠ DESTINO
PERCEBER ANTES ≠ PREVER O FUTURO
TECNOLOGIA ≠ PRODUTO
```

Também devem permanecer verificáveis:

- 11 movimentos funcionais, sem obrigação de 11 seções físicas;
- `M03 ≠ M10`;
- `M04 ≠ M05`;
- M08 com peso real de explicabilidade;
- M09 preservando autonomia;
- M11 aspiracional e não preditivo;
- Pessoa/Journey distinta de Business/população;
- assimetria de privacidade;
- exemplos conceituais identificados como não operacionais;
- ausência de claims inventados.

---

## 10. Formato de entrega

O formato oficial de transferência permanece **Markdown (`.md`)**.

PDF pode existir como material auxiliar para leitura humana, mas não substitui Markdown como input primário.

A emissão deverá ser distribuída também como `.zip`, preservando a separação por Home.

---

## 11. Materiais deliberadamente fora do pacote inicial

Não fazem parte do input inicial:

- template genérico interno de input generativo;
- fases/auditorias históricas;
- benchmarks;
- documentos antigos de Hero/Header/navegação;
- decisões intermediárias;
- rascunhos de conversa;
- documentação técnica de Engenharia;
- pricing não formalizado;
- documentação tecnológica de Intelligence não requerida pelo GENINPUT;
- todo o restante do GKR.

Materiais adicionais só entram quando uma dúvida concreta exigir aprofundamento deliberado.

---

## 12. Regras de integridade da entrega v4

O pacote v4 será íntegro quando:

1. contiver exatamente as 31 fontes canônicas listadas neste manifesto;
2. todos os documentos canônicos forem extraídos do mesmo commit canônico pós-merge;
3. contiver oito `LEIA-PRIMEIRO`, um por Home;
4. nenhum texto canônico for resumido ou reescrito para caber no pacote;
5. nomes externos não alterarem IDs ou conteúdo interno;
6. cada Source Lock/GENINPUT permanecer vinculado à respectiva Home;
7. documentos específicos estiverem fisicamente separados por Home;
8. não houver mistura de documentos históricos como fonte vigente;
9. outputs generativos começarem como `EXPLORAÇÃO`;
10. não existir autorização implícita para Engenharia ou publicação;
11. o pacote puder ser reproduzido a partir do checkpoint informado;
12. guias operacionais não se apresentarem como autoridade arquitetural;
13. v1, v2 e v3 permanecerem preservadas;
14. Business manter exatamente seu contexto vigente;
15. Intelligence possuir exatamente `GENINPUT + HANDOFF ESPECÍFICO + HOME SOURCE LOCK + MASTER + PRODUCT SOURCE LOCK + GPA-006`, além do Handoff comum;
16. Intelligence preservar seus 11 movimentos, fronteiras, privacidade, explicabilidade, autonomia e não predição;
17. nenhum mapa, wireframe, direção visual, UI ou protótipo ser fabricado pelo ato de emissão do GKR.

---

## 13. Evolução e reemissão

Se qualquer fonte obrigatória sofrer mudança material depois do snapshot, avaliar se a alteração afeta significado, narrativa, invariantes, contrato complementar, prompt controlado, liberdade de Design ou proibições de inferência.

Se afetar, emitir nova versão do manifesto e novo snapshot. Não substituir arquivos individualmente dentro de pacote já distribuído sem registrar nova versão.

Histórico:

- v1: preservada em sua emissão própria;
- v2: preservada em sua emissão própria;
- v3: `delivery/design-handoff-v3` — preservar sem reescrita;
- v4: futura `delivery/design-handoff-v4`, somente após integração e checkpoint pós-merge.

---

## 14. Próximo ato após integração

```text
MAIN CANÔNICA INTEGRADA
↓
CAPTURAR SHA EXATO PÓS-MERGE
↓
REVALIDAR 31/31 FONTES
↓
MATERIALIZAR delivery/design-handoff-v4
↓
CRIAR 8 LEIA-PRIMEIRO OPERACIONAIS
↓
GERAR SNAPSHOT/ZIP V4
↓
VALIDAR REPRODUTIBILIDADE E ISOLAMENTO
↓
REGISTRAR CHECKPOINT DA EMISSÃO
↓
SOMENTE ENTÃO LIBERAR O PACOTE PARA A FRENTE DE DESIGN
```

Esta preparação não executa esse ato.

---

## 15. Síntese

A versão `4.0.0` incorporou Guivos Intelligence como oitava Home ao método canônico de entrega, preservou as 25 fontes da v3, acrescentou seis fontes específicas de Intelligence e preparou um snapshot externo de **31 fontes canônicas + 8 guias operacionais = 39 arquivos**.

> **DESIGN DELIVERY V4 PREPARADO — SNAPSHOT V4 NÃO EMITIDO — DESIGN NÃO INICIADO.**

Nota histórica posterior: o snapshot v4 foi efetivamente emitido e possui registro próprio em `GKR-UX-HOMES-DESIGN-DELIVERY-V4-SNAPSHOT-001`. A frase acima permanece como estado desta versão preparatória no momento em que foi escrita.

---

## 16. Estado vigente sob auditoria integral

```text
V1–V4
→ HISTÓRICO PRESERVADO

MANIFESTO
→ MÉTODO PRESERVADO

NOVA EMISSÃO / REEMISSÃO / LIBERAÇÃO PARA DESIGN
→ SUSPENSA DURANTE A AUDITORIA INTEGRAL

FUTURA RETOMADA
→ EXIGE NOVO ATO GOVERNADO + REVALIDAÇÃO PÓS-AUDITORIA
```

O Manifesto continua normativo para a integridade de uma futura emissão quando reativada; não funciona como autorização de emissão no estado atual.