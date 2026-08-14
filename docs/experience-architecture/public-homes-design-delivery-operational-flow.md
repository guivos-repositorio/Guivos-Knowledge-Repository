---
id: GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
title: Homes Públicas — Fluxo Operacional de Uso do Pacote de Design
status: active
version: 1.1.0
owner: Experience Architecture
last_updated: 2026-08-14
parent: GKR-UX-HOMES-DESIGN-DELIVERY-001
depends_on:
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
normative: false
---

# Homes Públicas — Fluxo Operacional de Uso do Pacote de Design

## 1. Finalidade

Este guia registra, de forma curta e inequívoca, **como a pessoa responsável por Design, UX e UI deve iniciar o trabalho após receber o pacote externo vigente das seis Homes públicas da Guivos**.

Ele é um artefato operacional subordinado a `GKR-UX-HOMES-DESIGN-DELIVERY-001` e `GKR-UX-HOMES-DESIGN-HANDOFF-001`.

Este documento:

- não cria nova arquitetura;
- não substitui o Manifesto Canônico de Entrega;
- não substitui o Handoff Canônico;
- não altera os Documentos Mestres;
- não altera os Source Locks;
- não autoriza implementação ou publicação.

---

## 2. Fluxo obrigatório após o recebimento do pacote

```text
BAIXAR O ZIP DA EMISSÃO VIGENTE
      ↓
abrir 00-LEIA-PRIMEIRO
      ↓
escolher UMA Home
      ↓
abrir o LEIA-PRIMEIRO daquela Home
      ↓
seguir os 3 documentos indicados
      ↓
usar o Source Lock + Prompt no Figma Make
```

A sequência deve ser interpretada da seguinte forma:

1. **Baixar o ZIP** oficial da emissão de Design vigente.
2. **Abrir `00-LEIA-PRIMEIRO`** e ler o Handoff Canônico comum antes de trabalhar uma Home específica.
3. **Escolher uma única Home** para a execução em andamento: Pessoa, Organizações e Coletivos, Mall, Travel, Media ou Ads.
4. **Abrir o `LEIA-PRIMEIRO` daquela Home**, que identifica o contexto específico e a ordem de uso.
5. **Seguir os três documentos indicados na pasta da Home**:
   - Documento Mestre;
   - contrato complementar — Reconciliação pós-Media, `GPA-005` no caso de Media ou `GPA-007` no caso de Ads;
   - Source Lock + Prompt Controlado.
6. **Usar o Source Lock + Prompt no Figma Make ou ferramenta generativa equivalente**, mantendo como contexto somente as fontes autorizadas para aquela Home.

---

## 3. Regra de isolamento de contexto

> **Uma Home = uma execução semanticamente isolada.**

Não carregar simultaneamente no Figma Make os documentos específicos das seis Homes.

Para uma execução de uma Home, o contexto autorizado é:

```text
HANDOFF CANÔNICO COMUM
+
DOCUMENTO MESTRE DA HOME
+
CONTRATO COMPLEMENTAR DA HOME
+
SOURCE LOCK + PROMPT DA HOME
```

Documentos de outras Homes não devem ser adicionados à mesma execução apenas para aumentar contexto.

---

## 4. Regra específica para Guivos Ads

Para a Home Ads, utilizar:

```text
GKR-UX-HOMES-DESIGN-HANDOFF-001
+
GKR-UX-HOME-ADS-MASTER-001
+
GPA-007
+
GKR-UX-HOME-ADS-GENINPUT-001
```

Não carregar automaticamente contratos detalhados do Opportunity Boost, pricing ou documentação operacional de outros produtos. Se uma dúvida específica exigir aprofundamento, ampliar o contexto de forma deliberada e registrar a fonte adicional.

A referência externa a iFood Ads ou outros benchmarks não faz parte do Source Lock canônico e não deve ser tratada como template.

---

## 5. Estado do resultado gerado

Todo resultado inicial produzido pelo Figma Make ou ferramenta equivalente começa obrigatoriamente como:

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

## 6. Relação entre v1 e v2

A emissão v1 permanece um snapshot histórico íntegro das cinco Homes originalmente entregues.

A emissão v2 adiciona Guivos Ads e deve ser distribuída por branch/snapshot/ZIP próprios. Não misturar arquivos da v1 e da v2 numa mesma execução sem reconciliação explícita.

---

## 7. Regra final

> **Baixe a emissão correta, leia a orientação comum, escolha uma Home, mantenha o contexto isolado e só então use o Source Lock + Prompt como entrada da exploração generativa.**

O GKR governa o significado. Design governa a materialização. Ferramentas generativas ampliam a exploração; não decidem a arquitetura da Guivos.
