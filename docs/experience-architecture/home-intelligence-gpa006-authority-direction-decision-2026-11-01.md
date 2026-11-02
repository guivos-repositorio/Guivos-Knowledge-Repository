---
id: GKR-UX-HOME-INTELLIGENCE-GPA006-DIRECTION-DECISION-001
title: Decisão da Direção — Preservação da referência normativa GPA-006 v2.0.2
status: approved_documentary_scope
version: 1.0.0
owner: Direção da Guivos
last_updated: 2026-11-01
normative: false
related:
  - GPA-006
  - GKR-UX-HOME-INTELLIGENCE-MASTER-001
  - GKR-UX-HOME-INTELLIGENCE-SOURCELOCK-001
---

# Decisão da direção — referência normativa GPA-006

## 1. Manifestação expressa da direção

> A direção da Guivos aprova a alternativa A: preservar GPA-006 v2.0.2 como referência normativa da Home Intelligence, reconhecendo 2.0.3 como versão física posterior, exclusivamente para reconciliação documental, sem autorização operacional ou merge automático.

**Data do registro:** 01/11/2026. **Opção:** A. **Situação:** aprovada pela direção no escopo declarado acima.

## 2. Efeito documental autorizado

1. Preservar `GPA-006 v2.0.2` como **referência normativa declarada para a Home Pública Guivos Intelligence**, nos materiais e Source Locks que a governam.
2. Reconhecer `version: 2.0.3` no frontmatter de `docs/product-architecture/intelligence.md` como **versão física posterior do arquivo**, associada ao contrato de proveniência e explicabilidade registrado em [PR #566](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/pull/566).
3. Manter a distinção entre versão física e versão normativa, sem exigir propagação automática de 2.0.3 para as fontes congeladas.
4. A presente decisão **encerra a escolha de tratamento documental A** para a PR #720, mas não comprova ou aprova implementação funcional da Guivos AI.

## 3. Limites explícitos da autorização

Esta manifestação **não autoriza**: merge da PR #720; publicação em Pages; implantação; testes; inspeção operacional; execução de gates; alteração de credenciais ou papéis; promoção normativa para `GPA-006 v2.0.3`; descontinuação de `GPA-006 v2.0.2`; alterações em sistemas de produção; ou modificação automática de fontes fora do escopo.

Não rebaixar o frontmatter físico de 2.0.3 para 2.0.2. Eventual mudança de autoridade de produto requer deliberação específica.

## 4. Encaminhamento para a PR #720

- A decisão pode ser consumida na revisão documental da PR #720 para justificar a preservação das referências normativas a `GPA-006 v2.0.2`.
- Os Documentos Mestres, Source Locks, Design Handoff, Manifesto e Leia Primeiro das Homes permanecem sob **Experiência e Journey**.
- A proposta Retrospectiva / Contextual / Prospectiva permanece em 11 movimentos e não equivale a promessa de previsão ou operação.
- **Merge depende de avaliação e autorização distintas**, além das verificações do head atualizado. O novo commit deste registro exige conferir novamente as validações, sem presumir sucesso.

## 5. Evidência documental de origem

O commit [`601f0d6d98767b9dae399dbf0990e3361e8a064b`](https://github.com/guivos-repositorio/Guivos-Knowledge-Repository/commit/601f0d6d98767b9dae399dbf0990e3361e8a064b) alterou o metadado da versão do GPA-006 para 2.0.3 e adicionou a referência ao contrato de proveniência. A seção declaratória de autoridade permaneceu referindo 2.0.2.

**Estado resultante:** tratamento documental deliberado e registrado nesta branch; integração ao repositório canônico ainda pendente.
