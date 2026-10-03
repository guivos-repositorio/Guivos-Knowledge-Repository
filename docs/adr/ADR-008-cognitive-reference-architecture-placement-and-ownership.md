---
id: ADR-008
title: Subordinação e ownership da Cognitive Reference Architecture
status: approved
date: 2026-09-10
owner: Guivos
supersedes: null
related:
  - GPA-006
  - GIA-000
  - GAI-001
  - GEA-GRAPH-REFERENCE-001
  - ADR-003
  - ADR-005
  - ADR-006
  - ADR-007
---

# ADR-008 — Subordinação e ownership da Cognitive Reference Architecture

## Contexto

A evolução do Guivos Intelligence exige uma arquitetura de referência capaz de organizar, em nível lógico e conceitual, como pedidos cognitivos autorizados combinam contexto, conhecimento, evidências, relações, analytics e capacidades de IA para produzir compreensão útil e contextualizada.

Essa necessidade não cria um novo produto, uma nova autoridade transversal nem uma camada empresarial paralela. A arquitetura cognitiva deve permanecer subordinada às autoridades já vigentes e preservar as fronteiras entre produto, conhecimento, grafo, plataforma, governança e engenharia.

`GPA-006` permanece a autoridade de produto do Guivos Intelligence e estabelece, entre outros limites:

```text
UNIDADE SUPERIOR DE VALOR
→ compreensão útil e contextualizada

COMPREENDER
≠ DECIDIR

INTELLIGENCE CONECTA AUTORIDADES
→ NÃO AS ABSORVE
```

`GAI-001` permanece autoridade para princípios de evidência, contexto, atualização, explicabilidade, autonomia humana e distinção entre correlação e causalidade.

## Decisão

A Guivos estabelece a **Cognitive Reference Architecture como família subordinada à Guivos Intelligence Architecture (`GIA`)**.

A família utilizará o namespace:

```text
GIA-COG-xxx
```

Seu ownership arquitetural pertence à `GIA`.

A primeira autoridade documental da família será:

```text
GIA-COG-001
→ Cognitive Reference Architecture
→ Documento Mestre
```

## Posição arquitetural

```text
GPA-006
→ autoridade de produto

GIA-000 / GAI-001 / GAI-002
→ Intelligence Architecture e princípios

GIA-COG-*
→ arquitetura cognitiva de referência subordinada à GIA

GKA / Knowledge Architecture
→ autoridade sobre conhecimento, evidência e canon conforme seus próprios contratos

GEA-GRAPH-REFERENCE-001 / ADR-007
→ autoridade sobre arquitetura e tecnologia de referência para grafo

PLATFORM LAYER
→ dados, permissões, segurança, integrações, persistência e rastreabilidade

TECHNOLOGY / ENGINEERING ARCHITECTURE
→ realização física e implementação

GOVERNANCE
→ finalidade, autoridade, proteção, políticas e controles aplicáveis
```

Consequentemente:

```text
GIA-COG
≠ NOVO PRODUTO
≠ PEER DA GEA
≠ SUBSTITUTO DA GKA
≠ SUBSTITUTO DA GRAPH ARCHITECTURE
≠ PLATFORM LAYER
≠ ENGINEERING
≠ GOVERNANCE
```

## Fronteiras obrigatórias

A família `GIA-COG-*` deverá:

1. preservar `GPA-006` como autoridade sobre identidade, valor e responsabilidades do produto;
2. preservar `COMPREENDER ≠ DECIDIR`;
3. preservar `PROCESSING AUTHORIZED ≠ DISCLOSURE AUTHORIZED`;
4. consumir conhecimento e evidências sem criar autoridade canônica sobre suas fontes;
5. consumir relações governadas sem redefinir a arquitetura de grafo;
6. depender da Platform Layer para controles de dados, permissões, segurança, integração e rastreabilidade;
7. manter qualquer decomposição física sob autoridade de Technology / Engineering Architecture;
8. não converter capacidade técnica em autorização de uso;
9. distinguir fato, declaração, observação, inferência e predição;
10. preservar proveniência, temporalidade, incerteza, revisão e explicabilidade proporcional.

## Família documental

A família poderá evoluir para documentos especializados `GIA-COG-002..008` somente quando seus escopos forem individualmente autorizados e materialmente necessários.

A aprovação desta ADR **não cria esses documentos por inferência** e não torna nenhuma decomposição candidata obrigatória.

## Estado de maturidade

| Elemento | Estado |
|---|---|
| placement arquitetural | aprovado |
| owner | GIA |
| namespace | `GIA-COG-*` |
| documento mestre | `GIA-COG-001` autorizado para drafting/review |
| documentos `002..008` | não materializados |
| arquitetura física | não autorizada |
| modelo físico de dados | não autorizado |
| ontologia física | não autorizada |
| provedores/modelos/stack | não selecionados por esta ADR |
| credenciais / API keys | fora de escopo |
| dados reais | não autorizados por esta ADR |
| implementação | não autorizada |
| produção/operação | não autorizadas |

## Consequências

A partir desta decisão:

- a Cognitive Reference Architecture possui localização e ownership claros;
- `GIA-COG-001` pode ser persistido e revisado como draft sem adquirir autoridade canônica automática;
- futuras especializações cognitivas devem permanecer subordinadas à `GIA`;
- nenhuma tecnologia, engine, modelo ou fornecedor é promovido a requisito pela existência da família;
- implementação e produção continuam dependentes de decisões e gates próprios.

## Estado

**Decisão aprovada por adjudicação humana. Placement e ownership definidos; implementação, produção e uso de dados reais não autorizados.**
