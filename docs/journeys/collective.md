---
id: GKR-JOURNEY-COLLECTIVE-001
title: Jornada Integrada do Coletivo
status: draft
version: 0.16.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-08
related:
  - UXA-014
  - UXA-016
  - UXA-018
  - UXA-019
  - UXA-056
  - UXA-057
  - UXA-058
  - UXA-059
  - UXA-066
  - UXA-067
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
  - UXA-096
  - UXA-100
  - UXA-100-A1
  - UXA-100-A2
  - UXA-100-A3
normative: false
---

# Jornada Integrada do Coletivo

## 1. Formação, decisão e continuidade da Pessoa

```text
presença pública
→ descoberta
→ solicitação
→ análise responsável
→ aprovação/recusa
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

| Etapa | Maturidade | Evidência | Continuidade |
|---|---|---|---|
| presença pública e descoberta | validado localmente | UXA-016/018; UXA-060/063 | parcial entre famílias |
| solicitação | validado | UXA-064/065/066/067 | handoffs bilaterais posteriores validados nos gates |
| visão/gestão do responsável | validado | UXA-086/087/088/089 | TRN-112/105/106/107/109 integrais |
| aprovação → Meus Coletivos | validado | UXA-090/091/092 | TRN-108 integral |
| Meus Coletivos → Central | validado | UXA-092/093/094/096 | TRN-110 integral |
| Central corrente | **validado** | UXA-094/095/096 | TRN-110 e TRN-111 integrais |
| Início do Participante | **validado** | UXA-095/096 | **TRN-111 integral** |

## 2. Operação do responsável

```text
representação e autoridade
→ visão geral
→ gestão de solicitações
→ participantes e vínculos
→ comunicação oficial
→ atividades, consultas e decisões
→ proteção e moderação
→ relações institucionais
```

`COL-002` e `COL-003` estão validadas. `COL-004` a `COL-008` permanecem programadas/contratadas ou parcialmente cobertas e não são substituídas pelas superfícies da Pessoa.

## 3. Planos como etapa transversal canônica

A UXA-100-A3 registra **Planos** canonicamente na jornada operacional do Coletivo. A etapa pode ser acessada voluntariamente e também quando uma capacidade comercial legítima for atingida.

```text
COL-301 — Planos e comparação
├── TRN-411 → COL-302 — revisão de contratação
│   └── TRN-412 → COL-304 — resultado/recuperação
│       └── TRN-415 → COL-301
├── TRN-413 → COL-303 — downgrade/cancelamento
│   └── TRN-414 → COL-304
│       └── TRN-415 → COL-301
└── TRN-416 → BND-002 — contratação/dimensionamento assistido
```

`TRN-411` a `TRN-415` estão localmente validadas no pacote UXA-100. `TRN-416` permanece parcial porque o processo comercial posterior a `BND-002` não foi materializado. `BND-002` representa a necessidade de contratação/dimensionamento assistido quando o autoatendimento não for suficiente e não pertence semanticamente a um plano específico.

Entrada contextual permanece válida:

```text
criar atividade/oportunidade
→ limite do plano atingido ou publicação paga não incluída
├── manter rascunho / aguardar ciclo / alternativa gratuita aplicável
└── comparar planos
    → COL-301
```

As superfícies de criação/publicação que originam todos esses casos não são inventadas como novas transições nesta frente quando ainda não possuem identidade adequada no registro.

Referência canônica:

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

Regras:

- `COL-301` mostra plano atual e consumo do ciclo;
- compara `Livre → Mobiliza → Impacta → Rede`;
- comparação incremental pertence a `COL-301` e não cria tela própria;
- o delta direto plano atual → alvo permanece obrigatório;
- `COL-302` exibe preço mensal/anual, recorrência, início, pagador/beneficiário e método em simulação antes da confirmação;
- assinatura permanece separada de comissão, taxa do meio de pagamento e tributo;
- ações operacionais gratuitas válidas permanecem disponíveis;
- `COL-303` exige tratamento explícito de publicações gratuitas/pagas, administradores, núcleos/unidades, compromissos e exportação antes do downgrade;
- nenhum registro ou participante é apagado silenciosamente para efetivar redução de plano;
- `COL-304` diferencia sucesso de falha e preserva o estado anterior quando não houver confirmação;
- quando a contratação não puder ser concluída em autoatendimento, a jornada usa `BND-002` como fronteira assistida;
- plano pago não aumenta relevância orgânica, legitimidade ou impacto.

A UXA-100-A2 forneceu a validação funcional visual e a UXA-100-A3 promoveu `COL-301` a `COL-304`.

## 4. Handoffs críticos

| Ligação | Estado |
|---|---|
| COL-002 → COL-003 (`TRN-112`) | integralmente validada |
| PER-105 ↔ COL-003 (`TRN-105/106/107/109`) | integralmente validadas |
| COL-003 → PER-106 (`TRN-108`) | integralmente validada |
| PER-106 → PER-107 (`TRN-110`) | integralmente validada |
| PER-107 → PER-108 (`TRN-111`) | **integralmente validada por UXA-096** |
| Coletivo ↔ Organização | contratada; materialização bilateral pendente |
| COL-301 → BND-002 (`TRN-416`) | **parcial; processo de contratação/dimensionamento assistido posterior não materializado** |

## 5. Efeito da UXA-096

- reforma os SVGs correntes de `PER-107` e `PER-108` sem criar ativos;
- revalida `PER-107` e valida `PER-108`;
- valida `TRN-111` ponta a ponta com vínculo atual, retorno neutro e estado canônico;
- preserva os sete handoffs anteriores e adiciona `TRN-111` ao conjunto integral, totalizando oito;
- não materializa operação interna do responsável nem canais P1.

## 6. Princípios preservados

- responsável atua somente com autoridade concedida;
- apoio institucional não transfere governança;
- aprovação não cria função, moderação, autoridade ou presença;
- pertencimento, disponibilidade, papel aceito e autoridade permanecem separados;
- evento histórico não concede acesso interno;
- Central é triagem e Início é síntese; nenhum dos dois substitui canais especializados;
- atividade continua voluntária quando não houver compromisso previamente aceito;
- consulta não é votação universal nem obrigação de resposta;
- plano pago amplia capacidade, não legitimidade, relevância ou impacto;
- atingir cota não reduz visibilidade das publicações existentes;
- pausa, recusa e saída não reduzem reputação;
- estado canônico mais recente prevalece sobre estado visual obsoleto;
- validação integral documental não equivale a implementação.

## 7. Estado da vista

Esta vista permanece `draft` porque:

- participantes, comunicação e demais áreas do responsável continuam incompletos;
- estados P0B de superfícies da Pessoa permanecem separados;
- a relação Organização–Coletivo permanece contratada e não materializada;
- as transições de Planos são locais e `TRN-416` permanece parcial;
- cobrança real, gateway e processo assistido posterior a `BND-002` não foram implementados/validados ponta a ponta;
- outras continuidades ainda não foram examinadas como conjunto.

## 8. Estado da frente de Planos

A fragmentação e promoção canônica do Coletivo foi concluída pela UXA-100-A3 em `COL-301` a `COL-304`, `TRN-411` a `TRN-416` e `BND-002`. A taxonomia vigente desta frente é `Livre · Mobiliza · Impacta · Rede`. Nenhuma próxima UXA é iniciada automaticamente.
