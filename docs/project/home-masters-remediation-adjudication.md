---
id: GKR-HOME-MASTERS-REMEDIATION-001
title: Home Masters — Adjudicação de Remediação
status: active
version: 1.3.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-09-13
normative: true
maturity: closure_remediation_adjudication
related:
  - GKR-CHECKPOINT-HOME-MASTERS-PRIORITY-001
  - GKR-UX-SPECIALIZED-HOMES-RECONCILIATION-001
  - GKR-STATE-001
---

# Home Masters — Adjudicação de Remediação

## 1. Escopo

Este documento resolve somente lacunas de inventário, handoff e continuidade temporal identificadas na auditoria C1–C10. Não é Home Master, Product Master, Source Lock, Design ou implementação.

```text
HOME MASTER
→ CANONICAL SEMANTIC / FUNCTIONAL INPUT

HANDOFF AUTHORITY
≠ DESIGN RELEASE
≠ UI APPROVAL
≠ PROTOTYPE AUTHORIZATION
≠ IMPLEMENTATION RELEASE
```

Regra transversal de não invenção:

```text
TBD
→ REMAINS TBD

NOT DEFINED
→ REMAINS NOT DEFINED

NOT AUTHORIZED
→ REMAINS NOT AUTHORIZED

HISTORICAL MATURITY SIGNAL
→ DOES NOT BECOME CURRENT EXECUTION STATE BY INFERENCE
```

## 2. Inventário canônico da frente

A auditoria repo-wide reconhece exatamente oito Homes com Documento Mestre próprio. A tabela separa metadado físico do Master e maturidade governada corrente.

| Home | ID mestre | Path | Versão | Status físico | Maturidade governada corrente |
|---|---|---|---|---|---|
| Home Pública Principal / Pessoa | `GKR-UX-HOME-MASTER-001` | `docs/experience-architecture/public-home-master-document.md` | `1.0.2` | `active` | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |
| Home Pública — Organizações e Coletivos | `GKR-UX-HOME-OC-MASTER-001` | `docs/experience-architecture/public-home-organizations-collectives-master-document.md` | `1.0.0` | `active` | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |
| Guivos Mall | `GKR-UX-HOME-MALL-MASTER-001` | `docs/experience-architecture/public-home-mall-master-document.md` | `1.0.0` | `draft` | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |
| Guivos Travel | `GKR-UX-HOME-TRAVEL-MASTER-001` | `docs/experience-architecture/public-home-travel-master-document.md` | `1.0.0` | `draft` | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |
| Guivos Media | `GKR-UX-HOME-MEDIA-MASTER-001` | `docs/experience-architecture/public-home-media-master-document.md` | `1.0.0` | `draft` | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |
| Guivos Business | `GKR-UX-HOME-BUSINESS-MASTER-001` | `docs/experience-architecture/public-home-business-master-document.md` | `1.0.0` | `active` | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |
| Guivos Ads | `GKR-UX-HOME-ADS-MASTER-001` | `docs/experience-architecture/public-home-ads-master-document.md` | `1.0.0` | `draft` | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |
| Guivos Intelligence | `GKR-UX-HOME-INTELLIGENCE-MASTER-001` | `docs/experience-architecture/public-home-intelligence-master-document.md` | `0.1.1` | `draft` | `DOCUMENTALLY_RECONCILED_PRE_MATERIALIZATION` |

A maturidade governada corrente das oito Homes acima é estabelecida por `GKR-STATE-001`. Metadados históricos mais específicos nos Masters permanecem como proveniência e não substituem o estado corrente. Em particular:

- Pessoa mantém `maturity: reconciled_architecture_pre_materialization` no frontmatter do Master;
- O/C mantém `maturity: documentally_rebuilt_pre_materialization_under_full_corpus_audit` no frontmatter do Master;
- os `status: draft` de Mall, Travel, Media e Ads permanecem sinais históricos de maturidade conforme `GKR-UX-SPECIALIZED-HOMES-RECONCILIATION-001`;
- Intelligence mantém Master `v0.1.1` e Home Source Lock `v1.0.0` ativo/normativo.

Limites do inventário:

