---
id: GKR-JOURNEY-COLLECTIVE-001
title: Jornada Integrada do Coletivo
status: draft
version: 0.8.0
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
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-086
  - UXA-087
  - UXA-088
  - UXA-089
  - UXA-090
normative: false
---

# Jornada Integrada do Coletivo

## 1. Formação e presença pública

```text
propósito e identidade
→ criação e configuração
→ presença pública
→ descoberta por Pessoas
→ solicitação de participação
→ análise pelo responsável
→ formação ou recusa do vínculo
```

| Etapa | Maturidade primária | Autoridade contratual | Referência materializada | Evidência de validação | Continuidade integrada |
|---|---|---|---|---|---|
| propósito, identidade e papéis | contratado | UXA-014 | — | — | não examinada |
| criação e configuração | programado | UXA-059 | cobertura parcial e dispersa | — | ausente como fluxo integral |
| presença pública | validado | UXA-056 | UXA-016 e Perfil Público | UXA-018; UXA-063 | parcial |
| descoberta por Pessoas | validado | UXA-056 | UXA-060; UXA-062 | UXA-061; UXA-063 | parcial |
| recebimento de solicitação | validado no handoff elegível | UXA-056 | perspectiva da Pessoa em UXA-066; operação responsável em UXA-088 | UXA-067; UXA-089; UXA-090 | TRN-105 integralmente validada |
| visão do responsável | validado | UXA-059 | UXA-086 | UXA-087 | TRN-112 integralmente validada para gestão de solicitações |
| decisão do responsável | validado no escopo da superfície | UXA-056; UXA-059 | UXA-088; 7 SVGs desktop | UXA-089 | pedidos adicionais, respostas e recusa validados bilateralmente pela UXA-090 |
| formação ou recusa do vínculo | parcial | UXA-014; UXA-056 | recusa em PER-105; aprovação observável em PER-105; PER-106 ausente | recusa integrada por UXA-090; aprovação somente na origem/resultado intermediário | TRN-109 validada; TRN-108 parcial |

A UXA-090 fecha os handoffs elegíveis, mas não converte o conjunto em jornada validada porque a continuidade de aprovação para `PER-106` e a operação interna posterior permanecem incompletas.

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
→ evidências e responsabilidades
```

| Superfície ou responsabilidade | Maturidade primária | Autoridade | Materialização | Validação | Continuidade |
|---|---|---|---|---|---|
| representação e autoridade | contratado | UXA-014 | parcial | UXA-018; UXA-087 no escopo aplicável | não examinada integralmente |
| Visão Geral do Responsável | validado | UXA-059; UXA-086 | UXA-086; 1 SVG reformulado | UXA-087 | saída para COL-003 validada por TRN-112/UXA-090 |
| gestão de solicitações | validado | UXA-056; UXA-059 | UXA-088; 7 SVGs desktop; 6 reformulados em UXA-089 | UXA-089 | handoffs 105/106/107/109 e entrada 112 validados por UXA-090 |
| participantes e vínculos | programado | UXA-059 | — | — | ausente; depende de PER-106/continuidade pós-aprovação |
| comunicação oficial | programado | UXA-058; UXA-059 | — | — | ausente |
| atividades e decisões | programado | UXA-059 | parcial ou dispersa | — | não examinada |
| proteção e moderação | contratado | UXA-058 | cobertura parcial | — | não examinada |
| relações institucionais | contratado | UXA-019 | — | — | ausente |

## 3. Handoffs críticos

| Origem | Destino | Evidência da origem | Evidência do destino | Estado da transição |
|---|---|---|---|---|
| Visão Geral do Responsável | gestão de solicitações | UXA-086; UXA-087 | UXA-088; UXA-089 | `GKR-TRN-112` integralmente validada por UXA-090 |
| Pessoa solicitante | responsável do Coletivo | UXA-066; UXA-067 | UXA-088; UXA-089 | `GKR-TRN-105` e `107` integralmente validadas por UXA-090 |
| responsável do Coletivo | Pessoa solicitante | UXA-088; UXA-089 | UXA-066; UXA-067 | `GKR-TRN-106` e `109` integralmente validadas por UXA-090 |
| aprovação | resultado aprovado em PER-105 → Meus Coletivos | UXA-088; UXA-089 e resultado na Pessoa | `GKR-SURF-PER-106` ausente | `GKR-TRN-108` parcial; continuidade precisa ser refinada com PER-106 |
| Coletivo | Organização | contrato UXA-019 | materialização bilateral ausente | não materializada |

## 4. Princípios preservados

- responsável atua somente com autoridade concedida;
- confirmação não cria ou amplia autoridade;
- critérios de aprovação ou recusa precisam ter sido apresentados à Pessoa;
- apoio institucional não transfere propriedade do Coletivo;
- análise de solicitações é protegida;
- pedido adicional não é obrigação de revelar;
- acessibilidade não é critério oculto de elegibilidade;
- recusa não é reputação ou sanção;
- expiração não é decisão equivalente do responsável;
- cancelamento e expiração supervenientes tornam ações anteriores obsoletas;
- repetição de interação ou entrega não duplica o efeito lógico;
- atividade, alcance e volume não comprovam avanço humano;
- materialização não equivale a validação funcional;
- validação de superfície não equivale a validação de transição;
- validação integral documental não equivale a implementação.

## 5. Estado da vista

Esta vista permanece `draft` porque:

- `GKR-TRN-108` continua parcial;
- `GKR-SURF-PER-106 — Meus Coletivos` continua ausente;
- participantes, comunicação e demais áreas do responsável permanecem incompletos;
- a relação Organização–Coletivo permanece contratada e não materializada;
- outras continuidades da jornada ainda não foram examinadas como conjunto.

A UXA-090 reduz materialmente a dívida de continuidade, mas não fecha a Jornada do Coletivo.

## 6. Próxima validação necessária

A próxima frente autorizável é **UXA-091 — Materialização Controlada de Meus Coletivos (`GKR-SURF-PER-106`) e Refinamento da Continuidade Pós-Aprovação**.

A UXA-091 não é iniciada pela UXA-090 e depende de autorização separada.
