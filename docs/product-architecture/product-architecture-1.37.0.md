---
id: PRODUCT-ARCHITECTURE-OVERLAY-1.37.0
title: Arquitetura de Produtos — Estado Efetivo 1.37.0
status: active
version: 1.37.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - PRODUCT-ARCHITECTURE-OVERLAY-1.36.0
related:
  - PAS-001
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-W0-PLAN-001
  - M5.17
---

# Arquitetura de Produtos — Estado Efetivo 1.37.0

> Este overlay preserva a Arquitetura de Produtos vigente e registra o planejamento executável da Onda 0 da UIC-01.

## 1. Estado corrente

| Elemento | Estado |
|---|---|
| PAS-001 — Guivos Journey | Published 1.0.0 |
| Mapa Final de Capacidades | 1.0.1 |
| Engineering Handoff | Draft 0.6.0 efetivo |
| UIC-01 | Draft 0.6.0 |
| Estado da UIC-01 | Wave 0 implementation planned |
| Readiness arquitetural | 100% |
| Implementação | não iniciada |
| Marco | M5.17 |

## 2. Autoridades adicionadas

- plano executável da Onda 0;
- backlog de 80 histórias;
- plano das 16 dependências;
- ambientes e integração;
- seis provas técnicas;
- plano das 18 evidências;
- registro de riscos e interrupções;
- registro de dez decisões tecnológicas;
- UIC-01 0.6.0;
- Engineering Handoff 0.6.0.

## 3. Interpretação obrigatória

- `Wave 0 implementation planned` não equivale a implementação iniciada;
- 100% refere-se ao readiness arquitetural da UIC-01;
- backlog não cria autoridade normativa;
- dossier tecnológico não é ADR aceito;
- POC não é produção;
- ambiente Internal Trial não é produção;
- owner lógico não é owner nominal;
- dependência não implica microsserviço;
- evidência planejada não é evidência produzida.

## 4. Sequência autorizável

Após decisão separada:

1. W0-01 — Fundação do projeto;
2. ADRs tecnológicos bloqueantes;
3. W0-02 — Núcleo de domínio;
4. W0-03 — Contratos e persistência;
5. W0-04 a W0-06 conforme dependências;
6. W0-07 — Segurança e resiliência;
7. W0-08 — Gates e conclusão.

Nenhuma etapa é iniciada automaticamente por este overlay.

## 5. Outras UICs

UIC-02 a UIC-09 permanecem em `Normative sources mapped — 20%`. O avanço da UIC-01 não autoriza evolução paralela silenciosa das demais.

## 6. Gaps

- gaps arquiteturais UIC01-GAP-001 a 010 permanecem encerrados;
- descobertas de implementação usarão `UIC01-IMP-GAP-###`;
- novo gap não poderá alterar decisão funcional sem processo próprio.

## 7. Próximo ponto

> Propor execução controlada de W0-01, com owners nominais, local de implementação, pipeline mínimo, política de dados sintéticos e governança de evidências.

## 8. Não autorizado

- código ou POC sem aprovação específica;
- produção;
- lançamento;
- uso de dados reais;
- contratação automática;
- escolha tecnológica sem ADR quando permanente;
- expansão da Intelligence;
- reabertura silenciosa de arquitetura funcional.