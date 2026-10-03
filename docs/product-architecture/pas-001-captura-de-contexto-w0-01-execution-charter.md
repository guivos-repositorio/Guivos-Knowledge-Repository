---
id: PAS-001-CC-W0-01-CHARTER-001
title: Charter de Execução Controlada do W0-01 — Fundação do Projeto
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-PLAN-001
related:
  - PAS-001-CC-W0-BACKLOG-001
  - PAS-001-CC-W0-DEPENDENCY-001
  - PAS-001-CC-W0-EVIDENCE-001
  - PAS-001-CC-W0-RISK-001
  - PAS-001-CC-W0-TECH-DECISIONS-001
---

# PAS-001-CC-W0-01-CHARTER-001 — Charter de Execução Controlada do W0-01

> **Estado:** pacote documental definido. A execução permanece não autorizada e bloqueada até a atribuição dos owners nominais obrigatórios e uma decisão separada de início.

## 1. Objetivo

Preparar a fundação técnica e de governança necessária para que o W0-02 possa iniciar sem reinterpretar autoridade, escopo, segurança, evidências ou decisões tecnológicas.

O W0-01 estabelece:

- local oficial da implementação;
- estrutura lógica inicial;
- owners e aprovadores;
- estratégia de branches e revisão;
- pipeline mínimo;
- política de dados sintéticos;
- inventário de segredos e credenciais;
- padrão de evidências;
- registro de riscos, exceções e interrupções;
- priorização dos ADRs bloqueantes;
- validação das dependências `required_before_build`.

## 2. Histórias abrangidas

| História | Resultado do W0-01 |
|---|---|
| W0-01-ST-001 | estrutura de implementação e módulos lógicos definida |
| W0-01-ST-002 | convenções de branch, commit, versão e release definidas |
| W0-01-ST-003 | contrato do pipeline mínimo definido |
| W0-01-ST-004 | matriz de owners e aprovadores definida |
| W0-01-ST-005 | template versionado de evidência definido |
| W0-01-ST-006 | registro de riscos, exceções e interrupções definido |
| W0-01-ST-007 | política de dados sintéticos definida |
| W0-01-ST-008 | requisitos do inventário de segredos definidos |
| W0-01-ST-009 | método de validação das dependências anteriores ao build definido |

A conclusão documental dessas histórias não equivale à sua execução técnica.

## 3. Modelo de autorização

### 3.1 Decisão A — Formalização documental

Autoriza apenas:

- publicação dos contratos do W0-01 no GKR;
- definição de papéis, checks, templates e critérios;
- registro de bloqueios e pré-condições;
- preparação da decisão de execução.

### 3.2 Decisão B — Execução controlada

Exige nova aprovação específica e poderá autorizar:

- criação do repositório privado de implementação;
- configuração de proteções;
- criação da estrutura inicial;
- pipeline e verificações;
- fixtures sintéticas;
- produção de EV-017 e EV-018.

A Decisão B não autoriza W0-02, POCs, ambientes integrados, dados reais, Internal Trial ou produção.

## 4. Local oficial proposto

| Repositório | Responsabilidade |
|---|---|
| `Guivos-Knowledge-Repository` | autoridade normativa, arquitetura, decisões, marcos e consolidação |
| `Guivos-Capture-Context` | código, contratos executáveis, testes, fixtures, pipeline e evidências técnicas |

O segundo repositório deverá ser privado e somente poderá ser criado após a Decisão B.

## 5. Estrutura lógica inicial

A Onda 0 deverá começar como monólito modular, sem transformar cada capacidade em microsserviço e sem declarar topologia definitiva de produção.

```text
Guivos-Capture-Context/
├── .github/
├── docs/
│   ├── adr/
│   ├── decisions/
│   ├── risks/
│   ├── exceptions/
│   └── runbooks/
├── contracts/
│   ├── commands/
│   ├── responses/
│   ├── events/
│   └── schemas/
├── src/
│   ├── domain/
│   ├── application/
│   ├── interfaces/
│   └── infrastructure/
├── tests/
├── fixtures/synthetic/
├── evidence/
└── scripts/
```

