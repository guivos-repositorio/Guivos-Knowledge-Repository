---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: draft
version: 0.7.0
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

As superfícies citadas possuem materialização e validação nos respectivos pacotes, mas a continuidade integral entre compreensão inicial e Tela Hoje permanece não examinada como conjunto.

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
| Solicitação Pendente | validado | UXA-066 | UXA-067; estado aprovado UXA-092 | handoffs 105/106/107/109 por UXA-090; TRN-108 por UXA-092 |
| Meus Coletivos | **validado** | UXA-091/092; gatilho reformulado UXA-094 | UXA-092/094 | TRN-108 e **TRN-110** integralmente validadas |
| Central de Atualizações | **validado** | UXA-093; reformulação UXA-094 | **UXA-094** | **TRN-110 integralmente validada**; TRN-111 ausente |
| Início do Participante | reformulação/materialização pendente | UXA-059 | — | ausente |

## 3. Continuidade pós-aprovação validada

```text
COL-003 — decisão autorizada
→ resultado aprovado em PER-105
→ vínculo já formado
→ navegação opcional
→ PER-106 — vínculo confirmado visível
```

A sequência acima está integralmente validada no escopo de `GKR-TRN-108`.

## 4. Continuidade Meus Coletivos → Central validada

```text
PER-106
→ Pessoa escolhe “Ver atualizações”
→ nenhum vínculo ou leitura é alterado pelo clique
→ PER-107
→ Pessoa compreende origem, natureza, autoridade, leitura, ação e prazo
→ retorna sem consequência oculta
```

A UXA-094 valida `GKR-TRN-110` ponta a ponta no escopo documental.

Regras:

- abrir/reabrir a Central não marca itens como lidos;
- leitura não responde solicitação, aceita convite, confirma presença, concorda com decisão ou conclui tarefa;
- ação substantiva revalida estado canônico;
- cartão obsoleto não prevalece sobre atualização mais recente;
- repetição de abertura/leitura não duplica efeito;
- segurança material precede ação comum;
- preferências não essenciais não ocultam aviso essencial além do limite de segurança.

## 5. Decisões e proteções

- compartilhar pouco permanece legítimo;
- solicitação não equivale a aprovação;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- pausa não reduz reputação;
- aprovação não cria função, autoridade, notificação ou presença obrigatória;
- `Meus Coletivos` não utiliza ranking, pontuação de dedicação ou comparação;
- a Central não é feed social único;
- `lido` não equivale a consentimento ou efeito substantivo;
- alertas de segurança exigem risco material e autoridade identificada;
- recusa, cancelamento e expiração são eventos distintos;
- transições ausentes permanecem explicitamente registradas.

## 6. Estado da vista

Esta vista permanece `draft` porque:

- compreensão inicial → Tela Hoje não foi validada como conjunto;
- `PER-108` permanece sem materialização vigente;
- `TRN-111` continua ausente;
- estados P0B adicionais de `PER-106` e `PER-107` permanecem separados;
- outras continuidades da jornada pessoal ainda não foram examinadas ponta a ponta.

O status `draft` não invalida referências locais e handoffs específicos já validados.

## 7. Próxima evolução possível

A próxima frente autorizável para Coletivos é **UXA-095 — Materialização/Reformulação Controlada do Início do Participante (`GKR-SURF-PER-108`) e Refinamento de `GKR-TRN-111`**.

A UXA-095 não foi iniciada.
