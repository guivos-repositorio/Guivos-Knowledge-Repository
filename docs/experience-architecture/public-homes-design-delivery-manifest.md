---
id: GKR-UX-HOMES-DESIGN-DELIVERY-001
title: Homes Públicas — Manifesto Canônico de Entrega para Design
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-08-13
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
---

# Homes Públicas — Manifesto Canônico de Entrega para Design

## 1. Finalidade

Este manifesto define o **snapshot oficial de documentos a ser entregue à pessoa responsável por Design, UX e UI das cinco Homes públicas já convergidas da Guivos**.

Ele não cria nova arquitetura, não substitui os Documentos Mestres e não duplica suas decisões. Sua função é operacional: fixar **quais arquivos entram no pacote de handoff, em qual checkpoint do GKR, em qual ordem devem ser lidos e quais materiais ficam deliberadamente fora da entrega inicial**.

O pacote aqui governado serve à primeira rodada de:

- compreensão da arquitetura;
- exploração em Figma Make ou ferramenta equivalente;
- arquitetura visual;
- wireframe low-fi desktop;
- wireframe low-fi mobile;
- revisão humana de UX posterior.

Este manifesto não autoriza desenvolvimento, publicação ou promoção automática de qualquer output visual para estado canônico.

---

## 2. Checkpoint congelado

Os documentos da entrega v1 devem ser extraídos do seguinte checkpoint:

```text
repository: guivos-repositorio/Guivos-Knowledge-Repository
commit: 4fee04c4da8d099ac3c415c870391011ceb28e6d
```

Esse commit contém as cinco instâncias específicas de Source Lock e prompt controlado integradas pela PR #263.

A razão de congelar o checkpoint é impedir que um pacote enviado à designer seja silenciosamente alterado por mudanças futuras na `main`.

Regra:

> **Cada entrega é um snapshot reproduzível. Se o GKR evoluir materialmente, uma nova versão do pacote deve ser emitida; arquivos de checkpoints diferentes não devem ser misturados sem reconciliação explícita.**

---

## 3. Composição oficial: 16 documentos únicos

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

---

## 4. Estrutura recomendada do pacote enviado

O snapshot externo deve ser organizado assim:

```text
GUIVOS-HOMES-DESIGN-HANDOFF-v1/
├── 00-LEIA-PRIMEIRO/
│   └── 00-Handoff-Canonico.md
├── 01-HOME-PESSOA/
│   ├── 01-Documento-Mestre.md
│   ├── 02-Reconciliacao-Pos-Media.md
│   └── 03-Source-Lock-Prompt.md
├── 02-HOME-ORGANIZACOES-E-COLETIVOS/
│   ├── 01-Documento-Mestre.md
│   ├── 02-Reconciliacao-Pos-Media.md
│   └── 03-Source-Lock-Prompt.md
├── 03-HOME-MALL/
│   ├── 01-Documento-Mestre.md
│   ├── 02-Reconciliacao-Pos-Media.md
│   └── 03-Source-Lock-Prompt.md
├── 04-HOME-TRAVEL/
│   ├── 01-Documento-Mestre.md
│   ├── 02-Reconciliacao-Pos-Media.md
│   └── 03-Source-Lock-Prompt.md
└── 05-HOME-MEDIA/
    ├── 01-Documento-Mestre.md
    ├── 02-GPA-005-Guivos-Media.md
    └── 03-Source-Lock-Prompt.md
```

Os nomes externos podem ser simplificados para facilitar o uso pela designer, desde que o conteúdo permaneça integral e sem edição semântica.

---

## 5. Formato de entrega

Para o pacote primário, utilizar **Markdown (`.md`)** como formato oficial de transferência.

Motivos:

- preserva títulos, hierarquias, listas, blocos e contratos textuais;
- facilita leitura humana;
- facilita ingestão controlada por ferramentas generativas;
- evita perda semântica causada por extração de texto de PDFs;
- mantém o conteúdo próximo das fontes originais do GKR.

PDF pode ser produzido como material auxiliar para leitura humana, mas **não deve substituir os Markdown como input primário para Figma Make ou ferramenta equivalente**.

---

## 6. Ordem operacional por Home

Antes de gerar qualquer proposta para uma Home, a designer ou ferramenta deve ler apenas:

```text
1. HANDOFF CANÔNICO COMUM
↓
2. DOCUMENTO MESTRE DA HOME
↓
3. CONTRATO COMPLEMENTAR DA HOME
↓
4. SOURCE LOCK + PROMPT ESPECÍFICO
↓
5. EXECUÇÃO GENERATIVA
```

Não carregar simultaneamente os documentos específicos das cinco Homes em uma execução de geração.

A comparação entre Homes pode ocorrer em revisão humana de coerência, não como mistura indiscriminada de contexto durante a geração.

---

## 7. Materiais deliberadamente fora do pacote

Não fazem parte da entrega inicial:

- `GKR-UX-HOMES-GENINPUT-001` — template genérico interno;
- P1–P5 e demais fases históricas;
- auditorias históricas;
- benchmarks;
- documentos antigos de Hero/Header/navegação;
- estudos e decisões intermediárias;
- rascunhos de conversa;
- documentação técnica de Engenharia;
- documentos de produtos não necessários ao Source Lock da Home;
- todo o restante do GKR.

Esses materiais permanecem preservados e podem ser fornecidos sob demanda quando uma dúvida concreta exigir aprofundamento.

---

## 8. Regras de integridade da entrega

O pacote é íntegro quando:

1. contém exatamente os 16 documentos listados neste manifesto;
2. todos foram extraídos do commit congelado;
3. nenhum texto canônico foi resumido ou reescrito para caber no pacote;
4. os nomes externos não alteram IDs ou conteúdo interno;
5. cada Source Lock continua vinculado à sua respectiva Home;
6. não há mistura de documentos históricos como fonte vigente;
7. o pacote deixa claro que outputs generativos começam como `EXPLORAÇÃO`;
8. não há autorização implícita para Engenharia ou publicação;
9. o arquivo entregue pode ser reproduzido a partir do checkpoint informado.

---

## 9. Evolução e reemissão

Se qualquer uma das fontes obrigatórias sofrer mudança material depois deste snapshot, avaliar se a alteração afeta:

- significado;
- narrativa;
- invariantes;
- relação pós-Media;
- prompt controlado;
- liberdade de Design;
- proibições de inferência.

Se afetar, emitir nova versão do manifesto e novo snapshot.

Não substituir arquivos individualmente dentro de um pacote já distribuído sem registrar uma nova versão.

---

## 10. Síntese

A entrega oficial para Design não é o repositório inteiro.

É um snapshot pequeno, reproduzível e semanticamente governado:

```text
1 HANDOFF COMUM
+
5 × (DOCUMENTO MESTRE + COMPLEMENTO + SOURCE LOCK)
=
16 DOCUMENTOS ÚNICOS
```

Regra final:

> **Entregar contexto suficiente para materializar com liberdade, mas não contexto indiscriminado a ponto de permitir que a ferramenta reconstrua a arquitetura por inferência.**

Estado desta frente:

> **PACOTE V1 DEFINIDO — 16 FONTES CONGELADAS NO CHECKPOINT 4fee04c4da8d099ac3c415c870391011ceb28e6d — PRONTO PARA SNAPSHOT EXTERNO E ENTREGA À DESIGNER.**
