---
id: GKR-UX-HOMES-PERSON-OC-E1-S1-DECISION-001
title: Decisão E1 e S1 — redação editorial e reconciliação Source Lock
status: approved_preparation_only
version: 1.0.0
owner: Direção da Guivos
last_updated: 2026-11-01
normative: false
---

# Registro da deliberação E1 + S1

A direção da Guivos deliberou expressamente **E1 + S1** conforme o documento de decisões de 2026-11-01, **exclusivamente para preparação e revisão documental**, sem autorizar merge, publicação, implantação ou execução operacional.

## Aplicação na branch candidata

- Pessoa, Mestre candidato **1.0.9**: M06, M09 e M10 passaram de “Adendo candidato (não vigente)” para redação editorial integrante **somente da candidata**, não vigente na `main`.
- Organizações e Coletivos, Mestre candidato **1.0.10**: M03, M06 e M10, sob a mesma condição.
- Leia Primeiro Pessoa/O/C candidatos **1.0.6**: referências aos dois Mestres candidatos.
- Source Lock generativo compartilhado candidato **2.3.19**: referências internas Pessoa **1.0.9** e O/C **1.0.10**. Não modifica outras autoridades nem implica promoção operacional do arquivo.
- Manifesto candidato **7.0.57**: referência condicional ao Source Lock candidato **2.3.19** e às versões dos Mestres candidatos. O Manifesto vigente na `main` permanece **7.0.56**.
- A divergência anterior Source Lock físico 2.3.18 versus referência 2.3.17 do Manifesto é tratada por **proposta coordenada**, não por promoção implícita na `main`.

## Portões preservados

1. Revisão de impacto e critérios de não regressão.
2. Validações mecânica e semântica por SHA final, se for aberta PR.
3. Autorização específica da direção para merge, em momento posterior.
4. Autorização separada para qualquer publicação ou implantação.

**Estado:** `E1_S1_approved_for_preparation / coordinated_candidate_only / no_merge_no_publish`.
