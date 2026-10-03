---
id: PAS-001-CC-W0-EVIDENCE-001
title: Plano de Evidências da Onda 0 da Captura de Contexto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-W0-PLAN-001
related:
  - PAS-001-CC-UIC-READINESS-001
  - PAS-001-CC-W0-BACKLOG-001
  - PAS-001-CC-W0-POC-001
---

# PAS-001-CC-W0-EVIDENCE-001 — Plano de Evidências da Onda 0

## 1. Objetivo

Definir como cada incremento produz comprovação reproduzível para os gates de domínio, dados, segurança, qualidade e governança.

Documento, screenshot isolado, afirmação verbal ou ausência de incidente não constituem evidência suficiente.

## 2. Estrutura obrigatória

Cada evidência deverá conter:

```yaml
evidence_id: string
requirement_ids: string[]
implementation_version: string
environment: local | test | integration | security_lab | performance_lab | internal_trial
executed_at: datetime
owner: string
approver: string
method_reference: string
configuration_reference: string
data_set_reference: string
expected_result: object
observed_result: object
status: passed | failed | accepted_exception | not_measured | expired
exceptions: string[]
artifact_references: string[]
valid_until: datetime | null
integrity_hash: string
```

## 3. Matriz EV-001 a EV-018

| ID | Requisito | Incremento produtor | Ambiente mínimo | Artefato esperado | Gate |
|---|---|---|---|---|---|
| EV-001 | invariantes do agregado | W0-02 | Test | relatório por invariante e cobertura | domínio |
| EV-002 | transições e replay | W0-02 | Test | matriz de transições válidas/inválidas | domínio |
| EV-003 | contratos e schemas | W0-03 | Test/Integration | matriz produtor-consumidor e fixtures | domínio |
| EV-004 | isolamento e escopo | W0-05/W0-07 | Integration/Security Lab | relatório de zero acesso cruzado | segurança |
| EV-005 | logs seguros | W0-07 | Test/Security Lab | varredura de logs e regras de redaction | segurança |
| EV-006 | revogação | W0-05/W0-07 | Integration/Performance Lab | latência, bloqueio e confirmações | segurança/dados |
| EV-007 | correção | W0-03/W0-05 | Integration | estado atual, histórico e aplicação | domínio |
| EV-008 | backup, restore e replay | W0-04/W0-07 | Integration/Performance Lab | RPO/RTO e não reativação | dados |
| EV-009 | mídia protegida | W0-04 | Security Lab | quarentena, integridade e acesso | dados/segurança |
| EV-010 | busca protegida | W0-06 | Integration/Security Lab | isolamento, redaction e reconstrução | dados |
| EV-011 | prompt injection | W0-07 | Security Lab | suíte adversarial e resultados | segurança |
| EV-012 | acesso administrativo | W0-05 | Security Lab/Internal Trial | trilha JIT e auditoria | governança |
| EV-013 | SLIs e SLOs | W0-07 | Performance Lab | relatório p50/p95/p99 e orçamento | qualidade |
| EV-014 | consumidores | W0-05 | Integration | contrato, ack funcional e kill switch | domínio |
| EV-015 | compatibilidade | W0-03 | Test/Integration | matriz de versões e quarentena | qualidade |
| EV-016 | retenção e exclusão | W0-04/W0-06 | Integration | evidência por camada e derivado | dados |
| EV-017 | riscos e exceções | W0-01/W0-08 | repositório governado | registro aprovado e vigente | governança |
| EV-018 | ADRs e decisões | W0-01/W0-08 | repositório governado | dossiers, decisão e revisão | governança |

## 4. Evidências por incremento

### W0-01

- template validado;
- matriz de owners;
- registro de riscos;
- registro de decisões;
- política de dados sintéticos;
- pipeline inicial.

### W0-02

- relatório de invariantes;
- matriz de transições;
- cobertura de erros;
- replay sem novos fatos;
- confirmação restrita à autoridade humana.

### W0-03

- contratos executáveis;
- fixtures válidas e inválidas;
- concorrência;
- idempotência;
- publicação pós-persistência;
- compatibilidade.

