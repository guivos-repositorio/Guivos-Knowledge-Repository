---
id: UXA-100-A1
title: Integração de Planos às Jornadas e Telas Dedicadas
status: draft
version: 0.3.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
parent: UXA-100
depends_on:
  - GEM-004-PLAN-TAXONOMY-AUTHORITY-001
related:
  - UXA-100-A2
  - GKR-JOURNEYS-001
  - GKR-JOURNEY-PERSON-001
  - GKR-JOURNEY-COLLECTIVE-001
  - GKR-JOURNEY-ORGANIZATION-001
  - GKR-JOURNEY-SCREEN-GALLERY-PLANS-001
  - GKR-JOURNEY-SCREEN-CATALOG-001
  - GPA-004
normative: false
---

# Integração de Planos às Jornadas e Telas Dedicadas

## 1. Finalidade

A UXA-100-A1 estende a UXA-100 para inserir **Planos** explicitamente nas jornadas da Pessoa, do Coletivo e da Organização e materializar uma tela dedicada de Planos para cada participante.

A extensão não cria checkout real, cobrança implementada, entitlement operacional, oferta pública, IDs canônicos de superfície/transição ou promoção das jornadas.

A UXA-100-A2 executou posteriormente a auditoria funcional dos nove SVGs candidatos e os aprovou como materializações candidatas após reformulação controlada de seis ativos.