A linguagem, runtime e framework dependem do ADR-TCC-001.

## 6. Pacotes de trabalho

### W0-01A — Governança

- atribuir owners nominais;
- definir aprovadores;
- configurar CODEOWNERS;
- atribuir autoridade de interrupção;
- validar riscos high e critical.

### W0-01B — Decisões bloqueantes

- concluir ADR-TCC-001;
- concluir ADR-TCC-006;
- aprovar o recorte inicial de ADR-TCC-008;
- aprovar o recorte inicial de ADR-TCC-010;
- preparar ADR-TCC-002 e ADR-TCC-004.

### W0-01C — Fundação do repositório

- criar repositório privado após autorização;
- proteger `main`;
- criar templates e estrutura lógica;
- vincular requisitos e decisões ao GKR.

### W0-01D — Pipeline e dados

- implementar checks independentes da stack;
- implementar checks da stack escolhida;
- criar catálogo sintético;
- configurar varredura de segredos;
- registrar credenciais por ambiente.

### W0-01E — Evidências e encerramento

- produzir EV-017 e EV-018;
- comprovar as nove histórias;
- revalidar riscos e dependências;
- emitir decisão separada de encerramento.

## 7. Critérios de entrada para execução

A execução do W0-01 somente poderá ser autorizada quando:

- Architecture Owner nominal estiver atribuído;
- Engineering Owner nominal estiver atribuído;
- Security & Privacy Owner nominal estiver atribuído;
- Quality & Evidence Owner nominal estiver atribuído;
- Platform/DevOps Owner nominal ou responsável provisório aprovado estiver atribuído;
- repositório privado proposto estiver aprovado;
- política de branches estiver aprovada;
- contrato do pipeline estiver aprovado;
- política de dados sintéticos estiver aprovada;
- template de evidência estiver aprovado;
- ADR-TCC-001 e ADR-TCC-006 possuírem plano de decisão executável;
- riscos critical possuírem autoridade de tratamento.

## 8. Critérios de conclusão

O W0-01 somente estará concluído quando:

1. as nove histórias estiverem executadas;
2. owners obrigatórios estiverem nominalmente atribuídos;
3. repositório privado e proteções estiverem configurados;
4. push direto em `main` estiver impedido;
5. pipeline mínimo estiver obrigatório;
6. varredura de segredos estiver ativa;
7. catálogo sintético estiver versionado;
8. ADR-TCC-001 e ADR-TCC-006 estiverem aceitos;
9. recortes de ADR-TCC-008 e ADR-TCC-010 estiverem aprovados;
10. EV-017 e EV-018 forem reproduzíveis;
11. riscos high e critical possuírem owner e tratamento;
12. nenhuma exceção estiver sem validade;
13. produção permanecer fora do escopo;
14. W0-02 depender de decisão separada.

## 9. Gatilhos de interrupção

Interromper o fluxo afetado quando houver:

- repositório público por erro;
- dado pessoal real em fixture;
- segredo em commit, log ou artefato;
- owner obrigatório ausente na execução;
- tentativa de iniciar domínio sem ADR-TCC-001;
- fallback sem expiração ou owner;
- pipeline ignorável;
- PR sem requisito, risco ou evidência prevista;
- alteração de autoridade normativa;
- execução de POC ou ambiente integrado sem autorização;
- evidência não reproduzível.

## 10. Limites

Este charter não autoriza:

- criar o repositório de implementação;
- realizar commit de código;
- selecionar fornecedor automaticamente;
- provisionar ambientes;
- executar POCs;
- usar dados pessoais reais;
- iniciar W0-02;
- realizar Internal Trial;
- produzir ou lançar publicamente.
