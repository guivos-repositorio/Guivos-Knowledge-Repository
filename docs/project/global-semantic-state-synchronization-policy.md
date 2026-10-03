---
id: GKR-SEMANTIC-SYNC-001
title: Política de Sincronização Semântica do Estado Global
status: active
version: 1.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-06
depends_on:
  - GKR-STATE-001
related:
  - GKR-UXA-047-084-INDEX-001
  - GKR-CHANGELOG-INDEX-001
  - GKR-CANON-ADDENDA-INDEX-001
  - GKR-P1-REBASELINE-001
normative: true
---

# Política de Sincronização Semântica do Estado Global

## 1. Finalidade

Esta política impede que superfícies globais do Guivos Knowledge Repository apresentem versões, marcos, frentes ou maturidades divergentes das autoridades integradas.

Ela governa sincronização e descoberta. Não altera o estado arquitetural, não promove documentos e não autoriza a próxima frente.

## 2. Autoridade

`GKR-STATE-001` é a fonte transversal para:

- versão do estado;
- marco vigente;
- última frente integrada;
- próxima frente esperada;
- pausas;
- maturidade de galerias, matrizes e registros;
- limites e ressalvas vigentes.

As autoridades de domínio continuam prevalecendo para o conteúdo especializado. README, Home, índices e changelogs são superfícies derivadas.

## 3. Superfícies controladas

O gate semântico verifica, no mínimo:

1. `README.md`;
2. `docs/index.md`;
3. índice do intervalo UXA integrado;
4. índice de changelogs;
5. índice dos adendos canônicos;
6. política e registro de rebaseline do P1.

## 4. Regra dinâmica

O validador deve extrair a versão, o marco e a maior frente UXA registrada em `GKR-STATE-001` no commit em análise.

É proibido fixar no código uma premissa temporal como:

- “UXA-071 não iniciada”;
- “UXA-084 é sempre a última frente”;
- “M7.72 é permanente”;
- qualquer versão global imutável.

Valores concretos podem ser usados como baseline documental do pacote, mas o gate deve derivar o estado corrente da autoridade integrada.

## 5. Regras de consistência

As superfícies globais devem:

- declarar a versão e o marco extraídos de `GKR-STATE-001`;
- identificar a última UXA integrada sem apresentá-la como não iniciada;
- não conservar versões ou marcos antigos como estado vigente;
- preservar pausas e limites expressos no registro;
- distinguir aprovação documental de implementação e operação;
- manter a próxima frente como não iniciada até existir evidência integrada;
- apontar para índices cujos arquivos e links existam fisicamente.

## 6. Descobribilidade

A existência de um documento não é suficiente quando ele não pode ser localizado pelas superfícies de entrada.

A Home e o README devem apontar para:

- o Registro do Estado Atual;
- o índice UXA aplicável;
- o índice de changelogs;
- o índice dos adendos canônicos;
- os registros de rebaseline relevantes.

## 7. Gate automatizado

O script `scripts/validate_semantic_state.py` deverá falhar quando localizar:

- divergência de versão ou marco nas superfícies globais;
- ausência do último identificador UXA integrado;
- referências a estados antigos nas superfícies vigentes;
- ausência de qualquer artefato UXA obrigatório no intervalo controlado;
- link ou path UXA esperado não indexado;
- ausência dos documentos de controle do P1.

O workflow deverá executar em pull requests e em pushes para `main`.

## 8. Limites

O gate não determina mérito arquitetural, não substitui revisão humana e não prova que uma frente foi corretamente concluída. Ele verifica coerência entre autoridades e superfícies derivadas.

Nenhum sucesso mecânico autoriza merge automático, UXA-085, Engenharia de Produto ou pacotes P2–P9.