```text
JOURNEY
→ EXPERIENCE LAYER
→ NOT A NINTH HOME

COMMUNITY
→ NO CURRENT DISTINCT HOME AUTHORITY PROVEN
→ NO MASTER CREATED BY INFERENCE

PUBLIC O/C HOME
≠ AUTHENTICATED O/C EXPERIENCE

PRODUCT MASTER
≠ HOME MASTER
```

A individualização dos oito Masters no `mkdocs.yml` já está comprovada e não exige alteração nesta remediação.

## 3. Guivos Mall — contrato determinístico de handoff

`GKR-UX-HOME-MALL-MASTER-001` permanece a autoridade narrativa e funcional principal da Home Mall. Este contrato não cria layout ou implementação; apenas torna explícitas as regras necessárias para consumo determinístico do Master.

### 3.1 Estados semânticos obrigatórios

```text
MALL-HS-01 — BASELINE_PUBLIC
→ tese, pergunta-mãe, identidade Guivos e arquitetura de descoberta permanecem válidas independentemente de campanhas ou dados comerciais dinâmicos

MALL-HS-02 — COMMERCIAL_DATA_AVAILABLE
→ produto, oferta, preço, preço em pontos, marca ou parceiro só podem aparecer quando sustentados por fonte/autoridade aplicável

MALL-HS-03 — COMMERCIAL_DATA_UNAVAILABLE_OR_ERROR
→ ausência, erro ou indisponibilidade não podem ser convertidos em oferta, estoque, preço, elegibilidade ou parceria fictícios
→ tratamento visual/copy de fallback permanece TBD para Design/implementação

MALL-HS-04 — CAMPAIGN_ACTIVE
→ campanha pode alterar camada comercial temporária
→ não redefine pergunta-mãe nem transforma promoção em identidade permanente

MALL-HS-05 — PERSONALIZATION_AUTHORIZED
→ “recomendado para você” exige base legítima, finalidade e regras aplicáveis
→ sem essa base, usar descoberta/curadoria geral sem alegar personalização

MALL-HS-06 — SPONSORED_EXPOSURE
→ exposição paga permanece identificada
→ não assume aparência de recomendação orgânica
```

### 3.2 Comportamentos e interações

1. `Shopping` e `Gift Cards` permanecem portas distintas e atuais do Mall.
2. Busca direta permanece conceitualmente disponível para quem já sabe o que procura; sua implementação não é definida aqui.
3. Produto/oferta exibido pode iniciar outra experiência, mas detalhe, Perfil, Carrinho, Checkout, pedido e pós-compra começam fora da Home.
4. Saldo global da Pessoa pertence ao contexto de conta/Perfil; preço em pontos pertence à oferta elegível.
5. `Programa de Pontos` e `Gift Card Guivos` permanecem distintos.
6. Recomendação, destaque, oferta e patrocínio não podem ser fundidos.
7. Campanha comercial não elimina a camada permanente de significado e confiança.

### 3.3 Navegação governada

```text
GUIVOS
→ retorno à Home principal

MALL
→ identificação da especialidade atual

SHOPPING
→ universo comercial de produtos

GIFT CARDS
→ universo de vouchers, serviços, experiências e presentes

BUSCAR
→ acesso estrutural à descoberta direta

PERFIL / CARRINHO
→ acessos globais admitidos no Header
→ comportamento interno fora do escopo deste Master
```

A existência conceitual desses acessos não prova rota, URL, componente, disponibilidade técnica ou comportamento implementado.

### 3.4 Contrato para AI e desenvolvimento futuro

É proibido inferir ou fabricar:

- catálogo, estoque, preço, desconto, disponibilidade ou elegibilidade;
- parceiro institucional a partir da mera presença de marca/oferta;
- pagamento híbrido, taxa de conversão ou regra econômica não autorizada;
- mecânica de Perfil, Carrinho, Checkout ou página de produto;
- recomendação personalizada sem base, finalidade e autoridade aplicáveis;
- escala, liderança, segurança ou melhor preço sem evidência;
- decisão visual final a partir deste contrato.

### 3.5 Critérios objetivos de aceite — Mall

Um artefato derivado é semanticamente aceitável somente se:

