---
id: GKR-JOURNEY-PERSON-001
title: Jornada Integrada da Pessoa
status: draft
version: 0.10.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-07
related:
  - UXA-002
  - UXA-006
  - UXA-010
  - UXA-020
  - UXA-023
  - UXA-036
  - UXA-037
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
  - UXA-096
  - UXA-097
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
→ TRN-007 integralmente validada
→ primeira Tela Hoje
→ experiência recorrente e continuidades autorizadas
```

A UXA-097 valida integralmente a continuidade `PER-007 → PER-008`. A primeira variante de Hoje não presume avanço, mudança anterior, urgência ou conteúdo comercial e usa somente condição confirmada, autorizada e vigente.

A jornada completa permanece `draft`: `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda não estão validadas ponta a ponta.

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
| Central de Atualizações | validado | UXA-093/094/095/096 | UXA-094; versão corrente UXA-096 | TRN-110 e TRN-111 integralmente validadas |
| Início do Participante | validado | UXA-095/096 | UXA-096 | TRN-111 integralmente validada |

## 3. Compreensão inicial → Hoje validada

```text
PER-007
→ pessoa confirma escolhas compatíveis
→ persistência e personalização assumem somente o estado explicitamente escolhido
→ TRN-007
→ PER-008 consulta o estado canônico vigente
→ primeira Tela Hoje não conta a própria transição como avanço
```

Regras da UXA-097:

- personalização autorizada utiliza somente base confirmada, autorizada e vigente;
- `Continuar sem personalização` ou `Decidir depois` não bloqueiam Hoje, mas omitem indicações pessoais;
- `Excluir compreensão e continuar explorando` não pertence a `TRN-007`;
- estado obsoleto, retirada ou exclusão prevalecem sobre a renderização anterior;
- repetir, recarregar ou voltar não duplica efeito lógico nem cria avanço.

## 4. Continuidade pós-aprovação validada

`COL-003 → PER-105 aprovado → PER-106` permanece integralmente validada em `GKR-TRN-108`.

## 5. Meus Coletivos → Central validada

`PER-106 → Ver atualizações → PER-107` permanece integralmente validada em `GKR-TRN-110`.

## 6. Central → Início validada

```text
PER-107
→ Pessoa escolhe “Abrir início do Coletivo”
→ vínculo atual e permissão são revalidados
→ histórico não preserva acesso
→ nenhum vínculo, leitura, papel, presença ou autoridade é alterado
→ PER-108
→ mesmo Coletivo e vínculo lógico permanecem em contexto
```

`GKR-TRN-111` permanece integralmente validada pela UXA-096.

## 7. Proteções preservadas

- conclusão da compreensão inicial não equivale a avanço humano;
- personalização não é condição para acessar Hoje;
- compartilhar pouco permanece legítimo;
- acompanhar não equivale a participar;
- convite não cria vínculo;
- pausa não reduz reputação;
- aprovação não cria função, autoridade ou presença obrigatória;
- `Meus Coletivos` não utiliza ranking ou pontuação de dedicação;
- a Central não é feed social único;
- `lido` não equivale a consentimento ou efeito substantivo;
- evento histórico não concede acesso interno;
- abrir o Início não confirma presença, disponibilidade ou função;
- consulta não cria obrigação de resposta nem autoridade;
- `PER-108` sintetiza e encaminha para áreas próprias, sem replicá-las;
- estado canônico vigente prevalece sobre renderização anterior.

## 8. Estado da vista

Esta vista permanece `draft` porque:

- `TRN-001`, `TRN-003`, `TRN-004` e `TRN-005` ainda são parciais;
- estados P0B adicionais permanecem separados;
- áreas internas especializadas a partir de `PER-108` não foram validadas como conjunto;
- outras continuidades da jornada pessoal ainda não foram examinadas ponta a ponta.

O status `draft` não invalida referências locais e handoffs específicos já validados.

## 9. Próxima evolução possível

Com `V1 — compreensão inicial → Tela Hoje` fechada, a fila vigente passa a iniciar por `V2 — publicação → descoberta/mapa/lista/detalhe`. **UXA-098 não foi iniciada.**