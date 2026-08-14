---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 2.0.0
owner: Experience Architecture
last_updated: 2026-08-14
normative: true
depends_on:
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-GENINPUT-001
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
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este manifesto define a **emissão v2 do snapshot oficial de documentos a ser entregue à pessoa responsável por Design, UX e UI das seis Homes públicas já convergidas da Guivos**.

Ele não cria nova arquitetura, não substitui os Documentos Mestres e não duplica suas decisões. Sua função é operacional: fixar **quais fontes canônicas entram no handoff, em qual checkpoint do GKR, como devem ser separadas por Home, em qual ordem devem ser lidas e quais materiais ficam deliberadamente fora da entrega inicial**.

A emissão v1 permanece historicamente íntegra, reproduzível e associada ao checkpoint e à branch já emitidos. A v2 é uma nova emissão e **não altera silenciosamente o snapshot, branch ou ZIP da v1**.

O pacote v2 serve à primeira rodada de:

- compreensão da arquitetura;
- exploração em Figma Make ou ferramenta equivalente;
- arquitetura visual;
- wireframe low-fi desktop;
- wireframe low-fi mobile;
- revisão humana de UX posterior.

Este manifesto não autoriza desenvolvimento, publicação ou promoção automática de qualquer output visual para estado canônico.

---

## 2. Checkpoint da emissão v2

A emissão v2 deve ser materializada **após a integração canônica deste manifesto, do Handoff atualizado e do Source Lock do Ads**.

O checkpoint exato do snapshot externo será registrado no ato pós-merge que criar `delivery/design-handoff-v2`. Até esse momento, a base de elaboração é:

```text
repository: guivos-repositorio/Guivos-Knowledge-Repository
base de elaboração: ee0efc82dc17ec1c83cb34dc87695dbb2783b0c7
```

A branch de entrega v2 não deve ser criada a partir de estado não mesclado. O snapshot externo deve apontar para conteúdo canônico já integrado à `main`.

A razão de congelar o checkpoint é impedir que um pacote enviado à designer seja silenciosamente alterado por mudanças futuras na `main`.

Regra:

> **Cada entrega é um snapshot reproduzível. Se o GKR evoluir materialmente, uma nova versão do pacote deve ser emitida; arquivos de checkpoints diferentes não devem ser misturados sem reconciliação explícita.**

---

## 3. Composição canônica da v2: 19 documentos únicos

### 3.1 Documento comum — leia primeiro

1. `docs/experience-architecture/public-homes-design-handoff.md`
   - ID: `GKR-UX-HOMES-DESIGN-HANDOFF-001`
   - função: governa autorização da fase de Design, ordem de autoridade, liberdade de materialização e controle de ferramentas generativas.

### 3.2 Home Pública — Pessoa

2. `docs/experience-architecture/public-home-master-document.md`
   - ID: `GKR-UX-HOME-MASTER-001`
   - função: autoridade arquitetural da Home Pública — Pessoa.

3. `docs/experience-architecture/public-home-person-media-editorial-supply-reconciliation.md`
   - ID: `GKR-UX-HOME-PERSON-MEDIA-SUPPLY-001`
   - função: reconciliação pós-Media e fronteiras de abastecimento editorial.

4. `docs/experience-architecture/public-home-person-generative-design-source-lock.md`
   - ID: `GKR-UX-HOME-PERSON-GENINPUT-001`
   - função: Source Lock e prompt controlado da primeira exploração de Design.

### 3.3 Home Pública — Organizações e Coletivos

5. `docs/experience-architecture/public-home-organizations-collectives-master-document.md`
   - ID: `GKR-UX-HOME-OC-MASTER-001`
   - função: autoridade arquitetural da Home Pública — Organizações e Coletivos.

6. `docs/experience-architecture/public-home-organizations-collectives-media-editorial-supply-reconciliation.md`
   - ID: `GKR-UX-HOME-OC-MEDIA-SUPPLY-001`
   - função: reconciliação pós-Media e fronteiras editoriais/de confiança.

