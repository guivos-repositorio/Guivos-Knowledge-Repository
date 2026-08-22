---
id: GKR-TRADEMARK-OWNER-CLEARANCE-EVIDENCE-001
title: Evidências de Titular e Clearance Marcário — Guivos
status: active
version: 1.3.0
owner: Guivos
last_updated: 2026-08-21
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
  - GKR-GLOBAL-INTEGRITY-POST300-001
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

Em 20/08/2026 foi apresentada evidência da pesquisa oficial do INPI contendo quatro registros `Guivos` em vigor:

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

## 5. Evidência rastreável da pesquisa oficial das assinaturas

A pesquisa oficial das assinaturas é registrada no GKR por referência, sem copiar para o corpus público material externo que não precise integrar a Canon.

```text
evidence_id       = GKR-TM-EVIDENCE-INPI-SIGNATURE-2026-08-20-001
evidence_date     = 2026-08-20
evidence_type     = owner_supplied_official_INPI_search
storage_mode      = reference_only
source_system     = INPI official trademark search
holder/reviewer   = Guivos / titular
public_GKR_copy   = false
```

**Localização governada:** evidência fornecida pelo titular no fluxo de governança do GKR, composta por capturas/resultados da pesquisa oficial do INPI. O artefato bruto permanece fora do corpus público; este registro preserva o identificador, a origem, a data, o escopo e a conclusão necessários à rastreabilidade.

### 5.1 Escopo informado da busca

Sinais e variações pesquisados:

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

Escopo de decisão suportado por esta evidência:

```text
território = Brasil
base = INPI
sinais = Possibility, lived. + Possibilidade, vivida.
classes de filing em avaliação = 35 + 42
formas = exata + sem pontuação + termos dominantes + variações relevantes informadas
```

Resultado informado:

```text
nenhum registro exato encontrado para as assinaturas
nenhuma anterioridade bloqueadora identificada pelo titular
resultado considerado favorável pelo titular
```

Estado governado:

```text
official_INPI_signature_search_attested = true
blocking_prior_record_reported = false
owner_search_conclusion = favorable
evidence_traceability = reference_only_identified
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

`CLEAR` representa decisão interna de prosseguir com base no conjunto de evidências disponível e no risco aceito pelo titular. Ele não significa inexistência absoluta de risco registral.

## 7. Classes 35 e 42

A mesma pessoa jurídica já possui registros `GUIVOS` em vigor nas classes 35 e 42.

Isso oferece suporte factual para manter essas classes como núcleo das assinaturas.

A especificação exata do novo pedido continua condicionada à confirmação no e-Marcas no momento do protocolo.

```text
class_35_preflight_support = sufficient
class_42_preflight_support = sufficient
exact_specification = confirm_at_authorization_gate
AIaaS_activity_compatibility = evidence_required_if_item_is_to_be_filed
```

A evidência de registros GUIVOS em classe 42 **não prova, por si só, atividade efetiva compatível com toda especificação possível da classe 42**. Em particular, `AIaaS` exige confirmação própria antes de sua inclusão executada.

## 8. Matriz após o clearance

| Sinal | Classe | Clearance | Filing decision |
|---|---:|---|---|
| `Possibility, lived.` | 35 | `CLEAR` | `FILE` |
| `Possibility, lived.` | 42 | `CLEAR` | `FILE` |
| `Possibilidade, vivida.` | 35 | `CLEAR` | `FILE` |
| `Possibilidade, vivida.` | 42 | `CLEAR` | `FILE` |

A coluna `Filing decision` reproduz o resultado da autoridade downstream `GKR-TRADEMARK-SIGNATURE-FILING-DECISION-001` para leitura integrada; ela não é pré-requisito desta evidência.

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
+ evidence_reference_identified
+ blocking_prior_record_reported_false
+ signature_clearance_CLEAR
+ signature_filing_decision_FILE
≠ filing_authorized
≠ signature_filed
≠ signature_registered
```

## 10. Próximo gate na cadeia

O próximo gate lógico após esta evidência é **Signature Final Clearance & Filing Decision — Guivos**.

Depois da decisão `FILE / DEFER / EXCLUDE`, o fluxo poderá chegar ao **Brazil Signature Filing Authorization Package**.

Nenhum protocolo ou pagamento é autorizado por este documento.
