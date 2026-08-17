---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 3.0.0
owner: Experience Architecture
last_updated: 2026-08-16
normative: true
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
related:
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
  - GKR-UX-HOMES-DESIGN-DELIVERY-V2-SNAPSHOT-001
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este manifesto define a **emissão v3 do snapshot oficial de documentos a ser entregue à pessoa responsável por Design, UX e UI das sete Homes públicas já convergidas da Guivos**.

A emissão v3 adiciona a **Home Pública — Guivos Business** ao mesmo método de entrega já utilizado nas emissões anteriores.

Ela não cria mapa, wireframe, direção visual, UI ou protótipo no GKR. Sua função é operacional:

- fixar quais fontes canônicas entram no handoff;
- separar cada Home em contexto próprio;
- determinar a ordem de leitura;
- entregar Source Lock + Prompt controlado;
- permitir que a designer/Figma Make produza a exploração fora desta frente canônica;
- manter o resultado inicial como `EXPLORAÇÃO`.

As emissões v1 e v2 permanecem historicamente íntegras e não são alteradas retroativamente.

Regra:

> **O GKR emite o contexto controlado. A frente de Design materializa. A emissão não é o Design.**

---

## 2. Checkpoint da emissão v3

A emissão v3 somente poderá ser materializada **depois da integração canônica** deste manifesto, do Handoff Canônico v1.2.0 e do Source Lock Operacional + Prompt do Business.

O ato pós-merge deverá registrar em documento próprio:

```text
main canônica de origem: <SHA PÓS-MERGE>
branch externa: delivery/design-handoff-v3
snapshot commit: <SHA DO SNAPSHOT>
snapshot tree: <TREE DO SNAPSHOT>
```

A branch externa deverá nascer de conteúdo já integrado à `main`, conter somente o pacote externo de distribuição e não constituir fonte canônica paralela.

Regra:

> **Cada entrega é um snapshot reproduzível. Se o GKR evoluir materialmente, uma nova versão do pacote deve ser emitida; arquivos de checkpoints diferentes não devem ser misturados sem reconciliação explícita.**

---

## 3. Composição canônica da v3: 25 documentos únicos

### 3.1 Documento comum

1. `docs/experience-architecture/public-homes-design-handoff.md`
   - ID: `GKR-UX-HOMES-DESIGN-HANDOFF-001` v1.2.0;
   - função: governa autorização da fase de Design, ordem de autoridade, liberdade de materialização e controle de ferramentas generativas.

### 3.2 Home Pública — Pessoa

2. `docs/experience-architecture/public-home-master-document.md` — `GKR-UX-HOME-MASTER-001`;
3. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001`;
4. `docs/experience-architecture/public-home-person-generative-design-source-lock.md` — `GKR-UX-HOME-PERSON-GENINPUT-001`.

### 3.3 Home Pública — Organizações e Coletivos

5. `docs/experience-architecture/public-home-organizations-collectives-master-document.md` — `GKR-UX-HOME-OC-MASTER-001`;
6. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-OC-MEDIA-SUPPLY-001`;
7. `docs/experience-architecture/public-home-organizations-collectives-generative-design-source-lock.md` — `GKR-UX-HOME-OC-GENINPUT-001`.

### 3.4 Home Pública — Guivos Mall

8. `docs/experience-architecture/public-home-mall-master-document.md` — `GKR-UX-HOME-MALL-MASTER-001`;
9. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001`;
10. `docs/experience-architecture/public-home-mall-generative-design-source-lock.md` — `GKR-UX-HOME-MALL-GENINPUT-001`.

### 3.5 Home Pública — Guivos Travel

11. `docs/experience-architecture/public-home-travel-master-document.md` — `GKR-UX-HOME-TRAVEL-MASTER-001`;
12. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md` — `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001`;
13. `docs/experience-architecture/public-home-travel-generative-design-source-lock.md` — `GKR-UX-HOME-TRAVEL-GENINPUT-001`.

### 3.6 Home Pública — Guivos Media

14. `docs/experience-architecture/public-home-media-master-document.md` — `GKR-UX-HOME-MEDIA-MASTER-001`;
15. `docs/product-architecture/media.md` — `GPA-005`;
16. `docs/experience-architecture/public-home-media-generative-design-source-lock.md` — `GKR-UX-HOME-MEDIA-GENINPUT-001`.

### 3.7 Home Pública — Guivos Ads

17. `docs/experience-architecture/public-home-ads-master-document.md` — `GKR-UX-HOME-ADS-MASTER-001`;
18. `docs/product-architecture/ads.md` — `GPA-007`;
19. `docs/experience-architecture/public-home-ads-generative-design-source-lock.md` — `GKR-UX-HOME-ADS-GENINPUT-001`.

### 3.8 Home Pública — Guivos Business

20. `docs/experience-architecture/public-home-business-source-lock.md`
   - ID: `GKR-UX-HOME-BUSINESS-SOURCELOCK-001`;
   - função: lock semântico superior da futura materialização.

