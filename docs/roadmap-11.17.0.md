---
id: ROADMAP-OVERLAY-11.17.0
title: Roadmap Arquitetural — Estado Efetivo 11.17.0
status: active
version: 11.17.0
owner: Guivos
last_updated: 2026-07-19
supersedes_partial:
  - ROADMAP-OVERLAY-11.16.0
related:
  - PAS-001-ENGINEERING-HANDOFF-001
  - PAS-001-CC-UIC-001
  - PAS-001-CC-UIC-READINESS-001
  - M5.16
---

# Roadmap Arquitetural — Estado Efetivo 11.17.0

> O Roadmap-base permanece preservado. Este overlay prevalece sobre estado corrente, marco vigente, backlog prioritário e ponto de retomada.

## Estado atual

| Frente | Estado |
|---|---|
| Arquitetura funcional do Journey | Publicada e concluída |
| Engineering Handoff | Draft 0.5.0 efetivo |
| UIC-01 — Captura de Contexto | Draft 0.5.0 |
| Estado técnico da UIC-01 | Technically ready for implementation |
| Progresso | 100% |
| Marco vigente | M5.16 — Capture Context Technically Ready for Implementation |
| Frente operacional | Product Engineering |

## Entrega concluída

- domínio, lifecycle, contratos e schemas;
- armazenamento multimodal;
- retenção, exclusão, backup e restore;
- busca e indexação sensível;
- embeddings e derivados;
- 30 guardrails técnicos;
- matriz de atores, autoridades e estados;
- NFRs e SLOs candidatos;
- threat model com 26 ameaças;
- estratégia de testes e evidências;
- gates da Onda 0;
- cinco ADRs lógicos;
- resolução dos dez gaps da UIC-01.

## Progressão técnica

| Etapa | Estado | Progresso |
|---|---|---:|
| Fundação normativa | concluída | 20% |
| Modelo de domínio | concluído | 40% |
| Ciclo técnico | concluído | 60% |
| Contratos técnicos | concluídos | 80% |
| Prontidão técnica | definida | 100% |

## Backlog prioritário

### P0 — Planejamento da Onda 0

1. decompor autoridades em épicos, capacidades e histórias;
2. classificar as 16 dependências mínimas;
3. definir ambientes e estratégia de integração;
4. planejar provas técnicas de persistência, mídia, busca e mensageria;
5. definir instrumentação dos SLIs;
6. definir responsáveis pelos gates;
7. estabelecer sequência de implementação;
8. definir evidências por incremento;
9. definir estratégia de rollout interno;
10. registrar critérios de interrupção.

### P1 — ADRs tecnológicos

- linguagem e framework;
- persistência funcional;
- armazenamento de objetos;
- busca e vetores;
- mensageria;
- identidade e políticas;
- chaves e segredos;
- observabilidade;
- modelos e Intelligence;
- implantação.

### P2 — Execução da Onda 0

- implementar núcleo do agregado;
- implementar contratos e schemas;
- implementar conteúdo protegido;
- implementar correção e revogação;
- implementar consumidores mínimos;
- implementar busca protegida mínima;
- executar gates;
- produzir evidências.

## Gaps

Não permanecem gaps arquiteturais abertos na UIC-01. Novos gaps descobertos durante implementação deverão possuir novo identificador e não reabrir silenciosamente gaps encerrados.

## Próximo marco candidato

> `M5.17 — Capture Context Wave 0 Implementation Planned`

Condição: backlog executável, ADRs tecnológicos prioritários, dependências classificadas, ambientes definidos, responsáveis atribuídos e plano de evidências aprovado.

## Ponto exato de retomada

> Elaborar o plano executável da Onda 0 da Captura de Contexto.

## Limites

Readiness técnico não autoriza produção, lançamento, contratação automática de tecnologia ou flexibilização de segurança e privacidade.