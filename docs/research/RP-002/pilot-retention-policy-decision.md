---
id: RP-002-PILOT-RETENTION-DEC-001
title: Piloto — Decisão de Retenção e Eliminação A10
status: active
version: 1.0.0
owner: Guivos Research
last_updated: 2026-08-27
normative: false
parent: RP-002
maturity: retention_target_approved_pending_final_review
related:
  - RP-002-PILOT-DOC-CLOSE-001
  - RP-002-PILOT-DATA-LAW-001
  - RP-002-PILOT-IDENTITY-VAULT-DEC-001
  - RP-002-PILOT-RESEARCH-BASE-DEC-001
  - RP-002-PILOT-LINKAGE-KEY-DEC-001
  - RP-002-PILOT-BACKUP-RECOVERY-DEC-001
  - RP-002-PILOT-OPENAI-API-DEC-001
---

# Piloto — Decisão de Retenção e Eliminação A10

## 1. Finalidade

Este documento define os prazos-alvo de retenção e eliminação do primeiro Dry Run Real `N=1` do `RP-002`.

Os prazos são uma decisão interna proporcional ao piloto. Eles não são apresentados como prazos fixos impostos pela LGPD.

A revisão final A12 poderá exigir ajuste antes de Pessoa real. Qualquer ajuste deve ser versionado antes do Notice final.

## 2. Base de governança

A LGPD estabelece término do tratamento quando a finalidade é alcançada, quando os dados deixam de ser necessários/pertinentes, ao fim do período de tratamento, por manifestação do titular nos casos aplicáveis ou por determinação da autoridade.

Após o término, a conservação somente pode permanecer nas hipóteses legais aplicáveis.

A ANPD também esclarece que a LGPD não fixa um único prazo geral de tratamento: o prazo depende da finalidade e das circunstâncias.

Fontes oficiais verificadas em 2026-08-27:

- LGPD, arts. 15 e 16: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm>
- FAQ ANPD sobre tempo de tratamento: <https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes/perguntas-frequentes>
- Direitos dos titulares: <https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares>

Princípio adotado:

> **reter somente pelo tempo necessário à finalidade documentada e eliminar de forma controlada quando a necessidade termina.**

## 3. Marco temporal principal

Para participantes efetivamente admitidos, o marco `PARTICIPANT_CLOSURE` é a data em que ocorrer primeiro o encerramento formal do ciclo individual após o último follow-up previsto ou a desistência/revogação que encerre a participação.

Para pessoas não admitidas, o marco é `RECRUITMENT_CLOSURE`.

Para o ciclo de Research agregado, `PILOT_CYCLE_CLOSURE` é o encerramento formal do ciclo metodológico correspondente.

## 4. Matriz de retenção-alvo

| Classe | Prazo-alvo | Marco | Destino |
|---|---:|---|---|
| candidato não selecionado / contato de recrutamento | 30 dias | `RECRUITMENT_CLOSURE` | excluir |
| dados operacionais do participante no Identity Vault | 90 dias | `PARTICIPANT_CLOSURE` | excluir, salvo obrigação/necessidade válida documentada |
| Linkage Key | 90 dias no máximo | `PARTICIPANT_CLOSURE` | excluir a ligação; preferir antes quando não mais necessária |
| Research Base pseudonimizada | 12 meses | `PILOT_CYCLE_CLOSURE` | excluir ou anonimizar de forma efetiva para conhecimento agregado |
| prova mínima de Notice/consentimento/revogação | 24 meses | `PARTICIPANT_CLOSURE` | excluir ao fim, salvo obrigação/defesa jurídica específica revisada |
| registro mínimo de solicitação de direitos | 24 meses | fechamento da solicitação | excluir ao fim, salvo necessidade legal específica |
| logs mínimos de segurança/governança sem conteúdo rico | 90 dias | evento | excluir/rotacionar |
| backup recuperável de dado excluído do primário | até 30 dias adicionais | exclusão no primário | expirar na rotação seguinte, no máximo em 30 dias |
| dado sensível incidental desnecessário | sem retenção deliberada | identificação | eliminar assim que tecnicamente possível, target até 24h |
| áudio/vídeo | `OFF` | n/a | não coletar por padrão |
| transcrição bruta identificável | `OFF / PROHIBITED BY DEFAULT` | n/a | não criar por padrão |
| conhecimento efetivamente anonimizado/agregado | sem prazo do piloto | após anonimização efetiva | pode ser preservado como conhecimento não pessoal, sujeito a revisão de risco de reidentificação |

## 5. Candidatos não admitidos

Se uma Pessoa demonstrar interesse mas não entrar no Dry Run:

```text
MINIMUM RECRUITMENT DATA
→ retain up to 30 days after closure
→ then delete
```

Não manter lista de leads para marketing a partir do piloto.

Contato futuro fora do ciclo exige finalidade e base próprias.

## 6. Identity Vault

O Identity Vault serve à operação e aos direitos durante o ciclo e por janela curta após o fechamento.

Target:

```text
IDENTITY VAULT
→ 90 days after PARTICIPANT_CLOSURE
```

A janela existe para reconciliar follow-up final, correções, revogação e fechamento técnico.

Se a identidade deixar de ser necessária antes, a eliminação pode ser antecipada.

## 7. Linkage Key

