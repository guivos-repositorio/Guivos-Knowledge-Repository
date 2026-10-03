---
id: CHANGELOG-0.66.0-UIC-01-W0-01-CHARTER
title: Changelog 0.66.0 — Charter de Execução do W0-01
status: active
version: 0.66.0
owner: Guivos
last_updated: 2026-07-20
related:
  - PAS-001-CC-UIC-001-OVERLAY-0.7.0
  - PAS-001-CC-W0-01-CHARTER-001
  - M5.18
---

# Changelog 0.66.0 — Charter de Execução do W0-01

## Added

- charter de execução controlada do W0-01;
- matriz de owners e aprovadores;
- RACI e regras de segregação;
- proposta do repositório privado `Guivos-Capture-Context`;
- estratégia de branches, PRs, commits, versões e tags;
- contrato do pipeline mínimo;
- checks independentes e dependentes da stack;
- política de logs, artefatos e exceções;
- política de dados sintéticos;
- proibição de uso da VAL-002 como fixture;
- contrato de EV-017 e EV-018;
- plano de ADRs bloqueantes;
- checklist de autorização e encerramento;
- UIC-01 0.7.0;
- Engineering Handoff 0.7.0;
- Product Architecture 1.38.0;
- Roadmap 11.19.0;
- Knowledge Board 11.19.0;
- Architectural Milestones 4.17.0;
- Matriz de Consolidação 1.38.0.

## Changed

- ponto de retomada de planejamento genérico para atribuição nominal e autorização controlada do W0-01;
- marco de M5.17 para M5.18;
- estado da UIC-01 para `charter defined; execution blocked`.

## Clarified

- charter definido não significa execução autorizada;
- Guilherme Oliveira é owner nominal de patrocínio, produto e governança, não substituto automático dos papéis técnicos;
- owners técnicos não foram inventados;
- execução permanece em 0%;
- repositório de código permanece não criado;
- GitHub Actions é recomendação inicial, não infraestrutura definitiva;
- monólito modular é ponto de partida da Onda 0, não arquitetura final;
- EV-017/018 continuam não produzidas;
- W0-02 requer decisão separada.

## Preserved

- PAS-001 1.0.0;
- Mapa Final 1.0.1;
- UIC-01 0.1.0 a 0.6.0;
- dez gaps arquiteturais encerrados;
- plano W0-01 a W0-08;
- UIC-02 a UIC-09 em 20%;
- GLPA-001 1.1.1;
- GIA-000 1.3.0;
- programa VAL;
- VAL-002 2.1.0;
- limites de autoridade, segurança e privacidade.

## Not authorized

- criar `Guivos-Capture-Context`;
- configurar branch protection ou pipeline;
- produzir código;
- aceitar ADR sem owners competentes;
- executar POC;
- provisionar ambiente;
- usar dado real;
- iniciar W0-02;
- Internal Trial;
- produção ou lançamento.

## Next

Atribuir Architecture Owner, Engineering Owner, Security & Privacy Owner, Quality & Evidence Owner e Platform/DevOps Owner. Depois, submeter decisão específica para autorizar exclusivamente a execução das nove histórias do W0-01.
