---
id: UXA-100-A1
title: Integração de Planos às Jornadas e Telas Dedicadas
status: draft
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-100
related:
  - UXA-100-A2
  - GEM-004-A1
  - GPA-004
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
normative: false
---

# Integração de Planos às Jornadas e Telas Dedicadas

## 1. Finalidade

A UXA-100-A1 insere **Planos** explicitamente nas jornadas de Pessoa, Coletivo e Organização e materializa uma tela dedicada por participante.

A sincronização de 2026-08-08 atualiza somente taxonomia e leitura conceitual, preservando os nove SVGs existentes e sem criar checkout, cobrança implementada, entitlement operacional, oferta pública, novos IDs ou promoção de jornada.

## 2. Taxonomia aplicada

- Pessoa: `Free · Plus · Pro`;
- Coletivo: `Livre · Mobiliza · Impacta · Rede`;
- Organização: `Conecta · Eleva · Transforma`.

Referências visuais anteriores `Gestão/Impacto/Enterprise` e `Business Start/Growth/Scale` são migradas conforme GEM-004-A1.

Guivos Business (`Start · Growth · Scale · Enterprise`) permanece produto especializado fora da materialização desta UXA. `Organização Transforma ≠ Guivos Business Enterprise`.

## 3. Decisão de arquitetura

Planos é etapa transversal recorrente com dois pontos legítimos de entrada:

```text
entrada voluntária
área da conta/administração
→ Planos
```

```text
entrada contextual
limite legítimo atingido
→ alternativas gratuitas/operacionais aplicáveis
→ comparar planos
→ Planos
```

O participante não precisa atingir limite para conhecer, comparar ou administrar seu plano.

## 4. Espinha dorsal comum

```text
Planos
→ plano atual
→ consumo/capacidade do ciclo
→ comparação geral e incremental
→ delta direto atual → alvo
→ manter / mudar / downgrade / cancelar
→ revisão quando aplicável
→ resultado/recuperação
→ retorno ao contexto

quando contratação não for autonomamente configurável
→ BND-002 contratação/dimensionamento assistido
```

`BND-002` não é sinônimo de um plano específico.

## 5. Pessoa

![Pessoa — Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

A jornada preserva Free/Plus/Pro, entrada voluntária e contextual e proteção de Explorar/Mapa após cota Free. Plano pago não representa evolução humana.

## 6. Coletivo

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

A jornada compara `Livre · Mobiliza · Impacta · Rede`, preservando os preços/capacidades anteriormente governados. Mobiliza significa transformar intenção em mobilização coordenada; Impacta significa transformar mobilização em impacto sustentado/evidenciado; Rede representa complexidade operacional de rede, não superioridade do Coletivo.

Alternativas como rascunho, aguardar ciclo e modalidade gratuita aplicável permanecem visíveis. Quando houver necessidade real de proposta/dimensionamento, o handoff usa `BND-002` genericamente.

## 7. Organização

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

A jornada compara `Conecta · Eleva · Transforma`, preservando os preços/capacidades anteriormente atribuídos aos três níveis organizacionais.

Conecta liga capacidade institucional a pessoas/Coletivos/oportunidades; Eleva amplia coordenação e profundidade institucional; Transforma atende maior complexidade e capacidade sistêmica sem garantir impacto.

Esses planos pertencem à jornada da Organização e não são Guivos Business.

## 8. Conjunto visual preservado

A extensão continua com os mesmos 9 SVGs:

| Tipo | Pessoa | Coletivo | Organização | Total |
|---|---:|---:|---:|---:|
| tela dedicada de Planos | 1 | 1 | 1 | 3 |
| placa de fluxo de planos/pagamentos | 1 | 1 | 1 | 3 |
| comparação incremental | 1 | 1 | 1 | 3 |
| **Total** | **3** | **3** | **3** | **9** |

Inspeção: [Planos, Comparação e Cobrança](../journeys/screen-gallery-plans-billing.md).

Nenhum SVG Business é criado nesta frente.

## 9. Regra de comparação

```text
plano de maior capacidade
= capacidades preservadas
+ capacidades novas ou ampliadas
```

No downgrade, a interface mostra exatamente capacidades removidas/reduzidas. A comparação não apresenta maior capacidade como maior valor, mérito ou evolução.

## 10. Separações obrigatórias

- Planos ≠ oportunidade específica;
- assinatura ≠ taxa transacional;
- plano pago ≠ relevância, confiança, legitimidade ou evolução;
- Organização ≠ Guivos Business;
- Transforma ≠ Business Enterprise;
- tela materializada ≠ nova superfície;
- fluxo documentado ≠ gateway;
- contratação assistida ≠ checkout automático;
- BND-002 ≠ Enterprise/Scale/Rede/Transforma.

## 11. Estado documental

A sincronização taxonômica não altera as contagens nem maturidades já promovidas posteriormente pela UXA-100-A3: 118 SVGs canônicos, 53 superfícies/estados/fronteiras e 54 transições documentais no conjunto vigente.

Nenhuma jornada é promovida e Engenharia de Produto continua fora deste incremento.
