---
id: GKR-TRADEMARK-FILING-PREFLIGHT-001
title: Preflight de Depósito Marcário — Guivos e Assinatura Institucional
status: proposed
version: 1.4.0
owner: Guivos
last_updated: 2026-08-20
depends_on:
  - GKR-TRADEMARK-FILING-SCOPE-001
  - GKR-BRAND-ASSET-GOVERNANCE-001
  - GKR-BRAND-SIGNATURE-001
  - GKR-INSTITUTIONAL-LEGAL-ARCHITECTURE-001
related:
  - GKR-BRAND-DIGITAL-ASSETS-INDEX-001
  - GKR-TRADEMARK-OWNER-CLEARANCE-EVIDENCE-001
  - GKR-TRADEMARK-SIGNATURE-FILING-DECISION-001
  - GKR-TRADEMARK-BRAZIL-SIGNATURE-FILING-AUTH-001
  - GKR-OFFICIAL-NAMING-AUTHORITY-001
  - GTM-007
normative: true
---

# Preflight de Depósito Marcário — Guivos e Assinatura Institucional

## 1. Finalidade

Este documento consolida o preflight dos novos pedidos das assinaturas após:

- reconciliação do portfólio `GUIVOS` existente;
- clearance `CLEAR` das duas assinaturas;
- decisão `FILE` nas classes 35 e 42;
- preparação do pacote brasileiro de autorização.

Não protocola pedido nem autoriza pagamento.

## 2. Portfólio `GUIVOS` já coberto

```text
GUIVOS / 09 = EXISTING_REGISTERED
GUIVOS / 35 = EXISTING_REGISTERED
GUIVOS / 39 = EXISTING_REGISTERED
GUIVOS / 42 = EXISTING_REGISTERED
```

Essas linhas não entram no novo pacote.

## 3. Matriz dos quatro pedidos

| # | Sinal | Classe | Apresentação | Clearance | Decisão | Prontidão |
|---|---|---:|---|---|---|---|
| 1 | `Possibility, lived.` | 35 | Nominativa | `CLEAR` | `FILE` | `READY_FOR_AUTHORIZATION` |
| 2 | `Possibility, lived.` | 42 | Nominativa | `CLEAR` | `FILE` | `READY_FOR_AUTHORIZATION` |
| 3 | `Possibilidade, vivida.` | 35 | Nominativa | `CLEAR` | `FILE` | `READY_FOR_AUTHORIZATION` |
| 4 | `Possibilidade, vivida.` | 42 | Nominativa | `CLEAR` | `FILE` | `READY_FOR_AUTHORIZATION` |

## 4. Especificação exata — classe 35

Para ambos os sinais, selecionar somente:

1. `Provimento de mercado on-line para compradores e vendedores de produtos e serviços [marketplace]` — `350120`;
2. `Publicidade on-line em rede de computadores` — `350084`;
3. `Marketing` — `350106`.

## 5. Especificação exata — classe 42

Para ambos os sinais, selecionar somente:

1. `Software como serviço [SaaS]` — `420220`;
2. `Plataforma como serviço [PaaS]` — `420248`;
3. `Inteligência artificial como serviço [AIaaS]` — `420315`.

`AIaaS` integra a NCL 13, versão 2026, na classe 42.

## 6. Rota preferida

```text
INPI código 389
Pedido de registro de marca com especificação pré-aprovada — valor por classe
```

Usar `389` somente se todos os itens autorizados estiverem selecionáveis no e-Marcas no momento da preparação real.

Se houver necessidade de especificação livre:

```text
código 394 → STOP → revalidar → reautorizar
```

Não substituir itens silenciosamente.

## 7. Taxas vigentes de referência

Consulta oficial em 20/08/2026:

| Código | Integral por classe | Com desconto elegível de 50% |
|---|---:|---:|
| `389` | R$ 880,00 | R$ 440,00 |
| `394` | R$ 1.720,00 | R$ 860,00 |

### Cenário preferido

```text
4 pedidos × código 389
= R$ 3.520,00 integral
= R$ 1.760,00 com desconto de 50%, se confirmado
```

### Fallback não autorizado automaticamente

```text
4 pedidos × código 394
= R$ 6.880,00 integral
= R$ 3.440,00 com desconto elegível
```

## 8. Desconto

O INPI prevê redução de até 50% em serviços elegíveis para microempresas, MEI, EPP e outras categorias previstas.

Há indicação pública secundária de que `GUIVOS LTDA` é `MICRO EMPRESA`.

```text
discount_candidate = 50_percent
INPI_discount_confirmation = required_before_payment
```

Não presumir o desconto até o cadastro/GRU do INPI refletir o benefício.

## 9. Titular e cadastro

Para os quatro pedidos:

```text
GUIVOS LTDA
CNPJ 43.530.598/0001-33
```

Se o e-INPI/GRU exibir razão social ou CNPJ divergentes, não protocolar até reconciliar.

## 10. Checklist final de preflight

- [x] sinais canônicos fechados;
- [x] clearance `CLEAR`;
- [x] classes 35 e 42 fechadas;
- [x] apresentação nominativa fechada;
- [x] especificações-alvo fechadas;
- [x] rota preferida `389` definida;
- [x] taxas oficiais de referência revalidadas;
- [x] titular/CNPJ definidos;
- [x] custo integral e descontado calculados;
- [ ] disponibilidade dos seis itens confirmada no e-Marcas imediatamente antes das GRUs;
- [ ] desconto de 50% confirmado ou negado pelo INPI;
- [ ] autorização humana explícita de protocolo e gasto.

## 11. Estado consolidado

```text
signature_clearance = CLEAR
signature_35_42 = FILE
authorization_package_prepared = true
preferred_route = INPI_389
ready_for_authorization = true
filing_authorized = false
GRU_issued = false
GRU_paid = false
filed = false
registered = false
```

## 12. Próximo gate

**Human Filing Authorization**.

A autorização deverá fixar o teto financeiro conforme o cenário confirmado:

```text
A — 389 + desconto 50% = R$ 1.760,00
B — 389 sem desconto   = R$ 3.520,00
```

Se o código 394 se tornar necessário, retornar para nova autorização.