7. `docs/experience-architecture/public-home-organizations-collectives-generative-design-source-lock.md`
   - ID: `GKR-UX-HOME-OC-GENINPUT-001`
   - função: Source Lock e prompt controlado da primeira exploração de Design.

### 3.4 Home Pública — Guivos Mall

8. `docs/experience-architecture/public-home-mall-master-document.md`
   - ID: `GKR-UX-HOME-MALL-MASTER-001`
   - função: autoridade arquitetural da Home do Guivos Mall.

9. `docs/experience-architecture/public-home-mall-media-editorial-supply-reconciliation.md`
   - ID: `GKR-UX-HOME-MALL-MEDIA-SUPPLY-001`
   - função: reconciliação pós-Media e separação entre conteúdo editorial, recomendação, oferta e publicidade.

10. `docs/experience-architecture/public-home-mall-generative-design-source-lock.md`
    - ID: `GKR-UX-HOME-MALL-GENINPUT-001`
    - função: Source Lock e prompt controlado da primeira exploração de Design.

### 3.5 Home Pública — Guivos Travel

11. `docs/experience-architecture/public-home-travel-master-document.md`
    - ID: `GKR-UX-HOME-TRAVEL-MASTER-001`
    - função: autoridade arquitetural da Home do Guivos Travel.

12. `docs/experience-architecture/public-home-travel-media-editorial-supply-reconciliation.md`
    - ID: `GKR-UX-HOME-TRAVEL-MEDIA-SUPPLY-001`
    - função: reconciliação pós-Media e separação entre autoridade editorial e autoridade operacional do Travel.

13. `docs/experience-architecture/public-home-travel-generative-design-source-lock.md`
    - ID: `GKR-UX-HOME-TRAVEL-GENINPUT-001`
    - função: Source Lock e prompt controlado da primeira exploração de Design.

### 3.6 Home Pública — Guivos Media

14. `docs/experience-architecture/public-home-media-master-document.md`
    - ID: `GKR-UX-HOME-MEDIA-MASTER-001`
    - função: autoridade arquitetural da Home do Guivos Media.

15. `docs/product-architecture/media.md`
    - ID: `GPA-005`
    - função: autoridade complementar do produto Guivos Media, sua arquitetura editorial, propriedades, formatos, distribuição, abastecimento e continuidade.

16. `docs/experience-architecture/public-home-media-generative-design-source-lock.md`
    - ID: `GKR-UX-HOME-MEDIA-GENINPUT-001`
    - função: Source Lock e prompt controlado da primeira exploração de Design.

### 3.7 Home Pública — Guivos Ads

17. `docs/experience-architecture/public-home-ads-master-document.md`
    - ID: `GKR-UX-HOME-ADS-MASTER-001`
    - função: autoridade arquitetural da Home Pública — Guivos Ads.

18. `docs/product-architecture/ads.md`
    - ID: `GPA-007`
    - função: autoridade complementar do produto, relação publicitária, contratos entre superfícies, Opportunity Boost, publicidade contextual e qualificação comercial inteligente.

19. `docs/experience-architecture/public-home-ads-generative-design-source-lock.md`
    - ID: `GKR-UX-HOME-ADS-GENINPUT-001`
    - função: Source Lock e prompt controlado da primeira exploração de Design do Ads.

---

## 4. Decisão operacional: separar a entrega por Home

A entrega externa **não deve apresentar os 19 documentos como um conjunto indiferenciado**.

Embora o snapshot tenha 19 fontes canônicas únicas, o uso operacional deve ser separado em seis contextos independentes de trabalho.

A designer não deve precisar descobrir quais documentos pertencem a cada Home, nem selecionar manualmente fontes a partir de uma pasta única.

Princípio:

> **Uma Home = um contexto de trabalho isolado.**

A única fonte comum às seis Homes é `GKR-UX-HOMES-DESIGN-HANDOFF-001`, mantida em `00-LEIA-PRIMEIRO`.

