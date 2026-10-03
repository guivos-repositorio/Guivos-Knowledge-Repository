---
id: PAS-001-CC-UIC-001-OVERLAY-0.6.0
title: Captura de Contexto — Unidade de Engenharia 0.6.0
status: draft
version: 0.6.0
owner: Guivos
last_updated: 2026-07-19
normative: true
parent: PAS-001-CC-UIC-001
supersedes_partial:
  - PAS-001-CC-UIC-001-OVERLAY-0.5.0
related:
  - PAS-001-CC-W0-PLAN-001
  - PAS-001-CC-W0-BACKLOG-001
  - PAS-001-CC-W0-DEPENDENCY-001
  - PAS-001-CC-W0-ENV-001
  - PAS-001-CC-W0-POC-001
  - PAS-001-CC-W0-EVIDENCE-001
  - PAS-001-CC-W0-RISK-001
  - PAS-001-CC-W0-TECH-DECISIONS-001
---

# PAS-001-CC-UIC-001 — Unidade de Engenharia 0.6.0

> **Estado efetivo proposto:** `Draft 0.6.0 — Wave 0 implementation planned`.
>
> Este overlay preserva integralmente as autoridades 0.1.0 a 0.5.0. Prevalece somente sobre estado de planejamento, marco, backlog de execução e ponto de retomada.

## 1. Estado

| Dimensão | Estado |
|---|---|
| Fundação normativa | concluída |
| Modelo de domínio | definido para implementação |
| Lifecycle | definido para implementação |
| Contratos e schemas | tecnicamente propostos |
| Storage, índice, guardrails, NFR e segurança | tecnicamente definidos |
| Readiness arquitetural | 100% |
| Planejamento da Onda 0 | concluído |
| Implementação da Onda 0 | não iniciada |
| Produção | não autorizada |

## 2. Incremento concluído

O ciclo adiciona:

- plano executável em oito incrementos;
- backlog de 80 histórias verificáveis;
- classificação das 16 dependências;
- seis ambientes não produtivos;
- estratégia de integração;
- seis POCs obrigatórias ou condicionais;
- plano das 18 evidências;
- registro inicial de 20 riscos;
- critérios de interrupção e retomada;
- registro de dez dossiers tecnológicos;
- critérios do marco M5.17.

## 3. Estado de maturidade

`Wave 0 implementation planned` significa:

- equipe pode transformar o plano em execução após autorização separada;
- ADRs tecnológicos bloqueantes estão identificados;
- histórias possuem critérios e evidências;
- dependências possuem momento de necessidade;
- ambientes e POCs estão especificados;
- gates possuem responsabilidade lógica;
- riscos e interrupções estão governados.

Não significa:

- código implementado;
- tecnologia escolhida;
- POC executada;
- gate aprovado;
- uso de dados reais;
- Internal Trial autorizado;
- produção ou lançamento autorizados.

## 4. Incrementos planejados

| Incremento | Conteúdo | Evidências prioritárias |
|---|---|---|
| W0-01 | fundação, owners, pipeline e governança | EV-017/018 |
| W0-02 | núcleo de domínio | EV-001/002 |
| W0-03 | contratos, persistência e eventos | EV-003/007/015 |
| W0-04 | dados protegidos e mídia mínima | EV-008/009/016 |
| W0-05 | acesso, correção e revogação | EV-004/006/012/014 |
| W0-06 | busca protegida mínima | EV-010 |
| W0-07 | segurança, observabilidade e resiliência | EV-005/011/013 |
| W0-08 | fechamento dos cinco gates | EV-001 a EV-018 |

## 5. Dependências

As 16 dependências foram classificadas como:

- `required_before_build`;
- `required_before_integration`;
- `required_before_security_gate`;
- `required_before_operational_trial`;
- `required_before_production`;
- `optional_for_wave_0`.

Capacidade continua não equivalendo a microsserviço ou produto obrigatório.

## 6. Decisões tecnológicas

Dez dossiers estão identificados:

1. linguagem e framework;
2. persistência funcional;
3. conteúdo e object storage;
4. eventos e mensageria;
5. busca e vetores;
6. identidade, autorização e políticas;
7. chaves, segredos e criptografia;
8. observabilidade;
9. modelos e Intelligence;
10. infraestrutura e implantação.

Decisão permanente exige ADR após evidência suficiente.

## 7. Gaps

Não existem gaps arquiteturais reabertos. Descobertas de implementação deverão receber novos identificadores, por exemplo `UIC01-IMP-GAP-###`, e não alterar silenciosamente `UIC01-GAP-001` a `010`.

## 8. Marco

> `M5.17 — Capture Context Wave 0 Implementation Planned`

## 9. Condições para executar

A execução depende de autorização separada e de:

- backlog priorizado;
- owners nominais;
- ADRs bloqueantes decididos;
- dependências `required_before_build` disponíveis;
- ambientes mínimos preparados;
- riscos críticos tratados;
- plano de evidências aceito;
- produção explicitamente fora do escopo.

## 10. Ponto de retomada

> Propor a autorização e a estratégia de execução controlada do incremento W0-01, sem iniciar automaticamente ADRs, POCs ou código.

## 11. Limites preservados

- acesso técnico não equivale a autoridade funcional;
- Intelligence não confirma nem autoriza;
- conteúdo capturado é dado, não instrução de sistema;
- índice não é sistema de registro;
- correção e revogação exigem comprovação;
- POC não é produção;
- conclusão do planejamento não autoriza execução.