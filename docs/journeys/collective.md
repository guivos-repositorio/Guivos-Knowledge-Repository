---
id: GKR-JOURNEY-COLLECTIVE-001
title: Jornada Integrada do Coletivo
status: draft
version: 0.7.0
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
| recebimento de solicitação | contratado | UXA-056 | perspectiva da Pessoa em UXA-066; operação responsável em UXA-088 | UXA-067 e UXA-089 nas perspectivas respectivas | parcial |
| visão do responsável | validado | UXA-059 | UXA-086 | UXA-087 | parcial |
| decisão do responsável | validado no escopo da superfície | UXA-056; UXA-059 | UXA-088; 7 SVGs desktop | UXA-089 | bilateral ainda não validada |
| formação ou recusa do vínculo | contratado | UXA-014; UXA-056 | resultados na Pessoa em UXA-066 e origem da decisão em UXA-088 | UXA-067; UXA-089 em pacotes distintos | parcial |

A UXA-089 fecha o gate funcional de `COL-003`, mas não converte o conjunto em jornada validada.

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
| Visão Geral do Responsável | validado | UXA-059; UXA-086 | UXA-086; 1 SVG reformulado | UXA-087 | saída materializada, transição ainda não validada |
| gestão de solicitações | validado | UXA-056; UXA-059 | UXA-088; 7 SVGs desktop; 6 reformulados em UXA-089 | UXA-089 | parcial; handoffs não validados como conjunto |
| participantes e vínculos | programado | UXA-059 | — | — | ausente |
| comunicação oficial | programado | UXA-058; UXA-059 | — | — | ausente |
| atividades e decisões | programado | UXA-059 | parcial ou dispersa | — | não examinada |
| proteção e moderação | contratado | UXA-058 | cobertura parcial | — | não examinada |
| relações institucionais | contratado | UXA-019 | — | — | ausente |

## 3. Handoffs críticos

| Origem | Destino | Evidência da origem | Evidência do destino | Estado da transição |
|---|---|---|---|---|
| Visão Geral do Responsável | gestão de solicitações | UXA-086; UXA-087 | UXA-088; UXA-089 | ambos endpoints validados como superfícies; `GKR-TRN-112` ainda não validada ponta a ponta |
| Pessoa solicitante | responsável do Coletivo | UXA-066; UXA-067 | UXA-088; UXA-089 | endpoints validados em pacotes próprios; validação integrada pendente |
| responsável do Coletivo | Pessoa solicitante | UXA-088; UXA-089 | UXA-066; UXA-067 | efeitos dos pedidos adicionais e resultados existem nos dois lados; validação integrada pendente |
| aprovação | Meus Coletivos | UXA-088; UXA-089 e resultado na Pessoa | `GKR-SURF-PER-106` ausente | parcial e bloqueada após decisão |
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
- atividade, alcance e volume não comprovam avanço humano;
- materialização não equivale a validação funcional;
- validação de superfície não equivale a validação de transição.

## 5. Estado da vista

Esta vista permanece `draft` porque:

- `GKR-TRN-105` a `GKR-TRN-109` e `GKR-TRN-112` não estão validadas ponta a ponta;
- `GKR-SURF-PER-106 — Meus Coletivos` continua ausente;
- participantes, comunicação e demais áreas do responsável permanecem incompletos;
- a relação Organização–Coletivo permanece contratada e não materializada.

A validação de `COL-003` reduz uma dívida de superfície, mas não fecha a jornada.

## 6. Próxima validação necessária

A próxima frente autorizável é **UXA-090 — Validação Integrada dos Handoffs Bilaterais de Solicitação em Coletivos**.

A UXA-090 não é iniciada pela UXA-089 e depende de autorização separada.
