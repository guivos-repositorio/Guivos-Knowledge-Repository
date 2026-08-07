---
id: UXA-100-A1
title: Integração de Planos às Jornadas e Telas Dedicadas
status: draft
version: 0.1.2
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
parent: UXA-100
related:
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

A UXA-100-A1 estende a UXA-100 para inserir **Planos** explicitamente nas jornadas da Pessoa, do Coletivo e da Organização e materializar uma tela dedicada de Planos para cada participante.

A extensão não cria checkout real, cobrança implementada, entitlement operacional, oferta pública, IDs canônicos de superfície/transição ou promoção das jornadas.

## 2. Decisão de arquitetura da experiência

Planos passa a existir como **etapa transversal recorrente** da experiência, com dois pontos legítimos de entrada:

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

O participante não precisa atingir um limite para conhecer, comparar ou administrar seu plano.

## 3. Espinha dorsal comum

```text
Planos
→ plano atual
→ consumo/capacidade do ciclo
→ comparação geral
→ comparação incremental
→ delta direto plano atual → plano alvo
→ manter / upgrade / downgrade / cancelar / solicitar proposta
→ revisão da contratação quando aplicável
→ pagamento simulado ou processo comercial governado
→ sucesso/falha
→ retorno ao contexto anterior
```

## 4. Pessoa

Tela dedicada candidata:

![Pessoa — Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

A jornada inclui acesso voluntário por Conta/Configurações, plano atual e consumo da cota personalizada, comparação Free / Plus / Pro, ganho incremental e comparação direta, gestão de cobrança/downgrade/cancelamento e entrada contextual a partir de correspondência personalizada adicional após cota Free.

Proteção obrigatória: atingir a cota do Free não esconde oportunidade pública, Explorar ou Mapa.

## 5. Coletivo

Tela dedicada candidata:

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

A jornada inclui acesso pela administração/configurações, plano atual e consumo mensal, comparação Livre / Gestão / Impacto / Enterprise, delta incremental e direto, upgrade/downgrade/cancelamento, Enterprise por proposta comercial e entrada contextual quando cota/capacidade for atingida.

Alternativas como manter rascunho, aguardar ciclo ou usar modalidade gratuita aplicável permanecem visíveis quando funcionalmente válidas.

## 6. Organização

Tela dedicada candidata:

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

A jornada inclui acesso pela administração, plano atual/capacidade/consumo, comparação Business Start / Growth / Scale, diferença incremental e direta, mudança/downgrade/cancelamento, Scale por proposta comercial e entrada contextual quando capacidade de novas oportunidades/programas for atingida.

Arquivar, agendar ou manter rascunho permanecem alternativas quando aplicáveis.

## 7. Conjunto visual da UXA-100

A extensão consolida 9 SVGs candidatos:

| Tipo | Pessoa | Coletivo | Organização | Total |
|---|---:|---:|---:|---:|
| tela dedicada de Planos | 1 | 1 | 1 | 3 |
| placa de fluxo de planos/pagamentos | 1 | 1 | 1 | 3 |
| comparação incremental | 1 | 1 | 1 | 3 |
| **Total** | **3** | **3** | **3** | **9** |

Inspeção: [Planos, Comparação e Cobrança — Galeria Candidata](../journeys/screen-gallery-plans-billing.md).

## 8. Regra de comparação

Cada plano superior deverá ser apresentado como:

```text
plano superior
= capacidades preservadas do plano anterior
+ capacidades novas ou ampliadas deste degrau
```

Benefícios herdados não serão descritos como novidade. Quando plano atual e alvo forem conhecidos, a interface deve apresentar o delta direto. No downgrade, deve mostrar exatamente capacidades removidas ou reduzidas antes da confirmação.

## 9. Separações obrigatórias

- Planos ≠ oportunidade específica;
- assinatura ≠ taxa transacional;
- plano pago ≠ relevância;
- plano pago ≠ confiança ou legitimidade;
- plano pago ≠ evolução humana;
- tela materializada ≠ superfície canônica;
- fluxo de pagamento documentado ≠ gateway implementado;
- proposta Enterprise/Scale ≠ checkout automático.

## 10. Estado documental

Com esta extensão:

- Jornada da Pessoa: `draft` 0.12.0;
- Jornada do Coletivo: `draft` 0.13.0;
- Jornada da Organização: `draft` 0.5.0;
- Jornadas Integradas: `active` 0.28.1 como instrumento de leitura;
- Catálogo: `active` 0.23.0, preservando 109 SVGs canônicos e registrando 9 candidatos separados;
- Galeria principal: `active` 0.18.0, com referência ao apêndice candidato;
- Galeria candidata de Planos: `draft` 0.1.0.

A baseline canônica anterior permanece 109 SVGs, 40 IDs de superfície/responsabilidade/fronteira e 37 transições. Os 9 SVGs de Planos são candidatos e não alteram essas contagens.

Nenhuma jornada é promovida por esta extensão.

## 11. Próximo gate

Antes de qualquer promoção canônica, uma validação funcional posterior deverá examinar os 9 SVGs e decidir se cada tela está assertiva, quais estados devem ser fracionados, quais superfícies/transições devem ser criadas e como retorno, erro, idempotência e estado corrente serão registrados.

Nenhuma dessas decisões é automática.