---
id: GKR-TRADEMARK-FILING-PREFLIGHT-001
title: Preflight de Depósito Marcário — Guivos e Assinatura Institucional
status: active
version: 1.5.0
owner: Guivos
last_updated: 2026-08-21
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
  - GKR-GLOBAL-INTEGRITY-POST300-001
  - GTM-007
normative: true
---

# Preflight de Depósito Marcário — Guivos e Assinatura Institucional

## 1. Finalidade

Este documento é o **preflight de entrada** do fluxo de filing das assinaturas. Ele consolida condições, escopo técnico pretendido, rota, custos de referência e verificações que devem existir **antes** dos resultados downstream de clearance, decisão `FILE` e autorização operacional.

A ordem semântica é:

```text
ESCOPO DE FILING
→ PREFLIGHT
→ EVIDÊNCIA / CLEARANCE
→ DECISÃO FILE / DEFER / EXCLUDE
→ PACOTE DE AUTORIZAÇÃO
→ AUTORIZAÇÃO HUMANA
→ GRU / PROTOCOLO / EVIDÊNCIA REGISTRAL
```

Os documentos de clearance, decisão e autorização aparecem em `related` apenas para rastreabilidade. **Eles não são pré-requisitos deste preflight.**

Este documento não protocola pedido, não decide `CLEAR`, não decide `FILE` e não autoriza pagamento.

## 2. Portfólio `GUIVOS` já coberto

A evidência temática posterior reconcilia o portfólio `GUIVOS` nas classes 09, 35, 39 e 42. Para o escopo de preflight, essas linhas são tratadas como cobertura existente a confirmar/consultar na autoridade de evidência e não integram o pacote de duplicação.

```text
GUIVOS / 09
GUIVOS / 35
GUIVOS / 39
GUIVOS / 42
→ fora do novo pacote de simples duplicação
```

## 3. Escopo técnico dos quatro pedidos candidatos

| # | Sinal | Classe | Apresentação | Estado neste preflight |
|---|---|---:|---|---|
| 1 | `Possibility, lived.` | 35 | Nominativa | `PREFLIGHT_DEFINED` |
| 2 | `Possibility, lived.` | 42 | Nominativa | `PREFLIGHT_DEFINED` |
| 3 | `Possibilidade, vivida.` | 35 | Nominativa | `PREFLIGHT_DEFINED` |
| 4 | `Possibilidade, vivida.` | 42 | Nominativa | `PREFLIGHT_DEFINED` |

`PREFLIGHT_DEFINED` não significa clearance, decisão de depósito, autorização ou pedido protocolado.

## 4. Especificação-alvo — classe 35

Para ambos os sinais, alvo de seleção, se disponível no e-Marcas vigente:

1. `Provimento de mercado on-line para compradores e vendedores de produtos e serviços [marketplace]` — `350120`;
2. `Publicidade on-line em rede de computadores` — `350084`;
3. `Marketing` — `350106`.

## 5. Especificação-alvo — classe 42

Para ambos os sinais, alvo de seleção:

1. `Software como serviço [SaaS]` — `420220`;
2. `Plataforma como serviço [PaaS]` — `420248`;
3. `Inteligência artificial como serviço [AIaaS]` — `420315`, **somente se a compatibilidade com a atividade efetiva/objeto aplicável estiver evidenciada no gate de autorização**.

`AIaaS` integrar a classificação aplicável não substitui a necessidade de compatibilidade factual do titular.

```text
ITEM CLASSIFICÁVEL
≠ ITEM AUTOMATICAMENTE EXECUTÁVEL
```

Se a evidência de atividade efetiva não suportar AIaaS, o item deverá ser omitido do protocolo, sem reabrir automaticamente a decisão sobre a classe 42.

## 6. Rota preferida

```text
INPI código 389
Pedido de registro de marca com especificação pré-aprovada — valor por classe
```

Usar `389` somente se todos os itens efetivamente autorizados estiverem selecionáveis no e-Marcas no momento da preparação real.

Se houver necessidade de especificação livre:

```text
código 394 → STOP → revalidar → reautorizar
```

Não substituir itens silenciosamente.

## 7. Taxas vigentes de referência

Consulta de referência em 20/08/2026:

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

Taxas e elegibilidade devem ser revalidadas imediatamente antes da emissão/pagamento.

## 8. Desconto

Existe indicação de enquadramento empresarial potencialmente elegível a desconto, mas o benefício não deve ser presumido.

```text
discount_candidate = 50_percent
INPI_discount_confirmation = required_before_payment
```

## 9. Titular e cadastro pretendidos

```text
GUIVOS LTDA
CNPJ 43.530.598/0001-33
```

A identidade e a continuidade empresarial devem ser sustentadas pela autoridade de evidência. Se e-INPI/GRU exibir razão social ou CNPJ divergentes, não protocolar até reconciliar.

## 10. Checklist do preflight de entrada

- [x] sinais canônicos identificados;
- [x] classes-alvo 35 e 42 definidas;
- [x] apresentação nominativa definida;
- [x] especificações-alvo definidas;
- [x] rota preferida `389` definida;
- [x] taxas de referência registradas;
- [x] titular/CNPJ pretendidos identificados;
- [x] cenários de custo calculados;
- [ ] evidência de titular/portfólio reconciliada na autoridade própria;
- [ ] clearance executado e registrado na autoridade própria;
- [ ] decisão `FILE / DEFER / EXCLUDE` tomada na autoridade própria;
- [ ] compatibilidade de AIaaS com atividade efetiva evidenciada, caso o item vá integrar o filing;
- [ ] disponibilidade dos itens autorizados confirmada no e-Marcas imediatamente antes das GRUs;
- [ ] desconto confirmado ou negado pelo INPI;
- [ ] autorização humana explícita de protocolo e gasto.

Os itens downstream não impedem que o **preflight de entrada** esteja definido; eles impedem execução prematura do filing.

## 11. Estado deste documento

```text
preflight_defined = true
candidate_signals = 2
candidate_classes = 35_42
candidate_applications = 4
preferred_route = INPI_389
clearance_decision = governed_downstream
filing_decision = governed_downstream
filing_authorization = governed_downstream
AIaaS_execution = conditional_on_activity_evidence
```

## 12. Próxima autoridade na cadeia

A próxima autoridade lógica é `GKR-TRADEMARK-OWNER-CLEARANCE-EVIDENCE-001`, seguida por `GKR-TRADEMARK-SIGNATURE-FILING-DECISION-001`.

O pacote de autorização somente pode consumir esses resultados depois que estiverem registrados, preservando a ordem acíclica do fluxo.
