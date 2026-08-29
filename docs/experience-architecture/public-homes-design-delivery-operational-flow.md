---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 1.4.0
owner: Experience Architecture
last_updated: 2026-08-29
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-STATE-001
  - GKR-FULL-CORPUS-AUDIT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
normative: false
maturity: historical_operational_flow_preserved_execution_suspended_during_full_corpus_audit
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 0. Gate vigente durante a Auditoria Integral do GKR

Este documento preserva o **fluxo operacional histórico** utilizado para consumir os pacotes externos de Design.

No estado atual, o fluxo está **dormente e não executável como autorização**.

```text
FLUXO / MÉTODO
→ PRESERVADO

DOWNLOAD / SOURCE LOCK / PROMPT / FIGMA MAKE / EXPLORAÇÃO
→ NÃO AUTORIZADOS COMO NOVA EXECUÇÃO DURANTE A AUDITORIA

V1–V4
→ SNAPSHOTS HISTÓRICOS PRESERVADOS
```

As instruções abaixo continuam úteis como método de uma futura retomada, mas somente poderão voltar a ser executadas após ato humano explícito, reconciliação pós-auditoria do Handoff/Manifest/Flow e emissão ou revalidação de um pacote compatível com o checkpoint então vigente.

```text
FLUXO DOCUMENTADO
≠ FLUXO LIBERADO

PACOTE EXISTENTE
≠ PACOTE ATUALMENTE AUTORIZADO
```

---

## 1. Finalidade

Este guia registra como a pessoa responsável por Design, UX e UI deve iniciar o trabalho após receber o pacote externo vigente das **oito Homes públicas da Guivos**.

Ele é subordinado a `GKR-UX-HOMES-DESIGN-DELIVERY-001` e `GKR-UX-HOMES-DESIGN-HANDOFF-001`.

Este documento:

- não cria nova arquitetura;
- não substitui o Manifesto Canônico de Entrega;
- não substitui o Handoff Canônico;
- não altera Documentos Mestres, Source Locks, Handoffs específicos ou GENINPUTs;
- não produz mapa, wireframe, direção visual, UI ou protótipo;
- não autoriza implementação ou publicação.

A versão `1.3.0` amplia o fluxo operacional para Guivos Intelligence e registra o gate necessário entre a preparação do Manifesto v4 e a futura entrega para Design.

---

## 2. Gate anterior ao recebimento do pacote v4

O Manifesto `v4.0.0` preparado no GKR não equivale a pacote entregue.

Antes de Design receber v4, a frente canônica deve:

```text
MERGE DA PREPARAÇÃO EM MAIN
↓
CAPTURAR SHA EXATO PÓS-MERGE
↓
VALIDAR 31/31 FONTES DO MANIFESTO
↓
MATERIALIZAR delivery/design-handoff-v4
↓
CRIAR 8 LEIA-PRIMEIRO
↓
GERAR SNAPSHOT / ZIP V4
↓
VALIDAR REPRODUTIBILIDADE E ISOLAMENTO
↓
REGISTRAR CHECKPOINT DA EMISSÃO
↓
PACOTE DISPONÍVEL PARA DESIGN
```

Enquanto esse gate não estiver concluído:

> **SNAPSHOT V4 NÃO EMITIDO — DESIGN V4 NÃO INICIADO POR ESTA PREPARAÇÃO.**

Nota histórica: a emissão v4 foi posteriormente materializada e registrada em seu próprio snapshot record. Isso não altera a suspensão operacional vigente durante a auditoria integral.

---

## 3. Fluxo obrigatório após recebimento do pacote

```text
BAIXAR O ZIP DA EMISSÃO VIGENTE
      ↓
abrir 00-LEIA-PRIMEIRO
      ↓
escolher UMA Home
      ↓
abrir o LEIA-PRIMEIRO daquela Home
      ↓
seguir somente os documentos indicados
      ↓
usar o Source Lock + Prompt / GENINPUT da Home
      ↓
OUTPUT EXTERNO = EXPLORAÇÃO
```

A sequência significa:

1. baixar o ZIP oficial da emissão vigente;
2. ler o Handoff Canônico comum;
3. escolher somente uma Home: Pessoa, Organizações e Coletivos, Mall, Travel, Media, Ads, Business ou Intelligence;
4. abrir o `LEIA-PRIMEIRO` daquela Home;
5. carregar somente as fontes específicas indicadas naquele contexto;
6. utilizar o Source Lock + Prompt Controlado / GENINPUT em Figma Make ou ferramenta equivalente;
7. tratar toda saída como `EXPLORAÇÃO` até validação humana.

---

## 4. Regra de isolamento de contexto

> **Uma Home = uma execução semanticamente isolada.**

