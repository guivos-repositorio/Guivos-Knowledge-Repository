---
id: GKR-CCM-UXA-052-A1
title: Adendo da Matriz de Consolidação Canônica — UXA-052
status: active
version: 0.1.0
owner: Repositório de Conhecimento da Guivos
last_updated: 2026-08-02
depends_on:
  - UXA-051
  - UXA-052
related:
  - UXA-040
  - UXA-041
  - UXA-050
  - M7.54
normative: false
---

# Adendo da Matriz de Consolidação Canônica — UXA-052

## 1. Finalidade

Registrar a validação funcional e a reformulação dos cinco wireframes móveis da configuração do anunciante do Opportunity Boost sem criar Resultado Empresarial canônico, política operacional final ou autorização de desenvolvimento.

## 2. Resultado do incremento

| Elemento | Estado anterior | Estado proposto | Autoridade |
|---|---|---|---|
| configuração móvel | cinco wireframes materializados | funcionalmente válida após reformulação | UXA-051; UXA-052 |
| identidade da campanha | incompleta em algumas etapas | persistente entre as cinco telas | UXA-052 §5.1 |
| estado atual e exceção | próximos visualmente | separados e explicitamente rotulados | UXA-052 §5.2 |
| objetivo | seleção exibida com ambiguidade temporal | estado posterior a escolha explícita | UXA-052 §5.3 |
| critérios | revisáveis em nível geral | revisáveis ou removíveis individualmente | UXA-052 §5.4 |
| condição limitada | visível principalmente no gate | preservada até prévia e versão enviada | UXA-052 §5.5 |
| estimativa | sem atualização visível | provisória, datada e sujeita a recálculo | UXA-052 §5.6 |
| renovação automática | caixa vazia ambígua | estado desativado, sem consentimento | UXA-052 §5.7 |
| controles da pessoa | pareciam ações do anunciante | identificados como demonstração | UXA-052 §5.8 |
| cancelamento | ação aparentemente imediata | revisão e confirmação separadas | UXA-052 §5.9 |

## 3. Cobertura por canal

| Responsabilidade | Computador | Aplicativo móvel |
|---|---|---|
| elegibilidade e gates | validada e reformulada | validada e reformulada |
| objetivo e critérios | validada e reformulada | validada e reformulada |
| orçamento e período | validada e reformulada | validada e reformulada |
| prévia e confirmação | validada e reformulada | validada e reformulada |
| envio para avaliação | validado e reformulado | validado e reformulado |
| gestão da campanha | validada e reformulada | não materializada |
| relatório agregado | validado e reformulado | validado e reformulado |

## 4. Invariantes preservados

- configuração e aprovação não iniciam entrega;
- pagamento não altera relevância orgânica;
- primeiro resultado orgânico permanece orgânico;
- contexto protegido não alimenta publicidade;
- critérios protegidos permanecem excluídos;
- público insuficiente não amplia critérios automaticamente;
- condição limitada não equivale a bloqueio;
- CPM e CPC não são simultâneos;
- estimativa não é garantia;
- renovação automática permanece desativada;
- controles da pessoa não são ações do anunciante;
- cancelamento preserva histórico;
- anunciante não recebe lista de visualizadores.

## 5. Decisões que permanecem candidatas

| Tema | Estado |
|---|---|
| gestão móvel da campanha | não materializada |
| estados completos de erro | não materializados |
| inventário insuficiente | não materializado operacionalmente |
| preferências publicitárias | experiência detalhada não materializada |
| política final de categorias | não definida |
| política final de atribuição | não definida |
| limiar de agregação e privacidade | não definido |
| reconciliação e saldo | tratamento final não definido |
| protótipo e testes | não iniciados |
| Engenharia de Produto | pausada antes de W0-01 |

## 6. Resultado Empresarial

A UXA-052 não cria, aprova, funde ou canonicaliza Resultado Empresarial.

O estado permanece:

```text
Human decisions: 18
Under Validation: 9
Merged: 3
Rejected: 6
Approved Outcomes: 0
Canonical EO/BO codes: 0
```

## 7. Marco

O incremento propõe:

> **M7.54 — Configuração Móvel do Anunciante do Opportunity Boost Funcionalmente Validada e Reformulada**

## 8. Regra de avanço

Validação funcional não equivale a protótipo, teste com usuários, política operacional, implementação responsiva, campanha real ou produção.

Qualquer avanço posterior exige autorização separada.
