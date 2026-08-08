---
id: GKR-JOURNEY-COLLECTIVE-001
title: Jornada Integrada do Coletivo
status: draft
version: 0.14.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
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

## 3. Planos como etapa transversal candidata

A UXA-100 inclui **Planos** na jornada operacional do Coletivo. A etapa pode ser acessada a qualquer momento pela área de administração e também quando uma capacidade comercial legítima for atingida.

```text
Administração / Configurações
→ Planos
→ plano atual + consumo do ciclo
→ comparar Livre / Gestão / Impacto / Enterprise
→ manter, mudar ou solicitar proposta
→ revisão da contratação quando aplicável
→ pagamento simulado ou processo comercial governado
→ retorno à operação
```

Entrada contextual:

```text
criar atividade/oportunidade
→ limite do plano atingido ou publicação paga não incluída
├── manter rascunho / aguardar ciclo / alternativa gratuita aplicável
└── comparar planos
    → Planos
```

A tela candidata dedicada é:

![Coletivo — Planos](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

[Visualizar SVG](../assets/wireframes/uxa-100-collective-plans-screen-desktop.svg)

A tela e o fluxo devem:

- mostrar o plano atual e o consumo do ciclo;
- comparar `Livre → Gestão → Impacto → Enterprise`;
- mostrar somente o ganho incremental de cada degrau, sem reapresentar herança como novidade;
- mostrar delta direto plano atual → plano escolhido;
- exibir preço mensal/anual e recorrência aplicável antes da confirmação;
- manter ações operacionais não pagas válidas quando existirem;
- tratar Enterprise como proposta comercial e capacidade contratada, não checkout autônomo;
- no downgrade para Livre, escolher publicações gratuitas mantidas, encerrar/converter pagas excedentes e reduzir administradores/núcleos conforme limite;
- preservar compromissos, exportação e registros aplicáveis sem exclusão silenciosa;
- deixar claro que assinatura não aumenta relevância orgânica, legitimidade ou impacto.

A UXA-100-A2 aprovou funcionalmente esta etapa como candidata após reformulação da tela dedicada e do fluxo. Ela ainda não possui ID canônico de superfície ou transição.

## 4. Handoffs críticos

| Ligação | Estado |
|---|---|
| COL-002 → COL-003 (`TRN-112`) | integralmente validada |
| PER-105 ↔ COL-003 (`TRN-105/106/107/109`) | integralmente validadas |
| COL-003 → PER-106 (`TRN-108`) | integralmente validada |
| PER-106 → PER-107 (`TRN-110`) | integralmente validada |
| PER-107 → PER-108 (`TRN-111`) | **integralmente validada por UXA-096** |
| Coletivo ↔ Organização | contratada; materialização bilateral pendente |

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
- Planos foi aprovado funcionalmente apenas como etapa candidata, sem superfície/transição canônica;
- outras continuidades ainda não foram examinadas como conjunto.

## 8. Próxima evolução possível

A etapa Planos já foi auditada pela UXA-100-A2. A próxima decisão desta frente é definir, em ato governado separado, se os ativos serão fracionados e quais superfícies/transições canônicas serão criadas. Nenhuma promoção é automática.
