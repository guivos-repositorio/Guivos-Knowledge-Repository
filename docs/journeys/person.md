---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: draft
version: 0.4.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-002
  - UXA-006
  - UXA-010
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
  - UXA-056
  - UXA-060
  - UXA-061
  - UXA-062
  - UXA-063
  - UXA-064
  - UXA-065
  - UXA-066
  - UXA-067
  - UXA-068
  - UXA-069
  - UXA-072
  - UXA-073
  - UXA-074
  - UXA-075
  - UXA-090
  - UXA-091
normative: false
---

# Jornada Integrada da Pessoa

## 1. Início protegido e compreensão inicial

```text
Home pública
→ entrada protegida
→ escolha de modalidade
→ expressão guiada por texto ou voz
→ inventário e autorização
→ processamento visível
→ compreensão inicial revisável
→ decisão sobre persistência e personalização
→ Tela Hoje e continuidades autorizadas
```

| Etapa | Maturidade primária | Autoridade contratual | Referência materializada | Evidência de validação | Continuidade integrada |
|---|---|---|---|---|---|
| Home pública | validado | UXA-020 | UXA-022 | UXA-021 | parcial: entrada protegida examinada em pacote próprio |
| entrada protegida, escolha e autorização | validado | UXA-020; UXA-023 | UXA-034 | UXA-035 | parcial: ligação com expressão guiada exige leitura conjunta |
| expressão guiada | validado | UXA-068 | UXA-068 | UXA-069 | parcial: saída para inventário depende das autoridades da UXA-034 |
| processamento e compreensão inicial | validado | UXA-023 | UXA-036 | UXA-037 | parcial: transições examinadas nos pacotes de origem, não ponta a ponta nesta seção |
| Tela Hoje e continuidade recorrente | validado | UXA-002 | UXA-006 | UXA-010 | não examinada como continuidade integral após a compreensão inicial |

As superfícies citadas possuem materialização e validação nos respectivos pacotes, mas isso não valida toda a jornada pessoal ponta a ponta.

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

| Etapa | Maturidade primária | Autoridade contratual | Referência materializada | Evidência de validação | Continuidade integrada |
|---|---|---|---|---|---|
| descoberta e busca | validado | UXA-056 | UXA-060 | UXA-061 | parcial |
| Perfil Público | validado | UXA-056 | UXA-062 | UXA-063 | parcial |
| revisão e solicitação | validado | UXA-056 | UXA-064 | UXA-065 | parcial |
| Solicitação Pendente | validado com estado aprovado atual pendente de revalidação | UXA-056 | UXA-066; estado aprovado reformulado por UXA-091 | UXA-067 para a versão anterior; UXA-092 pendente para a versão atual aprovada | handoffs 105/106/107/109 integrados por UXA-090; pós-aprovação parcial |
| Meus Coletivos | materializado | UXA-056; UXA-059 | UXA-091; 1 SVG móvel | — | TRN-108 e TRN-110 parciais |
| Central de Atualizações | não iniciado | UXA-059 | — | — | ausente; TRN-110 parcial somente na origem |
| Início do Participante | reformulação pendente | UXA-059 | referência anterior não promovida nesta seção | — | ausente |

A UXA-091 estende a cobertura visual da Pessoa até `Meus Coletivos`, mas não valida a nova superfície nem a continuidade pós-aprovação.

## 3. Continuidade pós-aprovação proposta

```text
COL-003 — decisão autorizada
→ resultado aprovado em PER-105
→ Pessoa escolhe “Ver em Meus Coletivos”
→ PER-106 — vínculo confirmado visível
```

A continuidade acima está **materializada, porém parcial**. O estado aprovado corrente de `PER-105`, `PER-106` e `GKR-TRN-108` exigem validação/revalidação específica em frente posterior.

## 4. Decisões e proteções

- compartilhar pouco permanece legítimo;
- digitar não autoriza análise automática;
- gravação e transcrição possuem finalidade limitada;
- ajuda temporária não cria compreensão persistente;
- solicitação não equivale a aprovação;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- pausa não reduz reputação;
- aprovação não cria função, autoridade, notificação ou presença obrigatória;
- `Meus Coletivos` não utiliza ranking, pontuação de dedicação ou comparação entre participantes;
- recusa, cancelamento e expiração são eventos distintos;
- leitura, rolagem e silêncio não equivalem a confirmação;
- transições ausentes são mostradas como lacunas.

## 5. Estado da vista

Esta vista permanece `draft` porque:

- a continuidade entre compreensão inicial e Tela Hoje não foi validada como conjunto;
- o estado aprovado reformulado de `PER-105` ainda não foi revalidado;
- `PER-106` está materializada, porém não validada;
- `GKR-TRN-108` permanece parcial;
- `PER-107` permanece ausente;
- `PER-108` permanece com reformulação pendente.

O status `draft` não invalida referências locais já materializadas e validadas em seus pacotes de origem.

## 6. Próxima validação necessária

A próxima frente autorizável para esta continuidade é **UXA-092 — Validação Funcional de Meus Coletivos e Revalidação da Continuidade Pós-Aprovação**.

A UXA-092 não é iniciada pela UXA-091 e depende de autorização separada.
