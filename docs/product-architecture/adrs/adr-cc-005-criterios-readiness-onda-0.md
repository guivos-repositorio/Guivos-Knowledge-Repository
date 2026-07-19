---
id: ADR-CC-005
title: Critérios de Readiness da Onda 0
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-07-19
normative: true
related:
  - PAS-001-CC-UIC-READINESS-001
  - PAS-001-CC-UIC-NFR-SECURITY-001
---

# ADR-CC-005 — Critérios de Readiness da Onda 0

## Status

`Proposed 0.1.0`.

## Contexto

A classificação `Technically ready for implementation` pode ser interpretada incorretamente como código pronto, segurança comprovada ou produção autorizada. A Onda 0 precisa de gates verificáveis que separem definição arquitetural, implementação, evidência e go-live.

## Decisão

Adotar cinco gates independentes:

1. domínio;
2. dados;
3. segurança;
4. qualidade;
5. governança.

Cada item obrigatório deverá estar `passed` ou `accepted_exception`. Itens `failed`, `not_measured` ou com evidência expirada bloqueiam o gate.

## Significados

### Ready for implementation

Autoridades, contratos, riscos, testes e decisões lógicas suficientes para iniciar construção.

### Onda 0 concluída

Implementação mínima existente, gates executados e evidências reais produzidas.

### Ready for production

Decisão futura, separada, que exige critérios operacionais, jurídicos, segurança, privacidade e produto adicionais.

## Regras

- um gate não compensa falha de outro;
- documento não substitui evidência;
- ausência de incidente não comprova controle;
- exceção possui risco, mitigação, responsável, aprovador e expiração;
- risco residual é explicitado;
- SLO candidato precisa ser medido;
- decisão tecnológica exige ADR posterior;
- go-live nunca é implícito.

## Consequências positivas

- evita avanço por percepção subjetiva;
- cria rastreabilidade entre requisito, teste e evidência;
- separa arquitetura de operação;
- torna exceções temporárias e auditáveis;
- permite planejamento objetivo da Onda 0.

## Consequências negativas

- aumenta trabalho de evidência;
- pode retardar pilotos sem preparação;
- exige ownership claro;
- depende de instrumentação e ambientes representativos.

## Alternativas rejeitadas

### Checklist único sem gates

Rejeitado por permitir compensação indevida entre áreas críticas.

### Aprovação exclusivamente arquitetural

Rejeitada porque segurança, dados e operação precisam de evidências próprias.

### Considerar 100% como produção

Rejeitada por confundir definição lógica com implementação comprovada.

## Evidências requeridas

- matriz de testes;
- matriz de evidências;
- relatórios de carga e recuperação;
- testes de segurança e privacidade;
- registro de riscos;
- exceções aprovadas;
- ADRs tecnológicos quando aplicáveis;
- decisão formal da próxima onda.

## Decisões posteriores

Critérios específicos de piloto, beta, produção, rollout e rollback deverão ser definidos após a implementação da Onda 0.