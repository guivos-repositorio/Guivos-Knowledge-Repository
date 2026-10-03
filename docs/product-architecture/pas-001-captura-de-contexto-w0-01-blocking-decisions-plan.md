---
id: PAS-001-CC-W0-01-DECISIONS-001
title: Plano de Decisões Bloqueantes do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-CHARTER-001
related:
  - PAS-001-CC-W0-TECH-DECISIONS-001
  - PAS-001-CC-W0-01-OWNERS-001
  - PAS-001-CC-W0-01-PIPELINE-001
---

# PAS-001-CC-W0-01-DECISIONS-001 — Plano de Decisões Bloqueantes

## 1. Objetivo

Ordenar as decisões tecnológicas necessárias para executar o W0-01 e preparar o W0-02, sem escolher fornecedor ou stack neste ciclo documental.

## 2. Classes

- `P0-W0-01`: necessária para executar ou encerrar W0-01;
- `P0-W0-02`: necessária antes do build do domínio;
- `P1-W0-03`: preparar durante W0-01, decidir antes de persistência e integração;
- `later`: não bloqueia W0-01.

## 3. Matriz

| ADR | Tema | Prioridade | Estado requerido ao encerrar W0-01 |
|---|---|---|---|
| ADR-TCC-001 | linguagem e framework | P0-W0-02 | accepted |
| ADR-TCC-006 | identidade, autorização e políticas | P0-W0-02 | accepted |
| ADR-TCC-008 | observabilidade | P0-W0-01 | recorte inicial accepted; stack completa proposed |
| ADR-TCC-010 | infraestrutura e implantação | P0-W0-01 | recorte Local/Test/GitHub accepted |
| ADR-TCC-002 | persistência funcional | P1-W0-03 | research plan approved |
| ADR-TCC-004 | eventos e mensageria | P1-W0-03 | research plan approved |
| ADR-TCC-003 | conteúdo e object storage | later | identified/poc_required |
| ADR-TCC-005 | busca e vetores | later | identified/poc_required |
| ADR-TCC-007 | chaves e criptografia | later | researching |
| ADR-TCC-009 | modelos e Intelligence | later | deferred, salvo decisão de inclusão |

## 4. ADR-TCC-001 — Linguagem e framework

### Decisão mínima

- linguagem;
- runtime;
- framework de aplicação;
- framework de testes;
- abordagem de schemas;
- padrão de módulos;
- gerenciamento de dependências;
- versão suportada.

### Critérios eliminatórios

A opção é rejeitada se:

- não sustentar invariantes e tipagem adequadas;
- dificultar testes determinísticos;
- depender de serialização sem controle;
- impedir análise estática suficiente;
- impor microsserviços;
- criar risco operacional incompatível;
- não possuir estratégia de atualização e suporte.

### Método

Matriz ponderada e spike limitado, sem POC distribuída e sem dados reais.

## 5. ADR-TCC-006 — Identidade, autorização e políticas

### Decisão mínima

- contrato de identidade opaca;
- separação entre ator e participante;
- representação e validade;
- finalidade e escopo;
- decisão de política;
- explicabilidade mínima;
- fallback local para W0-02;
- auditoria minimizada.

### Critérios eliminatórios

Rejeitar opção que:

- trate autenticação como confirmação humana;
- permita autoridade implícita;
- não represente finalidade e validade;
- não bloqueie representação expirada;
- não permita teste determinístico de permitido/negado;
- exija dado real para funcionar.

## 6. ADR-TCC-008 — Recorte inicial de observabilidade

O W0-01 deverá decidir:

- formato de log estruturado;
- campos proibidos;
- correlação opaca;
- retenção de Local/Test;
- exportação de evidências;
- redaction e scanning;
- owner de configuração.

A stack completa de observabilidade pode permanecer `proposed` até W0-07.

## 7. ADR-TCC-010 — Recorte inicial de infraestrutura

O W0-01 deverá decidir:

- GitHub como local de implementação;
- repositório privado separado;
- GitHub Actions como CI inicial proposto;
- ambientes Local e Test;
- política de branches;
- gestão inicial de segredos;
- artefatos e retenção;
- rollback de workflows.

Não deverá decidir topologia de produção, multi-região, Internal Trial ou operação comercial.

## 8. Preparação de ADR-TCC-002 e ADR-TCC-004

Durante W0-01, produzir:

- requisitos;
- opções candidatas;
- critérios eliminatórios;
- POCs necessárias;
- riscos;
- owner;
- momento de decisão;
- custo de reversão.

Nenhum mecanismo de banco, event store, broker ou outbox é aceito automaticamente.

## 9. Método de decisão

Cada ADR deverá conter:

1. contexto;
2. requisitos normativos;
3. opções;
4. critérios e pesos;
5. critérios eliminatórios;
6. evidências;
7. decisão;
8. consequências positivas e negativas;
9. riscos;
10. reversão ou migração;
11. revisão;
12. owner e aprovador.

Pontuação alta não compensa violação de autoridade, isolamento, revogação, auditabilidade ou segurança.

## 10. Sequência

```text
owners nominais
  ↓
ADR-TCC-001 + ADR-TCC-006
  ↓
recortes ADR-TCC-008 + ADR-TCC-010
  ↓
estrutura e pipeline
  ↓
planos ADR-TCC-002 + ADR-TCC-004
  ↓
EV-018 e decisão de encerramento
```

## 11. Bloqueios

- sem Architecture Owner: nenhum ADR pode ser aceito;
- sem Engineering Owner: ADR-TCC-001 não pode ser recomendado;
- sem Security/Privacy Owner: ADR-TCC-006/008/010 não pode ser aceito;
- sem Quality/Evidence Owner: método e evidências não podem ser aprovados;
- sem decisão formal: implementação não começa;
- preferência pessoal, popularidade ou ferramenta já conhecida não constituem evidência suficiente.

## 12. Critérios de aceite

O plano estará executado quando:

- ADR-TCC-001 e ADR-TCC-006 estiverem accepted;
- recortes iniciais de ADR-TCC-008 e ADR-TCC-010 estiverem accepted;
- ADR-TCC-002 e ADR-TCC-004 possuírem planos aprovados;
- owners e aprovadores forem nominais;
- decisões estiverem vinculadas a requisitos e riscos;
- EV-018 contiver hashes e revisão;
- nenhuma decisão autorizar produção.

## 13. Limites

Este documento ordena decisões. Não seleciona TypeScript, JVM, .NET, Go, banco, broker, nuvem, provedor de identidade ou ferramenta de observabilidade.