Cada pasta específica de Home deve conter:

1. um `LEIA-PRIMEIRO` operacional daquela Home;
2. o Documento Mestre;
3. o contrato complementar — reconciliação pós-Media, `GPA-005` no caso do Media ou `GPA-007` no caso do Ads;
4. o Source Lock + Prompt Controlado.

O `LEIA-PRIMEIRO` específico é **arquivo operacional de embalagem**, não documento canônico do GKR e não nova autoridade arquitetural. Sua função é somente indicar a ordem de uso e evitar mistura de contexto.

---

## 5. Estrutura oficial do pacote externo v2

```text
GUIVOS-HOMES-DESIGN-HANDOFF-v2/
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
└── 06-HOME-ADS/
    ├── 00-LEIA-PRIMEIRO-ADS.md
    ├── 01-Documento-Mestre.md
    ├── 02-GPA-007-Guivos-Ads.md
    └── 03-Source-Lock-Prompt.md
```

O pacote externo contém, portanto:

```text
19 FONTES CANÔNICAS CONGELADAS
+
6 GUIAS OPERACIONAIS LEIA-PRIMEIRO
=
25 ARQUIVOS NO SNAPSHOT EXTERNO
```

Os seis guias operacionais não entram na contagem de fontes canônicas e não devem receber IDs normativos do GKR.

---

## 6. Conteúdo mínimo de cada `LEIA-PRIMEIRO` específico

Cada guia operacional deve informar de forma inequívoca:

- qual Home está sendo trabalhada;
- que o Handoff Canônico comum deve ser lido primeiro;
- quais três documentos da pasta formam o contexto específico daquela Home;
- qual é a ordem de leitura;
- qual arquivo contém o prompt que inicia a exploração generativa;
- que documentos das outras Homes não devem ser adicionados à mesma execução;
- que o output inicial é sempre `EXPLORAÇÃO`;
- que a ferramenta não possui autoridade para alterar arquitetura, significado ou decisões canônicas;
- qual é o checkpoint congelado do pacote v2, depois de materializado.

Modelo operacional:

```text
1. 00-Handoff-Canonico-das-Homes.md
↓
2. 01-Documento-Mestre.md
↓
3. 02-Contrato-Complementar.md
↓
4. 03-Source-Lock-Prompt.md
↓
5. EXECUÇÃO NO FIGMA MAKE / FERRAMENTA EQUIVALENTE
↓
6. OUTPUT = EXPLORAÇÃO
```

---

## 7. Regra de carregamento no Figma Make e ferramentas equivalentes

Para trabalhar em uma Home, utilizar **somente quatro fontes canônicas**:

```text
HANDOFF CANÔNICO COMUM
+
DOCUMENTO MESTRE DA HOME
+
CONTRATO COMPLEMENTAR DA HOME
+
SOURCE LOCK + PROMPT DA HOME
```

Não carregar simultaneamente documentos específicos de Pessoa, Organizações e Coletivos, Mall, Travel, Media e Ads na mesma execução generativa.

A comparação entre Homes pode ocorrer em revisão humana de coerência da família Guivos, mas não como mistura indiscriminada de contexto no momento da geração.

A separação física das pastas é uma proteção semântica, não apenas conveniência de organização.

---

## 8. Formato de entrega

Para o pacote primário, utilizar **Markdown (`.md`)** como formato oficial de transferência.

Motivos:

- preserva títulos, hierarquias, listas, blocos e contratos textuais;
- facilita leitura humana;
- facilita ingestão controlada por ferramentas generativas;
- evita perda semântica causada por extração de texto de PDFs;
- mantém o conteúdo próximo das fontes originais do GKR.

PDF pode ser produzido como material auxiliar para leitura humana, mas **não deve substituir os Markdown como input primário para Figma Make ou ferramenta equivalente**.

O pacote externo pode ser distribuído como arquivo `.zip`, desde que sua estrutura interna preserve exatamente a separação por Home definida neste manifesto.

---

