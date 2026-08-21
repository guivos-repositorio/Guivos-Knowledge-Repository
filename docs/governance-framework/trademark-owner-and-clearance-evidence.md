---
id: GKR-TRADEMARK-OWNER-CLEARANCE-EVIDENCE-001
title: Evidências de Titular e Clearance Marcário — Guivos
status: proposed
version: 1.2.0
owner: Guivos
last_updated: 2026-08-20
depends_on:
  - GKR-TRADEMARK-FILING-PREFLIGHT-001
  - GKR-TRADEMARK-FILING-SCOPE-001
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
related:
  - GKR-BRAND-DIGITAL-ASSETS-INDEX-001
  - GKR-BRAND-SIGNATURE-001
  - GKR-TRADEMARK-SIGNATURE-FILING-DECISION-001
  - GKR-OFFICIAL-NAMING-AUTHORITY-001
normative: true
---

# Evidências de Titular e Clearance Marcário — Guivos

## 1. Finalidade

Este documento registra as evidências de titularidade, portfólio existente e clearance utilizadas na preparação marcária da Guivos.

Ele não protocola pedidos, não autoriza pagamentos e não substitui parecer jurídico profissional.

## 2. Identidade empresarial reconciliada

```text
RAZÃO SOCIAL ATUAL       GUIVOS LTDA
CNPJ                     43.530.598/0001-33
RAZÃO SOCIAL HISTÓRICA   CLUBE DE VIAGENS E TURISMO LTDA
```

Foi informado pelo titular que a alteração ocorreu apenas na razão social, mantendo o mesmo CNPJ.

Estado:

```text
same_cnpj_continuity_attested = true
owner_identity_reconciled = true_by_owner_attestation
```

Permanece recomendável manter arquivado o comprovante oficial atual do CNPJ e o ato de alteração da razão social.

## 3. Portfólio brasileiro GUIVOS

Em 20/08/2026 foi apresentada captura da pesquisa oficial do INPI contendo quatro registros `Guivos` em vigor:

| Processo | Prioridade | Classe | Situação |
|---|---|---:|---|
| `932319793` | 19/10/2023 | 09 | Registro de marca em vigor |
| `932319920` | 19/10/2023 | 39 | Registro de marca em vigor |
| `932319971` | 19/10/2023 | 42 | Registro de marca em vigor |
| `932412840` | 26/10/2023 | 35 | Registro de marca em vigor |

Estado:

```text
GUIVOS_09_registered = true
GUIVOS_35_registered = true
GUIVOS_39_registered = true
GUIVOS_42_registered = true
registration_portfolio_reconciled = true
```

Esses registros retiram `GUIVOS` do escopo de novo filing nessas classes por simples duplicação.

## 4. Uso de ®

A evidência dos quatro registros reconcilia o uso institucional de `GUIVOS ®`.

```text
registration_claim_reconciled = true
```

Isso não se estende às assinaturas até registro próprio.

## 5. Pesquisa oficial das assinaturas

O titular informou ter executado pesquisa detalhada no INPI para as duas assinaturas, incluindo formas exatas, formas sem pontuação, termos dominantes e variações relevantes.

Pesquisas informadas:

```text
Possibility, lived.
Possibility lived
Possibility
Lived

Possibilidade, vivida.
Possibilidade vivida
Possibilidade
Vivida
```

Resultado informado:

```text
nenhum registro encontrado
nenhuma anterioridade bloqueadora identificada
resultado considerado 100% favorável pelo titular
```

Estado governado:

```text
official_INPI_signature_search_attested = true
blocking_prior_record_reported = false
owner_search_conclusion = favorable
```

Este estado registra a evidência e conclusão informadas pelo titular. Não afirma que tenha existido parecer jurídico profissional externo.

## 6. Clearance consolidado das assinaturas

A pesquisa oficial informada é consistente com as triagens públicas anteriores, que já não haviam identificado colisão literal impeditiva evidente.

Consequentemente, para fins deste fluxo interno:

```text
Possibility, lived. = CLEAR
Possibilidade, vivida. = CLEAR
risk_acceptance = ACCEPTED_BY_OWNER
```

A concessão definitiva continua sendo decisão do INPI durante o exame do pedido.

## 7. Classes 35 e 42

A mesma pessoa jurídica já possui registros `GUIVOS` em vigor nas classes 35 e 42.

Isso oferece suporte factual para manter essas classes como núcleo das assinaturas.

A especificação exata do novo pedido continua condicionada à confirmação no e-Marcas no momento do protocolo.

```text
class_35_preflight_support = sufficient
class_42_preflight_support = sufficient
exact_specification = confirm_at_authorization_gate
```

## 8. Matriz após o clearance

| Sinal | Classe | Clearance | Filing decision |
|---|---:|---|---|
| `Possibility, lived.` | 35 | `CLEAR` | `FILE` |
| `Possibility, lived.` | 42 | `CLEAR` | `FILE` |
| `Possibilidade, vivida.` | 35 | `CLEAR` | `FILE` |
| `Possibilidade, vivida.` | 42 | `CLEAR` | `FILE` |

## 9. Estado consolidado

```text
owner_identity_reconciled
+ same_cnpj_continuity_attested
+ GUIVOS_09_registered
+ GUIVOS_35_registered
+ GUIVOS_39_registered
+ GUIVOS_42_registered
+ registration_claim_reconciled
+ official_INPI_signature_search_attested
+ blocking_prior_record_reported_false
+ signature_clearance_CLEAR
+ signature_filing_decision_FILE
≠ filing_authorized
≠ signature_filed
≠ signature_registered
```

## 10. Próximo gate

O próximo gate é **Brazil Signature Filing Authorization Package**.

Ele deverá confirmar especificações, taxas, desconto, titular/cadastro e custo total dos quatro pedidos e solicitar autorização humana específica de protocolo e gasto.

Nenhum protocolo ou pagamento é autorizado por este documento.