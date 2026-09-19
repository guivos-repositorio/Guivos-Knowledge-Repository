---
id: GKR-UX-HOMES-DESIGN-CONSUMPTION-001
title: Homes Públicas — Contrato Canônico de Consumo para Designer e Sistemas de IA
status: active
version: 1.0.0
owner: Experience Architecture
last_updated: 2026-09-19
normative: true
maturity: v6_tool_neutral_design_consumption_contract
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOMES-DESIGN-PRODUCTION-RELEASE-001
  - GKR-HOME-MASTERS-REMEDIATION-001
related:
  - GKR-UX-HOMES-DESIGN-PRODUCTION-READINESS-001
  - GKR-UX-HOMES-GENINPUT-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-FLOW-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-V5-SNAPSHOT-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-HOME-OC-MASTER-001
  - GKR-UX-HOME-MALL-MASTER-001
  - GKR-UX-HOME-TRAVEL-MASTER-001
  - GKR-UX-HOME-MEDIA-MASTER-001
  - GKR-UX-HOME-ADS-MASTER-001
  - GKR-UX-HOME-BUSINESS-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
---

# Homes Públicas — Contrato Canônico de Consumo para Designer e Sistemas de IA

## 1. Finalidade

Esta autoridade define como a documentação das oito Homes públicas deve ser consumida pela designer e, opcionalmente, por sistemas de IA de apoio.

O modelo é deliberadamente **tool-neutral**. O Guivos Knowledge Repository não cria, edita, mantém, governa nem exige a criação de arquivos no Figma ou em qualquer outra ferramenta visual.

A designer é a autora da expressão visual e pode trabalhar manualmente no Figma, em outra ferramenta ou em combinação de ferramentas conforme seu processo profissional.

## 2. Separação de autoridade

```text
GKR
→ O QUE É
→ POR QUE EXISTE
→ O QUE PRECISA SIGNIFICAR
→ O QUE PRECISA FAZER
→ QUAIS VERDADES PRESERVAR
→ QUAIS LIMITES NÃO ULTRAPASSAR

DESIGNER
→ COMO EXPRESSAR
→ IDENTIDADE VISUAL
→ TIPOGRAFIA
→ CORES
→ IMAGENS
→ ILUSTRAÇÃO
→ COMPOSIÇÃO
→ GRID
→ MOTION
→ COMPONENTES
→ ATMOSFERA
→ LINGUAGEM VISUAL

IA DE APOIO
→ PODE LER AS MESMAS FONTES GOVERNADAS
→ PODE RESUMIR, EXPLORAR, COMPARAR E PROPOR
→ NÃO DEFINE VERDADE
→ NÃO SUBSTITUI A CRIATIVIDADE OU AUTORIA DA DESIGNER
```

## 3. Regra de não materialização pelo GKR

O GKR não possui uma etapa obrigatória de Figma Make, protótipo gerado por IA, arquivo intermediário ou Figma “definitivo”.

```text
DOCUMENTAÇÃO GOVERNADA
↓
COMPREENSÃO HUMANA
↓
CRIAÇÃO DA DESIGNER
↓
USO OPCIONAL DE IA COMO APOIO
↓
REVISÃO HUMANA / CONTRATUAL DA ENTREGA

GKR
→ NÃO MATERIALIZA O DESIGN
→ NÃO PRESCREVE O PROCESSO INTERNO DA DESIGNER
→ NÃO GOVERNA ESTRUTURA DE ARQUIVO FIGMA
```

A ferramenta visual utilizada pela designer pertence ao processo externo de Design.

## 4. Unidade de consumo

Cada Home deve ser compreendida isoladamente antes de qualquer criação.

A unidade mínima de consumo é:

1. `00-LEIA-PRIMEIRO` da Home no pacote de entrega vigente;
2. autoridades comuns do pacote;
3. Documento Mestre da Home;
4. fontes complementares explicitamente listadas;
5. dados, conteúdo e assets reais fornecidos separadamente quando aplicáveis.