## 9. Materiais deliberadamente fora do pacote

Não fazem parte da entrega inicial:

- `GKR-UX-HOMES-GENINPUT-001` — template genérico interno;
- P1–P5 e demais fases históricas;
- auditorias históricas;
- benchmarks;
- documentos antigos de Hero/Header/navegação;
- estudos e decisões intermediárias;
- rascunhos de conversa;
- documentação técnica de Engenharia;
- contratos detalhados do Opportunity Boost não requeridos pelo Source Lock inicial do Ads;
- documentos de produtos não necessários ao Source Lock da Home;
- todo o restante do GKR.

Esses materiais permanecem preservados e podem ser fornecidos sob demanda quando uma dúvida concreta exigir aprofundamento.

---

## 10. Regras de integridade da entrega

O pacote v2 é íntegro quando:

1. contém exatamente as 19 fontes canônicas listadas neste manifesto;
2. todos os documentos canônicos foram extraídos do mesmo commit congelado da emissão v2;
3. contém os seis `LEIA-PRIMEIRO` operacionais, um por Home;
4. nenhum texto canônico foi resumido ou reescrito para caber no pacote;
5. os nomes externos não alteram IDs ou conteúdo interno;
6. cada Source Lock continua vinculado à sua respectiva Home;
7. os documentos específicos estão fisicamente separados por Home;
8. não há mistura de documentos históricos como fonte vigente;
9. o pacote deixa claro que outputs generativos começam como `EXPLORAÇÃO`;
10. não há autorização implícita para Engenharia ou publicação;
11. o arquivo entregue pode ser reproduzido a partir do checkpoint informado;
12. os seis guias operacionais não se apresentam como autoridade arquitetural ou documento canônico;
13. a emissão v1 permanece intacta e não é silenciosamente substituída;
14. a Home Ads possui contexto isolado com `GKR-UX-HOME-ADS-MASTER-001 + GPA-007 + GKR-UX-HOME-ADS-GENINPUT-001`.

---

## 11. Evolução e reemissão

Se qualquer uma das fontes obrigatórias sofrer mudança material depois deste snapshot, avaliar se a alteração afeta:

- significado;
- narrativa;
- invariantes;
- relação pós-Media ou contrato complementar vigente;
- prompt controlado;
- liberdade de Design;
- proibições de inferência.

Se afetar, emitir nova versão do manifesto e novo snapshot.

Não substituir arquivos individualmente dentro de um pacote já distribuído sem registrar uma nova versão.

A emissão v2 deverá possuir:

- branch exclusiva `delivery/design-handoff-v2`;
- snapshot próprio;
- ZIP próprio;
- checkpoint canônico explícito;
- seis Homes;
- nenhuma mutação retroativa da v1.

A criação da branch e do snapshot v2 ocorre **somente após merge desta evolução documental**.

---

## 12. Síntese

A entrega oficial para Design não é o repositório inteiro e não é uma pasta única com 19 documentos misturados.

É um snapshot pequeno, reproduzível, separado por Home e semanticamente governado:

```text
1 HANDOFF COMUM
+
6 × (LEIA-PRIMEIRO OPERACIONAL + DOCUMENTO MESTRE + COMPLEMENTO + SOURCE LOCK)
=
19 FONTES CANÔNICAS + 6 GUIAS OPERACIONAIS
```

Regra final:

> **Entregar cada Home como um contexto de trabalho isolado, com contexto suficiente para materializar com liberdade, mas sem permitir que a ferramenta reconstrua a arquitetura por mistura ou inferência.**

A emissão v2 adiciona Guivos Ads sem reabrir ou adulterar a entrega v1.

Estado desta frente:

> **PACOTE V2 DEFINIDO DOCUMENTALMENTE — 19 FONTES CANÔNICAS + 6 GUIAS OPERACIONAIS — MATERIALIZAÇÃO DA BRANCH/SNAPSHOT EXTERNO PENDENTE DO MERGE CANÔNICO DESTA EMISSÃO.**