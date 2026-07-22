---
id: GEM-006-RELATIONSHIP-ARCHETYPES-001
title: Arquétipos de Relacionamento de Parceiros
status: draft
version: 0.1.0
owner: Guivos Economic Model
last_updated: 2026-07-21
parent: GEM-006
---

# Arquétipos de Relacionamento de Parceiros

## 1. Objetivo

Definir os formatos conceituais de relacionamento entre a Guivos e parceiros, mantendo separação entre papel, escopo, economia, dados e responsabilidades.

## 2. Arquétipos

### RA-01 — Catálogo

O parceiro disponibiliza oferta para descoberta. Não pressupõe transação, recomendação, disponibilidade ou qualidade continuada.

### RA-02 — Transacional

Inclui compra, reserva, contratação ou outra operação econômica. Exige identificação de pagador, vendedor, recebedor, repasse, reembolso e disputa.

### RA-03 — Prestação de serviço

O parceiro executa serviço para a Guivos ou para participantes. Exige escopo, qualificação, responsabilidade e evidência de entrega.

### RA-04 — Financiamento ou patrocínio

O parceiro fornece recursos, inventário ou capacidade vinculados a uma finalidade. Não recebe autoridade sobre beneficiários, evidências ou conteúdo independente.

### RA-05 — Distribuição ou indicação

O parceiro origina ou encaminha demanda. Exige consentimento, atribuição, prevenção de duplicidade e comunicação autorizada.

### RA-06 — Conteúdo e mídia

O parceiro produz, licencia ou distribui conteúdo. Exige direitos, identificação de patrocínio e separação editorial.

### RA-07 — Integração tecnológica

O parceiro conecta sistemas, dados ou infraestrutura. Exige finalidade, acesso mínimo, segurança, continuidade e saída reversível.

### RA-08 — Programa institucional

A relação atende organização, comunidade ou grupo financiado. Exige proteção de participantes, dados agregados e autonomia.

### RA-09 — Aliança estratégica

Combina vários papéis e produtos sob governança específica. Não constitui sociedade, exclusividade ou autoridade automática.

## 3. Combinação de arquétipos

Relacionamentos combinados deverão registrar:

- arquétipo primário;
- arquétipos adicionais;
- permissões por arquétipo;
- responsabilidades separadas;
- mecanismos econômicos separados;
- dados permitidos por finalidade;
- conflitos decorrentes da combinação.

## 4. Regra de não generalização

```text
aprovação de um relacionamento
não autoriza todos os relacionamentos do parceiro
```

Uma integração tecnológica, por exemplo, não autoriza atuação como anunciante, patrocinador ou fornecedor comercial.

## 5. Estados conceituais

- candidate;
- under_assessment;
- conditionally_approved;
- approved;
- activating;
- active_limited;
- active;
- under_review;
- suspended;
- exiting;
- terminated;
- archived.

## 6. Fora do escopo

- parceiro real;
- contrato;
- ativação;
- preço;
- comissão;
- integração implementada.
