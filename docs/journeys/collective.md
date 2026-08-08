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
| solicitação | validado | UXA-064/065/066/067 | handoffs posteriores validados nos gates |
| visão/gestão do responsável | validado | UXA-086/087/088/089 | TRN-112/105/106/107/109 integrais |
| aprovação → Meus Coletivos | validado | UXA-090/091/092 | TRN-108 integral |
| Meus Coletivos → Central | validado | UXA-092/093/094/096 | TRN-110 integral |
| Central corrente | **validado** | UXA-094/095/096 | TRN-110 e TRN-111 integrais |
| Início do Participante | **validado** | UXA-095/096 | TRN-111 integral |

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

`COL-002` e `COL-003` estão validadas. `COL-004` a `COL-008` permanecem programadas/contratadas ou parcialmente cobertas.

## 3. Planos como etapa transversal canônica

A UXA-100 registra Planos na jornada do Coletivo com a taxonomia vigente:

> **Livre · Mobiliza · Impacta · Rede**

Função conceitual:

- Livre: presença e mobilização essencial sem barreira econômica;
- Mobiliza: transformar intenção em mobilização coordenada;
- Impacta: transformar mobilização em impacto sustentado e evidenciado;
- Rede: coordenar complexidade de rede, múltiplos núcleos/unidades/territórios.

Esses nomes expressam capacidade de serviço, não legitimidade, mérito ou nível de evolução do Coletivo.

```text
COL-301 — Planos e comparação
├── TRN-411 → COL-302 — revisão de contratação
│   └── TRN-412 → COL-304 — resultado/recuperação
│       └── TRN-415 → COL-301
├── TRN-413 → COL-303 — downgrade/cancelamento
│   └── TRN-414 → COL-304
│       └── TRN-415 → COL-301
└── quando contratação não for autonomamente configurável
    → TRN-416 → BND-002 — contratação/dimensionamento assistido
```

`TRN-411` a `TRN-415` permanecem localmente validadas. `TRN-416` permanece parcial porque o processo posterior a `BND-002` não foi materializado.

Entrada contextual:

```text
criar atividade/oportunidade
→ limite do plano atingido ou capacidade não incluída
├── manter rascunho / aguardar ciclo / alternativa gratuita aplicável
└── comparar planos
    → COL-301
```

Referência canônica:

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

Regras:

- `COL-301` mostra plano atual e consumo;
- compara `Livre → Mobiliza → Impacta → Rede`;
- preços/capacidades existentes são preservados conforme GEM-004-A1;
- comparação incremental pertence a `COL-301`;
- delta direto atual→alvo permanece obrigatório;
- `COL-302` exibe preço, recorrência, início, pagador/beneficiário e condições aplicáveis;
- assinatura é separada de comissão, taxa e tributo;
- alternativas operacionais válidas permanecem disponíveis;
- `COL-303` trata publicações, administradores, núcleos/unidades, compromissos e exportação antes do downgrade;
- nenhum registro/participante é apagado silenciosamente;
- `COL-304` diferencia sucesso de falha;
- `BND-002` é genérico e não sinônimo de Rede;
- plano pago não aumenta relevância, legitimidade ou impacto.

## 4. Handoffs críticos

| Ligação | Estado |
|---|---|
| COL-002 → COL-003 (`TRN-112`) | integralmente validada |
| PER-105 ↔ COL-003 (`TRN-105/106/107/109`) | integralmente validadas |
| COL-003 → PER-106 (`TRN-108`) | integralmente validada |
| PER-106 → PER-107 (`TRN-110`) | integralmente validada |
| PER-107 → PER-108 (`TRN-111`) | integralmente validada por UXA-096 |
| Coletivo ↔ Organização | contratada; materialização bilateral pendente |
| COL-301 → BND-002 (`TRN-416`) | **parcial; processo assistido posterior não materializado** |

## 5. Princípios preservados

- responsável atua somente com autoridade concedida;
- apoio institucional não transfere governança;
- aprovação não cria função/moderação/autoridade;
- evento histórico não concede acesso interno;
- Central é triagem e Início é síntese;
- plano pago amplia capacidade, não legitimidade/relevância/impacto;
- atingir cota não reduz visibilidade existente;
- pausa, recusa e saída não reduzem reputação;
- estado canônico mais recente prevalece;
- validação documental não equivale a implementação.

## 6. Estado da vista

A vista permanece `draft`: operação interna segue incompleta, relação Organização–Coletivo não está materializada, transições de Planos são locais e `TRN-416` continua parcial. Cobrança real, gateway e processo posterior a BND-002 não foram implementados/validados ponta a ponta.

## 7. Estado da frente de Planos

A fragmentação permanece em `COL-301` a `COL-304`, `TRN-411` a `TRN-416` e `BND-002`, sem novos IDs, nova UXA ou promoção de maturidade.
