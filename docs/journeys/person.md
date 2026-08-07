---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: draft
version: 0.8.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-002
  - UXA-006
  - UXA-010
  - UXA-020
  - UXA-023
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-060
  - UXA-067
  - UXA-069
  - UXA-090
  - UXA-091
  - UXA-092
  - UXA-093
  - UXA-094
  - UXA-095
normative: false
---

# Jornada Integrada da Pessoa

## 1. Início protegido e compreensão inicial

```text
Home pública
→ entrada protegida
→ escolha de modalidade
→ expressão guiada
→ inventário e autorização
→ processamento visível
→ compreensão inicial revisável
→ Tela Hoje e continuidades autorizadas
```

A continuidade integral entre compreensão inicial e Tela Hoje permanece não examinada como conjunto.

## 2. Pessoa em Coletivos

```text
Explorar Coletivos
→ Resultados de Busca
→ Perfil Público
→ Revisão e Solicitação
→ Solicitação Pendente
→ resultado aprovado
→ Meus Coletivos
→ Central de Atualizações
→ Início do Participante
```

| Etapa | Maturidade | Referência | Evidência | Continuidade integrada |
|---|---|---|---|---|
| descoberta e busca | validado | UXA-060 | UXA-061 | parcial |
| Perfil Público | validado | UXA-062 | UXA-063 | parcial |
| revisão e solicitação | validado | UXA-064 | UXA-065 | parcial |
| Solicitação Pendente | validado | UXA-066 | UXA-067; estado aprovado UXA-092 | TRN-105/106/107/109 por UXA-090; TRN-108 por UXA-092 |
| Meus Coletivos | validado | UXA-091/092/094 | UXA-092/094 | TRN-108 e TRN-110 integralmente validadas |
| Central de Atualizações | **contrato validado; SVG corrente pendente** | UXA-093/094/095 | UXA-094 no SVG anterior | TRN-110 integral; **TRN-111 parcial** |
| Início do Participante | **materializado** | **UXA-095** | validação pendente | **TRN-111 parcial** |

## 3. Continuidade pós-aprovação validada

`COL-003 → PER-105 aprovado → PER-106` permanece integralmente validada em `GKR-TRN-108`.

## 4. Meus Coletivos → Central validada

`PER-106 → Ver atualizações → PER-107` permanece integralmente validada em `GKR-TRN-110`. A UXA-095 não altera esse contrato.

## 5. Central → Início materializada

```text
PER-107
→ Pessoa escolhe “Abrir início do Coletivo”
→ nenhum vínculo, leitura, papel, presença ou autoridade é alterado
→ PER-108
→ mesmo Coletivo e vínculo permanecem em contexto
```

A sequência é **parcial**. A origem visual foi reformulada e o destino é novo; ambos exigem validação antes de `TRN-111` ser examinada ponta a ponta.

## 6. Proteções preservadas

- compartilhar pouco permanece legítimo;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- pausa não reduz reputação;
- aprovação não cria função, autoridade ou presença obrigatória;
- `Meus Coletivos` não utiliza ranking ou pontuação de dedicação;
- a Central não é feed social único;
- `lido` não equivale a consentimento ou efeito substantivo;
- abrir o Início não confirma presença, disponibilidade ou função;
- consulta não cria obrigação de resposta nem autoridade;
- `PER-108` sintetiza e encaminha para áreas próprias, sem replicá-las.

## 7. Estado da vista

Esta vista permanece `draft` porque:

- compreensão inicial → Tela Hoje não foi validada como conjunto;
- `PER-107` corrente e `PER-108` aguardam validação específica;
- `TRN-111` permanece parcial;
- estados P0B adicionais permanecem separados;
- outras continuidades da jornada pessoal ainda não foram examinadas ponta a ponta.

O status `draft` não invalida referências locais e handoffs específicos já validados.

## 8. Próxima evolução possível

A próxima frente autorizável para Coletivos é **UXA-096 — Validação Funcional do Início do Participante, Revalidação de PER-107 e Validação Integrada de GKR-TRN-111**.

A UXA-096 não foi iniciada.
