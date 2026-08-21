---
id: GKR-TRADEMARK-SIGNATURE-FILING-DECISION-001
title: Signature Final Clearance & Filing Decision — Guivos
status: proposed
version: 1.1.0
owner: Guivos
last_updated: 2026-08-20
depends_on:
  - GKR-TRADEMARK-FILING-PREFLIGHT-001
  - GKR-TRADEMARK-OWNER-CLEARANCE-EVIDENCE-001
  - GKR-BRAND-SIGNATURE-001
related:
  - GKR-TRADEMARK-FILING-SCOPE-001
  - GKR-BRAND-DIGITAL-ASSETS-INDEX-001
normative: true
---

# Signature Final Clearance & Filing Decision — Guivos

## 1. Finalidade

Este documento fecha o gate de decisão de filing para:

```text
Possibility, lived. / 35
Possibility, lived. / 42
Possibilidade, vivida. / 35
Possibilidade, vivida. / 42
```

A decisão deste documento é `FILE / DEFER / EXCLUDE`.

Ele não protocola pedido, não paga taxa, não contrata agente e não constitui parecer jurídico profissional.

## 2. Evidência oficial informada

O titular informou ter executado, de forma detalhada, todas as pesquisas planejadas na base oficial do INPI, incluindo formas exatas, formas sem pontuação, termos dominantes e variações relevantes das duas assinaturas.

Resultado informado:

```text
Possibility, lived.          nenhum registro encontrado
Possibility lived            nenhum registro encontrado
Possibility                  nenhum registro bloqueador encontrado
Lived                        nenhum registro bloqueador encontrado

Possibilidade, vivida.       nenhum registro encontrado
Possibilidade vivida         nenhum registro encontrado
Possibilidade                nenhum registro bloqueador encontrado
Vivida                       nenhum registro bloqueador encontrado
```

A pesquisa foi declarada como detalhada e 100% favorável pelo titular.

Estado governado:

```text
official_INPI_signature_search_attested = true
blocking_prior_record_reported = false
owner_search_conclusion = favorable
```

Este registro documenta a evidência e conclusão informadas pelo titular. Não transforma a análise em parecer profissional externo que não ocorreu.

## 3. Resultado de clearance

Combinando:

- pesquisa pública anterior favorável;
- ausência de colisão literal pública impeditiva identificada;
- distintividade preliminar favorável;
- pesquisa oficial do INPI informada como detalhada e sem registros;
- inexistência de anterioridade bloqueadora reportada;

este gate conclui:

```text
Possibility, lived.          CLEAR
Possibilidade, vivida.       CLEAR
```

Para fins de governança do filing brasileiro:

```text
signature_clearance_decision = CLEAR
risk_acceptance = ACCEPTED_BY_OWNER
professional_external_opinion = not_required_for_this_internal_gate
```

`CLEAR` neste documento significa que não foi identificado impedimento conhecido suficiente para manter o filing em espera. A decisão final do INPI somente ocorre no exame oficial do pedido.

## 4. Distintividade

As duas assinaturas permanecem favoráveis como sinais marcários candidatos porque:

- não descrevem diretamente SaaS, marketplace, publicidade ou inteligência artificial;
- não indicam preço, qualidade, velocidade ou característica técnica;
- usam construção sintática marcada;
- funcionam como assinatura institucional;
- exigem interpretação conceitual.

Estado:

```text
preliminary_distinctiveness = favorable
```

## 5. Matriz decisória final

| Sinal | Classe | Clearance | Decisão |
|---|---:|---|---|
| `Possibility, lived.` | 35 | `CLEAR` | **FILE** |
| `Possibility, lived.` | 42 | `CLEAR` | **FILE** |
| `Possibilidade, vivida.` | 35 | `CLEAR` | **FILE** |
| `Possibilidade, vivida.` | 42 | `CLEAR` | **FILE** |

Nenhuma linha permanece `DEFER` por clearance.

Nenhuma linha recebe `EXCLUDE`.

## 6. Significado de FILE

Neste sistema:

```text
FILE
= decisão estratégica de depositar
+ clearance suficiente para avançar
+ classe aprovada para compor o pacote
```

Mas:

```text
FILE
≠ pedido protocolado
≠ taxa paga
≠ filing_authorized
≠ registro concedido
```

O protocolo exige gate humano separado.

## 7. Classes 35 e 42

A mesma pessoa jurídica já possui registros `GUIVOS` em vigor nas classes 35 e 42, conforme evidência reconciliada no GKR.

Isso oferece suporte factual relevante para manter essas classes como núcleo das assinaturas.

A execução do protocolo ainda deverá confirmar as especificações exatas no e-Marcas vigente.

Classe 35 — escopo candidato:

- marketplace on-line;
- publicidade on-line;
- marketing.

Classe 42 — escopo candidato:

- SaaS;
- PaaS;
- AIaaS, quando compatível com a atividade efetiva e a especificação vigente.

```text
CLASSE APROVADA PARA FILE
≠ TODA ESPECIFICAÇÃO POSSÍVEL DA CLASSE APROVADA
```

## 8. Estado consolidado

```text
GUIVOS_09_registered
+ GUIVOS_35_registered
+ GUIVOS_39_registered
+ GUIVOS_42_registered
+ owner_identity_reconciled
+ signature_system_canonical
+ signature_public_screening_favorable
+ official_INPI_signature_search_attested
+ blocking_prior_record_reported_false
+ signature_clearance_CLEAR
+ signature_35_42_FILE
≠ filing_authorized
≠ signature_filed
≠ signature_registered
```

## 9. Próximo gate

O próximo gate é:

**Brazil Signature Filing Authorization Package**

Ele deverá fechar, antes de qualquer protocolo:

1. texto exato de cada sinal;
2. natureza/apresentação do pedido;
3. especificação exata da classe 35 no e-Marcas;
4. especificação exata da classe 42 no e-Marcas;
5. taxa/código vigente;
6. elegibilidade ou não a desconto;
7. custo total final;
8. titular/cadastro utilizado no INPI;
9. checklist de quatro pedidos;
10. autorização humana explícita de protocolo e gasto.

Nenhum protocolo ou pagamento é autorizado por esta versão.