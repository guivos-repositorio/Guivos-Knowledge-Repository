---
id: PAS-001-CC-W0-01-EVIDENCE-001
title: Contrato de Evidências e Armazenamento do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-CHARTER-001
related:
  - PAS-001-CC-W0-EVIDENCE-001
  - PAS-001-CC-W0-01-OWNERS-001
  - PAS-001-CC-W0-01-PIPELINE-001
---

# PAS-001-CC-W0-01-EVIDENCE-001 — Contrato de Evidências e Armazenamento

## 1. Objetivo

Definir como o W0-01 produzirá, validará, armazenará e referenciará evidências sem transformar relatórios informais, screenshots isolados ou ausência de incidente em comprovação.

## 2. Evidências prioritárias

| Evidência | Uso no W0-01 |
|---|---|
| EV-017 | owners, riscos, exceções, política de dados e prontidão das dependências |
| EV-018 | ADRs, decisões, repositório, branch protection, pipeline e governança |

Checks de segredo, dados sintéticos e políticas poderão gerar artefatos auxiliares vinculados a EV-017/018.

## 3. Manifesto obrigatório

```yaml
evidence_id: string
requirement_ids: string[]
implementation_version: string
environment: repository_governed | local | test
executed_at: datetime
owner: string
approver: string
method_reference: string
configuration_reference: string
data_set_reference: string | null
expected_result: object
observed_result: object
status: passed | failed | accepted_exception | not_measured | expired
exceptions: string[]
artifact_references: string[]
valid_until: datetime | null
integrity_hash: string
```

## 4. Estrutura proposta

```text
evidence/
├── templates/
│   ├── evidence.schema.yaml
│   ├── evidence.example.yaml
│   └── gate-report.template.md
├── manifests/
│   └── index.yaml
└── W0-01/
    ├── EV-017/
    └── EV-018/
```

## 5. Separação por responsabilidade

| Local | Conteúdo permitido |
|---|---|
| GKR | autoridade, critérios, versão, hash, conclusão e referências |
| repositório de implementação | manifestos, relatórios não sensíveis e artefatos pequenos |
| armazenamento privado futuro | artefatos grandes, restritos ou adversariais |
| logs do pipeline | apenas resultado minimizado e referência |

O GKR não deverá receber credencial, log bruto, payload sensível, mídia, vetor explorável ou artefato operacional desnecessário.

## 6. Validade

| Evidência | Validade no W0-01 |
|---|---|
| atribuição de owners | até mudança de pessoa, autoridade ou acesso |
| branch protection | até mudança de configuração |
| pipeline | até mudança material de workflow, stack ou política |
| política sintética | até mudança de gerador ou regra |
| ADR | até supersessão ou condição de revisão |
| risco/exceção | até revisão, expiração ou encerramento |

Evidência expirada equivale a `not_measured` para decisão obrigatória.

## 7. Integridade

- manifesto e artefato deverão possuir hash;
- commit SHA deverá ser registrado;
- método deverá ser reproduzível;
- resultado falho não poderá ser removido;
- nova execução supersede, não apaga;
- configuração deverá ser referenciada;
- conteúdo sensível deverá ser redigido;
- aprovador deverá ser competente e diferente do único produtor quando o controle for crítico.

## 8. Método de produção

Cada evidência deverá registrar:

1. requisito;
2. preparação;
3. ambiente;
4. configuração;
5. dataset sintético quando aplicável;
6. comando ou procedimento;
7. resultado esperado;
8. resultado observado;
9. artefatos;
10. hash;
11. owner;
12. aprovador;
13. exceções;
14. validade.

## 9. Status

- `passed`: requisito comprovado no escopo;
- `failed`: comportamento incompatível;
- `accepted_exception`: falha formalmente aceita, com prazo;
- `not_measured`: execução ausente ou inválida;
- `expired`: validade encerrada.

Regras:

- `failed`, `not_measured` e `expired` bloqueiam item obrigatório;
- exceção sem owner, risco, prazo ou aprovador é inválida;
- ausência de incidente não é `passed`;
- screenshot sem método e hash não é evidência suficiente.

## 10. Pacote EV-017

Deverá incluir:

- matriz de owners;
- autoridades de interrupção;
- registro inicial de riscos;
- exceções vigentes;
- política de dados sintéticos;
- resultado da varredura de dados;
- inventário de dependências `required_before_build`;
- status e bloqueios;
- validade e hash.

## 11. Pacote EV-018

Deverá incluir:

- ADR-TCC-001 e ADR-TCC-006;
- recortes aprovados de ADR-TCC-008 e ADR-TCC-010;
- configuração do repositório;
- branch protection;
- CODEOWNERS;
- templates de PR;
- pipeline mínimo;
- execução válida e falha deliberada;
- decisão de encerramento do W0-01;
- hash e versão.

## 12. Evidência de configuração GitHub

Não basta screenshot. O pacote deverá conter:

- exportação ou registro estruturado da configuração;
- branch e commit de referência;
- checks exigidos;
- regra de aprovação;
- teste de push direto bloqueado;
- teste de PR bloqueado por falha;
- data e executor;
- resultado observado;
- hash do relatório.

## 13. Acesso

- menor privilégio;
- evidência de segurança segregada;
- artefato adversarial com acesso restrito;
- owner e aprovador com acesso compatível;
- retenção limitada à finalidade;
- compartilhamento externo proibido por padrão;
- remoção de acesso não elimina trilha mínima de decisão.

## 14. Critérios de aceite

O contrato estará executado quando:

- schema estiver versionado;
- exemplo válido e inválido existirem;
- pipeline validar manifestos;
- EV-017 e EV-018 forem produzidos;
- resultados falhos permanecerem rastreáveis;
- hashes forem verificáveis;
- GKR contiver referências e conclusão, não artefatos sensíveis;
- owners e aprovadores forem competentes;
- evidências puderem ser reproduzidas.

## 15. Limites

Este documento não produz EV-017 ou EV-018. Ele define o contrato para a execução autorizada do W0-01.
