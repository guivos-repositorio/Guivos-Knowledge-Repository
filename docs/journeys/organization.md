---
id: GKR-JOURNEY-ORGANIZATION-001
title: Jornada Integrada da Organização
status: draft
version: 0.8.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
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

| Etapa | Maturidade primária | Autoridade contratual | Referência materializada | Evidência de validação | Continuidade integrada |
|---|---|---|---|---|---|
| fundação institucional | contratado | UXA-014 | — | — | não examinada |
| Visão Geral da Organização | validado | UXA-014 | UXA-015 | UXA-017 | parcial |
| responsabilidade material atual | contratado | UXA-014 | presente parcialmente na Visão Geral | UXA-017 no escopo da referência | parcial |
| cadastro de oportunidades | validado | UXA-004 | UXA-008 | UXA-013 | **publicação → descoberta validada por UXA-098** |
| descoberta Mapa/Lista e detalhe | validado | UXA-004 | UXA-024; UXA-028; UXA-007 | UXA-025; UXA-029; UXA-012; UXA-101 no recorte de saída | **TRN-203/204/210/211 por UXA-098; TRN-205 até BND-001 por UXA-101** |
| relação Organização–Coletivo | contratado | UXA-019 | — | — | ausente |
| patrocínio e Opportunity Boost | materializado | UXA-038 | UXA-040 a UXA-055 | UXA-041 a UXA-055; residual UXA-099 | parcial |
| Planos e cobrança | **canonicamente registrado** | GEM-004 / UXA-100-A3 | 3 SVGs canônicos / 4 superfícies | UXA-100-A2/A3 | transições internas locais; Scale parcial |
| evidências e resultados institucionais | indeterminado | referências dispersas | matriz integrada ausente | — | não examinada |

A validação de uma tela institucional ou de um fluxo de cadastro não equivale à validação integral da jornada institucional.

## 2. Publicação → descoberta validada

A UXA-098 formaliza:

```text
ORG-003
→ oportunidade aprovada e ativa
→ autoridade e informações materiais vigentes
→ TRN-203
→ candidata à descoberta em PER-201
```

A ativação torna a oportunidade elegível ao inventário de descoberta, mas não garante impressão, posição, alcance ou recomendação; não concede à Organização autoridade sobre relevância individual; não converte patrocínio em prioridade orgânica; e permanece subordinada a disponibilidade, elegibilidade, proteção, atualização e moderação aplicáveis.

Pausa, expiração, encerramento ou alteração material prevalecem sobre cartões ou detalhes anteriormente renderizados. Reprocessamento do mesmo estado não duplica oportunidade nem prioridade.

## 3. Continuidade até a fronteira externa

A oportunidade mantém a mesma identidade lógica em Mapa, Lista e Detalhe.

- `TRN-210`: Mapa e Lista preservam a mesma consulta;
- `TRN-204`: Mapa abre o Detalhe preservando origem e estado;
- `TRN-211`: Lista abre o mesmo Detalhe preservando origem e estado;
- `TRN-205`: UXA-101 valida o handoff consciente de `PER-203` até `BND-001`.

Antes da saída, `PER-203` explicita destino externo, responsável, dados/contexto que acompanham ou não a transição e ausência de garantia de conclusão. Destino ausente, inválido ou materialmente alterado bloqueia redirecionamento silencioso. Após `BND-001`, o processo e o resultado pertencem ao terceiro.

A Organização continua responsável por manter preço, disponibilidade, local, modalidade, capacidade, elegibilidade, risco, responsável e demais informações materiais atualizados.

## 4. Planos como etapa transversal canônica

A UXA-100-A3 registra **Planos** canonicamente na jornada institucional da Organização.

```text
ORG-301 — Planos e comparação
├── TRN-421 → ORG-302 — revisão de contratação Growth
│   └── TRN-422 → ORG-304 — resultado/recuperação
│       └── TRN-425 → ORG-301
├── TRN-423 → ORG-303 — downgrade/cancelamento
│   └── TRN-424 → ORG-304
│       └── TRN-425 → ORG-301
└── TRN-426 → BND-002 — proposta Business Scale
```

