---
id: GKR-TRADEMARK-FILING-SCOPE-001
title: Escopo de Depósito Marcário — Guivos e Assinatura Institucional
status: proposed
version: 1.3.0
owner: Guivos
last_updated: 2026-08-20
depends_on:
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-BRAND-SIGNATURE-001
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
related:
  - GKR-BRAND-DIGITAL-ASSETS-INDEX-001
  - GKR-TRADEMARK-FILING-PREFLIGHT-001
  - GKR-TRADEMARK-OWNER-CLEARANCE-EVIDENCE-001
  - GKR-TRADEMARK-SIGNATURE-FILING-DECISION-001
  - GKR-TRADEMARK-BRAZIL-SIGNATURE-FILING-AUTH-001
  - GKR-OFFICIAL-NAMING-AUTHORITY-001
  - GTM-007
normative: true
---

# Escopo de Depósito Marcário — Guivos e Assinatura Institucional

## 1. Finalidade

Este documento governa o escopo de proteção marcária da marca `GUIVOS` e das assinaturas institucionais.

Ele separa cobertura existente, clearance, decisão de filing, pacote de autorização, protocolo e registro.

## 2. Portfólio brasileiro existente — GUIVOS

| Processo INPI | Classe | Estado |
|---|---:|---|
| `932319793` | 09 | `existing_registered_coverage` |
| `932319920` | 39 | `existing_registered_coverage` |
| `932319971` | 42 | `existing_registered_coverage` |
| `932412840` | 35 | `existing_registered_coverage` |

A razão social histórica exibida é `CLUBE DE VIAGENS E TURISMO LTDA`. O titular informou continuidade do mesmo CNPJ `43.530.598/0001-33` após a alteração para `GUIVOS LTDA`.

Não criar novo filing de `GUIVOS` nessas classes apenas para duplicar cobertura.

## 3. Assinaturas

```text
Assinatura global     Possibility, lived.
Versão PT             Possibilidade, vivida.
```

As duas são ativos marcários separados de `GUIVOS`.

## 4. Clearance e decisão

O titular informou pesquisa detalhada no INPI sem registros ou anterioridades bloqueadoras para as duas assinaturas e variações pesquisadas.

Estado:

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

```text
FILE ≠ filing_authorized
FILE ≠ filed
FILE ≠ registered
```

## 5. Especificação fechada para o pacote de autorização

### Classe 35

Escopo-alvo:

1. `Provimento de mercado on-line para compradores e vendedores de produtos e serviços [marketplace]` — `350120`;
2. `Publicidade on-line em rede de computadores` — `350084`;
3. `Marketing` — `350106`.

### Classe 42

Escopo-alvo:

1. `Software como serviço [SaaS]` — `420220`;
2. `Plataforma como serviço [PaaS]` — `420248`;
3. `Inteligência artificial como serviço [AIaaS]` — `420315`.

A rota preferida é código INPI `389`, desde que todos os itens permaneçam selecionáveis como especificação pré-aprovada no e-Marcas no momento real do filing.

Se a rota exigir código `394`, interromper e reautorizar custo/escopo.

## 6. Forma dos quatro pedidos

```text
APRESENTAÇÃO      Nominativa
NATUREZA          Produto e/ou serviço
TITULAR           GUIVOS LTDA
CNPJ              43.530.598/0001-33
TERRITÓRIO        Brasil
ROTA              pedido nacional direto no INPI
```

Não incluir logo, lockup, hashtag ou bordão.

## 7. Taxas e desconto

Referência oficial vigente consultada em 20/08/2026:

| Código | Integral por classe | Com desconto elegível de 50% |
|---|---:|---:|
| `389` | R$ 880,00 | R$ 440,00 |
| `394` | R$ 1.720,00 | R$ 860,00 |

Pacote preferencial:

```text
4 × código 389 = R$ 3.520,00 integral
4 × código 389 = R$ 1.760,00 com desconto de 50%
```

Há indicação pública secundária de porte `MICRO EMPRESA`, mas o desconto só será tratado como confirmado quando o cadastro/GRU do INPI reconhecer o enquadramento.

## 8. Estado de prontidão

```text
GUIVOS_09_35_39_42 = existing_registered_coverage
signature_clearance = CLEAR
signature_35_42 = FILE
authorization_package_prepared = true
preferred_route = INPI_389
filing_authorized = false
signature_filed = false
signature_registered = false
```

## 9. Fora da Onda 0

| Ativo | Estado |
|---|---|
| identidade visual `GUIVOS` | `DEFER` |
| `GUIVOS + Possibility, lived.` | `DEFER` |
| `GUIVOS + Possibilidade, vivida.` | `DEFER` |
| `#PossibilityLived` | `EXCLUDE` |
| `Do possível ao vivido.` | `EXCLUDE` |
| assinaturas / classes 9 e 39 | `EXCLUDE` |

## 10. Rota internacional

Para as assinaturas:

```text
signature_D0 = not_set
signature_priority_deadline = not_set
```

A eventual janela de prioridade somente começa após filing nacional efetivamente protocolado e evidenciado.

## 11. Invariantes

```text
GUIVOS REGISTRADA ≠ ASSINATURA REGISTRADA
CLEAR ≠ CONCESSÃO
FILE ≠ AUTORIZAÇÃO DE PROTOCOLO
READY_FOR_AUTHORIZATION ≠ FILING_AUTHORIZED
PEDIDO ≠ REGISTRO
REGISTRO BRASILEIRO ≠ PROTEÇÃO GLOBAL
```

## 12. Próximo gate

O `Brazil Signature Filing Authorization Package` está preparado em `GKR-TRADEMARK-BRAZIL-SIGNATURE-FILING-AUTH-001`.

O próximo gate é **Human Filing Authorization**.

Ele deverá autorizar explicitamente os quatro pedidos, emissão/pagamento das GRUs, protocolo e teto financeiro do cenário confirmado.

Nenhum protocolo ou pagamento é iniciado por este documento.