A versão 0.3.0 sincroniza a leitura do conjunto com `GEM-004-PLAN-TAXONOMY-AUTHORITY-001`, separando definitivamente **Organização** de **Guivos Business** sem criar nova superfície, transição ou SVG.

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
→ manter / upgrade / downgrade / cancelar / solicitar dimensionamento assistido
→ revisão da contratação quando aplicável
→ pagamento simulado ou processo comercial governado
→ sucesso/falha
→ retorno ao contexto anterior
```

Quando a contratação deixa de ser autonomamente configurável, o handoff existente para `BND-002` deve ser lido como **fronteira de contratação/dimensionamento assistido**, e não como fronteira semanticamente exclusiva de Enterprise ou Scale.

## 4. Pessoa

Tela dedicada candidata:

![Pessoa — Planos](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-person-plans-screen-mobile.svg)

A jornada inclui acesso voluntário por Conta/Configurações, plano atual e consumo da cota personalizada, comparação **Free / Plus / Pro**, ganho incremental e comparação direta, gestão de cobrança/downgrade/cancelamento e entrada contextual a partir de correspondência personalizada adicional após cota Free.

Proteção obrigatória: atingir a cota do Free não esconde oportunidade pública, Explorar ou Mapa.

A leitura conceitual é:

- **Free** — começar sem barreira econômica;
- **Plus** — aprofundar a jornada com mais contexto e continuidade;
- **Pro** — operar a própria jornada com maior profundidade e capacidade analítica.

## 5. Coletivo

Tela dedicada candidata:

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

A jornada inclui acesso pela administração/configurações, plano atual e consumo mensal, comparação **Livre / Mobiliza / Impacta / Rede**, delta incremental e direto, upgrade/downgrade/cancelamento e entrada contextual quando cota/capacidade for atingida.

A leitura conceitual é:

- **Livre** — organizar e agir livremente em escala inicial;
- **Mobiliza** — transformar intenção em mobilização coordenada;
- **Impacta** — transformar mobilização em impacto sustentado e evidenciado;
- **Rede** — conectar e coordenar múltiplos núcleos como uma rede.

Alternativas como manter rascunho, aguardar ciclo ou usar modalidade gratuita aplicável permanecem visíveis quando funcionalmente válidas.

A nomenclatura anterior Gestão / Impacto / Enterprise fica superada para leitura comercial do Coletivo. A mudança não promove transições nem cria equivalência automática de capacidade fora da autoridade econômica aplicável.

## 6. Organização

Tela dedicada candidata:

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

A jornada de Organização utiliza **Conecta / Eleva / Transforma**.

A leitura conceitual é:

- **Conecta** — conectar capacidade institucional a pessoas, coletivos e oportunidades;
- **Eleva** — elevar a capacidade institucional de gerar valor e continuidade;
- **Transforma** — transformar capacidade institucional em impacto sistêmico sustentado, condicionado a evidências reais.

A tela e seus estados preservam os IDs `ORG-301` a `ORG-304`. A sincronização de nomenclatura não cria nova jornada nem altera a natureza de Organização como participante.

Arquivar, agendar ou manter rascunho permanecem alternativas quando aplicáveis.

## 7. Guivos Business

Guivos Business não é um quarto tipo de participante desta materialização. Ele é um **produto especializado da Guivos** e possui taxonomia própria:

- Start;
- Growth;
- Scale;
- Enterprise.

A separação obrigatória é:

```text
Organização = participante do ecossistema
Guivos Business = produto especializado
```

Não existe correspondência automática 1:1 entre Conecta / Eleva / Transforma e Start / Growth / Scale / Enterprise.

Em particular:

> **Organização Transforma ≠ Guivos Business Enterprise.**

A UXA-100-A1 não cria `BUS-*`, tela dedicada, transição ou SVG para Guivos Business. Sua futura materialização, se necessária, dependerá de frente própria governada.

## 8. Conjunto visual da UXA-100

A extensão mantém os mesmos 9 SVGs:

| Tipo | Pessoa | Coletivo | Organização | Total |
|---|---:|---:|---:|---:|
| tela dedicada de Planos | 1 | 1 | 1 | 3 |
| placa de fluxo de planos/pagamentos | 1 | 1 | 1 | 3 |
| comparação incremental | 1 | 1 | 1 | 3 |
| **Total** | **3** | **3** | **3** | **9** |

Inspeção: [Planos, Comparação e Cobrança — Galeria Candidata](../journeys/screen-gallery-plans-billing.md).

A autoridade conceitual desta atualização não altera IDs, quantidade ou associação dos nove ativos.

## 9. Regra de comparação

Cada plano superior deverá ser apresentado como:

```text
plano superior
= capacidades preservadas do plano anterior
+ capacidades novas ou ampliadas deste degrau
```

Benefícios herdados não serão descritos como novidade. Quando plano atual e alvo forem conhecidos, a interface deve apresentar o delta direto. No downgrade, deve mostrar exatamente capacidades removidas ou reduzidas antes da confirmação.

A progressão entre planos representa capacidade/serviço e **não uma escada de valor, mérito ou evolução do participante**.

## 10. Separações obrigatórias

- Planos ≠ oportunidade específica;
- assinatura ≠ taxa transacional;
- plano pago ≠ relevância;
- plano pago ≠ confiança ou legitimidade;
- plano pago ≠ evolução humana;
- Organização ≠ Guivos Business;
- Organização Transforma ≠ Guivos Business Enterprise;
- tela materializada ≠ superfície canônica;
- fluxo de pagamento documentado ≠ gateway implementado;
- `BND-002` ≠ checkout automático;
- `BND-002` ≠ plano Enterprise ou Scale.

## 11. Estado documental

A sincronização conceitual preserva:

- Jornada da Pessoa: `draft`;
- Jornada do Coletivo: `draft`;
- Jornada da Organização: `draft`;
- 9 SVGs da UXA-100;
- os mesmos IDs canônicos promovidos posteriormente pela UXA-100-A3;
- nenhuma promoção artificial de maturidade.

Nenhuma jornada é promovida por esta extensão ou por sua auditoria.

## 12. Resultado da auditoria funcional preservado

A UXA-100-A2 permanece responsável pelo resultado já registrado:

- 9 SVGs auditados;
- 6 reformulados controladamente;
- 3 aprovados sem reforma;
- 9/9 aprovados funcionalmente no escopo então auditado;
- nenhuma implementação ou operação presumida.

A alteração de taxonomia não transforma essa auditoria em validação de uma futura experiência própria de Guivos Business.

## 13. Precedência

Em nomenclatura, função, significado e leitura conceitual dos planos, `GEM-004-PLAN-TAXONOMY-AUTHORITY-001` prevalece sobre referências históricas conflitantes desta UXA.

Esta sincronização não inicia UXA-102/V5 nem Engenharia de Produto.