### W0-04

- separação de conteúdo;
- integridade;
- quarentena;
- retenção;
- exclusão;
- restore;
- rotação de chave.

### W0-05

- decisões de acesso;
- isolamento;
- correção;
- revogação;
- consumidores;
- acesso administrativo.

### W0-06

- política de índice;
- filtro pré-recuperação;
- snippets;
- remoção após revogação;
- atualização após correção;
- reconstrução.

### W0-07

- logs seguros;
- testes adversariais;
- SLIs;
- carga;
- recuperação;
- runbooks.

### W0-08

- pacote final EV-001 a EV-018;
- relatórios de gates;
- exceções;
- riscos residuais;
- decisão de conclusão.

## 5. Validade

| Tipo | Validade padrão |
|---|---|
| domínio determinístico | até mudança material no domínio ou implementação |
| contrato/schema | até mudança de versão ou política de compatibilidade |
| segurança adversarial | até mudança material ou 90 dias, o que ocorrer primeiro |
| carga/SLO | até mudança material de infraestrutura ou perfil de carga |
| restore/RPO/RTO | 90 dias no ciclo de Onda 0 |
| acesso administrativo | até mudança de política ou mecanismo |
| risco/ADR | até revisão ou supersessão formal |

## 6. Integridade e armazenamento

- evidência deve possuir hash;
- artefato bruto e relatório devem ser vinculados;
- resultado falho não pode ser removido;
- nova execução supersede, não apaga;
- conteúdo sensível deve ser redigido;
- acesso ao artefato segue finalidade;
- evidência de segurança não deve publicar vetor explorável sem necessidade;
- logs de evidência não se tornam fonte de dados humanos.

## 7. Status

- `passed`: requisito comprovado no escopo;
- `failed`: resultado incompatível;
- `accepted_exception`: falha aceita formalmente com prazo;
- `not_measured`: execução ausente ou inválida;
- `expired`: validade encerrada.

Regras:

- `failed` bloqueia o gate;
- `not_measured` bloqueia item obrigatório;
- `expired` equivale a `not_measured`;
- exceção exige owner, risco, mitigação, prazo e aprovador;
- um gate não compensa outro.

## 8. Pacote de gate

Cada gate deverá receber:

- lista de requisitos;
- evidências vinculadas;
- status por requisito;
- falhas;
- exceções;
- riscos residuais;
- parecer do owner;
- decisão do aprovador;
- data e versão;
- condição de revalidação.

## 9. Gate de domínio

Evidências mínimas:

- EV-001;
- EV-002;
- EV-003;
- EV-007;
- EV-014.

## 10. Gate de dados

Evidências mínimas:

- EV-006;
- EV-008;
- EV-009;
- EV-010;
- EV-016.

## 11. Gate de segurança

Evidências mínimas:

- EV-004;
- EV-005;
- EV-006;
- EV-009;
- EV-011;
- EV-012;
- EV-014.

## 12. Gate de qualidade

Evidências mínimas:

- EV-003;
- EV-008;
- EV-013;
- EV-015.

## 13. Gate de governança

Evidências mínimas:

- EV-012;
- EV-017;
- EV-018;
- relatório consolidado dos demais gates.

## 14. Critérios de aceite do pacote final

O pacote final é aceitável somente quando:

- todas as EV obrigatórias existem;
- hashes são verificáveis;
- versões e ambientes são explícitos;
- métodos são reproduzíveis;
- exceções estão vigentes;
- riscos possuem owner;
- nenhuma evidência depende de conteúdo proibido;
- nenhum resultado foi omitido;
- aprovadores são competentes;
- produção não foi implicitamente autorizada.

## 15. Decisão de conclusão

A conclusão da Onda 0 exige decisão separada contendo:

- versão da implementação;
- status dos cinco gates;
- exceções vigentes;
- riscos residuais;
- limitações;
- itens deferred;
- recomendação;
- próxima decisão autorizada;
- declaração explícita de que conclusão da Onda 0 não equivale a go-live.