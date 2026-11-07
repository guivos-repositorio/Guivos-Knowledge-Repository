---
title: "Círculos de Possibilidades — Dossiê de Fronteiras Arquiteturais"
status: candidate
version: "0.5.0"
owner: "Direção Guivos — diagnóstico; propriedade canônica pendente"
last_updated: "2026-11-06"
normative: false
---

# Círculos de Possibilidades — Dossiê Único de Fronteiras Arquiteturais

> A direção acolheu o dossiê v0.5.0 **como diagnóstico documental condicionado**, não como decisão canônica. A publicação da categoria facilita consulta e transferência de contexto; não adjudica precedência ou autoridade, nem autoriza implantação.

## 1. Conclusão focal

A Fundação da Guivos admite fortalecimento de conexões e Próximos Passos que podem envolver conversas sem Oportunidade externa. Pessoa é participante já existente. Os contratos transversais admitem interação **mediada por objeto compartilhado autorizado**, sem atribuir relação social permanente ou canal genérico Pessoa↔Pessoa.

**Não foi comprovada cobertura contratual integral** de criação de círculo, chat, ingressos, moderação, notificações, retenção ou iniciativa automatizada. A existência de conceitos próximos não permite presumir autorização operacional.

## 2. Fronteira A — Autoridade do objeto Círculo

Questão reservada: a quem pertence a definição canônica do objeto temporário, sua identidade funcional, ciclo de vida, estados e exceções?

- [ADR-003](../../adr/ADR-003-architectural-ownership.md) exige **uma única arquitetura proprietária** para ativo canônico; a propriedade não pode ser atribuída unilateralmente.
- Círculo é proposto como **objeto contextual temporário**, **não** nova categoria de Participante, Coletivo ou novo produto.
- Estados `Em configuração`, `Ativo`, `Encerrado` são **descrições candidatas**, não estados registrados oficialmente.
- Prazos conceituais são 3, 7, 14 e 30 dias; prorrogação, início de contagem, mudança de organizador, extensão e retenção não estão contratados.
- Não criar IDs oficiais, superfícies PER ou transições GKR-TRN por inferência.

**Decisão pendente:** propriedade formal e contrato do objeto, sem alterar ADR-003.

## 3. Fronteira B — Interações, permissões e proteção

O [contrato de Relações e Interações](../participant-relationships-interactions-visibility-contract.md) v0.3.0 distingue co-presença contextual legítima de relação social bilateral autônoma não adjudicada. Ele explicita que não cria, sozinho, mensagens, convites, vínculos, permissões ou transições.

O [contrato de Comunicações](../communications-notifications-cross-ecosystem-contract.md) v0.4.0 permite eventos dirigidos a Pessoas autorizadas por um objeto, mas não cria DM ou canais externos de alerta por inferência.

**Comportamentos candidatos dependentes de contrato:** conversa coletiva, audiência, três modalidades de ingresso, convite por link encaminhável, visibilidade de círculo distinta de visibilidade do link principal, denúncia, banimento limitado ao círculo, intervenção de segurança Guivos, bloqueio de retorno de banidos, encerramento e tratamento do histórico.

Não criar feed social, amizade, seguidores, contatos persistentes, mensagens privadas automáticas ou canal externo de alerta sem autorização própria.

**Decisão pendente:** delimitação explícita do objeto comunicacional, permissões, moderação, privacy-by-default e eventos.

## 4. Fronteira C — Iniciativa do Guivos Intelligence

A autoridade de [Guivos Intelligence](../../product-architecture/intelligence.md) reconhece compreensão e recomendação, sem transferir decisão humana. O documento no repositório apresenta front matter v2.0.3, mas o próprio corpo identifica **GPA-006 v2.0.2 como autoridade vigente**; preservar essa decisão.

A Intelligence pode ser considerada para sugerir convergências e círculos. **Não se presume** que possa criar em nome de Pessoas, atribuir organizador automaticamente, inscrever participantes, enviar convites sem permissão ou revelar Jornada privada.

**Decisão pendente:** finalidade, dados permitidos, consentimento, iniciativa, responsabilidade, convites e aceite humano.

## 5. Autoridades e consultas necessárias

| Fonte | Função e limite |
|---|---|
| [ADR-003](../../adr/ADR-003-architectural-ownership.md) | Propriedade única de cada ativo canônico |
| [Glossário](../../glossary.md) | Pessoa, Participante, Coletivo e Papel; não modificar definições |
| [Fundação](../../geb/part-01-foundation/01-essence.md) | Autonomia, conexões e distinção entre Possibilidade/Oportunidade/Experiência |
| [Pessoa](../../participants/person.md) | Participação e contexto, sem presumir vínculo por co-presença |
| [Relações e Interações](../participant-relationships-interactions-visibility-contract.md) | Mediação contextual, não DM ou relação social autônoma |
| [Comunicações e Notificações](../communications-notifications-cross-ecosystem-contract.md) | Evento/objeto/destinatário autorizado, sem canais automáticos |
| [Domínios](../../product-architecture/pas-001-evolution-domains-model.md) | Taxonomia canônica JED-001–009, sem novas categorias |
| [Reconciliação de Domínios](../../product-architecture/pas-001-evolution-domains-semantic-reconciliation.md) | Uso transversal sem redefinição |
| [PAS-001 Experiências](../../product-architecture/pas-001-experiencias-fundamentos-iniciais.md) | Vivência efetiva ≠ participação/impacto presumidos |
| [PAS-001 Oportunidades Ativas](../../product-architecture/pas-001-oportunidades-ativas-fundamentos-iniciais.md) | Admissão contextual, não equivalência automática |
| [Surface Registry](../../journeys/surface-registry.md) | Não contém superfícies de círculo promovidas por este dossiê |
| [Transition Registry](../../journeys/transition-registry.md) | Não contém transições de círculo promovidas por este dossiê |

## 6. Matriz de decisões

| Questão | Estado |
|---|---|
| Nova categoria de participante ou novo produto | Não proposta |
| Uso de Pessoa e Papel contextual | Compatível em princípio |
| Interação mediada por objeto compartilhado | Fundamento identificado, contrato específico pendente |
| Propriedade canônica de Círculo | Não adjudicada |
| Conversas, convites e ingresso | Direção conceitual definida; contrato pendente |
| Taxonomia de Domínios de Evolução | Reutilização conceitual, integração pendente |
| Intelligence como proponente | Compatível em princípio; iniciativa autorizada pendente |
| Retenção e segurança operacionais | Não contratadas |
| Replit, Design, APIs, teste e publicação operacional | Não autorizados por este dossiê |

## 7. Orientação para continuidade

Um próximo exame pode submeter **somente as três fronteiras** às arquiteturas competentes, sem prolongar pareceres genéricos. Não criar novos IDs, adjudicar propriedade, declarar implementação, homologar prazos de retenção ou transformar a documentação candidata em contrato canônico por leitura da sua publicação.

[Leia Primeiro](read-first.md) · [Modelo Funcional](modelo-funcional.md)
