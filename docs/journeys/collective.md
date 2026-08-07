---
id: GKR-JOURNEY-COLLECTIVE-001
title: Jornada Integrada do Coletivo
status: draft
version: 0.5.0
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
→ análise protegida
→ formação ou recusa do vínculo
```

| Etapa | Maturidade primária | Autoridade contratual | Referência materializada | Evidência de validação | Continuidade integrada |
|---|---|---|---|---|---|
| propósito, identidade e papéis | contratado | UXA-014 | — | — | não examinada |
| criação e configuração | programado | UXA-059 | cobertura parcial e dispersa | — | ausente como fluxo integral |
| presença pública | validado | UXA-056 | UXA-016 e referências de Perfil Público | UXA-018; UXA-063 | parcial |
| descoberta por Pessoas | validado | UXA-056 | UXA-060; UXA-062 | UXA-061; UXA-063 | parcial |
| recebimento de solicitação | contratado | UXA-056 | perspectiva da Pessoa em UXA-066 | UXA-067 para a perspectiva da Pessoa | parcial e assimétrica |
| visão e decisão inicial do responsável | parcial | UXA-059 | visão geral validada em UXA-087; operação de decisão ainda ausente | UXA-087 somente para GKR-SURF-COL-002 | parcial |
| formação ou recusa do vínculo | contratado | UXA-014; UXA-056 | estados de retorno à Pessoa em UXA-066 | UXA-067 para a perspectiva da Pessoa | parcial e assimétrica |

A validação da Visão Geral do Responsável não materializa automaticamente a operação completa de decisão sobre solicitações.

## 2. Operação do responsável

```text
representação e autoridade
→ visão geral
→ solicitações e vínculos
→ comunicação oficial
→ atividades, consultas e decisões
→ proteção e moderação
→ relações institucionais
→ evidências e responsabilidades
```

| Superfície ou responsabilidade | Maturidade primária | Autoridade | Materialização | Validação | Continuidade |
|---|---|---|---|---|---|
| representação e autoridade | contratado | UXA-014 | parcial | UXA-018 no escopo da referência existente; UXA-087 na visão geral | não examinada integralmente |
| Visão Geral do Responsável | validado | UXA-059; UXA-086 | UXA-086; 1 SVG desktop reformulado | UXA-087 | parcial; saída para solicitações sem destino materializado |
| gestão de solicitações | programado | UXA-056; UXA-059 | apenas retorno na perspectiva da Pessoa | UXA-067 para a perspectiva da Pessoa | ausente na perspectiva do responsável |
| participantes e vínculos | programado | UXA-059 | — | — | ausente |
| comunicação oficial | programado | UXA-058; UXA-059 | — | — | ausente |
| atividades e decisões | programado | UXA-059 | parcial ou dispersa | — | não examinada |
| proteção e moderação | contratado | UXA-058 | cobertura parcial | — | não examinada |
| relações institucionais | contratado | UXA-019 | — | — | ausente |

## 3. Handoffs críticos

| Origem | Destino | Evidência da origem | Evidência do destino | Estado da transição |
|---|---|---|---|---|
| Visão Geral do Responsável | gestão de solicitações | UXA-086; UXA-087 | nenhuma superfície própria para GKR-SURF-COL-003 | parcial; origem validada, GKR-TRN-112 não validada ponta a ponta |
| Pessoa solicitante | responsável do Coletivo | UXA-066; UXA-067 | visão geral validada, mas a fila operacional específica não | parcial e bloqueada para validação ponta a ponta |
| responsável do Coletivo | Pessoa solicitante | retorno materializado na perspectiva da Pessoa | operação de decisão não materializada | parcial e assimétrica |
| Coletivo | Organização | contrato UXA-019 | materialização bilateral ausente | não materializada |

## 4. Princípios preservados

- responsável atua somente com autoridade concedida;
- apoio institucional não transfere propriedade do Coletivo;
- análise de solicitações é protegida;
- reputação é contextual, contestável e não universal;
- atividade, alcance e volume não comprovam avanço humano;
- validação de superfície não equivale a validação de transição;
- ausência visual remanescente permanece explícita.

## 5. Estado da vista

A UXA-087 conclui a validação funcional de `GKR-SURF-COL-002`, mas esta vista permanece `draft` porque:

- a gestão completa de solicitações continua ausente;
- `GKR-TRN-112` permanece parcial;
- o handoff de solicitação possui evidência operacional apenas na perspectiva da Pessoa e uma origem validada na perspectiva do responsável;
- participantes, comunicação e demais áreas do responsável permanecem incompletos;
- a formação do vínculo e a continuidade bilateral não estão validadas ponta a ponta;
- a relação Organização–Coletivo permanece contratada e não materializada.

O status `draft` preserva a distinção entre uma superfície validada e a completude da jornada do Coletivo.

## 6. Próxima materialização necessária

A próxima frente autorizável é **UXA-088 — Materialização Controlada da Gestão de Solicitações do Responsável do Coletivo (`GKR-SURF-COL-003`)**.

A UXA-088 depende de autorização separada e não é iniciada pela UXA-087.
