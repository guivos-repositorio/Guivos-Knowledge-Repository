---
id: ADR-CC-001
title: Separação entre Conteúdo Multimodal e Registro Funcional
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
related:
  - PAS-001-CC-UIC-DOMAIN-001
  - PAS-001-CC-UIC-STORAGE-INDEX-001
---

# ADR-CC-001 — Separação entre Conteúdo Multimodal e Registro Funcional

## Status

`Proposed 0.1.0`.

## Contexto

A Captura de Contexto recebe texto, áudio, voz, imagem, vídeo, documentos, respostas estruturadas e dados importados. O agregado funcional precisa preservar estados, autoria, natureza, confirmação, autorização, correção e revogação sem incorporar toda mídia bruta ao mesmo mecanismo lógico.

Misturar conteúdo pesado e registro funcional produz acoplamento, dificulta retenção, aumenta superfície de exposição, prejudica reconstrução e transforma decisões físicas em regras de domínio.

## Decisão

Separar logicamente:

1. registro funcional da UIC-01;
2. objetos de conteúdo protegidos;
3. derivados controlados;
4. índices e projeções;
5. evidências técnicas.

O registro funcional mantém referências protegidas, hashes, versões, proveniência, políticas e estados. Conteúdo binário ou sensível permanece fora do agregado, salvo exceção explícita de schema para conteúdo inline reduzido.

## Consequências positivas

- domínio independente de tecnologia de mídia;
- retenção e exclusão por camada;
- redução de payloads funcionais;
- criptografia e chaves segregáveis;
- reconstrução sem transportar mídia em cada evento;
- índices e derivados revogáveis;
- menor risco de conteúdo bruto em logs.

## Consequências negativas

- exige consistência entre referência e objeto;
- aumenta necessidade de reconciliação;
- falhas parciais precisam de compensação;
- backup e restore tornam-se multicamada;
- observabilidade deve correlacionar recursos sem expor conteúdo.

## Alternativas rejeitadas

### Armazenar tudo no agregado

Rejeitada por acoplamento, tamanho, exposição e dificuldade de retenção.

### Tratar storage como sistema de registro

Rejeitada porque objeto não expressa autoridade, confirmação, correção ou revogação funcional.

### Manter apenas derivados

Rejeitada porque pode perder fonte, integridade, auditabilidade e possibilidade de reprocessamento autorizado.

## Invariantes

- objeto físico não substitui `capture_input_id`;
- hash não substitui identidade;
- derivado exige fonte;
- exclusão do índice não equivale a exclusão do objeto;
- ausência do objeto deverá gerar estado técnico explícito;
- restauração não reativa conteúdo revogado;
- tecnologia escolhida não pode ampliar autoridade.

## Evidências requeridas

- teste de integridade referência–objeto;
- teste de conteúdo órfão;
- teste de restore multicamada;
- teste de revogação e exclusão;
- inventário de classes de armazenamento;
- prova de que eventos não carregam mídia proibida.

## Decisões posteriores

Banco funcional, object storage, formato de referência, estratégia de transação e KMS serão definidos em ADRs tecnológicos posteriores.