Não carregar simultaneamente documentos específicos das oito Homes.

As seis Homes originalmente presentes antes de Business preservam seus fluxos de contexto mínimo vigentes.

Business utiliza contexto específico maior porque suas fronteiras são distribuídas por Source Lock, Documento Mestre, Conversão, Contratos de Autoridade e `GPA-004`.

Intelligence utiliza contexto específico próprio para preservar produto, Home, explicabilidade, autonomia, privacidade e limites de inferência sem transformar tecnologia em produto.

---

## 5. Regra específica para Guivos Ads

Para Ads, permanece:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-ADS-MASTER-001
+
GPA-007
+
GKR-UX-HOME-ADS-GENINPUT-001
```

Não carregar automaticamente contratos detalhados do Opportunity Boost, pricing ou documentação operacional de outros produtos.

---

## 6. Regra específica para Guivos Business

Para Business, permanece:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-BUSINESS-SOURCELOCK-001
+
GKR-UX-HOME-BUSINESS-MASTER-001
+
GKR-UX-HOME-BUSINESS-CONVERSION-002
+
GKR-UX-HOME-BUSINESS-AUTHORITY-001
+
GPA-004
+
GKR-UX-HOME-BUSINESS-GENINPUT-001
```

Não carregar automaticamente outras Homes, conversão v1, documentos históricos, pricing ainda não formalizado, Ads, benchmarks ou documentos adicionais de Journey sem dúvida concreta.

---

## 7. Regra específica para Guivos Intelligence

Para Intelligence, utilizar:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-INTELLIGENCE-GENINPUT-001
+
GKR-UX-HOME-INTELLIGENCE-HANDOFF-001
+
GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
+
GKR-UX-HOME-INTELLIGENCE-MASTER-001
+
GKR-INTELLIGENCE-PRODUCT-SOURCELOCK-001
+
GPA-006
```

O contrato narrativo e o princípio transversal de outcome continuam autoridades, mas o GENINPUT já estabelece que não precisam ser adicionados como documentos extras quando sua função estiver preservada no pacote direto.

Não carregar automaticamente:

- Neo4j;
- GraphRAG;
- Power BI;
- Guivos.ai;
- documentação técnica de IA/LLM;
- documentos detalhados de Journey ou Business;
- benchmarks;
- rascunhos históricos.

Se uma dúvida concreta exigir material adicional, registrar deliberadamente a fonte e sua função.

### 7.1 Invariantes de leitura

```text
INFORMAÇÃO ≠ COMPREENSÃO
COMPREENDER ≠ DECIDIR
M03 ≠ M10
M04 ≠ M05
RELAÇÃO ≠ CAUSA
SINAL ≠ CERTEZA
PERCEBER ANTES ≠ PREVER O FUTURO
TECNOLOGIA ≠ PRODUTO
```

A designer deve preservar os 11 movimentos funcionalmente, sem obrigação de convertê-los em 11 seções físicas.

M08 precisa tornar explicabilidade visível; M09 preserva autoridade de decisão; M11 não pode ser materializado como previsão determinista.

---

## 8. Estado do resultado gerado

Todo resultado inicial produzido pela frente de Design, Figma Make ou ferramenta equivalente começa obrigatoriamente como:

> **EXPLORAÇÃO — NÃO CANÔNICA — NÃO APROVADA PARA IMPLEMENTAÇÃO.**

Fluxo de promoção:

```text
EXPLORAÇÃO
↓
CANDIDATO
↓
VALIDADO EM UX
↓
VALIDADO EM UI
↓
APROVADO PARA HANDOFF DE ENGENHARIA
```

A ferramenta generativa não possui autoridade para promover seu próprio output.

---

## 9. Relação entre v1, v2, v3 e v4

- v1 permanece snapshot histórico de sua emissão original;
- v2 permanece preservada;
- v3 permanece separada em `delivery/design-handoff-v3`;
- v4 possui snapshot histórico próprio registrado e deve ser preservada sem reescrita.

Não misturar arquivos entre emissões sem reconciliação explícita.

Nenhuma dessas emissões funciona como autorização atual para nova execução durante a auditoria integral.

---

## 10. Regra final

> **Baixe a emissão correta, leia a orientação comum, escolha uma Home, mantenha o contexto isolado e só então use o Source Lock + Prompt/GENINPUT como entrada da exploração externa.**

O GKR governa o significado. Design governa a materialização. Ferramentas generativas ampliam a exploração; não decidem a arquitetura da Guivos.

### Estado vigente

A regra acima permanece o método de consumo quando a frente for reativada.

```text
AGORA
→ FLUXO DORMENTE
→ NENHUMA NOVA EXECUÇÃO AUTORIZADA
```
