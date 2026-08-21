---
id: GKR-BRAND-DIGITAL-ASSETS-INDEX-001
title: Marca, Naming e Ativos Digitais — Índice Governado
status: active
version: 1.8.0
owner: Guivos
last_updated: 2026-08-20
related:
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-BRAND-SIGNATURE-001
  - GKR-TRADEMARK-FILING-SCOPE-001
  - GKR-TRADEMARK-FILING-PREFLIGHT-001
  - GKR-TRADEMARK-OWNER-CLEARANCE-EVIDENCE-001
  - GKR-TRADEMARK-SIGNATURE-FILING-DECISION-001
  - GKR-TRADEMARK-BRAZIL-SIGNATURE-FILING-AUTH-001
  - GKR-OFFICIAL-NAMING-AUTHORITY-001
  - GKR-DIGITAL-ASSET-CONTROL-001
  - GKR-LEGACY-NOMENCLATURE-RECONCILIATION-001
  - GKR-VALIDATED-UPDATES-SYNC-2026-08-08-001
normative: false
---

# Marca, Naming e Ativos Digitais

## 1. Propósito do domínio

Este conjunto governa identidade nominal, assinatura, proteção marcária e ativos digitais da Guivos.

A cadeia corrente é:

```text
naming canônico
→ autoridade verbal
→ portfólio existente
→ clearance das assinaturas
→ decisão FILE
→ authorization package
→ autorização humana
→ protocolo
→ evidência registral
```

## 2. Autoridade verbal

```text
Assinatura global     Possibility, lived.
Versão PT             Possibilidade, vivida.
Hashtag global        #PossibilityLived
Bordão PT             Do possível ao vivido.
```

## 3. Portfólio brasileiro existente — GUIVOS

| Processo | Classe | Situação |
|---|---:|---|
| `932319793` | 09 | Registro de marca em vigor |
| `932319920` | 39 | Registro de marca em vigor |
| `932319971` | 42 | Registro de marca em vigor |
| `932412840` | 35 | Registro de marca em vigor |

O titular informou continuidade do mesmo CNPJ `43.530.598/0001-33` após a alteração de `CLUBE DE VIAGENS E TURISMO LTDA` para `GUIVOS LTDA`.

```text
GUIVOS / 09 = existing_registered_coverage
GUIVOS / 35 = existing_registered_coverage
GUIVOS / 39 = existing_registered_coverage
GUIVOS / 42 = existing_registered_coverage
registration_claim_reconciled = true
```

## 4. Clearance e decisão das assinaturas

A pesquisa detalhada no INPI foi informada como favorável e sem anterioridades bloqueadoras.

```text
Possibility, lived. = CLEAR
Possibilidade, vivida. = CLEAR
risk_acceptance = ACCEPTED_BY_OWNER
```

Matriz:

| Sinal | Classe 35 | Classe 42 |
|---|---:|---:|
| `Possibility, lived.` | **FILE** | **FILE** |
| `Possibilidade, vivida.` | **FILE** | **FILE** |

## 5. Brazil Signature Filing Authorization Package

O pacote brasileiro está preparado em `GKR-TRADEMARK-BRAZIL-SIGNATURE-FILING-AUTH-001`.

### Forma

```text
Apresentação    Nominativa
Natureza        Produto e/ou serviço
Titular         GUIVOS LTDA
CNPJ            43.530.598/0001-33
Rota            INPI nacional direto
```

### Classe 35

1. `Provimento de mercado on-line para compradores e vendedores de produtos e serviços [marketplace]` — `350120`;
2. `Publicidade on-line em rede de computadores` — `350084`;
3. `Marketing` — `350106`.

### Classe 42

1. `Software como serviço [SaaS]` — `420220`;
2. `Plataforma como serviço [PaaS]` — `420248`;
3. `Inteligência artificial como serviço [AIaaS]` — `420315`.

### Rota e custo

Rota preferida: código INPI `389`, desde que todos os itens estejam selecionáveis como pré-aprovados no e-Marcas.

```text
4 × R$ 880,00 = R$ 3.520,00 integral
4 × R$ 440,00 = R$ 1.760,00 com desconto de 50%, se confirmado pelo INPI
```

Código `394` não está automaticamente autorizado; se necessário, deve haver nova autorização.

## 6. Documentos do domínio

- [Autoridade Oficial de Naming da Guivos](official-naming-authority.md)
- [Governança de Marca, Naming e Ativos Digitais](brand-naming-and-digital-assets-governance.md)
- [Assinatura de Marca e Sistema Verbal da Guivos](brand-signature-and-verbal-system.md)
- [Escopo de Depósito Marcário — Guivos e Assinatura Institucional](trademark-filing-scope.md) — `v1.3.0`
- [Preflight de Depósito Marcário — Guivos e Assinatura Institucional](trademark-filing-preflight.md) — `v1.4.0`
- [Evidências de Titular e Clearance Marcário — Guivos](trademark-owner-and-clearance-evidence.md) — `v1.2.0`
- [Signature Final Clearance & Filing Decision — Guivos](trademark-signature-filing-decision.md) — `v1.1.0`
- [Brazil Signature Filing Authorization Package — Guivos](trademark-brazil-signature-filing-authorization-package.md) — `v1.0.0`
- [Modelo Governado de Registro e Controle de Ativos Digitais](digital-asset-control-model.md)

## 7. Estado factual

```text
brand_naming_canonical
+ signature_system_canonical
+ GUIVOS_09_registered
+ GUIVOS_35_registered
+ GUIVOS_39_registered
+ GUIVOS_42_registered
+ owner_identity_reconciled
+ registration_claim_reconciled
+ signature_clearance_CLEAR
+ signature_35_42_FILE
+ authorization_package_prepared
+ ready_for_authorization
≠ filing_authorized
≠ GRU_issued
≠ GRU_paid
≠ signature_filed
≠ signature_registered
```

## 8. Invariantes

```text
GUIVOS REGISTRADA ≠ ASSINATURA REGISTRADA
GUIVOS ® ≠ Possibility, lived. ®
CLEAR ≠ CONCESSÃO
FILE ≠ AUTORIZAÇÃO DE PROTOCOLO
READY_FOR_AUTHORIZATION ≠ FILING_AUTHORIZED
PEDIDO ≠ REGISTRO
REGISTRO BRASILEIRO ≠ PROTEÇÃO GLOBAL
```

## 9. Próximo gate

O próximo gate é **Human Filing Authorization**.

A autorização humana deverá declarar explicitamente:

1. autorização dos quatro pedidos;
2. autorização de emissão/pagamento das GRUs;
3. autorização de protocolo;
4. teto financeiro conforme o cenário confirmado no INPI.

Cenários permitidos sem redefinir escopo:

```text
A — código 389 + desconto 50% = R$ 1.760,00
B — código 389 sem desconto   = R$ 3.520,00
```

Se o código `394` for necessário, parar e reautorizar.