1. preserva a pergunta-mãe e a progressão em onze movimentos sem obrigar onze seções visuais;
2. mantém `Mall = capacidade da Guivos`, não marca/ecossistema independente;
3. permite descoberta e acesso direto sem percurso narrativo obrigatório;
4. preserva `Home ≠ páginas internas`;
5. separa destaque, recomendação, oferta e patrocínio;
6. exibe dados comerciais somente quando sustentados;
7. não cria regra econômica ou estado operacional inexistente;
8. preserva autonomia da Pessoa e ausência de manipulação como regra;
9. mantém `MALL-HS-01..06` semanticamente distinguíveis;
10. não trata handoff como autorização de Design, UI, protótipo ou implementação.

## 4. Guivos Travel — contrato determinístico de handoff

`GKR-UX-HOME-TRAVEL-MASTER-001` permanece a autoridade narrativa e funcional principal da Home Travel. Este contrato complementa o Master sem congelar UI ou implementação.

### 4.1 Estados semânticos obrigatórios

```text
TRAVEL-HS-01 — BASELINE_PUBLIC
→ pergunta-mãe, identidade Guivos, inspiração e acesso aos serviços permanecem a base permanente da Home

TRAVEL-HS-02 — OPERATIONAL_SERVICE
→ os nove serviços registrados no Master/GPA-003 podem ser apresentados como operação existente
→ isso não implica disponibilidade de toda oferta, data, tarifa ou destino

TRAVEL-HS-03 — DESTINATION_OR_EXPERIENCE_PROVEN
→ destino, imagem, experiência ou contexto apresentado como real deve possuir lastro real
→ imagem inspiracional não simula disponibilidade operacional

TRAVEL-HS-04 — OFFER_DATA_AVAILABLE
→ preço, pontos, condição ou disponibilidade específica só aparecem quando sustentados pela oferta aplicável

TRAVEL-HS-05 — OFFER_DATA_UNAVAILABLE_OR_ERROR
→ ausência, erro ou indisponibilidade não se convertem em tarifa, vaga, disponibilidade, parceiro ou condição fictícios
→ tratamento visual/copy de fallback permanece TBD para Design/implementação

TRAVEL-HS-06 — CAMPAIGN_OR_SPONSORED
→ campanha é camada temporária e patrocínio permanece identificado
→ nenhuma dessas condições compra relevância orgânica nem redefine o Hero permanente
```

### 4.2 Comportamentos e interações

1. A Pessoa pode começar por descoberta/inspiração ou por acesso direto a serviço.
2. A narrativa não pode obrigar quem sabe o que procura a percorrer todos os movimentos antes de avançar.
3. `Serviços`, `Destinos` e `Experiências` permanecem territórios conceituais distintos.
4. Os nove serviços podem ser organizados pela lógica da viagem sem se tornarem nove produtos desconectados.
5. Relacionar serviços a uma mesma viagem não cria contratação conjunta obrigatória.
6. Destino e experiência permanecem conceitos diferentes.
7. Preço monetário e preço em pontos só aparecem quando elegíveis; saldo global pertence ao contexto de conta/Perfil.
8. Resultado de busca, detalhe, reserva, passageiro, pagamento, voucher, checkout e pós-venda começam fora da Home.

### 4.3 Navegação governada

```text
GUIVOS
→ retorno à Home principal

TRAVEL
→ identificação da especialidade atual

SERVIÇOS
→ acesso às capacidades operacionais registradas

DESTINOS
→ descoberta de lugares reais

EXPERIÊNCIAS
→ descoberta do que pode ser vivido no destino

BUSCAR
→ acesso direto quando aplicável

PERFIL
→ acesso global
→ comportamento interno fora do escopo da Home
```

Os CTAs finais do Master expressam destinos semânticos; não congelam rota, URL ou componente.

### 4.4 Contrato para AI e desenvolvimento futuro

É proibido inferir ou fabricar:

- destino, imagem, experiência, fornecedor ou parceiro inexistente;
- tarifa, disponibilidade, elegibilidade, data, inventário ou condição comercial sem fonte aplicável;
- cobertura mundial, liderança ou escala sem evidência;
- pagamento híbrido, taxa de conversão ou regra econômica não autorizada;
- reserva, checkout, emissão, cancelamento, reembolso, voucher ou pós-venda não definidos;
- recomendação/personalização sem base, finalidade e autoridade aplicáveis;
- obrigação de bundle entre serviços;
- causalidade ou promessa de transformação por viajar.

