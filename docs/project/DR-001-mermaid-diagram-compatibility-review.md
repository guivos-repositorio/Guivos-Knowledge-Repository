---
id: DR-001
title: Mermaid Diagram Compatibility Review
status: active
version: 0.2.0
owner: Guivos
last_updated: 2026-07-11
scope: Mermaid syntax, renderer compatibility, visual consistency and diagram coverage
---

# DR-001 — Mermaid Diagram Compatibility Review

## 1. Finalidade

Esta revisão valida os diagramas Mermaid do Guivos Knowledge Repository quanto a:

- sintaxe;
- compatibilidade entre renderizadores;
- legibilidade;
- consistência visual;
- adequação conceitual;
- ausência de prescrição técnica indevida;
- necessidade de diagramas adicionais.

## 2. Incidente identificado

O `GOG-001 — Guia Oficial da Guivos 4.2.0` apresentava a mensagem `Syntax error in text` no diagrama público da estrutura da Guivos.

A mesma falha aparecia duas vezes na interface porque o diagrama era processado em dois contextos distintos:

1. página normal do MkDocs;
2. versão agregada ou de impressão gerada pelo pipeline do site.

As imagens exibiam versões diferentes do Mermaid (`10.4.0` e `11.16.0`), confirmando que o mesmo bloco incompatível era analisado por mais de um renderizador.

## 3. Causa raiz

O bloco utilizava construções com compatibilidade inconsistente entre versões:

```text
S[Business | Mall | Travel | Media | Ads]
J <--> I
J <--> S
I <--> S
```

Os principais riscos eram:

- uso do caractere `|` dentro do rótulo sem aspas, interpretável como delimitador sintático;
- uso de aresta bidirecional compacta `<-->`, cuja interpretação pode variar conforme versão e integração;
- rótulos com caracteres especiais sem encapsulamento explícito.

## 4. Correções executadas

### 4.1 GOG-001 4.2.1

O diagrama público da estrutura da Guivos foi reescrito com:

- rótulos entre aspas;
- soluções especializadas em nós separados;
- arestas unidirecionais explícitas;
- remoção do caractere `|` do rótulo composto.

### 4.2 GLPA-001 1.1.1

A arquitetura em camadas utilizava o mesmo padrão de risco, especialmente arestas `<-->`.

O diagrama foi endurecido para compatibilidade cruzada por meio de:

- rótulos entre aspas;
- substituição de cada relação `<-->` por duas relações `-->`;
- manutenção de identificadores simples;
- preservação integral das decisões arquiteturais da versão 1.1.0.

## 5. Regra provisória de compatibilidade

Até a conclusão desta revisão, os diagramas Mermaid do GKR deverão preferir:

1. `flowchart TD` ou `flowchart LR`;
2. identificadores simples em ASCII;
3. rótulos textuais entre aspas quando contiverem pontuação, acentos ou símbolos;
4. arestas explícitas `-->`;
5. ausência de HTML embutido;
6. ausência de sintaxe dependente de versões recentes quando houver alternativa simples;
7. diagramas funcionais sem prescrever topologia técnica definitiva.

## 6. Auditoria dos documentos públicos

| Diagrama | Documento | Estado | Observação |
|---|---|---|---|
| Primeira compreensão | GOG | Válido | Fluxo simples, identificadores ASCII e arestas explícitas |
| Ciclo Contínuo de Evolução | GOG | Válido | Fluxo compatível e sem construções ambíguas |
| Estrutura pública da Guivos | GOG | Corrigido | Falha que originou o incidente; corrigida no GOG 4.2.1 |
| Funcionamento prático | GOG | Válido | Encadeamento simples e retorno explícito |

## 7. Auditoria inicial de Product Engineering

| Diagrama | Documento | Estado | Tratamento |
|---|---|---|---|
| Arquitetura em camadas | GLPA | Corrigido | Sintaxe endurecida na GLPA 1.1.1 |
| Aplicação das camadas ao Journey | PAS | Correção necessária | Contém rótulo com `|` e relações `<-->` |
| Filosofia operacional | PAS | Válido | Fluxo linear simples |
| Relação contínua com a vida real | PAS | Válido | Fluxo linear com retorno explícito |
| Ciclo Cognitivo | PAS | Válido | Fluxo linear e retorno explícito |
| Captura de Contexto | PAS | Refinamento recomendado | Sintaxe válida; revisar rótulos de decisão e aresta pontilhada em validação cruzada |
| Interpretação do Contexto | PAS | Válido | Fluxo linear simples |
| Contexto Vivo | PAS | Refinamento recomendado | Sintaxe funcional; revisar rótulo de aresta com vírgula e decisão em versões antigas |
| Ciclo de vida da informação | PAS | Validação cruzada necessária | `stateDiagram-v2` é suportado, mas deve ser testado nos dois renderizadores do pipeline |
| Meu Contexto Hoje | PAS | Pendente de inspeção final | Validar sintaxe e legibilidade no documento completo |

## 8. Padrões de risco encontrados

A revisão identificou quatro padrões que devem ser pesquisados no restante do GKR:

1. arestas compactas `<-->`;
2. caractere `|` dentro de rótulos;
3. rótulos extensos ou com pontuação sem aspas;
4. construções específicas, como `stateDiagram-v2`, que exigem validação nos dois renderizadores utilizados pelo pipeline.

## 9. Escopo remanescente

A revisão ainda deverá localizar e validar blocos Mermaid em:

- GIA e documentos de Intelligence;
- GEB;
- Enterprise Architecture;
- Reference Architecture;
- Research;
- Governance Framework;
- documentos de projeto e validação;
- páginas auxiliares do site.

## 10. Critérios por diagrama

Cada diagrama será classificado como:

- **válido** — sintaxe simples e compatível;
- **corrigido** — falha confirmada e removida;
- **refinamento recomendado** — renderiza, mas possui risco, ambiguidade ou baixa legibilidade;
- **substituição recomendada** — estrutura inadequada ao objetivo;
- **ausente** — documento ganharia compreensão relevante com novo diagrama.

## 11. Ponto de retomada

1. corrigir no PAS o diagrama `Aplicação das camadas ao Journey`;
2. validar no pipeline os diagramas de decisão e `stateDiagram-v2`;
3. continuar a auditoria pelos documentos arquiteturais listados na navegação do MkDocs;
4. somente encerrar a DR-001 após validação da página normal e da versão agregada de impressão.