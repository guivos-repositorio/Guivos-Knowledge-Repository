---
id: PAS-001-CC-W0-01-PIPELINE-001
title: Contrato do Pipeline Mínimo do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-CHARTER-001
related:
  - PAS-001-CC-W0-01-REPO-001
  - PAS-001-CC-W0-01-SYNTHETIC-DATA-001
  - PAS-001-CC-W0-01-EVIDENCE-001
---

# PAS-001-CC-W0-01-PIPELINE-001 — Contrato do Pipeline Mínimo

## 1. Objetivo

Definir o conjunto mínimo de validações obrigatórias para alterações do repositório de implementação, sem pressupor linguagem, fornecedor de nuvem ou topologia definitiva.

## 2. Princípios

- falha de requisito obrigatório bloqueia merge;
- pipeline não amplia autoridade;
- check aprovado não equivale a gate concluído;
- execução é reproduzível;
- resultados são vinculados ao commit;
- nenhum log contém segredo ou conteúdo sensível bruto;
- fixtures são sintéticas;
- checks não podem ser ignorados por conveniência;
- exceção possui owner, risco, validade e aprovador.

## 3. Camada independente da stack

Deverá estar disponível antes do ADR-TCC-001:

| Check | Objetivo | Bloqueia merge |
|---|---|---:|
| `governance-validation` | validar IDs, referências, manifests e arquivos obrigatórios | sim |
| `markdown-yaml-validation` | validar documentação operacional e configuração | sim |
| `secret-scan` | detectar credenciais, chaves e tokens | sim |
| `synthetic-data-scan` | detectar padrões de dados reais ou não permitidos | sim |
| `evidence-manifest` | validar schema dos manifests de evidência | sim |
| `link-reference-check` | validar referências internas e requisitos | sim |
| `license-dependency-policy` | impedir inclusão não aprovada de dependência ou licença | sim |
| `repository-policy-check` | validar templates, CODEOWNERS e proteções esperadas | sim |

## 4. Camada específica da stack

Ativada após ADR-TCC-001:

| Check | Requisito |
|---|---|
| `reproducible-install` | instalação por lockfile e versão fixa de runtime |
| `format` | formato determinístico |
| `lint` | regras estáticas aprovadas |
| `type-check-or-compile` | validação completa de tipos ou compilação |
| `unit-tests` | testes determinísticos do escopo |
| `schema-validation` | fixtures válidas e inválidas |
| `contract-tests` | produtor e consumidor compatíveis |
| `dependency-vulnerability-scan` | dependências conhecidas e riscos registráveis |
| `coverage-report` | cobertura por requisito, não apenas percentual agregado |
| `artifact-manifest` | versão, hash, dependências e configuração |

## 5. Ordem do pipeline

```text
policy preflight
  ↓
secret and synthetic-data scans
  ↓
document/config validation
  ↓
install and static analysis
  ↓
unit/schema/contract tests
  ↓
evidence and artifact manifests
  ↓
merge eligibility report
```

Falha em etapa anterior impede promoção das etapas que poderiam expor ou publicar artefatos.

## 6. Matriz de branch protection

Checks obrigatórios propostos:

```text
governance-validation
secret-scan
synthetic-data-scan
schema-validation
static-analysis
unit-tests
contract-tests
evidence-manifest
```

Novos checks poderão ser adicionados; remoção ou relaxamento exige revisão de Architecture, Security/Privacy e Quality/Evidence conforme o impacto.

## 7. Ambientes e permissões

### Pull request de origem externa

- sem segredos;
- sem acesso a ambiente superior;
- sem publicação de artefato confiável;
- apenas fixtures sintéticas aprovadas.

### Branch interna

- acesso mínimo;
- credenciais específicas;
- nenhum segredo persistido no runner;
- logs redigidos;
- artefatos com retenção limitada.

### Main

- pode gerar artefato versionado da Onda 0;
- não implanta produção;
- não promove Internal Trial automaticamente;
- não usa dados reais.

## 8. Política de logs

É proibido registrar:

- conteúdo capturado;
- documentos, imagens, áudio ou transcrições;
- segredos ou tokens;
- identificadores pessoais reais;
- payload completo de autorização;
- material de teste adversarial reutilizável sem redaction.

Permitido:

- IDs sintéticos ou opacos;
- códigos de erro;
- duração;
- contagem;
- versão;
- hash;
- status do check;
- referência de requisito.

## 9. Artefatos e retenção

Cada execução deverá produzir:

- commit SHA;
- versão do workflow;
- versões de ferramentas;
- status por check;
- hashes dos artefatos;
- dataset sintético utilizado;
- exceções;
- tempo de execução;
- referência de evidência quando aplicável.

Retenção inicial:

| Artefato | Retenção proposta |
|---|---|
| logs de PR | 30 dias |
| relatórios de teste | 90 dias ou até supersessão |
| manifestos de evidência | versionados enquanto válidos |
| artefato de build da Onda 0 | 30 dias, salvo evidência vinculada |
| segredo detectado | nunca persistir; registrar somente ocorrência redigida |

## 10. Exceções

Uma exceção somente é válida quando:

- check não protege autoridade, isolamento, segredo ou dados reais;
- motivo é documentado;
- risco é registrado;
- owner e aprovador são competentes;
- validade é curta;
- compensação existe;
- remoção é planejada.

Não são excepcionáveis:

- segredo detectado;
- dado real não autorizado;
- vazamento cruzado;
- contrato incompatível produzindo efeito;
- alteração de autoridade;
- ausência de owner para risco critical.

## 11. Evidência do W0-01

O pipeline deverá produzir evidência contendo:

- configuração dos workflows;
- branch protection;
- execução válida;
- execução deliberadamente falha;
- bloqueio de merge comprovado;
- zero segredo persistido;
- zero dado real;
- hash e versões;
- aprovadores.

## 12. Critérios de aceite

O contrato estará executado quando:

1. checks independentes da stack estiverem ativos;
2. checks da stack escolhida estiverem ativos;
3. `main` exigir os checks;
4. falha impedir merge;
5. logs respeitarem minimização;
6. artefatos possuírem hash;
7. resultado puder ser reproduzido;
8. exceções forem governadas;
9. nenhum workflow implantar produção.

## 13. Limites

Este documento não cria workflow, runner, segredo ou ambiente. GitHub Actions é a plataforma operacional inicial recomendada, mas sua ativação depende da execução autorizada do W0-01.