### 4.5 Critérios objetivos de aceite — Travel

Um artefato derivado é semanticamente aceitável somente se:

1. preserva a pergunta-mãe e a arquitetura em onze movimentos sem impor onze seções visuais;
2. mantém inspiração e operação real simultaneamente legíveis;
3. permite acesso direto aos serviços sem percurso narrativo obrigatório;
4. preserva os nove serviços operacionais sem inventar um décimo serviço;
5. distingue destino, experiência, oferta e conteúdo editorial;
6. usa somente destinos, imagens, experiências, ofertas e condições sustentados;
7. mantém páginas internas e fluxos de reserva fora do escopo da Home;
8. não obriga contratação conjunta de serviços relacionados;
9. mantém `TRAVEL-HS-01..06` semanticamente distinguíveis;
10. não trata handoff como autorização de Design, UI, protótipo ou implementação.

## 5. Business

A frase histórica de `GKR-UX-HOME-BUSINESS-MASTER-001` segundo a qual o Master não é handoff para Design é normalizada para:

```text
BUSINESS MASTER
→ CANONICAL DOCUMENTARY HANDOFF INPUT

HANDOFF
≠ DESIGN AUTHORIZATION
```

A indicação histórica de `SOURCE LOCK → PRÓXIMA ETAPA` não cria gate automático atual. Qualquer Source Lock permanece autoridade separada e depende de ato governado próprio.

A referência histórica de que a Home do Guivos Intelligence ainda não precisava existir foi superada: a Home Intelligence possui Master próprio e Home Source Lock vigente. Business não absorve essa autoridade.

## 6. Intelligence

A afirmação histórica de `GKR-UX-HOME-INTELLIGENCE-MASTER-001` de que o Home Source Lock ainda não havia sido criado está superada.

```text
GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001 v1.0.0
→ ACTIVE / NORMATIVE

MASTER
→ NARRATIVE / SEMANTIC / FUNCTIONAL AUTHORITY

HOME SOURCE LOCK
→ SOURCE PACKAGE / INVARIANT FREEZE WITHIN ITS SCOPE

MASTER
≠ SOURCE LOCK

MASTER + SOURCE LOCK
≠ DESIGN RELEASE
≠ IMPLEMENTATION RELEASE
```

`COMPREENDER ≠ DECIDIR` permanece obrigatório.

## 7. Demais Homes

Nenhuma remediação estrutural adicional é necessária para Pessoa, O/C, Media ou Ads. Snapshots temporais não substituem `GKR-STATE-001` como fonte do estado executivo corrente.

Media e Ads já possuem linguagem suficiente de handoff, aceite e limites. Pessoa e O/C permanecem sem gap arquitetural provado.

## 8. Estado C1–C10 no HEAD de elegibilidade

A remediação documental foi integralmente revalidada no HEAD `39277f305fced32ce351c113ab7e7d5d7cc76242`.

```text
C1 — REPO-WIDE INVENTORY
→ PASS

C2 — MASTER / ID / PATH / VERSION / STATUS / MATURITY
→ PASS
→ GOVERNED MATURITY ALIGNED TO GKR-STATE-001 FOR ALL 8 HOMES

C3 — PUBLIC × AUTHENTICATED × OTHER SURFACES
→ PASS

C4 — INDIVIDUALIZATION IN MENU
→ PASS

C5 — HANDOFF SUFFICIENCY
→ PASS
→ MALL + TRAVEL CONTRACTS EXPLICITLY SUPPLIED
→ REMEDIATION DISCOVERABLE VIA MKDOCS NAVIGATION

C6 — NEW MASTER ONLY IF PROVEN
→ PASS

C7 — AUTHORITY PRECEDENCE
→ PASS

C8 — SEMANTIC + MECHANICAL ON EXACT ELIGIBILITY HEAD
→ PASS
→ SEMANTIC #991 = SUCCESS
→ MECHANICAL #1236 = SUCCESS

C9 — INDEPENDENT GOVERNED REVIEW ON EXACT ELIGIBILITY HEAD
→ PASS
→ CODEX = DIDN'T FIND ANY MAJOR ISSUES
→ REVIEWED COMMIT = 39277f305f
→ OPEN REVIEW THREADS = 0

C10 — ZERO IMPLEMENTATION INFERENCE
→ PASS
```

