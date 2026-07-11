---
id: DR-001
title: Mermaid Diagram Compatibility Review
status: active
version: 0.3.0
owner: Guivos
last_updated: 2026-07-11
scope: Mermaid syntax, renderer compatibility, visual consistency and diagram coverage
---

# DR-001 — Mermaid Diagram Compatibility Review

## 1. Finalidade

Esta revisão valida os diagramas Mermaid do Guivos Knowledge Repository quanto a sintaxe, compatibilidade entre renderizadores, legibilidade, consistência visual, adequação conceitual e ausência de prescrição técnica indevida.

## 2. Incidente identificado

O `GOG-001 — Guia Oficial da Guivos 4.2.0` apresentava a mensagem `Syntax error in text` no diagrama público da estrutura da Guivos.

A mesma falha podia aparecer em mais de um ponto porque os diagramas são processados na página normal e na versão agregada ou de impressão. As imagens apresentaram Mermaid `10.4.0` e `11.16.0`, demonstrando a existência de renderizadores distintos no pipeline.

## 3. Causa raiz

O padrão incompatível identificado foi:

```text
S[Business | Mall | Travel | Media | Ads]
J <--> I
J <--> S
I <--> S
```

Riscos associados:

- caractere `|` dentro de rótulo sem aspas;
- aresta bidirecional compacta `<-->`;
- rótulos com pontuação, símbolos ou acentos sem encapsulamento;
- construções específicas de versões quando existe alternativa mais simples.

## 4. Correções executadas

### 4.1 GOG-001 4.2.1

O diagrama público da estrutura da Guivos foi reescrito com rótulos entre aspas, soluções em nós separados e arestas unidirecionais explícitas.

### 4.2 GLPA-001 1.1.1

O diagrama em camadas foi endurecido para compatibilidade cruzada, substituindo relações `<-->` por pares de relações `-->` e encapsulando rótulos.

### 4.3 PAS-001 0.4.2

A mensagem remanescente na versão agregada foi associada aos padrões de risco ainda presentes no PAS. O documento foi corrigido integralmente quanto aos diagramas Mermaid:

- `Aplicação das camadas ao Journey`: removidos `|` e `<-->`;
- todos os rótulos passaram a utilizar aspas;
- encadeamentos compactos foram substituídos por arestas explícitas;
- decisões com losangos e rótulos de aresta foram simplificadas;
- aresta pontilhada foi removida da Captura de Contexto;
- `stateDiagram-v2` foi substituído por `flowchart LR` no ciclo de vida da informação;
- os significados funcionais foram preservados.

A correção cobre o diagrama que poderia falhar na página do PAS e também na versão agregada ou de impressão exibida após o rodapé de outras páginas.

## 5. Regra de compatibilidade

Os diagramas Mermaid do GKR deverão preferir:

1. `flowchart TD` ou `flowchart LR`;
2. identificadores simples em ASCII;
3. rótulos textuais entre aspas;
4. arestas explícitas `-->`;
5. ausência de HTML embutido;
6. ausência de `|` em rótulos compostos;
7. ausência de `<-->` quando duas arestas explícitas puderem representar a relação;
8. alternativas simples a construções dependentes de versão;
9. diagramas funcionais sem prescrever topologia técnica definitiva.

## 6. Estado dos documentos públicos

| Diagrama | Documento | Estado |
|---|---|---|
| Primeira compreensão | GOG | Válido |
| Ciclo Contínuo de Evolução | GOG | Válido |
| Estrutura pública da Guivos | GOG | Corrigido no GOG 4.2.1 |
| Funcionamento prático | GOG | Válido |

## 7. Estado de Product Engineering

| Diagrama | Documento | Estado |
|---|---|---|
| Arquitetura em camadas | GLPA | Corrigido na GLPA 1.1.1 |
| Aplicação das camadas ao Journey | PAS | Corrigido no PAS 0.4.2 |
| Filosofia operacional | PAS | Compatibilidade endurecida |
| Relação contínua com a vida real | PAS | Compatibilidade endurecida |
| Ciclo Cognitivo | PAS | Compatibilidade endurecida |
| Captura de Contexto | PAS | Simplificado e corrigido |
| Interpretação do Contexto | PAS | Compatibilidade endurecida |
| Contexto Vivo | PAS | Simplificado e corrigido |
| Ciclo de vida da informação | PAS | Convertido para flowchart compatível |
| Meu Contexto Hoje | PAS | Compatibilidade endurecida |

## 8. Observação de publicação

Após um commit, a mensagem pode permanecer temporariamente no site publicado até que o pipeline de MkDocs/GitHub Pages conclua uma nova implantação e o navegador descarte o conteúdo em cache.

A validação visual deve ser feita após a implantação mais recente, preferencialmente com atualização forçada da página.

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

1. aguardar a implantação do commit do PAS 0.4.2;
2. validar a página normal do PAS e a versão agregada de impressão;
3. continuar a auditoria pelos demais documentos arquiteturais;
4. encerrar a DR-001 somente após não haver mensagens Mermaid nos dois contextos de renderização.
