---
id: DR-001
title: Mermaid Diagram Compatibility Review
status: active
version: 0.1.0
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

As imagens exibiam versões diferentes do Mermaid (`10.4.0` e `11.16.0`), confirmando que o mesmo bloco inválido era analisado por mais de um renderizador.

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

## 4. Correção executada

O GOG foi atualizado para `4.2.1`.

A correção adotou sintaxe conservadora e compatível:

- rótulos entre aspas;
- remoção do caractere `|` no nó;
- substituição de `<-->` por duas arestas unidirecionais explícitas;
- decomposição das soluções especializadas em nós separados.

## 5. Regra provisória de compatibilidade

Até a conclusão desta revisão, os diagramas Mermaid do GKR deverão preferir:

1. `flowchart TD` ou `flowchart LR`;
2. identificadores simples em ASCII;
3. rótulos textuais entre aspas quando contiverem pontuação, acentos ou símbolos;
4. arestas explícitas `-->`;
5. ausência de HTML embutido;
6. ausência de sintaxe dependente de versões recentes quando houver alternativa simples;
7. diagramas funcionais sem prescrever topologia técnica definitiva.

## 6. Escopo da auditoria

A revisão deverá localizar e validar todos os blocos `mermaid` em:

- GOG;
- PAS;
- GLPA;
- GIA;
- GEB;
- documentos de arquitetura empresarial;
- documentos de pesquisa;
- documentos de projeto;
- páginas auxiliares do site.

## 7. Critérios por diagrama

Cada diagrama será classificado como:

- **válido** — sintaxe simples e compatível;
- **corrigido** — falha confirmada e removida;
- **refinamento recomendado** — renderiza, mas possui ambiguidade ou baixa legibilidade;
- **substituição recomendada** — estrutura inadequada ao objetivo;
- **ausente** — documento ganharia compreensão relevante com novo diagrama.

## 8. Estado inicial

| Diagrama | Documento | Estado |
|---|---|---|
| Estrutura pública da Guivos | GOG | Corrigido no GOG 4.2.1 |
| Primeira compreensão | GOG | Pendente de validação cruzada |
| Ciclo Contínuo de Evolução | GOG | Pendente de validação cruzada |
| Funcionamento prático | GOG | Pendente de validação cruzada |
| Arquitetura em camadas | GLPA | Pendente de validação cruzada |
| Ciclo Cognitivo | PAS | Pendente de validação cruzada |
| Captura de Contexto | PAS | Pendente de validação cruzada |
| Interpretação do Contexto | PAS | Pendente de validação cruzada |
| Contexto Vivo | PAS | Pendente de validação cruzada |
| Ciclo de vida da informação | PAS | Pendente de validação cruzada |
| Meu Contexto Hoje | PAS | Pendente de validação cruzada |

## 9. Ponto de retomada

Executar busca completa por blocos Mermaid no repositório, catalogar os diagramas existentes e revisar primeiro os documentos públicos e de Product Engineering.