Documentos históricos, outputs de IA e referências visuais externas não substituem essas fontes.

## 5. Oito classes operacionais

Toda informação usada na criação deve ser distinguível como:

- `CANONICAL` — verdade governada que deve ser preservada;
- `DESIGN_CREATIVE` — território de criação livre da designer;
- `CONTENT_CANDIDATE` — copy, label ou formulação ainda sujeita a aprovação;
- `DESIGN_HYPOTHESIS` — hipótese reversível de solução;
- `PROTOTYPE_PLACEHOLDER` — conteúdo provisório que não pode parecer fato;
- `REAL_DATA_REQUIRED` — dado que exige fonte real;
- `OPEN_QUESTION` — decisão ainda aberta que não pode ser preenchida silenciosamente;
- `PROHIBITED_INFERENCE` — inferência vedada.

Nenhuma classe muda silenciosamente de status por ter sido desenhada ou sugerida por IA.

## 6. Liberdade criativa

A designer possui liberdade para criar, evoluir ou substituir identidade visual, tipografia, paleta, imagem, ilustração, grid, composição, ritmo, componentes, motion, linguagem gráfica, atmosfera, agrupamento físico, responsividade e copy não congelada.

Nenhuma fonte, cor, layout, dashboard, card, gráfico, estética tecnológica, benchmark ou componente visual é obrigatório apenas porque apareceu em documento histórico ou exploração anterior.

## 7. O que a liberdade criativa não pode redefinir

Design não pode alterar silenciosamente significado da Home, papéis de participantes e produtos, arquitetura narrativa governada, nomenclaturas, fronteiras interproduto, autoridade, autonomia, privacidade, causalidade, explicabilidade, dados, preços, disponibilidade, parcerias, métricas, cases ou natureza de publicidade/recomendação/editorial.

## 8. Sistemas de IA

IA é opcional. Não existe ferramenta obrigatória nem etapa generativa obrigatória.

Quando utilizada, a IA deve consumir as mesmas fontes governadas disponibilizadas à designer, preservar `CANONICAL`, respeitar `PROHIBITED_INFERENCE`, não inventar `REAL_DATA_REQUIRED` e devolver propostas como apoio, nunca como autoridade.

## 9. Referências e trabalhos anteriores

O arquivo histórico `guivos.com 2.0`, Design Systems existentes, benchmarks, explorações e qualquer material visual anterior podem ser consultados somente quando a designer considerar útil.

Eles não são autoridade semântica nem identidade visual canônica por existência.

A exploração `GKR-UX-HOME-PERSON-DESIGN-EXEC-001` registrada na Issue #394 foi abandonada e permanece fora do processo aprovado.

## 10. Pacote v5 e transição para v6

`delivery/design-handoff-v5` permanece congelado como snapshot histórico reproduzível.

```text
V5
→ FROZEN / HISTORICAL

V6
→ TARGET CURRENT DELIVERY
→ TOOL-NEUTRAL
→ DESIGNER + OPTIONAL AI
→ NOT YET EMITTED BY THIS DOCUMENT
```

## 11. Critério de prontidão para entrega à designer

Uma Home está documentalmente pronta quando significado, função, fontes, fronteiras, campos criativos, conteúdo variável, dados reais necessários e perguntas abertas estão suficientemente claros para criação sem reconstrução de arquitetura e sem prescrição estética indevida.

## 12. Estado

```text
DESIGN CONSUMPTION MODEL
→ TOOL-NEUTRAL

GKR FIGMA MATERIALIZATION
→ OUT OF PROCESS

DESIGNER
→ PRIMARY CREATIVE AUTHOR

AI
→ OPTIONAL SUPPORT

VISUAL IDENTITY
→ DESIGN-OWNED

V5
→ HISTORICAL / FROZEN

V6
→ UNDER REMEDIATION / NOT YET EMITTED
```