Esta adjudicação prevalece somente para o inventário de fechamento, o significado de handoff, os contratos complementares de Mall/Travel e os estados temporais explicitamente normalizados acima. Ela não substitui a arquitetura semântica dos Masters.

## 9. Histórico de revisão e remediação

Base física no início desta remediação:

```text
MAIN
→ 830b3f204a9e8e74aa65f73fb1fc68f5f228fade
```

A PR #365 permanece frente independente em HOLD. No início desta remediação, seu HEAD continuava `3a946a2c2ae840d6ac6f5dba91242479d46db2e5`, divergindo do `main` acima com `ahead_by = 29` e `behind_by = 61`.

```text
REVIEW 1 @ 7eb25a694795d469371865289357de42cf958845
→ P1 C2 — INVENTORY MISSING VERSION / STATUS / MATURITY
→ P1 C5 — MALL / TRAVEL CONTRACTS INSUFFICIENT
→ REMEDIATED

REVIEW 2 @ b51e7e1bb21383d1933553f8953e5532a474fcff
→ C5 FINDING CLEARED
→ P1 C2 — PESSOA / O-C GOVERNED MATURITY NOT ALIGNED TO GKR-STATE-001
→ REMEDIATED @ 3d4357c12d9d3fea7ae69b84efe13769ca2902b1

REVIEW 3 @ 3d4357c12d9d3fea7ae69b84efe13769ca2902b1
→ P1 C5 — REMEDIATION CONTRACT NOT DISCOVERABLE FROM CANONICAL NAVIGATION
→ ACCEPTED
→ REMEDIATED BY MKDOCS NAVIGATION EXPOSURE
→ NEW HEAD 39277f305fced32ce351c113ab7e7d5d7cc76242

REVIEW 4 @ 39277f305fced32ce351c113ab7e7d5d7cc76242
→ DIDN'T FIND ANY MAJOR ISSUES
→ C9 PASS
```

## 10. Formal closure changeset × integração em `main`

O HEAD `39277f...` comprova a elegibilidade de fechamento. Alterações documentais posteriores que formalizam esse fechamento criam novo HEAD e, por isso, **não herdam automaticamente C8/C9**.

```text
ELIGIBILITY HEAD 39277f...
→ C1–C10 PASS

FORMAL CLOSURE CHANGESET
→ IN PROGRESS IN PR #377

PR #377 MERGED
→ NO

CURRENT MAIN
→ HOME MASTERS NOT YET INTEGRATED

AFTER GOVERNED MERGE OF A CLEAN FINAL CLOSURE HEAD
→ HOME MASTERS FRONT = CONCLUDED / GOVERNED / INTEGRATED
```

Antes de qualquer merge do changeset final de fechamento, o HEAD final deve repetir:

```text
SEMANTIC VALIDATION ON EXACT FINAL CLOSURE HEAD
→ REQUIRED

MECHANICAL VALIDATION ON EXACT FINAL CLOSURE HEAD
→ REQUIRED

INDEPENDENT GOVERNED REVIEW ON EXACT FINAL CLOSURE HEAD
→ REQUIRED
```

Até que esses três gates estejam limpos no mesmo HEAD:

```text
PR #365
→ REMAINS OPEN / DRAFT / NOT MERGED / HOLD

O/C STATE MAP
→ NOT RELEASED

O/C PRIORITY FLOWS
→ NOT RELEASED

O/C NAVIGATION MATERIALIZATION
→ NOT RELEASED

O/C AUTHENTICATED WIREFRAMES
→ NOT RELEASED

DESIGN / UI / PROTOTYPE
→ NOT RELEASED

PRODUCT ENGINEERING
→ PAUSED BEFORE W0-01 / NOT RELEASED
```

Após eventual merge governado da PR #377, o primeiro ato é reconfirmar o `main` real e somente então reconciliar a PR #365, sem rebase ou merge cego.