`TRN-421` a `TRN-425` estão localmente validadas. `TRN-426` permanece parcial porque o processo comercial posterior a `BND-002` não foi materializado.

Entrada contextual:

```text
criar nova oportunidade/programa
→ capacidade do ciclo atingida
├── arquivar / agendar / manter rascunho quando aplicável
└── comparar planos
    → ORG-301
```

As superfícies administrativas de origem que não possuem identidade própria suficiente no registro não recebem transições inventadas nesta frente.

Referência canônica:

![Organização — Planos](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-organization-plans-screen-desktop.svg)

Regras:

- `ORG-301` mostra plano atual, uso e período do ciclo;
- compara `Business Start → Business Growth → Business Scale`;
- comparação incremental pertence a `ORG-301`, sem superfície adicional;
- apresenta delta direto do plano atual para o escolhido;
- `ORG-302` exibe preços mensal/anual, recorrência, início, pagador/autoridade financeira e beneficiário antes da confirmação;
- contratação não amplia consentimento nem acesso ao contexto individual de Pessoas;
- `ORG-303` exige selecionar unidades, administradores, publicações e Coletivos relacionados mantidos, integrações a encerrar e dados a exportar;
- históricos/agregados não são apagados para forçar retenção;
- `ORG-304` diferencia sucesso e falha, preservando plano anterior e direitos quando não houver confirmação;
- Scale usa `BND-002`, não checkout definitivo;
- capacidade comercial permanece separada de relevância, confiança, legitimidade e resultado.

## 5. Relação com Coletivos

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

| Campo | Organização | Coletivo | Estado da integração |
|---|---|---|---|
| autoridade | representante institucional autorizado | responsável autorizado pelo Coletivo | contratada pela UXA-019 |
| superfície de proposta | não materializada especificamente | não materializada especificamente | ausente |
| avaliação e negociação | contratada | contratada | não materializada |
| aprovação bilateral | contratada | contratada | não validada |
| relação ativa e revisão | contratada | contratada | não materializada |
| saída, pausa e encerramento | contratada | contratada | não materializada |

A relação preserva finalidade, compromissos, recursos, autonomia, dados, contestação e saída. Apoio ou patrocínio não concede propriedade, direção ou acesso irrestrito a dados.

## 6. Limites de visibilidade

- publicação não equivale a distribuição garantida;
- dados pessoais individuais não são expostos por padrão;
- resultados agregados dependem de finalidade e autoridade;
- publicidade não compra legitimidade, reputação ou relevância funcional;
- plano pago amplia capacidade institucional, não relevância orgânica;
- atingir limite do plano não altera retroativamente a legitimidade de publicações existentes;
- representante institucional atua somente dentro da unidade e do papel apresentados;
- `TRN-205` não atribui à Organização nem à Guivos controle sobre o processo externo posterior;
- cobertura incompleta permanece indicada como lacuna.

## 7. Estado da vista

Esta vista permanece `draft` porque:

- a relação Organização–Coletivo não possui materialização bilateral específica;
- a matriz institucional completa ainda não existe;
- `TRN-201` permanece parcial e `TRN-202` localmente validada;
- integrações patrocinadas com Mapa/Lista (`TRN-304`/`TRN-306`) permanecem parciais;
- as transições internas de Planos são locais e `TRN-426` permanece parcial;
- cobrança real, gateway e processo Scale não foram implementados/validados ponta a ponta;
- evidências e resultados institucionais continuam sem matriz integrada.

`TRN-205` deixa de ser pendência desta vista: UXA-101 a valida até `BND-001`, sem promover a jornada institucional completa.

## 8. Estado da frente

A organização mantém publicação/descoberta validada pela UXA-098, saída consciente até `BND-001` validada pela UXA-101 e Planos canônicos pela UXA-100-A3. Nenhuma próxima UXA é iniciada automaticamente.