21. `docs/experience-architecture/public-home-business-master-document.md`
   - ID: `GKR-UX-HOME-BUSINESS-MASTER-001`;
   - função: Documento Mestre público da Home Business.

22. `docs/experience-architecture/public-home-business-conversion-authority-v2.md`
   - ID: `GKR-UX-HOME-BUSINESS-CONVERSION-002`;
   - função: contratação online e modelos de implementação/operação.

23. `docs/experience-architecture/public-home-business-authority-contracts.md`
   - ID: `GKR-UX-HOME-BUSINESS-AUTHORITY-001`;
   - função: fronteiras de autoridade entre pessoa, empresa, Business, Journey, Incentivos, ecossistema e Intelligence.

24. `docs/product-architecture/business.md`
   - ID: `GPA-004`;
   - função: arquitetura funcional/comercial vigente do Guivos Business.

25. `docs/experience-architecture/public-home-business-generative-design-source-lock.md`
   - ID: `GKR-UX-HOME-BUSINESS-GENINPUT-001`;
   - função: Source Lock Operacional + Prompt controlado para a designer/Figma Make.

Business possui um contexto específico maior que as demais Homes porque seu Source Lock vigente exige preservar separadamente Documento Mestre, Conversão, Contratos de Autoridade e `GPA-004`. Não reduzir o pacote por conveniência sem autoridade posterior que consolide explicitamente essas fronteiras.

---

## 4. Decisão operacional: separar a entrega por Home

A entrega externa **não deve apresentar os 25 documentos como conjunto indiferenciado**.

O uso operacional deve ser separado em sete contextos independentes de trabalho.

Princípio:

> **Uma Home = um contexto de trabalho isolado.**

A única fonte comum às sete Homes é `GKR-UX-HOMES-DESIGN-HANDOFF-001`, mantida em `00-LEIA-PRIMEIRO`.

As seis Homes já presentes na v2 preservam sua composição anterior.

A Home Business recebe o conjunto maior definido pelo próprio Source Lock Business.

Os `LEIA-PRIMEIRO` específicos são **arquivos operacionais de embalagem**, não documentos canônicos do GKR e não novas autoridades arquiteturais.

---

## 5. Estrutura oficial do pacote externo v3

```text
GUIVOS-HOMES-DESIGN-HANDOFF-v3/
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
└── 07-HOME-BUSINESS/
    ├── 00-LEIA-PRIMEIRO-BUSINESS.md
    ├── 01-Source-Lock-Semantico.md
    ├── 02-Documento-Mestre.md
    ├── 03-Conversao-Global.md
    ├── 04-Contratos-de-Autoridade.md
    ├── 05-GPA-004-Guivos-Business.md
    └── 06-Source-Lock-Prompt.md
```

O pacote externo v3 conterá:

```text
25 FONTES CANÔNICAS CONGELADAS
+
7 GUIAS OPERACIONAIS LEIA-PRIMEIRO
=
32 ARQUIVOS NO SNAPSHOT EXTERNO
```

Os sete guias operacionais não entram na contagem de fontes canônicas e não recebem IDs normativos do GKR.

---

## 6. Conteúdo mínimo dos `LEIA-PRIMEIRO`

Cada guia operacional deve informar:

- qual Home está sendo trabalhada;
- que o Handoff Canônico comum deve ser lido primeiro;
- quais documentos específicos formam o contexto daquela Home;
- ordem de leitura;
- qual arquivo contém o prompt controlado;
- que documentos das outras Homes não devem ser adicionados à mesma execução;
- que o output inicial é sempre `EXPLORAÇÃO`;
- que a ferramenta não possui autoridade para alterar arquitetura, significado ou decisões canônicas;
- qual é o checkpoint congelado do pacote v3.

Para as seis Homes anteriores, manter o fluxo de quatro fontes canônicas já vigente.

Para Business, usar:

```text
1. HANDOFF CANÔNICO COMUM
↓
2. SOURCE LOCK SEMÂNTICO BUSINESS
↓
3. DOCUMENTO MESTRE BUSINESS
↓
4. CONVERSÃO GLOBAL VIGENTE
↓
5. CONTRATOS DE AUTORIDADE
↓
6. GPA-004
↓
7. SOURCE LOCK OPERACIONAL + PROMPT
↓
8. EXECUÇÃO NA FRENTE DE DESIGN
↓
9. OUTPUT = EXPLORAÇÃO
```

---

## 7. Regra de carregamento no Figma Make e ferramentas equivalentes

Para Pessoa, Organizações e Coletivos, Mall, Travel, Media e Ads, permanece a regra vigente de contexto mínimo isolado da v2.

Para Guivos Business, utilizar somente as sete fontes canônicas identificadas na seção anterior.

Não carregar simultaneamente documentos específicos das sete Homes na mesma execução generativa.