```text
LINKAGE KEY
→ no longer than Identity Vault retention
→ target maximum 90 days after PARTICIPANT_CLOSURE
```

Preferir remoção anterior quando não houver mais necessidade legítima de reidentificação.

A exclusão da Linkage Key reduz capacidade de reidentificação, mas não deve ser chamada de anonimização automática sem análise do restante do dataset.

## 8. Research Base pseudonimizada

Target:

```text
PSEUDONYMIZED RESEARCH BASE
→ 12 months after PILOT_CYCLE_CLOSURE
```

Justificativa metodológica:

- permitir análise do ciclo;
- comparar episódios;
- observar follow-up e New Momento;
- identificar padrões e contraexemplos;
- produzir decisão GO / REVISE / STOP;
- evitar retenção indefinida do dossiê individual.

Antes do término, avaliar se o conhecimento pode ser convertido em forma efetivamente anonimizada/agregada.

## 9. Prova mínima de Notice e consentimento

Target:

```text
NOTICE / CONSENT / WITHDRAWAL PROOF
→ 24 months after PARTICIPANT_CLOSURE
```

O registro deve ser mínimo:

- versão do Notice;
- status da manifestação;
- timestamp;
- referência mínima ao participante;
- revogação/fechamento quando aplicável.

Não manter o dossiê rico apenas para provar consentimento.

A12 deverá revisar se existe obrigação jurídica ou necessidade de defesa que exija prazo diferente antes do uso real.

## 10. Direitos do titular

Registro mínimo de solicitação e resposta:

```text
RIGHTS REQUEST MINIMUM LOG
→ 24 months after request closure
```

Conteúdo desnecessário da solicitação deve ser minimizado.

O prazo documental não autoriza reter anexos identificáveis por 24 meses se não forem necessários à prova do atendimento.

## 11. Backups

A exclusão deve alcançar cópias recuperáveis conforme rotação tecnicamente viável.

Target:

```text
PRIMARY DELETION
→ immediate according to approved event

RECOVERABLE BACKUP RESIDUAL WINDOW
→ maximum 30 additional days
```

Se um backup for restaurado dentro dessa janela, exclusões e revogações conhecidas devem ser reaplicadas antes da retomada do uso.

## 12. OpenAI API

A retenção do operador externo não é substituída pela política interna.

A documentação oficial da OpenAI verificada em 2026-08-27 informa que abuse monitoring logs podem reter conteúdo do cliente por até 30 dias por padrão, e que application state depende do endpoint/capability.

Target do piloto:

- não presumir ZDR;
- desabilitar persistência voluntária quando aplicável;
- não usar estado persistente por padrão;
- não enviar identidade direta;
- registrar no Notice a existência de processamento externo e retenção relevante do operador aprovado.

Fonte:

<https://platform.openai.com/docs/models/default-usage-policies-by-endpoint>

## 13. Revogação / solicitação de eliminação

Quando aplicável:

```text
NEW CONSENT-BASED PROCESSING
→ STOP

IDENTITY / LINKAGE / RESEARCH
→ evaluate and delete/anonymize as applicable

LEGAL CONSERVATION EXCEPTION
→ only if documented and applicable
```

A existência de prazo máximo nesta política não impede eliminação anterior por revogação, desnecessidade ou exercício de direito.

## 14. Dado sensível incidental

Se informação sensível surgir sem necessidade de persistência:

```text
PERSISTENCE
→ NO

DELETION TARGET
→ as soon as technically possible
→ operational target within 24 hours after identification
```

Se o dado já estiver em nota de trabalho, a nota deve ser sanitizada ou substituída conforme o caso.

## 15. Anonimização

Somente chamar material de anonimizado quando a reidentificação não for razoavelmente possível considerando meios disponíveis e o contexto.

Pseudônimo não equivale a anonimização.

Conhecimento agregado pode ser preservado fora dos prazos de dados pessoais apenas quando a anonimização for efetiva e não houver ligação reversível mantida.

## 16. Hold legal

Se houver obrigação legal, incidente, disputa ou necessidade concreta de preservação, a eliminação poderá ser suspensa somente para o escopo necessário.

```text
LEGAL HOLD
→ exception
→ documented reason
→ minimum scope
→ reviewed duration
```

Não existe hold genérico preventivo para todo o piloto.

## 17. Teste futuro

A7 deverá testar, com dados sintéticos, se os componentes permitem executar esta política, incluindo:

- localizar por pseudônimo;
- corrigir;
- excluir no primário;
- remover Linkage Key;
- verificar backup/residual window;
- confirmar ausência de cópia deliberada fora do boundary.

## 18. Estado documental de P3-D

A existência de prazos-alvo permite avançar documentalmente, mas P3-D não deve ser promovido para `PASS` antes de:

- A12 revisar os prazos;
- A11 refletir corretamente os períodos;
- stack real demonstrar que a política é executável.

```text
P3-D DOCUMENTATION
→ TARGET DEFINED

P3-D OPERATIONAL / FINAL
→ HOLD
```

## 19. Estado final

```text
A10 DOCUMENTATION
→ TARGET CLOSED PENDING A12 FINAL REVIEW

A10 OPERATIONAL ENFORCEMENT
→ HOLD

A11 FINAL NOTICE
→ MAY NOW BE RECONCILED DOCUMENTALLY

P3-D
→ HOLD

P4
→ HOLD

PARTICIPANT 001
→ HOLD
```
