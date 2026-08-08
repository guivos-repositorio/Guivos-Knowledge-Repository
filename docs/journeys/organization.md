---
id: GKR-JOURNEY-ORGANIZATION-001
title: Jornada Integrada da Organização
status: draft
version: 0.9.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
related:
  - UXA-004
  - UXA-007
  - UXA-008
  - UXA-012
  - UXA-013
  - UXA-014
  - UXA-015
  - UXA-017
  - UXA-019
  - UXA-024
  - UXA-025
  - UXA-028
  - UXA-029
  - UXA-038
  - UXA-055
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-098
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
  - UXA-101
  - GPA-004
normative: false
---

# Jornada Integrada da Organização

## 1. Continuidade institucional

```text
identidade, unidade e autoridade
→ visão geral institucional
→ responsabilidade material atual
→ oportunidades e programas
→ relações com Coletivos e Organizações
→ compromissos e recursos
→ evidências e resultados permitidos
→ revisão, renovação, ajuste, pausa ou encerramento
```

| Etapa | Maturidade primária | Autoridade | Evidência principal | Continuidade |
|---|---|---|---|---|
| fundação institucional | contratado | UXA-014 | — | não examinada |
| Visão Geral | validado | UXA-014 | UXA-015/017 | parcial |
| cadastro de oportunidades | validado | UXA-004 | UXA-008/013 | publicação→descoberta validada por UXA-098 |
| descoberta e detalhe | validado | UXA-004 | UXA-024/028/007 + validações | TRN-203/204/210/211; TRN-205 até BND-001 |
| relação Organização–Coletivo | contratado | UXA-019 | — | ausente |
| patrocínio/Opportunity Boost | materializado | UXA-038 | UXA-040 a UXA-055/099 | parcial |
| Planos e cobrança | canonicamente registrado | GEM-004 / UXA-100-A3 | 3 SVGs / 4 superfícies | transições internas locais; BND-002 parcial |
| evidências/resultados | indeterminado | referências dispersas | — | não examinada |

A validação de uma tela ou fluxo não equivale à validação integral da jornada institucional.

## 2. Organização não é Guivos Business

`Organização` é tipo de participante institucional. `Guivos Business` é produto especializado da Guivos.

A jornada da Organização utiliza planos:

> **Conecta · Eleva · Transforma**

Guivos Business utiliza taxonomia conceitual própria:

> **Start · Growth · Scale · Enterprise**

Não existe correspondência automática 1:1. **Organização Transforma ≠ Guivos Business Enterprise.**

Uma Organização pode operar no ecossistema sem contratar Business; contratar Business não altera automaticamente seu plano institucional.

## 3. Publicação → descoberta

A UXA-098 preserva:

```text
ORG-003
→ oportunidade aprovada/ativa
→ informações materiais vigentes
→ TRN-203
→ candidata à descoberta em PER-201
```

Ativação não garante impressão, posição, alcance ou recomendação e não transfere autoridade sobre relevância individual.

## 4. Continuidade até fronteira externa

Mapa, Lista e Detalhe preservam a mesma identidade lógica. `TRN-205` é validada pela UXA-101 somente até `BND-001`; processo e resultado posteriores pertencem ao terceiro.

A Organização continua responsável por preço, disponibilidade, local, modalidade, capacidade, elegibilidade, risco, responsável e demais informações materiais de suas oportunidades.

## 5. Planos como etapa transversal canônica

Função conceitual:

- **Conecta**: conectar capacidade institucional a Pessoas, Coletivos e oportunidades;
- **Eleva**: ampliar coordenação, recorrência, governança operacional e profundidade analítica;
- **Transforma**: atender maior complexidade institucional e transformar capacidade em impacto sistêmico sustentado quando houver evidência e governança.

Nenhum plano garante impacto, reputação ou legitimidade.

```text
ORG-301 — Planos e comparação
├── TRN-421 → ORG-302 — revisão de mudança autonomamente configurável
│   └── TRN-422 → ORG-304 — resultado/recuperação
│       └── TRN-425 → ORG-301
├── TRN-423 → ORG-303 — downgrade/cancelamento
│   └── TRN-424 → ORG-304
│       └── TRN-425 → ORG-301
└── quando contratação não for autonomamente configurável
    → TRN-426 → BND-002 — contratação/dimensionamento assistido
```

`TRN-421` a `TRN-425` permanecem localmente validadas. `TRN-426` permanece parcial.

Entrada contextual:

```text
criar nova oportunidade/programa
→ capacidade atingida
├── arquivar / agendar / manter rascunho quando aplicável
└── comparar planos
    → ORG-301
```

Referência:

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

Regras:

- `ORG-301` compara `Conecta → Eleva → Transforma`;
- preços/capacidades preservam a baseline governada em GEM-004-A1;
- comparação incremental pertence à mesma superfície;
- delta direto atual→alvo permanece obrigatório;
- `ORG-302` explicita preço/recorrência/início/pagador/beneficiário quando aplicáveis;
- contratação não amplia consentimento nem acesso a dados individuais;
- `ORG-303` trata unidades, administradores, publicações, Coletivos relacionados, integrações e exportação;
- históricos/agregados não são apagados para retenção;
- `ORG-304` diferencia sucesso/falha e preserva estado anterior quando não confirmado;
- `BND-002` é genérico e não sinônimo de Transforma;
- capacidade paga não compra relevância, confiança ou impacto.

## 6. Relação com Coletivos

```text
rascunho
→ proposta
→ avaliação bilateral
→ negociação
→ aprovação pelas duas autoridades
→ relação ativa
→ revisão
→ renovação, ajuste, pausa ou encerramento
```

A relação preserva finalidade, compromissos, recursos, autonomia, dados, contestação e saída. Apoio ou patrocínio não concede propriedade/direção/acesso irrestrito.

## 7. Limites de visibilidade

- publicação não equivale a distribuição garantida;
- dados individuais não são expostos por padrão;
- resultados agregados dependem de finalidade/autoridade;
- publicidade não compra legitimidade/reputação/relevância;
- plano institucional pago amplia capacidade, não posição orgânica;
- atingir limite não altera retroativamente publicações existentes;
- `TRN-205` não atribui controle sobre processo externo;
- cobertura incompleta permanece lacuna explícita.

## 8. Estado da vista

A vista permanece `draft`: relação Organização–Coletivo ainda não possui materialização bilateral completa; integrações patrocinadas seguem parciais; transições internas de Planos são locais; `TRN-426` permanece parcial; cobrança real, gateway e processo assistido posterior a `BND-002` não foram validados ponta a ponta.

A separação Organização ≠ Guivos Business não promove a jornada nem cria nova superfície.

## 9. Estado da frente

A Organização mantém publicação/descoberta validada, saída consciente até `BND-001` validada no limite Guivos e Planos canônicos pela UXA-100-A3. Nenhuma próxima UXA é iniciada automaticamente.