A comparação entre Homes pode ocorrer em revisão humana de coerência da família Guivos, mas não como mistura indiscriminada de contexto no momento da geração.

A separação física das pastas é uma proteção semântica, não apenas conveniência de organização.

---

## 8. Formato de entrega

O formato oficial de transferência permanece **Markdown (`.md`)**.

PDF pode ser produzido como material auxiliar para leitura humana, mas não substitui Markdown como input primário da ferramenta generativa.

A emissão deverá ser distribuída também como `.zip`, preservando exatamente a separação por Home definida neste manifesto.

---

## 9. Materiais deliberadamente fora do pacote

Não fazem parte da entrega inicial:

- template genérico interno de input generativo;
- fases históricas;
- auditorias históricas;
- benchmarks;
- documentos antigos de Hero/Header/navegação;
- estudos e decisões intermediárias;
- rascunhos de conversa;
- documentação técnica de Engenharia;
- pricing não formalizado;
- contratos detalhados do Opportunity Boost não requeridos pelo Ads;
- documentos de Journey não requeridos pelo Source Lock Business;
- todo o restante do GKR.

Materiais adicionais só entram quando uma dúvida concreta exigir aprofundamento deliberado.

---

## 10. Regras de integridade da entrega v3

O pacote v3 será íntegro quando:

1. contiver exatamente as 25 fontes canônicas listadas neste manifesto;
2. todos os documentos canônicos forem extraídos do mesmo commit canônico pós-merge;
3. contiver sete `LEIA-PRIMEIRO` operacionais, um por Home;
4. nenhum texto canônico for resumido ou reescrito para caber no pacote;
5. nomes externos não alterarem IDs ou conteúdo interno;
6. cada Source Lock permanecer vinculado à respectiva Home;
7. documentos específicos estiverem fisicamente separados por Home;
8. não houver mistura de documentos históricos como fonte vigente;
9. o pacote deixar claro que outputs generativos começam como `EXPLORAÇÃO`;
10. não existir autorização implícita para Engenharia ou publicação;
11. o arquivo entregue puder ser reproduzido a partir do checkpoint informado;
12. guias operacionais não se apresentarem como autoridade arquitetural;
13. v1 e v2 permanecerem intactas;
14. Ads preservar seu contexto isolado já vigente;
15. Business possuir exatamente `SOURCELOCK + MASTER + CONVERSION-002 + AUTHORITY-001 + GPA-004 + GENINPUT-001`, além do Handoff comum;
16. Business preservar Pontos fora da Home, Journey antes de Incentivos, Intelligence visual, contratação online e modelos de implementação/operação;
17. nenhum mapa, wireframe, direção visual, UI ou protótipo ser fabricado pelo ato de emissão do GKR.

---

## 11. Evolução e reemissão

Se qualquer fonte obrigatória sofrer mudança material depois do snapshot, avaliar se a alteração afeta significado, narrativa, invariantes, contrato complementar, prompt controlado, liberdade de Design ou proibições de inferência.

Se afetar, emitir nova versão do manifesto e novo snapshot.

Não substituir arquivos individualmente dentro de um pacote já distribuído sem registrar nova versão.

Histórico preservado:

- v1: `delivery/design-handoff-v1` @ `8e2a356ca84ba980e588258757800cde2a946f40`;
- v2: `delivery/design-handoff-v2` @ `486f1c5e784be6cf3db9b2fbcbc47da39f9e9016`;
- v3: será materializada em `delivery/design-handoff-v3` somente após integração canônica desta emissão.

---

## 12. Próximo ato após integração

Após merge da autoridade v3:

```text
MAIN CANÔNICA INTEGRADA
↓
MATERIALIZAR delivery/design-handoff-v3
↓
CRIAR 7 LEIA-PRIMEIRO OPERACIONAIS
↓
AUDITAR 25 FONTES CANÔNICAS + 7 GUIAS
↓
GERAR SNAPSHOT / ZIP V3
↓
REGISTRAR ATO FÁTICO PÓS-MERGE NO GKR
```

Esse processo **não executa o Design da Home Business**.

---

## 13. Síntese

A entrega oficial para Design não é o repositório inteiro e não é o Design pronto.

É um snapshot pequeno, reproduzível, separado por Home e semanticamente governado.

Regra final:

> **Entregar cada Home como contexto de trabalho isolado, com contexto suficiente para a designer materializar com liberdade, sem permitir que ferramenta ou layout reconstruam a arquitetura por mistura ou inferência.**

A emissão v3 adiciona Guivos Business sem reabrir as seis Homes da v2.

Estado desta frente antes da materialização factual:

> **EMISSÃO V3 DEFINIDA — 25 FONTES CANÔNICAS + 7 GUIAS OPERACIONAIS — SNAPSHOT/ZIP V3 PENDENTES DE ATO PÓS-MERGE — DESIGN VISUAL NÃO PRODUZIDO PELO GKR.**
